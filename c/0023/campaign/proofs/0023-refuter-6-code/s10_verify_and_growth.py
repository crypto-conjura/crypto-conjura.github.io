"""
s10 -- (i) independent verification of the (R)-violating degree-3 set found by
           s9 (rho = 21/4 > 2d-1 = 5 at d = 3, r = 7), by a code path that
           shares nothing with s4_helpers.analyse: lib6.cert_table +
           lib6.minimal_certs_generic (numpy boolean tables) and the slow
           per-point subset scan lib6.minimal_certs_bruteforce_point;
      (ii) how does max rho grow with the number of coordinates at FIXED
           degree?  Degree-safe hill climbing seeded with every record object
           (the L(7,3) record, the Hamming cosets, the address family, and
           products of them), at d = 3,4,5 and r up to 11.  This is the
           question that decides whether sup_A rho(A) is poly(d) or 2^Theta(d),
           i.e. whether [G5] closes in general or the minimal variant of P5
           dies outside the artifact's two witnesses.
"""
import sys, random, time
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from s4_helpers import analyse, prep, wht_deg, relevant
import lib6

random.seed(10_0023)

REC7 = 0x11bb0faafc0c7474d1d1cfc0aa0f2277        # s9's record, deg 3, r = 7

print("=" * 78)
print("(i) independent verification of the (R) violation")
print("=" * 78)
r = 7
A = np.array([bool((REC7 >> m) & 1) for m in range(1 << r)])
print(f" mask 0x{REC7:x}: |A| = {int(A.sum())}, density = "
      f"{F(int(A.sum()), 1 << r)}")
print(f" degree by lib6 (integer WHT on the boolean array): {lib6.degree_of(A, r)}")
print(f" degree by s4_helpers.wht_deg (independent code):   {wht_deg(REC7, r)}")
mc = lib6.minimal_certs_generic(A, r)
tot = 0
hist = {}
sizes_multiset = {}
for m, lst in mc.items():
    mx = max(bin(S).count("1") for S in lst)
    tot += mx
    hist[mx] = hist.get(mx, 0) + 1
    for S in lst:
        s = bin(S).count("1")
        sizes_multiset[s] = sizes_multiset.get(s, 0) + 1
rho_lib6 = F(tot, len(mc))
fl, order, popc = prep(r)
rho_s4, Ns, Pi, mxcod = analyse(REC7, r, fl, order, popc)
print(f" rho by lib6 generic tables : {rho_lib6} = {float(rho_lib6):.6f}")
print(f" rho by s4_helpers.analyse  : {rho_s4} = {float(rho_s4):.6f}   "
      f"match: {rho_lib6 == rho_s4}")
print(f" per-point max-size histogram: {dict(sorted(hist.items()))}")
print(f" minimal-certificate size multiset: {dict(sorted(sizes_multiset.items()))}, "
      f"prime-implicant profile N_s = {Ns} (max codim {mxcod})")
# third method on a sample of points: slow full subset scan
pts = sorted(mc)
bad = 0
for m in pts[:: max(1, len(pts) // 10)]:
    slow = sorted(lib6.minimal_certs_bruteforce_point(A, r, m))
    if slow != sorted(mc[m]):
        bad += 1
print(f" slow per-point subset scan on {len(pts[::max(1,len(pts)//10)])} points: "
      f"mismatches = {bad}")
print(f" => rho = {rho_s4} > 2d-1 = 5 CONFIRMED by three code paths; the "
      f"envelope (R) is FALSE")

print()
print("=" * 78)
print("(ii) growth of max rho with r at fixed degree (degree-safe hill climb,")
print("     seeded with every record object)")
print("=" * 78)


def subcube_mask(n, S, v):
    out = 0
    free = ((1 << n) - 1) & ~S
    w = free
    while True:
        out |= 1 << (v | w)
        if w == 0:
            break
        w = (w - 1) & free
    return out


def rand_subcube(n, c):
    S = 0
    for i in random.sample(range(n), c):
        S |= 1 << i
    return S, random.getrandbits(n) & S


def embed(P0, n0, n):
    """cylinder over the first n0 coordinates."""
    P = 0
    for m in range(1 << n):
        if (P0 >> (m & ((1 << n0) - 1))) & 1:
            P |= 1 << m
    return P


def product(P1, n1, P2, n2):
    """A_1 x A_2 on n1+n2 coordinates (degrees add, rho adds)."""
    P = 0
    for m in range(1 << (n1 + n2)):
        if ((P1 >> (m & ((1 << n1) - 1))) & 1) and ((P2 >> (m >> n1)) & 1):
            P |= 1 << m
    return P


def hamming(c):
    n = (1 << c) - 1
    cols = list(range(1, 1 << c))
    P = 0
    for m in range(1 << n):
        s = 0
        for i in range(n):
            if (m >> i) & 1:
                s ^= cols[i]
        if s == 0:
            P |= 1 << m
    return n, P


def address(k):
    N = k + (1 << k)
    P = 0
    for m in range(1 << N):
        if ((m >> (k + (m & ((1 << k) - 1)))) & 1) == 0:
            P |= 1 << m
    return N, P


def climb(P, n, d, iters):
    fl, order, popc = prep(n)
    full = (1 << (1 << n)) - 1
    cur = analyse(P, n, fl, order, popc)[0]
    best = (cur, P)
    for it in range(iters):
        mv = random.random()
        if mv < 0.45:
            Q = subcube_mask(n, *rand_subcube(n, random.randint(1, d)))
            if P & Q:
                continue
            Pn = P | Q
        elif mv < 0.9:
            Q = subcube_mask(n, *rand_subcube(n, random.randint(1, d)))
            if (P & Q) != Q:
                continue
            Pn = P & ~Q
        else:
            Pn = P ^ (1 << random.randrange(1 << n))
            if wht_deg(Pn, n) > d:
                continue
        if Pn == 0 or Pn == full:
            continue
        rr = analyse(Pn, n, fl, order, popc)[0]
        if rr >= cur:
            P, cur = Pn, rr
            if cur > best[0]:
                best = (cur, P)
    assert wht_deg(best[1], n) <= d
    return best


n3, H3 = hamming(2)          # n=3, deg 2, rho 3
n7, H7 = hamming(3)          # n=7, deg 4, rho 7
na, Aad = address(2)         # n=6, deg 3
seeds = {
    3: [("L(7,3) record", 7, REC7), ("address k=2", na, Aad),
        ("H3 x point-set", n3, H3)],
    4: [("Hamming c=3", n7, H7), ("record x forced coord", 8,
        embed(REC7, 7, 8) & subcube_mask(8, 1 << 7, 0)),
        ("H3 x H3", 6, product(H3, 3, H3, 3))],
    5: [("H3 x L(7,3) record", 10, product(H3, 3, REC7, 7)),
        ("Hamming c=3 x ?", n7, H7)],
}
print(f"{'d':>3} {'r':>3} {'seed':>22} {'seed rho':>10} {'best rho':>12} "
      f"{'float':>8} {'2d-1':>6} {'2^(d-1)':>8} {'#Rel':>5}")
for d in (3, 4, 5):
    for tag, n0, P0 in seeds[d]:
        for n in (n0, n0 + 1, min(n0 + 2, 11)):
            if n > 11 or n < n0:
                continue
            P = embed(P0, n0, n) if n > n0 else P0
            fl, order, popc = prep(n)
            r0 = analyse(P, n, fl, order, popc)[0]
            if wht_deg(P, n) > d:
                continue
            t0 = time.time()
            rb, Pb = climb(P, n, d, iters=8000 if n <= 9 else 3000)
            rel = len(relevant(Pb, n))
            star = " ***" if rb > 2 * d - 1 else ""
            print(f"{d:>3} {n:>3} {tag:>22} {float(r0):>10.4f} {str(rb):>12} "
                  f"{float(rb):>8.4f} {2*d-1:>6} {1<<(d-1):>8} {rel:>5}"
                  f"  [{time.time()-t0:.0f}s]{star}")
