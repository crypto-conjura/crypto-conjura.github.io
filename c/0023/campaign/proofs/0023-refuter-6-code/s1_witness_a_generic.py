"""
s1 -- witness (a) of 0023-prover-3-r3 §3 (address family with a hub):
ALL MINIMAL certificates of ALL points of A_k and B_k = A_k^c, computed by the
GENERIC brute force of lib6 (no structural input), for k = 1,2,3 (N = 3,6,11).

Deliverables (all exact, Fractions / integers):
  * exact multiset distribution of minimal-certificate SIZES,
  * per-point multiplicity distribution,
  * expected window size E_{x~Unif(A_k)}|W| under the selection rules
    MIN / MAX / UNIF / LEXF / LEXL and the two greedy shrink orders,
  * cross-check against the structural characterisation
        minimal certificates of x  <->  { U subseteq [k] : j_0 + {0,1}^U subseteq P(x) }
        S_U = (addr bits off U) u { targets of j_0 + {0,1}^U },  |S_U| = k-|U|+2^|U|,
    asserted set-for-set (not just size-for-size),
  * the CAP-I / Remark-2.2 ratio  E[pi] / E[|W(A)|+|W(B)|]  under each rule.
"""
import sys, time
import numpy as np
from fractions import Fraction as F
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib6 import (cert_table, minimal_certs_generic, minimal_certs_bruteforce_point,
                  selection_stats, greedy_shrink, degree_of, influences_exact, size)


def build_witness_a(k):
    """returns (N, A_bool, B_bool).  coords 0..k-1 = address bits (bit 0 <-> +1),
    coord k+j = target y_j;  A = {y_{addr} = +1} = {bit(k+addr)=0}."""
    N = k + (1 << k)
    n = 1 << N
    m = np.arange(n, dtype=np.int64)
    addr = m & ((1 << k) - 1)
    tgt_bit = (m >> (k + addr)) & 1
    A = (tgt_bit == 0)
    return N, A, ~A


def struct_mincerts(k, m, want_plus):
    """structural prediction: list of minimal-certificate masks for point m."""
    N = k + (1 << k)
    j0 = m & ((1 << k) - 1)
    P = [j for j in range(1 << k) if (((m >> (k + j)) & 1) == 0) == want_plus]
    Pset = set(P)
    out = []
    for U in range(1 << k):           # U as a bitmask over the k address bits
        # subcube j0 + {0,1}^U inside P ?
        ok = True
        v = U
        while True:
            if (j0 ^ v) not in Pset:
                ok = False
                break
            if v == 0:
                break
            v = (v - 1) & U
        if not ok:
            continue
        S = ((1 << k) - 1) & ~U        # address bits fixed
        v = U
        while True:
            S |= 1 << (k + (j0 ^ v))
            if v == 0:
                break
            v = (v - 1) & U
        out.append(S)
    return out


def ratios(exp_sz, exp_pay):
    return exp_pay / exp_sz


for k in (1, 2, 3):
    t0 = time.time()
    N, A, B = build_witness_a(k)
    d = k + 1
    assert degree_of(A, N) == d and degree_of(B, N) == d
    IA = influences_exact(A, N)
    IB = influences_exact(B, N)
    print(f"\n=== witness (a), k={k}, d={d}, N={N} ===")
    print(f"  deg=d ok; Inf(a_t)={IA[0]}, Inf(y_j)={IA[k]}  (A side); "
          f"B side: {IB[0]}, {IB[k]}")
    out = {}
    for name, X in (("A", A), ("B", B)):
        C = cert_table(X, N)
        mc = minimal_certs_generic(X, N, C)
        # ---- cross-check 1: structural characterisation, set for set
        for m, lst in mc.items():
            pred = struct_mincerts(k, m, want_plus=(name == "A"))
            assert sorted(lst) == sorted(pred), (name, k, m, lst, pred)
        # ---- cross-check 2: independent slow brute force on a sample of points
        pts = sorted(mc)
        for m in pts[:: max(1, len(pts) // 8)]:
            slow = sorted(minimal_certs_bruteforce_point(X, N, m))
            assert slow == sorted(mc[m]), (name, k, m)
        exp, szmset, mult, ppmax, npts = selection_stats(mc, N)
        # greedy shrink, two orders: address bits first, targets first
        g1 = F(0); g2 = F(0)
        order_addr_first = list(range(N))
        order_tgt_first = list(range(N))[::-1]
        for m in pts:
            g1 += size(greedy_shrink(X, N, m, order_addr_first, C))
            g2 += size(greedy_shrink(X, N, m, order_tgt_first, C))
        exp["GREEDY-addr-first"] = g1 / npts
        exp["GREEDY-tgt-first"] = g2 / npts
        out[name] = (exp, szmset, mult, ppmax, npts, mc)
        print(f"  side {name}: |{name}|={npts}")
        print(f"    minimal-cert SIZE multiset (size: count over all (x,cert) pairs): "
              f"{dict(sorted(szmset.items()))}")
        print(f"    per-point multiplicity histogram (#minimal certs: #points): "
              f"{dict(sorted(mult.items()))}")
        print(f"    per-point MAX size histogram: {dict(sorted(ppmax.items()))}")
        for rule in ("MIN", "MAX", "UNIF", "LEXF", "LEXL",
                     "GREEDY-addr-first", "GREEDY-tgt-first"):
            v = exp[rule]
            print(f"    E|W| under {rule:18s} = {v} = {float(v):.6f}   (d={d}, "
                  f"2^(d-1)={1<<(d-1)})")
    # ---- Remark 2.2 ratio E[pi]/E[|W_A|+|W_B|] per rule (independent draws)
    print("  CAP-I(b)/Remark-2.2 ratio  E[pi]/E[|W(A)|+|W(B)|]  per rule:")
    for rule in ("MIN", "MAX", "UNIF", "LEXF", "LEXL",
                 "GREEDY-addr-first", "GREEDY-tgt-first"):
        num = F(0); den = F(0)
        for name, other in (("A", IB), ("B", IA)):
            exp, szmset, mult, ppmax, npts, mc = out[name]
            # recompute the influence-weighted payment under the same rule
            payment = F(0); sz = F(0)
            for m, lst in mc.items():
                sizes = [size(S) for S in lst]
                if rule == "MIN":
                    sel = [S for S in lst if size(S) == min(sizes)]
                elif rule == "MAX":
                    sel = [S for S in lst if size(S) == max(sizes)]
                elif rule == "UNIF":
                    sel = lst
                elif rule == "LEXF":
                    sel = [min(lst, key=lambda S: tuple(i for i in range(N) if (S >> i) & 1))]
                elif rule == "LEXL":
                    sel = [max(lst, key=lambda S: tuple(i for i in range(N) if (S >> i) & 1))]
                elif rule.startswith("GREEDY"):
                    order = list(range(N)) if rule.endswith("addr-first") else list(range(N))[::-1]
                    sel = [greedy_shrink(A if name == "A" else B, N, m, order)]
                for S in sel:
                    payment += sum((other[i] for i in range(N) if (S >> i) & 1), F(0)) / len(sel)
                    sz += F(size(S), len(sel))
            num += payment / len(mc)
            den += sz / len(mc)
        r = num / den
        print(f"    {rule:18s}: E[pi]={num}  E[|W_A|+|W_B|]={den}  ratio={r} "
              f"= {float(r):.6f}")
    print(f"  [{time.time()-t0:.1f}s]")
