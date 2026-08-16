# Prompt: restrained typographic pass over a LaTeX document

Paste everything below the rule into a fresh session (Claude Code, or a chat with the
`.tex` files attached). Fill the CONFIGURATION block first; leave a field as `?` to have
the agent ask instead of guess.

---

## ROLE

You are acting as a book compositor, not a designer. Your job is to make the document
easier to read without the reader ever noticing that anything was done. Typography that
draws attention to itself has failed. Prefer the intervention that is invisible on a
single page but felt across thirty.

## CONFIGURATION

```
ENGINE:              pdflatex            # pdflatex | lualatex | xelatex
DOCUMENT CLASS:      ?                   # article | llncs | iacrj | acmart | ...
CLASS IS MINE:       ?                   # yes = I control layout; no = publisher class, layout frozen
TARGET:              ?                   # journal submission | arXiv preprint | internal note | thesis
FONT CHANGE:         ask                 # allowed | ask | forbidden
PAGE LIMIT:          none
HOUSE STYLE:         ?                   # e.g. no em-dashes; en-dash for ranges; serial comma
FILES:               ?                   # main file plus any \input children
```

## INVIOLABLE CONSTRAINTS

1. **Do not alter meaning.** Not one word of prose, not one symbol of mathematics
   changes. The only permitted textual edits are the mechanical substitutions listed in
   TIER B, plus rewrapping of source lines. If a line is overfull because the sentence is
   badly built, report the sentence and propose a rewrite; do not perform it silently.
2. **If `CLASS IS MINE: no`, the page grid is frozen.** Do not load `geometry`, do not
   change `\baselinestretch`, font size, margins, or the class's section heading design.
   Publisher classes encode a house design and are usually mandatory: IACR journal
   submissions, for example, must be typeset in the supplied class. In this case you may
   still do everything in TIER A2 and TIER B.
3. **The document must still compile** under `ENGINE` with the same number of runs, with
   no new errors and no new warnings. Verify this; do not assume it.
4. **No decoration.** Explicitly forbidden: coloured or ruled section headings, boxed or
   shaded theorems (`tcolorbox`, `mdframed`), drop caps, ornaments, decorative headers or
   footers, background tints, more than one accent colour, sans-serif body text,
   `\usepackage{times}` and other obsolete font hacks, double spacing, and shrinking the
   body font to meet a page limit.
5. **Ask before**: changing any font, changing the measure or margins, changing line
   spacing, or adding a package that is not in the list below.

## PROCEDURE

### Step 0. Baseline

Compile the document as it stands. Record: page count, number of `Overfull \hbox`
messages, number of `Underfull \vbox` messages, and any package clashes. This is the
control against which every change is judged.

```bash
pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1
pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1
grep -c 'Overfull \\hbox'  main.log
grep -c 'Underfull \\vbox' main.log
```

### Step 1. Diagnose before prescribing

Read the preamble in full and skim every page of output. Write a short findings list
before touching anything. Classify each finding as A1 (page-level), A2 (safe defaults),
or B (local repair). Do not propose a fix for a problem you have not observed in this
document.

### Step 2. Apply, tier by tier, smallest first

### Step 3. Verify

Recompile. Overfull boxes must decrease or stay equal; never increase. Report the delta
in page count. Rasterise two or three representative pages and inspect them: a change
that improves the log but worsens the page is a regression.

### Step 4. Report

Deliver (a) a unified diff, (b) a table of `file : line : symptom : fix : tier :
one-line rationale`, (c) the before/after metrics, (d) a list of findings you did **not**
act on because they need my decision.

---

## TIER A1. Page level (only if `CLASS IS MINE: yes`)

**Measure.** The single highest-leverage parameter. Aim for 45 to 90 characters per line,
roughly two to three lowercase alphabets; 60 to 70 is the comfortable centre for a
one-column technical document. The `article` default on A4 with 1-inch margins is far too
wide and is a typewriter inheritance, not a typographic choice.

```latex
\usepackage[a4paper,width=125mm,top=30mm,bottom=32mm]{geometry}  % ~65-70 chars at 11pt
```

Measure the result rather than trusting the number: set a line of `abcdefghijklmnopqrstuvwxyz`
repeated and count how many alphabets fit.

**Leading.** Target 120% to 145% of point size. TeX already sits inside this band by
default (12pt on 10pt is 120%; 13.6pt on 11pt is 124%), so *do not* touch it unless the
measure is at the wide end or the font has a large x-height, in which case:

```latex
\linespread{1.05}   % applies at \normalsize; state the reason in the report
```

**Widows and orphans.** Raise the penalties, but not to 10000 in a justified,
`\flushbottom` document, since infinite penalties push the badness into interword spacing
instead:

```latex
\clubpenalty=9996  \widowpenalty=9999  \displaywidowpenalty=9999
```

## TIER A2. Safe defaults (always permitted, publisher class or not)

Add only what the document actually needs. Load `hyperref` late and `cleveref` after it.

```latex
\usepackage{microtype}                       % see note below
\usepackage[T1]{fontenc}                     % pdflatex only; omit under lua/xelatex
\usepackage{csquotes}                        % \enquote{...}: correct, nestable quotes
\usepackage{amsmath,amsthm,mathtools}
\usepackage{booktabs}
\usepackage[font=small,labelfont=bf,skip=6pt]{caption}
\usepackage{enumitem}
\setlist{noitemsep,topsep=.35\baselineskip,leftmargin=*}
\usepackage{siunitx}                         % only if quantities with units occur
\usepackage{xurl}                            % only if long URLs occur in the bibliography
\usepackage[hidelinks]{hyperref}             % or muted colorlinks, see below
\usepackage[capitalise,noabbrev]{cleveref}
\emergencystretch=1em                        % last resort for stubborn lines
```

**`microtype` is the cheapest real improvement available.** It enables character
protrusion and font expansion, and under pdfTeX also interword-spacing and kerning
adjustment; the effect is a visibly more even grey texture and fewer overfull lines. One
line of preamble, no visible change to the design. If the document has a badly rivered
paragraph, try `\usepackage[protrusion=true,expansion=true,factor=1100]{microtype}`
before touching anything else.

**Links.** For print, `hidelinks`. For a screen preprint, one muted colour, never the
default fire-engine red and blue:

```latex
\usepackage{xcolor}
\definecolor{linkcol}{HTML}{1F4E79}
\hypersetup{colorlinks=true,allcolors=linkcol}
```

**Fonts** (only if `FONT CHANGE: allowed`; pdflatex-compatible, text and mathematics
matched, which is the part people get wrong):

- Libertinus: `\usepackage[lf]{libertinus}` with `\usepackage[libertinus,vvarbb]{newtxmath}`,
  or `\usepackage{libertinust1math}`. Warm, slightly bookish, excellent for long proofs.
- Times-alike: `\usepackage{newtxtext,newtxmath}`. Compact, conservative, matches most
  journal house styles.
- Doing nothing is a legitimate answer. Latin Modern with `microtype` is perfectly
  respectable and is never wrong.

Never change the text font without changing the mathematics font to match; a Palatino
page with Computer Modern integrals is worse than plain Computer Modern.

## TIER B. Local repairs

Apply mechanically wherever the symptom occurs. Each is a one-line diff.

### Text

| Symptom | Fix |
| --- | --- |
| `"straight quotes"` | `\enquote{...}` (or `` ``...'' ``) |
| `-` used for a range | `--` (en dash): `pp.~10--14`, `1990--2000` |
| `e.g. Alice`, `Prof. Smith` | `e.g.\ Alice`, `Prof.\ Smith` (kills the false sentence space) |
| sentence ending in a capital: `...in NP.` | `...in NP\@.` |
| `Lemma \ref{x}`, `see \cite{y}` | `Lemma~\ref{x}`, `see~\cite{y}`; better, `\cref{x}` |
| `\ldots` in prose | `\dots` |
| emphasis by `\underline` or bold | `\emph{...}` |
| `\bf \it \rm \tt \sf \sl \sc` | `\textbf \textit \textrm \texttt \textsf \textsl \textsc` |
| `\centerline{...}` | `\begin{center}...\end{center}` or `\centering` |
| manual `\\` at end of paragraph, stacked `\vspace` | delete; let TeX break the page |
| `\sloppy` document-wide | delete; use `\emergencystretch`, then fix the sentence |

### Mathematics

| Symptom | Fix |
| --- | --- |
| `$$...$$` | `\[...\]` |
| `eqnarray` | `align` / `aligned` (`eqnarray` has wrong spacing and is deprecated) |
| `\left( ... \right)` in inline math | `\bigl( ... \bigr)`: correct size, and the line can break |
| `\mathrm{Adv}`, `\text{Adv}` for an operator | `\DeclareMathOperator{\Adv}{Adv}` |
| `|x|`, `||x||`, `\{x | P(x)\}` | `\lvert x\rvert`, `\lVert x\rVert`, `\mid` |
| `\frac{a}{b}` inline | `a/b`, or `\tfrac` if unavoidable |
| display equation with no terminal punctuation | punctuate: a display is part of the sentence |
| `\mbox{if }` inside math | `\text{if }` |
| `x \in \mathcal{X}` where `\mathcal` is really a set of sets, etc. | leave alone; report only |
| `\cdots` / `\ldots` chosen by eye | `\dotsb`, `\dotsc`, `\dotsi`, `\dotsm` |

### Tables and floats

| Symptom | Fix |
| --- | --- |
| vertical rules `|` in the column spec | delete them, all of them |
| `\hline`, `\hline\hline` | `\toprule`, `\midrule`, `\bottomrule`; never mix with `\hline` |
| grouping shown by vertical rules | `\cmidrule(lr){2-4}` |
| numeric column misaligned on the decimal point | `siunitx` `S` column |
| caption below a table | captions go above tables, below figures |
| `\begin{center}` inside a float | `\centering` (avoids spurious vertical space) |
| `[h]` or `[h!]` placement | `[tbp]`; fighting the float algorithm always loses |
| `subfigure`, `psfig`, `epsfig`, `a4`, `doublespace` packages | `subcaption`, `graphicx`, `geometry`, `setspace` |

The rule against vertical and double rules is not a preference; it is the stated
philosophy of `booktabs` and reflects several centuries of practice in book work. The
package also inserts the correct amount of space above and below rules of differing
weight, which is what makes the tables look calm.

### Overfull boxes, in order of preference

1. Rewrite or reflow the sentence (report it to me, do not do it silently).
2. Add a hyphenation exception: `\hyphenation{pseudo-ran-dom}` or an inline `\-`.
3. `\emergencystretch=1em` in the preamble.
4. `\sloppypar` around the single offending paragraph.
5. Never `\sloppy` globally, never a negative `\hspace`, never shrink the font.

---

## SELF-CHECK BEFORE DELIVERING

- [ ] Does it compile, with no new errors or warnings?
- [ ] Did overfull-box count go down or stay level?
- [ ] Is the text font matched by the mathematics font?
- [ ] Would a reader notice anything other than that the pages read more easily? If yes,
      that change is too loud: revert it.
- [ ] Have I changed a single word of prose or a single symbol of mathematics without
      flagging it?
- [ ] Is every change I made traceable to an observed defect in *this* document?

## AUTHORITIES YOU MAY CITE IN THE REPORT

- R. Schlicht, *The microtype package* (user manual, `microtype.pdf` on CTAN).
- S. Fear, *Publication quality tables in LaTeX* (`booktabs.pdf` on CTAN).
- M. Downes and B. Beeton, *Short Math Guide for LaTeX*, AMS, v2.0 (2017).
- M. Trettin and J. Fenn, *An essential guide to LaTeX2e usage: obsolete commands and
  packages* (`l2tabu`, English translation, CTAN).
- M. Butterick, *Butterick's Practical Typography*, sections on line length, line
  spacing, and point size.
