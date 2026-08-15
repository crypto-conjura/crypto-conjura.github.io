# Tasks

Ordered by priority, highest first.

- [ ] **Finish resolving the LHL conjecture (secret-seed case)**

  `c/0004` (public seed) is proven; `c/0005` (secret seed) is still open. Its resolution note (`c/0004/latex/proof.tex`) cites a bound for the secret-seed case from an external "companion note," for comparison only: that note isn't included anywhere in this repo and its claim hasn't been independently checked. Either locate/add that companion note's own statement and resolution (as a citation, or as its own artifact), or treat the secret-seed case as genuinely unresolved and pursue it separately. Separately, neither statement has a Lean formalization yet (`status.statement_formal`/`proof_formal` are both `open` on both).

- [ ] **Verify status badge contrast in dark theme**

  The concentric-ring status badge (`scripts/status_badge.py`, `theme-light.scss`/`theme-dark.scss`) had a real bug where the lowest-grade (σ=0/π=0) ring and disc colours were nearly invisible against the light-theme page background — fixed and confirmed via an actual headless-Chrome screenshot. The dark-theme colours were only checked by comparing hex values (RGB distance from `$body-bg`), never with a real screenshot, because the site's dark mode is toggled via a `data-bs-theme="dark"` attribute (not `prefers-color-scheme`), which the available headless-Chrome flags couldn't force. Confirm it actually looks right — ideally by clicking the theme toggle in a real browser, or scripting the attribute switch some other way.

- [ ] **Add a "Resources" section to the sidebar for LaTeX templates and prompts**

  In `_quarto.yml`, `open-problems/latex-templates/index.qmd` currently sits nested under the "Open Problems" section (`_quarto.yml:61`), and "Prompts" is its own top-level sidebar section (`_quarto.yml:63-68`). Pull both out under a new top-level "Resources" section instead.

- [ ] **UC Encyclopedia content**

  Every one of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) is still a stub. Fill in real content incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts.

- [ ] **Tag papers by topic**

  Give papers the same tag treatment conjectures already have:

  - `papers/example-paper/index.qmd` already has the `categories: []` field scaffolded in; populate it once there's real content to tag.
  - Decide whether papers get their own per-topic listing pages (mirroring `open-problems/areas/<area>/index.qmd`), or a single `categories: true` filterable listing on `papers/index.qmd` (mirroring `blog/index.qmd`) — revisit once there's more than one real paper to justify either.

- [ ] **Convert the UC-for-gamers paper to HTML**

  Needed as a prerequisite (or at least a shared source) for the interactive UC tutorial task below: that tutorial quotes functionality excerpts from the paper, and an HTML version is what makes those excerpts reusable as live web content instead of screenshotted PDF pages.

  - The main conversion risk is the paper's heavy custom LaTeX: `tcolorbox` (the property/game boxes, saturated header + coloured body), `algpseudocode` (the operation listings), and extensive `\hypertarget`/`\hyperlink` cross-referencing (line numbering across shell/finalization boxes, `\opdef`/`\op` targets) — none of these survive a naive converter untouched. Check LaTeXML and `make4ht`/tex4ht against a representative box (e.g. one of `F-Net`, `F-AC`, `G-Clock`) early, before committing to a toolchain, to see which one preserves the box styling and internal hyperlinks rather than flattening them to plain text.
  - Whatever the box markup degrades to in HTML, math and cross-reference links must not: the per-box line numbering and cross-box hyperlinks are load-bearing for how the paper is read, so a conversion that silently drops or renumbers them is a regression, not an acceptable simplification.
  - Decide up front whether the target is (a) one faithful HTML mirror of the whole paper, or (b) just the excerpted figures/boxes the tutorial task needs pulled out individually — the two have very different toolchains (whole-document converter vs. per-box snippet export) and it's worth picking before starting rather than defaulting into whichever is easier to try first.

- [ ] **Interactive UC tutorial for the website**

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
  - **Deep-dive quizzes as combinatorial retrieval, not just recall.** The puzzle tier should force recombining a later chapter's functionality with an earlier chapter's property or shell: structurally the same "combine two entities" move the missing diagrams task (below) wants diagrams for, so the two tasks can likely share source material (a diagram doubling as a deep-dive quiz's prompt image).
  - **Light gamification paired with spaced review, not gamification alone.** Streaks/XP/progress bars alone are a weak retention lever; the literature's stronger result is spaced repetition *combined* with light game mechanics. Concretely: resurface a prior chapter's quiz question (in a new combination) a chapter or two later rather than only in that chapter's own quiz, and track a streak across that resurfacing rather than only within one session.

- [ ] **Recover or write the missing "diagrams" task**

  Referenced twice above (by the UC tutorial task, as a source of shareable diagrams combining a functionality with a property/shell) but never itself defined anywhere in this repo or file history. Either find where it was dropped, or write it fresh before the tutorial task needs it.
