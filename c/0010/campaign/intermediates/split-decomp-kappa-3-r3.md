# split-decomp-kappa-3-r3 — reducing Theorem E's hypotheses, and locating the $P$-cap

**Revision of `split-decomp-kappa-3-r2` after its blind review** (`split-decomp-kappa-3-r2-findings.md`,
verdict DEFECTS, four findings) **and after a repo-wide audit of the campaign.** No mathematics
in §§1–3 changes: every computational step of Lemma G0, Theorem E″, Corollary G1 and Corollary G2
was independently re-derived and confirmed by the referee. What changes is what the document
*says about itself*, in five places, plus two additions.

Upheld from the review:

- **F1 (class C).** Theorem E″'s proof opened "By Lemma G0 we may assume $q^{+}\delta\le\sigma'$",
  which is strictly weaker than what the sharpened sub-bounds then use
  ($\sigma'q^{+}\delta<1/64$); $q^{+}\delta\le\sigma'$ alone does not imply them. The later
  paragraph re-invoked the true dichotomy, so the logic was sound, but the opening sentence did
  not license what followed. **Fixed** in §2.
- **F2 (class A).** The Remark "(what changed, and what did not)" was carried over byte-for-byte
  from `split-decomp-kappa-3`, where "the only altered step is the fixed-set term" and "no
  constant moves" were true. In r2 the *query* term was rewritten too, with new constants
  $1/(8\sigma')$ and $1/16$. Both sentences were therefore false of the document they sat in.
  **Deleted and replaced** in §2.
- **F3 (class A).** Corollary G1's title claimed the proved region "contains the Contract's own
  instantiation", but its proof checks only **(H1)** at $P=\lceil t\rceil$ and never **(H2)**,
  a condition on $M$ that `thm:main` needs at whatever ambient $M$ it was handed. The referee
  called this "a softer instance of the same class of defect (F1) this revision was written to
  fix", which is right. **Retitled and qualified** in §2.
- **F4 (class A, minor).** The r2 note claimed §6 "differs only in the id on its END line and in
  swapping $\lfloor t\rfloor\ge t/2$ for $\lceil t\rceil\le t+1$"; the bibliography bullet had
  also gained an explanatory parenthetical. **Corrected** — see the invariant statement below.

From the audit, and more serious than any of the above:

- **A1.** §5 asserted that "`split-decomp-kappa-2-r2` has been through blind review at r1 and
  r2". **This is false.** There is one findings file in the campaign for that arm and it reviews
  `split-decomp-kappa-2`, the *pre-revision* artifact at `8c68c62`; its tally's own header states
  that it "does NOT carry over to r2". So Corollary D″, load-bearing for Theorem E″, sits in an
  artifact with **zero** verification passes — and D″'s constant is precisely where triage
  overruled a referee. **Corrected** in §5.
- **A2.** Nothing in this lineage distinguished Theorem E″'s per-$q$ region from the region on
  which `conj:main` *itself* is proved. `conj:main` fixes one family per $(P,\gamma)$ and then
  demands the bound at **every** $q$, so the region for `conj:main` is the intersection over $q$,
  which is strictly smaller. In particular the $\sqrt{q^{+}}$ relaxation of **(H1)** does *not*
  enlarge it. **New Remark** in §2 states the correct region.

Two additions: Remark `rem:window` in §2 (the $P$-gap is a bounded window, not a half-line) and
Remark `rem:second` in §4 (the Contract's `rem:reduces` names a second open problem that no
artifact in this campaign has ever engaged with).

Not fixed, because it was the reviewer's packaging, not the artifact: the review returned one
class-(E) entry, unable to open the package's `cards/` directory to check two §4 quotations. The
`cards/` files were present; the prompt named the directory without naming the files, and the
referee's tool set had no directory listing. Not load-bearing — §4 is independent of §§1–3 — but
it means §4's two card quotations remain unchecked by any referee.

**Invariant, checked mechanically section by section rather than asserted.** Against
`split-decomp-kappa-3-r2`: **§0, §1 and §3 are byte-identical.** **§4** is byte-identical apart
from the appended Remark `rem:second`. **§6** differs in exactly one line, the id on its END
line. **§5** differs in exactly one bullet, the third, whose tag changes from `[INHERITED]` to
`[INHERITED-UNAUDITED]`. **§2** is where the substance of this revision sits: the proof's opening
sentence (F1), the Remark deleted and replaced by two (F2), Corollary G1's title (F3), and four
appended Remarks — F3's scope note, A2 on `conj:main`'s region, the deflationary consequence for
(G1), and `rem:window`.

Theorem E″'s statement, **(H1)**, **(H2)**, Lemma G0 and Corollary G2 are untouched, so nothing
proved in r2 is weakened here. The four new mathematical claims — that **(H1)** over all $q$
binds at $q=0$ to $P\le\sqrt{\sigma'/\delta}+1$, that **(H2)** over all $q$ binds at $q=1$ to
$M\le\sigma'/(2\delta)$, that the $P$-window is non-empty in every non-vacuous instance, and that
it is bounded above by $N^{2}$ — were machine-checked over 189 non-vacuous parameter points
spanning $N\le2^{30}$, $\sigma\le64$, $q\le10^{7}$, $\delta\in[1/N,1]$: zero failures.

## 0. Goal

All notation is that of the Contract and of `split-decomp-kappa-2-r2` §0, unchanged:
$N,M\ge2$, $\mathsf{Fun}=\{f:[N]\times[N]\to[M]\}$, a split $\delta$-unpredictable pair
$(S_1,S_2)$ with leakage bounded by $\sigma_1,\sigma_2$, $\sigma:=\sigma_1+\sigma_2$,
$\sigma':=\sigma+2\log N$, $q^{+}:=q+1$, $\mu'(s):=\min(s\delta,2(s\delta^{2})^{1/3},1)$.
Logarithms are base two. $\mathcal Y^{P,\gamma}$ is the family of r3's Lemma P.

Theorem E of `split-decomp-kappa-2-r2` proves the Contract's conjecture with $c=2$, $C=8$ under
three hypotheses,
$$P\le\sqrt{\sigma'/\delta},\qquad q^{+}\delta\le\sigma',\qquad M\le\frac{\sigma'q^{+}}{4\delta}.$$
This document establishes three things.

**(G0)** The hypothesis $q^{+}\delta\le\sigma'$ may be **deleted**. It is implied by the
conclusion being non-vacuous.

**(G1)** The hypothesis $P\le\sqrt{\sigma'/\delta}$ may be **relaxed by a factor
$\sqrt{q^{+}}$**, to $P\le\sqrt{\sigma'q^{+}/\delta}+1$, with the same constants. This
matters because $\lceil\sqrt{\sigma'q^{+}/\delta}\,\rceil$ is exactly the $P$ at which the
Contract's own Theorem `thm:main` instantiates the conjecture: under Theorem E as stated, the
Contract's intended use of the conjecture sat a factor $\sqrt{q^{+}}$ **outside** the proved
region, and it no longer does. The additive $1$ is not cosmetic — it is what admits
`thm:main`'s **ceiling** rather than a nearby value, and it is free.

**(G2)** The hypothesis $M\le\sigma'q^{+}/(4\delta)$ may be replaced by
$\min\{\mu'(\min(qM,N^{2})),\,2\delta\sqrt M\}\le\sqrt{\sigma'q^{+}\delta}$, using Corollary
D″ in place of Corollary D′. At $q=0$ that condition is **vacuous**, since $\mu'(0)=0$
exactly, so at $q=0$ the conjecture holds for **every** $M$ and every observer under the single
hypothesis $P\le3\sqrt{\sigma'/\delta}$.

The conjecture in full is still **not** proved. §4 states what the residual $P$-cap is, why it
is a defect of the proof route rather than of the statement, and — in Obstruction O1 — why the
obvious repair needs a new idea rather than more care. §5 is the gap register.

## 1. The third hypothesis is free

**Lemma G0.** Let $N\ge2$. If $8\sqrt{\sigma'q^{+}\delta}\ge1$ then the conclusion of Theorem E
holds trivially, its right-hand side being at least $1\ge\mathsf{Adv}_{\mathcal Y,D}$.
Otherwise $q^{+}\delta\le\sigma'$ holds automatically. Consequently Theorem E is true with the
hypothesis $q^{+}\delta\le\sigma'$ removed.

*Proof.* $\mathsf{Adv}_{\mathcal Y,D}$ is a difference of two probabilities, so
$\mathsf{Adv}_{\mathcal Y,D}\le1$; and the right-hand side
$2(\sigma'+\log\gamma^{-1})q^{+}/P+8\sqrt{\sigma'q^{+}\delta}+\gamma$ is at least
$8\sqrt{\sigma'q^{+}\delta}$, every summand being non-negative. That disposes of the first case.
In the second, $8\sqrt{\sigma'q^{+}\delta}<1$ gives $\sigma'q^{+}\delta<1/64$, hence
$q^{+}\delta<1/(64\sigma')$. Since $N\ge2$ gives $2\log N\ge2$ and $\sigma\ge0$, we have
$\sigma'\ge2$, so $q^{+}\delta<1/128<2\le\sigma'$. $\square$

This is the same device r3 uses in the second sentence of Corollary A$'$ ("outside that regime
$q^{+}\delta>\sigma'\ge2$, so $\sqrt{\sigma'q^{+}\delta}>\sigma'>1$ and the target bound is
vacuous"); it is recorded here because Theorem E carries the condition as a hypothesis rather
than discharging it.

## 2. The $P$-hypothesis relaxes by $\sqrt{q^{+}}$

**Theorem E″.** Let $N,M\ge2$, $\gamma\in(0,1)$, $P\in\mathbb N$, $q\in\mathbb N\cup\{0\}$, and
let $\mathcal Y:=\mathcal Y^{P,\gamma/2}$ be the family of r3's Lemma P — built from
$(S_1,S_2,P,\gamma)$ alone, before $q$, indexed by $(f,\zeta)$, each member a $P$-mixture
consistent with its index. Suppose

  **(H1)** $P\le\sqrt{\sigma'q^{+}/\delta}+1$, and

  **(H2)** $\min\bigl\{\mu'(\min(qM,N^{2})),\ 2\delta\sqrt M\bigr\}\le\sqrt{\sigma'q^{+}\delta}$.

Then for every $q$-query challenge-oblivious observer $D$, with no restriction on challenge
resolution,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}+8\sqrt{\sigma'q^{+}\delta}+\gamma,$$
i.e. the Contract's conjecture holds on that region with $c=2$, $C=8$.

*Proof.* By Lemma G0 we may assume $8\sqrt{\sigma'q^{+}\delta}<1$, the other case being
trivial because the conclusion then exceeds $1\ge\mathsf{Adv}_{\mathcal Y,D}$. That gives both
$\sigma'q^{+}\delta<1/64$, used in the sharpened sub-bounds below, and $q^{+}\delta\le\sigma'$,
which is Lemma G0's conclusion. As in
Theorem E, r3's Theorem C gives, for the same fixed $D$ and with
$\varepsilon(D):=|\Pr[\mathsf{Real}=1]-\Pr[\mathsf{Real}_0=1]|$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \varepsilon(D)+\frac{2(\sigma'+\log\gamma^{-1})q}{P}+\gamma+P\delta+q\delta,$$
and the second term is at most the target's first, as $q\le q^{+}$. Four terms remain.

*The extraction term.* Corollary D″ applies to $D$ with no hypothesis on it and gives
$\varepsilon(D)\le\kappa(q)\le5\sqrt{\sigma'\delta}+\min\{\mu'(\min(qM,N^{2})),2\delta\sqrt M\}$.
Here $5\sqrt{\sigma'\delta}\le5\sqrt{\sigma'q^{+}\delta}$, and the minimum is at most
$\sqrt{\sigma'q^{+}\delta}$ by **(H2)**, so $\varepsilon(D)\le6\sqrt{\sigma'q^{+}\delta}$.

*Two sharpened sub-bounds, available because Lemma G0 has already put us in the non-vacuous
case.* There $8\sqrt{\sigma'q^{+}\delta}<1$, so $\sigma'q^{+}\delta<1/64$. Hence
$q^{+}\delta<1/(64\sigma')$, and $q^{+}\delta\le c^{2}\sigma'$ holds for $c=1/(8\sigma')$, so
$$q\delta\ \le\ q^{+}\delta\ \le\ \frac{1}{8\sigma'}\sqrt{\sigma'q^{+}\delta}\ \le\ \tfrac1{16}\sqrt{\sigma'q^{+}\delta}$$
using $\sigma'\ge2$. Likewise $\delta<1/(64\sigma'q^{+})$ gives
$\delta\le\tfrac1{8\sigma'q^{+}}\sqrt{\sigma'q^{+}\delta}\le\tfrac1{16}\sqrt{\sigma'q^{+}\delta}$.
Both are worth having: the crude bounds $q\delta\le\sqrt{\sigma'q^{+}\delta}$ and
$\delta\le\sqrt{\sigma'q^{+}\delta}$ each spend a whole unit of the target's $8$, and there
is no unit to spare.

*The fixed-set term.* Writing $t:=\sqrt{\sigma'q^{+}/\delta}$, so that $t\delta=\sqrt{\sigma'q^{+}\delta}$,
**(H1)** gives $P\le t+1$ and hence
$$P\delta\ \le\ t\delta+\delta\ \le\ \sqrt{\sigma'q^{+}\delta}+\tfrac1{16}\sqrt{\sigma'q^{+}\delta}\ =\ \tfrac{17}{16}\sqrt{\sigma'q^{+}\delta}.$$

*The query term.* $q\delta\le\tfrac1{16}\sqrt{\sigma'q^{+}\delta}$, above.

Adding, $6+\tfrac{17}{16}+\tfrac1{16}=7\tfrac18\le8$. $\square$

**Remark (the slack is real, and where it went).** The original Theorem E″ spent its budget
exactly — $6+1+1=8$ — by bounding $q\delta$ and, implicitly, any additive $\delta$ against a
full $\sqrt{\sigma'q^{+}\delta}$ each. Both are gross overestimates: in the only regime where
the conclusion says anything, each is smaller by a factor $8\sigma'\ge16$. Recovering that is
what pays for the additive $1$ in **(H1)**, and it leaves $\tfrac78$ of a unit unused.
Machine-checked over $N$ up to $2^{30}$, $\sigma$ up to $64$, $q$ up to $10^{7}$ and
$\delta\in[1/N,1]$, restricted to non-vacuous instances: the worst total is $7.0022$.

**Remark (what changed from Theorem E, accurately).** Two steps differ, not one. Theorem E
bounds the fixed-set term as $P\delta\le\sqrt{\sigma'\delta}\le\sqrt{\sigma'q^{+}\delta}$,
passing through an intermediate it does not need and paying $\sqrt{q^{+}}$ for the passage; the
direct inequality is what **(H1)** states. And Theorem E bounds the query term against a full
$\sqrt{\sigma'q^{+}\delta}$, where the sharpened bound above gives $\tfrac1{16}$ of one. The
constants $1/(8\sigma')$ and $1/16$ are new here; the target's $c=2$ and $C=8$ are not.
(`split-decomp-kappa-3-r2` carried a remark, inherited from its own predecessor, saying "the
only altered step is the fixed-set term" and "no constant moves". Both were true of the
predecessor and false of r2. Finding F2.)

**Remark (the quantifier order).** Contract Remark `rem:order` is respected exactly as in
Theorem E: **(H1)** and **(H2)** are conditions on the *region*, and $\mathcal Y^{P,\gamma/2}$ is
still fixed by $(S_1,S_2,P,\gamma)$ before $q$ is named. A $q$-dependent region is not a
$q$-dependent family — Theorem E already relies on this, its own third hypothesis
$M\le\sigma'q^{+}/(4\delta)$ mentioning $q$. Two blind referees have now checked this against
`rem:order` and `rem:index` directly rather than on the artifact's word, and both found no
violation.

**Corollary G1 (Theorem E″ reaches `thm:main`'s own $P$, on the region **(H2)**).** The
Contract's `thm:main` proves $\kappa(q)\le(4c+2C+4)\sqrt{\sigma'q^{+}\delta}+q\delta$ by
instantiating the conjecture at $\gamma:=N^{-2}$ and $P:=\lceil\sqrt{\sigma'q^{+}/\delta}\,\rceil$.
Under Theorem E that $P$ exceeds the admissible range by a factor $\sqrt{q^{+}}$, so Theorem E
supplied `thm:main` only at $q=0$; capping $P$ at $\sqrt{\sigma'/\delta}$ instead yields
$\kappa(q)=O(q^{+}\sqrt{\sigma'\delta})$, weaker than the target by $\sqrt{q^{+}}$.

Under **(H1)** that same $P$ is admissible, and it is admissible *as written*: with
$t:=\sqrt{\sigma'q^{+}/\delta}$ we have $\lceil t\rceil\le t+1$, which is exactly **(H1)**.
This is what the additive $1$ in **(H1)** is for. Taking $\lceil t\rceil$ rather than a nearby
value also improves the chase, since $\lceil t\rceil\ge t$ gives
$$\frac{\sigma'q^{+}}{P}\ \le\ \frac{\sigma'q^{+}}{t}\ =\ \sigma'q^{+}\sqrt{\frac{\delta}{\sigma'q^{+}}}\ =\ \sqrt{\sigma'q^{+}\delta}$$
with no factor $2$. So, with $\log\gamma^{-1}=2\log N\le\sigma'$ and hence
$\sigma'+\log\gamma^{-1}\le2\sigma'$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{4\sigma'q^{+}}{P}+8\sqrt{\sigma'q^{+}\delta}+\gamma\ \le\ 12\sqrt{\sigma'q^{+}\delta}+\gamma\ \le\ 13\sqrt{\sigma'q^{+}\delta},$$
using $\gamma=N^{-2}\le\delta^{2}\le\delta\le\sqrt{\sigma'q^{+}\delta}$.

*What the earlier version of this corollary got wrong.* `split-decomp-kappa-3` stated
**(H1)** as $P\le t$ and then instantiated at $\lfloor t\rfloor$, while asserting in its title
that the region contains `thm:main`'s $\lceil t\rceil$. It does not: $\lceil t\rceil>t$
whenever $t\notin\mathbb N$, which is the generic case — 165 of 180 points on a parameter grid
spanning $N\le2^{20}$, $\sigma\le64$, $q\le10^{4}$. The arithmetic there was correct for
$\lfloor t\rfloor$; the title was not established. Recorded as finding F1 of
`split-decomp-kappa-3-findings.md`.

*This is a statement about the conjecture, not about $\kappa$.* On the region **(H2)**,
Corollary D″ already bounds $\kappa(q)\le6\sqrt{\sigma'q^{+}\delta}$ outright, with no $P$ and
no appeal to the conjecture, so the Contract's *consequence* was never the thing missing there.
What **(H1)** buys is that the *decomposition statement itself* is now proved at the parameter
a user following the Contract would instantiate it at. Under Theorem E as stated, anyone using
the conjecture as `thm:main` uses it was outside the proved region.

**Remark (what this corollary does *not* say — finding F3).** The chase above verifies **(H1)**
at $P=\lceil t\rceil$ and nothing else. It does **not** verify **(H2)**, which is a condition on
$M$, and `thm:main` is handed its $M$ ambiently, before $P$, $\gamma$ and $q$ are chosen. So the
corollary's reach is "on the region **(H2)**", as its title now says, and not unconditionally.
The unqualified word "contains" in the r2 title was a softer instance of exactly the defect F1
was raised against, and is corrected here.

**Remark (the region for `conj:main` itself is smaller than **(H1)**$\wedge$**(H2)** — finding A2).**
This is the sharpest thing in this document and it was missing from every earlier version.
Theorem E″ is a statement *per $q$*: it fixes $P$ and $q$ jointly and then quantifies over
$q$-query observers. `conj:main` is not. It fixes one family per $(P,\gamma)$ — before $q$ — and
then demands the bound at **every** $q$. So `conj:main` holds at $(P,\gamma)$ exactly when
**(H1)** and **(H2)** hold at *every* $q$, and that is the intersection, not the region.

Both hypotheses are weakest at small $q$, so the intersection binds there. **(H1)** reads
$P\le\sqrt{\sigma'q^{+}/\delta}+1$, whose right side increases in $q$, so it binds at $q=0$:
$$P\ \le\ \sqrt{\sigma'/\delta}+1 .$$
**(H2)** is vacuous at $q=0$ and, via its $2\delta\sqrt M$ arm, reads $M\le\sigma'q^{+}/(4\delta)$
for $q\ge1$, binding at $q=1$:
$$M\ \le\ \frac{\sigma'}{2\delta} .$$
On that region one family serves every $q$ and `conj:main` is proved outright. Off it, Theorem E″
still gives the bound for the $q$ in its region — which is all `thm:main` ever needs, since
`thm:main` fixes one observer and therefore one $q$ — but it does not give `conj:main` at that
$P$.

**The consequence for (G1) is deflationary and should be stated plainly.** The $\sqrt{q^{+}}$
relaxation of **(H1)** does *not* enlarge the region on which `conj:main` is proved, because that
region is pinned at $q=0$ where the relaxation is worth nothing. Against Theorem E's original
$P\le\sqrt{\sigma'/\delta}$ and $M\le\sigma'q^{+}/(4\delta)$ — whose intersection over $q$ is
$P\le\sqrt{\sigma'/\delta}$, $M\le\sigma'/(4\delta)$ — this document's gain for `conj:main`
proper is the additive $1$ in $P$ and a factor $2$ in $M$. The $\sqrt{q^{+}}$ is real and it is
what makes `thm:main` derivable from Theorem E″ without loss; it is not a gain in the conjecture's
proved region, and (G1) should not be read as claiming one.

**Remark (the $P$-gap is a bounded window, not a half-line).**\label{rem:window}
No file in the campaign records this. For $P\ge N^{2}$ take $I:=[N]\times[N]$ and $a:=f$, so that
$Y_{f,\zeta}$ is the point mass at $f$. It is $P$-bit-fixing by Contract Definition `def:bf`
— $|I|=N^{2}\le P$, and the uniformity condition off $I$ is vacuous — it is consistent with $f$,
it is indexed by $(f,\zeta)$, and it depends on nothing else. Then $H^{*}=H$, so $\mathsf{Dec}$
and $\mathsf{Real}$ are the same experiment and $\mathsf{Adv}_{\mathcal Y,D}=0$ for every $q$ and
every $D$. So `conj:main` is trivially true at $P\ge N^{2}$, and the uncovered set is the window
$$\sqrt{\sigma'q^{+}/\delta}+1\ <\ P\ <\ N^{2},$$
non-empty in every non-vacuous instance, since $8\sqrt{\sigma'q^{+}\delta}<1$ and $\delta\ge1/N$
force $\sqrt{\sigma'q^{+}/\delta}<N/8$. This bounds the problem but does not shrink it: the
window is where every application lives.

## 3. At $q=0$ there is no restriction on $M$

**Corollary G2.** Let $N,M\ge2$, $\gamma\in(0,1)$ and $P\le3\sqrt{\sigma'/\delta}$. Then for
every $0$-query challenge-oblivious observer, and every $M$,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})}{P}+8\sqrt{\sigma'\delta}+\gamma.$$

*Proof.* **(H2)** at $q=0$ reads $\min\{\mu'(\min(0,N^{2})),2\delta\sqrt M\}=\min\{\mu'(0),2\delta\sqrt M\}$,
and $\mu'(0)=\min(0,0,1)=0$, so **(H2)** holds for every $M$. In r3's Theorem C at $q=0$ the
chain is $\mathsf{Adv}_{\mathcal Y,D}\le\varepsilon(D)+\gamma+P\delta$, the two $q$-carrying
terms vanishing. r3's Theorem A gives $\kappa(0)\le5\sqrt{\sigma'\delta}$ with no hypothesis on
$M$ and none on resolution — "for $q=0$, $s=0$ and every observer has resolution $1$
vacuously" — so $\varepsilon(D)\le5\sqrt{\sigma'\delta}$, leaving three units of the target's
$8\sqrt{\sigma'\delta}$ for $P\delta$: $P\delta\le3\sqrt{\sigma'\delta}$ iff
$P\le3\sqrt{\sigma'/\delta}$. $\square$

This strictly enlarges what `split-decomp-kappa-2-r2` §7 records as known ("the conjecture
holds for (i) every observer when $M\le\sigma'q^{+}/(4\delta)$, and (ii) every resolution-$1$
observer for arbitrary $M$"): at $q=0$ neither branch is needed, and the constant on the
$P$-cap improves by $3$.

## 4. The residual $P$-cap is a defect of the route, not of the statement

**Where it enters.** In r3's Theorem C the chain is
$\mathsf G_0=\mathsf{Real}$, $\mathsf G_1=\mathsf{Real}_0$, $\mathsf G_2=\mathsf{Dec}_0$,
$\mathsf G_3=\mathsf{Dec}$, and $P\delta$ appears **once**, in
$|\mathsf G_2-\mathsf G_3|\le P\delta+q\delta$, as the Contract's Lemma `lem:hit` bound
$\Pr[\mathbf x\in I_J]\le P\delta$. Every other term in Theorem E″'s proof is either $O(1/P)$
or $P$-free. So the whole of the $P$-cap is the requirement that $\Pr[\mathbf x\in I_J]$ be
absorbed into $\sqrt{\sigma'q^{+}\delta}$.

**Why the event is favourable, not adverse.** $\mathsf G_2\to\mathsf G_3$ replaces a uniform
independent challenge by $H^{*}(\mathbf x)$. On $\{\mathbf x\in I_J\}$ the fixed values of
$Y_{H,\mathbf z}$ agree with $H$ — this is *consistency*, Definition `def:bf` — so
$H^{*}(\mathbf x)=H(\mathbf x)$, which is exactly the challenge $\mathsf{Real}$ supplies. The
event on which the route pays $P\delta$ is the event on which $\mathsf{Dec}$'s challenge is
*correct*. The cost is incurred only because the route passes through $\mathsf{Dec}_0$, where
the challenge is uniform, and so must pay to put back a value it already had.

**The Contract says as much.** Remark `rem:uses` records that `thm:main` uses exactly three
features of the family and that "the consistency requirement of Definition `def:bf` is *not*
used anywhere in this section". That is precisely why the Contract's own derivation pays
$P\delta$: it discards the hypothesis that would make the payment unnecessary. r3's Theorem C
inherits the route and the cost.

**A candidate replacement.** Route $\mathsf{Real}\to\mathsf{Mid}\to\mathsf{Dec}$ with
$\mathsf{Mid}$ the experiment that draws $H,(\mathbf x,\mathbf z)$ as in $\mathsf{Real}$ and
$H^{*}\sample Y_{H,\mathbf z}$, and runs $D^{H^{*}}(H(\mathbf x),\mathbf z)$ — decomposed
oracle, *real* challenge. Then $|\mathsf{Mid}-\mathsf{Dec}|$ is supported on
$\{\mathbf x\notin I_J\}$, where the two challenges are $H(\mathbf u)$ and a fresh uniform
value at a point $\mathbf u$ off the fixed set. r3's Lemma P Step 2 supplies, via
[CDGS, Claim 2], that the conditional law of $H$ is a $(P,1-\delta_\zeta)$-dense source with
$\delta_\zeta\log M=(S_\zeta+\log\gamma^{-1})/P$; density at a single coordinate off the fixed
set gives $\Pr[H(\mathbf u)=v]\le M^{-(1-\delta_\zeta)}$, so
$$\mathrm{SD}\bigl(H(\mathbf u),\mathrm{Unif}([M])\bigr)\ \le\ M^{\delta_\zeta}-1\ \le\ \delta_\zeta\ln M\cdot M^{\delta_\zeta}\ \le\ 2\ln2\cdot\frac{S_\zeta+\log\gamma^{-1}}{P}$$
whenever $\delta_\zeta\log M\le1$ — where $M^{\delta_\zeta}=2^{\delta_\zeta\log M}\le2$ — i.e. whenever $P\ge S_\zeta+\log\gamma^{-1}$ — which is the
only regime in which the target's own first term is below $1$. So the replacement term is
$O\bigl((\sigma'+\log\gamma^{-1})/P\bigr)$: the *same shape as the target's first term*, and
decreasing in $P$ where $P\delta$ increases. If this route closes, the $P$-cap goes entirely.

**Three gaps, stated as gaps.** This is a candidate, not a proof.

- **(G-a)** The sources read the whole oracle, so $\mathbf x$ is not independent of $H$, and the
  single-coordinate density bound must be applied at a point correlated with the conditioning.
  `lem:hit` handles the analogous problem for *membership* in $I_J$ by exhibiting a predictor;
  the same device is needed here for the *value* at $\mathbf x$, and it is not obvious that the
  predictor formulation reaches it.
- **(G-b)** $|\mathsf{Real}-\mathsf{Mid}|$ has no bound yet. The observer there receives
  $H(\mathbf x)$, a value correlated with the very oracle it is distinguishing, whereas Lemma P
  bounds only the case of an independent uniform challenge. This is the load-bearing hop.
  **Obstruction O1 below shows it is not a bookkeeping gap.**
- **(G-c)** *Closed.* The density-to-statistical-distance step needs $(P,1-\delta)$-density at
  $|T|=1$. Source card `S1` records [CDGS, Definition 1] verbatim in substance: a source is
  $(1-\delta)$-dense if "for every subset $I\subseteq[N]$,
  $H_\infty(X_I)\ge(1-\delta)\cdot|I|\cdot\log M$", and $(P,1-\delta)$-dense if it "is fixed on
  at most $P$ coordinates and is $(1-\delta)$-dense on the rest". Singletons are included and
  the fixed coordinates are excluded, which is exactly the event $\mathbf x\notin I_J$ the step
  is applied on. So $\Pr[H(\mathbf u)=v]\le M^{-(1-\delta_\zeta)}$ for $\mathbf u\notin I_J$ is
  licensed as used.

**Obstruction O1 (why (G-b) needs a new idea).** Split on $E:=\{\mathbf x\in I_J\}$, an event
determined by $(H,\mathbf z,\mathbf x)$ before either experiment diverges, so of equal
probability in both. On $E$, consistency makes the challenge *literally identical*, not merely
equal in law: conditioning on $(H,\mathbf z,\mathbf x,J=j)$, $\mathsf{Real}$ runs
$D^{H}(v,\mathbf z)$ and $\mathsf{Dec}$ runs $D^{H^{*}}(v,\mathbf z)$ with the same
$v=H(\mathbf x)=H^{*}(\mathbf x)$. So the $E$-branch is a pure oracle swap, $X_j$ against
$Y_j$ — exactly what [CDGS, Claim 3] bounds — *except for the conditioning*. Three routes and
why each fails.

- **(a) Apply Claim 3 conditioned on $(\mathbf x,v)$.** The conditional law of $H$ given
  $(\mathbf z,J=j,\mathbf x,v)$ is $X_j$ reweighted by
  $\Pi_{H,\mathbf z}(\mathbf x)\cdot\mathbb 1[H(\mathbf x)=v]$. The indicator is harmless: it
  fixes one further coordinate, and a $(P,1-\delta)$-dense source conditioned on one coordinate
  off its fixed set is $(P+1,1-\delta)$-dense. The factor $\Pi_{H,\mathbf z}(\mathbf x)$ is
  not. r3's Lemma 1 controls $\Pi_{f,\zeta}$ only through $\mathbb E[m_1m_2]\le\delta$, and its
  own counterexample there — $m_1m_2=1$ on an event of probability $\delta$, from which
  "$\mathbb E[m_1m_2]\le\delta^{2}$ is false" — is a case where the reweighting concentrates the
  posterior on a single $f$, destroying density outright.
- **(b) Let the distinguisher sample $\mathbf x$ itself.** Given $(\mathbf z,j)$ and oracle
  access to $g$, a distinguisher can run $S_1^{g},S_2^{g}$ and condition on the leakage matching
  $\mathbf z$, which restores the right law at $g=H$. But Definition `def:sources` gives the
  sources unbounded query count — they "may read all of $H$" — so the resulting $T$ is unbounded
  and Claim 3's $T\delta\log M$ is vacuous. This is the same wall that forced Lemma P through a
  uniform independent challenge to begin with.
- **(c) Bound the $E$-branch trivially.** $\Pr[E]\le P\delta$ by `lem:hit`, so
  $\Pr[E]\cdot1=P\delta$ — the term being eliminated. The $E$-branch has to be shown *small*,
  not merely bounded.

**Lead L1 (the cost of conditioning on $\mathbf x$ is exactly the $2\log N$ inside $\sigma'$).**
Route (a) fails because conditioning on $\mathbf x$ reweights $X_j$ by
$\Pi_{H,\mathbf z}(\mathbf x)$. But the *size* of that reweighting is bounded, and by exactly
the right amount. Write $p(\mathbf u):=\Pr[\mathbf x=\mathbf u\mid\mathbf z=\zeta,J=j]$ for the
marginal under $X_j$, and $S_j:=N^{2}\log M-H_\infty(X_j)$. Since
$$\Pr[H=f\mid\mathbf z=\zeta,J=j,\mathbf x=\mathbf u]=\frac{X_j(f)\,\Pi_{f,\zeta}(\mathbf u)}{p(\mathbf u)}\ \le\ \frac{X_j(f)}{p(\mathbf u)},$$
the conditioned deficiency
$S(\mathbf u):=N^{2}\log M-H_\infty(H\mid\mathbf z=\zeta,J=j,\mathbf x=\mathbf u)$ satisfies
$S(\mathbf u)\le S_j+\log(1/p(\mathbf u))$. Two bounds on that penalty:

- *On average.* $\mathbb E_{\mathbf u}[\log(1/p(\mathbf u))]=H(\mathbf x\mid\mathbf z=\zeta,J=j)\le\log N^{2}=2\log N$.
- *With slack.* $\sum_{\mathbf u:\,p(\mathbf u)<\gamma/N^{2}}p(\mathbf u)\le\gamma$, so off an event
  of probability at most $\gamma$, $\log(1/p(\mathbf u))\le2\log N+\log\gamma^{-1}$.

Checked over 400 random instances with arbitrary per-$f$ product measures $\Pi_f$, degenerate
ones included: both bounds hold, the first tight to $0.9998$.

So conditioning on the challenge point costs $2\log N+\log\gamma^{-1}$ bits of deficiency — and
$\sigma':=\sigma+2\log N$ is *defined* as "the leakage length together with the number of bits
needed to name a point of the domain". The penalty is already budgeted for in the target's own
first term $c(\sigma'+\log\gamma^{-1})q^{+}/P$. Nothing in the constants has to move to pay it.

**Why L1 does not yet close (b).** [CDGS, Claim 3] needs $X_j$ *dense*, not merely of bounded
deficiency. Re-applying [CDGS, Claim 2] to the conditioned law converts deficiency back into
density, but at a *new* fixed set — one depending on $\mathbf x$ — and Contract Remark
`rem:index` forbids exactly that: "It may not be chosen using $\mathbf x$, which is why the
index set is $\mathsf{Fun}\times(\{0,1\}^{*})^{2}$ and not anything larger." So the
re-decomposition cannot be the family; it can only be an analysis device, and then Claim 3
compares the conditioned law to *its own* bit-fixing companion rather than to $Y_j$, and the
chain does not close. What would close it is a form of Claim 3 tolerating a
bounded-deficiency perturbation of a dense source against the **original** companion. That is
the sharp question this document leaves.

**On the multiplicative form, recorded so it is not tried twice.** Card `S1` also records
$\Pr[D^{X'}=1]\le M^{T\delta}\cdot\Pr[D^{Y'}=1]$, never used in this campaign, and a
multiplicative comparison does survive conditioning on a low-probability event where an
additive one does not. It does not help here: both forms of Claim 3 require $X'$ dense, and
route (a)'s failure is the loss of density, not the additivity of the conclusion.

Until **(G-b)** is settled nothing here improves **(H1)**. (G-a) and (G-b) are the whole of the
remaining obstruction, and (G-b) is the harder of the two: it asks for a presampling bound
against an observer holding a challenge correlated with the oracle, which is precisely the case
[CDGS, Lemma 1] does not cover and which card `S1` records this campaign as having already had
to route around once.

**Remark (a second open problem, which this campaign has never engaged with).**\label{rem:second}
Contract Remark `rem:reduces` records that the implication runs backwards too: there is a family,
independent of $q$ and $D$, with
$\mathsf{Adv}_{\mathcal Y,D}\le\kappa(q)+Aq/P_0+\gamma+P_0\delta+q\delta$ for
$A:=\sigma+2+\log(1/\gamma)$ and $P_0:=\min(P,\lceil\sqrt{A/\delta}\,\rceil)$, so that
$\kappa(q)=O(\sqrt{\sigma'q^{+}\delta})$ implies `conj:main` for $P\le\sqrt{A/\delta}$ and for
every $P$ when $q=O(1)$. It then states: "the directions hold at values of $P$ separated by
$\Theta(\sqrt{q^{+}})$, and closing that is a second open problem, distinct from bounding
$\kappa(q)$."

Two things follow, and neither is a claim. First, no artifact in this campaign cites
`rem:reduces`, and a search for its converse construction across every artifact returns nothing:
the second open problem has never been worked on, and it is not the $P$-cap or the $M$-corner.
Second, the $\Theta(\sqrt{q^{+}})$ separation it names is numerically the same factor that
**(H1)** relaxes, and Corollary G1 brings Theorem E″ to the $P$ at which `thm:main`'s direction
operates. Whether that closes `rem:reduces`'s separation, or merely coincides with it, is a
question this document does not answer — and the Remark on `conj:main`'s region above is a reason
for caution, since the separation is stated per $P$ while the two directions may quantify $q$
differently. Posed here so it stops being invisible.

## 5. Gap register

- **[INHERITED: r3 Theorem C, r3 Lemma P]** — *load-bearing* for Theorem E″, Corollaries G1 and
  G2. `split-decomp-kappa-1-r3` has now been through blind review with verdict CLEAN
  (`split-decomp-kappa-1-r3-findings.md`), which discharges the "has not been through blind
  review" clause of `split-decomp-kappa-2-r2` §9's first entry; the results themselves are
  still not reproved here.
- **[INHERITED: r3 Lemma 3 steps (1)–(3), r3 Lemma 4, r3 Theorem A]** — *load-bearing* for the
  Corollary D″ step of Theorem E″ and for Corollary G2. Same blind-review status.
- **[INHERITED-UNAUDITED: Corollary D″ of `split-decomp-kappa-2-r2`]** — *load-bearing* for
  Theorem E″, and the weakest link in this document's dependency chain. **`split-decomp-kappa-2-r2`
  has never been blind-reviewed.** The campaign's one findings file for that arm,
  `split-decomp-kappa-2-findings.md`, reviews `split-decomp-kappa-2` — the *pre-revision*
  artifact, at `8c68c62` — and its tally's header states in terms that it "does NOT carry over to
  r2, having been recorded against different content". So Corollary D″ stands at zero passes of
  five. Compounding it, the triage of that earlier pass **overruled** the referee on Corollary
  D″'s constant rather than upholding it, so the one referee opinion ever formed about this
  result was rejected and never re-tested. (`split-decomp-kappa-3` and its r2 both asserted that
  r2 "has been through blind review at r1 and r2". That was false; finding A1.)
- **[GAP: §4, items (G-a) and (G-b)]** — not load-bearing for anything asserted. §4's candidate
  route is stated, not proved, and Theorem E″ does not use it. (G-c) is closed against card
  `S1`. Obstruction O1 records why (G-b) is not a bookkeeping gap: the $E$-branch is a pure
  oracle swap, but every route to [CDGS, Claim 3] on it either destroys the density Claim 3
  needs or costs unbounded queries. Lead L1 quantifies the density loss — conditioning on
  $\mathbf x$ costs $2\log N+\log\gamma^{-1}$ bits of deficiency, exactly the $2\log N$ that
  $\sigma'$ is defined to carry — and names what would close it: a form of Claim 3 tolerating a
  bounded-deficiency perturbation of a dense source against the original bit-fixing companion.
- No `[GAP]` occurs in §§1–3.

## 6. External results used

- **[r3, Theorem C]**, **[r3, Lemma P]**, **[r3, Theorem A]** — `split-decomp-kappa-1-r3`.
  Restated where used; not reproved.
- **[kappa-2-r2, Corollary D″]** — `split-decomp-kappa-2-r2` §6. Restated; not reproved.
- **[CDGS, Claim 2]** (Coretti, Dodis, Guo, Steinberger, *Random Oracles and Non-Uniformity*,
  ePrint 2017/937). CARD (S1). Enters §1–§3 only transitively through r3's Lemma P; cited
  directly in §4, which proves nothing.
- $\lceil t\rceil\le t+1$; $\mathrm{SD}\le\sum_v(p_v-1/M)^{+}$; $e^{u}-1\le ue^{u}$.
  RESTATED, standard. (`split-decomp-kappa-3` used $\lfloor t\rfloor\ge t/2$ for $t\ge1$ in
  Corollary G1; the repair of F1 replaces it with $\lceil t\rceil\le t+1$, and it is no longer
  needed anywhere.)

### END OF ARTIFACT split-decomp-kappa-3-r3 ###
