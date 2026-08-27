---
id: 0023-prover-2-u3
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE (unit 3 of 5)
---

# Unit 3 — T4 (anatomy of the obstruction) and T5 (the repaired key step, and exactly what would kill it)

Notation as in u0 §0; L1–L5, T1–T3 as in u1–u2.

---

## T4 (the two-parameter family behind T3). PROVED-INLINE

**Definition ($\mathsf H(k,g,\Delta)$).** Let $k\ge2$, $m\ge1$, $N=k+m$; write
points as $(u,w)$, $u\in\{\pm1\}^k$ (the **block**), $w\in\{\pm1\}^m$ (the
**spectators**). Let $g:\{\pm1\}^m\to\{\pm1\}$ be **balanced**
($\mathbb E[g]=0$) of degree $D:=\deg g\ge1$, and let $p,q\in\{\pm1\}^k$ differ
exactly on a set $\Delta\subseteq[k]$ of **odd** size. Put $h:=\frac{1+g}2$
(which is $\{0,1\}$-valued) and
$$\mathbf 1_{\mathsf A}:=h\,(1-\mathbf 1_p)+(1-h)\,\mathbf 1_q,\qquad \mathsf B:=\mathsf A^{\,c}.$$
(For $k=d$, $m=1$, $g=w$, $\Delta=\{1\}$ this is exactly $\mathsf H_d$ of u2.)

**Statement.** Write $\varepsilon^T=\prod_{i\in T}p_i$ for $T\subseteq[k]$, and
call $T$ *even* or *odd* according to the parity of $|T\cap\Delta|$. Then:

1. $\mathsf A,\mathsf B$ are nonempty and disjoint, and $\alpha=\beta=\frac12$;
2. the nonzero multilinear coefficients of $\mathbf 1_{\mathsf A}$ are exactly
   $$\tfrac12\ \text{at}\ (\emptyset,\emptyset);\quad (\tfrac12-2^{-k})\hat g(S)\ \text{at}\ (\emptyset,S),\ S\ne\emptyset;\quad
   -2^{-k}\varepsilon^T\ \text{at}\ (T,\emptyset),\ T\ \text{odd};\quad
   -2^{-k}\varepsilon^T\hat g(S)\ \text{at}\ (T,S),\ T\ne\emptyset\ \text{even},\ S\ne\emptyset;$$
3. $\deg\mathbf 1_{\mathsf A}=\deg\mathbf 1_{\mathsf B}=\max(k,\,D+k-1)$; hence
   $f_{\mathsf A},f_{\mathsf B}\in\mathcal C^{\mathrm{ind}}_d$ whenever
   $k\le d$ and $D\le d-k+1$;
4. $\mathrm{Inf}_{u_i}(\mathbf 1_{\mathsf A})=2^{-k-1}$ for every block
   coordinate, and $\mathrm{Inf}_j(\mathbf 1_{\mathsf A})=Q_k\,\mathrm{Inf}_j(g)$
   for every spectator coordinate, where
   $Q_k:=(\tfrac12-2^{-k})^2+(2^{k-1}-1)2^{-2k}$ satisfies $4Q_k=1-2^{1-k}$;
   all influences of $\mathbf 1_{\mathsf B}$ agree with those of
   $\mathbf 1_{\mathsf A}$;
5. if $D\ge2$, the maximum-degree monomial supports of $\mathbf 1_{\mathsf A}$
   and of $\mathbf 1_{\mathsf B}$ are exactly the sets $T\cup S$ with
   $T\subseteq[k]$ even, $|T|=k-1$, and $S$ a maximum-degree character support
   of $g$ ($|S|=D$, $\hat g(S)\ne0$); if $D=1$ they are these together with the
   full block $[k]$;
6. for **every** maximum-degree monomial support $V=T\cup S$ as in (5),
   $$\pi\bigl((\mathsf A,V),(\mathsf B,V)\bigr)=(k-1)2^{1-k}+(1-2^{1-k})\sum_{j\in S}\mathrm{Inf}_j(g).$$

**Proof.** *(1)* Disjointness and nonemptiness are immediate ($\mathsf B$ is
the complement, and $\mathsf A\ni$ the points with $h=0,u=q$). $\alpha$ is the
constant coefficient, computed in (2).

*(2)* $\mathbf 1_p(u)=2^{-k}\sum_{T}\varepsilon^Tu^T$ and
$\mathbf 1_q(u)=2^{-k}\sum_T\varepsilon^T(-1)^{|T\cap\Delta|}u^T$, so
$$\mathbf 1_{\mathsf A}=h+2^{-k}\sum_{T\subseteq[k]}u^T\Bigl[(1-h)\varepsilon^T(-1)^{|T\cap\Delta|}-h\varepsilon^T\Bigr].$$
For $T$ odd the bracket is $-\varepsilon^T[(1-h)+h]=-\varepsilon^T$; for $T$
even it is $\varepsilon^T(1-2h)=-\varepsilon^Tg$. With $h=\frac{1+g}2$ this
gives
$$\mathbf 1_{\mathsf A}=\tfrac12+\tfrac{g}{2}-2^{-k}\!\!\sum_{T\ \mathrm{odd}}\!\varepsilon^Tu^T\ -\ 2^{-k}g\!\!\sum_{T\ \mathrm{even}}\!\varepsilon^Tu^T .$$
Expanding $g=\sum_S\hat g(S)\chi_S$ and collecting: the pure-spectator
monomials $(\emptyset,S)$ receive $\frac{\hat g(S)}2$ from $\frac g2$ and
$-2^{-k}\hat g(S)$ from the last sum's $T=\emptyset$ term (which is even, with
$\varepsilon^\emptyset=1$), total $(\frac12-2^{-k})\hat g(S)$; at
$(\emptyset,\emptyset)$ this is $\frac12+(\frac12-2^{-k})\hat g(\emptyset)=\frac12$
because $g$ is balanced. Odd $T$ (necessarily nonempty) receive
$-2^{-k}\varepsilon^T$ at $S=\emptyset$ only; nonempty even $T$ receive
$-2^{-k}\varepsilon^T\hat g(S)$, which vanishes at $S=\emptyset$ since
$\hat g(\emptyset)=0$. The four families of index pairs are pairwise disjoint,
so there is no further cancellation. This also gives
$\alpha=\frac12$, hence $\beta=\frac12$.

*(3)* From (2): odd-$T$ monomials have degree $|T|\le k$, with $T=[k]$ odd
(as $|\Delta|$ is odd) so degree $k$ is attained; even-$T$ monomials have
degree $|T|+|S|\le(k-1)+D$, and $|T|=k-1$ is attained by $T=[k]\setminus\{i\}$
for $i\in\Delta$ (then $|T\cap\Delta|=|\Delta|-1$ is even) with $|S|=D$
attained by any maximum-degree character of $g$; pure-spectator monomials have
degree $\le D$. So the degree is $\max(k,D+k-1)$. $\mathbf 1_{\mathsf B}=1-
\mathbf 1_{\mathsf A}$ has the same non-constant coefficients up to sign.

*(4)* Each monomial containing a fixed block coordinate $u_i$ contributes
$2^{-2k}$ in total: an odd $T\ni i$ contributes $2^{-2k}$ (one monomial), and
an even $T\ni i$ contributes $2^{-2k}\sum_S\hat g(S)^2=2^{-2k}$ (since
$\mathbb E[g^2]=1$). There are $2^{k-1}$ sets $T\subseteq[k]$ containing $i$,
so $\mathrm{Inf}_{u_i}=2^{k-1}2^{-2k}=2^{-k-1}$. For a spectator $j$, summing
the squared coefficients over the monomials containing $\chi_j$ gives
$\mathrm{Inf}_j=\bigl[(\tfrac12-2^{-k})^2+\#\{T\ne\emptyset\ \text{even}\}\,2^{-2k}\bigr]\mathrm{Inf}_j(g)$,
and $\#\{T\subseteq[k]\ \text{even}\}=2^{k-1}$ (the map $T\mapsto T\triangle\{i_0\}$,
$i_0\in\Delta$, is a bijection between even and odd $T$), so the bracket is
$Q_k$. Finally $4Q_k=(1-2^{1-k})^2+(2^{k+1}-4)2^{-2k}=1-2^{2-k}+2^{1-k}=1-2^{1-k}$.

*(5)* Immediate from (2)+(3): when $D\ge2$ the degree is $D+k-1>k$ and only
even $T$ with $|T|=k-1$ paired with $|S|=D$, $\hat g(S)\ne0$, attain it; when
$D=1$ the degree is $k$ and the block $[k]$ (odd) also attains it.

*(6)* By (4) and $\alpha=\beta=\frac12$,
$\pi=2\bigl[\sum_{i\in V}\mathrm{Inf}_i(\mathbf 1_{\mathsf A})+\sum_{i\in V}\mathrm{Inf}_i(\mathbf 1_{\mathsf A})\bigr]
=4\bigl[(k-1)2^{-k-1}+Q_k\sum_{j\in S}\mathrm{Inf}_j(g)\bigr]$, which is the
displayed value. $\square$

**Corollary T4′ (the mechanism, isolated).** On $\mathsf H(k,g,\Delta)$ the
maximum-degree-window payment is $(k-1)2^{1-k}$ plus (essentially) *the
influence that $g$ places on one of its own maximum-degree characters*. The
degree budget of the pair is spent almost entirely on the block, each of whose
coordinates carries only the L2 quantum $2^{-k-1}$; all remaining influence
sits on the spectators, which the block window misses. For $\mathsf H_d$
($k=d$, $D=1$, $g$ a dictator) this is T3's $d2^{1-d}$ on $V=[d]$ and
$1+(d-2)2^{1-d}$ on $V=U'$, matching the machine check of u2 exactly.

---

## T5 — the repaired key step

### T5(a) The hub-completed window functional, and the reduction it feeds

**Definition.** For $\tau\in(0,1]$ and $f=f_A\in\mathcal C^{\mathrm{ind}}_d$
fix any maximum-degree monomial support $S_f$ of $\mathbf 1_A$ and set
$$W_\tau(f)\ :=\ S_f\ \cup\ H_\tau(f),\qquad H_\tau(f):=\{i\in[N]:\mathrm{Inf}_i(f)\ge\tau\}.$$
This depends on $f$ alone (as T1/L5 require).

**Size bound (PROVED-INLINE).** $|S_f|\le d$ and, since $f$ has unit norm and
degree $\le d$,
$\sum_i\mathrm{Inf}_i(f)=\sum_S|S|\hat f(S)^2\le d\sum_S\hat f(S)^2=d$
(I02's free budget), so $|H_\tau(f)|\le d/\tau$ and
$$|W_\tau(f)|\ \le\ d\Bigl(1+\frac1\tau\Bigr)=:\omega_\tau(d).$$
With $\tau=1/4$: $\omega(d)=5d$. With $\tau=1/(2d)$: $\omega(d)=d+2d^2$.

**(PAY★★).** *There are $\tau(d)\ge1/\mathrm{poly}(d)$ and
$p(d)\ge1/\mathrm{poly}(d)$ such that for every $d,N$, every cross-disjoint
pair $A,B$ of nonempty degree-$\le d$ sets, and every choice of maximum-degree
supports used in $W_\tau$,*
$$\sum_{i\in W_\tau(f_B)}\mathrm{Inf}_i(f_A)+\sum_{i\in W_\tau(f_A)}\mathrm{Inf}_i(f_B)\ \ge\ p(d).$$

**Status: OPEN.** By T1 (with $\omega=\omega_\tau$),
$$\textbf{(PAY}\star\star\textbf{)}\ \Longrightarrow\ \text{R2 with }\delta(d)=\tfrac12\,p(d)/\omega_\tau(d)\ \ge\ 1/\mathrm{poly}(d),$$
so (PAY★★) is a *sufficient* repaired key step for plan P1: it would settle
R2. It is stated here as the corrected target, **not** as a claim.

### T5(b) (PAY★★) verified on every extremal family on the campaign's record

All four rows are re-derived here; none is inherited from `0023-refuter-3` or
from the strategist's table. Throughout $\tau=1/4$.

| family | windows $W_{1/4}$ | payment $\pi$ |
|---|---|---|
| **grid** (R1 extremal): $A_r=\{x:x_{r,j}=-1\ \forall j\}$, $B_c=\{x:x_{i,c}=+1\ \forall i\}$ on $[d]\times[d]$ | row $r$; column $c$ | **exactly $1$** |
| **codim-$d$ subcube pair** (killer (b)'s witness): $C=\{x:x_1=\dots=x_d=1\}$, $C^c$ | $[d]$; $[d]$ | $\ \ge d/2$ |
| **address pair** (killer (a)'s witness): $\mathsf{Ad}=\{(a,y):y_a=+1\}$, $\mathsf{Ad}^c$, $d=k+1$ | $\{a_1..a_k,y_j\}$; $\{a_1..a_k,y_{j'}\}$ | $k/2+2^{-k}$ |
| **$\mathsf H_d$** (u2, the new obstruction) | $S\cup\{w\}$ on both sides | $\ \ge1-2^{1-d}\ \ge\tfrac12$ |

*Derivations.* **Grid:** $\mathbf 1_{A_r}=\prod_j\frac{1-x_{rj}}2$ is a
codimension-$d$ subcube indicator, so its unique maximum-degree support is
row $r$; all its coefficients are $\pm2^{-d}$ and each row coordinate lies in
$2^{d-1}$ of them, so $\mathrm{Inf}_i(\mathbf 1_{A_r})=2^{-d-1}$ and
$\mathrm{Inf}_i(f_{A_r})=2^{-d-1}/2^{-d}=\frac12\ge\tau$ for $i$ in row $r$,
$0$ elsewhere; hence $H_\tau=$ row $r$ and $W_\tau(f_{A_r})=$ row $r$.
Symmetrically for $B_c$. Row $r$ and column $c$ meet exactly in the cell
$(r,c)$, so $\pi=\frac12+\frac12=1$. (Disjointness: a point of $A_r\cap B_c$
would need $x_{rc}=-1$ and $x_{rc}=+1$.) **Subcube pair:**
$\mathrm{Inf}_i(f_C)=\frac12$ and
$\mathrm{Inf}_i(f_{C^c})=2^{-d-1}/(1-2^{-d})$ for $i\in[d]$; both
maximum-degree supports are $[d]$ (for $C^c$ because
$\mathbf 1_{C^c}=1-\mathbf 1_C$), so
$\pi=d\bigl[\frac12+\frac{2^{-d-1}}{1-2^{-d}}\bigr]\ge d/2$. **Address pair:**
$\mathbf 1_{\mathsf{Ad}}=\frac12+\frac12\sum_j\mathbf 1[a=j]y_j$, whose
monomials are $u^T y_j$ ($T\subseteq[k]$) with coefficients $\pm2^{-k-1}$;
degree $k+1=d$; $\alpha=\frac12$; each address coordinate lies in
$2^k\cdot2^{k-1}$ monomials so $\mathrm{Inf}_{a_i}(\mathbf 1)=2^{2k-1}2^{-2k-2}=\frac18$,
i.e. $\mathrm{Inf}_{a_i}(f)=\frac14\ge\tau$, and
$\mathrm{Inf}_{y_j}(f)=2\cdot2^k2^{-2k-2}=2^{-k-1}$. Maximum-degree supports
are $\{a_1..a_k,y_j\}$; $H_\tau=\{a_1,\dots,a_k\}$, so
$W_\tau=\{a_1..a_k,y_j\}$ and $\pi=2\bigl[k\cdot\frac14+2^{-k-1}\bigr]=k/2+2^{-k}$.
**$\mathsf H_d$:** by u2/L6, $\mathrm{Inf}_w(f_{\mathsf A_d})=2Q_d=\frac{1-2^{1-d}}2\ge\frac14=\tau$
for $d\ge2$, so $w\in H_\tau$ on both sides and
$\pi\ge2\bigl[\mathrm{Inf}_w(\mathbf 1_{\mathsf A})+\mathrm{Inf}_w(\mathbf 1_{\mathsf A})\bigr]\cdot 1=4Q_d=1-2^{1-d}$.

So the heavy completion repairs precisely the defect T3 exhibits, and the
maximum-degree support repairs precisely the defect that would sink a
heavy-only functional (the subcube pair, whose complement side has **no**
$\tau$-heavy coordinate at all for $\tau>2^{-d-1}$ — that is refuter-3's
killer (b) seen from this side). Neither half alone survives; the union
survives all four.

### T5(c) Exactly what would refute (PAY★★): a single-function dilution question

**Statement (conditional refutation). PROVED-INLINE.** Let $c>0$ and suppose
that for infinitely many $D$ there exists a balanced
$g:\{\pm1\}^{m}\to\{\pm1\}$ with $\deg g=D$ and
$$\mu(g):=\max_j\mathrm{Inf}_j(g)\ \le\ 2^{-cD}.$$
Then (PAY★★) is false at every inverse-polynomial $p$, for every
$\tau\ge1/\mathrm{poly}(d)$.

**Proof.** Fix such a $D\ge2$, put $k:=\max(2,\lceil cD\rceil)$ and
$d:=k+D-1$ (so $2\le k\le d$, $D=d-k+1$, $d\le(1+c)D+1$, hence
$D\ge(d-1)/(1+c)$), and
take the pair $\mathsf H(k,g,\Delta)$ of T4 with $\Delta=\{1\}$; by T4(3) it lies in
$\mathcal C^{\mathrm{ind}}_d$ and by T4(1) it is cross-disjoint. By T4(4) all
influences of $f_{\mathsf A}$ are at most
$\max\bigl(2\cdot2^{-k-1},\,2Q_k\mu(g)\bigr)\le\max(2^{-k},\mu(g)/2)$, which is
$<\tau$ for all large $d$ because $\tau\ge1/\mathrm{poly}(d)$ while
$2^{-k}$ and $2^{-cD}$ are $2^{-\Theta(d)}$. Hence
$H_\tau(f_{\mathsf A})=H_\tau(f_{\mathsf B})=\emptyset$ and $W_\tau$ reduces to
a maximum-degree monomial support on both sides — *whatever* the choice, since
by T4(5) every such support is of the form $T\cup S$ with $|S|=D$, and then
T4(6) gives
$$\pi=(k-1)2^{1-k}+(1-2^{1-k})\sum_{j\in S}\mathrm{Inf}_j(g)\ \le\ (k-1)2^{1-k}+D\,\mu(g)\ \le\ 3d\,2^{-cD}\ \le\ 3d\,2^{-c(d-1)/(1+c)},$$
using $k\ge cD$ (so $2^{1-k}\le2\cdot2^{-cD}$), $D\le d$ and
$D\ge(d-1)/(1+c)$; this is $2^{-\Theta(d)}$.
As this holds for infinitely many $d$, no inverse-polynomial $p$ survives.
$\square$

**T5(c′) The converse: (PAY★★) implies the single-function bound.
PROVED-INLINE.** *If (PAY★★) holds with $\tau(d),p(d)\ge c_1d^{-c_2}$, then
every balanced $g:\{\pm1\}^m\to\{\pm1\}$ of degree $D$ has
$\mu(g)\ge1/\mathrm{poly}(D)$.*

**Proof.** $D=1$: a balanced $\pm1$-valued degree-$1$ function is $\pm x_j$, so
$\mu(g)=1$. Let $D\ge2$, put $k:=\lceil C\log_2(D+2)\rceil$ with
$C=C(c_1,c_2)$ large and $d:=k+D-1$; then $k\ge2$, $d\le2D$ for large $D$, and
$2^{-k}\le\min(\tau(d),p(d)/(4d))$ since $2^{-k}\le(D+2)^{-C}$ while
$\tau(d),p(d)/(4d)\ge c_1(2D)^{-c_2-1}/4$. Apply (PAY★★) to
$\mathsf H(k,g,\{1\})\in\mathcal C^{\mathrm{ind}}_d$ (T4(3)); by T4(4) both
sides have the same influence profile, $2^{-k}$ on block coordinates and
$2Q_k\mathrm{Inf}_j(g)\le\mathrm{Inf}_j(g)/2$ on spectators. If some coordinate
is $\tau(d)$-heavy it is a spectator $j$ (block coordinates carry
$2^{-k}<\tau$), so $\mathrm{Inf}_j(g)\ge2\tau(d)$ and
$\mu(g)\ge2\tau(d)\ge1/\mathrm{poly}(D)$. Otherwise $H_\tau=\emptyset$ on both
sides, $W_\tau$ is a maximum-degree support $T\cup S$ with $|S|=D$ (T4(5)), and
T4(6) with (PAY★★) gives
$p(d)\le(k-1)2^{1-k}+D\mu(g)\le p(d)/2+D\mu(g)$, so
$\mu(g)\ge p(d)/(2D)\ge1/\mathrm{poly}(D)$. $\square$

**The near-dichotomy this produces (the unit's main structural finding).** On
the shape $\mathsf H(k,g,\Delta)$ the payment is governed by
$\mu(g)=\max_j\mathrm{Inf}_j(g)$:

* if $\mu(g)\ge4\tau$ then the heaviest coordinate $j^\ast$ of $g$ lies in
  $H_\tau(f_{\mathsf A})\cap H_\tau(f_{\mathsf B})$ (T4(4):
  $\mathrm{Inf}_{j^\ast}(f_{\mathsf A})=2Q_k\mu(g)=\frac{1-2^{1-k}}2\mu(g)\ge\frac{\mu(g)}4\ge\tau$
  for $k\ge2$), so $\pi\ge2\tau$;
* if all coordinates are $\tau$-light then $\pi\le(k-1)2^{1-k}+D\mu(g)$, which
  is below every inverse polynomial when $\mu(g)=2^{-\Theta(D)}$ (the
  conditional refutation above).

Combined with T5(c′): **(PAY★★) holds only if every balanced degree-$D$ Boolean
function has a coordinate of influence $\ge1/\mathrm{poly}(D)$, and fails
outright if balanced degree-$D$ Boolean functions with all influences
$2^{-\Theta(D)}$ exist.** So **the rung's difficulty on this route is a
single-function question, not a two-family one**: *does every balanced
degree-$D$ Boolean function have a coordinate of influence
$\ge1/\mathrm{poly}(D)$?* Two remarks fixing its status
in this campaign, neither of them used inside any proof above:

* **The required dilution is extremal, not comfortable.** For balanced
  $\pm1$-valued $g$, $1=\mathrm{Var}(g)=\sum_{S\ne\emptyset}\hat g(S)^2\le
  \sum_S|S|\hat g(S)^2=\sum_j\mathrm{Inf}_j(g)$ (Poincaré, one line), while
  card **S6c** [READ] (Wellens, Discrete Analysis 2022:19, Thm 1.1 (1.3))
  bounds the number of relevant variables of a degree-$D$ Boolean function by
  $4.394\cdot2^{D}$. Hence $\mu(g)\ge1/(4.394\cdot2^{D})$ always: the object
  the conditional refutation needs must be within a constant factor of the
  junta bound's extreme. Card S6a's engine ($\mathrm{Inf}_j\ge2^{1-D}$ per
  relevant coordinate, reproved here as L2's $\pm1$ analogue) says the same
  from below.
* **The other direction is [SOURCE-BLOCKED], and I do not use it.** A printed
  $\mu(g)\ge\mathrm{Var}(g)/\mathrm{poly}(D)$ would remove this refutation
  shape; the only route the campaign has identified is OSSS + a
  depth-vs-degree bound, both currently **unread** (strategist §6.4's [MEMORY]
  register and its rank-1/rank-2 source requests). I therefore mark the status
  of (PAY★★) as **OPEN, not conditional**: I am *not* assuming the unread
  statement, and even granting it, it would only close *this* family shape and
  would **not** prove (PAY★★) — other shapes are unconstrained by it.

### T5(d) Two further honest limits of this unit

* **The fibre route is not crossed.** The strategist's V5/G2 identity is
  correct — for $i\in W$ and $W$-fibres $A_w$,
  $\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E_w[\mathrm{Inf}^{(w)}_i(\mathbf 1_{A_w})]$,
  because $\mathrm{Inf}_i(\mathbf 1_A)=\frac14\Pr_x[\mathbf 1_A(x)\ne\mathbf 1_A(x^{\oplus i})]$
  (L2's computation) and flipping $i\in W$ preserves the fibre. But the crudest
  fibre-wise isoperimetric bound
  $\sum_{i\in W}\mathrm{Inf}^{(w)}_i(\mathbf 1_{A_w})\ge\alpha_w(1-\alpha_w)$
  assembles only to $\mathbb E_w[\alpha_w\beta_w](\frac1\alpha+\frac1\beta)$,
  which on $\mathsf H_d$ with $W=U$ equals
  $4(1-2^{-d})2^{-d}=\Theta(2^{-d})$ (the two $w$-fibres have
  $\alpha_w\in\{1-2^{-d},2^{-d}\}$) — consistent with T3 and with the strategist's warning that
  FIBRE-BALANCE has an exponential floor. **I claim nothing that needs it, and
  I mark no gap: the route is simply not used.**
* **No claim of optimality for $W_\tau$.** T5(b) shows $W_\tau$ survives every
  extremal on record; T5(c) shows what would kill it. Nothing here shows that
  some *other* poly$(d)$ window functional could not do better, nor that
  $W_\tau$ works.

EMITTED unit 3 of 5; NEXT UNIT: u4 = type-checked Lean skeleton of the
definitions and of L4, L5, T1; ARTIFACT 0023-prover-2.

### END OF ARTIFACT 0023-prover-2-u3 ###
