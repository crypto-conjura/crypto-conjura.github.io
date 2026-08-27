# Provenance: 192-Round AES Is 2^-128-Close to Pairwise Independent

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Layout Graphs, Random Walks and the t-wise Independence of SPN Block Ciphers**
- Authors: Anastasiya Pelecanos, Stefano Tessaro, Vinod Vaikuntanathan
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/083
- Bibliographic detail: inferred
- File: `2024-083.pdf` (49 pages)
- sha256: `660e7b32c483da5c906a42b2a952e239b2678d04ff0c2cb7fb0c58d1f51a4555`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Theorem 7 proves the bound for '192-round censored AES' -- real AES S-boxes and mixing layer, but a subset of the mixing layers removed. The source conjectures the same round count suffices for AES itself, i.e. that censoring never increases security, and calls proving it an outstanding open problem. The best proved bound for actual AES is Liu-Tessaro-Vaikuntanathan's, needing more than 9000 rounds.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | We conjecture that 192-round of AES itself is also 2−128 -close to pairwise independent, i.e., the censoring mixing layers never increases security. |
| openness | 29 | 29 | exact (100%) | We view proving this conjecture formally to be an outstanding open problem. |
| rationale | 29 | 29 | exact (100%) | If one believes that the mixing layers are useful for AES to achieve pseudorandomness, then it is natural to expect that removing a large fraction of them shoul |
| proved | 7 | 7 | exact (100%) | We give a censored variant of AES which is 2−128 -close to pairwise independent after 192 rounds. |
| prior | 7 | 7 | exact (100%) | This should be contrasted with [LTV21], which shows that AES is 2−128 -close to pairwise independent after (more than) 9000 rounds. |
| thm6 | 28 | 28 | exact (100%) | The 7-round AES∗ is 2−128 -close to pairwise independent. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The conjecture is verbatim on page 7 with its rationale repeated on page 29 and the openness marker attached there. No repair was needed to the statement. Three contextual facts were added from elsewhere in the source and its predecessor, each grounded: Theorem 6's 7-round bound for AES*, the >9000-round prior bound for real AES, and the arithmetic by which 192 is reached. The independent-round-keys assumption is flagged prominently because the source states it and it is what separates the result from AES-128 as deployed.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
