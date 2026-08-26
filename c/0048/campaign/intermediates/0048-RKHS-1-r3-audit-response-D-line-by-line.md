MODEL: fable

### VERDICT ###
STATUS: CLEAN
The artifact proves a strictly stronger statement than the Contract (exact rank-one representation, Frobenius error 0, entropy cost log(n(n+1)/2) ≤ (2/(eδ))·n^δ with C(ε,δ) = 2/(eδ) independent of n, μ and ε), and every algebraic step, inequality, normalisation constant, dimension count and numerical claim recomputes correctly; the only findings are two cosmetic, non-blocking notation items.

### FINDINGS ###
| quoted location | class A-E | explanation |
|---|---|---|
| "So `r` is admissible for Definition `def:signed`." (Proof of the Theorem) and "Conjecture `conj:main` holds" (Corollary) | C | Dangling internal labels: `def:signed` and `conj:main` are not defined anywhere in the artifact. They unambiguously denote the Contract's Definition (signed reweighting) and the Contract's Statement, and the admissibility conditions (`E_μ|r| = 1`, Borel, μ-integrable) are explicitly verified in the text. Cosmetic; a competent reader fills this without effort; does not force DEFECTS. |
| "the space of quadratic forms replaced by the affine space `G := {X ↦ α + ⟨A,X⟩ : α ∈ R, A ∈ R^{n×n}}`" (Corollary B) | C | Terminology: `G` is a *linear* space of affine functions, not an affine space. Everything used about it (linearity, dimension ≤ n²+1, contains constants and coordinates) is correct as computed. Cosmetic; non-blocking. |

No class A, B, D or E defect found. Every number stated in the artifact is checkable from the artifact's own contents; none is unverifiable.

### STEP LOG ###
STEP 0 (completeness): line "### END OF ARTIFACT [T-1] ###" present; no mid-sentence or mid-proof break. Proceed.

DRIFT CHECK (class A, first): What the artifact actually proves — for every n ≥ 1 and every Borel probability measure μ on S^{n-1} there exist v_0 ∈ supp μ, c ∈ [(n(n+1)/2)^{-1/2}, 1], and a bounded Borel signed reweighting r (E_μ|r| = 1) with E_μ[r vv^T] = c·v_0v_0^T exactly and E_μ[|r| log|r|] ≤ log(n(n+1)/2); the Corollary then converts log(n(n+1)/2) ≤ (2/(eδ))·n^δ. Diff against Contract: Contract asks ∀ε,δ>0 ∃C(ε,δ)<∞ ∀n ∀μ ∃r (signed reweighting, entropy cost ≤ C·n^δ) ∃L nonzero rank one with ‖E[r vv^T] − L‖_F ≤ ε‖L‖_F. The artifact's r satisfies exactly the Contract's Definition (E|r| = 1, E[|r|log|r|] ≤ K, Borel, bounded hence μ-integrable; no extra regularity is *assumed*, only established); L = c·v_0v_0^T is nonzero rank one (c > 0, ‖v_0‖ = 1); error 0 ≤ ε‖L‖_F for every ε > 0; C = 2/(eδ) is finite, independent of n and μ (dependence on ε is permitted by Contract convention 1 and not needed). Quantifier order is respected (C fixed before n, μ). Strictly stronger conclusion; no drift. ACCEPTED.

Lemma 1, (P1): complement of supp μ is the union of all open null sets; second countability of S^{n-1} reduces it to a countable union; μ(supp μ) = 1. ACCEPTED.
Lemma 1(a): Q ↦ q_Q linear onto F_μ, so d ≤ dim Sym_n = n(n+1)/2; |v^TQv| ≤ ‖Q‖_op‖v‖² = ‖Q‖_op ≤ ‖Q‖_F on the sphere; L^∞(μ) ⊆ L²(μ) for probability μ. ACCEPTED.
Lemma 1(b): h = q_{Q−Q'} continuous, null; if h(v_0) ≠ 0 at a support point, U = {|h| > |h(v_0)|/2} is open, contains v_0, so μ(U) > 0, contradicting U ⊆ {h ≠ 0} null. Well-definedness and linearity of ev_v on classes via quadratic-form representatives follow. ACCEPTED.
Lemma 1(c): F_μ finite-dimensional Hilbert; every linear functional bounded; Riesz representer k_v unique; k_v = Σ_j ev_v(f_j)f_j for an ONB; K(v,v) = ev_v(k_v) by taking f = k_v. ACCEPTED.
Lemma 1(d): q_I(v) = ‖v‖² = 1 on the sphere; q_{E_{ab}}(v) = v_a v_b with E_{ab} = (e_ae_b^T + e_be_a^T)/2 symmetric — recomputed: v^TE_{ab}v = (v_av_b + v_bv_a)/2 = v_av_b. ACCEPTED.

Lemma 2, integrability preamble: k bounded (Lemma 1(a)), |v_av_b| ≤ 1 on the sphere. ACCEPTED.
Lemma 2(i): E_μ[k v_av_b] = ⟨k, g_{ab}⟩ = ev_{v_0}(g_{ab}) = (v_0)_a(v_0)_b for each (a,b); matrices agree entrywise. ACCEPTED.
Lemma 2(ii): E_μ[k] = ⟨k,[1]⟩ = ev_{v_0}([1]) = 1; E|k| ≥ |Ek| = 1; Cauchy–Schwarz E|k| ≤ (E k²)^{1/2} gives K(v_0,v_0) ≥ (E|k|)² ≥ 1; Ek = 1 ≠ 0 forces k ≠ 0. Inequality directions all correct. ACCEPTED.
Lemma 2(iii): K = ‖k‖² = E[k²]; E|k| ≤ K^{1/2} by Cauchy–Schwarz against 1; finite by boundedness. ACCEPTED.
Structural note (trace): tr E[k vv^T] = E[k‖v‖²] = E[k], tr(v_0v_0^T) = 1 — recomputed, consistent (not load-bearing). ACCEPTED.

Lemma 3, identity (2): for v ∈ supp μ, k_v = Σ_j ev_v(f_j)f_j = Σ_j q_j(v)f_j (Lemma 1(b) makes ev_v(f_j) = q_j(v) representative-independent on supp μ); Parseval gives K(v,v) = Σ_j q_j(v)² = g(v). ACCEPTED.
Lemma 3, identity (3): ∫g dμ = Σ_j ∫q_j² dμ = Σ_j‖f_j‖² = d (each ONB element has norm 1; finite sum, no interchange issue); g polynomial, Borel; equals K(v,v) on supp μ which has full measure by (P1), so ∫K dμ is well defined and equals d. ACCEPTED.
Lemma 3, cheap point: if μ({g ≤ d}) = 0 then h = g − d > 0 μ-a.e. with ∫h dμ = 0; a μ-a.e.-nonnegative function with zero integral is 0 a.e., contradicting h > 0 a.e. under a probability measure; so μ(A) > 0, A ∩ supp μ ≠ ∅ by (P1), and any v_0 there has K(v_0,v_0) = g(v_0) ≤ d ≤ n(n+1)/2. ACCEPTED.

Lemma 4, finiteness: φ(t) = t log t ≥ −1/e on [0,∞) (min at t = 1/e, value −1/e — recomputed) and φ(t) ≤ t² (t ≥ 1: log t ≤ t; t < 1: φ ≤ 0 ≤ t²) — both verified; with r ∈ L²(μ), φ(|r|) ∈ L¹(μ), entropy finite. ACCEPTED.
Lemma 4, Jensen: dν = |r|dμ is a probability measure (E_μ|r| = 1); ν({r = 0}) = 0 so log|r| is ν-a.e. finite; E_ν[log|r|] = E_μ[|r|log|r|] under the 0log0 convention; E_ν[|r|] = E_μ[r²] < ∞; Jensen for concave log gives E_ν[log|r|] ≤ log E_ν[|r|] = log E_μ[r²]. Direction correct (concave, ≤). ACCEPTED.
Lemma 4 sharpness note: equality iff |r| constant ν-a.e., i.e. |r| ∈ {0,c} μ-a.e.; then bound reads log(1/μ({|r| = c})) — recomputed: c·μ({|r|=c}) = 1 and entropy = c log c·μ = log c. Consistent (not load-bearing). ACCEPTED.

Theorem, constant c: c = 1/E_μ|k| with 1 ≤ E|k| ≤ K^{1/2} ≤ (n(n+1)/2)^{1/2} gives c ∈ [K^{-1/2},1] ⊆ [(n(n+1)/2)^{-1/2},1]. Both interval endpoints and inclusions recomputed. ACCEPTED.
Theorem, admissibility: r = c·k with quadratic-form representative q_{cQ_k}; bounded Borel, μ-integrable; E|r| = cE|k| = 1. ACCEPTED.
Theorem, exactness: E[r vv^T] = c·v_0v_0^T = L by Lemma 2(i) and linearity; rank one, nonzero, PSD; ‖L‖_F = c·‖v_0v_0^T‖_F = c·‖v_0‖² = c > 0; error 0 ≤ ε‖L‖_F for every ε > 0. ACCEPTED.
Theorem, entropy chain: E[r²] = c²K; log(c²K) = log(K/(E|k|)²) ≤ log K (since E|k| ≥ 1, log(E|k|)² ≥ 0 — direction correct) ≤ log(n(n+1)/2) by Lemma 3. ACCEPTED.

Corollary, n = 1: n(n+1)/2 = 1, log 1 = 0 ≤ (2/(eδ))·1^δ. Recomputed. ACCEPTED.
Corollary, n ≥ 2: n(n+1)/2 ≤ n² ⟺ n+1 ≤ 2n ⟺ n ≥ 1 — true for all n ≥ 1, a fortiori n ≥ 2 (checked n = 2: 3 ≤ 4); hence log(n(n+1)/2) ≤ 2 log n. ACCEPTED.
Corollary, calculus claim: f(x) = (log x)/x^δ, f'(x) = x^{−δ−1}(1 − δ log x), unique critical point x = e^{1/δ}, f(e^{1/δ}) = (1/δ)/e = 1/(eδ); f → −∞ as x → 0+, f → 0 as x → ∞, so it is the global max on (0,∞). Recomputed independently; the stated maximiser and maximum are both correct. Hence log n ≤ (1/(eδ))n^δ and 2 log n ≤ (2/(eδ))n^δ; C(ε,δ) = 2/(eδ), the constant in the final asymptotic comparison, is correct. ACCEPTED.

Remark A (not load-bearing), M = 0 bullet: ‖0 − L‖_F = ‖L‖_F > ε‖L‖_F for L ≠ 0 and ε ∈ (0,1). ACCEPTED.
Remark A, expansion: ‖M − tuw^T‖_F² = ‖M‖_F² − 2t·u^TMw + t² (recomputed via ⟨M, uw^T⟩ = u^TMw, ‖uw^T‖_F = 1); requirement ⟺ (1−ε²)t² − 2(u^TMw)t + ‖M‖_F² ≤ 0. ACCEPTED.
Remark A, optimisation: for fixed t > 0 the LHS is decreasing in u^TMw, so maximise it; max over unit u,w is s_1(M) = |λ_1| for symmetric M with the stated eigenvalue ordering. ACCEPTED.
Remark A, discriminant: with leading coefficient 1−ε² > 0, real root iff s_1² ≥ (1−ε²)‖M‖_F² = (1−ε²)Σλ_i²; rearranged: ε²λ_1² ≥ (1−ε²)Σ_{i≥2}λ_i² ⟺ Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1². Recomputed; matches. Root positivity for M ≠ 0: product = ‖M‖_F²/(1−ε²) > 0, sum = 2s_1/(1−ε²) > 0 (s_1 > 0 since M ≠ 0) — both recomputed from Vieta; an admissible t > 0 exists exactly then (any t between the roots, or the double root). The "iff" holds in both directions (if s_1² < (1−ε²)‖M‖² the quadratic is > 0 for all t and all u,w since u^TMw ≤ s_1). ACCEPTED.

Corollary B: dimension count — G = {X ↦ α + ⟨A,X⟩} has dim ≤ 1 + n² = n²+1 (recomputed); G contains the constant 1 (α=1, A=0) and each coordinate X_{ab} (α=0, A = e_ae_b^T); elements continuous (Lemma 1(b) transfers), bounded on X since |α + ⟨A,X⟩| ≤ |α| + ‖A‖_F on ‖X‖_F = 1 (Lemma 1(a) transfers); R^{n×n} second countable so (P1) transfers; Lemma 3 analogue gives X_0 ∈ supp μ with K ≤ dim ≤ n²+1; Lemma 2 analogues give E[k] = 1 and E[k(X)X] = X_0 entrywise; c = 1/E|k| ∈ (0,1] since E|k| ≥ 1; entropy ≤ log(c²K) ≤ log K ≤ log(n²+1). All dimension-dependent bounds recomputed; correct. ACCEPTED (modulo the cosmetic "affine space" wording, see FINDINGS).

Remark C(i)/(iii): reads the card quotations correctly — Q5's tightness is about deficient (hence, by Q9, nonnegative normalised) reweightings; Q1's "No" is for nonnegative r; the artifact claims no log-rank or pseudo-distribution consequence (Q4 flatness not supplied, honest supp μ used throughout). Checked against card S1 hypothesis by hypothesis; no misuse. ACCEPTED.
Remark C, "equivalently" derivation: k ≥ 0 μ-a.e. makes dμ' = k dμ a probability measure (Lemma 2(ii)); Lemma 2(i) gives E_{μ'}[vv^T] = v_0v_0^T; for unit w ⊥ v_0, E_{μ'}⟨v,w⟩² = w^Tv_0v_0^Tw = 0 so ⟨v,w⟩ = 0 μ'-a.s.; over an orthonormal basis of v_0^⊥ plus ‖v‖ = 1 this forces μ'({±v_0}) = 1; quadratic forms are even so k(−v_0) = k(v_0) = ev_{v_0}(k) = K(v_0,v_0) (Lemma 1(c)); hence 1 = ∫_{{±v_0}}k dμ = K(v_0,v_0)·μ({±v_0}), i.e. μ({±v_0}) = 1/K(v_0,v_0). Two-point-set lower bound recomputed: K ≤ n(n+1)/2 gives μ({±v_0}) ≥ 2/(n(n+1)) — correct. Conditioning entropy of r' = 1_{{±v_0}}/μ({±v_0}): E|r'| = 1 and E[|r'|log|r'|] = log(1/μ({±v_0})) = log K(v_0,v_0) ≤ log(n(n+1)/2) — recomputed. ACCEPTED.

NUMERICAL CHECK — full independent recomputation, n = 2, μ uniform (mass 1/4 each) on v_1=(1,0), v_2=(0,1), v_3=(1,1)/√2, v_4=(1,−1)/√2:
- F_μ: with Q = [[a,b],[b,c]], the value vector is (a, c, (a+c)/2 + b, (a+c)/2 − b), so x_1+x_2 = x_3+x_4 always, and conversely a = x_1, c = x_2, b = (x_3−x_4)/2 realises any such x. F_μ = {x : x_1+x_2 = x_3+x_4}, d = 3. MATCHES.
- Kernel: need (1/4)k·f = f_1 for all f ∈ F_μ, k ∈ F_μ, so k = 4·Proj_{F_μ}(e_1) with F_μ^⊥ = span u, u = (1,1,−1,−1); Proj e_1 = e_1 − (1/4)u = (3/4, −1/4, 1/4, 1/4); k = (3,−1,1,1). MATCHES.
- E_μ[k] = (3−1+1+1)/4 = 1. MATCHES. K = ‖k‖²_{L²(μ)} = (9+1+1+1)/4 = 3 = d. MATCHES.
- E_μ[k vv^T] = ¼(3[[1,0],[0,0]] − [[0,0],[0,1]] + ½[[1,1],[1,1]] + ½[[1,−1],[−1,1]]) = ¼([[3,0],[0,0]] − [[0,0],[0,1]] + [[1,0],[0,1]]) = ¼[[4,0],[0,0]] = v_1v_1^T. Exactly rank one. MATCHES.
- E_μ|k| = (3+1+1+1)/4 = 3/2, c = 2/3, r = (2, −2/3, 2/3, 2/3), E_μ|r| = (2 + 3·(2/3))/4 = 1. ALL MATCH. r takes the value −2/3: genuinely signed. MATCHES.
- Entropy = ¼(2 log 2 + 3·(2/3)log(2/3)) = ½(log 2 + log(2/3)) = ½log(4/3) = 0.143841 — stated 0.1438 CORRECT.
- E[r²] = ¼(4 + 3·(4/9)) = 4/3 (= c²K = (4/9)·3, cross-checked); log(4/3) = 0.287682 — stated 0.2877 CORRECT.
- log 3 = 1.098612 — stated 1.0986 CORRECT. Chain 0.1438 ≤ 0.2877 ≤ 1.0986 holds (strictly, consistent with the Lemma 4 sharpness note since |r| takes two nonzero values). ALL THREE NUMBERS IN THE ENTROPY CHAIN VERIFIED FROM SCRATCH.

Source quotations vs card S1: the eight verbatim quotes in DEPENDENCIES (Question 8.1 + follow-up; Theorem 2.3; Definition 2.2; §2.2 flatness; p.6 tightness; footnotes 7 and 8; §2.3 normalisation) match card items Q1–Q9 word for word; the artifact's use of each is as glossed in Remark C and Corollary B; no citation is load-bearing for the Theorem itself (all external mathematics is elementary and restated, and I verified each restatement above). No (D), no (E).

Unverifiable-number sweep (per assignment): every numeral in the artifact — 2/(eδ), n(n+1)/2, n²+1, n², 2 log n, 1/(eδ), e^{1/δ}, (n(n+1)/2)^{−1/2}, 2/(n(n+1)), ε²/(1−ε²), d = 3, k = (3,−1,1,1), 1, 3, 3/2, 2/3, (2,−2/3,2/3,2/3), 0.1438, 0.2877, 1.0986, page numbers of quotes — was recomputed or matched against the supplied card. None is unverifiable from the artifact's own contents plus the card.

### SOURCE REQUEST ###
none
