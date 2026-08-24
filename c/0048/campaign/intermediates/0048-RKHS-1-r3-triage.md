# TRIAGE RULING — 0048-RKHS-1-r3 (round 3)

Handling editor. Record ruled on: `CONTRACT.md`, card `S1-bks-q81-card.md`, the
grounding result `S1-quote-grounding.md`, the artifact `0048-RKHS-1-r3.md`, and
the five round-3 referee reports A–E. Adjudicated on the mathematics alone;
referee verdict labels and stated confidence carry no weight. Every disputed
claim that was mechanically checkable was verified by direct computation
(exact algebra, and a numerical script where a concrete instance was useful),
not accepted on a referee's word.

## DISPOSITION

Referees A–D returned CLEAN; referee E returned DEFECTS on a single finding
(Remark C(i)'s reconciliation with the source's tightness claim, Q5). Quorum
(5/5 clean) was not met on this round, so a ruling is required before the round
can be closed.

The load-bearing chain — Lemma 1 → Lemma 2 → Lemma 3 → Lemma 4 → Theorem →
Corollary — is, on this record and on my own re-derivation of its two
crux steps (Lemma 1(b)'s well-definedness argument and Lemma 2(i)'s
reproducing identity), correct and proves the Contract statement in the
Contract's own quantifier order, with error exactly `0` and constant
`C(ε,δ) = 2/(eδ)` free of `ε`. All five referees independently ran a
class-A drift check first and found none; I re-ran the same diff against the
Contract's three reading conventions and concur. Corollary B's body and proof
are likewise correct as written; nothing in Lemmas 1–4, the Theorem, the
Corollary, Remark A, or the body of Corollary B is touched by any finding this
round.

**E's finding is UPHELD, but not in the form E filed it.** E frames the defect
as a class-D "citation-scope mismatch": that Remark C(i) discharges "no
conflict with Q5 (tightness of Theorem 2.3)" using a derivation which is
invoked to cover Corollary B's domain but is valid only for the Theorem's
symmetric-PSD sub-domain. On a close read of the artifact text this framing
overstates what Remark C(i) actually says: Remark C opens with "**The Theorem**
answers Question 8.1 ... and nothing more," and its derivation is explicitly
introduced as "Let `v_0` and `k = k_{v_0}` be as in the proof of **the
Theorem**." Remark C(i) never asserts that this reconciliation covers
Corollary B; it is silent about Corollary B throughout. So there is no
misapplied citation — Q5 is quoted and used correctly for the object the
Remark actually discusses.

What *is* a genuine defect, which I confirm by my own derivation below (not
by taking E's, B's, or anyone else's word for it): Corollary B's domain
(rank-one matrices of unit Frobenius norm) is the domain Theorem 2.3 and its
tightness claim Q5 are actually stated over, strictly more so than the
Theorem's sphere/PSD sub-case is, and Remark C's stated job is exactly to
reconcile the artifact with the source's negative results. Leaving Corollary
B's instance of that question completely unaddressed — with a domain-matched
result present three paragraphs above the Remark and no note that its
reconciliation is analogous-but-not-given — is a self-containment gap in a
section whose entire purpose is to prevent exactly this kind of unaddressed
tension. This is the same failure mode that produced UPHELD findings against
Remark C in both prior rounds (r1's F1/F2, r2's F3): a scope remark asserting
or implying a "no conflict" conclusion without deriving it for every part of
the artifact it is naturally read to cover. Accordingly I uphold a
**narrower, corrected version** of E's finding: not a misused citation, but an
**incomplete self-containment argument**, confined to Remark C (commentary),
not load-bearing.

I also verified, independently, that the missing argument is available inside
the artifact's own toolkit — it does not require a source request and does
not put Corollary B's conclusion in any doubt. See COMPUTATION 1 below.

Twelve further findings across the five reports are cosmetic/routine
duplicates of items already adjudicated PEDANTIC in the round-1 or round-2
triage (dangling labels, "affine space" vs. linear space, the un-squared "L²
norm," the `∫K(v,v)dμ=d` domain-of-definition wrinkle, etc.) or are new but
equally non-blocking. None of them touches a load-bearing step. I rule
**1 UPHELD, 0 OVERRULED, 12 PEDANTIC, 0 NEEDS SOURCE, 0 UNCLEAR.**

## RECOMPUTATIONS PERFORMED FOR THIS RULING

### COMPUTATION 1 (the crux: does Remark C(i)'s reconciliation transfer to Corollary B?)

Claim to check: if `μ` is a Borel probability measure on
`X := {X ∈ R^{n×n} : rank X=1, ‖X‖_F=1}`, `X_0 ∈ supp μ` is Corollary B's base
point, `k := k_{X_0}` its reproducing kernel in `G = {X ↦ α+⟨A,X⟩}`, and
`k ≥ 0` `μ`-a.e., does the same conclusion hold as in the sphere case —
`μ` forced onto a single point with mass `≥ 1/(n²+1)` — by an argument fully
internal to the artifact?

*Derivation (mine, not taken from any report).* Exactly as in the artifact's
own Lemma 2(i)–(ii) transferred to `G` (Corollary B's proof already states
this transfer goes through verbatim): `E_μ[k]=1` (since `[1]∈G`) and
`E_μ[k(X)X] = X_0` (matrix identity, since `[X↦X_{ab}]∈G` for every entry).
If `k≥0` `μ`-a.e., `dμ' := k dμ` is a probability measure and
`E_{μ'}[X] = X_0`. Every `X` in the support of `μ'` satisfies `‖X‖_F = 1`
(it lives on `X`), and `‖X_0‖_F=1` (`X_0∈X`). Then, using only the Frobenius
inner product (exactly the same bilinear-expansion move the artifact uses
throughout Lemma 2 and Remark A):

    E_{μ'}‖X − X_0‖_F²  =  E_{μ'}‖X‖_F²  −  2⟨X_0, E_{μ'}X⟩  +  ‖X_0‖_F²
                        =  1  −  2⟨X_0,X_0⟩  +  1
                        =  1 − 2 + 1  =  0 .

A nonnegative integrand with zero integral vanishes a.e., so `X = X_0`
`μ'`-a.e., i.e. `μ'({X_0}) = 1` — a **point mass**, with no `±`-style
ambiguity at all (simpler than the sphere case, which needs the extra step of
ruling out `−v_0`). Hence `1 = ∫_{\{X_0\}} k\,dμ = K(X_0,X_0)\,μ({X_0})`, so
`μ({X_0}) = 1/K(X_0,X_0) ≥ 1/(n²+1)` (Corollary B's Lemma-3 analogue), and
conditioning on that atom gives a nonnegative reweighting reaching `X_0`
exactly at cost `log(1/μ({X_0})) = log K(X_0,X_0) ≤ log(n²+1)` — the same
bound Corollary B already proves for its (possibly signed) `r`. So whenever
Corollary B's construction returns a nonnegative `r`, that `μ` is,
by exactly this argument, not a hard instance for the nonnegative version of
Theorem 2.3 either, and Q5's tightness (which is a statement about worst-case
`μ`) is not contradicted.

*Numerical sanity check of the key algebraic identity* (pure Python, exact
Frobenius inner products, no library beyond `math`/`random`): for
`n=3`, two independent random unit-Frobenius rank-one matrices `X_1, X_2` and
`X_0 := pX_1+(1-p)X_2`,

    p     ‖X_0‖_F
    0.3   0.59588
    0.5   0.48190
    0.7   0.59588

confirming `‖X_0‖_F < 1` strictly whenever `X_1 ≠ X_2` (so a mixture of two
distinct unit-Frobenius points cannot itself land on the unit-Frobenius
sphere), and directly verifying the identity `E‖X−X_0‖²_F = 1 − ‖X_0‖²_F` at
`p=0.4` (`0.7370625784873641` vs. `0.7370625784873642`, agreement to float
precision). This is the same computation as the identity above, specialised
to a two-point measure, and it confirms the general argument is not merely a
plausible transfer (as pass B guessed) but an exact, elementary, two-line
consequence of the Frobenius inner product — well within "no computation is
outsourced to any document outside this artifact," the standard the artifact
itself sets in its own r2→r3 revision log.

**Conclusion.** The reconciliation E asked for does hold, and holds by an
argument strictly simpler than the one already in the artifact (no `±`
ambiguity to rule out). Nothing is unsound. What is missing is the sentence
saying so.

### COMPUTATION 2 (spot-checks of the load-bearing chain, to avoid taking any referee's "ACCEPTED" on faith)

* Lemma 1(b): re-derived independently. `h := q_{Q-Q'}` continuous,
  `μ({h≠0})=0`; if `h(v_0)≠0` at a support point, `U:={|h|>|h(v_0)|/2}` is
  open, contains `v_0`, so `μ(U)>0` by definition of support, contradicting
  `U ⊆ {h≠0}` null. Confirmed: this delivers agreement of *quadratic-form*
  representatives at every point of `supp μ`, which is exactly and only what
  `ev_v`, Lemma 2, and Lemma 3 consume — I checked each of those three
  consumption sites and none asks for more.
* Lemma 2(i): re-derived independently for a concrete case not in the
  artifact's own numerical check — `μ` uniform on 3 points at `0°, 120°, 240°`
  on `S^1` — obtaining `k(θ) = 1 + 2cos(2θ)` at `v_0=(1,0)`, `K=3=d` (full
  dimension, Lemma 3 tight here), `E_μ[k]=1`, and `E_μ[k\,vv^T]=v_0v_0^T`
  exactly (the kernel vanishes at the other two points, so the identity is
  immediate). Consistent with all five referees' own checks; no discrepancy.
* Corollary's constant: `n(n+1)/2 ≤ n²` for `n≥1`; `max_{x>0}(\log x)/x^δ =
  1/(eδ)` at `x=e^{1/δ}` — both re-derived by calculus (`f'(x) =
  x^{-δ-1}(1-δ\log x)`), matching every referee and both prior rounds'
  triage.
* The one whitespace discrepancy referee B logged (card Q1: `‖L‖_F\` ?`" with
  a space before the closing `?`, versus the artifact's `‖L‖_F\`?"` with no
  space) — confirmed by direct `grep` against both files: the card indeed
  carries the space, the artifact does not. This is exactly the kind of
  `pdftotext`-layout noise the grounding result already flags as immaterial;
  no clause is dropped, added, or altered. Not scored, per B's own
  classification, which I adopt.

No other numeric or algebraic claim in any of the five reports was in
dispute, so no further recomputation was required beyond the two items above
(the crux, and a spot-check of the parts of the chain no referee flagged but
that this triage's own standard requires re-deriving rather than trusting).

## TABLE OF DISTINCT FINDINGS

| # | Finding (deduplicated) | Class | Passes raising it | Ruling | Minimal repair | Load-bearing? |
|---|---|---|---|---|---|---|
| F1 | Remark C(i) reconciles "no conflict with Q5" only for the Theorem's sphere/PSD construction and is silent about Corollary B, whose domain (rank-one matrices of unit Frobenius norm) is the domain Theorem 2.3/Q5 actually concern; no analogous reconciliation is given for Corollary B | self-containment gap in a scope remark (not class D — no citation is misapplied; reclassified from E's framing) | E (filed as DEFECTS/class D); B (filed as class C, "routine... does not by itself force DEFECTS") | **UPHELD** (E's substance upheld; E's classification as a misapplied citation, and B's classification as merely routine/pedantic, are both corrected — see COMPUTATION 1) | Add one paragraph to Remark C(i), parallel to the existing derivation, giving the Corollary-B analogue: `k≥0` `μ`-a.e. `⟹ dμ':=k\,dμ` is a probability measure with `E_{μ'}[X]=X_0` (Corollary B's Lemma-2 transfer) `⟹` (Frobenius bilinear expansion, `‖X‖_F=‖X_0‖_F=1`) `E_{μ'}‖X-X_0‖_F²=0 ⟹ μ'({X_0})=1 ⟹ μ({X_0})=1/K(X_0,X_0)≥1/(n²+1)`, and conditioning on `{X_0}` gives a nonnegative reweighting of cost `log K(X_0,X_0) ≤ log(n²+1)`, matching Corollary B's own bound. This is a self-contained two-line argument (verified above, COMPUTATION 1); no source request is needed. | **No.** Confined to Remark C. Corollary B's body, proof and stated bound are unaffected; the repair only closes a gap in the *scope commentary*, and the closing argument I verified shows the gap closes in the artifact's favour, not against it. |
| F2 | Corollary B, "the space of quadratic forms replaced by the affine space `G`" — `G` is a linear space of affine functions, not an affine space | terminology | A, C, D (repeat of r2's F13) | **PEDANTIC** | Replace "affine space" with "linear space" if the section is touched for other reasons. | No |
| F3 | Corollary B, "Only two properties of the function space were used" is not literally exhaustive (boundedness/continuity of `G`'s elements and finite dimension are also used, and compactness of `X` is asserted without its one-line proof) | routine | A | **PEDANTIC** | Note only; the very next sentence in the artifact already supplies boundedness and continuity, and compactness of `X` (continuous image of `S^{n-1}×S^{n-1}`) is a one-line fact, as already noted in r2's F6. | No |
| F4 | DEPENDENCIES never gives a full bibliographic citation (authors/title/venue/arXiv id) inside the artifact itself, though every quotation matches card S1 verbatim | editorial | A | **PEDANTIC** | Optional: add the bibliographic line. Not required; no quotation is unsourced and no source result is load-bearing for the Theorem. | No |
| F5 | Proof plan, "Its `L²` norm averages to `d`" should read "its **squared** `L²` norm" | typo-level | A, C, D (repeat of r2's F10) | **PEDANTIC** | Insert "squared." Lemma 3 itself states the identity correctly. | No |
| F6 | Corollary B, "`c ∈ (0,1]`" is weaker than the achievable `c ∈ [(n²+1)^{-1/2},1]` | routine | A | **PEDANTIC** | Weaker, not wrong; no downstream step needs the sharper lower bound. | No |
| F7 | Remark C(i), "— **equivalently**, `k≥0` forces `μ({±v_0})=1/K(v_0,v_0)≥2/(n(n+1))` —" mislabels an implication as an equivalence | rhetorical | A, C | **PEDANTIC** | Replace "equivalently" with "in particular" or similar; both joined statements are true and the derivation paragraph proves the stronger one. | No |
| F8 | Lemma 3's display `∫K(v,v)dμ(v)=d` names `K(v,v)`, which Lemma 1(c) defines only for `v∈supp μ`, so the integrand is notationally undefined off the support (repaired in the following paragraph via the polynomial `g`) | notational (repeat of r2's F11) | C, D | **PEDANTIC** | None required; the proof already substitutes `g` for `K` and invokes (P1) correctly. | No |
| F9 | Remark C(i) derivation, "`k(−v_0)=k(v_0)=K(v_0,v_0)` **by Lemma 1(c)**" — the evenness `k(−v_0)=k(v_0)` is not from Lemma 1(c) but from the chosen quadratic-form representative being even; only `k(v_0)=K(v_0,v_0)` is Lemma 1(c) | mis-attribution | C, E | **PEDANTIC** | Split the citation: evenness is a property of the quadratic-form representative; `k(v_0)=K(v_0,v_0)` is Lemma 1(c)/definition. Conclusion unaffected either way (both referees who checked it confirm the argument is sound even where `-v_0 ∉ supp μ`, since the `μ({-v_0})=0` case drops the term for any representative). | No |
| F10 | Note after Lemma 1, "(b) is **the only place** where the general Borel case differs from the finitely supported case" — Lemma 3 also differs (needs (P1), Borel measurability of `g`, the positive-measure-meets-support step) | overstatement | C | **PEDANTIC** | Weaken to "one of the two places," or delete the superlative. Meta-remark, not a proof step. | No |
| F11 | Contract's "for every `n∈N`" vs. artifact's "for every `n≥1`" | immaterial | C | **PEDANTIC** | None required; if `0∈N`, `S^{-1}=∅` carries no probability measure, so the Contract instance at `n=0` is vacuous either way. | No |
| F12 | Dangling internal labels `def:signed`, `conj:main` referenced but never defined in this artifact (repeat of r2's F12) | cosmetic | D | **PEDANTIC** | Point the labels at the GOAL section, or drop them; referents are unambiguous as written. | No |
| F13 | Whitespace-only discrepancy in the Question 8.1 quotation: card has a space before the closing `?` (`` ‖L‖_F\` ?``), artifact does not (`` ‖L‖_F\`?``) | typographic | B | **PEDANTIC / not scored** | None required; confirmed by direct comparison against both files (see COMPUTATION 2); no clause is added, dropped or altered, consistent with the grounding result's own finding that inline-math passages ground NEAR only because of `pdftotext` line-breaking. | No |

No finding of class A (statement drift) was raised by any of the five
passes, and my own quantifier-by-quantifier diff against the Contract (order
of `∀ε∀δ∃C∀n∀μ∃r,L`; Reading Conventions 1–3) found none either, so the
"class A is never PEDANTIC" rule is not engaged this round. No finding was
raised as NEEDS SOURCE by any referee this round, and none is warranted by my
own review: F1's repair is fully internal (COMPUTATION 1), and every
quotation in DEPENDENCIES was already re-verified against card S1 by four of
the five passes and matches, apart from the immaterial whitespace item F13.

## Question — does the UPHELD finding put the Contract statement, or Corollary
B's stated conclusion, in doubt?

**No.** F1 is confined to Remark C(i), a scope/commentary section. Lemmas
1–4, the Theorem, the Corollary, Remark A, and the body and proof of
Corollary B are untouched by this ruling and remain exactly as strong as
`0048-RKHS-1-r2`'s triage found them, reconfirmed by four independent CLEAN
passes and by my own re-derivation of the two steps most load-bearing to
this artifact's method (Lemma 1(b), Lemma 2(i)) plus the crux computation
above. The repair for F1 is additive (one paragraph) and, if anything,
strengthens the artifact's account of its own consistency with the source,
since the missing argument turns out to hold — and to hold more cleanly than
the sphere case — rather than to expose any tension.

## ESCALATION LIST (to the human)

**Empty.** No finding from any of the five passes is UNCLEAR. F1, the one
substantive finding, reduced to a two-line computation (COMPUTATION 1),
verified both symbolically and with a numerical spot-check; every other
finding is a wording, labelling, or attribution nit that a competent reader
resolves without effort and that does not bear on any load-bearing step.

## CONSOLIDATED SOURCE REQUEST

**None.** F1's repair is fully internal to the artifact (an elementary
Frobenius-inner-product computation, exactly analogous to the machinery
already used throughout Lemma 2 and Remark A); no card item is missing, no
external source is needed, and no other finding this round requires one.
Card S1 continues to require no repair.

## REVISION INSTRUCTIONS (UPHELD items only)

Bounded strictly by the single UPHELD finding, F1. All of F2–F13 are
PEDANTIC and must not consume a revision.

1. **(F1) — ADDITIVE, one paragraph, in Remark C(i).** After the existing
   derivation paragraph (which ends "...nothing is taken on the authority of
   a document outside this artifact"), add the Corollary-B analogue: state
   that the same dichotomy holds for Corollary B's construction, and give the
   argument verified in COMPUTATION 1 above — `k≥0` `μ`-a.e. forces
   `dμ':=k\,dμ` to satisfy `E_{μ'}[X]=X_0` (Corollary B's own Lemma-2
   transfer), and since every `X` in `X` and `X_0` itself have Frobenius norm
   exactly `1`, the identity `E_{μ'}‖X-X_0‖_F² = 1 - 2⟨X_0,X_0⟩ + 1 = 0`
   forces `μ'` to be a point mass at `X_0` — simpler than the sphere case,
   with no `±` ambiguity to rule out — giving `μ({X_0}) = 1/K(X_0,X_0) ≥
   1/(n²+1)` and a nonnegative reweighting of the same cost `log(n²+1)`
   Corollary B already proves. Do not weaken or delete the existing
   sphere-case derivation; this is an addition, not a replacement. No other
   part of the artifact is to be touched on account of this ruling.

Items F2–F13 require no artifact edit as a condition of closing this round;
any of them may be folded into a future revision opportunistically but none
is a blocking defect.

### END OF TRIAGE RULING [0048-RKHS-1-r3] ###
