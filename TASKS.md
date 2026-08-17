# Tasks

Split into two sections: **Website and repository** (~6.25h) covers the site, its build tooling and the repository's configuration; **Conjectures and papers** (~3.5h) covers the mathematics — proving conjectures, and writing and checking the papers that report them. Within each section, tasks are ordered by difficulty: web-related tweaks, new web content, new conjectures, new papers, new books, resolutions. Time estimates are wall-clock: how long Opus 5 Max (Max reasoning effort) actually takes to finish the task end-to-end once the prompt is given, plus a flat 5-minute buffer — not human labor-hours. Tasks with a real manual component the model can't shortcut (testing on physical devices, sourcing/verifying external PDFs and citations, actual audio/podcast production, troubleshooting third-party tools) are weighted up accordingly, flagged per task below. Keep new estimates calibrated the same way. Total estimated time: **~17.75h** (rough; the UC Encyclopedia content dominates the uncertainty and could run well over its estimate).

Last reconciled against `main` at `f8237dc` on 17 August 2026.

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

- [ ] **Add a refuted variant of the status badge — same geometry, red instead of green (~0.75h)**

  Today the badge has no way to say a statement turned out to be *false*. A
  machine-checked refutation and a machine-checked proof both land on `π = 4`
  and render the identical dark-green sealed badge, because the six graded
  fields say how well established the work is and nothing says which way it
  points. Wanted: the same badge as a proven conjecture, on a red ramp.

  The direction has to come from somewhere, so this needs a seventh field in
  the `status:` block — `proof_direction: proves | refutes` — optional and
  defaulting to `proves`, so all 18 existing statement pages and
  `papers/uber-groups-rsr/` keep their current badge byte-for-byte and CI stays
  green without touching them. It is deliberately *not* a grade: it must not
  enter σ or π, so `--self-test`'s monotonicity argument is unaffected. Add
  the constraint that `refutes` requires `proof_informal != open` (there is no
  refutation without a proof of one), alongside the two existing dependency
  constraints in `validate()`.

  Files, and why each one:

  - [scripts/status_badge.py](scripts/status_badge.py) — parse and default the
    field in `parse_status_block()` (same `setdefault` pattern as
    `FREE_TEXT_FIELDS`), validate it, then in `render_badge_svg()` add a
    `cj-refuted` modifier class to the `<svg>` and swap the π = 4 glyph from
    `✓` to `✗`. Keep the gold seal for a sealed refutation: the seal means
    de-Bruijn-complete, not "true". `render_caption()` should say
    "Refutation: …" in place of "Proof: …" — that caption is also the `<a>`'s
    `aria-label`, so it is what a screen reader announces.
  - [scripts/build_index.py](scripts/build_index.py) — listing tables do *not*
    reuse the rendered `status_badge:` string; `listing_item()` re-derives the
    badge from primitives (`badge_sigma`, `badge_pi`, `badge_sealed`,
    `badge_dash`, `badge_glyph`). Add `badge_refuted` and make `badge_glyph`
    direction-aware, or the red badge appears on statement pages only and
    silently stays green in every listing. Also accept the new field in the
    `STATUS_FIELDS` validation loop, which currently errors on anything
    missing and would need it as a separate optional dict.
  - [_listing-templates/statement-table.ejs.md:27](_listing-templates/statement-table.ejs.md#L27)
    — emit `cj-refuted` on the `<svg>` when `item.badge_refuted`.
  - [theme-light.scss:323-336](theme-light.scss#L323-L336) and
    [theme-dark.scss:325-338](theme-dark.scss#L325-L338) — add
    `.cj-refuted .cj-ring-N` / `.cj-refuted .cj-disc-N` overrides. Specificity
    (0,2,0) beats the existing (0,1,0) rules, so no `!important` is needed.
    Match the green ramp's lightness steps step for step, including
    `disc-4 == ring-5`, so a red badge reads as exactly as strong as a green
    one at equal grade rather than as a warning.
  - [open-problems/status-legend/index.qmd](open-problems/status-legend/index.qmd)
    — the legend is hand-written HTML, not generated: add the refuted rows to
    the symbol key and a fifth worked example (sealed refutation) to the
    example table, and update the "Reading the badge" paragraph.
  - [schema/index.qmd:37](schema/index.qmd#L37) — the `status` row still says
    "the six existing graded fields"; and
    [_templates/statement.qmd](_templates/statement.qmd), whose `status:` block
    is what every new leaf is copied from.

  One thing to get right rather than skip: red-vs-green is the classic
  colour-blind pair, so the direction must survive greyscale. The `✗` glyph
  does that at π = 4. At π = 1–3 (a refutation drafted but not formalized)
  colour is the *only* channel, and the honest fix is that the caption,
  `aria-label` and `status_summary` carry it in words — worth stating in the
  legend rather than leaving implied.

  Also worth fixing while in there, since the `✗` depends on it: the centre
  glyph is currently near-invisible at several grades. Light theme paints it
  `#2a2a28` over `disc-4` `#2e6b3f` (~1.6:1); dark theme paints it `#f5f4ef`
  over `disc-4` `#a8e092` and over `disc-0` `#ffffff`, so today's π = 0 badge
  has an invisible `–` in dark mode. A sibling selector on the `<text>` that
  directly follows the disc (`.cj-disc-4 + .cj-glyph`, etc.) flips the ink
  without touching the SVG, and the legend's standalone glyph examples, which
  have no preceding disc, are unaffected.

  No statement on the site is currently refuted, so nothing turns red on
  landing — the legend example is the only visible change until the first
  `proof_direction: refutes` is set. The `relations` vocabulary already has
  `refutes` / `refuted-by`, so the naming is consistent with what exists.

- [ ] **UC Encyclopedia content (~5h — manual: sourcing and verifying real citations per functionality, not just drafting text)**

  97 of the 104 functionality pages (`uc/layer-N-.../<id>/index.qmd`) are still stubs — measured 16 August 2026, and it corrects the 93-of-100 figure this entry carried before (F-Rand, F-Store, F-Sig, G-PKI, G-Clock, F-Net, and F-AC are the seven filled in, ported from `surveys/uc-for-gamers/latex/main.tex`). Fill in the rest incrementally, one functionality at a time: precise UC-style definition, known realizations, security properties, and any formal/Lean artifacts. No other functionality currently has a ready-made source of this quality to adapt from, so expect this to mean drafting from the literature directly rather than porting.

  The tooling for this now exists end to end, so this is a matter of running it 97 times rather than inventing the process each time:

  - `scripts/uc_source.py <id>` does the mechanical half. It reads the page's own reference bullets, resolves each to a PDF (newest ePrint revision, falling back to the PostScript-only postings the 1990s papers still are), records every revision stamp, scans the text layer for interface-box titles, renders the pages carrying a box named after the functionality into `<id>/_src/`, and writes `<id>/_src/sources.json` with URL, revision, page and a ready-made citation pointer. The PNGs are gitignored — a proceedings figure is the publisher's — and `_src/` is `_`-prefixed so Quarto never publishes it; the manifest is committed and reproduces the images exactly.
  - `prompts/source.md` is the per-stub prompt, rewritten 16 August 2026 around that harvest: choose among the cited definitions in a fixed order (same object first, then revision/formulation/framework currency, then a tie-break ladder), capture the original as reviewer evidence, rewrite it in the book's notation, keep a mismatch register.
  - `scripts/gen_interface.py` turns the `.tex` fragment into the page's box with the line numbering computed and CI-gated, and `--vs-preview` compiles a fragment standalone to prove LaTeX prints the line numbers the generator computed — the check `--vs-pdf` cannot do for the 97 boxes the book does not typeset.

  Two facts the tooling has already established about the shape of the job: 11 of the 97 stubs cite nothing at all (F-RP, F-CRHF, F-MHF, F-OWF, F-PRG, F-ABE, F-IBE, F-GC, F-ORAM, F-PIR, F-PSI), so they need a literature search before the harvester has anything to work with; and a citation that yields no box is a normal, informative result — Rabin 1981 contains no `F_OT`, because it predates ideal functionalities, and the page should say so rather than force one.

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
