MODEL: opus

### VERDICT ###

STATUS: DEFECTS

The Contract's statement is, in my judgement, proved exactly as written (no drift: correct
quantifier order on `C(ε,δ)`, `L` genuinely nonzero rank one, relative accuracy met with
error `0`, no term read vacuously), but the artifact contains one outright false quantitative
assertion in Remark C.1, one deferred check I cannot reach, two over-strong negative scope
claims, and a heading/body mismatch in Corollary B — all outside the load-bearing line, none
of which I am permitted to repair.

### FINDINGS ###

| quoted location | class A-E | explanation |
|---|---|---|
| Remark C.1: "negative on `{⟨v,v_0⟩² < 1/(n+2)}`, a set of `μ`-measure `1 − o(1)`" | B (non-load-bearing) | The set is identified correctly but its measure is not `1 − o(1)`; it tends to a constant `≈ 0.6827`. For `μ` uniform on `S^{n-1}` and `t = ⟨v,v_0⟩`, `√n·t ⇒ N(0,1)`, so `μ{t² < 1/(n+2)} = μ{n t² < n/(n+2)} → P(χ²_1 < 1) = 2Φ(1) − 1 = 0.68269…`. Finite checks agree and are all bounded well away from 1: `n=2` gives exactly `1/3`; `n=3` gives `1/√5 ≈ 0.447`; `n=10` gives `≈ 0.64`. (The kernel itself is right: I verified `E_μ[k]=1`, `E_μ[k v_1²]=1`, `E_μ[k v_j²]=0` for `j≥2` from the sphere moments `E[v_1²]=1/n`, `E[v_1⁴]=3/(n(n+2))`, `E[v_1²v_2²]=1/(n(n+2))`, and `k(v_0) = n(n+1)/2 = d`.) The qualitative point the remark needs — `k` is negative on a set of positive measure, indeed `E_μ|k| ≈ 0.484·n ≫ 1 = E_μ[k]` — survives, so nothing in the Theorem or the Corollary is affected; but the sentence as written is false, and it is offered as the evidence for the remark's main assertion. |
| Remark C.1: "a set of `μ`-measure `1 − o(1)` (exact check recorded in the review of this artifact; not re-derived here)" | E | The one place in the artifact where a computation is outsourced, and it is outsourced to a document that is not the artifact and was not supplied to me ("the review of this artifact"). I cannot reach it. What the artifact needs it to say is a measure computation for `μ{⟨v,v_0⟩² < 1/(n+2)}` under uniform `μ`; when I perform that computation it contradicts the artifact (previous row). Load-bearing only for Remark C.1, hence not blocking on its own, but it must either be re-derived in the artifact or deleted. |
| Remark C.1: "so a conflict would require our construction to come out nonnegative on the hard `μ`. It does not." | C | The "hard `μ`" — the instance witnessing the source's "the answer to this question is No if one does not allow negative reweighting functions" — is never identified, and nothing shown here rules out that the construction's `k` is nonnegative on it. The only `μ` examined is the uniform one (and that examination is the erroneous claim above); the artifact itself then concedes "(No claim is made that the construction's `r` is signed for *every* non-point-mass `μ`.)", which is in tension with the flat "It does not". The concession is warranted: for `μ` uniform on `{e_1,…,e_n}` one has `F_μ ≅ R^n`, `k_{e_1} = (n,0,…,0) ≥ 0`, so the construction returns a *nonnegative* `r` with entropy exactly `log n`. Note also that the remark's logic runs backwards: given the Theorem, "our `r` is signed on the hard `μ`" is a *consequence* of the source's unproved-here "No", not independent corroboration of consistency. Non-load-bearing; I do not regard it as a routine gap a reader fills without effort, because it is the artifact's own consistency audit against the Contract's "Known boundary". |
| Remark C.2 heading: "**The log rank consequence does not follow.**" | C | Over-strong negative claim. What is argued is only that the *one quoted* dictionary (card Q4) requires flatness, and the Theorem's `r` is neither flat nor nonnegative — so *that* route is unavailable. That does not establish that no route exists; the source asserts a positive answer "may improve the best known bound for the log rank conjecture to `Õ(n^δ)`" without restricting itself to the quoted sentence, and no argument here excludes an intermediate step (e.g. any flattening/rounding of a signed low-entropy reweighting). The honest claim is "does not follow via the quoted flatness dictionary; other routes are not addressed". This matters more than a typical stylistic quibble: the credibility of the whole artifact rests on reconciling an `O(log n)` answer with the source's belief that a `δ < 1/2` answer would be "very interesting", and this remark is the reconciliation. |
| "COROLLARY B (the same for distributions over general rank one matrices)" vs its body "`X := {X ∈ R^{n×n} : rank X = 1, ‖X‖_F = 1}`" | A (scope drift local to Corollary B; the Contract statement itself is NOT affected) | The heading promises "general rank one matrices"; what is proved is the unit-Frobenius-norm slice only. That slice is exactly what the proof needs (`X` compact, so the affine functions are bounded and continuous — the two properties Lemma 1(a),(b) consume), but it is a genuine restriction relative to the source's Theorem 2.3 (card Q2: "any distribution over rank one `n × n` matrices"), and the artifact nowhere shows the unbounded case follows. Since Corollary B's stated purpose is to show "the mechanism is not an artefact of specialising to `X = vv^T`", the reader is entitled to know that it is instead an artefact of compactness plus a normalisation. Not part of the Contract, so it does not touch the main verdict on the statement. |
| DEPENDENCIES: "§2.3, p. 6, verbatim (normalisation used in Corollary B): 'We will restrict our attention to the case that all the columns of `U` and `V` are of unit norm.'" | D (minor) | Labelled "verbatim" but silently truncated. Card Q8 continues: "(This restriction is easy to lift and anyway holds automatically in our intended application.)" The dropped parenthetical is precisely the sentence bearing on the previous row: the source regards the unit-norm restriction as inessential, so citing §2.3 does not license Corollary B's confinement to it. (Footnote 7 is truncated the same way — dropping "In this paper we are more concerned with rectangles whose distance to being rank one … is some `ε > 0` that is only a small constant or `1/polylog(n)`" — but nothing in the artifact turns on that omission.) |

Nothing else I checked is a defect. In particular, on my assigned angle I could not find any drift, easing, or vacuous reading in the load-bearing line; details below.

### STEP LOG ###

**Step 0 — completeness.** `### END OF ARTIFACT [P-1] ###` present; no unit stops mid-sentence.
Last complete unit: NUMERICAL CHECK. Proceeded.

**Step A0 — what the artifact actually proves, in my words.**
*(Theorem.)* For every `n ≥ 1` and every Borel probability measure `μ` on `S^{n-1}`: let
`F_μ ⊆ L²(μ)` be the (finite-dimensional, `d := dim F_μ ≤ n(n+1)/2`) space of classes of
quadratic forms `v ↦ v^T Q v`, `Q ∈ Sym_n`. Then there is a point `v_0 ∈ supp μ` whose
reproducing kernel `k = k_{v_0} ∈ F_μ` has `K(v_0,v_0) = ‖k‖²_{L²(μ)} ≤ d`. Setting
`c := 1/E_μ|k| ∈ [K(v_0,v_0)^{-1/2}, 1]` and `r := c·k` (a quadratic form restricted to the
sphere, hence bounded Borel), one gets `E_μ|r| = 1`, `E_μ[r(v)vv^T] = c·v_0v_0^T` **exactly**,
and `E_μ[|r|log|r|] ≤ log(c²K(v_0,v_0)) ≤ log K(v_0,v_0) ≤ log(n(n+1)/2)`.
*(Corollary.)* Hence for every `δ > 0`, with `C := 2/(eδ)` (no `ε`-dependence), for every `n`
and every `μ` there are a signed reweighting `r` with entropy cost `≤ C·n^δ` and a nonzero
rank one `L := c v_0v_0^T`, `‖L‖_F = c > 0`, with `‖E_μ[r vv^T] − L‖_F = 0 ≤ ε‖L‖_F` for
every `ε > 0`.

**Step A1 — clause-by-clause diff against "THE STATEMENT TO BE PROVED OR REFUTED".**
- *"For every `ε > 0` and every `δ > 0` there exists a finite constant `C = C(ε,δ)`"*: met.
  `C = 2/(eδ)` is finite for each `δ > 0` and is exhibited before `n` and `μ` are introduced.
- *"such that the following holds for every `n ∈ N` and every Borel probability measure `μ`"*:
  met, and in the right order — `C` is a function of `δ` alone, so no `n`- or `μ`-dependence
  can hide in it. The proof of the Corollary quantifies `n, μ` inside. No swap. (`n = 0` is
  vacuous: `S^{-1} = ∅` carries no probability measure; `n = 1` is handled explicitly, where
  `log(n(n+1)/2) = 0`.) No "for all sufficiently large `n`" is smuggled in: the bound
  `log(n(n+1)/2) ≤ (2/(eδ))n^δ` is verified for `n = 1` separately and for all `n ≥ 2` via
  `n(n+1)/2 ≤ n²` and `sup_{x>0}(log x)/x^δ = 1/(eδ)`. I checked both: `n+1 ≤ 2n` for `n ≥ 1`,
  and `f(x) = (log x)/x^δ` has `f'(x) = x^{-δ-1}(1 − δ log x)`, maximum `1/(eδ)` at `x = e^{1/δ}`.
- *"there exist a signed reweighting `r` of `μ` with entropy cost at most `C·n^δ` (in the sense
  of the Definition above)"*: met in the Definition's full sense, both clauses. `E_μ|r| = 1`
  holds exactly (by construction `c = 1/E_μ|k|`, with `1 ≤ E_μ|k| ≤ K^{1/2} < ∞` so `c` is a
  well-defined positive real), and `E_μ[|r|log|r|] ≤ log(n(n+1)/2) ≤ C n^δ`. `r` is Borel and
  `μ`-integrable (bounded: `‖q_Q‖_∞ ≤ ‖Q‖_op ≤ ‖Q‖_F` on the sphere). Convention 2 is
  honoured in the only direction that could cheat: no regularity is *assumed* of `r`; the
  constructed `r` happens to be smooth, which is a strengthening, not an easing.
- *"and a **nonzero** rank one `L ∈ R^{n×n}`"*: met, not vacuously. `L = (c v_0)v_0^T` with
  `c ≥ (n(n+1)/2)^{-1/2} > 0` and `‖v_0‖ = 1`, so `rank L = 1` and `‖L‖_F = c > 0`. The
  nonzero clause is not obtained by a limiting or degenerate `L`: `L` is the exact value of
  `E_μ[r vv^T]`.
- *"such that `‖E_{v∼μ}[r(v)vv^T] − L‖_F ≤ ε‖L‖_F`"*: met as stated, with error `0`, on the
  nose and with no rescaling. Because the target is *relative*, one must check the trap where
  `‖L‖_F` is driven to `0` to make the right-hand side trivially large — impossible here since
  the left side is `0` and `L ≠ 0`; and the trap where `L` is allowed to be `0` — excluded.
  Remark A (which I verified independently: `‖M − tuw^T‖_F² = ‖M‖_F² − 2t·u^TMw + t²`,
  `max u^TMw = s_1(M)`, discriminant condition `s_1² ≥ (1−ε²)‖M‖_F²`, rearranging to
  `Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1²`, both roots positive for `M ≠ 0`) correctly confirms that
  the relative normalisation is not a free lunch and that `M = 0` would be inadmissible for
  `ε ∈ (0,1)`.
- Convention 3 (`L` need not be symmetric or PSD): the artifact delivers a PSD `L`, a special
  case of what is allowed — a strengthening, not a weakening.
- Convention 1 (track the `ε`-dependence): delivered in the strongest possible form,
  `C` independent of `ε`, because the error is `0`.
**Conclusion of the A-check: no statement drift on the Contract. The artifact proves the
Contract's statement and strictly more (error `0` instead of `ε‖L‖_F`; entropy `O(log n)`
instead of `O(n^δ)`; `C` free of `ε`).** I looked specifically for an "asymptotic standing in
for an explicit constant" and found the reverse: an explicit `log(n(n+1)/2)`.

**Step 1 — Lemma 1.** ACCEPTED. (P1) `μ(supp μ) = 1` from second countability/Lindelöf: correct.
(a) `F_μ` is the image of `Sym_n` under a linear map, so `d ≤ n(n+1)/2`, and `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F`
on `S^{n-1}`: correct. (b) The step I pressed hardest, since it is the one that makes point
evaluation legitimate on equivalence classes: `h := q_{Q−Q'}` is continuous, `{|h| > |h(v_0)|/2}`
is open and contains `v_0 ∈ supp μ`, so has positive measure, yet is contained in the null set
`{h ≠ 0}` — correct, and correctly used: `ev_v` is defined only through quadratic-form
representatives, and (b) says any two such representatives of one class agree at every support
point. (c) Riesz on a finite-dimensional inner-product space, `k_v = Σ_j ev_v(f_j)f_j`,
`K(v,v) = ⟨k_v,k_v⟩ = ev_v(k_v)`: correct. (d) `q_I ≡ 1` and `q_{E_{ab}}(v) = v_av_b` on the
sphere: correct, and this is the whole engine.

**Step 2 — Lemma 2.** ACCEPTED. (i) Entrywise, `E_μ[k v_av_b] = ⟨k, [q_{E_{ab}}]⟩ = q_{E_{ab}}(v_0)
= (v_0)_a(v_0)_b`, so `E_μ[k vv^T] = v_0v_0^T` exactly. I checked that (b) is genuinely needed
here and is genuinely available. (ii) `E_μ[k] = ⟨k,[q_I]⟩ = q_I(v_0) = 1`; hence `E_μ|k| ≥ 1`,
`K = E_μ[k²] ≥ (E_μ|k|)² ≥ 1`, `k ≠ 0`. (iii) Cauchy–Schwarz against `1`. All correct; absolute
convergence is justified by boundedness.

**Step 3 — Lemma 3.** ACCEPTED. `k_v = Σ_j q_j(v) f_j` and `K(v,v) = Σ_j q_j(v)²` for
`v ∈ supp μ`; `g := Σ_j q_j²` is a polynomial, hence Borel everywhere, and agrees with `K(v,v)`
on a set of full measure, so `∫ K dμ = Σ_j ‖f_j‖² = d`. The averaging argument is stated
carefully (if `μ{g ≤ d} = 0` then `g − d > 0` a.e. with zero integral, contradiction), and the
step `μ(A) > 0` together with `μ(supp μ) = 1` giving `A ∩ supp μ ≠ ∅` is correct. `d ≥ 1` since
`[1] ∈ F_μ` has norm 1, so the statement is not vacuous.

**Step 4 — Lemma 4.** ACCEPTED. `dν := |r|dμ` is a probability measure, `ν{r = 0} = 0`,
`E_ν[log|r|] = E_μ[|r|log|r|]`, `E_ν[|r|] = E_μ[r²] < ∞`, Jensen for the concave `log`. The
integrability preliminaries (`φ(t) ≥ −1/e`, `φ(t) ≤ t²`) are correct and do the required work.
The sharpness note (equality iff `|r| ∈ {0,c}` a.e., bound then `log(1/μ{|r| = c})`) is correct.

**Step 5 — Proof of the Theorem.** ACCEPTED. `c := 1/E_μ|k| ∈ [K^{-1/2},1]`, `E_μ|r| = 1`,
`E_μ[r vv^T] = c v_0v_0^T = L`, `‖L‖_F = c`, error `0`; entropy `≤ log(c²K) = log(K/(E_μ|k|)²)
≤ log K ≤ log(n(n+1)/2)`. Every inequality direction checked.

**Step 6 — Corollary (the Contract).** ACCEPTED; see Step A1.

**Step 7 — independent verification of the mechanism.** I re-derived the artifact's own numerical
check and two further instances, to make sure the "exact rank one" claim is not an artefact.
(i) The tabulated `n=2`, four-point example: `F_μ = {x : x_1+x_2 = x_3+x_4}`, `d = 3`,
`k = (3,−1,1,1)` reproduces (`(1/4)(3x_1 − x_2 + x_3 + x_4) = x_1` on `F_μ`), `E_μ[k]=1`,
`‖k‖²=3`, `(1/4)(3v_1v_1^T − v_2v_2^T + v_3v_3^T + v_4v_4^T) = v_1v_1^T`, `E_μ|k| = 3/2`,
`c = 2/3`, entropy `0.1438 ≤ log(4/3) = 0.2877 ≤ log 3`. All confirmed.
(ii) `μ` uniform on `S^{n-1}`: kernel `k = (n(n+2)/2)⟨v,v_0⟩² − n/2` verified by moments;
`E_μ[k vv^T] = v_0v_0^T` exactly; `E_μ|k| = (n/2)E|χ²_1 − 1| + o(n) ≈ 0.484 n`, so entropy is
`O(1)` here. This is the instance where cancellation is doing real work, and the construction
survives it.
(iii) `μ` uniform on `{e_1,…,e_n}`: `k_{e_1} = (n,0,…,0) ≥ 0`, entropy `log n`, exact rank one —
i.e. a case where the construction degenerates to "condition on one atom" and is *not* signed.
Consistent with the Theorem, but see Finding 3.
No contradiction with the Contract's "Known boundary" arises: the boundary says *some* `μ`
defeats every nonnegative `r` below exponent `1/2`, which is compatible with *every* `μ`
admitting a cheap signed `r`.

**Step 8 — fairness of the claim to answer the quoted question (card Q1).** Diffed the Contract
against Q1 verbatim. Q1 asks for: every `μ` over `S^{n−1}`, every `ε, δ > 0`, a not-necessarily-
positive `r` with `E|r| = 1`, `E[|r|log|r|] ⩽ O(n^δ)`, and a nonzero rank one `L` with
`‖E[r vv^T] − L‖_F ⩽ ε‖L‖_F`. The Contract adds only Borel measurability and `μ`-integrability
of `r` (a *constraint on the object to be produced*, hence a strengthening of the burden, not an
easing) and pins the implicit constant in `O(n^δ)` to depend on `ε,δ` only. The artifact's claim
"Question 8.1 is answered affirmatively, as literally posed" and "This matches Conjecture
`conj:main` of the Contract with no additional hypothesis" is therefore a fair reading of the
quoted text, and the ambiguity in `O(·)` is moot because the delivered constant is
`ε`-independent (so footnote 8 / card Q7 is correctly declared moot). All eight quotations in
DEPENDENCIES were collated against cards Q1–Q9: wording matches, with the two truncations
recorded in Finding 6. The "deficient ⇒ nonnegative" gloss in Remark C.1 is exactly what card
Q9 licenses. No load-bearing external result is used: the Theorem depends only on Riesz,
Cauchy–Schwarz, Jensen, `‖Q‖_op ≤ ‖Q‖_F`, `μ(supp μ) = 1`, and `sup(log x)/x^δ = 1/(eδ)`,
all restated, all standard, all verified above.

**Step 9 — Corollary B.** Mathematics ACCEPTED, framing DEFECTIVE (Finding 5). On
`X = {rank 1, ‖X‖_F = 1}` (compact: rank `≤ 1` is closed, intersected with the unit sphere,
which excludes `0`), `G = {X ↦ α + ⟨A,X⟩}` contains the constant `1` and every coordinate
`X ↦ X_{ab}`, its elements are continuous and bounded on `X`, and `dim G ≤ n²+1`; so Lemmas
1–4 do transfer and give `E_μ[rX] = cX_0` exactly with entropy `≤ log(n²+1)`. The claimed
mechanism-diagnosis ("constants and coordinates in one finite-dimensional function space") is
supported by the proof as written.

**Step 10 — Remark C.3.** No defect recorded, but noted: the identification of `ev_{v_0}` /
Lemma 1(b) as "exactly what fails" for pseudo-distributions is a plausible diagnosis, not a
proved impossibility, and the phrase "the setting the paper actually needs" blurs the source's
two distinct consequences (card Q1: log rank via distributions; running time via
pseudo-distributions). I judge this a routine looseness in an explicitly diagnostic remark and
do not count it as a defect.

**Minor, not counted:** the labels `conj:main` (Corollary) and `def:signed` (Theorem proof)
refer to items not present in the artifact; both are recoverable from the GOAL section.

### SOURCE REQUEST ###

1. **For Finding 4 (Remark C.2, class C).** The step of Barak–Kothari–Steurer §2.2 / around
   Theorem 2.4 (p. 5) that actually converts a `k`-deficient reweighting into the submatrix
   `A_{I,I}` — i.e. whatever flattening or rounding argument sits between Definition 2.2 (card
   Q9) and the sentence quoted as card Q4 — together with the text supporting "It may improve
   the best known bound for the log rank conjecture to `Õ(n^δ)`" (card Q1). Card Q4 alone gives
   the flatness dictionary but not the mechanism by which a merely low-KL (let alone signed)
   reweighting is converted, so I cannot adjudicate whether "the log rank consequence does not
   follow" is correct or merely unproved. My web attempts to obtain §2.2 verbatim
   (arXiv:1701.06321 abstract page, PDF, ar5iv HTML) did not return usable text.
2. **For Finding 2 (class E).** The document the artifact calls "the review of this artifact",
   or, preferably, an in-artifact derivation of `μ{⟨v,v_0⟩² < 1/(n+2)}` for uniform `μ` on
   `S^{n-1}`. My own computation of that quantity is `2Φ(1) − 1 + o(1) ≈ 0.6827`, which
   contradicts the artifact's "1 − o(1)".
