# Contributing

Conjura has three content layers: **problems** (hubs, under `p/`), **statements**
(leaves, under `c/`), and **facets** (generated listing pages under
`open-problems/`, never hand-authored). See `/schema/` for the full frontmatter
contract; this file covers the editorial rules and the day-to-day workflow.

## Adding a new statement

1. Pick (or create) its hub under `p/<slug>/` -- see "Adding a new problem"
   below if none fits.
2. Find the next free id: the highest `c/<id>/` directory plus one, or check
   `conjura.json` after running `build_index.py`. Ids are sequential,
   zero-padded to four digits, allocated once, and never reused -- if a
   statement is later withdrawn, its id keeps a tombstone page rather than
   going back into a pool.
3. Copy `_templates/statement.qmd` and its sibling folders to `c/<id>/`, fill
   in every field (see `/schema/`), and write the statement, proof (if any),
   and Lean artifact (if any).
4. Run `python3 scripts/status_badge.py` to populate `statement_sha` and the
   badge, then `python3 scripts/build_index.py` and
   `python3 scripts/check_relations.py` to validate the schema and the
   relation graph. All three must exit 0 before you open a PR.

## Adding a new problem

Copy `_templates/problem.qmd` to `p/<slug>/index.qmd` and write the
motivation, provenance/history, and parameter lattice (the axes the family
varies along; mark cells nobody has stated yet as `unstated`, not blank --
an empty cell is a research prompt).

## Same id or a new one?

- **Same identifier, `revision` bump**: a change to wording, notation, or
  exposition only -- the truth conditions of the statement don't move.
  Record the diff in the commit message, not on the page -- there's no
  in-page changelog section; `git log -- c/<id>/` is the changelog.
- **New identifier**: a change to the truth conditions themselves (an added
  hypothesis, a changed quantifier order, a different parameter regime). The
  old page stays up, its `category` becomes `withdrawn`, it gets a
  `withdrawn_reason` and a `{kind: superseded-by, target: "<new id>"}`
  relation. Never delete it and never let its id 404.

`revision` and `statement_sha` are otherwise script-maintained: run
`scripts/status_badge.py` after any edit to the `## Statement` tab, and let
it force `statement_match` back to `open` and bump `revision` for you if the
hash no longer matches what's on disk -- that's the mechanism that stops a
formalization match from being silently invalidated by a later wording edit.

## Classifying a misformalization

When a revision's diff exists because a *formalization* was found to be
defective (not just re-worded), classify it in the commit message using the
Formal Conjectures misformalization taxonomy (Firsching et al.,
"Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in
Mathematics", arXiv:2605.13171):

- **Level** -- where the defect sits: `Translation` (the formal statement
  doesn't match the informal one), `Underspecified` (the informal statement
  itself left something unstated), or `Source` (the original source material
  was wrong or ambiguous).
- **Type** -- what kind of defect: `syntactic`, `semantic`,
  `misrepresentation`, `implicit conventions`, `reporting`, `mathematical`.

Write it as `misformalization: <level>/<type>` in the commit message, e.g.
`misformalization: Translation/semantic`. Check the paper directly if the
level/type distinction for a given case isn't obvious from this summary --
this file paraphrases it, and paraphrases drift.

## Areas are tags, not homes

The 19 area slugs (`foundations`, `idealized-models`, `impossibility-results`,
`symmetric-key`, `information-theoretic`, `side-channel`, `public-key`,
`lattices`, `isogenies`, `quantum`, `zk`, `proof-systems`,
`homomorphic-encryption`, `obfuscation`, `mpc`, `secret-sharing`,
`universal-composability`, `privacy`, `consensus`) are fixed. A statement can
list several; don't rename or merge a slug without updating both
`_quarto.yml`'s sidebar and `AREA_SLUGS` in `scripts/build_index.py` together,
in the same commit.

## Citations

Never write a specific author/venue/year citation into `sources:` (or into
prose) without having verified it's real. If you can't verify one, leave it
out and flag the gap instead of guessing.

## Style

No em-dashes in prose. Never hand-edit `status_badge:` -- it's always script
output. Keep changes reviewable: one logical change per commit.

## Local setup

```
pip install -r requirements.txt
git config core.hooksPath .githooks           # once per clone: run the checks pre-commit
python3 scripts/status_badge.py --self-test   # grading logic sanity check
python3 scripts/status_badge.py               # regenerate badges + statement_sha
python3 scripts/build_index.py                # validate schema, emit _generated/ + conjura.json
python3 scripts/check_relations.py            # validate the relation graph
python3 scripts/gen_interface.py              # regenerate the UC functionality boxes
quarto preview                                # facet listings need build_index.py to have run first
```

CI runs the same checks (`status_badge.py --check`, `build_index.py`,
`check_relations.py`, `gen_interface.py --check`) before `quarto render`; a
non-zero exit from any of them fails the build.

`.githooks/pre-commit` runs those same checks locally, on commits that touch
`c/`, `p/`, any `.qmd`, `scripts/`, `_templates/`, or
`surveys/uc-for-gamers/latex/`. Enable it with the `core.hooksPath` line above
-- it is worth the one command, because the checks gate the job *before*
`quarto render`: a single unregenerated `statement_sha` fails every push after
it, not just its own, and the site stops deploying until someone notices. If
PyYAML is missing the hook still runs the `status_badge.py` and
`gen_interface.py` gates (both stdlib-only) and reports that it skipped the
other two. Bypass a single commit with `git commit --no-verify`.

## UC functionality boxes

The interface box on a functionality's encyclopedia page is *generated*, not
written. Each functionality owns one file,

```
surveys/uc-for-gamers/latex/functionalities/<id>.tex
```

holding its `\begin{interface}` environment. `main.tex` `\input`s that file, and
`scripts/gen_interface.py` renders the same file to the `.cj-interface` block on
`uc/layer-N-.../<id>/index.qmd`. Edit the `.tex` and regenerate; never edit the
HTML block on the page, since the next run overwrites it. Everything *around*
the block -- the notation paragraph above it, the commentary below -- is
hand-written and left alone.

Line numbers are computed, not copied: the script runs the book's own
`\algcont`/`\algsave` counter, so inserting a line in the `.tex` renumbers the
rest of the box in the HTML exactly as it does in the PDF. That is what the
`--check` gate protects. Before this existed the numbers were hardcoded in
`<ol start="N">` and nothing noticed when they went stale.

That counter is reimplemented in Python, though, so `--check` only proves the
page agrees with the fragment, never that either agrees with the book. To
close that loop, run

```
python3 scripts/gen_interface.py --vs-pdf
```

which reads the numbers back out of `surveys/uc-for-gamers/pdf/main.pdf` and
compares. It is not a CI gate on purpose: it needs `pdftotext`, and it reads a
committed PDF that is only as current as its last rebuild, so a red result
there can mean the PDF is stale rather than the boxes wrong. Run it after
changing a fragment, and rebuild the book before believing a failure.

Notation macros are read from `surveys/uc-for-gamers/latex/ucgamers.sty`, so a
new `\newcommand` there is understood without touching the script -- unless its
expansion is not valid MathJax (`\op` is `\textsc`, which MathJax cannot set),
in which case it also needs an entry in the script's `MACRO_OVERRIDES`. Adding
one without the other is how a box silently stops rendering on the web.
`functionalities/preview.tex` compiles a single fragment on its own, which is
the check that a fragment depends on nothing outside the shared style file:

```
cd surveys/uc-for-gamers/latex
pdflatex -output-directory=/tmp "\def\FRAG{f-sig}\input{functionalities/preview}"
```
