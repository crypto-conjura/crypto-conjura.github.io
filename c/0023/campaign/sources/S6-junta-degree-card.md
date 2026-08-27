# id: S6-junta-degree
# agent: Scout (source-carding errand, campaign c/0023, rung I02 / R2)
# model: claude-opus-5[1m]
# cycle: 3; status: COMPLETE

Discharges the first errand of `../intermediates/I02-degree-d-sets.md`: the
[MEMORY] flag on "a degree-$\le d$ Boolean function is a junta on $M(d)$
coordinates, $M(d)=2^{\Theta(d)}$". Four blocks, because the errand's three
named items split into an upper bound whose *sharpest printed constant* lives
in a fourth paper:

| block | result | retrieval |
|---|---|---|
| **S6a** | Nisan–Szegedy: $M(d)\le d\,2^{d-1}$, and the per-coordinate influence engine | [RESTATED] + [BLOCKED] on the 1994 print |
| **S6b** | Chiarelli–Hatami–Saks: $M(d)\le 6.614\cdot 2^{d}$ | [READ] |
| **S6c** | Wellens: $M(d)\le 4.394\cdot 2^{d}$ — **the sharpest printed bound** | [READ] |
| **S6d** | lower bounds: $M(d)\ge 3\cdot 2^{d-1}-2$ (and $\ge 2^d-1$) | [READ] |

**Notation fixed for this card.** $R(f)$ / $n(f)$ = number of relevant
variables of $f$ (the two sources' two names for the same quantity);
$$M(d)\ :=\ R_d\ :=\ \max\{R(f)\ :\ f\ \text{Boolean},\ \deg(f)\le d\},$$
which is I02's $M(d)$. $C_d:=R_d2^{-d}$; $C^*:=\lim_{d\to\infty}C_d$ (the
limit exists because $C_d$ is increasing, S6b). All four blocks are
statements about $M(d)$, uniformly in the number of variables $n$.

**Bottom line, printed record (combine S6c and S6d):**
$$3\cdot 2^{d-1}-2\ \le\ M(d)\ \le\ 4.394\cdot 2^{d}\qquad\text{for all }d\ge 1,$$
so $M(d)=\Theta(2^d)$ — **exponential in $d$, with matching exponent, as a
matter of print.** I02's recorded trap is therefore real and unavoidable, not
an artifact of a weak upper bound (see "Where the campaign uses this",
below).

---

## Shared conventions and the {0,1}/{±1} question (read once, applies to all blocks)

All four sources state their results for
$$f\colon\{0,1\}^n\to\{0,1\},$$
with $\deg(f)$ the degree of the unique multilinear polynomial in
$\mathbb{R}[x_1,\dots,x_n]$ agreeing with $f$ on $\{0,1\}^n$ (CHS p. 1;
Wellens DA p. 3). Our objects are $\{0,1\}$-valued indicators
$\mathbf 1_A$ on $\{\pm1\}^N$, normalized by $\|\mathbf 1_A\|_2$. Three
identifications are needed; the first is printed, the other two are
elementary and are flagged as the scout's own remarks, not citations.

1. **Domain $\{0,1\}^n$ vs $\{\pm1\}^n$: degree is unchanged. PRINTED**
   — Wellens, arXiv:1903.08214v2, p. 3 [READ]: "*Since the degree of $f$
   remains unchanged when $f$ is expressed as a multilinear polynomial over
   $\{0,1\}^n$ (as we consider in this paper) or $\{1,-1\}^n$ (as in the
   Fourier expansion) …*". So the Contract's $\deg$ (Fourier degree on
   $\{\pm1\}^N$) is exactly the sources' $\deg$ after the substitution
   $x_i\mapsto (1-z_i)/2$. The set of relevant coordinates is likewise
   preserved (the substitution is coordinatewise and invertible).
2. **Range $\{0,1\}$ vs $\{\pm1\}$: degree unchanged for non-constant $f$.**
   [SCOUT'S OWN ONE-LINE REMARK, not printed in these sources] $g:=1-2f$ is
   $\{\pm1\}$-valued and $f=(1-g)/2$; both maps are affine in the *value*,
   so $\deg f=\deg g$ whenever $f$ is non-constant, and both are $0$ when
   $f$ is constant. Hence "degree-$d$ Boolean function" may be read with
   either value set. (S6d's witness $\Xi_d$ is printed $\{\pm1\}$-valued;
   S6a–S6c are printed $\{0,1\}$-valued. No block changes under the switch.)
3. **Normalization is invisible to degree and to relevance.** [SCOUT'S OWN
   REMARK] $\mathbf 1_A/\|\mathbf 1_A\|_2=\alpha^{-1/2}\mathbf 1_A$ with
   $\alpha:=|A|/2^N=\|\mathbf 1_A\|_2^2>0$ a positive scalar; multiplying by
   it changes no monomial's vanishing, hence changes neither $\deg$ nor the
   relevant-coordinate set. It *does* rescale influence: see the influence
   dictionary in S6a.

**Consequence.** Every $f\in\mathcal C^{\mathrm{ind}}_d$ satisfies all
hypotheses of S6a–S6c after these identifications, and the conclusions apply
to it verbatim with $M(d)$ unchanged. **No hypothesis of any block fails for
our objects.** (This is the one thing the rung most needed checked: the
junta bound is *not* dodged by the indicator/normalization/±1 setting.)

---

### SOURCE CARD [S6a] ###

**Citation.** Noam Nisan and Mario Szegedy, *On the degree of Boolean
functions as real polynomials*, **Computational Complexity 4 (1994), no. 4,
301–313**, DOI 10.1007/BF01263419. Conference version: STOC '92, DOI
10.1145/129712.129757. (Bibliographic data cross-checked against three
independent bibliographies I read: CHS's reference [NS94], Wellens DA's
reference [15], and Chang–Fang's reference [23].)

**Retrieval status — split, read carefully.**

* The **1994 print itself: [BLOCKED]**. Rungs tried, all failed:
  (1) arXiv / ECCC — no version exists (the paper predates routine posting;
  searched by title and by author);
  (2) author homepage — `https://www.cs.huji.ac.il/~noam/` fetched, no
  reachable publication list;
  (3) DOI / aggregators — `link.springer.com/article/10.1007/BF01263419`
  returns HTTP 303 to `idp.springer.com` (paywall);
  `dl.acm.org/doi/pdf/10.1145/129712.129757` returns **HTTP 403**;
  `researchgate.net/publication/2508255` returns **HTTP 403**; the Semantic
  Scholar record exposes no free PDF;
  (4) restatements — succeeded, see next bullet.
* The **junta bound: [RESTATED]**, from two intermediaries whose pages I read
  as page images:
  - **Chiarelli–Hatami–Saks, arXiv:1801.08564v3, p. 1** [READ]: "*Nisan and
    Szegedy [NS94], proved that $R(f)$ is at most at most
    $\deg(f)\cdot 2^{\deg(f)-1}$.*" (the doubled "at most" is in the print).
  - **Wellens, Discrete Analysis 2022:19, p. 1, eq. (1.1)** [READ]:
    "*Nisan and Szegedy [15] proved a similar upper bound on $n(f)$ in terms
    of the degree of $f$, namely* $n(f)\le \deg(f)\cdot 2^{\deg(f)-1}$".
  - **Wellens, arXiv:1903.08214v2, p. 1, Theorem 1** [READ], stated with
    full hypotheses (this is the form to quote):
    "**Theorem 1** (Nisan-Szegedy [4]). *A function
    $f:\{0,1\}^n\to\{0,1\}$ with degree $d$ has at most
    $\frac{d}{2}\cdot 2^d$ relevant variables.*"
* **Internal numbering: only partially recovered.** No intermediary I read
  attaches a theorem number in NS94 to the junta bound; both restate it by
  content. What *is* attested is NS94's **Lemma 2.6** = the non-vanishing /
  support lemma $\Pr_x[p(x)\ne 0]\ge 2^{-\deg p}$ for nonzero multilinear
  real $p$ — cited as "[23, Lemma 2.6]" by Chang–Fang, arXiv:2510.13705v3,
  p. 2 [READ], and as "[NS94, Lemma 2.6]" inside KKDWY26 (already carded,
  card S5 item T9/R3). **Therefore: cite the junta bound by content through
  S6b/S6c, never as "[NS94, Theorem k]".**

**Verbatim statement (LaTeX; the printed forms of the intermediaries).**

```latex
% Wellens, arXiv:1903.08214v2, Theorem 1, p. 1:
A function $f:\{0,1\}^n\to\{0,1\}$ with degree $d$ has at most
$\tfrac{d}{2}\cdot 2^d$ relevant variables.

% equivalently, CHS p.1 / Wellens DA (1.1) p.1:
R(f)\ \le\ \deg(f)\cdot 2^{\deg(f)-1}.
```

**The engine, which is sharper than the bound and is what the rung actually
needs.** Wellens, arXiv:1903.08214v2, **p. 3, eq. (1)** [READ], attributed
there to [4] = NS94:

```latex
\mathrm{Inf}_i[f]\ \ge\ 2^{\,1-\deg_i(f)} .
```

Here (Wellens p. 2) $\mathrm{Inf}_i[f]:=\Pr_x[f(x)\ne f(x^{\oplus i})]$ and
$\deg_i(f)$ is the largest degree of a monomial of $f$ containing $x_i$; so
$\deg_i(f)\le\deg(f)$ and every relevant coordinate has
$\mathrm{Inf}_i[f]\ge 2^{1-d}$. Wellens p. 1 also prints the whole NS
argument: "*a polynomial of degree $d$ has total influence at most $d$, and
yet the derivative in the direction of a relevant coordinate is a degree
$d-1$ polynomial which is not identically zero, so it is non-zero on a random
input with probability at least $1/2^{d-1}$ … so there can be at most
$d\cdot 2^{d-1}$ of them.*"

**Hypotheses itemised.**
1. $f$ TOTAL and Boolean-valued on the full cube. ✔ for our
   $\mathbf 1_A$ (a set indicator is total and $\{0,1\}$-valued).
2. Degree = degree of the multilinear representation over $\{0,1\}^n$.
   ✔ via shared convention 1 (printed).
3. "Relevant" = appears in a monomial with nonzero coefficient (CHS p. 1)
   = $f$ genuinely depends on the coordinate (Wellens DA p. 3). The two
   definitions coincide; ✔ and unaffected by normalization (convention 3).
4. Nothing is assumed about $n$; the bound is $n$-free. ✔ — this is why the
   result is dangerous for the rung: it is exactly the kind of $N$-free
   statement I02 admits.
5. **Value range and cube convention:** printed for $\{0,1\}\to\{0,1\}$;
   ✔ for us via shared conventions 1–2, at the price of one elementary
   affine remark that is *not* printed in these sources.
6. ⚠ **Influence convention differs from the Contract's** and must be
   converted; see the dictionary below. Getting this wrong by a factor 4 or
   by a factor $\alpha$ is the likeliest citation defect on this card.

**Influence dictionary (SCOUT'S OWN elementary computation — verify before
use; not printed in any of S6a–S6d).** Let $A\subseteq\{\pm1\}^N$ be
nonempty, $\alpha=|A|/2^N$, $f=\mathbf 1_A/\sqrt\alpha$ the normalized
member of $\mathcal C^{\mathrm{ind}}_d$, and $\mathrm{Inf}_i$ the Contract's
Fourier influence.
* $\mathrm{Inf}^{\text{Wellens}}_i[\mathbf 1_A]=\Pr[\,\mathbf 1_A(x)\ne
  \mathbf 1_A(x^{\oplus i})\,] = 4\sum_{S\ni i}\widehat{\mathbf 1_A}(S)^2
  = 4\,\mathrm{Inf}_i(\mathbf 1_A)$ (via $g=1-2\mathbf 1_A$, for which
  $\widehat g(S)=-2\widehat{\mathbf 1_A}(S)$ at $S\ne\emptyset$).
* Hence for every coordinate $i$ relevant for $A$:
  $\mathrm{Inf}_i(\mathbf 1_A)\ \ge\ 2^{-1-d}$, with **equality** when $A$ is
  a subcube of codimension $d$ (check: $A=\{x:x_1=\dots=x_d=1\}$ has all
  coefficients $2^{-d}$ on $2^{d-1}$ sets containing $1$).
* After normalization: $\mathrm{Inf}_i(f)=\mathrm{Inf}_i(\mathbf
  1_A)/\alpha\ \ge\ 2^{-1-d}/\alpha\ \ge\ 2^{-1-d}$ (as $\alpha\le1$).
* And $\sum_i\mathrm{Inf}_i(f)\le d$ (I02's free elementary fact). Combining
  the last two: $f$ has at most $d\,2^{1+d}\alpha$ relevant coordinates —
  an $\alpha$-refined junta bound, tight for subcubes ($\alpha=2^{-d}$ gives
  $\le 2d$). Recorded as a lead, **unverified**.

**Conclusion in my own words.** A total Boolean function whose real
multilinear degree is at most $d$ cannot depend on more than $d\,2^{d-1}$
of its inputs, no matter how many inputs it has; the reason is that a
coordinate it depends on must carry flip-probability at least $2^{1-d}$,
while the whole function has only $d$ units of total influence to spend.

**What it does NOT say.**
* It gives **no bound below $2^{1-d}$** on anything: the per-coordinate
  quantum *is* $2^{-\Theta(d)}$ and is attained (AND of $d$ variables:
  each of its $d$ relevant coordinates has $\mathrm{Inf}_i[f]=2^{1-d}$
  exactly). So no sharpening of NS's argument can produce a $1/\mathrm{poly}(d)$
  per-coordinate floor.
* Nothing about *distributions* over functions, nothing about pairs or
  families of functions, nothing about cross-disjointness, nothing about
  $\ell_2$ norms, nothing about groups other than $\mathbb Z_2$.
* Nothing about *average-over-a-distribution* influence, which is R2's
  hypothesis: the bound is per-function.
* It does not say the junta is on a *canonical* or *small* coordinate set —
  only that the relevant set is finite and $n$-free.

**Where the campaign uses it.** Only to *delimit*: it is the statement I02's
"trap" section names. See the shared "Where the campaign uses this" section
after S6d.

### END OF CARD S6a ###

---

### SOURCE CARD [S6b] ###

**Citation.** John Chiarelli, Pooya Hatami, Michael Saks, *An Asymptotically
Tight Bound on the Number of Relevant Variables in a Bounded Degree Boolean
Function*, **Combinatorica 40 (2020), no. 2, 237–244**, DOI
10.1007/s00493-019-4136-7 (journal data via DBLP [READ]; the Springer page
itself is paywalled, HTTP 303 to `idp.springer.com`). Preprint read:
**arXiv:1801.08564v3** (19 Nov 2018), 6 pages.

**Retrieval status. [READ]** — full v3 PDF fetched from
`arxiv.org/pdf/1801.08564` and all 6 pages read as page images on
2026-08-27. Statements below transcribed from the print; page numbers are
the arXiv v3 pages. ⚠ Theorem *numbering* is verified only for the arXiv
version; the Combinatorica version may renumber.

**Verbatim statements (LaTeX).**

```latex
% Abstract, p. 1:
We prove that there is a constant $C\le 6.614$ such that every Boolean
function of degree at most $d$ (as a polynomial over $\mathbb{R}$) is a
$C\cdot 2^d$-junta, i.e. it depends on at most $C\cdot 2^d$ variables.
This improves the $d\cdot 2^{d-1}$ upper bound of Nisan and Szegedy
[Computational Complexity 4 (1994)].

% Theorem 1.1, p. 2:
There is a positive constant $C$ so that $R(f)2^{-\deg(f)}\le C$ for all
Boolean functions $f$, and thus $C_d\le C$ for all $d\ge 0$. In particular
$C^*$ is finite.

% Theorem 3.1, p. 4:
3/2 \le C^* \le 6.614.

% Lemma 1.2, p. 2:
C_d - C_{d-1} \le h_d 2^{-d},
% "which immediately implies $C_d\le\sum_{i=1}^d h_i2^{-i}$."

% Lemma 1.3, p. 2:
For any boolean function $f$, $h(f)\le d(f)^3$ and so for all $i\ge 1$
$h_i\le i^3$.
```

**Definitions the statements depend on (p. 1–2, verbatim in substance).**
$f:\{0,1\}^n\to\{0,1\}$; $\deg(f)$ = min degree of a real polynomial
agreeing with $f$ on $\{0,1\}^n$ = degree of its multilinear
representation; "*An input variable $x_i$ is relevant for a Boolean
function $f$ if it appears in a monomial of the multilinear representation
of $f$ with nonzero coefficient*"; $R(f)$ = number of relevant variables;
"*$f$ is a $t$-junta if $R(f)\le t$*"; $R_d=\max\{R(f):\deg f\le d\}$;
$C_d=R_d2^{-d}$; $R_d\ge 2R_{d-1}+1$ so $C_d\ge C_{d-1}+2^{-d}$ is
increasing, $C^*=\lim C_d\ge1$. A *maxonomial* is a monomial set
$S\subseteq[n]$ with $|S|=\deg(f)$ and nonzero coefficient; a *maxonomial
hitting set* $H$ meets every maxonomial; $h(f)$ = minimum size of one;
$h_d=\max\{h(f):\deg f\le d\}$. The proof's potential is
$W(f)=\sum_i 2^{-\deg_i(f)}$, $\deg_i(f)$ = max degree of a monomial
containing $x_i$; Proposition 2.1 (p. 3): $C_d=W_d$.

**Hypotheses itemised.** Identical to S6a's 1–5 (same conventions, same
paper family) — total, Boolean-valued, $\{0,1\}^n$, multilinear real
degree, $n$-free. ✔ for all of $\mathcal C^{\mathrm{ind}}_d$ via the
shared conventions. **One numbering trap:** Theorem 1.1 asserts only that
*some* finite $C$ works; the numeric $6.614$ is Theorem 3.1 (as an upper
bound on $C^*$) plus the monotonicity $C_d\le C^*$. Quoting "Theorem 1.1
gives $6.614$" is a citation defect.

**Conclusion in my own words.** The $d$-factor in Nisan–Szegedy is
removable: the number of relevant variables of a degree-$d$ Boolean
function is at most an absolute constant times $2^d$, and that constant is
at most $6.614$. The mechanism is a change of potential — weight each
variable by $2^{-\deg_i(f)}$ instead of by its influence — which behaves
almost additively under restricting a maxonomial hitting set.

**What it does NOT say.** Nothing about distributions, pairs, families,
cross-disjointness, indicators, norms, or non-$\mathbb Z_2$ groups; no
lower bound on influence beyond what S6a already gives; and (relevant to
R3) **nothing about non-Boolean-valued functions** — the whole argument
needs $f$ two-valued, since $\deg_i$ and maxonomial hitting sets are used
through the restriction identity $f=x_jf_1+(1-x_j)f_0$ with $f_0,f_1$
again Boolean. It does not determine $C^*$.

**Where the campaign uses it.** Delimiting only; see below.

### END OF CARD S6b ###

---

### SOURCE CARD [S6c] ###

**Citation, and this is the one to quote for the sharpest bound.** Jake
Wellens, *Relationships between the number of inputs and other complexity
measures of Boolean functions*, **Discrete Analysis 2022:19, 21 pp.**, DOI
10.19086/da.57741 (received 29 May 2020, revised 17 Apr 2021, published 23
Dec 2022; CC-BY). Preprint identity: **arXiv:2005.00566v2**. A separate,
earlier, apparently **unpublished** note by the same author —
arXiv:1903.08214v2, *A tighter bound on the number of relevant variables in
a bounded degree Boolean function*, 8 pp. — proves the weaker constant
$4.416$ and is **not in DBLP**; prefer the journal paper.

**Retrieval status. [READ]** — pages 1–3 of the Discrete Analysis version
(arXiv:2005.00566v2 PDF, journal-formatted) read as page images; pages 1–4
of arXiv:1903.08214v2 likewise read. All statements below are transcribed
from those pages.

**Verbatim statements (LaTeX).**

```latex
% Discrete Analysis 2022:19, Theorem 1.1, p. 2:
For any Boolean function $f$,
\[ n(f) \;\le\; 4.394\cdot 2^{\deg(f)}, \tag{1.3} \]
\[ n(f) \;\le\; \tfrac12\cdot 4^{C(f)}. \tag{1.4} \]
Moreover, if $f$ is monotone, then
\[ n(f)\;\le\;\min\Bigl\{\,1.325\cdot 2^{\deg(f)},\ \tfrac12\cdot4^{s(f)},\
   \tfrac14\cdot 2^{\mathrm{DT}(f)}+2\,\Bigr\}. \]

% arXiv:1903.08214v2, Theorem 3 (Main result), p. 2 (the weaker constant):
A function $f:\{0,1\}^n\to\{0,1\}$ with degree $d$ has at most
$(4.416)\cdot 2^d$ relevant variables.
```

**Definitions (Discrete Analysis, p. 3, verbatim in substance).** "*All
functions $f$ in this paper will be assumed to be Boolean valued on
$\{0,1\}^n$.*" $\mathrm{Rel}(f)$ = the set of $i\in[n]$ for which there
exists a pair of inputs $(x,x')$ agreeing off coordinate $i$ with
$f(x)\ne f(x')$; $n(f):=|\mathrm{Rel}(f)|$. $\deg(f)$ = degree of the
multilinear polynomial expansion over $\{0,1\}^n$. $C(f)$ certificate
complexity, $s(f)$ sensitivity, $\mathrm{DT}(f)$ decision-tree depth.

**Hypotheses itemised.**
1. Total, Boolean-valued, on $\{0,1\}^n$. ✔ for us (shared conventions).
2. Multilinear real degree. ✔.
3. $n$-free. ✔.
4. ⚠ The monotone clause ($1.325\cdot 2^{d}$) requires **monotonicity**,
   which our $\mathbf 1_A$ need not have — do not use the monotone constant
   for $\mathcal C^{\mathrm{ind}}_d$.
5. ⚠ (1.4) is in terms of certificate complexity, a different measure; do
   not mix it with the degree bound.

**Also printed here and worth recording (p. 1–2).** The paper's own
statements of the earlier bounds: (1.1) $n(f)\le\deg(f)2^{\deg(f)-1}$
[NS94]; (1.2) $n(f)\le 6.614\cdot 2^{\deg(f)}$ [CHS]; and, p. 2, "*in [4],
the authors also give an example with $n(f)\ge 1.5\cdot 2^{\deg(f)}-2$*".
Also p. 2: the largest known separations come from **Wegener's monotone
address function**, with
$n(f)=\Theta\bigl(2^{\deg(f)}/\sqrt{\deg(f)}\bigr)$ — note this is *below*
$1.5\cdot2^{d}$ and so does not improve the lower bound on $C^*$; and
Theorem 1.2 (p. 2), $\mathrm{bs}(f)\le\sqrt{2/3}\deg(f)^2+1$, a constant-factor
improvement on NS's block-sensitivity inequality (not used by us).

**Conclusion in my own words.** The best printed junta bound for a
degree-$d$ Boolean function is $4.394\cdot 2^{d}$ relevant variables; for
monotone functions $1.325\cdot2^{d}$. The improvement over CHS comes from
tracking block sensitivity through the restriction process and from
computing the small-$d$ block-sensitivity-vs-degree bound exactly rather
than using $\mathrm{bs}\le\deg^2$.

**What it does NOT say.** As S6b: nothing distributional, nothing about
pairs or families, nothing about indicators or norms, nothing outside
$\mathbb Z_2$, nothing for non-Boolean-valued functions. It does not close
the constant: the paper explicitly calls closing these gaps "*a fundamental
challenge left open by our work*" (p. 2).

**Where the campaign uses it.** This is the number to put in I02's trap
paragraph: $M(d)\le 4.394\cdot 2^{d}$.

### END OF CARD S6c ###

---

### SOURCE CARD [S6d] ###

**The lower bound on $M(d)$ — the block that makes I02's trap unavoidable.**

**Citation.** Chiarelli–Hatami–Saks, as S6b: **arXiv:1801.08564v3,
Theorem 3.1 (p. 4) and §3 (pp. 4–5)**; Combinatorica 40 (2020) 237–244.
Independent discovery credited in the print to **Igor Shinkar and Avishay
Tal, 2017, private communication** ([ST17] in the bibliography, p. 6) — so
there is no second citable paper for it.

**Retrieval status. [READ]** — pages 4–5 of arXiv:1801.08564v3 as page
images.

**Verbatim statements (LaTeX).**

```latex
% Theorem 3.1, p. 4 (the lower half is the content here):
3/2 \le C^* \le 6.614.

% Abstract, p. 1:
The bound of $C\cdot 2^d$ is tight up to the constant $C$ as a lower bound
of $2^d-1$ is achieved by a read-once decision tree of depth $d$. We
slightly improve the lower bound by constructing, for each positive
integer $d$, a function of degree $d$ with $3\cdot 2^{d-1}-2$ relevant
variables. A similar construction was independently observed by Shinkar
and Tal.

% §3, p. 4 (the witness):
We lower bound $C^*$ by exhibiting, for each $d$ a function $\Xi_d$ of
degree $d$ with $l(d)=\tfrac32 2^d-2$ relevant variables. ... It is more
convenient to switch our Boolean set to $\{-1,1\}$.

% §3, p. 5 (the construction, verbatim):
We define $\Xi_d:\{-1,1\}^{l(d)}\to\{-1,1\}$ as follows.
$\Xi_1:\{-1,1\}\to\{-1,1\}$ is the identity function and for all $d>1$,
$\Xi_d$ on $l(d)=2l(d-1)+2$ variables is defined in terms of $\Xi_{d-1}$
as follows:
\[ \Xi_d(s,t,\vec x,\vec y)=\frac{s+t}{2}\Xi_{d-1}(\vec x)
   +\frac{s-t}{2}\Xi_{d-1}(\vec y) \]
for all $s,t\in\{-1,1\}$ and $\vec x,\vec y\in\{-1,1\}^{l(d-1)}$.
```

The print then verifies, in one paragraph I read (p. 5): $\deg\Xi_d=1+
\deg\Xi_{d-1}=d$ by induction; $\Xi_d$ **depends on all of its variables**;
and $\Xi_d(s,t,\vec x,\vec y)$ equals $s*\Xi_{d-1}(\vec x)$ if $s=t$ and
$s*\Xi_{d-1}(\vec y)$ if $s\ne t$, hence is $\{\pm1\}$-valued. (This is the
address/select-type recursion the errand asked about: two "address" bits
$s,t$ choose which of two recursive copies to read. $l(1)=1$,
$l(d)=2l(d-1)+2$ gives $l(d)=3\cdot 2^{d-1}-2$.)

**Hypotheses itemised.** None to satisfy — this is a *construction*, so it
is a lower bound we cannot escape rather than a tool we must qualify. Two
facts to record about the witness:
1. It is printed on $\{-1,1\}^{l(d)}$ with $\{-1,1\}$ values — i.e. the
   witness lives natively in **our** cube. Its $\{0,1\}$-valued avatar
   $(1-\Xi_d)/2$ has the same degree $d$ (shared convention 2), so
   **$\Xi_d$ certifies the lower bound for our class**
   $\mathcal C^{\mathrm{ind}}_d$ too: the set
   $A_d=\Xi_d^{-1}(-1)\subseteq\{\pm1\}^{l(d)}$ is a degree-$d$ set whose
   indicator depends on all $3\cdot2^{d-1}-2$ coordinates.
2. $\Xi_d$ is **balanced-ish and dense** ($\alpha\approx 1/2$), not sparse;
   the $\alpha$-refined bound in S6a's dictionary is therefore not violated.

**Conclusion in my own words.** There are degree-$d$ Boolean functions
depending on $3\cdot2^{d-1}-2\approx 1.5\cdot 2^d$ variables (and a much
simpler read-once decision tree gives $2^d-1$), so the exponential
$2^{d}$ in the junta bound is genuine and only the constant is in question:
$1.5 \le \liminf M(d)2^{-d} \le \limsup M(d)2^{-d}\le 4.394$.

**What it does NOT say.** It does not give a *sequence of pairs* of
cross-disjoint sets, nor anything about influences of $\Xi_d$; it is a
single-function witness, and the campaign must not read it as a refutation
witness for R2. It does not determine $C^*$; I searched for improvements to
$3/2$ and found none in print (see report §D).

**Where the campaign uses it.** This is the block that converts I02's trap
from "our bound is weak" into "no bound can help".

### END OF CARD S6d ###

---

## Where the campaign uses this (all four blocks together)

**1. The trap in I02 is REAL, and the printed record closes it.** Setting
$M(d)=R_d$:
$$3\cdot 2^{d-1}-2\ \le\ M(d)\ \le\ 4.394\cdot 2^{d}.$$
The upper bound (S6c) legitimises the trap's premise: every
$f\in\mathcal C^{\mathrm{ind}}_d$ *is* a $\lfloor 4.394\cdot2^d\rfloor$-junta,
uniformly in $N$, with no hypothesis failing (shared conventions). The
lower bound (S6d) makes the trap unavoidable: **any** route that replaces
R1's window size $d$ by the junta size is capped at
$$\delta(d)\ \approx\ \frac{1}{2M(d)}\ \le\ \frac{1}{3\cdot2^{d}-4}\ =\
\Theta(2^{-d}),$$
which is $2^{-\Theta(d)}$ for every conceivable future improvement of the
constant. Sharpening of I02's wording, for the record: such a route would
yield at best $\Theta(2^{-d})$, i.e. it would strip only the $1/d$ from
card S1's $K1=2^{-d}/d$ (indeed $1/(2\cdot4.394\cdot2^d)\approx
0.114\cdot2^{-d}$ beats $2^{-d}/d$ for $d\ge 9$) — a constant-factor gain
inside the exponential regime, **not** progress on R2. An artifact taking
this route is a PARTIAL and must declare the threshold.

**2. The deeper barrier, which the junta count only reflects.** The
per-coordinate quantum, not the coordinate count, is the real obstruction
(S6a's engine): every coordinate a degree-$\le d$ Boolean function depends
on carries influence $\ge 2^{-1-d}$ (Fourier normalisation, un-normalized
indicator), and this is **attained** by $\mathrm{AND}_d$ / codimension-$d$
subcubes. Consequently any R2 argument of the shape "identify the
coordinates the functions *use*, then pay per used coordinate" is
structurally capped at $2^{-\Theta(d)}$, because "used" costs $2^{-\Theta(d)}$
and there are $2^{\Theta(d)}$ of them, and both exponentials are tight. A
proof of R2 must therefore charge against something other than
per-coordinate usage — consistent with I02's instruction to charge against
the *total influence budget* $\sum_i\mathrm{Inf}_i(f)\le d$, or (see the
report and card S7) against a **degree-sized projection obstruction**
rather than the junta.

**3. R3 compatibility (I02's binding generalization hypothesis).** All of
S6a–S6c require $f$ to be **two-valued**; their machinery (maxonomial
hitting sets, $\deg_i$, restriction into Boolean functions) does not survive
to nonnegative real degree-$d$ functions. So the junta route is doubly
disqualified: exponential *and* non-liftable. Card **S7** records the one
mechanism found that is both poly($d$) and field-agnostic.

**4. Do not cite by number where the number is unverified.** Use S6c's
Theorem 1.1 (1.3) for the sharpest bound; use S6b's abstract or
Theorem 3.1 for $6.614$ (not Theorem 1.1); cite NS94 by content via S6a,
never as "[NS94, Theorem k]" — the only NS94 number this campaign has
verified is **Lemma 2.6** (the $\Pr[p\ne0]\ge2^{-\deg p}$ lemma, already
carded as S5/T9-R3).

### END OF ARTIFACT S6-junta-degree ###
