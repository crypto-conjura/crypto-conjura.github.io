id: 0023-prover-3-r2-verify-F
agent: verifier-b
model: claude-opus-5[1m]
cycle: 3

# Blind referee pass F on `0023-prover-3-r2` (targeted re-verification of the repairs)

**STEP 0 COMPLETENESS.** The artifact ends with `### END OF ARTIFACT 0023-prover-3-r2 ###`
(line 1054) and no unit stops mid-proof. Not truncated; verification proceeds.

Inputs read: the artifact in full; `intermediates/I02-degree-d-sets.md`; `CONTRACT.md`;
`sources/S1-acc22-card.md`, `S6-junta-degree-card.md`, `S7-changfang26-card.md`
(S2, S3, S5 not cited by the artifact and not consulted). No predecessor artifact, ledger,
PROGRESS.md or prior verdict was read. **No shell was available in this thread**: every
numeric re-check below was done symbolically/by hand in exact arithmetic, not by running
the cited scripts.

---

## 1. FINAL VERDICT

**DEFECTS.** The repairs are arithmetically sound — T5, T7, the new $k-u+2^u$
minimality-of-size proof and the min-over-selections bound (least value $5/32$ at $k=3$
against $1/8$) all recompute exactly — but the newly inserted Remark 1.1 states an
"out-of-scope family refutes nothing" principle that **T2's own proof violates**: both caps
are obtained by evaluating the count at point-mass families whose $\max(\delta_{\mathbf F},
\delta_{\mathbf G})$ is $1/4$ resp. $1/2$, i.e. above every threshold at issue, so the
barrier *reading* of CAP I and CAP II (Corollary 3.2, VERDICT 2, §5.3's displayed sentence,
VERDICT 3, §6.2) is unproved under the artifact's own class model (class B); and the one
sentence the artifact instructs the ladder record to carry verbatim silently drops CAP II's
nonemptiness hypothesis (class A).

---

## 2. FINDINGS TABLE

| # | Quoted location | Class | Explanation |
|---|---|---|---|
| **F1** | T2 proof: *"for each $(A,B)\in\mathcal P_d$ with $|W(A)|+|W(B)|\ge1$ the point masses at $f_A,f_B$ form an incompatible family with positive denominator, giving $\Lambda=\dots$; take the infimum over those pairs"* — against Remark 1.1: *"A degenerate pair defeats an argument only if it is in scope … a family whose own $\max\delta$ exceeds the claimed threshold refutes nothing. (At the point masses $(A_k,B_k)$ of §3, $\max\delta=1/4$; at $(C,D)$ of §4, $\max\delta=1/2$; every threshold at issue here is $<1/(2d)\le1/4$ for $d\ge2$, so both are out of scope.)"* | **(B) CRITICAL, load-bearing** | The two sentences are mutually exclusive. Remark 1.1 (the U2 repair) asserts the general principle that a family whose own $\max\delta$ exceeds the claimed threshold imposes no obligation on a $\mathcal W$-argument, and computes that **both certified witnesses are exactly such families** ($1/4$ and $1/2$, versus thresholds $<1/(2d)$). T2's proof nevertheless derives the cap by evaluating $\Lambda$ at the point masses of those same two witness pairs. Under Remark 1.1's principle the weak value of $\Lambda$ there refutes nothing, so $T\le\Theta_W(d)$ does not follow and neither does any of: Corollary 3.2 ("any argument in $\mathcal W$ with a relevance-denominated window … establishes at most $\mathrm{poly}(d)2^{-d}$"), VERDICT 2's clauses (i) and (ii), §5.3's displayed conditional, VERDICT 3, §6.2's "$\Theta_{W_{\mathrm{Forced}}}(d)\le\frac1{2(2^d-1)}$" *read as a barrier*. Under the opposite (unrestricted) convention T2 stands but Remark 1.1's deletion of the empty-window inference is wrong — under that convention a pair with both windows empty makes the count silent for its own point-mass family and the unrestricted infimum is $0$, which is the very inference just deleted. The artifact offers no third class model, and [ESCALATED E1]'s claim that the convention is "used by **no cap** in this artifact" is false: it is used by the step that converts $\Theta_W$ into a barrier. What survives untouched: the purely arithmetic statements $\Theta_W(d)\le(d+1)2^{-d-1}$ (T6) and $\Theta_W(d)\le\frac1{2(2^d-1)}$ (T8) as bounds on the D5 infimum, and every §7 escape claim (those are negative and only get stronger under restriction). What does not survive is the identification of $\Theta_W$ with "what the technique can prove". I do not supply the missing ingredient. |
| **F2** | §5.3 display, repeated verbatim in VERDICT 3: *"no relevance-denominated window-payment argument, and no own-heavy-at-$\theta>\frac1{2(2^d-1)}$ window-payment argument, can establish R4's target …"*, with *"The ladder record must carry the displayed conditional sentence, not a summary of it."* | **(A) STATEMENT DRIFT** | T8 has **two** hypotheses: own-heaviness at $\theta>\frac1{2(2^d-1)}$ **and** $W(C)\ne\emptyset$. VERDICT 2(ii) keeps both ("own-heavy at a level $\theta>\frac1{2(2^d-1)}$ (strictly) **and nonempty at the subcube $C$**"); Remark 4.2′ keeps both and explicitly concedes "If a hypothetical own-heavy $W$ had $W(C)=\emptyset$ as well, witness (b) would contribute no bound, and this artifact would claim no cap for it." The designated record sentence drops the second hypothesis and therefore quantifies over own-heavy functionals the artifact itself declines to cap. The omission is not vacuous: an own-heavy rule can be empty at $C$ while nonempty and address-hub-sized on witness (a) (so T6 gives only $\approx\frac{d+1}{4d}$), i.e. the dropped hypothesis is load-bearing for the sentence as written. This is the sentence the artifact asks the campaign to record, so the drift is in its primary deliverable. |
| **F3** | VERDICT 1: *"P1 and P5 ESCAPE both caps — YES, both, by exact computation"*; §7.4: *"P5's plan uses **minimal** certificates …; §7.4 evaluates **minimum**-size certificates"*; [G5]. | **(C) JUSTIFICATION GAP (scope)** | §7.4's own conclusion is scoped ("— for minimum-size selections; see [G5]") and [G5] states that an unrestricted *minimal* selection admits a window of size $2^{d-1}$ at witness (a). Under Remark 2.2 that puts $\mathbb E|W(A_k)|\ge2^{d-1}$ into T6, i.e. an **exponential** cap $(d+1)2^{-d}$ — so for P5's *declared* certificate notion the CAP I escape is not merely unsettled, the cap can bite. The headline clause (iv) asserts the escape for "P5" unscoped, and calls the strategist's ruling "**confirmed**" on that basis. Partially mitigated inside the same item ("for the minimum-certificate window (P5)") and by VERDICT 6's drafting warning, but the headline as written overstates §7.4 and [G5]. Answering the audit question directly: **[G5] does damage the escape claim it sits next to, for the plan's declared notion**; it is correctly scoped in §7.4/[G5] and incorrectly scoped in VERDICT 1. |
| **F4** | VERDICT 5: *"Every localised window functional that is nonempty on the pairs approaching $\eta^*(d)$ — **which includes every functional named in this artifact** and both live plans' — is capped by the single number $\eta^*(d)$"* | **(C)** | Unproved for two functionals the artifact names: $W_{\mathrm{Forced}}$ (empty on **both** sides at the address pair, Remark 4.3; and $\mathrm{Forced}(D)=\emptyset$, Remark 4.2(b)) and $W^\theta_{\mathrm{hvy}}$ (empty at $D$, T8's proof). Whether either is nonempty at the pairs approaching $\inf\pi_{\mathrm{Rel}}$ is unknown, since those pairs are not identified anywhere. §8.1 states the correct restricted list ("$W_{\mathrm{rel}}$, $W_{\mathrm{sh}}$, $W_{\max}$ and the certificate windows, all nonempty on all of $\mathcal P_d$"). Verdict-vs-body overclaim. |
| **F5** | VERDICT: *"no cap proved here applies to $\mathcal W$ as a whole: §7 exhibits three localised members that neither cap touches"*; §7.1/§7.3/§7.4: *"Both caps' hypotheses fail quantitatively"* | **(C) / presentational** | T6 as stated is a theorem about **every** localised $W$ with $|W(A_k)|+|W(B_k)|\ge1$; its hypothesis therefore *holds* for $W_{\mathrm{sh}}$, $W_{\max}$ and both certificate windows (each is nonempty on all of $\mathcal P_d$, as §7.1/§7.3/§8.1 themselves prove). What fails is the *inverse-polynomial-density* instance T6(b), and T6's general conclusion degrades to $\approx\frac{d+1}{4d}$. So "the hypotheses of CAP I fail" and "neither cap touches them" are literally false; the intended and defensible claim is "no cap **below $1/\mathrm{poly}(d)$**". The body supplies the correct numbers immediately, so this is drafting, but it sits in the VERDICT's self-described "exact sense". |
| **F6** | Remark 4.3: *"Any window selected by an own-influence threshold $\theta\ge1/\mathrm{poly}(d)$ … is capped at $\frac1{2(2^d-1)}$ for all $d\ge d_0(\theta)$ … the nonemptiness hypothesis being discharged by Remark 4.2′"* | **(C) minor** | Remark 4.2′ discharges $W(C)\ne\emptyset$ only for $\frac1{2(2^d-1)}<\theta\le\frac12$. The quantified family "$\theta\ge1/\mathrm{poly}(d)$" includes constants $\theta>\frac12$, for which $W^\theta_{\mathrm{hvy}}\equiv\emptyset$ (no normalised indicator has $\mathrm{Inf}_i(f_A)>\frac12$) and no $d_0$ repairs the discharge. The conclusion still holds, but only through D5's degenerate zero convention, which Remark 4.3 does not invoke. So the "discharged for every rule named" claim is complete for the *named* rules ($W^\theta_{\mathrm{hvy}}$ at $\theta\le\frac12$, $W_{\mathrm{Forced}}$ at $\theta=\frac12$: both give $W(C)=[d]$ by T7) but not for the *quantified family* Remark 4.3 applies the cap to. |
| **F7** | Corollary 3.2: *"refuter-2's inequality (M) transplanted to $\mathcal C^{\mathrm{ind}}_d$"*; DEPENDENCIES table; changelog U6 *"Every row now carries the file path and the internal block id; added rows for …"* | **(D) CITATION / register** | `0023-refuter-2` and its "inequality (M)" appear in the body with **no dependency row and no restatement**; I cannot check what (M) says, and U6 declares the register complete. Same for `0023-prover-3-u5` L11, which carries [G4]'s one-line proof. Both are non-load-bearing on their face ([G4] is also "evident from the explicit certificates"), so severity is low, but the register is still incomplete after the U6 repair. |
| **F8** | DEPENDENCIES row **S7 (obstacle (ii))**: *"that a pair-dependent window is the obstacle to per-function factorisation"*; Remark 2.1: *"This is the only load-bearing form of obstacle (ii) recorded in card S7"* | **(D) minor, non-load-bearing** | Card S7 records obstacle (ii) as *non-canonicity of $T(A)$ across a distribution's support, so the union $T$ over a whole family is not bounded and the argument must be run pairwise or with a covering step*; S7 and S7b both state that the paper contains **nothing** about influences, families, pairs or factorisation (the word "influence" occurs once, in a motivating clause). The card therefore does not establish what the row says it establishes. §7.2's *Reading* uses obstacle (ii) in the card's own sense (non-canonicity) and is fine; Remark 2.1's gloss is the prover's own observation and should be labelled as such. Row is already marked "no (framing)", so nothing downstream fails. |
| **F9** | DEPENDENCIES row for `PROGRESS.md`: *"the rung classes R2, R3, R4, R5, R6′, R6($\mathbb Z_2$) and R4's target $c\,e^{-d^\alpha}$ … load-bearing? yes, for the scope clause only"* | **(E) UNVERIFIABLE, non-blocking** | `PROGRESS.md` is outside my permitted inputs, so I cannot check the fidelity of §5.3's restatement of R3–R6. Only R2 is checkable against `I02-degree-d-sets.md`, and it matches ("normalised indicators of degree-$\le d$ sets over $\mathbb Z_2$"). The artifact declares the dependency and restates the classes inline, which is the right handling; recorded so the tally shows this clause rests on an input this pass did not see. |

**No residual "value $\ge X$" claim found.** Checked every inequality in §§6–8: every lower
bound in the artifact is either a ratio **at a named pair** (§7.1, §7.4, §7.5, T9, §6.1 —
legitimate, and each is correctly labelled an upper bound on $\Theta_W$ by §7's standing
reading), or a bound on $\eta^*$ ($2^{-d}\le\eta^*\le1$, T4(d) — a lower bound on the
*ceiling*, which is consistent with "no lower bound on any $\Theta_W$"), or the conditional
$\text{(PAY}\star)\Rightarrow\eta^*\ge p$ (§8.5, hypothesis explicitly carried). The
predecessor's contradiction with the open bracket is gone; the remaining verdict-level
overclaims are F3–F5, none of which is a lower bound.

---

## 3. STEP-BY-STEP LOG

**Class (A) first — what the artifact actually proves, diffed against I02/CONTRACT.**
It proves nothing about R2's truth (correctly declared) and does not touch the Contract's
statement. Its deliverables are (i) exact influence tables for two pairs in $\mathcal P_d$;
(ii) two arithmetic ceilings on the D5 infimum $\Theta_W$ for two delimited sub-classes of a
stipulated class $\mathcal W$; (iii) the transfer of (ii) up the class chain; (iv) negative
"the hypotheses fail here" claims for three named functionals; (v) an open ceiling $\eta^*$
and a falsifiable milestone. Against I02: the artifact correctly declares that I02's central
mass-denominated question is closed in **neither** direction ([G1], VERDICT 2, Remark 4.3),
correctly declares PARTIAL, and correctly refuses to record any rung as condemned. Scope as
titled ("**two** window-payment sub-classes … the class as a whole is **not** capped") matches
what §§3–4 prove and what §7 exhibits — with the two exceptions F2 (the recorded sentence is
broader than T8) and F5 (the word "touches"). The barrier→technique-class inference itself is
F1.

**Definitions (repairs 1).** D5 now defines only $\Theta_W$. The single retained zero clause
($W\equiv\emptyset$ on *all* of $\mathcal P_d$) is sound as claimed: the count's denominator
then vanishes for every incompatible family, so no positive threshold is established. ✔
Remark 1.1 states and deletes the invalid "some pair with both windows empty $\Rightarrow$
establishes nothing" inference and gives the correct reason. ✔ as a repair — but the reason it
gives is what breaks T2 (F1). The two witness $\max\delta$ values quoted in Remark 1.1 are
right: point mass at $f_{A_k}$ has $\max_i\mathrm{Inf}_i=\max(\frac14,2^{-k-1})=\frac14$
($k\ge1$); at $(C,D)$, $\max(\frac12,\frac1{2(2^d-1)})=\frac12$. ✔

**T1.** Accepted. Factorisation uses only per-function windows and independence; finite sums;
$\sum_i\Pr[i\in W(g)]=\mathbb E|W(g)|$; symmetrisation. The second clause needs
$\mathbb E[|W(f)|+|W(g)|]>0$, which is carried. Remark 2.1's exclusion of pair-dependent
windows is the substantive one. Remark 2.2 (randomised windows) is routine by conditioning. ✔

**T2.** Statement and proof accepted *as arithmetic*; **rejected as a model of "what the class
establishes"** — F1. The internal variant "$\pi_W\ge p,|W|\le m\Rightarrow p/(2m)\le\Theta_W$"
checks out ($\frac p{2m}\le\frac{\pi_W}{2m}\le\frac{\pi_W}{|W(A)|+|W(B)|}$). ✔

**T3.** Accepted. $\mathrm{Inf}_i(f_A)=0$ off $\mathrm{Rel}(A)$, localisation on both sides,
$\mathrm{Inf}\ge0$; the restricted-versus-full infimum distinction ($\eta^*_W$ vs $\eta^*$) is
now correctly drawn, and the list of everywhere-nonempty windows is correct. ✔

**T4.** (a) restriction argument, degree exactly $m$, $2^{n-m}$ restrictions ⟹ $\Pr\ge2^{-m}$ ✔.
(b) disjoint relevant sets ⟹ combine patterns ⟹ common point ✔. (c) $D_i$ has degree $\le d-1$,
values in $\{0,\pm\frac12\}$, Parseval + (a) ⟹ $\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-d-1}$, then
$/\alpha_A\le1$ ✔ (independent of card S6a, as claimed). (d) lower $2^{-d}$ from (b)+(c) ✔;
upper $1$ from the row-subcube/column-subcube pair — both codimension-$d$ subcubes, disjoint,
$S=\{$crossing cell$\}$, each forces it, so $\frac12+\frac12=1$ ✔.

**T5 (recomputed by hand, exact).** (i) $\mathbf 1[b(a)=j]=\prod_t\frac{1+\varepsilon_t(j)a_t}2$
since $b_t(a)=j_t\iff a_t=1-2j_t$; the $y$-free part collapses to $\frac12$ because
$\sum_j\varepsilon_T(j)=0$ for $T\ne\emptyset$ ✔. (ii) distinct supports, coefficients
$\pm2^{-k-1}$, $\deg=k+1$, top supports $\{a_1..a_k,y_j\}$, $2^k$ of them ✔. (iv)
$\mathrm{Inf}_{y_j}(\mathbf 1)=2^k2^{-2k-2}=2^{-k-2}$, $\mathrm{Inf}_{a_t}(\mathbf 1)=
2^{2k-1}2^{-2k-2}=\frac18$; $/\alpha=\frac12$ gives $2^{-k-1}$ and $\frac14$ ✔. (v)
$\pi_{\mathrm{Rel}}=2(\frac k4+\frac12)=\frac{d+1}2$ ✔. Cross-check of the "independent check"
line: $|\mathrm{Rel}|=3,6,11$; $\pi_{\mathrm{Rel}}=\frac32,2,\frac52$; relevance ratios
$\frac14,\frac16,\frac5{44}$ — all reproduced ✔.

**T6 (CAP I).** Inequality and all three instances verified: (a) $W\supseteq\mathrm{Rel}$ with
localisation forces $W=W_{\mathrm{rel}}$, sum $=2(2^{d-1}+d-1)$, and
$\frac{d+1}{4(2^{d-1}+d-1)}\le(d+1)2^{-d-1}$ ⟺ $d\ge1$ ✔; (b) sum $\ge2c(2^{d-1}+d-1)\ge c2^d$
⟹ $\frac{d+1}{c2^{d+1}}$ ✔; (c) $\frac{d+1}{2}2^{-\varepsilon d}$ ✔. **Nonemptiness genuinely
discharged** in (a) ($\mathrm{Rel}(A_k)=[N]\ne\emptyset$), (b) ($c>0$ and $|\mathrm{Rel}|\ge1$,
window sizes integral), (c) (hypothesis is itself $\ge2^{\varepsilon d}\ge1$) ✔. Completeness of
the discharge list *relative to CAP I's uses*: Corollary 3.2 (density $\ge1/\mathrm{poly}$) ✔;
§7.2(iv) (explicitly notes $|W(A_k)|+|W(B_k)|\ge2^k\ge1$, and $\frac{d+1}{2\cdot2^{d-1}}=(d+1)2^{-d}$
is right) ✔; §7.1/§7.3/§7.4's degradation computations ✔. No use of CAP I lacks its hypothesis.

**T7 (recomputed).** $\mathbf 1_C=2^{-d}\sum_{S\subseteq[d]}x_S$; $\mathrm{Inf}_i(\mathbf 1_C)=
2^{d-1}4^{-d}=2^{-d-1}=\mathrm{Inf}_i(\mathbf 1_D)$; $\alpha_C=2^{-d}$,
$\alpha_D=\frac{2^d-1}{2^d}$ ⟹ $\frac12$ and $\frac1{2(2^d-1)}$ ✔;
$\pi_{\mathrm{Rel}}=\frac d2+\frac d{2(2^d-1)}$, giving $\frac43,\frac{12}7,\frac{32}{15},
\frac{80}{31},\frac{64}{21}$ at $d=2..6$ ✔. Remark 4.2: forcing ⟹ $\mathrm{Inf}_i(f_A)=\frac12$
exactly ✔; $|\mathrm{Forced}|\le d$ from $\alpha\le2^{-|F|}$ and $\alpha\ge2^{-d}$ ✔;
$\mathrm{Forced}(D)=\emptyset$ for $d\ge2$ with the $d=1$ exception named ✔ (P1 repair).

**T8 (CAP II) and Remark 4.2′.** Own-heaviness at $\theta>\frac1{2(2^d-1)}$ forces
$W(D)=\emptyset$ (every coordinate of $D$ is at or below the level, and $0$ off $[d]$) ✔;
localisation gives $W(C)\subseteq[d]$ so each of its coordinates costs exactly
$\frac1{2(2^d-1)}$ for the partner ✔; ratio $=\frac1{2(2^d-1)}$ ✔. The hypothesis
$W(C)\ne\emptyset$ is genuinely discharged for the two *named* own-heavy rules
($W^\theta_{\mathrm{hvy}}(C)=W_{\mathrm{Forced}}(C)=[d]$ by T7, provided $\theta\le\frac12$) ✔ —
but see F6 for the quantified family in Remark 4.3, and F2 for the record sentence that drops
the hypothesis altogether. T9's dichotomy arithmetic ✔ ($w_D\ge1\Rightarrow\ge\frac1{2(w_C+w_D)}
\ge\frac1{4d}$).

**§5 scope.** 5.1's class-genericity list of used ingredients is accurate (T1–T3 use only
incompatibility, independence, $\mathrm{Inf}\ge0$, point-mass admissibility, vanishing off
$\mathrm{Rel}$) ✔. 5.2's monotonicity direction is right and the "provably never transfer
downward" is the correct caveat, and §6.1 uses it correctly to spare frozen R1 ✔.
5.3's chain and the $d_0(c,\alpha)$ criterion check out ($(d+1)\ln2-\ln(d+1)-d^\alpha\to+\infty$
for $\alpha<1$) ✔; R5's "no distributional part" is right since T2 evaluates at point masses ✔
(that step is itself F1's). 5.4: the group Fourier computation is correct
($|\mathcal Y|^d$ characters of modulus $|\mathcal Y|^{-d}$; $\mathrm{Inf}_i(f_{C_{\mathcal Y}})
=1-|\mathcal Y|^{-1}$; $\mathrm{Inf}_i(f_{D_{\mathcal Y}})=\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^d-1}$),
and the even-order pullback is correct as argued (injective dual map, measure-preserving
$\varphi^N$, degree/influence/$\alpha$/disjointness preserved, $\mathbb Z_2$ quotient iff even
order) ✔. [G2] honestly scopes the odd-order hole ✔.

**§6 calibration.** 6.1 correct and materially important (witness (a) is outside
$\mathcal C^{\mathrm{junta}}_d$ because $2^{d-1}+d-1>d$ for $d\ge2$; witness (b) is inside but
R1's window is not own-heavy, T9 gives $\ge\frac14$, consistent with $\frac1{2d}$) ✔.
6.3's description of K1's proof ("Cauchy–Schwarz over the $|\mathcal Y|^d-1$ non-constant
blocks") **matches card S1** item S1.b verbatim in substance ✔ — no citation defect there.
6.4's exact comparison recomputed: $(d+1)2^{-d-1}=\frac12,\frac38,\frac14,\frac5{32}$ vs
$\frac1{2d}=\frac12,\frac14,\frac16,\frac18$, first strict inequality at $d=5$
($\frac3{32}<\frac1{10}$) ✔; $\frac{2^{-d}}d\le(d+1)2^{-d-1}$ ⟺ $d(d+1)\ge2$ ✔;
$\frac{2^{-d}}d\le\frac1{2(2^d-1)}$ ⟺ $d2^d\ge2^{d+1}-2$, true for $d\ge2$ ✔ (the U5 repair is
correct and the comparison is correctly declared unused).

**§7 escapes.** Standing reading paragraph correctly fixes the upper-bound direction ✔.
7.1: the $\le d$ size bound is now definitional, not a citation — and card S7b's shattering
theorem is correctly marked *not used* (F8 aside) ✔; nonemptiness on $\mathcal P_d$ argued
correctly ($\deg\mathbf 1_A=0\Rightarrow A$ = full cube $\Rightarrow B=\emptyset$) ✔;
$\pi=\frac k2+2^{-k}$, ratio $\ge\frac k{4(k+1)}\ge\frac18$, exact $\frac14,\frac5{24},
\frac{13}{64}$ ✔; witness (b) ratio $\frac14+\frac1{4(2^d-1)}$ ✔.
7.2: $\sigma_c$ is a signed permutation, $\sigma_c(A_k)=A_k$ (verified via
$b(a')=b(a)\oplus c$ and $y'_{b(a')}=y_{b(a)}$), transitive on targets, hence all-or-nothing
target part, hence (iii) and (iv) with T6's hypothesis explicitly checked ✔.
7.3: $W_{\max}$ with the $\mathrm{Rel}=\emptyset$ convention (P4 repair) ✔; the $k\ge2$
restriction is necessary and is stated (at $k=1$, $\mathrm{Inf}_{a_1}=\mathrm{Inf}_{y_j}=\frac14$)
✔; ratios $\frac14$ and $\frac14+\frac1{4(2^d-1)}$ ✔; the U10 repair (not own-heavy at any level
**strictly** above $\frac1{2(2^d-1)}$, because $D$ attains the level exactly) is exactly right ✔;
$|W_{\max}|\le d/\max_i\mathrm{Inf}_i$ ✔; the [MEMORY] gate is flagged and used in no claim ✔.
7.5: $\Sigma$-characterisation for the $u=0$ selection verified; worst case $2^{-k}$ (at $a=a'$),
average $\frac k4+4^{-k}$ (addresses are uniform and independent under
$x\sim\mathrm{Unif}(A_k),y\sim\mathrm{Unif}(B_k)$ because each address has the same number of
completions) ✔; $\Sigma\subseteq T_A\cap T_B\subseteq W(A)\cap W(B)\Rightarrow\pi_\Sigma\le\pi_W$
(P2 repair) ✔.

**§7.4 — the minimality/certificate repair, recomputed in exact arithmetic by hand.**
(i) Certificate lower bound: if $U$ is the set of free address bits, $|U|=u$, then $S$ must
contain the other $k-u$ address bits and **all** $2^u$ targets $y_{b(a)\oplus v}$, $v\subseteq U$,
each $+1$ at $x$; so $|S|\ge k-u+2^u$, and this is achieved with no slack. ✔
(ii) $\min_{0\le u\le k}(k-u+2^u)=k+1=d$, attained **exactly** at $u\in\{0,1\}$ ($u=2$ gives
$k+2$, and the expression is increasing thereafter). ✔ So minimality *of size* is proved, not
assumed.
(iii) Multiplicity $=1+\#\{t\in[k]:y_{b(a)\oplus e_t}(x)=+1\}\in[1,k+1]$, $x$-dependent — the
"unique" claim is correctly replaced, and the reported enumeration ranges $1$–$2$, $1$–$3$,
$1$–$4$ for $k=1,2,3$ are consistent with the bound $k+1$. ✔
(iv) Payment depends only on $(u_A,u_B)$ because all address bits share $\mathrm{Inf}=\frac14$
and all targets share $2^{-k-1}$; per side $\phi(u)=\frac{k-u}4+2^u2^{-k-1}$ with
$\phi(0)-\phi(1)=\frac14-2^{-k-1}\ge0$ for $k\ge1$, so the total gap is $\frac12-2^{-k}$ exactly
as printed, and the worst selection is $u_A=u_B=1$. ✔
(v) Worst-selection ratio $=\frac{\frac{k-1}2+2^{1-k}}{2(k+1)}$: I get $\frac14,\frac16,
\frac5{32},\frac{13}{80},\frac{11}{64},\dots$ for $k=1,2,3,4,5$ — matching the printed values,
with the **least value $\frac5{32}$ at $k=3$** and the sequence increasing to $\frac14$
thereafter. ✔ The equivalence "$\ge\frac18\iff k\ge3-2^{3-k}$" is algebraically exact and true
for all $k\ge1$. ✔ $\frac5{32}>\frac18$ ✔.
(vi) The $u=0$ selection reproduces P1's numbers $\frac14,\frac5{24},\frac{13}{64}$ ✔ (its
window *is* a maximum-degree monomial support).
(vii) Witness (b): $T_C(x)=[d]$ (unique), $T_D(y)=\{i\}$ with $y_i=-1$ (multiplicity
$\in[1,d]$, payment selection-independent), $\pi=\frac12+\frac d{2(2^d-1)}$ over denominator
$d+1$; exact $\frac5{18},\frac5{28},\frac{19}{150}$ at $d=2,3,4$ and $\ge\frac1{2(d+1)}$ ✔.
Conclusion: the minimality-of-size proof and the min-over-selections bound are **correct and
complete**, including under Remark 2.2 (window size is deterministically $d$, so
$\mathbb E\pi/2d\ge\min_{\text{selections}}\pi/2d$). The only defect attached to this repair is
the scoping of its consequence, F3.

**§8 frontier.** Item 1's hypothesis-carrying form is right (F4 concerns only VERDICT 5's
summary of it). Item 2's bracket is proved and correctly declared open ✔. Item 3's one-way
sufficiency is correct and the converse is correctly disclaimed ([G3]) ✔. Item 4 ✔. Item 5:
$\pi_{W_{\mathrm{sh}}}\le\pi_{\mathrm{Rel}}$ gives $\eta^*\ge p$, and with $\eta^*\le1$ (T4(d))
$p=1$ forces $\eta^*=1$; the milestone is genuinely cheaper than (PAY$\star$) (no window
choices quantified) ✔.

**Honesty audit.** Status PARTIAL ✔. The declared limits — stipulated class model [G1],
odd-order gap [G2], non-claimed converse [G3], routine [G4], the new [G5] — are real, and
[G1] in particular is the honest one that keeps I02's central question open in both
directions ✔. But the register of limits is **incomplete in two respects**: it does not record
that the barrier reading of both caps depends on a class-model convention the artifact itself
rejects elsewhere (F1 — and [ESCALATED E1] positively asserts the opposite, "used by no cap"),
and it does not record that the escape claim for P5's *declared* (minimal) notion is not
established (F3 is flagged in [G5] but contradicted in VERDICT 1). The [MEMORY] items are
genuinely unused ✔. No [SOURCE-BLOCKED] item exists ✔.

**Negation check (§3.5 step 0.5), per load-bearing lemma, with adjudication tag.**

| Lemma | Negation probed | Would the artifact's evidence exclude it? | Tag |
|---|---|---|---|
| T1 master count | some incompatible family evades $\mathbb E\pi_W\le\delta_F\mathbb E|W(g)|+\delta_G\mathbb E|W(f)|$ | yes — factorisation is exact, independence is used only where legitimate | MECH |
| **T2 value theorem** | **a $\mathcal W$-argument establishes $T>\Theta_W(d)$ by handling only in-scope families** | **no — the proof's point-mass instances are out of scope by Remark 1.1's own criterion, and nothing in the artifact rules the negation out** | **NONE** |
| T3 localisation ceiling | a localised $W$ with $\pi_W>\pi_{\mathrm{Rel}}$ at some pair | yes — non-negativity + localisation on both sides | MECH |
| T4(a)–(d) | a relevant coordinate with $\mathrm{Inf}_i(f_A)<2^{-d-1}$; $\eta^*>1$ | yes — inline proofs; card S6a corroborates (c) without being relied on | MECH (+CARD, non-load-bearing) |
| T5 / T7 tables | a different influence value at either witness | yes — re-derived here by hand in exact arithmetic; the cited scripts are corroborative only | MECH (CODE claimed, not re-run) |
| T6 CAP I (as a bound on $\Theta_W$) | $\Theta_{W_{\mathrm{rel}}}>(d+1)2^{-d-1}$ | yes — single admissible pair, hypothesis discharged | MECH |
| T8 CAP II (as a bound on $\Theta_W$) | an own-heavy $W$ with $\Theta_W>\frac1{2(2^d-1)}$ **and** $W(C)\ne\emptyset$ | yes | MECH |
| T8 as used in §5.3's record sentence (hypothesis dropped) | an own-heavy $W$ with $W(C)=\emptyset$ beating the ceiling | no — Remark 4.2′ concedes no cap is claimed for it | NONE (F2) |
| §5.2 monotonicity | a cap transferring downward | yes — infimum over a superset | MECH |
| §5.4 group forms | CAP II failing for some finite abelian $\mathcal Y$; CAP I failing for even order | yes for both as stated; odd order openly excluded | MECH |
| §7.2 non-canonicity | a canonical localised shattering selection | yes — orbit argument, $1\notin\{0,2^k\}$ | MECH |
| §7.4 minimality + min-over-selections | a minimum certificate of size $<d$, or a selection with ratio $<\frac5{32}$ | yes — recomputed exactly here | MECH (+CODE claimed) |
| §7.4 escape for P5 as planned (*minimal* certificates) | a minimal selection with $\mathbb E|W(A_k)|=2^{d-1}$, capped at $(d+1)2^{-d}$ | no — [G5] concedes it | NONE (F3) |
| §8.5 milestone | (PAY$\star$) at $p=1$ with $\eta^*<1$ | yes | MECH |

---

## 4. SOURCE REQUEST

None for the mathematics. Two register items, for Triage rather than the source queue:
`0023-refuter-2`'s "inequality (M)" (cited in Corollary 3.2 with no row and no restatement,
F7) and the R3–R6 rung definitions in `PROGRESS.md` (declared load-bearing for the scope
clause, outside this pass's inputs, F9). Both are campaign files, not literature.

### END OF ARTIFACT 0023-prover-3-r2-verify-F ###
