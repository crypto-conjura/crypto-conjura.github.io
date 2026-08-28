# Provenance: A CPA-Secure Encryption Scheme That Only a Quantum Attacker Breaks

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Post-Quantum Insecurity from LWE**
- Authors: Alex Lombardi, Ethan Mook, Willy Quach, Daniel Wichs
- Venue/archive: IACR ePrint / TCC 2022
- Identifier: IACR ePrint 2022/869
- Bibliographic detail: printed-in-source-bibliography
- File: `2022-869.pdf` (36 pages)
- sha256: `2650ae9aba4c3a0325f70e7850d32ab03229f8afb81d01643ad030749ee03373`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The first item in the source's Open Problems section. The source builds such counterexamples for PRFs, CPA-secure symmetric-key encryption, MACs, signatures and CCA-2-secure public-key encryption, all under LWE with black-box classical security proofs, and states why the CPA public-key case is not among them.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 12 | 12 | exact (100%) | Can we construct a CPA-secure public-key encryption scheme which is classically secure under LWE but post-quantum insecure? |
| openness | 12 | 12 | exact (100%) | We mention several fascinating open problems left by our work. |
| obstruction | 12 | 12 | exact (100%) | The CPA security game for public-key encryption consists of 3 rounds, so it may seem like we should be able to embed a QDS scheme inside it. But the 3rd round o... |
| route-qds | 12 | 12 | exact (100%) | Can we construct a 3-message stateless/resettable QDS under LWE? This would allow us to construct cryptosystems that are classically secure in the standard sens... |
| route-ipq | 12 | 12 | exact (100%) | Can we construct 3-message (resettably secure) IPQs from LWE? |
| what-is-proved | 1 | 1 | exact (100%) | Concretely, our work provides (contrived) constructions of pseudorandom functions, CPA-secure symmetric-key encryption, message-authentication codes, signatures... |
| cca | 4 | 4 | exact (100%) | A public-key encryption scheme that is classically CCA-2 secure in the standard sense, but is broken by a quantum adversary making 2 decryption queries before s... |
| why | 6 | 6 | exact (100%) | Such counterexamples are extremely important and serve as a warning that can hopefully prevent us from making such mistakes in the future. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

All eight quotes ground exact; two claimed pages were corrected by the grounder, the results list on PDF page 4 rather than printed page 2 and the counterexamples remark on PDF page 6 rather than printed page 3, the difference being the front matter offset. The correction on strength is that the source asks a question and the page states an existential proposition; that step is flagged in its own remark, with the note that the negative answer settles the problem too. The obstruction is quoted verbatim rather than paraphrased, since it is the whole reason the problem is attackable. Attribution checked: the four-message IPQ from LWE is Brakerski-Christiano-Mahadev-Vazirani-Vidick and the compiler is Kalai-Lombardi-Vaikuntanathan-Yang, both cited as such, and only the three-message QDS is the source's own. A forward literature check on 28 August 2026 found no construction of a CPA-secure public-key counterexample.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

Three. First, the source poses this as a question and the existential proposition on the page is this statement's step; a proof that no such scheme exists settles the question equally and would be the stronger result. Second, the schemes in this line are deliberately contrived and nothing here is evidence about LWE itself or about any deployed scheme -- the content is about what a classical black-box proof buys. Third, do not read the two neighbouring open problems as equivalent to this one: a three-message stateless QDS and a three-message IPQ from LWE are sufficient routes the source names, not restatements.

