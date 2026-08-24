# AUDIT — Line-by-line algebraic re-derivation of 0048-RKHS-1-r6

**Scope.** Cold read of CONTRACT.md, S1-bks-q81-card.md, and
0048-RKHS-1-r6.md only. No other intermediate, triage, or revision-history
file was read (per instructions), beyond the REVISION LOG appended inside
r6.md itself, which was read only to confirm completeness of the artifact
(STEP 0), not consulted as evidence for or against the mathematics.

## STEP 0 — Completeness gate

The file contains `### END OF ARTIFACT [0048-RKHS-1-r6] ###` (line 441),
followed only by a REVISION LOG section, which is declared front-matter/
metadata, not a mathematical claim. The artifact is not truncated. Proceeding
to full review.

## Statement drift (Class A) check

Contract: ∀ε,δ>0 ∃C(ε,δ)<∞ (indep. of n, μ) s.t. ∀n, ∀ Borel probability μ on
S^{n-1}, ∃ signed reweighting r of entropy cost ≤ C·n^δ and nonzero rank-one
L with ‖E_μ[r vv^T] − L‖_F ≤ ε‖L‖_F.

Artifact's Theorem proves something stronger and consistent with this: for
every n, μ, it exhibits r, L with the *exact* identity E_μ[r vv^T] = L (error
0) and entropy ≤ log(n(n+1)/2), and the Corollary repackages this as
C(ε,δ) = 2/(eδ) (independent of ε, since 0 ≤ ε‖L‖_F holds for every ε>0
whenever L≠0). This is a legitimate special case of the Contract's quantifier
structure (a solver is permitted to produce a C that happens not to depend on
ε; the Contract only requires *existence* of a valid C(ε,δ)). No drift found
between the theorem actually proved and Question 8.1 / the Contract.

## Line-by-line algebraic re-derivation

All of the following were independently re-derived symbolically from the
stated hypotheses, not merely read for plausibility.

**Lemma 1.** (a) `|v^TQv| ≤ ‖Q‖_op‖v‖² = ‖Q‖_op ≤ ‖Q‖_F` — correct (operator
norm of a symmetric matrix is its largest |eigenvalue|, dominated by the
Frobenius norm = ℓ²-norm of the eigenvalues). `d ≤ n(n+1)/2` — correct, image
of the linear map `Q ↦ [q_Q]` from `Sym_n` (dimension `n(n+1)/2`).
(b) The open-set/support argument is a correct, standard "continuous function
vanishing a.e. on the support of a measure vanishes on the whole support"
argument; verified the logic of the contrapositive (`U:={|h|>|h(v_0)|/2}` is
open, contains `v_0`, is a subset of the null set `{h≠0}`, forcing
`μ(U)=0`, contradicting `μ(U)>0` from `v_0∈supp μ`). Correct.
(c) Finite-dimensional Riesz representation — correct, and the explicit
formula `k_v = Σ_j ev_v(f_j) f_j` for an orthonormal basis is the standard
one.
(d) `q_I(v)=‖v‖²=1` on `S^{n-1}` — correct. `q_{E_{ab}}(v) = v^T E_{ab} v
= v_av_b` — re-derived directly: `v^T(e_ae_b^T+e_be_a^T)v/2 =
(v_av_b+v_bv_a)/2 = v_av_b`. Correct.

**Lemma 2.** (i) `E_μ[k v_av_b] = ⟨k,g_{ab}⟩ = ev_{v_0}(g_{ab}) =
(v_0)_a(v_0)_b` for every `(a,b)`, hence the matrix identity — correct,
directly from the reproducing property and Lemma 1(d).
(ii) `E_μ[k]=⟨k,[1]⟩=1`; `E_μ|k|≥|E_μ k|=1`; Cauchy–Schwarz
`(E|k|)² ≤ E[k²]·E[1²] = E[k²]` gives `K(v_0,v_0) ≥ 1` — re-derived and
correct in both direction and constant.
(iii) `K(v_0,v_0)=E_μ[k²]` is definitional; `E_μ|k| ≤ K(v_0,v_0)^{1/2}` is
Cauchy–Schwarz against the constant `1` — correct.
Structural note: `tr(v_0v_0^T)=‖v_0‖²=1` and
`tr E_μ[k vv^T] = E_μ[k‖v‖²]=E_μ[k]` — re-derived, correct, and it is exactly
the trace of (i).

**Lemma 3.** `k_v = Σ_j q_j(v) f_j` (Parseval expansion of the Riesz
representer in an orthonormal basis) gives
`K(v,v)=‖k_v‖² = Σ_j q_j(v)²` for `v∈supp μ` — correct.
`∫K(v,v)dμ = Σ_j∫q_j²dμ = Σ_j‖f_j‖² = d` since `(f_j)` orthonormal — correct
arithmetic (each of the `d` terms contributes exactly `1`).
The averaging argument for existence of a cheap `v_0` (`A:={g≤d}`,
contradiction from `h:=g-d>0` a.e. with `∫h dμ=0` forcing `h=0` a.e.) is a
correct, standard "cannot be above average everywhere" argument, and the
subsequent step `μ(A)>0 ⟹ A∩supp μ≠∅` (else `A` would be null, being a subset
of the complement of `supp μ`) is correctly reasoned.

**Lemma 4.** `φ(t)=t log t`: re-derived `φ(t)≥-1/e` for `t≥0` (minimum at
`t=1/e`, value `-1/e`, via `φ'(t)=log t+1=0`) — correct.
`φ(t)≤t²`: for `t≥1`, `log t < t` (standard, from `log t ≤ t-1 < t`) so
`t log t < t²`; for `t<1`, `φ(t)≤0≤t²` — correct, and correctly used to
establish `φ(|r|)∈L¹(μ)` via domination.
`E_ν[log|r|]=E_μ[|r|log|r|]` and `E_ν[|r|]=E_μ[r²]` for `dν=|r|dμ` — both
re-derived and correct (`∫|r|·|r|dμ=∫r²dμ`).
Jensen `E_ν[log|r|] ≤ log E_ν[|r|]` — correct application of Jensen for
concave `log` against the probability measure `ν`.

**Proof of the Theorem.** `c:=1/E_μ|k| ∈ [K(v_0,v_0)^{-1/2},1]` — correct,
reciprocal of a quantity in `[1,K(v_0,v_0)^{1/2}]`.
`E_μ|r| = c·E_μ|k| = 1` — correct.
`E_μ[r vv^T]=c v_0v_0^T=:L`, `‖L‖_F = c‖v_0v_0^T‖_F = c‖v_0‖² = c` (re-derived
`‖v_0v_0^T‖_F=‖v_0‖²=1` directly) — correct; error is exactly `0`.
Entropy chain: `E_μ[r²]=c²E_μ[k²]=c²K(v_0,v_0)=K(v_0,v_0)/(E_μ|k|)²` —
re-derived and correct; since `E_μ|k|≥1`, this is `≤K(v_0,v_0)≤n(n+1)/2` —
correct monotonicity and correct final bound via Lemma 4 + Lemma 3.

**Corollary.** `n=1`: `n(n+1)/2=1`, `log 1=0` — correct.
`n≥2`: `n(n+1)/2 ≤ n²` ⟺ `n+1≤2n` ⟺ `n≥1` — checked, holds (with equality at
`n=1`, strict for `n≥2`); `log(n(n+1)/2)≤2log n` — correct.
`max_{x>0}(log x)/x^δ = 1/(eδ)` at `x=e^{1/δ}`: re-derived via
`d/dx[(log x)/x^δ] ∝ x^{δ-1}(1-δ log x)=0 ⟹ log x=1/δ`, and
`f(e^{1/δ}) = (1/δ)/e^{δ·(1/δ)} = (1/δ)/e = 1/(eδ)` — independently confirmed
correct.
Hence `2 log n ≤ (2/(eδ))n^δ` for all `n` (including `n=1`, trivially
`0≤`positive) — correct, giving `C(ε,δ)=2/(eδ)`.

**Remark A.** `‖L‖_F=t`, `‖M-L‖_F² = ‖M‖_F² - 2t·u^TMw + t²` — re-derived by
direct bilinear expansion of the Frobenius inner product, matches (using
`⟨M,uw^T⟩=u^TMw`, verified from `⟨A,B⟩_F=ΣA_{ij}B_{ij}`).
`(1-ε²)t² - 2(u^TMw)t + ‖M‖_F² ≤ 0`: correctly rearranged from
`‖M-L‖²≤ε²t²`. Maximizing `u^TMw` over unit `u,w` gives the top singular
value `s_1(M)=|λ_1|` for symmetric `M` — correct.
Discriminant condition `s_1² ≥ (1-ε²)‖M‖_F²` rearranges (using
`‖M‖_F²=Σλ_i²=λ_1²+Σ_{i≥2}λ_i²`) to
`Σ_{i≥2}λ_i² ≤ (ε²/(1-ε²))λ_1²` — independently re-derived and confirmed
algebraically identical to the stated inequality.
Vieta: product of roots `=‖M‖_F²/(1-ε²)>0` (since `M≠0`), sum
`=2s_1/(1-ε²)>0` (since `s_1=|λ_1|>0` when `M≠0`) — correct, both roots
positive when real.

**Corollary B.** Dimension bound `dim G ≤ n²+1` — correct (parametrized by
`(α,A)∈R×R^{n×n}`, dimension `1+n²`). `[1]∈G` via `(α,A)=(1,0)`; `X↦X_{ab}∈G`
via `(α,A)=(0,e_ae_b^T)` — correct. The transfer of Lemmas 1-4 is asserted by
analogy (compactness of `X`, continuity giving Lemma 1(b), boundedness giving
Lemma 1(a)); this is a legitimate structural transfer — the *only* properties
of `F_μ` actually used anywhere in Lemmas 1-4 are (i) finite dimension, (ii)
containment of the constant function, (iii) containment of the relevant
coordinate functions, (iv) elements continuous/bounded on a compact domain,
and (v) an inner-product/L² structure — all five hold for `G` on `X` exactly
as claimed. No gap found in the transfer.

**Remark C(i), new paragraph (the specifically flagged computation).**
`dμ' := k dμ` a probability measure (from the transferred Lemma 2(ii)
analogue, `E_μ[k]=1`); `E_{μ'}[X]=X_0` (from the transferred Lemma 2(i)
analogue applied entrywise via `X_{ab}∈G`). Then, independently re-derived:

    E_{μ'}‖X−X_0‖_F² = E_{μ'}‖X‖_F² − 2⟨X_0,E_{μ'}X⟩ + ‖X_0‖_F²

by direct bilinear expansion of `‖X−X_0‖_F² = ‖X‖_F² − 2⟨X,X_0⟩ + ‖X_0‖_F²`
and linearity of `E_{μ'}` and of `⟨X_0,·⟩`. Since every `X∈X` has `‖X‖_F=1`
by definition of the domain `X`, `E_{μ'}‖X‖_F²=1`. Since `E_{μ'}[X]=X_0`,
`⟨X_0,E_{μ'}X⟩=⟨X_0,X_0⟩=‖X_0‖_F²=1` (as `X_0∈X` forces `‖X_0‖_F=1`). Hence

    E_{μ'}‖X−X_0‖_F² = 1 − 2·1 + 1 = 0,

exactly as the artifact states. This is the correct, fully checked
computation. The subsequent step ("nonnegative integrand with vanishing
integral vanishes a.e." ⟹ `μ'({X_0})=1`) is correct, as is
`1 = ∫_{\{X_0\}} k dμ = K(X_0,X_0)·μ({X_0})` (re-derived: total mass of `μ'`
is concentrated at `X_0`, and `k(X_0)=K(X_0,X_0)` by the transferred
Lemma 1(c)), giving `μ({X_0}) = 1/K(X_0,X_0) ≥ 1/(n²+1)` via the transferred
Lemma 3 bound `K(X_0,X_0)≤dim G≤n²+1`. The final entropy computation
`log(1/μ({X_0})) = log K(X_0,X_0) ≤ log(n²+1)` is correct and matches the
bound already proved for Corollary B's own `r`.

**Numerical check, independently reproduced.** `n=2`,
`v_1=(1,0),v_2=(0,1),v_3=(1,1)/√2,v_4=(1,-1)/√2`. Evaluation of a general
quadratic form `q_Q` at the four points, expressed in coordinates
`x_i=q_Q(v_i)`, gives the linear constraint `x_3+x_4=x_1+x_2`, confirming
`F_μ={x∈R^4 : x_1+x_2=x_3+x_4}`, `d=3` — reproduced exactly.
Solving for the reproducing kernel at `v_0=v_1` under the constraint
`k∈F_μ` and `(1/4)k·x=x_1` for all `x` in the 3-dimensional subspace: setting
`x_4=x_1+x_2-x_3` and matching coefficients gives the linear system
`k_1+k_4=4, k_2+k_4=0, k_3=k_4`, uniquely solved by `k=(3,-1,1,1)` —
independently re-derived and matches the artifact's claimed kernel exactly.
`E_μ[k]=(1/4)(3-1+1+1)=1` ✓. `K(v_0,v_0)=(1/4)(9+1+1+1)=3=d` ✓.
`E_μ[k vv^T] = (1/4)(3v_1v_1^T-v_2v_2^T+v_3v_3^T+v_4v_4^T)`: computed
directly as `(1/4)diag(4,0)... ` — full 2×2 matrix arithmetic gives
`[[4,0],[0,0]]/4 = v_1v_1^T` ✓ (independently recomputed: `3v_1v_1^T=[[3,0],[0,0]]`,
`-v_2v_2^T=[[0,0],[0,-1]]`, `v_3v_3^T+v_4v_4^T=[[1,0],[0,1]]`, sum
`[[4,0],[0,0]]`).
`E_μ|k|=(1/4)(3+1+1+1)=3/2` ✓; `c=2/3` ✓; `r=(2,-2/3,2/3,2/3)` ✓;
`E_μ|r|=(1/4)(2+2/3+2/3+2/3)=1` ✓.
Entropy: `(1/4)[2log2·2 + ... ]` — recomputed
`(1/4)[2·log2 + 3·(2/3)log(2/3)] = (1/4)[1.386294 - 0.810930] = 0.143841`,
matching the stated `0.1438` to the reported precision.
`log E[r²] = log((1/4)(4+3·4/9)) = log(4/3) = 0.287682`, matching `0.2877`.
`log 3 = 1.098612`, matching `1.0986`. Ordering `0.1438≤0.2877≤1.0986` holds.
Every number in the NUMERICAL CHECK section is independently reproduced
exactly.

## Sanity probes beyond the listed equations

Three limiting-case probes were run to check for hidden degeneracies not
visible in the abstract proof (division by zero, sign errors, vacuous
bounds):
* `μ` a point mass at `v_0`: `d=1`, `k=[1]`, `c=1`, `r≡1`, entropy `0` —
  degenerates correctly to "no reweighting needed."
* `μ` uniform on the standard basis `e_1,…,e_n`: `d=n`, kernel at `e_1` is
  `k(v)=n v_1²`, `c=1`, `r` is exactly the indicator/conditioning
  reweighting on `{e_1}`, entropy `=log n` exactly (the equality case of
  Lemma 4's sharpness note) — consistent with, and not contradicting, the
  Contract's "Known boundary" (that boundary concerns the *worst-case* `μ`
  for nonnegative `r`, not every `μ`).
* `μ` rotationally invariant (uniform on the whole sphere): by symmetry every
  point has the same `K(v,v)`, forcing `K(v,v)=d=n(n+1)/2` for every point —
  i.e., this is the case that *saturates* Lemma 3's bound rather than beating
  it, and the construction still produces a well-defined, generically signed
  `r` at cost exactly `log(n(n+1)/2)`. No degeneracy (`K(v,v)>0` throughout,
  no division by zero).
No hidden flaw was found in these probes; the RKHS/Christoffel-function
averaging argument behaves consistently across all three regimes tested.

## Minor items noted (not rising to a defect class)

* Remark C(i)'s existing (unchanged) sphere-case paragraph attributes
  `k(-v_0)=k(v_0)` to "Lemma 1(c)"; strictly, `k(-v_0)=k(v_0)` is evenness of
  the quadratic-form representative (not itself stated in Lemma 1(c)), while
  `k(v_0)=K(v_0,v_0)` *is* Lemma 1(c)'s content by definition. This is an
  attribution imprecision, not an incorrect claim (the equality itself is
  true and the entropy computation built on it is correct), and the
  artifact's own REVISION LOG already records it as a previously-adjudicated
  pedantic item (F9). Noted for completeness of a "however small" audit but
  not counted as a fresh defect.

## Result

No algebraic slip, dimension mismatch, sign error, or unjustified step was
found anywhere in Lemma 1(a)-(d), Lemma 2(i)-(iii), Lemma 3, Lemma 4, the
Theorem's proof, the Corollary's constant calculation, Remark A's algebra,
Corollary B's statement/proof, or the appended Corollary-B analogue in
Remark C(i) — including the specific computation
`E_{μ'}‖X-X_0‖_F² = 1 - 2⟨X_0,X_0⟩ + 1 = 0` singled out by the task, which is
correct. The NUMERICAL CHECK section was independently reproduced digit for
digit.

### VERDICT ###

STATUS: CLEAN

Every equation and inequality in the artifact — Lemma 1 through Lemma 4, the
Theorem, the Corollary's constant derivation (`n(n+1)/2≤n²`,
`max_{x>0}(log x)/x^δ=1/(eδ)`), Remark A's quadratic-in-t argument, Corollary
B's transfer of Lemmas 1-4 to the affine space `G`, and the newly appended
Corollary-B analogue in Remark C(i) (including the specifically flagged
`E_{μ'}‖X-X_0‖_F² = 1 - 2⟨X_0,X_0⟩ + 1 = 0` computation) — was independently
re-derived from the stated hypotheses and found correct; three additional
limiting-case probes (point mass, uniform-on-basis-vectors, rotationally
invariant `μ`) turned up no hidden degeneracy, division-by-zero, or sign
error; and the NUMERICAL CHECK section was reproduced exactly, including the
reproducing-kernel linear system, the resulting matrix identity
`E_μ[k vv^T]=v_1v_1^T`, and all four decimal entropy/log values. One
pre-existing, already-catalogued attribution imprecision (`k(-v_0)=k(v_0)`
cited to Lemma 1(c) rather than to evenness of quadratic forms) was noted but
does not affect the correctness of any conclusion and is not counted as a
fresh defect. No statement drift (Class A) was found between the theorem
proved and Question 8.1 / the Contract.

### FINDINGS ###

| Location | Severity/Class | Explanation |
|---|---|---|
| (none — no algebraic defect found) | — | Full line-by-line re-derivation of every displayed equation/inequality in Lemmas 1-4, Theorem, Corollary, Remark A, Corollary B, and the new Remark C(i) paragraph confirms correctness; NUMERICAL CHECK independently reproduced exactly. |
| Remark C(i), pre-existing sphere paragraph: "`k(−v_0)=k(v_0)=K(v_0,v_0)` by Lemma 1(c)" | Class D (cosmetic/attribution) — pre-existing, already adjudicated PEDANTIC (F9) per the artifact's own revision log | `k(-v_0)=k(v_0)` is evenness of the quadratic-form representative, not literally Lemma 1(c); `k(v_0)=K(v_0,v_0)` is Lemma 1(c). The underlying equality and the entropy computation built on it are both correct; only the citation is imprecise. Not a fresh defect. |
