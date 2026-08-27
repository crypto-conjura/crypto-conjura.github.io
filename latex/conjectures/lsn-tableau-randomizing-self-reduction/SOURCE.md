# Provenance: No Tableau-Randomizing Self-Reduction for Learning Stabilizer with Noise

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Average-Case Complexity of Quantum Stabilizer Decoding**
- Authors: Andrey Boris Khesin, Jonathan Z. Lu, Alexander Poremba, Akshar Ramkumar, Vinod Vaikuntanathan
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/1769
- Bibliographic detail: inferred
- File: `2025-1769.pdf` (77 pages)
- sha256: `61ae34e71d997ddc8eed3310fba70fbc0eff755fc3d7106405cf8d2964466ac4`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Conjecture 5.20 of the source. It proves a conditional barrier via what it calls the scrambling gap, exhibits an analogous classical no-go, and conjectures the barrier can be made unconditional for tableau-randomizing reductions. It is explicit that this is not an impossibility for random self-reductions in general.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 62 | 62 | near (98%) | There is no (V, ϵ, w, p) tableau-randomizing random self-reduction operator (as de1 fined in Definition 5.7) for LSN, for any V ⊆ Cn , w ≥ 1, such that ϵ = negl |
| openness | 62 | 62 | exact (100%) | It remains an open question as to whether these barriers can be surpassed, or can be strengthened to a complete impossibility theorem for random self-reductions |
| belief | 62 | 62 | exact (100%) | We conjecture that, at least in the case of tableau-randomizing reductions, analysis techniques generalizing the scrambling gap formalism will reveal unconditio |
| caveat | 62 | 62 | exact (100%) | these barriers do not definitely prove the non-existence of a random self-reduction. |
| obstruction | 52 | 52 | exact (100%) | The culprit preventing the existence of such a reduction is exchange symmetry between the code and the error |
| triviality | 52 | 52 | exact (100%) | A reduction with p = 43 is always possible, as this error is equivalent to replacing the encoded state |

## Adversarial check

**Verdict: faithful** (confidence: high)

Conjecture 5.20 is on page 62 and grounds at 99% coverage; the shortfall is a footnote marker splitting 'defined' across a line break in the text layer, not a wording difference. No repair was needed. The statement records the three escapes the source itself names -- non-tableau-randomizing reductions, dimension-increasing isometries, and eps = 1/poly(n) with smaller p -- because without them a reader would over-read the conjecture as an impossibility for self-reductions generally, which the source explicitly disclaims.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
