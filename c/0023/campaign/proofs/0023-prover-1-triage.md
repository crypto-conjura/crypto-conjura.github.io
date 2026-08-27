---
id: 0023-prover-1-triage
agent: triage
model: claude-fable-5
cycle: 2
---

# Triage ruling — artifact 0023-prover-1 (rung I01), verification round 1

Inputs: CONTRACT.md, I01-spread-junta.md, 0023-prover-1.md, the five blind
reports 0023-prover-1-verify-{A,B,C,D,E}.md, card S1-acc22-card.md.
Adjudicated on the mathematics alone; disputed computationally checkable points
were verified by exact-arithmetic enumeration (Fractions, exhaustive small
cases), not by rhetoric.

## Tally

**UPHELD: 0 · OVERRULED: 3 · PEDANTIC: 6 · NEEDS SOURCE: 0 · UNCLEAR: 0**

Per-pass post-triage status: **A clean, B clean, C clean, D clean, E clean**
(no pass produced an UPHELD finding).

---

## Rulings, every finding and observation in all five reports

### Pass A

**A-1 (§4 Lemma 2, degenerate case: "by the first direction, A∩B≠∅") —
class C — ruled PEDANTIC.**
Re-derived myself. The lemma's first proved paragraph, labelled (⇐), proves
"x∈A∩B ⟹ projections intersect"; as a direction of the biconditional it yields
only "disjoint projections ⟹ A∩B=∅", which cannot license concluding A∩B≠∅
from intersecting projections. The implication the degenerate case needs —
"projections intersect ⟹ A∩B≠∅" — is exactly the second paragraph's gluing
construction, which applies verbatim at S=∅ (u the empty string, any p∈P, q∈Q;
no consistency constraint since J∩K=∅; verified exhaustively by enumeration at
N=4 over all nonempty size-1-window pattern pairs: every S=∅ pair intersects).
So the referee is textually right: the cross-reference should read "second
direction". It is a one-word mislabel whose correct justification sits one
paragraph above in the same lemma; a competent reader fills it without effort.
Class C, not class A (no statement drift), so PEDANTIC is available and is the
right grade. Lemma 2 and everything downstream are unaffected. Suggested
(optional, next-revision-only) fix: "first" → "second".

**A's affirmative clearances — spot-checked, stand.** I re-derived Lemma 3's
reduction to g(a)=(a+b)log₂(a+b)−a·log₂a−b·log₂b−2b, g(b)=0, g′(a)=
log₂((a+b)/a)>0; Lemma 5's ν_P+ν_Q≤1 ⟹ ν_Pν_Q≤1/4 ⟹ payment ≥ ½log₂4 = 1;
Lemma 6's summation-order chain (average over 𝐅 taken before the δ_F bound,
routed through the partner's window); and the §0/§9-vs-I01 statement diff
(verbatim; δ(d)=1/(3d) N-free). All correct as A reports.

### Pass B

**B-1 (§5 Lemma 3, WLOG needs a≥1) — ruled PEDANTIC.**
Concur with the referee's own grading. In fact the artifact already writes
"Case b=0. Then |W|=a≥1" — the only implicit whisker is that a≥1 follows from
W≠∅ with b=0. Nothing to change.

**B-2 (§6 Lemma 4 Step 1, |V_u△V_{u′}| ≥ ||V_u|−|V_{u′}||) — ruled PEDANTIC.**
Standard one-line fact (△ contains the larger set minus the smaller); true,
routine, no rewrite required.

**B-3 (§10 Remark 10.1 vs card S1) — recorded by B as a non-defect; conclusion
concurred, reasoning corrected.** B's clearance says the inline construction
"matches the card's construction and stated influence level exactly". That is
wrong as stated: exact arithmetic shows the card's summed NegRow polynomial has
RelInf = 1/5 at d=2 (and strictly < 1/(2d) for all d≥2), while the artifact's
uniform row-distribution has average influence exactly 1/(2d) = 1/4 at d=2 —
numerically distinct objects (see D-1 below). B's bottom line (no citation
defect) is nonetheless correct, because the card is provenance-only and the
remark is self-proved. This correction does not create an UPHELD finding
against the artifact; it is a note against B's report for the record (per the
c/0048 lesson, affirmative clearances were spot-checked, and this one's
justification — though not its verdict — fails).

### Pass C

**C-1 (§10 Remark 10.1, "This is the NegRow/PosCol pattern of [ACC22] Claim
B.3 … reproved inline") — (D)-adjacent, non-load-bearing — ruled PEDANTIC.**
Same substance as D-1; see the consolidated ruling there. C's own grading
(PEDANTIC, no repair needed) is confirmed.

**C's affirmative clearances — spot-checked, stand** (Lemma 6's
enlarge-to-the-partner's-window analysis in C's log is correct and is the
sharpest statement in any report of why the forbidden max-over-support route is
avoided; independently confirmed).

### Pass D

**D-1 (§10 Remark 10.1, identification with card S1's NegRow/PosCol) — class D,
non-load-bearing — ruled PEDANTIC.** Adjudicated with my own re-derivation
against card S1, plus exact computation:

* Card S1 item S1.c prints Definition B.1's NegRow = Σᵢ AND_m(x_{i,*}) and
  PosCol = Σⱼ AND_n(−x_{*,j}): two *single summed polynomials*, i.e. singleton
  (point-distribution) supports, with RelInf strictly < 1/(2n) (Claim B.2).
* The artifact's Remark 10.1 object is a *uniform distribution over the d
  individual row (resp. column) singleton-pattern indicators*, with
  per-coordinate average influence **exactly** 1/(2d).
* Verified by exact arithmetic (Fractions, full-cube enumeration at d=1,2 via
  the flip identity, closed form for all d): artifact's average influence
  equals 1/(2d) exactly at every coordinate; the card's summed polynomial has
  RelInf = 2^{−m−1}/(n2^{−m}+n(n−1)2^{−2m}), e.g. 1/5 vs 1/4 at d=2, 2/15 vs
  1/6 at d=3. **Different objects for every d ≥ 2.** The artifact's is the
  distributional variant that I01's own "Grid ceiling" bullet describes; the
  combinatorial obstruction (all-(−1) row vs all-(+1) column crossing) is the
  same, which is what "the NegRow/PosCol pattern" gestures at.

Why PEDANTIC and not UPHELD: nothing from the card is *used* — the remark is
declared non-load-bearing (§11), fully self-proved from Lemma 1 (recomputed by
three referees and by me), and the card is invoked as provenance with the
explicit caveat "the card is context, not justification". No hypothesis of S1
enters any step, so no class-D misuse exists; the only imprecision is the word
"is" where "is the distributional analogue of" would be exact. Not class A, so
the never-PEDANTIC rule does not bind. Suggested (optional) one-word fix as D
proposes; no revision cycle is warranted for it.

**D O-1 (§8 Remark 8.1, "This is the engine I01's binding generalization
hypothesis demands") — ruled PEDANTIC (ledger note, no rewrite).**
The mathematical content of Remark 8.1 is true and verified (bilinear in
(p_a),(q_b); only per-coordinate averages and window budgets ≤ d; no
pattern-count constants). The claim that this engine is what R2/R3 inherit is
prover judgement about future rungs, not a fact this artifact establishes:
D correctly notes Lemma 1's exactly-one-endpoint dichotomy and Lemma 4's fiber
counting are indicator-specific and have no evident signed/complex analogue.
**Ledger instruction: record "generalization hypothesis met" as I01's own
recorded-detour test passed (no enumeration, no 2^{2^d}) — not as a verified
claim that the engine lifts to signed classes.**

**D O-2 (§2 ASCII dependency graph, long backslash from Lemma 1) — ruled
OVERRULED (as a defect; the referee itself called it cosmetic).**
The backslash terminates at the row "Theorem (uses 6)  + Remark 10.1 (uses 1;
NOT load-bearing)", whose "(uses 1)" annotation disambiguates the edge as
Lemma 1 → Remark 10.1; the §11 prose dependency statement is accurate. No
mathematical content is affected and no reader can be misled about the proof
chain. Nothing to change.

**D's affirmative clearances — spot-checked, stand** (D's negation-check table,
including the all-four-inequalities-tight trace of the grid through Lemma 6,
independently reproduced by my computation: the grid saturates (6.1) at exactly
1).

### Pass E

**E N1 (Remark 10.1 vs S1) — non-defect, concurred — merged into D-1: ruled
PEDANTIC** (same substance, same disposition).

**E N2 (§0 "within a factor 3/2 of optimal"; choosing 1/(3d) under-claims) —
ruled OVERRULED (no defect).** Under-claiming is not drift; I01 asks for one
admissible inverse-polynomial δ and c₁=1/3, c₂=1, δ(d)=1/(3d) is admissible.
Concur with E's own non-defect classification.

**E N3 (§1 real-valued reduction) — ruled OVERRULED (no defect).** The class
consists of nonnegative real functions; over ℤ₂ the characters are real, the
ℂ-Fourier coefficients of a real function are real, and |f̂(χ)|² = f̂(T)²; the
Contract itself prints this specialization. Legitimate, no gap.

**E N4 (Remark 8.1 meta-claim) — merged into D O-1: ruled PEDANTIC (ledger
note as above).**

**E's affirmative clearances — spot-checked, stand.**

---

## FILTERED REPORT (UPHELD + PEDANTIC only — input to any future reviser)

**UPHELD findings: none. No revision cycle is required; the artifact passes
triage unchanged.**

PEDANTIC notes (record only; optional one-word polish if the file is ever
touched for another reason — do NOT open a revision cycle for these):

| # | Location | Note |
|---|---|---|
| P1 (from A-1) | §4 Lemma 2, degenerate case | "by the first direction" should read "by the second direction" (the gluing construction, applied at S=∅). Mathematics unaffected. |
| P2 (from B-1) | §5 Lemma 3, case b=0 | a≥1 follows from W≠∅; artifact already writes "|W|=a≥1". |
| P3 (from B-2) | §6 Lemma 4 Step 1 | |V△V′| ≥ ||V|−|V′|| is a standard one-liner, uncited. |
| P4 (from C-1/D-1/E-N1) | §10 Remark 10.1 | "This is the NegRow/PosCol pattern of [ACC22] Claim B.3" → more exactly "the distributional analogue of". Card's object: summed polynomials, singleton supports, RelInf strictly < 1/(2d) (= at d=1); artifact's: uniform distributions over d indicators, average exactly 1/(2d). Verified numerically distinct for all d≥2. Non-load-bearing. |
| P5 (from D-O1/E-N4) | §8 Remark 8.1 | Ledger must record "generalization hypothesis met" as I01's detour test passed, not as a verified claim that the engine lifts to signed/complex classes (Lemmas 1 and 4 are indicator-specific). |
| P6 | §2 ASCII graph | (Subsumed cosmetic note; see O-2 ruling — no change needed.) |

Marginal card note (not a finding against the artifact): card S1 / [ACC22]
Claim B.2's strict "RelInf < 1/(2n)" is an equality at n=1 (RelInf = 1/2 =
1/(2·1); the printed proof's strictness comes from the n(n−1)2^{−2m} term,
which vanishes at n=1). Harmless everywhere it is used; worth a one-line
annotation on the card if it is ever revised.

## ESCALATION LIST (UNCLEAR)

None.

## CONSOLIDATED SOURCE REQUEST

None. No class-(D) misuse and no class-(E) unverifiable dependency exists; the
load-bearing chain (Lemmas 1–6, Theorem) cites nothing external, and the sole
card mention (S1, Remark 10.1) is provenance-only and was checked against the
card held.

## Disposition

All five passes are post-triage clean (0 UPHELD across A–E). Under §3.5's
acceptance rule this artifact has 5/5 clean passes: recommend **freeze-gate** —
mark I01/R1 ESTABLISHED and FROZEN against artifact 0023-prover-1, record the
tally and the P5 ledger caveat, evict the proof from active context, and
advance to the next rung. (External blind review per §3.5.1 remains the
campaign's higher bar before any headline claim; that is the human's call at
the freeze gate.)

### END OF ARTIFACT 0023-prover-1-triage ###
