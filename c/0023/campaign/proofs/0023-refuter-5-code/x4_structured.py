"""
x4_structured.py -- the named extremal families, exactly, and the d-scaling.

Families (all values exact Fractions; every one materialised as an explicit
pair of subsets of {+-1}^N and evaluated from the definition):

 F1 complementary pairs (A, A^c)           -- the "both sides share everything"
                                              extreme; identity pi = I(h)/(4a(1-a))
 F2 grid / NegRow-PosCol (ACC22 Claim B.3) -- codim-d subcubes whose windows
                                              meet in ONE coordinate
 F3 subcube pairs with window overlap t
 F4 punctured-halfcube pair                -- the |S| = N near-miss
 F5 TWO-BLOCK near-miss                    -- |S| = 2 and pi -> 1
 F6 hub / address families
 F7 majority sharing every coordinate
"""
import sys, os, time
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib5 import (popcount, bcounts, rel, influences, influences_fourier,
                  pi_rel, pi_rel_int, degree)


def show(tag, A, B, N, fourier=False, deg=True):
    pi, S = pi_rel(A, B, N)
    Num, Den = pi_rel_int(A, B, N)
    assert Fraction(Num, Den) == pi
    dA = degree(A, N) if deg else "-"
    dB = degree(B, N) if deg else "-"
    extra = ""
    if fourier:
        piF, SF = pi_rel(A, B, N, fourier=True)
        extra = f"  [Fourier recheck: {piF}, S match {SF == S}]"
    print(f"  {tag}: N={N} |A|={popcount(A)} |B|={popcount(B)} "
          f"deg(1_A)={dA} deg(1_B)={dB} |S|={len(S)}  "
          f"pi_Rel = {pi} = {float(pi):.9f}{extra}")
    return pi, S


def subcube(N, fixed):
    """fixed: dict coord -> bit value (0 => x_i=+1, 1 => x_i=-1)."""
    A = 0
    for p in range(1 << N):
        if all(((p >> i) & 1) == v for i, v in fixed.items()):
            A |= 1 << p
    return A


def halfcube(N, i=0, v=0):
    return subcube(N, {i: v})


def maj_set(N, coords, sign=+1):
    """{x : sign * Maj(x_coords) = +1}, |coords| odd."""
    A = 0
    for p in range(1 << N):
        s = sum(1 if ((p >> i) & 1) == 0 else -1 for i in coords)
        if (s > 0) == (sign > 0):
            A |= 1 << p
    return A


if __name__ == "__main__":
    print("=" * 74)
    print("F1  complementary pairs (A, A^c)")
    print("=" * 74)
    # identity check + the exhaustive min over all sets on N<=4
    for N in (2, 3, 4):
        best, bw = None, None
        bestg, bwg = None, None
        for A in range(1, (1 << (1 << N)) - 1):
            B = ((1 << (1 << N)) - 1) ^ A
            pi, S = pi_rel(A, B, N)
            if best is None or pi < best:
                best, bw = pi, A
            if len(S) == N and (bestg is None or pi < bestg):
                bestg, bwg = pi, A
        print(f"  N={N}: min over ALL complementary pairs = {best} "
              f"(witness 0x{bw:x}, deg {degree(bw,N)});  min over pairs with "
              f"|S|=N : {bestg} = {float(bestg):.6f} (witness 0x{bwg:x}, "
              f"deg {degree(bwg,N)})")
    # identity pi = I(h)/(4 a (1-a))
    N = 4
    ok = True
    for A in range(1, (1 << (1 << N)) - 1):
        B = ((1 << (1 << N)) - 1) ^ A
        pi, S = pi_rel(A, B, N)
        n = popcount(A)
        a = Fraction(n, 1 << N)
        Ih = sum(Fraction(b, 1 << (N - 1)) for b in bcounts(A, N))
        if pi != Ih / (4 * a * (1 - a)):
            ok = False
    print(f"  identity  pi = I(h)/(4 alpha(1-alpha))  verified on all "
          f"{(1<<(1<<N))-2} complementary pairs at N=4: {ok}")
    print("  (so complementary pairs have pi >= 1 with equality iff deg(h)=1,")
    print("   by I(h) >= Var(h) = 4 alpha(1-alpha) -- they GROW with degree)")

    print()
    print("=" * 74)
    print("F2  grid / NegRow-PosCol: codim-d subcubes, windows meeting in one")
    print("=" * 74)
    for d in (2, 3, 4):
        N = 2 * d - 1
        WA = list(range(d))
        WB = list(range(d - 1, 2 * d - 1))
        A = subcube(N, {i: 0 for i in WA})              # all +1 on W_A
        B = subcube(N, {i: 1 for i in WB})              # all -1 on W_B
        show(f"d={d} (windows {WA} / {WB}, clash at {d-1})", A, B, N,
             fourier=(N <= 5))
    for d in (2, 3, 4):
        N = d * d
        if N > 16:
            continue
        rowA = [0 * d + j for j in range(d)]
        colB = [i * d + 0 for i in range(d)]
        A = subcube(N, {i: 1 for i in rowA})            # row 0 all -1
        B = subcube(N, {i: 0 for i in colB})            # col 0 all +1
        show(f"full dxd grid, d={d} (row 0 all -1 vs col 0 all +1)",
             A, B, N)
    print("  formula for every d: each side is a codim-d subcube, so r_i = 1")
    print("  on each of its d fixed coordinates, S = the single shared cell,")
    print("  hence pi_Rel = 1/2 + 1/2 = 1 EXACTLY, for every d >= 1.")

    print()
    print("=" * 74)
    print("F3  subcube pairs with window overlap t")
    print("=" * 74)
    d = 3
    for t in (1, 2, 3):
        N = 2 * d - t
        WA = list(range(d))
        WB = list(range(d - t, 2 * d - t))
        A = subcube(N, {i: 0 for i in WA})
        B = subcube(N, {i: (1 if i in WA else 0) for i in WB})
        show(f"d=3, overlap t={t}", A, B, N)

    print()
    print("=" * 74)
    print("F4  punctured halfcube: A = H \\ {p},  B = H^c u {p}   (|S| = N)")
    print("=" * 74)
    for N in range(2, 13):
        H = halfcube(N, 0, 0)
        p = 1 << 0          # careful: point index 0 has coord0 = +1 -> in H
        p = 0
        A = H & ~(1 << p)
        B = (((1 << (1 << N)) - 1) ^ H) | (1 << p)
        if popcount(A) == 0:
            continue
        pi, S = pi_rel(A, B, N)
        half = 1 << (N - 1)
        pred = (Fraction(1, 2) + Fraction(half - 1, 2 * (half + 1))
                + (N - 1) * (Fraction(1, 2 * (half - 1))
                             + Fraction(1, 2 * (half + 1)))) if half > 1 else None
        print(f"  N={N:2d}: |S|={len(S)}  pi_Rel = {pi} = {float(pi):.9f}"
              f"   closed form matches: {pred == pi}")
    print("  closed form: pi = 1/2 + (2^{N-1}-1)/(2(2^{N-1}+1))")
    print("               + (N-1)[1/(2(2^{N-1}-1)) + 1/(2(2^{N-1}+1))]")
    print("             = 1 + Theta(N 2^{-N})  ->  1 from ABOVE, |S| = N.")

    print()
    print("=" * 74)
    print("F5  TWO-BLOCK near-miss: |S| = 2 and pi_Rel = 1 + 2^{1-K}")
    print("=" * 74)
    for K in range(1, 6):
        N = 2 + 2 * K
        # shared coords 0,1 ; A-private = 2..K+1 ; B-private = K+2..2K+1
        nAy0 = (1 << (K - 1)) + 1 if K >= 1 else 1
        nAy1 = (1 << (K - 1)) - 1 if K >= 1 else 0
        if nAy1 <= 0:
            nAy0, nAy1 = 1, 0
        A = 0
        B = 0
        for p in range(1 << N):
            y0 = (p >> 0) & 1
            y1 = (p >> 1) & 1
            zA = (p >> 2) & ((1 << K) - 1)
            zB = (p >> (2 + K)) & ((1 << K) - 1)
            # A lives on the half y0 = 0, prefix fibres of sizes nAy0 > nAy1
            if y0 == 0:
                lim = nAy0 if y1 == 0 else nAy1
                if zA < lim:
                    A |= 1 << p
            else:
                lim = nAy0 if y1 == 0 else nAy1
                if zB < lim:
                    B |= 1 << p
        if popcount(A) == 0 or popcount(B) == 0:
            print(f"  K={K}: degenerate")
            continue
        pi, S = show(f"K={K}", A, B, N)
        pred = 1 + Fraction(1, 1 << (K - 1)) if K >= 1 else None
        print(f"        closed form 1 + 2^(1-K) = {pred}  match: {pred == pi}")
    print("  -> the |S| >= 2 regime has INFIMUM exactly 1, NOT attained;")
    print("     the gap can be made 2^{1-K} for any K (degree grows with K).")

    print()
    print("=" * 74)
    print("F5' SHARPEST near-miss with |S| = 2 and CONTROLLED DEGREE:")
    print("    A = H \\ C_A,  B = H^c \\ C_B,  H = {x_0 = +1},")
    print("    C_A = codim-(2+p) subcube inside H fixing x_1 = -1 and A's")
    print("    private block; C_B likewise inside H^c with B's own block.")
    print("    Prediction: deg = 2+p and pi_Rel = 1 + 1/(2^{p+1}-1).")
    print("=" * 74)
    for p in range(0, 5):
        N = 2 + 2 * p
        if N > 14:
            break
        H = halfcube(N, 0, 0)
        # A-private block: coords 2..p+1 ; B-private: p+2..2p+1
        CA = subcube(N, {0: 0, 1: 1, **{2 + j: 0 for j in range(p)}})
        CB = subcube(N, {0: 1, 1: 0, **{2 + p + j: 0 for j in range(p)}})
        A = H & ~CA
        B = (((1 << (1 << N)) - 1) ^ H) & ~CB
        if popcount(A) == 0 or popcount(B) == 0:
            continue
        pi, S = show(f"p={p} (deg should be {2+p})", A, B, N)
        pred = 1 + Fraction(1, (1 << (p + 1)) - 1)
        print(f"        1 + 1/(2^(p+1)-1) = {pred}   match: {pred == pi}")
    print("  => at degree d = 2+p the |S| = 2 payment can be as low as")
    print("     1 + 1/(2^{d-1}-1) = 1 + 2^{-Theta(d)}.")

    print()
    print("=" * 74)
    print("F6  hub / address families (a single shared coordinate)")
    print("=" * 74)
    import random
    rng = random.Random(7)
    N = 7
    for trial in range(4):
        # A: x_0 = +1 and an arbitrary nonempty pattern on coords 1,2,3
        pa = rng.randrange(1, 1 << 8)
        pb = rng.randrange(1, 1 << 8)
        A = B = 0
        for p in range(1 << N):
            if ((p >> 0) & 1) == 0 and (pa >> ((p >> 1) & 7)) & 1:
                A |= 1 << p
            if ((p >> 0) & 1) == 1 and (pb >> ((p >> 4) & 7)) & 1:
                B |= 1 << p
        if popcount(A) and popcount(B):
            show(f"hub, patterns 0x{pa:x}/0x{pb:x}", A, B, N)

    print()
    print("=" * 74)
    print("F7  majority sharing EVERY coordinate (the expensive extreme)")
    print("=" * 74)
    for N in (3, 5, 7, 9, 11):
        rest = list(range(1, N))
        if len(rest) % 2 == 0:
            rest = rest[:-1]
        A = halfcube(N, 0, 0) & maj_set(N, rest, +1)
        B = halfcube(N, 0, 1) & maj_set(N, rest, -1)
        if popcount(A) and popcount(B):
            show(f"N={N} half x Maj", A, B, N, deg=(N <= 7))
    print("DONE x4")
