# Provenance: Advisor-Verifier-Prover Protocols Are Lengthy

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Advisor-Verifier-Prover Games and the Hardness of Information Theoretic Cryptography**
- Authors: Benny Applebaum, Oded Nir
- Venue/archive: IACR ePrint 2023
- Identifier: IACR ePrint 2023/1378
- Bibliographic detail: inferred
- File: `2023-1378.pdf` (33 pages)
- sha256: `2967588ffa66bbbfa45824d99b58e73db57428db0d574bec23c0d5fcbaf2c06d`
- Read on 2026-08-27T21:15:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Posed as Hypothesis 1.2 and offered 'both as a working hypothesis or as an (ambitious) target for future works'. Theorem 1.3 proves it implies super-polynomial lower bounds on sd-PIR, general secret sharing and fully-decomposable randomized encodings, for none of which a super-linear lower bound is known.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | Every prover-laconic AVP protocol that works for the class of n-bit predicates must have total communication complexity that is super polynomial in n. |
| openness | 5 | 5 | exact (100%) | Hypothesis 1.2 can be used both as a working hypothesis or as an (ambitious) target for future works. |
| consequence | 4 | 4 | exact (100%) | Under Hypothesis 1.2, sd-PIR over 2n -bit database, SSS over n-bit predicates, and DRE over n-bit predicates have all communication cost that grows super-polyno |
| progress | 5 | 5 | exact (100%) | Unfortunately, we do not get the best-known lower bounds for any of the above primitives. |
| upper | 5 | 5 | exact (100%) | these connections yield a non-trivial AVP with sub-exponential communication complexity of |
| motivation | 1 | 1 | exact (100%) | A major open problem in information-theoretic cryptography is to obtain a super-polynomial lower bound for the communication complexity of basic cryptographic t |

## Adversarial check

**Verdict: faithful** (confidence: high)

Hypothesis 1.2 is verbatim on page 4 and Theorem 1.3 sits immediately below it. No repair was needed. Two things were added rather than found: the statement records the source's own $2^{tilde O(sqrt n)}$ prover-laconic AVP as the upper end of the gap, and records that the hypothesis is false without the laconicity restriction, since the source's Example 1.1 gives a non-laconic AVP at polynomial cost. Both are the source's facts, assembled here to show the statement is neither vacuous nor trivially false.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.
