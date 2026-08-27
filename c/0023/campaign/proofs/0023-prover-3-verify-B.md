id: 0023-prover-3-verify-B
agent: verifier
model: claude-sonnet-5
cycle: 3

# Verification report on 0023-prover-3.md

## 1. FINAL VERDICT

CLEAN (no class A/B defects found after full independent re-derivation of both
witness influence tables, both caps, the localisation/master-count framework,
the scope/monotonicity direction, and the escape ruling in exact arithmetic);
one non-load-bearing (D) citation mischaracterisation and one unindependently-
re-derived (C) group-generalisation step are noted below and should be fixed
or flagged, but neither undermines any claimed result.

## 2. FINDINGS TABLE

| # | Location | Class | Explanation |
|---|---|---|---|
| 1 | DEPENDENCIES table, row "S7b ... a maximum-degree monomial support has size ≤ deg" and §7.1 "(\|W_sh\|≤d **by theorem**, card S7b...)" | D (citation defect, non-load-bearing) | Card `S7-changfang26-card.md`/`S7b-changfang26-addendum` establishes Chang–Fang's **Theorem 1.2** (a *shattering*/full-projection statement: `supp(f)` shatters `S^c` for `S` a maximum-degree monomial set) and **Corollary 3.4** (the group-uniform version). Neither states, nor is needed to state, "a maximum-degree monomial support has size ≤ deg" — that fact is an immediate consequence of the *definition* of degree (`deg(f) = max{|S| : α_S≠0}`, already fixed in the Contract), requiring no citation at all. The artifact itself concedes this a line later ("the projection property is not used"), so the citation is both mischaracterised and unnecessary for the claim it is attached to. This does not affect correctness: `|W_sh(A)|≤d` is true regardless of any citation, and no other use of S7/S7b (which the artifact correctly reserves as an unused, honestly-flagged lead in §8/GAP REGISTER) is load-bearing to any proved theorem. Recommend: cite nothing here, or replace with a one-line self-contained remark. |
| 2 | §6.2, "refuter-3 §5.1's 1/(8d) forcing bound" vs. the artifact's own inline recomputation "$\pi_W\ge\frac12+\frac12=1$ and $|W|\le d$ ... giving $\ge\frac1{2d}$" | note, non-blocking | The artifact's own master-count computation for `W_Forced` restricted to forcing pairs yields `≥1/(2d)`, a *better* (larger) constant than the "1/(8d)" figure attributed to refuter-3 in the campaign VERDICT summary and §6.2's heading. This is not a contradiction (any witnessed threshold ≤1/(2d) is consistent with both being true simultaneously — refuter-3 may have accepted a looser constant for an unrelated reason), but refuter-3 is outside my permitted file set, so I cannot independently confirm the "1/(8d)" number; recorded as unverifiable, not load-bearing to any of this artifact's own claims (its self-contained derivation of ≥1/(2d) stands on its own). |
| 3 | §5.4, "*CAP I* holds for ℤ₂ and, by pullback along a surjection φ:𝒴→ℤ₂ ..., for every **even-order** group" | C (justification gap, minor, non-blocking) | The pullback claim ("preserves degree, all coefficients, all influences, α and disjointness") is asserted with one parenthetical justification, not spelled out. It is a standard and plausible technique (precomposing a ℤ₂ witness with a surjective group homomorphism), and [G2] already correctly flags the *complementary* gap (odd-order groups are NOT claimed), which is independent evidence the artifact is being honest about scope rather than overclaiming. I was not able to fully re-derive the pullback in the time available; flagged for a future pass, not upheld as an error. |

No class A (statement drift) or class B (critical/broken step) defects found. No class E (unverifiable, load-bearing) findings: both cards actually needed (S6 family, S7/S7b) were locatable and read in full (`S6-junta-degree-card.md`, `S7-changfang26-card.md`, including the appended `S7b` addendum), and neither S6a (explicitly marked [RESTATED] by the artifact's own dependency table) nor S7/S7b is load-bearing to any proved theorem — T4(c) (the influence-quantum floor $2^{-d-1}$), which is the fact S6a would have supplied, is **proved from scratch inline** in the artifact (T4(a)+T4(c)'s derivative argument), exactly as the artifact itself states ("no [RESTATED] item is load-bearing").

## 3. STEP-BY-STEP LOG

**STEP 0 (completeness).** Artifact ends with `### END OF ARTIFACT 0023-prover-3 ###`; no mid-sentence/mid-proof truncation. PASS.

**STEP 0.5 (negation check).** For each load-bearing lemma below I checked whether the artifact (or a natural reading of its machinery) could also be made to support the negation; no case of both a lemma and its negation being accepted was found (no hard-stop contradiction). Specific checks: (i) CAP I's inequality at the address witness was independently re-derived in exact rational arithmetic and could not be made to fail; (ii) CAP II's inequality at the subcube witness likewise; (iii) the "own-heavy at θ" hypothesis is correctly a *fixed, θ-uniform-across-A* constraint (not silently re-scoped per-object), so T8's derivation and its would-be negation (own-heavy at a smaller θ escaping the cap) are exactly delineated by T9's dichotomy, itself independently verified — no overlap/contradiction found.

**Adjudication tags (load-bearing lemmas).**
- T1 (master count): **NONE** — proved inline, elementary, independently re-checked.
- T2 (value theorem): **NONE** — proved inline.
- T3 (localisation ceiling): **NONE** — proved inline; independently re-checked that it extends to Remark 2.2's randomised windows (pointwise bound survives expectation).
- T4(a)–(d) (non-vanishing / floor): **NONE** — proved inline; (c) explicitly re-proves card S6a's content rather than citing it (S6a itself is tagged RESTATED/BLOCKED-on-the-1994-print, and is correctly *not* relied on).
- T5 (address-pair table): **CODE** — cross-checked by hand in exact rational arithmetic for general $k$ and against the printed $k=1,2,3$ numerics (`check_witnesses.py`); every entry ($\alpha=1/2$, $|{\rm Rel}|=2^{d-1}+d-1$, $\mathrm{Inf}_{a_t}=1/4$, $\mathrm{Inf}_{y_j}=2^{-k-1}$, $\pi_{\rm Rel}=(d+1)/2$, and the quoted ratios $1/4,5/24,13/64$ / $1/4,1/6,5/44$) reproduced exactly.
- T6 (CAP I): **NONE** — derived correctly from T3+T5; re-verified the three corollaries (a)/(b)/(c)'s arithmetic (the key inequality $2^{d+1}\le 4(2^{d-1}+d-1)\iff d\ge1$ checked).
- T7 (subcube-pair table): **CODE** — re-derived $\mathrm{Inf}_i(f_C)=1/2$, $\mathrm{Inf}_i(f_D)=1/(2(2^d-1))$, and $\pi_{\rm Rel}$ from scratch; reproduced the printed $d=2..6$ table exactly (e.g. $d=4$: $\pi_{\rm Rel}=32/15$).
- T8 (CAP II): **NONE** — proved inline; re-verified the own-heavy⇒$W(D)=\emptyset$ step depends essentially on the **strict** inequality $\theta>1/(2(2^d-1))$ (the boundary case $\theta=$ threshold, realised exactly by $W_{\rm sh}(D)=[d]$ on witness (b), is correctly excluded — this is why P1 genuinely escapes CAP II there, not a technicality that a $\ge$ vs $>$ edit would erase; I checked both directions explicitly).
- T9 (dichotomy): **NONE** — arithmetic re-verified exactly ($\ge1/(2(w_C+w_D))\ge1/(4d)$ when $w_D\ge1$).
- §7.1–7.2 (P1 escape + non-canonicity theorem): **NONE**, self-contained (the automorphism $\sigma_c$ was re-verified to fix $A_k,B_k$ setwise and act transitively on targets; the S7b citation attached to the trivial size fact is the (D)-defect above, not load-bearing to the escape conclusion, which needs only $|W_{\rm sh}(A)|=\deg(A)\le d$, true by definition).
- §7.4–7.5 (P5 escape + drafting warning): **NONE**, self-contained (explicit certificates on both witnesses; S3a/S3b/S6c's $O(d^4)$ bound explicitly disclaimed as unneeded).
- §5.2 (monotonicity direction): **NONE** — re-derived; confirmed the direction is *caps propagate up (superclass), never down (subclass)*, correctly used in §6.1 to exempt frozen I01/R1 (witness (a) has $|\mathrm{Rel}|=2^{d-1}+d-1>d$, hence is not a member of $\mathcal C^{\mathrm{junta}}_d$, so CAP I cannot and does not condemn R1).
- §5.4 (group generalisation): **NONE** claimed, but flagged (C) above for the even-order pullback step, not independently re-derived by me to the same standard as everything else.
- §8 (frontier / η*): **NONE** — the one-directional "if $\eta^*=2^{-\Theta(d)}$ then everything capped" is an immediate corollary of T3 (already verified) applied uniformly; the converse is explicitly and correctly disclaimed, and the "(PAY⋆) at $p=1$ forces $\eta^*=1$" claim is correctly stated as conditional on an unestablished external hypothesis, not asserted as proved.

**Class-definition-drift check (task's directive #1).** D4's literal three-clause definition (fix a per-function localised window; prove a pointwise payment inequality in terms only of window sizes; conclude via linearity of expectation using only $\delta_{\mathbf F},\delta_{\mathbf G}$ and window sizes) was checked against: (a) the junta-substitution route (uses $W=\mathrm{Rel}$ or $W$ = the Nisan–Szegedy-type junta window) — this literally instantiates T1–T3, so Corollary 3.2's condemnation is a correct application, not a definition tailored after the fact; (b) P1/P5 — checked directly that their windows are localised (required) and that neither invokes anything beyond D4's own machinery for the *master-count* step (P1 uses an external theorem only to note $|W|\le d$, a fact not even needed since it is definitional; P5 uses Remark 2.2's randomised extension, explicitly built into the framework, not smuggled in) — so their escape is a genuine consequence of the caps' hypotheses (relevance-density / own-heaviness) failing on the witnesses, not of D4 secretly excluding them; (c) R1/I01 and refuter-3's $1/(8d)$ bound — both correctly and independently shown to sit *outside* the two caps' hypotheses (R1's class doesn't contain witness (a); refuter-3's forcing-pair restriction removes witness (b) as an admissible instance since $\mathrm{Forced}(D)=\emptyset$ there). No case found where the class, as literally written, contains a known-successful argument while the prose claims exclusion, or vice versa. No class A drift.

**Scope/monotonicity check (task's directive #4).** Re-verified both directions independently (see §5.2/§6.1 above): caps proved via a witness inside $\mathcal C^{\mathrm{ind}}_d$ propagate to every superclass containing that witness (immediate from $V^{\mathcal C'}\le V^{\mathcal C}\le K$ for $\mathcal C\subseteq\mathcal C'$), and do **not** propagate to any subclass not containing the witness — correctly used to exempt R1, not to falsely condemn it. No inversion found.

**Escape-ruling check (task's directive #5).** T8+T9 jointly and rigorously establish that "sum rather than min" is *insufficient* on its own: any own-heavy functional (sum-form, T8's proof does not use $\min$ anywhere) is still capped, so the true necessary pair of conditions the artifact's own proofs actually use is (α) a window-size bound not derived from the relevance count (used verbatim in §7.1/§7.4 via triviality/definition, not derived from a payment argument) and (β) willingness to include own-cheap coordinates (verified directly: $W_{\rm sh}(D)=[d]$ on witness (b) includes every coordinate of $D$ despite each being at the minimal influence value). This is proved, not merely asserted, and the artifact correctly disclaims the converse (§8.3).

## 4. SOURCE REQUEST

None. Both cards this artifact cites as load-bearing (S6 family, S7/S7b) were located at `c/0023/campaign/sources/S6-junta-degree-card.md` and `c/0023/campaign/sources/S7-changfang26-card.md` (the latter contains the S7b addendum inline) and read in full; neither is misapplied in a way that affects a proved result (see Finding #1 for the one mischaracterisation, which is non-load-bearing).

### END OF ARTIFACT 0023-prover-3-verify-B ###
