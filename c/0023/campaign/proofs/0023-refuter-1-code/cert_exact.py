"""
EXACT certification (pure rational arithmetic, no floats) of the d=2, N=4
record pair over Z_2 and of its optimality within its partition.

Pair (in +-1 variables x1..x4, uniform measure on {+-1}^4):

    f = (2 + x1 + x2 + x3 + x4 + x2x3 + x1x4) / sqrt(10)
    g = ( -4 + 2x1 + 2x2 + 2x3 + 2x4 - x1x2 - x1x3 - x2x4 - x3x4 ) / 6
      = -(x1 + x4 - 2)(x2 + x3 - 2)/6

CLAIMS (all verified exactly below; norms squared are used so everything is
rational):
 (1) deg f = deg g = 2;  ||f||_2 = ||g||_2 = 1.
 (2) f(x) * g(x) = 0 for all 16 points x  (incompatible singleton pair).
 (3) Inf_i(f) = 1/5 and Inf_i(g) = 1/6 for every i in {1,2,3,4};
     so max per-coordinate (average) influence = 1/5 < 1/4 = 1/(2d).
 (4) OPTIMALITY of 1/5 for this partition: with A = supp f, B = supp g
     (which partition the cube), every distribution over unit-norm degree<=2
     functions vanishing outside A has some coordinate with average
     influence >= 1/5.  Certificate: w = (1/4,1/4,1/4,1/4);
     exact PSD check of  Br^T (D_w - (1/5) I) Br  over the rational
     nullspace basis Br of V_A.  (Same check for side B at 1/6.)
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, ".")
from pcc_lib import (z2_charset, z2_eval_matrix_frac, frac_nullspace,
                     frac_psd_check, popcount)

N = 4
chars = z2_charset(N, 2)          # all S with |S| <= 2
Efrac = z2_eval_matrix_frac(N, chars)
P = 1 << N

def cvec(coeffs):
    """coeffs: dict S -> Fraction; return vector over `chars`."""
    return [F(coeffs.get(S, 0)) for S in chars]

S_ = lambda *idx: sum(1 << (i - 1) for i in idx)

# unnormalized: F0 = sqrt(10) f, G0 = 6 g  (integer coefficients)
F0 = cvec({0: 2, S_(1): 1, S_(2): 1, S_(3): 1, S_(4): 1,
           S_(2, 3): 1, S_(1, 4): 1})
G0 = cvec({0: -4, S_(1): 2, S_(2): 2, S_(3): 2, S_(4): 2,
           S_(1, 2): -1, S_(1, 3): -1, S_(2, 4): -1, S_(3, 4): -1})

def evaluate(v, x):
    return sum(c * e for c, e in zip(v, Efrac[x]))

# (1) degree and norm
assert max(popcount(S) for S, c in zip(chars, F0) if c) == 2
assert max(popcount(S) for S, c in zip(chars, G0) if c) == 2
norm2_F0 = sum(c * c for c in F0)          # = 10  => ||f|| = 1
norm2_G0 = sum(c * c for c in G0)          # = 36  => ||g|| = 1
assert norm2_F0 == 10 and norm2_G0 == 36
print("(1) degrees = 2; ||f||^2 = 10/10 = 1, ||g||^2 = 36/36 = 1  [exact]")

# (2) incompatibility, pointwise over all 16 points
vals_f = [evaluate(F0, x) for x in range(P)]
vals_g = [evaluate(G0, x) for x in range(P)]
assert all(a * b == 0 for a, b in zip(vals_f, vals_g))
A_pts = [x for x in range(P) if vals_f[x] != 0]
B_pts = [x for x in range(P) if vals_g[x] != 0]
assert set(A_pts) | set(B_pts) == set(range(P))
assert not (set(A_pts) & set(B_pts))
print(f"(2) f*g == 0 at all 16 points; supp f = {A_pts} (|A|={len(A_pts)}), "
      f"supp g = {B_pts} (|B|={len(B_pts)}); a partition  [exact]")

# also verify g's product form: 6g = -(x1+x4-2)(x2+x3-2) pointwise
for x in range(P):
    x1 = -1 if (x >> 0) & 1 else 1
    x2 = -1 if (x >> 1) & 1 else 1
    x3 = -1 if (x >> 2) & 1 else 1
    x4 = -1 if (x >> 3) & 1 else 1
    assert vals_g[x] == -(x1 + x4 - 2) * (x2 + x3 - 2)
print("    product form 6g = -(x1+x4-2)(x2+x3-2) verified pointwise [exact]")

# (3) influences
for i in range(N):
    inf_f = sum(c * c for c, S in zip(F0, chars) if (S >> i) & 1) / norm2_F0
    inf_g = sum(c * c for c, S in zip(G0, chars) if (S >> i) & 1) / norm2_G0
    assert inf_f == F(1, 5), (i, inf_f)
    assert inf_g == F(1, 6), (i, inf_g)
print("(3) Inf_i(f) = 1/5, Inf_i(g) = 1/6 for all i  [exact]")

# (4) optimality within the partition, via the exact dual certificate.
def side_lower_bound_cert(pts, q, wvec):
    """Exact check: for the space V of deg<=2 functions vanishing outside
    pts, and diagonal D_w with D_w[S] = sum_{i active in S} w_i, verify
    Br^T (D_w - q) Br is PSD  ==>  every rho in D(V) has
    max_i tr(P_i rho) >= sum_i w_i tr(P_i rho) >= q."""
    outside = [x for x in range(P) if x not in pts]
    Br = frac_nullspace([Efrac[x] for x in outside], len(chars))
    k = len(Br)
    Dw = [sum(wvec[i] for i in range(N) if (S >> i) & 1) - q for S in chars]
    G = [[sum(Br[a][j] * Dw[j] * Br[b][j] for j in range(len(chars)))
          for b in range(k)] for a in range(k)]
    return len(Br), frac_psd_check(G)

w = [F(1, 4)] * 4
dimA, okA = side_lower_bound_cert(A_pts, F(1, 5), w)
dimB, okB = side_lower_bound_cert(B_pts, F(1, 6), w)
assert okA and okB
print(f"(4) dual certificates PSD-verified exactly: tau(A) >= 1/5 "
      f"(dim V_A = {dimA}), tau(B) >= 1/6 (dim V_B = {dimB})")
print()
print("CERTIFIED: an incompatible singleton pair with d = 2, N = 4,")
print("max per-coordinate influence = 1/5 < 1/4 = 1/(2d); and 1/5 is")
print("optimal for its partition (both sides, exact rational certificates).")
