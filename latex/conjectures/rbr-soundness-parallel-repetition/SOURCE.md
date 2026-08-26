# Provenance: Round-by-Round Soundness Amplification Under Parallel Repetition

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Sum-check Protocol for Approximate Computations**
- Authors: Dor Bitan, Zachary DeStefano, Shafi Goldwasser, Yuval Ishai, Yael Tauman Kalai, Justin Thaler
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/2152
- Bibliographic detail: inferred
- File: `2025-2152.pdf` (38 pages)
- sha256: `ffefa28176dc1164b11b641207aef309cecfc5bc32c3332c78b3661f99ed5392`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Known in the special case of r-round protocols whose standard and round-by-round soundness errors are maximally separated, eps_RBR about eps^{1/r}, by CCH+18's Corollary 5.7. Open in general, including the eps^{2/r} regime the source's own protocol occupies.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 24 | 24 | exact (100%) | We conjecture the following general amplification property: Let Π be an r-round interactive protocol with round-by-round (RBR) soundness error ϵ. Then, (k · r)-... |
| openness | 24 | 24 | exact (100%) | This conjecture is known to hold in the special case of r-round protocols whose soundness error ϵ and RBR soundness error ϵRBR are maximally separated |

## Adversarial check

**Verdict: faithful** (confidence: high)

The conjecture is Remark 3, transcribed from the rendered page, and the definition it rests on is the source's Definition 3. The known special case is recorded with its citation, and the factor r in the repetition count -- the easiest thing to get wrong -- was checked against the printed text.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 24 | Remark 3 is printed immediately after Theorem 4.8 and was re-read off the rendered page; the exponent is eps^k. |
| openness | pass | 24 | Stays open: the remark itself names the one case where it is known and claims nothing more. |
| strength | pass | 24 | Strength matches exactly: r-round protocol, round-by-round error eps, (k r)-fold parallel repetition, error at most eps^k. |
| quantifiers-and-parameters | pass | 24 | Quantifiers checked: the conjecture is over all r-round protocols and, as the draft states it, all k >= 1. The consequence about Fiat-Shamir bits is recorded as a consequence rather than folded into the statement. |
| attribution | pass | 24 | The conjecture is the harvested paper's own; the known special case is attributed to CCH+18's Corollary 5.7 as the paper does. |
| definitions | pass | 7 | Definition 3's three clauses are reproduced verbatim, including that clause 2 quantifies over every partial transcript, prover message and subsequent verifier message. |
| fabrication | pass | - | No fabrication. The eps^{2/r} figure for the source's own protocol is quoted from its conclusion, not computed here. |
| self-containment | pass | - | Self-contained from Definition 3. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the repetition count is k times r and not k -- the factor r is what makes the bound consistent with the known maximally-separated case. And that the difficulty is in exhibiting a doomed set for the repeated protocol, not in amplifying ordinary soundness.

