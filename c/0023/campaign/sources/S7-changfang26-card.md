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
2026-08-27 — treat as a preprint. ~~unrefereed~~ **[CORRECTED by S7b,
2026-08-27:** the word "unrefereed" was wrong. v3's Acknowledgement (p. 12)
thanks "the anonymous referees for their careful reading of the manuscript",
so v3 has been through at least one refereeing round; only the *venue* is
unknown. Also: there is a **v2** (16 Oct 2025) the card omitted, and the
paper is **14 pages**.**]**

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
   [**S7b cross-reference:** flag 2's scout-own affine translation remark is
   no longer load-bearing — **Corollary 3.4** (block T3.4 below) is printed
   natively in character/Fourier language on a product of finite abelian
   groups, hence applies to $\{\pm1\}^N=\mathbb Z_2^N$ with the Contract's own
   degree and no change of variables.]
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

---

### SOURCE CARD [S7b] ###

# id: S7b-changfang26-addendum
# agent: Scout (bounded deciding-source read, campaign c/0023, cycle 3)
# model: claude-opus-5[1m]
# cycle: 3; status: COMPLETE

Addendum to card S7. Two jobs: (1) independent verification of the S7
attribution; (2) extension to the unread §§3–5, targeting the product-space
inequality (5) and the multivalued / finite-abelian-group versions.

**Retrieval status. [READ] — the ENTIRE paper, all 14 pages, as page images**
of the v3 PDF (`arxiv.org/pdf/2510.13705v3`, fetched 2026-08-27; the fetch
persisted the PDF locally and it was read with the page-image reader).
Rungs used: ladder rung 1 (arXiv) only; no block encountered. Abstract page
`arxiv.org/abs/2510.13705` also [READ]; the HTML rendering
`arxiv.org/html/2510.13705v3` was used first and **partially refused** to
reproduce whole sections, which is why the page-image read was done — record
this: for this paper the HTML route yields only short quotes, the PDF route
yields everything.

---

## JOB 1 — VERIFICATION VERDICT: **CARD S7 CONFIRMED** (one non-mathematical correction)

Everything mathematical in card S7 is exact. Checked item by item against
the printed pages:

* **Title (p. 1, verbatim):** "VC-Dimension vs Degree: An uncertainty
  principle for Boolean functions". ✔ matches S7.
* **Authors and affiliations (p. 1 footnotes, verbatim):** "Fan Chang" —
  "School of Statistics and Data Science, Nankai University, Tianjin, China
  and Extremal Combinatorics and Probability Group (ECOPRO), Institute for
  Basic Science (IBS), Daejeon, South Korea. E-mail:
  1120230060@mail.nankai.edu.cn. Supported by the NSFC under grant 124B2019
  and the Institute for Basic Science (IBS-R029-C4)."; "Yijia Fang" —
  "Department of Mathematics, National University of Singapore, Singapore.
  Email: fangyijia@u.nus.edu." ✔ matches S7's "Nankai / IBS ECOPRO" and
  "NUS". Two authors, no more.
* **Versions:** v1 15 Oct 2025 (21 KB), **v2 16 Oct 2025 (21 KB)**, v3
  11 Aug 2026 (17 KB), 14 pages; comments field "14 pages. This version
  contains a simpler proof and several additional applications"; primary
  class math.CO, cross-lists cs.CC, cs.DM; DOI 10.48550/arXiv.2510.13705;
  **no journal reference**. Stamp on p. 1: "arXiv:2510.13705v3 [math.CO]
  11 Aug 2026". S7 omitted v2 and the page count; added above.
* **MSC (p. 1, verbatim):** "Mathematics Subject Classification: 06E30;
  05D05; 68R05; 94B05". ✔ matches S7.
* **Theorem 1.2 — printed numbering and page CONFIRMED: p. 2**, stated in §1
  (Introduction), proof in §2 on **p. 4**. Verbatim, p. 2:
  > **Theorem 1.2.** *Let $\mathbb F$ be a field and let $f:\{0,1\}^n\to
  > \mathbb F$ be non-zero. Suppose that $c_S\ne 0$ in (1) and that
  > $|S|=\deg_{\mathbb F}(f)$. Then $\mathrm{supp}(f)$ shatters
  > $S^c=[n]\setminus S$.*

  This is **character-for-character** what card S7 records. ✔
* **Corollary 1.3 — p. 2** (numbering and page CONFIRMED), proof p. 4.
  Verbatim:
  > **Corollary 1.3** (VC-dimension vs degree). *Let $\mathbb F$ be a field
  > and let $f:\{0,1\}^n\to\mathbb F$ be non-zero. Then*
  > $$\mathrm{VC}(f)+\deg_{\mathbb F}(f)\ \ge\ n. \tag{2}$$
  > *In particular, every non-zero Boolean function $f:\{0,1\}^n\to\{0,1\}$
  > satisfies*
  > $$\mathrm{VC}(f)+\deg(f)\ \ge\ n,\qquad
  >   \mathrm{VC}(f)+\deg_{\mathbb F_2}(f)\ \ge\ n. \tag{3}$$

  ✔ matches S7 exactly, including the equation numbers (2) and (3).
* **Corollary 1.4 — p. 4** ✔ (S7's page is right); its *proof* is on p. 8
  (§4.2). Statement verbatim as in S7.
* **Definitions** (S7's block): (1) on p. 2, $\deg_{\mathbb F}$, the printed
  sentence "For $\mathbb F=\mathbb R$ and Boolean-valued $f$, it agrees with
  the usual real, or Fourier, degree $\deg(f)$", $\mathrm{supp}$/$\mathrm{VC}$
  on p. 2, "shatters" on p. 2, equality cases on p. 4 including "*However,
  subcubes are not the only equality cases; non-subcube examples already
  occur for $n=4$*". ✔ all confirmed verbatim on the stated pages.
* **Proof mechanism** as S7 paraphrases it (p. 4): ✔ confirmed line by line;
  the printed proof is 12 lines and elementary, with no auxiliary hypothesis.
* **S7's "roadmap" predictions all confirmed:** inequality (4) p. 3
  (= Theorem 4.1, p. 7); inequality (5) p. 3 (= Theorem 3.2, p. 6); the
  multivalued Sauer lemma (§3.3, p. 6) and the finite-abelian-group version
  (§3.4, p. 7); equality cases and $n\le4$ computations (§5, p. 10 + App. A).
* **S7's "does NOT say" list, now checked against ALL 14 pages, not 4:**
  the word "influence" appears **exactly once in the paper**, in the motivating
  sentence on p. 1 ("Motivated by the study of low-influence Boolean
  functions"), and in **no** statement, definition or proof. And there is
  **no** statement anywhere in the paper involving two functions, two
  families, a pair of sets, disjoint supports, or any cross-condition. S7's
  two most load-bearing negative claims are therefore **upgraded from
  "checked on pp. 1–4 + an HTML scan" to "verified over the complete text"**.

**The single correction (non-mathematical).** S7 wrote "treat as a preprint,
**unrefereed**". That is wrong: p. 12's Acknowledgement reads "The authors
would like to thank the anonymous referees for their careful reading of the
manuscript and for many valuable comments and suggestions, which
significantly improved the quality of the paper. The authors are especially
grateful to one anonymous referee whose helpful suggestions enabled the
authors to simplify the proof." So v3 is a **post-referee** revision (which
also explains the comments field "simpler proof"); the venue is simply not
printed. Corrected in place at the Citation block, with the v2 date and page
count added. Second in-place edit: a cross-reference line added at hypothesis
flag 2, because block T3.4 below removes the need for that flag's
scout-own $\{0,1\}\to\{\pm1\}$ affine remark. **Nothing else in S7 was
changed and nothing was deleted.**

Corroboration recorded in passing: the bibliography (p. 13) prints
"[23] N. Nisan and M. Szegedy. On the degree of Boolean functions as real
polynomials. *Comput. Complexity*, 4(4):301–313, 1994", so p. 2's citation
"[23, Lemma 2.6]" independently corroborates card S5's NS94 Lemma 2.6
attribution — as S7 already said, now with the full bibliographic entry.

---

## JOB 2(a) — Item T3.2: the product-space uncertainty principle (inequality (5))

**Verbatim statement, p. 6** (printed numbering **Theorem 3.2**; the
inequality is previewed unnumbered as (5) on p. 3):

```latex
Theorem 3.2 (Product-space uncertainty principle). Let
$f:X_1\times\cdots\times X_n\to\mathbb F$ be non-zero. If $S\subseteq[n]$
satisfies $f^{=S}\ne 0$ and $|S|=\deg_\otimes(f)$, then
\[ \pi_{S^c}(\mathrm{supp}(f)) = X_{S^c}. \]
In particular,
\[ \dim_\pi(\mathrm{supp}(f)) + \deg_\otimes(f) \ \ge\ n. \]
```

Proof: p. 6, half a page, elementary (fix $a\in X_{S^c}$, restrict $f$ to the
fibre $f_a(x_S)=f(x_S,a)$, show the $S$-component of $f_a$ is still the
non-zero $f^{=S}$, hence $f_a\not\equiv0$).

**The definitions it uses, verbatim, p. 3** (this is where a false transfer
would hide, so all of it is quoted):

```latex
Let $X = X_1\times\cdots\times X_n$ be a finite product set. For
$T\subseteq[n]$, write $X_T:=\prod_{i\in T}X_i$, with the convention that
$X_\emptyset$ is a one-point set. Let
  $\pi_T : X\to X_T$,   $\pi_T(x_1,\dots,x_n)=(x_i)_{i\in T}$,
be the coordinate projection. If $\mathcal A\subseteq X$, then
$\pi_T(\mathcal A):=\{\pi_T(x):x\in\mathcal A\}\subseteq X_T$. For a nonempty
set $\mathcal A\subseteq X$, define its coordinate projection dimension by
  $\dim_\pi(\mathcal A):=\max\{|T| : \pi_T(\mathcal A)=X_T\}$.
```

and, on the same page:

```latex
We use the standard degree associated with the Efron--Stein decomposition on
product spaces [24, Section 8.3]. Namely, write
  $f=\sum_{S\subseteq[n]} f^{=S}$
for the Efron--Stein degree decomposition. Equivalently, after choosing
complements $\mathbb F^{X_i}=\langle1\rangle\oplus W_i$ to the constants, the
component $f^{=S}$ lies in $\bigotimes_{i\in S}W_i\otimes
\bigotimes_{i\notin S}\langle1\rangle$. We define
  $\deg_\otimes(f):=\max\{|S| : f^{=S}\ne 0\}$.
Equivalently, $\deg_\otimes(f)\le r$ means that $f$ lies in the linear span of
all functions depending on at most $r$ coordinates.
```

Printed glosses worth carrying: "$\dim_\pi(\mathcal A)$ is the largest number
of coordinates on which $\mathcal A$ realizes every possible coordinate
pattern. This is the full-projection, or coordinate-density, notion of
Karpovsky–Milman [17]; in Alon's terminology [1], $\mathcal A$ is $I$-dense
exactly when $\pi_I(\mathcal A)=X_I$. In the homogeneous case
$X_1=\cdots=X_n=[q]$, it is the $q$-ary VC-dimension [22], also called the
Karpovsky–Milman dimension in later work on multivalued shattering [14]."
([24] = O'Donnell's book; [17] = Karpovsky–Milman, *Coordinate density of sets
of vectors*, Discrete Math. 24(2):177–184, 1978; [1] = Alon, *On the density
of sets of vectors*, Discrete Math. 46(2):199–202, 1983; [14] = Füredi–Sali,
*Optimal multivalued shattering*, SIAM J. Discrete Math. 26(2):737–744, 2012.)

**Hypotheses itemised, with flags.**
1. **$X=X_1\times\cdots\times X_n$ a FINITE product set** (printed on p. 3,
   inherited by Theorem 3.2); the $X_i$ are arbitrary finite sets and need
   **not** have equal sizes, and carry **no** algebraic or measure structure.
   ✔ Our $\mathcal Y^N$ is such a product.
2. **$\mathbb F$ an arbitrary field; $f$ arbitrary $\mathbb F$-valued,
   non-zero.** **No hypothesis on the characteristic of $\mathbb F$, on
   $|X_i|$ being invertible in $\mathbb F$, or on $\mathbb F$ being
   algebraically closed is stated anywhere in §3** — I looked for one
   specifically. ✔ for $\mathbb R$ and $\mathbb C$.
3. **$\deg_\otimes$ is defined relative to a CHOICE of complements
   $\mathbb F^{X_i}=\langle1\rangle\oplus W_i$.** ⚠ The paper never states
   that $\deg_\otimes$ is independent of that choice — but it does print the
   choice-free characterisation "*$\deg_\otimes(f)\le r$ means that $f$ lies
   in the linear span of all functions depending on at most $r$ coordinates*"
   (p. 3), which pins the value with no reference to $W_i$. **So the
   choice-dependence worry is answered in print**, and no scout inference is
   needed. Record it anyway: a prover quoting Theorem 3.2 in the general
   $\mathbb F$ form should quote the span characterisation alongside it.
4. **$|S|$ must be the EXACT $\deg_\otimes$** for the surjectivity form.
   ✔ harmless as in S7's flag 3: a bound $\deg_\otimes(f)\le d$ gives
   $\dim_\pi(\mathrm{supp}f)\ge n-d$, which is the form we use.
5. **$\mathcal A$ nonempty** is required for $\dim_\pi$ to be defined. ✔ our
   $f$ is unit-norm hence non-zero hence $\mathrm{supp}(f)\ne\emptyset$.
   (Note $T=\emptyset$ always qualifies, so $\dim_\pi\ge0$ always.)
6. No hypothesis on $n$; uniform in $n$. ✔ essential for the $N$-free
   $\delta$.

**IS $\deg_\otimes$ THE CONTRACT'S DEGREE? Answer: YES, and it is printed,
not inferred** — see T3.4. On a general finite product set with no group
structure the two notions cannot even be compared (the Contract's degree is
character-based and needs a group); the paper supplies the bridge itself in
§3.4, so the campaign does **not** have to argue the identification.

## JOB 2(b) — Item T3.3 and T3.4: multivalued and finite-abelian-group versions

**Both are PROVED in print, not announced and not deferred.**

**Theorem 3.3 (Multivalued Sauer lemma), p. 6, proof pp. 6–7.** Verbatim:

```latex
Theorem 3.3 (Multivalued Sauer lemma). Let $\mathcal A\subseteq
X_1\times\cdots\times X_n$ satisfy $\dim_\pi(\mathcal A)\le d$. Then
\[ |\mathcal A| \ \le\ \sum_{\substack{S\subseteq[n]\\|S|\ge n-d}}
     \prod_{i\in S}(q_i-1). \tag{6} \]
In particular, if $q_1=\cdots=q_n=q$, then
\[ |\mathcal A| \ \le\ \sum_{i=0}^{d}\binom{n}{i}(q-1)^{n-i}. \]
```
with $q_i:=|X_i|$ (printed, p. 6). The paper presents this as a **recovery,
not a new result**: "*We next recover the full-projection multivalued Sauer
lemma of Karpovsky–Milman, in Alon's non-homogeneous coordinate-density form
[17, 1]*" (p. 6). **Counting only — no degree hypothesis, no function.** Not
usable for R2 (see "does NOT say").

**Corollary 3.4, p. 7, proof p. 7. THIS IS THE ITEM THE PARENT CONTRACT
NEEDS.** The definitions and statement, verbatim, p. 7:

```latex
Let $G=G_1\times\cdots\times G_n$ be a product of finite Abelian groups.
Every character $\chi$ of $G$ factors as
  $\chi=\chi_1\otimes\cdots\otimes\chi_n$,
where $\chi_i$ is a character of $G_i$. Define the Fourier degree of a
character by
  $\deg(\chi):=|\{i:\chi_i \text{ is non-trivial}\}|$,
and for $f:G\to\mathbb C$, define
  $\deg_{\hat G}(f):=\max\{\deg(\chi):\hat f(\chi)\ne0\}$.

Corollary 3.4. Let $G=G_1\times\cdots\times G_n$ be a product of finite
Abelian groups, and let $f:G\to\mathbb C$ be non-zero. Then
\[ \dim_\pi(\mathrm{supp}(f)) + \deg_{\hat G}(f)\ \ge\ n. \]
```

and its complete printed proof, verbatim (four lines):

```latex
Proof. For each $i$, take $W_i\subseteq\mathbb C^{G_i}$ to be the span of the
non-trivial characters of $G_i$. Then $\mathbb C^{G_i}=\langle1\rangle\oplus
W_i$. With this choice, the Efron--Stein component $f^{=S}$ is precisely the
sum of the Fourier terms whose non-trivial coordinate factors occur exactly
on $S$. Hence $\deg_\otimes(f)=\deg_{\hat G}(f)$. The result follows from
Theorem 3.2.
```

**Hypotheses itemised, with flags for the Contract's objects
($\mathcal Y$ a finite abelian group, $f:\mathcal Y^N\to\mathbb C$,
$\|f\|_2=1$, $\deg(f)\le d$).**
1. **$G$ a finite product of finite abelian groups.** ✔ Take
   $G_1=\cdots=G_N=\mathcal Y$, $n=N$; the Contract's $\mathcal Y^N$ is a
   special case (the theorem is strictly more general — it allows different
   groups per coordinate, which the Contract does not need).
   ✔ **No** hypothesis that $\mathcal Y$ be cyclic, of prime order, of odd
   order, or a $p$-group. **No** hypothesis relating $|G_i|$ to anything.
2. **$f:G\to\mathbb C$, non-zero.** ✔ exact match to the Contract's value
   range (ℂ, per K3′). Unit norm is not needed and not used; it only
   guarantees non-zeroness. ✔
3. **$\deg_{\hat G}$ is EXACTLY the Contract's degree**, printed:
   $\deg(\chi)=|\{i:\chi_i\ \text{non-trivial}\}|$ and
   $\deg_{\hat G}(f)=\max\{\deg(\chi):\hat f(\chi)\ne0\}$, versus the
   Contract's `deg(χ) := |{i : χ_i ≠ 0̂}|`, `deg(f) := max{deg(χ) : f̂(χ)≠0}`.
   **Identical, symbol for symbol.** ✔✔ No transfer step, no convention
   mismatch, no tensor-vs-individual-degree ambiguity: the paper's own
   §3.4 does the identification $\deg_\otimes=\deg_{\hat G}$ for us.
   [One remark that is mine, not printed: the paper does not state its
   normalisation of $\hat f$; irrelevant, since the *vanishing pattern*
   $\hat f(\chi)\ne0$ is invariant under any non-zero rescaling of the
   transform, and the Contract's $\hat f$ is the orthonormal-character one.]
4. **Conclusion, unfolded via the printed definition of $\dim_\pi$:** there
   exists $T\subseteq[N]$ with $|T|=\dim_\pi(\mathrm{supp}f)\ge N-d$ such
   that $\pi_T(\mathrm{supp}f)=\mathcal Y^T$, i.e. **every** pattern in
   $\mathcal Y^T$ is realised by some $x$ with $f(x)\ne0$. Since
   $\pi_T$ surjective implies $\pi_{T'}$ surjective for every $T'\subseteq T$,
   the window $W:=[N]\setminus T$, $|W|\le d$, may be **enlarged freely**
   (shrinking $T$). This unfolding is definitional, not an inference.
   The stronger fibre-wise form $\pi_{S^c}(\mathrm{supp}f)=\mathcal Y^{S^c}$
   for $S$ any maximum-degree character support also holds, since
   $\deg_\otimes=\deg_{\hat G}$ lets Theorem 3.2's first display be applied
   directly.
5. Uniform in $N$; no asymptotics. ✔

**Conclusion in my words, in the Contract's language.** *For every finite
abelian group $\mathcal Y$, every $N$, and every non-zero $f:\mathcal Y^N\to
\mathbb C$ with $\deg(f)\le d$, there is a coordinate set $W\subseteq[N]$ with
$|W|\le d$ such that $\mathrm{supp}(f)$ projects ONTO $\mathcal Y^{[N]
\setminus W}$.* Degree $\le d$ forces full-projection outside a window of at
most $d$ coordinates — **group-uniformly, at every rung, with a $d$-sized (not
$2^{\Theta(d)}$-sized) loss.** So the S7 mechanism is **not** a
$\mathbb Z_2$-only import: it is available at R2, at R3 (non-zero real- or
complex-valued functions, no two-valuedness), and at the **top rung** for the
Contract's existentially-quantified $\mathcal Y$. This resolves possibility
(i) of `../proofs/0023-scout-4.md` §E affirmatively.

**What T3.2 / T3.3 / T3.4 do NOT say.** All of S7's negative list carries
over verbatim and is now verified against the complete text; additionally:
* **Nothing about influence.** One occurrence of the word in the paper, in a
  motivating clause on p. 1. No $\mathrm{Inf}_i$, no total influence, no
  noise operator, no hypercontractivity anywhere.
* **Single function only.** No two-function, two-family, pair, disjoint-
  support or cross-condition statement exists anywhere in the 14 pages. So
  neither R2 nor the Contract is settled or partially settled by this paper.
* **Theorem 3.3 is a pure counting bound with no function and no degree**; it
  bounds $|\mathcal A|$ from a $\dim_\pi$ *upper* bound, i.e. it runs in the
  direction opposite to our use (we get a $\dim_\pi$ *lower* bound and want
  structure, not a size bound). It is also explicitly **not new**
  (Karpovsky–Milman 1978 / Alon 1983; Füredi–Sali 2012). Do not cite it as
  the paper's contribution and do not use it for R2.
* **No canonical window.** $T$ is an arbitrary maximiser (equivalently $S^c$
  for an arbitrary maximum-degree character support); the paper offers no way
  to choose $T$ coherently across a family of functions. S7's obstacle (ii) —
  unbounded union of windows over a distribution's support — is **unchanged**
  by §§3–5.
* **No control of fibres.** $\pi_T$ surjective says nothing about
  $|\mathrm{supp}(f)\cap\pi_T^{-1}(y)|$; a fibre may be a single point. In
  particular this is *not* a subcube / product-structure conclusion.
* **[SCOUT'S OWN REMARK, flagged, one line, not printed anywhere:]** the
  *counting* consequence of T3.4 is only $|\mathrm{supp}f|\ge
  |\mathcal Y|^{N-d}$, i.e. density $\ge|\mathcal Y|^{-d}$ — **exactly card
  S1's K1 scale** for every group. So no argument that uses T3.4 *only* through
  the density it implies can beat K1; the poly($d$) content is in the
  coordinate structure (the $\le d$-sized window), never in the density. Any
  prover reaching for T3.4 should state which of the two it is using.
* Nothing distributional, nothing about $\ell_2$ norms, no upper bound on
  density, no lower bound on degree in terms of anything we control, no
  bound on the number of relevant coordinates (that is card S6).

**Where the campaign would use it.**
* **R2 (`../intermediates/I02-degree-d-sets.md`):** as S7's block "Where the
  campaign would use it" already records, unchanged — for a cross-disjoint
  pair $A,B$ take $W=W_A\cup W_B$, $|W|\le 2d$; both supports surject onto
  $\mathcal Y^{[N]\setminus W}$. Still a **lead, not a result**: obstacles (i)
  $w$-dependence of the conflicting trace and (ii) non-canonicity of the
  window are untouched by §§3–5.
* **R3 and the top rung:** T3.4 is the group-uniform, ℂ-valued form, so the
  mechanism survives the generalization hypothesis of I02 *and* reaches the
  Contract's existential $\mathcal Y$ in one step, with no scout inference in
  the chain. This is the addendum's main deliverable.
* **Not for:** anything about influence, families, or the threshold
  $\delta(d)$.

**Prior-art caveat, extended.** §3.3 is explicitly a recovery
(Karpovsky–Milman/Alon). §3.4 is presented as a corollary of §3.2 with **no
attribution to prior work and no novelty claim**; given how short its proof
is and how classical the character decomposition is, **treat the
finite-abelian-group shattering statement as plausibly folklore and do not
claim novelty for it**. For citation purposes this is immaterial: the
statement is printed and read. §3.1 recovers Sauer–Shelah–Perles–VC, with a
printed remark (p. 5) placing the method next to Anstee–Rónyai–Sali
*Shattering news* [2] and Gröbner-basis treatments [21, 25].

### END OF ARTIFACT S7b-changfang26-addendum ###
