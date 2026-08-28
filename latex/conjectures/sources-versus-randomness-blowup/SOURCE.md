# Provenance: The Price in Coins of Using Few Random Sources

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Random Sources in Private Computation**
- Authors: Geoffroy Couteau, Adi Rosén
- Venue/archive: IACR ePrint / ASIACRYPT 2022
- Identifier: IACR ePrint 2023/074
- Bibliographic detail: printed-in-source-bibliography
- File: `2023-074.pdf` (23 pages)
- sha256: `3ee68dc075bae1eba040c2a3aae8c249448315cffc19ab15d5c5c59e5cd65e86`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Printed as Conjecture 13 of the source, which calls proving it an interesting open question. Both halves are open: neither the O(t Rt) upper bound as a generic transformation nor the Omega(t Rt) lower bound is known. The source settles the neighbouring counting question exactly -- t sources are necessary and sufficient for deterministic functionalities, t+1 for randomized ones -- so what remains is the exchange rate, not the count.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 16 | 16 | exact (100%) | Let F be an n-party functionality that cannot be t-privately computed for t ≥ n/2. For any t < n/2, let Rt be the randomness complexity of t-privately computing... |
| openness | 15 | 15 | exact (100%) | We view the proof of Conjecture 13 an interesting open question. |
| framing | 4 | 4 | exact (100%) | Our conjecture states that, for such functionalities, a Θ(t) blowup in randomness complexity is necessary and sufficient to minimize the number of random source... |
| intuition | 15 | 15 | exact (100%) | We warn the reader that what follows is a purely intuitive reasoning: our goal here is to develop an intuition about which conjecture can reasonably be expected... |
| difficulty | 16 | 16 | exact (100%) | Characterizing the minimal amount of randomness required for securely computing a functionality is non-trivial in general, and indeed, no such general character... |
| xor | 15 | 15 | exact (100%) | This seemingly contradicts the intuition that t-source private computation should require more randomness than private computation without limitations on the nu... |
| constant-t | 16 | 16 | exact (100%) | Note that t being a constant captures a setting where matching the best known randomness complexity would not contradict Conjecture 13. |

## Adversarial check

**Verdict: faithful** (confidence: high)

Conjecture 13 is printed in the source in exactly this form and is transcribed verbatim, so nothing about its strength or its quantifiers is this statement's choice. All seven quotes ground exact on the pages claimed. The definitions of randomness complexity, source and t-source randomness complexity are the source's usage; the source does not give them numbered definitions, and the notation section here states them explicitly so the conjecture is readable without the paper. The XOR upper bound of Kushilevitz-Mansour and the constant-t AND result are recorded as compatible rather than contradictory, in the source's own words. A forward literature check on 28 August 2026 found the conjecture open; the nearest follow-up located, Randomness in Private Sequential Stateless Protocols (ePrint 2024/1448), studies a different restriction.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

Three things. First, Theta hides an upper bound and a lower bound and a partial result settles only one, so a resolution must say which. Second, the hypothesis is a property of the functionality, not of a protocol, so one complex F beating Omega(t Rt) refutes it. Third, the intuition the source offers for the conjecture is explicitly labelled non-rigorous by the source itself, and should not be mistaken for a proof sketch.

