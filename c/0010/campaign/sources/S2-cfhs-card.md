# Source card S2 — Coretti, Farshim, Harasser, Southern, *Multi-Source Randomness Extraction and Generation in the Random-Oracle Model*

ePrint 2025/1258; ITC 2025, LIPIcs vol. 343, art. 10, pp. 10:1--10:23. Retrievable at
<https://eprint.iacr.org/2025/1258.pdf> and <https://drops.dagstuhl.de/entities/volume/LIPIcs-volume-343>.

**Checked against the paper, 27 August 2026**, both the ePrint and the published LIPIcs version.
Every transcription below is faithful; four labels and glosses were wrong and are corrected, one
omission is restored, and **one defect in the paper itself** is recorded. Numbering differs between
versions: the ePrint uses per-environment counters (Lemma 3, Lemma 4, Theorem 2, Theorem 3), LIPIcs
one continuous counter (Lemma 3, Lemma 4, Theorem 21, Lemma 22, Theorem 23). Page references here
are **ePrint** unless marked.

## Setting (pp. 9–10)

$\mathrm{Fun}(N^{\ell},M)$; a source $S$ returns $(x,z)\in[N]\times\{0,1\}^{*}$; all parties
are unbounded and have oracle access to $H$. $S$ is $(q,\delta)$-unpredictable if every
predictor making at most $q$ oracle calls, on input the source's own leakage $z$, guesses
$x$ with probability at most $\delta$. The multi-source-extraction game draws
$H\gets_{\$}\mathrm{Fun}(N^{\ell},M)$, runs each $S_i$ to get $(x_i,z_i)$, sets
$y_0\gets_{\$}[M]$ and $y_1\gets H(x)$, and returns whether $D^{H}(y_b,z)$ guesses $b$;
$\mathsf{Adv}^{\mathrm{mse}}=2\Pr[\cdot]-1$. $\mathsf{Adv}^{\mathrm{mse}}_{\mathcal S,\mathcal D}:=2\Pr[\cdot]-1$ verbatim (p. 10).

**Two scoping corrections, 27 August 2026.** The card previously said "with $\ell=2$ this is exactly
the Contract's $\kappa$, up to the factor-of-two convention". The $2p-1$ normalisation is what
*removes* the factor, not what introduces one: $\sup_{\mathcal D}\mathsf{Adv}^{\mathrm{mse}}$
**equals** $\kappa(q)$, with no residual factor of two. And the identification holds at the level of
the *advantage measure only* — the **bounds** are different objects. At $\ell=2$ Theorem 3 gives a
cube root (or fourth, per the defect above) in $q_D/\delta^{2}$ carrying an **additive $N$**, where
the Contract's `thm:main` target is a square root in $\delta$ carrying only $\log N$. Separately,
the paper's unpredictability gives the predictor only $z_i$ where `def:sources` gives it the whole
$\vz$ — formally stronger; Contract `rem:vecz` closes exactly that gap for split sources, and this
card should point at it rather than leave a reader to notice.

## Lemma 3, flat decomposition (p. 9, not p. 8)

*Let $k\in\mathbb R_{>0}$ with $2^{k}\in\mathbb N$. Then every $k$-source $X$ is a convex
combination of flat $k$-sources: $X=\sum p_iX_i$ with $p_i\ge0$, $\sum p_i=1$, each $X_i$
uniform on a subset of size $2^{k}$.* Here a $k$-source satisfies $\Pr[X=x]\le2^{-k}$ for
every $x$, and a flat $k$-source is uniform on a set of size exactly $2^{k}$. Attributed there to reference **[33] in the ePrint** — but to **[34]** in the published LIPIcs
version, where **[33] is Unruh, "Random oracles and auxiliary input", CRYPTO 2007**, a different
paper that is separately load-bearing for this campaign. A reader holding the published version and
following "[33]" lands on the wrong reference. The work cited is **Vadhan, *Pseudorandomness*,
Foundations and Trends in TCS vol. 7, Now Publishers, 2012**; CFHS cite the monograph as a whole
with no lemma pointer.

## Lemma 4, item 3 --- binomial bounds (p. 9)

**There is no "Lemma 4.3" in either version.** The object is **Lemma 4, item 3** of three items in
a lemma titled "Numeric inequalities" (items 1 and 2 are used elsewhere in the paper, so the item
structure is real). Any citation of the form `[CFHS, Lemma 4.3]` is unresolvable and must read
`[CFHS, Lemma 4(3)]`. Corrected 27 August 2026.

*For $k,n\in\mathbb N$ with $0<k\le n$, $(n/k)^{k}\le\binom nk\le(en/k)^{k}$.*

## Theorem 3, MSE (p. 28)

*Let $\ell,M,N,q_D\in\mathbb N$ and $k\in\mathbb R_{>0}$. For every tuple
$S=(S_1,\dots,S_\ell)$ of sources, each $(N^{\ell},2^{-k})$-unpredictable and with unbounded
oracle access, and every distinguisher $D$ making at most $q_D$ oracle calls,*
$$\mathsf{Adv}^{\mathrm{mse}}_{S,D}=O\Bigl(\ell\log M\ \sqrt[\ell+1]{\tfrac{q_D}{2^{k\ell}}\,(\sigma+\ell N)}\Bigr),$$
*where $\sigma\ge\sum_i\sigma_i$ bounds the total leakage length.*

Obtained by compression: Yao's equivalence turns a distinguisher into a next-bit predictor,
which is split according to whether it queries the challenge point, the first case going
through their Theorem 2 (unrecoverability) and the second through an incompressibility
argument; the sources' oracle-dependence is handled by decomposing them into flat sources.

**Two observations recorded against this statement, both verified 27 August 2026.** Its
right-hand side vanishes at $q_D=0$, whereas the query-free extraction advantage is nonzero in
general; it is therefore read here as intended for $q_D\ge1$. **The paper does not itself impose
that restriction**, and its own conventions appear to admit $q_D=0$: Proposition 2 (p. 12) carries
an explicit side condition $q_{\mathcal D}\ge1$, which would be redundant unless $0\in\mathbb N$
here, and Theorem 3 carries no such condition. And the constant hidden in the $O(\cdot)$ is not
extracted anywhere — the proof runs on unspecified $\alpha$, $b$, and bare numerals — so any bound
quoting it is asymptotic.

**A third observation, and it is a defect in the paper.** The statement's radical index is
$\ell+1$; **the final case of its proof delivers $\ell+2$.** Verified from the text layer of both
the ePrint (statement p. 28, proof p. 33) and the published LIPIcs version (statement 10:16, proof
10:20), which are independently typeset and agree. The mechanism is clear: the incompressibility
step's gain is *quadratic* in $\epsilon$, and with $S=2^{k}/\beta$,
$\beta=b\ell\log M/((1-\alpha)\epsilon)$ one gets
$\epsilon^{2}S^{\ell}/(\log M)^{2}=\epsilon^{\ell+2}2^{k\ell}(1-\alpha)^{\ell}/((b\ell)^{\ell}(\log M)^{\ell+2})$,
hence exponent $1/(\ell+2)$ — exactly the paper's own displayed line. By contrast Theorem 2's gain
is only *linear* in $\epsilon$, giving $\epsilon^{\ell+1}$, which is why Theorem 2/21 states
$1/(\ell+1)$ correctly. In the only regime where the bound says anything, $u<1$, one has
$u^{1/(\ell+2)}>u^{1/(\ell+1)}$, so **the stated bound is strictly stronger than the proved one and
is not implied by it.** Nothing in this campaign uses Theorem 3's bound, so this is inert for the
proof chain; it is live for any prose quoting CFHS's rate.

**Not recorded on this card before:** Theorem 3 is the **UBU** corner of the paper's Figure 1 —
unbounded source, *bounded* distinguisher, unbounded predictor, with $q_{\mathcal P}=N^{\ell}$,
enough to read all of $H$. That is why it is compatible with the Contract's unbounded predictors.

## Section 1.4, the decomposition question (pp. 6–7)

The paper states that compression does not transfer to non-monolithic constructions such as
Merkle–Damgård or Sponge, and asks whether CDGS or Unruh decomposition can be run in the
multi-source setting. It rules out the naive route — running CDGS in parallel on $z_1$ and
$z_2$ and fixing the union — with the example $z_1:=\sum_{1\neq x\in[N]}H(x)$,
$z_2:=\sum_{x\in[N]}H(x)$: jointly the pair reveals $H(1)$, while individually neither leaks
anything about any particular point, so parallel decomposition fixes nothing. It conjectures that parallel decomposition is possible under appropriate restrictions and leaves it
open. (Section title is "Future Directions"; pp. 6--7 confirmed, and the example appears symbol for
symbol.)

**Footnote 4 (ePrint footnote 8) was dropped from this card and is restored, because it is
load-bearing:** "We note that this is an attack on directly applying decomposition as a proof
technique. Moreover, $z_1$ and $z_2$ can be made unpredictable by simply appending random bits."
Two things follow. CFHS themselves scope the example as an attack on *the technique*, not an
impossibility for the *statement* — which is precisely the distinction the campaign draws when it
calls the $P\delta$ cost a defect of the route rather than of the statement, so the source paper
corroborates that reading. And as literally written the example specifies only the leakages, never
the points $x_1,x_2$, so it does not by itself exhibit an *unpredictable* pair; the footnote is the
patch.

**One inherited overstatement.** The card said compression "does not transfer" to non-monolithic
constructions; the paper's wording is weaker — "not straightforward to apply" (p. 6). The Contract's
own §1 inherits the same overstatement.

**Worth recording as provenance for the barrier as well as the question:** p. 7 says "In
applications, $P$ cannot be chosen too large, as then the probability of certain bad events (e.g., a
challenge point lying in the set of fixed points) would be too large" — which is, verbatim, the
$P\delta$ obstruction the campaign identifies as its single blocking step. CFHS flag it in advance.
