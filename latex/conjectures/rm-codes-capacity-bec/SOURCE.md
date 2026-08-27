# Provenance: Reed-Muller Codes Efficiently Achieve Capacity for the Binary Erasure Channel

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Expanders Meet Reed-Muller: Easy Instances of Noisy k-XOR**
- Authors: Jaroslaw Blasiok, Paul Lou, Alon Rosen, Madhu Sudan
- Venue/archive: IACR ePrint 2026
- Identifier: IACR ePrint 2026/664
- Bibliographic detail: inferred
- File: `2026-664.pdf` (24 pages)
- sha256: `f0ba41ccc938a31f500e3051395e9910d289de735274b315251f3c32f63a29eb`
- Read on 2026-08-28T02:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Conjecture 14 of the source. That Reed-Muller codes achieve capacity for the BEC is a theorem of Kudekar et al.; what is open is the gap to capacity, i.e. a polynomial rate of convergence. The source needs it to strengthen its refutation of the expansion-implies-hardness conjecture for noisy k-XOR from quasi-polynomially many constraints to polynomially many.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 9 | 9 | exact (100%) | There exists a constant γ, such that for every m, r ∈ N such that RM(m, r) has rate at most 1 − ϵ, a random erasure pattern |
| openness | 9 | 9 | exact (100%) | The question of the gap-to-capacity results for RM codes for symmetric channels has been explicitly raised in |
| equivalent | 9 | 9 | exact (100%) | Conjecture 14 is equivalent to a statement that with probability 1 − o(1) there is no non-zero polynomial in |
| weak | 9 | 9 | exact (100%) | In fact, a plausibly simpler-to-prove conjecture suffices to derive a counterexample to the noisyXOR distinguishing problem where the number of constraints M is |
| need | 8 | 8 | exact (100%) | To get a result for a polynomial number of equations in the number of variables we need much faster rate of convergence to capacity than is currently known. |
| calibration | 9 | 9 | exact (100%) | this type of gap-to-capacity behavior is true and relatively simple to show for random codes, with a scaling exponent |
| neighbour | 4 | 4 | exact (100%) | we leave open the question of whether a random subspace construction of coset graphs is expanding. |

## Adversarial check

**Verdict: faithful** (confidence: high)

Conjecture 14 is verbatim on page 9 with its openness marker in the same paragraph. No repair was needed. The statement records three things from elsewhere in the source so the conjecture is not over-read: the weaker Conjecture 16 that already suffices for the application, the fact that the refutation of the expansion conjecture is unconditional and only its strongest form needs this, and the source's own note that the question is not its own but imported from the coding-theory literature.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
