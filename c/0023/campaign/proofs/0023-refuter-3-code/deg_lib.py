"""
deg_lib.py -- rung R2 (I02) machinery: normalized indicators of degree-<=d
SETS over Z_2.

CLASS (I02):  f = 1_A / ||1_A||_2 ,  A subseteq {+-1}^N nonempty,
              deg(1_A) <= d   (degree of the {0,1}-valued indicator).

STRUCTURE FACT (proved elementarily in the report, verified here):
  every degree-<=d set is a JUNTA on at most d 2^{d-1} coordinates, so the
  class is exactly the set of cylinders over degree-<=d patterns
  P subseteq {+-1}^J with |J| <= M(d).  Hence we can reuse the R1
  representation JFun(window, pat) from ../0023-refuter-2-code/junta_lib.py
  and its exact machinery (F1) influence formula, (F2) disjointness =
  projection disjointness, (F3)/(F4) payment lemmas.

  The ONLY difference from R1 is the admissible pattern set: R1 allowed all
  nonempty P with |J| <= d; R2 allows all nonempty P with deg(1_P) <= d and
  |J| unrestricted (but automatically <= M(d)).

DEGREE TEST.  For P subseteq {0,..,2^k-1}, the multilinear coefficient of
chi_S is 2^{-k} sum_{m in P} (-1)^{|S&m|}; deg(1_P) <= d iff that integer
sum vanishes for every S with |S| > d.
"""

import itertools, sys, os
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "0023-refuter-2-code"))
sys.path.insert(0, os.path.join(_HERE, "..", "0023-refuter-1-code"))

from junta_lib import (JFun, shared, disjoint, payment_lhs, payment_ok,
                       tau_lp, tau_dual_lower_exact, tau_upper_exact,
                       family_coords)


def popcount(x):
    return bin(x).count("1")


def walsh_int(pat, k):
    """Integer Walsh transform c_S = sum_{m in pat} (-1)^{|S & m|}, S=0..2^k-1."""
    return [sum(-1 if popcount(S & m) & 1 else 1 for m in pat)
            for S in range(1 << k)]


def pattern_degree(pat, k):
    c = walsh_int(pat, k)
    return max((popcount(S) for S in range(1 << k) if c[S] != 0), default=0)


def genuine(pat, k):
    """True iff the pattern depends on every one of the k window coordinates."""
    for b in range(k):
        if all((m ^ (1 << b)) in pat for m in pat):
            return False
    return True


# ---------------------------------------------------------------------
# Enumeration of degree-<=d {0,1}-valued functions on k variables, by the
# restriction recursion:  f = (g+h)/2 + x_k (g-h)/2  with g = f|_{x_k=+1},
# h = f|_{x_k=-1};  deg f <= d  iff  deg((g+h)/2) <= d and deg((g-h)/2) <= d-1.
# Since deg g, deg h <= d follows, we can build level k from level k-1.
# Patterns are frozensets of masks in [0, 2^k).
# ---------------------------------------------------------------------

def _coeffs(pat, k):
    return tuple(walsh_int(pat, k))          # 2^k integers (times 2^k)


_DEGF_CACHE = {}
_GENP_CACHE = {}


def deg_functions(k, d):
    """All P subseteq [0,2^k) with deg(1_P) <= d.  Exhaustive, exact."""
    if (k, d) in _DEGF_CACHE:
        return _DEGF_CACHE[(k, d)]
    out = _deg_functions(k, d)
    _DEGF_CACHE[(k, d)] = out
    return out


def _deg_functions(k, d):
    if k == 0:
        return [frozenset(), frozenset({0})]
    prev = deg_functions(k - 1, d)
    # precompute Walsh coefficient vectors on k-1 bits
    W = {p: _coeffs(p, k - 1) for p in prev}
    out = []
    Kp = 1 << (k - 1)
    hi = [S for S in range(Kp) if popcount(S) > d - 1]   # must vanish in g-h
    for g in prev:
        cg = W[g]
        for h in prev:
            ch = W[h]
            ok = True
            for S in hi:
                if cg[S] - ch[S] != 0:
                    ok = False
                    break
            if not ok:
                continue
            # (g+h)/2 automatically has degree <= d since deg g, deg h <= d
            out.append(frozenset(g) | frozenset(m | Kp for m in h))
    return out


def genuine_patterns(k, d):
    """Degree-<=d patterns on exactly k variables that depend on all of them,
    nonempty and not the full cube."""
    if (k, d) in _GENP_CACHE:
        return _GENP_CACHE[(k, d)]
    res = []
    for p in deg_functions(k, d):
        if not p or len(p) == (1 << k):
            continue
        if genuine(p, k):
            res.append(p)
    _GENP_CACHE[(k, d)] = res
    return res


# ---------------------------------------------------------------------
# The R2 class on N coordinates.
# ---------------------------------------------------------------------

def class_functions(N, d, maxwin=None):
    """All JFun(window, pat) with window subseteq range(N), pattern of degree
    <= d, depending on all window coordinates, nonempty, not the full cube.
    maxwin defaults to the junta bound d*2^(d-1)."""
    if maxwin is None:
        maxwin = min(N, d * (1 << (d - 1)))
    out = []
    for k in range(1, min(N, maxwin) + 1):
        pats = genuine_patterns(k, d)
        if not pats:
            continue
        for W in itertools.combinations(range(N), k):
            for p in pats:
                out.append(JFun(W, p))
    return out


def total_influence(f):
    return sum(f.influences().values(), Fraction(0))


def max_influence(f):
    return max(f.influences().values())


# ---------------------------------------------------------------------
# One-side value tau(family) with EXACT certificates.
#   tau(fam) = min over prob vectors p of max_i sum_a p_a Inf_i(f_a)
# Lower bound certificate: rational w in simplex with
#   min_a sum_i w_i Inf_i(f_a) = q   ==>  tau >= q.
# Upper bound certificate: rational mixture p with max_i ... = q  ==> tau <= q.
# ---------------------------------------------------------------------

def tau_exact(funs, max_den=5040):
    """Float LP, then rationalised two-sided certificates.
    Returns (lo, hi, w, p) with lo, hi Fractions and lo <= tau <= hi."""
    import numpy as np
    from scipy.optimize import linprog
    coords = family_coords(funs)
    ci = {c: j for j, c in enumerate(coords)}
    n, m = len(coords), len(funs)
    A = np.zeros((n, m + 1))
    for a, f in enumerate(funs):
        for c, v in f.influences().items():
            A[ci[c], a] = float(v)
    A[:, m] = -1.0
    cobj = np.zeros(m + 1); cobj[m] = 1.0
    Aeq = np.zeros((1, m + 1)); Aeq[0, :m] = 1.0
    res = linprog(cobj, A_ub=A, b_ub=np.zeros(n), A_eq=Aeq, b_eq=[1.0],
                  bounds=[(0, None)] * m + [(None, None)], method="highs")
    if not res.success:
        raise RuntimeError("LP failed")
    # upper: rationalise primal mixture
    p = [Fraction(x).limit_denominator(max_den) for x in res.x[:m]]
    s = sum(p)
    if s == 0:
        p = [Fraction(1, m)] * m
    else:
        p = [x / s for x in p]
    hi = tau_upper_exact(funs, p)
    # lower: rationalise dual weights (marginals of the coordinate constraints)
    y = getattr(res, "ineqlin", None)
    if y is not None and y.marginals is not None:
        wf = [-t for t in y.marginals]
    else:
        wf = [1.0] * n
    tot = sum(wf)
    if tot <= 0:
        wf = [1.0] * n; tot = float(n)
    w = {coords[j]: Fraction(wf[j] / tot).limit_denominator(max_den)
         for j in range(n)}
    sw = sum(w.values())
    if sw > 1:
        w = {c: v / sw for c, v in w.items()}
    lo = tau_dual_lower_exact(funs, w)
    return lo, hi, w, p


def tau_float(funs):
    return tau_lp(funs)[0]
