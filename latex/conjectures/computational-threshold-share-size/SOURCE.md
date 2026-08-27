# Provenance: Beating log n for Computational 2-out-of-n Secret Sharing

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Cryptography from Planted Graphs: Security with Logarithmic-Size Messages**
- Authors: Damiano Abram, Amos Beimel, Yuval Ishai
- Venue/archive: IACR ePrint 2023
- Identifier: IACR ePrint 2023/1929
- Bibliographic detail: inferred
- File: `2023-1929.pdf` (64 pages)
- sha256: `ede54906e7a9c04e92565cf8a7eca6e5020a157c0d3dfe90fdbe995096386dba`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. The information-theoretic share size is exactly log n and Shamir's scheme matches it. The source proves a (1/5) log log n lower bound in the computational setting with public information, leaving a log n versus log log n gap, and proves that closing it upward is equivalent to a planted-subgraph problem.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 8 | 8 | exact (100%) | What is the minimal share size of computa- tionally secure 2-out-of-n secret sharing with public information? Is it possible to beat the information-theoretic l... |
| openness | 8 | 8 | exact (100%) | We were only able to prove an Ω(log log n) lower bound, and showed the equivalence of improving the upper bound to planting both a large clique and a large inde... |
| progress | 16 | 16 | exact (100%) | In particular, we do not know whether there are schemes with δ · log n share size for any δ < 1. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is verbatim in the source's open-questions list and its equivalence is the source's Theorem 2.6. One symbol collision inherited from the source was renamed and the rename recorded.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 8 | The question is the second item of Section 1.1.5's open-questions list, with the log n target and the log log n lower bound in the same sentence. |
| openness | pass | 16 | Stays open: Section 2.4 says the source could not find an answer and offers necessary and sufficient conditions instead. |
| strength | pass | 8 | Strength matches: the source asks whether log n can be beaten 'even by a constant factor', which is what the statement asks. |
| quantifiers-and-parameters | pass | 17 | Theorem 2.6's quantifiers reproduced: a constant beta strictly between 1/2 and 1, a distribution over triples, hardness of distinguishing a random clique node from a random independent-set node. |
| attribution | pass | 8 | The question and the equivalence are the harvested paper's own; the log n information-theoretic bound is attributed to KN90 and CCX13, the attacks to Kucera and AKS98, and the 4-nodes-per-part example to BF07, as the paper does. |
| definitions | fail | 17 | The source writes I for the public information and also for the independent set in Theorem 2.6. Renamed the independent set to J throughout, with a sentence saying so, since carrying both into one statement would be a genuine ambiguity rather than a stylistic one. |
| fabrication | pass | - | No fabrication. The remark that the decision problem is solvable by an unbounded distinguisher, and the absence of a natural search version, are the source's own Remark 2.7. |
| self-containment | pass | - | Self-contained from the scheme definition plus Theorem 2.6. |

### Corrections the checker asked for

- **definitions_latex** — Symbol collision on I between public information and independent set, inherited from the source.
  - suggested: Rename the independent set to J in the equivalence and state that the source uses I for both.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the source uses I for both public information and the independent set; the independent set is renamed J here. That the target is beating log n by a constant factor, not asymptotically. And that a negative answer is a statement about graphs too, by the equivalence.

