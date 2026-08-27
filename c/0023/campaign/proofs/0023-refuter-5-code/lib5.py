"""
lib5.py -- exact machinery for the RELEVANCE PAYMENT

     pi_Rel(A,B) := sum_{i in Rel(B)} Inf_i(f_A) + sum_{i in Rel(A)} Inf_i(f_B)

on cross-disjoint pairs of nonempty sets A,B subseteq {+-1}^N.
Artifact 0023-refuter-5 (refuter cycle 3, narrow decisive milestone).

REPRESENTATION.  A set A subseteq {+-1}^N is a python int / uint64 BITMASK over
the 2^N points; bit m set iff the point m in A.  Bit b of the point index m
encodes coordinate b (0 -> +1, 1 -> -1).  Same convention as
../0023-refuter-4-code/lib4.py and ../0023-refuter-2-code/junta_lib.py.

EXACT FACTS (each re-derived here, no citation).

 (P1) boundary form of the influence.  For nonempty A, f_A = 1_A/||1_A||_2,
      Inf_i(f_A) = Inf_i(1_A)/alpha with alpha = |A|/2^N, and
      Inf_i(1_A) = E[(d_i 1_A)^2] = (1/4) Pr_x[1_A(x) != 1_A(x^{+i})]
                 = b_i(A) / 2^{N+1},      b_i(A) := #{x in A : x^{+i} notin A}.
      Hence
            Inf_i(f_A) = b_i(A) / (2|A|)   =:  r_i(A)/2 .
      (Cross-checked against the Fourier definition by influences_fourier.)

 (P2) Rel(A) = { i : b_i(A) > 0 }  (the coordinates 1_A genuinely depends on).

 (P3) Since Inf_i(f_A)=0 for i notin Rel(A),
        pi_Rel(A,B) = sum_{i in S} [ Inf_i(f_A) + Inf_i(f_B) ],
        S := Rel(A) cap Rel(B),
      so pi_Rel is an all-integer quantity:
        pi_Rel = Num / (2|A||B|),  Num = sum_{i in S} ( b_i(A)|B| + b_i(B)|A| ).
      The test "pi_Rel < 1" is exactly the integer test Num < 2|A||B|.
"""

from fractions import Fraction
import itertools

try:
    import numpy as np
except Exception:                                    # pragma: no cover
    np = None


# ------------------------------------------------------------------ scalar API

def popcount(x):
    return bin(x).count("1")


def bcounts(A, N):
    """b_i(A) for i=0..N-1, A a python-int mask over the 2^N points."""
    out = []
    for i in range(N):
        s = 1 << i
        b = 0
        m = A
        while m:
            low = m & -m
            p = low.bit_length() - 1
            if not ((A >> (p ^ s)) & 1):
                b += 1
            m ^= low
        out.append(b)
    return out


def rel(A, N):
    return [i for i, b in enumerate(bcounts(A, N)) if b > 0]


def influences(A, N):
    """exact Fractions Inf_i(f_A), i=0..N-1, via (P1)."""
    n = popcount(A)
    if n == 0:
        raise ValueError("empty set")
    return [Fraction(b, 2 * n) for b in bcounts(A, N)]


def influences_fourier(A, N):
    """exact Inf_i(f_A) from the FOURIER DEFINITION with an integer Walsh
    transform:  Inf_i(f) = sum_{S ni i} fhat(S)^2,  f = 1_A/||1_A||_2.
    Fully independent of (P1) -- the cross-check method."""
    pts = [m for m in range(1 << N) if (A >> m) & 1]
    n = len(pts)
    out = [Fraction(0)] * N
    for S in range(1 << N):
        c = 0
        for m in pts:
            c += -1 if popcount(S & m) & 1 else 1
        if c == 0:
            continue
        # 1_A^hat(S) = c/2^N ; f = 1_A/sqrt(mu), mu = n/2^N
        w = Fraction(c * c, 1 << (2 * N)) / Fraction(n, 1 << N)
        for i in range(N):
            if (S >> i) & 1:
                out[i] += w
    return out


def rel_fourier(A, N):
    """Rel(A) from the Fourier support: i is relevant iff some S containing i
    has a nonzero coefficient.  Independent of (P2)."""
    pts = [m for m in range(1 << N) if (A >> m) & 1]
    R = set()
    for S in range(1 << N):
        c = 0
        for m in pts:
            c += -1 if popcount(S & m) & 1 else 1
        if c:
            for i in range(N):
                if (S >> i) & 1:
                    R.add(i)
    return sorted(R)


def pi_rel(A, B, N, fourier=False):
    """exact Fraction pi_Rel(A,B) and the shared-relevant set S."""
    if fourier:
        IA, IB = influences_fourier(A, N), influences_fourier(B, N)
        RA = [i for i in range(N) if IA[i] > 0]
        RB = [i for i in range(N) if IB[i] > 0]
    else:
        IA, IB = influences(A, N), influences(B, N)
        RA = [i for i in range(N) if IA[i] > 0]
        RB = [i for i in range(N) if IB[i] > 0]
    S = sorted(set(RA) & set(RB))
    return sum((IA[i] + IB[i] for i in S), Fraction(0)), S


def pi_rel_int(A, B, N):
    """all-integer form: (Num, Den) with pi_Rel = Num/Den, Den = 2|A||B|."""
    bA, bB = bcounts(A, N), bcounts(B, N)
    nA, nB = popcount(A), popcount(B)
    Num = sum(bA[i] * nB + bB[i] * nA for i in range(N)
              if bA[i] > 0 and bB[i] > 0)
    return Num, 2 * nA * nB


def degree(A, N):
    """exact degree of the {0,1}-valued indicator 1_A."""
    pts = [m for m in range(1 << N) if (A >> m) & 1]
    deg = 0
    for S in range(1 << N):
        c = 0
        for m in pts:
            c += -1 if popcount(S & m) & 1 else 1
        if c:
            deg = max(deg, popcount(S))
    return deg


# --------------------------------------------------- shadow / measure reduction

def shadow_measure(A, N, S):
    """The fibre-mass distribution nu_A on {+-1}^S:
       nu(y) = |A_y| / |A|,  y in {+-1}^S  (indexed by the S-bits, compressed).
    Returns (list of Fractions of length 2^|S|, support bitmask)."""
    S = list(S)
    m = len(S)
    cnt = [0] * (1 << m)
    n = 0
    for p in range(1 << N):
        if (A >> p) & 1:
            y = 0
            for j, i in enumerate(S):
                if (p >> i) & 1:
                    y |= 1 << j
            cnt[y] += 1
            n += 1
    nu = [Fraction(c, n) for c in cnt]
    supp = 0
    for y, c in enumerate(cnt):
        if c:
            supp |= 1 << y
    return nu, supp


def Dvec(nu, m):
    """D_i(nu) = (1/2) sum_y |nu(y)-nu(y^{+i})| = sum_y (nu(y)-nu(y^{+i}))_+ ."""
    out = []
    for i in range(m):
        s = 1 << i
        t = Fraction(0)
        for y in range(1 << m):
            d = nu[y] - nu[y ^ s]
            if d > 0:
                t += d
        out.append(t)
    return out


def tv_to_uniform(nu, m):
    U = Fraction(1, 1 << m)
    return sum((x - U for x in nu if x > U), Fraction(0))


# ----------------------------------------------------------- numpy vector API

def flip_arrays(N):
    """masks/shifts implementing the point-permutation m -> m XOR 2^i on a
    uint64 bitmask over 2^N points (N <= 6)."""
    out = []
    for i in range(N):
        s = 1 << i
        Am = 0
        for m in range(1 << N):
            if not ((m >> i) & 1):
                Am |= 1 << m
        out.append((np.uint64(Am), np.uint64(s)))
    return out


def bvec_np(P, N, fl=None):
    """b_i for a uint64 array of masks; int64 (len(P), N)."""
    fl = fl if fl is not None else flip_arrays(N)
    P = np.asarray(P, dtype=np.uint64)
    out = np.empty((len(P), N), dtype=np.int64)
    for i, (Am, s) in enumerate(fl):
        F = ((P & Am) << s) | ((P >> s) & Am)
        out[:, i] = np.bitwise_count(P & ~F).astype(np.int64)
    return out


def subsets_of_mask(mask, N):
    """all submasks of `mask` (uint64 array), by doubling."""
    arr = np.zeros(1, dtype=np.uint64)
    for p in range(1 << N):
        if (mask >> p) & 1:
            arr = np.concatenate([arr, arr | np.uint64(1 << p)])
    return arr
