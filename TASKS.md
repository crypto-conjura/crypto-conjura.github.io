# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~11.75h** (rough; the UC Encyclopedia content item is especially uncertain and could run well over its estimate).

- [ ] **Usability on iPhone, Android, and other handheld devices (~1h — manual: needs real physical devices, not just emulation)**

  A real-device (or accurate emulation, not just a resized desktop browser) pass across the site. The one concrete problem previously found here -- the 6-column statement-listing tables squeezing unreadably on narrow screens -- is fixed (they're now a 3-column Status/Statement/Tags layout, with Model/Form/Category collapsed into wrapping pills and the open-obligations count folded into the status line; verified at 390px width). What's left:

  - Specifically test the UC-for-gamers "Contents" links (`pdf/main.pdf#page=N`) that jump into a PDF page — desktop browsers honor the `#page=` fragment in their built-in viewer, but mobile PDF handling (iOS Safari's viewer vs. Android Chrome/Samsung Internet, some of which just download the file) is inconsistent and needs checking on actual devices, not assumed from desktop behavior.
  - A broader real-device pass beyond that one fixed table -- touch targets, the sidebar/navbar at narrow widths, etc. -- hasn't been done yet.
  - Note this is distinct from the "Site-wide uniformity audit" task below — that one is about consistency across pages regardless of screen size; this one is specifically about narrow/touch viewports.

- [ ] **Site-wide uniformity audit: how a page relates to its position in the site (~50 min — minor manual: eyeballing the side-by-side visual comparison)**

  A general consistency pass across every page family (`open-problems/**`, `papers/**`, `surveys/**`, `resources/**`, `uc/**`, `c/000N`, `prompts/**`), not tied to one specific page. Three concrete dimensions:

  - **Names matching the links that lead to them.** A sidebar/navbar label and the destination page's own title should read as the same thing once you click through — this has already been fixed once for the Papers section (Archive/Committee vs. Example Paper/Programme Committee); check the rest of `_quarto.yml` and every section index for the same drift recurring.
  - **Sub-links listed on each page.** A section's own index page should list links to its children the same way everywhere — `index.qmd`'s "Explore" grid and `papers/index.qmd`'s "Browse" links (Archive/Committee) are the current model; check whether `surveys/index.qmd`, `resources/index.qmd`, `open-problems/index.qmd`, and `uc/index.qmd` all surface their sub-pages the same way, or whether some just rely on the sidebar and say nothing in the body.
  - **Look and feel across pages.** `page-layout`, `title-block-banner`/`title-block-style`, and related metadata should be applied consistently rather than page-by-page as an afterthought (a version of this was fixed once already for the Papers page specifically) — worth a real side-by-side visual comparison, both themes, rather than just diffing frontmatter.

- [ ] **Add a "Proposals" section under Papers (~20 min)**

  `papers/index.qmd`'s "## Browse" section currently links to two things: [Archive](/papers/example-paper/index.qmd) and [Committee](/papers/programme-committee/index.qmd) (`_quarto.yml:69-73` mirrors the same two under the Papers sidebar section). Add a third: "Proposals". Needs a new `papers/proposals/index.qmd` (mirroring the `example-paper`/`programme-committee` pattern), a third `_quarto.yml` sidebar entry, and a third Browse link.

  The concept, to write up on that page: a proposal names a *focused research topic*, not a full statement — like a grant proposal, but narrower and more concrete. Example: "When is a problem in the Uber assumption family random self-reducible?" An AI (potentially multi-agent, potentially distributed across machines) is then tasked with working the topic: surveying the area, generating candidate statements, checking its own results, and autoformalizing what holds up. A proposal is the seed of a Paper (or an Open Problem, if what comes out is a precise unresolved statement rather than a resolved write-up) — decide on that relationship, and on the exact page format (a simple list vs. per-proposal pages with their own status), when picked up.

  Also explain *who this is for*: proposals exist for people who have the research idea but not the computational resources to carry it out themselves — a researcher or academic in a country where even a Pro-tier subscription is out of reach, or a topic that genuinely needs a high-spend/premium-rate account to work through. Posting it as a proposal is how the idea gets pursued anyway, by whoever (or whatever compute) picks it up.

- [ ] **Document the pre-human review pipeline on the Programme Committee page (~15 min)**

  `papers/programme-committee/index.qmd`'s "## How reviewing works" section currently only describes the human-committee step (a member reviews, their name joins the `Reviewers` field). Add what happens *before* that: every paper first goes through agentic "stress tests" — meticulous, adversarial scrutiny for mistakes, run via topic-specific prompts that check for the fatal errors and gaps known to recur in that area's literature. Only after that does an editorial pass improve the writing itself against best practice for mathematical exposition (style manuals, standard conventions), and only after *that* is a paper in a position for a human reviewer to look at it — the agentic stages are a filter, not a replacement for the human step described above. Also worth stating as a standing constraint: a paper's focus is kept to its specific conjecture (not broadened into a survey or multi-result piece) precisely to keep this whole pipeline, human review included, tractable.

- [ ] **A Philosophy page, with an audio read-out and a podcast (~1.5h — manual: actual audio/podcast production, not just text generation)**

  A new page on the site's philosophy — distinct from `vision/index.qmd` ("why Conjura exists, where it's headed"), this is about the underlying worldview/reasoning rather than the roadmap; decide on the relationship between the two (separate page vs. a section of Vision) and where it sits in the nav (top-level like Vision, or nested under Resources) when picked up. Two things accompany the written page:

  - **An audio read-out** — a straight narrated version of the page's own text.
  - **A podcast** — a produced discussion-format episode, distinct from the read-out. Note the removed Blog section's old description ("informal write-ups — and eventually podcasts and videos — for resolved conjectures," `README.md:17`) was about individual resolved conjectures; this is scoped to the site's philosophy specifically, not that.

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

