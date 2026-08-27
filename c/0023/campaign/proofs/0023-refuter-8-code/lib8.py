"""
lib8.py -- exact machinery for the GAP-3 hunt (artifact 0023-refuter-8).

QUANTITIES.  For cross-disjoint nonempty A,B subseteq {+-1}^N of degree <= d,
f_A = 1_A/||1_A||_2, alpha = |A|/2^N:

    Q(A,B)      := max_i min( Inf_i(f_A), Inf_i(f_B) )      -- the GAP-3 target
    pi_M(A,B)   := sum_{i in M(B)} Inf_i(f_A) + sum_{i in M(A)} Inf_i(f_B)
                                                            -- monomial payment
    pi_tau(A,B) := sum_{i in W_tau(B)} Inf_i(f_A) + sum_{i in W_tau(A)} Inf_i(f_B)
                   with W_tau(X) = { i : Inf_i(f_X) >= tau }.

REPRESENTATION.  A set is a python int BITMASK over the 2^N points; bit m set
iff point m is in the set.  Bit b of m encodes coordinate b (0 -> +1, 1 -> -1).
Same convention as ../0023-refuter-5-code/lib5.py.

TWO INDEPENDENT INFLUENCE ROUTES (both exact, over Fraction / int):
  (M1) boundary route:  Inf_i(f_A) = b_i(A) / (2|A|), b_i = #{x in A : x^{+i} notin A}
  (M2) Fourier route:   integer fast Walsh-Hadamard transform of 1_A, then
                        Inf_i(f_A) = (sum_{S ni i} c_S^2) / (2^N |A|)  with
                        c_S = sum_x 1_A(x) chi_S(x) in Z  (since 1_A^(S)=c_S/2^N
                        and ||f_A||^2 normalisation divides by alpha = |A|/2^N).
(M2) also gives the exact degree and ALL maximum-degree supports.
"""

from fractions import Fraction
import itertools


# ---------------------------------------------------------------- basic

def popcount(x):
    return bin(x).count("1")


def points(A, N):
    return [m for m in range(1 << N) if (A >> m) & 1]


# ------------------------------------------------- (M1) boundary route

def bcounts(A, N):
    """b_i(A) = #{x in A : x^{+i} not in A}, for i = 0..N-1."""
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


def inf_boundary(A, N):
    n = popcount(A)
    if n == 0:
        raise ValueError("empty set")
    return [Fraction(b, 2 * n) for b in bcounts(A, N)]


# -------------------------------------------------- (M2) Fourier route

def fwht(vec):
    """in-place integer fast Walsh-Hadamard transform (natural/Hadamard order).
    Returns c[S] = sum_m vec[m] * (-1)^{popcount(S & m)}."""
    a = list(vec)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, h << 1):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j] = x + y
                a[j + h] = x - y
        h <<= 1
    return a


def spectrum(A, N):
    """integer Walsh coefficients c_S of the {0,1} indicator 1_A."""
    v = [(A >> m) & 1 for m in range(1 << N)]
    return fwht(v)


def inf_fourier(A, N, c=None):
    """Inf_i(f_A) via the Fourier definition, exact Fractions."""
    if c is None:
        c = spectrum(A, N)
    n = popcount(A)
    num = [0] * N
    for S in range(1 << N):
        cs = c[S]
        if cs == 0:
            continue
        w = cs * cs
        s = S
        while s:
            low = s & -s
            num[low.bit_length() - 1] += w
            s ^= low
    den = (1 << N) * n
    return [Fraction(x, den) for x in num]


def degree_and_tops(A, N, c=None):
    """(deg(1_A), list of ALL maximum-degree supports as frozensets)."""
    if c is None:
        c = spectrum(A, N)
    deg = 0
    tops = []
    for S in range(1 << N):
        if c[S] == 0:
            continue
        k = popcount(S)
        if k > deg:
            deg, tops = k, [S]
        elif k == deg and deg > 0:
            tops.append(S)
    if deg == 0:
        return 0, []
    return deg, [frozenset(i for i in range(N) if (S >> i) & 1) for S in tops]


# ------------------------------------------------------------- payments

def Qval(IA, IB):
    """max_i min(Inf_i(f_A), Inf_i(f_B)) and the argmax."""
    best, arg = Fraction(0), None
    for i, (a, b) in enumerate(zip(IA, IB)):
        v = a if a < b else b
        if v > best:
            best, arg = v, i
    return best, arg


def pi_M(IA, IB, MA, MB):
    return (sum((IA[i] for i in MB), Fraction(0))
            + sum((IB[i] for i in MA), Fraction(0)))


def pi_tau(IA, IB, tau):
    WA = [i for i, v in enumerate(IA) if v >= tau]
    WB = [i for i, v in enumerate(IB) if v >= tau]
    return (sum((IA[i] for i in WB), Fraction(0))
            + sum((IB[i] for i in WA), Fraction(0)), WA, WB)


# --------------------------------------------------------- slice profile

def slice_densities(A, N, M):
    """multiset of a_z = |A_z| / 2^{|M|} over fibres z in {+-1}^{[N]\\M},
    returned as a dict {Fraction: count}."""
    M = sorted(M)
    rest = [i for i in range(N) if i not in set(M)]
    cnt = {}
    for m in points(A, N):
        z = 0
        for j, i in enumerate(rest):
            if (m >> i) & 1:
                z |= 1 << j
        cnt[z] = cnt.get(z, 0) + 1
    out = {}
    dm = 1 << len(M)
    for z in range(1 << len(rest)):
        a = Fraction(cnt.get(z, 0), dm)
        out[a] = out.get(a, 0) + 1
    return out


# ----------------------------------------------------------- report card

def card(A, B, N, tau=None, label=""):
    """full exact report on a cross-disjoint pair; cross-checks (M1) vs (M2)."""
    assert A & B == 0, "not disjoint"
    assert A and B, "empty side"
    cA, cB = spectrum(A, N), spectrum(B, N)
    IA1, IB1 = inf_boundary(A, N), inf_boundary(B, N)
    IA2, IB2 = inf_fourier(A, N, cA), inf_fourier(B, N, cB)
    assert IA1 == IA2, "influence routes disagree on A"
    assert IB1 == IB2, "influence routes disagree on B"
    dA, topsA = degree_and_tops(A, N, cA)
    dB, topsB = degree_and_tops(B, N, cB)
    q, arg = Qval(IA1, IB1)
    # pi_M over EVERY choice of maximum-degree supports: report min and max
    pis = [pi_M(IA1, IB1, MA, MB) for MA in topsA for MB in topsB]
    res = dict(label=label, N=N, sizes=(popcount(A), popcount(B)),
               alpha=Fraction(popcount(A), 1 << N),
               beta=Fraction(popcount(B), 1 << N),
               degA=dA, degB=dB, ntopA=len(topsA), ntopB=len(topsB),
               topA=sorted(map(sorted, topsA))[:4],
               topB=sorted(map(sorted, topsB))[:4],
               Q=q, Qarg=arg, piM_min=min(pis), piM_max=max(pis),
               maxIA=max(IA1), maxIB=max(IB1), IA=IA1, IB=IB1)
    if tau is not None:
        pt, WA, WB = pi_tau(IA1, IB1, tau)
        res.update(pi_tau=pt, WA=WA, WB=WB, tau=tau)
    return res


def fmt(x, digits=4):
    if isinstance(x, Fraction):
        return f"{x}  (~{float(x):.{digits}g})"
    return str(x)


# ------------------------------------------------------- set constructors
# Coordinate convention: coordinate i corresponds to bit i of the point index;
# bit 0 -> value +1, bit 1 -> value -1.

def cube_all(N):
    return (1 << (1 << N)) - 1


def from_pred(N, pred):
    """set of points m in [0,2^N) with pred(m) true; pred sees the bitstring m
    where bit i = 0 means x_i = +1."""
    A = 0
    for m in range(1 << N):
        if pred(m):
            A |= 1 << m
    return A


def subcube(N, coords, vals):
    """{x : x_i = vals[j] for coords[j]}, vals in {+1,-1}."""
    fixed = 0
    want = 0
    for i, v in zip(coords, vals):
        fixed |= 1 << i
        if v == -1:
            want |= 1 << i
    return from_pred(N, lambda m: (m & fixed) == want)


def complement(A, N):
    return cube_all(N) ^ A
