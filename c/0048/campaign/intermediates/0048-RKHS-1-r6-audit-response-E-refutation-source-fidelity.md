# Referee Report — 0048-RKHS-1-r6
## Angle: REFUTATION-ATTEMPT-AND-SOURCE-FIDELITY (blind, cold read)

## STEP 0 — Completeness gate
The artifact contains `### END OF ARTIFACT [0048-RKHS-1-r6] ###` at the expected
place, and the file continues to a well-formed, grammatically complete final
sentence in its trailing REVISION LOG. Not truncated. Proceeding to full review.

## Statement actually proved, vs. the Contract (Class-A check, done first)
The artifact proves: for every Borel probability measure `μ` on `S^{n-1}`,
there exist `v_0 ∈ supp μ` and a signed reweighting `r` (a bounded quadratic
form on the sphere) with entropy cost `≤ log(n(n+1)/2)` such that
`E_μ[r(v)vv^T] = c·v_0v_0^T` **exactly** (Frobenius error `0`), `c>0`. The
Corollary then converts `log(n(n+1)/2) ≤ (2/(eδ))n^δ` to get
`C(ε,δ) = 2/(eδ)`, independent of `ε`. This is a *strengthening* of the
Contract's statement (exact recovery, `ε=0`, entropy `O(log n)` rather than
merely `O(n^δ)`), not a different theorem: since `0 ≤ ε‖L‖_F` holds for every
`ε>0`, the Contract's weaker existential claim follows immediately. No
statement drift found between the Contract and what is actually proved.
Corollary B is explicitly presented as an *additional* construction (unit-
Frobenius rank-one manifold), not as part of the Contract's target statement,
and is labeled as such.

## PART 1 — REFUTATION ATTEMPT

I tried to break the Theorem/Corollary/Corollary B with degenerate,
symmetric-discrete, and continuous test measures, and by stress-testing each
lemma's hypotheses individually.

1. **Point mass** `μ = δ_{v_0}`. `F_μ` collapses to the 1-dimensional space of
   constants on `L²(δ_{v_0})`; `K(v_0,v_0)=1=d`; `k=1`, `c=1`, `r=1`,
   `E_μ[rvv^T]=v_0v_0^T` exactly, entropy `0 = log(1)`. No violation.

2. **Symmetric discrete measure**: `μ` uniform on the standard basis
   `{e_1,…,e_n}` of `R^n`. Computed the reproducing kernel by hand:
   `F_μ ≅ R^n` (diagonal entries free), `d=n`; kernel at `v_0=e_1` is
   `k=(n,0,…,0)`; `E_μ[k]=1` ✓, `K(v_0,v_0)=n=d` (tight, equality case);
   `c=1`, `r=k`; `E_μ[rvv^T]=e_1e_1^T` exactly; entropy `= log n = log d`
   exactly, saturating Lemma 4's bound with equality. No violation — this is
   the extremal case, not a counterexample.

3. **Continuous symmetric measure**: `μ` uniform on `S^1` (`n=2`). By hand:
   basis `{1,cos2θ,sin2θ}` orthogonal under uniform measure, `d=3`. Kernel at
   `v_0=(1,0)`: solved `k(θ)=1+2cos2θ`. Checked `E_μ[k]=1` ✓,
   `E_μ[k^2]=1+4·(1/2)=3=d` ✓ (uniform measure ⟹ `K(v,v)=d` at *every* point
   by symmetry — the averaging bound is tight everywhere here, still not
   violated, `≤` holds as equality). Confirmed `k` is negative on an arc
   (`θ∈(π/3,2π/3)` mod the period), exhibiting the cancellation the Contract's
   "Known boundary" flags as necessary. Computed `E_μ|k| = (2π-2N)/(2π)` with
   `N=∫_{2π/3}^{4π/3}(1+2cosu)du = 2π/3-2√3 ≈ -1.370`, giving
   `E_μ|k|≈1.436`, `c≈0.696`, entropy bound `≤ log(3/1.436²)≈0.375 ≤ log 3`.
   Internally consistent, no violation.

4. **Independently re-derived the artifact's own numerical check** (`n=2`,
   `μ` uniform on 4 points `v_1,…,v_4`). Re-solved the reproducing-kernel
   linear system directly (not just spot-checking the printed numbers):
   confirmed `k=(3,-1,1,1)` satisfies `⟨k,f⟩=f_1` for the *entire*
   3-dimensional constraint space `{f: f_1+f_2=f_3+f_4}`, not merely at the
   specific vectors checked in the artifact's text; re-multiplied out
   `¼(3v_1v_1^T-v_2v_2^T+v_3v_3^T+v_4v_4^T)` entrywise and confirmed it equals
   `v_1v_1^T` exactly. The artifact's own numerical example is correct.

5. **Adversarial skewed-weight measure**: `n=2`, `μ(\{e_1\})=1-η`,
   `μ(\{e_2\})=η`, `η→0`. Computed `K(e_1,e_1)=1/(1-η)→1` and
   `K(e_2,e_2)=1/η→∞` as `η→0`; verified `(1-η)K(e_1,e_1)+ηK(e_2,e_2)=2=d`
   exactly (Lemma 3's averaging identity). The construction correctly selects
   the cheap point `v_0=e_1`; there is no way to force it onto the expensive
   point, and no measure can make *every* support point simultaneously
   expensive (that is exactly what the averaging argument forecloses). No
   counterexample.

6. **Boundary case `n=1`** (`S^0=\{-1,1\}`): degenerate but consistent —
   `d=1`, entropy `0 = log(n(n+1)/2)=log 1`. No violation.

7. **Targeted attacks on individual lemma hypotheses**: checked whether
   Lemma 1(b)'s open/null-set argument secretly needs more than "continuous +
   second countable" (it doesn't — standard); whether Lemma 3's averaging
   argument could fail for a pathological (non-atomic, fractal-support)
   measure (it can't — it is a two-line measure-theoretic fact independent of
   the geometry of `supp μ`); whether Lemma 4's Jensen step needs `r`
   bounded away from `0` (it doesn't, via the `0 log 0 := 0` convention and
   `ν({r=0})=0` by construction of `ν=|r|dμ`). Found no hidden restriction.

8. **Corollary B's transfer** (`S^{n-1}→X`, quadratic forms → the affine
   space `G`): checked compactness of `X` (continuous image of
   `S^{n-1}×S^{n-1}`, hence compact — holds), boundedness (`|⟨A,X⟩|≤‖A‖_F` by
   Cauchy–Schwarz since `‖X‖_F=1` on `X` — holds), and re-derived by hand the
   arithmetic of the newly-added Remark C(i) paragraph:
   `E_{μ'}‖X-X_0‖_F² = E_{μ'}‖X‖_F² - 2⟨X_0,E_{μ'}X⟩ + ‖X_0‖_F² = 1-2(1)+1=0`,
   confirming the point-mass conclusion `μ'(\{X_0\})=1` and the subsequent
   `μ(\{X_0\})=1/K(X_0,X_0)≥1/(n²+1)` bound. Correct.

**Outcome: no counterexample `(n,μ)` found** for the Theorem, the Corollary,
or Corollary B, despite deliberately targeting degenerate, symmetric, and
continuous distributions, and despite the a priori suspicion that a result
this strong (exact, `O(log n)`-entropy resolution of an open STOC 2017
question) invites extra scrutiny. Every individual lemma is an elementary,
generically-true fact (linear algebra, Riesz representation on a
finite-dimensional space, an averaging/pigeonhole argument, and Jensen's
inequality), and none of them acquires a hidden dependence on `μ` beyond the
dimension bound `d ≤ n(n+1)/2` (resp. `n²+1`), which is exactly what the
argument needs to stay uniform in `μ`.

## PART 2 — SOURCE FIDELITY

Cross-checked every quotation attributed to `S1-bks-q81-card.md` against the
card's verbatim text.

| Quotation used | Verbatim match? | Domain fidelity |
|---|---|---|
| Question 8.1 (Q1), GOAL/DEPENDENCIES | Exact match, including the "would be very interesting… We do know that the answer to this question is No if one does not allow negative reweighting functions" continuation | Applied as the Contract's literal target; no extension |
| Theorem 2.3 (Q2), DEPENDENCIES | Exact match | Correctly treated as *not* load-bearing for the Theorem (used only for the scope discussion in Remark C) |
| Definition 2.2 / "k-deficient" (Q9) | Exact match | Correctly used only for the card's own annotation ("deficient ⟹ nonnegative, normalised"); this is the card's explicit note, not an artifact-side extrapolation |
| Flatness dictionary, §2.2 (Q4) | Exact match | Artifact's claim "stated for flat distributions" is literally true of the quote (it begins "a flat distribution µ′…") — no broadening |
| Tightness remark, p.6 (Q5) | Exact except: nested quote marks rendered as `'close to rank one'` (single) vs. card's `"close to rank one"` (double) | No change of scope or meaning |
| Footnote 7 (Q6) | Exact except same single/double nested-quote substitution around `'approximate'` | No change of scope; this is the clause that a prior round restored in full (per the artifact's own revision log), and the restoration is verified complete here — the "small constant or `1/polylog(n)`" clause is present, not dropped |
| Footnote 8 (Q7) | Exact match | Correctly glossed as "moot here: our constant is independent of ε" — consistent with the quote, which is about ε-dependence of the *log-rank* bound, not the Contract's C(ε,δ) |
| §2.3 normalisation (Q8), in Corollary B and in DEPENDENCIES | Exact match, including the restored parenthetical "(This restriction is easy to lift and anyway holds automatically in our intended application.)" in both places | Artifact says this is "the normalisation used in the source paper's intended application" — this is exactly what the quote itself asserts ("…in our intended application"); the artifact does **not** claim Theorem 2.3 itself "is stated over" the unit-Frobenius domain — Corollary B is presented as the artifact's own independent construction on that domain, motivated by, but not attributed as a restatement of, Theorem 2.3 |

No dropped qualifying clause and no missing ellipsis were found in any
quotation; the two places flagged above are cosmetic nested-quote-mark
substitutions (single vs. double quotes around an inner quoted phrase),
almost certainly done to avoid an unresolvable nesting collision with the
outer quotation delimiter in plain text — they do not alter the meaning of
the quoted material and do not affect any hypothesis or domain claim drawn
from it.

I specifically looked for the pattern flagged in the task — an artifact claim
that a cited theorem "is stated over" some normalized/unit-Frobenius domain
— and found the one candidate (Corollary B's normalisation clause). Checked
word-for-word against Q8: the artifact's characterization is accurate and
does not stretch the card's language into a claim the card does not support.
Theorem 2.3 (Q2) itself is quoted as applying to "any distribution over rank
one `n×n` matrices" (no unit-norm restriction stated in that quote), and the
artifact never asserts otherwise — Corollary B is honestly scoped as an
artifact-internal construction on a *narrower* domain than Theorem 2.3's own
stated domain, not a broadening of it.

## FINDINGS

| Location | Severity/Class | Explanation |
|---|---|---|
| DEPENDENCIES, p.6 tightness quote (Q5) | D (cosmetic) | Nested quotation `'close to rank one'` uses single quotes where the card has double quotes `"close to rank one"`. No change in wording or meaning; likely a typographic nesting workaround. |
| DEPENDENCIES, footnote 7 quote (Q6) | D (cosmetic) | Same single/double nested-quote substitution around `'approximate'`. No change in wording or meaning. |

No Class A (statement drift), B (logical gap), C (unjustified step), or E
(unverifiable/needs source) defects were found. No counterexample to the
Theorem, Corollary, or Corollary B was found despite a deliberate, honest
attempt across degenerate, symmetric-discrete, continuous, and adversarially
skewed test measures.

## STEP LOG

See PART 1 above for the itemized refutation attempts (1–8) and their
outcomes, and PART 2 for the quotation-by-quotation source-fidelity
cross-check. Summary: eight distinct refutation attempts, all failed to
produce a counterexample; the artifact's own numerical check was independently
re-derived and confirmed rather than merely eyeballed; nine quotations
cross-checked against the source card, all substantively faithful, two
cosmetic (Class D) nested-quote-mark deviations noted.

### VERDICT ###
STATUS: CLEAN

Summary: The artifact proves a strengthening of the Contract's statement
(exact rank-one recovery, `ε=0`, entropy cost `O(log n)` via
`C(ε,δ)=2/(eδ)`, independent of `ε`) through an elementary but correct
finite-dimensional reproducing-kernel / Christoffel-function argument (Lemmas
1–4), and extends the same mechanism to the unit-Frobenius rank-one manifold
in Corollary B. A deliberate adversarial search — point masses, symmetric
discrete measures, continuous (rotationally symmetric) measures, and skewed
two-point measures, plus an independent hand re-derivation of the artifact's
own numerical example and of the newly added Corollary-B reconciliation
paragraph's arithmetic — produced no counterexample and no logical gap in any
lemma. Every quotation attributed to source card `S1-bks-q81-card.md` is
verbatim-faithful and applied within the domain the card's own words support;
the only deviations found are two cosmetic single/double nested-quote-mark
substitutions (Class D) that do not affect meaning or scope. No SOURCE
REQUEST is warranted; none of the card's material is treated as broader than
what it states, and the one place the artifact invokes a specific normalized
domain (Corollary B, citing the source's §2.3 unit-norm-columns remark) is
accurately and narrowly characterized as motivating an artifact-internal
construction, not as a restatement of Theorem 2.3 over that domain.
