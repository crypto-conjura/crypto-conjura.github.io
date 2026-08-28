#!/usr/bin/env python3
"""Report drafts in latex/conjectures/ that never became a site page.

Every other gate in this repository discovers content by globbing `c/` and
`papers/`: `build_index.py` reads `c/*/index.qmd` into `_generated/all.yml`,
`check_relations.py` walks the same set, `status_badge.py` validates it.
So a statement that reaches `c/` reaches the site's listings by itself, with
nothing to remember and nothing to wire up.

`latex/conjectures/` is on the other side of that line, and deliberately:
`artifact_manifest.py` excludes it because "promoting one is a manual
editorial act, not a build, so there is no output to be stale against". That
is right about *staleness* and silent about *existence*. A draft can sit in a
tracked folder forever and no script will ever mention it -- which was
tolerable while drafts arrived one at a time by hand, and stopped being
tolerable when `harvest_conjectures.py` began writing them from PDFs in
batches. A harvested draft that nobody promotes is indistinguishable, from
the outside, from one that was never harvested.

This script closes that gap and nothing else. It does not promote anything:
choosing a page's areas, model, form, status flags and difficulty is a
judgment about mathematics, and verifying its sources is a judgment about the
literature. It only answers "which drafts have no page yet".

  python3 scripts/draft_status.py           the full picture
  python3 scripts/draft_status.py --check   the CI gate

WHY --check DOES NOT FAIL ON AN UNPROMOTED DRAFT. Both workflows run every
gate before `quarto render`, and a non-zero exit fails the whole job. A gate
that failed on an unpromoted draft would therefore stop the site deploying
for everyone, on every push, until somebody promoted it -- turning "there is
editorial work outstanding" into "the site is down". That is precisely the
failure `status_badge.py` caused for two hours on 2026-08-15. Not promoting a
draft promptly is a normal state of affairs, not a broken repository, so it
is reported and the gate passes.

What DOES fail is a link that contradicts the tree: a page claiming a draft
folder that is not there, or two pages claiming the same draft *without* that
draft actually holding several conjectures. Those are errors in committed
metadata, they are cheap to fix, and leaving them unreported would rot the
signal the rest of the script depends on.

THE LINK IS EXPLICIT BECAUSE EVERY IMPLICIT ONE IS WRONG. Measured against
the tree, on 2026-08-17:

  * A draft's folder name is never the page's `problem:` slug --
    `split-decomp` vs `split-source-decomposition`, `mirror-theory` vs
    `generalized-mirror-theory`, and so on for every pair.
  * `problem:` is not unique: it names the problem, not the statement, so two
    statements about one problem share a value. Measured on 2026-08-17,
    `0004`/`0005` shared one and `0008`/`0009` shared another; both of the
    second pages were removed on 2026-08-28, but the field's meaning is
    unchanged and the next pair will collide the same way.
  * Titles are not unique either, and mislead. `groth16/statement.tex` and
    `split-nilp/statement.tex` are byte-identical, and correspond to two
    different pages.
  * The relation is not 1:1. One draft document can hold several conjectures
    and become several pages: `lhl-public-seed/` is subtitled "Two
    Leftover-Hash-Lemma Conjectures" and became `c/0004` and the secret-seed
    page then numbered `c/0005`. It still holds two `\begin{conjecture}`
    environments with only `c/0004` claiming it, which the check permits --
    it bounds claimants by conjectures, not the other way round.

So the page names its draft, in a `draft:` frontmatter field, and a draft
names nothing -- the direction that survives one document becoming several
pages. Nothing here guesses.
"""
import re
import sys
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "latex" / "conjectures"
STATEMENTS_DIR = ROOT / "c"

# _template is the skeleton every new draft is copied from, not a draft.
IGNORED = {"_template"}


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    return m.group(1) if m else ""


def scalar(fm, field):
    """Read one scalar out of frontmatter without PyYAML.

    Stdlib only, matching status_badge.py: PyYAML is a CI-only dependency
    here, and a gate that cannot run on a developer's machine (or in
    .githooks/pre-commit) is a gate that gets discovered in CI instead.
    """
    m = re.search(rf"^{field}:\s*(.*)$", fm, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
        val = val[1:-1]
    return val or None


def find_drafts():
    """Every draft folder, with the sha256 of its statement.tex."""
    out = {}
    if not DRAFTS.is_dir():
        return out
    for d in sorted(DRAFTS.iterdir()):
        if not d.is_dir() or d.name in IGNORED:
            continue
        tex = d / "statement.tex"
        if not tex.is_file():
            continue
        out[d.name] = {
            "sha256": hashlib.sha256(tex.read_bytes()).hexdigest(),
            # SOURCE.md is written only by harvest_conjectures.py, so it is
            # what distinguishes a machine-written draft nobody has read from
            # one a human sat down and wrote.
            "harvested": (d / "SOURCE.md").is_file(),
        }
    return out


def find_pages():
    """Every published statement and the draft it declares, if any."""
    out = {}
    for path in sorted(STATEMENTS_DIR.glob("*/index.qmd")):
        fm = frontmatter(path)
        out[path.parent.name] = {
            "draft": scalar(fm, "draft"),
            "title": scalar(fm, "title") or "",
        }
    return out


def audit():
    """Return (report, errors). Errors are the ones --check exits 1 on."""
    drafts, pages = find_drafts(), find_pages()
    errors = []

    claimed = {}
    for page_id, page in sorted(pages.items()):
        slug = page["draft"]
        if slug is None:
            continue
        if slug not in drafts:
            errors.append(
                f"c/{page_id}: draft: {slug!r} names no folder in "
                f"latex/conjectures/. Either the draft was renamed or "
                f"deleted, or the field is a typo."
            )
            continue
        claimed.setdefault(slug, []).append(page_id)

    # Two pages may share a draft -- one document can pose several
    # conjectures -- but only if the document really does. A draft with a
    # single conjecture environment claimed twice is a copied field.
    for slug, page_ids in sorted(claimed.items()):
        if len(page_ids) > 1:
            tex = (DRAFTS / slug / "statement.tex").read_text(
                encoding="utf-8", errors="replace"
            )
            n = len(re.findall(r"\\begin\{conjecture", tex)) or len(
                re.findall(r"\\cjconjecture", tex)
            )
            if n and n < len(page_ids):
                errors.append(
                    f"latex/conjectures/{slug}: claimed by "
                    f"{', '.join('c/' + p for p in page_ids)} "
                    f"({len(page_ids)} pages) but holds {n} conjecture(s)."
                )

    unpromoted = sorted(set(drafts) - set(claimed))
    unlinked = sorted(p for p, v in pages.items() if v["draft"] is None)

    # Same statement.tex in two folders. Not an error: it is how a
    # multi-conjecture document currently gets one folder per conjecture.
    by_hash = {}
    for slug, meta in drafts.items():
        by_hash.setdefault(meta["sha256"], []).append(slug)
    duplicates = sorted(v for v in by_hash.values() if len(v) > 1)

    return {
        "drafts": drafts,
        "pages": pages,
        "claimed": claimed,
        "unpromoted": unpromoted,
        "unlinked": unlinked,
        "duplicates": duplicates,
    }, errors


def main(argv):
    check = "--check" in argv
    report, errors = audit()
    drafts = report["drafts"]

    if not check:
        print(f"{len(drafts)} draft(s) in latex/conjectures/, "
              f"{len(report['pages'])} page(s) in c/\n")
        for slug, page_ids in sorted(report["claimed"].items()):
            print(f"  {slug:<24} -> {', '.join('c/' + p for p in page_ids)}")
        for pair in report["duplicates"]:
            print(f"\n  note: identical statement.tex in {', '.join(pair)}")

    if report["unpromoted"]:
        print(f"\n{len(report['unpromoted'])} draft(s) with no page in c/:")
        for slug in report["unpromoted"]:
            tag = " [harvested, unread]" if drafts[slug]["harvested"] else ""
            print(f"  latex/conjectures/{slug}{tag}")
        print("\nPromoting one is an editorial act, not a build: see "
              "latex/README.md.\nThis is a report, not a failure.")

    if report["unlinked"] and not check:
        print(f"\n{len(report['unlinked'])} page(s) declare no draft: "
              f"{', '.join('c/' + p for p in report['unlinked'])}")
        print("  (fine for a statement written straight into c/)")

    if errors:
        print(f"\n{len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    if check:
        print("draft_status: no broken draft links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
