---
id: 0023-refuter-1
agent: refuter
model: claude-fable-5
cycle: 1
status: COMPLETE
---

# Refuter report, cycle 1 — PCC (c/0023), inverse-polynomial influence regime

## VERDICT

**NEAR-MISS (obstruction characterised) / NO COUNTEREXAMPLE IN REGIME
[searched: exact-exhaustive ℤ₂ at (d,N) ∈ {1}×{1..4} ∪ {(2,3),(2,4),(3,4)};
exact-exhaustive ℤ₃ at (d,N) ∈ {(1,1),(1,2)}; structured block/design
families up to d = 8; stochastic partition search at (2,5),(2,6),(3,6)].**

No counterexample to the Conjecture was found, and none can be exhibited at
finite (d, N): a refutation is an asymptotic statement (for every group and
every inverse-polynomial δ, a violation at some d). What the search DID
produce, exactly certified:

1. **The presumed refutation frontier K2 (δ ≥ 1/(2d)) is not tight.** An
   explicit incompatible pair at d = 2, N = 4 has all per-coordinate
   influences ≤ **1/5 < 1/4 = 1/(2d)** (exact rational certificate, two
   independent methods). A two-parameter family extends this to
   **ε(d) ≤ (4/11)·d⁻¹ + o(1/d)** (certified seed: d = 4, influence 1/11).
   Consequently any conjecture-witnessing δ must satisfy **c₂ ≥ 1**
   (for every finite abelian group), and over ℤ₂ effectively
   δ(4D) < 1/(11D).
2. **A precise obstruction blocks every architecture searched from going
   below Θ(1/d)** (§5). This obstruction — conflicts between the two
   supports must be "paid for" locally, coordinate-block by
   coordinate-block, while the degree budget is spent linearly — is the
   candidate heart of a proof of the conjecture at δ(d) = c/d.
3. At d = 1 the conjecture's quantity is **exactly 1/2 for every N**
   (theorem, plus exhaustive verification): no decay in N whatsoever at
   the bottom rung.

Net assessment: the evidence gathered points **against falsity** in every
regime this search could reach; all constructions saturate at Θ(1/d) with
slowly improving constants (1/2 → 2/5 → 4/11), exactly the profile one
expects if ε*(d) = Θ(1/d) and the conjecture is TRUE with c₂ = 1.

Reproducible code: `proofs/0023-refuter-1-code/` (Python 3, numpy/scipy
for float SDPs, `fractions.Fraction` for every certificate; each script's
docstring states what it proves and how).

---

## 1. Reductions used (each elementary; proofs here, one paragraph)

**(R1) Support criterion.** (𝐅,𝐆) is incompatible iff
U_F := ⋃_{f∈supp 𝐅} {x : f(x)≠0} and U_G := ⋃_{g∈supp 𝐆} {x : g(x)≠0}
are disjoint. Immediate: f(x)g(x) ≠ 0 for some f,g,x iff some x lies in
some supp(f) ∩ supp(g) iff U_F ∩ U_G ≠ ∅.

**(R2) Partition WLOG.** For a support set A let V_A = {h : deg h ≤ d,
h ≡ 0 outside A} (a linear subspace) and
τ(A) = min over distributions on unit vectors of V_A of
max_i E[Inf_i]. Enlarging A enlarges V_A, so τ is nonincreasing in A;
for disjoint (A,B), (B^c, B) is a partition with value
max(τ(B^c),τ(B)) ≤ max(τ(A),τ(B)). Hence
**ε*(d,N) := min over incompatible pairs of max per-coordinate average
influence = min over partitions (A,A^c), both sides admitting a nonzero
function, of max(τ(A), τ(A^c))**. The two sides decouple.

**(R3) Density-matrix SDP + minimax dual.** A distribution over unit
vectors of V_A is exactly a density matrix ρ (PSD, tr = 1, range ⊆ V_A in
Fourier coordinates), and E Inf_i = tr(P_i ρ) with P_i the diagonal
projector onto characters active at i (mixtures ↔ spectral
decompositions). By von Neumann minimax,
τ(A) = max_{w∈Δ_N} λ_min(Π_V (Σ_i w_i P_i) Π_V). Every explicit rational w
gives a certified lower bound (an exact PSD check of
B_rᵀ(D_w − q·I)B_r over a rational nullspace basis B_r); every explicit
mixture gives a certified upper bound. For 𝒴 = ℤ₂ real coefficients are
WLOG (the defining equations are real and Re ρ of a complex optimum is
feasible with the same objective).

Monotonicity in both parameters: ε*(d+1,N) ≤ ε*(d,N) (bigger space) and
ε*(d,N+1) ≤ ε*(d,N) (pad with an unused coordinate; supports become
cylinders, still disjoint; influences unchanged).

## 2. Target 1: d = 1 exactly

**Theorem R-1 (ε*(1,N;ℤ₂) = 1/2 for every N).** Proof: (i) a nonzero
degree-≤1 f = a₀ + Σaᵢxᵢ (complex coefficients) vanishes on at most half
of {±1}^N — fix i with aᵢ ≠ 0; for each setting of the other coordinates
at most one value of xᵢ zeroes f. (ii) Classification of equality: writing
k = #{i : aᵢ ≠ 0}, exactly-half zero sets occur only for k ≤ 2, forms
c(1 ± xᵢ) and c(xᵢ ± xⱼ); for k ≥ 3, conditioning on the signs of the
other active coordinates, a fixed target value is hit by at most 2 of the
4 sign pairs of two chosen active coordinates, and hitting exactly 2
forces target 0 = −a₀ − R for every rest-sum R, impossible since R takes
≥ 2 values. (iii) For an incompatible pair, every f vanishes on U_G and
every g on U_F, so by (i) |U_F| = |U_G| = 2^{N−1}, U_G = U_F^c, every
f ∈ supp 𝐅 has support exactly U_F and zero set exactly U_G, which by
(ii) forces V_{U_F} to be one-dimensional of the listed forms; each such
unit function has some Inf_i = 1/2 exactly, and every member of supp 𝐅
is the same function up to phase, so averaging cannot help. ∎

**Computation C1** (`d1_z2_exhaustive.py`, exact rational arithmetic,
all partitions up to cube symmetry): N = 1,2,3,4 → all feasible
partitions (1, 2, 2, 2 orbits respectively) have both sides
one-dimensional and value exactly 1/2. Confirms the theorem and its
rigidity mechanism. **The bottom rung shows zero N-decay.**

**ℤ₃, d = 1** (`z3_d1.py`, float SDP, exhaustive over all partitions):
ε*(ℤ₃,1,1) = 2/3; ε*(ℤ₃,1,2) = 0.500000000 (all binding orbits have
both sides one-dimensional). No group advantage at d = 1. Coverage stops
at N = 2 (N = 3 has 2^26 partitions; not searched).

## 3. Target 2: the 1/(2d) regime, rediscovered and verified

**Grid pair** (found by optimizing cross-conflicting subcube designs; this
is presumably [ACC22]'s K2 object, obtained here independently): cells
(r,c) of a d×d grid, N = d²;
f_r = ∏_c (1+x_{r,c})/2^{d/2} (row r all +1), 𝐅 uniform over rows;
g_c = ∏_r (1−x_{r,c})/2^{d/2} (column c all −1), 𝐆 uniform over columns.
Row r and column c clash at cell (r,c). E Inf = (1/d)(1/2) = **1/(2d)**
exactly on every coordinate, both sides.

Verified (`grid_construction.py`) by two independent exact methods:
pointwise enumeration of all 2^{d²} points plus integer Walsh–Hadamard
influence computation (d ≤ 4), and the combinatorial coefficient argument
(d ≤ 8). **K2 confirmed: the conjecture's witness needs δ(d) < 1/(2d).**

**Every group:** replacing (1±x)/√2 by √q·1_{x=0} / √q·1_{x=1} gives the
same design over ℤ_q with influence (1/d)(1−1/q); verified for ℤ₃, d = 2
(`zq_grid.py`; disjointness exact, the rest to 1e−12). Any finite abelian
𝒴 contains two distinct elements, so **ε*(𝒴,d) ≤ (1−1/|𝒴|)/d for every
𝒴: a witnessing δ must have c₂ ≥ 1 regardless of the group.**

## 4. Target 3: below 1/(2d) — the money question

### 4.1 The certified 1/5 pair at d = 2 (K2's frontier is not tight)

Exhaustive SDP over all 221 partition orbits of {±1}⁴ at d = 2
(`dd_z2_exhaustive.py`): minimum ≈ 0.2000000. Extraction
(`inspect_witness.py`) revealed a **singleton–singleton** optimum, and
`cert_exact.py` certifies in pure rational arithmetic:

    f = (2 + x1 + x2 + x3 + x4 + x2x3 + x1x4)/√10
    g = −(x1 + x4 − 2)(x2 + x3 − 2)/6

deg = 2, unit norms, f·g ≡ 0 at all 16 points, Inf_i(f) = 1/5 and
Inf_i(g) = 1/6 for **all** i, and (dual PSD certificates, exact) no
distribution on either side of this partition beats 1/5. With the float
margins on the other orbits (all ≥ 0.2499) and exact certificates on the
two binding orbits (`cert_witness2.py`): **ε*(2,4) = 1/5 exactly.**

Structure: with u = x1+x4, v = x2+x3 ∈ {−2,0,2} (two 2-coordinate blocks
simulating a 3-letter alphabet), f ∝ φ(u) + φ(v) with φ(u) = (u+1)²−1 ≥ 0
vanishing on {−2,0}, and g ∝ (u−2)(v−2). "Union side" = sum of block
indicators; "product side" = product of degree-1 block factors.

### 4.2 The block family and the record ratio 4/11

Generalizing (`records.py`, all claims exact): m blocks of b coordinates,
marked = block all-+1; f = Σⱼ 1_{markedⱼ} (degree b),
g = ∏ⱼ (Σ_block x − b)/√(b+b²) (degree m). Exact influences:

    Inf_i(f) = 1/(2m(1+(m−1)2^{−b})),   Inf_i(g) = 1/(b+b²),
    d = max(b,m),  value V(b,m) = max of the two.

| seed | d | N | value | ratio d·V | status |
|---|---|---|---|---|---|
| (b,m)=(1,1) | 1 | 1 | 1/2 | 1/2 | exact (= grid) |
| (b,m)=(2,2) | 2 | 4 | **1/5** | 2/5 | exact, certified optimal for its partition |
| (b,m)=(3,3) | 3 | 9 | **2/15** | 2/5 | exact |
| (b,m)=(3,4) | 4 | 12 | **1/11** | **4/11** | exact |

Sweep over all (b,m) with b ≤ 7, m ≤ 24: the family's ratio is minimized
at **4/11 ≈ 0.3636** (attained at (3,4) and (4,7)); for large d it drifts
back up toward ~0.43. SDP probes with degree slack (`probe_f34.py`)
average the union side of the (3,4) partition down to 0.0908688 (float),
a further ~0.05% — the product side is pinned at exactly 1/12.

### 4.3 Transport to all degrees

**Transport lemma.** Given an incompatible pair (f,g) on ℤ₂^n, deg ≤ d₀,
influences ≤ (a,b): on a D×D grid of n-coordinate blocks set
f_R = ⊗_C f (row R), g_C = ⊗_R g (column C), 𝐅/𝐆 uniform over
rows/columns. Tensors over disjoint blocks multiply Fourier coefficients,
so norms stay 1, degrees multiply by D, and a coordinate in block (R,C)
has E_𝐅 Inf = a/D (activity probability 1/D). Row R and column C share
block (R,C), where supp f ∩ supp g = ∅. Hence a pair at degree D·d₀ with
influences (a/D, b/D). Verified **exactly** at D = 2 with the 1/5 seed
(`compose_verify.py`): d = 4, N = 16, influences (1/10, 1/12).

Corollary: **ε*(ℤ₂, 4D) ≤ 1/(11D)**, i.e. ε*(d) ≤ (4/11 + o(1))/d; with
§3, every even-order group inherits this via pullback along a surjection
𝒴 → ℤ₂ (characters pull back to characters, degrees/norms/influences and
supports are preserved), and every group has ε* = O(1/d) by the ℤ_q grid.
**Composition preserves the product ε·d exactly — it can transport a good
seed but can never improve the rate.**

### 4.4 Searches that found nothing better (exact coverage)

| search | space covered | result | what the null rules out / does not |
|---|---|---|---|
| exhaustive SDP, d=2, N=3 | all 13 partition orbits | min = 1/4 (float, margin 1e−7) | ε*(2,3) = 1/4: MUX/grid-equivalent optimal at N=3. Nothing beyond N=3. |
| exhaustive SDP, d=2, N=4 | all 221 orbits (= all 32767 partitions) | min = 1/5, certified | 1/5 is exactly optimal at N=4. Nothing about N ≥ 5. |
| exhaustive SDP, d=3, N=4 | all 221 orbits | min ∈ [0.18668134005, 0.18668136521] (no small quadratic fits) | value at (3,4); N ≥ 5 open. |
| SA, d=2, N=5 | 1044 distinct partitions (of ~2^31; seeds: block partition + random; 400-step anneals) | best 0.2000 | 1/5 not beaten in the explored neighborhoods; vast majority of partitions unexplored. |
| SA, d=2, N=6 | 666 distinct partitions | best 0.2000 | same caveat, weaker coverage. |
| SA, d=3, N=6 | 1027 distinct partitions | best 1/6 (= block(2,3) value) | consistent with 2/15 requiring N=9; not a proof. |
| Boolean scan, d=2 | all 65536 truth tables on 4 vars → all 212 degree-2 Boolean functions (exhaustive for d=2 if Nisan–Szegedy's ≤ d·2^{d−1} relevant-variable bound holds [MEMORY]) | best Boolean-derived pair value 1/4 | Boolean σ-pairs ((1±σ)/√2) cannot reach 1/5: the record is essentially non-Boolean. |
| structured probes (`probes.py`) | block partitions at (3,6),(3,6'),(2,6),(4,8),(4,8'),(3,9),(4,12) | product side exactly 1/6 resp. 1/12 in every case; union side SDP-averages down (e.g. 0.0632 < 1/14 at (4,8)) | averaging helps only the union side, and only with degree slack. |

All float SDP numbers are two-sided (dual eigenvalue lower bound at an
explicit w; explicit-mixture upper bound), reliable to ~1e−8; every
load-bearing minimum was re-certified in exact rational arithmetic.

## 5. The obstruction (why everything saturates at Θ(1/d))

Three independent walls were hit, and together they explain the profile:

**(O1) Conflict localization / union bound.** *Theorem (exact, proof
below): within the class of subcube-indicator distributions (every
support function a normalized ±indicator of a codim-≤d subcube), every
incompatible pair has max per-coordinate average influence ≥ 1/(2d); the
grid is extremal.* Proof: draw f,g independently; incompatibility means
they always conflict, and two subcubes are disjoint iff some shared
coordinate is forced to opposite signs, so
1 = Pr[conflict] ≤ Σᵢ Pr_F[i active]·Pr_G[i active] ≤ (2δ)·Σᵢ Pr_F[i
active] = 2δ·E|T| ≤ 2δd (influence of an active coordinate is exactly
1/2, so Pr[i active] = 2·E Inf_i ≤ 2δ). ∎
Every construction found evades this only by enlarging the local alphabet
(blocks): the conflict is then witnessed by a shared *block*, the same
argument runs at block granularity, and the gain is confined to the
per-block constants.

**(O2) The union/product asymmetry.** The sub-1/(2d) gains all come from
the union side f = Σⱼ(block indicators), whose per-coordinate influence
decays *quadratically* (norm² grows like m²·μ² once m ≳ 1/μ = 2^b blocks
are summed). But a union-side support {∃ marked block} forces the partner
to vanish on a union of block events, and (verified by the SDP probes:
product sides pinned at exactly 1/(b+b²)) the partner is forced into a
*product* with a factor per block — degree grows linearly in the number
of blocks while its per-coordinate influence is a constant 1/(b+b²).
Balancing the two sides optimizes at small b (the m ≈ 2^b saturation),
yielding exactly the observed 2/5 → 4/11 plateau. Within all
sum/product block architectures the ratio ε·d is bounded below by an
absolute constant; no choice of (b, m, designs) reaches o(1/d).

**(O3) Boolean impossibility.** Any pair of the form (1±σ)/√2 with σ
Boolean has value maxᵢ Inf_i(σ)/2, and [MEMORY — folklore chain, not
load-bearing: OSSS inequality + polynomial degree-vs-decision-tree-depth]
Var(σ) ≤ (max Inf)·DTdepth ≤ (max Inf)·poly(d), so Boolean-derived pairs
can never certify falsity (they are 1/poly(d)-bounded *provably*). The
counterexample, if it exists, must be essentially non-Boolean: spiky
nonnegative densities (our record f's are exactly that — sums of
indicators with sup-norm ≫ 1), the regime in which the Aaronson–Ambainis
kin (K4) has been open since 2009.

**(O4) The floor.** If K1 is confirmed (ε*(𝒴,d) ≥ |𝒴|^{−d}/d), no finite
search can falsify at fixed d; the open window is exactly
[2^{−d}/d, (4/11 + o(1))/d] for ℤ₂, and the refutation would have to
produce, for each polynomial p, some d with an incompatible pair at
influence < 1/p(d) — a construction whose per-block "conflict-cost /
influence-paid" ratio improves without bound. Nothing in the searched
architectures suggests a mechanism for that; O1–O2 suggest a proof of
the conjecture should be attempted at δ(d) = c/d via a weighted
conflict-localization argument (make the union bound work for general
low-degree supports, using the density reformulation: incompatibility ⟺
E[u·v] = 0 for u = E_𝐅|f|², v = E_𝐆|g|², nonneg, mean-1, degree ≤ 2d,
i.e. Cov(u,v) = −1 with all the anticorrelation carried on shared
low-degree characters).

## 6. Implausible-consequence check (§3.4 review update)

Neither truth value yields an implausible consequence against the
assumption hierarchy. FALSE: [CLM23]'s separations (and the [ACC22]
poly-query QROM key-agreement route) lose their engine — a dead proof
technique, not a new object or algorithm; falsity constructs nothing
cryptographic, places nothing in Pessiland, and gives no subexponential
algorithm for anything well-studied. Moreover K4 notes a later work
(arXiv:2504.05710) bypasses the conjecture downstream, so even the
application pressure is mild. TRUE: an Aaronson–Ambainis-strength theorem
— surprising mathematically, implausible to *prove cheaply*, but
consistent with everything known. One directional note: falsity would
imply a dramatic and provable Boolean-vs-L2-normalized separation (O3
shows the Boolean analogue is 1/poly-bounded), which is exactly the
separation AA-experience deems plausible-but-hard; nothing forbids it.
**No IMPLAUSIBLE CONSEQUENCE verdict in either direction.**

## 7. Outputs a Prover/Strategist should take from this

1. ε*(1,N;ℤ₂) = 1/2 ∀N (Theorem R-1, with proof) — a frozen-chain
   candidate and the d=1 rung settled.
2. ε*(2,3) = 1/4, ε*(2,4) = 1/5 (exact), ε*(3,4) ∈ [0.186681340,
   0.186681366]; ε*(3,9) ≤ 2/15, ε*(4,12) ≤ 1/11, ε*(ℤ₂,4D) ≤ 1/(11D)
   (exact constructions). K2 confirmed independently and improved by the
   constant 8/11.
3. The conjecture's viable window is now c₂ ≥ 1 (every group), c₁ ≤ 4/11
   effectively (even-order groups) — the natural target statement to
   prove is δ(d) = c/d, and the diagnosed obstruction (O1/O2) is where a
   proof should look: a block-granular conflict-localization inequality
   for general low-degree disjoint supports.
4. Warning to provers: per-function influence bounds are NOT equivalent
   to the average-influence hypothesis, but the d=2 record shows the
   distinction is not yet load-bearing at small d (the record is a
   singleton pair); distributions only mattered via the grid/design
   spreading (exactly a factor 1/D).

## 8. Code manifest (all under `proofs/0023-refuter-1-code/`)

`pcc_lib.py` (reductions R1–R3, exact rational linear algebra, exact PSD
checker, Kelley-cutting-plane SDP with certified two-sided bounds, cube
symmetry orbits, ℤ_q machinery) · `d1_z2_exhaustive.py` (C1) ·
`grid_construction.py` (K2, two methods) · `dd_z2_exhaustive.py`
(exhaustive orbit SDPs) · `inspect_witness.py` · `cert_exact.py` (the 1/5
certificate) · `cert_witness2.py` · `records.py` (block family, exact) ·
`compose_verify.py` (transport, exact at D=2; block(2,3) at d=3) ·
`probes.py`, `probe_f34.py` (structured probes) · `sa_search.py`
(+ `.out`) · `z3_d1.py` · `boolean_d2.py` · `zq_grid.py`. Total compute
≈ 7 minutes wall clock; environment: python3.14 venv with numpy 2.5.2,
scipy 1.18.1.

### END OF ARTIFACT 0023-refuter-1 ###
