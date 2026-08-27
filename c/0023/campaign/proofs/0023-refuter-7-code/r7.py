"""
r7.py -- artifact 0023-refuter-7 (refuter, cycle 4).

ONE QUESTION: the WINDOWED PAYMENT

    pi_tau(A,B) = sum_{i in W_tau(B)} Inf_i(f_A) + sum_{i in W_tau(A)} Inf_i(f_B),
    W_tau(A)    = M(A) union H_tau(A),
    H_tau(A)    = { i : Inf_i(f_A) >= tau },
    M(A)        = support of A MAXIMUM-DEGREE MONOMIAL of 1_A,

on the k-fold direct sum of the "hub witness", at tau = c/(2 D^4).

EXACT ARITHMETIC ONLY.  Fourier coefficients come from an integer fast
Walsh-Hadamard transform (int64, no rounding: |chat| <= 2^N <= 2^15, squares and
their sums fit); influences are python Fractions.  Cross-checked against the
boundary formula Inf_i(f_A) = b_i(A)/(2|A|) (independent derivation, no FFT).

CONVENTIONS.  A point x in {+-1}^N is the index m in [0,2^N); bit i of m is 0
for x_i=+1 and 1 for x_i=-1.  chi_S(x) = (-1)^{popcount(S & m)}.  A set is a
0/1 numpy array over the 2^N points.
"""

import sys
from fractions import Fraction
from itertools import product as iproduct
import numpy as np

rng = np.random.default_rng(20260828)

# ----------------------------------------------------------------- exact core

def fwht(a):
    """integer Walsh-Hadamard: returns chat[S] = sum_m a[m] (-1)^{pc(S&m)}."""
    a = np.array(a, dtype=np.int64)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            x = a[i:i + h].copy()
            y = a[i + h:i + 2 * h].copy()
            a[i:i + h] = x + y
            a[i + h:i + 2 * h] = x - y
        h *= 2
    return a


def popcounts(n):
    return np.bitwise_count(np.arange(n, dtype=np.uint64)).astype(np.int64)


def spec(a, N):
    """(chat, deg, |A|) for the 0/1 array a over 2^N points."""
    chat = fwht(a)
    pc = popcounts(1 << N)
    nz = chat != 0
    deg = int(pc[nz].max()) if nz.any() else 0
    return chat, deg, int(a.sum())


def influences_fourier(a, N):
    """exact Fractions Inf_i(f_A) = (sum_{S ni i} chat(S)^2)/(2^N |A|)."""
    chat, deg, nA = spec(a, N)
    sq = chat.astype(object) ** 2          # python ints: no overflow, ever
    idx = np.arange(1 << N)
    out = []
    for i in range(N):
        m = (idx >> i) & 1 == 1
        out.append(Fraction(int(sq[m].sum()), (1 << N) * nA))
    return out, deg, nA, chat


def influences_boundary(a, N):
    """independent method: Inf_i(f_A) = b_i(A)/(2|A|), b_i = |{x in A: x^i notin A}|."""
    nA = int(a.sum())
    idx = np.arange(1 << N)
    out = []
    for i in range(N):
        flipped = a[idx ^ (1 << i)]
        b = int(((a == 1) & (flipped == 0)).sum())
        out.append(Fraction(b, 2 * nA))
    return out


def maxdeg_supports(chat, deg, N):
    """all S with |S| = deg and chat(S) != 0 (the candidate M's)."""
    pc = popcounts(1 << N)
    return [int(S) for S in np.nonzero((pc == deg) & (chat != 0))[0]]


def pay(IA, IB, MA, MB, tau, N):
    """(pi_min, pi_max, windows) over the choice of the max-degree monomials.
       The two halves are independent, so each is optimised separately."""
    HA = [i for i in range(N) if IA[i] >= tau]
    HB = [i for i in range(N) if IB[i] >= tau]
    baseA = sum((IB[i] for i in HA), Fraction(0))   # paid by W(A) into f_B
    baseB = sum((IA[i] for i in HB), Fraction(0))   # paid by W(B) into f_A
    hA = set(HA)
    hB = set(HB)

    def extra(cands, I, H):
        vals = []
        for S in cands:
            v = sum((I[i] for i in range(N)
                     if ((S >> i) & 1) and i not in H), Fraction(0))
            vals.append((v, S))
        return min(vals), max(vals)

    (eAmin, SAmin), (eAmax, SAmax) = extra(MA, IB, hA)
    (eBmin, SBmin), (eBmax, SBmax) = extra(MB, IA, hB)
    pi_min = baseA + eAmin + baseB + eBmin
    pi_max = baseA + eAmax + baseB + eBmax
    info = dict(HA=HA, HB=HB, SAmin=SAmin, SBmin=SBmin,
                WAmin=sorted(hA | {i for i in range(N) if (SAmin >> i) & 1}),
                WBmin=sorted(hB | {i for i in range(N) if (SBmin >> i) & 1}))
    return pi_min, pi_max, info


def pi_rel(IA, IB, N):
    S = [i for i in range(N) if IA[i] > 0 and IB[i] > 0]
    return sum((IA[i] + IB[i] for i in S), Fraction(0)), S


def analyse(a, b, N, tau, label, verbose=True, check=True):
    IA, degA, nA, chatA = influences_fourier(a, N)
    IB, degB, nB, chatB = influences_fourier(b, N)
    if check:
        assert IA == influences_boundary(a, N), "method mismatch A"
        assert IB == influences_boundary(b, N), "method mismatch B"
        assert int((a * b).sum()) == 0, "not cross-disjoint"
        assert nA > 0 and nB > 0
    MA = maxdeg_supports(chatA, degA, N)
    MB = maxdeg_supports(chatB, degB, N)
    pmin, pmax, info = pay(IA, IB, MA, MB, tau, N)
    prel, S = pi_rel(IA, IB, N)
    if verbose:
        print(f"  [{label}] N={N} degA={degA} degB={degB} "
              f"alpha={Fraction(nA,1<<N)} beta={Fraction(nB,1<<N)} "
              f"#M(A)={len(MA)} #M(B)={len(MB)}")
        print(f"      tau={tau} = {float(tau):.6g}")
        print(f"      Inf(f_A) = {[str(x) for x in IA]}")
        print(f"      Inf(f_B) = {[str(x) for x in IB]}")
        print(f"      H_tau(A)={info['HA']}  H_tau(B)={info['HB']}")
        print(f"      W_tau(A)={info['WAmin']}  W_tau(B)={info['WBmin']} "
              f"(at the minimising M)")
        print(f"      pi_rel   = {prel} = {float(prel):.6g}   |S|={len(S)}")
        print(f"      pi_tau   MIN = {pmin} = {float(pmin):.6g}")
        print(f"      pi_tau   MAX = {pmax} = {float(pmax):.6g}")
    return dict(degA=degA, degB=degB, nA=nA, nB=nB, N=N,
                pmin=pmin, pmax=pmax, prel=prel, info=info, IA=IA, IB=IB)


# --------------------------------------------------------------- the witness

def hub_block(d):
    """A_d, B_d over N=d+1 coords: u = coords 0..d-1, hub w = coord d.
       p = all-plus  (u-index 0);  q = p with coord 0 flipped (u-index 1).
       A_d = {(u,+1): u != p} u {(u,-1): u = q};  B_d = complement."""
    N = d + 1
    a = np.zeros(1 << N, dtype=np.int64)
    for m in range(1 << N):
        u = m & ((1 << d) - 1)
        w_minus = (m >> d) & 1
        if w_minus == 0:
            a[m] = 1 if u != 0 else 0
        else:
            a[m] = 1 if u == 1 else 0
    return a, 1 - a


def blockwise(ablocks, N, d, k, rule):
    """compose k blocks of (d+1) coords.  rule in {'P','C','X'}."""
    nb = d + 1
    tot = 1 << N
    idx = np.arange(tot)
    pats = [(idx >> (j * nb)) & ((1 << nb) - 1) for j in range(k)]
    inA = [ablocks[j][pats[j]] for j in range(k)]
    if rule == 'P':                        # A = prod A_d , B = prod B_d
        A = np.ones(tot, dtype=np.int64)
        B = np.ones(tot, dtype=np.int64)
        for j in range(k):
            A *= inA[j]
            B *= (1 - inA[j])
        return A, B
    if rule == 'C':                        # A = prod A_d , B = complement of A
        A = np.ones(tot, dtype=np.int64)
        for j in range(k):
            A *= inA[j]
        return A, 1 - A
    if rule == 'X':                        # A = odd # of blocks in A_d, B = comp
        s = np.zeros(tot, dtype=np.int64)
        for j in range(k):
            s += inA[j]
        A = (s % 2).astype(np.int64)
        return A, 1 - A
    raise ValueError(rule)


# ------------------------------------------------------------------- drivers

def tau_of(D, c=Fraction(1)):
    return c / (2 * D ** 4)


def sec1():
    print("=" * 78)
    print("SECTION 1.  The hub witness itself (k=1): degree, density, influences,")
    print("            pi_tau at tau = c/(2 d^4), c = 1.   d = 2..6.")
    print("=" * 78)
    rows = []
    for d in range(2, 7):
        a, b = hub_block(d)
        N = d + 1
        tau = tau_of(d)
        print(f"\n d = {d}")
        r = analyse(a, b, N, tau, f"hub d={d}")
        # tau = infinity version (window = M only)
        r_inf = analyse(a, b, N, Fraction(10 ** 9), f"hub d={d}, tau=inf",
                        verbose=False)
        print(f"      [tau = infinity, i.e. W = M only]  "
              f"pi MIN = {r_inf['pmin']} = {float(r_inf['pmin']):.6g}, "
              f"MAX = {r_inf['pmax']} = {float(r_inf['pmax']):.6g}")
        rows.append((d, r, r_inf))
    print("\n TABLE 1  (k=1)")
    print(" d | deg | alpha | pi_rel | pi_tau MIN | pi_tau MAX | pi_inf MIN | pi_inf MAX")
    for d, r, ri in rows:
        print(f" {d} |  {r['degA']}  | {Fraction(r['nA'], 1<<r['N'])} | "
              f"{r['prel']} | {r['pmin']} | {r['pmax']} | {ri['pmin']} | {ri['pmax']}")
    return rows


def sec2():
    print("\n" + "=" * 78)
    print("SECTION 2.  k-fold DIRECT SUM, d <= 4, k <= 3, N <= 15.")
    print("            Rule P: A = prod_j A_d , B = prod_j B_d  (the stated rule)")
    print("            Rule C: A = prod_j A_d , B = complement of A")
    print("            Rule X: A = {odd # blocks in A_d}, B = complement")
    print("=" * 78)
    table = []
    for d in range(2, 5):
        for k in range(1, 4):
            N = k * (d + 1)
            if N > 15:
                print(f"  (skip d={d}, k={k}: N={N} > 15)")
                continue
            ab = [hub_block(d) for _ in range(k)]
            ablocks = [x[0] for x in ab]
            for rule in ('P', 'C', 'X'):
                A, B = blockwise(ablocks, N, d, k, rule)
                if A.sum() == 0 or B.sum() == 0:
                    print(f"  d={d} k={k} rule={rule}: DEGENERATE (empty side)")
                    continue
                # degrees first, then tau from the COMPOSED degree D
                _, degA, _ = spec(A, N)
                _, degB, _ = spec(B, N)
                D = max(degA, degB)
                print(f"\n d={d} k={k} rule={rule}  (composed degree D={D})")
                r = analyse(A, B, N, tau_of(D), f"d{d}k{k}{rule} tau=c/2D^4")
                r2 = analyse(A, B, N, tau_of(d), f"d{d}k{k}{rule} tau=c/2d^4",
                             verbose=False)
                rinf = analyse(A, B, N, Fraction(10 ** 9), "tau=inf",
                               verbose=False)
                print(f"      [same pair, tau = c/(2 d^4) with the BLOCK d={d}]"
                      f"  pi MIN = {r2['pmin']} = {float(r2['pmin']):.6g}")
                print(f"      [tau = infinity, W = M only]                     "
                      f"  pi MIN = {rinf['pmin']} = {float(rinf['pmin']):.6g}")
                table.append((d, k, rule, N, D, Fraction(int(A.sum()), 1 << N),
                              Fraction(int(B.sum()), 1 << N),
                              r['prel'], r['pmin'], r['pmax'],
                              r2['pmin'], rinf['pmin']))
    print("\n TABLE 2  (direct sums; tau = 1/(2 D^4) unless noted)")
    print(" d k rule |  N | D  | alpha | beta | pi_rel | piT MIN | piT MAX |"
          " piT MIN (tau=1/2d^4) | pi_inf MIN")
    for row in table:
        d, k, rule, N, D, al, be, prel, pmin, pmax, p2, pinf = row
        print(f" {d} {k}  {rule}   | {N:2d} | {D:2d} | {al} | {be} | "
              f"{prel} | {pmin} | {pmax} | {p2} | {pinf}")
    return table


def sec3():
    """Fragility hunt 1: structured families that attack the tau-window."""
    print("\n" + "=" * 78)
    print("SECTION 3.  Fragility hunt A -- structured attacks on the tau window.")
    print("=" * 78)

    # (3a) s-fold hub: A = {x_S = a}, B = {x_S != a}, both cylinders.
    print("\n (3a) 'thin-dependence' pair: A = {x_S = all-plus} x cube,")
    print("      B = {x_S != all-plus} x cube.  B's influence on S is ~2^-s,")
    print("      hence tau-LIGHT once 2^s > d^4 -- but M(B) must contain S.")
    for s in range(1, 8):
        N = s
        idx = np.arange(1 << N)
        A = (idx == 0).astype(np.int64)
        B = 1 - A
        _, dA, _ = spec(A, N)
        _, dB, _ = spec(B, N)
        D = max(dA, dB)
        r = analyse(A, B, N, tau_of(D), f"s={s}", verbose=False)
        IB = r['IB']
        print(f"   s={s}: D={D}  Inf_i(f_B)={IB[0]}  tau={tau_of(D)}  "
              f"B-heavy? {IB[0] >= tau_of(D)}  "
              f"pi_tau MIN={r['pmin']} ({float(r['pmin']):.4g})  "
              f"pi_rel={r['prel']}")

    # (3b) ADDRESS function: A = ADDR^{-1}(1), B = ADDR^{-1}(0) (complementary).
    print("\n (3b) ADDRESS function (k address bits, 2^k data bits): the")
    print("      Nisan-Szegedy-extremal spread -- ~2^d relevant coordinates of")
    print("      influence ~2^-d each, but the address bits stay heavy.")
    for kk in (1, 2, 3):
        N = kk + (1 << kk)
        if N > 12:
            break
        idx = np.arange(1 << N)
        addr = idx & ((1 << kk) - 1)                 # address bits = 0..kk-1
        data = (idx >> kk)
        val = (data >> addr) & 1                     # selected data bit
        A = (val == 0).astype(np.int64)              # data bit = +1
        B = 1 - A
        _, dA, _ = spec(A, N)
        D = dA
        r = analyse(A, B, N, tau_of(D), f"ADDR k={kk}", verbose=False)
        print(f"   k={kk}: N={N} D={D} #rel={sum(1 for x in r['IA'] if x>0)}  "
              f"tau={tau_of(D)}  |H_tau(A)|={len(r['info']['HA'])}  "
              f"pi_rel={r['prel']}  pi_tau MIN={r['pmin']} "
              f"({float(r['pmin']):.4g})")

    # (3c) hub witness with the hub REPLACED by a parity of h coordinates,
    #      to try to make the shared heavy coordinate light.
    print("\n (3c) hub-of-parity: replace the single hub w by the parity of h")
    print("      coordinates (A = {par=+1, u != p} u {par=-1, u=q}).")
    for d in (2, 3):
        for h in (1, 2, 3):
            N = d + h
            if N > 12:
                continue
            idx = np.arange(1 << N)
            u = idx & ((1 << d) - 1)
            par = np.bitwise_count((idx >> d).astype(np.uint64)).astype(np.int64) % 2
            A = np.where(par == 0, (u != 0).astype(np.int64),
                         (u == 1).astype(np.int64))
            B = 1 - A
            _, dA, _ = spec(A, N)
            D = dA
            r = analyse(A, B, N, tau_of(D), f"hubpar d={d} h={h}", verbose=False)
            print(f"   d={d} h={h}: N={N} D={D} tau={tau_of(D)} "
                  f"H(A)={r['info']['HA']} pi_rel={r['prel']} "
                  f"pi_tau MIN={r['pmin']} ({float(r['pmin']):.4g}) "
                  f"pi_inf MIN={analyse(A,B,N,Fraction(10**9),'',verbose=False)['pmin']}")


def sec4(Ns=(5, 6, 7), trials=240, steps=4000):
    """Fragility hunt 2: exhaustive at N<=3, randomised local search above."""
    print("\n" + "=" * 78)
    print("SECTION 4.  Fragility hunt B -- complete sweep at N<=3, then")
    print("            local search (min pi_tau MIN) at N=5,6,7 under deg<=D.")
    print("=" * 78)

    # complete sweep, N <= 3, all cross-disjoint pairs
    for N in (2, 3):
        tot = 1 << N
        best = None
        cnt = 0
        for A in range(1, 1 << tot):
            av = np.array([(A >> m) & 1 for m in range(tot)], dtype=np.int64)
            comp = ((1 << tot) - 1) & ~A
            sub = comp
            while True:
                if sub:
                    bv = np.array([(sub >> m) & 1 for m in range(tot)],
                                  dtype=np.int64)
                    _, dA, _ = spec(av, N)
                    _, dB, _ = spec(bv, N)
                    D = max(dA, dB, 1)
                    r = analyse(av, bv, N, tau_of(D), "", verbose=False,
                                check=False)
                    cnt += 1
                    if best is None or r['pmin'] < best[0]:
                        best = (r['pmin'], A, sub, D, r['prel'])
                if sub == 0:
                    break
                sub = (sub - 1) & comp
        print(f"   N={N}: {cnt} cross-disjoint pairs swept, "
              f"min pi_tau MIN = {best[0]} = {float(best[0]):.6g} "
              f"(A={best[1]:#0x}, B={best[2]:#0x}, D={best[3]}, "
              f"pi_rel={best[4]})")

    # local search, started at FEASIBLE points (disjoint codim-<=Dcap subcubes)
    def subcube(N, cod, tot):
        idx = np.arange(tot)
        coords = rng.choice(N, size=cod, replace=False)
        vals = rng.integers(0, 2, size=cod)
        m = np.ones(tot, dtype=bool)
        for c, v in zip(coords, vals):
            m &= (((idx >> int(c)) & 1) == int(v))
        return m.astype(np.int64), coords, vals

    for N in Ns:
        tot = 1 << N
        Dcap = 3
        globalbest = None
        for t in range(trials):
            a, ca, va = subcube(N, Dcap, tot)
            # force a disjoint partner: flip one fixed coordinate's value
            j = int(rng.integers(Dcap))
            idx = np.arange(tot)
            b = np.ones(tot, dtype=bool)
            for u, (c, v) in enumerate(zip(ca, va)):
                w = int(v) ^ (1 if u == j else 0)
                b &= (((idx >> int(c)) & 1) == w)
            b = b.astype(np.int64)
            if a.sum() == 0 or b.sum() == 0:
                continue

            def score(a, b):
                """lexicographic: (degree violation, pi_tau MIN).  Infeasible
                   starts are allowed and are driven into the deg<=Dcap set."""
                _, dA, nA = spec(a, N)
                _, dB, nB = spec(b, N)
                if nA == 0 or nB == 0:
                    return None
                viol = max(0, max(dA, dB) - Dcap)
                D = max(dA, dB, 1)
                r = analyse(a, b, N, tau_of(D), "", verbose=False, check=False)
                return (viol, r['pmin']), r

            cur = score(a, b)
            if cur is None:
                continue
            for st in range(steps // 20):
                m = int(rng.integers(tot))
                which = int(rng.integers(3))
                a2, b2 = a.copy(), b.copy()
                if which == 0:
                    a2[m] ^= 1
                    if a2[m] and b2[m]:
                        b2[m] = 0
                elif which == 1:
                    b2[m] ^= 1
                    if a2[m] and b2[m]:
                        a2[m] = 0
                else:
                    a2[m], b2[m] = b2[m], a2[m]
                nxt = score(a2, b2)
                if nxt is not None and nxt[0] <= cur[0]:
                    a, b, cur = a2, b2, nxt
            if cur[0][0] == 0 and (globalbest is None or cur[0][1] < globalbest[0]):
                globalbest = (cur[0][1], a.copy(), b.copy(), cur[1])
        if globalbest is not None:
            pm, a, b, r = globalbest
            print(f"   N={N} (deg<={Dcap}, {trials} restarts x {steps//20} moves): "
                  f"min pi_tau MIN found = {pm} = {float(pm):.6g}; "
                  f"pi_rel there = {r['prel']}; "
                  f"|A|={int(a.sum())} |B|={int(b.sum())} "
                  f"H(A)={r['info']['HA']} H(B)={r['info']['HB']}")


def sec5():
    """Why every search above is VACUOUS: the relevant-coordinate influence
       floor Inf_i(1_A) >= 2^{-1-deg}, verified exhaustively, and the resulting
       threshold in d below which H_tau(A) = Rel(A) identically."""
    print("\n" + "=" * 78)
    print("SECTION 5.  The floor  Inf_i(1_A) >= 2^{-1-deg(1_A)}  for every")
    print("            RELEVANT i  (from |supp(partial_i 1_A)| >= 2^{-(d-1)}),")
    print("            exhaustively verified, and the d-threshold it forces.")
    print("=" * 78)
    for N in (2, 3, 4):
        tot = 1 << N
        worst = None
        bad = 0
        for A in range(1, 1 << tot):
            av = np.array([(A >> m) & 1 for m in range(tot)], dtype=np.int64)
            chat, deg, nA = spec(av, N)
            I1 = [Fraction(int((chat.astype(object) ** 2)[
                np.arange(tot) >> i & 1 == 1].sum()), 1 << (2 * N))
                  for i in range(N)]
            for i in range(N):
                if I1[i] > 0:
                    ratio = I1[i] / Fraction(1, 1 << (1 + deg))
                    if ratio < 1:
                        bad += 1
                    if worst is None or ratio < worst[0]:
                        worst = (ratio, A, i, deg, I1[i])
        print(f"   N={N}: all {(1<<tot)-1} nonempty sets, every relevant "
              f"coordinate: violations = {bad}; tightest ratio "
              f"Inf_i(1_A)/2^-(1+deg) = {worst[0]} at A={worst[1]:#0x}, i={worst[2]}, "
              f"deg={worst[3]}, Inf={worst[4]}")

    print("\n   CONSEQUENCE.  For a cross-disjoint pair with deg <= d, every")
    print("   relevant i has Inf_i(f_A) = Inf_i(1_A)/alpha >= 2^{-1-d}/alpha")
    print("   >= 2^{-1-d} (alpha <= 1).  So a RELEVANT coordinate can be")
    print("   tau-LIGHT only if 2^{-1-d} < tau = c/(2 d^4), i.e. 2^d > d^4/c.")
    print("   Below that threshold H_tau(A) = Rel(A) and H_tau(B) = Rel(B)")
    print("   EXACTLY, hence pi_tau = pi_rel >= 1 (0023-refuter-5).")
    print("\n   d  | 2^d      | d^4/c, c=1/2 | c=1    | c=3/2  | light possible?"
          "  (c=1/2 | 1 | 3/2)")
    for d in range(2, 25):
        t = []
        for c in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
            t.append("Y" if Fraction(1, 1 << (1 + d)) < c / (2 * d ** 4) else "n")
        print(f"   {d:2d} | {1<<d:8d} | {float(d**4/0.5):12.0f} | {d**4:6d} | "
              f"{float(d**4/1.5):6.0f} | {t[0]} | {t[1]} | {t[2]}")
    print("\n   Same table for the side with alpha <= 1/2 (Inf_i(f_A) >= 2^-d):")
    for d in range(2, 25):
        t = []
        for c in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
            t.append("Y" if Fraction(1, 1 << d) < c / (2 * d ** 4) else "n")
        print(f"   d={d:2d}: light possible?  c=1/2:{t[0]}  c=1:{t[1]}  c=3/2:{t[2]}")


def sec6():
    """Closed form for the (3a) family beyond brute-force reach, exact."""
    print("\n" + "=" * 78)
    print("SECTION 6.  Family (3a) pushed past N=15 in CLOSED FORM (exact),")
    print("            the one family that does reach the tau-light regime.")
    print("            A = {x_S = all-plus}, B = complement, N = s, D = s.")
    print("            Inf_i(f_A) = 1/2 ; Inf_i(f_B) = 1/(2(2^s-1)) ; M(B) = S.")
    print("=" * 78)
    print("   s  | tau=1/(2s^4) | Inf_i(f_B)      | B-light? | pi_rel   | pi_tau")
    for s in list(range(2, 8)) + [10, 14, 16, 17, 18, 20, 24, 30, 40]:
        tau = Fraction(1, 2 * s ** 4)
        ib = Fraction(1, 2 * ((1 << s) - 1))
        light = ib < tau
        prel = s * (Fraction(1, 2) + ib)
        # W_tau(B) = M(B) = S (unique top monomial of 1_B = 1 - 1_A) always;
        # W_tau(A) = S too.  So pi_tau = pi_rel whether or not B is light.
        ptau = prel
        print(f"   {s:2d}  | {str(tau):12s} | {str(ib):15s} | "
              f"{'YES' if light else 'no ':8s} | {str(prel):8s} | {str(ptau)}")
    print("   (brute force above agrees exactly for s<=7; the s>=17 rows are the")
    print("    tau-LIGHT regime, and pi_tau does not move: M(B) carries it.)")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "5"):
        sec5()
    if which in ("all", "6"):
        sec6()
    if which in ("all", "1"):
        sec1()
    if which in ("all", "2"):
        sec2()
    if which in ("all", "3"):
        sec3()
    if which in ("all", "4"):
        sec4()
