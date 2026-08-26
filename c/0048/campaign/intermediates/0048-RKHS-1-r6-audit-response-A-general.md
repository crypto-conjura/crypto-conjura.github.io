# Blind Adversarial Referee Report — angle GENERAL
Artifact: `0048-RKHS-1-r6.md`
Contract: `c/0048/campaign/CONTRACT.md`
Source card: `c/0048/campaign/sources/S1-bks-q81-card.md`

## STEP 0 — Completeness gate
The artifact contains the required closing line `### END OF ARTIFACT [0048-RKHS-1-r6] ###`
(line 441) and continues afterward only with a REVISION LOG, which is
administrative, not mathematical content. No lemma, proof, or equation stops
mid-stream. **Not truncated.** Proceeding to full review.

## Statement actually proved, vs. the Contract (Class-A check)
Contract: ∀ε>0 ∀δ>0 ∃C(ε,δ) (indep. of n,μ) ∀n ∀μ ∃ signed r (entropy ≤
C·n^δ), ∃ nonzero rank-one L, with ‖E_μ[r vv^T]−L‖_F ≤ ε‖L‖_F.

Artifact's THEOREM constructs, for every n≥1 and every μ, a signed r and a
nonzero rank-one (in fact PSD) L with **exact** equality E_μ[r vv^T]=L
(hence trivially ‖·‖_F=0≤ε‖L‖_F for every ε>0) and entropy ≤
log(n(n+1)/2). The COROLLARY then bounds log(n(n+1)/2) ≤ (2/(eδ))n^δ for
every n≥1, giving C(ε,δ)=2/(eδ), independent even of ε. This is a strict
strengthening of the Contract's statement (ε=0 instead of ε>0 needed, and
O(log n) instead of O(n^δ)), so if the proof is correct it entails the
Contract's statement with correct quantifier order: r,L are constructed from
n,μ alone (not from ε), so the same witness serves every ε>0 simultaneously,
and C(ε,δ) is checked to depend only on ε,δ as required. **No statement
drift found; the artifact answers a strictly stronger question than asked
and correctly reduces that to the asked one.**

I flag, as context rather than a citable defect: the source explicitly frames
a positive answer to Question 8.1 for any δ<1/2 as something that "would be
very interesting" (card Q1), which suggests the authors regarded even the
weaker, ε-dependent, δ<1/2 case as open and hard. The artifact claims an
unconditional, ε-independent, O(log n) resolution for every δ>0 at once. That
is an unusually strong claim to make about a paper's own stated open
question. I could not locate a concrete mathematical flaw despite an
exhaustive line-by-line recheck (below) and a from-scratch recomputation of
every arithmetic step in the artifact's own numerical example (all of which
checked out exactly). I record this as a request for extra scrutiny in a
future round, not as a Class A–E defect, since I am not permitted to reject
on "surprising strength" alone without an identified error.

## Line-by-line verification of the mathematics

**Lemma 1** (quadratic-form space, evaluation, kernel). (a) is immediate
linear algebra. (b) is verified: the argument that `{|h|>|h(v0)|/2}` is open,
contains `v0`, hence has positive measure by definition of support, while
being contained in the μ-null set `{h≠0}`, is a valid contradiction; this
correctly transfers well-definedness of `ev_v` from a.e.-equality to
pointwise equality on `supp μ`. (c) Riesz representation on the
finite-dimensional space `F_μ` is routine and correctly invoked (every linear
functional on a finite-dimensional inner-product space is automatically
bounded). (d) is a direct computation (`q_I(v)=‖v‖²=1` on the sphere,
`q_{E_ab}(v)=v_av_b`), both correct.

**Lemma 2** (reproducing identities). (i) is the reproducing property applied
entrywise to `g_ab=[v↦v_av_b]∈F_μ`; correct, and the deduction that it holds
"for all a,b" including `a=b` is verified against Lemma 1(d)'s definition of
`E_ab`. (ii) `E_μ[k]=⟨k,[1]⟩=1`, correct; the chain `E_μ|k|≥1`,
`K(v0,v0)≥(E_μ|k|)²≥1` via Cauchy–Schwarz is verified. (iii) is definitional
plus Cauchy–Schwarz; correct.

**Lemma 3** (cheap base point). The trace identity `∫K(v,v)dμ=d` is verified
by expanding in an orthonormal basis (Parseval); this is the standard
"average leverage / reciprocal Christoffel function" identity, correctly
derived here from scratch (not cited from any source). The existence
argument (if `μ({g≤d})=0` then `g−d>0` μ-a.e. while `∫(g−d)dμ=0`, forcing
`g−d=0` a.e., contradiction) is a valid measure-theoretic argument, and the
subsequent step `A∩supp μ≠∅` (else `μ(supp μ)≤μ(A^c)<1`, contradicting
`μ(supp μ)=1`) is correctly executed. This gives a legitimately existing
`v0∈supp μ` with `K(v0,v0)≤d≤n(n+1)/2`, not merely a.e.

**Lemma 4** (entropy ≤ log second moment). `φ(t)=t log t ≤ t²` for all `t≥0`
(since `log t≤t` for all `t>0`, a standard elementary inequality, so
`t log t≤t·t`); this is correct and in fact holds without the case split the
artifact performs (the case split is harmless, not wrong). The
`ν:=|r|μ`-change-of-measure computation, `E_ν[log|r|]=E_μ[|r|log|r|]` and
`E_ν[|r|]=E_μ[r²]`, followed by Jensen on concave `log`, is a standard and
correctly executed argument.

**Proof of the Theorem.** All algebraic steps (`c:=1/E_μ|k|`, the bound
`c∈[K(v0,v0)^{-1/2},1]`, `E_μ|r|=1`, `E_μ[r vv^T]=c·v0v0^T`, `‖L‖_F=c`,
entropy `≤ log(c²K(v0,v0))=log(K(v0,v0)/(E_μ|k|)²)≤log K(v0,v0)≤log(n(n+1)/2)`)
were independently re-derived and match.

**COROLLARY.** `n(n+1)/2≤n²` for `n≥2` ⟹ `log(n(n+1)/2)≤2log n`;
`max_{x>0}(log x)/x^δ=1/(eδ)` was independently re-derived via calculus
(critical point at `x=e^{1/δ}`, value `1/(eδ)`) and matches exactly. The
`n=1` case (`log 1=0`) is trivial. Correct.

**REMARK A.** The algebra `‖M−L‖_F²=‖M‖_F²−2t·u^TMw+t²`, the discriminant
condition, and the final rearrangement to
`Σ_{i≥2}λ_i²≤(ε²/(1−ε²))λ_1²` were independently re-derived from the
quadratic-in-`t` formula and match exactly, including the "both roots
positive when `M≠0`" claim (product `=‖M‖_F²/(1−ε²)>0`, sum
`=2s_1/(1−ε²)>0` since `M≠0⟹λ_1≠0`).

**COROLLARY B.** The transfer of Lemmas 1–4 to the affine space
`G={X↦α+⟨A,X⟩}` on the compact domain `X` (compactness verified: `X` is the
intersection of the closed "rank ≤1" variety with the closed unit-Frobenius
sphere, hence closed and bounded) is structurally sound; the two properties
actually used (constant `∈G` via `α=1,A=0`, and coordinate functions `∈G` via
`A=e_ae_b^T`, using `⟨e_ae_b^T,X⟩=X_{ab}`) are correctly identified as
sufficient, and dimension count `≤n²+1` is correct.

**REMARK C, including the new (F1) paragraph.** The pre-existing sphere-case
"equivalently" derivation (`k≥0 ⟹ μ({±v0})=1/K(v0,v0)`) was independently
re-derived: the argument that `⟨v,w⟩=0` `μ'`-a.s. for every `w` in a basis of
`v0^⊥` forces `μ'({±v0})=1` is correct; `μ'({±v0})=K(v0,v0)·μ({±v0})=1` gives
`μ({±v0})=1/K(v0,v0)≥2/(n(n+1))`; and the conditioning reweighting
`r′:=1_{{±v0}}/μ({±v0})` reaching `v0v0^T` at entropy
`log(1/μ({±v0}))` was independently recomputed and matches. The **newly
added** Corollary-B paragraph (this round's only change) was checked in
full: `dμ′:=k dμ` a probability measure, `E_{μ′}[X]=X_0`, the Frobenius
bilinear expansion `E_{μ′}‖X−X_0‖_F²=1−2⟨X_0,X_0⟩+1=0` (independently
recomputed, correct), forcing `μ′({X_0})=1`, hence `μ({X_0})=1/K(X_0,X_0)`,
`≥1/(n²+1)`, and the conditioning reweighting reaching `X_0` at entropy
`log(1/μ({X_0}))≤log(n²+1)`. Every step recomputes correctly; this is a
faithful and, unlike the sphere case, slightly simpler (no `±`) analogue.

## Numerical check — recomputed from scratch
`n=2`, μ uniform on 4 named unit vectors. I independently recomputed:
`d=3` (verified the map `(a,b,c)↦(x1,x2,x3,x4)` is injective onto
`{x1+x2=x3+x4}`), the kernel `k=(3,−1,1,1)` at `v0=v1` (verified by solving
the 3 linear equations the reproducing property imposes), `E_μ[k]=1`,
`K(v0,v0)=‖k‖²=3`, the matrix identity
`¼(3v1v1^T−v2v2^T+v3v3^T+v4v4^T)=v1v1^T` (recomputed entrywise: sum is
`diag(4,0)`, `/4=diag(1,0)=v1v1^T` — exact), `E_μ|k|=3/2`, `c=2/3`,
`r=(2,−2/3,2/3,2/3)`, `E_μ|r|=1`, entropy `=0.1438` (recomputed:
`¼(2log2+2log(2/3))=0.1438`, matches to 4 s.f.), `log E[r²]=0.2877`
(recomputed: `E[r²]=4/3`, `log(4/3)=0.2877`, matches), `log 3=1.0986`. **All
of the artifact's stated numbers in this section are correct upon
independent recomputation.**

## Source-card verbatim audit (Class D findings)
1. Q1 quotation (used twice, once at top under DEPENDENCIES and implicitly
   referenced as "Q1" for the Target/GOAL): the card's text ends
   `...‖L‖_F ⩽ ε‖L‖_F` ?` (a space before the closing `?`); the artifact's
   DEPENDENCIES rendering ends `...‖L‖_F ⩽ ε‖L‖_F`?` (no space). Minor,
   non-substantive, but not byte-verbatim as the card's header promises
   ("Quotations below are verbatim"). (Noted in the artifact's own revision
   log as a previously-raised, previously-ruled-pedantic finding F13; I
   confirm it is a real, if trivial, discrepancy.)
2. Q8 quotation, embedded inside COROLLARY B's statement: the card's
   verbatim text begins "We will restrict our attention..." (capital `We`);
   the artifact's embedded rendering begins "we will restrict our
   attention..." (lower-case `we`), because it is spliced mid-sentence. The
   *separate* copy of the same quotation in the DEPENDENCIES section
   correctly preserves the capital `We`. This is a minor capitalization
   deviation from strict verbatim in one of the two places the quote
   appears.

Both quotations are otherwise used within their stated hypotheses: Q9
("deficient" ⟺ nonnegative + normalized, since it is defined only for
probability distributions) is correctly cited as the sole basis for the
"deficient hence nonnegative" gloss in Remark C(i), matching the card's own
explanatory note; Q4 (flatness) is correctly restricted to flat
distributions in Remark C(ii), with no overreach into the artifact's own
(non-flat) construction; Q5's tightness remark is correctly scoped to
Theorem 2.3 (deficient/nonnegative reweightings), not to the artifact's own
signed construction. No misapplied domain or dropped qualifying clause found
beyond the two typographic items above.

## Other minor (Class D / pedantic) observations
3. Proof plan: "Its `L²` norm averages to `d` over `μ`" — the quantity that
   averages to `d` (Lemma 3) is `K(v,v)=‖k_v‖²`, i.e. the **squared** `L²`
   norm, not the `L²` norm itself. This is loose language in a
   non-load-bearing overview paragraph; the actual Lemma 3 statement and
   proof are precise and correct.
4. Remark C(i) (the pre-existing sphere-case derivation, unchanged this
   round): "`k(−v_0)=k(v_0)=K(v_0,v_0)` by Lemma 1(c)" attributes both
   equalities to Lemma 1(c), but only the second (`k(v0)=ev_{v0}(k)=
   K(v0,v0)`) actually comes from Lemma 1(c)/the definition of `K`; the
   first (`k(−v0)=k(v0)`) is simply evenness of quadratic forms
   (`q_Q(−v)=q_Q(v)`), a fact not stated in Lemma 1(c). The equality itself
   is correct; only the attribution is imprecise.

Neither of items 3–4 affects the validity of any proof step; both are
citation/exposition nits in text the artifact's own revision log records as
previously flagged (F5, F9) and ruled pedantic in an earlier, unseen round.
I report them anyway per the brief to judge the artifact cold and note
everything found, however minor.

## Other checks performed, no defect found
- Reading convention #3 (L need not be symmetric/PSD): the artifact's L
  happens to be PSD; this is a permitted special case, not a violation.
- Reading convention #2 (no regularity beyond Borel measurable +
  integrable): the artifact's r is a bounded quadratic form, which is more
  regular than required but not forbidden, since the Contract only sets a
  floor, not a ceiling, on regularity.
- GAP REGISTER is empty and I found no `[GAP]`/`[SOURCE-BLOCKED]` markers in
  the body; SOURCE REQUEST is "none" and I found no place where an
  unverifiable external claim is relied upon (Class E does not apply here;
  every "External mathematics used" item is a standard, restated fact —
  Riesz representation, Cauchy–Schwarz, Jensen, `‖·‖_op≤‖·‖_F`, `μ(supp
  μ)=1`, and the elementary calculus maximum — none requiring a source
  card).
- Definition of "signed reweighting" and the `0 log 0:=0` convention in the
  artifact's GOAL match the Contract's Definition section exactly.
- Quantifier order of the final Corollary matches the Contract's required
  order (`C` depends only on `ε,δ`; `r,L` may depend on `n,μ,ε,δ`, and in
  fact here depend only on `n,μ`).

## ### VERDICT ###
STATUS: CLEAN (no Class A/B/C defects found after exhaustive line-by-line
re-derivation and full recomputation of the artifact's numerical example;
several Class D pedantic/typographic issues found, none load-bearing). The
artifact's Theorem, Lemmas 1–4, Corollary, Remark A, Corollary B, and the
newly added Remark C(i) paragraph (this round's sole edit) were each checked
independently against their own hypotheses and against elementary
mathematics, and all arithmetic in the artifact's numerical example was
recomputed from scratch and matches exactly. No statement drift relative to
the Contract was found: the artifact proves a strictly stronger claim (exact
rank-one match, `O(log n)` entropy, `ε`-independent constant) that correctly
entails the Contract's statement with the correct quantifier order. Two
verbatim-quotation deviations (a missing space before `?` in the Question
8.1 quote, and a capitalization change `We`→`we` in one of two copies of the
§2.3 quote embedded in Corollary B) and two exposition-level imprecisions
(an unsquared "`L²` norm" in the Proof plan, and an attribution of
`k(−v0)=k(v0)` to Lemma 1(c) that should instead cite evenness of quadratic
forms) were found; all are Class D. I explicitly flag, as a non-defect
observation for the human/orchestrator rather than a citable finding, that
the magnitude of the result (a uniform, `ε`-independent, `O(log n)`,
exact-equality resolution of a question the source paper frames as open and
"would be very interesting" even for the weaker `δ<1/2` case) is unusually
strong, and merits a second, independently-run adversarial pass focused
specifically on hunting for a hidden restriction on `μ` or `n` that the
proof's generality claim might be silently smuggling past — despite my not
having found any such restriction after checking every quantifier in Lemmas
1–4 and the Theorem against the stated "for every `n`, for every `μ`."

## ### FINDINGS ###

| Location | Severity/Class | Explanation |
|---|---|---|
| DEPENDENCIES, Question 8.1 quotation ("...`‖L‖_F ⩽ ε‖L‖_F`?") | D (pedantic, verbatim-fidelity) | Card has a space before the closing `?` ("`⩽ ε‖L‖_F` ?"); artifact's rendering has no space. Non-substantive but not byte-verbatim as claimed. |
| COROLLARY B statement, embedded §2.3 quotation ("we will restrict...") | D (pedantic, verbatim-fidelity) | Card's verbatim text begins with capital "We"; the copy embedded mid-sentence in Corollary B's statement lowercases it to "we". The separate DEPENDENCIES copy of the same quote is correctly capitalized. |
| Proof plan, "Its `L²` norm averages to `d` over `μ`" | D (pedantic, imprecise terminology) | The quantity shown (Lemma 3) to average to `d` is `K(v,v)=‖k_v‖²`, the squared `L²` norm, not the `L²` norm itself. Lemma 3's own statement and proof are precise; only this overview sentence is loose. |
| Remark C(i), pre-existing sphere-case derivation, "`k(−v_0)=k(v_0)=K(v_0,v_0)` by Lemma 1(c)" | D (pedantic, misattribution) | Only `k(v0)=K(v0,v0)` follows from Lemma 1(c)/the definition of `K`. `k(−v0)=k(v0)` follows instead from evenness of quadratic forms (`q_Q(−v)=q_Q(v)`), not stated in Lemma 1(c). The equality itself is correct; the citation is imprecise. |
| Whole artifact (Theorem, Lemmas 1–4, Corollary, Remark A, Corollary B, new Remark C(i) paragraph) | Not a defect — verification note | Every proof step was independently re-derived and every arithmetic claim in the NUMERICAL CHECK section was recomputed from scratch; all matched exactly. No Class A (statement drift), B, or C defect was found despite an adversarial search, including checking the quantifier order against the Contract and re-deriving Lemma 3's averaging argument, Lemma 4's Jensen step, and both Corollary-B and sphere-case reconciliation arguments in Remark C in full. |
| Whole artifact — scope/strength of claim | Not a citable defect — flagged for follow-up | The result as proved (uniform `O(log n)` entropy, exact rank-one match, `ε`-independent constant, for every `n` and every Borel probability measure `μ`) is markedly stronger than what the source paper frames as an open and "very interesting" question, even restricted to `δ<1/2`. I could not identify a flaw, but the gap between "open problem in a STOC 2017 paper" and "resolved in full generality by an elementary RKHS/Christoffel-function averaging argument" is large enough that I recommend a further independent pass targeted specifically at this concern before treating the artifact as settled. |
