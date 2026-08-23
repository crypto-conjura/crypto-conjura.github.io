# Provenance: A Quadratic-Advice Two-Block Sponge Collision Attack with Preprocessing

Written by hand, following `prompts/harvest.md`, on 2026-08-23.
`scripts/harvest_conjectures.py` could not be used on this machine
(neither model backend was available: no `claude` CLI binary on `PATH`, no
Anthropic SDK, no API credentials), so the extract/verify/typeset steps were
carried out in-session instead. The two mechanical steps the pipeline owns
were still run: every quote below was grounded against the PDF's `pdftotext
-layout` text layer using `PdfDoc.ground` from `scripts/harvest_conjectures.py`
itself, and the build was checked with `pdflatex`, `chktex` and `lacheck`.
**Nothing here has been checked by a human.**

This is the second of two statements harvested from the same paper. The
first is `../stb-conjecture-sponge/`, and the two are deliberately not
merged: the paper poses them as consecutive, separate open problems, and an
affirmative answer to this one refutes that one in the regime *ST*³ > *C*.

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

`paper-asks`. Section 1.3, "Discussions and open problems", second item,
headed "Better attacks for *B* = 2?" (p. 9). The paper observes that its own
Theorem 2 security bound carries a term *S*²*T*⁴/*C*² that no known attack
reaches, exhibits an attack reaching it in the *multi-instance* model
(Theorem 3, restated as Theorem 11 in section 5), and asks whether the same
ideas give a corresponding attack in the auxiliary-input model. The
multi-instance half is therefore a theorem of the paper; only the lift is
open, and the paper reports no partial result on it.

## Quotes, checked against the PDF text layer

Matched mechanically against `pdftotext -layout` output after undoing
ligatures, line-broken hyphens and curly quotes, using this repository's own
`ground()`.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 9 | 9 | exact (100%) | The current security upper bound for B = 2 suggests that there may exist an attack with advantage |
| openness | 9 | 9 | exact (100%) | Can we utilize similar ideas to show a corresponding attack in the auxiliary-input random permutation model? |
| partial | 9 | 9 | exact (100%) | And we show an attack in the multi-instance model with advantage |
| partial | 4 | 4 | exact (100%) | Therefore the above bound is optimal when the S 2 T 4 /C 2 term doesn't dominate the sum, i.e., ST 3 |
| hardness | 9 | 9 | exact (100%) | Because our attacks require knowing queries from previous rounds, our attacks don't apply to stateless multi-instance games. |
| definition | 11 | 11 | exact (100%) | takes σ and a challenge salt a ∈ [C] as input, makes T queries to F or F −1 , and outputs m, m′ . |
| definition | 12 | 12 | exact (100%) | Sample ai ← [C] at uniformly random without replacement |
| definition | 13 | 13 | exact (100%) | Such a theorem relating AI-security to MI-security has been used in several prior works. |
| definition | 10 | 10 | exact (100%) | Initialize (x0 , y0 ) = (0, a). |

All nine ground exactly on the pages claimed. The two displayed quantities
Ω(*S*²*T*⁴/*C*²) and (Ω(*S*²*T*⁴/*C*²))^*S* sit between the first three
quotes and do not survive text extraction; they were read from the rendered
page 9 and cross-checked against Theorem 3 on the rendered page 5 and
against Table 2 on page 6, which lists "(Ω̃(*S*²*T*⁴/*C*²))^*S* [Thm 11]"
in the *B* = 2 row of the "Our attacks" column. That cross-check mattered:
the text layer interleaves the superscripts of Theorem 3 and, read from the
text layer alone, appears to assign (Ω(*ST*/*C*))^*S* to the two-block case.

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

The asymmetry the statement asserts is real and is the paper's own: the
multi-instance attack is a theorem, the auxiliary-input attack is a
question. The repairs concern the statement's form rather than its content.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 9 | Section 1.3, p. 9, heading "Better attacks for *B* = 2?". |
| Openness | pass | 5, 9 | The paper supplies the MI attack and asks for the AI analogue; no section supplies one. Its own Table 1 (p. 5) lists the best known *B* = 2 attack as *ST*/*C* + *T*²/min(*C*,*R*), not *S*²*T*⁴/*C*², so the paper's own accounting agrees that the AI attack does not exist yet. |
| Strength | **fail → corrected** | 9 | The paper's target is Ω(*S*²*T*⁴/*C*²) with no range on *S*, *T*, *C*. Stated unrestricted, the claim asserts that a probability can exceed one. Corrected by the side condition *S*²*T*⁴ ≤ *C*², flagged in the remark "the side condition" as a formalization choice not taken from the paper. |
| Quantifiers and parameters | pass | 5, 12 | Theorem 3's side condition *S*, *T*, *R* ≥ 16 is carried into the statement's Theorem 1 verbatim. The MI game samples the *S* challenge salts uniformly **without replacement**, as the paper's Definition 5 does, and the statement's Definition 3 says so rather than defaulting to the with-replacement variant the paper defines separately as `rand-MICR` (Definition 6). |
| Attribution | pass | 9 | The MI attack and the *S*²*T*⁴/*C*² bound are both the source paper's; the attack whose optimality would be refuted is Freitag–Ghoshal–Komargodski's; the Merkle-Damgård comparison Θ̃(*ST*/*N* + *T*²/*N*) is attributed to Akshima–Cash–Drucker–Wee and Akshima–Guo–Liu, not to the source. |
| Definitions | pass | 10, 11, 12 | Sponge, the AI game and the MI game reproduce section 2.3 and Definitions 2, 3 and 5. The MI adversary's statefulness across rounds is stated, because it is what the hardness discussion turns on. |
| Fabrication | **fail → corrected** | 9 | The first draft asserted flatly that the AI attack exists. The paper says its bound "suggests that there may exist" one, then asks a question. Corrected: the remark "what the source paper does and does not claim" reproduces both hedges and records the direction as a reading. A second correction: the first draft implied a general MI-to-AI lifting principle; the remark "which lift is being asked for" now states that only this instance is asserted and that the theorem runs the other way (Theorem 6: an MI *bound* of δ^*S* gives an AI bound of 2δ). |
| Self-containment | pass | – | Definitions 1–3 give the construction and both games, so a solver knows which model the attack must live in and which one it may not. |

### Unsupported by the paper, and marked as such on the page

- The side condition *S*²*T*⁴ ≤ *C*² — the paper states no range.
- The Ω̃ rather than Ω in Conjecture 1 and Theorem 1. The paper's section 1.3
  prose writes Ω; its Theorem 3 and Table 2 write Ω̃. The tilde reading is
  taken from the theorem rather than from the prose.
- The account of *why* the lift is hard (the MI attack's reliance on
  accumulated earlier rounds). The paper states the fact — "our attacks
  require knowing queries from previous rounds" — in the *adjacent* open
  problem about stateless multi-instance games, and does not itself connect
  it to the AI lift. That connection is an inference drawn from the paper's
  own sentence rather than a claim the paper makes, and the page attributes
  it that way.

### Citations not in the source paper's reference list

None. `ACDW20`, `AGL22`, `CDG18` and `FGK22` all appear in the source
paper's reference list (pp. 32–33); `ADGL23` is the source paper itself.

### Build warnings, not suppressed

One instance of `chktex` warning 38 at line 112, on the verbatim quotation
of the paper's closing question, which ends in a question mark inside the
quotation marks. Not fixable without altering the quote; the folder's
`.chktexrc` is left identical to every other one.

## Forward literature check, 2026-08-23

Searched for any post-TCC-2023 auxiliary-input attack on two-block sponge
collisions, and for any improvement to the *B* = 2 sponge bounds. Found
none. **This is a targeted check, not an exhaustive sweep**; a reviewer
should search for papers citing IACR ePrint 2023/1444 and 2022/1009 before
relying on "still open".

## Build

- pdflatex: ok (3 passes, 0 LaTeX warnings)
- chktex: 1 warning (quotation artefact; see above)
- lacheck: 0 warnings
