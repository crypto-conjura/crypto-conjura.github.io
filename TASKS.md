# Tasks

Split into two sections: **Website and repository** (~5.5h) covers the site, its build tooling and the repository's configuration; **Conjectures and papers** (~7.5h) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~21.0h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `6d01888` on 17 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

## Website and repository

- [ ] **Simplify the Steering page: names first, each with a home icon (~0.5h — manual: real people's names, affiliations and links)**

  Requested 17 August 2026. `steering/index.qmd` is ten paragraphs wrapped
  around a seven-name list. Wanted: the names at the top, each linking to that
  person's own page through a house icon, a line saying the project wants more
  steering members, and a note that Pooya Farshim currently maintains the
  project.

  Homepages, each fetched and confirmed to return 200 on 17 August 2026 — link
  these rather than re-deriving them:

  - Manuel Barbosa — `https://www.dcc.fc.up.pt/~mbb/`
  - Pooya Farshim — `https://farshim.github.io/`
  - Denis Firsov — `https://firsov.ee/`
  - Jens Groth — `http://www0.cs.ucl.ac.uk/staff/j.groth/`
  - Mohammad Mahmoody — `https://www.cs.virginia.edu/~mohammad/`
  - Christian Rechberger — `https://www.isec.tugraz.at/person/christian-rechberger/`
  - Stefano Tessaro — `https://homes.cs.washington.edu/~tessaro/`

  Two of those need a decision rather than a paste. **Groth's page serves over
  `http` only** — `https://www0.cs.ucl.ac.uk/...` and
  `https://www.cs.ucl.ac.uk/staff/J.Groth/` both failed to connect from here,
  while the `http` URL returned 200 and its CV is dated April 2026, so the page
  is maintained and it is the TLS that is missing. An `http` link on an `https`
  site is a mixed-content nag in some browsers; retest, and if it still fails,
  either link it anyway with the plain URL or link his Nexus author page (he is
  Chief Scientist there) instead. **Rechberger's page** answers on both
  `iaik.tugraz.at` and `isec.tugraz.at` with the same content, the institute
  having rebranded to ISEC — prefer the `isec` URL so the link does not depend
  on a redirect.

  One factual error to fix while rewriting the list: the page lists **Mohammad
  Mahmoody under "Bilkent University"**, and his own homepage says he is an
  associate professor in the Computer Science Department at the **University of
  Virginia**. Correct it or drop affiliations from the list entirely — do not
  publish it as it stands. Jens Groth is the one name with no affiliation at all
  today.

  Icon mechanics, so this does not turn into a dependency hunt: `_extensions/`
  does not exist and no `.qmd` on the site uses an icon shortcode, but
  `_quarto.yml`'s `navbar.right: - icon: github` proves Quarto's bundled
  Bootstrap Icons ship with the theme, so an inline `<i class="bi
  bi-house-door-fill">` needs no extension. Confirm that in the rendered
  `_site` output rather than assuming it. An icon-only link has no accessible
  name, so each one needs an `aria-label` naming the person; and the colour
  should come from a `.cj-`-prefixed class defined in both `theme-light.scss`
  and `theme-dark.scss` rather than being hard-coded, the way every other custom
  element on the site is done.

  What "much simpler" should not cut: the sentence that support is not an
  endorsement or a review of any statement, the line that anyone listed can ask
  to be removed without giving a reason, and the pointer to the
  [provenance badge](/open-problems/status-legend/) — those exist because the
  page puts real people's names next to unreviewed AI-written mathematics. The
  recruiting line should say the project is looking for more steering members in
  **cryptography, formal methods and DevOps, and anyone who can bring tokens**,
  and it belongs folded into the existing "Supporting the project" list (Review,
  Problems, Compute and bounties) rather than added as a second list saying the
  same thing.

- [ ] **One page listing every UC functionality (~0.5h)**

  Requested 18 August 2026. `uc/index.qmd` offers only a "Browse" list of the nine layer pages, so seeing all 104 functionalities means opening nine tables and holding the result in your head. There is no cross-layer view, and no way to answer "which entries are written" without `python3 scripts/uc_status.py --check` (currently 16 `Defined`, 88 `Not yet written`, 0 `No canonical definition`).

  The precedent to copy is `open-problems/all/index.qmd`, which is the same page for statements and is four lines of frontmatter. Put the new one at `uc/all/index.qmd`, titled to match ("All functionalities"), and link it from `uc/index.qmd` above the Browse list — the layer list should stay, since it carries the dependency ordering the flat table cannot.

  It needs no generator. Statements have `_generated/all.yml` because badges are computed by `scripts/build_index.py`; a functionality's four fields are already in its own frontmatter, all 104 pages carry all four, so a plain Quarto listing does it:

  ```
  listing:
    id: all-functionalities
    contents: "../layer-*/*/index.qmd"
    type: table
    fields: [title, layer, status, definition]
    sort: [layer, title]
  ```

  Four things to get right, each of which has already bitten this repo:

  - **The glob must not swallow the layer index pages.** `../layer-*/*/index.qmd` matches entries only; `../layer-*/index.qmd` would add nine rows that are not functionalities.
  - **`layer:` is a bare integer 0–8**, not a name, so a Layer column reads "0" where the layer pages read "Idealized Setup and Resources". Either map the number to its name in a listing template (the mechanics are in `_listing-templates/statement-table.ejs.md`, whose header comment records that the engine is lodash templates and not full EJS) or set `field-display-names` and accept the number as a sort key. Do not invent a `layer_name:` field on 104 pages to avoid the choice.
  - **`sort-ui: false` on a 104-row table is worth reconsidering.** The layer tables set it because eight rows do not need sorting; this one is the page where filtering by `definition` or by `status` earns its keep. If a filter box is added, note the same template comment: Quarto's own "no matching items" div is un-hidden from a List.js event that never fires on a listing with no filter UI, which is why that template says it itself.
  - **The sidebar entry is the usual trap.** `_quarto.yml:112` has `uc/index.qmd` as a plain leaf under the Surveys section. Turning it into a `section:` with the new page as its only child is what `open-problems` does, but a `section:` needs `contents:` or Quarto renders it as an inert `<span>` and drops the href — the bug already recorded in the project notes. Adding the child is optional; linking from `uc/index.qmd` is not.

  Status values across the 104 entries, for whoever designs the columns: 71 `Canonical`, 16 `Idealized Setup`, 9 `Emerging`, 8 `Open`.

- [ ] **Stop encyclopedia macros from asking for a book rebuild (~0.5h)**

  Requested 17 August 2026, after the first three entries filled under the new artifact gate hit it. Every new functionality box needs one `\newcommand{\Fxxx}` in `surveys/uc-for-gamers/latex/ucgamers.sty`, because `scripts/gen_interface.py` reads macro meanings from that file and nowhere else. `ucgamers.sty` is a genuine input of the book, so `scripts/artifact_manifest.py --check` then reports the PDF and the HTML edition as stale and asks for `pdflatex main.tex` plus the four-minute `scripts/build_uc_html.sh` — for a macro the book never expands. Doing that 88 more times is 88 rebuilds and 88 title pages re-dated by `\today`, which is the *only* thing a rebuild changes: verified on 17 August by rebuilding at three passes and diffing the text layer, 211 pages, identical but for `August 15, 2026` → `August 17, 2026`.

  Half of the fix has landed: `artifact_manifest.py` now derives the book's inputs from the `\input{functionalities/...}` lines in `main.tex` instead of globbing `latex/**/*`, so adding a *fragment* no longer trips the gate. The remaining half is the `.sty`. Split the encyclopedia-only macro block — everything under the "Functionalities of the encyclopedia that the book does not itself typeset" comment — into its own file, say `functionalities/encyclopedia.sty`, and leave `ucgamers.sty` to the book. Four consumers read those macros and all four need the second file: `gen_interface.py`'s `load_macros`, `functionalities/preview.tex` (which is what `--vs-preview` compiles), `scripts/build_uc_html.sh` (which injects the macros into MathJax), and `main.tex` itself, which must *not* load it — the point of the split. Then `book_inputs()` in `artifact_manifest.py` needs no further change, since it already globs only `latex/*.sty`, and a new entry's macro stops being a book event.

  Do not simply drop `ucgamers.sty` from the watched inputs: a real edit to the book's notation must still invalidate the PDF, which is the whole reason that gate exists.

- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  88 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs — measured 17 August 2026, replacing the 97-of-104 figure this entry carried before. Sixteen are written: the seven ported from `surveys/uc-for-gamers/latex/main.tex` (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, F-AC), then F-CRS, F-COM, F-ZK, F-auth, F-OT, G-RO, and — 17 August — F-smt, F-MCOM and F-BC. Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. Run `python3 scripts/uc_status.py --check` for the current count rather than trusting this number.

  The tooling for this now exists end to end, so this is a matter of running it 97 times rather than inventing the process each time:

  - `scripts/uc_source.py <id>` does the mechanical half. It reads the page's own reference bullets, resolves each to a PDF (newest ePrint revision, falling back to the PostScript-only postings the 1990s papers still are), records every revision stamp, scans the text layer for interface-box titles, renders the pages carrying a box named after the functionality into `<id>/_src/`, and writes `<id>/_src/sources.json` with URL, revision, page and a ready-made citation pointer. The PNGs are gitignored — a proceedings figure is the publisher's — and `_src/` is `_`-prefixed so Quarto never publishes it; the manifest is committed and reproduces the images exactly.
  - `prompts/source.md` is the per-stub prompt, rewritten 16 August 2026 around that harvest: choose among the cited definitions in a fixed order (same object first, then revision/formulation/framework currency, then a tie-break ladder), capture the original as reviewer evidence, rewrite it in the book's notation, keep a mismatch register.
  - `scripts/gen_interface.py` turns the `.tex` fragment into the page's box with the line numbering computed and CI-gated, and `--vs-preview` compiles a fragment standalone to prove LaTeX prints the line numbers the generator computed — the check `--vs-pdf` cannot do for the 97 boxes the book does not typeset.

  Three things the runs so far have established, worth knowing before the next one. **A stub's own citations are often not where the definition is printed**: F-BC's three references include Canetti's framework paper, which prints no broadcast box at all, and the definition taken came from the two adaptive-broadcast papers instead. **A citation that yields no box is a result, not a gap** — Rabin 1981 contains no `F_OT` because it predates ideal functionalities, and Pfitzmann–Waidner's secure message transmission is an ideal *system* in the reactive-simulatability model, not a UC functionality; both pages say so. And **F-SFE has no printed box under that name** in either paper it cites (`uc/layer-6-secret-sharing-mpc/f-sfe/_src/sources.json` records that CLOS 2002 prints F_bc, F_cp, F_mcom, F_ot and F_zk, and no F_sfe), so that entry needs a forward literature search before it can be written, or a page saying the functionality is folklore.

  One earlier fact still stands: 11 of the stubs cite nothing at all (F-RP, F-CRHF, F-MHF, F-OWF, F-PRG, F-ABE, F-IBE, F-GC, F-ORAM, F-PIR, F-PSI), so they need a literature search before the harvester has anything to work with; and a citation that yields no box is a normal, informative result — Rabin 1981 contains no `F_OT`, because it predates ideal functionalities, and the page should say so rather than force one.

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

  Toolchain is pinned: `leanprover/lean4:v4.33.0`, Mathlib at the revision in `lake-manifest.json`. Keep `AuditProof.lean` passing throughout, since its entire purpose is that no declaration quietly acquires `sorryAx`, and update `LEDGER.md` as items close rather than at the end. Partial progress is worth committing: the ledger is designed for it, and an honest "items 1 to 3 done, 6 untouched" is more useful than nothing.

## Conjectures and papers

- [ ] **Promote the 10 remaining harvested drafts (~3h — manual: every statement is AI output over someone else's paper, and every citation needs verifying)**

  Requested 17 August 2026; the first group was published 18 August as
  [c/0019](/c/0019/), [c/0020](/c/0020/) and [c/0021](/c/0021/) under the new
  hub `p/black-box-uselessness/`, which leaves ten drafts. All are marked
  `[harvested, unread]` — written by `scripts/harvest_conjectures.py` from PDFs,
  with `SOURCE.md` saying in as many words that "nothing here was checked by a
  human yet". Promoting one is an editorial act, not a build, which is why no
  gate fails on the backlog (`--check` exits 0 on an unpromoted draft by design;
  see `latex/README.md`).

  **Four things the first group established, which will save the next one time.**
  *Drafts can be duplicates of each other*: `simon-oracle-amplification` and
  `simon-oracle-simultaneous-inversion` were both ePrint 2021/016's Conjecture
  6.7, written up twice, and became one statement — check the conjecture
  environments against each other before allocating an id, since ids are never
  reused. **`polynomial-compatibility` and `polynomial-compatibility-2` are the
  obvious next candidates for this**, and they come from *different* papers
  (2022/218 and 2023/570), so the check is whether the two papers state the same
  conjecture. *The corrections in `SOURCE.md` were already applied to the
  `.tex`*: that file preserves what the adversarial checker asked for, and is not
  a list of outstanding defects — diff it against the LaTeX rather than assuming
  either way. *The bibliographic details verify*: all eight source papers were
  checked against ePrint metadata on 18 August, correcting three the harvester
  had inferred (2023/571's title carries "Constructions and Lower Bounds";
  2022/1285 is TCC 2022; 2023/570 is EUROCRYPT 2023). *Crossref works where DBLP
  rate-limits*: `api.crossref.org/works?query.bibliographic=` verified every
  cited paper's authors, year and pages without being throttled.

  The ten, grouped by the paper each was harvested from — one promotion per
  draft, but the source reading is shared within a group:

  - **Austrin, Chung, Chung, Fu, Lin & Mahmoody, "On the Impossibility of Key
    Agreements from Quantum Random Oracles" (ePrint 2022/218, preprint)** —
    `caqb-imperfect-completeness`, `polynomial-compatibility`.
  - **Afshar, Couteau, Mahmoody & Sadeghi, "Fine-Grained Non-Interactive
    Key-Exchange: Constructions and Lower Bounds" (ePrint 2023/571, EUROCRYPT
    2023)** — `mggm-4nike-quadratic`, `sggm-3nike-quadratic-attack`.
  - **Mahmoody, Qi & Rahimi, "Lower Bounds for the Number of Decryption Updates
    in Registration-Based Encryption" (ePrint 2022/1285, TCC 2022)** —
    `rbe-dynamic-update-times`, `rbe-loglog-update-gap`.
  - One each from **Afshar, Chung, Hsieh, Lin & Mahmoody, "On the
    (Im)possibility of Time-Lock Puzzles in the Quantum Random Oracle Model"
    (ePrint 2023/932, preprint; the ASIACRYPT 2023 version is under a slightly
    different title)** — `fully-quantum-tlp-attack`; **Buxbaum & Mahmoody, "A
    Note on the Minimality of One-Way Functions in Post-Quantum Cryptography"
    (ePrint 2024/2095, CiC 2024)** — `nonblackbox-owf-minimality`;
    **Chung, Lin & Mahmoody, "Black-Box Separations for Non-Interactive
    Commitments in a Quantum World" (ePrint 2023/570, EUROCRYPT 2023)** —
    `polynomial-compatibility-2`; **Etesami, Gao, Mahloujifar & Mahmoody,
    "Polynomial-time targeted attacks on coin tossing for any number of
    corruptions" (ePrint 2021/1464, TCC 2021)** —
    `optimal-martingale-gap-finders`.

  Every line above is now the ePrint record rather than the harvester's guess,
  checked on 18 August 2026. What is still unverified is each draft's *internal*
  bibliography — the prior work it cites — which has to be checked per draft
  before it appears on a page, the way the first group's six were.

  Mechanics, so this does not turn into a discovery exercise:

  - `latex/README.md` § "Publishing a draft" is the procedure. The `.tex` and
    compiled PDF are copied into the new page's `latex/` and `pdf/`
    subfolders (both tracked), and the statement is transcribed into
    `index.qmd`. Model the frontmatter on `c/0018/`, the most recent page.
  - **`draft: <folder-name>` under `problem:` is the only link back**, and has
    to be written by hand — folder names are never the `problem:` slug, and
    `groth16/statement.tex` and `split-nilp/statement.tex` are byte-identical
    yet belong to different pages. Omit it and `draft_status.py` reports the
    draft unpromoted forever.
  - Most of these need a **new `p/<problem>/` page** too. `p/` now holds 14
    problems, none covering quantum random oracles, fine-grained NIKE, RBE
    update bounds, or coin-tossing attacks; `p/black-box-uselessness/` was
    added for the first group and is the model to copy — motivation, provenance
    with the ePrint link, a parameter lattice, and the list of statements. Where
    two drafts share a problem they should share one `p/` page and become
    sibling `c/` ids, the way `c/0019`–`c/0021` now do.
  - **Two page mechanics that are easy to miss**, both of which cost a failed
    gate the first time: a new leaf needs an empty
    `<!-- status:start --> ... <!-- status:end -->` pair in the body before
    `status_badge.py` will write anything into it, and `statement_sha: ""` is
    filled by that same script rather than by hand. A new `c/<id>/latex/` +
    `pdf/` pair is also a new artifact, so `artifact_manifest.py --update` has
    to run after the PDF is compiled or the publish workflow fails.
  - `areas` must come from the 19 fixed slugs (`scripts/build_index.py`
    validates); `quantum`, `public-key`, `impossibility-results` and
    `foundations` already exist as listing folders. Nothing needs adding to the
    taxonomy.

  Three judgment calls that should be made deliberately rather than in passing:

  - **`sggm-3nike-quadratic-attack` and `fully-quantum-tlp-attack` are phrased
    as attacks**, not conjectures. Check whether each is an open question or a
    result the source paper proves — the harvester's known failure mode is
    handing back a strengthening of a theorem the paper already has. If it is
    not open, it does not belong in `c/` at all.
  - **Two near-duplicate pairs.** `simon-oracle-amplification` and
    `simon-oracle-simultaneous-inversion` differ only by "Given a" vs "With a"
    in their titles, and `polynomial-compatibility` /
    `polynomial-compatibility-2` are variants of one statement. Their
    `statement.tex` files are *not* byte-identical, so these are four distinct
    documents — decide per pair whether that is two statements or one drafted
    twice, and delete rather than promote a redundant draft.
  - **Leave `c/0006` empty.** It was removed on purpose (`e99c874`, "it was a
    test placeholder, not a statement"), nothing in the tree references it, and
    the next promotion should start at `c/0019`. The gap in the sequence is not
    a missing page.

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
