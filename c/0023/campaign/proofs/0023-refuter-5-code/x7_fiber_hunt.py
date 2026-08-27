"""
x7_fiber_hunt.py -- the HIGH-N hunt, in the regime where the infimum is
actually approached, plus a stress test of the one non-obvious link in the
obstruction chain.

PART A.  Exact fibre representation.  A cross-disjoint pair in block form is
  A  <->  (A_y)_{y in {+-1}^m},  A_y subseteq {+-1}^{p_A}   (bitmask int)
  B  <->  (B_y)_{y in {+-1}^m},  B_y subseteq {+-1}^{p_B}
with A_y, B_y not both nonempty (= disjointness, x2 L1).  Then, EXACTLY,
  |A| = sum_y |A_y|,   b_i(A) = sum_y |A_y \\ A_{y+i}|   for i in the S-block,
so pi_Rel is computable with integer arithmetic at N = m+p_A+p_B up to 20+,
where no enumeration of the cube is possible.  Hill-climbing/annealing on the
fibre masks then searches exactly the near-miss regime (|S| >= 2, huge private
blocks) where pi_Rel -> 1.  Cross-checked against lib5.pi_rel by materialising
the pair for small (m,p).

PART B.  Stress test of link L3,  TV(nu,U) <= T(nu)/2,  on random measures on
{+-1}^m for m up to 10 (the only step of the chain that is not a one-line
counting identity).  A single counterexample here would break the proof that
the payment cannot go below 1 and would reopen the hunt.
"""
import sys, os, time, random
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib5 import popcount, pi_rel, degree


# --------------------------------------------------------------- fibre engine

def pi_fib(Af, Bf, m):
    """exact (Num, Den) with pi_Rel = Num/Den, from fibre masks."""
    nA = sum(popcount(x) for x in Af)
    nB = sum(popcount(x) for x in Bf)
    if nA == 0 or nB == 0:
        return None
    bA = []
    bB = []
    for i in range(m):
        s = 1 << i
        bA.append(sum(popcount(Af[y] & ~Af[y ^ s]) for y in range(1 << m)))
        bB.append(sum(popcount(Bf[y] & ~Bf[y ^ s]) for y in range(1 << m)))
    Num = sum(bA[i] * nB + bB[i] * nA
              for i in range(m) if bA[i] > 0 and bB[i] > 0)
    return Num, 2 * nA * nB


def materialise(Af, Bf, m, pA, pB):
    N = m + pA + pB
    A = B = 0
    for p in range(1 << N):
        y = p & ((1 << m) - 1)
        za = (p >> m) & ((1 << pA) - 1)
        zb = (p >> (m + pA)) & ((1 << pB) - 1)
        if (Af[y] >> za) & 1:
            A |= 1 << p
        if (Bf[y] >> zb) & 1:
            B |= 1 << p
    return A, B, N


def random_split(m, rng):
    """random assignment of each y to A-side, B-side or unused; both sides
    nonempty."""
    while True:
        lab = [rng.randrange(3) for _ in range(1 << m)]
        if 0 in lab and 1 in lab:
            return lab


def climb(m, pA, pB, steps, seed, T0=0.20, T1=0.002):
    rng = random.Random(seed)
    K = 1 << m
    lab = random_split(m, rng)
    FA, FB = (1 << (1 << pA)) - 1, (1 << (1 << pB)) - 1
    Af = [rng.getrandbits(1 << pA) & FA if lab[y] == 0 else 0
          for y in range(K)]
    Bf = [rng.getrandbits(1 << pB) & FB if lab[y] == 1 else 0
          for y in range(K)]
    for y in range(K):
        if lab[y] == 0 and Af[y] == 0:
            Af[y] = 1
        if lab[y] == 1 and Bf[y] == 0:
            Bf[y] = 1
    cur = pi_fib(Af, Bf, m)
    curv = cur[0] / cur[1] if cur else 1e9
    best, bestst = curv, (list(Af), list(Bf))
    for t in range(steps):
        T = T0 * (T1 / T0) ** (t / steps)
        side = rng.randrange(2)
        F = Af if side == 0 else Bf
        want = 0 if side == 0 else 1
        ys = [y for y in range(K) if lab[y] == want]
        y = rng.choice(ys)
        p = rng.randrange(1 << (pA if side == 0 else pB))
        old = F[y]
        F[y] = old ^ (1 << p)
        r = pi_fib(Af, Bf, m)
        val = r[0] / r[1] if r else 1e9
        if val <= curv or rng.random() < np.exp(-(val - curv) / T):
            curv = val
            if val < best:
                best, bestst = val, (list(Af), list(Bf))
        else:
            F[y] = old
    return best, bestst


if __name__ == "__main__":
    print("=" * 74)
    print("PART A  fibre-representation hunt (block form, exact integers)")
    print("=" * 74)
    # cross-check the fibre formula against the definition
    rng = random.Random(11)
    okc = 0
    for _ in range(30):
        m, pA, pB = 2, 2, 2
        lab = random_split(m, rng)
        Af = [rng.getrandbits(4) if lab[y] == 0 else 0 for y in range(4)]
        Bf = [rng.getrandbits(4) if lab[y] == 1 else 0 for y in range(4)]
        for y in range(4):
            if lab[y] == 0 and Af[y] == 0:
                Af[y] = 1
            if lab[y] == 1 and Bf[y] == 0:
                Bf[y] = 1
        r = pi_fib(Af, Bf, m)
        A, B, N = materialise(Af, Bf, m, pA, pB)
        pi, S = pi_rel(A, B, N)
        okc += (Fraction(r[0], r[1]) == pi)
    print(f"  fibre formula vs lib5.pi_rel on 30 random block pairs "
          f"(m=2,p=2,2): {okc}/30 agree")

    t0 = time.time()
    grand = None
    below = 0
    for (m, pA, pB, runs, steps) in ((2, 4, 4, 12, 4000),
                                     (2, 6, 6, 8, 4000),
                                     (2, 8, 8, 5, 3000),
                                     (3, 4, 4, 10, 4000),
                                     (3, 6, 6, 6, 3000),
                                     (4, 3, 3, 10, 4000),
                                     (4, 5, 5, 5, 3000),
                                     (5, 3, 3, 6, 3000),
                                     (6, 2, 2, 6, 3000)):
        best = None
        bstate = None
        for s in range(runs):
            v, st = climb(m, pA, pB, steps, seed=97 * m + 7 * pA + s)
            if best is None or v < best:
                best, bstate = v, st
        r = pi_fib(bstate[0], bstate[1], m)
        ex = Fraction(r[0], r[1])
        if ex < 1:
            below += 1
            print(f"  !!! BELOW 1: m={m} pA={pA} pB={pB} pi={ex} "
                  f"Af={bstate[0]} Bf={bstate[1]}")
        print(f"  m={m} p_A={pA} p_B={pB}  (N={m+pA+pB})  {runs}x{steps} "
              f"moves -> min pi_Rel = {ex} = {float(ex):.9f}")
        if grand is None or ex < grand:
            grand = ex
    print(f"  grand min = {grand} = {float(grand):.9f}; runs below 1: {below}"
          f"   ({time.time()-t0:.1f}s)")

    print()
    print("=" * 74)
    print("PART B  stress test of L3:  2*TV(nu,U) <= T(nu)")
    print("=" * 74)
    rng2 = np.random.default_rng(5)
    for m in range(2, 11):
        K = 1 << m
        worst = 1e9
        nbad = 0
        for kind in range(4):
            for _ in range(4000):
                if kind == 0:
                    v = rng2.random(K)
                elif kind == 1:
                    v = rng2.random(K) ** 8
                elif kind == 2:
                    v = rng2.random(K) * (rng2.random(K) < 0.3)
                else:
                    v = (rng2.random(K) < 0.5) * 1.0
                s = v.sum()
                if s <= 0:
                    continue
                nu = v / s
                T = 0.0
                for i in range(m):
                    idx = np.arange(K) ^ (1 << i)
                    T += np.maximum(nu - nu[idx], 0).sum()
                tv = np.maximum(nu - 1.0 / K, 0).sum()
                slack = T - 2 * tv
                if slack < -1e-12:
                    nbad += 1
                worst = min(worst, slack)
        print(f"  m={m:2d}: 16000 random measures, min slack T-2TV = "
              f"{worst:+.3e}, violations {nbad}")
    # exact-arithmetic spot checks
    bad = 0
    for _ in range(300):
        m = random.randrange(2, 6)
        K = 1 << m
        w = [random.randrange(0, 7) for _ in range(K)]
        if sum(w) == 0:
            continue
        nu = [Fraction(x, sum(w)) for x in w]
        T = sum(sum((nu[y] - nu[y ^ (1 << i)] for y in range(K)
                     if nu[y] > nu[y ^ (1 << i)]), Fraction(0))
                for i in range(m))
        tv = sum((x - Fraction(1, K) for x in nu if x > Fraction(1, K)),
                 Fraction(0))
        if T < 2 * tv:
            bad += 1
    print(f"  exact-Fraction spot checks (300 random rational measures): "
          f"violations {bad}")
    print("DONE x7")
