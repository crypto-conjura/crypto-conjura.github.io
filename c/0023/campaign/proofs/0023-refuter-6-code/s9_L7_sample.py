"""
s9 -- CORRECT uniform sample of the complete degree-<=3 class L(7,3).

ERRATUM this file repairs: the second block of s6_big_sweep.py built the r=7
level with `np.uint64 << 64`, which is 0 in numpy, so the "L(7,3) sample" there
was really a sample of the family { x_7 = +1 } x P, P in L(6,3) -- a legitimate
set of degree-<=4 sets on 7 coordinates (and (R) held on all 600000 of them,
max rho = 6 <= 2d-1 = 7), but NOT L(7,3).  Here the r=7 level is sampled
correctly, with python-int masks:

  L(7,3) = { g | (h << 64) : g,h in L(6,3), same level-exactly-3 coefficients },
so sampling a coefficient group with probability |group|^2 / sum |group|^2 and
then g,h uniformly inside it is exactly uniform on L(7,3).  The normalisation
sum |group|^2 = 126113920 reproduces |L(7,3)| from
../0023-refuter-4-code/r1c.out, which certifies the grouping.
"""
import sys, time
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from s4_helpers import analyse, prep, wht_deg


def coeff_level(Pmasks, r, lvl):
    Pm = np.asarray(Pmasks, dtype=np.uint64)
    cols = []
    for S in range(1 << r):
        if bin(S).count("1") != lvl:
            continue
        ev = od = 0
        for m in range(1 << r):
            if bin(S & m).count("1") & 1:
                od |= 1 << m
            else:
                ev |= 1 << m
        cols.append((np.uint64(ev), np.uint64(od)))
    out = np.empty((len(Pm), len(cols)), dtype=np.int64)
    for j, (ev, od) in enumerate(cols):
        out[:, j] = (np.bitwise_count(Pm & ev).astype(np.int64)
                     - np.bitwise_count(Pm & od).astype(np.int64))
    return out


def next_level_u64(cur, r0, d):
    C = coeff_level(cur, r0, d)
    o = np.lexsort(C.T[::-1])
    Cs, Ps = C[o], cur[o]
    new = np.ones(len(Cs), dtype=bool)
    new[1:] = np.any(Cs[1:] != Cs[:-1], axis=1)
    starts = np.flatnonzero(new)
    ends = np.append(starts[1:], len(Cs))
    shift = np.uint64(1 << r0)
    chunks = []
    for a, b in zip(starts, ends):
        blk = Ps[a:b]
        mm = len(blk)
        chunks.append(np.repeat(blk, mm) | (np.tile(blk, mm) << shift))
    return np.concatenate(chunks)


t0 = time.time()
cur = np.arange(1 << 8, dtype=np.uint64)
for r0 in (3, 4, 5):
    cur = next_level_u64(cur, r0, 3)
print(f"|L(6,3)| = {len(cur)} ({time.time()-t0:.0f}s)")

# groups of L(6,3) by the 20 level-exactly-3 coefficients
C = coeff_level(cur, 6, 3)
o = np.lexsort(C.T[::-1])
Cs, Ps = C[o], cur[o]
new = np.ones(len(Cs), dtype=bool)
new[1:] = np.any(Cs[1:] != Cs[:-1], axis=1)
starts = np.flatnonzero(new)
ends = np.append(starts[1:], len(Cs))
sizes = (ends - starts).astype(np.int64)
tot7 = int((sizes.astype(object) ** 2).sum())
print(f"#groups = {len(sizes)}, sum |group|^2 = {tot7} "
      f"(|L(7,3)| from r1c.out: 126113920, match: {tot7 == 126113920})")

rng = np.random.default_rng(9_0023)
w = (sizes.astype(np.float64) ** 2)
w /= w.sum()
NS = int(__import__('os').environ.get('NS','300000'))
gidx = rng.choice(len(sizes), size=NS, p=w)
fl, order, popc = prep(7)
best = None
viol = 0
t0 = time.time()
for c, gi in enumerate(gidx):
    a, b = starts[gi], ends[gi]
    blk = Ps[a:b]
    g = int(blk[rng.integers(len(blk))])
    h = int(blk[rng.integers(len(blk))])
    P = g | (h << 64)
    if P == 0 or P == (1 << 128) - 1:
        continue
    rho, Ns, Pi, mx = analyse(P, 7, fl, order, popc)
    dd = wht_deg(P, 7)
    assert dd <= 3, (hex(P), dd)
    if best is None or rho > best[0]:
        best = (rho, P, Ns, dd, mx)
    if rho > 2 * dd - 1:
        viol += 1
        if viol <= 5:
            print(f"  (R) VIOLATION 0x{P:x} deg={dd} rho={rho} N_s={Ns}")
    if c and c % 100_000 == 0:
        print(f"  ... {c} sampled ({time.time()-t0:.0f}s), best rho {best[0]}, "
              f"violations {viol}")
rho, P, Ns, dd, mx = best
print(f"L(7,3) uniform sample of {NS} of {tot7}: {time.time()-t0:.0f}s")
print(f"  max rho = {rho} = {float(rho):.5f} at 0x{P:x} (deg {dd}, 2d-1 = "
      f"{2*dd-1}, max PI codim {mx}, N_s={Ns})")
print(f"  violations of (R) rho <= 2 deg - 1: {viol}")
