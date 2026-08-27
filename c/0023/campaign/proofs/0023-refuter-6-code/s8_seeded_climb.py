"""
s8 -- the sharpest available test of the envelope (R): rho(A) <= 2 deg - 1.

Start the degree-safe hill climb AT the conjectured extremal point (the Hamming
/ repetition coset, which attains rho = 2d-1 exactly for d = 2^{c-1}) embedded
in a larger cube, and at the address family, and try to exceed 2d-1.
Also record the exact affine maximum for small d by brute force over cosets,
to show the general class strictly exceeds the affine one at d = 3.
"""
import sys, random, time
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from s4_helpers import analyse, prep, wht_deg, relevant

random.seed(8_0023)


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


def embed(Ppts, n0, n):
    """cylinder: A = {x : x_{0..n0-1} in Ppts}; irrelevant new coordinates."""
    P = 0
    for m in range(1 << n):
        if (m & ((1 << n0) - 1)) in Ppts:
            P |= 1 << m
    return P


def hamming_pts(c):
    n = (1 << c) - 1
    cols = list(range(1, 1 << c))
    pts = []
    for m in range(1 << n):
        s = 0
        for i in range(n):
            if (m >> i) & 1:
                s ^= cols[i]
        if s == 0:
            pts.append(m)
    return n, pts


def address_pts(k):
    N = k + (1 << k)
    pts = [m for m in range(1 << N) if ((m >> (k + (m & ((1 << k) - 1)))) & 1) == 0]
    return N, pts


def climb_from(P, n, d, iters):
    fl, order, popc = prep(n)
    full = (1 << (1 << n)) - 1
    cur = analyse(P, n, fl, order, popc)[0]
    best = (cur, P)
    for it in range(iters):
        mv = random.random()
        if mv < 0.45:
            c = random.randint(1, d)
            Q = subcube_mask(n, *rand_subcube(n, c))
            if P & Q:
                continue
            Pn = P | Q
        elif mv < 0.9:
            c = random.randint(1, d)
            Q = subcube_mask(n, *rand_subcube(n, c))
            if (P & Q) != Q:
                continue
            Pn = P & ~Q
        else:
            Pn = P ^ (1 << random.randrange(1 << n))
            if wht_deg(Pn, n) > d:
                continue
        if Pn == 0 or Pn == full:
            continue
        r = analyse(Pn, n, fl, order, popc)[0]
        if r >= cur:
            P, cur = Pn, r
            if cur > best[0]:
                best = (cur, P)
    assert wht_deg(best[1], n) <= d
    return best


print("=" * 78)
print("seeded climbs: can anything exceed 2d-1 ?")
print("=" * 78)
seeds = []
for c in (2, 3):
    n0, pts = hamming_pts(c)
    seeds.append((f"Hamming c={c} (n0={n0}, d={1<<(c-1)})", n0, set(pts), 1 << (c - 1)))
for k in (2, 3):
    n0, pts = address_pts(k)
    seeds.append((f"address k={k} (n0={n0}, d={k+1})", n0, set(pts), k + 1))

for tag, n0, pts, dseed in seeds:
    for n in (n0, n0 + 1, n0 + 2):
        if n > 10:
            continue
        P = embed(pts, n0, n)
        d = dseed
        fl, order, popc = prep(n)
        r0 = analyse(P, n, fl, order, popc)[0]
        t0 = time.time()
        rb, Pb = climb_from(P, n, d, iters=3000)
        _, Ns, Pi, mx = analyse(Pb, n, fl, order, popc)
        flag = "  *** EXCEEDS 2d-1 ***" if rb > 2 * d - 1 else ""
        print(f" {tag:34s} r={n:>2} d={d}: seed rho={r0}={float(r0):.4f} -> "
              f"best rho={rb}={float(rb):.4f}  (2d-1={2*d-1}, 2^(d-1)="
              f"{1<<(d-1)}) N_s={Ns} deg={wht_deg(Pb,n)} [{time.time()-t0:.0f}s]"
              f"{flag}")

print()
print("=" * 78)
print("exact AFFINE maximum of rho for small d (all cosets of all linear codes)")
print("=" * 78)
for n in range(2, 7):
    best = {}
    # all linear subspaces of F_2^n via all subsets closed under xor: enumerate
    # spans of up to n generators (dedup by the span itself)
    spans = set()
    def gen(gens, sp):
        spans.add(frozenset(sp))
        if len(gens) == n:
            return
        for g in range(1, 1 << n):
            if g in sp:
                continue
            nsp = sp | {s ^ g for s in sp}
            gen(gens + [g], nsp)
    gen([], {0})
    for sp in spans:
        for a in range(1 << n):
            pts = sorted(s ^ a for s in sp)
            P = 0
            for p in pts:
                P |= 1 << p
            if P == 0 or P == (1 << (1 << n)) - 1:
                continue
            d = wht_deg(P, n)
            rel = len(relevant(P, n))
            cur = best.get(d, 0)
            if rel > cur:
                best[d] = rel
    print(f" n={n}: max #Rel (= max rho over cosets) per degree: "
          f"{dict(sorted(best.items()))}   [2d-1 = "
          f"{ {d: 2*d-1 for d in sorted(best)} }]")
