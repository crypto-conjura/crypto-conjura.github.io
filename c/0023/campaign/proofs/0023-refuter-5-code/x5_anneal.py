"""
x5_anneal.py -- METHOD-INDEPENDENT hunt.  Simulated annealing directly on the
raw ternary labelling of {+-1}^N (each point: in A, in B, or in neither),
objective pi_Rel, N = 5,6,7,8.  Uses NONE of the structure exploited elsewhere
(no shadow lemma, no block decomposition, no measure relaxation) -- so it is an
independent check that the minimum really is 1 and never below.

Any state with pi_Rel < 1 is dumped immediately with an exact-Fraction
certificate.
"""
import sys, os, time, random
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib5 import popcount, pi_rel, pi_rel_int


def make_idx(N):
    ar = np.arange(1 << N)
    return [ar ^ (1 << i) for i in range(N)]


def pival(lab, N, idx):
    a = lab == 1
    b = lab == 2
    nA = int(a.sum())
    nB = int(b.sum())
    if nA == 0 or nB == 0:
        return 1e9, None
    tot = 0.0
    bs = []
    for i in range(N):
        bA = int(np.count_nonzero(a & ~a[idx[i]]))
        bB = int(np.count_nonzero(b & ~b[idx[i]]))
        bs.append((bA, bB))
        if bA and bB:
            tot += bA / (2 * nA) + bB / (2 * nB)
    return tot, (nA, nB, bs)


def anneal(N, steps, seed, T0=0.35, T1=0.004):
    rng = random.Random(seed)
    idx = make_idx(N)
    P = 1 << N
    lab = np.array([rng.randrange(3) for _ in range(P)], dtype=np.int8)
    cur, _ = pival(lab, N, idx)
    best, bestlab = cur, lab.copy()
    for t in range(steps):
        T = T0 * (T1 / T0) ** (t / steps)
        p = rng.randrange(P)
        old = lab[p]
        new = rng.randrange(3)
        if new == old:
            continue
        lab[p] = new
        val, _ = pival(lab, N, idx)
        if val <= cur or rng.random() < np.exp(-(val - cur) / T):
            cur = val
            if val < best:
                best, bestlab = val, lab.copy()
        else:
            lab[p] = old
    return best, bestlab


def to_masks(lab):
    A = B = 0
    for p, v in enumerate(lab):
        if v == 1:
            A |= 1 << p
        elif v == 2:
            B |= 1 << p
    return A, B


if __name__ == "__main__":
    t0 = time.time()
    grand = None
    for N, restarts, steps in ((5, 200, 30000), (6, 150, 40000),
                               (7, 100, 50000), (8, 60, 60000),
                               (9, 30, 80000)):
        best, bestpair, seeds_below = None, None, 0
        for s in range(restarts):
            v, lab = anneal(N, steps, seed=1000 * N + s)
            A, B = to_masks(lab)
            if A == 0 or B == 0:
                continue
            pi, S = pi_rel(A, B, N)
            if pi < 1:
                seeds_below += 1
                print(f"  !!! pi_Rel < 1 at N={N}: A=0x{A:x} B=0x{B:x} "
                      f"pi={pi}")
            if best is None or pi < best:
                best, bestpair = pi, (A, B, S)
        A, B, S = bestpair
        Num, Den = pi_rel_int(A, B, N)
        print(f"  N={N}: {restarts} annealing runs x {steps} steps -> "
              f"min pi_Rel = {best} = {float(best):.9f}  (|S|={len(S)}, "
              f"|A|={popcount(A)}, |B|={popcount(B)}, integer form "
              f"{Num}/{Den});  runs below 1: {seeds_below}")
        if grand is None or best < grand:
            grand = best
    print(f"  grand min over all annealing = {grand} "
          f"({time.time()-t0:.1f}s)")
    print("DONE x5")
