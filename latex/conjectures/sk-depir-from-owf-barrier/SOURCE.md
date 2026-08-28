# Provenance: No Black-Box Secret-Key Doubly Efficient PIR from One-Way Functions

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Black Box Crypto is Useless for Doubly Efficient PIR**
- Authors: Wei-Kai Lin, Ethan Mook, Daniel Wichs
- Venue/archive: IACR ePrint / EUROCRYPT 2025
- Identifier: IACR ePrint 2025/552
- Bibliographic detail: printed-in-source-bibliography
- File: `2025-552.pdf` (29 pages)
- sha256: `b8ef63fb8b1783ef9212f431901c8782e4880e9a0e69c203e71736ce1520cb2e`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. The source states this as its own conjecture and proves the special case of two-round passive-server SK-DEPIR. Its main theorem, that any crypto oracle can be stripped out of a SK-DEPIR and replaced by a one-way function, is stated conditionally on the conjecture, so the conjecture is the single remaining hypothesis between that compiler and a clean statement that no idealized generic primitive helps.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 4 | 4 | exact (100%) | We conjecture that there is no black-box construction of SK-DEPIR from just one-way functions. While we do not know how to prove this conjecture in its full gen... |
| openness | 4 | 4 | exact (100%) | While we do not know how to prove this conjecture in its full generality, we do prove it for the special case of 2-round passive-server SK-DEPIR. |
| conditional | 5 | 5 | exact (100%) | Under the conjecture that there is no black-box construction of SK-DEPIR from just one-way functions, this implies that there is no black-box construction of SK... |
| interpretation | 5 | 5 | exact (100%) | The main interpretation of our result is that DEPIR requires concrete hardness assumptions about real-world problems (e.g., hardness of Ring LWE), which cannot ... |
| context | 4 | 4 | exact (100%) | It remains a fascinating open problem to construct any flavor of DPEIR under any standard assumption beyond RingLWE, such as standard LWE, DDH (in bilinear maps... |
| converse | 4 | 4 | exact (100%) | Conversely, we do not know of any standard cryptographic primitives that would generically imply any flavor of DEPIR. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The conjecture is printed in the source in exactly this form and quoted verbatim on the page, so nothing about its strength is this statement's choice. All six quotes ground exact on the pages claimed. Existence, openness, strength, attribution and definitions all check: the source states the conjecture in its own voice, proves only the two-round passive-server case, and the definition of SK-DEPIR used here is the source's Definition 2.1 including its deliberate weakenings. The two neighbouring open questions the source poses -- constructing any DEPIR beyond Ring-LWE, and finding a standard primitive that implies DEPIR -- are recorded as separate questions and are not merged into the statement. A forward literature check on 28 August 2026 found no resolution; the closest follow-up, Black-Box Crypto is Useless for Pseudorandom Codes (arXiv 2506.01854), transplants the technique rather than settling this.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

Two things. First, the conjecture is an impossibility, so a proof and a refutation look nothing alike: a refutation is a construction of SK-DEPIR from one-way functions, which would be a major positive result and is not what the source expects. Second, the quantifier on locality matters -- the source deliberately weakens the definition (any o(N) locality, any polynomial round count, imperfect correctness) so that its negative results are as strong as possible, and a claimed proof for a more restrictive definition of SK-DEPIR settles less than the conjecture.

