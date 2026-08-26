# Triage rulings — split-decomp-kappa-2

**6 UPHELD / 0 OVERRULED / 1 PEDANTIC (the class C group) / 0 NEEDS-SOURCE.**
Findings as collated in `split-decomp-kappa-2-findings.md`. Ruled by a handling
editor in fresh context, checking each finding against the artifact, the Contract
and r3 directly rather than taking the referee's quotations on trust.

**None of the six is load-bearing.** No hypothesis, proof step or conclusion of
Lemma 0, Lemmas A/B/C, Theorem D, Corollary D′, Theorem E or Proposition F is
wrong, and no case was constructible in which an accepted result fails. All six
are false or unlicensed claims *about* what was achieved, or arithmetic inside a
justification.

| id | ruling | load-bearing? | reason |
|---|---|---|---|
| F1 | **UPHELD** | no | Verified against r3 directly. Both branches of r3's Theorem C′ are satisfied at q = 0: resolution 1 holds vacuously, and B′'s first arm is unbounded there. So r3 covers all M and all observers at q = 0, while Theorem E requires M ≤ σ'/(4δ). Non-vacuous: at σ' = 2, δ = 10⁻³, Theorem E's threshold is 500 while r3 covers every M and 8√(σ'δ) = 0.36. The regions are incomparable, not nested. Class A, so not eligible for PEDANTIC. |
| F2 | **UPHELD** | no | r3's hypothesis is "resolution 1, or the hypothesis of Corollary B′", of which M ≤ σ'/√(27δ) is only the *in particular* clause. B′'s second arm exceeds it by exactly √(σ'q/27); its first arm is unbounded at q = 0. Mitigating, and nowhere argued in the artifact: B′'s arm 2 can exceed σ'q⁺/(4δ) only when σ'qδ > (27/4)²q⁺², which forces 8√(σ'q⁺δ) ≫ 1, so containment for q ≥ 1 does survive in every non-vacuous regime. At q = 0 it fails outright. Aggravating: the artifact's own §4 "Corollary B′" collides in name with r3's, which is plausibly how the slip arose. |
| F3 | **UPHELD** | no | What Proposition F licenses, exactly: at δ = 1/N, for M ∈ [2, N²/2], any valid bound is at least δ√M/(4√2), so Corollary D′'s M-exponent ½ and coefficient 2 are optimal to within 8√2 **along that diagonal only**. It licenses nothing off it. The referee mislocates the sentence — the bold claim is inside "Three consequences", not outside — but the substance is right. |
| F4 | **UPHELD** | no | Recomputed: at σ = 0, N = 2, δ = 0.9 the replacement gives 6.83693 against 6.70820. Worst crossover δ* = 0.8551 at N = 2, σ = 0. Mitigation, not cure: every violation has both sides ≥ 6.5, so no non-vacuous instance is harmed. The second-term claim μ'(q) ≤ qδ is correct. |
| F5 | **UPHELD** | no | The display is false (coefficients sum to 5.512; at δ = 1, σ' = 2 the LHS is 7.38093 against 6.92965), and the cause is the double-count: γ₀ = δ is already inside the 3.21. **The referee's inference that D″'s constant is therefore unjustified is OVERRULED**: deleting "+δ" gives 1.302 + 3.21 = 4.512 ≤ 4.9, so the first arm remains justified by the constants its own source proof supplies. The defect is the parenthetical's arithmetic and the fix is a deletion. |
| F6 | **UPHELD** | no | The union sentence is false read standalone, and it is the sentence a reader will lift. Class A, so PEDANTIC is unavailable however light the repair; one clause discharges it. |
| C group | PEDANTIC | no | Each is one clause or one cross-reference. §3's and §4's "§7" both mean §8. "At least 1/8" needs even N — at N = 3 it is 0.11785 — and is 1/8·√(1−1/N²) in general; the §8 conclusion is untouched. Lemma 0's de-duplication is the only item with weight, and is discharged by one clause: D′ simulates repeated queries from its own transcript, changing no output and lowering the count. |

## Minimum change set

All deletions or single qualifying clauses. **No new mathematics, and no proof is
to be touched — in particular Theorem E's region and Corollary D″'s constant are
correct as stated and must not be weakened.**

1. §0: replace "strictly contains" with incomparability plus enlargement for q ≥ 1, noting r3 covers all M at q = 0.
2. Corollary E′: quote r3's hypothesis as written, and either restrict the containment and 1.299·q⁺/√δ claims to the sufficient condition M ≤ σ'/√(27δ), or keep them against full B′ and add the one-line non-vacuity argument. State that containment fails at q = 0. Optionally rename §4's Corollary B′ to avoid the collision.
3. §0 (F) and §8's bold sentence: restrict to δ = 1/N. Delete the claim that a smaller test class, chaining or sharper concentration cannot help.
4. §0 (A⁺, B⁺) and §6: delete "smaller in both terms whenever δ < 1", or bound it by δ ≤ 0.85.
5. Corollary D″ parenthetical: delete "+δ", re-add as 1.302 + 3.21 ≤ 4.512 ≤ 4.9, noting γ₀ is already inside the 3.21.
6. Corollary E′ union sentence: reinstate P ≤ √(σ'/δ) and q⁺δ ≤ σ' on both clauses.
7. Pedantic, same pass: one clause for Lemma 0's de-duplication; name 𝒴 in Lemma 0's (Real, Dec) clause; §3 and §4 "§7" → "§8"; qualify "at least 1/8".

## Recommendation

**Freeze with prose corrections**, made before the freeze rather than logged as
future work. Three of the six (F1, F2, F3) are false or unlicensed claims about
what has been achieved, and F6 is the artifact's most quotable sentence: as it
stands the artifact advertises a strict enlargement of r3 that fails at q = 0,
measured against a hypothesis r3 does not have, and asserts an impossibility a
single δ = 1/N family cannot support. But the fixes require no new mathematics.

The inherited, unaudited dependency on r3 (Theorem C, Lemma P, Lemma 3 steps
(1)–(3), Lemma 4) is accurately registered in §9, is orthogonal to these
findings, and should stay flagged. **r3 is the next thing that needs blind
verification.**
