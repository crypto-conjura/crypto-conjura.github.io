---
id: 0023-prover-3-u1
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: UNIT 1 of 6 (framework: L1–L4)
---

# Unit 1 — the framework: master count, value theorem, localisation ceiling, positivity floor

Conventions, definitions D2–D5 and the class $\mathcal W$: Unit 0 §1–§2.
Throughout, $W$ is a **localised** window functional at degree $d$
($W(A)\subseteq\mathrm{Rel}(A)$ for every admissible $A$), and for
$f=f_A\in\mathcal C^{\mathrm{ind}}_d(N)$ we write $W(f):=W(A)$; this is
well defined because $A=\mathrm{supp}(f_A)$ is recovered from $f_A$.

## L1 (master count)

**Statement.** Let $(\mathbf F,\mathbf G)$ be incompatible finitely supported
distributions over $\mathcal C^{\mathrm{ind}}_d(N)$ and put
$\delta_{\mathbf F}=\max_i\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]$,
$\delta_{\mathbf G}=\max_i\mathbb E_{\mathbf G}[\mathrm{Inf}_i(g)]$. Then, for
$f\sim\mathbf F$ and $g\sim\mathbf G$ drawn **independently**,
$$\mathbb E\bigl[\pi_W(f,g)\bigr]\ \le\ \delta_{\mathbf F}\,\mathbb E|W(g)|
+\delta_{\mathbf G}\,\mathbb E|W(f)| . \tag{L1.1}$$
Consequently, if $\Lambda\in\mathbb R$ satisfies
$\pi_W(A,B)\ge\Lambda\,(|W(A)|+|W(B)|)$ for every cross-disjoint pair
$(A,B)\in\mathcal P_d$, and $\mathbb E\bigl[|W(f)|+|W(g)|\bigr]>0$, then
$$\max(\delta_{\mathbf F},\delta_{\mathbf G})\ \ge\ \Lambda. \tag{L1.2}$$

**Proof.** All index sets are finite ($N<\infty$, both supports finite), so every
interchange below is a finite sum.

Incompatibility means: for all $f\in\mathrm{supp}\,\mathbf F$,
$g\in\mathrm{supp}\,\mathbf G$ and all $x$, $f(x)g(x)=0$. Since $f=f_A$ and
$g=f_B$ are positive multiples of $\mathbf 1_A$ and $\mathbf 1_B$, this says
exactly $A\cap B=\emptyset$; both are nonempty of degree $\le d$, so every cross
pair lies in $\mathcal P_d$. (Used only in the second half.)

For (L1.1), write $\pi_W(f,g)=\sum_{i\in[N]}\mathbf 1\{i\in W(g)\}
\mathrm{Inf}_i(f)+\sum_{i\in[N]}\mathbf 1\{i\in W(f)\}\mathrm{Inf}_i(g)$ and take
expectations. By independence of $f$ and $g$, for each $i$
$$\mathbb E\bigl[\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)\bigr]
=\Pr[i\in W(g)]\cdot\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]
\le\Pr[i\in W(g)]\cdot\delta_{\mathbf F},$$
using $\Pr[i\in W(g)]\ge0$ and $\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]\le
\delta_{\mathbf F}$. Summing over $i$ and using
$\sum_i\Pr[i\in W(g)]=\mathbb E|W(g)|$ gives the first term of (L1.1); the
second is symmetric. $\square$ (L1.1)

For (L1.2): every cross pair is in $\mathcal P_d$, so pointwise on the product
support $\pi_W(f,g)\ge\Lambda(|W(f)|+|W(g)|)$; taking expectations and combining
with (L1.1),
$$\Lambda\,\mathbb E\bigl[|W(f)|+|W(g)|\bigr]\ \le\ \delta_{\mathbf F}\mathbb E|W(g)|+\delta_{\mathbf G}\mathbb E|W(f)|\ \le\ \max(\delta_{\mathbf F},\delta_{\mathbf G})\,\mathbb E\bigl[|W(f)|+|W(g)|\bigr].$$
Divide by the positive number $\mathbb E[|W(f)|+|W(g)|]$. $\blacksquare$

**Remark L1.3 (why the window must be per-function).** The only step using
independence is the factorisation $\mathbb E[\mathbf 1\{i\in
W(g)\}\mathrm{Inf}_i(f)]=\Pr[i\in W(g)]\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]$.
If the window were allowed to depend on the *pair* — $W(A,B)$ — the
factorisation fails and (L1.1) is false in general; such arguments are therefore
outside $\mathcal W$ (Unit 0 §6(b)). This is card S7's obstacle (ii) in its only
load-bearing form: a window functional may be non-canonical, but it must be a
function of one side alone.

## L2 (value theorem: $V_W(d)$ is exactly what the class can prove)

**Statement.** Fix a localised $W$ and any function
$\rho:\mathbb Z_{\ge0}^2\to\mathbb R$ such that
$$\pi_W(A,B)\ \ge\ \rho\bigl(|W(A)|,|W(B)|\bigr)\qquad\text{for every }(A,B)\in\mathcal P_d. \tag{T2}$$
Let $T$ be the threshold established by the template (T1)–(T3) of D4, i.e.
$$T:=\inf_{(\mathbf F,\mathbf G)\ \mathrm{incompatible}}\Lambda(\mathbf F,\mathbf G),\qquad
\Lambda(\mathbf F,\mathbf G):=\begin{cases}\dfrac{\mathbb E\bigl[\rho(|W(f)|,|W(g)|)\bigr]}{\mathbb E\bigl[|W(f)|+|W(g)|\bigr]},&\mathbb E[|W(f)|+|W(g)|]>0,\\[2mm] 0,&\text{otherwise (the count is vacuous).}\end{cases}$$
Then $T\le V_W(d)$. Moreover the frozen rung's variant — "$\pi_W\ge p$ and
$|W|\le m$ uniformly, hence $\max\delta\ge p/(2m)$" — also yields at most
$V_W(d)$.

**Proof.** Two cases, matching D5.

*Case 1: some $(A_0,B_0)\in\mathcal P_d$ has $W(A_0)=W(B_0)=\emptyset$*, so
$V_W(d)=0$. Take $\mathbf F:=\delta_{f_{A_0}}$, $\mathbf G:=\delta_{f_{B_0}}$
(point masses). These are finitely supported distributions over
$\mathcal C^{\mathrm{ind}}_d(N)$ and $A_0\cap B_0=\emptyset$, so the family is
incompatible; and $\mathbb E[|W(f)|+|W(g)|]=0$, so
$\Lambda(\mathbf F,\mathbf G)=0$ and $T\le0=V_W(d)$.

*Case 2: no pair has both windows empty*, so $V_W(d)=\Theta_W(d)$. Let
$(A,B)\in\mathcal P_d$ be arbitrary and again take point masses at $f_A,f_B$;
then $\mathbb E[|W(f)|+|W(g)|]=|W(A)|+|W(B)|\ge1>0$ and
$$\Lambda=\frac{\rho(|W(A)|,|W(B)|)}{|W(A)|+|W(B)|}\ \overset{\text{(T2)}}{\le}\ \frac{\pi_W(A,B)}{|W(A)|+|W(B)|}.$$
Taking the infimum over $(A,B)\in\mathcal P_d$ gives $T\le\Theta_W(d)=V_W(d)$.

For the variant: let $p\le\inf_{\mathcal P_d}\pi_W$ and
$m\ge\sup_{A}|W(A)|$. For any $(A,B)\in\mathcal P_d$ we have $p\le\pi_W(A,B)$ and
$2m\ge|W(A)|+|W(B)|$, hence $p/(2m)\le\pi_W(A,B)/(|W(A)|+|W(B)|)$ whenever the
denominator is positive; taking the infimum, $p/(2m)\le\Theta_W(d)$. In Case 1
the pair $(A_0,B_0)$ forces $p\le\pi_W(A_0,B_0)=0$, so the variant's output is
$\le0=V_W(d)$. $\blacksquare$

**Stipulation, restated (this is a definition, not a theorem).** L2 bounds what
$\mathcal W$ *can output* under D4's stipulation that the count's quantitative
inputs are exactly (T2), the numbers $\delta_{\mathbf F},\delta_{\mathbf G}$, and
the window sizes. It is not a claim that no other argument can do better; §6 of
Unit 0 is the register of excluded techniques. [This is the load-bearing
modelling step of the whole barrier and is flagged again in the GAP REGISTER as
**definitional**, not as a gap in a proof.]

## L3 (localisation ceiling, and the universal ceiling $\eta^*$)

**Statement.** For every localised $W$ and every $(A,B)\in\mathcal P_d$, with
$S=S(A,B)=\mathrm{Rel}(A)\cap\mathrm{Rel}(B)$,
$$\pi_W(A,B)\ \le\ \pi_{\mathrm{Rel}}(A,B)\ =\ \sum_{i\in S}\bigl[\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)\bigr]. \tag{L3.1}$$
Consequently, with $\eta^*(d):=\inf_{(A,B)\in\mathcal P_d}\pi_{\mathrm{Rel}}(A,B)$,
$$V_W(d)\ \le\ \eta^*(d)\qquad\text{for \emph{every} localised }W. \tag{L3.2}$$

**Proof.** $\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha_A=0$ for
$i\notin\mathrm{Rel}(A)$, and all influences are $\ge0$. Hence
$$\sum_{i\in W(B)}\mathrm{Inf}_i(f_A)=\sum_{i\in W(B)\cap\mathrm{Rel}(A)}\mathrm{Inf}_i(f_A)
\le\sum_{i\in \mathrm{Rel}(B)\cap\mathrm{Rel}(A)}\mathrm{Inf}_i(f_A)=\sum_{i\in S}\mathrm{Inf}_i(f_A),$$
using $W(B)\subseteq\mathrm{Rel}(B)$ (localisation). Symmetrically for the other
term; adding gives (L3.1), and the displayed identity for
$\pi_{\mathrm{Rel}}$ is the case $W=W_{\mathrm{rel}}$ of the same computation.

For (L3.2): if some pair has both windows empty then $V_W(d)=0\le\eta^*(d)$
(note $\eta^*\ge0$). Otherwise, for every $(A,B)\in\mathcal P_d$,
$|W(A)|+|W(B)|\ge1$, so by (L3.1)
$\pi_W(A,B)/(|W(A)|+|W(B)|)\le\pi_{\mathrm{Rel}}(A,B)$; take infima.
$\blacksquare$

**Reading.** (L3.2) is the barrier's outer boundary: *no* window-payment
argument, canonical or not, point-indexed or not, poly-windowed or not, can
establish a threshold above $\eta^*(d)$. Unit 5 (L12) shows this is the exact
frontier of the method.

## L4 (positivity floor: $S\ne\emptyset$, the influence quantum, $\eta^*\ge2^{-d}$)

All three parts are proved from scratch; nothing here is cited.

**L4.0 (non-vanishing lemma).** *Let $p=\sum_{S\subseteq[n]}c_Sx_S$ be a
multilinear real polynomial, $p\not\equiv0$, $m:=\deg p$. Then
$\Pr_{x\sim\{\pm1\}^n}[p(x)\ne0]\ge2^{-m}$.*

*Proof.* Pick $T$ with $|T|=m$ and $c_T\ne0$. Fix any
$w\in\{\pm1\}^{[n]\setminus T}$ and let $p_w:\{\pm1\}^T\to\mathbb R$ be the
restriction. A monomial $x_S$ of $p$ contributes to the coefficient of $x_T$ in
$p_w$ only if $S\cap T=T$, i.e. $S\supseteq T$; and $S\supsetneq T$ would give
$|S|>m=\deg p$, impossible. So the coefficient of $x_T$ in $p_w$ equals $c_T\ne0$
and $p_w\not\equiv0$, whence $p_w(y)\ne0$ for at least one $y\in\{\pm1\}^T$. As
$w$ ranges over its $2^{n-m}$ values these points are distinct, so $p\ne0$ at
$\ge2^{n-m}$ points of $\{\pm1\}^n$. $\square$

**L4.1 ($S(A,B)\ne\emptyset$).** *Every $(A,B)\in\mathcal P_d$ has
$\mathrm{Rel}(A)\cap\mathrm{Rel}(B)\ne\emptyset$.*

*Proof.* The multilinear expansion of $\mathbf 1_A$ involves only the variables
$x_i$, $i\in R_A:=\mathrm{Rel}(A)$, so $\mathbf 1_A(x)=h_A(x|_{R_A})$ for some
$h_A:\{\pm1\}^{R_A}\to\{0,1\}$; likewise $\mathbf 1_B(x)=h_B(x|_{R_B})$. As
$A\ne\emptyset$ there is $p\in\{\pm1\}^{R_A}$ with $h_A(p)=1$, and similarly
$q\in\{\pm1\}^{R_B}$ with $h_B(q)=1$. If $R_A\cap R_B=\emptyset$, choose
$x\in\{\pm1\}^N$ with $x|_{R_A}=p$ and $x|_{R_B}=q$ (possible: the two
prescriptions are on disjoint coordinate sets). Then $x\in A\cap B$,
contradicting $A\cap B=\emptyset$. $\square$

**L4.2 (influence quantum).** *If $\deg\mathbf 1_A\le d$ and
$i\in\mathrm{Rel}(A)$ then $\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-d-1}$, hence also
$\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha_A\ge2^{-d-1}$.*

*Proof.* Put $D_i(x):=\tfrac12\bigl(\mathbf 1_A(x^{i\to+1})-\mathbf
1_A(x^{i\to-1})\bigr)$, a function of $x_{[N]\setminus\{i\}}$ with
$$D_i=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)\,x_{S\setminus\{i\}} .$$
The sets $S\setminus\{i\}$, $S\ni i$, are pairwise distinct, so this is the
multilinear (Fourier) expansion of $D_i$ in the $N-1$ variables $x_j$, $j\ne i$;
by Parseval $\mathbb E[D_i^2]=\sum_{S\ni i}\widehat{\mathbf
1_A}(S)^2=\mathrm{Inf}_i(\mathbf 1_A)$. Also $\deg D_i\le d-1$ (each monomial
lost the factor $x_i$), $D_i\not\equiv0$ (as $i$ is relevant), and
$D_i$ takes values in $\{0,\pm\tfrac12\}$ because $\mathbf 1_A$ is
$\{0,1\}$-valued. Hence
$$\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E[D_i^2]=\tfrac14\Pr[D_i\ne0]
\ \overset{\text{L4.0}}{\ge}\ \tfrac14\cdot2^{-(d-1)}=2^{-d-1}.$$
Finally $\alpha_A\le1$. $\square$
(This reproves card S6a's quantum $\ge2^{-1-d}$ inline, so no [RESTATED] item is
load-bearing here. It is attained: for $A=\{x:x_1=\dots=x_d=+1\}$,
$\mathrm{Inf}_i(\mathbf 1_A)=2^{-d-1}$ exactly — see Unit 3.)

**L4.3 ($\eta^*(d)\ge2^{-d}$, and $\eta^*(d)\le1$).** By L4.1 pick $i\in S(A,B)$;
then by L4.2 applied on both sides,
$\pi_{\mathrm{Rel}}(A,B)\ge\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)\ge2\cdot2^{-d-1}=2^{-d}$.
So $\eta^*(d)\ge2^{-d}>0$. For the upper bound take the $d\times d$ grid pair:
$A=$ the row-$r$ subcube $\{x:x_{r,c}=+1\ \forall c\}$, $B=$ the column-$c$
subcube $\{x:x_{r',c}=-1\ \forall r'\}$; both have degree $d$,
$\mathrm{Rel}(A)=$ row $r$, $\mathrm{Rel}(B)=$ column $c$, they are disjoint
(they disagree at the crossing cell), $S=\{(r,c)\}$, and each side has
$\mathrm{Inf}_{(r,c)}(f)=1/2$ (Unit 3, L7.1, with $d$ forced coordinates), so
$\pi_{\mathrm{Rel}}=1$. Hence
$$2^{-d}\ \le\ \eta^*(d)\ \le\ 1 .$$

**Remark L4.4 (the class does deliver something — and it is worse than K1).**
Taking $W=W_{\mathrm{rel}}$, L4.2–L4.3 plus the printed junta bound
$|\mathrm{Rel}(A)|\le4.394\cdot2^d$ (card S6c, READ; used **only** in this
remark) give
$\Theta_{W_{\mathrm{rel}}}(d)\ge2^{-d}/(2\cdot4.394\cdot2^{d})>0.11\cdot4^{-d}$.
So the relevance-denominated route is unconditionally *nonvacuous* — but its
guaranteed output, $\Theta(4^{-d})$, is worse than K1's $2^{-d}/d$, and CAP I
(Unit 2) shows its true value is at most $(d+1)2^{-d-1}$, i.e. of K1's order and
no better. Nothing in this remark is used later.

EMITTED unit 1 of 6. NEXT UNIT: 2 — witness (a), the address pair: exact
influence table (L5) and CAP I (L6).
ARTIFACT 0023-prover-3.

### END OF ARTIFACT 0023-prover-3-u1 ###
