# Provenance: Statistically Secure Robust Additive Randomized Encodings

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Additive Randomized Encodings and Their Applications**
- Authors: Shai Halevi, Yuval Ishai, Eyal Kushilevitz, Tal Rabin
- Venue/archive: IACR ePrint 2023
- Identifier: IACR ePrint 2023/870
- Bibliographic detail: inferred
- File: `2023-870.pdf` (46 pages)
- sha256: `21c631e4df19ce8dd6d039a01684e3e87e94d26da4d8c28b9fc20d4f722914ca`
- Read on 2026-08-27T18:30:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The source asks whether all functions admit a statistically secure ARE, robust or non-robust, and strongly conjectures the answer is negative. The non-robust half was subsequently refuted by Bitansky, Erabelli, Garg and Ishai, who construct statistical AREs for all finite functions. The robust half is open and is re-posed by that later work.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 7 | 7 | exact (100%) | The main open question is whether all functions admit a statistically secure (robust or non-robust) ARE. |
| openness | 5 | 5 | exact (100%) | We leave open the exis- tence of statistically secure ARE for general (or even constant-size) functions, and describe a failed attempt in this direction in Appe... |
| progress | 7 | 7 | exact (100%) | We strongly conjecture that the answer is negative. However, we were not able to prove this conjecture |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question is verbatim in Section 1.2, but half of it has since been settled -- against the source's own strong conjecture -- by a paper harvested into this archive two batches earlier. The statement is therefore restricted to the robust notion, posed in the achievability direction, with the refutation recorded in three places so a reader cannot miss it.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 7 | Section 1.2 states the main open question covering robust and non-robust statistical ARE, and page 5 records that the source leaves open the existence of statistically secure ARE for general or even constant-size functions. |
| openness | fail | 7 | Openness fails for half of the question as posed. The non-robust case is resolved affirmatively by Bitansky-Erabelli-Garg-Ishai (2025/1442), read in full during the Conjura harvest that produced c/0073: every finite function has a statistical ARE, which refutes the source's strong conjecture and settles the equality-over-{0,1,2} case it singled out. Repaired by restricting the statement to the robust notion, stating the refutation explicitly in the status line, the setting and a dedicated remark, and posing it as achievability rather than as the source's negative prediction. |
| strength | fail | 5 | Strength: the source's own prediction is negative; a draft that stated the conjecture in the source's direction would be asserting the opposite of what the surviving evidence suggests, since the one half that has been tested went the other way. Repaired by stating the achievability form and saying whose direction it is. |
| quantifiers-and-parameters | pass | 11 | Definition 3.4's quantifiers reproduced: for all lambda, n, l, all H subset [n] and all honest inputs x, statistical distance at most delta between the oracle-aided simulator and Pi_H. |
| attribution | pass | 10 | Robust ARE is the harvested paper's own notion; the MPRE and best-possible-MPC consequences are attributed to ABT21 and HIKR18 as the later work does. |
| definitions | pass | 11 | The residual function f_{H,x} is defined as the source defines it, and the reason robustness must concede it is the source's own argument. |
| fabrication | pass | - | No fabrication. The obfuscation implication for general functions over large domains is the source's own result, which is why the statement is restricted to finite f. |
| self-containment | pass | - | Self-contained from Definitions 3.1, 3.3 and 3.4. |

### Corrections the checker asked for

- **formal_statement_latex** — The source's question covers robust and non-robust together, and the non-robust half is now resolved.
  - suggested: Restrict the statement to statistically robust ARE for finite functions, and record the refutation of the non-robust half in the status line, the setting and a remark.
- **status_note** — Must not read as though the source's strong conjecture still stands.
  - suggested: Say that the non-robust half was refuted and that the robust half is what remains, naming the later work.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

Above all, that the non-robust half is no longer open and must not be published as though it were. Also that finiteness is essential -- robust ARE for general functions over large domains implies obfuscation -- and that the statement is posed as achievability rather than as the source's negative prediction, deliberately.

