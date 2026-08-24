# Blind referee report — angle: STATEMENT-DRIFT-AND-SCOPE
Artifact reviewed: `c/0048/campaign/intermediates/0048-RKHS-1-r6.md`
Contract: `c/0048/campaign/CONTRACT.md`
Source card: `c/0048/campaign/sources/S1-bks-q81-card.md`

## STEP 0 — Completeness gate

The artifact contains the line `### END OF ARTIFACT [0048-RKHS-1-r6] ###` (line 441),
followed only by a REVISION LOG section, which is bookkeeping, not mathematical
content. The artifact is not truncated. Proceeding to full review.

## Statement actually proved, vs. the Contract

Contract's statement, in my own words: ∀ε>0 ∀δ>0 ∃C=C(ε,δ)<∞ (not depending on
n or μ) ∀n∈N ∀ Borel prob. measure μ on S^{n-1} ∃ signed reweighting r of μ with
entropy cost ≤ C·n^δ and ∃ nonzero rank-one L with ‖E_μ[r vv^T] − L‖_F ≤ ε‖L‖_F.

Artifact's THEOREM proves, for every n≥1 and every Borel probability measure μ
on S^{n-1} (no restriction), the existence of v_0 ∈ supp μ and a signed
reweighting r with **exact** equality E_μ[r vv^T] = c·v_0v_0^T (so the
Frobenius error is identically 0, hence ≤ ε‖L‖_F for every ε>0) and entropy
cost ≤ log(n(n+1)/2). The COROLLARY packages this as C(ε,δ) = 2/(eδ),
independent of ε. This is a strictly stronger claim than the Contract's (it
gives ε = 0 and a bound that beats every C·n^δ, δ>0, for large n), proved over
exactly the Contract's domain (unrestricted μ, unrestricted n) and in the
Contract's own quantifier order (the constant is shown independent of both n
and μ, matching CONTRACT.md's Reading Convention 1). I find **no drift** in
the core Theorem/Corollary against the Contract's statement: it is a
legitimate, not silently narrower, substitute — if anything a strictly
stronger one, and the strengthening is explicit, not hidden.

The GOAL section's restatement of the claim also matches the Contract
verbatim in substance (same definition of signed reweighting, same
quantifiers, same "independent of n and μ" requirement). No drift there
either.

## Scope claims tied to source-card items (Q1–Q9): domain-misattribution check

I went through every place the artifact invokes Q1–Q9 and checked the
artifact's characterization of each cited result's domain/hypothesis against
the card's verbatim text.

* Q1 (Question 8.1) — used only to state the Contract's own target; domain
  (distributions over S^{n-1}) matches exactly. No drift.
* Q2 (Theorem 2.3) — the card's verbatim quote states this **without any
  Frobenius-norm restriction**: "Let µ be any distribution over rank one
  n × n matrices and ε > 0." The artifact's REMARK C(i) correctly reports
  Theorem 2.3's tightness (Q5) as being about *deficient* reweightings
  (Q9-nonnegative), without asserting any norm restriction on Theorem 2.3's
  own domain. No misattribution there.
* Q4 (flat distributions), Q5 (tightness), Q6/Q7 (footnotes), Q9
  (deficient = nonnegative) — all quoted and used consistently with the
  card's own text; I found no case where the artifact attributes a domain,
  hypothesis, or scope to these that the verbatim quotation does not support.
* Q8 (§2.3 unit-norm-columns normalisation) — this is the one item where a
  domain-narrowing move happens, and it is used correctly at first: Corollary
  B explicitly quotes Q8's own parenthetical ("This restriction is easy to
  lift and anyway holds automatically in our intended application") when it
  restricts its own new domain `X` to unit-Frobenius-norm rank-one matrices.
  The artifact does **not** claim this is the domain that Theorem 2.3 (Q2) is
  literally stated over — it is transparent that Q8's normalisation is "the
  normalisation used in the source paper's intended application," not a
  hypothesis of Theorem 2.3 itself. Corollary B is explicitly derived as an
  analogue of the *artifact's own* Theorem (via "Run Lemmas 1–4 verbatim ...")
  and not as a special case of Theorem 2.3. **This particular pattern — the
  one the task asked me to hunt for — is not present at the point where Q8 is
  first invoked.**

## The finding: a real domain/formalism misattribution, in the r6-added paragraph

However, the same restricted domain resurfaces in a way that *does* trip the
pattern, in the one paragraph that is new in this revision (the second new
paragraph of REMARK C(i), the Corollary-B analogue of the sphere-case
reconciliation):

> "So whenever Corollary B's construction returns a nonnegative `r`, that `μ`
> is, by exactly this argument, not a hard instance for the nonnegative
> version of Theorem 2.3 either."

Two things are conflated here that the card does not license conflating:

1. **Domain.** Corollary B's `μ` ranges only over
   `X := {X ∈ R^{n×n} : rank X = 1, ‖X‖_F = 1}` (the unit-Frobenius-norm
   slice, by Corollary B's own definition). Theorem 2.3, as quoted verbatim
   at Q2, is a statement about "any distribution over rank one `n × n`
   matrices" — an **unrestricted-norm** domain. The claim that a degenerate
   `μ` on the unit-Frobenius slice `X` is "not a hard instance ... for
   Theorem 2.3" implicitly asserts that the restricted-domain question and
   the general-domain question (Theorem 2.3's own, literal domain) are
   equivalent for purposes of "hardness." That equivalence is mathematically
   plausible (the problem is scale-invariant: relative Frobenius distance
   `ε‖L‖_F` doesn't care about the overall scale of the matrix), and Q8's own
   parenthetical ("this restriction is easy to lift") gestures at exactly
   this — but the artifact's new paragraph does not cite Q8, does not invoke
   scale-invariance, and does not otherwise justify the domain transfer
   anywhere in the derivation. As written, it is an unsupported leap from a
   claim about `X` to a claim about "Theorem 2.3" (whose card-quoted domain is
   strictly larger than `X`).
2. **Formalism.** Theorem 2.3's notion of reweighting is BKS's
   KL-divergence-based "`k`-deficient reweighting" of a *probability
   distribution* `µ′` (Q9: `∆_KL(µ′‖µ) ≤ k`, and "deficient" is *defined only
   for a probability distribution*, per the card's own editorial note). The
   artifact's Corollary B, by contrast, works throughout in its own
   "`E_μ[|r|\log|r|]`" signed-reweighting entropy formalism (the Contract's
   Definition, not BKS's Definition 2.2). In the *sphere*-case reconciliation
   paragraph (the pre-existing, untouched text), the phrase used is "not a
   hard instance for **the nonnegative question**" — carefully staying inside
   the artifact's own formalism and the Contract's own vocabulary (matching
   Question 8.1's domain and notion exactly, S^{n-1}, entropy of signed `r`).
   The new Corollary-B paragraph instead names BKS's actual, distinctly
   defined **Theorem 2.3** — a different formalism over a different (larger)
   domain — without ever building the bridge between "signed reweighting
   entropy cost ≤ log(n²+1) over `X`" and "KL-deficient reweighting of a
   probability distribution over all rank-one matrices" that such a claim
   would require.

Neither point is fatal to the artifact's resolution of the Contract: this
sentence sits inside REMARK C, which the artifact itself flags as
"not load-bearing" scope commentary, and it does not affect the Theorem,
Corollary, or Corollary B's own statement/proof, all of which are otherwise
untouched and (per my read) drift-free relative to the Contract. But the
artifact's REVISION LOG explicitly claims of this very paragraph that
"nothing is taken on the authority of a document outside this artifact,"
and its content is exactly the kind of domain-substitution the audit brief
asked me to check for: attributing to a general, card-quoted theorem
(Theorem 2.3, unrestricted-norm domain) a scope conclusion actually
established only for a narrower, artifact-invented sub-domain (`X`, the
unit-Frobenius slice), with no citation or internal derivation bridging the
gap.

## Other checks (no drift found)

* Quantifier order on the constant `C(ε,δ)`: correctly independent of `n`
  and `μ`, per Contract's Reading Convention 1 — verified in both the GOAL
  section and the Corollary's proof.
* `L` not required symmetric/PSD in the Contract (Reading Convention 3); the
  artifact's `L` happens to come out PSD, which is a strictly compliant
  special case, not a silent narrowing (the Contract permits, does not
  require, non-PSD `L`).
* Regularity of `r` (Borel measurable, μ-integrable, not required
  continuous/bounded) — the artifact's constructed `r` is bounded Borel,
  again a compliant special case, not an added hypothesis on the *input*
  (μ, n, ε, δ) side.
* Corollary B is presented as an additional, self-contained result about a
  different domain (matrices under Frobenius norm rather than vectors on the
  sphere) and is explicitly not needed to resolve the Contract's own
  conjecture (already fully resolved by the Theorem/Corollary over
  S^{n-1}); it does not narrow or replace the Contract's statement.

## ### FINDINGS ###

| Quoted location | Severity/class | Explanation |
|---|---|---|
| REMARK C(i), added paragraph: "...that `μ` is, by exactly this argument, not a hard instance for the nonnegative version of Theorem 2.3 either." | Class B (unjustified step / scope overreach, in the flavor of a domain misattribution) | Corollary B's `μ` ranges only over the unit-Frobenius slice `X`, while Theorem 2.3's card-verbatim domain (Q2: "any distribution over rank one `n × n` matrices") is unrestricted in norm; the sentence also silently switches from the artifact's own signed-reweighting entropy formalism to BKS's KL-divergence "deficient reweighting" formalism (Q9) without establishing any correspondence. Neither the domain-transfer (`X` → all rank-one matrices) nor the formalism-transfer (signed-`r` entropy → KL-deficient reweighting) is derived in the artifact or licensed by a card quotation; Q8's "easy to lift" remark, which would motivate the domain step, is not even cited here. This is precisely the pattern the audit brief calls "describing a sub-domain as the domain a general theorem is stated over," reoccurring in reverse (describing a sub-domain result as bearing on the general theorem). Confined to non-load-bearing REMARK C; does not affect the Theorem, Corollary, or Corollary B's own statement/proof, which correctly resolve the Contract. |
| Corollary B's own use of Q8 ("the normalisation used in the source paper's intended application (§2.3: ...)") | No defect | Correctly framed as the paper's own convenience convention, not as a hypothesis of Theorem 2.3; the card's parenthetical ("This restriction is easy to lift...") is quoted, not silently dropped. |
| THEOREM / COROLLARY vs. Contract statement | No defect (statement drift check passed) | Domain (all n≥1, all Borel μ on S^{n-1}), quantifier order (`C` independent of `n,μ`), and the Definition of signed reweighting all match the Contract; the proved result is a strict strengthening (`ε=0`, bound `O(log n)` beating every `C·n^δ`), not a narrower substitute. |

### VERDICT ###
STATUS: DEFECTS

One genuine but non-load-bearing defect was found: the paragraph added in
this revision to REMARK C(i) — the Corollary-B analogue of the sphere-case
reconciliation — claims that a degenerate `μ` on Corollary B's unit-Frobenius
domain `X` is "not a hard instance ... for Theorem 2.3," silently
transferring both the domain (unit-Frobenius-norm rank-one matrices `X`
versus Theorem 2.3's card-verbatim unrestricted-norm domain "any distribution
over rank one `n × n` matrices") and the formalism (the artifact's own
signed-reweighting entropy versus BKS's KL-divergence "deficient reweighting"
of Q9) without derivation or citation, in tension with the same paragraph's
explicit claim that "nothing is taken on the authority of a document outside
this artifact." This is exactly the domain-misattribution pattern the audit
was scoped to detect, though it occurs in scope commentary rather than in the
Theorem/Corollary that actually discharges the Contract. The core
THEOREM/COROLLARY were checked line-by-line against the Contract's
quantifier order (∀ε∀δ∃C∀n∀μ∃r,L, C independent of n and μ) and domain
(unrestricted Borel μ on S^{n-1}, all n≥1) and show no statement drift: the
proved result is a strict, explicitly-flagged strengthening of the Contract's
conjecture, not a silently narrower or differently-scoped substitute, and
every other invocation of card items Q1–Q9 accurately reflects the card's
verbatim text with no added or dropped hypotheses.
