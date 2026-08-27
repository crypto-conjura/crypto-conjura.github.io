"""
pcc_lib.py -- shared machinery for the c/0023 refuter searches.

Setting (Contract c/0023): Y a finite abelian group, functions f: Y^N -> C,
Fourier basis = product characters, deg(chi) = #active coordinates,
Inf_i(f) = sum_{chi: chi_i != 0} |fhat(chi)|^2, ||f||_2 = 1 under uniform
probability measure.

STRUCTURAL REDUCTIONS USED (proved in the report, elementary):

  (R1) A pair (F, G) is incompatible  <=>  U_F := union of pointwise supports
       of f in supp(F) is disjoint from U_G.  [f(x)g(x) != 0 for some f,g,x
       iff some x lies in supp(f) cap supp(g) iff U_F cap U_G != 0.]

  (R2) Monotonicity: enlarging the allowed support set only helps, so the
       minimum over incompatible pairs of max per-coordinate average influence
       equals the minimum over PARTITIONS (A, A^c) of Y^N of
       max(tau(A), tau(A^c)).

  (R3) Decoupling + density matrices: for a fixed allowed support set A, let
       V_A = { f : deg f <= d, f == 0 outside A }  (a linear subspace).
       Distributions over unit vectors of V_A with per-coordinate average
       influence <= t  <=>  density matrices rho (PSD, trace 1, range in V_A,
       in Fourier coordinates) with tr(P_i rho) <= t for all i, where P_i is
       the diagonal projection onto characters active at i.  Hence

         tau(A) := min_{rho in D(V_A)} max_i tr(P_i rho)
                 = max_{w in simplex} lambda_min( B* (sum_i w_i P_i) B ),

       (von Neumann minimax; B = orthonormal basis of V_A in Fourier coords).
       Any explicit w gives a certified LOWER bound; any explicit mixture of
       unit vectors in V_A gives a certified UPPER bound.

  For Y = Z_2 everything can be taken real (P_i and V_A are real; the real
  part of a complex optimal rho is again feasible with the same objective).
"""

import itertools, math, random
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog


# ----------------------------------------------------------------------
# Z_2 basics.  Points and characters of {0,1}^N are bitmasks 0..2^N-1.
# chi_S(x) = (-1)^{|S & x|}.
# ----------------------------------------------------------------------

def popcount(x):
    return bin(x).count("1")

def z2_charset(N, d):
    """All characters (bitmasks) of degree <= d, sorted by (degree, value)."""
    return sorted((S for S in range(1 << N) if popcount(S) <= d),
                  key=lambda S: (popcount(S), S))

def z2_eval_matrix(N, chars):
    """E[x, j] = chi_{chars[j]}(x), integer matrix (2^N x len(chars))."""
    P = 1 << N
    E = np.empty((P, len(chars)), dtype=np.int64)
    for j, S in enumerate(chars):
        for x in range(P):
            E[x, j] = -1 if (popcount(S & x) & 1) else 1
    return E

def z2_eval_matrix_frac(N, chars):
    P = 1 << N
    return [[Fraction(-1 if (popcount(S & x) & 1) else 1) for S in chars]
            for x in range(P)]


# ----------------------------------------------------------------------
# Exact rational linear algebra (for Z_2 certifications).
# ----------------------------------------------------------------------

def frac_nullspace(rows, ncols):
    """Nullspace basis (list of Fraction vectors) of the rational matrix
    given as list-of-rows; solves rows . v = 0."""
    M = [list(r) for r in rows]
    m = len(M)
    pivots = []
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, m):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis

def frac_psd_check(M):
    """Exact PSD check of a rational symmetric matrix via pivoted LDL^T.
    Returns True iff M is positive semidefinite."""
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] for i in range(n)]
    active = list(range(n))
    while active:
        # choose a strictly positive diagonal pivot if any
        piv = None
        for i in active:
            if A[i][i] > 0:
                piv = i
                break
        if piv is None:
            # all diagonal entries <= 0: PSD iff the active block is zero
            for i in active:
                if A[i][i] < 0:
                    return False
                for j in active:
                    if A[i][j] != 0:
                        return False
            return True
        p = A[piv][piv]
        rest = [i for i in active if i != piv]
        for i in rest:
            fi = A[i][piv] / p
            for j in rest:
                A[i][j] -= fi * A[piv][j]
        active = rest
    return True


# ----------------------------------------------------------------------
# tau(A) solver:  tau = max_{w in simplex} lambda_min( sum_i w_i M_i ),
# with M_i = B* P_i B.  Kelley cutting planes + primal mixture LP.
# Works for real symmetric or complex Hermitian M_i.
# ----------------------------------------------------------------------

def tau_solver(Ms, tol=1e-9, maxit=200):
    """Ms: list of k x k Hermitian numpy arrays (one per coordinate).
    Returns (lower, upper, w, cuts, mix) with
      lower = certified-in-floats lower bound  = lambda_min(M(w)),
      upper = certified-in-floats upper bound  = mixture value,
      w     = the dual weights (simplex),
      cuts  = list of unit vectors used,
      mix   = probability weights over cuts achieving `upper`.
    lower <= tau <= upper up to numerical error.
    """
    n = len(Ms)
    k = Ms[0].shape[0]
    herm = np.iscomplexobj(Ms[0])
    # initial cuts: eigenvectors at uniform w
    w = np.ones(n) / n
    cuts = []

    def eigmin_vec(w):
        M = sum(wi * Mi for wi, Mi in zip(w, Ms))
        vals, vecs = np.linalg.eigh(M)
        return vals[0], vecs[:, 0]

    def cutvals(v):
        # r_i = v* M_i v  (real)
        return np.array([float(np.real(np.conj(v) @ (Mi @ v))) for Mi in Ms])

    lam, v = eigmin_vec(w)
    best_lower, best_w = lam, w.copy()
    cuts.append(v)
    R = [cutvals(v)]
    upper = None
    mix = None
    for _ in range(maxit):
        # LP: max t  s.t.  t <= sum_i w_i R[j][i]  for all cuts j;  w in simplex
        m = len(R)
        # vars: w_1..w_n, t   ; minimize -t
        c = np.zeros(n + 1); c[-1] = -1.0
        A_ub = np.zeros((m, n + 1))
        for j in range(m):
            A_ub[j, :n] = -R[j]
            A_ub[j, n] = 1.0
        b_ub = np.zeros(m)
        A_eq = np.zeros((1, n + 1)); A_eq[0, :n] = 1.0
        b_eq = np.array([1.0])
        bounds = [(0, None)] * n + [(None, None)]
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                      bounds=bounds, method="highs")
        if not res.success:
            break
        w = res.x[:n]
        t_outer = res.x[n]          # outer approx: >= tau
        lam, v = eigmin_vec(w)      # true value at w: <= tau
        if lam > best_lower:
            best_lower, best_w = lam, w.copy()
        cuts.append(v)
        R.append(cutvals(v))
        if t_outer - best_lower < tol:
            break
    # primal upper bound: min over mixtures p of max_i sum_j p_j R[j][i]
    m = len(R)
    # vars p_1..p_m, s ; min s ; sum_j p_j R[j][i] <= s ; p in simplex
    c = np.zeros(m + 1); c[-1] = 1.0
    A_ub = np.zeros((n, m + 1))
    for i in range(n):
        A_ub[i, :m] = [R[j][i] for j in range(m)]
        A_ub[i, m] = -1.0
    b_ub = np.zeros(n)
    A_eq = np.zeros((1, m + 1)); A_eq[0, :m] = 1.0
    b_eq = np.array([1.0])
    bounds = [(0, None)] * m + [(None, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")
    if res.success:
        upper = res.x[m]
        mix = res.x[:m]
    return best_lower, upper, best_w, cuts, mix


def z2_side_matrices(N, d, A_mask, chars=None, E=None):
    """For support set A (bitmask over points of {0,1}^N): orthonormal basis
    B of V_A in character coordinates and the matrices M_i = B^T P_i B.
    Returns (dimV, Ms, B, chars). dimV=0 => no nonzero function."""
    if chars is None:
        chars = z2_charset(N, d)
    if E is None:
        E = z2_eval_matrix(N, chars)
    P = 1 << N
    outside = [x for x in range(P) if not (A_mask >> x) & 1]
    if outside:
        C = E[outside, :].astype(float)
        # nullspace via SVD
        u, s, vt = np.linalg.svd(C)
        rank = int(np.sum(s > 1e-9 * (s[0] if len(s) else 1)))
        B = vt[rank:].T  # columns orthonormal
    else:
        B = np.eye(len(chars))
    dimV = B.shape[1]
    if dimV == 0:
        return 0, None, None, chars
    Ms = []
    for i in range(N):
        diag = np.array([1.0 if (S >> i) & 1 else 0.0 for S in chars])
        Ms.append(B.T @ (diag[:, None] * B))
    return dimV, Ms, B, chars


def z2_partition_value(N, d, A_mask, tol=1e-9):
    """max(tau(A), tau(A^c)) for the partition (A, A^c); returns
    (value_lower, value_upper) or None if a side has no nonzero function."""
    P = 1 << N
    full = (1 << P) - 1
    res = []
    for mask in (A_mask, full ^ A_mask):
        dimV, Ms, B, chars = z2_side_matrices(N, d, mask)
        if dimV == 0:
            return None
        lo, up, w, cuts, mix = tau_solver(Ms, tol=tol)
        res.append((lo, up))
    return (max(res[0][0], res[1][0]), max(res[0][1], res[1][1]))


# ----------------------------------------------------------------------
# Cube symmetry group for Z_2^N: coordinate permutations x translations.
# Acts on points; induces action on partitions (plus side swap).
# ----------------------------------------------------------------------

def z2_group_point_maps(N):
    """All |G| = 2^N * N! maps as tuples: point -> point."""
    maps = []
    P = 1 << N
    for perm in itertools.permutations(range(N)):
        # x -> permute bits
        base = []
        for x in range(P):
            y = 0
            for i in range(N):
                if (x >> i) & 1:
                    y |= 1 << perm[i]
            base.append(y)
        for t in range(P):
            maps.append(tuple(base[x] ^ t for x in range(P)))
    return maps

def z2_partition_orbit_reps(N):
    """Orbit representatives of partitions (A, A^c) of {0,1}^N under the
    group above together with the side swap. A partition is encoded as the
    bitmask of A; canonical rep = min over orbit of min(mask, complement)."""
    P = 1 << N
    full = (1 << P) - 1
    maps = z2_group_point_maps(N)
    seen = bytearray((full + 1) >> 3) if False else None
    seen = set()
    reps = []
    for A in range(1, full):  # skip empty/full
        m0 = min(A, full ^ A)
        if m0 in seen:
            continue
        # BFS orbit
        orbit = set()
        stack = [m0]
        orbit.add(m0)
        while stack:
            cur = stack.pop()
            for g in maps:
                img = 0
                x = cur
                while x:
                    b = x & (-x)
                    img |= 1 << g[b.bit_length() - 1]
                    x ^= b
                img = min(img, full ^ img)
                if img not in orbit:
                    orbit.add(img)
                    stack.append(img)
        rep = min(orbit)
        reps.append(rep)
        seen |= orbit
    return reps


# ----------------------------------------------------------------------
# Z_q basics (used for q = 3).  Points = tuples in {0..q-1}^N encoded in
# base q; characters = tuples j in {0..q-1}^N, chi_j(x) = w^{sum j_i x_i}.
# ----------------------------------------------------------------------

def zq_point(x, N, q):
    return tuple((x // q**i) % q for i in range(N))

def zq_charset(N, q, d):
    chars = []
    for j in range(q**N):
        t = zq_point(j, N, q)
        if sum(1 for a in t if a != 0) <= d:
            chars.append(t)
    chars.sort(key=lambda t: (sum(1 for a in t if a != 0), t))
    return chars

def zq_eval_matrix(N, q, chars):
    w = np.exp(2j * np.pi / q)
    P = q**N
    E = np.empty((P, len(chars)), dtype=complex)
    for xi in range(P):
        x = zq_point(xi, N, q)
        for jj, t in enumerate(chars):
            E[xi, jj] = w ** (sum(a * b for a, b in zip(t, x)) % q)
    return E

def zq_side_matrices(N, q, d, A_set, chars=None, E=None):
    if chars is None:
        chars = zq_charset(N, q, d)
    if E is None:
        E = zq_eval_matrix(N, q, chars)
    P = q**N
    outside = [x for x in range(P) if x not in A_set]
    if outside:
        C = E[outside, :]
        u, s, vt = np.linalg.svd(C)
        rank = int(np.sum(s > 1e-9 * (s[0] if len(s) else 1)))
        B = vt[rank:].conj().T
    else:
        B = np.eye(len(chars), dtype=complex)
    dimV = B.shape[1]
    if dimV == 0:
        return 0, None, None, chars
    Ms = []
    for i in range(N):
        diag = np.array([1.0 if t[i] != 0 else 0.0 for t in chars])
        Ms.append(B.conj().T @ (diag[:, None] * B))
    return dimV, Ms, B, chars
