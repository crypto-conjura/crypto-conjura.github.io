"""
s7 -- what CAP I(b) / Remark 2.2 actually reads off witness (a) when the
window is an UNRESTRICTED MINIMAL certificate of a uniform random point.

Quantity tested by CAP I(b) under Remark 2.2:
        ratio(k) = E[pi] / E[|W(A_k)| + |W(B_k)|],
with (T5(iv)) Inf_{a_t} = 1/4 and Inf_{y_j} = 2^{-k-1} on BOTH sides, so a
level-u certificate (k-u address bits, 2^u targets) has
        own size   = k - u + 2^u,
        payment    = (k-u)/4 + 2^u 2^{-k-1}   against the partner's influences.
By symmetry of the two sides,
        E[pi] = 2[(k - E u)/4 + E[2^u] 2^{-k-1}],
        E[|W_A| + |W_B|] = 2[k - E u + E[2^u]].

(1) EXACT for k <= 6 under the worst (MAX) minimal selection, from the exact
    q_u = Pr[u_max >= u] (inclusion-exclusion over the binom(k,u) subcube
    events).
(2) RIGOROUS for every k:  ratio >= (k - U(k)) / (4 B(k))  with U(k), B(k) the
    exact-rational union bounds on E[u_max] and E[size(u_max)].
(3) The one rule that DOES get capped: a non-uniform point rule (a point mass
    at a point of A_k whose 2^k targets are all +1) has E|W| = 2^{d-1} and
    ratio exactly 2^{-d}.  Verified from the truth table for k <= 3 and by
    the closed form for all k.
(4) sum vs max: E[ total codim of ALL prime implicants containing x ] is
    QUASIPOLYNOMIAL in d (k^{Theta(log log k)}), so a bound that charges the
    whole prime-implicant mass is not poly(d); only the max/expectation is.
"""
import sys
from fractions import Fraction as F
from itertools import combinations
from math import comb, log2
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib6 import influences_exact, degree_of
import numpy as np


def submasks(U):
    v = U
    while True:
        yield v
        if v == 0:
            return
        v = (v - 1) & U


def q_exact(k, u):
    Ulist = []
    for c in combinations(range(k), u):
        U = 0
        for t in c:
            U |= 1 << t
        Ulist.append(frozenset(v for v in submasks(U) if v != 0))
    M = len(Ulist)
    total = F(0)

    def rec(i, cnt, un):
        nonlocal total
        if i == M:
            if cnt:
                total += (-1) ** (cnt + 1) * F(1, 1 << len(un))
            return
        rec(i + 1, cnt, un)
        rec(i + 1, cnt + 1, un | Ulist[i])
    rec(0, 0, frozenset())
    return total


print("=" * 78)
print("(1) EXACT ratio under the WORST (MAX) minimal-certificate selection")
print("=" * 78)
print(f"{'k':>3} {'d':>3} {'E u_max':>16} {'E 2^u_max':>16} {'E|W_A|+|W_B|':>16} "
      f"{'E pi':>14} {'ratio':>16} {'float':>9}")
for k in range(1, 7):
    d = k + 1
    q = {1: F(1) - F(1, 1 << k)}
    for u in range(2, k + 1):
        q[u] = q_exact(k, u)
    Eu = sum(q.values())
    E2u = F(1) + sum(F(1 << (u - 1)) * q[u] for u in q)
    size = 2 * (k - Eu + E2u)
    pay = 2 * (F(k - Eu, 4) + E2u * F(1, 1 << (k + 1)))
    print(f"{k:>3} {d:>3} {str(Eu):>16} {str(E2u):>16} {str(size):>16} "
          f"{str(pay):>14} {str(pay/size):>16} {float(pay/size):>9.6f}")

print()
print("=" * 78)
print("(2) RIGOROUS lower bound on the ratio for EVERY k (exact rationals)")
print("    U(k) = sum_u min(1, C(k,u) 2^{1-2^u})  >= E u_max")
print("    B(k) = (k+1) + sum_{u>=2}(2^{u-1}-1) min(1, C(k,u) 2^{1-2^u}) >= E size")
print("=" * 78)
print(f"{'k':>6} {'d':>6} {'U(k)':>12} {'B(k)':>14} {'ratio >=':>12} "
      f"{'2^-(d-1)':>12}")
for k in [2, 3, 4, 6, 8, 12, 16, 32, 64, 128, 512, 1024, 4096]:
    d = k + 1
    U = F(0)
    B = F(k + 1)
    for u in range(1, k + 1):
        if 2 ** u - 1 >= 4000:
            break
        t = F(comb(k, u), 1 << (2 ** u - 1))
        if t > 1:
            t = F(1)
        U += t
        if u >= 2:
            B += ((1 << (u - 1)) - 1) * t
    # ratio = E[pi] / E[|W_A|+|W_B|]
    #       >= [ 2*(k - Eu)/4 ] / [ 2*B ] = (k - U) / (4 B)
    lb = F(k - U, 1) / (4 * B)
    print(f"{k:>6} {d:>6} {float(U):>12.4f} {float(B):>14.4f} "
          f"{float(lb):>12.6f} {('2^-%d' % (d-1)):>12}")

print()
print("=" * 78)
print("(3) the ONE capped rule: non-uniform point selection (point mass at an")
print("    all-targets-+1 point).  W(A_k)=W(B_k)= all 2^k targets.")
print("=" * 78)
for k in (1, 2, 3):
    N = k + (1 << k)
    n = 1 << N
    m = np.arange(n, dtype=np.int64)
    addr = m & ((1 << k) - 1)
    A = ((m >> (k + addr)) & 1) == 0
    IA = influences_exact(A, N)
    IB = influences_exact(~A, N)
    W = list(range(k, N))                      # all targets
    pay = sum((IB[i] for i in W), F(0)) + sum((IA[i] for i in W), F(0))
    den = 2 * len(W)
    print(f" k={k} d={k+1}: |W|=2^(d-1)={len(W)}, E[pi]={pay} (closed form 1), "
          f"denominator={den}, ratio={pay/den} = 2^-d? "
          f"{pay/den == F(1, 1 << (k+1))}")
print(" closed form, all k: pi = 2 * 2^k * 2^{-k-1} = 1, denominator = 2*2^k,")
print("                     ratio = 2^{-(k+1)} = 2^{-d}   -- exponentially capped")

print()
print("=" * 78)
print("(4) sum vs max: expected TOTAL codim of all prime implicants at x")
print("    S(k) = sum_u C(k,u) 2^{1-2^u} (k-u+2^u)   vs   E[max] <= B(k)")
print("=" * 78)
print(f"{'k':>6} {'S(k)':>18} {'log2 S / log2 k':>18} {'B(k)':>12}")
for k in [4, 8, 16, 32, 64, 128, 256, 1024, 4096, 65536]:
    S = F(0)
    B = F(k + 1)
    for u in range(0, k + 1):
        if 2 ** u - 1 >= 4000:
            break
        t = F(comb(k, u), 1 << (2 ** u - 1))
        S += t * (k - u + (1 << u))
        if u >= 2:
            B += ((1 << (u - 1)) - 1) * min(t, F(1))
    print(f"{k:>6} {float(S):>18.6g} {log2(float(S))/log2(k):>18.4f} "
          f"{float(B):>12.4f}")
