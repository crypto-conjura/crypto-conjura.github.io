# Provenance: Somewhere Statistically Sound Arguments Are Fiat-Shamir Friendly

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Somewhere Statistical Soundness, Post-Quantum Security, and SNARGs**
- Authors: Yael Tauman Kalai, Vinod Vaikuntanathan, Rachel Yun Zhang
- Venue/archive: IACR ePrint 2021
- Identifier: IACR ePrint 2021/788
- Bibliographic detail: inferred
- File: `2021-788.pdf` (43 pages)
- sha256: `5c3bb2d12ec99919f18fe04066f6e374a4cc2c110ff44159dc2d09d8aa3a65e0`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Conjecture 1.3 of the source. It is explicit that it does not prove it, and asks for 'the proof (or refutation) of this conjecture' as an important open problem. It does prove that SSS implies straight-line soundness and hence post-quantum soundness, and that its own instantiation of Kilian's protocol is SSS.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 8 | 8 | exact (100%) | Conjecture 1.3. Any constant round SSS interactive argument (P, V) is Fiat-Shamir friendly. |
| openness | 6 | 6 | exact (100%) | We emphasize that we do not prove that any SSS interactive argument is Fiat-Shamir friendly, only conjecture it. |
| openness2 | 9 | 9 | exact (100%) | we conjecture that this instantiation is Fiat-Shamir friendly, and leave the proof (or refutation) of this conjecture as an important open problem. |
| definition | 6 | 6 | exact (100%) | meaning that for any SSS interactive argument (P, V) there exists a hash family H such that applying the Fiat-Shamir paradigm w.r.t. H to (P, V) results with a  |
| evidence | 8 | 8 | exact (100%) | We note that all known negative results for the Fiat-Shamir paradigm |
| evidence2 | 6 | 6 | exact (100%) | prior to this work, the only interactive argument that was proven to be Fiat-Shamir friendly, in the work of Canetti et al. |
| subgoal | 6 | 6 | exact (100%) | we propose constructing an SSS interactive argument for all of NP as a great open problem. |
| theorem | 22 | 22 | exact (100%) | Any θ-SSS interactive argument (P, V) w.r.t. a θ-decisional complexity assumption A is θ-straight-line sound. |

## Adversarial check

**Verdict: faithful** (confidence: high)

Conjecture 1.3 is verbatim on page 8 and the definition of Fiat-Shamir friendliness is quoted from the informal exposition on page 6. No repair was needed. One page correction: the 'proof (or refutation)' openness quote is on page 9, not page 7 as first recorded. The statement flags that the definition is existential in the hash family, since a reader could otherwise take the conjecture to be about Fiat-Shamir as deployed, which it is not.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
