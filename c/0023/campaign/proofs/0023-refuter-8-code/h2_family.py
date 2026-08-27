"""
h2_family.py -- the DEFORMATION of the certified witness into u3's branch 2.

FAMILY  W(d,k),  1 <= k <= d-2,   N = k+d.

   Z  = {0,..,k-1}          R  = { x_Z = (+1)^k }          (codim-k subcube)
   K  = {k,..,k+d-1}        T  = { x_K = (+1)^d }          (codim-d subcube)
   K1 = first d-k-1 coords of K,  U = { x : x_{K1} != (+1)^{d-k-1} }

   A := (R x U)  u  ({+-1}^Z x T)          B := complement of A

Equivalently 1_A = 1_R * 1_U + 1_T  (the two blocks are disjoint since
T's single point lies inside the subcube {x_{K1}=(+1)} = complement of U).

WHY.  deg(1_R 1_U) = k + (d-k-1) = d-1 while deg(1_T) = d, so 1_A has a UNIQUE
maximum-degree monomial, x_K, supported entirely inside K.  A is, up to
measure ~2^{-d}, the codim-k subcube R x {+-1}^K -- so its heavy coordinates
are Z, which the maximum-degree support misses.  T is a "degree booster"
parked on a set of measure 2^{-d}: it fixes the degree at d without moving any
influence.  That is exactly what the certified witness (A = codim-d subcube)
cannot do, and it is what puts the deformed pair inside branch 2.

VARIANT V2 (non-subcube base):  R := R1 u R2 with R1 = {x_{Z1}=(+1)^k},
R2 = {x_{Z2}=(+1)^k} on disjoint blocks Z1,Z2 -- deg(1_R)=2k, so |K1|=d-2k-1.
A is then at relative distance >= 1/2 from EVERY subcube.
"""
import sys, os
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import *
from fam8 import build_V1, build_V2, subcube_distance


def _dup_build_V1(d, k):
    N = k + d
    mZ = (1 << k) - 1
    mK = ((1 << d) - 1) << k
    mK1 = ((1 << (d - k - 1)) - 1) << k

    def pred(m):
        inR = (m & mZ) == 0
        inU = (m & mK1) != 0
        inT = (m & mK) == 0
        return (inR and inU) or inT
    A = from_pred(N, pred)
    return N, A, complement(A, N), list(range(k)), list(range(k, k + d)), \
        list(range(k, k + d - k - 1))


def _dup_build_V2(d, k):
    """non-subcube base R = R1 u R2 on two disjoint blocks of size k."""
    N = 2 * k + d
    mZ1 = (1 << k) - 1
    mZ2 = ((1 << k) - 1) << k
    mK = ((1 << d) - 1) << (2 * k)
    w = d - 2 * k - 1
    assert w >= 1, "need d >= 2k+2"
    mK1 = ((1 << w) - 1) << (2 * k)

    def pred(m):
        inR = ((m & mZ1) == 0) or ((m & mZ2) == 0)
        inU = (m & mK1) != 0
        inT = (m & mK) == 0
        return (inR and inU) or inT
    A = from_pred(N, pred)
    return N, A, complement(A, N), list(range(2 * k)), \
        list(range(2 * k, 2 * k + d)), list(range(2 * k, 2 * k + w))


def closed_V1(d, k):
    """closed forms derived by hand in the report; all exact Fractions."""
    q, r = Fraction(1, 2 ** k), Fraction(1, 2 ** d)
    alpha = q - r
    beta = 1 - alpha
    iZ = q / 2 - r                          # Inf_i(1_A), i in Z
    iK1 = 3 * r / 2 - q * r                 # Inf_i(1_A), i in K1
    iK0 = r / 2                             # Inf_i(1_A), i in K\K1
    sumK = (d - k - 1) * iK1 + (k + 1) * iK0
    Q = max(iZ, iK1, iK0) / beta            # = max_i Inf_i(1_A) / max(alpha,beta)
    piM = sumK * (1 / alpha + 1 / beta)
    return dict(alpha=alpha, beta=beta, iZ=iZ, iK1=iK1, iK0=iK0, Q=Q, piM=piM,
                maxIA=max(iZ, iK1, iK0) / alpha, maxIB=max(iZ, iK1, iK0) / beta)


def _dup_subcube_distance(A, N):
    """min over ALL 3^N subcubes C of |A xor C| / |A|  (exact Fraction)."""
    nA = popcount(A)
    best = Fraction(popcount(A ^ 0), nA)     # C = empty is not a subcube; start big
    best = Fraction(10 ** 9)
    import itertools
    for pat in itertools.product([0, 1, 2], repeat=N):   # 0 free, 1 -> +1, 2 -> -1
        fixed = 0
        want = 0
        for i, p in enumerate(pat):
            if p == 1:
                fixed |= 1 << i
            elif p == 2:
                fixed |= 1 << i
                want |= 1 << i
        C = 0
        for m in range(1 << N):
            if (m & fixed) == want:
                C |= 1 << m
        v = Fraction(popcount(A ^ C), nA)
        if v < best:
            best = v
    return best


print("=" * 78)
print("V1(d,k):  A = (R x U) u (cube x T),  B = complement")
print("=" * 78)
hits = []
for d in range(4, 10):
    for k in range(1, d - 1):
        N, A, B, Z, K, K1 = build_V1(d, k)
        if N > 13:
            continue
        tau = Fraction(1, 2 * d ** 4)
        r = card(A, B, N, tau=tau, label=f"V1 d={d} k={k}")
        cf = closed_V1(d, k)
        agree = (r['alpha'] == cf['alpha'] and r['Q'] == cf['Q']
                 and r['piM_min'] == cf['piM'] and r['maxIA'] == cf['maxIA']
                 and r['maxIB'] == cf['maxIB'])
        uniqM = (r['ntopA'] == 1 and r['ntopB'] == 1
                 and set(r['topA'][0]) == set(K) and set(r['topB'][0]) == set(K))
        print(f"\n  d={d} k={k} N={N}  alpha={r['alpha']} deg=({r['degA']},{r['degB']})")
        print(f"    unique max-degree support = K on both sides? {uniqM}   "
              f"(#topA={r['ntopA']}, topA={r['topA'][0]})")
        print(f"    Q      = {fmt(r['Q'])}   at coord {r['Qarg']} "
              f"({'in Z' if r['Qarg'] in Z else 'in K'})")
        print(f"    pi_M   = {fmt(r['piM_min'])}   (unique choice of supports)")
        print(f"    pi_tau = {fmt(r['pi_tau'])}  tau={fmt(tau)} "
              f"|W(A)|={len(r['WA'])} |W(B)|={len(r['WB'])}")
        print(f"    max Inf(f_A)={fmt(r['maxIA'])}  max Inf(f_B)={fmt(r['maxIB'])}")
        print(f"    closed forms agree with brute force? {agree}")
        assert agree, (r, cf)
        hits.append((d, k, r))

print()
print("=" * 78)
print("Branch diagnostics for V1  (slice profile over M = K, and rho)")
print("=" * 78)
for d, k in [(5, 2), (6, 2), (6, 3), (7, 3), (8, 3)]:
    N, A, B, Z, K, K1 = build_V1(d, k)
    if N > 12:
        continue
    sa = slice_densities(A, N, K)
    sb = slice_densities(B, N, K)
    print(f"  d={d} k={k}: max-degree slice densities of A: "
          f"{ {str(a): c for a, c in sorted(sa.items())} }")
    print(f"            max-degree slice densities of B: "
          f"{ {str(b): c for b, c in sorted(sb.items())} }")
    rho = Fraction(sum(c for a, c in sa.items() if a > Fraction(1, 2)),
                   2 ** (N - len(K)))
    print(f"            rho = Pr[a_z > 1/2] = {rho}   (E_d has rho = 1/2)")

print()
print("=" * 78)
print("Distance to the nearest subcube (relative to |A|), V1 and V2")
print("=" * 78)
for d, k in [(4, 1), (5, 2), (6, 2)]:
    N, A, B, Z, K, K1 = build_V1(d, k)
    print(f"  V1 d={d} k={k} N={N}: dist(A, nearest subcube)/|A| = "
          f"{fmt(subcube_distance(A, N))}")

print()
print("=" * 78)
print("V2(d,k): non-subcube cylinder base R = R1 u R2")
print("=" * 78)
for d, k in [(4, 1), (5, 1), (6, 1), (6, 2), (7, 2), (8, 2)]:
    if d - 2 * k - 1 < 1:
        continue
    N = 2 * k + d
    if N > 12:
        continue
    N, A, B, Z, K, K1 = build_V2(d, k)
    tau = Fraction(1, 2 * d ** 4)
    r = card(A, B, N, tau=tau, label=f"V2 d={d} k={k}")
    print(f"\n  d={d} k={k} N={N} alpha={r['alpha']} deg=({r['degA']},{r['degB']}) "
          f"#topA={r['ntopA']}")
    print(f"    topA={r['topA'][0]}  (K={K})")
    print(f"    Q      = {fmt(r['Q'])} at coord {r['Qarg']}")
    print(f"    pi_M   in [{fmt(r['piM_min'])}, {fmt(r['piM_max'])}]")
    print(f"    pi_tau = {fmt(r['pi_tau'])}   max Inf(f_B) = {fmt(r['maxIB'])}")
    if N <= 10:
        print(f"    dist(A, nearest subcube)/|A| = {fmt(subcube_distance(A, N))}")
