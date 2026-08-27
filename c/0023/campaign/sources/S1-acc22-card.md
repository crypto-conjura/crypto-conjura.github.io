### SOURCE CARD [S1] ###

id: S1-acc22
citation: Per Austrin, Hao Chung, Kai-Min Chung, Shiuan Fu, Yao-Ting Lin, Mohammad
Mahmoody, *On the Impossibility of Key Agreements from Quantum Random Oracles*,
Cryptology ePrint Archive 2022/218 (CRYPTO 2022, LNCS 13508,
DOI 10.1007/978-3-031-15979-4_6). PDF read: https://eprint.iacr.org/2022/218.pdf
(ePrint page dated 2022-02-25). All items below were read directly from the PDF
pages by the Scout (retrieval status [READ]); page numbers refer to the ePrint PDF.

Emitted by: 0023-scout-1, cycle 1, 2026-08-27.

---

## Item S1.a — The printed conjecture(s)

There are THREE printed formulations. The paper's own equivalences tie them together.

### Conjecture 1.2 (Polynomial Compatibility), p. 5 — informal, group fixed to Z_2, real coefficients

Verbatim:

> **Conjecture 1.2** (Polynomial Compatibility). *There is a function
> $\delta(d) = 1/\mathrm{poly}(d)$, such that the following holds for all
> $d \in \mathbb{N}$. Suppose $F, G$ are distributions over multilinear
> polynomials of degree $d$ with variables $x_1,\dots,x_N \in \{\pm 1\}$ and
> $\ell_2$-norm $1$ and bounded influences
> $\mathrm{Inf}_i(F), \mathrm{Inf}_i(G) \le \delta(d)$ for all $i \in [N]$.
> Then, there exist $f \in \mathrm{supp}(F)$, $g \in \mathrm{supp}(G)$ and
> $\mathbf{x} \in \{\pm 1\}^N$ such that $f(\mathbf{x}) \cdot g(\mathbf{x}) \ne 0$.*

Definitions in force (p. 4, "Some basic notions"): $f = \sum_{S \subseteq [N]}
\alpha_S \prod_{i \in S} x_i$ is a multilinear polynomial over binary variables
$x_i \in \{\pm 1\}$ with **real** coefficients $\alpha_S \in \mathbb{R}$;
$\deg(f) = \max_{\alpha_S \ne 0} |S|$; the $\ell_2$ norm is written
"$\|f\|_2 = \mathbb{E}_{\mathbf{x} \leftarrow \{\pm 1\}^N}[f(\mathbf{x})^2]$"
(as printed, without a square-root sign; the intended normalized-counting-measure
convention is clear from usage elsewhere);
$\mathrm{Inf}_i(f) = \sum_{S \ni i} \alpha_S^2$; and for a distribution $F$,
$\mathrm{Inf}_i(F) = \mathbb{E}_{f \leftarrow F}[\mathrm{Inf}_i(f)]$ is the
**expected** influence. So the influence hypothesis of Conjecture 1.2 is
per-coordinate, ON AVERAGE over the distribution — matching the Contract's
convention 2.

### Conjecture 4.3 (state form), p. 20 — group existentially quantified

Supporting definitions (p. 20):

> **Definition 4.1** ($(\mathcal{Y}, \delta, d, N)$-state). *Let $H$ be a register
> over the Hilbert space $\mathcal{Y}^N$. A quantum state $|\psi\rangle$ over
> registers $W$ and $H$ is a $(\mathcal{Y}, \delta, d, N)$-state if it satisfies
> the following two conditions:*
> - *$d$-**sparsity**: $|\hat{h}^H_{\max}(|\psi\rangle)| \le d$.*
> - *$\delta$-**lightness**: For every $x \in \mathcal{X}$, if we measure the
>   $H_x$ register of $|\psi\rangle$ in the Fourier basis, the probability of
>   getting $\hat{0}$ is at least $1 - \delta$.*

> **Definition 4.2** (Compatibility). *Two quantum states $|\psi\rangle$ and
> $|\phi\rangle$ over registers $W$ and $H$ are compatible if
> $\mathrm{supp}^H(|\psi\rangle) \cap \mathrm{supp}^H(|\phi\rangle) \ne \emptyset$,
> i.e., if their oracle supports in the computational basis (as defined in
> Definition 2.3) have non-empty intersection.*

Verbatim:

> **Conjecture 4.3.** *There exists a finite Abelian group $\mathcal{Y}$ and
> $\delta = 1/\mathrm{poly}(d)$ such that for any $d, N \in \mathbb{N}$, it holds
> that any two $(\mathcal{Y}, \delta(d), d, N)$-states $|\psi\rangle$ and
> $|\phi\rangle$ are compatible.*

### Conjecture 5.5 (polynomial form over a general group), p. 25 — REAL-valued functions

Fourier conventions in force (§5.1, pp. 24–25): $\mathcal{Y}$ an Abelian group of
order $|\mathcal{Y}|$, dual $\hat{\mathcal{Y}}$ with identity $\hat 0$; any
$f : \mathcal{Y}^N \to \mathbb{C}$ has
$f(\mathbf{x}) = \sum_{\chi \in \hat{\mathcal{Y}}^N} \hat f(\chi) \prod_{i=1}^N
\chi_i(\mathbf{x}_i)$; $\deg(\chi) = |\{i \mid \chi_i \ne \hat 0\}|$,
$\deg(f) = \max\{\deg(\chi) \mid \hat f(\chi) \ne 0\}$,
$\mathrm{Inf}_i(f) = \sum_{\chi : \chi_i \ne \hat 0} |\hat f(\chi)|^2$.

Verbatim:

> **Conjecture 5.5.** *There exists a finite Abelian group $\mathcal{Y}$ and a
> function $\delta(d) = 1/\mathrm{poly}(\cdot)$ such that the following holds for
> all $d$. Let $F$ and $G$ be two distributions of functions from $\mathcal{Y}^N$
> to $\mathbb{R}$ such that the following holds for all $f \in \mathrm{supp}(F)$
> and $g \in \mathrm{supp}(G)$.*
> - ***Unit $\ell_2$ norm**: $f$ and $g$ have $\ell_2$-norm $1$.*
> - ***$d$-degrees**: $\deg(f) \le d$ and $\deg(g) \le d$.*
> - ***$\delta$-influences on average**: For all $i \in [N]$, we have
>   $\mathbb{E}_{f \leftarrow F}[\mathrm{Inf}_i(f)] \le \delta$ and
>   $\mathbb{E}_{g \leftarrow G}[\mathrm{Inf}_i(g)] \le \delta$, where
>   $\delta = \delta(d)$.*
>
> *Then, there is an $f \in \mathrm{supp}(F)$, $g \in \mathrm{supp}(G)$, and
> $\mathbf{x} \in \mathcal{Y}^N$ such that
> $f(\mathbf{x}) \cdot g(\mathbf{x}) \ne 0$.*

Preceding sentence (p. 25): "Notice that, in the following formulation, we focus
on the distributions of functions whose range is $\mathbb{R}$ instead of
$\mathbb{C}$. Later on, in Theorem 5.6, we will show that it suffices to consider
real functions."

> **Theorem 5.6.** *Conjecture 5.5 is true if and only if Conjecture 4.3 is true.*

Proof of Theorem 5.6 is Appendix A (p. 40), "Reduction from Complex to Real": the
complex case reduces to the real case at the cost of a factor 2 in $\delta$
(the constructed real distributions $G_1, G_2$ satisfy
$\mathbb{E}[\mathrm{Inf}_i] \le 2\delta$), which $1/\mathrm{poly}$ absorbs. The
bridge Observation 5.4 (p. 25): two states are compatible iff their state
polynomial distributions have $f \in \mathrm{supp}(F_\psi)$,
$g \in \mathrm{supp}(F_\phi)$, $\mathbf{x} \in \mathcal{Y}^N$ with
$f(\mathbf{x}) g(\mathbf{x}) \ne 0$.

### Hypotheses itemised (Conjecture 5.5 / 4.3, the canonical forms)

1. $\mathcal{Y}$: finite Abelian, EXISTENTIALLY quantified (chosen with $\delta$,
   before $d, N, F, G$). Conjecture 1.2 is the special case with
   $\mathcal{Y} = \mathbb{Z}_2$ hard-wired.
2. $\delta$ inverse-polynomial in $d$, independent of $N$.
3. Both distributions: unit $\ell_2$ norm and degree $\le d$ pointwise on the
   support; influences bounded per-coordinate ON AVERAGE.
4. Range: $\mathbb{R}$ in printed 5.5; $\mathbb{C}$-version equivalent by
   Theorem 5.6 / Appendix A (factor 2 in $\delta$).
5. Finite support is NOT stated explicitly anywhere ("distributions of
   functions", $\mathrm{supp}$ used without qualification). In the source
   application, distributions arise by measuring a finite register
   (Definition 5.3, p. 25), hence are finitely supported. The Contract's
   convention 1 is an added (consistent, benign) reading, not a printed one.

---

## Item S1.b — The theorem proved (exponentially small influence)

Verbatim (p. 20):

> **Theorem 4.4.** *For all groups $\mathcal{Y}$, $d, N \in \mathbb{N}$, and
> $\delta < |\mathcal{Y}|^{-d}/d$, it holds that any two
> $(\mathcal{Y}, \delta, d, N)$-states $|\psi\rangle$ and $|\phi\rangle$ are
> compatible.*

- Threshold: $\delta < |\mathcal{Y}|^{-d}/d$, STRICT inequality. Confirms the
  Contract's K1 up to strict-vs-weak (repo note said "$\delta \le
  |\mathcal{Y}|^{-d}/d$"; printed is $<$).
- It is proved for ALL finite Abelian groups simultaneously (universal, not
  per-group-wanted).
- Proof (§5.2, p. 26) is via the polynomial formulation, and the proof uses
  strictly less than the conjecture's hypotheses. Verbatim (p. 26): "the theorem
  holds without any influence condition on $F$, and without any degree
  restriction on $G$. I.e., we only use that there is an $f \in \mathrm{supp}(F)$
  of degree $\le d$, and that
  $\mathbb{E}_{g \leftarrow G}[\mathrm{Inf}_i(g)] \le \delta$ for all $i \in [N]$."
- Proof mechanism (p. 26, for the barrier analysis): pick $f \in \mathrm{supp}(F)$
  and a maximal-degree character $\chi^*$ of $f$; WLOG its $\le d$ live
  coordinates are $1..d$. For any $g$, decompose
  $g(\mathbf{x}) = \sum_{\chi \in \hat{\mathcal{Y}}^d} g_\chi(\mathbf{x}_{>d})
  \chi(\mathbf{x}_{\le d})$. Two displayed estimates:
  $\sum_{\chi \ne \hat{\mathbf{0}}} \mathbb{E}_{\mathbf{x}_{>d}}[|g_\chi|^2]
  \le \sum_{i=1}^d \mathrm{Inf}_i(g)$ and
  $\mathbb{E}_{\mathbf{x}_{>d}}[|g_{\hat{\mathbf{0}}}|^2] \ge \|g\|_2^2 -
  \sum_{i=1}^d \mathrm{Inf}_i(g)$, hence
  $\mathbb{E}_{\mathbf{x}_{>d}}\big[|g_{\hat{\mathbf{0}}}|^2 -
  (|\mathcal{Y}|^d - 1)\sum_{\chi \ne \hat{\mathbf{0}}} |g_\chi|^2\big]
  \ge \|g\|_2^2 - |\mathcal{Y}|^d \sum_{i=1}^d \mathrm{Inf}_i(g)$,
  which is $> 0$ when $\delta < |\mathcal{Y}|^{-d}/d$; then averaging over
  $g \leftarrow G$, Cauchy–Schwarz across the $|\mathcal{Y}|^d - 1$ nonconstant
  blocks gives an $\mathbf{x}_{>d}$ with
  $|g_{\hat{\mathbf{0}}}(\mathbf{x}_{>d})| > \sum_{\chi \ne \hat{\mathbf{0}}}
  |g_\chi(\mathbf{x}_{>d})|$; the restriction of $f$ to that $\mathbf{x}_{>d}$
  is non-constant (contains $\chi^*$), so some $\mathbf{x}_{\le d}$ has
  $f \ne 0$, and $|g| \ge |g_{\hat{\mathbf{0}}}| - \sum |g_\chi| > 0$ at every
  such point. The exponential loss $|\mathcal{Y}|^d$ enters exactly where the
  constant block must dominate ALL $|\mathcal{Y}|^d - 1$ nonconstant blocks at
  once (Cauchy–Schwarz over the blocks).

Downstream use (p. 21): Theorem 4.6 (exponential-query attacks,
$|\mathcal{Y}|^d d^2/\lambda$ classical queries) = Theorem 4.4 + Lemma 4.7 with
$\varepsilon/\lambda = \delta = |\mathcal{Y}|^{-d}/d$.

Related printed machinery: Lemma 4.7 (p. 21): if any two
$(\mathcal{Y}, \delta = \varepsilon/\lambda, d, N)$-states are compatible then
$d$-query key agreement with range $\mathcal{Y}$ is $(1-\lambda,
d/\varepsilon)$-classically broken. Lemma 4.8 (p. 21, proof §8.2): group
equivalence — poly-query breakability for ONE group $\mathcal{Y}$ transfers to
all finite Abelian groups $\mathcal{Y}'$ with
$m = \lceil \log_{|\mathcal{Y}|}(d'^3 |\mathcal{Y}'| / 4\delta^2) \rceil$
overhead. (This is a transfer at the ATTACK level, not a printed equivalence of
the conjecture across groups.)

---

## Item S1.c — The counterexamples (Appendix B, "Example Functions", pp. 41–42)

Normalization used there (p. 41): relative influence
$\mathrm{RelInf}_i(f) := \mathrm{Inf}_i(f) / \mathbb{E}[|f|^2]$ (so unit-norm
rescaling is built in). $\mathsf{AND}_n : \{-1,1\}^n \to \{0,1\}$ is $1$ iff all
inputs are $-1$; $\mathbb{E}[\mathsf{AND}_n(x)^2] = 2^{-n}$,
$\mathrm{Inf}_i(\mathsf{AND}_n) = 2^{-n}/2$, so
$\mathrm{RelInf}_i(\mathsf{AND}_n) = 1/2$.

> **Definition B.1.** *For a set of $n \times m$ variables
> $\vec{x} = \{x_{ij}\}_{i \in [n], j \in [m]}$, we define the functions*
> $$\mathrm{NegRow}(\vec{x}) = \sum_{i=1}^n \mathsf{AND}_m(x_{i,*}) \qquad
>   \mathrm{PosCol}(\vec{x}) = \sum_{j=1}^m \mathsf{AND}_n(-x_{*,j}),$$
> *where $x_{i,*}$ denotes the $i$'th row ... and $x_{*,j}$ the $j$'th column.*

> **Claim B.2.** *The functions $\mathrm{NegRow}$ and $\mathrm{PosCol}$ satisfy:*
> 1. *$\mathrm{RelInf}_{ij}(\mathrm{NegRow}) < \frac{1}{2n}$ for all $i, j$.*
> 2. *$\mathrm{RelInf}_{ij}(\mathrm{PosCol}) < \frac{1}{2m}$ for all $i, j$.*
> 3. *$\mathrm{NegRow}(\vec{x})$ is non-zero if and only if there exists a row of
>    $\vec{x}$ which is all $-1$. As a consequence, $\mathrm{NegRow}(\vec x) = 0$
>    on exactly a $(1 - 2^{-m})^n$ fraction of all $\vec{x}$.*
> 4. *$\mathrm{PosCol}(\vec{x})$ is non-zero if and only if there exists a column
>    of $\vec{x}$ which is all $+1$. As a consequence, [printed "NegRow", clearly
>    meaning PosCol] $= 0$ on exactly a $(1 - 2^{-n})^m$ fraction of all $\vec x$.*

(Influence computation shown: $\mathrm{Inf}_{ij}(\mathrm{NegRow}) = 2^{-m}/2$ for
all $i,j$ and $\mathbb{E}[\mathrm{NegRow}^2] = n 2^{-m} + n(n-1) 2^{-2m} > n2^{-m}$.)

> **Claim B.3** (Example 1: best possible relation between degrees and
> influences). *For any $d$ there exist non-zero degree $d$ polynomials $f$ and
> $g$, having all relative influences bounded by $\frac{1}{2d}$, and satisfying
> $f(x) \cdot g(x) = 0$ for all $x$.*
> *Proof. Let $n = m = d$ and take the polynomials $\mathrm{NegRow}$ and
> $\mathrm{PosCol}$.* $\square$

Header sentence of Example 1 (p. 41): "This first example shows that the best
relation between degree and influence that can be hoped for is
$\max \mathrm{RelInf} \le \frac{1}{2d}$." And the intro (p. 5): "we give an
example showing that relation between $\delta$ and the degree $d$ must satisfy
$\delta < \frac{1}{2d}$, otherwise the conjecture is false."

Notes for downstream (what B.3 does and does not give):
- It is a SINGLETON-support counterexample (two fixed functions, i.e., point
  distributions), so average influence = pointwise influence; it violates even
  the max-influence-weakened conjecture at $\delta = 1/(2d)$.
- Incompatibility mechanism: an all-$(-1)$ row and an all-$(+1)$ column would
  have to agree at their crossing entry, so the supports are disjoint.
- GROUP DEPENDENCE: printed for $\mathcal{Y} = \mathbb{Z}_2$ (Boolean cube) ONLY.
  No counterexample for any other group is printed anywhere in the paper. Since
  the conjecture quantifies $\mathcal{Y}$ existentially, Claim B.3 pins
  $\delta(d) < 1/(2d)$ for $\mathbb{Z}_2$ but NOT for the conjecture as a whole;
  the Contract's K2 consequence "effectively $c_2 \ge 1$" is, as printed,
  established only for the $\mathbb{Z}_2$ instantiation. (The construction looks
  generalizable — indicators of "row all $= a$" vs "column all $= b$" for
  $a \ne b \in \mathcal{Y}$ — but that is not in the paper.)

Two further printed necessity examples (p. 42):
> **Claim B.4.** *For any $d \ge 1$ there exists non-zero functions $f$ and $g$
> such that: 1. $f$ has degree $d$; 2. $\max\mathrm{RelInf}(f)$ and
> $\max\mathrm{RelInf}(g)$ are both $O(2^{-d})$; 3. $f \cdot g = 0$.*
> (Proof: $n = 2^d$, $m = d$, $f = \mathrm{NegRow}$, $g$ = indicator of
> $\mathrm{NegRow} = 0$; $\max\mathrm{RelInf}(g) \le 4 \cdot 2^{-m} = 4\cdot2^{-d}$.)
> — so BOTH functions need the degree bound: exponentially small influence alone
> (with one unbounded degree) does not save the conjecture.

> **Claim B.5.** *For any $d \ge 1$ there exists functions $f$ and $g$ of
> $\ell_2$ norm 1 such that: 1. $f$ and $g$ have degree $d$; 2.
> $\max\mathrm{RelInf}(f)$ is $2^{-\Omega(d)}$; 3. $f \cdot g = 0$.*
> (Proof: $g = \mathsf{AND}_d(x)$, $f = 1 - \mathsf{AND}_d(x)$.)
> — so BOTH functions need the influence bound.

---

## Item S1.d — Context printed in the paper (for the barrier file)

- Comparison with Aaronson–Ambainis (p. 11, §1.3, verbatim in part): "our
  conjecture and the AA conjecture do not seem to be directly comparable, and it
  would be interesting to prove implications in either direction between them.
  One interesting similarity is that both conjectures hold, when we assume
  *exponentially* small influences [DFKO06]." Also: AA applies to the
  no-communication imperfect-completeness setting; PCC is tailored to perfect
  completeness with communication; "the 'intersection' of these, i.e., the case
  of no communication and perfect completeness, can be proved without a
  conjecture [OSSS05]."
- Theorem 4.5 (p. 20): if Conjecture 4.3 holds, key agreement with range
  $\mathcal{Y}$ is broken with $\mathrm{poly}(d, \log|\mathcal{Y}|)$ classical
  queries (probability $\ge 0.8$).
- Theorem 1.4 / Section 7: if the Simulation Conjecture is FALSE, a classically
  secure QCCC key agreement with imperfect completeness EXISTS in the QROM — so
  unconditional classical attacks in the imperfect-completeness setting require
  resolving the Simulation Conjecture; this does not constrain proofs of PCC
  itself.

## What this source does NOT say

- It does not prove any influence regime beyond $\delta < |\mathcal{Y}|^{-d}/d$.
- It does not print a counterexample for any group other than $\mathbb{Z}_2$.
- It does not state that distributions are finitely supported.
- It does not prove or claim any implication between PCC and the AA conjecture,
  in either direction.
- Lemma 4.8 transfers attacks across groups, NOT the conjecture/counterexamples
  across groups.

## Where we use it

Pins the Contract's statement provenance (Conjectures 1.2/4.3/5.5 + Theorem 5.6),
K1 (Theorem 4.4, threshold $\delta < |\mathcal{Y}|^{-d}/d$, all groups), and K2
(Claim B.3, $\mathbb{Z}_2$ only, $1/(2d)$, singleton supports). The §5.2 proof
mechanism is the named technique whose failure mode at inverse-polynomial
$\delta$ the Strategist must diagnose.

### END OF SOURCE CARD [S1] ###
