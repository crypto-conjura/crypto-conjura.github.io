# Provenance: Soundness of the Hold-Out Test on Dirty Ciphertext Coordinates

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Quasipolynomial Cryptanalysis of the McEliece Cryptosystem (or: PIR Meets McEliece)**
- Authors: Ashrujit Ghoshal, Yuval Ishai, Aayush Jain, Nuozhou Sun
- Venue/archive: IACR ePrint 2026
- Identifier: IACR ePrint 2026/1630
- Bibliographic detail: inferred
- File: `2026-1630.pdf` (63 pages)
- sha256: `bb767d7beb40e649ae0f04841458583b3abb623ab1531530b2dbd67bd9cbdb39`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The source's distinguishing attack is unconditional and proved. Its decryption attack is heuristic, and this is the unproved step: completeness on clean coordinates is its Claim 6.2, while soundness on dirty ones is supported only by a heuristic dimension count and small-parameter experiments.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 12 | 12 | exact (100%) | For a dirty coordinate eτ ̸= 0, we do not currently have a proof that the hold-out test rejects τ for either code family. |
| openness | 40 | 40 | exact (100%) | We currently do not have a proof to lower bound the probability of this event. |
| openness | 14 | 14 | exact (100%) | Further validation of the underlying conjectures, or ideally an unconditional proof of quasipolynomial decryption, are left for future work. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The unproved step is stated twice in the source's own words and the paper asks for exactly this proof. The statement reproduces Algorithm 3's kernel and Claim 6.2's completeness condition, and records that the binary Goppa family -- the one Classic McEliece uses -- is the case with no end-to-end experimental support.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 12 | The gap is stated twice in the source: in Section 1.1.2 ('we do not currently have a proof that the hold-out test rejects tau for either code family') and after Claim 6.2 ('We currently do not have a proof to lower bound the probability of this event'). |
| openness | pass | 40 | Stays open: Appendix A supplies heuristics and experiments, never a proof, and Section 1.2 asks for an unconditional proof of quasipolynomial decryption. |
| strength | pass | 12 | Strength matches: the source's missing step is rejection of dirty coordinates, which is what the statement asserts. The completeness half is not claimed here. |
| quantifiers-and-parameters | pass | 38 | Quantifiers taken from Algorithm 3 and Claim 6.2: the kernel condition is over every j != tau and every a in A_{<s,k+1}; the completeness condition is s(\|I_cl\| - 1) > d D, which the statement requires the parameters to satisfy. |
| attribution | pass | 37 | The hypothesis is the harvested paper's own; the multiplicity-code machinery is attributed to KSY14 as the paper does. |
| definitions | pass | 20 | Hasse derivatives, Hasse jets and A_{<s,k} are used as Definitions 2.7 and 2.9 define them; the McEliece key distribution is Definition 2.4. |
| fabrication | pass | 12 | No fabrication. The conditional conclusion about the quadratic ciphertext barrier is stated as conditional, and the distinguishing attack is stated as unconditional, matching the source. |
| self-containment | pass | - | Self-contained: the kernel definition, the instance distribution and the completeness condition are all given. |

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the statement is for binary Goppa, the family Classic McEliece actually uses, and not only for GRS -- the source's experiments do not cover an end-to-end binary Goppa instance. And that the source's Remark 6.3 one-sided variant relocates the heuristic rather than removing it, so a resolution has to address one of the two directions.

