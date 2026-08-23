# Provenance: Classical Presampling Against Quantum Queries

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

- Paper: **Unifying Presampling via Concentration Bounds**
- Authors: Siyao Guo, Qian Li, Qipeng Liu, Jiapeng Zhang
- Venue/archive: IACR Cryptology ePrint Archive 2020/1589; TCC 2021, LNCS 13042, pp. 177-208 2020 (ePrint), 2021 (TCC)
- Identifier: eprint 2020/1589
- Bibliographic detail: high -- title and authors read off the PDF; TCC 2021 volume and pages from the Springer record
- File: `2020-1589.pdf` (44 pages)
- sha256: `0b95442f8a4e0c02d7139d3ec83bb51a8fbea225ac86a17a94b0369b6762144b`
- Read on 2026-08-23T00:00:00Z via the `in-session (no model backend on this host)` backend

## How the paper leaves it open

`explicitly-conjectured-as-a-barrier`. Printed as `Conjecture 4' in the source's Section 3, `Barriers for Leveraging Presampling Techniques' (p. 17). The source's Theorem 4 shows it implies the folklore conjecture that quantum speedups need structure, so a proof is at least as hard as a central open problem in quantum computing; no refutation is known, and the source offers no evidence in either direction.

## Quotes, checked against the PDF text layer

Each was matched mechanically against `pdftotext` output after undoing
ligatures, line-broken hyphens and curly quotes. `exact` is a verbatim
hit; `near` means the span is present with a symbol mangled by the
extractor. A conjecture whose statement or openness quote failed to
ground was dropped before this file was written.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 17 | 17 | exact (100%) | Let X be distributed uniformly over [M ]N and Z := f (X), where f : [M ]N → {0, 1}S is an arbitrary function. For any P ∈ N, there exists a family {Yz }z∈{0,1}S... |
| openness | 17 | 17 | exact (100%) | we ask the question: is it possible to leverage Lemma 3 (and Theorem 3) to the quantum world ? The following conjecture formally states that the presampling tec... |
| openness | 17 | 17 | exact (100%) | In this section, we show that even requiring a much weaker bound (Conjecture 4) implies Conjecture 1, which reveals a barrier for leveraging Lemma 3 to the quan... |
| context | 18 | 18 | exact (100%) | As discussed in the last section, the natural extension of Lemma 3 does not work in the quantum world; otherwise, we can prove AA conjecture. |
| context | 15 | 15 | exact (100%) | both Conjecture 1 and Conjecture 2 are still quite open , and they are proven only for some class of functions |
| context | 5 | 5 | exact (100%) | Ideally, we would like to show a statement similar to classical presampling: AI-QROM can be reduced to BF-QROM, where the random oracle is fixed classically on ... |
| context | 5 | 5 | exact (100%) | Our first contribution points out a barrier to prove the above ideal version (with connections to AA conjecture). In light of the barrier, we present our quantu... |
| context | 17 | 17 | exact (100%) | Note that this conjecture is weaker than Section 2.5 in the sense that the dependency on S can be arbitrary, but Lemma 3 is polynomial in S. |
| context | 19 | 19 | exact (100%) | To overcome the barrier, we may need to ‘quantumly’ fix P input-output pairs and avoid the AA conjecture barrier. However, it is not clear how to ‘fix quantumly... |
| definition | 13 | 13 | exact (100%) | The following lemma was given in [CDGS18]. It shows that a random oracle distribution conditioned on advice is very close to a convex combination of P -bit-fixi... |
| definition | 13 | 13 | exact (100%) | An (N, M )-source is called P -bit-fixing if it is fixed on at most P coordinates and uniform on the rest. |

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: high)

The conjecture is transcribed from a numbered display and its status as an open barrier is stated by the source in as many words. The one thing a draft can get wrong here is tone: the paper does not claim the conjecture is true, it claims that proving it is at least as hard as the Aaronson-Ambainis programme, and the draft has to say that rather than presenting it as the authors' expectation.

| check | result | page | finding |
| --- | --- | --- | --- |
| existence | pass | 17 | Numbered Conjecture 4 in Section 3. |
| openness | pass | 18 | Section 4 opens by saying the natural extension does not work in the quantum world 'otherwise, we can prove AA conjecture', and the paper's own theorem goes to a different (quantum bit-fixing) model instead. Nothing later in the paper proves or refutes Conjecture 4. |
| strength | pass | 17 | Transcribed symbol for symbol, including h(S) . T . (log M / P)^C with T to the first power outside the C-th power. |
| quantifiers | unclear | 17 | C and h are introduced in a sentence after the display; the draft reads both as existential and gives its reason (that is what makes the conjecture weaker than the classical Lemma 3, as the source says it is) in a remark. |
| attribution | pass | 17 | The source's own conjecture. The classical Lemma 3 it weakens is attributed to Coretti-Dodis-Guo-Steinberger by the source and by the draft; the Aaronson-Ambainis conjecture is attributed to AA11. |
| definitions | pass | 13 | (N,M)-source and P-bit-fixing are the source's Definitions 7 and 8, reproduced verbatim in meaning. |
| fabrication | pass | 5 | The claim about what the ideal presampling would buy for function inversion is quoted from pp. 5-6 of the source, split at the page break rather than stitched across it, because the sentence is interrupted there by a footnote and a running head; the claim that the quantum bit-fixing model is the one later work uses is the draft's own and is supported in its Remark 3 by Liu (EUROCRYPT 2023) and by arXiv:2510.12112, both read directly. |
| self-containment | pass | - | Definition 1, Lemma 1 and Conjecture 1 of the draft are enough to know what to prove without the source. |

### Corrections the checker asked for

- **status_note** — Presenting Conjecture 4 as something the authors believe would misrepresent the paper, which states it in a section titled 'Barriers' in order to show it is hard to prove.
  - suggested: Say in the status line and the setting that the conjecture is posed as a barrier, and that the source takes no position on its truth.
- **formal_statement_latex** — The text layer of the PDF drops the absolute-value bars around the difference of probabilities.
  - suggested: Bars confirmed by rendering p. 17 of the PDF at 150 dpi and reading the display; they are present in both Lemma 3 and Conjecture 4.

## Build

- pdflatex: ok
- chktex: 0 warnings
- lacheck: 0 warnings

## What to check hardest

The source prints the quantifiers for C and h after the display rather than inside the statement, so their reading (existential, taken here) has to be inferred from the surrounding sentence that the conjecture is weaker than the classical lemma. The draft says so in a remark. Note also that the conjecture is posed as a barrier -- the paper does not assert it is true -- so a page that presented it as the authors' belief would misrepresent them. One quote used in the draft spans a page break with a footnote and a running head between its halves; it grounds at only 80% coverage as a single span, so it is quoted as two spans with their own page numbers instead.

