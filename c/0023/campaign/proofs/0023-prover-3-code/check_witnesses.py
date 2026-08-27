"""Exact re-derivation of the two barrier witnesses (prover-3, campaign c/0023).

Independent of refuter-3's code: sets are bitmask truth tables on {+-1}^N, Fourier
coefficients by integer fast Walsh-Hadamard, every reported number exact
(fractions.Fraction).  Convention: point x <-> mask m, bit i set <=> x_i = -1.
"""
from fractions import Fraction as F
from itertools import combinations


def wht(vals):
    a = list(vals); n = len(a); h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a


class BoolSet:
    def __init__(self, N, member):
        self.N = N
        self.tt = [1 if member(m) else 0 for m in range(1 << N)]
        self.size = sum(self.tt); assert self.size > 0
        self.g = wht(self.tt)
        self.alpha = F(self.size, 1 << N)
        acc = [0] * N; self.deg = 0
        for S, c in enumerate(self.g):
            if c:
                w = bin(S).count("1")
                if w > self.deg: self.deg = w
                c2 = c * c
                for i in range(N):
                    if (S >> i) & 1: acc[i] += c2
        den = 1 << (2 * N)
        self.infu = [F(a, den) for a in acc]                 # Inf_i(1_A)
        self.I = [x / self.alpha for x in self.infu]         # Inf_i(f_A)
        self.R = {i for i in range(N) if acc[i]}
        self.md = [S for S, c in enumerate(self.g)
                   if c and bin(S).count("1") == self.deg]

    def cert(self, m):
        val = self.tt[m]
        for size in range(self.N + 1):
            for T in combinations(sorted(self.R), size):
                mk = 0
                for i in T: mk |= 1 << i
                if all(self.tt[y] == val for y in range(1 << self.N)
                       if (y & mk) == (m & mk)):
                    return set(T)
        raise AssertionError


def bits(S): return {i for i in range(64) if (S >> i) & 1}
def piW(A, B, WA, WB):
    return sum((A.I[i] for i in WB), F(0)) + sum((B.I[i] for i in WA), F(0))
def piRel(A, B):
    S = A.R & B.R
    return sum((A.I[i] + B.I[i] for i in S), F(0)), S


print("=" * 79)
print("WITNESS (a): address pair (A_k, A_k^c),  A_k = {y_addr(a)=+1},  d=k+1")
print("=" * 79)
for k in (1, 2, 3):
    N = k + (1 << k); d = k + 1
    def addr(m, k=k):
        j = 0
        for t in range(k): j = 2 * j + ((m >> t) & 1)
        return j
    A = BoolSet(N, lambda m: ((m >> (k + addr(m))) & 1) == 0)
    B = BoolSet(N, lambda m: ((m >> (k + addr(m))) & 1) == 1)
    assert A.deg == d == B.deg
    assert all(A.tt[m] + B.tt[m] == 1 for m in range(1 << N))
    p, S = piRel(A, B)
    print(f"k={k} d={d} N={N} alpha={A.alpha}: |Rel A|=|Rel B|={len(A.R)},{len(B.R)}"
          f"  k+2^k={k+(1<<k)}   |S|={len(S)}")
    print(f"  Inf(f_A): addr={[A.I[i] for i in range(k)]}  targets={[A.I[k+j] for j in range(1<<k)]}")
    print(f"  Inf(f_B): addr={[B.I[i] for i in range(k)]}  targets={[B.I[k+j] for j in range(1<<k)]}")
    print(f"  sum_i Inf_i(f_A) = {sum(A.I, F(0))}   hand k/4+1/2 = {F(k,4)+F(1,2)}")
    print(f"  pi_Rel = {p}   hand k/2+1 = {F(k,2)+1}")
    print(f"  RATIO pi_Rel/(|Rel A|+|Rel B|) = {p/(len(A.R)+len(B.R))}"
          f"   hand (k/2+1)/(2(k+2^k)) = {(F(k,2)+1)/(2*(k+(1<<k)))}")
    print(f"  max-deg supports 1_A: {len(A.md)}, sizes {sorted({bin(s).count('1') for s in A.md})},"
          f" all addr bits in each: {all(bits(s)>=set(range(k)) for s in A.md)},"
          f" exactly one target each: {all(len(bits(s)-set(range(k)))==1 for s in A.md)}")
    print(f"  max-deg supports 1_B: {len(B.md)}, same shape:"
          f" {all(bits(s)>=set(range(k)) and len(bits(s)-set(range(k)))==1 for s in B.md)}")
    pays = [(piW(A,B,bits(sa),bits(sb)), bin(sa).count('1')+bin(sb).count('1'))
            for sa in A.md for sb in B.md]
    print(f"  SHATTERING window: min payment = {min(q for q,_ in pays)}"
          f"  hand k/2+2^-k = {F(k,2)+F(1,1<<k)};  min ratio = {min(q/s for q,s in pays)}")
    if k <= 2:
        cp = []
        for ma in range(1 << N):
            if not A.tt[ma]: continue
            TA = A.cert(ma)
            for mb in range(1 << N):
                if not B.tt[mb]: continue
                TB = B.cert(mb)
                cp.append((piW(A,B,TA,TB), len(TA)+len(TB)))
        print(f"  MIN-CERTIFICATE window: min payment = {min(q for q,_ in cp)},"
              f" max |T_A|+|T_B| = {max(s for _,s in cp)}, min ratio = {min(q/s for q,s in cp)}")

print()
print("=" * 79)
print("WITNESS (b): codim-d subcube pair (C, C^c),  C = {x_1=..=x_d=+1}")
print("=" * 79)
for d in (2, 3, 4, 5, 6):
    N = d
    C = BoolSet(N, lambda m: m == 0)
    D = BoolSet(N, lambda m: m != 0)
    assert C.deg == d == D.deg
    p, S = piRel(C, D)
    print(f"d={d}: alpha_C={C.alpha} alpha_Cc={D.alpha} Inf(f_C)={C.I[0]}"
          f" Inf(f_Cc)={D.I[0]} (hand 1/(2(2^d-1)) = {F(1,2*((1<<d)-1))})"
          f"  |Rel|={len(C.R)},{len(D.R)}")
    print(f"   pi_Rel = {p} (hand d/2+d/(2(2^d-1)) = {F(d,2)+F(d,2*((1<<d)-1))});"
          f"  ratio = {p/(len(C.R)+len(D.R))}")
    print(f"   max-deg supports: 1_C {len(C.md)} of size {bin(C.md[0]).count('1')};"
          f" 1_Cc {len(D.md)} of size {bin(D.md[0]).count('1')}")
    sh = [(piW(C,D,bits(sa),bits(sb)), bin(sa).count('1')+bin(sb).count('1'))
          for sa in C.md for sb in D.md]
    print(f"   SHATTERING: payment {min(q for q,_ in sh)} (hand d/2+d/(2(2^d-1)) ="
          f" {F(d,2)+F(d,2*((1<<d)-1))}), ratio {min(q/s for q,s in sh)}"
          f" (hand 1/4+1/(4(2^d-1)) = {F(1,4)+F(1,4*((1<<d)-1))})")
    # own-heavy window: W(A) = {i : Inf_i(f_A) >= theta}, theta = 1/(2d)
    th = F(1, 2 * d)
    WC = {i for i in range(N) if C.I[i] >= th}
    WD = {i for i in range(N) if D.I[i] >= th}
    q = piW(C, D, WC, WD); s = len(WC) + len(WD)
    print(f"   OWN-HEAVY (theta=1/(2d)): W(C)={sorted(WC)} W(C^c)={sorted(WD)}"
          f" payment={q} ratio={q/s if s else 'undef(0)'}"
          f"  (hand 1/(2(2^d-1)) = {F(1,2*((1<<d)-1))})")
    if d <= 4:
        cp = []
        for ma in range(1 << N):
            if not C.tt[ma]: continue
            TA = C.cert(ma)
            for mb in range(1 << N):
                if not D.tt[mb]: continue
                TB = D.cert(mb)
                cp.append((piW(C,D,TA,TB), len(TA)+len(TB)))
        print(f"   MIN-CERTIFICATE: min payment = {min(q for q,_ in cp)},"
              f" min ratio = {min(q/s for q,s in cp)}, max window sum = {max(s for _,s in cp)}")

print()
print("=" * 79)
print("L11.2 check: Sigma-restricted certificate payment on witness (a)")
print("=" * 79)
for k in (1, 2, 3, 4):
    d = k + 1
    infA_addr = F(1, 4); infA_tgt = F(1, 1 << (k + 1))
    tot = F(0); worst = None
    for a in range(1 << k):
        for a2 in range(1 << k):
            diff = bin(a ^ a2).count("1")
            pay = F(diff, 1) * (infA_addr + infA_addr)          # opposite address bits
            if a == a2:
                pay += infA_tgt + infA_tgt                       # the shared target read
            tot += pay
            worst = pay if worst is None else min(worst, pay)
    avg = tot / F(1 << (2 * k))
    print(f"k={k} d={d}: worst-case Sigma payment = {worst} (hand 2^-k = {F(1,1<<k)});"
          f"  average = {avg}  (hand k/4+2^-2k = {F(k,4)+F(1,1<<(2*k))})")
