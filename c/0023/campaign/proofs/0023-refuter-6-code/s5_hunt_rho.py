"""
s5 -- hunt for a degree-<=d set with SUPERPOLYNOMIAL
        rho(A) := E_{x~Unif(A)} [ max codim of a prime implicant containing x ]
      ( = expected window size of the worst unrestricted MINIMAL-certificate
        selection; rho(A) = 2^{Omega(d)} for some family would settle [G5]
        negatively, because (A,A^c) is in P_d and pi_Rel <= 2d always ).

Parts:
 (a) identify the extremal sets found by the exhaustive sweeps of s4;
 (b) the HAMMING/SIMPLEX family: A = a coset of the [2^c-1, 2^c-1-c] Hamming
     code has degree exactly d = 2^(c-1), every point isolated, hence a unique
     prime implicant of codim n = 2d-1 at every point: rho = 2d-1 EXACTLY.
     Verified by integer Walsh-Hadamard (degree) and by exhaustive
     minimum-distance / prime-implicant computation.
 (c) the affine ceiling: for every coset A of a linear code, rho(A) = #Rel(A)
     and #Rel(A) <= 2 deg - 1 (weight-counting identity, proved in the
     artifact); checked on random cosets.
 (d) HILL CLIMB over general degree-<=d sets, n <= 10, with the degree-safe
     move set {add a codim-<=d subcube disjoint from A, delete a codim-<=d
     subcube contained in A, flip one point if the degree survives}, objective
     rho; several restarts per (d,n).
"""
import sys, time, random
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from s4_helpers import analyse, prep, wht_deg, relevant

random.seed(60230827)

# ------------------------------------------------------------------ (a) sets found
print("=" * 78)
print("(a) structure of the extremal sets found by the exhaustive sweeps")
print("=" * 78)
found = [(3, 0x18, "r=3 d=2 rho=3"),
         (5, 0x15548002, "r=5 d=3 rho=17/4 (exhaustive max over L(5,3))"),
         (5, 0x17568406, "r=5 d=3 max PI codim 5"),
         (6, 0x50420a4230220c44, "r=6 d=3 rho=5 (sample max)"),
         (6, 0x5042ddc0fc44bdf5, "r=6 d=3 max PI codim 6 (sample)")]
for r, P, tag in found:
    fl, order, popc = prep(r)
    rho, Ns, Pi, mx = analyse(P, r, fl, order, popc)
    pts = [m for m in range(1 << r) if (P >> m) & 1]
    dens = F(len(pts), 1 << r)
    rel = relevant(P, r)
    # coset test: is pts an affine subspace over F_2?
    a0 = pts[0]
    diffs = {p ^ a0 for p in pts}
    is_coset = all(((x ^ y) in diffs) for x in diffs for y in diffs)
    print(f" {tag}: mask=0x{P:x} deg={wht_deg(P,r)} |A|={len(pts)} "
          f"density={dens} #Rel={len(rel)} rho={rho}={float(rho):.4f} "
          f"N_s={Ns} affine-coset={is_coset}")
    print(f"    points: {[format(p,'0'+str(r)+'b') for p in pts][:20]}"
          f"{' ...' if len(pts)>20 else ''}")

# --------------------------------------------------- (b) Hamming / simplex family
print()
print("=" * 78)
print("(b) HAMMING coset family: rho = n = 2d-1 with degree exactly d = 2^(c-1)")
print("=" * 78)
for c in (2, 3, 4):
    n = (1 << c) - 1
    cols = [j for j in range(1, 1 << c)]          # all nonzero vectors of F_2^c
    # C = { x in F_2^n : sum_i x_i cols[i] = 0 }  (Hamming code, distance 3)
    P = 0
    pts = []
    for m in range(1 << n):
        s = 0
        for i in range(n):
            if (m >> i) & 1:
                s ^= cols[i]
        if s == 0:
            P |= 1 << m
            pts.append(m)
    deg = wht_deg(P, n)
    dmin = min(bin(a ^ b).count("1") for i, a in enumerate(pts)
               for b in pts[i + 1:]) if len(pts) > 1 else n
    d_pred = 1 << (c - 1)
    print(f" c={c}: n={n} |A|={len(pts)} density=2^-{c} deg={deg} "
          f"(predicted 2^(c-1)={d_pred}) min distance={dmin} "
          f"-> all points isolated: {dmin >= 2}")
    if n <= 7:
        fl, order, popc = prep(n)
        rho, Ns, Pi, mx = analyse(P, n, fl, order, popc)
        print(f"      exact rho={rho}={float(rho):.4f}, N_s={Ns}, "
              f"2d-1={2*deg-1}, match: {rho == 2*deg-1}")
    else:
        print(f"      isolated points => unique PI per point of codim n={n}; "
              f"rho = n = {n} = 2d-1 = {2*deg-1}: {n == 2*deg-1}")

# ------------------------------------------------------- (c) random coset check
print()
print("=" * 78)
print("(c) random cosets of random linear codes: rho = #Rel <= 2*deg - 1 ?")
print("=" * 78)
viol = 0
for trial in range(400):
    n = random.randint(3, 7)
    k = random.randint(1, n - 1)
    basis = [random.getrandbits(n) for _ in range(k)]
    span = {0}
    for b in basis:
        span |= {s ^ b for s in span}
    a = random.getrandbits(n)
    pts = sorted(s ^ a for s in span)
    P = 0
    for p in pts:
        P |= 1 << p
    if P == 0 or P == (1 << (1 << n)) - 1:
        continue
    deg = wht_deg(P, n)
    fl, order, popc = prep(n)
    rho, Ns, Pi, mx = analyse(P, n, fl, order, popc)
    rel = relevant(P, n)
    ok = (rho == len(rel)) and (len(rel) <= 2 * deg - 1)
    if not ok:
        viol += 1
        print(f"  VIOLATION n={n} mask=0x{P:x} deg={deg} rho={rho} "
              f"#Rel={len(rel)} N_s={Ns}")
print(f" 400 random cosets: violations of [rho = #Rel and #Rel <= 2deg-1] = {viol}")

# ------------------------------------------------------------- (d) hill climb
print()
print("=" * 78)
print("(d) HILL CLIMB over degree-<=d sets (degree-safe moves), objective rho")
print("=" * 78)


def subcube_mask(n, S, v):
    """bitmask of the subcube {z : z&S == v}."""
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
    idx = random.sample(range(n), c)
    S = 0
    for i in idx:
        S |= 1 << i
    v = random.getrandbits(n) & S
    return S, v


def climb(n, d, iters=4000, restarts=6):
    fl, order, popc = prep(n)
    full = (1 << (1 << n)) - 1
    best = (F(0), 0)
    for rs in range(restarts):
        # start: a few random disjoint codim-d subcubes
        P = 0
        for _ in range(random.randint(1, 6)):
            S, v = rand_subcube(n, d)
            Q = subcube_mask(n, S, v)
            if P & Q == 0:
                P |= Q
        if P == 0 or P == full:
            continue
        cur = analyse(P, n, fl, order, popc)[0]
        for it in range(iters):
            mv = random.random()
            if mv < 0.4:
                c = random.randint(1, d)
                S, v = rand_subcube(n, c)
                Q = subcube_mask(n, S, v)
                if P & Q:
                    continue
                Pn = P | Q
            elif mv < 0.8:
                c = random.randint(1, d)
                S, v = rand_subcube(n, c)
                Q = subcube_mask(n, S, v)
                if (P & Q) != Q:
                    continue
                Pn = P & ~Q
            else:
                m = random.randrange(1 << n)
                Pn = P ^ (1 << m)
                if wht_deg(Pn, n) > d:
                    continue
            if Pn == 0 or Pn == full:
                continue
            newr = analyse(Pn, n, fl, order, popc)[0]
            if newr >= cur:
                P, cur = Pn, newr
        assert wht_deg(P, n) <= d, "move set broke the degree bound"
        if cur > best[0]:
            best = (cur, P)
    return best


print(f"{'d':>3} {'n':>3} {'best rho':>12} {'float':>9} {'2d-1':>6} "
      f"{'2^(d-1)':>8} {'#Rel':>5} {'N_s'}")
for d in (2, 3, 4, 5):
    for n in (6, 8, 10):
        if n <= d:
            continue
        t0 = time.time()
        rho, P = climb(n, d, iters=2500, restarts=5)
        fl, order, popc = prep(n)
        _, Ns, Pi, mx = analyse(P, n, fl, order, popc)
        rel = relevant(P, n)
        print(f"{d:>3} {n:>3} {str(rho):>12} {float(rho):>9.4f} {2*d-1:>6} "
              f"{1<<(d-1):>8} {len(rel):>5} {Ns}  deg={wht_deg(P,n)} "
              f"0x{P:x} [{time.time()-t0:.0f}s]")
