# Referee Report — 0048-RKHS-1-r6 — Angle: MEASURE-THEORETIC (blind pass)

**Artifact reviewed.** `c/0048/campaign/intermediates/0048-RKHS-1-r6.md`
**Inputs read.** `CONTRACT.md`, `sources/S1-bks-q81-card.md`, the artifact itself.
No other file in `intermediates/` was consulted.

## STEP 0 — Completeness gate

The artifact contains the line `### END OF ARTIFACT [0048-RKHS-1-r6] ###`
(line 441 of the file) and no equation/proof stops mid-way before it; the
material after that marker is an explicitly-labelled `REVISION LOG` appendix,
consistent with the artifact's own header note ("REVISION LOG at the end of
this file"). **Not truncated.** Proceeding to full review.

## Statement-drift check (Class A), done first

The artifact proves: for every `n ≥ 1` and every Borel probability measure `μ`
on `S^{n-1}`, there is `v_0 ∈ supp μ`, `c ∈ [(n(n+1)/2)^{-1/2}, 1]`, and a
bounded Borel `r` (a quadratic form restricted to the sphere) with
`E_μ[r(v)vv^T] = c·v_0v_0^T` **exactly** and entropy `≤ log(n(n+1)/2)`. This
is then packaged as `C(ε,δ) = 2/(eδ)`, independent of `ε`, answering the
Contract's existential statement with a strictly stronger conclusion (exact
rank-one, error `0 ≤ ε‖L‖_F` for every `ε>0`). This matches the Contract's
"THE STATEMENT TO BE PROVED" with no weakening or narrowing of the
quantifiers (`∀ε,δ`, `∀n`, `∀μ` Borel — no finiteness/niceness restriction is
introduced anywhere in the Theorem's hypotheses). **No statement drift found.**

Corollary B is not required by the Contract (the Contract's Notation and
Statement sections speak only of `S^{n-1}`); it is presented as an
additional, self-labelled result. Per the launching instruction, it and its
Remark C reconciliation paragraph are audited below on their own terms as
part of the measure-theoretic content in scope.

## Measure-theoretic audit

I went through Lemma 1(b),(c), Lemma 2, Lemma 3's trace identity, Lemma 4's
Jensen argument, and the newly-added Corollary-B paragraph line by line,
specifically hunting for smuggled regularity (atomicity, absolute continuity,
density, closedness of support) that would fail for a general Borel `μ`.

**Lemma 1(b) (well-definedness of evaluation at points of `supp μ`).** The
proof uses only: (i) quadratic-form representatives are continuous, hence
`{h≠0}` open where `h≠0`; (ii) the topological definition of support (every
open neighbourhood of a support point has positive measure). Neither atoms
nor density nor countability of `supp μ` is used. I tried to break this with
a singular-continuous `μ` (e.g. a measure supported on a fat Cantor subset
of `S^1`, or of `S^2`'s equator): the argument goes through verbatim, because
it never needs `{h≠0}` to be Lebesgue-null, only `μ`-null, and it never
invokes analytic continuation or density of `supp μ`. This is the correct,
general argument and it is used correctly. The parenthetical note after
Lemma 1 ("(b) is the only place where the general Borel case differs from the
finitely supported case...") is an accurate self-assessment.

**Preliminary (P1), `μ(supp μ)=1`.** Correctly derived from second
countability via the Lindelöf property (an arbitrary union of open null sets
admits a countable subcover from among its own members, hence is itself
null by countable subadditivity). This is the standard, fully general fact;
it holds for every Borel probability measure on a second-countable space,
atomic or not, with no additional hypothesis. `X` (Corollary B's domain) is
a subspace of `R^{n×n}`, hence also second countable, so the same fact
transfers; the artifact's claim "Run Lemmas 1-4 verbatim... X (compact)"
implicitly relies on this, correctly.

**"Non-closed support" as a hunted counterexample.** I looked for a Borel
`μ` whose support fails to be closed, per the task's suggestion. This is not
achievable: `supp μ` is *defined* as the complement of the union of all open
`μ`-null sets, which is closed by construction, for every Borel measure on
every topological space. There is no coherent adversarial instance here;
the artifact's arguments that rest on `supp μ` being closed (needed, e.g.,
implicitly for `A ∩ supp μ ≠ ∅` type deductions in Lemma 3) are safe for this
reason, not because of an unstated assumption.

**Lemma 1(c)/(d), Lemma 2 (kernel construction and its identities).** `F_μ`
is a finite-dimensional subspace of `L²(μ)` regardless of `μ` (it is the
image of a fixed finite-dimensional space `Sym_n`, resp. `G`, under a linear
map into `L²(μ)`), so the Riesz representation of `ev_v` always exists and is
unique — no compactness/separability/atomicity of `μ` is needed beyond
finite-dimensionality of the target inner-product space. Integrability in
Lemma 2 is disposed of by boundedness (`k` and the coordinate functions are
all bounded on the compact domain, and `μ` is a probability measure), so no
extra regularity of `μ` is used. I checked this survives non-atomic and
singular `μ` identically.

**Lemma 3, `∫K(v,v)dμ = d` (trace/Christoffel identity).** The subtlety
flagged by the task — is the integrand genuinely well-defined `μ`-a.e. and
Borel? — is handled correctly: `K(v,v)` is officially defined only on
`supp μ` (via Lemma 1(c)), but the proof exhibits a genuine Borel (in fact
polynomial/continuous) function `g` on the whole domain that agrees with
`K(v,v)` at **every** point of `supp μ` (not just a.e. on it — this follows
from Parseval plus the exact, pointwise identity `ev_v(f_j)=q_j(v)` valid at
every `v∈supp μ` by Lemma 1(b)), and then uses `μ(supp μ)=1` (P1) to identify
`∫K(v,v)dμ` with `∫g dμ`. This sidesteps the well-definedness worry entirely
rather than assuming it. The subsequent argument that some `v_0 ∈ supp μ`
achieves `K(v_0,v_0) ≤ d` (via `μ(A)>0 ⟹ A∩supp μ≠∅`, using only that
`S^{n-1}\supp μ` is null) is correct and needs no atomicity.

**Lemma 4 (entropy bound via `t log t` / Jensen).** The proof is fully
general: `φ(t)=t log t` is sandwiched (`φ(t) ≥ -1/e`, `φ(t) ≤ t²`) so
`φ(|r|) ∈ L¹(μ)` follows from `r ∈ L²(μ)` alone; `dν := |r|dμ` is a bona
fide probability measure for **any** Borel-measurable, `μ`-integrable `|r|`
with `E_μ|r|=1` (no atomicity, density, or continuity of `μ` or `r` needed);
`ν({r=0})=0` is immediate from the definition of `ν`; and the final step is
ordinary Jensen for `log`, concave, against the probability measure `ν`. I
found no hidden regularity beyond the explicitly stated `r ∈ L²(μ)`. Note
that this hypothesis (`r∈L²(μ)`) is formally stronger than the Contract's
Definition, which asks only for Borel-measurable + `μ`-integrable `r`; this
is not an overclaim, however, since the Theorem only ever invokes Lemma 4 for
its own constructed `r`, which is bounded (hence trivially in every `L^p`,
`p<∞`, on the probability space `(S^{n-1},μ)`). The connecting one-line fact
("bounded ⟹ L²" ) is used but not spelled out at the point of invocation in
the Proof of the Theorem ("`r ∈ L²(μ)` with `E_μ|r|=1`, so Lemma 4 ... give");
this is trivial and I do not rate it as a defect, only note it as the one
place a fully pedantic reader could ask for one more clause.

**Corollary B and the new Remark C paragraph (the audited addition).** This
is the part most exposed to a "works only for nice `μ`" failure, since it
asserts that `k ≥ 0` `μ`-a.e. forces `μ'({X_0}) = 1`, i.e. an atom. I traced
the chain of implications specifically to see whether atomicity of `μ` (or
of the derived `μ'`) is *assumed* anywhere, which would be circular, or
whether it is *derived*:

1. `dμ' := k dμ` is a probability measure — needs only `k ≥ 0` `μ`-a.e. and
   `∫k dμ=1` (the transfer of Lemma 2(ii)); no atomicity used.
2. `E_{μ'}[X] = X_0` — this is `E_μ[kX]=X_0` (the transfer of Lemma 2(i)),
   an unconditional reproducing-kernel identity that holds for the *signed*
   `k` regardless of sign; reinterpreted via `μ'=kdμ` once `k≥0` is assumed.
3. `E_{μ'}‖X-X_0‖_F² = E_{μ'}‖X‖_F² - 2⟨X_0,E_{μ'}X⟩ + ‖X_0‖_F² = 1-2+1 = 0`
   — this is the general Hilbert-space "variance" identity
   `E‖Y-EY‖² = E‖Y‖² - ‖EY‖²`, valid for any integrable finite-dimensional
   random vector, using only `‖X‖_F≡1` on the domain `X` (true identically,
   not just a.e.) and step 2. No regularity of `μ` needed here either.
4. "Nonnegative integrand, vanishing integral ⟹ vanishes a.e." is a basic
   measure-theoretic fact valid for *every* measure. This yields
   `μ'({X_0})=1` as a **conclusion**, not an input.
5. `1 = μ'({X_0}) = ∫_{\{X_0\}} k\,dμ = k(X_0)\,μ({X_0}) = K(X_0,X_0)\,μ({X_0})`
   (using `k(X_0)=ev_{X_0}(k)=K(X_0,X_0)`, valid because `X_0∈supp μ`), so
   `μ({X_0}) = 1/K(X_0,X_0) > 0`.

So the argument genuinely *derives* that `μ` must have an atom at `X_0`
whenever the hypothesis `k_{X_0}≥0` `μ`-a.e. holds; it does not assume this
for a "nice" `μ` and merely check the nice case. I attempted the natural
adversarial move — take `μ` singular continuous or absolutely continuous on
`X` and ask whether the same chain still runs — and it does: for such `μ`,
the derivation instead shows that the hypothesis `k_{X_0}≥0` `μ`-a.e. *cannot*
hold (since a non-atomic `μ` has `μ({X_0})=0` for every point, contradicting
step 5), which is a consistent, non-pathological conclusion, not a breakdown
of the proof. In other words: the claim actually being proved is an
implication ("if the reweighting is already nonnegative, `μ` has an atom
there"), and the implication is sound for arbitrary Borel `μ`; it says
nothing false about non-atomic `μ` because for those the antecedent simply
fails. I could not find a `μ` for which this reasoning produces an
incorrect conclusion.

The mechanical transfer claim ("Run Lemmas 1-4 verbatim... boundedness on
`X` gives Lemma 1(a)... continuity of the elements of `G` gives Lemma 1(b)
unchanged") is accurate: every step of Lemmas 1-4 that I checked uses only
(i) finite-dimensionality of the function space, (ii) continuity/boundedness
of its elements on a compact domain, (iii) that it contains the constant
function, and (iv) that it contains enough coordinate functions to recover
the matrix identity — all four hold for `G` on `X` exactly as claimed.

## Other observations (non-blocking)

* The dimension counts (`d ≤ n(n+1)/2` for `Sym_n`, `dim G ≤ n²+1` for the
  affine space `{α + ⟨A,·⟩}`) are correct arithmetic and are used only as
  upper bounds, so a possible strict inequality `dim F_μ < dim(ambient space)`
  for special `μ` (e.g. `μ` concentrated on a coordinate hyperplane) causes
  no issue — the proof only ever needs the upper bound.
* `n=1` edge case (`S^0 = \{-1,1\}`) is consistent: `log(1·2/2)=log 1=0`,
  matching the fact that any measure on a two-point space is automatically
  atomic, so no continuum subtlety arises there; the Corollary's case split
  at `n=1` is correctly handled separately.

## Conclusion of the measure-theoretic audit

I did not find a Class A (statement drift), B, or C defect in the
measure-theoretic machinery. Every place where the Contract's requirement of
an *arbitrary* Borel probability measure (not finitely-supported, not
absolutely continuous, not "nice" in any sense) could plausibly break the
argument — evaluation at support points, kernel existence/integrability, the
trace identity's integrand, the entropy/Jensen step, and the new atom-forcing
argument for Corollary B — is instead handled by an argument that provably
does not use atomicity, density, or closedness-of-support as a hidden
assumption; where such properties appear (e.g. `μ` having an atom at `X_0`),
they are *derived*, not assumed. I was unable to construct a singular
continuous, non-atomic, or otherwise pathological counterexample that
defeats any step.

### VERDICT ###

STATUS: CLEAN

Summary: Judged purely on the measure-theoretic content, the artifact
correctly handles arbitrary Borel probability measures `μ` on `S^{n-1}`
(Theorem, Lemmas 1-4) and on the unit-Frobenius rank-one manifold `X`
(Corollary B and its Remark C reconciliation paragraph), with no smuggled
regularity: Lemma 1(b)'s well-definedness argument, the trace identity of
Lemma 3, the Jensen/entropy step of Lemma 4, and the newly-added Corollary-B
point-mass paragraph all rest only on general facts (topology of support,
finite-dimensional Riesz representation, Lindelöf-based full-measure-of-
support, and a Hilbert-space variance identity) that hold without atomicity,
absolute continuity, or closedness assumptions on `μ`; where the argument
concludes that `μ` has an atom, this is a derived consequence of a stated
hypothesis (`k≥0` a.e.), not an assumption, and I could not construct a
singular-continuous or non-atomic counterexample that breaks any step. No
Class A/B/C/D/E defects were found on this angle; the artifact is CLEAN with
respect to the measure-theoretic audit requested.

### FINDINGS ###

| Quoted location | Severity/class | Explanation |
|---|---|---|
| (none — no defect found) | — | Lemma 1(b)'s proof (`if h(v_0)≠0 for some v_0∈supp μ, then U:={|h|>|h(v_0)|/2} is open...`) verified correct for singular-continuous/non-atomic `μ`; no gap. |
| (none — no defect found) | — | Preliminary (P1) (`μ(supp μ)=1`, via second countability/Lindelöf) verified as the standard, fully general fact; transfers correctly to `X`. |
| (none — no defect found) | — | Lemma 3's `∫K(v,v)dμ=d`: integrand well-definedness resolved via an everywhere-on-`supp μ` polynomial representative `g`, not an a.e. hand-wave; correct. |
| (none — no defect found) | — | Lemma 4's Jensen/`t log t` step: uses only Borel measurability, `r∈L²(μ)`, and `E_μ|r|=1`; no extra regularity of `μ` or `r` smuggled in. |
| Remark C(i), added paragraph (`Corollary B's construction... k ≥ 0 μ-a.e.... μ'({X_0})=1`) | (none — no defect found) | Traced the full chain; the atom `μ({X_0})=1/K(X_0,X_0)>0` is a derived consequence of the hypothesis `k_{X_0}≥0` a.e., valid for arbitrary Borel `μ`, not an assumption of atomicity; no counterexample found. |
| Proof of the Theorem (`r ∈ L²(μ) with E_μ|r|=1, so Lemma 4 ... give`) | D (pedantic) | The one-line fact "bounded Borel function on a probability space is in `L²`" is used but not spelled out at the point of invoking Lemma 4; trivial, not a genuine gap. |
| Task-suggested "non-closed support" pathology | (checked, non-issue) | `supp μ` is closed by definition for every Borel measure on every topological space; no such counterexample is constructible, so this cannot be a source of failure anywhere in the artifact. |
