"""
s4 -- SEARCH beyond the two witnesses (part 3 of the question).

REDUCTION USED (proved in the artifact, §Search):
  * A minimal certificate of a point of A is exactly a PRIME IMPLICANT of A
    (a maximal subcube contained in A); the minimal certificates of x are the
    prime implicants containing x.
  * For ANY nonempty A != cube with deg(1_A) <= d, the pair (A, A^c) is in
    P_d (both sides degree <= d, disjoint, nonempty).  So a degree-<=d set A
    with E_{x~Unif(A)}[max prime-implicant codim] = 2^{Omega(d)} immediately
    gives a CAP-I(b) witness that kills the unrestricted-minimal variant of P5
    (numerator pi <= pi_Rel <= 2d always, denominator exponential).
  Hence the search space is: ALL degree-<=d sets, and the objective is
        rho(A) := E_{x~Unif(A)} [ max codim of a prime implicant containing x ].

Per set this script computes, exactly (integers only):
    rho(A) as a Fraction; the prime-implicant profile N_s (number of PIs of
    codim s); the PI mass Pi(A) = sum_s N_s 2^-s = E_{x~cube}[#PIs containing x];
    and max_s (log2 N_s - s + d), the quantity that must be >> 0 at
    exponentially large s for a counterexample to exist.

COVERAGE
  (A) ALL 2^16 sets on r = 4 coordinates (every degree).
  (B) ALL degree-<=3 sets on r = 5: the complete class L(5,3), 807980 sets
      (count cross-checks ../0023-refuter-4-code/r1a.out).
  (C) ALL degree-<=2 sets on r = 5, 6.
  (D) random sample of the complete class L(6,3) (16750860 sets) -- sample, not
      exhaustive; size stated in the output.
"""
import sys, time, random
import numpy as np
from fractions import Fraction as F
from math import log2

sys.path.insert(0, __file__.rsplit("/", 1)[0])

# ------------------------------------------------------------------ bit helpers

def flip_masks(r):
    out = []
    for i in range(r):
        s = 1 << i
        A = 0
        for m in range(1 << r):
            if not ((m >> i) & 1):
                A |= 1 << m
        out.append((A, s))
    return out


def analyse(P, r, fl, order, popc):
    """P: python-int bitmask over the 2^r points.  Returns
       (rho as Fraction, {s: N_s}, Pi as Fraction, maxcodim)."""
    n = 1 << r
    full = n - 1
    cert = {full: P}
    for S in order:                       # decreasing popcount, S != full
        i = (~S & full).bit_length() - 1
        S2 = S | (1 << i)
        c = cert[S2]
        Ai, si = fl[i]
        c2 = ((c & Ai) << si) | ((c >> si) & Ai)
        cert[S] = c & c2
    Z = [0] * (r + 1)
    Ns = {}
    mass = 0
    for S in range(n):
        c = cert[S]
        if not c:
            continue
        mn = c
        Sb = S
        i = 0
        while Sb:
            if Sb & 1:
                mn &= ~cert[S ^ (1 << i)]
                if not mn:
                    break
            Sb >>= 1
            i += 1
        if not mn:
            continue
        s = popc[S]
        Z[s] |= mn
        pc = bin(mn).count("1")
        mass += pc
        Ns[s] = Ns.get(s, 0) + pc // (1 << (r - s))
    # suffix ORs -> sum over points of the max codim
    tot = 0
    suf = 0
    maxcod = 0
    for s in range(r, 0, -1):
        suf |= Z[s]
        if Z[s]:
            maxcod = max(maxcod, s)
        tot += bin(suf).count("1")
    npts = bin(P).count("1")
    return F(tot, npts), Ns, F(mass, 1 << r), maxcod


def wht_deg(P, r):
    tt = [(P >> m) & 1 for m in range(1 << r)]
    v = tt
    h = 1
    while h < len(v):
        for i in range(0, len(v), h * 2):
            for j in range(i, i + h):
                x, y = v[j], v[j + h]
                v[j], v[j + h] = x + y, x - y
        h *= 2
    deg = 0
    for S, c in enumerate(v):
        if c:
            deg = max(deg, bin(S).count("1"))
    return deg


def prep(r):
    fl = flip_masks(r)
    n = 1 << r
    order = sorted((S for S in range(n - 1)), key=lambda S: -bin(S).count("1"))
    popc = [bin(S).count("1") for S in range(n)]
    return fl, order, popc


# ----------------------------------------------------------- (A) all sets, r=4
print("=" * 78)
print("(A) EXHAUSTIVE: all 2^(2^r) sets on r = 3, 4 coordinates, every degree")
print("=" * 78)
for r in (3, 4):
    fl, order, popc = prep(r)
    best = {}
    t0 = time.time()
    for P in range(1, (1 << (1 << r)) - 1):     # nonempty, not the full cube
        d = wht_deg(P, r)
        rho, Ns, Pi, mx = analyse(P, r, fl, order, popc)
        cur = best.get(d)
        key = (rho, mx)
        if cur is None or key > cur[0]:
            best[d] = (key, P, Ns, Pi)
    print(f" r={r} ({time.time()-t0:.1f}s):")
    for d in sorted(best):
        (rho, mx), P, Ns, Pi = best[d]
        print(f"   d={d}: max rho = {rho} = {float(rho):.4f}  (d={d}, "
              f"2^(d-1)={1<<max(0,d-1)}), max PI codim at the argmax = {mx}, "
              f"N_s={Ns}, PI mass={Pi}, argmax mask=0x{P:0{1<<(r-2)}x}")

# --------------------------------------------- degree-filtered enumeration L(r,d)

def coeff_level(Pmasks, r, lvl):
    """integer Walsh coefficients at exactly level lvl, vectorised over an
    array of uint64 masks (r <= 6 so 2^r <= 64 bits)."""
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


def enumerate_L(r, d):
    """ALL masks P on r coordinates with deg(1_P) <= d.  Level-by-level:
    deg <= d on r+1 coords iff both halves have deg <= d and their
    level-exactly-d coefficients agree."""
    cur = np.arange(1 << (1 << d), dtype=np.uint64)      # r0 = d: all patterns
    r0 = d
    while r0 < r:
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
        cur = np.concatenate(chunks)
        r0 += 1
    return cur


print()
print("=" * 78)
print("(B),(C) EXHAUSTIVE degree-filtered classes")
print("=" * 78)
for (r, d) in ((4, 3), (5, 2), (6, 2), (5, 3)):
    t0 = time.time()
    L = enumerate_L(r, d)
    print(f" |L({r},{d})| = {len(L)}  (built {time.time()-t0:.1f}s)")
    if len(L) > 3_000_000:
        print("   too large for the per-set sweep here; see (D)")
        continue
    fl, order, popc = prep(r)
    t0 = time.time()
    bestrho = None
    bestmx = None
    worst_gap = None
    seen_deg = set()
    for Pm in L:
        P = int(Pm)
        if P == 0 or P == (1 << (1 << r)) - 1:
            continue
        rho, Ns, Pi, mx = analyse(P, r, fl, order, popc)
        if bestrho is None or rho > bestrho[0]:
            bestrho = (rho, P, Ns, Pi, mx)
        if bestmx is None or mx > bestmx[0]:
            bestmx = (mx, P, Ns, Pi, rho)
        g = max(log2(N) - s for s, N in Ns.items())
        if worst_gap is None or g > worst_gap[0]:
            worst_gap = (g, P, Ns)
    rho, P, Ns, Pi, mx = bestrho
    print(f"   swept {len(L)} sets ({time.time()-t0:.1f}s)")
    print(f"   max rho = {rho} = {float(rho):.5f}   (d={d}: poly ref d={d}, "
          f"d^2={d*d}; exp ref 2^(d-1)={1<<(d-1)}) at mask 0x{P:x}, "
          f"N_s={Ns}, PI mass={Pi}, max PI codim {mx}")
    mx2, P2, Ns2, Pi2, rho2 = bestmx
    print(f"   max PI codim over the class = {mx2} at mask 0x{P2:x} "
          f"(its rho = {rho2} = {float(rho2):.5f}, N_s={Ns2})")
    g, Pg, Nsg = worst_gap
    print(f"   max_s [log2 N_s - s] = {g:.4f} (needs to exceed -d = {-d} at "
          f"exponentially large s for a blow-up) at mask 0x{Pg:x}, N_s={Nsg}")

# ------------------------------------------------------- (D) sample of L(6,3)
print()
print("=" * 78)
print("(D) RANDOM SAMPLE of the complete degree-<=3 class on r = 6")
print("=" * 78)
t0 = time.time()
L = enumerate_L(6, 3)
print(f" |L(6,3)| = {len(L)} (cross-check r1a.out: 16750860) ({time.time()-t0:.1f}s)")
rng = np.random.default_rng(6023)
NS = 400_000
idx = rng.choice(len(L), size=NS, replace=False)
fl, order, popc = prep(6)
t0 = time.time()
bestrho = None
bestmx = None
for j in idx:
    P = int(L[j])
    if P == 0 or P == (1 << 64) - 1:
        continue
    rho, Ns, Pi, mx = analyse(P, 6, fl, order, popc)
    if bestrho is None or rho > bestrho[0]:
        bestrho = (rho, P, Ns, Pi, mx)
    if bestmx is None or mx > bestmx[0]:
        bestmx = (mx, P, Ns, Pi, rho)
print(f" sampled {NS} of {len(L)} ({100*NS/len(L):.2f}%) in {time.time()-t0:.1f}s")
rho, P, Ns, Pi, mx = bestrho
print(f" max rho in the sample = {rho} = {float(rho):.5f} at mask 0x{P:016x}, "
      f"N_s={Ns}, PI mass={Pi}, max PI codim {mx}   (d=3: 2^(d-1)=4)")
mx2, P2, Ns2, Pi2, rho2 = bestmx
print(f" max PI codim in the sample = {mx2} at 0x{P2:016x} (rho={float(rho2):.5f}, "
      f"N_s={Ns2})")
