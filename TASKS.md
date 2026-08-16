# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~13.8h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `3aba67d` on 16 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

- [ ] **Shorten the About page, then proofread it with `prompts/prose.md`, then update it (~50 min)**

  `about/index.qmd` is 163 lines and roughly 3,080 words under 21 headings: two `Part` headings, then 19 sections and subsections beneath them. It got there by accretion, three tasks in one day writing into the same page, and it now reads as a list of positions rather than one.

  Three steps, in order. The shortening comes first, because proofreading a structure that is about to change wastes the pass.

  - **Cut and merge subsections.** The clearest candidates are the four `(an idea we're exploring)` subsections in Part I, which close on near-identical disclaimer sentences and would read better as one subsection with four short entries. Part II's seven `##` sections are each defensible alone but are cumulatively long for a reasoning half. Target something closer to 10 or 12 headings without losing an argument.
  - **One cross-reference breaks if the merge happens.** `## Say plainly what isn't built yet` states that "four of its subsections carry the same flat disclaimer" and names the bounties, the idle tokens, the distributed compute and the journal. Collapsing those four into one makes that sentence false, so it has to move with them.
  - **Then the proofread, then apply it.** Run the page through `prompts/prose.md` and update the page from the result rather than treating the output as final copy.

  Two frictions worth knowing before starting, neither a reason not to do it:

  - **`prompts/prose.md` is built for LaTeX, not Quarto.** Its opening line says it revises "a mathematical manuscript... written in LaTeX and compiled with `pdflatex`", and its rules assume `.tex` source, `\label`s, and math environments. `about/index.qmd` is Quarto markdown with callout blocks, a table and site-relative links. The prose rules carry over; the mechanical and typesetting ones do not, and the edit-tagging convention needs adapting or dropping.
  - **The site recommends the other prompt for new work.** `prompts/index.qmd` describes `prose.md` as "the original, shorter version... Kept for comparison; use the manuscript version above for new work", meaning `revise.md`, which adds length targets, a mechanical sweep and a conflict register. `prose.md` is what was asked for and is what should be run; worth a second pass with `revise.md` if the first leaves the length target unmet.

- [ ] **Move the UC Encyclopedia under Surveys (~30 min — decide the URL question before touching anything)**

  The Encyclopedia is a top-level section today: `uc/` in the repo, its own navbar entry on the right of `_quarto.yml`, and its own top-level sidebar section with the nine layers under it. Putting it under Surveys is really two different jobs, and which one this is has to be settled first:

  - **Navigation only.** The navbar and sidebar entries move under Surveys, `surveys/index.qmd` gains it in the "Browse" list, and every URL stays at `/uc/...`. Cheap, reversible, and nothing outside `_quarto.yml` and one listing page changes. Note `_quarto.yml` carries a comment demanding the navbar's left-hand entries and the sidebar's top-level sections stay mirrored — the UC entry currently lives in `navbar.right`, so moving it means the mirroring rule now applies to it.
  - **URLs too.** `/uc/...` becomes `/surveys/uc/...`, which moves 114 `.qmd` files and rewrites references in `scripts/gen_interface.py`, `prompts/source.md`, `CONTRIBUTING.md`, `README.md`, `index.qmd`, `latex/README.md`, `latex/uc/README.md`, and the cross-links inside the already-filled functionality pages (`f-sig`, `f-net`, `f-ac`, `g-pki`). Every old URL then needs an alias or it 404s. Doable, but it is the whole afternoon's difference from the option above.

  My read: navigation only, unless there is a reason to want the URLs to match the hierarchy. The recommendation is not free of friction though —

  - `surveys/index.qmd` defines a survey as "book-length expository work… a sustained treatment of one area, built to teach it", and its Browse list currently holds exactly one entry, UC for Gamers. An encyclopedia of 100 functionality pages is a reference work, not a book read front to back; the section's own definition needs a sentence widening it, or the Encyclopedia will sit there contradicting the paragraph above it.
  - `uc/index.qmd` says in its own words that the section "may eventually move to a dedicated site of its own, separate from Conjura." Filing it under Surveys pushes the opposite way. Either that note goes, or the move is explicitly the interim arrangement and says so — leaving both claims on the site is the kind of quiet contradiction the rest of this list keeps trying to avoid.
  - Surveys and the Encyclopedia are already entangled in the right direction: seven of the filled functionality pages were ported out of `surveys/uc-for-gamers/latex/main.tex`, and the Surveys page already promises interactive content generated from a survey's own text. That is the actual argument for the move, and it is worth stating on the page rather than leaving the new hierarchy to imply it.

- [ ] **Say on the site that the site itself is AI-generated and not yet reviewed (~25 min — manual: whether this becomes an open call for reviewers is a commitment only you can make)**

  The badges cover the research artifacts: a statement, a proof, a Lean file each carry a graded provenance and a "reviewed by" line. Nothing covers the *container* — the prose on every page, `CONTRIBUTING.md`, `schema/`, the scripts under `scripts/`, the encyclopedia stubs, the templates. All of it was generated by an AI under extensive human prompting and refinement, and none of it has been independently reviewed by anybody. That is exactly the kind of thing this site says elsewhere should be disclosed per artifact, so omitting it about itself would be the single most quotable inconsistency available to a critic — and a fair one.

  What it has to say, in one short paragraph: the site is AI-generated; a human directed, prompted and refined it throughout, so it is not unsupervised output; it has **not** had thorough independent review, and it wants that review from more than one reviewer. Written as a plain statement of status, not an apology and not a disclaimer that tries to shed responsibility — the "extensive prompting and refinement" clause is there because it is true, not to soften the first clause.

  Mechanics, which are the actual work:

  - **A site-wide notice needs a footer, and there isn't one.** `_quarto.yml` has `navbar` and `sidebar` but no `page-footer`, so a persistent one-line notice means adding that key plus matching styling in both `theme-light.scss` and `theme-dark.scss`. One line linking to the full statement on `about/index.qmd` is the right weight; a banner on every page is not.
  - **The full statement lives on `about/index.qmd`**, and it belongs next to "Plausible isn't the same as true" and "Say plainly what isn't built yet" — it is those two commitments turned on the site itself, and saying so is what keeps it from reading as boilerplate.
  - **Say what would take it down.** A notice with no exit condition becomes furniture that nobody updates and every reader learns to skip. State what changes it: which parts have been reviewed, by whom, and when — the same shape as the badge semantics, so the notice narrows as review actually happens rather than staying a permanent blanket.
  - **Decide whether it asks for something.** "Wants multiple reviewers" can be a statement of fact or an open call with a route in (an issue label, a contact). The second is more useful and is a commitment; that choice is yours.

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
