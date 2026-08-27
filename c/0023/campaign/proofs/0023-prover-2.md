---
id: 0023-prover-2
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: PARTIAL
---

# 0023-prover-2 — plan P1 (class (a) REDUCTION) on rung R2 / intermediate I02

## VERDICT — **PARTIAL** (with one PLAN-STEP REFUTED)

1. **PROVED, unconditionally:** the corrected master count with
   pair-independent windows (L5); the two-family positivity lemma
   (L4 = the strategist's G1); the reduction **(PAY★$_\mathcal W$) ⟹ R2** with
   $\delta(d)=\theta\,p(d)/(2\omega(d))$ (T1); and the unconditional threshold
   **R2 holds for every $\delta(d)<2^{-d}/d$** (T2). *T2's threshold is
   exponential in $d$, so by I02's own rule this is a PARTIAL and settles
   nothing on this rung: R2's content window $[2^{-d}/d,\,1/(2d))$ is
   untouched.* Its value is that it re-derives card S1's K1 threshold exactly,
   for $\mathcal C^{\mathrm{ind}}_d$, by an independent route whose only
   $d$-dependence in the count is $|W|\le d$ (no junta size anywhere).
2. **REFUTED:** plan P1's key step **(PAY★) as stated** (`0023-strategist-2`
   V3: quantified over *every* choice of maximum-degree monomial supports, or
   over all shattering windows) is **false, exponentially**. Explicit family
   $(\mathsf A_d,\mathsf B_d)$ on $d+1$ coordinates with payment exactly
   $d\,2^{1-d}$; hand proof plus an exact-arithmetic machine certificate for
   $d=2..12$. The advertised constant $p=1$ already fails at $d=3$
   ($\pi=3/4$). This is a **third obstruction**, independent of both certified
   killers of `0023-refuter-3`.
3. **ISOLATED, OPEN:** the choice-map form the reduction actually consumes
   survives. I state the repaired key step (PAY★★) for the *hub-completed*
   window functional $W_\tau(f)=(\text{max-degree support})\cup\{i:\mathrm{Inf}_i(f)\ge\tau\}$
   of size $\le d(1+1/\tau)$, verify it (payment $\ge1/2$) on **all four**
   extremal families on the campaign's record including the new one, prove a
   conditional refutation identifying exactly one object that would kill it (a
   balanced degree-$D$ $\pm1$-valued function with all influences
   $\le2^{-cD}$), and prove the **converse (T5(c′))**: (PAY★★) *implies* that
   every balanced degree-$D$ Boolean function has a coordinate of influence
   $\ge1/\mathrm{poly}(D)$. So P1's repaired step is at least as hard as that
   single-function statement — which this campaign has **not** carded (it is
   plan P4's source gate). This is a hardness-of-technique result, and it
   relocates the rung's difficulty from two-family combinatorics to a
   single-function influence question.
4. **R2 is NOT proved and NOT refuted here.** No inverse-polynomial threshold
   is claimed. Nothing in this artifact refutes R2 (item 2's family violates
   R2's influence hypothesis by a wide margin — it is a counterexample to a
   technique, not to the rung).
5. **No load-bearing [SOURCE-BLOCKED] or [MEMORY] dependency.** The single
   external input is card **S7b** ([READ]); everything else is proved inline.

---

## 0. The target, the notation, and the definitions

**R2 (intermediate I02), the statement addressed.** There exist $c_1\in(0,1]$,
$c_2>0$ and $\delta:\mathbb N\to(0,1]$ with $\delta(d)\ge c_1d^{-c_2}$ such
that for all $d,N$ and all finitely supported distributions $\mathbf F,\mathbf
G$ over
$\mathcal C^{\mathrm{ind}}_d=\{\mathbf 1_A/\|\mathbf 1_A\|_2:\emptyset\ne
A\subseteq\{\pm1\}^N,\ \deg\mathbf 1_A\le d\}$
satisfying $\mathbb E_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb E_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]\le\delta(d)$ for every $i\in[N]$,
there are $f\in\mathrm{supp}\,\mathbf F$, $g\in\mathrm{supp}\,\mathbf G$ and
$x$ with $f(x)g(x)\ne0$. Equivalently, in combinatorial form: two families of
degree-$\le d$ sets that are pairwise disjoint across the two families cannot
both keep every per-coordinate average influence $\le\delta(d)$.

**Notation.** $\{\pm1\}^N$ carries the uniform measure. Every
$f:\{\pm1\}^N\to\mathbb R$ has a unique multilinear expansion
$f=\sum_{S\subseteq[N]}\hat f(S)x^S$, $x^S=\prod_{i\in S}x_i$, with the $x^S$
orthonormal; $\deg f=\max\{|S|:\hat f(S)\ne0\}$;
$\mathrm{Inf}_i(f)=\sum_{S\ni i}\hat f(S)^2$ (the Contract's definitions,
specialised to $\mathcal Y=\mathbb Z_2$). For $\emptyset\ne A$:
$\alpha=|A|/2^N$, $f_A=\mathbf 1_A/\sqrt\alpha$ (unit norm),
$\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha$, and
$$\mathrm{rel}(A):=\{i:\exists x,\ \mathbf 1_A(x)\ne\mathbf 1_A(x^{\oplus i})\}.$$
$x^{\oplus i}$ flips coordinate $i$. $\pi_T(A)$ is the projection of $A$ to the
coordinates in $T$.

**Definition 1 (shattering window).** For $\emptyset\ne A$ with
$\deg\mathbf 1_A\le d$,
$$\mathcal S_d(A):=\{W\subseteq[N]:|W|\le d,\ \pi_{[N]\setminus W}(A)=\{\pm1\}^{[N]\setminus W}\}.$$

**Definition 2 (payment).**
$$\pi\bigl((A,W_A),(B,W_B)\bigr):=\sum_{i\in W_B}\mathrm{Inf}_i(f_A)+\sum_{i\in W_A}\mathrm{Inf}_i(f_B).$$
A **sum over the two sides**, never a $\min$; each side charged on the
**partner's** window.

*Degenerate case $d=0$:* a degree-$0$ indicator of a nonempty set is $\equiv1$,
so $A=B=\{\pm1\}^N$ and R2's conclusion is immediate. All statements below take
$d\ge1$.

## 1. Method sketch

L1 (nonvanishing) $\to$ L2 (influence quantum) and L3 (card S7b window) $\to$
L4 (positivity: every shattering window of $A$ meets $\mathrm{rel}(B)$) $\to$
T2 (unconditional payment $\ge2^{1-d}$), which fed into L5 (master count) and
T1 (reduction) gives R2 at $\delta<2^{-d}/d$. Then T3: an explicit family whose
payment on a genuine maximum-degree window is $d2^{1-d}$, refuting (PAY★) as
stated. Then T4 (the two-parameter family behind it, exact spectrum) and T5
(the repaired functional, its verification on all extremals, and the exact
object that would refute it). No case split; the only branch is
all-windows (refuted) vs choice-map (open).

---

## 2. M1a: the unconditional reduction

### L1 (nonvanishing). PROVED-INLINE

*Let $p:\{\pm1\}^n\to\mathbb R$ be multilinear, $p\not\equiv0$, $\deg p\le k$.
Then $\Pr_x[p(x)\ne0]\ge2^{-k}$.*

**Proof.** Induction on $n$, for all $k$ simultaneously. $n=0$: $p$ is a
nonzero constant, probability $1$. $n\ge1$: write $p(x)=q(x')+x_nr(x')$ with
$x'=(x_1,\dots,x_{n-1})$, $q,r$ multilinear, $r=\frac12(p(\cdot,+1)-p(\cdot,-1))$.
If $r\equiv0$ then $p=q$ does not involve $x_n$, $q\not\equiv0$, $\deg q\le k$,
and the inductive hypothesis in $n-1$ variables applies. If $r\not\equiv0$,
then every monomial of $x_nr$ is a monomial of $p$, so $\deg r\le k-1$ (and
$k\ge1$); by induction $\Pr_{x'}[r(x')\ne0]\ge2^{1-k}$, and for each such $x'$,
$p(x',+1)-p(x',-1)=2r(x')\ne0$ forces one of the two values to be nonzero, so
$\Pr_{x_n}[p\ne0\mid x']\ge\frac12$. Multiply. $\square$

### L2 (influence quantum). PROVED-INLINE

*$\emptyset\ne A$, $\deg\mathbf 1_A\le d$, $i\in\mathrm{rel}(A)$ $\Rightarrow$
$\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-1-d}$, hence
$\mathrm{Inf}_i(f_A)\ge2^{-1-d}/\alpha$.*

**Proof.** Write $\mathbf 1_A=q+x_ir$ with $q,r$ free of $x_i$; then
$r=\frac12(\mathbf 1_A|_{x_i=+1}-\mathbf 1_A|_{x_i=-1})\in\{-\frac12,0,\frac12\}$
pointwise, and $r\not\equiv0$ iff $i\in\mathrm{rel}(A)$. Grouping the expansion,
$r=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)x^{S\setminus\{i\}}$, so by
orthonormality $\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E[r^2]=\frac14\Pr[r\ne0]$.
Since $\deg r\le d-1$, L1 gives $\Pr[r\ne0]\ge2^{1-d}$, so
$\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-1-d}$. Normalisation: $\mathrm{Inf}_i(cf)=c^2\mathrm{Inf}_i(f)$.
$\square$

*(The same computation for a $\pm1$-valued $g$ of degree $D$ gives
$\mathrm{Inf}_j(g)=\Pr[r\ne0]\ge2^{1-D}$ for relevant $j$; used in §4.)*

### L3 (windows exist). CARD S7b [READ], plus one inline closure step

*For $\emptyset\ne A$ with $\deg\mathbf 1_A\le d$: (1) $\mathcal S_d(A)\ne
\emptyset$; (2) every maximum-degree monomial support $S$ of $\mathbf 1_A$
(i.e. $\widehat{\mathbf 1_A}(S)\ne0$, $|S|=\deg\mathbf 1_A$) lies in
$\mathcal S_d(A)$; (3) $\mathcal S_d(A)$ is closed under enlargement up to
size $d$.*

**Provenance.** (1),(2): card **S7b**, item **T3.4** (Chang–Fang,
arXiv:2510.13705v3, Cor. 3.4, p. 7) with its item **T3.2** (Thm 3.2, p. 6,
first display), applied with $G_1=\dots=G_N=\mathbb Z_2$. Hypotheses checked
against the card: product of finite abelian groups ✔; $f=\mathbf 1_A$ non-zero
(as $A\ne\emptyset$) ✔; $\deg_{\hat G}$ is the Contract's degree — printed and
"identical, symbol for symbol" (card flag 3), and over $\mathbb Z_2$ a
character non-trivial exactly on $S$ is the monomial $x^S$ ✔; the conclusion
$\dim_\pi(\mathrm{supp}f)+\deg_{\hat G}(f)\ge N$ unfolds *definitionally*
(card flag 4) to: some $T$ with $|T|\ge N-d$ has $\pi_T(A)=\{\pm1\}^T$; put
$W=[N]\setminus T$ ✔; for (2), card flag 4's last sentence records the
fibre-wise form of T3.2 for $S$ **any** maximum-degree character support ✔;
uniform in $N$ ✔.
**Proof of (3).** $\pi_{[N]\setminus W'}$ factors through
$\pi_{[N]\setminus W}$ when $W\subseteq W'$, and a composition of surjections
onto the stated codomains is surjective. $\square$

**Not used anywhere in this artifact:** the density consequence
$\alpha\ge2^{-d}$ of the same card (capped at K1's scale). *S7b usage
declaration: **WINDOW only**.*

### L4 = G1 (positivity). PROVED-INLINE — new

*Let $A,B$ be nonempty and disjoint and $W\in\mathcal S_d(A)$. Then
$W\cap\mathrm{rel}(B)\ne\emptyset$.* (No degree hypothesis on $B$ is used.)

**Proof.** Suppose $W\cap\mathrm{rel}(B)=\emptyset$; fix $b\in B$. By
surjectivity there is $a\in A$ with $a|_{[N]\setminus W}=b|_{[N]\setminus W}$.
Let $i_1,\dots,i_m\in W$ be the coordinates where $a,b$ differ, and
$b^{(0)}=b$, $b^{(t)}=(b^{(t-1)})^{\oplus i_t}$, so $b^{(m)}=a$. Each $i_t\in
W$ is not in $\mathrm{rel}(B)$, i.e. $\mathbf 1_B(y)=\mathbf 1_B(y^{\oplus
i_t})$ for **all** $y$; applying this at $y=b^{(t-1)}$ and inducting on $t$
gives $\mathbf 1_B(a)=\mathbf 1_B(b)=1$. So $a\in A\cap B$ — contradiction.
$\square$

**Remarks.** (i) $m=0$ (i.e. $a=b$) is included; in particular $W=\emptyset$ is
impossible for a cross-disjoint pair. (ii) This is strictly stronger than the
cylinder-based projection step of the frozen R1 proof and is the **first
two-family consequence of Chang–Fang** on record: cards S7 and S7b certify,
over the paper's complete text, that the source contains no two-function
statement, so the combination with disjointness is new and is proved, not
cited. (iii) It is *not* R1's projection-disjointness: nothing is claimed
about $\pi_S(A),\pi_S(B)$ being disjoint (for general degree-$\le d$ sets they
typically both fill $\{\pm1\}^S$).

### L5 (master count, pair-independent windows). PROVED-INLINE

*Let $\mathbf F,\mathbf G$ be finitely supported distributions over
$\mathcal C^{\mathrm{ind}}_d$, $\delta_{\mathbf F}=\max_i\mathbb
E_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]$, $\delta_{\mathbf G}$ likewise. Let
$W(\cdot)$ assign to each function in the two supports a set $W(\cdot)\subseteq
[N]$ **depending on that function alone**, and draw $f\sim\mathbf F$,
$g\sim\mathbf G$ independently. Then*
$$\mathbb E_{f,g}\bigl[\pi(f,g)\bigr]\le\delta_{\mathbf F}\mathbb E_g|W(g)|+\delta_{\mathbf G}\mathbb E_f|W(f)|\ \le\ (\delta_{\mathbf F}+\delta_{\mathbf G})\,\omega\quad\text{if }|W(\cdot)|\le\omega .$$

**Proof.** All sums are finite, so
$$\mathbb E_{f,g}\Bigl[\sum_{i\in W(g)}\mathrm{Inf}_i(f)\Bigr]=\sum_{i=1}^N\mathbb E_{f,g}\bigl[\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)\bigr]=\sum_{i=1}^N\Pr_g[i\in W(g)]\,\mathbb E_f[\mathrm{Inf}_i(f)],$$
by independence — this is where $W(g)$ must not depend on $f$. Bound
$\mathbb E_f[\mathrm{Inf}_i(f)]\le\delta_{\mathbf F}$ (the weights
$\Pr_g[i\in W(g)]$ are nonnegative) and use
$\sum_i\Pr_g[i\in W(g)]=\mathbb E_g|W(g)|$. The other term is symmetric.
$\square$

**Two drafting rules, verified.** Charging a side on its *own* window loses the
$\delta$ factor (one gets only $\sum_{i\in W(f)}\mathrm{Inf}_i(f)\le d$ and the
count degenerates); and a pair-dependent $W$ breaks the factorisation. The
latter is card S7's non-canonicity obstacle in its only load-bearing form.

### T1 (the reduction). PROVED-INLINE

*Let $\omega(d)\ge1$, $p(d)>0$. Suppose for every $d\ge1,N\ge1$ there is a map
$W$ assigning to each $f\in\mathcal C^{\mathrm{ind}}_d$ on $\{\pm1\}^N$ a
window $W(f)$ with $|W(f)|\le\omega(d)$ such that*
$$\textbf{(PAY}\star_{\mathcal W}\textbf{)}\qquad\sum_{i\in W(f_B)}\mathrm{Inf}_i(f_A)+\sum_{i\in W(f_A)}\mathrm{Inf}_i(f_B)\ \ge\ p(d)$$
*for every pair of nonempty disjoint $A,B$ with $\deg\mathbf 1_A,\deg\mathbf
1_B\le d$. Then R2 holds with any $\delta:\mathbb N\to(0,1]$ satisfying
$\delta(d)<p(d)/(2\omega(d))$; in particular $\delta$ is inverse-polynomial as
soon as $p\ge1/\mathrm{poly}$ and $\omega\le\mathrm{poly}$.*

**Proof.** Fix $d,N,\mathbf F,\mathbf G$ satisfying R2's hypotheses at
$\delta(d)$ and suppose they are incompatible. Each $f\in\mathcal
C^{\mathrm{ind}}_d$ equals $\mathbf 1_A/\sqrt\alpha$ for the unique nonempty
$A=\{x:f(x)\ne0\}$ with $\deg\mathbf 1_A\le d$, and $f(x)g(x)\ne0\iff x\in
A\cap B$; so incompatibility says exactly that $A\cap B=\emptyset$ for every
pair in $\mathrm{supp}\,\mathbf F\times\mathrm{supp}\,\mathbf G$. Hence
$\pi\ge p(d)$ pointwise and $\mathbb E[\pi]\ge p(d)$, while L5 gives
$\mathbb E[\pi]\le2\delta(d)\omega(d)<p(d)$. Contradiction; so the pair is
compatible. $\square$

### T2 (unconditional payment and threshold). PROVED-INLINE

*(a) For every $d\ge1$, every cross-disjoint pair of nonempty degree-$\le d$
sets, and **every** $W_A\in\mathcal S_d(A)$, $W_B\in\mathcal S_d(B)$,*
$$\pi\ \ge\ 2^{-1-d}\Bigl(\frac1\alpha+\frac1\beta\Bigr)\ \ge\ 2^{1-d}.$$
*(b) R2 holds with every $\delta:\mathbb N\to(0,1]$ such that
$\delta(d)<2^{-d}/d$ for all $d\ge1$.*

**Proof of (a).** L4 applied to $W_A$ gives $i\in W_A\cap\mathrm{rel}(B)$;
applied with the roles of $A,B$ exchanged and the window $W_B\in\mathcal
S_d(B)$ it gives $j\in W_B\cap\mathrm{rel}(A)$. All summands of $\pi$ are
nonnegative, so $\pi\ge\mathrm{Inf}_j(f_A)+\mathrm{Inf}_i(f_B)\ge2^{-1-d}(\frac1\alpha+\frac1\beta)$
by L2. Disjointness gives $\alpha+\beta\le1$, and AM–HM gives
$\frac1\alpha+\frac1\beta\ge\frac4{\alpha+\beta}\ge4$. $\square$

**Proof of (b).** For each $d,N$ choose (finitely many choices from nonempty
finite collections; no choice axiom) some $W(f)\in\mathcal S_d(A)$ for each
$f=f_A\in\mathcal C^{\mathrm{ind}}_d$; then $|W(f)|\le d$ and (a) supplies
(PAY★$_\mathcal W$) with $p(d)=2^{1-d}$. T1 gives R2 for every
$\delta(d)<2^{1-d}/(2d)=2^{-d}/d$. $\square$

### Declarations (I02's trap clause)

* **T2(b) is a PARTIAL, not a proof of R2**: its threshold degrades
  exponentially in $d$. R2's content window $[2^{-d}/d,\,1/(2d))$ is untouched.
* **The exponential is not the junta size.** No step uses cards S6b–S6d; the
  window is $\le d$ *by theorem*. It is the influence **quantum** $2^{-1-d}$
  of L2, which card S6a certifies is attained (codimension-$d$ subcubes) and
  unimprovable. So T2 is exactly the reach of *positivity alone*.
* **Relation to K1 (card S1, ACC22 Thm 4.4).** K1 gives every
  $\delta<2^{-d}/d$ for every finite abelian group; T2(b) reproduces that
  threshold exactly for $\mathcal C^{\mathrm{ind}}_d$ over $\mathbb Z_2$ by an
  independent route (no per-character mass accounting).

---

## 3. T3: (PAY★) as stated is FALSE, exponentially

**Definition ($\mathsf H_d$).** For $d\ge2$ put $N=d+1$ and write points as
$(u,w)$, $u\in\{\pm1\}^d$ (**block**, coordinates $u_1..u_d$), $w\in\{\pm1\}$
(**hub**). Let $p=(+1,\dots,+1)$ and $q=(-1,+1,\dots,+1)$ in $\{\pm1\}^d$
(differing exactly in $u_1$). Put
$$\mathsf A_d:=\{(u,w):w=+1,u\ne p\}\cup\{(u,w):w=-1,u=q\},\qquad \mathsf B_d:=\mathsf A_d^{\,c}.$$

### L6 (exact spectrum). PROVED-INLINE

*With $U=\{u_1..u_d\}$ and $U'=\{u_2,\dots,u_d,w\}$:*
$$\mathbf 1_{\mathsf A_d}=\tfrac{1+w}2-2^{-d}\!\!\sum_{T\subseteq U,\ u_1\in T}\!\!u^T\ -\ 2^{-d}\,w\!\!\sum_{T\subseteq U\setminus\{u_1\}}\!\!u^T,$$
*so the nonzero coefficients are $\frac12$ at $\emptyset$; $\frac12-2^{-d}$ at
$\{w\}$; $-2^{-d}$ at each $T\ni u_1$; $-2^{-d}$ at each $T\cup\{w\}$,
$\emptyset\ne T\subseteq U\setminus\{u_1\}$. Consequently:
(1) $\deg\mathbf 1_{\mathsf A_d}=\deg\mathbf 1_{\mathsf B_d}=d$, so both
normalisations lie in $\mathcal C^{\mathrm{ind}}_d$;
(2) $\alpha=\beta=\frac12$;
(3) $\mathrm{Inf}_{u_i}(\mathbf 1_{\mathsf A_d})=2^{-d-1}$ for all $i\in[d]$ and
$\mathrm{Inf}_w(\mathbf 1_{\mathsf A_d})=(\frac12-2^{-d})^2+(2^{d-1}-1)2^{-2d}$,
with the same values for $\mathbf 1_{\mathsf B_d}$;
(4) $U$ and $U'$ are maximum-degree monomial supports of both indicators,
hence (L3(2)) lie in $\mathcal S_d(\mathsf A_d)\cap\mathcal S_d(\mathsf B_d)$.*

**Proof.** With $h=\frac{1+w}2$,
$\mathbf 1_{\mathsf A}=h(1-\mathbf 1_p)+(1-h)\mathbf 1_q
=h+2^{-d}\sum_{T\subseteq U}u^T[(1-h)\varepsilon^T-h]$ where
$\mathbf 1_p=2^{-d}\sum_Tu^T$, $\mathbf 1_q=2^{-d}\sum_T\varepsilon^Tu^T$ and
$\varepsilon^T=(-1)^{\mathbf 1\{u_1\in T\}}$. If $u_1\in T$ the bracket is
$-(1-h)-h=-1$; else it is $(1-h)-h=1-2h=-w$. Substituting $h=\frac{1+w}2$ and
separating the (even) $T=\emptyset$ term gives the display; the listed
monomials are pairwise distinct, so the coefficients are exact, and
$\frac12-2^{-d}\ne0$ for $d\ge2$.
(1) Degrees present: $|T|\le d$ with $T=U\ni u_1$ attaining $d$; and
$|T|+1\le d$ for $T\subseteq U\setminus\{u_1\}$. $\mathbf 1_{\mathsf B}=1-\mathbf
1_{\mathsf A}$ has the same coefficients off $\emptyset$ up to sign.
(2) $\alpha$ is the constant coefficient.
(3) Every monomial containing $u_i$ has coefficient $\pm2^{-d}$; the count is
$2^{d-1}$ in both cases ($i=1$: the $T\ni u_1$ with $T\ni u_i$, i.e.
$2^{d-1}$; $i\ge2$: $2^{d-2}$ of the first kind plus $2^{d-2}$ of the second),
so $\mathrm{Inf}_{u_i}=2^{d-1}2^{-2d}=2^{-d-1}$. For $w$: the monomial $\{w\}$
plus the $2^{d-1}-1$ monomials $T\cup\{w\}$.
(4) $|U|=|U'|=d=\deg$ and the coefficients at $u^U$ and at
$u^{U\setminus\{u_1\}}w$ are $\mp2^{-d}\ne0$. $\square$

*(Direct check of shattering, independent of L3(2): off $U$ only $w$ remains
and both signs occur in each set; off $U'$ only $u_1$ remains and both signs
occur in each set.)*

### T3 (the certificate). PROVED-INLINE + machine-checked

*For every $d\ge2$, $(\mathsf A_d,\mathsf B_d)$ is a cross-disjoint pair in
$\mathcal C^{\mathrm{ind}}_d$ and, for the maximum-degree monomial supports
$W_{\mathsf A}=W_{\mathsf B}=U$,*
$$\pi\bigl((\mathsf A_d,U),(\mathsf B_d,U)\bigr)=d\,2^{1-d}.$$

**Proof.** By L6(2),(3),
$\pi=\frac1\alpha\sum_{i\in U}\mathrm{Inf}_i(\mathbf 1_{\mathsf A})+\frac1\beta\sum_{i\in U}\mathrm{Inf}_i(\mathbf 1_{\mathsf B})=2\cdot d2^{-d-1}+2\cdot d2^{-d-1}=d2^{1-d}$.
$\square$

**Consequences.** (i) (PAY★) of `0023-strategist-2` V3 — quantified over every
choice of maximum-degree monomial supports — is false at every
inverse-polynomial $p$, with exponential decay $d2^{1-d}$. (ii) The same
refutes the version quantified over all *shattering* windows (L6(4)).
(iii) $p=1$ fails from $d=3$: values $1,\frac34,\frac12,\frac5{16},\frac3{16},
\frac7{64},\frac1{16},\frac9{256},\frac5{256},\frac{11}{1024},\frac3{512}$ for
$d=2..12$. At $d=2$ the value is exactly $1$, which is why the strategist's
$d\le2$ calibration (V4) did not see this.

**Machine confirmation (second, independent method).**
`proofs/0023-prover-2-code/check_family.py` builds the two sets from the set
definition (not from the expansion), computes coefficients by an integer
Walsh–Hadamard transform in exact `Fraction` arithmetic, and asserts for
$d=2..12$: degrees $=d$; $\alpha=\beta=\frac12$; all block influences
$=2^{-d-1}$; the hub influence; that $U,U'$ are maximum-degree supports of both
sides; that both sets surject off $U$ and off $U'$ (enumerated); and
$\pi(U,U)=d2^{1-d}$, $\pi(U',U')=1+(d-2)2^{1-d}$. All assertions pass; no
floating point enters any assertion.

**What T3 does NOT do.** It does **not** refute R2:
$\mathrm{Inf}_w(f_{\mathsf A_d})=2\bigl[(\frac12-2^{-d})^2+(2^{d-1}-1)2^{-2d}\bigr]
=\frac{1-2^{1-d}}2\to\frac12$, so this singleton-supported pair violates R2's
influence hypothesis at every inverse-polynomial $\delta$. It is a
counterexample to a *technique*.

**Why it is a third, independent obstruction.** Its windows have size $d$, and
$\mathsf A_d$ has only $d+1$ relevant coordinates, so refuter-3's killer (a)
(payment denominated in the relevant-coordinate count, $2^{\Theta(d)}$) does
not apply; and no $\min$ over the two sides occurs, so killer (b) does not
apply. The mechanism is new: the Chang–Fang window is a *degree* object and the
payment is an *influence* object, and cards S7/S7b certify that the source
couples them nowhere. In $\mathsf H_d$ all influence mass sits on the hub $w$,
which the maximum-degree support $U$ misses, while every coordinate of $U$
carries only the L2 quantum $2^{-d-1}$ — the minimum degree $d$ permits.

---

## 4. T4–T5: the anatomy, and the repaired key step

### T4 (the two-parameter family). PROVED-INLINE

**Definition ($\mathsf H(k,g,\Delta)$).** $k\ge2$, $m\ge1$, $N=k+m$; points
$(u,w)$ with $u\in\{\pm1\}^k$ (block), $w\in\{\pm1\}^m$ (spectators). Let
$g:\{\pm1\}^m\to\{\pm1\}$ be balanced ($\mathbb E g=0$) with $D=\deg g\ge1$;
let $p,q\in\{\pm1\}^k$ differ exactly on $\Delta$ with $|\Delta|$ odd; put
$h=\frac{1+g}2$ and $\mathbf 1_{\mathsf A}=h(1-\mathbf 1_p)+(1-h)\mathbf 1_q$,
$\mathsf B=\mathsf A^c$. ($\mathsf H_d=\mathsf H(d,w,\{1\})$.) Call
$T\subseteq[k]$ *even/odd* by the parity of $|T\cap\Delta|$; $\varepsilon^T=\prod_{i\in T}p_i$.

*Then: (1) $\mathsf A,\mathsf B$ are nonempty, disjoint, $\alpha=\beta=\frac12$;
(2) the nonzero coefficients of $\mathbf 1_{\mathsf A}$ are $\frac12$ at
$(\emptyset,\emptyset)$; $(\frac12-2^{-k})\hat g(S)$ at $(\emptyset,S)$,
$S\ne\emptyset$; $-2^{-k}\varepsilon^T$ at $(T,\emptyset)$, $T$ odd;
$-2^{-k}\varepsilon^T\hat g(S)$ at $(T,S)$, $\emptyset\ne T$ even,
$S\ne\emptyset$;
(3) $\deg\mathbf 1_{\mathsf A}=\deg\mathbf 1_{\mathsf B}=\max(k,D+k-1)$, so
both lie in $\mathcal C^{\mathrm{ind}}_d$ iff $k\le d$ and $D\le d-k+1$;
(4) $\mathrm{Inf}_{u_i}(\mathbf 1_{\mathsf A})=2^{-k-1}$ and
$\mathrm{Inf}_j(\mathbf 1_{\mathsf A})=Q_k\mathrm{Inf}_j(g)$ for spectators $j$,
where $Q_k=(\frac12-2^{-k})^2+(2^{k-1}-1)2^{-2k}$ satisfies $4Q_k=1-2^{1-k}$;
influences of $\mathbf 1_{\mathsf B}$ agree;
(5) for $D\ge2$ the maximum-degree monomial supports of both indicators are
exactly the $T\cup S$ with $T$ even, $|T|=k-1$, and $S$ a maximum-degree
character support of $g$; for $D=1$, these together with $[k]$;
(6) on every such window $V=T\cup S$,
$\pi=(k-1)2^{1-k}+(1-2^{1-k})\sum_{j\in S}\mathrm{Inf}_j(g)$.*

**Proof.** (1),(2): as in L6,
$\mathbf 1_{\mathsf A}=h+2^{-k}\sum_Tu^T[(1-h)\varepsilon^T(-1)^{|T\cap\Delta|}-h\varepsilon^T]$,
the bracket being $-\varepsilon^T$ for odd $T$ and $-\varepsilon^Tg$ for even
$T$; hence
$\mathbf 1_{\mathsf A}=\frac12+\frac g2-2^{-k}\sum_{\mathrm{odd}}\varepsilon^Tu^T-2^{-k}g\sum_{\mathrm{even}}\varepsilon^Tu^T$.
Expanding $g=\sum_S\hat g(S)\chi_S$: pure-spectator monomials get
$\frac{\hat g(S)}2-2^{-k}\hat g(S)$ (the $T=\emptyset$ term is even); at
$S=\emptyset$ this is $\frac12$ since $\hat g(\emptyset)=0$, giving
$\alpha=\frac12$; odd $T$ (nonempty) get $-2^{-k}\varepsilon^T$ at
$S=\emptyset$; nonempty even $T$ get $-2^{-k}\varepsilon^T\hat g(S)$, which
vanishes at $S=\emptyset$. The four index families are disjoint, so no
cancellation.
(3) Odd $T$ gives degree $|T|\le k$ with $T=[k]$ odd (as $|\Delta|$ is odd);
even $T$ with $|T|\le k-1$ (attained by $[k]\setminus\{i\}$, $i\in\Delta$)
gives $|T|+|S|\le k-1+D$; pure-spectator monomials give $\le D$.
(4) A block coordinate $u_i$ receives $2^{-2k}$ from each $T\ni i$ (odd $T$:
one monomial; even $T$: $2^{-2k}\sum_S\hat g(S)^2=2^{-2k}$ since $\mathbb
E[g^2]=1$), and $\#\{T\ni i\}=2^{k-1}$. A spectator $j$ receives
$[(\frac12-2^{-k})^2+(2^{k-1}-1)2^{-2k}]\mathrm{Inf}_j(g)$, using
$\#\{T\ \text{even}\}=2^{k-1}$ (bijection $T\mapsto T\triangle\{i_0\}$,
$i_0\in\Delta$). Then
$4Q_k=(1-2^{1-k})^2+(2^{k+1}-4)2^{-2k}=1-2^{2-k}+2^{1-k}=1-2^{1-k}$.
(5) Immediate from (2)+(3). (6) By (4) and $\alpha=\beta=\frac12$,
$\pi=4[(k-1)2^{-k-1}+Q_k\sum_{j\in S}\mathrm{Inf}_j(g)]$. $\square$

**Corollary (the mechanism).** On $\mathsf H(k,g,\Delta)$ the
maximum-degree-window payment is $(k-1)2^{1-k}$ plus, up to the factor
$1-2^{1-k}$, *the influence $g$ places on one of its own maximum-degree
characters*. For $\mathsf H_d$ ($k=d$, $g$ a dictator) this is $d2^{1-d}$ on
$[d]$ and $1+(d-2)2^{1-d}$ on $U'$ — both confirmed exactly by the machine
check.

### T5(a) The repaired functional and the repaired key step

For $\tau\in(0,1]$ and $f=f_A\in\mathcal C^{\mathrm{ind}}_d$ fix a
maximum-degree monomial support $S_f$ of $\mathbf 1_A$ and set
$$W_\tau(f):=S_f\cup H_\tau(f),\qquad H_\tau(f)=\{i:\mathrm{Inf}_i(f)\ge\tau\}.$$
It depends on $f$ alone, as T1/L5 require. Since
$\sum_i\mathrm{Inf}_i(f)=\sum_S|S|\hat f(S)^2\le d$ for unit-norm $f$ of degree
$\le d$ (I02's free budget), $|H_\tau(f)|\le d/\tau$ and
$$|W_\tau(f)|\ \le\ \omega_\tau(d):=d(1+1/\tau)\quad(=5d\ \text{at}\ \tau=\tfrac14).$$

> **(PAY★★) [OPEN].** *There are $\tau(d),p(d)\ge1/\mathrm{poly}(d)$ such that
> every cross-disjoint pair of nonempty degree-$\le d$ sets pays
> $\pi\ge p(d)$ on the windows $W_\tau$, for every admissible choice of the
> maximum-degree supports inside $W_\tau$.*

By T1, **(PAY★★) $\Rightarrow$ R2** with
$\delta(d)=\frac12p(d)/\omega_\tau(d)\ge1/\mathrm{poly}(d)$ — i.e. it would
settle the rung. It is stated as the corrected target, not claimed.

### T5(b) (PAY★★) verified on every extremal on record ($\tau=\frac14$)

| family | $W_{1/4}$ on the two sides | $\pi$ |
|---|---|---|
| **grid** (R1 extremal): $A_r=\{x:x_{r,j}=-1\,\forall j\}$, $B_c=\{x:x_{i,c}=+1\,\forall i\}$ on $[d]\times[d]$ | row $r$ ; column $c$ | **exactly 1** |
| **codim-$d$ subcube pair** (killer (b)'s witness) $C$, $C^c$ | $[d]$ ; $[d]$ | $\ge d/2$ |
| **address pair** (killer (a)'s witness) $\mathsf{Ad}=\{(a,y):y_a=+1\}$, $\mathsf{Ad}^c$, $d=k+1$ | $\{a_1..a_k,y_j\}$ ; $\{a_1..a_k,y_{j'}\}$ | $k/2+2^{-k}$ |
| **$\mathsf H_d$** (§3, the new obstruction) | $S\cup\{w\}$ on both sides | $\ge1-2^{1-d}\ge\frac12$ |

*Derivations (all inline; nothing inherited).* **Grid:**
$\mathbf 1_{A_r}=\prod_j\frac{1-x_{rj}}2$ is a codim-$d$ subcube indicator with
all coefficients $\pm2^{-d}$ and each row coordinate in $2^{d-1}$ of them, so
$\mathrm{Inf}_i(\mathbf 1_{A_r})=2^{-d-1}$, $\mathrm{Inf}_i(f_{A_r})=\frac12\ge\tau$
on row $r$ and $0$ elsewhere; its unique maximum-degree support is row $r$;
hence $W_\tau(f_{A_r})=$ row $r$ and symmetrically for $B_c$. Row $r$ meets
column $c$ exactly in cell $(r,c)$, so $\pi=\frac12+\frac12=1$. (Disjointness:
cell $(r,c)$ would have to be both $-1$ and $+1$.) **Subcube pair:**
$\mathrm{Inf}_i(f_C)=\frac12$, $\mathrm{Inf}_i(f_{C^c})=\frac{2^{-d-1}}{1-2^{-d}}$
for $i\in[d]$, and $[d]$ is the maximum-degree support of both (as
$\mathbf 1_{C^c}=1-\mathbf 1_C$), so
$\pi=d[\frac12+\frac{2^{-d-1}}{1-2^{-d}}]\ge d/2$. Note the complement side has
**no** $\tau$-heavy coordinate for $\tau>2^{-d-1}$: a heavy-only functional
would fail here, which is killer (b) seen from this side.
**Address pair:** $\mathbf 1_{\mathsf{Ad}}=\frac12+\frac12\sum_j\mathbf 1[a=j]y_j$
has monomials $u^Ty_j$ with coefficients $\pm2^{-k-1}$, degree $k+1=d$,
$\alpha=\frac12$; $\mathrm{Inf}_{a_i}(\mathbf 1)=2^{2k-1}2^{-2k-2}=\frac18$ so
$\mathrm{Inf}_{a_i}(f)=\frac14\ge\tau$, and
$\mathrm{Inf}_{y_j}(f)=2\cdot2^k2^{-2k-2}=2^{-k-1}$; maximum-degree supports are
$\{a_1..a_k,y_j\}$ and $H_\tau=\{a_1..a_k\}$, so
$\pi=2[k/4+2^{-k-1}]=k/2+2^{-k}$. **$\mathsf H_d$:** by L6,
$\mathrm{Inf}_w(f_{\mathsf A_d})=2Q_d=\frac{1-2^{1-d}}2\ge\frac14$ for $d\ge2$,
so $w\in H_\tau$ on both sides and $\pi\ge4Q_d=1-2^{1-d}$.

So the two halves of $W_\tau$ repair each other's failure: the heavy set
catches $\mathsf H_d$'s hub, the maximum-degree support catches the subcube
pair. Neither half alone survives all four.

### T5(c) Exactly what would refute (PAY★★). PROVED-INLINE (conditional)

*Let $c>0$ and suppose that for infinitely many $D$ there is a balanced
$g:\{\pm1\}^m\to\{\pm1\}$ with $\deg g=D$ and $\mu(g):=\max_j\mathrm{Inf}_j(g)\le2^{-cD}$.
Then (PAY★★) is false at every inverse-polynomial $p$, for every
$\tau\ge1/\mathrm{poly}(d)$.*

**Proof.** Given such a $D\ge2$, set $k:=\max(2,\lceil cD\rceil)$ and
$d:=k+D-1$ (so $2\le k\le d$, $D=d-k+1$, and $d\le(1+c)D+1$, whence
$D\ge(d-1)/(1+c)$ and $d\to\infty$ with $D$). Take $\mathsf
H(k,g,\Delta)$ with $\Delta=\{1\}$: by T4(3) it lies in $\mathcal
C^{\mathrm{ind}}_d$, by T4(1) it is cross-disjoint. By T4(4) every influence of
$f_{\mathsf A}$ (and of $f_{\mathsf B}$) is at most
$\max(2^{-k},\mu(g)/2)\le2^{-cD}$, which is $<\tau$ for large $D$ since
$\tau\ge1/\mathrm{poly}(d)$ and $d=O(D)$; so $H_\tau=\emptyset$ on both sides
and $W_\tau$ is a maximum-degree support — *whichever* one is chosen, since by
T4(5) (with $D\ge2$) all of them have the form $T\cup S$ with $|S|=D$. T4(6)
then gives
$$\pi=(k-1)2^{1-k}+(1-2^{1-k})\!\!\sum_{j\in S}\!\mathrm{Inf}_j(g)\ \le\ d\,2^{1-k}+D\mu(g)\ \le\ 3d\,2^{-cD}\ \le\ 3d\,2^{-c(d-1)/(1+c)},$$
which is $2^{-\Theta(d)}$, below every inverse polynomial for large $d$.
$\square$

**T5(c′) The converse implication: (PAY★★) is at least as hard as a
single-function question. PROVED-INLINE.** *Suppose (PAY★★) holds with
$\tau(d),p(d)\ge c_1d^{-c_2}$. Then every balanced $g:\{\pm1\}^m\to\{\pm1\}$
of degree $D$ satisfies $\mu(g)\ge1/\mathrm{poly}(D)$.*

**Proof.** For $D=1$ a balanced $\pm1$-valued degree-$1$ function is
$\pm x_j$, so $\mu(g)=1$. Let $D\ge2$. Choose $k=k(D):=\lceil C\log_2(D+2)\rceil$
with $C=C(c_1,c_2)$ large, and put $d:=k+D-1$; then $k\ge2$, $d\le2D$ for large
$D$, and
$$2^{-k}\le\min\Bigl(\tau(d),\ \frac{p(d)}{4d}\Bigr)$$
because $2^{-k}\le(D+2)^{-C}$ while $\tau(d),p(d)/(4d)\ge c_1d^{-c_2}/(4d)\ge
c_1(2D)^{-c_2-1}/4$. Apply (PAY★★) to $\mathsf H(k,g,\{1\})$, which lies in
$\mathcal C^{\mathrm{ind}}_d$ by T4(3). By T4(4) the two sides have identical
influence profiles: $\mathrm{Inf}_{u_i}(f_{\mathsf A})=2\cdot2^{-k-1}=2^{-k}$ on
block coordinates and $\mathrm{Inf}_j(f_{\mathsf A})=2Q_k\mathrm{Inf}_j(g)\le
\mathrm{Inf}_j(g)/2$ on spectators. Two cases.

*Case 1: some coordinate is $\tau(d)$-heavy for $f_{\mathsf A}$.* It is not a
block coordinate, since $2^{-k}<\tau(d)$ by the choice of $k$. So it is a
spectator $j$ with $2Q_k\mathrm{Inf}_j(g)\ge\tau(d)$, and $2Q_k\le\frac12$
gives $\mu(g)\ge\mathrm{Inf}_j(g)\ge2\tau(d)\ge1/\mathrm{poly}(D)$.

*Case 2: no coordinate is $\tau(d)$-heavy.* Then
$H_\tau(f_{\mathsf A})=H_\tau(f_{\mathsf B})=\emptyset$, so on both sides
$W_\tau$ is a maximum-degree monomial support, necessarily of the form $T\cup
S$ with $|S|=D$ by T4(5); T4(6) and (PAY★★) give
$p(d)\le\pi\le(k-1)2^{1-k}+D\mu(g)\le p(d)/2+D\mu(g)$, whence
$\mu(g)\ge p(d)/(2D)\ge1/\mathrm{poly}(D)$. $\square$

**The resulting near-dichotomy (this artifact's main structural finding).** On
the shape $\mathsf H(k,g,\Delta)$ the payment is governed entirely by
$\mu(g)=\max_j\mathrm{Inf}_j(g)$:
*(i)* if $\mu(g)\ge4\tau$ then $\pi\ge2\tau$ — indeed the heaviest coordinate
$j^\ast$ of $g$ satisfies $\mathrm{Inf}_{j^\ast}(f_{\mathsf A})=2Q_k\mu(g)\ge
\frac{1-2^{1-k}}2\mu(g)\ge\mu(g)/4\ge\tau$ for $k\ge2$, so $j^\ast$ is
$\tau$-heavy for **both** sides and $\pi\ge2\tau$;
*(ii)* if all coordinates are $\tau$-light then $\pi\le(k-1)2^{1-k}+D\mu(g)$
(T5(c)'s display), which is below every inverse polynomial when $\mu(g)$ is
exponentially small in $D$.
Together with T5(c′): **(PAY★★) holds only if every balanced degree-$D$
Boolean function has a coordinate of influence $\ge1/\mathrm{poly}(D)$, and it
fails outright if balanced degree-$D$ Boolean functions with all influences
$2^{-\Theta(D)}$ exist.** So plan P1's repaired key step is *at least as hard
as* — and on this family shape essentially equivalent to — a **single-function**
question, not a two-family one:
*does every balanced degree-$D$ Boolean function have a coordinate of influence
$\ge1/\mathrm{poly}(D)$?* Two remarks, used in no proof above:

* *The required dilution is extremal.* For balanced $\pm1$-valued $g$,
  $1=\mathrm{Var}(g)=\sum_{S\ne\emptyset}\hat g(S)^2\le\sum_S|S|\hat g(S)^2=\sum_j\mathrm{Inf}_j(g)$,
  while card **S6c** [READ] bounds the number of relevant variables of a
  degree-$D$ Boolean function by $4.394\cdot2^{D}$; hence
  $\mu(g)\ge1/(4.394\cdot2^{D})$ always. The object the refutation needs sits
  within a constant factor of the junta bound's extreme.
* *The other direction is source-blocked and is not used.* A printed
  $\mu(g)\ge\mathrm{Var}(g)/\mathrm{poly}(D)$ would remove this refutation
  shape; the only identified route is OSSS + a depth-vs-degree bound, both
  **unread** in this campaign (strategist §6.4's [MEMORY] register). Even
  granting it, it would close only *this* shape and would **not** prove
  (PAY★★). Status of (PAY★★): **OPEN, not conditional.**

### T5(d) The fibre route is not crossed

The strategist's identity
$\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E_w[\mathrm{Inf}^{(w)}_i(\mathbf 1_{A_w})]$
for $i\in W$ is correct (it is L2's computation
$\mathrm{Inf}_i=\frac14\Pr[\mathbf 1_A(x)\ne\mathbf 1_A(x^{\oplus i})]$ plus
the fact that flipping $i\in W$ preserves the $W$-fibre). But the crude
fibre-wise bound $\sum_{i\in W}\mathrm{Inf}^{(w)}_i(\mathbf 1_{A_w})\ge\alpha_w(1-\alpha_w)$
assembles only to $\mathbb E_w[\alpha_w\beta_w](\frac1\alpha+\frac1\beta)$,
which on $\mathsf H_d$ with $W=U$ equals $4(1-2^{-d})2^{-d}=\Theta(2^{-d})$.
**Nothing in this artifact uses it, so there is no gap to mark; the FIBRE-BALANCE
question is untouched and remains open (it is plan P2's).**

---

## 5. GAP REGISTER

| # | item | class | load-bearing for |
|---|---|---|---|
| G-1 | **(PAY★★) is OPEN** (T5(a)). Not a gap in any proof: no theorem here assumes it. It is the *stated* remaining step of plan P1 after T3 killed (PAY★). | open problem, not a gap | R2 itself (via T1). |
| G-2 | Direction check on T5(c)/T5(c′). The implication **(PAY★★) $\Rightarrow$ "every balanced degree-$D$ Boolean function has influence $\ge1/\mathrm{poly}(D)$"** (T5(c′)) is *general* — the family $\mathsf H(k,g,\Delta)$ enters only as a witness, and the conclusion is about all balanced $g$. The **reverse** implication is **not** claimed: a max-influence bound would refute only T5(c)'s refutation *shape* and would not prove (PAY★★). | scope declared | nothing; both directions are stated as proved/not-claimed respectively. |
| G-3 | The choice of maximum-degree support inside $W_\tau$ is *existential* for the prover: (PAY★★) as stated quantifies over all admissible choices, which is the conservative (harder) reading. A weaker reading (some canonical choice) is not used. | reading declared | nothing. |
| G-4 | Nothing is marked [GAP] inside any proof of §§2–4. L1, L2, L4, L5, L6, T1, T2, T3, T4, T5(b), T5(c) are complete. | — | — |

**No [SOURCE-BLOCKED] step exists in this artifact.** The one source-blocked
statement in the campaign that touches this material (OSSS + depth-vs-degree)
appears only in T5(c)'s second remark, explicitly outside every proof.

## 6. DEPENDENCIES

| dependency | exact use | tag |
|---|---|---|
| **Card S7b, item T3.4** (Chang–Fang, arXiv:2510.13705v3, Cor. 3.4, p. 7) + **item T3.2** (Thm 3.2, p. 6, first display): for $G$ a product of finite abelian groups and $f:G\to\mathbb C$ non-zero, $\dim_\pi(\mathrm{supp}f)+\deg_{\hat G}(f)\ge n$, and $\pi_{S^c}(\mathrm{supp}f)=X_{S^c}$ for $S$ a maximum-degree character support. | **L3** (window existence and the maximum-degree-support form). The *only* load-bearing external input. Hypotheses checked item by item in L3; **WINDOW only**, density never used. | **CARD** [READ] |
| **Card S6c** (Wellens, Discrete Analysis 2022:19, Thm 1.1 (1.3)): a degree-$D$ Boolean function has $\le4.394\cdot2^{D}$ relevant variables. | T5(c), *remark only* (to show the required dilution is extremal). Not used in any proof. | **CARD** [READ], non-load-bearing |
| **Card S6a** (Nisan–Szegedy influence quantum $\mathrm{Inf}^{\mathrm{flip}}_i\ge2^{1-d}$). | Cited only as corroboration of **L2**, which is proved inline from L1. | **CARD** [RESTATED], non-load-bearing |
| **Card S1 / K1** (ACC22 Thm 4.4: the statement holds for $\delta<|\mathcal Y|^{-d}/d$). | Comparison only, in T2's declarations. | **CARD**, non-load-bearing |
| **I01 / R1 (FROZEN)** | Cited only as a frozen statement in the discussion (the grid extremal's role, and that the junta subclass is settled). **Not re-derived, not re-verified; none of its internal lemmas (F1–F4) is used.** | frozen black box |
| Nisan–Szegedy Lemma 2.6 (nonvanishing) | **Proved inline as L1**; no citation. | **PROVED-INLINE** |
| everything else (L2, L4, L5, L6, T1, T2, T3, T4, T5) | — | **PROVED-INLINE** |

**Machine artifacts.** `proofs/0023-prover-2-code/check_family.py` (exact
rational arithmetic; all assertions pass for $d=2..12$) —
independent confirmation of §3. `proofs/0023-prover-2-code/check_table.py` —
exact confirmation of the three inherited-family rows of T5(b): grid
$\pi=1$ exactly ($d=2,3,4$); subcube pair
$\pi=d(\frac12+\frac{2^{-d-1}}{1-2^{-d}})$ ($d=2..5$); address pair
$\pi=k/2+2^{-k}$ ($k=1,2,3$), with $\mathrm{Inf}_{a_i}(\mathbf 1)=\frac18$ and
$\mathrm{Inf}_{y_j}(\mathbf 1)=2^{-k-2}$ as derived. `campaign/lean/0023-prover-2-skeleton.lean` —
statement-only Lean skeleton of the definitions and of L1, L2, L4, L5, T1, T2,
T3; type-checks against Mathlib (lean4 v4.33.0) with nine `sorry`s and **no
errors**. Compilation of a `sorry`-closed file is not proof; the skeleton
certifies the *statements*, not the proofs.

**Units.** `0023-prover-2-u0` (sketch), `-u1` (M1a), `-u2` (T3), `-u3`
(T4/T5), `-u4` (Lean). This file is the assembled, self-contained artifact.

## 7. SOURCE REQUEST

**None from this plan.** (Recorded for the campaign, not requested here: the
strategist's rank-1/rank-2 requests — OSSS and a decision-tree-depth-vs-degree
bound — would settle whether T5(c)'s refutation shape exists, hence would
resolve one half of (PAY★★)'s status. They are plan P4's gate; this artifact
proceeds without them and claims nothing that needs them.)

### END OF ARTIFACT 0023-prover-2 ###
