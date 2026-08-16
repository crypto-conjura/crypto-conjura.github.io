#!/usr/bin/env bash
#
# Build the HTML edition of UC for Gamers from the same LaTeX the PDF is built
# from, and drop it in surveys/uc-for-gamers/html/.
#
# Why a script rather than a note: every step below is the kind of thing that
# is rediscovered painfully. Each is a real failure this build hit, in the
# order it hit them.
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
#   5. Splitting needs the two Unicode characters in the source declared.
#      Four headings use \texorpdfstring whose PDF branch is a literal Δ or π
#      (chapters 18 and 19, sections 21.2 and 21.4). Unsplit, nothing reads
#      that branch. Split, tex4ht writes those titles into main.4ct and feeds
#      them back through LaTeX, where inputenc has no definition for either
#      and errors. The build still finishes and still writes 59 files, so the
#      only symptom is a table of contents reading "18 -Delayed Network" and
#      "The protocol _Sig". Declaring both characters is what fixes it.
#
#   6. The sidebar is generated here, never hand-written into the HTML.
#      Every main*.html is overwritten on each run, so an edit made in the
#      output is destroyed by the next build with no warning. The navigation
#      is built from tex4ht's own table of contents, which already carries
#      resolved chapter and section numbering, so adding a chapter to the
#      book updates the sidebar with no change to this script.
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

# Step 5: declare the two non-ASCII characters, in the build copy only. The
# source stays as the PDF build wants it.
python3 - <<'PY' || { echo "FAIL: step 5 (unicode declarations)"; exit 1; }
import pathlib, re
p = pathlib.Path("main.tex")
s = p.read_text()
decl = ("\\usepackage[utf8]{inputenc}\n"
        "\\DeclareUnicodeCharacter{0394}{\\ensuremath{\\Delta}}\n"
        "\\DeclareUnicodeCharacter{03C0}{\\ensuremath{\\pi}}")
# lambda, not a string, for the same reason step 4 needs one: a string
# replacement expands backslash escapes, and "\usepackage" starts with an
# invalid \u escape. As a string this raises re.PatternError, and without
# set -e the build then runs happily on undeclared Unicode.
s, n = re.subn(r"\\usepackage\[utf8\]\{inputenc\}", lambda _: decl, s, count=1)
assert n == 1, "inputenc line not found -- step 5 needs updating"
p.write_text(s)
PY

# Step 2: "mathjax" keeps formulas as text.
# "3" splits at section level; "sections+" adds the next/prev/up crosslinks.
make4ht -u main.tex "mathjax,3,sections+" >build.log 2>&1
# make4ht exits non-zero on benign font warnings; judge by output, not status.
[ -f main.html ] || { echo "FAIL: no main.html produced"; tail -20 build.log; exit 1; }
echo "    $(ls -1 main*.html | wc -l | tr -d ' ') pages"

# Step 4: give MathJax the book's own macros.
python3 - "$ROOT" <<'PY' || { echo "FAIL: step 4 (mathjax macros)"; exit 1; }
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
    h2 = h2.replace("<title></title>", "<title>UC for Gamers</title>", 1)
    f.write_text(h2)
print(f"    injected {len(out)} macros")
PY

# Step 6: build the sidebar from tex4ht's own table of contents and put it on
# every page.
python3 - <<'PY' || { echo "FAIL: step 6 (sidebar)"; exit 1; }
import pathlib, re

toc_src = pathlib.Path("main.html").read_text(errors="ignore")
block = re.search(r"<div class='tableofcontents'>(.*?)</div>", toc_src, re.S)
assert block, "no tableofcontents in main.html -- did the split option change?"

# Each entry is: <span class='<kind>Toc'>[number] <a href='file#id' ...>title</a></span>
ENTRY = re.compile(
    r"<span class='(likechapter|chapter|section)Toc'>\s*"
    r"([0-9.]*)\s*"
    r"<a href='([^']+)'[^>]*>(.*?)</a>", re.S)

# Once step 5 declares them, tex4ht renders those two characters as inline
# MathJax, so the raw title reads
#   <span class='mathjax-inline'>\(\relax \Delta \)</span>-Delayed Network
# Navigation should not depend on MathJax having loaded, so map the two the
# book uses back to text. Anything else left in math mode is a new case and
# fails the build rather than shipping a sidebar entry full of backslashes.
MATH = {r"\Delta": "Δ", r"\pi": "π"}

def detex(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"\\\((.*?)\\\)",
               lambda m: MATH.get(m.group(1).replace("\\relax", "").strip(),
                                  m.group(0)), t)
    return " ".join(t.split())

entries = []
for kind, num, href, title in ENTRY.findall(block.group(1)):
    entries.append((kind, num, href, detex(title)))
assert entries, "table of contents parsed to nothing"
stuck = [t for _, _, _, t in entries if "\\" in t]
assert not stuck, f"titles still carrying LaTeX, extend MATH: {stuck}"

# tex4ht lists the unnumbered front and back matter twice: once as a
# chapterToc whose href points into the contents page's own listing, and once
# as a likechapterToc pointing at the real page. Keeping both would put
# "Introduction", "Pending Issues" and "Bibliography" in the sidebar twice,
# half of them landing on the wrong page. Numbered chapters are never
# affected, so dropping unnumbered chapterToc entries is the whole fix.
# The "Contents" entry goes too: in a sidebar, that is the sidebar.
entries = [(k, n, h, t) for k, n, h, t in entries
           if not (k == "chapter" and not n) and t.lower() != "contents"]

def li(kind, num, href, title, current):
    cls = f"ucnav-{kind}" + (" ucnav-current" if current else "")
    aria = " aria-current='page'" if current else ""
    n = f"<span class='ucnav-num'>{num}</span> " if num else ""
    return f"<li class='{cls}'><a href='{href}'{aria}>{n}{title}</a></li>"

TOGGLE = ("<button class='ucnav-toggle' type='button' aria-controls='ucnav' "
          "aria-expanded='false'>Contents</button>")

JS = """<script>
(function () {
  var nav = document.getElementById('ucnav'),
      btn = document.querySelector('.ucnav-toggle');
  if (!nav || !btn) return;
  btn.addEventListener('click', function () {
    var open = document.body.classList.toggle('ucnav-open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  // Keep the current chapter in view without scrolling the page itself.
  var cur = nav.querySelector('.ucnav-current');
  if (cur) nav.scrollTop = cur.offsetTop - nav.clientHeight / 2;
})();
</script>"""

pages = sorted(pathlib.Path(".").glob("main*.html"))
for f in pages:
    items = "\n".join(
        li(k, n, h, t, h.split("#")[0] == f.name) for k, n, h, t in entries)
    nav = (f"<nav class='ucnav' id='ucnav' aria-label='Contents'>"
           f"<div class='ucnav-head'><a href='main.html'>UC for Gamers</a></div>"
           f"<ul>{items}</ul></nav>")
    h = f.read_text(errors="ignore")
    # Insert after <body...>, and close the wrapper before </body>. tex4ht
    # writes "<body>" plainly, but match attributes in case that changes.
    # lambda again: chapter titles carry backslashes, and as a string
    # replacement the first "\D" of a \Delta raises re.PatternError.
    ins = TOGGLE + nav + "<div class='ucnav-body'>"
    h2, n = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + ins, h, count=1)
    if n == 0:
        continue
    h2 = h2.replace("</body>", "</div>" + JS + "</body>", 1)
    f.write_text(h2)
print(f"    sidebar on {len(pages)} pages, {len(entries)} entries")

CSS = """

/* ---- generated by scripts/build_uc_html.sh, step 6 -------------------- */
/* This page is standalone tex4ht output and inherits nothing from the
   site's Quarto theme, so the sidebar carries its own palette. */
:root {
  --ucnav-w: 19rem;
  --ucnav-bg: #f6f6f4;
  --ucnav-fg: #33332f;
  --ucnav-muted: #77776f;
  --ucnav-rule: #dededa;
  --ucnav-accent: #7a2d1e;
}
@media (prefers-color-scheme: dark) {
  :root {
    --ucnav-bg: #1c1c1a;
    --ucnav-fg: #d8d8d2;
    --ucnav-muted: #8f8f87;
    --ucnav-rule: #34342f;
    --ucnav-accent: #e0846b;
  }
}
/* tex4ht sets "body { margin: 1em auto; max-width: 80ch }", which centres the
   reading column in the whole viewport. Offsetting that column by the
   sidebar width stacks the two and leaves a wide gap down the middle. A
   two-column grid on the body instead lets the column centre itself in what
   is actually left over. */
body {
  margin: 0; padding: 0; max-width: none;
  display: grid; grid-template-columns: var(--ucnav-w) minmax(0, 1fr);
}
.ucnav {
  grid-column: 1;
  position: sticky; top: 0; align-self: start;
  height: 100vh; overflow-y: auto; overscroll-behavior: contain;
  background: var(--ucnav-bg); color: var(--ucnav-fg);
  border-right: 1px solid var(--ucnav-rule);
  font-size: 0.82rem; line-height: 1.4; padding: 1rem 0 3rem;
  -webkit-overflow-scrolling: touch; z-index: 20;
}
.ucnav-head { font-weight: 700; padding: 0 1rem 0.75rem; }
.ucnav-head a, .ucnav a { color: inherit; text-decoration: none; }
.ucnav ul { list-style: none; margin: 0; padding: 0; }
.ucnav li a {
  display: block; padding: 0.28rem 1rem 0.28rem 1.6rem;
  border-left: 3px solid transparent;
}
.ucnav li a:hover { background: rgba(127,127,127,0.12); }
.ucnav-num { color: var(--ucnav-muted); }
.ucnav-chapter > a, .ucnav-likechapter > a { font-weight: 600; }
.ucnav-section > a { padding-left: 2.9rem; color: var(--ucnav-muted); }
.ucnav-current > a {
  border-left-color: var(--ucnav-accent); color: var(--ucnav-accent);
  background: rgba(127,127,127,0.10); font-weight: 700;
}
.ucnav-body {
  /* border-box, or the 0.62em of padding is added to a width already set to
     100% of the column. That is 20px of horizontal overflow on a 390px
     WebKit viewport, and none at all on Chromium, so it only shows up on
     one of the two phones tested. */
  box-sizing: border-box;
  grid-column: 2; min-width: 0; width: 100%; max-width: 80ch;
  margin: 1em auto; padding: 0 0.62em;
}
.ucnav-toggle { display: none; }

/* The book sets its own widths on these; keep them inside the column. */
.ucnav-body img, .ucnav-body svg, .ucnav-body table { max-width: 100%; }

@media (max-width: 60rem) {
  /* A sidebar holding its column at this width is how horizontal overflow
     gets reintroduced, so it leaves the grid and goes off-canvas instead. */
  body { grid-template-columns: minmax(0, 1fr); }
  .ucnav {
    position: fixed; top: 0; left: 0; bottom: 0; height: auto;
    width: var(--ucnav-w); transform: translateX(-100%);
    transition: transform 0.18s ease;
  }
  body.ucnav-open .ucnav { transform: none; }
  .ucnav-body { grid-column: 1; margin-top: 3rem; }
  .ucnav-toggle {
    display: block; position: fixed; top: 0.5rem; left: 0.5rem; z-index: 30;
    font: inherit; font-size: 0.8rem; padding: 0.35rem 0.7rem;
    background: var(--ucnav-bg); color: var(--ucnav-fg);
    border: 1px solid var(--ucnav-rule); border-radius: 0.25rem;
  }
}
"""
css = pathlib.Path("main.css")
css.write_text(css.read_text(errors="ignore") + CSS)
PY

echo "==> checking"
rc=0
chk() { if [ "$2" = "$3" ]; then echo "    ok   $1: $2"; else echo "    FAIL $1: got $2, want $3"; rc=1; fi; }

# NB: tex4ht emits single-quoted attributes. A grep for src="..." matches
# nothing here and, in a for-loop, silently reports success. Match both.
svg_refs=$(grep -hoE "src=[\"'][^\"']*\.svg[\"']" main*.html | sort -u | wc -l | tr -d ' ')
svg_files=$(ls -1 ./*.svg 2>/dev/null | wc -l | tr -d ' ')
chk "diagrams referenced vs produced" "$svg_refs" "$svg_files"
chk "unresolved cross-references" "$(grep -h -c '\[?\]' main*.html | paste -sd+ - | bc)" "0"
chk "formulas left as images" "$(grep -ho "<img[^>]*alt='\[[^P]" main*.html | wc -l | tr -d ' ')" "0"
chk "pages without a sidebar" "$(grep -L "class='ucnav'" main*.html | wc -l | tr -d ' ')" "0"
# Step 5 regression guard. Test the sidebar text, which step 6 resolves to
# literal Δ and π: if the declarations go missing, detex has nothing to map
# and both drop to zero pages. Testing the body instead does not work, since
# the headings there legitimately read "</span>-Delayed Network" with the
# character sitting in a MathJax span.
pages=$(ls -1 main*.html | wc -l | tr -d ' ')
chk "pages whose sidebar kept its Delta" "$(grep -l 'Δ-Delayed' main*.html | wc -l | tr -d ' ')" "$pages"
chk "pages whose sidebar kept its pi" "$(grep -l 'π_Sig' main*.html | wc -l | tr -d ' ')" "$pages"
# The survey's own page links into these files by name, and tex4ht names them
# by position (mainch7.html), so adding a chapter to the book renumbers them
# and rots that page with no other symptom. Check the links against the build.
idx="$ROOT/surveys/uc-for-gamers/index.qmd"
bad_links=0
for target in $(grep -oE '\(html/main[^)]+\)' "$idx" | tr -d '()' | sed 's|^html/||'); do
  file="${target%%#*}"
  frag="${target#*#}"
  if [ ! -f "$file" ]; then bad_links=$((bad_links + 1)); continue; fi
  if [ "$frag" != "$target" ] && ! grep -q "id='$frag'" "$file"; then
    bad_links=$((bad_links + 1))
  fi
done
chk "index.qmd links that do not resolve" "$bad_links" "0"

tex_h=$(grep -cE '^\\(chapter|section)\{' main.tex)
html_h=$(grep -hoE '<h[23][^>]*>' main*.html | wc -l | tr -d ' ')
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
