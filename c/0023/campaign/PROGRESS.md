# PROGRESS — c/0023

Campaign c/0023 — Polynomial Compatibility Conjecture (PCC), inverse-polynomial influence regime; depth 0; Contract: `c/0023/campaign/CONTRACT.md`; harness: `prompts/solve.md`.
Status 2026-08-27: Scout complete (`proofs/0023-scout-1.md`, verdict NO PRIOR RESOLUTION FOUND); source cards S1 (ACC22), S2 (CLM23) in `sources/`; Case ladder below AWAITING HUMAN APPROVAL — no rung materialised, no proving started. What remains to be discharged: everything (no rung attempted).

---

## Case ladder (Case Planner, 2026-08-27, harness §3.2.1)

### Conventions binding every rung

* **Group fixing.** Rungs R1–R5 and the operative route of R6 fix $\mathcal{Y}=\mathbb{Z}_2$ (domain $\{\pm 1\}^N$, Fourier/degree/influence as in the Contract). The conjecture quantifies the group existentially, so a $\mathbb{Z}_2$ proof of the top settles it; the launcher's ruling permits $\mathbb{Z}_2$-fixed rungs. Each $\mathbb{Z}_2$ rung is a genuine special case of the $\mathbb{Z}_2$-instantiated conjecture, the intended route. Contingency: if any rung is **refuted for every inverse-polynomial $\delta$ over $\mathbb{Z}_2$**, that kills $\mathbb{Z}_2$-PCC but **not** the conjecture (the printed $1/(2d)$ ceiling is $\mathbb{Z}_2$-only — card S1, Scout B2/C5); the ladder then re-bases on another group, R1–R3 porting verbatim.
* **Value range.** All rungs are $\mathbb{R}$-valued (R1–R3 are nonnegative-valued by construction). $\mathbb{R}\to\mathbb{C}$ is free at top-rung assembly: ACC22 Thm 5.6 / App. A, factor 2 in $\delta$, absorbed by $1/\mathrm{poly}$ (card S1).
* **Threshold schema $\Delta$.** "Inverse-polynomial form" means: *there exist $c_1\in(0,1]$, $c_2>0$ and $\delta:\mathbb{N}\to(0,1]$ with $\delta(d)\ge c_1 d^{-c_2}$ for all $d\ge 1$*, quantified before $d,N,\mathbf{F},\mathbf{G}$. Distributions are finitely supported (Contract convention 1); the influence hypothesis is per-coordinate on average (convention 2); the conclusion is exact non-vanishing at one common point (convention 4).
* **$\mathbb{Z}_2$ ceiling (B.3 consistency, checked per rung).** Every rung class below contains the $d\times d$ row/column grid mechanism at per-coordinate average influence exactly $1/(2d)$ (as distributions for R1–R3, as the printed singleton NegRow/PosCol for R3/R5/R6 — card S1, Claim B.3). Hence every $\mathbb{Z}_2$ rung's witnessing constants must, and can, sit below the $1/(2d)$ line: e.g. $c_1\le 1/4$, $c_2=1$. No rung below claims a threshold at or above $1/(2d)$, so none contradicts B.3.
* **K1 nontriviality filter (checked per rung).** ACC22 Thm 4.4 (card S1) settles every threshold $\delta<|\mathcal{Y}|^{-d}/d$, for all groups, all $d,N$, full generality. Every rung's threshold exceeds $2^{-d}/d$ asymptotically; fixed-$d$ slices of every rung are settled by K1 (see below) — each rung's content is **$d$-uniformity at a super-exponential threshold**.

### Axes skipped as settled, immediate, or vacuous (with reasons)

1. **Fixed small degree ($d=1$, then $d=2$, any fixed $d$) — SETTLED by K1, skipped.** At fixed $d$, K1's threshold $|\mathcal{Y}|^{-d}/d$ is a *constant independent of $N$*, and a fixed-$d$ rung asks exactly for some positive constant threshold. So ACC22 Thm 4.4 settles the entire fixed-$d$ axis. (At $d=1$ over $\mathbb{Z}_2$ the slice is closed *exactly*: K1 gives $\delta<1/2$, and $f=(1-x_1)/\sqrt2$, $g=(1+x_1)/\sqrt2$ — unit norm, degree 1, influences $1/2$, $fg\equiv 0$ — shows $1/2$ is sharp. Planner check, trivial.)
2. **Thresholds $\le |\mathcal{Y}|^{-d}/d$ (incl. "singleton at exponentially small influence") — SETTLED by K1, skipped.**
3. **$\pm 1$-valued functions — VACUOUS, skipped.** A $\{\pm1\}$-valued function never vanishes; the conclusion holds at every $x$. ("Boolean-valued" can only mean $\{0,1\}$-valued, i.e. normalized indicators = R2.)
4. **Subcube (conjunction) indicator distributions — IMMEDIATE, skipped; recorded as Rung 0 calibration below.** Union bound settles it at the exactly optimal $\delta(d)<1/(2d)$.
5. **$\mathbb{R}$-vs-$\mathbb{C}$ as a rung axis — SETTLED equivalent, skipped.** Card S1 (ACC22 Thm 5.6 / App. A): equivalent up to factor 2 in $\delta$.
6. **Bounded ($\mathrm{poly}(d)$) support size as a rung above singleton — skipped as a rung; a free rider on R5.** One-paragraph reduction: drop support elements of probability $<1/(2S)$ (remaining mass $\ge 1/2$); survivors have pointwise influences $\le 2S\delta$; apply the singleton rung at threshold $2S(d)\delta(d)$, still inverse-polynomial for $S(d)=\mathrm{poly}(d)$. Record as a corollary when R5 freezes. The support-size axis's genuine content is *unbounded* support = R6.

### Rung 0 (calibration — NOT a rung; planner-level sketch, unverified, not citable until written up and verified)

Class: distributions over normalized subcube indicators $\mathbf{1}_A/\|\mathbf{1}_A\|_2$, $A$ a subcube fixing $\le d$ coordinates. For a fixed coordinate of a conjunction the relative influence is $1/2$ (card S1), so the hypothesis $\mathbb{E}_{\mathbf{F}}[\mathrm{Inf}_i]\le\delta$ reads $\Pr_{A\sim\mathbf{F}}[i \text{ fixed}]\le 2\delta$. Two subcubes are disjoint iff some coordinate is fixed by both with opposite signs. If every $A\in\mathrm{supp}\,\mathbf{F}$ conflicts with a fixed $B\in\mathrm{supp}\,\mathbf{G}$, then $1\le\sum_{i\in\mathrm{fix}(B)}\Pr_{\mathbf{F}}[i\in\mathrm{fix}(A)]\le 2\delta d$. So $\delta(d)<1/(2d)$ forces compatibility — and the row/column grid distributions ($\mathbf{F}$ uniform over the $d$ row-subcubes, $\mathbf{G}$ over the $d$ column-subcubes, $\mathbb{E}[\mathrm{Inf}_i]=1/(2d)$ exactly; re-verified, unreported, by in-repo Refuter code `proofs/0023-refuter-1-code/grid_construction.py`) show $1/(2d)$ is optimal for this class. **Calibration lessons:** (i) B.3's constant is the exact truth for conjunctions; (ii) the union-bound/per-coordinate-budget mechanism — the same accounting inside K1's proof — is optimal on conjunctions and, as R1 shows, collapses to exponential thresholds the moment patterns are richer. Rungs must beat that mechanism.

---

### The ladder

All rungs quantify over **all $d,N\in\mathbb{N}$** and all finitely supported $\mathbf{F},\mathbf{G}$ over the stated class satisfying the Contract's three hypotheses at $\delta(d)$; conclusion always: $\exists f\in\mathrm{supp}\,\mathbf{F},\ g\in\mathrm{supp}\,\mathbf{G},\ x$ with $f(x)\,g(x)\ne 0$.

---

**R1 — Spread-junta indicator rung ($\mathbb{Z}_2$, windows of size $\le d$).**

*Statement.* There exist $c_1\in(0,1]$, $c_2>0$, $\delta(d)\ge c_1 d^{-c_2}$ such that for all $d,N$ and all finitely supported $\mathbf{F},\mathbf{G}$ over
$$\mathcal{C}^{\mathrm{junta}}_d:=\Bigl\{\tfrac{\mathbf{1}_A}{\|\mathbf{1}_A\|_2}\ :\ A=\{x\in\{\pm1\}^N: x_J\in P\},\ J\subseteq[N],\ |J|\le d,\ \emptyset\ne P\subseteq\{\pm1\}^J\Bigr\}$$
with $\mathbb{E}_{f\sim\mathbf{F}}[\mathrm{Inf}_i(f)]\le\delta(d)$ and $\mathbb{E}_{g\sim\mathbf{G}}[\mathrm{Inf}_i(g)]\le\delta(d)$ for every $i\in[N]$, some $f\in\mathrm{supp}\,\mathbf{F}$, $g\in\mathrm{supp}\,\mathbf{G}$, $x$ have $f(x)g(x)\ne0$. (Unit norm and $\deg\le d$ are automatic for the class. Equivalent combinatorial form: two cross-disjoint families of $\le d$-window cylinder patterns, with each side's per-coordinate influence mass spread below $\delta(d)$, cannot exist — for indicators the conclusion is exactly $A\cap B\ne\emptyset$ for some pair, i.e. projections to shared windows intersect for some pair.)

*What it adds over Rung 0.* Arbitrary patterns on the windows, not conjunctions: disjointness loses its single-coordinate witness, and a *relevant* window coordinate may carry relative influence as small as $2^{-\Theta(d)}$, so the union bound recovers only exponential thresholds. This is the exp-vs-poly gap — the conjecture's characteristic difficulty — in its minimal, purely finite-combinatorial form, with the distributional-spreading mechanism (Contract crux: $\delta$ independent of $N$) fully present.

*Scout status.* Open. K1 covers only $\delta<2^{-d}/d$; B.3-consistent (class contains the grid distributions, so any witnessing $\delta$ needs $\delta(d)<1/(2d)$, i.e. effectively $c_2\ge1$ — allowed); nonvacuous (spread grid-type families satisfy the hypotheses nontrivially). The Scout did not search this as a standalone combinatorial object (cross-disjoint spread window-pattern families); a targeted micro-scout at rung start is cheap insurance. Refuter-first per §3.2.1: bounded search over small $d$/windows/patterns before proving — this rung is also the deliberate falsification honeypot for $\mathbb{Z}_2$-PCC (see Conventions, contingency).

*Generalization hypothesis.* The union-bound **replacement** — a weighted counting/entropy argument proving "cross-disjointness of spread bounded-window pattern families forces some coordinate to carry $\ge 1/\mathrm{poly}(d)$ average influence" — is the combinatorial engine expected to survive to R2/R3 (windows become effective windows / level sets) and into the top rung's treatment of state-polynomial supports. If the proof instead exploits exact pattern finiteness (constants like $2^{2^d}$ over pattern enumeration), it is a detour: the ladder demands the influence-driven version.

---

**R2 — Degree-$d$ set rung ($\mathbb{Z}_2$, general Boolean-valued).**

*Statement.* Schema $\Delta$ for all finitely supported $\mathbf{F},\mathbf{G}$ over
$$\mathcal{C}^{\mathrm{ind}}_d:=\bigl\{\mathbf{1}_A/\|\mathbf{1}_A\|_2\ :\ \emptyset\ne A\subseteq\{\pm1\}^N,\ \deg(\mathbf{1}_A)\le d\bigr\}.$$

*What it adds over R1.* Strictly contains R1 ($|J|\le d\Rightarrow\deg\le d$; degree-$d$ sets need not be $d$-juntas). Windows blow up from $d$ to $\exp(d)$ (degree-$d$ Boolean functions are $\exp(d)$-juntas — Nisan–Szegedy-type theorem; **[MEMORY], must be carded before any rung proof cites it**), so *degree*, not window size, becomes the honest complexity parameter; first rung where Fourier-structural facts about degree-$d$ Boolean functions (junta bounds, granularity of coefficients — also to be carded) must do real work.

*Scout status.* Open; not settled by S1/S2 (K1 exponential only); B.3-consistent as in R1 (class $\supseteq$ grid distributions, so $\delta(d)<1/(2d)$ forced; fine).

*Generalization hypothesis.* The mechanism converting "$\deg\le d$" into effective-window/spread structure with only $\mathrm{poly}(d)$ losses should survive to R3, where level sets of nonnegative degree-$d$ functions replace sets. A proof leaning on exact $\{0,1\}$-valuedness beyond granularity-type facts dies at R3 — detour.

---

**R3 — One-sided (nonnegative) rung ($\mathbb{Z}_2$).**

*Statement.* Schema $\Delta$ for all finitely supported $\mathbf{F},\mathbf{G}$ over
$$\mathcal{C}^{+}_d:=\bigl\{f:\{\pm1\}^N\to\mathbb{R}_{\ge0}\ :\ \|f\|_2=1,\ \deg f\le d\bigr\}.$$

*What it adds over R2.* Strictly contains R2 (indicators are nonnegative; NegRow $\in\mathcal{C}^+_d\setminus\mathcal{C}^{\mathrm{ind}}_d$). Values beyond $\{0,\mathrm{const}\}$: mass can spike; non-vanishing sets are no longer degree-structured (the support-indicator of NegRow has degree $\approx d^2$, not $d$). First rung whose class contains the full printed extremal landscape (B.3's NegRow/PosCol as singletons, and their distributional spreadings). Flattening ($f\mapsto\mathbb{E}_{\mathbf{F}}[f]$, which preserves the union of supports for nonnegative $f$) is available but degrades beyond $\mathrm{poly}$ support sizes — the unbounded-support spreading difficulty appears here in its pure one-sided form.

*Scout status.* Open. K1's proof shape (card S1.b: uses only one degree-$d$ $f$ plus the average influence bound on $\mathbf{G}$) yields only the exponential regime here; B.3-consistent ($c_2\ge1$ forced, allowed); nonvacuous.

*Generalization hypothesis.* The unbounded-support spreading argument, with nonnegativity used **only** to identify "all pairs vanish jointly" with a mass-covering statement about supports, should survive as the distributional half of R6's proof, with R4/R5 supplying the replacement for that single nonnegative step (cancellation control). If the proof needs quantitative pointwise positivity (min-value lower bounds), it is likely a detour.

---

**=== EXPECTED DIFFICULTY JUMP A (combinatorial → analytic: signs and cancellation enter; refuter-style search stops being decisive) ===**

---

**R4 — Sub-polynomial threshold rung (full $\mathbb{Z}_2$ class, signed).**

*Statement.* There exist $\alpha\in(0,1)$ and $c>0$ such that for all $d,N$ and all finitely supported $\mathbf{F},\mathbf{G}$ over $\{f:\{\pm1\}^N\to\mathbb{R},\ \|f\|_2=1,\ \deg f\le d\}$ with $\mathbb{E}_{f\sim\mathbf{F}}[\mathrm{Inf}_i(f)]\le c\,e^{-d^{\alpha}}$ and $\mathbb{E}_{g\sim\mathbf{G}}[\mathrm{Inf}_i(g)]\le c\,e^{-d^{\alpha}}$ for all $i$, the conclusion holds.

*Implied by the conjecture:* from a $\mathbb{Z}_2$ witness $\delta(d)\ge c_1d^{-c_2}$, take any $\alpha$ and $c:=\min\bigl(1,\min_{d\le d_0} c_1 d^{-c_2}e^{d^\alpha}\bigr)>0$ where $d_0$ is the finite crossover; then $c\,e^{-d^\alpha}\le\delta(d)$ for all $d$, and lowering the influence ceiling shrinks the hypothesis class.

*What it adds over R3.* Signs/cancellation and full distributional generality at once — but with exponential quantitative room. The named target is exactly Scout C1's obstruction: beat the $|\mathcal{Y}|^d$ Cauchy–Schwarz-across-blocks loss in K1's proof (card S1.b) by **any** exponent improvement ($2^{-d}\to e^{-d^\alpha}$, $\alpha<1$). This is the Contract's first named-partial tier. Ordering note: **not comparable to R1–R3 by containment** (class larger, threshold smaller); placed here because the sub-polynomial room makes it the natural first fight with cancellation, before the frontier threshold.

*Scout status.* Open — precisely the Contract's named partial "$\exp(-d^{\alpha})$, $\alpha<1$". Not settled by K1 ($e^{-d^\alpha}\gg 2^{-d}/d$ for large $d$). B.3-consistent: need $c\,e^{-d^\alpha}<1/(2d)$ for all $d$; $\min_d e^{d^\alpha}/(2d)>0$, so the existential $c$ absorbs it (at $\alpha=1/2$ the binding case is $d=4$: $e^{2}/8\approx0.92$, so $c\le0.9$ suffices).

*Generalization hypothesis.* The accounting that replaces Cauchy–Schwarz across all $|\mathcal{Y}|^d-1$ nonconstant blocks (e.g. level-by-level character grouping with per-level $\mathrm{poly}(d)$ losses) is the quantitative skeleton R6 must tighten to inverse-polynomial by feeding in R1–R3's spreading combinatorics. Even failure survives usefully **if** it produces a cap-diagnosis ("this restructuring stalls at $e^{-d^{\alpha}}$ because …") — that diagnosis is then the precise statement of what R6 must overcome. Natural sub-stages if it resists: R4 $\cap$ singleton, R4 $\cap$ nonnegative.

---

**R5 — Singleton rung at inverse-polynomial threshold ($\mathbb{Z}_2$, signed).**

*Statement.* There exist $c_1\in(0,1]$, $c_2>0$, $\delta(d)\ge c_1d^{-c_2}$ such that for all $d,N$ and all $f,g:\{\pm1\}^N\to\mathbb{R}$ with $\|f\|_2=\|g\|_2=1$, $\deg f,\deg g\le d$, $\max_i\mathrm{Inf}_i(f)\le\delta(d)$, $\max_i\mathrm{Inf}_i(g)\le\delta(d)$, there is $x$ with $f(x)g(x)\ne0$. (Point-mass $\mathbf{F},\mathbf{G}$; equivalently the max-influence variant for arbitrary supports, since a pointwise hypothesis holds pair by pair.)

*What it adds over R4.* The threshold jumps from sub-polynomial to the inverse-polynomial frontier: the class contains NegRow/PosCol (B.3) at $1/(2d)$, so the proof must operate in the tight regime and "see" why $1/(2d)$ is the truth's neighborhood — genuinely tight-regime analytic structure theory (zero sets of low-degree, low-influence, unit-norm polynomials cannot complementarily cover the cube). This is the AA-adjacent analytic heart. Ordering note: contains the singleton slices of R3 and of R4 (each implied by R5 — for R4's slice, at its lower threshold); **not** comparable to R3/R4 wholesale (no spreading); ordered above R4 on expected difficulty (frontier threshold beats sub-poly room).

*Scout status.* Open — the Contract's named partial "singleton supports". B.3 applies verbatim: $c_2\ge1$ forced over $\mathbb{Z}_2$; consistent, nonvacuous (NegRow at $n=m=d$ has all relative influences $\le 1/(2d)$ and vanishes somewhere). AA kinship (Scout B4/C3): the analogous inverse-polynomial regime of Aaronson–Ambainis is open since 2009 except for completely bounded (block-)multilinear forms [RESTATED: arXiv:2203.00212, 2304.06713] and a for-some random-restriction variant [RESTATED: arXiv:2402.13952]; ACC22 p. 11 prints that PCC and AA are not directly comparable, so none of that settles R5 — but the completely-bounded transfer surface (state polynomials have quantum provenance) is the freshest import to try here. In-repo Refuter tooling (`dd_z2_exhaustive.py`: exact singleton frontier $\varepsilon^*(d,N)$ over cube partitions, unreported) is the rung's ready-made sanity check.

*Generalization hypothesis.* The per-function structure theorem ("unit norm, $\deg\le d$, all influences $\le1/\mathrm{poly}(d)$ $\Rightarrow$ quantitative anti-covering of the zero set") is the engine R6 applies inside an average. Prefer proofs in K1's **asymmetric shape** — one $f$ fixed, the other side averaged (card S1.b proves that shape viable) — since those survive averaging on one side by construction. A proof requiring both functions fixed and symmetric is half a detour.

---

**=== EXPECTED DIFFICULTY JUMP B (the full quantitative core: inverse-polynomial threshold × unbounded-support averaging × cancellation, simultaneously; run the full Strategist wave here per harness §4) ===**

---

**R6 (TOP) — the full conjecture.**

*Statement (verbatim Contract, `conj:main`):*
```latex
There exist a finite abelian group $\cY$, constants $c_1\in(0,1]$ and
$c_2>0$, and a function $\delta\colon\NN\to(0,1]$ satisfying
$\delta(d)\ge c_1\,d^{-c_2}$ for all $d\ge 1$ --- equivalently,
$\delta(d)\ge 1/p(d)$ for some polynomial $p$ --- such that for every
$d\in\NN$ and every $N\in\NN$ the following holds.

Let $\bF$ and $\bG$ be any two probability distributions over functions
$\cY^N\to\CC$ such that: unit $\ell_2$ norm on the support; degree at
most $d$ on the support; and for every $i\in[N]$,
$\E_{f\sample\bF}[\operatorname{Inf}_i(f)]\le\delta(d)$ and
$\E_{g\sample\bG}[\operatorname{Inf}_i(g)]\le\delta(d)$.
Then there exist $f\in\operatorname{supp}(\bF)$,
$g\in\operatorname{supp}(\bG)$, and $x\in\cY^N$ such that
$f(x)\cdot g(x)\ne 0$.
```
(Macros are the Contract's; hypotheses abbreviated from its itemized list, unchanged in content — the Contract file remains the authoritative statement.)

*Declared route.* Prove the operative target **R6′**: the $\mathbb{Z}_2$, $\mathbb{R}$-valued, arbitrary-finite-support instantiation at inverse-polynomial $\delta$ — which strictly contains R1–R3 and R5, and implies R4. Then conclude R6 by existential group instantiation plus the carded $\mathbb{R}\to\mathbb{C}$ equivalence (card S1: ACC22 Thm 5.6 / App. A, factor 2 in $\delta$, absorbed). Fallback: if $\mathbb{Z}_2$ is refuted at all inverse-polynomial thresholds along the way, re-base R1–R5 on another finite abelian group (unexplored in print; only the $\mathbb{Z}_2$ ceiling is published).

*What it adds over R5.* The unbounded-support average-influence hypothesis on **both** sides simultaneously, with signs: support elements may individually violate any pointwise influence bound (grid mechanism), and the flattening and mass-restriction crutches of R3/R5 provably degrade at exponential support sizes. This is exactly the form CLM23 consumes (card S2: the average form is forced by state-polynomial distributions; max-over-support is Contract-forbidden as a substitute).

*Scout status.* Open — Scout verdict NO PRIOR RESOLUTION FOUND (2022 through 2026-08-27); the three 2026 bypass papers remove downstream load without proving any regime (Scout B5); CLM23 and ePrint 2023/1720 still consume it.

*Generalization hypothesis.* None required (top rung).

---

### Ordering rationale, containment lattice, reorder options

Containments: R0 $\subset$ R1 $\subset$ R2 $\subset$ R3 $\subset$ R6′; R5 $\subset$ R6′; R4 $\subset$ (implied by) R6′; R5 $\supset$ singleton slices of R3 and R4; R4 vs R1–R3 and R5 vs R3/R4 are **incomparable as statements** — their relative order is the planner's difficulty judgment (cancellation with exponential room before cancellation at the frontier; spreading before either). Defensible reorderings for the human: (a) swap R4 and R5 (attack the analytic heart before threshold-climbing); (b) promote R4 to immediately after Rung 0 if one believes threshold-improvement is purely technique-limited, keeping R1–R3 as fallbacks; (c) drop R2 if R1's proof visibly scales in the window size (R2 then becomes a rider on R3).

Sanctioned insertion points if a rung resists (Weakener fodder, pre-authorized shapes): below R1 — uniform-probability or density-$2^{-\Theta(d)}$-pattern variants; below R4/R5 — nonnegative singleton at inverse-poly; between R4 and R6 — full class at $\exp(-\mathrm{polylog}\,d)$ (the Contract's second named-partial tier); below R6 — poly-size-support signed distributional (beyond the free rider only if the R5 reduction's loss must be avoided).

### Barrier pre-check (Contract, BARRIER CHECKLIST)

The Contract's checklist ticks **nothing**: relativization/algebrization/natural proofs are not applicable to this unconditional Fourier-analytic statement, and black-box/meta-reduction barriers live only in the downstream applications. No rung's intended technique class, if it succeeded, would breach any ticked barrier — the pre-check passes vacuously and is recorded here. One internal caution: the Contract names a *candidate* internal barrier ("arguments using only per-coordinate influence budgets cannot beat exponential thresholds") as a possible future BARRIER-plan target, not an established fact. Rung 0's calibration is evidence *for* that candidate on conjunctions; R1–R3's generalization hypotheses are phrased so that their proofs, if found, either refute that candidate or visibly use more than per-coordinate budgets. No conflict today; if a BARRIER plan later establishes it, re-examine R1–R3's surviving-feature claims and hand R4+ the diagnosis.

### Gate

**APPROVED by the human, 2026-08-27, as ordered** (no reorder). R1 is
materialised as `intermediates/I01-spread-junta.md` — the single active
target. In flight: Refuter-first computational sanity check on I01 (bounded
search over small $d$, windows, patterns; artifact `0023-refuter-2`) plus the
rung-start micro-scout flagged in R1's Scout status (artifact
`0023-scout-2`); one Prover follows only if the Refuter finds no
counterexample.
