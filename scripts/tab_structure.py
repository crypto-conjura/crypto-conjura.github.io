#!/usr/bin/env python3
"""Keep every statement page's tabs the same tabs, in the same order.

Three layouts had grown up under `c/` without anyone deciding between them:
the oldest pages tabbed Statement/Proof/Formal Artifact and left Open
obligations loose below, the middle ones tabbed Statement/Proof/Discussion
and left Open obligations and Sources loose, and the newest tabbed all five.
A reader moving between two statements found the same material in different
places, or absent, with nothing saying which.

So the tab set is fixed here, in one list, and checked. It was taken from
`c/0020`, and on 2026-08-18 `Sources` was removed from it: sources now sit at
the end of the `Statement` tab as a `### Sources` subsection, which keeps them
beside the statement they support instead of a tab away, and stops a reader
having to leave the statement to see where it came from. `###` matters -- a
`##` there would create the sixth tab this list exists to forbid. The set is
now:

    Statement | Proof | Discussion | Open obligations

The rules are deliberately few, because a layout gate that also has opinions
about content stops being checkable:

  1. The body holds exactly one `::: {.panel-tabset}` div.
  2. Its direct `##` headings are exactly CANON, in that order, with none
     missing and none extra. A page with nothing to say under a heading says
     so under the heading; it does not drop it, because a dropped heading is
     indistinguishable from an unwritten one.
  3. No `##` heading sits outside the tabset. Anything below it renders as a
     loose section under the last tab, which is where the drift started.

Nested divs (callouts, other tabsets inside a tab) are counted, so a
`::: {.callout-note}` inside the Statement tab does not close it -- the bug
that made the first survey of this problem wrong.

    python3 scripts/tab_structure.py            # report every page's layout
    python3 scripts/tab_structure.py --check    # CI gate, exits 1 on drift

Standard library only, like the other gates here: PyYAML is not installed on
every machine, and a gate that cannot run locally is a gate that only fails
in CI.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted(ROOT.glob("c/0*/index.qmd"))
CANON = ["Statement", "Proof", "Discussion", "Open obligations"]

FENCE = re.compile(r"^(:{3,})\s*(\{[^}]*\})?\s*$")
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)


def layout(path):
    """(tab headings in order, headings outside the tabset, tabset count)."""
    text = path.read_text(encoding="utf-8")
    body = FRONT.sub("", text, count=1)
    stack, tabs, outside, opened = [], [], [], 0
    for line in body.splitlines():
        m = FENCE.match(line)
        if m:
            if m.group(2):
                is_tabset = "panel-tabset" in m.group(2)
                opened += is_tabset
                stack.append("tabset" if is_tabset else "div")
            elif stack:
                stack.pop()
            continue
        if line.startswith("## "):
            heading = line[3:].strip()
            if stack[:1] == ["tabset"] and len(stack) == 1:
                tabs.append(heading)
            else:
                outside.append(heading)
    return tabs, outside, opened


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit non-zero; write nothing")
    args = ap.parse_args()

    bad = 0
    for path in PAGES:
        tabs, outside, opened = layout(path)
        rel = path.relative_to(ROOT)
        problems = []
        if opened != 1:
            problems.append(f"{opened} panel-tabset div(s), expected exactly 1")
        if tabs != CANON:
            missing = [h for h in CANON if h not in tabs]
            extra = [h for h in tabs if h not in CANON]
            if missing:
                problems.append("missing tab(s): " + ", ".join(missing))
            if extra:
                problems.append("unexpected tab(s): " + ", ".join(extra))
            if not missing and not extra:
                problems.append("tabs out of order: " + " | ".join(tabs))
        if outside:
            problems.append("heading(s) outside the tabset: " + ", ".join(outside))
        if problems:
            bad += 1
            print(f"FAIL {rel}")
            for p in problems:
                print(f"       {p}")
        elif not args.check:
            print(f"ok   {rel}")

    if args.check:
        print(f"\n{len(PAGES)} statement page(s) checked, {bad} with drift")
    if bad:
        print("\nThe tab set is fixed by CANON in this file, taken from c/0020.\n"
              "A page with nothing to say under a heading keeps the heading and\n"
              "says so under it.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
