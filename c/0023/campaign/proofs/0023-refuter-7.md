---
id: 0023-refuter-7
agent: refuter
model: claude-opus-5[1m]
cycle: 4
status: COMPLETE
---

# The windowed payment $\pi_\tau$ on direct sums of the hub witness

## VERDICT — **PLAN SURVIVES** ($\pi_\tau$ stalls at $\Omega(1)$; it does not decay in $k$ or $d$)

$$\boxed{\ \pi_\tau\ \text{does not decay: for the }k\text{-fold direct sum}\ \pi_\tau=\pi_{\mathrm{Rel}}=k\bigl(1+(d-1)2^{1-d}\bigr)\ \ge k\ \ }$$

**But the milestone could not have failed**, and that is the finding. §4 proves
that at every $d\le 16$ (any $c\le1$; $d\le15$ for any $c\le 3/2$) and **every**
$N$, $H_\tau(A)=\mathrm{Rel}(A)$ *identically*, so $\pi_\tau=\pi_{\mathrm{Rel}}\ge1$
by `0023-refuter-5`. The check was run at $d\le6$. Absolute $p=1$ is therefore a
**theorem** in the whole computationally reachable range; a null result there
rules out nothing about $d\ge17$, which is where (PAY$\star\star$) can first fail.

## 1. The witness, verified from the definitions (exact, $c=1$)

$\deg\mathbf 1_{A_d}=\deg\mathbf 1_{B_d}=d$ and $\alpha=\beta=1/2$ confirmed for
$d=2..6$ by integer Walsh transform. Influences (exact, two independent methods —
Fourier and boundary counting $b_i/2|A|$ — agreeing everywhere):
$\mathrm{Inf}_w=\tfrac12-2^{-d}$ on the hub, $2^{-d}$ on each $u$-coordinate.
There are exactly **two** maximum-degree monomials, $[d]$ and $\{w\}\cup[d]\setminus\{1\}$.

| $d$ | $\alpha$ | $\pi_{\mathrm{Rel}}$ | $\pi_\tau$ | $\pi_{\tau=\infty}$ **min** over $M$ | $\pi_{\tau=\infty}$ **max** over $M$ |
|---|---|---|---|---|---|
| 2 | 1/2 | 3/2 | 3/2 | 1 | 1 |
| 3 | 1/2 | 3/2 | 3/2 | 3/4 | 5/4 |
| 4 | 1/2 | 11/8 | 11/8 | 1/2 | 5/4 |
| 5 | 1/2 | 5/4 | 5/4 | 5/16 | 19/16 |
| 6 | 1/2 | 37/32 | 37/32 | 3/16 | 9/8 |

$\pi_\tau=1+(d-1)2^{1-d}\downarrow 1$: **no decay in $d$ either**, not even
polynomial. Windows: $H_\tau(A)=H_\tau(B)=$ all $d+1$ coordinates at every $d$.

**Correction to the plan's premise.** The hub defeats the $\tau=\infty$ payment
($d\,2^{1-d}$) only under the *minimising* choice $M=[d]$. Since (PAY$\star$) says
"*a* maximum-degree monomial", the choice $M=\{w\}\cup[d]\setminus\{1\}$ gives
$\pi_{\tau=\infty}\ge1$ at every $d$ — the hub witness does **not** defeat the
$\tau=\infty$ version under the existential reading of $M$.

## 2. Direct sums — definition and result

Blocks $j=1..k$ of $d+1$ coordinates, $N=k(d+1)$. Three rules, all non-degenerate,
all computed exactly at $\tau=1/(2D^4)$ with $D$ the **composed** degree (and
re-run at $\tau=1/(2d^4)$ with the block $d$ — identical values):
**P** $A=\prod_jA_d,\ B=\prod_jB_d$ (the stated rule); **C** $A=\prod_jA_d$,
$B=\overline A$; **X** $A=\{\#\{j:\text{block}\in A_d\}\text{ odd}\}$, $B=\overline A$.

| $d$ | $k$ | rule | $N$ | $D$ | $\alpha$ | $\beta$ | $\pi_{\mathrm{Rel}}$ | $\pi_\tau$ | $\pi_{\tau=\infty}$ min |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 2 | P | 8 | 6 | 1/4 | 1/4 | 3 | **3** | 3/2 |
| 3 | 3 | P | 12 | 9 | 1/8 | 1/8 | 9/2 | **9/2** | 9/4 |
| 4 | 2 | P | 10 | 8 | 1/4 | 1/4 | 11/4 | **11/4** | 1 |
| 4 | 3 | P | 15 | 12 | 1/8 | 1/8 | 33/8 | **33/8** | 3/2 |
| 4 | 3 | C | 15 | 12 | 1/8 | 7/8 | 33/14 | **33/14** | 6/7 |
| 4 | 3 | X | 15 | 12 | 1/2 | 1/2 | 33/8 | **33/8** | 3/2 |

(Full $2\le d\le4$, $1\le k\le3$ table in the code output; $\pi_\tau=\pi_{\mathrm{Rel}}$
in all 27 cases, $\pi_\tau^{\min}=\pi_\tau^{\max}$ over the $2^k$ choices of $M$.)

**Why the test is structurally blind.** $f_{A_1\times A_2}=f_{A_1}\!\otimes\!f_{A_2}$,
so $\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(f_{A_d})$ **pointwise**: a direct sum
copies the influence profile and multiplies the *total* by $k$. It cannot
dilute any coordinate below $\tau$; it can only add windows. Direct summation is
the wrong amplifier for this quantity — it *helps* the plan (even the $M$-only
payment grows, $k\cdot d2^{1-d}\ge1$ once $k\ge2^{d-1}/d$).

## 3. Search space covered (and what a null result does not rule out)

Complete sweeps: all 15/255/65535 nonempty sets at $N=2,3,4$ (§4 floor check);
all 50 and 6050 cross-disjoint pairs at $N=2,3$ ($\min\pi_\tau=1$ exactly).
Structured: cylinder pairs $A=\{x_S=\vec+\},B=\overline A$ for $s\le7$ brute
force and $s\le40$ in closed form; ADDRESS functions $k\le3$ ($N\le11$, the
Nisan–Szegedy-extremal spread); hub-of-parity $d\le3,h\le3$; local search at
$N=5,6,7$ under $\deg\le3$ (30 restarts $\times$ 150 moves, never left the
subcube stratum, $\min=3$). **Every one returned $\pi_\tau=\pi_{\mathrm{Rel}}\ge1$.**
This rules out nothing at $d\ge17$: see §4. Compute $\approx4$ min.

## 4. Why: the relevant-coordinate influence floor, and the real threshold

$\partial_i\mathbf 1_A$ is a nonzero multilinear polynomial of degree $\le d-1$
with values in $\{0,\pm\frac12\}$, hence nonzero on $\ge2^{1-d}$ of the cube, so
for every **relevant** $i$: $\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-1-d}$ and
$\mathrm{Inf}_i(f_A)\ge2^{-1-d}/\alpha\ge2^{-1-d}$. Verified exhaustively over all
$65535$ nonempty sets at $N=4$: **0 violations**, equality attained (singletons).
A relevant coordinate can therefore be $\tau$-light only if $2^d>d^4/c$:

$$\textbf{no }\tau\textbf{-light relevant coordinate exists for }d\le16\ (c\le1),\ d\le15\ (c\le3/2),$$

so $W_\tau=\mathrm{Rel}$ and $\pi_\tau=\pi_{\mathrm{Rel}}\ge1$ there, for all $N$.
**(PAY$\star\star$) with absolute $p=1$ is a theorem for every $d\le16$.**

## 5. Near-miss: the one family that reaches the $\tau$-light regime, and its obstruction

$A=\{x_S=\vec+\}$, $B=\overline A$, $|S|=s=D$: $\mathrm{Inf}_i(f_B)=\frac1{2(2^s-1)}<\tau$
for all $i$ once $s\ge17$ — $H_\tau(B)=\emptyset$, the whole $B$-side window
collapses. Exact values ($s=17$: $\pi_{\mathrm{Rel}}=\pi_\tau=1114112/131071$;
$s=40$: $4398046511104/219902325555$). $\pi_\tau$ does not move, because
$\mathbf 1_B=1-\mathbf 1_{x_S=\vec+}$ has a **unique** maximum-degree monomial, $S$
itself, so $M(B)\supseteq S$ pays the full $s/2$ that $H_\tau(B)$ lost.

**The obstruction, precisely.** Whenever the light side factorises,
$\mathbf 1_B=\mathbf 1_{B'}(x_S)\cdot g(x_{P_B})$, $\deg$ is additive and every
maximum-degree monomial meets $S$ in a maximum-degree monomial of $\mathbf 1_{B'}$
— $M$ *cannot* avoid the shared coordinates. A counterexample must therefore make
$B$'s dependence on $S$ and on $P_B$ **non-multiplicative** (a union, not a
product), so that some top-degree monomial lives entirely off $S$, while keeping
$\ge d^4$ shared coordinates $\tau$-light on both sides — which by §4 forces
$d\ge17$, $N\ge17$, i.e. beyond any exhaustive search ($2^{2^{17}}$ sets). That
disjunction — *factorised $\Rightarrow$ $M$ pays; non-factorised $\Rightarrow$ ?* —
is L4's missing case and should be the next target, not more search.

Code: `proofs/0023-refuter-7-code/r7.py` (sections 1–6; exact `Fraction`/integer
FWHT throughout, every influence cross-checked by boundary counting).

### END OF ARTIFACT 0023-refuter-7 ###
