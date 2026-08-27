# split-decomp-kappa-4-r2 — the $P$-window at fixed $q$; the $q$-free window costs $\sqrt{q^{+}}$

**Revision of `split-decomp-kappa-4` after a six-referee blind audit** — five passes on the
artifact spanning two model families (lenses: the definitional step, arithmetic and constants,
quantifier order, case coverage, citation fidelity) and one on three unmerged simplification
claims. **No theorem is withdrawn and no constant moves the wrong way.** Every defect was in what
the document said *about* its results, which is the class its own lineage keeps failing in.

**What the audit confirmed, unanimously and after adversarial attempts to break it.** Lemma H0 —
that a $P_0$-mixture with $P_0\le P$ *is* a $P$-mixture, read off `def:bf`'s $|I|\le P$ — was
attacked by four referees independently, each trying to construct a reading of `def:bf` on which it
fails. None could; one corroborated the "at most $P$" convention against card S1's quotation of
[CDGS, Definition 1]. The arithmetic referee re-derived every inequality by hand, reproduced both
reported grid sizes exactly, found **no class-(B) error**, and confirmed $c=2$ and $C=13$ follow
from the displayed inequalities rather than from the grid. The case-coverage referee confirmed the
case split is exhaustive on $\mathbb N$ with no boundary gap. No referee found any violation of
`rem:index`, and none found a leak of $D$, $\mathbf x$ or the challenge into either family.

Upheld and repaired here:

- **B1 (class A, the serious one).** Theorem H′ read "Suppose **(H2)** holds at $q$" and then
  quantified its conclusion over *every* $q$ — $q$ free in the hypothesis, rebound in the
  conclusion. Read literally the hypothesis is vacuously satisfiable at $q=0$, where $\mu'(0)=0$,
  so the theorem would have delivered `conj:main` for every $M$ and contradicted its own §4. The
  correct hypothesis is **(H2) at every $q$**, i.e. $M\le\sigma'/(2\delta)$, which is strictly
  stronger and was never written down. **Corrected in §3**, with a non-vacuous witness supplied.
  Three referees raised this; the one that gave an instance gave a vacuous one, and the witness has
  been replaced rather than the finding waived.
- **B2 (class A).** $A\ne\sigma'$. `rem:reduces` caps at $\lceil\sqrt{A/\delta}\,\rceil$ with
  $A:=\sigma+2+\log(1/\gamma)$; this document caps at $\lceil\sqrt{\sigma'/\delta}\,\rceil$. They
  coincide only at $\gamma=N^{-2}$ and diverge without bound as $\gamma\downarrow0$. "The same
  capping, at the same $q$-free point" and "reproduces" were wrong. **Corrected in §3.**
- **B3 (class A).** "The separation is *exactly* the price of $q$-independence, and nothing else"
  claimed necessity from an achievability result, contradicted §4's own listing of the question as
  open, and overrode `split-decomp-kappa-3-r4` §4's `rem:second`, which had warned that
  `rem:reduces`'s $\sqrt{q^{+}}$ is a separation *in $P$ between two directions of a biconditional*
  while this one is a *degradation of $C$ at fixed $P$*. Four referees raised it. **Corrected in
  §0 and §3**; the caution stands and is now quoted rather than overridden.
- **B4 (class A).** The document misdescribed its own evidence: "$q\le10^{7}$" and "$P$ swept
  across the whole axis" were loop bounds, and the vacuity filter meant **no point with
  $q\ge10^{3}$ was ever evaluated** — $\sqrt{q^{+}}$, Theorem H′'s whole subject, reached only
  $\sqrt{11}$. The check is rewritten and rerun; see §2.
- **B5 (class C).** $N,M\ge2$ was used three times and never stated, and $\sigma'\ge2$ was asserted
  with no derivation. Four referees. At $N=1$, $\gamma_0=1\notin(0,1)$, the sub-assertion
  "$N^{-2}\le1/4$" is false, and $\sigma=0$ gives $P_0=0\notin\mathbb N$; at $M=1$ Lemma P declines
  to construct the family. **Stated as a standing hypothesis in §1.**
- **B6–B10 (class D).** Summary lines scoped wrongly ("closes completely", "an artefact of the
  quantifier order alone") against §3–§4's own narrower claims; §6's register omitted Lemma P,
  Corollary D″, `rem:index` and `rem:order`; "(H2) is a condition on $M,q,\delta$ alone" omits $N$
  and $\sigma'$; "$P\delta$ never needs to exceed $S$" is off by an additive $\delta$; Corollary G2
  was credited with a fact shown inside its proof; Lemma H1 was titled "two bounds" and stated
  three; and the worst observed constant was printed as $12.0000$, rounding away the strict
  inequality that is the only reason the number is interesting. All corrected.

**One improvement beyond the findings.** Lemma H1's third bound is sharpened from $N^{-2}\le S$ to
$N^{-2}\le\tfrac14S$, valid for every $N\ge2$. Two referees observed that the crude form was the
whole of r1's slack. $C=13$ now carries three quarters of a unit rather than being reached exactly,
and the sharpened form is what the floor-cap variant of the simplification audit needs.

**Class (E), charged to the requester and not to the artifact.** Both r1 and this revision cite
`PROGRESS.md` for campaign-status claims, and `PROGRESS.md` was not in the referee package. Three
referees correctly recorded those claims as unverifiable within scope; one issued a source request;
one disclosed reading it out of package and noted it is not independent corroboration, having been
written concurrently. The §5 claims sourced to the *dependencies* — zero passes, the overruled
objection on Corollary D″ — were checked and confirmed against DEP-A and DEP-B's own text.

**Invariant, checked mechanically.** Against `split-decomp-kappa-4`: §0 and §5 differ only in the
sentences the findings name; §1 gains the standing hypothesis and the sharpened Lemma H1; §2 gains
the corrected evidence remark; §3 gains the corrected hypothesis and two replaced remarks; §4 gains
two corrections; §6 gains three register entries. **No theorem statement changes except Theorem
H′'s hypothesis**, which is strengthened, and no constant in Theorem H changes.

**Verification status: this revision has zero passes of five.** It answers a five-pass audit of its
predecessor, which is not the same as having been audited itself.

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

**Standing hypothesis: $N,M\ge2$ (finding B5).** Every dependency states it — Theorem E″ opens
"Let $N,M\ge2$", r3's Lemma P opens "Let $N\ge2$, $M\ge2$" and notes its construction "divides by
$\log M$ and is stated for $M\ge2$ only" — and r1 inherited it silently. It is what licenses
$\sigma'\ge2$, via $2\log N\ge2$ and $\sigma\ge0$, and it is used three times below. At $N=1$ the
construction genuinely fails: $\gamma_0=\max(\gamma,1)=1\notin(0,1)$, so Theorem E″ cannot be
invoked, and with $\sigma=0$ one gets $t_q=0$ and $P_0=0\notin\mathbb N$. At $M=1$ the family is
not constructed by its own source. Neither case is in scope.

Fix an instance $(N,M,\sigma_1,\sigma_2,\delta)$ with $N,M\ge2$ and a split $\delta$-unpredictable
pair $(S_1,S_2)$. Given a requested $P\in\mathbb N$ and $\gamma\in(0,1)$, put
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
$P_0\le\lceil t_q\rceil\le t_q+1$; hypothesis **(H2)** does not mention $P$, so it is unaffected. (It is a condition on $M,q,\delta$
*and* on $N,\sigma'$; only the absence of $P$ is load-bearing here.) $\square$

**Lemma H1 (three slack bounds).** $\log\gamma_0^{-1}\le\log\gamma^{-1}$; $\log\gamma_0^{-1}\le\sigma'$,
hence $\sigma'+\log\gamma_0^{-1}\le2\sigma'$; and $N^{-2}\le S$.

*Proof.* $\gamma_0\ge\gamma$ gives the first. For the second,
$\gamma_0\ge N^{-2}$ gives $\log\gamma_0^{-1}\le2\log N\le\sigma'$ by the definition of $\sigma'$.
For the third, $\delta\ge1/N$ (a uniform guess predicts $x_i$ with probability $1/N$, so no
$\delta<1/N$ is achievable), $\sigma'\ge2$ — which needs $N\ge2$ — and $q^{+}\ge1$ give
$S\ge\sqrt{2/N}$, whence
$$N^{-2}\le\tfrac14S\iff N^{-2}\le\tfrac14\sqrt{2/N}\iff N^{-3}\le\tfrac12,$$
true for every $N\ge2$. The sharper $S/4$ costs nothing and is stated because the crude
$N^{-2}\le S$ of r1 was the whole of r1's slack. $\square$

The first bound is what keeps $c$ at $2$: without it the clamp would cost a factor in the
leading term rather than in the additive one.

## 2. Theorem H — at fixed $q$, the bound holds at every $P$

**Theorem H.** Fix $q\in\mathbb N\cup\{0\}$ and suppose **(H2)**. For every $P\in\mathbb N$ and
every $\gamma\in(0,1)$, the family $\mathcal Y=\mathcal Y^{P_0,\gamma_0/2}$ of §1 consists of
$P$-mixtures consistent with their indices, depends only on $(S_1,S_2,P,\gamma,q)$, and satisfies,
for every $q$-query challenge-oblivious observer $D$ and with no restriction on challenge
resolution,
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}\ +\ 13\,S\ +\ \gamma .$$
That is, the Contract's `conj:main` **display** with $c=2$, $C=13$ and no hypothesis on $P$ — but
not `conj:main` itself, which requires the family to depend only on $(S_1,S_2,P,\gamma)$. A
$q$-dependent family satisfies a relaxation of the conjecture. (r1's sentence here read "That is,
the Contract's `conj:main` with $c=2$, $C=13$", which in isolation overclaims — finding B7.)

*Proof.* Lemma H0 licenses Theorem E″ at $(P_0,\gamma_0)$, which gives
$$\mathsf{Adv}_{\mathcal Y,D}\ \le\ \frac{2(\sigma'+\log\gamma_0^{-1})q^{+}}{P_0}+8S+\gamma_0 .$$
Two cases.

*Case (a), $P\le\lceil t_q\rceil$.* Then $P_0=P$, and by Lemma H1
$\log\gamma_0^{-1}\le\log\gamma^{-1}$, so the first term is at most $2Bq^{+}/P$, which is the
target's own first term with $c=2$. For the additive term,
$\gamma_0\le\gamma+N^{-2}\le\gamma+\tfrac14S$. Total: $2Bq^{+}/P+8\tfrac14S+\gamma$.

*Case (b), $P>\lceil t_q\rceil$.* Then $P_0=\lceil t_q\rceil\ge t_q$, and by Lemma H1
$\sigma'+\log\gamma_0^{-1}\le2\sigma'$, so
$$\frac{2(\sigma'+\log\gamma_0^{-1})q^{+}}{P_0}\ \le\ \frac{4\sigma'q^{+}}{t_q}
\ =\ 4\sigma'q^{+}\sqrt{\frac{\delta}{\sigma'q^{+}}}\ =\ 4S .$$
With $\gamma_0\le\gamma+\tfrac14S$ again, the total is at most $12\tfrac14S+\gamma\le13S+\gamma$, and the target's first term
is non-negative.

Both cases are dominated by $2Bq^{+}/P+13S+\gamma$. $\square$

**Remark (the $P$-window closes for this statement, and where the constants went).** Against
Theorem E″ the trade is exact: **(H1)** is deleted outright and $C$ moves $8\to13$, while $c$ does
not move. Of the five extra units, four are the capping in case (b) and a quarter is the
$\gamma$-clamp; three quarters go unused.

**The evidence, described accurately — r1 described its own grid wrongly, finding B4.** r1 reported
"$q\le10^{7}$" and "$P$ swept across the whole axis". Those were *loop bounds*. The vacuity filter
$8\sqrt{\sigma'q^{+}\delta}<1$ requires $\sigma'q^{+}\delta<1/64$, and with $\delta\ge1/N$ and
$N\le2^{20}$ that forces $q^{+}<410$: **no point with $q\ge10^{3}$ was ever evaluated**, so
$\sqrt{q^{+}}$ — Theorem H′'s entire subject — was exercised only to $\sqrt{11}\approx3.3$. $P$
took nine sampled values, not a sweep; $\delta$ took five, not an interval.

The check is rewritten. `c/0010/campaign/checks/cap-fixed-q.py` now runs $N$ to $2^{44}$, which
makes $q=10^{7}$ non-vacuous and exercises $\sqrt{q^{+}}$ to $3162$; evaluates **(H2)** explicitly
and skips points where it fails, since the theorems claim nothing there; and checks $P_0\ge1$,
which Theorem E″ requires and r1 never verified. **64224 points, zero failures**, for Theorem H,
for Theorem H′, and for the floor-cap variant.

Two cautions on what a grid can show. Its worst observed constant is $12.0000000000$, and the value
is *strictly* above $12$ — which is the whole point, being what shows $C=12$ fails; r1 printed it
rounded to $12.0000$ and lost that. And the grid measures the *actual* $\gamma_0/S$, not the
$\le\tfrac14$ that Lemma H1 supplies, so **it cannot distinguish the proved constant from the
observed one**. It corroborates; it does not establish. $C=13$ is established by the displayed
inequalities alone, as the audit's arithmetic referee independently confirmed.

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

**Theorem H′.** Suppose **(H2)** holds at **every** $q\in\mathbb N\cup\{0\}$ — equivalently, by
`split-decomp-kappa-3-r4` §2's computation, $M\le\sigma'/(2\delta)$, the intersection binding at
$q=1$. The family $\mathcal Y'$ depends only on $(S_1,S_2,P,\gamma)$ — not on $q$ — consists of $P$-mixtures consistent with their indices, and
satisfies, for every $P\in\mathbb N$, every $q\in\mathbb N\cup\{0\}$ and every $q$-query
challenge-oblivious observer $D$,
$$\mathsf{Adv}_{\mathcal Y',D}\ \le\ \frac{2(\sigma'+\log\gamma^{-1})q^{+}}{P}
\ +\ \bigl(4\sqrt{q^{+}}+9\bigr)S\ +\ \gamma .$$

*Proof.* As in Lemma H0, with **(H1)** at $P_0'$ holding for *every* $q$ at once, since
$P_0'\le\lceil t_0\rceil\le t_0+1\le t_q+1$ by $t_0\le t_q$. **(H2)** is *not* uniform in $q$ and
is supplied at every $q$ by hypothesis; this is the step r1 omitted. Theorem E″ then applies at
$(P_0',\gamma_0)$ for each $q$. Case (a), $P\le\lceil t_0\rceil$, is as before and gives
$2Bq^{+}/P+9S+\gamma$. Case (b), $P>\lceil t_0\rceil$: now $P_0'\ge t_0=\sqrt{\sigma'/\delta}$, so
$$\frac{4\sigma'q^{+}}{t_0}\ =\ 4\sigma'q^{+}\sqrt{\frac{\delta}{\sigma'}}\ =\ 4q^{+}\sqrt{\sigma'\delta}
\ =\ 4\sqrt{q^{+}}\cdot S ,$$
using $S=\sqrt{q^{+}}\sqrt{\sigma'\delta}$. Adding $8S$ and $\gamma_0\le\gamma+\tfrac14S$ gives the
claim, with a quarter-unit to spare. $\square$

**Remark (the hypothesis is strictly stronger than **(H2)**, and r1 got this wrong — finding B1).**
r1 wrote "Suppose **(H2)** holds at $q$" and then quantified its conclusion over *every* $q$,
leaving $q$ free in the hypothesis and rebinding it in the conclusion. Three readings, all
defective: read at one $q$, the hypothesis is *vacuously* satisfiable at $q=0$, since $\mu'(0)=0$
makes **(H2)** free there, so the theorem would deliver `conj:main` for every $M$ and contradict its
own §4; read per-$q$ it is true but is then not `conj:main`, which demands one family good at every
$q$; only the intersection reading is both true and sufficient, and r1 never wrote it down.

The distinction is not idle. A non-vacuous witness: $N=2^{12}$, $\sigma=0$ (so $\sigma'=24$),
$\delta=2^{-12}$, $M=2^{16}$. Then $8\sqrt{\sigma'q^{+}\delta}<1$ at both $q=0$ and $q=1$;
**(H2)** holds at $q=0$; and at $q=1$ it fails on both arms, $2\delta\sqrt M=0.125$ and
$\mu'(\min(M,N^{2}))=0.315$ against $S=0.108$. So there is an admitted, non-vacuous instance at
which r1's hypothesis holds and its conclusion is unproved. (The referee raising this offered an
instance vacuous at both $q$, where the target exceeds $1$ and the claim holds trivially; the
finding is upheld, its witness replaced.)

**Remark (an analogue of `rem:reduces`; what is and is not shown — findings B2, B3).** The
Contract's `rem:reduces` gives a $q$-free family with
$\mathsf{Adv}\le\kappa(q)+Aq/P_0+\gamma+P_0\delta+q\delta$ at
$P_0=\min(P,\lceil\sqrt{A/\delta}\,\rceil)$, $A:=\sigma+2+\log(1/\gamma)$, concluding `conj:main`
"for $P\le\sqrt{A/\delta}$, and for every $P$ when $q=O(1)$", the two directions separated by
$\Theta(\sqrt{q^{+}})$ for growing $q$. Two corrections to r1.

**It is not the same cap (B2).** r1 called this "the same capping, at the same $q$-free point".
$A$ carries a $\log(1/\gamma)$ that $\sigma'=\sigma+2\log N$ does not, and has $+2$ where $\sigma'$
has $+2\log N$. They coincide only at $\gamma=N^{-2}$ and diverge without bound as
$\gamma\downarrow0$ — at $\gamma=10^{-30}$, which this document's own check exercises, $A$ exceeds
$\sigma'$ by roughly $100$. Theorem H′ is an *analogue*, run against Theorem E″'s machinery rather
than against $\kappa$ directly. It is not a reproduction.

**Only one direction is shown (B3).** r1 said Theorem H shows the separation is "*exactly* the
price of $q$-independence, and nothing else". That claims a necessity this document does not
establish. What is proved is achievability: $q$-dependence **suffices** to remove the
$\sqrt{q^{+}}$, within this route. No lower bound against $q$-free families appears anywhere here,
and §4 lists finding such a family — or showing none exists — as open, which r1's "exactly"
contradicted. `split-decomp-kappa-3-r4` §4's `rem:second` had already warned against precisely this
identification, noting that `rem:reduces`'s $\Theta(\sqrt{q^{+}})$ is a separation *in the value of
$P$ between two directions of a biconditional*, whereas the $\sqrt{q^{+}}$ here is a *degradation
of the constant $C$ at fixed $P$*. Different objects, same exponent. r1 overrode a documented
caution without argument; the caution stands.

What survives is narrower and still worth having: this is the campaign's first engagement with
`rem:reduces`, recorded as cited by no artifact, and it supplies one direction of its question.

**Remark (what this does, and does not do, to the campaign's status line — finding B6).** The
window $t_0+1<P<N^{2}$ is stated for `conj:main` with $C$ absolute and a $q$-free family. **That
window does not close here, and r1's summary saying it "closes completely" was scoped wrongly.**
What is true: on that window, and on the smaller region $M\le\sigma'/(2\delta)$, Theorem H′ gives
the bound with $C(q)=4\sqrt{q^{+}}+9$ — non-absolute, hence not `conj:main` — and Theorem H gives
it with $C=13$ once $q$ may be fixed first, which is a relaxation of `conj:main`, not `conj:main`.
The honest residue on the $P$-axis is **a $\sqrt{q^{+}}$ in the constant under $q$-free families,
on $M\le\sigma'/(2\delta)$**: narrower than "an uncovered region", and wider than r1 claimed.

## 4. What this does and does not settle

**Settled, on region (H2):** the $P$-axis, at fixed $q$, in full. No $P$-hypothesis survives in
Theorem H.

**Not settled, and not touched:**

- **The $M$-corner.** **(H2)** is carried unchanged through both theorems. Everything here is
  conditional on it, and `PROGRESS.md` §2.2's open question — whether the first arm of Corollary
  D″ can be made $M$-free — is exactly as open as before. At $q=0$, **(H2)** is vacuous for every $M$, since
  $\mu'(0)=0$, so Theorem H is unconditional there. (r1 credited Corollary G2's *conclusion*; the
  fact is shown inside G2's proof, and G2's statement carries a $P\le3\sqrt{\sigma'/\delta}$
  hypothesis Theorem H does not need.)
- **Strict `conj:main` with absolute $C$.** Theorem H′ leaves the $\sqrt{q^{+}}$. Closing it is
  the Contract's `rem:reduces` second open problem, now with a sharper description: find a
  $q$-free family achieving what the $q$-aware cap achieves, or show none exists.
- **The lower-bound side.** Nothing here bears on Proposition F or on tightness.

**A redirection this forces, and it is the practical point.** `split-decomp-kappa-3-r4` §4 spends
the campaign's deepest effort — Obstruction O1, Lead L1, the request for a new form of [CDGS,
Claim 3] tolerating a bounded-deficiency perturbation — on removing $P\delta$ so that large $P$
can be afforded. Theorem H shows that at fixed $q$ **that work is unnecessary**: one never needs a
fixed set larger than $\lceil t_q\rceil$, so $P\delta$ never needs to exceed $S+\delta$ (r1 said
$S$; $\lceil t_q\rceil\delta\le(t_q+1)\delta=S+\delta$, which is why Theorem E″'s own proof carries
this term as $\tfrac{17}{16}S$). §4's programme
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
- **[r3, Lemma P]** — `split-decomp-kappa-1-r3` §6. The family $\mathcal Y^{P,\gamma}$ itself,
  constructed in §1 at $(P_0,\gamma_0)$. Restated; not reproved. (Named in r1's §1 and omitted from
  r1's register.)
- **[kappa-2-r2, Corollary D″]** — §6 there. Enters only transitively, as the extraction term inside
  Theorem E″. Registered because r1's own §5 calls it load-bearing while r1's register omitted it.
- **[Contract, Remarks `rem:index`, `rem:order`]** — quoted as licensing conditions in Lemma H0 and
  in §2's remarks. Both omitted by r1.
- $\lceil t\rceil\le t+1$; $t_q=t_0\sqrt{q^{+}}$; $\delta\ge1/N$; $\sigma'\ge2$ (needs $N\ge2$).
  RESTATED, standard.

### END OF ARTIFACT split-decomp-kappa-4-r2 ###
