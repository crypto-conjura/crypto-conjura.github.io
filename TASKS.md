# Tasks

## To do

- [ ] **Tag papers by topic**

  Give papers the same tag treatment conjectures already have:

  - `papers/example-paper/index.qmd` already has the `categories: []` field scaffolded in; populate it once there's real content to tag.
  - Decide whether papers get their own per-topic listing pages (mirroring `open-problems/<topic>/index.qmd`), or a single `categories: true` filterable listing on `papers/index.qmd` (mirroring `blog/index.qmd`) — revisit once there's more than one real paper to justify either.

- [ ] **UC Encyclopedia content**

  Every one of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) is still a stub. Fill in real content incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts.

- [ ] **Verify status badge contrast in dark theme**

  The concentric-ring status badge (`scripts/status_badge.py`, `theme-light.scss`/`theme-dark.scss`) had a real bug where the lowest-grade (σ=0/π=0) ring and disc colours were nearly invisible against the light-theme page background — fixed and confirmed via an actual headless-Chrome screenshot. The dark-theme colours were only checked by comparing hex values (RGB distance from `$body-bg`), never with a real screenshot, because the site's dark mode is toggled via a `data-bs-theme="dark"` attribute (not `prefers-color-scheme`), which the available headless-Chrome flags couldn't force. Confirm it actually looks right — ideally by clicking the theme toggle in a real browser, or scripting the attribute switch some other way.

- [ ] **Finish resolving the LHL conjecture (secret-seed case)**

  `open-problems/information-theoretic/leftover-hash-lemma-unpredictable-sources/` currently resolves only the *public-seed* half of the page's two conjectures. The *secret-seed* conjecture is still open: the resolution note (`latex/proof.tex`) cites a bound for it from an external "companion note" for comparison only, but that companion note isn't included anywhere in this repo and its claim hasn't been independently checked. Either locate/add that companion note's own statement+resolution (as a citation, or as its own artifact), or treat the secret-seed case as genuinely unresolved and pursue it separately. Separately, neither conjecture has a Lean formalization yet (`status.statement_formal`/`proof_formal` are both `open`) — nobody was asked to write one for this pass.

## Future

- [ ] **Future Task 2: Interactive UC tutorial for the website**, based on this document.

  Structure:

  - Chapter by chapter: each chapter opens with a few slides explaining its concepts, with
    Next/Previous navigation.
  - Slides include images and excerpts of functionalities drawn from the paper.
  - Each section ends with a quiz, in three tiers (detailed below): basic-knowledge, deep-dive, and
    harder/trick-statement.

  Design techniques to build the tutorial around, drawn from how Brilliant.org, Duolingo and the
  spaced-repetition/gamification literature approach technical learning — worth a fresh look at
  these sources when this task is actually picked up, since the field moves:

  - **Learn by doing, not watching.** Brilliant's core lesson unit is a guided problem the learner
    manipulates directly — drag, choose, compute — with the concept explained *through* the
    interaction rather than in a lecture the learner then gets quizzed on. Apply this to the
    chapter slides: prefer a slide where the reader drags a process id onto a functionality box or
    predicts a UC-emulation outcome before being told the answer, over a slide of prose followed by
    a separate quiz question.
  - **Build intuition before formalism, minimal cognitive load per slide.** Start each chapter's
    slide sequence with the simplest instance of the idea (one functionality, one corruption, no
    hybrids) and layer complexity slide by slide — mirrors both Brilliant's approach and the
    progressive-disclosure pattern Duolingo's onboarding uses to avoid overwhelming a new user.
  - **Immediate, specific feedback, not just right/wrong.** Every quiz answer — correct or not —
    should get a one-line explanation tied to *why*, not a bare checkmark/cross. This is what
    Brilliant's "instant custom feedback" and Duolingo's per-answer explanations both lean on for
    retention.
  - **Misconception-based distractors for the multiple-choice tiers.** Each wrong option should be
    "wrong for a reason" — a specific, real misunderstanding a UC newcomer plausibly holds (e.g.
    conflating the security parameter with a corruption bound, assuming the environment can see a
    functionality's internal coins, forgetting a shell has to be built to the *strictest* verdict it
    serves) — not an arbitrary false statement. This is the standard advice for effective
    distractors in technical assessment design, and it directly serves the "harder quizzes" tier:
    a true/false statement that inverts logic should invert a *specific* convention from
    [[uc-for-gamers-conventions]] or the Notation conventions list above, so a wrong answer
    diagnoses which convention the reader hasn't internalized yet.
  - **Deep-dive quizzes as combinatorial retrieval, not just recall.** The puzzle tier should force
    recombining a later chapter's functionality with an earlier chapter's property or shell —
    structurally the same "combine two entities" move Future Task 1 wants diagrams for, so the two
    future tasks can likely share source material (a diagram from Task 1 doubling as a deep-dive
    quiz's prompt image).
  - **Light gamification paired with spaced review, not gamification alone.** Streaks/XP/progress
    bars alone are a weak retention lever; the literature's stronger result is spaced repetition
    *combined* with light game mechanics. Concretely: resurface a prior chapter's quiz question
    (in a new combination) a chapter or two later rather than only in that chapter's own quiz, and
    track a streak across that resurfacing rather than only within one session.

- [ ] **Future Task 3: Convert the paper to HTML for the website.** Needed as a prerequisite (or at
  least a shared source) for Future Task 2 — the tutorial slides quote functionality excerpts from
  the paper, and an HTML version is what makes those excerpts reusable as live web content instead
  of screenshotted PDF pages.

  - The main conversion risk is the paper's heavy custom LaTeX: `tcolorbox` (the property/game
    boxes, saturated header + coloured body), `algpseudocode` (the operation listings), and
    extensive `\hypertarget`/`\hyperlink` cross-referencing (line numbering across shell/finalization
    boxes, `\opdef`/`\op` targets) — none of these survive a naive converter untouched. Check
    LaTeXML and `make4ht`/tex4ht against a representative box (e.g. one of `F-Net`, `F-AC`,
    `G-Clock`) early, before committing to a toolchain, to see which one preserves the box styling
    and internal hyperlinks rather than flattening them to plain text.
  - Whatever the box markup degrades to in HTML, math and cross-reference links must not: the
    per-box line numbering and cross-box hyperlinks are load-bearing for how the paper is read (see
    the Notation conventions above), so a conversion that silently drops or renumbers them is a
    regression, not an acceptable simplification.
  - Decide up front whether the target is (a) one faithful HTML mirror of the whole paper, or
    (b) just the excerpted figures/boxes Future Task 2 needs pulled out individually — the two have
    very different toolchains (whole-document converter vs. per-box snippet export) and it's worth
    picking before starting rather than defaulting into whichever is easier to try first.

  > Note: this section references "Future Task 1" (diagrams) twice, but no such task is defined anywhere in this file or the rest of the repo — either it was dropped in a past edit, or it was never written down. Flagging rather than inventing content for it.
