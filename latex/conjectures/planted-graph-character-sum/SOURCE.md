# Provenance: A Character-Sum Conjecture for Planted Subgraphs

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

`paper-conjectures`. The source derives the formula governing low-degree detection of a planted subgraph, observes the character sum in it should be small for most graphs, and says it leaves the rigorous study of the question to future work. No bound is proved and none is stated as a target.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 28 | 28 | exact (100%) | We conjecture that, for most graphs H, the sum |
| openness | 28 | 28 | exact (100%) | We leave the rigorous study of this problem to future work. |
| definition | 28 | 28 | exact (100%) | We use π ◦ H to denote the graph obtained by permuting the nodes (n.b. not the edges) of H according to π |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is verbatim on page 28 and explicitly left to future work. Its one real defect is that 'small' is unquantified, so a target had to be supplied; that choice is recorded as a correction and given its own remark.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 28 | The conjecture and the sentence leaving it to future work are both on page 28, in the discussion following Theorem 4.7. |
| openness | pass | 28 | Stays open: the source says explicitly that it leaves the rigorous study to future work and offers only a heuristic. |
| strength | fail | 28 | The source says the sum 'should be small' without quantifying. The drafted bound -- a o(1) fraction of \|Sym(n)\| -- is supplied by the statement. Recorded as a correction and flagged in its own remark, with stronger and more useful targets named as not claimed by the source. |
| quantifiers-and-parameters | pass | 28 | Quantifier order checked: for most H, the bound holds for all alpha -- not the other way round, which would be much weaker. |
| attribution | pass | 28 | The conjecture is the harvested paper's own; the clique-size fact bounding the useful degree range is attributed to BE76 as the paper does. |
| definitions | pass | 28 | The encodings are the source's: a graph and an edge set are both bit vectors indexed by potential edges, pi acts on nodes and not edges, and V(alpha) counts touched nodes. |
| fabrication | pass | - | No fabrication. The detection formula is transcribed from the source, and the claim that structured graphs maximize the sum is the source's own parenthetical. |
| self-containment | pass | - | Self-contained once the encodings are given, which the notation section does. |

### Corrections the checker asked for

- **formal_statement_latex** — No quantitative target is given by the source.
  - suggested: State the bound as a o(1) fraction of |Sym(n)| for a 1 - o(1) fraction of graphs, and add a remark saying the target is this statement's and naming the stronger forms that would be more useful.
- **notation_latex** — Writing the maximum as n! collides with lacheck and reads as punctuation.
  - suggested: Write the maximum as |Sym(n)|, which is what it denotes.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The target bound is supplied by this statement and not by the source, which says only 'small'. And the 'for most H' clause cannot be dropped: cliques and independent sets attain the maximum, which is the phenomenon rather than a defect.

