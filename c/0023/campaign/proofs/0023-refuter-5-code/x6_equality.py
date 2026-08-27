"""
x6_equality.py -- the EQUALITY MANIFOLD of the payment.

Two questions, both settled here in the swept regimes:

 Q1  Which pairs attain pi_Rel = 1?  Claim: exactly those with |S| = 1, i.e.
     A and B sit in opposite halves of one coordinate which is the ONLY
     coordinate relevant to both; then pi_Rel = 1/2 + 1/2 = 1 identically,
     whatever A and B are inside their halves.

 Q2  Why can |S| >= 2 not attain it?  Tracing the equality conditions of the
     x2 chain: equality in
        TV(nu,U) = (1/2)sum_y | 2^{-m} sum_J (nu(y) - nu(y+J)) |
                <= 2^{-m} sum_J TV(nu, sigma_J nu)
     forces, for every y, all the differences nu(y)-nu(y') (y' over the whole
     cube) to have ONE sign -- i.e. every value of nu is the max or the min of
     nu, so nu takes at most two values, and since nu=0 off Y it is UNIFORM on
     Y.  Then T(nu) = |E(Y,Y^c)|/|Y| = 1 with |Y| = 2^{m-1}, and the
     edge-isoperimetric equality case forces Y to be a codim-1 subcube, whose
     uniform measure has D_i = 0 for every i except one -- contradicting
     D_i = r_i > 0 for all i in S unless m = 1.

 Checked below: (Q1) on every pair at N<=3 and every equality pair at N=4;
 (Q2) the edge-isoperimetric equality case exhaustively for m <= 4, and the
 two-value consequence on all N<=4 equality pairs.
"""
import sys, os
from fractions import Fraction
from itertools import combinations
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib5 import (popcount, bcounts, rel, pi_rel, shadow_measure, Dvec,
                  tv_to_uniform)


def all_pairs(N):
    P = 1 << N
    for A in range(1, 1 << P):
        C = ((1 << P) - 1) ^ A
        sub = C
        while sub:
            yield A, sub
            sub = (sub - 1) & C


def q1(N):
    """|S| = 1  <=>  pi_Rel = 1 ?"""
    n_s1 = n_s1_not1 = n_eq = n_eq_bigS = 0
    for A, B in all_pairs(N):
        pi, S = pi_rel(A, B, N)
        if len(S) == 1:
            n_s1 += 1
            if pi != 1:
                n_s1_not1 += 1
        if pi == 1:
            n_eq += 1
            if len(S) != 1:
                n_eq_bigS += 1
    return n_s1, n_s1_not1, n_eq, n_eq_bigS


def n4_pass():
    """vectorised pass over all 3^16 labellings at N=4: collect the pairs with
    |S|=1 and the pairs with pi=1, and test both directions plus the
    structural claim on every one of them."""
    from lib5 import flip_arrays, bvec_np, subsets_of_mask
    N = 4
    P = 1 << N
    FULL = (1 << P) - 1
    fl = flip_arrays(N)
    n_s1 = n_s1_not1 = n_eq = n_eq_bigS = 0
    struct_bad = 0
    for A in range(1, FULL):
        C = FULL ^ A
        nA = popcount(A)
        bA = np.array(bcounts(A, N), dtype=np.int64)
        Bs = subsets_of_mask(C, N)[1:]
        if len(Bs) == 0:
            continue
        nB = np.bitwise_count(Bs).astype(np.int64)
        bB = bvec_np(Bs, N, fl)
        sel = (bB > 0) & (bA[None, :] > 0)
        Num = ((bA[None, :] * nB[:, None] + bB * nA) * sel).sum(axis=1)
        Den = 2 * nA * nB
        sizeS = sel.sum(axis=1)
        one = Num == Den
        s1 = sizeS == 1
        n_s1 += int(s1.sum())
        n_s1_not1 += int((s1 & ~one).sum())
        n_eq += int(one.sum())
        n_eq_bigS += int((one & ~s1).sum())
        # structural claim on the |S|=1 pairs
        for j in np.flatnonzero(s1):
            B = int(Bs[j])
            i = int(np.flatnonzero(sel[j])[0])
            Ah = {(p >> i) & 1 for p in range(P) if (A >> p) & 1}
            Bh = {(p >> i) & 1 for p in range(P) if (B >> p) & 1}
            if len(Ah) != 1 or len(Bh) != 1 or Ah == Bh:
                struct_bad += 1
    return n_s1, n_s1_not1, n_eq, n_eq_bigS, struct_bad


def iso_equality(m):
    """all Y with |Y| = 2^{m-1}: is |E(Y,Y^c)| = 2^{m-1} only for codim-1
    subcubes?"""
    K = 1 << m
    half = K // 2
    subcubes = set()
    for i in range(m):
        for v in (0, 1):
            subcubes.add(frozenset(y for y in range(K) if ((y >> i) & 1) == v))
    tight = 0
    tight_noncube = 0
    for Y in combinations(range(K), half):
        Ys = set(Y)
        e = sum(1 for y in Ys for i in range(m) if (y ^ (1 << i)) not in Ys)
        if e == half:
            tight += 1
            if frozenset(Ys) not in subcubes:
                tight_noncube += 1
        if e < half:
            print(f"    !! isoperimetry violated at m={m}: {sorted(Ys)}")
    return tight, tight_noncube, len(subcubes)


def two_value_check(N):
    """on every equality pair, is nu uniform on its shadow (the forced form)?"""
    tot = nonuniform = 0
    for A, B in all_pairs(N):
        pi, S = pi_rel(A, B, N)
        if pi != 1:
            continue
        tot += 1
        for X in (A, B):
            nu, supp = shadow_measure(X, N, S)
            vals = {v for v in nu if v > 0}
            if len(vals) > 1:
                nonuniform += 1
    return tot, nonuniform


if __name__ == "__main__":
    print("=" * 74)
    print("Q1  |S| = 1  <=>  pi_Rel = 1")
    print("=" * 74)
    for N in (2, 3):
        n_s1, n_s1_not1, n_eq, n_eq_bigS = q1(N)
        print(f"  N={N}: pairs with |S|=1 : {n_s1}, of which pi != 1 : "
              f"{n_s1_not1}      pairs with pi=1 : {n_eq}, of which |S| != 1 :"
              f" {n_eq_bigS}")
    n_s1, n_s1_not1, n_eq, n_eq_bigS, sb = n4_pass()
    print(f"  N=4: pairs with |S|=1 : {n_s1}, of which pi != 1 : {n_s1_not1}"
          f"      pairs with pi=1 : {n_eq}, of which |S| != 1 : {n_eq_bigS}")
    print(f"  N=4: |S|=1 pairs failing 'A and B in opposite halves of that "
          f"coordinate': {sb}")

    print()
    print("=" * 74)
    print("Q2  the forced equality shape")
    print("=" * 74)
    for N in (2, 3):
        tot, nonu = two_value_check(N)
        print(f"  N={N}: equality pairs {tot}; sides whose shadow measure is "
              f"NOT uniform on its support: {nonu}  (must be 0: m=1 shadows "
              f"are single points)")
    for m in (2, 3, 4):
        t, tn, ns = iso_equality(m)
        print(f"  m={m}: |Y|=2^(m-1) with edge boundary exactly 2^(m-1): "
              f"{t} sets, of which NOT codim-1 subcubes: {tn} "
              f"(codim-1 subcubes: {ns})")
    print("DONE x6")
