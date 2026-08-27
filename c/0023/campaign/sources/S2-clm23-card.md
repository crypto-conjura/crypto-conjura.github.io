### SOURCE CARD [S2] ###

id: S2-clm23
citation: Kai-Min Chung, Yao-Ting Lin, Mohammad Mahmoody, *Black-Box Separations
for Non-Interactive Commitments in a Quantum World*, Cryptology ePrint Archive
2023/570. PDF read: https://eprint.iacr.org/2023/570.pdf. All items below were
read directly from the PDF pages by the Scout (retrieval status [READ]); page
numbers refer to the ePrint PDF (§2.2 "Polynomial Compatibility Conjecture" is
pp. 14–16, §2.3 "The Donoho–Stark Uncertainty Principle" pp. 16–17, consumption
in §4 pp. 22–26).

Emitted by: 0023-scout-1, cycle 1, 2026-08-27.

---

## Item S2.a — The conjecture as printed here (the Contract's verbatim source)

Verbatim (p. 15):

> **Conjecture 2.8** (Polynomial Compatibility). *There exists a finite abelian
> group $\mathcal{Y}$ and a function $\delta(d) = 1/\mathrm{poly}(d)$ such that
> the following holds for all $d, N$. Let $\mathbf{F}$ and $\mathbf{G}$ be two
> distributions of functions from $\mathcal{Y}^N$ to $\mathbb{C}$*[^fn8] *such
> that the following holds for all $f \in \mathrm{supp}(\mathbf{F})$ and
> $g \in \mathrm{supp}(\mathbf{G})$.*
> - ***Unit $\ell_2$ norm**: $f$ and $g$ have $\ell_2$-norm 1.*
> - ***$d$-degrees**: $\deg(f) \le d$ and $\deg(g) \le d$.*
> - ***$\delta$-influences on average**: For all $i \in [N]$, we have
>   $\mathbb{E}_{f \leftarrow \mathbf{F}}[\mathrm{Inf}_i(f)] \le \delta$ and
>   $\mathbb{E}_{g \leftarrow \mathbf{G}}[\mathrm{Inf}_i(g)] \le \delta$, where
>   $\delta = \delta(d)$.*
>
> *Then, there is an $f \in \mathrm{supp}(\mathbf{F})$,
> $g \in \mathrm{supp}(\mathbf{G})$, and $\mathbf{x} \in \mathcal{Y}^N$ such that
> $f(\mathbf{x}) \cdot g(\mathbf{x}) \ne 0$.*

[^fn8]: Footnote 8 (p. 15), verbatim: "As shown in [ACC+22], regardless of the
image being $\mathbb{R}$ or $\mathbb{C}$, the conjectures are equivalent up to a
constant factor in $\delta$. For convenience, we use the version with
$\mathbb{C}$."

Fourier conventions (p. 15): $\|f\|_2 :=
\sqrt{\mathbb{E}_{\mathbf{x} \leftarrow \mathcal{Y}^N} |f(\mathbf{x})|^2}$
(square root printed here, unlike ACC22 p. 4);
$\mathrm{Inf}_i(f) = \sum_{\chi : \chi_i \ne \hat 0} |\hat f(\chi)|^2$; degree of
$\chi$ = number of non-identity components.

PROVENANCE NOTE: the Contract's verbatim statement (`c/0023/latex/main.tex`,
Conjecture `conj:main`) matches Conjecture 2.8 here ($\mathbb{C}$-valued), NOT
the printed ACC22 Conjecture 5.5 ($\mathbb{R}$-valued); the two are equivalent by
ACC22 Theorem 5.6 / Appendix A up to a constant factor in $\delta$ (footnote 8
above). Finite support is not stated in either paper; in this paper every
distribution to which the conjecture is applied is a state polynomial
distribution (Definition 2.11), which is finitely supported by construction
(finitely many measurement outcomes $w$).

---

## Item S2.b — The quantum-state formulation and the conversion lemma

> **Definition 2.9** ($(\mathcal{Y}, \delta, d, N)$-state), p. 15. *Let $H$ be a
> register over the Hilbert space $\mathbb{C}^{\mathcal{Y}^\mathcal{X}}$, where
> $|\mathcal{X}| = N$. A quantum state $|\psi\rangle$ over registers $W$ and $H$
> is a $(\mathcal{Y}, \delta, d, N)$-state if it satisfies the following two
> conditions:*
> - *$d$-**sparsity**: $|\hat h^H_{\max}(|\psi\rangle)| \le d$. In other words,
>   for any measurement of the registers $H$ in the Fourier basis, the oracle
>   support in the Fourier basis (as defined in Definition 2.6) is at most $d$
>   (note that this is regardless of the basis in which we measure the register
>   $W$).*
> - *$\delta$-**lightness**: For every $x \in \mathcal{X}$, it holds that
>   $w(x) \le \delta$.*
>
> (Here $w(x) := \|\Pi_x |\phi\rangle\|^2$ with
> $\Pi_x := \sum_{\hat y \in \hat{\mathcal{Y}} \setminus \{\hat 0\}}
> |\hat y\rangle\langle\hat y|_{H_x}$ — Definition 2.7, "quantum
> $\varepsilon$-heavy queries", credited to [ACC+22].)

> **Definition 2.10** (State polynomial), p. 15. *For a (normalized) quantum
> state $|\psi\rangle$ over the register $H$, the state polynomial of
> $|\psi\rangle$ is the function $f_\psi : \mathcal{Y}^N \to \mathbb{C}$ defined
> by* $f_\psi(h) = |\mathcal{Y}|^{N/2} \cdot \langle \psi | h \rangle =
> \sum_{\chi \in \hat{\mathcal{Y}}^N} \langle \psi | \chi \rangle
> \prod_{i=1}^N \chi_i(h_i)$. *Note that $\|f_\psi\|_2 = 1$.*

> **Definition 2.11** (State polynomial distribution), p. 16. *For a
> (normalized) quantum state $|\psi\rangle$ over registers $W, H$, the state
> polynomial distribution of $|\psi\rangle$ is the distribution
> $\mathbf{F}_\psi$ over (normalized) functions $f$ which is sampled by
> measuring $W$ in the computational basis and then taking the (normalized)
> state polynomial corresponding to the residual collapsed state over the
> register $H$. Explicitly, if $|\psi\rangle_{WH} = \sum_{w,\hat h}
> \alpha_{w\hat h} |w\rangle_W |\hat h\rangle_H$, then the support set of
> $\mathbf{F}_\psi$ consists of the state polynomial $f_{\Psi_w}$ of the
> normalized state $|\psi_w\rangle := \sum_{\hat h} \alpha_{w\hat h}
> |\hat h\rangle_H / \|\sum_{\hat h} \alpha_{w\hat h} |\hat h\rangle_H\|$ for
> each $w$. The probability of each $f_{\Psi_w}$ is defined to be
> $\|\sum_{\hat h} \alpha_{w\hat h} |\hat h\rangle_H\|^2$.*

The conversion lemma, verbatim (p. 16):

> **Lemma 2.12.** *Let $\mathbf{F}_\psi$ be the state polynomial distribution of
> an arbitrary $(\mathcal{Y}, \delta, d, N)$-state $|\psi\rangle$. Then the
> following holds.*
> 1. ***Unit $\ell_2$ norm**: $f$ has $\ell_2$-norm 1 for every
>    $f : \mathcal{Y}^N \to \mathbb{C}$ in the support set of $\mathbf{F}_\psi$.*
> 2. ***$d$-degrees**: $\deg(f) \le d$ for every $f : \mathcal{Y}^N \to
>    \mathbb{C}$ in the support set of $\mathbf{F}_\psi$.*
> 3. ***$\delta$-influences on average**: For all $i \in [N]$, we have
>    $\mathbb{E}_{f \leftarrow \mathbf{F}_\psi}[\mathrm{Inf}_i(f)] \le \delta$.*

Note the direction: states $\Rightarrow$ polynomial distributions. Together with
compatibility $\Leftrightarrow$ common non-vanishing point (ACC22
Observation 5.4), this makes the polynomial conjecture (2.8) imply the state
conjecture; ACC22 Theorem 5.6 gives full equivalence. The average (not max)
influence in item 3 is forced because different measurement outcomes $w$ carry
different residual states — only the AVERAGE heaviness over $w$ is controlled by
$\delta$-lightness of $|\psi\rangle$. This is exactly why the Contract forbids
strengthening the hypothesis to max-over-support influence.

---

## Item S2.c — Which regime the application consumes

- Theorem 4.1 (p. 23): "Assuming Conjecture 2.8, there is no quantum black-box
  construction of non-interactive commitments in the CCQD model from one-way
  functions." Simplification stated below it (p. 23): "we first assume the
  abelian group associated with the random oracle to be $\mathbb{Z}_2^\kappa$
  and Conjecture 2.8 holds for $\mathbb{Z}_2$. For the general case in which
  Conjecture 2.8 holds for some abelian group $\mathcal{Y}_\circ$, we instead
  pick the OWFs ... as $f : \mathcal{Y}_\circ^\kappa \mapsto
  \mathcal{Y}_\circ^\kappa$."
- Construction 4.5 (p. 24): the cheating receiver runs the ACC22 heavy-query
  learner (Lemma 4.3) with parameter $\varepsilon = \delta(d\kappa)/10$ "where
  $\delta(\cdot)$ is the function defined in Conjecture 2.8 for $\mathcal{Y} =
  \mathbb{Z}_2$" (consistency check, p. 25: "By our choice of $\varepsilon$, we
  have $3\varepsilon \le \delta(d\kappa)$"). Attack query count
  $1.01 \kappa^2 d / \varepsilon = \mathrm{poly}(d, \kappa)$ — polynomial ONLY
  because $\delta$ is inverse-polynomial. The purified views are shown to be
  $(\mathbb{Z}_2, \delta(d\kappa), d\kappa, N')$-states (p. 25), converted by
  Lemma 2.12, and Conjecture 2.8 is applied at effective degree $d\kappa$.
  CONCLUSION: CLM23 needs the conjecture exactly in the inverse-polynomial
  regime $\delta(d) = 1/\mathrm{poly}(d)$; ACC22's proven exponential regime
  (Theorem 4.4) yields only exponential-query attacks and cannot substitute.

---

## Item S2.d — The uncertainty-principle ingredient (proof-surface datum)

> **Lemma 2.13** (Theorem 3.1 in [WW21], as cited there), p. 16. *Let
> $\mathcal{Y}$ be a finite abelian group. If $f : \mathcal{Y} \to \mathbb{C}$
> is a non-zero function and $\hat f : \hat{\mathcal{Y}} \to \mathbb{C}$ denotes
> its Fourier transform, then*
> $|\mathrm{supp}(f)| \cdot |\mathrm{supp}(\hat f)| \ge |\mathcal{Y}|$.
> (Donoho–Stark support-size uncertainty principle.)

> **Corollary 2.14**, p. 16. *Given $f_0, f_1 : \mathcal{Y}^{\mathcal{X}} \to
> \mathbb{C}$ such that $\deg(f_0), \deg(f_1) \le d$, we have*
> $$|\mathrm{supp}(f_0) \cap \mathrm{supp}(f_1)| \ge
>   \frac{|\mathcal{Y}|^{|\mathcal{X}|}}{O(d |\mathcal{X}|^{2d}
>   |\mathcal{Y}|^{2d})}.$$
> Proof sets $f := f_0 \cdot f_1$ (degree $\le 2d$, Fourier support $\le
> (2d+1)(|\mathcal{X}||\mathcal{Y}|)^{2d}$) and applies Lemma 2.13 to $f$.

CAUTION (Scout's reading, load-bearing for any uncertainty-principle plan):
Lemma 2.13 requires $f \ne 0$, so Corollary 2.14 as used implicitly requires
$f_0 \cdot f_1 \not\equiv 0$; without that hypothesis the corollary is FALSE
(ACC22's NegRow/PosCol are degree-$d$ with $f_0 f_1 \equiv 0$ and empty support
intersection). The paper uses it correctly: Construction 4.6 step 2 (p. 25)
first "Find[s] $f_0 \in \mathrm{supp}(\mathbf{F}_0)$, $f_1 \in
\mathrm{supp}(\mathbf{F}_1)$ such that $f_0 \cdot f_1$ is not constant zero" —
and the EXISTENCE of that pair is exactly what Conjecture 2.8 supplies (p. 26:
"Assuming Conjecture 2.8 holds for $\mathcal{Y} = \mathbb{Z}_2$, there must
exist $f_0 \in \mathrm{supp}(\mathbf{F}_0)$ and $f_1 \in
\mathrm{supp}(\mathbf{F}_1)$ such that $f_0 \cdot f_1 \not\equiv 0$"). So in
this pipeline, Donoho–Stark AMPLIFIES a common non-zero point into MANY, but
cannot produce the first one. Any plan hoping to prove PCC from Donoho–Stark
alone must first defeat exactly this gap.

## What this source does NOT say

- It proves NO regime of the conjecture (no new threshold, no counterexample);
  it consumes the conjecture as an unproven hypothesis.
- Lemma 2.12 converts states to polynomial distributions; it is one direction
  only and adds no strength to the conjecture.
- Corollary 2.14 does NOT say two low-degree functions always have intersecting
  supports (see caution above).

## Where we use it

Pins the Contract's K3: the $(\mathcal{Y}, \delta, d, N)$-state formulation
(Definition 2.9), the conversion lemma (Lemma 2.12), the exact consumption
regime (inverse-polynomial, at effective degree $d\kappa$, group
$\mathbb{Z}_2$-first with generic-group fallback), and the Donoho–Stark
amplification with its implicit non-vanishing hypothesis.

### END OF SOURCE CARD [S2] ###
