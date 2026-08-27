---
id: 0023-prover-2-u1
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE (unit 1 of 5) — milestone M1a
---

# Unit 1 — M1a: the unconditional reduction, the positivity lemma, and an unconditional threshold

Notation as in u0 §0. Throughout, $d\ge1$ is an integer, $N\ge1$, and
$A,B\subseteq\{\pm1\}^N$ are nonempty with $\deg\mathbf 1_A\le d$,
$\deg\mathbf 1_B\le d$; $\alpha=|A|/2^N$, $\beta=|B|/2^N$,
$f_A=\mathbf 1_A/\sqrt\alpha$, $f_B=\mathbf 1_B/\sqrt\beta$.

*(The degenerate case $d=0$: a degree-$0$ indicator is constant, and being an
indicator of a nonempty set it is $\equiv1$, so $A=B=\{\pm1\}^N$ and R2's
conclusion is immediate. All statements below are for $d\ge1$.)*

---

## L1 (nonvanishing). PROVED-INLINE

**Statement.** Let $p:\{\pm1\}^n\to\mathbb R$ be a multilinear polynomial,
$p\not\equiv0$, $\deg p\le k$. Then $\Pr_{x}[p(x)\ne0]\ge2^{-k}$, $x$ uniform
on $\{\pm1\}^n$.

*(This is the statement attributed in the literature to Nisan–Szegedy,
Lemma 2.6 — see card S6a's retrieval note. It is proved from scratch here, so
**no citation is load-bearing**.)*

**Proof.** Induction on $n$, the statement being asserted for all $k\ge0$
simultaneously.

*Base $n=0$.* Then $p$ is a nonzero constant and $\Pr[p\ne0]=1\ge2^{-k}$.

*Step.* Let $n\ge1$ and write $x=(x',x_n)$, $x'\in\{\pm1\}^{n-1}$. By
multilinearity $p(x)=q(x')+x_n\,r(x')$ with $q,r$ multilinear in $x'$;
explicitly $r=\tfrac12\bigl(p(\cdot,+1)-p(\cdot,-1)\bigr)$.

*Case 1: $r\equiv0$.* Then $p=q$ does not involve $x_n$; $q\not\equiv0$ and
$\deg q\le k$, so the inductive hypothesis in $n-1$ variables gives
$\Pr_{x'}[q(x')\ne0]\ge2^{-k}$, and $\Pr_x[p(x)\ne0]=\Pr_{x'}[q(x')\ne0]$.

*Case 2: $r\not\equiv0$.* Every monomial of $x_nr(x')$ is a monomial of $p$,
so $1+\deg r\le\deg p\le k$; in particular $k\ge1$ and $\deg r\le k-1$. By the
inductive hypothesis, $\Pr_{x'}[r(x')\ne0]\ge2^{-(k-1)}$. Fix $x'$ with
$r(x')\ne0$: since $p(x',+1)-p(x',-1)=2r(x')\ne0$, at least one of
$p(x',+1),p(x',-1)$ is nonzero, so $\Pr_{x_n}[p(x',x_n)\ne0\mid x']\ge\tfrac12$.
Averaging, $\Pr_x[p(x)\ne0]\ge\tfrac12\cdot2^{-(k-1)}=2^{-k}$. $\square$

---

## L2 (influence quantum). PROVED-INLINE from L1

**Statement.** Let $\emptyset\ne A\subseteq\{\pm1\}^N$ with
$\deg\mathbf 1_A\le d$ and let $i\in\mathrm{rel}(A)$. Then
$$\mathrm{Inf}_i(\mathbf 1_A)\ \ge\ 2^{-1-d},\qquad\text{hence}\qquad
\mathrm{Inf}_i(f_A)\ =\ \frac{\mathrm{Inf}_i(\mathbf 1_A)}{\alpha}\ \ge\ \frac{2^{-1-d}}{\alpha}.$$

**Proof.** Write $\mathbf 1_A=q+x_i r$ with $q,r$ multilinear and not
involving $x_i$; then $r=\tfrac12(\mathbf 1_A|_{x_i=+1}-\mathbf 1_A|_{x_i=-1})$
takes values in $\{-\tfrac12,0,\tfrac12\}$, and $r\not\equiv0$ exactly because
$i\in\mathrm{rel}(A)$. Grouping the expansion by whether $S\ni i$ gives
$r=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)\,x^{S\setminus\{i\}}$, so by
orthonormality of the monomials
$$\mathrm{Inf}_i(\mathbf 1_A)=\sum_{S\ni i}\widehat{\mathbf 1_A}(S)^2=\mathbb E[r^2]
=\tfrac14\Pr[r\ne0].$$
Every monomial of $x_ir$ is a monomial of $\mathbf 1_A$, so $\deg r\le d-1$;
L1 gives $\Pr[r\ne0]\ge2^{-(d-1)}$, whence
$\mathrm{Inf}_i(\mathbf 1_A)\ge\tfrac14\,2^{1-d}=2^{-1-d}$. The normalized
form follows from $\mathrm{Inf}_i(cf)=c^2\mathrm{Inf}_i(f)$ with
$c=\alpha^{-1/2}$. $\square$

*(This is card S6a's "engine" in the Contract's Fourier normalisation; the
card's own influence dictionary asserts the same value $2^{-1-d}$. Proving it
inline removes the card's flagged factor-4 conversion risk from the dependency
list.)*

---

## L3 (shattering windows exist). CARD S7b [READ] + one definitional closure step

**Statement.** Let $\emptyset\ne A\subseteq\{\pm1\}^N$ with
$\deg\mathbf 1_A\le d$. Then:

1. $\mathcal S_d(A)\ne\emptyset$;
2. if $S\subseteq[N]$ satisfies $\widehat{\mathbf 1_A}(S)\ne0$ and
   $|S|=\deg\mathbf 1_A$, then $S\in\mathcal S_d(A)$;
3. if $W\in\mathcal S_d(A)$ and $W\subseteq W'$ with $|W'|\le d$, then
   $W'\in\mathcal S_d(A)$.

**Provenance and hypothesis check.** (1) and (2) are card S7b's item **T3.4**
(Chang–Fang, arXiv:2510.13705v3, Corollary 3.4, p. 7, [READ]) together with
its item **T3.2** (Theorem 3.2, p. 6, first display), applied with
$G_1=\dots=G_N=\mathbb Z_2$, so $G=\mathbb Z_2^N\cong\{\pm1\}^N$ and $n=N$.
Hypotheses, itemised against the card:
*(a)* $G$ a finite product of finite abelian groups ✔;
*(b)* $f:G\to\mathbb C$ non-zero — take $f=\mathbf 1_A$, non-zero as
$A\ne\emptyset$ ✔;
*(c)* $\deg_{\hat G}$ is the Contract's degree — the card records this as
printed and "identical, symbol for symbol" (card S7b, flag 3), and for
$\mathcal Y=\mathbb Z_2$ a character $\chi$ with non-trivial coordinates
exactly on $S$ is the monomial $x^S$, so $\deg_{\hat G}(\mathbf 1_A)=
\deg\mathbf 1_A\le d$ ✔;
*(d)* the conclusion $\dim_\pi(\mathrm{supp}f)+\deg_{\hat G}(f)\ge N$ unfolds,
by the card's printed definition of $\dim_\pi$, to: there is $T$ with
$|T|\ge N-d$ and $\pi_T(A)=\{\pm1\}^T$; put $W=[N]\setminus T$, $|W|\le d$.
The card states in flag 4 that this unfolding is definitional, not an
inference ✔. For (2), the card's flag 4 last sentence records the stronger
fibre-wise form of T3.2, $\pi_{S^c}(\mathrm{supp}f)=\mathcal Y^{S^c}$ for $S$
**any** maximum-degree character support ✔.
*(e)* No hypothesis on $N$; uniform in $N$ ✔ (essential: our $\delta$ must be
$N$-free).

(3) is immediate and proved here: $\pi_{[N]\setminus W'}$ is the composition of
$\pi_{[N]\setminus W}$ with the coordinate projection
$\{\pm1\}^{[N]\setminus W}\to\{\pm1\}^{[N]\setminus W'}$ (legitimate since
$[N]\setminus W'\subseteq[N]\setminus W$), and a composition of surjections
onto the stated codomains is surjective. $\square$

**What is NOT used.** The density consequence $\alpha\ge2^{-d}$ of the same
card (capped at K1's scale, card S7b's scout remark) is used nowhere in this
artifact.

---

## L4 = G1 (positivity: every shattering window of $A$ meets $\mathrm{rel}(B)$). PROVED-INLINE — new

**Statement.** Let $A,B\subseteq\{\pm1\}^N$ be nonempty and disjoint and let
$W\in\mathcal S_d(A)$. Then $W\cap\mathrm{rel}(B)\ne\emptyset$.

*(No degree hypothesis on $B$ is needed; only that $W$ is a shattering window
for $A$ and that $A\cap B=\emptyset$, $B\ne\emptyset$.)*

**Proof.** Suppose $W\cap\mathrm{rel}(B)=\emptyset$. Fix $b\in B$ ($B\ne
\emptyset$). Since $W\in\mathcal S_d(A)$, the projection
$\pi_{[N]\setminus W}(A)$ is all of $\{\pm1\}^{[N]\setminus W}$, so there is
$a\in A$ with $a|_{[N]\setminus W}=b|_{[N]\setminus W}$.

The points $a$ and $b$ differ only in coordinates of $W$; let
$i_1,\dots,i_m\in W$ be those coordinates and set $b^{(0)}=b$,
$b^{(t)}=(b^{(t-1)})^{\oplus i_t}$, so $b^{(m)}=a$. For each $t$, the
coordinate $i_t$ lies in $W$, hence $i_t\notin\mathrm{rel}(B)$, hence by the
definition of $\mathrm{rel}(B)$ we have $\mathbf 1_B(y)=\mathbf 1_B(y^{\oplus
i_t})$ for **every** $y$; applying this at $y=b^{(t-1)}$ gives
$\mathbf 1_B(b^{(t)})=\mathbf 1_B(b^{(t-1)})$. By induction on $t$,
$\mathbf 1_B(a)=\mathbf 1_B(b^{(m)})=\mathbf 1_B(b)=1$, i.e. $a\in B$. Then
$a\in A\cap B$, contradicting disjointness. $\square$

**Remarks.** (i) The case $m=0$ ($a=b$) is included and gives the
contradiction at once; in particular the lemma also covers $W=\emptyset$,
which is therefore impossible for a cross-disjoint pair. (ii) This is
strictly stronger than the cylinder-based projection step of the frozen R1
proof, and is the first two-family consequence of the Chang–Fang window
recorded in this campaign: card S7 and card S7b both certify (over the
complete text) that the source contains **no** two-function statement, so the
combination with disjointness is new here and must be verified, not cited.
(iii) It is *not* the projection-disjointness of R1's (F3)/(F4): nothing is
claimed about $\pi_S(A)$ and $\pi_S(B)$ being disjoint — for general
degree-$\le d$ sets they typically both fill $\{\pm1\}^S$.

---

## L5 (master count with pair-independent windows). PROVED-INLINE

**Statement.** Let $\mathbf F,\mathbf G$ be finitely supported distributions
over $\mathcal C^{\mathrm{ind}}_d$ on $\{\pm1\}^N$, and let
$\delta_{\mathbf F}:=\max_{i\in[N]}\mathbb E_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]$,
$\delta_{\mathbf G}$ likewise. Let $W(\cdot)$ assign to each function in
$\mathrm{supp}\,\mathbf F\cup\mathrm{supp}\,\mathbf G$ a set
$W(\cdot)\subseteq[N]$, **depending on that function alone**. Draw
$f\sim\mathbf F$ and $g\sim\mathbf G$ *independently* and put
$$\pi(f,g):=\sum_{i\in W(g)}\mathrm{Inf}_i(f)+\sum_{i\in W(f)}\mathrm{Inf}_i(g).$$
Then
$$\mathbb E_{f,g}[\pi(f,g)]\ \le\ \delta_{\mathbf F}\,\mathbb E_g|W(g)|+\delta_{\mathbf G}\,\mathbb E_f|W(f)| .$$
In particular if $|W(\cdot)|\le\omega$ always, then $\mathbb E[\pi]\le
(\delta_{\mathbf F}+\delta_{\mathbf G})\,\omega$.

**Proof.** All sums are finite ($N$ coordinates, finite supports), so
expectations and sums interchange freely:
$$\mathbb E_{f,g}\Bigl[\sum_{i\in W(g)}\mathrm{Inf}_i(f)\Bigr]
=\sum_{i=1}^N\mathbb E_{f,g}\bigl[\mathbf 1\{i\in W(g)\}\,\mathrm{Inf}_i(f)\bigr]
=\sum_{i=1}^N\Pr_g[i\in W(g)]\cdot\mathbb E_f[\mathrm{Inf}_i(f)],$$
the last step by independence of $f$ and $g$ — this is where $W(g)$ must not
depend on $f$. Bounding $\mathbb E_f[\mathrm{Inf}_i(f)]\le\delta_{\mathbf F}$
(legitimate as $\Pr_g[i\in W(g)]\ge0$) and using
$\sum_i\Pr_g[i\in W(g)]=\mathbb E_g|W(g)|$ gives
$\le\delta_{\mathbf F}\mathbb E_g|W(g)|$. The second term is symmetric.
$\square$

**The two drafting rules, verified.** (i) The payment must sit on the
*partner's* window: charging $\sum_{i\in W(f)}\mathrm{Inf}_i(f)$ would give
$\Pr_f$-weights correlated with $\mathrm{Inf}_i(f)$ and no $\delta$ factor
(indeed $\sum_{i\in W(f)}\mathrm{Inf}_i(f)\le d$ is all one can say, and the
count degenerates). (ii) $W(\cdot)$ must be pair-independent, else the
factorisation above fails; this is card S7's non-canonicity obstacle in its
only load-bearing form.

---

## T1 (the reduction). PROVED-INLINE

**Statement.** Let $\omega,p$ be functions of $d$ with $\omega(d)\ge1$,
$p(d)>0$. Suppose that for every $d\ge1$ and $N\ge1$ there is a map $W_{d,N}$
assigning to each $f\in\mathcal C^{\mathrm{ind}}_d$ on $\{\pm1\}^N$ a window
$W_{d,N}(f)\subseteq[N]$ with $|W_{d,N}(f)|\le\omega(d)$, such that
$$\textbf{(PAY}\star_{\mathcal W}\textbf{)}\qquad
\sum_{i\in W(f_B)}\mathrm{Inf}_i(f_A)+\sum_{i\in W(f_A)}\mathrm{Inf}_i(f_B)\ \ge\ p(d)$$
for **every** pair of nonempty disjoint $A,B\subseteq\{\pm1\}^N$ with
$\deg\mathbf 1_A,\deg\mathbf 1_B\le d$. Then the R2 statement holds with any
$\delta:\mathbb N\to(0,1]$ satisfying $\delta(d)<p(d)/(2\omega(d))$ for all
$d\ge1$. In particular, if $p(d)\ge1/\mathrm{poly}(d)$ and
$\omega(d)\le\mathrm{poly}(d)$ then $\delta$ may be taken inverse-polynomial,
which is exactly what R2 asks for.

**Proof.** Fix $d,N$ and distributions $\mathbf F,\mathbf G$ over
$\mathcal C^{\mathrm{ind}}_d$ with $\mathbb E_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]
\le\delta(d)$ and $\mathbb E_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]\le\delta(d)$
for every $i$. Assume, for contradiction, that they are *incompatible*:
$f(x)g(x)=0$ for all $f\in\mathrm{supp}\,\mathbf F$,
$g\in\mathrm{supp}\,\mathbf G$, $x\in\{\pm1\}^N$.

Each $f\in\mathcal C^{\mathrm{ind}}_d$ is $\mathbf 1_A/\sqrt\alpha$ for the
unique nonempty $A=\{x:f(x)\ne0\}$ with $\deg\mathbf 1_A\le d$; so
$f(x)g(x)\ne0\iff x\in A\cap B$, and incompatibility says precisely that
$A\cap B=\emptyset$ for every pair $(f,g)=(f_A,f_B)$ in
$\mathrm{supp}\,\mathbf F\times\mathrm{supp}\,\mathbf G$. Hence
(PAY$\star_{\mathcal W}$) applies to every such pair and $\pi(f,g)\ge p(d)$
pointwise, so $\mathbb E[\pi]\ge p(d)$. On the other hand L5 with
$\omega=\omega(d)$ and $\delta_{\mathbf F},\delta_{\mathbf G}\le\delta(d)$
gives $\mathbb E[\pi]\le2\,\delta(d)\,\omega(d)<p(d)$. Contradiction. So the
pair is compatible, i.e. some $f,g,x$ have $f(x)g(x)\ne0$. $\square$

---

## T2 (unconditional threshold). PROVED-INLINE

**Statement (a) — unconditional payment.** For every $d\ge1$, every $N$, every
nonempty disjoint $A,B\subseteq\{\pm1\}^N$ with
$\deg\mathbf 1_A,\deg\mathbf 1_B\le d$, and **every** choice of
$W_A\in\mathcal S_d(A)$, $W_B\in\mathcal S_d(B)$,
$$\pi\bigl((A,W_A),(B,W_B)\bigr)\ =\ \sum_{i\in W_B}\mathrm{Inf}_i(f_A)+\sum_{i\in W_A}\mathrm{Inf}_i(f_B)\ \ge\ 2^{-1-d}\Bigl(\frac1\alpha+\frac1\beta\Bigr)\ \ge\ 2^{1-d}.$$

**Statement (b) — threshold.** The R2 statement holds with every
$\delta:\mathbb N\to(0,1]$ such that $\delta(d)<2^{-d}/d$ for all $d\ge1$.

**Proof of (a).** By L4 applied to the pair $(A,B)$ and $W_B\in\mathcal
S_d(B)$ — with the roles of the two sets exchanged — there is
$j\in W_B\cap\mathrm{rel}(A)$; and by L4 applied to $W_A\in\mathcal S_d(A)$
there is $i\in W_A\cap\mathrm{rel}(B)$. All summands of $\pi$ are
nonnegative, so keeping only these two terms and applying L2 twice,
$$\pi\ \ge\ \mathrm{Inf}_j(f_A)+\mathrm{Inf}_i(f_B)\ \ge\ \frac{2^{-1-d}}{\alpha}+\frac{2^{-1-d}}{\beta}.$$
Since $A$ and $B$ are disjoint, $\alpha+\beta\le1$; and by AM–HM
$\frac1\alpha+\frac1\beta\ge\frac{4}{\alpha+\beta}\ge4$. Hence
$\pi\ge2^{-1-d}\cdot4=2^{1-d}$. $\square$

**Proof of (b).** For each $d,N$ define a window map on
$\mathcal C^{\mathrm{ind}}_d$ by choosing, for each of the finitely many
$f=f_A$ in the class, some $W(f)\in\mathcal S_d(A)$; this is possible by L3(1)
(a choice from finitely many nonempty finite collections; no choice axiom
needed). Then $|W(f)|\le d=:\omega(d)$, and by (a) the hypothesis
(PAY$\star_{\mathcal W}$) of T1 holds with $p(d)=2^{1-d}$. T1 yields R2 for
every $\delta(d)<2^{1-d}/(2d)=2^{-d}/d$. $\square$

### Declarations required by I02 and by the plan's TRAP clause

* **T2(b) is a PARTIAL, not a proof of R2.** Its threshold $2^{-d}/d$
  degrades exponentially in $d$, so by I02's recorded rule ("an artifact whose
  threshold degrades exponentially in $d$ … is a PARTIAL, not a proof of R2,
  and must say so in its verdict") it settles nothing on this rung. R2's
  content window $[2^{-d}/d,\ 1/(2d))$ is **untouched** by T2.
* **Where the exponential comes from.** *Not* from the junta size: no step
  above uses cards S6b–S6d, and the window is $\le d$ by theorem (L3). It
  comes from the influence *quantum* $2^{-1-d}$ of L2, which card S6a
  certifies is attained (codimension-$d$ subcubes) and cannot be improved.
  So T2 is exactly as far as *positivity alone* can go, and the entire rung is
  the constant in (PAY$\star$).
* **Relation to K1.** Card S1's K1 gives the full $\mathbb Z_2$ statement for
  every $\delta<2^{-d}/d$. T2(b) reproduces that threshold *exactly*, for the
  subclass $\mathcal C^{\mathrm{ind}}_d$, by a completely independent route
  (no per-character mass accounting; the only external input is card S7b's
  $\le d$-sized window). It is therefore a **second, structurally different
  proof of a K1-order threshold**, and — by L3's provenance — the first
  one whose only $d$-dependence in the *count* is $|W|\le d$.

EMITTED unit 1 of 5 (milestone M1a complete); NEXT UNIT: u2 = T3, the
refutation of (PAY$\star$) in its all-windows form; ARTIFACT 0023-prover-2.

### END OF ARTIFACT 0023-prover-2-u1 ###
