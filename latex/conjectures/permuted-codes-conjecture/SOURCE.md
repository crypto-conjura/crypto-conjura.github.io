# Provenance: The General Permuted Codes Conjecture

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Improved Pseudorandom Codes from Permuted Puzzles**
- Authors: Miranda Christ, Noah Golowich, Sam Gunn, Ankur Moitra, Daniel Wichs
- Venue/archive: IACR ePrint / arXiv / STOC 2025
- Identifier: IACR ePrint 2025/2222 (arXiv:2512.08918)
- Bibliographic detail: printed-in-source-bibliography
- File: `2025-2222.pdf` (51 pages)
- sha256: `f4a4657e9243742e4c4d2014c795b448da11a0f30663ec960da1926e7e6201b1`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. A new hardness assumption, printed as Conjecture 3.1 of the source and stated in its most general form deliberately, as a target for cryptanalysis rather than as the minimum the applications need. The applications need only the Reed-Solomon and folded Reed-Solomon specialisations, which the source states separately as Conjectures 3.2 and 5.3.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 11 | 11 | exact (100%) | The permuted codes conjecture states that if C = C(λ) ⊆ Fnq is any family of linear codes with dual distance d = d(λ) = λΩ(1) and η = Ω(1) is any constant error... |
| openness | 5 | 5 | exact (100%) | We state the general form of the conjecture, since we are unable to find any counterexamples, and wish to provide a broad target for cryptanalysis. However, for... |
| necessity | 6 | 6 | exact (100%) | In fact, it turns out that all three of the randomizations (alphabet permutation, index permutation, and noise) are necessary: The permuted codes conjecture wou... |
| evidence | 1 | 1 | exact (100%) | We show that this conjecture is implied by the permuted puzzles conjecture used previously to construct doubly efficient private information retrieval. To give ... |
| statistical | 5 | 5 | exact (100%) | we show statistical evidence for the permuted codes conjecture over constant-size alphabets: A sample of O(log n) codewords are jointly statistically uniform |
| refutation | 5 | 5 | exact (100%) | We show in Theorem 4.5 that the conjecture would be false in general in this case, by taking C to be the Reed-Solomon code. |
| neighbour | 8 | 8 | exact (100%) | It remains an interesting open question to construct sub-exponentially secure pseudorandom codes from more standard assumptions than the permuted codes conjectu... |

## Adversarial check

**Verdict: faithful** (confidence: high)

Conjecture 3.1 is transcribed verbatim from the source and grounds exact on page 11, as do six further quotes (one page-5 span re-copied after the grounder flagged a line-broken hyphen). Strength: the general form is the source's own, and the two specialisations it actually uses, plus the sub-exponential strengthening it also records, are named on the page as different statements rather than merged in. Attribution is separated carefully -- the permuted puzzles conjecture is Boyle-Holmgren-Ma-Weiss and Blackwell-Wootters, the toy conjecture is Boyle-Ishai-Pass-Wootters, and only the implication between them and the Reed-Solomon refutation are the source's. The neighbouring open question about basing pseudorandom codes on LPN or LWE is recorded separately and not merged. A forward literature check on 28 August 2026 found the conjecture open and the paper at STOC 2026; no cryptanalysis of it was located.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

Three things. First, this is a candidate-hardness conjecture, and the case for publishing it as an open problem rather than treating it as an assumption the paper makes is argued explicitly on the page -- a reviewer who disagrees should disagree with that argument. Second, the sub-exponential strengthening the source also records is a different statement, and it is the one the headline application uses; a proof or refutation should say which version it addresses. Third, the general form quantifies over all linear code families of polynomial dual distance, whereas the applications need only specific codes, so a counterexample for some exotic family refutes the conjecture as stated without touching the constructions built on it.

