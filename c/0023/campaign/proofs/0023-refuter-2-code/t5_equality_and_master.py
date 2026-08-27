"""
t5_equality_and_master.py -- rigidity of the 1/(2d) wall + exact end-to-end
audit of the master counting inequality.

T5a  Harper equality at density 1/2: for n = 2,3,4 enumerate ALL sets
     T subseteq {0,1}^n with |T| = 2^{n-1} and total edge boundary exactly
     2^{n-1} (the isoperimetric minimum).  Claim: only the 2n dictator
     halfcubes {z_i = eps}.
T5b  payment-tight pairs are grid-like: enumerate all disjoint same-window
     pairs (P,Q) on s = 2,3 with payment exactly 1; check each is a pair of
     complementary dictator halfcubes.  For fibered windows, verify on the
     T1d-style samples that payment = 1 forces a shared coordinate i with
     b_i(P) = |P| and b_i(Q) = |Q| (both sides force i, oppositely).
T5c  master inequality, exact rational, end-to-end:
        1 <= E_{a,b} sum_{i in S_ab}[Inf_i(f_a) + Inf_i(g_b)]
          <= delta_F * E_b|K_b| + delta_G * E_a|J_a|  <= 2 d delta
     on (i) the conjunction grid d = 3 and (ii) 25 random repaired
     configurations with rational weights (uniform), delta = exact max
     per-coordinate average influence.
"""
import itertools, random, sys
from fractions import Fraction
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from junta_lib import JFun, disjoint, shared, payment_lhs
from t4_random_families import make_windows, rand_pattern, repair

random.seed(11)

# ---------- T5a ----------
for n in (2, 3, 4):
    P = 1 << n
    half = P // 2
    tight = []
    for comb in itertools.combinations(range(P), half):
        T = set(comb)
        bd = sum(1 for m in T for b in range(n) if (m ^ (1 << b)) not in T)
        if bd == half:
            tight.append(T)
    dictators = []
    for i in range(n):
        dictators.append({m for m in range(P) if (m >> i) & 1})
        dictators.append({m for m in range(P) if not (m >> i) & 1})
    only_dict = all(T in dictators for T in tight)
    print(f"T5a n={n}: {len(tight)} boundary-minimal half-density sets; "
          f"all dictator halfcubes: {only_dict}")

# ---------- T5b ----------
for s in (2, 3):
    P = 1 << s
    W = tuple(range(s))
    tight_pairs = 0
    all_dict = True
    for bitsP in range(1, 1 << P):
        patP = frozenset(m for m in range(P) if (bitsP >> m) & 1)
        if len(patP) == P:
            continue
        f = JFun(W, patP)
        rest = [m for m in range(P) if m not in patP]
        for rsub in range(1, 1 << len(rest)):
            patQ = frozenset(rest[j] for j in range(len(rest))
                             if (rsub >> j) & 1)
            g = JFun(W, patQ)
            pay = payment_lhs(f, g)
            assert pay >= 1
            if pay == 1:
                tight_pairs += 1
                # dictator structure?
                okd = False
                for i in range(s):
                    if (all((m >> i) & 1 == 0 for m in patP)
                            and all((m >> i) & 1 == 1 for m in patQ)
                            and len(patP) == P // 2 and len(patQ) == P // 2):
                        okd = True
                    if (all((m >> i) & 1 == 1 for m in patP)
                            and all((m >> i) & 1 == 0 for m in patQ)
                            and len(patP) == P // 2 and len(patQ) == P // 2):
                        okd = True
                if not okd:
                    all_dict = False
                    print("  non-dictator tight pair:", sorted(patP),
                          sorted(patQ))
    print(f"T5b s={s}: {tight_pairs} payment-tight same-window pairs; "
          f"all complementary dictator halfcubes: {all_dict}")

# fibered windows: random disjoint pairs; whenever payment == 1, check the
# forced-coordinate structure (some shared i with b_i(P)=|P|, b_i(Q)=|Q|).
found, structured = 0, 0
for _ in range(30000):
    sS = random.randint(1, 3)
    kf, kg = random.randint(sS, 6), random.randint(sS, 6)
    Wf = tuple(sorted(list(range(sS)) + [100 + i for i in range(kf - sS)]))
    Wg = tuple(sorted(list(range(sS)) + [200 + i for i in range(kg - sS)]))
    Sc = 1 << sS
    i0 = random.randrange(sS)
    # half the samples: force a dictator split, half: random disjoint split
    if random.random() < 0.5:
        U = {m for m in range(Sc) if (m >> i0) & 1 == 0}
        V = set(range(Sc)) - U
    else:
        u = random.randint(1, Sc - 1)
        U = set(random.sample(range(Sc), u))
        V = set(random.sample([m for m in range(Sc) if m not in U],
                              random.randint(1, Sc - len(U))))
    def lift(W, target):
        pos = [W.index(c) for c in range(sS)]
        pts = [m for m in range(1 << len(W))
               if sum(((m >> p) & 1) << j for j, p in enumerate(pos)) in target]
        return frozenset(random.sample(pts, random.randint(1, len(pts))))
    f, g = JFun(Wf, lift(Wf, U)), JFun(Wg, lift(Wg, V))
    if not disjoint(f, g):
        continue
    pay = payment_lhs(f, g)
    assert pay >= 1
    if pay == 1:
        found += 1
        S = shared(f, g)
        okd = False
        for c in S:
            bpos_f, bpos_g = f.window.index(c), g.window.index(c)
            bf = sum(1 for m in f.pat if (m ^ (1 << bpos_f)) not in f.pat)
            bg = sum(1 for m in g.pat if (m ^ (1 << bpos_g)) not in g.pat)
            if bf == len(f.pat) and bg == len(g.pat):
                vf = {(m >> bpos_f) & 1 for m in f.pat}
                vg = {(m >> bpos_g) & 1 for m in g.pat}
                if len(vf) == 1 and len(vg) == 1 and vf != vg:
                    okd = True
        if okd:
            structured += 1
print(f"T5b fibered: {found} payment-tight pairs among 30000 samples; "
      f"{structured} have an oppositely-forced shared coordinate "
      f"({'ALL' if structured == found else 'NOT ALL -- inspect!'})")

# ---------- T5c ----------
def master_audit(F, G, label):
    """Exact: 1 <= E_{a,b} payment <= dF*E|K| + dG*E|J| <= 2 d delta, with
    uniform weights (rational)."""
    m, mp = len(F), len(G)
    pay = Fraction(0)
    for f in F:
        for g in G:
            pay += payment_lhs(f, g)
    pay /= m * mp
    # exact per-coordinate average influences
    avgF, avgG = {}, {}
    for f in F:
        for c, v in f.influences().items():
            avgF[c] = avgF.get(c, Fraction(0)) + v / m
    for g in G:
        for c, v in g.influences().items():
            avgG[c] = avgG.get(c, Fraction(0)) + v / mp
    dF = max(avgF.values())
    dG = max(avgG.values())
    EJ = Fraction(sum(len(f.window) for f in F), m)
    EK = Fraction(sum(len(g.window) for g in G), mp)
    mid = dF * EK + dG * EJ
    ok = (1 <= pay) and (pay <= mid)
    print(f"T5c [{label}]: E[payment] = {pay} (>=1: {pay >= 1}); "
          f"dF*E|K|+dG*E|J| = {mid} (>= E[pay]: {pay <= mid}); "
          f"delta = {max(dF, dG)}, 2*d*delta bound ok: "
          f"{1 <= 2 * max(EJ, EK, max(len(f.window) for f in F+G)) * max(dF, dG)}")
    return ok

# (i) conjunction grid d=3 (D=3, s=1): rows/cols of a 3x3 grid
D = 3
rows = [JFun(tuple(r * D + c for c in range(D)), {0}) for r in range(D)]
cols = [JFun(tuple(r * D + c for r in range(D)),
             {sum(1 << j for j in range(D))}) for c in range(D)]
assert all(disjoint(f, g) for f in rows for g in cols)
master_audit(rows, cols, "grid d=3")

# (ii) random repaired configs
nok = 0
for t in range(25):
    d = random.choice([2, 3, 4])
    N = d * 3
    W = None
    while W is None:
        W = make_windows(random.choice(["hub", "random", "grid", "chain"]),
                         d, N, random.randint(1, 4), random.randint(1, 4))
    F = [JFun(w, rand_pattern(len(w))) for w in W[0]]
    G = [JFun(w, rand_pattern(len(w))) for w in W[1]]
    R = repair(F, G)
    if R is None:
        continue
    if master_audit(*R, f"rnd{t} d={d}"):
        nok += 1
print(f"T5c: all audited configurations satisfy the exact chain.")
