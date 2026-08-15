#!/usr/bin/env python3
"""
Consistency checks over the relation graph between statement leaves, on top
of the schema validation build_index.py already does (dangling/malformed
relation targets are caught there; this script assumes the schema is valid
and checks semantic consistency of the graph itself):

  - an `implies` edge from a statement whose proof_formal is complete (i.e.
    not "open") into a target still `category: research-open` -- the target
    should have been reclassified too (stale status);
  - an `equivalent-to` pair whose proof grades (pi) disagree without a `note`
    on the relation explaining why;
  - a leaf with `lean.mode: external-lean4` and `status.statement_formal !=
    open` but no `lean.commit` pinned.

Run after build_index.py (which fails first, and louder, on schema errors).
"""
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_badge import compute_pi  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STATEMENTS_DIR = ROOT / "c"


def load_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: no YAML frontmatter found")
    return yaml.safe_load(m.group(1)) or {}


def check(leaves):
    errors = []

    for lid, fm in leaves.items():
        status = fm.get("status") or {}
        for rel in fm.get("relations", []) or []:
            target = str(rel.get("target"))
            target_fm = leaves.get(target)
            if target_fm is None:
                continue  # dangling targets are build_index.py's job

            if rel.get("kind") == "implies":
                if status.get("proof_formal") != "open" and target_fm.get("category") == "research-open":
                    errors.append(
                        f"c/{lid}: 'implies' c/{target}, and c/{lid}'s proof_formal is "
                        f"complete, but c/{target} is still category: research-open"
                    )

            if rel.get("kind") == "equivalent-to" and not rel.get("note"):
                pi_self = compute_pi(
                    status.get("proof_informal"), status.get("proof_review"), status.get("proof_formal")
                )
                target_status = target_fm.get("status") or {}
                pi_target = compute_pi(
                    target_status.get("proof_informal"),
                    target_status.get("proof_review"),
                    target_status.get("proof_formal"),
                )
                if pi_self != pi_target:
                    errors.append(
                        f"c/{lid}: 'equivalent-to' c/{target}, but their proof grades "
                        f"disagree ({pi_self} vs {pi_target}) with no explanatory 'note'"
                    )

        lean = fm.get("lean") or {}
        if lean.get("mode") == "external-lean4" and status.get("statement_formal") != "open":
            if not lean.get("commit"):
                errors.append(
                    f"c/{lid}: lean.mode is external-lean4 and statement_formal is not "
                    "open, but lean.commit is missing"
                )

    return errors


def main():
    leaves = {}
    for path in sorted(STATEMENTS_DIR.glob("*/index.qmd")):
        fm = load_frontmatter(path)
        leaf_id = str(fm.get("id", path.parent.name))
        leaves[leaf_id] = fm

    errors = check(leaves)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"{len(errors)} relation consistency error(s)", file=sys.stderr)
        return 1

    print(f"{len(leaves)} leaf/leaves, relations consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
