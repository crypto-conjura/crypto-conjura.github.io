# id: S3-2026-bypass-lemmas
# agent: Scout (source-request resolution, campaign c/0023)
# model: claude-fable-5
# cycle: 2 (post-strategist source gate); status: COMPLETE

Resolves the Strategist's SOURCE REQUEST (artifact `0023-strategist-1`, ranks 1
and 2). One file, two cards. Retrieval method for both: prompted extraction of
the arXiv HTML full text via WebFetch (the extractor was instructed to quote
verbatim, twice per lemma with independently phrased prompts; the two passes
agreed word-for-word on every quoted clause). I did not view the raw page or
PDF myself, so both cards are tagged **[RESTATED]**, not [READ], per protocol.
Access-ladder rungs tried: arXiv abs pages (metadata only); arXiv HTML full
text (extraction succeeded, twice each); no PDF read.

---

### SOURCE CARD [S3a] ###

**Citation.** Longcheng Li, Qian Li, Xingjian Li, Qipeng Liu, *Impossibility
of Perfectly Complete Many-Round Key Agreement in the QROM*, arXiv:2608.03824
(v1, Aug 2026), **Lemma 3.5, §3** (page numbers unavailable in the HTML
rendering; §3's numbered results are Thm 3.1 main theorem, Lem 3.2 transcript
rectangularity, Lem 3.3 disjoint key supports, Lem 3.4 few candidate keys,
Lem 3.5 this one; no Lem 3.6). Applied in §3.5 ("The Eavesdropper") inside the
proof of Theorem 3.1.

**Retrieval status.** [RESTATED — extraction of arxiv.org/html/2608.03824v1,
two independent verbatim-quote passes in full agreement]. The label
"Disjoint-support separator" appeared in the first extraction's rendering of
the lemma header; whether it is the paper's parenthetical name or the
extractor's gloss is unconfirmed — do not cite the name, cite the number.

**Verbatim statement (LaTeX, as extracted).**

```latex
Let $p,q\colon\{0,1\}^N\to\mathbb{R}$ be multilinear polynomials of degree at
most $d$ such that
\[ p(z)\,q(z)=0 \quad\text{for every } z\in\{0,1\}^N. \]
There is a deterministic decision tree of depth $O(d^4)$ which, under the
promise $p(z)+q(z)\neq 0$, determines whether $p(z)\neq 0$ or $q(z)\neq 0$.
```

Proof opening (extracted, for orientation only — proof not carded): "We
construct the tree recursively. At one node, restrict $p$ and $q$ by the
answers already queried, and let $S\subseteq[N]$ be the set of unqueried
variables."

**Hypotheses, itemised, with PCC-object flags.**

1. $p,q$ are **real-valued multilinear polynomials on $\{0,1\}^N$**.
   ⚠ PCC's objects are $\mathbb{C}$-valued functions on $\mathcal{Y}^N$ for an
   arbitrary finite abelian group: matches only $\mathcal{Y}=\mathbb{Z}_2$,
   and $\mathbb{C}$-valued $f$ must first be split (real/imaginary parts) —
   splitting can break the disjoint-support hypothesis 3 below (supports of
   $\operatorname{Re}f$ and $\operatorname{Im}g$ need not multiply to zero).
2. **Degree at most $d$, both polynomials.** ✔ PCC grants this pointwise on
   both supports.
3. **Pointwise disjoint supports: $p(z)q(z)=0$ for every $z$.** ✔ exactly the
   shape of a PCC-incompatible pair $(f,g)$ with $fg\equiv 0$; note this is a
   *hypothesis* here, so the lemma is a tool for reasoning about would-be
   counterexample pairs, not for producing the conjectured common nonzero
   point.
4. **Promise $p(z)+q(z)\neq 0$ at the queried input $z$.** ⚠ PCC provides no
   such promise: an incompatible pair can have (many) common zeros
   $p(z)=q(z)=0$, and there the tree's output is unconstrained. Any transfer
   must control the mass of the common-zero set or condition on avoiding it.
5. **A single fixed pair $(p,q)$.** ⚠ per-function/algorithmic, not
   distributional: PCC quantifies over distributions $\mathbf{F},\mathbf{G}$
   with only *average* per-coordinate influence control; the lemma would have
   to be invoked pair-by-pair on $\operatorname{supp}\mathbf{F}\times
   \operatorname{supp}\mathbf{G}$, with a different tree per pair.
6. No norm hypothesis, no influence hypothesis, no query bound on $N$. ✔ the
   depth $O(d^4)$ is independent of $N$ (favourable — matches PCC's
   $N$-free $\delta$); the constant in $O(d^4)$ is not printed.

**Conclusion in my own words.** If two real multilinear degree-$\le d$
polynomials on the Boolean cube never are simultaneously nonzero, then there
is one fixed deterministic decision tree, of depth polynomial in $d$ alone
(order $d^4$, no $N$ dependence), that reads $O(d^4)$ bits of an unknown input
$z$ and — whenever at least one of the two values $p(z),q(z)$ is nonzero —
correctly names which one it is. Disjointness of supports makes "which one is
nonzero at $z$" a well-defined single-valued promise problem, and the lemma
says this problem has query complexity poly($d$), not poly($N$).

**What it does NOT say.**
- It is **per-pair and algorithmic**, not distributional: nothing about
  distributions over polynomials, expectations, or simultaneity across many
  pairs.
- It **controls no influences and no norms**: neither hypothesis nor
  conclusion mentions $\operatorname{Inf}_i$ or $\|\cdot\|_2$. Any influence
  consequence (e.g. via OSSS applied to the depth-$O(d^4)$ tree) is an
  *inference the campaign must supply and justify*, not content of the lemma.
- It does **not find a nonzero point** of $p$ or $q$, and cannot contradict
  $pq\equiv 0$ — it presupposes it.
- It says nothing off the promise (inputs with $p(z)=q(z)=0$), nothing about
  $\mathbb{C}$-valued functions, and nothing about groups other than
  $\mathbb{Z}_2$.
- The extractor reports the paper **never invokes the Polynomial Compatibility
  Conjecture in this application** (the paper's stated point is removing it).

**Where we use it.** Strategist plan **P2 (class (e) TRANSFER)**, milestone
gate now open: singleton-PCC test — for point masses on an incompatible pair
$(f,g)$ over $\mathbb{Z}_2$ (real-valued first), run the Lemma 3.5 tree and
apply OSSS to the induced tree to try to force some coordinate influence
$\ge 1/O(d^4)$-type bounds, targeting singleton-PCC at $\delta=1/O(d^5)$;
failure must isolate which flagged hypothesis (1, 4, or 5) breaks the
transfer. Flags 4 and 5 above are the expected failure points (Scout
obstruction C4).

---

### SOURCE CARD [S3b] ###

**Citation.** Longcheng Li, Qian Li, Xingjian Li, Qipeng Liu, *Cryptomania
v.s. Minicrypt in a Quantum World*, arXiv:2504.05710 **v2** (June 2026),
**Lemma 3.4, §3** (page numbers unavailable in the HTML rendering; §3's other
numbered results: Lem 3.1 entropy bound on quantum algorithm output, Lem 3.3
repetition decreases conditional mutual information; no Lem 3.5). Not named
"win-win" in the statement; §1.3's technical overview titles the idea "Compute
the partial assignment: a win-win argument".

**Retrieval status.** [RESTATED — extraction of arxiv.org/html/2504.05710v2,
two independent verbatim-quote passes in full agreement].

**Supporting definitions (verbatim, as extracted).** A partial assignment is a
function $\mu\colon[N]\to\{0,1,\star\}$; $x^\mu$ is the string
$x'\in\{0,1\}^N$ with $x'_i:=\mu(i)$ if $i\in\operatorname{supp}(\mu)$ and
$x'_i:=x_i$ otherwise; the product $\mu\cdot\eta$ is the partial assignment
with $x^{\mu\cdot\eta}=(x^\mu)^\eta$ for all $x$ (so in $\mu_\ell\cdot\mu$
below, $\mu$ is applied second and wins on overlaps). $\deg(f)$ is the degree
of $f$'s multilinear polynomial expression.

**Verbatim statement (LaTeX, as extracted).**

```latex
Let $m>0$ be an integer. For any degree-$d$ function
$f\colon\{0,1\}^N\to\mathbb{R}$ that is not identically zero, we can
explicitly construct a partial assignment $\mu$ of $|\mu|\le md^2$ such that:
either
(a) for any $x\in\{0,1\}^N$, $f(x^\mu)\neq 0$; or
(b) for any $x\in\{0,1\}^N$, there must exist $m$ pairwise disjoint partial
assignments $\mu_1,\dots,\mu_m$ of size at most $d$ such that
$f(x^{\mu_\ell\cdot\mu})\neq 0$ for all $\ell\in[m]$.
```

Proof opening (extracted, orientation only): "We propose an algorithm to
construct such a partial assignment $\mu$. The algorithm maintains a function
$\tilde f$ and a partial assignment $\tilde\mu$ ... repeat until
$\deg(\tilde f)=0$."

**Hypotheses, itemised, with PCC-object flags.**

1. **One single function $f$**, real-valued on $\{0,1\}^N$. ⚠ same two flags
   as S3a items 1 and 5: $\mathbb{Z}_2$-and-$\mathbb{R}$ only, and
   per-function rather than distributional. Nothing here couples *two*
   functions, let alone two distributions.
2. **$\deg f\le d$.** ✔ granted on PCC supports.
3. **$f\not\equiv 0$.** ✔ every $f\in\operatorname{supp}(\mathbf{F})$ has
   $\|f\|_2=1$, hence is nonzero.
4. $m$ is a free integer parameter traded against the restriction size
   $md^2$. ✔ no constraint PCC objects could fail.
5. No influence, norm, or distribution hypothesis; explicit/algorithmic
   construction of $\mu$ **from the full description of $f$** (the proof is a
   post-hoc analysis of a fixed function; it contains no oracle-query
   accounting for *finding* $\mu$).

**Conclusion in my own words.** Every nonzero degree-$d$ real polynomial on
the cube admits an explicitly constructible restriction $\mu$ fixing at most
$md^2$ coordinates with a win-win outcome: either restricting by $\mu$ alone
already makes $f$ nonvanishing at *every* point, or else from *every* point
$x$ there are $m$ pairwise-disjoint further restrictions of size $\le d$ each
of which (applied on top of $\mu$) lands $f$ on a nonzero value. Loosely: a
small restriction either kills all zeros of $f$ or manufactures, at every
point, $m$ disjoint low-weight certificates of non-vanishing.

**What it does NOT say.**
- Nothing about **pairs** $(f,g)$, joint restrictions, or a common point
  where two functions are simultaneously nonzero — the exact content PCC
  needs. Applying it separately to $f$ and $g$ gives two restrictions
  $\mu_f,\mu_g$ with no compatibility between them; making them cohere across
  $\operatorname{supp}\mathbf{F}\times\operatorname{supp}\mathbf{G}$ is
  precisely the campaign's open difficulty (Scout C4), not something this
  lemma addresses.
- **No influence control** in hypothesis or conclusion. Case (b)'s $m$
  disjoint small certificates are *suggestive* of block-sensitivity-style
  statements, but the lemma asserts no bound on $\operatorname{Inf}_i$, and
  no such corollary is carded here.
- Not distributional; no $\delta$, no averages, no norms; silent for
  $\mathbb{C}$-valued functions and for groups other than $\mathbb{Z}_2$.
- The construction's explicitness is relative to knowing $f$ exactly; the
  lemma says nothing about query access.

**Where we use it.** Strategist plan **P2**, secondary import: single-function
structural tool for the singleton/support-restricted rungs (e.g. combine with
S3a's tree, or use case (a)/(b) dichotomy to argue a unit-norm low-degree $f$
with all influences $\le\delta$ cannot have its nonzero set confined to a
prescribed small region). Any such use must bridge flag 1 (per-function →
distributional) explicitly.

---

**Consistency note for downstream verifiers (class D checks).** These cards
are extraction-derived. Each quoted clause was returned identically by two
independently phrased extraction passes, but the underlying page was never
read raw by any campaign agent; if a proof comes to *depend on the constant*
inside Lemma 3.5's $O(d^4)$, or on the exact recursion in either proof, that
step is [SOURCE-BLOCKED] until the PDF is read.

### END OF ARTIFACT S3-2026-bypass-lemmas ###
