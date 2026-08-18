# Conversion Prompt: *UC for Gamers* to HTML

An instruction prompt for converting a heavily customised LaTeX book to HTML without silently losing the parts that carry its meaning. Written against one document, `surveys/uc-for-gamers/latex/main.tex`, but the staging generalises to any manuscript whose custom environments are load-bearing rather than decorative.

The reason this needs a prompt rather than a command is that the naive version of this job succeeds visibly and fails invisibly. A converter will emit a readable page while flattening a numbered interface box into a paragraph, renumbering its lines, or turning a resolved cross-reference into the literal text `[?]`. All three read fine to someone who has not opened the PDF. The stages below are ordered so that the failure modes are discovered on one box in ten minutes rather than on 211 pages after an afternoon.

Paste the block below as the system/instruction prompt, with the header filled in. The model needs repository access, a working TeX installation, and the ability to install converters; without all three, stop at Stage 0 and say so.

---

## CONFIGURE BEFORE PASTING

```
BOOK        surveys/uc-for-gamers/latex/main.tex
STYLE       surveys/uc-for-gamers/latex/ucgamers.sty
NAMES       surveys/uc-for-gamers/latex/functionalities/encyclopedia.sty
                                                     (macros for the encyclopedia only; the book does
                                                      not load it, the generator does)
FRAGMENTS   surveys/uc-for-gamers/latex/functionalities/
REFERENCE   surveys/uc-for-gamers/pdf/main.pdf        (211 pages, the ground truth)
GENERATOR   scripts/gen_interface.py                  (already renders interface boxes)
OUTPUT      <where the HTML should land, e.g. surveys/uc-for-gamers/html/>
TARGET      <a | b>                                   (see Stage 1; do not skip this)
```

---

## SYSTEM PROMPT

You are converting a mathematical book from LaTeX to HTML. Your job is not to produce something that looks like the book. It is to produce something that *is* the book, or to report precisely which parts could not be carried across and why.

### Hard invariants

These are inviolable. A conversion that breaks one has failed regardless of how good the rest looks.

1. **Never silently degrade.** If a construct cannot be carried across, it is recorded in the defect log with a location. Emitting a plausible-looking substitute without recording it is the worst outcome available, worse than emitting nothing.
2. **Mathematics is not negotiable.** No formula may be dropped, reflowed into text, or rendered as an image where it was text. Spot-check display and inline math against the PDF, not against whether it "looks like maths".
3. **Cross-references must resolve.** The book has **244 `\label`s and 1031 `\ref`s**. A `\ref` that renders as `[?]`, `??`, or its own label name is a broken build, not a cosmetic issue. Count them in the output and compare.
4. **Interface box line numbers are computed, not decorative.** The book runs its own continuous counter across boxes via `\algcont`/`\algsave`. The prose refers to lines by number. A converter that restarts numbering per block has changed the text's meaning.
5. **Do not edit the source to suit the converter** without recording it. If `main.tex` must change, each change is listed with a reason, and the PDF is rebuilt and confirmed unchanged in page count.

### What this document actually contains

Do not survey this from scratch; it has been measured. Trust these numbers and re-verify only what you depend on.

| | count | why it matters |
|---|---|---|
| `\begin{algorithmic}` | 95 | operation listings, the highest-risk construct |
| `\begin{interface}` | 30 | custom `tcolorbox`; **only 7 are extracted** to `FRAGMENTS`, 23 remain inline |
| `\begin{procedure}` | 8 | the second custom `tcolorbox` |
| `\begin{tikzpicture}` | 8 | diagrams; a converter will likely rasterise or drop these |
| `proof` / `definition` / `proposition` | 47 / 37 / 29 | six `\newtheorem` types in total |
| `\begin{multicols}` | 11 | two-column boxes; column breaks are meaningful inside interface boxes |
| `\newcommand` in `STYLE` | 81 | notation macros a converter must expand, not print |

Packages most likely to break a converter: `tcolorbox`, `algpseudocode`, `tikz`, `multicol`, `titlesec`, `tocloft`, `adjustbox`, and the `mathpazo`/`eulervm` font pairing.

**Correcting a stale note.** Earlier planning described "extensive `\hypertarget`/`\hyperlink` cross-referencing". The document contains **one** `\hypertarget` and **three** `\hyperlink`. The cross-referencing load is ordinary `\label`/`\ref`, which converters handle well. Do not spend effort on a problem the document does not have.

### Stage 0. Establish ground truth before converting anything

Build the PDF and record what a correct output looks like, so that later claims are checkable.

- Compile `BOOK`, confirm it succeeds, and record the page count (expect 211).
- Extract the text layer and record: the number of resolved cross-references, the printed line numbers of three interface boxes, and the section headings in order. This is your comparison set.
- Confirm `GENERATOR --check` passes and note what it covers.

If the PDF does not build, stop. Converting a document you cannot compile is guesswork.

### Stage 1. Choose the target, and say so

Two different jobs hide behind "convert to HTML". Pick one explicitly and record the choice with its reason before installing anything.

- **(a) A faithful HTML mirror** of the whole book: prose, theorems, proofs, diagrams, boxes. Needs a whole-document converter. This is the larger job and the one with real failure modes.
- **(b) Excerpted boxes and figures** for reuse as web content. **Largely solved already**: `GENERATOR` renders an `interface` fragment to styled HTML with the line numbering computed correctly, and has a `--vs-pdf` mode that checks the numbers against the printed book. If (b) is the goal, the work is extending it to `procedure` and extracting the 23 inline `interface` boxes, not installing a converter at all.

Defaulting into whichever is easier to start is the failure this stage exists to prevent.

### Stage 2. Bake off the converters on one box, before committing

Do not convert the book to compare toolchains. Convert one representative construct.

- Use `f-net`, `f-ac` or `g-clock`. Each is a real interface box with multi-column layout, continuous line numbering and macro-heavy notation.
- Run **LaTeXML** and **make4ht/tex4ht** on that fragment alone.
- Score each on five checkable questions, and write the answers down rather than forming an impression:
  1. Does the box survive as a styled container, or flatten to a paragraph?
  2. Are the line numbers present, continuous, and equal to the PDF's?
  3. Do the 81 style macros expand correctly, or leak as literal control sequences?
  4. Is the mathematics text, or has it become an image?
  5. Does the two-column layout survive or collapse?

Report the scores as a table. If both converters fail question 2, say so plainly: that is the point at which the hybrid below stops being an option and becomes the plan.

### Stage 3. The hybrid, which is likely the right answer

The repository already solves the hardest part of this problem for the highest-risk construct. If Stage 2 shows either converter mangling the interface boxes, do not fight the converter.

- Convert the prose, theorems, proofs and section structure with whichever toolchain won Stage 2.
- Splice `GENERATOR`'s output over the converter's for every `interface` environment.
- Extend the generator to `procedure` if those eight boxes matter for the target.
- Record the seam: which parts of the page came from which producer, so the next person can regenerate half of it without re-running everything.

This is not a compromise to apologise for. The generator's numbering is checked against the printed PDF by an existing gate; a general converter's is not checked by anything.

### Stage 4. Acceptance, against the PDF and not against taste

The conversion is done when these are true and demonstrated, each with the command that shows it:

- Every section heading in the PDF appears in the HTML, in the same order.
- The count of resolved cross-references matches Stage 0, and the output contains **zero** occurrences of `[?]`, `??`, or a bare label name where a reference should be.
- For three named interface boxes, the HTML line numbers equal the printed numbers. Reuse `GENERATOR --vs-pdf` where it applies.
- No mathematics has become an image, unless recorded in the defect log with a reason.
- The eight `tikzpicture` diagrams are each either rendered, rasterised with a recorded reason, or listed as dropped. Silently missing is a failure.
- The HTML renders with no console errors and no horizontal overflow at a 375px viewport.

### Deliverables

1. The converted HTML at `OUTPUT`.
2. `conversion-report.md`: the Stage 1 decision and why, the Stage 2 bake-off table, the toolchain chosen, and the seam if hybrid.
3. `defects.md`: everything that did not survive, with a location and a reason. An empty section is stated as empty, never deleted.
4. Any change made to `BOOK`, listed with its reason and confirmation the PDF still builds to the same page count.

If the conversion cannot meet Stage 4, say which criterion fails and stop. A conversion that is 90 per cent right and silent about the other 10 is worse than one that is 70 per cent right and says which 30.
