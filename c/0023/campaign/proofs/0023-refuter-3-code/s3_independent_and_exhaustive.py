"""
s3_independent_and_exhaustive.py

(I) INDEPENDENT verification of (LOC-2).  Completely different code path from
    s2: degree-<=2 sets are represented as BITMASKS OVER THE 2^N POINTS of
    {+-1}^N with N = 7 (every possible overlap of two windows of size <= 4 is
    realised: 4+4-1 = 7); disjointness is a mask AND; influences come from an
    integer Walsh-Hadamard transform over all 2^N points (the DEFINITION
    Inf_i = sum_{S ni i} fhat(S)^2, exact rationals) -- no (F1) boundary-count
    formula, no window/pattern WLOG, no symmetry reduction.

(II) EXACT SANDWICH for eps*_ind(d,N), all N.  For a family cA put
        tau(cA) = min_p max_i sum_a p_a Inf_i(a)
                = max_{w in simplex_N} min_{A in cA} <w, Inf(A)>  (minimax).
     For B_0 in the class let  cA(B_0) = {A in class : A cap B_0 = empty}.
       LOWER: any incompatible (F,G) has some g with support B_0, and then
              supp F subseteq cA(B_0), so
              max(delta_F,delta_G) >= tau(cA(B_0)) >= min_{B_0} tau(cA(B_0)).
       UPPER: (cA(B_0), cB) with cB = {B : B cap A = empty for all A in cA(B_0)}
              is a genuine incompatible pair containing B_0, so
              eps* <= min_{B_0} max(tau(cA(B_0)), tau(cB)).
     Up to the hyperoctahedral symmetry of the cube, B_0 may be taken to be a
     canonical pattern on the window {0..k-1}: the sweep over B_0 is therefore
     EXHAUSTIVE with only sum_k #patterns(k) representatives.
     If LOWER = UPPER the value of eps*_ind(d,N) is exact.
"""
import itertools
from fractions import Fraction
from deg_lib import genuine_patterns, JFun, popcount

def pr(*a):
    print(*a, flush=True)

def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

# ----------------------------------------------------------------------
def point_mask(W, pat, N):
    mask = 0
    for x in range(1 << N):
        m = 0
        for b, c in enumerate(W):
            if (x >> c) & 1:
                m |= 1 << b
        if m in pat:
            mask |= 1 << x
    return mask

def deg_sets_pointmasks(N, d, maxwin):
    """dict point-bitmask -> window tuple, over all degree-<=d sets."""
    out = {}
    for k in range(1, min(N, maxwin) + 1):
        for p in genuine_patterns(k, d):
            for W in itertools.combinations(range(N), k):
                mk = point_mask(W, p, N)
                if mk not in out:
                    out[mk] = W
    return out

def influences_from_points(mask, N):
    """Exact influences of 1_A/||1_A||_2 straight from the point mask, via an
    integer Walsh-Hadamard transform.  Integer accumulation, one division."""
    pts = [x for x in range(1 << N) if (mask >> x) & 1]
    sz = len(pts)
    acc = [0] * N
    for S in range(1, 1 << N):
        c = 0
        for x in pts:
            c += -1 if (popcount(S & x) & 1) else 1
        if c == 0:
            continue
        cc = c * c
        for i in range(N):
            if (S >> i) & 1:
                acc[i] += cc
    den = (1 << N) * sz
    return [Fraction(a, den) for a in acc], sz

# ----------------------------------------------------------------------
hr("(I) INDEPENDENT check of (LOC-2) on point masks, N = 7")
N = 7
D = deg_sets_pointmasks(N, 2, 4)
pr(f"  distinct degree-<=2 sets in {{+-1}}^{N}: {len(D)}")
INF = {}
for mask in D:
    inf, sz = influences_from_points(mask, N)
    rel = tuple(i for i in range(N) if inf[i] != 0)
    assert rel == D[mask], (rel, D[mask], "relevant-coordinate mismatch")
    INF[mask] = (inf, rel, sz)
vals = sorted(set(v for inf, _, _ in INF.values() for v in inf if v != 0))
pr(f"  influences via integer WHT; relevant sets match the windows in all"
   f" {len(D)} cases;  spectrum {vals}")

keys = list(D)
worst = None; npair = 0; noshare = 0
for ma in keys:
    infa, rela, _ = INF[ma]
    sa = set(rela)
    for mb in keys:
        if ma & mb:
            continue                      # not disjoint
        infb, relb, _ = INF[mb]
        npair += 1
        S = sa & set(relb)
        if not S:
            noshare += 1
        pi = sum((infa[i] + infb[i] for i in S), Fraction(0))
        rhs = Fraction(len(rela) + len(relb), 4)
        sl = pi - rhs
        if worst is None or sl < worst[0]:
            worst = (sl, pi, rhs, len(rela), len(relb), sorted(S), ma, mb)
pr(f"  ordered disjoint pairs examined: {npair};"
   f"  with empty shared window: {noshare} (must be 0)")
pr(f"  min of pi - (|J|+|K|)/4  =  {worst[0]}"
   f"   ==> (LOC-2) {'HOLDS' if worst[0] >= 0 else 'FAILS'}   [INDEPENDENT]")
pr(f"    extremal pair: |J|={worst[3]} |K|={worst[4]} S={worst[5]}"
   f" pi={worst[1]} rhs={worst[2]}")

# ----------------------------------------------------------------------
hr("(II) exact sandwich for eps*_ind(d,N)")
import numpy as np
from scipy.optimize import linprog

def tau_lp(infs, N):
    """max_{w in simplex} min_a <w, I_a>; returns (value, w, active list)."""
    m = len(infs)
    c = np.zeros(N + 1); c[N] = -1.0
    A_ub = np.zeros((m, N + 1)); b_ub = np.zeros(m)
    for a, I in enumerate(infs):
        for i in range(N):
            A_ub[a, i] = -float(I[i])
        A_ub[a, N] = 1.0
    A_eq = np.zeros((1, N + 1)); A_eq[0, :N] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, None)] * N + [(None, None)], method="highs")
    assert res.success, "LP failed"
    return res.x[N], res.x[:N]

def exact_lower_cert(infs, N, w):
    """w rational in the simplex -> tau >= min_a <w,I_a> (exact)."""
    return min(sum((w[i] * I[i] for i in range(N)), Fraction(0)) for I in infs)

def sandwich(N, d, maxwin, verbose=False):
    Dm = deg_sets_pointmasks(N, d, maxwin)
    masks = list(Dm)
    INFL = {}
    for m in masks:
        inf, _ = influences_from_points(m, N)
        INFL[m] = inf
    best_lo = None; best_up = None; arg_lo = None; arg_up = None
    reps = []
    for k in range(1, min(N, maxwin) + 1):
        for p in genuine_patterns(k, d):
            reps.append(point_mask(tuple(range(k)), p, N))
    for B0 in reps:
        A0 = [m for m in masks if not (m & B0)]
        if not A0:
            continue
        tA, wA = tau_lp([INFL[m] for m in A0], N)
        if best_lo is None or tA < best_lo:
            best_lo = tA; arg_lo = (B0, len(A0), wA)
        UA = 0
        for m in A0:
            UA |= m
        B1 = [m for m in masks if not (m & UA)]
        tB, wB = tau_lp([INFL[m] for m in B1], N)
        v = max(tA, tB)
        if best_up is None or v < best_up:
            best_up = v; arg_up = (B0, len(A0), len(B1), tA, tB)
    return best_lo, best_up, arg_lo, arg_up, len(masks), len(reps)

for (N_, d_, mw) in ((3, 2, 3), (4, 2, 4), (5, 2, 4), (6, 2, 4), (7, 2, 4),
                     (8, 2, 4), (3, 3, 3), (4, 3, 4)):
    lo, up, al, au, nsets, nreps = sandwich(N_, d_, mw)
    tag = "EXACT" if abs(lo - up) < 1e-9 else "sandwich"
    pr(f"  d={d_} N={N_}: |class|={nsets:6d} reps={nreps:5d}   "
       f"LB={lo:.10f}  UB={up:.10f}  [{tag}]   1/(2d)={1/(2*d_):.6f}")
    if au:
        pr(f"      best pair: |cA|={au[1]} |cB|={au[2]} tauF={au[3]:.8f} tauG={au[4]:.8f}")
pr("\nDONE s3")
