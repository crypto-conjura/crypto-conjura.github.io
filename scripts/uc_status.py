#!/usr/bin/env python3
"""
Keep each UC encyclopedia entry's `definition:` field honest.

Every layer index renders a Status column, and what it reports is how
established the *concept* is: `Canonical`, `Idealized Setup`, `Emerging`,
`Open`. What no page reported until now is whether the entry actually contains
a definition. Most do not. A reader scanning a layer index could not tell a
written entry from an empty slot, because both said `Canonical` with the same
confidence.

`definition:` is that second, orthogonal signal, and it is generated rather
than hand-set for the same reason `status_badge` is: it is computable from the
page, so trusting a human to keep 104 of them in step is a slow way of getting
it wrong.

Three values, and the third is the point:

  Defined                  the page carries a box, transcribed from a source
  Not yet written          a slot with citations and no definition yet
  No canonical definition  none exists in the literature to transcribe

The values are the words the table shows, so there is no mapping layer between
what is checked and what a reader sees. The first two are derived: a page has a
`.cj-interface` box or it does not. The third is a claim about the literature
that no script can make, so it is the one value a human may write, and this
script preserves it. Writing it on a page that does have a box is a
contradiction and fails the check.

  python3 scripts/uc_status.py            write the field on every entry
  python3 scripts/uc_status.py --check    report drift, write nothing, exit 1

`--check` is the CI gate. It needs no more than read access.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = sorted(ROOT.glob("uc/layer-*/*/index.qmd"))

DEFINED = "Defined"
PENDING = "Not yet written"
NONE_KNOWN = "No canonical definition"
VALUES = (DEFINED, PENDING, NONE_KNOWN)

# The box the generator writes. Matching the opening div is enough: a page
# either has one or has nothing at all, and a half-written box fails
# gen_interface.py --check long before it reaches this script.
BOX = re.compile(r'<div class="cj-interface">')
FIELD = re.compile(r"^definition:\s*(.+?)\s*$", re.M)
FRONT = re.compile(r"\A---\n(.*?\n)---\n", re.S)


def read(path):
    text = path.read_text(encoding="utf-8")
    m = FRONT.match(text)
    if not m:
        return None, None, text
    fm = m.group(1)
    cur = FIELD.search(fm)
    return fm, (cur.group(1).strip('"\'') if cur else None), text


def wanted(path, text, current):
    has_box = bool(BOX.search(text))
    if current == NONE_KNOWN:
        # A human's claim about the literature. Kept, unless the page went and
        # acquired a definition anyway, which makes the claim false.
        return DEFINED if has_box else NONE_KNOWN
    return DEFINED if has_box else PENDING


def main():
    check = "--check" in sys.argv
    if not ENTRIES:
        sys.exit("no uc/layer-*/*/index.qmd found")

    drift, wrote, bad = [], 0, []
    counts = {v: 0 for v in VALUES}

    for path in ENTRIES:
        rel = path.relative_to(ROOT)
        fm, current, text = read(path)
        if fm is None:
            bad.append(f"{rel}: no YAML frontmatter")
            continue
        if current is not None and current not in VALUES:
            bad.append(f"{rel}: definition: {current!r} is not one of {VALUES}")
            continue
        want = wanted(path, text, current)
        counts[want] += 1

        if current == want:
            continue
        if current == NONE_KNOWN and want == DEFINED:
            bad.append(f"{rel}: marked {NONE_KNOWN!r} but the page carries a box")
            continue
        if check:
            drift.append(f"{rel}: definition: {current!r} -> {want!r}")
            continue

        if current is None:
            # After `layer:` if there is one, else at the end of the block, so
            # the field lands somewhere predictable rather than wherever a
            # regex happened to match.
            if re.search(r"^layer:.*$", fm, re.M):
                # A lambda, not a replacement string. re.sub reads escapes in a
                # string replacement, so the quotes around the value come back
                # as a literal backslash-quote. The same trap is documented
                # twice in scripts/build_uc_html.sh.
                new_fm = re.sub(r"^(layer:.*)$",
                                lambda m: f'{m.group(1)}\ndefinition: "{want}"',
                                fm, count=1, flags=re.M)
            else:
                new_fm = fm.rstrip("\n") + f'\ndefinition: "{want}"\n'
        else:
            new_fm = FIELD.sub(lambda _: f'definition: "{want}"', fm, count=1)
        path.write_text(text.replace(fm, new_fm, 1), encoding="utf-8")
        wrote += 1

    for b in bad:
        print(f"  ERROR {b}")
    summary = ", ".join(f"{counts[v]} {v}" for v in VALUES)
    if check:
        for d in drift:
            print(f"  DRIFT {d}")
        print(f"{len(ENTRIES)} entrie(s) checked: {summary}")
        if drift or bad:
            print(f"{len(drift)} stale, {len(bad)} invalid. "
                  f"Run `python3 scripts/uc_status.py` to reconcile.")
            return 1
        return 0
    print(f"{wrote} entrie(s) updated out of {len(ENTRIES)}: {summary}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
