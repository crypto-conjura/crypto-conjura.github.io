id: 0023-prover-3-verify-D
agent: verifier-b
model: claude-opus-5[1m]
cycle: 3

# Blind referee pass D on `0023-prover-3.md` (internal barrier for rung R2 / I02)

Inputs read: the artifact; `intermediates/I02-degree-d-sets.md`; `CONTRACT.md`;
cards `S1-acc22`, `S2-clm23`, `S6-junta-degree` (S6a–S6d), `S7-changfang26`
(+ S7b addendum). No other `proofs/` artifact was opened.

**Tooling note.** No Bash/execution tool was exposed in this session, so the
"exact arithmetic" recheck was done symbolically by hand in exact fractions and
is reproduced in §3 below at every value the artifact tabulates (k = 1,2,3 for
witness (a); d = 1..6 for witness (b); all escape ratios). Every number the
artifact prints was reproduced. Also: the harness file at `prompts/solve.md`
§3.5 contains **no step 0.5 and no CODE/MECH/CARD/NONE tag scheme**; I have
supplied a negation check and per-lemma adjudication tags in §3.6 on my own
reading of that instruction, and flag the mismatch.

---

## 1. FINAL VERDICT

**DEFECTS.** STEP 0 passes and the barrier's core survives — both caps are
correct with the right barrier quantifier order (witness fixed before the
functional), both witness influence tables recompute exactly, the scope
direction is right (caps travel *up* to larger classes and provably not *down*
to R1's junta class), and the two conceded successes (R1's bounded-window
cylinder result and the 1/(8d) forcing bound) genuinely fall **outside** D4 as
literally written, so the barrier is **not** false — but §7.4's "**the unique**
minimum certificate" claim is **false** (each x ∈ A_k has k+1 distinct
minimum certificates of size d), which unproves §7.4's exact-payment identity
and §7.5's Σ-characterisation as stated; §6.4's "both caps sit far below the
grid ceiling 1/(2d)" is **false at d = 2,3,4**; the load-bearing S7b citation
attributes a definitional fact to Chang–Fang Theorem 1.2 / Corollary 3.4, which
says nothing of the kind; and the advertised R3–R6′ scope chain plus the §6.1/§6.2
calibration descriptions of I01 and refuter-3 are **unverifiable** from the
permitted inputs.

---

## 2. FINDINGS TABLE

| # | Quoted location | Class | Explanation |
|---|---|---|---|
| F1 | §7.4: "the **unique** minimum certificate of $x\in A_k$ is $\{a_1..a_k,y_{b(a)}\}$ (size $d$): freeing an address bit moves the read, freeing the target lets it flip. So the payment equals P1's, $\frac k2+2^{-k}$" | **(B)** | False. Drop address bit $a_t$ and fix **both** targets $y_{b(a)},y_{b(a)\oplus e_t}$ to $+1$: this is a certificate of size $(k-1)+2=k+1=d$. In general a certificate fixing $p$ address bits needs $\ge 2^{k-p}$ targets, so size $p+2^{k-p}$, minimised at **both** $p=k$ and $p=k-1$: there are $k+1$ minimum certificates per point, not one. The quoted justification only shows the stated set is *irredundant*, and does not establish minimum size $d$ either (that needs the $p+2^{k-p}$ minimisation, which is nowhere performed). Consequence: "the payment equals P1's, $\frac k2+2^{-k}$" and the ratio "$\ge\frac18$" are **not established** for P5, since P5's window is "certificates of a random point" and the selection among the $k+1$ minima is unspecified. Blast radius is confined: the *hypothesis-failure* half of §7.4's last sentence (window size $=d$ for every minimum certificate; $T_D(y)$ own-cheap on witness (b)) is logically independent of the payment value, as is all of §§2–6 and §8. I do not assess whether a repair exists. |
| F2 | §7.5: "On witness (a), $i\in\Sigma$ iff ($i=a_t$, $a_t\ne a'_t$) or ($i=y_{b(a)}$ and $a=a'$), hence $\sum_{i\in\Sigma}[\dots]=\frac12|\{t:a_t\ne a'_t\}|+2^{-k}\mathbf 1\{a=a'\}$" | **(C)** | The displayed identity is correct **only** for the type-I certificate on both sides; by F1 that is a choice, not a fact, so the identity (and the worst-case $2^{-k}$ / average $\frac k4+4^{-k}$ that P5's drafting warning rests on) is proved for one certificate selection only. The averaging step itself checks out: under $x\sim\mathrm{Unif}(A_k)$ the address block is uniform (each $a$ has exactly $2^{2^k-1}$ completions), the two draws are independent, so $\mathbb E[\frac12\mathrm{dist}]=\frac k4$ and $2^{-k}\Pr[a=a']=4^{-k}$ — both as printed. |
| F3 | §6.4: "Both are far below the grid ceiling $\frac1{2d}$ (IG1) and below R2's target, as a barrier must be." | **(B)**, non-load-bearing | CAP I's ceiling $(d+1)2^{-d-1}$ **exceeds** $1/(2d)$ at $d=2$ ($3/8>1/4$), $d=3$ ($1/4>1/6$) and $d=4$ ($5/32>1/8$); it drops below only from $d=5$ ($6/64<1/10$). CAP II's $\frac1{2(2^d-1)}$ does satisfy the comparison for all $d\ge2$. The stated flat claim is therefore false for CAP I at three values of $d$. It is a self-check, not a premise: nothing downstream uses it, and the *consequential* direction of §6.4 (caps must lie **above** K1's proved $2^{-d}/d$) is verified correct — $2^{-d}/d\le(d+1)2^{-d-1}$ for $d\ge1$ (equality at $d=1$) and $2^{-d}/d\le\frac1{2(2^d-1)}$ for $d\ge2$. |
| F4 | DEPENDENCIES row: "**S7b** (card) \| Chang–Fang Thm 1.2 / Cor. 3.4: a maximum-degree monomial support has size $\le\deg$ \| CARD, READ \| §7.1 \| yes" | **(D)** | Misattribution. Card S7/S7b record Theorem 1.2 as "*$\mathrm{supp}(f)$ shatters $S^c$*" and Corollary 3.4 as "*$\dim_\pi(\mathrm{supp} f)+\deg_{\hat G}(f)\ge n$*". Neither states, nor needs to state, that a maximum-degree monomial support has size $\le\deg$ — that is true **by the definition of degree** (the card's own "does NOT say" list is explicit that the paper contains no other statement of this kind). The fact is harmless because trivially true, but the artifact marks this row *load-bearing for the escape claim*, and §7.1 leans on the words "$|W_{\mathrm{sh}}|\le d$ **by theorem**, card S7b". A referee reading the card cannot find the cited content. |
| F5 | §5.3: "they lie in $\mathcal C^{\mathrm{ind}}_d\subset\mathcal C^{+}_d\subset\{\mathbb R\text{-valued}\dots\}$, i.e. in the classes of **R2 ⊂ R3 ⊂ R4/R5/R6′ ⊂ R6($\mathbb Z_2$)** (`PROGRESS.md`)"; VERDICT 3 "**SCOPE (proved)**" | **(E)** | The rung classes R3–R6′ and R4's target $c\,e^{-d^\alpha}$ are defined only in `PROGRESS.md`, which is not among the permitted inputs and is not restated in the artifact. The *conditional* content is fine and I verified it: monotonicity 5.2 is correct as stated and in the correct direction, and $(d+1)2^{-d-1}<c\,e^{-d^\alpha}$ for large $d$. But "SCOPE (proved)" cannot be certified here: the inclusions are asserted, not exhibited, and "R5 needs no distributional part" presupposes a rung statement I cannot see. Load-bearing for verdict item 3 only. |
| F6 | §6.1 "R1's engine *is* a window-payment argument with $W\supseteq\mathrm{Rel}$ … payment $\ge1$, $|W|\le d$"; §6.2 "refuter-3 §5.1's $1/(8d)$ forcing bound … **restricted to forcing pairs** … exactly as declared"; Remark 4.4 "refuter-3 refutes the **$\min$-form** route … via $\theta^*(d)\le\frac1{2(2^d-1)}$" | **(E)** | Three descriptions of unreadable campaign artifacts. Partial corroboration is available and checks out: I02's frozen-inputs block gives R1 $=1/(3d)$ with tightness $1/(2d)$, and I independently recomputed that the grid pair has $\pi_{\mathrm{Rel}}/(|W_A|+|W_B|)=1/(2d)$ under $W=\mathrm{Rel}$, so §6.1's numbers are internally consistent. Not corroborable: that refuter-3 §5.1's $1/(8d)$ bound is *declared* restricted to forcing pairs (on which the whole R1 exemption / calibration turns), and the "$\min$-form is dead" half of Remark 4.4's "**necessary** but not sufficient". Note the DEPENDENCIES table lists only `0023-refuter-3` **§4** (the witnesses), not §5.1 or §5.3, though both are cited in the text — an incomplete dependency register. |
| F7 | VERDICT 2: "Every *relevance-denominated* window functional is capped at $(d+1)2^{-d-1}$ (**CAP I**, §3); every *own-heavy* window functional at level $\theta\ge1/\mathrm{poly}(d)$ is capped at $\frac1{2(2^d-1)}$" | **(C)** | Two dropped qualifiers, both present in the theorems and both material. (i) $(d+1)2^{-d-1}$ is T6(a), i.e. density $c=1$; at density $c$ the ceiling is T6(b)'s $(d+1)/(c2^{d+1})$, which is only $\mathrm{poly}(d)2^{-d}$ (the title's claim), not $(d+1)2^{-d-1}$. (ii) T8 requires the strict $\theta>\frac1{2(2^d-1)}$, i.e. $d\ge d_0(\theta)$ for $\theta=1/\mathrm{poly}(d)$ — stated in Remark 4.3, dropped in the verdict. (iii) Most important for a reader: both sentences omit the **object-class relativisation**. T6/T8 bound $V_W$ over $\mathcal P_d(\mathcal C^{\mathrm{ind}}_d)$; read without that, "every relevance-denominated window functional is capped at $(d+1)2^{-d-1}$" would condemn frozen R1 (relevance-denominated, $W\supseteq\mathrm{Rel}$, proving $1/(3d)$), and the artifact's own §6.1 exemption depends on the omitted quantifier. The theorems are correct; the one-line summary is not self-standing. |
| F8 | VERDICT 1: "the shattering-window functional (P1) has **value** $\ge1/8$ and $>1/4$; the certificate functional (P5) has **value** $\ge1/(2(d+1))$" | **(C)** | "Value" is a defined term (D5: $V_W(d)$, an infimum over **all** of $\mathcal P_d$). What §7.1/§7.4 establish are *ratios at two specific pairs*, which are upper-bound witnesses, never lower bounds on $V_W$. The preceding clause "On the two certified witnesses" mitigates, but the sentence as written invites exactly the inversion a barrier report must avoid (no lower bound on any $V_W$ is proved anywhere, and §8 correctly declines to claim one). |
| F9 | VERDICT 2: "This closes I02's own flagged route ('re-base R1's payment argument on the influence budget') **in its per-coordinate / per-relevant-coordinate form**, negatively"; GAP REGISTER [G1] | **(C)** | The qualifier is honest, but the register does not flag the resulting scope hole, and it is the rung's central question. I02 flags charging "*against influence **mass** rather than against a bounded window*". D4(T3) admits only $\delta_{\mathbf F},\delta_{\mathbf G}$ and window **sizes** as quantitative inputs, so the mass-denominated form of I02's route is outside $\mathcal W$ by construction and is condemned by neither cap. [G1]'s list of non-members ("level weights, hypercontractivity, coordinate correlations, pair-dependent windows, fibre renormalisation, variance identities, constructive witnesses") does not name it. Remark 4.3 covers only the *thresholded* reading of the budget (heavy coordinates → own-heavy → CAP II). |
| F10 | Remark 4.5 / VERDICT 1: "A surviving functional needs **both** (α) a relevance-independent size bound and (β) own-cheap charging" | **(C)** | Informal glosses standing in for the literal negations the proofs use. The negation of T6's hypothesis is quantitative smallness of $|W(A_k)|+|W(B_k)|$: by T6(c) a *relevance-independent* bound of $2^{\varepsilon d}$ is still capped at $(d+1)2^{-\varepsilon d}/2$, so (α) as worded is not the condition established; the condition is sub-exponential (effectively $\mathrm{poly}(d)$) window size on the address family. Likewise (β)'s content is "$W(A)$ contains a coordinate with $\mathrm{Inf}_i(f_A)\le\frac1{2(2^d-1)}$", not a disposition. §7.1 does check both quantitatively, so the mathematics is where it should be; the *conjunction advertised in the verdict* is a paraphrase. Insufficiency of the min→sum move **is** properly proved (T8 exhibits capped sum-form functionals); its "necessity" half is not (see F6). |
| F11 | Remark 4.2(b) / Remark 4.3: "$\mathrm{Forced}(C)=[d]$, $\mathrm{Forced}(D)=\emptyset$" | **(C)**, pedantic | Fails at $d=1$, where $D=\{x_1=-1\}$ forces $x_1$. Everything using it is stated for $d\ge2$ or "$d\ge d_0(\theta)$", so nothing breaks. |
| F12 | D5 / T2: "$V_W(d):=0$ if some pair has both windows empty"; §6.2 "over $\mathcal P_d$ one has $V_{W_{\mathrm{Forced}}}=0$" | **(C)**, model-relative | Correct **under** D4's stipulation (an argument whose only tool is the count derives nothing from a family with zero denominator, hence proves R2 at no positive $\delta$), but note what it is not: the address singleton family it invokes has $\max_i\mathrm{Inf}_i=1/4$, so it never violates R2 — the "$=0$" is a statement about the stipulated argument shape, not about the mathematics of R2. Flagged only because §6.2 and Remark 4.3 present "$V_{W_{\mathrm{Forced}}}=0$" as a fact about the route rather than about the model. Covered in substance by [G1]. |
| F13 | Title: "per-coordinate window-payment arguments cannot beat $\mathrm{poly}(d)2^{-d}$ — and the two live plans escape it" | **(C)**, pedantic | The two clauses are consistent only if "per-coordinate" is read as restricting to the two sub-classes (as Corollary 3.2's "in its per-coordinate form" does). The VERDICT block corrects this in its first two sentences and is unambiguous, so this is a titling defect, not statement drift. |
| F14 | §§3, 4, 7 "Independent check. `check_witnesses.py` … exact `Fraction`s"; [G4] "proved in one line in the unit file (`u5`, L11)" | **(E)**, discharged | Code and unit files `u0`–`u5` are not part of the artifact and were not available. Non-blocking: I reproduced every tabulated number by hand in exact arithmetic (§3.3–3.4) and they all agree, and [G4]'s claim is indeed evident from the explicit certificates. |

**Not found (probed and cleared).** Class (A) statement drift on the barrier's
own claims: none beyond F7/F8/F13's summary-line imprecision. Quantifier
inversion in either cap: none — the witness pair is fixed before $W$ in both
T6 and T8, so both are "every functional in the class is capped", not "there is
a pair on which these functionals are capped". Scope inversion: none — 5.2 is
stated and proved in the correct direction (up, never down), which is the
direction the R1 exemption needs. Union bound over an unbounded index,
worst-case/expected conflation (§7.5 handles this explicitly and correctly),
lost hybrid factor, unshown independence (Remark 2.1 correctly isolates the
one place independence is used and correctly excludes pair-dependent windows):
none. Use of §8.3's non-claimed converse: **none** — every downstream use of
$\eta^*$ is the one-directional ceiling, including verdict item 5's
"$p=1$ forces $\eta^*=1$".

---

## 3. STEP-BY-STEP LOG

### 3.0 STEP 0 completeness
`### END OF ARTIFACT 0023-prover-3 ###` present; §§1–8 + GAP REGISTER +
DEPENDENCIES + SOURCE REQUEST all closed; no mid-proof stop. **PASS.**

### 3.1 Class-definition drift (priority 1, done first)
- D4 fixes $\mathcal P_d$ = **all** cross-disjoint pairs of degree-$\le d$ sets
  (§1), and (T2) demands $\pi_W\ge\rho$ **for all** of them. Accepted.
- **R1 (bounded-window cylinder result, $\delta=1/(3d)$ on
  $\mathcal C^{\mathrm{junta}}_d$) is exempt, twice over.** (i) Literally: R1's
  payment inequality holds for cylinder pairs only, so (T2) over $\mathcal P_d$
  fails and R1 $\notin\mathcal W$. (ii) Under §5.1's class-generic reinstantiation
  at $\mathcal C^{\mathrm{junta}}_d$, R1 *is* in $\mathcal W(\mathcal C^{\mathrm{junta}})$,
  but the caps were proved by exhibiting witnesses, and 5.2 is a one-way street:
  $\mathcal C\subseteq\mathcal C'\Rightarrow V^{\mathcal C'}_{W'}\le V^{\mathcal C}_W$
  because $\mathcal P_d(\mathcal C)\subseteq\mathcal P_d(\mathcal C')$ and an
  infimum over a superset is smaller. Verified, and witness (a) is genuinely
  outside $\mathcal C^{\mathrm{junta}}_d$ ($|\mathrm{Rel}(A_k)|=2^{d-1}+d-1>d$).
  Cross-check that no contradiction hides here: witness (b) **is** a $d$-junta,
  and T9 gives ratio $\frac14+\frac1{4(2^d-1)}$ there for $W=\mathrm{Rel}$, while
  the grid pair gives exactly $1/(2d)$ — i.e. $V^{\mathrm{junta}}_{W_{\mathrm{rel}}}\le1/(2d)$,
  above R1's proved $1/(3d)$. Consistent. **Barrier not falsified by R1.**
- **The $1/(8d)$ forcing bound is exempt.** As described (restricted to pairs
  whose forced sets meet) it fails (T2) on $\mathcal P_d$, and under the
  class-generic reading its object class excludes both witnesses
  ($\mathrm{Forced}(D)=\emptyset$, and the address pair forces nothing). Either
  route exempts it. The exemption is *contingent on the artifact's description
  of refuter-3 §5.1* being faithful — see F6. Its numeric consistency checks:
  the sub-class argument yields $\ge1/(2d)\ge1/(8d)$. **Barrier not falsified.**
- Condemned set: $W=W_{\mathrm{rel}}$ (junta substitution), density-$1/\mathrm{poly}$
  windows, windows of size $\ge2^{\varepsilon d}$ on the address family,
  own-influence-thresholded windows at $1/\mathrm{poly}$, $W_{\mathrm{Forced}}$.
  All genuinely satisfy the caps' hypotheses. Accepted. Scope hole at the
  mass-denominated form: **F9**.

### 3.2 Framework (T1–T4)
- **T1** accepted. $\pi_W(f,g)=\sum_i\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)+\sum_i\mathbf 1\{i\in W(f)\}\mathrm{Inf}_i(g)$
  is D3 verbatim; the factorisation needs only $f\perp(g,W(g))$, which
  own-function windows give; $\sum_i\Pr[i\in W(g)]=\mathbb E|W(g)|$ by finiteness.
  Second clause: $\Lambda\,\mathbb E[|W(f)|+|W(g)|]\le\mathbb E[\pi_W]\le\max(\delta_{\mathbf F},\delta_{\mathbf G})\mathbb E[|W(f)|+|W(g)|]$.
  Remark 2.1's exclusion of pair-dependent windows is exactly the step that
  would break, correctly identified. Remark 2.2 (randomised windows) accepted:
  conditioning on the draws preserves both the factorisation and (via T3, which
  is pointwise per realisation) the ceiling.
- **T2** accepted **as a model-relative statement**. The only lower bound the
  stipulated shape has for $\pi_W$ is $\rho(|W|,|W|)$, and the best lower bound
  on $\max(\delta_{\mathbf F},\delta_{\mathbf G})$ extractable from
  $\delta_{\mathbf F}\mathbb E|W(g)|+\delta_{\mathbf G}\mathbb E|W(f)|$ is
  $\mathbb E[\rho]/\mathbb E[|W(f)|+|W(g)|]$ (tight). Point masses at any
  $(A,B)\in\mathcal P_d$ are admissible finitely-supported distributions over
  $\mathcal C^{\mathrm{ind}}_d$ and are incompatible, so $T\le\rho/(w_A+w_B)\le\pi_W/(w_A+w_B)$;
  infimum gives $T\le\Theta_W$. The frozen-rung variant checks: $p\le\pi_W$ and
  $2m\ge w_A+w_B$ give $p/(2m)\le\Theta_W$. Empty-window clause: F12.
- **T3** accepted. $W(B)\cap\mathrm{Rel}(A)\subseteq\mathrm{Rel}(B)\cap\mathrm{Rel}(A)=S$
  and influences are $\ge0$; symmetrise; $V_W\le\eta^*$ including the empty case
  since $\eta^*\ge2^{-d}>0$.
- **T4** accepted. (a) is NS94 Lemma 2.6 reproved correctly (restrict off a
  maximum-degree $T$; the $x_T$-coefficient survives because no $S\supsetneq T$
  exists; $2^{n-m}$ restrictions each contribute a nonzero point). (b) correct
  (combine patterns on disjoint relevant sets). (c) correct:
  $D_i=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)x_{S\setminus i}$ has values in
  $\{0,\pm\frac12\}$, degree $\le d-1$, so
  $\mathrm{Inf}_i(\mathbf 1_A)=\frac14\Pr[D_i\ne0]\ge2^{-d-1}$; dividing by
  $\alpha_A\le1$ is legitimate. Cross-checked against card S6a's influence
  dictionary ("$\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-1-d}$, with equality when $A$
  is a codimension-$d$ subcube") — matches, and matches T7's
  $\mathrm{Inf}_i(\mathbf 1_C)=2^{-d-1}$ exactly. (d) both halves verified; the
  grid pair (row-subcube vs column-subcube) is in $\mathcal P_d$, has
  $S=\{$crossing cell$\}$, both sides force it, $\pi_{\mathrm{Rel}}=1$.
- Remark 4.2(a) accepted: $x_i\mathbf 1_A=s\mathbf 1_A$ gives
  $\widehat{\mathbf 1_A}(S\cup i)=s\widehat{\mathbf 1_A}(S)$, so
  $\mathrm{Inf}_i(\mathbf 1_A)=\frac12\|\mathbf 1_A\|_2^2=\frac{\alpha_A}2$ and
  $\mathrm{Inf}_i(f_A)=\frac12$. 4.2(b) accepted ($2^{-|F|}\ge\alpha_A\ge2^{-d}$).

### 3.3 Witness (a), recomputed in exact arithmetic
$\mathbf 1[b(a)=j]=\prod_t\frac{1+\varepsilon_t(j)a_t}2=2^{-k}\sum_T\varepsilon_T(j)a_T$;
$\mathbf 1_{A_k}=\sum_j\mathbf 1[b(a)=j]\frac{1+y_j}2$; the $y$-free part is
$\frac12$ because $\sum_j\varepsilon_T(j)=0$ for $T\ne\emptyset$. T5(i)–(iii)
confirmed. Influences: $\mathrm{Inf}_{y_j}(\mathbf 1)=2^k\cdot2^{-2k-2}=2^{-k-2}$,
$\mathrm{Inf}_{a_t}(\mathbf 1)=2^{k-1}2^k\cdot2^{-2k-2}=\frac18$; divide by
$\alpha=\frac12$. Independent full expansion at $k=1$:
$\mathbf 1_{A_1}=\frac12+\frac14(y_0+a_1y_0+y_1-a_1y_1)$, verified at four
sample points, Parseval $\frac14+4\cdot\frac1{16}=\frac12=\alpha$. Table:

| $k$ | $d$ | $\lvert\mathrm{Rel}\rvert$ | $\mathrm{Inf}_{a_t}(f)$ | $\mathrm{Inf}_{y_j}(f)$ | $\pi_{\mathrm{Rel}}$ | ratio at $W=\mathrm{Rel}$ | $W_{\mathrm{sh}}$ ratio |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 1/4 | 1/4 | 3/2 | 1/4 | 1/4 |
| 2 | 3 | 6 | 1/4 | 1/8 | 2 | 1/6 | 5/24 |
| 3 | 4 | 11 | 1/4 | 1/16 | 5/2 | 5/44 | 13/64 |

All eight columns agree with T5, the "Independent check" paragraph and §7.1.
General identities re-derived: $\pi_{\mathrm{Rel}}=2(\frac k4+\frac12)=\frac{d+1}2$;
$W_{\mathrm{sh}}$ payment $=2(\frac k4+2^{-k-1})=\frac k2+2^{-k}$, ratio
$\frac{k/2+2^{-k}}{2(k+1)}\ge\frac k{4(k+1)}\ge\frac18$.

### 3.4 Witness (b), recomputed in exact arithmetic
$\mathbf 1_C=2^{-d}\sum_{S\subseteq[d]}x_S$;
$\mathrm{Inf}_i(\mathbf 1_C)=2^{d-1}4^{-d}=2^{-d-1}=\mathrm{Inf}_i(\mathbf 1_D)$;
$\alpha_C=2^{-d}$, $\alpha_D=1-2^{-d}$, so $\mathrm{Inf}_i(f_C)=\frac12$ and
$\mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)}$.

| $d$ | $\mathrm{Inf}_i(f_D)$ | $\pi_{\mathrm{Rel}}(C,D)$ | $W_{\mathrm{sh}}$/$W_{\max}$ ratio | P5 ratio |
|---|---|---|---|---|
| 2 | 1/6 | 4/3 | 1/4+1/12 | 5/18 |
| 3 | 1/14 | 12/7 | 1/4+1/28 | 5/28 |
| 4 | 1/30 | 32/15 | 1/4+1/60 | 19/150 |
| 5 | 1/62 | 80/31 | 1/4+1/124 | — |
| 6 | 1/126 | 64/21 | 1/4+1/252 | — |

All agree with T7's parenthetical check and with §7.1/§7.4's exact values
($5/18,5/28,19/150$ reproduced: $[\frac12+\frac d{2(2^d-1)}]/(d+1)$).

### 3.5 Caps, dichotomy, scope, escapes, frontier
- **T6 (CAP I)** accepted, incl. (a) $(d+1)/(4(2^{d-1}+d-1))\le(d+1)2^{-d-1}$
  (needs $2^{d+1}+4d-4\ge2^{d+1}$), (b) $w\ge2c(2^{d-1}+d-1)\ge c2^d$, (c). Only
  localisation is used; witness fixed independently of $W$. $d\ge2$ correctly
  required ($k\ge1$). $N=k+2^k$ grows with $d$, which is legitimate precisely
  because R2's $\delta$ must be $N$-free.
- **T8 (CAP II)** accepted; strict $\theta>\frac1{2(2^d-1)}$ forces
  $W(D)=\emptyset$, then ratio $=\frac{|W(C)|/(2(2^d-1))}{|W(C)|}$.
- **T9** accepted: $\pi_W(C,D)=\frac12 w_D+\frac{w_C}{2(2^d-1)}$; $w_D=0<w_C$
  gives exactly $\frac1{2(2^d-1)}$; $w_D\ge1$ gives $\ge\frac1{2(w_C+w_D)}\ge\frac1{4d}$
  since $w_C,w_D\le|{\rm Rel}|=d$. The "iff" is witness-local and correctly so.
- **Remark 4.4** — the *insufficiency* of min→sum is genuinely proved (T8
  exhibits sum-form functionals still capped at $2^{-\Theta(d)}$); the
  *necessity* half is imported, not proved (F6).
- **§5.1/5.2** accepted; direction correct and non-invertible (F5 for the rung
  identifications).
- **§5.4 groups** accepted, recomputed: for $C_{\mathcal Y}$ the $|\mathcal Y|^d$
  characters supported in $[d]$ carry modulus $|\mathcal Y|^{-d}$;
  $\mathrm{Inf}_i(\mathbf 1_C)=|\mathcal Y|^{d-1}(|\mathcal Y|-1)|\mathcal Y|^{-2d}=(1-|\mathcal Y|^{-1})|\mathcal Y|^{-d}$;
  dividing by $\alpha_C=|\mathcal Y|^{-d}$ and $\alpha_D=1-|\mathcal Y|^{-d}$
  gives $1-|\mathcal Y|^{-1}$ and $\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^d-1}$,
  which specialise at $|\mathcal Y|=2$ to $\frac12$ and $\frac1{2(2^d-1)}$.
  Even-order pullback along $\varphi:\mathcal Y\twoheadrightarrow\mathbb Z_2$
  accepted (a surjective homomorphism exists exactly for even order; it
  preserves coefficients, degree, influences, $\alpha$ — uniform pushforward —
  and disjointness). [GAP-2] honestly scoped.
- **§7.1 (P1 escapes)** accepted; both hypothesis failures checked
  quantitatively (density $d/(2^{d-1}+d-1)$ degrades T6(b) to $\approx(d+1)/(4d)$;
  $W_{\mathrm{sh}}(D)=[d]$ is own-cheap).
- **§7.2 (non-canonicity)** accepted: $b(a')=b(a)\oplus c$ so
  $y'_{b(a')}=y_{b(a)}$ and $\sigma_c$ fixes $A_k,B_k$; the targets form one
  orbit; hence a canonical localised $W$ takes $\emptyset$ or all $2^{k}$
  targets, so it is never a shattering selection, and in the "all" case
  $|W(A_k)|\ge2^{d-1}$ gives $V_W\le(d+1)2^{-d}$.
- **§7.3 ($W_{\max}$)** accepted, including the $k\ge2$ restriction (at $k=1$,
  $\mathrm{Inf}_{y_j}=\mathrm{Inf}_{a_1}=\frac14$ and $W_{\max}$ is all of $[N]$),
  canonicity, localisation via T4(b), and $|W_{\max}|\le d/\max_i\mathrm{Inf}_i$.
  The [MEMORY] caveat is correctly flagged and used in no claim.
- **§7.4 (P5)** witness (b) accepted ($T_C=[d]$ is the unique minimum
  certificate; $T_D(y)=\{i\}$ minimum of size 1; $\pi=\frac12+\frac d{2(2^d-1)}$
  over $d+1$). Witness (a): **F1**.
- **§7.5** worst-case/average separation accepted modulo **F2**; the
  worst-case-vs-average distinction is handled explicitly and correctly, and the
  conclusion "any per-point variant is capped" is the right direction.
- **§8** accepted: (1) ceiling from T3 (+ Remark 2.2, sound because T3 is
  pointwise per realisation); (2) bracket from T4(d); (3) one-directional and
  labelled so, with $|S|\le2^{\Theta(d)}$ following from T4(c); (4) both
  witnesses $\Theta(d)$; (5) $\pi_{W_{\mathrm{sh}}}\le\pi_{\mathrm{Rel}}$ needs
  $W_{\mathrm{sh}}$ localised (true: monomial coordinates are relevant), so
  $p=1\Rightarrow\eta^*\ge1$, and $\eta^*\le1$ from the grid pair, giving
  $\eta^*=1$; the milestone's logic ("a hit refutes $p=1$, not R2") is correct.

### 3.6 Negation check and per-lemma adjudication
Tags: **MECH** = re-derived/negation attempted symbolically by hand here;
**CARD** = cross-checked against a source card; **NONE** = not adjudicable from
permitted inputs. (No **CODE** tag is available: no execution tool in this
session.)

| load-bearing lemma | negation attempt | tag |
|---|---|---|
| T1 master count | would need failure of the independence factorisation; blocked by own-function windows | MECH |
| T2 value theorem | would need an argument of shape D4 with $T>V_W$; blocked by admissibility of point masses | MECH (model-relative) |
| T3 localisation ceiling | would need $\pi_W>\pi_{\mathrm{Rel}}$; blocked by $W(B)\cap\mathrm{Rel}(A)\subseteq S$ | MECH |
| T4(a)(b)(c)(d) | searched for a degree-$\le d$ counterexample at each; none; (c) equality case matches card | MECH + CARD (S6a) |
| T5 address table | recomputed $k=1,2,3$ exactly, plus full $k=1$ expansion | MECH |
| T6 CAP I | tried to evade by shrinking $w$; blocked for $W\supseteq\mathrm{Rel}$/density $c$/size $2^{\varepsilon d}$ | MECH |
| T7 subcube table | recomputed $d=2..6$ exactly; equality case matches card S6a | MECH + CARD |
| T8 CAP II, T9 dichotomy | tried $w_D\ge1$ (escapes, as the artifact says); strictness of $\theta$ needed and present | MECH |
| §5.2 monotonicity | tried the reverse direction; correctly unavailable (this is what exempts R1) | MECH |
| §5.4 group CAP II / even-order CAP I | recomputed characters and pullback | MECH |
| §7.2 automorphism theorem | verified $\sigma_c$ fixes $A_k$ and acts transitively on targets | MECH |
| §7.4 witness (a) certificate | **negation succeeded — counterexample found** (F1) | MECH |
| §6.4 grid-ceiling comparison | **negation succeeded at $d=2,3,4$** (F3) | MECH |
| §5.3 rung inclusions R3–R6′ | not adjudicable (PROGRESS.md not permitted) | NONE |
| §6.1/§6.2/Rmk 4.4 descriptions of I01, refuter-3 | partially corroborated via I02 frozen inputs; core scope claims not adjudicable | NONE |
| S7b size-bound citation | checked against card S7/S7b; not in the cited theorem | CARD (fails) |
| S1/K1 comparison | checked against card S1 (Thm 4.4, strict $\delta<|\mathcal Y|^{-d}/d$) | CARD |

### 3.7 Honesty audit
Declared limits ([G1] stipulated class model, [G2] odd-order groups, [G3]
non-claimed converse, [G4] routine, [MEMORY] flagged-unused) are all real and
correctly located; the converse is used nowhere; the [MEMORY] items are indeed
confined to §7.3's caveat. Undeclared limits: **F5** (scope chain), **F9**
(the mass-denominated form of the rung's own flagged route), **F7**(iii) (the
object-class relativisation on which the R1 exemption depends is absent from
the verdict), **F12** (the $V_W=0$ convention is model-relative), and the
incomplete dependency register noted in **F6**. Verdict item 5's "sharp,
cheap, falsifiable milestone" and item 6's "no plan proposes" are
non-mathematical and unadjudicated.

---

## 4. SOURCE REQUEST

All (D)/(E) items are **internal** to the campaign; no external upload is
needed. Ranked restatement requests, each replaceable by an in-artifact
restatement:

**Rank 1.** The rung statements for R3, R4, R5, R6′, R6($\mathbb Z_2$) with
their object classes and targets (`PROGRESS.md`, or restated self-containedly in
the artifact). Needed for: verdict item 3 / §5.3 ("SCOPE (proved)"), which
cannot be certified blind. Rungs tried: the artifact, I02, CONTRACT.md, all
cards — none defines R3–R6′. Fallback: demote verdict item 3 to "caps hold in
every class containing the two witnesses" (which §5.2 does establish) and drop
the named rungs.

**Rank 2.** The exact statement and declared scope of `0023-refuter-3` §5.1
(the $1/(8d)$ forcing bound) and §5.3 / the $\min$-form refutation
$\theta^*(d)\le\frac1{2(2^d-1)}$. Needed for: the §6.2 calibration (the
highest-stakes exemption in the artifact) and Remark 4.4's "necessary" half.
Fallback: mark §6.2 conditional on refuter-3 and weaken Remark 4.4 to the
insufficiency direction only, which is proved here.

**Rank 3.** A one-paragraph statement of I01's engine (window, payment,
assembly) as used in §6.1. Needed for: the R1 diagnosis sentence, not for any
cap. Fallback: state §6.1 as a conditional reading of I01.
### END OF ARTIFACT 0023-prover-3-verify-D ###
