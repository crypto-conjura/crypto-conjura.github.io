---
id: 0023-refuter-4
agent: refuter
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE
---

# Refuter report, cycle 3 (narrow probe) — rung R2 / I02, the single live question

**Assignment.** Is $\varepsilon^*_{\mathrm{ind}}(3)<1/6$, using degree-$\le3$ sets
over $\mathbb Z_2$ whose windows have size $4,5,6$ — the regime where
`0023-refuter-3` left (LOC-3) false, its own coverage thin (365 disjoint
window-4/5 pairs), and window-6 patterns unenumerable by its recursion.

## VERDICT

**NO COUNTEREXAMPLE IN REGIME + NEAR-MISS (obstruction identified and certified).**

$$\boxed{\ \varepsilon^*_{\mathrm{ind}}(3)=\tfrac16\ \text{ in every regime searched; } \tfrac1{24}\le\varepsilon^*_{\mathrm{ind}}(3)\le\tfrac16\ \text{ overall. } 1/6 \textbf{ SURVIVES.}}$$

Regime, stated exactly (what was **complete** vs **sampled**):

| object | coverage | result |
|---|---|---|
| the class on a window of **6** coordinates | **complete**: all $\lvert L(6,3)\rvert=16\,750\,860$ patterns enumerated | 12 091 128 genuine 6-juntas exist |
| the class on a window of **7** coordinates | **complete**: all $\lvert L(7,3)\rvert=126\,113\,920$ swept | 25 383 680 genuine 7-juntas exist |
| **singleton** pairs (one set per side), windows $\le7$ | **complete** | $\min\Phi=3/16>1/6$; **0** patterns at or below $1/6$ |
| $\kappa_3\le3$ ("no 4 disjoint conflict groups") | **complete for every $N$** (finite reduction, all 95 shapes, two independent linear systems, two primes each) | certified |
| partner set of the $3\times3$ grid's $F$-side | **complete** | exactly the 27 columns $\Rightarrow$ value exactly $1/6$ |
| $F=4$ codim-3 subcubes on disjoint triples ($\bar I_F=1/8<1/6$) | **complete** | partner side **EMPTY** |
| designs at $N=6$ | class complete (16.75 M sets), **seeds sampled** | best $2/11=0.1818$ |
| designs at $N=9$ | universe: **all** window-$\le4$ patterns on **all** windows (2 033 682 placed sets) + sampled window-5/6; **all 91** single-set seeds up to window symmetry | best $1/6$ (the grid), unimproved |
| designs at $N=10,11,12$ | pool-subsampled universes ($\approx1.6\cdot10^5$ placed sets), closure + hill-climb | best $1/6$ |
| windows $8$–$12$ (genuine sets), $d\ge4$ | **not covered** — see §6 | open |

Code: `proofs/0023-refuter-4-code/` (`lib4.py`, `r1a`–`r7`, outputs `*.out`).
Compute $\approx20$ min wall clock. Every reported optimum carries an exact
`Fraction` certificate; the two headline structural facts are each computed
twice by independent methods.

## 1. The window-6 and window-7 classes, completely (the blocked computation)

`0023-refuter-3`'s restriction recursion cost $\lvert L(k-1,3)\rvert^2$ and died
at $k=6$. Grouping by the **degree-exactly-3 integer Walsh coefficients** makes
it output-linear: $\deg(1_P)\le3$ for $P=g\sqcup h$ iff $\deg 1_g,\deg 1_h\le3$
and $g,h$ have identical level-3 coefficients (`lib4`, fact (E2)). Hence

$$\lvert L(k,3)\rvert:\quad 256,\ 12\,870,\ 807\,980,\ \mathbf{16\,750\,860},\ \mathbf{126\,113\,920}\quad(k=3,\dots,7),$$

with $12\,091\,128$ and $25\,383\,680$ genuine (relevant on all $k$).
**Consistency check that validates the whole enumeration:** a degree-3 set is a
cylinder over a genuine pattern, so
$\lvert L(7,3)\rvert=2+\sum_{j\le7}\binom7j\mathrm{gen}(j)$; the right side is
$2+14+210+7630+417\,480+15\,667\,008+84\,637\,896+25\,383\,680=126\,113\,920$ —
**exact agreement** (`r1b`, `r1c`). Two random spot checks (200 members' degrees
by brute-force Walsh transform; 200 non-members confirmed of degree $>3$) also pass.

Two facts used throughout, both elementary and both re-verified exhaustively:
* **(E3) influence floor.** $\partial_i 1_P$ is a nonzero $\{0,\pm\frac12\}$-valued
  polynomial of degree $\le2$, hence nonzero on $\ge\frac14$ of the cube, so
  $\mathrm{Inf}_i(h)=b_i/2^{k-1}\ge\frac14$, i.e. $b_i\ge2^{k-3}$
  ($h=2\cdot1_P-1$). Observed value set, exhaustive for $k\le7$:
  $\mathrm{Inf}_i(h)\in\{\frac14,\frac38,\frac12,\frac58,\frac34,1\}$ — always a
  multiple of $\frac18$, minimum exactly $\frac14=2^{1-d}$.
* **(E3')** consequently every degree-$\le3$ set is a junta on
  $\le\frac{3}{1/4}=12=d2^{d-1}$ coordinates (Nisan–Szegedy, re-derived in one
  line, no citation).

## 2. Singleton pairs: complete for windows $\le7$, and it is a near-miss

For a disjoint pair the value is $\max_i$ influence on each side; both sets must
be **cheap** (all $\mathrm{Inf}_i(f_P)<1/6$, i.e. $b_i<\lvert P\rvert/3$), which
with (E3) forces density $>3/8$ on both — so both densities lie in
$(\frac38,\frac58)$ and the relevant quantity is
$\Phi(P)=\max_i b_i/\bigl(2\min(\lvert P\rvert,2^k-\lvert P\rvert)\bigr)$.

$$\min_{k\le7}\Phi=\mathbf{3/16}=0.1875\ >\ 1/6=0.1667,\qquad
\#\{\Phi<1/6\}=\#\{\Phi=1/6\}=\mathbf 0 .$$

Exhaustive: $k\le5$ gives $1/4$ (reproducing refuter-3's S4A by an independent
implementation), $k=6$ and $k=7$ both give $3/16$. The frontier therefore *does*
improve when windows 6–7 are admitted — $1/4\to3/16$ — and then **stops just
above $1/6$**. Absolute floor: $\Phi\ge2^{-d}=1/8$ by (E3); at $d=2$ the floor
is attained and coincides with $1/(2d)$, at $d=3$ it is not attained.

The $3/16$ minimiser (mask `10507109030461310070`, verified by two influence
methods): balanced ($\lvert P\rvert=32$), all six influences $3/16$,
$T=9/8$, Fourier profile $1/4/4/8$ across levels $0/1/2/3$ with coefficients
$\{\pm\frac18,\frac12\}$. It beats the MUX/address set of the same window
($\max\mathrm{Inf}=1/4$), which is why refuter-3's address analysis stopped at $1/4$.

**Cheap sets do exist** (this kills the "individual functions are protected"
reading): 9 024 at $k=5$, **279 360** at $k=6$, **297 920** at $k=7$. Two
families at $k=6$: density $5/8$ with $\max\mathrm{Inf}=3/20$, and density $3/4$
with $\max\mathrm{Inf}=1/8$ — *exactly the $2^{-d}$ floor*. So a **single**
degree-3 set can hold every influence at $1/8<1/6$; an Aaronson–Ambainis-style
per-function bound is **not** what protects the rung at $d=3$. What protects it
is the partner side: taking $W=A^c$ for every cheap $A$ (all symmetry invariants,
3 representatives each, complete class at $N=6$, `r2` S1):

| cheap seed $A$ | $\tau_F$ (the cheap side) | $\tau_G$ (everything inside $A^c$) |
|---|---|---|
| density $3/4$, $\max\mathrm{Inf}=1/8$ | $1/8$ | $\mathbf{3/8}$ |
| density $5/8$, $\max\mathrm{Inf}=3/20$ | $3/20$ | $\mathbf{1/4}$ |

Cheapness is bought with density, and density confines the partners.

## 3. The obstruction: $\kappa_d\le d$, certified twice

**Definition.** For a nonempty set $A$ let $\kappa(A)$ be the largest number of
**pairwise disjoint** coordinate groups $S_1,\dots,S_m$ with
$\pi_{S_j}(A)\ne\{\pm1\}^{S_j}$ ("$A$ is constrained on $S_j$").

**Why it is the right quantity.** If the $F$-side is $K$ codim-3 subcubes on $K$
disjoint triples then $\bar I_F(i)=1/(2K)<1/6$ for $K\ge4$ — the $F$-side alone
beats $1/(2d)$ effortlessly. Every partner must be constrained on all $K$
triples, so a partner exists only if $\kappa\ge K$. The $3\times3$ grid is the
case $K=3=d$, and it **saturates** $\kappa$.

**Finite reduction (exact).** Restrict every coordinate outside
$S_1\cup\dots\cup S_m$ to a value where $A$ stays nonempty: the restriction is a
nonempty degree-$\le3$ set on $w=\sum\lvert S_j\rvert\le12$ coordinates (by (E3'))
still constrained on the same groups; and after sign flips each missing point is
all-$(+1)$, the *weakest* constraint. So $\kappa\ge m$ is possible iff for some
shape $(s_1,\dots,s_m)$, $\sum s_j\le12$, a nonempty degree-$\le3$ set is
supported in $V=\bigcap_j\{x:x_{S_j}\ne{+}\cdots{+}\}$.

**Result (`r3`, `r5`).** For **all 95 shapes** with $m\in\{4,5\}$ and
$\sum s_j\le12$ the space of degree-$\le3$ functions supported in $V$ is
$\{0\}$ — computed twice by *different* linear systems (value space: $|V|$
unknowns, "level-$\ge4$ coefficients vanish"; coefficient space: $D_3$ unknowns,
"$f(x)=0$ off $V$"), each modulo two primes, all agreeing. Hence

$$\kappa(A)\le 3\quad\text{for every nonempty degree-}{\le}3\text{ set }A,\ \text{in every }N.$$

**Control (validates the framework against settled ground).** The same
computation at $d=2$ returns $\kappa_2\le2$ — consistent with the *proved*
$\varepsilon^*_{\mathrm{ind}}(2)=1/4=1/(2\cdot2)$ attained by the $2\times2$ grid,
i.e. $K=2=d$. The pattern is $\kappa_d\le d$.

**Why it is true, transparently.** The computed dimensions for $m\le3$ obey
$$\dim\{f:\deg f\le d,\ \mathrm{supp}\,f\subseteq V\}=\#\{S:\lvert S\rvert\le d,\ S\cap S_j\ne\emptyset\ \forall j\}$$
(e.g. $m=3$: $\prod_j s_j$; $m=2$: $s t+\binom{s+t}3-\binom s3-\binom t3$;
verified on all 101 shapes with $m\le3$). No set of size $\le d$ can meet $d+1$
disjoint groups, so the dimension is $0$ at $m=d+1$. **This is the heart of the
proof of R2 at $d=3$ and it is what a prover should formalise** (the basis is
explicit: $\prod_j\frac{1-x_{a_j}}2\cdot\prod_{\text{extra}}\frac{1\pm x}2$).

## 4. The grid is exactly optimal *and rigid* (complete sub-result)

For $F=\{$3 codim-3 subcubes on disjoint triples$\}$ ($N=9$): the space of
degree-$\le3$ functions supported in $V(3,3,3)$ has dimension **27**, and the
27 "column" indicators $\prod_{a}\frac{1-x_{c_a}}2$ span exactly that space
(`r5`, rank 27 both primes). Evaluating any element of that span at a point $x$
gives $\sum_{a\in A(x),b\in B(x),c\in C(x)}\lambda_{abc}$; taking
$\lvert A\rvert=\lvert B\rvert=\lvert C\rvert=1$ forces $\lambda\in\{0,1\}$ and
taking $A=T_1,B=T_2,C=T_3$ forces $\sum\lambda\le1$: **at most one $\lambda$ is
$1$**. Adding an outside coordinate $z$ is impossible ($1_B=\frac{1\pm x_z}2 1_C$
has degree 4, and $\frac{1_C+1_{C'}}2+x_z\frac{1_C-1_{C'}}2$ has degree 4 for
distinct columns). So:

> the **only** degree-$\le3$ sets disjoint from three codim-3 subcubes on disjoint
> triples are the 27 columns; each forces one coordinate per triple, so
> $\sum_i\bar I_G(i)=3/2$ over 9 coordinates and the partner side's value is
> **exactly $1/6$**.

Confirmed by search: at $N=9,10,11$ the closure of the grid seed is
$(\lvert F\rvert,\lvert G\rvert)=(27,3)$ with $\tau_F=\tau_G=1/6$ exactly
(`r4`, `r6`), and 30–40 hill-climbing steps from there find nothing better.
And the $K=4$ test: **partner side empty** (`r4` at $N=12$; exactly, by §3).

## 5. Design searches, and the cap on count-based proofs

**Reformulation used (exact, and worth keeping).** Cross-disjointness means
$\bigcup F$ and $\bigcup G$ are disjoint, and enlarging each side to *all* class
sets inside its region only lowers both values, so
$$\varepsilon^*_{\mathrm{ind}}(d,N)=\min_{W\subseteq\{\pm1\}^N}\max\Bigl(\tau\bigl(\{A:A\cap W=\emptyset\}\bigr),\ \tau\bigl(\{B:B\subseteq W\}\bigr)\Bigr),$$
i.e. the search space is the **2-colourings of the cube**, and one evaluation is
two vectorised sweeps plus two $N$-row LPs.

| search | best value | notes |
|---|---|---|
| $N=6$, complete class, cheap seeds + 400 random seeds + local search | $2/11=0.1818$ | multi-set beats the singleton bound $3/16$; still $>1/6$ |
| $N=9$, 2.03 M placed sets, **all 91** single-set seeds up to symmetry | $1/4$ from singles, $\mathbf{1/6}$ from the grid | grid is a strict local optimum |
| $N=10,11,12$, closure + hill-climb, 60 seeds each | $1/6$ | $K=4$ subcubes: partner side empty |

**The count technique is capped at $\rho^*\le1/10$** (`r7`, exact). Define
$\rho^*=\min_{\text{disjoint pairs}}\pi/(\lvert J\rvert+\lvert K\rvert)$ with
$\pi=\sum_{i\in J\cap K}[\mathrm{Inf}_i f+\mathrm{Inf}_i g]$; averaging gives
$\delta\ge\rho^*$ and nothing better. Witness: $A=\{x_0={+}1\}\cap C$ and
$B=\{x_0={-}1\}\cap C'$ with $C,C'$ signed 4-cycles on disjoint quadruples —
each has window 5, influences $(\frac12,\frac14,\frac14,\frac14,\frac14)$
(verified twice), shares only $x_0$, so $\pi=1$ and the ratio is $1/10$. This
sharpens refuter-3's sampled $1/8$ and confirms: **no payment/window count can
reach $1/6$ at $d=3$.** But $\rho^*$ is unattainable by a design — a set forcing
only one coordinate can only meet partners forcing *that* coordinate, making it a
hub of average influence $1/2$. That gap between $\rho^*=1/10$ and the true
$1/6$ is exactly what $\kappa\le d$ explains. (Supporting structure, complete
over the level-6 class: a set forcing $t$ coordinates has window
$\le t+w_{\max}(3-t)$, i.e. $5,3,3$ for $t=1,2,3$; **zero** genuine window-6
sets force anything.)

## 6. What is NOT covered — read this before quoting the verdict

1. **Windows 8–12.** Genuine degree-3 sets exist at window 7; $\lvert L(8,3)\rvert$
   was not computed, so $w_{\max}(3)\in[7,12]$ is **open**. The singleton result
   ($\min\Phi=3/16$) is complete only for windows $\le7$. $\kappa_3\le3$ is
   *not* affected (its reduction caps the window at 12 unconditionally).
   **This is the single most valuable next computation**, and it is now cheap:
   within each level-6 group, level-7 patterns are keyed by the difference of the
   15 degree-2 coefficients, so $\lvert L(8,3)\rvert=\sum(\text{class size})^2$
   over those difference classes, and
   $\mathrm{gen}(8)=\lvert L(8,3)\rvert-2-\sum_{j\le7}\binom8j\mathrm{gen}(j)$.
   Numerically it matters too: the universal payment count gives
   $\delta\ge1/(2w_{\max})$, i.e. $1/24$ today and $\mathbf{1/14}$ if
   $w_{\max}(3)=7$ — a factor $2.3$ from $1/6$, and the cheapest honest route to
   R2 at $d=3$.
2. **Multi-set designs are nowhere complete.** $N=6$ has the complete class but
   sampled seeds; $N=9$ has complete window-$\le4$ patterns but sampled
   window-5/6 and only 91 single-set + 120 multi-set seeds; $N=10$–$12$ are
   pool-subsampled (the $N=12$ pool even lost the codim-3 subcube pattern, which
   is why its $K=3$ line reads 0 partners — a code artefact, not mathematics;
   §3–§4 settle $K\ge4$ exactly and independently).
3. **Designs whose conflict groups overlap.** $\kappa\le d$ kills disjoint-group
   $F$-sides. A general design's groups $\{J_A\cap J_B\}_{A\in\mathrm{supp}F}$
   may pairwise intersect; the maximal-matching/cover step then only yields
   $\delta\ge1/(16\cdot12)=1/192$, weaker than the $1/24$ already available. So
   $\kappa\le d$ is the **mechanism**, not yet the proof.
4. **$d\ge4$ untouched** (beyond the $d=2$ control). $\kappa_d\le d$ would give
   R2 only with an exponential constant, since a cover has size up to
   $d\cdot w_{\max}(d)=2^{\Theta(d)}$ and the minimum influence is
   $2^{-\Theta(d)}$; consistent with refuter-3's barrier.
5. Nothing here touches R3, $\mathbb Z_2$-PCC, or the parent conjecture.

## 7. Implausible-consequence check (§3.4 review update)

$\varepsilon^*_{\mathrm{ind}}(3)<1/6$ implies neither a Minicrypt object in
Pessiland nor a subexponential algorithm — the Impagliazzo-hierarchy test does
not fire (as in refuter-3 §7), and the value $1/6$ is not protected by any
five-worlds argument. The decisive evidence is instead computational and
structural: (i) the singleton frontier is $3/16$ over the *complete* window-$\le7$
class; (ii) $\kappa_3\le3$ holds *for every $N$*; (iii) the grid's closure is
*exactly* $1/6$ with a *unique* partner family. Conversely, a design beating
$1/6$ would have to be a Boolean phenomenon with no disjoint-group structure,
which is a sharp and falsifiable target rather than an implausible one.

## 8. Blueprint handed to the prover (what to prove, in order)

1. **L1 (window).** $w_{\max}(3)\le8$ (or exactly 7): then the universal payment
   inequality $\pi\ge1$ (R1's (F4), true for *arbitrary* sets) plus averaging
   gives $\delta\ge1/(2w_{\max})\ge1/16$ — R2 at $d=3$, unconditionally, in a page.
2. **L2 ($\kappa$).** $\dim\{f:\deg f\le d,\ \mathrm{supp}f\subseteq V(S_1..S_m)\}=\#\{S:\lvert S\rvert\le d,\ S\cap S_j\ne\emptyset\ \forall j\}$,
   hence $\kappa_d\le d$. Basis is explicit (§3); the computation certifies every
   case needed at $d=3$.
3. **L3 (the residual).** Upgrade $\kappa_d\le d$ from *disjoint* to
   *fractionally disjoint* conflict groups. That is the only gap between the
   certified mechanism and $\varepsilon^*_{\mathrm{ind}}(3)=1/6$, and the grid
   (which saturates $\kappa=d$ with equality in every link) is the unique
   extremal configuration to respect.

## 9. Code manifest (`proofs/0023-refuter-4-code/`)

`lib4.py` (grouping recursion for $L(k,3)$, integer Walsh transforms, boundary
counts, two independent exact influence routines) · `r1a_structure.py` (class
sizes $k\le5$, influence quantisation, cheap sets, $\Phi$ frontier $k\le5$;
`r1a.out`) · `r1b_level6.py` (**complete** level 6: enumeration, genuineness,
cheap sets, $\Phi=3/16$, $\lvert L(7,3)\rvert$; writes `L6.npy`, `L6_b.npy`,
`L6_n.npy` — **regenerate by rerunning `r1b`; they are deleted, being 250 MiB, and
are inputs to r1c/r2/r4/r6/r7**; `r1b.out`) · `r1c_level7.py` (**complete** level
7 sweep; `r1c.out`) · `r2_designs_n6.py` (the $W$-formulation; cheap-seed table,
sampled seeds, local search at $N=6$; `r2.out`) · `r3_kappa.py` (window-7
verification by brute force, the $3/16$ object, $\kappa$ in value space;
`r3.out`) · `r5_repertoire.py` ($\kappa$ in coefficient space, the $d=2$ control,
the conflict repertoire, the 27-column completeness; `r5.out`) ·
`r4_designs_bigN.py` (designs at $N=9..12$, $K$-subcube tests; `r4.out`) ·
`r6_n9_dense.py` (dense $N=9$ universe, all single-set seeds up to symmetry;
`r6.out`) · `r7_checks.py` (forcing-vs-window, the exact $\rho^*\le1/10$ witness,
payment sampling, cheapness/density; `r7.out`).
Environment: python 3.14, numpy 2.5.2, scipy 1.18.1 (scipy LPs for search only;
every reported optimum re-certified with `fractions.Fraction`; every rank
computed modulo two primes). No z3 available in this environment; the SAT/ILP
route was replaced by the grouping recursion (§1) and exact linear algebra (§3),
which turned out to be complete rather than heuristic.

### END OF ARTIFACT 0023-refuter-4 ###
