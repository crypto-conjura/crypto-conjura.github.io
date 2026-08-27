"""
x9_counts.py -- the EXACT SIZE of the pair space swept by x3's complete block
sweeps (the "state the exact space covered" obligation).

For each class and each (m, k): n(m,k) = #{sets on k coords, in the class,
relevant to all of the first m coordinates}.  The block sweep for a given m
covers every ordered pair (A,B) with A in some (m,k_A) family and B in some
(m,k_B) family, i.e. (sum_k n(m,k))^2 ordered pairs, for EVERY N (the private
blocks may sit anywhere, and coordinates relevant to neither side are free).
"""
import sys, os, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "0023-refuter-4-code"))
from lib4 import level3_all, next_level, coeffs, flip_arrays


def count_genuine(P, k, m, chunk=2_000_000):
    fl = flip_arrays(k)
    tot = 0
    for s in range(0, len(P), chunk):
        Q = P[s:s + chunk]
        gen = np.bitwise_count(Q) > 0
        for i in range(m):
            Am, sh = fl[i]
            F = ((Q & Am) << sh) | ((Q >> sh) & Am)
            gen &= np.bitwise_count(Q & ~F) > 0
        tot += int(gen.sum())
    return tot


def deg3_class(k):
    P = level3_all()
    for kk in range(3, k):
        P = next_level(P, kk)
    return P


if __name__ == "__main__":
    for tag, kmax in (("arbitrary degree", 4), ("degree<=3", 6),
                      ("degree<=2", 6)):
        print("=" * 70)
        print(f"{tag}, k <= {kmax}")
        print("=" * 70)
        n = {}
        for k in range(1, kmax + 1):
            t0 = time.time()
            if tag == "arbitrary degree":
                P = np.arange(1 << (1 << k), dtype=np.uint64)
            else:
                P = deg3_class(k) if k >= 3 else np.arange(1 << (1 << k),
                                                           dtype=np.uint64)
                if tag == "degree<=2" and k >= 3:
                    C = coeffs(P, k, sizes=(3,))
                    P = P[(C == 0).all(axis=1)]
            for m in range(1, min(k, 4) + 1):
                n[(m, k)] = count_genuine(P, k, m)
            print(f"  k={k}: |class|={len(P)}  "
                  + "  ".join(f"n(m={m})={n[(m,k)]}"
                              for m in range(1, min(k, 4) + 1))
                  + f"   ({time.time()-t0:.1f}s)")
        grand = 0
        for m in range(1, 5):
            tot = sum(v for (mm, k), v in n.items() if mm == m)
            cell = max((v for (mm, k), v in n.items() if mm == m), default=0)
            print(f"  m={m}: sides = {tot}  =>  ordered pairs covered = "
                  f"{tot*tot:,}   (largest single (k_A,k_B) cell "
                  f"{cell*cell:,})")
            grand += tot * tot
        print(f"  TOTAL ordered cross-disjoint pairs covered completely: "
              f"{grand:,}")
    print("DONE x9")
