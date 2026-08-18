# Tasks

Split into two sections: **Website and repository** (~5.0h) covers the site, its build tooling and the repository's configuration; **Conjectures and papers** (~4.5h) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~17.5h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `cbb23c7` on 18 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

## Website and repository

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
