# Collated referee findings — split-decomp-kappa-1

Five referee passes, four completed with a VERDICT line, one aborted mid-report
(session limit) and therefore not a recorded verdict. Transcribed verbatim in
substance by the audit operator, who has ruled on nothing. Each entry preserves
the severity the raising pass assigned. Where passes disagree, the disagreement
is recorded rather than resolved.

Pass 1 = Opus, general-probabilistic. Pass 2 = Opus, targeted at Lemma P and the
G2->G3 coupling (ABORTED, no verdict). Pass 3 = Sonnet, adversarial construction.
Pass 4 = Sonnet, correspondence and source fidelity. Pass 5 = Fable, line-by-line.

---

## F1 — CONTESTED. Theorem C', first line of proof.

Raised SERIOUS by pass 1 and pass 2, independently. Logged MINOR by pass 3.
Not flagged by pass 5, which ruled Theorem C' PROVED.

The line reads: "Proof. kappa(q) <= 6 sqrt(sigma' q+ delta) by Corollary A' or B'."

Passes 1 and 2 state: in the branch where D has challenge resolution 1,
Corollary A' bounds only kappa^na(q), the supremum over resolution-1 observers,
whereas Theorem C's statement and proof carry kappa(q), the supremum over ALL
q-query challenge-oblivious observers ("|G0 - G1| <= kappa(q) by definition of
kappa"). Corollary A' does not bound kappa(q). Nothing in the artifact bounds
kappa(q) by 6 sqrt(sigma' q+ delta) without a hypothesis on M.

Pass 1's configuration: N = 2^20, delta = 2^-30, sigma = 0 (so sigma' = 40),
M = 2^25, q = 1. Then mu(min(qM,N^2)) = min(M delta, 3(M delta^2)^{1/3}, 1)
= min(2^-5, 3 * 2^-11.67, 1) ~ 0.0094, while sqrt(sigma' q+ delta) ~ 2.7e-4.
So the only available bound on kappa(1) is ~35x the target.

Pass 2's configuration: M = 2^100, sigma' = 100, delta = 2^-60, q = 1,
P = ceil(sqrt(sigma'/delta)). The hypothesis M <= sigma'/sqrt(27 delta) fails by
~2^70, so Corollaries B'/B'' give nothing, and mu(2^100) = 1. Pass 2 adds that
the quantity asserted in that proof line is one the artifact's own Barrier 1
declares unproved in exactly this regime.

Both passes state the conclusion of Theorem C' is nonetheless obtainable, because
Theorem C's step |G0 - G1| is instantiated at the fixed D and Proposition 6.2
bounds it directly for that D with M' = 1; but that re-derivation is nowhere
written, and Theorem C is stated only with kappa(q). Both propose the same
repair: restate Theorem C in D-relative form. Pass 1 calls it "one-line, entirely
within the existing proof of Theorem C. No new mathematics." Pass 2 records that
as written, the headline claim C' is proved only in its second branch (M small).

Pass 3's contrary view, in full: the application "is mathematically valid in
context - in the resolution-1 case the specific observer's advantage is bounded
by kappa^na(q), not by invoking the (false in general) inequality
kappa(q) <= kappa^na(q) - but as literally written it conflates kappa(q) with
kappa^na(q), which is imprecise notation rather than a derivable identity."

## F2 — MINOR, raised by passes 1, 3, 5. Section 0 item (C) vs Theorem C.

Section 0 advertises "an explicit family Y^{P,gamma}" with the bound stated
immediately after; Theorem C proves that bound for Y^{P,gamma/2}. Feeding
Y^{P,gamma} into Lemma P directly yields 2 gamma, not gamma, in the slack term.
All three passes call it cosmetic and note Theorem C itself is correct.

## F3 — MINOR, raised by passes 1 and 2. Section 3 closing paragraph, last sentence.

The text reads: "Setting k1 = 1 degenerates the bound to t >= sqrt(L) >> 1: the
lemma is vacuous for one source, as it must be." Both passes report this
computation is false.

Pass 1: at k1 = 1, k2 = N, t^2 = [ln(eN) + N + C0]/(2N) -> 1/2, so t ~ 0.707.
With N = 2^20, sigma = 0, gamma_0 = 2^-10: L ~ 14.9, C0 ~ 36.0, t ~ 0.707,
whereas sqrt(L) ~ 3.86.
Pass 2: N = 1000, sigma = 0, gamma_0 = 0.01: L = 7.908, C0 = 21.19, k2 = 1000
gives t = 0.717, whereas sqrt(L) = 2.81.

Both add that k1 = 1 models a deterministic first coordinate, not "one source":
the Contract's Remark rem:ell1 has a single source emitting a point of [N]^2
whose posterior need not factor at all. Both state the artifact's proof DOES fail
for one source, but for a different reason than the one given - the unavailability
of Lemma 1's product structure. Both mark it not load-bearing. Both note this
sentence is the artifact's stated answer to a demand the Contract makes
explicitly, which is why they raise it despite it being non-load-bearing.

## F4 — MINOR, raised by passes 1 and 2. Section 3 closing paragraph, test count.

The text reads: "There are 2^M possible tests, but once the observer is fixed and
the revealed values are conditioned away, only |Z| < 2^{sigma+2} of them are
reached." Both passes report the stated reason is false: given zeta, the test
still varies with f through the revealed values, so more than |Z| tests are
reached. What makes the proof work is that the events T_{S0,w} partition the
space, so no union bound over them is needed - which Steps 1 to 3 do correctly.
Exposition only; both passes affirm the proof itself is correct.

## F5 — MINOR, pass 1. Theorems A and B never invoke Lemma 0.

kappa(q) and kappa^na(q) are suprema over observers the Contract permits to be
randomised, but Proposition 6.2 is proved only for deterministic D, and neither
Theorem A nor Theorem B cites Lemma 0. Separately: Lemma 0's conclusion asserts
D' is q-query and challenge-oblivious but does not assert D' inherits challenge
resolution 1, which Theorem A's kappa^na claim needs; and the resolution
definition speaks of "the runs D^f(v,zeta)", which is not well-formed for a
randomised D unless the coins are held fixed across v and v'. Pass 1 calls the
repair trivial (fix rho, note D_rho has resolution 1) but absent.

## F6 — MINOR, pass 1. Lemma 2 applies CFHS Lemma 3 outside the card's range.

The card states the lemma for k in R_{>0}. Lemma 2 uses exponent k' = log k where
k = floor(1/m), so k' = 0 whenever k = 1, i.e. whenever m > 1/2 - reachable, e.g.
the Section 1 counterexample source conditioned on E, where m_i = 1. The
conclusion is trivially true at k = 1, so pass 1 calls this bookkeeping, but the
cited result is used beyond its stated range.

Note for triage: pass 4 examined the same step and reported the opposite -
that the hypothesis "only requires 2^k in N, not that k be an integer" and is
"genuinely satisfied ... not merely assumed". Pass 5 also passed it.

## F7 — MINOR, pass 1. Lemma P Step 2 breaks at M = 1.

delta_zeta := (S_zeta + log gamma^-1)/(P log M) divides by log M, which is 0 at
M = 1; the escape clause then reads "the asserted bound exceeds q log M >= q",
and q log M = 0 < q for q >= 1. Configuration: M = 1, q = 1, any P, gamma = 1/2.
The lemma's conclusion is still true (Fun is a singleton so Real_0 = Dec_0) but
the proof does not cover it. Section 0 assumes N >= 2 and imposes no lower bound
on M; the Contract admits M in N.

## F8 — MINOR, pass 1. Lemma P's family is not defined on the whole index set.

Step 1 begins "For zeta with Pr[z = zeta] > 0", and Y_{f,zeta} is defined only
through mu_zeta. The Contract requires a family indexed by all f in Fun and all
zeta in {0,1}* x {0,1}*. For zeta outside the support of z, including every
zeta not in Z, no Y_{f,zeta} is specified, so the family as constructed does not
meet the Contract's typing. Purely definitional (set them uniform).

## F9 — MINOR, pass 1. Lemma P Step 2's vacuity argument is valid only off B.

The chain requires S_zeta <= Sbar, which is the definition of zeta not in B. For
zeta in B with delta_zeta > 1 the inference is unavailable. Configuration: a zeta
with Pr[z = zeta] = 2^-100, so S_zeta may far exceed Sbar for small sigma and
gamma^-1. Pass 1 marks it harmless, since Step 4 charges all of B to
Pr[z in B] < gamma, but the text does not restrict the argument to zeta not in B.

## F10 — MINOR, pass 1. Lemma 4 assumes h surjective.

"for j = 1..M' run D^f(v_j,zeta) for a fixed v_j in h^{-1}(j)" presupposes
h^{-1}(j) nonempty. Configuration: M = 4, M' = 3, h(1)=h(2)=h(3)=1, h(4)=2, so
3 is not in the image and v_3 does not exist. Repair: range over image(h), which
only shrinks the budget.

## F11 — MINOR, pass 1. Corollary A' asserted without proof.

The two inequalities needed are immediate, but no proof is given, and Corollary
A' is load-bearing for Theorem C'.

## F12 — MINOR, pass 4. Theorem C proof, parenthetical.

"(For q >= P that term already exceeds 2 sigma' > 1, so no hypothesis q < P is
needed.)" The claim is asserted without derivation, and the text has just shown
the numerator is bounded ABOVE by 2 sigma' + 2 log gamma^-1, which is the wrong
direction for the lower-bound claim being made. Pass 4 notes the fact actually
needed - that the term exceeds 1 - is independently easy (sigma + 2 +
2 log(2/gamma) > 4 > 1 using sigma >= 0, gamma < 1), so soundness of Theorem C is
not threatened, but the specific comparison to 2 sigma' is not derived.

## F13 — MINOR, pass 5. Section 0 narrows to N >= 2 without flagging it.

The Contract quantifies "for all N and M" with no lower bound; the submission
assumes N >= 2 throughout and does not list this in Section 9. Pass 5 notes low
impact, since N = 1 forces delta >= 1 and the conjectured bound is vacuous, but
the narrowing is unflagged.

## F14 — MINOR, pass 5. Section 8 crossover claims informal.

"the first is smaller when M <~ N log^3 M" and "once q >~ log^6 M (sigma + 2N)^2
delta / sigma'^3" are stated with <~ and >~ and no worked derivation. Not
load-bearing for any numbered result.

## F15 — MINOR, pass 2, TRUNCATED. Section 1 counterexample's range.

Pass 2 began: the counterexample is valid only for M >= 5 but is asserted for
2 <= M <= N. Against its own unpredictability parameter delta_unp = 2 delta, the
assertion that "E[m1 m2] <= delta_unp^2 is false" requires delta > 4 delta^2,
i.e. M > 4. At M = 2 (delta = 1/2, delta_unp = 1, delta_unp^2 ...) — the report
was cut off here by the session limit and the finding is incomplete.

Note for triage: passes 1, 4 and 5 each examined this counterexample and each
affirmed it, pass 5 recomputing the predictor's success probability
delta + (1-delta)/N <= 2 delta independently. None raised a range restriction.

---

## Patterns probed and reported NOT found

Recorded because a triage that only sees findings will mis-weigh the report.

Pass 1 probed and did not find: quantifier-order inversion; union bound over an
unbounded index; worst-case versus expected confusion; a lost hybrid factor;
unshown independence at the two places it matters (theta versus the fresh cells
in Lemma 3 Step 1, and H* versus x in Theorem C). It affirmed the Section 1
counterexample and that Lemma 5's 1/3 exponent is correctly forced by it.

Pass 2, before aborting, reported Lemma P survives attack (deficiency bound,
"conditional law of H is exactly X_j", oracle-indexing, consistency, arithmetic
all confirmed); the G2->G3 coupling correct; Proposition 6.2 correct; Lemma 4's
budget and determinacy correct; Lemma 5's optimisation correct; and "all claimed
constants are right", having re-derived them independently.

Pass 3 attempted four explicit constructions against the M-free leading term
(large-M correlated source; challenge-steered 1-query observer at large M;
row/column-leaking sources of the CFHS obstruction type; boundary cases q=0,
N=M=2, delta=1/N, delta=1) and reports it could not violate Theorem A or B.
It re-derived the Lemma 3 numeric chain and notes L + C0 <= 3.63 sigma' +
ln gamma_0^-1 is valid but tight, ~0.6% margin at N=2, sigma=0, with the packaged
sqrt(8 delta (...)) absorbing it comfortably.

Pass 4 verified quantifier order, retention of consistency, the index set, and
every predicator's entitlements against the Contract's definition; and confirmed
Theorem C's explicit constants do not depend on the unextracted constant in
CFHS Theorem 3.

Pass 5 ruled every numbered result from Lemma 0 to Theorem C' PROVED and answered
four targeted questions in the artifact's favour, including that the artifact
never needs a bound on Pr[x in Q] in the real experiment.
