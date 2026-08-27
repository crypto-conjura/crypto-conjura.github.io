id: 0023-strategist-1
agent: strategist
model: claude-fable-5
cycle: 1
status: COMPLETE

# Strategist plan set — c/0023, Polynomial Compatibility Conjecture (inverse-polynomial influence regime)

Inputs: CONTRACT.md; 0023-scout-1; cards S1 (ACC22), S2 (CLM23). No proof is
attempted here. Claims below tagged [STRAT-CLAIM] are strategist-level
observations with half-page proofs sketched; the assigned prover must verify
each before load-bearing use. Everything else is planning judgment.

## 0. Strategic picture and shared reformulations

**Why the campaign continues despite the 2026 bypasses:** CLM23's commitments
separation and ePrint 2023/1720's QPKE separation still consume PCC (Scout B5);
and PCC is now a clean open problem in Boolean-function analysis independent of
its original application.

**The wall pattern.** Every known incompatible construction (B.3
NegRow/PosCol; its ℤ_q analogue; row-indicator vs. column-cell-indicator
mixtures) bottoms out at per-coordinate average influence Θ(1/d): the
disjointness certificate is always a "crossing" (a row of a's must meet a
column of b's), and crossing geometry taxes influence at rate 1/degree.
Meanwhile the only proved compatibility mechanism (S1.b, §5.2) pays
|𝒴|^{deg f} for constant-block domination. The open window is
[|𝒴|^{-d}/d, 1/(2d)) over ℤ₂, and the six plans attack it from both ends plus
the meta-level.

Three reformulations all plans may share as vocabulary (each ≤ half page to
verify; R1–R2 need Contract convention 1, which is WLOG by R3):

* **R1 (occupancy density).** For finitely supported 𝐅 put
  μ_𝐅(x) := E_{f←𝐅}[|f(x)|²]. Then μ_𝐅 ≥ 0, E μ_𝐅 = 1, deg μ_𝐅 ≤ 2d, and
  ∪_{f∈supp 𝐅} supp(f) = supp(μ_𝐅). Hence **(𝐅,𝐆) incompatible ⟺
  μ_𝐅 · μ_𝐆 ≡ 0** (disjoint union-supports — the reformulation flagged in the
  task; adopted). [STRAT-CLAIM]
* **R2 (coefficient lightness).** For every χ ≠ 0 with live coordinate i,
  |μ̂_𝐅(χ)| ≤ 2·E_f[√(Inf_i(f))] ≤ 2√δ. (Split the convolution
  (f·conj f)^(χ) = Σ_{χ'} f̂(χ+χ')·conj(f̂(χ')) by which factor is live at i;
  Cauchy–Schwarz each half; Jensen.) So incompatible families are densities
  with **individually tiny** nonconstant Fourier coefficients — but their
  Fourier ℓ¹ mass is uncontrolled, and that is exactly where §5.2's
  exponential loss lives. [STRAT-CLAIM]
* **R3 (density-operator form; kills the distribution quantifier).** A
  distribution 𝐅 enters hypotheses and conclusion only through
  M_𝐅 := E_f[|f⟩⟨f|], a PSD unit-trace operator on
  V_d := span{χ : deg χ ≤ d}: E_f Inf_i(f) = Tr(M_𝐅 L_i) with L_i the
  projector onto {χ : χ_i ≠ 0̂}, and μ_𝐅 = the point-basis diagonal of M_𝐅.
  Conversely every PSD unit-trace M on V_d arises from a finitely supported
  distribution (its spectral ensemble) with the same Tr(M L_i) and the same
  diagonal. **PCC ⟺ for every pair M, M′ of PSD unit-trace operators on V_d
  with Tr(M L_i), Tr(M′ L_i) ≤ δ(d) for all i, the point-basis diagonals have
  intersecting supports.** Corollaries: supports of size ≤ dim V_d ≤
  (N|𝒴|)^d are WLOG (justifying Contract convention 1); the problem is a
  finite SDP-feasibility question for each (d, N); and this is precisely ACC22
  Conjecture 4.3's state form made finite-dimensional-explicit. [STRAT-CLAIM]

**Recurring obstruction to name once:** passing from f to |f|² (or conditioning
on a subcube / collapsing after a restriction) inflates influence bounds unless
one controls either ‖f‖_∞ (which the hypotheses do not give) or the collapsed
norm in the denominator. Plans P1, P2, P4, P5, P6 are engineered to hit this
wall in *different* places or to avoid it by different means; the independence
matrix in §3 records this.

## 1. BARRIER PRE-CHECK (Contract BARRIER CHECKLIST, applied)

* Relativization / natural proofs / algebrization: **not applicable** — PCC is
  an unconditional statement about finite function spaces; no plan below
  asserts a complexity-class separation. No plan's success would breach these.
* Black-box / meta-reduction barriers: live only downstream (CLM23's
  separations); no plan touches the application layer.
* **Operative internal gate — Claim B.3 (card S1.c):** over ℤ₂ there are
  singleton-support incompatible pairs at influence 1/(2d). Any plan whose
  success would certify compatibility at some δ(d) ≥ 1/(2d) over ℤ₂ is dead on
  arrival. Gate applied per plan: P1's joint collapse lemma is required to
  demonstrably fail on NegRow/PosCol at δ = 1/(2d) (built into its milestone);
  P2's OSSS route can only output thresholds δ = O(d^{-5})-ish (depth-O(d⁴)
  trees), safely below 1/(2d); P3 contains B.3 as a feasible point of its
  search space; P4 targets c/d² with B.3 as the ceiling witness; P5's
  barrier-witnesses must merely beat the coefficient scale √(2/d) that B.3
  already achieves; P6's target dichotomy bound must be ≤ 1/(2d), set at c/d².
* **N-dependence trap (Contract quantifier order):** any step that union-bounds
  over N coordinates or N-dependent character counts proves the wrong
  statement. Flagged inside P1, P2, P6 where the risk is live.

## 2. The six plans

### P1 — class (a) REDUCTION: restrict, collapse, bootstrap ACC22 Thm 4.4 at degree O(log d)

**Thesis.** PCC follows from ACC22 Theorem 4.4 applied after a random
restriction, because Thm 4.4's true cost is |𝒴|^{deg f*} for a *single*
selected f* (the S1-carded asymmetry: no influence bound on 𝐅, no degree bound
on 𝐆 is used), so it suffices that some restriction ρ leaves a surviving f*
of exact degree O(log_{|𝒴|} d) while the collapsed 𝐆-side average influences
on f*'s ≤ O(log d) live coordinates stay below |𝒴|^{-deg f*}/deg f* =
1/poly(d).

**Key step.** A *joint collapse lemma*: for every admissible (𝐅,𝐆) at
δ = 1/poly(d) there exists a restriction ρ (equivalently, a computational-basis
measurement of part of the oracle register) such that (i) some f ∈ supp(𝐅) has
f|_ρ ≢ 0 with exact degree ≤ C log d, and (ii) the collapsed, reweighted 𝐆|_ρ
(probabilities ∝ Pr[g]·‖g|_ρ‖², the state-collapse weighting of S2's
Definition 2.11) has Σ_{i ∈ live(χ*)} E[Inf_i] ≤ |𝒴|^{-C log d}/(C log d).
Everything turns on beating *collapse inflation*: the reweighting divides by
E‖g|_ρ‖², which adversarial 𝐆 can make small exactly where (i) holds. No step
may union-bound over N; survival rates must be p = p(d).

**Falsifiable milestone (≤2 pp).** Two halves, each one page: (M1a) prove or
refute the *single-function* collapse statement — for every unit f, deg ≤ d,
max_i Inf_i(f) ≤ δ, there is a ρ with f|_ρ ≢ 0 and deg(f|_ρ) ≤ k(d, δ) =
O(log d) (true by hand for NegRow and for spread block-character mixtures;
settle it in general or produce the counterexample). (M1b) exhibit, on the B.3
pair at δ = 1/(2d), the exact inequality where the *joint* lemma fails
(mandatory B.3 gate: if the joint lemma seems provable at 1/(2d), the plan is
wrong, stop). Outcome either validates the mechanism shape or pins the
inflation inequality quantitatively.

**Prior of full proof: 8%.** The bootstrap shape is genuinely new relative to
print (nothing in S1/S2 or the Scout's sweep restricts-then-reapplies 4.4),
and the asymmetry it exploits is real; but collapse inflation is precisely the
phenomenon that has kept the AA-kin open, and the adversary controls where
norms shrink.

**Yield on failure.** The inflation inequality, isolated and quantified — the
first formalized entry for the Contract's empty "Known barriers" section, and
the diagnosed obstruction the Weakener needs; plus (M1a) as a reusable
structural lemma either way.

### P2 — class (e) TRANSFER: 2026 win-win/decision-tree machinery + OSSS

**Thesis.** The only new low-degree machinery since 2022 — arXiv:2504.05710
Lemma 3.4 (win-win partial assignments forcing non-vanishing) and
arXiv:2608.03824 Lemma 3.5 (an O(d⁴)-query decision-tree procedure for
disjoint-support low-degree pairs) — converts an incompatible pair into a
shallow query algorithm, and the OSSS inequality [OSSS05; ACC22 p. 11 cites it
for the no-communication perfect-completeness case — MEMORY-tagged, prover
must card it] then forces some queried coordinate to carry influence
≥ Var/poly(d) > δ, a contradiction.

**Key step.** A *distributional* decision lemma: upgrade the per-function,
adaptively-chosen certificates of the 2026 lemmas to certificates measured
against the densities μ_𝐅, μ_𝐆 (or the operators M, M′), so that OSSS's
"influence of the computed function" is dominated by the families' average
influences. Adaptivity-per-function versus simultaneity-per-distribution is
exactly where this can die; also note the completely-bounded AA case
(arXiv:2203.00212) as a secondary import — state polynomials inherit quantum
provenance, and whether M_𝐅's spectral ensemble inherits complete boundedness
is unexplored in print (Scout C3).

**Falsifiable milestone (≤2 pp).** First pin the exact statement of 2608.03824
Lemma 3.5 (currently [RESTATED]; issue the source request — this is the plan's
gate). Then attempt the **singleton case**: for point masses on f, g with
fg ≡ 0, run Lemma 3.5's procedure against the pair and apply OSSS to the
induced tree; either this proves singleton-PCC at δ = 1/O(d⁵) (a major rung —
gate-check: threshold must land below 1/(2d), which it does by construction),
or the write-up isolates the precise type mismatch (e.g., the procedure
requires query access to a *given* x rather than computing a total Boolean
function under the uniform measure). ACC22's authors knew OSSS and did not
claim this, so expect the mismatch — but nobody has run it against the 2026
lemmas, which did not exist then.

**Prior of full proof: 4%** (singleton partial: ~15%). The distributional
upgrade fights the same simultaneity that makes PCC hard; but the import is
fresh and unexamined, and the singleton test is cheap once the source is
pinned.

**Yield on failure.** A precisely documented adaptivity barrier ("per-function
query certificates cannot aggregate over distributions because ...") — the
honest comparison between PCC and the 2026 line the literature currently
lacks; source cards for both 2026 lemmas; possibly the singleton rung.

### P3 — class (c) REFUTATION: density-operator SDP search below the 1/(2d) frontier

**Thesis.** PCC is false, and the witness exploits the slack B.3 does not use —
*average* influence over genuinely mixed distributions (rank ≥ 2 operators M),
searchable exactly at small (d, N) via R3: minimize max_i max(Tr(M L_i),
Tr(M′ L_i)) over PSD unit-trace M, M′ on V_d whose point-basis diagonals have
disjoint supports, then scale the discovered pattern combinatorially.

**Key step.** The R3 reformulation makes the inner problem, for each fixed
support split A ⊔ Aᶜ, an exact SDP (zero diagonal entries of a PSD matrix
force zero rows, so "diag supp ⊆ A" is linear); the outer loop over splits is
finite and symmetry-reducible. Everything turns on whether the optimum at
small d beats the singleton value 1/(2d) — i.e., whether mixing buys anything.
Two no-go facts to record en route [STRAT-CLAIM, one paragraph each]: padding/
tensoring an incompatible pair never lowers influence as a function of degree
(influence is norm-invariant under tensoring, degree only grows), and mixing
independent copies destroys disjointness (supports union); so any refutation
needs a genuinely new crossing structure — which is what the search hunts.

**Falsifiable milestone (≤2 pp incl. computation summary).** Over 𝒴 = ℤ₂,
d = 2: compute ε(2, N) = min-max average influence over incompatible pairs,
exhaustively over splits for N ≤ 5 (SDP dimension ≤ 16), heuristically
(orbit-reduced / local search over splits) for N ≤ 10. Falsifiable dichotomy:
either some pair beats the singleton frontier (ε(2,N) < 1/4 − c, refutation
momentum + an explicit mixed template to scale), or all optima match the
NegRow/PosCol pattern (tightness evidence: mixing buys nothing at d = 2, and
the extremal dual data feeds P5/P6).

**Prior of full disproof: 8%.** Reasoning: P(PCC false) ≈ 30% — the 1/d wall
pattern and the authors' stated belief point to truth, but the
average-influence slack is genuinely unexplored in print; P(this search finds
a scalable seed | false) ≈ 25–30%.

**Yield on failure.** Exact small-case extremals and their dual certificates —
the calibration data every proof plan needs (what does the tight pair look
like at d = 2?); elimination of the "mixing slack" refutation route; the
padding/tensoring no-go recorded.

### P4 — class (d) WEAKENING: the singleton nonnegative case, i.e. "|h| of low degree"

**Thesis.** The strongest special case plausibly provable now is the singleton
nonnegative case — 𝐅, 𝐆 point masses on f, g ≥ 0 with fg ≡ 0, which
*contains* the extremal B.3 pair (NegRow, PosCol ≥ 0) — via its equivalent
reformulation [STRAT-CLAIM, half page with careful normalization]: **if
h : 𝒴^N → ℝ is sign-indefinite, deg h ≤ d, and |h| also has degree ≤ d, then
max_i max(Inf-type of the two parts) ≥ c/d^C** (take f, g the positive and
negative parts (|h| ± h)/2; influences comparable up to constants).

**Key step.** The pair (h, |h|) both low-degree is a rigid algebraic condition
— the zero set separating the sign regions must be "flat" enough for the
absolute value not to raise degree — and the plan bets this rigidity forces a
1/poly(d)-influential coordinate. Declared per the Contract as a ladder rung
with its own contract (settles nothing about distributions); the bridge from
general singletons via (f², g²) is noted and explicitly BLOCKED by the L∞
obstruction (Inf_i(f²) ≤ 4‖f‖_∞² Inf_i(f) is the best generic bound).

**Falsifiable milestone (≤2 pp).** Classify, over ℤ₂, all sign-indefinite h
with deg h ≤ 2 and deg |h| ≤ 2 (a concrete algebraic exercise: |h| − h is
nonnegative, even-ish, degree ≤ 2), and compute the minimum of the max
influence over the class; falsified if some family drives it below c/d² -scale
already at d = 2, proved if the d ≤ 2 classification gives a constant bound
matching the B.3-extrapolated ceiling. Either outcome is exact and small.

**Prior: rung proved ~15%; full PCC via this plan ~2%** (the lift from
singletons to distributions is the conjecture's actual difficulty — S2's
Lemma 2.12 note explains why average influence is forced by state collapse).

**Yield on failure.** The |h|-reformulation itself (a clean, quotable
equivalent of singleton-nonneg PCC, new to print as far as the Scout found);
the d ≤ 2 classification; a sharpened sense of whether even singletons are out
of reach — which would re-rank every other plan.

### P5 — class (f) BARRIER: the density-relaxation fork

**Thesis.** Any proof that uses the hypotheses only through the occupancy
densities (R1) and their coefficient lightness (R2) — i.e., through
"μ, ν ≥ 0, degree ≤ 2d, mean 1, all nonconstant |μ̂|, |ν̂| ≤ 2√δ, disjoint
supports" — cannot prove PCC, because such pairs exist with coefficient scale
d^{-ω(1)}; equivalently, a proof must use the off-diagonal/PSD structure of R3
(the genuinely "quantum" information).

**Key step.** Construct two nonnegative degree-≤2d functions with disjoint
supports, means 1, and all nonconstant Fourier coefficients superpolynomially
small — the B.3 pair achieves scale √(2/d) (via R2 at δ = 1/(2d)), so the
question is whether coefficient scale, unlike influence, can be driven far
below poly. **The fork:** if such pairs exist, the barrier stands and the
campaign learns that R1/R2-only arguments (including any naive
uncertainty-principle or first-moment route — cf. S2.d's caution on
Donoho–Stark) are dead; if they provably do NOT exist below 1/poly(d)
coefficient scale, that nonexistence statement plus R2 IMPLIES PCC at
δ′ = (δ/4)² — the barrier attempt becomes a reduction of PCC to a clean,
distribution-free density statement. Note the relaxation is strict twice over
(coefficient-only influence data; nonneg ⊋ SOS-realizable diagonals), so the
barrier branch is the easier of the two to win.

**Falsifiable milestone (≤2 pp).** Beat B.3's coefficient scale by one
polynomial notch or show it cannot be done: construct disjoint nonneg
degree-≤2d mean-1 pairs with max nonconstant coefficient O(1/d) (quadratically
below √(2/d)) — candidate templates: design-spread sums of shifted AND²
blocks with second-order cancellation — or prove an Ω(d^{-1/2}) coefficient
lower bound for all disjoint pairs. Either outcome in two pages; both
reshape the plan space.

**Prior: barrier established ~25%; PCC proved via the reduction branch ~3%.**
Coefficient smallness is a much weaker constraint than influence smallness
(no per-coordinate accounting), so the barrier branch is favored — which is
exactly why this plan is cheap information.

**Yield on failure (neither branch closes).** Intermediate coefficient-scale
bounds pinning exactly where density-only information stops sufficing — a
quantitative refinement of the barrier file either way; a library of
disjoint-support density templates for P3.

### P6 — class (b) DIRECT CONSTRUCTION: explicit dual certificates for the set-dichotomy φ(A) ∨ φ(Aᶜ)

**Thesis.** Define φ_d(A) := min{max_i Tr(M L_i) : M PSD, unit trace, on V_d,
diag supp(M) ⊆ A}; then PCC ⟺ for every A ⊆ 𝒴^N,
max(φ_d(A), φ_d(Aᶜ)) > δ(d) [STRAT-CLAIM via R3, three lines], and the plan
constructs, for each A, an explicit dual/spectral certificate showing "either
A or Aᶜ costs ≥ c/d² in influence to occupy with a low-degree density" — an
isoperimetric-type dichotomy over sets, proved by exhibiting the certificate
directly rather than by contradiction.

**Key step.** SDP duality for φ_d(A) (Slater care needed at the constrained
boundary — prover work), then N-uniform certificate construction: the dual
object is a combination Σ λ_i L_i plus a point-supported penalty on Aᶜ, and
everything turns on building it with weights depending only on d and the
geometry of A near its boundary, never on N. This uses exactly what P5's
relaxation drops (PSD/off-diagonal structure), so P5's barrier, if it stands,
does not touch P6.

**Falsifiable milestone (≤2 pp).** Derive the dual characterization of φ_d(A)
rigorously, then certify the B.3 set: for A = "some row all −1" on the d×d
cube, prove φ_d(A) ≥ c/d by an explicit dual certificate (the primal NegRow
gives φ_d(A) ≤ 1/(2d), so the target is a matching lower bound — first ever
influence *lower* bound for an occupancy problem in this literature; refuted
if the dual value provably degenerates, i.e., the SDP has an N-dependent
duality gap).

**Prior of full proof: 5%.** The reformulation is clean and the B.3
certificate looks reachable, but "for every A, N-uniformly" is a wide-open
quantifier, and spectrahedral-shadow lower bounds are notoriously hard.

**Yield on failure.** The φ(A) dichotomy reformulation and the first dual
certificate (for the B.3 sets) — a lower-bound tool absent from print, useful
to P3 (dual data guides the search) and to any successor campaign; a precise
record of whether the duality gap is N-dependent.

## 3. Mutual-independence matrix (why no two fail for the same reason)

| Plan | Dies iff |
|---|---|
| P1 | conditioning/collapse inflates 𝐆-side influence at 1/poly scale (measurement back-action) |
| P2 | per-function adaptive certificates cannot be made distributional (simultaneity/adaptivity mismatch) |
| P3 | PCC is true / mixing slack buys nothing at reachable (d,N) — "failure" is itself evidence, orthogonal to all proof plans |
| P4 | the algebraic rigidity of (h, |h|) both low-degree is insufficient or intractable at general d — a singleton/structural failure independent of distributional effects |
| P5 | intermediate coefficient scales resist both construction and impossibility — a relaxation-strength question, not a proof-mechanism question |
| P6 | N-dependent SDP duality gap / no N-uniform dual certificates — an SOS-expressiveness failure that P5's relaxation cannot cause (P6 uses exactly the structure P5 drops) and P1's inflation cannot cause (no conditioning anywhere in P6) |

P1 vs P2: both would prove PCC, but P1 never builds a query algorithm and P2
never restricts/collapses; their key inequalities live on different objects.
P3 vs P4 share small-d computation substrate but opposite failure semantics.
P4's L∞ block is distinct from P1's collapse inflation (no conditioning in P4).

## 4. Ranking by information-gained / effort, and wave order

1. **P3** — lowest effort (small exact SDPs), highest calibration value: its
   outcome re-weights the truth prior for every other plan and supplies the
   extremal patterns P5/P6 consume. Run first.
2. **P5** — cheap milestone, fork-shaped: either output (barrier or
   reduction-to-density) restructures the campaign; also formally discharges
   R1/R2 for everyone.
3. **P4** — small exact algebra; creates the first ladder rung and a quotable
   reformulation; feeds P3's search space.
4. **P1** — the most plausible full-proof mechanism; milestone is two
   one-page halves (M1a, M1b) and its failure output (the inflation
   inequality) is the diagnosed obstruction the harness wants on file.
5. **P2** — gated on one source upload (2608.03824 Lemma 3.5 exact statement);
   after the gate, the singleton test is cheap and high-information, but the
   gate puts it behind P1.
6. **P6** — heaviest machinery and longest runway; run after P3/P5 deliver
   extremal/dual data. Its milestone is still self-contained if run early.

Suggested wave: Provers on P3, P5, P4 (cheap, decorrelated, all ≤2pp
milestones) in cycle 2; P1 and the P2 source gate in cycle 3; P6 when P3's
dual data lands. Refuter sweep 0023-refuter-1 runs independently; P3's SDP
search is complementary (operator-level, exact), not duplicative.

### SOURCE REQUEST ###
Rank 1: Li–Li–Li–Liu, arXiv:2608.03824; exact statement + proof of Lemma 3.5
(decision-tree procedure for disjoint-support low-degree polynomials), pages
covering §3; P2's milestone collapses without it; rungs tried by Scout: arXiv
abs + html extraction ([RESTATED]); fallback: run P2 on the extraction,
flagged, with everything downstream conditional.
Rank 2 (below the bar, only if cheap): arXiv:2504.05710v2 Lemma 3.4 exact
statement, same rationale, same fallback.

### END OF ARTIFACT 0023-strategist-1 ###
