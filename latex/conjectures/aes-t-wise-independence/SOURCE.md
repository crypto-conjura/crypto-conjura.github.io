# Provenance: t-Wise Independence of AES for t > 2

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **The t-wise Independence of Substitution-Permutation Networks**
- Authors: Tianren Liu, Stefano Tessaro, Vinod Vaikuntanathan
- Venue/archive: IACR ePrint 2021
- Identifier: IACR ePrint 2021/507
- Bibliographic detail: inferred
- File: `2021-507.pdf` (51 pages)
- sha256: `1477e9eaea3822b67a3274f136ff8a4f5924614bd7ae7c481c1757a9255c3356`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. Named by the source as the first of 'the two outstanding open problems that come of this work'. It proves almost pairwise independence (t = 2) for multi-round AES with independent round keys, and an existential t-wise result for key-alternating ciphers with most permutations, but nothing for concrete AES beyond t = 2.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | the two outstanding open problems that come of this work are (a) to prove t-wise independence of multi-round AES with independent round keys, for t > 2; and (b) |
| keys | 7 | 7 | exact (100%) | understanding the precise role of key schedules is an important open problem. |
| prior | 31 | 31 | exact (100%) | 6r-round AES is 2r−1 (0.472)r -close to pairwise independence. |
| attack | 46 | 46 | exact (100%) | We show that for a modest number of rounds r |
| scope | 1 | 1 | exact (100%) | Sufficiently strong (almost) pairwise independence already suffices to resist (truncated) differential attacks and linear cryptanalysis |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open problem is verbatim on page 7 but is named without quantifiers: no t, no eps, no target round count. The quantifier structure in the conjecture -- for every t and eps, some finite r -- is this statement's choice and is flagged as such in a dedicated remark, along with the note that a resolution should report the dependence r(t,eps). The second correction is contextual: the source's own Appendix B refutes the width-1 specialization of the claim at modest round counts, which is recorded as an obstruction rather than buried, together with the reason (Carlitz) that it does not refute the conjecture itself.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
