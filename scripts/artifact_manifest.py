#!/usr/bin/env python3
"""Detect when a generated artifact no longer matches the LaTeX it came from.

Every `.tex` on this site has generated output committed beside it. Nothing
else notices when the two drift, so an edited source with an unrebuilt PDF
leaves a page whose "Download LaTeX source" and "View PDF" links disagree with
each other. On an archive that is a content error, not a build annoyance.

This is the same idea as `gen_interface.py --check` and `status_badge.py`'s
`statement_sha`, applied to whole artifacts instead of fragments: hash the
inputs, record the hash beside the outputs, and fail when they diverge.

It detects drift in **both** directions:

  * source edited, output not rebuilt -- the common case;
  * output edited by hand, so it is no longer what the build would produce.
    `build_uc_html.sh` warns that a hand-edit to its output is destroyed by the
    next run with no warning; recording output hashes is what makes that
    visible instead of silent.

It never builds anything and never rewrites an artifact. CI runs `ubuntu-latest`
with no TeX at all, and `build_uc_html.sh` wants macOS TeX Live, `make4ht` and
TeX Live's own `dvisvgm`. Detecting staleness is cheap and needs none of that;
rebuilding is left to a human on a machine that can.

    python3 scripts/artifact_manifest.py --check     # CI gate, exits 1 on drift
    python3 scripts/artifact_manifest.py --update    # re-baseline after a rebuild

Standard library only: PyYAML is not installed on every machine here, and a
gate that cannot run locally is a gate that only fails in CI.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
# Repo root, beside conjura.json, and committed: _generated/ is gitignored
# because everything in it is rebuilt at deploy time, whereas this file *is*
# the baseline. A manifest CI regenerates before checking proves nothing.
MANIFEST = ROOT / "artifacts.json"

# Source suffixes that actually change a build's output. A stray .log or .aux
# in a latex/ folder is build litter, not an input.
SOURCE_SUFFIXES = {".tex", ".cls", ".sty", ".bib", ".bst"}


def artifacts():
    """(name, input globs, output globs, how to rebuild it).

    Deliberately not covered:

    * `latex/uc/**` -> the encyclopedia interface boxes. `gen_interface.py
      --check` already regenerates those from their fragment and fails on
      disagreement, and two gates guarding one thing disagree eventually.
    * `latex/conjectures/**`, `latex/books/**` -> the staging area for drafts
      that are not yet site pages. Promoting one is a manual editorial act,
      not a build, so there is no output to be stale against.
    """
    out = []
    for d in sorted((ROOT / "c").glob("0*")):
        if (d / "latex").is_dir() and (d / "pdf").is_dir():
            out.append((
                f"c/{d.name}",
                [f"c/{d.name}/latex/**/*"],
                [f"c/{d.name}/pdf/*.pdf"],
                f"cd c/{d.name}/latex && pdflatex main.tex   # and any other .tex beside it",
            ))
    out.append((
        "papers/uber-groups-rsr",
        ["latex/papers/uber-groups-rsr/**/*"],
        ["papers/uber-groups-rsr/pdf/*.pdf", "papers/uber-groups-rsr/latex/**/*"],
        "cd latex/papers/uber-groups-rsr && pdflatex main.tex, then copy source and PDF into papers/uber-groups-rsr/",
    ))
    book = book_inputs()
    out.append((
        "surveys/uc-for-gamers/pdf",
        book,
        ["surveys/uc-for-gamers/pdf/*.pdf"],
        "cd surveys/uc-for-gamers/latex && pdflatex main.tex",
    ))
    out.append((
        "surveys/uc-for-gamers/html",
        book,
        ["surveys/uc-for-gamers/html/*"],
        "scripts/build_uc_html.sh   # ~4 minutes; needs TeX Live, make4ht, TeX Live's dvisvgm",
    ))
    return out


def book_inputs():
    """Globs for the files the book is actually built from.

    Not `latex/**/*`: `functionalities/` holds one fragment per encyclopedia
    entry, and `main.tex` `\\input`s only the handful of boxes the book itself
    typesets. The other ninety-odd are the encyclopedia's source, rendered to
    `uc/.../index.qmd` by `gen_interface.py` and gated by its `--check`, so
    counting them here would ask for a book rebuild every time an entry is
    filled in -- a rebuild that cannot change a single page of the book. That
    is the same reasoning that keeps `latex/uc/**` out of this file entirely.

    Read from `main.tex` rather than hardcoded, so a fragment promoted into
    the book starts being watched the moment it is `\\input`.

    The `.sty` glob is `latex/*.sty`, not `latex/**/*.sty`, and that is the
    same decision one level down. `functionalities/encyclopedia.sty` holds the
    names of those other ninety-odd functionalities, and every entry written
    adds one `\\newcommand` to it; `main.tex` does not load that file, so
    nothing in it can reach a page of the book. `ucgamers.sty` sits beside
    `main.tex` and is watched, because an edit to the book's own notation must
    still invalidate the PDF.
    """
    latex = ROOT / "surveys" / "uc-for-gamers" / "latex"
    globs = ["surveys/uc-for-gamers/latex/*.tex",
             "surveys/uc-for-gamers/latex/*.sty"]
    main = latex / "main.tex"
    if main.exists():
        for m in re.finditer(r"\\input\{(functionalities/[^}]+)\}",
                             main.read_text()):
            name = m.group(1)
            globs.append("surveys/uc-for-gamers/latex/%s%s"
                         % (name, "" if name.endswith(".tex") else ".tex"))
    return globs


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def collect(globs, sources_only):
    """Map of repo-relative path -> content hash, sorted for determinism."""
    files = {}
    for g in globs:
        for p in sorted(ROOT.glob(g)):
            if not p.is_file() or p.name.startswith("."):
                continue
            if sources_only and p.suffix.lower() not in SOURCE_SUFFIXES:
                continue
            files[str(p.relative_to(ROOT))] = digest(p)
    return dict(sorted(files.items()))


def state():
    st = {}
    for name, ins, outs, cmd in artifacts():
        inputs = collect(ins, sources_only=True)
        outputs = collect(outs, sources_only=False)
        if not inputs:
            continue
        joined = "".join(f"{k}:{v}" for k, v in inputs.items())
        st[name] = {
            "rebuild": cmd,
            "input_digest": hashlib.sha256(joined.encode()).hexdigest()[:16],
            "inputs": inputs,
            "outputs": outputs,
        }
    return st


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true", help="fail if any artifact is stale")
    g.add_argument("--update", action="store_true", help="re-baseline after a rebuild")
    args = ap.parse_args()

    now = state()

    if args.update:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps(now, indent=1, sort_keys=True) + "\n")
        n_out = sum(len(a["outputs"]) for a in now.values())
        print(f"wrote {MANIFEST.relative_to(ROOT)}: {len(now)} artifacts, "
              f"{sum(len(a['inputs']) for a in now.values())} inputs, {n_out} outputs")
        return 0

    if not MANIFEST.exists():
        print(f"FAIL no manifest at {MANIFEST.relative_to(ROOT)}; run --update", file=sys.stderr)
        return 1
    was = json.loads(MANIFEST.read_text())

    stale = []
    for name, cur in now.items():
        old = was.get(name)
        if old is None:
            stale.append((name, cur["rebuild"], [f"new artifact, not yet in the manifest"]))
            continue
        why = []
        if old["input_digest"] != cur["input_digest"]:
            changed = [k for k, v in cur["inputs"].items() if old["inputs"].get(k) != v]
            gone = [k for k in old["inputs"] if k not in cur["inputs"]]
            why += [f"source changed: {p}" for p in changed[:6]]
            why += [f"source removed: {p}" for p in gone[:3]]
        for k, v in cur["outputs"].items():
            if k in old["outputs"] and old["outputs"][k] != v:
                why.append(f"output edited since it was built: {k}")
        missing = [k for k in old["outputs"] if k not in cur["outputs"]]
        why += [f"output missing: {p}" for p in missing[:3]]
        if why:
            stale.append((name, cur["rebuild"], why))

    for name in was:
        if name not in now:
            stale.append((name, "remove it from the manifest with --update",
                          ["artifact is in the manifest but no longer on disk"]))

    if not stale:
        print(f"ok   {len(now)} artifacts, all outputs match their source")
        return 0

    print(f"FAIL {len(stale)} artifact(s) no longer match their source:\n", file=sys.stderr)
    for name, cmd, why in stale:
        print(f"  {name}", file=sys.stderr)
        for w in why:
            print(f"      {w}", file=sys.stderr)
        print(f"      rebuild: {cmd}", file=sys.stderr)
        print(f"      then:    python3 scripts/artifact_manifest.py --update\n", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
