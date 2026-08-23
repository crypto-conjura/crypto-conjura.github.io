# Provenance: A Safe Two-Scheme Key Cycle for Every Encryption Scheme

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

`explicitly-conjectured`. Printed as `Conjecture 2' in the source's concluding Section 6 (p. 20), immediately after the sentence saying that the known separation results do not rule it out. Open in both directions.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 20 | 20 | exact (100%) | Conjecture 2: For any (public key) encryption scheme Enc there is a (possibly different) encryption scheme Enc′ such that Enc(pk, ·) is secure in the presence o... |
| openness | 20 | 20 | exact (100%) | However, this is different from computing a simple cycle Encpk (sk) directly, because the evaluated ciphertext follows a different distribution. So, it is not r... |
| context | 19 | 19 | exact (100%) | However, for the purpose of applying (a generalization of) Theorem 6 it is not necessary to use the same encryption scheme at every step of the cycle. |
| context | 19 | 19 | exact (100%) | Note that the new (existentially quantified) scheme Enc′ is not required to be homomorphic. |
| context | 20 | 20 | exact (100%) | Still, proving that the conjecture is true would provide interesting information about the feasibility of achieving circular security in a generic way. |
| context | 19 | 19 | exact (100%) | Previous results have shown how to build encryption schemes Enc such that publishing such a cycle is insecure. So, one cannot achieve full composability generic... |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is printed verbatim and left open, and the source explains precisely why the existing separations do not apply. Two gaps in the printed statement had to be closed to make it non-vacuous -- validity of the partner scheme and IND-CPA security of the starting scheme -- and both are recorded as the draft's own additions rather than presented as the source's.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 20 | Printed as a displayed, labelled conjecture. |
| openness | pass | 20 | Posed in the last section; the following paragraph discusses variants and consequences but settles nothing. Nothing after p. 20 but references. |
| strength | pass | 20 | Stated at the source's strength: the 2-cycle public-key form only. The source's listed variants (longer cycles, private-key Enc', bitwise encryption) are named in the draft's setting and explicitly excluded from the statement. |
| quantifiers | corrected | 20 | The for-all/exists shape is the point of the conjecture and is preserved. Two implicit hypotheses were made explicit: validity of Enc' and IND-CPA security of Enc. Without the first the statement is vacuous, see the draft's Remark 1. |
| attribution | pass | 20 | The paper's own conjecture. The separations it says do not apply are attributed in the draft to KRW15, KW16, AP16, GKW17a, GKW17b, HK17, exactly the keys the source cites at that point. |
| definitions | pass | 5 | Encryption scheme, validity and IND-CPA are the source's Definitions 1 and 2. The key encodings psi, psi' are named by the draft because the source writes Enc'_{pk'}(sk) with the encoding implicit; that is a renaming, not a redefinition. |
| fabrication | pass | 20 | The claims about what a proof would and would not give are quoted from the source's own paragraph, including the caveat that the conjecture does not by itself imply composable FHE. |
| self-containment | pass | - | Definitions 1-3 plus Conjecture 2 of the draft are enough to know what to prove. |

### Corrections the checker asked for

- **formal_statement_latex** — A degenerate Enc' whose ciphertexts do not depend on the message satisfies the printed statement without forming a cycle at all.
  - suggested: Require Enc' to be valid, i.e. perfectly correct, and say in a remark that the source leaves this implicit.
- **formal_statement_latex** — The printed statement quantifies over any encryption scheme Enc, including insecure ones, for which the conclusion is false.
  - suggested: Restrict to IND-CPA secure Enc and flag the restriction.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

As literally printed the conjecture is trivially true, because the source's Definition 1 does not require an `encryption scheme' to be correct: a scheme whose ciphertexts are independent of the message satisfies it vacuously. The draft's Remark 1 says so and requires validity. Also, the printed statement puts no security hypothesis on Enc, without which the conclusion fails trivially; the draft adds IND-CPA security of Enc and flags the addition.

