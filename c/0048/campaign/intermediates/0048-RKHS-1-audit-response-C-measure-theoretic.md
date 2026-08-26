MODEL: opus

### VERDICT ###
STATUS: DEFECTS
The main line (Lemmas 1–4, Theorem, Corollary) is, to the limit of my checking,
correct and does prove the Contract statement — with room to spare — but
Remark C.1 contains two false mathematical assertions, one of them refuted by
the artifact's own numerical check and the other by an explicit two-line
counterexample; these are confined to a scope remark and do not damage the
Theorem or the Corollary.

### FINDINGS ###

| quoted location | class A-E | explanation |
|---|---|---|
| Remark C.1: "the kernel `k` has `E_μ[k] = 1` but `E_μ\|k\| = K(v_0,v_0)^{1/2}` in general" | B | False as an identity. Cauchy–Schwarz (the artifact's own Lemma 2(iii)) gives only `E_μ\|k\| ≤ K(v_0,v_0)^{1/2}`, with equality iff `\|k\|` is `μ`-a.e. constant. The artifact refutes itself in its own NUMERICAL CHECK: there `E_μ\|k\| = 3/2` while `K(v_0,v_0)^{1/2} = √3 ≈ 1.732`. Since Remark C.1's inference "`k` is negative somewhere whenever `E_μ\|k\| > E_μ[k]`" (which is itself correct) is fed by this false identity, the remark's argument that `k` is signed collapses. |
| Remark C.1: "Our `r` takes both signs unless `μ` is a point mass" | B | False, and not merely unproved. Adversarial `μ`: take `n = 2` and `μ` uniform on `{e_1, −e_1, e_2, −e_2} ⊂ S^1`. A quadratic form `q_Q` takes the value `Q_{11}` at `±e_1` and `Q_{22}` at `±e_2`, so `F_μ` is 2-dimensional (`d = 2`) and, at `v_0 = e_1`, the Riesz representer is `k = 2·1_{{±e_1}}`: indeed `⟨k,f⟩ = ¼(2f(e_1)+2f(−e_1)) = f(e_1)` for every `f ∈ F_μ`, and `E_μ[k] = 1`, `K(v_0,v_0) = 2 = d`, `E_μ[k vv^T] = e_1e_1^T`. Here `k ≥ 0` everywhere, so `E_μ\|k\| = 1`, `c = 1`, `r = k ≥ 0` — a *nonnegative* reweighting — while `μ` is not a point mass and `E_μ[vv^T] = diag(½,½)` is not rank one. The same happens for `μ` uniform on any antipodal pair `{±v}` (`d = 1`, `k ≡ 1`, `r ≡ 1`) and, more generally, for `μ` uniform on `{±e_1,…,±e_n}` (`k = n·1_{{±e_1}}`, entropy `log n`). The correct dividing line is `K(v_0,v_0) = 1`, i.e. `F_μ` = constants, i.e. `vv^T` `μ`-a.e. constant, i.e. `μ` supported on an antipodal pair — not "point mass"; and even outside that case `r` need not be signed. NOT LOAD-BEARING: the Theorem and the Corollary nowhere use that `r` is signed, and I found no actual conflict with the "known boundary" (for the hard `μ`, e.g. uniform on `S^{n−1}`, the kernel `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2` is genuinely negative on `{⟨v,v_0⟩² < 1/(n+2)}`, a set of `μ`-measure `1 − o(1)`). But as written, Remark C.1's stated ground for "no conflict with the paper's tightness claim" is not established. |
| Lemma 1(b), last clause: "Well-definedness of `ev_v` follows, since two representatives of the same class agree `μ`-a.e., hence at `v ∈ supp μ`" | C (routine) | As phrased this is false for arbitrary representatives: an `L²(μ)` class contains representatives differing from `q_Q` at the single point `v`. What is actually needed and actually proved is the displayed statement of (b), i.e. that two *quadratic-form* representatives agree on `supp μ`, and `ev_v` is defined through quadratic-form representatives only. A competent reader repairs the sentence at zero cost; I report it but do not count it toward DEFECTS. |
| Lemma 3: "off the support nothing below uses `g`" | C (routine) | Inaccurate: the very next line defines the *globally* Borel set `A := {g ≤ d}` and applies `μ` to it. The claim survives because `μ(supp μ) = 1` makes both `μ(A)` and `A ∩ supp μ` independent of the choice of representatives `q_j` (only `A ∩ supp μ` is used to produce `v_0`), but the parenthetical as stated overclaims. Routine. |
| Lemma 3 / Theorem: `d ≥ 1` and `supp μ ≠ ∅` never recorded | C (routine) | Both are immediate (`μ(supp μ) = 1` forces `supp μ ≠ ∅`; `[1] = [q_I] ∈ F_μ` is nonzero in `L²(μ)` since `μ` is a probability measure, so `d ≥ 1`), and `d ≥ 1` is needed for "orthonormal basis `f_1,…,f_d`" and for `log K(v_0,v_0) ≥ 0` to be the intended reading. Routine. |
| DEPENDENCIES, footnote 7 quotation "verbatim" | C (hygiene) | The artifact's quotation of footnote 7 stops at "…entries equal." and silently drops the card's closing sentence ("In this paper we are more concerned with rectangles whose distance to being rank one (or monochromatic) is some `ε > 0` that is only a small constant or `1/polylog(n)`"), with no ellipsis. Nothing in the argument turns on the omitted sentence — if anything it supports the artifact's "our constant is independent of `ε`" remark — so this is citation hygiene, not misuse. |

No class A (statement drift) and no class D or E defect found. All eight quotations
used from the source are on the card and are reproduced faithfully (modulo the
footnote-7 truncation above); nothing external is load-bearing for the
mathematics, which is self-contained and elementary.

### STEP LOG ###

STEP 0 (completeness). `### END OF ARTIFACT [M-1] ###` present at line 339; the
last unit (NUMERICAL CHECK) is complete. Not truncated. Proceed.

STEP 1 (statement drift, class A — checked first). What the artifact actually
proves, in my words: *for every `n ≥ 1` and every Borel probability measure `μ`
on `S^{n−1}` there is a point `v_0 ∈ supp μ` and a scalar
`c ∈ [(n(n+1)/2)^{−1/2}, 1]` such that the reproducing kernel of the space of
(classes of) quadratic forms in `L²(μ)`, based at `v_0` and rescaled to have
`E_μ|r| = 1`, satisfies `E_μ[r(v)vv^T] = c·v_0v_0^T` exactly, with entropy cost
`E_μ[|r| log|r|] ≤ log(n(n+1)/2)`; whence, for every `δ > 0`,
`log(n(n+1)/2) ≤ (2/(eδ))·n^δ` for all `n ≥ 1`.*
Diff against the Contract: the Contract asks, for each `ε,δ > 0`, for a finite
`C(ε,δ)` independent of `n` and `μ`, a signed reweighting of entropy cost
`≤ C n^δ`, and a nonzero rank one `L` with relative Frobenius error `≤ ε‖L‖_F`.
The artifact delivers `C = 2/(eδ)` (no `ε`-dependence — allowed, stronger),
relative error `0 ≤ ε‖L‖_F` for every `ε > 0` (stronger), `L = c v_0v_0^T` which
is rank one and nonzero because `c ≥ (n(n+1)/2)^{−1/2} > 0` and `‖v_0‖ = 1`
(exactly what the Contract demands: rank one, nonzero, not required symmetric or
PSD), and `r` Borel and bounded hence `μ`-integrable (Contract convention 2:
no extra regularity added — the artifact adds *more* regularity than required,
which is harmless for an existence claim). Quantifier order: `C` is produced
from `δ` alone, before `n` and `μ` are introduced (Corollary, lines 193–196), so
the "for all `ε,δ` exists `C` for all `n,μ`" order of the Contract is respected,
not the weaker `μ`-dependent-`O(·)` reading that the source's own `O(n^δ)`
notation would permit. Definitions used match the Contract's Definition
verbatim (`E|r| = 1` as an equality, `0 log 0 := 0`, `r` not required
nonnegative). **No statement drift.** Nothing is proved only for large `n`; the
`n = 1` case is handled explicitly.

STEP 2 (Lemma 1(a)) ACCEPTED. `Q ↦ q_Q` linear, so `F_μ = image(Sym_n)` is a
linear subspace of dimension `≤ dim Sym_n = n(n+1)/2`. `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F`
on `S^{n−1}` (the operator-norm inequality is legitimate and restated in
DEPENDENCIES). `L^∞(μ) ⊆ L²(μ)` because `μ` is a probability measure. The
finite-dimensionality is genuine (image of a finite-dimensional space), so `F_μ`
is closed in `L²(μ)` and the `L²(μ)`-norm restricted to `F_μ` is a norm, not a
seminorm (elements are equivalence classes).

STEP 3 (Preliminaries P1, P2) ACCEPTED. (P1): `S^{n−1}` is a second-countable
metric space, `(supp μ)^c` is the union of all open `μ`-null sets, and by
Lindelöf that union is a countable union of null sets, hence null; `supp μ` is
closed, hence Borel, so `μ(supp μ) = 1` is meaningful and true. (P2) is the
defining property of the support and is used only in that direction. `supp μ ≠ ∅`
follows.

STEP 4 (Lemma 1(b) — my angle item (1): point evaluation on the quotient)
ACCEPTED, modulo the phrasing nitpick above. The argument is exactly right and
uses nothing but continuity of `h = q_{Q−Q'}` on `S^{n−1}` and (P2):
`U = {|h| > |h(v_0)|/2}` is open in `S^{n−1}`, contains `v_0 ∈ supp μ`, hence
`μ(U) > 0`; but `U ⊆ {h ≠ 0}` which is `μ`-null. Contradiction. I probed the
degenerate cases my angle called for and (b) survives all of them:
(i) `supp μ` contained in a proper quadric `{q_{Q_0} = 0}` — then `[q_{Q_0}] = 0`
in `L²(μ)` *and* `q_{Q_0} ≡ 0` on `supp μ`, which is precisely the consistency
(b) asserts; no non-degeneracy of `μ` is invoked anywhere.
(ii) `μ` non-atomic with `supp μ = S^{n−1}` (e.g. uniform), and
(iii) `μ = Σ_i 2^{−i} δ_{v_i}` on a countable dense set, where the `v_0` produced
by Lemma 3 may be a *non-atom* of `μ` — the construction never needs
`μ({v_0}) > 0`, and I confirmed no later step assumes it. Point evaluation is
well defined on the quotient exactly because it is defined via the (unique on
`supp μ`) quadratic-form representative; a "point evaluation on `L²(μ)` classes"
is never claimed.

STEP 5 (Lemma 1(c),(d)) ACCEPTED. Riesz on the finite-dimensional inner-product
space `F_μ`: every linear functional is bounded and has a unique representer;
`k_v = Σ_j ev_v(f_j) f_j` in any orthonormal basis; `K(v,v) = ⟨k_v,k_v⟩ =
ev_v(k_v)`. Note (good practice) that no Gram matrix of the spanning family
`{q_{E_{ab}}}` is inverted, so the argument does not covertly assume
`d = n(n+1)/2` or that any operator is invertible — my angle item (5). (d):
`q_I(v) = ‖v‖² = 1` on `S^{n−1}` and `v^T E_{ab} v = v_a v_b` with
`E_{ab} = (e_ae_b^T + e_be_a^T)/2` — both verified by direct computation.

STEP 6 (Lemma 2(i)–(iii)) ACCEPTED. All integrands are bounded (`k` bounded by
Lemma 1(a), `|v_a v_b| ≤ 1`), so every integral converges absolutely; the matrix
identity is asserted and proved entrywise, matching the Contract's entrywise
definition of `E[r vv^T]`, so no Fubini or interchange of limits is used
anywhere in the artifact — my angle item (4) finds nothing to attack.
(i) `E_μ[k v_a v_b] = ⟨k, g_{ab}⟩ = ev_{v_0}(g_{ab}) = (v_0)_a (v_0)_b`: correct,
and the *exactness* of the rank-one conclusion is a genuine consequence of the
reproducing property, not an approximation.
(ii) `E_μ[k] = ⟨k,[1]⟩ = 1`, then `E_μ|k| ≥ |E_μ k| = 1` and
`K = E_μ[k²] ≥ (E_μ|k|)² ≥ 1`, and `k ≠ 0`. Correct. I verified the structural
note (trace of (i)) independently.
(iii) `K = ‖k‖²`, `E_μ|k| ≤ K^{1/2}` by Cauchy–Schwarz against `1`. Correct.
Independent check on `μ` = uniform on `S^{n−1}`: solving
`tr P·I + 2P = n(n+2) v_0v_0^T` gives `k = q_P` with
`P = (n(n+2)/2)v_0v_0^T − (n/2)I`, i.e. `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2`; I
confirmed `E_μ[k] = 1`, `k(v_0) = n(n+1)/2 = d = K(v_0,v_0)`, and
`E_μ[k vv^T] = v_0v_0^T` exactly. Consistent with Lemmas 1–3.

STEP 7 (Lemma 3 — my angle items (2) and (3)) ACCEPTED. Angle item (2), the
"integral of the kernel = a dimension": `K(v,v) = Σ_j q_j(v)²` for
`v ∈ supp μ` by Parseval with `⟨k_v,f_j⟩ = ev_v(f_j) = q_j(v)`; `g := Σ_j q_j²`
is a polynomial, hence Borel and defined *everywhere*, so no measurability or
off-support definedness problem arises; `μ(supp μ) = 1` makes `∫ g dμ =
∫_{supp μ} K(v,v) dμ`; and `∫ g dμ = Σ_j ∫ q_j² dμ = Σ_j ‖f_j‖² = d` because
`∫ q_j² dμ` is by definition `‖f_j‖²_{L²(μ)} = 1`. Representative-independence
is exactly as needed: changing the `q_j` off `supp μ` changes `g` but changes
neither `∫ g dμ` nor `A ∩ supp μ`. Angle item (3), "positive measure delivers a
support point": `μ(A) = 0` would give `h := g − d > 0` `μ`-a.e. together with
`∫ h dμ = 0`; `h ≥ 0` `μ`-a.e. with vanishing integral forces `h = 0` `μ`-a.e.,
and two full-measure sets cannot be disjoint under a probability measure — so
`μ(A) > 0`. Then `μ(A ∩ supp μ) = μ(A) > 0` because `μ((supp μ)^c) = 0`, hence
`A ∩ supp μ ≠ ∅`, and for `v_0` in it `K(v_0,v_0) = g(v_0) ≤ d` legitimately
(the identity (2) holds *at* `v_0` because `v_0 ∈ supp μ`). This is the step my
brief asked me to break, and I could not: the argument does not merely produce a
positive-measure set, it intersects it with a full-measure set. The only
adversarial route would be `μ(supp μ) < 1`, which (P1) excludes on a
second-countable space.

STEP 8 (Lemma 4) ACCEPTED. `φ(t) = t log t ≥ −1/e` on `[0,∞)` (minimum at
`t = 1/e`) and `φ(t) ≤ t²` on `[0,∞)` (for `t ≥ 1` from `log t ≤ t`; for `t < 1`
from `φ ≤ 0`), so `φ(|r|) ∈ L¹(μ)` when `r ∈ L²(μ)` and the entropy is a finite
real number. `dν = |r| dμ` is a probability measure since `E_μ|r| = 1`;
`ν({r = 0}) = ∫_{\{r=0\}} |r| dμ = 0`, so `log|r|` is `ν`-a.e. real-valued and
`E_ν[log|r|] = E_μ[|r| log|r|]` with the `0 log 0 = 0` convention matching a
`ν`-null set — this bookkeeping is done correctly and is the one place where a
`−∞` could have leaked in. `|r|` is `ν`-integrable (`E_ν|r| = E_μ[r²] < ∞`), so
Jensen for the concave `log` applies and gives the claim. The sharpness remark
(equality iff `|r| ∈ {0,c}` a.e.) is correct and unused.

STEP 9 (Proof of the Theorem) ACCEPTED. `E_μ|k| ∈ [1, K^{1/2}]` gives
`c := 1/E_μ|k| ∈ [K^{−1/2}, 1] ⊆ [(n(n+1)/2)^{−1/2}, 1]`; `r := c q_{Q_k}` is a
bounded Borel function with `E_μ|r| = 1`, so admissible; `E_μ[r vv^T] = c v_0v_0^T
=: L` with `‖L‖_F = c |v_0|² = c > 0`, rank one and nonzero, error exactly `0`;
entropy `≤ log E_μ[r²] = log(c²K) ≤ log K ≤ log d ≤ log(n(n+1)/2)` using `c ≤ 1`
(i.e. `E_μ|k| ≥ 1`) and Lemma 3. All quantities are computed on the class, so the
choice of the quadratic-form representative is immaterial to `E_μ|r|`,
`E_μ[r vv^T]` and the entropy. Note the entropy bound is `≥ 0`, as it must be.

STEP 10 (Corollary) ACCEPTED. `n = 1`: `n(n+1)/2 = 1`, bound `0`. `n ≥ 2`:
`n(n+1)/2 ≤ n²` (true for all `n ≥ 1`), so the entropy is `≤ 2 log n`; and
`max_{x>0} (log x)/x^δ = 1/(eδ)` at `x = e^{1/δ}` — I verified the calculus —
gives `2 log n ≤ (2/(eδ)) n^δ`. Hence `C(ε,δ) = 2/(eδ)` is finite, independent of
`n`, `μ` and `ε`. The Contract statement follows.

STEP 11 (Remark A) ACCEPTED (and confirmed not load-bearing). For symmetric `M`
and `ε ∈ (0,1)`: with `L = t u w^T`, `‖M − L‖_F² = ‖M‖_F² − 2t·u^TMw + t²`
(since `⟨M,L⟩ = t·u^TMw`), the constraint is
`(1−ε²)t² − 2(u^TMw)t + ‖M‖_F² ≤ 0`, maximising `u^TMw` at `s_1(M) = |λ_1|` is
optimal because `t > 0`, and solvability is the discriminant condition
`s_1² ≥ (1−ε²)Σ_i λ_i²`, which rearranges exactly as claimed; positivity of the
roots is checked correctly via product and sum. The `M = 0` case needs `ε < 1`,
which the remark assumes.

STEP 12 (Corollary B) ACCEPTED with a routine gap only. `X` is compact (closed:
rank `≤ 1` is closed and on `‖X‖_F = 1` rank `≤ 1` forces rank `= 1`; bounded)
and second countable, so (P1)/(P2) transfer; `G` is a linear space of affine
functions of dimension `≤ n²+1`, contains the constant `1` and every coordinate
`X ↦ X_{ab}`, and its elements are continuous and bounded on `X` — which are
exactly the two inputs Lemmas 1–4 used. So `E_μ[k] = 1`, `E_μ[k X] = X_0`,
`K(X_0,X_0) ≤ d ≤ n²+1`, `c = 1/E_μ|k| ∈ (0,1]`, entropy `≤ log(n²+1)`. The
stated equivalence `X = ab^T` with `‖a‖ = ‖b‖ = 1` is correct. The transfer is
stated rather than rewritten, but every used property is named; routine.

STEP 13 (Remark C) DEFECTIVE in part 1 — see FINDINGS. Parts 2 and 3 are
scope claims, correctly grounded in cards Q4 and Q1 respectively (flatness is
indeed required by the dictionary quoted in Q4, and the artifact is candid that
`ev_{v_0}` has no pseudo-distribution analogue because Lemma 1(b) is where
`supp μ` enters). I checked that `Remark C` is not used by any earlier step.

STEP 14 (Numerical check) ACCEPTED and independently reproduced. With
`μ` uniform on `v_1 = (1,0)`, `v_2 = (0,1)`, `v_3 = (1,1)/√2`, `v_4 = (1,−1)/√2`,
a quadratic form `Q = [[a,b],[b,c]]` has value vector
`(a, c, (a+c)/2 + b, (a+c)/2 − b)`, so `F_μ = {x : x_1+x_2 = x_3+x_4}` and
`d = 3`. Solving `¼ k·f = f_1` for all `f ⊥ (1,1,−1,−1)` with `k ∈ F_μ` gives
`k = (3,−1,1,1)`; `E_μ[k] = 1`, `‖k‖² = 3 = d`,
`¼(3v_1v_1^T − v_2v_2^T + v_3v_3^T + v_4v_4^T) = v_1v_1^T` (I computed
`[[4,0],[0,0]]/4`), `E_μ|k| = 3/2`, `c = 2/3`, `E_μ[r²] = 4/3`,
entropy `= ½log(4/3) = 0.1438`. All stated numbers check out. (This same example
is what refutes Remark C.1's identity: `3/2 ≠ √3`.)

STEP 15 (source use, classes D/E) ACCEPTED. Every external mathematical
ingredient (Riesz on a finite-dimensional space, Cauchy–Schwarz, Jensen,
`‖Q‖_op ≤ ‖Q‖_F`, `μ(supp μ) = 1` on a second-countable space,
`max_{x>0}(log x)/x^δ = 1/(eδ)`) is standard and restated in usable form; none is
misapplied. Every quotation from BKS is covered by card S1 and is faithful (see
the footnote-7 hygiene note). The claim that Question 8.1 (card Q1) "matches the
statement of the Contract with no additional hypothesis" is correct, and in fact
the artifact proves the *uniform-in-`μ`* reading that the Contract fixes, which
is the stronger of the two readings the source's `O(n^δ)` notation admits. No
class E: nothing load-bearing rests on a source I could not check.

### SOURCE REQUEST ###
none
