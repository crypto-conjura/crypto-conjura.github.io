"""
r1a_structure.py -- exact structure of the degree-<=3 class, windows k <= 5,
plus the exact size of the k=6 class.

WHAT IT SETTLES
 1. |L(k,3)| for k = 3,4,5 (cross-check against 0023-refuter-3 s1: 256, 12870,
    807980) and |L(6,3)| EXACTLY, by the grouping identity
    |L(k+1,3)| = sum_classes |class|^2 (no enumeration of level 6 needed).
 2. The exact set of achievable values of Inf_i(h) = b_i / 2^(k-1) over ALL
    degree-<=3 patterns with k <= 5 (h = +-1-valued version).  Tests (E3)
    (floor 1/4) and the "multiple of 1/4" quantisation.
 3. All CHEAP patterns (all influences of f_P below 1/6) with k <= 5, genuine,
    with their densities -- these are the only sets that can appear in a
    SINGLETON pair beating 1/6.
 4. The exact max relevant-coordinate count for degree <= 3 at k <= 5.
"""
import sys, time
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import (level3_all, next_level, coeffs, bvec, popcnt, group_by_key,
                  influences, influences_fourier, max_degree)

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

hr("(1) class sizes |L(k,3)|")
L = {3: level3_all()}
pr(f"  k=3: |L| = {len(L[3])}")
for k in (3, 4):
    L[k + 1] = next_level(L[k], k)
    pr(f"  k={k+1}: |L| = {len(L[k+1])}   ({time.time()-t0:.1f}s)")

# |L(6,3)| by the grouping identity, without enumerating level 6
grps5 = group_by_key(L[5], 5, sizes=(3,))
sizes5 = np.array([len(g) for g in grps5], dtype=np.int64)
pr(f"  k=5 groups (same deg-3 coefficient vector): {len(grps5)}, "
   f"max group {sizes5.max()}, sum {sizes5.sum()}")
pr(f"  => |L(6,3)| = sum |class|^2 = {int((sizes5.astype(object)**2).sum())}")

hr("(2) achievable Inf_i(h) = b_i / 2^(k-1)  (h = 2*1_P-1), all k <= 5")
allvals = {}
for k in (1, 2, 3, 4, 5):
    if k not in L:
        # small levels: rebuild from scratch (all patterns have degree<=3 for k<=3)
        L[k] = np.arange(1 << (1 << k), dtype=np.uint64) if k <= 2 else L[k]
    P = L[k]
    B = bvec(P, k)
    vals = set()
    for v in np.unique(B):
        if v:
            vals.add(Fraction(int(v), 1 << (k - 1)))
    allvals[k] = sorted(vals)
    pr(f"  k={k}: nonzero Inf_i(h) values = {[str(v) for v in allvals[k]]}")
    nz = B > 0
    pr(f"        min = {min(allvals[k]) if allvals[k] else None}, "
       f"max relevant coords = {int(nz.sum(axis=1).max())}")
allv = sorted(set().union(*allvals.values()))
pr(f"  union over k<=5: {[str(v) for v in allv]}")
pr(f"  ALL are multiples of 1/4 ? "
   f"{all((v*4).denominator == 1 for v in allv)}")
pr(f"  floor 1/4 respected (E3) ? {min(allv) >= Fraction(1,4)}")

hr("(3) CHEAP genuine patterns with k <= 5: all b_i < |P|/3  (all Inf_i(f_P) < 1/6)")
for k in (1, 2, 3, 4, 5):
    P = L[k]
    B = bvec(P, k)
    n = popcnt(P)
    genuine = np.all(B > 0, axis=1)
    cheap = np.all(B * 3 < n[:, None], axis=1) & genuine & (n > 0)
    idx = np.flatnonzero(cheap)
    pr(f"  k={k}: {len(idx)} cheap genuine patterns")
    dens = {}
    for j in idx:
        f = Fraction(int(n[j]), 1 << k)
        dens.setdefault(f, 0)
        dens[f] += 1
    for f in sorted(dens):
        pr(f"      density {f}: {dens[f]} patterns  "
           f"(complement cheap too? need b_i < (2^k-|P|)/3)")
    # which of them have their COMPLEMENT cheap as well (singleton pair < 1/6)
    both = np.all(B * 3 < np.minimum(n, (1 << k) - n)[:, None], axis=1) & genuine
    pr(f"      of these, {int(both.sum())} have a cheap complement "
       f"(=> singleton pair below 1/6)")
    if both.sum():
        for j in np.flatnonzero(both)[:5]:
            pr(f"        WITNESS mask={int(P[j])} |P|={int(n[j])} b={B[j].tolist()}")

hr("(4) exhaustive singleton-complement frontier Phi = max_i b_i/(2 min(|P|,2^k-|P|))")
best = None
for k in (1, 2, 3, 4, 5):
    P = L[k]
    B = bvec(P, k)
    n = popcnt(P)
    ok = (n > 0) & (n < (1 << k))
    mn = np.minimum(n, (1 << k) - n)
    with np.errstate(divide="ignore", invalid="ignore"):
        phi = B.max(axis=1) / (2.0 * mn)
    phi[~ok] = np.inf
    j = int(np.argmin(phi))
    v = Fraction(int(B[j].max()), 2 * int(mn[j]))
    pr(f"  k={k}: min Phi = {v} = {float(v):.5f}   witness mask={int(P[j])} "
       f"|P|={int(n[j])} b={B[j].tolist()}")
    if best is None or v < best[0]:
        best = (v, k, int(P[j]))
pr(f"  OVERALL k<=5: min Phi = {best[0]} at k={best[1]} (1/6 = 0.16667, "
   f"1/8 = 0.125 is the floor)")

pr(f"\nDONE r1a in {time.time()-t0:.1f}s")
