# Provenance: The Sponge STB Conjecture

Written by hand, following `prompts/harvest.md`, on 2026-08-23.
`scripts/harvest_conjectures.py` could not be used on this machine
(neither model backend was available: no `claude` CLI binary on `PATH`, no
Anthropic SDK, no API credentials), so the extract/verify/typeset steps were
carried out in-session instead. The two mechanical steps the pipeline owns
were still run: every quote below was grounded against the PDF's `pdftotext
-layout` text layer using `PdfDoc.ground` from `scripts/harvest_conjectures.py`
itself, and the build was checked with `pdflatex`, `chktex` and `lacheck`.
**Nothing here has been checked by a human.**

## Source

- Paper: **On Time-Space Lower Bounds for Finding Short Collisions in Sponge Hash Functions**
- Authors: Akshima, Xiaoqi Duan, Siyao Guo, Qipeng Liu
- Venue/archive: TCC 2023; IACR ePrint 2023/1444
- Identifier: IACR ePrint 2023/1444
- Bibliographic detail: printed-on-page
- File: `2023-1444.pdf` (36 pages)
- sha256: `bef55b22bc602ba742c1372664d291b5ae0800a20cdb5b13ef85f55940babf3d`
- Read on 2026-08-23 in-session (no backend)

## How the paper leaves it open

`paper-poses-and-asks-for-proof-or-refutation`. Section 1.3, "Discussions
and open problems", opens with the heading "Is STB-conjecture true for
sponge hashing?" and states the conjecture as the paper's own transport of
the Merkle-Damgård STB conjecture of Akshima–Cash–Drucker–Wee to the sponge
setting. It then says it "will be extremely interesting to either prove or
refute" it, and names *B* = 2 as the case to attack first. The paper takes
no position on which way it goes, and the sibling open problem it poses in
the next paragraph — published separately as the statement in
`../sponge-2block-ai-attack/` — would refute this one for *ST*³ > *C* if
answered affirmatively.

## Quotes, checked against the PDF text layer

Matched mechanically against `pdftotext -layout` output after undoing
ligatures, line-broken hyphens and curly quotes, using this repository's own
`ground()`. `exact` is a verbatim hit; `near` means the span is present with
a symbol mangled by the extractor.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 8 | 8 | exact (100%) | It is natural to consider a similar STB-conjecture for sponge hash functions, conjecturing the |
| statement | 8 | 8 | exact (100%) | attack by Freitag et al. [FGK22] is optimal for B |
| openness | 9 | 9 | near (93%) | It will be extremely interesting to either prove or refute the sponge STB-conjecture. To start with, is the STB-conjecture true for B = 2 in sponge? |
| partial | 8 | 8 | exact (100%) | However, this conjecture is only proved for very large B |
| partial | 4 | 4 | exact (100%) | Therefore the above bound is optimal when the S 2 T 4 /C 2 term doesn't dominate the sum, i.e., ST 3 |
| hardness | 5 | 5 | exact (100%) | As the bounds in Theorem 1, Theorem 2 and the general |
| hardness | 5 | 5 | exact (100%) | bound are the best one can prove using the multi-instance technique, other novel techniques are required to obtain optimal bounds for collision resistance of sponge in the AI setting. |
| context | 3 | 3 | exact (100%) | For other choices of B, only sub-optimal bounds are known for B |
| definition | 11 | 11 | exact (100%) | has unbounded access to F (and F −1 ), and outputs S bits of advice, denoted σ |
| definition | 11 | 11 | exact (100%) | takes σ and a challenge salt a ∈ [C] as input, makes T queries to F or F −1 , and outputs m, m′ . |
| definition | 10 | 10 | exact (100%) | Initialize (x0 , y0 ) = (0, a). |

The `near` row is the openness quote: 93% coverage with a single 93% run,
which is the "this sentence with one symbol mangled" signature rather than a
paraphrase. The two `statement` rows bracket the displayed formula
Θ(*STB*/*C* + *T*²/min(*R*,*C*)), which does not survive text extraction;
it was read from the rendered page 8 and cross-checked against Table 1
(p. 5), which lists the same quantity as the best known attack for
3 ≤ *B* ≤ *T*.

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium-high)

The conjecture is genuinely the paper's, genuinely open outside *B* ≈ *T*,
and comes with a proved obstruction (Theorem 3) rather than a bare wish. Two
defects in the first draft were repaired.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 8 | Section 1.3, p. 8, heading "Is STB-conjecture true for sponge hashing?". |
| Openness | pass | 9 | Read past section 1.3. The paper's own results are Theorem 1 (*B* = 1 bound), Theorem 2 (*B* = 2 bound) and Theorem 3 (MI-model attacks proving the technique's limits), developed in sections 3–5; none settles the conjecture. Table 1 (p. 5) leaves the 3 ≤ *B* ≤ *T* "Our Security bounds" cell empty. |
| Strength | **fail → corrected** | 4 | The first draft called *B* = 2 wholly open. The paper's own Theorem 2 settles it when *ST*³ ≤ *C*: "Therefore the above bound is optimal when the *S*²*T*⁴/*C*² term doesn't dominate the sum, i.e., *ST*³ ≤ *C*" (p. 4). Corrected: the first open case is now stated as *B* = 2 with *ST*³ > *C*. |
| Quantifiers and parameters | pass | 11 | *B* is a function of *R* and *C* rather than a constant, as the paper's Definition 3 has it — which is what makes the range *B* ≥ 3 non-vacuous. *S*, *T* follow the paper's Definition 2. Inverse queries are counted, the one structural difference from the Merkle-Damgård setting, and the statement says so. |
| Attribution | pass | 8 | The conjecture is the source paper's. The attack whose optimality it asserts is Freitag–Ghoshal–Komargodski's; the Merkle-Damgård conjecture being transported is Akshima–Cash–Drucker–Wee's; the *B* ≈ *T* bound is Coretti–Dodis–Guo's. All three are attributed on the page and again in a dedicated remark. |
| Definitions | pass | 10 | Sponge, the *B*-AICR game and the advantage reproduce section 2.3 and Definitions 2–3 clause for clause, including the initialization (*x*₀, *y*₀) = (0, *a*) and the exclusive-or into the outer part only. |
| Fabrication | **fail → corrected** | 9 | The first draft presented the conjecture without recording that the paper asks equally for a refutation, which reads as attributing a belief the authors do not state. Corrected by a remark quoting "either prove or refute" and naming the refutation route. |
| Self-containment | pass | – | Definitions 1–2 and the notation list fix the construction, the game, the resources and the asymptotic convention. |

### Unsupported by the paper, and marked as such on the page

- The Θ̃ in the conjecture. The paper prints a bare Θ for the conjectured
  quantity while every bound and attack it states carries Õ or Ω̃, including
  the attack whose optimality is being conjectured. The polylogarithmic
  reading is recorded in the remark "Θ̃ rather than Θ".
- The affirmative direction. Recorded in the remark "the source takes no
  side".

### Citations not in the source paper's reference list

None. Every work cited (`ACDW20`, `AGL22`, `CDG18`, `FGK22`) appears in the
source paper's own reference list (pp. 32–33), and `ADGL23` is the source
paper itself.

### Build warnings, not suppressed

`chktex` reports two instances of warning 38 ("You should not use
punctuation in front of quotes"), at lines 32 and 258. Both are the same
verbatim quotation of the paper's question "is the STB-conjecture true for
*B* = 2 in sponge?", which ends in a question mark inside the quotation
marks. Neither is fixable without altering a quote, and the same pattern
occurs in already-published drafts (for example
`../nonblackbox-owf-minimality/statement.tex` line 302), so the folder's
`.chktexrc` is left identical to every other one rather than customized.

## Forward literature check, 2026-08-23

Searched for any work after TCC 2023 proving or refuting the sponge STB
conjecture, or improving the *B* = 2 or *B* ≥ 3 sponge bounds. Found none;
the most recent items located on this question are the source paper itself
and Freitag–Ghoshal–Komargodski (CRYPTO 2022). **This is a targeted check,
not an exhaustive sweep**, and a reviewer should search for papers citing
IACR ePrint 2023/1444 and 2022/1009 before relying on "still open".

## Build

- pdflatex: ok (2 passes, 0 LaTeX warnings)
- chktex: 2 warnings (both quotation artefacts; see above)
- lacheck: 0 warnings
