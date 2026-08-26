# split-decomp-kappa-3 — reducing Theorem E's hypotheses, and locating the $P$-cap

Continues `split-decomp-kappa-2-r2` (Theorem E) and `split-decomp-kappa-1-r3` (Theorem C,
Lemma P). Nothing below is a new attack: every result here is a re-accounting of Theorem E's
own proof, and the point is that two of its three hypotheses are not doing work.

## 0. Goal

All notation is that of the Contract and of `split-decomp-kappa-2-r2` §0, unchanged:
$N,M\ge2$, $\mathsf{Fun}=\{f:[N]\times[N]\to[M]\}$, a split $\delta$-unpredictable pair
$(S_1,S_2)$ with leakage bounded by $\sigma_1,\sigma_2$, $\sigma:=\sigma_1+\sigma_2$,
$\sigma':=\sigma+2\log N$, $q^{+}:=q+1$, $\mu'(s):=\min(s\delta,2(s\delta^{2})^{1/3},1)$.
Logarithms are base two. $\mathcal Y^{P,\gamma}$ is the family of r3's Lemma P.

Theorem E of `split-decomp-kappa-2-r2` proves the Contract's conjecture with $c=2$, $C=8$ under
three hypotheses,
$$P\le\sqrt{\sigma'/\delta},\qquad q^{+}\delta\le\sigma',\qquad M\le\frac{\sigma'q^{+}}{4\delta}.$$
This document establishes three things.

**(G0)** The hypothesis $q^{+}\delta\le\sigma'$ may be **deleted**. It is implied by the
conclusion being non-vacuous.

**(G1)** The hypothesis $P\le\sqrt{\sigma'/\delta}$ may be **relaxed by a factor $\sqrt{q^{+}}$**,
to $P\le\sqrt{\sigma'q^{+}/\delta}$, with the same constants. This matters because
$\lceil\sqrt{\sigma'q^{+}/\delta}\,\rceil$ is exactly the $P$ at which the Contract's own
Theorem `thm:main` instantiates the conjecture: under Theorem E as stated, the Contract's
intended use of the conjecture sat a factor $\sqrt{q^{+}}$ **outside** the proved region, and
it no longer does.

**(G2)** The hypothesis $M\le\sigma'q^{+}/(4\delta)$ may be replaced by
$\min\{\mu'(\min(qM,N^{2})),\,2\delta\sqrt M\}\le\sqrt{\sigma'q^{+}\delta}$, using Corollary
D″ in place of Corollary D′. At $q=0$ that condition is **vacuous**, since $\mu'(0)=0$
exactly, so at $q=0$ the conjecture holds for **every** $M$ and every observer under the single
hypothesis $P\le3\sqrt{\sigma'/\delta}$.

The conjecture in full is still **not** proved. §4 states what the residual $P$-cap is, why it
is a defect of the proof route rather than of the statement, and — in Obstruction O1 — why the
obvious repair needs a new idea rather than more care. §5 is the gap register.

## 1. The third hypothesis is free

**Lemma G0.** Let $N\ge2$. If $8\sqrt{\sigma'q^{+}\delta}\ge1$ then the conclusion of Theorem E
holds trivially, its right-hand side being at least $1\ge\mathsf{Adv}_{\mathcal Y,D}$.
Otherwise $q^{+}\delta\le\sigma'$ holds automatically. Consequently Theorem E is true with the
hypothesis $q^{+}\delta\le\sigma'$ removed.

*Proof.* $\mathsf{Adv}_{\mathcal Y,D}$ is a difference of two probabilities, so
$\mathsf{Adv}_{\mathcal Y,D}\le1$; and the right-hand side
$2(\sigma'+\log\gamma^{-1})q^{+}/P+8\sqrt{\sigma'q^{+}\delta}+\gamma$ is at least
$8\sqrt{\sigma'q^{+}\delta}$, every summand being non-negative. That disposes of the first case.
In the second, $8\sqrt{\sigma'q^{+}\delta}<1$ gives $\sigma'q^{+}\delta<1/64$, hence
$q^{+}\delta<1/(64\sigma')$. Since $N\ge2$ gives $2\log N\ge2$ and $\sigma\ge0$, we have
$\sigma'\ge2$, so $q^{+}\delta<1/128<2\le\sigma'$. $\square$

This is the same device r3 uses in the second sentence of Corollary A$'$ ("outside that regime
$q^{+}\delta>\sigma'\ge2$, so $\sqrt{\sigma'q^{+}\delta}>\sigma'>1$ and the target bound is
vacuous"); it is recorded here because Theorem E carries the condition as a hypothesis rather
than discharging it.

## 2. The $P$-hypothesis relaxes by $\sqrt{q^{+}}$

**Theorem E″.** Let $N,M\ge2$, $\gamma\in(0,1)$, $P\in\mathbb N$, $q\in\mathbb N\cup\{0\}$, and
let $\mathcal Y:=\mathcal Y^{P,\gamma/2}$ be the family of r3's Lemma P — built from
$(S_1,S_2,P,\gamma)$ alone, before $q$, indexed by $(f,\zeta)$, each member a $P$-mixture
consistent with its index. Suppose

  **(H1)** $P\le\sqrt{\sigma'q^{+}/\delta}$, and

  **(H2)** $\min\bigl\{\mu'(\min(qM,N^{2})),\ 2\delta\sqrt M\bigr\}\le\sqrt{\sigma'q^{+}\delta}$.

Then for every $q$-query challenge-oblivious observer $D$, with no restriction on challenge
resolution,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}+8\sqrt{\sigma'q^{+}\delta}+\gamma,$$
i.e. the Contract's conjecture holds on that region with $c=2$, $C=8$.

*Proof.* By Lemma G0 we may assume $q^{+}\delta\le\sigma'$, the other case being trivial. As in
Theorem E, r3's Theorem C gives, for the same fixed $D$ and with
$\varepsilon(D):=|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]|$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \varepsilon(D)+\frac{2(\sigma'+\log\gamma^{-1})q}{P}+\gamma+P\delta+q\delta,$$
and the second term is at most the target's first, as $q\le q^{+}$. Four terms remain.

*The extraction term.* Corollary D″ applies to $D$ with no hypothesis on it and gives
$\varepsilon(D)\le\kappa(q)\le5\sqrt{\sigma'\delta}+\min\{\mu'(\min(qM,N^{2})),2\delta\sqrt M\}$.
Here $5\sqrt{\sigma'\delta}\le5\sqrt{\sigma'q^{+}\delta}$, and the minimum is at most
$\sqrt{\sigma'q^{+}\delta}$ by **(H2)**, so $\varepsilon(D)\le6\sqrt{\sigma'q^{+}\delta}$.

*The fixed-set term.* $P\delta\le\sqrt{\sigma'q^{+}\delta}$ **iff** $P^{2}\delta^{2}\le\sigma'q^{+}\delta$
**iff** $P\le\sqrt{\sigma'q^{+}/\delta}$, which is **(H1)**.

*The query term.* $q\delta\le q^{+}\delta=\sqrt{q^{+}\delta}\sqrt{q^{+}\delta}\le\sqrt{\sigma'}\sqrt{q^{+}\delta}=\sqrt{\sigma'q^{+}\delta}$
by $q^{+}\delta\le\sigma'$.

Adding, $6+1+1=8$. $\square$

**Remark (what changed, and what did not).** The only altered step is the fixed-set term.
Theorem E bounds $P\delta\le\sqrt{\sigma'\delta}\le\sqrt{\sigma'q^{+}\delta}$, passing through
the intermediate $\sqrt{\sigma'\delta}$ and paying $\sqrt{q^{+}}$ for the passage; the direct
inequality is what **(H1)** states. No constant moves. The quantifier order of Contract Remark
`rem:order` is respected exactly as in Theorem E: **(H1)** and **(H2)** are conditions on the
*region*, and $\mathcal Y^{P,\gamma/2}$ is still fixed by $(S_1,S_2,P,\gamma)$ before $q$ is
named. A $q$-dependent region is not a $q$-dependent family — Theorem E already relies on this,
its own third hypothesis $M\le\sigma'q^{+}/(4\delta)$ mentioning $q$.

**Corollary G1 (the proved region now contains the Contract's own instantiation).** The
Contract's `thm:main` proves $\kappa(q)\le(4c+2C+4)\sqrt{\sigma'q^{+}\delta}+q\delta$ by
instantiating the conjecture at $\gamma:=N^{-2}$ and $P:=\lceil\sqrt{\sigma'q^{+}/\delta}\,\rceil$.
Under Theorem E that $P$ exceeds the admissible range by a factor $\sqrt{q^{+}}$, so Theorem E
supplied `thm:main` only at $q=0$; capping $P$ at $\sqrt{\sigma'/\delta}$ instead yields
$\kappa(q)=O(q^{+}\sqrt{\sigma'\delta})$, weaker than the target by $\sqrt{q^{+}}$. Under
**(H1)** the range reaches $\sqrt{\sigma'q^{+}/\delta}$, so
$P:=\lfloor\sqrt{\sigma'q^{+}/\delta}\rfloor$ is admissible, and $\lfloor t\rfloor\ge t/2$ for
$t\ge1$ — with $t:=\sqrt{\sigma'q^{+}/\delta}\ge\sqrt2$ since $\sigma'\ge2$, $q^{+}\ge1$,
$\delta\le1$ — gives $\sigma'q^{+}/P\le2\sqrt{\sigma'q^{+}\delta}$ and hence, with
$\log\gamma^{-1}=2\log N\le\sigma'$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ 4\sigma'q^{+}/P+8\sqrt{\sigma'q^{+}\delta}+\gamma\ \le\ 16\sqrt{\sigma'q^{+}\delta}+\gamma\ \le\ 17\sqrt{\sigma'q^{+}\delta},$$
using $\gamma=N^{-2}\le\delta^{2}\le\delta\le\sqrt{\sigma'q^{+}\delta}$.

*This is a statement about the conjecture, not about $\kappa$.* On the region **(H2)**,
Corollary D″ already bounds $\kappa(q)\le6\sqrt{\sigma'q^{+}\delta}$ outright, with no $P$ and
no appeal to the conjecture, so the Contract's *consequence* was never the thing missing there.
What **(H1)** buys is that the *decomposition statement itself* is now proved at the parameter
a user following the Contract would instantiate it at. Under Theorem E as stated, anyone using
the conjecture as `thm:main` uses it was outside the proved region.

## 3. At $q=0$ there is no restriction on $M$

**Corollary G2.** Let $N,M\ge2$, $\gamma\in(0,1)$ and $P\le3\sqrt{\sigma'/\delta}$. Then for
every $0$-query challenge-oblivious observer, and every $M$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})}{P}+8\sqrt{\sigma'\delta}+\gamma.$$

*Proof.* **(H2)** at $q=0$ reads $\min\{\mu'(\min(0,N^{2})),2\delta\sqrt M\}=\min\{\mu'(0),2\delta\sqrt M\}$,
and $\mu'(0)=\min(0,0,1)=0$, so **(H2)** holds for every $M$. In r3's Theorem C at $q=0$ the
chain is $\mathsf{Adv}_{\mathcal Y,D}\le\varepsilon(D)+\gamma+P\delta$, the two $q$-carrying
terms vanishing. r3's Theorem A gives $\kappa(0)\le5\sqrt{\sigma'\delta}$ with no hypothesis on
$M$ and none on resolution — "for $q=0$, $s=0$ and every observer has resolution $1$
vacuously" — so $\varepsilon(D)\le5\sqrt{\sigma'\delta}$, leaving three units of the target's
$8\sqrt{\sigma'\delta}$ for $P\delta$: $P\delta\le3\sqrt{\sigma'\delta}$ iff
$P\le3\sqrt{\sigma'/\delta}$. $\square$

This strictly enlarges what `split-decomp-kappa-2-r2` §7 records as known ("the conjecture
holds for (i) every observer when $M\le\sigma'q^{+}/(4\delta)$, and (ii) every resolution-$1$
observer for arbitrary $M$"): at $q=0$ neither branch is needed, and the constant on the
$P$-cap improves by $3$.

## 4. The residual $P$-cap is a defect of the route, not of the statement

**Where it enters.** In r3's Theorem C the chain is
$\mathsf G_0=\mathsf{Real}$, $\mathsf G_1=\mathsf{Real}_0$, $\mathsf G_2=\mathsf{Dec}_0$,
$\mathsf G_3=\mathsf{Dec}$, and $P\delta$ appears **once**, in
$|\mathsf G_2-\mathsf G_3|\le P\delta+q\delta$, as the Contract's Lemma `lem:hit` bound
$\Pr[\mathbf x\in I_J]\le P\delta$. Every other term in Theorem E″'s proof is either $O(1/P)$
or $P$-free. So the whole of the $P$-cap is the requirement that $\Pr[\mathbf x\in I_J]$ be
absorbed into $\sqrt{\sigma'q^{+}\delta}$.

**Why the event is favourable, not adverse.** $\mathsf G_2\to\mathsf G_3$ replaces a uniform
independent challenge by $H^{*}(\mathbf x)$. On $\{\mathbf x\in I_J\}$ the fixed values of
$Y_{H,\mathbf z}$ agree with $H$ — this is *consistency*, Definition `def:bf` — so
$H^{*}(\mathbf x)=H(\mathbf x)$, which is exactly the challenge $\mathsf{Real}$ supplies. The
event on which the route pays $P\delta$ is the event on which $\mathsf{Dec}$'s challenge is
*correct*. The cost is incurred only because the route passes through $\mathsf{Dec}_0$, where
the challenge is uniform, and so must pay to put back a value it already had.

**The Contract says as much.** Remark `rem:uses` records that `thm:main` uses exactly three
features of the family and that "the consistency requirement of Definition `def:bf` is *not*
used anywhere in this section". That is precisely why the Contract's own derivation pays
$P\delta$: it discards the hypothesis that would make the payment unnecessary. r3's Theorem C
inherits the route and the cost.

**A candidate replacement.** Route $\mathsf{Real}\to\mathsf{Mid}\to\mathsf{Dec}$ with
$\mathsf{Mid}$ the experiment that draws $H,(\mathbf x,\mathbf z)$ as in $\mathsf{Real}$ and
$H^{*}\sample Y_{H,\mathbf z}$, and runs $D^{H^{*}}(H(\mathbf x),\mathbf z)$ — decomposed
oracle, *real* challenge. Then $|\mathsf{Mid}-\mathsf{Dec}|$ is supported on
$\{\mathbf x\notin I_J\}$, where the two challenges are $H(\mathbf u)$ and a fresh uniform
value at a point $\mathbf u$ off the fixed set. r3's Lemma P Step 2 supplies, via
[CDGS, Claim 2], that the conditional law of $H$ is a $(P,1-\delta_\zeta)$-dense source with
$\delta_\zeta\log M=(S_\zeta+\log\gamma^{-1})/P$; density at a single coordinate off the fixed
set gives $\Pr[H(\mathbf u)=v]\le M^{-(1-\delta_\zeta)}$, so
$$\mathrm{SD}\bigl(H(\mathbf u),\mathrm{Unif}([M])\bigr)\ \le\ M^{\delta_\zeta}-1\ \le\ \delta_\zeta\ln M\cdot M^{\delta_\zeta}\ \le\ 2\ln2\cdot\frac{S_\zeta+\log\gamma^{-1}}{P}$$
whenever $\delta_\zeta\log M\le1$ — where $M^{\delta_\zeta}=2^{\delta_\zeta\log M}\le2$ — i.e. whenever $P\ge S_\zeta+\log\gamma^{-1}$ — which is the
only regime in which the target's own first term is below $1$. So the replacement term is
$O\bigl((\sigma'+\log\gamma^{-1})/P\bigr)$: the *same shape as the target's first term*, and
decreasing in $P$ where $P\delta$ increases. If this route closes, the $P$-cap goes entirely.

**Three gaps, stated as gaps.** This is a candidate, not a proof.

- **(G-a)** The sources read the whole oracle, so $\mathbf x$ is not independent of $H$, and the
  single-coordinate density bound must be applied at a point correlated with the conditioning.
  `lem:hit` handles the analogous problem for *membership* in $I_J$ by exhibiting a predictor;
  the same device is needed here for the *value* at $\mathbf x$, and it is not obvious that the
  predictor formulation reaches it.
- **(G-b)** $|\mathsf{Real}-\mathsf{Mid}|$ has no bound yet. The observer there receives
  $H(\mathbf x)$, a value correlated with the very oracle it is distinguishing, whereas Lemma P
  bounds only the case of an independent uniform challenge. This is the load-bearing hop.
  **Obstruction O1 below shows it is not a bookkeeping gap.**
- **(G-c)** *Closed.* The density-to-statistical-distance step needs $(P,1-\delta)$-density at
  $|T|=1$. Source card `S1` records [CDGS, Definition 1] verbatim in substance: a source is
  $(1-\delta)$-dense if "for every subset $I\subseteq[N]$,
  $H_\infty(X_I)\ge(1-\delta)\cdot|I|\cdot\log M$", and $(P,1-\delta)$-dense if it "is fixed on
  at most $P$ coordinates and is $(1-\delta)$-dense on the rest". Singletons are included and
  the fixed coordinates are excluded, which is exactly the event $\mathbf x\notin I_J$ the step
  is applied on. So $\Pr[H(\mathbf u)=v]\le M^{-(1-\delta_\zeta)}$ for $\mathbf u\notin I_J$ is
  licensed as used.

**Obstruction O1 (why (G-b) needs a new idea).** Split on $E:=\{\mathbf x\in I_J\}$, an event
determined by $(H,\mathbf z,\mathbf x)$ before either experiment diverges, so of equal
probability in both. On $E$, consistency makes the challenge *literally identical*, not merely
equal in law: conditioning on $(H,\mathbf z,\mathbf x,J=j)$, $\mathsf{Real}$ runs
$D^{H}(v,\mathbf z)$ and $\mathsf{Dec}$ runs $D^{H^{*}}(v,\mathbf z)$ with the same
$v=H(\mathbf x)=H^{*}(\mathbf x)$. So the $E$-branch is a pure oracle swap, $X_j$ against
$Y_j$ — exactly what [CDGS, Claim 3] bounds — *except for the conditioning*. Three routes and
why each fails.

- **(a) Apply Claim 3 conditioned on $(\mathbf x,v)$.** The conditional law of $H$ given
  $(\mathbf z,J=j,\mathbf x,v)$ is $X_j$ reweighted by
  $\Pi_{H,\mathbf z}(\mathbf x)\cdot\mathbb 1[H(\mathbf x)=v]$. The indicator is harmless: it
  fixes one further coordinate, and a $(P,1-\delta)$-dense source conditioned on one coordinate
  off its fixed set is $(P+1,1-\delta)$-dense. The factor $\Pi_{H,\mathbf z}(\mathbf x)$ is
  not. r3's Lemma 1 controls $\Pi_{f,\zeta}$ only through $\mathbb E[m_1m_2]\le\delta$, and its
  own counterexample there — $m_1m_2=1$ on an event of probability $\delta$, from which
  "$\mathbb E[m_1m_2]\le\delta^{2}$ is false" — is a case where the reweighting concentrates the
  posterior on a single $f$, destroying density outright.
- **(b) Let the distinguisher sample $\mathbf x$ itself.** Given $(\mathbf z,j)$ and oracle
  access to $g$, a distinguisher can run $S_1^{g},S_2^{g}$ and condition on the leakage matching
  $\mathbf z$, which restores the right law at $g=H$. But Definition `def:sources` gives the
  sources unbounded query count — they "may read all of $H$" — so the resulting $T$ is unbounded
  and Claim 3's $T\delta\log M$ is vacuous. This is the same wall that forced Lemma P through a
  uniform independent challenge to begin with.
- **(c) Bound the $E$-branch trivially.** $\Pr[E]\le P\delta$ by `lem:hit`, so
  $\Pr[E]\cdot1=P\delta$ — the term being eliminated. The $E$-branch has to be shown *small*,
  not merely bounded.

**Lead L1 (the cost of conditioning on $\mathbf x$ is exactly the $2\log N$ inside $\sigma'$).**
Route (a) fails because conditioning on $\mathbf x$ reweights $X_j$ by
$\Pi_{H,\mathbf z}(\mathbf x)$. But the *size* of that reweighting is bounded, and by exactly
the right amount. Write $p(\mathbf u):=\Pr[\mathbf x=\mathbf u\mid\mathbf z=\zeta,J=j]$ for the
marginal under $X_j$, and $S_j:=N^{2}\log M-H_\infty(X_j)$. Since
$$\Pr[H=f\mid\mathbf z=\zeta,J=j,\mathbf x=\mathbf u]=\frac{X_j(f)\,\Pi_{f,\zeta}(\mathbf u)}{p(\mathbf u)}\ \le\ \frac{X_j(f)}{p(\mathbf u)},$$
the conditioned deficiency
$S(\mathbf u):=N^{2}\log M-H_\infty(H\mid\mathbf z=\zeta,J=j,\mathbf x=\mathbf u)$ satisfies
$S(\mathbf u)\le S_j+\log(1/p(\mathbf u))$. Two bounds on that penalty:

- *On average.* $\mathbb E_{\mathbf u}[\log(1/p(\mathbf u))]=H(\mathbf x\mid\mathbf z=\zeta,J=j)\le\log N^{2}=2\log N$.
- *With slack.* $\sum_{\mathbf u:\,p(\mathbf u)<\gamma/N^{2}}p(\mathbf u)\le\gamma$, so off an event
  of probability at most $\gamma$, $\log(1/p(\mathbf u))\le2\log N+\log\gamma^{-1}$.

Checked over 400 random instances with arbitrary per-$f$ product measures $\Pi_f$, degenerate
ones included: both bounds hold, the first tight to $0.9998$.

So conditioning on the challenge point costs $2\log N+\log\gamma^{-1}$ bits of deficiency — and
$\sigma':=\sigma+2\log N$ is *defined* as "the leakage length together with the number of bits
needed to name a point of the domain". The penalty is already budgeted for in the target's own
first term $c(\sigma'+\log\gamma^{-1})q^{+}/P$. Nothing in the constants has to move to pay it.

**Why L1 does not yet close (b).** [CDGS, Claim 3] needs $X_j$ *dense*, not merely of bounded
deficiency. Re-applying [CDGS, Claim 2] to the conditioned law converts deficiency back into
density, but at a *new* fixed set — one depending on $\mathbf x$ — and Contract Remark
`rem:index` forbids exactly that: "It may not be chosen using $\mathbf x$, which is why the
index set is $\mathsf{Fun}\times(\{0,1\}^{*})^{2}$ and not anything larger." So the
re-decomposition cannot be the family; it can only be an analysis device, and then Claim 3
compares the conditioned law to *its own* bit-fixing companion rather than to $Y_j$, and the
chain does not close. What would close it is a form of Claim 3 tolerating a
bounded-deficiency perturbation of a dense source against the **original** companion. That is
the sharp question this document leaves.

**On the multiplicative form, recorded so it is not tried twice.** Card `S1` also records
$\Pr[D^{X'}=1]\le M^{T\delta}\cdot\Pr[D^{Y'}=1]$, never used in this campaign, and a
multiplicative comparison does survive conditioning on a low-probability event where an
additive one does not. It does not help here: both forms of Claim 3 require $X'$ dense, and
route (a)'s failure is the loss of density, not the additivity of the conclusion.

Until **(G-b)** is settled nothing here improves **(H1)**. (G-a) and (G-b) are the whole of the
remaining obstruction, and (G-b) is the harder of the two: it asks for a presampling bound
against an observer holding a challenge correlated with the oracle, which is precisely the case
[CDGS, Lemma 1] does not cover and which card `S1` records this campaign as having already had
to route around once.

## 5. Gap register

- **[INHERITED: r3 Theorem C, r3 Lemma P]** — *load-bearing* for Theorem E″, Corollaries G1 and
  G2. `split-decomp-kappa-1-r3` has now been through blind review with verdict CLEAN
  (`split-decomp-kappa-1-r3-findings.md`), which discharges the "has not been through blind
  review" clause of `split-decomp-kappa-2-r2` §9's first entry; the results themselves are
  still not reproved here.
- **[INHERITED: r3 Lemma 3 steps (1)–(3), r3 Lemma 4, r3 Theorem A]** — *load-bearing* for the
  Corollary D″ step of Theorem E″ and for Corollary G2. Same blind-review status.
- **[INHERITED: Corollary D″ of `split-decomp-kappa-2-r2`]** — *load-bearing* for Theorem E″.
  `split-decomp-kappa-2-r2` has been through blind review at r1 and r2; the triage of its
  findings overruled the referee on Corollary D″'s constant, which is the one place in this
  document's dependency chain where a referee objection was rejected rather than upheld.
- **[GAP: §4, items (G-a) and (G-b)]** — not load-bearing for anything asserted. §4's candidate
  route is stated, not proved, and Theorem E″ does not use it. (G-c) is closed against card
  `S1`. Obstruction O1 records why (G-b) is not a bookkeeping gap: the $E$-branch is a pure
  oracle swap, but every route to [CDGS, Claim 3] on it either destroys the density Claim 3
  needs or costs unbounded queries. Lead L1 quantifies the density loss — conditioning on
  $\mathbf x$ costs $2\log N+\log\gamma^{-1}$ bits of deficiency, exactly the $2\log N$ that
  $\sigma'$ is defined to carry — and names what would close it: a form of Claim 3 tolerating a
  bounded-deficiency perturbation of a dense source against the original bit-fixing companion.
- No `[GAP]` occurs in §§1–3.

## 6. External results used

- **[r3, Theorem C]**, **[r3, Lemma P]**, **[r3, Theorem A]** — `split-decomp-kappa-1-r3`.
  Restated where used; not reproved.
- **[kappa-2-r2, Corollary D″]** — `split-decomp-kappa-2-r2` §6. Restated; not reproved.
- **[CDGS, Claim 2]** (Coretti, Dodis, Guo, Steinberger, *Random Oracles and Non-Uniformity*,
  ePrint 2017/937). CARD (S1). Enters §1–§3 only transitively through r3's Lemma P; cited
  directly in §4, which proves nothing.
- $\lfloor t\rfloor\ge t/2$ for $t\ge1$; $\mathrm{SD}\le\sum_v(p_v-1/M)^{+}$;
  $e^{u}-1\le ue^{u}$. RESTATED, standard.

### END OF ARTIFACT split-decomp-kappa-3 ###
