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
#   7. The site's look is restated here as plain CSS, not imported. This
#      page is standalone tex4ht output rendered outside Quarto, so it sees
#      neither theme-light.scss nor theme-dark.scss. The palette, the serif
#      and display faces and the link colours below are copies of those two
#      files, and nothing detects drift between them: change a colour there
#      and it has to be changed here too. The book's own tcolorbox fills are
#      left alone in both themes: each rule sets a text colour beside its
#      background, so recolouring the fill for dark mode without the text
#      would destroy the contrast the pair was chosen for.
#
#      Light is the base and dark is the override, reachable two ways: the
#      reader's system preference, and a button in the sidebar that overrides
#      it and persists. The media query is guarded with :not([data-theme=
#      "light"]) so a reader who picks light on a dark-mode machine keeps it.
#      The stored choice is read by a script in <head>, not with the rest of
#      the JavaScript at the end of <body>: read after first paint, the wrong
#      theme is on screen for a frame before being swapped. Every page carries
#      that script and the build fails if any does not, because one page
#      missing it flashes and no spot check would show which.
#
#  10. MathJax is loaded from this site, not from tex4ht's hardcoded CDN.
#      assets/mathjax/ holds mathjax@3.2.2 tex-chtml-full and its CHTML
#      fonts, and _quarto.yml points every other page at the same copy.
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

# Step 8: give every pseudocode line label an anchor. tex4ht emits nothing
# for a \label inside algpseudocode, so all 298 line references resolve to
# the enclosing heading or to an anchor that was never written. A
# \hypertarget beside each \label is what tex4ht does turn into an id.
# The line labels are not all in main.tex: 25 of them live in the
# functionalities/ includes, and anchoring only main.tex leaves exactly
# those references pointing at a heading.
ANCHOR = (r"\\label\{(ln:[^}]*)\}",
          lambda m: "\\label{%s}\\hypertarget{%s}{}" % (m.group(1), m.group(1)))
# main.tex is edited in memory: re-reading it here would discard the Unicode
# declarations added above, and the only symptom of that is a table of
# contents quietly losing its Delta and pi again.
s, total = re.subn(ANCHOR[0], ANCHOR[1], s)
for f in sorted(pathlib.Path("functionalities").glob("*.tex")):
    t, k = re.subn(ANCHOR[0], ANCHOR[1], f.read_text())
    if k:
        f.write_text(t)
    total += k
assert total > 0, "no ln: labels found -- step 8 needs updating"
print(f"    anchored {total} pseudocode line labels")

# Step 9: \emph carries no semantics in tex4ht's output, only an italic font
# class shared with every other italic on the page. \HCode exists only under
# tex4ht, so the PDF build is untouched by this and the guard keeps a plain
# latex run working.
emph = ("\\makeatletter\n"
        "\\AtBeginDocument{\\ifdefined\\HCode\n"
        "  \\let\\uc@emph\\emph\n"
        "  \\renewcommand{\\emph}[1]{\\HCode{<em>}\\uc@emph{#1}\\HCode{</em>}}\\fi}\n"
        "\\makeatother\n"
        "\\begin{document}")
s, n = re.subn(r"\\begin\{document\}", lambda _: emph, s, count=1)
assert n == 1, "begin{document} not found -- step 9 needs updating"

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
out.setdefault("relax", "")                # a TeX no-op; step 6 strips the
                                           # ones step 5 causes, this catches
                                           # any the book emits elsewhere
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
    # Step 10: load MathJax from this site, not from a CDN. tex4ht hardcodes
    # cdn.jsdelivr.net, which made every formula in the book depend on a
    # third party and ran a different major version from the rest of the
    # site. The vendored copy is the one _quarto.yml points at too. The path
    # is absolute because these pages sit four levels down and the site is
    # served from the domain root.
    h2 = re.sub(r"https://cdn\.jsdelivr\.net/npm/mathjax@[^'\"]*",
                lambda _: "/assets/mathjax/tex-chtml-full.js", h2)
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

# Runs in <head>, before the body is painted. Reading the stored choice after
# first paint would show the wrong theme for a frame and then swap it, which is
# the flash this avoids. Kept to one statement and wrapped, because localStorage
# throws rather than returning null when a browser blocks storage.
HEAD_JS = ("<script>try{var t=localStorage.getItem('uc-theme');"
           "if(t)document.documentElement.setAttribute('data-theme',t);}"
           "catch(e){}</script>")

THEME_BTN = (
    "<button class='ucnav-theme' type='button'>"
    "<svg class='uc-moon' viewBox='0 0 24 24' aria-hidden='true'>"
    "<path d='M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z'/></svg>"
    "<svg class='uc-sun' viewBox='0 0 24 24' aria-hidden='true'>"
    "<circle cx='12' cy='12' r='4'/>"
    "<path d='M12 2v2M12 20v2M2 12h2M20 12h2"
    "M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4'/>"
    "</svg></button>")

JS = """<script>
(function () {
  var nav = document.getElementById('ucnav'),
      btn = document.querySelector('.ucnav-toggle');
  if (nav && btn) {
    btn.addEventListener('click', function () {
      var open = document.body.classList.toggle('ucnav-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // Keep the current chapter in view without scrolling the page itself.
    var cur = nav.querySelector('.ucnav-current');
    if (cur) nav.scrollTop = cur.offsetTop - nav.clientHeight / 2;
  }

  var root = document.documentElement,
      tbtn = document.querySelector('.ucnav-theme');
  if (!tbtn) return;
  // What the reader is actually looking at. No attribute means no choice has
  // been made, so the system preference is what the CSS is following.
  // Dark unless a choice is stored. Not matchMedia: the CSS ignores the
  // system preference, so consulting it here would label the button wrong for
  // anyone on a light-mode machine who has not chosen anything yet.
  function inForce() {
    return root.getAttribute('data-theme') || 'dark';
  }
  function paint() {
    var t = inForce();
    tbtn.setAttribute('data-theme-state', t);
    tbtn.setAttribute('aria-label',
      t === 'dark' ? 'Switch to the light theme' : 'Switch to the dark theme');
    tbtn.setAttribute('title', tbtn.getAttribute('aria-label'));
  }
  tbtn.style.display = 'block';
  paint();
  tbtn.addEventListener('click', function () {
    var next = inForce() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('uc-theme', next); } catch (e) {}
    paint();
  });
})();
</script>"""

pages = sorted(pathlib.Path(".").glob("main*.html"))
heads = 0
rots = 0
urlfix = 0
for f in pages:
    items = "\n".join(
        li(k, n, h, t, h.split("#")[0] == f.name) for k, n, h, t in entries)
    # "../" is the survey's own page on the site, which is where the site
    # navigation lives; this edition is otherwise a dead end with no way back.
    nav = (f"<nav class='ucnav' id='ucnav' aria-label='Contents'>"
           f"<div class='ucnav-head'>"
           f"<a class='ucnav-up' href='../'>&#8592; Conjura</a>"
           f"<a class='ucnav-book' href='main.html'>UC for Gamers</a>"
           f"{THEME_BTN}"
           f"</div><ul>{items}</ul></nav>")
    h = f.read_text(errors="ignore")
    # Step 5's \ensuremath reaches the page as "\(\relax \Delta \)". \relax is
    # a TeX no-op with nothing to typeset, and MathJax has no definition for
    # it, so it renders as literal red text next to the four affected
    # headings. Drop it: removing a no-op cannot change what the math means.
    h = h.replace(r"\(\relax ", r"\(")
    # Insert after <body...>, and close the wrapper before </body>. tex4ht
    # writes "<body>" plainly, but match attributes in case that changes.
    # lambda again: chapter titles carry backslashes, and as a string
    # replacement the first "\D" of a \Delta raises re.PatternError.
    ins = TOGGLE + nav + "<div class='ucnav-body'>"
    h2, n = re.subn(r"(<body[^>]*>)", lambda m: m.group(1) + ins, h, count=1)
    if n == 0:
        continue
    h2 = h2.replace("</body>", "</div>" + JS + "</body>", 1)
    h2, hn = re.subn(r"</head>", HEAD_JS + "</head>", h2, count=1)
    heads += hn
    # Step 11: the book's one sideways figure, in 4.3 Parallel Composition.
    # main.tex rotates it 90 degrees because it is too wide for a portrait
    # page. tex4ht carries that over as a CSS transform, and a transform does
    # not affect layout: the box still reserves the unrotated 847x290 while the
    # image draws 290 wide and 847 tall, so roughly 550pt of diagram lands on
    # the paragraph underneath. The web has no page to fit it to, so the
    # rotation goes and the figure scrolls sideways instead, which is what this
    # stylesheet already does with wide tables and equations.
    h2, rn = re.subn(r"<span class='rotatebox'[^>]*>(\s*<img[^>]*>\s*)</span>",
                     lambda m: f"<span class='ucfig-wide'>{m.group(1)}</span>",
                     h2, flags=re.S)
    rots += rn
    # Step 12: LaTeX's own escape, left in the URL. The bibliography writes
    # \url{...Selected\%20Scientific...}, which is correct LaTeX, and the PDF
    # gets a clean %20: verified by reading the URI annotations out of
    # surveys/uc-for-gamers/pdf/main.pdf, which carry no backslash. tex4ht
    # copies the escape through into the href instead, and the published link
    # 404s while the same link in the PDF works. Fixed here rather than in the
    # source, because the source is not what is wrong.
    def _unescape(m):
        global urlfix
        u = m.group(1)
        if "\\%" in u:
            urlfix += 1
            u = u.replace("\\%", "%")
        return "href='" + u + "'"
    h2 = re.sub(r"href='([^']*)'", _unescape, h2)
    f.write_text(h2)
print(f"    sidebar on {len(pages)} pages, {len(entries)} entries")
# A page that missed the head script shows the wrong theme for a frame before
# correcting itself, which is exactly the bug the script exists to prevent and
# is invisible in a spot check. Fail rather than ship a subset.
assert heads == len(pages), f"head script reached {heads} of {len(pages)} pages"
# One sideways figure exists in the book. If the source gains another and
# this silently keeps rewriting one, the new one overlaps its text with no
# sign here; if a future tex4ht stops emitting rotatebox, this hits 0 and
# the fix has quietly become a no-op.
assert rots == 1, f"expected 1 rotated figure, rewrote {rots}"
print(f"    unescaped {urlfix} URL(s) carrying a LaTeX percent escape")
print(f"    theme toggle and pre-paint script on {heads} pages")

CSS = """

/* ---- generated by scripts/build_uc_html.sh, steps 6 and 7 ------------- */
/* This page is standalone tex4ht output and inherits nothing from the
   site's Quarto theme, so the theme's tokens are restated here as plain
   CSS. Keep these in sync with theme-light.scss and theme-dark.scss: they
   are copies, not imports, and nothing detects drift between them. */
/* Dark is the default, and unconditionally so: this edition opens black
   whatever the reader's machine prefers. Light is reachable only by choosing
   it with the button in the sidebar, which stores the choice. There is
   deliberately no prefers-color-scheme rule here. One would mean the default
   is whatever the visitor's system says, which is the opposite of having a
   default. The two palettes are written once each in this script and emitted
   into one selector apiece, so they cannot drift apart. */
:root {
  --cj-serif: "Hoefler Text", Baskerville, "Big Caslon", "Palatino Linotype",
              Palatino, "Book Antiqua", Georgia, "Times New Roman", serif;
  --cj-display: "Big Caslon", "Baskerville Old Face", "Hoefler Text",
                Baskerville, "Palatino Linotype", Palatino, Georgia, serif;
  --cj-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas,
             "Liberation Mono", monospace;
  --ucnav-w: 19rem;
@@DARK@@}
:root[data-theme="light"] {@@LIGHT@@}

/* Step 7: the book itself, in the site's typography and palette. tex4ht
   ships its own colours and a browser-default serif; without this the page
   reads as a different site that happens to be linked from this one. */
body { background: var(--cj-bg); color: var(--cj-fg); font-family: var(--cj-serif); }
::selection { background: var(--cj-select); color: var(--cj-fg); }
.ucnav-body a { color: var(--cj-link); }
.ucnav-body a:hover { color: var(--cj-link-hover); }
h1, h2, h3, h4, h5, h6,
.partHead, .chapterHead, .likechapterHead,
.sectionHead, .likesectionHead,
.subsectionHead, .likesubsectionHead { font-family: var(--cj-display); }
/* A heading is a link back to the contents. Underlined accent-blue heads
   are tex4ht's default and read as broken; keep the heading's own colour. */
.chapterHead a, .likechapterHead a, .sectionHead a, .likesectionHead a,
.subsectionHead a, .likesubsectionHead a { color: inherit; text-decoration: none; }
.titlemark { color: var(--cj-muted); font-size: 0.62em; display: block;
             letter-spacing: 0.04em; text-transform: uppercase; }
tt, code, .obeylines-h, .verbatim { font-family: var(--cj-mono); font-size: 0.9em; }
code { color: var(--cj-link); background: var(--cj-code-bg); }
/* tex4ht's [next] [prev] [up] strip, quieted to furniture. */
.crosslinks { font-size: 0.8rem; color: var(--cj-muted); margin: 0.5em 0 1.5em; }
.crosslinks a { color: var(--cj-muted) !important; text-decoration: none; }
.crosslinks a:hover { color: var(--cj-link) !important; }
/* Same two fixes the site theme carries, for the same reasons: a wide
   equation or table must scroll on its own rather than widen the page. */
mjx-container[jax="CHTML"][display="true"] { overflow-x: auto; overflow-y: hidden; max-width: 100%; }
.ucnav-body table { border-collapse: collapse; display: block; overflow-x: auto; }
.ucnav-body td, .ucnav-body th { border-color: var(--cj-rule); }
hr { border: 0; border-top: 1px solid var(--cj-rule); }
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
  background: var(--cj-bg); color: var(--cj-fg);
  border-right: 1px solid var(--cj-rule);
  font-family: var(--cj-serif); font-size: 0.82rem; line-height: 1.4;
  padding: 0 0 3rem;
  -webkit-overflow-scrolling: touch; z-index: 20;
}
/* Sticky, or the scroll-to-current below carries the title and the way
   back to the site off the top of the list. */
.ucnav-head {
  position: sticky; top: 0; z-index: 1; font-weight: 700;
  background: var(--cj-bg); border-bottom: 1px solid var(--cj-rule);
  /* Room on the right for the theme button, which is positioned against this
     box (sticky is a positioned element, so it is already the containing
     block) and would otherwise sit on top of a longer book title. */
  padding: 0.9rem 3rem 0.6rem 1rem;
}
.ucnav-head a, .ucnav a { color: inherit; text-decoration: none; }
.ucnav-up { display: block; font-weight: 400; font-size: 0.82em;
            color: var(--cj-muted) !important; margin-bottom: 0.3rem; }
.ucnav-up:hover { color: var(--cj-link) !important; }
.ucnav-book { font-family: var(--cj-display); font-size: 1.05em; }
/* Hidden until the script below reveals it. A theme button that cannot switch
   the theme is worse than no button, and without JavaScript this one cannot. */
.ucnav-theme {
  display: none; position: absolute; top: 0.8rem; right: 0.85rem;
  background: none; border: 1px solid var(--cj-rule); border-radius: 0.25rem;
  color: var(--cj-muted); cursor: pointer; padding: 0.3rem; line-height: 0;
}
.ucnav-theme:hover { color: var(--cj-link); border-color: var(--cj-link); }
.ucnav-theme svg { width: 0.95rem; height: 0.95rem; display: block;
                   fill: none; stroke: currentColor; stroke-width: 1.6;
                   stroke-linecap: round; stroke-linejoin: round; }
/* Show the theme being offered, not the one in force: in light, a moon. */
.ucnav-theme .uc-sun { display: none; }
.ucnav-theme[data-theme-state="dark"] .uc-sun { display: block; }
.ucnav-theme[data-theme-state="dark"] .uc-moon { display: none; }
.ucnav ul { list-style: none; margin: 0; padding: 0; }
.ucnav li a {
  display: block; padding: 0.28rem 1rem 0.28rem 1.6rem;
  border-left: 3px solid transparent;
}
.ucnav li a:hover { background: rgba(127,127,127,0.12); }
.ucnav-num { color: var(--cj-muted); }
.ucnav-chapter > a, .ucnav-likechapter > a { font-weight: 600; }
.ucnav-section > a { padding-left: 2.9rem; color: var(--cj-muted); }
.ucnav-current > a {
  border-left-color: var(--cj-link); color: var(--cj-link);
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
/* Step 11: the unrotated sideways figure. It is wider than the column, so
   it scrolls in place at full size rather than being shrunk to fit, which
   at 62% would leave the labels inside it unreadable. */
.ucfig-wide { display: block; overflow-x: auto; max-width: 100%; }
.ucfig-wide img { max-width: none; }

/* The diagrams are drawn as black ink on white, so on the dark default they
   have to be inverted, and tex4ht's own rule cannot do it: it ships
   "@media (prefers-color-scheme: dark) { img[src^=main] { filter: invert(1) } }",
   which follows the machine rather than this page's default and would leave a
   light-mode visitor reading black figures on a black page. Inverted here
   unconditionally instead, and undone only when light is chosen. The hue
   rotation is not decoration: a plain invert turns the book's accent orange
   (#a8630f) into blue, and rotating the hue back puts it where it was drawn. */
img[src^="main"] { filter: invert(1) hue-rotate(180deg); }
:root[data-theme="light"] img[src^="main"] { filter: none; }

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
    background: var(--cj-bg); color: var(--cj-fg);
    border: 1px solid var(--cj-rule); border-radius: 0.25rem;
  }
}
"""
DARK = """
  color-scheme: dark;
  --cj-bg: #1f1e1d;
  --cj-fg: #f0e8c0;
  --cj-link: #e89b7f;
  --cj-link-hover: #f2b79f;
  --cj-rule: #383634;
  --cj-code-bg: #262524;
  --cj-muted: #9a9384;
  --cj-select: #3a3430;
"""
LIGHT = """
  color-scheme: light;
  --cj-bg: #faf9f5;
  --cj-fg: #1f1e1d;
  --cj-link: #a34f2a;
  --cj-link-hover: #8a4223;
  --cj-rule: #e5e3dc;
  --cj-code-bg: #f0eee6;
  --cj-muted: #6d6a63;
  --cj-select: #f7ede8;
"""
assert CSS.count("@@DARK@@") == 1, "the dark tokens go in :root, once"
assert CSS.count("@@LIGHT@@") == 1, "the light tokens go in the opt-in, once"
CSS = CSS.replace("@@DARK@@", DARK).replace("@@LIGHT@@", LIGHT)

css = pathlib.Path("main.css")
css.write_text(css.read_text(errors="ignore") + CSS)
PY

# Step 8b: repoint the line references at the anchors step 8 created, and
# drop the bogus fragment tex4ht puts on its own "up" links.
python3 - <<'STEP8' || { echo "FAIL: step 8 (line references)"; exit 1; }
import pathlib, re

pages = sorted(pathlib.Path(".").glob("main*.html"))
text = {q.name: q.read_text(errors="ignore") for q in pages}

# Where did each \hypertarget{ln:...} end up?
where = {}
for name, h in text.items():
    # tex4ht sanitises the colon out of a \hypertarget key, so
    # \hypertarget{ln:session} lands as id='ln_session'.
    for lab in re.findall(r"id='(ln_[^']+)'", h):
        where.setdefault(lab, name)

# tex4ht records the label it could not resolve in a comment inside the link
# text: <a href='...'>3<!-- tex4ht:ref: ln:session --></a>. That comment is
# the only thing tying the reference back to the line it meant.
# Match a whole <a>...</a> and look for the comment inside it. A single
# regex reaching from href to comment spans intervening links instead --
# .*? crosses </a> under re.S -- so the comment gets attributed to an
# earlier anchor and 183 of the 481 rendered references are skipped while
# the count still reports success.
ANCH = re.compile(r"<a href='([^']*)'([^>]*)>(.*?)</a>", re.S)
MARK = re.compile(r"<!--\s*tex4ht:ref:\s*(ln:[A-Za-z0-9_@.\-]+)\s*-->")
# Section pages point "up" at their chapter page, not only at main.html.
UP = re.compile(r"href='(main[a-z0-9]*\.html)#main[a-z0-9]*\.html'")

stats = {"fixed": 0, "missing": 0, "ups": 0}

def repoint(m):
    mark = MARK.search(m.group(3))
    if not mark:
        return m.group(0)
    key = mark.group(1).replace(":", "_")
    page = where.get(key)
    if not page:
        stats["missing"] += 1
        return m.group(0)
    stats["fixed"] += 1
    return "<a href='%s#%s'%s>%s</a>" % (page, key, m.group(2), m.group(3))

for name, h in text.items():
    h2 = ANCH.sub(repoint, h)
    h2, n = UP.subn(lambda m: "href='" + m.group(1) + "'", h2)
    stats["ups"] += n
    if h2 != h:
        pathlib.Path(name).write_text(h2)

print("    repointed {fixed} line references ({missing} unresolved), "
      "{ups} up-links".format(**stats))
assert stats["missing"] == 0, "%d line references have no anchor" % stats["missing"]
STEP8

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
chk "pages without the theme button" "$(grep -L "class='ucnav-theme'" main*.html | wc -l | tr -d ' ')" "0"
chk "rotated figures left overlapping their text" "$(grep -ho "class='rotatebox'" main*.html | wc -l | tr -d ' ')" "0"
chk "the sideways figure, unrotated and scrollable" "$(grep -ho "class='ucfig-wide'" main*.html | wc -l | tr -d ' ')" "1"
chk "LaTeX escapes left inside a URL" "$(grep -oh "href='[^']*\\\\%" main*.html | wc -l | tr -d ' ')" "0"
# The theme the reader picked has to win over the theme their machine prefers,
# for the diagrams as well as the page. Without the guarded pair below, light
# chosen on a dark-mode machine renders inverted figures on a light page.
chk "diagram inversion following the choice" "$(grep -c ':root\[data-theme="light"\] img' main.css)" "1"
chk "pages without the pre-paint theme script" "$(grep -L "uc-theme" main*.html | wc -l | tr -d ' ')" "0"
# Light must be the base, so that a browser with no support for the query, and
# a reader who has chosen light, both get it. If the light tokens ever move
# inside a media query this is 0 and the page has no light theme at all.
chk "dark is the default palette" "$(awk '/^:root \{/{f=1} f&&/--cj-bg: #1f1e1d/{print;exit}' main.css | wc -l | tr -d ' ')" "1"
chk "light is reachable by choice" "$(grep -c '^:root\[data-theme="light"\] {' main.css)" "1"
# A prefers-color-scheme rule of ours would defeat the point of a default. The
# one tex4ht ships is still in the file and is overridden, so match only the
# selectors this script writes.
chk "our own system-preference rules" "$(grep -c ':root:not(\[data-theme' main.css)" "0"
chk "each palette written exactly once" "$(grep -c -- '--cj-bg: #1f1e1d' main.css)$(grep -c -- '--cj-bg: #faf9f5' main.css)" "11"
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
chk "MathJax fetched from a CDN" "$(grep -oh 'cdn\.jsdelivr\.net\|cdnjs\.cloudflare\.com\|unpkg\.com' main*.html | wc -l | tr -d ' ')" "0"
chk "TeX no-ops left in the math" "$(grep -oh '\\relax' main*.html | wc -l | tr -d ' ')" "0"

# Defect 2: the old cross-reference check greped for "[?]", which is what
# LaTeX emits for an *unresolved* \ref. Every line reference resolved; they
# resolved to the wrong place, so that check reported success on 298 broken
# links. This one parses every href and tests the fragment against the ids
# actually present. NB tex4ht writes single-quoted attributes, so a check
# written against href=" matches nothing and silently passes.
dead=$(python3 - <<'AUDIT'
import pathlib, re
text = {q.name: q.read_text(errors="ignore") for q in pathlib.Path(".").glob("main*.html")}
ids = {n: set(re.findall(r"\bid='([^']+)'", h)) for n, h in text.items()}
dead = 0
for name, h in text.items():
    for href in re.findall(r"\bhref='([^']+)'", h):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        tgt, _, frag = href.partition("#")
        tgt = tgt or name
        if not tgt.endswith(".html"):
            continue
        if tgt not in text or (frag and frag not in ids[tgt]):
            dead += 1
print(dead)
AUDIT
)
chk "dead internal links" "$dead" "0"
chk "emphasis carried as <em>" "$([ "$(grep -ho '<em[ >]' main*.html | wc -l | tr -d ' ')" -gt 300 ] && echo yes || echo no)" "yes"
# Count the references still NOT landing on a line rather than the ones that
# do: the book renders 481 line references from 298 \ref commands, because
# the functionality boxes are typeset in more than one place, so any fixed
# expected total is wrong the moment that changes.
stray=$(grep -oh "<a href='[^']*'[^>]*>[^<]*<!-- tex4ht:ref: ln:" main*.html | grep -vc "#ln_")
chk "line references not landing on a line" "$stray" "0"
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
