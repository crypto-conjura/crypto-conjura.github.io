# Provenance: Perfect Fully Anonymous Secret Sharing for the 3-out-of-5 Threshold

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Fully Anonymous Secret Sharing**
- Authors: Allison Bishop, Matthew Green, Yuval Ishai, Abhishek Jain, Paul Lou
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/1984
- Bibliographic detail: inferred
- File: `2025-1984.pdf` (74 pages)
- sha256: `852bbd19477fd62e9f9f8b41b0b7ecb719d1895df0162a02b3ccca065500c4e5`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. Statistical and computational FASS are settled by the source and prior work. The perfect version is stated by the source to be open for every reconstruction threshold 3 <= t <= n-2, and open even for the weaker multi-dealer notion, with 3-out-of-5 the smallest open case.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 17 | 17 | exact (100%) | The first open question is the possibility of perfect U-FASS for general access structures, namely U-FASS with both perfect uniformity and perfect correctness. |
| openness | 17 | 17 | exact (100%) | The question is open even for threshold structures with reconstruction threshold 3 ≤ 𝑡 ≤ 𝑛 − 2 and even for the weaker notion of perfect M-FASS. In particular, ... |
| openness | 17 | 17 | exact (100%) | Interesting progress on this question has been recently made by Con [Con24], who shows that Shamir’s original scheme can be instantiated to give a perfect U-FAS... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question and the 3-out-of-5 instance are verbatim in Section 2.4 and stay open. One choice needed recording: the source poses it at U-FASS but says it is open even at M-FASS, so the statement is posed at M-FASS with the relationship between the two spelled out.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 17 | The open question is the first item of Section 2.4, and it names the 3-out-of-5 case explicitly. |
| openness | pass | 17 | Stays open: the section is the paper's open-questions list and the progress it reports (Con) covers gap thresholds only. |
| strength | fail | 17 | The source asks for perfect U-FASS and adds that the question is open 'even for the weaker notion of perfect M-FASS'. Stating it at U-FASS would be the stronger reading; the draft states it at M-FASS, which is the notion the source flags as already unknown, with a remark recording that a U-FASS construction is strictly better and that an impossibility at M-FASS settles U-FASS too. |
| quantifiers-and-parameters | pass | 23 | Definitions 4.1 and 4.2's quantifiers reproduced, including that U-anonymity compares against the uniform distribution on the publicly known single-share support and that M-anonymity's distinguishing task swaps exactly one share. |
| attribution | pass | 17 | The question is the harvested paper's own; the gap-threshold progress is attributed to Con as the paper does. |
| definitions | pass | 17 | The constant-share-size clause is the source's own reading of 'perfect', quoted rather than inferred. |
| fabrication | pass | - | No fabrication. The draft states that the source's Omega(ell) lower bound does not apply here, which the source itself says of the single-minterm and small-threshold cases. |
| self-containment | pass | - | Self-contained from Definitions 3.5, 4.1 and 4.2. |

### Corrections the checker asked for

- **formal_statement_latex** — Choice between the U-FASS and M-FASS readings.
  - suggested: State the conjecture at M-FASS, matching the source's 'even for the weaker notion' clause, and add a remark on how the two readings relate in each direction.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That 'perfect' includes the share size being independent of any security parameter -- the source says a perfect U-FASS scheme must provide anonymity with constant-size shares -- since otherwise the known Shamir variant would already qualify. And that the statement is at the weaker M-FASS notion, as the source's 'even for' phrasing indicates.

