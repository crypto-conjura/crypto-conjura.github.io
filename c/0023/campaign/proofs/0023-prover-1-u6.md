---
id: 0023-prover-1-u6
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 6 of 8: Lemma 6 + Theorem + tightness remark)
---

# 0023-prover-1 — Unit 6: Lemma 6 (master count), the Theorem (I01), and the tightness remark

Conventions as in Unit 0. Uses Lemma 5 (Unit 5) and, for the remark, Lemma 1
(Unit 1). Influences are nonnegative (sums of squares, by definition).

---

**Lemma 6 (master count).** Let $d,N\in\mathbb{N}$ and let $\mathbf F$,
$\mathbf G$ be finitely supported probability distributions over
$\mathcal{C}^{\mathrm{junta}}_d$ (on $\{\pm1\}^N$), with each support element
carrying a fixed witnessing representation: write
$\mathrm{supp}\,\mathbf F=\{f_1,\dots,f_m\}$ with probabilities
$p_1,\dots,p_m>0$, $\sum_a p_a=1$, and representations $f_a=f_{J_a,P_a}$,
$|J_a|\le d$; likewise $\mathrm{supp}\,\mathbf G=\{g_1,\dots,g_n\}$,
probabilities $q_b>0$, $\sum_b q_b=1$, representations $g_b=f_{K_b,Q_b}$,
$|K_b|\le d$. Suppose the pair $(\mathbf F,\mathbf G)$ is **incompatible**:
for every $a\in[m]$, $b\in[n]$ the supports $A_a$ of $f_a$ and $B_b$ of $g_b$
are disjoint. Put
$$\delta_F:=\max_{i\in[N]}\ \mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)],\qquad
\delta_G:=\max_{i\in[N]}\ \mathbb{E}_{g\sim\mathbf G}[\mathrm{Inf}_i(g)].$$
Then
$$\delta_F\cdot\Bigl(\textstyle\sum_b q_b|K_b|\Bigr)\ +\ \delta_G\cdot\Bigl(\textstyle\sum_a p_a|J_a|\Bigr)\ \ge\ 1.\tag{6.1}$$
In particular, since $|J_a|,|K_b|\le d$,
$$(\delta_F+\delta_G)\,d\ \ge\ 1\qquad\text{and hence}\qquad \max(\delta_F,\delta_G)\ \ge\ \frac1{2d}.\tag{6.2}$$

*Proof.* All sums below are finite ($m,n,N<\infty$), so exchanging their
order is unconditionally valid.

For each pair $(a,b)$ set $S_{ab}:=J_a\cap K_b$. Since $A_a\cap
B_b=\emptyset$, Lemma 5 applies to the representations
$(J_a,P_a),(K_b,Q_b)$:
$$\sum_{i\in S_{ab}}\bigl[\mathrm{Inf}_i(f_a)+\mathrm{Inf}_i(g_b)\bigr]\ \ge\ 1 .$$
Multiply by $p_aq_b\ge0$ and sum over $a\in[m]$, $b\in[n]$; using
$\sum_{a,b}p_aq_b=1$:
$$\underbrace{\sum_{a,b}p_aq_b\sum_{i\in S_{ab}}\mathrm{Inf}_i(f_a)}_{=: \Sigma_1}\ +\ \underbrace{\sum_{a,b}p_aq_b\sum_{i\in S_{ab}}\mathrm{Inf}_i(g_b)}_{=: \Sigma_2}\ \ge\ 1 .\tag{6.3}$$

**Bounding $\Sigma_1$.** Since $S_{ab}\subseteq K_b$ and every
$\mathrm{Inf}_i(f_a)\ge0$, enlarging the index set can only increase the
inner sum:
$$\Sigma_1\ \le\ \sum_{a,b}p_aq_b\sum_{i\in K_b}\mathrm{Inf}_i(f_a)
\ =\ \sum_{b}q_b\sum_{i\in K_b}\ \underbrace{\sum_{a}p_a\,\mathrm{Inf}_i(f_a)}_{=\ \mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\ \le\ \delta_F}
\ \le\ \delta_F\sum_b q_b\,|K_b| .$$

**Bounding $\Sigma_2$.** Symmetrically, $S_{ab}\subseteq J_a$ and
$\mathrm{Inf}_i(g_b)\ge0$ give
$$\Sigma_2\ \le\ \sum_a p_a\sum_{i\in J_a}\ \underbrace{\sum_b q_b\,\mathrm{Inf}_i(g_b)}_{=\ \mathbb{E}_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]\ \le\ \delta_G}
\ \le\ \delta_G\sum_a p_a\,|J_a| .$$

Substituting both bounds into (6.3) yields (6.1). Since $|K_b|\le d$ for all
$b$ and $|J_a|\le d$ for all $a$ (class membership of the witnesses),
$\sum_bq_b|K_b|\le d$ and $\sum_ap_a|J_a|\le d$, so (6.1) gives
$(\delta_F+\delta_G)d\ge\delta_F\sum_bq_b|K_b|+\delta_G\sum_ap_a|J_a|\ge1$;
and $\delta_F+\delta_G\le2\max(\delta_F,\delta_G)$ gives (6.2). $\blacksquare$

**Remark 6.1 (generalization hypothesis).** The count is linear in each
distribution, uses only per-coordinate *average* influences and the window
budgets $|J|,|K|\le d$, and never enumerates patterns: no constant depends on
the number of possible patterns (nothing like $2^{2^d}$). It replaces the
union bound of the conjunction-subclass calibration: instead of a union over
"conflict coordinates", each cross pair is charged a unit payment which the
average-influence budget must fund through the partner's window. This is the
engine I01's generalization hypothesis asks for.

---

**Theorem (I01).** There exist $c_1\in(0,1]$, $c_2>0$, and
$\delta:\mathbb{N}\to(0,1]$ with $\delta(d)\ge c_1d^{-c_2}$ for all $d\ge1$,
such that for all $d,N\in\mathbb{N}$ and all finitely supported distributions
$\mathbf F,\mathbf G$ over
$$\mathcal{C}^{\mathrm{junta}}_d=\Bigl\{\tfrac{\mathbf 1_A}{\|\mathbf 1_A\|_2}:A=\{x\in\{\pm1\}^N:x_J\in P\},\ J\subseteq[N],\ |J|\le d,\ \emptyset\ne P\subseteq\{\pm1\}^J\Bigr\}$$
satisfying, for every $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb{E}_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]\le\delta(d)$, there exist
$f\in\mathrm{supp}\,\mathbf F$, $g\in\mathrm{supp}\,\mathbf G$, and
$x\in\{\pm1\}^N$ with $f(x)\,g(x)\ne0$.

Explicit witnesses: $c_1=1/3$, $c_2=1$, $\delta(d)=1/(3d)$.

*Proof.* First, admissibility of the witnesses: $c_1=1/3\in(0,1]$,
$c_2=1>0$; for $d\ge1$, $\delta(d)=1/(3d)\in(0,1/3]\subseteq(0,1]$ and
$\delta(d)=1/(3d)\ge c_1d^{-c_2}=1/(3d)$ ✓.

Fix $d,N\in\mathbb{N}$ and distributions $\mathbf F,\mathbf G$ as in the
statement. For each element of $\mathrm{supp}\,\mathbf F$ and of
$\mathrm{supp}\,\mathbf G$ fix a witnessing representation as in Unit 0
(class membership guarantees at least one). Both supports are nonempty: a
finitely supported probability distribution has total mass $1$ carried by
finitely many points, at least one of which has positive probability.

Suppose, for contradiction, that the conclusion fails: for **all**
$f\in\mathrm{supp}\,\mathbf F$, $g\in\mathrm{supp}\,\mathbf G$ and **all**
$x\in\{\pm1\}^N$, $f(x)g(x)=0$. For normalized indicators
$f=\mathbf 1_A/\|\mathbf 1_A\|_2$ and $g=\mathbf 1_B/\|\mathbf 1_B\|_2$ we
have $f(x)g(x)=\mathbf 1_A(x)\mathbf 1_B(x)/(\|\mathbf 1_A\|_2\|\mathbf
1_B\|_2)$, which is $>0$ if $x\in A\cap B$ and $=0$ otherwise; so the failure
of the conclusion says precisely that every pair of supports is disjoint,
i.e. $(\mathbf F,\mathbf G)$ is incompatible in the sense of Lemma 6.

By Lemma 6 (6.2), $\max(\delta_F,\delta_G)\ge1/(2d)$. But the influence
hypothesis says $\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\le\delta(d)$
for every $i$, i.e. $\delta_F\le\delta(d)=1/(3d)$, and likewise
$\delta_G\le1/(3d)$. Hence
$$\frac1{2d}\ \le\ \max(\delta_F,\delta_G)\ \le\ \frac1{3d},$$
a contradiction ($1/(2d)>1/(3d)$ for every $d\ge1$). So the conclusion
holds. $\blacksquare$

**Remark 6.2 (conventions with $0$).** If the reader's $\mathbb{N}$ contains
$0$: extend $\delta$ by $\delta(0):=1$ (the constraint
$\delta(d)\ge c_1d^{-c_2}$ is imposed only for $d\ge1$). At $d=0$ the class
consists of the single function $f\equiv1$ ($J=\emptyset$, $P$ the unique
nonempty pattern), and any $f,g$ in the supports satisfy $f(x)g(x)=1\ne0$ at
every $x$. At $N=0$ the cube is a single point, $[N]=\emptyset$ makes the
influence hypothesis vacuous, the class is again $\{f\equiv1\}$, and the
conclusion holds at the unique point. Both cases are trivially consistent
with the statement.

---

**Remark 6.3 (tightness; NON-load-bearing).** No witnessing $\delta$ for I01
can satisfy $\delta(d)\ge1/(2d)$ for any $d\ge1$; hence the constant in
Lemma 6 is exact and $\delta(d)=1/(3d)$ is within a factor $3/2$ of optimal.

*Proof of the remark (self-contained, via Lemma 1).* Fix $d\ge1$ and take
$N=d^2$, coordinates indexed by $(r,c)\in[d]\times[d]$. For $r\in[d]$ let
$J_r=\{(r,c):c\in[d]\}$ (row $r$), $P_r=\{(-1,\dots,-1)\}\subseteq\{\pm1\}^{J_r}$,
and $f_r=f_{J_r,P_r}$; for $c\in[d]$ let $K_c=\{(r,c):r\in[d]\}$ (column
$c$), $Q_c=\{(+1,\dots,+1)\}$, and $g_c=f_{K_c,Q_c}$. All windows have size
$d$, all patterns are nonempty, so all $2d$ functions lie in
$\mathcal{C}^{\mathrm{junta}}_d$. The $f_r$ are pairwise distinct (the point
with row $r$ all $-1$ and all other coordinates $+1$ lies in the support of
$f_r$ only), likewise the $g_c$. Let $\mathbf F$ be uniform on
$\{f_1,\dots,f_d\}$ and $\mathbf G$ uniform on $\{g_1,\dots,g_d\}$.

*No common nonvanishing point:* any $x$ with $f_r(x)g_c(x)\ne0$ would need
$x_{(r,c)}=-1$ (from $x_{J_r}\in P_r$) and $x_{(r,c)}=+1$ (from
$x_{K_c}\in Q_c$) — impossible. So the I01 conclusion fails for
$(\mathbf F,\mathbf G)$.

*Influences:* $P_r$ is a single point of a $d$-dimensional cube, so
$b_i(P_r)=1$ for every $i\in J_r$, and Lemma 1 gives
$\mathrm{Inf}_i(f_r)=1/2$ for $i\in J_r$ and $0$ otherwise. Hence for every
coordinate $(r',c')$: $\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_{(r',c')}(f)]
=\frac1d\sum_{r}\mathrm{Inf}_{(r',c')}(f_r)=\frac1d\cdot\frac12=\frac1{2d}$
(only $r=r'$ contributes). Symmetrically for $\mathbf G$.

So $(\mathbf F,\mathbf G)$ satisfies every I01 hypothesis at influence level
exactly $1/(2d)$ and violates the conclusion; a witnessing $\delta$ with
$\delta(d)\ge1/(2d)$ would be contradicted at this $(d,N)$. (This
construction is the NegRow/PosCol pattern of card S1, Claim B.3, reproved
here inline; the card is context, not justification.) $\square$

EMITTED unit 6 of 8; NEXT UNIT Final assembly (`0023-prover-1.md`); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u6 ###
