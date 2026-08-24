MODEL: fable

### VERDICT ###
STATUS: CLEAN
Every algebraic step, inequality, normalisation constant, dimension count, and numerical claim in the artifact recomputes correctly, the proved theorem is strictly stronger than the Contract statement (exact rank-one equality, entropy cost log(n(n+1)/2) ≤ (2/(eδ))·n^δ with C independent of ε), and every external quotation is covered verbatim by source card S1.

### FINDINGS ###
| quoted location | class A-E | explanation |
| --- | --- | --- |
| — | — | No defects of class A, B, C, D or E found. Every number stated in the artifact (kernel entries, the three identities, normalisations, entropy chain, measure lower bounds on both domains, dimension counts, the constant 2/(eδ), and the calculus maximum) was independently recomputed and verified from the artifact's own contents; none was unverifiable. |

### STEP LOG ###
STEP 0 (completeness): `### END OF ARTIFACT [W-1] ###` present at the end; no unit stops mid-sentence, mid-equation or mid-proof. Proceed.

STATEMENT DRIFT (checked first): The artifact proves — for every n ≥ 1 and every Borel probability μ on S^{n-1} — the existence of a signed reweighting r (E_μ|r| = 1, r a bounded quadratic form, hence Borel and μ-integrable) and a nonzero rank-one PSD L = c·v₀v₀ᵀ with E_μ[r vvᵀ] = L exactly (Frobenius error 0) and entropy cost E_μ[|r| log|r|] ≤ log(n(n+1)/2), and then in the Corollary that this implies the Contract with C(ε,δ) = 2/(eδ). Diff against Contract: exact equality implies ‖E[r vvᵀ] − L‖_F = 0 ≤ ε‖L‖_F for every ε > 0; entropy log(n(n+1)/2) ≤ (2/(eδ))n^δ with a constant depending only on δ, permitted (Contract allows dependence on ε and δ; independence of ε is a strengthening, and matches Contract convention 1). Signedness of r is permitted by the Contract; L is not required symmetric/PSD, so PSD is fine; r is Borel and μ-integrable as required, no extra regularity assumed. Quantifier order matches: r and L depend on n and μ; C does not. No drift.

Lemma 1(a): Q ↦ q_Q linear, F_μ its image in L²(μ), so d ≤ dim Sym_n = n(n+1)/2 — dimension count n(n+1)/2 recomputed, correct. |vᵀQv| ≤ ‖Q‖_op‖v‖₂² = ‖Q‖_op ≤ ‖Q‖_F on S^{n-1} (operator norm bounded by Frobenius: standard, restated in DEPENDENCIES). L^∞(μ) ⊆ L²(μ) for probability μ. Accepted.

Lemma 1, Preliminaries (P1): complement of supp μ is a union of open null sets; S^{n-1} second countable ⇒ Lindelöf ⇒ countable subunion covers ⇒ null. Accepted. (P2) is the definition of support. Accepted.

Lemma 1(b): h = q_{Q−Q'} continuous, μ({h ≠ 0}) = 0; if h(v₀) ≠ 0 at a support point, U = {|h| > |h(v₀)|/2} is open (continuity), contains v₀, so μ(U) > 0 by (P2), yet U ⊆ {h ≠ 0} null — contradiction. Well-definedness and linearity of ev_v follow as written. Accepted.

Lemma 1(c): finite-dimensional subspace of L²(μ) is a Hilbert space; every linear functional bounded; Riesz gives unique k_v; explicit formula k_v = Σ_j ev_v(f_j) f_j for any orthonormal basis verified by testing against each f_j; K(v,v) = ev_v(k_v) by taking f = k_v. Accepted.

Lemma 1(d): q_I(v) = ‖v‖₂² = 1 on the sphere; q_{E_ab}(v) = vᵀ(e_a e_bᵀ + e_b e_aᵀ)v/2 = v_a v_b — recomputed, the symmetrised E_ab with the factor 1/2 is exactly right. Accepted.

Lemma 2, absolute convergence: k bounded (Lemma 1(a)), |v_a v_b| ≤ 1 on the sphere. Accepted.

Lemma 2(i): E_μ[k v_a v_b] = ⟨k, g_ab⟩ = ev_{v₀}(g_ab) = (v₀)_a(v₀)_b for each (a,b); entrywise identity E_μ[k vvᵀ] = v₀v₀ᵀ. Recomputed. Accepted.

Lemma 2(ii): E_μ[k] = ⟨k,[1]⟩ = ev_{v₀}([1]) = q_I(v₀) = 1; E_μ|k| ≥ |E_μ k| = 1; Cauchy–Schwarz (E|k|)² ≤ E[k²]·E[1²] = K(v₀,v₀), so K ≥ 1; E[k] = 1 ≠ 0 forces k ≠ 0. All directions recomputed and correct. Accepted.

Lemma 2(iii): K(v₀,v₀) = ‖k‖² = E[k²] by definition; finite by boundedness; E|k| ≤ K^{1/2} by Cauchy–Schwarz against 1. Accepted. (Structural note — trace of (i) equals (ii) — checked: tr E[k vvᵀ] = E[k‖v‖²] = E[k], tr(v₀v₀ᵀ) = 1. Correct, non-load-bearing.)

Lemma 3, identity (2): for v ∈ supp μ, k_v = Σ_j ev_v(f_j) f_j = Σ_j q_j(v) f_j (representatives evaluate ev_v by Lemma 1(b)); Parseval gives K(v,v) = Σ_j q_j(v)² = g(v). Accepted.

Lemma 3, identity (3): ∫ g dμ = Σ_j ∫ q_j² dμ = Σ_j ‖f_j‖²_{L²(μ)} = d (each ∫q_j²dμ = ‖[q_j]‖² = 1 for any representative, since representatives agree μ-a.e.); g bounded polynomial on the sphere so the interchange of finite sum and integral is trivial; (P1) makes ∫K dμ well defined. Recomputed: ∫K(v,v)dμ = d, correct. Accepted.

Lemma 3, existence: if μ({g ≤ d}) = 0 then h = g − d > 0 μ-a.e. with ∫h dμ = 0; h·1_{h>0} ≥ 0 with zero integral vanishes a.e., contradicting h > 0 a.e. under a probability measure. So μ(A) > 0; with μ(supp μ) = 1, μ(A ∩ supp μ) > 0 hence nonempty; any v₀ there has K(v₀,v₀) = g(v₀) ≤ d ≤ n(n+1)/2. Accepted.

Lemma 4: φ(t) = t log t ≥ −1/e on t ≥ 0 (minimum at t = 1/e, value −1/e — recomputed); φ(t) ≤ t² (t ≥ 1: log t ≤ t; t < 1: φ ≤ 0 ≤ t²) — both branches verified; hence φ(|r|) sandwiched between −1/e and r², both integrable, so entropy finite. dν = |r|dμ is a probability measure (E_μ|r| = 1); ν({r = 0}) = ∫_{r=0}|r|dμ = 0, so log|r| is ν-a.e. finite and E_ν[log|r|] = E_μ[|r|log|r|] with the 0·log 0 = 0 convention matching the ν-null set; E_ν[|r|] = E_μ[r²] < ∞; Jensen for concave log gives E_ν[log|r|] ≤ log E_μ[r²]. All recomputed. Accepted. (Sharpness note: equality in Jensen iff |r| ν-a.e. constant, i.e. |r| ∈ {0,c} μ-a.e.; then 1 = c·μ({|r|=c}) and entropy = log c = log(1/μ({|r|=c})) — recomputed, correct, non-load-bearing.)

Theorem, normalisation: 1 ≤ E|k| ≤ K^{1/2} gives c = 1/E|k| ∈ [K^{-1/2}, 1] ⊆ [(n(n+1)/2)^{-1/2}, 1] using K ≤ d ≤ n(n+1)/2 from Lemma 3. Both interval endpoints and both inclusions recomputed; directions correct. Accepted.

Theorem, admissibility: r = c·k is a quadratic form times a constant, bounded Borel, μ-integrable; E_μ|r| = c·E_μ|k| = 1. Accepted.

Theorem, rank-one part: E_μ[r vvᵀ] = c·v₀v₀ᵀ = L by Lemma 2(i) and linearity; c > 0 and ‖v₀‖₂ = 1 give L rank one, nonzero, PSD; ‖L‖_F = c·‖v₀v₀ᵀ‖_F = c·‖v₀‖₂² = c — recomputed. Error 0 ≤ ε‖L‖_F for every ε > 0 since ‖L‖_F = c > 0. Accepted.

Theorem, entropy: Lemma 4 applies (r ∈ L²(μ), E|r| = 1): entropy ≤ log E[r²] = log(c²K) = log(K/(E|k|)²) ≤ log K ≤ log(n(n+1)/2), using E|k| ≥ 1 and K ≤ d. Each equality/inequality in the chain recomputed; directions correct; the argument of every log is ≥ 1 (c²K = K/(E|k|)² ≥ 1 by Cauchy–Schwarz), so no sign issue. Accepted.

Corollary (the Contract): n = 1: log(1·2/2) = log 1 = 0 ≤ (2/(eδ))·1^δ — correct. n ≥ 2: n(n+1)/2 ≤ n² ⟺ n+1 ≤ 2n ⟺ n ≥ 1 — correct; log(n²) = 2 log n. Calculus claim recomputed: d/dx[(log x)x^{-δ}] = x^{-δ-1}(1 − δ log x), unique critical point x = e^{1/δ}, second-derivative/sign check confirms maximum, value (1/δ)/e^{δ·(1/δ)} = 1/(eδ) — the constant 1/(eδ) and the maximiser e^{1/δ} are both correct. Hence log n ≤ (1/(eδ))n^δ and 2 log n ≤ (2/(eδ))n^δ. Final constant C(ε,δ) = 2/(eδ), independent of ε — consistent with Contract convention 1. Accepted.

Remark A (non-load-bearing, recomputed anyway): ‖M − tuwᵀ‖_F² = ‖M‖_F² − 2t·uᵀMw + t² (cross term ⟨M, uwᵀ⟩_F = uᵀMw — recomputed); the requirement ≤ ε²t² rearranges to (1−ε²)t² − 2(uᵀMw)t + ‖M‖_F² ≤ 0 — recomputed; larger uᵀMw lowers the quadratic for t > 0, max over unit u,w is s₁(M) = |λ₁| for symmetric M — correct; real root iff s₁² ≥ (1−ε²)‖M‖_F², i.e. λ₁² ≥ (1−ε²)(λ₁² + Σ_{i≥2}λᵢ²) ⟺ ε²λ₁² ≥ (1−ε²)Σ_{i≥2}λᵢ² ⟺ Σ_{i≥2}λᵢ² ≤ (ε²/(1−ε²))λ₁² — algebra recomputed, matches the displayed inequality exactly; root product ‖M‖_F²/(1−ε²) > 0 and root sum 2s₁/(1−ε²) > 0 (s₁ > 0 since M ≠ 0) so both roots positive — recomputed. M = 0 case: ‖L‖_F > ε‖L‖_F for ε < 1 — correct. Accepted.

Corollary B: dimension count of G = {X ↦ α + ⟨A,X⟩}: spanned by the constant and the n² coordinate functionals, so dim ≤ n² + 1 — recomputed, correct. X = {rank 1, ‖·‖_F = 1} is the continuous image of S^{n-1} × S^{n-1}, hence compact, second countable as a metric subspace — the two properties Lemma 1(b) needs hold; boundedness |α + ⟨A,X⟩| ≤ |α| + ‖A‖_F on X gives Lemma 1(a); G contains 1 (α=1, A=0) and each X_ab (α=0, A = e_a e_bᵀ) — these are the only two membership facts Lemmas 2–3 used, as the artifact states. Resulting bounds: K(X₀,X₀) ≤ d ≤ n²+1, c = 1/E|k| ∈ [(n²+1)^{-1/2}, 1] ⊆ (0,1], entropy ≤ log(n²+1); cX₀ nonzero rank one since ‖X₀‖_F = 1. All recomputed. Accepted.

Remark C(i), sphere branch (quantitative claims recomputed): if k ≥ 0 μ-a.e. then E|k| = E[k] = 1, c = 1, r = k, cost ≤ log K ≤ log(n(n+1)/2) = O(log n) — correct. Derivation of μ({±v₀}) = 1/K(v₀,v₀): dμ′ = k dμ probability (Lemma 2(ii)); E_{μ′}[vvᵀ] = v₀v₀ᵀ (Lemma 2(i)); for unit w ⊥ v₀, E_{μ′}⟨v,w⟩² = wᵀv₀v₀ᵀw = 0 so ⟨v,w⟩ = 0 μ′-a.s.; finite intersection over an orthonormal basis of v₀^⊥ plus ‖v‖₂ = 1 forces v ∈ {±v₀} μ′-a.s. — correct. k(v₀) = ev_{v₀}(k) = K(v₀,v₀) (Lemma 1(c)); k(−v₀) = k(v₀) since the quadratic-form representative is even; the case split on μ({−v₀}) > 0 (then −v₀ is an atom, hence in supp μ, so Lemma 1(b) applies) vs = 0 (term drops) is handled correctly. Hence 1 = μ′({±v₀}) = K(v₀,v₀)·μ({±v₀}), so μ({±v₀}) = 1/K(v₀,v₀) ≥ 1/d ≥ 2/(n(n+1)) — the lower bound 2/(n(n+1)) recomputed from d ≤ n(n+1)/2, correct. Conditioning reweighting r′ = 1_{{±v₀}}/μ({±v₀}): E_μ[r′vvᵀ] = v₀v₀ᵀ (both atoms map to v₀v₀ᵀ), E_μ|r′| = 1, cost log(1/μ({±v₀})) = log K(v₀,v₀) ≤ log(n(n+1)/2) — recomputed. Accepted.

Remark C(i), matrix branch: k ≥ 0 gives c = 1, r = k, cost ≤ log(n²+1); E_{μ′}⟨X₀,X⟩ = ‖X₀‖_F² = 1 while ⟨X₀,X⟩ ≤ 1 on the domain (Cauchy–Schwarz, unit Frobenius norms); nonnegative μ′-mean-zero function 1 − ⟨X₀,X⟩ vanishes μ′-a.s.; equality in Cauchy–Schwarz between unit-norm matrices forces X = X₀ μ′-a.s., so μ′({X₀}) = 1; then 1 = K(X₀,X₀)·μ({X₀}) gives μ({X₀}) = 1/K(X₀,X₀) ≥ 1/(n²+1) — the lower bound recomputed from d ≤ n²+1, correct (and μ({X₀}) > 0 is forced by the identity itself). Conditioning r′ = 1_{{X₀}}/μ({X₀}) has cost log(1/μ({X₀})) = log K(X₀,X₀) ≤ log(n²+1) — recomputed. Accepted.

Remark C(ii),(iii): scope disclaimers only — no log-rank claim, no pseudo-distribution claim, unnormalised domain of Theorem 2.3 explicitly not addressed. Consistent with cards Q1–Q9; the "deficient ⇒ nonnegative" gloss is exactly what card Q9 supports. Accepted.

DEPENDENCIES: all external mathematics (finite-dimensional Riesz, Cauchy–Schwarz, Jensen, ‖Q‖_op ≤ ‖Q‖_F, full support of second-countable Borel measures, the calculus maximum) is restated and elementary; every verbatim source quotation matches card S1 (Q1–Q9) word for word; Question 8.1 as quoted matches the Contract statement with the Contract's declared quantifier convention. No citation defect, nothing unverifiable.

NUMERICAL CHECK, recomputed entirely from scratch:
- Function space: q_Q values at the four atoms are (Q₁₁, Q₂₂, (Q₁₁+Q₂₂)/2 + Q₁₂, (Q₁₁+Q₂₂)/2 − Q₁₂), so x₃ + x₄ = x₁ + x₂ always, and conversely any such x is attained (Q₁₁ = x₁, Q₂₂ = x₂, Q₁₂ = (x₃−x₄)/2). F_μ = {x ∈ R⁴ : x₁+x₂ = x₃+x₄}, d = 3 — both correct.
- Kernel: k = (3,−1,1,1) lies in F_μ (3 + (−1) = 2 = 1 + 1) and reproduces: ⟨k,f⟩ = ¼(3f₁ − f₂ + f₃ + f₄) = ¼(3f₁ − f₂ + f₁ + f₂) = f₁ for all f ∈ F_μ; uniqueness of the Riesz representer confirms it. Correct.
- E_μ[k] = (3 − 1 + 1 + 1)/4 = 1 ✓. K(v₀,v₀) = (9+1+1+1)/4 = 3 = d ✓.
- Matrix identity: 3v₁v₁ᵀ − v₂v₂ᵀ + v₃v₃ᵀ + v₄v₄ᵀ = [[3,0],[0,−1]] + ½[[1,1],[1,1]] + ½[[1,−1],[−1,1]] = [[3,0],[0,−1]] + [[1,0],[0,1]] = [[4,0],[0,0]]; divided by 4 gives [[1,0],[0,0]] = v₁v₁ᵀ ✓ exactly rank one.
- Normalisation: E_μ|k| = (3+1+1+1)/4 = 3/2 ✓; c = 2/3 ✓; r = (2, −2/3, 2/3, 2/3) ✓; E_μ|r| = (2 + 3·(2/3))/4 = 1 ✓.
- Entropy chain: E[|r|log|r|] = ¼(2 log 2 + 2 log(2/3)) = ½ log(4/3) = 0.143841… — the stated 0.1438 is correct. E[r²] = ¼(4 + 3·4/9) = 4/3 (= c²K = (4/9)·3 ✓); log(4/3) = 0.287682… — the stated 0.2877 is correct. log 3 = 1.098612… — the stated 1.0986 is correct. Chain 0.1438 ≤ 0.2877 ≤ 1.0986 holds with the claimed directions. r is genuinely signed (entry −2/3) ✓.
- Every number in the artifact was verifiable from the artifact's own contents; no orphaned numerical claim exists.

Independent plausibility probe (verifier's own, not required by the artifact): for μ uniform on S^{n-1}, the construction yields k(v) = −n/2 + (n(n+2)/2)⟨v,v₀⟩², which satisfies E[k] = 1, E[k vvᵀ] = v₀v₀ᵀ, and E[k²] = n(n+1)/2 = d exactly — confirming the mechanism on a natural instance and that k is genuinely signed there, consistent with the Contract's "Known boundary" for nonnegative r.

### SOURCE REQUEST ###
none
