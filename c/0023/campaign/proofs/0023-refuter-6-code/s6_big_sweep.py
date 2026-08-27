"""
s6 -- the two big sweeps, testing the conjecture that emerged from s4/s5:

      (R)   rho(A) := E_{x~Unif(A)}[ max codim of a prime implicant containing x ]
                   <=  2 deg(1_A) - 1     for every set A, 0 != A != cube.

  * complete class L(6,3): ALL 16750860 degree-<=3 sets on 6 coordinates;
  * random sample of the complete class L(7,3) (126113920 sets);
  * ALL 2^16 sets on 4 coordinates and ALL degree-<=2 sets on 6 coordinates
    were already swept in s4 -- rechecked here against (R).
Reports the maximum of rho, the maximum of rho - (2d-1), and every violation.
"""
import sys, time
import numpy as np
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from s4_helpers import analyse, prep, wht_deg
from fractions import Fraction as F


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


def next_level(cur, r0, d):
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


def sweep(masks, r, d, label, every=2_000_000):
    fl, order, popc = prep(r)
    full = (1 << (1 << r)) - 1
    best = None
    worst_slack = None
    viol = 0
    t0 = time.time()
    for c, Pm in enumerate(masks):
        P = int(Pm)
        if P == 0 or P == full:
            continue
        rho, Ns, Pi, mx = analyse(P, r, fl, order, popc)
        dd = wht_deg(P, r)
        if best is None or rho > best[0]:
            best = (rho, P, Ns, dd, mx)
        slack = rho - (2 * dd - 1)
        if worst_slack is None or slack > worst_slack[0]:
            worst_slack = (slack, P, dd, rho, Ns)
        if slack > 0:
            viol += 1
            if viol <= 5:
                print(f"   (R) VIOLATION: 0x{P:x} deg={dd} rho={rho} "
                      f"(> 2d-1 = {2*dd-1}) N_s={Ns}")
        if every and c and c % every == 0:
            print(f"   ... {c} swept ({time.time()-t0:.0f}s), best rho so far "
                  f"{best[0]}, violations {viol}")
    rho, P, Ns, dd, mx = best
    print(f" {label}: swept {c+1} masks in {time.time()-t0:.0f}s")
    print(f"   max rho = {rho} = {float(rho):.5f} at 0x{P:x} (deg {dd}, "
          f"2d-1 = {2*dd-1}, max PI codim {mx}, N_s={Ns})")
    sl, Pv, dv, rv, Nv = worst_slack
    print(f"   max [rho - (2d-1)] = {sl} = {float(sl):.5f} at 0x{Pv:x} "
          f"(deg {dv}, rho {rv})")
    print(f"   violations of (R): {viol}")


print("=" * 78)
print("complete class L(6,3): all degree-<=3 sets on 6 coordinates")
print("=" * 78)
cur = np.arange(1 << 8, dtype=np.uint64)
for r0 in (3, 4, 5):
    cur = next_level(cur, r0, 3)
print(f" |L(6,3)| = {len(cur)}")
sweep(cur, 6, 3, "L(6,3) EXHAUSTIVE", every=4_000_000)

print()
print("=" * 78)
print("random sample of the complete class L(7,3)")
print("=" * 78)
t0 = time.time()
L7 = next_level(cur, 6, 3)
print(f" |L(7,3)| = {len(L7)} (cross-check r1c.out: 126113920) "
      f"({time.time()-t0:.0f}s)")
rng = np.random.default_rng(7023)
NS = 600_000
idx = rng.choice(len(L7), size=NS, replace=False)
sweep(L7[idx], 7, 3, f"L(7,3) SAMPLE ({NS} of {len(L7)})", every=200_000)
