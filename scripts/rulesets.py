#!/usr/bin/env python3
"""
Keep this repository's branch rulesets in a file rather than only in GitHub's
settings UI, so that a protection rule is reviewable, has its reasoning written
down next to it, and can be restored after someone changes it by hand.

Desired state lives in `.github/rulesets/*.json`, one ruleset per file, in the
exact body shape the REST API takes. `.github/rulesets/README.md` explains why
each rule in `protect-main.json` was chosen, including the two settings that
look wrong until you know what they prevent.

  python3 scripts/rulesets.py --check    compare live against the files
  python3 scripts/rulesets.py --apply    create or update to match the files
  python3 scripts/rulesets.py --show     print the live rulesets

`--check` exits 1 on any drift, matching the other check modes in this
directory. It needs read access only. `--apply` needs repository admin.

Comparison is a subset match: every field named in the file must match what is
live, and any rule live that the file does not name is reported. Fields the API
adds on its own (id, timestamps, _links, node_id, source) are ignored, because
comparing whole documents would report drift on every call.

A ruleset present on the repository with no file here is reported by `--check`
but never modified or deleted, so this directory can be adopted one ruleset at
a time without it treating everything else as drift to erase. `--apply` only
ever creates or updates.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULESET_DIR = ROOT / ".github" / "rulesets"

# Set by the API, not by us. Present in every response, never in a request.
GENERATED = {"id", "created_at", "updated_at", "_links", "node_id", "source",
             "source_type", "current_user_can_bypass"}


def gh(*args, body=None):
    """Run `gh api` and return parsed JSON, or exit with the API's own error."""
    proc = subprocess.run(["gh", "api", *args], input=body, capture_output=True,
                          text=True)
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout).strip()
        sys.exit(f"gh api {' '.join(args)} failed:\n  {err}")
    return json.loads(proc.stdout) if proc.stdout.strip() else None


def slug():
    """owner/repo from the origin remote, so this is not pinned to one fork."""
    url = subprocess.run(["git", "-C", str(ROOT), "remote", "get-url", "origin"],
                         capture_output=True, text=True).stdout.strip()
    m = re.search(r"[:/]([^/:]+/[^/]+?)(?:\.git)?$", url)
    if not m:
        sys.exit(f"cannot parse an owner/repo out of the origin remote: {url!r}")
    return m.group(1)


def strip(obj):
    """Drop API-generated keys so a request body and a response can be compared."""
    if isinstance(obj, dict):
        return {k: strip(v) for k, v in obj.items() if k not in GENERATED}
    if isinstance(obj, list):
        return [strip(v) for v in obj]
    return obj


# Roles whose actor_id carries no information. The API takes an id for these on
# write and returns null for them on read, so comparing the id reports a
# difference that no number of --apply runs can ever settle.
IMPLICIT_ID_ACTORS = {"OrganizationAdmin", "EnterpriseOwner"}


def actor_key(a):
    kind = a.get("actor_type")
    ident = None if kind in IMPLICIT_ID_ACTORS else a.get("actor_id")
    return (kind, ident, a.get("bypass_mode"))


def drift(want, live):
    """Return a list of human-readable differences, empty when live satisfies want."""
    out = []

    for field in ("name", "target", "enforcement"):
        if field in want and want[field] != live.get(field):
            out.append(f"{field}: want {want[field]!r}, live {live.get(field)!r}")

    if "conditions" in want:
        w = strip(want["conditions"])
        got = strip(live.get("conditions") or {})
        if json.dumps(w, sort_keys=True) != json.dumps(got, sort_keys=True):
            out.append(f"conditions: want {json.dumps(w, sort_keys=True)}, "
                       f"live {json.dumps(got, sort_keys=True)}")

    if "bypass_actors" in want:
        w = sorted(actor_key(a) for a in want["bypass_actors"])
        got = sorted(actor_key(a) for a in (live.get("bypass_actors") or []))
        if w != got:
            out.append(f"bypass_actors: want {w}, live {got}")

    if "rules" in want:
        want_rules = {r["type"]: strip(r.get("parameters") or {})
                      for r in want["rules"]}
        live_rules = {r["type"]: strip(r.get("parameters") or {})
                      for r in (live.get("rules") or [])}
        for t, params in want_rules.items():
            if t not in live_rules:
                out.append(f"rule {t}: missing")
                continue
            # Subset, not equality: the API fills in defaults we did not set,
            # and reporting those as drift would make --check useless.
            for k, v in params.items():
                if live_rules[t].get(k) != v:
                    out.append(f"rule {t}.{k}: want {v!r}, "
                               f"live {live_rules[t].get(k)!r}")
        for t in live_rules:
            if t not in want_rules:
                out.append(f"rule {t}: live but not in the file")

    return out


def load():
    if not RULESET_DIR.is_dir():
        sys.exit(f"no ruleset directory at {RULESET_DIR.relative_to(ROOT)}")
    files = sorted(RULESET_DIR.glob("*.json"))
    if not files:
        sys.exit(f"no *.json in {RULESET_DIR.relative_to(ROOT)}")
    want = {}
    for f in files:
        try:
            doc = json.loads(f.read_text())
        except json.JSONDecodeError as e:
            sys.exit(f"{f.relative_to(ROOT)} is not valid JSON: {e}")
        if "name" not in doc:
            sys.exit(f"{f.relative_to(ROOT)} has no \"name\"")
        if doc["name"] in want:
            sys.exit(f"two files define a ruleset named {doc['name']!r}")
        want[doc["name"]] = (f, doc)
    return want


def live_rulesets(repo):
    """Full detail for each ruleset. The list endpoint returns a summary only."""
    return {r["name"]: gh(f"repos/{repo}/rulesets/{r['id']}")
            for r in (gh(f"repos/{repo}/rulesets") or [])}


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--check"
    if mode not in ("--check", "--apply", "--show"):
        sys.exit(__doc__.strip())

    repo = slug()
    live = live_rulesets(repo)

    if mode == "--show":
        if not live:
            print(f"{repo}: no rulesets")
        for name, r in live.items():
            print(f"{name}  (id {r['id']}, {r['target']}, {r['enforcement']})")
            for rule in r.get("rules") or []:
                params = strip(rule.get("parameters") or {})
                print(f"    {rule['type']}"
                      + (f"  {json.dumps(params, sort_keys=True)}" if params else ""))
            for a in r.get("bypass_actors") or []:
                print(f"    bypass: {a.get('actor_type')} "
                      f"{a.get('actor_id')} ({a.get('bypass_mode')})")
        return 0

    want = load()
    problems = 0

    for name, (path, doc) in want.items():
        rel = path.relative_to(ROOT)
        if name not in live:
            if mode == "--check":
                print(f"MISSING  {name}  ({rel}) is not on {repo}")
                problems += 1
            else:
                created = gh(f"repos/{repo}/rulesets", "-X", "POST", "--input", "-",
                             body=json.dumps(doc))
                print(f"created  {name}  (id {created['id']}) from {rel}")
            continue

        d = drift(doc, live[name])
        if not d:
            print(f"ok       {name}  matches {rel}")
            continue
        if mode == "--check":
            print(f"DRIFT    {name}  ({rel})")
            for line in d:
                print(f"           {line}")
            problems += 1
        else:
            gh(f"repos/{repo}/rulesets/{live[name]['id']}", "-X", "PUT",
               "--input", "-", body=json.dumps(doc))
            print(f"updated  {name}  (id {live[name]['id']}) to match {rel}")
            for line in d:
                print(f"           was: {line}")

    for name in live:
        if name not in want:
            print(f"UNMANAGED {name} is on {repo} with no file in "
                  f"{RULESET_DIR.relative_to(ROOT)} (left alone)")
            if mode == "--check":
                problems += 1

    if mode == "--check" and problems:
        print(f"\n{problems} ruleset(s) differ. "
              f"Run `python3 scripts/rulesets.py --apply` to reconcile.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
