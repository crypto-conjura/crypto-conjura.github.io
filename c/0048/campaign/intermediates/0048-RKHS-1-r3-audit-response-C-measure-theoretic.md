MODEL: opus

### VERDICT ###
STATUS: CLEAN
The artifact carries its `### END OF ARTIFACT [T-1] ###` line, proves a statement that
strictly implies the Contract with the Contract's own quantifier order, and every
measure-theoretic step I was asked to attack (well-definedness of point evaluation on
the quotient, the kernel-trace identity `∫K(v,v)dμ = d`, the averaging step producing a
support point with `K ≤ d`, the Jensen/entropy step, and the closing structural claim)
survives adversarial testing; the only items I found are notational/rhetorical
imprecisions of class (C) that a competent reader fills without effort and that I state
explicitly do not force DEFECTS.

### FINDINGS ###

| quoted location | class A-E | explanation |
|---|---|---|
| Lemma 3 statement: "`∫ K(v,v) dμ(v) = d`" | (C) routine, non-blocking | `K(v,v)` is defined by Lemma 1(c) **only** for `v ∈ supp μ`, so the displayed integral is literally an integral of a function that is undefined on `(supp μ)^c`. The proof repairs this in the next paragraph ("`g` is a polynomial, hence Borel, and by (P1) it represents `v ↦ K(v,v)` up to a null set, so the integral is well defined"), and the computation `∫ g dμ = Σ_j ∫ q_j² dμ = Σ_j ‖f_j‖² = d` is done on `g`, never on `K`. So the gap is only between the statement's notation and the proof's object. I verified that nothing downstream evaluates `K(v,v)` off the support: the only consumer is `A := {g ≤ d}`, and `A` is built from `g`. Non-blocking. |
| Remark C, derivation: "`k(−v_0) = k(v_0) = K(v_0,v_0)` **by Lemma 1(c)**" | (C) routine, non-blocking | Two small mis-attributions. (1) Lemma 1(c) gives `ev_{v_0}(k_{v_0}) = K(v_0,v_0)` and hence `k(v_0) = K(v_0,v_0)`; the *evenness* `k(−v_0) = k(v_0)` comes from the chosen quadratic-form representative `q_{Q_k}` being even, not from Lemma 1(c). (2) The symbol `k(−v_0)` is representative-independent only when `−v_0 ∈ supp μ` (that is exactly the scope of Lemma 1(b)). The conclusion is nevertheless correct as written: in the identity `1 = μ′({±v_0}) = k(v_0)μ({v_0}) + k(−v_0)μ({−v_0})`, if `μ({−v_0}) > 0` then `−v_0 ∈ supp μ` and Lemma 1(b) applies, while if `μ({−v_0}) = 0` the term vanishes for *any* representative. So `μ({±v_0}) = 1/K(v_0,v_0)` holds either way. Non-blocking; and Remark C is not load-bearing for the Theorem. |
| Remark C(i): "at most `log(n(n+1)/2)` — **equivalently**, `k ≥ 0` forces `μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))`" | (C) rhetorical, non-blocking | The two joined statements are not equivalent. "If `r ≥ 0` then `r` is a nonnegative reweighting of cost `≤ log(n(n+1)/2)`" is *implied by* (and strictly weaker than) the structural statement "`k ≥ 0 ⟹ μ({±v_0}) = 1/K(v_0,v_0)`". Both are true (I derived both from Lemmas 1–3 independently, see STEP LOG S13–S14) and the quantitative forms are exactly right, so the word "equivalently" is loose exposition rather than a false mathematical assertion. Non-blocking. |
| Note after Lemma 1: "(b) is **the only place** where the general Borel case differs from the finitely supported case" | (C) over-statement, non-blocking | Lemma 3 also differs: for general `μ` it needs (P1) `μ(supp μ) = 1`, Borel measurability of `g`, and the "positive measure ⟹ nonempty intersection with `supp μ`" step, all of which are vacuous for finitely supported `μ`. The claim is a meta-remark about the proof, not a step of it. Non-blocking. |
| Proof plan: "Its `L²` norm averages to `d` over `μ`" | (C) typo-level | It is the *squared* `L²` norm, `K(v,v) = ‖k_v‖²`, that averages to `d`. Lemma 3 states it correctly. Non-blocking. |
| Corollary B: "the space of quadratic forms replaced by the **affine space** `G`", "Run Lemmas 1–4 **verbatim**" | (C) routine, non-blocking | `G` is a linear subspace of `C(X)` consisting of affine functions, not an affine space; and the transport of Lemmas 1–4 is asserted rather than executed. I checked the transport myself and it does go through: `X` is compact (a limit of rank-`≤1` matrices of Frobenius norm `1` has rank exactly `1`, so `X` is closed and bounded) and second countable, so (P1) and Lemma 1(b) hold verbatim by continuity; `|α + ⟨A,X⟩| ≤ |α| + ‖A‖_F` on `X` gives Lemma 1(a); `1 ∈ G` and `X ↦ X_{ab} ∈ G` give Lemma 2(ii) and 2(i); `Σ_j q_j²` is a polynomial in the entries of `X`, giving Lemma 3; Lemma 4 never touches the geometry. `dim G ≤ n²+1` gives the stated `log(n²+1)`. Non-blocking. |
| Contract "for every `n ∈ N`" vs artifact "for every `n ≥ 1`" | (C) immaterial | If `0 ∈ N` then `S^{-1} = ∅` carries no probability measure and the Contract instance is vacuous. No drift of substance. |

No defect of class (A), (B), (D), or (E) was found. In particular:

* **(A) checked first and cleared.** See STEP LOG S1.
* **(D) cleared.** Every quotation in the DEPENDENCIES block is character-for-character
  the corresponding card item (Q1, Q2, Q4, Q5, Q6, Q7, Q8, Q9), and each is used only
  for the proposition the card supports. No source result is used as a mathematical
  input: the Theorem's proof is self-contained.
* **(E) cleared.** All external mathematics (finite-dimensional Riesz, Cauchy–Schwarz,
  Jensen for a concave function against a probability measure, `‖Q‖_op ≤ ‖Q‖_F`,
  `μ(supp μ) = 1` on a second-countable space, `max_{x>0}(log x)/x^δ = 1/(eδ)`) is
  restated and elementary; nothing needs a source I cannot reach.

### STEP LOG ###

**S0. Completeness gate.** The file ends with `### END OF ARTIFACT [T-1] ###`. No
sentence, display or proof terminates mid-stream; every lemma has a `∎`. The gate is
passed, so I verified rather than returning TRUNCATED.

**S1. Class (A) statement drift — checked first.**
What the artifact actually proves, in my own words: *for each `n ≥ 1` and each Borel
probability measure `μ` on `S^{n-1}` there is a point `v_0` of `supp μ`, a scalar
`c ∈ [(n(n+1)/2)^{-1/2}, 1]`, and a function `r` which is the restriction to the sphere
of one symmetric quadratic form, such that `E_μ|r| = 1`, `E_μ[|r| log|r|] ≤ log(n(n+1)/2)`,
and `E_μ[r(v)vv^T]` equals `c·v_0v_0^T` on the nose.* The Corollary then converts
`log(n(n+1)/2) ≤ 2 log n ≤ (2/(eδ))n^δ` into the Contract's form.
Diff against the Contract: (i) quantifier order — the Contract demands `C = C(ε,δ)`
chosen *before* `n` and `μ`; the artifact's `C = 2/(eδ)` depends on neither `n` nor `μ`,
so the order is right, not swapped; (ii) the conclusion is *strengthened*, not weakened
(error `0 ≤ ε‖L‖_F` for every `ε > 0`, entropy `O(log n)` rather than `O(n^δ)`, `L`
exactly rank one and PSD); (iii) hypotheses are *not* strengthened — `μ` is an arbitrary
Borel probability measure, `r` is only required Borel and `μ`-integrable and is delivered
bounded Borel, which is admissible under Contract convention 2 ("no further regularity is
assumed" — delivering *more* regularity than required is legal, demanding it would not
be); (iv) `L` is not required symmetric/PSD and the artifact's being PSD is a bonus;
(v) `r` is genuinely signed in general (the numerical check exhibits a signed `r`, and my
own computations below do too), so the Contract's `δ < 1/2` regime is not being read the
easy way. The relative normalisation is not exploited degenerately: Remark A shows that
`M = 0` is *not* admissible, so "cancel to zero" is unavailable and the artifact does not
take it. **No drift.**

**S2. Lemma 1(a) accepted.** `Q ↦ q_Q` is linear, so `F_μ` is the image of `Sym_n` and
`d ≤ n(n+1)/2`. `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F` for `‖v‖₂ = 1`. `μ` a probability measure
gives `L^∞(μ) ⊆ L²(μ)`. Note `d ≥ 1`, since `[q_I] = [1] ≠ 0` in `L²(μ)`; the proof never
needs this stated separately but it is what keeps `log d` well defined and the ONB in
Lemma 3 nonempty.

**S3. Lemma 1(b) accepted — read with maximum suspicion, as instructed.** `h := q_{Q−Q'}`
is continuous on `S^{n-1}` and `μ({h ≠ 0}) = 0`. If `h(v_0) ≠ 0` for some
`v_0 ∈ supp μ`, then `U := {|h| > |h(v_0)|/2}` is open by continuity, contains `v_0`,
hence `μ(U) > 0` by (P2); but `U ⊆ {h ≠ 0}` is null. Airtight. This is *precisely* the
clause the whole argument rests on, so I checked what it delivers against what is later
consumed:
 - *delivered:* any two **quadratic-form** representatives of one class of `F_μ` agree at
   every point of `supp μ`.
 - *consumed in Lemma 1(c):* well-definedness of `ev_v` on `F_μ` for `v ∈ supp μ`. The
   artifact is explicit that `ev_v` is "defined through quadratic-form representatives
   only" — which is exactly the strength (b) supplies. It does **not** claim, and does
   not need, that an arbitrary `L²`-representative of the class (which may be modified on
   a null set to any value at `v`) has the same value; that would be false and is not
   used anywhere. This is the trap in the problem and the artifact does not fall into it.
 - *consumed in Lemma 2:* `ev_{v_0}([1]) = 1` and `ev_{v_0}(g_{ab}) = (v_0)_a(v_0)_b`.
   These are exactly "the value of *some* quadratic representative", made unambiguous
   by (b). Correct usage.
 - *consumed in Lemma 3:* `ev_v(f_j) = q_j(v)` for the chosen representatives `q_j` and
   `v ∈ supp μ`. Again exactly (b).
 - *consumed in Remark C:* one evaluation at `−v_0`, which may lie outside `supp μ`; see
   the (C) finding. Conclusion unaffected.
 So: neither more nor less than (b) is used. Linearity of `ev_v` is inherited from
 `Q ↦ q_Q(v)` together with `[q_Q] + [q_{Q'}] = [q_{Q+Q'}]`. Accepted.

**S4. Preliminaries (P1), (P2) accepted.** (P1): with `{B_i}` a countable base of
`S^{n-1}`, `(supp μ)^c = ⋃{B_i : μ(B_i) = 0}` (if `v ∉ supp μ` there is open `U ∋ v` with
`μ(U) = 0` and a base element `v ∈ B_i ⊆ U`), a countable union of null sets; `supp μ` is
closed hence Borel. So `μ(supp μ) = 1`. (P2) is the definition. Both are used only where
legitimate.

**S5. Lemma 1(c) accepted.** `F_μ` is a finite-dimensional subspace of `L²(μ)`, hence
complete and a Hilbert space with the inherited inner product (positive-definite because
we are already in the quotient by `μ`-a.e. equality — the quotient is what makes this
work, and the artifact's `F_μ` is defined as a set of classes). Every linear functional on
a finite-dimensional inner-product space has a unique Riesz representer, so `k_v` exists
and is unique; `k_v = Σ_j ev_v(f_j) f_j` is the correct expansion in a real ONB;
`K(v,v) := ‖k_v‖² = ev_v(k_v)` follows by taking `f = k_v`. No invertibility of any
moment/Gram matrix on `Sym_n` is assumed anywhere — the construction lives on the
quotient, so `d < n(n+1)/2` (measure on a proper quadric, on a great subsphere, on
finitely many points) is harmless. Checked explicitly against my adversarial examples in
S15.

**S6. Lemma 1(d) accepted.** `q_I(v) = ‖v‖₂² = 1` identically on the sphere, and
`v^T E_{ab} v = v_a v_b` with `E_{ab} = (e_ae_b^T + e_be_a^T)/2`. This is where the
sphere constraint does its work: the constant function is a *homogeneous* quadratic form,
which is what makes the normalisation free.

**S7. Lemma 2(i) accepted — the crux.** For each `a,b`, `g_{ab} := [v ↦ v_av_b] = [q_{E_{ab}}]
∈ F_μ` by 1(d), so the reproducing property gives
`E_μ[k·v_av_b] = ⟨k, g_{ab}⟩ = ev_{v_0}(g_{ab}) = (v_0)_a(v_0)_b`. Entrywise this is
`E_μ[k vv^T] = v_0v_0^T`, exactly. All integrals converge absolutely (`k` bounded by
1(a), `|v_av_b| ≤ 1`), so the entrywise expectation matching the Contract's definition of
`E[r vv^T]` is legitimate; no Fubini and no limit interchange is required anywhere in the
artifact. Independent consistency check: `tr` of the identity reproduces 2(ii), and for
unit `w ⊥ v_0` it forces `E_μ[k⟨v,w⟩²] = 0` with a nonnegative integrand — which is the
precise reason `k` must be signed unless `μ` lives on `±v_0`; that dovetails exactly with
Remark C rather than contradicting it.

**S8. Lemma 2(ii),(iii) accepted.** `E_μ[k] = ⟨k,[1]⟩ = ev_{v_0}([1]) = q_I(v_0) = 1`;
then `E_μ|k| ≥ |E_μ k| = 1`, `K(v_0,v_0) = E_μ[k²] ≥ (E_μ|k|)² ≥ 1` (Cauchy–Schwarz /
Jensen), `E_μ|k| ≤ (E_μk²)^{1/2} = K^{1/2} < ∞` (Cauchy–Schwarz against `1`, finite by
1(a)), and `E_μ[k] = 1 ≠ 0` gives `k ≠ 0`. All four uses of Cauchy–Schwarz are with
bounded integrands on a probability space. Accepted.

**S9. Lemma 3, the identity, accepted.** With `f_1,…,f_d` an ONB and `q_j` quadratic
representatives, `k_v = Σ_j ev_v(f_j) f_j` gives `K(v,v) = Σ_j ev_v(f_j)² = Σ_j q_j(v)²
=: g(v)` for every `v ∈ supp μ` (this is (2), and it uses exactly Lemma 1(b) — nothing
more). Then `∫ g dμ = Σ_j ∫ q_j² dμ = Σ_j ‖f_j‖²_{L²(μ)} = d`: a **finite** sum, so
linearity of the integral suffices; each `∫ q_j² dμ = ‖f_j‖² = 1` by definition of the
class, hence independent of the representative chosen. Note the identity `∫K dμ = d` is
*not* sensitive to representative choice or to the behaviour of `g` off `supp μ`, because
`μ((supp μ)^c) = 0`; the parenthetical "off the support nothing below uses `g`" is
accurate, since the only later use is via `A ∩ supp μ`. The "`tr P` / mean reciprocal
Christoffel function" gloss is correct (`tr P = d` for `P` the projection onto `F_μ`) and
is not load-bearing. Accepted modulo the (C) notational point above.

**S10. Lemma 3, the averaging step, accepted — this is angle item (3).** `A := {g ≤ d}`
is Borel since `g` is a polynomial. If `μ(A) = 0` then `h := g − d > 0` `μ`-a.e. while
`∫h dμ = 0`; a nonnegative-a.e. function with vanishing integral vanishes a.e., and
`h = 0` a.e. together with `h > 0` a.e. is impossible under a measure of total mass `1`.
Hence `μ(A) > 0`. The step I was asked to attack — that positive measure delivers a point
of `A` **inside the support** — is correct and correctly justified: by (P1),
`μ(A ∩ supp μ) = μ(A) > 0`, so `A ∩ supp μ ≠ ∅`. (A "positive measure ⟹ nonempty" step
alone would only give a point of `A`, at which `g(v)` need not equal `K(v,v)`; the
artifact does not make that error — it cites (P1) precisely here.) For `v_0` in the
intersection, `K(v_0,v_0) = g(v_0) ≤ d ≤ n(n+1)/2` by (2). Accepted.

**S11. Lemma 4 accepted — angle item (4).** `φ(t) = t log t` satisfies `φ ≥ −1/e` on
`[0,∞)` and `φ(t) ≤ t²` (for `t ≥ 1` since `log t ≤ t`; for `t < 1` since `φ ≤ 0`), so
`|φ(|r|)| ≤ max(1/e, r²) ∈ L¹(μ)` and the entropy is a finite real number — the
integrability that Jensen needs is thus established rather than assumed. `dν := |r|dμ` is
a probability measure because `E_μ|r| = 1`; `ν({r = 0}) = ∫_{\{r=0\}}|r|dμ = 0`, so
`log|r|` is `ν`-a.e. finite and `E_ν[log|r|] = E_μ[|r|log|r|]` with the `0 log 0 = 0`
convention exactly matching the `ν`-null set — this is the one place where the convention
could have been abused, and it is handled correctly. `E_ν[|r|] = E_μ[r²] < ∞`, so Jensen
for the concave `log` against the probability measure `ν` gives
`E_μ[|r|log|r|] ≤ log E_μ[r²]`. Accepted. The sharpness note is also correct (strict
concavity forces `|r|` `ν`-a.s. constant, i.e. `|r| ∈ {0,c}` `μ`-a.e., and then
`c = 1/μ({|r| = c})` with the bound equal to `log(1/μ({|r| = c}))`); it is not
load-bearing.

**S12. Proof of the Theorem accepted.** `v_0` from Lemma 3 with `K(v_0,v_0) ≤ d`;
`1 ≤ E_μ|k| ≤ K^{1/2} < ∞` from 2(ii),(iii), so `c := 1/E_μ|k|` is well defined, strictly
positive, and lies in `[K^{-1/2},1] ⊆ [(n(n+1)/2)^{-1/2},1]`. Taking `q_{cQ_k}` as
representative makes `r` an honest bounded Borel function on all of `S^{n-1}` (a
representative with a quadratic form exists by the definition of `F_μ`), so `r` is
`μ`-integrable and every `μ`-integral of `r` is representative-independent;
`E_μ|r| = cE_μ|k| = 1`, so `r` is admissible for the Contract's Definition.
`E_μ[r vv^T] = c v_0v_0^T = L` by 2(i); `‖L‖_F = c‖v_0v_0^T‖_F = c‖v_0‖₂² = c > 0`, `L`
is rank one, nonzero, PSD, and the error `0 ≤ ε‖L‖_F` for every `ε > 0`. Entropy:
`E_μ[|r|log|r|] ≤ log E_μ[r²] = log(c²K(v_0,v_0)) = log(K/(E_μ|k|)²) ≤ log K ≤ log(n(n+1)/2)`,
using `E_μ|k| ≥ 1` and Lemma 3. Every inequality is in the right direction. Accepted.

**S13. Corollary accepted.** `n = 1`: `log 1 = 0 ≤ C n^δ`. `n ≥ 2`: `n(n+1)/2 ≤ n²` (true
for all `n ≥ 1`) gives `log(n(n+1)/2) ≤ 2 log n`, and `max_{x>0}(log x)/x^δ = 1/(eδ)` at
`x = e^{1/δ}` gives `log n ≤ n^δ/(eδ)`, hence `≤ (2/(eδ))n^δ`. `C = 2/(eδ)` is finite for
every `δ > 0` and independent of `n, μ, ε`. I spot-checked `n = 2, δ = 0.01`
(`1.0986 ≤ 74.1`) and `n = 2, δ = 10` (`1.0986 ≤ 75.3`). Accepted; the quantifier order
demanded by Contract convention 1 is respected.

**S14. Remark A accepted (not load-bearing).** With `L = tuw^T`, `‖u‖=‖w‖=1`, `t > 0`:
`‖M−L‖_F² = ‖M‖_F² − 2t·u^TMw + t²`, and the requirement is
`(1−ε²)t² − 2(u^TMw)t + ‖M‖_F² ≤ 0`. Since `ε ∈ (0,1)` the leading coefficient is
positive and increasing `u^TMw` only helps, so the optimum is `u^TMw = s_1(M) = |λ_1|`.
Real root iff `s_1² ≥ (1−ε²)Σλ_i²`, i.e. iff `Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1²`; for
`M ≠ 0` both roots are positive (product `‖M‖_F²/(1−ε²) > 0`, sum `2s_1/(1−ε²) > 0`), so
an admissible `t > 0` exists exactly then. `M = 0` is excluded because `‖L‖_F > ε‖L‖_F`.
Correct, and it does establish that the relative normalisation is not degenerate.

**S15. Remark C, angle item (6): I derived the structural claim myself from the lemmas as
stated.** Hypothesis `k ≥ 0` `μ`-a.e. Then Lemma 2(ii) (`E_μk = 1`) makes `dμ′ := k dμ` a
probability measure, and Lemma 2(i) gives `E_{μ′}[vv^T] = v_0v_0^T`. For unit `w ⊥ v_0`,
`E_{μ′}⟨v,w⟩² = w^Tv_0v_0^Tw = 0` with a nonnegative integrand, so `⟨v,w⟩ = 0` `μ′`-a.s.;
intersecting the `n−1` null sets from an ONB of `v_0^⊥` (a **finite** union, no
unbounded-index issue) and using `‖v‖₂ = 1` gives `μ′({±v_0}) = 1`. Evaluating
`1 = ∫_{\{±v_0\}} k dμ = K(v_0,v_0)(μ({v_0}) + μ({−v_0}))` yields `μ({±v_0}) =
1/K(v_0,v_0)`, and `K(v_0,v_0) ≤ n(n+1)/2` (Lemma 3) yields `≥ 2/(n(n+1))`. **The claim
does follow from the lemmas as stated, and its quantitative form is exactly right**
(equality `1/K`, not merely `≥`; and the bound `2/(n(n+1))`, not `2/n²`), subject only to
the representative caveat at `−v_0` recorded as (C) above, which does not change the
value. The follow-on claim is also exactly right: `r′ := 1_{\{±v_0\}}/μ({±v_0})` has
`E_μ|r′| = 1`, `E_μ[r′ vv^T] = v_0v_0^T` exactly (both `±v_0` contribute `v_0v_0^T`), and
`E_μ[r′ log r′] = log(1/μ({±v_0})) = log K(v_0,v_0) ≤ log(n(n+1)/2)` — the same bound the
Theorem gives. Also correct is the observation that when `k ≥ 0` one has `E_μ|k| = E_μ[k]
= 1`, hence `c = 1`, so `r = k` itself is the nonnegative reweighting. Remark C(ii) and
C(iii) are honest scope disclaimers, and C(ii) matters: the card's dictionary (Q4) is
stated for *flat* distributions, the Theorem supplies no flatness, so no log-rank
consequence is claimed and none follows. Remark C(i)'s reading of Q1's last sentence as
existential over `μ` is the correct negation of the quoted question, so no conflict with
the source's negative results is created.

**S16. Corollary B accepted (transport checked by me, see (C) finding).** Accepted.

**S17. Numerical check reproduced independently.** `F_μ = {x ∈ R⁴ : x_1+x_2 = x_3+x_4}`
is right (the image of `Sym_2` under evaluation at the four points sits inside this
3-dimensional hyperplane and has dimension 3, so equals it), `d = 3`. `k = (3,−1,1,1)`
lies in `F_μ` and satisfies `(1/4)(3x_1 − x_2 + x_3 + x_4) = (1/4)(4x_1) = x_1` on `F_μ`,
so it is the representer at `v_1`. `E_μk = 1`, `‖k‖² = (1/4)(9+1+1+1) = 3 = d`, and
`(1/4)(3v_1v_1^T − v_2v_2^T + v_3v_3^T + v_4v_4^T) = (1/4)[[4,0],[0,0]] = v_1v_1^T`
exactly. `E_μ|k| = 3/2`, `c = 2/3`, `r = (2,−2/3,2/3,2/3)`, `E_μ|r| = 1`, entropy
`= (1/4)(2log2 + 2·(2/3)log(2/3)) = 0.1438`, `E_μ[r²] = 4/3`, `log(4/3) = 0.2877`,
`log 3 = 1.0986`. Every number in the artifact checks out, and `r` is indeed signed.

**S18. My own adversarial tests (angle items 1,2,5).** I tried to break the two exact
identities with the measures the assignment suggests; all confirm the artifact.
 - *Uniform on `S^{n-1}` (`d = n(n+1)/2` full).* The representer at `v_0` must be
   `k(v) = −n/2 + (n(n+2)/2)⟨v,v_0⟩²`; independently, `E[⟨v,v_0⟩² vv^T] =
   (n(n+2))^{-1}(I + 2v_0v_0^T)` and `E[vv^T] = I/n` give `E[k vv^T] = v_0v_0^T`
   **exactly**, and `k(v_0) = n(n+1)/2 = d = K(v_0,v_0)`, `E[k] = 1`. Here `k` is
   negative wherever `⟨v,v_0⟩² < 1/(n+2)`, i.e. almost everywhere for large `n`, so the
   construction is genuinely using cancellation — consistent with, not contradicting,
   the `r ≥ 0` lower bound in the Contract's "Known boundary".
 - *Uniform on `{±1/√n}^n` (the canonical hard instance for nonnegative reweightings).*
   Writing `v = x/√n`, `F_μ = span{1} ⊕ span{x_ax_b}_{a<b}`, `d = 1 + n(n−1)/2 <
   n(n+1)/2` (so the moment map on `Sym_n` is *not* injective — nothing breaks, because
   the argument works on the quotient). The representer at `x_0 = (1,…,1)` is
   `k = 1 + Σ_{a<b}x_ax_b = ((Σx_a)² − n + 2)/2`, and I verified directly
   `E[((Σx_a)² − (n−2))x_ax_b] = 2` for all `a,b` (including `a = b`), giving
   `E[k vv^T] = v_0v_0^T` exactly, with `K = d`. Entropy of the normalised `r` is `O(1)`.
 - *A great subsphere (equator of `S²`).* `d = 3 < 6`; `k = 1 + 2cos2θ`; I computed all
   six entries of `E[k vv^T]` and got exactly `e_1e_1^T`, including the identically-zero
   third row and column.
 - *A proper quadric not through a symmetric position: the circle `{v_3 = 1/√2,
   v_1²+v_2² = 1/2} ⊂ S²`.* Here `F_μ = span{1, cos2θ, sin2θ, cosθ, sinθ}`, `d = 5 < 6`,
   `k = 1 + 2cos2θ + 2cosθ`, `K = 5 = d`, and I computed all six entries: `E[k v_1²] =
   1/2`, `E[k v_2²] = 0`, `E[k v_3²] = 1/2`, `E[k v_1v_2] = 0`, `E[k v_1v_3] = 1/2`,
   `E[k v_2v_3] = 0`, i.e. exactly `v_0v_0^T` for `v_0 = (1/√2,0,1/√2)`. `k` is signed
   (`k(π/2) = −1`).
 - *Finitely supported measures.* Uniform on `{e_1,…,e_n}`: `d = n`, `k = n·1_{\{e_1\}}`,
   `K = n = d`, `E[k vv^T] = e_1e_1^T`, entropy `= log n = log K` (Lemma 4 tight, `r ≥ 0`),
   and Remark C's prediction `μ({±e_1}) = 1/K = 1/n` holds on the nose. Two antipodal
   points: `d = 1`, `k = 1`, `K = 1`, entropy `0`, `μ({±v_0}) = 1 = 1/K`. Single atom:
   `d = 1`, `r = 1`. `n = 1` (`S⁰`): `F_μ` = constants, `d = 1`, `r = 1`, `L = 1`.
 - *Structural sanity.* The linear-algebra count also confirms the mechanism is not an
   accident: `Q ↦ E[q_Q vv^T]` maps `Sym_n` to `Sym_n`, and "image proportional to
   `v_0v_0^T`" is `dim Sym_n − 1` constraints, so a nonzero solution always exists; the
   content the kernel adds is (a) that the proportionality constant is forced nonzero and
   normalised to `1` (by `[1] ∈ F_μ`, i.e. by the sphere constraint), and (b) the
   second-moment bound `E[k²] = K(v_0,v_0) ≤ d` from Lemma 3, which is what buys the
   `log d` entropy. Both are proved, not assumed.
 In none of these tests did any step silently require finite support, invertibility of a
 moment operator, `d = n(n+1)/2`, or an atom at `v_0` (the uniform-sphere case has
 `μ({v_0}) = 0` and works).

**S19. Common-failure sweep.** No quantifier inversion (S1, S13). No union or measure
bound over an unbounded index — the only unions are over a countable base (P1, a genuine
countable union of null sets, correctly handled) and over `n−1` basis vectors (S15). No
worst-case/expected conflation: Lemma 3 is an honest averaging argument that is converted
into a *pointwise* statement about a specific `v_0`, with the support-intersection step
supplied. No asymptotics standing in for a constant: `C = 2/(eδ)` is explicit. No
reduction/hybrid factor to lose. No independence assumed anywhere. No limit, sum-integral
or expectation interchange beyond finite sums of bounded integrands. No induction, so no
missing base case. No measure-zero exception treated as empty — on the contrary, the
`μ`-null vs. `supp μ` distinction is exactly what Lemma 1(b), (P1) and the Lemma 3
averaging step are built to respect. The constructed `r` is checked against every clause
of the Contract's Definition (Borel, `μ`-integrable, `E|r| = 1`, entropy bound) and `L`
against every clause of the conclusion (rank one, nonzero, relative error).

### SOURCE REQUEST ###
none
