---
id: 0023-prover-2-u0
agent: prover
model: claude-opus-5[1m]
cycle: 3
status: COMPLETE (unit 0 of 5)
---

# Unit 0 — METHOD SKETCH (plan P1, class (a) REDUCTION; target I02 / rung R2)

**Running verdict (to be confirmed at the Final unit): PARTIAL.**
Unconditional theorems obtained (units 1): the corrected master count, the
positivity lemma G1, the reduction `(PAY★)⇒R2`, and an unconditional
threshold `δ(d) < 2^{-d}/d` for R2 — which is *exponential in d*, hence by
I02's own rule a **PARTIAL, not a proof of R2**, declared here and in the
verdict. Refutation obtained (unit 2): P1's key step **(PAY★) as the
strategist states it (quantified over every maximum-degree monomial support)
is FALSE**, exponentially, with an exact certificate. What survives (unit 3):
the *choice-map* form of (PAY★), for which I isolate a repaired window
functional and record exactly which further object would refute it.

## 0. Notation fixed for this artifact

$\{\pm1\}^N$ carries the uniform measure; all expectations are over it.
Every $f:\{\pm1\}^N\to\mathbb R$ has a unique multilinear expansion
$f=\sum_{S\subseteq[N]}\hat f(S)\,x^S$, $x^S=\prod_{i\in S}x_i$; the monomials
$x^S$ are orthonormal. As in the Contract (case $\mathcal Y=\mathbb Z_2$),
$\deg f=\max\{|S|:\hat f(S)\ne0\}$ and $\mathrm{Inf}_i(f)=\sum_{S\ni i}\hat
f(S)^2$. For $\emptyset\ne A\subseteq\{\pm1\}^N$ put $\alpha=|A|/2^N$ and
$f_A=\mathbf 1_A/\sqrt\alpha$ (so $\|f_A\|_2=1$ and
$\mathrm{Inf}_i(f_A)=\mathrm{Inf}_i(\mathbf 1_A)/\alpha$). Write
$$\mathrm{rel}(A):=\{i\in[N]:\exists x,\ \mathbf 1_A(x)\ne\mathbf 1_A(x^{\oplus i})\}$$
(the relevant coordinates), and for $W\subseteq[N]$ let $\pi_{[N]\setminus
W}(A)$ be the projection of $A$ to the coordinates outside $W$.

**Definition (shattering window).** For $\emptyset\ne A$ with
$\deg\mathbf 1_A\le d$,
$$\mathcal S_d(A):=\bigl\{W\subseteq[N]\ :\ |W|\le d,\
\pi_{[N]\setminus W}(A)=\{\pm1\}^{[N]\setminus W}\bigr\}.$$
"$A$ surjects off $W$." This is the *only* use this artifact makes of card
S7b; the density consequence $\alpha\ge2^{-d}$ is never used to derive a
threshold (S7b usage declaration: **WINDOW only**, per strategist §6.2).

**Definition (payment).** For a pair of nonempty $A,B$ and windows
$W_A,W_B$,
$$\pi\bigl((A,W_A),(B,W_B)\bigr):=\sum_{i\in W_B}\mathrm{Inf}_i(f_A)\ +\ \sum_{i\in W_A}\mathrm{Inf}_i(f_B).$$
Note it is a **sum over the two sides**, never a $\min$ (strategist IG3), and
each side is charged on the **partner's** window (strategist V2(i)).

## 1. Skeleton

| # | statement | status |
|---|---|---|
| **L1** | *Nonvanishing.* $p:\{\pm1\}^n\to\mathbb R$ multilinear, $p\not\equiv0$, $\deg p\le k$ $\Rightarrow$ $\Pr_x[p(x)\ne0]\ge2^{-k}$. | PROVED-INLINE (u1) |
| **L2** | *Influence quantum.* $\emptyset\ne A$, $\deg\mathbf 1_A\le d$, $i\in\mathrm{rel}(A)$ $\Rightarrow$ $\mathrm{Inf}_i(\mathbf 1_A)\ge2^{-1-d}$, i.e. $\mathrm{Inf}_i(f_A)\ge2^{-1-d}/\alpha$. | PROVED-INLINE from L1 (u1) |
| **L3** | *Window existence.* $\mathcal S_d(A)\ne\emptyset$; every maximum-degree monomial support of $\mathbf 1_A$ lies in $\mathcal S_d(A)$; $\mathcal S_d(A)$ is closed under enlargement up to size $d$. | CARD S7b (T3.4 / T3.2), [READ] |
| **L4 = G1** | *Positivity (two-family, new).* $A,B\ne\emptyset$, $A\cap B=\emptyset$, $W\in\mathcal S_d(A)$ $\Rightarrow$ $W\cap\mathrm{rel}(B)\ne\emptyset$. (No degree hypothesis on $B$ is used.) | PROVED-INLINE (u1) |
| **L5** | *Master count (corrected, pair-independent windows).* For any window map $f\mapsto W(f)$ with $|W(f)|\le \omega$ depending only on $f$: incompatible $(\mathbf F,\mathbf G)$ with per-coordinate average influences $\le\delta$ satisfy $\mathbb E_{f,g}[\pi]\le2\omega\delta$. | PROVED-INLINE (u1) |
| **T1** | *Reduction.* If $\pi\ge p(d)$ for all cross-disjoint pairs at the chosen windows, then R2 holds with any $\delta(d)<p(d)/(2d)$. | PROVED-INLINE (u1) |
| **T2** | *Unconditional threshold.* $\pi\ge2^{1-d}$ for **every** cross-disjoint degree-$\le d$ pair and **every** $W_A\in\mathcal S_d(A)$, $W_B\in\mathcal S_d(B)$; hence R2 holds for every $\delta(d)<2^{-d}/d$. **Exponential: PARTIAL by I02's rule.** | PROVED-INLINE (u1) |
| **T3** | *Refutation of (PAY★).* An explicit family $(\mathsf A_d,\mathsf B_d=\mathsf A_d^{\,c})$ of cross-disjoint degree-$d$ sets and maximum-degree monomial supports $W_{\mathsf A}=W_{\mathsf B}=U$ with $\pi=d\,2^{1-d}$. So (PAY★) at $p(d)\ge1/\mathrm{poly}(d)$ is false, and $p=1$ already fails at $d=3$ ($\pi=3/4$). | PROVED-INLINE + machine-checked (u2) |
| **T4** | *Anatomy.* The general two-parameter family behind T3; exact influence profile; the complete list of its maximum-degree supports; the exact payment on each. | PROVED-INLINE (u3) |
| **T5** | *What survives.* The choice-map form (PAY★$_\mathcal W$) is not refuted; a repaired window functional $W_\tau(f)=(\text{a max-degree support})\cup\{i:\mathrm{Inf}_i(f)\ge\tau\}$ of size $\le d+d/\tau$ pays $\ge1$ on all four known extremal families and on T3's family; and a single explicitly described object (a balanced degree-$D$ Boolean function with all influences $\le\tau$ and light maximum-degree supports) would refute it. | PROVED-INLINE + table (u3) |
| **LEAN** | Type-checked skeleton of the definitions and of L4, L5, T1 (bodies `sorry`). | u4 |

No case split is needed: the argument is a chain. The only branch is T3 vs T5
(all-windows vs choice-map quantification of (PAY★)), and both branches are
resolved.

## 2. Where the plan's [STRAT-CLAIM]s land (each refereed, none inherited)

* **V2 (master count)** — refereed and correct as stated; proved as **L5**
  here. Both drafting warnings are real and are respected.
* **V3 / (PAY★)** — refereed and **REFUTED as stated** (T3). The reduction
  V3$\Rightarrow$R2 itself is correct and is **T1**.
* **§0.5 (G1)** — refereed and correct; proved as **L4**, in the sharper form
  that no degree hypothesis on $B$ is needed.
* **§0.3 (the killers pay $\Omega(d)$ on S7b windows)** — I re-derive the two
  entries I use (codim-$d$ subcube pair, grid pair) from scratch in u3; they
  are correct. But §0.3's inference "*therefore the S7b window route is
  immune*" does **not** follow, and T3 is the explicit obstruction it missed:
  immunity to the two *known* killers is not immunity.
* **V4 (calibration $p=1$)** — the two data points are correct, but the
  extrapolation is false: $p=1$ fails at $d=3$ (T3).
* **V5 / FIBRE-BALANCE (G2)** — the fibre identity is correct (used
  diagnostically in u3, proved there); I do **not** cross the fibre-balance
  normalisation gap and I claim nothing that needs it. T3 in fact shows the
  gap is not merely a proof difficulty at the level of the S7b window: the
  quantity it controls really does fall exponentially for the family of T3.
* **§0.5's unconditional corollary** ($\max\delta\ge2^{-1-d}/(2d)$) — correct
  but not tight; T2 sharpens it to $2^{-d}/d$ using $1/\alpha+1/\beta\ge4$.

## 3. Honest statement of what is NOT attempted

* No step uses R1's projection-disjointness ((F3)/(F4) of `0023-prover-1`);
  I01 is cited only as a frozen statement, never re-derived (strategist §6.3).
* No step charges a payment against relevant-coordinate count (refuter-3
  killer (a)), and no step uses $\min(\mathrm{Inf}_if,\mathrm{Inf}_ig)$
  (killer (b)).
* No step uses the junta bound (cards S6b–S6d), so no threshold here degrades
  because of $M(d)=2^{\Theta(d)}$; T2's exponential comes from the influence
  *quantum* (card S6a's engine, reproved inline as L2), which is a different
  and irreducible source (S6a "what it does NOT say", bullet 1).
* No source outside card S7b is load-bearing. Nothing is [SOURCE-BLOCKED] in
  units 1–3. Unit 3 flags one *optional* strengthening that would need OSSS +
  depth-vs-degree (the strategist's open source request); it is used only to
  say which further result would settle T5's status, never inside a proof.

EMITTED unit 0 of 5; NEXT UNIT: u1 = M1a (L1, L2, L3, L4, L5, T1, T2);
ARTIFACT 0023-prover-2.

### END OF ARTIFACT 0023-prover-2-u0 ###
