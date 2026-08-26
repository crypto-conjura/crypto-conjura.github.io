# Provenance: A Balanced Square-Root Information-Theoretic Preprocessing PIR

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **PIR with Client-Side Preprocessing: Information-Theoretic Constructions and Lower Bounds**
- Authors: Yuval Ishai, Elaine Shi, Daniel Wichs
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/976
- Bibliographic detail: inferred
- File: `2024-976.pdf` (41 pages)
- sha256: `2eec344698a3764b0d2f6670f8389e992f847f6363610c66594a5d35b36018cf`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The client-space-times-bandwidth product is settled up to n^{o(1)} by the source's own matching bounds. What is open is whether client space, bandwidth and per-query server computation can be O~(n^{1/2}) simultaneously; the source's best scheme has client space and server computation O~(n^{2/3}).

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | It is a fascinating open problem whether it is possible to close this gap and achieve a scheme where the client space, bandwidth and server computation are all ... |
| openness | 7 | 7 | exact (100%) | In the sublinear-server-computation regime, there is still some gap between our upper bound (Theorem 1.4) and the lower bounds (Theorem 1.1, [CK20, Theorem 23])... |

## Adversarial check

**Verdict: faithful** (confidence: high)

The statement is the source's own sentence, at its own strength, with the cost measures used as the source defines them and the lower bound it must respect quoted from the same paper. Nothing needed repair.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 7 | The sentence naming the open problem, with the O~(n^{1/2}) target for all three measures, is on page 7 and was re-read off the rendered page rather than the text layer. |
| openness | pass | 7 | Stays open: it appears after Theorem 1.4, the paper's best construction, and nothing later improves on that profile. |
| strength | pass | 7 | Strength matches: the source asks for all three measures at O~(n^{1/2}), which is what the draft states, with no strengthening to exact bounds or weakening to two measures. |
| quantifiers-and-parameters | pass | 2 | Theorem 1.1's quantifiers are reproduced carefully: it constrains the initial client hint only, and holds against arbitrary server encoding, dynamic state, unbounded polynomial computation and any number of round trips. |
| attribution | pass | 7 | The open problem is the harvested paper's; the second bracketing lower bound is attributed to CK20 as the paper does. |
| definitions | pass | 3 | Online versus offline bandwidth, and 'server computation' as bits read, are used in the source's senses; Table 1 was checked for the cost profile. |
| fabrication | pass | - | No fabrication found. The draft does not claim the source proves the target impossible, which it does not. |
| self-containment | pass | - | Self-contained: the model definition plus three cost measures. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the statement is not accidentally excluded by the source's own Theorem 1.1 -- it is not, since the client-space-times-bandwidth product at the target is O~(n), which the bound permits. And that server computation, the third clause, is the genuinely new demand rather than a restatement of the first two.

