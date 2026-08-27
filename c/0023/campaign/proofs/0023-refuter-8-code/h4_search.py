"""
h4_search.py -- BOUNDED EXHAUSTIVE SEARCH, to state exactly what was covered.

Space covered:
  (S1) N = 3: EVERY cross-disjoint pair (A,B) of nonempty subsets of {+-1}^3.
       (3^8 = 6561 assignments of the 8 points to {A, B, neither}, minus the
        ones with an empty side.)
  (S2) N = 4: EVERY cross-disjoint pair (A,B) of nonempty subsets of {+-1}^4.
       (3^16 = 43,046,721 assignments.)  Vectorised with numpy, exact integer
       arithmetic throughout (all quantities are rationals with denominator
       2|A| or 2|B|; comparisons are done on the exact Fractions of the
       best few candidates only).

Reported for each pair:  d = max(deg 1_A, deg 1_B),
  Q     = max_i min(Inf_i(f_A), Inf_i(f_B))
  piM   = min over choices of maximum-degree supports M(A),M(B) of
          sum_{i in M(B)} Inf_i(f_A) + sum_{i in M(A)} Inf_i(f_B)
          (the minimum is separable, so it is computed exactly)
and we minimise  max(piM, Q)  -- the joint objective a branch-2 counterexample
must drive to 2^{-Theta(d)}.
"""
import sys, os, itertools, time
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import *


def precompute(N):
    """for every subset mask of {+-1}^N: |X|, b_i(X), deg, list of top supports."""
    P = 1 << N
    M = 1 << P
    size = np.zeros(M, dtype=np.int64)
    bvec = np.zeros((M, N), dtype=np.int64)
    deg = np.zeros(M, dtype=np.int8)
    topbits = np.zeros(M, dtype=np.int64)     # bitmask over the 2^N supports S
    for X in range(M):
        size[X] = popcount(X)
        if size[X] == 0:
            continue
        bvec[X] = bcounts(X, N)
        c = spectrum(X, N)
        dd, tb = 0, 0
        for S in range(P):
            if c[S] == 0:
                continue
            k = popcount(S)
            if k > dd:
                dd, tb = k, 1 << S
            elif k == dd and dd > 0:
                tb |= 1 << S
        deg[X] = dd
        topbits[X] = tb
    return size, bvec, deg, topbits


def run(N, tlimit=600):
    P = 1 << N
    size, bvec, deg, topbits = precompute(N)
    supports = [[i for i in range(N) if (S >> i) & 1] for S in range(P)]
    full = (1 << P) - 1
    best = {}                                # d -> (value, A, B)
    t0 = time.time()
    npairs = 0
    allX = np.arange(1 << P, dtype=np.int64)
    for A in range(1, 1 << P):
        if deg[A] == 0:
            continue
        comp = full ^ A
        # all nonempty submasks of comp
        subs = [0]
        m = comp
        while m:
            low = m & -m
            subs = subs + [s | low for s in subs]
            m ^= low
        subs = np.array(subs[1:], dtype=np.int64)
        if subs.size == 0:
            continue
        subs = subs[deg[subs] > 0]
        if subs.size == 0:
            continue
        nA = size[A]
        bA = bvec[A]
        nB = size[subs]
        bB = bvec[subs]                       # (m, N)
        # Q  (exact rationals compared via cross-multiplication on int64)
        # min(bA_i/(2nA), bB_i/(2nB)) -> compare bA_i*nB vs bB_i*nA
        x = bA[None, :] * nB[:, None]         # numerator over 2 nA nB
        y = bB * nA
        mn = np.minimum(x, y)
        Qnum = mn.max(axis=1)                 # / (2 nA nB)
        # pi_M: separable minimum
        #   term1 = min_{MB top of B} sum_{i in MB} bA_i / (2 nA)
        #   term2 = min_{MA top of A} sum_{i in MA} bB_i / (2 nB)
        vS = np.array([sum(bA[i] for i in supports[S]) for S in range(P)],
                      dtype=np.int64)          # / (2 nA)
        t1 = np.full(subs.size, np.iinfo(np.int64).max, dtype=np.int64)
        tbB = topbits[subs]
        for S in np.argsort(vS):
            sel = ((tbB >> int(S)) & 1).astype(bool) & (t1 == np.iinfo(np.int64).max)
            t1[sel] = vS[S]
        topsA = [S for S in range(P) if (topbits[A] >> S) & 1]
        t2 = None
        for S in topsA:
            v = bB[:, supports[S]].sum(axis=1) if supports[S] else np.zeros(subs.size, dtype=np.int64)
            t2 = v if t2 is None else np.minimum(t2, v)
        # pi_M = t1/(2nA) + t2/(2nB) = (t1*nB + t2*nA) / (2 nA nB)
        piNum = t1 * nB + t2 * nA
        obj = np.maximum(piNum, Qnum)          # same denominator 2 nA nB
        dd = np.maximum(deg[A], deg[subs])
        npairs += subs.size
        for d in np.unique(dd):
            sel = dd == d
            j = int(np.argmin(obj[sel] / (2.0 * nA * nB[sel])))
            idx = np.nonzero(sel)[0][j]
            val = F(int(obj[idx]), int(2 * nA * nB[idx]))
            key = int(d)
            if key not in best or val < best[key][0]:
                best[key] = (val, A, int(subs[idx]),
                             F(int(piNum[idx]), int(2 * nA * nB[idx])),
                             F(int(Qnum[idx]), int(2 * nA * nB[idx])))
        if time.time() - t0 > tlimit:
            print(f"  ** TIME LIMIT after A = {A} of {1 << P} **")
            return best, npairs, False
    return best, npairs, True


for N in (3, 4):
    print("=" * 78)
    print(f"(S{N-2}) N = {N}: EVERY cross-disjoint pair of nonempty subsets")
    print("=" * 78)
    t0 = time.time()
    best, npairs, complete = run(N, tlimit=700)
    print(f"  pairs examined: {npairs:,}   exhaustive: {complete}   "
          f"time {time.time()-t0:.1f}s")
    print(f"  {'d':>3} | {'min max(pi_M, Q)':>20} | {'pi_M there':>14} | "
          f"{'Q there':>14} | {'|A|':>4} {'|B|':>4}")
    for d in sorted(best):
        v, A, B, pm, q = best[d]
        print(f"  {d:>3} | {str(v):>20} | {str(pm):>14} | {str(q):>14} | "
              f"{popcount(A):>4} {popcount(B):>4}")
    print()
