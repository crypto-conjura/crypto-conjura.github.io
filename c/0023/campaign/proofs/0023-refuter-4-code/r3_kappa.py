"""
r3_kappa.py -- the CONFLICT-CAPACITY test, and independent verification of the
window-6 / window-7 objects found by r1b / r1c.

WHY kappa MATTERS.  Suppose the F-side of a design is K codimension-3 subcubes
sitting on K PAIRWISE DISJOINT coordinate triples T_1..T_K (all coordinates
forced to +1).  Then Ibar_F(i) = (1/K)(1/2) = 1/(2K) < 1/6 as soon as K >= 4,
so the F side alone would beat 1/(2d) = 1/6.  Every partner B must satisfy
B cap A_a = empty for each a, i.e. the projection of B onto each triple T_a
must MISS the point (+,+,+).  So a partner exists only if some degree-<=3 set
is "constrained" (has a non-surjective projection) on K disjoint coordinate
groups at once.  Define

   kappa(A) = max # of pairwise disjoint coordinate groups S_1..S_m
              with pi_{S_j}(A) != full cube  (A nonempty, deg 1_A <= 3).

FINITE REDUCTION (exact).  If A subseteq {+-1}^n is constrained on disjoint
groups S_1..S_m, restrict every coordinate outside S_1 u ... u S_m to a value
where A stays nonempty: the restriction is a nonempty degree-<=3 set on
w = sum|S_j| coordinates, still constrained on the same groups.  Also every
degree-<=3 set is a junta on at most d*2^(d-1) = 12 coordinates
(Inf_i(h) >= 2^(1-d) = 1/4 for every relevant i and sum_i Inf_i(h) <= d = 3),
so w <= 12.  Hence kappa >= m is possible iff, FOR SOME SHAPE
(s_1..s_m), sum s_j <= 12, there is a nonempty {0,1}-valued degree-<=3
function on w coordinates supported inside

   V = intersect_j { x : x_{S_j} != r_j }        (WLOG r_j = all-(+1)),

and a shape with a SMALLER missing set is weaker, so testing "each projection
misses exactly one point" covers every constrained configuration.

The test is exact linear algebra: the degree-<=3 functions supported in V form
the kernel of the |{S : |S| >= 4}| x |V| integer matrix (chi_S(x)); if the
kernel is 0 there is no such set at all.  Ranks are computed modulo two
different large primes.
"""
import sys, time, itertools
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import max_degree, influences, influences_fourier

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

# =====================================================================
hr("(A) independent verification of a GENUINE window-7 degree-3 set")
# from r1c: lo=10305009121259077630, hi=9291644006787366910, |P|=80,
# b=[16,24,24,24,16,16,24]
lo, hi = 10305009121259077630, 9291644006787366910
P7 = lo | (hi << 64)
pts = [m for m in range(128) if (P7 >> m) & 1]
pr(f"  |P| = {len(pts)} (expect 80)")
# brute-force multilinear expansion, exact integers
coef = {}
for S in range(128):
    c = sum(-1 if bin(S & m).count("1") & 1 else 1 for m in pts)
    if c:
        coef[S] = Fraction(c, 128)
deg = max(bin(S).count("1") for S in coef)
pr(f"  brute-force degree of 1_P = {deg} (expect 3)")
rel = [i for i in range(7)
       if any(((P7 >> m) & 1) != ((P7 >> (m ^ (1 << i))) & 1) for m in range(128))]
pr(f"  relevant coordinates = {rel} (expect all 7)")
inf1 = [Fraction(sum(1 for m in pts if not ((P7 >> (m ^ (1 << i))) & 1)),
                 2 * len(pts)) for i in range(7)]
# Fourier-definition influences of f = 1_P/||1_P||_2
mu = Fraction(len(pts), 128)
inf2 = [Fraction(0)] * 7
for S, c in coef.items():
    for i in range(7):
        if (S >> i) & 1:
            inf2[i] += c * c / mu
pr(f"  influences (boundary count) = {[str(x) for x in inf1]}")
pr(f"  influences (Fourier def.)   = {[str(x) for x in inf2]}")
pr(f"  the two methods agree: {inf1 == inf2}")
pr(f"  max influence = {max(inf1)} vs 1/6 = {Fraction(1,6)}  -> cheap? "
   f"{max(inf1) < Fraction(1,6)}")
pr(f"  total influence T = {sum(inf1)}")
pr(f"  Fourier coefficients of 1_P by level: "
   f"{ {L: sorted({str(c) for S,c in coef.items() if bin(S).count('1')==L}) for L in range(4)} }")
pr(f"  #forced coordinates = "
   f"{sum(1 for i in range(7) if all(((m>>i)&1)==0 for m in pts) or all(((m>>i)&1)==1 for m in pts))}")

hr("(B) the minimiser of the singleton-complement frontier at k=6 (Phi=3/16)")
Q = 10507109030461310070
qpts = [m for m in range(64) if (Q >> m) & 1]
qc = {}
for S in range(64):
    c = sum(-1 if bin(S & m).count("1") & 1 else 1 for m in qpts)
    if c:
        qc[S] = Fraction(c, 64)
pr(f"  |P| = {len(qpts)}, degree = {max(bin(S).count('1') for S in qc)}")
pr(f"  influences of f_P: {[str(x) for x in influences(Q, 6)]}")
pr(f"  influences via Fourier: {[str(x) for x in influences_fourier(Q, 6)]}")
pr(f"  Inf_i(h) (h = 2*1_P-1) = "
   f"{[str(4*x*Fraction(len(qpts),64)) for x in influences(Q,6)]}")
pr(f"  Fourier support sizes by level: "
   f"{ {L: sum(1 for S in qc if bin(S).count('1')==L) for L in range(4)} }")
pr(f"  coefficient values: {sorted({str(c) for c in qc.values()})}")

# =====================================================================
hr("(C) kappa: is any degree-<=3 set constrained on m >= 4 disjoint groups?")

P1, P2 = 2147483647, 1000000007

def rank_mod(M, p):
    """rank of integer matrix M mod prime p (numpy int64 Gaussian elimination)."""
    A = (M.astype(np.int64) % p).copy()
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        piv = None
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        piv = r + nz[0]
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        col = A[r + 1:, c].copy()
        nzr = np.flatnonzero(col)
        if nzr.size:
            A[r + 1 + nzr] = (A[r + 1 + nzr] - col[nzr, None] * A[r][None, :]) % p
        r += 1
        if r == rows:
            break
    return r

def kernel_dim(shape, verbose=False):
    """dim of {f : deg f <= 3, supp f subseteq V} for the given group shape."""
    w = sum(shape)
    # coordinates: group j occupies a block; V = points avoiding all-zero
    # (i.e. all +1) on each block
    offs, o = [], 0
    for s in shape:
        offs.append(o); o += s
    V = []
    for x in range(1 << w):
        ok = True
        for (off, s) in zip(offs, shape):
            blk = (x >> off) & ((1 << s) - 1)
            if blk == 0:            # x_{S_j} = all +1  -> forbidden
                ok = False
                break
        if ok:
            V.append(x)
    hiS = [S for S in range(1 << w) if bin(S).count("1") >= 4]
    if not hiS:
        return len(V), len(V), None      # no constraint at all
    M = np.empty((len(hiS), len(V)), dtype=np.int8)
    Va = np.array(V, dtype=np.int64)
    for j, S in enumerate(hiS):
        M[j] = np.where(np.bitwise_count(Va & S) & 1, -1, 1)
    r1 = rank_mod(M, P1)
    r2 = rank_mod(M, P2)
    return len(V) - r1, len(V) - r2, (M, V)

shapes = []
for m in (4, 5):
    for comb in itertools.combinations_with_replacement(range(1, 10), m):
        if sum(comb) <= 12:
            shapes.append(tuple(sorted(comb)))
shapes = sorted(set(shapes), key=lambda s: (len(s), sum(s), s))
pr(f"  shapes to test (4 or 5 disjoint groups, total size <= 12): {len(shapes)}")
alive = []
for sh in shapes:
    w = sum(sh)
    d1, d2, extra = kernel_dim(sh)
    tag = "" if d1 == 0 else "   <-- NONZERO KERNEL"
    pr(f"   groups {sh} (w={w}, |V|={None if extra is None else len(extra[1])}): "
       f"dim = {d1} (mod p1), {d2} (mod p2){tag}   [{time.time()-t0:.0f}s]")
    if d1 != d2:
        pr("      !! rank differs between primes -- rerun exactly")
    if d1 > 0:
        alive.append((sh, d1, extra))

hr("(D) shapes with a nonzero kernel: hunt a {0,1}-valued member")
if not alive:
    pr("  NONE.  For every shape with 4 or 5 disjoint constrained groups and")
    pr("  total window <= 12, the ONLY degree-<=3 function supported in V is 0.")
    pr("  => kappa(A) <= 3 for every nonempty degree-<=3 set A, in every")
    pr("     dimension N.  A degree-3 set cannot be constrained on four")
    pr("     disjoint coordinate groups.")
else:
    for sh, d, extra in alive:
        M, V = extra
        pr(f"  shape {sh}: kernel dim {d} over Q; searching {{0,1}} members")
        # exact rational nullspace via sympy-free integer elimination:
        # brute force over small kernels only
        import numpy.linalg as la
        Mf = M.astype(np.float64)
        u, s, vt = la.svd(Mf, full_matrices=True)
        ns = vt[len(s) - int((s > 1e-8).sum()):]
        pr(f"    numeric nullspace rows: {ns.shape}")
        # a {0,1} vector in the kernel must have all its 0/1 pattern; test all
        # sign patterns only if dim is tiny
        if d <= 3:
            found = None
            import itertools as it
            grid = np.array(list(it.product(range(-4, 5), repeat=d)))
            for g in grid:
                v = (g[:, None] * ns).sum(axis=0)
                if np.allclose(v, np.round(v)) and set(np.round(v)).issubset({0.0, 1.0}) \
                        and np.round(v).sum() > 0:
                    found = np.round(v)
                    break
            pr(f"    {{0,1}}-valued kernel member found: {found is not None}")
        else:
            pr("    kernel too large for the brute-force sweep -- flag for follow-up")

pr(f"\nDONE r3 in {time.time()-t0:.1f}s")
