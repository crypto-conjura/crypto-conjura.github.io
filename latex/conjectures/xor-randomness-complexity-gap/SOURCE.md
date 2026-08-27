# Provenance: The Exact Randomness Complexity of t-Secure XOR

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Tight Bounds on the Randomness Complexity of Secure Multiparty Computation**
- Authors: Vipul Goyal, Yuval Ishai, Yifan Song
- Venue/archive: IACR ePrint 2022
- Identifier: IACR ePrint 2022/799
- Bibliographic detail: inferred
- File: `2022-799.pdf` (42 pages)
- sha256: `40d7c0f64a649dd661ffc71045b519e09cbbdd569cd1c6d9f28f6c709cbc9fd2`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The source proves an Omega(t^2) lower bound, matching Kushilevitz and Mansour's non-explicit O(t^2 log(n/t)) upper bound up to a logarithmic factor -- and up to a constant factor when t = Omega(n) -- and gives an explicit protocol at O(t^2 log^2 n). It states it leaves the remaining polylogarithmic gaps open.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 3 | 3 | exact (100%) | We leave open the question of characterizing the randomness complexity of general MPC without helper parties, as well as closing the remaining (polylogarithmic)... |
| openness | 3 | 3 | exact (100%) | Evidence for the difficulty of these questions in some parameter regimes was given by Kushile- vitz et al. [KOR96], who showed a two-way relation between the ra... |
| progress | 2 | 2 | exact (100%) | we obtain an explicit protocol for XOR that uses O(t2 ·log2 n) random bits. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open question is verbatim on page 3 and the three bounds bracketing it are the source's own summary. One bibliography entry was misattributed and was corrected against the paper's reference list; perfect privacy and explicitness are recorded as the two things a reader must not silently relax.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 3 | The sentence leaving the remaining polylogarithmic gaps open is on page 3, immediately after the upper-bound summary. |
| openness | pass | 3 | Stays open: the source states it settles the main questions but explicitly not the polylogarithmic gaps. |
| strength | pass | 2 | Strength matches: the statement asks for the order of the randomness complexity in the regime that is actually open, t = o(n), rather than claiming a direction. |
| quantifiers-and-parameters | pass | 2 | The three bounds are transcribed with their attributions and explicitness status: Omega(t^2) the source's, O(t^2 log(n/t)) non-explicit from KM97, O(t^2 log^2 n) explicit from the source. |
| attribution | pass | 2 | The lower bound is the harvested paper's; the upper bounds and the difficulty evidence are attributed to KM97, Benaloh, Chor-Kushilevitz and KOR96 as the paper does. |
| definitions | pass | 2 | 'Randomness complexity' is the source's worst-case count of tossed coins, and privacy is perfect, which the source's own statistical-privacy counterexample shows is essential. |
| fabrication | fail | 2 | An earlier draft attributed [Ben86] to Michael Ben-Or, 'Another advantage of free choice'. The source's reference list gives Josh Cohen Benaloh, 'Secret sharing homomorphisms: keeping shares of a secret sharing', CRYPTO '86. Corrected, along with the venue details of KM97, BDPV99, CK93, KOR96 and GIS22a. |
| self-containment | pass | - | Self-contained from the model description and the three bounds. |

### Unsupported by the paper

- An earlier draft misattributed [Ben86] to Ben-Or; corrected against the source's own reference list.

### Corrections the checker asked for

- **bibliography** — [Ben86] misattributed.
  - suggested: Josh Cohen Benaloh, 'Secret sharing homomorphisms: keeping shares of a secret sharing', CRYPTO '86, pages 251-260.
- **setting_latex** — The prose named Ben-Or as a source of the textbook protocol.
  - suggested: Name Benaloh, and Chor and Kushilevitz.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That perfect privacy is load-bearing: with statistical privacy a folklore committee protocol beats Omega(n^2), which the source uses to explain why its technique is combinatorial. That explicitness is a second, separate axis. And that the settled regime t = Omega(n) is excluded.

