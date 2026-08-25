# Provenance: A Designated-Verifier SNARG with One Group Element and tau + o(tau) Bits

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Designated-Verifier SNARGs with One Group Element**
- Authors: Gal Arnon, Jesko Dujmovic, Yuval Ishai
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/517
- Bibliographic detail: inferred
- File: `2025-517.pdf` (52 pages)
- sha256: `9fc5ce9614a7be927b214ece156462ad1b5b232ddb00ce0afeaf67f3e9ed90f8`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Numbered Conjecture 1.3 of the source. Its Theorem 1.1 achieves one group element plus O(tau) bits with a large constant (56 tau bits at quadratic CRS size); its Theorem 1.2 achieves one group element, one random-oracle output and about 2 tau bits. The conjecture halves the additive term and asks for no random oracle.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 6 | 6 | exact (100%) | The above two potential improvements could lead to the following dv-SNARG. |
| openness | 5 | 5 | exact (100%) | However, we believe that our analysis is quite loose, and conjecture that an even a slightly simpler construction can achieve a better level of soundness. |
| openness | 6 | 6 | exact (100%) | We leave open the question of designing practical LPCPs with |

## Adversarial check

**Verdict: faithful** (confidence: high)

The statement is a numbered conjecture of the source, transcribed bullet by bullet from the rendered page, and its supporting definitions are the source's own. The unusual log log lambda term was confirmed against the PDF rather than normalized away.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 6 | Conjecture 1.3 is printed as a numbered conjecture on page 6 and its three bullets were re-read off the rendered page. |
| openness | pass | 6 | Stays open: it is in Section 1.2 ('Open problems and future directions') and neither Theorem 1.1 nor Theorem 1.2 achieves its parameters. |
| strength | pass | 6 | Strength matches exactly: the three bullets are transcribed verbatim, including the log log lambda in the soundness exponent. |
| quantifiers-and-parameters | pass | 6 | Quantifiers checked bullet by bullet against the rendered page: soundness against t-query adversaries, proof size in G-elements plus bits, CRS size in G-elements. |
| attribution | pass | 6 | Conjecture 1.3 is the harvested paper's own. |
| definitions | pass | 15 | dv-SNARG and the generic group model are Definitions 3.4 and 3.2, reproduced with completeness, adaptive soundness and succinctness. |
| fabrication | pass | - | No fabrication. The draft records the two ingredients as identified-but-unestablished, which is what the source says, and does not claim either is proved. |
| self-containment | pass | - | Self-contained from Definitions 3.2 and 3.4. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The soundness term 2^{-tau + log log lambda} is unusual and is the source's; a reader may take it for a typo and prove the stronger 2^{-tau} statement. Also that the CRS is required linear and the random oracle disallowed, which is what separates the conjecture from the source's own Theorems 1.1 and 1.2.

