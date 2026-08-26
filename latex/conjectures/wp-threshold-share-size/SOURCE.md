# Provenance: Weakly Private (n-1)-out-of-n Secret Sharing Below Logarithmic Share Size

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Cryptography with Weak Privacy**
- Authors: Amos Beimel, Yuval Ishai, Eyal Kushilevitz, Hanjun Li
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/1978
- Bibliographic detail: inferred
- File: `2025-1978.pdf` (40 pages)
- sha256: `5b0cc33ee9cf0d3b228d475a7ca917cab11ce3db2eb7ffcdf905f38828a614cf`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. The 2-out-of-n case is settled: Beimel and Franklin give 1/n-weakly-private schemes with share size 2, against Theta(log n) for perfect privacy. The source states large thresholds are open and asks specifically about (n-1)-out-of-n at share size o(log n).

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | Beimel and Franklin [9] constructed 1/n-WP 2-out-of-n threshold secret-sharing schemes with share size 2, leaving the case of large thresholds open. Is there a ... |
| openness | 7 | 7 | exact (100%) | In addition to extending this study to other primitives, our results leave several natural open problems. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The question is verbatim in the source's open-problems list and the only definition it needs is the source's own Definition 2.2. The one thing worth stating explicitly, and stated, is that the source does not pin the privacy parameter p.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 7 | The question is the last item of the source's 'Open Problems' list, with the Beimel-Franklin benchmark in the same sentence. |
| openness | pass | 7 | Stays open: it is in the open-problems list, after all of the paper's results. |
| strength | pass | 7 | Strength matches: the source asks for a WP (n-1)-out-of-n scheme with share size o(log n), which is the drafted statement. |
| quantifiers-and-parameters | pass | 12 | Definition 2.2's quantifiers reproduced: for every unauthorized set, every pair of secrets and every share vector, one-sided inequality with factor p; perfect correctness for every authorized set and every randomness. |
| attribution | pass | 7 | The question is the harvested paper's own; the 2-out-of-n construction is attributed to Beimel and Franklin as the paper does. |
| definitions | pass | 12 | The draft keeps the source's distinction between weak privacy and secrecy, and its share-size conventions (max share size, size of the secret). |
| fabrication | pass | - | No fabrication. The Theta(log n) perfect-privacy figure is attributed to the works the paper cites for it, not to the paper itself. |
| self-containment | pass | - | Self-contained from Definition 2.2 plus the threshold structure. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the threshold really is n-1 and the unauthorized sets therefore of size n-2, which is what makes the case different from Beimel-Franklin's threshold 2. And that no bound on p is being smuggled in: the source asks for weak privacy without pinning p.

