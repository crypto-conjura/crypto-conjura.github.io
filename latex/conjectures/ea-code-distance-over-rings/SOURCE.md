# Provenance: Minimum Distance of Expand-Accumulate Codes over Arbitrary Rings

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Correlated Pseudorandomness from Expand-Accumulate Codes**
- Authors: Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Nicolas Resch, Peter Scholl
- Venue/archive: IACR ePrint 2022
- Identifier: IACR ePrint 2022/1014
- Bibliographic detail: inferred
- File: `2022-1014.pdf` (59 pages)
- sha256: `fb060f99b5e08d1f25f9575d28f6a53a76e1b065cada860e58f9c711b2c0b325`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Theorem 3.10 proves the distance bound over the binary field only. Over a ring of size q the source's proof technique forces the rate to satisfy R much less than 1/ln q, which it states it believes is an artefact, supported by small-parameter weight-distribution experiments over F_17 and Z_16.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 21 | 21 | exact (100%) | We conjecture that the minimum distance should at the very least not degrade over larger rings; in fact, we believe that it should increase commensurately. |
| openness | 21 | 21 | exact (100%) | Theorem 3.10 applies only to the case of the binary field, and one can naturally wonder about the distance over arbitrary rings. |
| progress | 21 | 21 | exact (100%) | However, we believe that this is an artifact of the proof. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is verbatim on page 21 with a named obstruction and experimental support. Only one repair was needed: the source states two claims and just one of them is quantified enough to be the statement.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 21 | The 'Arbitrary rings' paragraph on page 21 states the conjecture and the rate restriction the proof forces. |
| openness | pass | 21 | Stays open: the source gives experiments rather than a proof, and says it believes the restriction is an artefact. |
| strength | fail | 21 | The source makes two claims -- that the distance does not degrade, and that it should increase commensurately -- and only the first is quantified enough to state. Repaired by conjecturing the non-degradation form and recording the stronger claim as the source's belief in its own remark. |
| quantifiers-and-parameters | pass | 18 | Theorem 3.10's quantifiers reproduced: R constant, p = C ln N / N in (0,1/2), delta in (0,1/2), beta = 1/2 - delta, N sufficiently large, and the two side conditions including C > 1/beta^2. |
| attribution | pass | 21 | The conjecture is the harvested paper's own; the pseudorandom-correlation-generator line the distance feeds is attributed to BCG+19b. |
| definitions | pass | 13 | The accumulator matrix and EA sampling are Definitions 3.1 and 3.2 verbatim, including that H = BA is treated as a generator matrix despite the H notation, which the source explains in its Remark 3.3. |
| fabrication | pass | - | No fabrication. The F_17 and Z_16 experiments are the source's, and the choice of one field and one ring with zero divisors is read off its own parameters rather than inferred. |
| self-containment | pass | - | Self-contained from Definitions 3.1, 3.2 and Theorem 3.10. |

### Corrections the checker asked for

- **formal_statement_latex** — The source's stronger claim -- distance increases commensurately with ring size -- is unquantified.
  - suggested: Conjecture the non-degradation form and record the stronger claim as belief in a remark, asking any resolution to report the improvement it obtains.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the conjecture is the weaker of the source's two claims -- non-degradation -- with the stronger claim of commensurate improvement recorded as belief rather than promoted. And that the named obstruction is a concentration inequality (the expander Hoeffding bound), so the substance is a bound that does not pay ln q.

