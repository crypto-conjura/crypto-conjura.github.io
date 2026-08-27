"""
SDP probe of the Family(3,4) partition at (d=4, N=12): can density-matrix
averaging (with the degree-slack deg f = 3 < d = 4) push either side below
the hand values 1/11 (union side) / 1/12 (product side)?
"""
import sys, time
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import z2_charset, z2_eval_matrix, z2_side_matrices, tau_solver

N, d = 12, 4
blocks = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
P = 1 << N
t0 = time.time()
A_pts = [x for x in range(P)
         if any(all(not (x >> i) & 1 for i in blk) for blk in blocks)]
chars = z2_charset(N, d)
print(f"N={N} d={d}: {len(chars)} characters, |A|={len(A_pts)}, "
      f"|B|={P-len(A_pts)}")
E = z2_eval_matrix(N, chars)
A = sum(1 << x for x in A_pts)
full = (1 << P) - 1
for name, mask in (("A (union)", A), ("B (product)", full ^ A)):
    dV, Ms, Bb, _ = z2_side_matrices(N, d, mask, chars, E)
    lo, up, w, cuts, mix = tau_solver(Ms, tol=1e-9, maxit=300)
    print(f"side {name}: dim {dV}, tau in [{lo:.9f}, {up:.9f}]  "
          f"(1/11={1/11:.9f}, 1/12={1/12:.9f}) [{time.time()-t0:.0f}s]")
