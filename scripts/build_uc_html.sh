#!/usr/bin/env bash
#
# Build the HTML edition of UC for Gamers from the same LaTeX the PDF is built
# from, and drop it in surveys/uc-for-gamers/html/.
#
# Why a script rather than a note: three of the four steps below are the kind
# of thing that is rediscovered painfully. Each is a real failure this build
# hit, in the order it hit them.
#
#   1. hyperref must be loaded. ucgamers.sty's \fopl expands to \hyperlink, so
#      without it the interface boxes fail with "Undefined control sequence"
#      and the operation names vanish.
#
#   2. "mathjax" must be passed to make4ht. Without it tex4ht renders every
#      formula as an image: 5,886 of them, unsearchable and unstyleable.
#
#   3. dvisvgm must be TeX Live's, not Homebrew's standalone. The Homebrew
#      build cannot find texmf.cnf, so it emits "none of the default map files
#      could be found" and produces no files at all, while make4ht still writes
#      <img src="main0x.svg"> for all nine diagrams. The page then looks fine
#      until you notice every diagram is a broken image. Putting
#      /Library/TeX/texbin first is what fixes it.
#
#   4. MathJax needs the book's macros. The output is full of \Fnet, \op, \V
#      and 68 others, none of which MathJax knows. They are injected from
#      ucgamers.sty via scripts/gen_interface.py's loader, which already maps
#      the ones MathJax cannot render (\op is \textsc) through MACRO_OVERRIDES.
#
# Usage:  scripts/build_uc_html.sh [--check]
#         --check verifies the result and writes nothing to the repository.

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LATEX="$ROOT/surveys/uc-for-gamers/latex"
DEST="$ROOT/surveys/uc-for-gamers/html"
WORK="$(mktemp -d)"
CHECK_ONLY=0
[ "${1:-}" = "--check" ] && CHECK_ONLY=1

# Step 3: TeX Live's toolchain, ahead of any Homebrew standalone.
export PATH="/Library/TeX/texbin:$PATH"
export TEXINPUTS=".:$LATEX:"

command -v make4ht >/dev/null || { echo "make4ht not found (TeX Live)"; exit 1; }
command -v dvisvgm >/dev/null || { echo "dvisvgm not found (TeX Live)"; exit 1; }

echo "==> building in $WORK"
cp -r "$LATEX"/* "$WORK/"
cd "$WORK"

# Step 2: "mathjax" keeps formulas as text.
make4ht -u main.tex "mathjax" >build.log 2>&1
# make4ht exits non-zero on benign font warnings; judge by output, not status.
[ -f main.html ] || { echo "FAIL: no main.html produced"; tail -20 build.log; exit 1; }

# Step 4: give MathJax the book's own macros.
python3 - "$ROOT" <<'PY'
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(sys.argv[1]) / "scripts"))
import gen_interface as G
out = {}
for name, (nargs, body) in G.load_macros().items():
    if re.search(r'\\(textsc|textnormal|hyperlink|hypertarget|textcolor)\b', body) \
       and name not in G.MACRO_OVERRIDES:
        continue
    out[name] = [body, nargs] if nargs else body
# Two LaTeX built-ins the book uses in math mode that MathJax has no
# definition for. Without these they render as red literal text.
out.setdefault("P", r"\unicode{x00B6}")   # pilcrow, from $\P$ in the source
out.setdefault("allowbreak", "")           # a line-break hint, no visual effect
cfg = "window.MathJax = { tex: { tags: 'ams', macros: " + json.dumps(out) + " } };"
for f in pathlib.Path(".").glob("main*.html"):
    h = f.read_text(errors="ignore")
    # lambda, not a string: re.sub expands backslash escapes in a string
    # replacement, which turns json.dumps's correct \\mathbf back into
    # \mathbf and makes "\uparrow" an invalid JS unicode escape. That kills
    # the whole config with a SyntaxError, so MathJax silently defines none of
    # the macros and 70% of formulas render as red literal text.
    h2 = re.sub(r'MathJax = \{[^;]*\};', lambda _: cfg, h, count=1)
    if h2 == h:
        h2 = h.replace("</head>", f"<script>{cfg}</script>\n</head>", 1)
    # tex4ht leaves <title> empty for a book with a \titlepage.
    h2 = h2.replace("<title></title>",
                    "<title>UC for Gamers</title>", 1)
    f.write_text(h2)
print(f"    injected {len(out)} macros")
PY

echo "==> checking"
rc=0
chk() { if [ "$2" = "$3" ]; then echo "    ok   $1: $2"; else echo "    FAIL $1: got $2, want $3"; rc=1; fi; }

# NB: tex4ht emits single-quoted attributes. A grep for src="..." matches
# nothing here and, in a for-loop, silently reports success. Match both.
svg_refs=$(grep -oE "src=[\"'][^\"']*\.svg[\"']" main.html | sort -u | wc -l | tr -d ' ')
svg_files=$(ls -1 ./*.svg 2>/dev/null | wc -l | tr -d ' ')
chk "diagrams referenced vs produced" "$svg_refs" "$svg_files"
chk "unresolved cross-references" "$(grep -c '\[?\]' main.html || true)" "0"
chk "formulas left as images" "$(grep -o "<img[^>]*alt='\[[^P]" main.html | wc -l | tr -d ' ')" "0"
tex_h=$(grep -cE '^\\(chapter|section)\{' main.tex)
html_h=$(grep -oE '<h[23][^>]*>' main.html | wc -l | tr -d ' ')
echo "    info headings: $tex_h in source, $html_h in html"

if [ "$CHECK_ONLY" = "1" ]; then
  echo "==> --check: leaving $WORK in place, repository untouched"
  exit $rc
fi
[ $rc -ne 0 ] && { echo "==> checks failed, not installing"; exit $rc; }

echo "==> installing to $DEST"
mkdir -p "$DEST"
rm -f "$DEST"/*.html "$DEST"/*.css "$DEST"/*.svg
cp main*.html main.css ./*.svg "$DEST"/
echo "    $(ls -1 "$DEST" | wc -l | tr -d ' ') files, $(du -sh "$DEST" | cut -f1)"
rm -rf "$WORK"
