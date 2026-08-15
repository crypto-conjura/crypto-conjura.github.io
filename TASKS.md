# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates assume the work is done with Claude (Premium) doing the bulk of it, not a human working unassisted — keep new estimates calibrated the same way. Total estimated time: **~69h** (rough; the two research/production-scale items — UC Encyclopedia content and the LHL secret-seed resolution — are especially uncertain and could run well over their estimate, or in the LHL case, not resolve at all regardless of tooling).

- [ ] **Convert the UC-for-gamers paper to HTML (~5h)**

  Needed as a prerequisite (or at least a shared source) for the interactive UC tutorial task below: that tutorial quotes functionality excerpts from the paper, and an HTML version is what makes those excerpts reusable as live web content instead of screenshotted PDF pages.

  - The main conversion risk is the paper's heavy custom LaTeX: `tcolorbox` (the property/game boxes, saturated header + coloured body), `algpseudocode` (the operation listings), and extensive `\hypertarget`/`\hyperlink` cross-referencing (line numbering across shell/finalization boxes, `\opdef`/`\op` targets) — none of these survive a naive converter untouched. Check LaTeXML and `make4ht`/tex4ht against a representative box (e.g. one of `F-Net`, `F-AC`, `G-Clock`) early, before committing to a toolchain, to see which one preserves the box styling and internal hyperlinks rather than flattening them to plain text.
  - Whatever the box markup degrades to in HTML, math and cross-reference links must not: the per-box line numbering and cross-box hyperlinks are load-bearing for how the paper is read, so a conversion that silently drops or renumbers them is a regression, not an acceptable simplification.
  - Decide up front whether the target is (a) one faithful HTML mirror of the whole paper, or (b) just the excerpted figures/boxes the tutorial task needs pulled out individually — the two have very different toolchains (whole-document converter vs. per-box snippet export) and it's worth picking before starting rather than defaulting into whichever is easier to try first.

- [ ] **UC Encyclopedia content (~30h)**

  Every one of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) is still a stub. Fill in real content incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts.

- [ ] **Port the functionalities already defined in uc-for-gamers into the UC Encyclopedia (~4h)**

  `surveys/uc-for-gamers/latex/main.tex` gives full, concrete pseudocode definitions (not just names) for seven functionalities, each in its own chapter with a "Functionality" section: F-Rand (Ch. "Randomness"), F-Store (Ch. "Storage"), F-Sig (Ch. "Digital Signatures", plus a whole deep-dive chapter), G-PKI (Ch. "Public-Key Infrastructure"), G-Clock (Ch. "Global Clock"), F-Net (Ch. "Δ-Delayed Network"), and F-AC (Ch. "Δ-Delayed Authenticated Channel"). Note: F-Diffuse and F-IO are only *named* in the book (line ~932: "functionalities we do not give"), not actually defined — don't port those as if they were.

  - `f-sig`, `g-clock`, and `g-pki` already have encyclopedia pages (`uc/layer-3-public-key-primitives/f-sig`, `uc/layer-0-idealized-setup/g-clock`, `uc/layer-0-idealized-setup/g-pki`) but are currently thin stubs (title, status, one-liner, external references only) — fill them in with the book's actual definitions.
  - `f-rand`, `f-store`, `f-net`, and `f-ac` have no encyclopedia page at all yet. `f-rand`/`f-store` likely belong under `uc/layer-0-idealized-setup/` alongside `g-clock`/`g-pki`. `f-net`/`f-ac` likely belong under `uc/layer-1-channels-agreement-ledgers/`, but that layer already has `f-auth` and `f-sc` (non-delayed authenticated/secure channel) — decide whether `f-net`/`f-ac` are new, distinct entries (the book's variants are Δ-delayed) or should fold into/rename those existing stubs, before creating new folders.
  - Overlaps with the broader "UC Encyclopedia content" task above; this is the slice of it with a ready-made source to adapt from rather than starting from a blank stub.

- [ ] **Interactive UC tutorial for the website (~18h)**

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

- [ ] **Finish and publish the uber-groups-rsr paper (~2h)**

  `latex/papers/uber-groups-rsr/main.tex` — "The Uber Assumption and its Random Self-Reducibility (in Non-Bilinear and Type 1, 2, 3 Bilinear Groups)" — is a working draft under `/latex/` (local-only, not on GitHub per `latex/README.md`). Finish the draft, then publish it following `latex/README.md`'s "Publishing a draft" flow: create `papers/uber-groups-rsr/` from the `papers/example-paper/index.qmd` template, move the `.tex` source and compiled PDF into its `latex/`/`pdf/` subfolders, and transcribe the statement into `index.qmd`.

- [ ] **Finish resolving the LHL conjecture (secret-seed case) (~10h)**

  `c/0004` (public seed) is proven; `c/0005` (secret seed) is still open. Its resolution note (`c/0004/latex/proof.tex`) cites a bound for the secret-seed case from an external "companion note," for comparison only: that note isn't included anywhere in this repo and its claim hasn't been independently checked. Either locate/add that companion note's own statement and resolution (as a citation, or as its own artifact), or treat the secret-seed case as genuinely unresolved and pursue it separately. Separately, neither statement has a Lean formalization yet (`status.statement_formal`/`proof_formal` are both `open` on both).
