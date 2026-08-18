#!/usr/bin/env python3
"""Render a functionality's interface box from LaTeX to the HTML on its page.

One interface definition, two consumers. The definition lives in

    surveys/uc-for-gamers/latex/functionalities/<id>.tex

as a `\\begin{interface}` environment; `main.tex` `\\input`s it, and this
script renders the same file to the `.cj-interface` block on

    uc/layer-N-.../<id>/index.qmd

so that neither copy is transcribed by hand. `--check` compares the two and
fails when they have drifted, which is what makes the arrangement worth
having: without it the fragment is just a file the page happens to resemble.

    python3 scripts/gen_interface.py            # rewrite every page's box
    python3 scripts/gen_interface.py --check     # fail if any page has drifted
    python3 scripts/gen_interface.py f-sig       # one functionality
    python3 scripts/gen_interface.py --stdout f-sig
    python3 scripts/gen_interface.py --vs-pdf    # numbers vs the printed book
    python3 scripts/gen_interface.py --vs-preview f-com   # ... vs a standalone
                                                          # compile of the
                                                          # fragment itself

Line numbers are *computed*, never read out of the source. `algpseudocode`
numbers each block from 1 and the book carries a running count across blocks
by hand, through `\\algcont`/`\\algsave` and the `contline` counter; this
script runs that same counter, so a line inserted mid-box renumbers
everything after it in the HTML exactly as it does in the PDF. That is the
failure this whole arrangement exists to prevent: the old hand-written
blocks hardcoded `<ol start="N">`, and nothing noticed when N went stale.

Because that counter is *reimplemented* here rather than shared with LaTeX,
`--check` can only prove the page agrees with the fragment, not that either
agrees with the book. `--vs-pdf` closes that loop: it reads the numbers out
of the compiled PDF's text layer and compares. It is a local verification
aid, not a CI gate, for the reasons in check_vs_pdf's docstring. `--vs-preview`
does the same for a fragment the book does not typeset -- which is every
encyclopedia box beyond the seven the book carries -- by compiling it on its
own through functionalities/preview.tex.

Macro meanings are read from the two shared style files rather than
duplicated here, so a new `\\newcommand` is understood without touching this
file: ucgamers.sty for the book's own notation, and
functionalities/encyclopedia.sty for the names of the functionalities the
book does not typeset -- kept apart so that writing an encyclopedia entry
does not mark the book's PDF stale. The exceptions are in MACRO_OVERRIDES
below: macros whose LaTeX expansion is not something MathJax can render.
"""

import argparse
import difflib
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LATEX = REPO / "surveys" / "uc-for-gamers" / "latex"
FRAGMENTS = LATEX / "functionalities"
# Both are read for macros; only the first is an input of the book. See
# encyclopedia.sty's header for why the split exists.
STY = LATEX / "ucgamers.sty"
ENCYCLOPEDIA_STY = FRAGMENTS / "encyclopedia.sty"
UC = REPO / "uc"

# Macros whose style-file definition cannot be handed to MathJax as-is.
# \op is \textnormal{\textsc{...}}, and MathJax has no small-caps math font;
# \id expands to a bare `id`, which sets as two italic variables rather than
# one name. Each entry is (number of arguments, replacement body).
MACRO_OVERRIDES = {
    "op": (1, r"\mathsf{#1}"),
    "opl": (1, r"\mathsf{#1}"),
    "opdef": (1, r"\mathsf{#1}"),
    "fopl": (1, r"\mathsf{Full#1}"),
    "fopdef": (1, r"\mathsf{Full#1}"),
    "atom": (1, r"\mathsf{#1}"),
    "id": (0, r"\mathit{id}"),
}

# Value atoms. In the book these are small caps in the comment colour; on the
# page they are a span, so they leave the surrounding math rather than being
# faked inside it.
ATOMS = {"ok", "rej", "true", "false", "done"}

# Identifier macros as they appear in an operation signature's argument list,
# where the output is HTML rather than math.
SIG_IDENTS = {
    "vk": "vk", "msg": "msg", "sigma": "&sigma;", "tau": "&tau;",
    "id": "id", "PID": "pid",
}


# --------------------------------------------------------------- macros

def load_macros(*styles):
    """Read \\newcommand/\\renewcommand definitions out of the style files.

    Defaults to both of them, in load order, so a name defined in the
    encyclopedia file wins over the book's -- the same way LaTeX resolves it.
    """
    macros = {}
    for sty in styles or (STY, ENCYCLOPEDIA_STY):
        if not sty.exists():
            continue
        text = sty.read_text()
        for m in re.finditer(r"\\(?:re)?newcommand\{\\([A-Za-z]+)\}(\[(\d)\])?\{", text):
            name, nargs = m.group(1), int(m.group(3) or 0)
            body, ok = _brace_arg(text, m.end() - 1)
            if ok:
                macros[name] = (nargs, body)
    macros.update(MACRO_OVERRIDES)
    return macros


def _brace_arg(text, i):
    """Read the balanced {...} group starting at text[i] == '{'."""
    if i >= len(text) or text[i] != "{":
        return "", False
    depth, j = 0, i
    while j < len(text):
        if text[j] == "\\":
            j += 2
            continue
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], True
        j += 1
    return "", False


def expand(s, macros, depth=0):
    """Expand macros until nothing is left that we know how to expand."""
    if depth > 24:
        raise RuntimeError("macro expansion did not terminate in: " + s[:80])
    out, i, changed = [], 0, False
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            m = re.match(r"\\([A-Za-z]+)", s[i:])
            if not m:                       # \{ \} \, \! and friends
                out.append(s[i:i + 2])
                i += 2
                continue
            name = m.group(1)
            if name not in macros:
                out.append(m.group(0))
                i += m.end()
                continue
            nargs, body = macros[name]
            j = i + m.end()
            args = []
            for _ in range(nargs):
                while j < len(s) and s[j] == " ":
                    j += 1
                arg, ok = _brace_arg(s, j)
                if not ok:
                    raise RuntimeError(r"\%s wants an argument in: %s" % (name, s[:80]))
                args.append(arg)
                j += len(arg) + 2
            for k, a in enumerate(args, 1):
                body = body.replace("#%d" % k, a)
            out.append(body)
            i, changed = j, True
        else:
            out.append(s[i])
            i += 1
    result = "".join(out)
    return expand(result, macros, depth + 1) if changed else result


def tidy_math(s):
    """Cosmetic joins that make the emitted math read like handwritten math."""
    prev = None
    while prev != s:                        # \mathsf{G}\mathsf{PKI} -> \mathsf{GPKI}
        prev = s
        s = re.sub(r"\\mathsf\{([^{}]*)\}\\mathsf\{([^{}]*)\}", r"\\mathsf{\1\2}", s)
    return re.sub(r"\s+", " ", s).strip()


# ----------------------------------------------------------- fragments

class Op:
    def __init__(self, sig):
        self.sig = sig          # raw LaTeX of the \opsig argument, plus any "from"
        self.lines = []         # list of (number|None, html)


def parse_fragment(path, macros):
    """Pull the title, the parameter line and the operations out of a fragment."""
    text = path.read_text()

    m = re.search(r"\\begin\{interface\}(\[[^\]]*\])?\s*\{", text)
    if not m:
        raise RuntimeError("%s: no \\begin{interface}" % path.name)
    head, ok = _brace_arg(text, m.end() - 1)
    if not ok:
        raise RuntimeError("%s: unterminated interface title" % path.name)

    title_tex, _, params_tex = head.partition("\\\\")
    pm = re.search(r"\\params\s*\{", params_tex)
    params_tex = _brace_arg(params_tex, pm.end() - 1)[0] if pm else ""

    body = text[m.end() + len(head) + 1:]
    body = body[:body.index("\\end{interface}")]

    ops, op = [], None
    contline, lineno = 0, 0
    pending_sig = None
    in_alg = False

    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("%%"):
            continue

        if line.startswith("\\opsig"):
            pending_sig = line
            continue
        if line.startswith("\\begin{algorithmic}"):
            if pending_sig is None:
                raise RuntimeError("%s: algorithmic block with no \\opsig" % path.name)
            op = Op(pending_sig)
            pending_sig, in_alg = None, True
            continue
        if line.startswith("\\end{algorithmic}"):
            ops.append(op)
            op, in_alg = None, False
            continue
        if not in_alg:
            continue                        # multicols, \vspace, \columnbreak, \scriptsize

        # The running line count, exactly as the book keeps it: \algcont
        # resumes from `contline` and \algsave hands the count on, so a line
        # added anywhere renumbers the rest of the box here and in the PDF
        # alike. Both may share a line with \setcounter.
        m = re.match(r"\\setcounter\{contline\}\{(\d+)\}\s*", line)
        if m:
            contline, line = int(m.group(1)), line[m.end():].strip()
        if line.startswith("\\algcont"):
            lineno = contline
            line = line[len("\\algcont"):].strip()
        if line.startswith("\\algsave"):
            contline = lineno
            line = line[len("\\algsave"):].strip()
        if not line:
            continue
        if line.startswith("\\EndIf") or line.startswith("\\EndOn") \
                or line.startswith("\\EndIndent"):
            op.depth = max(0, getattr(op, "depth", 0) - 1)
            continue

        if line.startswith("\\Comment"):    # a comment on its own line
            body_txt, _ = _brace_arg(line, line.index("{"))
            n, html = op.lines[-1]
            op.lines[-1] = (n, html + comment_html(body_txt, macros))
            continue

        if line.startswith("\\Statex"):     # unnumbered continuation of the line above
            n, html = op.lines[-1]
            op.lines[-1] = (n, merge_continuation(html, line[len("\\Statex"):], macros))
            continue

        depth = getattr(op, "depth", 0)
        if line.startswith("\\If"):
            cond, _ = _brace_arg(line, line.index("{"))
            content = r"$\textbf{if}\ " + strip_math(cond) + r"\ \textbf{then}$"
            op.depth = depth + 1
        elif line.startswith("\\Req"):
            arg, _ = _brace_arg(line, line.index("{"))
            content = r"$\textbf{require}\ " + strip_math(arg) + "$"
        elif line.startswith("\\State"):
            content = line[len("\\State"):]
        else:
            raise RuntimeError("%s: unhandled line %r" % (path.name, line))

        lineno += 1
        op.lines.append((lineno, statement_html(content, macros, depth)))

    if op is not None or pending_sig is not None:
        raise RuntimeError("%s: unclosed operation block" % path.name)

    return {
        "title": inline_html(title_tex, macros),
        "params": params_html(params_tex, macros),
        "ops": ops,
    }


def strip_math(s):
    """`$x$` -> `x`, for a condition we are about to wrap in more math."""
    s = s.strip()
    return s[1:-1].strip() if s.startswith("$") and s.endswith("$") else s


# --------------------------------------------------------------- lines

# A math group: `$...$`, where an escaped `\$` (the sampling arrow's own
# dollar, in `\gets_{\$}`) is a character and not a delimiter.
MATH = re.compile(r"(?<!\\)\$((?:[^$\\]|\\.)*)\$", re.S)


def segments(s, macros):
    """Split a run of LaTeX into ('math'|'atom'|'text', value) segments."""
    out, i = [], 0
    for m in MATH.finditer(s):
        if m.start() > i:
            out += roman_segments(s[i:m.start()])
        inner = m.group(1).strip()
        if inner.startswith("\\") and inner.lstrip("\\") in ATOMS:
            out.append(("atom", inner.lstrip("\\")))
        else:
            out.append(("math", tidy_math(expand(inner, macros))))
        i = m.end()
    if i < len(s):
        out += roman_segments(s[i:])
    return out


def roman_segments(t):
    """Text between maths. `\\textbf{...}` is a code keyword, so it becomes
    math and merges with whatever maths sits beside it; the book sets the
    rest -- `for each`, `as`, a trailing semicolon -- in upright roman, and
    so does the page."""
    out, i = [], 0
    for m in re.finditer(r"\\textbf\{([^{}]*)\}", t):
        if m.start() > i:
            out.append(("text", t[i:m.start()]))
        out.append(("math", r"\textbf{%s}" % m.group(1)))
        i = m.end()
    if i < len(t):
        out.append(("text", t[i:]))
    return out


def render(segs):
    """Segments to HTML, merging math that is only separated by a space."""
    merged = []
    for kind, val in segs:
        if kind == "text" and re.fullmatch(r" ?", val) and merged \
                and merged[-1][0] == "math":
            merged.append(("glue", val))
            continue
        if kind == "math" and len(merged) >= 2 and merged[-1][0] == "glue" \
                and merged[-2][0] == "math":
            merged.pop()
            k, prev = merged.pop()
            merged.append(("math", (prev + r"\ " + val).strip()))
            continue
        if merged and merged[-1][0] == "glue":
            k, v = merged.pop()
            merged.append(("text", v))
        merged.append((kind, val))
    if merged and merged[-1][0] == "glue":
        merged[-1] = ("text", merged[-1][1])

    out = []
    for kind, val in merged:
        if kind == "math":
            out.append(r"\(" + val + r"\)")
        elif kind == "atom":
            out.append('<span class="cj-atom">%s</span>' % val)
        else:
            out.append(text_html(val))
    return "".join(out).strip()


def text_html(s):
    """Roman text between maths: `\\ ` is a hard space, the rest is prose."""
    s = re.sub(r"\\label\{[^{}]*\}", "", s)
    s = s.replace(r"\quad", "&nbsp;&nbsp;").replace("\\ ", "&nbsp;")
    s = re.sub(r"\\,|\\;|\\!", "", s)
    return re.sub(r"\s+", " ", s)          # a line break in the .tex is a space here


def statement_html(content, macros, depth):
    content = re.sub(r"\\label\{[^{}]*\}", "", content).strip()
    indent = depth > 0
    if content.startswith(r"\quad"):         # a hanging continuation line
        content, indent = content[len(r"\quad"):].strip(), True
    elif content.startswith(r"\algand"):     # the aligned-∧ continuation
        content = r"$\wedge$ " + content[len(r"\algand"):].lstrip("\\ ").strip()
        indent = True
    html = render(segments(content, macros))
    return '<span class="cj-ind">%s</span>' % html if indent else html


def merge_continuation(html, tail, macros):
    """Fold a `\\Statex` line into the `\\State` above it, math and all."""
    tail = re.sub(r"\\label\{[^{}]*\}", "", tail).strip()
    tail = re.sub(r"^\\quad\\?\s*", "", tail).strip()
    m = re.fullmatch(r"\$(.*)\$", tail, re.S)
    if m and html.endswith(r"\)"):
        return html[:-2] + " " + tidy_math(expand(m.group(1), macros)) + r"\)"
    return html + " " + render(segments(tail, macros))


def comment_html(body, macros):
    return '<span class="cj-comment">// %s</span>' % render(segments(body, macros))


def inline_html(s, macros):
    return render(segments(s.strip(), macros))


def params_html(s, macros):
    return render(segments(s.strip(), macros)).replace("&nbsp;&nbsp;", "&nbsp;")


# ---------------------------------------------------------- signatures

def sig_html(raw, macros):
    """`\\opsig{$\\id.\\op{Rnd}()$} \\quad from $\\id'$` to its HTML."""
    i = raw.index("{")
    inner, _ = _brace_arg(raw, i)
    rest = raw[i + len(inner) + 2:]
    trailing_colon = rest.lstrip().startswith(":")
    frm = re.search(r"from\s+\$([^$]*)\$", rest)

    inner = strip_math(inner)
    html = ""

    if inner.startswith(r"\id."):
        html += '<span class="cj-id">id</span>.'
        inner = inner[len(r"\id."):]

    m = re.match(r"\\(op|opdef|opl|fopl|fopdef)\{([A-Za-z]+)\}", inner)
    if m:
        name = ("Full" if m.group(1).startswith("fop") else "") + m.group(2)
        inner = inner[m.end():]
    else:
        m = re.match(r"\\([A-Za-z]+)", inner)
        if not m:
            raise RuntimeError("cannot read operation name from %r" % inner)
        name, inner = m.group(1), inner[m.end():]

    html += name
    if inner.startswith("_"):
        sub, _ = _brace_arg(inner, inner.index("{"))
        html += "<sub>%s</sub>" % sig_token(sub)
        inner = inner[inner.index("{") + len(sub) + 2:]

    args, ok = _brace_arg("{" + inner.strip()[1:], 0) if inner.strip().startswith("(") \
        else ("", False)
    if inner.strip().startswith("("):
        args = inner.strip()[1:inner.strip().rindex(")")]
    html += "(" + render_args(args) + ")"

    if frm:
        who = frm.group(1).replace(r"\id", "").replace("'", "")
        html += ('<span class="cj-op-from">from <span class="cj-id">id</span>'
                 '&prime;%s</span>' % who)
    elif trailing_colon:
        html += ":"
    return html


def render_args(args):
    if not args.strip():
        return ""
    parts = re.split(r"([,;])", args)
    out = []
    for part in parts:
        if part in (",", ";"):
            out.append(part + " ")
        elif part.strip():
            out.append(sig_token(part.strip()))
    return "".join(out).rstrip(", ")


def sig_token(tok):
    tok = tok.strip()
    m = re.fullmatch(r"\\(?:V|op|opl|opdef)\{([A-Za-z]+)\}", tok)
    if m:
        return '<span class="cj-rm">%s</span>' % m.group(1)
    if tok.startswith("\\"):
        name = tok[1:]
        return '<span class="cj-id">%s</span>' % SIG_IDENTS.get(name, name)
    return '<span class="cj-id">%s</span>' % tok


# ----------------------------------------------------------- rendering

def to_html(box, macros):
    out = ['<div class="cj-interface">',
           '<div class="cj-interface-head">',
           '<div class="cj-interface-title">%s</div>' % box["title"],
           '<div class="cj-interface-params">%s</div>' % box["params"],
           "</div>",
           '<div class="cj-interface-body">']
    for op in box["ops"]:
        start = op.lines[0][0] if op.lines else 1
        out += ["", '<div class="cj-op">',
                '<div class="cj-op-sig">%s</div>' % sig_html(op.sig, macros),
                '<ol class="cj-code" start="%d">' % start]
        out += ["<li>%s</li>" % html for _, html in op.lines]
        out += ["</ol>", "</div>"]
    out += ["", "</div>", "</div>"]
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- pages

BLOCK = re.compile(r"```\{=html\}\n(<div class=\"cj-interface\">.*?)```\n", re.S)


def pdf_line_numbers(fid, pages, want):
    """The line numbers actually printed in the book, for one box.

    Locates the box by its printed title and reads back the `N:` labels.
    The subscript is set in small caps, so its case in the PDF text layer
    varies per name (`FRand`, but `GPKI` and `FAC`); match case-insensitively.
    """
    kind, name = fid.split("-", 1)
    rx = re.compile(r"Functionality\s+" + ("F" if kind == "f" else "G")
                    + r"\s*" + name + r"\b", re.I)
    labels = printed_labels
    for i, page in enumerate(pages):
        if not rx.search(page):
            continue
        here = labels(page)
        nxt = labels(pages[i + 1]) if i + 1 < len(pages) else []
        combined = here + [n for n in nxt if n > (here[-1] if here else 0)]
        if not combined:
            continue
        # The name is discussed in the prose around the box as well, so the
        # first page mentioning it need not be the one carrying it. Attribute
        # the box to the page whose labels actually overlap what we computed.
        box_page = i if set(want) & set(here) else i + 1
        return combined, box_page + 1
    return None, None


def printed_labels(text):
    """The `N:` line labels algpseudocode printed, in order of appearance."""
    return [int(n) for n in re.findall(r"(?:^|\s)(\d{1,3}):\s", text)]


def html_line_numbers(html):
    """The line numbers the generated web block prints, in order."""
    out = []
    for start, body in re.findall(r'<ol class="cj-code" start="(\d+)">(.*?)</ol>',
                                  html, re.S):
        out.extend(range(int(start), int(start) + len(re.findall(r"<li>", body))))
    return out


def page_for(fid):
    hits = sorted(UC.glob("layer-*/%s/index.qmd" % fid))
    if len(hits) != 1:
        raise SystemExit("expected exactly one page for %s, found %d" % (fid, len(hits)))
    return hits[0]


def fragments(only=None):
    ids = sorted(p.stem for p in FRAGMENTS.glob("*.tex") if p.stem != "preview")
    if only:
        missing = [f for f in only if f not in ids]
        if missing:
            raise SystemExit("no fragment for: " + ", ".join(missing))
        ids = [f for f in ids if f in only]
    return ids


def check_vs_pdf(ids):
    """Confirm the computed line numbers are the ones the book prints.

    `--check` proves the page matches the fragment. It cannot prove either
    matches the book, because the running `\\algcont`/`\\algsave` count is
    reimplemented here rather than shared with LaTeX. This closes that loop
    against the compiled PDF.

    Deliberately not a CI gate. It needs `pdftotext` (poppler), it reads a
    committed PDF that is only as fresh as its last rebuild, and it leans on
    the text layer of a small-caps subscript. A false red here would block
    the site deploy for a reason that has nothing to do with the site.
    """
    pdf = LATEX.parent / "pdf" / "main.pdf"
    if not pdf.exists():
        print("no compiled book at %s" % pdf.relative_to(REPO))
        return 1
    try:
        out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                             capture_output=True, text=True, check=True).stdout
    except (FileNotFoundError, subprocess.CalledProcessError) as e:
        print("cannot run pdftotext (%s); install poppler to use --vs-pdf" % e)
        return 1

    pages = out.split("\f")
    macros = load_macros()
    bad = 0
    for fid in ids:
        want = html_line_numbers(to_html(parse_fragment(FRAGMENTS / (fid + ".tex"),
                                                        macros), macros))
        got, page = pdf_line_numbers(fid, pages, want)
        if got is None:
            print("%-9s NOT FOUND in the PDF" % fid)
            bad += 1
            continue
        span = sorted({n for n in got if want[0] <= n <= want[-1]})
        if span == sorted(set(want)):
            print("%-9s lines %d..%d (%d) match PDF page %d, printed folio %d"
                  % (fid, want[0], want[-1], len(want), page, page - 1))
        else:
            print("%-9s MISMATCH\n   computed: %s\n   printed : %s  (PDF page %d)"
                  % (fid, want, span, page))
            bad += 1
    print("\n%d box(es) checked against the PDF, %d mismatched" % (len(ids), bad))
    return 1 if bad else 0


def check_vs_preview(ids, keep=None):
    """Same check as --vs-pdf, but against the fragment compiled on its own.

    `--vs-pdf` can only check the seven boxes the book actually typesets. The
    encyclopedia's other ninety-seven have no printed counterpart, so the loop
    it closes -- are the numbers this script computes the numbers LaTeX
    prints? -- would be open for exactly the boxes nobody has proofread. The
    fragments already compile standalone through functionalities/preview.tex,
    which exists to keep them free of main.tex's preamble, so compile there
    and read the numbers off that.

    Slower than --vs-pdf (a pdflatex run per fragment) and needs a TeX
    installation, so it is a local gate for new work, not a CI one.
    """
    import tempfile

    macros = load_macros()
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(keep) if keep else Path(tmp)
        out.mkdir(parents=True, exist_ok=True)
        for fid in ids:
            want = html_line_numbers(to_html(
                parse_fragment(FRAGMENTS / (fid + ".tex"), macros), macros))
            job = out / fid
            try:
                r = subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                     "-jobname", fid, "-output-directory", str(out),
                     r"\def\FRAG{%s}\input{functionalities/preview}" % fid],
                    cwd=LATEX, capture_output=True, text=True,
                    # pdflatex writes font-encoded glyphs into its Overfull and
                    # Underfull warnings -- a \bigl\{ in a narrow column is
                    # enough -- and those bytes are not UTF-8. Decoding
                    # strictly turns a *successful* compile into a traceback.
                    errors="replace")
            except FileNotFoundError:
                print("cannot run pdflatex; install TeX to use --vs-preview")
                return 1
            if r.returncode or not job.with_suffix(".pdf").exists():
                tail = [ln for ln in r.stdout.splitlines() if ln.startswith("!")]
                print("%-9s DOES NOT COMPILE  %s" % (fid, tail[0] if tail else ""))
                bad += 1
                continue
            text = subprocess.run(
                ["pdftotext", "-layout", str(job.with_suffix(".pdf")), "-"],
                capture_output=True, text=True, check=True).stdout
            got = sorted(set(printed_labels(text)))
            if got == sorted(set(want)):
                print("%-9s lines %d..%d (%d) match the standalone compile"
                      % (fid, want[0], want[-1], len(want)))
            else:
                print("%-9s MISMATCH\n   computed: %s\n   printed : %s"
                      % (fid, want, got))
                bad += 1
    print("\n%d box(es) compiled standalone, %d mismatched" % (len(ids), bad))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ids", nargs="*", help="functionality ids; default all")
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit non-zero; write nothing")
    ap.add_argument("--stdout", action="store_true", help="print the HTML instead")
    ap.add_argument("--vs-pdf", action="store_true",
                    help="compare computed line numbers against the printed PDF "
                         "(needs pdftotext; not a CI gate, see below)")
    ap.add_argument("--vs-preview", action="store_true",
                    help="compile each fragment on its own and compare line "
                         "numbers; works for boxes the book does not typeset")
    ap.add_argument("--keep", metavar="DIR",
                    help="with --vs-preview, keep the compiled PDFs here")
    args = ap.parse_args()

    if args.vs_pdf:
        return check_vs_pdf(fragments(args.ids))
    if args.vs_preview:
        return check_vs_preview(fragments(args.ids), args.keep)

    macros = load_macros()
    drift, wrote = [], []

    for fid in fragments(args.ids):
        box = parse_fragment(FRAGMENTS / (fid + ".tex"), macros)
        html = to_html(box, macros)

        if args.stdout:
            print(html, end="")
            continue

        page = page_for(fid)
        text = page.read_text()
        m = BLOCK.search(text)
        if not m:
            raise SystemExit("%s: no .cj-interface block to replace" % page)
        if m.group(1) == html:
            continue
        if args.check:
            drift.append((fid, page, m.group(1), html))
        else:
            page.write_text(text[:m.start(1)] + html + text[m.end(1):])
            wrote.append(fid)

    if args.stdout:
        return 0

    if args.check:
        for fid, page, have, want in drift:
            print("drift: %s is not what %s.tex produces" %
                  (page.relative_to(REPO), fid))
            for line in difflib.unified_diff(
                    have.splitlines(), want.splitlines(),
                    fromfile="page", tofile="generated", lineterm="", n=1):
                print("  " + line)
        n = len(fragments(args.ids))
        print("%d box(es) checked, %d drifted" % (n, len(drift)))
        if drift:
            print("run `python3 scripts/gen_interface.py` to regenerate")
        return 1 if drift else 0

    print("%d box(es) updated out of %d scanned"
          % (len(wrote), len(fragments(args.ids))) +
          (": " + ", ".join(wrote) if wrote else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
