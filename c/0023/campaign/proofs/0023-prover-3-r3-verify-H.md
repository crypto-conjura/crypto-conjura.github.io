---
id: 0023-prover-3-r3-verify-H
agent: verifier-b
model: claude-opus-5[1m]
cycle: 3
---

# Diff-only referee pass on `0023-prover-3-r3.md` against `0023-prover-3-r2.md`

Mandate: narrow. Check (1) the diff's scope against the r2-triage's text-only
mandate, (2) that the five upheld repairs landed and landed correctly, (3) that
the ladder-record sentence matches the ruling verbatim and is marked/warned,
(4) that the repair introduced nothing new that is wrong, (5) that PARTIAL and
all five gaps survive. NOT a re-review of the mathematics.

**Tooling note.** No Bash/`diff` tool was exposed to this pass. The change set
was therefore reconstructed by reading both artifacts in full, line by line
(r2: 1055 lines; r3: 1251 lines), plus `sources/S7-changfang26-card.md` (594
lines, incl. the S7b addendum) for the one CARD adjudication. Every "unchanged"
assertion below is a direct text comparison, not an inference from the r3
changelog.

## STEP 0 — COMPLETENESS

`### END OF ARTIFACT 0023-prover-3-r3 ###` present at line 1251. Not truncated.
Front matter complete (`id, agent, model, cycle, status: PARTIAL`). Proceed.

## STEP 0.5 — NEGATION CHECK (per changed load-bearing sentence)

| # | New/changed claim | Negation attempted | Outcome | Tag |
|---|---|---|---|---|
| N1 | Record sentence + title + VERDICT 3, with "**and nonempty at the codimension-$d$ subcube $C$**" | Exhibit an argument, relevance-denominated or own-heavy-at-$\theta>\frac1{2(2^d-1)}$-and-nonempty-at-$C$, establishing a threshold above $(d+1)2^{-d-1}$ resp. $\frac1{2(2^d-1)}$ | Blocked by T2+T6 / T2+T8, both verbatim from r2. The edit *adds* a hypothesis to a negative statement, i.e. narrows what is condemned; structurally it cannot create an overclaim | MECH |
| N2 | §5.3's new non-vacuity paragraph: an own-heavy-at-$\tfrac14$ $W$ with $W(C)=\emptyset$ taking the address hub gets only $\frac{d+1}{4(d-1)}$ from T6 | Find a cap in this artifact that does catch such a $W$ | None: CAP II's second hypothesis fails by construction; T6 at denominator $2(d-1)$ gives exactly $\frac{d+1}{4(d-1)}$; T3/§8.1 gives only $\eta^*_W\le1$. Such a $W$ exists (localised, own-heavy at $\tfrac14$ since $\mathrm{Inf}_{a_t}=\tfrac14$, empty elsewhere) — own-heaviness is an inclusion constraint, as the paragraph says | MECH |
| N3 | VERDICT 1: CAP I's hypothesis **holds**, its conclusion degrades to $\approx\frac{d+1}{4d}$ | Find a CAP I hypothesis that fails for $W_{\mathrm{sh}}$ / cert / $W_{\max}$ at the address pair | T6's sole hypothesis is nonemptiness of the combined window, which holds for all three; T6(b)'s density premise holds at $c=2^{-\Theta(d)}$ and yields a vacuous ceiling. r3's "hypothesis holds, conclusion degrades" is the correct diagnosis (see F3 for one numeral) | MECH |
| N4 | VERDICT 5's restricted list ($W_{\mathrm{rel}},W_{\mathrm{sh}},W_{\max}$, cert windows; **not** $W_{\mathrm{Forced}},W^\theta_{\mathrm{hvy}}$) | Find a member of the list that is empty at some pair of $\mathcal P_d$, or an excluded rule that is nonempty everywhere | List members all nonempty on $\mathcal P_d$ (T4(b); §7.1's $\deg\ge1$ argument; certificates of a point are nonempty unless $A=\{\pm1\}^N$, excluded). Exclusions correct: $\mathrm{Forced}=\emptyset$ on both sides at the address pair and $\mathrm{Forced}(D)=\emptyset$; $W^\theta_{\mathrm{hvy}}(D)=\emptyset$ above the level | MECH |
| N5 | Remark 4.3's P-b addition: $\mathrm{Inf}_i(f_A)\le\frac12$ for every nonempty $A$, so $W^\theta_{\mathrm{hvy}}\equiv\emptyset$ at $\theta>\frac12$ | Find $A,i$ with $\mathrm{Inf}_i(f_A)>\frac12$ | Impossible: $\frac{P_1/4}{P_2+P_1/2}\le\frac12\iff0\le P_2/2$. Inline derivation is complete and correct | MECH (+CODE, via the triage's brute force) |
| N6 | §8's record-keeping note ($\eta^*=1$; the two killers unconditional) | Check for a retraction or a silent contradiction of §8.2 / VERDICT 1 / VERDICT 5, which still say "open" | No contradiction: the note names those three places explicitly, calls them **superseded, not falsified**, attributes $\eta^*=1$ to `0023-refuter-5` as **CERTIFIED, not verified**, and conditions no claim on it. Independent settlement is not asserted, so the disclosure is adequate | NONE (disclosed) |
| N7 | Declined gloss ("equality iff $i$ is forced") | Test the gloss itself | The gloss is **false** in the "only if" direction: $A=\{(+1,+1),(-1,-1)\}\subseteq\{\pm1\}^2$, $i=1$ gives $P_1=1,P_2=0$, so $\mathrm{Inf}_1(f_A)=\frac12$, yet $A$ does not force $x_1$ ($\deg\mathbf 1_A=2$, so $A$ is in the class for $d\ge2$). Declining was **right**; the reviser's stated ground is exactly this counterexample | MECH |

## 1. FINAL VERDICT

The repair is **CLEAN as a repair** — the diff touches nothing but the permitted
surfaces, all five upheld findings landed and landed correctly, the ladder-record
sentence reproduces the ruling's text verbatim and is both marked as the record
sentence and accompanied by an explicit "do not paste r2's version" warning, the
declined "equality iff forced" gloss was correctly declined, and the artifact
still declares PARTIAL with [G1]–[G5] intact — with one newly introduced
non-load-bearing class-(D) mis-description of card S7 inside the very register row
being repaired, plus four pedantic items.

## 2. FINDINGS TABLE

| # | Location (quoted) | Class | Grade | Explanation |
|---|---|---|---|---|
| F1 | Preamble, l. 11–19: "the repair is to the title, to **four VERDICT clauses**, to §5.3's displayed record sentence, to **Remark 1.1**, Remark 2.1, Remark 4.3 and **two register rows**" | (D) light | PEDANTIC | Self-description miscounts its own diff: **three** VERDICT clauses changed (1, 3, 5 — clause 2(ii) already carried the nonemptiness clause in r2 and is verbatim; 4 and 6 untouched); **three** register rows changed (S7 restated + two added); and Remark 1.1 is verbatim from r2 — what the repair added is the *new* Remark 1.1$'$. Bookkeeping only; nothing mathematical rests on it. |
| F2 | DEPENDENCIES, S7 obstacle-(ii) row: "**The card says nothing about influences, families, pairs or factorisation**" | (D) light | UPHELD-worthy, non-load-bearing | False of the *card*, and in tension with the same table cell: the card's obstacle (ii), quoted two clauses earlier, speaks of "the union $T$ over a whole **family**"; the card's "Where the campaign would use it" block runs the argument for a cross-disjoint **pair** $A,B$. What the card records is that **the paper** says nothing about influences/families/pairs (S7 "What it does NOT say"; upgraded to the full 14 pages by S7b). The ruling's own wording was "states twice that *the paper* contains nothing about …". One-word fix: "the card records that the paper says nothing about …". Row is marked non-load-bearing and Remark 2.1's parallel wording is clean, so nothing downstream moves. This is a *new* defect introduced by the repair. |
| F3 | VERDICT 1: "their density there is only $d/(2^{d-1}+d-1)$, so T6(b)'s ceiling degrades to $\approx\frac{d+1}{4d}$" | (C) trivial | PEDANTIC | Attributed to all three functionals, but §7.3 computes $W_{\max}$'s density as $(d-1)/(2^{d-1}+d-1)$, whose T6 ceiling is $\frac{d+1}{4(d-1)}$. Both are $2^{-\Theta(d)}$ and both ceilings are $\approx\frac14$, so the clause's conclusion ("no bound below $1/\mathrm{poly}(d)$") is untouched; the "$\approx$" absorbs it. The ruling prescribed this numeral for $W_{\mathrm{sh}}$ and r3 applied it verbatim to all three. Minor headline/body inconsistency. |
| F4 | §5.3, new paragraph: "Such a $W$ is capped by nothing in this artifact (Remark 4.2$'$)" | (C) trivial | PEDANTIC | Literally loose: T3/§8.1 formally caps every localised $W$ by $\eta^*_W\le1$. The intended reading is fixed by the immediately preceding clause ("no exponential cap at all"), and it is the artifact's established locution (used identically for the mass-denominated route in VERDICT 2, Remark 4.3, [G1]). Not a new overclaim. |
| F5 | §8 note: "Each of `0023-refuter-3` **§4's** two certificates … against (HEAVY$_\theta$)" | (D) light | PEDANTIC | §4 supplies the two witness families and their tables; the (HEAVY$_\theta$) refutation is §5.2 — as the artifact's own register rows record, and as the ruling attributed it ("refuter-3 §4/§5.2"). The note is labelled record-keeping and is load-bearing for nothing. |
| — | Theorem statements, constants, proofs, witness tables, declared gaps | — | NO FINDING | No class-B mandate violation: T1–T9 (statements *and* proofs), CAP I/CAP II constants, T5/T7 tables and their exact checks, §5.1–5.2, §5.4, §6.1–6.4, §7.1–7.5 (every ratio and the whole certificate arithmetic), §8 items 1–5, and [G1]–[G5]/[MEMORY]/[ESCALATED E1] are character-for-character r2. |

No class (A), (B) or (E) finding. No SOURCE REQUEST.

## 3. LOG, KEYED TO THE DIFF HUNKS

Thirteen hunks, no more. Permitted-surface column refers to the mandate as
stated to this pass.

**H1 — Title (l. 9).** Two edits, both required. (i) "own-heavy" → "own-heavy
*while nonempty at the codimension-$d$ subcube $C$*" (U-A1, place 1 of 3).
(ii) "escape both caps" → "escape both caps: P1 outright, P5 for minimum-size
certificate selections (its declared minimal-certificate variant is open,
[G5])" (U-A2). Both land; wording tracks the ruling's §2/§8.2 prescription.
P1 left unqualified — correct per the ruling (§7.1 evaluates exactly P1's
declared window; the size bound is definitional; the ratio is the same for
every choice of the two top supports). PERMITTED.

**H2 — New preamble paragraph (l. 11–19), and r2's opening line re-led
("r2 was in turn a revision of …", l. 21).** Provenance/scope prose. Not in the
enumerated permitted list, but it is front-matter record-keeping, not a theorem,
constant, proof, witness table or gap, so it is not a class-B mandate breach.
Its substantive claim — "No theorem, constant, proof, witness table or gap was
changed" — I confirm as true. Its enumeration of the diff is inaccurate: F1.
BENIGN + F1.

**H3 — VERDICT 1 (l. 58–84).** Two edits. (i) First sentence gains "P1
outright, P5 for minimum-size certificate selections ([G5] for its declared
minimal-certificate variant, which is open)" — U-A2 place 2 of 2, matching the
ruling. (ii) The "precisely what is proved" sentence is rebuilt per U-B2:
r2's "at both certified witnesses the hypotheses of CAP I and of CAP II fail"
becomes "neither cap yields any bound below $1/\mathrm{poly}(d)$ …", then splits
the two caps — CAP I: "*not* a failure of its hypothesis — T6's nonemptiness
hypothesis **holds** … but a degradation of its conclusion"; CAP II: "the
hypothesis genuinely **fails**", with witness (b)'s $D$ attaining the level
exactly. The CAP II half is left as the ruling directed (verbatim substance from
r2, which the ruling certified accurate). Negation checks N3, N4 pass. One
numeral over-applied: F3. PERMITTED, LANDED.

**H4 — VERDICT 3 (l. 109–121).** Lead-in gains "— this displayed sentence, and
only this one, is the sentence intended for the campaign's ladder record
(`LEDGER.md`, `PROGRESS.md`); the r2 version of it must not be pasted there,
because it omitted CAP II's nonemptiness hypothesis"; the display is replaced.
Check 3 discharged: the display is **word-for-word** the ruling's U-A1 sentence
(only the emphasis markup differs: the ruling bolds the inserted clause, r3
bolds it in VERDICT 3 and italicises it in §5.3; "No" is capitalised in both,
as in the ruling — r2 had lowercase "no" in §5.3). Marked as the record
sentence ✔; predecessor's version explicitly proscribed ✔ (twice, here and in
§5.3's closing line). PERMITTED, LANDED.

**H5 — VERDICT 5 (l. 130–139).** U-B1: "which includes every functional named in
this artifact" is gone, replaced by §8.1's restricted list plus an explicit
"it does **not** include $W_{\mathrm{Forced}}$ or $W^\theta_{\mathrm{hvy}}$,
which are empty at some pairs of $\mathcal P_d$ and for which only T3's
restricted ceiling $\eta^*_W$ is claimed". Agrees with §8.1 (unchanged). N4
passes. No conflict with [G5], which concerns expected window *size* under
CAP I(b), not nonemptiness. PERMITTED, LANDED.

**H6 — New Remark 1.1$'$ (l. 221–231), pedantic P-a.** Reproduces the ruling
§1(d) text: a witness pair is used only (i) to instantiate (T2)'s quantifier
over $\mathcal P_d$, pinning $\rho$ at one window-size profile, and (ii) to
certify the profile is realisable — never as a counterexample to a class
member's conclusion; scope is a predicate of a family, not of a pair. Consistent
with Remark 1.1 (verbatim from r2) and with [ESCALATED E1]: it chooses no
convention. Does not weaken either cap — and the r3 changelog states, correctly,
that the caps were deliberately *not* restated as scope-conditional, the ruling
having OVERRULED the objection that asked for that. PERMITTED, LANDED.

**H7 — Remark 2.1 (l. 250–259).** r2's "This is the only load-bearing form of
obstacle (ii) recorded in card S7" — the sentence the ruling named as false — is
gone. Replaced by: the pair-dependence/factorisation observation is "**this
artifact's own**", the card's obstacle (ii) is quoted in the card's own words,
§7.2's *Reading* is pointed at as the place that uses the card's sense.
CARD-adjudicated against `sources/S7-changfang26-card.md` l. 218–220: the quoted
clause ("non-canonicity of the maximum-degree window $T(A)$ across a
distribution's support, so that the union $T$ over a whole family is not bounded
and the argument must be run pairwise or with a covering step") is the card's
wording, with "maximum-degree window" a faithful gloss of the card's "$T(A)$ …
'some maximum-degree monomial set'" (card l. 140). §7.2's *Reading* (unchanged)
does use non-canonicity in that sense. Remark 2.1 is clean. **Tag: CARD.**

**H8 — Remark 4.3 (l. 477–488), pedantic P-b.** Adds the $\mathrm{Inf}_i(f_A)\le
\frac12$ derivation, restricts the asserted cap to $\theta\le\frac12$, notes
that at $\theta>\frac12$ the rule is identically empty so witness (b) supplies
no bound, and routes the excluded range to [ESCALATED E1] without choosing it.
N5 passes. Correctly does **not** import the ruling's "equality iff $i$ is
forced" parenthetical — see H13. PERMITTED, LANDED.

**H9 — §5.3 (l. 570–594).** Display replaced by the ruling's sentence (see H4);
two sentences added marking it as the record sentence and recording why the
omission was non-vacuous (N2 passes; the $\frac{d+1}{4(d-1)}$ figure is T6 at
denominator $2(d-1)$, as the ruling computed); "$\eta^*(d)\in[2^{-d},1]$ is open
(§8.2)" gains "; see the r3 note at the end of §8"; the closing instruction
becomes "**exactly as displayed, including its nonemptiness clause** — not a
summary of it, and not r2's version of it". One loose locution: F4. The
"*Consequence for R4*" paragraph above the display, with its $d_0(c,\alpha)$
criterion, is verbatim r2. PERMITTED, LANDED.

**H10 — DEPENDENCIES (l. 966, 979, 980).** S7 obstacle-(ii) row restated in the
card's words with the factorisation observation attributed to this artifact, and
"where" changed to "§7.2 *Reading* (the card's sense); Remark 2.1 cites the card
only to contrast it"; row still marked non-load-bearing (U-C1). Two rows added
(P-c): `0023-refuter-2` §2's master count (M) → Corollary 3.2, CERTIFIED, not
load-bearing; `0023-prover-3-u5` (L11) → [G4] and §7.4's localisation check, not
load-bearing. Both descriptions match [G4], Corollary 3.2 and the ruling. The
restated S7 row carries F2. PERMITTED, LANDED (F2).

**H11 — §8 record-keeping note (l. 885–908).** Labelled "(added in r3;
record-keeping only — nothing in §§1–8 is retracted, and no claim above is
conditioned on it)". Part (1) records §8.2/§8.5 as **superseded, not falsified**
by `0023-refuter-5` (flagged CERTIFIED, not verified) plus the triage's
exhaustive search at $(N,d)=(3,2),(4,2),(4,3)$ with $\min\pi_{\mathrm{Rel}}=1$
attained at $|S|=1$ — a faithful restatement of the ruling §5's extra check and
of E3, including leaving the ledger's CERTIFIED-vs-verified choice to the human.
Part (2) records the two killers as unconditional per-pair certificates. Item 2
and item 5 themselves are untouched, so no §8 statement changed. N6 passes; one
citation looseness: F5. PERMITTED (this is the "labelled record-keeping note").

**H12 — Changelog housekeeping.** r2's changelog heading becomes "CHANGELOG, r2
(each finding of `0023-prover-3-triage.md` → what changed)" with an added line
"*Retained here unaltered, for the record; the r3 changelog follows it.*"; its
body (U1–U10, P1–P6, "Preserved unchanged") is verbatim r2. PERMITTED.

**H13 — New r3 changelog (l. 1154–1248).** Maps U-A1, U-A2, U-B1, U-B2, U-C1,
P-a–P-d and the §8 note to the edits above; opens by declaring the text-only
scope and closes with "Not changed, deliberately" (E1 stays escalated, no
[SOURCE-BLOCKED] exists, SOURCE REQUEST remains none, both [MEMORY] items stay
flagged and unused). I checked each entry against the actual text: all accurate,
including the two "already carried it / unchanged" claims (§7.4's
"— for minimum-size selections; see [G5]" and [G5] itself were already in r2, so
U-A2 needed only the title and VERDICT 1; T8, VERDICT 2(ii) and Remark 4.2$'$
already carried both hypotheses, so U-A1 needed only the three flagged places).
*Observation, not a finding:* the changelog is silent about the declined
"equality iff forced" gloss, so r3 carries no trace of why it was omitted. The
ruling raised that gloss only inside its own P-b verification aside, never as a
required edit, so silence is within mandate — and per N7 the gloss is false in
the "only if" direction, so importing it would have introduced a genuine error.
Declining was right. PERMITTED.

**Checks 1 and 5, explicitly.**
*Scope (check 1):* the change set is confined to the title; VERDICT clauses 1, 3
and 5; §5.3's display and its two flanking sentences; Remark 1.1$'$ (new),
Remark 2.1, Remark 4.3; three register rows; the labelled §8 note; and the
changelog/preamble housekeeping. **No theorem statement, constant, proof,
witness table or declared gap was touched** — verified by direct comparison, not
from the changelog. No class-B finding. The only item outside the enumerated
list is H2's preamble paragraph, which is provenance prose.
*PARTIAL and gaps (check 5):* `status: PARTIAL` in the front matter and
"**PARTIAL.**" opening the VERDICT, both unchanged; [G1], [G2], [G3], [G4], [G5]
present and character-identical to r2, together with [MEMORY], [ESCALATED E1]
and the "no [SOURCE-BLOCKED] item" line; SOURCE REQUEST still "None". Nothing
was discharged, downgraded or added.

**Outside this pass's mandate.** I found no mathematical error in the caps, the
witness tables or the certificate arithmetic, and I did not re-derive them. F3
and F4 are the only places where a changed sentence brushes against the
mathematics, and both are presentational.

## 4. SOURCE REQUEST

None. The only external dependency this pass adjudicated is
`sources/S7-changfang26-card.md`, which is in-repo and was read here in full
(including the S7b addendum).

### END OF ARTIFACT 0023-prover-3-r3-verify-H ###
