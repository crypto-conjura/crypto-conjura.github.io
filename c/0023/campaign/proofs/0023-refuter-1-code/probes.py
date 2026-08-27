"""
Targeted structural probes (float SDP with certified-in-float two-sided
bounds).  Each probe evaluates a specific partition (A, A^c) of Z_2^N at
degree bound d:  value = max(tau(A), tau(A^c)).

Block notation: coordinates in consecutive pairs ("blocks"); block j is
MARKED at x iff both its coordinates are + (bits 0).  These probes test
whether density-matrix averaging can push the block-family below its
hand-built values (f-sum side: 2/(m^2+3m); g-product side: 1/6).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import z2_charset, z2_eval_matrix, z2_side_matrices, tau_solver

def marked_mask_pts(N, blocks):
    """Set of points where at least one block is marked (block = tuple of
    coordinate indices; marked = all bits zero, i.e. all-plus)."""
    P = 1 << N
    pts = set()
    for x in range(P):
        for blk in blocks:
            if all(not (x >> i) & 1 for i in blk):
                pts.add(x)
                break
    return pts

def atleast_k_marked_pts(N, blocks, k):
    P = 1 << N
    pts = set()
    for x in range(P):
        cnt = sum(1 for blk in blocks
                  if all(not (x >> i) & 1 for i in blk))
        if cnt >= k:
            pts.add(x)
    return pts

def eval_partition(N, d, A_pts, label):
    chars = z2_charset(N, d)
    E = z2_eval_matrix(N, chars)
    P = 1 << N
    full = (1 << P) - 1
    A = sum(1 << x for x in A_pts)
    out = [label]
    vals = []
    for name, mask in (("A", A), ("B", full ^ A)):
        dV, Ms, B, _ = z2_side_matrices(N, d, mask, chars, E)
        if dV == 0:
            print(f"{label}: side {name} has dim V = 0 (infeasible)")
            return None
        lo, up, w, cuts, mix = tau_solver(Ms, tol=1e-10, maxit=400)
        vals.append((lo, up, dV))
    v_lo = max(vals[0][0], vals[1][0])
    v_up = max(vals[0][1], vals[1][1])
    print(f"{label}:")
    print(f"  tau(A) in [{vals[0][0]:.9f}, {vals[0][1]:.9f}] (dim {vals[0][2]}), "
          f"tau(B) in [{vals[1][0]:.9f}, {vals[1][1]:.9f}] (dim {vals[1][2]})")
    print(f"  value in [{v_lo:.9f}, {v_up:.9f}]")
    return v_lo, v_up

if __name__ == "__main__":
    B2 = [(0, 1), (2, 3), (4, 5)]
    # (i) d=3, N=6, m=3 2-blocks: A = {some block marked}
    eval_partition(6, 3, marked_mask_pts(6, B2),
                   "(i) d=3 N=6: A={>=1 of 3 blocks marked} (hand: 1/9 vs 1/6)")
    # (ii) d=3, N=6, b=3 blocks, m=2: A = {some 3-block marked}
    B3 = [(0, 1, 2), (3, 4, 5)]
    eval_partition(6, 3, marked_mask_pts(6, B3),
                   "(ii) d=3 N=6: A={>=1 of 2 triple-blocks marked} "
                   "(hand: 4/17 vs 1/12)")
    # (iii) d=2, N=6: A = {>= 2 of 3 blocks marked}
    eval_partition(6, 2, atleast_k_marked_pts(6, B2, 2),
                   "(iii) d=2 N=6: A={>=2 of 3 blocks marked}")
    # (iv) d=2, N=6: A = {>= 1 of 3 blocks marked} (g-side would need deg 3)
    eval_partition(6, 2, marked_mask_pts(6, B2),
                   "(iv) d=2 N=6: A={>=1 of 3 blocks marked}")
    # (v) d=4, N=8: 4 blocks, A = {>=1 marked}
    B24 = [(0, 1), (2, 3), (4, 5), (6, 7)]
    eval_partition(8, 4, marked_mask_pts(8, B24),
                   "(v) d=4 N=8: A={>=1 of 4 blocks marked} (hand: 1/14 vs 1/6)")
    # (vi) d=4, N=8: A = {>=2 of 4 blocks marked}
    eval_partition(8, 4, atleast_k_marked_pts(8, B24, 2),
                   "(vi) d=4 N=8: A={>=2 of 4 blocks marked}")
    # (vii) d=3, N=6: A = {>=2 of 3 blocks marked}
    eval_partition(6, 3, atleast_k_marked_pts(6, B2, 2),
                   "(vii) d=3 N=6: A={>=2 of 3 blocks marked}")
