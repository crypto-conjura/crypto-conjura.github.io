---
id: 0023-prover-3-u0
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: UNIT 0 of 6 (METHOD SKETCH)
---

# P6 / class (f) BARRIER — rung R2 (I02). Unit 0: method sketch, definitions, lemma statements

**Plan pursued:** `0023-strategist-2` §3.6 (P6) only. No other plan's work read.

## VERDICT (provisional; final in Unit 6)

**PARTIAL — barrier ESTABLISHED for two explicitly named sub-classes, and
REFUTED as a barrier for the whole window-payment class.** Precisely:

1. A technique class is defined (§2): *window-payment arguments*, the class whose
   entire per-pair input is a payment inequality denominated in a per-function
   coordinate window, assembled by the frozen rung's master count. Its power is
   pinned to a single number $V_W(d)$ per window functional (Lemma L2).
2. **BARRIER (proved, Units 2–3):** every *relevance-denominated* window
   functional has $V_W(d)\le(d+1)2^{-d-1}$, and every *own-heavy* window
   functional (windows contain only coordinates heavy for their own side) has
   $V_W(d)\le\frac1{2(2^d-1)}$. Both are $2^{-\Theta(d)}$, i.e. no better than
   K1. This closes I02's own flagged route ("re-base R1's payment on the
   total-influence budget") in the negative **in its per-coordinate form**, and
   it holds at R2–R6 (Unit 4).
3. **CLAUSE (iv) — the strategist's ruling is CONFIRMED: P1 and P5 ESCAPE**
   (Unit 5), by exact computation on both witnesses, not by fiat: the
   shattering-window functional pays $\ge d/2$ with windows of size $d$ (value
   $\ge1/8$ on witness (a), $\ge1/4$ on witness (b)); the certificate functional
   pays $\ge1/2$ with windows of size $\le 2d$ (value $\ge 1/(2(d+1))$).
4. **The barrier does NOT extend to the whole class, and I prove exactly why**
   (Unit 5, L12): the *universal* ceiling of the class is
   $\eta^*(d):=\inf_{\text{pairs}}\sum_{i\in \mathrm{Rel}(A)\cap\mathrm{Rel}(B)}
   [\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)]$, and both certified witnesses have
   $\pi_{\mathrm{Rel}}=\Theta(d)$, hence provably cannot cap it. A barrier for
   the full class **would follow from** exhibiting a cross-disjoint pair all of
   whose shared relevant coordinates are cheap for **both** sides — exactly
   refuter-3 §6(iii)'s unfound fourth mechanism (the converse is not claimed).
   So the honest status is: the
   class boundary can be cut where the strategist said, the two live plans are on
   the live side, and one number decides the fate of the entire method.
5. A **new equivariant survivor** is recorded (Unit 5, Remark L10.3): the
   argmax-influence window $W_{\max}$ is canonical, escapes both witnesses, and
   is not covered by either cap — a live functional nobody has proposed.

A barrier is not a refutation: **R2 remains open**, and nothing here bears on
its truth.

## 1. Standing conventions

$N,d\in\mathbb N$; the cube is $\{\pm1\}^N$ with uniform measure;
$\hat h(S)$, $\deg$, $\mathrm{Inf}_i(h)=\sum_{S\ni i}\hat h(S)^2$ are the
Contract's. For $\emptyset\ne A\subseteq\{\pm1\}^N$ put
$\alpha_A:=|A|/2^N$, $f_A:=\mathbf 1_A/\lVert\mathbf 1_A\rVert_2
=\alpha_A^{-1/2}\mathbf 1_A$, so $\lVert f_A\rVert_2=1$ and
$\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha_A$.

$$\mathcal C^{\mathrm{ind}}_d(N):=\{f_A:\emptyset\ne A\subseteq\{\pm1\}^N,\ \deg\mathbf 1_A\le d\},\qquad
\mathcal C^{\mathrm{ind}}_d:=\textstyle\bigcup_N\mathcal C^{\mathrm{ind}}_d(N).$$

$\mathrm{Rel}(A):=\{i:\mathbf 1_A$ has a monomial containing $x_i\}
=\{i:\mathrm{Inf}_i(\mathbf 1_A)>0\}$. A **cross-disjoint pair** at degree $d$ is
$(A,B)$ with $A,B\subseteq\{\pm1\}^N$ nonempty, $\deg\mathbf 1_A,\deg\mathbf
1_B\le d$, $A\cap B=\emptyset$; $\mathcal P_d$ is the set of all of them (over
all $N$), and $S(A,B):=\mathrm{Rel}(A)\cap\mathrm{Rel}(B)$.

For indicators, R2's conclusion "$\exists f,g,x$ with $f(x)g(x)\ne0$" is exactly
"$\exists$ a pair with $A\cap B\ne\emptyset$" (I02, combinatorial form), so a
counterexample family to R2 is a pair of finitely supported
$\mathbf F,\mathbf G$ over $\mathcal C^{\mathrm{ind}}_d(N)$ all of whose
cross pairs lie in $\mathcal P_d$; call such a pair of distributions
**incompatible**, and write $\delta_{\mathbf F}:=\max_i\mathbb
E_{\mathbf F}[\mathrm{Inf}_i(f)]$, likewise $\delta_{\mathbf G}$.

## 2. The technique class, formally

This section *is* the deliverable: a barrier is only as good as its class.

**D2 (window functional).** A **window functional** at degree $d$ is a family of
maps $W$ assigning to each $N$ and each nonempty $A\subseteq\{\pm1\}^N$ with
$\deg\mathbf 1_A\le d$ a set $W(A)\subseteq[N]$. It is **localised** if
$W(A)\subseteq\mathrm{Rel}(A)$ for every $A$. It is **canonical**
(equivariant) if $W(\sigma A)=\sigma W(A)$ for every automorphism $\sigma$ of
the cube (signed permutation of coordinates). *Only localisation is assumed in
the caps; canonicity is used solely in the clause-(iv) analysis.*

Two properties name the barrier's sub-classes.

* $W$ is **relevance-denominated with density $c$** (on a family $\mathcal
  A$) if $|W(A)|\ge c\,|\mathrm{Rel}(A)|$ for all $A\in\mathcal A$. The junta
  window $W_{\mathrm{rel}}(A):=\mathrm{Rel}(A)$ has $c=1$.
* $W$ is **own-heavy at level $\theta$** if
  $W(A)\subseteq\{i:\mathrm{Inf}_i(f_A)\ge\theta\}$ for every $A$: a window
  never contains a coordinate cheap *for its own function*. Examples:
  $W^\theta_{\mathrm{hvy}}(A):=\{i:\mathrm{Inf}_i(f_A)\ge\theta\}$;
  $W_{\mathrm{Forced}}(A):=\{i: A$ lies in a subcube fixing $i\}$ (own-heavy at
  $\theta=1/2$, since a forced coordinate has $\mathrm{Inf}_i(f_A)=1/2$).

**D3 (payment).** For localised $W$ and $(A,B)\in\mathcal P_d$,
$$\pi_W(A,B):=\sum_{i\in W(B)}\mathrm{Inf}_i(f_A)+\sum_{i\in W(A)}\mathrm{Inf}_i(f_B),
\qquad \pi_{\mathrm{Rel}}(A,B):=\pi_{W_{\mathrm{rel}}}(A,B).$$
Payment is a **sum over the two sides**, never a $\min$ (drafting constraint
IG3 of `0023-strategist-2` §1; Unit 3 shows the caps hold anyway, which is a
strengthening of refuter-3's $\min$-form killer).

**D4 (the class $\mathcal W$: window-payment arguments).** An argument belongs to
$\mathcal W$ if it establishes R2-type thresholds by exactly this template:

> **(T1)** fix a localised window functional $W$ (each side's window depends on
> its own function only);
> **(T2)** prove a per-pair payment inequality $\pi_W(A,B)\ge
> \rho(|W(A)|,|W(B)|)$ for **all** $(A,B)\in\mathcal P_d$, where $\rho$ is any
> function of the two window sizes;
> **(T3)** conclude by the master count: linearity of expectation over
> independent $f\sim\mathbf F$, $g\sim\mathbf G$, using as its only quantitative
> inputs the hypothesis numbers $\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]\le
> \delta_{\mathbf F}$, $\mathbb E_{\mathbf G}[\mathrm{Inf}_i(g)]\le
> \delta_{\mathbf G}$ and the window sizes.

**Stipulation (definitional, not a theorem).** "Its only per-pair input is
(T2), and its only use of the hypotheses is (T3)" is what membership in
$\mathcal W$ *means*. An argument using anything else about $A,B$ — level
weights, hypercontractivity, correlations between coordinates, the pair's joint
structure, a fibre decomposition, a variance identity — is **outside**
$\mathcal W$ and the barrier says nothing about it. §6 lists the exclusions
explicitly.

**D5 (the value of a window).**
$$\Theta_W(d):=\inf\Bigl\{\tfrac{\pi_W(A,B)}{|W(A)|+|W(B)|}\ :\ (A,B)\in\mathcal P_d,\ |W(A)|+|W(B)|\ge1\Bigr\},$$
$$V_W(d):=\begin{cases}0,&\text{if some }(A,B)\in\mathcal P_d\text{ has }W(A)=W(B)=\emptyset,\\ \Theta_W(d),&\text{otherwise,}\end{cases}$$
with $\Theta_W(d):=0$ if the index set is empty. $V_W(d)$ is the number the
barrier bounds; Lemma L2 shows it is exactly the best threshold any member of
$\mathcal W$ with window $W$ can establish.

## 3. Lemma statements (proved in Units 1–5)

**L1 (master count).** Let $W$ be localised, $(\mathbf F,\mathbf G)$
incompatible over $\mathcal C^{\mathrm{ind}}_d(N)$. Then
$\mathbb E[\pi_W(f,g)]\le\delta_{\mathbf F}\mathbb E|W(g)|+\delta_{\mathbf
G}\mathbb E|W(f)|$. Consequently, if $\pi_W\ge\Lambda\,(|W(A)|+|W(B)|)$ on all
of $\mathcal P_d$ and $\mathbb E[|W(f)|+|W(g)|]>0$, then
$\max(\delta_{\mathbf F},\delta_{\mathbf G})\ge\Lambda$.

**L2 (value theorem: $V_W$ is exactly what the class can prove).** For every
localised $W$ and every $\rho$: if $\pi_W\ge\rho(|W(A)|,|W(B)|)$ on all of
$\mathcal P_d$, the threshold established by (T1)–(T3) is at most $V_W(d)$. In
particular the sub-variant "$\pi_W\ge p$ and $|W|\le m$ always, hence
$\max\delta\ge p/(2m)$" (the frozen rung's shape) yields at most $V_W(d)$.

**L3 (localisation ceiling).** For every localised $W$ and every
$(A,B)\in\mathcal P_d$,
$\pi_W(A,B)\le\pi_{\mathrm{Rel}}(A,B)=\sum_{i\in S(A,B)}[\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)]$.
Hence, with $\eta^*(d):=\inf_{\mathcal P_d}\pi_{\mathrm{Rel}}(A,B)$,
$$\sup\{V_W(d):W\ \text{localised}\}\ \le\ \eta^*(d).$$

**L4 (positivity floor; $\eta^*>0$).** For $(A,B)\in\mathcal P_d$:
(i) $S(A,B)\ne\emptyset$; (ii) $\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-d-1}$ for
$i\in\mathrm{Rel}(A)$, hence $\mathrm{Inf}_i(f_A)\ge2^{-d-1}$;
(iii) $\eta^*(d)\ge2^{-d}$, so $V_{W_{\mathrm{rel}}}(d)\ge$ … (a K1-order bound
for the whole class, obtained inside the class). Both (i) and (ii) are proved
inline from scratch; no source is cited load-bearingly.

**L5 (witness (a): the address pair).** For $k\ge1$, $d=k+1$,
$N=k+2^k$: $A_k:=\{x:y_{\mathrm{addr}(a)}=+1\}$ and $B_k:=A_k^c$ satisfy
$\deg\mathbf 1_{A_k}=\deg\mathbf 1_{B_k}=d$, $\alpha=1/2$,
$\mathrm{Rel}=[N]$ ($|{\cdot}|=k+2^k$),
$\mathrm{Inf}_{a_t}(f)=1/4$, $\mathrm{Inf}_{y_j}(f)=2^{-k-1}$ on both sides,
$\pi_{\mathrm{Rel}}(A_k,B_k)=k/2+1$, and the maximum-degree monomial supports of
$\mathbf 1_{A_k}$ (and of $\mathbf 1_{B_k}$) are exactly the $2^k$ sets
$\{a_1,\dots,a_k,y_j\}$.

**L6 (CAP I: the relevance-denominated cap).** For every localised $W$ and
$d\ge2$ (write $k=d-1$),
$$V_W(d)\ \le\ \frac{d+1}{2\bigl(|W(A_k)|+|W(B_k)|\bigr)}\quad\text{(and }V_W(d)=0\text{ if both are empty).}$$
Hence if $W$ is relevance-denominated with density $c$ on the address family,
$$V_W(d)\ \le\ \frac{d+1}{4c\,(2^{d-1}+d-1)}\ \le\ \frac{d+1}{c\,2^{d+1}},$$
and $V_{W_{\mathrm{rel}}}(d)\le(d+1)2^{-d-1}$. More generally $c\ge1/\mathrm{poly}(d)$,
or merely $|W(A_k)|\ge2^{\varepsilon d}$, gives $V_W(d)=2^{-\Theta(d)}$.

**L7 (CAP II: the own-heavy cap).** Let $C:=\{x:x_1=\dots=x_d=+1\}$,
$D:=C^c$. Then $(C,D)\in\mathcal P_d$, $\mathrm{Rel}(C)=\mathrm{Rel}(D)=[d]$,
$\mathrm{Inf}_i(f_C)=1/2$ and $\mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)}$ for
$i\in[d]$. Consequently every localised $W$ that is own-heavy at a level
$\theta>\frac1{2(2^d-1)}$ satisfies
$$V_W(d)\ \le\ \frac1{2(2^d-1)}.$$
In particular every window selected by an influence threshold
$\theta\ge1/\mathrm{poly}(d)$ is capped at $2^{-\Theta(d)}$, and so is
$W_{\mathrm{Forced}}$ (for which in fact $V=0$).

**L8 (SCOPE: the caps hold at R2–R6).** (i) $V_W$ is monotone in the object
class: enlarging the class of admissible pairs can only lower the infimum, so a
cap proved over $\mathcal P_d$ holds verbatim over any larger pair class.
(ii) Both witnesses are **singleton pairs of normalised indicators**, hence
admissible objects in $\mathcal C^{\mathrm{ind}}_d\subset\mathcal C^+_d\subset
\{\text{signed, unit norm},\deg\le d\}$ and in every rung's class R2–R6
(including R5, whose distributions are point masses). (iii) Therefore the caps
of L6/L7 hold for the corresponding technique at R3, R4, R5 and R6 (ℤ₂
instantiation, and for any group whose $\mathbb Z_2$-pullback is admissible).
(iv) At R4 the target is $c\,e^{-d^\alpha}$ with $\alpha<1$: since
$(d+1)2^{-d-1}<c\,e^{-d^{\alpha}}$ fails for no large $d$ (i.e. the cap is
*below* the R4 target for all large $d$), the class cannot deliver R4's
threshold either.

**L9 (CALIBRATION: what the barrier does NOT condemn).**
(i) **Frozen I01/R1 is not condemned.** R1's engine is a window-payment argument
with $W\supseteq\mathrm{Rel}$, i.e. inside CAP I's technique sub-class — but its
object class is $\mathcal C^{\mathrm{junta}}_d$, which **does not contain
witness (a)** ($|\mathrm{Rel}(A_k)|=k+2^k>d$), while $|W|\le d$ holds there by
fiat. This is the barrier's one-sentence explanation of why R1 was provable and
R2 is not.
(ii) **refuter-3 §5.1's $1/(8d)$ forcing bound is not condemned.** It is the
window-payment argument with $W=W_{\mathrm{Forced}}$ *restricted to the
sub-class of forcing pairs*; witness (b) is not a forcing pair, so it does not
bear on that statement. What CAP II does say is that this route establishes
**nothing** on the complementary (spread) pairs — $V_{W_{\mathrm{Forced}}}=0$
over all of $\mathcal P_d$ — which is exactly the restriction refuter-3
declared.
(iii) **P4's OSSS/variance route is not condemned**: no window, no payment, so
it is outside $\mathcal W$ by D4. Likewise K1's block Cauchy–Schwarz and P2's
fibre construction.

**L10 (CLAUSE (iv), part 1: P1 escapes).** Let $W_{\mathrm{sh}}$ be any
selection of a maximum-degree monomial support (card S7b's shattering window,
$|W_{\mathrm{sh}}|\le d$ by theorem). Then on witness (a)
$\pi_{W_{\mathrm{sh}}}=k/2+2^{-k}$ with $|W|=d$ each, ratio $\ge1/8$; on
witness (b) $\pi_{W_{\mathrm{sh}}}=\frac d2+\frac d{2(2^d-1)}$, ratio
$=\frac14+\frac1{4(2^d-1)}>\frac14$. So **neither witness caps
$W_{\mathrm{sh}}$**, and neither CAP I (windows are $\le d$, not
relevance-denominated: $d/|{\mathrm{Rel}}|=2^{-\Theta(d)}$) nor CAP II
(the window of $B_k$/of $D$ contains coordinates cheap for its own side) applies.
**Structural reason, and it is a theorem (L10.2):** $\mathrm{Aut}(A_k)$ acts
transitively on the $2^k$ target coordinates, and every maximum-degree monomial
support contains exactly one target; hence **no canonical (equivariant)
localised functional can be a shattering window**. P1's escape is purchased
exactly by the non-canonicity that card S7 lists as its obstacle (ii) — and the
master count is indifferent to canonicity (L1 needs only per-function
dependence), so the escape is legitimate, not a loophole.

**L11 (CLAUSE (iv), part 2: P5 escapes).** For the point-indexed certificate
functional $T_A(x)$ (minimum-size certificates, $|T|\le C(\mathbf 1_A)$): on
witness (a) the payment is $k/2+2^{-k}$ with $|T_A|+|T_B|=2d$; on witness (b) it
is $\frac12+\frac d{2(2^d-1)}\ge\frac12$ with $|T_A|+|T_B|=d+1$, ratio
$\ge\frac1{2(d+1)}$. Both exceed every $2^{-\Theta(d)}$; the point-indexed
variant of L1 is stated and the same conclusion drawn. So **P5 escapes too**,
for the same structural reason (poly-size window that is *not* own-heavy).

**L12 (FRONTIER: what a full barrier would need — the honest limit).** By L3 the
whole class is capped by $\eta^*(d)$, and
$$\exists(A,B)\in\mathcal P_d\ \text{with}\ \textstyle\sum_{i\in S(A,B)}[\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)]=2^{-\Theta(d)}
\ \Longrightarrow\ \text{[full barrier for }\mathcal W],$$
i.e. a cross-disjoint pair whose shared relevant coordinates are **all cheap for
both sides simultaneously** would cap P1, P5 and everything else at once. The
converse is **not** claimed (CAP II caps a sub-class while $\eta^*$ stays
$\Theta(d)$); what $\eta^*\ge1/\mathrm{poly}(d)$ does establish is that no cap
can come from the localisation ceiling alone. Both certified witnesses have
$\pi_{\mathrm{Rel}}=\Theta(d)$, hence **provably cannot supply this**; and
$\eta^*(d)\ge2^{-d}$ (L4) with $\eta^*(d)\le1$ (the grid pair). So the two
killers cap sub-classes only, and the fate of the *whole* method is decided by
the single quantity $\eta^*(d)$ — refuter-3 §6(iii)'s unfound fourth mechanism,
now with an exact numerical target.

## 4. Case split / dependency skeleton

```
L1 (count)  ── L2 (value)  ┐
L3 (localisation ceiling) ─┼─→ L6  (CAP I)   ← L5 (address table)
L4 (floor, inline proofs) ─┘   └─→ L7 (CAP II)  ← subcube table (in L7)
L6,L7 ─→ L8 (scope R2–R6) ─→ L9 (calibration: R1, forcing bound, P4 all clear)
L3,L5,L7 ─→ L10, L11 (clause (iv): P1, P5 escape) ─→ L12 (frontier η*)
```

No branch depends on an unread source; §5 lists the only three citations and
each is used non-load-bearingly or is re-proved inline.

## 5. Sources and their role

* **S1 (K1, ACC22 Thm 4.4, $\delta<|\mathcal Y|^{-d}/d$)** — CARD, used only to
  interpret "$2^{-\Theta(d)}$ = no progress".
* **S6c/S6d ($3\cdot2^{d-1}-2\le M(d)\le4.394\cdot2^d$)** — CARD, used only in
  remarks: they say the junta window is *unavoidably* exponential; my caps do
  not depend on them (the address family is exhibited explicitly).
* **S6a's influence quantum $\ge2^{-1-d}$** — CARD, but **re-proved inline**
  (L4(ii)) so that nothing rests on a [RESTATED] item.
* **S7b (Chang–Fang Cor. 3.4 / Thm 1.2: $|W_{\mathrm{sh}}|\le d$ by theorem)** —
  CARD, used only *comparatively*, in clause (iv), to certify that P1's window
  is $\le d$ by theorem. **Window only; the density consequence is never used**
  (S7b usage declaration, per strategist §6.2).
* `0023-refuter-3` §4 supplied the two witness families as *leads*. Every number
  I use is **re-derived from scratch** here (Units 2–3) and independently
  re-checked in exact arithmetic by `0023-prover-3-code/check_witnesses.py`
  (integer Walsh–Hadamard, `Fraction` output); the barrier does not depend on
  refuter-3's code.

## 6. What the class EXCLUDES (stated so the barrier cannot be over-read)

The barrier is silent on, and does **not** condemn: (a) arguments using
influence data beyond the per-coordinate averages (level weights, noise
operators, hypercontractivity); (b) arguments whose window depends on the
**pair** rather than on each function separately (these break L1's independence
factorisation, so they are not in $\mathcal W$ at all, and they are also not
known to be sound); (c) fibre/restriction arguments that change the
normalisation (P2's FIBRE-BALANCE); (d) variance-vs-influence arguments (P4:
OSSS + depth-vs-degree); (e) K1's Cauchy–Schwarz-across-blocks accounting;
(f) constructive arguments that exhibit a common point; (g) any window
functional that is neither relevance-denominated nor own-heavy — in particular
the shattering window (P1), the certificate window (P5) and the
argmax-influence window $W_{\max}$ (new, Unit 5).

Nothing here assumes the class is exhaustive. It is not, and §6 is the register
of what it misses.

EMITTED unit 0 of 6. NEXT UNIT: 1 — proofs of L1–L4 (the framework: master
count, value theorem, localisation ceiling, positivity floor).
ARTIFACT 0023-prover-3.

### END OF ARTIFACT 0023-prover-3-u0 ###
