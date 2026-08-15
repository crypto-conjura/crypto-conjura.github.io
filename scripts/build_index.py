#!/usr/bin/env python3
"""
Walks c/*/index.qmd, validates each leaf's frontmatter against the Conjura
statement schema (see /schema/), and emits:

  - _generated/areas/<slug>.yml   one per the 19 fixed area slugs (always,
    even when empty, matching today's always-present topic pages)
  - _generated/model/<value>.yml, _generated/form/<value>.yml,
    _generated/assumption/<value>.yml   only for values actually in use
  - _generated/problems/<slug>.yml   the leaves belonging to each hub
  - _generated/all.yml   every browsable statement, for the global listing
  - conjura.json   the full index, keyed by 4-digit identifier

Withdrawn statements are excluded from the browsable facet/all listings (they
stay directly addressable at their own /c/<id>/ URL as a tombstone) but are
still included in conjura.json and in relation cross-checks.

Requires PyYAML (see requirements.txt) -- status_badge.py deliberately stays
dependency-free since it only ever needs a handful of scalar fields, but this
script needs to read nested structures (relations, lean, sources) that a
regex parser can't handle safely.
"""
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from status_badge import (  # noqa: E402
    compute_sigma,
    compute_pi,
    render_caption,
    render_statement_caption,
    render_proof_caption,
    _DASH,
    _GLYPH,
    LEGEND_URL,
)

ROOT = Path(__file__).resolve().parent.parent
STATEMENTS_DIR = ROOT / "c"
PROBLEMS_DIR = ROOT / "p"
GENERATED_DIR = ROOT / "_generated"
CONJURA_JSON = ROOT / "conjura.json"

# Kept in sync with _quarto.yml's sidebar. Do not silently rename or merge.
AREA_SLUGS = [
    "foundations", "idealized-models", "impossibility-results", "symmetric-key",
    "information-theoretic", "side-channel", "public-key", "lattices", "isogenies",
    "quantum", "zk", "proof-systems", "homomorphic-encryption", "obfuscation",
    "mpc", "secret-sharing", "universal-composability", "privacy", "consensus",
]
MODELS = {"rom", "prom", "icm", "ggm", "qrom", "standard", "other"}
FORMS = {
    "separation", "lower-bound", "tight-bound", "equivalence", "impossibility",
    "assumption", "characterization",
}
ASSUMPTION_CLASSES = {"unconditional", "falsifiable", "non-falsifiable"}
CATEGORIES = {"research-open", "research-solved", "test", "api", "withdrawn"}
RELATION_KINDS = {
    "generalizes", "specializes", "implies", "implied-by", "equivalent-to",
    "strengthens", "variant-of", "refutes", "refuted-by", "superseded-by",
}
LEAN_MODES = {"in-repo", "external-lean4", "other-system", "none"}
ID_RE = re.compile(r"^\d{4}$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")

STATUS_FIELDS = {
    "statement_informal": ("ai", "human"),
    "statement_formal": ("open", "ai", "human"),
    "statement_match": ("open", "ai", "human"),
    "proof_informal": ("open", "ai", "human"),
    "proof_review": ("ai", "human"),
    "proof_formal": ("open", "ai", "human"),
}

REQUIRED_FIELDS = [
    "id", "problem", "title", "areas", "model", "form", "assumption_class",
    "category", "statement_sha", "revision", "status", "status_summary",
]


def load_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?\n)---\n", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: no YAML frontmatter found")
    return yaml.safe_load(m.group(1)) or {}


def parse_obligations(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(
        r"^##\s+Open obligations\s*\n(.*?)(?=^#{1,6}\s|\Z)", text, re.MULTILINE | re.DOTALL
    )
    if not m:
        return []
    obligations = []
    for line in m.group(1).splitlines():
        item = re.match(r"^\s*-\s+\[( |x|X)\]\s+(.*\S)\s*$", line)
        if item:
            obligations.append({"done": item.group(1).lower() == "x", "text": item.group(2)})
    return obligations


def validate_leaf(fm, path, errors):
    def err(msg):
        errors.append(f"{path}: {msg}")

    for field in REQUIRED_FIELDS:
        if field not in fm:
            err(f"missing required field '{field}'")

    leaf_id = str(fm.get("id", path.parent.name))
    if not ID_RE.match(leaf_id):
        err(f"id {leaf_id!r} is not a 4-digit zero-padded string")
    elif path.parent.name != leaf_id:
        err(f"id {leaf_id!r} does not match directory name {path.parent.name!r}")

    areas = fm.get("areas")
    if not isinstance(areas, list) or not areas:
        err("areas must be a non-empty list")
    else:
        for a in areas:
            if a not in AREA_SLUGS:
                err(f"area {a!r} is not one of the 19 fixed area slugs")

    if "model" in fm and fm["model"] not in MODELS:
        err(f"model {fm['model']!r} not in {sorted(MODELS)}")
    if "form" in fm and fm["form"] not in FORMS:
        err(f"form {fm['form']!r} not in {sorted(FORMS)}")
    if "assumption_class" in fm and fm["assumption_class"] not in ASSUMPTION_CLASSES:
        err(f"assumption_class {fm['assumption_class']!r} not in {sorted(ASSUMPTION_CLASSES)}")
    if "category" in fm and fm["category"] not in CATEGORIES:
        err(f"category {fm['category']!r} not in {sorted(CATEGORIES)}")
    if fm.get("category") == "withdrawn":
        if not str(fm.get("withdrawn_reason", "")).strip():
            err("category is withdrawn but withdrawn_reason is missing or empty")
        relations = fm.get("relations", []) or []
        if not any(r.get("kind") == "superseded-by" for r in relations):
            err("category is withdrawn but no {kind: superseded-by, target: ...} relation is present")

    problem_slug = fm.get("problem")
    if not isinstance(problem_slug, str) or not problem_slug:
        err("problem must be a single non-empty hub slug")
    elif not (PROBLEMS_DIR / problem_slug / "index.qmd").exists():
        err(f"problem {problem_slug!r} has no matching p/{problem_slug}/index.qmd")

    status = fm.get("status") or {}
    for field, allowed in STATUS_FIELDS.items():
        if field not in status:
            err(f"status.{field} missing")
        elif status[field] not in allowed:
            err(f"status.{field} = {status[field]!r} not in {allowed}")

    if not SHA_RE.match(str(fm.get("statement_sha", ""))):
        err("statement_sha is not a 64-character hex sha256 digest")

    for rel in fm.get("relations", []) or []:
        if rel.get("kind") not in RELATION_KINDS:
            err(f"relation kind {rel.get('kind')!r} not in {sorted(RELATION_KINDS)}")
        target = str(rel.get("target", ""))
        if not ID_RE.match(target):
            err(f"relation target {target!r} is not a 4-digit id")

    lean = fm.get("lean") or {}
    if lean and lean.get("mode") not in LEAN_MODES:
        err(f"lean.mode {lean.get('mode')!r} not in {sorted(LEAN_MODES)}")

    return leaf_id


def listing_item(leaf_id, fm):
    # The listing template renders the badge from these small primitive
    # values (mirroring status_badge.py's render_badge_svg) rather than from
    # a pre-rendered HTML string: Quarto's custom-listing pipeline escapes
    # (and applies smart-typography to) whole string field values loaded
    # from a contents YAML file before a template ever sees them, so passing
    # a full <a><svg>...</svg></a> blob through as one field renders as
    # literal escaped text, not the badge. Small values substituted into
    # markup that's otherwise static in the .ejs.md template don't have this
    # problem, the same way item.model/item.form already render correctly.
    status = fm.get("status") or {}
    sigma = compute_sigma(
        status.get("statement_informal"), status.get("statement_formal"), status.get("statement_match")
    )
    pi = compute_pi(status.get("proof_informal"), status.get("proof_review"), status.get("proof_formal"))
    return {
        "id": leaf_id,
        "title": fm["title"],
        "short_title": fm.get("short_title", fm["title"]),
        "path": f"/c/{leaf_id}/",
        "badge_sigma": sigma,
        "badge_pi": pi,
        "badge_sealed": pi == 4 and sigma >= 4,
        "badge_dash": _DASH[status.get("statement_match")] or "",
        "badge_glyph": _GLYPH[pi],
        "badge_caption": render_caption(status),
        "badge_statement_caption": render_statement_caption(status),
        "badge_proof_caption": render_proof_caption(status),
        "badge_legend_url": LEGEND_URL,
        "status_summary": fm["status_summary"],
        "model": fm["model"],
        "form": fm["form"],
        "assumption_class": fm["assumption_class"],
        "category": fm["category"],
        "open_obligations": sum(1 for o in fm["_obligations"] if not o["done"]),
    }


def write_yaml(path, items):
    path.write_text(yaml.safe_dump(items, sort_keys=False, allow_unicode=True), encoding="utf-8")


def emit(leaves):
    for sub in ("areas", "model", "form", "assumption", "problems"):
        (GENERATED_DIR / sub).mkdir(parents=True, exist_ok=True)

    browsable = {lid: fm for lid, fm in leaves.items() if fm.get("category") != "withdrawn"}

    for area in AREA_SLUGS:
        items = sorted(
            (listing_item(lid, fm) for lid, fm in browsable.items() if area in (fm.get("areas") or [])),
            key=lambda x: x["id"],
        )
        write_yaml(GENERATED_DIR / "areas" / f"{area}.yml", items)

    for facet_dir, field in (("model", "model"), ("form", "form"), ("assumption", "assumption_class")):
        used = sorted({fm[field] for fm in browsable.values() if field in fm})
        for value in used:
            items = sorted(
                (listing_item(lid, fm) for lid, fm in browsable.items() if fm.get(field) == value),
                key=lambda x: x["id"],
            )
            write_yaml(GENERATED_DIR / facet_dir / f"{value}.yml", items)

    problems = sorted({fm["problem"] for fm in leaves.values() if "problem" in fm})
    for slug in problems:
        items = sorted(
            (listing_item(lid, fm) for lid, fm in leaves.items() if fm.get("problem") == slug),
            key=lambda x: x["id"],
        )
        write_yaml(GENERATED_DIR / "problems" / f"{slug}.yml", items)

    all_items = sorted((listing_item(lid, fm) for lid, fm in browsable.items()), key=lambda x: x["id"])
    write_yaml(GENERATED_DIR / "all.yml", all_items)

    index = {}
    for lid, fm in leaves.items():
        index[lid] = {
            "title": fm.get("title"),
            "short_title": fm.get("short_title", fm.get("title")),
            "problem": fm.get("problem"),
            "areas": fm.get("areas"),
            "model": fm.get("model"),
            "form": fm.get("form"),
            "assumption_class": fm.get("assumption_class"),
            "category": fm.get("category"),
            "revision": fm.get("revision"),
            "statement_sha": fm.get("statement_sha"),
            "status": fm.get("status"),
            "status_summary": fm.get("status_summary"),
            "obligations": fm.get("_obligations"),
            "relations": fm.get("relations", []),
            "lean": fm.get("lean", {}),
            "sources": fm.get("sources", []),
            "path": f"/c/{lid}/",
        }
    CONJURA_JSON.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {CONJURA_JSON.relative_to(ROOT)} ({len(index)} statements)")

    for sub, count in (
        ("_generated/areas", len(AREA_SLUGS)),
    ):
        print(f"wrote {sub}/ ({count} files)")


def build():
    errors = []
    leaves = {}
    for path in sorted(STATEMENTS_DIR.glob("*/index.qmd")):
        fm = load_frontmatter(path)
        leaf_id = validate_leaf(fm, path, errors)
        fm["_obligations"] = parse_obligations(path)
        leaves[leaf_id] = fm

    for leaf_id, fm in leaves.items():
        for rel in fm.get("relations", []) or []:
            target = str(rel.get("target"))
            if target not in leaves:
                errors.append(f"c/{leaf_id}: relation target {target!r} does not exist")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"{len(errors)} schema error(s), {len(leaves)} leaf/leaves scanned", file=sys.stderr)
        return 1

    emit(leaves)
    print(f"{len(leaves)} leaf/leaves scanned, schema OK")
    return 0


if __name__ == "__main__":
    sys.exit(build())
