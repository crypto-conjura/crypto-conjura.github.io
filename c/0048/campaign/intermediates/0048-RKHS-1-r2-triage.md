# TRIAGE RULING — 0048-RKHS-1-r2 (round 2)

Handling editor. Record ruled on: `CONTRACT.md`, card `S1-bks-q81-card.md`, the
grounding result `S1-quote-grounding.md`, the artifact `0048-RKHS-1-r2.md`, and
the five round-2 referee reports A–E. Nothing else was consulted; in particular
the round-1 reports and the round-1 triage were not read, and no claim below
rests on any assertion made in them.

## DISPOSITION

The load-bearing chain — Lemma 1 → Lemma 2 → Lemma 3 → Lemma 4 → Theorem →
Corollary — is, on this record and on my own recomputation, correct and proves
the Contract statement in the Contract's own quantifier order, with error exactly
`0` and constant `C(ε,δ) = 2/(eδ)` free of `ε`; all five referees concur on this
independently and I found no dissent to adjudicate there. Every substantive
defect this round lies in Remark C plus two truncated quotations and one heading.
The centre of the round is the sentence in Remark C.1 asserting that the negativity
set of the uniform-sphere kernel has `μ`-measure `1 − o(1)`. **I computed this
myself and it is false**: the measure is strictly increasing in `n` from exactly
`1/3` at `n = 2` and increases to the strict supremum `erf(1/√2) = 2Φ(1) − 1 =
0.6826894921…`, which it never attains; the *complement* retains measure at least
`0.3173`, so the claim is not merely imprecise but bounded away from the truth
uniformly in `n`. Because the standing instruction forbids certifying any number
on a report's word, I also recomputed the kernel formula, `K(v_0,v_0)`,
`E_μ|k|`, the entropy chain, the Corollary's constant, the artifact's four-point
numerical check, and each referee's own auxiliary figures; that exposed a wrong
number inside referee B's report and small arithmetic slips inside referee C's,
recorded below with the correct values. I rule **8 UPHELD, 3 OVERRULED,
4 PEDANTIC, 1 NEEDS SOURCE, 0 UNCLEAR**. No UPHELD finding touches the
mathematics of any load-bearing step; the single UPHELD item that touches a
load-bearing object at all is the *heading* of Corollary B, whose body is correct
as written.

## TABLE OF DISTINCT FINDINGS

| # | Defect (deduplicated) | Passes raising it | Ruling | Minimal repair | Load-bearing? |
|---|---|---|---|---|---|
| F1 | Remark C.1: "negative on `{⟨v,v_0⟩² < 1/(n+2)}`, a set of `μ`-measure `1 − o(1)`" — the measure is `1/3` at `n=2`, rises monotonically, and has strict supremum `erf(1/√2) ≈ 0.68269` | A, B, C, D, E | **UPHELD** | Delete the words "a set of `μ`-measure `1 − o(1)`"; if a number is wanted, write "a set of `μ`-measure at least `1/3` for every `n ≥ 2`, tending to `2Φ(1) − 1 ≈ 0.683`". Deletion suffices — Remark C.1 needs only positivity of that measure. | No. Commentary (Remark C.1). Theorem, Corollary, Corollary B, Lemmas 1–4, Remark A do not consume it. |
| F2 | Remark C.1: "(exact check recorded in the triage of this artifact; not re-derived here)" — a quantitative claim discharged by a document outside the artifact, and the claim it was asked to carry is F1, which is false | B, C, D, E | **UPHELD** | Delete the parenthetical. No source can support it (see COMPUTATION 1). | No. Commentary. |
| F3 | Remark C.1: "so a conflict would require our construction to come out nonnegative on the hard `μ`. **It does not.**" — asserted, not shown; and it sits in tension with the artifact's own later parenthetical disclaiming any universal signedness claim | B, C, E | **UPHELD** | One sentence, verified in COMPUTATION 4: *if the constructed `r` is `≥ 0` `μ`-a.e. then `r` is itself a nonnegative reweighting of entropy cost `≤ log(n(n+1)/2) = O(log n)`, so such a `μ` is not a hard instance for the nonnegative question; equivalently `k ≥ 0` forces `μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))`, and conditioning on that atom is a nonnegative reweighting of cost `log(1/μ({±v_0})) ≤ log(n(n+1)/2)`.* | No. Commentary, but this is the artifact's own consistency audit against the Contract's "Known boundary", so it must be closed or removed, not left asserted. |
| F4 | Remark C.2 heading: "**The log rank consequence does not follow.**" — the argument establishes only that the one dictionary the card quotes (Q4, stated for *flat* distributions) is unavailable | B, E | **UPHELD** | Weaken heading and first clause to: "The log rank consequence does not follow *via the flatness dictionary quoted at Q4*; no other route is addressed here." Drop the sentence that predicates flatness of `r` (the card never defines "flat"). | No. Commentary (Remark C.2). |
| F5 | Remark C.3: "unavailable in the setting the paper actually needs ('if appropriately extended to pseudo-distributions', p. 19)" — in card Q1 that conditional attaches to the *running-time* consequence only, not to the log-rank consequence | E (B noted, not filed) | **UPHELD** | Weaken to: "unavailable in the pseudo-distribution setting, which the paper names as the condition for its *running-time* consequence (Q1)." | No. Commentary (Remark C.3). |
| F6 | Remark C.3: "a pseudo-distribution has no support points"; "the inner product used … is a degree-4 moment and so *does* have a pseudo-distribution analogue" — substantive technical assertions in terms ("pseudo-distribution", "sos") that card S1 nowhere defines, while DEPENDENCIES claims all external mathematics used is "all standard, all elementary, none from a paper" | E | **NEEDS SOURCE** | Unsettleable from the card as supplied. Goes to the source queue, not to the reviser. **Moot if the Remark C replacement recommended under Question 2 is adopted**, since that replacement makes no technical assertion about pseudo-distributions. | No. Commentary (Remark C.3). |
| F7 | DEPENDENCIES, footnote 7 labelled "verbatim" but truncated without ellipsis; the dropped clause is "In this paper we are more concerned with rectangles whose distance to being rank one (or monochromatic) is some `ε > 0` that is only a small constant or `1/ polylog(n)`" | B, C, E; confirmed by the grounding result | **UPHELD** | Restore the dropped clause (it is on the card, Q6) or mark the cut with "…". | No. Citation apparatus. See Question 3(a): restoring changes no conclusion. |
| F8 | DEPENDENCIES / Corollary B, §2.3 labelled "verbatim" but truncated; the dropped parenthetical is "(This restriction is easy to lift and anyway holds automatically in our intended application.)" | B, E; confirmed by the grounding result | **UPHELD** | Restore the parenthetical (card Q8). | No, but see Question 3(b): restoring *does* change the force of the citation, and interacts with F9. |
| F9 | Corollary B heading: "the same for distributions over **general** rank one matrices" versus the body's hypothesis `X = {rank X = 1, ‖X‖_F = 1}`. Class-A scope drift local to Corollary B (the Contract statement is unaffected) | B (as A), E (as D) | **UPHELD** | Change the heading to "…for distributions over rank one matrices of unit Frobenius norm". Not PEDANTIC: class-A drift is never PEDANTIC, and the restriction is genuine — on unnormalised rank one matrices the elements of `G` are unbounded, Lemma 1(a) fails, and the obvious rescaling `X ↦ X/‖X‖_F` does not transport the entropy bound (it introduces `log(1/‖X‖_F)` terms with no available control). | Touches a load-bearing object (Corollary B) but only its title; the body and its proof are correct as written and need no edit. |
| F10 | Proof plan: "Its `L²` norm averages to `d` over `μ`" — it is the *squared* `L²` norm that averages to `d` | C | **PEDANTIC** | Insert "squared". Lemma 3 and eq. (3) state it correctly; no reader is misled. | No. |
| F11 | Lemma 3 display `∫ K(v,v) dμ(v) = d`: the integrand is only constructed on `supp μ` | C | **PEDANTIC** | None required. The proof repairs it in place (integrates the polynomial `g`, invokes (P1), and quarantines the off-support values explicitly). | No. |
| F12 | Dangling label references `def:signed`, `conj:main` to a scheme absent from the artifact | B (minor), D | **PEDANTIC** | Point them at the GOAL section. Referents unambiguous. | No. |
| F13 | Corollary B proof: "Run Lemmas 1–4 verbatim …" does not spell out that Lemma 1(b) and Lemma 3 transfer under the *affine* parametrisation `(α,A)`; and `G` is called an "affine space" when it is a linear space of functions | A (as C, routine), E (as "harmless slip") | **PEDANTIC** | Replace "affine space" by "linear space". `G` is closed under linear combinations as a set of functions, which is all Lemmas 1(b) and 3 use; a competent reader fills this without effort. | No. |
| F14 | Referee A's clearance: "Cross-checked every verbatim quotation … all match exactly … never a misquote" | A | **OVERRULED** | This clearance is wrong. The grounding result and my reading of the artifact against card items Q6 and Q8 both show two material clauses dropped (F7, F8). A's citation audit missed them. | — |
| F15 | Referee B's figure: "`n=10` gives `≈ 0.64`" for the negativity measure | B | **OVERRULED** as stated | The exact value at `n = 10` is `0.6107168575…` (closed form in COMPUTATION 1); `0.6465477…` is the value at `n = 20`. Referee E's `0.611` is the correct one. B's *conclusion* (the measure is bounded away from `1`) is unaffected. | — |
| F16 | Referee C's auxiliary `S^1` figures: `E|1+2cos u| ≈ 1.43610`, entropy `= 0.2500` | C | **OVERRULED** as stated | Exact `E|1+2cos u| = (2π/3 + 4√3)/(2π) = 1.4359906…`, not `1.43610`; entropy `= 0.245988…`, not `0.2500`; `log(3c²) = 0.374911…`, not `0.37475`. These are the referee's own numbers, not the artifact's; no artifact defect follows, and C's conclusion is unaffected. | — |

No finding was ruled UNCLEAR; there is nothing on this record to escalate to the
human. **ESCALATION LIST: empty.**

## RECORDED COMPUTATIONS

All computations were run in this session; the driver scripts used pure-Python
400-node Gauss–Legendre quadrature (machine-precision on these smooth
integrands), `fractions.Fraction` where the case is finite and rational, and
closed forms where one exists. Each is stated so a reader can redo it.

### COMPUTATION 1 (the disputed number). `μ` uniform on `S^{n-1}`, `t := ⟨v,v_0⟩`. Then `t²  ~ Beta(1/2,(n−1)/2)`, so
`μ{⟨v,v_0⟩² < 1/(n+2)} = I_{1/(n+2)}(1/2,(n−1)/2)`, equivalently
`2 C_n ∫_0^{(n+2)^{-1/2}} (1−t²)^{(n−3)/2} dt` with
`C_n = Γ(n/2)/(√π Γ((n−1)/2))`.

| `n` | measure of the negativity set |
|---|---|
| 2 | `0.3333333333` (exact `1/3`) |
| 3 | `0.4472135955` (exact `1/√5`) |
| 4 | `0.5049746539` |
| 5 | `0.5399492472` |
| 10 | `0.6107168575` (exact closed form below) |
| 20 | `0.6465477487` |
| 50 | `0.6681956564` |
| 100 | `0.6754364479` |
| 1000 | `0.6819636405` |
| 10 000 | `0.6826169015` |
| 1 000 000 | `0.6826887663` |

Independent exact cross-checks. `n = 2`: `t = cos θ` with `θ` uniform, so the
measure is `P(|cos θ| < 1/2) = 1/3` exactly. `n = 3`: `t ~ U[−1,1]`
(Archimedes), so the measure is `P(|t| < 5^{-1/2}) = 1/√5 = 0.4472135955…`
exactly. `n = 10`: substituting `t = sin θ` and expanding
`cos⁸θ = (1/128)(35 + 56cos2θ + 28cos4θ + 8cos6θ + cos8θ)` gives
`2C_{10}·(1/128)(35a + 28 sin2a + 7 sin4a + (4/3) sin6a + (1/8) sin8a)` with
`a = arcsin(1/√12)`, which evaluates to `0.6107168575`, matching the quadrature
to ten digits.

Asymptotics, stated and checked. `n t² ⇒ χ²_1` and the threshold
`n·(1/(n+2)) = n/(n+2) → 1`, so the limit is
`P(χ²_1 < 1) = 2Φ(1) − 1 = erf(1/√2) = 0.6826894921370859…`. I verified the
sequence is strictly increasing in `n` for `2 ≤ n ≤ 400` and that the maximum
over `2 ≤ n ≤ 200000` is `0.6826858627 < erf(1/√2)`; so the supremum is the limit
and is not attained. **Verdict: the measure lies in `[1/3, erf(1/√2))` for every
`n ≥ 2` and is bounded away from `1` uniformly in `n`. "`1 − o(1)`" is false, and
false in the direction that flatters the remark.** The *positive* set retains
measure `≥ 1 − erf(1/√2) = 0.3173105079…`, which is what referee C reported
correctly. All five reports were right that the claim is false; referees A, C, D
and E reported correct values, referee B one incorrect one (F15).

### COMPUTATION 2 (the kernel itself, which I uphold as correct). For uniform `μ`, `E[v_av_bv_cv_d] = (δ_{ab}δ_{cd} + δ_{ac}δ_{bd} + δ_{ad}δ_{bc})/(n(n+2))`, so the reproducing condition `E[(v^TQv)(v^TAv)] = v_0^TAv_0` for all `A ∈ Sym_n` reads `(tr Q)I + 2Q = n(n+2) v_0v_0^T`; the ansatz `Q = a v_0v_0^T + bI` gives `an + b + 2b = 0` and `2a = n(n+2)`, i.e. `a = n(n+2)/2`, `b = −n/2`, hence
`k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2` — the artifact's formula. Numerical
confirmation by quadrature: `E_μ[k] = 1.000000000000` and
`E_μ[k²] = 6, 28, 1275` at `n = 3, 7, 50`, matching
`K(v_0,v_0) = k(v_0) = n(n+1)/2 = 6, 28, 1275`. So the kernel and the negativity
region `{⟨v,v_0⟩² < 1/(n+2)}` are correct; only the measure was wrong.

### COMPUTATION 3 (`E_μ|k|` on the uniform sphere, quoted by B and E). Quadrature gives `E_μ|k|/n = 0.71696, 0.63148, 0.52307, 0.48758, 0.48430, 0.48398` at `n = 2, 3, 10, 100, 1000, 10000`, converging to `(1/2)E|Z²−1| = 2/√(2πe) = 0.4839414490…` (since `E|Z²−1| = 4/√(2πe) = 0.9678828981…`). Referees B ("`≈ 0.484 n`") and E ("`0.4839 n`") are both correct.

### COMPUTATION 4 (the repair for F3, verified). `k` is a quadratic form, hence even, so `k(−v_0) = k(v_0) = K(v_0,v_0)`. Suppose `k ≥ 0` `μ`-a.e. Then `dμ′ := k dμ` is a probability measure (Lemma 2(ii)) with `E_{μ′}[vv^T] = v_0v_0^T` (Lemma 2(i)); testing against any unit `w ⊥ v_0` gives `E_{μ′}⟨v,w⟩² = 0`, so `⟨v,w⟩ = 0` `μ′`-a.s., and ranging `w` over an orthonormal basis of `v_0^⊥` forces `μ′` to be carried by `{±v_0}`. Hence `1 = μ′({±v_0}) = K(v_0,v_0)·μ({±v_0})`, i.e.
`μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))` exactly (`1/3, 1/6, 1/55, 1/5050` at
`n = 2, 3, 10, 100`). Conditioning on that atom is then a *nonnegative*
reweighting reaching `v_0v_0^T` exactly at cost
`log(1/μ({±v_0})) ≤ log(n(n+1)/2) = 1.09861, 1.79176, 4.00733, 8.52714` at those
`n`. Equivalently and more briefly (referee C's one-liner, which I checked and
find correct and minimal): a nonnegative `r` with `E_μ|r| = 1` *is* a nonnegative
reweighting, so if the construction ever returns one, that `μ` admits a
nonnegative reweighting of cost `O(log n) = o(n^δ)` and is therefore not a hard
instance for the source's negative result. Both forms are sound; either closes F3
in one sentence.

### COMPUTATION 5 (referee B's `{e_1,…,e_n}` instance, which I uphold). For `μ` uniform on `{e_1,…,e_n}`, `q_Q(e_i) = Q_{ii}`, so `F_μ ≅ R^n`, `d = n`, and the kernel at `e_1` is `k = (n,0,…,0)`: nonnegative, with `E_μ[k] = E_μ|k| = 1` and entropy exactly `(1/n)·n log n = log n` (`0.693147, 1.609438, 4.605170` at `n = 2, 5, 100`), inside the bound `log(n(n+1)/2)` (`1.098612, 2.708050, 8.527144`). So the construction is genuinely not always signed — which the artifact already concedes in its own parenthetical, and which does not contradict the source, since this `μ` is easy for nonnegative reweightings.

### COMPUTATION 6 (the Corollary's constant, recomputed rather than accepted). `f(x) = (log x)/x^δ` has `f′(x) = x^{−δ−1}(1 − δ log x)`, so the unique maximum is at `x = e^{1/δ}` with value `(1/δ)e^{−1} = 1/(eδ)`; I confirmed this against a scan over `log x ∈ (0,2000)` at `δ = 0.5, 1, 3` (agreement to 7 digits; for `δ ≤ 0.1` the scan range simply does not reach `e^{1/δ}`, which is why the analytic value exceeds the scan maximum there — the analytic value is the correct one). I then verified the Corollary's inequality `log(n(n+1)/2) ≤ (2/(eδ))n^δ` by direct evaluation over `δ ∈ {0.005, 0.010, …, 1.000}` (200 values) and every `n` from `1` to `100000`: **zero violations**. `n = 1` is the equality-adjacent boundary case `log 1 = 0`. So `C(ε,δ) = 2/(eδ)` stands, with no `ε`-dependence.

### COMPUTATION 7 (the artifact's own NUMERICAL CHECK, in exact arithmetic). With `r = (2, −2/3, 2/3, 2/3)` and uniform weights `1/4`: `E_μ|r| = 1` exactly (`Fraction`); `E_μ[r²] = 4/3` exactly; entropy `= (1/2)log(4/3) = 0.1438410362…` (artifact prints `0.1438`); `log E_μ[r²] = log(4/3) = 0.2876820724…` (artifact prints `0.2877`); `log 3 = 1.0986122886…`. Chain `0.14384 ≤ 0.28768 ≤ 1.09861` holds. Every printed figure in the artifact's numerical check is correct.

### COMPUTATION 8 (Corollary B's bound). `dim G ≤ n²+1` and the bound `log(n²+1)` versus the sphere's `log(n(n+1)/2)`: `0.69315` vs `0` (`n=1`), `1.60944` vs `1.09861` (`n=2`), `2.30259` vs `1.79176` (`n=3`), `4.61512` vs `4.00733` (`n=10`). So the artifact's parenthetical that the sphere case "only buys the sharper bound `log(n(n+1)/2)` over `log(n²+1)`" is arithmetically right.

## ANSWERS TO THE FOUR QUESTIONS

### 1. Do any UPHELD findings put the Contract statement in doubt?

**No.** Every UPHELD finding is confined to Remark C, to the citation apparatus,
or to one heading. Concretely: F1, F2, F3 live inside Remark C.1; F4 inside
Remark C.2; F5 inside Remark C.3; F7 and F8 inside DEPENDENCIES (with F8 also
touching a parenthetical gloss in Corollary B's statement of hypotheses); F9
touches Corollary B's *title* only. Remark C, Remark A, the DEPENDENCIES prose
and the NUMERICAL CHECK could all be deleted outright and the Theorem, the
Corollary and Corollary B would stand untouched and complete: their proofs use
only Riesz on a finite-dimensional inner-product space, Cauchy–Schwarz, Jensen,
`‖Q‖_op ≤ ‖Q‖_F`, `μ(supp μ) = 1` on a second-countable space, and
`sup_{x>0}(log x)/x^δ = 1/(eδ)`, all restated in the artifact and all verified
above (COMPUTATION 6 for the last). No referee, on any of the five passes, filed
a defect inside that chain, and my own spot-checks (COMPUTATIONS 2, 6, 7) found
none. The single UPHELD item that touches a load-bearing object, F9, is a
heading; its repair is three words and does not alter a hypothesis, a step or a
conclusion of Corollary B's body.

### 2. Remark C: repair again, or delete?

**Recommendation: delete Remark C in its present form and replace it with a short
card-supported scope note (delete-and-replace, not a third repair in place).**

*The case for repairing again.* Each individual defect has a cheap fix: F1 is a
deletion, F2 is a deletion, F3 is one sentence I have already verified
(COMPUTATION 4), F4 and F5 are weakenings of a heading and a phrase. Remark C.1's
consistency audit against the Contract's "Known boundary" is genuinely valuable —
a reader who sees an `O(log n)` answer to a question the source expected to be
hard below `n^{1/2}` will immediately suspect a contradiction with the source's
"the answer to this question is No if one does not allow negative reweighting
functions", and Remark C.1 is where that suspicion is met. Deleting it throws
that away.

*The case for deleting.* Remark C has now consumed the entire substantive defect
budget of two consecutive rounds while contributing nothing to the proof, and its
failure mode has been the same both times: it makes quantitative and scope claims
that are stronger than anything it derives or than the card supports. Its C.3 in
particular reasons in vocabulary the card does not define, which is why F6 is
unsettleable at all (a defect that revision cannot fix). A remark whose stated
job is to *limit* claims has twice been the artifact's only source of
overclaiming.

*Resolution.* The duty Remark C discharges is real: with it gone the artifact
would overclaim by silence, because a bare "Question 8.1 answered affirmatively"
invites the reader to infer the log-rank and pseudo-distribution consequences the
source attaches to a `δ < 1/2` answer. But that duty is dischargeable in a few
sentences that assert nothing beyond the card and nothing I have not checked.
**Minimal honest replacement** (fully supported by card items Q1, Q4, Q5, Q9 and
by COMPUTATION 4):

> **REMARK C (scope).** The Theorem answers Question 8.1 as literally posed
> (card Q1) and nothing more. (i) *No conflict with the source's negative
> results.* "It can be shown that as stated, Theorem 2.3 is tight" (Q5) is about
> *deficient* reweightings, which are probability distributions and hence
> nonnegative by Definition 2.2 (Q9); and "the answer to this question is No if
> one does not allow negative reweighting functions" (Q1) is an existential
> statement over `μ`. Neither is contradicted here, because whenever the
> construction returns a nonnegative `r`, that `r` is itself a nonnegative
> reweighting of entropy cost at most `log(n(n+1)/2) = O(log n)` — equivalently,
> `k ≥ 0` forces `μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))` — so such a `μ` is not
> a hard instance for the nonnegative question. (ii) *No log-rank consequence is
> claimed.* The submatrix dictionary quoted at Q4 is stated for *flat*
> distributions and the Theorem supplies no flatness guarantee, so that route is
> unavailable; no other route is addressed, and Theorem 2.4 (Q3) is untouched.
> (iii) *The pseudo-distribution version is out of scope.* Every use of `supp μ`
> in the proof — Lemma 1(b),(c), Lemma 2, Lemma 3, the Theorem — presumes an
> honest distribution. The source attaches its pseudo-distribution condition to
> its *running-time* consequence (Q1); this artifact addresses neither.

That is three sentences plus three clauses, contains no unverified number, makes
no assertion in undefined vocabulary, and moots F6 without a source request. It
also happens to preserve the one genuinely useful thing Remark C.1 was trying to
say, now with a proof.

### 3. The two dropped clauses named by the grounding result.

**(a) Footnote 7 / card Q6.** The artifact's "verbatim" quotation stops after the
Gavinsky–Lovett sentence and drops "In this paper we are more concerned with
rectangles whose distance to being rank one (or monochromatic) is some `ε > 0`
that is only a small constant or `1/ polylog(n)`." **UPHELD (F7).** Restoring it
**changes no conclusion the artifact draws.** Footnote 7 is quoted for context
only; it feeds no argument. If anything the restored clause is mildly favourable
to the artifact, since it confirms that the source's own `ε` regime is a small
constant or `1/polylog(n)`, which is consistent with the artifact's observation
that footnote 8's `ε`-dependence caveat is moot for a construction whose constant
carries no `ε` at all (verified: `C(ε,δ) = 2/(eδ)`, COMPUTATION 6).

**(b) §2.3 / card Q8.** The artifact drops "(This restriction is easy to lift and
anyway holds automatically in our intended application.)" **UPHELD (F8).**
Restoring it **does change a conclusion**, in two opposite directions that must
both be recorded. It *supports* the artifact's gloss "the normalisation used in
the source paper's intended application" — the dropped parenthetical is in fact
the only place on the card that mentions the intended application, so as the
artifact stands that gloss is licensed by words it declined to quote. But it also
*undercuts* the use of §2.3 to license Corollary B's confinement to the
unit-Frobenius-norm slice: the source calls the unit-norm restriction "easy to
lift" for its own method, whereas Corollary B's method genuinely needs it
(compactness of `X` is what supplies boundedness in Lemma 1(a), and the rescaling
`X ↦ X/‖X‖_F` does not transport the entropy bound). So restoring Q8 in full both
repairs the gloss and confirms F9: the heading "general rank one matrices" must
be narrowed.

### 4. The scope-overreach claims, and the strongest form the card supports.

**(a) The cited paper's log-rank consequence.** The referees are right (F4,
UPHELD). Card Q1 records the paper's own "It may improve the best known bound for
the log rank conjecture to `Õ(n^δ)`" with no flatness caveat attached to that
clause, and the card contains §2.2 only as the single flatness sentence Q4 — not
the reduction itself. The artifact therefore settles a tension between its own
result and the source's stated expectation by assertion, on the strength of an
excerpt. **Strongest form the card supports:** *the submatrix dictionary quoted
at Q4 is stated for flat distributions; the Theorem provides no flatness
guarantee, so that dictionary cannot be invoked for this `r`, and in particular
the Theorem names no submatrix and leaves Theorem 2.4 (Q3) untouched. Whether
some other route from a signed low-entropy reweighting to a log-rank bound exists
is not addressed.* Note also that "flat" is used by the card (Q4) but never
defined by it, so any claim *about the predicate* "`r` is flat" is outside the
card; the supported claim is about the dictionary's hypothesis, not about `r`.

**(b) Pseudo-distributions.** The referees are right (F5, UPHELD). In card Q1 the
sentence is "It may improve the best known bound for the log rank conjecture to
`Õ(n^δ)` **and if appropriately extended to pseudo-distributions**, improve our
algorithm's running time to `exp(Õ(n^δ))` as well" — the conditional governs the
running-time clause only. Calling the pseudo-distribution setting "the setting
the paper actually needs" promotes one of two advertised consequences into the
sole one. **Strongest form the card supports:** *the paper names a
pseudo-distribution extension as the condition for its running-time consequence;
this artifact proves nothing about pseudo-distributions, and every use of
`supp μ` in the proof presumes an honest distribution.* The further assertions
that a pseudo-distribution "has no support points" and that the degree-4 moment
inner product "does have a pseudo-distribution analogue" are **NEEDS SOURCE**
(F6): the card defines neither "pseudo-distribution" nor "sos", so they cannot be
checked here, and they also contradict the artifact's own DEPENDENCIES claim that
all external mathematics it uses is "all standard, all elementary, none from a
paper".

**(c) Corollary B's heading.** The referees are right (F9, UPHELD; class-A drift,
therefore not eligible to be PEDANTIC). The body proves the statement for
`X = {rank X = 1, ‖X‖_F = 1}`; the heading says "general rank one matrices"; the
source's Theorem 2.3 (Q2) is stated for "any distribution over rank one `n × n`
matrices". **Strongest form the card and the proof support:** *the same mechanism
works for any Borel probability measure on the set of rank one `n × n` matrices
of unit Frobenius norm, with entropy cost `log(n²+1)`; this is the normalisation
the source adopts in §2.3 (Q8), which the source itself describes as easy to lift
for its own method but which this proof genuinely uses (through compactness).*

## REVISION INSTRUCTIONS (UPHELD items only)

Bounded strictly by the eight UPHELD findings. F6 is **not** in this list: it is
NEEDS SOURCE and leaves the loop for the source queue; the reviser must not
attempt to argue it. F10–F13 are PEDANTIC and must not consume a revision.
F14–F16 are OVERRULED referee items requiring no artifact edit.

1. **(F1) — DELETION.** In Remark C.1, delete "a set of `μ`-measure `1 − o(1)`".
   If a quantifier is retained in its place, it must be the verified one: "a set
   of `μ`-measure at least `1/3` for every `n ≥ 2`, increasing to
   `2Φ(1) − 1 ≈ 0.683`". Do not write `1 − o(1)` in any form.
2. **(F2) — DELETION.** Delete the parenthetical "(exact check recorded in the
   triage of this artifact; not re-derived here)". No computation may be
   outsourced to a document outside the artifact.
3. **(F3) — SUBSTANTIVE NEW ARGUMENT (one sentence).** Replace the bare "It does
   not." with the argument verified in COMPUTATION 4 above: a nonnegative output
   `r` is itself a nonnegative reweighting of cost `≤ log(n(n+1)/2) = O(log n)`,
   so any `μ` on which the construction returns a nonnegative `r` is not a hard
   instance for the source's negative result; optionally add the structural form,
   that `k ≥ 0` forces `μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))`.
4. **(F4) — WEAKENING.** Retitle Remark C.2 "The log rank consequence does not
   follow *via the quoted flatness dictionary*", and confine the body's claim to
   the dictionary's hypothesis. Delete the clause predicating flatness of `r`
   ("nothing in its construction constrains `r` to be flat"), since the card
   never defines that predicate.
5. **(F5) — WEAKENING.** In Remark C.3, replace "the setting the paper actually
   needs" with a formulation that attaches the pseudo-distribution condition to
   the source's running-time consequence only, as card Q1 does.
6. **(F7) — RESTORATION OF QUOTED TEXT.** In DEPENDENCIES, restore the final
   clause of footnote 7 from card Q6, or mark the cut with an explicit ellipsis.
7. **(F8) — RESTORATION OF QUOTED TEXT.** In DEPENDENCIES and in Corollary B's
   statement, restore the §2.3 parenthetical from card Q8: "(This restriction is
   easy to lift and anyway holds automatically in our intended application.)"
8. **(F9) — WEAKENING.** Retitle Corollary B "the same for distributions over
   rank one matrices of unit Frobenius norm". The body and proof of Corollary B
   are correct and must not be otherwise edited.

*Editor's note to the reviser.* Instructions 1–5 all fall inside Remark C. If the
handling editor's Question-2 recommendation is adopted — delete Remark C and
substitute the replacement text given there verbatim — then instructions 1–5 are
discharged in a single edit, F6 becomes moot, and only instructions 6–8 remain.
That is the disposition I recommend. Under no circumstance may this revision
touch Lemmas 1–4, the Theorem, the Corollary, Remark A, or the body of
Corollary B.

## CONSOLIDATED SOURCE REQUEST

Referees B and E filed six source requests between them. Five are refused, with
reasons; one is forwarded.

**FORWARDED — 1 item.**

1. **For F6 (Remark C.3, class E).** From Barak–Kothari–Steurer,
   arXiv:1701.06321v2: the definition of a *pseudo-distribution* and of the
   pseudo-expectation operator `Ẽ` (the latter appears unexplained inside card
   item Q2), together with whatever the paper says about which functionals of a
   distribution do and do not have pseudo-distribution analogues. Needed to check
   two assertions in Remark C.3: that "a pseudo-distribution has no support
   points", and that a degree-4 moment inner product "does have a
   pseudo-distribution analogue". *Conditional:* if the Remark C replacement
   recommended under Question 2 is adopted, this request may be closed unfilled,
   since the replacement asserts nothing about pseudo-distributions beyond
   quoting card Q1.

**REFUSED — 5 items.**

2. (B#2, E#1) The document the artifact calls "the review/triage of this
   artifact", to certify `μ{⟨v,v_0⟩² < 1/(n+2)} = 1 − o(1)`. **Refused: settled
   by computation.** COMPUTATION 1 shows the quantity is `1/3` at `n=2`,
   `1/√5` at `n=3`, `0.6107168575` at `n=10`, and has strict supremum
   `erf(1/√2) = 0.6826894921…`. No admissible source can certify `1 − o(1)`; the
   sentence is to be deleted (instruction 1), not sourced.
3. (B#1, E#2) BKS §2.2 in full, plus the passage carrying "It may improve the
   best known bound for the log rank conjecture to `Õ(n^δ)`". **Refused as
   unnecessary:** it would be needed only to *retain* the flat negative claim,
   and instruction 4 weakens that claim to what card Q4 already supports. If a
   later campaign wants to assert the strong negative, this request must be
   re-opened first.
4. (E#4) Full footnote 7 and full §2.3. **Refused: already on the card** (Q6,
   Q8); the grounding result confirms the card carries both clauses in full. The
   repair is to the artifact (instructions 6, 7), not to the card.
5. Any source for "flat" as a predicate of a signed function. **Refused as moot**
   under instruction 4, which removes the only use of that predicate.
6. Any source bearing on the artifact's `ε`-independence versus footnote 8.
   **Refused as moot:** verified independently, `C(ε,δ) = 2/(eδ)` contains no
   `ε` (COMPUTATION 6).

**Card status.** Card S1 requires no repair; the grounding result and my own
comparison agree that it carries every clause the artifact dropped.

### END OF TRIAGE RULING [0048-RKHS-1-r2] ###
