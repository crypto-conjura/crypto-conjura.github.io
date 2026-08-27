---
id: 0023-refuter-2
agent: refuter
model: claude-fable-5
cycle: 2
status: COMPLETE
---

# Refuter report, cycle 2 — rung R1 / intermediate I01 (spread-junta indicators, ℤ₂)

**Target:** I01 (`intermediates/I01-spread-junta.md`), assumed FALSE; hunted for
incompatible pairs of distributions over
$\mathcal{C}^{\mathrm{junta}}_d = \{\mathbf 1_A/\|\mathbf 1_A\|_2 : A=\{x: x_J\in P\},\ |J|\le d,\ \emptyset\neq P\subseteq\{\pm1\}^J\}$
with max per-coordinate average influence below every inverse polynomial in $d$.

## VERDICT

**NO COUNTEREXAMPLE IN REGIME [exact-exhaustive at $(d,N)\in\{(2,2),(2,3),(2,4),(3,3),(3,4)\}$;
all structured product/grid/tribes/ball/parity/affine architectures at general $d$ (exact);
1,712 stochastic + hill-climbed free-form families at $d\le 6$, $N\le 12$],**
and stronger: the search terminated in a fully quantitative obstruction — an
elementary five-step counting chain, every step verified in exact arithmetic at
scale, which pins the incompatible-family frontier of this class at **exactly
$1/(2d)$**. If the chain survives prover write-up and verification, rung R1 is
**TRUE with $\delta(d)=\theta/(2d)$ for any $\theta<1$ (e.g. $\delta(d)=1/(3d)$), optimally** —
the grid ceiling $1/(2d)$ is not just an upper bound for the class, it is the exact frontier.
Pattern richness cannot push the frontier below $\Theta(1/d)$; it cannot even improve the
grid's constant. The falsification honeypot fails. The answer to the rung's money question
("can relative influences as small as $2^{-\Theta(d)}$ help?") is a certified **no**, and §5
says precisely why.

Code: `proofs/0023-refuter-2-code/` (imports `../0023-refuter-1-code/pcc_lib.py`);
total compute ≈ 2.5 min wall clock.

## 1. Exact structural facts (each verified in exact arithmetic; proofs one line each)

Write $k=|J|$, $\mu=|P|/2^k$, and for a direction $i\in J$ let $b_i(P)$ = number of
$i$-edges of the cube $\{\pm1\}^J$ with exactly one endpoint in $P$. For $S\subseteq J$ let
$\nu_P(S)=|\pi_S(P)|/2^{|S|}$ (projection density). Verified in `t1_formula_and_lemmaA.py`:

* **(F1) Influence formula.** $\mathrm{Inf}_i(\mathbf 1_A/\|\mathbf 1_A\|_2) = b_i(P)/(2|P|)$
  for $i\in J$, else $0$. (Discrete-derivative identity; cross-checked against exact
  integer Walsh–Hadamard, exhaustive $k\le3$, 500 random $k\le8$.)
* **(F2) Disjointness = projection disjointness.** $A\cap B=\emptyset$ iff
  $\pi_S(P_A)\cap\pi_S(P_B)=\emptyset$ on $S=J_A\cap J_B$; in particular $S\neq\emptyset$
  is forced (nonempty patterns on disjoint windows always meet). (Lift/restrict; checked
  against brute-force support intersection, 2,700 pairs.)
* **(F3) Projection-density payment ("Lemma A").** For every $S\subseteq J$:
  $\sum_{i\in S}\mathrm{Inf}_i(f_P)\ \ge\ \tfrac12\log_2\!\big(1/\nu_P(S)\big)$.
  Integer-exact form $2^{\sum_S b_i}\cdot|\pi_S P|^{|P|}\ge 2^{|S||P|}$.
  Proof route: group $i$-edges ($i\in S$) over their $S$-projection to get
  $\sum_{S} b_i(P)\ \ge\ \mathrm{TV}_S(w)$ for the fiber-count function
  $w(u)=|P\cap\pi_S^{-1}(u)|$; layer-cake $\mathrm{TV}(w)=\sum_t|\partial_E\{w\ge t\}|$;
  hypercube edge-isoperimetry $|\partial_E T|\ge|T|\log_2(2^{|S|}/|T|)$ on each level set
  ($\subseteq \pi_S P$). **Verified exhaustively for all $984{,}858$ (pattern, $S$) pairs with
  $k\le4$ and 200,000 random cases $k\in[5,12]$; zero violations.**
  [External ingredient, MEMORY-grade until written: the standard edge-isoperimetric
  inequality; provable inline in half a page by induction on $n$ — recommended, keeps I01
  self-contained.]
* **(F4) Per-pair payment ≥ 1.** If $f,g$ have disjoint supports with shared window $S$,
  then $\nu_f(S)+\nu_g(S)\le1$, so $\nu_f\nu_g\le\tfrac14$, and by (F3) twice:
  $\sum_{i\in S}\big[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)\big]\ \ge\ \tfrac12\log_2\tfrac{1}{\nu_f\nu_g}\ \ge\ 1 .$
  Integer-exact form $|Q|\sum_S b_i(P)+|P|\sum_S b_i(Q)\ge2|P||Q|$. **Verified on 20,000+
  random disjoint pairs; minimum observed payment exactly 1 (tight).**

## 2. The candidate theorem (the obstruction, in final form)

**Master count (M).** Let $(\mathbf F,\mathbf G)$ be incompatible over
$\mathcal{C}^{\mathrm{junta}}_d$, $\delta_F=\max_i\mathbb E_{\mathbf F}\mathrm{Inf}_i$,
$\delta_G=\max_i\mathbb E_{\mathbf G}\mathrm{Inf}_i$. Draw $f_a\sim\mathbf F$, $g_b\sim\mathbf G$
independently; apply (F4) to each pair and take expectations:
$$1\ \le\ \mathbb E_{a,b}\Big[\sum_{i\in J_a\cap K_b}\mathrm{Inf}_i(f_a)+\mathrm{Inf}_i(g_b)\Big]
\ \le\ \sum_i \Pr_b[i\in K_b]\,\overline{I}_F(i)\ +\ \sum_i\Pr_a[i\in J_a]\,\overline{I}_G(i)
\ \le\ \delta_F\,\mathbb E_b|K_b|+\delta_G\,\mathbb E_a|J_a|\ \le\ (\delta_F+\delta_G)\,d .$$
Hence $\boxed{\ \max(\delta_F,\delta_G)\ \ge\ 1/(2d)\ }$ — and the grid attains it, so
$\varepsilon^*_{\mathrm{junta}}(d)=1/(2d)$ exactly, with the strict threshold matching
K2/Claim B.3 in both directions. The refined form
$\delta_F\,\mathbb E_b|K_b|+\delta_G\,\mathbb E_a|J_a|\ge1$ trades the two sides' window
budgets. The whole chain (F1)→(M) was audited end-to-end in exact rational arithmetic on
the $d=3$ grid and 25 random repaired configurations (`t5`, section T5c): every
intermediate quantity satisfies its inequality, and the grid meets **every** link with
equality ($\mathbb E[\text{payment}]=1$, $\delta_F\mathbb E|K|+\delta_G\mathbb E|J|=1$).

This is a union-bound **replacement** (weighted counting + isoperimetry), no pattern
enumeration, no $2^{2^d}$ constants: the rung's **generalization hypothesis is satisfied**
by this proof route.

## 3. Target 1 — exact small cases (all certified in rational arithmetic)

Method: partition sweep of $\{\pm1\}^N$ up to cube symmetry (reps from predecessor's
`pcc_lib`), per side the distribution optimum is an LP
$\tau=\min_p\max_i\sum_a p_a I_a(i)$; float sweep, then exact dual (lower, every feasible
orbit) and mixture (upper, best orbit) certificates. `t2_exact_small.py`:

| $(d,N)$ | orbits (feasible) | $\varepsilon^*_{\mathrm{junta}}$ | vs $1/(2d)$ | full-class value (refuter-1) |
|---|---|---|---|---|
| (2,2) | 3 | **1/2** exact | above | — |
| (2,3) | 8 | **1/3** exact | above | 1/4 |
| (2,4) | 59 | **1/4** exact | $=1/(2d)$, grid-attained | **1/5** |
| (3,3) | 13 | **1/4** exact | above ($d{=}3$ grid needs $N{=}9$) | — |
| (3,4) | 201 | **1/4** exact | above | ≈ 0.18668 |

Two findings. (i) **No pattern-rich configuration beats the grid**: at $(2,4)$ the minimum
over *all* partitions and *all* junta distributions is exactly $1/4=1/(2d)$. (ii) The junta
frontier and the full signed-class frontier **provably diverge already at $d=2$**
($1/4$ vs $1/5$): the sub-$1/(2d)$ full-class records are essentially non-indicator objects.

## 4. Target 2 — structured families at general $d$ (exact, `t3_structured.py`)

All in-class; $\varepsilon\cdot d$ charted; product rule and closed forms first verified
against brute-force `JFun` instances; cross-disjointness and payments exact.

| architecture | $\varepsilon\cdot d$ | where the payment chain bites |
|---|---|---|
| conjunction grid ($D{\times}D$, $s{=}1$) | $1/2$ | equality throughout (M): the extremal object |
| parity cells, size $s$ | $s/2$ | overpays: payment $=|S|=s$ per pair vs required 1 |
| affine-subspace cells | $\ge 1/2$ | $b_i\in\{0,|P|\}$, so influence $\in\{0,\tfrac12\}$: reduces to conjunction behavior |
| tribes cells $(w,T)$, grid | min $=1/2$ at $(1,1)$; grows $\approx w/2$ | KKL tax: spreading boundary at density $\tfrac12$ inflates total influence $\Theta(\log s)\times$ Harper's floor |
| tribes vs complement, single pair $N{=}d$ | min $=1/2$ at $d{=}1$; $\Theta(\log d)$ profile | same |
| Hamming ball vs complement ($k\le40$, all $\rho$) | min $=1/2$ | majority-boundary $\Theta(\sqrt d)$ or forced-coordinate 1/2 |
| point vs complement (density $2^{-s}$) | $s/2$ | sparse side overpays $\tfrac12\log_2(1/\mu)=s/2$ |
| $\varphi(s)$: best disjoint cell pair, **exhaustive** $s\le3$ | $\varphi(1)=\tfrac12,\ \varphi(2)=1,\ \varphi(3)=\tfrac34$ | $s=1$ optimal: enlarging the cell alphabet strictly hurts |
| $\varphi(4),\varphi(5)$ (complement-exhaustive at 4 + $3{\cdot}10^5$ random) | best seen $6/7$, $7/6$ | same trend |
| tensor/transport inside the class (= product-cell grids) | preserves $\varepsilon\cdot d$ exactly | can transport, never improve — as in refuter-1 §4.3 |

Free-form stochastic sweep (`t4`): hub/sunflower, uniform-random, grid-like, and
nested-chain window layouts, random sparse/dense/balanced patterns, exact repair to
cross-disjointness, LP-optimized weights, hill-climbing on the best configs:
$(d,N)\in\{(2,6),(2,8),(3,6),(3,9),(4,8),(4,12),(5,10),(6,12)\}$, 3,550 attempts, 1,712
valid incompatible configurations. **Global minimum $\varepsilon\cdot d=0.5000$; the exact
minimum payment across every audited cross pair was exactly 1, never below.**

## 5. Target 3 — the obstruction, quantitatively (prover's blueprint)

Why richness can't win, mechanism by mechanism:

1. **Low-influence coordinates are bought with dense projections.** A relevant coordinate
   with $\mathrm{Inf}_i=2^{-\Theta(d)}$ exists only in patterns whose projections are nearly
   full in the relevant directions ((F1): $b_i\ll|P|$). But conflicting through a window $S$
   *taxes the product* $\nu_f(S)\nu_g(S)\le\tfrac14$ ((F2)), and (F3) converts projection
   sparsity into influence: total influence on $S$ at least $\tfrac12\log_2(1/\nu)$. So the
   cheap coordinates are exactly the ones that cannot certify any conflict; every pair still
   costs total influence $\ge1$ on the shared window (F4). Richness relocates the cost; it
   never reduces it.
2. **Concentration beats spreading, by isoperimetric rigidity.** Payment exactly 1 forces
   $\nu_f=\nu_g=\tfrac12$ with Harper equality; boundary-minimal half-density sets are
   dictator halfcubes only (verified exhaustively $n\le4$, `t5` T5a), so **every
   payment-tight cross pair conflicts through a single oppositely-forced shared coordinate
   with uniform fibers** — locally, the grid (verified: all 10,494 payment-tight sampled
   pairs + exhaustive $s\le3$, T5b). Any attempt to spread a pair's payment across
   coordinates (tribes, majority, parity) inflates it: KKL-profile $\Theta(\log s)$ tax at
   density $\tfrac12$, $\tfrac12\log_2(1/\mu)$ tax at low density.
3. **Concentrated payments are then capped by the window budget.** Payments of $\tfrac12$
   per forced coordinate can only be amortized by distributional spreading over many
   windows, and the master count (M) charges each pair through the partner's window size:
   $\delta_F\,\mathbb E|K|+\delta_G\,\mathbb E|J|\ge1$ with $|J|,|K|\le d$. The grid
   saturates every inequality simultaneously; nothing in the class has slack anywhere else
   to exploit. Hub/core layouts fail precisely here: forcing all conflicts through a common
   core makes every partner's window contain every core ($\mathbb E|K|\ge$ #cores·size), and
   the budget bites at exactly $1/(2d)$.

**The candidate inequality, with the violation locus of every attempted construction,** is
(M) in §2: grid = equality; parity/affine cells violate minimality of per-pair payment by a
factor $s$; tribes/majority by $\Theta(\log s)/\Theta(\sqrt s)$ (KKL/boundary spread); sparse
patterns by $\tfrac12\log_2(1/\mu)$; hubs lose in the $\mathbb E|K|$ factor.

## 6. Target 4 — coverage; what the null results do and do not rule out

**Covered.** Exact-exhaustive: all support partitions up to symmetry at
$(2,2),(2,3),(2,4),(3,3),(3,4)$ with full junta LPs, rationally certified. Exact
parametric: all architectures of §4 in the stated ranges. Stochastic: §4's sweep (hub /
random / grid / chain layouts, $d\le6$, $N\le12$, LP + hill-climb). Fact verification:
(F1)–(F4) as itemized in §1; (F3) is exhaustive precisely on all windows of size $\le4$
and sampled to $k=12$.

**Ruled out (modulo the chain (F1)–(M) surviving verification):** any counterexample to R1,
at every $(d,N)$, any support sizes, any inverse-polynomial (indeed any) $\delta<1/(2d)$
— falsity of R1 would contradict the hypercube edge-isoperimetric inequality via five
elementary steps.

**Not ruled out / not established.** (i) Nothing about R2+ or ℤ₂-PCC: (F3)/(F4) are
indicator-specific; the full-class $1/5<1/4$ certificate (refuter-1) proves the engine
*must* generalize nontrivially — for mixtures/signed $f$, "projection density" has no
direct analogue, and spiky sums-of-indicators genuinely pay less than any indicator on the
same support. The generalization target for R2 is a payment lemma for the densities
$u=\mathbb E_{\mathbf F}|f|^2$ (degree $\le2d$, mean 1). (ii) The exhaustive verification
of (F3) stops at window size 4 (+ sampling to 12); its general-$k$ truth rests on the
standard isoperimetric inequality, which the prover must prove inline or via card.
(iii) Exact values at $(d,N)$ not listed (e.g. $(2,5)$ exhaustive, $(4,4)$) were not
computed; monotonicity plus the floor make them non-decisive.

## 7. Implausible-consequence check (§3.4 review update)

Deriving what R1-falsity implies: (a) by I01's descent block, ℤ₂-PCC false — by refuter-1
§6 this yields no cryptographic object, no Minicrypt-in-Pessiland placement, no
subexponential algorithm for any well-studied problem; the Impagliazzo-hierarchy test
alone would **not** flag it. (b) But at this rung falsity implies more: a violation of the
chain of §1–2, whose only non-elementary link is Harper's edge-isoperimetric inequality —
an established theorem. So falsity is not merely implausible; it is impossible modulo a
five-step derivation now verified in exact arithmetic at every computationally reachable
scale. **No IMPLAUSIBLE CONSEQUENCE verdict is needed; the direct obstruction is
strictly stronger.**

## 8. Handoff notes for the prover (I01)

Lemma chain to write up: L1=(F1), L2=(F2), L3=(F3) (prove edge-iso inline by induction —
recommended over a source card), L4=(F4), L5=(M); conclusion: R1 with
$\delta(d)=1/(3d)$, $c_1=1/3$, $c_2=1$, plus tightness via the grid (citable from card S1
Claim B.3 or refuter-1 §3). Generalization hypothesis: satisfied. Warnings: keep the
average-influence hypothesis (the count is linear in the distributions — do not upgrade to
per-function bounds); handle $S_{ab}=\emptyset$ and constant functions explicitly (both
degenerate cases are excluded by nonemptiness of patterns, §1 F2).

## 9. Code manifest (`proofs/0023-refuter-2-code/`)

`junta_lib.py` (class representation, exact influences/disjointness/payments, family LPs,
exact dual/mixture certificates) · `t1_formula_and_lemmaA.py` (F1–F4 stress, 112 s) ·
`t2_exact_small.py` (exact $\varepsilon^*_{\mathrm{junta}}$ table, 20 s) ·
`t3_structured.py` (structured charts, 11 s) · `t4_random_families.py` (stochastic sweep +
hill-climb + exhaustive (3,3), 4 s) · `t5_equality_and_master.py` (rigidity + master-chain
audit, 2 s). Environment: python 3.14, numpy 2.5.2, scipy 1.18.1 (venv; scipy floats used
only for LP search — every load-bearing number re-certified with `fractions.Fraction` or
integer arithmetic). Reuses `../0023-refuter-1-code/pcc_lib.py` (partition orbit reps).

### END OF ARTIFACT 0023-refuter-2 ###
