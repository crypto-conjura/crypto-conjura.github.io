# Provenance: Degree-2 Statistical Randomized Encodings for Every Finite Function

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Separating Two-Round Secure Computation from Oblivious Transfer**
- Authors: Benny Applebaum, Zvika Brakerski, Sanjam Garg, Yuval Ishai, Akshayaram Srinivasan
- Venue/archive: IACR ePrint 2020
- Identifier: IACR ePrint 2020/116
- Bibliographic detail: inferred
- File: `2020-116.pdf` (43 pages)
- sha256: `f61c664a364c33da0575f1ae2f00ac3d92be4be0acf4cb13c9ab5ba5b4f24753`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-asks-question`. Question 1.6 of the harvested paper, attributed there to Ishai-Kushilevitz and Applebaum-Ishai-Kushilevitz and described as open for almost 20 years. Degree-3 encodings exist for every finite function; negative results are known for perfectly private degree 2. The harvested paper adds a new consequence, its Proposition 1.7.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 6 | 6 | exact (100%) | While some negative results are known for perfectly private degree-2 RE [IK00], the feasibility of statistically private degree-2 RE (that are allowed to have a... |
| openness | 6 | 6 | exact (100%) | We relate this longstanding open problem to the completeness of 3-party functionalities under RPBB reductions. |
| progress | 6 | 6 | exact (100%) | A positive answer to Question 1.6 would imply that Theorem 1.5 holds with |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is numbered and verbatim, stays open through the paper's own open-problems list, and comes with a new consequence the harvested paper proves. The one correction is attribution: the question predates this paper by twenty years and the statement says so in three places.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 6 | Question 1.6 is printed as a numbered question on page 6, with the surrounding paragraph saying the statistical case has remained open for almost 20 years. |
| openness | pass | 10 | Stays open: the harvested paper's own open-problems list twice says a negative answer to Question 1.6 would be required to extend its results, so it plainly does not settle it. |
| strength | pass | 6 | Strength matches: 'Does every finite function admit a degree-2 statistical randomized encoding?' is the statement, with perfect correctness and statistical privacy, which is the standard reading the paper's own contrast with perfect privacy fixes. |
| quantifiers-and-parameters | pass | 6 | Quantifiers: degree is total degree in (x, r) jointly, not in x alone -- the distinction that makes degree 3 classical and degree 2 hard. |
| attribution | fail | 6 | Attribution: the question is not the harvested paper's. It is attributed there to [IK00, AIK04]. Recorded by naming both in the conjecture's own header, in the status line, and in a dedicated remark, and by saying that what the harvested paper adds is Proposition 1.7. |
| definitions | pass | 5 | (d,p)-MULTPlus and strict RPBB reductions are used as the paper defines them, and Theorem 1.5's statement is transcribed rather than paraphrased. |
| fabrication | pass | - | No fabrication. The incomparability of degree-2 RE and ARE is the companion paper's own observation, quoted rather than inferred. |
| self-containment | pass | - | Self-contained from the randomized-encoding definition and the degree measure. |

### Corrections the checker asked for

- **status_note** — Must not present a cited question as the harvested paper's own.
  - suggested: State in the status line, the conjecture header and a remark that the question is Question 1.6 there, attributed to IK00 and AIK04, and that the harvested paper's contribution is Proposition 1.7 and the two barrier observations.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

Attribution above all: the question is not the harvested paper's own, and the statement must say so. Also that perfect-privacy negative results do not settle it, and that the ARE question of the companion paper is incomparable rather than equivalent.

