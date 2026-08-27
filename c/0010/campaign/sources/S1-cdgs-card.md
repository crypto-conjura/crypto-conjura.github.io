# Source card S1 — Coretti, Dodis, Guo, Steinberger, *Random Oracles and Non-Uniformity*

ePrint 2017/937 (version dated 8 August 2022); EUROCRYPT 2018 pp. 227--258. Retrievable at
<https://eprint.iacr.org/2017/937.pdf>; the title-page date is confirmed against that file.

**Checked against the paper, 27 August 2026** — the first time any card in this campaign has been.
Full text reached including Appendix A. **No mathematical defect found.** Every claim below is
verified against the source; page numbers were wrong and are corrected; four items were missing and
are added. The EUROCRYPT proceedings version was *not* reached (paywall) and cannot substitute:
the paper's own bibliography entry [15] marks the ePrint as the full version, and a 32-page
proceedings version cannot contain the p. 40 appendix on which everything below turns.

## Definition 1 (p. 10, verbatim in substance)

An $(N,M)$-source is a random variable $X$ with range $[M]^{N}$. A source is called

- $(1-\delta)$-dense if for every subset $I\subseteq[N]$, $H_\infty(X_I)\ge(1-\delta)\cdot|I|\cdot\log M$;
- $(P,1-\delta)$-dense if it is fixed on at most $P$ coordinates and is $(1-\delta)$-dense on the rest;
- $P$-bit-fixing if it is fixed on at most $P$ coordinates and uniform on the rest.

**The "at most" is verbatim, p. 10, for both notions** — verified 27 August 2026, and it matters:
`split-decomp-kappa-4`'s Theorem H turns on it. It is load-bearing *in the paper itself*, twice.
The $\gamma$-closeness step (p. 41) replaces $Y_{\mathsf{final}}$ by the uniform distribution and
calls the result a combination of $(P',1-\delta)$-dense sources; uniform fixes **zero** coordinates,
so only "at most" makes that legal, and Claim 2 is false under an "exactly $P$" reading. And p. 12
says "the sources $Y'$ are fixed on **at most** $P$ coordinates, as desired". One formal wrinkle
inherited here: $P'=(S_z+\log1/\gamma)/(\delta\log M)$ is a *real number* while Definition 1's $P$
is used as an integer, so "fixed on at most $P'$ coordinates" is the only reading that parses; if
the campaign ever needs $|I_j|\le\lfloor P'\rfloor$ that is an inference, not a quotation.

## Claim 2 (stated p. 11; restated and proved in Appendix A, pp. 40--41)

*Let $X$ be uniform over $[M]^{N}$, $Z:=f(X)$ for arbitrary $f:[M]^N\to\{0,1\}^S$, $X_z$ the
law of $X$ conditioned on $f(X)=z$, and $S_z:=N\log M-H_\infty(X_z)$. For every $\delta>0$,
$X_z$ is $\gamma$-close to a convex combination of finitely many $(P',1-\delta)$-dense
sources, for $P'=(S_z+\log 1/\gamma)/(\delta\cdot\log M)$.*

**What the proof establishes, beyond the statement.** The proof takes $Y:=X_z$, picks the
largest $I$ admitting $y_I$ with $\Pr[Y_I=y_I]>2^{-(1-\delta)|I|\log M}$, splits off
$Y':=Y\mid Y_I=y_I$, and recurses on $Y\mid Y_I\neq y_I$ while
$\Pr[X\in\mathrm{supp}(Y)]>\gamma$. Three consequences are used in this campaign and are
visible in that argument:

1. **Only the min-entropy deficiency is used.** Claim 25 (density of $Y'_{\bar I}$) uses only
   maximality of $I$; Claim 26 ($|I|\le S/(\delta\log M)$) uses only $H_\infty(Y)\ge N\log M-S$;
   the recursion's invariant $H_\infty(Y)\ge N\log M-(S+\log1/\gamma)$ uses only
   $\Pr[Y=y]=\Pr[X=y\mid X\in\mathrm{supp}(Y)]$. Nowhere is it used that $X_z$ is a
   conditioning of a uniform variable by a deterministic function. The claim therefore holds
   for any distribution on $[M]^N$ of min-entropy deficiency $S_z$.
2. **The components have pairwise disjoint supports**, since each step removes
   $\mathrm{supp}(Y')$ from the current support before recursing. Hence the index of the
   component containing a sampled $x$ is a deterministic function of $x$.
3. **Fixed values are values the sample takes**: the component fixes $I$ to $y_I$ and is
   supported on $\{x:x_I=y_I\}$.
4. **The decomposition is available in exact form, with a bounded residue.** The proof gives
   $X=\sum_j\lambda_jY'_j+\lambda_{\mathrm{fin}}Y_{\mathsf{final}}$ where each $\lambda_jY'_j$ is the
   restriction of $X$ to $\mathrm{supp}\,Y'_j$, and the loop condition
   $\Pr[X\in\mathrm{supp}(Y)]>\gamma$ gives $\lambda_{\mathrm{fin}}\le\gamma$. This is what r3's
   Lemma P actually uses, and it is *not* Claim 2's stated $\gamma$-closeness. Added 27 August
   2026: the card previously listed three consequences while the chain used four.

**Warning, and it is a trap.** Consequence 2 (disjoint supports) holds for the **exact**
decomposition above. It **fails** for the $\gamma$-close object Claim 2 asserts, because the
paper's realisation of $\gamma$-closeness replaces $Y_{\mathsf{final}}$ by the *uniform*
distribution (p. 41), whose support is all of $[M]^N$. r3's Lemma P is safe because it uses the
exact form. Anyone "simplifying" Lemma P to quote Claim 2 literally would silently lose
consequence 2, and with it the deterministic-index property that makes $Y_{f,\zeta}$ well defined
and `lem:hit` applicable.

**A fillable hole in the source, recorded because no artifact records it.** Claim 26 as printed
bounds $|I|\le S/(\delta\log M)$ — with $S$, **not** $S+\log\gamma^{-1}$. The version r3's
Lemma P needs, at every recursion step, appears only in **footnote 15 on p. 41**: "The bound on
$|I|$ is easily adapted to account for entropy deficiency $S+\log1/\gamma$ instead of $S$." It is
genuinely easy, by consequence 1 — Claim 26's proof uses only the entropy bound, so the
substitution is mechanical. But the numerator $S_\zeta+\log\gamma^{-1}$ that Lemma P sets equal to
$P\delta_\zeta\log M$ rests on a one-line "easily adapted" in someone else's footnote, and any
external-results register citing Claim 2 should cite the footnote too.

**Also verified against the paper.** Claims 25 and 26 exist with exactly those numbers on p. 40,
saying exactly what is described above. Claim 25's proof uses only the maximality of $I$. Claim 26's
proof uses the entropy bound *and* the construction's own inequality (5) — which is internal to the
recursion, not a hypothesis on $X$, so consequence 1 stands as intended. And the paper states
Claims 25/26 once, for the first recursion step only; their re-application at every later step is
left implicit, licensed by exactly consequence 1. So consequence 1 is not a re-reading — it is a
step the paper itself needs and does not write down.

## Claim 3 (stated p. 11, proved pp. 11--12)

*For any $(P',1-\delta)$-dense source $X'$ and its corresponding $P'$-bit-fixing source $Y'$
— fixed on the same coordinates to the same values — and for any (adaptive) distinguisher
$D$ that queries at most $T$ coordinates of its oracle,*
$$\bigl|\Pr[D^{X'}=1]-\Pr[D^{Y'}=1]\bigr|\ \le\ T\delta\cdot\log M,$$
*and $\Pr[D^{X'}=1]\le M^{T\delta}\cdot\Pr[D^{Y'}=1]$.*

The proof is an H-coefficient argument on transcripts: $p_{X'}(\tau)\le M^{-(1-\delta)T}$ and
$p_{Y'}(\tau)=M^{-T}$, whence the statistical distance of transcripts is at most
$1-M^{-T\delta}\le T\delta\log M$. It assumes without loss of generality that $D$ is
deterministic and does not query fixed positions.

## Lemma 1 (p. 10) — recorded for completeness, not used

*Let $X$ be uniform over $[M]^N$ and $Z:=f(X)$ with $f:[M]^N\to\{0,1\}^S$. For any $\gamma>0$
and $P\in\mathbb N$ there is a family $\{Y_z\}_{z\in\{0,1\}^S}$ of convex combinations of
$P$-bit-fixing $(N,M)$-sources such that for any distinguisher $D$ taking an $S$-bit input
and querying at most $T<P$ coordinates,*
$$\bigl|\Pr[D^{X}(f(X))=1]-\Pr[D^{Y_{f(X)}}(f(X))=1]\bigr|\ \le\ \frac{(S+\log1/\gamma)\cdot T}{P}+\gamma,$$
*and*
$$\Pr[D^{X}(f(X))=1]\ \le\ 2^{(S+2\log1/\gamma)T/P}\cdot\Pr[D^{Y_{f(X)}}(f(X))=1]+2\gamma.$$

The multiplicative arm was **missing from this card until 27 August 2026** and is added because it
matters for bookkeeping: `PROGRESS.md` records "the multiplicative form of Claim 3" as ruled out as
a route, and this is a *second, different* multiplicative form, belonging to Lemma 1 rather than
Claim 3, which no artifact has examined or ruled out.

This packaged form is **not** what this campaign uses, for two reasons: its family is indexed
by the advice alone, so the decomposed oracle is drawn independently of the real one and is
not consistent with it; and its Claim 4, which bounds $\mathbb E_z[S_z]\le S$, relies on $Z$
being a deterministic function of $X$, which fails for randomised leakage. Claims 2 and 3 are
used directly instead.
