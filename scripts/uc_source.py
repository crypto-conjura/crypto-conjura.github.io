#!/usr/bin/env python3
"""Harvest the sources a UC encyclopedia stub cites, ready for prompts/source.md.

One functionality page cites one to four papers. Before anything can be
written about it, someone has to fetch those papers, work out which of them
actually prints a definition of *this* functionality, notice that the ePrint
posting has been revised four times since the proceedings version, and get an
image of the figure in front of a reviewer. That is mechanical, it is the same
ninety-seven times, and doing it by hand is where an en-masse run goes wrong:
not in the mathematics, but in downloading the 2004 revision of a paper that
was last corrected in 2011 and never noticing.

So this script does that half, deterministically, and leaves the judgment to
the prompt:

    python3 scripts/uc_source.py --list          # stubs, by how much seed they have
    python3 scripts/uc_source.py f-auth          # harvest one
    python3 scripts/uc_source.py f-auth f-com    # or several
    python3 scripts/uc_source.py --all --limit 8

For each citation on the page it resolves the URL to a PDF, records the
version it got and every later revision ePrint knows about, scans the text
layer for interface-box titles, and renders the pages whose box names *this*
functionality to PNG. Output lands in the entry's own folder:

    uc/layer-N-<slug>/<id>/_src/
        sources.json                  the manifest, committed
        <citekey>-p<page>.png         one image per candidate box, not committed

`_src/` is chosen so that Quarto ignores it (it ignores `_`- and `.`-prefixed
paths), because a figure from a Springer or IEEE proceedings version is the
publisher's and must not be republished on a public site. The PNGs are
gitignored for the same reason; `sources.json` is committed, and it carries
the URL, the revision stamp and the page number, so anyone can regenerate the
images exactly by re-running this script. If a source is CC-BY and the figure
is wanted on the page itself, that is a per-paper decision made after checking
the licence, and it goes in `<id>/img/` instead, where the site will publish it.

The scan is a *lead generator*, not an answer. It finds pages whose text layer
contains something shaped like "Functionality F_auth"; it cannot tell whether
that box is the definition, a variant used in a proof, or a mention in a
figure caption. Deciding is Stage 1 of prompts/source.md, and a citation this
script finds nothing in is a normal result worth reporting rather than a bug.

Needs `pdftotext` and `pdftoppm` (poppler) and `curl`. Downloads are cached in
~/.cache/conjura-uc-sources, so re-running is free and the IACR server is hit
once per paper rather than once per run.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
UC = REPO / "uc"
CACHE = Path(os.environ.get("CONJURA_CACHE",
                            Path.home() / ".cache" / "conjura-uc-sources"))
UA = "conjura-uc-source/1.0 (+https://crypto-conjura.github.io)"
TIMEOUT = 60

# A reference bullet on a stub page. The link text is the title, the URL is
# where the PDF lives, and what precedes the link is the author list.
REF = re.compile(r"^- (?P<authors>[^[]*)\[\*(?P<title>[^]]+)\*\]\((?P<url>[^)]+)\)"
                 r"(?P<rest>.*)$", re.M)
EPRINT = re.compile(r"eprint\.iacr\.org/(?:archive/)?(\d{4})/(\d+)")
YEAR = re.compile(r"\b(19|20)\d{2}\b")

# An interface-box title in a paper's text layer. Authors write the subscript
# a dozen ways once a PDF is flattened to text -- "Fauth", "F auth", "FAUTH",
# "F_{auth}", "Fauth" with the F in a math font and the subscript adjacent --
# so match the shape and normalize the name afterwards rather than trying to
# enumerate the spellings.
BOXTITLE = re.compile(
    r"(?:^|\n)[ \t]*(?:The\s+)?(?:Ideal\s+)?(?:Functionality|FUNCTIONALITY)"
    r"[ \t]*:?[ \t]*(?P<kind>[FG])[ \t_]*(?P<name>[A-Za-z][A-Za-z0-9 _-]{0,24})")
# ... and the same box announced as a figure caption instead of a banner.
CAPTION = re.compile(
    r"(?:^|\n)[ \t]*(?:Figure|Fig\.)[ \t]*(?P<num>\d+)[ \t]*[.:][^\n]{0,120}",
    re.I)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, check=True, **kw)


# ------------------------------------------------------------------ pages

def entry_pages():
    """Every functionality page, by id."""
    return {p.parent.name: p for p in sorted(UC.glob("layer-*/*/index.qmd"))}


def is_stub(page):
    """A page is a stub until it has an interface box to read."""
    return "## Functionality" not in page.read_text(encoding="utf-8")


def citations(page):
    """The reference bullets on a page, in the order they are printed."""
    text = page.read_text(encoding="utf-8")
    out = []
    for m in REF.finditer(text):
        authors = m.group("authors").strip().rstrip(".").strip()
        rest = m.group("rest")
        years = YEAR.findall(rest) and re.findall(r"\b((?:19|20)\d{2})\b", rest)
        out.append({
            "authors": authors,
            "title": m.group("title").strip(),
            "url": m.group("url").strip(),
            "venue": rest.strip(" ."),
            "year": int(years[-1]) if years else None,
            "citekey": citekey(authors, years[-1] if years else None),
        })
    return out


def citekey(authors, year):
    """A short, stable, filesystem-safe name for a citation."""
    names = re.split(r",| and ", authors)
    first = re.sub(r"[^A-Za-z]", "", names[0]) or "anon"
    return "%s%s" % (first.lower(), year or "")


# ------------------------------------------------------------------ fetch

def fetch(url, dest):
    """Download to `dest` unless it is already cached. Returns the sha256.

    ePrint postings from the 1990s are PostScript only, and those are exactly
    the papers cited as the origin of a functionality, so a 404 on the `.pdf`
    is retried as `.ps` and converted rather than reported as unavailable.
    """
    if not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            body = get(url)
        except urllib.error.HTTPError as e:
            if e.code != 404 or not url.endswith(".pdf"):
                raise
            ps = dest.with_suffix(".ps")
            ps.write_bytes(get(url[:-4] + ".ps"))
            run(["ps2pdf", str(ps), str(dest)])
            body = None
        if body is not None:
            if not body.startswith(b"%PDF"):
                raise ValueError("not a PDF (server sent %d bytes of %s)"
                                 % (len(body), body[:16]))
            dest.write_bytes(body)
    return hashlib.sha256(dest.read_bytes()).hexdigest()[:16]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read()


def eprint_versions(year, num):
    """Every revision ePrint holds, newest first, as display stamps.

    This is the currency check the whole harvest exists for. A stub citing a
    2003 posting says nothing about whether the definition on it was rewritten
    in 2005; ePrint's archive page does, and `/YYYY/NNN.pdf` always serves the
    newest, which is therefore what we read.
    """
    url = "https://eprint.iacr.org/archive/versions/%s/%s" % (year, num)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            html = r.read().decode("utf-8", "replace")
    except (urllib.error.URLError, OSError):
        return []
    # Each row prints its stamp twice (once as the link, once as the label),
    # so dedupe while keeping the page's newest-first order.
    return list(dict.fromkeys(re.findall(r"\b(\d{8}:\d{6})\b", html)))


def resolve(cite):
    """Where to get this citation's PDF, and what version that is."""
    url = cite["url"]
    m = EPRINT.search(url)
    if m:
        year, num = m.group(1), m.group(2)
        vs = eprint_versions(year, num)
        return {
            "pdf": "https://eprint.iacr.org/%s/%s.pdf" % (year, num),
            "kind": "eprint",
            "revisions": vs,
            "version": vs[0] if vs else None,
            "revised_since_first": len(vs) - 1 if vs else None,
        }
    if url.lower().endswith(".pdf"):
        return {"pdf": url, "kind": "direct", "revisions": [], "version": None}
    return {"pdf": None, "kind": "manual", "revisions": [], "version": None}


# ------------------------------------------------------------------- scan

def pages_text(pdf):
    # pdftotext ends the last page with a form feed too, so the naive split
    # leaves an empty page on the end and reports one page too many.
    out = run(["pdftotext", "-layout", str(pdf), "-"]).stdout.split("\f")
    return out[:-1] if out and not out[-1].strip() else out


def normalize(name):
    return re.sub(r"[^a-z0-9]", "", name.lower())


def boxes(text_pages):
    """Interface-box titles found in a PDF's text layer, with their pages."""
    found = []
    for i, page in enumerate(text_pages, 1):
        for m in BOXTITLE.finditer(page):
            raw = ("%s_%s" % (m.group("kind"), m.group("name"))).strip()
            found.append({"page": i, "title": " ".join(raw.split()),
                          "norm": normalize(m.group("kind") + m.group("name"))})
    return found


def wanted_names(fid):
    """Spellings of a functionality id that a paper might print.

    `f-auth` is `Fauth` here and `F_AUTH` there; `g-pki` is `Gpki` but also
    `GPKI` and, in the papers that predate the global-setup notation, `Fca`.
    Only the mechanical variations are generated -- an alias like Fca -> g-pki
    is a judgment about the literature and belongs in the report, not here.
    """
    kind, name = fid.split("-", 1)
    stem = normalize(name)
    return {normalize(kind) + stem, normalize(kind) + stem.rstrip("s"),
            normalize(kind) + stem + "s"}


def candidates(fid, found):
    """Boxes whose name matches the target, and the rest, kept separately."""
    want = wanted_names(fid)
    hit = [b for b in found if b["norm"] in want]
    near = [b for b in found if b["norm"] not in want
            and any(w[1:] and w[1:] in b["norm"] for w in want)]
    return hit, near


def shoot(pdf, page, dest, dpi):
    """Render one page of a PDF to a PNG at `dest`."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    stem = dest.with_suffix("")
    run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
         "-png", "-singlefile", str(pdf), str(stem)])
    return dest


# ---------------------------------------------------------------- harvest

def harvest(fid, page, dpi, max_shots):
    src = page.parent / "_src"
    cites = citations(page)
    manifest = {
        "id": fid,
        "page": str(page.relative_to(REPO)),
        "generated_by": "scripts/uc_source.py",
        "citations": [],
    }
    if not cites:
        print("  no citations on the page -- this one needs a literature "
              "search before it can be sourced")

    shots = 0
    for cite in cites:
        rec = dict(cite)
        rec.update(resolve(cite))
        pdf_url = rec.pop("pdf")
        rec["pdf_url"] = pdf_url
        print("  %-16s %s" % (rec["citekey"], rec["title"][:60]))

        if not pdf_url:
            rec["status"] = "no direct PDF; fetch by hand from " + rec["url"]
            print("       -> %s" % rec["status"])
            manifest["citations"].append(rec)
            continue

        local = CACHE / (rec["citekey"] + "-" + hashlib.sha1(
            pdf_url.encode()).hexdigest()[:8] + ".pdf")
        try:
            rec["sha256_16"] = fetch(pdf_url, local)
        except Exception as e:                      # noqa: BLE001 -- reported
            rec["status"] = "download failed: %s" % e
            print("       -> %s" % rec["status"])
            manifest["citations"].append(rec)
            continue

        text = pages_text(local)
        rec["pdf_pages"] = len(text)
        found = boxes(text)
        hit, near = candidates(fid, found)
        rec["boxes_matching"] = hit
        rec["boxes_nearby"] = near[:12]
        # A miss is the common case and usually means the paper names the box
        # something else -- Canetti et al.'s global-setup paper defines what
        # this site calls f-acrs, but prints it under another name. So when
        # nothing matches, hand over every box the paper does print: deciding
        # that one of them is the target is a judgment about the literature,
        # and the reader of this manifest is the one equipped to make it.
        if not hit:
            rec["boxes_in_paper"] = list({b["title"]: b for b in found}.values())[:24]
        rec["status"] = "ok"
        if rec.get("version"):
            print("       version %s (%d revision(s) on ePrint)"
                  % (rec["version"], rec.get("revised_since_first") or 0))

        rec["screenshots"] = []
        for b in hit:
            if shots >= max_shots:
                rec["screenshots"].append({"page": b["page"],
                                           "png": None,
                                           "note": "over --max-shots"})
                continue
            png = src / ("%s-p%d.png" % (rec["citekey"], b["page"]))
            shoot(local, b["page"], png, dpi)
            shots += 1
            rec["screenshots"].append({
                "page": b["page"], "title": b["title"],
                "png": str(png.relative_to(page.parent)),
                "pointer": pointer(rec, b["page"]),
            })
            print("       p%-4d %-28s -> %s"
                  % (b["page"], b["title"], png.relative_to(REPO)))
        if not hit:
            other = sorted({b["title"] for b in near} or
                           {b["title"] for b in found})
            print("       no box named %s; this paper prints: %s"
                  % (fid, ", ".join(other[:8]) or "no boxes at all"))
        manifest["citations"].append(rec)

    src.mkdir(parents=True, exist_ok=True)
    (src / "sources.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print("  manifest: %s" % (src / "sources.json").relative_to(REPO))
    return manifest


def pointer(rec, page):
    """The citation line that replaces the image on the public page.

    The screenshot is evidence for a reviewer and stays out of the site; what
    a reader gets is this, precise enough to re-derive the screenshot in a few
    seconds: which posting, which revision, which page.
    """
    bits = [rec["authors"], rec["title"]]
    if rec.get("kind") == "eprint":
        m = EPRINT.search(rec["url"])
        bits.append("ePrint %s/%s" % (m.group(1), m.group(2)))
        if rec.get("version"):
            bits.append("revision %s" % rec["version"])
    bits.append("p. %d" % page)
    return ", ".join(b for b in bits if b)


# ------------------------------------------------------------------- main

def do_list(pages):
    rows = []
    for fid, p in pages.items():
        if not is_stub(p):
            continue
        cites = citations(p)
        rows.append((len(cites), fid, str(p.relative_to(REPO))))
    for n, fid, path in sorted(rows):
        print("%-10s %d citation(s)  %s" % (fid, n, path))
    print("\n%d stub(s); %d with no citation to start from"
          % (len(rows), sum(1 for n, _, _ in rows if n == 0)))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ids", nargs="*", help="functionality ids, e.g. f-auth")
    ap.add_argument("--list", action="store_true",
                    help="list the stubs and how many citations each has")
    ap.add_argument("--all", action="store_true", help="every stub")
    ap.add_argument("--limit", type=int, default=0,
                    help="with --all, stop after this many entries")
    ap.add_argument("--dpi", type=int, default=200, help="screenshot dpi")
    ap.add_argument("--max-shots", type=int, default=6,
                    help="cap the images written per entry")
    args = ap.parse_args()

    for tool in ("pdftotext", "pdftoppm"):
        if not any((Path(d) / tool).exists() for d in os.environ["PATH"].split(":")):
            sys.exit("%s not found; install poppler" % tool)

    pages = entry_pages()
    if args.list:
        return do_list(pages)

    ids = args.ids
    if args.all:
        ids = [f for f, p in pages.items() if is_stub(p)]
        if args.limit:
            ids = ids[:args.limit]
    if not ids:
        return do_list(pages)

    bad = [f for f in ids if f not in pages]
    if bad:
        sys.exit("no page for: " + ", ".join(bad))

    for fid in ids:
        print("%s (%s)" % (fid, pages[fid].parent.relative_to(REPO)))
        harvest(fid, pages[fid], args.dpi, args.max_shots)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
