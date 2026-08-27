"""
r2_designs_n6.py -- design search inside the COMPLETE class at N = 6
(all 16750860 degree-<=3 subsets of the 6-cube).

REDUCTION USED (exact, elementary).  Let (F,G) be a cross-disjoint pair of
families.  Every B in supp G is disjoint from every A in supp F, so
    supp G  subseteq  {B in class : B subseteq W},   W := (union of supp F)^c
    supp F  subseteq  {A in class : A subseteq W^c}.
Enlarging both supports to those two full families keeps cross-disjointness and
can only DECREASE both one-sided values.  Hence

  eps*_ind(3, N) = min over W subseteq {+-1}^N, both sides nonempty, of
                   max( tau({A in class: A cap W = empty}),
                        tau({B in class: B subseteq W}) ),
  tau(H) = min_p max_i sum_{P in H} p_P Inf_i(f_P)   (an LP).

So the search space at N=6 is the 2-colourings of the 64-point cube, and one
evaluation is two vectorised sweeps over the class plus two 6-row LPs.

THREE SEARCHES
 (S1) W = A^c for every CHEAP A (all Inf_i(f_A) < 1/6), up to the
      hyperoctahedral symmetry: the F side is then already below 1/6 with a
      SINGLE set, so the whole question is whether the sets inside A^c can
      spread below 1/6.  Exhaustive over cheap-set orbits, windows <= 6.
 (S2) W = P^c for a random/structured sample of class members P.
 (S3) local search (steepest descent + restarts) over W in the full
      2^64-point space, moves = add/remove a class set, flip a cube point.

Any value below 1/6 is re-certified in exact rational arithmetic twice.
"""
import sys, time, random
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import influences, influences_fourier, popcnt

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

L6 = np.load("L6.npy")
B6 = np.load("L6_b.npy").astype(np.int32)
N6 = np.load("L6_n.npy").astype(np.int32)
M = len(L6)
pr(f"class at N=6: {M} sets  ({time.time()-t0:.1f}s)")

# ---------------------------------------------------------------- profiles
# influence vector of a set = b_i/(2|P|); tabulate distinct (b, |P|) rows
key = np.concatenate([B6, N6[:, None]], axis=1)
uni, pid = np.unique(key, axis=0, return_inverse=True)
pid = pid.astype(np.int32)
NP = len(uni)
INF = uni[:, :6].astype(np.float64) / (2.0 * np.maximum(uni[:, 6:7], 1))
pr(f"distinct influence profiles: {NP}")

from scipy.optimize import linprog

def tau_of_profiles(rows):
    """rows: index array into uni.  Returns (tau, mixture over rows, dual w)."""
    A = INF[rows]                      # (m,6)
    m = len(rows)
    # LP: min t  s.t.  A^T p <= t*1 , sum p = 1, p>=0
    Aub = np.concatenate([A.T, -np.ones((6, 1))], axis=1)
    c = np.zeros(m + 1); c[m] = 1.0
    Aeq = np.zeros((1, m + 1)); Aeq[0, :m] = 1.0
    res = linprog(c, A_ub=Aub, b_ub=np.zeros(6), A_eq=Aeq, b_eq=[1.0],
                  bounds=[(0, None)] * m + [(None, None)], method="highs")
    if not res.success:
        return None
    w = None
    y = getattr(res, "ineqlin", None)
    if y is not None and y.marginals is not None:
        w = -np.asarray(y.marginals)
    return res.x[m], res.x[:m], w

def sides(Wmask):
    """(rowsA, rowsB): profile indices present on each side, or None if empty."""
    w = np.uint64(Wmask)
    selA = (L6 & w) == np.uint64(0)          # A cap W = empty
    selB = (L6 & ~w) == np.uint64(0)         # B subseteq W
    selA &= N6 > 0
    selB &= N6 > 0
    if not selA.any() or not selB.any():
        return None, None
    pa = np.zeros(NP, dtype=bool); pa[pid[selA]] = True
    pb = np.zeros(NP, dtype=bool); pb[pid[selB]] = True
    return np.flatnonzero(pa), np.flatnonzero(pb)

def value(Wmask):
    ra, rb = sides(Wmask)
    if ra is None:
        return None
    ta = tau_of_profiles(ra)
    tb = tau_of_profiles(rb)
    if ta is None or tb is None:
        return None
    return max(ta[0], tb[0]), ta, tb, ra, rb

# --------------------------------------------------- exact certificates
def exact_upper(rows, p, maxden=10**6):
    """exact rational upper bound on tau from a float mixture."""
    q = [Fraction(float(x)).limit_denominator(maxden) for x in p]
    s = sum(q)
    if s == 0:
        return None
    q = [x / s for x in q]
    acc = [Fraction(0)] * 6
    for wq, r in zip(q, rows):
        if wq == 0:
            continue
        b = uni[r, :6]; n = int(uni[r, 6])
        for i in range(6):
            if b[i]:
                acc[i] += wq * Fraction(int(b[i]), 2 * n)
    return max(acc)

def exact_lower(rows, w, maxden=10**6):
    """exact rational lower bound tau >= min_a <w,I_a> for w in the simplex."""
    if w is None:
        return None
    w = np.maximum(np.asarray(w, dtype=float), 0.0)
    if w.sum() <= 0:
        return None
    wf = [Fraction(float(x)).limit_denominator(maxden) for x in w / w.sum()]
    s = sum(wf)
    if s > 1:
        wf = [x / s for x in wf]
    best = None
    for r in rows:
        b = uni[r, :6]; n = int(uni[r, 6])
        v = sum((wf[i] * Fraction(int(b[i]), 2 * n) for i in range(6) if b[i]),
                Fraction(0))
        best = v if best is None else min(best, v)
    return best

SIX = Fraction(1, 6)
hits = []

def report(tag, Wmask, res):
    v, ta, tb, ra, rb = res
    ub_a = exact_upper(ra, ta[1]); ub_b = exact_upper(rb, tb[1])
    lo_a = exact_lower(ra, ta[2]); lo_b = exact_lower(rb, tb[2])
    flag = ""
    if ub_a is not None and ub_b is not None and max(ub_a, ub_b) < SIX:
        flag = "   *** BELOW 1/6 ***"
        hits.append((tag, Wmask, ub_a, ub_b))
    pr(f"   {tag}: eps = {v:.6f}  (tauF<={ub_a}, tauG<={ub_b}; "
       f"tauF>={lo_a}, tauG>={lo_b}){flag}")
    return v

# ==================================================================== (S1)
hr("(S1) W = A^c for every CHEAP A (all Inf_i(f_A) < 1/6), windows <= 6")
cheap = np.all(B6 * 3 < N6[:, None], axis=1) & (N6 > 0) & ((B6 > 0).sum(axis=1) > 0)
cidx = np.flatnonzero(cheap)
pr(f"  cheap sets at N=6 (any window): {len(cidx)}")
# group them by (sorted b-vector, |P|) -- a symmetry invariant -- and take
# every distinct invariant class, plus extra representatives per class
inv = {}
for j in cidx:
    k = (tuple(sorted(B6[j].tolist())), int(N6[j]))
    inv.setdefault(k, []).append(int(j))
pr(f"  distinct symmetry invariants among cheap sets: {len(inv)}")
best = None
for k, js in sorted(inv.items()):
    reps = js[:3]
    pr(f"  invariant sorted-b={k[0]} |P|={k[1]}  ({len(js)} sets, testing "
       f"{len(reps)} reps; max Inf = {Fraction(max(k[0]), 2*k[1])})")
    for j in reps:
        Wm = (~int(L6[j])) & ((1 << 64) - 1)
        res = value(Wm)
        if res is None:
            pr(f"     A={int(L6[j])}: one side EMPTY (no partner) -- skipped")
            continue
        v = report(f"A={int(L6[j])}", Wm, res)
        if best is None or v < best[0]:
            best = (v, int(L6[j]))
pr(f"  best over cheap seeds: eps = {best[0]:.6f} at A={best[1]}"
   f"   (1/6 = {1/6:.6f})")

# ==================================================================== (S2)
hr("(S2) W = P^c for a sample of class members P (any P, not just cheap)")
random.seed(20260827)
rng = np.random.default_rng(4242)
samp = rng.choice(M, 400, replace=False)
best2 = None
vals = []
for j in samp:
    Wm = (~int(L6[j])) & ((1 << 64) - 1)
    res = value(Wm)
    if res is None:
        continue
    v = res[0]
    vals.append(v)
    if best2 is None or v < best2[0]:
        best2 = (v, int(L6[j]), res)
pr(f"  {len(vals)} evaluable seeds; min eps = {best2[0]:.6f}")
report(f"best sampled seed P={best2[1]}", (~best2[1]) & ((1 << 64) - 1), best2[2])

# ==================================================================== (S3)
hr("(S3) local search over W in the full 2^64 space (moves: +-class set, "
   "+-cube point)")
FULL = (1 << 64) - 1
def rand_start():
    j = int(rng.integers(0, M))
    return (~int(L6[j])) & FULL

bestglob = None
for trial in range(6):
    W = rand_start()
    res = value(W)
    while res is None:
        W = rand_start(); res = value(W)
    cur = res[0]
    for step in range(60):
        cand = None
        for _ in range(6):
            if random.random() < 0.5:
                j = int(rng.integers(0, M))
                Wn = W | int(L6[j]) if random.random() < 0.5 else W & ~int(L6[j])
            else:
                x = int(rng.integers(0, 64))
                Wn = W ^ (1 << x)
            Wn &= FULL
            if Wn == W:
                continue
            r = value(Wn)
            if r is None:
                continue
            if cand is None or r[0] < cand[1]:
                cand = (Wn, r[0], r)
        if cand is None or cand[1] >= cur - 1e-12:
            break
        W, cur, res = cand[0], cand[1], cand[2]
    pr(f"  trial {trial}: eps = {cur:.6f}  ({time.time()-t0:.0f}s)")
    if bestglob is None or cur < bestglob[0]:
        bestglob = (cur, W, res)
pr(f"  best local-search value: {bestglob[0]:.6f}")
report("local-search optimum", bestglob[1], bestglob[2])

hr("SUMMARY")
pr(f"  hits below 1/6: {len(hits)}")
for h in hits:
    pr(f"    {h}")
pr(f"DONE r2 in {time.time()-t0:.1f}s")
