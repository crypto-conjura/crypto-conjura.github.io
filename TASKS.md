# Tasks

Ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates assume the work is done with Claude (Premium) doing the bulk of it, not a human working unassisted — keep new estimates calibrated the same way. Total estimated time: **~76h** (rough; the two research/production-scale items — UC Encyclopedia content and the LHL secret-seed resolution — are especially uncertain and could run well over their estimate, or in the LHL case, not resolve at all regardless of tooling).

- [ ] **Simplify the conjecture-listing tables (~2h)**

  `_listing-templates/statement-table.ejs.md` — shared by 28 pages (`open-problems/all/index.qmd` plus every `areas/`, `model/`, `form/`, `assumption/` listing page) — currently renders 6 columns: Status badge, Statement (+ one-line summary), Model, Form, Category, Open (obligations count). Simplify it: the Model/Form/Category trio in particular reads as three separate wide columns for what's really just tag data — consider collapsing them into a single compact tags cell (small pills/labels) next to the statement, and reconsider whether the Open-obligations count earns its own column or belongs folded into the status summary line instead. Since one shared template drives all 28 pages, this is high-leverage — and overlaps with the "Usability on handheld devices" task above, which flagged this same table as cramped on narrow screens; a simpler table may resolve both at once.

- [ ] **Usability on iPhone, Android, and other handheld devices (~4h)**

  A real-device (or accurate emulation, not just a resized desktop browser) pass across the site. One concrete problem already found: the wide statement-listing tables — `open-problems/all/index.qmd` and every `open-problems/areas/<area>/index.qmd`, all built from `_listing-templates/statement-table.ejs.md` (Status/Statement/Model/Form/Category/Open, 6 columns) — don't adapt for narrow screens, they just squeeze, so on an iPhone-width viewport "Model"/"Form"/"Category" become single-word columns wrapping awkwardly across several lines instead of scrolling horizontally or collapsing columns. By contrast the 2-column UC Encyclopedia tables (`uc/layer-N-.../index.qmd`, Functionality/Status) read fine at the same width — worth using that as the bar to clear.

  - Also worth specifically testing: the UC-for-gamers "Contents" links (`pdf/main.pdf#page=N`) that jump into a PDF page — desktop browsers honor the `#page=` fragment in their built-in viewer, but mobile PDF handling (iOS Safari's viewer vs. Android Chrome/Samsung Internet, some of which just download the file) is inconsistent and needs checking on actual devices, not assumed from desktop behavior.
  - Note this is distinct from the earlier "Site-wide uniformity audit" task above — that one is about consistency across pages regardless of screen size; this one is specifically about narrow/touch viewports.

- [ ] **Site-wide uniformity audit: how a page relates to its position in the site (~6h)**

  A general consistency pass across every page family (`open-problems/**`, `papers/**`, `surveys/**`, `resources/**`, `uc/**`, `c/000N`, `prompts/**`), not tied to one specific page. Three concrete dimensions:

  - **Names matching the links that lead to them.** A sidebar/navbar label and the destination page's own title should read as the same thing once you click through — this has already been fixed once for the Papers section (Archive/Committee vs. Example Paper/Programme Committee); check the rest of `_quarto.yml` and every section index for the same drift recurring.
  - **Sub-links listed on each page.** A section's own index page should list links to its children the same way everywhere — `index.qmd`'s "Explore" grid and `papers/index.qmd`'s "Browse" links (Archive/Committee) are the current model; check whether `surveys/index.qmd`, `resources/index.qmd`, `open-problems/index.qmd`, and `uc/index.qmd` all surface their sub-pages the same way, or whether some just rely on the sidebar and say nothing in the body.
  - **Look and feel across pages.** `page-layout`, `title-block-banner`/`title-block-style`, and related metadata should be applied consistently rather than page-by-page as an afterthought (a version of this was fixed once already for the Papers page specifically) — worth a real side-by-side visual comparison, both themes, rather than just diffing frontmatter.

- [ ] **Add a "Proposals" section under Papers (~1h)**

  `papers/index.qmd`'s "## Browse" section currently links to two things: [Archive](/papers/example-paper/index.qmd) and [Committee](/papers/programme-committee/index.qmd) (`_quarto.yml:69-73` mirrors the same two under the Papers sidebar section). Add a third: "Proposals" — a place for paper ideas/topics worth writing up but not yet claimed by anyone, the papers analogue of an open conjecture. Needs a new `papers/proposals/index.qmd` (mirroring the `example-paper`/`programme-committee` pattern), a third `_quarto.yml` sidebar entry, and a third Browse link. Exact scope (a simple list vs. something with its own per-proposal pages) is an open call — decide when picked up.

- [ ] **Convert the UC-for-gamers paper to HTML (~5h)**

  Needed as a prerequisite (or at least a shared source) for the interactive UC tutorial task below: that tutorial quotes functionality excerpts from the paper, and an HTML version is what makes those excerpts reusable as live web content instead of screenshotted PDF pages.

  - The main conversion risk is the paper's heavy custom LaTeX: `tcolorbox` (the property/game boxes, saturated header + coloured body), `algpseudocode` (the operation listings), and extensive `\hypertarget`/`\hyperlink` cross-referencing (line numbering across shell/finalization boxes, `\opdef`/`\op` targets) — none of these survive a naive converter untouched. Check LaTeXML and `make4ht`/tex4ht against a representative box (e.g. one of `F-Net`, `F-AC`, `G-Clock`) early, before committing to a toolchain, to see which one preserves the box styling and internal hyperlinks rather than flattening them to plain text.
  - Whatever the box markup degrades to in HTML, math and cross-reference links must not: the per-box line numbering and cross-box hyperlinks are load-bearing for how the paper is read, so a conversion that silently drops or renumbers them is a regression, not an acceptable simplification.
  - Decide up front whether the target is (a) one faithful HTML mirror of the whole paper, or (b) just the excerpted figures/boxes the tutorial task needs pulled out individually — the two have very different toolchains (whole-document converter vs. per-box snippet export) and it's worth picking before starting rather than defaulting into whichever is easier to try first.

- [ ] **UC Encyclopedia content (~28h)**

  93 of the 100 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, and F-AC are now filled in, ported from `surveys/uc-for-gamers/latex/main.tex`). Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. No other functionality currently has a ready-made source of this quality to adapt from, so expect this to mean drafting from the literature directly rather than porting.

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
