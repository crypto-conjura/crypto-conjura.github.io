# id: S3-2026-bypass-lemmas
# agent: Scout (source-request resolution, campaign c/0023)
# model: claude-fable-5
# cycle: 2 (post-strategist source gate); status: COMPLETE

Resolves the Strategist's SOURCE REQUEST (artifact `0023-strategist-1`, ranks 1
and 2). One file, two cards.

**Upgrade to [READ], 2026-08-27 (same day, second pass).** The human uploaded
both PDFs (`2504.05710v2.pdf`, `2608.03824v1.pdf`) in response to this card's
residual source request; the orchestrator read both statements and both proofs
directly from the page images. Every clause previously carded from extraction
matches the printed text word-for-word; page numbers and proof internals are
now filled in below. Both cards are therefore **[READ]** (retrieval history:
first pass 2026-08-27 by Scout at [RESTATED] grade via two cross-checked arXiv
HTML extractions; the extractions proved accurate).

---

### SOURCE CARD [S3a] ###

**Citation.** Longcheng Li, Qian Li, Xingjian Li, Qipeng Liu, *Impossibility
of Perfectly Complete Many-Round Key Agreement in the QROM*, arXiv:2608.03824
(v1, 4 Aug 2026), **Lemma 3.5 ("Disjoint-support separator"), §3.4, statement
p. 7, proof pp. 7–8**. §3's numbered results: Thm 3.1 main theorem (p. 5),
Lem 3.2 transcript rectangularity (p. 6), Lem 3.3 disjoint key supports
(p. 6), Lem 3.4 few candidate keys (p. 7), Lem 3.5 this one; no Lem 3.6.
Applied in §3.5 ("The Eavesdropper", p. 9) inside the proof of Theorem 3.1.

**Retrieval status.** [READ — PDF `2608.03824v1.pdf`, uploaded by the human
2026-08-27, statement and full proof read from the page images]. The
parenthetical name "(Disjoint-support separator)" is the paper's own (p. 7);
citable. The prior extraction-grade quotes matched the PDF verbatim.

**Verbatim statement (LaTeX, confirmed against the PDF, p. 7).**

```latex
Let $p,q\colon\{0,1\}^N\to\mathbb{R}$ be multilinear polynomials of degree at
most $d$ such that
\[ p(z)\,q(z)=0 \quad\text{for every } z\in\{0,1\}^N. \]
There is a deterministic decision tree of depth $O(d^4)$ which, under the
promise $p(z)+q(z)\neq 0$, determines whether $p(z)\neq 0$ or $q(z)\neq 0$.
```

**Proof mechanism (READ, pp. 7–8) — carded because the campaign's P2 plan may
need the recursion, not just the statement.** Recursive tree. At a node,
restrict $p,q$ by the answers so far; $S \subseteq [N]$ the unqueried
variables. If both restrictions $\equiv 0$: no promised input reaches this
subcube, label arbitrarily. If exactly one $\equiv 0$: label with the other
side. Otherwise let $D = \max(\deg p, \deg q) \ge 1$ ($D = 0$ is impossible:
two nonzero constants cannot have disjoint supports) and set $s = p^2 - q^2$,
$\deg s \le 2D$, $s \not\equiv 0$. Pick $z^\star \in \{0,1\}^S$ maximizing
$|s(z^\star)|$ (so $|s(z^\star)| > 0$ and exactly one of $p(z^\star),
q(z^\star)$ is nonzero); WLOG $p(z^\star) \ne 0$, so $s(z^\star) > 0$ and
$q(z^\star) = 0$. Take a maximal family of pairwise-disjoint maximum
monomials of $q$ with supports $M_1, \dots, M_b$ ($b \ge 1$). For each $i$:
fixing everything outside $M_i$ to $z^\star$ preserves the maximum monomial's
coefficient, so the restriction to $M_i$'s variables is nonzero, and since
$q(z^\star) = 0$ there is a nonempty $E_i \subseteq M_i$ with
$q((z^\star)^{E_i}) \ne 0$ (superscript = flip those coordinates); disjoint
supports then force $s((z^\star)^{E_i}) < 0$. Define $r : \{0,1\}^b \to
\mathbb{R}$, $r(y) = s((z^\star)^{\cup_{i: y_i = 1} E_i}) / |s(z^\star)|$;
block-disjointness gives $\deg r \le \deg s \le 2D$, and maximality of
$|s(z^\star)|$ gives $|r| \le 1$, $|r(0^b)| = 1$, $r(y) \cdot r(0^b) \le 0$
for $|y| = 1$. The paper's Lemma 2.3 (p. 5, from [KKDWY26], statement printed
in full there: any such $r$ has $\deg r \ge \sqrt{b/2}$) then yields
$\sqrt{b/2} \le 2D$, i.e. **$b \le 8D^2$ — the constant is explicit at this
step**. Query all of $M_1 \cup \dots \cup M_b$ (at most $bD \le 8D^3$
variables); by maximality every maximum monomial of $q$ loses a variable, so
on every branch $q|_\rho \equiv 0$ or $\deg(q|_\rho) < \deg q$ (symmetric on
$p$ when $q(z^\star) \ne 0$). Each stage lowers $\deg p + \deg q \le 2d$ by at
least 1, so $\le 2d$ stages of $\le 8d^3$ queries: **depth $\le 16 d^4$
follows from the printed argument** (the bound as printed is $O(d^4)$ with
universal constants; the $16d^4$ arithmetic is ours, assembled from the
printed steps).

**Proof dependencies (all printed in the paper).** Lemma 2.3 = Kothari,
Kovacs-Deak, Wang, Yang, *Rational degree is polynomially related to degree*,
arXiv:2601.08727v2, to appear FOCS 2026 — statement READ from this paper's
p. 5, its proof NOT read (a use depending on the internals of [KKDWY26]
itself would be [SOURCE-BLOCKED: KKDWY26]). Lemma 2.1 = Nisan–Szegedy
support bound ($|\mathrm{supp}(f)| \ge 2^{N-d}$, p. 4). Lemma 2.2 = BBC+01
polynomial method, incl. the postselected-branch extension (p. 4).

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
   $N$-free $\delta$); a concrete bound $\le 16 d^4$ assembles from the
   printed proof steps (see Proof mechanism above).

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
v.s. Minicrypt in a Quantum World*, arXiv:2504.05710 **v2** (1 Jun 2026),
**Lemma 3.4, §3.2, statement p. 13, proof p. 14** (§3's other numbered
results: Lem 3.1 entropy bound on quantum algorithm output, p. 13; Lem 3.3
repetition decreases conditional mutual information, p. 13; no Lem 3.5). Not
named "win-win" in the statement; §1.3's technical overview (p. 6) titles the
idea "Compute the partial assignment: a win-win argument", and the lemma's
own preamble (p. 13) calls it "a win-win situation".

**Retrieval status.** [READ — PDF `2504.05710v2.pdf`, uploaded by the human
2026-08-27, statement and full proof read from the page images]. The prior
extraction-grade quotes matched the PDF verbatim.

**Supporting definitions (verbatim, as extracted).** A partial assignment is a
function $\mu\colon[N]\to\{0,1,\star\}$; $x^\mu$ is the string
$x'\in\{0,1\}^N$ with $x'_i:=\mu(i)$ if $i\in\operatorname{supp}(\mu)$ and
$x'_i:=x_i$ otherwise; the product $\mu\cdot\eta$ is the partial assignment
with $x^{\mu\cdot\eta}=(x^\mu)^\eta$ for all $x$ (so in $\mu_\ell\cdot\mu$
below, $\mu$ is applied second and wins on overlaps). $\deg(f)$ is the degree
of $f$'s multilinear polynomial expression.

**Verbatim statement (LaTeX, confirmed against the PDF, p. 13).**

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

**Proof mechanism (READ, p. 14).** Iterative; maintain $\tilde f = f$,
$\tilde\mu = \emptyset$; at most $\deg(f)$ rounds. Each round: build a
maximal set $\mathcal{S}$ of pairwise-disjoint maximum monomials of
$\tilde f$. If $|\mathcal{S}| > m$: stop and return $\tilde\mu$ — case (b)
holds because for each of the $> m$ disjoint maximum monomials, the paper's
Lemma 2.12 (p. 11, from [Mid04]: for any nonzero $f$, any maximum monomial
$x_S$, and any $x$, some $\mu$ with $\mathrm{supp}(\mu) = S$ has
$f(x^\mu) \ne 0$) supplies the small disjoint certificate. Otherwise fix all
variables appearing in $\mathcal{S}$ one at a time, each time choosing the
bit that keeps $\tilde f \not\equiv 0$ (always possible); update $\tilde\mu
\leftarrow \tilde\mu \cdot \eta$, $\tilde f \leftarrow \tilde f^\eta$. By
maximality every maximum monomial meets $\mathcal{S}$, so the degree drops by
$\ge 1$ per fixing round; if $\deg \tilde f = 0$ then $\tilde f \equiv c \ne
0$ and case (a) holds. Size: $\le d$ rounds $\times \le md$ variables $=
md^2$. Dependency: Lemma 2.12 = Midrijanis, quant-ph/0403168 (statement READ
from this paper's p. 11; [Alo99] is cited alongside it in the overview).

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

**Consistency note for downstream verifiers (class D checks).** Both cards
are now [READ]: statements and proofs were read directly from the
human-uploaded PDFs on 2026-08-27, and the earlier extraction-grade quotes
matched the printed text exactly. The former [SOURCE-BLOCKED] caveat on
Lemma 3.5's recursion and constant is lifted (see the Proof mechanism
sections). Two residual blocks remain, one level deeper: a step that depends
on the *internals* of [KKDWY26] (arXiv:2601.08727v2 — only its statement is
printed in 2608.03824) or of [Mid04] (quant-ph/0403168 — only its statement
is printed in 2504.05710v2) is [SOURCE-BLOCKED: KKDWY26] resp.
[SOURCE-BLOCKED: Mid04] until those papers are read themselves.

**Context also read while carding (not separately carded).** 2608.03824's
full attack structure: Thm 3.1 ($O((q_A+q_B)^5)$ classical queries, key
recovered with certainty; d = min(2(q_A+q_B), N)); Lem 3.2 transcript
rectangularity via Stinespring purification of the QCCC protocol; Lem 3.3
disjoint key supports from perfect completeness; Lem 3.4 $|\mathcal{K}_t| \le
2^d$ candidate keys; §3.5 binary search over keys invoking Lemma 3.5 per
level. The paper states (p. 2) "Perfect completeness is essential to our
argument" and confirms in print that it removes the [ACC22] conjecture
(bypass, not resolution — consistent with the Scout's verdict). Provenance
note printed in the paper (pp. 1, 3): the proof was found by "GPT-5.6 Sol
Ultra" in a one-shot conversation, with the authors independently verifying
every statement.

### END OF ARTIFACT S3-2026-bypass-lemmas ###
