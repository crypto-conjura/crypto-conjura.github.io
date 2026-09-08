"""
r1_exhaustive.py -- COMPLETE searches over all degree-<=d subsets of {+-1}^N.

Part 1: min over nonempty A of  min_{W admissible for A} lam(A,W).
Part 2: min over CROSS-DISJOINT pairs (A,B) of
          minmax = min_{W in adm(A,B)} max(lam(A,W), lam(B,W))    (adversary picks W)
          maxmax = max_{W in adm(A,B)} max(lam(A,W), lam(B,W))    (prover picks W)
        where adm(A,B) = {W_A u W_B : W_X a minimal defect set of X, |W_X| <= d}.

Everything exact (Fraction / int).  N <= 4 is complete over all 2^(2^N) subsets.
"""
import sys, os, itertools, time
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib9 import (lam, minimal_defect_sets, admissible_windows, deg, alpha,
                  popcount, relevant, maxinf_rel, fibre_profile, cube_all)


def degsets(N, d):
    """all nonempty A subseteq {+-1}^N with deg(1_A) <= d."""
    out = []
    for A in range(1, 1 << (1 << N)):
        if deg(A, N) <= d:
            out.append(A)
    return out


def part1(N, d, sets):
    best, arg = None, None
    for A in sets:
        if A == cube_all(N):
            continue                       # A = whole cube: lam = 0, no partner
        Ds = minimal_defect_sets(A, N, d)
        if not Ds:
            continue
        for W in Ds:
            v = lam(A, N, W)
            if best is None or v < best:
                best, arg = v, (A, W)
    return best, arg


def part2(N, d, sets, cap=None):
    bestmin, argmin = None, None
    bestmax, argmax = None, None
    dcache = {}
    for A in sets:
        if A not in dcache:
            dcache[A] = minimal_defect_sets(A, N, d)
        if not dcache[A]:
            continue
        for B in sets:
            if A & B:
                continue
            if B not in dcache:
                dcache[B] = minimal_defect_sets(B, N, d)
            if not dcache[B]:
                continue
            vals = []
            for wa in dcache[A]:
                for wb in dcache[B]:
                    W = tuple(sorted(set(wa) | set(wb)))
                    vals.append((max(lam(A, N, W), lam(B, N, W)), W))
            lo = min(vals)
            hi = max(vals)
            if bestmin is None or lo[0] < bestmin:
                bestmin, argmin = lo[0], (A, B, lo[1])
            if bestmax is None or hi[0] < bestmax:
                bestmax, argmax = hi[0], (A, B, hi[1])
    return (bestmin, argmin), (bestmax, argmax)


def describe(A, N):
    pts = [format(m, "0%db" % N)[::-1] for m in range(1 << N) if (A >> m) & 1]
    return "|A|=%d  alpha=%s  rel=%s  pts(+=0)=%s" % (
        popcount(A), alpha(A, N), relevant(A, N),
        ",".join(pts) if len(pts) <= 12 else "...")


if __name__ == "__main__":
    for N in (2, 3, 4):
        for d in range(1, N + 1):
            t0 = time.time()
            S = degsets(N, d)
            b1, a1 = part1(N, d, S)
            print("== N=%d d=%d :  #{A : deg<=d} = %d" % (N, d, len(S)))
            print("   PART 1  min_A min_W lam(A,W) = %s (~%.5f)   2^-d/alpha floor?"
                  % (b1, float(b1)))
            if a1:
                A, W = a1
                print("      minimiser: W=%s  %s  profile=%s"
                      % (list(W), describe(A, N),
                         {str(k): v for k, v in sorted(fibre_profile(A, N, W).items())}))
            (lo, alo), (hi, ahi) = part2(N, d, S)
            print("   PART 2  min over pairs of  min_W max(lamA,lamB) = %s (~%.5f)"
                  % (lo, float(lo)))
            if alo:
                A, B, W = alo
                print("      pair: W=%s | A: %s | B: %s"
                      % (list(W), describe(A, N), describe(B, N)))
                print("      lamA=%s lamB=%s  alpha=%s beta=%s  2^{1-d}=%s"
                      % (lam(A, N, W), lam(B, N, W), alpha(A, N), alpha(B, N),
                         F(2, 2 ** d)))
            print("   PART 2' min over pairs of  max_W max(lamA,lamB) = %s (~%.5f)"
                  % (hi, float(hi)))
            if ahi:
                A, B, W = ahi
                print("      pair: W=%s | A: %s | B: %s"
                      % (list(W), describe(A, N), describe(B, N)))
            print("   [%.1fs]" % (time.time() - t0))
