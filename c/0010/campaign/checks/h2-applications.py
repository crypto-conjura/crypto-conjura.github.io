#!/usr/bin/env python3
"""Does (H2) hold at application parameters?  Run: python3 h2-applications.py

D is assumed to have FULL challenge resolution M -- confirmed for this campaign's
applications, since a general distinguisher D^H(y,z) may steer its queries on y.
That removes the M-free arm mu'(q) of resolution-1 observers, and by kappa-2-r2 6
the 2 d sqrt(M) arm is then strictly the smaller of the two for q >= 1, M >= 4,
2 d sqrt(M) < 1.  So (H2) reduces to arm 2 alone:

    2 d sqrt(M) <= sqrt(s' q+ d)   <=>   M <= s' q+ / (4 d)
                                   <=>   log2 M <= k + log2(s' q+) - 2

with k := log2(1/delta) the per-source unpredictability in bits.  Read plainly:
do not ask for more output bits than one source's unpredictability, plus a
logarithmic allowance.  The q-dependence is only additive-logarithmic.
"""
import math
# (H2), arm 2:  2 d sqrt(M) <= sqrt(s' q+ d)  <=>  M <= s' q+ /(4 d)
# in bits:      log2 M <= k + log2(s' q+) - 2      with k := log2(1/delta)
def row(name, logN, sigma, k, logM, logq):
    sp   = sigma + 2*logN
    qp   = 2.0**logq + 1
    allow= k + math.log2(sp*qp) - 2          # max log2 M permitted by (H2)
    S    = math.sqrt(sp*qp*2.0**-k)          # the bound's own error term sqrt(s' q+ d)
    ok   = "yes" if logM <= allow else "NO"
    sec  = -math.log2(S) if S>0 else float('inf')
    print(f"{name:<44} k={k:<4} logM={logM:<8} allowed<={allow:7.1f}  (H2):{ok:<4} "
          f"bound~2^-{sec:.0f}")

print("delta = 2^-k (per-source unpredictability); output length = log2 M bits")
print("sigma=64 leakage, q = 2^64 queries throughout\n")
row("128-bit key, 256-bit-unpredictable sources", 512, 64, 256, 128, 64)
row("256-bit key, 256-bit-unpredictable sources", 512, 64, 256, 256, 64)
row("256-bit key, 128-bit-unpredictable sources", 512, 64, 128, 256, 64)
row("512-bit output, 256-bit-unpredictable src ", 512, 64, 256, 512, 64)
row("1 Mbit stream, 256-bit-unpredictable src  ", 512, 64, 256, 2**20, 64)
row("128-bit key, 128-bit-unpredictable sources", 512, 64, 128, 128, 64)
print()
# where exactly does it break, as a function of q?
print("q-dependence is only additive-logarithmic, k=256, sigma=64, logN=512:")
for logq in [0, 1, 8, 32, 64, 128]:
    sp=64+1024; qp=2.0**logq+1
    print(f"   q=2^{logq:<4} -> (H2) allows log2 M <= {256+math.log2(sp*qp)-2:.1f}")
