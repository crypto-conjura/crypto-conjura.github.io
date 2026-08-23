# Provenance: A Tight Quantum Time-Space Tradeoff for Two-Block Merkle-Damgård Collisions

Written by hand, following `prompts/harvest.md`, on 2026-08-23.
`scripts/harvest_conjectures.py` could not be used on this machine
(neither model backend was available: no `claude` CLI binary on `PATH`, no
Anthropic SDK, no API credentials), so the extract/verify/typeset steps were
carried out in-session instead. The two mechanical steps the pipeline owns
were still run: every quote below was grounded against the PDF's `pdftotext
-layout` text layer using `PdfDoc.ground` from `scripts/harvest_conjectures.py`
itself, and the build was checked with `pdflatex`, `chktex` and `lacheck`.
**Nothing here has been checked by a human.**

**This is the weakest of the four statements in this batch, and the reason is
definitional, not mathematical: the source paper never defines the quantum
model.** Read the "Definitions" row of the check table and the statement's
remark "the model is supplied here, not taken from the source" before
anything else.

## Source

- Paper: **Time-Space Lower Bounds for Finding Collisions in Merkle-Damgård Hash Functions**
- Authors: Akshima, Siyao Guo, Qipeng Liu
- Venue/archive: CRYPTO 2022, Part III, LNCS 13509, pp. 192–221; IACR ePrint 2022/885 (this version dated 6 July 2022)
- Identifier: IACR ePrint 2022/885
- Bibliographic detail: printed-on-page
- File: `2022-885.pdf` (34 pages)
- sha256: `4467ddab666b88f94c1b471c91c81cec5ff8031f0c39808bd1da1cc8abbb2071`
- Read on 2026-08-23 in-session (no backend)

## How the paper leaves it open

`paper-asks`. Section 1.3, "Discussions and open problems", second item,
headed "Tight quantum time-space tradeoffs for finding collisions in MD?"
(p. 10). The paper is classical throughout — its own theorems are classical
bounds in the auxiliary-input random-oracle model — and reports the quantum
state of the art as having no matching upper and lower bounds at *any* block
length, including *B* = 2 and *B* = *T*. It asks two questions in the same
paragraph; this statement is the second of them, and the first is
deliberately kept separate (see the statement's remark "the security-jump
question is a different statement").

## Quotes, checked against the PDF text layer

Matched mechanically against `pdftotext -layout` output after undoing
ligatures, line-broken hyphens and curly quotes, using this repository's own
`ground()`. All nine ground exactly on the pages claimed.

| role | page | found | match | quote |
| --- | --- | --- | --- | --- |
| statement | 10 | 10 | exact (100%) | Motivated by analyzing post-quantum non-uniform security, several recent works [CGLQ20, GLLZ21] studied the same question in the quantum setting, in which the adversary is given S-(qu)bit of advice and T quantum oracle queries. |
| openness | 10 | 10 | exact (100%) | However, unlike the classical setting, no matching bounds are known, even for B = 2 and B = T . |
| openness | 10 | 10 | exact (100%) | Is there a security jump for finding 2-block collisions and unbounded collisions in the quantum setting? Can we leverage our new proof for B = 2 to prove a tight security bound in the quantum setting? |
| parameters | 10 | 10 | exact (100%) | However, the best-known attack achieves O(ST 2 /N + T 3 /N ) for every 2 |
| parameters | 10 | 10 | exact (100%) | security bound by [GLLZ21], suggests that the optimal attack may speed up the trivial quantum collision finding by a factor of S. |
| context | 3 | 3 | exact (100%) | In particular, their bound confirms STB conjecture for B = O(1). |
| definition | 12 | 12 | exact (100%) | is unbounded (making unbounded number of oracle queries to H) and outputs S bits of advice σ; |
| definition | 12 | 12 | exact (100%) | takes σ and a salt a ∈ [N ], issues T queries to H and outputs m1 , m2 . |
| definition | 12 | 12 | exact (100%) | The game outputs 1 (indicating that the adversary wins) if and only if A outputs a pair of MD collision with at most B(N ) blocks. |

Note what the fifth quote does *not* include: the paper's sentence begins
"The Ω(*ST*³/*N*) security bound by [GLLZ21]", and the quote starts after
the formula because the formula does not survive text extraction. The Ω was
read from the rendered page 10. See the "Quantifiers and parameters" row
below — this is the paper's own notation and it is unconventional.

## Adversarial check

**Verdict: faithful-with-corrections** (confidence: medium)

The question is posed in the paper's open-problems section, nothing in the
paper or in the literature settles it, and the statement is at the paper's
strength on the mathematics it does state. Four defects were repaired, one
of them serious.

| check | result | page | finding |
| --- | --- | --- | --- |
| Existence | pass | 10 | Section 1.3, p. 10, heading "Tight quantum time-space tradeoffs for finding collisions in MD?". |
| Openness | pass | 10 | The paper's own contributions are classical: Theorem 1 (the 2 < *B* < *T* bound), Theorem 2 (the *B* = 2 bound), Theorem 3 (the MI reduction), developed in sections 2–4 with the classical proofs in the appendix. Nothing in the paper proves anything quantum, and it states outright that no matching quantum bounds are known at any *B*. |
| Strength | **fail → corrected** | 10 | The paper asks whether a tight quantum bound can be proved; it does not name the tight value. The statement fixes the affirmative direction by taking the reported best attack to be optimal — the only candidate value the paper's own two figures make available. Recorded in the remark "the source poses a question; the direction is a reading", which also says that a refutation resolves the paper's question just as well. |
| Quantifiers and parameters | **unclear** | 10 | The paper writes the known security bound as **Ω**(*ST*³/*N*) and the known attack as **O**(*ST*²/*N* + *T*³/*N*), which is the reverse of the usual convention (a security bound upper-bounds advantage; an attack lower-bounds it). This cannot be settled from this paper, which proves neither figure. Both are quoted as printed in the remark "the source's *O* and Ω are reproduced as printed", the conjecture itself is stated in the conventional direction, and the reader is told to check Guo–Li–Liu–Zhang directly. **This is the one check that did not pass and could not be resolved from the source.** |
| Attribution | pass | 10 | The question is the source paper's. The quantum attack and the *ST*³/*N* figure are attributed to Chung–Guo–Liu–Qian and Guo–Li–Liu–Zhang exactly as the paper attributes them; the classical *B* = 2 result to Akshima–Cash–Drucker–Wee and to the source paper's own Theorem 2; the classical unbounded-length result to Coretti–Dodis–Guo–Steinberger. |
| Definitions | **fail → corrected** | 12 | The paper defines only the classical game (Definitions 2 and 3, p. 12, quoted above) and describes the quantum setting in a single clause, citing two other papers for it. The statement's Definition 3 follows the paper's classical definitions clause for clause on the classical parts and then supplies four choices the paper does not make: quantum rather than classical advice, a single computationally unbounded preprocessing stage, standard XOR-type superposition queries, and no bound on the online stage beyond the query count. The remark "the model is supplied here, not taken from the source" states each choice and names this as the part most in need of checking against the two cited papers. A different reading — classical advice, say, or a bounded-memory online stage — would be a different statement. |
| Fabrication | **fail → corrected** | 10 | The first draft merged the paper's two quantum questions into one statement with two clauses, which the harvest prompt forbids and which would also have been wrong: granting the tight *B* = 2 bound does not settle whether a security jump exists, since the unbounded-length quantum advantage could still be Θ̃(*ST*³/*N*). Corrected: the statement is the tight *B* = 2 bound alone, and the remark "the security-jump question is a different statement" explains the gap. |
| Self-containment | pass | – | Definitions 1–2 and the notation list fix the construction, the resources and the quantity — subject to the model caveat above, which is the whole of the reservation on this statement. |

### Unsupported by the paper, and marked as such on the page

- The entire quantum model (statement's Definition 3). Recorded in the
  remark "the model is supplied here, not taken from the source".
- The affirmative direction of the conjecture. Recorded in the remark "the
  source poses a question; the direction is a reading".
- The account of why transplanting the classical *B* = 2 proof is hard —
  that the "high knowledge gaining" events are counting statements about a
  recorded transcript that a quantum offline stage does not have. The events
  themselves are the paper's (section 1.2, pp. 6–7, listed as **E**₁, **E**₂,
  **E**₃); the observation that they do not survive quantization is an
  inference and is not something the paper says. A reviewer should treat that
  paragraph as the page's own reasoning.

### Citations not in the source paper's reference list

None. `ACDW20`, `CDGS18`, `CGLQ20`, `GLLZ21` and `Unr07` all appear in the
source paper's reference list (pp. 32–34); `AGL22` is the source paper
itself.

### Build warnings, not suppressed

`chktex` reports seven warnings, all artefacts of verbatim quotation:

- Four instances of warning 36 ("You should put a space in front of / after
  parenthesis"), at lines 85 and 240. Both are the paper's own phrase
  "*S*-(qu)bit of advice", quoted verbatim; inserting the spaces `chktex`
  wants would alter the quote.
- Three instances of warning 38 ("You should not use punctuation in front of
  quotes"), at lines 87, 112 and 268, on quoted sentences that end in a full
  stop or a question mark inside the quotation marks.

The folder's `.chktexrc` is left identical to every other one rather than
customized to hide these.

## Forward literature check, 2026-08-23

Searched for any tight quantum time-space tradeoff for collision-finding in
Merkle-Damgård, at *B* = 2 or otherwise, published after CRYPTO 2022.
Found none. Two adjacent items were located and checked far enough to rule
out: Carolan–Poremba–Zhandry, *(Quantum) Indifferentiability and
Pre-Computation* (arXiv:2410.16595), which is about indifferentiability
under pre-computation and whose application is to the one-round sponge, not
to *B*-block Merkle-Damgård collision bounds; and the *Journal of
Cryptology* 37 (2024) version of the source paper itself. **This is a
targeted check, not an exhaustive sweep**, and the quantum
time-space-tradeoff literature is active; a reviewer should search for
papers citing IACR ePrint 2022/885 and TCC 2021's *Unifying presampling via
concentration bounds* before relying on "still open".

## Build

- pdflatex: ok (3 passes, 0 LaTeX warnings)
- chktex: 7 warnings (all quotation artefacts; see above)
- lacheck: 0 warnings
