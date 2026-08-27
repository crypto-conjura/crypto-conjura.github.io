"""
r7_checks.py -- closing checks.

 (1) FORCING vs WINDOW.  A degree-<=3 set that forces t coordinates has
     1_A = prod_{j<=t}(1 +- x_{c_j})/2 * h with deg h <= 3-t, so its window is
     at most t + w_max(3-t) = 5, 3, 3 for t = 1, 2, 3.  Checked exhaustively
     against the complete level-6 class: no genuine 6-coordinate degree-3 set
     forces anything.
 (2) The window-5 forcing witness and the resulting EXACT CAP on every
     count/payment argument:  rho* := min over disjoint pairs of
     pi(f,g)/(|J|+|K|), where pi = sum_{i in J cap K}[Inf_i f + Inf_i g].
     Any proof of the shape "pi >= c(|J|+|K|) for all disjoint pairs, then
     average" yields at best delta >= rho*.  Exhibits rho* <= 1/10.
 (3) The universal payment inequality pi >= 1 (R1's (F4), valid for arbitrary
     sets) re-checked on 200000 random disjoint pairs of the level-6 class, plus
     the minimum of pi over those pairs.
 (4) min total influence T = sum_i Inf_i(f_P) per window size, and the density
     spectrum of the class (which sets are cheap).
"""
import sys, time, random, itertools
import numpy as np
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib4 import bvec, popcnt, influences, influences_fourier

t0 = time.time()
def pr(*a):
    print(*a, flush=True)
def hr(t):
    pr("\n" + "=" * 72); pr(t); pr("=" * 72)
rng = np.random.default_rng(97531)

L6 = np.load("L6.npy"); B6 = np.load("L6_b.npy").astype(np.int32)
N6 = np.load("L6_n.npy").astype(np.int32)
gen6 = np.all(B6 > 0, axis=1)

hr("(1) forcing and window size")
# P forces coordinate i iff all points of P agree on bit i.
force = np.zeros((len(L6), 6), dtype=bool)
for i in range(6):
    A = np.uint64(0)                       # points with bit i = 0
    for m in range(64):
        if not ((m >> i) & 1):
            A |= np.uint64(1) << np.uint64(m)
    lo = (L6 & A) == np.uint64(0)           # no point with bit i = 0
    hi = (L6 & ~A) == np.uint64(0)          # no point with bit i = 1
    force[:, i] = (lo | hi) & (N6 > 0)
nf = force.sum(axis=1)
pr(f"  max #forced coordinates over the whole level-6 class: {int(nf.max())} "
   f"(must be <= 3)")
pr(f"  genuine 6-coordinate sets that force at least one coordinate: "
   f"{int((gen6 & (nf > 0)).sum())}   (0 confirms window <= 5 for forcing sets)")
for t in (1, 2, 3):
    sel = (nf == t) & (N6 > 0)
    if sel.any():
        wmax = int((B6[sel] > 0).sum(axis=1).max())
        pr(f"  sets forcing exactly {t} coordinate(s): {int(sel.sum())}, "
           f"largest window {wmax} (bound {t + [0,1,4,7][3-t] if 3-t<=3 else 0})")

hr("(2) the count/payment cap rho*: an exact 1/10 pair")
# window-5 forcing set: A = {x_0 = +1} cap C where C is the degree-2 4-cycle on
# coordinates 1..4.  Pattern over the window (0,1,2,3,4), bit b = coordinate b.
def four_cycle_pattern():
    """the 24 signed 4-cycles are 1_C = 1/2 + (s1 x1x2 + s2 x2x3 + s3 x3x4 +
    s4 x4x1)/4 with prod s = -1; take s = (+,+,+,-)."""
    P = set()
    for m in range(16):
        x = [1 - 2 * ((m >> b) & 1) for b in range(4)]
        v = Fraction(1, 2) + Fraction(x[0]*x[1] + x[1]*x[2] + x[2]*x[3]
                                      - x[3]*x[0], 4)
        assert v in (0, 1), v
        if v == 1:
            P.add(m)
    return P
C = four_cycle_pattern()
pr(f"  4-cycle degree-2 set: |C| = {len(C)} of 16")
# A on window (0,1,2,3,4): bit0 = x_0, must be 0 (=+1); bits1..4 carry C
PA = {(m << 1) | 0 for m in C}
maskA = 0
for m in PA:
    maskA |= 1 << m
pr(f"  A = {{x_0=+1}} cap C: |P_A| = {len(PA)}, influences = "
   f"{[str(x) for x in influences(maskA, 5)]}")
pr(f"     Fourier-definition influences = "
   f"{[str(x) for x in influences_fourier(maskA, 5)]}")
IA = influences(maskA, 5)
# B: same shape but forcing x_0 = -1, on window (0,5,6,7,8)
PB = {(m << 1) | 1 for m in C}
maskB = 0
for m in PB:
    maskB |= 1 << m
IB = influences(maskB, 5)
pr(f"  B = {{x_0=-1}} cap C' : influences = {[str(x) for x in IB]}")
pr(f"  shared window = {{x_0}}; projections {{+1}} and {{-1}} are disjoint "
   f"=> A cap B = empty (F2)")
pi = IA[0] + IB[0]
pr(f"  payment pi = Inf_0(A)+Inf_0(B) = {pi};  |J|+|K| = 10; "
   f"ratio = {pi/10} = {float(pi/10):.4f}")
pr(f"  => rho* <= {pi/10} < 1/8 (0023-refuter-3's sampled bound) < 1/6.")
pr(f"     Every payment-count proof of the rung is capped at rho*, so no such")
pr(f"     proof can reach 1/6 at d=3 -- but rho* is NOT attainable by a design")
pr(f"     (both sides would have to force the SAME single coordinate, making it")
pr(f"     a hub of average influence 1/2).")

hr("(3) the universal payment inequality pi >= 1 on random disjoint pairs")
idx = np.flatnonzero(gen6)
tries = 0; found = 0; worst = None
while found < 200000 and tries < 4000000:
    a, b = rng.choice(idx, 2, replace=False)
    tries += 1
    if int(L6[a]) & int(L6[b]):
        continue
    found += 1
    ja = [i for i in range(6) if B6[a, i] > 0]
    jb = [i for i in range(6) if B6[b, i] > 0]
    S = set(ja) & set(jb)
    p = sum(Fraction(int(B6[a, i]), 2 * int(N6[a])) for i in S) + \
        sum(Fraction(int(B6[b, i]), 2 * int(N6[b])) for i in S)
    if worst is None or p < worst[0]:
        worst = (p, int(L6[a]), int(L6[b]), sorted(S))
pr(f"  {found} disjoint pairs of GENUINE window-6 sets sampled "
   f"({tries} draws); min payment pi = {worst[0]} = {float(worst[0]):.4f}")
pr(f"  pi >= 1 held on every sampled pair: {worst[0] >= 1}")
pr(f"  minimum ratio pi/(|J|+|K|) on these (both windows 6): "
   f"{worst[0]/12} = {float(worst[0]/12):.4f}")

hr("(4) min total influence T and cheapness by window")
for w, arr in (("<=6 genuine", idx),):
    T = B6[arr].sum(axis=1) / (2.0 * N6[arr])
    j = arr[int(np.argmin(T))]
    pr(f"  window-6 genuine: min T = {Fraction(int(B6[j].sum()), 2*int(N6[j]))}"
       f" (|P|={int(N6[j])}, b={B6[j].tolist()}), max T = {T.max():.4f}")
cheap = gen6 & np.all(B6 * 3 < N6[:, None], axis=1)
dens = {}
for j in np.flatnonzero(cheap):
    dens[Fraction(int(N6[j]), 64)] = dens.get(Fraction(int(N6[j]), 64), 0) + 1
pr(f"  cheap genuine window-6 sets by density: {dens}")
pr(f"  every cheap set has density > 3/8: {all(k > Fraction(3,8) for k in dens)}")
pr(f"\nDONE r7 in {time.time()-t0:.1f}s")
