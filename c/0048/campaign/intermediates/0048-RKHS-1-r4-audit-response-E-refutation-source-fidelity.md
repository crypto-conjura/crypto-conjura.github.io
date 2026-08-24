MODEL: opus

### VERDICT ###

STATUS: DEFECTS

Every refutation attempt against the main Theorem, its Corollary, Remark A and
Corollary B failed — I reproduced the construction symbolically and numerically
on degenerate, mixed and fully continuous measures on both domains and it
delivers exactly what is claimed at the claimed cost — but Remark C contains one
claim about the *domain* over which the cited Theorem 2.3 and its tightness
remark are stated that the source card contradicts (class D), and the Corollary B
transfer sentence understates which properties the transfer needs (class C,
routine).

### FINDINGS ###

| quoted location | class | explanation |
|---|---|---|
| REMARK C(i): "The same holds for Corollary B, whose domain — not the sphere — is the one Theorem 2.3 and the tightness claim of Q5 are stated over" | **D** | Card **Q2** states Theorem 2.3 over "any distribution over rank one `n × n` matrices" — no norm normalisation. Corollary B's domain is the strict subset `X = {rank X = 1, ‖X‖_F = 1}`. The unit-norm restriction the artifact leans on is card **Q8**, which is from §2.3 (p. 6), *after* Theorem 2.3 (p. 5), and is a restriction the source imposes on `U, V` for its own later development; nothing on the card puts it into the statement of Theorem 2.3 or into the tightness claim of Q5 ("as stated, Theorem 2.3 is tight" — i.e. as stated over all rank one matrices). So the asserted identity of domains is not card-supported and is false per Q2. The artifact contradicts itself eleven lines later ("What is *not* addressed is the unnormalised domain of Theorem 2.3 (Q2) … Corollary B treats only the unit-Frobenius slice named at Q8"), which is the correct statement. Non-load-bearing: the *conclusion* of Remark C(i) ("no conflict") survives, because a signed reweighting cannot conflict with a negative result about nonnegative ones on any domain; only the scope claim is wrong. But it is a misdescription of a cited result's hypotheses, hence D, and per REFEREE-PROMPT it blocks CLEAN. |
| COROLLARY B, proof: "Run Lemmas 1–4 verbatim with `S^{n-1}` replaced by `X` (compact) … Only two properties of the function space were used: it contains the constant `1` … and it contains each coordinate function" | **C** (routine gap; does **not** by itself force DEFECTS) | The transfer also uses (i) finite-dimensionality of `G` (Lemma 1(c) needs `ev_X` bounded and needs `F_μ` closed in `L²(μ)`); (ii) second countability of `X` for preliminary (P1) `μ(supp μ) = 1`, invoked in Lemma 3; (iii) Borel measurability of `g = Σ_j q_j²` in Lemma 3, which here holds because affine functions are polynomials. The sentence names only the constant and the coordinates, then supplies continuity and boundedness but not (i)–(iii). All three are immediate — `dim G ≤ n²+1` is stated one line earlier, `X ⊂ R^{n×n}` is metrisable and separable, and squares of affine functions are polynomials — so I record this as a gap a competent reader fills without effort, and I do not count it toward the verdict. |

No class A (statement drift), no class B, no class E. The main Theorem, the
Corollary, Remark A and Corollary B are, to the best of my ability to break them,
correct as stated.

### STEP LOG ###

**Step 0 — completeness gate.** The artifact carries `### END OF ARTIFACT [W-1] ###`
as its last line. No sentence, equation or proof stops mid-way; every environment
(GOAL, THEOREM, Lemmas 1–4, Proof of the Theorem, COROLLARY, REMARK A,
COROLLARY B, REMARK C, DEPENDENCIES, NUMERICAL CHECK) closes. **Not truncated.**

**Step 1 — class A: what is actually proved, in my words.**

> For every `n ≥ 1` and every Borel probability measure `μ` on `S^{n-1}`: let
> `F_μ ⊆ L²(μ)` be the (at most `n(n+1)/2`-dimensional) space of `μ`-classes of
> restrictions of real quadratic forms, `d = dim F_μ`. Then there is a point
> `v_0 ∈ supp μ` whose reproducing kernel `k = k_{v_0} ∈ F_μ` has
> `K(v_0,v_0) = ‖k‖²_{L²(μ)} ≤ d`, and with `c := 1/E_μ|k| ∈ [(n(n+1)/2)^{-1/2}, 1]`
> the function `r := c·k` (a bounded Borel function, being a quadratic form
> restricted to the sphere) satisfies `E_μ|r| = 1`,
> `E_μ[|r|log|r|] ≤ log K(v_0,v_0) ≤ log(n(n+1)/2)`, and
> `E_μ[r(v)vv^T] = c·v_0v_0^T` **with equality**, a nonzero rank one PSD matrix of
> Frobenius norm `c`.
> Consequently, for any `ε > 0` and `δ > 0`, with `C := 2/(eδ)` the Contract's
> displayed statement holds for every `n` and every `μ`, with Frobenius error
> exactly `0`.

Diff against the Contract, item by item.
* Hypotheses: identical. "Every `n ∈ N`", "every Borel probability measure `μ` on
  `S^{n-1}`". No regularity added to `μ`; no atoms, no absolute continuity, no
  finite support assumed. Lemma 1's note explicitly flags that only Lemma 1(b)
  distinguishes the general Borel case from the finitely supported one, and it is
  proved, not waved.
* Requirements on `r`: Borel ✓ (a polynomial restricted to the sphere),
  `μ`-integrable ✓ (bounded, `μ` a probability measure), `E_μ|r| = 1` ✓ (exact,
  by construction of `c`), entropy ≤ `C n^δ` ✓. Reading convention 2 (no extra
  regularity may be added) is respected — the artifact's `r` is *more* regular
  than required, which is permitted; it does not restrict `μ` in exchange.
* Requirements on `L`: rank one ✓, nonzero ✓ (`c ≥ K^{-1/2} > 0`), symmetry/PSD
  not required but delivered — a strengthening, not a weakening. Reading
  convention 3 respected.
* Quantifier order: `C` is fixed after `ε, δ` and before `n` and `μ`
  (`C = 2/(eδ)` depends on neither `n` nor `μ`), exactly Reading convention 1.
  No "for all sufficiently large `n`" is smuggled in: `n = 1` is handled
  explicitly in the Corollary.
* Direction of strengthening: three ways stronger than asked — error `0` instead
  of `ε‖L‖_F`, cost `O(log n)` instead of `O(n^δ)`, `C` independent of `ε`. The
  artifact advertises all three in its GOAL block rather than hiding them.
* Vacuity check: the "easy reading" of a relative-error criterion would be to let
  `E_μ[r vv^T] = 0` and call it rank one; Remark A shows that reading is closed
  off (`M = 0` admits no admissible `L`), and the construction's output is
  `c v_0 v_0^T ≠ 0` anyway. So the ambiguous term is not read the vacuous way.

**No class A defect.**

**Step 2 — Lemma 1, accepted.** (P1): the complement of `supp μ` is the union of
all null open sets; second countability lets a basis element be chosen inside
each, so the union is a countable union of null sets — correct. (P2) is the
definition. (a): `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F` on the sphere, and `L^∞ ⊆ L²` under a
probability measure — correct; `d ≤ n(n+1)/2` as the image of `Sym_n`. (b): the
continuity argument is correct and is the right argument (the open set
`{|h| > |h(v_0)|/2}` meets `supp μ`, so has positive measure, yet sits inside a
null set). Well-definedness and linearity of `ev_v` on `F_μ` for `v ∈ supp μ`
follow, and the artifact says exactly why. (c): finite dimension ⇒ closed in
`L²(μ)` ⇒ Hilbert; every linear functional on a finite-dimensional space is
bounded; Riesz gives a unique `k_v ∈ F_μ`; `K(v,v) = ev_v(k_v)` by taking
`f = k_v`. (d): `q_I ≡ 1` on the sphere and `q_{E_{ab}}(v) = v_a v_b` — I checked
`v^T((e_ae_b^T + e_be_a^T)/2)v = v_a v_b`. Accepted.

**Step 3 — Lemma 2, accepted.** (i) is the reproducing property applied to the
`n(n+1)/2` coordinate-product classes; every entry checks out, giving
`E_μ[k vv^T] = v_0v_0^T` **exactly**. (ii) is the same applied to `[1] = [q_I]`;
the sphere constraint is what makes `1` a quadratic form, and the artifact's
structural note (that (ii) is the trace of (i)) is correct and is a good
consistency check. `E_μ|k| ≥ |E_μ k| = 1`, `K = E_μ[k²] ≥ (E_μ|k|)² ≥ 1`,
`k ≠ 0`. (iii) Cauchy–Schwarz against `1`. Absolute convergence is justified by
boundedness. Accepted.

**Step 4 — Lemma 3, accepted.** `k_v = Σ_j ev_v(f_j) f_j` and
`K(v,v) = Σ_j q_j(v)²`; `∫K dμ = Σ_j ‖f_j‖² = d` (finite sum, no interchange
issue). The averaging step is done correctly and is not a worst-case/average
conflation: from `∫ g dμ = d` one gets `μ({g ≤ d}) > 0` (else `g − d > 0` a.e.
with mean `0`, so `(g−d)^+ = 0` a.e., contradiction), then `μ(supp μ) = 1` gives
`{g ≤ d} ∩ supp μ ≠ ∅`. The off-support values of `g` are correctly quarantined.
Accepted.

**Step 5 — Lemma 4, accepted.** `φ(t) = t log t ≤ t²` for `t ≥ 0` (`log t ≤ t` for
`t ≥ 1`; `φ ≤ 0` for `t < 1`) and `φ ≥ −1/e`, so `φ(|r|) ∈ L¹` when `r ∈ L²` —
the finiteness claim is earned, not assumed. `dν := |r|dμ` is a probability
measure; `ν({r = 0}) = 0`, so the `0 log 0` convention lines up with a `ν`-null
set and `E_ν[log|r|] = E_μ[|r|log|r|]`; Jensen for concave `log` gives
`≤ log E_ν[|r|] = log E_μ[r²]`. Note `E_μ[r²] ≥ (E_μ|r|)² = 1`, so the bound is
never a negative number masquerading as a bound. Accepted; the sharpness remark
(equality iff `|r|` is two-valued) is correct and correctly identifies that this
is where the bound is lossy.

**Step 6 — Proof of the Theorem, accepted.** All four Contract requirements on `r`
and all three on `L` are individually verified in the text; nothing is
constructed and left unchecked. `‖L‖_F = c‖v_0v_0^T‖_F = c` uses
`‖v_0v_0^T‖_F = ‖v_0‖² = 1` ✓. The entropy chain
`log(c²K) = log(K/(E_μ|k|)²) ≤ log K ≤ log d` uses `E_μ|k| ≥ 1` (Lemma 2(ii)) and
`K ≤ d` (Lemma 3) ✓.

**Step 7 — Corollary, accepted.** `n = 1`: `log 1 = 0` ✓. `n ≥ 2`:
`n(n+1)/2 ≤ n²` ⟺ `n+1 ≤ 2n` ✓, so `log(n(n+1)/2) ≤ 2 log n`;
`max_{x>0}(log x)/x^δ = 1/(eδ)` at `x = e^{1/δ}` (I verified: `log x = 1/δ`,
`x^δ = e`) ✓; hence `2 log n ≤ (2/(eδ))n^δ` for all `n > 0` ✓. `C = 2/(eδ)` is
finite for each `δ > 0` and independent of `ε, n, μ` ✓.

**Step 8 — Remark A, accepted (and independently re-derived).**
`‖M − t uw^T‖_F² = ‖M‖_F² − 2t·u^TMw + t²` (I recomputed
`⟨M, uw^T⟩ = u^TMw`); the criterion is
`(1−ε²)t² − 2(u^TMw)t + ‖M‖_F² ≤ 0`; monotonicity in `u^TMw` makes `s_1(M)`
optimal; discriminant `≥ 0` ⟺ `s_1² ≥ (1−ε²)‖M‖_F²` ⟺
`Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1²`; both roots positive when `M ≠ 0`. Writing a
general rank one `L = ab^T` as `t uw^T`, `t = ‖a‖‖b‖ = ‖L‖_F`, is WLOG.
Numerical spot-checks: `M = diag(1,0)` gives the admissible interval
`t ∈ [1/(1+ε), 1/(1−ε)]` ✓; `M = I_2` gives the threshold `ε ≥ 1/√2`, which I
confirmed directly from `(1−ε²)t² − 2t + 2 ≤ 0` ✓.

**Step 9 — Corollary B, accepted modulo the class C above.** `X` is the continuous
image of `S^{n-1} × S^{n-1}` under `(a,b) ↦ ab^T`, hence compact, and the
"equivalently" clause is correct (rescale `a ↦ a/‖a‖`, `b ↦ b‖a‖`). `G` contains
`1` and every `X ↦ X_{ab} = ⟨e_ae_b^T, X⟩` ✓; elements of `G` are continuous and
bounded on `X` (`|α + ⟨A,X⟩| ≤ |α| + ‖A‖_F`) ✓; `dim G ≤ n²+1` ✓. Lemma 2(i)'s
analogue gives `E_μ[k(X)X] = X_0` exactly, `c ∈ (0,1]`, cost `≤ log(n²+1)`.
(Calling `G` an "affine space" is a misnomer — it is a linear space of affine
functions — but nothing depends on it.)

**Step 10 — Remark C, checked hypothesis by hypothesis against the card.**
* "deficient ⇒ nonnegative": card **Q9** defines `k`-deficient only for a
  *probability distribution* `µ′`, and the card's own closing note says exactly
  this. The gloss is inside the card's words. **Supported.**
* "'the answer … is No if one does not allow negative reweighting functions' (Q1)
  is an existential statement over `μ`": the negation of Q1's universally
  quantified question is `∃ε,δ ∃μ`. **Supported** (mildly abbreviated —
  existential over `ε, δ` too — which if anything weakens the artifact's own
  position, not strengthens it).
* The "not a hard instance" argument, spherical case: I verified every link.
  `k ≥ 0` a.e. ⇒ `dμ′ = k dμ` is a probability measure; `E_{μ′}[vv^T] = v_0v_0^T`
  kills `⟨v,w⟩` for each of the `n−1` basis vectors of `v_0^⊥` (a finite union of
  null sets, no unbounded index); `‖v‖ = 1` then forces `μ′({±v_0}) = 1`;
  `k(v_0) = K(v_0,v_0)`; `k(−v_0) = k(v_0)` by evenness of the representative,
  with the `μ({−v_0}) = 0` and `μ({−v_0}) > 0` cases *both* handled (the second
  via "an atom lies in the support", which is correct); hence
  `μ({±v_0}) = 1/K ≥ 2/(n(n+1))`, and `r′ = 1_{{±v_0}}/μ({±v_0})` is a genuine
  nonnegative reweighting of cost `log K` reaching `v_0v_0^T` exactly. Airtight.
* The same argument on `X`: `1 − ⟨X_0,X⟩ ≥ 0` with `μ′`-mean `0`; equality in
  Cauchy–Schwarz between unit-Frobenius matrices forces `X = X_0`;
  `μ({X_0}) = 1/K(X_0,X_0) ≥ 1/(n²+1)`. Airtight; and the artifact correctly
  notes why the antipodal bookkeeping of the spherical case does not transfer.
* Domain claim: **the class D above.**
* "(ii) No log-rank consequence is claimed." Card **Q4** states the dictionary
  for *flat* `µ′` only, and the Theorem supplies no flatness; so the quoted route
  is indeed unavailable. This is a claim about the quoted route, not about all
  routes, and the artifact says "no other route is addressed". Checked for
  **over-modesty** in the other direction: card Q1 says a positive solution
  "*may* improve the best known bound for the log rank conjecture to `Õ(n^δ)`" —
  hedged — so declining to claim the consequence does not undercut anything the
  card asserts. **Not overreach in either direction.**
* "(iii) pseudo-distributions out of scope": card Q1 attaches the
  pseudo-distribution clause to the *running-time* consequence ("and if
  appropriately extended to pseudo-distributions, improve our algorithm's running
  time"), exactly as the artifact says. The artifact also correctly identifies
  that every use of `supp μ` presumes an honest measure. **Supported.**
* "moot here: our constant is independent of `ε`" (against card **Q7**): Q7 warns
  that log-rank applications may need better control of the `ε`-dependence; the
  artifact's bound has no `ε` in it and its error is `0` for every `ε`, so the
  warning is indeed inapplicable to this bound. **Supported.**

**Quotation fidelity, character by character.** Every one of the eight quotations
in DEPENDENCIES matches the card, including the source's own typo in footnote 7
("to find a in a rank `n` Boolean matrix"), which is preserved — a good sign of
genuine copying rather than reconstruction. Three deviations, all typographic,
all of which I judge immaterial and none of which I count as a defect:
(1) Q1 is quoted as `…≤ ε‖L‖_F`?" where the card prints a space before the
question mark; (2) the Theorem 2.3 quotation acquires a terminal period the card
does not have; (3) inside Corollary B the §2.3 quotation is opened with lowercase
"we" where the card has "We" (the DEPENDENCIES copy of the same sentence is
capitalised correctly). No substantive word, symbol, quantifier or bound differs
anywhere. The one gloss the artifact adds to a definition — "*deficient*, hence
nonnegative" — is within the card's own words (Q9 plus the card's note). The
inference that the source's intended application lives on the unit-Frobenius
slice is card-supported by Q4 (distributions over `{u_i v_i^T}`) together with Q8
(those `u_i, v_i` are unit norm in the intended application).

**Step 11 — REFUTATION ATTEMPTS (all failed; reported as failures).**
I rebuilt the construction from scratch in each case and checked
`E_μ[k] = 1`, `E_μ[k vv^T] = v_0v_0^T` (or `E_μ[kX] = X_0`) entrywise,
`K(v_0,v_0) ≤ d`, and the entropy bound.

*Sphere, degenerate measures.* `μ = δ_{v_0}` (`d = 1`, `k = 1`, cost `0`);
`μ = ½δ_{v_0} + ½δ_{−v_0}` (`d = 1`, `k = 1`); `n = 1`, `S^0 = {±1}` (`d = 1`),
which is the case a missing base case would break — it works and the Corollary
handles it separately; `μ = ½δ_{e_1} + ½δ_{e_2}` in `R²` (`d = 2`, `k = (2,0)`,
`K = 2`, `c = 1`, entropy `= log 2 = log K`, i.e. Lemma 4 *tight*, and the
Remark C equality `μ({±v_0}) = 1/K = ½` holds on the nose);
`μ` uniform on `{e_1,…,e_n}` in `R^n` (`d = n`, `k = n·1_{e_1}`, `K = n`, cost
`log n = log K`, tight again); `μ` uniform on `{e_1, −e_1, u}` in `R²` (`d = 2`,
`k = (1.5,1.5,0)`, `K = 1.5`, `μ({±e_1}) = 2/3 = 1/K` — this is the case designed
to break the antipodal bookkeeping of Remark C, and it does not).

*Sphere, atomic non-degenerate.* The artifact's own NUMERICAL CHECK, recomputed
independently: `F_μ = {x_1 + x_2 = x_3 + x_4}` with `d = 3`, `k = (3,−1,1,1)`
(verified by `⟨k,f⟩ = ¼(3f_1 − f_2 + f_3 + f_4) = f_1` on `F_μ`), `K = 3`,
`E_μ[k vv^T] = v_1v_1^T` (`v_3v_3^T + v_4v_4^T = I` is the load-bearing
cancellation), `E_μ|k| = 3/2`, `c = 2/3`, entropy `0.1438 ≤ 0.2877 = log E[r²]`.
Every printed number is right. Also `μ` uniform on `5` equally spaced points of
`S^1`: `k = 1 + 2cos 2θ`, `K = 3`, exact rank one, entropy bound `0.295`.

*Sphere, continuous measures.* Uniform on `S^1`: `k = 1 + 2cos 2θ`, `K = 3 = d`,
`E|k| = (1/2π)∫|1+2cos u|du = 1.436`, cost bound `log(3/1.436²) = 0.375`, and I
verified `E[k vv^T] = v_0v_0^T` entry by entry. Uniform on `S^{n-1}` for general
`n`: I solved for the kernel in closed form,
`k(v) = (n(n+2)/2)(v·v_0)² − n/2`, and verified `E[k] = 1`,
`K(v_0,v_0) = n(n+1)/2 = d`, and — using
`E[v_iv_jv_kv_l] = (δ_{ij}δ_{kl}+δ_{ik}δ_{jl}+δ_{il}δ_{jk})/(n(n+2))` —
`E[k vv^T] = (I + 2v_0v_0^T)/2 − I/2 = v_0v_0^T` exactly. Asymptotically
`E|k| ≈ (n/2)E|Z²−1| ≈ 0.484n`, so the cost bound tends to `log 2.14 ≈ 0.76`,
i.e. `O(1)`, not merely `O(log n)`. `n = 3` numerically (`v·v_0` uniform on
`[−1,1]`): `E|k| = 1.894`, cost bound `0.514 ≤ log 6`. A mixed
atomic-plus-continuous measure `μ = ½δ_{e_1} + ½·Unif(S^1)`: solving the `3×3`
Gram matrix gives `k = ½ + cos 2θ`, `K = 1.5 ≤ d = 3`, and I verified
`E_μ[k vv^T] = e_1e_1^T` entrywise; here `μ({±v_0}) = ½ ≠ 1/K = 2/3`, which is
*consistent* with Remark C precisely because `k` is signed on this measure — a
live test of that Remark's hypothesis, passed. Finally the natural
"hard-for-nonnegative" instance, `μ` uniform on `{±1}^n/√n`:
`d = 1 + n(n−1)/2`, `k = 1 + (S²−n)/2` with `S = Σx_i`; I verified `E[k] = 1` and
`E[k vv^T] = v_0v_0^T` on and off the diagonal; `E|k| ≈ 0.484n`, cost `O(1)`, and
`k` is genuinely signed. No counterexample.

*Matrix domain, degenerate.* `n = 1` (`X = {±1}`, `d = 2 = n²+1`, `k = 1 + X`,
`K = 2`, `μ({X_0}) = ½ = 1/K ≥ 1/(n²+1)` ✓); `μ = δ_{X_0}` (`d = 1`, cost `0`);
`μ = ½δ_{e_1e_1^T} + ½δ_{e_2e_2^T}` (`d = 2`, `k = (2,0)`, `K = 2`, nonnegative
`k`, `μ({X_0}) = ½ = 1/K ≥ 1/5` ✓).

*Matrix domain, continuous.* `μ` = law of `ab^T` with `a, b` independent uniform
on `S^1`. From `E[X_{ij}X_{kl}] = δ_{ik}δ_{jl}/4` and `E[X_{ij}] = 0` the space
`G` is exactly `n²+1 = 5` dimensional with orthonormal basis `1, 2X_{ij}`, and
`k(X) = 1 + 4X_{11} = 1 + 4a_1b_1`, `K = 5`; I verified `E[k] = 1` and
`E[kX] = e_1e_1^T = X_0` entrywise. This was my sharpest attempt at Remark C: `μ`
is atomless, so `μ({X_0}) = 0`, contradicting the Remark's `μ({X_0}) = 1/K` — but
the Remark's hypothesis fails, since `a_1b_1 < −1/4` with positive probability
and so `k` is genuinely signed. `E|k| ≈ 1.79`, `c ≈ 0.56`, cost bound `≈ 0.45`.
Second continuous test, `μ` = law of `aa^T` with `a` uniform on `S^1` (a
degenerate `d = 3 < n²+1` slice of `X`): `k = 1 + 2cos 2θ`, `E[kX] = X_0`
verified entrywise, again atomless with signed `k`. No counterexample on either
domain.

*What a successful refutation would have had to look like, and why none exists.*
The only quantities that could blow up are `E_μ|k|` and `K(v_0,v_0)`. `E_μ|k|` is
bounded below by `1` (Lemma 2(ii)) and enters the entropy bound only through
`−2 log E_μ|k| ≤ 0`, and `K(v_0,v_0) ≤ d ≤ n(n+1)/2` at the Lemma 3 point; and
the Frobenius error is identically `0`, so no `ε` can be too small. The
construction's only visible "cost" is that `‖L‖_F = c` may be as small as
`Θ(1/n)` (it is `≈ 2.07/n` for the uniform measure and for the hypercube
measure). That is *permitted* by the Contract — Reading convention 3 makes the
accuracy relative to `‖L‖_F`, and Remark A shows this is not a vacuous reading
since `M = 0` admits no `L` — and the artifact nowhere claims otherwise. I record
it as an honest feature, not a defect; a referee who wanted a lower bound on
`‖L‖_F` would be asking for a different Contract.

*Common failure patterns probed and not found.* Quantifier order on `C`: correct
(§Step 1). Union bound over an unbounded index: none; the only unions are over
`n−1` basis vectors and `d` basis functions, both finite. Worst-case vs expected:
Lemma 3's averaging is a legitimate existence argument, and the resulting bound
is a pointwise bound at the chosen `v_0`. Asymptotic standing in for an explicit
constant: the reverse — the constant `2/(eδ)` is explicit. Lost reduction factor:
no reduction or hybrid. Oracle/adversary access: n/a. Simulation vs statistical
closeness: n/a. Unshown independence: no independence is claimed anywhere.
Interchange of limit/sum/integral: only finite sums. Missing base case: no
induction, and `n = 1` is treated explicitly. Measure-zero exception treated as
empty: the opposite — Lemma 1(b) and (P1) are precisely the care needed, and
Lemma 3 quarantines off-support values of `g`. Object constructed but not fully
checked: all seven required properties of `(r, L)` are verified in the text.

**Independent check of the source.** I could reach arXiv:1701.06321 (Barak,
Kothari, Steurer, *Quantum entanglement, sum of squares, and the log rank
conjecture*, STOC 2017) and confirm the title, authors, venue and abstract, and I
could confirm the substance of Definition 2.2, Theorem 2.3, the tightness
sentence and the §2.3 unit-norm sentence via the HTML rendering. I could not get
a character-faithful rendering of p. 19 (Question 8.1) or of footnotes 7–8 from
any web source available to me — the PDF text layer was not extractable through
the fetch tool and the HTML rendering returned paraphrase. This is **not** a
class E: the card is supplied and is the designated authority for this review,
and the class D finding above is decided entirely from the card's own Q2/Q5/Q8,
not from anything I failed to reach. I note the limitation only so that the
character-level fidelity claims in "Quotation fidelity" above are understood as
*artifact-versus-card*, which is what was asked.

### SOURCE REQUEST ###

For the class D finding only, and only to let the editor confirm the reading of
the card rather than to fill any gap in the proof:

1. The printed statement of **Theorem 2.3** together with the surrounding text on
   p. 5 of arXiv:1701.06321v2, so that it can be confirmed that "any distribution
   over rank one `n × n` matrices" is not silently restricted to matrices of unit
   Frobenius norm at that point in the paper (card Q2 as it stands says it is
   not, and card Q8's restriction appears only later, in §2.3 on p. 6).
2. The paragraph on p. 6 containing "It can be shown that as stated, Theorem 2.3
   is tight" (card Q5) in full, so that the domain over which the tightness claim
   is asserted can be read off directly.

If both confirm the card, the class D finding stands as written and the fix is
one sentence: delete the assertion that Corollary B's domain is Theorem 2.3's
domain, keeping the artifact's own later, correct sentence that Corollary B
treats only the unit-Frobenius slice.
