"""
C1: d = 1, Y = Z_2.  EXACT exhaustive computation of

    eps*(1, N) = min over incompatible pairs (F, G) on Z_2^N of
                 max_i max( E_F Inf_i , E_G Inf_i )

for N = 1, 2, 3, 4, via reductions (R1)-(R3) of pcc_lib: this equals the
min over partitions (A, A^c) of {0,1}^N, both sides admitting a nonzero
degree-<=1 function vanishing outside them, of max(tau(A), tau(A^c)).

All feasibility (nullspace) computations are done in EXACT rational
arithmetic.  Whenever both sides have dim V = 1 the value is computed
exactly (the density matrix is forced).  Any side with dim V >= 2 would be
flagged and handled by the SDP (none occur; this is the rigidity claim).
"""
import sys, itertools
from fractions import Fraction
sys.path.insert(0, ".")
from pcc_lib import (z2_charset, z2_eval_matrix_frac, frac_nullspace,
                     z2_partition_orbit_reps, popcount)

def side_exact(N, chars, Efrac, mask):
    """Return (dim, exact influence vector of the unique unit function)
    for the space of degree<=1 functions vanishing outside `mask`."""
    P = 1 << N
    outside = [x for x in range(P) if not (mask >> x) & 1]
    rows = [Efrac[x] for x in outside]
    basis = frac_nullspace(rows, len(chars))
    dim = len(basis)
    if dim != 1:
        return dim, None
    v = basis[0]
    norm2 = sum(a * a for a in v)
    infs = []
    for i in range(N):
        infs.append(sum(a * a for a, S in zip(v, chars) if (S >> i) & 1) / norm2)
    return dim, infs

def main():
    for N in range(1, 5):
        chars = z2_charset(N, 1)
        Efrac = z2_eval_matrix_frac(N, chars)
        P = 1 << N
        full = (1 << P) - 1
        reps = z2_partition_orbit_reps(N)
        feasible = []
        big_dim_flag = []
        for A in reps:
            dA, infA = side_exact(N, chars, Efrac, A)
            if dA == 0:
                continue
            dB, infB = side_exact(N, chars, Efrac, full ^ A)
            if dB == 0:
                continue
            if dA != 1 or dB != 1:
                big_dim_flag.append((A, dA, dB))
                continue
            val = max(max(infA), max(infB))
            feasible.append((A, val, infA, infB))
        print(f"N={N}: {len(reps)} partition orbits; "
              f"{len(feasible)} feasible (both sides nonzero)")
        if big_dim_flag:
            print("  !! partitions with dim >= 2 on a side (rigidity fails):",
                  big_dim_flag)
        if feasible:
            vals = sorted(set(v for _, v, _, _ in feasible))
            print(f"  exact values over feasible partitions: "
                  f"{[str(v) for v in vals]}")
            best = min(feasible, key=lambda t: t[1])
            A, val, infA, infB = best
            print(f"  eps*(1,{N}) = {val}   (witness A mask = {A:#x}, "
                  f"A = {sorted(x for x in range(P) if (A>>x)&1)})")
            print(f"    influences side A: {[str(t) for t in infA]}")
            print(f"    influences side B: {[str(t) for t in infB]}")
        print()

if __name__ == "__main__":
    main()
