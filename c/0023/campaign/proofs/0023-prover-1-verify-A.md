id: 0023-prover-1-verify-A
agent: verifier
model: claude-sonnet-5
cycle: 2

# Verification report: 0023-prover-1 (I01, rung R1)

## 1. FINAL VERDICT

CLEAN (modulo one PEDANTIC-grade cross-reference slip): the artifact proves
exactly the I01 rung statement (δ(d)=1/(3d), c1=1/3, c2=1, for all d,N,
finitely-supported F,G over 𝒞^junta_d, δ independent of N) with no statement
drift, no broken step, and an empty gap register that is in fact empty; every
inequality — including the inline entropy-form edge-isoperimetric induction
(Lemma 3) and the linearity-of-expectation double-counting argument
(Lemma 6) — was independently re-derived line by line and is correct, and
the whole lemma chain is cross-validated by an exact tightness witness
(Remark 10.1's grid construction saturates Lemmas 1, 4, 5, 6 simultaneously
with equality), which is strong evidence against a sign/constant error
anywhere in the chain.

## 2. FINDINGS TABLE

| Location | Class | Explanation |
|---|---|---|
| §4, Lemma 2, "(Degenerate case S=∅.)": "by the first direction, A∩B≠∅" | C | Mislabeled internal cross-reference. The paragraph proved first is the "(⇐, via contrapositive)" direction, whose content is "x∈A∩B ⟹ projections intersect" — that does *not* license concluding A∩B≠∅ from intersecting projections. The needed fact (intersecting projections ⟹ construct x∈A∩B) is the content of the *second*, "(⇒, via contrapositive)" paragraph (the explicit gluing construction), applied with S=∅. The correct justification is present verbatim one paragraph above in the same lemma, so this does not affect soundness of Lemma 2 or anything downstream — Lemma 2 itself is correct — but as written the cited justification does not support the claim. |
| Whole artifact | — | No other defect found after full line-by-line re-derivation (see log). No Class A (statement drift), B (critical error), D (citation misuse), or E (unverifiable) items found. |

## 3. STEP-BY-STEP LOG

STEP 0 (completeness): artifact ends with `### END OF ARTIFACT 0023-prover-1 ###` (line 526); not truncated. Proceeding to full review.

STEP 0.5 (negation check): performed throughout by testing each load-bearing lemma against its own stated/constructible tight examples (a wrong direction or a wrong constant would necessarily be *violated*, not merely loose, at a tight example). Result: no lemma's negation is supportable; every tight example saturates the stated inequality with equality (see below), which is inconsistent with a sign flip or misplaced constant anywhere in the chain. No CONTRADICTION found.

Class (A) check (statement drift), done first: the artifact's §0 "Statement proved" and §9 Theorem are transcribed verbatim identical to I01's Statement block (same quantifier order: ∃c1,c2,δ first, independent of N; ∀d,N,F,G with the *average*, per-coordinate influence hypothesis — not max-over-support, not summed over i; ∃f,g,x with f(x)g(x)≠0, exact non-vanishing). δ(d)=1/(3d) is independent of N throughout the whole derivation (Lemma 6's bound depends only on d via |J_a|,|K_b|≤d, never on m,n,N). No drift found.

- Lemma 1 (Inf formula): Step 1 (orthonormal Fourier basis + Parseval) — standard, correctly derived from independence of coordinates under uniform measure. Step 2 (flip identity, Inf_i(f)=¼E[(f(x)-f(x^⊕i))²]) — correctly derived via Parseval applied to the difference function. Step 3 (edge-count formula for a normalized indicator) — correctly computes the squared difference and the size of its support via disjointness of i-edges. Step 4 (junta lift) — correctly computes |A|=|P|2^{N-|J|} and the i∈J / i∉J cases via the edge-lifting bijection. Verified against a known fact: singleton pattern gives Inf_i=1/2 (classical AND influence), matches. ACCEPTED.
- Lemma 2 (disjointness ⟺ projection disjointness): both directions correctly proved by contrapositive; the (⇒) direction's gluing construction (partition of [N] into J, K\J, complement) is correct and checked coordinate-by-coordinate. Degenerate S=∅ case: conclusion correct, but see Class-C finding above on the cross-reference. ACCEPTED with the noted (C).
- Lemma 3 (hypercube entropy-form isoperimetry, proved by induction): base case n=0 checked (0=0). Inductive step's exact edge partition (facet edges vs. direction-n edges) verified to be an exact, exhaustive, disjoint decomposition of the n-cube's edge set. Case b=0 algebra checked exactly (a·log2(2^{n-1}/a)+a = a·log2(2^n/a)). Case b≥1: reduced the required inequality to g(a)=(a+b)log2(a+b)-a log2 a - b log2 b - 2b ≥ 0 for real a≥b>0; independently recomputed g(b)=0 and g'(a)=log2((a+b)/a)>0, confirming g increasing hence ≥0 on [b,∞). Re-verified numerically at n=2 (|W|=1,2,3) and independently at n=3, |W|=2 (antipodal pair, 6 ≥ 4). Equality (Remark 5.1) matches subcube structure exactly. ACCEPTED, no gap.
- Lemma 4 (projection-density payment): S=∅ case trivial (0=0), correctly handled. General case: Step 1's boundary/total-variation inequality (4.2) re-derived and correct (grouping i-edges of the window cube by S-projection, using |V_u△V_u'|≥|w(u)-w(u')|). Step 2's layer-cake identity (4.3) re-derived and correct (standard integer identity |c-c'|=Σ_t|1[c≥t]-1[c'≥t]|, checked directly). Step 3's per-level application of Lemma 3 and the monotonicity step (L_t⊆π_S(P) ⟹ smaller argument of log) correctly chained; Σ_t|L_t|=|P| verified via double counting. Assembly is a correct chain of three inequalities/identities. Independently verified tightness: singleton P at S=J gives exact equality (LHS=RHS=|J|/2), matching Lemma 3's subcube-equality case exactly (a genuine cross-check the constants haven't drifted). ACCEPTED.
- Lemma 5 (per-pair payment ≥1): uses Lemma 2 to force S≠∅ under the disjointness hypothesis (so no division-by-zero / undefined-log issue arises when Lemma 5 is actually invoked in Lemma 6). AM–GM step ν_P·ν_Q ≤ ¼ re-derived correctly from ν_P+ν_Q≤1. Two instances of Lemma 4 added correctly. Tight example (Remark 7.1) re-verified by hand: Inf_1(f)=Inf_1(g)=1/2, sum=1, exact equality. ACCEPTED.
- Lemma 6 (master count): re-derived the double sum manipulation (6.3) term by term; the two "enlarge index set" bounds (S_ab⊆K_b and S_ab⊆J_a, using influence non-negativity) and the subsequent Fubini-type reordering of the finite triple sum (a,b,i) are valid and correctly executed (all index sets finite: m,n,N<∞ by the finitely-supported and given-N hypotheses; no unbounded-index union-bound issue, and crucially no factor of m,n ever enters the final bound — this is exactly what makes δ N/support-size independent, matching the Contract's binding requirement). The final chain (δ_F+δ_G)d ≥ δ_F·(Σq_b|K_b|) + δ_G·(Σp_a|J_a|) ≥ 1, using Σq_b|K_b|≤d, Σp_a|J_a|≤d and non-negativity, is a valid direction of inequality (verified explicitly: X≤d,Y≤d,δ_F,δ_G≥0 ⟹ δ_FX+δ_GY ≤ (δ_F+δ_G)d, combined with δ_FX+δ_GY≥1 gives (δ_F+δ_G)d≥1). Cross-validated against Remark 10.1's construction: δ_F=δ_G=1/(2d) exactly, giving (δ_F+δ_G)d=1 exactly — the master inequality is saturated with equality by an independently-checked example, strong evidence the constant 1/(2d) is exactly right (not off by a misplaced factor of 2 or 4). ACCEPTED.
- Theorem (§9): admissibility of c1,c2,δ trivially checked; contradiction argument correctly translates "conclusion fails" into "all support pairs disjoint" (using that f(x)g(x) for normalized indicators is >0 exactly on A∩B), correctly invokes Lemma 6, and correctly derives 1/(2d) ≤ max(δ_F,δ_G) ≤ 1/(3d), a genuine contradiction since 1/(2d)>1/(3d) for all d≥1. ACCEPTED.
- Remark 3.1 (automatic degree bound): flip-parity argument (f̂(T)=-f̂(T)=0 for T⊄J) correctly derived; non-load-bearing but correct.
- Remark 9.1 (ℕ∋0 convention): non-load-bearing side note; checked and internally consistent (d=0 class is {f≡1}, N=0 cube is a point) whichever convention is used.
- Remark 10.1 (tightness, non-load-bearing): construction (uniform mixtures of single-row / single-column point-pattern indicators) correctly shown pairwise-incompatible and to carry average influence exactly 1/(2d); independently recomputed and matches. Non-load-bearing per the artifact's own gap register, and I used it above purely as a corroborating cross-check on Lemmas 1/4/5/6, not as part of the proof itself.
- Gap register / Dependencies (§11–12): confirmed empty and accurate — no external result, card, or refuter computation is used as justification anywhere in the load-bearing chain (S1 appears only in the non-load-bearing Remark 10.1, correctly tagged CARD/context-only there).

## Adjudication tags (load-bearing lemmas)

All load-bearing lemmas (Lemma 1, Lemma 2, Lemma 3, Lemma 4, Lemma 5, Lemma 6, and the Theorem) are tagged **NONE**: each is verified by direct inline mathematical re-derivation by hand; none rests on executed code (CODE), a mechanized/formal proof (MECH), or an external source card (CARD). The one mention of card S1 (in Remark 10.1) is explicitly non-load-bearing and correctly tagged as context by the artifact itself.

## 4. SOURCE REQUEST

None. No external result is cited as justification for any load-bearing step; both source cards (S1, S2) were read and are consistent with the artifact's (non-load-bearing) mention of S1.

### END OF ARTIFACT 0023-prover-1-verify-A ###
