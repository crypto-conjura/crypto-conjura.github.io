# Tasks

Split into three sections. **Credibility and distribution** (~4.5h) covers review, prior-art checking, and — as of 19 August 2026 — the legal/security/governance items below; it is first because the project's binding constraint is there rather than in content supply. **Website and repository** (~25.5h) covers the site, its build tooling, the repository's configuration, and the product/data-model redesign added 19 August 2026. **Conjectures and papers** (~20.5h, plus one unbounded item added 19 August 2026 — see below) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty, *except* where noted: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools, anything needing a lawyer or a GitHub org owner) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~50.5h** (rough; the UC Encyclopedia content, the new data-model item, the new harvest-and-promote item and the Persian translation added 23 August 2026 all dominate the uncertainty — the last of these has no meaningful estimate since 1,066 unread PDFs are waiting and the count of conjectures they'll yield is unknown until it's run).

Tasks added 19 August 2026 come from `maintainer-brief.md`, a compact maintainer brief (Jens, 18 August 2026) arguing Conjura's product should be a living AI-native record of open problems — pose → investigate → record progress → verify → preserve — evaluated on evidence rather than origin, with a visibly separate vetted archive and incubator lane. Within the two sections it touches, its tasks are ordered by *leverage and risk* rather than difficulty: cheap legal/security/governance fixes first, then the data-model work everything else (problem cards, the canonical page, admission) depends on, then the website/IA changes themselves. This pushes UC Encyclopedia content — the largest existing item — to the end of its section, consistent with the standing argument above that content supply is not the binding constraint.

Last reconciled against `main` at `4cd26ae` on 19 August 2026. The prior-resolution sweep is done as of this reconciliation: 6 statements (c/0018, c/0026, c/0027, c/0037, c/0038, and c/0046 from an earlier pass) turned out to already be resolved and are now marked accordingly; the other 37 are confirmed still open, each with a dated literature-check note on its own page.

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
  **all** of them — no statement has been read by a human. `reviews/` is
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

- [ ] **Get a trademark/legal opinion on the name "Conjura" before investing further (~0.5h to commission — manual: needs an actual lawyer; not executable by the model)**

  Flagged in the 19 August 2026 maintainer brief: "Conjura" has a material conflict risk with an existing exact-name AI/software business and with the nearby CONJUR security mark, and a new trademark filing would not defeat earlier rights — this should be resolved (or at least scoped) before renaming is expensive to undo. The brief separately asks for legal review of contributor rights, licenses, privacy, and the project name; bundle all four into one engagement rather than running it four times. The model's part is limited to drafting the questions for counsel and identifying what would need to change (name, domain, branding) if the opinion comes back negative — the opinion itself is external and not something to simulate.

- [ ] **Harden account and disclosure security (~1h — manual: MFA and org-owner changes need an actual GitHub org owner logged in)**

  From the same brief: strong MFA, multiple organization owners, branch protection, reviewed deployments, and a tested recovery process, plus a private responsible-disclosure channel for security-sensitive submissions (the brief lists account compromise and security-sensitive disclosures among the project's principal risks). The model can draft the branch-protection ruleset, the disclosure-channel text/`SECURITY.md`, and a recovery-test checklist; actually flipping the GitHub org settings needs a human with owner access.

- [ ] **Publish the site's governance rules and a privacy notice (~2h)**

  The brief asks for explicit, published rules for acceptance, verification, correction, retraction, attribution, and appeal — none of which exist today as a standalone page — plus an inventory of personal-data flows and a factual privacy notice. This is what lets editorial states like "Contested" and "Retracted" mean something specific rather than being ad hoc calls, and it should land before the admission/status-model work below so that work has rules to implement rather than invent.

- [ ] **Ask the seven steering members for one review each (~1h of our time — manual: seven real people, and whether they reply is not ours to control)**

  The sharpest number on the site is that `proof_review` is `ai` on all 29
  statements. Seven established cryptographers already back the project on
  `participate/index.qmd`, and the ask that converts a name into a review is not a
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
  semantics in `problems/status-legend/` so the ask names exactly which
  flag a review moves and what it does not claim.

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

  **Superseded 19 August 2026, read this before the rest of this entry.**
  `participate/index.qmd` § "Supporting the project" was rewritten the same day
  on direct instruction, to different supplied copy — dropping the scarcity
  ordering this entry was written against, and dropping the "cost of
  attacking a problem should come down to compute anyone can bring" sentence
  entirely (confirmed intentional, not an oversight, when asked). The
  six-item analysis immediately below is against the *old* text and needs
  re-checking against the new one before this entry is run; the "must not
  drop the compute-not-budget argument" instruction at the end of this entry
  no longer applies and should be removed once the rest is re-checked, not
  followed.

  `participate/index.qmd` § "Supporting the project" was, as of 18 August 2026, a
  six-item list ordered *by how scarce each kind of help is*: reviewing,
  conjecture formulation and resolutions, formalizations, website and
  workflow maintenance, tokens, ideas. Checked against the roadmap, four of
  the six already carried it and two gaps were real:

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
  about this section. **Mohammad Mahmoody is still listed as "Bilkent
  University"** — his link itself is fixed separately, above, but the
  affiliation label disagreeing with it is not; confirm what his actual
  current affiliation is before writing a replacement rather than guessing.
  **Jens Groth's link is `http`-only** (`http://www0.cs.ucl.ac.uk/staff/j.groth/`),
  a mixed-content nag from an `https` site, and he is the one name carrying no
  affiliation.

  What the rewrite must not drop, since it is why the wording is careful: that
  support is not an endorsement or a review of any statement, that reviews are
  recorded only in the [provenance badge](/problems/status-legend/), and that
  anyone listed can ask to be removed without giving a reason. (The pointer to
  [Philosophy](/philosophy/) for the compute-not-budget argument is no longer
  on this list — see the superseded-19-August note above.)

- [ ] **Stop the harvester re-reading papers it has already read (~1.5h)**

  Requested 23 August 2026: `scripts/harvest_conjectures.py` should not reprocess PDFs under `latex/harvest/processed/`. Investigated the same day, and the picture is narrower than the request assumes: the script already refuses to reprocess by content, twice over. `main()` drops any input whose immediate parent is `processed/` (`pdfs = [p for p in pdfs if p.parent.name != PROCESSED.name]`), and `process()` checks the file's sha256 against `processed/harvest-log.json` before any text extraction or model call, returning `skipped-duplicate`. The ledger is currently exact — 58 documents, 58 PDFs in `processed/`, every hash present, no orphans in either direction. So no paper under `processed/` is being re-read today. What is broken is the surrounding behaviour, in four places:

  - **A skipped duplicate is moved into `processed/` anyway.** The run loop does `if status in ("ok", "skipped-duplicate") and not args.keep: move_to_processed(pdf, sha)`. `move_to_processed` finds the name already taken and falls back to `<stem>-<sha8>.pdf`, so an exact byte-duplicate lands in `processed/` a second time under a mangled name. That breaks the 58 = 58 invariant above and degrades every filename-keyed check downstream, including `latex/harvest/prune-papers`, which matches on basename. An exact duplicate belongs in `pruned/` or deleted, not copied into `processed/` twice.
  - **The discovery filter is too narrow.** `p.parent.name != PROCESSED.name` excludes only a directory named exactly `processed` exactly one level up. `latex/harvest/pruned/` is not excluded and currently holds 8 exact duplicates of already-processed papers, so `harvest_conjectures.py latex/harvest/pruned/*.pdf` walks straight into the previous bullet; a nested `processed/` inside an author folder is not excluded either. Test path containment against `PROCESSED` (and `pruned/`), not the parent's name.
  - **Dedup is by file bytes, not by paper identity.** The same paper as a different arXiv version, or as an ePrint/arXiv pair of the same work, has a different sha256 and is read again in full — model calls and all. This is the expensive failure and the one actually worth fixing. The ledger already records `pdf.name` and the drafts' `SOURCE.md` carries the resolved identifier, so key the ledger on a normalised paper id (ePrint `YYYY-NNN`; arXiv id with the version suffix stripped) alongside the hash, and report a hit on either.
  - **Nothing says up front how much of a batch is already done.** Neither `--dry-run` nor `--report` cross-checks the input list against the ledger, so duplicates surface one line at a time as the run hits them. On a batch the size of the current tree that is the difference between a decision and a surprise.

  While in here, run `latex/harvest/prune-papers` (it has not been run since five exact duplicates arrived in live author folders: `Vinod Vaikuntanathan/2024-1795.pdf`, `Giulio Malavolta/2021-248.pdf`, `Geoffroy Couteau/2021-016.pdf`, `Geoffroy Couteau/2023-571.pdf`, `Hoeteck Wee/2026-417.pdf`), and correct the stale counts in the harvester entry under "Conjectures and papers". **Counts done 23 August 2026**, and the tree matches neither figure recorded here: the top level is now **empty** (all 8 loose PDFs were harvested that day, not the 5 listed here — the three older ones, `2007-168`, `2017-937` and `2025-1258`, dated 22 August, were loose too and this count missed them), `processed/` holds **66**, `pruned/` holds **8**, and the author subfolders hold **1,066** by two independent counts, not 1,077. The 11-PDF discrepancy against the figure recorded here hours earlier is unexplained and worth a recount rather than trusting either number. `prune-papers` still has not been run. **Recount after the second batch of 23 August 2026**: the top level is empty again, `processed/` holds **78** against 78 ledger documents, and `pruned/` holds **11** — the three extra being the byte-identical duplicates (2022/885, 2023/1444, 2024/1171) that arrived with that batch and were routed to `pruned/` **by hand**, which is exactly the behaviour the first bullet above asks the script to adopt. That is now a worked example of the fix rather than a hypothetical: the 78 = 78 invariant survives only because the move was done manually. **Recount after the third batch, same day**: the top level is empty again, `processed/` holds **87** against 87 ledger documents with no orphans and no hash mismatches in either direction, and `pruned/` still holds **11** — the nine papers of that batch were all fresh, checked against the ledger by hash and by filename and against the author subfolders for byte-duplicates before anything was read, so nothing needed routing to `pruned/` and the invariant survived without a manual move this time. `prune-papers` has still not been run. **Recount after the fourth batch, same day**: the top level is empty again and `processed/` holds **101** against 101 ledger documents, no orphans and no hash mismatches. `pruned/` still holds **11**: the fourteen papers of that batch were all fresh, though two of them (2021/885, 2022/028) are byte-identical to copies in the `Yuval Ishai/` author folder that had never been processed — so they were not duplicates when read, and those two folder copies **are** duplicates now. That is a case `prune-papers` would catch, and one more reason to run it. `prune-papers` has still not been run.

- [ ] **Design the research-object and status/verification data model (~4h — uncertain: this schema decision is what the rest of the site's data model inherits)**

  The maintainer brief's central structural argument: treat problem, exact statement, attempt, progress result, resolution claim, review, source, artifact, and activity event as separate, versioned objects rather than compressing everything into one status badge. Independent axes to model: problem state (proposed / open / candidate resolution / resolved-refuted / withdrawn), result scope (full / partial / variant-only), open-status evidence (candidate / source-supported / literature-checked / expert-confirmed / contested), publication state, AI contribution, and verification/editorial state (Unreviewed / In review / Supported / Multiply verified / Contested / Retracted-refuted). Verification methods — artifact reproduced, proof-assistant kernel checked, informal-to-formal fidelity audited, independently expert reviewed, literature/open-status checked, peer reviewed — should combine rather than form one ladder, and "Contested" is an overlay on any of them, not a replacement: a Lean-checked artifact can still encode the wrong statement. Also record significance bands (Landmark / Field-shaping / Significant / Specialist / Exploratory / Unassessed, each with a rationale, kept separate from research priority) and problem horizons (Sharp / Incremental / Programme / Conceptual). Do this before the problem-card and problem-page tasks below — they consume these fields, they shouldn't invent them ad hoc.

- [ ] **Design the AI-provenance labels and the credit/attempt-report model (~3h)**

  Five AI-contribution labels — Human-only, AI-assisted, AI co-developed, AI-led/discovered, Undisclosed/unclear — recorded separately from problem origin and per-task execution role; avoid the brief's flagged ambiguous catch-all "AI-generated," and preserve the actual model/version, tools, workflow, and human steering behind the classification. Attempt reports default to a structured public report (exact statement/context version, model and tools, prompts/workflow, cost and human time, approaches tried, failures, useful intermediate claims, code/artifacts, human interventions, reviewer disposition) with a reproducibility bundle opt-in and no private chain-of-thought required or solicited. Separately, split credit into named roles — problem poser, discoverer, submitter, statement editor/maintainer, literature/open-status checker, solver, counterexample finder, partial-result author, formalizer, statement-match reviewer, proof reviewer, reproducer, tool builder — map them to CRediT where useful, and give stable IDs, recommended citations, BibTeX, ORCID, and a public contribution ledger. A problem poser should not automatically inherit authorship on a later solution.

- [ ] **Build the two-lane admission model and staged triage for new problems (~3h)**

  Keep a visibly separate vetted archive (passed provenance/formulation/open-status checks) from a laboratory/incubator lane (precise enough to assess, not yet vetted), rather than one undifferentiated list. New submissions should pass staged triage — prior-art search, precise formulation, cheap falsification/boundary tests, responsible-disclosure screening, bounded attempts, then promotion if the evidence warrants it — with a submission timestamp that records receipt, not novelty or priority. Depends on the status-model task above for the state values this triage moves between.

- [ ] **Redesign the homepage and primary navigation around the problem index (~2h)**

  Nav should read Problems · Activity · Contribute · Search — drop Papers, Surveys, the UC Encyclopedia, and Philosophy/About from primary nav, preserving their URLs and reachability via a secondary resources page. The homepage itself becomes the working problem index rather than a manifesto: a visitor should see and assess real problems immediately, led by vetted records, with the review queue and incubator surfaced only as an explicit opt-in filter. Each problem card should show title, one-sentence formulation, open/resolved state and partial progress, origin and open-status confidence, years open, significance band, field/model tags, AI-contribution and verification badges, current frontier, and last update with a next action — this depends on the status/AI-provenance model above existing first.

- [ ] **Restructure the canonical problem page to the brief's eight-part layout (~3h)**

  Header and exact claim; why it matters; precise statement/model/definitions/assumptions; current frontier and remaining gap; progress timeline and prior attempts; verification/formalization/disputes/open obligations; sources and citations with PDFs/TeX/Lean/code/data; and actions (investigate, review, correct, subscribe, discuss). Tabs can stay as shortcuts, but essential evidence must not live only behind them, and citations should be inline rather than forcing a reader through a separate chain of source pages.

- [ ] **Stand up GitHub Discussions and one activity stream (~2h — manual: enabling Discussions needs an org owner)**

  Turn GitHub Discussions on, linked to stable problem IDs, as the durable-deliberation layer under the canonical record — a Discord/live-meeting layer, if one exists, stays social-only, and any substantive result from chat gets written back into the record. Build one high-signal activity stream exposed three ways: a website page, an RSS/Atom feed, and a documented JSON feed, with per-problem and per-topic subscriptions.

- [ ] **Apply the licensing stack and set up preservation exports (~2h — blocked on the legal review in "Credibility and distribution")**

  CC BY 4.0 for research prose and authored statements, CC0 for structured catalogue metadata, MIT or Apache-2.0 for code and formalizations, with third-party material keeping its own terms and no implied Conjura license over it — all subject to the legal review above, so don't apply this until that comes back. Alongside it: complete static/JSON exports, immutable releases, independent backups, and an actually-tested restoration, not just a documented one.

- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  46 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs, three are marked *No canonical definition*, and fifty-five are written — measured 18 August 2026. **Superseded 23 August 2026: 22 stubs remain, six are *No canonical definition*, and seventy-six are written** — a batch of twenty landed that day and its findings are below. Run `python3 scripts/uc_status.py --check` for the current split rather than trusting these numbers. Added 18 August: F-acc, F-TSIG, F-adsig, F-NIZK, F-PUF, then F-aPAKE, F-saPAKE, F-VSS, F-ABB, F-dauth, then F-SNARK, F-thdec and F-DKG with F-eqv and F-NMCOM as *No canonical definition*, alongside the forty-two already listed in `git log`.

  **The 23 August 2026 batch of twenty, and eight findings worth keeping.** Written with definitions:
  `f-ke` and `f-sc` (Canetti–Krawczyk 2002/059, the strong $\mathcal{F}_{\textsc{ke}}$ and $\mathcal{F}_{\textsc{sc}}$),
  `f-ro` (the *local* oracle, from Badertscher et al. 2017/149 Fig. 3), `g-gg`, `f-asyncmpc`, `f-phe`, `f-fe`,
  `f-ledger`, `f-gsig`, `f-ae`, `f-fsaead`, `f-psi`, `f-mix`, `f-onion`, `f-crypto`, `f-dh`, `f-cred`.
  Written as *No canonical definition*: `f-nce`, `f-obf`, `f-incoerc`.

  - **A stub with no citation at all is not a dead end.** `f-psi` cited nothing and now carries Rindal–Rosulek 2017/769
    Fig. 1, found by forward search. The same route is still open for `f-crhf`, `f-mhf`, `f-owf`, `f-prg`, `f-rp`,
    `f-abe`, `f-ibe`, `f-gc`, `f-oram`, `f-pir` — searched for this batch without success on ORAM and garbling, so those
    two are the ones to attack with a better query rather than the ones to write off.
  - **Two printed functionalities are defective as printed, and both defects would have gone into the box.**
    `f-asyncmpc`'s source initializes its delay counter to $0$, decrements on fetch and delivers when it reaches $0$ —
    so delivery never happens; fixed the way the same paper's own channel does it, and the page says a protocol proved
    against the printed box is not proved against this one. `f-fe`'s source stores an **unbound variable** $\mathsf{s}'$
    as the successor state. Read both pages before trusting either source.
  - **Read the *second half* of a condition.** `f-phe`'s substitution clause fires when the server was compromised
    **or no entry was stored yet**; the first transcription had only the first half, and the re-check caught it. Same
    class of error in `f-gsig`, where the source tests for one specific rejected record and a test on the verdict alone
    is stricter than the source.
  - **`--vs-preview` produces false MISMATCHes from `pdftotext`, not from the fragment.** Three fragments failed the
    check with a line number that LaTeX had plainly printed; the extraction inserts a `0x01` byte after the colon at
    certain column positions. **Moving a `\columnbreak` fixes it.** Three columns are much worse than two — `f-cred`
    lost six numbers in `multicols{3}` and none in `{2}`.
  - **Two columns hold about 60 numbered lines and no more.** `f-cred` at 87 lines silently lost everything past 73:
    the box overflowed the page and `--vs-preview` reported the tail missing. That is the hard budget for a one-box
    page, and it is why the biggest functionalities need the *declared fragment* treatment (`f-crypto`, `f-cred`,
    `f-dh`) that `f-mac` and `f-kdf` established.
  - **Passed over on size, with the reason recorded here rather than rediscovered.** `f-cgka` (Alwen–Jost–Mularczyk
    Fig. 10 is ~130 lines plus two pages of helpers plus a separate safety-predicate figure), `f-secmsg` and `f-cke`
    (Canetti et al. 2022/376 Figs. 6–7 and 13–14, two pages each), `f-vote` (e-cclesia Figs. on pp. 24–26, two pages,
    clock-parameterized), `f-chan` (Dziembowski et al. Fig. 6, recursive virtual channels with round arithmetic),
    `g-ledger`. Each wants a sitting of its own **and** a decision about how a box longer than 60 lines is presented.
  - **`f-ledger` and `g-ledger` are now two different objects**, which resolves the duplicate flagged earlier:
    `f-ledger` carries Dziembowski et al.'s $\widehat{\mathcal{L}}$, a twelve-line account-balance ledger, and
    `g-ledger` keeps Badertscher et al.'s transaction-log $\mathcal{G}_{\mathsf{ledger}}$. The first is *printed* as a
    local functionality and *used* as a global one, which is the cleanest example in the literature of the point that
    globality is a fact about use rather than a field a box carries.
  - **Six titles were wrong, continuing the run.** `g-gg` claimed "global observable variant; bilinear types 1–3" and
    the printed box is neither observable nor type-1/2; `f-fe` claimed "predicate encryption", absent from its source;
    `f-phe` claimed "key rotation", which is a *separate* functionality in the same paper; `f-asyncmpc` said "MPC"
    where the box is one-shot SFE; `f-mix` said "verifiable shuffle", which is a proof technique; `f-ledger` said
    "transaction ledger" for an account-balance box. `f-dh` said "exponentiation" and the box offers key *agreement*.

  Two sources needed non-ePrint handling: the Makita et al. group-signature paper is **in Japanese** and its box is a
  translation (a weaker chain of custody than any other entry here, flagged on the page), and three sources exist only
  as PostScript (2001/069, 1996/001, 2002/059) and were converted with Ghostscript, so their PDF page numbers are the
  PostScript's own and both numbers are given.

  The tooling for this now exists end to end, so this is a matter of running it 97 times rather than inventing the process each time:

  - `scripts/uc_source.py <id>` does the mechanical half. It reads the page's own reference bullets, resolves each to a PDF (newest ePrint revision, falling back to the PostScript-only postings the 1990s papers still are), records every revision stamp, scans the text layer for interface-box titles, renders the pages carrying a box named after the functionality into `<id>/_src/`, and writes `<id>/_src/sources.json` with URL, revision, page and a ready-made citation pointer. The PNGs are gitignored — a proceedings figure is the publisher's — and `_src/` is `_`-prefixed so Quarto never publishes it; the manifest is committed and reproduces the images exactly.
  - `prompts/source.md` is the per-stub prompt, rewritten 16 August 2026 around that harvest: choose among the cited definitions in a fixed order (same object first, then revision/formulation/framework currency, then a tie-break ladder), capture the original as reviewer evidence, rewrite it in the book's notation, keep a mismatch register.
  - `scripts/gen_interface.py` turns the `.tex` fragment into the page's box with the line numbering computed and CI-gated, and `--vs-preview` compiles a fragment standalone to prove LaTeX prints the line numbers the generator computed — the check `--vs-pdf` cannot do for the 97 boxes the book does not typeset.

  Three things the runs so far have established, worth knowing before the next one. **A stub's own citations are often not where the definition is printed**: F-BC's three references include Canetti's framework paper, which prints no broadcast box at all, and the definition taken came from the two adaptive-broadcast papers instead. **A citation that yields no box is a result, not a gap** — Rabin 1981 contains no `F_OT` because it predates ideal functionalities, and Pfitzmann–Waidner's secure message transmission is an ideal *system* in the reactive-simulatability model, not a UC functionality; both pages say so. And **F-SFE has no printed box under that name** in either paper it cites (`uc/layer-6-secret-sharing-mpc/f-sfe/_src/sources.json` records that CLOS 2002 prints F_bc, F_cp, F_mcom, F_ot and F_zk, and no F_sfe), so that entry needs a forward literature search before it can be written, or a page saying the functionality is folklore.

  **~~The pool of small clean boxes is exhausted.~~ It is not, and the claim was an artefact of the harvester.**
  Corrected 18 August 2026, after the batch that followed it found five. `uc_source.py`'s box scan reports
  false negatives far more often than the three modes recorded below suggest: running
  `pdftotext -layout <paper> | grep -E '(Figure|Fig\.) [0-9]+.*[Ff]unctionality'` over the *already cached*
  PDFs turns up directly-named boxes the harvest missed in at least fourteen entries. Five were written
  straight from that list. Before believing any "no box found" result, run that grep — it costs seconds,
  the PDFs are already in `~/.cache/conjura-uc-sources`, and the harvester is not the authority its
  `sources.json` looks like.

  **The clearest case is `f-nizk`, which this file had listed as a candidate for a *No canonical definition*
  page.** Its own primary citation — Groth, Ostrovsky and Sahai, JACM 2012 — prints $\mathcal{F}_{\mathsf{NIZK}}$
  in Figure 4, and the harvest reported nothing. That is the fourth false-negative mode again, and it means
  the other two names on that candidate list, `f-ro` and `f-eqv`, should be re-checked the same way before
  anyone writes them off.

  **Already located, for the next batches, with the box named in the cited paper:** `f-cred`
  ($\mathcal{F}_{\mathsf{daa}}$, Camenisch et al. — note the name is DAA, not credentials, so it is a naming
  judgment), `f-snark` ($\mathcal{F}_{\textsc{weak-nizk}}$, Kosba et al.) and `f-secmsg`
  ($\mathcal{F}_{\mathsf{SM}}$, Figure 7 — large, and entangled with the paper's other four modules).

  **The generator accepts a narrow LaTeX subset, and finding out the hard way costs a rebuild.**
  `parse_fragment` handles `\State`, `\Req`, `\If`, `\EndIf`, `\Comment`, `\Statex`, `\algcont`,
  `\algsave` and `\setcounter` — and nothing else. In particular there is **no `\Else` and no `\ElsIf`**:
  write two guarded `\If`s instead, negating the first condition where the source's `else if` semantics
  require it. Every command must sit on **one source line** (a wrapped `\If{...}` condition raises), and a
  `\label` must share the line with its statement rather than sit on the next one.

  **A fifth false-negative mode: the definition may not be in a figure at all.** `f-dkg` sat unwritten
  because Wikström states it as a numbered `Functionality 4 (Distributed Key Generation)` environment in
  running text, so both the harvester's box scan *and* the figure-caption sweep that found the previous ten
  entries looked straight past it. Add `grep -nE 'Functionality [0-9]+ *\\('` to the sweep. The same paper
  states its three hybrids the same way.

  **"No canonical definition" now has two more worked examples, and both are structural rather than
  accidental.** `f-eqv`: equivocability is a property of a *scheme*, not something a functionality can
  express — a commitment box stores the value directly and has no ciphertext to reinterpret, so
  equivocation is what the *simulator* does. `f-nmcom`: UC security already *implies* non-malleability,
  against arbitrary other protocols and not merely other copies, so a non-malleable commitment
  functionality would assert what `F-COM`/`F-MCOM` already give. Both pages were written only after a
  forward search, per the rule below, and both say what would resolve them. Note the neat cross-check:
  Kosba et al.'s $\\mathcal{F}_{\\textsc{weak-nizk}}$ needed an explicit `Maul` interface *added* in order
  to permit mauling, which is the cleanest evidence available that the unmodified functionalities forbid it.

  **A SNARK has no functionality of its own.** Succinctness is a property of a proof system, and an ideal
  functionality has no proof strings whose length it could bound. Ganesh et al.'s box is GOS12's
  $\\mathcal{F}_{\\mathsf{NIZK}}$ with one plumbing difference, so transcribing it would have duplicated
  `f-nizk`; the `f-snark` slot carries $\\mathcal{F}_{\\textsc{weak-nizk}}$ instead, which is the one
  genuinely distinct box in its citations.

  **`f-thdec` gained a reference.** Its two cited papers print no threshold-decryption functionality; Zyskind,
  Zarchy, Leibovich and Peikert (CCS 2025, ePrint 2025/1781) do, and it was added. That is the
  "box printed in a paper the stub does not cite" mode, now seen three times. Their $\\mathcal{F}_{\\mathsf{Decrypt}}$
  also carries the strongest caveat any source here has attached to its own box -- it "is not a complete
  functionality for threshold encryption", and without an external well-formedness restriction the
  `Decrypt` command "would act as an unrestricted decryption oracle, from which it is easy to learn the
  secret key". The page leads with that rather than burying it.

  **Two more shading-coded figures, and the trap is now a pattern rather than an incident.** After
  `f-acc`'s colour key, the OPAQUE paper turned out to encode *three* functionalities in two figures by
  typography alone: Figure 1's caption reads "$\\mathcal{F}_{\\mathsf{aPAKE}}$ (full text) and
  $\\mathcal{F}_{\\mathsf{saPAKE+}}$ (shadowed text omitted)", and Figure 2 is then a *marked diff* of
  $\\mathcal{F}_{\\mathsf{saPAKE}}$ against that second one. None of the shading survives `pdftotext`, so a
  text-only reading silently produces a blend of three different objects. **Render the figure and look at
  it** whenever a caption mentions full text, shading, marks, colour or omission — `pdftoppm -f <p> -l <p>
  -r 135 -png` is enough. Treat a caption naming two functionalities as a hard stop.

  **A citekey is not unique across entries, which breaks naive cross-entry scans.** `canetti2001` means
  Canetti--Fischlin, *Universally composable commitments*, on `f-nmcom` and `f-eqv`, and Canetti's framework
  paper on `f-ke`. A scan that globs `~/.cache/conjura-uc-sources/<citekey>-*.pdf` and takes the first match
  will read the wrong paper. Match on the recorded `sha256_16` instead.

  **Still located and unwritten, from the same grep:**
  `f-secmsg` ($\\mathcal{F}_{\\mathsf{SM}}$, Figure 7, entangled with four sibling modules), `f-chan`
  (state channels, Dziembowski et al.), `f-cred` ($\\mathcal{F}_{\\mathsf{daa}}$ -- DAA, a naming judgment
  against "credentials"), `f-snark` ($\\mathcal{F}_{\\textsc{weak-nizk}}$, Kosba et al.).

  **`f-fhe`'s citation resolved to nothing of its own (21 August 2026).** Checked Zyskind, Zarchy,
  Leibovich and Peikert (CCS 2025, ePrint 2025/1781) directly: it prints $\\mathcal{F}_{\\mathsf{ABB}}$
  (`f-abb`'s object) and $\\mathcal{F}_{\\mathsf{Decrypt}}$ (`f-thdec`'s -- now written, and it converges
  with an independently-drafted reading almost line for line, which is as strong a confirmation as this
  process gets that the object landed on the right page). Neither is a general FHE functionality --
  $\\mathcal{F}_{\\mathsf{Decrypt}}$ decrypts one already-computed LWE ciphertext and says nothing about
  the homomorphic evaluation that produced it. `f-fhe` itself is therefore back to unlocated: it needs a
  forward search for a paper that prints an actual FHE-evaluation functionality, not another look at this
  one.

  **Two more stub titles were claims, and both were wrong (18 August).** `f-acc` read "Accumulator, vector
  commitment" — the source defines no vector-commitment functionality and the phrase "vector commitment"
  appears nowhere in it, checked; retitled to "Accumulator". `f-tsig` read "Threshold signature", but the
  printed box requires *every* signatory to have asked before a signature exists, so it is the unanimous
  ($n$-of-$n$) case and the threshold lives in the protocol; retitled "Threshold signature, unanimous".
  That is eleven of the last nineteen entries retitled. Two more went on the second batch: `f-dauth` read
  "On-line deniable authentication" and its source defines no such functionality -- the paper's result is
  that on-line deniable authentication is *impossible*, and the object it prints is
  $\\mathcal{F}_{\\mathsf{keia}}$, key exchange with incriminating abort; and `f-vss` now names the
  *spooling* variant it actually transcribes, since the non-spooled Definition 4 is the one the paper says
  adaptive corruption defeats.

  **A new paging trap: the archive listing and the PDF can disagree about the title.** ePrint 2021/060 is
  posted as "UC Non-Interactive, Proactive, **Threshold** ECDSA with Identifiable Aborts", which is also the
  CCS 2020 title of record, but the title page of its newest revision (`20241021:172019`) reads
  "**Distributed** ECDSA". The rename is internal to the revision and never reached the metadata, so a
  reader who fetches the PDF and one who reads the listing see different titles for one document. Record
  both when this happens.

  **"No canonical definition" now has a worked example: `f-sfe`.** The page shows the harvest that establishes the absence, rules out the three extraction failures seen earlier, explains why a compiler theorem has nothing to draw a box around, and gives the two routes out (find a paper that prints it, or retire the slot). Use it as the template for the other stubs whose sources genuinely print nothing — `f-ro` and `f-eqv` are the remaining candidates — but see the correction below before trusting either.

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

## Conjectures and papers

- [ ] **Add the missing salt to `c/0003`, whose statement is false as printed (~1h — placed first in this section because it is a correctness defect, not an improvement)**

  Found 23 August 2026 by the attackability triage (`audits/2026-08-23-conjecture-attackability-triage.md`). The page states the k-collision time-space tradeoff for an **unsalted** random oracle, and in that model it is refuted in one line: the offline stage stores a single k-collision in `k log N` bits, the online stage outputs it with no queries at all, and the claimed `S^{k-1} T^k = Omega(N^{k-1})` fails outright while success tends to one. A random `H : [N] -> [N]` has about `N/k!` k-collisions, so one exists almost surely and the advice is `O(log N)` bits.

  The diagnosis is a dropped hypothesis rather than a wrong belief: every source the page cites is stated relative to a salt drawn *after* the advice is fixed. The k = 2 baseline in its own comparison table, `S*T^2 = Theta(N)` attributed to Coretti–Dodis–Guo–Steinberger, is the salted theorem transcribed without its salt, and the multicollision literature it points at (Akshima, ITC 2024) is salted Merkle-Damgård throughout, indexed by a block bound `B` the page never mentions. Independent corroboration from inside the repo: the Lean file's own signature is `opaque FindsKCollision (S T k N : Nat) : Prop`, with no salt argument either, which the item below already flags for a different reason.

  Restore the salt, decide whether the target is the threshold form or the advantage form the cited results actually prove, and say whether `B` is in scope. Then re-check whether the repaired statement is still open, because the salted `k >= 3` cell has at least one paper on it.

- [ ] **Refresh `c/0024`'s state of the art, which its own caveat flagged as unchecked (~1h)**

  Found 23 August 2026 by the same pass. The page's caveats say it is a 2023 ePrint whose citing papers have not been checked. They have been now: Bauer, Couteau and Sadeghi, *Fine-Grained Non-Interactive Key Exchange, Revisited* (ePrint 2024/834, CRYPTO 2024) reach a hardness gap up to `N^1.6` **in Maurer's model**, assuming non-uniformly secure injective pseudorandom generators with exponential hardness, and achieve the quadratic gap in the standard model.

  This does not settle the page. Its conjecture demands vanishing advantage against computationally unbounded query-bounded eavesdroppers, so it is information-theoretic, whereas the `N^1.6` construction is conditional on a computational assumption. But it is a rung the page does not record, it is what any future attempt would be measured against, and it is exactly the object a produced "solution" would be mistaken for. Add it to the progress remark, and check the sibling [c/0025](/c/0025/) in the same pass, since the same paper works the other half of that gap.

- [ ] **Record the `sigma = 0` boundary of `c/0010`, and strengthen `rem:ell1` with a zero-leakage counterexample (~2h)**

  Found 26 August 2026 while answering a question about the zero-leakage case of `conj:main` in `c/0010/campaign/CONTRACT.md`. Strictly, `sigma = 0` is outside the stated range: the parameter list writes `q in N u {0}` explicitly but `sigma_1, sigma_2 in N`, so `N` excludes zero there and `sigma >= 2`. It is reachable anyway, since `sigma_i` bounds the leakage (`|z_i| <= sigma_i`) rather than fixing it, so `sigma_1 = sigma_2 = 1` with empty-string leakage realises it. Three findings, none of which change the statement or the proof; all three belong in the remarks.

  **1. At zero leakage the presampling content of the conjecture is empty, and the conjecture is equivalent to its own consequence.** The empty fixed set is admissible for every `P in N` (`|{}| <= P`, and consistency with `f` is vacuous), so the constant family `Y_f := uniform on Fun` is legal. With `sigma = 0`, `Dec` under that family is `D` talking to a fresh uniform `H*` with `x` independent of `H*`; `Pr[x in Q] <= q delta` by `lem:query`'s argument, and off that event `H*(x)` is uniform and independent of `D`'s view, so `Dec` is within `q delta` of `Real_0` — which at `sigma = 0` does not involve `x` at all. Hence `Adv <= kappa(q) + q delta`, and in the non-vacuous regime `sigma' q+ delta <= 1` the `q delta` is absorbed into `C sqrt(sigma' q+ delta)`. Combined with `thm:main` this makes `conj:main` and `thm:main` equivalent at `sigma = 0` up to constants. So `sigma = 0` is not a rung on the presampling ladder — nothing about mixtures or fixed sets is tested there, and a prover who proves it has proved the consequence directly.

  **2. What `sigma = 0` does test is exactly tight, and it pins down `sigma'`.** At `sigma = 0`, `q = 0`, `thm:main` reads: `H(x_1,x_2)` is `O(sqrt(log N * delta))`-close to uniform for two independent sources that read all of `H` and remain `delta`-unpredictable given `H` — a random function is a two-source extractor against sources that know it. Two numerical checks, 26 August 2026. A source pair supported on a worst-case `a x a` rectangle, `a = 1/delta`, achieves bias `sqrt(ln N * delta)` (Hoeffding against the union bound over `C(N,a)^2` rectangles), and `sqrt(sigma' delta) = sqrt(2 log_2 N * delta)` exceeds it by exactly `sqrt(2/ln 2) ~ 1.699` at every `a` from `2^6` to `2^16` — `N`-independent, a log-base artifact only. And monochromatic `a x a` rectangles in a random 2-colouring of `[2^20]^2` vanish at `a ~ 40 = 2 log_2 N`, which is precisely where `sqrt(sigma' delta)` crosses 1 and the bound goes vacuous. So the `2 log N` in `sigma' := sigma + 2 log N` is not slack and the square root is not a proof artifact: both are forced at zero leakage. The "bits needed to name a point of the domain" reading of that term is literally the union-bound cost of the source choosing its support after seeing `f`, which is why the same `2 log N` reappears as `C_0`'s `ln(4N^2/gamma_0)` in Lemma 3 of `split-decomp-kappa-1-r3.md`.

  **3. `rem:ell1` should be strengthened, because splitness is needed even at zero leakage.** `rem:ell1`'s single-source counterexample spends a 1-bit leakage, so it says nothing at `sigma = 0`, which invites the reading that leakage is where the difficulty lives. It is not. Drop only splitness, keep the pair domain and `sigma = 0`: let one source output `x` uniform from `A := {u in [N]^2 : H(u) = 0}`, `|A| ~ N^2/M`. Each coordinate marginal is uniform to within `1 +- O(sqrt(M log N / N))`, so `delta = (1+o(1))/N`, the floor `delta >= 1/N` of `def:sources`. Yet `H(x) = 0` with probability 1 while `Real_0`'s challenge is uniform, so the 0-query `D` testing `y = 0` gives `kappa(0) >= 1 - 1/M`, against a bound of `(4c+2C+4) sqrt(2 log N / N)`: `6.2e-3` at `N = 2^20`, `2.4e-4` at `N = 2^30`. Sharper than `rem:ell1`'s vector in four ways — zero leakage, unpredictability at its floor, a 0-query observer, and no use of the leakage channel at all, since the source encodes everything in its *choice* of `x`. It also sharpens `rem:ell1`'s own warning about where independence is used: what splitness buys is that post-hoc selection is confined to a *product* set, and biased rectangles are rare exactly where biased sets are not.

  **The work.** Add a remark to `CONTRACT.md` recording (1), since it tells a future prover not to spend a rung on `sigma = 0`, and (2), as evidence that `sigma'` and the exponent are not negotiable. Supplement `rem:ell1` with the zero-leakage example, keeping the leakage one if it is doing separate duty. Then re-read the frozen artifacts against (3): `rem:ell1` demands that any proposed proof "fail visibly when the two sources are replaced by one", and that demand has only ever been checked against the leakage-based vector.

- [ ] **Verify `split-decomp-kappa-3`, then propagate it into `kappa-2-r2` §7/§9 (~3h)**

  Written 26 August 2026. `c/0010/campaign/intermediates/split-decomp-kappa-3.md` re-accounts Theorem E of `split-decomp-kappa-2-r2` and finds that two of its three hypotheses are not load-bearing. It proves nothing new about the oracle; every step is a re-derivation inside Theorem E's own proof, and all ten numeric claims in it were machine-checked over a parameter grid (`N` from 2 to 2^20, `sigma` from 0 to 64, `q` from 0 to 10^7, `delta` from `1/N` to 1) with zero failures.

  **What it establishes.** (G0) The hypothesis `q+ delta <= sigma'` can be deleted: either `8 sqrt(sigma' q+ delta) >= 1`, in which case the conclusion exceeds 1 and holds trivially since an advantage is at most 1, or `q+ delta < 1/(64 sigma') <= 1/128 < 2 <= sigma'` and the hypothesis holds anyway. This is the device r3 already uses in the second sentence of Corollary A'. (G1) The hypothesis `P <= sqrt(sigma'/delta)` relaxes to `P <= sqrt(sigma' q+/delta)`, a factor `sqrt(q+)`, with no constant moving — Theorem E bounds `P delta <= sqrt(sigma' delta) <= sqrt(sigma' q+ delta)` through an intermediate it does not need, and the direct inequality is exactly `P <= sqrt(sigma' q+/delta)`. (G2) The hypothesis `M <= sigma' q+/(4 delta)` becomes `min{mu'(min(qM,N^2)), 2 delta sqrt(M)} <= sqrt(sigma' q+ delta)` by using Corollary D" instead of D', and at `q = 0` that is vacuous because `mu'(0) = 0` exactly, so at `q = 0` the conjecture holds for **every** `M` and every observer under the single hypothesis `P <= 3 sqrt(sigma'/delta)`.

  **Why (G1) is the one that matters.** The Contract's `thm:main` instantiates the conjecture at `P = ceil(sqrt(sigma' q+/delta))`. Under Theorem E as stated that `P` sits a factor `sqrt(q+)` **outside** the proved region, so Theorem E supplied `thm:main` only at `q = 0`; capping `P` at `sqrt(sigma'/delta)` instead yields `kappa(q) = O(q+ sqrt(sigma' delta))`, weaker than the target by `sqrt(q+)`. Under (G1) the region reaches the Contract's own instantiation point. Note what this is and is not: on the `M` region, Corollary D" already bounds `kappa(q) <= 6 sqrt(sigma' q+ delta)` outright with no `P` and no appeal to the conjecture, so the *consequence* was never missing there — what (G1) buys is that the *decomposition statement itself* is now proved where a user following the Contract would use it.

  **Pass 1 done, 26 August 2026: DEFECTS, one finding.** A blind referee in fresh context, package-only, upheld F1 (class A): Corollary G1 was titled "the proved region now contains the Contract's own instantiation" while its proof used `P = floor(t)`, whereas `thm:main` instantiates at `ceil(t)`, which violated (H1) as then stated — at 165 of 180 grid points. Repaired in `split-decomp-kappa-3-r2`: (H1) widens to `P <= sqrt(sigma' q+/delta) + 1`, which is free, because the query term and the additive delta are each at most `(1/16) sqrt(sigma' q+ delta)` in the only regime the conclusion is non-vacuous — the total falls from exactly 8 to 7.0022 and `C = 8` survives with room. Corollary G1's own constant improves from 17 to 13. Everything else was accepted, including the quantifier-order Remark, which was the flagged class-(A) hazard, and every citation into r3 and kappa-2-r2 checked word-for-word. Four angles still to go.

  **Pass 1 on r2 done, 27 August 2026: DEFECTS, four findings, no computational error.** F1 (C) the proof's opening sentence licensed less than the sharpened sub-bounds use; F2 (A) a self-description carried over from the predecessor, false of r2 once the query term was also rewritten; F3 (A) Corollary G1's title overclaimed, verifying (H1) at `ceil(t)` but never (H2) — the referee called it "a softer instance of the same class of defect (F1) this revision was written to fix"; F4 (A, minor) the invariant claim undersold its own diff. All four repaired in `split-decomp-kappa-3-r3`. One class-(E) entry is charged to my packaging, not the artifact: the prompt named `cards/` without naming its files and the agent type had no directory listing, so two §4 card quotations remain unchecked by any referee.

  **Two further findings came from a repo-wide audit, both repaired in r3.** A1: §5 asserted that `split-decomp-kappa-2-r2` "has been through blind review at r1 and r2" — false, the one findings file reviews the pre-revision `split-decomp-kappa-2` at `8c68c62` and its tally says it does not carry over, so **Corollary D″ stands at zero passes** and the triage of that earlier pass *overruled* the referee on its constant. A2: the region for `conj:main` is the intersection over `q` of (H1) and (H2), not the region — `P <= sqrt(sigma'/delta)+1` and `M <= sigma'/(2 delta)` — so the `sqrt(q+)` relaxation does **not** enlarge where the conjecture is proved; the gain over the original Theorem E is the additive 1 and a factor 2 in M.

  **The full remaining-work ledger is now `c/0010/campaign/PROGRESS.md`**, written 27 August 2026 from that audit. Read it before picking up this campaign; the items below are the subset that is mine to schedule.

  **The work.** (a) Five verification angles on `split-decomp-kappa-3-r3`, and — first, because it is the weakest link — the first ever pass on `split-decomp-kappa-2-r2`, whose Corollary D″ is load-bearing for Theorem E″ at zero passes with an overruled referee objection against its constant. Worth aiming one of them at whether Corollary D" really applies to `D` with no hypothesis, since D"'s first arm is the one whose referee objection the kappa-2 triage **overruled** rather than upheld. (b) Then restate `kappa-2-r2` §7's Theorem E with the reduced hypotheses and rewrite §7's closing "what is now known is the union" paragraph, which is superseded: at `q = 0` neither of its two branches is needed. (c) Update `kappa-2-r2` §9's first two gap entries, which say `split-decomp-kappa-1-r3` "has no findings file and has not been through blind review" — it now has both, verdict CLEAN.

  **Defect found 27 August 2026, unrepaired: `rem:window` states the wrong window.** `split-decomp-kappa-3-r3` §2, `rem:window`, writes the uncovered set as `sqrt(sigma' q+/delta) + 1 < P < N^2` and then says "the window is where every application lives". Both cannot hold. That lower endpoint is the *per-q* hypothesis (H1), and `thm:main` instantiates at `P = ceil(t_q)` with `t_q := sqrt(sigma' q+/delta)`, so `ceil(t_q) <= t_q + 1` puts the application point outside that window by construction — which is exactly what Corollary G1, two pages earlier in the same file, proves. The "every application" claim is true of the *other* window, the one for `conj:main`, whose endpoint is q-free because (H1) binds at `q = 0`: `sqrt(sigma'/delta) + 1 < P < N^2`. Applications with `q >= 1` do live in that one. Writing `t_0 := sqrt(sigma'/delta)`, non-vacuity (`8 sqrt(sigma' q+ delta) < 1`) gives `delta < 1/(64 sigma' q+)` hence `t_0 > 8 sigma' sqrt(q+) >= 16`; since `t_q = t_0 sqrt(q+1)`, for `q >= 1` we get `ceil(t_q) >= t_0 sqrt(2) > t_0 + 1` with room. At `q = 0` the two coincide and `ceil(t_0) <= t_0 + 1` is covered, which is just "q = 0 is done" restated. So the corrected line is: unproved on `sqrt(sigma'/delta) + 1 < P < N^2`, where every application with `q >= 1` lives — a *wider* window than r3 states, and the reason applications fall outside it is not that `ceil(t)` is too big for (H1), which G1 fixed, but that `conj:main` demands one family good at every `q` and so is pinned at `q = 0`. This is precisely the per-q / intersection-over-q conflation that finding A2 was written to prevent, three paragraphs earlier in the same document. **Fix in both places**: `split-decomp-kappa-3-r3` §2 `rem:window`, and `c/0010/campaign/PROGRESS.md` §2.1, which inherited the sentence verbatim.

  **What is still open, and it is not what §8 says.** kappa-2-r2 §8 names the `M`-cap as Barrier 1. After (G2) the sharper residue is the `P`-cap: `P > sqrt(sigma' q+/delta)`. kappa-3 §4 locates it precisely — `P delta` enters r3's Theorem C at exactly one point, the `Pr[x in I_J] <= P delta` of the Contract's `lem:hit`, in the hop `Dec_0 -> Dec` — and argues it is a defect of the route rather than of the statement: on `{x in I_J}` consistency forces `H*(x) = H(x)`, the challenge `Real` supplies, so the event the route pays `P delta` for is the event on which `Dec`'s challenge is *correct*. The Contract concedes the mechanism itself, `rem:uses` recording that consistency "is *not* used anywhere in this section". §4 proposes routing `Real -> Mid -> Dec` with `Mid` carrying the decomposed oracle and the real challenge, which replaces `P delta` by a term of order `(sigma' + log gamma^-1)/P` — the same shape as the target's first term, and decreasing in `P` where `P delta` increases. Two gaps block it, both stated in §4: (G-a) the sources read the whole oracle, so the single-coordinate density bound must be applied at a point correlated with the conditioning; (G-b) `|Real - Mid|` has no bound, the observer there holding a challenge correlated with the oracle it is distinguishing, which is exactly the case [CDGS, Lemma 1] does not cover. (G-c) is closed: card `S1` records [CDGS, Definition 1] asserting density for *every* coordinate subset, singletons included, off the fixed set.

  **Where to push, and it is a specific question.** kappa-3 §4's Lead L1 quantifies (G-a): conditioning on the challenge point `x` reweights `X_j` by `Pi_{H,z}(x)`, and the reweighting costs at most `log(1/p(u))` bits of min-entropy deficiency, which is `<= 2 log N` on average and `<= 2 log N + log(1/gamma)` off an event of probability `gamma` (both checked over 400 random instances with arbitrary per-`f` product measures, the first tight to 0.9998). That is *exactly* the `2 log N` that `sigma' := sigma + 2 log N` is defined to carry — "the leakage length together with the number of bits needed to name a point of the domain" — so the penalty is already budgeted for in the target's own first term and no constant has to move. What blocks it is narrower than (G-a) as first stated: [CDGS, Claim 3] needs the source *dense*, not merely of bounded deficiency, and re-applying Claim 2 to recover density produces a fixed set depending on `x`, which Contract `rem:index` forbids the family from using. So the sharp question is whether Claim 3 admits a form tolerating a bounded-deficiency perturbation of a dense source against the **original** bit-fixing companion. Try that before anything else in §4. The multiplicative form of Claim 3 on card `S1` is recorded in §4 as *not* a way in — both forms need density — so that it is not tried twice.

- [ ] **Make the LaTeX and Lean statements say the same thing (~9h — placed first in this section for risk, not difficulty; the bridge-lemma item is real mathematics and may not land)**

  Requested 23 August 2026, and the request is about the mathematics, not the tooling: the conjecture as printed in the original paper, as typeset in `c/<id>/latex/main.tex`, and as formalized in `c/<id>/lean/Statement.lean` should be the same statement, as literally as possible. Surveyed 23 August 2026 across all four formalized statements.

  **Only one of the four Lean files states its conjecture.** `c/0001`, `c/0002` and `c/0003` put the mathematical content behind `opaque` — `opaque ArisesFromSystem (q m xiMax h : Nat) : Prop`, `opaque FindsKCollision (S T k N : Nat) : Prop`, `opaque SimQueryBound`/`opaque Advantage`. An `opaque` predicate can be `False`, so a theorem hypothesising one may be vacuous and nothing in the file can detect it. All three sit at `statement_match: open`, which is honest, but they should not be presented as formal statements.

  **`c/0002` is worse than vacuous: its formal statement is trivially provable.** Its conjecture carries hypotheses `q <= o(N^{1/2})` and `xi_max <= o(N^{1/2})` that do not appear in the Lean at all, and the `O(q * xi_max / N)` in the conclusion became `exists c, 0 < c and ...` *inside* every universal quantifier — so a prover chooses `c` per instance, and since a larger `c` weakens the bound, `c := t^{-1}` for `t = q * xi_max / N` drives the right-hand side to exactly `0`. Verified 23 August 2026 by restating the theorem with the `opaque` hypothesis generalised to an arbitrary predicate (so no proof could be using it) plus `1 <= q`, `1 <= xi_max`, and proving it: `#print axioms` reports `[propext, Classical.choice, Quot.sound]`, no `sorryAx`, and the linter reports the system hypothesis as unreferenced. Trivially true on every parameter setting Mirror Theory is about.

  **The governing principle: if the LaTeX statement cannot be transliterated, the LaTeX statement is what to fix.** Every divergence found came from translating around a defect in the printed statement instead of repairing it, and asymptotic notation is the main offender — `o` and `O` are meaningless on a single instance, so the formalizer must invent a quantifier order, and `c/0002` invented the wrong one. De-asymptotise in the paper, with explicit constants and explicit order ("there exist c1, c2 > 0 such that for all N and all G with q <= c1 sqrt(N) and xi_max <= c1 sqrt(N), h >= ... (1 - c2 q xi_max / N)"), and the Lean becomes a transcription with no judgement left in it.

  **The work:**

  - **Restate `c/0002`'s conjecture de-asymptotised, then reformalize it (~2h).** The hypotheses have to reappear and the constant has to move outside. `c/0004`'s docstring already says why quantifier order is the whole content of a statement like this; `c/0002` is the same shape and gets it backwards.
  - **Do the same for `c/0001` and `c/0003` (~3h).** Either define the object (`c/0004` shows it is usually possible: "nothing is `opaque`"), or, where a dependency is genuinely too large, quantify over a *constrained* structure carrying the properties the statement needs, so a reader can check those against the paper. Never `opaque P : Prop` as a hypothesis. If neither is workable, drop the Lean file rather than ship a statement that pins nothing.
  - **Close the six `c/0004` gaps (~1.5h).** `[DecidableEq K]`/`[DecidableEq D]` are binders of `lhl_public_seed` with no printed counterpart (they exist only to get `Fintype (K x D -> R)`) — discharge them classically inside `Table`'s instance so the theorem quantifies over exactly `[Fintype]`/`[Nonempty]`, as the paper does. `Z` is quantified in Lean and never introduced in the paper — add it to the paper ("fix also a set of auxiliary information, not necessarily finite"). `y_0 <- H(sd,x)` is inlined into the `if` — bind it with `PMF.pure` (equal by `PMF.pure_bind`) so the game body is one line per figure line. Replace `b : Bool` plus `if b then y1 else y0` with `b <-$ Fin 2` and `y : Fin 2 -> R`, so the paper's `y_b` is literally `y b` and the bit convention stops existing — `MATCH.md` admits `extAdv_eq_zero_of_subsingleton` cannot detect a swap of it. Rename the Lean type variables to the paper's script letters so `K` can mean the cardinality in both files, as against today's collision where `D` is the input type in Lean and the input set, its cardinality, and the distinguisher in the paper. And either use or delete the paper's `SD` and `U_R`, which it defines and then never mentions again.
  - **Prove the correspondence rather than tabulating it (~1.5h, uncertain).** `MATCH.md` argues; a lemma settles. For `c/0004` the sharp instrument is exactly the abandoned apparatus: a bridge lemma tying `extAdv` to statistical distance, `extAdv <= 2 SD(...)` with equality at the optimal distinguisher, which is the classical leftover-hash formulation. A mis-wired game fails it at once. Add a non-vacuity lemma too — exhibit an epsilon-unpredictable source at nontrivial epsilon (the uniform source on the input set with trivial auxiliary output is `1/D`-unpredictable). An `exists c` statement over a hypothesis class nobody has shown inhabited is the hole `c/0002` is sitting in.
  - **One definitions file per source document (~1h).** `c/0004/latex/main.tex` states both conjectures; Lean has only the public-seed one and `c/0005` (secret seed) has no Lean at all. Put `Table`, `Source`, `Predictor`, `predGame` and `Unpredictable` in one file that both statements import, mirroring the single paper. Two independent copies of the same games drift, and no per-page match table can see it.
  - **Then, and only as support, the gate work (~1h).** Of the plumbing logged on 22 August the surviving useful piece is generating the `## Statement` box from the `.tex`, so there are two objects to keep in step rather than three; plus versioning the `statement_sha` hash basis (it is a hash of content x normalizer version: `c/0004/lean/MATCH.md` pins `f1912b71...` while the frontmatter reads `85c5fd1b...`, the mathematics unchanged, the basis moved when `_ARTIFACT_ROW_RE` entered `statement_text_for_hash` in `0556b94`), and gating `MATCH.md`'s recorded hash against the page's.

- [ ] **Run the harvester over `latex/harvest/` and promote what survives (~size unknown — this is the largest item in the file; batch it, don't run it all at once)**

  Requested 19 August 2026: process the PDFs in `latex/harvest/` into conjectures, faithfulness-check each against its source PDF, publish the survivors to `c/`, and let the pipeline move processed PDFs out of the way. The pipeline for exactly this already exists end to end (`scripts/harvest_conjectures.py`, prompts in `prompts/harvest.md`, documented in `latex/harvest/README.md`) and is why this is a log-and-batch item rather than a from-scratch build:

  - **Extract → ground → verify → typeset → compile.** Every candidate conjecture must carry verbatim, page-numbered quotes for its statement and its openness; those quotes are checked against the PDF's own text layer (not by a model) before anything is written; a second, independent model call sees only the PDF and the drafted record and is asked to *refute* it — that's the faithfulness check the request asks for, already built in rather than a step to add. `--dry-run`, `--limit N` and `--report` are there for exactly the batching this needs.
  - **The harvester does not recurse.** `HARVEST.glob("*.pdf")` (`scripts/harvest_conjectures.py`) only sees files directly in `latex/harvest/`, never in the 16 author subfolders below it — those subfolders are `arxiv-dl`/`iacr-dl`'s bulk-download staging area, a separate stage upstream of the harvester proper. The script does accept explicit paths as positional args (e.g. `"latex/harvest/Jens Groth"/*.pdf`), so a subfolder can be harvested without first flattening it, and `move_to_processed` works from any source path — but nothing runs on a subfolder by just calling the script with no arguments. `./prune-papers` (dedup against `processed/` by filename, run 19 August 2026: removed 8 exact duplicates) is worth running before any of this, regardless of which folder is targeted next.
  - **Progress, 19 August 2026: the single loose PDF at `latex/harvest/1701.06321v2.pdf` was run** (this was the actually-requested scope; a batch accidentally started against Jens Groth's 11-paper subfolder was caught and fully reverted mid-run — 5 papers it had already processed were unwound from `processed/harvest-log.json` and moved back, none had produced a conjecture, so nothing else needed undoing). The single PDF (Barak–Kothari–Steurer, *Quantum entanglement, sum of squares, and the log rank conjecture*, STOC 2017) yielded 2 candidates, both flagged `faithful-with-corrections` by the adversarial check — one for attributing an unhedged "would improve" to the authors where the paper says "may", one for requiring a *deterministic* algorithm where the paper's own rounding step is randomized. Both were independently re-verified against the source PDF (not just trusted from `SOURCE.md`) before publishing; the typeset step had already applied the corrections. A forward literature check on both was also run before publishing — worth doing given the "Credibility and distribution" tension below, and it mattered here: a same-month paper (arXiv:2608.10147, August 2026) looked at first pass like it might resolve one of the two, and turned out on closer reading to stay in a different regime. Published as [c/0048](/c/0048/) and [c/0049](/c/0049/).
  - **Progress, 23 August 2026: the eight loose PDFs at the top level of `latex/harvest/` were run** — all of it in-session rather than through the script, because **neither model backend was available on this machine**: no `claude` CLI binary on `PATH`, no Anthropic SDK, no API credentials, so `pick_backend()` had nothing to return. The mechanical halves of the pipeline were still used and still load-bearing: every quote was grounded with `PdfDoc.ground` imported from `scripts/harvest_conjectures.py` itself (38 quotes, 36 `exact`, 2 `near`, 0 ungrounded, 0 page mismatches — and it earned its keep, catching one span typed from memory rather than copied), and each draft was built with `pdflatex`/`chktex`/`lacheck`. `processed/harvest-log.json` was written by hand in the script's own schema, so `--report` reads the batch back correctly and the eight will never be re-read. **Two host dependencies had to be installed to get this far**: `poppler` (the repo says `brew install poppler`, "it is not optional here" — without it neither `pdftotext` nor the PDF reader works at all) and `PyYAML` from `requirements.txt` (without it `build_index.py`, `check_relations.py` and `gen_topics.py` all skip silently, and the pre-commit hook says so rather than blocking).

    Four conjectures survived, from three of the eight papers, all in one new hub, [p/short-collision-time-space-tradeoffs](/problems/short-collision-time-space-tradeoffs/): [c/0050](/c/0050/) (the Merkle-Damgård STB conjecture, from ePrint 2020/770), [c/0051](/c/0051/) (the sponge STB conjecture) and [c/0052](/c/0052/) (whether the multi-instance two-block sponge attack lifts to auxiliary input) from ePrint 2023/1444, and [c/0053](/c/0053/) (a tight quantum two-block Merkle-Damgård bound, from ePrint 2022/885). c/0051 and c/0052 carry a *conditional* `refutes`/`refuted-by` edge: an affirmative answer to c/0052 kills c/0051 in the regime ST³ > C, and nothing is refuted yet.

    **The forward literature check is what earned its place this round, again.** Unruh's ePrint 2007/168 has a whole "Open questions" section with three numbered conjectures, and every one is resolved: Conjecture 14 disproved by Dodis–Guo–Katz, Conjecture 16 by Coretti–Dodis–Guo and Tessaro, and — the one that would otherwise have been published — **Conjecture 15 settled affirmatively by Dodis, Jain, Lin, Luo and Wichs, FOCS 2024** (ePrint 2026/854), which cites it as `[Unr07b; Conjecture 15]` and titles its §5.1 "Resolving Unruh's Conjecture". A 2007 paper's open-problems section is exactly the shape of thing that reads as a safe harvest and is not.

    **Four of the eight papers yielded nothing, and the reasons are worth keeping.** ePrint 2024/1171 (tight DDH time-space tradeoffs) *poses* nothing — it only resolves other people's open questions, which is a correct and common result. ePrint 2017/937 (Coretti–Dodis–Guo–Steinberger) has two open questions, both unstateable: "we conjecture that ST/P suffices for most natural indistinguishability applications" has no formal referent, and "classify precisely the type of indistinguishability applications where such hybrid reduction can be applied" is a programme. ePrint 2020/296 (multidimensional database reconstruction) leaves a Diophantine equation unsolved but takes no position on it — it says the solution count "appears" that it "may" be unbounded while adopting the opposite as a working heuristic, so there is no statement at the paper's strength to publish. And **ePrint 2025/1258's one real conjecture is already published as [c/0010](/c/0010/)**, harvested from that paper by hand before this batch and before the paper was in the ledger; its other two items are a programme and a question with no account of what blocks it. All of this is recorded per-document in `processed/harvest-log.json`.

    Two citation errors were caught in self-review after the pages were written, both the kind the verify step exists for: ePrint 2020/770's Theorem 8 (the zero-walk bound) carries side conditions `B ≤ T` **and** `SB ≥ T`, and the first draft dropped the second; and ePrint 2023/1444's Theorem 1 is informal on p. 3 with its formal version as Theorem 8 on p. 14, not on p. 14 outright. Both fixed in the drafts and the pages, with the PDFs rebuilt and `artifact_manifest.py --update` re-run.

  - **Progress, 23 August 2026 (second batch): the fifteen loose PDFs dropped at the top level after the first batch were run**, in-session again and for the same reason — `pick_backend()` still has nothing to return on this machine. Three of the fifteen (2022/885, 2023/1444, 2024/1171) were byte-identical duplicates of papers already in the ledger; they were moved to `pruned/` rather than into `processed/` a second time, which is what the "stop the harvester re-reading papers" item above says the script should do and currently does not. The remaining twelve were read in full. Every quote was grounded with `PdfDoc.ground` from the script itself — **23 quotes, 23 `exact`, 0 `near`, 0 ungrounded**, with two claimed page numbers corrected by the grounder (a definition on p. 9 not p. 8, a remark on p. 19 not p. 18) — and each draft was built with `pdflatex`/`chktex`/`lacheck` and its `SOURCE.md` rendered by the script's own `write_source_note`. The ledger now holds **78 documents against 78 PDFs in `processed/`**, no orphans in either direction.

    Three conjectures survived, from two of the twelve papers, in two new hubs. [p/circular-security-and-composability](/p/circular-security-and-composability/) holds [c/0054](/c/0054/) and [c/0055](/c/0055/), Micciancio's two conjectures from ePrint 2024/1545 — that a fully composable homomorphic encryption scheme can always be turned into a circular-secure one, and that every encryption scheme has a partner making a two-scheme key cycle safe to publish. [p/quantum-presampling](/p/quantum-presampling/) holds [c/0056](/c/0056/), Guo–Li–Liu–Zhang's Conjecture 4 from ePrint 2020/1589: classical bit-fixing presampling against a quantum distinguisher, which their own Theorem 4 shows implies the folklore conjecture that quantum speedups need structure. No relation edges were drawn between c/0054 and c/0055: neither implies the other, the source says so, and the hub carries the connection instead.

    **The forward literature check killed the two best candidates in the batch, both from the same 2025 paper.** ePrint 2020/693's headline open problem — that the quantum time-space tradeoff for inverting *permutations* is `ST + T² = Θ̃(N)`, which its authors say they cannot prove "due to a lack of compressed permutation oracles" — was **resolved** by Akshima, Besselman, Chung, Guo and Yang, *Tight Quantum Time-Space Tradeoffs for Permutation Inversion* (arXiv:2510.12112, October 2025), which says "In this work, we resolve this open problem" and bypasses the missing compressed permutation oracle with Rosmanis's representation theory. The *same paper's Lemma 2* is, verbatim, ePrint 2020/1589's **Conjecture 7** (`GOWF` is `O((P+T²)/N)`-secure in the `P`-BF-QRPM), in the same rejection-sampling bit-fixing model. Two conjectures from two different papers, both dead, both from one arXiv posting ten months old, and neither would have been caught by reading the source PDFs alone. A third, 2020/693's question about the exponent on the success probability for quantum advice, was resolved by Liu (EUROCRYPT 2023), which quotes the question and answers it.

    **One deliberate non-harvest, recorded so the decision is visible.** ePrint 2020/1589 leaves a real gap on salted Merkle-Damgård collision resistance in the AI-QROM — its Theorem 2 proves `Õ(ST³/M)`, the best known attack gives `ST²/M + T³/M`, and it says "Further closing this gap is an intriguing question" — but it commits to no value, so publishing it would mean fixing a direction the source does not. The site already carries one page of exactly that shape, [c/0053](/c/0053/) for the two-block case, with a caveat saying the direction is the page's own reading; a second guess of the same kind is inventing a conjecture, not harvesting one. Left in the ledger's `rejected` list instead.

    **Nine of the twelve papers yielded nothing, and the reasons cluster.** Three answer their own question inside the paper (2026/295 asks whether sublinear-in-circuit-size OT-based OLE is possible and provides "a positive answer"; 2020/1555's existence question for LWE-based NIKE is settled affirmatively *in its own framework* by its Theorem 4 under iO, leaving only "from LWE alone" and "practical", neither of which is a proposition; 2025/1700 solves the open problem it inherits). Four leave only programmes (2024/1506's "explore the space between search and decision problems", 2021/523's "finding the right model to combine fast refresh with slow refresh", 2025/1700's three formalization directions, 2026/255's named limitations with no claim about lifting them). One leaves nothing at all — 2021/1002 has no conclusion, no future-work section and answers its main question completely. And 2026/877's two future-work questions are an assumption-removal with no stated obstruction and a packing optimization, while its SP-RLWE "conjecture" is a security assumption about its own construction, which `prompts/harvest.md` rejects by name. All twelve are recorded per-document in `processed/harvest-log.json`, with the quoted sentence and the reason.

    **Two things worth knowing before the next batch.** `pdftotext -layout` output is frequently classified as binary (a stray control byte somewhere in 40 pages), and **`grep` silently returns nothing on those files** — the first scan of this batch reported "no open problems" for two papers that have them. Strip control characters (`tr -d '\000-\010\013\016-\037'`) before scanning. And the text layer drops tall delimiters: the absolute-value bars around a distinguishing advantage in 2020/1589's Conjecture 4 are invisible in `pdftotext` output and were confirmed by rendering the page at 150 dpi and reading it. Anything with `\left|...\right|`, `\binom` or a tall fraction needs the same treatment before it is transcribed.

  - **Progress, 23 August 2026 (third batch): the nine loose PDFs left at the top level were run** — all nine Couteau-co-authored (a loose copy of part of his author folder), 401 pages, all fresh against the ledger by hash *and* filename, none duplicated in the author subfolders, so nothing was routed to `pruned/` this time. In-session again, for the third time and the same reason: no `claude` binary on `PATH`, no `anthropic` module, no `ANTHROPIC_API_KEY`, so `pick_backend()` has nothing to return. The mechanical halves earned their keep again — **19 quotes grounded with `PdfDoc.ground`, 18 `exact`, 1 `near`, 0 ungrounded**, two claimed page numbers corrected before anything was written (the asymptotic-parameters passage is on p. 16, not 19), plus 14 more quotes grounded for the ledger's rejection reasons, of which two more page numbers were corrected. Each draft builds clean under `pdflatex`/`chktex`/`lacheck` and each `SOURCE.md` was rendered by the script's own `write_source_note`. The ledger now holds **87 documents against 87 PDFs in `processed/`**, no orphans and no hash mismatches in either direction.

    Three conjectures survived, **all from one paper**, in one new hub: [p/pcfs-from-sparse-lpn](/p/pcfs-from-sparse-lpn/) holds [c/0057](/c/0057/), [c/0058](/c/0058/) and [c/0059](/c/0059/), all from Braun–Couteau–Melissaris–Riahinia–Sadeghi, *Fast Pseudorandom Correlation Functions from Sparse LPN* (ePrint 2025/1644, ASIACRYPT 2025). Its "Open Questions" paragraph poses two — a PCF from sparse LPN secure against subexponentially many queries rather than only superpolynomially many, and a weak PCF from sparse LPN in the standard model — and c/0057 and c/0058 carry reciprocal `variant-of` edges, because they are two axes of one construction and neither implies the other. The third, c/0059, is different in kind and is the more interesting harvest: not a question the paper asks but **a claim it asserts and does not prove**, that the dual-distance bound it computes over F_2 lower-bounds the bound over larger fields. Every large-field sparse-LPN parameter set in this literature depends on it, the source says so ("All previous works assume that the bound does not degrade as the field size grows"), and both sides are explicit finite sums, so one parameter triple could refute it.

    **A numerical probe was run for c/0059, and it is the reason to trust that page's mathematics.** Both printed bounds were reimplemented in exact rational arithmetic, and the F_2 side was validated against the source's own Table 2 first: it reproduces the published `D` exactly at `n = 2^15, m/n = 32, rho = 40` for `k = 7,8,9,10` (1574, 1948, 2244, 2478) and lands exactly 2 high at three other spot checks, a last-term boundary effect. On the general-field side the bound rises with `p` at every parameter set probed, consistent with the claim. Two things the probe surfaced that the source does not mention, both now on the page: the comparison is **vacuous** at every dimension where the general-field side is computable, because the F_2 regular bound is trivial below about `n = 2^11`; and part of what makes the source's sentence plausible may be the **ensemble** difference rather than the field, since exact-weight-k rows collide with probability 1/C(n,k) while block-regular rows collide with probability (k/n)^k — at `n = 512, k = 10` that is 97 against 1.

    **Both logged caveats from the second batch paid off, and a third joined them.** Stripping control characters before scanning was necessary. Rendering pages before transcribing tall mathematics was *load-bearing*: the source's `N := n/k` comes out of the text layer as `N := nk`, with the fraction flattened, and c/0059's definitions would have been wrong had they been typed from `pdftotext`. The new one: **`pdftotext -layout` interleaves the columns of two-column ACM papers so badly that a scan of the result is meaningless.** 2025/1475 (ASIA CCS 2026) reported no open-problem language on the first pass for that reason alone and had to be re-extracted without `-layout` before it could be read at all. Check the extraction before believing a negative.

    **The forward literature check found no kills this round, and instead found corroboration.** ePrint 2025/2002 (Hasler–Reisert, December 2025) reuses the source's recursion for OLE and multiparty Beaver triples and inherits *both* open questions verbatim — "the expansion is still asymptotically smaller than the subexponential expansion of previous PCFs" and "The random oracle is inherent to our construction ... Therefore, we do not obtain a weak PCF in the standard model" — which is the strongest available evidence that c/0058's obstruction is structural rather than an artefact of one write-up. ePrint 2026/1355 (Ishai–Krawczyk–Rabin, July 2026) cites the source as state of the art without touching either question. For c/0059 the nearest result is ePrint 2026/1753, which proves a *different* ensemble's distance bound in a "field-uniform form" — adjacent, not a resolution. One citation invented in a first draft was caught in self-review: the Brzuska et al. hash-then-evaluate paper is ePrint 2023/1145, not the 2024 number first written down.

    **Eight of the nine papers yielded nothing, and the reasons are unusually clean.** Four answer their own framing question inside the paper (2025/094 poses removing the HSS setup round and *is* the removal; 2025/2325 asks whether garbled circuits can be generated silently and "answer[s] the question in the affirmative"; 2025/1053's two framing questions are its own two theorems; 2025/966 solves the N-party HSS problem it opens with). One is superseded from **inside this batch**: 2025/269's "our techniques do not extend to protocols with N > 10 parties" is broken by 2025/966, two of the same authors, which gets any polynomial N — worth noting that a batch can invalidate itself, so read the batch before harvesting from it. Two have no open-problem content at all (2025/1475, an applied FIDO2 systems paper; 2025/1803, whose conclusion invites reuse of a technique). And 2025/268 states its gap only as a direction it "seek[s] to advance". All nine are in `processed/harvest-log.json` with the quoted sentence and the reason.

    **One structural observation for the next batch.** All three surviving conjectures come from one paper and all nine papers share one co-author, so this batch's whole yield is co-authored by Geoffroy Couteau. That is the Mahmoody concentration problem in miniature — see the review-request item above, where twelve of one author's statements is called out as an ask nobody can make. Worth capping how many statements from one author's work go up in a single sitting, or at least knowing the count before writing the review request.


  - **Progress, 23 August 2026 (fourth batch): the fourteen loose PDFs dropped at the top level after the third batch were run** — Itai Dinur's corpus this time, 618 pages, all fresh against the ledger by hash and by filename. Two of them (2021/885, 2022/028) are byte-identical to copies sitting in the `Yuval Ishai/` author folder, which were never processed, so they were *not* duplicates for this run — but those two folder copies are duplicates now, and `prune-papers` matches on basename, so running it would catch them. In-session again, fourth time, same reason. **22 quotes grounded for the three drafts, 21 `exact`, 1 `near`, 0 ungrounded**, plus 22 more grounded for the ledger's rejection reasons, all exact. The ledger now holds **101 documents against 101 PDFs in `processed/`**, no orphans, no hash mismatches.

    A much richer batch than the three that preceded it, and the reason is the corpus: Dinur's papers state their open problems, often as numbered conjectures with formulas. **Three conjectures survived, from two papers, in two new hubs.** [p/adaptivity-in-preprocessing-tradeoffs](/p/adaptivity-in-preprocessing-tradeoffs/) holds [c/0060](/c/0060/) and [c/0061](/c/0061/), both from Dinur–Keller–Marmor's *Non-Adaptive Cryptanalytic Time-Space Lower Bounds via a Shearer-like Inequality for Permutations* (ePrint 2025/783, STOC 2026): the conjectured `O~(T²/N + rST/N)` tradeoff for generic DLOG with preprocessing and `r` rounds of adaptivity, whose two endpoints — `r = 1` (their own Theorem 1.1) and `r = T` (Corrigan-Gibbs–Kogan) — are *both already theorems* and which is matched at every `r` by an attack they describe in one line; and their conjecture that Theorem 1.2's `sqrt(ST/N)` term is not tight for DDH, where the right answer is `ST/N`. [p/multidimensional-lphs](/p/multidimensional-lphs/) holds [c/0062](/c/0062/), Boyle–Dinur–Gilboa–Ishai–Keller–Klein's conjecture (ePrint 2022/028, ITCS 2022) that their printed `Random-Walk-Hash` algorithm is an optimal two-dimensional locality-preserving hash for shifts.

    **c/0062 is the best-documented conjecture harvested so far, and worth reading as a template.** Everything is on the page: the algorithm in full (three short procedures), a *matching lower bound* that is the source's own Theorem 1.4, the intended analysis written out by the authors, and the precise point where it fails — the analysis needs the random walk's steps to be independent, and the algorithm's loop-breaking rule (which both parties must share for the scheme to work at all) correlates them. The authors even say what they would rather have: "If the algorithm would make monotone queries along (at least) one axis ... then it would avoid loops and its analysis would be much simpler. Unfortunately, we do not know how to design such an algorithm with similar performance."

    **The rendering caveat paid for itself for the third batch running.** `Random-Walk-Hash`'s final step size is `sqrt(d'/2)`; the text layer flattens the radical and reads as `sqrt(d')/2`, a different algorithm. It was transcribed from a 150 dpi render of PDF p. 25. A new numbering caveat joined the list: in ePrint 2025/783 **the printed page numbers run one behind the PDF's**, so every citation on c/0060 and c/0061 carries both numbers — the same failure mode TASKS already records for the GUC paper.

    **Two rejections were close enough to be worth arguing with.** ePrint 2024/929 conjectures that its own multi-user bound for even `r` "is not tight in all settings" but names no value for the truth and offers "improving this bound (or devising a matching attack)" as alternatives, so it commits to no direction — the contrast with c/0061, where the same author's other paper conjectures non-tightness *and names the right bound*, is exactly the line this project draws. And ePrint 2026/1192 (Alon–Dinur) asks whether its lower bound extends beyond query-bounded reductions, but its own §2.1.3 argues the unrestricted notion is definitionally awkward — "Such reductions are arguably not black-box" — so the paper leans *against* the direction a page would have to fix; its headline question, the minimal number of PRG calls needed for a PRF, commits to no value either. Both are recorded in full in the ledger.

    **Eleven of the fourteen yielded nothing, and this batch's reasons are almost all one of two shapes.** Gap-closing with no committed side (2021/1460's "improve our lower bound ... or alternatively, improve the k-tree algorithm", 2023/288's fourth question) and programmes about a method's reach (2020/229's "find more problems in cryptography for which ...", 2020/188's "many new and interesting open questions", 2021/885's "how to better exploit the structured matrices", 2023/288's three "can we use similar techniques to ..." items). Then attack engineering (2022/424 twice, 2021/885, 2021/578), security assumptions about the paper's own candidates (2021/885's wPRF and PRG parameter sets, rejected by name in prompts/harvest.md), one routine extension the authors call "not difficult" (2024/338), and two papers with no open-problem content at all (2023/171 and 2025/1326, neither of which has a conclusion section).

    **Same-author concentration, again, and worse.** All fourteen papers share a co-author, and the review-request problem flagged after the third batch now has two instances: three statements from Couteau's work and three from Dinur's, all AI-written and unreviewed. Before the next batch it is worth deciding whether the author-folder staging area should be harvested author-by-author at all, since it guarantees this shape.
  - **What's still waiting**, counted 23 August 2026 after the batch above: **1,066** PDFs across 39 author subfolders, all genuinely untouched. The top level is now empty, so nothing runs by invoking the script with no arguments. The tree is far bigger than the 403 this entry claimed until today: Giulio Malavolta 82, Yuval Ishai 77, Takashi Yamakawa 56, Geoffroy Couteau 52, Daniel Wichs 46, Vinod Vaikuntanathan 45, Aggelos Kiayias 44, Stefano Tessaro 43, Prabhanjan Ananth 39, Amit Sahai 38, Ilan Komargodski 37, Rafael Pass 36, Dakshita Khurana 35, Hoeteck Wee 33, Huijia Lin 32, Krzysztof Pietrzak 30, Aayush Jain 29, Ron Rothblum 28, Benny Applebaum 27, Tomoyuki Morimae 26, Zvika Brakerski 24, Qipeng Liu 23, Nir Bitansky 21, Alon Rosen 21, Daniele Micciancio 20, Alex Lombardi 20, Yanyi Liu 16, Alexander Russell 14, Divesh Aggarwal 13, Luowen Qian 12, Jeremiah Blocki 11, Jens Groth 11, Andrej Bogdanov 11, Siyao Guo 8, Noah Stephens-Davidowitz 6, and four empty folders (Joel Alwen, Dominique Unruh, Boaz Barak, Akshima). `scripts/draft_status.py` reported 53 drafts in `latex/conjectures/` against 52 pages in `c/` when this was counted; after the second batch of 23 August it is 56 against 55, with the same **two** pre-existing non-promotions as before (`polynomial-compatibility`, `simon-oracle-simultaneous-inversion` — both intentionally merged into sibling pages, not oversights; see their `SOURCE.md`). The top level of `latex/harvest/` is empty again, and `processed/` holds 78.
  - **Promotion is the part that isn't automated**, and it's real per-draft judgment, not a script: follow `latex/README.md` § "Publishing a draft". The doc's own prose says to create `open-problems/<topic>/<slug>/`; that's stale — every live example (`c/0001` through `c/0049`) is a flat `c/<id>/` (4-digit, zero-padded, next free number) with `latex/` and `pdf/` subfolders, no topic, no `open-problems/`, so follow the working examples over the doc text. Hand-write `draft: <folder-name>` under `problem:` in the new page — folder names and `problem:` slugs never match automatically. Two undocumented pre-commit-hook requirements bit the 18 August batch twice, and a third gate exists that the README doesn't mention at all: an empty `<!-- status:start/end -->` block before `scripts/status_badge.py` will touch a page; `python3 scripts/artifact_manifest.py --update` after the PDF is in place; and `scripts/tab_structure.py --check` requires the body's *only* `##` headings, inside one `::: {.panel-tabset}`, to be exactly `Statement | Proof | Discussion | Open obligations`, in that order, with `### Sources` nested inside `Statement` rather than a separate tab.
  - **This is exactly the tension the "Credibility and distribution" section opens with.** 1,066 unread PDFs could plausibly produce several hundred new conjectures, every one landing with `proof_review: ai` on a site where that's already true of all statements and almost none has been read by a person. Don't run `--all` in one sitting: harvest and promote in small batches, and weigh this against the steering-member-review and prior-resolution-sweep tasks above rather than letting it silently outrun them.

- [ ] **Finish the Uber-assumption paper and run the checks on it (~1.5h — uncertain: the remaining mathematics is real work, not write-up)**

  `latex/papers/uber-groups-rsr/main.tex` ("The Uber Assumption and its Random Self-Reducibility, in Non-Bilinear and Type 1, 2, 3 Bilinear Groups") is ~1,290 lines across 13 sections and compiles clean, but it is still a working draft — the last four commits were all substantive mathematics (2026-08-15/16: house-class conversion, a strengthened separation result, the decision procedure recast in standard algebra primitives). Finish it, then put it through the checks.

  Publishing is done — `projects/uber-groups-rsr/` exists, badge generated, PDF and LaTeX copies in place, listed under Papers → Archive. Two of the checks are done too, and are recorded in a "Checks run" section on the page itself rather than only in `git log`:

  - **Bibliography: verified, 16 August 2026.** All seventeen entries checked against their sources — author list, title, venue, volume, page range, year — including the two the paper leans on hardest, Galbraith–Paterson–Smart (*Discrete Applied Mathematics* 156(16):3113–3121, 2008) for the type classification and Boyen (Pairing 2008, LNCS 5209, pp. 39–56) for the Uber baseline. Nothing fabricated, misdated or misattributed, and the preliminary-version notes on Blum–Luby–Rubinfeld, Regev and Escala et al. check out. Nothing further owed here.
  - **`chktex` and `lacheck`: clean, 16 August 2026.** Two genuine hits fixed (intersentence spacing after "co-CDH", a missing `~` before a `\ref`), two source-hygiene spaces tidied, one inline suppression on the `\Span` definition. `latex/papers/uber-groups-rsr/.chktexrc` pins the four suppressed warnings with a documented reason each — 3, 24 and 36 as expected, plus 8, which fires only on correct en-dashes here and cannot mask a *missing* one. Re-run with `chktex -q -l .chktexrc main.tex` from that directory.

  What is actually left:

  - **Finish the mathematics.** The blocking item, and the author's. This is what keeps `status_summary` reading "working draft" and `proof_review` at `ai`.
  - **Run the four prompts.** None have been run yet: `prompts/proof.md` (the idealized-model audit — the paper lives in the generic-group model, squarely in its scope), then `prompts/style.md` and `prompts/latex.md` for typesetting, and `prompts/revise.md` for prose. Note `prompts/revise.md` enforces "no em-dashes in prose" as a hard invariant and the paper currently has 39, so that pass is not cosmetic.

- [ ] **Translate *UC for Gamers* into Persian and typeset it right-to-left (~9h — the translation is the bulk of the hours, the RTL rework is where it can go wrong; placed last in this section per the "new books" ordering above)**

  Requested 23 August 2026. The book is the project's own content, so there is no permission question — only a translation question and a typesetting one, and they are separable.

  **What is being translated.** `latex/books/uc-for-gamers/main.tex`: one file, 9,570 lines, ~62,300 words of extractable prose (76,200 words of source with comments stripped; 345 comment lines, which are notes to the maintainer and should *not* be translated), compiling to 211 pages. Thirty `\chapter`s, 29 `\section`s, and the bulk of the mathematics inside 130 `algorithmic` blocks, 38 `interface` boxes, 37 `definition`s, 47 `proof`s, 29 `proposition`s, 8 `procedure`s and 8 `tikzpicture`s.

  **Pick the source first, and it is not obvious.** There are two divergent copies in the tree and they differ by 634 lines:
  - `latex/books/uc-for-gamers/main.tex` — the single-file book, 5.5×8.5in trade-paperback geometry, carries the notation block inline (lines 282–427), and is the one with a committed `main.pdf`.
  - `surveys/uc-for-gamers/latex/main.tex` — the modular edition the *site* publishes: 8,970 lines plus `ucgamers.sty` (209 lines) and 61 files under `functionalities/`, listed in `_quarto.yml` and hashed in `artifacts.json`, served from `surveys/uc-for-gamers/index.qmd` as HTML + PDF + LaTeX source.

  Translating the book copy is easier (one file, no `.sty` indirection) but strands the result outside the site's build; translating the survey copy inherits `scripts/build_uc_html.sh` and the artifacts manifest but multiplies the file count by 60. Decide before starting, and reconcile the two English copies first if they have drifted in content rather than only in packaging — otherwise the Persian edition silently forks a third version.

  **The preamble does not survive the switch to XeLaTeX, and that is the real work.** Persian needs `xepersian` (or `polyglossia`+`bidi`) under XeLaTeX; the current preamble is pdfTeX-era and four of its font lines become errors: `\usepackage[T1]{fontenc}`, `\usepackage[utf8]{inputenc}`, `mathpazo`, `eulervm` and `[scaled=0.90]{helvet}` all have to be replaced with `fontspec` equivalents plus a Latin-math choice that still looks like the English edition (Palatino-with-Euler is the current pairing; `newpxmath`/`newpxtext` or Asana Math under `unicode-math` are the candidates). Beyond fonts, expect trouble in exactly the places this book is dense: `bidi` has documented conflicts with `tcolorbox` (all four box styles — functionality, procedure, definition, theorem-like — are `tcolorbox`), with `titlesec` (which this preamble uses for a hand-built running head that reads `\botmark` and hooks `\refstepcounter` — see the long comment at lines 92–120, it is fragile and *will* need re-testing under RTL), with `algpseudocode` (130 blocks, and pseudocode conventionally stays LTR inside an RTL document), and with `multicols` (18 uses). The 8 TikZ diagrams need node text translated and their layout mirrored or deliberately left LTR. `microtype`'s protrusion is only partly available under XeTeX. Budget the preamble rework as its own pass, ahead of any translation, and keep it in a separate `.sty` so the English book is not touched.

  **Fonts: nothing suitable is installed, verified 23 August 2026.** The toolchain itself is fine — `xelatex`, `lualatex`, `latexmk`, and `xepersian.sty`, `polyglossia.sty`, `bidi.sty`, `fontspec.sty` are all present (TeX Live 20260301 via Homebrew). But there is no Vazirmatn, no XB family, no Noto Naskh Arabic, and no Persian font registered with fontconfig; TeX Live ships only `nazli` as Type 1 (for `arabi`, useless to XeLaTeX) and Amiri as TrueType inside `texmf-dist`, which `fontspec` cannot find by name. A probe compiled clean only with an explicit path:

  ```
  \settextfont[Path=/opt/homebrew/.../fonts/truetype/public/amiri/,
    Extension=.ttf,UprightFont=Amiri-Regular,BoldFont=Amiri-Bold]{Amiri}
  ```

  Amiri is an Arabic naskh, not a Persian face, and it has no matching sans for the box titles. The right move is to install Vazirmatn (SIL OFL, has a real weight range and a sans character that suits the box furniture) or the XB family, and pin the font by path in the new `.sty` so the build is reproducible on a machine that has not installed anything system-wide. Also noted from the probe: `pdftotext` on Arabic-script XeTeX output returns presentation-form glyphs, so the Persian PDF will not be searchable or copy-pasteable the way the English one is unless a font mapping is set up — check this before declaring the PDF done.

  **Translation policy has to be written down before the first chapter, not after.** Persian cryptography terminology is not settled, and this book coins heavily in English ("guard", "silencer", "mediator", "blocker", "absorption lemma", "identical until bad", "responsive calls", "sanitization"). Decide once and record it in a glossary file committed alongside the translation: which terms are translated, which are transliterated, which stay in Latin script, and whether the English term is parenthesized at first use. Keep every identifier, macro name, label, `\ref` target and bibliography entry in Latin script and untranslated — the 61 functionality names, `\Fsig`, `\Zenv` and the rest are notation, not prose. The bibliography stays as published. The AI-disclosure on the title page must be translated too, not dropped.

  **Deliverables.** Translated source, the new RTL style file, a compiled PDF, the glossary, and a decision recorded on whether this becomes a site page (a Persian `surveys/uc-for-gamers/fa/` or its own path) or stays a `latex/` draft. If it goes on the site, it needs its own `proof_review`/disclosure treatment like every other page, and the translation is unreviewed by a Persian-speaking cryptographer — say so on the page rather than letting it read as authoritative.
