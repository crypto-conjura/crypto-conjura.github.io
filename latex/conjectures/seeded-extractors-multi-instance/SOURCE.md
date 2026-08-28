# Provenance: Is Every Seeded Extractor a Multi-Instance Extractor?

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Multi-Instance Randomness Extraction and Security against Bounded-Storage Mass Surveillance**
- Authors: Jiaxin Guan, Daniel Wichs, Mark Zhandry
- Venue/archive: IACR ePrint / TCC 2023
- Identifier: IACR ePrint 2023/409
- Bibliographic detail: printed-in-source-bibliography
- File: `2023-409.pdf` (48 pages)
- sha256: `1f2d3a0583bfa63b56f98e88452c3f1adb9aa6941bf38003a5a245938eccb4c0`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The source poses the question with both answers live and proves the property for two specific code-based extractors (Hadamard, and Reed-Muller composed with Hadamard) via a property it isolates and calls hinting. Concurrent independent work of Dinur, Stemmer, Woodruff and Zhou proves it for universal hash functions by a different argument. No extractor is known to fail it, and no general proof is known.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | It remains as a fascinating open problem whether every standard seeded extractor is also a multi-instance randomness extractor or if there is some counterexampl... |
| openness | 7 | 7 | exact (100%) | A natural approach would be to try to show that every standard seeded extractor is also a “multi-instance randomness extractor”. |
| obstruction | 7 | 7 | exact (100%) | Unfortunately, this prevents us for using the block-entropy lemma to analyze multi-instance extraction, where the adversary sees some extracted outputs from all... |
| failed-attempt | 7 | 7 | exact (100%) | We were initially convinced that the general result does hold and invested much effort trying to prove it via some variant of the above approach without success... |
| definition | 15 | 15 | exact (100%) | is (t, α, β, ε)-multi-instance extracting if the following holds. |
| concurrent | 6 | 6 | exact (100%) | They study this problem in a completely different context of differential-privacy lower bounds. They show that (in our language) universal hash functions are “m... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open problem is quoted verbatim and grounds exact on page 7, as do the obstruction and the footnote recording the failed attempt. The correction the check forced is on strength: the source states the question with no parameters, so the quantitative conjecture on the page is flagged as this statement's reading and two weaker readings are named beside it, rather than presented as the source's. Definition 3.1 is transcribed from the source verbatim in substance. Attribution is separated: the universal-hash result is concurrent independent work of Dinur, Stemmer, Woodruff and Zhou, not the source's, and the page says so. A forward literature check on 28 August 2026 found no resolution and no counterexample.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

The quantitative form of the conjecture is this statement's reading, not the source's: the source asks the question qualitatively and attaches no parameters to it. Three readings are separated on the page -- a uniform loss function, some beta = alpha - o(1) per extractor, and the purely qualitative form -- and a proof should say which it establishes. A counterexample settles all three and is the outcome the source's own phrasing keeps open. Note also that the definition quantifies over a random variable I_X chosen after the source, which is not optional: the source's own example (one uniformly chosen block set to zero) shows no fixed coordinate can be claimed uniform.

