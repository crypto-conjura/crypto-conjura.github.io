"""
Simulated annealing over PARTITIONS (A, A^c) of Z_2^N at degree bound d,
objective = max(tau(A), tau(A^c)) via the density-matrix SDP (float).

Purpose: hunt for partitions beating the best known structured values:
  (d=2, N=5) and (d=2, N=6): anything < 1/5 = 0.2 ?
  (d=3, N=6):                anything < 2/15 ~ 0.13333 ?
Seeds: random subsets + the block-family partitions (padded with unused
coordinates, which leaves the value unchanged).

Search parameters and coverage are printed; every evaluation is cached.
This is a stochastic search: a null result rules out only the neighborhoods
explored, not all partitions.
"""
import sys, random, time
sys.path.insert(0, ".")
import numpy as np
from pcc_lib import z2_charset, z2_eval_matrix, z2_side_matrices, tau_solver

def make_eval(N, d):
    chars = z2_charset(N, d)
    E = z2_eval_matrix(N, chars)
    P = 1 << N
    full = (1 << P) - 1
    cache = {}
    def value(A):
        key = min(A, full ^ A)
        if key in cache:
            return cache[key]
        v = 0.0
        for mask in (A, full ^ A):
            dV, Ms, B, _ = z2_side_matrices(N, d, mask, chars, E)
            if dV == 0:
                v = float("inf")
                break
            lo, up, w, cuts, mix = tau_solver(Ms, tol=1e-7, maxit=80)
            v = max(v, up)
        cache[key] = v
        return v
    return value, cache, P, full

def pad_block_partition(N, blocks):
    """A = {>=1 marked block} as bitmask over 2^N points (unused coords free)."""
    P = 1 << N
    A = 0
    for x in range(P):
        if any(all(not (x >> i) & 1 for i in blk) for blk in blocks):
            A |= 1 << x
    return A

def anneal(N, d, seeds, n_iter, T0, seed_rng, label, target):
    rng = random.Random(seed_rng)
    value, cache, P, full = make_eval(N, d)
    best_v, best_A = float("inf"), None
    t0 = time.time()
    for A0 in seeds:
        A = A0
        v = value(A)
        if v < best_v:
            best_v, best_A = v, A
        for it in range(n_iter):
            T = T0 * (1 - it / n_iter) + 1e-4
            B = A ^ (1 << rng.randrange(P))
            if rng.random() < 0.3:
                B ^= 1 << rng.randrange(P)
            vB = value(B)
            if vB <= v or (vB < float("inf") and
                           rng.random() < pow(2.718, -(vB - v) / T)):
                A, v = B, vB
                if v < best_v:
                    best_v, best_A = v, A
    pts = sorted(x for x in range(P) if (best_A >> x) & 1) if best_A else None
    print(f"{label}: best value {best_v:.8f} (target to beat: {target}); "
          f"{len(cache)} distinct partitions evaluated; {time.time()-t0:.0f}s")
    print(f"  best A = {pts}")
    return best_v, best_A

if __name__ == "__main__":
    rnd = random.Random(12345)
    # ---- (d=2, N=5) ----
    P5 = 1 << 5
    seeds25 = [pad_block_partition(5, [(0, 1), (2, 3)])]
    seeds25 += [rnd.getrandbits(P5) for _ in range(2)]
    anneal(5, 2, seeds25, 400, 0.02, 1, "(d=2, N=5)", "1/5 = 0.2")
    # ---- (d=2, N=6) ----
    P6 = 1 << 6
    seeds26 = [pad_block_partition(6, [(0, 1), (2, 3)])]
    seeds26 += [rnd.getrandbits(P6) for _ in range(1)]
    anneal(6, 2, seeds26, 350, 0.02, 2, "(d=2, N=6)", "1/5 = 0.2")
    # ---- (d=3, N=6) ----
    seeds36 = [pad_block_partition(6, [(0, 1), (2, 3), (4, 5)]),
               pad_block_partition(6, [(0, 1, 2), (3, 4, 5)])]
    seeds36 += [rnd.getrandbits(P6) for _ in range(1)]
    anneal(6, 3, seeds36, 350, 0.02, 3, "(d=3, N=6)", "2/15 ~ 0.13333")
