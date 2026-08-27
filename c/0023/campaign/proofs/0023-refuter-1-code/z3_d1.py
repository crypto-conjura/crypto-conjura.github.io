"""
Y = Z_3, d = 1: exhaustive over all partitions (A, A^c) of Z_3^N for
N = 1, 2 (both sides must admit a nonzero degree<=1 function vanishing
outside them).  Degree over Z_q counts ACTIVE COORDINATES, so a degree-1
function of one Z_3 coordinate is an arbitrary function of it.

Complex Hermitian SDP (floats, two-sided bounds).  Reduction R2 (min over
disjoint pairs = min over partitions) applies verbatim.
"""
import sys, itertools, time
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import zq_charset, zq_eval_matrix, zq_side_matrices, tau_solver

def run(N, q=3, d=1):
    t0 = time.time()
    chars = zq_charset(N, q, d)
    E = zq_eval_matrix(N, q, chars)
    P = q**N
    results = []
    for bits in range(1, (1 << P) - 1):
        A = {x for x in range(P) if (bits >> x) & 1}
        if 0 not in A:      # fix side-swap symmetry: point 0 in A
            continue
        B = set(range(P)) - A
        dA, MsA, BA, _ = zq_side_matrices(N, q, d, A, chars, E)
        if dA == 0:
            continue
        dB, MsB, BB, _ = zq_side_matrices(N, q, d, B, chars, E)
        if dB == 0:
            continue
        loA, upA, _, _, _ = tau_solver(MsA, tol=1e-9)
        loB, upB, _, _, _ = tau_solver(MsB, tol=1e-9)
        results.append((max(loA, loB), max(upA, upB), sorted(A), dA, dB))
    results.sort()
    print(f"Z_3, d=1, N={N}: {len(results)} feasible partitions "
          f"(of {(1<<P)//2 - 1}); time {time.time()-t0:.0f}s")
    for lo, up, A, dA, dB in results[:6]:
        print(f"  value in [{lo:.9f}, {up:.9f}]  dims=({dA},{dB})  A={A}")
    if results:
        print(f"  ==> eps*(Z_3, d=1, N={N}) in "
              f"[{results[0][0]:.9f}, {results[0][1]:.9f}]")
    print()

if __name__ == "__main__":
    run(1)
    run(2)
