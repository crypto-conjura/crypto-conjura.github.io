# Provenance: Is XOR a Weak 2-Immunizer for Backdoored Generators?

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Immunizing Backdoored PRGs**
- Authors: Marshall Ball, Yevgeniy Dodis, Eli Goldin
- Venue/archive: IACR ePrint 2023
- Identifier: IACR ePrint 2023/1778
- Bibliographic detail: printed-in-source-bibliography
- File: `2023-1778.pdf` (41 pages)
- sha256: `40dc8a9d2cff3f2e41144f2fddd1998b95fc47701ab6c6712cdde989891bb26a`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. The single unresolved entry in the source's own table. XOR is proved not to be a strong 2-immunizer under the Alekhnovich assumption; a bilinear pairing is proved not to be a weak one under SXDH; a random oracle is proved to be a secure 2-immunizer even in the auxiliary-input ROM. The weak case for XOR is left open, and the source says it conjectures the counterexample exists.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 8 | 8 | exact (100%) | The only exception is the explicit counter-example to the insecurity of XOR as a weak 2-immunizer, which we leave open (but conjecture to be true). |
| openness | 13 | 13 | exact (100%) | Note that there is no simple way to adapt the public key encryption scheme used to prove this theorem to be sufficiently homomorphic to prove that XOR is not a ... |
| route | 17 | 17 | exact (100%) | We remark that the Alekhnovich PKE is not jointly ⊕-homomorphic with itself. We leave it as an open question as to whether such a pair of encryption schemes exi... |
| sufficient | 17 | 17 | exact (100%) | If there exists (Gen, Enc, Dec), (Gen′ , Enc′ , Dec′ ) pseudorandom and jointly ⊕- homomorphic, then ⊕ is not a (poly(λ), 1, negl(λ), negl(λ))-secure weak 2-imm... |
| pairing | 8 | 8 | exact (100%) | As partial evidence, we show that the pairing operation (which looks similar to XOR) is not a weak 2-immunizer under a widely believed SXDH assumption in pairin... |
| separation | 8 | 8 | exact (100%) | While we know such C cannot be “highly dependent on both inputs”, which rules out most natural choices one would consider (including cryptographic hash function... |
| other-question | 8 | 8 | exact (100%) | Is there a 2-immunizer C in the standard model whose security can be black-box reduced to an efficiently falsifiable assumption? |

## Adversarial check

**Verdict: faithful** (confidence: high)

All seven quotes ground exact on the pages claimed. Existence and openness are unambiguous, stated twice by the source in its own voice, with a direction (it conjectures the counterexample exists). Strength: the parameter tuple in the conjecture is the source's own, taken from Corollary 3.13 and matching Theorem 3.1, so it is not this statement's choice. The check separated three things a faithful-looking draft could easily merge: the strong-case result (proved, different notion), the pairing result (proved, weak notion, different operation), and the black-box separation (about provability, not about whether XOR works). The other open question the source calls fascinating -- a standard-model 2-immunizer with a black-box reduction to a falsifiable assumption -- is recorded as a separate question and deliberately not merged into the statement. A forward literature check on 28 August 2026 found no follow-up settling it.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

Two confusions to avoid. First, strong versus weak: the implication runs from strong security to weak security, so the source's counterexample to the strong case says nothing here, and the reason is concrete -- Alekhnovich's scheme is XOR-homomorphic with itself under one key but not jointly XOR-homomorphic with itself under two independent keys. Second, Corollary 3.13 is a sufficient condition only; nothing in the source says a counterexample has to come from a jointly homomorphic pair, so a proof that no such pair exists would not refute the conjecture. The source's black-box separation likewise does not settle it in either direction: it rules out a black-box proof from a falsifiable assumption that XOR is an immunizer, not the fact.

