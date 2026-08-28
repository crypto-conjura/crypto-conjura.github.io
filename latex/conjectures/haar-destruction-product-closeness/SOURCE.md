# Provenance: One Haar-Random State Looks Like Many

Written in-session following `prompts/harvest.md`; `scripts/harvest_conjectures.py`
could not run its model stage on this machine. Nothing here was checked by a
human yet; this file is what the run believed and why.

## Source

- Paper: **Pseudorandomness with Proof of Destruction and Applications**
- Authors: Amit Behera, Zvika Brakerski, Or Sattath, Omri Shmueli
- Venue/archive: IACR ePrint / TCC 2023
- Identifier: IACR ePrint 2023/543
- Bibliographic detail: printed-in-source-bibliography
- File: `2023-543.pdf` (76 pages)
- sha256: `1758584f3023dd97a3954b23d432abd1b72748c2d3daef6b495d5143aaed35c8`
- Read on 2026-08-28T12:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and the per-conjecture harvest.json are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Stated by the source in its Open Problems section as a conjecture it believes true, with the explicit note that it could neither prove it nor find it proved or even formalised in the literature. The source proves a strictly weaker pointwise domination bound, its Lemma 2, which suffices for its own applications and says nothing about total variation distance.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. Where `found` differs from the claimed page, the claim was
wrong and the found page is what the statement cites.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 10 | 10 | exact (100%) | In some of the applications, we required the following quantum information-theoretic conjecture regarding Haar random states that we believe is true: For any al... |
| openness | 10 | 10 | exact (100%) | We could not prove nor find any previous work in the literature that proves or even formalizes this conjecture. |
| weaker | 10 | 10 | exact (100%) | We proved a different variant of it in Lemma 2, which was sufficient for the applications and might be of independent interest. |
| why | 10 | 10 | exact (100%) | We think this is an interesting open question on its own, and if proven, this result can be a useful tool for quantum cryptography. |
| gap | 18 | 18 | exact (100%) | We believe that the distributions are in fact, statistically close due to the strong concentration of the Haar measure, but we have not been able to prove it. T... |
| ancillae | 9 | 9 | exact (100%) | However, the destruct algorithms may use ancillae qubits, and therefore the overall process becomes non-unitary, even before the measurement. |

## Adversarial check

**Verdict: faithful** (confidence: high)

The conjecture is printed in the source in prose and is transcribed with the mathematics unchanged; only the names A, TV and N are this statement's, and the page says so. All six quotes ground exact, with one page claim corrected by the grounder (the ancillae remark is on page 9, not 10). Openness is unambiguous: the source says it could not prove it and could not find it formalised. Strength was checked against Lemma 2 to make sure the two are not conflated -- Lemma 2 is a pointwise ratio bound with a factor of about t factorial, not a statistical-closeness bound, and the page states the gap explicitly and quotes the source's own footnote saying so. A forward literature check on 28 August 2026 turned up no proof or refutation; the search was targeted at the pseudorandom-states line rather than exhaustive over quantum information theory, which is where a proof would most plausibly already exist.

## Build

`pdflatex` clean; `chktex -q` 0 warnings under the per-folder `.chktexrc`
(every suppression documented in that file, checked hit by hit);
`lacheck` silent.

## What to check hardest

Two things to check hardest. First, which distribution is which: the correlated one draws a single Haar state and hands out t copies of it, the product one draws t independent states, and the source's Definition 3 introduces them in the reverse order from the conjecture's own sentence, so it is easy to swap them. Second, the quantifier on A: it is every algorithm, not every efficient one, so a computational argument does not settle it, and a proof restricted to projective measurements on the input register leaves out exactly the ancillae-using case the source flags as the difficulty.

