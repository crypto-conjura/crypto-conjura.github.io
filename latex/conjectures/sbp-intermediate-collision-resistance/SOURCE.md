# Provenance: Collision Resistance of the Symmetric Binary Perceptron

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Collision Resistance of Single-Layer Neural Nets**
- Authors: Marco Benedetti, Andrej Bogdanov, Enrico M. Malatesta, Marc Mezard, Gianmarco Perrupato, Alon Rosen, Nikolaj I. Schwartzbach, Riccardo Zecchina
- Venue/archive: IACR ePrint 2026
- Identifier: IACR ePrint 2026/1143
- Bibliographic detail: inferred
- File: `2026-1143.pdf` (35 pages)
- sha256: `34a65a59d117268e7f22371a581de029465d43a09ee3f3be8d6ed9b9fdfc1b20`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. Posed as a displayed Open Question and called a central open challenge. The source gives an efficient online collision finder for small kappa and an overlap-gap-based online lower bound for a different, randomized activation -- introduced precisely because the SBP's own collision space resists a first-moment analysis.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 5 | 5 | exact (100%) | For some α < 1, does there exist an intermediate window of κ |
| openness | 3 | 3 | exact (100%) | Resolving whether SBP is collision resistant in this middle regime, for some α < 1 and some κ, remains a central open challenge. |
| gap | 3 | 3 | exact (100%) | The difficult case is the intermediate window, where the positive-tail escape route no longer applies but no OGP-based hardness result is known for collision fi |
| whymodel | 5 | 5 | exact (100%) | This extra randomness removes the rigid alignments that make the SBP collision space difficult to analyze, while preserving the obstruction to the positive-tail |
| neighbour | 7 | 7 | exact (100%) | We leave confirming this conjecture, or finding algorithmic counterexamples, as an open direction for future work. |
| concrete | 5 | 5 | exact (100%) | Neither known algorithmic techniques nor hardness arguments currently apply when κ lies in an intermediate window |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The Open Question is verbatim on page 5 and is recorded in the affirmative purely because a statement needs a direction; a remark says so explicitly and notes the source predicts nothing. Two page claims were corrected by grounding: the 'central open challenge' and 'difficult case' passages are on page 3, not 4, and the 'neither known algorithmic techniques' passage is on page 5, not 4. The paper's numbered Conjecture 1.4 is a different statement -- it concerns the randomized oscillating activation, not the SBP -- and is recorded as a neighbour rather than merged in.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
