# Overnight run report

**Agent:** Claude Opus 5, running in Claude Code with edit/command auto-accept.
**Base commit:** `412ff63` on `main` ("Add prompts/source.md: fill one UC functionality stub end to end").
**Window:** 2026-08-16 02:01:32Z to 03:25Z, about 1 hour 24 minutes of the 8 hours budgeted.
**`main` untouched.** No pushes, no force-pushes, no history rewriting. Thirteen branches, all local.

Every task in the queue is closed. No task was checkpointed for running over
budget. T8, which was allotted "all remaining time", was stopped early on
judgement rather than on the clock; see its entry for why.

---

## Summary

| Task | Status | Branch |
|---|---|---|
| T0 baseline | not needed | -- |
| T1 CI gate beyond `c/` | **DONE** | `overnight/01-ci-gate` |
| T2 listing empty state | **DONE, premise corrected** | `overnight/02-listing-filter` |
| T3 `site-url` and social metadata | **DONE** | `overnight/03-site-url` |
| T4 README reconciliation | **DONE** | `overnight/04-readme` |
| T5 citation sweep | **DONE** | `overnight/05-citations` |
| T6 UC fragment pipeline | **ALREADY IMPLEMENTED; verified, and extended** | `overnight/06-uc-boxes` |
| T7 Lean statement for c/0004 | **DONE** | `overnight/07-lean-statement` |
| T8 Lean proof campaign | **PARTIAL (expected)** | `overnight/08-lean-proof` |
| T9a license draft | **DONE (draft)** | `overnight/09a-license-draft` |
| T9b c/0005 | **DONE (draft)** | `overnight/09b-c0005-secret-seed` |
| T9c c/0006 fork draft | **DONE (draft)** | `overnight/09c-c0006-ksource` |
| T9d blog restoration | **DONE (draft)** | `overnight/09d-blog-restore` |
| T10 integration | **DONE** | `overnight/10-integration` |

Integration: all twelve task branches merged into `overnight/10-integration`
in order, one conflict, resolved. 30 commits, 35 files, +2318/-64.

---

## Section 4: environment and baseline

| Step | Result |
|---|---|
| Quarto | 1.10.18, matching the pin in `publish.yml`. No install needed. |
| `latexmk` / `pdflatex` | present (`/opt/homebrew/bin`) |
| `elan` / `lake` / `lean` | present; `elan 4.1.2`, toolchains including `leanprover/lean4:v4.33.0` |
| `gh auth status` | authenticated as `farshim`, scopes `admin:public_key, gist, read:org, repo` |
| PyYAML | **not installed, and not installable as instructed** |

**FINDING (environment, not the repo).** `pip install -r requirements.txt`
fails twice over on this machine: `/usr/local/bin/pip` is a dead shim pointing
at a removed Python 2.7, and `python3 -m pip` refuses under PEP 668
("externally managed environment"). Per D1 I took the smallest reversible
option and built a virtualenv in the session scratchpad rather than passing
`--break-system-packages` against the user's system Python. Nothing in the
repository was changed for this. The operator may want a `venv` line in
`CONTRIBUTING.md`'s Local setup block; I did not add one, since it is a
property of this machine rather than of the project.

**Baseline on clean `main`, all four gates green** (the fourth, `gen_interface.py`,
is not in the prompt's list because it did not exist when the prompt was written):

```
$ python3 scripts/status_badge.py --check c
0 file(s) would be updated out of 8 scanned
$ python3 scripts/build_index.py
wrote conjura.json (8 statements) / wrote _generated/areas/ (19 files) / 8 leaf/leaves scanned, schema OK
$ python3 scripts/check_relations.py
8 leaf/leaves, relations consistent
$ python3 scripts/gen_interface.py --check
7 box(es) checked, 0 drifted
$ python3 scripts/status_badge.py --self-test
self-test OK: 228 constraint-valid tuples, monotone in every field
$ quarto render
Output created: _site/index.html          (exit 0)
```

Baseline was green, so no `overnight/00-baseline` task was created.

---

## T1. Extend the CI gate beyond `c/` -- DONE

**Branch** `overnight/01-ci-gate`, 2 commits:
`9a6aaf5` gate `papers/`; `4059d28` add `checks.yml`.

The badge gate now scans `c/` **and** `papers/`. The one non-obvious part:
`status_badge.py`'s no-argument default was `["c"]`, so gating `papers/` while
leaving the default alone would have printed a fix instruction that did not
fix anything. The default moved with the gate (`DEFAULT_ROOTS = ("c", "papers")`),
so `--check c papers` and bare `status_badge.py` cover the same set.

**Decision (D1).** `p/` hubs are exempt. A hub carries no badge, only an
aggregate over its children, so it has no `status:` block to grade. Pages
without one are skipped anyway, so naming the two roots explicitly is about
intent: adding a `status:` block to a hub should be a deliberate schema change.
Recorded in a new "What the badge gate scans" section of `schema/index.qmd`.

**Verification.** Staling the hashed `## Statement` block of
`papers/example-paper/index.qmd`:

```
$ python3 scripts/status_badge.py --check c            # old gate
0 file(s) would be updated out of 8 scanned            exit 0   <- misses it
$ python3 scripts/status_badge.py --check c papers     # new gate
STALE: papers/example-paper/index.qmd would be updated by scripts/status_badge.py
ERROR: 1 file(s) are stale                             exit 1   <- catches it
```

Staling reverted; `git diff --stat -- papers/` empty afterwards.

`checks.yml` runs the four Python gates plus `quarto render` on
`pull_request`, with `permissions: contents: read` only, no artifact upload
and no deploy job, so it cannot touch Pages. Validated with **actionlint
1.7.7** (downloaded to the scratchpad): clean on both workflows, exit 0.

---

## T2. Listing empty state -- DONE, but the premise was wrong

**Branch** `overnight/02-listing-filter`, 1 commit `58c78ea`.

**FINDING: the reported bug does not reproduce, and the prescribed fix is a
verified no-op.** The prompt describes "a populated table followed by a stray
'No matching items' line". What is actually emitted, on all 37 listing pages,
is `<div class="listing-no-matching d-none">`, and `.d-none{display:none!important}`
is present in the Bootstrap bundle those pages link. Headless Chrome
(`--dump-dom`, 8s virtual time) on `open-problems/all` after JS: class attribute
still `listing-no-matching d-none`. Quarto only un-hides that div from List.js's
`updated` event, which never fires on these pages because they carry
`sort-ui: false` and get no filter box.

I applied `filter-ui: false` to all 28 pages using `statement-table.ejs.md`,
rendered, and measured: **still 37 pages emitting the div, still 0 visible.**
The key changes nothing, because these pages already had no filter UI. I
reverted all 28 files rather than commit 28 no-op edits into facet
directories that R6 says should not be hand-authored.

**The real defect, which the same investigation surfaced.** 16 of the 28 facet
pages have no statements tagged to them, and each rendered as a table header
row with nothing under it and no explanation, because the message that exists
to explain exactly that is the one that never un-hides. Fixed in the shared
template `_listing-templates/statement-table.ejs.md` with an
`items.length === 0` branch, in the site's own voice ("Nobody has stated one
yet. An empty facet is a research prompt, not an error"), plus a
`.cj-listing-empty` rule in both themes.

Two incidental gotchas, now documented in the template for the next editor:
Quarto's engine is lodash templates, not full EJS, so `<%#` comments are a
syntax error; and a comment may not contain a closing tag delimiter, because
the scanner stops at the first one.

**Verification** on the freshly rendered `_site`: 16 empty facets now carry the
message, 12 populated tables unchanged (`open-problems/all` still lists its 8
rows), 0 header-only tables remain, no template comment leaks into the HTML,
`.cj-listing-empty` present in the emitted CSS, and headless Chrome confirms
the message is present after JS.

---

## T3. `site-url` and social metadata -- DONE

**Branch** `overnight/03-site-url`, 1 commit `046d810`.

Added `site-url`, `repo-url`, `open-graph: true`, `twitter-card: true` to
`website:`, and `canonical-url: true` to `format: html:`.

**Decision.** `canonical-url` is a format option, not a `website:` one (per
`/Applications/quarto/share/schema/document-links.yml:145`), but it is inert
until `site-url` exists, so the two belong in the same change. Without it,
`site-url` alone produced a sitemap but no canonical tags.

**Verification** (integration branch): `sitemap.xml` lists **174 URLs, all
absolute** on the site origin; **174 of 198** emitted HTML files carry a
canonical tag, none of them relative (the other 24 are redirect stubs and
library pages, which get none by design); `c/0004` resolves to
`https://crypto-conjura.github.io/c/0004/` and carries 3 `og:` and 3
`twitter:` tags.

**Noted, not worked around.** Quarto 1.10.18 emits no `og:url` and no
`og:image` even with `site-url` set. The absolute URL a crawler follows is the
canonical tag. Adding an `og:image` would want a real preview image, which is
a design decision, not a config one.

---

## T4. README reconciliation plus Actions badge -- DONE

**Branch** `overnight/04-readme`, 2 commits: `d10f1b8` layout and badge,
`1b728e5` em-dashes.

Layout block regenerated from `find` and `git ls-files`. Mechanically checked:
every path named in the block exists, and every tracked top-level directory is
named. `blog/posts/` removed, with one sentence on the removal consistent with
the dated comment in `_quarto.yml`. Added `surveys/`, `uc/`, `vision/`,
`philosophy/`, `latex/`, `scripts/`, `_listing-templates/`, `_generated/`,
`.githooks/`, `.github/`.

Also corrected against reality rather than intention:

- `resources/` was described as "not rendered on the site". It is rendered, and
  it is in the navbar.
- The local-development block listed three gate scripts and the prose said
  "three checks". There are four; `gen_interface.py` was missing.
- The per-folder convention omitted `lean/`, which `c/0001`-`c/0003` have.
- Six em-dashes, which `CONTRIBUTING.md`'s own style rule forbids.

**FINDING: `latex/README.md` says the folder is gitignored. It is not.** Its
first paragraph read "It's excluded from git (`/latex/` in `.gitignore`), so
nothing here ever reaches GitHub or the published site." There is no such rule
in `.gitignore`, `git check-ignore -v latex/papers/uber-groups-rsr` reports
NOT IGNORED, and all **144 files** under `latex/` are tracked and present on
`origin/main`, including `latex/papers/uber-groups-rsr/`.

I checked whether this was an accident before touching it: commit `4ace801`
("Track top-level latex/ drafts folder; ignore LaTeX build byproducts",
authored by Pooya Farshim) deliberately un-ignored the folder. So the tracking
is intended and the prose is stale, which is exactly the D2 case: the
configuration and the actual behaviour win, and the prose gets updated. The
paragraph now says the folder is tracked and public, and that what it is
excluded from is the *rendered site* (confirmed: `_site/latex` does not exist).

No content was un-tracked. If the operator did intend `latex/` to be private,
that is a decision for them, not for this run.

**Badge.** `[![Publish site](.../publish.yml/badge.svg?branch=main)](.../publish.yml)`.
Fetched 2026-08-16T02:19:25Z: the workflow page exists and is titled
"Publish site", lists 180 runs, head of `main` `412ff63`; the badge SVG returns
HTTP 200, `image/svg+xml`, 2294 bytes, `<title>Publish site - passing</title>`.

---

## T5. Citation surfacing and verification sweep -- DONE

**Branch** `overnight/05-citations`, 2 commits `d5b8e0d`, `70e9399`.

### Fetch log

Every citation added this run, and every one I was asked to check. All fetched
2026-08-16, between 02:20Z and 02:31Z.

| URL | Confirmed |
|---|---|
| `https://arxiv.org/abs/2602.10177` | **Feng et al., "Towards Autonomous Mathematics Research"**, submitted 10 Feb 2026. 28 authors, first Tony Feng, last Thang Luong. Abstract describes the *Aletheia* agent and an evaluation over the 700 open problems of Bloom's Erdős Conjectures database. **CONFIRMED.** |
| `https://arxiv.org/html/2602.10177v1` | Full text. The 6.5% figure is real and verbatim: "only 6.5% were meaningfully correct in addressing what we deemed to be the *intended* interpretation", with "137 (68.5%) of the responses were fundamentally flawed" and 50 more technically valid but vacuous, out of 200. **CONFIRMED**, but see the finding below on the section number. |
| `https://arxiv.org/abs/2605.20120` | **Gabriel Rongyang Lau, "Using Aristotle API for AI-Assisted Theorem Proving in Lean 4: A Formalisation Case Study of the Grasshopper Problem"**, submitted 19 May 2026. Abstract: four verified helper lemmas, but "the main theorem grasshopper closed directly by one unresolved sorry". **CONFIRMED** -- it resolves, the author is Lau as `solve.md` attributes, and the content is consistent with the sorry-trap claim. |
| `https://arxiv.org/abs/2605.13171` | **Firsching et al., "Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics"**, submitted 13 May 2026, first author Firsching. **CONFIRMED.** |
| `https://arxiv.org/html/2605.13171v1` | The misformalization taxonomy `CONTRIBUTING.md` paraphrases is real and accurate, in Section 3.3 and Appendix A.4: three levels (Translation, Underspecified, Source) and six types (syntactic, semantic, misrepresentation at translation; implicit conventions at underspecified; reporting, mathematical at source). **CONFIRMED** -- the paraphrase has not drifted. |
| `https://www.cambridge.org/core/books/abs/surveys-in-combinatorics-1989/...` | **McDiarmid, "On the method of bounded differences"**, *Surveys in Combinatorics, 1989*, ed. J. Siemons, pp. 148-188, Cambridge University Press, DOI `10.1017/CBO9781107359949.008`. Every field matches the `bibitem` in `c/0004/latex/proof.tex`. **CONFIRMED.** |
| `https://github.com/crypto-conjura/.../publish.yml` + badge SVG | see T4 |

**FINDING (minor, not edited).** `prompts/solve.md` cites the 6.5% figure as
arXiv:2602.10177 **Section 5.2**. In the v1 HTML it is **Section 4.2**.
`solve.md` is operator-authored, so per the task I did not edit it; the new
citation on `prompts/index.qmd` says 4.2.

### Edits

`prompts/index.qmd`: the 6.5% sentence now carries the reference inline, with
the breakdown (200 gradeable, 137 fundamentally flawed, 50 vacuous, 13 left).

`c/0004` `sources:` populated with the two entries that verify: the self-hosted
statement source, and McDiarmid. **`statement_sha` unchanged at `f1912b71`,
`revision` unchanged at 1** after running the script, confirming `sources:`
sits outside the hashed block as expected.

**Gap logged, not filled.** `c/0004/latex/main.tex` is 112 lines, carries no
bibliography and cites nothing, so it identifies no published antecedent for
the conjecture. Nothing was guessed to fill the gap.

### Link sweep

Over the rendered `_site` (integration branch): **198 pages, 13166 links**.

- **Internal: 2 broken targets**, both pre-existing and both on the paper
  template: `papers/example-paper/latex/main.tex` and `.../pdf/main.pdf`. Those
  directories contain only placeholder `README.md`s. Not introduced by this
  run, and arguably intentional for a template, so reported rather than
  changed. This run introduced no internal 404s.
- **External: 130 distinct URLs across 31 hosts. Zero dead.** A first pass
  flagged 11, all false positives: 7 `eprint.iacr.org` 429s (rate limiting;
  re-checked individually with delays, e.g. `eprint.iacr.org/2000/067` and
  `/2001/055` both return 200), and 4 ACM `doi.org` 403s (all four resolve,
  302, to `portal.acm.org`, which then blocks automated clients). No content
  file was edited on the strength of the sweep.

---

## T6. UC per-functionality fragment pipeline -- ALREADY IMPLEMENTED

**Branch** `overnight/06-uc-boxes`, 1 commit `4387dc3`.

**The repository moved between the prompt being written and this run.** Per D4
I trusted the tree. Stages (a) through (e) all already exist:

| Stage | State on `main` |
|---|---|
| (a) shared style file | `surveys/uc-for-gamers/latex/ucgamers.sty`, 195 lines |
| (b) per-functionality fragments | `functionalities/{f-ac,f-net,f-rand,f-sig,f-store,g-clock,g-pki}.tex`, `\input` by `main.tex` at lines 5873-7531 |
| (c) generator | `scripts/gen_interface.py`, 20 KB, reads macros from the `.sty` |
| (d) `--check` mode | present |
| (e) wired in | `publish.yml` and `.githooks/pre-commit` both run it |

`CONTRIBUTING.md` already documents the whole arrangement. The prompt's own
Facts block is superseded: the boxes are not "hand-written `.cj-interface`
HTML with hardcoded `<ol start="N">`" any more.

So T6 became verification of the stated acceptance criteria, all of which pass:

- **The book still compiles from the factored source.** `latexmk -pdf` exit 0,
  211 pages, no rerun warnings. The committed `pdf/main.pdf` is also 211 pages,
  so the factoring changed nothing.
- **Each fragment compiles standalone**, which is what proves it depends on
  nothing outside `ucgamers.sty`. All 7 via `functionalities/preview.tex`:
  `pdflatex` exit 0, 1 page each.
- **`--check` regenerates byte-identically**: `7 box(es) checked, 0 drifted`.
- **`--check` fails on a perturbed page**: injecting a spurious `<li>` into
  `f-sig`'s block produces a unified diff and exit 1. Reverted, tree clean.

**The new work: line numbers checked against the printed book.** `--check`
proves the page matches the fragment; it cannot prove either matches the PDF,
because the running `\algcont`/`\algsave` count is reimplemented in Python
rather than shared with LaTeX. If that reimplementation were wrong, page and
fragment would agree with each other and disagree with the book, and nothing
would say so. I added `gen_interface.py --vs-pdf`, which reads the `N:` labels
out of the compiled PDF's text layer:

```
f-rand    lines 1..10 (10) match PDF page 137, printed folio 136
f-store   lines 1..10 (10) match PDF page 141, printed folio 140
f-sig     lines 1..36 (36) match PDF page 147, printed folio 146
g-pki     lines 1..12 (12) match PDF page 153, printed folio 152
g-clock   lines 1..23 (23) match PDF page 160, printed folio 159
f-net     lines 1..20 (20) match PDF page 170, printed folio 169
f-ac      lines 1..17 (17) match PDF page 179, printed folio 178

7 box(es) checked against the PDF, 0 mismatched
```

Those are exactly the pages and folios the prompt's Facts block predicted.
**No page-versus-PDF discrepancy was found.**

Negative test: inserting one `\State` into `f-rand.tex` renumbers the box to
1..11 and `--vs-pdf` reports MISMATCH against the printed 1..10, exit 1.
Perturbation reverted.

**Decision.** `--vs-pdf` is deliberately **not** wired into CI. It needs
`pdftotext`, it reads a committed PDF that is only as fresh as its last
rebuild, and it leans on the text layer of a small-caps subscript. A false red
there would stop the site deploying for a reason unrelated to the site.
Documented as a local check in `CONTRIBUTING.md`.

---

## T7. Lean statement for c/0004 -- DONE

**Branch** `overnight/07-lean-statement`, 1 commit `0fc65ed`.

Lake project at `c/0004/lean/`, **Mathlib `v4.33.0`, revision
`db584cd6d46c92f209a44c0f1c829460d327499d`**, toolchain
`leanprover/lean4:v4.33.0`. `.lake/` (7.4 GB) is gitignored;
`lake-manifest.json` and `lean-toolchain` are committed, so the build
reconstructs exactly.

**Nothing is `opaque`.** Finite sets as `Fintype`s, the oracle as
`PMF.uniformOfFintype (K × D → R)`, both games written out, `PMF` for all
randomness, advantages in `ℝ`. Unbounded adversaries are modelled as arbitrary
functions of the whole table, which is exactly what unbounded means and needs
no complexity class. `c` is bound outermost, ahead of the types and of
epsilon.

**One deliberate choice worth the operator's eye.** `Z`, the
auxiliary-information alphabet, carries no `Fintype` and no `DecidableEq`. The
informal statement never says what `z` ranges over, and nothing in the file
needs it finite, so leaving it arbitrary is the weaker assumption and the
safer translation.

**Done-means, met.**

```
$ lake build
warning: Statement.lean:122:8: declaration uses `sorry`
Build completed successfully (2597 jobs).          # exactly one sorry, the conjecture
$ lake env lean Audit.lean
'Conjura0004.lhl_public_seed'                depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
'Conjura0004.predAdv_nonneg'                 depends on axioms: [propext, Classical.choice, Quot.sound]
'Conjura0004.predAdv_le_one'                 depends on axioms: [propext, Classical.choice, Quot.sound]
'Conjura0004.predAdv_mem_unitInterval'       depends on axioms: [propext, Classical.choice, Quot.sound]
'Conjura0004.extAdv_le_one'                  depends on axioms: [propext, Classical.choice, Quot.sound]
'Conjura0004.neg_one_le_extAdv'              depends on axioms: [propext, Classical.choice, Quot.sound]
'Conjura0004.extAdv_eq_zero_of_subsingleton' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Six sanity lemmas, `sorry`-free. The load-bearing one is
`extAdv_eq_zero_of_subsingleton`: when the output set is a singleton the
extraction advantage is exactly `0`, which fails for several plausible ways of
getting the game wrong.

`MATCH.md` maps every quantifier, game line, advantage and constant to its Lean
name, and records five judgement calls. It is explicit about what the sanity
lemmas do **not** pin down: the `b = false` / `b = true` challenge convention
stays provable either way round under `Subsingleton R`, so it is held only by
the definition and its docstring.

Badges regenerated by script only: ring `cj-ring-1` (dotted) to `cj-ring-3`
with `stroke-dasharray='5,3'` (the dashed AI-matched style); disc unchanged at
`cj-disc-1`. `statement_sha` unchanged at `f1912b71`, `revision` still 1,
because the Statement tab itself did not move. `build_index.py` and
`check_relations.py` both pass on the new `lean:` block.

Per R3 the fields are `statement_formal: ai` and `statement_match: ai`. Neither
is a field an AI may set to `human`.

---

## T8. Lean proof campaign -- PARTIAL (the expected outcome)

**Branch** `overnight/08-lean-proof`, 5 commits, ratcheted: every lemma
committed the moment it compiled `sorry`-free. No proved lemma was deleted.
`c/0004/lean/LEDGER.md` is the running account.

### The Mathlib audit, done first

This is the most reusable finding of the run.

| Sought | Present in Mathlib v4.33.0 |
|---|---|
| McDiarmid / bounded differences | **absent** (zero occurrences of `McDiarmid`) |
| Azuma-Hoeffding | present, but only in the measure-theoretic martingale setting |
| Statistical / total variation distance on a `PMF` | **absent** (`totalVariation` is only for vector and signed measures) |
| Chebyshev, Bernstein, Chernoff | present in various forms, none the bounded-differences statement |

So **two of the seven "standard facts" the informal proof borrows from outside
itself are not borrowable**, and have to be built: Fact 2.1 (statistical
distance as optimal advantage) and Fact 2.2 (McDiarmid). Using the
measure-theoretic Azuma would mean dragging the filtration apparatus into a
setting that is finite in every direction.

### Proved, `sorry`-free

`Proof.lean` is warning-free and contains **zero** `sorry`s. Sixteen
declarations, `#print axioms` reporting only `propext`, `Classical.choice`,
`Quot.sound` for every one (grep for `sorryAx` in the audit output: 0 hits).

1. **Statistical distance** on a finite type as half the l1 distance, in `ℝ`,
   with `SD_nonneg`, `SD_le_one`, `SD_comm`, `SD_self`, and the identity
   `sum_pos_part_eq_SD` that the next step turns on.
2. **Fact 2.1, in full.** `distAdv_le_SD`: no unbounded, randomized
   distinguisher beats the statistical distance. `distAdv_mapTest`: the
   maximum-a-posteriori test attains it. `isGreatest_distAdv` packages the two,
   which matches how the informal proof states it, with a maximum rather than
   a supremum.
3. **The bridge, Lemma 3.1's first half.** `extGame_eq_distGame` shows the
   extraction game *is* a distinguishing game between the two laws the view has
   under the two challenge bits; the only work is walking the challenge bit from
   last to first through four `PMF.bind_comm`s. Then `extAdv_le_SD_views` and
   `extAdv_mapDist` give `isGreatest_extAdv`: the best extraction advantage
   **is** the view distance.
4. **The predictor bound**, Lemma 3.1's other half: `predAdv_le_maxMass`.

Why this and not the mathematics above it: `Statement.lean` defines the
advantage operationally, as a game, and every later step of the informal proof
works with an analytic quantity. Nothing above the bridge can be formalized
until the bridge exists, and Mathlib supplies neither end of it.

### One restriction, recorded not hidden

The bridge section assumes `[Fintype Z]`, which the conjecture does not,
because `SD` is a `Finset` sum and the view carries `z`. `Statement.lean`
deliberately leaves `Z` arbitrary. Removing this means redoing the statistical
distance with `tsum`; it is item 1 of the outstanding list.

### Honesty

**`proof_formal` stays `open`.** `lhl_public_seed` is untouched and still a
`sorry`. A ledger of progress is not a proof. The badge did not move.

`LEDGER.md` lists eight outstanding obligations in dependency order and is
blunt that items 4-8 are the mathematics, with the finite bounded-differences
inequality a project in itself.

### Why T8 stopped early rather than running to the clock

T8 was allotted all remaining time to a hard stop. It had roughly five and a
half hours left when I stopped. The judgement, under "when in doubt between
doing less verifiably and more speculatively, do less, verifiably": the next
items are the flattening lemma, the mean at a fixed support, and a
from-scratch finite McDiarmid. Each is a multi-hour formalization with real
risk of ending as a half-written `sorry` scaffold, which is worth less to a
reviewer than a smaller closed result plus an accurate ledger. What is
committed is a coherent, complete, self-contained layer with nothing
outstanding inside it. If the operator would rather have speculative scaffolds
for the remaining lemmas, that is a cheap follow-up from this branch.

---

## T9a. License draft -- DONE (draft)

**Branch** `overnight/09a-license-draft`, 1 commit `d890d70`.

`LICENSE-CODE` (MIT, "Copyright (c) 2026 the Conjura contributors") and
`LICENSE-CONTENT` (CC BY 4.0), plus a Licensing section in README scoping each.
Lean artifacts are scoped as code.

**Marked as a draft, not in force, on purpose.** The README says so in its
first line, and no per-page footer notices were added.

**This one needs the operator before it can merge.** The last section of
`LICENSE-CONTENT` says it: imported `.tex` and PDFs under `c/*/latex/`,
`papers/*/latex/`, `surveys/*/latex/` and `latex/` came from co-authored and
published work and may carry third-party rights the Conjura contributors
cannot relicense. Nothing in this run can settle that.

---

## T9b. c/0005, the secret-seed variant -- DONE (draft)

**Branch** `overnight/09b-c0005-secret-seed`, 1 commit `4a8f6d5`.

The id sequence ran 0001-0004, 0006-0009. `c/0005/` existed on disk as an empty
reserved directory (untracked, holding only `.DS_Store` and an empty
`sessions/`), so the hole was real.

Filled with the statement already sitting unclaimed: `c/0004`'s own source
document states two conjectures, and only the public-seed one was tracked.
Conjecture 1, the secret-seed variant, was described on the hub page as "not
tracked". Transcribed from the same PDF, which is copied into `c/0005/latex`
and `c/0005/pdf` on the c/0004 layout.

Relation `{kind: variant-of, target: "0004"}` -- same setting, same source,
same prediction game, differing only in whether the distinguisher receives the
seed. `category: research-open`. `proof_informal: open`; no proof is claimed,
and the Proof tab says the c/0004 note takes this conjecture as its foil rather
than proving it.

Per **R3**, `statement_informal: ai`. The transcription is from the operator's
own source document, so this is a field the operator may legitimately flip to
`human` after checking it against `latex/main.tex` Conjecture 1. The page's
first open obligation says exactly that.

The hub's parameter lattice moves the single-source secret-seed cell from *not
tracked* to c/0005. All three scripts green: 9 leaves, schema OK, relations
consistent.

---

## T9c. c/0006 upgrade draft -- DONE (draft)

**Branch** `overnight/09c-c0006-ksource`, 1 commit `467a85c`.

The page quietly assumed one reading of "k-source extraction". It now states
**two** candidate formalizations side by side and picks neither; `category`
stays `test`.

- **Fork A**: `k` independent sources, each epsilon-unpredictable.
- **Fork B**: one source emitting a jointly unpredictable tuple, coordinates
  allowed to correlate.

Both measured against the same baseline, the `k`-fold hybrid, which costs a
factor `k` and at `k=1` is exactly c/0004's corollary (so the existing
`generalizes`/`specializes` pair with c/0004 stays consistent).

**FINDING: Fork B in its naive form is false, with an explicit witness.** Take
`k = 2`, `x₁` uniform on `𝒟`, `x₂ = d₀` fixed, `z = ⊥`. The best predictor
guesses `(d, d₀)` and wins exactly when it guesses `x₁`, so the tuple is
`(1/D)`-unpredictable. But the distinguisher holds `H` and `sd₂`, so it
recomputes `H(sd₂, d₀)` and gets advantage exactly `1 - 1/R`. Fixing `R` and
sending `D, K → ∞` drives any bound of the conjectured shape to zero while the
advantage does not move, so no universal constant survives. A tuple can be hard
to guess whole while one coordinate carries no entropy, and one dead coordinate
is enough.

Checked numerically as well as analytically: simulating the attack at
`K=8, D=64, R=16, k=2` over 400k trials gives `Pr[b'=b] = 0.96948`, advantage
`0.93895`, against the predicted `1 - 1/(2R) = 0.96875` and `1 - 1/R = 0.9375`.
At `D = 2^40, K = 2^20` the conjectured RHS at `c=1` is `0.0087` while the
advantage is still `0.9375`.

Fork B is therefore stated in a repaired form, with conditional per-coordinate
unpredictability.

**Second finding, on the bound shape.** The page now says that the `√k`
improvement is a guess and not a corollary. Generic Hellinger tensorization
gives `SD(P^⊗k, Q^⊗k) ≤ √(2k · SD(P,Q))`, which is `√(kδ)` and therefore
*worse* than the hybrid's `kδ` unless `δ` is already small. Reaching `√k · δ`
needs `H² = O(δ²)` for this particular pair, which is a claim about how
c/0004's bound is attained.

Generated fields by script only: `revision` 2 to 3, `statement_sha` rewritten,
`statement_match` held at `open`.

**Small inconsistency reported, not changed:** `c/0006` carries
`form: lower-bound`, but both forks state an upper bound on advantage, as
c/0004 does with `form: tight-bound`. Changing it is a taxonomy call for the
operator; it is on the page's obligation list.

---

## T9d. Blog restoration -- DONE (draft)

**Branch** `overnight/09d-blog-restore`, based on `overnight/03-site-url`
(the feed needs `site-url` to build absolute URLs), 1 commit `9fd8551`.

`blog/index.qmd` as a listing with `feed: true`, and one post,
`blog/posts/public-seed-costs-a-factor-of-k.qmd`, explaining c/0004: why the
obvious guess is false, and what the correction costs. Blog restored to both
navbar and sidebar, with the dated `_quarto.yml` comment updated to record what
happened rather than what was planned.

**The post opens with the honesty box the task specified**: AI-written, about a
proof that is itself an AI draft no human has independently reviewed, pi = 1 on
the badge scale, with a link to the status legend. Its closing section says
which two things would move the badge and notes that neither is something an AI
can do for itself.

**The numbers in the post were checked, not repeated.** Simulating the
image-membership distinguisher at `D = R = 64, 256, 1024` gives advantages
`0.354, 0.360, 0.369` against the predicted miss fraction `(1-1/R)^D → 1/e =
0.368`, which is the "37%" and the "at least 1/4" the post claims. The best
constant this route gives, `(6/5)√(1 + ln 2)`, is `1.5615` as stated.

**Verification.** `_site/blog/index.xml` parses as well-formed RSS
(`ElementTree`, no exception), one item, channel link and item link both
absolute on the site origin. Navbar and sidebar both list Open Problems,
Papers, Surveys, Resources, Blog, UC Encyclopedia, in that same order. (The
home page carries no sidebar at all, which is pre-existing full-width layout,
not a regression.)

---

## T10. Integration -- DONE

**Branch** `overnight/10-integration`, base `412ff63`, all twelve task branches
merged in order T1 through T9d. 30 commits, 35 files, +2318/-64.

**One conflict**, in `c/0004/index.qmd`: T5 added `sources:` where T7 replaced
the adjacent `lean:` block. Both wanted; resolved by keeping both. Re-ran
`status_badge.py`: `statement_sha` still `f1912b71`, `revision` still 1.

No other integration breakage. Nothing was fixed beyond the conflict itself.

**Final state of the integration branch:**

```
$ python3 scripts/status_badge.py --check c papers
0 file(s) would be updated out of 12 scanned
$ python3 scripts/build_index.py
wrote conjura.json (9 statements) / wrote _generated/areas/ (19 files) / 9 leaf/leaves scanned, schema OK
$ python3 scripts/check_relations.py
9 leaf/leaves, relations consistent
$ python3 scripts/gen_interface.py --check
7 box(es) checked, 0 drifted
$ python3 scripts/gen_interface.py --vs-pdf
7 box(es) checked against the PDF, 0 mismatched
$ quarto render
Output created: _site/index.html          (exit 0, 0 errors, 64s)
$ lake build   (in c/0004/lean)
warning: Statement.lean:122:8: declaration uses `sorry`
Build completed successfully (2599 jobs).
```

Cross-checks on the integrated render: 16 empty facets carry a message, 0
header-only tables; sitemap 174 URLs all absolute, 174 pages with canonical, 0
relative; c/0005 renders; c/0006 shows both forks; the blog feed is
well-formed with 1 item; c/0004 links `Proof.lean` and `LEDGER.md` and shows
ring 3 / disc 1. Internal links: the same 2 pre-existing template placeholders,
nothing new. `_site` is 19 MB and the 7.4 GB `.lake` tree did not leak into it.

---

## Pull requests

`gh` was authenticated, so per R1 a draft PR was opened per branch, labeled
`overnight`. All eleven are **drafts**, so none can be merged by accident.

| PR | Branch | Base |
|---|---|---|
| [#1](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/1) | `overnight/02-listing-filter` | `main` |
| [#2](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/2) | `overnight/03-site-url` | `main` |
| [#3](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/3) | `overnight/04-readme` | `main` |
| [#4](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/4) | `overnight/05-citations` | `main` |
| [#5](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/5) | `overnight/06-uc-boxes` | `main` |
| [#6](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/6) | `overnight/07-lean-statement` | `main` |
| [#7](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/7) | `overnight/08-lean-proof` | `overnight/07-lean-statement` |
| [#8](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/8) | `overnight/09a-license-draft` | `main` |
| [#9](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/9) | `overnight/09b-c0005-secret-seed` | `main` |
| [#10](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/10) | `overnight/09c-c0006-ksource` | `main` |
| [#11](https://github.com/crypto-conjura/crypto-conjura.github.io/pull/11) | `overnight/09d-blog-restore` | `overnight/03-site-url` |

An `overnight` label was created for this (the repository had no such label).

### BLOCKED: two branches could not be pushed, so have no PR

`overnight/01-ci-gate` and `overnight/10-integration` were **rejected by
GitHub**:

```
! [remote rejected] overnight/01-ci-gate -> overnight/01-ci-gate
  (refusing to allow an OAuth App to create or update workflow
   `.github/workflows/checks.yml` without `workflow` scope)
```

The authenticated token carries `admin:public_key, gist, read:org, repo` and
**not `workflow`**, so any branch touching `.github/workflows/` is refused.
`overnight/10-integration` contains T1, so it is refused for the same reason.

I did not widen the token, re-authenticate, or change any repository setting:
R7 puts credentialed and settings actions out of scope, and a scope change is
not something to do to someone's account while they are asleep.

**Both branches exist locally and are complete**, with all gates green. To get
them up:

```
gh auth refresh -h github.com -s workflow      # then re-run:
git push -u origin overnight/01-ci-gate
git push -u origin overnight/10-integration
```

Or apply T1 by hand: it is two files of workflow change plus
`scripts/status_badge.py`, `CONTRIBUTING.md` and `schema/index.qmd`.

A consequence worth noting: `checks.yml` is what would have given these PRs
CI. Since it could not be pushed, **the eleven open PRs have no CI running
against them**. Everything in this report was verified locally instead, and
the commands are quoted so you can re-run them.

---

## Decisions taken under Section 2

| # | Decision | Rule |
|---|---|---|
| 1 | Built a scratchpad virtualenv for PyYAML rather than `--break-system-packages` against the system Python | D1 |
| 2 | `p/` hubs exempt from the badge gate; documented in `schema/` rather than left implicit | D1 |
| 3 | Moved `status_badge.py`'s default roots with the gate, so the fix instruction covers what the gate checks | D1 |
| 4 | Reverted the prescribed `filter-ui: false` after measuring it as a no-op, and fixed the defect the evidence actually showed | D1, D3 |
| 5 | `canonical-url` placed in `format: html:` (where its schema puts it) rather than `website:` | D2 |
| 6 | `latex/README.md` prose updated to match the tracked-and-public reality; no content un-tracked | D2 |
| 7 | Trusted the working tree over the prompt's Facts block for T6, which was superseded | D4 |
| 8 | `--vs-pdf` kept out of CI to avoid a false red stopping the deploy | D1 |
| 9 | `Z` left an arbitrary type in the Lean statement, since the informal statement constrains it not at all | D1 |
| 10 | Added McDiarmid to c/0004 `sources:` (verified, and cited by `proof.tex`) but nothing for the statement's antecedent, which does not exist in the source | R4 |
| 11 | T9 executed before T8 | D5 |
| 12 | T8 stopped on judgement with time remaining, rather than starting a lemma likely to end half-written | stated above |

## Findings, collected

1. **Environment:** `pip` is broken on this machine two different ways; PyYAML needs a venv.
2. **T2:** the reported "No matching items" leak does not reproduce; `filter-ui: false` is a measured no-op; the real defect was 16 facet pages rendering an unexplained empty table.
3. **T4:** `latex/README.md` claimed the folder is gitignored; 144 files under it are tracked and public. Deliberate per `4ace801`; prose was stale.
4. **T4:** README's `resources/` description, gate count, and `lean/` omission were all wrong; six em-dashes against the repo's own style rule.
5. **T5:** arXiv:2605.20120 **CONFIRMED** real (Lau, Grasshopper/Aristotle, 19 May 2026) and consistent with the sorry-trap attribution.
6. **T5:** `prompts/solve.md` cites Section 5.2 for the 6.5% figure; it is Section 4.2. Operator-authored, not edited.
7. **T5:** `c/0004/latex/main.tex` has no bibliography, so no published antecedent exists to cite. Gap logged, not filled.
8. **T5:** zero dead external links out of 130; the 11 initial flags were rate limiting and ACM bot protection.
9. **T6:** no UC page-versus-PDF discrepancy. All seven boxes match the printed book on exactly the predicted pages.
10. **T8:** Mathlib v4.33.0 has no McDiarmid, no bounded-differences inequality, and no statistical distance on a `PMF`. Two of the informal proof's seven borrowed facts must be built from scratch.
11. **T9c:** the jointly-unpredictable-tuple version of the k-source conjecture is **false** in its naive form, with an explicit witness, verified numerically.
12. **T9c:** the `√k` bound shape is a guess; generic Hellinger tensorization gives only `√(kδ)`.
13. **T9c:** `c/0006` carries `form: lower-bound` while stating an upper bound.
14. **Pre-existing:** two broken internal links on the paper template.
15. **Credentials:** the `gh` token lacks the `workflow` scope, so the two branches touching `.github/workflows/` could not be pushed and have no PR. Not worked around; see the Pull requests section.

---

# Morning checklist

### Recommended merge order

Independent, merge in any order, lowest risk first:

1. `overnight/03-site-url` -- config only, biggest visible win.
2. `overnight/02-listing-filter` -- template plus two SCSS blocks.
3. `overnight/04-readme` -- docs only.
4. `overnight/01-ci-gate` -- gate widening plus the new `checks.yml`.
   **Local only: push blocked for lack of the `workflow` token scope.** Merge
   it before the content branches if you want them checked by CI.
5. `overnight/06-uc-boxes` -- adds `--vs-pdf`, changes no output.
6. `overnight/05-citations` -- one prose citation, one `sources:` block.

Then, in this order because they build on each other:

7. `overnight/07-lean-statement`, then `overnight/08-lean-proof` (contains 07).
8. `overnight/09b-c0005-secret-seed`, `overnight/09c-c0006-ksource`.
9. `overnight/09d-blog-restore` (contains 03).

Hold until you have decided:

10. `overnight/09a-license-draft` -- **needs your confirmation**, see below.

Or merge `overnight/10-integration` and get all of it at once; it is already
conflict-resolved, gates green, renders clean. It is "merge last", and it is
**local only** for the same token-scope reason.

### What needs a human, by design

These are constitutive human acts under the site's badge semantics. No AI run
can do them, and this one did not try.

- [ ] **Independent human review of the c/0004 informal proof.** This is what
      moves pi from 1 to 2. The proof is at `c/0004/pdf/proof.pdf`.
- [ ] **Human match check of `c/0004/lean/Statement.lean`** against the
      Statement tab, which moves sigma from 3 to 4. `MATCH.md` is the AI
      version and is written to be checked rather than trusted. Two places to
      look first: the quantifier order on `c` (it must be outermost), and the
      `b = false` / `b = true` challenge convention, which the sanity lemmas
      deliberately do **not** pin down.
- [ ] **Supply the c/0004 `sessions/` transcript.** Left empty; per R5 I did
      not fabricate one. This run's own provenance is this report.

### Decisions only you can make

- [ ] **T9a licensing.** Confirm whether the Conjura contributors can license
      the imported LaTeX under `c/*/latex/`, `papers/*/latex/`,
      `surveys/*/latex/` and `latex/`, or whether those need carving out. The
      draft is written to be safe either way but says "not in force" until you
      say so.
- [ ] **T9c fork choice.** Fork A (independent sources) or Fork B repaired
      (conditional per-coordinate unpredictability). They are different
      theorems; c/0006 cannot carry both. Whichever loses is dropped or minted
      as its own id.
- [ ] **c/0005 `statement_informal`.** Currently `ai` per R3. If you check the
      transcription against `c/0005/latex/main.tex` Conjecture 1 and are
      satisfied it is faithful to your own source, this is legitimately
      `human`.
- [ ] **`latex/` visibility.** It is tracked and public, deliberately per
      `4ace801`. I only fixed the README that said otherwise. Worth a
      deliberate second look given `latex/papers/uber-groups-rsr/` is in there.
- [ ] **`c/0006` `form:`** is `lower-bound` but the page states an upper bound.
- [ ] **`prompts/solve.md`** cites Section 5.2 for the 6.5% figure; it is 4.2.
      Yours to edit.

### Housekeeping

- [ ] **Push the two blocked branches.** `gh auth refresh -h github.com -s workflow`,
      then push `overnight/01-ci-gate` and `overnight/10-integration`. Until
      then the eleven open PRs have no CI, because `checks.yml` lives on the
      branch that could not be pushed.
- [ ] Close the draft PRs you do not want; they are all drafts, so nothing can
      merge itself.

### Red baseline findings

None. All four gates and a full render were green on clean `main` at
`412ff63`, and are green on the integration branch. The only baseline problem
was local tooling (`pip`), not the repository.
