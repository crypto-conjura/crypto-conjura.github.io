---
id: 0023-prover-3-triage
agent: triage
model: claude-opus-5[1m]
cycle: 3
---

# Triage ruling on `0023-prover-3.md` (internal barrier for rung R2 / I02), verification round 1

Inputs ruled on: `0023-prover-3-verify-{A,B,C,D,E}.md`. Raw verdicts as filed:
A NOT CLEAN (no class B), B CLEAN, C CLEAN, D DEFECTS, E DEFECTS.

Adjudication was done on the mathematics, with exact-arithmetic re-derivation
(`Fraction`, brute-force enumeration over the full cube) for every disputed
computational claim, and by reading the campaign files the blind passes could not
see (`0023-strategist-2` for P1/P5 fidelity, `0023-prover-1` for
$\mathcal C^{\mathrm{junta}}_d$, `0023-refuter-3` §§4–5.3, `PROGRESS.md` for the
rung classes, and the source cards under their real filenames).

**TALLY: 10 UPHELD / 9 OVERRULED / 6 PEDANTIC / 0 NEEDS SOURCE / 0 UNCLEAR.**

**Per pass, is anything UPHELD?**
A — **no** (2 PEDANTIC, 1 OVERRULED; its one "no repair needed" wording flag is
upheld only in D's/E's sharper form). B — **yes, one** (the S7b citation defect);
B's CLEAN verdict is nonetheless **wrong**: it affirmatively cleared four items
now upheld. C — **yes, two** (verdict quantifiers; S7b); C's CLEAN verdict is
likewise **wrong**. D — **yes, seven**. E — **yes, seven**. The two DEFECTS
passes carry essentially all of the value of this round.

---

## 1. FILTERED REPORT (UPHELD + PEDANTIC only)

### UPHELD

**U1 — class (A), scope overclaim. The title and both R4 sentences quantify over
the whole class $\mathcal W$.** Sources: E-F1 (class A); D-F13 (filed as
pedantic — **that classification is overruled**, and STATEMENT DRIFT is never
pedantic in any case).
Locations: title "*per-coordinate window-payment arguments cannot beat
$\mathrm{poly}(d)2^{-d}$*"; §5.3 "*the class cannot deliver R4's sub-exponential
target either*"; VERDICT 3 "*the class cannot deliver R4 either*".
Ruling: what is proved is that **two** D2 sub-classes (relevance-denominated;
own-heavy above $\tfrac1{2(2^d-1)}$) are capped. §7 exhibits three localised
members of $\mathcal W$ (max-degree-monomial-support, minimum certificate,
$W_{\max}$) that no cap in the artifact touches, and §8.2 leaves
$\eta^*\in[2^{-d},1]$ open; E-F1 adds a fourth (per-function case-split window)
and I confirm it is inside D4. So the title's first clause is contradicted by the
artifact's own §7, and the two R4 sentences are false as written. The VERDICT's
opening sentence ("refuted as a barrier for the whole window-payment class") is
the correct scope; the title and §5.3/VERDICT 3 must be rewritten over the two
sub-classes. **Ladder consequence, stated exactly:** the campaign may **not**
record R4 (or R2, R3, R5, R6′) as condemned. What it may record is: *no
relevance-denominated window-payment argument, and no own-heavy-at-$1/\mathrm{poly}(d)$
window-payment argument, can establish R4's target $c\,e^{-d^\alpha}$ (or any
threshold above $(d+1)2^{-d-1}$ resp. $\tfrac1{2(2^d-1)}$) in the object class of
R2, R3, R4, R5, R6′ or R6($\mathbb Z_2$).* That conditional form **is** proved
(see §3, item 4).

**U2 — class (B), T2/D5's empty-window branch is invalid; every "$V=0$" claim
falls.** Source: E-F2 alone. (D-F12 saw the same sentence and ruled it "correct
under D4's stipulation"; **that ruling is overruled**. A, B, C cleared it.)
Location: T2's proof, "*the point masses at $f_{A_0},f_{B_0}$ form an
incompatible family with zero denominator, so $T\le0=V_W(d)$*", and D5's ":=0"
clause.
Re-derived ruling: an argument in $\mathcal W$ must prove *"every family with
$\max(\delta_{\mathbf F},\delta_{\mathbf G})<\delta(d)$ is compatible"*. A
degenerate family (all windows empty, hence $\pi_W\equiv0$, hence $\rho(0,0)\le0$
and the count reads $0\le0$) defeats the argument **only if it is in scope**,
i.e. only if its own $\max\delta$ is below the threshold claimed. At $(A_k,B_k)$
as point masses $\max\delta=1/4$; at $(C,D)$, $1/2$. Every threshold in play is
$<1/(2d)\le1/4$ for $d\ge2$, so these families are out of scope and refute
nothing. The sound ceiling is
$T\le\min\bigl(\Theta_W(d),\ \inf\{\max(\delta_{\mathbf F},\delta_{\mathbf G}):
\text{incompatible},\ \text{all windows empty}\}\bigr)$, a positive number in
general — not $0$.
Casualties (all must be deleted or restated): D5's zero clause read as a barrier
statement; T6's "$V_W(d)=0$ if $W(A_k)=W(B_k)=\emptyset$"; T8's "*If also
$W(C)=\emptyset$ … $V_W=0$*"; Remark 4.3's "*for $W_{\mathrm{Forced}}$ in fact
$V=0$*"; §6.2's "*over $\mathcal P_d$ one has $V_{W_{\mathrm{Forced}}}=0$*".
**Survivors:** CAP I(a),(b),(c) (their hypotheses force a nonempty — indeed
large — window at the address pair) and CAP II whenever $W(C)\ne\emptyset$. In
particular $W_{\mathrm{Forced}}$ **is still capped at $\tfrac1{2(2^d-1)}$** by
witness (b) ($\mathrm{Forced}(C)=[d]\ne\emptyset$); only the strictly stronger
"establishes nothing at all" claim is unproved. Net damage to the campaign-facing
content: small; damage to the artifact's text: five sentences.

**U3 — class (B), the quantitative escape figures are not proved: "value" is an
infimum, and only two pairs were evaluated.** Sources: E-F3 (B); D-F8 (C).
Location: VERDICT 1, "*the shattering-window functional (P1) has **value**
$\ge1/8$ and $>1/4$; the certificate functional (P5) has **value**
$\ge1/(2(d+1))$*".
Ruling, precisely. $V_W(d)$ is defined (D5) as an infimum over **all** of
$\mathcal P_d$. A ratio computed at one pair is an **upper** bound on that
infimum; §7 computes two such ratios. So no lower bound on any $V_W$ is proved
anywhere in the artifact, and the quoted sentence is unproved. It is also
internally inconsistent: $V_{W_{\mathrm{sh}}}\le\eta^*$ (T3), so
"$V_{W_{\mathrm{sh}}}\ge1/8$" would settle $\eta^*(d)\ge1/8$ — exactly what §8.2
records as open and §8.5 invites the reader to attack.
**What the escape ruling DOES support** (this is the form the campaign must
carry, and it is fully proved):
> At the two certified witnesses the caps' *hypotheses fail* for
> $W_{\mathrm{sh}}$ and for the minimum-certificate window — on witness (a) the
> relevance density is $d/(2^{d-1}+d-1)=2^{-\Theta(d)}$, so CAP I(b) degrades to
> $\approx(d+1)/(4d)$, vacuous against the $1/(2d)$ grid ceiling; on witness (b)
> the window is own-cheap ($W_{\mathrm{sh}}(D)=[d]$, $T_D(y)=\{i\}$), so CAP II's
> hypothesis fails and T9 gives $\ge\frac1{4d}$ there. Hence **P1 and P5 are not
> capped by CAP I or CAP II, and in particular not by the two witnesses that kill
> the relevance-denominated and own-heavy routes.**
**What it does NOT support:** "P1 has value $\ge1/8$", "P5 has value
$\ge1/(2(d+1))$", or any claim that P1/P5 achieve an inverse-polynomial payment.
$V_{W_{\mathrm{sh}}}(d)\le\eta^*(d)\in[2^{-d},1]$ remains open, and (PAY$\star$)
at $p=1$ remains the open milestone of §8.5. Read as "not capped by these
witnesses" the clause is correct and is the campaign-critical finding; read as
"value bounded below" it is false. The VERDICT must say the former.

**U4 — class (B), the minimum-certificate uniqueness claim is false (two
independent passes; confirmed here by exhaustive enumeration).** Sources: D-F1,
E-F4. (B and C both affirmatively cleared §7.4; both are wrong.)
Location: §7.4, "*the **unique** minimum certificate of $x\in A_k$ is
$\{a_1..a_k,y_{b(a)}\}$ (size $d$) … So the payment equals P1's,
$\frac k2+2^{-k}$*".
Verified by brute force over the whole cube for $k=1,2,3$ (all $x\in A_k$, all
certificates, exact fractions): minimum certificate **size** is indeed
$\min_U\bigl(k-|U|+2^{|U|}\bigr)=k+1=d$, but the **number** of minimum
certificates per point is $1,2,\dots,k+1$ depending on $x$ (observed multisets:
$k=1$: 1–2; $k=2$: 1–3; $k=3$: 1–4). Freeing one address bit $a_t$ and fixing
both reachable targets is a second certificate of size $d$ whenever
$y_{b(a)\oplus e_t}=+1$ at $x$. So uniqueness is false, and the quoted
justification establishes only irredundancy, not minimality of size (which needs
the $p+2^{k-p}$ minimisation, nowhere performed).
Downstream damage, ruled exactly:
* **Falls:** the exactness of §7.4's payment ("equals P1's, $\frac k2+2^{-k}$")
  and the printed $1/4,5/24,13/64$; and §7.5's characterisation "*$i\in\Sigma$
  iff …*" with its average $\frac k4+4^{-k}$ — both hold only for the declared
  $U=\emptyset$ selection (D-F2, upheld as part of this item).
* **Survives:** the escape conclusion. I computed the **worst** ratio over all
  points and all minimum-certificate selections on both sides:
  $1/4,\ 1/6,\ 5/32$ for $k=1,2,3$, i.e. $\min=5/32>1/8$; in general the
  worst selection is $|U|=1$ on both sides, giving
  $\bigl[\tfrac{k-1}2+2^{1-k}\bigr]/\bigl(2(k+1)\bigr)\ge\tfrac18$ for all
  $k\ge1$ (equivalent to $k\ge3-2^{3-k}$). So "ratio $\ge1/8$ at witness (a)"
  is true for **every** minimum-certificate selection and is repairable in two
  lines.
* **Survives untouched:** witness (b)'s values ($T_C=[d]$ is the unique minimum
  certificate; $T_D(y)=\{i\}$; $\pi=\frac12+\frac d{2(2^d-1)}$ over $d+1$; exact
  $5/18,5/28,19/150$), the hypothesis-failure half of §7.4 (own-cheap $T_D$),
  §7.5's worst-case $2^{-k}$ and hence the drafting warning ("P5 must stay
  averaged"), and all of §§2–6, §7.1–7.3, §8.
* Required repair: state the certificate notion (**minimum** vs the plan's
  **minimal**, see §2 note 3) and the selection rule, or quantify over all
  selections and use the $5/32$ bound.

**U5 — class (B), non-load-bearing: "*both caps sit far below the grid ceiling
$\frac1{2d}$*" is false for CAP I at small $d$.** Source: D-F3 alone (A, B, C
cleared it; E's log explicitly asserts "*Both caps also lie below $\frac1{2d}$.
ACCEPTED*" — a false affirmative clearance).
Verified exactly: $(d+1)2^{-d-1}$ vs $\tfrac1{2d}$ gives
$d=1:\ \tfrac12=\tfrac12$ (not below, equal); $d=2:\ \tfrac38>\tfrac14$;
$d=3:\ \tfrac14>\tfrac16$; $d=4:\ \tfrac5{32}>\tfrac18$; first strict
$<$ at $d=5$ ($\tfrac3{32}<\tfrac1{10}$). CAP II's $\tfrac1{2(2^d-1)}$ satisfies
the comparison for all $d\ge2$. The sentence is a self-check, used nowhere, and
the *consequential* direction of §6.4 (both caps lie **above** K1's $2^{-d}/d$)
is correct and re-verified. Repair: restrict to "for $d\ge5$", or drop.

**U6 — class (D), citation defect: the S7b dependency row, plus an incomplete
dependency register.** Sources: B-1, C-2, D-F4, E-F11 (first half), A-2 (in
part).
Card `S7-changfang26-card.md` (read here in full, S7b addendum inline) records
Theorem 1.2 as "*$\mathrm{supp}(f)$ shatters $S^c$*" and Corollary 3.4 as
"*$\dim_\pi(\mathrm{supp}f)+\deg_{\hat G}(f)\ge n$*". **Neither states** that a
maximum-degree monomial support has size $\le\deg$; that is true by the
Contract's own definition of degree. So the row misattributes a definitional fact
and wrongly marks it "**load-bearing: yes**". Repair: delete "by theorem, card
S7b" in §7.1, replace with the one-line definitional remark, and mark the row
non-load-bearing (or re-purpose it to the projection property, which §7.1
explicitly does not use). Also required in the same table:
(i) give the **card filenames** (`S6-junta-degree-card.md` for S6a/S6c/S6d,
`S7-changfang26-card.md` for S7/S7b) — see the process note, §4;
(ii) the register lists `0023-refuter-3` **§4** only, while the text cites §5.1,
§5.2 and §5.3.

**U7 — class (C), VERDICT 2 drops three material qualifiers.** Sources: C-1,
D-F7. Repair the one-line summary to match the theorems: (i) $(d+1)2^{-d-1}$ is
T6(a), i.e. density $c=1$; at density $c$ the ceiling is T6(b)'s
$(d+1)/(c2^{d+1})$; (ii) T8 needs the **strict** $\theta>\tfrac1{2(2^d-1)}$,
hence "for all $d\ge d_0(\theta)$" when $\theta=1/\mathrm{poly}(d)$ (Remark 4.3
has this; the verdict drops it); (iii) the **object-class relativisation** is
missing: T6/T8 bound $V_W$ over $\mathcal P_d(\mathcal C^{\mathrm{ind}}_d)$, and
without that qualifier the sentence would condemn frozen R1 — the artifact's own
§6.1 exemption depends on the omitted quantifier.

**U8 — class (C), the two "surviving functional needs (α) and (β)" glosses are
not the conditions proved.** Sources: D-F10, E-F6. (α) "*a relevance-independent
size bound*" is **not** what T6 leaves open: by T6(c) a relevance-independent
bound of $2^{\varepsilon d}$ is still capped at $(d+1)2^{-\varepsilon d}/2$; the
condition is a **sub-exponential (effectively $\mathrm{poly}(d)$) window size on
the address family**. (β)'s content is the quantitative
"$W(A)$ contains an $i$ with $\mathrm{Inf}_i(f_A)\le\tfrac1{2(2^d-1)}$", not a
disposition. Likewise T9's "*the decisive question for a plan*" must be scoped:
T9's test is necessary and sufficient to escape **witness (b)** only — §8.1's
$\eta^*$ ceiling binds every localised $W$ regardless, and CAP I bites through a
different mechanism (Remark 4.5 says so). §7.1/§7.4 do the checks
quantitatively, so the mathematics is right; the advertised conjunction is a
paraphrase and must be stated as the two quantitative negations.

**U9 — class (C), an undeclared scope hole at the rung's own central question:
the mass-denominated form of I02's flagged route is condemned by neither cap.**
Sources: D-F9, E-F9 (independent agreement).
I02 flags charging payment "*against influence **mass** rather than against a
bounded window*" ($\sum_i\mathrm{Inf}_i\le d$). D4(T3) admits only
$\delta_{\mathbf F},\delta_{\mathbf G}$ and window **sizes** as quantitative
inputs, so a mass-denominated count is outside $\mathcal W$ by construction and
is capped by nothing here. Only the *thresholded* reading ("the coordinates
carrying a $1/\mathrm{poly}(d)$ share of the budget") is covered, via CAP II
(Remark 4.3, correct). [G1]'s list of non-members does not name it. Repair: name
it in VERDICT 2 next to the existing hedge and in [G1]. This is the single most
campaign-relevant omission after U1: the rung's central question is **not**
closed by this artifact, in either direction.

**U10 — class (C), light: §7.3's own-heaviness strictness.** Source: E-F7(a).
"*Neither relevance-denominated nor own-heavy at level $\ge\tfrac1{2(2^d-1)}$*"
is unproved as written (the only available bound, T4(c), gives $2^{-d-1}$, which
sits just **below** $\tfrac1{2(2^d-1)}$, so the "$\ge$" claim is undecided). The
claim the argument needs — and which does follow from T7, since witness (b)'s $D$
attains the level exactly — is "not own-heavy at any level **strictly above**
$\tfrac1{2(2^d-1)}$", which is precisely what CAP II requires. One-word fix.

### PEDANTIC (note; no rewrite required)

* **P1.** Remark 4.2(b)'s "$\mathrm{Forced}(D)=\emptyset$" fails at $d=1$
  ($D=\{x_1=-1\}$ forces $x_1$) — A (class B) and D-F11 (class C). Verified
  false at $d=1$; verified harmless: T8 at $d=1$ needs $\theta>\tfrac12$, which
  is the identically-empty window ($\mathrm{Inf}_i(f_A)\le\tfrac12$ always),
  Remark 4.3 is stated for $d\ge d_0(\theta)$, and §6.2 uses the address pair
  ($d\ge2$). Add "for $d\ge2$" while revising. (A's class-B grading is downgraded;
  E's log clearance of this line at all $d$ is a second false affirmative.)
* **P2.** §7.5 does not spell out the relation between $\pi_\Sigma$ and D3's
  $\pi_W$ (A). One line suffices and is correct:
  $\Sigma(x,y)\subseteq T_A(x)\cap T_B(y)=W(A)\cap W(B)$ and influences are
  $\ge0$, hence $\pi_\Sigma\le\pi_W$ — which is exactly what makes the caps bind
  P5's actual averaged inequality.
* **P3.** §5.4's even-order pullback is asserted with a parenthetical (B-3).
  It is correct: $\hat\varphi$ is injective on duals, so degree, coefficients,
  influences, $\alpha$ and disjointness are preserved, and a finite abelian group
  has a $\mathbb Z_2$ quotient iff its order is even. C, D and E each re-derived
  it. One added clause if convenient.
* **P4.** $W_{\max}$'s localisation silently narrows D1 to pairs in
  $\mathcal P_d$ (E-F7(b)): on the full cube $\mathrm{Rel}=\emptyset$ while
  $W_{\max}=[N]$. Define $W_{\max}(A):=\emptyset$ when $\mathrm{Rel}(A)=\emptyset$.
* **P5.** Remark 4.4's bolded "*necessary* but not sufficient" carries its
  attribution two lines earlier, not in the bolded sentence (E-F5). I verified
  `0023-refuter-3` §5.2 does refute the min-form (HEAVY$_\theta$) route via
  $\theta^*(d)\le\tfrac1{2(2^d-1)}$, tagged CERTIFIED (not verified) in the
  register; so the claim is properly inherited. Say "inherited from refuter-3
  §5.2" in the bolded sentence.
* **P6.** §5.3's "$(d+1)2^{-d-1}<c\,e^{-d^\alpha}$ for all large $d$" gives no
  explicit $d_0$ (E-F10, in part). True as stated; an explicit $d_0(c,\alpha)$
  would be better.

---

## 2. OVERRULED (with the error named)

1. **The four "missing card" (E)-class findings — A-2, C-3, E-F11 (first half),
   and D-F14's code/unit-file item — are OVERRULED.** The cards exist and were
   read here: `sources/S6-junta-degree-card.md` (blocks S6a–S6d) and
   `sources/S7-changfang26-card.md` (with the S7b addendum inline); B located
   both and was right. `0023-prover-3-code/check_witnesses.py` and units
   `u0–u5` also exist in `proofs/`. No source is unreachable, so **no finding is
   NEEDS SOURCE**. The residual defect is documentation, upheld under U6(i) and
   recorded as the process note in §4.
2. **B-2 (the "$1/(8d)$ vs $\ge1/(2d)$" tension) is OVERRULED.** Read
   `0023-refuter-3` §5.1: it proves both "forcing-only incompatible families
   never beat $1/(2d)$" and "any family with $\Pr[\text{forcing}]\ge\frac12$ has
   $\max\delta\ge1/(8d)$". The artifact's inline $\ge\tfrac1{2d}$ on the forcing
   sub-class is consistent with, and is the same computation as, refuter-3's; no
   defect.
3. **D-F5 and E-F10 (the R3–R6′ scope chain "unverifiable") are OVERRULED as
   defects.** Both were honest blind-scope flags, and I resolved them:
   `PROGRESS.md` defines R3 (nonnegative unit-norm degree-$d$), R4 (full signed
   class, target $c\,e^{-d^\alpha}$, $\alpha<1$), R5 (signed, point masses, at
   the inverse-polynomial frontier), R6′ ($\mathbb Z_2$, $\mathbb R$-valued,
   arbitrary finite support). The two witnesses are unit-norm, nonnegative,
   $\{0,\text{const}\}$-valued, degree $\le d$ **singleton** pairs, hence
   admissible in each of those classes; with §5.2 (monotonicity, direction
   verified correct and non-inverted by four passes and by me) the caps do hold
   verbatim in every one of those object classes, and the R4 numeric comparison
   is correct. §5.3's *mathematics* stands. Only its **quantifier** is wrong, and
   that is U1, not F5/F10. Add `PROGRESS.md` to the register (U6).
4. **D-F6 and the "unadjudicable" half of E-F5 (the §6.1/§6.2/Remark 4.4
   descriptions of I01 and refuter-3) are OVERRULED.** I read both artifacts:
   §6.2's characterisation of refuter-3 §5.1 as "the window-payment argument with
   $W=W_{\mathrm{Forced}}$ restricted to forcing pairs" is faithful (refuter-3
   §5.1 splits $\mathrm{supp}\,\mathbf G$ into forcing/non-forcing and its bound
   is conditioned on $\Pr[\text{forcing}]$), and §6.1's description of R1's engine
   matches `0023-prover-1`. Register incompleteness only (U6(ii)).
5. **E-F8 ("witness (b) is not in $\mathcal C^{\mathrm{junta}}_d$") is
   OVERRULED.** `0023-prover-1` defines
   $\mathcal C^{\mathrm{junta}}_d=\{\mathbf 1_A/\lVert\cdot\rVert: A=\{x:x_J\in
   P\},|J|\le d,\emptyset\ne P\subseteq\{\pm1\}^J\}$ — an arbitrary **pattern
   set** $P$, i.e. all $d$-juntas, not a single cylinder pattern. $D=C^c$ is
   $\{x:x_{[d]}\in P\}$ with $P$ = all patterns but one. So §6.1's "witness (b)
   **is** in that class" is true, and the artifact's calibration reasoning there
   is exactly right. E read I02's shorthand "cylinder-pattern class" too
   narrowly.
6. **E-F11 (second half) — "§7.1 may have evaluated a DIFFERENT functional from
   P1's" — is OVERRULED; see §3 item 6 for the full ruling.**
7. **C-4 (plan-fidelity caveat) is DISCHARGED, not upheld**; see §3 item 6, with
   one residual note carried into U4 (minimum vs minimal certificates).
8. **D-F12 ("$V_W=0$ is correct under D4's stipulation, flag as
   model-relative") is OVERRULED**: the inference is not correct even under the
   stipulation, for the reason given in U2. D identified the right sentence and
   drew the wrong conclusion; E's F2 is the correct analysis.
9. **A's finding 3 as filed ("textually correct… no repair needed") is
   OVERRULED**: the VERDICT-1 "value" sentence is a defect, not a wording risk
   (U3). A's instinct was right and its ruling was wrong; a verifier is not
   entitled to clear a false claim as a style matter.

Also recorded, as a matter of record rather than a finding: **B's and C's CLEAN
verdicts are both incorrect.** B affirmatively cleared U2, U3, U4 and U5 (its
§7.4 line — "self-contained (explicit certificates on both witnesses)" — is a
false clearance of an enumerable claim); C affirmatively cleared U2, U4 and U5
and states it "re-derived §7.4/§7.5's certificate-window computations". Neither
ran code; both certified an enumerable, false uniqueness claim. In the conflicts
between the CLEAN pair (B, C) and the DEFECTS pair (D, E): **D/E are right** on
§7.4 uniqueness, §6.4's grid-ceiling sentence, the value-vs-ratio inversion and
(E alone) T2's empty-window branch; **B/C are right** on the cards being
locatable and non-blocking, and B is right that no external upload is needed.

---

## 3. The six directed items, ruled

1. **E's F2 / the empty-window case — E is right, the artifact is wrong.**
   UPHELD as U2, with the exact repair and the exact blast radius given there:
   CAP I(a)–(c) and CAP II's main branch are untouched; the five "$V=0$"
   sentences fall; $W_{\mathrm{Forced}}$ remains exponentially capped by witness
   (b). The reason the artifact's inference fails is quantitative, not
   philosophical: the degenerate families it invokes have $\max\delta\in\{1/4,1/2\}$,
   above every threshold at issue, so they lie outside the scope of the statement
   an argument in $\mathcal W$ must prove.
2. **E's F3 / the quantitative escape figures — E is right.** UPHELD as U3. The
   escape ruling supports "**P1 and P5 are not capped by CAP I, CAP II, or the two
   certified witnesses**" — i.e. the strategist's §0.6 ruling that the S7b route
   is live is confirmed, and the campaign's lead plan is **not** dead. It does
   **not** support "value $\ge1/8$" / "value $\ge1/(2(d+1))$" or any lower bound
   on $V_{W_{\mathrm{sh}}}$ or $V_{\text{cert}}$; those would settle §8.2's open
   bracket. Campaign-facing wording: *not capped by these witnesses*, never
   *value bounded below*.
3. **D's and E's shared finding on minimum-certificate uniqueness — both are
   right; confirmed by exhaustive enumeration.** UPHELD as U4, with the surviving
   identities enumerated there (escape conclusion survives at $5/32>1/8$ for
   every selection; witness (b) untouched; §7.5's worst case and the "P5 must
   stay averaged" warning untouched; the *exact* payment identity and §7.5's
   $\Sigma$-characterisation fall). Note for the orchestrator: this is a case
   where two independent passes report the same genuine class-B error, but the
   **fast-refute rule (§3.5) must not fire** — the duplicated defect is contained
   inside one escape computation, it does not touch the barrier's core or the
   escape's conclusion, and this artifact is not a rung attempt.
4. **E's F1 / scope overclaim — UPHELD (U1), and the ladder record must say so.**
   Do **not** record R4 as condemned. Record the conditional form given in U1.
   Given U1 and U9 together, the honest ledger line is: *two window-payment
   sub-classes are dead at every rung's object class; the class $\mathcal W$ as a
   whole is not capped, and the mass-denominated form of I02's own flagged route
   is not capped either.*
5. **D's grid-ceiling finding — UPHELD (U5).** Exact arithmetic:
   $(d+1)2^{-d-1}=\tfrac12,\tfrac38,\tfrac14,\tfrac5{32}$ vs
   $\tfrac1{2d}=\tfrac12,\tfrac14,\tfrac16,\tfrac18$ at $d=1,2,3,4$ — equal at
   $d=1$ and strictly larger at $d=2,3,4$; first strictly below at $d=5$. D is
   right and A/B/C/E's clearances of that sentence are wrong.
6. **E's F11 second half — OVERRULED. The artifact evaluated the lead plan's
   functional, not a different one.** This is the item that steers the campaign,
   so the evidence, from `0023-strategist-2` (which the blind passes could not
   read):
   * §2's V1 table defines the plan's window verbatim as "**shattering window**
     $W(A)$ | *any maximum-degree monomial support*; $A$ surjects onto
     $\{\pm1\}^{[N]\setminus W}$ | size $\le d$ | card S7b".
   * P1's key step (PAY$\star$) is quantified over "*every pair of
     maximum-degree monomial supports*".
   So P1's window **is** a maximum-degree monomial support; the surjectivity
   ("shattering") is a *property* of that window supplied by Chang–Fang, used
   elsewhere in P1 (its positivity lemma G1), not an alternative definition. The
   artifact's §7.1 ("$W_{\mathrm{sh}}(A)=$ any maximum-degree monomial support …
   the projection property is not used") and its "independently of the choices"
   are exactly faithful, including the quantification over selections. E's
   alternative reading (a *maximal shattered set*, i.e. the Chang–Fang object
   $S^c$) is also excluded on size grounds: that set has size $\ge N-d$, whereas
   P1's whole point is a window of size $\le d$ uniformly in $N$. **The escape
   ruling therefore applies to the lead plan as intended.** The name
   "shattering window" is the campaign's own established shorthand (strategist
   V1), so no rename is needed; adding the half-line "$=$ a maximum-degree
   monomial support, in the sense of `0023-strategist-2` V1" would close the
   ambiguity for good.
   Residual fidelity note (carried into U4, not a separate finding): P5's plan
   uses **minimal** certificates and an averaged inequality over
   $x\sim\mathrm{Unif}(A),y\sim\mathrm{Unif}(B)$ with payment over $\Sigma(x,y)$;
   §7.4 evaluates **minimum**-size certificates. Both are localised and both are
   inside Remark 2.2, and §7.5 correctly evaluates the plan's $\Sigma$-form, so
   the escape ruling transfers — but §7.4 must say which notion and which
   selection it evaluates.
7. **A's $d=1$ remark and the citation defects — PEDANTIC (P1) and UPHELD (U6)
   respectively**, as detailed above.
8. **Spot-check of the affirmative clearances — done, and it changed the
   outcome**: see the closing paragraph of §2. Two of the five passes certified
   as CLEAN an artifact containing four upheld defects, one of them (U4)
   decidable by a ten-line enumeration that neither ran. Weight the CLEAN
   verdicts of B and C accordingly in the tally.

---

## 4. PROCESS NOTE (not a finding against the artifact's mathematics)

Four of the five passes (A, C, D, E) read files outside the blind-verifier view
— `LEDGER.md` and/or `PROGRESS.md` — and all four self-disclosed it. In every
case the purpose was the same: **to recover source-card filenames that the
artifact cites only by internal block id** (S6a, S6c, S6d, S7b), and, for D/E,
the rung definitions R3–R6′. Three passes then filed class-(E) "card
unreachable" findings that are simply false (the cards exist as
`S6-junta-degree-card.md` and `S7-changfang26-card.md`, the latter carrying the
S7b addendum inline); one pass (B) guessed the filenames and cleared them.

Root cause: the artifact's DEPENDENCIES table names blocks, not files, and §5.3
names rungs defined only in `PROGRESS.md` without restating them. The fix belongs
in the artifact's dependency table (U6), not in the verifier prompt: every row
must carry the **path** of the card or artifact it cites, and any row citing a
rung class must either restate the class in one line or cite `PROGRESS.md` by
path and section. With that in place a blind pass has no incentive to step
outside its view, and the three spurious (E) findings of this round disappear.
No blindness violation is charged against any pass; the leakage was disclosed,
was confined to filename/label recovery, and did not import a prior verdict or
the prover's reasoning.

---

## 5. ESCALATION LIST (human)

No finding is UNCLEAR; both items below are adjudicated above and are escalated
for **ratification**, because each changes something the human owns.

* **E1 — the repaired class model (U2).** Deleting the "$V=0$" branch changes
  D5/T2 and hence what "$\mathcal W$" means, which is [G1]'s stipulated content
  and the artifact's chief conceptual contribution. My ruling is that T2's
  ceiling becomes
  $T\le\min\bigl(\Theta_W,\ \inf\{\max\delta:\text{incompatible, all windows
  empty}\}\bigr)$; the alternative (keep the convention but restate it as "the
  count is uninformative on such families", claiming nothing) is weaker but
  safer. Human picks; the reviser must not choose the class model on its own
  initiative.
* **E2 — the ladder record (U1, U9).** The line the campaign writes into
  `LEDGER.md`/`PROGRESS.md` about what is now condemned is a ladder-level
  commitment. My ruling: **R4 is not condemned**; the two sub-classes are
  condemned in every rung's object class; the mass-denominated form of I02's own
  flagged route is condemned by nothing here. Recommend the human paste the
  conditional sentence from U1 verbatim rather than any summary of it.

## 6. CONSOLIDATED SOURCE REQUEST

**None.** Every card and internal artifact cited by the artifact or requested by
a pass exists in the repository and was read during this triage
(`S1-acc22-card.md`, `S2-clm23-card.md`, `S6-junta-degree-card.md`,
`S7-changfang26-card.md` incl. S7b, `0023-strategist-2`, `0023-refuter-3`,
`0023-prover-1`, `PROGRESS.md`). D's three ranked "restatement requests" and E's
two are all resolved above and are **not** routed to the source queue; the
underlying need is a documentation fix inside the artifact (U6, §4). No external
upload is warranted.

---

## 7. RECOMMENDATION

**REVISE — one bounded cycle, wording-and-scope dominated, no new mathematics
required.** Rationale: this artifact will never be frozen as a rung; its job is
to steer plan selection. Its *machinery* is in good shape (five passes plus this
triage re-derived T1–T9, both witness tables and §7.2 independently; I found no
error in any of them). But four of the sentences the campaign would actually
cite — the title, "the class cannot deliver R4", "P1 has value $\ge1/8$", and the
"$V=0$" family — are exactly the defective ones. A steering artifact whose
headline is wrong is worse than no artifact, and the repairs are cheap.

Ranked instructions for the reviser (address in this order; change nothing
unflagged; do **not** weaken any theorem to close a gap):

1. **U1** — retitle and requantify: title, §5.3, VERDICT 3, over the two D2
   sub-classes; keep the VERDICT's existing "refuted as a barrier for the whole
   class" sentence and make the title agree with it.
2. **U3** — replace every "has value $\ge$" with "the caps' hypotheses fail at
   the two certified witnesses; neither cap touches it", and say in one clause
   that no lower bound on any $V_W$ is claimed.
3. **U2** — delete or restate the five "$V=0$" claims per the escalated model
   (E1); keep CAP II's cap on $W_{\mathrm{Forced}}$, which survives.
4. **U4** — fix §7.4: state the certificate notion and selection, drop
   "unique", replace the exact payment identity by the min-over-selections bound
   ($\ge5/32>1/8$; the $|U|=1$ selection is the worst), and scope §7.5's
   $\Sigma$-identity to the declared selection.
5. **U9** — name the mass-denominated exclusion in VERDICT 2 and [G1].
6. **U6** — repair the dependency table: S7b row (definitional, non-load-bearing),
   card and artifact **paths**, refuter-3 §5.1/§5.2/§5.3, `PROGRESS.md`.
7. **U7, U8, U10, U5** — the quantifier and gloss repairs, and the $d\ge5$
   restriction in §6.4.
8. **P1–P6** — fold in while touching those lines; none justifies a rewrite.

**What the campaign may rely on now, before the revision lands** (all
independently re-derived here): T1–T3 and the value theorem's non-empty case;
T5 and T7's exact tables; **CAP I(a)–(c)**; **CAP II with $W(C)\ne\emptyset$** —
so every own-influence-threshold window at $\theta\ge1/\mathrm{poly}(d)$,
including $W_{\mathrm{Forced}}$ and "the coordinates carrying a
$1/\mathrm{poly}(d)$ share of the influence budget", is dead **in sum form**,
which is the artifact's genuine advance over refuter-3; §5.1–5.2 and hence the
caps in the object classes of R2, R3, R4, R5, R6′, R6($\mathbb Z_2$), and §5.4's
group versions; **§7.2's non-canonicity theorem** (the cleanest new result here);
§8.1/8.2/8.4/8.5 including the cheap falsifiable milestone (search for a
cross-disjoint degree-$\le d$ pair with $\pi_{\mathrm{Rel}}<1$); and the escape
ruling **in its "not capped by these witnesses" form**, which confirms
`0023-strategist-2` §0.6: **P1 remains the lead plan and P5 remains live.**

**What the campaign may not rely on** until revised: any "$V=0$"/"establishes
nothing"; any "value $\ge$"; "the whole window-payment class cannot beat
$\mathrm{poly}(d)2^{-d}$"; "R4 is condemned"; §7.4's exact P5 payment identity
and §7.5's $\Sigma$-identity as unconditional; §6.4's grid-ceiling sentence.

Next action after the revision: re-verify only the changed sections (U1–U4 are
textual; U2's model change is the only one needing a fresh pass), then let the
Strategist proceed on P1's milestone (M1b: decide (PAY$\star$) at $p=1$, i.e.
hunt a pair with $\pi_{\mathrm{Rel}}<1$), which §8.5 has now made cheap and
which is the single highest-information next computation in this campaign.

### END OF ARTIFACT 0023-prover-3-triage ###
