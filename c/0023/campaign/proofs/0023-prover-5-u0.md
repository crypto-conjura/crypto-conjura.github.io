id: 0023-prover-5-u0
agent: prover
model: claude-opus-5[1m]
cycle: 5
status: SKETCH

# P2 method sketch — the fibre-wise witness on degree-$2d$ densities

**Verdict up front.** P2 does **not** inherit fibre balance: it *inverts* it. The
weight $\mathbb E_w[\min(\alpha_w/\alpha,\beta_w/\beta)]$ is replaced by a
quantity that is $\ge 1$ unconditionally and is $2^{\Theta(d)}$ *large* exactly
on the codimension-$d$ subcube pair that killed route 2. Its enemy is a
different family, named in §4.

## 1. The object

Fix a window $W$ once, from the two **densities**, not from any single function.
For $w\in\{\pm1\}^{[N]\setminus W}$ and $A\in\operatorname{supp}\mathbf F$ write
$A_w\subseteq\{\pm1\}^W$ for the trace, $\alpha_w^{(A)}$ its density in the
fibre, and $p_A=\Pr_w[A_w\ne\emptyset]$. The bounded quantity is
$$\kappa_A \;=\; \frac{p_A}{\alpha_A}\;=\;\frac{1}{\mathbb E_w[\alpha_w^{(A)}\mid A_w\ne\emptyset]}\in[1,2^{d}],$$
the reciprocal **conditional** fibre density of $A$ on the fibres it meets. The
family of fibres is *all* of them: surjectivity of the density supports off $W$
is pointwise, not measure-theoretic.

## 2. Why this is not the same loss renamed

$\kappa_A$ never divides one small density by another. It compares $A$ to
itself, conditioned on the fibres where it lives, so no fibre on which $A$ is
absent can dilute it — that is precisely the cancellation that gave
$\mathbb E_w[\min(\cdot,\cdot)]$ its exponential floor. Concretely: on the
codim-$d$ subcube versus complement, $\alpha_w^{(A)}=2^{-d}$ and $p_A=1$, so
$\kappa_A=2^{d}$ and the chain below returns $\delta\ge 1/(8d)$; the old weight
returns $1$ and buys nothing. The two are not monotone in one another.

## 3. Chain (statements only)

1. **Canonical window.** $\mu_{\mathbf F},\mu_{\mathbf G}$ are nonzero of degree
   $\le 2d$, so by S7b each support projects onto every coordinate outside a set
   of size $\le 2d$; put $W=W_F\cup W_G$, $|W|\le 4d$. *Hands 2: one window,
   fixed before any $f$ is drawn, off which both union supports are surjective.*
2. **No fibre is filled.** For every $w$ and every $A\in\operatorname{supp}\mathbf F$,
   $A_w\ne\{\pm1\}^W$ — otherwise $\operatorname{supp}\mu_{\mathbf G}$ misses the
   fibre, contradicting 1. *Hands 3: every met trace is proper and nonempty.*
3. **Dimension-free fibre quantum.** $1_{A_w}$ and its complement are nonzero of
   degree $\le d$, so $\alpha_w^{(A)},1-\alpha_w^{(A)}\ge 2^{-d}$ and
   $\sum_{i\in W}\mathrm{Inf}_i^{(w)}(1_{A_w})\ge \alpha_w^{(A)}(1-\alpha_w^{(A)})\ge 2^{-d-1}$,
   with no dependence on $|W|$ or $N$. *Hands 4: a per-met-fibre influence
   quantum.*
4. **Assembly.** Averaging $\mathrm{Inf}_i(1_A)=\mathbb E_w[\mathrm{Inf}_i^{(w)}(1_{A_w})]$
   over $i\in W$, over $w$, and over $\mathbf F$, and dividing by $\alpha_A$,
   $$\max_{i}\ \mathbb E_{f\sim\mathbf F}[\mathrm{Inf}_i(f)]\ \ge\ \frac{2^{-d-1}}{4d}\,\mathbb E_A[\kappa_A],$$
   and symmetrically for $\mathbf G$. *Hands the rung whenever
   $\mathbb E_A[\kappa_A]\ge 2^{d}/\mathrm{poly}(d)$.*

## 4. Sparse pairs

They are P2's **good** case, not its obstruction. $\kappa_A\approx 2^{d}$ says
the traces sit at the granularity floor $2^{-d}$ on their own fibres, which is
what near-minimal density forces; then step 4 gives $\delta\ge1/\mathrm{poly}(d)$.
P2 is therefore complementary to the surviving payment route, which needs
$\min(\alpha,\beta)\ge1/\mathrm{poly}(d)$. The residual enemy is $\kappa_A=O(1)$:
each $A$ dense inside a $2^{-d}$-fraction of fibres, i.e. a junta on coordinates
*outside* the canonical window, the family collectively covering all fibres.

## 5. Cheap falsifiable check

Compute $W$, $p_A$, $\alpha_A$, $\kappa_A$ on the $d\times d$ grid distributions
and on the address pair with the existing exact enumerators, and compare step
4's output with the certified ceiling $1/(2d)$ and with refuter-2's exhaustive
$d=2$ frontier $1/4$. Any pair where the bound exceeds the pair's true maximum
average influence refutes the chain (error in 1–3); grid $\kappa=O(1)$ instead
confirms §4's enemy is occupied and caps P2 at $2^{-\Theta(d)}$.

### END OF ARTIFACT 0023-prover-5-u0 ###
