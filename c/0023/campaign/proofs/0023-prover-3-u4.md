---
id: 0023-prover-3-u4
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: UNIT 4 of 6 (SCOPE lemma + CALIBRATION lemma)
---

# Unit 4 — L8: the scope of the barrier (R2–R6); L9: what it does NOT condemn

## L8 (SCOPE)

### L8.0 The framework is class-generic

Let $\mathcal C$ be **any** family of functions $h:\{\pm1\}^N\to\mathbb R$
($N$ ranging over $\mathbb N$) with $\lVert h\rVert_2=1$ and $\deg h\le d$. Put
$\mathrm{Rel}(h):=\{i:\mathrm{Inf}_i(h)>0\}$;
$$\mathcal P_d(\mathcal C):=\{(h_1,h_2)\in\mathcal C\times\mathcal C:\ \text{same }N,\ h_1h_2\equiv0\},$$
and for a localised window functional $W$ on $\mathcal C$ ($W(h)\subseteq
\mathrm{Rel}(h)$) define $\pi_W$, $\Theta^{\mathcal C}_W(d)$, $V^{\mathcal
C}_W(d)$ exactly as in D3–D5 with $\mathcal P_d$ replaced by $\mathcal
P_d(\mathcal C)$.

*Every proof in Units 1 and 3 is class-generic.* L1 uses only: (a) all cross
pairs of an incompatible family lie in $\mathcal P_d(\mathcal C)$ — which is the
definition of incompatible; (b) independence; (c) $\mathrm{Inf}_i\ge0$. L2 uses
only that point masses on $\mathcal C$ are admissible distributions. L3 uses only
$\mathrm{Inf}_i(h)=0$ off $\mathrm{Rel}(h)$. So L1–L3 hold over every such
$\mathcal C$, verbatim. (L4's floor $\eta^*\ge2^{-d}$ is *indicator-specific* —
it uses $\{0,1\}$-valuedness — and is not used in any cap.)

### L8.1 Monotonicity in the object class

**Statement.** Let $\mathcal C\subseteq\mathcal C'$ and let $W'$ be a localised
window functional on $\mathcal C'$, $W:=W'|_{\mathcal C}$. Then
$$V^{\mathcal C'}_{W'}(d)\ \le\ V^{\mathcal C}_{W}(d).$$

**Proof.** $\mathcal P_d(\mathcal C)\subseteq\mathcal P_d(\mathcal C')$. If some
pair in $\mathcal P_d(\mathcal C)$ has both $W$-windows empty, the same pair lies
in $\mathcal P_d(\mathcal C')$ with both $W'$-windows empty, so
$V^{\mathcal C'}_{W'}=0$. Otherwise $\Theta^{\mathcal C'}_{W'}$ is an infimum of
the same ratios over a superset of pairs, hence $\le\Theta^{\mathcal C}_{W}$.
$\blacksquare$

**Consequence (the shape of the scope claim).** A cap proved by exhibiting one
witness pair inside $\mathcal C^{\mathrm{ind}}_d$ **automatically holds over every
larger object class**, for the corresponding technique. So the scope question
reduces to: in which rungs' classes do the two witnesses live?

### L8.2 Both witnesses are singleton pairs of normalised indicators

$(A_k,B_k)$ (L5) and $(C,D)$ (L7.1) are pairs of nonempty degree-$\le d$ subsets
of $\{\pm1\}^N$; the corresponding functions $f_{A_k},f_{B_k},f_C,f_D$ are
unit-norm, nonnegative, $\{0,\text{const}\}$-valued, of degree $\le d$; the pairs
are cross-disjoint; and taken as **point-mass** distributions they satisfy the
rungs' hypotheses with $\delta=\max_i\mathrm{Inf}_i$. Hence, with the ladder's
class names (`PROGRESS.md`, verbatim):
$$\{f_{A_k},f_{B_k},f_C,f_D\}\subset\mathcal C^{\mathrm{ind}}_d
\subset\mathcal C^{+}_d
\subset\{h:\{\pm1\}^N\to\mathbb R,\ \lVert h\rVert_2=1,\ \deg h\le d\}
\subset\{h:\{\pm1\}^N\to\mathbb C,\ \dots\},$$
and each inclusion is the class inclusion of R2 $\subset$ R3 $\subset$
R4/R5/R6′ $\subset$ R6($\mathbb Z_2$).

### L8.3 The caps at R2, R3, R4, R5, R6

Combining L8.1 with L6 and L7.3:

| rung | object class | CAP I applies | CAP II applies | numerical ceiling |
|---|---|---|---|---|
| **R2** | $\mathcal C^{\mathrm{ind}}_d$ | yes | yes | $(d+1)2^{-d-1}$ / $\frac1{2(2^d-1)}$ |
| **R3** | $\mathcal C^{+}_d$ (nonneg.) | yes | yes | same |
| **R4** | signed, all supports, target $c\,e^{-d^\alpha}$ | yes | yes | same |
| **R5** | signed, point masses | yes | yes | same |
| **R6′** | signed ℝ-valued, all supports | yes | yes | same |
| **R6** ($\mathcal Y=\mathbb Z_2$ instantiation) | ℂ-valued | yes | yes | same |

For R5 note that the barrier does not even need the distributional part: L2's
proof already evaluates the count at point masses, so $V_W$ is the same number
whether or not spreading is allowed. For R4 the target threshold is
$c\,e^{-d^{\alpha}}$ with $\alpha<1$, $c>0$; since
$$\frac{d+1}{2^{d+1}}\ <\ c\,e^{-d^{\alpha}}\quad\text{for all sufficiently large }d
\qquad(\text{because } e^{d^\alpha}\,(d+1)/2^{d+1}\to0),$$
a technique capped at $(d+1)2^{-d-1}$ **cannot deliver R4's sub-exponential
target either**. The same comparison applies to CAP II's $\frac1{2(2^d-1)}$.

**Statement of the scope lemma, then, in one sentence.** *For every rung R2–R6
(over $\mathbb Z_2$), every window-payment argument whose window functional is
relevance-denominated (CAP I) or own-heavy at level $\ge1/\mathrm{poly}(d)$ (CAP
II) establishes at most $\max(\delta_{\mathbf F},\delta_{\mathbf
G})\ge\mathrm{poly}(d)\,2^{-d}$; in particular it establishes neither R2's
inverse-polynomial target, nor R3's, nor R5's, nor R6's, nor even R4's
sub-exponential target.* This confirms `0023-strategist-2` §3.6's scope
prediction, with the inclusions spelled out (L8.2) and the mechanism
(monotonicity, L8.1) made explicit.

### L8.4 Group scope

* **CAP II generalises to every finite abelian group $\mathcal Y$** (proved
  inline). Fix $y_0\in\mathcal Y$ and let
  $C_{\mathcal Y}:=\{x\in\mathcal Y^N:x_1=\dots=x_d=y_0\}$,
  $D_{\mathcal Y}:=C_{\mathcal Y}^{\,c}$. Then
  $\mathbf 1_{C_{\mathcal Y}}=\prod_{i\le d}\frac1{|\mathcal Y|}\sum_{\chi\in
  \widehat{\mathcal Y}}\overline{\chi(y_0)}\chi(x_i)$, so
  $\widehat{\mathbf 1_{C_{\mathcal Y}}}(\chi)$ is nonzero exactly for the
  $|\mathcal Y|^{d}$ characters supported in $[d]$, each of modulus
  $|\mathcal Y|^{-d}$; hence $\deg=d$, $\alpha=|\mathcal Y|^{-d}$, and for
  $i\le d$, $\mathrm{Inf}_i(\mathbf 1_{C_{\mathcal Y}})
  =\alpha\bigl(1-\tfrac1{|\mathcal Y|}\bigr)$ (the fraction of those characters
  with $\chi_i$ non-trivial), i.e.
  $$\mathrm{Inf}_i(f_{C_{\mathcal Y}})=1-\tfrac1{|\mathcal Y|},\qquad
  \mathrm{Inf}_i(f_{D_{\mathcal Y}})=\frac{1-1/|\mathcal Y|}{|\mathcal Y|^{d}-1},$$
  the latter because $\mathbf 1_{D}=1-\mathbf 1_{C}$ has the same non-trivial
  coefficients and $\alpha_D=1-|\mathcal Y|^{-d}$. Repeating L7.3 verbatim: any
  localised own-heavy functional at level
  $\theta>\frac{1-1/|\mathcal Y|}{|\mathcal Y|^d-1}$ has
  $V_W(d)\le\frac{1-1/|\mathcal Y|}{|\mathcal Y|^d-1}\le|\mathcal Y|^{-\Theta(d)}$.
  So CAP II reaches the **top rung for every group**, not only $\mathbb Z_2$.
* **CAP I is proved for $\mathbb Z_2$**, hence for every $\mathbb
  Z_2$-instantiated rung, and transports to every finite abelian group of **even
  order**: if $\varphi:\mathcal Y\to\mathbb Z_2$ is a surjective homomorphism,
  then $A':=(\varphi^N)^{-1}(A)$ satisfies $\mathbf 1_{A'}=\mathbf
  1_A\circ\varphi^N$, whose Fourier expansion is obtained from that of
  $\mathbf 1_A$ by replacing each $\mathbb Z_2$-character by its pullback (a
  character of $\mathcal Y$, non-trivial iff the original is), so degree,
  all coefficients, all influences, $\alpha$, and disjointness are preserved
  exactly.
* **[GAP — scope limitation, not attempted]** For groups of **odd** order there
  is no $\mathbb Z_2$ quotient and I give no native address-type witness, so CAP
  I is **not** established there. This limits only CAP I, only for odd-order
  groups, and only at the top rung (the ladder's declared route is
  $\mathbb Z_2$).

## L9 (CALIBRATION — the three things the barrier must not condemn, and does not)

A class that condemned a proved $\mathrm{poly}(d)$ result would be false. Three
tests, each resolved by locating the object or the technique relative to the
class boundary.

### L9.1 Frozen I01 / rung R1 ($\delta=1/(3d)$, $\varepsilon^*_{\mathrm{junta}}=1/(2d)$) — NOT condemned

R1's engine *is* a window-payment argument, with $W$ the class-given
$\le d$-sized cylinder window (so $W\supseteq\mathrm{Rel}$: relevance-complete,
CAP I's technique sub-class), payment $\pi_W\ge1$ and $|W|\le d$, assembled by
exactly L1. Its object class is
$$\mathcal C^{\mathrm{junta}}_d=\{f_A:\ A=\{x:x_J\in P\},\ |J|\le d\}. $$
CAP I's cap does **not** apply over that class, because **witness (a) is not in
it**: $|\mathrm{Rel}(A_k)|=k+2^k=2^{d-1}+d-1>d$ (L5(3)), so $A_k$ is not a
$\le d$-window cylinder pattern, and by L8.1 the cap transfers only *upward*
(to larger classes), never downward. Witness (b) *is* in
$\mathcal C^{\mathrm{junta}}_d$ ($C$ and $D=C^c$ are both patterns on the window
$[d]$), but CAP II does not apply either, since R1's window is not own-heavy: on
$D$ it is $[d]$, whose coordinates have $\mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)}$ —
cheap for their own function. Consistency check with witness (b) inside R1's
class: L7.5 with $w_C=w_D=d$ gives ratio $\frac14+\frac1{4(2^d-1)}\ge\frac14$,
comfortably above R1's proved $\frac1{2d}$.

**The barrier's one-sentence diagnosis of the R1$\to$R2 jump:** *R1 is provable
by a relevance-denominated payment because its class caps the relevance window at
$d$ by fiat; R2 is not, because its class contains a degree-$d$ set with
$2^{d-1}$ relevant coordinates and only $\Theta(d)$ units of payment to
distribute over them.*

### L9.2 refuter-3 §5.1's forcing bound ($\max\delta\ge1/(8d)$ for families with $\Pr[\text{forcing conflict}]\ge\tfrac12$) — NOT condemned

That argument is the window-payment argument with $W=W_{\mathrm{Forced}}$
(localised, $|W|\le d$ by L7.2(b), own-heavy at $\theta=\tfrac12$ by L7.2(a)),
**restricted to the sub-class of forcing pairs** — pairs sharing a coordinate
forced oppositely by the two sides. On that sub-class the payment is
$\pi_W\ge\tfrac12+\tfrac12=1$ and the windows are $\le d$, so the restricted
value is $\ge\frac1{2d}$: a genuine $\mathrm{poly}(d)$ result about a declared
sub-class, exactly as refuter-3 declared it.

CAP II applies to $W_{\mathrm{Forced}}$ only as a route to **all** of R2, and
what it says is precisely refuter-3's own caveat: witness (b) is **not** a forcing
pair ($\mathrm{Forced}(D)=\emptyset$), so the payment inequality $\pi\ge1$ is
false there; over all of $\mathcal P_d$ one gets $V_{W_{\mathrm{Forced}}}(d)\le
\frac1{2(2^d-1)}$, and in fact $=0$ because the address pair (which forces
nothing on either side, L5) has both windows empty. **No contradiction, and no
condemnation:** the barrier says the forcing window cannot be extended from the
forcing sub-class to $\mathcal P_d$, which is what "the whole residual difficulty
of R2 is the spread case" (refuter-3 §5) already asserted.

### L9.3 P4's variance route, K1's proof, P2's construction — outside the class

* **P4** (OSSS + depth-vs-degree $\Rightarrow$ $\max_i\mathrm{Inf}_i(f_A)\ge
  \frac{1-\alpha}{4D}$ for the sparser side, hence $\frac1{8D}$): no window, no
  payment inequality, no per-pair charge — it is a statement about **one**
  function's variance. It is not in $\mathcal W$ by D4, so neither CAP applies.
  (Consistency: P4's conclusion concerns max-influence/bounded-support variants,
  not R2's average hypothesis, so no clash with the caps either way.)
* **K1** (card S1, ACC22 Thm 4.4): its proof is a Cauchy–Schwarz over the
  $|\mathcal Y|^d-1$ non-constant blocks of $g$ restricted to a maximum-degree
  character's coordinates — again no per-pair payment; outside $\mathcal W$.
* **P2** (fibre-wise construction of a common point): exhibits a point rather
  than charging influence; outside $\mathcal W$ (Unit 0 §6(c),(f)).

### L9.4 Consistency of the caps with proved thresholds (a self-check the barrier must pass)

A cap **below** a proved threshold would refute the barrier. Both caps sit
strictly above K1's proved threshold $2^{-d}/d$ (card S1):
$$\frac{2^{-d}}{d}\ \le\ \frac{d+1}{2}\,2^{-d}=(d+1)2^{-d-1}\quad(d\ge1),\qquad
\frac{2^{-d}}{d}\ \le\ \frac1{2(2^d-1)}\quad(d\ge2),$$
the second because $d\,2^d\ge2(2^d-1)$ for $d\ge2$. Both are far below the grid
ceiling $\frac1{2d}$ (I02's IG1) and below R2's inverse-polynomial target, as a
barrier must be. So the barrier is consistent with everything the campaign has
proved, and its content is exactly: *the capped sub-classes cannot climb out of
K1's exponential regime.*

EMITTED unit 4 of 6. NEXT UNIT: 5 — CLAUSE (iv): where P1 (shattering window) and
P5 (certificate window) sit relative to the class, the non-canonicity theorem,
the new equivariant survivor $W_{\max}$, and L12 (the exact frontier $\eta^*$).
ARTIFACT 0023-prover-3.

### END OF ARTIFACT 0023-prover-3-u4 ###
