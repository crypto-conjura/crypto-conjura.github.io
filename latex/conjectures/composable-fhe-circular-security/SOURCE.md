# Provenance: Every Fully Composable Homomorphic Encryption Scheme Yields a Circular-Secure One

Written by hand, following `prompts/harvest.md`, on 2026-08-23.
`scripts/harvest_conjectures.py` could not be used on this machine
(neither model backend was available: no `claude` CLI binary on `PATH`, no
Anthropic SDK, no API credentials, so `pick_backend()` had nothing to
return), so the extract/verify/typeset steps were carried out in-session
instead. The mechanical steps the pipeline owns were still run, from the
script itself: every quote below was grounded against the PDF's
`pdftotext -layout` text layer with `PdfDoc.ground`, the build was checked
with `compile_check` (pdflatex, chktex, lacheck), and this file was rendered
by the script's own `write_source_note`. **Nothing here has been checked by
a human.**

## Source

- Paper: **Fully Composable Homomorphic Encryption**
- Authors: Daniele Micciancio
- Venue/archive: IACR Cryptology ePrint Archive 2024/1545; IACR Communications in Cryptology 2(1) 2024 (ePrint), 2025 (CiC)
- Identifier: eprint 2024/1545
- Bibliographic detail: high -- title, author, date and section numbering read off the PDF; the CiC publication date was checked at cic.iacr.org/p/2/1/1
- File: `2024-1545.pdf` (23 pages)
- sha256: `f6091e84d0a4883ece66812ab9c17e4eeeb1ebd25ce9fd045ed5676c538efd39`
- Read on 2026-08-23T00:00:00Z via the `in-session (no model backend on this host)` backend

## How the paper leaves it open

`explicitly-conjectured`. Printed as `Conjecture 1' in the source's concluding Section 6 (p. 19), as the way to address the displayed Question `Is circular security necessary necessary to achieve full composability?'. The converse direction is the source's own Theorem 6. No partial result and no counterexample is offered for this direction.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 19 | 19 | exact (100%) | Conjecture 1: Any fully composable homomorphic encryption scheme can be modified into a circular secure one. |
| openness | 19 | 19 | exact (100%) | Question: Is circular security necessary necessary to achieve full composability? |
| openness | 19 | 19 | exact (100%) | Note that the question does not make any reference to encryption noise, and all concepts (circular security, homomorphic encryption and full composability) have... |
| context | 19 | 19 | exact (100%) | In fact, one could ask if any fully composable homomorphic encryption scheme is already circular secure, but this is most likely false as one can adapt the simp... |
| context | 19 | 19 | exact (100%) | So, the circular secure scheme of Conjecture 1 can be different from (but still depend on) the original composable FHE scheme. Given that circular security impl... |
| definition | 9 | 9 | exact (100%) | for all keys (sk, pk) ← Gen(κ), function f : Mw → M in F, and ciphertexts c ∈ C w such that Dec∗ (sk, c) ∈ Mw . |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is printed verbatim in the source and is genuinely left open there; the only real defect in a draft of it is that the source states no quantifiers, so any formal version is supplied rather than quoted. The draft therefore prints the source's sentence as Conjecture 1 and its own formalization as a separately numbered Conjecture 2, with the choices listed in a remark.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 19 | Printed as a displayed, labelled conjecture in Section 6. |
| openness | pass | 19 | Section 6 is the paper's last section before the references; the conjecture is posed there and nothing later addresses it. Read forward to the end of the paper (p. 20) to confirm. |
| strength | pass | 19 | The draft does not strengthen: it prints the sentence as-is, and its formalization asks only for existence of some circular-secure scheme, which is the weakest reading consistent with the source's own gloss that the scheme 'can be different from (but still depend on) the original'. |
| quantifiers | unclear | 19 | The source supplies none. The draft's Remark 1 lists the three choices it makes and says they are not the source's. |
| attribution | pass | 19 | The paper's own conjecture, not one it cites; the circular-security counterexamples it points to are attributed to others in the draft as well. |
| definitions | pass | 9 | Full composability is the source's Definition 6 and is reproduced clause for clause, including the quantification over all ciphertexts c with Dec*(sk,c) in M^w. psi-circular IND-CPA security is its Definition 3. |
| fabrication | pass | 19 | Every claim about the source in the draft's setting section is quoted or paraphrased from pp. 18-20. The remark that the formalization is non-vacuous only in the Impagliazzo-worlds sense is the draft's own and is marked as such. |
| self-containment | unclear | - | The printed conjecture alone is not enough to know what to prove; the draft's Conjecture 2 plus Definitions 1-5 are, under the reading it states. |

### Corrections the checker asked for

- **formal_statement_latex** — The source states no formal version, so presenting one as the source's would misattribute it.
  - suggested: Print the source's sentence as its own numbered conjecture and the formalization as a second one, with a remark naming every choice made.
- **status_note** — Calling the conjecture 'open' without saying that the converse is a theorem of the same paper understates what is known.
  - suggested: Status line records Theorem 6 as the settled direction.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The printed conjecture is one English sentence and fixes no quantifiers; the formal statement above is this page's reading and is flagged as such in Remark 1 of the draft. Three choices were made that the source does not make: that the conclusion is the existence of a circular-secure scheme rather than a property of the original; that the key encoding psi is existentially quantified; and that the constructed scheme need not be homomorphic. A reader who chooses differently is working on a different statement.

