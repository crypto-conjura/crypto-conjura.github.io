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

## Adding a new paper

Copy `_templates/paper.qmd` to `papers/<slug>/index.qmd`, create the
`latex/`, `pdf/` and `sessions/` folders beside it, and add the paper by
hand to the "## Papers" list in `papers/archive/index.qmd` -- that list is
written, not generated. Run `python3 scripts/status_badge.py` afterwards to
populate `statement_sha` and the badge. A paper carries no id, hub, areas
or relations, so `build_index.py` and `check_relations.py` do not apply.

## Rebuilding a generated artifact

Every `.tex` here has generated output committed beside it: the statement
PDFs under `c/<id>/pdf/`, the paper under `papers/uber-groups-rsr/`, and the
UC book's PDF and its 59-page HTML edition. `scripts/artifact_manifest.py`
records the hash of each artifact's inputs beside the hash of its outputs, and
`--check` fails when they diverge, in either direction: a source edited
without a rebuild, or a generated file edited by hand.

Editing generated output by hand is the failure worth naming. The next
rebuild destroys it silently, so the check exists to make that visible before
it happens rather than after it is lost.

When a `.tex` changes, rebuild the artifact and re-baseline:

```
scripts/build_uc_html.sh                          # for the UC edition, ~4 min
python3 scripts/artifact_manifest.py --update     # then record the new hashes
```

The check never builds anything. CI has no TeX, and `build_uc_html.sh` needs
TeX Live, `make4ht` and TeX Live's own `dvisvgm`, so it only ever reports that
a rebuild is owed.

For the UC book it watches what the book is actually built from, which is
narrower than the folder: `main.tex`, the `.cls` and `.sty` files beside it,
and only those `functionalities/*.tex` fragments `main.tex` `\input`s. The
other ninety-odd fragments are the encyclopedia's source, gated by
`gen_interface.py --check` instead, and counting them here would ask for a
rebuild every time an entry is filled in -- one that cannot change a page of
the book. The same reasoning keeps `functionalities/encyclopedia.sty` out:
it holds the names of the functionalities the book does not typeset, so it
is not a book input, whereas `ucgamers.sty` is and an edit to it still owes
a rebuild.

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

## Nothing under `c/` is ever deleted

The never-delete rule is absolute, and it covers every page under `c/`,
including `category: test` scaffolding. A page that has served its purpose is
**withdrawn**, never removed: set `category: withdrawn`, give it a
`withdrawn_reason`, and leave it in place. Its URL keeps resolving forever.

This is stricter than the rule that stood until 17 August 2026, which let a
`test` page be deleted outright on the grounds that scaffolding asserts
nothing. That carve-out is gone. The reason is that deletion is
indistinguishable, from outside, from a result being quietly disappeared, and
an archive whose case rests on keeping the record cannot afford a mechanism
for making pages vanish -- not even one reserved for pages that never claimed
anything. `c/0006` was deleted under the old rule on 2026-08-16, which is why
the ids skip it; that is the last such deletion.

Withdrawal delists rather than erases. `build_index.py` drops withdrawn
statements from every generated facet view, so a withdrawn page stops
appearing in area, form and model listings while its own page, and every link
and citation aiming at it, keeps working.

Two things hold whenever a page is withdrawn.

- **The id is retired, not recycled.** Allocating a new statement into a freed
  number would make an old link point at unrelated content, which is the
  failure the allocate-once rule exists to prevent.
- **A successor is recorded when there is one.** If the page is withdrawn
  because a new id replaced it, add `{kind: superseded-by, target: "<new
  id>"}`. A page withdrawn for any other reason needs no successor, and
  `withdrawn_reason` carries the explanation instead.

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

## Provenance tags

`tags:` is a second, optional list on a statement, and it answers a different
question from `areas:`. An area says what a statement is *about*; a tag says
where it came from. They are kept apart deliberately -- folding provenance
into the subject taxonomy would put an affiliation into the by-area browse,
where a reader looking for `consensus` would find it sitting beside them.

```yaml
tags: [iog]
```

The vocabulary is closed, held in `TAG_SLUGS` in `scripts/build_index.py`, for
the same reason `AREA_SLUGS` is: a free-text field grows typos and
near-synonyms, and nothing would catch `IOG` written against `iog`. Adding a
slug means editing `TAG_SLUGS` and adding a facet page under
`open-problems/tags/<slug>/`, copying an existing one.

One slug exists today.

**`iog`** -- a cited source has an author affiliated with
[Input Output Research](https://www.iog.io/papers). It renders as an outlined
`IOG` chip in the Tags column of every statement listing, linking to
[the tag page](/open-problems/tags/iog/), and pairs with the inline
[affiliation mark](#the-input-output-affiliation-mark) on the reference line
itself. The tag is the coarse, browsable signal; the mark says which reference
earned it.

It claims what the mark claims and no more: that an author is affiliated, not
that the paper was published, funded or endorsed by them, and nothing at all
about the statement -- which is this site's formalization of a question the
paper left open, not the paper's own work. Verify the affiliation before
adding the tag, under the citation rule above; an affiliation is a factual
claim about a real person.

Nothing derives the tag automatically. A statement citing an IO-affiliated
author needs both the tag and the mark added by hand.

## Before you open a public pull request or issue

Every route in this file is public, and that is almost always right. The one
exception is a result that breaks something deployed, weakens a parameter set
or standard real systems rely on, or attacks a named implementation. Those go
through [private vulnerability reporting](https://github.com/crypto-conjura/crypto-conjura.github.io/security/advisories/new)
first, not through a pull request or an issue, both of which are world-readable
the moment they exist.

Nearly nothing on this site is in that category: conjectures, lower bounds,
impossibility results and asymptotic statements in idealized models have
nothing deployed to attack. `SECURITY.md` at the repository root sets out the
scope, the timeline, and why an embargoed write-up cannot live on a branch here
at all.

## Write access and `main`

Nobody needs write access to contribute. Fork the repository, push a branch to
your fork, and open a pull request. The write role is granted only to
maintainers, and granting it is not what lets a change land.

`main` is protected by a branch ruleset: no direct pushes, no force-pushes, no
deletion, and every change arrives through a pull request whose `checks` job is
green. The ruleset is kept as JSON in `.github/rulesets/`, with the reasoning
for each rule beside it, rather than only in the settings UI. Check the live
repository against those files with `python3 scripts/rulesets.py --check`, which
needs read access only.

GitHub has no way to grant write access to one folder. Repository roles cover
the whole repository, and the one path-scoped rule GitHub offers is unavailable
on public repositories. So "you may edit `latex/` only" is a review convention
here, not something the platform enforces.

## Citations

Never write a specific author/venue/year citation into `sources:` (or into
prose) without having verified it's real. If you can't verify one, leave it
out and flag the gap instead of guessing.

### The Input Output affiliation mark

A cited paper with an author affiliated with [Input Output Research](https://www.iog.io/papers)
carries a small mark at the end of its reference line:

```html
<a class="cj-io" href="https://www.iog.io/papers"
   title="An author of this paper is affiliated with Input Output Research"
   aria-label="An author of this paper is affiliated with Input Output Research. Opens their publication list.">Input<span class="cj-io-bar"></span>Output</a>
```

Three rules, and they are about accuracy rather than taste.

**It marks an author, not a paper.** The claim it makes is only the one a
reference line can support: that somebody on the author list is affiliated
with IO. It does *not* say the paper was published, funded or endorsed by
them, and it must not be used to imply that. Where the two come apart --
a paper by an IO-affiliated author that IO's own publication list does not
carry -- the mark is still correct, because it is about the author.

**Verify the affiliation before adding it, the same way `sources:` entries are
verified.** An affiliation is a factual claim about a real person and belongs
under the rule above, not under style.

**It borrows a colour, not artwork.** The wordmark is set in the site's own
type, and the separator is a CSS rule rather than a glyph. That rule carries
IO's own red-orange, `$io-red: #ea3802`, sampled from the brightest pixel of
their 48px favicon -- their stylesheets expose no brand token, and the only
red in them belongs to a cookie-consent widget. The same rule leads the `IOG`
tag chip, so the two read as one family.

Do not go further and substitute their SVG or other brand assets. A colour on
a 2px rule is attribution; reproducing the mark would imply a relationship
that does not exist. The colour is used on rules and never on text, so it
carries no contrast requirement of its own.

Currently applied to: `c/0039` (Cojocaru, Kiayias, Shen, Wallden) and
`c/0040`/`c/0041` (Abram, Ball, Garay, Kiayias), all citing papers whose
author Aggelos Kiayias is Chief Scientist at Input Output. Nothing enforces
this -- it is a hand-applied convention, so a new statement citing an
IO-affiliated author needs the mark added by hand.

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

CI runs the same checks (`status_badge.py --check c papers`, `build_index.py`,
`check_relations.py`, `gen_interface.py --check`) before `quarto render`; a
non-zero exit from any of them fails the build.

The badge gate covers `c/` **and** `papers/`: a paper page carries the same
`status:`, `statement_sha`, and `status_badge` contract as a statement, so an
unregenerated paper badge is the same failure. Hubs under `p/` are exempt by
design (a hub has no badge of its own, only an aggregate over its children --
see `/schema/`). `c` and `papers` are also what bare `status_badge.py`
regenerates, so the gate and the fix cover the same set.

`.githooks/pre-commit` runs those same checks locally, on commits that touch
`c/`, `p/`, `papers/`, any `.qmd`, `scripts/`, `_templates/`, or
`surveys/uc-for-gamers/latex/`. Enable it with the `core.hooksPath` line above
-- it is worth the one command, because the checks gate the job *before*
`quarto render`: a single unregenerated `statement_sha` fails every push after
it, not just its own, and the site stops deploying until someone notices. If
PyYAML is missing the hook still runs the `status_badge.py` and
`gen_interface.py` gates (both stdlib-only) and reports that it skipped the
other two. Bypass a single commit with `git commit --no-verify`.

## Does a UC entry have a definition?

Every UC encyclopedia entry carries `definition:` in its frontmatter, and every
layer index shows it as a column beside `status:`. The two say different things
and both are needed: `status:` is how established the concept is, `definition:`
is whether this page actually contains one.

Three values, and like `status_badge:` the field is generated, so do not
hand-edit the first two:

- `"Defined"` and `"Not yet written"` are derived from whether the page carries
  a `.cj-interface` box. `scripts/uc_status.py` writes them and
  `--check` gates them in CI.
- `"No canonical definition"` is the exception, and the only value a human sets
  by hand. It records that the literature has none to transcribe, which is a
  result rather than a chore, and the script preserves it. Writing it on a page
  that does have a box is a contradiction and fails the check.

Run `python3 scripts/uc_status.py` after adding or filling an entry.

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

Notation macros are read from two files -- `ucgamers.sty` for the book's own
notation and `functionalities/encyclopedia.sty` for the names of the
functionalities the book does not typeset -- so a new `\newcommand` in either
is understood without touching the script, unless its expansion is not valid
MathJax (`\op` is `\textsc`, which MathJax cannot set), in which case it also
needs an entry in the script's `MACRO_OVERRIDES`. Adding one without the other
is how a box silently stops rendering on the web. A new functionality's name
belongs in the second file: the first is a watched book input, so putting it
there owes a rebuild the book cannot be changed by.
`functionalities/preview.tex` compiles a single fragment on its own, which is
the check that a fragment depends on nothing outside those two files:

```
cd surveys/uc-for-gamers/latex
pdflatex -output-directory=/tmp "\def\FRAG{f-sig}\input{functionalities/preview}"
```
