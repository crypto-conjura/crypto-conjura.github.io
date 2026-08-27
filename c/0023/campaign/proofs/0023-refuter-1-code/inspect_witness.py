"""
Inspect + exactly certify the d=2, N=4 record partitions found by
dd_z2_exhaustive.py (value ~ 0.2 < 1/4 = the K2/grid frontier at d=2).

For a given partition (A, A^c):
  * exact rational nullspace bases of V_A, V_B (degree <= 2, vanish outside);
  * float SDP to locate optimal rho and dual w on each side;
  * print everything for structure hunting.
"""
import sys
from fractions import Fraction
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import (z2_charset, z2_eval_matrix, z2_eval_matrix_frac,
                     frac_nullspace, z2_side_matrices, tau_solver)

def name_char(S, N):
    if S == 0:
        return "1"
    return "".join(f"x{i+1}" for i in range(N) if (S >> i) & 1)

def inspect(N, d, A_pts):
    chars = z2_charset(N, d)
    E = z2_eval_matrix(N, chars)
    Efrac = z2_eval_matrix_frac(N, chars)
    P = 1 << N
    A = sum(1 << x for x in A_pts)
    full = (1 << P) - 1
    for label, mask in (("A", A), ("B", full ^ A)):
        pts = sorted(x for x in range(P) if (mask >> x) & 1)
        pm = [tuple('+' if not (x >> i) & 1 else '-' for i in range(N))
              for x in pts]
        print(f"side {label}: points {pts}")
        print(f"          {[''.join(t) for t in pm]}")
        outside = [x for x in range(P) if not (mask >> x) & 1]
        basis = frac_nullspace([Efrac[x] for x in outside], len(chars))
        print(f"  dim V = {len(basis)}; basis (character: coeff):")
        for v in basis:
            terms = [f"{c}*{name_char(S, N)}" for c, S in zip(v, chars) if c]
            print("    ", "  +  ".join(terms))
        dV, Ms, B, _ = z2_side_matrices(N, d, mask, chars, E)
        lo, up, w, cuts, mix = tau_solver(Ms, tol=1e-12)
        print(f"  tau in [{lo:.12f}, {up:.12f}]")
        print(f"  optimal dual weights w = {np.round(w, 8)}")
        # primal: build rho from cuts and mixture, report per-coordinate infl.
        k = B.shape[1]
        rho = np.zeros((k, k))
        for p, v in zip(mix, cuts):
            rho += p * np.outer(v, v)
        infl = [float(np.trace(Ms[i] @ rho)) for i in range(N)]
        print(f"  per-coordinate avg influence at optimum: {np.round(infl,8)}")
        # eigen-decomposition of rho -> the actual functions in the mixture
        vals, vecs = np.linalg.eigh(rho)
        print("  optimal mixture (weight: function in character coords):")
        for lam, u in zip(vals, vecs.T):
            if lam > 1e-8:
                fvec = B @ u
                terms = [f"{c:+.5f}*{name_char(S, N)}"
                         for c, S in zip(fvec, chars) if abs(c) > 1e-7]
                print(f"    {lam:.6f}:  " + "  ".join(terms))
        print()

if __name__ == "__main__":
    print("=" * 70)
    print("witness 1: A=[0,1,2,4,6,8,9]  (dims (2,4))")
    print("=" * 70)
    inspect(4, 2, [0, 1, 2, 4, 6, 8, 9])
    print("=" * 70)
    print("witness 2: A=[0,1,2,3,4,6,8,9]  (dims (3,3))")
    print("=" * 70)
    inspect(4, 2, [0, 1, 2, 3, 4, 6, 8, 9])
