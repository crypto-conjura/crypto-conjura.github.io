"""
s11 -- numerical check of the closed form of the artifact's section 3:

  rho <= B(k) <= (k+1) + 4 u_dagger L + 1  <= (k+1) + 8 L lg L + 24 L + 1,
  L = max(2, lg k),  u_dagger = max{u >= 2 : 2^u <= 4 u L}  (<= 2 lg L + 6).

B(k) is the exact-rational union bound; the two closed forms must dominate it.
"""
from fractions import Fraction as F
from math import comb, log2

print(f"{'k':>7} {'u_dag':>6} {'2lgL+6':>7} {'4 u_dag L+1':>12} "
      f"{'8LlgL+24L+1':>13} {'B(k)-d (exact)':>15} {'both dominate?':>15}")
for k in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 16384, 65536]:
    L = max(2.0, log2(k))
    u = 2
    while 2 ** (u + 1) <= 4 * (u + 1) * L:
        u += 1
    ud = u
    cf1 = 4 * ud * L + 1
    cf2 = 8 * L * log2(L) + 24 * L + 1
    B = F(k + 1)
    for uu in range(2, k + 1):
        if 2 ** uu - 1 >= 4000:
            break
        t = min(F(comb(k, uu), 1 << (2 ** uu - 1)), F(1))
        B += ((1 << (uu - 1)) - 1) * t
    ex = float(B) - (k + 1)
    ok = (ex <= cf1) and (ex <= cf2) and (ud <= 2 * log2(L) + 6)
    print(f"{k:>7} {ud:>6} {2*log2(L)+6:>7.2f} {cf1:>12.2f} {cf2:>13.2f} "
          f"{ex:>15.4f} {str(ok):>15}")
