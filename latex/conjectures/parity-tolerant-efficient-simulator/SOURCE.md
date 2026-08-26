# Provenance: An Efficiently Simulatable Parity-Tolerant Circuit

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Leakage-Tolerant Circuits**
- Authors: Yuval Ishai, Yifan Song
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/332
- Bibliographic detail: inferred
- File: `2024-332.pdf` (55 pages)
- sha256: `b3b1ed860ad1d1c647c80274b1cab50972a3f14480b30485be98f895c7fa19dd`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. Feasibility is settled: the source compiles every circuit into a t-parity-tolerant one of size O~(s) + poly(n,m,h,t,kappa). What is open is the simulator's running time, which is exponential in t; the source gives partial evidence under LPN that inefficient simulation may be inherent for a related relaxed notion.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 3 | 3 | exact (100%) | Is there a t-parity-tolerant circuit with a poly(t)-time simulator? |
| openness | 3 | 3 | exact (100%) | Our simulator needs to find a short vector in a linear code defined by the parity queries, and we are only able to show that this is inherent for a related enco... |
| openness | 3 | 3 | exact (100%) | Several natural questions are left open for future work. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is verbatim in 'Future directions' and stays open through Appendix H. The parameters of the achieved construction were wrong in the draft and were corrected against Corollary 2.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 3 | The question is the second item of the 'Future directions' list, with the short-vector obstruction named in the same sentence. |
| openness | pass | 13 | Stays open: page 13's 'On the Need for Inefficient Simulation' explains the 2^{O(t)} cost and Appendix H gives only conditional evidence, never a resolution. |
| strength | pass | 3 | Strength matches: the source asks for a poly(t)-time simulator for a t-parity-tolerant circuit, which is what the draft states. |
| quantifiers-and-parameters | fail | 13 | An earlier draft asserted error 2^{-Omega(t)} and size \|C_f\| poly(t). Corollary 2 gives size O~(s) + poly(n,m,h,t,kappa) with error negligible in a statistical parameter kappa, and the intermediate compiler needs k = O(t(t+kappa)). Corrected. |
| attribution | pass | 3 | The question is the harvested paper's own; the probing-tolerance notions it generalizes are attributed to ISW03, AIS18 and GIS22 as the paper does. |
| definitions | pass | 14 | Definition 2 is reproduced with both simulator stages and the ideal leakage on (x,y), which is what makes tolerance different from resilience. |
| fabrication | pass | 13 | No fabrication. The draft states that the source's stateful application already achieves poly(t)-time simulation, which the source says explicitly, rather than presenting it as open. |
| self-containment | pass | - | Self-contained from Definitions 1 and 2 and the parity leakage class. |

### Corrections the checker asked for

- **formal_statement_latex** — Error and size parameters did not match Corollary 2.
  - suggested: State error negligible in a statistical security parameter kappa and size polynomial in |C_f|, t and kappa, and require the simulator to run in poly(|C_f|, t, kappa).
- **setting_latex** — The mechanism behind the exponential simulator was asserted rather than described.
  - suggested: Record that the simulator computes the union of V(XOR_{i in S} W_i) over all 2^t subsets S, that the resulting set is small (|V| <= kt), and that it is finding it that costs 2^{O(t)}.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the leakage class is t parities of arbitrarily many wires and not t probes (for probing, efficient simulation is classical), that this is tolerance and not resilience, and that the source's own stateful application already has poly(t)-time simulation -- three ways the statement could be accidentally weakened into something known.

