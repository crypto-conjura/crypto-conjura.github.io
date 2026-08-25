# Provenance: Polylogarithmic Single-Server Shuffle PIR with Negligible Security Error

Written by `scripts/harvest_conjectures.py`. Nothing here was checked
by a human yet; this file is what the run believed and why.

## Source

- Paper: **Information-Theoretic Single-Server PIR in the Shuffle Model**
- Authors: Yuval Ishai, Mahimna Kelkar, Daniel Lee, Yiping Ma
- Venue/archive: IACR ePrint 2024
- Identifier: IACR ePrint 2024/930
- Bibliographic detail: inferred
- File: `2024-930.pdf` (48 pages)
- sha256: `a64775d98d42c85247cc0f14389faf0dae6dc43c6352dca3b547123de469d9d7`
- Read on 2026-08-25T16:00:00Z via the `claude-code-session (harvest_model backends unavailable on this machine: no anthropic SDK, no ANTHROPIC_API_KEY, no claude CLI on PATH; extraction, adversarial re-check and typesetting were done by the authoring Claude Code session reading the PDF directly. Quote grounding, pdflatex/chktex/lacheck and this file are harvest_conjectures.py's own code.)` backend

## How the paper leaves it open

`paper-conjectures`. Settled in three neighbouring corners: O(n^gamma) communication with inverse-polynomial error and polynomially many queries; polylogarithmic communication with n^{O(log n)} queries; negligible error with O(n/log n) communication. The polylogarithmic-and-negligible corner with polynomially many queries is open, and is ruled out for inner-outer constructions with an additive inner layer by the source's Theorem 6.5.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 30 | 30 | exact (100%) | We conjecture that polylogarithmic communication per client with negligible security can be achieved by instantiating both OPIR and IPIR with the Reed-Muller PI... |
| openness | 30 | 30 | exact (100%) | The main technical question we leave open in this work is the possibility of obtaining similar results with negligible security error |
| openness | 3 | 3 | exact (100%) | We also discuss open problems (Section 7) on whether negligible security is possible (with polynomially many clients) by using other protocols in the inner laye... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The question and the conjecture are both verbatim in Section 7, and the polynomial-client framing is verbatim on page 3. Two corrections were needed: the statement had to be posed as the existence claim rather than the named instantiation, and the client bound had to be quantified.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 30 | Section 7 states the main open question and the conjecture explicitly. |
| openness | pass | 30 | Stays open: the conjecture is in the paper's final section, after all results, and Theorem 6.5 is a barrier rather than a resolution. |
| strength | fail | 30 | The paper's conjecture names a construction (Reed-Muller in both layers); the draft states the existence claim instead. Repaired by stating the existence claim, which is the open question posed on page 3, and recording the authors' route as a remark labelled as strictly stronger. |
| quantifiers-and-parameters | fail | 3 | The conjecture sentence does not bound the number of clients. The polynomial bound comes from page 3's framing of the open problem. Repaired by quantifying C as polynomial in the statement and quoting page 3 for it. |
| attribution | pass | 30 | The conjecture is the harvested paper's own, not cited from elsewhere. |
| definitions | pass | 15 | Definition 5.1 is reproduced with its own quantifiers, including the C* >= C(n) quantifier that is easy to lose. |
| fabrication | pass | - | No claim attributed to the paper that it does not make. Theorem 6.5's hypotheses (constant-server additive inner PIR, polynomially bounded client and sub-query-vector counts) are stated in full rather than summarized as 'additive'. |
| self-containment | pass | - | Definition 5.1 plus the statement is enough to know what to build. |

### Corrections the checker asked for

- **formal_statement_latex** — Conflated the paper's conjecture (a named instantiation) with its open question (existence).
  - suggested: Make the conjecture the existence claim; add a remark quoting the Reed-Muller sentence and saying that establishing it via that instantiation is strictly stronger.
- **formal_statement_latex** — Client count unquantified.
  - suggested: Require C polynomial, and cite page 3 ('with polynomially many clients') as the source for that clause.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

That the conjecture is stated at the paper's strength. The paper conjectures a specific instantiation (Reed-Muller in both layers); the drafted statement is the existence claim its introduction poses, with the instantiation recorded as the authors' conjectured route in a remark. Also that the polynomial client bound comes from the introduction, not from the conjecture sentence.

