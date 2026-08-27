"""
x3_blocks.py -- COMPLETE pair sweeps by the block decomposition.

WHY THE BLOCK FORM IS FULLY GENERAL (no loss).  Put S = Rel(A) cap Rel(B).
A is a cylinder over Rel(A) = S u P_A and B over Rel(B) = S u P_B with
P_A cap P_B = empty; coordinates outside Rel(A) u Rel(B) are irrelevant to both
and change nothing (b_i and |A| scale together).  So EVERY cross-disjoint pair,
at every N, is a pair of the block form
        A on S u P_A,   B on S u P_B,   both genuine on all of S,
and (x2, L1) A cap B = empty is EQUIVALENT to the two S-shadows being disjoint.
Moreover
        pi_Rel = (1/2) [ sum_{i in S} r_i(A) + sum_{i in S} r_i(B) ]
SEPARATES: the A-side term depends on A alone.  Hence

  min pi_Rel over the whole product family {A} x {B}
     = (1/2) min_{Y_A cap Y_B = empty} [ mu_A(Y_A) + mu_B(Y_B) ],
     mu(Y) := min { sum_{i in S} r_i(A) : shadow_S(A) = Y, A genuine on S },

which turns a sweep of |{A}|*|{B}| pairs into a linear-time table computation.
The inner minimisation is done EXHAUSTIVELY over the stated class, and the
combination over disjoint shadows exactly (subset-min / zeta transform).

CLASSES SWEPT (per side, all sets, no sampling):
  (i)  ARBITRARY degree: every one of the 2^(2^k) subsets of a k-cube, k<=4.
       => complete over all cross-disjoint pairs, at ANY N, in which each side
          has at most 4 relevant coordinates (e.g. m=1,p=3: N=7).
  (ii) degree <= 3: the complete class L(k,3), k <= 6 (16 750 860 sets), built
       by the lib4 grouping recursion.
       => complete over all pairs of degree-<=3 sets, at ANY N, in which each
          side has at most 6 relevant coordinates.  Pair space swept for
          (m,p_A,p_B)=(1,5,5): (7.4e6)^2 ~ 5.5e13 pairs.
  (iii) degree <= 2: the same, filtered to vanishing level-3 coefficients.
"""
import sys, os, time
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "0023-refuter-4-code"))
from lib5 import popcount, bcounts, pi_rel, degree
from lib4 import level3_all, next_level, coeffs, flip_arrays as fl4

BIG = 1e18


def shadow_masks(k, m):
    """uint64 point-masks: index y in [0,2^m) -> all points whose first m bits
    equal y."""
    out = []
    for y in range(1 << m):
        w = 0
        for p in range(1 << k):
            if (p & ((1 << m) - 1)) == y:
                w |= 1 << p
        out.append(np.uint64(w))
    return out


def side_table(P, k, m, chunk=2_000_000):
    """mu(Y) for every shadow Y (array of size 2^(2^m)) over the given set
    family P (uint64 masks on the k-cube), S-block = coords 0..m-1.
    Also returns an argmin witness mask per shadow."""
    SH = shadow_masks(k, m)
    fl = fl4(k)
    NS = 1 << (1 << m)
    mu = np.full(NS, BIG)
    wit = np.zeros(NS, dtype=np.uint64)
    for s in range(0, len(P), chunk):
        Q = P[s:s + chunk]
        n = np.bitwise_count(Q).astype(np.int64)
        ok = n > 0
        sb = np.zeros(len(Q), dtype=np.int64)
        gen = np.ones(len(Q), dtype=bool)
        for i in range(m):
            Am, sh = fl[i]
            F = ((Q & Am) << sh) | ((Q >> sh) & Am)
            bi = np.bitwise_count(Q & ~F).astype(np.int64)
            sb += bi
            gen &= bi > 0
        sel = ok & gen
        if not sel.any():
            continue
        Q2, sb2, n2 = Q[sel], sb[sel], n[sel]
        shd = np.zeros(len(Q2), dtype=np.int64)
        for y in range(1 << m):
            shd |= ((Q2 & SH[y]) != 0).astype(np.int64) << y
        val = sb2 / n2
        # group-min with witness
        order = np.lexsort((val, shd))
        shd_o, val_o, Q_o = shd[order], val[order], Q2[order]
        first = np.ones(len(shd_o), dtype=bool)
        first[1:] = shd_o[1:] != shd_o[:-1]
        idx = np.flatnonzero(first)
        better = val_o[idx] < mu[shd_o[idx]]
        take = idx[better]
        mu[shd_o[take]] = val_o[take]
        wit[shd_o[take]] = Q_o[take]
    return mu, wit


def subset_min(mu, m):
    """h[w] = min over v subseteq w of mu[v]."""
    h = mu.copy()
    K = 1 << m
    ar = np.arange(len(h))
    for b in range(K):
        bit = 1 << b
        idx = np.flatnonzero((ar & bit) != 0)
        h[idx] = np.minimum(h[idx], h[idx ^ bit])
    return h


def combine(muA, witA, muB, witB, m):
    """min over disjoint shadows of muA[Y_A]+muB[Y_B]; exact witness pair."""
    K = 1 << m
    FULL = (1 << K) - 1
    hB = subset_min(muB, m)
    best, bY = BIG, None
    for Y in range(1, FULL + 1):
        if muA[Y] >= BIG:
            continue
        comp = FULL ^ Y
        if comp == 0 or hB[comp] >= BIG:
            continue
        v = muA[Y] + hB[comp]
        if v < best:
            best, bY = v, Y
    if bY is None:
        return None, None, None
    comp = FULL ^ bY
    # recover the B shadow attaining hB[comp]
    cand = [v for v in range(1, comp + 1) if (v & ~comp) == 0
            and muB[v] < BIG]
    vb = min(cand, key=lambda v: muB[v])
    return best, (bY, vb), (witA[bY], witB[vb])


def exact_pi(maskA, kA, maskB, kB, m):
    """exact Fraction pi_Rel for a block pair, from the definition, by
    materialising the pair on N = m + (kA-m) + (kB-m) coordinates."""
    pA, pB = kA - m, kB - m
    N = m + pA + pB
    # coordinate layout: 0..m-1 shared, m..m+pA-1 = A-private, then B-private
    A = 0
    for p in range(1 << N):
        ya = p & ((1 << (m + pA)) - 1)
        if (maskA >> ya) & 1:
            A |= 1 << p
    B = 0
    for p in range(1 << N):
        y = p & ((1 << m) - 1)
        z = (p >> (m + pA)) & ((1 << pB) - 1)
        if (maskB >> (y | (z << m))) & 1:
            B |= 1 << p
    return A, B, N


def report(name, muA, witA, kA, muB, witB, kB, m):
    best, Ys, wits = combine(muA, witA, muB, witB, m)
    if best is None:
        print(f"    {name}: no disjoint shadow pair (family empty)")
        return None
    pi = best / 2
    mA, mB = int(wits[0]), int(wits[1])
    A, B, N = exact_pi(mA, kA, mB, kB, m)
    exact, S = pi_rel(A, B, N)
    ok = "OK" if abs(float(exact) - pi) < 1e-9 else "MISMATCH"
    print(f"    {name}: min pi_Rel = {exact} = {float(exact):.9f}  [{ok}]"
          f"  shadows {Ys}  |S|={len(S)}  N={N}"
          f"  deg(1_A)={degree(A,N)} deg(1_B)={degree(B,N)}"
          f"  |A|={popcount(A)} |B|={popcount(B)}")
    return exact


def all_sets(k):
    return np.arange(1 << (1 << k), dtype=np.uint64)


def deg3_class(k):
    P = level3_all()
    for kk in range(3, k):
        P = next_level(P, kk)
    return P


def deg2_filter(P, k):
    C = coeffs(P, k, sizes=(3,))
    return P[(C == 0).all(axis=1)]


if __name__ == "__main__":
    print("=" * 74)
    print("(i) ARBITRARY DEGREE, each side <= 4 relevant coordinates")
    print("    complete over every cross-disjoint pair with |Rel| <= 4 per")
    print("    side, at every N")
    print("=" * 74)
    tabs = {}
    for m in (1, 2, 3, 4):
        for k in range(m, 5):
            t0 = time.time()
            mu, wit = side_table(all_sets(k), k, m)
            tabs[(m, k)] = (mu, wit)
            nz = int(np.count_nonzero(mu < BIG))
            print(f"  m={m} k={k}: {1<<(1<<k)} sets, {nz} realisable shadows"
                  f"  ({time.time()-t0:.1f}s)")
    print()
    overall = None
    for m in (1, 2, 3, 4):
        for kA in range(m, 5):
            for kB in range(kA, 5):
                muA, witA = tabs[(m, kA)]
                muB, witB = tabs[(m, kB)]
                v = report(f"m={m} p_A={kA-m} p_B={kB-m}",
                           muA, witA, kA, muB, witB, kB, m)
                if v is not None and (overall is None or v < overall):
                    overall = v
    print(f"  ==> min over (i) = {overall} = {float(overall):.9f}")

    print()
    print("=" * 74)
    print("(ii)/(iii) degree <= 3 and degree <= 2 classes, each side <= 6")
    print("    relevant coordinates (complete classes L(k,3), k<=6)")
    print("=" * 74)
    for d in (3, 2):
        tabs = {}
        for k in range(1, 7):
            P = deg3_class(k) if k >= 3 else all_sets(k)
            if d == 2:
                P = deg2_filter(P, k) if k >= 3 else P
            for m in range(1, min(k, 4) + 1):
                t0 = time.time()
                mu, wit = side_table(P, k, m)
                tabs[(m, k)] = (mu, wit)
            print(f"  d<={d} k={k}: |class| = {len(P)}"
                  f"   ({time.time()-t0:.1f}s for the last m)")
        print()
        overall = None
        for m in (1, 2, 3, 4):
            for kA in range(m, 7):
                for kB in range(kA, 7):
                    if (m, kA) not in tabs or (m, kB) not in tabs:
                        continue
                    muA, witA = tabs[(m, kA)]
                    muB, witB = tabs[(m, kB)]
                    v = report(f"d<={d} m={m} p_A={kA-m} p_B={kB-m}",
                               muA, witA, kA, muB, witB, kB, m)
                    if v is not None and (overall is None or v < overall):
                        overall = v
        print(f"  ==> min over degree <= {d} = {overall} = "
              f"{float(overall):.9f}")
    print("DONE x3")
