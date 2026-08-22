# Collated referee findings — round r2 (COMPLETE)

Three passes against r2 on a neutrally staged, provenance-stripped package.
Pass B = Opus, supremum discipline. Pass C = Sonnet, refutation attempt + scope.
Pass A = Opus, targeted at Lemma P and the G2->G3 coupling; it aborted twice on
infrastructure (session limit, then output cap) and was re-run terse as pass A2,
which completed. Both aborted attempts, before dying, reported Lemma P and the
coupling sound; neither is counted as a verdict.
Transcribed by the audit operator, who has ruled on nothing.

## Standing context triage must have

Round 1 ran against the pre-r2 content and its triage ruled 4 upheld
(F1, F3, F5, F7), 2 overruled (F12, F15), 9 pedantic. r2 applied the four upheld
repairs. Two findings below are re-raisings of items round-1 triage already ruled
PEDANTIC and should be checked against that ruling rather than adjudicated fresh:
G7 below is round-1 F6, and G6 below is round-1 F10.

Round 1's serious finding F1 (Theorem C stated with the unrestricted supremum
while Theorem C' fed it a bound on the restricted one) was examined directly by
pass B, which was not told the finding existed, and pass B reports the repair
sound on both axes it probed. That is recorded here as a negative result, not a
finding.

---

## G1 — SERIOUS, pass B. Lemma 0's proof against the Section 4 definition.

The r2 text of Lemma 0's proof asserts: "challenge resolution is defined in
Section 4 per fixed coin string, so if the runs D^f_rho(v,zeta) and
D^f_rho(v',zeta) issue the same query positions for every rho whenever
h(v)=h(v'), they do so in particular for rho*."

Pass B reports that Section 4's definition says no such thing: it reads "for all
f, zeta and all v, v' with h(v)=h(v'), the runs D^f(v,zeta) and D^f(v',zeta)
issue the same sequence of query positions", and never quantifies coins at all.
For a randomised D that sentence has no truth value. Section 0's own gloss of the
class -- "observers whose query positions do not depend on the challenge value" --
reads naturally as a statement about the LAW of the query positions, and under
that reading pass B reports Lemma 0's inheritance claim is false.

Counterexample given: N = 2, M = 2, q = 1. D flips rho uniform in {0,1} and, on
challenge v in {1,2}, queries cell (1,1) if v XOR rho = 1 and (2,2) otherwise.
For each fixed v the query position is uniform on {(1,1),(2,2)} -- identical in
law for v=1 and v=2 -- so D's query positions do not depend on the challenge
value. Yet D_0 queries (1,1) at v=1 and (2,2) at v=2, and D_1 does the reverse:
neither coin fixing has resolution 1, both have resolution 2. So D' = D_{rho*}
does not inherit resolution 1, and Lemma 4 yields s = min(qM',N^2) = 2, whereas
Theorem A's closing step applies "Resolution 1 gives s <= q" with s = 1.

Pass B's assessment of the consequence: the class over which kappa^na is a
supremum is not determined by the document; on one admissible reading it contains
observers that steer their probes by the challenge conditioned on their coins,
which is the case Section 9's Barrier 1 declares open. Theorem A's statement is
therefore underdetermined, and on the Section 0 reading its proof has a false
step; on the Lemma 0 reading everything goes through but the supporting
definition is not in Section 4. This propagates to Theorem C' branch 1 for
randomised observers.

Note for triage: this text is new in r2. It was introduced as the repair to
round-1 finding F5, which triage upheld with the instruction "add to Lemma 0 that
D' inherits D's challenge resolution (immediate once resolution is read per fixed
coin string, which the definition should say)". The repair asserted the reading in
Lemma 0 rather than writing it into the Section 4 definition, which is the gap
pass B is reporting.

## G2 — MINOR, passes B and C. N >= 2 is an undeclared narrowing.

Section 0 fixes N >= 2 globally and it is load-bearing, but the list of what is
not proved names "all P, all q, all M, all observers" and does not mention N; the
Contract quantifies over all N in the naturals.
Pass B's concrete failure: at N = 1, sigma_1 = sigma_2 = 1 (so sigma = 2 and
sigma' = sigma + 2 log 1 = 2) with gamma = 1/2, Theorem C's step "as N >= 2 gives
sigma + 2 <= sigma'" is false.
Pass C independently notes the same, adding that the M = 1 case got an explicit
aside in Lemma P while N = 1 got none, so the asymmetry is what stands out.

## G3 — MINOR, pass B. M >= 2 is likewise undeclared, and the M = 1 patch is not propagated.

Lemma P patches M = 1 in a parenthetical, but Theorem C' neither restates M >= 2
nor invokes the patch, so the Contract's M = 1 instance is claimed by nothing.
Note for triage: the Lemma P parenthetical is new in r2, added as the repair to
round-1 finding F7.

## G4 — MINOR, pass B. Theorem C' proof, the parenthetical alternative route.

"equivalently, Proposition 6.2 bounds epsilon(D) directly at M'=1" is false for a
randomised D, since Proposition 6.2 is stated for deterministic D. With G1 also
biting the primary route, pass B reports branch 1 has no valid route for a
randomised resolution-1 observer.

## G5 — MINOR, pass B. Lemma 0's statement does not cover what Theorem A invokes.

The statement covers only Adv-domination and attainment of the supremum defining
kappa(q). The (Real, Real_0) pairing, the attainment of kappa^na, and
resolution-inheritance all live only in the proof body, which Theorem A cites. A
reader instantiating Lemma 0 as stated cannot derive Theorem A's opening step.

## G6 — MINOR, pass B. Lemma 4 presumes h surjective.

"for j = 1..M' run D^f(v_j,zeta) for a fixed v_j in h^{-1}(j)" is ill-formed when
h^{-1}(j) is empty; M = 2, M' = 2, h(1) = h(2) = 1 is a legal witness under the
definition and leaves h^{-1}(2) empty.
This is round-1 finding F10, which triage ruled PEDANTIC on the ground that
ranging over image(h) only shrinks the budget. Recorded for consistency.

## G7 — MINOR, pass B. Lemma 2 applies the flat-decomposition lemma at exponent 0.

CARD-B states it for k in R_{>0} with 2^k in N; the submission applies it at
k = log k_i, which is 0 when k_i = 1, reachable with positive probability (m_i = 1
on the event E of the Section 1 counterexample).
This is round-1 finding F6, which triage ruled PEDANTIC on the ground that at
k = 0 the conclusion is the triviality pi = sum_u pi(u) delta_u. Recorded for
consistency.

## G8 — MINOR, pass B. q = 0 falls between Corollary B' and Theorem C' branch 2.

Corollary B's first arm M <= sqrt(sigma'/(q delta)) is undefined at q = 0, and
Corollary B'' is proved only for q >= 1, so Theorem C' branch 2 has no content at
q = 0. The case is rescued only by an observation inside Theorem A's proof
("for q = 0 every observer has resolution 1 vacuously"), which is never connected
to Theorem C'.

## G9 — MINOR, pass B. Lemma P Step 2 phrases the family's definition inside a case split on q.

"hence is vacuous for q >= 1, and for q = 0 both experiments ...; set Y_{f,zeta}
uniform" reads as defining the family by cases on q, in a document whose Contract
makes "family chosen before q" part of the statement. Pass B notes the intended
reading is recoverable (set Y := uniform whenever delta_zeta > 1, a q-free
condition) but that the sentence as written invites the quantifier-order
violation the Contract's rem:order forbids.
Note for triage: this sentence is new in r2, added as the repair to round-1
finding F7.

## G10 — MINOR, pass B. Theorem B's trailing observer quantifier is vacuous.

kappa(q) is already a supremum over the class, so "for every q and every q-query
challenge-oblivious observer" adds nothing; pass B calls it symptomatic
imprecision in the bookkeeping under audit.

## G11 — MINOR, pass C. Theorem B's proof is terse on the delta = 1 edge case.

"as in Theorem A" carries the gamma_0 = delta in (0,1) requirement by reference
only.

## G12 — NOT A DEFECT, pass C, recorded because it is a positioning risk.

The Contract's own "Progress to date" describes the known q = 1 result as holding
under M delta at most polylogarithmic, whereas Corollary B'' requires
M sqrt(delta) <= sigma'/27 -- a strictly smaller admissible range of M for small
delta. Pass C states this is not an internal inconsistency, since the submission
disclaims the full conjecture, but that a reader could be misled about how much of
the Contract's recorded progress this document re-derives.

---

## Negative results reported, recorded so triage does not over-weigh the findings

Pass B checked and found sound: Lemma 1(i)-(iv) including the 2 delta / sqrt(theta)
step; the E[m1 m2] <= delta^2 counterexample; Lemma 2's bilinearity and the floor
inequality; Lemma 3's Hoeffding conditioning on T_{S0,w} and the full union-bound
arithmetic, including that random (k1,k2) and zeta correlated with f are covered by
the simultaneous event with no unshown independence; Lemma 5's optimisation;
Claim 6.1 and Proposition 6.2's assembly; Theorem A's constants; Corollary A';
Lemma P Steps 1-4 against CARD-A, including the min-entropy-deficiency-only
reading, disjoint supports, fixed-values-are-sampled-values, and the 2 gamma
assembly; Theorem C's G2->G3 coupling and its use of the Contract's two lemmas;
the c = 2, C = 8 assembly; and Section 8's threshold. It reports no class-E defect:
every external result in Section 10 is covered by a card.

Pass C attempted refutation along five axes (large M with small delta; row and
column leakage; oracle-correlated split sources; challenge-steered observers; and
the boundary cases q = 0, delta minimal, delta = 1, smallest N and M) and reports
it could not violate any numbered theorem. It verified by direct computation that
the Section 3 single-source paragraph's claim t(1,N)^2 -> 1/2 is correct as
written, and that the paragraph identifies a failure point other than the
fixed-set-misses-challenge lemma, which is what the Contract's rem:ell1 demands.
It re-derived the constants in Lemma 3, Corollary A', Theorem C' and Corollaries
B'/B''.

---

## Findings added by pass A2

## G13 — MINOR, pass A2. Lemma P's family is undefined at off-support leakage indices.

Step 1 opens "For zeta with Pr[z=zeta] > 0", and Step 2's "uniform otherwise"
clause disambiguates only f outside supp X_j, not an off-support zeta. Concrete:
sigma_1 = sigma_2 = 1 with zeta = (0,0) unreachable leaves Y_{f,(0,0)} with no
value, so the object is not a family in the Contract's sense. No experiment
reaches such a zeta, so no displayed bound changes.
This is round-1 finding F8, ruled PEDANTIC then. Recorded for consistency.

## G14 — MINOR as ranked by pass A2, BUT SEE THE TENSION BELOW. Lemma P Steps 2-3.

Pass A2 reports that Step 2 asserts "mu_zeta = sum_j lambda_j X_j +
lambda_fin Y_fin with lambda_fin <= gamma ... all supports pairwise disjoint",
and hence Step 3's "the conditional law of H is exactly X_j", from CARD-A's
Claim 2 — whose *statement* gives only gamma-closeness to *some* convex
combination. It reports that the card's "what the proof establishes" supplies
disjointness (observation 2) and fixed-values-are-taken (observation 3) but
never that lambda_j X_j is the mu_zeta-restriction, and never that the card's
stopping rule "Pr[X in supp(Y)] > gamma" bounds the *mu_zeta-mass* of the
residue by gamma.

Its concrete failure: if the X in that stopping rule is the *uniform*
distribution, then at Pr[z=zeta] = 2^{-sigma} the rule bounds the residue only
by gamma * 2^sigma under mu_zeta, which would replace Step 4's "+ gamma" by
"+ gamma 2^sigma" and destroy Lemma P.

**Tension triage must resolve, flagged by the operator without ruling on it.**
Pass A2 ranks this MINOR and says "the conclusion is recoverable from Claim 2's
gamma-close reading, but the identification is not written" — yet its own
concrete failure says the alternative reading destroys Lemma P. Those two
statements cannot both be the right weight. The question is precise and settleable
from CARD-A alone: in the card's recorded stopping rule, does the symbol X denote
the uniform distribution or the conditioned distribution X_z being decomposed?
The card's proof sketch opens "For ease of notation, let S := S_z and X := X_z."
Triage should rule on that, and re-rank the finding accordingly: if X = X_z the
finding is at most a missing sentence; if X is uniform, Lemma P and everything
downstream of it fails.

## G15 — MINOR, pass A2. Lemma 2 invoked at exponent 0.

Third independent raising of round-1 finding F6 (= G7 above), ruled PEDANTIC.
A2 adds that k_i = 1 occurs with probability delta via the Section 1
counterexample and is used inside Proposition 6.2 at exactly those (f,zeta).

## G16 — MINOR, pass A2. Lemma 4 presupposes h surjective.

Third independent raising of round-1 finding F10 (= G6 above), ruled PEDANTIC.
A2's witness: M = 4, M' = 3, h = (1,1,2,2) leaves h^{-1}(3) empty; it notes the
loop must skip empty fibres and the budget qM' is unaffected.

## Operator note on the re-raising pattern

F6/G7/G15 and F10/G6/G16 have each now been raised by three independent passes
across two rounds, and triage ruled both PEDANTIC in round 1. Either they are
genuinely trivial and referees are pattern-matching on a citation-range slip and
a surjectivity slip, or the round-1 ruling was wrong. Triage should say which,
because a finding that returns every round at zero cost to fix is cheaper to fix
than to keep adjudicating.

## Negative results from pass A2

Areas cleared explicitly: the G2-to-G3 coupling in full (both oracles carry the
component's law, identical-until-bad legitimate, both Contract lemmas inside
their hypotheses, the Lemma-query predictor simulable in Dec_0); Proposition 6.2's
split and flattening; Lemma 3's simultaneous quantification, T_{S0,w}
measurability, Hoeffding, and the step-(3) counting; Lemma 4's budget and the
determination of the whole test by the revealed data; Lemma 5's optimisation;
the Section 1 counterexample's splitness and unpredictability; and every stated
constant, itemised. It also confirms Corollary A''s vacuity remark and finds no
concealed statement drift.
