---
id: 0023-refuter-3
agent: refuter
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE
---

# Refuter report, cycle 3 — rung R2 / intermediate I02 (degree-≤d set indicators, ℤ₂)

**Target:** I02, assumed FALSE. Hunted for cross-disjoint families over
$\mathcal C^{\mathrm{ind}}_d=\{\mathbf 1_A/\lVert\mathbf 1_A\rVert_2:\deg\mathbf 1_A\le d\}$
whose maximal per-coordinate average influence beats every inverse polynomial in $d$.

## VERDICT

**NO COUNTEREXAMPLE IN REGIME**
[$d=2$: **complete**, every $N$, by proof — see §1; $d=3$: exhaustive over the
sub-class of $\le3$-junta degree-3 sets (every $N$), exhaustive over all
complement pairs with window $\le 5$, exhaustive design search at $N\le7$,
$4\cdot10^5$ sampled window-4/5 pairs; $d\le 9$: all structured architectures
(grid, MUX/address tensor grids, address hubs, codim-$d$ subcube/complement,
signed-4-cycle designs), exact]
**+ NEAR-MISS (two obstruction families, both certified, both rigid).**

**THE HEADLINE NUMBER.**
$$\boxed{\varepsilon^*_{\mathrm{ind}}(2)=\tfrac14=\tfrac1{2d}\quad\text{exactly, for every }N.}$$
It is **not** strictly between $1/5$ and $1/4$: widening R1's class from
$\le2$-window cylinder patterns to *all* degree-$\le2$ sets does **not** move
the frontier one bit, even though the class is strictly and interestingly
richer (§2). The $1/5$ full-signed-class record of `0023-refuter-1` is therefore
purchased entirely by non-indicator functions. Rung R2 at $d=2$ is **TRUE with
the optimal constant**, $\delta(2)=\theta/4$ for any $\theta<1$, and the proof
is a finite exhaustive check plus five lines of counting (§1) — a ready-made
prover unit.

**The bad news, stated as sharply as the evidence permits.** The two proof
routes on the table for general $d$ are both **dead**, each killed by an
explicit family, exactly computed:

| route | local inequality | status | killer |
|---|---|---|---|
| payment vs **window budget** (refuter-2's (M)) | $\pi\ge(\lvert J\rvert+\lvert K\rvert)/(2d)$ | true $d=2$; **FALSE $d\ge3$** | address sets: ratio $\to 2^{-\Theta(d)}$ |
| payment vs **influence mass** (I02's flagged route) | $\exists i\in S:\min(\mathrm{Inf}_i f,\mathrm{Inf}_i g)\ge1/\mathrm{poly}(d)$ | **FALSE $d\ge2$** | codim-$d$ subcube vs complement: $\theta=\frac1{2(2^d-1)}$ |

Neither killer is a counterexample: each is *rigid* (§5), and the rigidity is
where the proof of R2 must live. One clean unconditional fragment survives and
is proved here without any computer: **every incompatible pair whose conflicts
are of "forcing" type satisfies $\max(\delta_F,\delta_G)\ge1/(2d)$** (§5.1) —
the correct generalisation of R1's mechanism to arbitrary degree-$d$ sets, with
no $2^{\Theta(d)}$ junta loss. The whole residual difficulty of R2 is the
complementary case, "spread conflicts", and §5 pins it.

Code: `proofs/0023-refuter-3-code/` (imports `../0023-refuter-2-code/junta_lib.py`).
Compute ≈ 9 min wall clock. Every load-bearing number is a `Fraction` or an integer.

## 1. $\varepsilon^*_{\mathrm{ind}}(2)=1/4$: the proof, and its two independent checks

**(a) Class enumeration (exact, `s1`).** Every degree-$\le2$ set is a junta on
at most **4** coordinates, and 4 is attained. Elementary reason (no citation,
no Nisan–Szegedy): $\partial_i\mathbf 1_A$ is a nonzero degree-$\le1$ function
with values in $\{0,\pm\frac12\}$, and a nonzero degree-$\le1$ multilinear
polynomial is nonzero on at least half the cube (refuter-1 Thm R-1(i)), so
$\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E[(\partial_i\mathbf 1_A)^2]\ge\frac18$ for
every relevant $i$; meanwhile
$\sum_i\mathrm{Inf}_i(\mathbf 1_A)=\sum_S|S|\widehat{\mathbf 1_A}(S)^2\le2(\mu-\mu^2)\le\frac12$.
Hence $\#\{\text{relevant}\}\le4$. Exhaustive confirmation: the restriction
recursion gives $|L(k,2)|=4,16,70,222,552,1164$ for $k=1..6$ with
$2,10,32,\mathbf{24},0,0$ patterns depending on all $k$ coordinates. So the
class on $\{\pm1\}^N$ is exactly the cylinders over these $2+10+32+24$ pattern
types — a *complete* search space for every $N$.

**(b) The local payment inequality (LOC-2).** For a disjoint pair with windows
$J,K$ and $S=J\cap K$, set $\pi(f,g)=\sum_{i\in S}[\mathrm{Inf}_i(f)+\mathrm{Inf}_i(g)]$.
$$\textbf{(LOC-2)}\qquad \pi(f,g)\ \ge\ \tfrac14\bigl(|J|+|K|\bigr).$$
**Verified exhaustively, twice, independently:**
* `s2`: all 292 disjoint pairs over $(k_f,k_g,s)$ for $k_f,k_g\le4$, $s\ge1$
  (WLOG: all patterns on both windows are enumerated, so relabelling inside a
  window is absorbed); influences by the (F1) boundary-count formula; exact
  rationals. $\min\bigl(\pi-\frac{|J|+|K|}4\bigr)=\mathbf 0$.
* `s3`: a disjoint code path — sets as **bitmasks over the $2^7=128$ points**
  of $\{\pm1\}^7$ (every overlap of two $\le4$-windows is realised, $4+4-1=7$),
  disjointness = mask AND, influences from the **definition** by integer
  Walsh–Hadamard, no formula (F1), no WLOG, no symmetry reduction. All 2184
  class members, all 24360 ordered disjoint pairs:
  $\min\bigl(\pi-\frac{|J|+|K|}4\bigr)=\mathbf 0$; relevant-coordinate sets
  agree with the windows in all 2184 cases; 0 disjoint pairs with empty shared
  window. Influence spectrum: exactly $\{1/6,1/4,1/2\}$.

**(c) The count.** Let $(\mathbf F,\mathbf G)$ be incompatible,
$u_i=\Pr_{\mathbf F}[i\in J]$, $v_i=\Pr_{\mathbf G}[i\in K]$. Drawing
$f_a\sim\mathbf F$, $g_b\sim\mathbf G$ independently,
$$\mathbb E[\pi]=\sum_i\bigl[\overline I_F(i)v_i+\overline I_G(i)u_i\bigr]\le\delta_F\,\mathbb E|K|+\delta_G\,\mathbb E|J|,$$
while (LOC-2) gives $\mathbb E[\pi]\ge\frac14(\mathbb E|J|+\mathbb E|K|)$. Hence
$\max(\delta_F,\delta_G)\ge1/4$. The $2\times2$ grid attains $1/4$; so does the
MUX pair at $N=3$. **$\varepsilon^*_{\mathrm{ind}}(2)=1/4$.** Equality holds
simultaneously in every link for both extremal objects (checked in `s4`:
$\mathbb E[\pi]=1$, $\mathbb E|J|=\mathbb E|K|=2$ for the grid;
$\mathbb E[\pi]=3/2$, $\mathbb E|J|=\mathbb E|K|=3$ for MUX).

**(d) Search confirmation.** Independent of the proof, the closure-based design
search (`s6`, exact cross-disjointness, LP weights, rational certificates
$\tau_F\le1/4$, $\tau_G\le1/4$) finds minimum $\varepsilon=1/4$ at
$N=4,5,6,7,8,9$ over 188 seeds each (all single-set seeds up to cube symmetry
plus random 2- and 3-set seeds), class sizes 220…6090. Nothing beats $1/4$.

## 2. What the wider class actually contains (all new relative to R1)

Degree-$\le2$ sets that are *not* $\le2$-window patterns, exhaustively (`s1`):
* **32 genuine 3-juntas**, e.g. the MUX/address set
  $A=\{x_1{=}1\wedge x_2{=}1\}\cup\{x_1{=}{-}1\wedge x_3{=}1\}$: three
  influences $1/4$, total influence $3/4$, $\mu=1/2$.
* **24 genuine 4-juntas**, all of the form
  $\mathbf 1_A=\frac12+\frac14(s_1x_1x_2+s_2x_2x_3+s_3x_3x_4+s_4x_4x_1)$ with
  $\prod s_i=-1$ (signed 4-cycles): four influences $1/4$, total influence 1.
  These attain the junta bound $d2^{d-1}=4$ exactly.
* **Complements**: $\deg\mathbf 1_{A^c}=\deg\mathbf 1_A$, so $(A,A^c)$ is always
  an incompatible singleton pair in the class — a mechanism absent from R1.
  Complement of a 2-subcube: two influences $1/6$ (the class minimum).
* **Forcing lemma (exhaustive, `s1`):** a degree-$\le2$ set contained in a
  halfcube is a subcube of codimension $\le2$ (0 exceptions). At $d=3$ this
  *fails*: 292 non-subcube forcing sets with windows up to 4.
* General: **a degree-$\le d$ set forces at most $d$ coordinates**, and a forced
  coordinate has influence **exactly** $1/2$ (`s5`; observed maxima 2 and 3 at
  $d=2,3$). Elementary: $A\subseteq$ codim-$t$ subcube $\Rightarrow\deg\ge t$.

## 3. Target 1 — exact small cases

| $(d,N)$ | class size | $\varepsilon^*_{\mathrm{ind}}$ | $\varepsilon^*_{\mathrm{junta}}$ (refuter-2) | full signed (refuter-1) |
|---|---|---|---|---|
| $(2,3)$ | 68 | $1/4$ | $1/3$ | $1/4$ |
| $(2,4)$ | 220 | $1/4$ | $1/4$ | **$1/5$** |
| $(2,N)$, $N\le9$ | ≤6090 | $1/4$ (proved: all $N$) | $1/4$ | $\le1/5$ |
| $(3,N)$, $N\le7$, windows $\le3$ | ≤7854 | $1/4$ | $1/4$ | ≈0.1867 at $N=4$ |

Two consequences. (i) **The indicator restriction is exactly what stops $1/5$**:
$\mathcal C^{\mathrm{ind}}_2$ contains the whole of $\mathcal C^{\mathrm{junta}}_2$
plus 56 new pattern types, and still cannot reach below $1/4$; the sub-$1/(2d)$
signed records are essentially non-Boolean, as refuter-1 (O3) suspected.
(ii) Within the sub-class of degree-3 sets that are $\le3$-juntas, (LOC-3)
*holds* exhaustively (6202 pairs, min slack 0), so the same count gives
$\varepsilon^*=1/6$ there, for every $N$ — a free partial for $d=3$.

## 4. Target 2 — the non-junta objects, and where they break the routes

**(LOC-3) is FALSE.** Exhaustive over all complement pairs with window $\le5$:
$\min(\pi-k/d)=-1/24$ at $k=5$ ($\pi=13/8$ vs $5/3$). Sampled window-4/5 pairs:
$\min\pi/(|J|+|K|)=1/8<1/6$, realised by a forcing pair whose windows carry
three influence-free-riders each. So at $d=3$ the payment/window count already
cannot reach the optimal $1/(2d)$.

**The address family kills the route asymptotically** (`s2`, `s7`; two
independent computations — integer Walsh–Hadamard on the full $2^{11}$ cube, and
the closed form $\mathbf 1_A=\frac12+\frac12\sum_j\mathbf 1[a{=}j]y_j$, which
agree exactly). $A_k=\{x:y_{\mathrm{addr}(a)}=+1\}$ has degree $k+1$,
$k+2^k$ relevant coordinates, influences $1/4$ ($k$ address bits) and
$2^{-k-1}$ ($2^k$ targets), $\mu=1/2$, $T=k/4+1/2$:

| $k$ | $d$ | $\lvert J\rvert$ | $\pi(A_k,A_k^c)$ | $(\lvert J\rvert{+}\lvert K\rvert)/2d$ | $\pi/(\lvert J\rvert{+}\lvert K\rvert)$ |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 3/2 | 3/2 | 1/4 (tight) |
| 2 | 3 | 6 | 2 | 2 | 1/6 (tight) |
| 3 | 4 | 11 | 5/2 | **11/4** | 1/8.8 |
| 5 | 6 | 37 | 7/2 | 37/6 | 1/21.1 |
| 8 | 9 | 264 | 5 | 88/3 | 1/105.6 |

$\pi/(|J|+|K|)=\frac{k/2+1}{2(k+2^k)}=2^{-\Theta(d)}$. **Any argument that
charges a conflict against the partner's window size — refuter-2's (M), the
minimal-conflict-dimension variant, or the R1 proof with $M(d)$ substituted —
is capped at $2^{-\Theta(d)}$, i.e. at K1's already-known threshold.** This is a
barrier statement about the technique, verified exactly, not a counterexample.

**The cheap-coordinate family kills the influence-mass route** (`s7`).
$C=$ codim-$d$ subcube: $(C,C^c)$ is incompatible in the class with
$\mathrm{Inf}_i(f_C)=1/2$ and $\mathrm{Inf}_i(f_{C^c})=\frac1{2(2^d-1)}$
($d=2..8$: $1/6,1/14,1/30,1/62,1/126,1/254,1/510$). Hence
$$\theta^*(d):=\min_{\text{disjoint pairs}}\ \max_{i\in S}\min\bigl(\mathrm{Inf}_i f,\mathrm{Inf}_i g\bigr)\ \le\ \frac1{2(2^d-1)},$$
and exhaustively $\theta^*(2)=1/6$, $\theta^*(3)\le1/14$ (both attained by this
family). Consequence in §5.2.

## 5. Target 3 — the obstruction, quantitatively (the prover's blueprint)

### 5.1 What the total-influence budget *does* buy (unconditional, no computer)

The route I02 flags works, in full, for **forcing conflicts**. Facts: a
degree-$\le d$ set forces $\le d$ coordinates; a forced coordinate has influence
exactly $1/2$ (§2). Fix $f\in\mathrm{supp}\,\mathbf F$ and split
$\mathrm{supp}\,\mathbf G$ into $G_1$ (pairs conflicting through a coordinate of
$\mathrm{Forced}(f)$ forced oppositely by $g$) and $G_2$. Then
$\sum_{i\in\mathrm{Forced}(f)}\Pr_{\mathbf G}[g\text{ opposes at }i]\ge\Pr[G_1]$,
so some $i$ has $\Pr\ge\Pr[G_1]/d$ and
$$\overline I_G(i)\ \ge\ \frac{\Pr[G_1]}{2d}.$$
Distributional form: $\Pr[\text{forcing conflict}]\le\sum_i(2\overline I_F(i))(2\overline I_G(i))\le4\delta_G\sum_i\overline I_F(i)\le4d\,\delta_G$,
using only $\sum_i\mathrm{Inf}_i(f)\le d$. **So: forcing-only incompatible
families never beat $1/(2d)$, and any family with $\Pr[\text{forcing}]\ge\frac12$
has $\max\delta\ge1/(8d)$.** No window sizes, no junta size: the exponential
trap is absent. This is the correct lift of R1's mechanism and should be
Lemma 1 of the R2 attempt.

### 5.2 Exactly where the candidate inequality of that shape fails

The natural completion is
**(HEAVY$_\theta$)** *every disjoint pair has $i\in S$ with
$\min(\mathrm{Inf}_i f,\mathrm{Inf}_i g)\ge\theta(d)$*, which by
Markov + union bound + the budget gives
$1\le\sum_i\frac{\overline I_F(i)}{\theta}\frac{\overline I_G(i)}{\theta}\le\frac{d\,\delta_G}{\theta^2}$,
i.e. $\max\delta\ge\theta(d)^2/d$ — inverse-polynomial **iff**
$\theta(d)\ge1/\mathrm{poly}(d)$. **It is not:** §4 gives
$\theta^*(d)\le\frac1{2(2^d-1)}$, exactly, from the simplest object in sight.
So (HEAVY) fails at $2^{-\Theta(d)}$ and this count yields only
$\max\delta\ge 2^{-\Theta(d)}/d$ — again no better than K1. The failure is
**not** repairable by asymmetric variants: charging $f$'s influence against
$g$'s mere *relevance* re-introduces either $\mathbb E|K|$ (window budget,
capped by §4) or $\max_iu_i$ (relevance spread), and converting relevance to
influence costs the class's minimum nonzero influence, which is $2^{-\Theta(d)}$
(e.g. $1/(2(2^d-1))$, or $2^{-k-1}$ for address targets). This is the precise
place, and the precise factor, at which every inequality of that shape breaks.

### 5.3 Why the two killers are not counterexamples (the rigidity, certified)

* **Cheap-coordinate rigidity.** The cheap side $C^c$ has exactly **one**
  possible partner: the only degree-$\le d$ subset of a codim-$d$ subcube $C$ is
  $C$ itself (exhaustively verified for $(d,N)=(2,4),(2,5),(3,5)$; elementary
  reason: $A\subseteq C\Rightarrow\mathbf 1_A=\mathbf 1_C h$, so $\deg\ge d$ with
  equality only for $h$ constant). That partner pays $1/2$. Cheapness of one
  side is bought by pinning the other.
* **Address (hub) rigidity.** For two address sets to be disjoint they must
  share the whole address block: `s4` tested every layout of the $G$-side
  address block and target pool inside a 12-coordinate pool — disjoint with the
  **same** address block: 1/12 ($k{=}1$), 2/720 ($k{=}2$); with a **different**
  address block: **0/48 and 0/19440**. Since every cross pair must conflict, the
  address block is a hub common to the whole support, so its influence $1/4$
  cannot be diluted: every address-based design sits at $\delta=1/4$, verified
  ($\varepsilon\cdot2d=1.0$ for address- and MUX-tensor grids at $D=1,2$; the
  tensor/transport rule preserves $\varepsilon\cdot d$ exactly, as in
  refuter-1 §4.3).
* **Consistency with the literature-level barrier**: for *singleton* pairs the
  class is protected by the Boolean case of Aaronson–Ambainis
  ($\max_i\mathrm{Inf}_i\ge\mathrm{Var}/\mathrm{poly}(d)$ via OSSS +
  degree-vs-decision-tree-depth; [MEMORY]-grade, not used in any claim above),
  since $\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\mu$ and
  $\mu_f+\mu_g\le1$ for a disjoint pair. **The whole of R2's difficulty is
  dilution across a distribution, not the individual functions.**

**Blueprint.** L1 forcing lemma (§2); L2 forcing count $\Rightarrow1/(2d)$
(§5.1); L3 the spread case: show that a conflict with no oppositely-forced
shared coordinate forces the two sides to share a *bounded* structure. The two
rigidity facts above are the empirical content of L3; both known
cheap-coordinate mechanisms are covered by them, and no third mechanism appeared
in this search.

## 6. Target 4 — coverage, and what the null results do and do not rule out

**Covered.** (a) $d=2$: the class is *completely* enumerated (junta bound 4,
proved and exhaustively confirmed to $k=6$), (LOC-2) verified on all disjoint
pairs by two independent implementations, so $\varepsilon^*_{\mathrm{ind}}(2)=1/4$
holds for **every** $N$, every support size, every distribution — a proof, not a
search. (b) $d=3$: exhaustive for all pairs with windows $\le3$ (6202 pairs,
(LOC-3) holds ⇒ $1/6$ on that sub-class for all $N$); exhaustive over all
$746{,}048{+}$ complement pairs with window $\le5$; exhaustive design search at
$N\le7$ with windows $\le3$ (260 seeds each); $4\cdot10^5$ sampled window-4/5
pairs. (c) $d\le9$: the structured architectures listed in the verdict, exact.
(d) Structural facts of §2 exhaustive in the stated ranges.

**Ruled out.** Any counterexample at $d=2$ (unconditionally). Any counterexample
at $d=3$ built only from $\le3$-junta degree-3 sets. Any counterexample from
tensor/transport of a small seed (preserves $\varepsilon\cdot d$). Any
counterexample from address-hub or subcube/complement architectures at any $d$.
Both published-style proof routes as *sole* mechanisms for general $d$ (§4) —
this is a barrier, and it means an R2 artifact built on window budgets is
capped at $2^{-\Theta(d)}$ and must declare itself PARTIAL per I02.

**NOT ruled out.** (i) $\varepsilon^*_{\mathrm{ind}}(3)<1/6$ using windows
$4$–$6$: (LOC-3) *is* false there, my window-4/5 coverage is thin (365 disjoint
pairs out of $4\cdot10^5$ draws — the class at window 5 has 746k patterns and at
window 6 is not enumerable by this recursion), and degree-3 junta size $\ge5$
(the true value, 6, was not reached). **This is the single most valuable next
computation.** (ii) Anything at $d\ge4$ beyond the structured families: the
class at $d=4$ admits juntas on up to 32 coordinates and was never enumerated.
(iii) A fourth cheap-coordinate mechanism, unlike dense-complement and address:
nothing in this search excludes one, and the barrier of §4–5.2 says a
counterexample, if it exists, must look like one (many relevant coordinates of
influence $2^{-\Theta(d)}$ carrying the conflicts, with the expensive core
spread over the support). (iv) Nothing about R3 or ℤ₂-PCC.

## 7. Implausible-consequence check (§3.4 review update)

R2-falsity implies ℤ₂-PCC-falsity, which (refuter-1 §6, refuter-2 §7)
constructs no cryptographic object, places nothing in Pessiland, and yields no
subexponential algorithm: the Impagliazzo-hierarchy test does not flag it. At
this rung, though, a sharper test applies and *does* fire: R2-falsity at $d=2$
would contradict a finite exact computation (§1), and R2-falsity at any $d$
would require a balanced-ish degree-$d$ Boolean function family whose influence
is diluted across a distribution by more than $\mathrm{poly}(d)$ while every
cross pair still conflicts — which, for singleton supports, is refuted by the
Boolean case of Aaronson–Ambainis (a theorem). So falsity is confined to a
strictly distributional phenomenon with no known mechanism. **No IMPLAUSIBLE
CONSEQUENCE verdict is needed; §1 (for $d=2$) and §5.3 (in general) are
stronger.**

## 8. Code manifest (`proofs/0023-refuter-3-code/`)

`deg_lib.py` (class enumeration by the restriction recursion; degree test by
integer Walsh–Hadamard; reuses `JFun`, (F1)–(F4) from
`../0023-refuter-2-code/junta_lib.py`) · `s1_class_structure.py` (junta size,
influence spectrum, forcing lemma, complement and general singleton frontiers;
`s1.out`) · `s2_payment_inequality.py` ((LOC-2) exhaustive, (LOC-3) refuted,
address family two ways; `s2.out`) · `s3_independent_and_exhaustive.py`
(independent (LOC-2) on point masks at $N=7$; sandwich for
$\varepsilon^*_{\mathrm{ind}}(d,N)$; `s3.out`) · `s4_hunt_d3_and_hub.py`
($d=3$ ratio hunt, hub-disjointness test, structured designs with exact
cross-disjointness + LP + diagnostics; `s4.out`) · `s5_heavy_lemma.py`
($\theta^*(d)$ sweeps, forcing facts, address stress test; `s5.out`) ·
`s6_design_search.py` (closure-based design search with rational certificates;
`s6.out`) · `s7_obstruction_certificates.py` (the two obstruction families and
their rigidity; `s7.out`). Environment: python 3.14 venv, numpy 2.5.2,
scipy 1.18.1; scipy LPs used only for search, every reported optimum
re-certified with `fractions.Fraction` or integers.

### END OF ARTIFACT 0023-refuter-3 ###
