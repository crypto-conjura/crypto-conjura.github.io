# Provenance: Circuit Satisfiability Resists Small Space with Preprocessing

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Succinct Interactive Oracle Proofs: Applications and Limitations**
- Authors: Shafik Nassar, Ron D. Rothblum
- Venue/archive: IACR ePrint 2022
- Identifier: IACR ePrint 2022/281
- Bibliographic detail: inferred
- File: `2022-281.pdf` (37 pages)
- sha256: `8d40170a01642e911e9bf6cc8f4f1f8e4747a3a40418dae461b63157b0824fb7`
- Read on 2026-08-28T02:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Conjecture 1.2 of the source, a parameterized family rather than a single claim. Corollary 1.3 turns each parameter setting into a limitation on succinct IOPs. The source attaches decreasing confidence as the class T grows, calling the largest setting only '(arguably) unlikely' to be false.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 5 | 5 | exact (100%) | For a function class T , the conjecture states that CSAT for circuits of size n over m input bits cannot be solved by an algorithm that uses poly(m) space and t |
| confidence | 5 | 5 | exact (100%) | we conjecture that even probabilistic quasi-polynomial time preprocessing would not be sufficient, and taking things |
| consequence | 5 | 5 | exact (100%) | With t(n, m) = poly(n), there is no succinct IOP for RCSAT with a constant number of rounds and O(log n) query complexity. |
| refutation | 33 | 33 | exact (100%) | it would imply a surprising interplay between space and time complexities and in particular, yield an interesting space-time trade-off for CSAT. |
| calibration | 33 | 33 | exact (100%) | it was later proved that for general circuits, the pebbling approach cannot do much better |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 1.2 is verbatim on page 5 and is transcribed as printed, including its parameterization by T. The correction is one of emphasis, recorded in a dedicated remark: because the conjecture is a scale of hypotheses rather than one claim, and because the source explicitly attaches different confidence to different settings of T, a resolution in either direction is meaningless unless it names its T. Without that remark a reader would take the statement to be a single proposition.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
