# TRIAGE — 0048-RKHS-1

Handling editor's ruling on the union of referee passes A–E. Adjudicated on the
mathematics alone; referee confidence and referee verdict labels carry no weight.
Every disputed claim that was mechanically checkable was checked by exact
computation (sympy, rational arithmetic) rather than by argument.

## Disposition summary

The Contract-level chain — Lemma 1, Lemma 2, Lemma 3, Lemma 4, the Theorem and
the Corollary — survives triage intact. Four passes (A, C, D, E) converge, and my
own exact recomputation confirms, on exactly one real mathematical defect, raised
at three separate loci: the artifact's universal claim that its `r` "takes both
signs unless `μ` is a point mass" is false, and the quantitative sentence offered
in its support (`E_μ|k| = K(v_0,v_0)^{1/2}` "in general") misstates the
artifact's own Lemma 2(iii) inequality as an equality — refuted by the artifact's
own NUMERICAL CHECK (`E_μ|k| = 3/2`, `K^{1/2} = √3 = 1.7320…`). I verified all
three proposed counterexamples in exact arithmetic and all three are sound, and
in each of them the offending base point is a *legitimate* output of Lemma 3
(`K(v_0,v_0) ≤ d`), so the construction itself can emit a nonnegative `r`. Both
defects live in the Proof plan prose and Remark C, which no earlier step invokes;
deleting them outright would leave a proof of the Contract statement that stands.
Pass B's affirmative clearance of Remark C.1 ("the artifact's `r` is shown
genuinely signed … whenever `μ` is not a point mass") is itself false and is
overruled, so that the reviser does not lean on it. One further sentence-level
over-claim inside load-bearing Lemma 1(b) is upheld as a wording repair that does
not disturb the lemma's content. Six findings are pedantic. One finding — the
gloss "deficient, i.e. nonnegative" — cannot be settled from card S1 and leaves
the revision loop for the source queue.

## Recomputations performed for this ruling

Exact (rational/symbolic) verification, not reasoning:

| claim checked | result |
|---|---|
| Artifact NUMERICAL CHECK (`n=2`, 4 points): `d`, `k`, `E_μ[k]`, `K`, `E_μ\|k\|`, `E_μ[k vv^T]`, entropy | `d=3`, `k=(3,−1,1,1)`, `E_μ[k]=1`, `K=3`, `E_μ\|k\|=3/2`, `E_μ[k vv^T]=v_1v_1^T` exactly, entropy `= log2 − ½log3 = 0.1438… ≤ log(4/3) = 0.2877… ≤ log3`. All artifact digits correct. |
| A's / D's counterexample: `μ = ½(δ_{e_1}+δ_{e_2})` on `S^1` | `d=2`, `k=(2,0) ≥ 0`, `E_μ[k]=1`, `K=2=d` (so Lemma 3 admits `v_0=e_1`), `E_μ\|k\|=1`, `c=1`, `E_μ[k vv^T]=e_1e_1^T`. Valid; `μ` is not a point mass. |
| C's counterexample: `μ` uniform on `{±e_1,±e_2}` | `d=2`, `k=2·1_{\{±e_1\}} ≥ 0`, `E_μ[k]=1`, `K=2=d`, `E_μ[k vv^T]=e_1e_1^T`. Valid. |
| E's counterexample: antipodal support, `μ = ⅓δ_{v_0}+⅔δ_{−v_0}` | `d=1`, `k ≡ 1 ≥ 0`, `K=1`, `E_μ[k vv^T]=v_0v_0^T`. Valid. |
| `E_μ\|k\| = K^{1/2}` "in general" | FALSE: `3/2 ≠ √3` in the artifact's own example. |
| The true replacement witness (`μ` uniform on `S^{n−1}`), `n=2` | `k = 4cos²θ − 1 = 1 + 2cos2θ`; `E_μ[k]=1`, `K=k(0)=3=d`, `E_μ[k cos²]=1`, `E_μ[k·cosθ sinθ]=0`, `E_μ[k sin²]=0`, `E_μ\|k\| = 1/3 + 2√3/π = 1.43599… > 1`. Genuinely signed. General `n`: `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2`, `E_μ[k]=1`, `E_μ[k vv^T]=v_0v_0^T`, `k(v_0)=n(n+1)/2`, negative on `{⟨v,v_0⟩² < 1/(n+2)}` of measure `1−o(1)`. Confirmed. |
| Corollary calculus `max_{x>0}(log x)/x^δ = 1/(eδ)` | Confirmed symbolically (`δ = 1/7` → `7/e = 2.5751…`). `n(n+1)/2 ≤ n²` for `n ≥ 1`; `n=1` gives `log 1 = 0`. Corollary sound. |
| Remark A's criterion `Σ_{i≥2}λ_i² ≤ (ε²/(1−ε²))λ_1²` | Algebraically identical to the discriminant condition `s_1² ≥ (1−ε²)‖M‖_F²`; both roots positive for `M ≠ 0`. Sound as stated for `ε ∈ (0,1)`. |

(Incidental, not an artifact defect: pass E's closed form for the uniform-`S^1`
value, "`2/3 + 2√3/π ≈ 1.4359`", is a typo — the closed form is `1/3 + 2√3/π`;
E's numeric value `1.4359`, and hence E's `c ≈ 0.6964` and entropy bound
`≈ 0.375`, are correct. Nothing follows for the artifact.)

## Findings and rulings

| # | finding (quoted locus) | passes raising | ruling | minimal repair | load-bearing? |
|---|---|---|---|---|---|
| F1 | The universal claim that the construction's output is signed: Proof plan, "Cancellation enters through `k`, which takes both signs unless `μ` is a point mass"; Remark C.1, "Our `r` takes both signs unless `μ` is a point mass"; Remark C.2, "Our `r` is not flat and not nonnegative, so it names no submatrix" | A (C.1 and C.2), C (C.1), D (Proof plan and C.1), E (C.1) | **UPHELD** | Delete the universal claim at all three loci and replace with the true conditional the artifact already proves — "`k` is negative somewhere whenever `E_μ\|k\| > E_μ[k] = 1`" — plus, if a positive statement about the hard measures is wanted, the verified witness `μ` uniform on `S^{n−1}`, where `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2` is negative on a set of measure `1−o(1)`. In C.2, the conclusion ("names no submatrix, Theorem 2.4 untouched") must be re-grounded on the *absence of a flatness guarantee* for the construction, not on a false universal claim that `r` is never flat: in the two-point example `r = 2·1_{\{e_1\}}` is both nonnegative and flat. | **No** — Proof plan prose and Remark C only. No lemma, the Theorem, the Corollary or Corollary B invokes signedness. Deleting all three sentences leaves the Contract proof untouched. |
| F2 | Remark C.1, "the kernel `k` has `E_μ[k] = 1` but `E_μ\|k\| = K(v_0,v_0)^{1/2}` in general" | A, C, D, E | **UPHELD** | Replace `=` with `≤` (Lemma 2(iii), Cauchy–Schwarz, equality iff `\|k\|` is `μ`-a.e. constant), or delete the clause with F1. | **No** — commentary. |
| F3 | Lemma 1(b) closing clause, "Well-definedness of `ev_v` follows, since two representatives of the same class agree `μ`-a.e., hence at `v ∈ supp μ`" | C (as routine) | **UPHELD** (wording only) | One-clause rewrite: well-definedness holds because two *quadratic-form* representatives of the same class agree on `supp μ` (the displayed statement of (b)), and `ev_v` is defined through quadratic-form representatives only. As literally written the clause is false — an `L²(μ)` class contains representatives differing at the single point `v`. | Touches the *text* of load-bearing Lemma 1(b), **but not its content**: the displayed statement and its proof are correct as given, and nothing downstream changes. Does not put the Contract proof in doubt. |
| F4 | Pass B's clearance of Remark C.1: "the artifact's `r` is shown genuinely signed (`E_μ\|k\| > E_μ[k]` whenever `μ` is not a point mass)" | B (as an affirmative clearance) | **OVERRULED** | None on the artifact. Recorded so the reviser does not treat Remark C.1 as cleared: the parenthetical is exactly the false claim of F1, refuted by three exactly verified counterexamples above. | n/a |
| F5 | Remark C.1, "concerns *deficient*, i.e. nonnegative, reweightings" — the equation "deficient = nonnegative" is not on card S1 | A (class C), E (class D/E, with a source request) | **NEEDS SOURCE** | Leaves the revision loop. Card S1 quotes Theorem 2.3 (Q2) using the undefined term "deficient" and defines only "flat" (Q4). Add BKS Definition 2.2 (≈ p. 5) verbatim to the card. E reports having checked it independently and found the artifact's gloss factually correct; that check is outside the card and cannot be substituted for it. The reviser must NOT be asked to argue around this. | **No** — Remark C.1 only. |
| F6 | Corollary B: (P1) / second countability of the ambient `X` never re-checked when the transfer is claimed "verbatim" | A (class C) | **PEDANTIC** | Note only. `X = \{ab^T : ‖a‖=‖b‖=1\}` is the continuous image of `S^{n−1}×S^{n−1}`, hence compact and second countable; C and D both fill it in one line. | No |
| F7 | Corollary B cosmetics: `G` called an "affine space" while used as a linear subspace; `c ∈ (0,1]` asserted without the one-line reason (`1 ∈ G ⇒ E_μ\|k\| ≥ 1`) | A (class C) | **PEDANTIC** | Note only; both statements are true as used. | No |
| F8 | Lemma 3 parenthetical, "off the support nothing below uses `g`" | C (class C) | **PEDANTIC** | Note only. `A := \{g ≤ d\}` is indeed defined globally, but only `μ(A)` and `A ∩ supp μ` are used, and `μ(supp μ) = 1` makes both independent of off-support values of `g`; C itself concedes the claim survives. | No |
| F9 | `d ≥ 1` and `supp μ ≠ ∅` never recorded | C (class C) | **PEDANTIC** | Note only; both immediate (`μ(supp μ)=1 ⇒ supp μ ≠ ∅`; `[1]=[q_I] ≠ 0` in `L²(μ) ⇒ d ≥ 1`). | No |
| F10 | DEPENDENCIES: the footnote-7 quotation labelled "verbatim" silently drops the card's closing sentence, with no ellipsis | C (hygiene), E (noted and dismissed) | **PEDANTIC** | Note only; add an ellipsis if the line is touched for other reasons. Footnote 7 is context, load-bearing for nothing; the omitted sentence, if anything, supports the artifact. | No |
| F11 | Remark C.3: broken indentation, final sentence of item 3 renders at top level | A (class C, cosmetic) | **PEDANTIC** | Note only; typographic. | No |

Sub-threshold observations that I do not count as findings, recorded for
completeness: A's step 15 notes that the Lemma 4 sharpness "iff" is asserted
rather than derived and explicitly places it beneath the reporting threshold — I
agree, the note is correct and unused. E's two refutation attempts against the
Theorem (discrete 4-point and continuous uniform `S^1`) both failed; I
reproduced both and they fail, which is corroboration of the Theorem, not a
finding. B's "informational" row on the over-strength of the result (`O(log n)`
entropy, `ε`-free constant) raises no defect and I confirm no drift: `C = 2/(eδ)`
is produced from `δ` alone, before `n` and `μ`, exactly the Contract's
`∀ε ∀δ ∃C ∀n ∀μ` order.

**Class A (statement drift).** All five passes ran the drift check first and all
five found none; I re-ran the diff against the Contract's three reading
conventions and agree. Convention 1: `C(ε,δ) = 2/(eδ)` is independent of `n` and
`μ` and is fixed before them; a constant that happens not to depend on `ε` is an
admissible instance of `C(ε,δ)`, not a violation. Convention 2: the witness `r`
is bounded and continuous, i.e. *more* regular than the floor — the Contract
forbids *assuming* extra regularity of an arbitrary `r`, not delivering a nice
witness. Convention 3: a PSD symmetric witness `L` is a legitimate special case
of "nonzero rank one", and Remark A (verified) shows the relative-error clause is
not satisfied degenerately, since `‖L‖_F = c ≥ (n(n+1)/2)^{−1/2} > 0` and `M = 0`
admits no `L` at all. Therefore no class-A finding exists to rule on, and the
class-A rule (never PEDANTIC) is not engaged.

## Question 1 — does any UPHELD finding touch a load-bearing step?

**No.** Nothing the referees found puts the proof of the Contract statement in
doubt.

* F1 and F2 are confined to the Proof plan's closing sentence and to Remark C.1
  and C.2. These are scope and motivation commentary; no lemma, the Theorem, the
  Corollary or Corollary B cites them, and signedness of `r` is nowhere a
  hypothesis of anything. Deleting the Proof plan's last sentence and Remark C.1
  and C.2 outright would leave the Theorem and Corollary exactly as strong as
  they are now.
* F3 is a false sentence *inside* load-bearing Lemma 1(b), so it is not purely
  commentary and must be fixed; but the mathematics of Lemma 1(b) — its displayed
  statement and its proof, which four passes and I checked independently — is
  correct, and the repair is a rewording that changes no quantifier, no
  hypothesis and no downstream step.
* F5 is not a mathematical defect at all and never reaches the reviser.

So: all UPHELD findings are either deletable commentary (F1, F2) or a
sentence-level rewrite in a lemma whose content is sound (F3). The Contract
statement remains proved, with entropy `≤ log(n(n+1)/2)`, exact rank one, and
`C(ε,δ) = 2/(eδ)`.

## Question 2 — for each UPHELD finding, what kind of repair?

| # | kind of minimal repair |
|---|---|
| F1 | **Weakening of an over-strong claim** (equivalently, deletion). A universal claim is replaced by the conditional the artifact already proves; optionally accompanied by the uniform-sphere witness, which I have verified, so even the optional part is *not* a substantive new argument. C.2's conclusion must be re-grounded, which is a re-wording of the reason, not a new proof. |
| F2 | **Deletion**, or a one-character weakening (`=` → `≤`). |
| F3 | **Weakening / restatement** of one clause. No new argument. |

No UPHELD finding requires a substantive new argument.

## Revision instructions (UPHELD only, in order)

1. **Proof plan, final sentence.** Delete "Cancellation enters through `k`, which
   takes both signs unless `μ` is a point mass." Replace, if a sentence is wanted
   there, with: "Cancellation is available through `k`, which is negative
   somewhere whenever `E_μ|k| > E_μ[k] = 1`." Do not assert that this holds for
   every non-point-mass `μ`; it does not.
2. **Lemma 1(b), final clause.** Rewrite "Well-definedness of `ev_v` follows,
   since two representatives of the same class agree `μ`-a.e., hence at
   `v ∈ supp μ`" so that it says what (b) actually proves: any two
   *quadratic-form* representatives of a class of `F_μ` agree at every
   `v ∈ supp μ`, and `ev_v` is defined via quadratic-form representatives, so it
   is well defined on classes. Do not claim that arbitrary `L²(μ)`
   representatives agree at `v`. Nothing else in Lemma 1 changes.
3. **Remark C.1, quantitative clause.** Delete "`E_μ|k| = K(v_0,v_0)^{1/2}` in
   general" or change the equality to the inequality `E_μ|k| ≤ K(v_0,v_0)^{1/2}`
   of Lemma 2(iii), noting equality holds iff `|k|` is `μ`-a.e. constant.
4. **Remark C.1, headline claim.** Delete "Our `r` takes both signs unless `μ` is
   a point mass." The "no conflict with the paper's tightness claim" conclusion
   must be re-grounded on either (i) the true conditional of instruction 1, or
   (ii) the fact that the source's negative result is a worst-case statement over
   `μ`, together with the verified hard-instance computation: for `μ` uniform on
   `S^{n−1}`, `k(v) = (n(n+2)/2)⟨v,v_0⟩² − n/2` is negative on
   `{⟨v,v_0⟩² < 1/(n+2)}`, of `μ`-measure `1 − o(1)`. Option (ii) is the stronger
   remark and is fully verified; either is acceptable.
5. **Remark C.2, first clause.** Delete "Our `r` is not flat and not nonnegative,
   so it names no submatrix" and re-ground the (correct) conclusion on the
   absence of any flatness guarantee for the construction: the dictionary of §2.2
   applies only to flat reweightings, and the Theorem supplies no flatness, so it
   names no submatrix and Theorem 2.4's dual form is untouched. Do not claim that
   `r` is never flat or never nonnegative — for `μ = ½(δ_{e_1}+δ_{e_2})` the
   construction outputs `r = 2·1_{\{e_1\}}`, which is both.

Items 1, 3, 4 and 5 may alternatively be discharged by deleting the Proof plan's
final sentence and all of Remark C.1 and C.2; the Theorem, the Corollary and
Corollary B are unaffected either way. Nothing else in the artifact is to be
touched on account of this triage. In particular the PEDANTIC items F6–F11 are
explicitly *not* to consume a revision.

## Escalation list (to the human)

None. No finding in any of the five passes is UNCLEAR: every disputed claim
reduced to a finite computation, and every such computation was carried out in
exact arithmetic above.

## SOURCE REQUEST (consolidated)

One item, from finding F5 (raised by A and E; E's out-of-card web check is not a
substitute for the card).

* **Source:** Barak, Kothari, Steurer, *Quantum entanglement, sum of squares, and
  the log rank conjecture*, arXiv:1701.06321v2.
* **Needed:** the verbatim definition of "`k`-deficient reweighting" —
  Definition 2.2, approximately p. 5 — reported to read "we say that a
  probability distribution `μ′` is a `k`-deficient reweighting of `μ` if
  `Δ_KL(μ′‖μ) ≤ k`".
* **Why:** card S1 quotes Theorem 2.3 (Q2) using the term "deficient" but never
  defines it, and defines only the distinct term "flat" (Q4). Remark C.1's gloss
  "deficient, i.e. nonnegative" is therefore unverifiable from the card as
  supplied. Adding this quotation to card S1 settles it.
* **Impact if unsupplied:** confined to Remark C.1's scope commentary. The
  Theorem, the Corollary and Corollary B do not use the term, and the artifact's
  own DEPENDENCIES section correctly records the source as load-bearing only for
  the claim that the Theorem answers Question 8.1 — which card item Q1 supports
  verbatim.
