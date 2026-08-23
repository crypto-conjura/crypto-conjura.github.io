# Revision report: `c/0010/latex/solution.tex`

*Extraction for Split Unpredictable Sources, and Decomposition on a Region.*
Prose revision under `tex-manuscript-revision`. No mathematical content was
changed. Suspected errors were reported, not repaired: see `concerns.md`.

| | |
|---|---|
| Source | `solution.tex`, 743 lines, 3928 prose words |
| Revision | `solution-revised.tex`, 743 lines, 3942 prose words (**+14, +0.4%**) |
| Lines changed | 62 (all in place; no line inserted or deleted) |
| Typeset length | 11 pages → 11 pages |
| Linter findings | 104 → 53 |
| `pdflatex` errors | 0 → 0 |
| Overfull hboxes | 5 → 5, identical positions and magnitudes |
| `\label`s | 23 → 23, all preserved |
| Math spans | 697, preserved in order |
| Environment delimiters | 78, preserved in order |
| Reference keys | 75 → 79 (four added; see *Recorded deviations*) |
| Proof overviews | 0 of 15 present; 15 proposed in `proposals.json` |

## Where these files live, and how to rebuild

This package sits in `c/0010/revision/`, deliberately **not** in
`c/0010/latex/`. `scripts/artifact_manifest.py` treats every `.tex` under
`c/<id>/latex/**` as an input to the published PDFs in `c/<id>/pdf/`, so
dropping a second `.tex` in there marks `c/0010`'s committed artifacts stale
against a file that is a review deliverable rather than a build input. Keeping
the revision one directory across leaves the manifest baseline honest.

The cost is that `solution-revised.tex` no longer sits beside the two class
files it loads. To build it:

```
cp c/0010/revision/solution-revised.tex c/0010/latex/
cd c/0010/latex && latexmk -pdf solution-revised.tex
```

`solution-revised.pdf` here is the output of exactly that, 11 pages, and is
committed for reading on paper. Nothing regenerates it, so treat it as a
snapshot of this revision rather than as a live artifact.

## Pass 0. Reconnaissance (no edits)

**Audience.** A cryptography reader working in the random-oracle /
non-uniformity / presampling line, holding the companion statement document
(`main.tex`) open. The document declares its dependence explicitly at line 78
("Notation is that of the statement document and is not repeated"), so it is not
free-standing and cannot be read as if it were.

**The single idea.** Two split unpredictable sources make the posterior law of
the challenge cell a *product* measure; a product measure flattens onto a
combinatorial rectangle; so extraction becomes the discrepancy of a random
matrix on rectangles against tests nameable by short leakage. That buys two
unconditional extraction bounds, and, composed with presampling, the conjecture
on a region of $(P,q,M)$.

**Contribution list and its evidence** [SPJ-EVID].

| Claim | Evidence | Forward-referenced in source? |
|---|---|---|
| (A) `\kna` bound, unconditional | `thm:A` (L433) | no → added |
| (B) `\kappa` bound, unconditional | `thm:B` (L469) | no → added |
| (C) explicit consistent family | `thm:C` (L560) | no → added |
| (C′) the conjecture on a region | `thm:cprime` (L607) | no → added |
| "What is not proved" | `\S sec:barriers` | yes |
| "Where to be most sceptical" | `thm:cprime`, `def:res`, `\S sec:review` | yes |

**Concept count** [GOL-CONCEPTS]. Two new definitions (*revealing rule*,
*challenge resolution*) and roughly ten named derived quantities
($\theta_{\zeta,f}$, $p_\theta$, $m_i$, $k_i$, $\Pi_{f,\zeta}$, $t(k_1,k_2)$,
$\mu(s)$, $C_0$, $L$, $\delta_\zeta$). Not overload for a document of this
length; recorded so the count is on the table.

**Proof inventory.** 15 `proof` environments: L104, 138, 188, 238, 336, 363,
387, 408, 438, 459, 473, 486, 514, 574, 619. Lengths 5 to 46 lines. **None**
opens with an overview. Three (`lem:disc`, `lem:P`, `thm:C`) already use run-in
`\emph{...}` step headings, which is a structured style and made the overviews
easier to write faithfully.

**Notation table.** Built and audited; the collisions it exposed are in Pass 5.

## Pass 1. Architecture

| Line | Rule | Before | After | Note |
|---|---|---|---|---|
| 45 | SPJ-EVID | `Unconditional. This settles` | `Unconditional (Theorem~\ref{thm:A}). This settles` | claim (A) now points at its evidence |
| 50 | SPJ-EVID | `and every observer. Unconditional.` | `… Unconditional (Theorem~\ref{thm:B}).` | claim (B) |
| 53 | SPJ-EVID | `…+q\delta$.` | `…+q\delta$ (Theorem~\ref{thm:C}).` | claim (C) |
| 57 | SPJ-EVID | `or $M\le\sigma'/\sqrt{27\delta}$.` | `… (Theorem~\ref{thm:cprime}).` | claim (C′) |

Checked and left alone:

- **No abstract environment.** `\cjresolves` (L29–32) does the job: 44 words,
  self-contained, no internal cross-reference. Satisfies [GOL-ABS] as it stands.
- **No roadmap paragraph** [SPJ-ROADMAP]. Nothing to remove, and nothing was
  reinstated.
- **Terminal "What is not proved"** [GOL-CONC]. Goldreich would move open
  problems into the introduction; the Reader's guide already summarises them and
  forward-references `\S sec:barriers`, and the two barriers cannot be stated
  without `lem:disc`, `lem:rr` and `lem:mass`. The exception applies. No edit.
- **Layering** [GOL-LAYER]. Conceptual commentary is consistently placed in
  unnumbered paragraphs between results (L89, 120, 159, 203, 319, 350, 375, 394,
  630). This is the layering the rule asks for, done deliberately.
- **Opening** [KNU24]. §1 opens "Everything below rests on two observations,
  which together turn the conjecture into a statement about the discrepancy of a
  random matrix on combinatorial rectangles." Kept verbatim.

Structural findings routed to `deferred.md`: cold arrival of `def:rr` (D10),
independent theorem counters (D5), chit-chat inside three statements (D6, D7,
D8), backward derivation of $C_0$ and $t$ (D11), duplicated commentary (D14,
D15).

## Pass 2. Statements

| Line | Rule | Before | After | Note |
|---|---|---|---|---|
| 54 | KNU1 | `constants $c=2$, $C=8$, for` | `constants $c=2$ and $C=8$, for` | two adjacent formulas read as one list item |
| 181 | KNU1 | `$\|\pi^{i}\|_\infty=m_i$, $k_i:=\lfloor1/m_i\rfloor$,` | `…$, writing $k_i:=…$,` | the second was a *definition*, not a further hypothesis; "writing" says so, and matches the author's own idiom at L128 |
| 309 | KNU2, GOL-CAT | `$D$ has \emph{challenge resolution $M'$} if` | `An observer $D$ has …` | definition opened on a symbol; noun in apposition |
| 382 | KNU1 | `$\theta_{\zeta,f}$,`⏎`$\Prob{\Real=1}=` | *(reverted)* | see Pass 7, R2 |
| 498 | KNU1 | `Let $P\in\mathbb N$, $\gamma\in(0,1)$.` | `Let $P\in\mathbb N$ and $\gamma\in(0,1)$.` | |
| 498 | KNU1, GOL-CAT | `For $M=1$, $\Fun$ is a singleton` | `For $M=1$ the set $\Fun$ is a singleton` | Halmos's overworked comma; also names the object |
| 616 | KNU1 | `with $c=2$, $C=8$.` | `with $c=2$ and $C=8$.` | consistent with L54 |

**Hedge words, every occurrence** [HAL§10]. Two, both inside proofs, neither
carrying a justification. Left in place and reported:

- L367 `the arm $1$ is trivial.` (proof of `lem:mass`)
- L540 `Consistency is immediate;` (proof of `lem:P`, Step 2)

No occurrence of *obvious*, *obviously*, *clearly*, *evidently*, *easy to see*,
*straightforward*, or *routine* anywhere in the document. That is unusual and
worth saying.

**Hanging theorems** [KNU4]. All 20 statement environments checked: every one is
preceded by a sentence ending in a period, a question mark, `\end{proof}`,
`\end{definition}`, or a `\section` head. None.

**Degenerate cases** [HAL§11]. Handled explicitly and in the right places:
$q=0$ (L449), $s=0$ (L359), $k=1$ (L192), $M=1$ (L498), $\delta=1$ (L443),
$\delta_\zeta>1$ (L527). One of them is not actually proved and one may be dead;
see `concerns.md` C4 and C5.

**Definitional choices** [GOL-CHOICE]. `def:res`'s coin quantifier is labelled
*seemingly essential* in prose, with a two-line counterexample (L319–326), and
the surjectivity of $h$ is labelled *without loss* (L315). Both exemplary. Two
choices are unlabelled: `def:rr`'s restriction of the test to a function of
$\zeta$ and the inspected values, and the constant $C_0$. Proposed labels in
`deferred.md` (D9).

## Pass 3. Proofs

| Line | Rule | Before | After | Note |
|---|---|---|---|---|
| 148–151 | KNU-DASH, KNU25 | `computes $\pi^{i}_{H,z_i}$ --- it may … instructs --- and outputs` | `… $\pi^{i}_{H,z_i}$ (it may … instructs), and outputs` | reads correctly with the parenthetical removed |
| 189 | KNU2, GOL-CAT | `$m\ge1/N$ gives $k\le N$` | `The inequality $m\ge1/N$ gives $k\le N$` | proof opened on a symbol |
| 189 | HAL§17 | `For $x\ge1$,`⏎`$\lfloor x\rfloor\ge x/2$` | `For $x\ge1$ we`⏎`have $\lfloor x\rfloor\ge x/2$` | comma overworked as a separator between symbols; [KNU8] permits "we have $x=y$" |
| 191 | HAL§16 | `so with $x=1/m$,`⏎`$1/k\le2m$` | `so taking $x=1/m$ yields`⏎`$1/k\le2m$` | names the move (substitute) |
| 195 | HAL§17 | `$\|\pi\|_\infty\le1/k=2^{-\log k}$, $\log k>0$ and` | `…$ with $\log k>0$ and` | the comma made the "Since" clause look finished; all three remain hypotheses |
| 204 | GOL-PTR | `That is harmless, because` | `The failure to factor is harmless, because` | "That" reached back across a display |
| 250 | KNU1 | `$\theta(f(u))-p_\theta$,`⏎`$u\in R\setminus S_0$, are` | `…,`⏎`for $u\in R\setminus S_0$, are` | Knuth's own example: an index range abutting the term it indexes |
| 337 | KNU2, GOL-CAT | `$\mathcal A_\zeta$ inspects one coordinate` | `The procedure $\mathcal A_\zeta$ inspects one coordinate` | |
| 343 | KNU-DASH | `whole execution ---`⏎`hence its output bit --- is` | `whole execution,`⏎`hence its output bit, is` | short apposition takes commas |
| 449 | KNU1 | `For $q=0$, $s=0$ and every` | `For $q=0$ we have $s=0$, and every` | the original genuinely misparses: `$s=0$` reads as a second hypothesis when it is a conclusion |
| 460 | KNU2, HAL§16 | `$5\sqrt{\sigma'\delta}\le5\sqrt{\sigma'q^{+}\delta}$; and` | `Monotonicity gives $5\sqrt{…}$; and` | opened on a symbol; names the move |
| 487 | KNU2 | `$qM\delta\le\sqrt{\sigma'q^{+}\delta}$ follows` | `The inequality $qM\delta\le…$ follows` | |
| 589 | HAL§17, GOL-CAT | `function of $(H,\vz)$, $H^{\circ}$ is` | `function of $(H,\vz)$, the oracle $H^{\circ}$ is` | Halmos's example verbatim ("Since $p\ne0$, $p\in U$") |
| 620 | KNU2, KNU8 | `$\varepsilon(D)\le6\sqrt{\sigma'q^{+}\delta}$: in` | `We have $\varepsilon(D)\le6\sqrt{…}$: in` | consistent with the document's sparse "we" (L315, 445, 519) |

**Mandatory overviews** [LAM-SKETCH]. All 15 proofs lack one. Fifteen are
proposed in `proposals.json`, each with a `step_map` tying every sentence to a
verbatim fragment of its own proof body, a `gaps` list, and a risk grade. They
are **not** woven into the revised source: per the proposal contract an
insertion pass over mathematical content admits no diff that shows whether the
new material is true, so they are offered item by item. Five are graded HIGH:
`ov02`, `ov06`, `ov09`, `ov10`, `ov14`. Page cost if all fifteen are accepted:
+1250 words, 31% growth. Accepting them selectively is the expected use.

**Discharge** [LAM-QED]. Ten of the fifteen proofs end on the statement they were
to prove. Five end on an intermediate quantity, leaving the last step to the
reader: proofs of `lem:prod` (the factor 2), `lem:mass` (the min over three
arms), `thm:A` (the constant 5), `cor:A` (the constant 6), `thm:C` (the sum of
the three hybrid gaps). Two of those five are missing mathematics rather than
missing prose and are in `concerns.md` (C2, C4); the other three are arithmetic
the reader can do, and are recorded in the corresponding overview's `gaps`.

**Assumption scope** [LAM-SCOPE]. The `\emph{Step n}` headings in `lem:P` and
the `\emph{…}` headings in `lem:disc` and `thm:C` make scope visible, which is
what the rule asks. One loose spot: in `lem:disc`, `$S_0$` and `$w$` are bound
variables in the first step (L240) and used as though fixed in the second
(L248). Reported, not repaired.

**No decorative contradiction** [SU-CONTRA]. Checked: `cor:B` argues by
contrapositive and uses it. Nothing to strip.

**No repeated proof** [HAL§12]. `thm:B` points at `thm:A` rather than repeating
it (L476). Correct as it stands.

## Pass 4. Sentences

| Line | Rule | Before | After | Note |
|---|---|---|---|---|
| 68 | KNU-DASH | `same species --- a` | `same species: a` | |
| 165 | KNU1 | `Let $2\le M\le N$, $\delta:=1/M$, let` | `Let $2\le M\le N$, put $\delta:=1/M$, let` | "put" matches the author's usage at L218 |
| 210 | KNU-DASH, KNU25 | `one at a time --- the next … seen --- halts` | `one at a time (the next … seen), halts` | |
| 290 | GOL-PTR | `This is the one respect` | `The narrow union is the one respect` | |
| 294 | HAL§14 | `demands that any proof fail` | `demands that every proof fail` | genuinely ambiguous quantifier |
| 297 | KNU-DASH | `vacuous --- and in any case` | `vacuous; and in any case` | joins two independent clauses |
| 321 | KNU1 | `at $N=M=2$, $q=1$, the observer` | `at $N=M=2$ and $q=1$, the observer` | |
| 325 | KNU-DASH | `coins are fixed --- exactly … open --- and` | `coins are fixed (exactly … open), and` | |
| 331 | KNU-DASH | `$v_j\in h^{-1}(j)$ --- which exists … --- inspecting` | `$v_j\in h^{-1}(j)$ (which exists …), inspecting` | inside a quoted procedure; punctuation only |
| 397 | KNU1 | `probe $f$ $q$ times?` | `probe $f$ in $q$ queries?` | two formulas separated by a single space; "queries" is the document's own term |
| 465 | GOL-PTR | `This settles the statement's line` | `The corollary settles the statement's line` | |
| 502 | KNU-DASH, KNU25 | `$\bits^{*}$ --- with $Y_{f,\zeta}$ … $\zeta$ --- depending` | `$\bits^{*}$ (with … $\zeta$), depending` | |
| 537 | KNU1 | `its set $I_j$,`⏎`$|I_j|\le P$, to` | `its set $I_j$,`⏎`with $|I_j|\le P$, to` | |
| 575 | KNU1 | `$\mathsf G_2=\Dec_0$,`⏎`$\mathsf G_3=\Dec$.` | `$\mathsf G_2=\Dec_0$ and`⏎`$\mathsf G_3=\Dec$.` | |
| 599 | KNU-DASH | `$\le P\delta$ --- its proof requires` | `$\le P\delta$; its proof requires` | |
| 609 | KNU-DASH | `holds --- in`⏎`particular if …$.` | `holds (in`⏎`particular if …$).` | parentheses keep the scope of the disjunction unambiguous, which a comma would not |
| 622 | KNU-DASH | `applies --- equivalently, … at $M'=1$; in` | `applies (equivalently, … at $M'=1$); in` | |
| 637 | KNU1 | `$\ell=2$, $2^{-k}=\delta$, $q_D=q$ gives` | `…, $2^{-k}=\delta$ and $q_D=q$ gives` | |
| 657 | GOL-PTR | `This is not slack in the counting.` | `The gap is not slack in the counting.` | |
| 671 | KNU-DASH | `query sets --- unions of $M$`⏎`… paths --- rather` | `query sets (unions of $M$`⏎`… paths) rather` | |
| 680 | KNU-DASH | `at all --- only the route` | `at all, only the route` | |
| 694 | KNU-DASH | `structure --- conditioning … $\{Y_I\ne y_I\}$ --- also` | `structure (conditioning … $\{Y_I\ne y_I\}$) also` | |
| 726 | KNU-DASH | `same species --- a claim left` | `same species: a claim left` | parallel to L68 |

All 23 em dashes removed [KNU-DASH]. Hyphen, en dash and `$-$` were left
untouched and are used correctly throughout.

**"any", all four occurrences** [HAL§14]. One fixed (L294). Three left, with
reasons: L297 `in any case` and L728 `at any point` are idiomatic, not
quantifiers; L702 `any adaptive $T$-query distinguisher` sits inside an italic
restatement of [CDGS, Claim 3] and editing it would alter a quotation.

**"which" for "that", all six flagged** [KNU22]. All six are false positives:
every one follows a comma or a preposition (`in which` L290, L504; `of which`
L601, L725; `on which` L741; and L331 is non-restrictive inside the new
parentheses). No edit.

**Voice and person.** No hedged passive of the `it can be seen that` family
anywhere, and no `Note that` / `It is worth noting that` filler. The register is
impersonal declarative with a sparse "we" (L315, 445, 519), which [HAL§13]
endorses; my two additions ("we have", L189 and L620) hold that register. The
passive at L723 (`Two rounds of adversarial review were run`) is **kept**: the
agent is generic and naming it would assert something the source does not, which
is the resolution recorded in the conflict register for [SPJ-VOICE].

**Capitalisation of named items** [KNU19]. The `enumerate` items of `lem:prod`
were referred to as `Item~1` (L144) but `item~2`, `item~4` elsewhere. Four edits,
not tabulated above because they are identical in form: `item~2` → `Item~2`
(L147), `item~2` → `Item~2` (L153), `item~4` → `Item~4` (L154), `item~2` →
`Item~2` (L155). Now uniform throughout.

**Blah test** [KNU13]. Applied to all 14 paragraphs containing displayed
mathematics. All survive: each display is introduced by prose that names what is
being bounded or substituted. The two paragraphs that survive least well are the
numeric chains at L280 and L259, which is a [HAL§16] finding recorded below
rather than a prose defect.

**First-sentence thread** [SU-SKIM]. Read alone, the first sentences of the
unnumbered commentary paragraphs (L89, 120, 159, 203, 319, 350, 375, 394, 465,
630) carry the argument end to end. No edit.

## Pass 5. Notation

No edits: every fix in this pass would change a math span. All reported.

**Symbol collisions** [HAL§6][KNU14]. Six, in descending order of how likely
they are to mislead:

1. **$\theta$ has two meanings.** The test $\theta:[M]\to\bits$ (L121 and
   throughout) and a real threshold in $(0,1]$ (`lem:prod`(4) at L134; `lem:mass`
   at L367–372, with $g(\theta)$ and $\theta^{*}$). The test is the document's
   central object, and `lem:mass` invokes `lem:prod`(4) — so both meanings are
   live within one proof. This is the collision to fix first.
2. **$\delta$ has three.** The unpredictability parameter (global), the density
   parameter $\delta_\zeta$ of the [CDGS] decomposition (L527), and the point
   mass $\delta_u$ (L193).
3. **$S$ has four.** The sources $S_1,S_2$; the min-entropy deficiency $S_\zeta$
   and $\bar S$ (L517, 520); the inspected set $S_0\subseteq[N]^2$ (L240); and
   $\mathcal S$, the revealed set. $S_1,S_2$ against $S_\zeta$ is the near
   collision.
4. **$\mu$ has two.** The mass bound $\mu(s)$ (L40, 359) and the conditional law
   $\mu_\zeta$ (L516).
5. **$k$ has two.** $k=\lfloor1/m\rfloor$ (flattening) and the entropy parameter
   with $2^{-k}=\delta$ (L637).
6. **$c$ has two.** The conjecture's absolute constant (L54) and the Hoeffding
   range lengths $c_i$ (L715).

Font-distinguished and therefore acceptable, but recorded: $P$ / $\mathsf P$ /
$P'$; $G$ / $\mathsf G_i$; $T$ / $\mathcal T$; $m$ against $M$ and $M'$.
$e$ is reserved for Euler's number throughout, as [HAL§6] requires.

**An undefined symbol.** $Q$ at L603 (`$\Prob{\vx\in Q}\le q\delta$`) is never
introduced. See `concerns.md` C3.

**Subscript depth** [KNU15][GOL-NOTA]. Nine sites. The worst is
$p_{\theta_{\zeta,f}}$, a subscript on a doubly-subscripted object, at L228, 245,
346, 384. Redesign proposed in `deferred.md` (D2); one of the nine flags
($[N]^{2}$, L244) is a false positive.

**Numbered display never referenced** [KNU16]. `eq:disc` (L226). Its number is
never used: the proof of `prop:master` cites the *lemma* (L425), not the
equation. The starred form would fix it, but that would delete a `\label`, which
invariant 3 forbids. Reported only.

**Unreferenced labels.** `def:rr` and `rem:one` are defined and never
referenced. Harmless on statement environments, which are legitimately
addressable; recorded for completeness.

**Set-builder** L520 uses `:` rather than `\mid` (`$\{\zeta:S_\zeta>\bar S\}$`),
against the document's own practice at L128. Math change; reported only.

## Pass 6. Subtraction

One edit:

| Line | Rule | Before | After | Note |
|---|---|---|---|---|
| 163 | GOL-PTR, SU-IMP | `This matters, because it is what forces the exponent $1/3$ in Lemma~\ref{lem:mass}.` | `The failure forces the exponent $1/3$ in Lemma~\ref{lem:mass}.` | −7 words; names the antecedent, and "this matters" asserted nothing the rest of the sentence did not |

**Pass 6 found no other filler that could be removed without deleting a claim.**
That is the finding, and it is why the revision is 14 words longer rather than
shorter. Every candidate was examined:

- The commentary at L45–48 and L465–467 is near-verbatim duplicated, but the
  final clauses differ mathematically (*no dependence on $M$* against *no
  $\log M$*), so neither can be deleted and they cannot be unified without
  changing content. `concerns.md` C10 and `deferred.md` D14.
- The phrase *both of the same species: a claim left underdetermined rather than
  false* appears at L68 and again at L726. Here the content **is** identical, so
  one copy is removable, but removing a 13-word characterisation from someone
  else's manuscript is a judgement for the author. `deferred.md` D15.
- The elementary proof of $\lfloor x\rfloor\ge x/2$ (L189–192) reproduces a
  standard fact [GOL-LAYER], but it is two lines and the factor 2 it yields
  propagates into every later bound. Kept.
- The unused lower bound $(n/k)^{k}$ in the [CFHS, Lemma 4.3] restatement (L708)
  is a red herring [SU-RH]. It sits inside a quotation of an external result;
  reported, not cut.
- `\S sec:review` (L718–741) is long for a review-status section, and every
  sentence of it is load-bearing epistemic disclosure. Kept in full.

Length accounting, since the revision grew: the +14 words are the net of −7 here
and +21 across eleven Pass 3/4 edits that insert a noun or an inference marker
where [KNU2], [HAL§17] or [GOL-PTR] requires one. No page limit was named. If
one is, take D14 and D15 first.

## Pass 7. LaTeX mechanics

| Line | Rule | Before | After | Note |
|---|---|---|---|---|
| 282 | KNU-TIE | `giving \eqref{eq:Et}.` | `giving~\eqref{eq:Et}.` | the only missing tie in the file |
| 429 | KNU21 | `non-negative` | `nonnegative` | Knuth's list |

### Two edits reverted after measurement

Both were correct by rule and wrong in effect: each lengthened the prose
preceding a long unbreakable inline formula and pushed it into the margin. The
document is meant to be read on paper, so the box wins.

| | Rule | Edit | Measured effect | Disposition |
|---|---|---|---|---|
| R1 | HAL§17, HAL§16 | L258 `By the definition of $t$,` → `The definition of $t$ gives` | **new** overfull hbox, 9.75pt, at L258–266 | reverted; the real fix is D3 |
| R2 | HAL§17, KNU8 | L382 `…$\theta_{\zeta,f}$,` → `…$\theta_{\zeta,f}$ we have` | existing overfull hbox at L382–385 worsened 19.6pt → 48.8pt | reverted; the real fix is D4 |

With both reverted the revision's typesetting diagnostics are identical to the
source's: 0 errors, 5 overfull hboxes at the same five paragraphs and the same
five magnitudes (15.99, 12.84, 41.15, 19.61, 27.90 pt). All five are
pre-existing, all five are long inline formulas, and all five need a math change
to fix; they are D3 and D4.

### Reported, not repaired

- **`\frac` in inline math** [KNU-FRAC], 2 sites: `\ln\frac{4N^{2}}{\gamma_0}`
  (L219, inside a lemma statement) and `e^{-k_1\ln\frac{eN}{k_1}}` (L259, a
  `\frac` inside an exponent). Both set microscopic type. The slashed form is a
  math change → D3.
- **Unnamed moves in a numeric chain** [HAL§16], L280: the chain
  `$L+C_0=1+\ln N+\dots\le3\ln N+0.694\sigma+3.78+\ln\gamma_0^{-1}$` collects
  terms and rounds $\ln2$ up to $0.694$ and $1+2\ln2+\ln4$ up to $3.78$ without
  saying so. One sentence naming the moves would fix it; that sentence is an
  addition, so it is D12.
- **Twelve source lines now exceed the file's ~80-column wrap** (45, 190, 195,
  290, 294, 321, 337, 465, 498, 538, 589, 620). The source already has 80 such
  lines, almost all long inline math, so the convention is not strictly enforced.
  I did **not** reflow: a cosmetic reflow would touch a dozen line-blocks beyond
  the semantic edits and make the diff harder to audit, which is the opposite of
  what this deliverable is for. Reflow these when you next touch the paragraphs.

Checked and correct as they stand: `\sample` used uniformly for all four
samplings (L79, 223, 391, 587); `i.i.d.\ ` escaped correctly (L243, 287);
`\tfrac12` chosen for an inline fraction (L296); TeX quotes at L330 and L332;
`\mid` in the conditional probabilities at L128 and L141; no colon before any
display [KNU23]; no `\forall`/`\exists`/`iff`/`s.t.` in running prose [KNU3]; no
programming notation in math [KNU-PROG]; all 14 macro definitions used.

## Recorded deviations from the mechanical check

`check_invariants.py` compares reference keys and macro counts as ordered lists,
so the four Pass 1 forward references show as violations. They are the **only**
deviation, and both runs are given so the prose work can be audited separately
from the additions.

**Run 1, prose-only revision (the 49 prose edits, no added references):**

```
Formal invariants:
  ok      math spans: 697 preserved, order intact
  ok      reference keys: 75 preserved, order intact
  ok      environment delimiters: 78 preserved, order intact
  ok      proof overviews: 15 retained above floor
  ok      macros: no new macro names introduced

Prose words: 3928 -> 3938  (-10 removed, -0.3%)
```

Every formal invariant holds exactly. This is the evidence that the prose pass
touched no mathematics.

**Run 2, delivered revision (`solution-revised.tex`):**

```
Formal invariants:
  ok      math spans: 697 preserved, order intact
  FAIL    reference keys
            added (1x): ref:thm:A
            added (1x): ref:thm:B
            added (1x): ref:thm:C
            added (1x): ref:thm:cprime
  ok      environment delimiters: 78 preserved, order intact
  ok      proof overviews: 15 retained above floor
  FAIL    macros not present in the original
            \ref (4x)

Prose words: 3928 -> 3942  (-14 removed, -0.4%)
```

Both FAILs are the same four insertions counted twice: four `\ref` macros
carrying four reference keys, each pointing at a `\label` that already exists in
the source, all four inside the Reader's guide, all four required by [SPJ-EVID]
and by this skill's own checklist. No label was renamed or deleted. To recover a
mechanically clean run, drop the four parentheticals at L45, 50, 53 and 57.

Note also that the script's "macros not present in the original" test is
implemented as a `Counter` subtraction, so it fires on any *increase* in the
count of an existing macro, not only on a genuinely new macro name. Every other
edit in this revision was written to keep all macro counts non-increasing.

## Note on `check_proposals.py`

All 15 overview proposals report `overview anchor does not resolve inside any
proof environment`, and this is a bug in the checker, not a property of the
proposals. `locate()` falls back to searching a whitespace-normalised copy of the
source and returns an index into *that* string, which is then compared against
`start`/`end` offsets taken from the *original* string. The two offset spaces
drift apart by one character per collapsed newline, so every anchor appears to
sit earlier than it does. Measured drift across this file, 48 characters at the
first proof rising monotonically to 146 at the fifteenth:

```
id     orig_off  norm_off   drift   proof
ov01       5012      4964      48     [1]
ov05      17727     17637      90     [5]
ov10      23817     23701     116    [10]
ov15      32407     32261     146    [15]
```

Verified independently, in a single offset space: each of the 15 anchors occurs
**exactly once** in the source and lies inside its intended proof, in order 1
through 15. The checker's other tests all pass: kinds, positions, marker
comments, macro availability, `basis`, `risk`, paragraph counts, and the
forbidden-phrase scan. That scan earned its keep, catching *trivial* in `ov11`,
which is now rewritten.

## Verification checklist

- [x] **Compiles with `pdflatex`, same number of errors as before or fewer.** 0 → 0. Overfull hboxes 5 → 5, at identical positions and magnitudes.
- [x] **Every `\label` present in the original is present in the revision.** 23 → 23.
- [x] **Every math span, macro name, citation key and environment delimiter appears in the same order, except where recorded.** 697 math spans, 78 delimiters, all macro counts non-increasing. Exception recorded: four added `\ref` keys.
- [x] **No em dashes.** 23 → 0.
- [x] **Every claim in the introduction has a forward reference to its evidence.** Four added; the other two already had them.
- [x] **Abstract self-contained, no internal references, under 200 words.** No `abstract` environment; `\cjresolves` serves, 44 words, no internal cross-reference.
- [ ] **Every proof opens with an overview of at most two paragraphs.** Not satisfied in the source: 0 of 15. Fifteen proposed in `proposals.json`, all one paragraph, none applied. This is the proposal contract working as designed, not an omission.
- [x] **Every overview has a step map covering its sentences, a risk grade, and a gaps list.** All 15.
- [x] **No overview uses crux, key difficulty, main obstacle, essential idea, tight, optimal, clear, obvious, immediate, easy to see, routine, standard, or trivial.** Verified by `check_proposals.py` after fixing `ov11`.
- [x] **Every gap listed in an overview appears as a question in `concerns.md`.** Six gaps; all six appear in §4 of `concerns.md`.
- [ ] **Every proof ends by discharging its stated goal.** Ten of fifteen. The five exceptions are itemised under Pass 3 and split between `concerns.md` (two are missing mathematics) and the overviews' `gaps` (three are unwritten arithmetic).
- [x] **Every occurrence of "obvious", "clearly", "easy to see", "straightforward" in the author's text is listed.** Zero occurrences of those four; the two members of the family that do occur (*trivial* L367, *immediate* L540) are listed under Pass 2.
- [ ] **Notation table: no symbol with two meanings, no meaning with two symbols.** Not satisfied. Six collisions listed under Pass 5, headed by $\theta$. None repaired: every repair is a math change.
- [x] **Blah test passed on every paragraph containing displayed mathematics.** All 14.
- [x] **Word count reported before and after.** 3928 → 3942. **The after is larger, by 14 words (0.4%)**, contrary to the default target. Accounted for under Pass 6; no page limit was named, and D7/D8 will more than recover it.
- [x] **Every edit in the report carries a rule ID.** 51 applied replacement operations, 2 reverted, all tagged. Forty-seven of the applied operations appear as 50 table rows above (the operation spanning L188–191 fixes three rules and so takes three rows; the one at L498 takes two); the remaining four are the `Item~n` capitalisations, tagged [KNU19] under Pass 4.
- [ ] **Every claim, hypothesis, quantifier, modal qualifier and citation in the original is present and unaltered in the revision, checked last in a fresh pass.** **Not done here, and it is the one check that cannot be done by the reviser.** Run it in a clean context with the prompt in `SKILL.md`, on `solution.orig.tex` against `solution-revised.tex`. The mechanical evidence that it should come back empty is Run 1 above; mechanical evidence cannot see a lost hypothesis, which is the whole reason the check exists.
