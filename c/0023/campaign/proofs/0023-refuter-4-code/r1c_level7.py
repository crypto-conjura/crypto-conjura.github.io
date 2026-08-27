"""
r1c_level7.py -- COMPLETE pass over the degree-<=3 class on a window of SEVEN
coordinates: |L(7,3)| = 126113920 patterns, enumerated implicitly as ordered
pairs (g,h) of level-6 patterns sharing their degree-exactly-3 Walsh
coefficients (fact (E2) of lib4).  A level-7 pattern is the pair
P = g  u  (h shifted by 64 points), and

     b_i(P) = b_i(g) + b_i(h)   (i < 6),      b_6(P) = |g XOR h| ,
     |P|    = |g| + |h| .

Both summands are already tabulated in L6_b.npy / L6_n.npy, so the whole level
is swept with integer adds and one popcount per pair.

SETTLES
  * the maximum number of relevant coordinates of a degree-<=3 set at k=7
    (i.e. whether the class has any genuine 7-junta at all -> whether window 6
    is the top of the class);
  * every CHEAP genuine level-7 pattern (all Inf_i(f_P) < 1/6);
  * the exact singleton-complement frontier
    Phi = max_i b_i / (2 min(|P|,128-|P|)) at k=7;
  * the value set of Inf_i(h) = b_i/2^6 at k=7 (quantisation check).
"""
import sys, time
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import coeffs, popcnt

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

L6 = np.load("L6.npy")
B6 = np.load("L6_b.npy").astype(np.int16)
N6 = np.load("L6_n.npy").astype(np.int16)
pr(f"loaded L6: {len(L6)} patterns ({time.time()-t0:.1f}s)")

hr("group level 6 by the 20 degree-exactly-3 Walsh coefficients")
C = np.empty((len(L6), 20), dtype=np.int8)
CH = 1 << 21
for a in range(0, len(L6), CH):
    C[a:a+CH] = coeffs(L6[a:a+CH], 6, sizes=(3,)).astype(np.int8)
pr(f"  coefficients computed ({time.time()-t0:.1f}s)")
perm = np.lexsort(C.T[::-1])
Cs = C[perm]
newrow = np.ones(len(Cs), dtype=bool)
newrow[1:] = np.any(Cs[1:] != Cs[:-1], axis=1)
starts = np.flatnonzero(newrow).astype(np.int64)
sizes = np.diff(np.append(starts, len(Cs))).astype(np.int64)
del C, Cs
pr(f"  #groups = {len(starts)}, max size {sizes.max()} ({time.time()-t0:.1f}s)")
sq = sizes.astype(np.int64) ** 2
tot = int(sq.sum())
pr(f"  total level-7 patterns = {tot}")
cum = np.concatenate([[0], np.cumsum(sq)])

# reorder the tables so group members are contiguous
L6p, B6p, N6p = L6[perm], B6[perm], N6[perm]
del L6, B6, N6, perm

hr("sweep all 126113920 level-7 patterns")
maxrel = 0
genuine_cnt = 0
bvals = set()
cheap_masks = []          # (lo, hi) of cheap genuine level-7 patterns
best_phi = None
phi_below = phi_eq = 0
CHUNK = 1 << 23
done = 0
while done < tot:
    hi_t = min(tot, done + CHUNK)
    t = np.arange(done, hi_t, dtype=np.int64)
    gidx = np.searchsorted(cum, t, side="right") - 1
    r = t - cum[gidx]
    m = sizes[gidx]
    a = starts[gidx] + r // m
    b = starts[gidx] + r % m
    B = np.empty((len(t), 7), dtype=np.int16)
    B[:, :6] = B6p[a] + B6p[b]
    B[:, 6] = np.bitwise_count(L6p[a] ^ L6p[b]).astype(np.int16)
    n = (N6p[a] + N6p[b]).astype(np.int32)
    rel = (B > 0).sum(axis=1)
    maxrel = max(maxrel, int(rel.max()))
    gen = rel == 7
    genuine_cnt += int(gen.sum())
    bvals |= set(int(v) for v in np.unique(B) if v)
    ok = (n > 0) & (n < 128)
    cheap = np.all(B.astype(np.int32) * 3 < n[:, None], axis=1) & gen
    if cheap.any():
        for j in np.flatnonzero(cheap):
            cheap_masks.append((int(L6p[a[j]]), int(L6p[b[j]]),
                                int(n[j]), B[j].tolist()))
    mn = np.minimum(n, 128 - n)
    num = B.max(axis=1).astype(np.int32)
    phi_below += int((ok & (num * 6 < 2 * mn)).sum())
    phi_eq += int((ok & (num * 6 == 2 * mn)).sum())
    v = np.where(ok, num / (2.0 * np.maximum(mn, 1)), np.inf)
    j = int(np.argmin(v))
    cand = (float(v[j]), Fraction(int(num[j]), 2 * int(mn[j])),
            int(L6p[a[j]]), int(L6p[b[j]]), int(n[j]), B[j].tolist())
    if best_phi is None or cand[0] < best_phi[0]:
        best_phi = cand
    done = hi_t
    if (done // CHUNK) % 4 == 0:
        pr(f"  ... {done}/{tot} ({time.time()-t0:.1f}s)  maxrel={maxrel} "
           f"genuine={genuine_cnt} bestPhi={best_phi[1]}")

hr("RESULTS at k = 7")
pr(f"  max relevant coordinates = {maxrel}")
pr(f"  #genuine (relevant on all 7) = {genuine_cnt}")
pr(f"  b_i values seen: {sorted(bvals)}")
pr(f"  => Inf_i(h) values: "
   f"{[str(Fraction(v,64)) for v in sorted(bvals)]}")
pr(f"  #patterns with Phi < 1/6 : {phi_below}")
pr(f"  #patterns with Phi = 1/6 : {phi_eq}")
pr(f"  min Phi = {best_phi[1]} = {best_phi[0]:.6f}  "
   f"(lo={best_phi[2]}, hi={best_phi[3]}, |P|={best_phi[4]}, b={best_phi[5]})")
pr(f"  #cheap genuine level-7 patterns = {len(cheap_masks)}")
for c in cheap_masks[:10]:
    pr(f"     lo={c[0]} hi={c[1]} |P|={c[2]} b={c[3]}")
pr(f"\nDONE r1c in {time.time()-t0:.1f}s")
