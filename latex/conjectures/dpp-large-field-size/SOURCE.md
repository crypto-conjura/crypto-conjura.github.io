# Provenance: Improving the Field Size of Large-Field Dot-Product Proofs

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Dot-Product Proofs and Their Applications**
- Authors: Nir Bitansky, Prahladh Harsha, Yuval Ishai, Ron D. Rothblum, David J. Wu
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/1138
- Bibliographic detail: inferred
- File: `2024-1138.pdf` (83 pages)
- sha256: `61393d1dc1e4057fec1b58eaf6291784bc90eba8cb89b53a1ae8b7187846880a`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. The small-field regime is settled: soundness Theta(1/sqrt q) is achieved and proved optimal. In the large-field regime the source achieves soundness eps for every prime p >= Omega~(S^9/eps^6) and states it believes the S-dependence is not tight.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | We believe that the analysis of our compiler is not tight, and leave open the question of improving the bound on p given by Theorem 1.3. |
| openness | 9 | 9 | exact (100%) | In particular, we conjecture that the dependence on S (i.e., the circuit size) in our current soundness bound can be im- |
| statement | 9 | 9 | exact (100%) | This was shown in the simpler case of the Hadamard-based LPCP using a random walk argument [BIOW20], |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is footnote 6 and the open question is on page 4, both verbatim. Two repairs: the exponent had to be existentially quantified because the source names no target, and one bibliography entry was misattributed and was corrected against the paper's own reference list.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 4 | Both the open question ('improving the bound on p given by Theorem 1.3') and the conjecture (footnote 6, page 7) are in the paper. |
| openness | pass | 7 | Stays open: footnote 6 is attached to the concrete-efficiency discussion in Section 1.1.3, after all constructions. |
| strength | fail | 7 | The source says the S-dependence 'can be improved' without a target exponent. Repaired by asking for some a < 9 and adding a remark that any resolution should report the pair it achieves, plus naming the two stronger targets the source does not claim. |
| quantifiers-and-parameters | pass | 4 | Theorem 1.3's quantifiers reproduced: promise DPP, prime p >= Omega~(S^9/eps^6), proof length O(S log(S/eps)), perfect completeness, soundness eps. |
| attribution | pass | 7 | The conjecture is the harvested paper's own; the random-walk precedent is attributed to BIOW20 as the paper does. |
| definitions | pass | 3 | 'Promise DPP' is used in the source's sense (soundness only for Boolean x, no promise on the proof). The distinction matters: the non-promise variant costs proof length O(S + n^2) and a worse p. |
| fabrication | fail | 7 | An earlier draft attributed BIOW20 to Bitansky et al. and titled it 'Weakly extractable one-way functions'; the source's reference list gives Barta, Ishai, Ostrovsky and Wu, 'On succinct arguments and witness encryption from groups'. Corrected. |
| self-containment | pass | - | Self-contained from the DPP definition alone. |

### Unsupported by the paper

- An earlier draft's bibliography misattributed [BIOW20]; corrected against the source's own reference list.

### Corrections the checker asked for

- **formal_statement_latex** — No target exponent is named by the source.
  - suggested: Ask for some a < 9 with the eps-exponent free, and add a remark recording that the source names no target and that the two stronger readings are not claimed.
- **bibliography** — [BIOW20] misattributed.
  - suggested: Ohad Barta, Yuval Ishai, Rafail Ostrovsky and David J. Wu, 'On succinct arguments and witness encryption from groups', CRYPTO 2020.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the conjecture is about the S-dependence specifically, not about closing the polynomial gap to the optimal O(1/sqrt |F|) soundness -- the source treats those as different questions and says the second may need a different approach. Also that proof length is held at O(S log(S/eps)): the source can already trade it for a worse dependence of p.

