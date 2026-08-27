# Provenance: Average-Case Hardness of Planted k-Orthogonal Vectors

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **The Planted Orthogonal Vectors Problem**
- Authors: David Kuehnemann, Adam Polak, Alon Rosen
- Venue/archive: IACR ePrint 2025
- Identifier: IACR ePrint 2025/780
- Bibliographic detail: inferred
- File: `2025-780.pdf` (20 pages)
- sha256: `349a84df85c4475d4c2acfe5f43786eea65ed0f0eb2c187f30374057017b6aae`
- Read on 2026-08-28T02:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Conjecture 10 of the source, and a newly proposed average-case assumption rather than a question the literature already asked. Its worst-case counterpart -- that k-OV requires n^(k-o(1)) time -- is a central conjecture of fine-grained complexity.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 11 | 11 | exact (100%) | For any α(n) = ω(1) and ε > 0, there exists no algorithm A that solves the planted decision k-OV problem with any constant success probability δ > |
| marginals | 1 | 1 | exact (100%) | Our planted distribution has the property that any subset of strictly less than k vectors has the same marginal distribution as in the model distribution, consi |
| motivation | 1 | 1 | exact (100%) | The security of cryptographic systems crucially relies on heuristic assumptions about averagecase hardness of certain computational problems. |
| goal | 4 | 4 | exact (100%) | A key goal of fine-grained cryptography is to devise an advanced asymmetric cryptography scheme |
| s2d | 12 | 12 | exact (100%) | Theorem 12 (Search-to-decision reduction). For any α(n) = polylog(n), if there exists an algorithm that solves the planted decision k-OV problem |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

Conjecture 10 is verbatim on page 11 and needed no repair. Two things are recorded rather than assumed. First, the statement says explicitly what kind of claim this is -- a newly proposed assumption awaiting cryptanalysis, published because the underlying object is canonical and the planting is analysed rather than merely asserted, not because the literature had posed it. Second, a parameter mismatch the source does not flag: the conjecture is stated for alpha = omega(1) while the search-to-decision reduction requires alpha = polylog(n), so a resolution should say which regime it addresses.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
