# TRIAGE RULING — 0048-RKHS-1-r6 (round 6)

Handling editor. Record ruled on: `CONTRACT.md`, card `S1-bks-q81-card.md`, the
grounding result `S1-quote-grounding.md`, the artifact `0048-RKHS-1-r6.md`, and
the five round-6 referee reports A–E. Adjudicated on the mathematics alone;
referee verdict labels and stated confidence carry no weight. Every disputed
claim that was mechanically checkable was independently re-derived (not taken
on any referee's word), and the one substantive dispute (B vs. E, over the
new Remark C(i) Corollary-B paragraph) was resolved by my own close reading of
the artifact text against the card items it cites and against the Contract's
own Definition — not by picking a side on authority or referee confidence.

## DISPOSITION

Referees A, C, D, E returned CLEAN (Class-D nits only, several of them
already-catalogued repeats from the round-3 triage: F5 "L² norm" unsquared,
F9 the `k(−v_0)=k(v_0)` misattribution, F13 the Q1 whitespace nit). Referee B
returned DEFECTS on the single new sentence added this round — the closing
line of the new Corollary-B paragraph in Remark C(i):

> "So whenever Corollary B's construction returns a nonnegative `r`, that `μ`
> is, by exactly this argument, not a hard instance for the nonnegative
> version of Theorem 2.3 either."

B's claim: this silently (i) transfers a conclusion proved only on Corollary
B's unit-Frobenius-norm domain `X` onto Theorem 2.3's unrestricted domain
(Q2: "any distribution over rank one `n × n` matrices"), and (ii) swaps the
artifact's own signed-`r` entropy formalism for BKS's KL-divergence
"k-deficient reweighting" formalism (Q9), with no citation or derivation
bridging either gap.

**B's finding is OVERRULED.** On my own re-derivation, both of B's premises
fail.

**(a) No domain transfer occurs, because there is nothing to transfer.**
`X := {X ∈ R^{n×n} : rank X = 1, ‖X‖_F = 1}` is not a different domain from
Theorem 2.3's; it is a strict *subset* of it. Q2's verbatim text places no
restriction whatsoever on the norm or scale of the rank-one matrices `µ`
ranges over ("any distribution over rank one `n × n` matrices"), so every
Borel probability measure `μ` on `X` — Corollary B's own object — already
*is*, without any further argument, a distribution over rank one `n×n`
matrices, i.e. a legitimate instance of Theorem 2.3's own stated domain. A
claim about a specific instance that happens to live inside the general
domain is not a claim about "the domain" and requires no domain-transfer
lemma, no citation of Q8, and no invocation of scale-invariance — unlike the
defect pattern the task asked me to check for (a clause asserting that the
unit-Frobenius set `X` *is* "the domain Theorem 2.3 ... is stated over," which
would misattribute Theorem 2.3's own general hypothesis to Corollary B's
narrower one). I searched the artifact for that pattern and it is absent: the
Corollary B statement itself is explicit that `X`'s unit-Frobenius
normalisation is "the normalisation used in the source paper's *intended
application*" (quoting Q8's own "This restriction is easy to lift and anyway
holds automatically in our intended application"), never that it is Theorem
2.3's stated domain. The disputed sentence in Remark C(i) says only that
*this particular* `μ` (an object that is, by construction, both an instance
of Corollary B's `X` and, automatically, an instance of Theorem 2.3's general
domain) is not a hard instance — a claim about one point of the general
domain, not about the domain as a whole. That is exactly the "related-but-
distinct" possibility flagged by the task, and it is not present in this
artifact's actual text: the r6 paragraph contains neither the parallel
branch's flagged clause (Corollary B's domain "the domain Theorem 2.3 ... [is]
stated over") nor a covert equivalent of it.

**(b) No formalism swap occurs, because the Contract's own Definition already
identifies the two formalisms for nonnegative `r`.** `CONTRACT.md`'s
Definition section states, verbatim: "If in addition `r ≥ 0` holds `μ`-almost
everywhere, then `r` is a *nonnegative* reweighting; in that case
`dμ' := r dμ` is a probability measure and the entropy cost is exactly the
Kullback–Leibler divergence `Δ_KL(μ'‖μ)`." This is not an artifact
invention; it is the Contract's own bridge, fixed before either the artifact
or Corollary B was written, and it is *exactly* Q9's definition of a
`k`-deficient reweighting (`Δ_KL(µ′‖µ) ⩽ k`, defined only for `µ′` a
probability distribution — i.e. for nonnegative reweightings). So "entropy
cost ≤ log(n²+1) for a nonnegative reweighting of `μ`" and "a
`log(n²+1)`-deficient reweighting of `μ`" are the same statement under a
definition already on file, not a silent substitution invented in Remark
C(i). Given (a) and (b), the sentence B objects to is a correctly-scoped,
fully-licensed observation, not an unjustified leap: this `μ` (an instance
of Theorem 2.3's general domain, admitting a deficient/nonnegative
reweighting of cost `O(log n)` whenever the sign condition holds) is not a
hard instance for Theorem 2.3's nonnegative case — consistent with, and not
contradicting, Q5's tightness remark, which concerns the worst case over
*all* `μ`, not this one. This is, in substance, the identical argument the
round-3 triage's own COMPUTATION 1 already ran and certified (down to using
this same closing sentence, word for word, as part of the verified
derivation the round-3 ruling directed the reviser to reproduce) — so this
round's referee dispute is, on inspection, a dispute over whether an
already-verified derivation's own stated conclusion is itself sound, and it
is.

**E's CLEAN read is therefore correct: "accurately scoped as motivating an
artifact-internal construction, not as a restatement of Theorem 2.3 over that
domain."** B's read mistakes a claim-about-one-instance for a claim-about-a-
domain, and mistakes a Contract-level definitional identity for an
unsupported bridge.

Twelve minor Class-D findings across A, C, D, E — repeats of already-
catalogued items (F5, F9, F13 from the round-3 triage) and a small number of
new but equally cosmetic verbatim-quotation nits — touch nothing load-bearing.
I rule **0 UPHELD, 1 OVERRULED, 7 PEDANTIC (deduplicated), 0 NEEDS SOURCE, 0
UNCLEAR.**

The artifact required no revision this round; none is ordered.

## RECOMPUTATIONS PERFORMED FOR THIS RULING

### RECOMPUTATION 1 (the B-vs-E dispute: is the Corollary-B reconciliation sentence a domain/formalism overreach?)

Checked directly against the two source items in play.

* **Q2 (Theorem 2.3), verbatim:** "Let `µ` be any distribution over rank one
  `n × n` matrices and `ε > 0`." No norm, scale, or Frobenius-norm hypothesis
  appears anywhere in this sentence. `X` (Corollary B's domain,
  unit-Frobenius-norm rank-one matrices) is a subset of "rank one `n×n`
  matrices" full stop, so `μ` supported on `X` is, without further argument, a
  distribution over rank one `n×n` matrices — an instance of Q2's domain, not
  an object outside it requiring translation.
* **Q9 (Definition 2.2), verbatim, plus card's own explanatory note:**
  "`µ′` is a `k`-deficient reweighting of `µ` if `∆_KL(µ′‖µ) ⩽ k`," and "a
  `k`-deficient reweighting is by definition nonnegative ... and normalised."
* **Contract Definition (independent of the artifact and of both referees):**
  "If in addition `r ≥ 0` holds `μ`-almost everywhere, ... the entropy cost is
  exactly the Kullback–Leibler divergence `Δ_KL(μ'‖μ)`." I re-derived this
  identity is exact, not approximate: for `r ≥ 0` with `E_μ[r]=E_μ|r|=1`,
  `dμ':=r\,dμ` is a probability measure with Radon-Nikodym derivative `r`, so
  `Δ_KL(μ'‖μ) = E_{X∼μ'}\log(dμ'/dμ)(X) = E_{μ'}[\log r] = E_μ[r\log r]` —
  literally the artifact's own "entropy cost" quantity. Hence "entropy cost
  ≤ K" for nonnegative `r` and "`K`-deficient reweighting" (Q9) name the same
  object, by a chain that runs entirely through the Contract, before any
  artifact text is written.

Combining these two facts: the disputed sentence asserts, for a `μ`
supported on `X` (hence automatically inside Theorem 2.3's domain) for which
Corollary B's own construction happens to return `r ≥ 0`, that a nonnegative
reweighting of cost `≤ log(n²+1)` exists reaching `X_0` exactly — i.e., that
this `μ` admits a `log(n²+1)`-deficient reweighting reaching an exact
rank-one match, in Q9's own vocabulary, established by Q9 as identical to the
artifact's nonnegative-entropy-cost claim via the Contract's Definition.
That is a correct, internally-derived instance-level statement about a
`μ` that is, by construction, inside Theorem 2.3's stated domain. No
citation gap and no domain transfer exist to fill; there is nothing left to
bridge. **B's finding does not survive independent re-derivation; OVERRULED.**

### RECOMPUTATION 2 (checking for the parallel-branch's flagged defect pattern, verbatim)

The task flagged that a parallel revision branch's r4 was faulted (3/5
referees) for a clause describing Corollary B's domain as "the domain
Theorem 2.3 and the tightness claim of Q5 are stated over" — a false
domain-equivalence claim, since Q2 places no norm restriction on Theorem
2.3's domain. I grepped the r6 artifact's Corollary B statement and the new
Remark C(i) paragraph for any form of this claim. It is absent: Corollary
B's statement calls `X`'s normalisation "the normalisation used in the
source paper's intended application (§2.3: ...)" — attributing the
restriction to Q8 (the paper's own convenience convention for its intended
application), never to Theorem 2.3's stated hypotheses — and the new Remark
C(i) paragraph never characterises `X` as Theorem 2.3's domain at all; it
only asserts a scoped, instance-level, "not a hard instance" conclusion, per
RECOMPUTATION 1. So the r6 paragraph contains **neither** the parallel
branch's defect nor a disguised form of it. (I note, separately and only for
completeness, that the round-3 triage's own COMPUTATION 1 narrative — not the
artifact — once used loose language, "the domain Theorem 2.3 ... [is]
actually stated over," to describe Corollary B's domain in its DISPOSITION
prose; that phrasing does not appear in the artifact under review and is not
before me to rule on this round, since only the artifact and this round's
five reports are the input to this ruling. I flag it below for the human,
out of caution, since it is the same imprecise locution that sank the
parallel branch, even though it never made it into any artifact text here.)

### RECOMPUTATION 3 (spot-check of the load-bearing chain, unchanged this round)

None of the five reports disputes any load-bearing step (Lemmas 1–4, the
Theorem, the Corollary, Remark A, Corollary B's own statement/proof); all
five independently re-derived the new paragraph's arithmetic
(`E_{μ'}‖X−X_0‖_F² = 1 − 2⟨X_0,X_0⟩ + 1 = 0`) and it is correct — I re-checked
it a sixth time by the same bilinear expansion and it is exact. Since this
round's artifact is `r3` plus one additive, non-load-bearing paragraph, and
the round-3 triage already independently re-derived and numerically
spot-checked (COMPUTATION 1/2 of that ruling) every load-bearing step and the
identical arithmetic now appearing in the artifact, no further re-derivation
of Lemmas 1–4/Theorem/Corollary/Remark A/Corollary B's body was required
beyond confirming (which I did, by reading) that none of it changed a single
byte relative to `r3.md`, as the artifact's own header and REVISION LOG
claim and as all five referees independently confirmed.

## TABLE OF DISTINCT FINDINGS

| # | Finding (deduplicated) | Class | Passes raising it | Ruling | Minimal repair | Load-bearing? |
|---|---|---|---|---|---|---|
| G1 | New Remark C(i) closing sentence ("...not a hard instance for the nonnegative version of Theorem 2.3 either") allegedly transfers Corollary B's unit-Frobenius-domain conclusion onto Theorem 2.3's unrestricted domain, and swaps the artifact's signed-entropy formalism for Q9's KL-deficient formalism, without derivation or citation | Class B framing by the referee (unjustified step / scope overreach) | B (DEFECTS) | **OVERRULED** — see RECOMPUTATION 1: `X` is a subset of, not a departure from, Theorem 2.3's stated domain (Q2 places no norm restriction), so an instance-level claim about a `μ` on `X` requires no domain-transfer argument; and the Contract's own Definition already identifies nonnegative-`r` entropy cost with `Δ_KL(μ'‖μ)`, i.e. with Q9's "deficient reweighting" exactly, so no formalism gap exists either. E's CLEAN read of the same sentence is the one that survives independent re-derivation. | None — no repair needed; the sentence is correct as written. | No (Remark C is scope commentary), but the finding itself, had it been correct, would not have been load-bearing either — moot given OVERRULED. |
| G2 | Proof plan: "Its `L²` norm averages to `d`" should be "squared `L²` norm" | typo-level | A (repeat of round-3 F5) | **PEDANTIC** | Insert "squared"; Lemma 3 itself is stated correctly. | No |
| G3 | Remark C(i), pre-existing sphere-case paragraph: "`k(−v_0)=k(v_0)=K(v_0,v_0)` by Lemma 1(c)" attributes evenness of the quadratic-form representative to Lemma 1(c), which only supplies `k(v_0)=K(v_0,v_0)` | mis-attribution | A, C, D (repeat of round-3 F9) | **PEDANTIC** | Split the citation: evenness is a property of the representative; `k(v_0)=K(v_0,v_0)` is Lemma 1(c). Conclusion unaffected. | No |
| G4 | DEPENDENCIES, Question 8.1 quotation: card has a space before the closing `?`, artifact's rendering does not | typographic | A (repeat of round-3 F13) | **PEDANTIC / not scored** | None required; `pdftotext`-layout noise, no clause altered. | No |
| G5 | COROLLARY B statement, the embedded Q8 quotation begins lower-case "we will restrict..." where the card (and the separate DEPENDENCIES copy) has capital "We"; a mid-sentence splice conventionally lowercases the lead word of an integrated quotation | typographic / stylistic | A | **PEDANTIC** | Optional: capitalize and bracket, `[W]e`, if the section is touched for other reasons; not required, since the DEPENDENCIES copy already preserves the verbatim capitalization and the embedded copy is grammatically integrated, a standard convention rather than a fidelity break. | No |
| G6 | DEPENDENCIES, Q5 and Q6 quotations: nested quotation marks rendered as single quotes (`'close to rank one'`, `'approximate'`) where the card/PDF use double quotes | typographic | D, E (Q5 also independently logged in `S1-quote-grounding.md` as "cosmetic only") | **PEDANTIC** | None required; no wording or scope change, a plain-text nesting workaround. | No |
| G7 | Proof of the Theorem: the one-line fact "bounded Borel function on a probability space is in `L²`" is used (to invoke Lemma 4) but not spelled out at the point of use | trivial omission | C | **PEDANTIC** | Optional: add one clause noting boundedness ⟹ `L²(μ)` for a probability measure `μ`. Not required; trivial. | No |

No finding of Class A (statement drift) was raised by any of the five
passes this round, and my own quantifier-by-quantifier diff of the Theorem
and Corollary against the Contract's `∀ε∀δ∃C∀n∀μ∃r,L` and Reading Conventions
1–3 found none either — all five referees agree the artifact proves a strict
*strengthening* (exact match, `ε=0`, `O(log n)` entropy, `ε`-independent
constant) in the Contract's own quantifier order, and I concur. No finding
was raised, or is warranted, as NEEDS SOURCE: G1's resolution required only
the Contract's own Definition and the card's own verbatim text for Q2/Q9,
both already on file; nothing here needed a new source. G1, the one
disputed finding, is resolved on the mathematics (RECOMPUTATION 1), not by
authority — B's referee framing is overruled on its merits, not because E
outvoted B or expressed more confidence.

## ESCALATION LIST (to the human)

**Empty for this round's five reports.** No finding from A–E is UNCLEAR.
G1 (the only substantive dispute) is resolved by direct textual and
definitional check, not left open.

One item is flagged for the human's attention as **context, not as a finding
of this round**: the round-3 triage ruling's own DISPOSITION prose (not the
artifact) once described Corollary B's domain as "the domain Theorem 2.3 and
its tightness claim Q5 are actually stated over" (`0048-RKHS-1-r3-triage.md`,
line ~45) — the same imprecise locution (domain-of-`X` conflated with
domain-of-Theorem-2.3) that, in a parallel branch's artifact text, drew
correct fault from 3/5 referees. It never made it into any artifact text in
this lineage (the r6 artifact under review here correctly attributes the
unit-Frobenius restriction to Q8's "intended application" gloss, not to
Theorem 2.3's stated hypotheses, per RECOMPUTATION 2), so it is not a defect
in `0048-RKHS-1-r6.md` and is not ruled on here. It is noted only because a
future round's Remark-C drafting, if it ever leans on that triage sentence
verbatim rather than on the card's own Q2 text, would reproduce the parallel
branch's actual error. No action is required now.

## CONSOLIDATED SOURCE REQUEST

**None.** No finding this round requires an external source; card S1
continues to require no repair (per `S1-quote-grounding.md`, already fully
discharged in `r3`'s revision). G1's resolution used only material already
on file (Contract's Definition, card items Q2 and Q9).

## REVISION INSTRUCTIONS

**None.** No finding was UPHELD this round. The seven PEDANTIC items (G2–G7,
deduplicated) must not consume a revision, per the same standard applied in
the round-2 and round-3 rulings; any of them may be folded into a future
revision opportunistically, but none is a blocking defect, and the artifact
requires no edit to close round 6.

## TALLY

0 upheld / 1 overruled / 7 pedantic / 0 needs-source / 0 unclear

### END OF TRIAGE RULING [0048-RKHS-1-r6] ###
