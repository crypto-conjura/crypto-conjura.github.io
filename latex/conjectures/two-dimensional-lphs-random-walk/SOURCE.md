# Provenance: An Optimal Two-Dimensional Locality-Preserving Hash for Shifts

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Locality-Preserving Hashing for Shifts with Connections to Cryptography**
- Authors: Elette Boyle, Itai Dinur, Niv Gilboa, Yuval Ishai, Nathan Keller, Ohad Klein
- Venue/archive: IACR ePrint; ITCS 2022
- Identifier: ePrint 2022/028 (ITCS 2022, LIPIcs 215, art. 27)
- Bibliographic detail: printed-on-page
- File: `2022-028.pdf` (62 pages)
- sha256: `351eeab8ac344e2279f269bdf6dbcd838dbf352429193728e90905ee0e36c89b`
- Read on 2026-08-23T14:33:35Z via the `none (in-session; no CLI binary, no SDK, no credentials)` backend

## How the paper leaves it open

`paper-conjectures`. Open, and asserted rather than asked: the source prints the algorithm, conjectures the error rate, reports experiments consistent with it, states that it could not analyse it, and leaves settling it to future work. A proof would close the two-dimensional case, since the matching lower bound is the source's own Theorem 1.4.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 24 | 24 | exact (100%) | We conjecture that the following symmetric algorithm (Random-Walk-Hash) has the optimal performance of |
| openness | 24 | 24 | exact (100%) | However, we were not able to rigorously analyze it. |
| openness | 7 | 7 | exact (100%) | However, the analysis (and especially deterministic resolution of cycles in the random walk) is quite involved, and settling our conjecture is left open for fut... |
| progress | 7 | 7 | exact (100%) | we present another 2-dimensional LPHS algorithm, which seems harder to analyze, but for which we conjecture that the error rate is at most |
| progress | 7 | 7 | exact (100%) | Our experiments suggest that the error rate of this algorithm is indeed |
| progress | 24 | 24 | exact (100%) | In practice we cannot guarantee independence, since the random walk occasionally runs into loops. |
| definition | 24 | 24 | exact (100%) | The main heuristic assumption we make is that each rw-stage(x, d, L, i, j) can be modeled by a random walk on Z2 , starting at (i, j) and having independent ste... |
| parameter | 7 | 7 | exact (100%) | This bound is essentially the best one can hope for given the lower bound discussed below. |
| parameter | 7 | 7 | exact (100%) | For n = Ω(d2/k ), any k-dimensional (d, δ)-LPHS satisfies |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

The conjecture is printed under the heading 'Conjectured optimal algorithm' in Section 4.1.4, restated in the introduction, and explicitly left open; nothing later in the paper analyses the algorithm. Two corrections were forced: the last step size was first transcribed as sqrt(d')/2 from the text layer, which is wrong, and the hypotheses on n and b were first invented rather than left open as the source leaves them.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 24 | Section 4.1.4, PDF p. 24: 'We conjecture that the following symmetric algorithm (Random-Walk-Hash) has the optimal performance of delta = O~(1/d).' Restated on PDF p. 7. |
| openness | pass | 24 | 'However, we were not able to rigorously analyze it', and on PDF p. 7 'settling our conjecture is left open for future work'. Section 4.2 proves the lower bound, not this upper bound; no later section returns to the algorithm. |
| strength | pass | 24 | Stated about the printed algorithm, as the source states it, rather than as the weaker existence claim. The weaker reading is named on the page and explicitly not adopted. |
| quantifiers-and-parameters | unclear | 24 | The source's conjecture names no hypothesis on n or b, while neighbouring lemmas assume n = Omega(d) and 2^b >= d^4 or b >= 3 log n. The statement says 'for all large enough n and b' and flags this; a reviewer should pin it down. |
| attribution | pass | 24 | The source's own conjecture about its own algorithm. The one-dimensional optimum it builds on is attributed to Dinur-Keller-Klein, as the source attributes it. |
| definitions | fail | 25 | The final step size is sqrt(d'/2), with the radical over d'/2, confirmed by rendering PDF p. 25 at 150 dpi; the text layer flattens it and reads as sqrt(d')/2. The first draft had the wrong one. Also corrected: the per-stage failure exponent, which is d'^{-2^{-l}} counting Min-Hash as the first stage, not d'^{-2^{-(l+1)}}. |
| fabrication | pass | 24 | The two random-walk claims and the loop-breaking obstruction are the source's own, quoted or closely paraphrased. The step-size pattern d'^{1/2-2^{-(l+1)}} is this page's arithmetic on the printed exponents 1/4, 3/8, 7/16 and is labelled as a description of them. |
| self-containment | pass | - | All three procedures and the LPHS definition are printed on the page; a reader needs nothing from the source to attempt it. |

### Corrections the checker asked for

- **definitions_latex** — Last step size transcribed from the text layer as sqrt(d')/2.
  - suggested: sqrt(d'/2), read off the rendered page.
- **definitions_latex** — Per-stage failure probability exponent was off by one in the setting prose.
  - suggested: d'^{-2^{-l}} with Min-Hash counted as the first stage, consistent with the source's O(d'^{-1/4}), O(d'^{-1/8}) for the first two rw-stages.
- **formal_statement_latex** — First draft invented hypotheses n = Omega(d) and 2^b >= d^4.
  - suggested: Leave them as 'large enough' and record in a remark that the source's own statement names none.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The conjecture is about a specific printed algorithm, not about the existence of some O~(1/d) scheme, and the page states the former; check that the transcription of Algorithms 1, 7 and 8 is exact, in particular the last step size, which is sqrt(d'/2) and not sqrt(d')/2 -- the PDF text layer flattens the radical. The hypotheses on n and b are left as 'large enough' because the source's statement of the conjecture names none.

