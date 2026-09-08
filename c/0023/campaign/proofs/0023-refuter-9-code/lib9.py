"""
lib9.py -- window / fibre machinery for lambda (artifact 0023-refuter-9).

Reuses the exact bitmask machinery of ../0023-refuter-8-code/lib8.py
(sets are python ints over the 2^N points; bit m set iff point m in the set;
bit i of m encodes coordinate i, 0 -> +1, 1 -> -1).

DEFINITIONS (0023-analysis-1 (dagger)).  For A subseteq {+-1}^N and a window
W subseteq [N]:
    alpha_w = |A_w| / 2^{|W|}   for w in {+-1}^{[N]\\W}  (A_w = trace on W)
    lam(A,W) = E_w[ min(alpha_w, 1-alpha_w) ] / alpha.

ADMISSIBLE WINDOWS (0023-analysis-1 S1, "route 2 sets W = W_A u W_B"):
W_A is a *projection-defect set*: |W_A| <= d and A_w =/= empty for every
w in {+-1}^{[N]\\W_A}.  Any superset of a defect set is a defect set, and any
defect set can be shrunk to one inside the relevant coordinates of A, so the
minimal defect sets live inside rel(A).
"""
import sys, os, itertools
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "0023-refuter-8-code"))
from lib8 import (popcount, points, spectrum, degree_and_tops, inf_fourier,
                  inf_boundary, from_pred, subcube, complement, cube_all, fmt)


# ---------------------------------------------------------------- fibres

def fibre_counts(A, N, W):
    """list of |A_w| indexed by w in {+-1}^{[N]\\W} (integers, exact)."""
    Wl = sorted(W)
    rest = [i for i in range(N) if i not in set(Wl)]
    cnt = [0] * (1 << len(rest))
    for m in points(A, N):
        z = 0
        for j, i in enumerate(rest):
            if (m >> i) & 1:
                z |= 1 << j
        cnt[z] += 1
    return cnt


def lam(A, N, W):
    """exact Fraction lam(A,W); raises on empty A."""
    nA = popcount(A)
    assert nA > 0
    cnt = fibre_counts(A, N, W)
    dW = 1 << len(W)
    tot = 0                      # sum over w of min(|A_w|, 2^{|W|}-|A_w|)
    for c in cnt:
        tot += c if 2 * c <= dW else dW - c
    # E_w[min] = tot / (len(cnt) * dW) ;  alpha = nA / 2^N = nA/(len(cnt)*dW)
    return F(tot, nA)


def E_min(A, N, W):
    nA = popcount(A)
    cnt = fibre_counts(A, N, W)
    dW = 1 << len(W)
    tot = sum(c if 2 * c <= dW else dW - c for c in cnt)
    return F(tot, len(cnt) * dW)


def fibre_profile(A, N, W):
    """dict {alpha_w : multiplicity} exact."""
    cnt = fibre_counts(A, N, W)
    dW = 1 << len(W)
    out = {}
    for c in cnt:
        a = F(c, dW)
        out[a] = out.get(a, 0) + 1
    return out


# ------------------------------------------------------- defect windows

def is_defect_set(A, N, W):
    """True iff every fibre over [N]\\W meets A (S7b projection property)."""
    return all(c > 0 for c in fibre_counts(A, N, W))


def relevant(A, N):
    """coordinates i with Inf_i(1_A) > 0."""
    return [i for i, v in enumerate(inf_fourier(A, N)) if v > 0]


def minimal_defect_sets(A, N, d):
    """all inclusion-minimal defect sets of size <= d, inside rel(A)."""
    R = relevant(A, N)
    out = []
    for k in range(0, min(d, len(R)) + 1):
        for W in itertools.combinations(R, k):
            Ws = set(W)
            if any(set(m) <= Ws for m in out):
                continue
            if is_defect_set(A, N, W):
                out.append(tuple(sorted(W)))
        if out and k == 0:
            break
    return out


def admissible_windows(A, B, N, d):
    """{W_A u W_B} over minimal defect sets of A and of B (the literal rule of
    0023-analysis-1 S1).  Returns a sorted list of frozensets."""
    DA = minimal_defect_sets(A, N, d)
    DB = minimal_defect_sets(B, N, d)
    out = set()
    for wa in DA:
        for wb in DB:
            out.add(frozenset(wa) | frozenset(wb))
    return sorted(out, key=lambda s: (len(s), sorted(s)))


# ------------------------------------------------------------- reporting

def deg(A, N):
    return degree_and_tops(A, N)[0]


def alpha(A, N):
    return F(popcount(A), 1 << N)


def maxinf_rel(A, N):
    """max_i Inf_i(f_A) = max_i Inf_i(1_A)/alpha  (lib8 already normalises)."""
    return max(inf_fourier(A, N))
