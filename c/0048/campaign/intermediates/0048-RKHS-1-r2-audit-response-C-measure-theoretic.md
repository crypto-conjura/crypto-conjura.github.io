MODEL: opus

### VERDICT ###
STATUS: DEFECTS
The measure-theoretic and functional-analytic core (Lemmas 1–4, the Theorem, the
Corollary, Corollary B, Remark A) survives every attack I could mount and in my
judgment correctly proves the Contract statement — indeed strictly more than it —
but Remark C.1 contains a false quantitative claim (the negative set of the
uniform-measure kernel is asserted to have measure `1 − o(1)`; it has measure
`1/3` at `n = 2` and tends to `P(|Z| < 1) ≈ 0.6827`, never near `1`), which is a
class-B error even though it is non-load-bearing.

STEP 0 (completeness). The artifact ends with `### END OF ARTIFACT [P-1] ###`
(line 362). No unit stops mid-sentence, mid-equation or mid-proof; every lemma,
the Theorem, both Corollaries, Remarks A and C, the DEPENDENCIES block and the
NUMERICAL CHECK are closed with `∎` or a completed paragraph. Not truncated;
verification proceeds.

CLASS A CHECK FIRST — what the artifact actually proves, in my words.

For every `n ≥ 1` and every Borel probability measure `μ` on `S^{n-1}`, let
`F_μ ⊆ L²(μ)` be the (finite-dimensional) space of a.e.-classes of restrictions
of real quadratic forms to the sphere, `d = dim F_μ ∈ [1, n(n+1)/2]`. Then there
is a point `v_0 ∈ supp μ` at which the reproducing kernel `k = k_{v_0}` of `F_μ`
satisfies `E_μ[k²] = K(v_0,v_0) ≤ d`; the normalised function `r = k/E_μ|k|` is a
bounded polynomial, satisfies `E_μ|r| = 1`, satisfies
`E_μ[r(v)vv^T] = c·v_0v_0^T` **exactly** with `c = 1/E_μ|k| ∈ [d^{-1/2},1]`, and
has entropy cost `E_μ[|r|log|r|] ≤ log(c²K(v_0,v_0)) ≤ log K(v_0,v_0) ≤
log(n(n+1)/2)`. Hence (Corollary) the Contract holds with `C(ε,δ) = 2/(eδ)`,
independent of `ε`, and with Frobenius error identically `0`.

Diff against the Contract:
* Quantifier order: Contract wants `∀ε ∀δ ∃C ∀n ∀μ ∃(r,L)`. The artifact
  produces `C = 2/(eδ)` depending on `δ` only, before `n` and `μ` are seen, and
  `r, L` after. Order is correct; `C` is uniform in `n` and `μ` as demanded by
  Reading convention 1. No hidden `ε`- or `n`-dependence: `r` is constructed
  without reference to `ε`.
* Conclusion: the Contract asks for `‖E[r vv^T] − L‖_F ≤ ε‖L‖_F` with `L ≠ 0`
  rank one; the artifact delivers error `0` and `L = c v_0v_0^T` with
  `‖L‖_F = c ≥ (n(n+1)/2)^{-1/2} > 0`. Strictly stronger, and the strengthening
  is legitimate (`0 ≤ ε‖L‖_F` for every `ε > 0` precisely because `‖L‖_F > 0`;
  the artifact says so, line 181). `L` is not required symmetric/PSD by the
  Contract and being PSD is no cheat (Reading convention 3).
* Entropy: Contract's definition of "signed reweighting with entropy cost ≤ K"
  requires `r` Borel, `μ`-integrable, `E_μ|r| = 1`, `E_μ[|r|log|r|] ≤ K` with
  `0log0 := 0`. All four are checked (lines 176–177, 183–189). `log(n(n+1)/2) ≤
  (2/(eδ))n^δ` for all `n ≥ 1`: at `n = 1` the left side is `0`; for `n ≥ 2`,
  `n(n+1)/2 ≤ n²` and `log n ≤ n^δ/(eδ)`. Verified.
* No asymptotics stand in for constants; no "sufficiently large `n`"; `n = 1` is
  handled explicitly. `r` is allowed to depend on `μ` and `n`, which the Contract
  permits.

No class-A drift. The artifact proves the Contract statement and more.

### FINDINGS ###

| quoted location | class A-E | explanation |
|---|---|---|
| Remark C.1, "negative on `{⟨v,v_0⟩² < 1/(n+2)}`, a set of `μ`-measure `1 − o(1)` (exact check recorded in the review of this artifact; not re-derived here)" (lines 258–260) | **B** (non-load-bearing) | The kernel formula itself is right — I verified `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2` independently: `E_μ[k] = (n(n+2)/2)(1/n) − n/2 = 1`; `k(v_0) = n(n+1)/2 = d`; `E[k v_1²] = (n(n+2)/2)(3/(n(n+2))) − 1/2 = 1`, `E[k v_2²] = 1/2 − 1/2 = 0`, `E[k v_1v_2] = 0` for `v_0 = e_1`; and for `n = 2` it reduces to `4cos²φ − 1 = 1 + 2cos 2φ`, which is exactly the kernel I computed from scratch for the uniform measure on `S^1`. But the *measure* of the negative set is not `1 − o(1)`. With `t = ⟨v,v_0⟩`, the negative set is `{t² < 1/(n+2)}` and `μ` of it equals `P(|t| < (n+2)^{-1/2})`. At `n = 2`, `t = cos φ` with `φ` uniform, so this is `P(|cos φ| < 1/2) = 1/3` exactly (cross-check: `1 + 2cos 2φ < 0 ⟺ 2φ ∈ (2π/3, 4π/3) mod 2π`, measure `1/3`). At `n = 3`, `t` is uniform on `[−1,1]`, giving exactly `1/√5 ≈ 0.447`. As `n → ∞`, `n t² ⇒ χ²_1` and the threshold `n/(n+2) → 1`, so the measure tends to `P(χ²_1 < 1) = P(|Z| < 1) ≈ 0.6827`. The negative set therefore has measure in `[1/3, 0.6827)`, bounded away from `1`; equivalently the *positive* set retains measure `≈ 0.317`, not `o(1)`. The claim is false as stated. It is not load-bearing: Remark C.1 only needs the negative set to have positive measure (which is true, and also follows from `E_μ|k| > 1`), and no lemma, the Theorem, the Corollary or Corollary B consumes this number. The deferral "exact check recorded in the review of this artifact" points at a document not in the record, so the claim is also unsupported inside the artifact. |
| Remark C.1, "so a conflict would require our construction to come out nonnegative on the hard `μ`. **It does not.**" (lines 256–257) | C (routine, non-load-bearing) | The general assertion "it does not" is discharged only for the single instance `μ = ` uniform, followed by the honest disclaimer "(No claim is made that the construction's `r` is signed for *every* non-point-mass `μ`.)" A reader can fill this without effort — on any `μ` where every nonnegative reweighting costs `ω(log n)`, the constructed `r` (cost `≤ log(n(n+1)/2)`) is necessarily not a.e. nonnegative, since a nonnegative `r` with `E_μ|r| = 1` *is* a nonnegative reweighting. I flag it as reported-but-not-forcing per the prompt's instruction. It has no downstream consumer. |
| Proof plan, "Its `L²` norm averages to `d` over `μ`" (line 43) | C (typo, routine) | It is the *squared* `L²` norm, `K(v,v) = ‖k_v‖²`, that averages to `d` (Lemma 3, eq. (3)). Lemma 3 states it correctly; the plan sentence is loose. Fixed by inserting "squared"; nothing depends on it. |
| Lemma 3 display, "`∫ K(v,v) dμ(v) = d`" (line 119) | C (routine, and explicitly handled) | As literally written the integrand is undefined on `(supp μ)^c`, because `ev_v` — hence `k_v`, hence `K(v,v)` — is only constructed for `v ∈ supp μ` (Lemma 1(b),(c)). The proof repairs this in place: it integrates the everywhere-defined polynomial `g = Σ_j q_j²`, notes via (P1) that `g = K(·,·)` off a null set, and adds "(…off the support nothing below uses `g`.)" So the statement is a notational abbreviation for `∫_{supp μ} K(v,v) dμ`, and the value `d` is correct. Routine; I record it only because my brief was to read this clause with maximum suspicion. |
| DEPENDENCIES, "Footnote 7, p. 6, **verbatim**: … 'having a `1 − 1/O(n)` fraction of its entries equal.'" (lines 338–340) | C (quotation hygiene) | Compared against card item Q6, the quotation is truncated before the footnote's final sentence ("In this paper we are more concerned with rectangles whose distance to being rank one (or monochromatic) is some `ε > 0` …") with no ellipsis, while being labelled verbatim. The omission changes nothing the artifact infers — footnote 7 is quoted for context and is used in no argument — so this is hygiene, not misuse of an external result, and I do not classify it as (D). |

No class-A, no class-D, no class-E defect found. The single class-B item is
confined to a remark the artifact itself labels "diagnosis for the review" and
does not touch the resolution of the Contract.

### SOURCE REQUEST ###
none

### STEP LOG ###

Preliminaries.
* (P1) `μ(supp μ) = 1`. ACCEPTED. `(supp μ)^c = ∪{U open : μ(U) = 0}`; `S^{n-1}`
  is second countable hence hereditarily Lindelöf, so this open set is a
  *countable* union of members of that family, hence null. The artifact's
  one-line version compresses the Lindelöf step but is correct. Works for `n = 1`
  (`S^0` two points, discrete) as well.
* (P2) `v ∈ supp μ`, `U ∋ v` open `⟹ μ(U) > 0`. ACCEPTED (definition of support).

Lemma 1(a). ACCEPTED. `Q ↦ q_Q` linear on `Sym_n` so `F_μ` is a linear image and
`d ≤ dim Sym_n = n(n+1)/2`; `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F` for `‖v‖₂ = 1` and `Q`
symmetric; `μ` a probability measure gives `L^∞(μ) ⊆ L²(μ)`. Note also `d ≥ 1`
(the class `[1] = [q_I]` is nonzero in `L²(μ)`), which Lemma 3 needs to speak of
an orthonormal basis `f_1,…,f_d`; this is implicit but immediate from 1(d).

Lemma 1(b) — THE CLAUSE I WAS ASKED TO DISTRUST. ACCEPTED as stated, and what is
proved is exactly what is later consumed.
* The proof: `h := q_{Q−Q'}` is a polynomial, hence continuous on `S^{n-1}`, with
  `μ({h ≠ 0}) = 0`. If `h(v_0) ≠ 0` for `v_0 ∈ supp μ` then
  `U := {|h| > |h(v_0)|/2}` is open (continuity), contains `v_0`, so `μ(U) > 0`
  by (P2); yet `U ⊆ {h ≠ 0}` is null. Contradiction. Correct; continuity is
  genuinely available and is the only regularity used.
* Well-definedness of `ev_v` on the *quotient*: this is the crux and it is clean.
  `F_μ` is *defined* as the set of classes that admit a quadratic-form
  representative, and `ev_v` is *defined* through such a representative. Two
  quadratic-form representatives of the same class differ by `q_{Q−Q'} = 0`
  `μ`-a.e., so (b) forces equal values at every `v ∈ supp μ`. Hence `ev_v` is a
  genuine function on `F_μ` for `v ∈ supp μ`. Linearity: `[q_Q] + λ[q_{Q'}] =
  [q_{Q+λQ'}]` and `q_{Q+λQ'}(v) = q_Q(v) + λ q_{Q'}(v)`.
* Adversarial probe. The obvious trap is a class of `F_μ` with a *non-quadratic*
  representative that disagrees at `v` — e.g. modify a polynomial on a null
  subset of `supp μ`. This does not break anything, because `ev_v` is never
  applied to such a representative; the definition quantifies over
  quadratic-form representatives only, and no later step evaluates a
  non-polynomial representative pointwise. Scope check on every consumer:
  Lemma 1(c) needs `ev_v` linear on `F_μ` at `v ∈ supp μ` ✓; Lemma 2 applies
  `ev_{v_0}` to `[1]` and to `g_{ab}` at `v_0 ∈ supp μ` ✓; Lemma 3 needs
  `ev_v(f_j) = q_j(v)` for `v ∈ supp μ` ✓; the Theorem's `v_0` comes from
  Lemma 3 and lies in `supp μ` ✓. Point evaluation is *never* used off the
  support. Neither more nor less than (b) provides is consumed.
* Second-order probe: a measure on a proper quadric. Take `n = 3`, `μ` uniform on
  the great circle `{v_3 = 0}`. Then `q_{e_3e_3^T} = v_3²` vanishes `μ`-a.e., so
  `[q_{e_3e_3^T}] = 0` in `F_μ` — and indeed `v_3² = 0` at *every* support point,
  exactly as (b) predicts; `d` drops to `3 < 6`. No inconsistency, and the
  degeneracy only improves the final bound (`log d`, not `log(n(n+1)/2)`). Same
  for `μ` on a great subsphere `S^{m-1} ⊂ S^{n-1}`: `d = m(m+1)/2`.

Lemma 1(c). ACCEPTED. `F_μ` is a finite-dimensional subspace of `L²(μ)`, hence a
Hilbert space, and — this is the reason the quotient was taken — the `L²(μ)`
form is *positive definite* on it, not merely semi-definite, so Riesz applies.
Every linear functional on a finite-dimensional inner-product space is bounded
and has a unique representer. `k_v = Σ_j ev_v(f_j) f_j` is correct
(`⟨k_v,f_j⟩ = ev_v(f_j)`), and `K(v,v) = ‖k_v‖² = ev_v(k_v)` follows by taking
`f = k_v`. No operator is inverted anywhere and no Gram matrix is assumed
invertible; the basis is obtained by Gram–Schmidt.

Lemma 1(d). ACCEPTED. `q_I(v) = ‖v‖₂² ≡ 1` on `S^{n-1}` — the one place the
sphere constraint is used, and it is used correctly; `q_{E_{ab}}(v) = v_av_b`
with `E_{ab} = (e_ae_b^T + e_be_a^T)/2 ∈ Sym_n`.

Lemma 2(i). ACCEPTED. `g_{ab} = [q_{E_{ab}}] ∈ F_μ` by 1(d), so
`E_μ[k v_av_b] = ⟨k, g_{ab}⟩ = ev_{v_0}(g_{ab}) = (v_0)_a(v_0)_b`, entrywise for
all `a,b`, giving `E_μ[k vv^T] = v_0v_0^T` **exactly**. Both sides
representative-independent. Absolute convergence: `k` bounded by 1(a),
`|v_av_b| ≤ 1`. No interchange of limits, no Fubini, no monotone/dominated
convergence is needed anywhere in Lemmas 2–4 — every manipulation is a finite
sum or a single integral of a bounded function against a probability measure.

Lemma 2(ii). ACCEPTED. `E_μ[k] = ⟨k,[1]⟩ = ev_{v_0}([1]) = q_I(v_0) = 1`; then
`E_μ|k| ≥ |E_μ k| = 1` and `K(v_0,v_0) = E_μ[k²] ≥ (E_μ|k|)² ≥ 1` by
Cauchy–Schwarz against `1`; `E_μ[k] = 1 ≠ 0` forces `k ≠ 0`. The structural note
(that (ii) is the trace of (i)) is correct: `tr E_μ[k vv^T] = E_μ[k‖v‖²] =
E_μ[k]` and `tr(v_0v_0^T) = 1`.

Lemma 2(iii). ACCEPTED. `E_μ[k²] = ‖k‖² = K(v_0,v_0) < ∞` (boundedness);
`E_μ|k| ≤ (E_μ k²)^{1/2}` by Cauchy–Schwarz.

Lemma 3 — THE AVERAGING/CHRISTOFFEL STEP. ACCEPTED.
* `K(v,v) = Σ_j q_j(v)² =: g(v)` for `v ∈ supp μ`: from `k_v = Σ_j ev_v(f_j) f_j`
  with `ev_v(f_j) = q_j(v)` (legitimate by 1(b)), plus Parseval for an
  orthonormal basis. Independence of the choice of basis and representatives on
  `supp μ` follows from uniqueness in 1(c), as the artifact notes.
* Well-definedness off the support: `g` is a polynomial, defined and bounded
  everywhere, and equals `K(·,·)` on the full-measure set `supp μ`. Off the
  support `g` depends on the choices, and the artifact explicitly quarantines
  this ("off the support nothing below uses `g`"). I checked every downstream use
  and the quarantine holds: `A = {g ≤ d}` is formed globally but only
  `A ∩ supp μ` is used, and there `g = K(·,·)` canonically. The value of the
  integral is unaffected by the choices because `μ((supp μ)^c) = 0`.
* `∫ g dμ = Σ_j ∫ q_j² dμ = Σ_j ‖f_j‖² = d`. ACCEPTED: finite sum, each `q_j²`
  bounded hence integrable, so the exchange of `Σ` and `∫` is trivial; and
  `∫ q_j² dμ = ‖f_j‖²_{L²(μ)} = 1` because `q_j` represents the unit vector
  `f_j`. This is the identity `∫K dμ = tr P` and it is proved from scratch, with
  no appeal to an uncited source.
* "positive measure delivers a point in the support" — THE STEP I WAS ASKED TO
  BREAK. ACCEPTED. If `μ(A) = 0` then `h := g − d > 0` `μ`-a.e. while
  `∫ h dμ = 0`; a `μ`-a.e. nonnegative function with zero integral vanishes
  a.e., so `h = 0` `μ`-a.e., incompatible with `h > 0` `μ`-a.e. under a measure
  of total mass `1 > 0`. Hence `μ(A) > 0`. Then `μ(A \ supp μ) ≤
  μ((supp μ)^c) = 0` by (P1), so `μ(A ∩ supp μ) = μ(A) > 0` and in particular
  `A ∩ supp μ ≠ ∅`. This is exactly the "measure-zero exception treated as
  empty" trap and the artifact does not fall into it: it does not claim `A` is
  nonempty and then evaluate at an arbitrary point of `A`, it intersects with the
  support first. Any `v_0 ∈ A ∩ supp μ` has `K(v_0,v_0) = g(v_0) ≤ d`.
* Adversarial probes of Lemma 3. (i) Atomic `μ` with tiny atoms: `n = 2`,
  atoms at `(1,0),(0,1),(1,1)/√2` with weights `p_1 = 0.001, …`. Here `F_μ` is
  all of `R³`, `d = 3`, `K(v_i,v_i) = 1/p_i`, and `∫K dμ = Σ p_i/p_i = 3 = d` ✓;
  the averaging step correctly rejects the light atom `v_1` (`K = 1000 > 3`) and
  lands on an atom of weight `≥ 1/3`. So the argument does *not* silently pick a
  bad support point. (ii) `μ` uniform on `{e_1,…,e_n}`: `d = n`,
  `K(e_i,e_i) = n` for all `i`, `k = n·1_{e_i}`, cost `log n = log d` ✓ — note
  `r ≥ 0` here, consistent with the artifact's disclaimer. (iii) `μ` with
  `d = 1`: then every `v_av_b` is `μ`-a.e. constant, hence by 1(b) constant on
  `supp μ`, so `supp μ ⊆ {±v_0}` and `E_μ[vv^T] = v_0v_0^T` — the Theorem's
  conclusion with `k ≡ 1`. Consistent; no hidden assumption that `d` is full.

Lemma 4. ACCEPTED. `φ(t) = t log t` satisfies `φ ≥ −1/e` on `[0,∞)` and
`φ(t) ≤ t²` (for `t ≥ 1` from `log t ≤ t`; for `t < 1` from `φ ≤ 0`), so
`φ(|r|)` is squeezed between an integrable constant and `r² ∈ L¹`, hence
integrable and the entropy is a finite real. `dν := |r|dμ` is a probability
measure since `E_μ|r| = 1`; `ν({r = 0}) = ∫_{\{r=0\}}|r|dμ = 0`, so `|r| > 0`
`ν`-a.e. and `E_ν[log|r|] = E_μ[|r|log|r|]` with the `0log0 = 0` convention
accounted for exactly on the `ν`-null set `{r = 0}`; `E_ν[|r|] = E_μ[r²] < ∞`.
Jensen for the concave `log` against the probability measure `ν` applied to the
`ν`-a.e. positive, `ν`-integrable `|r|` gives `E_ν[log|r|] ≤ log E_ν[|r|]`. The
inequality direction is right (this is the standard "`χ²` dominates KL" bound).
The sharpness remark is also correct: strict concavity of `log` gives equality
iff `|r|` is `ν`-a.e. constant, i.e. `|r| ∈ {0,c}` `μ`-a.e., whence
`c = 1/μ({|r| = c})` and the bound reads `log(1/μ({|r| = c}))`.

Proof of the Theorem. ACCEPTED. `c = 1/E_μ|k|` is well defined and positive
(`1 ≤ E_μ|k| < ∞`) and lies in `[K(v_0,v_0)^{-1/2}, 1] ⊆ [(n(n+1)/2)^{-1/2},1]`.
`r := q_{cQ_k}` for any `Q_k` with `[q_{Q_k}] = k` is a bounded polynomial, hence
Borel and `μ`-integrable — the Contract's regularity clause (Reading convention 2)
is met and nothing extra is assumed. `E_μ|r| = 1`. `E_μ[r vv^T] = c v_0v_0^T = L`
is rank one (`c > 0`, `‖v_0‖ = 1`), nonzero, `‖L‖_F = c > 0`, so error
`0 ≤ ε‖L‖_F` for every `ε > 0`. Entropy: `E_μ[r²] = c²K(v_0,v_0) =
K(v_0,v_0)/(E_μ|k|)² ≤ K(v_0,v_0) ≤ d ≤ n(n+1)/2`, so Lemma 4 gives
`E_μ[|r|log|r|] ≤ log K(v_0,v_0) ≤ log(n(n+1)/2)`. All choices of `Q_k` give the
same class, hence the same `E_μ[r vv^T]`, `E_μ|r|` and entropy; the arbitrariness
of `Q_k` is harmless and no claim is made about `r` off `supp μ`.

Corollary (the Contract). ACCEPTED. `n = 1`: `log 1 = 0 ≤ C`. `n ≥ 2`:
`n(n+1)/2 ≤ n²` (⟺ `n ≥ 1`), `log(n(n+1)/2) ≤ 2 log n`, and
`max_{x>0}(\log x)/x^δ = 1/(eδ)` at `x = e^{1/δ}` (checked: `(1/δ)e^{-1}`), so
`2 log n ≤ (2/(eδ))n^δ`. `C(ε,δ) = 2/(eδ)` is finite, independent of `n`, `μ` and
`ε`. Spot-checked at `(δ,n) = (10,2)` and `(0.01,2)`.

Remark A. ACCEPTED (not load-bearing, but correct). `‖M − tuw^T‖_F² = ‖M‖_F²
− 2t·u^TMw + t²`; maximising `u^TMw` over unit `u,w` gives `s_1(M) = |λ_1|` and
only helps since `t > 0`; the discriminant condition `s_1² ≥ (1−ε²)‖M‖_F²`
rearranges to `Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1²`; for `M ≠ 0` both roots are
positive so an admissible `t > 0` exists exactly then; `ε ∈ (0,1)` keeps
`1−ε² > 0`. The `M = 0` case is right too. This confirms that the Contract's
relative normalisation is not being exploited degenerately.

Corollary B. ACCEPTED. `X = {ab^T : ‖a‖ = ‖b‖ = 1}` is compact (continuous image
of a compact set) and metric, hence second countable, so (P1)/(P2) transfer.
`G = span{1} + {X ↦ ⟨A,X⟩}` has `dim ≤ n²+1`, its elements are affine hence
continuous (Lemma 1(b) transfers) and bounded on `X` (`|α + ⟨A,X⟩| ≤ |α| +
‖A‖_F` since `‖X‖_F = 1`; Lemma 1(a) transfers). `1 ∈ G` gives `E_μ[k] = 1`;
`X ↦ X_{ab} ∈ G` gives `E_μ[k X] = X_0`; Lemma 3 gives `K(X_0,X_0) ≤ d ≤ n²+1`
at some `X_0 ∈ supp μ`; Lemma 4 is measure-theoretic and transfers verbatim. The
list of "only two properties used" is slightly incomplete as stated but the two
omitted ones (finite dimension, continuity/boundedness) are supplied in the very
next sentence, so I record no defect. `X_0` is rank one by membership in `X` and
`c > 0`, so `cX_0` is rank one and nonzero.

Remark C.1. DEFECT (class B) on the `1 − o(1)` measure claim; see FINDINGS. The
surrounding reasoning is otherwise sound: "deficient" is nonnegative by card item
Q9 (a probability distribution), both quoted claims are worst-case over `μ`, and
`E_μ|k| > E_μ[k] = 1` does imply `k < 0` on a set of positive measure. The
general assertion "It does not" is under-supported (class C above).

Remark C.2. ACCEPTED as a self-limitation. The flatness dictionary (card Q4)
indeed requires flatness, which the Theorem does not supply; the artifact
correctly declines to claim a log-rank consequence, so there is no inflated
claim to police here.

Remark C.3. ACCEPTED as commentary. The identification of `ev_{v_0}`/Lemma 1(b)
as the step with no pseudo-distribution analogue is consistent with the proof as
written: `supp μ` is used in 1(b), 1(c), Lemma 2 (via `v_0`), Lemma 3 (twice) and
the Theorem, so the honest-distribution hypothesis really is load-bearing.

DEPENDENCIES block. Riesz on a finite-dimensional inner-product space,
Cauchy–Schwarz in `L²(μ)`, Jensen against a probability measure,
`‖Q‖_op ≤ ‖Q‖_F`, `μ(supp μ) = 1` on a second-countable space, and
`max_{x>0}(log x)/x^δ = 1/(eδ)` are all standard and all restated in usable form;
none is a black box and none is misapplied. The BKS quotations were checked one
by one against card S1: Q1 (Question 8.1 and its follow-up), Q2 (Theorem 2.3),
Q4 (flatness), Q5 (tightness), Q7 (footnote 8), Q8 (§2.3), Q9 (Definition 2.2)
all match verbatim and are used only for the "this answers Question 8.1" framing
and the self-limitations; the footnote-7 quotation is truncated without ellipsis
(hygiene note above). No external result is load-bearing for the mathematics, so
there is no class-D or class-E exposure.

NUMERICAL CHECK (recomputed independently). `n = 2`, uniform on
`(1,0),(0,1),(1,1)/√2,(1,−1)/√2`. Quadratic-form values are
`(Q_{11}, Q_{22}, (Q_{11}+Q_{22})/2 + Q_{12}, (Q_{11}+Q_{22})/2 − Q_{12})`, so
`F_μ = {x : x_1+x_2 = x_3+x_4}` and `d = 3` ✓. Solving `(1/4)k − e_1 ⊥ F_μ` with
`k ∈ F_μ` gives `k = (3,−1,1,1)` ✓; `E_μ[k] = 1` ✓; `‖k‖² = 3 = d` ✓;
`E_μ[k vv^T] = (1/4)[[4,0],[0,0]] = v_1v_1^T` ✓; `E_μ|k| = 3/2`, `c = 2/3`,
`r = (2,−2/3,2/3,2/3)`, `E_μ|r| = 1` ✓, entropy `= (1/4)(2log2 + 2log(2/3)) =
0.14384` and `E_μ[r²] = 4/3` with `log(4/3) = 0.28768` ✓, both `≤ log 3` ✓, and
`r` is genuinely signed ✓. I also ran the construction from scratch on `μ`
uniform on `S^1` (`d = 3`, `k(φ) = 1 + 2cos2φ`, `E[k vv^T] = e_1e_1^T` exactly,
`E|k| = (2π/3 + 4√3)/(2π) ≈ 1.436`, `c ≈ 0.696`, entropy `≤ log(3c²) ≈ 0.374`)
and on `μ` uniform on `S^{n-1}` for general `n` (kernel as in Remark C.1;
`c = Θ(1/n)`, `E[r²] = Θ(1)`, entropy `O(1)`), on point masses, on `{±v_0}`, on
`{e_1,…,e_n}`, on a great subsphere and on a proper quadric. In every case the
identity `E_μ[r vv^T] = c v_0v_0^T` held exactly and the entropy bound held. I
could not construct a `μ` that breaks any step.

Bottom line for my angle: the quotient/point-evaluation clause, the
`∫K dμ = d = dim` identity (including the off-support representative question),
the positive-measure-meets-support step, and all integrability and Jensen /
Cauchy–Schwarz steps are correct as written; nothing assumes finite support, an
invertible operator, or a full-dimensional `F_μ`. The only error I found is the
false `1 − o(1)` in Remark C.1, which the Theorem, the Corollary, Corollary B and
Remark A do not depend on.
