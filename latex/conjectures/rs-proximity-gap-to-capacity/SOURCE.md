# Provenance: Proximity Gaps for Reed-Solomon Codes Up to Capacity

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Proximity Gaps for Reed-Solomon Codes**
- Authors: Eli Ben-Sasson, Dan Carmon, Yuval Ishai, Swastik Kopparty, Shubhangi Saraf
- Venue/archive: IACR ePrint 2020
- Identifier: IACR ePrint 2020/654
- Bibliographic detail: inferred
- File: `2020-654.pdf` (61 pages)
- sha256: `a66a5d0d43e53b6a1cb83cbe87ee86e9c8f5c65562c85b22fef1396603ffe47f`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Proved up to the Johnson/Guruswami-Sudan bound delta < 1 - sqrt(rho); conjectured up to capacity delta <= 1 - rho - eta. Nothing known contradicts c1 = c2 = 2, and in characteristic greater than the degree nothing known contradicts c1 = c2 = 1, though those smaller exponents are ruled out in characteristic two.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | However, we conjecture that Theorem 1.2 holds even for larger proximity parameters, up to capacity (1 − ρ). See Conjecture 8.4 and the discussion there. |
| openness | 43 | 43 | exact (100%) | Closing the gap between the provable upper and lower bounds on s is left as an interesting open problem. |
| parameter | 43 | 43 | exact (100%) | To the best of our knowledge, nothing contradicts setting c1 = c2 = 2 in the conjecture below. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The statement is a numbered conjecture of the source, transcribed with both bullets and with the source's own calibration of the constants, including the characteristic-two exclusion that rules out the smaller pair. Nothing needed repair.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 43 | Conjecture 8.4 is printed as a numbered conjecture on page 43, with its two bullets. |
| openness | pass | 43 | Stays open: it is in the paper's discussion of two open questions, after all theorems, and the paper proves only up to the Johnson bound. |
| strength | pass | 4 | Strength matches: Remark 1.1 says the source conjectures Theorem 1.2 holds up to capacity, and Conjecture 8.4 states it for Theorems 1.2, 1.4, 1.5 and 1.6 with explicit error shapes. Both bullets transcribed. |
| quantifiers-and-parameters | pass | 2 | Quantifiers checked against Theorem 1.2 and Theorem 1.4: the error is piecewise, eps_U = n/q below the unique decoding radius and eps_J above it; correlated agreement gives a single D' of density 1 - delta on which every generator agrees with a codeword. |
| attribution | pass | 43 | Conjecture 8.4 is the harvested paper's own; the FRI query-count conjecture it would imply is attributed to BBHR18b as the paper does, and the characteristic-two obstruction to BGKS20's Appendix B. |
| definitions | pass | 2 | 'Proximity gap', 'correlated agreement', rate and blocklength are used in the source's senses; the code is RS[F_q, D, k] of dimension k+1. |
| fabrication | pass | - | No fabrication. The claim about what settling it buys is the source's own accounting, and the constants discussion is quoted rather than inferred. |
| self-containment | pass | - | Self-contained from the proximity-gap definition plus Theorem 1.2's error shapes. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That both bullets of Conjecture 8.4 are reproduced, including the Theorem 1.5 curve version with its (l n)^{c2}. And the characteristic caveat: the smaller exponents provably fail in characteristic two, so a resolution must state which characteristic it needs.

