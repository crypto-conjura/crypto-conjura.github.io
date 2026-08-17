#!/usr/bin/env python3
"""Turn the PDFs in latex/harvest/ into conjecture drafts, one folder each.

Drop papers into `latex/harvest/`, run this, and each one is read for the
open problems it actually poses, each promoted problem is written out as a
`latex/conjectures/<slug>/statement.tex` in the Conjura house style, and the
PDF is moved to `latex/harvest/processed/` so it is never read twice:

    python3 scripts/harvest_conjectures.py                # everything waiting
    python3 scripts/harvest_conjectures.py --dry-run      # what would be read
    python3 scripts/harvest_conjectures.py --limit 1      # one paper
    python3 scripts/harvest_conjectures.py --report       # what has been done

The interesting question is not how to get a model to write a plausible
conjecture from a paper -- that is easy, and that is the problem. It is how
to stop it writing a plausible conjecture the paper does not contain. A
model reading a forty-page paper will cheerfully hand back an open problem
that is a strengthening of a theorem the paper proves, or a question the
authors answered in Section 6, or a synthesis of two remarks that no one has
ever posed, and all three read exactly like the real thing. So the pipeline
is arranged so that the model's claims are *checked*, and mostly not by
another model:

  1. Extract      One call, constrained to a schema, against the whole PDF.
                  Every candidate must carry verbatim quotes, with page
                  numbers, for its statement and for its openness.

  2. Ground       Not a model call. Every quote is checked against the PDF's
                  own text layer, after undoing the damage extraction does
                  (ligatures, hyphens broken across lines, curly quotes).
                  A quote that is not in the paper is not evidence, and a
                  candidate whose statement or openness quote does not
                  ground is dropped before anything is written to disk.
                  This is the load-bearing check: it is mechanical, it
                  cannot be talked round, and fabrication is exactly what it
                  catches.

  3. Verify       A second call that sees the PDF and the drafted record and
                  nothing else -- not the extractor's reasoning, not its
                  confidence -- and is asked to refute it: is this open, is
                  it stated at this strength, is any of it invented. Errors
                  decorrelate only if the checker cannot see the trace it is
                  checking, which is why the draft arrives stripped.

  4. Typeset      A third call renders the surviving record as statement.tex
                  against the conjura-conjecture class.

  5. Compile      Not a model call. pdflatex, then chktex and lacheck. A
                  statement that does not build is marked, not shipped
                  quietly.

Everything the run believed is written next to the output as `harvest.json`
and `SOURCE.md`: the quotes, their pages, whether each grounded exactly or
fuzzily, the verifier's checks, and every citation the model could not find
in the paper's own bibliography (marked `[UNVERIFIED]`, and left marked).

The model calls go through `scripts/harvest_model.py`, which can run against
the Anthropic SDK or the Claude Code CLI; the wording of the three asks is in
`prompts/harvest.md`, not here.
"""

from __future__ import annotations

import argparse
import datetime
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest_model import (  # noqa: E402
    EXTRACT_SCHEMA,
    TEX_SCHEMA,
    VERIFY_SCHEMA,
    ModelError,
    pick_backend,
)

ROOT = Path(__file__).resolve().parent.parent
HARVEST = ROOT / "latex" / "harvest"
PROCESSED = HARVEST / "processed"
CONJECTURES = ROOT / "latex" / "conjectures"
TEMPLATE = CONJECTURES / "_template"
PROMPTS = ROOT / "prompts" / "harvest.md"
LEDGER = PROCESSED / "harvest-log.json"

# A quote grounds if this much of it is found in the text layer. Exact
# substring match is the normal case; the slack below is for spans where the
# extractor mangled a symbol in the middle of otherwise plain prose.
#
# Coverage alone is too generous: a paraphrase of a real sentence shares most
# of its characters with the original and scores ~0.98 by that measure, which
# is exactly the thing this check exists to catch. So only runs of at least
# RUN characters count towards coverage, and a `near` verdict additionally
# needs one long unbroken run -- the signature of "really this sentence, with
# one symbol mangled" rather than "the same words, rearranged".
NEAR = 0.90
NEAR_RUN = 0.40
WEAK = 0.75
RUN = 12


# --------------------------------------------------------------------------
# The PDF and its text layer
# --------------------------------------------------------------------------

_LIGATURES = {
    "\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl",
    "\ufb03": "ffi", "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st",
}
_DASHES = dict.fromkeys(map(ord, "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"), "-")
_SINGLES = dict.fromkeys(map(ord, "\u2018\u2019\u201a\u201b\u2032"), "'")
_DOUBLES = dict.fromkeys(map(ord, "\u201c\u201d\u201e\u201f\u2033"), '"')


def normalize(text):
    """Fold a span to the form both sides of the grounding check agree on.

    Undoes what PDF extraction does to prose and what a typesetter does to
    punctuation, in that order: hyphenation has to go before whitespace is
    collapsed, because it is the line break that identifies it.

    Hyphens then go entirely, on both sides. Joining a word broken across
    lines turns "non-\\nuniform" into "nonuniform", which no longer matches
    the "non-uniform" a quoter copied off the page; deleting the character
    from both the needle and the haystack is the only way the two agree
    without knowing which hyphens the typesetter inserted.
    """
    text = unicodedata.normalize("NFKC", text)
    for lig, plain in _LIGATURES.items():
        text = text.replace(lig, plain)
    text = re.sub(r"(\w)[-\u2010\u2011]\s*\n\s*(\w)", r"\1\2", text)
    text = text.translate(_DASHES).translate(_SINGLES).translate(_DOUBLES)
    text = text.replace("-", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip().casefold()


class PdfDoc:
    """One harvested paper: its bytes, its pages, and its text layer."""

    def __init__(self, path):
        self.path = Path(path)
        self.size = self.path.stat().st_size
        self.sha256 = hashlib.sha256(self.path.read_bytes()).hexdigest()
        self.page_text = self._extract()
        self.pages = len(self.page_text)
        self.norm_pages = [normalize(p) for p in self.page_text]
        self.norm_all = " ".join(self.norm_pages)
        # Where each page starts in norm_all, so a hit can be named a page.
        self.page_starts, at = [], 0
        for p in self.norm_pages:
            self.page_starts.append(at)
            at += len(p) + 1

    def _extract(self):
        proc = subprocess.run(
            ["pdftotext", "-layout", str(self.path), "-"],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"pdftotext failed on {self.path.name}: {proc.stderr.strip()}")
        # pdftotext separates pages with a form feed.
        return proc.stdout.split("\f")[:-1] or [proc.stdout]

    def has_text_layer(self):
        return sum(len(p.split()) for p in self.page_text) > 200

    def marked_text(self):
        return "\n\n".join(
            f"[[page {i}]]\n{p}" for i, p in enumerate(self.page_text, 1)
        )

    def page_at(self, offset):
        page = 1
        for i, start in enumerate(self.page_starts, 1):
            if start <= offset:
                page = i
            else:
                break
        return page

    # -- grounding ---------------------------------------------------------

    def ground(self, quote, claimed_page):
        """Locate `quote` in the paper. Never raises; always returns a verdict.

        Returns a dict with `status` in exact / near / weak / ungrounded /
        too-short, the coverage achieved, and the page it was actually found
        on so a wrong page number shows up as its own finding.
        """
        needle = normalize(quote)
        out = {
            "quote": quote,
            "claimed_page": claimed_page,
            "found_page": None,
            "coverage": 0.0,
            "longest_run": 0.0,
            "status": "ungrounded",
        }
        if len(needle) < 24:
            out["status"] = "too-short"
            return out

        # Exact first, on the claimed page, then anywhere.
        if 1 <= claimed_page <= self.pages:
            at = self.norm_pages[claimed_page - 1].find(needle)
            if at >= 0:
                out.update(status="exact", coverage=1.0, found_page=claimed_page)
                return out
        at = self.norm_all.find(needle)
        if at >= 0:
            out.update(status="exact", coverage=1.0, found_page=self.page_at(at))
            return out

        coverage, longest, offset = self._best_window(needle)
        out["coverage"] = round(coverage, 3)
        out["longest_run"] = round(longest, 3)
        if offset is not None:
            # The window starts before the match to give the anchor room, so
            # take the page from its middle; a fuzzy hit's page is approximate.
            out["found_page"] = self.page_at(offset + len(needle) // 2)
        if coverage >= NEAR and longest >= NEAR_RUN:
            out["status"] = "near"
        elif coverage >= WEAK:
            out["status"] = "weak"
        return out

    def _best_window(self, needle):
        """How much of `needle` appears in the paper, and in how long a run.

        Anchored rather than swept: a handful of shingles taken from across
        the quote say where to look, and only those neighbourhoods are scored.
        A quote whose every shingle is absent is not in the paper at all, and
        the coarse sweep that follows exists only to say so cheaply.

        Two numbers come back because one is not enough. Coverage says how
        much of the quote is present; the longest run says whether it is
        present *as this sentence*. A paraphrase scores high on the first and
        low on the second, which is the whole distinction being drawn.
        """
        hay, n = self.norm_all, len(needle)
        offsets = set()
        for cut in (0.1, 0.35, 0.6, 0.85):
            start = int(n * cut)
            anchor = needle[start:start + 16]
            if len(anchor) < 16:
                continue
            at = hay.find(anchor)
            while at >= 0 and len(offsets) < 64:
                offsets.add(max(0, at - start - 32))
                at = hay.find(anchor, at + 1)
        if not offsets:
            offsets = range(0, max(1, len(hay) - n), max(1, n // 2))

        best, best_run, where = 0.0, 0.0, None
        for off in offsets:
            window = hay[off:off + n + 64]
            blocks = [
                b for b in difflib.SequenceMatcher(
                    None, needle, window, autojunk=False
                ).get_matching_blocks() if b.size >= RUN
            ]
            if not blocks:
                continue
            score = sum(b.size for b in blocks) / n
            if score > best:
                best = score
                best_run = max(b.size for b in blocks) / n
                where = off
            if best >= 0.999:
                break
        return best, best_run, where


# --------------------------------------------------------------------------
# Prompts
# --------------------------------------------------------------------------

def load_prompts():
    """Pull the delimited prompt blocks out of prompts/harvest.md."""
    if not PROMPTS.exists():
        raise SystemExit(f"missing prompt file: {PROMPTS.relative_to(ROOT)}")
    text = PROMPTS.read_text(encoding="utf-8")
    found = dict(
        re.findall(
            r"<!-- prompt:([a-z.\-]+) -->\n(.*?)\n<!-- /prompt:\1 -->",
            text,
            re.S,
        )
    )
    need = {
        "extract.system", "extract.user",
        "verify.system", "verify.user",
        "tex.system", "tex.user",
    }
    missing = need - set(found)
    if missing:
        raise SystemExit(
            f"{PROMPTS.relative_to(ROOT)} is missing prompt blocks: "
            + ", ".join(sorted(missing))
        )
    return found


def fill(template, **fields):
    """Substitute <<NAME>> markers. Not str.format: the payloads are LaTeX."""
    for key, value in fields.items():
        template = template.replace(f"<<{key}>>", str(value))
    return template


# --------------------------------------------------------------------------
# Checking a candidate
# --------------------------------------------------------------------------

REQUIRED_FIELDS = ("slug", "title", "informal", "formal_statement_latex", "quotes")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def check_candidate(cand, doc, strict=True):
    """Ground every quote and decide whether the candidate survives.

    Returns (ok, grounding_records, reasons_it_failed).
    """
    reasons, records = [], []

    for field in REQUIRED_FIELDS:
        if not cand.get(field):
            reasons.append(f"empty required field: {field}")
    slug = cand.get("slug", "")
    if slug and not SLUG_RE.match(slug):
        reasons.append(f"slug is not kebab-case: {slug!r}")

    quotes = cand.get("quotes") or []
    for q in quotes:
        try:
            page = int(q.get("page") or 0)
        except (TypeError, ValueError):
            page = 0
        rec = doc.ground(q.get("text", ""), page)
        rec["role"] = q.get("role", "")
        records.append(rec)

    def worst(role):
        got = [r for r in records if r["role"] == role]
        if not got:
            return None
        order = {"exact": 3, "near": 2, "weak": 1, "ungrounded": 0, "too-short": 0}
        return max(got, key=lambda r: order[r["status"]])

    for role in ("statement", "openness"):
        best = worst(role)
        if best is None:
            reasons.append(f"no {role} quote supplied")
        elif best["status"] in ("ungrounded", "too-short"):
            reasons.append(
                f"{role} quote is not in the paper "
                f"(best coverage {best['coverage']:.0%}): {best['quote'][:90]!r}"
            )
        elif strict and best["status"] == "weak":
            reasons.append(
                f"{role} quote only weakly grounds "
                f"({best['coverage']:.0%}): {best['quote'][:90]!r}"
            )

    bad = [r for r in records if r["status"] in ("ungrounded", "too-short")]
    if records and len(bad) * 3 > len(records):
        reasons.append(f"{len(bad)} of {len(records)} quotes are not in the paper")

    for page in cand.get("pages") or []:
        if not (isinstance(page, int) and 1 <= page <= doc.pages):
            reasons.append(f"cites page {page}, but the PDF has {doc.pages}")

    return (not reasons), records, reasons


def unverified_citations(cand):
    return [
        b for b in (cand.get("bibliography") or [])
        if b.get("verified") != "printed-in-source-bibliography"
    ]


# --------------------------------------------------------------------------
# Writing the folder
# --------------------------------------------------------------------------

def find_class_files():
    cls = TEMPLATE / "conjura-conjecture.cls"
    if not cls.exists():
        raise SystemExit(f"missing {cls.relative_to(ROOT)}; cannot start a conjecture folder")
    rc = TEMPLATE / ".chktexrc"
    if not rc.exists():
        rc = next(CONJECTURES.glob("*/.chktexrc"), None)
    return cls, rc


def claim_folder(slug):
    """Take latex/conjectures/<slug>/, never overwriting an existing folder.

    The claim is the mkdir itself, not a preceding exists() check: several
    papers can be read at once, and two of them arriving at the same slug a
    millisecond apart must not both believe they own it.
    """
    for n in range(1, 100):
        folder = CONJECTURES / (slug if n == 1 else f"{slug}-{n}")
        try:
            folder.mkdir(parents=True)
            return folder
        except FileExistsError:
            continue
    raise RuntimeError(f"could not claim a folder for {slug!r}")


def compile_check(folder, no_compile=False):
    """pdflatex, chktex, lacheck. Reports; does not throw the work away."""
    result = {"compiled": None, "chktex": None, "lacheck": None, "errors": []}
    tex = folder / "statement.tex"
    if no_compile or not shutil.which("pdflatex"):
        return result

    for _ in range(2):
        proc = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
            cwd=folder, capture_output=True, text=True,
        )
    result["compiled"] = proc.returncode == 0
    if proc.returncode != 0:
        result["errors"] = [
            line for line in proc.stdout.splitlines()
            if line.startswith("!") or "Undefined control sequence" in line
        ][:20]

    # Both linters print several lines per finding -- chktex echoes the source
    # line and a caret rule under it -- so count the headline lines, not the
    # output lines, or one dash warning reads as three.
    for tool, cmd, head in (
        ("chktex", ["chktex", "-q", tex.name], lambda ln: ln.startswith("Warning")),
        ("lacheck", ["lacheck", tex.name], lambda ln: ln.startswith('"')),
    ):
        if not shutil.which(tool):
            continue
        proc = subprocess.run(cmd, cwd=folder, capture_output=True, text=True)
        lines = [ln for ln in (proc.stdout + proc.stderr).splitlines() if ln.strip()]
        result[tool] = [ln for ln in lines if head(ln)][:20]

    for junk in ("*.aux", "*.log", "*.out", "*.toc", "*.fls", "*.fdb_latexmk"):
        for f in folder.glob(junk):
            f.unlink()
    return result


def write_source_note(folder, record):
    """The provenance a reviewer reads before believing any of it."""
    cand, doc_meta = record["candidate"], record["document"]
    verify = record.get("verify") or {}
    lines = [
        f"# Provenance: {cand['title']}",
        "",
        "Written by `scripts/harvest_conjectures.py`. Nothing here was checked",
        "by a human yet; this file is what the run believed and why.",
        "",
        "## Source",
        "",
        f"- Paper: **{doc_meta.get('title') or '(untitled)'}**",
        f"- Authors: {', '.join(doc_meta.get('authors') or []) or '(unknown)'}",
        f"- Venue/archive: {doc_meta.get('venue_or_archive') or '(unknown)'}"
        f" {doc_meta.get('year') or ''}".rstrip(),
        f"- Identifier: {doc_meta.get('identifier') or '(none read)'}",
        f"- Bibliographic detail: {doc_meta.get('citation_confidence', 'unknown')}",
        f"- File: `{record['pdf']['name']}` ({record['pdf']['pages']} pages)",
        f"- sha256: `{record['pdf']['sha256']}`",
        f"- Read on {record['run']['at']} via the `{record['run']['backend']}` backend",
        "",
        "## How the paper leaves it open",
        "",
        f"`{cand.get('openness_kind', '?')}`. {cand.get('status_note', '')}",
        "",
        "## Quotes, checked against the PDF text layer",
        "",
        "Each was matched mechanically against `pdftotext` output after undoing",
        "ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim",
        "hit; `near` means the span is present with a symbol mangled by the",
        "extractor. A conjecture whose statement or openness quote failed to",
        "ground was dropped before this file was written.",
        "",
        "| role | page | found | match | quote |",
        "| --- | --- | --- | --- | --- |",
    ]
    for g in record["grounding"]:
        quote = g["quote"].replace("|", "\\|").replace("\n", " ")
        quote = quote[:160] + ("..." if len(quote) > 160 else "")
        found = g["found_page"] if g["found_page"] is not None else "-"
        flag = " ⚠" if g["found_page"] not in (None, g["claimed_page"]) else ""
        lines.append(
            f"| {g['role']} | {g['claimed_page']} | {found}{flag} | "
            f"{g['status']} ({g['coverage']:.0%}) | {quote} |"
        )

    lines += [
        "",
        "## Adversarial check",
        "",
        f"**Verdict: {verify.get('verdict', 'not run')}** "
        f"(confidence: {verify.get('confidence', '-')})",
        "",
        verify.get("reason", ""),
        "",
    ]
    if verify.get("checks"):
        lines += ["| check | result | page | finding |", "| --- | --- | --- | --- |"]
        for c in verify["checks"]:
            finding = str(c.get("finding", "")).replace("|", "\\|")
            lines.append(
                f"| {c.get('name', '')} | {c.get('result', '')} | "
                f"{c.get('page') or '-'} | {finding} |"
            )
        lines.append("")
    if verify.get("fabrications"):
        lines += ["### Unsupported by the paper", ""]
        lines += [f"- {f}" for f in verify["fabrications"]] + [""]
    if verify.get("corrections"):
        lines += ["### Corrections the checker asked for", ""]
        for c in verify["corrections"]:
            lines.append(f"- **{c.get('field')}** — {c.get('problem')}")
            if c.get("corrected"):
                lines.append(f"  - suggested: {c['corrected']}")
        lines.append("")

    unverified = unverified_citations(cand)
    if unverified:
        lines += [
            "## Citations that could not be verified",
            "",
            "These were not read off the harvested paper's own reference list.",
            "Do not remove the `[UNVERIFIED]` markers in `statement.tex` until",
            "each has been checked against the actual paper.",
            "",
        ]
        lines += [
            f"- `{b.get('key')}` — {b.get('authors')}, *{b.get('title')}*, "
            f"{b.get('venue')} {b.get('year')}"
            for b in unverified
        ]
        lines.append("")

    build = record.get("build") or {}
    lines += [
        "## Build",
        "",
        f"- pdflatex: {'ok' if build.get('compiled') else 'FAILED' if build.get('compiled') is False else 'not run'}",
        f"- chktex: {len(build.get('chktex') or [])} warnings",
        f"- lacheck: {len(build.get('lacheck') or [])} warnings",
        "",
    ]
    if build.get("errors"):
        lines += ["```"] + build["errors"] + ["```", ""]
    if cand.get("risks"):
        lines += ["## What to check hardest", "", cand["risks"], ""]

    (folder / "SOURCE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Ledger
# --------------------------------------------------------------------------

def read_ledger():
    if LEDGER.exists():
        return json.loads(LEDGER.read_text(encoding="utf-8"))
    return {"version": 1, "documents": {}}


def write_ledger(ledger):
    """Merge into whatever is on disk, then write.

    Papers are read one process per paper when there are several to get
    through, and each holds the ledger it read at startup. Writing that back
    wholesale would drop every entry a sibling added in the meantime; merging
    first costs nothing, since the entries are keyed by content hash and two
    processes never write the same one.
    """
    PROCESSED.mkdir(parents=True, exist_ok=True)
    merged = read_ledger()
    merged["documents"].update(ledger["documents"])
    ledger["documents"] = merged["documents"]
    LEDGER.write_text(json.dumps(merged, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------------
# The run
# --------------------------------------------------------------------------

def process(pdf_path, backend, prompts, args, ledger):
    """Read one paper end to end. Returns (folders_written, note)."""
    print(f"\n=== {pdf_path.name}")
    doc = PdfDoc(pdf_path)
    print(f"  {doc.pages} pages, {doc.size / 1e6:.1f}MB, sha256 {doc.sha256[:12]}")

    if doc.sha256 in ledger["documents"] and not args.force:
        print("  already in the ledger under this hash; skipping (use --force to redo)")
        return [], "skipped-duplicate", doc.sha256
    if not doc.has_text_layer():
        print("  ! no usable text layer -- quotes could not be checked. Skipping.")
        print("    Run OCR over it first (e.g. ocrmypdf) and drop it back in.")
        return [], "no-text-layer", doc.sha256
    if args.dry_run:
        print("  (dry run: no model calls, nothing written, file left in place)")
        return [], "dry-run", doc.sha256

    # --- 1. extract -------------------------------------------------------
    print("  [1/5] reading for open problems...")
    extracted = backend.complete(
        system=prompts["extract.system"],
        prompt=fill(
            prompts["extract.user"],
            PDF_NAME=pdf_path.name,
            PAGES=doc.pages,
            MAX_CONJECTURES=args.max_conjectures,
        ),
        schema=EXTRACT_SCHEMA,
        pdf=doc,
        max_tokens=32000,
        effort=args.effort,
        label="extract",
    )
    meta = extracted.get("document") or {}
    candidates = extracted.get("candidates") or []
    print(f"        paper: {meta.get('title') or '(untitled)'}")
    print(f"        {len(candidates)} candidate(s), "
          f"{len(extracted.get('rejected') or [])} considered and passed over")
    for r in extracted.get("rejected") or []:
        print(f"          - passed over: {r.get('what', '')[:70]} -- {r.get('why', '')[:70]}")

    written, dropped = [], []
    run_meta = {"at": now(), "backend": backend.name, "effort": args.effort}
    considered = candidates[: args.max_conjectures]
    over_cap = len(candidates) - len(considered)

    for cand in considered:
        title = cand.get("title") or cand.get("slug") or "(untitled)"
        print(f"\n  -- {title}")

        # --- 2. ground ----------------------------------------------------
        ok, grounding, reasons = check_candidate(cand, doc, strict=not args.lenient)
        exact = sum(1 for g in grounding if g["status"] == "exact")
        print(f"     [2/5] quotes: {exact}/{len(grounding)} verbatim in the PDF")
        for g in grounding:
            if g["status"] != "exact":
                print(f"           {g['status']} ({g['coverage']:.0%}) "
                      f"[{g['role']} p{g['claimed_page']}] {g['quote'][:70]!r}")
        if not ok:
            print("     DROPPED -- did not ground:")
            for reason in reasons:
                print(f"           {reason}")
            dropped.append((title, "quotes did not ground: " + "; ".join(reasons)))
            continue

        # --- 3. verify ----------------------------------------------------
        print("     [3/5] adversarial check...")
        draft = {k: cand[k] for k in cand if k not in ("why_interesting", "why_clean", "risks")}
        verify = backend.complete(
            system=prompts["verify.system"],
            prompt=fill(
                prompts["verify.user"],
                PDF_NAME=pdf_path.name,
                PAGES=doc.pages,
                DRAFT=json.dumps(draft, indent=2, ensure_ascii=False),
            ),
            schema=VERIFY_SCHEMA,
            pdf=doc,
            max_tokens=16000,
            effort=args.effort,
            label="verify",
        )
        verdict = verify.get("verdict", "unfaithful")
        print(f"           verdict: {verdict} ({verify.get('confidence', '?')})")
        for c in verify.get("checks") or []:
            if c.get("result") != "pass":
                print(f"           {c.get('result')}: {c.get('name')} -- "
                      f"{str(c.get('finding', ''))[:90]}")
        if verdict in ("unfaithful", "not-a-conjecture") and not args.keep_unfaithful:
            print(f"     DROPPED -- {verify.get('reason', '')[:160]}")
            dropped.append((title, f"adversarial check: {verdict}"))
            continue

        # --- 4. typeset ---------------------------------------------------
        print("     [4/5] writing statement.tex...")
        rendered = backend.complete(
            system=prompts["tex.system"],
            prompt=fill(
                prompts["tex.user"],
                RECORD=json.dumps(cand, indent=2, ensure_ascii=False),
                CORRECTIONS=json.dumps(verify.get("corrections") or [], indent=2),
                UNVERIFIED=json.dumps(
                    [b.get("key") for b in unverified_citations(cand)]
                ),
                SOURCE_LINE=(
                    f"{', '.join(meta.get('authors') or []) or 'Unknown'}. "
                    f"{meta.get('title') or pdf_path.stem}. "
                    f"{meta.get('venue_or_archive') or ''} {meta.get('year') or ''}"
                ).strip(),
            ),
            schema=TEX_SCHEMA,
            # No PDF: the mathematics has already been checked, and a
            # compositor that can see the source is a compositor that can
            # quietly re-derive it.
            pdf=None,
            max_tokens=32000,
            effort=args.effort,
            label="typeset",
        )
        tex = (rendered.get("tex") or "").strip()
        if "\\documentclass{conjura-conjecture}" not in tex or "\\end{document}" not in tex:
            print("     DROPPED -- rendered statement.tex is not a complete document")
            dropped.append((title, "typeset output was not a complete document"))
            continue

        folder = claim_folder(cand["slug"])
        cls, rc = find_class_files()
        shutil.copy2(cls, folder / cls.name)
        if rc:
            shutil.copy2(rc, folder / ".chktexrc")
        (folder / "statement.tex").write_text(tex + "\n", encoding="utf-8")

        # --- 5. compile ---------------------------------------------------
        print("     [5/5] pdflatex, chktex, lacheck...")
        build = compile_check(folder, no_compile=args.no_compile)
        if build["compiled"] is False:
            print("           ! does not compile -- flagged in SOURCE.md, folder kept")
        elif build["compiled"]:
            noise = len(build.get("chktex") or []) + len(build.get("lacheck") or [])
            print(f"           compiles; {noise} lint warning(s)")

        record = {
            "pdf": {"name": pdf_path.name, "sha256": doc.sha256, "pages": doc.pages},
            "run": run_meta,
            "document": meta,
            "candidate": cand,
            "grounding": grounding,
            "verify": verify,
            "build": build,
        }
        (folder / "harvest.json").write_text(
            json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        write_source_note(folder, record)
        written.append(folder)
        print(f"     -> {folder.relative_to(ROOT)}")

    report_verdict(pdf_path, candidates, written, dropped, over_cap)

    ledger["documents"][doc.sha256] = {
        "file": pdf_path.name,
        "title": meta.get("title", ""),
        "pages": doc.pages,
        "processed_at": run_meta["at"],
        "backend": backend.name,
        "candidates_found": len(candidates),
        "conjectures_written": [str(f.relative_to(ROOT)) for f in written],
        "dropped": [{"title": t, "why": w} for t, w in dropped],
    }
    return written, "ok", doc.sha256


def report_verdict(pdf_path, candidates, written, dropped, over_cap=0):
    """Say, for one paper, whether anything was found and whether it was kept.

    The step-by-step trace above answers this only by implication: a paper
    that yields nothing prints a `0 candidate(s)` line and then simply stops,
    which is indistinguishable at a glance from a paper still being read. The
    two numbers a reader actually wants are *found* -- did the paper pose an
    open problem at all -- and *created* -- did one survive grounding, the
    adversarial check and typesetting to become a folder on disk. They differ
    whenever a check does its job, so neither implies the other.
    """
    name = pdf_path.name
    if not candidates:
        print(f"\n  = {name}: NO CONJECTURE FOUND -- the paper posed no open "
              f"problem this run could use. Nothing written.")
        return
    print(f"\n  = {name}: {len(candidates)} found, {len(written)} created, "
          f"{len(dropped)} dropped" + (f", {over_cap} over the cap" if over_cap else ""))
    for folder in written:
        print(f"      created: {folder.relative_to(ROOT)}")
    for title, why in dropped:
        print(f"      dropped: {title[:60]} -- {why[:90]}")
    if not written:
        print("      NO CONJECTURE CREATED -- every candidate failed a check "
              "above; nothing was written.")


def move_to_processed(pdf_path, sha256):
    PROCESSED.mkdir(parents=True, exist_ok=True)
    dest = PROCESSED / pdf_path.name
    if dest.exists():
        dest = PROCESSED / f"{pdf_path.stem}-{sha256[:8]}{pdf_path.suffix}"
    shutil.move(str(pdf_path), str(dest))
    return dest


def do_report():
    ledger = read_ledger()
    docs = ledger.get("documents", {})
    if not docs:
        print("Nothing harvested yet.")
        return
    print(f"{len(docs)} paper(s) processed.\n")
    for sha, rec in sorted(docs.items(), key=lambda kv: kv[1].get("processed_at", "")):
        written = rec.get("conjectures_written") or []
        print(f"{rec.get('processed_at', '?')}  {rec.get('file')}  [{sha[:12]}]")
        if rec.get("title"):
            print(f"    {rec['title']}")
        found = rec.get("candidates_found", 0)
        if not found:
            print("    no conjecture found -- nothing written")
        else:
            print(f"    {found} candidate(s) -> "
                  f"{len(written)} conjecture(s) kept"
                  + ("" if written else "  (NONE CREATED)"))
        for w in written:
            print(f"      created: {w}")
        for d in rec.get("dropped") or []:
            print(f"      dropped: {str(d.get('title'))[:60]} -- {str(d.get('why'))[:80]}")
    waiting = sorted(p for p in HARVEST.glob("*.pdf"))
    print(f"\n{len(waiting)} PDF(s) waiting in {HARVEST.relative_to(ROOT)}/")


def main():
    ap = argparse.ArgumentParser(
        description="Extract checked conjectures from the PDFs in latex/harvest/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("The interesting question")[0],
    )
    ap.add_argument("pdfs", nargs="*", type=Path,
                    help="specific PDFs; default is everything in latex/harvest/")
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be read, make no model calls, move nothing")
    ap.add_argument("--report", action="store_true", help="print the ledger and exit")
    ap.add_argument("--limit", type=int, default=0, help="stop after N papers")
    ap.add_argument("--max-conjectures", type=int, default=3,
                    help="most conjectures to keep from one paper (default 3)")
    ap.add_argument("--backend", choices=("auto", "api", "cli"), default="auto")
    ap.add_argument("--effort", choices=("low", "medium", "high", "xhigh", "max"),
                    default="high")
    ap.add_argument("--text-only", action="store_true",
                    help="send the extracted text instead of the PDF (for oversized files)")
    ap.add_argument("--budget-usd", type=float, default=None,
                    help="per-call spend cap, cli backend only")
    ap.add_argument("--lenient", action="store_true",
                    help="accept a weakly-grounded statement or openness quote")
    ap.add_argument("--keep-unfaithful", action="store_true",
                    help="write folders the adversarial check rejected (marked as such)")
    ap.add_argument("--no-compile", action="store_true", help="skip pdflatex and the linters")
    ap.add_argument("--keep", action="store_true",
                    help="leave processed PDFs in latex/harvest/ instead of moving them")
    ap.add_argument("--force", action="store_true",
                    help="re-read a paper already in the ledger")
    args = ap.parse_args()

    if args.report:
        do_report()
        return 0

    HARVEST.mkdir(parents=True, exist_ok=True)
    pdfs = args.pdfs or sorted(HARVEST.glob("*.pdf"))
    pdfs = [p for p in pdfs if p.parent.name != PROCESSED.name]
    if not pdfs:
        print(f"No PDFs in {HARVEST.relative_to(ROOT)}/. Drop some in and run again.")
        return 0
    if args.limit:
        pdfs = pdfs[: args.limit]

    if not shutil.which("pdftotext"):
        raise SystemExit("pdftotext not found (brew install poppler); it is not optional here")

    prompts = load_prompts()
    backend = None if args.dry_run else pick_backend(
        args.backend, budget_usd=args.budget_usd, text_only=args.text_only
    )
    if backend:
        print(f"Backend: {backend.name}, effort {args.effort}")
    ledger = read_ledger()

    total, failures, outcomes = [], [], []
    for pdf in pdfs:
        try:
            written, status, sha = process(pdf, backend, prompts, args, ledger)
        except (ModelError, RuntimeError, OSError) as exc:
            print(f"  ! {exc}")
            print("    Left in place so the run can be retried.")
            failures.append((pdf.name, str(exc)))
            outcomes.append((pdf.name, "failed", 0))
            continue
        total += written
        outcomes.append((pdf.name, status, len(written)))
        if status in ("ok", "skipped-duplicate") and not args.keep:
            dest = move_to_processed(pdf, sha)
            print(f"  moved to {dest.relative_to(ROOT)}")
        if status == "ok":
            write_ledger(ledger)

    # Every paper gets a line here whether or not it produced anything. A run
    # that listed only its successes would let a paper that yielded nothing
    # leave no trace at all in the summary, which is the case most worth
    # seeing: it is either a paper with no open problem in it, or a prompt
    # that failed to find the one that is there.
    print(f"\n{'=' * 60}")
    print(f"{len(outcomes)} paper(s) seen:\n")
    label = {
        "ok": "read",
        "failed": "FAILED",
        "skipped-duplicate": "skipped, already in the ledger",
        "no-text-layer": "SKIPPED, no text layer (run OCR)",
        "dry-run": "not read (dry run)",
    }
    for name, status, count in outcomes:
        if status == "ok":
            verdict = f"{count} conjecture(s) created" if count else "no conjecture created"
        else:
            verdict = label.get(status, status)
        print(f"  {name:<28} {verdict}")
    print(f"\n{len(total)} conjecture folder(s) written:")
    for folder in total:
        print(f"  {folder.relative_to(ROOT)}")
    if failures:
        print(f"\n{len(failures)} paper(s) failed and were left in place:")
        for name, why in failures:
            print(f"  {name}: {why}")
    if total:
        print("\nNothing here has been read by a human. Each folder's SOURCE.md")
        print("carries the quotes, their pages and the checks; read it before")
        print("trusting the statement.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
