"""
s2 -- witness (a): EXACT expected window size for EVERY minimal-certificate
selection rule, at every k.

STRUCTURE (proved in the artifact, verified set-for-set against generic brute
force by s1 for k<=3, and spot-verified for k=4,5 by s3):
  x ~ Unif(A_k)  <->  j_0 = b(a) uniform in {0,1}^k, y_{j_0} = +1, the other
  2^k - 1 targets i.i.d. uniform +-1.  Write P = {j : x_{y_j} = +1} and
  R = P \ {j_0} (uniform random subset of the other 2^k-1 addresses).
  Minimal certificates of x  <->  { U subseteq [k] : j_0 + {0,1}^U subseteq P },
  with |S_U| = k - |U| + 2^|U| =: size(|U|).  The valid family is a DOWNSET.

Hence, with u_max := max{|U| : U valid} (well defined, U = empty is always valid),
  MAX rule  E|W| = E[size(u_max)] = (k+1) + sum_{u>=2} (2^{u-1} - 1) q_u,
  q_u := Pr[u_max >= u] = Pr[ exists U, |U| = u, {0,1}^U \ {0} subseteq R ],
and MIN rule E|W| = d = k+1 exactly, and for EVERY rule
        d = k+1 <= E|W| <= E[size(u_max)].

This script computes:
  (1) k <= 4: E|W| under MIN/MAX/UNIF exactly by enumerating all 2^(2^k-1)
      subsets R (32768 for k=4) in exact rational arithmetic;
  (2) k <= 6: q_u exactly by inclusion-exclusion over the binom(k,u) subcube
      events, hence E[size(u_max)] exactly;
  (3) every k: the exact-rational union-bound upper bound
        E[size(u_max)] <= (k+1) + sum_{u>=2} (2^{u-1}-1) min(1, C(k,u) 2^{1-2^u}),
      tabulated up to k = 4096, with the excess over d and a closed-form check;
  (4) the exact level profile: expected number of minimal certificates of each
      size, and the fraction of (point, minimal certificate) pairs whose size
      is >= a threshold (part 2 of the question: isolated or typical?).
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, log2, ceil


def submasks(U):
    v = U
    while True:
        yield v
        if v == 0:
            return
        v = (v - 1) & U


def valid_Us(k, R, j0=0):
    """R: python int bitmask over addresses (bit j set iff j in R); j0 = 0.
    U valid iff every nonzero v <= U has (j0 ^ v) in R."""
    out = []
    for U in range(1 << k):
        ok = True
        for v in submasks(U):
            if v == 0:
                continue
            if not ((R >> (j0 ^ v)) & 1):
                ok = False
                break
        if ok:
            out.append(U)
    return out


def size_of(k, u):
    return k - u + (1 << u)


print("=" * 78)
print("(1) EXACT by full enumeration over R  (k <= 4)")
print("=" * 78)
exact_max = {}
for k in (1, 2, 3, 4):
    n = 1 << k
    tot = 1 << (n - 1)                 # subsets R of the n-1 addresses != 0
    accMIN = accMAX = accUNIF = F(0)
    lvl = {}                           # expected count of valid U per level
    for Rlow in range(tot):
        # spread Rlow over addresses 1..n-1 (address 0 = j0 is always in P)
        R = (Rlow << 1) | 1
        Us = valid_Us(k, R)
        sizes = [size_of(k, bin(U).count("1")) for U in Us]
        accMIN += min(sizes)
        accMAX += max(sizes)
        accUNIF += F(sum(sizes), len(sizes))
        for U in Us:
            u = bin(U).count("1")
            lvl[u] = lvl.get(u, 0) + 1
    d = k + 1
    eMIN, eMAX, eUNIF = (a / tot for a in (accMIN, accMAX, accUNIF))
    exact_max[k] = eMAX
    print(f" k={k} d={d}: E|W| MIN={eMIN} MAX={eMAX}={float(eMAX):.6f} "
          f"UNIF={eUNIF}={float(eUNIF):.6f}   2^(d-1)={1<<(d-1)}")
    prof = {}
    for u, c in sorted(lvl.items()):          # NB size_of(k,0) == size_of(k,1):
        sz = size_of(k, u)                    # accumulate, never overwrite
        prof[sz] = prof.get(sz, F(0)) + F(c, tot)
    print(f"    expected #minimal certs of each size: "
          f"{ {s: str(v) for s, v in prof.items()} }")
    tot_exp = sum(prof.values())
    print(f"    expected total #minimal certs = {tot_exp} = {float(tot_exp):.4f}; "
          f"size-{1<<k} share of the multiset = "
          f"{prof.get(1<<k, F(0))/tot_exp} = {float(prof.get(1<<k,F(0))/tot_exp):.3e}")

print()
print("=" * 78)
print("(2) EXACT q_u by inclusion-exclusion over the binom(k,u) subcube events")
print("=" * 78)


def q_exact(k, u):
    """Pr[ exists U subseteq [k], |U|=u, {0,1}^U \\ 0 subseteq R ], R uniform
    over subsets of {0,1}^k \\ {0}.  Inclusion-exclusion over the binom(k,u)
    events; each intersection has probability 2^{-|union of the punctured
    subcubes|}."""
    Ulist = []
    for c in combinations(range(k), u):
        U = 0
        for t in c:
            U |= 1 << t
        pts = frozenset(v for v in submasks(U) if v != 0)
        Ulist.append(pts)
    M = len(Ulist)
    total = F(0)
    # DFS over subsets of the events, carrying the running union
    def rec(i, cnt, un):
        nonlocal total
        if i == M:
            if cnt:
                total += (-1) ** (cnt + 1) * F(1, 1 << len(un))
            return
        rec(i + 1, cnt, un)
        rec(i + 1, cnt + 1, un | Ulist[i])
    rec(0, 0, frozenset())
    return total


for k in range(1, 7):
    d = k + 1
    qs = {}
    for u in range(2, k + 1):
        if comb(k, u) > 22:            # keep 2^{binom(k,u)} bounded
            qs[u] = None
            continue
        qs[u] = q_exact(k, u)
    if any(v is None for v in qs.values()):
        print(f" k={k}: skipped (an inclusion-exclusion level too large)")
        continue
    E = F(k + 1) + sum(((1 << (u - 1)) - 1) * qs[u] for u in qs)
    tag = ""
    if k in exact_max:
        tag = f"   [matches (1): {E == exact_max[k]}]"
    print(f" k={k} d={d}: q_u = { {u: str(v) for u, v in qs.items()} }")
    print(f"      E[size(u_max)] = {E} = {float(E):.6f}{tag}")

print()
print("=" * 78)
print("(3) RIGOROUS union-bound upper bound, all k  (exact rationals)")
print("     E[size(u_max)] <= (k+1) + sum_{u>=2} (2^{u-1}-1) min(1, C(k,u) 2^{1-2^u})")
print("=" * 78)
print(f"{'k':>6} {'d':>6} {'bound':>22} {'bound-d':>12} {'4 L lg L + 4':>14} "
      f"{'2^(d-1)':>12}")
for k in [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 48, 64, 128, 256, 512,
          1024, 2048, 4096]:
    d = k + 1
    S = F(0)
    for u in range(2, k + 1):
        c = comb(k, u)
        # min(1, c * 2^{1-2^u}) exactly
        t = F(c, 1 << (2 ** u - 1)) if 2 ** u - 1 < 4000 else F(0)
        if 2 ** u - 1 >= 4000:
            t = F(0)                   # 2^{-2^u} < 2^{-4000}: below any printed digit
        if t > 1:
            t = F(1)
        S += ((1 << (u - 1)) - 1) * t
        if u > 6 and t == 0:
            break
    B = F(k + 1) + S
    L = max(2.0, log2(k + 2))
    cf = 4 * L * max(1.0, log2(L)) + 4
    print(f"{k:>6} {d:>6} {float(B):>22.6f} {float(B-d):>12.6f} {cf:>14.2f} "
          f"{('2^%d' % (d-1)):>12}")

print()
print("=" * 78)
print("(4) Level profile at large k: expected #minimal certs of each size,")
print("    and Pr[some minimal cert of size >= threshold]  (union bound / exact)")
print("=" * 78)
for k in (4, 8, 16, 32, 64):
    d = k + 1
    print(f" k={k} (d={d}, 2^(d-1)={1<<(d-1)}):")
    rows = []
    for u in range(0, k + 1):
        if 2 ** u - 1 > 2000:
            break
        c = comb(k, u)
        exp_cnt = F(c, 1 << (2 ** u - 1))
        rows.append((u, size_of(k, u), exp_cnt))
    tot = sum(r[2] for r in rows)
    for u, s, e in rows[:8]:
        print(f"    u={u:>2} size={s:>6}  E[#certs]={float(e):>14.6g}  "
              f"share={float(e/tot):>10.4g}  Pr[u_max>=u]<={float(min(F(1),e)):>10.4g}")
    # the exponential-size extreme
    e_top = F(1, 1 << (2 ** k - 1)) if 2 ** k - 1 < 4000 else None
    if e_top is not None:
        print(f"    u=k  size={1<<k:>6} (= 2^(d-1), the [G5] object): "
              f"Pr = 2^-(2^k-1) = {float(e_top):.6g}; "
              f"contribution to E[size] = {float(e_top*(1<<k)):.6g}")
    else:
        print(f"    u=k  size={1<<k} (= 2^(d-1), the [G5] object): "
              f"Pr = 2^-(2^{k}-1) < 2^-4000; contribution < 2^{k}*2^-(2^{k}-1)")
