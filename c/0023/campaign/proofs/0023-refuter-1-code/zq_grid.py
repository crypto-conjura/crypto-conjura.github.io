"""
Grid construction over Y = Z_q (here q = 3), d x d grid of single
coordinates, N = d^2:

  f_r = prod_c sqrt(q) 1_{x_{r,c} = 0}   (rows),  F uniform over rows
  g_c = prod_r sqrt(q) 1_{x_{r,c} = 1}   (cols),  G uniform over columns

Row r and column c conflict at cell (r,c): x = 0 vs x = 1.  Unit norms,
degree d, per-coordinate average influence = (1/d) * (q-1)/q.

Hence for EVERY finite abelian group Y (taking any element 1 != 0):
eps*(Y, d) <= (1 - 1/|Y|)/d = O(1/d), so any conjecture-witnessing delta
must have c_2 >= 1 REGARDLESS of the group.

This script verifies q = 3, d = 2 numerically to 1e-12 (support
disjointness is checked exactly as an integer statement).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import zq_point, zq_charset, zq_eval_matrix

q, d = 3, 2
N = d * d
P = q**N
cell = lambda r, c: r * d + c

# truth tables
def row_f(r):
    return np.array([q**(d/2) if all(zq_point(x, N, q)[cell(r, c)] == 0
                                     for c in range(d)) else 0.0
                     for x in range(P)])
def col_g(c):
    return np.array([q**(d/2) if all(zq_point(x, N, q)[cell(r, c)] == 1
                                     for r in range(d)) else 0.0
                     for x in range(P)])

fs = [row_f(r) for r in range(d)]
gs = [col_g(c) for c in range(d)]
# incompatibility (exact: entries are 0 or q^{d/2}, product zero iff one is 0)
for a in fs:
    for b in gs:
        assert not np.any((a != 0) & (b != 0))
# norms
for h in fs + gs:
    assert abs(np.mean(h**2) - 1) < 1e-12
# influences via Fourier
chars = zq_charset(N, q, N)   # full character set
E = zq_eval_matrix(N, q, chars)
def influences(h):
    hh = (E.conj().T @ h) / P          # Fourier coefficients
    deg = max(sum(1 for a in t if a) for t, c in zip(chars, hh)
              if abs(c) > 1e-9)
    infl = [sum(abs(c)**2 for t, c in zip(chars, hh) if t[i] != 0)
            for i in range(N)]
    return deg, infl
avgF = np.zeros(N); avgG = np.zeros(N)
for h in fs:
    deg, infl = influences(h)
    assert deg == d
    avgF += np.array(infl) / d
for h in gs:
    deg, infl = influences(h)
    assert deg == d
    avgG += np.array(infl) / d
target = (1 / d) * (q - 1) / q
assert np.allclose(avgF, target, atol=1e-12)
assert np.allclose(avgG, target, atol=1e-12)
print(f"Z_{q} grid, d={d}, N={N}: incompatible; unit norms; degree {d}; "
      f"all per-coordinate average influences = (1/d)(q-1)/q = {target:.6f}")
print("=> eps*(Y,d) = O(1/d) for every finite abelian group Y.")
