# Provenance: A Subexponential-Query PCF from Sparse LPN

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Fast Pseudorandom Correlation Functions from Sparse LPN**
- Authors: Lennart Braun, Geoffroy Couteau, Kelsey Melissaris, Mahshid Riahinia, Elahe Sadeghi
- Venue/archive: IACR ePrint; ASIACRYPT 2025
- Identifier: ePrint 2025/1644
- Bibliographic detail: printed-on-page
- File: `2025-1644.pdf` (38 pages)
- sha256: `a6d41228a29cec5c92a2784ef8c0d3e13a0be1977ea08dfbbee4ea97fe272042`
- Read on 2026-08-23T11:45:14Z via the `none (in-session; no CLI binary, no SDK, no credentials)` backend

## How the paper leaves it open

`paper-asks-question`. Open in both directions. The source poses it as the first of its two open questions and takes no position; the affirmative direction stated here is the page's own reading. The source's own construction is secure against subexponential-time adversaries for up to n^(log n / log log n) queries.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 10 | 10 | exact (100%) | Is it possible to build a PCF with fully-subexponential security (in runtime and queries) from sparse LPN? |
| openness | 10 | 10 | exact (100%) | Our PCF only achieves subexponential security up to superpolynomially-many queries, a lower asymptotic security level compared to previous candidates. |
| openness | 10 | 10 | exact (100%) | Open Questions. We mention two interesting open questions: |
| progress | 5 | 5 | exact (100%) | Compared with previous constructions from VDLPN, EALPN, DCR, or QR, our PCF comes with a theoretical limitation: while previous constructions were plausibly sec... |
| parameter | 16 | 16 | exact (100%) | these parameters achieve security with inverse-superpolynomial advantage against subexponential-time adversaries making at most superpolynomially-many queries t... |
| parameter | 16 | 16 | exact (100%) | evaluation must run in polynomial time |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

The question is printed verbatim in a section titled 'Open Questions' on p. 10 and is not answered anywhere in the paper, whose last section is 4.5 and which contains no theorem about query bounds beyond Theorem 1's a-priori-fixed ones. Two corrections were forced on the first draft: it pinned the sparsity to polylog(n), which strengthens the statement beyond the question asked, and it left the advantage requirement unflagged where the source's phrase constrains only runtime and queries.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 10 | Printed verbatim under 'Open Questions. We mention two interesting open questions:' as item (1). |
| openness | pass | 10 | The paper's last section is 4.5 (pp. 30-32), there is no conclusion after it, and no lemma, claim or theorem addresses the query regime beyond Theorem 1, whose bounds QA, QB, QO are fixed a priori. Checked the full list of numbered results (Theorem 1, Lemmas 2-6, Claims 1-2, Definitions 1-10). |
| strength | fail | 6 | The first draft required k = polylog(n), which the question does not: Definition 5 allows any k in [3, n], and the polylog choice belongs to the source's conservative flavour of the assumption (Section 1.4, p. 6). Corrected. |
| quantifiers-and-parameters | unclear | 10 | 'Fully-subexponential security (in runtime and queries)' does not say what the advantage must be, and the source's own result has inverse-superpolynomial advantage (p. 16). The statement asks for one exponent to serve size, queries and advantage, and the remark now records the weaker reading explicitly. |
| attribution | pass | 10 | The source's own open question about its own construction, not a question it attributes to anyone else. |
| definitions | pass | 13 | PCF is the source's Definition 9 (after Boyle et al.), sparse LPN its Definition 5 (p. 11), subfield VOLE its Definition 10 (p. 13). All three are reproduced from the source rather than replaced by standard variants. |
| fabrication | fail | 16 | The first draft quoted the parameter constraint as 'we require k L = poly(n)', which is the text layer's rendering of $k^L$; that would print a typo on the page as if it were the source's. Replaced by the prose fragment 'evaluation must run in polynomial time' plus the exponent set in mathematics. |
| self-containment | pass | - | The statement is readable from the page's own Definitions 5 and 9 and the notation list; no symbol is used undefined and no defined symbol is unused. |

### Corrections the checker asked for

- **formal_statement_latex** — Pinned the sparsity to polylog(n), strengthening the statement past the question asked.
  - suggested: Quantify k only over Definition 5's range 3 <= k <= n, and record the polylog reading in a remark.
- **setting_latex** — Quoted 'we require k L = poly(n)', a text-layer artefact for $k^L$.
  - suggested: Quote only 'evaluation must run in polynomial time' and set the exponent in mathematics.
- **risks** — The advantage requirement was stated without flagging that the source's phrase does not constrain it.
  - suggested: Added the second remark naming both readings, and the weaker one the statement implies.

## Citations that could not be verified

These were not read off the harvested paper's own reference list.
Do not remove the `[UNVERIFIED]` markers in `statement.tex` until
each has been checked against the actual paper.

- `HR25` — Sebastian Hasler, Pascal Reisert, *Pseudorandom Correlation Functions for Multiparty Beaver Triples from Sparse LPN*, IACR ePrint 2025/2002 2025

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The source names no obstruction at all, which is the weakest point: the page supplies the parameter tension (evaluation cost k^L against stretch m^(L)) from the source's printed constraints rather than from any claim the source makes about difficulty. Also check the two readings recorded in the second remark: whether the advantage should be subexponentially small (the source's phrase constrains only runtime and queries) and whether the sparsity should be pinned to polylog(n).

