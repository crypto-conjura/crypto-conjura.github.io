# Provenance: The Binary Dual-Distance Bound Is the Worst Case

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Fast Pseudorandom Correlation Functions from Sparse LPN**
- Authors: Lennart Braun, Geoffroy Couteau, Kelsey Melissaris, Mahshid Riahinia, Elahe Sadeghi
- Venue/archive: IACR ePrint; ASIACRYPT 2025
- Identifier: ePrint 2025/1644
- Bibliographic detail: printed-on-page
- File: `2025-1644.pdf` (38 pages)
- sha256: `a6d41228a29cec5c92a2784ef8c0d3e13a0be1977ea08dfbbee4ea97fe272042`
- Read on 2026-08-23T11:45:14Z via the `none (in-session; no CLI binary, no SDK, no credentials)` backend

## How the paper leaves it open

`paper-conjectures`. Open, and asserted rather than asked: the source writes that it expects the binary bound to lower-bound the bound over larger fields, gives an intuition, records that all previous work assumes as much, and proves nothing. No counterexample is known and no proof is known.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 26 | 26 | exact (100%) | However, we expect the bound obtained through our analysis over F2 to provide a lower bound on that over larger fields. |
| openness | 26 | 26 | exact (100%) | All previous works assume that the bound does not degrade as the field size grows and a common heuristic is, therefore, to use the bounds from the analysis over... |
| openness | 32 | 32 | exact (100%) | Note that the complexity of the computation is at least cubic in the LPN dimension n and quickly becomes infeasible for the large dimensions that we are interes... |
| progress | 26 | 26 | exact (100%) | Intuitively, as the field grows, canceling rows gets harder; it no longer suffices for balls to land in the same bins but they must have opposite values. |
| definition | 26 | 26 | near (100%) | Our analysis above exploits properties of F2 (e.g., cancellations are more likely compared to a general field and only even-weight vectors matter). This allows ... |
| definition | 30 | 30 | exact (100%) | In Section 4.3 we gave explicit formulae to compute the dual distance of regular random codes |
| parameter | 28 | 28 | exact (100%) | D = 0 indicates that we can only guarantee a trivial bound |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

The claim is printed as a belief the source holds and does not prove ('we expect ... to provide a lower bound'), it is load-bearing for the source's own large-field parameter selection, and nothing later in the paper proves it -- Section 4.5 supplies formulae and then says evaluating them is infeasible at the dimensions of interest. The correction that mattered: the two bounds the source's sentence compares are computed for different code ensembles, which the first draft did not say.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 26 | Printed on p. 26 in the paragraph 'Analysis Over a General Field', confirmed by rendering the page at 150 dpi. |
| openness | pass | 32 | Not proved anywhere: the numbered results are Theorem 1, Lemmas 2-6 and Claims 1-2, none about field size, and Section 4.5's closing paragraph says the general-field computation is at least cubic in n and infeasible at the dimensions of interest. The source's phrasing is 'we expect', and it records that previous work merely assumes it. |
| strength | fail | 26 | The source's sentence compares its F_2 analysis (Section 4.3, RegularCodeGen) with the general-field analysis (Section 4.5, SparseCodeGen), so the two sides are different ensembles as well as different fields. The first draft stated the inequality without recording this. Corrected by naming both ensembles in the definitions and adding the remark; the same-ensemble variant is explicitly not what is stated. |
| quantifiers-and-parameters | pass | 28 | Universally quantified over p, rho, k, n, m, as the source's unrestricted sentence implies; the D = 0 convention for a trivial bound is the source's own, from the Table 2 caption on p. 28. |
| attribution | pass | 26 | The expectation is the source's own ('we expect'). The practice of using the binary bound over larger fields is attributed to previous work, as the source attributes it, to ADINZ17 and BCGI18. |
| definitions | pass | 30 | Both formulae were transcribed from rendered images of pp. 26 and 30 rather than from the text layer, which drops the fraction in N := n/k and prints it as 'nk'. SparseCodeGen and RegularCodeGen are the source's Definitions 3 and 4, p. 11. |
| fabrication | pass | - | The remark about the (p-1)^w factor is labelled as an observation about the source's own printed summand, not as a claim of the source's. No claim is attributed to the source that it does not make. |
| self-containment | pass | - | The two probabilities q_w and pi^(p)_w are defined probabilistically on the page, so both bounds are fully determined without the source's recursions. |

### Corrections the checker asked for

- **definitions_latex** — The two bounds were stated without recording that D_2 is computed for the regular ensemble and D_p for the sparse ensemble.
  - suggested: Name the ensemble in each definition and add the remark on the mismatch and on the even-weight-only structure of the F_2 sum.
- **formal_statement_latex** — No convention for the case where the constraint fails at w = 1, where the max is over an empty set.
  - suggested: Set the value to 0 in that case, following the source's own Table 2 caption.
- **notation_latex** — N := n/k was first read off the text layer, which renders it 'nk'.
  - suggested: Transcribe from the rendered page: N := n/k, the length of one block of a regular row.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `Kha26` — Majid Khabbazian, *Linear Distance for Fixed-Row-Weight Expand-Accumulate Codes over Arbitrary Fields*, IACR ePrint 2026/1753 2026

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The two bounds are computed for different code ensembles -- the F_2 side for the regular ensemble, the general-field side for the sparse ensemble -- which is a feature of the source's sentence and not of this transcription, and is the first thing to check. A structural consequence is that the F_2 sum runs over even weights only while the general-field sum runs over all weights. The source's extension remark (replace p_{w,0}^k by p_{w.k,0}) gives a same-ensemble variant of the claim that is arguably the more natural one, and is deliberately not what is stated.

