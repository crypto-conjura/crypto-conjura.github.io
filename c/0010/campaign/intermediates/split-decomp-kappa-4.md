# split-decomp-kappa-4 — the $P$-window closes at fixed $q$; the strict window costs $\sqrt{q^{+}}$

**New arm, not a revision.** Nothing earlier in the campaign is corrected or weakened. The
content is one construction — cap the fixed set at the balance point instead of at the requested
$P$ — applied twice, and the observation that the campaign's hardest open item, the $P$-cap of
`split-decomp-kappa-3-r4` §4, is an artefact of the *quantifier order* alone and not of the
decomposition problem.

Two results, on the region **(H2)** of Theorem E″ throughout (the $M$-corner is untouched here):

- **Theorem H.** If the family may depend on $q$, `conj:main` holds at **every** $P\in\mathbb N$,
  with $c=2$, $C=13$. The $P$-window of §2.1 of `PROGRESS.md` closes completely.
- **Theorem H′.** With the family independent of $q$, as `conj:main` proper demands, the same
  construction gives **every** $P$ with $C(q)=4\sqrt{q^{+}}+9$. So the strict window is not
  "unproved": it is proved with $C$ degraded by exactly $\Theta(\sqrt{q^{+}})$.

Theorem H′ is the Contract's own `rem:reduces` made uniform in $P$. `rem:reduces` states the
$\Theta(\sqrt{q^{+}})$ separation and calls closing it "a second open problem"; **no artifact in
this campaign has ever cited it** (`PROGRESS.md` §2.3). What is added here is the identification
of *what the separation is*: it is the price of $q$-independence, and nothing else.

Notation is the Contract's: $\sigma':=\sigma+2\log N$, $q^{+}:=q+1$,
$S:=\sqrt{\sigma'q^{+}\delta}$, $B:=\sigma'+\log\gamma^{-1}$, and
$$t_q:=\sqrt{\sigma'q^{+}/\delta},\qquad t_0:=\sqrt{\sigma'/\delta},\qquad t_q=t_0\sqrt{q^{+}}.$$
Logarithms are base $2$ throughout, as in `split-decomp-kappa-3-r4`.

## 0. Goal

`PROGRESS.md` §2.1 records the campaign's blocking item as the window
$t_0+1<P<N^{2}$, and `split-decomp-kappa-3-r4` §4 locates the obstruction at a single step: the
$P\delta$ of the Contract's `lem:hit`, which grows in $P$ while the target's first term
$\sim\sigma'q^{+}/P$ shrinks. §4's programme is to *remove* $P\delta$, by rerouting
$\mathsf{Real}\to\mathsf{Mid}\to\mathsf{Dec}$; Obstruction O1 and Lead L1 record why that needs a
new form of [CDGS, Claim 3].

This document does not attack $P\delta$. It observes that one never has to pay it at the
requested $P$, because **a $P_0$-mixture with $P_0\le P$ is already a $P$-mixture** — Contract
Definition `def:bf` asks $|I|\le P$, so the fixed-set bound is monotone in $P$ and a family built
for a smaller budget satisfies the larger one verbatim. The conjecture asks for *some* family of
$P$-mixtures; it does not ask that the fixed sets be large.

## 1. The capping construction

Fix an instance $(N,M,\sigma_1,\sigma_2,\delta)$ and a split $\delta$-unpredictable pair
$(S_1,S_2)$. Given a requested $P\in\mathbb N$ and $\gamma\in(0,1)$, put
$$\gamma_0:=\max(\gamma,\,N^{-2}),\qquad P_0:=\min\bigl(P,\ \lceil t_q\rceil\bigr),\qquad
\mathcal Y:=\mathcal Y^{P_0,\gamma_0/2},$$
$\mathcal Y^{\cdot,\cdot}$ being the family of r3's Lemma P, as used by Theorem E″ of
`split-decomp-kappa-3-r4`.

**Lemma H0 (the construction is admissible).** Every member of $\mathcal Y$ is a $P$-mixture
consistent with its index; $\mathcal Y$ is indexed by $(f,\zeta)$ and by nothing else; and
Theorem E″ applies to it at $(P_0,\gamma_0)$.

*Proof.* Each member is a $P_0$-mixture, so each component has fixed set $I$ with
$|I|\le P_0\le P$; Definition `def:bf` requires $|I|\le P$ and nothing more, so each is a
$P$-bit-fixing source and the mixture is a $P$-mixture. Consistency is a property of the fixed
*values*, $a(u)=f(u)$ on $I$, and is preserved verbatim. The index set is that of
$\mathcal Y^{P_0,\gamma_0/2}$, namely $\mathsf{Fun}\times(\{0,1\}^{*})^{2}$, as
Contract `rem:index` requires. For Theorem E″ at $(P_0,\gamma_0)$: $\gamma_0\in(0,1)$ since
$\gamma<1$ and $N^{-2}\le1/4$; hypothesis **(H1)** reads $P_0\le t_q+1$ and holds because
$P_0\le\lceil t_q\rceil\le t_q+1$; hypothesis **(H2)** is a condition on $M,q,\delta$ alone and
does not mention $P$, so it is unaffected. $\square$

**Lemma H1 (two slack bounds).** $\log\gamma_0^{-1}\le\log\gamma^{-1}$; $\log\gamma_0^{-1}\le\sigma'$,
hence $\sigma'+\log\gamma_0^{-1}\le2\sigma'$; and $N^{-2}\le S$.

*Proof.* $\gamma_0\ge\gamma$ gives the first. For the second,
$\gamma_0\ge N^{-2}$ gives $\log\gamma_0^{-1}\le2\log N\le\sigma'$ by the definition of $\sigma'$.
For the third, $\delta\ge1/N$ (a uniform guess predicts $x_i$ with probability $1/N$, so no
$\delta<1/N$ is achievable), $\sigma'\ge2$ and $q^{+}\ge1$ give
$S\ge\sqrt{2/N}$, and $N^{-2}\le\sqrt{2/N}\iff N^{-3}\le2$, true for every $N\ge1$. $\square$

The first bound is what keeps $c$ at $2$: without it the clamp would cost a factor in the
leading term rather than in the additive one.

## 2. Theorem H — at fixed $q$, `conj:main` holds at every $P$

**Theorem H.** Fix $q\in\mathbb N\cup\{0\}$ and suppose **(H2)**. For every $P\in\mathbb N$ and
every $\gamma\in(0,1)$, the family $\mathcal Y=\mathcal Y^{P_0,\gamma_0/2}$ of §1 consists of
$P$-mixtures consistent with their indices, depends only on $(S_1,S_2,P,\gamma,q)$, and satisfies,
for every $q$-query challenge-oblivious observer $D$ and with no restriction on challenge
resolution,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}\ +\ 13\,S\ +\ \gamma .$$
That is, the Contract's `conj:main` with $c=2$, $C=13$, and **no hypothesis on $P$**.

*Proof.* Lemma H0 licenses Theorem E″ at $(P_0,\gamma_0)$, which gives
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma_0^{-1})q^{+}}{P_0}+8S+\gamma_0 .$$
Two cases.

*Case (a), $P\le\lceil t_q\rceil$.* Then $P_0=P$, and by Lemma H1
$\log\gamma_0^{-1}\le\log\gamma^{-1}$, so the first term is at most $2Bq^{+}/P$, which is the
target's own first term with $c=2$. For the additive term,
$\gamma_0\le\gamma+N^{-2}\le\gamma+S$. Total: $2Bq^{+}/P+9S+\gamma$.

*Case (b), $P>\lceil t_q\rceil$.* Then $P_0=\lceil t_q\rceil\ge t_q$, and by Lemma H1
$\sigma'+\log\gamma_0^{-1}\le2\sigma'$, so
$$\frac{2(\sigma'+\log\gamma_0^{-1})q^{+}}{P_0}\ \le\ \frac{4\sigma'q^{+}}{t_q}
\ =\ 4\sigma'q^{+}\sqrt{\frac{\delta}{\sigma'q^{+}}}\ =\ 4S .$$
With $\gamma_0\le\gamma+S$ again, the total is at most $13S+\gamma$, and the target's first term
is non-negative.

Both cases are dominated by $2Bq^{+}/P+13S+\gamma$. $\square$

**Remark (the $P$-window is closed, and where the constants went).** Against Theorem E″ the trade
is exact: **(H1)** is deleted outright and $C$ moves $8\to13$, while $c$ does not move. Of the
five extra units, four are the capping in case (b) and one is the $\gamma$-clamp. Machine-checked
over **16644 grid points** — $N\le2^{20}$, $\sigma\le64$, $q\le10^{7}$, $\delta\in[1/N,1]$,
$\gamma$ down to $10^{-30}$, and $P$ swept across the whole axis including $\lceil t_q\rceil$,
$2\lceil t_q\rceil$, $N$, $N^{2}/2$ and $N^{2}$ — zero failures, in
`c/0010/campaign/checks/cap-fixed-q.py`. The smallest $C$ that suffices on that grid is
$12.0000$, attained at $\gamma\ll N^{-2}$ and $P=N^{2}$, so the proved $13$ carries one unit of
slack, all of it in the crude $N^{-2}\le S$ of Lemma H1.

**Remark (what the relaxation is, exactly).** Only one thing changes against `conj:main`: the
family is allowed to depend on $q$, through $P_0=\min(P,\lceil t_q\rceil)$ and nothing else. It
still may not depend on $D$, on $\mathbf x$, or on anything the Contract's `rem:index` forbids;
it is still one family per $(P,\gamma,q)$, still indexed by $(f,\zeta)$, still consistent. The
Contract's `rem:order` warns that relaxing the order "makes the statement easier in a way the
intended applications cannot use". Theorem H is a witness to the first half of that sentence. The
second half is a claim about applications on which the Contract offers no argument and this
document takes no position, beyond noting that `thm:main` itself fixes one observer, hence one
$q$, before it instantiates.

## 3. Theorem H′ — one $q$-free family, every $P$, at a cost of $\sqrt{q^{+}}$

Cap instead at the $q$-free balance point: $P_0':=\min(P,\lceil t_0\rceil)$,
$\mathcal Y':=\mathcal Y^{P_0',\gamma_0/2}$. This family mentions no $q$.

**Theorem H′.** Suppose **(H2)** holds at $q$. The family $\mathcal Y'$ depends only on
$(S_1,S_2,P,\gamma)$ — not on $q$ — consists of $P$-mixtures consistent with their indices, and
satisfies, for every $P\in\mathbb N$, every $q\in\mathbb N\cup\{0\}$ and every $q$-query
challenge-oblivious observer $D$,
$$\mathsf{Adv}_{\mathcal Y',D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}
\ +\ \bigl(4\sqrt{q^{+}}+9\bigr)S\ +\ \gamma .$$

*Proof.* As in Lemma H0, with **(H1)** at $P_0'$ holding for *every* $q$ at once, since
$P_0'\le\lceil t_0\rceil\le t_0+1\le t_q+1$ by $t_0\le t_q$. Theorem E″ then applies at
$(P_0',\gamma_0)$ for each $q$. Case (a), $P\le\lceil t_0\rceil$, is as before and gives
$2Bq^{+}/P+9S+\gamma$. Case (b), $P>\lceil t_0\rceil$: now $P_0'\ge t_0=\sqrt{\sigma'/\delta}$, so
$$\frac{4\sigma'q^{+}}{t_0}\ =\ 4\sigma'q^{+}\sqrt{\frac{\delta}{\sigma'}}\ =\ 4q^{+}\sqrt{\sigma'\delta}
\ =\ 4\sqrt{q^{+}}\cdot S ,$$
using $S=\sqrt{q^{+}}\sqrt{\sigma'\delta}$. Adding $8S$ and $\gamma_0\le\gamma+S$ gives the
claim. $\square$

Machine-checked over **12852 grid points** in the same file: zero failures, worst multiplier on
$S$ equal to $21.2665$ against the claimed $4\sqrt{q^{+}}+9$ (which is $22.27$ at the $q=10$ point
where the worst is attained).

**Remark (this is `rem:reduces`, and it identifies the separation).** The Contract's
`rem:reduces` gives a $q$-free family with
$\mathsf{Adv}\le\kappa(q)+Aq/P_0+\gamma+P_0\delta+q\delta$ at
$P_0=\min(P,\lceil\sqrt{A/\delta}\,\rceil)$ — the same capping, at the same $q$-free point — and
concludes `conj:main` "for $P\le\sqrt{A/\delta}$, and for every $P$ when $q=O(1)$", the two
directions being separated by $\Theta(\sqrt{q^{+}})$ for growing $q$. Theorem H′ restates that
uniformly in $P$ and against Theorem E″'s machinery rather than against $\kappa$ directly;
Theorem H then shows the separation is *exactly* the price of $q$-independence, since capping at
$t_q$ instead of $t_0$ removes it and changes nothing else. That is the first thing this campaign
has said about `rem:reduces`, which `PROGRESS.md` §2.3 records as cited by no artifact.

**Remark (what this does to §2.1's status line).** `PROGRESS.md` §2.1 calls the window
$t_0+1<P<N^{2}$ unproved. Strictly that is about `conj:main` with $C$ absolute, and it stands.
But the window is not blank: on all of it, Theorem H′ proves `conj:main` with
$C(q)=4\sqrt{q^{+}}+9$, and Theorem H proves it outright once $q$ may be fixed first. The honest
statement of the residue is therefore **a $\sqrt{q^{+}}$ in the constant under $q$-free families**,
not an uncovered region.

## 4. What this does and does not settle

**Settled, on region (H2):** the $P$-axis, at fixed $q$, in full. No $P$-hypothesis survives in
Theorem H.

**Not settled, and not touched:**

- **The $M$-corner.** **(H2)** is carried unchanged through both theorems. Everything here is
  conditional on it, and `PROGRESS.md` §2.2's open question — whether the first arm of Corollary
  D″ can be made $M$-free — is exactly as open as before. At $q=0$, Corollary G2 discharges
  **(H2)** for every $M$, so Theorem H is unconditional there.
- **Strict `conj:main` with absolute $C$.** Theorem H′ leaves the $\sqrt{q^{+}}$. Closing it is
  the Contract's `rem:reduces` second open problem, now with a sharper description: find a
  $q$-free family achieving what the $q$-aware cap achieves, or show none exists.
- **The lower-bound side.** Nothing here bears on Proposition F or on tightness.

**A redirection this forces, and it is the practical point.** `split-decomp-kappa-3-r4` §4 spends
the campaign's deepest effort — Obstruction O1, Lead L1, the request for a new form of [CDGS,
Claim 3] tolerating a bounded-deficiency perturbation — on removing $P\delta$ so that large $P$
can be afforded. Theorem H shows that at fixed $q$ **that work is unnecessary**: one never needs a
fixed set larger than $\lceil t_q\rceil$, so $P\delta$ never needs to exceed $S$. §4's programme
is therefore aimed squarely and solely at the $q$-free statement, where the cap must sit at $t_0$
and the $\sqrt{q^{+}}$ is real. Anyone resuming §4 should know they are working on `rem:reduces`'s
second open problem, not on the $P$-cap as §2.1 describes it.

## 5. Gap register

- **[INHERITED-UNAUDITED: Theorem E″ of `split-decomp-kappa-3-r4`]** — *load-bearing* for
  everything here; both theorems are corollaries of it. `split-decomp-kappa-3-r4` stands at
  **zero verification passes of five**, as does its predecessor r3.
- **[INHERITED-UNAUDITED: Corollary D″ of `split-decomp-kappa-2-r2`]** — *load-bearing*
  transitively, as the extraction term inside Theorem E″, and the weakest link in the chain:
  zero passes, with the one referee objection ever raised against its constant **overruled**
  rather than upheld.
- **[INHERITED: Contract `def:bf`, `rem:index`, `rem:order`, `rem:reduces`]** — `def:bf`'s
  $|I|\le P$ is load-bearing for Lemma H0 and is quoted verbatim from the Contract. The
  Contract's own lemmas `lem:hit` and `lem:query` have never been refereed by any pass
  (`PROGRESS.md` §3); they enter here only transitively through Theorem E″.
- **[GAP: (H2)]** — carried, not discharged, except at $q=0$ via Corollary G2.
- **No `[GAP]` occurs in §§1–3 beyond (H2).**

**Verification status of this document: zero passes of five.** It has had no blind review, no
triage, and no refuter pass. Its two theorems are short and their arithmetic is machine-checked,
which is not the same as refereed, and the one non-arithmetical step — Lemma H0's claim that a
$P_0$-mixture is a $P$-mixture — is precisely the kind of definitional move a referee should
attack first.

## 6. External results used

- **[kappa-3-r4, Theorem E″]** — `split-decomp-kappa-3-r4` §2. Restated where used; not reproved.
  Both **(H1)** and **(H2)** are quoted as stated there.
- **[kappa-3-r4, Corollary G2]** — same, for the $q=0$ discharge of **(H2)** in §4.
- **[Contract, Definition `def:bf`]** — quoted for $|I|\le P$ and for consistency.
- **[Contract, Remark `rem:reduces`]** — quoted in §3; its $P_0=\min(P,\lceil\sqrt{A/\delta}\,\rceil)$
  is the construction Theorem H′ reproduces.
- $\lceil t\rceil\le t+1$; $t_q=t_0\sqrt{q^{+}}$; $\delta\ge1/N$. RESTATED, standard.

### END OF ARTIFACT split-decomp-kappa-4 ###
