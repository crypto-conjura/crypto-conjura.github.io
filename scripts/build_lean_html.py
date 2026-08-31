#!/usr/bin/env python3
"""Render one Lean package's sources as a single syntax-highlighted HTML page.

    python3 scripts/build_lean_html.py c/0004/lean
    python3 scripts/build_lean_html.py c/0004/lean --out c/0004/lean/html

Writes `<package>/html/index.html`: every `.lean` file of the package on one
page, in the site's palette and typography, with line anchors, a declaration
index, and every `sorry` marked. The output is committed, like the HTML
edition of *UC for Gamers* under `surveys/uc-for-gamers/html/`, so a reader
gets it without this script having to run in CI.

Why Pygments, and not a Lean documentation generator. All three alternatives
were checked on 31 August 2026 before this file was written:

  * **doc-gen4** is the canonical generator and is version-current (its `main`
    pins `leanprover/lean4:v4.34.0-rc2`, so a ref compatible with this repo's
    `v4.33.0` exists). It is still the wrong tool here: `lake build <lib>:docs`
    needs the `docs` facet of every transitive import, and a breadth-first
    walk of the module graph from the five Mathlib modules `c/0004` imports
    reaches 8,566 modules, roughly 8,300 of them Mathlib. That is the full
    Mathlib documentation build -- hours of compute, several GB of HTML -- to
    document 767 lines. `.github/workflows/lean_action_ci.yml` separately
    records why `leanprover-community/docgen-action@v1` is not wired into CI.
  * **LeanInk + Alectryon** is the combination that would give hover-over goal
    states, the thing that would make a proof file genuinely readable in a
    browser. It is dead for this toolchain: LeanInk's last commit is 18 July
    2024 and its `lean-toolchain` reads `v4.6.0-rc1`, twenty-seven minor
    versions behind `v4.33.0`.
  * **Quarto's own highlighter cannot do it**, which is why this is a
    generated page rather than a ```lean fence in a `.qmd`:
    `quarto pandoc --list-highlight-languages` lists 163 languages and none of
    them is Lean.

Pygments 2.21's `Lean4Lexer` tokenizes these files with zero `Error` tokens,
and -- the reason it is enough for this job -- it reports `sorry` as
`Generic.Error` and `/-- ... -/` as `String.Doc`, so the two things a reader
of a Conjura statement actually needs to see are distinguishable in the
markup rather than guessed at by eye.

Pygments is not a dependency of the site build. Install it where it is needed:

    python3 -m venv /tmp/cvenv && /tmp/cvenv/bin/pip install pygments
    /tmp/cvenv/bin/python scripts/build_lean_html.py c/0004/lean

The palette, the serif and display faces and the link colours below are
copies of `theme-light.scss` and `theme-dark.scss`, the same arrangement (and
the same caveat) as `scripts/build_uc_html.sh`: nothing detects drift between
them, so a colour changed there has to be changed here too. Light is the base
because the site's own default is light; dark is reached by the reader's
system preference or by the button in the header, and the choice is stored
under Quarto's own `quarto-color-scheme` key so that a reader who has put the
site in dark mode arrives here in dark mode too.

The self-checks at the end of the run are not decoration. The one that matters
is `CLASS_STYLE` coverage: if a future Lean file (or a future Pygments) emits
a token class this file has no colour for, the run fails rather than shipping
a page with invisible-by-default syntax.
"""

from __future__ import annotations

import argparse
import html
import os
import pathlib
import re
import sys

try:
    from pygments.lexers import Lean4Lexer
    from pygments.token import STANDARD_TYPES
except ModuleNotFoundError:  # pragma: no cover - the message is the point
    sys.exit(
        "Pygments is not installed. It is not a dependency of the site build;\n"
        "  python3 -m venv /tmp/cvenv && /tmp/cvenv/bin/pip install pygments\n"
        "then run this script with /tmp/cvenv/bin/python."
    )

REPO = pathlib.Path(__file__).resolve().parent.parent
GITHUB = "https://github.com/crypto-conjura/crypto-conjura.github.io/blob/main"

# Reading order, not alphabetical order: what is claimed, then how it is
# proved, then what was audited. Any file not named here follows, sorted.
# `lakefile.lean` is build configuration rather than mathematics; a package
# using the Lean form rather than the TOML form should not have it rendered
# as if it were part of the development.
ORDER = ["Statement", "Proof", "Audit", "AuditProof"]
SKIP = {"lakefile.lean"}

# One declaration per line, which is how Lean is written and how every file in
# this repository is written. Attributes (`@[simp]`) may precede the modifier
# stack; the identifier is whatever follows the keyword up to the first space,
# colon, bracket or binder brace.
DECL = re.compile(
    r"^(?:@\[[^\]]*\]\s*)?"
    r"(?:(?:private|protected|noncomputable|partial|unsafe|scoped|local)\s+)*"
    r"(theorem|lemma|def|abbrev|structure|inductive|instance|class|opaque"
    r"|axiom|example)\b[ \t]*"
    r"([^\s:({\[⦃⟨]*)"
)
NAMESPACE = re.compile(r"^(namespace|section|end)\b[ \t]*([^\s]*)")

# Pygments' short class names, each given a colour in both themes. Keys are
# the classes this repository's Lean actually produces plus the near neighbours
# a future file would reach for; `check_classes` fails the build if a file
# produces one that is missing, so this list cannot silently fall behind.
#
# The scheme is deliberately narrow -- four hues and a muted grey -- because
# the accent colour (`--cj-link`) is spoken for by links everywhere else on the
# site and must not also mean "keyword" here.
CLASS_STYLE: dict[str, str] = {
    "k": "kw",       # Keyword: by, fun, do, if
    "kd": "kw",      # Keyword.Declaration
    "kn": "kw",      # Keyword.Namespace: theorem, def, namespace, variable
    "kr": "kw",      # Keyword.Reserved
    "kt": "ty",      # Keyword.Type: Prop, Type
    "kc": "kw",      # Keyword.Constant
    "kp": "kw",      # Keyword.Pseudo
    "n": "id",       # Name: everything the lexer does not classify further
    "nb": "ty",      # Name.Builtin
    "bp": "op",      # Name.Builtin.Pseudo: =, →, ∀ and friends
    "nc": "ty",      # Name.Class
    "nf": "id",      # Name.Function
    "nn": "ty",      # Name.Namespace
    "nv": "id",      # Name.Variable
    "no": "ty",      # Name.Constant
    "o": "op",       # Operator
    "ow": "kw",      # Operator.Word
    "p": "op",       # Punctuation
    "c": "cmt",      # Comment: the `/-` and `-/` delimiters
    "c1": "cmt",     # Comment.Single: -- ...
    "cm": "prose",   # Comment.Multiline: /- ... -/ and /-! ... -/
    "cp": "cmt",     # Comment.Preproc
    "cs": "cmt",     # Comment.Special
    "sd": "prose",   # Literal.String.Doc: /-- ... -/
    "s": "str",      # Literal.String
    "s1": "str",
    "s2": "str",
    "sa": "str",
    "sc": "str",     # Literal.String.Char
    "se": "str",     # Literal.String.Escape
    "si": "str",     # Literal.String.Interpol
    "sx": "str",     # Literal.String.Other
    "m": "num",      # Literal.Number
    "mi": "num",
    "mf": "num",
    "mh": "num",
    "mo": "num",
    "mb": "num",
    "gr": "sorry",   # Generic.Error: this is how the lexer reports `sorry`
    "ge": "sorry",   # Generic.Emph -- unreachable in Lean, styled anyway
    "gs": "kw",      # Generic.Strong
    "err": "bad",    # Error: the lexer gave up on this text
    "w": "id",       # Text.Whitespace
    "cd": "cmt",     # Comment.Doc (Pygments spells doc comments both ways)
}

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
  --cj-target: #f8ecd4;
  --lean-kw: #8b3a62;
  --lean-ty: #2f6b7a;
  --lean-id: #1f1e1d;
  --lean-op: #6d6a63;
  --lean-str: #3f6b3a;
  --lean-num: #3f6b3a;
  --lean-cmt: #6d6a63;
  --lean-prose: #4a4640;
  --lean-sorry: #9c2b21;
  --lean-sorry-bg: #f7e2de;
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
  --cj-target: #332a1a;
  --lean-kw: #e5a0c0;
  --lean-ty: #8fc6d4;
  --lean-id: #f0e8c0;
  --lean-op: #9a9384;
  --lean-str: #a8cf9a;
  --lean-num: #a8cf9a;
  --lean-cmt: #9a9384;
  --lean-prose: #cfc8ad;
  --lean-sorry: #ff9d92;
  --lean-sorry-bg: #40201d;
"""


def rel_to_repo(path: pathlib.Path) -> str:
    """`path` as a repository-relative POSIX path, or absolute if it is outside.

    `--out` may point anywhere, and a ValueError from `relative_to` is not the
    error anyone running this wanted to see.
    """
    try:
        return path.relative_to(REPO).as_posix()
    except ValueError:
        return path.as_posix()


def cls_of(ttype) -> str:
    """The class name `HtmlFormatter` would emit for a token type.

    Reimplemented rather than imported because the formatter exposes it only
    as a private helper, and because the fallback to the nearest styled
    ancestor is exactly what makes `CLASS_STYLE` finite: `Name.Foo.Bar` with
    no entry of its own is rendered as `Name`.
    """
    t = ttype
    while t is not None:
        name = STANDARD_TYPES.get(t)
        if name:
            return name
        t = t.parent
    return ""


def frontmatter(path: pathlib.Path) -> dict[str, str]:
    """The scalar keys of a `.qmd` YAML header, read without PyYAML.

    PyYAML is not installed in the environment this repository is maintained
    from (the pre-commit hook says so out loud), and the three values wanted
    here -- `id`, `title`, `short_title` -- are flat quoted scalars in every
    statement page. Nested keys are ignored on purpose.
    """
    out: dict[str, str] = {}
    if not path.exists():
        return out
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return out
    for line in lines[1:]:
        if line.strip() == "---":
            break
        # Top-level keys only: an indented line belongs to a nested block
        # (`status:`, `lean:`, `sources:`) and is not wanted here. Splitting
        # the file on "---" instead of walking it would end the header early
        # on any value containing a triple dash.
        m = re.match(r'^([a-z_]+):[ \t]*"?(.*?)"?[ \t]*$', line)
        if m and m.group(2):
            out.setdefault(m.group(1), m.group(2))
    return out


def package_files(pkg: pathlib.Path) -> list[pathlib.Path]:
    """The package's own `.lean` files, in reading order.

    Recursive, because a package may put its modules in a subtree
    (`lean/Verify.lean` is one line and an import of `lean/Verify/Basic.lean`),
    but never into a dot-directory: `.lake/` is ~7 GB of fetched Mathlib and is
    gitignored for exactly that reason, so walking into it would be both wrong
    and slow.
    """
    found = []
    for dirpath, dirnames, filenames in os.walk(pkg):
        # Pruned in place rather than filtered afterwards: an rglob would walk
        # all ~8,300 files of the fetched Mathlib before discarding them.
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f.endswith(".lean") and f not in SKIP:
                found.append(pathlib.Path(dirpath) / f)
    return sorted(found, key=lambda q: (
        ORDER.index(q.stem) if q.stem in ORDER else len(ORDER),
        q.relative_to(pkg).as_posix()))


def render(path: pathlib.Path, slug: str) -> tuple[list[str], dict[str, int], list[tuple]]:
    """One file, as highlighted lines plus what the nav and header need.

    Returns the `<span class='lean-line'>` markup for each source line, a
    count dictionary, and the declaration list. The lexer is run over the
    whole file and the token stream re-split on newlines rather than
    highlighting line by line, because a `/- ... -/` comment or a docstring
    spans lines and a per-line lexer would lose the state that classifies it.
    """
    src = path.read_text(encoding="utf-8")
    lexer = Lean4Lexer()

    seen_classes: set[str] = set()
    sorries = 0
    # Build the markup one line at a time. `line` accumulates the spans of the
    # current source line; a token containing newlines is split so that the
    # class is reopened on the next line, which is what keeps a multi-line
    # comment styled on every one of its lines instead of only the first.
    lines: list[list[str]] = [[]]
    for ttype, value in lexer.get_tokens(src):
        cls = cls_of(ttype)
        if cls:
            seen_classes.add(cls)
        if cls == "gr" and value.strip() == "sorry":
            sorries += 1
        parts = value.split("\n")
        for i, part in enumerate(parts):
            if i:
                lines.append([])
            if not part:
                continue
            esc = html.escape(part)
            lines[-1].append(f'<span class="{cls}">{esc}</span>' if cls else esc)
    # `get_tokens` appends a trailing newline, so the last element is the empty
    # remainder after it; a file that does end in a newline would otherwise
    # gain a spurious blank final line with a line number of its own.
    if lines and not lines[-1]:
        lines.pop()

    unstyled = sorted(c for c in seen_classes if c not in CLASS_STYLE)
    if unstyled:
        sys.exit(
            f"{path}: token classes with no colour in CLASS_STYLE: "
            f"{', '.join(unstyled)}.\nAdd them there rather than letting the "
            "page ship with unstyled syntax."
        )

    decls: list[tuple[str, str, str, int]] = []
    for n, raw in enumerate(src.splitlines(), start=1):
        m = DECL.match(raw)
        if m:
            kind, name = m.group(1), m.group(2)
            decls.append(("decl", kind, name or f"({kind})", n))
            continue
        m = NAMESPACE.match(raw)
        if m and m.group(1) == "namespace" and m.group(2):
            decls.append(("namespace", "namespace", m.group(2), n))

    markup = [
        f'<span class="lean-line" id="{slug}-L{n}">'
        f'<a class="lean-ln" href="#{slug}-L{n}">{n}</a>'
        f'<span class="lean-src">{"".join(spans) or " "}</span></span>'
        for n, spans in enumerate(lines, start=1)
    ]
    counts = {
        "lines": len(lines),
        "decls": sum(1 for k, *_ in decls if k == "decl"),
        "sorries": sorries,
    }
    return markup, counts, decls


def plural(n: int, one: str, many: str | None = None) -> str:
    return f"{n} {one if n == 1 else (many or one + 's')}"


HEAD_JS = (
    # Runs before the body is painted, so a reader in dark mode never sees a
    # frame of light. Quarto stores its own toggle's state under
    # `quarto-color-scheme` as 'alternate' (the dark of the two themes, since
    # `_quarto.yml` lists light first) or 'default'; reading the same key is
    # what carries a choice made on the statement page into this one. Wrapped
    # because localStorage throws, rather than returning null, where a browser
    # blocks storage outright.
    "<script>try{var t=localStorage.getItem('quarto-color-scheme');"
    "if(t)document.documentElement.setAttribute('data-theme',"
    "t==='alternate'?'dark':'light');}catch(e){}</script>"
)

THEME_BTN = (
    "<button class='lean-theme' type='button'>"
    "<svg class='lean-moon' viewBox='0 0 24 24' aria-hidden='true'>"
    "<path d='M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z'/></svg>"
    "<svg class='lean-sun' viewBox='0 0 24 24' aria-hidden='true'>"
    "<circle cx='12' cy='12' r='4'/>"
    "<path d='M12 2v2M12 20v2M2 12h2M20 12h2"
    "M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4'/>"
    "</svg></button>"
)

JS = """<script>
(function () {
  var nav = document.getElementById('leannav'),
      btn = document.querySelector('.lean-nav-toggle');
  if (nav && btn) {
    btn.addEventListener('click', function () {
      var open = document.body.classList.toggle('lean-nav-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    // On a phone the nav is a drawer over the listing; leaving it open after
    // a jump hides the line the reader just asked for.
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        document.body.classList.remove('lean-nav-open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  var root = document.documentElement,
      tbtn = document.querySelector('.lean-theme');
  if (!tbtn) return;
  // What the reader is looking at. No attribute means no choice is stored, so
  // the CSS is following the system preference -- and unlike the UC edition,
  // this page does follow it, so matchMedia is the right question to ask.
  function inForce() {
    var set = root.getAttribute('data-theme');
    if (set) return set;
    return window.matchMedia &&
      window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark' : 'light';
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
    // Written back under Quarto's key so the choice survives the trip back to
    // the statement page, in the value Quarto itself expects there.
    try {
      localStorage.setItem('quarto-color-scheme',
                           next === 'dark' ? 'alternate' : 'default');
    } catch (e) {}
    paint();
  });
})();
</script>"""


def stylesheet() -> str:
    """The whole page's CSS, both palettes written exactly once each."""
    syntax = "\n".join(
        f".lean-src .{cls} {{ color: var(--lean-{role}); }}"
        for cls, role in sorted(CLASS_STYLE.items())
        if role not in ("prose", "sorry", "bad")
    )
    return f""":root {{
  --cj-serif: "Hoefler Text", Baskerville, "Big Caslon", "Palatino Linotype",
              Palatino, "Book Antiqua", Georgia, "Times New Roman", serif;
  --cj-display: "Big Caslon", "Baskerville Old Face", "Hoefler Text",
                Baskerville, "Palatino Linotype", Palatino, Georgia, serif;
  --cj-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas,
             "Liberation Mono", monospace;
  --leannav-w: 20rem;
{LIGHT}}}
/* Dark twice over, and it has to be: the media query is what serves a reader
   who has chosen nothing, the attribute selector is what lets the button beat
   the system preference in both directions. The :not() guard is what stops the
   query from overriding an explicit choice of light. */
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{{DARK}  }}
}}
:root[data-theme="dark"] {{{DARK}}}

* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--cj-bg); color: var(--cj-fg);
  font-family: var(--cj-serif); line-height: 1.6;
}}
::selection {{ background: var(--cj-select); color: var(--cj-fg); }}
a {{ color: var(--cj-link); }}
a:hover {{ color: var(--cj-link-hover); }}

/* The nav: files and their declarations, fixed beside the listing on a
   desktop, a drawer behind a button on a phone. */
.leannav {{
  position: fixed; top: 0; left: 0; bottom: 0; width: var(--leannav-w);
  overflow-y: auto; padding: 1.2rem 1rem 3rem;
  background: var(--cj-bg); border-right: 1px solid var(--cj-rule);
  font-size: 0.82rem;
}}
.leannav-head {{
  display: flex; align-items: flex-start; gap: 0.5rem;
  margin-bottom: 1rem; padding-bottom: 0.8rem;
  border-bottom: 1px solid var(--cj-rule);
}}
.leannav-head div {{ flex: 1 1 auto; min-width: 0; }}
.leannav-up {{
  display: block; text-decoration: none; color: var(--cj-muted) !important;
  font-size: 0.9em; margin-bottom: 0.25rem;
}}
.leannav-up:hover {{ color: var(--cj-link) !important; }}
.leannav-id {{
  font-family: var(--cj-display); font-size: 1.15em; display: block;
  text-decoration: none;
}}
.leannav ul {{ list-style: none; margin: 0 0 1.2rem; padding: 0; }}
.leannav-file {{
  font-family: var(--cj-mono); font-size: 0.95em; margin-top: 1rem;
  padding-top: 0.6rem; border-top: 1px solid var(--cj-rule);
}}
.leannav-file:first-child {{ border-top: 0; margin-top: 0; padding-top: 0; }}
.leannav li a {{ text-decoration: none; display: block; padding: 0.12rem 0; }}
.leannav-decl a {{
  font-family: var(--cj-mono); font-size: 0.92em; padding-left: 0.9rem;
  overflow-wrap: anywhere;
}}
.leannav-namespace a {{
  color: var(--cj-muted) !important; font-style: italic; margin-top: 0.4rem;
}}
.leannav-kind {{ color: var(--cj-muted); font-style: italic; font-size: 0.85em; }}
.leannav-sorry {{ color: var(--lean-sorry); }}

/* The theme button and the phone-only nav button, both plain squares so they
   read as controls without competing with the accent colour. */
.lean-theme, .lean-nav-toggle {{
  background: none; border: 1px solid var(--cj-rule); border-radius: 0.25rem;
  color: var(--cj-muted); cursor: pointer; font-family: var(--cj-serif);
}}
.lean-theme {{ display: none; padding: 0.3rem; line-height: 0; flex: 0 0 auto; }}
.lean-theme svg {{
  width: 1rem; height: 1rem; fill: none; stroke: currentColor;
  stroke-width: 1.6; stroke-linecap: round;
}}
.lean-theme:hover, .lean-nav-toggle:hover {{
  color: var(--cj-link); border-color: var(--cj-link);
}}
.lean-moon, .lean-theme[data-theme-state="dark"] .lean-sun {{ display: block; }}
.lean-sun, .lean-theme[data-theme-state="dark"] .lean-moon {{ display: none; }}
.lean-nav-toggle {{
  display: none; position: fixed; top: 0.6rem; left: 0.6rem; z-index: 3;
  padding: 0.35rem 0.7rem; background: var(--cj-bg);
}}

main {{ margin-left: var(--leannav-w); padding: 2rem 1.5rem 6rem; }}
.lean-body {{ max-width: 62rem; margin: 0 auto; }}
h1 {{ font-family: var(--cj-display); font-size: 1.6rem; font-style: italic;
     color: var(--cj-link); margin: 0 0 0.4rem; }}
h2 {{
  font-family: var(--cj-mono); font-size: 1.1rem; margin: 2.6rem 0 0.2rem;
  padding-top: 1.2rem; border-top: 1px solid var(--cj-rule);
}}
h2 a {{ text-decoration: none; }}
.lean-lede {{ margin: 0 0 0.6rem; }}
.lean-meta {{ color: var(--cj-muted); font-size: 0.85rem; margin: 0 0 1.6rem; }}
.lean-meta a {{ color: var(--cj-muted); }}
.lean-meta a:hover {{ color: var(--cj-link); }}
.lean-filemeta {{ color: var(--cj-muted); font-size: 0.85rem; margin: 0 0 0.8rem; }}
.lean-note {{
  background: var(--cj-code-bg); border-left: 2px solid var(--cj-link);
  padding: 0.8rem 1rem; margin: 0 0 1.8rem; font-size: 0.92rem;
}}
.lean-note p {{ margin: 0.4rem 0; }}
.lean-note p:first-child {{ margin-top: 0; }}
.lean-note p:last-child {{ margin-bottom: 0; }}

/* The listing. Wide lines scroll inside the block, never the page. */
pre.lean {{
  background: var(--cj-code-bg); border: 1px solid var(--cj-rule);
  border-radius: 0.25rem; margin: 0 0 1rem; padding: 0.9rem 0;
  overflow-x: auto; font-family: var(--cj-mono); font-size: 0.83rem;
  line-height: 1.55; tab-size: 2;
  /* Each line is a block that preformats its own text (.lean-src below), so
     the newlines this file is written with -- one line span per source line,
     to keep a regenerated page's diff readable -- must not render as blank
     lines here. */
  white-space: normal;
}}
.lean-line {{ display: block; padding-right: 1rem; }}
.lean-line:target {{
  background: var(--cj-target);
  /* A line jumped to lands under the top edge of the window otherwise, which
     on a phone is under the Files button as well. */
  scroll-margin-top: 4rem;
}}
.lean-ln {{
  display: inline-block; width: 3.2rem; padding-right: 1rem;
  text-align: right; color: var(--cj-muted) !important; text-decoration: none;
  /* Not part of the code: excluded from a copy so pasting the listing into an
     editor gives Lean, not Lean with a column of numbers down the side. */
  user-select: none; -webkit-user-select: none;
}}
.lean-ln:hover {{ color: var(--cj-link) !important; }}
.lean-src {{ white-space: pre; }}
{syntax}
/* Docstrings and block comments are prose, and the files here use them to
   carry the design notes a reader needs most; dimming them to comment grey
   buries the argument. Serif, near-full contrast, still in the listing. */
.lean-src .cm, .lean-src .sd {{
  color: var(--lean-prose); font-family: var(--cj-serif); font-style: italic;
  font-size: 1.08em;
}}
/* The one thing a reader of a Conjura statement must not miss. */
.lean-src .gr, .lean-src .ge {{
  color: var(--lean-sorry); background: var(--lean-sorry-bg);
  padding: 0 0.2em; border-radius: 0.15em; font-weight: 600;
}}
.lean-src .err {{
  color: var(--lean-sorry); text-decoration: underline wavy;
}}
footer {{
  margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--cj-rule);
  color: var(--cj-muted); font-size: 0.85rem;
}}

@media (max-width: 62rem) {{
  .leannav {{
    transform: translateX(-100%); transition: transform 0.2s ease; z-index: 2;
    width: min(var(--leannav-w), 88vw);
  }}
  .lean-nav-open .leannav {{ transform: none; }}
  .lean-nav-toggle {{ display: block; }}
  main {{ margin-left: 0; padding: 3.4rem 0.9rem 5rem; }}
}}
"""


def build(pkg: pathlib.Path, out_dir: pathlib.Path):
    files = package_files(pkg)
    if not files:
        sys.exit(f"{pkg}: no .lean files to render.")

    meta = frontmatter(pkg.parent / "index.qmd")
    cid = meta.get("id", "")
    title = meta.get("title", "")
    short = meta.get("short_title", title)
    toolchain = ""
    tc = pkg / "lean-toolchain"
    if tc.exists():
        toolchain = tc.read_text(encoding="utf-8").strip()
    mathlib = ""
    lakefile = pkg / "lakefile.toml"
    if lakefile.exists():
        m = re.search(
            r'name\s*=\s*"mathlib".*?rev\s*=\s*"([^"]+)"',
            lakefile.read_text(encoding="utf-8"), re.S)
        if m:
            mathlib = m.group(1)

    # Relative paths computed from wherever the page is actually written, not
    # assumed to be `<package>/html/`: `--out` is allowed to put it elsewhere,
    # and a link built from a guess would be broken exactly there.
    rel_page = os.path.relpath(pkg.parent, out_dir) + "/"
    rel_raw = os.path.relpath(pkg, out_dir) + "/"
    gh_dir = f"{GITHUB}/{rel_to_repo(pkg)}"

    nav: list[str] = ["<ul>"]
    body: list[str] = []
    totals = {"lines": 0, "decls": 0, "sorries": 0}

    for path in files:
        # The module's path inside the package, with the separators turned into
        # dashes, is the anchor prefix: unique even when two subtrees hold a
        # `Basic.lean`, and equal to the bare name for a flat package, so
        # `#Statement-L42` keeps meaning what it means today.
        rel = path.relative_to(pkg)
        slug = rel.with_suffix("").as_posix().replace("/", "-")
        label = rel.as_posix()
        markup, counts, decls = render(path, slug)
        for k in totals:
            totals[k] += counts[k]

        nav.append(
            f"<li class='leannav-file'><a href='#file-{slug}'>{label}</a></li>")
        for kind, keyword, name, line in decls:
            cls = "leannav-namespace" if kind == "namespace" else "leannav-decl"
            dlabel = html.escape(name)
            tag = f"<span class='leannav-kind'>{keyword}</span> " if kind == "decl" else ""
            nav.append(
                f"<li class='{cls}'><a href='#{slug}-L{line}'>{tag}{dlabel}</a></li>")

        bits = [plural(counts["lines"], "line"),
                plural(counts["decls"], "declaration")]
        if counts["sorries"]:
            bits.append(
                f"<span class='leannav-sorry'>{plural(counts['sorries'], 'sorry', 'sorries')}"
                "</span>")
        else:
            bits.append("no sorries")
        body.append(
            f"<h2 id='file-{slug}'><a href='#file-{slug}'>{label}</a></h2>\n"
            f"<p class='lean-filemeta'>{' &middot; '.join(bits)} &middot; "
            f"<a href='{rel_raw}{label}'>raw file</a> &middot; "
            f"<a href='{gh_dir}/{label}'>on GitHub</a></p>\n"
            f"<pre class='lean' tabindex='0'>\n{chr(10).join(markup)}\n</pre>"
        )
    nav.append("</ul>")

    who = f"c/{cid}" if cid else rel_to_repo(pkg)
    heading = f"{who} &mdash; Lean sources"
    lede = html.escape(title) if title else ""
    env = " &middot; ".join(x for x in (
        f"toolchain <code>{html.escape(toolchain)}</code>" if toolchain else "",
        f"Mathlib <code>{html.escape(mathlib)}</code>" if mathlib else "",
    ) if x)
    sorry_line = (
        f"{plural(totals['sorries'], 'sorry', 'sorries')} in the package"
        if totals["sorries"] else "no sorries in the package")

    # The notes beside the sources are linked on GitHub rather than in place:
    # Pages serves .md as text/markdown, which some browsers render as plain
    # text and others download, whereas GitHub renders it. (The per-file "raw"
    # links below do point in place, and Pages serves .lean as
    # application/octet-stream, so those are downloads by design -- that link
    # is there for the reader who wants the bytes the compiler sees.)
    extras = [q.name for q in sorted(pkg.glob("*.md"))]
    extra_line = ""
    if extras:
        links = ", ".join(f"<a href='{gh_dir}/{n}'>{n}</a>" for n in extras)
        extra_line = f"<p class='lean-meta'>Beside the sources: {links}.</p>"

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{who} Lean sources &mdash; {html.escape(short)}</title>
<meta name="description" content="The Lean sources of {who}, syntax-highlighted, with line anchors and every sorry marked.">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
{HEAD_JS}
<style>
{stylesheet()}</style>
</head>
<body>
<button class="lean-nav-toggle" type="button" aria-controls="leannav" aria-expanded="false">Files</button>
<nav class="leannav" id="leannav" aria-label="Files and declarations">
  <div class="leannav-head">
    <div>
      <a class="leannav-up" href="{rel_page}">&#8592; {who}</a>
      <a class="leannav-id" href="#top">Lean sources</a>
    </div>
    {THEME_BTN}
  </div>
{''.join(nav)}
</nav>
<main id="top">
<div class="lean-body">
<h1>{heading}</h1>
<p class="lean-lede">{lede}</p>
<p class="lean-meta">
  {plural(len(files), 'file')} &middot; {plural(totals['lines'], 'line')} &middot;
  {plural(totals['decls'], 'declaration')} &middot; {sorry_line}
  {(' &middot; ' + env) if env else ''}<br>
  <a href="{rel_page}">Statement page</a> &middot;
  <a href="{gh_dir}">Sources on GitHub</a>
</p>
{extra_line}
<div class="lean-note">
<p>This page is generated from the files themselves by
<a href="{GITHUB}/scripts/build_lean_html.py">scripts/build_lean_html.py</a>;
edits made here are destroyed by the next run. It is a reading copy, not a
certificate: what a statement compiles to is decided by the compiler, and a
marked <code>sorry</code> is an unproved goal, so a file can be green in CI and
still assert nothing on its own.</p>
<p>Every line is addressable &mdash; click a line number, or append
<code>#Statement-L42</code> to the URL.</p>
</div>
{''.join(body)}
<footer>
Generated by <code>scripts/build_lean_html.py</code> from
<code>{rel_to_repo(pkg)}</code>. Highlighting by Pygments'
Lean&nbsp;4 lexer; see the script's header for why not doc-gen4.
</footer>
</div>
</main>
{JS}
</body>
</html>
"""

    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page, encoding="utf-8")
    return out, files, totals


def check(out: pathlib.Path, pkg: pathlib.Path, files, totals) -> None:
    """Fail loudly on the mistakes this page could ship silently."""
    text = out.read_text(encoding="utf-8")
    failures: list[str] = []

    def chk(label: str, got, want) -> None:
        if got != want:
            failures.append(f"{label}: got {got!r}, want {want!r}")

    chk("each palette written exactly once",
        (text.count("--cj-bg: #faf9f5"), text.count("--cj-bg: #1f1e1d")), (1, 2))
    chk("every file rendered",
        sum(text.count(f"id='file-{q.relative_to(pkg).with_suffix('').as_posix().replace('/', '-')}'")
            for q in files), len(files))
    chk("one line anchor per source line",
        text.count('class="lean-line"'), totals["lines"])
    # A `sorry` in prose is not a `sorry` in the development: the token count
    # is the smaller number by construction, and this is what says so.
    grep = sum(p.read_text(encoding="utf-8").count("sorry") for p in files)
    if totals["sorries"] > grep:
        failures.append(
            f"more sorry tokens ({totals['sorries']}) than occurrences of the "
            f"word ({grep}); the lexer or the counter is wrong")
    # Escaping, checked by counting rather than by eye: Lean is full of `<`,
    # and one unescaped angle bracket silently eats the rest of a line as a
    # tag. The page's own entities are written with a literal `&`, so the
    # `&amp;` count is exactly the sources' `&` count.
    src = "".join(p.read_text(encoding="utf-8") for p in files)
    chk("every < escaped", text.count("&lt;"), src.count("<"))
    chk("every > escaped", text.count("&gt;"), src.count(">"))
    chk("every & escaped", text.count("&amp;"), src.count("&"))

    if failures:
        sys.exit("self-checks failed:\n  " + "\n  ".join(failures))


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Render a Lean package's sources as one highlighted HTML page.")
    ap.add_argument("package", type=pathlib.Path,
                    help="the Lean package directory, e.g. c/0004/lean")
    ap.add_argument("--out", type=pathlib.Path, default=None,
                    help="output directory (default: <package>/html)")
    args = ap.parse_args()

    pkg = args.package.resolve()
    if not pkg.is_dir():
        sys.exit(f"{args.package}: not a directory")
    out_dir = args.out.resolve() if args.out else pkg / "html"

    out, files, totals = build(pkg, out_dir)
    check(out, pkg, files, totals)
    print(f"wrote {rel_to_repo(out)} "
          f"({plural(len(files), 'file')}, {plural(totals['lines'], 'line')}, "
          f"{plural(totals['decls'], 'declaration')}, "
          f"{plural(totals['sorries'], 'sorry', 'sorries')})")


if __name__ == "__main__":
    main()
