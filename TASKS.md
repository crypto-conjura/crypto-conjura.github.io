# Tasks

Split into two sections: **Website and repository** (~7.5h) covers the site, its build tooling and the repository's configuration; **Conjectures and papers** (~14.0h) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~21.5h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `a278f80` on 17 August 2026.

Completed tasks are deleted from this file rather than checked off and kept: this is a list of live work, and `git log` is the record of what closed and when.

## Website and repository

- [ ] **A Formalizations section (~1h)**

  Lean artifacts exist and nothing on the site collects them. Four statements carry one (`c/0001` through `c/0004`), each reachable only from its own page through the `lean:` frontmatter block, so there is no way to ask what has been formalized, how far, or under which toolchain without opening all four.

  What the section should show, all of it derivable rather than typed:

  - **Which statements have an artifact**, from the `lean:` block already in the frontmatter: `mode`, `path`, `decl`, `toolchain`, and `commit` where the project is external.
  - **How far each one got.** `c/0001`, `c/0002` and `c/0003` are a statement and a single `sorry`, 37 to 49 lines each. `c/0004` is 476 sorry-free lines of `Proof.lean` under one open theorem. Those are very different states and the site currently reports both as "has Lean".
  - **What the axiom audit says.** `c/0004` already carries `Audit.lean` and `AuditProof.lean`, whose whole job is that nothing reports `sorryAx`. That result is the strongest evidence on the site and it is invisible from outside the folder.

  Generate it, do not maintain it by hand: a sorry count and a toolchain string are computable from the files, and this repository's rule is that anything computable is generated and CI-gated. The same reasoning as `definition:` on the UC entries.

  One thing to get right rather than fudge: a page listing formalizations must not let "formalized" mean two things. A compiled statement with an open proof and a compiled proof are different claims, and the badge already distinguishes them ($\sigma$ against $\pi$). The section should reuse that vocabulary rather than invent a second one.

- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  97 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs — measured 16 August 2026, and it corrects the 93-of-100 figure this entry carried before (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, and F-AC are the seven filled in, ported from `surveys/uc-for-gamers/latex/main.tex`). Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. No other functionality currently has a ready-made source of this quality to adapt from, so expect this to mean drafting from the literature directly rather than porting.

  The tooling for this now exists end to end, so this is a matter of running it 97 times rather than inventing the process each time:

  - `scripts/uc_source.py <id>` does the mechanical half. It reads the page's own reference bullets, resolves each to a PDF (newest ePrint revision, falling back to the PostScript-only postings the 1990s papers still are), records every revision stamp, scans the text layer for interface-box titles, renders the pages carrying a box named after the functionality into `<id>/_src/`, and writes `<id>/_src/sources.json` with URL, revision, page and a ready-made citation pointer. The PNGs are gitignored — a proceedings figure is the publisher's — and `_src/` is `_`-prefixed so Quarto never publishes it; the manifest is committed and reproduces the images exactly.
  - `prompts/source.md` is the per-stub prompt, rewritten 16 August 2026 around that harvest: choose among the cited definitions in a fixed order (same object first, then revision/formulation/framework currency, then a tie-break ladder), capture the original as reviewer evidence, rewrite it in the book's notation, keep a mismatch register.
  - `scripts/gen_interface.py` turns the `.tex` fragment into the page's box with the line numbering computed and CI-gated, and `--vs-preview` compiles a fragment standalone to prove LaTeX prints the line numbers the generator computed — the check `--vs-pdf` cannot do for the 97 boxes the book does not typeset.

  Two facts the tooling has already established about the shape of the job: 11 of the 97 stubs cite nothing at all (F-RP, F-CRHF, F-MHF, F-OWF, F-PRG, F-ABE, F-IBE, F-GC, F-ORAM, F-PIR, F-PSI), so they need a literature search before the harvester has anything to work with; and a citation that yields no box is a normal, informative result — Rabin 1981 contains no `F_OT`, because it predates ideal functionalities, and the page should say so rather than force one.

  What the estimate is still carrying is the part the tooling cannot shortcut: choosing between incompatible variants, and verifying every citation is a real paper at a real venue in a real year. Expect the mismatch registers to be the most interesting output, and expect some functionalities to have no canonical printed definition at all — that finding is itself a page worth having.

  One ordering trap, which turns CI red for the whole site: `gen_interface.py --check` runs in both workflows over every fragment in `functionalities/` and errors if a fragment's page has no `.cj-interface` block to replace. The page scaffold and the fragment must land in the same commit.

- [ ] **Regenerate derived artifacts when their `.tex` source changes (~1.5h)**

  Requested 17 August 2026. Every `.tex` on this site has generated output committed beside it, and nothing currently detects when the two have drifted apart. Editing a source and forgetting to rebuild leaves a PDF or an HTML edition that silently disagrees with the LaTeX it claims to come from, which on this site is a content error rather than a build annoyance.

  The pairs that exist today:

  - `c/<id>/latex/main.tex` → `c/<id>/pdf/main.pdf`, for eight statements.
  - `latex/papers/uber-groups-rsr/main.tex` → `papers/uber-groups-rsr/{latex,pdf}/`.
  - `surveys/uc-for-gamers/latex/main.tex` → `pdf/main.pdf` **and** the 59-page HTML edition under `html/`, via `scripts/build_uc_html.sh`.
  - `latex/uc/.../main.tex` → the UC encyclopedia interface boxes, via `scripts/gen_interface.py`.

  **The pattern to copy already exists.** `gen_interface.py --check` regenerates a page's box from its fragment and fails CI when the two disagree; `status_badge.py` hashes each `## Statement` block into `statement_sha` and forces a revision bump when it moves. Both run in `checks.yml` and `publish.yml` today. The new work is extending that idea from fragments to whole artifacts, not inventing a mechanism.

  Four things a naive implementation gets wrong:

  - **`main.tex` is not the only input.** A build also depends on `conjura-conjecture.cls`, `conjura-solution.cls`, `ucgamers.sty` and, for the book, 14 `functionalities/*.tex` fragments. Hashing only `main.tex` misses a class-file edit entirely — and the line-anchor work on 16 August broke in exactly this way, because a change confined to `functionalities/` was invisible to a check that looked only at the main file. Hash the whole input set, and record which files were in it.
  - **CI cannot build these today.** Both workflows run `ubuntu-latest`, and `build_uc_html.sh` hardcodes `/Library/TeX/texbin`, which is macOS-only, on top of needing TeX Live, `make4ht` and TeX Live's own `dvisvgm` rather than Homebrew's. A full TeX Live install in Actions costs minutes and about a gigabyte per run. Decide up front whether CI *builds* or merely *detects staleness*; the second is cheap and needs no TeX at all.
  - **Detect-and-fail is more in keeping than regenerate-and-commit.** A bot pushing regenerated artifacts cannot reach `main` anyway now that the branch ruleset requires pull requests, and silent regeneration is against the grain of a repository whose other gates deliberately refuse to fix things quietly (`status_badge.py` forces the revision bump rather than re-baselining). Failing with "`c/0004/pdf/main.pdf` is stale against its source, run X" is the smaller and more honest feature.
  - **The book build is slow.** `build_uc_html.sh` takes about four minutes end to end, measured repeatedly on 16 August. Running it on every push is not viable; running it only when its own input hashes change is the point of the feature.

  Suggested shape: a `scripts/artifact_manifest.py` writing a committed manifest of input-hash → outputs per artifact, with `--check` for CI and `--update` after a real rebuild, registered alongside the four existing gates. Local rebuilds stay manual; the script only ever says whether the committed output matches the committed source.

## Conjectures and papers

- [ ] **Mine IOG's 2026 research papers for open problems (~2.5h — manual: reading each paper for what it actually leaves open, and verifying every citation)**

  Requested 16 August 2026. Harvest the 2026 research papers from IOG's listing, read each for the problems it leaves open, and file what comes out in two places: open-ended directions as **proposals**, precise falsifiable claims as **conjectures**.

  The harvest is smaller than it looks, checked at source on 16 August 2026:

  - The listing is `https://www.iog.io/news?type=research-paper&page=N`, `N` from 1 to 15, 348 paper links in total. Pagination is `page=`, not `p=` — `p=2` silently returns page 1 again, which is how a scrape ends up harvesting the same twenty papers fifteen times.
  - **Only 19 are dated 2026, and all of them are on page 1**, since the listing is reverse-chronological. Pages 2 to 15 are 2025 and earlier. So the job is 19 papers, not 292.
  - Despite being a Next.js app, the listing HTML carries both the `/papers/<slug>` links and the "Month YYYY" dates, so plain `curl` is enough and Playwright is not needed. There is no public JSON behind it (`/api/papers` 404s).
  - Each detail page links its PDF directly, and for those checked it is IACR ePrint (e.g. `eprint.iacr.org/2026/1116.pdf`). Prefer the ePrint URL over any mirror: it is versioned, citable, and the revision is recoverable.

  Where the output goes, both of which already exist and neither of which needs inventing:

  - **Proposals** go in the "## Open proposals" section of `papers/proposals/index.qmd`, which is still the placeholder "No proposals have been posted yet" and carries a `callout-note` saying so — remove that callout when the first one lands. That page already defines a proposal as exactly what is wanted here: a focused research topic, narrower than a survey but not yet precise enough to be a conjecture.
  - **Conjectures** go in as statement leaves: `c/<next id>/` from `_templates/paper.qmd`'s sibling `_templates/statement.qmd`, under a problem hub in `p/`, which is what makes them appear under `/open-problems/`. Ids are sequential, allocated once and never reused; the highest today is `c/0009`. See CONTRIBUTING.md for the allocation and revision rules.

  Three things to get right:

  - **The split is a judgement, and most will be proposals.** A paper's closing "we leave X to future work" is usually a direction, not a statement. It is a conjecture only if it can be written so a referee could refute it. Do not inflate a hint into a formal claim to make the conjecture list longer; an honestly-filed proposal is worth more than a conjecture nobody can attack.
  - **Do not commit the PDFs.** They are the authors'. Follow the encyclopedia's precedent: `scripts/uc_source.py` already resolves references to ePrint PDFs, records URL, revision and page in a committed `sources.json`, and renders evidence images into a gitignored `_src/`. Copy that shape rather than a new one, and it may be worth extending that script rather than writing a second harvester.
  - **Every citation must be real.** Author, venue and year verified against the source, never reconstructed from memory. This is the standing rule on this site and the reason the estimate carries a manual flag.

  The CI gates apply to anything landing under `c/`: `status_badge.py`, `build_index.py` and `check_relations.py` all run before `quarto render`, so a leaf with an unregenerated badge or a dangling relation fails the deploy for everyone.

- [ ] **Finish the Uber-assumption paper and run the checks on it (~1.5h — uncertain: the remaining mathematics is real work, not write-up)**

  `latex/papers/uber-groups-rsr/main.tex` ("The Uber Assumption and its Random Self-Reducibility, in Non-Bilinear and Type 1, 2, 3 Bilinear Groups") is ~1,290 lines across 13 sections and compiles clean, but it is still a working draft — the last four commits were all substantive mathematics (2026-08-15/16: house-class conversion, a strengthened separation result, the decision procedure recast in standard algebra primitives). Finish it, then put it through the checks.

  Publishing is done — `papers/uber-groups-rsr/` exists, badge generated, PDF and LaTeX copies in place, listed under Papers → Archive. Two of the checks are done too, and are recorded in a "Checks run" section on the page itself rather than only in `git log`:

  - **Bibliography: verified, 16 August 2026.** All seventeen entries checked against their sources — author list, title, venue, volume, page range, year — including the two the paper leans on hardest, Galbraith–Paterson–Smart (*Discrete Applied Mathematics* 156(16):3113–3121, 2008) for the type classification and Boyen (Pairing 2008, LNCS 5209, pp. 39–56) for the Uber baseline. Nothing fabricated, misdated or misattributed, and the preliminary-version notes on Blum–Luby–Rubinfeld, Regev and Escala et al. check out. Nothing further owed here.
  - **`chktex` and `lacheck`: clean, 16 August 2026.** Two genuine hits fixed (intersentence spacing after "co-CDH", a missing `~` before a `\ref`), two source-hygiene spaces tidied, one inline suppression on the `\Span` definition. `latex/papers/uber-groups-rsr/.chktexrc` pins the four suppressed warnings with a documented reason each — 3, 24 and 36 as expected, plus 8, which fires only on correct en-dashes here and cannot mask a *missing* one. Re-run with `chktex -q -l .chktexrc main.tex` from that directory.

  What is actually left:

  - **Finish the mathematics.** The blocking item, and the author's. This is what keeps `status_summary` reading "working draft" and `proof_review` at `ai`.
  - **Run the four prompts.** None have been run yet: `prompts/proof.md` (the idealized-model audit — the paper lives in the generic-group model, squarely in its scope), then `prompts/style.md` and `prompts/latex.md` for typesetting, and `prompts/revise.md` for prose. Note `prompts/revise.md` enforces "no em-dashes in prose" as a hard invariant and the paper currently has 39, so that pass is not cosmetic.

- [ ] **Formalize the proof of LHL extraction, public seed (~8h, highly uncertain: real formalization, and one item is a project on its own)**

  `c/0004` is the only resolved statement on the site, and its proof is the obvious next artifact: the statement is formalized and matched, `Proof.lean` is 476 lines with no `sorry`, and everything is in place except the theorem itself. `c/0004/lean/Statement.lean:134` holds the single real `sorry`, on `Conjura0004.lhl_public_seed`. Discharging it is what moves `status.proof_formal` off `open`, and by the discipline recorded in `LEDGER.md` nothing else may move it.

  Do not re-derive the plan. `c/0004/lean/LEDGER.md` already lists what is proved and what is outstanding, in dependency order, and it was written to be picked up:

  - Items 1 to 3 are groundwork: dropping `[Fintype Z]` in favour of `tsum`, the second half of Lemma 3.1 (factoring the view distance as an average over rows, which is where publishing the seed does its work), and the attainment half of the predictor bound.
  - Items 4, 5, 7 and 8 are the flattening argument, the mean at fixed support, the uniform deviation bound and the final assembly.
  - **Item 6 is the one to size the task by.** Fact 2.2, bounded differences, in the finite special case. The ledger calls it "the single largest item, and the one Mathlib does not help with at all", and that was checked: Mathlib has no McDiarmid inequality and no bounded-differences lemma. It is a formalization project in its own right and could exceed the estimate for everything else combined.
  - Seven supporting facts are named and unattempted. Fact 2.5 is Jensen and is in Mathlib; Fact 2.7 needs the monotonicity of $(1-1/R)^R$ and is not the one-liner it looks like.

  Toolchain is pinned: `leanprover/lean4:v4.33.0`, Mathlib at the revision in `lake-manifest.json`. Keep `AuditProof.lean` passing throughout, since its entire purpose is that no declaration quietly acquires `sorryAx`, and update `LEDGER.md` as items close rather than at the end. Partial progress is worth committing: the ledger is designed for it, and an honest "items 1 to 3 done, 6 untouched" is more useful than nothing.

- [ ] **Attempt the Groth conjecture (~2h — highly uncertain: genuine open research, may not resolve regardless of time spent)**

  `c/0008` ("No Two-Element Split Non-Interactive Linear Proofs for Hard Relations") and `c/0009` ("Groth16 Proof-Size Optimality in the Pure Generic Group Model") are both open — whether a 2-element split NILP can be statistically sound against affine provers for any hard relation generator, equivalently whether Groth16's 3-group-element proof size is optimal in the pure GGM (no random oracle, non-interactive, publicly verifiable, generic prover). `p/groth16-proof-size-optimality/index.qmd` has the full parameter lattice and provenance: Groth (EUROCRYPT 2016) posed the 2-element question as his paper's own closing open problem; every subsequent result has attacked some restriction of the pure-GGM model rather than this exact cell. `c/0008` implies `c/0009`, so proving the stronger statement (`c/0008`) resolves both.
