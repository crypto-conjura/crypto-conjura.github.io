# Tasks

Split into three sections. **Credibility and distribution** (~4.5h) covers review, prior-art checking, and — as of 19 August 2026 — the legal/security/governance items below; it is first because the project's binding constraint is there rather than in content supply. **Website and repository** (~24h) covers the site, its build tooling, the repository's configuration, and the product/data-model redesign added 19 August 2026. **Conjectures and papers** (~4.5h, plus one unbounded item added 19 August 2026 — see below) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty, *except* where noted: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools, anything needing a lawyer or a GitHub org owner) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~33h** (rough; the UC Encyclopedia content, the new data-model item, and the new harvest-and-promote item all dominate the uncertainty — the last of these has no meaningful estimate since 403 unread PDFs are waiting and the count of conjectures they'll yield is unknown until it's run).

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
  semantics in `problems/status-legend/` so the ask names exactly which
  flag a review moves and what it does not claim.

## Website and repository

- [ ] **List proposals in the same style as problems, built to scale — this is a data-model change, not a CSS one (~3h)**

  Requested 20 August 2026, with the explicit expectation that many more proposals are coming — worth designing for that up front rather than reskinning the current page and hitting the same wall `problems/by-area/` hit before it was fixed 19 August.

  **Why this can't be "just make it look like the table."** The problems listings (`problems/all/`, `problems/by-area/`, `problems/by-topic/`) all work the same way: `scripts/build_index.py` reads structured frontmatter from every `c/<id>/index.qmd`, emits `_generated/<facet>/<value>.yml`, and a Quarto `listing:` block renders that YAML through `_listing-templates/statement-table.ejs.md` — sortable table, status badge, clickable tag chips, one row per statement. `projects/proposals/index.qmd` today (84 lines, 8 entries from the 19/20 August programmes merge) is the opposite: hand-written prose, one `### Paper Title` / `#### Direction` / quote / description block per entry, no frontmatter, nothing a script could read. Matching the *look* without matching the *data shape* means hand-formatting an ever-growing wall of prose into table rows by hand, forever — the thing "a lot more will be added" is specifically warning against.

  **Recommended shape, mirroring the `c/` pattern at a scale that fits what a proposal actually is:**
  - Each proposal gets its own small page, `projects/proposals/<slug>/index.qmd`, with light frontmatter — no Lean, no sigma/pi status badge (a proposal has no proof to grade, unlike a statement): `title`, `short_title`, `source` (citation + URL), `topics` (reuse the 19 August `TOPIC_SLUGS` taxonomy rather than inventing a second one), `date_added`, and a `status` simpler than a statement's (e.g. `open` / `claimed` / `resolved-into: c/00NN`). The existing 8 entries migrate into 8 such pages as the first step, not left inline.
  - `projects/proposals/index.qmd` becomes an index/listing page like `problems/all/index.qmd`: a small generator (a leaner sibling of `build_index.py`, or an extension of it — decide which when this is picked up) walks `projects/proposals/*/index.qmd`, writes `_generated/proposals/all.yml`, and a `listing:` block renders it through a proposals-specific template (a trimmed copy of `statement-table.ejs.md` — same tag-chip rendering for `topics`, no status-badge SVG column since there's nothing to grade yet).
  - Add a `--check` gate for the new generator and wire it into `.githooks/pre-commit` and `.github/workflows/publish.yml`, matching every other generated-content gate on this site (`gen_topics.py`'s is the most recent example, 19 August).

  **The one design call worth confirming before building, since it changes the file count:** per-proposal pages (recommended above, matches "problems" most literally and gives each proposal a stable URL to cite/link once one graduates into a real statement) vs. keeping everything on one page with a generated table at the top linking to same-page anchors below (less scalable as the count grows, but avoids ~50+ tiny files if proposals turn out to be numerous and short-lived). Decide explicitly; don't default to whichever is less code today if it doesn't hold up once "a lot more" actually arrive.

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
  `support/index.qmd` § "Supporting the project" was rewritten the same day
  on direct instruction, to different supplied copy — dropping the scarcity
  ordering this entry was written against, and dropping the "cost of
  attacking a problem should come down to compute anyone can bring" sentence
  entirely (confirmed intentional, not an oversight, when asked). The
  six-item analysis immediately below is against the *old* text and needs
  re-checking against the new one before this entry is run; the "must not
  drop the compute-not-budget argument" instruction at the end of this entry
  no longer applies and should be removed once the rest is re-checked, not
  followed.

  `support/index.qmd` § "Supporting the project" was, as of 18 August 2026, a
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

  46 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs, three are marked *No canonical definition*, and fifty-five are written — measured 18 August 2026. Run `python3 scripts/uc_status.py --check` for the current split rather than trusting these numbers. Added 18 August: F-acc, F-TSIG, F-adsig, F-NIZK, F-PUF, then F-aPAKE, F-saPAKE, F-VSS, F-ABB, F-dauth, then F-SNARK, F-thdec and F-DKG with F-eqv and F-NMCOM as *No canonical definition*, alongside the forty-two already listed in `git log`.

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
  judgment), `f-snark` ($\mathcal{F}_{\textsc{weak-nizk}}$, Kosba et al.), `f-ba` ($\mathcal{F}_{\mathsf{csf}}$,
  Cohen et al.), `f-fhe` ($\mathcal{F}_{\mathsf{ABB}}$ and $\mathcal{F}_{\mathsf{Decrypt}}$ — the first is
  arguably `f-abb`'s object, not this one), `f-mac` and `f-kdf` (both inside Küsters--Tuengerthal's single
  $\mathcal{F}_{\mathsf{crypto}}$ library, so one reading serves two entries), `f-se`
  ($\mathcal{F}_{\mathsf{senc}}$, Figures 10--12 — three figures, a sitting of its own) and `f-secmsg`
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

  **Still located and unwritten, from the same grep:** `f-se` ($\\mathcal{F}_{\\mathsf{senc}}$,
  K\u00fcsters--Tuengerthal Figures 10--12, about 120 lines over three pages -- a sitting of its own),
  `f-secmsg` ($\\mathcal{F}_{\\mathsf{SM}}$, Figure 7, entangled with four sibling modules), `f-chan`
  (state channels, Dziembowski et al.), `f-cred` ($\\mathcal{F}_{\\mathsf{daa}}$ -- DAA, a naming judgment
  against "credentials"), `f-snark` ($\\mathcal{F}_{\\textsc{weak-nizk}}$, Kosba et al.), `f-ba`
  ($\\mathcal{F}_{\\mathsf{csf}}$ and the wrapper family, Cohen et al.), `f-fhe`
  ($\\mathcal{F}_{\\mathsf{Decrypt}}$; its $\\mathcal{F}_{\\mathsf{ABB}}$ hit belongs to `f-abb`, now
  written), and `f-mac`/`f-kdf` (both inside one $\\mathcal{F}_{\\mathsf{crypto}}$ library).

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

- [ ] **Run the harvester over `latex/harvest/` and promote what survives (~size unknown — this is the largest item in the file; batch it, don't run it all at once)**

  Requested 19 August 2026: process the PDFs in `latex/harvest/` into conjectures, faithfulness-check each against its source PDF, publish the survivors to `c/`, and let the pipeline move processed PDFs out of the way. The pipeline for exactly this already exists end to end (`scripts/harvest_conjectures.py`, prompts in `prompts/harvest.md`, documented in `latex/harvest/README.md`) and is why this is a log-and-batch item rather than a from-scratch build:

  - **Extract → ground → verify → typeset → compile.** Every candidate conjecture must carry verbatim, page-numbered quotes for its statement and its openness; those quotes are checked against the PDF's own text layer (not by a model) before anything is written; a second, independent model call sees only the PDF and the drafted record and is asked to *refute* it — that's the faithfulness check the request asks for, already built in rather than a step to add. `--dry-run`, `--limit N` and `--report` are there for exactly the batching this needs.
  - **The harvester does not recurse.** `HARVEST.glob("*.pdf")` (`scripts/harvest_conjectures.py`) only sees files directly in `latex/harvest/`, never in the 16 author subfolders below it — those subfolders are `arxiv-dl`/`iacr-dl`'s bulk-download staging area, a separate stage upstream of the harvester proper. The script does accept explicit paths as positional args (e.g. `"latex/harvest/Jens Groth"/*.pdf`), so a subfolder can be harvested without first flattening it, and `move_to_processed` works from any source path — but nothing runs on a subfolder by just calling the script with no arguments. `./prune-papers` (dedup against `processed/` by filename, run 19 August 2026: removed 8 exact duplicates) is worth running before any of this, regardless of which folder is targeted next.
  - **Progress, 19 August 2026: the single loose PDF at `latex/harvest/1701.06321v2.pdf` was run** (this was the actually-requested scope; a batch accidentally started against Jens Groth's 11-paper subfolder was caught and fully reverted mid-run — 5 papers it had already processed were unwound from `processed/harvest-log.json` and moved back, none had produced a conjecture, so nothing else needed undoing). The single PDF (Barak–Kothari–Steurer, *Quantum entanglement, sum of squares, and the log rank conjecture*, STOC 2017) yielded 2 candidates, both flagged `faithful-with-corrections` by the adversarial check — one for attributing an unhedged "would improve" to the authors where the paper says "may", one for requiring a *deterministic* algorithm where the paper's own rounding step is randomized. Both were independently re-verified against the source PDF (not just trusted from `SOURCE.md`) before publishing; the typeset step had already applied the corrections. A forward literature check on both was also run before publishing — worth doing given the "Credibility and distribution" tension below, and it mattered here: a same-month paper (arXiv:2608.10147, August 2026) looked at first pass like it might resolve one of the two, and turned out on closer reading to stay in a different regime. Published as [c/0048](/c/0048/) and [c/0049](/c/0049/).
  - **What's still waiting**, unchanged by the above: 403 PDFs across the same 16 authors' folders (Yuval Ishai 77, Geoffroy Couteau 52, Aggelos Kiayias 50, Stefano Tessaro 47, Prabhanjan Ananth 39, Benny Applebaum 27, Qipeng Liu 23, Alex Lombardi 20, Alexander Russell 18, Divesh Aggarwal 13, Luowen Qian 12, Jens Groth 11, Siyao Guo 8, Noah Stephens-Davidowitz 6; Boaz Barak and Dominique Unruh folders exist but are empty) — genuinely untouched, not merely reverted-and-equivalent. `scripts/draft_status.py --report` now shows 50 draft folders in `latex/conjectures/`, 48 promoted to `c/`, and the same **two** pre-existing non-promotions as before (`polynomial-compatibility`, `simon-oracle-simultaneous-inversion` — both intentionally merged into sibling pages, not oversights; see their `SOURCE.md`).
  - **Promotion is the part that isn't automated**, and it's real per-draft judgment, not a script: follow `latex/README.md` § "Publishing a draft". The doc's own prose says to create `open-problems/<topic>/<slug>/`; that's stale — every live example (`c/0001` through `c/0049`) is a flat `c/<id>/` (4-digit, zero-padded, next free number) with `latex/` and `pdf/` subfolders, no topic, no `open-problems/`, so follow the working examples over the doc text. Hand-write `draft: <folder-name>` under `problem:` in the new page — folder names and `problem:` slugs never match automatically. Two undocumented pre-commit-hook requirements bit the 18 August batch twice, and a third gate exists that the README doesn't mention at all: an empty `<!-- status:start/end -->` block before `scripts/status_badge.py` will touch a page; `python3 scripts/artifact_manifest.py --update` after the PDF is in place; and `scripts/tab_structure.py --check` requires the body's *only* `##` headings, inside one `::: {.panel-tabset}`, to be exactly `Statement | Proof | Discussion | Open obligations`, in that order, with `### Sources` nested inside `Statement` rather than a separate tab.
  - **This is exactly the tension the "Credibility and distribution" section opens with.** 403 unread PDFs could plausibly produce well over 100 new conjectures, every one landing with `proof_review: ai` on a site where that's already true of all statements and almost none has been read by a person. Don't run `--all` in one sitting: harvest and promote in small batches, and weigh this against the steering-member-review and prior-resolution-sweep tasks above rather than letting it silently outrun them.

- [ ] **Finish the Uber-assumption paper and run the checks on it (~1.5h — uncertain: the remaining mathematics is real work, not write-up)**

  `latex/papers/uber-groups-rsr/main.tex` ("The Uber Assumption and its Random Self-Reducibility, in Non-Bilinear and Type 1, 2, 3 Bilinear Groups") is ~1,290 lines across 13 sections and compiles clean, but it is still a working draft — the last four commits were all substantive mathematics (2026-08-15/16: house-class conversion, a strengthened separation result, the decision procedure recast in standard algebra primitives). Finish it, then put it through the checks.

  Publishing is done — `projects/uber-groups-rsr/` exists, badge generated, PDF and LaTeX copies in place, listed under Papers → Archive. Two of the checks are done too, and are recorded in a "Checks run" section on the page itself rather than only in `git log`:

  - **Bibliography: verified, 16 August 2026.** All seventeen entries checked against their sources — author list, title, venue, volume, page range, year — including the two the paper leans on hardest, Galbraith–Paterson–Smart (*Discrete Applied Mathematics* 156(16):3113–3121, 2008) for the type classification and Boyen (Pairing 2008, LNCS 5209, pp. 39–56) for the Uber baseline. Nothing fabricated, misdated or misattributed, and the preliminary-version notes on Blum–Luby–Rubinfeld, Regev and Escala et al. check out. Nothing further owed here.
  - **`chktex` and `lacheck`: clean, 16 August 2026.** Two genuine hits fixed (intersentence spacing after "co-CDH", a missing `~` before a `\ref`), two source-hygiene spaces tidied, one inline suppression on the `\Span` definition. `latex/papers/uber-groups-rsr/.chktexrc` pins the four suppressed warnings with a documented reason each — 3, 24 and 36 as expected, plus 8, which fires only on correct en-dashes here and cannot mask a *missing* one. Re-run with `chktex -q -l .chktexrc main.tex` from that directory.

  What is actually left:

  - **Finish the mathematics.** The blocking item, and the author's. This is what keeps `status_summary` reading "working draft" and `proof_review` at `ai`.
  - **Run the four prompts.** None have been run yet: `prompts/proof.md` (the idealized-model audit — the paper lives in the generic-group model, squarely in its scope), then `prompts/style.md` and `prompts/latex.md` for typesetting, and `prompts/revise.md` for prose. Note `prompts/revise.md` enforces "no em-dashes in prose" as a hard invariant and the paper currently has 39, so that pass is not cosmetic.

- [ ] **Attempt the Groth conjecture (~2h — highly uncertain: genuine open research, may not resolve regardless of time spent)**

  `c/0008` ("No Two-Element Split Non-Interactive Linear Proofs for Hard Relations") and `c/0009` ("Groth16 Proof-Size Optimality in the Pure Generic Group Model") are both open — whether a 2-element split NILP can be statistically sound against affine provers for any hard relation generator, equivalently whether Groth16's 3-group-element proof size is optimal in the pure GGM (no random oracle, non-interactive, publicly verifiable, generic prover). `p/groth16-proof-size-optimality/index.qmd` has the full parameter lattice and provenance: Groth (EUROCRYPT 2016) posed the 2-element question as his paper's own closing open problem; every subsequent result has attacked some restriction of the pure-GGM model rather than this exact cell. `c/0008` implies `c/0009`, so proving the stronger statement (`c/0008`) resolves both.
