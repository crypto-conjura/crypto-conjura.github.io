---
id: 0023-prover-3-u5
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: UNIT 5 of 6 (CLAUSE (iv): P1 and P5; the frontier)
---

# Unit 5 — clause (iv): where P1 and P5 sit; the non-canonicity theorem; the exact frontier $\eta^*$

**Headline finding (refereeing `0023-strategist-2` §0.6's ruling): CONFIRMED.
P1 and P5 ESCAPE the barrier.** Not by definition — by exact evaluation of the
two certified witnesses on their window functionals, and by checking that both
of CAP I's and CAP II's hypotheses fail for them. The strategist's stated reasons
are also confirmed, but sharpened: the operative reason is *not* "sum rather than
$\min$" (L7.6 shows that is insufficient) but the conjunction of **(α) window
size bounded by a theorem unrelated to relevance** and **(β) willingness to
charge coordinates that are cheap for their own side**.

## L11.1 (the framework covers randomised and point-indexed windows)

**Statement.** Let each admissible $A$ carry a probability law $\mu_A$ on subsets
of $\mathrm{Rel}(A)$ (a *randomised localised window*), with the draw
$W(A)\sim\mu_A$ independent of everything else. Then L1, L2 and L3 hold with
$|W(A)|$ replaced by $\mathbb E_{\mu_A}|W(A)|$ and $\pi_W$ by its expectation;
in particular
$$V_W(d)\ \le\ \inf_{(A,B)\in\mathcal P_d}\frac{\mathbb E\,\pi_W(A,B)}{\mathbb E|W(A)|+\mathbb E|W(B)|}\ \le\ \eta^*(d).$$

**Proof.** In L1's proof replace $\mathbf 1\{i\in W(g)\}$ by its conditional
expectation: $\mathbb E[\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)]
=\Pr[i\in W(g)]\,\mathbb E_{\mathbf F}[\mathrm{Inf}_i(f)]$, valid because the
window draw for $g$ is independent of $f$; summing gives
$\sum_i\Pr[i\in W(g)]=\mathbb E|W(g)|$. L2's point-mass evaluation and L3's
term-by-term domination are unchanged (L3 holds pointwise in the draw, hence in
expectation). $\blacksquare$

This is what places **P5** inside the framework: its window
$T_A(x)$, $x\sim\mathrm{Unif}(A)$, is a randomised window whose law depends only
on $A$. (A window depending on the *partner* is still excluded — Remark L1.3.)

## L10 (P1: the shattering window escapes)

Let $W_{\mathrm{sh}}$ be **any** selection assigning to each degree-$\le d$ set
$A$ one maximum-degree monomial support of $\mathbf 1_A$ (card S7b: such a set
$W$ has $|W|\le d$ **by theorem**, and $A$ projects onto
$\{\pm1\}^{[N]\setminus W}$; the projection property is not used below).
$W_{\mathrm{sh}}$ is localised: a monomial support consists of relevant
coordinates.

### L10.1 Exact values on both witnesses

**(a) Address pair.** By L5(2) the only maximum-degree supports are
$\{a_1,\dots,a_k,y_j\}$, so $W_{\mathrm{sh}}(A_k)=\{a_*,y_j\}$ and
$W_{\mathrm{sh}}(B_k)=\{a_*,y_{j'}\}$ for some $j,j'$, each of size $d$. Using
L5(4) (both sides have the same influence table),
$$\pi_{W_{\mathrm{sh}}}(A_k,B_k)=\Bigl(\tfrac k4+2^{-k-1}\Bigr)+\Bigl(\tfrac k4+2^{-k-1}\Bigr)=\tfrac k2+2^{-k},$$
$$\frac{\pi_{W_{\mathrm{sh}}}}{|W_{\mathrm{sh}}(A_k)|+|W_{\mathrm{sh}}(B_k)|}
=\frac{k/2+2^{-k}}{2(k+1)}\ \ge\ \frac{k}{4(k+1)}\ \ge\ \frac18\qquad(k\ge1),$$
independently of the choices $j,j'$. (Script: $1/4,\ 5/24,\ 13/64$ for
$k=1,2,3$; payments $1,\ 5/4,\ 13/8$.)

**(b) Subcube pair.** By L7.1(1) each side has the unique maximum-degree support
$[d]$, so $W_{\mathrm{sh}}(C)=W_{\mathrm{sh}}(D)=[d]$ and
$$\pi_{W_{\mathrm{sh}}}(C,D)=\frac d2+\frac d{2(2^d-1)},\qquad
\frac{\pi_{W_{\mathrm{sh}}}}{2d}=\frac14+\frac1{4(2^d-1)}\ >\ \frac14 .$$

**Conclusion.** Neither witness caps $W_{\mathrm{sh}}$: both give values
$\ge1/8$, i.e. $\Omega(1)$, whereas a cap must be $2^{-\Theta(d)}$. Moreover both
class hypotheses fail, and fail *quantitatively*:
* **CAP I fails.** $W_{\mathrm{sh}}$ has density
  $c=|W_{\mathrm{sh}}(A_k)|/|\mathrm{Rel}(A_k)|=d/(2^{d-1}+d-1)=2^{-\Theta(d)}$ on
  the address family; CAP I(b) with that $c$ degrades to
  $(d+1)/(4c(k+2^k))=(d+1)/(4d)\approx\tfrac14$ — its own inequality returns a
  vacuous bound, exactly as Remark L6.2 predicted.
* **CAP II fails.** $W_{\mathrm{sh}}(D)=[d]$ consists of coordinates with
  $\mathrm{Inf}_i(f_D)=\frac1{2(2^d-1)}$: *cheap for their own function*. So
  $W_{\mathrm{sh}}$ is own-heavy only at the exponentially small level
  $\theta\le\frac1{2(2^d-1)}$, which is excluded by CAP II's hypothesis; and by
  the dichotomy L7.5 (case $w_D=d\ge1$) witness (b) yields $\ge\frac1{4d}$.

### L10.2 (Non-canonicity theorem — why the escape is real, and what it costs)

**Statement.** (i) For every $c\in\{0,1\}^k$ the map $\sigma_c$ defined by
$a_t\mapsto\varepsilon_t(c)a_t$ (sign flip iff $c_t=1$) and
$y'_j:=y_{j\oplus c}$ is an automorphism of $\{\pm1\}^N$ with
$\sigma_c(A_k)=A_k$ and $\sigma_c(B_k)=B_k$; the induced action on coordinates is
transitive on the $2^k$ targets. (ii) Consequently, if $W$ is **canonical**
(equivariant: $W(\sigma A)=\sigma W(A)$ for every cube automorphism $\sigma$) and
localised, then $W(A_k)\cap\{\text{targets}\}$ is $\emptyset$ or all $2^k$
targets. (iii) Hence **no canonical localised functional is a shattering-window
selection**: every maximum-degree support contains exactly one target
(L5(2)), and $1\notin\{0,2^k\}$. (iv) Every canonical localised $W$ satisfies:
either $|W(A_k)|\ge2^{k}=2^{d-1}$, and then CAP I gives
$V_W(d)\le(d+1)2^{-d}$; or $W(A_k)\subseteq\{a_1,\dots,a_k\}$.

**Proof.** (i) $\sigma_c$ flips signs of some coordinates and permutes the target
coordinates by the involution $j\mapsto j\oplus c$, so it is a cube automorphism.
With $s_t=\varepsilon_t(c)=1-2c_t$: $b_t(s_ta_t)=\frac{1-s_ta_t}2$ equals
$b_t(a)$ if $c_t=0$ and $1-b_t(a)$ if $c_t=1$, i.e. $b(a')=b(a)\oplus c$. Hence
$x'=\sigma_c(x)$ satisfies $y'_{b(a')}=y_{b(a)\oplus c\oplus c}=y_{b(a)}$, so
$x'\in A_k\iff x\in A_k$; thus $\sigma_c(A_k)=A_k$ and (complementing)
$\sigma_c(B_k)=B_k$. Given targets $j,j'$, take $c=j\oplus j'$.
(ii) Equivariance plus $\sigma_c(A_k)=A_k$ give $W(A_k)=\sigma_cW(A_k)$ for every
$c$; so the target part of $W(A_k)$ is a union of orbits of the transitive action,
i.e. $\emptyset$ or everything. (iii),(iv) immediate, using L6(a)-style
arithmetic: $|W(A_k)|+|W(B_k)|\ge2^{k}$ gives
$V_W\le\frac{(d+1)/2}{2^{d-1}}=(d+1)2^{-d}$. $\blacksquare$

**Reading (the load-bearing clause-(iv) insight).** P1's escape is purchased
*exactly* by non-canonicity — card S7/S7b's obstacle (ii) ("$T(A)$ is not
canonical; the theorem gives no way to choose one coherently across a family").
Two consequences, in opposite directions:
* **The escape is legitimate, not a loophole.** L1 requires only that each side's
  window depend on its own function; it never requires equivariance. A fixed but
  arbitrary selection $A\mapsto W_{\mathrm{sh}}(A)$ is admissible, and P1's
  target inequality (PAY$\star$) is even *quantified over all* selections, which
  is stronger than the count needs.
* **The escape has a price, now identified.** Within the canonical world, L10.2(iv)
  says a functional must either be exponentially large on the address family
  (capped) or confine itself to the "hub" (the address block). So any *canonical*
  route must explain how it chooses among $2^{d-1}$ symmetric targets — it
  cannot. This is the precise sense in which the shattering window's
  non-canonicity is not a defect of the theorem but the *source of its power*.

### L10.3 (a new canonical survivor: the argmax-influence window $W_{\max}$)

Define $W_{\max}(A):=\{i:\mathrm{Inf}_i(f_A)=\max_j\mathrm{Inf}_j(f_A)\}$. It is
canonical and localised (in a cross-disjoint pair both sides have
$\mathrm{Rel}\ne\emptyset$ by L4.1, so the max is positive). On witness (a) with
$k\ge2$: $W_{\max}=\{a_1,\dots,a_k\}$ on both sides, payment $k/2$, denominator
$2k$, **ratio $1/4$**. On witness (b): $W_{\max}(C)=W_{\max}(D)=[d]$ (influences
constant within each side), ratio $\frac14+\frac1{4(2^d-1)}$. It is neither
relevance-denominated (density $k/(k+2^k)$) nor own-heavy at any level
$\ge\frac1{2(2^d-1)}$ (on $D$ the max influence *is* $\frac1{2(2^d-1)}$). **So
$W_{\max}$ escapes both caps and is canonical** — a live window functional that
no plan in `0023-strategist-2` proposes. Two honest caveats: (1) no payment
inequality for it is proved here or anywhere; (2) its window size is bounded by
$d/\max_i\mathrm{Inf}_i(f_A)$ (total-influence budget), so it is
$\mathrm{poly}(d)$-sized exactly when the sparser side of a pair has
$\max_i\mathrm{Inf}_i\ge1/\mathrm{poly}(d)$ — which is P4's uncarded gate
(**[MEMORY: OSSS + depth-vs-degree]**, flagged, not used and not cited in any
claim above).

## L11 (P5: the certificate window escapes)

For $x\in A$ a *certificate* is $T\subseteq[N]$ such that the subcube through $x$
fixing $T$ is contained in $A$; $T_A(x)$ denotes a minimum-size one. Certificate
coordinates of a minimal certificate are relevant (if $i\in T$ is removable-free,
minimality supplies a point where flipping $i$ changes $\mathbf 1_A$), so
$T_A(\cdot)$ is a localised randomised window in the sense of L11.1 when
$x\sim\mathrm{Unif}(A)$. P5's own size bound is $|T_A|\le C(\mathbf 1_A)\le
\mathrm{bs}\cdot s\le(\sqrt{2/3}\,d^2+1)^2=O(d^4)$ (card S6c Thm 1.2 for
$\mathrm{bs}$, plus the textbook $C\le\mathrm{bs}\cdot s$); **that bound is not
needed below** — the witnesses' certificates are computed explicitly.

### L11.1′ Exact values on both witnesses

**(a) Address pair.** For $x\in A_k$ the unique minimum certificate is
$\{a_1,\dots,a_k\}\cup\{y_{b(a)}\}$, of size $d$: leaving an address bit free
allows the read to move to another target (which may be $-1$), and leaving
$y_{b(a)}$ free allows it to flip. Likewise for $y\in B_k$. Hence the windows
are shattering windows, and by L10.1(a)
$$\pi=\tfrac k2+2^{-k},\qquad \frac{\pi}{|T_{A_k}|+|T_{B_k}|}=\frac{k/2+2^{-k}}{2d}\ \ge\ \tfrac18 .$$

**(b) Subcube pair.** For $x\in C$ the unique minimum certificate is $[d]$; for
$y\in D$ a minimum certificate is $\{i\}$ for any $i\le d$ with $y_i=-1$ (size
$1$). Hence
$$\pi=\underbrace{\mathrm{Inf}_i(f_C)}_{=1/2}+\underbrace{\sum_{j\in[d]}\mathrm{Inf}_j(f_D)}_{=d/(2(2^d-1))}\ \ge\ \tfrac12,
\qquad \frac{\pi}{|T_C|+|T_D|}\ \ge\ \frac{1/2}{d+1}=\frac1{2(d+1)} .$$
(Script, exact: payments $5/6,5/7,19/30$ and ratios $5/18,5/28,19/150$ for
$d=2,3,4$, with window sums $\le d+1$.)

**Conclusion.** Both values are $\ge1/\mathrm{poly}(d)$, so **neither witness
caps the certificate route**. Both class hypotheses fail for the same two reasons
as for P1: the window size is $O(d^4)$ *by a theorem about block sensitivity*,
never the relevance count (CAP I vacuous); and on the cheap side $D$ the window
$\{i\}$ consists of a coordinate cheap for its own function (CAP II's hypothesis
fails; L7.5 gives $\ge\frac1{2(d+1)}$).

**Remark L11.2 (a precise drafting warning for P5: average, never worst case).**
P5's stated payment is over $\Sigma(x,y)$, the coordinates the two certificates
fix *oppositely* — a subset of $T_A(x)\cap T_B(y)$, hence a *smaller* payment
than $\pi_W$; so the escape above must be re-checked in that restricted form.
Doing so exactly on witness (a): $x\in A_k$ has address $a$, $y\in B_k$ has
address $a'$, and $i\in\Sigma(x,y)$ iff ($i=a_t$ with $a_t\ne a'_t$) or
($i=y_{b(a)}$ and $a=a'$). Hence
$$\sum_{i\in\Sigma(x,y)}\bigl[\mathrm{Inf}_i(f_{A_k})+\mathrm{Inf}_i(f_{B_k})\bigr]
=\tfrac12\,\bigl|\{t:a_t\ne a'_t\}\bigr|+2^{-k}\mathbf 1\{a=a'\},$$
which is **$2^{-k}=2^{-\Theta(d)}$ in the worst case** (the points whose
addresses agree) but, since $a,a'$ are independent and uniform for
$x\sim\mathrm{Unif}(A_k)$, $y\sim\mathrm{Unif}(B_k)$,
$$\mathbb E_{x,y}\Bigl[\sum_{i\in\Sigma(x,y)}(\cdots)\Bigr]=\frac k4+2^{-2k}\ \ge\ \frac{d-1}4 .$$
On witness (b) every point pair gives $\Sigma(x,y)=\{i\}$ with $y_i=-1$ and
payment $\mathrm{Inf}_i(f_C)+\mathrm{Inf}_i(f_D)\ge\frac12$.
**Conclusion:** P5's *averaged* certificate payment escapes both witnesses
($\ge(d-1)/4$ and $\ge1/2$), but a **per-point** ($\forall x,y$) variant of P5's
inequality is capped at $2^{-\Theta(d)}$ by witness (a). P5's milestone is
correctly stated as an average and must stay that way; this warning is new
relative to `0023-refuter-3` and `0023-strategist-2`. It also shows P5's
assembly needs L11.1's randomised-window count (the average over $x$ is the
window law), not a deterministic one.

## L12 (the exact frontier of the whole method: the single number $\eta^*(d)$)

**Statement.**
1. *(Universal ceiling; L3.2 + L11.1)* For every localised window functional $W$
   — canonical or not, deterministic or randomised, point-indexed or not —
   $V_W(d)\le\eta^*(d):=\inf_{(A,B)\in\mathcal P_d}\sum_{i\in S(A,B)}
   [\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)]$.
2. *(Bracket, L4.3)* $2^{-d}\le\eta^*(d)\le1$, the upper bound attained by the
   $d\times d$ grid pair.
3. *(One-directional sufficiency — stated carefully)* **(a)** If
   $\eta^*(d)=2^{-\Theta(d)}$ — i.e. if there is a cross-disjoint degree-$\le d$
   pair all of whose shared relevant coordinates are cheap **for both sides at
   once** (by L4.2 each shared coordinate contributes $\ge2^{-d}$, so such a pair
   must also have $|S(A,B)|\le2^{\Theta(d)}$) — then **every** localised
   window-payment argument is capped at that level by part 1, and P1, P5,
   $W_{\max}$ and the whole class die together. **(b)** The converse fails, and
   it is important not to claim it: $\eta^*(d)\ge1/\mathrm{poly}(d)$ does *not*
   imply that no further barrier exists — CAP II is a cap obtained while
   $\pi_{\mathrm{Rel}}(C,D)=\Theta(d)$ is large, by making $\pi_W$ collapse far
   below $\pi_{\mathrm{Rel}}$. What $\eta^*(d)\ge1/\mathrm{poly}(d)$ *does*
   establish is that no cap can come from the **localisation ceiling alone**
   (L3.1): any further barrier must, like CAP II, exploit the **window selection
   rule**, not the pair's total shared payment.
4. *(The two certified witnesses provably cannot supply it)*
   $\pi_{\mathrm{Rel}}(A_k,B_k)=\frac{d+1}2$ and
   $\pi_{\mathrm{Rel}}(C,D)=\frac d2+\frac d{2(2^d-1)}$ — both $\Theta(d)$, i.e.
   *large*. So no strengthening of the present witnesses can extend the barrier
   to the whole class.
5. *(Necessary condition for P1, new)* P1's target inequality (PAY$\star$) at
   constant $p$ implies $\eta^*(d)\ge p$. Combined with 2, **(PAY$\star$) at
   $p=1$ forces $\eta^*(d)=1$ exactly**: no cross-disjoint degree-$\le d$ pair
   may have total shared-relevance payment below $1$, with the grid extremal.
   That is a sharp, cheap, falsifiable milestone — *search for a cross-disjoint
   pair with $\pi_{\mathrm{Rel}}<1$* — strictly easier to test than
   (PAY$\star$) itself (it quantifies over no window choices) and strictly
   necessary for it.

**Proof.** 1 is L3.2 (with L11.1 for the randomised case). 2 is L4.3. 3(a) is
part 1 applied to every $W$; 3(b) is the observation that CAP II's proof exhibits
$\pi_W(C,D)=\frac{|W(C)|}{2(2^d-1)}\ll\pi_{\mathrm{Rel}}(C,D)=\Theta(d)$, so the
inequality of part 1 is not the only capping mechanism, together with the trivial
remark that L3.1 is the only pair-based bound available to an argument that knows
nothing about $W$ beyond localisation. 4 is L5(5) and L7.1(4). For 5: (PAY$\star$) says
$\pi_{W_{\mathrm{sh}}}(A,B)\ge p$ for all pairs and all selections; by L3.1
$\pi_{W_{\mathrm{sh}}}\le\pi_{\mathrm{Rel}}$, so $\pi_{\mathrm{Rel}}(A,B)\ge p$
for all pairs, i.e. $\eta^*(d)\ge p$. $\blacksquare$

**The clause-(iv) verdict, stated for the ledger.**

> The strategist's ruling stands: **killer (a) is a statement about
> relevance-denominated windows and killer (b) about own-heavy windows; neither
> binds the $\le d$-sized shattering window (P1) or the $O(d^4)$ certificate
> window (P5), and I have verified this by exact evaluation, obtaining values
> $\ge1/8$ and $\ge1/(2(d+1))$ respectively.** The correct general statement of
> why they escape is the conjunction (α)+(β) of this unit's headline, not the
> min-vs-sum distinction (L7.6). The whole method is nevertheless capped by one
> number, $\eta^*(d)\in[2^{-d},1]$; P1 at $p=1$ requires $\eta^*(d)=1$; and a
> pair with $\eta^*$ exponentially small would kill P1, P5 and the entire class
> at once. **That pair is refuter-3 §6(iii)'s unfound fourth mechanism, and
> $\pi_{\mathrm{Rel}}<1$ is now its precise, checkable signature.**

EMITTED unit 5 of 6. NEXT UNIT: 6 — assembly of `0023-prover-3.md` (verdict, gap
register, dependencies, stage handoff).
ARTIFACT 0023-prover-3.

### END OF ARTIFACT 0023-prover-3-u5 ###
