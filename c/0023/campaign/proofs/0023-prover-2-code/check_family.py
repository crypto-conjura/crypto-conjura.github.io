#!/usr/bin/env python3
"""
0023-prover-2, unit 2 (T3): exact machine check of the family (A_d, B_d) that
refutes (PAY*) in its all-maximum-degree-windows form.

Coordinates: 0..d-1 are the block u_1..u_d ; coordinate d is the hub w.
Encoding: index bit i set  <=>  x_i = -1.
  p = (+1,...,+1),  q = p with u_1 flipped.
  A = {(u,w) : w=+1, u != p} u {(u,w) : w=-1, u = q},  B = A^c.

Everything is exact rational arithmetic (fractions.Fraction) and an integer
Walsh-Hadamard transform; no floating point enters any assertion.

Checks, for each d in 2..12:
  deg(1_A) = deg(1_B) = d                     (membership in C^ind_d)
  alpha = beta = 1/2
  Inf_i(1_A) = 2^{-d-1} for every block coordinate i
  Inf_w(1_A) = (1/2-2^{-d})^2 + (2^{d-1}-1) 2^{-2d}
  U  = {u_1..u_d}      is a maximum-degree monomial support of 1_A and of 1_B
  U' = {u_2..u_d, w}   is a maximum-degree monomial support of 1_A and of 1_B
  pi(U,U)   = d * 2^{1-d}
  pi(U',U') = 1 + (d-2) * 2^{1-d}
  U, U' are shattering windows (A and B surject off each of them)
"""
from fractions import Fraction as F

def wht(vals, N):
    a = list(vals); n = 1 << N; h = 1
    while h < n:
        for i in range(0, n, h*2):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [c / n for c in a]        # a[S] = coefficient of monomial x^S

pc = lambda x: bin(x).count('1')

def surjects_off(S, W, N):
    """does S subset {+-1}^N project onto {+-1}^{[N]\\W} ?"""
    comp = [i for i in range(N) if not (W >> i) & 1]
    seen = set()
    for m in S:
        seen.add(tuple((m >> i) & 1 for i in comp))
    return len(seen) == 1 << len(comp)

print(f"{'d':>3} {'degA':>4} {'alpha':>6} {'Inf_ui':>12} {'Inf_w':>12} {'pi(U)':>12} {'pi(U-prime)':>14}")
for d in range(2, 13):
    N = d + 1
    U   = (1 << d) - 1                       # block coordinates
    Up  = ((1 << d) - 2) | (1 << d)          # u_2..u_d together with the hub
    p_mask, q_mask = 0, 1
    A = []
    for m in range(1 << N):
        um = m & ((1 << d) - 1)
        w_neg = (m >> d) & 1
        A.append(F(1) if ((um != p_mask) if not w_neg else (um == q_mask)) else F(0))
    B = [1 - v for v in A]
    cA, cB = wht(A, N), wht(B, N)
    degA = max(pc(S) for S in range(1 << N) if cA[S] != 0)
    degB = max(pc(S) for S in range(1 << N) if cB[S] != 0)
    alpha, beta = cA[0], cB[0]
    inf = lambda c, i: sum(c[S]**2 for S in range(1 << N) if (S >> i) & 1)
    infA = [inf(cA, i) for i in range(N)];  infB = [inf(cB, i) for i in range(N)]
    pay = lambda WA, WB: (sum(infA[i] for i in range(N) if (WB >> i) & 1)/alpha
                          + sum(infB[i] for i in range(N) if (WA >> i) & 1)/beta)
    piU, piUp = pay(U, U), pay(Up, Up)
    Aset = [m for m in range(1 << N) if A[m] == 1]
    Bset = [m for m in range(1 << N) if B[m] == 1]
    # assertions (exact)
    assert degA == d and degB == d
    assert alpha == F(1,2) and beta == F(1,2)
    assert all(infA[i] == F(1, 2**(d+1)) for i in range(d))
    assert infA[d] == (F(1,2) - F(1,2**d))**2 + (2**(d-1)-1)*F(1,4**d)
    assert infB == infA
    assert cA[U] != 0 and pc(U) == degA and cB[U] != 0
    assert cA[Up] != 0 and pc(Up) == degA and cB[Up] != 0
    assert piU  == F(d) * F(2)**(1-d)
    assert piUp == 1 + F(d-2) * F(2)**(1-d)
    for W in (U, Up):
        assert surjects_off(Aset, W, N) and surjects_off(Bset, W, N)
    print(f"{d:>3} {degA:>4} {str(alpha):>6} {str(infA[0]):>12} {str(infA[d]):>12} "
          f"{str(piU):>12} {str(piUp):>14}")
print("\nALL EXACT ASSERTIONS PASSED (d = 2..12).")
