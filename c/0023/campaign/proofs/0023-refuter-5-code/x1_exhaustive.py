"""
x1_exhaustive.py -- COMPLETE sweep of every cross-disjoint pair (A,B) of
nonempty subsets of {+-1}^N for N = 1,2,3,4.  No degree restriction, so the
sweep covers every d simultaneously.

Space swept: all ternary labellings of the 2^N points (each point in A, in B,
or in neither), minus the two degenerate labellings per side:
      N=1:  3^2 = 9        N=2:  3^4 = 81
      N=3:  3^8 = 6561     N=4:  3^16 = 43 046 721      pairs (ordered)
All arithmetic INTEGER: the test pi_Rel < 1 is Num < 2|A||B|  (lib5 (P3)).

For N <= 3 every pair is additionally evaluated a SECOND, independent way:
influences from the integer Walsh transform (Fourier definition) and Rel from
the Fourier support.
"""
import sys, os, time
from fractions import Fraction
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib5 import (popcount, bcounts, pi_rel, pi_rel_int, influences,
                  influences_fourier, rel, rel_fourier, degree,
                  flip_arrays, bvec_np, subsets_of_mask)


def small_exhaustive(N):
    """pure-python, two independent methods, every pair."""
    P = 1 << N
    best = None
    best_pair = None
    nviol = nequal = nempty_S = 0
    vals = {}
    mismatch = 0
    for A in range(1, 1 << P):
        C = ((1 << P) - 1) ^ A
        if C == 0:
            continue
        B = C
        # iterate all nonempty submasks of C
        sub = C
        while sub:
            B = sub
            piA, S = pi_rel(A, B, N)
            Num, Den = pi_rel_int(A, B, N)
            assert Fraction(Num, Den) == piA, (A, B)
            # independent method: Fourier
            piF, SF = pi_rel(A, B, N, fourier=True)
            if piF != piA or SF != S:
                mismatch += 1
            if len(S) == 0:
                nempty_S += 1
            if piA < 1:
                nviol += 1
            if piA == 1:
                nequal += 1
            vals[piA] = vals.get(piA, 0) + 1
            if best is None or piA < best:
                best, best_pair = piA, (A, B)
            sub = (sub - 1) & C
    return dict(N=N, best=best, best_pair=best_pair, nviol=nviol,
                nequal=nequal, nempty_S=nempty_S, mismatch=mismatch,
                vals=vals)


def n4_exhaustive():
    """vectorised complete sweep at N=4 (3^16 ordered pairs)."""
    N = 4
    P = 1 << N
    FULL = (1 << P) - 1
    fl = flip_arrays(N)
    best = 10.0
    best_key = None
    best2 = 10.0            # restricted to |S| >= 2
    best2_key = None
    nviol = 0
    nequal = 0
    nemptyS = 0
    keyset = set()
    npairs = 0
    t0 = time.time()
    for A in range(1, FULL):
        C = FULL ^ A
        if C == 0:
            continue
        nA = popcount(A)
        bA = bcounts(A, N)
        Bs = subsets_of_mask(C, N)[1:]          # drop empty
        if len(Bs) == 0:
            continue
        nB = np.bitwise_count(Bs).astype(np.int64)
        bB = bvec_np(Bs, N, fl)
        sel = (bB > 0) & (np.array(bA, dtype=np.int64)[None, :] > 0)
        bAr = np.array(bA, dtype=np.int64)[None, :]
        Num = ((bAr * nB[:, None] + bB * nA) * sel).sum(axis=1)
        Den = 2 * nA * nB
        sizeS = sel.sum(axis=1)
        npairs += len(Bs)
        nviol += int(np.count_nonzero(Num < Den))
        nequal += int(np.count_nonzero(Num == Den))
        nemptyS += int(np.count_nonzero(sizeS == 0))
        ratio = Num / Den
        j = int(np.argmin(ratio))
        if ratio[j] < best:
            best = float(ratio[j])
            best_key = (A, int(Bs[j]), int(Num[j]), int(Den[j]))
        m2 = sizeS >= 2
        if m2.any():
            r2 = np.where(m2, ratio, 10.0)
            j2 = int(np.argmin(r2))
            if r2[j2] < best2:
                best2 = float(r2[j2])
                best2_key = (A, int(Bs[j2]), int(Num[j2]), int(Den[j2]))
        low = ratio < 1.30
        if low.any():
            ks = np.unique(Num[low] * 1000 + Den[low])
            keyset.update(int(k) for k in ks)
    return dict(best=best, best_key=best_key, best2=best2, best2_key=best2_key,
                nviol=nviol, nequal=nequal, nemptyS=nemptyS, npairs=npairs,
                keyset=keyset, secs=time.time() - t0)


if __name__ == "__main__":
    print("=" * 74)
    print("(a) N = 1,2,3 : every cross-disjoint pair, two independent methods")
    print("=" * 74)
    for N in (1, 2, 3):
        r = small_exhaustive(N)
        vals = sorted(r["vals"].items())
        print(f"  N={N}: pairs={sum(r['vals'].values())}  "
              f"min pi_Rel = {r['best']} = {float(r['best']):.6f}")
        print(f"        #(pi<1) = {r['nviol']}   #(pi==1) = {r['nequal']}   "
              f"#(S empty) = {r['nempty_S']}   "
              f"boundary-vs-Fourier mismatches = {r['mismatch']}")
        print("        smallest values (value : #pairs) :",
              ", ".join(f"{v}:{c}" for v, c in vals[:6]))
        A, B = r["best_pair"]
        print(f"        an argmin: A=0x{A:x} B=0x{B:x}  S={pi_rel(A,B,N)[1]}  "
              f"deg1_A={degree(A,N)} deg1_B={degree(B,N)}")

    print()
    print("=" * 74)
    print("(b) N = 4 : all 3^16 = 43,046,721 ordered labellings, integer-exact")
    print("=" * 74)
    r = n4_exhaustive()
    print(f"  ordered cross-disjoint pairs swept: {r['npairs']}"
          f"   ({r['secs']:.1f}s)")
    print(f"  #(pi_Rel < 1)  = {r['nviol']}       <-- 0 means NO counterexample")
    print(f"  #(pi_Rel == 1) = {r['nequal']}")
    print(f"  #(S = empty)   = {r['nemptyS']}     <-- must be 0")
    A, B, Num, Den = r["best_key"]
    print(f"  min pi_Rel = {Fraction(Num,Den)} = {r['best']:.6f}   "
          f"witness A=0x{A:x} B=0x{B:x} S={pi_rel(A,B,4)[1]}")
    A2, B2, Num2, Den2 = r["best2_key"]
    print(f"  min pi_Rel over pairs with |S| >= 2 : {Fraction(Num2,Den2)} = "
          f"{r['best2']:.6f}   witness A=0x{A2:x} B=0x{B2:x} "
          f"S={pi_rel(A2,B2,4)[1]}")
    vals = sorted({Fraction(k // 1000, k % 1000) for k in r["keyset"]})
    print("  all distinct pi_Rel values below 13/10:")
    print("   ", ", ".join(str(v) for v in vals))
    print("DONE x1")
