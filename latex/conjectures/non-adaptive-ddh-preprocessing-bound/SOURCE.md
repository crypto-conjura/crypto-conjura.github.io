# Provenance: The Optimal Bound for Non-Adaptive DDH with Preprocessing

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Non-Adaptive Cryptanalytic Time-Space Lower Bounds via a Shearer-like Inequality for Permutations**
- Authors: Itai Dinur, Nathan Keller, Avichai Marmor
- Venue/archive: IACR ePrint; STOC 2025
- Identifier: ePrint 2025/783 (STOC 2026; arXiv:2505.00894)
- Bibliographic detail: printed-on-page
- File: `2025-783.pdf` (45 pages)
- sha256: `a42b579c7e49b6d2aef367b57f03bc471652ac3b5579cfe3d5e8268ee7279da8`
- Read on 2026-08-23T14:33:35Z via the `none (in-session; no CLI binary, no SDK, no credentials)` backend

## How the paper leaves it open

`paper-conjectures`. Open. The proved bound is the source's Theorem 1.2; the conjectured improvement is stated twice, in the results section and again in the open-problems paragraph. The same theorem's bound for square-DDH is sharp, with an attack the source sketches in its Appendix B.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 6 | 6 | exact (100%) | For the DDH problem, we conjecture that the bound on the success probability is not |
| statement | 11 | 11 | near (100%) | As written, we conjecture that the bound of Theorem 1.2 is not tight, and the optimal bound is |
| openness | 11 | 11 | exact (100%) | Another open problem, mentioned above, is to close the gap between upper and lower bounds for non-adaptive (S, T )-algorithms for the DDH problem. |
| progress | 6 | 6 | exact (100%) | For the sqDDH problem, the theorem is sharp, as a simple non-adaptive variant of the adaptive algorithm of [CK18] sketched in Appendix B attains its success pro... |
| progress | 6 | 6 | exact (100%) | Possibly, the techniques used in the recent |
| definition | 18 | 18 | exact (100%) | Note that if k = 0, the algorithm effectively receives |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is stated twice in the source, in its own words, with the value named; it is not proved anywhere, and its Section 5.2 proves only the weaker Theorem 1.2. The correction that mattered: the source's phrase 'the optimal bound is' asserts a matching lower bound too, and the first draft folded both halves into one statement without recording the choice.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 6 | Printed on printed p. 5 (PDF p. 6) immediately after Theorem 1.2, and again in the open-problems paragraph on printed p. 10 (PDF p. 11). |
| openness | pass | 11 | Listed as an open problem; Section 5.2 proves only Theorem 1.2, whose DDH case the source calls not tight. No later result improves it. |
| strength | fail | 11 | 'the optimal bound is X' claims both an upper bound and a matching attack. The page states the upper-bound half only, which is weaker than the source's sentence; recorded explicitly in the setting and in a remark rather than silently. |
| quantifiers-and-parameters | pass | 6 | N prime; success probability measured against 1/2 as in Theorem 1.2; the polylogarithmic factor is the source's O~. The DDH query structure is quoted from the game definition on PDF p. 18. |
| attribution | pass | 6 | The conjecture is the source's own; the adaptive tight bound is attributed to [ABG+24] and the earlier upper bound and the sqDDH attack to [CK18], as in the source. |
| definitions | pass | 18 | The DDH permutation-challenge game, including the translation function for k = 0 and k = 1, is reproduced from the source's Section 3.3. |
| fabrication | pass | - | The remark contrasting the degree structure of DDH and square-DDH queries is derived from the two translation functions printed in the source, and is labelled as this page's reading of why the proof cannot tell them apart. |
| self-containment | pass | - | The model, the game and both bounds are on the page. |

### Corrections the checker asked for

- **formal_statement_latex** — Stated the source's 'optimal bound' as if the matching-attack half were also being conjectured.
  - suggested: State the upper-bound half only, and record the two-sided reading in a remark with what a solver should check.
- **status_note** — Did not record that the same theorem is sharp for square-DDH.
  - suggested: Say so, since it is what makes the DDH case a question rather than a suspicion.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The source says 'the optimal bound is', which claims a matching algorithm as well; the page states only the upper-bound half and says so. Check whether the corresponding non-adaptive attack really achieves ST/N -- if it does not, the source's two-sided sentence is false even if this statement is true.

