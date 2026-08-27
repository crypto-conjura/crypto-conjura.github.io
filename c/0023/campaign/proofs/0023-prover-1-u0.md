---
id: 0023-prover-1-u0
agent: prover
model: claude-fable-5
cycle: 2
status: COMPLETE (unit 0 of 8: method sketch)
---

# 0023-prover-1 — Unit 0: METHOD SKETCH

**Target:** intermediate I01 (`intermediates/I01-spread-junta.md`), rung R1.
**Assigned plan:** 0023-refuter-2 §8 (lemma chain L1–L5; conclusion with
δ(d) = 1/(3d), c₁ = 1/3, c₂ = 1; grid tightness as a non-load-bearing remark).
**Discipline:** every lemma proved from scratch, for all d and N; the refuter's
computations are evidence only and are cited nowhere. The single non-elementary
ingredient (a hypercube edge-isoperimetry-type inequality) is proved inline by
induction, in exactly the weak "entropy form" the payment lemma needs — not
cited from memory, not full Harper.

## 0. Statement to be proved (verbatim from I01)

There exist $c_1\in(0,1]$, $c_2>0$, and $\delta:\mathbb{N}\to(0,1]$ with
$\delta(d)\ge c_1 d^{-c_2}$ for all $d\ge 1$, such that for all $d,N\in\mathbb{N}$
and all finitely supported distributions $\mathbf{F},\mathbf{G}$ over the class

$$\mathcal{C}^{\mathrm{junta}}_d:=\Bigl\{\tfrac{\mathbf{1}_A}{\|\mathbf{1}_A\|_2}\ :\ A=\{x\in\{\pm1\}^N: x_J\in P\},\ J\subseteq[N],\ |J|\le d,\ \emptyset\ne P\subseteq\{\pm1\}^J\Bigr\}$$

satisfying, for every $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf{F}}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb{E}_{g\sim\mathbf{G}}[\mathrm{Inf}_i(g)]\le\delta(d)$,
there exist $f\in\mathrm{supp}\,\mathbf{F}$, $g\in\mathrm{supp}\,\mathbf{G}$,
and $x\in\{\pm1\}^N$ with $f(x)\,g(x)\ne 0$.

We will prove it with the explicit witnesses $c_1=1/3$, $c_2=1$,
$\delta(d)=1/(3d)$.

## 1. Conventions (fixed once, used in every unit)

* $\mathbb{N}=\{1,2,3,\dots\}$. (If a reader's convention includes $0$: both
  $d=0$ and $N=0$ are degenerate-trivial; handled by a one-line remark in the
  final theorem.)
* Uniform measure on $\{\pm1\}^N$; inner product
  $\langle f,g\rangle=\mathbb{E}_{x}[f(x)g(x)]$ (real-valued functions suffice
  here: every class member is real-valued);
  $\|f\|_2=(\mathbb{E}_x f(x)^2)^{1/2}$.
* Fourier: characters $\chi_T(x)=\prod_{i\in T}x_i$ for $T\subseteq[N]$;
  every $f:\{\pm1\}^N\to\mathbb{R}$ has a unique expansion
  $f=\sum_{T\subseteq[N]}\hat f(T)\chi_T$ with $\hat f(T)=\mathbb{E}[f\chi_T]\in\mathbb{R}$.
  Per the parent Contract specialized to $\mathcal{Y}=\mathbb{Z}_2$:
  $\mathrm{Inf}_i(f)=\sum_{T\ni i}\hat f(T)^2$, applied AFTER normalization
  (i.e., to $\mathbf 1_A/\|\mathbf 1_A\|_2$).
* Points of $\{\pm1\}^J$ are $\pm1$-strings indexed by $J$; $x_J$ is the
  restriction of $x$ to $J$. For $u\in\{\pm1\}^J$ and $i\in J$, $u^{\oplus i}$
  flips coordinate $i$. An **$i$-edge** of $\{\pm1\}^J$ is an unordered pair
  $\{u,u^{\oplus i}\}$; an **edge** is an $i$-edge for some $i\in J$.
* For $\emptyset\ne P\subseteq\{\pm1\}^J$ and $i\in J$:
  $b_i(P):=\#\{i\text{-edges of }\{\pm1\}^J\text{ with exactly one endpoint in }P\}$.
* For $W\subseteq\{\pm1\}^n$: $\partial_E W:=$ the set of edges of $\{\pm1\}^n$
  (all directions) with exactly one endpoint in $W$.
* For $S\subseteq J$: $\pi_S:\{\pm1\}^J\to\{\pm1\}^S$ is coordinate
  restriction; the **projection density** is
  $\nu_P(S):=|\pi_S(P)|/2^{|S|}$.
* Notation guard: $T$ is reserved for Fourier index sets, $S$ for shared
  windows, $J,K$ for windows, $P,Q$ for patterns, $W$ for the set in the
  isoperimetric lemma, $L_t$ for level sets.
* Every class member $f$ is fixed together with one **witnessing
  representation** $(J,P)$, $|J|\le d$, $\emptyset\ne P\subseteq\{\pm1\}^J$
  (representations are not unique; all quantities we use are either intrinsic
  to $f$ or proved for the chosen representation, and the final count uses
  only $|J|\le d$). Write $f_{J,P}:=\mathbf 1_A/\|\mathbf 1_A\|_2$ for
  $A=\{x:x_J\in P\}$. Since $P\ne\emptyset$, $A\ne\emptyset$, so
  $\|\mathbf 1_A\|_2>0$ and $f_{J,P}$ is well defined with $\|f_{J,P}\|_2=1$.

## 2. Lemma chain (full statements; proofs in units 1–6)

**Lemma 1 (influence formula; = plan step L1).**
Let $f=f_{J,P}$. Then for every $i\in[N]$:
$$\mathrm{Inf}_i(f)=\begin{cases} \dfrac{b_i(P)}{2|P|} & i\in J,\\[2pt] 0 & i\notin J.\end{cases}$$
Proof route: (i) orthonormality of the $\chi_T$ (one line); (ii) the flip
identity $f(x)-f(x^{\oplus i})=2\sum_{T\ni i}\hat f(T)\chi_T(x)$, whence
$\mathrm{Inf}_i(f)=\tfrac14\mathbb{E}_x[(f(x)-f(x^{\oplus i}))^2]$ by
Parseval; (iii) exact edge count for the normalized indicator:
$\mathrm{Inf}_i=|\partial_i A|/(2|A|)$, and the junta structure gives
$|A|=|P|2^{N-|J|}$, $|\partial_i A|=b_i(P)2^{N-|J|}$ for $i\in J$, $0$ else.
Side remarks (non-load-bearing, one line each): $\deg f\le|J|\le d$ and
$\|f\|_2=1$, as asserted by I01.

**Lemma 2 (disjointness = projection disjointness on the shared window;
= plan step L2).**
Let $f=f_{J,P}$, $g=f_{K,Q}$ with supports $A,B$, and let $S=J\cap K$. Then
$$A\cap B=\emptyset\iff \pi_S(P)\cap\pi_S(Q)=\emptyset .$$
In particular if $S=\emptyset$ then $A\cap B\ne\emptyset$ (nonempty patterns
on disjoint windows always meet); so disjointness forces $S\ne\emptyset$.
Proof route: one direction by restriction of a common point; the other by
explicitly assembling a common point from $p\in P$, $q\in Q$ agreeing on $S$.

**Lemma 3 (hypercube edge-isoperimetry, entropy form; the inline ingredient
inside plan step L3).**
For every $n\ge0$ and every nonempty $W\subseteq\{\pm1\}^n$:
$$|\partial_E W|\ \ge\ |W|\log_2\frac{2^n}{|W|}.$$
Proof route: induction on $n$; split by the last coordinate into halves of
sizes $a\ge b$; exact decomposition
$|\partial_E W|=|\partial_E W_+|+|\partial_E W_-|+|W_+\triangle W_-|$ and
$|W_+\triangle W_-|\ge a-b$; the case $b=0$ directly, the case $b\ge1$ reduces
to the real-variable inequality
$(a+b)\log_2(a+b)-a\log_2 a-b\log_2 b\ge 2b$ for $a\ge b>0$, proved by a
one-derivative monotonicity argument with equality at $a=b$.

**Lemma 4 (projection-density payment; = plan step L3).**
For every $f=f_{J,P}$ and every $S\subseteq J$:
$$\sum_{i\in S}\mathrm{Inf}_i(f)\ \ge\ \frac12\log_2\frac{1}{\nu_P(S)}.$$
Proof route: with $w(u)=|P\cap\pi_S^{-1}(u)|$ (fiber counts),
(i) $\sum_{i\in S}b_i(P)\ge \mathrm{TV}_S(w):=\sum_{\text{edges }\{u,u'\}\text{ of }\{\pm1\}^S}|w(u)-w(u')|$
(grouping window-cube edges over their $S$-projections);
(ii) layer cake: $\mathrm{TV}_S(w)=\sum_{t\ge1}|\partial_E L_t|$ for the level
sets $L_t=\{u:w(u)\ge t\}$, a finite sum;
(iii) Lemma 3 on each nonempty $L_t\subseteq\pi_S(P)$, then
$\sum_t|L_t|=|P|$ and monotonicity of the log factor give
$\sum_{i\in S}b_i(P)\ge|P|\log_2(2^{|S|}/|\pi_S(P)|)$; divide by $2|P|$ and
apply Lemma 1. ($S=\emptyset$ is trivially fine: both sides are $0$.)

**Lemma 5 (per-pair payment ≥ 1; = plan step L4).**
If $f=f_{J,P}$ and $g=f_{K,Q}$ have $A\cap B=\emptyset$, then with $S=J\cap K$:
$$\sum_{i\in S}\bigl[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)\bigr]\ \ge\ 1 .$$
Proof route: Lemma 2 gives $\pi_S(P)\cap\pi_S(Q)=\emptyset$ with both
projections nonempty, hence $\nu_P(S)+\nu_Q(S)\le1$, hence
$\nu_P(S)\nu_Q(S)\le1/4$ (AM–GM); apply Lemma 4 to each side and add.

**Lemma 6 (master count; = plan step L5).**
Let $\mathbf F,\mathbf G$ be finitely supported distributions over
$\mathcal{C}^{\mathrm{junta}}_d$ (each support element with a fixed witnessing
representation) such that every pair
$(f,g)\in\mathrm{supp}\,\mathbf F\times\mathrm{supp}\,\mathbf G$ has disjoint
supports. Put $\delta_F:=\max_{i\in[N]}\mathbb{E}_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]$
and $\delta_G:=\max_{i\in[N]}\mathbb{E}_{g\sim\mathbf G}[\mathrm{Inf}_i(g)]$.
Then
$$\delta_F\cdot\mathbb{E}_{g\sim\mathbf G}|K_g|\ +\ \delta_G\cdot\mathbb{E}_{f\sim\mathbf F}|J_f|\ \ge\ 1,
\qquad\text{hence}\qquad (\delta_F+\delta_G)\,d\ \ge\ 1,\qquad
\max(\delta_F,\delta_G)\ \ge\ \frac1{2d}.$$
Proof route: weight Lemma 5's per-pair inequality by the product probabilities
and sum; bound $\sum_{i\in S}\le\sum_{i\in(\text{partner's window})}$ using
nonnegativity of influences; exchange the (finite) sums; use the
per-coordinate average-influence caps and $|J|,|K|\le d$. This is the
union-bound replacement demanded by I01's generalization hypothesis: linear in
both distributions, no pattern enumeration, no constants like $2^{2^d}$.

**Theorem (I01, quantified witnesses).**
The I01 statement holds with $c_1=1/3$, $c_2=1$, $\delta(d)=1/(3d)$.
Proof route: contrapositive. If the conclusion fails for some $d,N,\mathbf
F,\mathbf G$, every pair of support elements has disjoint supports (for
normalized indicators, $f(x)g(x)\ne0\iff x\in A\cap B$); supports are nonempty
(total probability 1, finite support); Lemma 6 gives
$\max(\delta_F,\delta_G)\ge1/(2d)$, contradicting the hypothesis
$\delta_F,\delta_G\le1/(3d)<1/(2d)$.

**Remark (tightness; NON-load-bearing).**
For every $d\ge1$, at $N=d^2$, the row/column grid pair — $\mathbf F$ uniform
on the $d$ row functions $f_r=f_{J_r,\{(-1,\dots,-1)\}}$, $\mathbf G$ uniform
on the $d$ column functions with pattern all-$(+1)$ — lies in
$\mathcal{C}^{\mathrm{junta}}_d$, has every per-coordinate average influence
exactly $1/(2d)$ (computed inline from Lemma 1), and has $f(x)g(x)=0$
everywhere for every pair. Hence no witnessing $\delta$ can have
$\delta(d)\ge1/(2d)$ for any $d$: Lemma 6's constant is exact, and
$\delta(d)=1/(3d)$ is within a factor $3/2$ of optimal. (Proved inline; card
S1 Claim B.3 is consistent with this but is not cited as justification.)

## 3. Dependency graph and case split

```
Lemma 1 (Fourier/edge formula)   Lemma 2 (projection criterion)   Lemma 3 (isoperimetry, standalone)
      \                                |                                /
       \                               |                    Lemma 4 (uses 1, 3)
        \                              |                       /
         \                             Lemma 5 (uses 2, 4)
          \                            |
           \                     Lemma 6 (uses 5, nonneg. influences from def.)
            \                          |
             Theorem (uses 6; Lemma 1 only via the chain)  + Remark (uses 1; not load-bearing)
```

Case split ledger (each discharged where it arises):
* $S=\emptyset$ (disjoint windows, incl. constant functions $J=\emptyset$):
  Lemma 2 shows disjointness impossible; Lemma 4 trivially true.
* $b=0$ (empty half) in Lemma 3's induction: direct.
* Empty level sets $L_t$, $t>\max w$: contribute 0; sum truncated.
* Non-unique representations: fixed witness per support element; Lemma 6 uses
  only $|J|\le d$ of the witness; influences are intrinsic to $f$.
* $d=0$ / $N=0$ under a $0\in\mathbb{N}$ convention: trivial, remark in the
  Theorem.

## 4. Dependencies and sources

External results used: **none**. Every step is proved inline from the parent
Contract's definitions (specialized to $\mathcal{Y}=\mathbb{Z}_2$ as fixed in
I01). No source request. The refuter's numerical verifications are not cited.
Card S1 is mentioned only in the non-load-bearing tightness remark as
consistency context, never as justification.

## 5. Lean skeleton decision

Skipped. The combinatorial core (Lemma 3) is cheaply formalizable, but the
statement of I01 requires Fourier analysis and influences on the Boolean cube,
for which there is no cheap Mathlib scaffolding; a skeleton that elides
Lemma 1 would not de-risk the actual approach. Budget goes to the prose proof.

## 6. Unit plan

u1 = Lemma 1; u2 = Lemma 2; u3 = Lemma 3; u4 = Lemma 4; u5 = Lemma 5;
u6 = Lemma 6 + Theorem + Remark; Final = assembly into `0023-prover-1.md`
(self-contained, verdict first, gap register, dependencies, stage handoff).

EMITTED unit 0 of 8; NEXT UNIT u1 (Lemma 1); ARTIFACT 0023-prover-1.

### END OF ARTIFACT 0023-prover-1-u0 ###
