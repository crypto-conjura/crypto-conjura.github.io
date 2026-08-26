# Provenance: A Standard-Model Weak PCF from Sparse LPN

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

`paper-asks-question`. Open. The source poses it as the second of its two open questions; the affirmative direction stated here is the page's own reading. Unlike its companion, this question comes with an obstruction the source names explicitly, and an independent follow-up reports the same oracle as inherent to the same recursion.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 10 | 10 | exact (100%) | Is it possible to get rid of the random oracle model by settling for a weak PCF (that is only required to be secure on random inputs)? |
| openness | 11 | 11 | exact (100%) | it is unclear how to replace the RO with standard model primitives. The reduction from sparse-LPN requires programming the RO, and it is unclear how the reducti... |
| openness | 10 | 10 | exact (100%) | Open Questions. We mention two interesting open questions: |
| progress | 10 | 10 | exact (100%) | Intriguingly, all previous PCF candidates were secure in the standard model when targeting only weak security, as the random oracle was used only as a generic s... |
| progress | 11 | 11 | exact (100%) | a new “sparse-LPN with pseudorandom matrix” assumption, a plausible but non-standard variant of LPN |
| definition | 10 | 10 | exact (100%) | the random oracle is used adaptively to sample rows of a product of matrices |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is printed verbatim on p. 10 as item (2) of the source's 'Open Questions', the obstruction is spelled out across pp. 10-11, and nothing later in the paper addresses either. One correction was forced: the superpolynomial-output clause is load-bearing and was not flagged as the page's own reading in the first draft, which would have presented a choice of the page's as the source's.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 10 | Item (2) under 'Open Questions', printed verbatim. |
| openness | pass | 11 | The paper says twice on p. 11 that it is unclear how to proceed, and offers no construction; the paper ends at Section 4.5 with no result touching the model. Corroborated externally: ePrint 2025/2002 (December 2025) states 'we do not obtain a weak PCF in the standard model' for the same recursion. |
| strength | fail | 10 | The draft's superpolynomial-output requirement is not in the source's sentence. It is necessary -- a weak PCF for polynomially many outputs is a PCG, which sparse LPN already gives -- but it is a reading, and is now labelled as one in the setting and in the remark. |
| quantifiers-and-parameters | pass | 10 | The source's parenthetical fixes what 'weak' means ('only required to be secure on random inputs'), and the statement uses exactly that. No parameter regime is claimed that the source does not state. |
| attribution | pass | 10 | The source's own question about its own construction. The hash-then-evaluate paradigm it contrasts with is attributed to Brzuska et al., as on the page. |
| definitions | unclear | 13 | The source prints Definition 9 for strong PCFs and defines 'weak' only by the parenthetical; the weak-PCF definition on the page is Definition 9 with random inputs, which is Boyle et al.'s notion but is not printed in the source. Flagged in risks. |
| fabrication | pass | - | Every claim in the setting is quoted or paraphrased from pp. 8-11. The claim that the oracle samples rows of a product of matrices via a k-ary hash tree is the source's own account on pp. 9-10. |
| self-containment | pass | - | Readable from the page's Definitions 1 and 2 and the notation list. |

### Corrections the checker asked for

- **formal_statement_latex** — The superpolynomial-output clause was presented without saying it is the page's reading rather than the source's wording.
  - suggested: Label it as the page's reading, and say why it is needed: a weak PCF with polynomially many outputs is a PCG.
- **status_note** — Did not record the independent corroboration that the oracle is inherent to this recursion.
  - suggested: Cite ePrint 2025/2002's own statement, marked [UNVERIFIED] as it is not in the source's bibliography.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `HR25` — Sebastian Hasler, Pascal Reisert, *Pseudorandom Correlation Functions for Multiparty Beaver Triples from Sparse LPN*, IACR ePrint 2025/2002 2025

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

Two readings are the page's own and neither is in the source: that the conjecture demands superpolynomially many outputs (without which a PCG answers it trivially), and that 'from sparse LPN' excludes the 'sparse-LPN with pseudorandom matrix' variant the source describes. Check also that the weak-PCF definition given matches Boyle et al.'s, which the source cites but does not print.

