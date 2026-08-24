MODEL: opus

### VERDICT ###

STATUS: DEFECTS

The main line (Lemmas 1-4, Theorem, Corollary) survives a sustained refutation
attempt across seven explicitly computed measures and is, as far as I can check,
correct and strictly stronger than the Contract; but Remark C contains one false
quantitative claim, one claim deferred to a source that does not exist, two
overreaching conclusions about the cited external problems that the source card
does not support, and two quotations labelled "verbatim" from which material
clauses have been silently dropped.

### FINDINGS ###

| quoted location | class A-E | explanation |
|---|---|---|
| REMARK C.1: "negative on `{⟨v,v_0⟩² < 1/(n+2)}`, a set of `μ`-measure `1 − o(1)`" | B | False for every `n`. Under `μ` uniform on `S^{n-1}`, `t := ⟨v,v_0⟩` has density proportional to `(1−t²)^{(n−3)/2}`, so `μ{t² < 1/(n+2)} = P(n t² < n/(n+2))`. Since `n t² ⇒ χ²_1`, this tends to `P(χ²_1 < 1) = 2Φ(1) − 1 = 0.6827`, and is smaller for small `n`: exactly `1/3` at `n = 2` (`P(|cos θ| < 1/2)`), exactly `1/√5 = 0.4472` at `n = 3` (`t ~ U[−1,1]`), `0.611` at `n = 10` (Simpson against the Beta normalisation `√π Γ(4.5)/(2Γ(5))`). The measure is bounded above by `≈ 0.683` uniformly in `n`, hence is not `1 − o(1)`; it is not even `1 − o(1)` along a subsequence. The kernel formula `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2` itself IS correct (I re-derived `E[k] = 1`, `E[k v_1²] = 1`, `E[k v_2²] = 0`, `K = n(n+1)/2` from `E[t²] = 1/n`, `E[t⁴] = 3/(n(n+2))`, `E[t²v_2²] = 1/(n(n+2))`), and the surviving qualitative claim — `k < 0` on a set of positive measure — is true. NOT LOAD-BEARING for the Theorem or the Corollary; it is load-bearing only for the rhetorical force of Remark C.1's consistency check. |
| REMARK C.1: "(exact check recorded in the review of this artifact; not re-derived here)" | E | A quantitative claim in the artifact is discharged by citing a document that is not the artifact and is not supplied to me — indeed a document downstream of the artifact. I cannot reach it, no card covers it, and the claim it is asked to support is the false one above. The artifact needs this source to say that `μ{⟨v,v_0⟩² < 1/(n+2)} = 1 − o(1)`; no such source can say so. Non-load-bearing, so it does not by itself block the Theorem, but it is a genuine unverifiable citation and it is exactly why the claim should have been derived in place. |
| REMARK C.1: "so a conflict would require our construction to come out nonnegative on the hard `μ`. It does not." | C | The "hard `μ`" are not identified anywhere in the artifact or the card — Q1 asserts only that the answer is "No if one does not allow negative reweighting functions", which is an existential statement over `μ` with no witness. The artifact therefore cannot check its own construction on them, and "It does not" is asserted, not shown. The uniform-sphere computation that follows establishes signedness for ONE measure that is nowhere claimed to be a hard instance. The parenthetical two sentences later — "(No claim is made that the construction's `r` is signed for *every* non-point-mass `μ`.)" — contradicts the unqualified "It does not". I judge this a real gap rather than a routine one, because it is precisely the point at which a reader would want to know whether the Theorem contradicts the cited paper. (Note for the record, not as a repair: I closed this myself in the other direction — see STEP LOG item R11 — and found no contradiction. That the gap is fillable does not make it filled.) |
| REMARK C.2 heading: "The log rank consequence does not follow." | D | Overreach against the card. Card Q1 records the paper's own statement that a positive solution to Question 8.1 for any `δ < 1/2` "may improve the best known bound for the log rank conjecture to `Õ(n^δ)`", with NO flatness caveat attached to that clause (the pseudo-distribution caveat in the same sentence is attached only to the running-time clause). The artifact's entire ground for the flat negative is that the one dictionary the card quotes, Q4, is stated for *flat* distributions. Nothing in the card says Q4 is the only bridge from a reweighting to a log-rank bound; §2.2 is quoted only as a single clause, and the actual reduction is not in the card at all. So the artifact settles by assertion a tension between its own result and the source paper's stated expectation, in the source paper's disfavour, on the strength of an excerpt. The narrower claim the card does support is "the quoted dictionary cannot be invoked for this `r`", which is not the same proposition as "the log rank consequence does not follow". Compounding this, "flat" is a technical term the card never defines (its own note only says flat is "distinct from" deficient), so "nothing in its construction constrains `r` to be flat" is a claim about an undefined predicate. |
| REMARK C.3: "unavailable in the setting the paper actually needs (\"if appropriately extended to pseudo-distributions\", p. 19)" | D | Misreads the scope of the quoted clause. In card Q1 the sentence is: "It may improve the best known bound for the log rank conjecture to `Õ(n^δ)` **and if appropriately extended to pseudo-distributions**, improve our algorithm's running time to `exp(Õ(n^δ))` as well." The pseudo-distribution extension is attached by the source to the *algorithm's running time* only; the log-rank clause carries no such condition. Calling the pseudo-distribution setting "the setting the paper actually needs" therefore promotes one of the two advertised consequences into the sole one, which the quoted words do not support. |
| REMARK C.3: "a pseudo-distribution has no support points"; "The inner product used ... is a degree-4 moment and so *does* have a pseudo-distribution analogue" | E | Substantive technical assertions about "pseudo-distribution" and "sos", terms that the card nowhere defines and about which it makes no claim beyond the four words "extended to pseudo-distributions". I have no card and no in-artifact definition against which to check either assertion, and the artifact's DEPENDENCIES section explicitly claims all external mathematics used is "all standard, all elementary, none from a paper" — which is not true of these two. Non-load-bearing; recorded because Remark C.3 is offered as an "exact obstruction" and an exact obstruction stated in undefined terms cannot be checked. |
| DEPENDENCIES: "Footnote 7, p. 6, verbatim: ..." | D | Labelled verbatim but truncated without ellipsis. Card Q6 continues: "In this paper we are more concerned with rectangles whose distance to being rank one (or monochromatic) is some `ε > 0` that is only a small constant or `1/ polylog(n)`." The omitted sentence is the one that calibrates the source's `ε` regime, i.e. it is directly relevant to the artifact's boast of `ε`-independence. Low severity — the omission does not favour the artifact and footnote 7 carries nothing load-bearing — but a quotation marked verbatim must be verbatim. |
| COROLLARY B / DEPENDENCIES: "§2.3, p. 6, verbatim: \"We will restrict our attention to the case that all the columns of `U` and `V` are of unit norm.\"" used to justify "the normalisation used in the source paper's intended application" | D | Same defect, and here it is self-serving in a small way. Card Q8 continues: "(This restriction is easy to lift and anyway holds automatically in our intended application.)" The dropped parenthetical is the only place the card mentions the intended application, so the artifact's gloss is licensed by words it does not quote. It cuts the other way too: the card says the restriction "is easy to lift" *for the source paper*, whereas Corollary B's method genuinely requires it (unnormalised rank-one matrices form an unbounded set, on which the elements of `G` are unbounded and Lemma 1(a) fails). Corollary B's heading "the same for distributions over general rank one matrices" therefore overstates its own hypothesis, which is `rank X = 1` **and** `‖X‖_F = 1`; the source's Theorem 2.3 (Q2) is stated for "any distribution over rank one `n × n` matrices". The body states the hypothesis correctly, so this is a heading/scope defect, not a mathematical one. |

No class-A statement drift found; no class-B, -C, -D or -E defect found anywhere
in the chain Lemma 1 → Lemma 2 → Lemma 3 → Lemma 4 → Theorem → Corollary, which
is the entirety of what the Contract asks for. Remark A is independently correct.
Corollary B is correct as stated in its body. All defects above lie in the
commentary and the citation apparatus.

### STEP LOG ###

**Step 0. Completeness.** `### END OF ARTIFACT [P-1] ###` present as the final
line (line 362). No unit stops mid-sentence. Gate passed; I verified the whole
artifact.

**Step 1 (class A first). What the artifact actually proves, in my words.**
For every `n ≥ 1` and every Borel probability `μ` on `S^{n-1}`, let `F_μ` be the
image in `L²(μ)` of the real quadratic forms, `d = dim F_μ`. Then there is a
point `v_0 ∈ supp μ` at which the reciprocal Christoffel function is at most `d`,
and the reproducing kernel `k = k_{v_0}` of `F_μ` at that point, rescaled by
`c = 1/E_μ|k| ∈ [K(v_0,v_0)^{-1/2}, 1]`, is a bounded Borel function with
`E_μ|ck| = 1`, `E_μ[ck·vv^T] = c v_0v_0^T` **exactly** (Frobenius error zero, not
`ε`), and `E_μ[|ck| log|ck|] ≤ log K(v_0,v_0) ≤ log(n(n+1)/2)`.
Diff against the Contract: the Contract asks for `≤ C(ε,δ)n^δ` entropy and
`≤ ε‖L‖_F` error, for a `C` chosen before `n` and `μ`. The artifact delivers
`≤ log(n(n+1)/2)` entropy — independent of `ε` and of `δ` — and error `0`, with
`L = c v_0v_0^T` rank one and nonzero because `c ≥ (n(n+1)/2)^{-1/2} > 0`. The
Corollary then quantifies `C = 2/(eδ)` before `n, μ`. Quantifier order is the
Contract's; the conclusion is strictly stronger, not weaker; no asymptotic stands
in for an exact constant (the constant is explicit); "signed reweighting" is used
with the Contract's Definition, not an easy reading. ACCEPTED, no drift.

**Step 2. Lemma 1(a).** `Q ↦ q_Q` linear, `F_μ` its image, `d ≤ dim Sym_n =
n(n+1)/2`. `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F` on `S^{n-1}`. `L^∞(μ) ⊆ L²(μ)` as `μ` is a
probability measure. ACCEPTED.

**Step 3. Lemma 1(b) and (P1),(P2).** `h := q_{Q−Q'}` is continuous; if
`h(v_0) ≠ 0` at `v_0 ∈ supp μ` then `{|h| > |h(v_0)|/2}` is open, contains `v_0`,
has positive measure by (P2), and sits inside a null set. `μ(supp μ) = 1` via
second countability of `S^{n-1}`. Well-definedness of `ev_v` on classes is
correctly restricted to quadratic-form representatives, and any two such
representatives of one class agree at every support point by the displayed
statement. This is the step the artifact itself flags as the only place the
general Borel case differs from the finite case, and it is done properly.
ACCEPTED.

**Step 4. Lemma 1(c),(d).** Finite-dimensional subspace of `L²(μ)` is a Hilbert
space; `ev_v` linear on it hence bounded; Riesz gives a unique `k_v ∈ F_μ`;
`K(v,v) = ⟨k_v,k_v⟩ = ev_v(k_v)`. `q_I ≡ 1` on the sphere and
`q_{(e_ae_b^T+e_be_a^T)/2}(v) = v_av_b` (including `a=b`, where `E_aa = e_ae_a^T`).
ACCEPTED.

**Step 5. Lemma 2 — the crux, checked hard.** `⟨k,g_{ab}⟩_{L²(μ)} = E_μ[k v_av_b]`
by definition of the inner product, and `ev_{v_0}(g_{ab}) = (v_0)_a(v_0)_b`;
matching all `(a,b)` gives `E_μ[k vv^T] = v_0v_0^T` exactly. `[1] ∈ F_μ` gives
`E_μ[k] = 1`, hence `E_μ|k| ≥ 1` and `K = E_μ[k²] ≥ (E_μ|k|)² ≥ 1` and `k ≠ 0`.
Cauchy-Schwarz gives `E_μ|k| ≤ K^{1/2}`. Absolute convergence from boundedness of
`k` and of `v_av_b`. The structural note (the `E_μ[k] = 1` identity is the trace
of the matrix identity, available only because `‖v‖ = 1` makes the constant a
quadratic form) is correct and is the right diagnosis of where the free
normalisation comes from. ACCEPTED.

**Step 6. Lemma 3.** `k_v = Σ_j q_j(v) f_j` by Parseval and `ev_v(f_j) = q_j(v)`;
`K(v,v) = Σ_j q_j(v)²` on `supp μ`; `g := Σ_j q_j²` is a polynomial, Borel, agrees
with `K(·,·)` up to a null set by (P1); `∫g dμ = Σ_j ‖f_j‖² = d`. The averaging
argument is stated correctly, including the degenerate branch: if `μ{g ≤ d} = 0`
then `h := g − d > 0` `μ`-a.e. with `∫h dμ = 0`, impossible. Then `μ(A) > 0` plus
`μ(supp μ) = 1` gives `μ(A ∩ supp μ) > 0`, hence nonempty — this is the
"measure-zero exception treated as empty" trap and the artifact does not fall in
it. Nothing below uses `g` off the support, as stated. ACCEPTED.

**Step 7. Lemma 4.** `φ(t) = t log t` satisfies `φ ≥ −1/e` on `t ≥ 0` (min at
`1/e`) and `φ(t) ≤ t²` on `t ≥ 0` (`log t ≤ t` for `t ≥ 1`; `φ ≤ 0 ≤ t²` for
`t < 1`), so `φ(|r|) ∈ L¹(μ)` and the entropy is a finite real number — the
integrability is actually checked rather than assumed. `dν := |r|dμ` is a
probability measure with `ν{r = 0} = 0`, so `log|r|` is `ν`-a.e. finite,
`E_ν[log|r|] = E_μ[|r|log|r|]` with the stated convention matching a `ν`-null
set, and `E_ν[|r|] = E_μ[r²] < ∞`. Jensen for the concave `log` against `ν` is
applied in the correct direction to a `ν`-integrable, `ν`-a.s. positive random
variable. The sharpness note is also correct: equality forces `|r|` constant on
`{r ≠ 0}`, and then `E_μ[r²] = c = 1/μ{|r| = c}`. ACCEPTED.

**Step 8. Proof of the Theorem.** `c = 1/E_μ|k| ∈ [K^{-1/2},1] ⊆
[(n(n+1)/2)^{-1/2},1]` from Step 5 and Step 6. `r = c q_{Q_k}` is a polynomial
restricted to the sphere, hence bounded Borel hence `μ`-integrable, and
`E_μ|r| = 1`, so `r` is admissible for the Contract's Definition. `‖c v_0v_0^T‖_F
= c‖v_0‖² = c > 0`, rank one, nonzero, and the error is exactly `0 ≤ ε c` for
every `ε > 0`. Entropy: `E_μ[|r|log|r|] ≤ log E_μ[r²] = log(c²K) = log(K/(E|k|)²)
≤ log K ≤ log(n(n+1)/2)`, each inequality unconditional. ACCEPTED.

**Step 9. Corollary.** `n = 1`: `n(n+1)/2 = 1`, bound `0`. `n ≥ 2`: `n(n+1)/2 ≤
n²` (true for all `n ≥ 1`), so `log(n(n+1)/2) ≤ 2 log n`; and `max_{x>0} (log
x)/x^δ = 1/(eδ)` at `x = e^{1/δ}` (I differentiated: `x^{δ-1}(1 − δ log x)/x^{2δ}`),
giving `2 log n ≤ (2/(eδ))n^δ`. `C = 2/(eδ)` is finite for each `δ > 0`, depends
on neither `n` nor `μ` nor `ε`. ACCEPTED. The Contract is delivered.

**Step 10. Remark A.** Independently re-derived. `‖M − tuw^T‖_F² = ‖M‖_F² − 2t
u^TMw + t²`; the constraint is `(1−ε²)t² − 2(u^TMw)t + ‖M‖_F² ≤ 0`;
`max_{‖u‖=‖w‖=1} u^TMw = s_1(M) = |λ_1|` for symmetric `M`; discriminant
`≥ 0 ⟺ λ_1² ≥ (1−ε²)Σλ_i² ⟺ Σ_{i≥2}λ_i² ≤ ε²λ_1²/(1−ε²)`; both roots positive
when `M ≠ 0`; `ε ∈ (0,1)` is assumed so `1−ε² > 0` and the `M = 0` case is right.
The parametrisation covers non-symmetric rank one `L`, as the Contract permits.
ACCEPTED, and it does establish the artifact's point that the relative
normalisation is not being exploited degenerately.

**Step 11. Corollary B.** `X = {rank X = 1, ‖X‖_F = 1}` is closed (a limit of
rank-one matrices of unit Frobenius norm has rank `≤ 1` and norm `1`, hence rank
exactly `1`) and bounded, so compact and second countable; `G` is a linear (the
artifact says "affine", a harmless slip) space of dimension `≤ n²+1` of continuous
functions, containing the constant `1` and each coordinate `X ↦ X_{ab}`. Lemmas
1-4 do transfer on those two properties plus continuity and boundedness, and
`c ∈ (0,1]`, `E[rX] = cX_0` exactly rank one nonzero, entropy `≤ log(n²+1)`.
ACCEPTED as stated in the body; see the FINDINGS row on its heading and its
citation.

**Step 12. Numerical check in the artifact, independently re-derived.**
`x_1 = a`, `x_2 = c`, `x_3 = (a+c)/2 + b`, `x_4 = (a+c)/2 − b`, so
`F_μ = {x_1+x_2 = x_3+x_4}`, `d = 3`. `k = (3,−1,1,1)` lies in `F_μ` and
`⟨k,x⟩ = (1/4)(3x_1 − x_2 + x_3 + x_4) = (1/4)(4x_1) = x_1`. `E_μ[k] = 1`,
`‖k‖² = 3 = d`, `E_μ[k vv^T] = (1/4)[[4,0],[0,0]] = v_1v_1^T`. `E_μ|k| = 3/2`,
`c = 2/3`, `r = (2,−2/3,2/3,2/3)`, `E_μ|r| = 1`, entropy `= (1/2)log(4/3) =
0.143841`, `log E_μ[r²] = log(4/3) = 0.287682`, `log 3 = 1.098612`. Every figure
in the artifact is right to the digits printed, and `r` is indeed signed.
ACCEPTED.

**REFUTATION ATTEMPT — what I tried and what happened. I could not refute the
Theorem.** Stated plainly: after the following seven concrete measures plus two
structural attacks, I found no `n` and no `μ` for which the construction fails to
deliver an exactly-rank-one nonzero `L`, and none for which the entropy exceeds
`log(n(n+1)/2)`.

R1. Degenerate: `μ = δ_{v_0}`. `F_μ` collapses to the constants, `d = 1`, `k ≡ 1`,
`E[k vv^T] = v_0v_0^T`, `c = 1`, entropy `0`. Delivers.

R2. Degenerate: `μ = pδ_{v_0} + (1−p)δ_{−v_0}`. Quadratic forms cannot separate
antipodes, so again `d = 1`, `k ≡ 1`, entropy `0`. Delivers. (I tried this
specifically hoping `ev_{v_0}` would be ill-defined; it is not, because `q_Q(v_0)
= q_Q(−v_0)` for every quadratic form, so Lemma 1(b) is unstrained.)

R3. Degenerate: `n = 2`, `μ = pδ_{(1,0)} + (1−p)δ_{(0,1)}`, `p` small. Here
`d = 2`, `k_{(1,0)} = (1/p, 0)`, `K = 1/p → ∞` as `p → 0`. This is the attempt to
blow up the entropy. It fails because Lemma 3 does not let you pick the base
point: `∫K dμ = p(1/p) + (1−p)/(1−p) = 2 = d`, and Lemma 3 forces the atom of
mass `≥ 1/2`, giving `K ≤ 2` and entropy `log(1/p') ≤ log 2 ≤ log 3`. The "cheap
base point" step is exactly what defeats this attack, and it is correctly stated.

R4. Bound-saturating: `μ` uniform on `d = n(n+1)/2` points in general position.
Then `k = d·1_{v_0}` and the entropy equals `log d` exactly — the Lemma 4 bound is
attained, `r ≥ 0`, and this is plain conditioning on one atom. Cost `2 log n`,
still `≤ (2/(eδ))n^δ`. No overrun. Same for `μ` uniform on `e_1,…,e_n` (`d = n`,
entropy `log n`).

R5. Continuous: `μ` uniform on `S^{n-1}`, all `n`. Verified the kernel from
scratch as recorded in FINDINGS; `E[k vv^T] = v_0v_0^T` exactly. Asymptotically
`k ≈ (n/2)(Z²−1)` with `Z ~ N(0,1)`, `E|k| → 0.4839n`, `r → (Z²−1)/0.96788`, and
the entropy tends to an absolute constant, three orders below the `log(n(n+1)/2)`
bound. Delivers, cheaply.

R6. Continuous and degenerate simultaneously: `μ` uniform on a great circle of
`S²`, where `d = 3 < 6 = n(n+1)/2`, so the kernel is not the full-sphere one and
`E[k vv^T]` must still kill the third row and column. `k(θ) = 1 + 2cos2(θ−θ_0)`;
I verified `E[k] = 1`, `K = 3 = d`, and `E[k vv^T] = e_1e_1^T` exactly including
the vanishing third row/column. `E|1+2cos u| = (1/2π)(2π − 2(2π/3 − 2√3)) =
1.43610`, `c = 0.69633`; entropy by 12-interval Simpson `= 0.2500`, against the
bound `log(c²·3) = log 1.45461 = 0.37475 ≤ log 3`. Delivers.

R7. The artifact's own 4-point example, re-derived from scratch (Step 12).

R8. Cost-overrun attack in general. The chain
`entropy ≤ log E[r²] = log(c²K) ≤ log K ≤ log d ≤ log(n(n+1)/2)` uses only
`c = 1/E_μ|k| ≤ 1`, which follows from `E_μ|k| ≥ |E_μ k| = 1`, which follows from
`[1] ∈ F_μ`, which holds because `‖v‖ = 1`. There is no measure-dependent slack
anywhere, so no `μ` can push the cost above `log(n(n+1)/2)`. The Corollary's
arithmetic is exact rather than asymptotic. Attack fails.

R9. Relative-normalisation attack. I checked whether `L` could be forced to `0`
or the error to exceed `ε‖L‖_F`. `‖L‖_F = c ≥ (n(n+1)/2)^{-1/2} > 0` and the error
is identically `0`, so the `M = 0` failure mode that Remark A correctly identifies
never arises. Attack fails.

R10. Measurability/regularity attack. I looked for a `μ` making `r`
non-measurable or non-integrable, since the Contract forbids adding regularity.
`r` is a fixed polynomial restricted to the sphere, so it is bounded and Borel for
every `μ`; and both `E_μ[r vv^T]` and `E_μ[|r|log|r|]` depend only on the
`μ`-class, so the choice of representative is immaterial. Attack fails.

R11. The most promising attack: manufacture a contradiction with card Q1's "the
answer to this question is No if one does not allow negative reweighting
functions". If the constructed `r` were `≥ 0` `μ`-a.e. for some `μ` that is hard
for nonnegative reweightings, the Theorem and Q1 could not both hold. Working the
consequence: `k ≥ 0` with `E_μ[k] = 1` makes `dμ' := k dμ` a probability measure
with `E_{μ'}[vv^T] = v_0v_0^T`, so for every unit `w ⊥ v_0` we get
`E_{μ'}⟨v,w⟩² = w^Tv_0v_0^Tw = 0`, hence `⟨v,w⟩ = 0` `μ'`-a.s.; ranging `w` over
an orthonormal basis of `v_0^⊥` forces `μ'` to be supported on `{±v_0}`, hence
`μ` to have an atom there of mass `≥ 1/K ≥ 2/(n(n+1))`. So on any atomless `μ`
the construction is necessarily signed, and on `μ` with such a heavy atom the
instance is easy for nonnegative reweightings anyway (conditioning costs
`log(1/mass) ≤ log(n(n+1)/2)`). Both branches are consistent with Q1 and with Q5,
so this route is closed and the attack fails. I record this because it is the
argument Remark C.1 asserts without giving; the assertion remains a class-C gap
in the artifact regardless of the fact that it happens to be true.

Net: the Contract-relevant chain is, on my reading, correct, and I say so plainly
rather than dressing a failed refutation up as a defect. What the artifact
exploits is that on the sphere the constant function is a quadratic form, so the
degree-2 reproducing kernel simultaneously normalises itself (`E_μ[k] = 1`) and
reproduces the second-moment matrix (`E_μ[k vv^T] = v_0v_0^T`), while the mean
reciprocal Christoffel function `∫K dμ = d ≤ n(n+1)/2` caps the second moment and
hence, via Jensen, the entropy. Every one of those four ingredients is proved in
the artifact from restated elementary facts.

**Step 13. Source fidelity, item by item against the card.** Q1 (Question 8.1 and
the following paragraph): reproduced verbatim, no clause dropped, and the
artifact's claim that this "matches Conjecture conj:main of the Contract with no
additional hypothesis" is a fair reading — the only gap between Q1's `O(n^δ)` and
the Contract's `C(ε,δ)n^δ` is the placement of the hidden constant, which the
Contract's reading convention 1 fixes in the harder direction (uniform in `n` and
`μ`), and the artifact meets that harder reading. Q1 imposes no measurability
requirement on `r`; the Contract adds Borel measurability, and the artifact's `r`
satisfies it, so no hypothesis is smuggled either way. Q2 (Theorem 2.3):
verbatim. Q9 (Definition 2.2): verbatim, and the "deficient, hence nonnegative"
gloss is textually the card's own closing note, so the gloss is inside the card's
words — this is the one place where the artifact's use of a definitional gloss is
fully clean. Q4: verbatim as a clause. Q5: verbatim. Q7: verbatim, and the "moot
here" comment is fair since the artifact's `C` genuinely has no `ε` in it. Q6 and
Q8: quoted as "verbatim" with material final clauses silently dropped — see
FINDINGS. Terms used substantively but never defined by the card:
"pseudo-distribution", "sos", "flat", "log rank conjecture" — see FINDINGS.
Conclusions drawn about the external problems (Remark C.2's flat negative on log
rank, Remark C.3's "the setting the paper actually needs") exceed the card in the
conservative direction — see FINDINGS. I found no overreach in the *inflationary*
direction: the artifact nowhere claims the log-rank conjecture, the algorithm
speed-up, or the pseudo-distribution version, and its statement that "the source
paper's Question 8.1 is answered affirmatively, as literally posed" is supported
by Q1 read together with the Contract's reading conventions.

### SOURCE REQUEST ###

1. For the (E) at REMARK C.1: the document the artifact calls "the review of this
   artifact", in which the "exact check" of `μ{⟨v,v_0⟩² < 1/(n+2)}` is said to be
   recorded. The artifact needs it to certify that this measure is `1 − o(1)`. I
   compute `1/3` at `n = 2`, `1/√5` at `n = 3`, `0.611` at `n = 10` and
   `2Φ(1) − 1 = 0.6827` in the limit, so I expect no admissible source exists and
   the sentence should be corrected rather than sourced.

2. For the (D) at REMARK C.2: the full text of Barak-Kothari-Steurer §2.2 and of
   whatever passage carries the reduction behind "It may improve the best known
   bound for the log rank conjecture to `Õ(n^δ)`" (card Q1). The card supplies
   §2.2 only as the single flatness clause Q4, which is not enough to license the
   claim that no route from a signed reweighting to a log-rank bound exists.

3. For the (D) at REMARK C.3 and the (E) on "pseudo-distribution": the paper's
   definition of a pseudo-distribution and of `Ẽ` (the latter appears unexplained
   inside card Q2), sufficient to check "a pseudo-distribution has no support
   points" and "a degree-4 moment ... does have a pseudo-distribution analogue".

4. For the two truncated quotations: the full footnote 7 (card Q6) and the full
   §2.3 sentence with its parenthetical (card Q8) are already on the card; I do
   not need them re-supplied, only the artifact's quotations corrected to match or
   marked with ellipses.
