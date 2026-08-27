---
id: 0023-strategist-2
agent: strategist
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE
---

# Strategist plan set — rung R2 / intermediate I02 (degree-≤d set indicators, ℤ₂)

Target: `intermediates/I02-degree-d-sets.md` **only** — not ℤ₂-PCC, not the
Contract. Inputs read in full: I02; `0023-refuter-3` (the frontier
ε\*_ind(2)=1/4, its §5 blueprint, its two killed routes with certificates);
`0023-refuter-2` (frozen rung's mechanism); `0023-scout-4`, `0023-scout-5`;
cards S1, S5(via ledger), S6a–S6d, S7 + S7b; CONTRACT.md (BARRIER CHECKLIST);
PROGRESS.md (ladder R1–R6); LEDGER (frozen I01, dead plans);
`0023-strategist-1` (cycle-1 plans, for non-duplication).

No proof is attempted. Claims tagged **[STRAT-CLAIM]** are strategist-level
observations with the argument sketched in ≤5 lines; the assigned prover must
verify each before load-bearing use. I01 is cited **only as its frozen
statement**; no plan below requires re-deriving or re-verifying it (§6.3).

---

## 0. RULING — the S7b window vs refuter-3's killer (a). THE RECONCILIATION.

**Verdict: killer (a) does NOT apply to the S7b shattering window. It applies
only to the junta / relevant-coordinate window. The two agents were talking
about two different objects, and the difference is exactly the difference
between 2^Θ(d) and d.** The lead plan (P1) is built on this.

### 0.1 What killer (a) actually says

`0023-refuter-3` §4 certifies, in exact arithmetic, that for the address family
$A_k$ ($d=k+1$, $\lvert J\rvert=k+2^k$ relevant coordinates, influences $1/4$ on
the $k$ address bits and $2^{-k-1}$ on the $2^k$ targets):

$$\frac{\pi(A_k,A_k^c)}{\lvert J\rvert+\lvert K\rvert}=\frac{k/2+1}{2(k+2^k)}=2^{-\Theta(d)} .$$

The numerator $\pi$ is a **payment** (a sum of influences over a shared
coordinate set). The denominator is **the number of relevant coordinates**.
So what is certified dead is: *any argument whose per-pair local inequality is
$\pi\ \ge\ c\,(\lvert J\rvert+\lvert K\rvert)/d$ with $J,K$ the
relevant-coordinate sets.* The kill is caused **entirely by the denominator
blowing up to $2^{\Theta(d)}$**, i.e. by the junta size — the very quantity
I02's trap names, and the very quantity cards S6c/S6d prove is $\Theta(2^d)$
and unimprovable.

### 0.2 Why the S7b window is a different object, and immune

Card S7b (Chang–Fang Cor. 3.4, READ and independently verified by
`0023-scout-5`) gives, for every finite abelian $\mathcal Y$, every $N$, every
nonzero $\deg\le d$ function, a window $W$ with $\lvert W\rvert\le d$ such that
$\mathrm{supp}$ projects **onto** $\mathcal Y^{[N]\setminus W}$. Concretely
over ℤ₂: $W$ may be taken to be **any maximum-degree monomial support** of
$\mathbf 1_A$, so $\lvert W\rvert\le d$ *by theorem*, uniformly in $N$ — while
$A$ may depend on $\approx 2^d$ coordinates (card S7, "what it does NOT say",
last bullet).

Therefore a payment inequality charged against the **S7b window size** never
has a $2^{\Theta(d)}$ denominator: the master count of `0023-refuter-2` §2 runs
verbatim with $J,K$ replaced by S7b windows and returns
$\delta_F\,\mathbb E\lvert W_g\rvert+\delta_G\,\mathbb E\lvert W_f\rvert\ge\pi$
with $\lvert W\rvert\le d$, i.e. $\max\delta\ \ge\ \pi/(2d)$. **No exponential
appears anywhere.**

### 0.3 The killer's own certificate, evaluated on the S7b window (the decisive check)

I evaluated refuter-3's two certified killer families on S7b windows. Both pay
$\ge 1/2$; one pays exactly $1$. **[STRAT-CLAIM]**, arithmetic re-derivable in
five lines each from refuter-3's own printed influence tables:

| family (refuter-3's killer) | S7b windows | payment $\pi$ on the S7b windows |
|---|---|---|
| address pair $(A_k,A_k^c)$, $d=k+1$ (kills the window-budget route) | $W_A=\{a_1..a_k,y_j\}$, $W_B=\{a_1..a_k,y_{j'}\}$, each of size $d$ | $\ge k\cdot\tfrac14\cdot 2 = k/2$ (address block is in **both** windows: $\mathbf 1_{A_k}=\tfrac12+\tfrac12\sum_j\mathbf 1[a{=}j]y_j$, so every maximum-degree monomial is $a_1\cdots a_k y_j$) |
| codim-$d$ subcube pair $(C,C^c)$ (kills HEAVY$_\theta$) | $W_A=W_B=\{1,\dots,d\}$ (unique top monomial, and $\mathbf 1_{C^c}=1-\mathbf 1_C$) | $d\bigl(\tfrac12+\tfrac1{2(2^d-1)}\bigr)\ \ge\ d/2$ |
| $d\times d$ grid (the R1 extremal) | $W_A=$ row $r$, $W_B=$ column $c$ | exactly $1$ ($\tfrac12+\tfrac12$ at the crossing cell) |
| MUX/3-junta and signed-4-cycle pairs at $d=2$ (refuter-3 §2's new objects) | any top-monomial pair | exactly $1$ |

The address family's ratio collapses to $2^{-\Theta(d)}$ **only** because
$2^k$ cheap target coordinates are counted in $\lvert J\rvert$. On the S7b
window only **one** target coordinate appears, and the $k$ expensive address
bits are *forced into both windows* — which is refuter-3 §5.3's own certified
"hub rigidity", now doing work *for* the proof instead of against it.

### 0.4 Killer (b) is also inapplicable to this route, for a second, independent reason

Killer (b) refutes **HEAVY$_\theta$**: $\exists i\in S$ with
$\min(\mathrm{Inf}_i f,\mathrm{Inf}_i g)\ge 1/\mathrm{poly}(d)$. The S7b count
needs no such thing: its payment is a **sum of the two sides separately**,
$\sum_{i\in W_B}\mathrm{Inf}_i(f_A)+\sum_{i\in W_A}\mathrm{Inf}_i(f_B)$, never a
$\min$. On killer (b)'s own witness $(C,C^c)$ this sum is $\ge d/2$ while the
$\min$ is $1/(2(2^d-1))$. **The $\min$-vs-sum distinction is where refuter-3's
§5.2 "not repairable by asymmetric variants" argument stops being binding:**
that paragraph rules out converting the partner's *relevance* into influence
(cost = the class's minimum nonzero influence, $2^{-\Theta(d)}$) — but the S7b
route never converts relevance to influence. It charges the partner's
**degree-window membership**, which costs nothing because $\lvert W\rvert\le d$
is a theorem.

### 0.5 The genuine gap, stated exactly (both halves, as the task demands)

Nothing above proves R2. Two gaps remain and they are the content of P1/P2:

* **(G1) — SOLVED, positively, and it is new.** Is the payment positive at
  all? **Yes, unconditionally, in two lines.** [STRAT-CLAIM] If
  $W_A\cap\mathrm{relevant}(B)=\emptyset$ then $B$ depends only on coordinates
  outside $W_A$; take $b\in B$, and use S7b surjectivity of $A$ off $W_A$ to
  find $a\in A$ agreeing with $b$ on $[N]\setminus W_A$; then $a\in B$, so
  $A\cap B\ne\emptyset$ — contradiction. Hence **every cross-disjoint pair has
  $W_A\cap\mathrm{relevant}(B)\ne\emptyset$ and $W_B\cap\mathrm{relevant}(A)
  \ne\emptyset$**, so $\pi>0$ always. This is strictly stronger than R1's (F2)
  (which needed cylinders) and is the S7b analogue of it. With card S6a's
  quantum $\mathrm{Inf}_i\ge2^{-1-d}$ it already yields, unconditionally,
  $\max\delta\ge2^{-1-d}/(2d)$ — the same order as K1, for free, by a
  completely different argument. **The entire fight is the constant.**
* **(G2) — OPEN, and it is the rung.** $f$'s influence is *not* confined to
  $W_A$: a conflict located inside $W_A\cup W_B$ does not automatically charge
  against $f$'s influence budget, and restricting $f$ to a fibre changes
  influences while the hypothesis constrains the unrestricted $f$. The exact
  bridge is the identity **[STRAT-CLAIM, one line]**
  $$\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E_{w}\bigl[\mathrm{Inf}^{(w)}_i(\mathbf 1_{A_w})\bigr]\qquad (i\in W),$$
  ($w$ = uniform pattern off $W$, $A_w$ = the fibre trace, influence computed
  inside $\{\pm1\}^W$; proof: count $i$-edges fibre by fibre) — exact, no loss.
  But the **normalisations differ**: R1-style fibre payments are stated for
  $\mathbf 1_{A_w}/\lVert\cdot\rVert$, i.e. divided by $\alpha_w$, whereas the
  hypothesis divides by $\alpha=\mathbb E_w\alpha_w$. Assembling the fibre
  payments therefore produces the weight $\mathbb
  E_w[\min(\alpha_w/\alpha,\beta_w/\beta)]$, and *that* quantity — not any
  window size, not any $\min_i$ influence — is the one place a
  $2^{-\Theta(d)}$ could still leak in. I name it **FIBRE-BALANCE** and hand it
  to P2. It is a **third** obstruction, unrelated to either certified killer.

### 0.6 Ruling recorded for the ledger

> **The S7b route is LIVE.** refuter-3's killer (a) is a statement about
> relevant-coordinate (junta) windows and does not bind arguments charging the
> $\le d$-sized shattering window; both of refuter-3's certified killer families
> pay $\Omega(d)$ on their S7b windows, and the grid and all $d=2$ extremals pay
> exactly $1$, which is precisely the constant needed to reproduce the two
> *proved* frontier values $\varepsilon^*(1)=1/2$ and
> $\varepsilon^*_{\mathrm{ind}}(2)=1/4$. Record S7b as the rung's lead
> mechanism, not as a dead route.

---

## 1. BARRIER PRE-CHECK (HARNESS §4 / Contract BARRIER CHECKLIST), applied per plan

**Classical barriers — all NOT APPLICABLE, as the Contract's checklist states.**
R2 is an unconditional finite Fourier-analytic statement about
$\{\pm1\}^N$; no plan below asserts a complexity-class separation, constructs a
natural property, uses an oracle-relativizable or algebrizing framework, or
touches the black-box/meta-reduction layer (which lives only in [CLM23]'s
downstream separations). No plan's success would breach a known barrier.
**Pre-check passes for all six; recorded, not assumed.**

**Internal gates, which are the ones that actually bite here.** A plan dead by
any of these is dead before a prover runs:

* **(IG1) Grid ceiling** (card S1 Claim B.3 / I02's "Grid ceiling"). Any plan
  whose success would certify compatibility at $\delta(d)\ge1/(2d)$ over ℤ₂ is
  dead on arrival. Checked per plan below; P1's best possible output is exactly
  $c/(2d)$ with $c\le1$, so it must be stated with $\theta<1$ as R1 was.
* **(IG2) Killer (a) = window-budget cap** (refuter-3 §4). Any plan whose local
  inequality charges the partner's **relevant-coordinate** window is capped at
  $2^{-\Theta(d)}$. P1 and P5 are checked clear in §0.3 and §3.5 respectively
  (both use $\mathrm{poly}(d)$-sized windows that are *not* the junta set); P2
  and P4 charge no window at all.
* **(IG3) Killer (b) = HEAVY$_\theta$ cap** (refuter-3 §4–5.2). Any plan
  requiring a shared coordinate with $\min(\mathrm{Inf}_if,\mathrm{Inf}_ig)\ge
  1/\mathrm{poly}(d)$ is capped at $2^{-\Theta(d)}$. Every plan below is
  formulated with **sum** payments; no plan takes a $\min$ over the two sides.
  This is checked explicitly per plan and is a hard drafting constraint on any
  prover: *if your key inequality contains $\min(\mathrm{Inf}_if,
  \mathrm{Inf}_ig)$, you have re-derived a killed route.*
* **(IG4) Junta-substitution trap** (I02, cards S6c+S6d). Any plan whose
  threshold degrades exponentially in $d$ is a PARTIAL and must say so in its
  own text. Each plan below carries a TRAP line doing exactly that.
* **(IG5) R3-liftability** (I02's generalization hypothesis, binding on
  technique choice). Flagged per plan; not disqualifying at R2, but a plan that
  dies at R3 is a recorded detour and is ranked down.

---

## 2. Shared vocabulary (all plans may use; each item ≤ half a page to verify)

Fix $A,B\subseteq\{\pm1\}^N$ nonempty with $\deg\mathbf 1_A,\deg\mathbf 1_B\le
d$ and $A\cap B=\emptyset$; $\alpha=\lvert A\rvert/2^N$,
$\beta=\lvert B\rvert/2^N$ (so $\alpha+\beta\le1$);
$f_A=\mathbf 1_A/\sqrt\alpha$.

**V1 — Three different windows, never to be conflated again.** This distinction
is the single most important product of this artifact.

| name | definition | size | source |
|---|---|---|---|
| **junta window** $J(A)$ | the relevant-coordinate set | $\le 4.394\cdot2^d$, and $\ge3\cdot2^{d-1}-2$ in the worst case | cards S6c, S6d |
| **shattering window** $W(A)$ | any maximum-degree monomial support; $A$ surjects onto $\{\pm1\}^{[N]\setminus W}$ | $\le d$ | card S7b (T3.4/T1.2) |
| **certificate window** $T(x)$, $x\in A$ | a coordinate set fixing membership: subcube through $x$ inside $A$ | $\le C(\mathbf 1_A)\le O(d^4)$ | S6c Thm 1.2 + inline $C\le \mathrm{bs}\cdot s$ (§3.5) |

$W$ and $T$ are $\mathrm{poly}(d)$; $J$ is not. Killer (a) constrains arguments
denominated in $J$. **Every plan below must declare which window it uses.**

**V2 — The master count, corrected, with pair-independent windows.**
[STRAT-CLAIM, three lines] Let $\mathbf F,\mathbf G$ be incompatible. Choose any
map $f\mapsto W(f)$ and $g\mapsto W(g)$ (**each depending only on its own
function**). Draw $f\sim\mathbf F$, $g\sim\mathbf G$ independently and put
$$\pi(f,g):=\sum_{i\in W(g)}\mathrm{Inf}_i(f)+\sum_{i\in W(f)}\mathrm{Inf}_i(g).$$
Then $\mathbb E[\pi]\le\delta_F\,\mathbb E\lvert W(g)\rvert+\delta_G\,\mathbb
E\lvert W(f)\rvert\le(\delta_F+\delta_G)\,d$, because independence factorises
$\mathbb E_{f,g}[\mathbf 1\{i\in W(g)\}\mathrm{Inf}_i(f)]=\Pr[i\in
W(g)]\cdot\overline I_F(i)$. Hence a per-pair bound $\pi\ge p$ gives
$$\max(\delta_F,\delta_G)\ \ge\ p/(2d).$$
Two drafting warnings, both fatal if ignored: (i) the payment must sit on the
**partner's** window (charging a side's influence on its own window loses the
$\delta$ factor and yields only the vacuous $\pi\le2d$); (ii) $W(\cdot)$ must
not depend on the partner — this is card S7's obstacle (ii) (non-canonicity)
in its **only** load-bearing form, and it is why the target inequality below is
quantified over *all* admissible window choices.

**V3 — The target inequality.**
$$\textbf{(PAY}\star\textbf{)}\qquad \sum_{i\in W_B}\mathrm{Inf}_i(f_A)\ +\ \sum_{i\in W_A}\mathrm{Inf}_i(f_B)\ \ge\ p(d)$$
for **every** cross-disjoint degree-$\le d$ pair and **every** choice of
maximum-degree supports $W_A,W_B$. By V2, (PAY$\star$) $\Rightarrow$ R2 with
$\delta(d)=\theta\,p(d)/(2d)$, $\theta<1$. Inverse-polynomial iff
$p(d)\ge1/\mathrm{poly}(d)$; $p=1$ would give exactly $1/(2d)$.

**V4 — Calibration: (PAY$\star$) with $p=1$ reproduces every proved value.**
$d=1$: $\pi=1$, count gives $1/2=\varepsilon^*(1,N)$ (refuter-1 Thm R-1,
exact, every $N$). $d=2$: $\pi=1$ on the grid, the MUX/3-junta, the signed
4-cycle and subcube-complement pairs (§0.3), count gives
$1/4=\varepsilon^*_{\mathrm{ind}}(2)$ (refuter-3 §1, proved, every $N$). No
other route on the table predicts both constants. This is the strongest
available evidence that $p=1$ and that $\varepsilon^*_{\mathrm{ind}}(d)=1/(2d)$
exactly.

**V5 — Fibre decomposition and FIBRE-BALANCE.** With $W\supseteq W_A\cup W_B$,
$w$ ranging over $\{\pm1\}^{[N]\setminus W}$, $A_w,B_w\subseteq\{\pm1\}^W$ the
traces, $\alpha_w=\lvert A_w\rvert/2^{\lvert W\rvert}$: both traces are
**nonempty for every $w$** (S7b surjectivity off $W_A$ and off $W_B$,
monotone under shrinking the projected set) and **disjoint**. So each $w$
restricts the pair to an incompatible pair on a cube of $\le2d$ coordinates —
R1-shaped structure with a $\mathrm{poly}(d)$ window. Assembling fibre payments
against the global normalisation produces the weight
$$\textbf{(FIBRE-BALANCE)}\qquad \mathbb E_w\bigl[\min(\alpha_w/\alpha,\ \beta_w/\beta)\bigr]\ \ge\ 1/\mathrm{poly}(d)\ ?$$
[STRAT-CLAIM] The adversary's optimum of the assembled bound is exactly this
quantity, and a two-parameter calculation shows it can only be small if one
side's mass is concentrated on a fibre-set where the other side is
minimally-thin; the floor $\alpha_w\ge2^{-\lvert W\rvert}$ caps the damage at
$2^{-\Theta(d)}$. Both certified killers give $\approx1$ here (§3.2). Unknown in
general; this is P2's key step.

**V6 — S7b usage declaration (mandatory per plan, per card S7b's scout remark).**
S7b has two consequences: the **density** $\lvert A\rvert\ge2^{N-d}$ (capped at
K1's scale, worthless) and the **$\le d$-sized window** (the only
$\mathrm{poly}(d)$ content). Every plan below states which it uses; **no plan
uses the density**, except P3 which uses it only as a search constraint.

---

## 3. THE SIX PLANS

### P1 — class (a) REDUCTION: reduce R2 to one pair-level inequality on S7b windows

**Thesis.** R2 follows from the single per-pair inequality (PAY$\star$) via the
frozen rung's own master count with the junta window replaced by the
$\le d$-sized shattering window of card S7b — a replacement that is legitimate
because refuter-3's killer (a) is a statement about junta windows only (§0).

**Key step everything turns on.** (PAY$\star$) at $p(d)\ge1/\mathrm{poly}(d)$:
for every cross-disjoint degree-$\le d$ pair and every pair of maximum-degree
monomial supports, $\sum_{i\in W_B}\mathrm{Inf}_i(f_A)+\sum_{i\in
W_A}\mathrm{Inf}_i(f_B)\ge p(d)$. Positivity is already a theorem (§0.5 G1);
the fight is the constant. The mechanism that must supply it is *not* R1's
projection-disjointness — for general degree-$\le d$ sets $\pi_S(A)$ and
$\pi_S(B)$ typically both fill $\{\pm1\}^S$, so R1's (F2)/(F4) chain has no
direct analogue and **must not be assumed to lift** — but the fibre structure
of V5: every fibre off $W_A\cup W_B$ carries a genuine incompatible pair on
$\le2d$ coordinates.

**FALSIFIABLE MILESTONE (< 2 pages, decisive fork).**
*(M1a, ≤1 p, provable now.)* Write out V2 + V3 + §0.5(G1): the reduction
"(PAY$\star$) with $p$ ⟹ R2 with $\delta=\theta p/(2d)$", plus the
unconditional corollary $\max\delta\ge2^{-1-d}/(2d)$ from the S6a quantum. This
is a complete, self-contained unconditional theorem of the campaign either way.
*(M1b, ≤1 p, the fork.)* Decide (PAY$\star$) at $p=1$ on the class's known
extremals and by exhaustive machine check where the class is enumerable:
$d\le2$ (complete class, refuter-3 `deg_lib` enumeration), all
$\le3$-junta degree-3 pairs, all complement pairs with window $\le5$, and by
hand on the address and codim-$d$-subcube families at every $d$ (§0.3).
**Refuted** by any single pair with $\pi<1$ — then re-run at
$p=1/\mathrm{poly}(d)$ and report the observed $\min\pi$ as a function of $d$;
**refuted as a route** only if $\min\pi$ decays exponentially.
Note the milestone is *cheap*: refuter-3's code already enumerates the class,
computes exact influences by integer Walsh–Hadamard, and can extract
maximum-degree monomial supports directly from the transform.

**TRAP (I02).** If the observed $p(d)$ decays exponentially, any artifact built
on it is a **PARTIAL, not a proof of R2**, and must declare the threshold. The
route's *design* is trap-free: no junta size, no per-used-coordinate payment,
and the count's only $d$-dependence is $\lvert W\rvert\le d$.

**S7b usage.** **WINDOW only** — the $\le d$-sized shattering window and its
surjectivity. The density consequence is never used.

**I01.** Cited only as the frozen statement (for the tightness discussion and
as the $d=2$/junta-subclass sanity anchor). The proof does **not** re-derive
I01; where it needs a fibre-level payment it must prove its own (R1's internal
(F3)/(F4) are stated for cylinders and their extension to arbitrary sets is
**not** part of the frozen statement — a prover may re-prove what it needs,
labelled as new).

**Prior probability of proving R2: 22%.** Reasoning: the route is the only one
on the table that (i) has a $\mathrm{poly}(d)$ window as a *theorem*, (ii)
survives both certified killers with an explicit margin, (iii) reproduces both
proved frontier constants ($1/2$ at $d=1$, $1/4$ at $d=2$) with the same
constant $p=1$, and (iv) needs no unread source. Against it: (PAY$\star$) is a
strong uniform claim over a class with no classification, the fibre-assembly
leak of V5 is real, and $\pi$ can in principle be as small as $2^{-1-d}$ on
influence-floor grounds, so a proof must extract the constant from disjointness
itself. R3-liftability: **good** — S7b is printed for ℂ-valued functions on any
product of finite abelian groups (card S7b T3.2/T3.4), so the window survives
to R3 and to the top rung verbatim.

**Yield if it fails.** (a) The unconditional theorem of M1a — a second,
independent proof of a K1-order threshold by a route with no exponential in its
design, plus the new structural lemma "$W_A$ meets $\mathrm{relevant}(B)$ for
every cross-disjoint pair" (strictly stronger than R1's (F2), and the first
two-family statement ever derived from Chang–Fang). (b) An exact table of
$\min\pi(d)$ — the quantitative locus where degree-window payment breaks, i.e.
the third certified obstruction of the campaign, and the direct input to P6's
barrier. (c) The corrected master count V2, reusable by every later rung.

---

### P2 — class (b) DIRECT CONSTRUCTION: build the common point fibre-by-fibre on the union-support densities

**Thesis.** Do not charge anything: *construct* the witness. Collapse both
distributions to their occupancy densities $\mu_{\mathbf F}=\mathbb
E_{f}[f^2]$, $\mu_{\mathbf G}=\mathbb E_g[g^2]$ (nonnegative, mean 1, degree
$\le2d$; incompatibility $\iff\mu_{\mathbf F}\mu_{\mathbf G}\equiv0$, i.e. the
two **union supports** $U,V$ are disjoint — `0023-strategist-1` R1, CONDITIONAL
in the ledger, one paragraph to verify), apply S7b to each *density* to get
windows $V_F,V_G$ of size $\le2d$, and exhibit a point of $U\cap V$ by choosing
the off-window pattern $w$ first (both traces are then nonempty by
surjectivity) and the in-window point second, with a positivity/counting
argument on the $\le4d$-dimensional cube.

**Key step everything turns on.** **FIBRE-BALANCE** (V5) at
$1/\mathrm{poly}(d)$, or any substitute that survives the mismatch between the
fibre normalisation $\alpha_w$ and the global $\alpha$. Equivalently: find one
$w$ whose two traces are *both* not-too-thin relative to their global densities,
then contradict disjointness inside a $\le4d$-cube using the influence
hypothesis transported through the exact identity
$\mathrm{Inf}_i(\mathbf 1_A)=\mathbb E_w[\mathrm{Inf}^{(w)}_i(\mathbf 1_{A_w})]$
(§0.5 G2). The plan's whole novelty is that the distribution quantifier is
**eliminated before** any window is chosen — S7b is applied to a single
function per side, so card S7's obstacle (ii) (non-canonicity across a family)
**cannot arise**. That is the structural reason this plan is independent of P1.

**FALSIFIABLE MILESTONE (< 2 pages).** Decide FIBRE-BALANCE, in the
pair-of-sets form (no distributions): for cross-disjoint degree-$\le d$ sets
$A,B$ and $W=W_A\cup W_B$, is $\mathbb E_w[\min(\alpha_w/\alpha,\beta_w/\beta)]
\ge1/\mathrm{poly}(d)$? Compute it exactly on: the codim-$d$ subcube pair
(value $1$: every fibre has $\alpha_w=2^{-d}=\alpha$, $\beta_w=\beta$), the
address pair (value $1-o(1)$: $\alpha_w=(2m_w+1)/2^{k+1}$ with $m_w$
binomial, so $\alpha_w\approx\alpha=\tfrac12$ off a set of measure
$2^{-\Theta(2^k)}$), the grid, and the $d=2$ class exhaustively; then attempt
either a proof at $1/\mathrm{poly}(d)$ or an explicit anti-concentrated pair
(the shape to hunt: $A$'s mass exponentially concentrated on a fibre-set $S$
while $A$ still meets every fibre off $S$ in a single point, $B$ mirror-image).
**Refuted** by such a pair — which would be a *new* certified obstruction, not a
counterexample to R2.

**TRAP (I02).** If FIBRE-BALANCE is only $2^{-\Theta(d)}$-true, this plan
yields at best a PARTIAL and must declare $\delta(d)=2^{-\Theta(d)}$, i.e. no
progress past K1 — stated here so a prover cannot sell it otherwise.

**S7b usage.** **WINDOW only**, and applied to a *degree-$2d$* object (the
density), so the window is $\le2d$: the plan must state that constant honestly.
Density consequence unused.

**I01.** Not cited at all (the plan is constructive; it does not use R1's
payment engine). No re-derivation.

**Prior probability of proving R2: 10%.** Reasoning: the collapse to densities
is free and removes the hardest quantifier, and S7b applies to densities
verbatim (ℝ-valued, nonzero) — a genuinely new configuration nobody has looked
at. Against: constructive arguments must beat the adversary at *every* fibre
choice, and the normalisation mismatch is a real leak with an exponential floor;
also the plan loses the factor-2 in degree twice (window $\le2d$, degree $2d$),
which matters only for constants but signals that the analytic slack is thin.
R3-liftability: **excellent** — the plan already works with nonnegative
degree-$2d$ functions, which *is* R3's class, so a success here likely proves
R3 simultaneously. That is the main reason it is ranked above P3 despite the
lower prior.

**Yield if it fails.** The FIBRE-BALANCE quantity, computed on every known
extremal and either proved or refuted — the missing third axis of refuter-3's
obstruction map (its §6 "NOT ruled out (iii)" asks precisely for a fourth
cheap-coordinate mechanism; an anti-concentrated pair *is* one, and the search
is guided rather than blind). Plus the verified density reformulation
(`0023-strategist-1` R1 upgraded from CONDITIONAL), which every later rung
needs.

---

### P3 — class (c) REFUTATION: hunt a mechanism whose $\varepsilon\!\cdot\!d\to0$, starting from refuter-3's flagged $d=3$ gap

**Thesis.** R2 is false, and the witness is refuter-3 §6's "NOT ruled out (iii)":
a fourth cheap-coordinate mechanism, with many relevant coordinates of influence
$2^{-\Theta(d)}$ carrying the conflicts while the expensive core is diluted
across the support — first visible as $\varepsilon^*_{\mathrm{ind}}(3)<1/6$
using windows $4$–$6$, where refuter-3's coverage is thin (365 disjoint pairs
out of $4\cdot10^5$ draws; window-6 not enumerable by its recursion).

**Key step everything turns on** — and this is the part `0023-refuter-4` is
**not** doing, so the plans do not duplicate: **the scaling step.** A seed at
$d=3$ with $\varepsilon\cdot d<1/2$ does **not** refute R2: refuter-1 §4.3 and
refuter-3's tensor/transport rule preserve $\varepsilon\cdot d$ *exactly*, so
any seed only improves the constant, never the rate. A refutation therefore
needs a composition rule under which $\varepsilon\cdot d$ **decays** — i.e. a
way to grow $d$ by $D$ while growing the influence dilution by more than $D$.
The plan's real target is that rule; the $d=3$ probe is its calibration.
Concretely: search for compositions where the two sides' degrees grow
*asymmetrically* (the union/product asymmetry of refuter-1 (O2), which
plateaued at $4/11$ in the signed class and has never been run inside
$\mathcal C^{\mathrm{ind}}_d$), and for hub-free architectures (refuter-3 §5.3
certifies that address hubs cannot dilute; a refutation must avoid hubs
entirely).

**What a hit at $d=3$ would mean (stated, per the task, without duplicating the
search).** (i) It would be the **first sub-$1/(2d)$ indicator pair**, killing
refuter-3 §3's finding that "the indicator restriction is exactly what stops
$1/5$" and moving the $\mathcal C^{\mathrm{ind}}$ frontier off the junta
frontier for the first time. (ii) It would **refute (PAY$\star$) at $p=1$**
(P1's headline constant) while leaving P1 alive at
$p=1/\mathrm{poly}(d)$ — so P1's milestone should be read jointly with
refuter-4's output. (iii) It would **not** refute R2, and any artifact claiming
otherwise is committing the rate-vs-constant error above. (iv) It would make
FIBRE-BALANCE (P2) the prime suspect and hand P6 a fourth certificate.

**FALSIFIABLE MILESTONE (< 2 pages).** Prove or refute the **rate-rigidity
dichotomy**: *every composition rule that (a) keeps both sides inside
$\mathcal C^{\mathrm{ind}}$, (b) is built from tensoring/transport/direct sums
of seeds, preserves $\varepsilon\cdot d$ up to a constant factor.* Two pages:
compute $\varepsilon\cdot d$ for the closure of the known seeds under
tensor, disjoint-coordinate union, and the asymmetric block construction of
refuter-1 §4.2 restricted to indicators; either exhibit one rule that decays
(refutation momentum, and R2 is in real danger) or record the closure as
$\varepsilon\cdot d=\Theta(1)$ (which is the strongest evidence for R2 short of
a proof, and tells the refuter to stop composing and start hunting primitives).

**TRAP (I02).** Not applicable in the same form (a refutation has no
threshold), but the dual trap is: a hit that only improves the constant must be
reported as **a constant improvement, not a refutation**. Written into the
milestone.

**S7b usage.** Used only as a **search constraint** (both sides must surject off
$\le d$ coordinates, which prunes the space) and — legitimately here — through
the **density** floor $\alpha\ge2^{-d}$, which bounds the enumeration. No
proof-side use, so the K1 cap on density arguments is irrelevant.

**I01.** Cited only to skip the junta subclass (already settled) — no
re-derivation.

**Prior probability of refuting R2: 7%.** Reasoning: two independent exhaustive
sweeps (refuter-2, refuter-3) plus a proved $d\le2$ frontier plus certified
rigidity of both known cheap-coordinate mechanisms; the singleton case is
essentially closed by P4's carded chain, so falsity is confined to a strictly
distributional phenomenon with no known mechanism. But the $d\ge4$ class was
never enumerated and composition rules have only been checked for the three
known ones. Probability that the *milestone* returns decisive information:
$>85\%$.

**Yield if it fails.** The closure computation is the campaign's first
**rate-rigidity statement** ("no composition of known seeds beats $\Theta(1/d)$
inside the indicator class"), which is exactly what a Weakener or a barrier
write-up needs, and it retires the "just search harder" option with a reason.

---

### P4 — class (d) WEAKENING: bounded-support R2, via OSSS + decision-tree-depth-vs-degree

**Thesis.** The strongest special case I believe provable **now** is R2 with
$\lvert\mathrm{supp}\,\mathbf F\rvert,\lvert\mathrm{supp}\,\mathbf G\rvert\le
S(d)=\mathrm{poly}(d)$, at $\delta(d)=1/(8\,D(d)\,S(d))=1/\mathrm{poly}(d)$,
because the singleton case of R2 is *already* a consequence of printed
literature the campaign has not yet carded, and bounded support reduces to
singletons with a factor $S$.

**Key step everything turns on.** The single-function chain
[**[MEMORY] — every link must be carded before any prover cites it; this is the
plan's gate**]: (i) **OSSS**: for Boolean $h$ computed by a decision tree with
query probabilities $\rho_i$, $\mathrm{Var}(h)\le\sum_i\rho_i\,
\mathrm{Inf}^{\mathrm{flip}}_i(h)$, hence $\mathrm{Var}(h)\le
D\cdot\max_i\mathrm{Inf}^{\mathrm{flip}}_i(h)$ with $D$ the depth;
(ii) **depth vs degree**: $D(h)\le\mathrm{poly}(\deg h)$ (candidates to card:
Midrijanis, quant-ph/0403168, $O(\deg^3)$ — *already a latent queue item in the
ledger*; or the classical Nisan–Smolensky route, whose block-sensitivity
ingredient $\mathrm{bs}\le\sqrt{2/3}\deg^2+1$ **is** carded and READ, card S6c
Thm 1.2 (1.5)); (iii) card S6a's influence dictionary
$\mathrm{Inf}^{\mathrm{flip}}_i(\mathbf 1_A)=4\,\mathrm{Inf}_i(\mathbf 1_A)$.
Then for a cross-disjoint pair, $\alpha+\beta\le1$ forces one side to have
density $\le1/2$, and that side satisfies
$$\max_i\mathrm{Inf}_i(f_A)=\frac{\max_i\mathrm{Inf}_i(\mathbf 1_A)}{\alpha}\ \ge\ \frac{\alpha(1-\alpha)}{4D\alpha}\ =\ \frac{1-\alpha}{4D}\ \ge\ \frac1{8D}.$$
Support reduction: the highest-probability $f^*\in\mathrm{supp}\,\mathbf F$ has
$\Pr[f^*]\ge1/S$, so $\mathrm{Inf}_i(f^*)\le S\delta$ for every $i$; apply the
display to the sparser of $f^*,g^*$. **[STRAT-CLAIM]**, half a page.

**FALSIFIABLE MILESTONE (< 2 pages).** (i) Card OSSS and one depth-vs-degree
bound, checking hypotheses against $\mathbf 1_A$ (total, $\{0,1\}$-valued —
both fine; watch the $\{0,1\}$ vs $\{\pm1\}$ variance and influence
conventions, which is where the factor-4 citation defect lives, card S6a flag
6). (ii) Write the half-page display above. **Refuted** if OSSS's printed
hypotheses exclude our objects (e.g. if the printed form is restricted to
monotone $h$ or to a *random* tree with an extra condition our $D$ bound cannot
supply), or if no printed poly depth-vs-degree bound survives carding — in
which case refuter-3 §5.3's "protected by the Boolean case of
Aaronson–Ambainis" remark must be **struck from the record** rather than
promoted, and the campaign learns that even the singleton case of R2 is open.

**Two consequences worth more than the rung itself.** (a) The same display,
with no support restriction, proves **R2 with the max-influence hypothesis in
place of the average** for *every* support size. I02 forbids selling that as R2
(and this plan does not), but it converts the difficulty statement into a
theorem: **the entire content of R2 is dilution of influence across the
distribution, nothing else** — precisely refuter-3 §5.3's claim, upgraded from
a [MEMORY] remark to a carded result. (b) It closes I02's "Partials" clause
for the sub-class of bounded-size supports without touching the exponential
regime.

**TRAP (I02).** Threshold is $1/\mathrm{poly}(d)$ for $S=\mathrm{poly}(d)$,
so the trap is avoided — but the plan is a **declared PARTIAL** in any case:
it does not establish R2, and the restriction ("supports of size
$\le\mathrm{poly}(d)$", or "max- instead of average-influence") must appear in
the artifact's own verdict line and next to any theorem statement.

**S7b usage.** **NEITHER** — no window, no density. Complete independence from
the S7b question is deliberate: if §0's ruling were somehow wrong, this plan is
unaffected.

**I01.** Not used. (Note the free corollary that needs no plan at all: any
distribution supported on degree-$\le d$ sets that are $k$-juntas lies in
$\mathcal C^{\mathrm{junta}}_k$, so **frozen I01 at parameter $k$** settles that
sub-class at $\delta=1/(3k)$ — inverse-polynomial whenever
$k=\mathrm{poly}(d)$. One paragraph, black-box citation only, and it should be
recorded as a partial the moment R2 is attempted.)

**Prior probability of proving R2: 2%.** (Probability the *rung* is proved:
**70%**, gated on the two cards; probability the max-influence corollary lands:
75%.) Reasoning: the mathematics is a short assembly of known theorems; the
risk is entirely bibliographic. The lift to R2 is essentially nil because the
$S$ factor is not removable — the grid shows average-influence families with
unbounded support and no compatible pair at $1/(2d)$, so no argument that
passes through a per-function influence bound can reach R2's hypothesis.
R3-liftability: **fails** — every link needs $h$ two-valued (cards S6/S6b's
warning), so this is a *declared detour* under IG5, acceptable because its
deliverable is a partial and a difficulty-localisation, not a route to the top.

**Yield if it fails.** Two carded theorems the campaign will want at R5 anyway
(R5 *is* the signed singleton rung), and a decisive answer to whether the
singleton case of R2 is open — which re-ranks every other plan and, if it is
open, means refuter-3 §5.3's rigidity discussion rests on nothing.

---

### P5 — class (e) TRANSFER: import query complexity — certificate windows of size $O(d^4)$

**Thesis.** Query complexity supplies a **second** $\mathrm{poly}(d)$ window,
disjoint in provenance from S7b: every degree-$\le d$ set is a union of
subcubes of codimension $\le C=O(d^4)$, so every point of $A$ and every point of
$B$ carry $\mathrm{poly}(d)$-sized certificates, and disjointness forces two
certificates to fix a **common coordinate oppositely** — R0's calibration
mechanism, at $\mathrm{poly}(d)$ instead of $2^{\Theta(d)}$.

**Named machinery imported.** Certificate complexity, block sensitivity,
sensitivity (query complexity / decision-tree analysis), via
$C(h)\le\mathrm{bs}(h)\cdot s(h)\le\mathrm{bs}(h)^2$ (textbook, **provable
inline in one paragraph**: take a maximal family of disjoint minimal sensitive
blocks at $x$; there are $\le\mathrm{bs}$ of them, each of size $\le s$, and
their union is a certificate) combined with the **carded, READ**
$\mathrm{bs}(h)\le\sqrt{2/3}\deg(h)^2+1$ (card S6c, Discrete Analysis 2022:19
Thm 1.2 (1.5)). So $C(\mathbf 1_A)\le(\sqrt{2/3}d^2+1)^2=O(d^4)$ with **no new
source request**.

**Key step everything turns on.** The **certificate-to-influence bridge**: from
"the certificates of $x\in A$ and $y\in B$ share an oppositely-fixed
coordinate $i$" to "$\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)$ is large on
average over a suitable choice of certificates". A certificate coordinate need
not be *sensitive*, which is the honest gap. The available foothold
[STRAT-CLAIM]: if $T$ is a **minimal** certificate for $x$ and $i\in T$, then
inside the codimension-$(\lvert T\rvert-1)$ subcube fixing $T\setminus\{i\}$
there is at least one $i$-edge cut by $A$ — so minimal certificates do generate
boundary, and the question is purely one of *multiplicity*: how many cut
$i$-edges does averaging over $x\sim\mathrm{Unif}(A)$ produce, relative to
$2^N\alpha$? That is a clean, self-contained quantitative question.

**FALSIFIABLE MILESTONE (< 2 pages).** Prove or refute the
**certificate payment inequality**: for cross-disjoint degree-$\le d$ sets, with
$T_A(x),T_B(y)$ minimal certificates and $\Sigma$ the set of coordinates fixed
oppositely by the two,
$$\mathbb E_{x\sim A}\,\mathbb E_{y\sim B}\Bigl[\sum_{i\in\Sigma(x,y)}\bigl(\mathrm{Inf}_i(f_A)+\mathrm{Inf}_i(f_B)\bigr)\Bigr]\ \ge\ c .$$
Two pages: (i) prove $\Sigma\ne\emptyset$ always (two disjoint subcubes must fix
some coordinate oppositely — three lines); (ii) evaluate the left side exactly
on the codim-$d$ subcube pair, the address pair, and the grid (the values are
$\ge1/2$, $\ge k/4$ and $1$ respectively — the two certified killers are
neutralised here for the *same structural reason* as in §0.3, namely that the
window is $\mathrm{poly}(d)$, but by a different window); (iii) attempt the
general bound or exhibit a pair where minimal certificates concentrate on
influence-floor coordinates. **Refuted** by such a pair.

**Barrier pre-check, explicit.** IG2 clear: the certificate window is
$O(d^4)$, never the relevant-coordinate set (for the address set the certificate
is $\{a_1..a_k,y_j\}$, of size $d$, while $J=k+2^k$). IG3 clear: the payment is
a **sum** of both sides' influences on $\Sigma$, never
$\min(\mathrm{Inf}_if,\mathrm{Inf}_ig)$ — the codim-$d$ pair therefore does not
bite. IG1 clear: best output $c/(2\cdot O(d^4))\ll1/(2d)$.

**TRAP (I02).** Threshold is $\mathrm{poly}(d)$ by construction ($C=O(d^4)$ is
a **polynomial** bound; no junta size enters). If the bridge only yields
$c=2^{-\Theta(d)}$, the artifact is a PARTIAL and must declare it.

**S7b usage.** **NEITHER window nor density** — S7b is not used at all. This is
the plan's independence guarantee: it needs no Chang–Fang input, so §0's ruling
is irrelevant to it.

**I01.** Cited only as the frozen statement, for the observation that the
mechanism specialises to R1's when the sets are cylinders. No re-derivation.

**Prior probability of proving R2: 12%.** Reasoning: the window bound is a
theorem with a carded ingredient and the conflict structure is exactly R0's, so
the skeleton is sound and $\mathrm{poly}(d)$ throughout; the bridge from
certificates to influence is the one unknown, and it is a *local* question
(unlike P1's global one), which is why the prior is not lower. Against it: the
$O(d^4)$ window makes the constant loose, and the bridge is exactly the kind of
"certificates are not sensitivity" mismatch that has defeated several
query-complexity transfers before. R3-liftability: **fails** —
certificate/block-sensitivity machinery needs two-valuedness (card S6b's
explicit warning), so a success here is a *recorded detour* under IG5 that
proves R2 but hands R3 nothing. Ranked down for that reason, not for its prior.

---

### P6 — class (f) BARRIER: promote refuter-3's two killers into a stated internal barrier, and draw the line

**Thesis.** refuter-3's two certificates are not merely dead routes: they prove
a theorem about a *class of arguments*. State and prove it —
**"no argument whose per-pair input is (i) a payment bounded below in terms of
the partner's relevant-coordinate-window size, or (ii) the existence of a shared
coordinate heavy for both sides, can produce a threshold above
$2^{-\Theta(d)}$, at any rung R2–R6"** — and, in the same breath, prove that the
barrier does **not** cover the two $\mathrm{poly}(d)$ window functionals (S7b's
shattering window, P5's certificate window), so that the campaign stops
re-killing live routes and starts spending only on those.

**Key step everything turns on.** A definition, not an estimate: formalise a
*window-payment argument* as a pair $(W,\rho)$ — a window functional $W$ on
$\mathcal C^{\mathrm{ind}}_d$ and a nondecreasing $\rho$ — whose entire
per-pair input is $\pi_W(A,B)\ge\rho(\lvert W(A)\rvert,\lvert W(B)\rvert)$, fed
to the master count V2. Then prove the two caps:
$$\Theta_{\mathrm{rel}}(d):=\inf_{\text{cross-disjoint}}\frac{\pi_J(A,B)}{\lvert J(A)\rvert+\lvert J(B)\rvert}=2^{-\Theta(d)},\qquad
\theta^*(d)\le\frac1{2(2^d-1)},$$
the first from the address family, the second from the codim-$d$ subcube pair —
**both already computed exactly by refuter-3 §4**, so the mathematics is
present and the work is the class definition plus a scope lemma.

**The scope lemma, which is the plan's most valuable line.** Both witnesses are
**singleton pairs of normalised indicators**. Hence they belong to
$\mathcal C^{\mathrm{ind}}_d\subset\mathcal C^+_d\subset$ the full signed class,
and they are singleton-supported, so they are admissible objects at **R2, R3,
R4, R5 and R6 simultaneously**. Therefore the barrier, once proved, condemns the
technique class **at every remaining rung**, not just at R2 — the single most
consequential thing a barrier here can say, and it is nearly free.

**FALSIFIABLE MILESTONE (< 2 pages).** (i) State the class $(W,\rho)$
precisely, with the master count as the only permitted assembly; (ii) prove the
two caps from refuter-3's tables (re-deriving the address influences in five
lines so the barrier does not depend on unverified code); (iii) prove the scope
lemma; (iv) **the cross-check that decides the plan's value**: verify that the
S7b and certificate functionals are **outside** the class, i.e. exhibit the
quantities $\Theta_W$ for $W\in\{$shattering, certificate$\}$ and show that the
witnesses do not cap them (values $\ge1/2$ on both killers, §0.3 and §3.5).
**Refuted** if (iv) fails — i.e. if the class cannot be defined so as to
contain the killed routes while excluding the live ones. That outcome would be
*more* valuable than success: it would mean P1 and P5 are also capped, and the
rung's honest status would drop to "no known route above $2^{-\Theta(d)}$".

**What proving it would cost, and what it would settle.** Cost: one prover
unit, ≈2 pages, no new sources, no computation beyond re-deriving two influence
tables — cheap because refuter-3 did the hard part. It would settle: (a) that
I02's own flagged route ("re-base R1's payment on the total-influence budget")
is dead in its per-coordinate form, closing the rung's central open question
in the negative and redirecting it to window functionals; (b) that the same is
true at R3–R6, so the ladder's later rungs must not retry it; (c) the first
entry in the Contract's empty "Known barriers" section, and the exact
formulation the Contract's BARRIER CHECKLIST invites ("arguments using only
per-coordinate influence budgets cannot beat exponential thresholds" — now with
a proof and a sharp boundary). It would **not** settle R2 either way, and it
would **not** condemn P1/P2/P5, which is the point of clause (iv).

**TRAP (I02).** This plan is *about* the trap: its content is that a whole class
of arguments degrades exponentially in $d$. It claims no threshold and so
cannot be mistaken for a proof; the artifact must nonetheless state that a
barrier is not a refutation and leaves R2 open.

**S7b usage.** **WINDOW**, used only negatively/comparatively (to show the
shattering window escapes the cap). Density unused.

**I01.** Cited as the frozen statement to note that R1 *is* a member of the
capped class with $\lvert J\rvert\le d$ by fiat — which is exactly why R1 was
provable and R2 is not, in one sentence. No re-derivation.

**Prior probability of proving R2: 0%** (a barrier proves nothing about R2 —
reported honestly). Probability the barrier is established as stated: **55%**;
probability clause (iv) comes out *against* the live plans (the high-information
adverse outcome): **15%**.

**Yield if it fails.** Even a failed class definition produces the comparison
table of window functionals — junta vs shattering vs certificate, with each
one's certified cap or lack of one — which is the artifact any future worker on
this problem most needs, and which no existing campaign document contains.

---

## 4. Mutual independence (no two plans fail for the same reason)

| plan | class | dies **iff** | object it lives on | window used |
|---|---|---|---|---|
| **P1** | (a) reduction | the *global* pair-level inequality (PAY$\star$) is false: some cross-disjoint pair's two maximum-degree supports meet the partner's influence only on floor-level coordinates | one pair of sets, two top-monomial supports | shattering, $\le d$ |
| **P2** | (b) construction | FIBRE-BALANCE fails: a pair whose masses are anti-concentrated across fibres (a *third* obstruction, unrelated to either killer) | one pair of **densities**, fibre-wise | shattering of a degree-$2d$ object, $\le2d$ |
| **P3** | (c) refutation | R2 is true / every composition rule preserves $\varepsilon\cdot d$ (rate rigidity) — failure is *evidence for* R2, orthogonal to all proof plans | families and composition rules | none (search constraint only) |
| **P4** | (d) weakening | the printed OSSS / depth-vs-degree statements do not cover $\mathbf 1_A$ **(a bibliographic failure, not a mathematical one)**; as a route to R2 it dies on the non-removable support factor $S$ | one function, variance vs max influence | none |
| **P5** | (e) transfer | minimal certificates can concentrate on influence-floor coordinates: the certificate-to-influence bridge has no multiplicity (a *local* failure) | one point of each set, minimal certificates | certificate, $O(d^4)$ |
| **P6** | (f) barrier | the technique class cannot be cut so as to contain the two killed routes and exclude the two live ones (clause (iv)) — a definitional failure | classes of arguments, not objects | all three, comparatively |

Pairwise checks of the non-obvious cases. **P1 vs P2:** both use S7b, but P1's
inequality is global over the pair while P2's is a fibre-wise average; P1 can
hold with FIBRE-BALANCE false (a direct proof of (PAY$\star$) need not go
through fibres) and P2 can succeed with (PAY$\star$) false (a construction needs
one good fibre, not a payment on every pair). **P1 vs P5:** different windows,
different theorems (Chang–Fang shattering vs block-sensitivity), and P5 needs no
S7b at all, so §0's ruling cannot kill both. **P4 vs P5:** both borrow from
query complexity, but P4 uses an *inequality about one function* (OSSS) and
fails bibliographically or on the $S$ factor, while P5 uses the *combinatorics
of certificates on a pair* and fails on multiplicity; neither failure implies
the other. **P3 vs everything:** its failure is positive evidence for the other
five. **P6 vs P1/P5:** P6 is explicitly constructed to *test* whether it kills
them (clause (iv)); if it does, that is a single informative event, not two
plans failing for one reason.

---

## 5. Ranking by (information gained)/(effort), with the wave order

1. **P1 (REDUCTION).** Half of it — the reduction, the master count with
   pair-independent windows, and the unconditional positivity theorem $W_A\cap
   \mathrm{relevant}(B)\ne\emptyset$ — is provable *today* in one page, and the
   other half is a machine check on code that already exists. It is also the
   only plan whose success would prove R2 *with the exact optimal constant*
   ($\varepsilon^*_{\mathrm{ind}}(d)=1/(2d)$), and the only one that reproduces
   both proved frontier values. Highest information per unit effort in the set.
   **Run first.**
2. **P6 (BARRIER).** Cheapest genuine deliverable (refuter-3 supplied the
   certificates; the work is a definition and a scope lemma), and it is the plan
   that *protects the campaign's budget*: clause (iv) either certifies that P1
   and P5 are outside the capped class — licensing all further spend — or
   reveals that they are inside it, which would be the most important negative
   result available at this rung, and would also condemn the technique class at
   R3–R6. Run **concurrently with P1**, since it is the pre-check P1 deserves.
3. **P4 (WEAKENING).** Two source cards and half a page of assembly for: a
   proved partial, a max-influence theorem at every support size, the
   discharge of refuter-3 §5.3's load-bearing-for-nothing [MEMORY] remark, and
   the theorem "R2's content is exactly dilution". Low novelty, very high
   certainty, negligible effort. Its cards are wanted at R5 regardless.
4. **P5 (TRANSFER).** New mechanism, no new sources, $\mathrm{poly}(d)$
   throughout, and a *local* key question. Ranked below P4 only because of its
   R3-detour status (IG5) and the loose $O(d^4)$.
5. **P2 (DIRECT CONSTRUCTION).** Highest R3-value of the set (it already works
   on nonnegative degree-$2d$ functions, i.e. R3's class), and its milestone
   isolates a genuinely new obstruction; but the constructive route is the
   longest runway and the leak has an exponential floor.
6. **P3 (REFUTATION).** Ranked last **only because its cheap half is already in
   flight** as `0023-refuter-4`: the marginal work here is the composition/rate
   question, which is more expensive and less likely to fire. Do not duplicate
   refuter-4's search; read its output into P1's milestone (a hit refutes
   $p=1$, not R2 — §3.3).

**Suggested wave (cycle 3–4).** Provers on **P1** and **P6** immediately (they
are complementary and both mostly write-up); **P4** in parallel *behind its
source gate* (OSSS + one depth-vs-degree bound); then **P5**, then **P2**.
`0023-refuter-4` continues independently; its verdict is an input to P1's M1b
and to P3's milestone, not a substitute for either.

---

## 6. Discipline notes binding on every prover

**6.1 The TRAP line is mandatory.** Each plan above carries an explicit TRAP
paragraph. Any artifact produced under these plans whose threshold degrades
exponentially in $d$ must declare itself **PARTIAL** in its verdict line, per
I02. Two of the six (P4, and P1's fallback) can legitimately produce
$\mathrm{poly}(d)$ thresholds under a *declared restriction*; those restrictions
must appear next to the theorem statement, not only in the verdict.

**6.2 S7b declarations, collected** (per card S7b's scout remark that the
density consequence is capped at K1 and therefore worthless): P1 — **window**;
P2 — **window** (of a degree-$2d$ object); P3 — density and window, **as search
constraints only**; P4 — **neither**; P5 — **neither**; P6 — **window**,
comparatively. **No plan derives a threshold from the $2^{-d}$ density floor.**

**6.3 Frozen I01 is a black box.** No plan requires re-deriving or
re-verifying I01. Where a plan wants a *fibre-level or set-level* payment
inequality, note that R1's internal (F3)/(F4) are stated for **cylinder
patterns**; their extension to arbitrary degree-$\le d$ sets is **not** part of
the frozen statement and must be proved afresh and labelled as new. Citing
"I01" for such an extension is a class-(D) citation defect.

**6.4 [MEMORY] register opened by this artifact** (nothing downstream may cite
these until carded):
* **OSSS inequality** (P4 gate) — needed as: $\mathrm{Var}(h)\le\sum_i\rho_i
  \mathrm{Inf}^{\mathrm{flip}}_i(h)$ for a decision tree with query
  probabilities $\rho_i$. Currently attested in this campaign only as a
  *citation inside* card S1.d ([ACC22] p. 11 mentions [OSSS05]); the statement
  itself has never been read.
* **Decision-tree depth vs degree**, $D(h)\le\mathrm{poly}(\deg h)$ (P4 gate) —
  Midrijanis quant-ph/0403168 ($O(\deg^3)$) is already a latent ledger queue
  item; the Nisan–Smolensky route needs only carded material plus one textbook
  step.
* **$C(h)\le\mathrm{bs}(h)\cdot s(h)$** (P5) — textbook; **prove inline**, do
  not card.
* **refuter-3 §5.3's "protected by the Boolean case of Aaronson–Ambainis"** —
  per the task, this remark is [MEMORY]-tagged and load-bearing for nothing.
  **P4 is the only plan that wants it, and P4's first action is to card it.**
  Until then no artifact may cite it, including in prose about rigidity.

**6.5 Two claims in §0 that a prover must verify before use.** The fibre-average
influence identity (§0.5 G2) and the positivity lemma (§0.5 G1) are
[STRAT-CLAIM]. They are short, but they are the load-bearing new mathematics of
this artifact and must be written out and refereed, not inherited.

### SOURCE REQUEST ###

Rank 1: O'Donnell–Saks–Schramm–Servedio, *Every decision tree has an influential
variable* (FOCS 2005; arXiv cs/0508071) — the exact statement and hypotheses of
the OSSS inequality (theorem + the one page containing it). P4's entire chain
collapses without it, and refuter-3 §5.3's rigidity remark cannot be promoted
past [MEMORY]. Rungs tried by this strategist: none directly (no web access in
this role); the Scout's ladder rung 1 (arXiv) should reach it, so this is
plausibly a *read*, not an upload. Fallback: run P4 with the step marked
[SOURCE-BLOCKED: OSSS] and everything downstream conditional.

Rank 2: G. Midrijanis, *Exact quantum query complexity for total Boolean
functions* (quant-ph/0403168) — the printed decision-tree-depth-vs-degree bound
$D(h)=O(\deg(h)^3)$, statement and hypotheses only. Already a latent ledger
queue item. Fallback: the Nisan–Smolensky route using carded S6c Thm 1.2 plus
one textbook step, at a worse polynomial — acceptable, since P4 only needs
$\mathrm{poly}$.

Rank 3 (below the bar, recorded only): nothing. All other load-bearing material
in this artifact is carded and READ (S1, S6a–S6d, S7, S7b) or is elementary and
provable inline.

### END OF ARTIFACT 0023-strategist-2 ###

