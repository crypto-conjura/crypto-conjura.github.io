---
id: 0023-prover-1-verify-D
agent: verifier-b
model: claude-opus-5[1m] (Opus 5, 1M context)
cycle: 2
---

# Blind referee pass D on artifact `0023-prover-1` (rung I01)

## STEP 0 — COMPLETENESS

Artifact terminates with `### END OF ARTIFACT 0023-prover-1 ###`; §§0–12 are all
present, no unit stops mid-proof, no dangling forward reference (the §2
dependency graph names exactly Lemmas 1–6 + Theorem + Remark 10.1, and all
eight exist). **Not truncated.** Proceed to verification.

---

## 1. FINAL VERDICT

**CLEAN** — the artifact proves exactly the I01 statement, with the quantifiers
in the contracted order and δ(d)=1/(3d) independent of N; Lemmas 1–6 and the
Theorem are each derived in full from the Contract's definitions with no
external input, and I found no class-(A)–(E) defect that affects the result
(two non-blocking observations, both on explicitly non-load-bearing remarks,
are recorded below).

---

## 2. CLASS (A) CHECK FIRST — WHAT THE ARTIFACT ACTUALLY PROVES

**In my own words.** Fix c₁=1/3, c₂=1, δ(d)=1/(3d), *before* any d, N, **F**,
**G**. Let d,N ≥ 1 and let **F**,**G** be *any* finitely supported probability
distributions whose supports consist of functions of the form
1_A/‖1_A‖₂ with A = {x ∈ {±1}^N : x_J ∈ P}, |J| ≤ d, ∅ ≠ P ⊆ {±1}^J. Suppose
that **for every single coordinate i ∈ [N]** the *average over the
distribution* of Inf_i is ≤ 1/(3d), for both **F** and **G**. Then some
f ∈ supp **F**, some g ∈ supp **G**, and some x ∈ {±1}^N have f(x)g(x) ≠ 0.

**Diff against the I01 rung statement (§"Statement", lines 22–32).** Word for
word identical modulo the instantiation of the three existential witnesses.
Item by item on the drift axes the task names:

| Axis | I01 requires | Artifact delivers | OK? |
|---|---|---|---|
| Quantifier order | ∃(c₁,c₂,δ) → ∀(d,N,**F**,**G**) → ∃(f,g,x) | §9 Theorem states it in exactly this order; witnesses are numeric constants fixed in the statement line, not functions of d,N,**F**,**G** | ✓ |
| Class | 𝒞^junta_d: normalized indicators of ≤d-windows, P ≠ ∅ | §0 reproduces the class verbatim; §1 fixes f_{J,P} := 1_A/‖1_A‖₂; nothing wider or narrower is used | ✓ |
| Average vs max influence | E_{f∼**F**}[Inf_i(f)] ≤ δ(d) | Lemma 6 defines δ_F := max_{i∈[N]} **E**_{f∼**F**}[Inf_i(f)] — a max over *coordinates*, of the *average over the distribution*. The counting step ∑_a p_a Inf_i(f_a) = E_**F**[Inf_i] is genuinely distributional; there is no max-over-support anywhere | ✓ (this is the failure mode the Contract forbids, and it is avoided) |
| Per-coordinate vs summed | "for every i ∈ [N]" | Used exactly as a per-coordinate bound; the summation in Lemma 6 is over i ∈ K_b (resp. J_a), and the bound δ_F is applied once per coordinate in that window | ✓ |
| N-independence of δ | δ = δ(d) only | δ(d)=1/(3d). N enters the proof only through (a) the cancelling factor 2^{N−|J|} in Lemma 1 (1.3)/(1.4), and (b) the finite index set [N] in the max defining δ_F. The final chain (6.1)→(6.2) contains no N | ✓ |
| Exactness of conclusion | f(x)g(x) ≠ 0 at a single point | §9 negates exactly this; the contradiction hypothesis "for all f,g,x: f(x)g(x)=0" is converted into cross-disjointness of supports using positivity of normalized indicators. No approximate/high-probability substitute | ✓ |
| Degree/unit norm | I01 says "automatic" | Remark 3.1 discharges both inline (non-load-bearing, but correct) | ✓ |
| NOT-acceptable list | δ(N); max-over-support; windows > d; citing "Rung 0" | None occur. Windows enter only via |J_a|,|K_b| ≤ d of the *chosen* witness. The conjunction "Rung 0" calibration is never cited | ✓ |

**No class-(A) drift.** The artifact does not prove a weaker or a different
statement, and it does not overclaim: §12 restates "establishes rung R1 only —
not ℤ₂-PCC and not PCC".

---

## 3. NEGATION CHECK (§3.5 step 0.5), per load-bearing lemma

For each lemma I assumed the negation and hunted for a witness, by hand
computation on small cubes and by looking for structural slack.

| Lemma | Negation attempted | Result | Tag |
|---|---|---|---|
| **L1** Inf_i(f_{J,P}) = b_i(P)/(2|P|) | Recomputed the Fourier expansion by hand for (i) J={1}, P={+1}: 1_A=(1+x₁)/2, f=(1+x₁)/√2, Inf₁=1/2 vs b₁/(2|P|)=1/2; (ii) J={1,2}, P = all but (−,−): 1_A = 3/4+x₁/4+x₂/4−x₁x₂/4, ‖1_A‖₂²=3/4, Inf₁ = (4/3)(1/16+1/16)=1/6 vs b₁/(2|P|)=1/6 | Formula exact in both; no witness | **MECH** |
| **L2** A∩B=∅ ⟺ π_S(P)∩π_S(Q)=∅ | Tried S=∅ (the vacuity trap) and J⊄K overlaps; the explicit glue point in the (⇒) direction is well defined because {J, K\J, [N]\(J∪K)} partitions [N] | No witness; the S=∅ branch is discharged, not assumed away | **MECH** |
| **L3** \|∂_E W\| ≥ \|W\| log₂(2^n/\|W\|) | n=2: \|W\|=1 (2 = 2, equality), \|W\|=2 diagonal (4 ≥ 2), \|W\|=2 subcube (2 = 2), \|W\|=3 (2 ≥ 1.245); n=3: \|W\|=3 L-shape (5 ≥ 4.245), \|W\|=6 with complement an edge (4 ≥ 2.49) and with complement antipodal (6 ≥ 2.49); W = full cube (0 = 0) | No witness; equality only at subcubes, as Remark 5.1 says | **MECH** |
| **L4** ∑_{i∈S} Inf_i ≥ ½log₂(1/ν_P(S)) | Sought a low-influence sparse-projection pattern: subcube P with j fixed coordinates in S (LHS=RHS=j/2, equality); parity/diagonal P (LHS=1/2 > RHS=0, slack); product pattern P = U×{±1}^{J\S} (reduces to L3 on U, no slack lost); P ⊆ a half-space (LHS=RHS=1/2) | No witness; the inequality is tight exactly where L3 is | **MECH** |
| **L5** cross-disjoint pair pays ≥ 1 on S | ν_P+ν_Q ≤ 1 is forced by disjoint nonempty projections inside {±1}^S; the AM–GM step is tight only at ν_P=ν_Q=1/2, realised by Remark 7.1 (J=K={1}, P={−1}, Q={+1}) at exactly 1 | No witness | **MECH** |
| **L6** δ_F·E\|K\| + δ_G·E\|J\| ≥ 1 | Tried to beat max(δ_F,δ_G) ≥ 1/(2d). Ceiling: for any indicator class member Inf_i = b_i(P)/(2\|P\|) ≤ 1/2 (each point of P lies on exactly one i-edge), so δ_F,δ_G ≤ 1/2; d=2 would need δ_F+δ_G < 1/2, i.e. one side near 0, i.e. that side essentially constant, which meets everything and destroys cross-disjointness. Traced the grid through *every* step: Σ₁ = 1/2 = δ_F∑q_b\|K_b\|, L5 pays exactly 1 per pair, \|J_a\|=\|K_b\|=d — **all four inequalities in the chain are simultaneously equalities**, so there is no slack a cleverer family could exploit | No witness; bound is attained, not beaten | **MECH** |
| Remark 10.1 (non-load-bearing) | Checked the grid ceiling against card S1 (Claim B.3, RelInf ≤ 1/(2d), ℤ₂ only) and against I01's "Grid ceiling" line | Consistent; the remark is reproved inline and does not rest on the card | **CARD** |

No lemma survived as a negation candidate. Adjudication summary:
L1–L6 **MECH**, Remark 10.1 **CARD**, none **NONE**, none required **CODE**
(all checks were closed-form or on cubes of size ≤ 8).

---

## 4. FINDINGS TABLE

| # | Quoted location | Class | Explanation |
|---|---|---|---|
| D-1 | §10 Remark 10.1: "*(This is the NegRow/PosCol pattern of [ACC22] Claim B.3 — card S1 — reproved inline; the card is context, not justification.)*" | (D), **non-load-bearing, PEDANTIC** | Card S1 item S1.c prints Claim B.3 with **NegRow = ∑_{i} AND_m(x_{i,*})** and **PosCol = ∑_j AND_n(−x_{*,j})**, i.e. two *single summed polynomials* with *singleton* supports and RelInf **< 1/(2n)** (strict). The artifact's object is different: a *uniform distribution over the d individual row indicators* against a uniform distribution over the d column indicators, with average influence **exactly 1/(2d)**. The two are not the same construction — the artifact's is the distributional variant that I01's "Grid ceiling" line describes. The word "is" overstates the identification. This is harmless because (a) Remark 10.1 is explicitly declared non-load-bearing (§11), (b) the artifact reproves its own version in full and correctly (I checked b_i(P_r)=1, Inf=1/2 on J_r, E=1/(2d)), and (c) the card is invoked as provenance, not as justification. No hypothesis of S1 is used, so there is nothing to check hypothesis-by-hypothesis. Fix would be one word ("the distributional analogue of"). |
| O-1 | §8 Remark 8.1: "*This is the engine I01's binding generalization hypothesis demands.*" | Observation (not A–E); non-mathematical self-assessment | The mathematical claims in Remark 8.1 are all true as stated and I verified them (the count is linear in each distribution; only per-coordinate averages and the budgets \|J\|,\|K\| ≤ d are used; no constant depends on the number of patterns). But the *editorial* claim that this engine is what R2/R3 inherit is not established by the artifact: Lemma 1's exact edge-count identity and Lemma 4's fiber-counting both use essentially that the functions are 0/1-valued indicators (the "exactly one endpoint in A" dichotomy in Lemma 1 Step 3 has no analogue for signed or complex-valued f). I flag this only so the ledger does not record "generalization hypothesis met" as a *verified* fact; it is a judgement about future rungs, outside I01's statement, and it does not affect acceptance of I01. |
| O-2 | §2 ASCII dependency graph, the long backslash from "Lemma 1" to "Theorem" | Cosmetic | The Theorem uses Lemma 1 only through Lemma 6 → Lemma 5 → Lemma 4; the direct edge drawn from Lemma 1 to the Theorem row appears to be the Remark 10.1 edge. Purely presentational; the §11 prose ("the proof chain is Lemmas 1–6 and the Theorem") is accurate. |

**Nothing UPHELD-worthy at class (A), (B), (C) or (E).** No [GAP], no
[SOURCE-BLOCKED], no [MEMORY] tags are needed anywhere: the gap register's
claim of emptiness is, as far as I can check, honest.

---

## 5. STEP-BY-STEP LOG

### §1 Conventions
- ℕ = {1,2,…} declared; the 0-conventions are quarantined in Remark 9.1. **Accepted.**
- Real-valued reduction: every class member is a nonnegative real function, so the Contract's |f̂(χ)|² is f̂(T)², and the ℤ₂ characters are χ_T(x)=∏_{i∈T}x_i with deg(χ_T)=|T|. Matches the Contract's own specialization paragraph (Contract lines 33–35). **Accepted.**
- f_{J,P} well defined: P ≠ ∅ ⇒ A ≠ ∅ ⇒ ‖1_A‖₂ > 0. **Accepted.**
- **Witnessing representations.** The non-injectivity of (J,P) ↦ f_{J,P} is correctly flagged and correctly neutralised: Inf_i and supp are intrinsic to the function; Lemmas 2,4,5 are stated for arbitrary valid (J,P); Lemma 6 uses only |J_a|,|K_b| ≤ d of the chosen witness, which class membership supplies. I checked that S_ab = J_a ∩ K_b, though witness-dependent, is used only through (i) Lemma 5 (whose hypothesis A_a ∩ B_b = ∅ is witness-independent) and (ii) the inclusions S_ab ⊆ K_b, S_ab ⊆ J_a. **Accepted — this is a real trap, and it is properly disarmed.**

### §3 Lemma 1
- Step 1: χ_Tχ_{T'} = χ_{T△T'}; E[χ_U] = 1[U=∅] by coordinate independence; orthonormality of 2^N functions in a 2^N-dimensional space ⇒ basis; Parseval. **Accepted** (self-contained, no circularity).
- Step 2: χ_T(x^{⊕i}) = ±χ_T(x) ⇒ f(x)−f(x^{⊕i}) = 2∑_{T∋i} f̂(T)χ_T(x); Parseval on that function gives (1.1) Inf_i = ¼E[(f−f^{⊕i})²]. **Accepted.**
- Step 3: the point set {x : exactly one of x, x^{⊕i} ∈ A} is the endpoint set of ∂_iA and has size 2|∂_iA| (i-edges are point-disjoint); with ‖1_A‖₂² = |A|/2^N, E[(f−f^{⊕i})²] = 2|∂_iA|/|A| and Inf_i = |∂_iA|/(2|A|). Arithmetic recomputed and correct. **Accepted.**
- Step 4: (1.3) |A| = |P|2^{N−|J|}; i ∉ J gives ∂_iA = ∅; i ∈ J gives (1.4) |∂_iA| = b_i(P)2^{N−|J|} via the bijection (window i-edge, v) ↦ cube i-edge. Substitution cancels 2^{N−|J|}, leaving b_i(P)/(2|P|) — **N drops out here**, which is the load-bearing point for N-independence. **Accepted.**
- Sanity checks (singleton ⇒ 1/2; full pattern ⇒ 0) verified independently. Remark 3.1(ii) (degree ≤ |J|) verified: f̂(T) = −f̂(T) = 0 for i ∈ T\J.

### §4 Lemma 2
- (⇐) contrapositive: x ∈ A∩B ⇒ x_S ∈ π_S(P) ∩ π_S(Q). **Accepted.**
- (⇒) contrapositive: the glue point x (p on J, q on K\J, +1 elsewhere) is well defined because J, K\J, [N]\(J∪K) partition [N]; x_J = p ∈ P and x_K = q ∈ Q, the latter checked separately on K\J and on K∩J = S using p_S = u = q_S. **Accepted.**
- S = ∅ branch: π_∅(P) = π_∅(Q) = the one-point cube, so they meet, so A∩B ≠ ∅. Constant functions (J = ∅) meet everything. Consequence "disjointness ⇒ S ≠ ∅" is what Lemma 5 needs. **Accepted — the degenerate case is discharged, not swept aside.**

### §5 Lemma 3 (the inline isoperimetry — read hardest)
- **Base n = 0.** The only nonempty W is the one-point cube; LHS = 0 (no edges), RHS = 1·log₂1 = 0. Base case present and correct. **Accepted.**
- **Boundary decomposition.** |∂_EW| = |∂_EW₊| + |∂_EW₋| + |W₊△W₋|. I re-derived this: facet edges split by the last coordinate ε and are boundary iff the projected edge is in ∂_EW_ε; direction-n edges are boundary iff u ∈ W₊△W₋; the two kinds are disjoint and exhaust E({±1}^n). **Exact, not an inequality.** Then |W₊△W₋| ≥ |W₊\W₋| ≥ a−b. **Accepted.**
- **WLOG a ≥ b.** Both the decomposition and the target are invariant under ε ↦ −ε, so the reduction is legitimate. **Accepted.**
- **Case b = 0.** W₋ = ∅ so ∂_EW₋ = ∅; IH applies to W₊ ≠ ∅ (nonempty since |W| = a ≥ 1). a log₂(2^{n−1}/a) + a = a(n−1−log₂a) + a = a(n−log₂a) = a log₂(2^n/a). Recomputed; correct. **Accepted** — note the IH is invoked only at n−1 and only on a nonempty set, so there is no "invoking the statement at a value not yet established".
- **Case b ≥ 1.** Both halves nonempty ⇒ IH applies twice. I independently expanded RHS(3.3) − (a+b)log₂(2^n/(a+b)) and obtained (a+b)log₂(a+b) − a log₂a − b log₂b − 2b, matching the artifact's g(a) exactly (the (n−1) terms cancel against (a+b)n leaving −(a+b), which combines with +a−b to give −2b). **Accepted.**
- **g(a) ≥ 0.** g(b) = 2b log₂(2b) − 2b log₂b − 2b = 2b + 2b log₂b − 2b log₂b − 2b = 0 ✓. g′(a) = log₂(a+b) + 1/ln2 − log₂a − 1/ln2 = log₂((a+b)/a) > 0 for b > 0 ✓ (the 1/ln2 terms genuinely cancel; the derivative of a log₂a is log₂a + 1/ln2, correctly quoted). g is C¹ on [b,∞) for b > 0, so g(a) ≥ g(b) = 0. Applying at integers a = |W₊|, b = |W₋| is legitimate since the claim is for all reals a ≥ b. **Accepted.**
- **Equality cases (Remark 5.1).** Subcube of codimension |I|: each i ∈ I contributes exactly |W| boundary i-edges (every point of W has its i-neighbour outside W, and each such edge is counted once), free directions contribute none; |W||I| = |W|log₂(2^n/|W|). Correct, and explicitly declared not used downstream. **Accepted.**
- All three n=2 sanity checks recomputed and correct.
- **Verdict on Lemma 3: complete and correct**, base case present, induction well founded, no equality-case sleight of hand.

### §6 Lemma 4
- S = ∅ branch: empty sum = 0 = ½log₂(1/1). **Accepted.**
- (4.1): ∑_u w(u) = |P|; w(u) ≥ 1 ⟺ u ∈ π_S(P). **Accepted.**
- Step 1 (4.2): for i ∈ S the grouping of window i-edges by their S-projection is a *bijection* onto (S-cube i-edge, v) pairs, so the displayed b_i(P) identity is an equality; the inner count is |V_u △ V_{u'}| ≥ ||V_u|−|V_{u'}|| = |w(u)−w(u')|. Summing over i ∈ S and using that each S-cube edge is an i-edge for exactly one i ∈ S gives ∑_{i∈S}b_i(P) ≥ TV_S(w). **Index bookkeeping checked: no edge double-counted, none missed.** **Accepted.**
- Step 2 (4.3) layer cake: |c−c′| = ∑_{t≥1}|1[c≥t]−1[c′≥t]| (the summand is 1 for exactly the |c−c′| values of t in (min,max]); the interchange is of two *finite* sums (t ≤ t_max, edges finite), so no interchange justification is owed. An edge contributes to the t-th term iff exactly one endpoint is in L_t, giving ∑_t|∂_EL_t|. **Accepted.**
- Step 3: L_t ≠ ∅ for 1 ≤ t ≤ t_max (any maximiser of w lies in it) — the nonemptiness hypothesis of Lemma 3 is checked, not assumed. L_t ⊆ L_1 = π_S(P) ⇒ log₂(2^s/|L_t|) ≥ log₂(2^s/|π_S(P)|), and the prefactor |L_t| ≥ 0 makes the substitution valid in the right direction. ∑_{t=1}^{t_max}|L_t| = ∑_u w(u) = |P|. **Accepted.**
- Assembly: (4.2)+(4.3)+(4.4) gives (4.0); dividing by 2|P| > 0 and substituting Lemma 1 (legitimate since S ⊆ J, so Lemma 1's i ∈ J branch applies to every i in the sum) gives the influence form. **Accepted.**
- Both sanity checks recomputed (singleton with S=J: both sides |J|/2; diagonal: 1/2 ≥ 0).

### §7 Lemma 5
- Lemma 2 gives disjoint projections *and* S ≠ ∅. **Accepted.**
- Disjoint nonempty subsets of {±1}^S ⇒ |π_S(P)|+|π_S(Q)| ≤ 2^{|S|} ⇒ ν_P+ν_Q ≤ 1 ⇒ (AM–GM) ν_Pν_Q ≤ 1/4. **Accepted.**
- Lemma 4 applied twice (hypotheses S ⊆ J and S ⊆ K both hold), summed: ½log₂(1/ν_P) + ½log₂(1/ν_Q) = ½log₂(1/(ν_Pν_Q)) ≥ ½log₂4 = 1. Note ν_P, ν_Q > 0 since the patterns are nonempty, so no log of zero. **Accepted.**
- Remark 7.1 tightness verified.

### §8 Lemma 6 (the counting step — read hardest)
- Finiteness of m, n, N ⇒ all interchanges valid, as stated. **Accepted.**
- Per-pair payment: A_a ∩ B_b = ∅ for **every** (a,b) — this is the hypothesis, and it is used for every pair, not on average. Lemma 5 gives ∑_{i∈S_ab}[Inf_i(f_a)+Inf_i(g_b)] ≥ 1 for each pair. **Accepted.**
- Weighting: multiply by p_aq_b ≥ 0 and sum; ∑_{a,b}p_aq_b = 1 (product of two probability vectors), so the RHS is 1, not something smaller. **This is the load-bearing "linearity of expectation" step, and the index sets are right:** the outer sum is over supp**F** × supp**G**, the inner over S_ab ⊆ [N]. **Accepted.**
- Σ₁ bound: S_ab ⊆ K_b and Inf_i ≥ 0 ⇒ enlarging the inner index set from S_ab to K_b increases the sum (direction correct). Then the sum over a is *inside*, giving ∑_a p_a Inf_i(f_a) = **E**_**F**[Inf_i] ≤ δ_F for each i ∈ K_b — i.e. the average-influence hypothesis is applied *per coordinate*, exactly as contracted, and the b-sum then contributes |K_b| coordinates each. Σ₁ ≤ δ_F ∑_b q_b|K_b|. I re-derived this exchange of order explicitly; it is correct. **Accepted.**
- Σ₂ symmetric via S_ab ⊆ J_a. **Accepted.**
- (6.1) ⇒ (6.2): ∑_b q_b|K_b| ≤ d and ∑_a p_a|J_a| ≤ d (convex combinations of numbers ≤ d), multiplied by δ_F, δ_G ≥ 0 — nonnegativity is needed here and is available. Then δ_F+δ_G ≤ 2max ⇒ max ≥ 1/(2d). **Accepted.**
- **No union bound over an unbounded index anywhere.** The only sums are over the two finite supports and over windows of size ≤ d; the support sizes m, n never appear in any bound, and N appears in no bound. This is the pattern I probed hardest for and it is absent.
- Remark 8.1's mathematical content verified (see finding O-1 for its editorial content).

### §9 Theorem
- Admissibility of the witnesses checked: c₁ = 1/3 ∈ (0,1], c₂ = 1 > 0, δ(d) = 1/(3d) ∈ (0,1/3] ⊆ (0,1], and δ(d) ≥ c₁d^{−c₂} with equality. **Accepted.**
- Supports nonempty (finitely supported probability distribution). **Accepted.**
- Contradiction hypothesis ⇒ cross-disjointness: for normalized indicators f(x)g(x) = 1_A(x)1_B(x)/(‖1_A‖₂‖1_B‖₂) is **strictly positive** on A∩B and 0 elsewhere, so "f(x)g(x)=0 for all x" is *equivalent* to A∩B = ∅ (no sign cancellation is possible — this is exactly where the indicator restriction of the rung is used, and it is used correctly). **Accepted.**
- Lemma 6 (6.2) then gives max(δ_F,δ_G) ≥ 1/(2d) while the hypothesis gives ≤ 1/(3d); 1/(2d) > 1/(3d) for every d ≥ 1. **Accepted.**
- Remark 9.1 (0 ∈ ℕ conventions): d=0 gives class {f ≡ 1} with f·g ≡ 1 ≠ 0; N=0 gives a one-point cube, vacuous influence hypothesis, class {f ≡ 1}. Both correct; both quarantined as convention handling, not load-bearing under the artifact's own ℕ = {1,2,…}. **Accepted.**

### §10 Remark 10.1 (declared non-load-bearing)
- Grid construction: N = d², rows/columns as windows of size exactly d, singleton patterns, all in 𝒞^junta_d. Distinctness of the f_r and g_c argued correctly. **Accepted.**
- Incompatibility: f_r(x)g_c(x) ≠ 0 would force x_{(r,c)} = −1 and = +1. **Accepted.**
- Influences: b_i(P_r) = 1 for i ∈ J_r (singleton in a d-cube), Lemma 1 gives 1/2; uniform mixing over d rows gives E = 1/(2d) at every coordinate, since coordinate (r′,c′) lies in J_r only for r = r′. Recomputed. **Accepted.** Consequence (no δ ≥ 1/(2d) witnesses I01) is correct, and consistent with I01's "Grid ceiling" line and card S1.
- See finding D-1 for the one-word attribution imprecision.

### §11–12 Gap register / dependencies
- The gap register's "Empty" is consistent with what I read: Lemma 3 is the only potentially borrowed ingredient and it is proved from scratch in the exact weak form used (not Harper's exact theorem, which is not needed). No step cites an external result for justification. **Accepted.**
- §12's scope discipline (δ never depends on N; average not max influence; windows ≤ d; exact non-vanishing; establishes R1 only) matches what the proof actually does. **Accepted.**

---

## 6. COMMON-FAILURE-PATTERN SWEEP (explicit)

| Pattern | Where it could have bitten | Finding |
|---|---|---|
| Quantifier order swapped / "sufficiently large" dropped | §9 Theorem | Clean; witnesses are absolute constants fixed before d, N, **F**, **G**; no asymptotics anywhere (the Contract says "None. Nothing tends to infinity") |
| Union/probability bound over an unbounded index | Lemma 6, the a,b double sum | **Absent by construction**: the double sum is a *weighted average* with total weight 1, not a union bound; m, n never appear in any estimate |
| Worst-case vs expected conflated | δ_F := max_i **E**_**F**[Inf_i] | Correct: max over the *finite coordinate set*, expectation over the *distribution*. The forbidden max-over-support reading is nowhere used — I checked Lemma 6's Σ₁ step specifically, where a max-over-support proof would have been easier and is not what is written |
| Asymptotic standing in for an explicit constant | δ(d) = 1/(3d) | Explicit; the rung asks for explicit c₁,c₂ and gets them |
| Lost reduction/hybrid factor | Lemma 5 → Lemma 6 routing | Accounted: the per-pair payment 1 is routed through the *partner's* window budget, and the factor d is carried explicitly into (6.2). The final 3/2 slack (1/(3d) vs 1/(2d)) is stated, not hidden |
| Independence assumed but not shown | the product weights p_aq_b | No independence is *assumed* about **F**,**G**; p_aq_b is the artifact's own choice of weights for averaging a family of *deterministic* inequalities, one per pair, each of which holds unconditionally. Legitimate |
| Limit / sum–integral / expectation interchange unjustified | (4.3) layer cake; Lemma 6 reordering | Both are finite sums, and the artifact says so. No justification owed |
| Negligible/measure-zero exception treated as empty | none applicable (all objects finite) | n/a |
| Induction with missing base case or premature invocation | Lemma 3 | Base n = 0 present; IH invoked only at n−1 and only on nonempty halves (the b = 0 case invokes it on W₊ only) |
| Object constructed but not shown to satisfy every property | the grid in Remark 10.1; the glue point in Lemma 2 | Both fully checked (class membership, window size, distinctness, influence level; and x_J ∈ P *and* x_K ∈ Q respectively) |
| Degenerate/vacuous reading of the class or the conclusion | 𝒞^junta_d with P = ∅; S = ∅; constant functions; empty supports | All four discharged explicitly (§1 well-definedness; Lemma 2; Lemma 2's constant-function line; §9's nonempty-support line) |

---

## 7. SOURCE REQUEST

**None.** The artifact uses no external result: card S1 is invoked once, in a
declared non-load-bearing remark, as provenance only, and I was able to check
that mention against the card already held (see D-1). No class-(E) finding
arises, so nothing blocks acceptance on library grounds.

### END OF ARTIFACT 0023-prover-1-verify-D ###
