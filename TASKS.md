# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~12.25h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `8937c1f` on 16 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

- [ ] **Remove the Example Paper page (~0.25h)**

  Delete `/papers/example-paper/`: `index.qmd` plus three subfolders (`latex/`, `pdf/`, `sessions/`) that contain nothing but a `README.md` each.

  **Decide what happens to the template first, because that page is not dead weight.** It is the live contract a new paper is copied from: the full `status:` block, `reviewers: []`, `status_summary`, `status_updated`, `revision`, `statement_sha` and the generated `status_badge`, with a callout telling the copier which fields to fill and which note to delete. `_templates/` holds only `problem.qmd` and `statement.qmd`, so deleting this folder leaves the repo with no paper template at all. Three options: delete outright and let `papers/uber-groups-rsr/` serve as the exemplar; move it to `_templates/paper.qmd`, which puts it beside its two siblings and out of the rendered site; or delete it and fold the frontmatter contract into `CONTRIBUTING.md`. Moving it to `_templates/` is the recommendation, since the page's own callout already calls it a template page and `_templates/` is where the other two contracts live.

  Five inbound references break on deletion and none of them is a Quarto listing, so all five are hand edits:

  - `papers/index.qmd:17` — a "Browse" bullet.
  - `papers/archive/index.qmd:28` — an entire "## Not papers" section that exists only to explain why this page is not in the archive list. Delete the section, not just the link.
  - `papers/programme-committee/index.qmd:22` — "see the [paper template]", load-bearing for the sentence about how `reviewers` accumulates. Needs a replacement target, not just link removal.
  - `README.md:42` — names it as a starting template alongside `_templates/statement.qmd` and `_templates/problem.qmd`.
  - `latex/README.md:59`.

  Two things not to get wrong:

  - Re-run `python3 scripts/status_badge.py`, `build_index.py` and `check_relations.py` after the deletion and commit their output. All three gate the deploy ahead of `quarto render`, and a stale index entry pointing at a removed folder fails every subsequent push by anyone, with the failure blaming an innocent commit.
  - `papers/example-paper/sessions/README.md` is the only non-empty `sessions/` directory in the repo. It is documentation, not a transcript, so the About page's claim that session logs are the one promise still unkept stays true after this removal. Do not "fix" the About page as a side effect.

- [ ] **Finish the Uber-assumption paper and run the checks on it (~1.5h — uncertain: the remaining mathematics is real work, not write-up)**

  `latex/papers/uber-groups-rsr/main.tex` ("The Uber Assumption and its Random Self-Reducibility, in Non-Bilinear and Type 1, 2, 3 Bilinear Groups") is ~1,290 lines across 13 sections and compiles clean, but it is still a working draft — the last four commits were all substantive mathematics (2026-08-15/16: house-class conversion, a strengthened separation result, the decision procedure recast in standard algebra primitives). Finish it, then put it through the checks.

  Publishing is done — `papers/uber-groups-rsr/` exists, badge generated, PDF and LaTeX copies in place, listed under Papers → Archive. Two of the checks are done too, and are recorded in a "Checks run" section on the page itself rather than only in `git log`:

  - **Bibliography: verified, 16 August 2026.** All seventeen entries checked against their sources — author list, title, venue, volume, page range, year — including the two the paper leans on hardest, Galbraith–Paterson–Smart (*Discrete Applied Mathematics* 156(16):3113–3121, 2008) for the type classification and Boyen (Pairing 2008, LNCS 5209, pp. 39–56) for the Uber baseline. Nothing fabricated, misdated or misattributed, and the preliminary-version notes on Blum–Luby–Rubinfeld, Regev and Escala et al. check out. Nothing further owed here.
  - **`chktex` and `lacheck`: clean, 16 August 2026.** Two genuine hits fixed (intersentence spacing after "co-CDH", a missing `~` before a `\ref`), two source-hygiene spaces tidied, one inline suppression on the `\Span` definition. `latex/papers/uber-groups-rsr/.chktexrc` pins the four suppressed warnings with a documented reason each — 3, 24 and 36 as expected, plus 8, which fires only on correct en-dashes here and cannot mask a *missing* one. Re-run with `chktex -q -l .chktexrc main.tex` from that directory.

  What is actually left:

  - **Finish the mathematics.** The blocking item, and the author's. This is what keeps `status_summary` reading "working draft" and `proof_review` at `ai`.
  - **Run the four prompts.** None have been run yet: `prompts/proof.md` (the idealized-model audit — the paper lives in the generic-group model, squarely in its scope), then `prompts/style.md` and `prompts/latex.md` for typesetting, and `prompts/revise.md` for prose. Note `prompts/revise.md` enforces "no em-dashes in prose" as a hard invariant and the paper currently has 39, so that pass is not cosmetic.

- [ ] **Attempt the Groth conjecture (~2h — highly uncertain: genuine open research, may not resolve regardless of time spent)**

  `c/0008` ("No Two-Element Split Non-Interactive Linear Proofs for Hard Relations") and `c/0009` ("Groth16 Proof-Size Optimality in the Pure Generic Group Model") are both open — whether a 2-element split NILP can be statistically sound against affine provers for any hard relation generator, equivalently whether Groth16's 3-group-element proof size is optimal in the pure GGM (no random oracle, non-interactive, publicly verifiable, generic prover). `p/groth16-proof-size-optimality/index.qmd` has the full parameter lattice and provenance: Groth (EUROCRYPT 2016) posed the 2-element question as his paper's own closing open problem; every subsequent result has attacked some restriction of the pure-GGM model rather than this exact cell. `c/0008` implies `c/0009`, so proving the stronger statement (`c/0008`) resolves both.

- [ ] **Convert the UC-for-gamers paper to HTML (~1.25h — manual: trial-and-error against third-party LaTeX toolchains)**

  Needed as a prerequisite (or at least a shared source) for the interactive UC tutorial task below: that tutorial quotes functionality excerpts from the paper, and an HTML version is what makes those excerpts reusable as live web content instead of screenshotted PDF pages.

  - The main conversion risk is the paper's heavy custom LaTeX: `tcolorbox` (the property/game boxes, saturated header + coloured body), `algpseudocode` (the operation listings), and extensive `\hypertarget`/`\hyperlink` cross-referencing (line numbering across shell/finalization boxes, `\opdef`/`\op` targets) — none of these survive a naive converter untouched. Check LaTeXML and `make4ht`/tex4ht against a representative box (e.g. one of `F-Net`, `F-AC`, `G-Clock`) early, before committing to a toolchain, to see which one preserves the box styling and internal hyperlinks rather than flattening them to plain text.
  - Whatever the box markup degrades to in HTML, math and cross-reference links must not: the per-box line numbering and cross-box hyperlinks are load-bearing for how the paper is read, so a conversion that silently drops or renumbers them is a regression, not an acceptable simplification.
  - Decide up front whether the target is (a) one faithful HTML mirror of the whole paper, or (b) just the excerpted figures/boxes the tutorial task needs pulled out individually — the two have very different toolchains (whole-document converter vs. per-box snippet export) and it's worth picking before starting rather than defaulting into whichever is easier to try first. Note that (b) is already solved for the functionality boxes: `scripts/gen_interface.py` renders a `\begin{interface}` fragment to styled HTML directly, no third-party converter involved, and it handles the `algpseudocode` subset and the continuous line numbering that a general converter is most likely to mangle. It covers only `interface` environments, not the paper's prose, theorems or diagrams — but if a trial shows LaTeXML/`make4ht` flattening the boxes, splicing this generator's output back over the converter's is a live option, and extending it to the `procedure` environment is a small job.


- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  93 of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, and F-AC are now filled in, ported from `surveys/uc-for-gamers/latex/main.tex`). Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. No other functionality currently has a ready-made source of this quality to adapt from, so expect this to mean drafting from the literature directly rather than porting.

  The tooling for this now exists, so this is a matter of running it 93 times rather than inventing the process each time: `prompts/source.md` is the per-stub prompt (source the definition, screenshot it as reviewer evidence, rewrite it in the book's notation, keep a mismatch register), and `scripts/gen_interface.py` turns the `.tex` fragment it produces into the page's box with the line numbering computed and CI-gated. What the estimate is still carrying is the part the tooling cannot shortcut: locating each definition in the literature, choosing between incompatible variants, and verifying every citation is a real paper at a real venue in a real year. Expect the mismatch registers to be the most interesting output, and expect some functionalities to have no canonical printed definition at all — that finding is itself a page worth having.

- [ ] **Interactive UC tutorial for the website (~2.25h — minor manual: clicking through the drag/interactive slides by hand to check they actually work)**

  Based on the UC-for-gamers paper; depends on the HTML-conversion task above.

  Structure:

  - Chapter by chapter: each chapter opens with a few slides explaining its concepts, with Next/Previous navigation.
  - Slides include images and excerpts of functionalities drawn from the paper.
  - Each section ends with a quiz, in three tiers: basic-knowledge, deep-dive, and harder/trick-statement.

  Design techniques to build the tutorial around, drawn from how Brilliant.org, Duolingo and the spaced-repetition/gamification literature approach technical learning — worth a fresh look at these sources when this task is actually picked up, since the field moves:

  - **Learn by doing, not watching.** Brilliant's core lesson unit is a guided problem the learner manipulates directly — drag, choose, compute — with the concept explained *through* the interaction rather than in a lecture the learner then gets quizzed on. Apply this to the chapter slides: prefer a slide where the reader drags a process id onto a functionality box or predicts a UC-emulation outcome before being told the answer, over a slide of prose followed by a separate quiz question.
  - **Build intuition before formalism, minimal cognitive load per slide.** Start each chapter's slide sequence with the simplest instance of the idea (one functionality, one corruption, no hybrids) and layer complexity slide by slide — mirrors both Brilliant's approach and the progressive-disclosure pattern Duolingo's onboarding uses to avoid overwhelming a new user.
  - **Immediate, specific feedback, not just right/wrong.** Every quiz answer — correct or not — should get a one-line explanation tied to *why*, not a bare checkmark/cross. This is what Brilliant's "instant custom feedback" and Duolingo's per-answer explanations both lean on for retention.
  - **Misconception-based distractors for the multiple-choice tiers.** Each wrong option should be "wrong for a reason" — a specific, real misunderstanding a UC newcomer plausibly holds (e.g. conflating the security parameter with a corruption bound, assuming the environment can see a functionality's internal coins, forgetting a shell has to be built to the *strictest* verdict it serves) — not an arbitrary false statement. This directly serves the harder-quizzes tier: a true/false statement that inverts logic should invert a *specific* convention from the paper's notation-conventions list, so a wrong answer diagnoses which convention the reader hasn't internalized yet.
  - **Deep-dive quizzes as combinatorial retrieval, not just recall.** The puzzle tier should force recombining a later chapter's functionality with an earlier chapter's property or shell.
  - **Light gamification paired with spaced review, not gamification alone.** Streaks/XP/progress bars alone are a weak retention lever; the literature's stronger result is spaced repetition *combined* with light game mechanics. Concretely: resurface a prior chapter's quiz question (in a new combination) a chapter or two later rather than only in that chapter's own quiz, and track a streak across that resurfacing rather than only within one session.
