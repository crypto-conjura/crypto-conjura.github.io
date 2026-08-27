"""
x8_groups.py -- the same payment over Z_q, q > 2 (the Contract's group is
EXISTENTIALLY quantified, so the cheapest group is what matters).

GENERAL-GROUP INFLUENCE (re-derived, no citation).  For an abelian group Y and
f: Y^N -> C,  Inf_i(f) = (1/2) E_{x, x'}[ |f(x)-f(x')|^2 ], x' = x with
coordinate i re-randomised: expand in characters,
    E|f(x)-f(x')|^2 = 2 sum_chi |fhat|^2 - 2 sum_{chi_i = 0} |fhat|^2
                    = 2 Inf_i(f).
For f_A = 1_A/||1_A||_2 with alpha = |A|/q^N this gives, with L ranging over
the q^{N-1} lines in direction i,
    Inf_i(f_A) = 1 - (sum_L |A cap L|^2) / (q|A|) ,
which for q=2 is b_i(A)/(2|A|), the Boolean formula of lib5 (P1).  Everything
below is exact integer arithmetic:
    pi_Rel < 1   <=>   sum_{i in S} [ Bi(A)|B| + Bi(B)|A| ]  <  q|A||B|,
    Bi(A) = q|A| - sum_L |A cap L|^2 .
"""
import sys, os, time, random
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib5 import pi_rel


def lines(q, N):
    """for each coordinate i, the list of point-index sets of the q^{N-1}
    lines in direction i."""
    P = q ** N
    out = []
    for i in range(N):
        buckets = {}
        for p in range(P):
            digs = []
            x = p
            for j in range(N):
                digs.append(x % q)
                x //= q
            key = tuple(d for j, d in enumerate(digs) if j != i)
            buckets.setdefault(key, []).append(p)
        out.append(list(buckets.values()))
    return out


def line_masks(q, N):
    L = lines(q, N)
    return [[np.uint64(sum(1 << p for p in ln)) for ln in Li] for Li in L]


def pi_int(Amask, Bmask, q, N, LM):
    nA = bin(Amask).count("1")
    nB = bin(Bmask).count("1")
    if nA == 0 or nB == 0:
        return None
    Num = 0
    for Li in LM:
        BA = q * nA - sum(bin(int(Amask) & int(m)).count("1") ** 2
                          for m in Li)
        BB = q * nB - sum(bin(int(Bmask) & int(m)).count("1") ** 2
                          for m in Li)
        if BA > 0 and BB > 0:
            Num += BA * nB + BB * nA
    return Num, q * nA * nB


def exhaustive(q, N):
    P = q ** N
    LM = line_masks(q, N)
    best, bw = None, None
    nviol = neq = 0
    tot = 0
    for A in range(1, 1 << P):
        C = ((1 << P) - 1) ^ A
        sub = C
        while sub:
            r = pi_int(A, sub, q, N, LM)
            if r:
                tot += 1
                v = Fraction(*r)
                if v < 1:
                    nviol += 1
                    if nviol < 4:
                        print(f"    !!! pi<1: q={q} N={N} A={A:x} B={sub:x} "
                              f"pi={v}")
                if v == 1:
                    neq += 1
                if best is None or v < best:
                    best, bw = v, (A, sub)
            sub = (sub - 1) & C
    return best, bw, nviol, neq, tot


def hunt(q, N, runs, steps, seed=3):
    """annealing for the point sets too large to enumerate."""
    rng = random.Random(seed)
    P = q ** N
    LM = line_masks(q, N)
    best, bw = None, None
    for r in range(runs):
        lab = [rng.randrange(3) for _ in range(P)]
        A = sum(1 << p for p in range(P) if lab[p] == 1)
        B = sum(1 << p for p in range(P) if lab[p] == 2)
        cur = pi_int(A, B, q, N, LM)
        curv = cur[0] / cur[1] if cur else 1e9
        for t in range(steps):
            T = 0.3 * (0.01 / 0.3) ** (t / steps)
            p = rng.randrange(P)
            old = lab[p]
            new = rng.randrange(3)
            if new == old:
                continue
            if old == 1:
                A ^= 1 << p
            elif old == 2:
                B ^= 1 << p
            if new == 1:
                A |= 1 << p
            elif new == 2:
                B |= 1 << p
            lab[p] = new
            rr = pi_int(A, B, q, N, LM)
            val = rr[0] / rr[1] if rr else 1e9
            if val <= curv or rng.random() < np.exp(-(val - curv) / T):
                curv = val
                if best is None or val < best:
                    best, bw = val, (A, B)
            else:
                if new == 1:
                    A ^= 1 << p
                elif new == 2:
                    B ^= 1 << p
                if old == 1:
                    A |= 1 << p
                elif old == 2:
                    B |= 1 << p
                lab[p] = old
    return best, bw, LM


if __name__ == "__main__":
    print("=" * 74)
    print("engine cross-check: q=2 must reproduce the Boolean numbers")
    print("=" * 74)
    for N in (2, 3):
        LM = line_masks(2, N)
        bad = 0
        for A in range(1, 1 << (1 << N)):
            C = ((1 << (1 << N)) - 1) ^ A
            sub = C
            while sub:
                r = pi_int(A, sub, 2, N, LM)
                pi, S = pi_rel(A, sub, N)
                if Fraction(*r) != pi:
                    bad += 1
                sub = (sub - 1) & C
        print(f"  q=2 N={N}: general-group engine vs lib5 on every pair: "
              f"{bad} mismatches")

    print()
    print("=" * 74)
    print("exhaustive sweeps over Z_q^N (all cross-disjoint pairs)")
    print("=" * 74)
    for q, N in ((3, 1), (5, 1), (7, 1), (3, 2)):
        t0 = time.time()
        best, bw, nviol, neq, tot = exhaustive(q, N)
        print(f"  Z_{q}^{N} ({q**N} points, {tot} ordered pairs): "
              f"min pi_Rel = {best} = {float(best):.6f}   #(<1)={nviol}  "
              f"#(=1)={neq}   witness A={bw[0]:x} B={bw[1]:x}"
              f"   ({time.time()-t0:.1f}s)")
    print("  Two reference pairs over Z_q, exactly:")
    print("   * opposite cosets {x_1=a} / {x_1=b}:  pi = 2(q-1)/q  (>1 for q>2)")
    print("   * one point vs the other q-1 points:  Inf = (q-1)/q and 1/q,")
    print("     so pi = 1 EXACTLY for every q -- the payment floor 1 is NOT")
    print("     Boolean-specific, and q=2 is not cheaper than q>2.")

    print()
    print("=" * 74)
    print("annealing where enumeration is impossible")
    print("=" * 74)
    for q, N, runs, steps in ((4, 2, 20, 20000), (3, 3, 12, 20000),
                              (5, 2, 12, 20000)):
        t0 = time.time()
        best, bw, LM = hunt(q, N, runs, steps)
        r = pi_int(bw[0], bw[1], q, N, LM)
        print(f"  Z_{q}^{N} ({q**N} points): {runs}x{steps} moves -> "
              f"min pi_Rel = {Fraction(*r)} = {float(Fraction(*r)):.6f}"
              f"   ({time.time()-t0:.1f}s)")
    print("DONE x8")
