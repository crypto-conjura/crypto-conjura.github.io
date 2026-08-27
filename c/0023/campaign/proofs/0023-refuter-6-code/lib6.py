"""
lib6.py -- exact machinery for MINIMAL vs MINIMUM certificates of degree-<=d
sets over Z_2.  Artifact 0023-refuter-6 (gap [G5] of 0023-prover-3-r3 §7.4).

REPRESENTATION.  A set ("pattern") on r coordinates is a boolean numpy array A
of length 2^r; point m in {0,..,2^r-1} encodes coordinate i by bit i of m,
with bit 0 -> +1 and bit 1 -> -1 (same convention as
../0023-refuter-4-code/lib4.py and ../0023-prover-3-r2-code/check_min_certificates.py).

DEFINITIONS (verbatim from 0023-prover-3-r3 §7.4).
  For x in A, S subseteq [r] is a CERTIFICATE of x if every y with y_S = x_S
  lies in A.  It is MINIMAL if no proper subset is a certificate, and MINIMUM
  if it has least size among all certificates of x.

GENERIC METHOD (no structural input at all).  For every mask S let
  cert[S][m] = 1  iff  { y : y & S == m & S } subseteq A.
cert[full] = A and cert[S \ {i}][m] = cert[S][m] AND cert[S][m ^ 2^i]; the
recursion is exact and cert[S][m] depends only on m & S.  Then S is a minimal
certificate of m iff cert[S][m] and NOT cert[S ^ 2^i][m] for every i in S.
Cost 2^r masks x 2^r points booleans: r <= 12 comfortably.

Everything numeric is integer or Fraction; no floating point enters a claim.
"""

import numpy as np
from fractions import Fraction as F
from itertools import combinations


# ----------------------------------------------------------------- transforms

def wht_int(v):
    """in-place-safe integer Walsh-Hadamard transform of a list of ints."""
    v = list(v)
    n = len(v)
    h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x, y = v[j], v[j + h]
                v[j], v[j + h] = x + y, x - y
        h *= 2
    return v


def degree_of(A, r):
    """exact degree of the {0,1}-indicator's multilinear expansion (0 if constant)."""
    tt = [int(b) for b in A]
    g = wht_int(tt)
    deg = 0
    for S, c in enumerate(g):
        if c:
            deg = max(deg, bin(S).count("1"))
    return deg


def influences_exact(A, r):
    """exact Fractions Inf_i(f_A), f_A = 1_A / ||1_A||_2, from the Fourier
    definition with an integer Walsh-Hadamard transform."""
    tt = [int(b) for b in A]
    n = sum(tt)
    if n == 0:
        return [F(0)] * r
    g = wht_int(tt)                      # g[S] = 2^r * hat(1_A)(S)
    acc = [F(0)] * r
    for S, c in enumerate(g):
        if not c:
            continue
        w = F(c * c, 1 << (2 * r))       # hat(1_A)(S)^2
        for i in range(r):
            if (S >> i) & 1:
                acc[i] += w
    alpha = F(n, 1 << r)
    return [a / alpha for a in acc]


# --------------------------------------------------- generic certificate table

def cert_table(A, r):
    """boolean array C of shape (2^r, 2^r): C[S, m] = 1 iff the subcube
    {y : y&S == m&S} is contained in A.   Fully generic; no structure used."""
    n = 1 << r
    C = np.zeros((n, n), dtype=bool)
    full = n - 1
    C[full] = A
    # process masks in decreasing popcount so that S|2^i is ready before S
    order = sorted(range(n), key=lambda S: -bin(S).count("1"))
    idx = np.arange(n)
    perm = [idx ^ (1 << i) for i in range(r)]
    for S in order:
        if S == full:
            continue
        # pick some i not in S
        i = (~S & full).bit_length() - 1
        S2 = S | (1 << i)
        C[S] = C[S2] & C[S2][perm[i]]
    return C


def minimal_certs_generic(A, r, C=None):
    """dict point -> list of minimal-certificate masks (generic brute force)."""
    if C is None:
        C = cert_table(A, r)
    n = 1 << r
    out = {}
    pts = [m for m in range(n) if A[m]]
    for m in pts:
        lst = []
        for S in range(n):
            if not C[S, m]:
                continue
            ok = True
            i = 0
            SS = S
            while SS:
                if SS & 1:
                    if C[S ^ (1 << i), m]:
                        ok = False
                        break
                SS >>= 1
                i += 1
            if ok:
                lst.append(S)
        out[m] = lst
    return out


def minimal_certs_bruteforce_point(A, r, m):
    """INDEPENDENT slow check for one point: enumerate all subsets, test the
    certificate property directly by scanning the subcube, then filter minimal.
    Used only to cross-check cert_table()."""
    n = 1 << r
    certs = []
    for S in range(n):
        good = True
        free = (~S) & (n - 1)
        # enumerate submasks of free
        v = free
        while True:
            if not A[(m & S) | v]:
                good = False
                break
            if v == 0:
                break
            v = (v - 1) & free
        if good:
            certs.append(S)
    cs = set(certs)
    return [S for S in certs
            if all((S ^ (1 << i)) not in cs for i in range(r) if (S >> i) & 1)]


# ------------------------------------------------------------ selection rules

def size(S):
    return bin(S).count("1")


def tuple_of(S, r):
    return tuple(i for i in range(r) if (S >> i) & 1)


def selection_stats(mincerts, r):
    """exact Fractions for the expected window size, x ~ Unif(A), under:
      MIN  : any minimum-size minimal certificate      (= min size)
      MAX  : the largest minimal certificate           (adversarial)
      UNIF : uniform among ALL minimal certificates
      LEXF : lexicographically first (sorted index tuple, Python order)
      LEXL : lexicographically last
    Also returns the exact multiset distribution of minimal-certificate sizes
    (counted over all (point, minimal certificate) pairs) and the per-point
    multiplicity distribution.
    """
    pts = sorted(mincerts)
    npts = len(pts)
    tot = {k: F(0) for k in ("MIN", "MAX", "UNIF", "LEXF", "LEXL")}
    size_multiset = {}
    mult_hist = {}
    per_point_max = {}
    for m in pts:
        lst = mincerts[m]
        sizes = [size(S) for S in lst]
        tot["MIN"] += F(min(sizes))
        tot["MAX"] += F(max(sizes))
        tot["UNIF"] += F(sum(sizes), len(sizes))
        tf = min(lst, key=lambda S: tuple_of(S, r))
        tl = max(lst, key=lambda S: tuple_of(S, r))
        tot["LEXF"] += F(size(tf))
        tot["LEXL"] += F(size(tl))
        for s in sizes:
            size_multiset[s] = size_multiset.get(s, 0) + 1
        mult_hist[len(lst)] = mult_hist.get(len(lst), 0) + 1
        per_point_max[max(sizes)] = per_point_max.get(max(sizes), 0) + 1
    exp = {k: v / npts for k, v in tot.items()}
    return exp, size_multiset, mult_hist, per_point_max, npts


def greedy_shrink(A, r, m, order, C=None):
    """the natural algorithmic minimal certificate: start from [r] and delete
    coordinates in the given order whenever the result is still a certificate.
    Returns the mask.  (Any greedy shrink lands on a MINIMAL certificate.)"""
    if C is None:
        C = cert_table(A, r)
    S = (1 << r) - 1
    for i in order:
        T = S & ~(1 << i)
        if C[T, m]:
            S = T
    return S
