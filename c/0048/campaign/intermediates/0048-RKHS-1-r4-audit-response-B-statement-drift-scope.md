MODEL: opus

### VERDICT ###

STATUS: DEFECTS

The Theorem and Corollary prove exactly the Contract's statement (indeed a
strictly stronger one) with no class-A drift and no broken step that I could
find, but Remark C(i) contains one class-D misdescription of the cited
Theorem 2.3 / Q5 domain — it asserts that Corollary B's unit-Frobenius domain
"is the one" Theorem 2.3 and the tightness claim are stated over, which
contradicts card Q2 ("any distribution over rank one `n × n` matrices") and is
retracted by the artifact itself three sentences later — so a limiting claim is
asserted over a wider domain than the one on which it is proved.

### STEP 0 — COMPLETENESS GATE ###

Not truncated. The artifact carries its terminal line `### END OF ARTIFACT
[W-1] ###`; the last complete unit before it is the `NUMERICAL CHECK` section,
and nothing stops mid-sentence, mid-equation or mid-proof. Every lemma, the
Theorem, the Corollary, Remark A, Corollary B, Remark C, DEPENDENCIES and the
numerical check are closed (∎ or full stop). Verification proceeds.

### WHAT THE ARTIFACT ACTUALLY PROVES (my words, before any diff) ###

**S_art (Theorem).** Let `n ≥ 1` and let `μ` be any Borel probability measure on
`S^{n-1}`. Let `F_μ ⊆ L²(μ)` be the (finite-dimensional) space of `μ`-classes of
real quadratic forms `v ↦ v^TQv`, `Q ∈ Sym_n`, and `d = dim F_μ ≤ n(n+1)/2`.
Then there is a point `v_0 ∈ supp μ` whose reproducing kernel `k = k_{v_0} ∈ F_μ`
for evaluation at `v_0` satisfies `K(v_0,v_0) := ‖k‖²_{L²(μ)} ≤ d`, and, setting
`c := 1/E_μ|k| ∈ [(n(n+1)/2)^{-1/2}, 1]` and `r := c·k` (represented by a single
quadratic form, hence continuous and bounded on `S^{n-1}`):

* `r` is Borel, `μ`-integrable, `E_μ|r| = 1` **exactly**;
* `E_μ[|r| log|r|] ≤ log E_μ[r²] = log(c²K(v_0,v_0)) ≤ log K(v_0,v_0) ≤
  log(n(n+1)/2)`;
* `E_{v∼μ}[r(v)vv^T] = c·v_0v_0^T` **exactly** (zero error), and
  `L := c·v_0v_0^T` is rank exactly one, nonzero, PSD, with `‖L‖_F = c > 0`.

**S_cor.** Since `log(n(n+1)/2) ≤ 2 log n ≤ (2/(eδ))·n^δ` for every `n ≥ 1` and
`δ > 0` (with `n = 1` giving `0`), the Contract's statement holds with
`C(ε,δ) := 2/(eδ)`, a constant independent of `n`, `μ` **and** `ε`, and with the
Frobenius error identically `0`.

Auxiliary claims proved: Remark A (an exact spectral characterisation of when a
symmetric `M` admits a nonzero rank one `L` with `‖M−L‖_F ≤ ε‖L‖_F`, `ε∈(0,1)`);
Corollary B (the same construction on `X = {rank-1, ‖X‖_F = 1}` with the affine
function space `G`, giving `E_μ[r(X)X] = cX_0` exactly and entropy
`≤ log(n²+1)`); Remark C's appendix (if the produced `k` is `μ`-a.e. nonnegative
then `μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))` on the sphere, resp.
`μ({X_0}) = 1/K(X_0,X_0) ≥ 1/(n²+1)` on `X`, and conditioning on that atom is a
*nonnegative* reweighting of cost `log K ≤ log(n(n+1)/2)`, resp. `log(n²+1)`).

### CLAUSE-BY-CLAUSE DIFF AGAINST THE CONTRACT ###

Contract clause → artifact, in order.

1. **"For every `ε > 0` and every `δ > 0` there exists a finite constant
   `C = C(ε,δ)`"** → artifact exhibits `C = 2/(eδ)`, finite for each `δ > 0`.
   Quantifier order is *correct and not reversed*: `C` is produced from `ε,δ`
   alone, before `n` and `μ` are seen, because the artifact's entropy bound
   `log(n(n+1)/2)` is itself uniform over all `μ` on `S^{n-1}` and the
   comparison `log(n(n+1)/2) ≤ C n^δ` is a numerical fact about `n`, `δ`. There
   is no `∀n ∃C` hidden anywhere, and no "for all sufficiently large `n`":
   `n = 1` is treated separately and `n ≥ 2` uniformly. **No drift.**
   `C` is *independent of `ε`*. Reading convention 1 permits `ε`-dependence and
   asks that it be tracked; producing an `ε`-free constant is strictly stronger
   and honours the convention. **No drift.**
2. **"for every `n ∈ N` and every Borel probability measure `μ` on `S^{n-1}`"**
   → artifact: "For every `n ≥ 1` and every Borel probability measure `μ`". No
   secret restriction to finitely supported, atomic, absolutely continuous or
   symmetric `μ`; Lemma 1(b) exists precisely to handle general Borel `μ`
   without approximation, and the artifact says so. (`n = 0` would make
   `S^{-1} = ∅` carry no probability measure, so it is vacuous either way.)
   **No drift.**
3. **"there exist a signed reweighting `r` of `μ` with entropy cost at most
   `C·n^δ` (in the sense of the Definition above)"** → each conjunct of the
   Contract's Definition is discharged: Borel measurable (a quadratic form
   restricted to the sphere is continuous), `μ`-integrable (bounded, Lemma 1(a)),
   `E_μ|r| = 1` **exactly** (not `≤ 1`, not `≈ 1`, not after rescaling), and
   `E_μ[|r| log|r|]` shown *finite* (Lemma 4's `−1/e ≤ φ`, `φ(t) ≤ t²`
   sandwich) and `≤ log(n(n+1)/2) ≤ C n^δ`. The convention `0 log 0 := 0` is
   used consistently with the `ν`-null set `{r = 0}`. Nonnegativity of `r` is
   nowhere assumed. **No drift.**
   Reading convention 2 ("no further regularity … and none may be added"): the
   artifact *assumes* no regularity of `μ` or of an ambient `r`; the continuity
   of the *produced* `r` is a property of the witness, not an added hypothesis,
   and a witness may be as regular as it likes. **No drift.**
4. **"and a nonzero rank one matrix `L ∈ R^{n×n}`"** → `L = c v_0v_0^T` with
   `c ≥ (n(n+1)/2)^{-1/2} > 0` and `‖v_0‖₂ = 1`, so `rank L = 1` exactly and
   `L ≠ 0`. The nonzero requirement is honoured *non-vacuously*: the lower bound
   on `c` is explicit and `n`-quantitative, so the artifact never slides into
   `L = 0`, never reads "rank one" as "rank at most one", and never lets `L`
   degenerate as `n → ∞` in a way that would make `‖L‖_F = 0`. Reading
   convention 3 (`L` need not be symmetric or PSD) is respected: the artifact
   delivers a *PSD* `L`, which is a permitted special case, not a weakening.
   **No drift.**
5. **"`‖E_{v∼μ}[r(v)vv^T] − L‖_F ≤ ε‖L‖_F`"** → achieved with left side `= 0`
   and `‖L‖_F = c > 0`, for every `ε > 0` simultaneously. I checked the three
   ways this clause could be met in a degenerate or rescaled sense, and none is
   used: (i) `L` is not a rescaled surrogate — it is *literally* the matrix
   `E_μ[r vv^T]`; (ii) the inequality is not met by inflating `‖L‖_F` to swamp
   an error term (Remark A verifies independently that the relative constraint
   is scale-invariant and non-vacuous, so this loophole does not exist and is
   not used); (iii) `‖L‖_F` is not driven to `0` to make the right side
   meaningless — the left side is `0` regardless of `c`, and `c > 0` is bounded
   below. The relative accuracy is met **as stated**. **No drift.**
6. **"Known boundary" (nonnegative case tight at `δ = 1/2`)** → the artifact's
   `r` is genuinely signed in general; the numerical check exhibits
   `r = (2, −2/3, 2/3, 2/3)`, and Remark C's appendix characterises exactly when
   `r ≥ 0` can happen (`μ` puts mass `1/K(v_0,v_0)` on `{±v_0}`). No
   contradiction with the stated boundary. **No drift.**

**Conclusion of the class-A pass: I find no statement drift.** The artifact
proves the Contract and strictly more (zero error rather than `ε`-error;
`O(log n)` rather than `O(n^δ)` entropy; `C` free of `ε`). Every ambiguous term
of the Contract — "signed reweighting", "entropy cost", "nonzero rank one",
"relative accuracy" — is read in the hard direction, not the easy or vacuous
one. I pressed the quantifier order on `C(ε,δ)`, `n` and `μ` specifically and it
is correct.

### FINDINGS ###

| quoted location | class A–E | explanation |
|---|---|---|
| Remark C(i): "The same holds for Corollary B, whose domain — not the sphere — is the one Theorem 2.3 and the tightness claim of Q5 are stated over" | **D** (also reads as an A-type scope overreach in a limiting claim) | Card Q2 states Theorem 2.3 for "any distribution over rank one `n × n` matrices" — the *unnormalised* domain — and Q5's tightness is asserted of Theorem 2.3 "as stated", hence over that same unnormalised domain. Corollary B's domain is `X = {rank X = 1, ‖X‖_F = 1}`, a proper subset (the Q8 slice, which is a *later* restriction of attention in §2.3, not a hypothesis of Theorem 2.3). So the definite identification "is the one … are stated over" misdescribes the hypothesis of the cited theorem. The artifact contradicts itself in the same paragraph: "What is *not* addressed is the unnormalised domain of Theorem 2.3 (Q2) … Corollary B treats only the unit-Frobenius slice named at Q8". Effect: the defensive claim of no-conflict is *asserted* over the domain of Q2/Q5 while it is *proved* only on the Q8 slice — exactly the "limiting claim over a wider domain than proved" failure. Non-load-bearing for the Theorem, the Corollary or the Contract; it damages only the scope remark. (The substantive consistency argument for the Q8 slice itself — atom, Cauchy–Schwarz equality, `μ({X_0}) = 1/K(X_0,X_0)` — I verified and accept.) |
| DEPENDENCIES, Question 8.1 bullet: "**This matches Conjecture `conj:main` of the Contract with no additional hypothesis; the review is faithful.**" | C (non-forcing) | Over-strong as written. The Contract *does* add to Q1's literal text: Borel measurability and `μ`-integrability of `r` (reading convention 2 — Q1 says only "a … function `r : S^{n−1} → R`"), and it pins the `O(n^δ)` constant to be independent of `n` and `μ` (convention 1 — Q1's `O(·)` inside a statement already quantified over `μ`, hence over `n`, is otherwise ill-defined and would read vacuously). Both additions *increase* the solver's burden, so the artifact proving the Contract does imply an affirmative answer to Q1; the error is therefore in the harmless direction and does not touch soundness. But "no additional hypothesis" is not what the two documents show, and a referee should not have to reconstruct which direction the discrepancy runs. |
| Remark C(ii): "so that route is unavailable"; Remark C(i) opening: "answers Question 8.1 as literally posed (card Q1) and nothing more" | C (non-forcing) | Two loose scope phrasings, both in the *modest* direction. (a) What is proved is that Q4's dictionary is stated for *flat* distributions and the Theorem gives no flatness, i.e. Q4 does not *directly* apply; "that route is unavailable" is a stronger, unproved negative. (Incidentally the artifact understates its own obstruction: a signed `r` corresponds to no distribution `μ′` at all, so Q4 cannot even be addressed, let alone flatness.) (b) "and nothing more" sits oddly beside the GOAL's own "the Frobenius error equal to `0`" and beside Corollary B, both of which are strictly more than Q1 asks; in context "nothing more" plainly means "no further *consequences* are claimed", which is defensible, so I record this only as imprecision. Neither inflates the result; neither forces DEFECTS on its own. |
| DEPENDENCIES: "Cauchy–Schwarz in `L²(μ)`, and in the Frobenius inner product on `R^{n×n}`; used in Remark C(i). … — RESTATED." | C (routine, non-forcing) | The self-declared inventory of external mathematics is incomplete and its "RESTATED" labels are partly nominal. Not listed: the *equality case* of Cauchy–Schwarz (load-bearing in Remark C(i) to force `X = X_0` `μ′`-a.s.); the variational characterisation `max_{‖u‖=‖w‖=1} u^TMw = s_1(M)` (Remark A); "a nonnegative function with vanishing integral vanishes a.e." (Lemma 3, and twice in Remark C(i)); Parseval / expansion in an orthonormal basis (Lemma 3). All four are textbook facts a competent reader supplies without effort — this is exactly the routine gap the prompt says need not force DEFECTS, and I so judge it. |
| DEPENDENCIES header: "**Source, READ (local copy `the published PDF`, text layer extracted with `pdftotext -layout`).**" | note, no class | The artifact never identifies its source bibliographically — no authors, title, venue or arXiv identifier appears anywhere in it; "the published PDF" reads as an unfilled placeholder. Identification is possible only through the supplied card. Not an (E): every quoted passage is covered by card S1, and I independently corroborated Q2, Q5, Q8, Q9 against arXiv:1701.06321 (see SOURCE REQUEST). Recorded so that the editor can require the reference to be named. |

**Verbatim-quotation audit (character by character, artifact vs card).** Every
passage the artifact labels "verbatim" was collated against S1. **No clause is
dropped, added or altered in substance in any of the nine quotations**, including
the *sic* in Q6 ("to find a in a rank `n` Boolean matrix"), which is faithfully
preserved. Four purely typographic deviations, none affecting meaning and none
of which I count as a defect: (i) Q1, the card's space before the closing "?" is
absent in the artifact; (ii) Q2, the artifact adds a sentence-final period after
`ε‖L‖_F`, which the card lacks; (iii) Q5 and Q6, the card's double quotation
marks around "close to rank one" and "approximate" appear as single quotes;
(iv) in **Corollary B** the §2.3 passage is opened as "we will restrict our
attention…" where the card reads "**W**e will restrict our attention…", i.e. a
case change inside quotation marks presented as verbatim (the same passage is
quoted correctly, with capital W, in DEPENDENCIES). Item (iv) is the only one I
would ask the author to fix, and only for hygiene.

**Scope-claim audit against the card, hypothesis by hypothesis.** Besides the
class-D row above, each remaining external claim checks out:
* "'It can be shown that as stated, Theorem 2.3 is tight' (Q5) is about
  *deficient* reweightings, which are probability distributions and hence
  nonnegative by Definition 2.2 (Q9)" — supported: Q9 defines `k`-deficient only
  for a *probability distribution* `µ′`, and the card's own closing note says
  this is the definition the term in Q2 carries. The artifact flags Q9 as "the
  sole basis" for the gloss, which is honest. Accepted. (Q2's pseudo-expectation
  notation `Ẽ_{µ′}X` does not undermine this, since Q9 fixes `µ′` to be an
  honest distribution.)
* "'the answer to this question is No if one does not allow negative reweighting
  functions' (Q1) is an existential statement over `μ`" — correct: Q8.1 is
  universally quantified over `µ`, so its negation is existential over `µ`, and
  the artifact's universally-quantified positive result with a *signed* `r`
  cannot contradict it. Accepted, and the accompanying converse check (if the
  produced `k ≥ 0` then `µ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))`, so that `µ`
  admits a cheap *nonnegative* reweighting and is not a witness for the "No") is
  proved on exactly the domain where its hypothesis `k ≥ 0` holds. Accepted.
* Remark C(iii), "The source attaches its pseudo-distribution condition to its
  *running-time* consequence (Q1); this artifact addresses neither" — a
  defensible parse of Q1 ("and if appropriately extended to pseudo-distributions,
  improve our algorithm's running time…", the conditional clause attaching to the
  second consequence), and in any case the artifact claims neither consequence,
  so nothing rests on the parse. The accompanying inventory of `supp μ` uses
  (Lemma 1(b),(c), Lemma 2, Lemma 3, the Theorem) is accurate and complete.
  Accepted.
* Footnote-8 gloss "— moot here: our constant is independent of `ε`" — literally
  true (`C = 2/(eδ)`), and consistent with Remark C(ii)'s disclaimer of any
  log-rank consequence, so it does not smuggle in a claim about clearing the
  log-rank hurdle. Accepted.
* Corollary B's "the normalisation used in the source paper's intended
  application (§2.3: …)" — supported by Q8 ("anyway holds automatically in our
  intended application"); and `{rank 1, ‖X‖_F = 1} = {ab^T : ‖a‖₂ = ‖b‖₂ = 1}`
  is correct since `‖ab^T‖_F = ‖a‖₂‖b‖₂`. Accepted.
* "None of the source material is load-bearing for the Theorem; it is
  load-bearing only for the claim that the Theorem answers Question 8.1" —
  accurate; the Theorem's proof is self-contained. Accepted.

### STEP LOG ###

Accepted steps (one line each; I re-derived each rather than reading past it).

1. Restatement of the goal and of the Definition in the GOAL section — matches
   the Contract clause for clause (the Contract's "let `K ≥ 0`" is dropped, which
   is immaterial: the delivered bound `log(n(n+1)/2) ≥ 0`). Accepted.
2. Lemma 1(a): `Q ↦ [q_Q]` linear, so `F_μ` is a subspace and
   `d ≤ dim Sym_n = n(n+1)/2`; `|v^TQv| ≤ ‖Q‖_op ≤ ‖Q‖_F` on `S^{n-1}`;
   `L^∞(μ) ⊆ L²(μ)` for a probability measure. Accepted.
3. (P1) `μ(supp μ) = 1` via second countability, (P2) support definition.
   Accepted.
4. Lemma 1(b): `h := q_{Q−Q'}` continuous and `μ`-a.e. zero; if `h(v_0) ≠ 0` at a
   support point then the open set `{|h| > |h(v_0)|/2}` is a null superset of a
   neighbourhood of `v_0`, contradiction. The set is open *in* `S^{n-1}`, which
   is what (P2) needs. Well-definedness of `ev_v` is stated precisely — through
   quadratic-form representatives only — which is the correct and only viable
   formulation, since a class in `F_μ` also has non-quadratic representatives.
   This is the crux of handling general Borel `μ`, and it is done. Accepted.
5. Lemma 1(c): finite-dimensional Riesz representer `k_v`, `K(v,v) = ev_v(k_v)`,
   explicit `k_v = Σ_j ev_v(f_j) f_j` (checked against any orthonormal basis).
   Accepted.
6. Lemma 1(d): `q_I ≡ 1` and `q_{E_{ab}}(v) = v_av_b` on `S^{n-1}` — the whole
   mechanism. `E_{ab} = (e_ae_b^T + e_be_a^T)/2` is symmetric, as required.
   Accepted.
7. Lemma 2(i): `E_μ[k v_av_b] = ⟨k, g_{ab}⟩ = ev_{v_0}(g_{ab}) = (v_0)_a(v_0)_b`
   entrywise, hence `E_μ[k vv^T] = v_0v_0^T`; absolute convergence from
   boundedness. Accepted.
8. Lemma 2(ii): `E_μ[k] = ⟨k,[1]⟩ = 1`; `E_μ|k| ≥ 1`; `K(v_0,v_0) ≥ 1` by
   Cauchy–Schwarz; `k ≠ 0`. Accepted. (The structural note that (ii) is the
   trace of (i) is correct and is a genuine consistency check.)
9. Lemma 2(iii): `E_μ[k²] = K(v_0,v_0)`, `1 ≤ E_μ|k| ≤ K(v_0,v_0)^{1/2} < ∞`.
   Accepted.
10. Lemma 3: `K(v,v) = Σ_j q_j(v)² =: g(v)` on `supp μ`; `∫ g dμ = Σ_j ‖f_j‖² =
    d`; the choice-independence caveat and the "off the support nothing uses `g`"
    caveat are both correctly flagged. The existence argument (`μ({g ≤ d}) > 0`,
    else a strictly positive function has zero integral; then intersect with
    `supp μ`, which has full measure) is valid. `d ≥ 1` since `[1] ∈ F_μ` is
    nonzero, so the orthonormal basis is nonempty. Accepted.
11. Lemma 4: `φ(t) = t log t ≥ −1/e`, `φ(t) ≤ t²`, hence `φ(|r|) ∈ L¹(μ)` and the
    entropy is a finite real; `dν = |r|dμ` is a probability measure with
    `ν({r = 0}) = 0`; `E_ν[log|r|] = E_μ[|r|log|r|]`; `E_ν[|r|] = E_μ[r²]`;
    Jensen for concave `log` against `ν`. Accepted. (The sharpness remark —
    equality iff `|r| ∈ {0,c}` a.e. — is correct and not load-bearing.)
12. Proof of the Theorem: `c := 1/E_μ|k| ∈ [K^{-1/2},1] ⊆ [(n(n+1)/2)^{-1/2},1]`;
    `E_μ|r| = 1`; `E_μ[r vv^T] = c v_0v_0^T = L` with `‖L‖_F = c > 0`; error `0`;
    entropy `≤ log(c²K) = log(K/(E_μ|k|)²) ≤ log K ≤ log(n(n+1)/2)`. Accepted.
13. Corollary: `n = 1` gives `log 1 = 0`; `n(n+1)/2 ≤ n²` for `n ≥ 1`;
    `max_{x>0}(log x)/x^δ = 1/(eδ)` at `x = e^{1/δ}` (re-derived); hence
    `log(n(n+1)/2) ≤ 2 log n ≤ (2/(eδ))n^δ`. `C(ε,δ) = 2/(eδ)` is finite for each
    `δ > 0` and independent of `n`, `μ`, `ε`. Accepted.
14. Remark A: `L = tuw^T`, `t > 0`; `‖M−L‖_F² = ‖M‖_F² − 2t·u^TMw + t²`;
    monotone in `u^TMw`, optimum `s_1(M) = |λ_1|`; discriminant condition
    `s_1² ≥ (1−ε²)‖M‖_F²` rearranges to `Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1²`; both
    roots positive when `M ≠ 0`; `M = 0` admits no `L`. The restriction to
    `ε ∈ (0,1)` is stated, and `(1−ε²) > 0` is used only there. Accepted, and it
    does discharge the scale-invariance worry it is offered for.
15. Corollary B: `X` compact and second countable; `G` of dimension `≤ n²+1`
    contains the constant `1` and every coordinate `X ↦ X_{ab}`; elements of `G`
    are continuous and bounded on `X` (`|α + ⟨A,X⟩| ≤ |α| + ‖A‖_F`), which is all
    Lemmas 1–4 used. Hence `E_μ[rX] = cX_0` exactly, `c ∈ (0,1]`, entropy
    `≤ log(n²+1)`. Accepted. (The parenthetical explanation of why the sphere
    gets `log(n(n+1)/2)` instead of `log(n²+1)` is correct.)
16. Remark C(i) appendix, spherical case: `k ≥ 0` ⟹ `dμ′ = k dμ` is a probability
    measure with `E_{μ′}[vv^T] = v_0v_0^T` ⟹ `⟨v,w⟩ = 0` `μ′`-a.s. for each of
    the `n−1` basis vectors of `v_0^⊥` (a finite union of null sets) ⟹
    `μ′({±v_0}) = 1`; `k(v_0) = K(v_0,v_0)`, `k(−v_0) = k(v_0)` by evenness of the
    quadratic representative, with the representative-independence at `−v_0`
    correctly split into the cases `μ({−v_0}) > 0` (then `−v_0 ∈ supp μ`, so
    Lemma 1(b) applies) and `μ({−v_0}) = 0` (then the term drops) — this is
    precisely the subtle point and it is handled; hence
    `μ({±v_0}) = 1/K(v_0,v_0) ≥ 2/(n(n+1))`, and conditioning gives a nonnegative
    reweighting of cost `log K(v_0,v_0)` reaching `v_0v_0^T`. Accepted.
17. Remark C(i) appendix, `X` case: `1 − ⟨X_0,X⟩ ≥ 0` has `μ′`-mean `0`, hence
    `⟨X_0,X⟩ = 1` `μ′`-a.s., hence `X = X_0` `μ′`-a.s. by the equality case of
    Cauchy–Schwarz among unit-Frobenius matrices; `1 = K(X_0,X_0)μ({X_0})`;
    conditioning gives cost `log K(X_0,X_0) ≤ log(n²+1)`. The reason the
    spherical argument does not transfer verbatim (affine, not even; no antipodal
    fibre) is correctly identified. Accepted — **except** for the domain
    identification flagged as the class-D finding.
18. Numerical check: I reproduced it independently. `F_μ = {x : x_1+x_2 = x_3+x_4}`
    (since `x_3 + x_4 = a + c = x_1 + x_2` for `q_Q`, `Q = [[a,b],[b,c]]`),
    `d = 3`; `k = (3,−1,1,1) ∈ F_μ` reproduces evaluation at `v_1`;
    `E_μ[k] = 1`, `‖k‖² = 3`, `E_μ[k vv^T] = ¼[[4,0],[0,0]] = v_1v_1^T`;
    `E_μ|k| = 3/2`, `c = 2/3`, `r = (2,−2/3,2/3,2/3)`, `E_μ|r| = 1`,
    entropy `= ¼(2log2 + 2log(2/3)) = 0.1438`, `log E_μ[r²] = log(4/3) = 0.2877`,
    `log 3 = 1.0986`. All figures confirmed; `r` is indeed signed. Accepted.
19. Two additional stress tests of my own, since the result is strong enough to
    invite suspicion of a hidden error (recorded for the editor, not as
    verification the artifact owes): for `μ` uniform on `S^{n-1}` the kernel is
    `k(v) = (n/2)((n+2)⟨v,v_0⟩² − 1)`, and `E_μ[k vv^T] = v_0v_0^T` holds exactly
    by the fourth-moment identity `E[v_iv_jv_kv_l] = (δ_{ij}δ_{kl} + δ_{ik}δ_{jl}
    + δ_{il}δ_{jk})/(n(n+2))`, with `K(v_0,v_0) = n(n+1)/2 = d`; for `μ` uniform
    on `{±1}^n/√n` the kernel at `v_0 = 1/√n` is `k = 1 + Σ_{i<j}x_ix_j` and
    `E_μ[k vv^T] = v_0v_0^T` exactly, with `E_μ|k| = Θ(n)` so `c = Θ(1/n)` and
    entropy `O(1)`. Both are cases where the *nonnegative* problem is hard, and
    in both the cancellation is genuine. Consistent with the artifact.

Defects, in full: see the FINDINGS table. The single blocking item is the
class-D row; it is confined to one clause of Remark C(i), is contradicted by the
artifact's own later sentence, and is load-bearing for nothing but that clause.
Nothing in the Theorem, the Corollary, Remark A, Corollary B or the appendix of
Remark C depends on it, so the class-A verdict (no drift) and the mathematical
verdict (no class-B error found) stand independently of it.

### SOURCE REQUEST ###

For the class-D finding, and to let the editor adjudicate the domain question
without further guesswork, I request the following additions to card S1 (my own
external check reached arXiv:1701.06321 and corroborated the wording of Q2, Q5,
Q8 and Q9 through an HTML rendering, but I could not retrieve Section 8, so Q1
and Q7 rest on the card alone):

1. The full text of §2.2 and §2.3 of arXiv:1701.06321v2 (pp. 5–6) surrounding
   Theorem 2.3, sufficient to establish **over which domain the assertion "as
   stated, Theorem 2.3 is tight" is made** — in particular whether the tightness
   instance is a distribution over *arbitrary* rank one `n × n` matrices or over
   the unit-Frobenius slice `{ab^T : ‖a‖₂ = ‖b‖₂ = 1}` of Q8, and whether the
   §2.3 unit-norm restriction is in force at the point where tightness is
   asserted. This is exactly what the class-D clause asserts without support.
2. Whatever the paper says in support of "It can be shown that as stated,
   Theorem 2.3 is tight" (a proof, a reference, or confirmation that the paper
   leaves it as an unsupported assertion). Not load-bearing for the artifact —
   the artifact only needs the claim to concern *nonnegative* reweightings, which
   Q9 already settles — but needed to referee the no-conflict claim as stated.
3. Section 8, p. 19 of arXiv:1701.06321v2 in full, so that Q1 (Question 8.1, the
   paragraph following it, and footnote 8) can be confirmed independently of the
   card. This is the passage on which the artifact's entire claim of relevance
   rests, and it is the one passage of the card I could not reach externally.

No class-(E) item was found: every external result the artifact uses is either
restated and elementary, or quoted from card S1.
