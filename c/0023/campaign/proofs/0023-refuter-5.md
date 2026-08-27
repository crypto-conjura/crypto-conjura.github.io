---
id: 0023-refuter-5
agent: refuter
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE
---

# Refuter report, cycle 3 (one-page decisive milestone) — the RELEVANCE PAYMENT floor

**Assignment (single question).** Is there a cross-disjoint pair of nonempty
degree-$\le d$ sets $A,B\subseteq\{\pm1\}^N$ (any $N$, any $d\ge2$) whose
relevance payment

$$\pi_{\mathrm{Rel}}(A,B)\;:=\;\sum_{i\in\mathrm{Rel}(B)}\mathrm{Inf}_i(f_A)\;+\;\sum_{i\in\mathrm{Rel}(A)}\mathrm{Inf}_i(f_B),
\qquad f_A=\mathbf 1_A/\lVert\mathbf 1_A\rVert_2,$$

is **strictly below 1**? Cross-disjoint means $A\cap B=\emptyset$, both nonempty;
$\mathrm{Rel}(A)$ is the set of coordinates $\mathbf 1_A$ genuinely depends on.
Designed by the barrier prover as a cheap substitute for a much more expensive
hypothesis: a single pair below 1 kills the lead plan's payment constant $p=1$;
a family driving $\pi_{\mathrm{Rel}}$ to $2^{-\Theta(d)}$ kills the technique class.

## VERDICT

**NO COUNTEREXAMPLE — IN ANY REGIME, AND NONE EXISTS: the floor is proved.
Plus a NEAR-MISS that matters (the floor is approached, never crossed, off the
equality manifold).**

$$\boxed{\ \min\pi_{\mathrm{Rel}}=\mathbf 1\ \text{ EXACTLY, over all }N\text{, all }d\ge1,\ \text{no degree restriction needed;}\ \ \pi_{\mathrm{Rel}}<1\ \text{is IMPOSSIBLE.}\ }$$

Three sharper statements, each certified below:

1. **Attainment, and only there.** $\pi_{\mathrm{Rel}}(A,B)=1$ **iff**
   $|S|=1$ where $S:=\mathrm{Rel}(A)\cap\mathrm{Rel}(B)$, and then necessarily
   $A$ and $B$ lie in opposite halves of that one coordinate, whereupon
   $\pi_{\mathrm{Rel}}=\tfrac12+\tfrac12=1$ *identically*, whatever the two sets
   do inside their halves. The ACC22 Claim B.3 grid pair (NegRow/PosCol) is in
   this family, at every $d$. (The "$\Leftarrow$" direction is a two-line
   identity; "$\Rightarrow$" is proved in §3 modulo the standard
   edge-isoperimetric equality case, which is verified exhaustively here for
   $m\le4$, and is verified end-to-end for all pairs at $N\le4$.)
2. **No $d$-decay.** $\min\pi_{\mathrm{Rel}}=1$ for **every** $d\ge1$, attained
   at degree exactly $d$ by codim-$d$ subcube pairs whose windows meet in one
   coordinate. The quantity does not decay in $d$ at all — polynomially or
   otherwise — so **this test does not kill the technique class**.
3. **But there is no slack off the equality manifold.** The $|S|\ge2$ branch has
   infimum exactly 1, *not attained*: an explicit family gives, at degree exactly
   $d$, pairs with $|S|=2$ and $\pi_{\mathrm{Rel}}=1+\dfrac1{2^{\,d-1}-1}$ for
   every $d\ge2$, and this coincides with the complete-sweep minimum of the
   $|S|\ge2$ branch wherever a complete answer exists ($4/3$ at $d=2,3$; $8/7$ at
   $d=4$). So a case split "either $|S|=1$, or $|S|\ge2$ where I have room"
   buys at most $2^{-\Theta(d)}$ — never $1/\mathrm{poly}(d)$.

Code: `proofs/0023-refuter-5-code/` (`lib5.py`, `x1`–`x9`, outputs `x*.out`).
Compute $\approx14$ min wall clock. Every reported optimum carries an exact
integer/`Fraction` certificate; the headline quantity is computed by two
independent methods (boundary counting and the integer Walsh transform) and the
minimum is established both by search and by proof.

## 1. The quantity in integer form (the certificate format)

Re-derived, no citation (`lib5` (P1)–(P3)). With $b_i(A):=\#\{x\in A: x^{\oplus i}\notin A\}$,

$$\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E[(\partial_i\mathbf 1_A)^2]=\tfrac14\Pr_x[\mathbf 1_A(x)\ne\mathbf 1_A(x^{\oplus i})]=\frac{b_i(A)}{2^{N+1}},
\qquad \mathrm{Inf}_i(f_A)=\frac{b_i(A)}{2|A|},$$

and $\mathrm{Rel}(A)=\{i: b_i(A)>0\}$. Since $\mathrm{Inf}_i(f_A)=0$ off
$\mathrm{Rel}(A)$, the payment is supported on the **shared** relevance:

$$\pi_{\mathrm{Rel}}(A,B)=\sum_{i\in S}\Bigl[\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)\Bigr]
=\frac{\mathrm{Num}}{2|A||B|},\quad
\mathrm{Num}=\sum_{i\in S}\bigl(b_i(A)|B|+b_i(B)|A|\bigr),$$

so the test "$\pi_{\mathrm{Rel}}<1$" is the **all-integer** test
$\mathrm{Num}<2|A||B|$ — no floating point anywhere in the decision. Writing
$r_i(A):=b_i(A)/|A|$ (relative boundary), $\pi_{\mathrm{Rel}}=\frac12\bigl[\sum_{i\in S}r_i(A)+\sum_{i\in S}r_i(B)\bigr]$.

Cross-check of the formula against the Fourier definition
$\mathrm{Inf}_i(f)=\sum_{T\ni i}\hat f(T)^2$ with an integer Walsh transform, and
of $\mathrm{Rel}$ against the Fourier support: **0 mismatches on every
cross-disjoint pair at $N\le3$ (6050 pairs)**, and on every structured witness
in §5 (`x1.out`, `x4.out`).

## 2. Search space covered — exactly what was complete and what was sampled

The block form below is **not a restriction**: put $S=\mathrm{Rel}(A)\cap\mathrm{Rel}(B)$;
$A$ is a cylinder over $S\cup P_A$, $B$ over $S\cup P_B$ with $P_A\cap P_B=\emptyset$,
and coordinates relevant to neither change nothing ($b_i$ and $|A|$ scale
together). So "each side has $\le k$ relevant coordinates" is the only real
parameter, and it is **independent of $N$**.

| object | coverage | result |
|---|---|---|
| all cross-disjoint pairs at $N\le3$ | **complete**, two independent methods | $\min=1$; 0 below |
| all cross-disjoint pairs at $N=4$ | **complete**: all $3^{16}$ labellings, 42 915 650 ordered pairs, integer-exact | $\min=1$; **0 below**; 5224 pairs at exactly 1; $S=\emptyset$ never occurs |
| **arbitrary degree**, every pair with $\le4$ relevant coords per side, **every $N$** | **complete**: exactly **16 957 208 176** ordered pairs (block tables; largest single $(k_A,k_B)$ cell $4\,261\,478\,400$) | $\min=1$; per-$|S|$ minima $8/7,\,9/7,\,80/63$ for $|S|=2,3,4$ |
| **degree $\le3$**, every pair with $\le6$ relevant coords per side and $|S|\le4$, **every $N$** | **complete** over the classes $L(k,3)$, $k\le6$ (16 750 860 sets): exactly **970 576 069 559 784** ordered pairs ($9.7\cdot10^{14}$) | $\min=1$; $|S|=2,3,4$ minima $4/3,4/3,3/2$ |
| **degree $\le2$**, **entire class, every $N$** (a degree-2 set is a junta on $\le4$ coords, so the $\le6$ sweep is exhaustive) | **complete**: 1 801 512 ordered pairs | $\min=1$; $|S|\ge2$ minimum $=4/3$ |
| complementary pairs $(A,A^c)$ | **complete** at $N\le4$; identity proved | $\min=1$ iff $\deg=1$; grows with degree |
| measure-level relaxation $\min[T(\nu)+T(\omega)]$, disjoint supports | **complete** over rational grids, $m\le4$ (up to 490 314 measures per $m$) | $=2$ exactly, i.e. payment floor 1, matching the proved bound |
| equality manifold ($\pi=1$) | **complete** at $N\le4$; edge-isoperimetric equality case complete for $m\le4$ | $\pi=1\iff|S|=1$, no exceptions |
| raw ternary-labelling annealing, $N=5,6,7,8,9$ | sampled (540 runs, $2.3\cdot10^7$ evaluated states), **uses none of the structure above** | best exactly $1$ at $N=5,6,7,8$; $8171/6972$ at $N=9$ (budget-limited); **0 runs below 1** |
| fibre-representation annealing, $|S|\le6$, $N\le18$ | sampled (the regime where the infimum is *approached*) | best $=1$; 0 below 1 |
| link L3 ($2\,\mathrm{TV}(\nu,U)\le T(\nu)$) | 144 000 random measures, $m\le10$, + 300 exact-rational | 0 violations |
| $\mathcal Y=\mathbb Z_q$, $q>2$ | **complete** for $\mathbb Z_3^1,\mathbb Z_5^1,\mathbb Z_7^1,\mathbb Z_3^2$; annealing for $\mathbb Z_4^2,\mathbb Z_3^3,\mathbb Z_5^2$ | $\min=1$ exactly there too; 0 below |
| **not covered by search:** degree $\le3$ with $7$–$12$ relevant coords per side, $|S|\ge5$, degree $\ge4$ beyond 4 relevant coords per side, general $\mathcal Y$ at larger $N$ | — | covered instead by the **proof** in §3 (for $\mathcal Y=\mathbb Z_2$); for $\mathcal Y\ne\mathbb Z_2$ the floor is unproved (§6) |

## 3. Why it cannot go below 1 — the obstruction, in four links

This is the near-miss analysis §3.4(4) turned into a proof of the floor. Each
link is elementary and each was verified numerically before being believed
(`x2.out`; the chain was checked on **all** 6050 pairs at $N=3$ and on 120 000
random pairs at $N=4,5,6$, with zero violations at every link).

Let $S=\mathrm{Rel}(A)\cap\mathrm{Rel}(B)$, $m=|S|$; for $y\in\{\pm1\}^S$ let
$A_y,B_y$ be the fibres and put $\nu(y)=|A_y|/|A|$, $\omega(y)=|B_y|/|B|$
(probability measures on $\{\pm1\}^S$).

**(L1) Shared relevance is nonempty, and the shadows are disjoint.**
If $A_y\ne\emptyset\ne B_y$, pick $z_A\in A_y$, $z_B\in B_y$ and build $z$
agreeing with $z_A$ on $\mathrm{Rel}(A)\setminus S$ and with $z_B$ on
$\mathrm{Rel}(B)\setminus S$ (disjoint blocks). $A$ depends only on
$S\cup(\mathrm{Rel}(A)\setminus S)$, so $(y,z)\in A$; likewise $(y,z)\in B$ —
contradicting $A\cap B=\emptyset$. Hence $Y_A:=\mathrm{supp}\,\nu$ and
$Y_B:=\mathrm{supp}\,\omega$ are **disjoint**, both nonempty, so $m\ge1$: a
cross-disjoint pair can never have $S=\emptyset$ (which would make the payment
$0$). *This is the only place disjointness is used, and it is used in full.*

**(L2) Fibre-mass bound.** At least $(|A_y|-|A_{y^{\oplus i}}|)_+$ points of
$A_y$ have their $i$-flip outside $A$, so
$r_i(A)\ge\sum_y(\nu(y)-\nu(y^{\oplus i}))_+=:D_i(\nu)$, whence
$\sum_{i\in S}r_i(A)\ge T(\nu):=\sum_{i\in S}D_i(\nu)$.

**(L3) Flip-averaging (the only non-counting step).** $D_i(\nu)=\mathrm{TV}(\nu,\sigma_i\nu)$
for the coordinate flip $\sigma_i$; flips commute, so
$\mathrm{TV}(\nu,\sigma_J\nu)\le\sum_{i\in J}D_i(\nu)$, and averaging over all
$2^m$ subsets $J$ — which maps $\nu$ to the uniform measure $U$ — gives

$$\mathrm{TV}(\nu,U)\;\le\;2^{-m}\sum_J\mathrm{TV}(\nu,\sigma_J\nu)\;\le\;2^{-m}\sum_J\sum_{i\in J}D_i(\nu)\;=\;\tfrac12T(\nu).$$

Independently $\mathrm{TV}(\nu,U)\ge\nu(Y_A)-U(Y_A)=1-|Y_A|/2^m$.

**(L4) The floor.** Disjointness gives $|Y_A|+|Y_B|\le2^m$, so

$$T(\nu)+T(\omega)\;\ge\;2\Bigl[\bigl(1-\tfrac{|Y_A|}{2^m}\bigr)+\bigl(1-\tfrac{|Y_B|}{2^m}\bigr)\Bigr]\;\ge\;2,
\qquad\text{hence}\qquad \pi_{\mathrm{Rel}}\;\ge\;1 .\qquad\blacksquare$$

The relaxation is **tight**, not merely valid: any dyadic measure pair with
disjoint supports is realised exactly by a set pair (take nested prefix fibres
over a fixed order in each private block, which makes L2 an equality), which is
why the measure-level minimum computed exhaustively in `x2` is exactly 2 and why
the search and the bound agree to the last digit.

**Equality analysis (why $|S|\ge2$ can never attain it).** Equality forces
equality at every link. In L3 the averaging step is equality only if, for each
$y$, all differences $\nu(y)-\nu(y')$ have one sign — i.e. every value of $\nu$
is its max or its min, so $\nu$ takes two values and, being $0$ off $Y_A$, is
**uniform on $Y_A$**; then $T(\nu)=|E(Y_A,Y_A^c)|/|Y_A|$ and L4 forces
$|Y_A|=2^{m-1}$ with $|E(Y_A,Y_A^c)|=2^{m-1}$. The edge-isoperimetric equality
case (standard; verified exhaustively here for $m\le4$: the only such sets are
the $2m$ codim-1 subcubes) then makes $Y_A$ a codim-1 subcube, whose uniform
measure has $D_i=0$ for all but one $i$ — contradicting $D_i=r_i>0$ for all
$i\in S$ unless $m=1$. Verified independently and completely at $N\le4$:
**every** pair with $\pi=1$ has $|S|=1$ and lies in opposite halves; **every**
pair with $|S|=1$ has $\pi=1$ (`x6.out`).

## 4. The equality manifold is large, and the plan must be exactly tight on it

At $N=4$, 5224 of the 42 915 650 ordered cross-disjoint pairs sit exactly at 1;
the family is characterised, not sporadic: *fix a coordinate $i$; let $A$ be any
nonempty subset of $\{x_i=+1\}$ and $B$ any nonempty subset of $\{x_i=-1\}$ such
that no coordinate other than $i$ is relevant to both.* Then
$b_i(A)=|A|$, $b_i(B)=|B|$, $S=\{i\}$, and $\pi_{\mathrm{Rel}}=1$ regardless of
everything else. Members include:

* the ACC22 Claim B.3 **grid** pair (row all $-1$ / column all $+1$): verified
  exactly for the full $d\times d$ grid at $d=2,3,4$ ($N=4,9,16$) and by the
  one-line formula for all $d$;
* every **codim-$d$ subcube pair** whose windows meet in exactly one coordinate,
  degree exactly $d$;
* every **hub/address** pair (a shared decision coordinate, arbitrary private
  patterns) — four random instances at $N=7$ all exactly 1.

Consequence for the lead plan: $p=1$ is **exactly** the largest admissible
payment constant, and the bound is tight on a rich family that includes the
campaign's known extremal object. Any step that loses a constant factor at the
payment stage, or that needs strict inequality without treating this family
separately, fails.

## 5. Near-misses (the finding a prover most needs)

Two exact families approach the floor from above with $|S|\ge2$; both were found
by the complete block sweep and then verified by materialising the pair and
evaluating from the definition (`x4.out`).

**(F5′) Punctured-half pair, $|S|=2$, degree-controlled.** $H=\{x_0=+1\}$;
$C_A\subset H$ the codim-$(2+p)$ subcube fixing $x_1=-1$ and $A$'s private block,
$C_B\subset H^c$ likewise with $B$'s own private block; $A=H\setminus C_A$,
$B=H^c\setminus C_B$. Then $\deg\mathbf 1_A=\deg\mathbf 1_B=2+p$, $|S|=2$ and

$$\pi_{\mathrm{Rel}}=1+\frac1{2^{p+1}-1}=1+\frac1{2^{\,d-1}-1}\quad(d=2+p),$$

verified exactly for $p=0,\dots,4$: $2,\ 4/3,\ 8/7,\ 16/15,\ 32/31$. These match
the complete sweeps ($4/3$ at $d\le3$, $8/7$ at degree 4 with $\le4$ relevant
coords per side), so the law is *sharp* in every regime where a complete answer
exists.

**(F4) Punctured halfcube, $|S|=N$.** $A=H\setminus\{p\}$, $B=H^c\cup\{p\}$:
$\pi_{\mathrm{Rel}}=1+\Theta(N2^{-N})$ exactly ($80/63$, $304/255$, $384/341$,
…, $1404928/1398101$ at $N=4,\dots,12$), with **every** coordinate relevant to
both sides.

**What this rules out.** The infimum over $|S|\ge2$ is exactly 1. So:
*there is no constant, and no inverse polynomial in $d$, of extra payment
available on the $|S|\ge2$ branch* — at degree $d$ the available surplus is at
most $2^{-\Theta(d)}$, exactly the scale the rung is trying to escape. A plan
that hopes to gain by splitting on $|S|$ gains nothing usable; a plan that
charges the payment only against $S$ must be exactly tight.

**What obstructs pushing below 1** is precisely L1+L3: to have small relative
boundary on the shared coordinates a set must spread over the shared cube, but
disjointness forces the two shadows into disjoint halves of it, and the
flip-averaging inequality says separating a probability measure from uniform by
$t$ in total variation costs total shared boundary at least $2t$. Concentration
tricks (mass on a deep interior fibre) fail because a heavy fibre next to a light
one is itself boundary — that is exactly the term L2 keeps.

## 6. Degree behaviour, and other groups

* **No decay in $d$.** $\min_{\deg\le d}\pi_{\mathrm{Rel}}=1$ for every $d\ge1$,
  attained at degree exactly $d$; the *second* level (the $|S|\ge2$ branch) is
  $1+1/(2^{d-1}-1)\downarrow1$, i.e. it decays to the floor exponentially in $d$
  but never through it. Complementary pairs move the other way:
  $\pi_{\mathrm{Rel}}(A,A^c)=I(h)/(4\alpha(1-\alpha))$ with $h=2\cdot\mathbf 1_A-1$
  (identity verified on all 65 534 complementary pairs at $N=4$), which is
  $\ge1$ by $I(h)\ge\mathrm{Var}(h)$ with equality iff $\deg h=1$, and grows like
  $d/2$ for codim-$d$ subcubes.
* **Other groups (the Contract's group is existentially quantified).** Using
  $\mathrm{Inf}_i(f)=\tfrac12\mathbb E|f(x)-f(x')|^2$ ($x'$ = $x$ with coordinate
  $i$ re-randomised), which for $\mathcal Y=\mathbb Z_q$ gives the exact integer
  form $\mathrm{Inf}_i(f_A)=1-\bigl(\sum_L|A\cap L|^2\bigr)/(q|A|)$ over lines
  $L$ in direction $i$ (engine cross-checked against the Boolean formula on every
  pair at $N\le3$): $\min\pi_{\mathrm{Rel}}=1$ **exactly** for
  $\mathbb Z_3^1,\mathbb Z_5^1,\mathbb Z_7^1,\mathbb Z_3^2$ (complete sweeps) and
  for $\mathbb Z_4^2,\mathbb Z_3^3,\mathbb Z_5^2$ (annealing), attained by
  "one point vs. the other $q-1$ points" ($\mathrm{Inf}=(q-1)/q$ and $1/q$). So
  the floor 1 is **not** Boolean-specific and no group is cheaper — but the L3
  proof is Boolean (it averages over the flip group), so for
  $\mathcal Y\ne\mathbb Z_2$ the floor is **searched, not proved**.

## 7. IMPLAUSIBLE CONSEQUENCE check

The tested statement is a finite combinatorial identity about $\{\pm1\}^N$; it
places no object in any of Impagliazzo's worlds and yields no algorithm, so the
verdict class does not fire. The one derived consequence worth testing is the
*calibration* against the frozen ceiling K2 (card S1, ACC22 Claim B.3: over
$\mathbb Z_2$ any witnessing $\delta$ needs $\delta(d)<1/(2d)$). The connection is
visible in the grid itself, with no reference to the plan: in the $d\times d$ grid
distributions the payment is $1$ per pair, split $\tfrac12/\tfrac12$ between the
sides, and each side spreads its $\tfrac12$ over $d$ equally likely functions
whose relevant windows partition the coordinates — so the per-coordinate average
influence is exactly $\tfrac12/d=1/(2d)$. A payment floor $p$ therefore
corresponds to a licensable threshold $\delta<p/(2d)$; at $p=1$ that is **exactly**
the K2 ceiling, reached but not exceeded, with the grid pair simultaneously the
K2 witness and a $\pi_{\mathrm{Rel}}=1$ equality case. Two things follow: a derivation returning
$p>1$ would contradict K2 and must be wrong; a derivation returning $\delta\ge1/(2d)$
(non-strict) would contradict K2 and must be wrong. $p=1$ with a strict
inequality is the unique consistent landing point — i.e. the constant is not
merely admissible, it is forced. (Stated conditionally: the accounting step from
payment to $\delta$ is the plan's, and this refuter did not read the plan.)

## 8. What this null result does and does not rule out

**Does rule out:** any refutation of the lead plan by exhibiting a cheap
cross-disjoint pair; any hope of a $2^{-\Theta(d)}$ payment collapse (the
quantity is $\ge1$ for all $d$, so the technique class survives *this* test);
any claim that the constant should be smaller than 1 (it is attained) or could be
larger than 1 (it is attained); and — via §5 — any argument that extracts
$1/\mathrm{poly}(d)$ of slack from the $|S|\ge2$ case.

**Does not rule out:** (i) failure of the plan *elsewhere* — this tests one
inequality, not the conversion from payment to a $\delta$ threshold, nor the
distributional step (note only that $\pi_{\mathrm{Rel}}\ge1$ pointwise implies
$\mathbb E\pi_{\mathrm{Rel}}\ge1$ for any distribution over cross-disjoint pairs,
so nothing is lost by averaging, but an LP/dual value such as `0023-refuter-3`'s
$\tau$ is a *different* quantity and is not bounded by this); (ii) a payment
defined against $\mathrm{Rel}(A)\cup\mathrm{Rel}(B)$, or against a coordinate set
larger than $S$, which is a different functional and was not tested; (iii) the
non-Boolean groups, where the floor is empirically 1 but the proof does not
transfer; (iv) the possibility that the true difficulty of rung R2 lives in
regimes where $|S|$ is large and the payment is *big* (§5's F7: majority-type
pairs sharing every coordinate pay $\Theta(\sqrt N)$) — the payment being large
there does not by itself bound the per-coordinate influences, which is what the
rung needs.

## 9. Reproduction

```
proofs/0023-refuter-5-code/
  lib5.py             exact payment machinery: (P1) boundary influence,
                      (P2) Rel, (P3) integer form; Fourier cross-check
  x1_exhaustive.py    complete N<=4 sweep (3^16 labellings)          -> x1.out
  x2_reduction.py     the chain L1-L4 on explicit pairs + exhaustive
                      measure relaxation for m<=4                    -> x2.out
  x3_blocks.py        complete block-form pair sweeps (arbitrary degree
                      k<=4; degree<=3 and <=2 with L(k,3), k<=6)     -> x3.out
  x4_structured.py    named families F1-F7 exactly, d-scaling        -> x4.out
  x5_anneal.py        structure-free annealing, N=5..9               -> x5.out
  x6_equality.py      equality manifold + isoperimetric equality case -> x6.out
  x7_fiber_hunt.py    fibre-representation hunt to N=18 + L3 stress  -> x7.out
  x8_groups.py        Z_q version, exhaustive and annealed           -> x8.out
  x9_counts.py        exact size of the pair space swept by x3       -> x9.out
```
Run with a python that has numpy (`/usr/local/bin/python3.13` here); no scipy
required.

### STATE DELTA

Artifact: `0023-refuter-5`; Status: COMPLETE.
Established: $\min\pi_{\mathrm{Rel}}=1$ exactly over all cross-disjoint pairs
(all $N$, all $d$), **not** below; attained iff $|\mathrm{Rel}(A)\cap\mathrm{Rel}(B)|=1$;
proof of the floor via shadow-disjointness + flip-averaging, verified at every
link; the $|S|\ge2$ branch has infimum 1 with degree-$d$ surplus exactly
$1/(2^{d-1}-1)$.
Killed: the possibility of refuting the payment constant $p=1$ by a cheap pair;
the hope of $1/\mathrm{poly}(d)$ slack on the $|S|\ge2$ branch.
Conditional: the floor for $\mathcal Y\ne\mathbb Z_2$ (searched, unproved).
New sources: none.
NEXT ACTION: hand §3's four-link proof to the barrier prover as the calibrated
input for the $p=1$ payment step of the R2 plan (it is a lemma, not just a search
result), and have the next prover unit state the payment-to-$\delta$ accounting
that must keep $\delta<1/(2d)$ strict.
If interrupted here: the campaign loses the only exact determination of the
payment floor and the two near-miss families that pin its slack.

### END OF ARTIFACT 0023-refuter-5 ###
