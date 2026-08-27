"""s4_helpers.py -- the per-set exact routines shared by s4 and s5.

A set on r coordinates is a python-int bitmask P over the 2^r points (bit m set
iff point m in A).  analyse(P,...) returns, exactly:
  rho   = E_{x~Unif(A)}[ max codim of a prime implicant containing x ]
          ( = expected window size under the WORST minimal-certificate
            selection: minimal certificates of x = prime implicants of A
            containing x )
  N_s   = number of prime implicants of codim s
  Pi    = sum_s N_s 2^-s = E_{x~cube}[#prime implicants containing x]
  maxcod= max codim of a prime implicant.
Only integer / Fraction arithmetic.
"""
from fractions import Fraction as F


def flip_masks(r):
    out = []
    for i in range(r):
        s = 1 << i
        A = 0
        for m in range(1 << r):
            if not ((m >> i) & 1):
                A |= 1 << m
        out.append((A, s))
    return out


def prep(r):
    fl = flip_masks(r)
    n = 1 << r
    order = sorted((S for S in range(n - 1)), key=lambda S: -bin(S).count("1"))
    popc = [bin(S).count("1") for S in range(n)]
    return fl, order, popc


def analyse(P, r, fl, order, popc):
    n = 1 << r
    full = n - 1
    cert = {full: P}
    for S in order:
        i = (~S & full).bit_length() - 1
        S2 = S | (1 << i)
        c = cert[S2]
        Ai, si = fl[i]
        c2 = ((c & Ai) << si) | ((c >> si) & Ai)
        cert[S] = c & c2
    Z = [0] * (r + 1)
    Ns = {}
    mass = 0
    for S in range(n):
        c = cert[S]
        if not c:
            continue
        mn = c
        Sb, i = S, 0
        while Sb:
            if Sb & 1:
                mn &= ~cert[S ^ (1 << i)]
                if not mn:
                    break
            Sb >>= 1
            i += 1
        if not mn:
            continue
        s = popc[S]
        Z[s] |= mn
        pc = bin(mn).count("1")
        mass += pc
        Ns[s] = Ns.get(s, 0) + pc // (1 << (r - s))
    tot, suf, maxcod = 0, 0, 0
    for s in range(r, 0, -1):
        suf |= Z[s]
        if Z[s]:
            maxcod = max(maxcod, s)
        tot += bin(suf).count("1")
    npts = bin(P).count("1")
    return F(tot, npts), Ns, F(mass, 1 << r), maxcod


def wht_deg(P, r):
    v = [(P >> m) & 1 for m in range(1 << r)]
    h = 1
    while h < len(v):
        for i in range(0, len(v), h * 2):
            for j in range(i, i + h):
                x, y = v[j], v[j + h]
                v[j], v[j + h] = x + y, x - y
        h *= 2
    deg = 0
    for S, c in enumerate(v):
        if c:
            deg = max(deg, bin(S).count("1"))
    return deg


def relevant(P, r):
    out = []
    for i in range(r):
        s = 1 << i
        for m in range(1 << r):
            if ((P >> m) & 1) != ((P >> (m ^ s)) & 1):
                out.append(i)
                break
    return out
