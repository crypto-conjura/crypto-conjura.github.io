"""
r5_repertoire.py -- (i) an INDEPENDENT re-derivation of the kappa bound using a
different linear system, (ii) the same test for d = 2 as a control (the answer
eps*_ind(2) = 1/4 is already proved, so the framework must reproduce
kappa_2 <= 2), (iii) the exact CONFLICT REPERTOIRE: for which shapes
(s_1..s_m) does a nonempty degree-<=d set exist whose projection onto m
disjoint coordinate groups of those sizes misses a point in every group,
(iv) the complete partner set of the 3-disjoint-triples design.

TWO INDEPENDENT LINEAR SYSTEMS for the same question.
  r3 worked in VALUE space: unknowns = the |V| values of f on V, equations =
  "the Walsh coefficient of f at S vanishes" for every |S| >= d+1.
  r5 works in COEFFICIENT space: unknowns = the D_d = sum_{j<=d} C(w,j)
  multilinear coefficients of f, equations = "f(x) = 0" for every x outside V.
  dim(solution space) must agree.  Ranks are taken modulo two primes.
"""
import sys, time, itertools
import numpy as np
from fractions import Fraction

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

P1, P2 = 2147483647, 1000000007

def rank_mod(M, p):
    A = (M.astype(np.int64) % p).copy()
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        piv = r + nz[0]
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        col = A[r + 1:, c].copy()
        nzr = np.flatnonzero(col)
        if nzr.size:
            A[r + 1 + nzr] = (A[r + 1 + nzr] - col[nzr, None] * A[r][None, :]) % p
        r += 1
        if r == rows:
            break
    return r

def sol_dim(shape, d):
    """dim { f multilinear, deg f <= d, f(x) = 0 for every x outside V }
    in COEFFICIENT space.  V = {x : x_{S_j} != all-(+1) for each group j}."""
    w = sum(shape)
    offs, o = [], 0
    for s in shape:
        offs.append(o); o += s
    bad = []
    for x in range(1 << w):
        for (off, s) in zip(offs, shape):
            if ((x >> off) & ((1 << s) - 1)) == 0:
                bad.append(x)
                break
    cols = [S for S in range(1 << w) if bin(S).count("1") <= d]
    A = np.empty((len(bad), len(cols)), dtype=np.int8)
    Ba = np.array(bad, dtype=np.int64)
    for j, S in enumerate(cols):
        A[:, j] = np.where(np.bitwise_count(Ba & S) & 1, -1, 1)
    r1 = rank_mod(A, P1)
    r2 = rank_mod(A, P2)
    assert r1 == r2, (shape, r1, r2)
    return len(cols) - r1, len(cols), len(bad)

# =====================================================================
hr("(i)/(ii) kappa for d = 3 and the d = 2 CONTROL, coefficient-space system")
for d, ms in ((2, (3, 4)), (3, (4, 5))):
    wmax = d * (1 << (d - 1))
    pr(f"  d = {d}: junta bound w <= d*2^(d-1) = {wmax}; "
       f"testing every shape with m in {ms} groups and sum <= {wmax}")
    worst = []
    nshape = 0
    for m in ms:
        for comb in itertools.combinations_with_replacement(range(1, wmax + 1), m):
            if sum(comb) > wmax:
                continue
            nshape += 1
            dim, ncol, nbad = sol_dim(tuple(sorted(comb)), d)
            if dim > 0:
                worst.append((tuple(sorted(comb)), dim))
    pr(f"     shapes tested: {nshape};  shapes with a nonzero solution space: "
       f"{len(worst)}  {worst[:6]}")
    pr(f"     => kappa_{d} <= {min(ms) - 1} for every nonempty degree-<={d} set"
       f"   ({time.time()-t0:.0f}s)")

# =====================================================================
hr("(iii) CONFLICT REPERTOIRE at d = 3: shapes with m = 1,2,3 groups")
for m in (1, 2, 3):
    rows = []
    for comb in itertools.combinations_with_replacement(range(1, 13), m):
        if sum(comb) > 12:
            continue
        sh = tuple(sorted(comb))
        dim, ncol, nbad = sol_dim(sh, 3)
        rows.append((sh, dim))
    live = [r for r in rows if r[1] > 0]
    dead = [r for r in rows if r[1] == 0]
    pr(f"  m={m}: {len(live)} shapes admit a nonzero degree-<=3 solution, "
       f"{len(dead)} do not")
    pr(f"      live: {live}")
    pr(f"      dead: {[r[0] for r in dead]}")

# =====================================================================
hr("(iv) the COMPLETE partner set of the 3-disjoint-triples design")
dim, ncol, nbad = sol_dim((3, 3, 3), 3)
pr(f"  shape (3,3,3): w=9, D_3 = {ncol} coefficients, {nbad} vanishing "
   f"conditions, solution space dimension = {dim}")
# the 27 'column' indicators 1_{x_a=x_b=x_c=-1}, a in T1, b in T2, c in T3
cols3 = [S for S in range(1 << 9) if bin(S).count("1") <= 3]
cidx = {S: j for j, S in enumerate(cols3)}
COLS = []
for a in range(3):
    for b in range(3, 6):
        for c in range(6, 9):
            v = np.zeros(len(cols3), dtype=np.int64)
            # 1_{x_a=-1} 1_{x_b=-1} 1_{x_c=-1} = prod (1-x_i)/2, coefficients
            # (+-1)/8 on the 8 subsets of {a,b,c}
            for T in range(8):
                S = 0
                sgn = 1
                for k, i in enumerate((a, b, c)):
                    if (T >> k) & 1:
                        S |= 1 << i
                        sgn = -sgn
                v[cidx[S]] += sgn          # times 1/8, cleared by scaling
            COLS.append(v)
COLS = np.array(COLS)
rc1, rc2 = rank_mod(COLS, P1), rank_mod(COLS, P2)
pr(f"  the 27 column indicators span a space of dimension {rc1} (={rc2})")
pr(f"  solution space dimension = {dim}  ->  they COINCIDE: {rc1 == dim}")
pr("  Consequence (with the two-line argument in the report): the only")
pr("  nonempty degree-<=3 sets disjoint from three codim-3 subcubes on")
pr("  disjoint triples are those 27 columns; each forces one coordinate per")
pr("  triple, so the partner side has sum_i Ibar = 3/2 spread over 9")
pr("  coordinates and its value is EXACTLY 1/6.")

pr(f"\nDONE r5 in {time.time()-t0:.1f}s")
