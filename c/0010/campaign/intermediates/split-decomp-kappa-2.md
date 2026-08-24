# A $q$-free bound for two split unpredictable sources, and the conjecture without the resolution hypothesis

Intermediate `split-decomp-kappa-2`. This artifact attacks **Barrier 1** of
`split-decomp-kappa-1-r3` §9 — challenge-steered probes — and closes it on a region that
strictly contains the region r3 covered for unrestricted observers. It does **not** supersede
r3. Its Lemma P and Theorem C are used here and are not reproved; its Theorems A and B are
strengthened, not replaced; its Lemmas 0–2 and Claim 6.1 are reproved from scratch below so
that the new results do not rest on an artifact that has yet to be blind-verified.

Two items raised by an in-session smell test are repaired in place: Lemma 0's clause (iii)
conjoined the two paired experiments where its proof supplies a maximiser per pair, and §0's
aside on (D) claimed of the collected corollary what holds only of the display. Neither is
load-bearing. The id is unchanged and no revision suffix is taken, because that test is not a
verification pass and no tally has ever been recorded against this content.

## 0. Goal

Fix $N,M\in\mathbb N$ with $N\ge2$, $M\ge2$, and let $\mathsf{Fun}:=\{f:[N]\times[N]\to[M]\}$
with $H\gets_{\$}\mathsf{Fun}$. Let $(S_1,S_2)$ be a split $\delta$-unpredictable pair of
sources with leakage bounded by $\sigma_1,\sigma_2$; put $\sigma:=\sigma_1+\sigma_2$,
$\sigma':=\sigma+2\log N$, $q^{+}:=q+1$. All logarithms are base two; $\ln$ is natural.
Definitions of source, splitness, unpredictability, $P$-bit-fixing source, $P$-mixture,
consistency, observer, challenge resolution, the experiments $\mathsf{Real}$, $\mathsf{Dec}$,
$\mathsf{Real}_0$, $\mathsf{Dec}_0$, the advantage $\mathsf{Adv}_{\mathcal Y,D}$ and the
extraction advantage $\kappa(q)$ are those of the Contract and of r3 §4, and are not repeated.
Write $\mathcal Z:=\{0,1\}^{\le\sigma_1}\times\{0,1\}^{\le\sigma_2}$, $L:=\ln(eN)$, and for
$c>0$
$$t_c(k_1,k_2)\;:=\;\sqrt{\frac{k_1\ln\frac{eN}{k_1}+k_2\ln\frac{eN}{k_2}+c}{2k_1k_2}}.$$

This document establishes five things.

**(D)** $\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|\le\gamma_0+\sqrt{2\delta\ln(eN)}+\delta\sqrt{2M\ln2+2\ln(4N^{2}/\gamma_0)}$
for **every** challenge-oblivious observer, of any query count — bounded or unbounded — and
any challenge resolution. Consequently $\kappa(q)\le5\sqrt{\sigma'\delta}+2\delta\sqrt M$ for
every $q$. The display mentions neither $q$ nor $\sigma$; the collected corollary is free of
$q$ and retains $\sigma$ only inside $\sigma'$.

**(A⁺, B⁺)** r3's Theorems A and B hold with $5\sqrt{\sigma'\delta}$ replaced by
$\sqrt{2\delta\ln(eN)}+4\delta\sqrt{\sigma'}$ and $\mu$ replaced by
$\mu'(s)=\min(s\delta,2(s\delta^{2})^{1/3},1)$ — smaller in both terms whenever $\delta<1$.

**(E)** The Contract's conjecture holds with the absolute constants $c=2$, $C=8$, for
**every** observer — no resolution hypothesis — whenever $P\le\sqrt{\sigma'/\delta}$,
$q^{+}\delta\le\sigma'$ and $M\le\sigma'q^{+}/(4\delta)$. This enlarges r3's unrestricted
region by the factor $1.299\,q^{+}/\sqrt\delta$.

**(F)** The new term $\delta\sqrt M$ is tight to within a factor $12$, already for
resolution-$1$ observers. No $q$-free bound can do better in $M$.

The conjecture in full is **not** proved. §8 states exactly what remains.

## 1. The two ideas

**Idea 1 — a second-moment sharpening.** Every bound in r3 that pays for the joint posterior
mass pays it as $\mathbb E[m_1m_2]\le\delta$ followed by concavity of $\sqrt\cdot$, yielding
$\sqrt\delta$. Cauchy–Schwarz applied to $\sqrt{m_1}\cdot\sqrt{m_2}$ instead gives
$\mathbb E[\sqrt{m_1m_2}]\le\sqrt{\mathbb E[m_1]\,\mathbb E[m_2]}\le\delta$, a factor
$\sqrt\delta$ better. This is where the second source's independence is spent a second time,
the first being the product structure itself. It is an equality on two structurally different
families (§2), so nothing is traded away.

**Idea 2 — drop the revealing rule.** r3 controls the $f$-dependence of the observer's test
$\theta_{\zeta,f}$ by *revealing* the $qM'$ cells that determine it and excising them, at cost
$\mu(\min(qM',N^{2}))$; the resolution $M'$ is the whole content of Barrier 1. Instead, prove
the rectangle-discrepancy bound simultaneously for **every** $\theta:[M]\to\{0,1\}$ and
substitute $\theta_{\zeta,f}$ afterwards. The union bound then costs $M\ln2$ inside the
numerator of $t$ and nothing else: no revealing rule, no excised set, no $\mu$, no resolution,
no $q$. Under Idea 1 that $M$ reaches the final bound as $\delta\sqrt M$, not $\sqrt{M\delta}$;
both halves are needed, since Lemma B alone run through r3's concavity step would give
$\sqrt{M\delta}$ and enlarge nothing.

## 2. Preliminaries

Throughout, $\mathbb E[\cdot]$ without a subscript is over $(f,\zeta)\sim(H,\mathbf z)$, and
$m_i=m_i(f,\zeta)$, $k_i=\lfloor1/m_i\rfloor$.

**Lemma 0 (derandomisation).** Fix one of the two paired experiments,
$(\mathsf{Real},\mathsf{Real}_0)$ or $(\mathsf{Real},\mathsf{Dec})$. For every
challenge-oblivious observer $D$ whose query count is bounded by $q\in\mathbb N\cup\{0\}$, or
unbounded, there is a deterministic challenge-oblivious $D'$ with (i) query count no larger
than $D$'s, (ii) the same challenge resolution as $D$, and (iii) the advantage *in that pair*
no larger for $D$ than for $D'$ — that is,
$\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|$ in the first case and
$\mathsf{Adv}_{\mathcal Y,D}$ in the second.

The maximiser is chosen per pair, and the two need not coincide: the lemma does **not** supply
a single $D'$ dominating both, and nothing below asks it to. Every appeal to it — in
Theorem D and in Theorems A⁺, B⁺ — is to the pair $(\mathsf{Real},\mathsf{Real}_0)$, and
Theorem C is stated for a fixed $D$ with no supremum taken, so $\mathsf{Adv}_{\mathcal Y,D}$ is
never bounded by passing to a derandomised observer.

*Proof.* Let $\rho$ be $D$'s coins and $D_\rho$ the deterministic strategy it then runs. A
deterministic strategy may be assumed never to repeat a query, replaying a recorded answer
changing no output and only lowering the query count; it is then a finite decision tree of
depth at most $\min(q,N^{2})$, branching over $[M]$, whose behaviour matters only on inputs in
$[M]\times\mathcal Z$, the experiments never feeding it a $\zeta$ outside the support of
$\mathbf z$. All of $[M],\mathcal Z,[N]^{2}$ being finite, there are finitely many such
strategies, so $\rho\mapsto D_\rho$ has finite image $\{s_1,\dots,s_n\}$.

Each quantity at issue is $\bigl|\Pr[\mathsf E_1=1]-\Pr[\mathsf E_0=1]\bigr|$ for a pair of
experiments drawing every component other than $\rho$ from the same joint law, with $\rho$
independent of every other draw: for $(\mathsf{Real},\mathsf{Real}_0)$ the two differ only in
the challenge, for $(\mathsf{Real},\mathsf{Dec})$ only in the oracle and challenge. So with
$\alpha(s):=\Pr[\mathsf E_1=1\mid D_\rho=s]-\Pr[\mathsf E_0=1\mid D_\rho=s]$,
$$\bigl|\Pr[\mathsf E_1=1]-\Pr[\mathsf E_0=1]\bigr|=\Bigl|\sum_{i}\Pr[D_\rho=s_i]\alpha(s_i)\Bigr|\le\max_i|\alpha(s_i)|,$$
a maximum over a finite set, attained at some $s^{*}=s^{*}(\mathsf E_0,\mathsf E_1)$; take
$D':=s^{*}$, giving (i) and (iii) for the pair fixed at the outset, and for that pair only.
For (ii), let $D$ have resolution $M'$ via $h$. The definition quantifies over *every* coin
string: for all $\rho,f,\zeta$ and all $v,v'$ with $h(v)=h(v')$, the runs
$D^{f}_{\rho}(v,\zeta)$ and $D^{f}_{\rho}(v',\zeta)$ issue the same query positions. Taking
$\rho$ with $D_\rho=s^{*}$ gives the property for $D'$, via the same $h$. $\square$

**Lemma 1 (posterior product structure).** For every $(f,\zeta)$ in the support of
$(H,\mathbf z)$ the conditional law of $\mathbf x$ is
$\Pi_{f,\zeta}=\pi^{1}_{f,\zeta_1}\otimes\pi^{2}_{f,\zeta_2}$, where
$\pi^{i}_{f,\zeta_i}(u)=\Pr[x_i=u\mid H=f,\;z_i=\zeta_i]$. With
$m_i:=\|\pi^{i}_{f,\zeta_i}\|_\infty$: (i) $\max_{\mathbf u}\Pi_{f,\zeta}(\mathbf u)=m_1m_2$;
(ii) $\mathbb E[m_i]\le\delta$ for $i=1,2$; (iii) $\mathbb E[m_1m_2]\le\delta$.

*Proof.* Conditioned on $H=f$, $(x_1,z_1)$ is a function of $f$ and $S_1$'s private coins and
$(x_2,z_2)$ of $f$ and $S_2$'s, and the coin strings are independent by splitness, so
$$\Pr[\mathbf x=\mathbf u,\mathbf z=\zeta\mid f]=\prod_{i}\Pr[x_i=u_i,z_i=\zeta_i\mid f].$$
Summing over $\mathbf u$ gives $\Pr[\mathbf z=\zeta\mid f]=\prod_i\Pr[z_i=\zeta_i\mid f]$,
positive because $(f,\zeta)$ is in the support, hence each factor is positive; dividing gives
the product form, and in particular the marginal of $x_i$ given $(H,\mathbf z)$ is
$\pi^{i}_{f,\zeta_i}$, which is Contract Remark `rem:vecz`. (i) is the fact that the maximum of
a product measure is the product of the maxima.

For (ii), let $\mathsf P$ be the predictor that, on input $\mathbf z$ with oracle access to
$H$, reads all of $H$ — permitted, predictors having unbounded query count — computes
$\pi^{i}_{H,z_i}$ and outputs its least maximiser $u^{*}(H,z_i)$; it may do this, the sources
being fixed and predictors being arbitrary, possibly randomised, functions of their inputs.
Conditioning on $(H,\mathbf z)=(f,\zeta)$, its output is the constant $u^{*}(f,\zeta_i)$ and,
by the marginal just computed, $\Pr[x_i=u^{*}\mid f,\zeta]=m_i$. Averaging,
$\Pr[\mathsf P^{H}(\mathbf z)=x_i]=\mathbb E[m_i]\le\delta$. (iii) follows from $m_2\le1$ and
(ii). $\square$

**Lemma 2 (flattening).** Let $\pi$ be a distribution on $[N]$ with $\|\pi\|_\infty=m$ and
$k:=\lfloor1/m\rfloor$. Then $1\le k\le N$, $1/k\le2m$, and $\pi$ is a convex combination of
distributions uniform on subsets of $[N]$ of size exactly $k$. Consequently, for every
$G:[N]^{2}\to[-1,1]$ and all $\pi^{1},\pi^{2}$ with $\|\pi^{i}\|_\infty=m_i$,
$k_i=\lfloor1/m_i\rfloor$,
$$\bigl|\mathbb E_{\pi^{1}\otimes\pi^{2}}[G]\bigr|\le\max\bigl\{\bigl|\mathbb E_{\mathrm{Unif}(B_1)\otimes\mathrm{Unif}(B_2)}[G]\bigr|:B_i\subseteq[N],\ |B_i|=k_i\bigr\}.$$

*Proof.* A distribution on $[N]$ has $m\ge1/N$, so $k\le N$; and $m\le1$ gives $k\ge1$. For
$x\ge1$, $\lfloor x\rfloor\ge x/2$: for $1\le x<2$ because $\lfloor x\rfloor=1\ge x/2$, for
$x\ge2$ because $\lfloor x\rfloor>x-1\ge x/2$. With $x=1/m$ this gives $1/k\le2m$. If $k=1$
then $\pi=\sum_u\pi(u)\delta_u$ is already a convex combination of uniforms on singletons and
no external result is needed. Assume $k\ge2$ and put $\lambda:=\log k$, so $\lambda>0$ and
$2^{\lambda}=k\in\mathbb N$; from $k\le1/m$ we get $\|\pi\|_\infty\le1/k=2^{-\lambda}$, so
$\pi$ is a $\lambda$-source and the flat-decomposition lemma [CFHS, Lemma 3] writes it as a
convex combination of distributions uniform on subsets of size $2^{\lambda}=k$, which exist in
$[N]$ since $k\le N$. For the display, write $\pi^{i}=\sum_j\alpha^i_j\mathrm{Unif}(B^i_j)$;
then $\pi^{1}\otimes\pi^{2}=\sum_{j,j'}\alpha^1_j\alpha^2_{j'}\mathrm{Unif}(B^1_j)\otimes\mathrm{Unif}(B^2_{j'})$,
so $\mathbb E_{\pi^1\otimes\pi^2}[G]$ is a convex combination of the quantities on the right.
No structure of $G$ is used beyond boundedness: the linearity exploited is in
$(\pi^{1},\pi^{2})$, not in $G$. $\square$

**Claim 3 (what the two real experiments compute).** For deterministic challenge-oblivious
$D$, writing $\theta_{\zeta,f}(v):=D^{f}(v,\zeta)$ and $p_\theta:=|\theta^{-1}(1)|/M$,
$$\Pr[\mathsf{Real}=1]=\mathbb E\bigl[\mathbb E_{\mathbf x\sim\Pi_{f,\zeta}}[\theta_{\zeta,f}(f(\mathbf x))]\bigr],\qquad\Pr[\mathsf{Real}_0=1]=\mathbb E\bigl[p_{\theta_{\zeta,f}}\bigr].$$

*Proof.* Condition on $(H,\mathbf z)=(f,\zeta)$. In both experiments $D$'s oracle is the real
$H=f$ and $D$ is deterministic, so its output on challenge input $v$ is $\theta_{\zeta,f}(v)$;
this is well defined precisely because $D$ is challenge-oblivious, its input being $(v,\zeta)$
and never $\mathbf x$. In $\mathsf{Real}$ the challenge is $f(\mathbf x)$ with
$\mathbf x\sim\Pi_{f,\zeta}$ by Lemma 1; in $\mathsf{Real}_0$ it is $y\gets_{\$}[M]$,
independent of everything, so the conditional expectation of the output is
$p_{\theta_{\zeta,f}}$. $\square$

## 3. The second-moment sharpening

**Lemma A.** With $m_1,m_2$ as in Lemma 1:

  (a) $\mathbb E[\sqrt{m_1m_2}]\le\delta$;
  (b) $\Pr[m_1m_2>\vartheta]\le\delta/\sqrt\vartheta$ for every $\vartheta\in(0,1]$;
  (c) pointwise, for $k_i=\lfloor1/m_i\rfloor$ and every $c>0$,
      $t_c(k_1,k_2)\le\sqrt{L(m_1+m_2)}+\sqrt{2c}\,\sqrt{m_1m_2}$;
  (d) $\mathbb E[t_c(k_1,k_2)]\le\sqrt{2L\delta}+\delta\sqrt{2c}$.

*Proof.* **(a)** $m_1,m_2$ are nonnegative and bounded by $1$, so all expectations are finite,
and by Cauchy–Schwarz and Lemma 1(ii) applied to each coordinate separately,
$\mathbb E[\sqrt{m_1}\cdot\sqrt{m_2}]\le\sqrt{\mathbb E[m_1]}\sqrt{\mathbb E[m_2]}\le\delta$.

**(b)** $m_1m_2>\vartheta$ iff $\sqrt{m_1m_2}>\sqrt\vartheta$; Markov and (a).

**(c)** $t_c^{2}=\frac{\ln(eN/k_1)}{2k_2}+\frac{\ln(eN/k_2)}{2k_1}+\frac{c}{2k_1k_2}$. Each
$k_i\ge1$, so $\ln(eN/k_i)\le L$; and $1/k_i\le2m_i$, so $\frac1{2k_i}\le m_i$ and
$\frac1{2k_1k_2}\le2m_1m_2$. Hence $t_c^{2}\le L(m_1+m_2)+2c\,m_1m_2$, and
$\sqrt{a+b}\le\sqrt a+\sqrt b$ gives the claim.

**(d)** Take expectations in (c). By concavity of $\sqrt\cdot$ and Lemma 1(ii),
$\mathbb E[\sqrt{L(m_1+m_2)}]\le\sqrt{L(\mathbb E m_1+\mathbb E m_2)}\le\sqrt{2L\delta}$; and
$\sqrt{2c}\,\mathbb E[\sqrt{m_1m_2}]\le\delta\sqrt{2c}$ by (a). $\square$

**Where the improvement lies.** r3 bounds the same quantity by
$\sqrt{L(\mathbb E m_1+\mathbb E m_2)+2c\,\mathbb E[m_1m_2]}\le\sqrt{2\delta(L+c)}$, using
concavity on the whole expression. Splitting first and applying Cauchy–Schwarz to the cross
term replaces $\sqrt{2c\delta}$ by $\delta\sqrt{2c}$. The stronger hypothesis
$\mathbb E[m_1m_2]\le\delta^{2}$, which would give the same conclusion directly, is **false**
(r3 §1), and (a) does not follow from $\mathbb E[m_1m_2]\le\delta$ by Jensen, which runs the
other way.

**(a) is an equality on two structurally different families.** In r3's §1 counterexample —
$2\le M\le N$, $E:=\{f(1,1)=1\}$, both sources outputting $1$ on $E$ and a uniform point off
it, leaking nothing — $m_1=m_2=1$ on $E$ and $=1/N$ off it, so
$\mathbb E[\sqrt{m_1m_2}]=\frac1M+(1-\frac1M)\frac1N=\mathbb E[m_i]$, the pair's exact
unpredictability parameter. In the flat family of §7, $m_1=m_2=1/N=\delta$ identically and
again $\mathbb E[\sqrt{m_1m_2}]=\delta$. The first has $m_1m_2$ with a heavy tail, the second
has it deterministic.

## 4. Universal rectangle discrepancy

**Lemma B.** Let $N\ge2$, $M\ge2$, $\gamma_0\in(0,1)$, and put
$C_1:=M\ln2+\ln\frac{4N^{2}}{\gamma_0}$. With probability at least $1-\gamma_0$ over
$f\gets_{\$}\mathsf{Fun}$, simultaneously for all $k_1,k_2\in[N]$, all $B_i\subseteq[N]$ with
$|B_i|=k_i$, and **all** $\theta:[M]\to\{0,1\}$, writing $R:=B_1\times B_2$,
$$\Bigl|\frac{1}{k_1k_2}\sum_{\mathbf u\in R}\bigl(\theta(f(\mathbf u))-p_\theta\bigr)\Bigr|\le t_{C_1}(k_1,k_2).$$

*Proof.* **(1)** Fix $k_1,k_2$, sets $B_i$ with $|B_i|=k_i$, and a function $\theta$ — all
fixed before $f$ is drawn. For $\mathbf u\in R$ put $Y_{\mathbf u}:=\theta(f(\mathbf u))-p_\theta$.
The coordinates of $f$ are i.i.d. uniform on $[M]$, so the $k_1k_2$ variables $Y_{\mathbf u}$
are independent; each has mean zero exactly, since
$\Pr[\theta(f(\mathbf u))=1]=|\theta^{-1}(1)|/M=p_\theta$; and each lies in
$\{-p_\theta,1-p_\theta\}$, an interval of length $1$. Hoeffding's inequality with
$\lambda:=k_1k_2\,t_{C_1}$ and all $c_i=1$ gives conditional failure probability at most
$2\exp(-2t_{C_1}^{2}k_1k_2)$.

**(2)** By the definition of $t_c$,
$2t_{C_1}^{2}k_1k_2=k_1\ln\frac{eN}{k_1}+k_2\ln\frac{eN}{k_2}+C_1$, so that bound equals
$2\bigl(\frac{eN}{k_1}\bigr)^{-k_1}\bigl(\frac{eN}{k_2}\bigr)^{-k_2}2^{-M}\frac{\gamma_0}{4N^{2}}$.

**(3)** For the fixed pair $(k_1,k_2)$ the number of tuples $(B_1,B_2,\theta)$ is
$\binom{N}{k_1}\binom{N}{k_2}2^{M}\le(\frac{eN}{k_1})^{k_1}(\frac{eN}{k_2})^{k_2}2^{M}$, by
$\binom nk\le(en/k)^{k}$ [CFHS, Lemma 4.3] and the fact that there are exactly $2^{M}$
functions $[M]\to\{0,1\}$. The three exponential factors cancel exactly, leaving at most
$\gamma_0/(2N^{2})$ per pair and $\gamma_0/2\le\gamma_0$ over the at most $N^{2}$ pairs. The
union is finite. $\square$

**Corollary B′.** With $\nu_R:=f_{*}\mathrm{Unif}(R)$, and since every subset of $[M]$ is
$\theta^{-1}(1)$ for exactly one $\theta$, Lemma B says: with probability at least $1-\gamma_0$
over $f$, every rectangle $R=B_1\times B_2$ satisfies
$\mathrm{SD}(\nu_R,\mathrm{Unif}([M]))\le t_{C_1}(|B_1|,|B_2|)$.

**The quantifier order is the mechanism.** The good event is a property of $f$ alone, and on
it the bound holds for every $\theta$ fixed in advance; substituting the particular
$\theta_{\zeta,f}$, which does depend on $f$, is legitimate because a statement "for all
$\theta$, $\Phi(f,\theta)\le t$" may be instantiated at any $\theta$ whatsoever. This is why no
conditioning on inspected values is needed, why the sum runs over all of $R$, and why no
revealing rule, budget, excised set or term $\Pi(\mathcal S)$ appears. r3's Lemmas 4 and 5 —
hence the entire cost of Barrier 1 — are bypassed rather than improved.

**The leakage has disappeared.** r3's Lemma 3 pays a factor $|\mathcal Z|<2^{\sigma+2}$ because
its test class is indexed by $\zeta$; here the class is all of $\{0,1\}^{[M]}$, which is
$\zeta$-free, so $C_1$ contains no $\sigma$. The trade is $\sigma+2\rightsquigarrow M$ inside a
budget paid at rate $\delta\sqrt{2C_1}$, i.e. $\delta\sqrt\sigma\rightsquigarrow\delta\sqrt M$
in the final bound, and not $\sqrt{\sigma\delta}\rightsquigarrow\sqrt{M\delta}$.

**No better union bound is available.** By Corollary B′ the object bounded is a statistical
distance, whose expectation over random $f$ is of order $\sqrt{M/(k_1k_2)}$ when
$M\le k_1k_2$, while $t_{C_1}\ge\sqrt{(M\ln2)/(2k_1k_2)}$. §7 turns this into a proof. What is
lossy — necessarily, and only for small $q$ — is bounding a $q$-query observer's advantage by
the full statistical distance in the first place.

**Where one source would break this.** With a single source emitting a point of $[N]^{2}$,
Lemma 1(i) is unavailable and Lemma 2 flattens onto an arbitrary subset $B\subseteq[N]^{2}$ of
size $k=\lfloor1/m\rfloor$, not onto a rectangle. Step (3) would then range over
$\binom{N^{2}}{k}\le(eN^{2}/k)^{k}$ sets, forcing
$t^{2}\ge\frac12\ln(eN^{2}/k)\ge\frac12$ since $k\le N^{2}$, so $t\ge1/\sqrt2$ and the
conclusion is vacuous, independently of $\delta$, $M$, $\sigma$. Lemma A(a) collapses likewise,
its Cauchy–Schwarz step being applied across the two coordinates. This is the visible
one-source failure Contract Remark `rem:ell1` demands, and it occurs before any bound on the
probability that a fixed set contains $\mathbf x$ is invoked, as that remark also requires.

## 5. A $q$-free bound on the extraction advantage

**Theorem D.** Let $N,M\ge2$ and $\gamma_0\in(0,1)$. For **every** challenge-oblivious observer
$D$ — of any query count, bounded or unbounded, and any challenge resolution —
$$\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|\le\gamma_0+\sqrt{2\delta\ln(eN)}+\delta\sqrt{2M\ln2+2\ln\tfrac{4N^{2}}{\gamma_0}}.$$

*Proof.* By Lemma 0 we may assume $D$ deterministic; Lemma 0 imposes no bound on the query
count, and nothing below refers to one. With $\theta_{\zeta,f}$ and $p_\theta$ as in Claim 3,
set $\Delta(f,\zeta):=\bigl|\mathbb E_{\mathbf u\sim\Pi_{f,\zeta}}[\theta_{\zeta,f}(f(\mathbf u))-p_{\theta_{\zeta,f}}]\bigr|$;
by Claim 3 and the triangle inequality the left side is at most $\mathbb E[\Delta]$.

Fix $(f,\zeta)$ in the support and put
$G_{f,\zeta}(\mathbf u):=\theta_{\zeta,f}(f(\mathbf u))-p_{\theta_{\zeta,f}}\in[-1,1]$. By
Lemma 1 the law $\Pi_{f,\zeta}$ is a product, so Lemma 2 applies with this $G$ and gives
$$\Delta(f,\zeta)\le\max_{|B_i|=k_i}\Bigl|\frac{1}{k_1k_2}\sum_{\mathbf u\in B_1\times B_2}\bigl(\theta_{\zeta,f}(f(\mathbf u))-p_{\theta_{\zeta,f}}\bigr)\Bigr|.$$
Let $\mathcal E$ be the event of Lemma B, a property of $f$ alone, of probability at least
$1-\gamma_0$; the marginal law of $f$ under $\mathbb E[\cdot]$ is uniform on $\mathsf{Fun}$. On
$\mathcal E$ the maximum is at most $t_{C_1}(k_1,k_2)$: the pair $(k_1,k_2)$ lies in
$[N]\times[N]$ by Lemma 2, the maximising $B_i$ are among the sets quantified over, and
$\theta_{\zeta,f}$ is one particular element of $\{0,1\}^{[M]}$, over all of which Lemma B
quantifies. Since $G\in[-1,1]$ gives $\Delta\le1$ pointwise, and $t_{C_1}\ge0$,
$$\mathbb E[\Delta]\le\Pr[\mathcal E^{c}]+\mathbb E[\mathbb 1_{\mathcal E}t_{C_1}]\le\gamma_0+\mathbb E[t_{C_1}]\le\gamma_0+\sqrt{2L\delta}+\delta\sqrt{2C_1},$$
by Lemma A(d) at $c=C_1$. $\square$

For $M=1$ the set $\mathsf{Fun}$ is a singleton and $\mathsf{Real}$, $\mathsf{Real}_0$ are the
same experiment, so the advantage is $0$ and the excluded case needs no bound.

**Corollary D′.** For every $q\in\mathbb N\cup\{0\}$,
$\kappa(q)\le5\sqrt{\sigma'\delta}+2\delta\sqrt M$, with no restriction on the observer.

*Proof.* If $\delta=1$ then $5\sqrt{\sigma'\delta}\ge5\sqrt2>1\ge\kappa(q)$; assume $\delta<1$
and take $\gamma_0:=\delta$. Recall $\delta\ge1/N$, $N\ge2$, and
$\sigma'\ge2\log N\ge2$, so $\ln N\le\frac{\ln2}{2}\sigma'\le0.3466\sigma'$ and
$1\le\sigma'/2$. Then $2\delta L=2\delta(1+\ln N)\le1.6932\sigma'\delta$, so
$\sqrt{2\delta L}\le1.3012\sqrt{\sigma'\delta}$; and, using $\ln(1/\delta)\le\ln N$,
$$2C_1=2M\ln2+2\ln4+4\ln N+2\ln\tfrac1\delta\le1.3863M+2.7726+6\ln N\le1.3863M+3.4657\sigma',$$
whence $\delta\sqrt{2C_1}\le1.1774\delta\sqrt M+1.8617\delta\sqrt{\sigma'}\le1.1774\delta\sqrt M+1.8617\sqrt{\sigma'\delta}$,
using $\delta\sqrt{\sigma'}=\sqrt\delta\sqrt{\sigma'\delta}\le\sqrt{\sigma'\delta}$. Finally
$\gamma_0=\delta\le\sqrt{\sigma'\delta}$ as $\delta\le1\le\sigma'$. Adding,
$(1+1.3012+1.8617)\sqrt{\sigma'\delta}+1.1774\delta\sqrt M\le5\sqrt{\sigma'\delta}+2\delta\sqrt M$. $\square$

## 6. The revealing-rule arm, sharpened

**Lemma C.** Let $\mathcal S(f,\zeta)\subseteq[N]^{2}$ be a function of $(f,\zeta)$ with
$|\mathcal S|\le s$. Then for $s\ge1$
$$\mathbb E\bigl[\min(\Pi_{f,\zeta}(\mathcal S(f,\zeta)),1)\bigr]\le\mu'(s):=\min\bigl(s\delta,\ 2(s\delta^{2})^{1/3},\ 1\bigr),$$
and the left side is $0$ for $s=0$.

*Proof.* By Lemma 1(i), $\Pi(\mathcal S)=\sum_{\mathbf u\in\mathcal S}\pi^1(u_1)\pi^2(u_2)\le s\,m_1m_2$;
expectations and Lemma 1(iii) give the arm $s\delta$, and the arm $1$ is trivial. For the
third, fix $\vartheta\in(0,1]$, bound by $s\vartheta$ on $\{m_1m_2\le\vartheta\}$ and by $1$
off it, and use Lemma A(b):
$\mathbb E[\min(\Pi(\mathcal S),1)]\le g(\vartheta):=s\vartheta+\delta\vartheta^{-1/2}$. Then
$g'(\vartheta)=s-\frac12\delta\vartheta^{-3/2}$ vanishes at $\vartheta^{*}=(\delta/2s)^{2/3}$,
which lies in $(0,1]$ since $\delta\le1\le2s$, and $g''>0$; and
$g(\vartheta^{*})=(2^{-2/3}+2^{1/3})(s\delta^{2})^{1/3}\le1.89(s\delta^{2})^{1/3}\le2(s\delta^{2})^{1/3}$. $\square$

This is r3's Lemma 5 with its Markov input replaced by Lemma A(b), improving the middle arm's
constant from $3$ to $2$. The arm $2(s\delta^{2})^{1/3}$ still cannot be improved to $s\delta^{2}$,
since $\mathbb E[m_1m_2]\le\delta^{2}$ is false.

**Theorems A⁺, B⁺.** *Granting* r3's Lemma 3, steps (1)–(3) — for a revealing rule of budget
$s$ and every $\gamma_0\in(0,1)$, with probability at least $1-\gamma_0$ over $f$,
simultaneously for all $\zeta\in\mathcal Z$, all $k_1,k_2\in[N]$ and all $|B_i|=k_i$,
$$\Bigl|\tfrac{1}{k_1k_2}\!\!\sum_{\mathbf u\in R\setminus\mathcal S(f,\zeta)}\!\!\bigl(\theta_{\zeta,f}(f(\mathbf u))-p_{\theta_{\zeta,f}}\bigr)\Bigr|\le t_{C_0}(k_1,k_2),\quad C_0:=(\sigma+2)\ln2+\ln\tfrac{4N^{2}}{\gamma_0},$$
— *and* r3's Lemma 4, that a deterministic $q$-query challenge-oblivious observer of resolution
$M'$ induces a revealing rule of budget $s=\min(qM',N^{2})$ with
$\theta_{\zeta,f}(v)=D^{f}(v,\zeta)$: for every $\gamma_0$ and every such $D$,
$$\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|\le\gamma_0+\sqrt{2\delta\ln(eN)}+\delta\sqrt{2C_0}+\mu'\bigl(\min(qM',N^{2})\bigr),$$
and at $\gamma_0=\delta$ this collects to
$$\kappa^{\mathrm{na}}(q)\le\sqrt{2\delta\ln(eN)}+4\delta\sqrt{\sigma'}+\mu'(q),\qquad
\kappa(q)\le\sqrt{2\delta\ln(eN)}+4\delta\sqrt{\sigma'}+\mu'\bigl(\min(qM,N^{2})\bigr),$$
the first at $M'=1$ and the second at $M'=M$; $\kappa(0)$ obeys the first, every observer
having resolution $1$ vacuously at $q=0$.

*Proof.* Run r3's Proposition 6.2 verbatim: with
$G_{f,\zeta}(\mathbf u):=(\theta(f(\mathbf u))-p_\theta)\mathbb 1[\mathbf u\notin\mathcal S(f,\zeta)]$
one has $\Delta\le|\mathbb E_\Pi[G]|+\Pi(\mathcal S)$; Lemma 2 bounds the first term by the
rectangle quantity above; and $\Delta\le1$ gives
$\mathbb E[\Delta]\le\Pr[\mathcal E^{c}]+\mathbb E[t_{C_0}]+\mathbb E[\min(\Pi(\mathcal S),1)]$,
whose three terms are $\gamma_0$, Lemma A(d) at $c=C_0$, and Lemma C. Lemma 0 reduces the
suprema to deterministic observers of unchanged resolution. Only the last two bounds differ
from r3, which uses $\sqrt{2\delta(L+C_0)}$ and $\mu$. For the collected forms take
$\gamma_0=\delta$, so $\ln(1/\delta)\le\ln N$ and
$2C_0\le1.3863\sigma+5.5452+6\ln N\le(1.3863+2.7726+2.0794)\sigma'=6.238\sigma'$, giving
$\delta\sqrt{2C_0}\le2.498\delta\sqrt{\sigma'}$; and $\gamma_0=\delta\le0.708\delta\sqrt{\sigma'}$,
the two together at most $3.21\delta\sqrt{\sigma'}\le4\delta\sqrt{\sigma'}$. $\square$

Against r3's $\kappa^{\mathrm{na}}(q)\le5\sqrt{\sigma'\delta}+q\delta$ this is smaller in both
terms whenever $\delta<1$: the $\sqrt{\sigma'}$ now carries $\delta$ rather than $\sqrt\delta$,
and $\mu'(q)\le q\delta$.

**Corollary D″.** $\kappa(q)\le5\sqrt{\sigma'\delta}+\min\{\mu'(\min(qM,N^{2})),\ 2\delta\sqrt M\}$,
the first arm granting the two inherited facts, the second unconditional. (Both leading parts
are at most $5\sqrt{\sigma'\delta}$: $4.164$ for the second arm by Corollary D′, and
$1.302\sqrt{\sigma'\delta}+3.21\delta\sqrt{\sigma'}+\delta\le4.9\sqrt{\sigma'\delta}$ for the
first.)

**Which arm wins.** Suppose $q\ge1$, $M\ge4$, and $2\delta\sqrt M<1$. Then the new arm is the
smaller: against $\mu'$'s arm $1$ immediately; against $2(s\delta^{2})^{1/3}$ with $s\le qM$
because $2\delta\sqrt M\le2(qM\delta^{2})^{1/3}$ iff $\delta\sqrt M\le q$, and
$\delta\sqrt M<1/2<q$; against $s\delta\le qM\delta$ because $q\sqrt M\ge2$. The cap
$s=N^{2}$ never binds usefully, since $\mu'(N^{2})=1$: both $N^{2}\delta\ge N\ge2$ and
$2(N\delta)^{2/3}\ge2$, as $\delta\ge1/N$. So for every $q\ge1$ and $M\ge4$ the new arm
dominates wherever either says anything; the old arm survives only at $q=0$, where
$\mu'(0)=0$ is exact and $\delta\sqrt M$ is pure loss, and in the corner $M\in\{2,3\}$.

## 7. From extraction to decomposition

**Theorem E.** Let $N,M\ge2$, $\gamma\in(0,1)$, and let $P\in\mathbb N$,
$q\in\mathbb N\cup\{0\}$ satisfy
$$P\le\sqrt{\sigma'/\delta},\qquad q^{+}\delta\le\sigma',\qquad M\le\frac{\sigma'q^{+}}{4\delta}.$$
Let $\mathcal Y:=\mathcal Y^{P,\gamma/2}$ be the family of r3's Lemma P — built from
$(S_1,S_2,P,\gamma)$ alone, before $q$, indexed by $(f,\zeta)$, each member a $P$-mixture
consistent with its index. Then for **every** $q$-query challenge-oblivious observer $D$, with
no restriction on challenge resolution,
$$\mathsf{Adv}_{\mathcal Y,D}\le\frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}+8\sqrt{\sigma'q^{+}\delta}+\gamma,$$
i.e. the Contract's conjecture holds on that region with $c=2$, $C=8$.

*Proof.* This is the only step that inherits an unproved result: r3's Theorem C, and the
Lemma P it rests on, are not reproved here. Granting them, with
$\varepsilon(D):=|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]|$ for the same fixed $D$,
$$\mathsf{Adv}_{\mathcal Y,D}\le\varepsilon(D)+\frac{2(\sigma'+\log\gamma^{-1})q}{P}+\gamma+P\delta+q\delta.$$
The second term is at most the target's first, as $q\le q^{+}$. Corollary D′ applies to $D$
with no hypothesis on it and gives $\varepsilon(D)\le5\sqrt{\sigma'\delta}+2\delta\sqrt M$;
here $5\sqrt{\sigma'\delta}\le5\sqrt{\sigma'q^{+}\delta}$, and $2\delta\sqrt M\le\sqrt{\sigma'q^{+}\delta}$
iff $M\le\sigma'q^{+}/(4\delta)$, the third hypothesis, so $\varepsilon(D)\le6\sqrt{\sigma'q^{+}\delta}$.
Next $P\delta\le\sqrt{\sigma'\delta}\le\sqrt{\sigma'q^{+}\delta}$ by the hypothesis on $P$, and
$q\delta\le q^{+}\delta=\sqrt{q^{+}\delta}\sqrt{q^{+}\delta}\le\sqrt{\sigma'}\sqrt{q^{+}\delta}$
by $q^{+}\delta\le\sigma'$. Adding, $6+1+1=8$. $\square$

The quantifier order of Contract Remark `rem:order` is respected: $\mathcal Y^{P,\gamma/2}$ is
fixed by $(S_1,S_2,P,\gamma)$ before $q$ is named. Consistency with the drawn $f$ is retained,
so the conclusion is the Contract's conjecture and not the weakening of its Remark `rem:uses`.

**Corollary E′ (what is gained over r3's Theorem C′).** r3 reaches the same conclusion, with
the same $c,C$ and the same conditions on $P$ and $q$, but requires in addition that either
$D$ have challenge resolution $1$, or $M\le\sigma'/\sqrt{27\delta}$. Theorem E requires
neither. The second branch is strictly contained, since $\sqrt{27\delta}\ge4\delta$ for
$\delta\le1$ gives $\sigma'q^{+}/(4\delta)\ge\sigma'/(4\delta)\ge\sigma'/\sqrt{27\delta}$, and
the ratio of thresholds is $\frac{\sqrt{27}}{4}\cdot\frac{q^{+}}{\sqrt\delta}=1.299\,q^{+}/\sqrt\delta$.
The first branch is dropped, not subsumed: it covers all $M$ for resolution-$1$ observers. What
is now known is the union — the conjecture holds with $c=2$, $C=8$ for (i) every observer when
$M\le\sigma'q^{+}/(4\delta)$, and (ii) every resolution-$1$ observer for arbitrary $M$ — and
Barrier 1 was exactly the gap between (i) and (ii), now closed on (i).

## 8. Tightness, and what is not proved

**Proposition F.** Let $N\ge2$ and $2\le M\le N^{2}/2$. Let $S_1$ and $S_2$ each draw
$x_i\gets_{\$}[N]$ on their own private coins and output $(x_i,\varepsilon)$. Then the pair is
split, $\sigma_1=\sigma_2=0$, $\sigma'=2\log N$, and it is $\delta$-unpredictable with
$\delta=1/N$. There is a deterministic challenge-oblivious observer $D^{*}$, making $N^{2}$
queries and of challenge resolution $1$, with
$$\bigl|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]\bigr|\ \ge\ \frac{\delta\sqrt M}{4\sqrt2}\ =\ \frac{\sqrt M}{4\sqrt2\,N}.$$

*Proof.* **(1)** The coins are independent, so the pair is split. Here
$\mathbf z=(\varepsilon,\varepsilon)$ always and each $x_i$ is uniform on $[N]$ and independent
of $H$ and of $x_{3-i}$. A predictor is an arbitrary, possibly randomised function of
$(\mathbf z,H)$, so its output is independent of $x_i$ and
$\Pr[\mathsf P^{H}(\mathbf z)=x_i]=1/N$ for every $\mathsf P$: the pair is
$\delta$-unpredictable exactly for $\delta=1/N$, the least value Definition `def:sources`
permits.

**(2)** $D^{*}$ queries all $N^{2}$ cells, so holds $f$; forms $\nu(v):=|f^{-1}(v)|/N^{2}$; and
on challenge $v$ outputs $\mathbb 1[\nu(v)>1/M]$. It is challenge-oblivious, deterministic,
makes $N^{2}$ queries, and its query positions are the same for every challenge value, so its
resolution is $1$.

**(3)** Condition on $H=f$. In $\mathsf{Real}$, $\mathbf x$ is uniform on $[N]^{2}$ and
independent of $f$, so the challenge $f(\mathbf x)$ has law exactly $\nu$; in
$\mathsf{Real}_0$ it is uniform on $[M]$. With $A_f:=\{v:\nu(v)>1/M\}$,
$$\Pr[\mathsf{Real}=1\mid f]-\Pr[\mathsf{Real}_0=1\mid f]=\sum_{v}\bigl(\nu(v)-\tfrac1M\bigr)^{+}=\mathrm{SD}\bigl(\nu,\mathrm{Unif}([M])\bigr)\ \ge 0,$$
so no cancellation occurs on averaging and the advantage equals
$\mathbb E_f[\mathrm{SD}(\nu,\mathrm{Unif}([M]))]$.

**(4)** *Claim: let $Y=\sum_{i=1}^{n}Y_i$ with $Y_i$ i.i.d., $\mathbb E Y_1=0$, $|Y_1|\le1$,
and $s^{2}:=\mathbb E Y^{2}=n\mathbb E Y_1^{2}$. If $s\ge1$ then $\mathbb E|Y|\ge s/2$.*
Discarding the terms with an index to an odd power, which vanish,
$\mathbb E Y^{4}=n\mathbb E Y_1^{4}+3n(n-1)(\mathbb E Y_1^{2})^{2}\le n\mathbb E Y_1^{2}+3n^{2}(\mathbb E Y_1^{2})^{2}=s^{2}+3s^{4}$,
using $\mathbb E Y_1^{4}\le\mathbb E Y_1^{2}$, valid as $|Y_1|\le1$. Hölder with exponents
$3/2$ and $3$ gives $s^{2}=\mathbb E[|Y|^{2/3}|Y|^{4/3}]\le(\mathbb E|Y|)^{2/3}(\mathbb E Y^{4})^{1/3}$,
so $\mathbb E|Y|\ge s^{3}/\sqrt{s^{2}+3s^{4}}\ge s^{3}/(2s^{2})=s/2$ for $s\ge1$.

**(5)** Put $n:=N^{2}$, $p:=1/M$, $X_v:=|f^{-1}(v)|$. Over uniform $f$ the summands
$\mathbb 1[f(\mathbf u)=v]$ are i.i.d. Bernoulli$(p)$, so $X_v\sim\mathrm{Bin}(n,p)$ and each
centred summand lies in $[-p,1-p]$, of absolute value at most $1$. As
$\mathrm{SD}(\nu,\mathrm{Unif}([M]))=\frac{1}{2n}\sum_v|X_v-np|$ and the $X_v$ are identically
distributed, $\mathbb E_f[\mathrm{SD}]=\frac{M}{2n}\mathbb E|X-np|$. Here
$s^{2}=np(1-p)=\frac{N^{2}}{M}(1-\frac1M)\ge\frac{N^{2}}{2M}$ for $M\ge2$, and $s^{2}\ge1$ since
$M\le N^{2}/2$, so (4) gives $\mathbb E|X-np|\ge\frac{N}{2\sqrt{2M}}$ and
$\mathbb E_f[\mathrm{SD}]\ge\frac{M}{2N^{2}}\cdot\frac{N}{2\sqrt{2M}}=\frac{\sqrt M}{4\sqrt2 N}$. $\square$

**Three consequences.**

*Corollary D′ is tight in $M$ to within a factor $12$.* On this family Corollary D′ gives
$\kappa(N^{2})\le5\sqrt{\sigma'\delta}+2\delta\sqrt M$ and Proposition F gives
$\kappa(N^{2})\ge\delta\sqrt M/(4\sqrt2)$; the $M$-terms differ by $8\sqrt2<12$. So **no
$q$-free bound can improve the $M$-dependence of Theorem D**: a smaller test class, a chaining
argument or a sharper concentration inequality cannot help, and any further progress must make
the bound depend on $q$.

*The residue is not about challenge resolution.* $D^{*}$ has resolution $1$, so the lower bound
applies to $\kappa^{\mathrm{na}}$ as well as $\kappa$. Consistently, Theorem A⁺ says nothing
here: $\mu'(N^{2})=1$.

*The Contract's $q^{+}$ is necessary, and the conjecture is not threatened.* At
$M=\lfloor N^{2}/2\rfloor$ the advantage is at least $\frac18$ while
$\sqrt{\sigma'\delta}=\sqrt{2\log N/N}\to0$, so no bound $\kappa(q)\le h(\sigma',\delta,N)$ free
of both $M$ and $q$ can hold. The Contract's target at those parameters reads
$C\sqrt{\sigma'q^{+}\delta}\ge C\sqrt{2N\log N}\gg1$ and is vacuous, so nothing is refuted.

**Barrier 1, restated after this artifact.** What remains uncovered is
$M>\sigma'q^{+}/(4\delta)$ for observers of resolution $>1$, intersected with the region where
neither $\mu'(\min(qM,N^{2}))$ nor r3 §8's compression arm reaches the target — that is, $M$
large together with $q$ *small*, which is exactly the corner r3 §8 already identified as
unreached. The sharp open question is whether
$$\kappa(q)\ \le\ O\bigl(\sqrt{\sigma'\delta}\bigr)+\mu'(q)$$
holds for unrestricted observers, i.e. whether the first arm can be made $M$-free. Both arms in
hand are individually tight — $\mu'$ on r3's §1 counterexample at $s=1$, and $\delta\sqrt M$ on
Proposition F — and nothing here claims their minimum is. An interpolation between the two
routes, revealing the runs for $v$ in a subset $T\subseteq[M]$ and union-bounding over the
$2^{M-|T|}$ completions, costs $\mu'(q|T|)+\delta\sqrt{2(C_0+(M-|T|)\ln2)}$ and gives nothing
beyond the endpoints up to constants: driving the first term below $1$ forces
$|T|\lesssim1/(q\delta^{2})$, which leaves $M-|T|=M(1-o(1))$ whenever $\delta\sqrt M\gtrsim1$.

## 9. Gap register

- **[INHERITED-UNAUDITED: r3 Theorem C, r3 Lemma P]** — *load-bearing*, for **Theorem E and
  Corollary E′ only**. `split-decomp-kappa-1-r3` has no findings file and has not been through
  blind review; its predecessors r1 and r2 have. Theorems D, A⁺, B⁺, Corollaries D′, D″ and
  Proposition F do not depend on it.
- **[INHERITED-UNAUDITED: r3 Lemma 3 steps (1)–(3), r3 Lemma 4]** — *load-bearing*, for
  **Theorems A⁺, B⁺ and the first arm of Corollary D″ only**. Not for Theorem D, Corollary D′,
  Theorem E or Proposition F.
- No `[GAP]` occurs in the arguments of §§2–5 and §8; they depend only on the two source cards
  and on standard inequalities restated in §10.

## 10. External results used

- **[CFHS, Lemma 3]** (Coretti, Farshim, Harasser, Southern, *Multi-Source Randomness
  Extraction and Generation in the Random-Oracle Model*, ePrint 2025/1258, p. 8). *Let
  $k\in\mathbb R_{>0}$ with $2^{k}\in\mathbb N$. Then every $k$-source $X$ — meaning
  $\Pr[X=x]\le2^{-k}$ for all $x$ — is a convex combination of flat $k$-sources, i.e. of
  variables uniform on subsets of size $2^{k}$.* CARD (S2). Load-bearing for Lemma 2, hence for
  everything below it.
- **[CFHS, Lemma 4.3]** (same page). *For $0<k\le n$, $(n/k)^{k}\le\binom nk\le(en/k)^{k}$.*
  CARD (S2). Used in Lemma B step (3).
- **Hoeffding's inequality**: for independent $X_1,\dots,X_n$ with $X_i$ taking values in an
  interval of length $c_i$, $\Pr[|\sum X_i-\mathbb E\sum X_i|\ge\lambda]\le2\exp(-2\lambda^{2}/\sum c_i^{2})$.
  RESTATED, standard; used in Lemma B with $c_i=1$.
- **Cauchy–Schwarz, Markov, Jensen, Hölder** (the last with exponents $3/2$ and $3$).
  RESTATED, standard; used in Lemma A, Lemma C and Proposition F(4).
- **[CDGS, Claim 2]** and **[CDGS, Claim 3]** (Coretti, Dodis, Guo, Steinberger, *Random Oracles
  and Non-Uniformity*, ePrint 2017/937). CARD (S1). They enter **only** through r3's Lemma P,
  i.e. transitively under the first inherited dependency above, and are not used directly here.

### END OF ARTIFACT split-decomp-kappa-2 ###
