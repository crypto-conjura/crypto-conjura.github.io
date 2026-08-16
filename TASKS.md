# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~12.58h** (rough; the UC Encyclopedia content item is especially uncertain and could run well over its estimate).

- [ ] **Usability on iPhone, Android, and other handheld devices (~15 min — manual: PDF fragment behavior needs a real physical device, not just emulation)**

  Playwright's actual device emulation (WebKit as iPhone 14, Chromium as Pixel 7 — real per-device viewport, touch, and pixel-ratio profiles, not a resized desktop window) found and fixed three real horizontal-overflow bugs on narrow viewports, all in `theme-{light,dark}.scss`: MathJax display equations wider than their column (c/0001, c/0002, c/0004, and likely other statement pages), plain markdown/pandoc tables that didn't scroll (c/0001–c/0003), and the page-layout:article content grid not shrinking below its content's intrinsic width the same way page-layout:full was already fixed to. Verified clean afterward on both device profiles across the landing, listing, statement, and UC pages. Also verified: the mobile sidebar/navbar off-canvas toggle (`.quarto-btn-toggle`, in `quarto-secondary-nav`) works correctly — an initial concern that it was unreachable turned out to be testing the wrong button, not a real bug. Touch targets are dominated by standard framework chrome (search button, hamburger, dark-mode toggle, anchorjs heading anchors) at their normal sizes; the one custom element under the 44px guideline is the small `cj-status-link` badge icon (~24-28px on these profiles), a minor cosmetic gap, not fixed here.

  What's left, and can't be shortcut by emulation (Playwright drives the real WebKit/Chromium rendering engines but not iOS/Android's native PDF viewer integration): check the UC-for-gamers "Contents" links (`pdf/main.pdf#page=N`) on an actual iPhone and Android phone — desktop browsers honor the `#page=` fragment in their built-in viewer, but real mobile PDF handling (iOS Safari's viewer vs. Android Chrome/Samsung Internet, some of which just download the file) is inconsistent and can't be verified through emulation.

- [ ] **Mention a multi-account, multi-model distributed compute idea on the Vision page (~15 min)**

  `vision/index.qmd` already has two "(an idea we're exploring)" subsections following the same pattern: "Incentives for open problems" (on-chain bounties) and "Idle tokens" (other people's spare API/subscription capacity donated to the backlog). Add a third, distinct from both: a distributed system Conjura itself would run, orchestrating particularly compute-intensive research tasks across multiple AI accounts and multiple different models (not just one account, one model) to get more throughput on the hardest open problems than any single account/rate-limit allows. Same framing as the other two: a direction worth exploring, not a built feature.

- [ ] **A Philosophy page, with an audio read-out and a podcast (~1.5h — manual: actual audio/podcast production, not just text generation)**

  A new page on the site's philosophy — distinct from `vision/index.qmd` ("why Conjura exists, where it's headed"), this is about the underlying worldview/reasoning rather than the roadmap; decide on the relationship between the two (separate page vs. a section of Vision) and where it sits in the nav (top-level like Vision, or nested under Resources) when picked up. Two things accompany the written page:

  - **An audio read-out** — a straight narrated version of the page's own text.
  - **A podcast** — a produced discussion-format episode, distinct from the read-out. Note the removed Blog section's old description ("informal write-ups — and eventually podcasts and videos — for resolved conjectures," `README.md:17`) was about individual resolved conjectures; this is scoped to the site's philosophy specifically, not that.

- [ ] **Attempt the Groth conjecture (~2h — highly uncertain: genuine open research, may not resolve regardless of time spent)**

  `c/0008` ("No Two-Element Split Non-Interactive Linear Proofs for Hard Relations") and `c/0009` ("Groth16 Proof-Size Optimality in the Pure Generic Group Model") are both open — whether a 2-element split NILP can be statistically sound against affine provers for any hard relation generator, equivalently whether Groth16's 3-group-element proof size is optimal in the pure GGM (no random oracle, non-interactive, publicly verifiable, generic prover). `p/groth16-proof-size-optimality/index.qmd` has the full parameter lattice and provenance: Groth (EUROCRYPT 2016) posed the 2-element question as his paper's own closing open problem; every subsequent result has attacked some restriction of the pure-GGM model rather than this exact cell. `c/0008` implies `c/0009`, so proving the stronger statement (`c/0008`) resolves both.

- [ ] **Convert the UC-for-gamers paper to HTML (~1.25h — manual: trial-and-error against third-party LaTeX toolchains)**

  Needed as a prerequisite (or at least a shared source) for the interactive UC tutorial task below: that tutorial quotes functionality excerpts from the paper, and an HTML version is what makes those excerpts reusable as live web content instead of screenshotted PDF pages.

  - The main conversion risk is the paper's heavy custom LaTeX: `tcolorbox` (the property/game boxes, saturated header + coloured body), `algpseudocode` (the operation listings), and extensive `\hypertarget`/`\hyperlink` cross-referencing (line numbering across shell/finalization boxes, `\opdef`/`\op` targets) — none of these survive a naive converter untouched. Check LaTeXML and `make4ht`/tex4ht against a representative box (e.g. one of `F-Net`, `F-AC`, `G-Clock`) early, before committing to a toolchain, to see which one preserves the box styling and internal hyperlinks rather than flattening them to plain text.
  - Whatever the box markup degrades to in HTML, math and cross-reference links must not: the per-box line numbering and cross-box hyperlinks are load-bearing for how the paper is read, so a conversion that silently drops or renumbers them is a regression, not an acceptable simplification.
  - Decide up front whether the target is (a) one faithful HTML mirror of the whole paper, or (b) just the excerpted figures/boxes the tutorial task needs pulled out individually — the two have very different toolchains (whole-document converter vs. per-box snippet export) and it's worth picking before starting rather than defaulting into whichever is easier to try first.


- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  93 of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, and F-AC are now filled in, ported from `surveys/uc-for-gamers/latex/main.tex`). Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. No other functionality currently has a ready-made source of this quality to adapt from, so expect this to mean drafting from the literature directly rather than porting.

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

