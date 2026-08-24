# Collated referee findings — split-decomp-kappa-2

One referee pass, blind: fresh context, no project context, judging only the
artifact, the Contract, r3 as a supplied dependency, and the source cards. The
artifact reviewed is the committed `split-decomp-kappa-2.md` as of `8c68c62`,
i.e. **after** the two in-session smell-test repairs of #140, so none of these
findings restates one of those.

Transcribed in substance by the audit operator, who has ruled on nothing.
Rulings are in `split-decomp-kappa-2-triage.md`.

Verdict: **DEFECTS**. Six findings of class A, B or D, plus a group of routine
class C items. No load-bearing class E: every citation was reachable and the
cards covered the external results, so there is no source request.

## Package note

The pre-existing staged package at `split-decomp-kappa-2-audit-files/` was NOT
used. Its `ARTIFACT.md` predates #140, and it omits r3, which the artifact needs
because it does not repeat its definitions and inherits r3's Lemma P and
Theorem C without reproving them. A referee given that package must return a
load-bearing (E) on the inherited results and stop. r3 was therefore supplied,
with instructions to treat it as an external citation and check hypothesis by
hypothesis, and to note that r3 has itself never been blind-verified.

---

## F1 (A) — statement drift

§0: "closes it on a region that **strictly contains** the region r3 covered for
unrestricted observers." Not established. At q = 0 every observer has challenge
resolution 1 vacuously, so r3's Theorem C′ branch 1 covers all M at q = 0,
whereas Theorem E there requires M ≤ σ'/(4δ). Non-vacuous. The artifact concedes
the point elsewhere ("the old arm survives only at q = 0"; "The first branch is
dropped, not subsumed"), so §0 is inconsistent with §§6–7.

## F2 (D) — citation defect

§7 Corollary E′ reports r3's Theorem C′ hypothesis as "either D has challenge
resolution 1, or M ≤ σ'/√(27δ)". r3 requires "resolution 1, or **the hypothesis
of Corollary B′**", of which M ≤ σ'/√(27δ) is only a sufficient condition. B′'s
hypothesis is strictly weaker: its second arm exceeds σ'/√(27δ) by √(σ'q/27)
whenever σ'q > 27, and at q = 0 its first arm holds for every M. So the
containment is proved against the wrong baseline and the advertised
1.299·q⁺/√δ enlargement is measured against a region smaller than r3 covers.
Theorem E itself is not implicated.

## F3 (A) — unlicensed impossibility claim

§0 item (F) and the bold sentence inside §8's "Three consequences" assert that no
q-free bound can improve the M-dependence. Proposition F is a single family with
δ = 1/N exactly and σ' = 2 log N, so it pins the exponent and coefficient only
along that diagonal. It excludes nothing of the form δ√M·φ(Nδ) with φ(1) = Θ(1)
and φ decaying for Nδ ≫ 1. The "factor 12" tightness likewise holds only at
δ = 1/N. The "On this family" version is correctly hedged.

## F4 (B) — false comparison

§0 item (A⁺, B⁺) and §6: "smaller in both terms whenever δ < 1". False. At
σ = 0, N = 2, δ = 0.9 the replacement gives 6.8369 against 6.708. The claim
ignores the additive √(2δ ln(eN)).

## F5 (B) — false arithmetic in a justification

§6 Corollary D″ parenthetical: "1.302√(σ'δ) + 3.21δ√σ' + δ ≤ 4.9√(σ'δ)". False:
the coefficients sum to 5.512, and at δ = 1, σ' = 2 the LHS is 7.381 against
6.930. γ₀ = δ is already absorbed into the 3.21, so "+δ" double-counts.

## F6 (A) — under-qualified restatement

§7 Corollary E′'s union sentence states the conjecture holds "for (i) every
observer when M ≤ σ'q⁺/(4δ), and (ii) every resolution-1 observer for arbitrary
M", dropping the standing hypotheses P ≤ √(σ'/δ) and q⁺δ ≤ σ'. Recoverable from
the same paragraph, but this is the quotable sentence.

## Routine (C), reported without forcing the verdict

Lemma 0's de-duplication is asserted rather than argued, and it is what makes the
strategy image finite and forces halting in the unbounded case. Lemma 0's
(Real, Dec) clause leaves the family 𝒴 implicit. §3 and §4 cross-reference §7
where §8 is meant. §8's "advantage at least 1/8" holds for even N only.

## What the referee accepted

The unbounded-query case of (D) is supported. Theorem E's region is exactly as
stated, is a two-sided window in q, and is the Contract's conjecture rather than
the weakened reading. Proposition F's construction satisfies every property it
needs and the direction of its lower bound is correct. Lemma 0 clause (iii)'s
quantifier structure matches its proof. Every concentration and counting step
verified, including that the 2^M tests are paid for exactly by M ln 2 in C₁, and
the binomial fourth moment. Cards used within their stated hypotheses.

## Inherited dependency, as confirmed against §9

Theorem E and Corollary E′ are correct only if r3's Theorem C and Lemma P are
correct; Lemma P transitively carries CDGS Claims 2 and 3. Theorems A⁺, B⁺ and
the first arm of Corollary D″ are correct only if r3's Lemma 3 steps (1)–(3) and
Lemma 4 are correct. Theorem D, Corollary D′ and Proposition F are independent
of r3. **r3 has never been blind-verified.**
