"""
The two-parameter BLOCK FAMILY and the current record seeds.

Family(b, m): m disjoint blocks of b coordinates each, N = m*b.
Marked_j = {block j all +}.
  f = sum_{j=1}^m  1_{Marked_j}                      (degree b, "union" side)
  g = prod_{j=1}^m (x_{j,1}+...+x_{j,b} - b)/sqrt(b+b^2)   (degree m)
Then (exact, verified below):
  supp f = {>=1 marked block},  supp g = {no marked block}:  incompatible.
  Inf_i(f) = 1 / (2m (1 + (m-1) 2^{-b}))   for every coordinate i,
  Inf_i(g) = 1 / (b + b^2),
  d = max(b, m),   value  V(b,m) = max of the two,   ratio r = d * V.

Records: (b,m) = (2,2): d=2, V = 1/5,  r = 2/5    [certified in cert_exact]
         (b,m) = (3,4): d=4, V = 1/11, r = 4/11   [certified HERE, exact]

This script: (1) exact verification of Family(3,4) (and Family(2,2),
Family(3,3)); (2) ratio table over the family; (3) float SDP probe of
Family(3,3) at (d=3, N=9) to measure the further averaging gain.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, ".")
from pcc_lib import popcount, z2_charset, z2_eval_matrix, z2_side_matrices, tau_solver

def family_coeffs(b, m):
    N = b * m
    blocks = [tuple(range(j * b, (j + 1) * b)) for j in range(m)]
    # f0 = 2^b * f = sum_j prod_{i in block_j} (1 + x_i)
    f0 = {}
    for blk in blocks:
        for mask in range(1 << b):
            S = 0
            for t in range(b):
                if (mask >> t) & 1:
                    S |= 1 << blk[t]
            f0[S] = f0.get(S, 0) + 1
    # g0 = prod_j (sum x - b)
    g0 = {0: 1}
    for blk in blocks:
        term = {0: -b}
        for i in blk:
            term[1 << i] = 1
        new = {}
        for S1, c1 in g0.items():
            for S2, c2 in term.items():
                new[S1 | S2] = new.get(S1 | S2, 0) + c1 * c2
        g0 = new
    return N, f0, g0

def truth_table(coef, nbits):
    tab = []
    for x in range(1 << nbits):
        v = 0
        for S, c in coef.items():
            v += -c if (popcount(S & x) & 1) else c
        tab.append(v)
    return tab

def verify_family(b, m):
    N, f0, g0 = family_coeffs(b, m)
    degf = max(popcount(S) for S, c in f0.items() if c)
    degg = max(popcount(S) for S, c in g0.items() if c)
    assert degf == b and degg == m, (degf, degg)
    n2f = sum(c * c for c in f0.values())
    n2g = sum(c * c for c in g0.values())
    tf, tg = truth_table(f0, N), truth_table(g0, N)
    assert all(u * v == 0 for u, v in zip(tf, tg))          # incompatible
    inff = [sum((F(c * c, n2f) for S, c in f0.items() if (S >> i) & 1), F(0))
            for i in range(N)]
    infg = [sum((F(c * c, n2g) for S, c in g0.items() if (S >> i) & 1), F(0))
            for i in range(N)]
    expF = F(1, 2 * m) / (1 + F(m - 1, 2**b))
    expG = F(1, b + b * b)
    assert all(v == expF for v in inff), (inff[:4], expF)
    assert all(v == expG for v in infg), (infg[:4], expG)
    d = max(b, m)
    V = max(expF, expG)
    print(f"Family({b},{m}): d={d}, N={N}, Inf(f)={expF}, Inf(g)={expG}, "
          f"value={V}, ratio d*V = {d*V}  [EXACT: incompatibility pointwise, "
          f"norms, degrees, influences]")
    return d, V

def ratio_table(bmax=7, mmax=24):
    print("\nratio r(b,m) = max(b,m)*V(b,m), best per d:")
    best = {}
    for b in range(1, bmax + 1):
        for m in range(1, mmax + 1):
            fF = F(1, 2 * m) / (1 + F(m - 1, 2**b))
            fG = F(1, b + b * b)
            d = max(b, m)
            V = max(fF, fG)
            r = d * V
            if d not in best or r < best[d][0]:
                best[d] = (r, b, m, V)
    for d in sorted(best):
        r, b, m, V = best[d]
        print(f"  d={d:2d}: best (b,m)=({b},{m}), value={V} ~ {float(V):.5f}, "
              f"ratio={V*d} ~ {float(V*d):.5f}")

if __name__ == "__main__":
    verify_family(2, 2)
    verify_family(3, 3)
    verify_family(3, 4)
    ratio_table()
    # SDP probe of Family(3,3)'s partition at d=3 (N=9): can averaging beat
    # the hand value 2/15 on the union side / 1/12 on the product side?
    print("\nSDP probe, Family(3,3) partition, d=3, N=9:")
    N = 9
    blocks = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    P = 1 << N
    A_pts = [x for x in range(P)
             if any(all(not (x >> i) & 1 for i in blk) for blk in blocks)]
    chars = z2_charset(N, 3)
    E = z2_eval_matrix(N, chars)
    A = sum(1 << x for x in A_pts)
    full = (1 << P) - 1
    for name, mask in (("A (union side)", A), ("B (product side)", full ^ A)):
        dV, Ms, Bb, _ = z2_side_matrices(N, 3, mask, chars, E)
        lo, up, w, cuts, mix = tau_solver(Ms, tol=1e-9, maxit=300)
        print(f"  side {name}: dim {dV}, tau in [{lo:.9f}, {up:.9f}]")
