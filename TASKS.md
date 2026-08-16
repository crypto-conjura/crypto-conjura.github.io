# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~12.0h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `5e5e95b` on 16 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

- [ ] **Restrict who can modify anything outside `latex/` (~0.5h, blocked on a decision)**

  Requested 16 August 2026: allow others to modify only the `latex/` folder. Investigated the same day. The literal form of this is not available on this repository, so what follows is what is available instead.

  - **GitHub has no path-scoped write permission.** The repository roles (Read, Triage, Write, Maintain, Admin) each apply to the whole repository. The only path-aware enforcement GitHub offers is the "Restrict file paths" rule, and that rule exists only inside a *push* ruleset. The documentation scopes push rulesets to "a private or internal repository and that repository's entire fork network", and this repository is public, so push rulesets cannot be created here at all; the separate Team-plan requirement reported for them is moot on top of that. The rule is in any case a deny list of `fnmatch` patterns with no negation syntax, so "everything except `latex/`" would have to enumerate the other 27 top-level entries and would silently stop covering whatever is added later.
  - **There is nothing to restrict today.** `farshim` is the only account with any access: one organization member, no teams, no outside collaborators, no bots. Everyone else already reaches the repository through a fork and a pull request and can modify nothing without a merge. That flow, not a permission setting, is what currently enforces the intent, and it is stricter than what was asked for.
  - **`main` is unprotected, which is the actual gap.** No rulesets, no branch protection, no `CODEOWNERS`. The moment any collaborator is granted write access they can push anything anywhere, `latex/` or otherwise, with nothing to stop them.

  Two ways forward, to be chosen before anything is built:

  - Grant write access to nobody and leave the configuration alone. Strongest guarantee available on this plan, already in force, nothing to maintain.
  - Or, before write access is ever granted: a branch ruleset on `main` requiring pull requests, which unlike a push ruleset *is* available for public repositories on the Free plan, plus a `pull_request` Actions job that reads the changed paths and fails when an author outside an allow list touches anything beyond `latex/`, registered as a required status check. This is the closest free equivalent to the rule that was asked for, and it enforces rather than documents. A repository admin can still bypass it, so it constrains collaborators, not the owner.

  The second is only worth building if collaborators are actually going to be added.

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

- [ ] **Fix the four known defects in the HTML edition of UC for Gamers (~0.75h)**

  The conversion itself is done and live at `/surveys/uc-for-gamers/html/main.html`, built by `scripts/build_uc_html.sh`. These are what it shipped with, known and unfixed. Numbers below were measured against the installed files on 16 August 2026, and they correct the looser description in pull request #23, which undercounted the first defect and misdiagnosed it as two.

  - **No line reference in the edition works.** Of 1,104 cross-references, the 806 pointing at definitions, sections, theorems and the rest all resolve correctly. All 298 pointing at pseudocode lines fail, in two ways: 279 resolve but land on the enclosing chapter heading instead of the line, and 19 are dead, pointing at two synthetic anchors (`#x1-11001r3.6`, `#x1-18001r5`) that tex4ht never emitted. Eight distinct labels collapse onto those two targets, which is the tell: tex4ht is not emitting per-line anchors for `algpseudocode` labels at all, and the surviving links only appear to work. This is the load-bearing defect, because line-referenced pseudocode is how the paper explains itself.
  - **`scripts/build_uc_html.sh` cannot catch the above.** Its cross-reference check greps for `[?]`, which is what LaTeX emits for an *unresolved* `\ref`. These all resolved; they resolved to the wrong place. A fix should add a real link audit to the script: parse every `href`, check the fragment against the ids actually present, and fail on a dead one. Note the trap that produced the bad numbers in #23 and twice more during the build: tex4ht writes single-quoted attributes, so a check written against `href="` matches nothing and reports success.
  - **`\emph` degrades to a font-class span.** 348 `\emph` in the source, 0 `<em>` in the output, 1,162 `class='pplri8t-'` spans instead. Emphasis is visual only, carrying nothing for screen readers or for search.
  - **MathJax loads from a CDN.** Every other asset on the site is self-hosted; this page fetches `cdn.jsdelivr.net` on load, and none of the 5,886 formulas render if that fetch fails.

- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  97 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs — measured 16 August 2026, and it corrects the 93-of-100 figure this entry carried before (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, and F-AC are the seven filled in, ported from `surveys/uc-for-gamers/latex/main.tex`). Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. No other functionality currently has a ready-made source of this quality to adapt from, so expect this to mean drafting from the literature directly rather than porting.

  The tooling for this now exists end to end, so this is a matter of running it 97 times rather than inventing the process each time:

  - `scripts/uc_source.py <id>` does the mechanical half. It reads the page's own reference bullets, resolves each to a PDF (newest ePrint revision, falling back to the PostScript-only postings the 1990s papers still are), records every revision stamp, scans the text layer for interface-box titles, renders the pages carrying a box named after the functionality into `<id>/_src/`, and writes `<id>/_src/sources.json` with URL, revision, page and a ready-made citation pointer. The PNGs are gitignored — a proceedings figure is the publisher's — and `_src/` is `_`-prefixed so Quarto never publishes it; the manifest is committed and reproduces the images exactly.
  - `prompts/source.md` is the per-stub prompt, rewritten 16 August 2026 around that harvest: choose among the cited definitions in a fixed order (same object first, then revision/formulation/framework currency, then a tie-break ladder), capture the original as reviewer evidence, rewrite it in the book's notation, keep a mismatch register.
  - `scripts/gen_interface.py` turns the `.tex` fragment into the page's box with the line numbering computed and CI-gated, and `--vs-preview` compiles a fragment standalone to prove LaTeX prints the line numbers the generator computed — the check `--vs-pdf` cannot do for the 97 boxes the book does not typeset.

  Two facts the tooling has already established about the shape of the job: 11 of the 97 stubs cite nothing at all (F-RP, F-CRHF, F-MHF, F-OWF, F-PRG, F-ABE, F-IBE, F-GC, F-ORAM, F-PIR, F-PSI), so they need a literature search before the harvester has anything to work with; and a citation that yields no box is a normal, informative result — Rabin 1981 contains no `F_OT`, because it predates ideal functionalities, and the page should say so rather than force one.

  What the estimate is still carrying is the part the tooling cannot shortcut: choosing between incompatible variants, and verifying every citation is a real paper at a real venue in a real year. Expect the mismatch registers to be the most interesting output, and expect some functionalities to have no canonical printed definition at all — that finding is itself a page worth having.

  One ordering trap, which turns CI red for the whole site: `gen_interface.py --check` runs in both workflows over every fragment in `functionalities/` and errors if a fragment's page has no `.cj-interface` block to replace. The page scaffold and the fragment must land in the same commit.

- [ ] **Interactive UC tutorial for the website (~2.25h — minor manual: clicking through the drag/interactive slides by hand to check they actually work)**

  Based on the UC-for-gamers paper. Its prerequisite is met: the HTML edition exists at `/surveys/uc-for-gamers/html/main.html`, so chapter text, the nine diagrams as SVG and the functionality boxes can all be quoted as live web content rather than screenshotted from the PDF. Read the defect task above before quoting anything with a line reference in it.

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
