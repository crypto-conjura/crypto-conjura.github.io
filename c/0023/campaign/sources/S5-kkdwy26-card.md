# id: S5-kkdwy26
# agent: Scout (bounded deciding-source read, campaign c/0023, rung I01)
# model: claude-fable-5
# cycle: 2; status: COMPLETE

Resolves the deciding source named in `../proofs/0023-scout-2.md` §E. One
paper, four carded items (C1, T4, T10+F7, T9/R3), one shared retrieval status.

**Citation.** Robin Kothari, Matt Kovacs-Deak, Daochen Wang, Rain Zimin Yang,
*Rational degree is polynomially related to degree*, arXiv:2601.08727 **v2**
(8 Apr 2026; v1 13 Jan 2026; comments field: "26 pages; v2: added an author,
improved main result" — the abs page does NOT print a venue; the "to appear
FOCS 2026" attribution is inherited from card S3a / 2608.03824 and is not
re-verified here). Main result: $\deg(f)\le\widetilde O(\mathrm{rdeg}(f)^3)$,
in fact $\deg(f)\le\widetilde O(\deg_\pm(f)^2\,\mathrm{rdeg}(f))$, for every
total Boolean $f$.

**Retrieval status.** [READ — full PDF fetched from arxiv.org/pdf/2601.08727v2
on 2026-08-27; all 26 pages read as page images; statements below transcribed
from the print]. Author list note: the fourth author is **Rain Zimin Yang**
(p. 1), not "Yang, R." guessed forms; S3a's short cite "[KKDWY26]" remains
correct.

**Global conventions (p. 2, §2).** Boolean $f\colon\{0,1\}^n\to\{0,1\}$;
$\mathrm{rdeg}(f)$ = min over rational representations $p/q$ ($q\ne 0$ on the
cube, $p/q=f$ pointwise) of $\max(\deg p,\deg q)$ (Def. 2);
$\deg_\pm$ sign degree (Def. 3); $\mathrm{ndeg}$ nondeterministic degree:
min degree of multilinear $p$ with $p(x)\ne 0\iff f(x)=1$ (Def. 4);
Fact 3 (p. 3, with proof): $\mathrm{rdeg}(f)=\max(\mathrm{ndeg}(f),
\mathrm{ndeg}(\neg f))$.

---

## Item C1 — Corollary 1 (p. 4): the discrete-Markov lemma behind S3a

This is the result printed as "Lemma 2.3 [KKDWY26]" in 2608.03824 (card S3a).
Statement AND proof now read at the source; **S3a's residual
[SOURCE-BLOCKED: KKDWY26] on internal uses of Lemma 2.3 is lifted** — cite
this card.

**Verbatim statement (LaTeX, p. 4).**

```latex
Let $p\in\mathbb{R}[X_1,\dots,X_n]$ and $h>0$. Suppose that $p$ has the
following properties:
 (i)   $|p(x)|\le h$ for all $x\in\{0,1\}^n$,
 (ii)  $|p(0^n)| = h$,
 (iii) $p(x)\cdot p(0^n)\le 0$ for all $x\in\{0,1\}^n$ with $|x|=1$.
Then, $\sqrt{n/2}\le \deg(p)$.
```

**Confirmation for S3a.** With $h=1$ this is exactly the statement S3a
carries; the constant $\sqrt{n/2}$ is confirmed, not sharpened. Hence the
$b\le 8D^2$ step and the assembled $\le 16d^4$ depth in S3a's proof-mechanism
section stand on a READ foundation end to end.

**Proof mechanism (READ, p. 4).** WLOG $p(0^n)=h$ and $p\le 0$ at weight 1
(else replace $p$ by $-p$); $p$ multilinear,
$p=a_0+(a_1X_1+\dots+a_nX_n)+\text{higher}$; (ii) gives $a_0=h$, (iii) gives
$a_0+a_i\le 0$, so $a_i\le -h$ for all $i$. Symmetrize (Fact 5, p. 3:
$P(y)=\mathbb{E}_{x\sim B_y^n}[p(x)]$, $\deg P\le\deg p$, $B_y^n$ = i.i.d.
Bernoulli($y$) bits): $|P(y)|\le h$ on $[0,1]$ by (i), and
$P'(0)=a_1+\dots+a_n\le -nh$. Markov's inequality (their Theorem 1, p. 4:
$|P'(x)|\le\frac{b_2-b_1}{a_2-a_1}\deg(P)^2$ for $P$ mapping $[a_1,a_2]$ into
$[b_1,b_2]$) gives $nh\le|P'(0)|\le 2h\deg(P)^2$, so
$\deg(p)\ge\deg(P)\ge\sqrt{n/2}$.

**Hypotheses itemised.** (1) real polynomial on $\{0,1\}^n$ — same
$\mathbb{Z}_2$/real flags as S3a item 1; (2) hypothesis (ii) is that the
value at $0^n$ ATTAINS the global max modulus $h$ of (i) — the easiest clause
to misremember; (3) sign condition (iii) only at Hamming weight exactly 1;
nothing is assumed at weights $\ge 2$. No multilinearity assumed in the
statement (reduced to it WLOG in the proof).

---

## Item T4 — Theorem 4 (p. 7): the result 2608.03824 cites as [KKDWY26, Thm 4]

**Verbatim statement (LaTeX, p. 7).**

```latex
For every Boolean function $f$,
\[ \mathrm{D}(f) \;\le\; 4\deg_\pm(f)^2\,\mathrm{rdeg}(f)^2 \;\le\; 16\,\mathrm{rdeg}(f)^4. \]
```

($\mathrm{D}$ = deterministic decision tree complexity, Def. 7 p. 3; second
inequality via Fact 2, $\deg_\pm(f)/2\le\mathrm{rdeg}(f)$.)

**Proof mechanism (READ, p. 7).** Algorithm 1: repeatedly query a hitting set
of the maximal monomials of a nondeterministic representation $p^i$ of the
current restriction $f^i$ (or of $q^i$ for $\neg f^i$); Corollary 2 (p. 7,
from Lemma 2 p. 5 + Lemma 3 p. 6) guarantees one of the two has a hitting set
of size $\le 2\deg(\cdot)\deg_\pm(f^i)^2$; each round drops $\deg p^i$ or
$\deg q^i$ by $\ge 1$, so $\le 2\,\mathrm{rdeg}(f)$ rounds. The engine under
Corollary 2 is Lemma 2 (p. 5): $\min_{x\in\{0,1\}^n}\mathrm{bs}_x(f)\le
2\deg_\pm(f)^2$, whose proof (p. 6) is exactly the sensitive-block-to-$r$
compression that S3a's Lemma 3.5 reuses, closed by Corollary 1 (Item C1).
No $n$-dependence anywhere in T4 (the improved Theorem 8, p. 16,
$\mathrm{D}(f)\le O(\mathrm{rdeg}(f)\deg_\pm(f)^2\log n)\le
O(\mathrm{rdeg}(f)^3\log n)$, DOES carry a $\log n$ — for the campaign's
$N$-free $\delta$ purposes T4, not T8, is the usable form).

**Hypotheses / flags for I01–R5 transfer.** TOTAL Boolean $f$ only. The
disjoint-support promise problem of a PCC pair is a PARTIAL function, and the
paper itself proves the total-function machinery does NOT extend to partial
functions in general (Fact 7, Item T10 below; footnote 7, p. 18: "rational
degree could be much smaller than degree for partial Boolean functions").
2608.03824's Lemma 3.5 (card S3a) IS the transfer of this proof scheme to the
disjoint-support promise setting; T4 itself adds nothing on top of S3a for
the rung. Consistency check: S3a's assembled $16d^4$ constant coincides with
T4's printed $16\,\mathrm{rdeg}^4$.

---

## Item T10+F7 — Theorem 10 and Fact 7 (p. 18): the paper's only pair-of-disjoint-support statement

**Theorem 10 (Effective Hypercube Nullstellensatz), verbatim (p. 18).**

```latex
Let $g_1,g_2\in\mathbb{R}[X_1,\dots,X_n]$. Suppose $g_1$ and $g_2$ do not
share any common zeros on the hypercube $\{0,1\}^n$. Further suppose
$g_1(x)\cdot g_2(x)=0$ for all $x\in\{0,1\}^n$. Then there exist
$h_1,h_2\in\mathbb{R}[X_1,\dots,X_n]$ such that
\[ h_1(x)g_1(x)+h_2(x)g_2(x)=1 \quad\text{for all } x\in\{0,1\}^n, \]
and
\[ \max\bigl(\deg(\overline{h_1g_1}),\deg(\overline{h_2g_2})\bigr)
   \le \widetilde O\bigl(\deg(g_1)^{1.5}\deg(g_2)^{1.5}\bigr), \]
where the overline denotes multilinearization using
$X_1^2=X_1,\dots,X_n^2=X_n$.
```

**Hypotheses itemised, with I01/R5 flags.**
1. $g_1g_2\equiv 0$ on the cube ✔ — exactly a PCC-incompatible pair shape.
2. **No common zeros: at EVERY cube point at least one $g_i$ is nonzero.** ⚠
   This is the everywhere-promise. An I01/R5 incompatible pair
   $(f,g)=(\mathbf{1}_A/\|\cdot\|,\mathbf{1}_B/\|\cdot\|)$ with $A\cap
   B=\emptyset$ has common zeros on all of $(A\cup B)^c$, which is generally
   almost the whole cube; hypothesis 2 FAILS for the rung's objects except in
   the degenerate covering case $A\cup B=\{0,1\}^N$. Same flag as S3a
   hypothesis 4.
3. Per-pair, real, $\mathbb{Z}_2$ only; no influence, no norms, no
   distributions — same flags as S3a items 1 and 5.

**Fact 7, verbatim (p. 18) — the matching barrier.**

```latex
There exist $g_1,g_2\in\mathbb{R}[X_1,\dots,X_n,Y_1,\dots,Y_n]$ each of
degree $1$ that do not share any common zeros on $\{0,1\}^{2n}$ such that: if
$h_1,h_2\in\mathbb{R}[X_1,\dots,X_n,Y_1,\dots,Y_n]$ satisfy
$h_1(x)g_1(x)+h_2(x)g_2(x)=1$ for all $x\in\{0,1\}^{2n}$, then
$\max(\deg(\overline{h_1g_1}),\deg(\overline{h_2g_2}))\ge n$.
```

(Explicit construction p. 19: $g_1=X_1+\dots+X_n$,
$g_2=X_1+\dots+X_n+Y_1+\dots+Y_n-(n+1)$; proof by Minsky–Papert
symmetrization.) So dropping the disjoint-support hypothesis $g_1g_2\equiv 0$
kills any poly($d$) partition-of-unity bound even at degree 1: **the
$fg\equiv 0$ structure, not the promise alone, is what carries poly($d$)
conclusions** — supporting evidence that P2's reliance on disjointness is the
right axis. Conjecture 1 (p. 18): the $m$-polynomial version of Theorem 10 is
OPEN (conjectured), so no $m$-family Nullstellensatz can be cited.

---

## Item T9/R3 — Theorem 9 + Remark 3 (p. 16): the paper's influence/junta content (exponential regime only)

**Theorem 9, verbatim (p. 16).** "For every $f\colon\{0,1\}^n\to\{0,1\}$ that
depends on all $n$ variables, $\mathrm{rdeg}(f)\ge\Omega(\log n)$."

**The influence step inside the proof (Eq. (51), p. 16).** For each relevant
variable $i$, with $p/q$ an optimal rational representation and
$r(x)=p(x)q(x^i)-p(x^i)q(x)$ (so $\deg r\le 2\,\mathrm{rdeg}(f)$):
$\mathrm{Inf}_i[f]=\Pr[r(x)\ne 0]\ge 2^{-\deg(r)}\ge 2^{-2\,\mathrm{rdeg}(f)}$,
via their Theorem 3 ([NS94, Lemma 2.6], p. 5: nonzero multilinear $p$ has
$\Pr_x[p(x)\ne 0]\ge 2^{-\deg(p)}$; alternative proof printed).
$\mathrm{Inf}_i$ here is $\Pr[f(x)\ne f(x^i)]$ (defined p. 16).

**Remark 3 (p. 16), junta corollary.** A Boolean function with rational
degree $d$ depends on at most $O(d^4 2^{2d})$ variables.

**Flag.** This is the paper's ONLY influence machinery, and it is the
$2^{-\Theta(d)}$ engine (Nisan–Szegedy/Theorem 3) — the SAME regime as the
already-carded ACC22 Theorem 4.4 boundary ($2^{-d}/d$, card S1). It cannot
reach I01's window $[2^{-d}/d,\ 1/(2d))$. Conjecture 2 (p. 19,
Gotsman–Linial-flavoured: $\mathrm{Inf}[f]\le O(\sqrt{n}\,\mathrm{ndeg}(f))$)
is a CONJECTURE, not citable as a result.

---

## What the paper does NOT contain (checked against the full text)

- **No distributions over polynomials or functions** anywhere (the only
  distributions are over decision trees, Def. 8 p. 9, and product measures
  $B_y^n$ for symmetrization, Fact 5 p. 3).
- **No cross-disjoint FAMILIES**: every pair statement (T10/F7) is a single
  fixed pair; nothing couples more than two polynomials except the OPEN
  Conjecture 1.
- **No influence hypothesis in any theorem** (influence appears only in
  conclusions/proofs of T9 and in Conjecture 2), and no influence conclusion
  stronger than $2^{-2\,\mathrm{rdeg}}$ per relevant coordinate.
- **No spread, no juntas beyond Remark 3's $O(d^42^{2d})$**, no indicator or
  cylinder-pattern specialisations, no norm ($\|\cdot\|_2$) statements.
- Nothing for partial functions beyond the NEGATIVE Fact 7; nothing for
  groups other than $\mathbb{Z}_2$; nothing $\mathbb{C}$-valued in the main
  text (App. A handles $\mathbb{C}$ amplitudes only to reduce back to real
  polynomials via their Lemma 8 = [IJK+25, Lemma 26], a positive-combination
  non-vanishing lemma, p. 21 — potentially reusable for S3a's flag-1
  real/complex split, but per-point over a FINITE domain $D$ and
  non-constructive in the constants $c_i$).

**Where we use it.** C1: closes S3a's residual dependency; P2's per-pair
engine now fully READ. T4: the total-function template P2 adapts; cite for
the $16d^4$ constant. T10+F7: R5/singleton-PCC context — F7 is barrier
evidence that any rung proof must exploit $fg\equiv 0$ itself, not merely a
promise; T10 is unusable for I01's objects (flag 2). T9/R3: cite only to
delimit — the rational-degree line's influence toolbox tops out at the
exponential regime already covered by card S1.

### END OF ARTIFACT S5-kkdwy26 ###
