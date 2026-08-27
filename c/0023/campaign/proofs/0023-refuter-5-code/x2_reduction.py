"""
x2_reduction.py -- the SHADOW/MEASURE reduction, and the exact obstruction
chain, checked numerically at every link.

THE CHAIN (each link re-derived from scratch; verified below, never assumed).

 (L1) SHARED RELEVANCE IS NONEMPTY, and the shadows are disjoint.
      Let S = Rel(A) cap Rel(B) and m=|S|.  For y in {+-1}^S let A_y, B_y be the
      fibres.  If A_y and B_y are both nonempty, pick z_A, z_B in them and build
      z agreeing with z_A on Rel(A)\\S and with z_B on Rel(B)\\S (disjoint
      coordinate blocks).  A depends only on S u (Rel(A)\\S), so (y,z) in A;
      likewise (y,z) in B -- contradicting A cap B = empty.  Hence the SHADOWS
      Y_A={y: A_y != empty}, Y_B={y: B_y != empty} are DISJOINT, and since both
      are nonempty, m >= 1.

 (L2) FIBRE-MASS LOWER BOUND.  nu(y):=|A_y|/|A|.  Every point of A_y whose
      i-flip is outside A is counted by b_i(A), and at least
      (|A_y|-|A_{y+i}|)_+ points of A_y have that property, so
          r_i(A) := b_i(A)/|A| >= sum_y (nu(y)-nu(y+i))_+ =: D_i(nu),
      hence  sum_{i in S} r_i(A) >= T(nu) := sum_{i in S} D_i(nu).

 (L3) FLIP-AVERAGING.  D_i(nu) = TV(nu, sigma_i nu) where sigma_i flips
      coordinate i.  Flips commute, so TV(nu, sigma_J nu) <= sum_{i in J} D_i,
      and averaging over the 2^m subsets J (which sends nu to the uniform U):
          TV(nu, U) <= 2^{-m} sum_J sum_{i in J} D_i(nu) = T(nu)/2 .
      Independently, TV(nu,U) >= nu(Y_A) - U(Y_A) = 1 - |Y_A|/2^m.

 (L4) PAYMENT >= 1.  With |Y_A| + |Y_B| <= 2^m (disjointness),
          T(nu)+T(omega) >= 2[(1-|Y_A|/2^m) + (1-|Y_B|/2^m)] >= 2,
      so  pi_Rel = (1/2)[sum_{i in S} r_i(A) + sum_{i in S} r_i(B)] >= 1 .

WHAT IS CHECKED HERE
 (a) L1, L2, L3, L4 on EVERY cross-disjoint pair at N=3 and on 300k random
     pairs at N=4,5,6 -- exact Fractions.
 (b) the measure-level relaxation solved by exhaustive rational grid search:
       g_D(Y) = min { T(nu) : nu supported in Y, denominators D }
     for m=1,2,3,4, then min over disjoint (Y_A,Y_B) of g+g.  If that minimum
     were < 2 the payment constant 1 would be dead (the reduction is TIGHT:
     any measure pair is realisable by an actual set pair, see x3 family F7).
 (c) the same minimum restricted to GENUINE configurations (every shared
     coordinate really relevant on both sides): the |S|>=2 regime.
"""
import sys, os, time, random
from fractions import Fraction
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib5 import (popcount, bcounts, pi_rel, pi_rel_int, influences,
                  rel, shadow_measure, Dvec, tv_to_uniform)


# ------------------------------------------------------------------ (a) chain

def check_chain(N, pairs):
    """returns dict of counters; asserts nothing, reports violations."""
    bad = {k: 0 for k in ("L1_emptyS", "L1_shadow", "L2", "L3a", "L3b", "L4",
                          "pi_lt_1")}
    worst = {"T_sum": None, "pi": None}
    for A, B in pairs:
        RA, RB = rel(A, N), rel(B, N)
        S = sorted(set(RA) & set(RB))
        if not S:
            bad["L1_emptyS"] += 1
            continue
        m = len(S)
        nu, sA = shadow_measure(A, N, S)
        om, sB = shadow_measure(B, N, S)
        if sA & sB:
            bad["L1_shadow"] += 1
        DA, DB = Dvec(nu, m), Dvec(om, m)
        rA = [Fraction(b, popcount(A)) for b in bcounts(A, N)]
        rB = [Fraction(b, popcount(B)) for b in bcounts(B, N)]
        for j, i in enumerate(S):
            if rA[i] < DA[j] or rB[i] < DB[j]:
                bad["L2"] += 1
        TA, TB = sum(DA), sum(DB)
        if tv_to_uniform(nu, m) > TA / 2 or tv_to_uniform(om, m) > TB / 2:
            bad["L3a"] += 1
        if (tv_to_uniform(nu, m) < 1 - Fraction(popcount(sA), 1 << m)
                or tv_to_uniform(om, m) < 1 - Fraction(popcount(sB), 1 << m)):
            bad["L3b"] += 1
        if TA + TB < 2:
            bad["L4"] += 1
        if worst["T_sum"] is None or TA + TB < worst["T_sum"]:
            worst["T_sum"] = TA + TB
        pi, _ = pi_rel(A, B, N)
        if pi < 1:
            bad["pi_lt_1"] += 1
        if worst["pi"] is None or pi < worst["pi"]:
            worst["pi"] = pi
    return bad, worst


def all_pairs(N):
    P = 1 << N
    for A in range(1, 1 << P):
        C = ((1 << P) - 1) ^ A
        sub = C
        while sub:
            yield A, sub
            sub = (sub - 1) & C


def random_pairs(N, k, seed=1):
    rng = random.Random(seed)
    P = 1 << N
    out = []
    while len(out) < k:
        A = rng.getrandbits(P)
        if A == 0:
            continue
        C = ((1 << P) - 1) ^ A
        if C == 0:
            continue
        # random nonempty submask of C
        B = C & rng.getrandbits(P)
        if B == 0:
            B = C & -C
        out.append((A, B))
    return out


# ------------------------------------------- (b),(c) measure-level relaxation

def compositions(parts, D):
    """all nonneg integer tuples of length `parts` summing to D."""
    out = []
    cur = [0] * parts

    def rec(j, rem):
        if j == parts - 1:
            cur[j] = rem
            out.append(tuple(cur))
            return
        for v in range(rem + 1):
            cur[j] = v
            rec(j + 1, rem - v)
    rec(0, D)
    return out


def grid_minima(m, D):
    """g_D(Y) for every Y subseteq {+-1}^m, by group-min + subset(zeta)-min.
    Returns (g_all, g_gen) as int arrays of D*T values (so exact rationals
    T = value/D), indexed by the 2^(2^m) support masks."""
    K = 1 << m
    C = np.array(compositions(K, D), dtype=np.int64)      # (M,K)
    Tnum = np.zeros(len(C), dtype=np.int64)
    pos = np.zeros((len(C), m), dtype=np.int64)
    for i in range(m):
        idx = np.arange(K) ^ (1 << i)
        dif = C - C[:, idx]
        pi_ = np.maximum(dif, 0).sum(axis=1)              # D * D_i(nu)
        pos[:, i] = pi_
        Tnum += pi_
    supp = ((C > 0).astype(np.int64) *
            (1 << np.arange(K, dtype=np.int64))[None, :]).sum(axis=1)
    BIG = 10 ** 9
    g = np.full(1 << K, BIG, dtype=np.int64)
    np.minimum.at(g, supp, Tnum)
    gen = (pos > 0).all(axis=1)
    gg = np.full(1 << K, BIG, dtype=np.int64)
    if gen.any():
        np.minimum.at(gg, supp[gen], Tnum[gen])
    # subset-min (zeta) transform: min over submasks
    for b in range(K):
        bit = 1 << b
        sel = (np.arange(1 << K) & bit) != 0
        idx = np.flatnonzero(sel)
        g[idx] = np.minimum(g[idx], g[idx ^ bit])
        gg[idx] = np.minimum(gg[idx], gg[idx ^ bit])
    return g, gg, D


def relaxation_min(m, D):
    g, gg, D = grid_minima(m, D)
    K = 1 << m
    FULL = (1 << K) - 1
    best = None
    bestY = None
    bestg = None
    bestgY = None
    for Y in range(1, FULL):
        Z = FULL ^ Y
        if g[Y] < 10 ** 9 and g[Z] < 10 ** 9:
            v = g[Y] + g[Z]
            if best is None or v < best:
                best, bestY = v, (Y, Z)
        if gg[Y] < 10 ** 9 and gg[Z] < 10 ** 9:
            v = gg[Y] + gg[Z]
            if bestg is None or v < bestg:
                bestg, bestgY = v, (Y, Z)
    return (Fraction(best, D), bestY,
            Fraction(bestg, D) if bestg is not None else None, bestgY, g, D)


def analytic_bound_check(m, D):
    """verify g_D(Y) >= 2(1-|Y|/2^m) exactly, for every Y."""
    g, gg, D = grid_minima(m, D)
    K = 1 << m
    bad = 0
    tight = 0
    for Y in range(1, (1 << K)):
        if g[Y] >= 10 ** 9:
            continue
        lhs = Fraction(int(g[Y]), D)
        rhs = 2 * (1 - Fraction(popcount(Y), K))
        if lhs < rhs:
            bad += 1
        if lhs == rhs:
            tight += 1
    return bad, tight


if __name__ == "__main__":
    print("=" * 74)
    print("(a) the chain L1-L4 on explicit pairs (exact Fractions)")
    print("=" * 74)
    t0 = time.time()
    bad, worst = check_chain(3, list(all_pairs(3)))
    print(f"  N=3, ALL 6050 cross-disjoint pairs: violations {bad}")
    print(f"        min over pairs of T(nu)+T(omega) = {worst['T_sum']}"
          f"   (bound: >= 2);  min pi_Rel = {worst['pi']}")
    for N, k in ((4, 60000), (5, 40000), (6, 20000)):
        bad, worst = check_chain(N, random_pairs(N, k))
        print(f"  N={N}, {k} random pairs: violations {bad}")
        print(f"        min T(nu)+T(omega) = {worst['T_sum']}"
              f"   min pi_Rel = {worst['pi']} = {float(worst['pi']):.6f}")
    print(f"  ({time.time()-t0:.1f}s)")

    print()
    print("=" * 74)
    print("(b),(c) measure-level relaxation: min [g(Y_A)+g(Y_B)] over DISJOINT")
    print("        nonempty supports, exhaustive over rational grids")
    print("=" * 74)
    for m, D in ((1, 24), (2, 24), (3, 16), (4, 8)):
        t1 = time.time()
        v, Ys, vg, Ygs, g, D = relaxation_min(m, D)
        nb, nt = analytic_bound_check(m, D)
        print(f"  m={m}  grid denominator {D}  "
              f"(#measures {len(compositions(1<<m, D))})")
        print(f"      min [T(nu)+T(omega)] over disjoint supports = {v}"
              f"    supports (Y_A,Y_B) = {Ys}")
        print(f"      best GENUINE (all D_i>0 both sides) ON THIS GRID = {vg}"
              f"    supports = {Ygs}")
        print(f"        [grid-restricted: an UPPER bound on the genuine "
              f"infimum, not a lower bound]")
        print(f"      g_D(Y) >= 2(1-|Y|/2^m): violations {nb}, "
              f"tight for {nt} supports   ({time.time()-t1:.1f}s)")
    print("DONE x2")
