---
id: 0023-prover-3-r2-triage
agent: triage
model: claude-opus-5[1m]
cycle: 3
---

# Triage ruling on `0023-prover-3-r2.md` (focused re-verification round, passes F and G)

Inputs ruled on: `0023-prover-3-r2-verify-F.md` (RAW: DEFECTS, agent verifier-b) and
`0023-prover-3-r2-verify-G.md` (RAW: PARTIAL, agent verifier). Also read for
adjudication: `0023-prover-3-triage.md` (the ruling that directed these repairs),
`intermediates/I02-degree-d-sets.md`, `CONTRACT.md`, `PROGRESS.md` (rung classes
R3–R6′), `sources/S7-changfang26-card.md`, `sources/S1-acc22-card.md`,
`proofs/0023-refuter-2.md` §2, `proofs/0023-refuter-3.md`, `proofs/0023-refuter-5.md`
(verdict only), `proofs/0023-prover-3-u5.md` (L11).

Every disputed computational claim was re-derived here from scratch in exact
arithmetic (integer Walsh–Hadamard on full truth tables, `Fraction`s, exhaustive
enumeration), not by reading the artifact's scripts and not by reasoning:
witness (a) for k=1,2,3 (N=3,6,11); witness (b) for d=2..6 plus brute force at
d=2,3,4; all minimum certificates of all points on both sides of witness (a) for
k≤3 with all selections; the §7.4 worst-selection sequence to k=8; §6.4's three
comparisons for d=1..7; §5.4's group formulas for (q,d)=(3,2),(4,2),(2,3);
max_i Inf_i(f_A) over every nonempty subset of {±1}^N for N≤4; and a full search
for min π_Rel over all cross-disjoint degree-≤d pairs at (N,d)=(3,2),(4,2),(4,3).

**TALLY: 5 UPHELD / 4 OVERRULED / 4 PEDANTIC / 0 NEEDS SOURCE / 0 UNCLEAR.**

---

## 1. F's class-B claim (F1): OVERRULED

F1 holds that Remark 1.1's repaired principle ("a family out of scope refutes
nothing") is violated by T2's own proof, because both caps are obtained by
evaluating the count at point masses whose max(δ_F,δ_G) is 1/4 resp. 1/2 — above
every threshold at issue — so the *barrier reading* of CAP I and CAP II is
unproved. I rule this **OVERRULED**, on the mathematics. The four directed
questions, answered in order.

### (a) Is F's reading of the repaired remark correct, and does the caps' proof rely on out-of-scope families?

**F's reading is not correct, and the caps' proof does not rely on out-of-scope
families in the sense Remark 1.1 speaks of.** The factual half of F's claim is
right and I confirm it: the point masses at (A_k,B_k) have max δ = max(1/4,
2^{−k−1}) = 1/4, and at (C,D) max δ = max(1/2, 1/(2(2^d−1))) = 1/2; every
threshold at issue is < 1/(2d) ≤ 1/4 for d ≥ 2. What is wrong is the inference.
A witness pair enters this framework in **two logically distinct roles**, and
scope is relevant to one and irrelevant to the other.

**Role 1 (Remark 1.1's role): a family offered as a counterexample to the
class's *conclusion*.** The deleted inference was "some pair has both windows
empty, therefore the argument establishes nothing". That is an assertion that the
argument's conclusion fails at that family, i.e. that the family is a
counterexample. A family with max δ = 1/4 satisfies "max δ ≥ T" trivially for
every T ≤ 1/4, so it is not a counterexample; that is exactly why the previous
round's U2 struck the inference, and it is what Remark 1.1 says ("refutes
nothing"). Scope is decisive here because the failure is a **coverage** failure:
the count derives no inequality at all for such a family, and an uncovered
family hurts only if it could itself be a genuine counterexample.

**Role 2 (T2's role): a pair used to pin ρ, and a family used to certify that a
window-size profile is realisable.** D4(T2) requires the per-pair inequality
π_W(A,B) ≥ ρ(|W(A)|,|W(B)|) for **all** (A,B) ∈ 𝒫_d. A *pair* is not a family:
it carries no δ and no threshold, so "out of scope" is not even a predicate that
applies to it. Since (A_k,B_k) ∈ 𝒫_d, (T2) forces ρ at the window-size profile
(w,w), w = 2^{d−1}+d−1, to be at most π_W(A_k,B_k) ≤ π_Rel(A_k,B_k) = (d+1)/2 —
unconditionally, with no scope notion in sight. The point-mass family then does
one further job only: it certifies that this profile is *realised* by some
incompatible family, so that (T3)'s uniform output cannot simply ignore it. That
certificate is not a refutation of anything.

**Why the class cannot escape by restricting its quantification.** The only way
to save T > Θ_W is for the argument to prove that the bad window-size profiles
are not realised by families with max δ < T. Within D4 that is unavailable by
stipulation: (T3) admits δ_F, δ_G and window sizes as its only quantitative
inputs, and never a *relation* between them; a lemma of the form "max δ < T ⇒
E|W| ≤ poly(d)" is precisely the extra mathematics the barrier says is needed, and
it is outside 𝒲 by construction (see [G1]). So T2's ceiling stands under the
artifact's own class model.

**And F's alternative model is self-refuting.** Suppose one adopts F's symmetric
convention and restricts T2's infimum to in-scope families, i.e. declares that
the class establishes T iff the count yields max δ ≥ T for every incompatible
family with max δ < T. T1 itself gives, for every family,

    Λ(F,G) = E[ρ]/E[|W(f)|+|W(g)|] ≤ E[π_W]/E[|W(f)|+|W(g)|] ≤ max(δ_F,δ_G),

so at any family with max δ < T one has Λ ≤ max δ < T and the count *never*
concludes. Under F's convention the class therefore establishes T iff no
incompatible family with max δ < T exists — i.e. "provable by the class"
collapses to "true", no barrier of any kind is expressible, and frozen R1 would
have to be credited with the exact frontier of its class (1/4 at d=2) rather than
the 1/(2d) its proof actually delivers. A convention under which the notion of
"what a technique can prove" is identical to "what is true" is not a model of
provability; it is the negation of the concept. F's F1 therefore proves too much,
and its own concession — "under the opposite (unrestricted) convention T2 stands
but Remark 1.1's deletion of the empty-window inference is wrong" — is also
incorrect: under the unrestricted convention the empty-window inference remains
invalid, for the Role-1 reason above (coverage failure ≠ counterexample).

One subsidiary charge in F1 is simply false on inspection: [ESCALATED E1]'s
sentence that the empty-window convention is "used by no cap in this artifact" is
**true**. Both caps carry explicit nonemptiness hypotheses (T6:
|W(A_k)|+|W(B_k)| ≥ 1; T8: W(C) ≠ ∅), and the point masses T2 uses have nonempty
windows by construction, so no zero-denominator convention is invoked anywhere in
the chain that converts Θ_W into a barrier.

What is genuinely deficient is one sentence of *drafting*: Remark 1.1's
parenthetical volunteers the two witnesses' max δ values without saying which
role they play, which is what let a careful referee read a contradiction into it.
That is the PEDANTIC item P-a below (one added sentence), not a defect in a proof.

### (b) Is the damage confined to the barrier reading, or does it reach the arithmetic?

Moot, since (a) is answered "no", but recorded for the register: **it would not
have reached the arithmetic even had F been right**, and F concedes as much. I
re-derived independently, in exact arithmetic: T5's table (α = 1/2, deg = k+1,
|Rel| = 3,6,11, Inf = 1/4 on address bits and 1/4,1/8,1/16 on targets, π_Rel =
3/2,2,5/2, 2^k top supports); T7's table (Inf(f_C) = 1/2, Inf(f_D) =
1/6,1/14,1/30,1/62,1/126 at d = 2..6, π_Rel = 4/3,12/7,32/15,80/31,64/21);
T6(a)–(c) and T8's constants; T9's dichotomy; §7.1's W_sh ratios 1/4, 5/24, 13/64
(identical over *every* choice of the two top supports, as claimed); §7.3's W_max
ratios; §7.4's minimum-certificate enumeration (all sizes = d, multiplicities
1–2, 1–3, 1–4, worst-selection ratios 1/4, 1/6, 5/32, best-selection 1/4, 5/24,
13/64), the worst-selection sequence 1/4, 1/6, 5/32, 13/80, 11/64, 81/448,
193/1024, 449/2304 with global minimum 5/32 > 1/8 at k=3; §6.4's comparisons
(CAP I below the 1/(2d) grid ceiling first at d = 5, CAP II for all d ≥ 2, both
caps ≥ K1's 2^{−d}/d for all d ≥ 1 with equality at d = 1); and §5.4's group
formulas (Inf_i(f_C) = 1 − |𝒴|^{−1}, Inf_i(f_D) = (1 − |𝒴|^{−1})/(|𝒴|^d − 1),
exactly |𝒴|^d nonzero characters) at (q,d) = (3,2), (4,2), (2,3). Every number in
the artifact's tables and constants is correct. The witness influence tables and
the two constants are now confirmed by five earlier passes, two passes this round,
two triages and this independent recomputation.

### (c) Does anything survive as a usable steering claim? The two concrete killers.

**Yes, and this is the operative answer: the two concrete killers of
`0023-refuter-3` stand regardless, unconditionally, and they are not
class-model-dependent in any degree.** The reason is structural, not a matter of
degree of confidence: each killer refutes a **universally quantified per-pair
inequality** by exhibiting one explicit pair, and a per-pair inequality has no
family, no δ, no threshold and therefore no notion of "scope" attached to it.

* **Killer (a), refuter-3 §4, the address family.** The inequality at issue is
  (M)-transplanted, π(A,B) ≥ (|J|+|K|)/(2d) for all cross-disjoint degree-≤d
  pairs. At (A_3,A_3^c) (d = 4, N = 11) I recompute π = 5/2 against
  (|J|+|K|)/(2d) = 22/8 = 11/4: the inequality is **false**, exactly, with an
  exact rational certificate on a fully enumerated 2^11-point cube. The ratio
  π/(|J|+|K|) = (k/2+1)/(2(k+2^k)) = 2^{−Θ(d)} is likewise an exact computation
  at named sets.
* **Killer (b), refuter-3 §4/§5.2, the codimension-d subcube.** θ*(d) :=
  min over disjoint pairs of max_{i∈S} min(Inf_i f, Inf_i g) ≤ 1/(2(2^d−1)),
  witnessed by (C,C^c), which I recompute exactly at d = 2,3,4 by brute force
  (1/6, 1/14, 1/30) and in closed form to d = 6. This refutes (HEAVY_θ) at every
  θ ≥ 1/poly(d).

Neither statement mentions distributions, δ, thresholds, in-scope-ness, or the
class 𝒲. They are finite exact certificates about named pairs and would survive
the complete demolition of the artifact's class model. **The campaign has lost
nothing operationally**; even on F's own reading only a generalisation (from
"these two named per-pair inequalities are false" to "these two technique
sub-classes cannot beat 2^{−Θ(d)}") would have been at risk. As it happens, per
this ruling, the generalisation is not at risk either.

### (d) Is it repairable by a bounded edit, or does it need new mathematics?

No repair is required, because F1 is overruled. If the human wishes belt-and-
braces, the bounded edit is **one added sentence** (P-a): after Remark 1.1, state
that a witness pair is used in this artifact only (i) to instantiate (T2)'s
universal quantifier over 𝒫_d, pinning ρ at a window-size profile, and (ii) to
certify that the profile is realisable — never as a counterexample to a class
member's conclusion — and that scope in the sense of Remark 1.1 is therefore
irrelevant to T2. No new mathematics, no change to any theorem, no change to any
constant. Restating the caps as conditional on a scope convention would be a
*weakening in response to a mistaken objection* and must not be done.

---

## 2. G's class-A finding (title / VERDICT clause (iv) vs [G5]): UPHELD

G's finding 1 and F's F3 are the same defect, filed at different severities; the
class-A grading is correct and, per §3.6, STATEMENT DRIFT is never PEDANTIC.

Ruling on the mathematics. The title asserts "the two live plans escape both
caps" and VERDICT 1 opens "P1 and P5 ESCAPE both caps — YES, both, by exact
computation". §7.4 evaluates **minimum**-size certificate selections and says so;
[G5] states plainly that P5's declared notion is **minimal** (irredundant)
certificates, that witness (a) admits a minimal certificate of size 2^{d−1} (the
all-targets certificate at a point whose 2^k targets are all +1 — I verify such
points exist for k ≤ 3 and that this set is a certificate and is irredundant),
and that whether an unrestricted minimal selection keeps E|W(A_k)| = poly(d) —
the quantity CAP I(b) tests under Remark 2.2 — is not determined. So for P5's
declared technique the CAP I escape is not merely unproved: T6 at
E|W(A_k)| ≥ 2^{d−1} would give an exponential ceiling (d+1)2^{−d}. The headline
therefore clears a plan the body leaves open, in the artifact's two most-read
sentences, and the artifact instructs the campaign to steer on it. Upheld as
**U-A2**. P1 has no analogous problem: §7.1 evaluates exactly the plan's declared
window (a maximum-degree monomial support, `0023-strategist-2` §2 table V1), the
size bound is definitional, and the ratio is the same 1/4, 5/24, 13/64 for
*every* choice of the two supports (re-verified exhaustively here).

Repair (two clauses, no mathematics): title — "…and the two live plans escape
both caps: P1 outright, P5 for minimum-size certificate selections (its declared
minimal-certificate variant is open, [G5])"; VERDICT 1 first sentence — the same
qualifier, which the *later* part of the same clause already carries ("the
minimum-certificate window (P5)").

---

## 3. FILTERED REPORT (UPHELD + PEDANTIC only)

### UPHELD

**U-A1 — class (A). The designated ladder-record sentence drops CAP II's
nonemptiness hypothesis; so does the title's "own-heavy" clause.** Source: F2
(F is right; G affirmatively cleared this area — see §5). Locations: §5.3's
displayed sentence, repeated verbatim in VERDICT 3, with the instruction "The
ladder record must carry the displayed conditional sentence, not a summary of
it"; and the title's "own-heavy" clause. T8 has two hypotheses: own-heaviness at
θ > 1/(2(2^d−1)) **and** W(C) ≠ ∅. VERDICT 2(ii) keeps both; Remark 4.2′ keeps
both and explicitly concedes that an own-heavy W with W(C) = ∅ is not capped by
this artifact. The record sentence quantifies over all own-heavy functionals,
including the ones the artifact declines to cap. The omission is **not vacuous**:
own-heaviness (D2) is an inclusion constraint, not a selection rule, so a
localised W may be own-heavy at θ = 1/4 and still have W(C) = ∅ while taking the
address hub W(A_k) = {a_1..a_k} on witness (a) — for which T6 yields only
(d+1)/(4(d−1)) ≈ 1/4, no exponential cap at all. Since this is the one sentence
the artifact tells the campaign to paste into `LEDGER.md`/`PROGRESS.md`, the drift
is in the primary deliverable. Corrected sentence, to be used verbatim:

> *No relevance-denominated window-payment argument, and no window-payment
> argument whose window is own-heavy at some level θ > 1/(2(2^d−1)) **and
> nonempty at the codimension-d subcube C**, can establish R4's target
> c·e^{−d^α} — or any threshold above (d+1)2^{−d−1} resp. 1/(2(2^d−1)) — in the
> object class of R2, R3, R4, R5, R6′ or R6(ℤ_2).*

**U-A2 — class (A). Title and VERDICT 1 clear P5 unqualified; [G5] leaves P5's
declared (minimal-certificate) variant open.** Sources: G-1 (class A), F3 (filed
class C; the class-C grading is overruled — this is drift). Full ruling in §2
above, with the two-clause repair.

**U-B1 — class (C). VERDICT 5's inclusion claim is unproved.** Source: F4.
VERDICT 5 asserts that the η*(d) ceiling covers "every localised window
functional that is nonempty on the pairs approaching η*(d) — which includes every
functional named in this artifact". Two named functionals are empty at some pairs
of 𝒫_d: W_Forced (empty on both sides at the address pair, Remark 4.3; and
Forced(D) = ∅ for d ≥ 2) and W^θ_hvy (empty at D, by T8's own proof). Whether
either is nonempty at the pairs approaching inf π_Rel is not established, and
those pairs are nowhere identified. §8.1 states the correct restricted list
(W_rel, W_sh, W_max, the certificate windows). Repair: make VERDICT 5's
parenthetical agree with §8.1.

**U-B2 — class (C). VERDICT 1's "the hypotheses of CAP I … fail" is literally
false for CAP I.** Source: F5. T6 is a theorem about *every* localised W with a
nonempty combined window at the address pair; that hypothesis **holds** for W_sh,
W_max and both certificate windows (§7.1/§7.3/§8.1 prove it). What fails is
T6(b)'s inverse-polynomial-density instance, and what happens is that T6's
general conclusion degrades to ≈(d+1)/(4d) — which I re-verify: the W_sh density
on witness (a) is d/(2^{d−1}+d−1), and the resulting ceiling is vacuous against
the 1/(2d) grid ceiling for every d ≥ 2. The body says this correctly and
immediately; the VERDICT, inside its self-declared "exact sense", does not.
Repair: "no cap below 1/poly(d)" in place of "the hypotheses fail" / "neither cap
touches them", for the CAP I half. (The CAP II half is accurate as written: the
own-heaviness hypothesis genuinely fails at every level > 1/(2(2^d−1)), because
witness (b)'s D attains the level exactly — re-verified.)

**U-C1 — class (D), light. The S7 obstacle-(ii) dependency row misdescribes the
card.** Source: F8. Card `sources/S7-changfang26-card.md` records obstacle (ii)
as *non-canonicity of T(A) across a distribution's support, so the union T over a
whole family is not bounded and the argument must be run pairwise or with a
covering step*, and states twice that the paper contains nothing about
influences, families, pairs or factorisation. The row instead says the card
records "that a pair-dependent window is the obstacle to per-function
factorisation", and Remark 2.1 says "This is the only load-bearing form of
obstacle (ii) recorded in card S7". The pair-dependence/factorisation observation
is the artifact's own and is correct; it is not the card's. §7.2's *Reading* uses
obstacle (ii) in the card's own sense and is fine. This is the sibling row of the
one U6 just repaired, so it is upheld rather than waved: restate the row in the
card's words and attribute the factorisation observation to this artifact. Nothing
downstream depends on it (the row is already marked non-load-bearing).

### PEDANTIC (note; no rewrite required)

* **P-a (from F1).** Add one sentence after Remark 1.1 distinguishing the two
  roles of a witness pair (§1(d) gives the text). Formally optional — the
  mathematics is correct as it stands — but this is now the second round in which
  the empty-window model has generated a false-positive class-B finding from a
  strong referee, so folding it in while touching the VERDICT is cheap insurance.
* **P-b (F6).** Remark 4.3 applies CAP II to the quantified family
  "θ ≥ 1/poly(d)", which includes constants θ > 1/2; there W^θ_hvy ≡ ∅ on the
  whole class, so Remark 4.2′'s discharge does not apply and the conclusion holds
  only through D5's degenerate zero convention, which Remark 4.3 does not invoke.
  F's premise is correct and I verified it two ways: Inf_i(f_A) =
  (¼·P_1)/(P_2 + ½·P_1) ≤ ½ with equality iff i is forced, and by brute force
  max_i Inf_i(f_A) = 1/2 exactly over *every* nonempty subset of {±1}^N, N ≤ 4.
  Harmless: the named rules (W^θ_hvy at θ ≤ ½, W_Forced at θ = ½) are genuinely
  discharged, and the conclusion is true in the excluded range anyway.
* **P-c (F7).** Register still lacks rows for `0023-refuter-2` §2's master count
  (M), cited in Corollary 3.2, and for `0023-prover-3-u5` L11 ([G4]'s one-line
  proof). Both exist and were read here; both are non-load-bearing. U6 did not
  name them, so this is not an undershoot of the previous instruction; two lines
  if the table is touched.
* **P-d (G-7).** §6.1's "T9 gives ≥ 1/4 there" is an equality up to
  1/(4(2^d−1)) (exact value 1/4 + 1/(4(2^d−1)), re-verified); correct as stated.

---

## 4. OVERRULED (with the error named)

1. **F1 (class B, load-bearing) — OVERRULED.** Error: conflation of the two roles
   a witness pair plays (counterexample to a class member's conclusion, where
   Remark 1.1's scope test applies, versus instantiation of (T2)'s universal
   quantifier over 𝒫_d plus a realisability certificate for a window-size
   profile, where it does not); plus adoption of a scope-restricted model of
   provability which, by T1's own inequality Λ ≤ max δ, collapses "provable by
   the class" into "true" and makes every barrier — and R1's actual 1/(2d) —
   inexpressible. Full reasoning in §1. F's subsidiary charge that [ESCALATED
   E1]'s "used by no cap" is false is also wrong: both caps carry explicit
   nonemptiness hypotheses and the point masses T2 uses have nonempty windows.
2. **F9 (class E, PROGRESS.md unverifiable) — OVERRULED as a defect, and
   explicitly NOT routed to the source queue.** `PROGRESS.md` is in-repo and I
   checked §5.3's restatement line by line against it: R3 = arbitrary nonnegative
   unit-norm degree-≤d functions (l. 44/137) ✔; R4 = full signed ℝ-valued class,
   target c·e^{−d^α}, α < 1 (l. 154/162) ✔; R5 = full signed class at the
   inverse-polynomial frontier, point-mass distributions (l. 170) ✔; R6′ = ℤ_2,
   ℝ-valued, arbitrary finite support at inverse-polynomial δ (l. 207) ✔; R2 as in
   I02 ✔. The blind flag was honest and correct handling; there is no defect and
   no unreachable source.
3. **G-8 (refuter-3 §5.1 CERTIFIED-not-verified) — OVERRULED as a defect.**
   Correctly disclosed in the register, used only in §6.2's calibration
   self-check, load-bearing for nothing. I read refuter-3 §5.1: the artifact's
   characterisation of it is faithful.
4. **G-9 (P1/P5 defined in an external artifact) — OVERRULED as a defect.** Both
   windows are restated inline and self-containedly; the previous triage read
   `0023-strategist-2` and confirmed fidelity for P1 (§3 item 6 there), which I
   do not reopen. The one genuine residue — minimal versus minimum certificates —
   is upheld separately as U-A2, which is where it belongs.

---

## 5. SPOT-CHECK OF THE REFEREES' AFFIRMATIVE CLEARANCES

Required because an affirmative clearance in this campaign has twice proved
false. Done by recomputation, not by reading.

* **G's finding #2 ("the nonemptiness hypotheses are genuinely discharged, not
  merely asserted, at every place a cap is actually invoked") is FALSE as
  stated** — the third false affirmative clearance in this campaign. It fails at
  Remark 4.3's quantified family θ ≥ 1/poly(d) ∋ θ > 1/2, where W^θ_hvy ≡ ∅ (see
  P-b, with my two independent verifications that max_i Inf_i(f_A) ≤ 1/2 always).
  F caught it; G cleared it. Consequence for the tally: G's PARTIAL verdict
  over-cleared one area, and its per-finding "none (verified correct)" entries
  should be weighted accordingly.
* **F's clearance of T2 "as arithmetic" but rejection "as a model" is the right
  arithmetic and the wrong model** — §1.
* **Neither referee caught that the *title*'s own-heavy clause carries the same
  dropped hypothesis as §5.3's display.** F filed the display and VERDICT 3 only;
  G's class-A finding is about P5. Added here, inside U-A1.
* **G's #3, #4, #5, #6 clearances (the §7.4 certificate arithmetic; §5.3's R4
  inequality and the "not condemned" half; §7.2's non-canonicity theorem; §5.4's
  group generalisation) all hold** — each independently reproduced here in exact
  arithmetic; numbers listed in §1(b). Likewise F's clearances of T4, T5, T6, T7,
  T8, T9, §5.1–5.4, §6.1, §6.4, §7.1–7.5 and §8.1–8.5, and F's finding that no
  residual "value ≥ X" claim survives (I re-scanned §§6–8: every lower bound is a
  ratio at a named pair, a bound on the ceiling η*, or an explicitly conditional
  implication).
* **One extra check neither pass ran, reported because it bears on the ledger,
  not on the artifact:** at (N,d) = (3,2), (4,2), (4,3) I searched *all*
  cross-disjoint degree-≤d pairs and min π_Rel = 1 exactly, attained with
  |S| = 1. This is consistent with T4(d) and with `0023-refuter-5`'s later boxed
  claim that η*(d) = 1 exactly for all d. The artifact's §8.2 ("bracket open") and
  §8.5 ("falsifiable milestone: search for a pair with π_Rel < 1") were honest at
  the time of writing and are now **superseded, not falsified**; the ledger must
  not carry "η* bracket open" forward, and §8.5's milestone is resolved in the
  negative (no such pair). No finding against the artifact.

---

## 6. ESCALATION LIST (human)

No finding is UNCLEAR. Three items for ratification, all adjudicated above.

* **E1 (carried, now narrowed).** The empty-window class model. My ruling in §1
  narrows what E1 can affect: whichever of the two candidate conventions the
  human ratifies, **neither cap changes and neither cap's barrier reading
  changes**, because T2's instantiation uses nonempty-window point masses and is
  independent of the empty-window convention. E1 is now a presentational choice
  about D5's degenerate clause only. It remains the human's, and the reviser must
  not choose it.
* **E2 (carried).** The ladder-record wording. My ruling supplies the corrected
  sentence verbatim in U-A1; the version currently printed in the artifact
  (§5.3, VERDICT 3) must **not** be pasted into `LEDGER.md`/`PROGRESS.md`,
  because it omits CAP II's nonemptiness hypothesis. R4 remains not condemned;
  the mass-denominated form of I02's central question remains capped by nothing.
* **E3 (new, record-keeping).** `0023-refuter-5` closes §8.2's open bracket
  (η* = 1 exactly) and resolves §8.5's milestone. Since refuter-5 is CERTIFIED,
  not verified, the human decides whether the ledger records η* = 1 as CERTIFIED
  or waits for a verification pass; either way the artifact's "open" must be
  annotated as superseded rather than left to mis-steer a cold start.

## 7. CONSOLIDATED SOURCE REQUEST

**None.** No finding is NEEDS SOURCE. Every document either referee could not
reach is a campaign file present in this repository and read during this triage
(`PROGRESS.md`, `0023-refuter-2`, `0023-refuter-3`, `0023-refuter-5`,
`0023-strategist-2`, `0023-prover-3-u5`, and the S1/S6/S7 cards). F's two
"register items for Triage" are resolved as P-c. No external upload is warranted.

---

## 8. RECOMMENDATION

**(i) ONE MORE BOUNDED REVISION (r3), strictly text-only, naming exactly five
items.** I disagree with the orchestrator's provisional (ii), narrowly, and here
is the reason.

The mathematics is finished. T1–T9, both witness tables, both caps' constants,
§5.2's monotonicity direction, §5.4's group forms, §7.2's non-canonicity theorem
and §7.4's certificate arithmetic have now been re-derived independently by five
passes, two passes this round, two triages and this ruling's exact-arithmetic
recomputation, and nothing in them is wrong. F1, the one finding that would have
mattered, is overruled, and the two concrete killers are unconditional
certificates that no class-model dispute can touch. So this is not a case for a
fresh proof attempt, a weakening, or an escalation of substance.

But two of the surviving defects are **class (A) STATEMENT DRIFT in the artifact's
title and in the one sentence it instructs the campaign to paste into the ladder
record**, and §3.6 forbids grading drift as pedantic. Option (ii) — accept as
PARTIAL and move on — would leave a steering document whose title clears a plan
(P5-as-declared) that its own [G5] leaves open, and whose designated record
sentence condemns a class of arguments strictly larger than T8 proves anything
about. That is exactly how a barrier overclaim propagates into a cold-start read
two cycles later, and it is the failure this campaign has already had to reverse
once (PROGRESS.md's E2 annotation exists precisely because of it). The cost of
avoiding it is small and bounded: five edits, none longer than two lines, none
touching a theorem, a constant, a proof or a gap other than by pointer.

**r3's instructions, exhaustive; change nothing else, and do not weaken any
theorem:**

1. **U-A1** — add "and nonempty at the codimension-d subcube C" to the own-heavy
   clause in §5.3's display, in VERDICT 3's copy of it, and in the title. Use the
   corrected sentence in U-A1 verbatim.
2. **U-A2** — qualify the title's "the two live plans escape both caps" and
   VERDICT 1's first sentence with "P1 outright, P5 for minimum-size certificate
   selections ([G5] for the declared minimal-certificate variant)".
3. **U-B1** — make VERDICT 5's parenthetical agree with §8.1's restricted list.
4. **U-B2** — reword VERDICT 1's CAP I half to "no cap below 1/poly(d)" /
   "T6's conclusion degrades to ≈(d+1)/(4d)"; leave the CAP II half alone.
5. **U-C1** — restate the S7 obstacle-(ii) row in the card's own words and
   attribute the pair-dependence/factorisation observation to this artifact.
6. **P-a–P-d** — fold in only while touching those lines.

Verification after r3: a **diff-only** check of the title, the VERDICT block,
§5.3's display, VERDICT 5, Remark 2.1 and the two register rows. Do not re-run a
full pass; nothing else changed, and the mathematics has been verified past the
point of useful return. This is revision cycle 2 of the three the harness allows,
the defect classes are disjoint from the previous round's, and no defect has
survived a cycle, so the stopping rules are not engaged and the cognitive-well
risk is negligible for text-only edits under a diff-only recheck.

**If the human prefers (ii) on budget grounds**, it is acceptable *only* with both
of these conditions, because the artifact's own title would then remain wrong:
(1) the ladder record is written from U-A1's corrected sentence and U-A2's
qualifier, never from the artifact's own §5.3/VERDICT 3/title; and (2) this
ruling is filed beside the artifact as its errata, and the ledger's manifest row
for `0023-prover-3-r2` records "title and VERDICT carry two class-A overclaims,
corrected in `0023-prover-3-r2-triage` §3". Nothing here warrants (iii): no
finding is UNCLEAR and no ruling in this round needed a judgement the mathematics
could not settle.

### END OF ARTIFACT 0023-prover-3-r2-triage ###
