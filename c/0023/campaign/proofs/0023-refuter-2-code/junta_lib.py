"""
junta_lib.py -- rung R1 (I01) machinery: normalized cylinder-pattern
indicators over Z_2.

CLASS (I01): f = 1_A / ||1_A||_2 with A = {x in {+-1}^N : x_J in P},
J subseteq [N], |J| <= d, P a nonempty subset of {+-1}^J.

REPRESENTATION.  A class function is JFun(window, pat):
  window : sorted tuple of coordinate indices (global names, any hashables)
  pat    : frozenset of ints in [0, 2^k), k = len(window); bit b of a mask
           encodes the value of coordinate window[b]  (0 -> +1, 1 -> -1).

EXACT FACTS USED (verified by t1_formula_and_lemmaA.py):

  (F1) influence formula:  Inf_i(f) = b_i(P) / (2 |P|)  for i = window[b],
       where b_i(P) = #{m in P : m XOR (1<<b) not in P} = number of
       direction-b boundary edges of P inside the window cube.
       (Cross-checked against the Fourier definition Inf_i = sum_{S ni i}
       fhat(S)^2 with exact integer Walsh-Hadamard.)

  (F2) disjointness:  supp(f) cap supp(g) = emptyset  <=>  the projections
       of the two patterns to the shared window S = J_f cap J_g are
       disjoint subsets of {+-1}^S.  In particular S = emptyset forces
       intersection (both patterns nonempty).

  (F3) payment lemma (candidate; exhaustively verified small, sampled
       large):  for any S subseteq J,
           sum_{i in S} Inf_i(f_P)  >=  (1/2) log2( 1 / nu_P(S) ),
       nu_P(S) := |pi_S(P)| / 2^|S|.  Integer-exact form:
           2^{sum_{i in S} b_i(P)} * |pi_S(P)|^{|P|}  >=  2^{|S| |P|}.

  (F4) per-pair payment: if f, g disjoint with shared window S, then
       nu_f(S) + nu_g(S) <= 1, so nu_f nu_g <= 1/4 and
           sum_{i in S} [Inf_i(f) + Inf_i(g)]  >=  1.
       Integer-exact form:
           |Q| * sum_{i in S} b_i(P) + |P| * sum_{i in S} b_i(Q)
              >=  2 |P| |Q|.
"""

import itertools, random
from fractions import Fraction


class JFun:
    __slots__ = ("window", "pat", "k")

    def __init__(self, window, pat):
        window = tuple(window)
        assert list(window) == sorted(set(window)), "window must be sorted, distinct"
        self.window = window
        self.k = len(window)
        pat = frozenset(pat)
        assert pat, "pattern must be nonempty"
        assert all(0 <= m < (1 << self.k) for m in pat)
        self.pat = pat

    def __repr__(self):
        return f"JFun({self.window}, {sorted(self.pat)})"

    # ---- exact boundary counts and influences (F1) ----
    def bcounts(self):
        """b[b] = # direction-b boundary edges of pat, b = position in window."""
        return [sum(1 for m in self.pat if (m ^ (1 << b)) not in self.pat)
                for b in range(self.k)]

    def influences(self):
        """dict: global coordinate -> Fraction influence (exact, via F1)."""
        P = len(self.pat)
        return {self.window[b]: Fraction(c, 2 * P)
                for b, c in enumerate(self.bcounts())}

    def influences_fourier(self):
        """Exact influence via the Fourier definition (integer WH). Slow;
        for cross-checking F1 only."""
        k, P = self.k, len(self.pat)
        # c_S = sum_z 1_P(z) chi_S(z), chi_S(z) = (-1)^{|S & z|}
        out = {}
        for b in range(k):
            tot = Fraction(0)
            for S in range(1 << k):
                if not (S >> b) & 1:
                    continue
                c = sum(-1 if bin(S & m).count("1") & 1 else 1 for m in self.pat)
                tot += Fraction(c * c, (1 << k) * P)
            out[self.window[b]] = tot
        return out

    def project(self, coords):
        """Set of masks over `coords` (subset of window, sorted) hit by pat."""
        pos = [self.window.index(c) for c in coords]
        return {sum(((m >> p) & 1) << j for j, p in enumerate(pos))
                for m in self.pat}

    def density(self):
        return Fraction(len(self.pat), 1 << self.k)

    def support_mask(self, N):
        """Bitmask over points x in [0,2^N) (bit x set iff x in A); global
        coordinates must be in range(N).  Point bit i = value of coord i."""
        mask = 0
        pos = list(self.window)
        free = [i for i in range(N) if i not in self.window]
        for m in self.pat:
            base = 0
            for b, c in enumerate(pos):
                if (m >> b) & 1:
                    base |= 1 << c
            for fill in range(1 << len(free)):
                x = base
                for j, c in enumerate(free):
                    if (fill >> j) & 1:
                        x |= 1 << c
                mask |= 1 << x
        return mask


def shared(f, g):
    return tuple(sorted(set(f.window) & set(g.window)))

def disjoint(f, g):
    """Exact support-disjointness test via (F2)."""
    S = shared(f, g)
    if not S:
        return False
    return not (f.project(S) & g.project(S))

def payment_lhs(f, g):
    """Exact sum_{i in S}[Inf_i(f)+Inf_i(g)] over the shared window (Fraction)."""
    S = shared(f, g)
    If, Ig = f.influences(), g.influences()
    return sum((If[c] for c in S), Fraction(0)) + sum((Ig[c] for c in S), Fraction(0))

def payment_ok(f, g):
    """Exact check of (F4) for a disjoint pair. Returns (ok, lhs Fraction)."""
    lhs = payment_lhs(f, g)
    return lhs >= 1, lhs

def lemmaA_ok(pat, k, Spos):
    """Integer-exact check of (F3) for pattern `pat` (masks over k bits) and
    subset of window positions Spos (tuple of bit positions)."""
    P = len(pat)
    sb = 0
    for b in Spos:
        sb += sum(1 for m in pat if (m ^ (1 << b)) not in pat)
    proj = {sum(((m >> p) & 1) << j for j, p in enumerate(Spos)) for m in pat}
    # 2^{sb} * |proj|^P >= 2^{|S| P}
    return (1 << sb) * (len(proj) ** P) >= 1 << (len(Spos) * P)


# ---------------------------------------------------------------------
# Family value: for a family (list of JFun) the one-side LP
#   tau = min over prob vectors p of max_coord sum_a p_a Inf_a(coord)
# and the pair value eps(F,G) = max(tau(F), tau(G)); incompatibility is
# checked pairwise via `disjoint`.
# ---------------------------------------------------------------------

def family_coords(funs):
    s = set()
    for f in funs:
        s |= set(f.window)
    return sorted(s)

def tau_lp(funs, solver="scipy"):
    """Float LP value + weights: min_p max_i sum_a p_a I_a(i)."""
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
    c_obj = np.zeros(m + 1); c_obj[m] = 1.0
    A_eq = np.zeros((1, m + 1)); A_eq[0, :m] = 1.0
    res = linprog(c_obj, A_ub=A, b_ub=np.zeros(n), A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, None)] * m + [(None, None)], method="highs")
    if not res.success:
        raise RuntimeError("LP failed")
    return res.x[m], res.x[:m], res

def tau_dual_lower_exact(funs, w):
    """Exact lower bound on tau from rational simplex weights w (dict
    coord->Fraction, sum<=1, >=0): tau >= min_a sum_i w_i I_a(i)."""
    assert all(v >= 0 for v in w.values()) and sum(w.values()) <= 1
    best = None
    for f in funs:
        val = sum((w.get(c, Fraction(0)) * v for c, v in f.influences().items()),
                  Fraction(0))
        best = val if best is None else min(best, val)
    return best

def tau_upper_exact(funs, p):
    """Exact upper bound on tau from rational weights p (list of Fraction,
    sum=1): tau <= max_i sum_a p_a I_a(i)."""
    assert sum(p) == 1 and all(x >= 0 for x in p)
    acc = {}
    for pa, f in zip(p, funs):
        if pa == 0:
            continue
        for c, v in f.influences().items():
            acc[c] = acc.get(c, Fraction(0)) + pa * v
    return max(acc.values()) if acc else Fraction(0)

def pair_value(F, G):
    """Float eps(F,G) after checking cross-disjointness exactly."""
    for f in F:
        for g in G:
            if not disjoint(f, g):
                raise ValueError("pair not incompatible")
    tF, pF, _ = tau_lp(F)
    tG, pG, _ = tau_lp(G)
    return max(tF, tG), (tF, pF), (tG, pG)


# ---------------------------------------------------------------------
# Enumeration of the whole class at small (d, N).
# ---------------------------------------------------------------------

def all_class_functions(d, N, prune_duplicates=True):
    """All JFun with window subseteq range(N), |window| <= d, excluding the
    constant (full-support) function, which can never join an incompatible
    pair.  If prune_duplicates, keep only patterns depending on ALL window
    coordinates (others duplicate smaller-window functions)."""
    out = []
    for k in range(1, d + 1):
        for W in itertools.combinations(range(N), k):
            for bits in range(1, 1 << (1 << k)):
                pat = frozenset(m for m in range(1 << k) if (bits >> m) & 1)
                if prune_duplicates:
                    # require dependence on every window coordinate
                    if any(all((m ^ (1 << b)) in pat for m in pat)
                           for b in range(k)):
                        continue
                out.append(JFun(W, pat))
    return out


def rounded_fraction_vector(xs, max_den=1000):
    return [Fraction(x).limit_denominator(max_den) for x in xs]
