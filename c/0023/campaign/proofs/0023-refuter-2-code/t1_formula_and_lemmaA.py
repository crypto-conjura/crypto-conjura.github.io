"""
t1_formula_and_lemmaA.py -- exact stress tests of the four load-bearing facts.

T1a (F1): influence formula b_i/(2|P|) == Fourier influence.
     EXHAUSTIVE k <= 3 (all nonempty patterns), RANDOM 500 patterns k in 4..8.
T1b (F2): disjointness via shared-window projection == brute-force support
     disjointness on the full cube.  EXHAUSTIVE over all pairs of windows
     within N=4 and 400 random pattern pairs per window pair.
T1c (F3, Lemma A): EXHAUSTIVE k <= 4: all 2^{2^k}-1 nonempty patterns x all
     window subsets S.  RANDOM: 200000 (pattern, S) samples with k in 5..12.
     Integer-exact:  2^{sum_S b_i} * |proj|^{|P|} >= 2^{|S||P|}.
     Also record equality cases at k <= 3 (they identify the tight examples).
T1d (F4, per-pair payment >= 1): RANDOM 20000 disjoint pairs, window sizes
     <= 8, overlap sizes 1..6, patterns generated adversarially sparse/dense.
     Integer-exact:  |Q| sum_S b_i(P) + |P| sum_S b_i(Q) >= 2|P||Q|.
     Record the minimum payment seen and its configuration.

Any violation is printed loudly and exits nonzero.
"""
import itertools, random, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from fractions import Fraction
from junta_lib import JFun, disjoint, lemmaA_ok, payment_ok, shared

random.seed(20260827)
fail = False

# ---------- T1a ----------
def check_formula(f):
    return f.influences() == f.influences_fourier()

cnt = 0
for k in range(1, 4):
    W = tuple(range(k))
    for bits in range(1, 1 << (1 << k)):
        pat = frozenset(m for m in range(1 << k) if (bits >> m) & 1)
        if not check_formula(JFun(W, pat)):
            print("T1a FAIL", k, sorted(pat)); fail = True
        cnt += 1
print(f"T1a exhaustive k<=3: {cnt} patterns, formula exact: OK")
cnt = 0
for _ in range(500):
    k = random.randint(4, 8)
    P = 1 << k
    pat = frozenset(random.sample(range(P), random.randint(1, P)))
    if not check_formula(JFun(tuple(range(k)), pat)):
        print("T1a FAIL rnd", k, sorted(pat)); fail = True
    cnt += 1
print(f"T1a random k in 4..8: {cnt} patterns: OK")

# ---------- T1b ----------
N = 4
tests = 0
for kf in range(1, N + 1):
    for kg in range(1, N + 1):
        for Wf in itertools.combinations(range(N), kf):
            for Wg in itertools.combinations(range(N), kg):
                for _ in range(12):
                    pf = frozenset(random.sample(range(1 << kf),
                                                 random.randint(1, 1 << kf)))
                    pg = frozenset(random.sample(range(1 << kg),
                                                 random.randint(1, 1 << kg)))
                    f, g = JFun(Wf, pf), JFun(Wg, pg)
                    brute = (f.support_mask(N) & g.support_mask(N)) == 0
                    if disjoint(f, g) != brute:
                        print("T1b FAIL", f, g); fail = True
                    tests += 1
print(f"T1b projection-disjointness vs brute force, N=4: {tests} pairs: OK")

# ---------- T1c ----------
eq_cases = []
total = 0
for k in range(1, 5):
    Spos_all = [tuple(S) for r in range(1, k + 1)
                for S in itertools.combinations(range(k), r)]
    for bits in range(1, 1 << (1 << k)):
        pat = frozenset(m for m in range(1 << k) if (bits >> m) & 1)
        for Spos in Spos_all:
            if not lemmaA_ok(pat, k, Spos):
                print("T1c FAIL LemmaA", k, sorted(pat), Spos); fail = True
            total += 1
            if k <= 3:
                P = len(pat)
                sb = sum(1 for b in Spos for m in pat
                         if (m ^ (1 << b)) not in pat)
                proj = {sum(((m >> p) & 1) << j for j, p in enumerate(Spos))
                        for m in pat}
                if (1 << sb) * (len(proj) ** P) == 1 << (len(Spos) * P) \
                        and len(proj) < (1 << len(Spos)):
                    eq_cases.append((k, sorted(pat), Spos))
print(f"T1c exhaustive k<=4: {total} (pattern,S) checks: Lemma A holds")
print(f"    nontrivial equality cases at k<=3: {len(eq_cases)} "
      f"(sample: {eq_cases[:6]})")
total = 0
for _ in range(200000):
    k = random.randint(5, 12)
    P = 1 << k
    style = random.random()
    if style < 0.4:   # sparse
        sz = random.randint(1, 8)
    elif style < 0.8: # dense
        sz = P - random.randint(1, 8)
    else:
        sz = random.randint(1, P)
    pat = frozenset(random.sample(range(P), sz))
    r = random.randint(1, k)
    Spos = tuple(sorted(random.sample(range(k), r)))
    if not lemmaA_ok(pat, k, Spos):
        print("T1c FAIL rnd", k, sorted(pat), Spos); fail = True
    total += 1
print(f"T1c random k in 5..12: {total} checks: Lemma A holds")

# ---------- T1d ----------
def rand_disjoint_pair():
    """Random disjoint pair with controlled shared window."""
    s = random.randint(1, 6)
    kf = random.randint(s, 8)
    kg = random.randint(s, 8)
    # global coords: shared = 0..s-1, f extra 100.., g extra 200..
    Wf = tuple(range(s)) + tuple(100 + i for i in range(kf - s))
    Wg = tuple(range(s)) + tuple(200 + i for i in range(kg - s))
    Wf, Wg = tuple(sorted(Wf)), tuple(sorted(Wg))
    # disjoint projection targets U, V on the shared cube
    Scube = 1 << s
    sizes = random.choice([(1, 1), (1, Scube - 1),
                           (Scube // 2, Scube // 2),
                           (random.randint(1, Scube - 1), None)])
    u = sizes[0]
    U = set(random.sample(range(Scube), u))
    rest = [m for m in range(Scube) if m not in U]
    v = sizes[1] if sizes[1] else random.randint(1, len(rest))
    V = set(random.sample(rest, min(v, len(rest))))
    def lift(W, target):
        pos = [W.index(c) for c in range(s)]
        free = [b for b in range(len(W)) if b not in pos]
        pts = []
        for m in range(1 << len(W)):
            mS = sum(((m >> p) & 1) << j for j, p in enumerate(pos))
            if mS in target:
                pts.append(m)
        # random nonempty subset covering an arbitrary sub-collection
        sz = random.randint(1, len(pts))
        return frozenset(random.sample(pts, sz))
    f = JFun(Wf, lift(Wf, U))
    g = JFun(Wg, lift(Wg, V))
    return f, g

worst = None
for t in range(20000):
    f, g = rand_disjoint_pair()
    assert disjoint(f, g)
    ok, lhs = payment_ok(f, g)
    if not ok:
        print("T1d FAIL payment", f, g, lhs); fail = True
    if worst is None or lhs < worst[0]:
        worst = (lhs, f, g)
print(f"T1d 20000 random disjoint pairs: payment >= 1 holds; "
      f"minimum payment = {worst[0]} (float {float(worst[0]):.6f})")
print(f"    minimizer: shared={shared(worst[1],worst[2])} "
      f"f={worst[1]} g={worst[2]}")

print("ALL T1 PASS" if not fail else "T1 FAILURES PRESENT")
sys.exit(1 if fail else 0)
