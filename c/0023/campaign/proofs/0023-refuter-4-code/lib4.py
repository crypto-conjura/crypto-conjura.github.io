"""
lib4.py -- fast exact machinery for degree-<=3 SETS on k<=6 coordinates,
rung R2 / I02, refuter cycle 3 (artifact 0023-refuter-4).

REPRESENTATION.  A "pattern" on k coordinates is a subset P of the window cube
{0,..,2^k-1}, stored as a uint64 BITMASK over the 2^k points (bit m set iff
m in P).  Bit b of a point m encodes coordinate b (0 -> +1, 1 -> -1), the same
convention as ../0023-refuter-2-code/junta_lib.py.

EXACT FACTS USED (each re-derived, no citation).

 (E1) boundary counts.  b_i(P) = #{m in P : m XOR 2^i not in P}.
      Inf_i(1_P) = b_i / 2^(k+1),   Inf_i(f_P) = b_i / (2|P|)   [(F1) of R1],
      and for the +-1-valued h = 2*1_P - 1,  Inf_i(h) = b_i / 2^(k-1).

 (E2) degree test / restriction recursion.  Splitting on coordinate k-1,
      P = g | (h << 2^(k-1)) with g,h patterns on k-1 coordinates, one has
      deg(1_P) <= 3  iff  deg(1_g), deg(1_h) <= 3 AND the degree-exactly-3
      integer Walsh coefficients of g and h COINCIDE.  (f = (g+h)/2 +
      x_k (g-h)/2; the second part must have degree <= 2.)

 (E3) influence floor.  For deg(1_P) <= 3 and i relevant, d_i 1_P is a nonzero
      {0,+-1/2}-valued multilinear polynomial of degree <= 2, hence nonzero on
      at least a 2^-2 fraction of the cube, hence
          Inf_i(h) >= 1/4,  i.e.  b_i >= 2^(k-3).
      (Verified exhaustively for k <= 5 in r1a.)

 (E4) cheapness.  Call P CHEAP iff every relevant influence of the normalized
      indicator is < 1/6 = 1/(2d):  b_i < |P|/3 for all i.  By (E3) a cheap
      genuine pattern has |P| > 3*2^(k-3) = (3/8) 2^k.
"""

import numpy as np
from fractions import Fraction

# ---------------------------------------------------------------- bit helpers

def flip_arrays(k):
    """A_i (uint64) and shift s_i = 2^i so that
       flip_i(P) = ((P & A_i) << s_i) | ((P >> s_i) & A_i)
    permutes the 2^k point-bits by m -> m XOR 2^i."""
    out = []
    for i in range(k):
        s = 1 << i
        A = 0
        for m in range(1 << k):
            if not ((m >> i) & 1):
                A |= 1 << m
        out.append((np.uint64(A), np.uint64(s)))
    return out


def popcnt(x):
    return np.bitwise_count(x).astype(np.int64)


def bvec(P, k, fl=None):
    """b_i for an array P of uint64 masks; returns int64 array (len(P), k)."""
    fl = fl or flip_arrays(k)
    P = np.asarray(P, dtype=np.uint64)
    out = np.empty((len(P), k), dtype=np.int64)
    for i, (A, s) in enumerate(fl):
        F = ((P & A) << s) | ((P >> s) & A)
        out[:, i] = popcnt(P & ~F)
    return out


def walsh_key_arrays(k, sizes=(3,)):
    """For every S subseteq [k] with |S| in sizes, the pair of uint64 masks
    (even, odd) of points m with popcount(S&m) even / odd.  Then
    c_S(P) = popcount(P & even) - popcount(P & odd)."""
    out = []
    for S in range(1 << k):
        if bin(S).count("1") not in sizes:
            continue
        ev = od = 0
        for m in range(1 << k):
            if bin(S & m).count("1") & 1:
                od |= 1 << m
            else:
                ev |= 1 << m
        out.append((S, np.uint64(ev), np.uint64(od)))
    return out


def coeffs(P, k, sizes=(3,)):
    """integer Walsh coefficients c_S for |S| in sizes; (len(P), nS) int64."""
    W = walsh_key_arrays(k, sizes)
    P = np.asarray(P, dtype=np.uint64)
    out = np.empty((len(P), len(W)), dtype=np.int64)
    for j, (S, ev, od) in enumerate(W):
        out[:, j] = popcnt(P & ev) - popcnt(P & od)
    return out


def max_degree(P, k):
    """exact degree of 1_P for a single python-int mask (0 if constant)."""
    deg = 0
    for S in range(1 << k):
        ev = od = 0
        for m in range(1 << k):
            if (P >> m) & 1:
                if bin(S & m).count("1") & 1:
                    od += 1
                else:
                    ev += 1
        if ev - od != 0:
            deg = max(deg, bin(S).count("1"))
    return deg


# --------------------------------------------------- level-by-level build-up

def level3_all():
    """all 256 patterns on 3 coordinates (every one has degree <= 3)."""
    return np.arange(256, dtype=np.uint64)


def next_level(P, k):
    """From ALL degree-<=3 patterns P on k coordinates, produce all degree-<=3
    patterns on k+1 coordinates (masks over 2^(k+1) points).  Uses (E2):
    group by the degree-exactly-3 coefficient vector, then take every ordered
    pair inside a group."""
    C = coeffs(P, k, sizes=(3,))
    order = np.lexsort(C.T[::-1])
    Cs, Ps = C[order], P[order]
    # group boundaries
    if len(Cs) == 0:
        return np.zeros(0, dtype=np.uint64)
    newrow = np.ones(len(Cs), dtype=bool)
    newrow[1:] = np.any(Cs[1:] != Cs[:-1], axis=1)
    starts = np.flatnonzero(newrow)
    ends = np.append(starts[1:], len(Cs))
    shift = np.uint64(1 << k)
    chunks = []
    for a, b in zip(starts, ends):
        blk = Ps[a:b]
        m = len(blk)
        G = np.repeat(blk, m)
        H = np.tile(blk, m)
        chunks.append(G | (H << shift))
    return np.concatenate(chunks)


def group_by_key(P, k, sizes=(3,)):
    """dict: bytes(key) -> np.array of indices, key = deg-exactly-3 coeffs."""
    C = coeffs(P, k, sizes=sizes)
    order = np.lexsort(C.T[::-1])
    Cs = C[order]
    newrow = np.ones(len(Cs), dtype=bool)
    newrow[1:] = np.any(Cs[1:] != Cs[:-1], axis=1)
    starts = np.flatnonzero(newrow)
    ends = np.append(starts[1:], len(Cs))
    return [order[a:b] for a, b in zip(starts, ends)]


# ------------------------------------------------------------ exact influences

def influences(Pmask, k):
    """exact Fractions Inf_i(f_P) for a single python-int mask."""
    n = bin(Pmask).count("1")
    out = []
    for i in range(k):
        s = 1 << i
        b = 0
        for m in range(1 << k):
            if (Pmask >> m) & 1 and not ((Pmask >> (m ^ s)) & 1):
                b += 1
        out.append(Fraction(b, 2 * n) if n else Fraction(0))
    return out


def influences_fourier(Pmask, k):
    """exact Inf_i(f_P) from the FOURIER DEFINITION, integer Walsh transform:
    Inf_i(f) = sum_{S ni i} fhat(S)^2 with f = 1_P/||1_P||_2.
    Independent of (E1)/bcounts -- used to double-check every hit."""
    pts = [m for m in range(1 << k) if (Pmask >> m) & 1]
    n = len(pts)
    out = [Fraction(0)] * k
    for S in range(1 << k):
        c = 0
        for m in pts:
            c += -1 if bin(S & m).count("1") & 1 else 1
        if c == 0:
            continue
        # 1_P hat(S) = c / 2^k ; f = 1_P / sqrt(mu) ; mu = n/2^k
        w = Fraction(c * c, (1 << (2 * k))) / Fraction(n, 1 << k)
        for i in range(k):
            if (S >> i) & 1:
                out[i] += w
    return out
