# INTERMEDIATE I01 — Rung R1: Spread-junta indicator rung (ℤ₂, windows ≤ d)

**Campaign:** c/0023 (PCC, inverse-polynomial regime) · **Parent contract:** `../CONTRACT.md` (depth 0)
**Ladder position:** R1 of the approved ladder (`../PROGRESS.md`, approved by the human 2026-08-27)
**Status:** ACTIVE TARGET (the single active statement per HARNESS §2.4)

## Descent block (rung, not a weakening)

* This is a **special case** of Conjecture `conj:main` restricted to 𝒴 = ℤ₂
  and to normalized cylinder-pattern indicators; it is IMPLIED by the
  conjecture (any witnessing δ for ℤ₂-PCC witnesses R1).
* **Does NOT establish:** neither PCC nor ℤ₂-PCC. A proof of I01 is one rung.
* **Refutation scope:** exhibiting, over ℤ₂, incompatible R1-class pairs at
  influence levels below every inverse polynomial (for infinitely many d)
  refutes **ℤ₂-PCC** outright (the class is inside the full ℤ₂ class) — but
  NOT PCC, whose group is existentially quantified; the ladder then re-bases
  on another group. This rung is the campaign's designated falsification
  honeypot.

## Statement (to be proved or refuted)

There exist $c_1\in(0,1]$, $c_2>0$, and $\delta:\mathbb{N}\to(0,1]$ with
$\delta(d)\ge c_1 d^{-c_2}$ for all $d\ge 1$, such that for all $d,N\in\mathbb{N}$
and all finitely supported distributions $\mathbf{F},\mathbf{G}$ over the class

$$\mathcal{C}^{\mathrm{junta}}_d:=\Bigl\{\tfrac{\mathbf{1}_A}{\|\mathbf{1}_A\|_2}\ :\ A=\{x\in\{\pm1\}^N: x_J\in P\},\ J\subseteq[N],\ |J|\le d,\ \emptyset\ne P\subseteq\{\pm1\}^J\Bigr\}$$

satisfying, for every $i\in[N]$,
$\mathbb{E}_{f\sim\mathbf{F}}[\mathrm{Inf}_i(f)]\le\delta(d)$ and
$\mathbb{E}_{g\sim\mathbf{G}}[\mathrm{Inf}_i(g)]\le\delta(d)$,
there exist $f\in\mathrm{supp}\,\mathbf{F}$, $g\in\mathrm{supp}\,\mathbf{G}$,
and $x\in\{\pm1\}^N$ with $f(x)\,g(x)\ne 0$.

Unit norm and $\deg\le d$ are automatic for the class (a $|J|$-junta indicator
has degree $\le |J|$). Norms, degree, influence: as in the parent Contract's
Definitions over $\mathcal{Y}=\mathbb{Z}_2$ ($\{\pm1\}$-coordinates,
$\mathrm{Inf}_i(f)=\sum_{S\ni i}\hat f(S)^2$ after normalization).

**Equivalent combinatorial form.** For indicators the conclusion is exactly
$A\cap B\ne\emptyset$ for some pair, and $A\cap B=\emptyset$ iff the two
patterns' projections to the shared window $J_A\cap J_B$ are disjoint. So the
rung says: two families of $\le d$-window cylinder patterns that are
**cross-disjoint** (every pair conflicts on its shared window) cannot both
have all per-coordinate average influences below $\delta(d)$, with $\delta$
inverse-polynomial in $d$ and independent of $N$.

## What counts

- [x] **Proof:** any $c_1, c_2$ (equivalently any inverse-polynomial δ). Per
  the parent Contract and card S1 (Claim B.3: the $d\times d$ grid
  distributions live in this class at per-coordinate average influence
  exactly $1/(2d)$), any witnessing δ must satisfy $\delta(d)<1/(2d)$, so
  effectively $c_2\ge 1$; a proof at $\delta(d)=c/d^{2}$ or even $c/d^{100}$
  settles the rung.
- [x] **Refutation:** as in the Descent block (sub-inverse-polynomial
  incompatible families, infinitely many d).
- [x] **Partials:** thresholds between K1's $2^{-d}/d$ (settled — card S1,
  ACC22 Thm 4.4, which covers the full class hence this one) and
  $1/\mathrm{poly}(d)$: e.g. $e^{-d^\alpha}$ within this class. Valuable,
  settles nothing; record against this file with its own declared threshold.

**NOT acceptable:** δ depending on N; replacing average influence by
max-over-support; patterns of window size $>d$; treating the "Rung 0"
conjunction calibration (planner-level, unverified) as established.

## Known boundary (context; cite only through cards)

* **K1 (card S1, ACC22 Thm 4.4):** the full ℤ₂ statement — hence this rung —
  holds for all $\delta<2^{-d}/d$. The rung's content is entirely the window
  $[2^{-d}/d,\ 1/(2d))$.
* **Grid ceiling (card S1, Claim B.3 + refuter artifact 0023-refuter-1 §3):**
  the row/column grid distributions are in $\mathcal{C}^{\mathrm{junta}}_d$
  with all average influences exactly $1/(2d)$ and no compatible pair, so no
  δ at or above $1/(2d)$ can witness the rung.
* **Conjunction subclass (planner calibration, UNVERIFIED as a written
  artifact):** for conjunction patterns only, a union bound reportedly gives
  the rung at every $\delta(d)<1/(2d)$, optimally. A prover may redo this
  four-line argument inline (it is short) but may not cite it.
* **Full-class frontier (refuter artifact 0023-refuter-1, computationally
  certified, not five-pass verified):** in the *full* signed class,
  incompatible pairs exist at $\varepsilon^*(2,4)=1/5<1/4$ and asymptotically
  $(4/11+o(1))/d$ — those constructions are NOT in this rung's indicator
  class; whether richer-than-conjunction patterns push the *indicator-class*
  frontier below $\Theta(1/d)$ is exactly what the rung-level Refuter must
  probe.

## Generalization hypothesis (binding on the prover's technique choice)

The proof should be a union-bound **replacement** — a weighted
counting/entropy argument showing cross-disjointness of spread bounded-window
pattern families forces some coordinate to carry $\ge 1/\mathrm{poly}(d)$
average influence — because that engine is what R2/R3 and the top rung can
inherit. A proof exploiting exact pattern finiteness (constants like
$2^{2^d}$ from enumerating patterns) is a recorded detour: admissible for a
first freeze, but the ledger must flag that the generalization hypothesis is
unmet.

## Interpretation rule

As in the parent Contract: if any part admits more than one reading, STOP and
report it; do not resolve it yourself.
