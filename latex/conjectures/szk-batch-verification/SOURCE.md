# Provenance: Batch Verification for Statistical Zero Knowledge

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Strong Batching for Non-Interactive Statistical Zero-Knowledge**
- Authors: Changrui Mu, Shafik Nassar, Ron D. Rothblum, Prashant Nalini Vasudevan
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/229
- Bibliographic detail: inferred
- File: `2024-229.pdf` (31 pages)
- sha256: `a23487ab021835b6b2430eaba75a5e55ac569f0eb4b64c73943b581aac80824d`
- Read on 2026-08-28T02:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. Named by the source as 'the most pressing open question' its work leaves. Its Theorem 1.1 gives the NISZK analogue: communication and CRS length poly(n, log k) for k up to 2^(n^0.01). A poly(n) dependence is unavoidable even at k = 1 under a sub-exponential hardness assumption, so log k is the aggressive part of the bound.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 12 | 12 | exact (100%) | The most pressing open question is whether a similar result holds for SZK |
| fallback | 12 | 12 | exact (100%) | Or, alternatively, one that features less strigent, yet non-trivial, communication such as sub-linear dependence on k? |
| proved | 20 | 20 | near (100%) | Then, Π⊗k has an NISZK protocol in which the communication complexity and the length of the common random string is |
| inevitable | 4 | 4 | exact (100%) | We remark that a poly(n) dependence in the communication complexity is inevitable, even when k = 1, assuming the existence of a sub-exponentially hard problem i |
| technique | 4 | 4 | exact (100%) | Hash functions with bounded independence (specifically 4-wise independence su |
| neighbour | 12 | 12 | exact (100%) | Is it possible to construct batch protocols even for NISZK ∩ NP that preserve prover e |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is verbatim on page 12 and is recorded in the affirmative because a statement needs a direction; the source poses it as a question and predicts nothing. Two corrections are recorded rather than applied. The source offers a weaker fallback in the same sentence -- any sub-linear dependence on k -- and the statement says a resolution should report which target it hits. And the source's own theorem carries a range restriction on k that the question does not repeat, so the statement asks a resolution to name its range.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
