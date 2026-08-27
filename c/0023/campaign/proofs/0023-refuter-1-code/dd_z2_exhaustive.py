"""
C3 / Target 3 core: EXHAUSTIVE computation of eps*(d, N) over Z_2 for small
(d, N), over ALL partitions of the cube (up to cube symmetry + side swap),
with distributions handled exactly by the density-matrix SDP (pcc_lib R3).

  eps*(d,N) = min over partitions (A, A^c), both sides admitting a nonzero
              deg<=d function vanishing outside them, of max(tau(A), tau(A^c)).

For each orbit representative we compute certified (in floating point)
lower and upper bounds on tau via the concave dual  max_w lambda_min(M(w))
(every evaluated w is a valid lower bound; every explicit mixture of unit
vectors an upper bound).  Global minima are then re-certified in EXACT
rational arithmetic by cert_exact.py.

Usage: python dd_z2_exhaustive.py d N [d N ...]
"""
import sys, time
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import (z2_charset, z2_eval_matrix, z2_side_matrices,
                     z2_partition_orbit_reps, tau_solver)

def run(d, N, show=8):
    t0 = time.time()
    chars = z2_charset(N, d)
    E = z2_eval_matrix(N, chars)
    P = 1 << N
    full = (1 << P) - 1
    reps = z2_partition_orbit_reps(N)
    results = []
    for A in reps:
        dA, MsA, BA, _ = z2_side_matrices(N, d, A, chars, E)
        if dA == 0:
            continue
        dB, MsB, BB, _ = z2_side_matrices(N, d, full ^ A, chars, E)
        if dB == 0:
            continue
        loA, upA, wA, _, _ = tau_solver(MsA, tol=1e-10)
        loB, upB, wB, _, _ = tau_solver(MsB, tol=1e-10)
        results.append((max(loA, loB), max(upA, upB), A, dA, dB))
    results.sort()
    print(f"d={d} N={N}: {len(reps)} partition orbits, "
          f"{len(results)} feasible; time {time.time()-t0:.1f}s")
    for lo, up, A, dA, dB in results[:show]:
        pts = sorted(x for x in range(P) if (A >> x) & 1)
        print(f"  value in [{lo:.10f}, {up:.10f}]  dims=({dA},{dB})  "
              f"A={pts}")
    if results:
        lo, up, A, dA, dB = results[0]
        print(f"  ==> eps*({d},{N}) in [{lo:.10f}, {up:.10f}]")
    print()
    return results

if __name__ == "__main__":
    args = [int(a) for a in sys.argv[1:]] or [2, 3, 2, 4]
    for j in range(0, len(args), 2):
        run(args[j], args[j + 1])
