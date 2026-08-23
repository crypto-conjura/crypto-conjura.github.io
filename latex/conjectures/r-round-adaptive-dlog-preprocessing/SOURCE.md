# Provenance: Discrete Logarithm with Preprocessing and r Rounds of Adaptivity

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

`paper-conjectures`. Open for every 1 < r < T. The r = 1 case is the source's Theorem 1.1 and the r = T case is the bound of Corrigan-Gibbs and Kogan; nothing in between is proved. The source states the interpolation as a conjecture and says it would be sharp.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 11 | 11 | exact (100%) | For the DLOG problem, we conjecture that the success probability of an (S, T )-algorithm with r rounds of adaptivity is at most |
| openness | 11 | 11 | exact (100%) | More generally, a natural goal to pursue, in view of our results, is to obtain time-space lower bounds for adaptive attacks with preprocessing, as a function of... |
| openness | 11 | 11 | exact (100%) | The independence of the queries from the challenge appears inherent to our proof strategy. |
| progress | 11 | 11 | exact (100%) | This matches our result for non-adaptive algorithms (i.e., 1 round of adaptivity), as well as the bounds of [CK18] for adaptive algorithms (i.e., T rounds of ad... |
| progress | 11 | 11 | exact (100%) | it would be sharp, as for any 1 ≤ r ≤ T , it is matched by a variant of the adaptive algorithm of [BL13, CK18, Mih10], in which instead of constructing one chai... |
| progress | 11 | 11 | exact (100%) | extending our approach beyond this restriction would require new Shearer-type inequalities or alternative techniques that can handle such challenge-dependent qu... |
| definition | 17 | 17 | exact (100%) | We say that A1 is non-adaptive if given any z, its queries are fixed and do not (further) depend on |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

The conjecture is printed verbatim in the source's open-problems paragraph on printed p. 10 (PDF p. 11), with both endpoints identified by the source itself and a matching attack sketched. It is not proved anywhere in the paper: the numbered results are Theorems 1.1-1.3 and 4.1, none about intermediate r. The correction that mattered: the source never defines 'r rounds of adaptivity', so the page had to supply a definition, and the first draft presented it as if it were the source's.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 11 | Printed verbatim: 'For the DLOG problem, we conjecture that the success probability of an (S, T )-algorithm with r rounds of adaptivity is at most O~(T^2/N + rST/N)'. |
| openness | pass | 11 | Stated in a paragraph headed 'Open problems'. The paper proves only r = 1 (Theorem 1.1, printed p. 4) and cites [CK18] for r = T. No result addresses intermediate r; checked against the full list of numbered statements. |
| strength | fail | 11 | The source's phrase 'r rounds of adaptivity' is undefined in the paper -- it appears exactly once. The statement therefore depends on a definition the page supplies, which is a change in kind, not degree. Corrected by labelling Definition 3 as the page's own and by pinning it to the two endpoints the source names. |
| quantifiers-and-parameters | pass | 11 | The polylogarithmic factor is the source's O~; r ranges over 1..T as the source's 'for any 1 <= r <= T' has it; N prime as in Theorem 1.1. |
| attribution | pass | 11 | The conjecture is the source's own. The r = T endpoint is attributed to [CK18] and the matching attack to [BL13, CK18, Mih10], as the source attributes them. |
| definitions | unclear | 17 | Non-adaptivity is quoted from the source's Section 3.2 (PDF p. 17). The r-round notion is not in the source. Flagged in risks and on the page. |
| fabrication | pass | - | The obstruction paragraph is the source's own account, quoted. The claim that each extra round buys a factor only in the ST/N term is a reading of the printed formula, labelled as such. |
| self-containment | pass | - | The generic group model, the (S,T) model and the r-round notion are all on the page; the statement needs nothing else. |

### Corrections the checker asked for

- **definitions_latex** — The r-round notion was presented without saying the source never defines it.
  - suggested: Label Definition 3 as this page's, and add the remark showing it reproduces the source's two named endpoints.
- **formal_statement_latex** — The polylogarithmic factor was written as O~ inside the statement.
  - suggested: Existentially quantify an explicit polylogarithmic function c(N), so the statement is a proposition rather than an asymptotic idiom.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The definition of 'r rounds of adaptivity' is this page's, not the source's -- the phrase occurs once in the paper and is never defined. Check the batching notion in Definition 3 against the two endpoints the source names; any definition that gets r = 1 and r = T right is close to it, but the intermediate content depends on details such as whether batch sizes may adapt.

