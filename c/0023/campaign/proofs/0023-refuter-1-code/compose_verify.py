"""
Transport of the (d=2, eps=1/5) seed to higher degree, verified exactly.

TRANSPORT LEMMA (grid-outer composition; proof in report).  Given an
incompatible pair of singletons (f, g) on Z_2^n with deg <= d0, unit norm,
max_i Inf_i(f) <= a, max_i Inf_i(g) <= b, build for any D >= 1, on
N = D^2 * n coordinates arranged in a D x D grid of n-coordinate blocks:

  F = uniform over rows R:      f_R = tensor product over C of f on block (R,C)
  G = uniform over columns C:   g_C = tensor product over R of g on block (R,C)

Then: unit norms; deg <= D*d0; every (f_R, g_C) pair has disjoint supports
(they share block (R,C), where supp f cap supp g = empty); and for a
coordinate in block (R,C):  E_F Inf_i = a_i/D,  E_G Inf_i = b_i/D.

With the certified seed (a = 1/5, b = 1/6):  eps*(2D) <= 1/(5D) = (2/5)/d.

This script verifies the D = 2 instance EXACTLY (d = 4, N = 16):
   * incompatibility pointwise over all 2^16 points (integer arithmetic);
   * norms, degrees, and all 16 per-coordinate average influences exactly
     (Fraction arithmetic on tensored Fourier coefficients):
     expected: E_F Inf_i = 1/10 for all i (and E_G Inf_i = 1/12),
     so max = 1/10 < 1/8 = 1/(2d) at d = 4.
Also verifies the m=3 block pair at d=3, N=6 (eps = 1/6, ties grid with
fewer coordinates), exactly.
"""
import sys, itertools
from fractions import Fraction as F
sys.path.insert(0, ".")
from pcc_lib import popcount

# ---- seed pair on 4 coordinates, integer coefficient dictionaries S->c ----
S_ = lambda *idx: sum(1 << (i - 1) for i in idx)
F0 = {0: 2, S_(1): 1, S_(2): 1, S_(3): 1, S_(4): 1, S_(2, 3): 1, S_(1, 4): 1}
G0 = {0: -4, S_(1): 2, S_(2): 2, S_(3): 2, S_(4): 2,
      S_(1, 2): -1, S_(1, 3): -1, S_(2, 4): -1, S_(3, 4): -1}
NORM2_F0, NORM2_G0 = 10, 36     # exact squared norms of the integer forms

def tensor(coefA, coefB, shift):
    """Coefficients of A(x_block0) * B(x_block1), block1 shifted by `shift`."""
    out = {}
    for Sa, ca in coefA.items():
        for Sb, cb in coefB.items():
            out[Sa | (Sb << shift)] = ca * cb
    return out

def truth_table(coef, nbits):
    tab = []
    for x in range(1 << nbits):
        v = 0
        for S, c in coef.items():
            v += -c if (popcount(S & x) & 1) else c
        tab.append(v)
    return tab

def influences(coef, norm2, nbits):
    return [sum((F(c * c, norm2) for S, c in coef.items() if (S >> i) & 1),
                F(0))
            for i in range(nbits)]

def verify_D2():
    n, D = 4, 2
    Nn = D * D * n  # 16
    # blocks (R,C) -> shift 4*(2R+C)
    sh = lambda R, C: 4 * (2 * R + C)
    rows = [tensor(F0, F0, 4) for _ in range(1)]  # placeholder
    f_rows, g_cols = [], []
    for R in range(D):
        # tensor f on (R,0) and (R,1)
        c = {}
        a = {S << sh(R, 0): v for S, v in F0.items()}
        b = {S << sh(R, 1): v for S, v in F0.items()}
        for Sa, ca in a.items():
            for Sb, cb in b.items():
                c[Sa | Sb] = ca * cb
        f_rows.append(c)
    for C in range(D):
        c = {}
        a = {S << sh(0, C): v for S, v in G0.items()}
        b = {S << sh(1, C): v for S, v in G0.items()}
        for Sa, ca in a.items():
            for Sb, cb in b.items():
                c[Sa | Sb] = ca * cb
        g_cols.append(c)
    # degrees
    for c in f_rows + g_cols:
        assert max(popcount(S) for S in c) == 4
    # norms: squared norm of tensor = product = 100 and 36^2
    for c in f_rows:
        assert sum(v * v for v in c.values()) == NORM2_F0 ** 2
    for c in g_cols:
        assert sum(v * v for v in c.values()) == NORM2_G0 ** 2
    # incompatibility pointwise over 2^16 points
    tf = [truth_table(c, Nn) for c in f_rows]
    tg = [truth_table(c, Nn) for c in g_cols]
    for a in tf:
        for b in tg:
            assert all(x * y == 0 for x, y in zip(a, b))
    # influences: E_F Inf_i = average over rows
    infF = [F(0)] * Nn
    for c in f_rows:
        for i, v in enumerate(influences(c, NORM2_F0 ** 2, Nn)):
            infF[i] += v / D
    infG = [F(0)] * Nn
    for c in g_cols:
        for i, v in enumerate(influences(c, NORM2_G0 ** 2, Nn)):
            infG[i] += v / D
    assert all(v == F(1, 10) for v in infF), infF
    assert all(v == F(1, 12) for v in infG), infG
    print("composed pair (D=2): d=4, N=16, E_F Inf_i = 1/10, "
          "E_G Inf_i = 1/12 for all i; incompatible; all EXACT.")
    print("  => eps*(4) <= 1/10 < 1/8 = 1/(2d);  generally eps*(2D) <= 1/(5D).")

def verify_block_m3():
    # d=3, N=6: blocks {1,2},{3,4},{5,6}; marked = block all-plus.
    # f = sum_j 1_{block j = ++} (deg 2), g = prod_j (xa+xb-2)/sqrt6 (deg 3)
    n = 6
    blocks = [(0, 1), (2, 3), (4, 5)]
    # integer forms: f0 = 4*f-sum = sum_j (1+xa)(1+xb); g0 = prod (xa+xb-2)
    f0 = {}
    for a, b in blocks:
        for S, c in {0: 1, 1 << a: 1, 1 << b: 1, (1 << a) | (1 << b): 1}.items():
            f0[S] = f0.get(S, 0) + c
    g0 = {0: 1}
    for a, b in blocks:
        term = {0: -2, 1 << a: 1, 1 << b: 1}
        new = {}
        for S1, c1 in g0.items():
            for S2, c2 in term.items():
                new[S1 | S2] = new.get(S1 | S2, 0) + c1 * c2
        g0 = new
    assert max(popcount(S) for S, c in f0.items() if c) == 2
    assert max(popcount(S) for S, c in g0.items() if c) == 3
    n2f = sum(c * c for c in f0.values())   # ||f0||^2
    n2g = sum(c * c for c in g0.values())
    tf, tg = truth_table(f0, n), truth_table(g0, n)
    assert all(x * y == 0 for x, y in zip(tf, tg))
    inff = influences(f0, n2f, n)
    infg = influences(g0, n2g, n)
    assert all(v == F(1, 9) for v in inff), inff
    assert all(v == F(1, 6) for v in infg), infg
    print("block pair m=3: d=3, N=6, Inf_i(f) = 1/9, Inf_i(g) = 1/6, "
          "incompatible; EXACT.  (ties the 1/(2d) grid at d=3, with N=6 not 9)")

if __name__ == "__main__":
    verify_D2()
    verify_block_m3()
