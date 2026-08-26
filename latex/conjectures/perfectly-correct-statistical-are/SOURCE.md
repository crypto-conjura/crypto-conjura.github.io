# Provenance: A Perfectly Correct Statistically Secure Additive Randomized Encoding

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Shuffling is Universal: Statistical Additive Randomized Encodings for All Functions**
- Authors: Nir Bitansky, Saroja Erabelli, Rachit Garg, Yuval Ishai
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/1442
- Bibliographic detail: inferred
- File: `2025-1442.pdf` (23 pages)
- sha256: `45510b5dcac7eae92afbaf9a575b02fe861373e713adac4a6987c0f2ac282b3a`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. Statistical security with statistical correctness is settled by the source for every finite function. Perfect correctness is known in the computational setting and, in the statistical setting, only in a relaxed Las Vegas form where the evaluator may declare failure.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | Does every 𝑓 admit a perfectly correct and statistically secure ARE? |
| openness | 7 | 7 | exact (100%) | For ARE with statistical security, we are only able to achieve a relaxed “Las Vegas” notion of correctness, where the evaluator is never wrong but may declare f... |
| openness | 7 | 7 | exact (100%) | Our work leaves several interesting questions for future research. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The question is verbatim in the source's open-questions list, the definition it rests on is the source's Definition 2.1, and the Las Vegas relaxation that stands between the source's theorem and the question is recorded rather than glossed. Nothing needed repair.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 7 | The question is the first bullet of Section 1.4 ('Open Questions'). |
| openness | pass | 7 | Stays open: the bullet itself records that only Las Vegas correctness is achieved, pointing at Appendix A. |
| strength | pass | 7 | Strength matches: 'Does every f admit a perfectly correct and statistically secure ARE?' is exactly the drafted statement. |
| quantifiers-and-parameters | pass | 2 | Theorem 1.1's quantifier structure is respected: for any f over a finite domain and any error bound, an ARE with both errors at most that bound. The draft's statement fixes the correctness error at 0 and leaves the security error free, which is the question asked. |
| attribution | pass | 7 | The question is the harvested paper's own; ARE is attributed to HIKR23 and the perfect-correctness precedents to HIKR23 and BEG25 as the paper does. |
| definitions | pass | 7 | Definition 2.1 is reproduced with eps-correctness and delta-security separate, which is what makes the question well-posed. |
| fabrication | pass | - | No fabrication. The draft does not claim the source conjectures an answer; it states that the source poses the question. |
| self-containment | pass | - | Self-contained from Definition 2.1. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That Las Vegas correctness is not mistaken for perfect correctness -- a decoder that may output bottom does not resolve this. And that the statement is a feasibility question over finite domains, not an efficiency question; the efficiency question (extending NL/poly to P/poly) is a different open problem the source says would settle FKN94.

