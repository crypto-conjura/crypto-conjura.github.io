"""
r1b_level6.py -- COMPLETE enumeration of the degree-<=3 class on a window of
SIX coordinates (the regime 0023-refuter-3 could not reach), and the exact
answers it settles:

  (a) |L(6,3)| = 16750860 patterns, enumerated explicitly as uint64 point-masks
      over the 64 points of the 6-cube.
  (b) max number of relevant coordinates of a degree-<=3 set at k=6
      (are there GENUINE 6-coordinate degree-3 sets at all?).
  (c) the exact value set of Inf_i(h) = b_i/2^5 (quantisation).
  (d) ALL CHEAP genuine patterns (every Inf_i(f_P) < 1/6) with their densities.
  (e) the exact singleton-complement frontier
        Phi(P) = max_i b_i / (2 min(|P|, 64-|P|))
      over the WHOLE level-6 class -- i.e. whether ANY degree-3 set with
      window <= 6 gives a singleton pair (A, A^c) below 1/6.
  (f) |L(7,3)| exactly, by the grouping identity (no enumeration).

Everything is integer arithmetic on bitmasks; influences are exact Fractions.
"""
import sys, time
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import (level3_all, next_level, coeffs, bvec, popcnt, group_by_key,
                  influences, influences_fourier, max_degree, flip_arrays)

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)

hr("(a) build L(6,3)")
L4 = next_level(level3_all(), 3)
L5 = next_level(L4, 4)
pr(f"  |L(4,3)|={len(L4)}  |L(5,3)|={len(L5)}   ({time.time()-t0:.1f}s)")
L6 = next_level(L5, 5)
pr(f"  |L(6,3)|={len(L6)}   ({time.time()-t0:.1f}s)  "
   f"mem {L6.nbytes/2**20:.0f} MiB")
assert len(np.unique(L6)) == len(L6), "duplicates in L6!"
pr("  masks are pairwise distinct (checked)")

# spot-check the degree of 200 random members by brute-force Walsh transform
rng = np.random.default_rng(12345)
sample = rng.choice(len(L6), 200, replace=False)
degs = [max_degree(int(L6[j]), 6) for j in sample]
pr(f"  brute-force degree check on 200 random members: max degree = {max(degs)}")
# and check that 200 random NON-members are indeed of degree > 3
cnt_bad = 0
seen = set(int(x) for x in L6[:0])  # not used; use searchsorted instead
L6s = np.sort(L6)
tries = 0
while tries < 200:
    m = int(rng.integers(0, 1 << 63))  # random 63-bit mask
    j = np.searchsorted(L6s, np.uint64(m))
    inl = j < len(L6s) and int(L6s[j]) == m
    if inl:
        continue
    tries += 1
    if max_degree(m, 6) <= 3:
        cnt_bad += 1
pr(f"  200 random masks OUTSIDE the list: how many actually have degree<=3? "
   f"{cnt_bad} (must be 0)")

hr("(b),(c) b-vectors, relevant counts, influence quantisation")
B = np.empty((len(L6), 6), dtype=np.int8)
fl = flip_arrays(6)
CH = 1 << 21
for a in range(0, len(L6), CH):
    B[a:a+CH] = bvec(L6[a:a+CH], 6, fl).astype(np.int8)
n = popcnt(L6).astype(np.int16)
pr(f"  b-vectors computed ({time.time()-t0:.1f}s)")
rel = (B > 0).sum(axis=1)
pr(f"  max relevant coordinates at k=6: {int(rel.max())}")
pr(f"  #genuine (relevant on all 6): {int((rel == 6).sum())}")
vals = sorted({Fraction(int(v), 32) for v in np.unique(B) if v})
pr(f"  nonzero Inf_i(h) values at k=6: {[str(v) for v in vals]}")
pr(f"  floor 1/4 = 8/32 respected? {min(vals) >= Fraction(1,4)}")
pr(f"  all multiples of 1/8 (b_i multiple of 4)? "
   f"{all((v*8).denominator == 1 for v in vals)}")

hr("(d) CHEAP genuine level-6 patterns: all b_i < |P|/3")
genuine = rel == 6
cheap = np.all(B.astype(np.int32) * 3 < n[:, None].astype(np.int32), axis=1) & genuine & (n > 0)
pr(f"  #cheap genuine = {int(cheap.sum())}")
idx = np.flatnonzero(cheap)
from collections import Counter
cc = Counter()
for j in idx:
    cc[(int(n[j]), int(B[j].max()))] += 1
for key in sorted(cc):
    pr(f"    |P|={key[0]} (density {Fraction(key[0],64)})  max b_i={key[1]}: "
       f"{cc[key]} patterns   -> max Inf_i(f_P) = {Fraction(key[1], 2*key[0])}")

hr("(e) EXACT singleton-complement frontier at k=6")
ok = (n > 0) & (n < 64)
mn = np.minimum(n, 64 - n).astype(np.int32)
num = B.max(axis=1).astype(np.int32)
# Phi = num / (2 mn); compare as rationals via cross multiplication against 1/6
below = ok & (num * 6 < 2 * mn)          # Phi < 1/6
eq = ok & (num * 6 == 2 * mn)
pr(f"  patterns with Phi < 1/6 : {int(below.sum())}")
pr(f"  patterns with Phi = 1/6 : {int(eq.sum())}")
with np.errstate(divide="ignore", invalid="ignore"):
    phi = np.where(ok, num / (2.0 * np.maximum(mn, 1)), np.inf)
j = int(np.argmin(phi))
v = Fraction(int(num[j]), 2 * int(mn[j]))
pr(f"  min Phi over the whole level-6 class = {v} = {float(v):.6f}")
pr(f"      witness mask={int(L6[j])} |P|={int(n[j])} b={B[j].tolist()}")
# the full bottom of the spectrum
order = np.argsort(phi)[:40]
spec = {}
for j in order:
    if not ok[j]:
        continue
    spec.setdefault(Fraction(int(num[j]), 2*int(mn[j])), 0)
    spec[Fraction(int(num[j]), 2*int(mn[j]))] += 1
pr(f"  smallest Phi values seen: {[str(x) for x in sorted(spec)][:6]}")
# exact count of each of the smallest few values
for target in [Fraction(1,8), Fraction(5,32), Fraction(1,6), Fraction(3,16),
               Fraction(1,5), Fraction(7,32), Fraction(1,4)]:
    c = int((ok & (num * target.denominator == 2 * mn * target.numerator)).sum())
    pr(f"    #patterns with Phi exactly {target}: {c}")

hr("(f) |L(7,3)| by the grouping identity")
g6 = group_by_key(L6, 6, sizes=(3,))
s6 = np.array([len(g) for g in g6], dtype=object)
pr(f"  #groups at k=6 = {len(g6)}, max group = {int(max(s6))}")
pr(f"  |L(7,3)| = {int((s6**2).sum())}")

np.save("L6.npy", L6)
np.save("L6_b.npy", B)
np.save("L6_n.npy", n)
pr(f"\nsaved L6.npy / L6_b.npy / L6_n.npy")
pr(f"DONE r1b in {time.time()-t0:.1f}s")
