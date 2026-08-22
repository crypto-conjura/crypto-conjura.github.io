# Extraction and decomposition for two split unpredictable random-oracle sources

Revision r2 of `split-decomp-kappa-1`, repairing four findings upheld in triage
(F1, F3, F5, F7). Supersedes that id; the earlier id's audit tally does not carry
over, since it was recorded against different content.

## 0. Goal

Fix $N,M\in\mathbb N$ with $N\ge 2$ and $M\ge 2$ and let $\mathsf{Fun}:=\{f:[N]\times[N]\to[M]\}$, with
$H\gets_{\$}\mathsf{Fun}$. Let $(S_1,S_2)$ be a split $\delta$-unpredictable pair of sources
with leakage bounded by $\sigma_1,\sigma_2$, $\sigma:=\sigma_1+\sigma_2$,
$\sigma':=\sigma+2\log N$, and let $q^{+}:=q+1$. All logarithms are base two.
Definitions of source, splitness, unpredictability, $P$-bit-fixing source,
$P$-mixture, consistency, observer, the experiments $\mathsf{Real}$, $\mathsf{Dec}$,
$\mathsf{Real}_0$, $\mathsf{Dec}_0$, the advantage $\mathsf{Adv}_{\mathcal Y,D}$ and the
extraction advantage $\kappa(q)$ are those of the Contract and are not repeated.

This document establishes four things.

**(A)** $\kappa^{\mathrm{na}}(q)\le 5\sqrt{\sigma'\delta}+q\delta$, where $\kappa^{\mathrm{na}}$
restricts the supremum to observers whose *query positions* do not depend on the
challenge value; and $\kappa(0)\le 5\sqrt{\sigma'\delta}$ with no restriction.

**(B)** $\kappa(q)\le 5\sqrt{\sigma'\delta}+\mu(\min(qM,N^{2}))$ for every $q$ and every
observer, where $\mu(s):=\min\bigl(s\delta,\ 3(s\delta^{2})^{1/3},\ 1\bigr)$.

**(C)** An explicit family $\mathcal Y^{P,\gamma}$, chosen before $q$, with
$\mathsf{Adv}_{\mathcal Y,D}\le\kappa(q)+2(\sigma'+\log\gamma^{-1})q/P+\gamma+P\delta+q\delta$.

**(C$'$)** Consequently the Contract's conjecture holds, with the absolute constants
$c=2$ and $C=8$, for every $P\le\sqrt{\sigma'/\delta}$ and every $q$ with
$q^{+}\delta\le\sigma'$, provided either the observer's query positions are independent
of the challenge value, or $M\le\sigma'/\sqrt{27\delta}$.

The conjecture in full — all $P$, all $q$, all $M$, all observers — is **not** proved.
Section 9 states exactly what is missing and why.

## 1. The two structural facts

Write $\mathcal Z:=\{0,1\}^{\le\sigma_1}\times\{0,1\}^{\le\sigma_2}$, so
$|\mathcal Z|=(2^{\sigma_1+1}-1)(2^{\sigma_2+1}-1)<2^{\sigma+2}$.

**Lemma 0 (derandomisation).** For every $q$ and every $q$-query challenge-oblivious $D$
there is a deterministic such $D'$ with $\mathsf{Adv}_{\mathcal Y,D}\le\mathsf{Adv}_{\mathcal Y,D'}$,
and the supremum defining $\kappa(q)$ is attained on deterministic observers.

*Proof.* Let $\rho$ be $D$'s coins and $D_\rho$ the deterministic strategy it then runs.
All of $\mathsf{Fun},[N],[M],\mathcal Z$ are finite and $D$ makes at most $q$ queries, so
there are finitely many deterministic $q$-query challenge-oblivious strategies. Each
quantity at issue is $|\mathbb E_\rho[\alpha(\rho)]|$ with
$\alpha(\rho)=\Pr[\mathsf E_1=1\mid\rho]-\Pr[\mathsf E_0=1\mid\rho]$, the coins being
independent of every other draw and the paired experiments differing in no other
component; so it is at most $\max_\rho|\alpha(\rho)|$, attained at some $\rho^{*}$. Take
$D':=D_{\rho^{*}}$, which is $q$-query and challenge-oblivious. Moreover $D'$
inherits any challenge resolution $D$ has: challenge resolution is defined in Section 4
per fixed coin string, so if the runs $D^{f}_{\rho}(v,\zeta)$ and $D^{f}_{\rho}(v',\zeta)$
issue the same query positions for every $\rho$ whenever $h(v)=h(v')$, they do so in
particular for $\rho^{*}$. $\square$

Once $D$ is deterministic and its oracle is fixed to $f$, its output is a function of its
challenge input alone; write $\theta:[M]\to\{0,1\}$ for that function and
$p_\theta:=|\theta^{-1}(1)|/M$.

**Lemma 1 (posterior product structure).** For every $(f,\zeta)$ in the support of
$(H,\mathbf z)$, the conditional law of $\mathbf x$ is the product
$\Pi_{f,\zeta}=\pi^{1}_{f,\zeta_1}\otimes\pi^{2}_{f,\zeta_2}$ with
$\pi^{i}_{f,\zeta_i}(u)=\Pr[x_i=u\mid H=f,\ z_i=\zeta_i]$. Writing
$m_i:=\|\pi^{i}_{f,\zeta_i}\|_\infty$:

  (i) $\max_{\mathbf u}\Pi_{f,\zeta}(\mathbf u)=m_1m_2$;
 (ii) $\mathbb E[m_i]\le\delta$ for $i=1,2$;
(iii) $\mathbb E[m_1m_2]\le\delta$;
 (iv) $\Pr[m_1m_2>\theta]\le 2\delta/\sqrt\theta$ for every $\theta\in(0,1]$.

*Proof.* The two sources are run on independent private coins and on the same $H$, so
conditioned on $H=f$ their output pairs are independent:
$\Pr[x_1=u_1,z_1=\zeta_1,x_2=u_2,z_2=\zeta_2\mid f]=\prod_i\Pr[x_i=u_i,z_i=\zeta_i\mid f]$.
Summing over $u_1,u_2$ gives $\Pr[\mathbf z=\zeta\mid f]=\prod_i\Pr[z_i=\zeta_i\mid f]>0$,
and dividing gives the product form. (i) is the fact that the maximum of a product
measure is the product of the maxima.

For (ii), let $\mathsf P$ be the predictor that, on input $\mathbf z$ and with oracle
access to $H$, reads all of $H$, computes $\pi^{i}_{H,z_i}$ — it may, the sources being
fixed and predictors being arbitrary, possibly randomised, functions of their inputs —
and outputs a maximiser. Then
$\Pr[\mathsf P^{H}(\mathbf z)=x_i]=\mathbb E_{(f,\zeta)}[m_i(f,\zeta)]$, which
unpredictability bounds by $\delta$.

(iii) follows from $m_2\le1$ and (ii). For (iv), $m_1m_2>\theta$ with both factors in
$[0,1]$ forces $m_i>\sqrt\theta$ for some $i$; Markov and (ii) give
$\Pr[m_i>\sqrt\theta]\le\delta/\sqrt\theta$. $\square$

Fact (i) is where the second source is spent: a single cell of $[N]^2$ carries mass
$m_1m_2$, a product of two independently small numbers, whereas one unpredictable source
over $[N]^2$ gives only $\delta$ per cell.

**$\mathbb E[m_1m_2]\le\delta^{2}$ is false**, and the counterexample is needed later to
justify an exponent. Let $2\le M\le N$, $\delta:=1/M$, let $E$ be the event $f(1,1)=1$,
of probability $\delta$, and let both sources output $x_i:=1$ if $E$ holds and $x_i$
uniform on $[N]$ otherwise, leaking the empty string. The coins are independent, so the
pair is split, and $\mathbb E[m_i]=\delta+(1-\delta)/N\le2\delta$, so the pair is
$2\delta$-unpredictable; yet $m_1m_2=1$ on $E$, so $\mathbb E[m_1m_2]\ge\delta$. Splitness
constrains the coins, not the two sources' common dependence on $f$.

## 2. Flattening

**Lemma 2.** Let $\pi$ be a distribution on $[N]$ with $\|\pi\|_\infty=m$ and
$k:=\lfloor1/m\rfloor$. Then $1\le k\le N$, $1/k\le2m$, and $\pi$ is a convex combination
of distributions uniform on subsets of size exactly $k$. Consequently, for every
$G:[N]^{2}\to[-1,1]$ and every $\pi^{1},\pi^{2}$ with $\|\pi^{i}\|_\infty=m_i$,
$k_i=\lfloor1/m_i\rfloor$,
$$\bigl|\mathbb E_{\pi^{1}\otimes\pi^{2}}[G]\bigr|\ \le\ \max\bigl\{\ \bigl|\mathbb E_{\mathrm{Unif}(B_1)\otimes\mathrm{Unif}(B_2)}[G]\bigr|\ :\ |B_i|=k_i\ \bigr\}.$$

*Proof.* $m\ge1/N$ gives $k\le N$; $m\le1$ gives $k\ge1$. For $x\ge1$, $\lfloor x\rfloor\ge x/2$
(for $1\le x<2$ because $\lfloor x\rfloor=1\ge x/2$; for $x\ge2$ because $\lfloor x\rfloor>x-1\ge x/2$),
so with $x=1/m$, $1/k\le2m$. Since $\|\pi\|_\infty\le1/k=2^{-\log k}$ and $2^{\log k}=k\in\mathbb N$,
the flat-decomposition lemma [CFHS, Lemma 3] applies and writes $\pi$ as a convex
combination of distributions uniform on $k$-subsets. The displayed inequality follows
because $(\rho^1,\rho^2)\mapsto\mathbb E_{\rho^1\otimes\rho^2}[G]$ is bilinear, so
substituting both decompositions expresses the left side as a convex combination of the
quantities on the right. $\square$

Note that $G$ is arbitrary; it will carry an indicator $\mathbb 1[\mathbf u\notin\mathcal S]$
that does not factor over the coordinates, which is harmless because the linear structure
used is in $(\pi^1,\pi^2)$, not in $G$.

## 3. Rectangle discrepancy

A **revealing rule of budget $s$** is a family $(\mathcal A_\zeta)_{\zeta\in\mathcal Z}$ of
procedures, where $\mathcal A_\zeta$ inspects coordinates of $f$ one at a time — the next
a function of $\zeta$ and the values already seen — halts having inspected a set
$\mathcal S(f,\zeta)$ with $|\mathcal S(f,\zeta)|\le s$, and outputs a test
$\theta_{\zeta,f}:[M]\to\{0,1\}$ that is a function of $\zeta$ and the inspected values.

**Lemma 3.** Let $N\ge2$, $\gamma_0\in(0,1)$ and $(\mathcal A_\zeta)$ a revealing rule.
Put $L:=\ln(eN)$, $C_0:=(\sigma+2)\ln2+\ln\frac{4N^{2}}{\gamma_0}$ and
$$t(k_1,k_2):=\sqrt{\frac{k_1\ln\frac{eN}{k_1}+k_2\ln\frac{eN}{k_2}+C_0}{2k_1k_2}}.$$
Then with probability at least $1-\gamma_0$ over $f\gets_{\$}\mathsf{Fun}$, simultaneously
for all $\zeta\in\mathcal Z$, all $k_1,k_2\in[N]$ and all $B_i\subseteq[N]$ with
$|B_i|=k_i$, writing $R=B_1\times B_2$,
$$\Bigl|\ \tfrac{1}{k_1k_2}\!\!\sum_{u\in R\setminus\mathcal S(f,\zeta)}\!\!\bigl(\theta_{\zeta,f}(f(u))-p_{\theta_{\zeta,f}}\bigr)\Bigr|\ \le\ t(k_1,k_2).$$
Moreover $t(k_1,k_2)\le\sqrt{L(m_1+m_2)+2C_0m_1m_2}$ whenever $k_i=\lfloor1/m_i\rfloor$, and
$$\mathbb E\bigl[t(k_1,k_2)\bigr]\ \le\ \sqrt{2\delta(L+C_0)}\ \le\ \sqrt{8\delta(\sigma'+\log\gamma_0^{-1})}.$$

*Proof.* **(1)** Fix $\zeta$. For $S_0\subseteq[N]^{2}$ and $w\in[M]^{S_0}$ the event
$\mathcal T_{S_0,w}=\{\mathcal S(f,\zeta)=S_0\wedge f|_{S_0}=w\}$ is measurable with
respect to $f|_{S_0}$: replaying $\mathcal A_\zeta$ on $w$ reproduces its whole inspection
sequence. The coordinates of $f$ being i.i.d. uniform, conditioning on such an event
leaves $f|_{[N]^{2}\setminus S_0}$ i.i.d. uniform; and $\theta_{\zeta,f},p_{\theta_{\zeta,f}}$
are constant on $\mathcal T_{S_0,w}$.

**(2)** Fix also $k_1,k_2,B_1,B_2$ and condition on $\mathcal T_{S_0,w}$. Write
$\theta,p_\theta$ for the constants and $n_0:=|R\setminus S_0|\le k_1k_2$. The variables
$\theta(f(u))-p_\theta$, $u\in R\setminus S_0$, are independent, lie in an interval of
length $1$, and have mean $0$, since $f(u)$ is uniform on $[M]$ and
$\Pr[\theta(f(u))=1]=p_\theta$ exactly. Hoeffding's inequality with
$\lambda:=k_1k_2t(k_1,k_2)$ gives conditional failure probability at most
$2\exp(-2\lambda^{2}/n_0)\le2\exp(-2t^{2}k_1k_2)$, uniformly in $(S_0,w)$, hence also
unconditionally.

**(3)** By the definition of $t$,
$2\exp(-2t^{2}k_1k_2)=2\,e^{-k_1\ln\frac{eN}{k_1}}e^{-k_2\ln\frac{eN}{k_2}}2^{-(\sigma+2)}\frac{\gamma_0}{4N^{2}}$.
There are $|\mathcal Z|\binom{N}{k_1}\binom{N}{k_2}$ tuples with the given $(k_1,k_2)$;
$\binom{N}{k}\le(eN/k)^{k}$ and $|\mathcal Z|<2^{\sigma+2}$ cancel the three exponential
factors, leaving at most $\gamma_0/(2N^{2})$ per pair $(k_1,k_2)$ and $\gamma_0/2$ in total.

**(4)** $t^{2}=\frac{\ln(eN/k_1)}{2k_2}+\frac{\ln(eN/k_2)}{2k_1}+\frac{C_0}{2k_1k_2}
\le\frac{L}{2k_2}+\frac{L}{2k_1}+\frac{C_0}{2k_1k_2}$ since $k_i\ge1$, and $1/k_i\le2m_i$
by Lemma 2 bounds the three terms by $Lm_2$, $Lm_1$, $2C_0m_1m_2$.

**(5)** By concavity of $\sqrt{\cdot}$ and Lemma 1(ii),(iii),
$\mathbb E[t]\le\sqrt{L(\mathbb E m_1+\mathbb E m_2)+2C_0\mathbb E[m_1m_2]}\le\sqrt{2\delta(L+C_0)}$.
Numerically $L+C_0=1+\ln N+(\sigma+2)\ln2+\ln4+2\ln N+\ln\gamma_0^{-1}\le3\ln N+0.694\sigma+3.78+\ln\gamma_0^{-1}$;
as $\sigma'\ge2.885\ln N$ and $\sigma'\ge2$ for $N\ge2$, this is at most
$3.63\sigma'+\ln\gamma_0^{-1}$, whence $\mathbb E[t]\le\sqrt{8\delta(\sigma'+\log\gamma_0^{-1})}$. $\square$

**$M$ occurs nowhere in $t$.** The alphabet enters only through $p_\theta$, which cancels,
and through the i.i.d. structure of $\{f(u)\}$, which is alphabet-blind. There are $2^{M}$
possible tests, but once the observer is fixed and the revealed values are conditioned
away, only $|\mathcal Z|<2^{\sigma+2}$ of them are reached.

**Where one source would break this.** Not in the size of $t$: at $k_1=1,k_2=N$ one gets
$t(1,N)^{2}=(L+N+C_0)/(2N)\to\tfrac12$, so $t\to1/\sqrt2$, which is neither large nor
vacuous — and in any case $k_1=1$ models a *deterministic first coordinate*, not a single
source. The failure is earlier and total. A single source emits a point of $[N]^{2}$ whose
posterior given the oracle and the leakage need not factor at all; Lemma 1(i) is then
unavailable, so a cell carries mass up to $\delta$ rather than $m_1m_2$, and there is no
product measure for Lemma 2 to flatten onto a rectangle. Lemmas 2 and 3 have no input, and
the argument does not begin. This is the visible failure Remark `rem:ell1` of the Contract
demands.

## 4. The observer as a revealing rule, and the mass of the revealed set

Say $D$ has **challenge resolution $M'$** if there is $h:[M]\to[M']$ such that for all
$f,\zeta$ and all $v,v'$ with $h(v)=h(v')$, the runs $D^{f}(v,\zeta)$ and $D^{f}(v',\zeta)$
issue the same sequence of query *positions*; the output bit is unconstrained. Every $D$
has resolution $M$; resolution $1$ means the query positions ignore the challenge value.

**Lemma 4.** Let $D$ be deterministic, $q$-query, challenge-oblivious, of resolution $M'$.
Then the procedures "$\mathcal A_\zeta$: for $j=1,\dots,M'$ run $D^{f}(v_j,\zeta)$ for a
fixed $v_j\in h^{-1}(j)$, inspecting each queried cell not already known" form a revealing
rule of budget $s=\min(qM',N^{2})$, with $\theta_{\zeta,f}(v):=D^{f}(v,\zeta)$.

*Proof.* $\mathcal A_\zeta$ inspects one coordinate at a time, the next being a function of
$\zeta$ and the values already seen: the loop and the representatives are fixed in advance,
and inside run $j$ the next position is a function of $(v_j,\zeta)$ and previous answers.
Each of the $M'$ runs issues at most $q$ positions, so at most $qM'$ cells, and at most
$N^{2}$ exist. Finally, for arbitrary $v$ with $j=h(v)$, the run $D^{f}(v,\zeta)$ issues
exactly the positions run $j$ issued, all inspected and recorded, so its whole execution —
hence its output bit — is reconstructible from $(v,\zeta,\mathcal S,f|_{\mathcal S})$.
Therefore the entire function $\theta_{\zeta,f}$, and $p_{\theta_{\zeta,f}}$, is determined
by $(\zeta,\mathcal S,f|_{\mathcal S})$. $\square$

**Lemma 5.** For a revealing rule of budget $s\ge1$,
$\mathbb E[\min(\Pi_{f,\zeta}(\mathcal S(f,\zeta)),1)]\le\mu(s):=\min(s\delta,\ 3(s\delta^{2})^{1/3},\ 1)$;
for $s=0$ the left side is $0$.

*Proof.* By Lemma 1(i), $\Pi(\mathcal S)=\sum_{\mathbf u\in\mathcal S}\pi^1(u_1)\pi^2(u_2)\le s\,m_1m_2$.
Taking expectations and using Lemma 1(iii) gives the arm $s\delta$; the arm $1$ is trivial.
For the third, fix $\theta\in(0,1]$, bound by $s\theta$ on $\{m_1m_2\le\theta\}$ and by $1$
off it, and use Lemma 1(iv): $\mathbb E[\min(\Pi(\mathcal S),1)]\le g(\theta):=s\theta+2\delta\theta^{-1/2}$.
Then $g'(\theta)=s-\delta\theta^{-3/2}$ vanishes at $\theta^{*}=(\delta/s)^{2/3}$, which is
$\le1$ since $s\ge1\ge\delta$, and $g''>0$; and
$g(\theta^{*})=s^{1/3}\delta^{2/3}+2s^{1/3}\delta^{2/3}=3(s\delta^{2})^{1/3}$. $\square$

The bound $s\delta^{2}$, which would be available if $\mathbb E[m_1m_2]\le\delta^{2}$, is
**not** available: see the counterexample in Section 1. The exponent $1/3$ is exactly what
the $\sqrt\theta$ of Lemma 1(iv) produces, and Lemma 5 is tight at $s=1$ for that example.

## 5. Bounds on the extraction advantage

**Claim 6.1.** For deterministic $D$ with associated $\theta_{\zeta,f}$,
$\Pr[\mathsf{Real}=1]=\mathbb E_{(f,\zeta)}\bigl[\mathbb E_{\mathbf x\sim\Pi_{f,\zeta}}[\theta_{\zeta,f}(f(\mathbf x))]\bigr]$
and $\Pr[\mathsf{Real}_0=1]=\mathbb E_{(f,\zeta)}[p_{\theta_{\zeta,f}}]$.

*Proof.* Condition on $(H,\mathbf z)=(f,\zeta)$. In both experiments $D$'s oracle is $f$, so
its output on challenge $v$ is $\theta_{\zeta,f}(v)$. In $\mathsf{Real}$ the challenge is
$f(\mathbf x)$ with $\mathbf x\sim\Pi_{f,\zeta}$ by Lemma 1; in $\mathsf{Real}_0$ it is
uniform and independent, with $\mathbb E_{v\gets_{\$}[M]}[\theta(v)]=p_\theta$. $\square$

So $\mathsf{Real}$ and $\mathsf{Real}_0$ differ in the challenge alone, the oracle being the
true $H$ in both.

**Proposition 6.2.** For every $\gamma_0\in(0,1)$ and deterministic $q$-query
challenge-oblivious $D$ of resolution $M'$,
$$\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|\le\gamma_0+\sqrt{8\delta(\sigma'+\log\gamma_0^{-1})}+\mu\bigl(\min(qM',N^{2})\bigr).$$

*Proof.* By Claim 6.1 and the triangle inequality the left side is at most
$\mathbb E[\Delta]$ with $\Delta(f,\zeta):=|\mathbb E_{\Pi}[\theta(f(\mathbf x))-p_\theta]|$.
Put $G_{f,\zeta}(\mathbf u):=(\theta(f(\mathbf u))-p_\theta)\mathbb 1[\mathbf u\notin\mathcal S(f,\zeta)]\in[-1,1]$,
so that $\Delta\le|\mathbb E_{\Pi}[G_{f,\zeta}]|+\Pi(\mathcal S)$. Lemma 2 bounds
$|\mathbb E_{\Pi}[G]|$ by the largest $|\mathbb E_{\mathrm{Unif}(B_1)\otimes\mathrm{Unif}(B_2)}[G]|$
over $|B_i|=k_i=\lfloor1/m_i\rfloor$, and for such a rectangle that quantity equals
$\bigl|\frac{1}{k_1k_2}\sum_{\mathbf u\in R\setminus\mathcal S}(\theta(f(\mathbf u))-p_\theta)\bigr|$,
which on the event $\mathcal E$ of Lemma 3 is at most $t(k_1,k_2)$. As $\Delta\le1$ always,
$\mathbb E[\Delta]\le\Pr[\mathcal E^{c}]+\mathbb E[t]+\mathbb E[\min(\Pi(\mathcal S),1)]$,
and the three terms are bounded by $\gamma_0$, by Lemma 3's last display, and by $\mu(s)$
via Lemmas 4 and 5. $\square$

**Theorem A.** $\kappa^{\mathrm{na}}(q)\le5\sqrt{\sigma'\delta}+q\delta$, and $\kappa(0)\le5\sqrt{\sigma'\delta}$.

*Proof.* Both $\kappa^{\mathrm{na}}(q)$ and $\kappa(0)$ are suprema over observers the
Contract permits to randomise, whereas Proposition 6.2 is stated for deterministic $D$; by
Lemma 0 the suprema are attained on deterministic observers, and $D'=D_{\rho^{*}}$ inherits
$D$'s challenge resolution, so restricting to deterministic resolution-$1$ observers loses
nothing. If $\delta=1$ then $\sqrt{\sigma'\delta}\ge\sqrt2>1$ and there is nothing to prove;
else take $\gamma_0:=\delta$ in Proposition 6.2. Since $\delta\ge1/N$ we get
$\log\gamma_0^{-1}\le\log N\le\sigma'/2$, so the middle term is at most
$\sqrt{12\sigma'\delta}\le3.47\sqrt{\sigma'\delta}$, and $\gamma_0=\delta\le\sqrt{\sigma'\delta}$
as $\delta\le1\le\sigma'$. Resolution $1$ gives $s\le q$ and $\mu(q)\le q\delta$. For $q=0$,
$s=0$ and every observer has resolution $1$ vacuously. $\square$

**Corollary A$'$.** If $q^{+}\delta\le\sigma'$ then $\kappa^{\mathrm{na}}(q)\le6\sqrt{\sigma'q^{+}\delta}$.
Outside that regime $q^{+}\delta>\sigma'\ge2$, so $\sqrt{\sigma'q^{+}\delta}>\sigma'>1$ and the
target bound is vacuous.

**Theorem B.** $\kappa(q)\le5\sqrt{\sigma'\delta}+\mu(\min(qM,N^{2}))$ for every $q$ and every
$q$-query challenge-oblivious observer.

*Proof.* By Lemma 0 the supremum defining $\kappa(q)$ is attained on deterministic
observers; apply Proposition 6.2 to such a $D$ with $M'=M$ and $\gamma_0=\delta$, as in
Theorem A. $\square$

**Corollary B$'$.** $\kappa(q)\le6\sqrt{\sigma'q^{+}\delta}$ whenever $q^{+}\delta\le\sigma'$ and
either $M\le\sqrt{\sigma'/(q\delta)}$ or $M\le\sigma'^{3/2}\sqrt{q/\delta}/27$.

*Proof.* $qM\delta\le\sqrt{\sigma'q^{+}\delta}$ follows from $qM^{2}\delta\le\sigma'$; and
$3(qM\delta^{2})^{1/3}\le\sqrt{\sigma'q^{+}\delta}$ follows from $27qM\delta^{1/2}\le\sigma'^{3/2}q^{3/2}$. $\square$

**Corollary B$''$.** If $M\le\sigma'/\sqrt{27\delta}$ then the hypothesis of Corollary B$'$
holds for every $q\ge1$.

*Proof.* The first arm fails only if $q>\sigma'/(M^{2}\delta)$ and the second only if
$q<729M^{2}\delta/\sigma'^{3}$; both fail at some $q$ only if $\sigma'^{4}<729M^{4}\delta^{2}$,
i.e. $M>\sigma'/\sqrt{27\delta}$. $\square$

## 6. Presampling, in oracle-indexed consistent form

**Lemma P.** Let $N\ge2$, $M\ge2$, $P\in\mathbb N$, $\gamma\in(0,1)$. (For $M=1$,
$\mathsf{Fun}$ is a singleton, so $\mathsf{Real}_0$ and $\mathsf{Dec}_0$ are the same
experiment and the bound holds with left side $0$; the construction below divides by
$\log M$ and is stated for $M\ge2$ only.) There is a family
$\mathcal Y^{P,\gamma}=\{Y_{f,\zeta}\}$ indexed by $f\in\mathsf{Fun}$ and
$\zeta\in\{0,1\}^{*}\times\{0,1\}^{*}$, depending only on $(S_1,S_2,P,\gamma)$, in which
every $Y_{f,\zeta}$ is a $P$-mixture consistent with $f$ — indeed a single $P$-bit-fixing
source — such that for every $q$ and every $q$-query observer taking $\mathbf z$ and an
independent uniform value of $[M]$,
$$\bigl|\Pr[\mathsf{Real}_0=1]-\Pr[\mathsf{Dec}_0=1]\bigr|\le\frac{q(\sigma+2+2\log\gamma^{-1})}{P}+2\gamma.$$

*Proof.* **Step 1.** For $\zeta$ with $\Pr[\mathbf z=\zeta]>0$ let $\mu_\zeta$ be the law of
$H$ given $\mathbf z=\zeta$ and $S_\zeta:=N^{2}\log M-H_\infty(\mu_\zeta)$. Since
$\mu_\zeta(f)=\Pr[H=f]\Pr[\mathbf z=\zeta\mid H=f]/\Pr[\mathbf z=\zeta]\le(|\mathsf{Fun}|\Pr[\mathbf z=\zeta])^{-1}$,
we get $S_\zeta\le\log(1/\Pr[\mathbf z=\zeta])$. With $\bar S:=\sigma+2+\log\gamma^{-1}$ and
$\mathcal B:=\{\zeta:S_\zeta>\bar S\}$, every $\zeta\in\mathcal B$ has
$\Pr[\mathbf z=\zeta]<\gamma2^{-(\sigma+2)}$, so $\Pr[\mathbf z\in\mathcal B]<|\mathcal Z|\gamma2^{-(\sigma+2)}<\gamma$.

**Step 2.** Fix $\zeta$ and set $\delta_\zeta:=(S_\zeta+\log\gamma^{-1})/(P\log M)$. If
$\delta_\zeta>1$ the asserted bound exceeds $q\log M\ge q$, hence is vacuous for $q\ge1$,
and for $q=0$ both experiments give the observer a uniform challenge and no oracle access;
set $Y_{f,\zeta}$ uniform. Otherwise apply the decomposition [CDGS, Claim 2] to $\mu_\zeta$
with parameter $\delta_\zeta$; since $(S_\zeta+\log\gamma^{-1})/(\delta_\zeta\log M)=P$ it yields
$\mu_\zeta=\sum_j\lambda_j X_j+\lambda_{\mathrm{fin}}Y_{\mathrm{fin}}$ with
$\lambda_{\mathrm{fin}}\le\gamma$, each $X_j$ a $(P,1-\delta_\zeta)$-dense source, all supports
pairwise disjoint, and each $X_j$ fixing its set $I_j$, $|I_j|\le P$, to values that every
$f$ in its support takes. Let $Y_j$ be the corresponding $P$-bit-fixing source and define
$Y_{f,\zeta}:=Y_j$ for the unique $j$ with $f\in\mathrm{supp}\,X_j$, and $Y_{f,\zeta}:=$ uniform
otherwise. Consistency is immediate; the construction reads only $(f,\zeta)$ and the
decomposition, which depends only on $(S_1,S_2,P,\gamma)$. Write $J=J(f,\zeta)$.

**Step 3.** Fix $\zeta\notin\mathcal B$ with $\delta_\zeta\le1$, and condition on $J=j$.
Since $\lambda_jX_j$ is the restriction of $\mu_\zeta$ to $\mathrm{supp}\,X_j$, the conditional
law of $H$ is exactly $X_j$; in $\mathsf{Dec}_0$ the oracle is drawn freshly from $Y_j$.
The challenge is uniform and independent, so conditioning on it leaves a fixed $q$-query
adaptive distinguisher between $X_j$ and $Y_j$; [CDGS, Claim 3] bounds its advantage by
$q\delta_\zeta\log M=q(S_\zeta+\log\gamma^{-1})/P$, and averaging over the challenge preserves this.

**Step 4.** Averaging over $j$ and bounding the residue event, of conditional probability at
most $\gamma$, by $1$, then averaging over $\zeta$ and bounding $\mathcal B$'s contribution
by $\Pr[\mathbf z\in\mathcal B]<\gamma$ while using $S_\zeta\le\bar S$ off $\mathcal B$, gives
the claim. $\square$

## 7. From extraction to decomposition

**Theorem C.** With $\mathcal Y:=\mathcal Y^{P,\gamma/2}$, for every $q$ and every $q$-query
challenge-oblivious $D$, writing $\varepsilon(D):=\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|$
for that same $D$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \varepsilon(D)+\frac{2(\sigma'+\log\gamma^{-1})q}{P}+\gamma+P\delta+q\delta.$$
Since $\varepsilon(D)\le\kappa(q)$ for every such $D$, the same bound holds with $\kappa(q)$
in place of $\varepsilon(D)$; but the $D$-relative form is the one Theorem C$'$ uses, and the
inequality $\kappa(q)\le\kappa^{\mathrm{na}}(q)$ is false in general and is nowhere needed.

*Proof.* Interpolate $\mathsf G_0=\mathsf{Real}$, $\mathsf G_1=\mathsf{Real}_0$,
$\mathsf G_2=\mathsf{Dec}_0$, $\mathsf G_3=\mathsf{Dec}$.

$|\mathsf G_0-\mathsf G_1|=\varepsilon(D)$, by definition, for the fixed $D$ the theorem is
instantiated at; no supremum is taken here.

$|\mathsf G_1-\mathsf G_2|$: Lemma P with slack $\gamma/2$ gives
$q(\sigma+2+2\log(2/\gamma))/P+\gamma$; as $N\ge2$ gives $\sigma+2\le\sigma'$ and $\sigma'\ge2$,
the numerator is at most $2\sigma'+2\log\gamma^{-1}$. (For $q\ge P$ that term already exceeds
$2\sigma'>1$, so no hypothesis $q<P$ is needed.)

$|\mathsf G_2-\mathsf G_3|\le P\delta+q\delta$: draw $H$, $(\mathbf x,\mathbf z)$ and $J$ with
fixed set $I_J$; let $H^{\circ}\sim Y_J$ and $U\gets_{\$}[M]$ be independent of everything
else; let $H^{*}$ be $H^{\circ}$ with its value at $\mathbf x$ overwritten by $U$ when
$\mathbf x\notin I_J$. As $J$ is a function of $(H,\mathbf z)$, $H^{\circ}$ is independent of
$\mathbf x$ given $(H,\mathbf z,J)$; conditioning on $\mathbf x=\mathbf u\notin I_J$, the
source $Y_J$ is uniform and independent at $\mathbf u$, so both $H^{\circ}$ and $H^{*}$ are
distributed as $Y_J$. Running $\mathsf G_3$ with oracle $H^{*}$ and $\mathsf G_2$ with oracle
$H^{\circ}$ and challenge $U$, the two executions receive the same input on
$\{\mathbf x\notin I_J\}$, since there $H^{*}(\mathbf x)=U$, and their oracles agree off
$\mathbf x$. So they diverge only if $\mathbf x\in I_J$ or $D$ queries $\mathbf x$; being
identical up to the step before a first query at $\mathbf x$, that event has equal
probability in both and may be measured in $\mathsf G_2$. The Contract's Lemma
"the fixed set misses the challenge" gives $\Pr[\mathbf x\in I_J]\le P\delta$ — its proof
requires only that $\mathcal Y$ depend on $(S_1,S_2,P,\gamma)$ alone, be indexed by
$(f,\zeta)$, and have its component drawn independently of $\mathbf x$ given $(H,\mathbf z)$,
all of which hold, $J$ being a function of $(H,\mathbf z)$. The Contract's Lemma "the
observer misses the challenge" gives $\Pr[\mathbf x\in Q]\le q\delta$ in $\mathsf G_2$, its
predictor being simulable because the challenge there is uniform and independent. $\square$

**Theorem C$'$.** Suppose $N\ge2$, $q^{+}\delta\le\sigma'$, $P\le\sqrt{\sigma'/\delta}$, and
either $D$ has challenge resolution $1$, or the hypothesis of Corollary B$'$ holds — in
particular if $M\le\sigma'/\sqrt{27\delta}$. Then with $\mathcal Y=\mathcal Y^{P,\gamma/2}$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}+8\sqrt{\sigma'q^{+}\delta}+\gamma,$$
that is, the Contract's conjecture holds on that region with $c=2$, $C=8$.

*Proof.* $\varepsilon(D)\le6\sqrt{\sigma'q^{+}\delta}$: in the first branch $D$ has
challenge resolution $1$, so $\varepsilon(D)\le\kappa^{\mathrm{na}}(q)$ and Corollary A$'$
applies — equivalently, Proposition 6.2 bounds $\varepsilon(D)$ directly at $M'=1$; in the
second branch Corollary B$'$ bounds $\kappa(q)\ge\varepsilon(D)$. Then
$P\delta\le\sqrt{\sigma'\delta}\le\sqrt{\sigma'q^{+}\delta}$ by the hypothesis on $P$;
$q\delta\le q^{+}\delta\le\sqrt{\sigma'q^{+}\delta}$ by $q^{+}\delta\le\sigma'$. $\square$

The family is built from $(P,\gamma)$ before $q$ and the bound holds for every $q$, so the
Contract's quantifier order is respected; and every $Y_{f,\zeta}$ is consistent with $f$,
so the conclusion is the Contract's conjecture, not the weakening its Remark on consistency
describes.

## 8. Combination with the compression bound

For $q\ge1$, [CFHS, Theorem 3] with $\ell=2$, $2^{-k}=\delta$, $q_D=q$ gives
$\kappa(q)=O(\log M\cdot(q\delta^{2}(\sigma+2N))^{1/3})$. Hence
$$\kappa(q)\le5\sqrt{\sigma'\delta}+\min\bigl\{\ \mu(\min(qM,N^{2})),\ \ O\bigl(\log M\,(q\delta^{2}(\sigma+2N))^{1/3}\bigr)\bigr\},$$
and Theorem C converts either arm. The arms are complementary: the first is smaller when
$M\lesssim N\log^{3}M$, the second when $M$ is very large relative to $N$; the second also
relaxes as $q$ grows, giving the target shape with no condition on $M$ once
$q\gtrsim\log^{6}M(\sigma+2N)^{2}\delta/\sigma'^{3}$. What neither arm reaches is $M$ large
together with $q$ small.

## 9. What is not proved

**Barrier 1: challenge-steered probes.** Uncovered: $M>\sigma'/\sqrt{27\delta}$ with $q$ in
the window left by Corollaries B$'$ and Section 8. This is not slack in the counting.
Lemma 3 compares $\mathbb E_\Pi[\theta(f(\mathbf x))]$ with $p_\theta$, an average over all
of $[M]$, so $\theta$ must be known everywhere; by Lemma 4 an observer that steers its
probes by the challenge makes $\theta(v)$ depend on $q$ cells varying with $v$, so all $qM$
must be revealed before the test is fixed; and Lemma 5 is then tight for what it is given,
because coordinatewise $\delta$-unpredictability does not yield $\mathbb E[m_1m_2]\le\delta^{2}$.
Two possible exits, neither taken here: replace the reference $p_\theta$ by
$\theta(f'(\mathbf x))$ for an independent copy $f'$ of $f$ off a single cell, which would
cut the budget from $qM$ to $q$ at the price of proving Lemma 3 for a random, $f$-dependent
reference; or bound $\Pi(\mathcal S)$ for *reachable* query sets — unions of $M$ decision-tree
paths — rather than arbitrary $qM$-sets.

**Barrier 2: large $P$ with growing $q$.** Theorem C loses $P\delta$ at $\mathsf G_2\to\mathsf G_3$,
capping the range at $P\le\sqrt{\sigma'/\delta}$. The slack is identifiable: on
$\{\mathbf x\in I_J\}$, which is what costs $P\delta$, consistency makes the decomposed
challenge $H^{*}(\mathbf x)$ equal the real challenge $H(\mathbf x)$, so the event does not
harm $\mathsf{Adv}_{\mathcal Y,D}$ at all — only the route through the uniform-challenge
worlds. A proof comparing $\mathsf G_3$ with $\mathsf G_0$ directly would not pay it.

## 10. External results used

- **[CDGS, Claim 2]** (Coretti, Dodis, Guo, Steinberger, *Random Oracles and Non-Uniformity*,
  ePrint 2017/937, Appendix A, p. 40). *Let $X_z$ be a distribution on $[M]^{n}$ with
  min-entropy deficiency $S_z$ and let $\gamma>0$. For every $\delta>0$, $X_z$ is
  $\gamma$-close to a convex combination of finitely many $(P',1-\delta)$-dense sources with
  $P'=(S_z+\log1/\gamma)/(\delta\log M)$.* The paper states this for $X_z=X\mid f(X)=z$ with
  $X$ uniform and $f$ deterministic; its proof uses only the min-entropy deficiency, and the
  form above is what that proof establishes. The proof's structure — conditioning on
  $\{Y_I=y_I\}$ and recursing on $\{Y_I\ne y_I\}$ — also supplies the disjointness of the
  components' supports and the fact that fixed values are values the sampled $f$ takes; both
  are used in Lemma P. Load-bearing for Lemma P, Theorem C, Theorem C$'$; not for Theorems A, B.
- **[CDGS, Claim 3]** (same paper, p. 11). *For any $(P',1-\delta)$-dense source $X'$ and its
  corresponding $P'$-bit-fixing source $Y'$, and any adaptive distinguisher $D$ querying at
  most $T$ coordinates, $|\Pr[D^{X'}=1]-\Pr[D^{Y'}=1]|\le T\delta\log M$.* Load-bearing for
  Lemma P.
- **[CFHS, Lemma 3]** (Coretti, Farshim, Harasser, Southern, *Multi-Source Randomness
  Extraction and Generation in the Random-Oracle Model*, ePrint 2025/1258, p. 8). *Let
  $k\in\mathbb R_{>0}$ with $2^{k}\in\mathbb N$. Then every $k$-source $X$ — meaning
  $\Pr[X=x]\le2^{-k}$ for all $x$ — is a convex combination of flat $k$-sources, i.e. of
  variables uniform on subsets of size $2^{k}$.* Load-bearing for Lemma 2.
- **[CFHS, Lemma 4.3]** (same page). *For $0<k\le n$, $(n/k)^{k}\le\binom nk\le(en/k)^{k}$.*
  Routine, used in Lemma 3.
- **[CFHS, Theorem 3]** (same paper, p. 28). *For every tuple of $\ell$ sources, each
  $(N^{\ell},2^{-k})$-unpredictable with unbounded oracle access, and every distinguisher
  making at most $q_D$ oracle calls, $\mathsf{Adv}^{\mathrm{mse}}=O(\ell\log M\sqrt[\ell+1]{q_D2^{-k\ell}(\sigma+\ell N)})$.*
  Used only for the second arm of Section 8, whose constant is therefore not explicit; its
  right-hand side vanishes at $q_D=0$ whereas $\kappa(0)>0$ in general, so it is invoked only
  for $q\ge1$.
- **Hoeffding's inequality**, in the form: for independent $X_1,\dots,X_n$ with $X_i$ taking
  values in an interval of length $c_i$, $\Pr[|\sum X_i-\mathbb E\sum X_i|\ge\lambda]\le2\exp(-2\lambda^{2}/\sum c_i^{2})$.
  Standard; used in Lemma 3 with $c_i=1$.

### END OF ARTIFACT split-decomp-kappa-1-r2 ###
