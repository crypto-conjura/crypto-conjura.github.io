---
id: 0023-prover-3-verify-E
agent: verifier-b
model: claude-opus-5[1m]
cycle: 3
---

# Blind referee pass E — adversarial-construction angle

Inputs read: `proofs/0023-prover-3.md` (in full), `CONTRACT.md`,
`intermediates/I02-degree-d-sets.md`, `sources/S1-acc22-card.md`,
`sources/S2-clm23-card.md`. Cards S6a/S6c/S6d/S7b: NOT REACHABLE (see F11).
No shell was available in this pass; all arithmetic below was re-derived by hand
in exact rationals (see F12).

---

## 1. FINAL VERDICT

**DEFECTS FOUND — the two headline caps (CAP I(a)–(c), CAP II with the expensive
side's window nonempty) and the exact witness tables survive an aggressive
attempt to break them, but T2's empty-window case is invalid (class B), so every
"$V=0$" claim collapses; VERDICT clause 1's "P1 has value $\ge1/8$ / P5 has value
$\ge1/(2(d+1))$" contradicts §8.2's own open bracket for $\eta^*$ (class B); §7.4's
minimum certificate is not unique (class B, conclusion survives); and the title's
"per-coordinate window-payment arguments cannot beat $\mathrm{poly}(d)2^{-d}$" is
a claim the artifact itself refutes in §7 (class A scope conflation).**

No refutation of the barrier was found: I could not build a class member that
falls inside D2's literal hypotheses and beats the caps, and the caps' proofs do
bound every such member I could construct (§3 of the log).

## 2. FINDINGS TABLE

| # | Quoted location | Class | Explanation |
|---|---|---|---|
| F1 | Title: "*per-coordinate window-payment arguments cannot beat $\mathrm{poly}(d)\,2^{-d}$*"; §5.3 "*the class cannot deliver R4's sub-exponential target either*"; VERDICT 3 "*the class cannot deliver R4 either*" | **A** | Systematic conflation of $\mathcal W$ (D4) with the two D2 **sub**-classes. What is proved is: (i) relevance-denominated windows are capped, (ii) own-heavy-at-$\theta\ge1/\mathrm{poly}(d)$ windows are capped. §7 exhibits three members of $\mathcal W$ (P1, P5, $W_{\max}$) to which **no** cap applies, and §8.2 leaves $\eta^*\in[2^{-d},1]$ open, so the class as a whole is *not* capped. The VERDICT's opening sentence corrects this ("refuted as a barrier for the whole window-payment class"), but the title and both R4 sentences repeat the wrong scope. A barrier artifact's whole content is the delimitation of its class; mislabelling it is the highest-cost defect here. |
| F2 | T2 proof: "*the point masses at $f_{A_0},f_{B_0}$ form an incompatible family with zero denominator, so $T\le0=V_W(d)$*" (and D5's "$:=0$" clause) | **B** | Invalid inference. The statement an argument in $\mathcal W$ must prove is "**every family with $\delta_{\mathbf F},\delta_{\mathbf G}\le\delta(d)$ is compatible**". A zero-denominator incompatible family need not be *refuted* by the count; it need only be **out of scope**, i.e. have $\max\delta\ge\delta(d)$ — and observing that uses only $\delta_{\mathbf F},\delta_{\mathbf G}$, which (T3) **explicitly permits as inputs**. So the correct ceiling is $\min\bigl(\Theta_W(d),\ \inf\{\max\delta:\text{incompatible},\ \text{all windows empty}\}\bigr)$, a positive number in general (at $(A_k,B_k)$ as point masses, $\max\delta=1/4$; at $(C,D)$, $1/2$), not $0$. Casualties: D5's zero clause read as a barrier statement; T6's "$V_W(d)=0$ if $W(A_k)=W(B_k)=\emptyset$"; T8's "*If also $W(C)=\emptyset$ … $V_W=0$*" branch; Remark 4.3's "*for $W_{\mathrm{Forced}}$ in fact $V=0$*"; §6.2's "*over $\mathcal P_d$ one has $V_{W_{\mathrm{Forced}}}=0$*". **Not** affected: CAP I(a),(b),(c) (their hypotheses force a large window on the address pair) and CAP II whenever $W(C)\ne\emptyset$ — which is the only non-degenerate case for indicators, since $\mathrm{Inf}_i(f_A)\le1/2$ always, so $\theta>1/2$ makes $W$ empty everywhere and the argument vacuous. Net effect: $W_{\mathrm{Forced}}$ is still capped at $\frac1{2(2^d-1)}$ by witness (b); the strictly stronger "establishes nothing" claim is unproved. |
| F3 | VERDICT 1: "*the shattering-window functional (P1) has value $\ge1/8$ and $>1/4$; the certificate functional (P5) has value $\ge1/(2(d+1))$*" | **B** | "Value" is D5's $V_W(d)$, an **infimum over all of $\mathcal P_d$**. §7 computes the ratio at **two** pairs only; nothing there lower-bounds an infimum. Worse, this is internally contradictory: $V_{W_{\mathrm{sh}}}\le\eta^*$ by T3, so "$V_{W_{\mathrm{sh}}}\ge1/8$" would prove $\eta^*(d)\ge1/8$ for all $d$ — exactly what §8.2 records as open ($2^{-d}\le\eta^*\le1$) and what §8.5 invites the reader to *attack* by searching for a pair with $\pi_{\mathrm{Rel}}<1$. The defensible claim, and the one §7.1/§7.4 actually argue, is "the two caps' hypotheses fail for P1 and P5, so neither cap touches them" — an escape from the caps, not a lower bound on the value. |
| F4 | §7.4: "*the unique minimum certificate of $x\in A_k$ is $\{a_1..a_k,y_{b(a)}\}$ (size $d$)*"; "*So the payment equals P1's, $\frac k2+2^{-k}$*" | **B** (contained) | Uniqueness is false. A certificate is determined by the set $U$ of **free** address bits together with all $2^{|U|}$ reachable targets fixed to $+1$; its size is $k-|U|+2^{|U|}$, minimised at **both** $|U|=0$ and $|U|=1$. So whenever $y_{b(a)\oplus e_t}=+1$ at $x$ (true for most $x\in A_k$ once $k\ge1$) there is a second minimum certificate $\{a_{[k]\setminus\{t\}},y_{b(a)},y_{b(a)\oplus e_t}\}$, also of size $d$. Hence "size $d$" is right but the payment is selection-dependent: the $|U|=1$ selection pays $\frac{k-1}2+2^{1-k}$, not $\frac k2+2^{-k}$ (exact ratios $1/4,\,1/6,\,5/32,\,0.1625$ for $k=1..4$). The escape conclusion "ratio $\ge1/8$" **survives** (the minimum over selections and $k$ is $5/32>1/8$), and §7.5's worst case $2^{-k}$ survives too (I checked it for the $|U|=1$ selection: $\Sigma$ still pays only $2^{-k}$ when $a=a'$), but §7.4's stated exactness, and §7.5's $\Sigma$-characterisation ("*$i\in\Sigma$ iff …*") and average $\frac k4+4^{-k}$, hold only for the declared $U=\emptyset$ selection. Since P5's window is a *choice* among minima, the artifact must say which selection it evaluates. |
| F5 | Remark 4.4: "*The min$\to$sum move is necessary but not sufficient*" | **C** | "Not sufficient" is *proved* (T8 exhibits sum-form members that are still capped) — this is the artifact's genuine advance over refuter-3. "**Necessary**" is asserted: the min-form functional is never defined in this artifact, and the only support is `0023-refuter-3` §5.2's $\theta^*(d)\le\frac1{2(2^d-1)}$, which the dependency table itself tags **CERTIFIED (not verified)**. State it as inherited, or drop "necessary". |
| F6 | T9: "*The decisive question for a plan is therefore not "$\min$ or sum?" but: does my window ever contain a coordinate cheap for its own function and expensive for the partner?*"; Remark 4.4 "*the sufficient condition is T9's italicised question*" | **C** | T9 proves this test is necessary and sufficient **to escape witness (b)** — nothing more. It is not sufficient to escape the barrier: §8.1's $\eta^*$ ceiling binds every localised $W$ regardless, and CAP I bites through a different mechanism entirely (Remark 4.5 says so). Calling it "the decisive question for a plan" overstates a one-witness dichotomy. |
| F7 | §7.3: "*Neither relevance-denominated nor own-heavy at level $\ge\frac1{2(2^d-1)}$*"; "*Canonical and localised (both sides of a cross-disjoint pair have $\mathrm{Rel}\ne\emptyset$, T4(b))*" | **C** | Two small gaps. (a) As written the own-heaviness claim needs $\min_A\max_i\mathrm{Inf}_i(f_A)<\frac1{2(2^d-1)}$, which is unproved: the only bound available (T4(c)) gives $2^{-d-1}$, which sits *just below* $\frac1{2(2^d-1)}$, so the inequality is not decided. The claim the argument needs — $W_{\max}$ is not own-heavy at any level **strictly above** $\frac1{2(2^d-1)}$ — does follow from T7, since witness (b)'s $D$ attains that level exactly. Fix the strictness. (b) D1 demands localisation for **every** admissible $A$; $W_{\max}$ of the full cube is $[N]\not\subseteq\mathrm{Rel}=\emptyset$. The parenthetical silently narrows D1 to pairs in $\mathcal P_d$. |
| F8 | §6.1: "*Witness (b) **is** in that class*" [$\mathcal C^{\mathrm{junta}}_d$] | **C/E** | I02 names $\mathcal C^{\mathrm{junta}}_d$ "the $\le d$-window **cylinder-pattern** class" and says "every $\le d$-window cylinder indicator has degree $\le d$"; under that reading $D=C^c$ is a union of $2^d-1$ patterns, not a cylinder pattern, so witness (b) is **not** in $\mathcal C^{\mathrm{junta}}_d$ and the sentence is false. (It is true if $\mathcal C^{\mathrm{junta}}_d$ means all $d$-juntas.) Harmless direction — if witness (b) is outside, §6.1's calibration is only easier — but the class is frozen and this is an assertion about it, not a derivation. Cannot be settled from the permitted inputs. |
| F9 | VERDICT 2: "*This closes I02's own flagged route ("re-base R1's payment argument on the influence budget") **in its per-coordinate / per-relevant-coordinate form**, negatively*" | **C** | The hedge is correct but load-bearing and easy to over-read, and it is buried. I02's flagged route is to **denominate the count by influence mass** ($\sum_i\mathrm{Inf}_i\le d$) instead of by window size. A mass-denominated count is not expressible inside D4(T3), whose only quantitative inputs are $\delta_{\mathbf F},\delta_{\mathbf G}$ and window **sizes**; so that route is not covered by any cap in this artifact. Only the reading "select the coordinates carrying a $1/\mathrm{poly}(d)$ share of the budget" is covered (Remark 4.3, via CAP II, and that is correct). The verdict should carry this exclusion, not only [G1]. |
| F10 | §5.3: "*the classes of **R2 ⊂ R3 ⊂ R4/R5/R6′ ⊂ R6($\mathbb Z_2$)** (`PROGRESS.md`)*"; "*At R4, whose target is $c\,e^{-d^\alpha}$*"; "*R5 needs no distributional part*" | **E** | The rung names, their classes and R4's target live in `PROGRESS.md`, which is not among the permitted inputs. What I could verify is the mathematics: 5.1 (class-genericity) and 5.2 (monotonicity) are correct, the two witness pairs are unit-norm nonnegative $\{0,\text{const}\}$-valued degree-$\le d$ functions, and therefore the caps hold verbatim over **any** class containing them. The mapping onto R3–R6′ and the "cannot deliver R4" comparison are unadjudicated here. The R4 comparison is also only "for all large $d$" with no explicit $d_0$. |
| F11 | §7.1: "*$|W_{\mathrm{sh}}|\le d$ **by theorem**, card S7b; the projection property is not used*"; DEPENDENCIES rows S6a/S6c/S6d/S7b | **E** | Cards S6a, S6c, S6d, S7b are unreachable: only `S1-acc22-card.md` and `S2-clm23-card.md` exist among the paths I could address under `sources/`. Non-load-bearing as used: S6a is re-proved inline (T4(c), verified below), S6c/S6d are context, and S7b's *used* content is true by the definition of degree — a maximum-degree monomial support of a degree-$\le d$ polynomial has size exactly $\deg\le d$ — so "by theorem" is decorative, not a citation defect. **But** it exposes a substantive risk the artifact should close: §7.1 calls the functional the "*shattering* window" while defining it as a maximum-degree monomial support and explicitly disclaiming the projection property. If P1's window is in fact a maximal **shattered** set (the Chang–Fang projection object), then §7.1/§7.4 evaluate a *different* functional from P1's and the escape ruling for P1 does not apply as stated. Unsettleable from the permitted inputs; route to Triage. |
| F12 | — | note | No shell/exec tool was available to this pass, so `0023-prover-3-code/check_witnesses.py` was neither run nor read (it is also outside the permitted inputs). Every printed exact value was instead re-derived by hand in exact rationals; all 24 of them check out (log §2). The independent-check paragraphs are therefore corroborated, not merely accepted. |

## 3. STEP-BY-STEP LOG

### 3.0 Class (A) first: what the artifact actually proves, diffed against the Contract

In my words, discharging the artifact's own labels:

1. For every localised window functional $W$ (windows a function of each side's
   own set), the count $\mathbb E[\pi_W]\le\delta_{\mathbf F}\mathbb E|W(g)|
   +\delta_{\mathbf G}\mathbb E|W(f)|$ holds, and any argument that uses only
   this count plus a payment lower bound in the two window sizes establishes a
   threshold at most $\Theta_W(d)=\inf_{\mathcal P_d}\pi_W/(|W(A)|+|W(B)|)$.
2. Two evaluations of $\Theta_W$: at the address pair, $\Theta_W\le
   \frac{d+1}{2(|W(A_k)|+|W(B_k)|)}$, hence $\le(d+1)2^{-d-1}$ once the window
   has $1/\mathrm{poly}(d)$ relevance density; at the codimension-$d$ subcube
   pair, $\Theta_W\le\frac1{2(2^d-1)}$ once the window is own-heavy above that
   level.
3. A universal ceiling $\Theta_W\le\eta^*(d)$ for every localised $W$, with
   $\eta^*\in[2^{-d},1]$ and its true value **open**.
4. Three named functionals (max-degree-monomial-support, minimum certificate,
   max-influence) to which neither cap applies.

Diff vs. the I02 Contract: the artifact is not a proof or refutation of R2 and
does not claim to be. It is labelled `status: PARTIAL`, states "**R2 remains
open**", never substitutes an $N$-dependent $\delta$, never replaces average
influence by max-over-support in the *statement* it constrains, and it lands
squarely inside the parent CONTRACT's BARRIER CHECKLIST invitation ("arguments
using only per-coordinate influence budgets cannot beat exponential
thresholds"). **No class-A drift against the Contract.** The class-A finding F1
is internal: the artifact's title and its two R4 sentences name a class
(all of $\mathcal W$) that the artifact itself shows is not capped.

On the question I was asked to answer plainly — *would this change what a
researcher should attempt?* Partly, and less than the title implies. Genuinely
actionable and non-straw: **CAP II**, which kills every own-influence-threshold
window at $\theta\ge1/\mathrm{poly}(d)$ *in sum form*, including
$W_{\mathrm{Forced}}$ and "the coordinates carrying a $1/\mathrm{poly}(d)$ share
of the influence budget" — a family a competent prover would try, and which
refuter-3 had killed only in min form; and **§7.2**, a clean structural theorem
that no *canonical* localised functional can select max-degree monomial supports,
so a symmetric route must either go exponentially large (capped) or retreat to
the address hub. Formalising an already-recorded non-solution: **CAP I**, which is
I02's own junta-substitution trap with an explicit ceiling $(d+1)2^{-d-1}$ — new
only in that it shows no cleverer payment inequality rescues the route. Not
constrained at all, and this is most of the space: pair-dependent windows
(excluded by fiat, Remark 2.1), case splits over pair type, mass-denominated
counts (F9), level weights, and all three functionals of §7. So the honest
delta to a researcher's to-do list is "stop trying own-heavy windows", plus one
cheap falsifiable milestone (§8.5). That is real but small, and F1 is the reason
it reads as larger.

### 3.1 Accepted steps (one line each)

- §1 setup, D1–D5: internally consistent; $\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha_A$ is correct for a positive rescaling. ACCEPTED.
- **T1 (master count).** Factorisation $\mathbb E[\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)]=\Pr[i\in W(g)]\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]$ uses only $f\perp g$ and per-own-side windows; finite sums, so no interchange issue; $\sum_i\Pr[i\in W(g)]=\mathbb E|W(g)|$ correct; the "hence" clause correctly requires a positive denominator. ACCEPTED. **MECH.**
- **Remark 2.1 (pair-dependent windows break T1).** ACCEPTED, and I confirmed the inequality genuinely *fails* (not merely that the proof fails), so the exclusion is substantive: take $\mathbf F=\{f_1,f_2\}$, $\mathbf G=\{g_1,g_2\}$ uniform with $\mathrm{Inf}_1(f_1)=\mathrm{Inf}_2(f_2)=\mathrm{Inf}_1(g_1)=\mathrm{Inf}_2(g_2)=1$ and the other influences $0$, so $\delta_{\mathbf F}=\delta_{\mathbf G}=\frac12$; let the pair-window be a coordinate heavy for both when $i=j$ and any single coordinate otherwise. Then $\mathbb E[\pi]=\frac12\cdot2+\frac12\cdot1=\frac32>1=\delta_{\mathbf F}\mathbb E|W|+\delta_{\mathbf G}\mathbb E|W|$. **MECH.**
- **Remark 2.2 (randomised / point-indexed windows).** Conditioning on the draws is legitimate because $\mu_A$ depends on $A$ only and is drawn independently of the other side; T1, T3 and the point-mass evaluation all survive with expectations. I additionally checked two constructions I built to break it — a mixture of $W_{\mathrm{rel}}$ and $W_{\mathrm{sh}}$ at weight $\frac12$ (caught by CAP I(b) at density $c=\frac12$: ratio $\approx(d+1)2^{-d}$ at the address pair) and the same mixture at weight $2^{-d}$ (escapes both caps, density $\approx d2^{1-d}$, and the artifact never claims otherwise). ACCEPTED. **MECH.**
- **T2, non-empty case.** Point masses at $(f_A,f_B)$ for $(A,B)\in\mathcal P_d$ are an admissible incompatible family, so $T\le\rho/(|W(A)|+|W(B)|)\le\pi_W/(|W(A)|+|W(B)|)$; infimum gives $T\le\Theta_W$. I also checked that refusing to symmetrise buys nothing (the rung bounds both sides by the same $\delta$), so the class cannot improve on $\Theta_W$ by asymmetric bookkeeping. ACCEPTED. **MECH.**
- **T2, empty case.** REJECTED — see F2. **NONE.**
- **T3 (localisation ceiling).** $W(B)\cap\mathrm{Rel}(A)\subseteq S(A,B)$ plus $\mathrm{Inf}\ge0$; the ceiling step correctly uses $|W(A)|+|W(B)|\ge1$. Negation check: drop localisation and T3 is false (a window containing an own-irrelevant but partner-relevant coordinate can pay more than $\pi_{\mathrm{Rel}}$), so the hypothesis is load-bearing and used. ACCEPTED. **MECH.**
- **T4(a).** For $\deg p=m$ exactly, the $x_T$-coefficient of $p|_w$ is $\sum_{S\supseteq T}c_Sw_{S\setminus T}=c_T\ne0$ because no $S\supsetneq T$ survives; each of $2^{n-m}$ restrictions is nonzero. ACCEPTED. Applied to $D_i$ with $m=\deg D_i\le d-1$, which is the legitimate use. **MECH.**
- **T4(b).** Correct: cross-disjointness plus $\mathrm{Rel}(A)\cap\mathrm{Rel}(B)=\emptyset$ lets one splice a point of $A$ and a point of $B$. ACCEPTED. **MECH.**
- **T4(c).** $D_i\in\{0,\pm\frac12\}$, $\mathrm{Inf}_i(\mathbf 1_A)=\frac14\Pr[D_i\ne0]\ge\frac142^{-(d-1)}=2^{-d-1}$, divide by $\alpha_A\le1$. ACCEPTED; this genuinely re-proves card S6a inline, so the [RESTATED] tag is not load-bearing. **MECH.**
- **T4(d).** Lower $2^{-d}$ from (b)+(c). Upper: row-subcube vs column-subcube has $S=\{(1,1)\}$, both sides force it, $\pi_{\mathrm{Rel}}=\frac12+\frac12=1$. ACCEPTED. **MECH.** (Unrequested corroboration of the extremality question in item 3 of my brief: **every** pair with $|S|=1$ has $\pi_{\mathrm{Rel}}$ **exactly** $1$ — if $\mathrm{Rel}(A)\cap\mathrm{Rel}(B)=\{i\}$ then for each value $s$ of $x_i$ one of the two slices $A_s,B_s$ is empty, and non-emptiness of $A$ and $B$ forces each side to force $i$, so each contributes $\frac12$ by Remark 4.2(a). Hence $\eta^*(d)<1$ requires $|S|\ge2$, and §8.5's milestone search may be restricted accordingly. The artifact's claim is only $\eta^*\le1$ attained at the grid, which is correct and does not assert unconditional extremality.)
- **T5 (address pair, exact table).** Re-derived independently: $\mathbf 1[b(a)=j]=2^{-k}\sum_T\varepsilon_T(j)a_T$; $y$-free part sums to $\frac12$; expansion coefficients $\pm2^{-k-1}$ on the $2^{2k}$... more precisely on the $2^k\cdot2^k$ distinct monomials $a_Ty_j$, all supports distinct, so (i) *is* the multilinear expansion; $\deg=k+1=d$; top supports exactly the $2^k$ sets $\{a_1..a_k,y_j\}$; $\alpha=\frac12$; $\mathrm{Rel}=[N]=S$, $|\mathrm{Rel}|=k+2^k=2^{d-1}+d-1$; $\mathrm{Inf}_{y_j}(\mathbf 1)=2^k2^{-2k-2}=2^{-k-2}\Rightarrow\mathrm{Inf}_{y_j}(f)=2^{-k-1}$; $\mathrm{Inf}_{a_t}(\mathbf 1)=2^{2k-1}2^{-2k-2}=\frac18\Rightarrow\frac14$; $\sum_i\mathrm{Inf}_i(f)=\frac k4+\frac12$; $\pi_{\mathrm{Rel}}=2(\frac k4+\frac12)=\frac{d+1}2$. Printed independent-check values all confirmed: $|\mathrm{Rel}|=3,6,11$; $\mathrm{Inf}=\frac14$ and $\frac14,\frac18,\frac1{16}$; $\pi_{\mathrm{Rel}}=\frac32,2,\frac52$; ratios $\frac14,\frac16,\frac5{44}$. ACCEPTED. **MECH.**
- **T6 (CAP I).** $\Theta_W\le\pi_W(A_k,B_k)/(|W(A_k)|+|W(B_k)|)\le\frac{(d+1)/2}{|W(A_k)|+|W(B_k)|}$ by T3+T5(v); (a) $W\supseteq\mathrm{Rel}$ with localisation forces $W=\mathrm{Rel}$, sum $=2(2^{d-1}+d-1)$, giving $\le\frac{d+1}{4(2^{d-1}+d-1)}\le(d+1)2^{-d-1}$; (b) $\ge2c(2^{d-1}+d-1)\ge c2^d$ gives $\frac{d+1}{c2^{d+1}}$; (c) immediate. ACCEPTED except the empty branch (F2). **MECH.**
- **T7 (subcube pair, exact table).** $\mathbf 1_C=2^{-d}\sum_{S\subseteq[d]}x_S$; $\alpha_C=2^{-d}$; $\mathrm{Inf}_i(\mathbf 1_C)=2^{d-1}4^{-d}=2^{-d-1}$; $\mathrm{Inf}_i(f_C)=\frac12$; complementation preserves non-constant coefficients so $\mathrm{Inf}_i(\mathbf 1_D)=2^{-d-1}$ and $\mathrm{Inf}_i(f_D)=\frac{2^{-d-1}}{1-2^{-d}}=\frac1{2(2^d-1)}$; $\pi_{\mathrm{Rel}}=\frac d2+\frac d{2(2^d-1)}$. Printed checks confirmed: $\mathrm{Inf}(f_D)=\frac16,\frac1{14},\frac1{30},\frac1{62},\frac1{126}$ and $\pi_{\mathrm{Rel}}=\frac43,\frac{12}7,\frac{32}{15},\frac{80}{31},\frac{64}{21}$ for $d=2..6$. ACCEPTED. **MECH.**
- **Remark 4.2 (forcing).** (a) $x_i\mathbf 1_A=s\mathbf 1_A$ gives $\widehat{\mathbf 1_A}(S\cup\{i\})=s\widehat{\mathbf 1_A}(S)$, hence $\mathrm{Inf}_i(\mathbf 1_A)=\frac{\alpha_A}2$ and $\mathrm{Inf}_i(f_A)=\frac12$. (b) $\alpha_A\le2^{-|F|}$ and $\alpha_A\ge2^{-d}$ by T4(a) give $|F|\le d$. $\mathrm{Forced}(C)=[d]$, $\mathrm{Forced}(D)=\emptyset$, $\mathrm{Forced}(A_k)=\mathrm{Forced}(B_k)=\emptyset$ — all confirmed. ACCEPTED. **MECH.** (Free corollary I used in F2: for indicators $\Pr[D_i\ne0]\le2\alpha_A$, so $\mathrm{Inf}_i(f_A)\le\frac12$ **always**; hence own-heaviness at $\theta>\frac12$ is the identically-empty window.)
- **T8 (CAP II), main branch.** All $\mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)}<\theta$ (including $i\notin[d]$, where it is $0$), so $W(D)=\emptyset$; then $\pi_W(C,D)=|W(C)|\cdot\frac1{2(2^d-1)}$ since $W(C)\subseteq[d]$, and the ratio is exactly $\frac1{2(2^d-1)}$. ACCEPTED; empty branch REJECTED (F2). **MECH.**
- **T9 (dichotomy).** $\frac{\frac12w_D+\frac{w_C}{2(2^d-1)}}{w_C+w_D}$; $w_D=0<w_C$ gives $\frac1{2(2^d-1)}$; $w_D\ge1$ gives $\ge\frac{w_D/2}{w_C+w_D}\ge\frac1{2(w_C+w_D)}\ge\frac1{4d}$ using $w_C,w_D\le d$. ACCEPTED as arithmetic; its gloss overstated (F6). **MECH.**
- **5.1 class-genericity, 5.2 monotonicity.** 5.1's inventory of what T1–T3 use is accurate (incompatibility, independence, $\mathrm{Inf}\ge0$, admissibility of point masses, vanishing off $\mathrm{Rel}$) and T4's floor is indeed used in no cap. 5.2: $\mathcal P_d(\mathcal C)\subseteq\mathcal P_d(\mathcal C')$, the ratio agrees on shared pairs, the empty-window clause transfers, so $V^{\mathcal C'}_{W'}\le V^{\mathcal C}_W$ — **upward only**, and I checked both directions of the brief's item 4: the artifact never transfers a cap downward, and §6.1 uses non-transfer correctly (the address pair has $2^{d-1}+d-1>d$ relevant coordinates, so it is outside any $d$-junta class). ACCEPTED. **MECH.**
- **5.4 groups.** Verified: $\widehat{\mathbf 1_{C_{\mathcal Y}}}$ is supported on the $|\mathcal Y|^d$ characters living in $[d]$, each of modulus $|\mathcal Y|^{-d}$; $\alpha=|\mathcal Y|^{-d}$; $\mathrm{Inf}_i(\mathbf 1_C)=(|\mathcal Y|-1)|\mathcal Y|^{-d-1}$, so $\mathrm{Inf}_i(f_C)=1-|\mathcal Y|^{-1}$ and $\mathrm{Inf}_i(f_D)=\frac{1-|\mathcal Y|^{-1}}{|\mathcal Y|^d-1}$; T8 runs verbatim. Pullback along a surjection $\varphi:\mathcal Y\to\mathbb Z_2$: $\hat\varphi$ is injective on duals, so degrees, coefficients, influences and $\alpha$ are preserved and indicators pull back to indicators with disjointness intact — correct, and every even-order finite abelian group admits such a $\varphi$. [GAP-2] (odd order) is honestly scoped. ACCEPTED. **MECH.**
- **6.4 consistency self-check.** $\frac{2^{-d}}d\le(d+1)2^{-d-1}\iff2\le d(d+1)$, true for $d\ge1$; $\frac{2^{-d}}d\le\frac1{2(2^d-1)}\iff(d-2)2^d\ge-2$, true for $d\ge1$ (equality at $d=1$). Both caps also lie below $\frac1{2d}$. ACCEPTED — and this is the right check for a barrier to run. **MECH / CARD (S1 read, K1 threshold confirmed strict $<|\mathcal Y|^{-d}/d$).**
- **7.1 P1 escape.** $W_{\mathrm{sh}}$ is localised ($i\in S\Rightarrow\mathrm{Inf}_i(\mathbf 1_A)\ge\widehat{\mathbf 1_A}(S)^2>0$) and nonempty on every pair in $\mathcal P_d$ (a pair cannot contain the full cube). Address pair: $\pi=2(\frac k4+2^{-k-1})=\frac k2+2^{-k}$, ratio $\frac{k/2+2^{-k}}{2(k+1)}\ge\frac k{4(k+1)}\ge\frac18$, exact $\frac14,\frac5{24},\frac{13}{64}$ — all confirmed, and confirmed independent of which targets are chosen. Subcube pair: ratio $\frac14+\frac1{4(2^d-1)}$ — confirmed. CAP I(b) at density $c=d/(2^{d-1}+d-1)$ degrades to $\frac{(d+1)(2^{d-1}+d-1)}{d\,2^{d+1}}\approx\frac{d+1}{4d}$ — confirmed, and vacuous against the $\frac1{2d}$ grid ceiling. ESCAPE FROM THE CAPS ACCEPTED; the value claim in VERDICT 1 rejected (F3); the identification of P1's window flagged (F11). **MECH.**
- **7.2 non-canonicity theorem.** Verified in full: with $s_t=1-2c_t$, $b(a')=b(a)\oplus c$ and $y'_{b(a')}=y_{b(a)}$, so $\sigma_c$ fixes $A_k$ and $B_k$ and acts transitively on targets; equivariance makes the target part of $W(A_k)$ a union of orbits, hence $\emptyset$ or all $2^k$; a top support has exactly one target and $1\notin\{0,2^k\}$ for $k\ge1$; (iv) then gives $|W(A_k)|+|W(B_k)|\ge2^{d-1}$ and T6 yields $(d+1)2^{-d}$. This is the artifact's cleanest result. ACCEPTED. **MECH.**
- **7.3 $W_{\max}$.** Canonicity and the two evaluations confirmed ($k\ge2$: $W_{\max}=\{a_1..a_k\}$, $\pi=\frac k2$, ratio $\frac14$; note the $k=1$ exclusion is necessary since there $2^{-k-1}=\frac14$ ties the address influence — the artifact states $k\ge2$ correctly). Size bound $|W_{\max}|\le d/\max_i\mathrm{Inf}_i$ from $\sum_i\mathrm{Inf}_i\le d$. ACCEPTED with F7. The [MEMORY: OSSS + depth-vs-degree] tag is correctly confined to a caveat and used in no claim. **MECH.**
- **7.4 / 7.5 P5.** Minimum certificate **size** $=\min_U(k-|U|+2^{|U|})=k+1=d$ confirmed; uniqueness refuted (F4); subcube-pair values $T_C=[d]$, $T_D=\{i\}$, $\pi=\frac12+\frac d{2(2^d-1)}$, windows summing to $d+1$, exact ratios $\frac5{18},\frac5{28},\frac{19}{150}$ at $d=2,3,4$ — all confirmed. §7.5: under $x\sim\mathrm{Unif}(A_k)$ the address block is uniform and independent of the targets, so $\mathbb E|\{t:a_t\ne a'_t\}|=k/2$ and the average payment is $\frac k4+4^{-k}$, worst case $2^{-k}$ at $a=a'$ — confirmed, including for the alternative $|U|=1$ selection. The relation $\pi_\Sigma\le\pi_W$ (since $\Sigma\subseteq W(A)\cap W(B)$) is what makes the caps bind P5's actual inequality, and it holds. The worst-case/average split is correctly identified as worst-case-vs-average, not conflated. ACCEPTED with F4. **MECH.**
- **8.1–8.5 frontier.** $V_W\le\eta^*$ for every localised $W$ (T3, and it survives randomisation); bracket $[2^{-d},1]$; §8.3's one-directional sufficiency is correctly stated and correctly labelled as not converse; §8.4's two witness values are $\Theta(d)$, so neither witness can supply the frontier; §8.5's implication ($\pi_{W_{\mathrm{sh}}}\le\pi_{\mathrm{Rel}}$, so (PAY$\star$) at $p$ forces $\eta^*\ge p$, and $p=1$ forces $\eta^*=1$) is valid, and the milestone is genuinely cheaper than (PAY$\star$) since no window choices are quantified. ACCEPTED. **MECH.**
- **GAP REGISTER.** [G1] is the honest and correct disclosure that D4 is a stipulation and the class is not exhaustive; [G2], [G3], [G4] are correctly scoped; the [MEMORY] items are genuinely unused. ACCEPTED — this register is the reason F1 is a labelling defect rather than a fabrication.

### 3.2 Adversarial construction attempts (the assignment's core), all failed to refute

1. **Fit R1's $1/(3d)$ engine inside the class over $\mathcal C^{\mathrm{ind}}_d$.** Fails at (T2): R1's payment $\ge1$ with $|W|\le d$ requires the relevance window to be $\le d$, which the address pair destroys ($2^{d-1}+d-1$ relevant coordinates, $\pi_{\mathrm{Rel}}=\frac{d+1}2$). CAP I(a) then binds any $W\supseteq\mathrm{Rel}$ at $(d+1)2^{-d-1}$. **No refutation**, and §6.1's non-transfer reasoning is the correct explanation.
2. **Fit refuter-3's $1/(8d)$ forcing bound inside the class.** $W_{\mathrm{Forced}}$ is localised, own-heavy at $\theta=\frac12>\frac1{2(2^d-1)}$ for $d\ge2$, and $\mathrm{Forced}(C)=[d]\ne\emptyset$ — so T8's **sound** branch applies and the functional is capped at $\frac1{2(2^d-1)}$ over all of $\mathcal P_d$. The $1/(8d)$ result is not a member of $\mathcal W$ because (T2) is proved only on forcing pairs, a restricted pair set (restricting pairs *raises* $\Theta_W$, so no cap applies). **No refutation**; §6.2's ruling stands, minus its "$V=0$" clause (F2).
3. **Randomised / averaged / mixture windows.** Three constructions tried (equal mixture of $W_{\mathrm{rel}}$ and $W_{\mathrm{sh}}$; $2^{-d}$-weighted mixture; certificate-of-a-random-own-point). Each is either caught by the appropriate cap at the density its mixture actually has, or escapes and is already conceded. Remark 2.2's extension is sound. **No refutation.**
4. **Per-function case-split windows** ($W(A)=\mathrm{Forced}(A)$ if nonempty, else $W_{\mathrm{sh}}(A)$). Legitimately inside the class (still per-own-side), and it escapes both caps ($w_D=d\ge1$ on witness (b), density $2^{-\Theta(d)}$ on witness (a)). The artifact does not claim otherwise, so this is consistent with it — but it is a fourth escaping member the artifact does not name, and it shows again that the capped region is small (F1).
5. **Pair-indexed windows.** Genuinely outside: I exhibited a family where T1's inequality is false by a factor $3/2$ (log §3.1, Remark 2.1 entry). So the exclusion is not an artifact of the proof technique — but it is also the exclusion that removes the most plausible route, which the title does not disclose.
6. **A member whose value the caps' proofs fail to bound.** Found only in the branch F2 identifies: an own-heavy $W$ with $W(C)=\emptyset$, and $W_{\mathrm{Forced}}$'s "$V=0$" claim. That is a defect in the cap's reach, not a counterexample to the caps' stated numbers.

### 3.3 Negation check and per-lemma adjudication tags

| load-bearing lemma | negation probed | verdict | tag |
|---|---|---|---|
| T1 master count | drop per-own-side dependence | negation realisable (explicit family, $\frac32>1$) $\Rightarrow$ hypothesis is used, lemma sensitive | **MECH** |
| T2 non-empty case | argument in $\mathcal W$ beating $\Theta_W$ | not realisable; point masses are admissible and asymmetry buys nothing | **MECH** |
| T2 empty case | argument in $\mathcal W$ establishing $T>0$ with some pair's windows both empty | **negation realisable** (discharge by $\delta_{\mathbf F}$, an input D4 permits) $\Rightarrow$ lemma false as a barrier claim | **NONE** |
| T3 localisation ceiling | non-localised $W$ paying above $\pi_{\mathrm{Rel}}$ | realisable, so localisation is genuinely load-bearing and is genuinely assumed | **MECH** |
| T4(a),(c) | degree-$m$ witness with $\Pr[p\ne0]<2^{-m}$ / relevant $i$ with $\mathrm{Inf}_i<2^{-d-1}$ | not realisable; proofs are tight and self-contained (S6a not needed) | **MECH** |
| T5, T7 exact tables | any printed value wrong | all 24 printed values re-derived and confirmed | **MECH** (would be CODE with a shell; F12) |
| T6 CAP I(a)(b)(c) | relevance-denominated $W$ at density $1/\mathrm{poly}(d)$ with value $\ge1/\mathrm{poly}(d)$ | not realisable given T3+T5 | **MECH** |
| T8 CAP II, $W(C)\ne\emptyset$ | own-heavy $W$ at $\theta\ge1/\mathrm{poly}(d)$ with value $\ge1/\mathrm{poly}(d)$ | not realisable given T7 | **MECH** |
| T8 CAP II, $W(C)=\emptyset$ | same | inherits F2; for indicators the branch is degenerate ($\mathrm{Inf}\le\frac12$), for larger classes it is live | **NONE** |
| 5.2 monotonicity | a cap transferring downward | not realisable; direction correct and correctly used | **MECH** |
| 5.4 group version | a finite abelian $\mathcal Y$ of even order where the pullback loses degree or influence | not realisable; $\hat\varphi$ injective | **MECH** |
| 7.2 non-canonicity | a canonical localised max-degree-support selection | not realisable ($1\notin\{0,2^k\}$) | **MECH** |
| K1 comparison (§6.4) | a cap below a proved threshold | not realisable; both inequalities verified | **CARD** (S1 read) |
| S7b size bound (§7.1) | $|W_{\mathrm{sh}}|>d$ | not realisable — true by the definition of degree, so the card is not needed; but the *identity* of P1's window is unsettled | **CARD unreachable / NONE on identity** (F11) |
| I01 / R1 statement (§6.1) | witness (b) membership in $\mathcal C^{\mathrm{junta}}_d$ | unadjudicable from permitted inputs; false under the natural reading of "cylinder pattern" | **NONE** (F8) |
| rung labels R3–R6′ (§5.3) | classes not containing the witnesses | unadjudicable without `PROGRESS.md`; the class-generic statement is verified | **NONE** (F10) |

### 3.4 What a reviser must change, minimally

Not my job to supply the argument, but the defect boundary is worth stating
precisely so Triage can route it: F2 confines itself to the empty-window
convention, so CAP I(a)–(c), CAP II with $W(C)\ne\emptyset$, T9, §5, §7.2, §8 and
both exact tables stand as proved; F3 and F1 are wording of claims the body does
not make; F4 is contained and does not move the $\ge1/8$ conclusion. A reviser
who deletes every "$V=0$" claim, restates the title over the two D2 sub-classes,
replaces "has value $\ge$" with "the caps' hypotheses fail at the two certified
witnesses", and names the certificate selection would, as far as this pass can
tell, be left with a correct artifact. That is not a clean pass, and F11's
identity question must be answered before P1's escape can be recorded.

## 4. SOURCE REQUEST

Rank 1: the campaign's own card **S7b** (Chang–Fang, Thm 1.2 / Cor. 3.4) — needed
only to settle F11, i.e. whether P1's window is a maximum-degree monomial support
(in which case the size bound is definitional and the card is decorative) or a
maximal shattered set via the projection property (in which case §7.1/§7.4
evaluate a different functional and the escape ruling for P1 does not apply as
stated). Rungs tried: ten path guesses under
`c/0023/campaign/sources/` (`S6-*`, `S7-*`, `S6a-*`, `S7b-*` variants); only
`S1-acc22-card.md` and `S2-clm23-card.md` resolve. No web rung attempted, since
the question is about *which object this campaign's P1 uses*, not about the
published theorem. Fallback if unavailable: record F11 as an open identification
question against §7.1 and treat P1's escape as CONDITIONAL.

Rank 2: `PROGRESS.md`'s rung definitions R3, R4, R5, R6′ and R4's declared target
— needed only to adjudicate §5.3's rung mapping (F10). Fallback: accept §5.1–5.2
as proved (they are) and record §5.3 as UNVERIFIED labelling.

Not requested: S6a (re-proved inline and verified), S6c, S6d (context only),
`0023-refuter-3` and `0023-prover-1` (correctly cited as CERTIFIED / FROZEN and
not load-bearing for any cap).

### END OF ARTIFACT 0023-prover-3-verify-E ###
