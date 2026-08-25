# Provenance: The Linear-Test Bias of Multi-Disjoint Syndrome Decoding

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Computationally Secure Aggregation and Private Information Retrieval in the Shuffle Model**
- Authors: Adria Gascon, Yuval Ishai, Mahimna Kelkar, Baiyu Li, Yiping Ma, Mariana Raykova
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/870
- Bibliographic detail: inferred
- File: `2024-870.pdf` (50 pages)
- sha256: `640d1911f8bc3e2b1dc0565deea83adaaed85e3c41454d7357209c8003c7239b`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-states-open`. The source proves a non-tight reduction from standard decisional syndrome decoding, and separately conjectures that the DOOM algorithm is the best attack on MDSD; the linear-test bias is the one quantity it states it cannot bound.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 17 | 17 | exact (100%) | One plausible approach to study our conjectured hardness of MDSD is to apply the linear test framework of [BCG+ 20], by checking if there are noticable bias whe... |
| openness | 17 | 17 | exact (100%) | We do not know how to bound such bias for the MDSD distribution, and we leave it as an open question. |
| statement | 17 | 17 | exact (100%) | We conjecture that the DOOM algorithm [Sen11] is the most efficient one for breaking the MDSD problem. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The open question is verbatim in Section 3.3.1 and stays open. The one real defect is that the drafted statement fixes an exponential rate the source never names; that is repaired by existentially quantifying the constants and saying so in a remark.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 17 | The linear-test route is named in Section 3.3.1 and the paper says it does not know how to bound the bias. |
| openness | pass | 17 | Stays open: no later section, appendix or table returns to the bias. Section 8's open problems repeat that MDSD needs further study. |
| strength | fail | 17 | The source states no target bound, so the exponential rate in the drafted statement is supplied by the draft, not the paper. Recorded as a correction and flagged in a remark rather than dropped, since without a rate the statement has no content. |
| quantifiers-and-parameters | pass | 12 | MDSD's quantifiers are Definition 8 verbatim: H uniform over F^{n x m}, E uniform over the disjoint error set, both independent. |
| attribution | pass | 12 | MDSD and beMDSD are introduced by this paper, not cited from elsewhere; the linear test framework is attributed to BCG+20 as the paper does. |
| definitions | pass | 12 | Disjoint error set is Definition 7 verbatim; bias is not defined in the source, so the draft's definition is stated explicitly as its own. |
| fabrication | pass | - | Nothing in the draft is attributed to the paper that it does not contain. The DOOM optimality conjecture is quoted, not merged into the statement. |
| self-containment | pass | - | Statement is readable from Definitions 7, 8 and the draft's linear-test definition alone. |

### Corrections the checker asked for

- **formal_statement_latex** — The source names the linear-test framework and the quantity but no target bound, so any specific rate is the draft's choice.
  - suggested: State the rate as existentially quantified constants and add a remark saying the source gives no target, that the regular-LPN analogy is what fixes the natural target, and that a weaker quantitative bound would already resolve the source's question.
- **status_note** — Must not read as though the paper claims the bias is small.
  - suggested: Say the paper conjectures MDSD is hard and separately reports it cannot bound the linear-test bias.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the intended quantifier order is bias for a fixed test over the error distribution with H fixed, not bias over both. And that the disjointness of the supports, not the sparsity, is the actual obstruction -- a proof that ignores the correlation between error vectors is almost certainly wrong.

