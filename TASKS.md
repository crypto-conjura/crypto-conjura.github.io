# Tasks

Split into four sections. **Credibility and distribution** (~8.5h) covers review, prior-art checking, external addressability and the two unkept promises on the [Philosophy](/about/) page — it is first because the project's binding constraint is there rather than in content supply; **Website and repository** (~5.5h) covers the site, its build tooling and the repository's configuration; **Formalizations** covers machine-checked artifacts; **Conjectures and papers** (~4.5h) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~26.5h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `cbb23c7` on 18 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

## Credibility and distribution

Added 18 August 2026 from an outside strategic review of the site, supplied in
full. Its central argument is structural and worth stating before the tasks,
because it is an argument *about this file*: the binding constraint on the
project is not content supply, and until today the backlog was almost entirely
content supply. The two pull against each other — every page the unreviewed
pipeline adds enlarges the surface that the "AI-generated, not independently
reviewed" notice has to cover, so the corpus's liability grows while its
credibility does not. This section is placed first for that reason.

**What was checked against the repository on 18 August 2026**, since the review
supplied numbers and several had drifted or were slightly off:

- *Confirmed.* 0 stars, 0 watchers, 0 forks, 0 open issues. Exactly one of the
  statements carries a non-open badge (`c/0004`), and `proof_review: ai` on
  **all** of them — no statement has been read by a human. `papers/reviews/` is
  still a placeholder saying no committee has formed. GitHub Discussions is
  **disabled** on the repository. The Philosophy page does call session logs
  "the one promise still unkept" while `schema/index.qmd` records them as
  "excluded from the site" — the contradiction the review names is real.
- *Drifted upward, not wrong.* 388 commits, not 371; 29 statements, not 28.
- *Corrected.* `conjura.json` is **not** undocumented: it is described in
  `README.md`, `CONTRIBUTING.md` and `schema/index.qmd`, and it is served —
  `https://crypto-conjura.github.io/conjura.json` returns 200 and 70 KB. What
  it actually lacks is a version envelope (its top-level keys are bare
  statement ids), immutable snapshots and a citation stanza. And session logs
  are on disk for **9 of 29** leaves, not for each one.
- *Context the review omits.* **The repository was created on 13 August 2026**,
  five days before the review. Zero stars on a five-day-old repository is a
  much weaker signal than zero stars on an established one, and the
  recruitment items below should not be justified by that number.
- *Not verified here, and load-bearing.* The Erdős figures (700 problems, 13
  addressed, 4 novel, 9 already in the literature), the `formal-conjectures`
  counts (2,615 / 1,029 / 836), the August 2025 comments date, and the FOCS,
  ICML and ICLR 2026 policy summaries are all repeated from the review on its
  own authority. Check each at source before any of it reaches a page —
  the same rule the rest of this site is held to.
- *Verified at source.* `google-deepmind/formal-conjectures` exists, is active
  (pushed 17 August 2026, 1,185 stars), and its `FormalConjectures/` tree has
  directories for Erdős, OEIS, Green, Hilbert, Kourovka, Litt, Millennium and
  quantum problems and **none for cryptography**. Its README states the
  discipline verbatim: "Tags are immutable: fixes to misformalizations are
  never patched into an existing benchmark version but instead go into
  `v{N+1}`."

- [ ] **Ask the seven steering members for one review each (~1h of our time — manual: seven real people, and whether they reply is not ours to control)**

  The sharpest number on the site is that `proof_review` is `ai` on all 29
  statements. Seven established cryptographers already back the project on
  `support/index.qmd`, and the ask that converts a name into a review is not a
  committee seat but one statement in that person's own area — bounded, and
  completable by a busy person in an evening. The review's suggested pairings,
  which match the areas on each statement page:

  - **Groth** — `c/0008` / `c/0009`, the split-NILP and Groth16 optimality pair.
    His own EUROCRYPT 2016 paper posed the 2-element question as its closing
    open problem, which makes this the least presumptuous ask on the list.
  - **Tessaro** — `c/0001` (6-round Feistel indifferentiability) and `c/0002`
    (generalized mirror theory).
  - **Mahmoody** — the twelve statements at `c/0019`–`c/0030`, every one of
    them harvested from a paper he co-authored. Ask for one, not twelve.
  - **Rechberger** — `c/0012`, the censored-cipher transfer statement.
  - **Barbosa** and **Firsov** — the Lean artifact on `c/0004`, the one
    statement that is formalized and matched.

  Seven of twenty-nine reviewed is the difference between an archive that can
  be cited and one that cannot. Before sending anything, read the badge
  semantics in `open-problems/status-legend/` so the ask names exactly which
  flag a review moves and what it does not claim.

- [ ] **Sweep every statement for a prior resolution already in the literature (~3h — manual: a real literature search per statement, and the failure mode is a false negative)**

  The review's most useful borrowed finding is that on erdosproblems.com
  "open" status tracked *obscurity* rather than difficulty — most of what a
  large model resolved there turned out to be already solved in the
  literature. Conjura is more exposed to this than that list is, because its
  statements are harvested from other papers' open-problem sections, and an
  open-problem section ages from the day it is printed. Twelve of the
  twenty-nine — `c/0019`–`c/0030` — were promoted in a batch on 18 August 2026
  from eight source papers, and none has had a forward-citation check.

  Do this before spending compute on attacks, not after. It is cheap, it is
  publishable on its own if it finds anything, and it forecloses the failure
  the site could not recover from: announcing a resolution of something that
  was already known. For each statement, follow citations *forward* from the
  source paper rather than searching the statement's own wording, since a
  resolution rarely reuses the phrasing of the question.

- [ ] **Make the archive externally addressable: version `conjura.json`, then upstream the Lean statements (~1.5h)**

  Two halves, and the first is nearly done already. `conjura.json` is built by
  `scripts/build_index.py`, gitignored, and published at
  `https://crypto-conjura.github.io/conjura.json` (200, 70 KB, 29 entries). It
  is documented in `README.md`, `CONTRIBUTING.md` and `schema/index.qmd`. What
  it lacks is what makes a file citable: its top level is bare statement ids
  with no envelope, so there is no schema version, no generation timestamp, no
  snapshot tag and nothing to cite. Add the envelope, publish immutable
  snapshots, and put a citation stanza on `schema/index.qmd` next to the
  description that is already there.

  Copy the versioning discipline from `formal-conjectures`, whose README says
  it plainly: tags are immutable, and a fix to a misformalization goes into the
  next version rather than being patched into an existing one. That rule exists
  because a benchmark that is silently corrected is not a benchmark, and it is
  the same reason `CONTRIBUTING.md` already has a same-id-versus-new-id rule.

  The second half is the one with an audience attached. `formal-conjectures`
  has directories for Erdős, OEIS, Green, Hilbert, Kourovka, Litt, Millennium
  and quantum problems, and none for cryptography — checked 18 August 2026.
  Upstreaming the Lean statements under a cryptography directory costs nothing
  the project is not already paying, and reaches exactly the audience the
  benchmark argument on the [Philosophy](/about/) page depends on. Read their
  contribution guide first; a rejected PR is worse than none.

- [ ] **Lower the contribution floor below "open a pull request" (~1h)**

  Confirmed on 18 August 2026: **GitHub Discussions is disabled** on the
  repository, so there is currently no way to say anything about a statement
  short of a pull request. The review's evidence is that per-problem discussion
  — not the catalogue — is what accumulated contributors on erdosproblems.com,
  and it is the single cheapest thing on this list.

  The friction is worse than it looks. `revision` and `statement_sha` are
  script-maintained, `CONTRIBUTING.md` says so, the repository ships a
  `.githooks/pre-commit`, and a stale hash fails the whole site build — the
  gate that took the deploy down for ~25 commits on 15 August 2026. A
  cryptographer will leave a remark on a page. They will not clone a Quarto
  site, install a git hook and regenerate a badge to do it.

  Enable Discussions, embed a per-statement thread on each `/c/<id>/` page, and
  decide the AI-disclosure norm at the same time rather than later. The review
  reports that Bloom settled on *disclosure plus verification* rather than
  prohibition, on the reasoning that a ban is unenforceable and drives the use
  underground — which is the position this site's badge system already takes
  for its own content, so adopting it for comments is consistent rather than
  novel.

- [ ] **Publish the session logs, and fix the contradiction about them (~1h)**

  The [Philosophy](/about/) page calls session logs "the one promise still
  unkept"; `schema/index.qmd` records that they "still live in each leaf's
  `sessions/` folder for provenance (excluded from the site)" as a settled
  design choice. Those two sentences cannot both stand. Decide which, and edit
  the other — that decision is the task, and it is smaller than it looks
  because the logs are already on disk.

  Two facts to size it with. They exist for **9 of the 29** leaves, not all of
  them, so publishing them makes an uneven record visible and the pages should
  say so rather than imply the other twenty had no session. And publishing is a
  redaction question before it is a configuration one: a session log is a raw
  transcript and nobody has read these with an eye to what is in them.

- [ ] **Fund one bounty end to end (~0.5h of our time — manual: the amount, the money and the adjudicator are the maintainer's call, not ours)**

  The [Philosophy](/about/) page has intended from the start "to let anyone
  attach a bounty payable once a resolution is verified rather than when a
  committee has met", and no bounty exists. The review's argument for doing one
  now at any amount is that a working instance settles questions a general
  scheme cannot: who adjudicates, what counts as verified, what happens on a
  disputed claim. Name a human adjudicator, pick the statement, and write down
  the rule before there is money on it.

- [ ] **Stress-test the venue positioning on the Philosophy page (~0.5h — manual: three policies to read at source, and they change)**

  `about/index.qmd` rests its stance toward venues on the ACM policy's
  requirement that a work be "not primarily the result of the tool's generative
  capabilities", read at source on 16 August 2026, and says several results
  here cross that line on purpose. The review's counter is that 2026 norms
  converged on *disclosure plus human accountability* rather than prohibition,
  and that none of FOCS, ICML or ICLR 2026 bars a heavily AI-assisted result
  that a named human vouches for — so the site's badge system already exceeds
  what the venues demand, and positioning the project as *more* transparent
  than they require is a better recruiting pitch than positioning it outside
  them.

  That argument is worth taking seriously and its evidence is **unverified
  here**: read the FOCS, ICML and ICLR 2026 policies at source before a word of
  it reaches the page, and keep the ACM sentence, which was verified. If the
  policies say what the review says they say, the rewrite is a repositioning
  and not a retraction — the site would still be doing more than any of them
  ask.

## Website and repository

- [ ] **Revisit "Supporting the project" against the project roadmap (~0.5h)**

  Requested 18 August 2026, with a roadmap supplied in the request: the
  project's aim is to move from *a repository of AI-generated content* to *a
  reliable platform of verified cryptographic research*, under three headings —
  **strengthen verification** (formalization in Lean; a structured,
  community-led peer review run through GitHub), **deepen the research core**
  (expand the UC encyclopedia; complete book-length surveys that map subfields
  and show how conjectures connect), and **refine AI tooling**.

  **The third heading arrived truncated** — the request ends mid-sentence at
  "Conjura's unique angle is it" — so that bullet is not yet specified and this
  entry should not be run until it is. Ask before starting.

  `support/index.qmd` § "Supporting the project" is today a six-item list
  ordered *by how scarce each kind of help is*: reviewing, conjecture
  formulation and resolutions, formalizations, website and workflow
  maintenance, tokens, ideas. Checked against the roadmap, four of the six
  already carry it and two gaps are real:

  - Roadmap 1a (formalization) is item 3, and 1b (human review) is item 1 —
    both already the top of the list, and item 1 already says most statements
    have never been read by a person. Nothing missing but emphasis.
  - Roadmap 3 (AI tooling) is item 4, which mentions "the scripts and prompts
    behind it" but reads as ordinary site maintenance. Sharpening it is
    probably where the truncated bullet lands.
  - **Roadmap 2a and 2b have no item at all.** Neither the UC encyclopedia nor
    the surveys is mentioned anywhere in this section, though both are the
    largest bodies of work on the site — 104 functionality pages and
    `surveys/uc-for-gamers/`. That is the substantive addition.

  **The editorial decision to make first**, because it changes the shape rather
  than the wording. The existing list answers "what can *I* do", ordered by
  scarcity; the roadmap answers "where is the *project* going", ordered by
  theme. Merging them turns a list of asks into a list of goals and loses the
  scarcity ordering, which is the thing that makes the list useful to someone
  deciding where to spend an afternoon. The alternative — keep the six asks as
  they are, add a short roadmap above or beside them, and have each ask point
  at the part of the roadmap it serves — preserves both, at the cost of a
  longer page. Recommend the second; decide it explicitly either way.

  Two factual errors on the same page to fix while it is open, neither of them
  about this section. **Mohammad Mahmoody is listed as "Bilkent University"
  while his own entry links to `cs.virginia.edu`** — the label and its own link
  disagree, and his homepage says the University of Virginia. **Jens Groth's
  link is `http`-only** (`http://www0.cs.ucl.ac.uk/staff/j.groth/`), a
  mixed-content nag from an `https` site, and he is the one name carrying no
  affiliation.

  What the rewrite must not drop, since it is why the wording is careful: that
  support is not an endorsement or a review of any statement, that reviews are
  recorded only in the [provenance badge](/open-problems/status-legend/), that
  anyone listed can ask to be removed without giving a reason, and the pointer
  to [Philosophy](/about/) for the compute-not-budget argument.

- [ ] **Decide what `latex/uc/` is for, then retire or reconcile it (~0.5h)**

  Requested 18 August 2026, as "publish new UC pages". Investigating it turned
  up that the thing being asked for cannot currently be done, and that the
  reason is worth fixing on its own.

  `latex/README.md` documents a publishing step for UC entries — "regenerate
  `uc/layer-N-.../<slug>/index.qmd` from the matching
  `latex/uc/layer-N-.../<slug>/main.tex`" — and `latex/uc/README.md` says to
  write the real content into those pre-made files. Neither has ever happened.
  `latex/uc/` has exactly **one commit in its history** (`4ace801`, the one
  that started tracking `latex/` at all), and all 100 `main.tex` files are
  byte-identical 52-line skeletons: title filled in, five sections stubbed out
  as comments, nothing written.

  Meanwhile every entry that *is* written was written by a completely
  different route, the one `prompts/source.md` and `CONTRIBUTING.md` describe:
  `uc_source.py` harvests the sources, the prose goes straight into
  `uc/.../index.qmd`, and the interface box is generated by
  `gen_interface.py` from a fragment in
  `surveys/uc-for-gamers/latex/functionalities/<id>.tex`. `latex/uc/` is not
  read at any point. So the two pipelines do not merely differ — publishing
  from `latex/uc/` today would overwrite every written page with an empty
  skeleton.

  Three symptoms of the same drift, all cheap to fix once the decision is made:

  - `scripts/artifact_manifest.py` describes `latex/uc/**` as "the
    encyclopedia interface boxes ... `gen_interface.py --check` already
    regenerates those from their fragment". That is a description of
    `surveys/uc-for-gamers/latex/functionalities/`, not of `latex/uc/`, which
    holds article-style drafts the generator never opens. The exclusion is
    still right; the reason given for it is not.
  - Four site entries have no draft folder at all — `f-rand`, `f-store`,
    `f-ac`, `f-net`. Those are the four added in `464314c` when they were
    ported from the book, after the 100 skeletons were generated, so the
    "exact 1:1 correspondence" `latex/uc/README.md` promises is already 100
    against 104.
  - Nothing watches the divergence. `draft_status.py` globs
    `latex/conjectures/` only, so a staging area that has silently stopped
    being the source of truth is invisible to every gate — which is precisely
    the failure mode that script's docstring exists to describe, one folder
    over.

  The decision is editorial, not technical, and it is the author's:

  **Retire it.** Delete `latex/uc/`, drop its two README paragraphs, and say
  in `latex/README.md` that UC entries are written directly to the site page
  by `prompts/source.md`. This matches what has actually happened for every
  written entry, and removes 100 files that can only ever mislead. Cheapest,
  and the recommendation unless the drafts folder is wanted for something.

  **Reconcile it.** Keep it as a real staging area: add the four missing
  folders, and make `prompts/source.md` write the draft first and the page
  from the draft. This buys a per-entry LaTeX artifact the site does not
  currently keep — worth something, since conjectures and papers both keep
  theirs — at the cost of a second write per entry, 86 times over.

  Either way, fix the `artifact_manifest.py` docstring, and if the folder
  stays, extend `draft_status.py` (or a sibling) to report UC drafts that
  never became pages, so this cannot drift silently again.

- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  61 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs, one is marked *No canonical definition*, and forty-two are written — measured 18 August 2026. Run `python3 scripts/uc_status.py --check` for the current split rather than trusting these numbers. Written so far: the seven ported from `surveys/uc-for-gamers/latex/main.tex` (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, F-AC), then F-CRS, F-COM, F-ZK, F-auth, F-OT, G-RO, then — 17 August — F-smt, F-MCOM and F-BC, and — 18 August — F-CERT, F-ACRS, F-PKI, F-syn, F-KR, F-CP, F-COT, F-RBC, F-SA, F-wrap, F-ABA, F-diffuse, F-PKE, F-rPKE, F-aPKE, F-pwKE, F-OLE, F-coin, F-beacon, F-BlSig, F-VRF, F-TLP, F-clocksync, F-nettime, F-LSC and F-OPRF, plus F-SFE as *No canonical definition*.

  The tooling for this now exists end to end, so this is a matter of running it 97 times rather than inventing the process each time:

  - `scripts/uc_source.py <id>` does the mechanical half. It reads the page's own reference bullets, resolves each to a PDF (newest ePrint revision, falling back to the PostScript-only postings the 1990s papers still are), records every revision stamp, scans the text layer for interface-box titles, renders the pages carrying a box named after the functionality into `<id>/_src/`, and writes `<id>/_src/sources.json` with URL, revision, page and a ready-made citation pointer. The PNGs are gitignored — a proceedings figure is the publisher's — and `_src/` is `_`-prefixed so Quarto never publishes it; the manifest is committed and reproduces the images exactly.
  - `prompts/source.md` is the per-stub prompt, rewritten 16 August 2026 around that harvest: choose among the cited definitions in a fixed order (same object first, then revision/formulation/framework currency, then a tie-break ladder), capture the original as reviewer evidence, rewrite it in the book's notation, keep a mismatch register.
  - `scripts/gen_interface.py` turns the `.tex` fragment into the page's box with the line numbering computed and CI-gated, and `--vs-preview` compiles a fragment standalone to prove LaTeX prints the line numbers the generator computed — the check `--vs-pdf` cannot do for the 97 boxes the book does not typeset.

  Three things the runs so far have established, worth knowing before the next one. **A stub's own citations are often not where the definition is printed**: F-BC's three references include Canetti's framework paper, which prints no broadcast box at all, and the definition taken came from the two adaptive-broadcast papers instead. **A citation that yields no box is a result, not a gap** — Rabin 1981 contains no `F_OT` because it predates ideal functionalities, and Pfitzmann–Waidner's secure message transmission is an ideal *system* in the reactive-simulatability model, not a UC functionality; both pages say so. And **F-SFE has no printed box under that name** in either paper it cites (`uc/layer-6-secret-sharing-mpc/f-sfe/_src/sources.json` records that CLOS 2002 prints F_bc, F_cp, F_mcom, F_ot and F_zk, and no F_sfe), so that entry needs a forward literature search before it can be written, or a page saying the functionality is folklore.

  **The pool of small clean boxes is exhausted.** Everything still unwritten is one of: a multi-page functionality (`g-ledger`/`f-ledger`, `f-cgka`, `f-sapake`, `f-chan`), a paper printing no box the scan can find (most of layers 2 and 7), or a stub citing nothing at all (the eleven listed below). Batches from here on should expect to take a large entry or resolve a naming question, not to find an easy transcription.

  **"No canonical definition" now has a worked example: `f-sfe`.** The page shows the harvest that establishes the absence, rules out the three extraction failures seen earlier, explains why a compiler theorem has nothing to draw a box around, and gives the two routes out (find a paper that prints it, or retire the slot). Use it as the template for the other stubs whose sources genuinely print nothing — `f-ro`, `f-eqv`, `f-nizk` are the immediate candidates, all three harvested and recorded.

  **Stub titles are wrong so often that reading the source first is now the rule, and titles are not the only field affected.** Three ePrint postings have turned out to carry titles different from the ones their stubs cite — the ECVRF paper, and ePrint 2019/838, whose title page reads *"Ouroboros Chronos: Permissionless Clock Synchronization via Proof-of-Stake"* against the stub's *"Dynamic ad hoc clock synchronization"*. Authors matched in every case. Check the title page, not just the venue.

  **Ticked functionalities need a declared translation.** Papers from the TARDIS/CRAFT line define time through a *global ticker* plus an inbox/outbox pair, with an explicit `Tick` interface the ticker drives. This framework has no ticker and delivery is a pull, so the countdown is decremented by the recipient's own call — the translation `F-diffuse`, `F-beacon` and `F-TLP` all make. The accounting survives; *who drives the clock* does not, and the page must say so.

  **One entry is deliberately stronger than its source, and says so: `F-TLP`.** The printed functionality leaks the message after $\\epsilon\\Gamma$ steps, conceding that an adversary with more compute than the honest solver arrives early. Modelling that needs a per-party step counter and a second parameter. It is omitted, so a protocol proved against the source is **not** proved against this box. If any other entry ends up in that position, state it on the page the same way.

  **A stub that does not exist is also a gap.** The CRAFT harvest turned up a printed, unclaimed $\\mathcal{F}_{\\textsc{vdf}}$ — verifiable delay functions — and the site has no `f-vdf` page to put it on. Worth a pass over the stub list against the functionalities the harvested papers actually print, rather than only the reverse.

  **A fourth false-negative mode, and it invalidated this file's own triage.** The box may be printed in a paper the stub does not cite. This entry recorded `f-pke` as having no printed definition; in fact Canetti–Krawczyk–Nielsen print $\\mathcal{F}_{\\textsc{pke}}$, and the page simply cited three papers that do not. A "no box found" result is a statement about *the references on the page*, never about the literature — so before believing one, ask who else would print this object.

  **Two entries are ready and were passed over on size, beyond the ledger pair.** `f-cgka` ($\\mathcal{F}_{\\mathsf{cgka}}$ across three pages of the MLS insider-security paper) and `f-sapake` (OPAQUE's Fig. 2, six labelled sections with a marked diff against its predecessor). Both want a sitting of their own. Note also that OPAQUE prints the *strong* asymmetric variant only; plain $\\mathcal{F}_{\\mathsf{aPAKE}}$ appears there under its older name and would have to be sourced separately.

  **Two entries need a decision before they can be written**, both recorded in the triage commits. `f-leak`: Micali–Reyzin print no functionality at all — physically observable cryptography is a model, not a UC notion — and the nearest printed object is a leakage-tolerant *channel*, so the page is either retitled or becomes the site's first "No canonical definition" entry. `f-nettime`: the best match is an attackable approximate clock printed as $\\mathcal{G}_{\\mathsf{clock}}$, which collides with the site's existing `g-clock` page from the book — a different object under the same name.

  **The most reliable finding so far: a stub's title is usually wrong.** Nine of the twelve entries written on 18 August had to be retitled, and the errors are not cosmetic — F-syn said "Bounded-delay network", a property the object provably lacks; F-rbc said "Reliable broadcast" where the printed box is *relaxed* broadcast, a different notion weakening a different property; F-CERT named a different box in the same paper. Others named the role rather than the printed functionality (F-split, F-diffuse, F-REG/F-KRK) or implied the wrong scope (F-PKI, F-COT/F-ROT). Read the title against the source first; it is a claim, not a label.

  **`gen_interface.py` expands every fragment's macros on every run**, so a batch cannot be split one-entry-per-commit unless each commit carries all of the batch's macros. The pre-commit hook rejects the intermediate states, correctly. Either land all the macros in the batch's first commit, or land the batch as one commit.

  **Two entries are ready and were passed over on size.** `g-ledger` and `f-ledger` both point at the same printed object, `G_ledger`, which is a multi-page functionality with its variables in a separate figure — a sitting of its own, not a slot in a batch. Note also that the site has two pages for one printed box, so one of them should say so or go, and that the source argues global-versus-local is a fact about *use* rather than a type a functionality carries — which bears directly on this site's `f-`/`g-` convention.

  **Three ways a harvest reports a false negative**, all three now seen. A box whose name carries a diacritic does not match the scan ($\\bar{\\mathcal{G}}_{acrs}$, F-ACRS). A page id that names *two* functionalities matches neither printed box (F-COT). And a paper whose mathematical glyphs do not survive the text layer reports "no boxes at all" while its figures are perfectly legible in the rendered page — Barak–Canetti–Nielsen–Pass extracts as "The key registration functionality, , is presented in Figure 2", and F-KR was transcribed from the image. Before concluding a cited paper prints nothing, check whether its extracted *prose* has holes in it.

  **Check the paging on every source.** Three of the five 18 August sources number their printed pages differently from the PDF: ePrint 2000/067 runs three behind, 2002/140 two behind, 2006/432 one behind, and 2003/239 and 2020/924 agree. A pointer copied from `sources.json` unexamined sends a reader holding the paper to the wrong page, so both numbers belong on the page.

  **A stub's title is a claim, and five of seven were wrong.** F-CERT said "Certification authority" (a different box in the same paper), F-ACRS carried an unsourced "sunspots" gloss, F-syn said "Bounded-delay network" (a property the object does not have, and the subject of the published criticism of it), F-PKI read as the directory when its box serves one party, and F-REG/F-KRK named two functionalities neither cited paper prints. Read the title against the source before trusting it as the seed.

  Two findings from the 18 August pair, both about the harvester rather than the mathematics. **A missing box may be a false negative.** `uc_source.py` matches the printed heading, so a functionality typeset with a diacritic in its name does not match: $\\bar{\\mathcal{G}}_{acrs}$ is printed in the GUC paper and the scan reported none, because the combining macron does not survive the text layer as the plain name. When `boxes_in_paper` lists neighbours but `boxes_matching` is empty, read the pages around the neighbours before concluding the paper prints nothing. **And check the paging.** The GUC paper's printed page numbers run one behind the PDF's own, so a pointer taken from `sources.json` unexamined sends a reader holding the proceedings to the wrong page; both numbers belong on the page.

  A stub's title is also a claim. F-CERT's said "Certification authority", which is a *different* functionality in the same paper, and F-ACRS's carried a "sunspots" gloss that appears in neither the cited paper nor any of the 107 harvested PDFs. Both were corrected when the entries were written. Read the title against the source before trusting it as the seed.

  One earlier fact still stands: 11 of the stubs cite nothing at all (F-RP, F-CRHF, F-MHF, F-OWF, F-PRG, F-ABE, F-IBE, F-GC, F-ORAM, F-PIR, F-PSI), so they need a literature search before the harvester has anything to work with; and a citation that yields no box is a normal, informative result — Rabin 1981 contains no `F_OT`, because it predates ideal functionalities, and the page should say so rather than force one.

  **Decided 18 August 2026: one bulk harvest first, then write the entries one
  at a time.** The two halves have opposite economics and the decision is only
  about the first. `uc_source.py` already caches every download in
  `~/.cache/conjura-uc-sources` and hits a given paper once rather than once per
  run, so `--all` is not a speed optimisation — pre-fetching costs nothing that
  writing entry-by-entry would not pay anyway. What it buys is *triage in one
  pass*: the 88 stubs cite **102 distinct URLs, 65 of them ePrint and 37 on
  personal homepages, publisher sites and one-off hosts**, and that second group
  is where dead links, paywalls and PostScript-only postings live. Each one
  discovered mid-write is an unrelated detour dropped into the middle of a
  mathematical judgment call. Harvest first and the entire failure set — dead
  URLs, papers that print no box under the name at all (the F-SFE finding), and
  the 11 stubs citing nothing — is a work-list *before* any writing starts, when
  it can be cleared in one literature-search sitting.

  Do **not** extend that to the writing. Choosing among incompatible variants and
  keeping a mismatch register is per-entry judgment, and batching it is how a run
  of 88 pages turns into plausible-sounding filler. The harvest is mechanical and
  can land as one commit (77 `sources.json` manifests, plus roughly 1 MB of
  gitignored PNGs per entry — about 80 MB of untracked `_src/` images); the prose
  stays one entry per commit.

  One thing to fix before pointing it at everything: `uc_source.py` contains no
  delay between downloads — no `sleep` anywhere in the file — so `--all` fires
  ~102 requests back to back at ePrint and three dozen other hosts. Add a small
  per-request pause, or run it in `--limit` batches.

  What the estimate is still carrying is the part the tooling cannot shortcut: choosing between incompatible variants, and verifying every citation is a real paper at a real venue in a real year. Expect the mismatch registers to be the most interesting output, and expect some functionalities to have no canonical printed definition at all — that finding is itself a page worth having.

  One ordering trap, which turns CI red for the whole site: `gen_interface.py --check` runs in both workflows over every fragment in `functionalities/` and errors if a fragment's page has no `.cj-interface` block to replace. The page scaffold and the fragment must land in the same commit.

## Formalizations

- [ ] **Formalize the proof of LHL extraction, public seed (~8h, highly uncertain: real formalization, and one item is a project on its own)**

  `c/0004` is the only resolved statement on the site, and its proof is the obvious next artifact: the statement is formalized and matched, `Proof.lean` is 476 lines with no `sorry`, and everything is in place except the theorem itself. `c/0004/lean/Statement.lean:134` holds the single real `sorry`, on `Conjura0004.lhl_public_seed`. Discharging it is what moves `status.proof_formal` off `open`, and by the discipline recorded in `LEDGER.md` nothing else may move it.

  Do not re-derive the plan. `c/0004/lean/LEDGER.md` already lists what is proved and what is outstanding, in dependency order, and it was written to be picked up:

  - Items 1 to 3 are groundwork: dropping `[Fintype Z]` in favour of `tsum`, the second half of Lemma 3.1 (factoring the view distance as an average over rows, which is where publishing the seed does its work), and the attainment half of the predictor bound.
  - Items 4, 5, 7 and 8 are the flattening argument, the mean at fixed support, the uniform deviation bound and the final assembly.
  - **Item 6 is the one to size the task by.** Fact 2.2, bounded differences, in the finite special case. The ledger calls it "the single largest item, and the one Mathlib does not help with at all", and that was checked: Mathlib has no McDiarmid inequality and no bounded-differences lemma. It is a formalization project in its own right and could exceed the estimate for everything else combined.
  - Seven supporting facts are named and unattempted. Fact 2.5 is Jensen and is in Mathlib; Fact 2.7 needs the monotonicity of $(1-1/R)^R$ and is not the one-liner it looks like.

  **Consider doing item 6 as a Mathlib contribution rather than an in-repo lemma** (added 18 August 2026 from the strategic review). Bounded differences / McDiarmid is absent from Mathlib, which is why the ledger calls it the sizing item; that absence is also what makes it worth upstreaming. It converts the largest private item on this list into an externally reviewed artifact and a route into the Lean community, which pays down the review deficit in the one currency that is actually available. It will be slower than an in-repo proof, and that is the trade to weigh.

  Toolchain is pinned: `leanprover/lean4:v4.33.0`, Mathlib at the revision in `lake-manifest.json`. Keep `AuditProof.lean` passing throughout, since its entire purpose is that no declaration quietly acquires `sorryAx`, and update `LEDGER.md` as items close rather than at the end. Partial progress is worth committing: the ledger is designed for it, and an honest "items 1 to 3 done, 6 untouched" is more useful than nothing.

## Conjectures and papers

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
