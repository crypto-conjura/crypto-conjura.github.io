# INTERMEDIATE I02 — Rung R2: Degree-$d$ set rung (ℤ₂, general Boolean-valued)

**Campaign:** c/0023 (PCC, inverse-polynomial regime) · **Parent contract:** `../CONTRACT.md` (depth 0)
**Ladder position:** R2 of the approved ladder (`../PROGRESS.md`); the rung directly above the frozen R1
**Status:** ACTIVE TARGET (the single active statement per HARNESS §2.4)
**Cites as a black box:** I01 / rung R1, ESTABLISHED+FROZEN 2026-08-27, proof artifact `proofs/0023-prover-1.md` — statement below under "Frozen inputs". Never re-verify it.

## Descent block (rung, not a weakening)

* A **special case** of Conjecture `conj:main` restricted to 𝒴 = ℤ₂ and to
  normalized indicators of degree-≤$d$ sets; IMPLIED by the conjecture.
* **Strictly contains R1:** every $\le d$-window cylinder indicator has degree
  $\le d$, but a degree-$\le d$ set need not be a $d$-junta.
* **Does NOT establish:** neither PCC nor ℤ₂-PCC. One rung.
* **Refutation scope:** identical to R1's — a sub-inverse-polynomial
  incompatible family in this class kills ℤ₂-PCC, not PCC (the group is
  existentially quantified); the ladder would re-base on another group.

## Statement (to be proved or refuted)

There exist $c_1\in(0,1]$, $c_2>0$, and $\delta:\mathbb{N}\to(0,1]$ with
$\delta(d)\ge c_1 d^{-c_2}$ for all $d\ge 1$, such that for all $d,N\in\mathbb{N}$
and all finitely supported distributions $\mathbf{F},\mathbf{G}$ over

$$\mathcal{C}^{\mathrm{ind}}_d:=\bigl\{\mathbf{1}_A/\|\mathbf{1}_A\|_2\ :\ \emptyset\ne A\subseteq\{\pm1\}^N,\ \deg(\mathbf{1}_A)\le d\bigr\}$$

satisfying, for every $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf{F}}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb{E}_{g\sim\mathbf{G}}[\mathrm{Inf}_i(g)]\le\delta(d)$,
there exist $f\in\mathrm{supp}\,\mathbf{F}$, $g\in\mathrm{supp}\,\mathbf{G}$,
and $x\in\{\pm1\}^N$ with $f(x)\,g(x)\ne 0$.

Unit norm is automatic (the class is normalized). Degree, norm and influence
are the parent Contract's, specialised to $\mathcal{Y}=\mathbb{Z}_2$;
$\deg(\mathbf{1}_A)$ is the degree of the $\{0,1\}$-valued indicator's own
multilinear expansion, **not** of the normalized function (normalization is a
positive scalar and does not change degree).

**Combinatorial form.** For indicators the conclusion is again exactly
$A\cap B\ne\emptyset$ for some pair, so the rung says: two cross-disjoint
families of degree-$\le d$ subsets of the cube cannot both spread their
per-coordinate average influence below an inverse polynomial in $d$,
uniformly in $N$.

## Frozen inputs (cite as black boxes; do not re-verify)

* **I01 / R1 (FROZEN).** The same statement with $\mathcal{C}^{\mathrm{ind}}_d$
  replaced by the $\le d$-window cylinder-pattern class
  $\mathcal{C}^{\mathrm{junta}}_d$, established with $\delta(d)=1/(3d)$
  ($c_1=1/3$, $c_2=1$), and tight in the sense that no $\delta(d)\ge 1/(2d)$
  witnesses it (the $d\times d$ grid distributions). Proof: `0023-prover-1`.
* **K1 (card S1, ACC22 Thm 4.4).** The full ℤ₂ statement — hence this rung —
  holds for every $\delta<2^{-d}/d$. The rung's content is the window
  $[2^{-d}/d,\ 1/(2d))$.
* **Grid ceiling (card S1 Claim B.3; reproved inline in `0023-prover-1`).**
  $\mathcal{C}^{\mathrm{junta}}_d\subset\mathcal{C}^{\mathrm{ind}}_d$ contains
  the grid distributions at average influence exactly $1/(2d)$ with no
  compatible pair, so any witnessing $\delta$ here also needs
  $\delta(d)<1/(2d)$, i.e. effectively $c_2\ge 1$.

## The trap this rung exists to avoid (recorded non-solution)

A degree-$\le d$ Boolean function is a junta on $M(d)$ coordinates for some
$M(d)=2^{\Theta(d)}$ (the Nisan–Szegedy-type theorem — **[MEMORY], must be
carded before any proof cites it; carding is this rung's first errand**).
Substituting $M(d)$ for the window size $d$ in R1's proof therefore yields
only $\delta(d)\approx 1/(2M(d))=2^{-\Theta(d)}$ — no better than K1, hence
**no progress on this rung**. An artifact whose threshold degrades
exponentially in $d$ by this route is a PARTIAL, not a proof of R2, and must
say so in its verdict.

Consequently the honest complexity parameter must be $d$ itself, not the
junta size. One elementary fact is available for free and is the natural
poly($d$) substitute for "window of size $\le d$" (any prover may re-derive
it in one line; it is not a citation): for every unit-norm $f$ of degree
$\le d$,
$$\sum_{i=1}^{N}\mathrm{Inf}_i(f)=\sum_{S}|S|\,\hat f(S)^2\le d\sum_S \hat f(S)^2 = d .$$
So each function carries a **total** influence budget of at most $d$,
uniformly in $N$, whether or not it is a $d$-junta. Whether R1's payment
argument can be re-based on this budget (charging payment against influence
mass rather than against a bounded window) is the rung's central question,
not an established route — it is flagged here as the orchestrator's reading
of the generalization hypothesis, unverified.

## What counts

- [x] **Proof:** any inverse-polynomial $\delta$ (so any $c_1,c_2$); as above,
  $c_2\ge 1$ is forced.
- [x] **Refutation:** a family of cross-disjoint degree-$\le d$ set pairs whose
  maximal per-coordinate average influence is below every inverse polynomial
  along an infinite sequence of $d$.
- [x] **Partials (valuable; settle nothing):** any threshold strictly between
  $2^{-d}/d$ and $1/\mathrm{poly}(d)$ — e.g. $e^{-d^{\alpha}}$,
  $e^{-\mathrm{polylog}\,d}$ — with the threshold declared; or the rung for a
  declared sub-class of degree-$d$ sets (bounded density, symmetric sets,
  sets whose indicator is a decision-tree/DNF of bounded size), each recorded
  against this file with its restriction stated.

**NOT acceptable:** δ depending on $N$; max-over-support in place of average
influence; the junta-substitution route sold as a proof of R2 (see the trap
above); re-deriving or re-verifying I01.

## Known boundary specific to this rung

* **The junta and full-class frontiers already diverge (refuter-certified,
  not verified as theorem — `0023-refuter-2`, `0023-refuter-1`).** At $d=2$
  the exact frontier inside $\mathcal{C}^{\mathrm{junta}}_2$ is $1/4=1/(2d)$,
  while in the *full signed* class an incompatible pair exists at $1/5$. The
  $1/5$ witness is **not** in $\mathcal{C}^{\mathrm{ind}}_2$ (its $g$ is not
  $\{0,c\}$-valued), so it does not bound this rung — but it shows the
  indicator restriction is doing real work, and the first refuter question
  here is exactly where $\varepsilon^*_{\mathrm{ind}}(d)$ sits between the two.
* **Scout status.** R2 has not been searched as a standalone object; the
  campaign-level sweep (`0023-scout-1`) and the R1 micro-sweep
  (`0023-scout-2`, which killed cross-intersecting-family, spread-lemma,
  subcube-partition and AA-specialisation routes) are the prior art on
  record.

## Generalization hypothesis (binding on technique choice)

The mechanism converting "$\deg\le d$" into effective-spread structure **with
poly($d$) losses** must survive to R3, where level sets of nonnegative
degree-$d$ functions replace sets. A proof leaning on exact
$\{0,1\}$-valuedness beyond granularity-type facts, or on the $2^{\Theta(d)}$
junta size, dies at R3 and is a recorded detour.

## Interpretation rule

As in the parent Contract: if any part admits more than one reading, STOP and
report it; do not resolve it yourself.
