# Provenance: Constant-Overhead Boolean AMD Circuits

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Oblivious Transfer with Constant Computational Overhead**
- Authors: Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, Lisa Kohl, Nicolas Resch, Peter Scholl
- Venue/archive: IACR ePrint 2023
- Identifier: IACR ePrint 2023/817
- Bibliographic detail: inferred
- File: `2023-817.pdf` (42 pages)
- sha256: `1c92672a45b0e5b009e381549fc5c74db5cd0a33b727123e1c277ac50d3fa796`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. Polylogarithmic overhead in |C| and lambda is achieved by Genkin, Ishai and Weiss; constant overhead is open. The source's Theorem 43 shows that achieving it would, together with the source's own constant-overhead OT protocol, settle the main open question on constant-overhead secure computation for general Boolean circuits.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 33 | 33 | exact (100%) | Combined with a constant-overhead OT protocol, this reduces an affirmative answer to the main open question to the design of constant-overhead AMD circuits. |
| openness | 32 | 32 | exact (100%) | Finally, while we leave open the existence of constant-overhead protocols for general Boolean circuits, our result for OT allows us to reduce this question to a... |
| progress | 33 | 33 | exact (100%) | The main result of [GIW16] is a construction of AMD circuits with polylogarithmic overhead (in \|C\|, λ). Whether this can be improved was left open |

## Adversarial check

**Verdict: faithful** (confidence: high)

The open question and the reduction are both in Section 6.3, and Definition 42 with Theorem 43 make the statement self-contained. The one thing needing care -- that the reduction runs one way, so an AMD lower bound would close a route rather than the problem -- is recorded in its own remark.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 32 | Section 6.3 states the reduction and says the source leaves open the existence of constant-overhead protocols for general Boolean circuits. |
| openness | pass | 33 | Stays open: Theorem 43 is conditional on exactly this hypothesis and the source names GIW16's polylogarithmic overhead as the state of the art. |
| strength | pass | 33 | Strength matches: the hypothesis of Theorem 43 is transcribed verbatim, including the 2^{-lambda} security and the O(\|C\|) + poly(lambda)\|C\|^{0.9} size. |
| quantifiers-and-parameters | pass | 33 | Definition 42's quantifiers reproduced: for any additive attack there exist distributions Delta_in and Delta_out such that for every x the statistical distance is at most eps -- the distributions may not depend on x. |
| attribution | pass | 33 | AMD circuits are attributed to GIP+14 as the source does; Theorem 43 is attributed to the source with its 'Cf. [GIW16], Claim 18' provenance. |
| definitions | pass | 33 | 'Additive attack' is used in the source's Boolean sense: toggling an arbitrary subset of wires. |
| fabrication | pass | - | No fabrication. The claim that the source supplies the other hypothesis is its own main result, and the contrast with the IPS08/DIK10 route is the source's own sentence. |
| self-containment | pass | - | Self-contained from Definition 42. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the size bound is the source's shape, O(|C|) + poly(lambda)|C|^{0.9}, and not plain O(|C|). That the reduction is one-directional: a lower bound on AMD circuits closes a route, not the main question. And that the source's own relaxed-security and restricted-class results do not settle it.

