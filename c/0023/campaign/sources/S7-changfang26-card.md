# id: S7-changfang26
# agent: Scout (bounded prior-art check, campaign c/0023, rung I02 / R2)
# model: claude-opus-5[1m]
# cycle: 3; status: COMPLETE

The one item found in the R2 prior-art sweep (`../proofs/0023-scout-4.md`)
that clears the card bar: a printed, poly($d$)-loss, field-agnostic
mechanism converting "$\deg\le d$" into spread-type structure. It is the
only candidate found in print that satisfies I02's *generalization
hypothesis* (survives to R3, where nonnegative real degree-$d$ functions
replace sets), because it is stated for arbitrary field-valued functions.

**Citation.** Fan Chang (Nankai / IBS ECOPRO) and Yijia Fang (NUS),
*VC-Dimension vs Degree: An uncertainty principle for Boolean functions*,
**arXiv:2510.13705v3**, 11 Aug 2026 (v1: 15 Oct 2025). MSC 06E30, 05D05,
68R05, 94B05. **No journal reference is printed** on the arXiv record as of
2026-08-27 — treat as a preprint, unrefereed.

**Retrieval status. [READ]** — v3 PDF fetched from
`arxiv.org/pdf/2510.13705v3`; **pages 1–4 read as page images**, which cover
the abstract, all definitions, Theorem 1.2, Corollary 1.3, Corollary 1.4,
the equality-cases paragraph, and the complete proofs of Theorem 1.2 and
Corollary 1.3. Sections 3–5 (pp. 5–end) **NOT read** — see "what remains
unread", below. The bibliography entries quoted here were obtained from the
arXiv HTML rendering of the same version [READ, via HTML].

---

## Item T1.2 — Theorem 1.2 (p. 2): the support-shattering theorem

**Verbatim statement (LaTeX, p. 2).**

```latex
Let $\mathbb{F}$ be a field and let $f:\{0,1\}^n\to\mathbb{F}$ be non-zero.
Suppose that $c_S\ne 0$ in (1) and that $|S|=\deg_{\mathbb F}(f)$. Then
$\mathrm{supp}(f)$ shatters $S^c=[n]\setminus S$.
```

**Verbatim statement of the numerical form, Corollary 1.3 (p. 2).**

```latex
(VC-dimension vs degree.) Let $\mathbb F$ be a field and let
$f:\{0,1\}^n\to\mathbb F$ be non-zero. Then
\[ \mathrm{VC}(f)+\deg_{\mathbb F}(f)\ \ge\ n. \tag{2} \]
In particular, every non-zero Boolean function $f:\{0,1\}^n\to\{0,1\}$
satisfies
\[ \mathrm{VC}(f)+\deg(f)\ \ge\ n,\qquad
   \mathrm{VC}(f)+\deg_{\mathbb F_2}(f)\ \ge\ n. \tag{3} \]
```

**Definitions the statement depends on (all p. 2, verbatim in substance).**
* (1) is the $\mathbb F$-polynomial representation
  $f(x)=\sum_{S\subseteq[n]}c_Sx^S$, $x^S=\prod_{i\in S}x_i$, unique and
  multilinear; $\deg_{\mathbb F}(f):=\max\{|S|:c_S\ne0\}$. "*For
  $\mathbb F=\mathbb R$ and Boolean-valued $f$, it agrees with the usual
  real, or Fourier, degree $\deg(f)$.*" (printed, p. 2 — this is the
  identification we need).
* $\mathrm{supp}(f):=\{x\in\{0,1\}^n:f(x)\ne0\}$, identifying
  $x\in\{0,1\}^n$ with the set $\{i:x_i=1\}\subseteq[n]$;
  $\mathrm{VC}(f):=\mathrm{VC}(\mathrm{supp}(f))$.
* A family $\mathcal F\subseteq 2^{[n]}$ **shatters** $S$ if all $2^{|S|}$
  subsets of $S$ occur as traces $A\cap S$, $A\in\mathcal F$;
  $\mathrm{VC}(\mathcal F)$ is the largest size of a shattered set.
* Equality cases (p. 4, printed): for $C\subseteq\{0,1\}^n$ a subcube of
  codimension $k$, $\mathrm{VC}(C)=n-k$ and
  $\deg(\mathbf 1_C)=\deg_{\mathbb F_2}(\mathbf 1_C)=k$. "*However,
  subcubes are not the only equality cases; non-subcube examples already
  occur for $n=4$.*"

**Proof mechanism (READ, p. 4).** Half a page and elementary. Fix a
maximum-degree monomial set $S$, $|S|=D=\deg f$. For each $A\subseteq S^c$
restrict the coordinates in $S^c$ by $x_i=1$ ($i\in A$), $x_i=0$
($i\in S^c\setminus A$), giving $g_A:\{0,1\}^S\to\mathbb F$. The
coefficient of $x^S$ in $g_A$ is still $c_S$: a monomial of $f$ can only
contribute to $x^S$ after the restriction if it contains every variable of
$S$, and if it also contained a variable outside $S$ its degree would
exceed $D$. So $g_A\not\equiv0$, hence $g_A(\mathbf 1_B)=f(\mathbf
1_{A\cup B})\ne0$ for some $B\subseteq S$; then $A\cup B\in\mathrm{supp}(f)$
has trace $A$ on $S^c$. As $A$ was arbitrary, $\mathrm{supp}(f)$ shatters
$S^c$.

**Hypotheses itemised, with flags for our objects.**
1. **Any field $\mathbb F$**, and **any** $\mathbb F$-valued $f$; only
   $f\not\equiv0$ is needed. ✔ Our normalized indicators are nonzero
   $\mathbb R$-valued functions. ✔✔ **This is the hypothesis that matters
   for R3:** the theorem does not need $f$ two-valued, unlike every block
   of card S6, so it applies verbatim to nonnegative real degree-$d$
   functions and to their level sets' generating function.
2. **Domain is $\{0,1\}^n$**, printed. ⚠ Our cube is $\{\pm1\}^N$. The
   substitution $x_i\mapsto(1-z_i)/2$ is coordinatewise, invertible and
   affine, so it preserves the multilinear degree (printed in card S6's
   shared convention 1) and carries $\mathrm{supp}$ to $\mathrm{supp}$ and
   shattering to shattering (shattering is a statement about the set of
   coordinate patterns realised, invariant under relabelling $0
   \leftrightarrow -1$ per coordinate). [SCOUT'S OWN REMARK, one line, not
   printed here.] After the substitution, "$A$ shatters $T$" reads: for
   every $y\in\{\pm1\}^T$ there is $a\in A$ with $a|_T=y$, i.e. **$A$
   projects onto $\{\pm1\}^T$**.
3. **$|S|$ is the EXACT degree**, not an upper bound. ✔ harmless: our
   hypothesis $\deg(\mathbf 1_A)\le d$ gives $|S|=\deg(\mathbf 1_A)\le d$,
   so the shattered set has size $\ge N-d$.
4. Normalization is irrelevant: $\mathrm{supp}(\alpha^{-1/2}\mathbf
   1_A)=A$ and the degree is unchanged (card S6, shared convention 3). ✔
5. No hypothesis on $n$ (=$N$); the statement is uniform in $N$. ✔ — this
   is essential for the Contract's $N$-free $\delta$.

**Conclusion in my own words, in the campaign's language.** For every
nonempty $A\subseteq\{\pm1\}^N$ with $\deg(\mathbf 1_A)\le d$ there is a
coordinate set $T=T(A)\subseteq[N]$ with $|T|\le d$ such that $A$ projects
**onto** all of $\{\pm1\}^{[N]\setminus T}$: every pattern off $T$ is
realised by some point of $A$. Equivalently, degree $\le d$ forces
full-projection outside a set of at most $d$ coordinates. Immediate
consequences: $|A|\ge 2^{N-d}$, i.e. density $\ge 2^{-d}$ (this recovers
[NS94, Lemma 2.6] for indicators — Chang–Fang themselves note the
comparison on p. 2, citing "[23, Lemma 2.6]" with [23] = Nisan–Szegedy
1994, which independently corroborates card S5's attribution of that
lemma number); and $\mathrm{VC}(A)\ge N-d$.

**What it does NOT say.**
* **Nothing about influences**, of any flavour. The word does not appear in
  any statement on pp. 1–4 (the abstract's only nod is "*Motivated by the
  study of low-influence Boolean functions*", p. 1, with no influence
  result).
* **Nothing about two sets or two families.** Checked twice: no pair or
  cross-condition statement occurs on the read pages, and an
  HTML-wide check for two-family statements returned none. So it does
  **not** settle or partially settle R2 by itself.
* Nothing distributional; nothing about $\ell_2$ norms; no upper bound on
  density; no *lower* bound on degree in terms of anything we control.
* $T(A)$ is **not canonical**: it is "some maximum-degree monomial set", of
  which there may be many, and the theorem gives no way to choose one
  coherently across a family — a real obstacle for any two-family argument,
  since R1's payment argument needs windows that can be compared.
* It does **not** say $A$ contains a subcube of codimension $\le d$, only
  that it surjects onto the complementary coordinates; nothing controls the
  fibres (a fibre may be a single point).
* It gives no bound on the number of relevant coordinates (that is S6), and
  $T(A)$ is not the junta set: $A$ can depend on $\approx 2^d$ coordinates
  while $|T(A)|\le d$.

**Prior-art caveat — do not claim novelty.** The algebraic content sits next
to the classical "standard monomial" theory of set systems (Frankl–Pach;
Anstee–Rónyai–Sali) and to Moran–Rashtchian, *Shattered sets and the
Hilbert function*, arXiv:1511.08245 [abstract READ only; it runs the other
direction — extremal VC classes resist low-degree approximation], and the
support-size corollary is explicitly older ([NS94, Lemma 2.6]). Chang–Fang
present Theorem 1.2 as new ("*our main result is the following structural
theorem*", p. 2) while noting their framework re-derives Sauer–Shelah and
Sziklai–Weiner. The shattering upgrade may well be folklore in the standard-
monomial literature. For citation purposes this does not matter: the
statement above is printed and read; if a referee wants an older source,
that is a source-queue item, not a gap.

## Item C1.4 — Corollary 1.4 (p. 4), recorded only to delimit

```latex
(Sziklai--Weiner over arbitrary fields.) Let $\mathbb F$ be a field, let
$0\le r\le n$, and let $P\in\mathbb F[X_1,\dots,X_n]$. Denote $w_H(x)$ the
Hamming weight simply as the number of $1$'s in $x$. Suppose that $P(x)=0$
for every $x\in\{0,1\}^n$ with $w_H(x)>r$ and that $P(x_0)\ne 0$ for some
$x_0\in\{0,1\}^n$ with $w_H(x_0)\le r$. Then $\deg(P)\ge n-r$.
```

Not usable for R2 (its hypothesis is vanishing on a Hamming ball
complement, which our sets do not satisfy), but recorded because it is the
paper's only other statement about a polynomial forced to vanish on a large
prescribed region — the nearest thing in this paper to a
disjoint-support hypothesis.

## What remains unread (and why it is the campaign's next deciding source)

Sections 3–5 (pp. 5–end) were not read. From the printed roadmap (pp. 3–4)
they contain, in order: the Sauer–Shelah proof; a **finite-product-space
analogue** — printed as inequality (5), p. 3, "$\dim_\pi(\mathrm{supp}(f))+
\deg_\otimes(f)\ge n$ for every nonzero $f:X_1\times\dots\times X_n\to
\mathbb F$", where $\dim_\pi$ is the coordinate-projection dimension
("*the largest number of coordinates on which $\mathcal A$ realizes every
possible coordinate pattern*") and $\deg_\otimes$ is the Efron–Stein degree;
a **multivalued Sauer lemma / finite-Abelian-group version**; the Fourier-
support theorem (4) $\mathrm{VC}(\mathrm{Spec}(f))\ge\deg_{\mathbb F_2}(f)$,
$\mathrm{VC}(\mathrm{supp}(f))+\mathrm{VC}(\mathrm{Spec}(f))\ge n$; and
equality cases with computations for $n\le4$.

The product-space form (5) is the one the *parent* Contract needs, because
the parent quantifies over an arbitrary finite abelian group $\mathcal Y$
and its degree is exactly the Efron–Stein / character-support degree of the
Contract's definition. If (5) is printed with $\deg_\otimes$ equal to the
Contract's $\deg$, the mechanism lifts from $\mathbb Z_2$ to every
$\mathcal Y$ in one step.

## Where the campaign would use it

**R2, as the poly($d$) replacement for the junta window.** [SCOUT'S OWN
INFERENCE, UNVERIFIED — a lead for the Strategist, not a result.] Let
$A,B\subseteq\{\pm1\}^N$ be nonempty, $\deg\mathbf 1_A,\deg\mathbf 1_B\le
d$, $A\cap B=\emptyset$. Apply T1.2 twice: $A$ projects onto
$\{\pm1\}^{[N]\setminus T_A}$ and $B$ onto $\{\pm1\}^{[N]\setminus T_B}$
with $|T_A|,|T_B|\le d$. Put $T=T_A\cup T_B$, $|T|\le 2d$. Then for every
pattern $w$ on $[N]\setminus T$ **both** $A$ and $B$ contain points whose
restriction off $T$ agrees with $w$ in the coordinates each is free on, and
$A\cap B=\emptyset$ forces the achievable traces on $T$ to conflict. This
is the same *shape* as R1's "conflicting patterns on a shared window of
size $\le d$", with window $T$ of size $\le 2d$ — i.e. a candidate way to
re-base R1's payment argument on a **$2d$-sized** window instead of a
$4.394\cdot2^d$-sized junta, which is exactly the poly($d$) mechanism I02
asks for. Two visible obstacles, both real: (i) $w$-dependence — the
conflicting trace pair may vary with $w$, whereas R1's cylinders conflict
uniformly; (ii) non-canonicity of $T(A)$ across a distribution's support
(see "what it does NOT say"), so the union $T$ over a whole family is not
bounded and the argument must be run pairwise or with a covering step.
Neither obstacle is addressed by anything in print that I found.

**R3.** Because T1.2 holds for arbitrary field-valued nonzero $f$, the same
window $T(f)$, $|T(f)|\le\deg f$, exists for a nonnegative real degree-$d$
function; the mechanism is therefore not killed by I02's generalization
hypothesis, unlike everything in card S6.

**Not for.** Any statement about influence, about families, or about the
threshold $\delta(d)$ — none of that is in this paper.

### END OF ARTIFACT S7-changfang26 ###
