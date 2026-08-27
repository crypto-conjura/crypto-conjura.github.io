"""
h1_baselines.py -- exact report cards for the two reference pairs:

  (W)  the CERTIFIED WITNESS: A = codimension-d subcube, B = complement.
  (E)  the family E_d of 0023-prover-4-u3 section 3.

Everything exact (Fractions + integer Walsh-Hadamard); each influence is
computed twice, by the boundary route and by the Fourier route, and lib8.card
asserts they agree.
"""
import sys, os
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import *


def witness(d, N=None):
    """A = {x_0=..=x_{d-1}=+1}; B = complement."""
    N = N if N is not None else d
    A = subcube(N, range(d), [1] * d)
    return A, complement(A, N)


def Ed(d, N=None):
    """E_d:  K={0..d-1}, t=d, u=(+1..+1), v=(-1,+1,..,+1).
       A = {x_t=+1, x_K != u} u {x_t=-1, x_K=v};  B = complement."""
    N = N if N is not None else d + 1
    uK, vK = 0, 1                      # bit patterns on K (bit set = -1)
    tb = 1 << d
    mK = (1 << d) - 1

    def pred(m):
        if (m >> d) & 1 == 0:          # x_t = +1
            return (m & mK) != uK
        return (m & mK) == vK
    A = from_pred(N, pred)
    return A, complement(A, N)


def show(r, extra=()):
    print(f"  {r['label']}: N={r['N']} |A|={r['sizes'][0]} |B|={r['sizes'][1]} "
          f"alpha={r['alpha']} deg=({r['degA']},{r['degB']}) "
          f"#topA={r['ntopA']} #topB={r['ntopB']}")
    print(f"     topA (<=4) {r['topA']}   topB (<=4) {r['topB']}")
    print(f"     Q  = {fmt(r['Q'])}   at coord {r['Qarg']}")
    print(f"     pi_M in [{fmt(r['piM_min'])} , {fmt(r['piM_max'])}]  "
          f"(over all choices of maximum-degree supports)")
    print(f"     max_i Inf_i(f_A) = {fmt(r['maxIA'])}   "
          f"max_i Inf_i(f_B) = {fmt(r['maxIB'])}")
    if 'pi_tau' in r:
        print(f"     tau={fmt(r['tau'])}  pi_tau={fmt(r['pi_tau'])} "
              f"|W(A)|={len(r['WA'])} |W(B)|={len(r['WB'])}")
    for k in extra:
        print(f"     {k}: {r[k]}")


print("=" * 78)
print("(W) CERTIFIED WITNESS  A = codim-d subcube, B = complement")
print("=" * 78)
for d in range(2, 11):
    A, B = witness(d)
    r = card(A, B, d, label=f"W d={d}")
    show(r)
    # closed forms
    pred_Q = Fraction(1, 2 * (2 ** d - 1))
    pred_piM = Fraction(d, 2) + Fraction(d, 2 * (2 ** d - 1))
    assert r['Q'] == pred_Q, (r['Q'], pred_Q)
    assert r['piM_min'] == r['piM_max'] == pred_piM, (r['piM_min'], pred_piM)
    print(f"     [closed form checks OK]  Q = 1/(2(2^d-1)),  "
          f"pi_M = d/2 + d/(2(2^d-1)) >= 1/2")

print()
print("=" * 78)
print("(E) FAMILY E_d of prover-4-u3")
print("=" * 78)
for d in range(2, 11):
    A, B = Ed(d)
    r = card(A, B, d + 1, label=f"E d={d}")
    show(r)
    pred_Q = Fraction(1 - Fraction(2, 2 ** d), 2)
    pred_piM = Fraction(2 * d, 2 ** d)
    ok_Q = (r['Q'] == pred_Q)
    print(f"     [closed forms]  Q?=(1-2^{{1-d}})/2 -> {ok_Q};  "
          f"pi_M(K,K)?=d*2^{{1-d}}={pred_piM} -> "
          f"{pred_piM in (r['piM_min'], r['piM_max']) or (r['piM_min']<=pred_piM<=r['piM_max'])}")

print()
print("SUMMARY TABLE  (exact)")
print(f"{'d':>3} | {'W: Q':>22} | {'W: pi_M':>16} | {'E: Q':>22} | {'E: pi_M(min)':>16}")
for d in range(2, 13):
    A, B = witness(d); rw = card(A, B, d, label="")
    A, B = Ed(d);      re = card(A, B, d + 1, label="")
    print(f"{d:>3} | {str(rw['Q']):>22} | {str(rw['piM_min']):>16} | "
          f"{str(re['Q']):>22} | {str(re['piM_min']):>16}")
