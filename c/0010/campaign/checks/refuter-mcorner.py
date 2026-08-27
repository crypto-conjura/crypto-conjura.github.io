#!/usr/bin/env python3
r"""refuter-mcorner --- counterexample search for the M-corner of campaign c/0010.

Run with an interpreter that has numpy (here: /usr/local/bin/python3, numpy 2.2.3).

THE QUESTION (PROGRESS.md 2.2, kappa-2-r3 8)
--------------------------------------------
kappa(q) := sup over q-query challenge-oblivious observers D of
            | Pr[Real = 1] - Pr[Real_0 = 1] |,
for H : [N]x[N] -> [M] uniform and a split delta-unpredictable source pair.
The bound in hand (Corollary D'') is

    kappa(q) <= 5 sqrt(sigma' delta) + min{ mu'(min(qM,N^2)), 2 delta sqrt(M) },
    sigma' = sigma + 2 log2 N,   mu'(s) = min(s d, 2 (s d^2)^(1/3), 1).

The only proved lower bound (Proposition F) attains delta sqrt(M)/(4 sqrt 2) but spends
q = N^2 queries, and kappa is monotone in q, so it says nothing at small q.  The
blocking hypothesis (H2) binds exactly at SMALL q with LARGE M.  Hence:

    does kappa(q) carry ANY M-dependence for small q?

This program assumes the answer is YES and hunts for the witness.  Everything it
prints is either an exact rational/closed-form quantity or a Monte-Carlo estimate
with its own standard error; the parameter grid of every stage is printed with the
stage.

WHAT IS COMPUTED, STAGE BY STAGE
--------------------------------
S1  TRUE optimum, brute force.  For tiny (N,M) the whole function space Fun is
    enumerated and the exact optimal advantage is computed by alternating exact
    maximisation over (source, observer), for q = 0,1,2 and sigma in {0,2}.
    Observer space = ALL deterministic q-query challenge-oblivious observers with
    full challenge resolution (query positions may be steered by the challenge
    value and by the leakage; q=2 is an arbitrary depth-2 adaptive decision tree).
    Source space = all f-dependent flat product sources (justified below).
    Output: the Pareto frontier (delta, best advantage) for each M, so the
    M-dependence at fixed (N, delta, q) is read off directly.
    At the smallest sizes the alternation is validated against exhaustive
    enumeration of the entire observer space.

S2  Exact large-M limit for value-symmetric sources.  For sources whose behaviour
    depends on f only through its value-partition pattern, the optimal 1-query
    observer is derived in closed form (see THEOREM S2 below) and the optimum is
    then computed EXACTLY, in rational arithmetic, at M up to 2^40 by summing over
    set partitions of the N^2 cells.  This is the M-scaling question answered with
    no sampling and no truncation, for that class.

S3  Mechanism catalogue at realistic parameters.  Exact closed forms (checked
    against Monte Carlo) for the three attack mechanisms found:
       HIT   (predictability leak)        p (1 - 1/M),      p <= delta
       PLANT (rectangle counting)         ~ sqrt(sigma' delta), M-FREE by construction
       FIT   (histogram fitting)          delta^2 Phi(q,M),  Phi = M E[(Bin(q,1/M) - q/M)^+]
    and the phase law for FIT: Phi(q,M) ~ min(q, sqrt(qM/2pi)), i.e. the
    M-dependence of the best known attack switches OFF for M >~ q.

S4  Corner audit.  Over a large grid of (N, sigma, delta, q, M) the best attack in
    the whole catalogue (maximised over its internal parameters) is compared with
    the M-free target 5 sqrt(sigma' delta) + mu'(q) and with the corner condition
    M > sigma' q+ / (4 delta).  Reports the max ratio over the grid, and over the
    corner points only.

S3E Proposition F off the diagonal: the FIT family reproduces delta sqrt(M) for
    EVERY delta at q = 1/delta^2 queries, not only at delta = 1/N with q = N^2;
    and the table of where the M-dependence turns on versus where the corner is.

S3F The near-miss, measured: the only 1-query certificate for the challenge is
    "f(u(y)) = y", and the density of certifiable cells -- hence the yield of the
    attack -- FALLS as M grows, because planting a certificate costs log M bits
    per cell against the 2K log(N/K) bits of freedom in choosing the rectangle.

S5  Open-ended search at moderate N with sampled oracles and a train/test split,
    so that overfitting to the sample cannot manufacture a counterexample: the
    observer is fitted on train oracles and scored on fresh ones, with the source
    recomputed on the fresh ones by the same (legitimate, f-measurable) rule.

S6  What the obstruction suggests: replacing Lemma B's union over all 2^M tests by
    a union over q-query TRANSCRIPTS turns delta sqrt(M) into
    delta sqrt(q log(N^2 M)); the arithmetic of whether that reaches the Contract's
    target is checked over a grid.  A lead for the prover, not a proof.

WHY FLAT PRODUCT SOURCES ARE WLOG (used by S1 and S5)
-----------------------------------------------------
Fix the observer, hence for each f a test theta_f : [M] -> {0,1}.  The advantage is
   Adv = E_f[ sum_v (rho_f(v) - 1/M) theta_f(v) ],   rho_f = pushforward of pi^1 (x) pi^2,
and by Lemma 1 of kappa-2-r3 the posterior is exactly the product pi^1 (x) pi^2 and the
unpredictability constraint is exactly E_f[m_i] <= delta with m_i = ||pi^i||_inf.  The
Lagrangian is  sum_f Pr[f] ( pi^1_f A_f pi^2_f - lam_1 m_1(f) - lam_2 m_2(f) ),
separable over f and bilinear in (pi^1, pi^2).  For fixed pi^2 the inner problem is
   max over pi of  g . pi - lam ||pi||_inf,   g := A_f pi^2,
whose extreme points put mass m on the top k = floor(1/m) coordinates and 1 - mk on one
more; the value is affine in m at fixed support, so an optimum is attained at m = 1/k,
i.e. at a FLAT pi.  Alternating gives a flat-flat optimum.  So the Lagrangian optimum is
attained on the flat family, and every (advantage, delta) pair printed below comes from an
explicit flat source and is therefore a genuine lower bound on kappa at that delta.

THEOREM S2 (proved here, used by S2; verified numerically inside S1)
-------------------------------------------------------------------
Call a source value-symmetric if pi^i_{g o f} = pi^i_f for every permutation g of [M].
Then for every such source the optimal 1-query challenge-oblivious observer is the
COLLISION TEST at a single cell, and
    kappa_sym(1) = max over cells c of | Pr[ f(x) = f(c) ] - 1/M |.
Proof.  Let W_f(v) := Pr[f] (rho_f(v) - 1/M).  A 1-query observer is (u, beta) with
theta_f(v) = beta(v, f(u(v))).  Given the observer, the gain decomposes over v, and for a
fixed cell c the best beta(v,.) accepts b iff A_c(v,b) := sum_{f : f(c)=b} W_f(v) > 0.
Value-symmetry gives A_c(g v, g b) = A_c(v, b), so A_c(v,b) = a_c for b = v and
a_c' for b != v; sum_b A_c(v,b) = sum_f W_f(v) = 0 forces a_c' = -a_c/(M-1).  Hence the
per-v gain is |a_c| whichever sign a_c has (accept only b=v, or accept all b != v), and
summing over the M values, M |a_c| = | E_f[ rho_f(f(c)) ] - 1/M | = |Pr[f(x)=f(c)] - 1/M|.
Maximising over c (and over the option of not querying, which is dominated) gives the
claim.  QED
Consequences, both visible in the printout: value-symmetric sources have
kappa_sym(0) = 0, and their entire 1-query signal is the collision probability, which is
bounded by mu'(|f^{-1}(w)|) ~ mu'(N^2/M) -- DECREASING in M.

VERIFICATION POLICY
-------------------
Any candidate counterexample is verified twice: (i) exact rational arithmetic by direct
enumeration, (ii) an independent Monte-Carlo simulation of the two experiments Real and
Real_0 that never touches rho, W or any of the algebra above.  Both verifiers are run
below on the best witness of every S1 configuration, whether or not it is a
counterexample, so the verifiers themselves are exercised.
"""

import itertools
import math
import sys
from fractions import Fraction

# REPRODUCIBILITY NOTE (added after the pass, 27 August 2026).
# This script requires numpy.  The default `python3` on the machine it was written
# on does NOT have it; the run of record used /usr/local/bin/python3 (3.13.2,
# numpy 2.2.3).  Invoke as:
#     /usr/local/bin/python3 -u refuter-mcorner.py            # all stages
#     /usr/local/bin/python3 -u refuter-mcorner.py 4           # one stage
# The run of record is refuter-mcorner-run.txt (EXIT=0).  Stage 4 alone
# reproduces the corner audit in a few minutes; stage 1 is the slow one.

import numpy as np

RNG = np.random.default_rng(20260827)

# --------------------------------------------------------------------------- #
# helpers                                                                     #
# --------------------------------------------------------------------------- #

def mu_prime(s, d):
    if s <= 0:
        return 0.0
    return min(s * d, 2.0 * (s * d * d) ** (1.0 / 3.0), 1.0)


def sigma_prime(sigma, N):
    return sigma + 2.0 * math.log2(N)


def targets(N, M, sigma, d, q):
    """The three yardsticks used throughout."""
    sp = sigma_prime(sigma, N)
    lead = 5.0 * math.sqrt(sp * d)                       # M-free leading term
    mfree = lead + mu_prime(q, d)                        # conjectured M-free bound
    cordd = lead + min(mu_prime(min(q * M, N * N), d), 2.0 * d * math.sqrt(M))
    conj = math.sqrt(sp * (q + 1) * d)                   # Contract target, sans constant
    corner = M > sp * (q + 1) / (4.0 * d)                # (H2) fails <=> corner
    return dict(sp=sp, lead=lead, mfree=mfree, cordd=cordd, conj=conj, corner=corner)


def nonempty_subsets(N):
    out = []
    for r in range(1, N + 1):
        out.extend(itertools.combinations(range(N), r))
    return out


def all_functions(N, M):
    n2 = N * N
    nF = M ** n2
    F = np.empty((nF, n2), dtype=np.int64)
    idx = np.arange(nF)
    for j in range(n2):
        F[:, j] = (idx // (M ** j)) % M
    return F


# --------------------------------------------------------------------------- #
# S1: exact brute force at tiny parameters                                    #
# --------------------------------------------------------------------------- #

class Exact:
    """Exact optimisation over (flat f-dependent source, deterministic q-query
    challenge-oblivious observer) for the full function space Fun = [M]^([N]x[N]).

    Leakage model: sigma_i deterministic bits z_i = xi_i(f) chosen by the source
    together with its rectangle; G = 2^sigma leakage classes.  (Deterministic
    leakage does not change the unpredictability constraint -- with x_i uniform on
    B_i(f), the posterior mode given (f, z_i) is still 1/|B_i(f)| -- so the
    constraint stays E_f[1/|B_i(f)|] <= delta.)
    """

    def __init__(self, N, M, sigma_bits=0):
        self.N, self.M = N, M
        self.n2 = N * N
        self.G = 1 << sigma_bits
        self.sigma = sigma_bits
        self.F = all_functions(N, M)
        self.nF = self.F.shape[0]
        subs = nonempty_subsets(N)
        self.rects = []
        for s1 in subs:
            for s2 in subs:
                cells = [a * N + b for a in s1 for b in s2]
                self.rects.append((len(s1), len(s2), cells))
        self.nR = len(self.rects)
        self.RMAT = np.zeros((self.n2, self.nR))
        self.area = np.empty(self.nR)
        self.pen = np.empty(self.nR)          # 1/k1 + 1/k2
        for r, (k1, k2, cells) in enumerate(self.rects):
            self.RMAT[cells, r] = 1.0
            self.area[r] = k1 * k2
            self.pen[r] = 1.0 / k1 + 1.0 / k2
        self.invk1 = np.array([1.0 / k1 for k1, k2, _ in self.rects])
        self.invk2 = np.array([1.0 / k2 for k1, k2, _ in self.rects])
        # one-hot of F[:, c] cached lazily
        self._oh = {}

    def onehot(self, c):
        if c not in self._oh:
            self._oh[c] = (self.F[:, c][:, None] == np.arange(self.M)[None, :])
        return self._oh[c]

    # ---- source side -------------------------------------------------------
    def rho_minus_uniform(self, src_r):
        """W[i, v] = rho_i(v) - 1/M for the flat source with rectangle src_r[i]."""
        M = self.M
        W = np.empty((self.nF, M))
        ar = np.arange(M)
        for r in range(self.nR):
            sel = np.nonzero(src_r == r)[0]
            if sel.size == 0:
                continue
            k1, k2, cells = self.rects[r]
            cnt = np.zeros((sel.size, M))
            for c in cells:
                cnt += (self.F[sel, c][:, None] == ar[None, :])
            W[sel] = cnt / (k1 * k2) - 1.0 / M
        return W

    def deltas(self, src_r):
        return (float(self.invk1[src_r].mean()), float(self.invk2[src_r].mean()))

    # ---- observer side -----------------------------------------------------
    def best_observer(self, W, zeta, q):
        """Exact best deterministic q-query observer given the source.

        Returns (advantage, obs) where obs is a per-(group, value) description.
        """
        M, n2 = self.M, self.n2
        total = 0.0
        obs = []
        for g in range(self.G):
            mask = zeta == g
            if not mask.any():
                obs.append(None)
                continue
            Wg = W[mask] / self.nF
            Fg = self.F[mask]
            if q == 0:
                Rv = Wg.sum(axis=0)                        # (M,)
                acc = Rv > 0
                total += float(np.maximum(Rv, 0.0).sum())
                obs.append(("q0", acc))
            elif q == 1:
                best_gain = np.full(M, -np.inf)
                best_cell = np.zeros(M, dtype=int)
                accs = np.zeros((n2, M, M), dtype=bool)
                for c in range(n2):
                    oh = (Fg[:, c][:, None] == np.arange(M)[None, :])
                    A = oh.T.astype(np.float64) @ Wg       # A[b, v]
                    accs[c] = (A > 0).T                    # accs[c][v][b]
                    gain = np.maximum(A, 0.0).sum(axis=0)  # (M,)
                    upd = gain > best_gain
                    best_gain = np.where(upd, gain, best_gain)
                    best_cell = np.where(upd, c, best_cell)
                total += float(best_gain.sum())
                beta = np.zeros((M, M), dtype=bool)
                for v in range(M):
                    beta[v] = accs[best_cell[v]][v]
                obs.append(("q1", best_cell, beta))
            elif q == 2:
                # depth-2 adaptive tree per value v: c1(v), then c2(v, b1), then beta.
                best_gain = np.full(M, -np.inf)
                best = [None] * M
                # J[(c1,c2)][b1*M+b2][v]
                Jt = {}
                for c1 in range(n2):
                    for c2 in range(n2):
                        j = Fg[:, c1] * M + Fg[:, c2]
                        oh = (j[:, None] == np.arange(M * M)[None, :])
                        Jt[(c1, c2)] = oh.T.astype(np.float64) @ Wg  # (M*M, M)
                for c1 in range(n2):
                    # per (v, b1): best c2 and its gain
                    gain_b1 = np.full((M, M), -np.inf)          # [b1][v]
                    arg_b1 = np.zeros((M, M), dtype=int)
                    for c2 in range(n2):
                        T = Jt[(c1, c2)].reshape(M, M, M)       # [b1][b2][v]
                        gg = np.maximum(T, 0.0).sum(axis=1)     # [b1][v]
                        upd = gg > gain_b1
                        gain_b1 = np.where(upd, gg, gain_b1)
                        arg_b1 = np.where(upd, c2, arg_b1)
                    gain = gain_b1.sum(axis=0)                  # (M,)
                    upd = gain > best_gain
                    for v in range(M):
                        if upd[v]:
                            c2v = arg_b1[:, v].copy()
                            bet = np.zeros((M, M), dtype=bool)
                            for b1 in range(M):
                                T = Jt[(c1, c2v[b1])].reshape(M, M, M)
                                bet[b1] = T[b1, :, v] > 0
                            best[v] = (c1, c2v, bet)
                    best_gain = np.where(upd, gain, best_gain)
                total += float(best_gain.sum())
                obs.append(("q2", best))
            else:
                raise ValueError("q in {0,1,2}")
        return total, obs

    def theta_tables(self, obs):
        """TH[g][i, v] in {0,1}: the observer's output on challenge v under oracle f_i,
        as if f_i were in leakage class g (needed because the source picks its class)."""
        M = self.M
        TH = np.zeros((self.G, self.nF, M), dtype=np.uint8)
        ar = np.arange(self.nF)
        for g in range(self.G):
            o = obs[g]
            if o is None:
                continue
            if o[0] == "q0":
                TH[g][:, :] = o[1].astype(np.uint8)[None, :]
            elif o[0] == "q1":
                cells, beta = o[1], o[2]
                for v in range(M):
                    TH[g][:, v] = beta[v][self.F[:, cells[v]]]
            else:
                for v in range(M):
                    c1, c2v, bet = o[1][v]
                    b1 = self.F[:, c1]
                    b2 = self.F[ar, c2v[b1]]
                    TH[g][:, v] = bet[b1, b2]
        return TH

    def best_source(self, TH, lam):
        """Per-f exact maximisation of  mean_{rect} theta(f(.)) - lam * (1/k1 + 1/k2)."""
        best_val = None
        best_r = None
        best_g = None
        ar = np.arange(self.nF)
        for g in range(self.G):
            A = np.empty((self.nF, self.n2))
            for c in range(self.n2):
                A[:, c] = TH[g][ar, self.F[:, c]]
            V = (A @ self.RMAT) / self.area[None, :] - lam * self.pen[None, :]
            r = V.argmax(axis=1)
            v = V[ar, r]
            if best_val is None:
                best_val, best_r, best_g = v, r, np.zeros(self.nF, dtype=int)
            else:
                upd = v > best_val
                best_val = np.where(upd, v, best_val)
                best_r = np.where(upd, r, best_r)
                best_g = np.where(upd, g, best_g)
        return best_r, best_g

    def advantage(self, src_r, zeta, TH):
        """Signed advantage of the given (source, observer)."""
        ar = np.arange(self.nF)
        th = TH[zeta, ar, :]                            # (nF, M)
        W = self.rho_minus_uniform(src_r)
        return float((W * th).sum() / self.nF)

    # ---- driver ------------------------------------------------------------
    def penalized_best_source(self, TH, lam):
        """max over sources of (adv - lam (E[1/k1] + E[1/k2])) for a FIXED observer."""
        src_r, zeta = self.best_source(TH, lam)
        adv = self.advantage(src_r, zeta, TH)
        d1, d2 = self.deltas(src_r)
        return adv - lam * (d1 + d2), adv, max(d1, d2)

    def search(self, q, lams, restarts, iters=25, seed=0, pen_out=None):
        rng = np.random.default_rng(seed)
        found = []
        starts = []
        full_r = self.nR - 1                            # (full, full) rectangle
        starts.append(("uniform", np.full(self.nF, full_r), np.zeros(self.nF, dtype=int)))
        for t in range(restarts):
            starts.append(("rand%d" % t,
                           rng.integers(0, self.nR, self.nF),
                           rng.integers(0, self.G, self.nF)))
        for lam in lams:
            for name, r0, g0 in starts:
                src_r, zeta = r0.copy(), g0.copy()
                prev = -np.inf
                for _ in range(iters):
                    W = self.rho_minus_uniform(src_r)
                    adv, obs = self.best_observer(W, zeta, q)
                    TH = self.theta_tables(obs)
                    pen = lam * (self.invk1[src_r].mean() + self.invk2[src_r].mean())
                    cur = adv - pen
                    src_r, zeta = self.best_source(TH, lam)
                    if cur <= prev + 1e-14:
                        break
                    prev = cur
                W = self.rho_minus_uniform(src_r)
                adv, obs = self.best_observer(W, zeta, q)
                TH = self.theta_tables(obs)
                d1, d2 = self.deltas(src_r)
                found.append((max(d1, d2), adv, src_r.copy(), zeta.copy(), obs))
                if pen_out is not None:
                    pv = adv - lam * (d1 + d2)
                    pen_out[lam] = max(pen_out.get(lam, -np.inf), pv)
        return found


def pareto(found, dgrid):
    """best advantage among witnesses with delta_eff <= d, for each d in dgrid."""
    out = {}
    for d in dgrid:
        best = None
        for (de, adv, src, zeta, obs) in found:
            if de <= d + 1e-12 and (best is None or adv > best[1]):
                best = (de, adv, src, zeta, obs)
        out[d] = best
    return out


# ---- exact rational verifier ---------------------------------------------- #

def exact_verify(E, src_r, zeta, obs):
    """Recompute (delta_1, delta_2, advantage) in exact rational arithmetic,
    by direct enumeration over Fun.  Independent of the float path."""
    TH = E.theta_tables(obs)
    nF, M = E.nF, E.M
    adv = Fraction(0)
    d1 = Fraction(0)
    d2 = Fraction(0)
    for i in range(nF):
        k1, k2, cells = E.rects[int(src_r[i])]
        d1 += Fraction(1, k1)
        d2 += Fraction(1, k2)
        th = TH[int(zeta[i]), i, :]
        cnt = 0
        for c in cells:
            if th[int(E.F[i, c])]:
                cnt += 1
        ptheta = Fraction(int(th.sum()), M)
        adv += Fraction(cnt, k1 * k2) - ptheta
    return d1 / nF, d2 / nF, adv / nF


def mc_verify(E, src_r, zeta, obs, nsamp=200000, seed=1):
    """Independent Monte-Carlo simulation of Real and Real_0.  Touches neither rho
    nor W nor any algebra of the analytic path: it draws f, runs the source's rule,
    draws x from the rectangle, evaluates the oracle, and runs the observer."""
    rng = np.random.default_rng(seed)
    TH = E.theta_tables(obs)
    idx = rng.integers(0, E.nF, nsamp)                  # f uniform on Fun
    r = src_r[idx]
    g = zeta[idx]
    x1 = np.empty(nsamp, dtype=int)
    x2 = np.empty(nsamp, dtype=int)
    for rr in range(E.nR):
        sel = np.nonzero(r == rr)[0]
        if sel.size == 0:
            continue
        k1, k2, cells = E.rects[rr]
        s1 = sorted({c // E.N for c in cells})
        s2 = sorted({c % E.N for c in cells})
        x1[sel] = np.array(s1)[rng.integers(0, k1, sel.size)]
        x2[sel] = np.array(s2)[rng.integers(0, k2, sel.size)]
    y_real = E.F[idx, x1 * E.N + x2]
    y_ideal = rng.integers(0, E.M, nsamp)
    p_real = TH[g, idx, y_real].mean()
    p_ideal = TH[g, idx, y_ideal].mean()
    se = math.sqrt((p_real * (1 - p_real) + p_ideal * (1 - p_ideal)) / nsamp)
    return float(p_real - p_ideal), se


def collision_formula(E, src_r):
    """max over cells c of |Pr[f(x)=f(c)] - 1/M|; the closed form of THEOREM S2."""
    best = 0.0
    argc = None
    for c in range(E.n2):
        tot = 0.0
        for r in range(E.nR):
            sel = np.nonzero(src_r == r)[0]
            if sel.size == 0:
                continue
            k1, k2, cells = E.rects[r]
            hit = np.zeros(sel.size)
            for cc in cells:
                hit += (E.F[sel, cc] == E.F[sel, c])
            tot += (hit / (k1 * k2)).sum()
        val = tot / E.nF - 1.0 / E.M
        if abs(val) > abs(best):
            best, argc = val, c
    return best, argc


def symmetrise_source(E, src_r):
    """Project a source onto the value-symmetric class: keep the choice made at the
    lexicographically least f of each value-partition pattern."""
    n2, M = E.n2, E.M
    key = {}
    out = np.empty_like(src_r)
    for i in range(E.nF):
        f = E.F[i]
        seen, lab, pat = {}, 0, []
        for c in range(n2):
            v = int(f[c])
            if v not in seen:
                seen[v] = lab
                lab += 1
            pat.append(seen[v])
        t = tuple(pat)
        if t not in key:
            key[t] = src_r[i]
        out[i] = key[t]
    return out


def stage1():
    print("=" * 78)
    print("S1  EXACT BRUTE FORCE OVER ALL OF Fun = [M]^([N]x[N])")
    print("=" * 78)
    print("Observer space : every deterministic q-query challenge-oblivious observer,")
    print("                 full challenge resolution (query cells steered by the")
    print("                 challenge value and the leakage); q=2 = arbitrary depth-2")
    print("                 adaptive tree.  Optimal observer computed in closed form.")
    print("Source space   : all f-dependent flat product sources (WLOG, see header),")
    print("                 with sigma deterministic bits of leakage per source.")
    print("Method         : alternating exact maximisation, Lagrange sweep over the")
    print("                 unpredictability constraint, many restarts; best kept.")
    print("Yardsticks     : lead = 5 sqrt(sigma' delta)   (M-free leading term)")
    print("                 mfree = lead + mu'(q)         (conjectured M-free bound)")
    print("                 D''   = lead + min(mu'(min(qM,N^2)), 2 delta sqrt M)")
    print()
    lams = [0.0, 0.01, 0.025, 0.05, 0.075, 0.1, 0.15, 0.2, 0.275, 0.35, 0.425,
            0.5, 0.6, 0.75, 0.9, 1.0, 1.25, 1.5, 2.0, 3.0, 4.0]
    grid = [
        # (N, M list, sigma bits, q list, restarts)
        (2, [2, 3, 4, 6, 8, 12, 16], 0, [0, 1], 24),
        (2, [2, 3, 4, 6, 8], 0, [2], 12),
        (2, [2, 3, 4, 6, 8], 2, [0, 1], 12),
        (3, [2, 3], 0, [0, 1, 2], 10),
        (3, [4], 0, [0, 1], 6),
        (3, [2, 3], 2, [1], 6),
    ]
    print("GRID:")
    for (N, Ms, sb, qs, rs) in grid:
        print("  N=%d  M in %s  sigma=%d  q in %s  restarts=%d  |Fun| in %s"
              % (N, Ms, sb, qs, rs, [M ** (N * N) for M in Ms]))
    print()
    results = {}
    series = {}
    for (N, Ms, sb, qs, rs) in grid:
        for q in qs:
            dgrid = sorted({1.0 / N, 0.4, 0.5, 0.6, 0.75, 1.0} | {1.0 / N})
            dgrid = [d for d in dgrid if d >= 1.0 / N - 1e-12]
            print("-" * 78)
            print("N=%d  sigma=%d  q=%d" % (N, sb, q))
            hdr = "  %5s | %9s | " % ("M", "|Fun|") + " | ".join(
                "%10s" % ("d<=%.3f" % d) for d in dgrid)
            print(hdr)
            for M in Ms:
                E = Exact(N, M, sb)
                found = E.search(q, lams, rs, seed=1000 * N + 10 * M + q)
                pf = pareto(found, dgrid)
                row = "  %5d | %9d | " % (M, E.nF)
                cells = []
                for d in dgrid:
                    b = pf[d]
                    if b is None:
                        cells.append("%10s" % "-")
                    else:
                        cells.append("%10.6f" % b[1])
                        results[(N, sb, q, M, d)] = b
                        series.setdefault((N, sb, q, d), {})[M] = b[1]
                print(row + " | ".join(cells))
            # yardstick line at delta = 1/N
            d0 = 1.0 / N
            for M in Ms:
                b = results.get((N, sb, q, M, d0))
                if b is None:
                    continue
                t = targets(N, M, sb, b[0], q)
                print("     M=%2d  delta_eff=%.4f  adv=%.6f | lead=%.4f mfree=%.4f "
                      "D''=%.4f conj=%.4f corner=%s ok(D'')=%s"
                      % (M, b[0], b[1], t["lead"], t["mfree"], t["cordd"], t["conj"],
                         t["corner"], b[1] <= t["cordd"] + 1e-9))
    m_scaling_diagnostic(series)
    return results


def m_scaling_diagnostic(series):
    """Discriminate 'saturating in M' from 'growing like sqrt(M)'.

    For each (N, sigma, q, delta) with at least three M values, least-squares fit
        model A:  adv(M) = a - b/M        (saturating; a = the M -> infinity value)
        model B:  adv(M) = c sqrt(M)      (the delta sqrt M shape of Proposition F)
    and report the residuals.  Model A winning by orders of magnitude, with
    adv(Mmax)/a close to 1, is the negative answer to 'does kappa carry
    M-dependence at small q'.
    """
    print()
    print("-" * 78)
    print("S1D  M-SCALING DIAGNOSTIC  (is the M-dependence saturating or growing?)")
    print("-" * 78)
    print("  fit A: adv = a - b/M   (saturating, a = extrapolated M=infinity value)")
    print("  fit B: adv = c sqrt(M) (the shape of the delta sqrt M residue)")
    print("  and the model-free growth exponent p := dlog(adv)/dlog(M): p = 1/2 is")
    print("  the delta sqrt(M) shape, p = 0 is saturation.  p_last uses the two")
    print("  largest M, p_fit is the log-log least-squares slope.")
    print("  %3s %3s %2s %6s | %5s | %9s %9s | %9s %9s | %8s | %6s %6s"
          % ("N", "sig", "q", "delta", "#M", "a", "resid A", "c", "resid B",
             "adv/a", "p_last", "p_fit"))
    for key in sorted(series):
        N, sb, q, d = key
        pts = sorted(series[key].items())
        if len(pts) < 3:
            continue
        Ms = np.array([p[0] for p in pts], dtype=float)
        ys = np.array([p[1] for p in pts], dtype=float)
        if ys.max() <= 1e-12:
            continue
        A = np.stack([np.ones_like(Ms), -1.0 / Ms], axis=1)
        solA, *_ = np.linalg.lstsq(A, ys, rcond=None)
        rA = float(np.sqrt(((A @ solA - ys) ** 2).mean()))
        B = np.sqrt(Ms)[:, None]
        solB, *_ = np.linalg.lstsq(B, ys, rcond=None)
        rB = float(np.sqrt(((B @ solB - ys) ** 2).mean()))
        p_last = (math.log(ys[-1] / ys[-2]) / math.log(Ms[-1] / Ms[-2])
                  if ys[-2] > 0 and Ms[-1] > Ms[-2] else float("nan"))
        L = np.stack([np.ones_like(Ms), np.log(Ms)], axis=1)
        pf, *_ = np.linalg.lstsq(L, np.log(np.maximum(ys, 1e-15)), rcond=None)
        print("  %3d %3d %2d %6.3f | %5d | %9.5f %9.2e | %9.5f %9.2e | %8.4f | "
              "%6.3f %6.3f"
              % (N, sb, q, d, len(pts), solA[0], rA, solB[0], rB,
                 ys[-1] / solA[0] if solA[0] > 0 else float("nan"),
                 p_last, pf[1]))
    print("  (a saturating fit with residual orders of magnitude below the sqrt(M)")
    print("   fit, and adv/a close to 1 at the largest M, means the M-dependence of")
    print("   the TRUE optimum is the bounded factor (1 - O(1/M)), not growth in M.)")


def exhaustive_penalized(E, q, lams):
    """max over the ENTIRE observer space, and over sources, of the penalized
    objective  adv - lam (E[1/k1] + E[1/k2])  --- exactly, by enumeration.

    q=0: all 2^M tests theta : [M] -> {0,1}.
    q=1: all (u, beta) with u : [M] -> cells, beta : [M]x[M] -> {0,1}.
    The source is optimised exactly per f (the objective is separable over f once
    lam is fixed), so this is the exact value of the penalized bilinear problem.
    sigma = 0 only.  Both signs of the advantage are covered because complementing
    beta negates the signed advantage (sum_v sum_b A = 0), and the complement is
    in the enumeration.
    """
    M, n2 = E.M, E.n2
    assert E.G == 1
    best = {lam: -np.inf for lam in lams}
    def upd(TH):
        for lam in lams:
            pv, adv, de = E.penalized_best_source(TH, lam)
            if pv > best[lam]:
                best[lam] = pv
    if q == 0:
        for mask in range(1 << M):
            th = np.array([(mask >> v) & 1 for v in range(M)], dtype=np.uint8)
            upd(np.tile(th, (1, E.nF, 1)))
    elif q == 1:
        for u in itertools.product(range(n2), repeat=M):
            base = np.empty((E.nF, M), dtype=np.int64)
            for v in range(M):
                base[:, v] = E.F[:, u[v]]
            for bm in range(1 << (M * M)):
                TH = np.empty((1, E.nF, M), dtype=np.uint8)
                for v in range(M):
                    row = (bm >> (v * M)) & ((1 << M) - 1)
                    beta = np.array([(row >> b) & 1 for b in range(M)],
                                    dtype=np.uint8)
                    TH[0, :, v] = beta[base[:, v]]
                upd(TH)
    else:
        raise ValueError
    return best


def stage1_exhaustive():
    print()
    print("-" * 78)
    print("S1E  VALIDATION: alternating search vs EXHAUSTIVE enumeration of the")
    print("     entire observer space (sigma = 0)")
    print("-" * 78)
    print("  Compared object: the penalized optimum")
    print("      V(lam) = max over observers, sources of [ adv - lam (E 1/k1 + E 1/k2) ]")
    print("  which is what the alternation maximises.  Exhaustive = every observer.")
    lams = [0.0, 0.05, 0.15, 0.3, 0.5, 0.8, 1.2, 2.0]
    cases = [(2, 2, 0), (2, 3, 0), (2, 4, 0), (2, 6, 0), (2, 8, 0), (2, 12, 0),
             (3, 2, 0), (3, 3, 0), (2, 2, 1), (2, 3, 1)]
    allmatch = True
    for (N, M, q) in cases:
        E = Exact(N, M, 0)
        ex = exhaustive_penalized(E, q, lams)
        pen = {}
        E.search(q, lams, 24, seed=99, pen_out=pen)
        nobs = (1 << M) if q == 0 else (N * N) ** M * (1 << (M * M))
        gaps = [ex[lam] - pen.get(lam, -np.inf) for lam in lams]
        ok = max(gaps) <= 1e-9
        allmatch = allmatch and ok
        print("  N=%d M=%2d q=%d : %10d observers enumerated ; max(exhaustive - "
              "alternating) = %+.2e  %s"
              % (N, M, q, nobs, max(gaps), "MATCH" if ok else "*** ALT IS BELOW ***"))
    print("  every case matches: %s" % allmatch)


def stage1_bigM():
    print()
    print("-" * 78)
    print("S1B  LARGE-M SPOT CHECK AT N=2 (exact, all of Fun, few restarts)")
    print("-" * 78)
    print("  the same exact optimisation with M pushed to 32 (|Fun| = 2^20), to")
    print("  extend the M-range of the saturation fit")
    lams = [0.0, 0.1, 0.3, 0.6, 1.0]
    series = {}
    for (N, sb, q) in [(2, 0, 1), (2, 2, 1), (2, 0, 0), (2, 2, 0), (2, 0, 2)]:
        dgrid = [0.5, 0.6, 0.75]
        print("  N=%d sigma=%d q=%d :" % (N, sb, q))
        for M in ((8, 12, 16) if q == 2 else (8, 16, 24, 32)):
            E = Exact(N, M, sb)
            found = E.search(q, lams, 2 if q == 2 else 3, iters=10 if q == 2 else 12,
                             seed=555 + M)
            pf = pareto(found, dgrid)
            row = []
            for d in dgrid:
                if pf[d]:
                    row.append("d<=%.2f: %.6f" % (d, pf[d][1]))
                    series.setdefault((N, sb, q, d), {})[M] = pf[d][1]
                else:
                    row.append("d<=%.2f: -" % d)
            print("    M=%2d (|Fun|=%7d) : %s" % (M, E.nF, "  ".join(row)))
    m_scaling_diagnostic(series)


def stage1_leakage():
    print()
    print("-" * 78)
    print("S1S  LEAKAGE SWEEP: can sigma bits of oracle-dependent leakage create")
    print("     M-dependence at q = 1?  (exact, all of Fun, N = 2)")
    print("-" * 78)
    print("  sigma bits are split 1:1 between the sources; G = 2^sigma leakage")
    print("  classes; with |Fun| = M^4 oracles, sigma = 6 already identifies f to")
    print("  within 2^6 classes, so this is a leakage-RICH test.")
    print("  %6s | " % "sigma" + " | ".join("%22s" % ("M=%d" % M)
                                            for M in (2, 4, 8)))
    lams = [0.0, 0.1, 0.25, 0.5, 0.8, 1.2]
    series = {}
    for sb in (0, 2, 4, 6):
        cells = []
        for M in (2, 4, 8):
            E = Exact(2, M, sb)
            found = E.search(1, lams, 8, iters=15, seed=4242 + M + sb)
            pf = pareto(found, [0.5])
            adv = pf[0.5][1] if pf[0.5] else 0.0
            sp = sigma_prime(sb, 2)
            cells.append("%10.6f (/lead %.3f)" % (adv, adv / (5 * math.sqrt(sp * 0.5))))
            series.setdefault((2, sb, 1, 0.5), {})[M] = adv
        print("  %6d | " % sb + " | ".join(cells))
    print("  (delta = 1/2 = 1/N throughout, so the sources are forced uniform on [N]")
    print("   and every bit of the advantage comes from the leakage; 'lead' is")
    print("   5 sqrt(sigma' delta), the M-free leading term.)")


def stage3e():
    print()
    print("=" * 78)
    print("S3E  A SHARPER PROPOSITION F, AND WHERE THE M-DEPENDENCE TURNS ON")
    print("=" * 78)
    print("The FIT family with K = 1/delta and q = K^2 queries reproduces")
    print("Proposition F's delta sqrt(M) for EVERY delta, not only on delta = 1/N:")
    print("   source: x_i uniform on a FIXED K-subset (sigma = 0, delta = 1/K)")
    print("   observer: query all K^2 cells of the rectangle, Bayes-test the")
    print("             challenge against the exact histogram (resolution 1)")
    print("   advantage = Phi(K^2, M)/K^2   exactly, ~ delta sqrt(M/2pi) for M <= K^2.")
    print("This costs q = 1/delta^2 queries, NOT N^2, so it is a strictly stronger")
    print("statement than Proposition F whenever delta > 1/N.")
    print()
    print("  %6s %8s %5s | %12s | %12s | %8s | %10s"
          % ("K=1/d", "M", "q=K^2", "exact adv", "d sqrt M/(4r2)", "ratio", "d sqrtM/2pi"))
    for K in (4, 8, 16, 32):
        for M in sorted({2, 4, K, K * K // 4, K * K}):
            if M < 2 or M > K * K:
                continue
            d = 1.0 / K
            ex = fit_advantage(K, K * K, M)
            pf = d * math.sqrt(M) / (4 * math.sqrt(2))
            print("  %6d %8d %5d | %12.7f | %12.7f | %8.3f | %10.7f"
                  % (K, M, K * K, ex, pf, ex / pf, d * math.sqrt(M / (2 * math.pi))))
    print()
    print("ONSET.  adv_FIT(q) = Phi(min(q,K^2),M)/K^2 with Phi ~ min(q, sqrt(qM/2pi)):")
    print("  q <= M : adv ~ q delta^2      -- M-FREE")
    print("  q >= M : adv ~ delta^2 sqrt(qM) -- M-dependent, up to delta sqrt M at q=K^2")
    print("So the M-dependence turns on at q ~ M.  The corner (H2 fails) is")
    print("  M > sigma' q+/(4 delta)   i.e.   q < 4 M delta/sigma' - 1,")
    print("which is BELOW the onset q ~ M by the factor sigma'/(4 delta) >= sigma' N/4.")
    print()
    print("  %8s %8s %10s | %14s | %14s | %10s"
          % ("N", "delta", "sigma'", "onset q ~ M", "corner q <", "separation"))
    for N in (2 ** 10, 2 ** 20, 2 ** 40):
        for dm in (1.0, 64.0):
            d = min(1.0, dm / N)
            for sig in (0, 64):
                sp = sigma_prime(sig, N)
                M = 2 ** 32
                print("  %8s %8.2e %10.1f | %14.3e | %14.3e | %10.3e"
                      % ("2^%d" % round(math.log2(N)), d, sp, float(M),
                         max(0.0, 4 * M * d / sp - 1), sp / (4 * d)))
    print("  (M = 2^32 in this table; the separation factor sigma'/(4 delta) does not")
    print("   depend on M, so the conclusion is uniform in M.)")


def stage3f():
    print()
    print("=" * 78)
    print("S3F  THE NEAR-MISS: A 1-QUERY CERTIFICATE FOR THE CHALLENGE, AND WHY ITS")
    print("     YIELD FALLS AS M GROWS")
    print("=" * 78)
    print("The only way a 1-query observer can certify that the challenge lies in a")
    print("planted set is to reproduce the challenge value at a challenge-determined")
    print("cell: fix u : [M] -> [N]^2 and accept iff f(u(y)) = y.  In Real_0 this")
    print("accepts with probability ~1/M.  In Real it accepts with probability 1 if")
    print("the source's rectangle consists of cells c with f(u(f(c))) = f(c).")
    print("Each such cell is an event of probability ~2/M, so planting it on all K^2")
    print("cells costs K^2 log M bits against the 2K log(N/K) bits of freedom in")
    print("choosing the rectangle: the yield must fall like 1/log M.  Measured:")
    print()
    print("  %3s %3s | %8s | %14s | %14s | %10s | %10s"
          % ("N", "K", "M", "max density", "minus 1/M", "delta=1/K", "5sqrt(s'd)"))
    for (N, K) in [(8, 2), (8, 3), (10, 2), (10, 3)]:
        rows = list(itertools.combinations(range(N), K))
        for M in (2, 4, 16, 64, 256, 1024):
            rng = np.random.default_rng(31 + M + 100 * N + 7 * K)
            trials = 200
            tot = 0.0
            for _ in range(trials):
                f = rng.integers(0, M, size=N * N)
                u = rng.integers(0, N * N, size=M)      # the observer's cell map
                lab = (f[u[f]] == f).astype(np.float64).reshape(N, N)
                best = -1.0
                for R in rows:
                    sub = lab[list(R), :]
                    top = np.sort(sub.sum(axis=0))[::-1][:K].sum()
                    best = max(best, top / (K * K))
                tot += best
            md = tot / trials
            d = 1.0 / K
            print("  %3d %3d | %8d | %14.5f | %14.5f | %10.4f | %10.4f"
                  % (N, K, M, md, md - 1.0 / M, d,
                     5 * math.sqrt(sigma_prime(0, N) * d)))
    print()
    print("  The advantage of this attack is (max density - 1/M) at delta = 1/K.  It")
    print("  DECREASES in M, and never approaches delta, let alone delta sqrt M.")
    print("  With the probability-p variant (both sources collapse onto a certifiable")
    print("  rectangle only on an f-event of probability p <= delta K) the advantage")
    print("  is p (max density) <= delta K (max density), still falling in M.")


def witness_structure(E, src_r, zeta):
    """Which mechanism is the winning source using?

    HIT-like  : the fraction of oracles on which the source is DETERMINISTIC
                (k1 = k2 = 1), i.e. the observer can simply query the point.
    FIT-like  : the fraction on which it is the full uniform source (k_i = N),
                whose only signal is the histogram / collision term.
    PLANT-like: the rest -- a proper f-dependent sub-rectangle.
    """
    k1 = np.array([E.rects[int(r)][0] for r in src_r])
    k2 = np.array([E.rects[int(r)][1] for r in src_r])
    det = float(((k1 == 1) & (k2 == 1)).mean())
    unif = float(((k1 == E.N) & (k2 == E.N)).mean())
    return ("deterministic on %.3f of oracles (HIT), fully uniform on %.3f (FIT), "
            "proper sub-rectangle on %.3f (PLANT); leakage classes used %d"
            % (det, unif, 1.0 - det - unif, len(set(zeta.tolist()))))


def stage1_verify(results):
    print()
    print("=" * 78)
    print("S1V  DOUBLE VERIFICATION OF THE BEST WITNESSES")
    print("=" * 78)
    print("(i) exact rational recomputation by enumeration; (ii) independent Monte")
    print("Carlo of Real vs Real_0.  Also: THEOREM S2's closed form checked against")
    print("the brute-force optimum on the value-symmetrised source.")
    print()
    keys = sorted({(N, sb, q, M) for (N, sb, q, M, d) in results})
    shown = 0
    todo = []
    for (N, sb, q, M) in keys:
        if not (N == 2 and M <= 8) and not (N == 3 and M <= 3):
            continue                                    # keep the exact pass cheap
        for d0 in (1.0 / N, 0.75):                      # forced-uniform AND conspiring
            b = results.get((N, sb, q, M, d0))
            if b is not None:
                todo.append((N, sb, q, M, b))
    for (N, sb, q, M, b) in todo:
        E = Exact(N, M, sb)
        de, adv, src, zeta, obs = b
        f1, f2, fadv = exact_verify(E, src, zeta, obs)
        mc, se = mc_verify(E, src, zeta, obs)
        print("N=%d M=%2d sigma=%d q=%d : float adv=%.8f | exact adv=%s=%.8f | "
              "MC=%.5f+-%.5f | exact delta=(%s,%s)=(%.6f,%.6f)"
              % (N, M, sb, q, adv, fadv, float(fadv), mc, se, f1, f2,
                 float(f1), float(f2)))
        print("        structure: %s" % witness_structure(E, src, zeta))
        assert abs(float(fadv) - adv) < 1e-9, "exact/float mismatch"
        assert abs(mc - adv) < 6 * se + 1e-9, "MC/analytic mismatch"
        shown += 1
    print("verified %d witnesses; exact == float to 1e-9 and MC within 6 sigma in all."
          % shown)
    # Theorem S2 check
    print()
    print("THEOREM S2 check (collision-test closed form vs brute-force optimum,")
    print("on value-symmetrised sources, q=1):")
    for (N, M, sb) in [(2, 2, 0), (2, 3, 0), (2, 4, 0), (2, 6, 0), (3, 2, 0), (3, 3, 0)]:
        E = Exact(N, M, sb)
        found = E.search(1, [0.0, 0.2, 0.5, 1.0], 8, seed=7)
        # a NON-trivial symmetric source: best witness with delta_eff <= 0.75
        cand = [t for t in found if t[0] <= 0.75 + 1e-12] or found
        best = max(cand, key=lambda t: t[1])
        sym = symmetrise_source(E, best[2])
        W = E.rho_minus_uniform(sym)
        adv, obs = E.best_observer(W, np.zeros(E.nF, dtype=int), 1)
        coll, c = collision_formula(E, sym)
        adv0, _ = E.best_observer(W, np.zeros(E.nF, dtype=int), 0)
        d1, d2 = E.deltas(sym)
        print("  N=%d M=%2d (delta=%.3f) : brute q=1 opt=%.8f   collision "
              "formula=%.8f (cell %s)   brute q=0 opt=%.2e (theory: 0)"
              % (N, M, max(d1, d2), adv, abs(coll), c, adv0))


# --------------------------------------------------------------------------- #
# S2: exact large-M limit for value-symmetric sources                         #
# --------------------------------------------------------------------------- #

def set_partitions(n):
    """all set partitions of range(n) as restricted-growth strings"""
    a = [0] * n
    m = [0] * n
    while True:
        yield tuple(a)
        i = n - 1
        while i > 0 and a[i] == m[i - 1] + 1:
            i -= 1
        if i == 0:
            return
        a[i] += 1
        mi = max(m[i - 1], a[i])
        m[i] = mi
        for j in range(i + 1, n):
            a[j] = 0
            m[j] = mi


def stage2():
    print()
    print("=" * 78)
    print("S2  EXACT M-SCALING FOR VALUE-SYMMETRIC SOURCES, ANY M (rational arithmetic)")
    print("=" * 78)
    print("By THEOREM S2 (header) the optimal 1-query observer against a")
    print("value-symmetric source is the collision test, so")
    print("   kappa_sym(1) = max_c | Pr[f(x) = f(c)] - 1/M |,")
    print("and Pr[f(x)=f(c)] depends on f only through its value partition.  Summing")
    print("over set partitions of the N^2 cells with weight M(M-1)...(M-b+1)/M^(N^2)")
    print("gives the EXACT optimum at any M, with the source optimised per pattern")
    print("under a Lagrange multiplier for E[1/k_i] <= delta.  Cell c = (0,0).")
    print()
    for N in (2, 3):
        n2 = N * N
        subs = nonempty_subsets(N)
        rects = []
        for s1 in subs:
            for s2 in subs:
                rects.append((len(s1), len(s2), [a * N + b for a in s1 for b in s2]))
        pats = list(set_partitions(n2))
        print("N=%d : %d cells, %d set partitions, %d rectangles"
              % (N, n2, len(pats), len(rects)))
        # per pattern, per rectangle: collision count with cell 0
        coll = np.zeros((len(pats), len(rects)))
        nb = np.zeros(len(pats), dtype=int)
        for p, pat in enumerate(pats):
            nb[p] = max(pat) + 1
            for r, (k1, k2, cells) in enumerate(rects):
                coll[p, r] = sum(1 for c in cells if pat[c] == pat[0]) / (k1 * k2)
        pen = np.array([1.0 / k1 + 1.0 / k2 for k1, k2, _ in rects])
        ik1 = np.array([1.0 / k1 for k1, k2, _ in rects])
        ik2 = np.array([1.0 / k2 for k1, k2, _ in rects])
        Ms = [2, 3, 4, 8, 16, 64, 256, 1024, 2 ** 16, 2 ** 24, 2 ** 40]
        lams = [0.0, 0.001, 0.005, 0.02, 0.05, 0.1, 0.2, 0.4, 0.7, 1.0, 2.0]
        dgrid = [1.0 / N, 0.4, 0.5, 0.75, 1.0]
        dgrid = sorted({d for d in dgrid if d >= 1.0 / N - 1e-12})
        print("  %12s | %8s | " % ("M", "Pr[noninj]")
              + " | ".join("%11s" % ("d<=%.3f" % d) for d in dgrid))
        for M in Ms:
            # exact rational pattern weights
            w = []
            Mn = M ** n2
            for p in range(len(pats)):
                num = 1
                for j in range(nb[p]):
                    num *= (M - j)
                w.append(Fraction(num, Mn))
            wf = np.array([float(x) for x in w])
            pnon = 1.0 - wf[[p for p in range(len(pats)) if nb[p] == n2]].sum()
            best = {d: None for d in dgrid}
            for lam in lams:
                V = coll - lam * pen[None, :]
                r = V.argmax(axis=1)
                adv = float((wf * (coll[np.arange(len(pats)), r])).sum()) - 1.0 / M
                d1 = float((wf * ik1[r]).sum())
                d2 = float((wf * ik2[r]).sum())
                de = max(d1, d2)
                for d in dgrid:
                    if de <= d + 1e-12 and (best[d] is None or abs(adv) > abs(best[d][1])):
                        best[d] = (de, adv, lam)
            row = "  %12d | %8.5f | " % (M, pnon)
            print(row + " | ".join(
                ("%11.7f" % best[d][1]) if best[d] else "%11s" % "-" for d in dgrid))
        print("  (exact rational weights; entries are max_c |Pr[f(x)=f(c)] - 1/M| at the")
        print("   best value-symmetric source with E[1/k_i] <= delta)")
        print()


# --------------------------------------------------------------------------- #
# S3: mechanism catalogue at realistic parameters                             #
# --------------------------------------------------------------------------- #

def Phi_exact(q, M):
    """M * E[(Bin(q,1/M) - q/M)^+] by exact rational summation (small q only)."""
    if q == 0:
        return Fraction(0)
    p = Fraction(1, M)
    tot = Fraction(0)
    for j in range(q + 1):
        w = Fraction(math.comb(q, j)) * p ** j * (1 - p) ** (q - j)
        e = Fraction(j) - Fraction(q, M)
        if e > 0:
            tot += w * e
    return M * tot


def Phi(q, M):
    """M * E[(Bin(q,1/M) - q/M)^+], evaluated in log space for any q, M.

    Since E[X] = q/M exactly, E[(X - E X)^+] = E|X - E X|/2, and de Moivre's mean
    absolute deviation identity for the binomial gives
        E|X - np| = 2 m (1-p) C(n,m) p^m (1-p)^(n-m),   m = floor(np) + 1.
    Hence Phi(q,M) = (M/2) E|X - q/M|.  Checked against Phi_exact below.
    """
    if q == 0:
        return 0.0
    p = 1.0 / M
    n = q
    m = int(math.floor(n * p)) + 1
    if m > n:
        return 0.0
    lg = (math.lgamma(n + 1) - math.lgamma(m + 1) - math.lgamma(n - m + 1)
          + m * math.log(p) + (n - m) * math.log1p(-p))
    lmad = math.log(2.0 * m) + math.log1p(-p) + lg
    return math.exp(math.log(M / 2.0) + lmad)


def fit_advantage(K, q, M):
    """Exact advantage of the FIT attack: source flat on a KxK rectangle, observer
    queries q of its cells (resolution 1) and runs the Bayes test.  Equals
    sum_v (nu_bar(v) - 1/M)^+ = Phi(min(q,K^2), M) / K^2."""
    qq = min(q, K * K)
    return Phi(qq, M) / (K * K)


def stage3():
    print()
    print("=" * 78)
    print("S3  MECHANISM CATALOGUE AT REALISTIC PARAMETERS")
    print("=" * 78)
    print("Three mechanisms exhaust everything the search found.  Exact closed forms,")
    print("each checked against an independent Monte-Carlo simulation.")
    print()
    print("(a) HIT.  On an f-event of probability p both sources output one cell c*")
    print("    (E[m_i] = p + (1-p)/N <= delta), else uniform on [N].  Observer queries")
    print("    c* and accepts iff y = f(c*).   adv = p (1 - 1/M)  exactly.")
    print("    q queries -> q planted cells -> adv = min(1, q p)(1 - 1/M).")
    print("    M-dependence: the factor (1 - 1/M), bounded by 1.  Ceiling: q delta.")
    print()
    print("(b) PLANT.  Sources choose a KxK rectangle B1xB2 = argmax of the empirical")
    print("    density of an observer-side test set; observer runs the test.  The test")
    print("    set has density alpha in [M] BY CONSTRUCTION (e.g. accept iff")
    print("    f(u(y)) in S with |S| = alpha M), so the cell labels are i.i.d.")
    print("    Bernoulli(alpha) whatever M is: the mechanism is M-FREE identically.")
    print("    Measured below: the achievable bias a(N,K) and its independence of M.")
    print()
    print("(c) FIT.  Source flat on a KxK rectangle; observer spends q queries inside")
    print("    it and Bayes-tests the challenge against the partial histogram.")
    print("    EXACT:  adv = Phi(min(q,K^2), M) / K^2,  Phi(q,M) = M E[(Bin(q,1/M)-q/M)^+].")
    print("    Phi ~ min(q, sqrt(qM/2pi)): the M-dependence switches OFF for M >~ q.")
    print()
    print("S3a  FIT: the phase law.  Phi(q,M) as a function of M at fixed q.")
    qs = [1, 2, 4, 16, 64, 256, 1024]
    Ms = [2, 4, 16, 64, 256, 1024, 4096, 2 ** 16, 2 ** 24]
    print("  %6s | " % "q" + " | ".join("%9s" % ("M=2^%d" % int(math.log2(M)))
                                        for M in Ms) + " |  Phi(q,inf)=q")
    for q in qs:
        vals = []
        for M in Ms:
            vals.append(Phi(q, M) if q <= 1024 else float("nan"))
        print("  %6d | " % q + " | ".join("%9.4f" % v for v in vals)
              + " |  %8d" % q)
    print("  -> at fixed q, Phi is INCREASING in M but saturates at q; the whole")
    print("     M-dependence lives in M <~ q, and Phi(q,M)/q >= 1 - O(q/M).")
    print()
    print("  relative M-dependence remaining at M = c*q (Phi(q,M)/q):")
    print("  %8s | " % "q" + " | ".join("%9s" % ("M=%dq" % c) for c in (1, 4, 16, 64, 256)))
    for q in (4, 16, 64, 256):
        print("  %8d | " % q + " | ".join("%9.5f" % (Phi(q, c * q) / q)
                                          for c in (1, 4, 16, 64, 256)))
    print()
    print("  the deficit law: 1 - Phi(q,M)/q measured against q/M")
    print("  %8s | " % "q" + " | ".join("%17s" % ("M=%dq" % c)
                                        for c in (1, 4, 16, 64, 256, 1024)))
    for q in (16, 256, 4096):
        cells = []
        for c in (1, 4, 16, 64, 256, 1024):
            d = 1.0 - Phi(q, c * q) / q
            cells.append("%.6f (x%.4f)" % (d, d * c))
        print("  %8d | " % q + " | ".join(cells))
    print("  the bracket is deficit/(q/M): it is 1.00 to four digits for M >= 256q,")
    print("  so 1 - Phi(q,M)/q = (1-o(1)) q/M.  CONSEQUENCE FOR THE APPLICATIONS:")
    print("  at a 512-bit output (M = 2^512) and a generous q = 2^80 queries, the best")
    print("  known attack is M-free to relative accuracy 2^-432; its M-dependence")
    print("  cannot appear before q ~ M = 2^512 queries.")
    print()
    print("S3b  FIT: exact formula vs Monte Carlo (source flat on KxK, q cells probed)")
    print("  %4s %6s %5s | %12s | %12s | %9s" % ("K", "M", "q", "exact", "MC", "se"))
    for (K, M, q) in [(4, 4, 4), (4, 16, 8), (8, 8, 16), (8, 64, 32), (8, 64, 64),
                      (16, 16, 64), (16, 256, 128)]:
        ex = fit_advantage(K, q, M)
        mc, se = mc_fit(K, M, q, nsamp=400000)
        print("  %4d %6d %5d | %12.7f | %12.7f | %9.7f" % (K, M, q, ex, mc, se))
    print()
    print("S3c  PLANT: achievable bias by exhaustive densest-KxK-rectangle search in")
    print("     a random NxN Bernoulli(alpha) label matrix (alpha = 1/2 = the test's")
    print("     density in [M]), and the same quantity with the labels produced by an")
    print("     actual random f : [N]^2 -> [M] and test set S of size M/2 -- equal for")
    print("     every M, which is the M-freeness of the mechanism, measured.")
    print("  %4s %4s | %14s | %s" % ("N", "K", "bias(Bern 1/2)",
                                     "bias via f:[N]^2->[M], M = 2,8,64,4096"))
    for (N, K) in [(6, 2), (6, 3), (8, 2), (8, 3), (8, 4), (10, 3), (10, 4), (12, 4)]:
        b0 = plant_bias_bernoulli(N, K, 0.5, trials=400)
        row = []
        for M in (2, 8, 64, 4096):
            row.append(plant_bias_via_f(N, K, M, trials=400))
        print("  %4d %4d | %14.5f | %s" % (N, K, b0,
                                           "  ".join("%.5f" % r for r in row)))
    print("     sqrt(2 ln(N/K)/K)/2 for reference:")
    for (N, K) in [(6, 2), (6, 3), (8, 2), (8, 3), (8, 4), (10, 3), (10, 4), (12, 4)]:
        print("       N=%2d K=%d : %.5f" % (N, K, math.sqrt(2 * math.log(N / K) / K) / 2))
    print()
    print("S3d  steering buys nothing at q=1: collision test at ONE fixed cell vs a")
    print("     challenge-steered cell map u : [M] -> KxK rectangle (source flat on it)")
    print("  %4s %6s | %12s | %12s" % ("K", "M", "fixed cell", "steered u(y)"))
    for (K, M) in [(4, 8), (4, 64), (8, 16), (8, 256), (16, 1024)]:
        a, b = mc_steering(K, M, nsamp=400000)
        print("  %4d %6d | %12.7f | %12.7f" % (K, M, a, b))
    print("     (both equal 1/K^2 - o(1) = delta^2; steering neither helps nor hurts)")


def mc_fit(K, M, q, nsamp=200000, seed=5):
    """MC estimate of the FIT attack advantage; independent of the Phi formula."""
    rng = np.random.default_rng(seed)
    # oracle restricted to the KxK rectangle is all that matters
    f = rng.integers(0, M, size=(nsamp, K * K))
    Q = np.arange(q if q <= K * K else K * K)
    counts = np.zeros((nsamp, M), dtype=np.int32)
    for c in Q:
        counts[np.arange(nsamp), f[:, c]] += 1
    qq = len(Q)
    # Bayes test: accept iff n_y > q/M  (nu_bar(y) - 1/M has the sign of n_y - q/M)
    x = rng.integers(0, K * K, nsamp)
    y_real = f[np.arange(nsamp), x]
    y_ideal = rng.integers(0, M, nsamp)
    acc_r = counts[np.arange(nsamp), y_real] > qq / M
    acc_i = counts[np.arange(nsamp), y_ideal] > qq / M
    pr, pi_ = acc_r.mean(), acc_i.mean()
    se = math.sqrt((pr * (1 - pr) + pi_ * (1 - pi_)) / nsamp)
    return float(pr - pi_), se


def plant_bias_bernoulli(N, K, alpha, trials=200, seed=11):
    """E[ max over KxK rectangles of empirical density ] - alpha, exhaustive over
    rectangles (N,K small)."""
    rng = np.random.default_rng(seed)
    rows = list(itertools.combinations(range(N), K))
    tot = 0.0
    for _ in range(trials):
        A = (rng.random((N, N)) < alpha).astype(np.float64)
        best = -1.0
        for R in rows:
            sub = A[list(R), :]                 # K x N
            colsum = sub.sum(axis=0)            # per column
            top = np.sort(colsum)[::-1][:K].sum()
            best = max(best, top / (K * K))
        tot += best - alpha
    return tot / trials


def plant_bias_via_f(N, K, M, trials=200, seed=12):
    """Same, but the labels come from a genuine f : [N]^2 -> [M] and a test set S of
    size ceil(M/2): label(u) = 1[f(u) in S].  Must be independent of M."""
    rng = np.random.default_rng(seed)
    rows = list(itertools.combinations(range(N), K))
    S = set(range(M // 2)) if M % 2 == 0 else set(range((M + 1) // 2))
    alpha = len(S) / M
    tot = 0.0
    for _ in range(trials):
        f = rng.integers(0, M, size=(N, N))
        A = np.isin(f, list(S)).astype(np.float64)
        best = -1.0
        for R in rows:
            sub = A[list(R), :]
            colsum = sub.sum(axis=0)
            top = np.sort(colsum)[::-1][:K].sum()
            best = max(best, top / (K * K))
        tot += best - alpha
    return tot / trials


def mc_steering(K, M, nsamp=200000, seed=13):
    """collision test at a fixed cell vs a challenge-steered cell, source flat on KxK."""
    rng = np.random.default_rng(seed)
    f = rng.integers(0, M, size=(nsamp, K * K))
    x = rng.integers(0, K * K, nsamp)
    y_real = f[np.arange(nsamp), x]
    y_ideal = rng.integers(0, M, nsamp)
    # fixed cell 0
    a_r = (f[:, 0] == y_real).mean()
    a_i = (f[:, 0] == y_ideal).mean()
    # steered: u(y) = y mod K^2
    u_r = y_real % (K * K)
    u_i = y_ideal % (K * K)
    b_r = (f[np.arange(nsamp), u_r] == y_real).mean()
    b_i = (f[np.arange(nsamp), u_i] == y_ideal).mean()
    return float(a_r - a_i), float(b_r - b_i)


# --------------------------------------------------------------------------- #
# S4: corner audit                                                            #
# --------------------------------------------------------------------------- #

def best_known_attack(N, M, sigma, d, q):
    """Best advantage over the whole catalogue, maximised over internal parameters.

    HIT   : min(1, q*p) (1 - 1/M) with p <= delta            (needs no leakage)
    FIT   : p * Phi(min(q,K^2), M) / K^2 maximised over K <= N and p <= min(1, d*K)
            (the p-event variant: with probability p, announced by one leakage bit,
             both sources restrict to a KxK rectangle; E[m_i] = p/K + (1-p)/N <= d)
    PLANT : c * sqrt(sigma' delta) with c = 1 (an over-generous stand-in: the
            measured constant in S3c is below 1/2, and the mechanism is M-free)
    """
    hit = min(1.0, d * math.sqrt(max(q, 1))) * (1.0 - 1.0 / M)
    fit = 0.0
    argK = None
    # LEAKAGE AS VIRTUAL QUERIES: sigma bits can announce the values of
    # sigma/log2(M) cells (S1S measures exactly this substitution), so the FIT
    # mechanism is credited with q + sigma/log2 M probed cells.  Generous.
    qeff = q + sigma / math.log2(M)
    Ks = sorted({1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 64, 128, 1024, 2 ** 15, N}
                | {int(round(math.sqrt(max(qeff, 1)))), max(1, int(round(1.0 / d)))})
    for K in Ks:
        if K < 1 or K > N:
            continue
        p = min(1.0, d * K)
        qq = min(qeff, K * K)
        if qq < 1:
            continue
        val = min(1.0, p * Phi(int(round(qq)), M) / (K * K))
        if val > fit:
            fit, argK = val, K
    plant = min(1.0, math.sqrt(sigma_prime(sigma, N) * d))
    return dict(hit=hit, fit=fit, plant=plant, argK=argK,
                best=min(1.0, max(hit, fit, plant)))


def stage4():
    print()
    print("=" * 78)
    print("S4  CORNER AUDIT OVER A LARGE PARAMETER GRID")
    print("=" * 78)
    print("For every grid point the best attack in the catalogue is compared with")
    print("  mfree = 5 sqrt(sigma' delta) + mu'(q)      (the conjectured M-free bound)")
    print("  D''   = 5 sqrt(sigma' delta) + min(mu'(min(qM,N^2)), 2 delta sqrt M)")
    print("  conj  = sqrt(sigma' q+ delta)              (the Contract's target)")
    print("and the corner condition M > sigma' q+/(4 delta), i.e. (H2) fails.")
    print("A counterexample to M-freeness at small q needs best > mfree AND corner.")
    print()
    Ns = [2 ** k for k in (4, 6, 8, 10, 14, 20, 30)]
    sigmas = [0, 1, 8, 64]
    qs = [0, 1, 2, 8, 64, 1024, 65536]
    Mfracs = None
    Ms = [2, 4, 16, 256, 2 ** 16, 2 ** 32, 2 ** 64]
    dmults = [1.0, 2.0, 8.0, 64.0, 1024.0]      # delta = dmult / N, capped at 1
    print("GRID: N in %s" % [int(math.log2(n)) for n in Ns], "(as log2)")
    print("      sigma in %s" % sigmas)
    print("      q in %s" % qs)
    print("      M in %s (as log2)" % [round(math.log2(m)) for m in Ms])
    print("      delta = mult/N, mult in %s (capped at 1)" % dmults)
    n_pts = n_corner = n_viol_mfree = n_viol_dd = n_viol_conj = 0
    n_nonvac = n_surplus = 0
    worst = (0.0, None)
    worst_corner = (0.0, None)
    worst_conj = (0.0, None)
    worst_nonvac = (0.0, None)
    worst_surplus = (0.0, None)
    Minf = 2 ** 200
    for N in Ns:
        for sigma in sigmas:
            sp = sigma_prime(sigma, N)
            for q in qs:
                for M in Ms:
                    for mult in dmults:
                        d = min(1.0, mult / N)
                        n_pts += 1
                        t = targets(N, M, sigma, d, q)
                        a = best_known_attack(N, M, sigma, d, q)
                        ainf = best_known_attack(N, Minf, sigma, d, q)
                        r = a["best"] / t["mfree"]
                        if r > worst[0]:
                            worst = (r, (N, M, sigma, d, q, a))
                        rc = a["best"] / t["conj"]
                        if rc > worst_conj[0]:
                            worst_conj = (rc, (N, M, sigma, d, q, a))
                        if a["best"] > t["mfree"] + 1e-12:
                            n_viol_mfree += 1
                        if a["best"] > t["cordd"] + 1e-12:
                            n_viol_dd += 1
                        if a["best"] > t["conj"] + 1e-12:
                            n_viol_conj += 1
                        # M-SURPLUS: how much of the attack is NOT available at M=infinity
                        surplus = a["best"] - ainf["best"]
                        if surplus > 1e-12:
                            n_surplus += 1
                            if surplus > worst_surplus[0]:
                                worst_surplus = (surplus, (N, M, sigma, d, q, a))
                        if t["mfree"] <= 0.5:                  # non-vacuous target
                            n_nonvac += 1
                            if r > worst_nonvac[0]:
                                worst_nonvac = (r, (N, M, sigma, d, q, a))
                        if t["corner"]:
                            n_corner += 1
                            if r > worst_corner[0]:
                                worst_corner = (r, (N, M, sigma, d, q, a))
    print()
    print("grid points evaluated            : %d" % n_pts)
    print("of which in the corner (H2 fails): %d" % n_corner)
    print("of which non-vacuous (mfree<=1/2): %d" % n_nonvac)
    print("points where best attack > mfree : %d" % n_viol_mfree)
    print("points where best attack > D''   : %d" % n_viol_dd)
    print("points where best attack > conj  : %d" % n_viol_conj)
    print("points where best attack at this M EXCEEDS its own M=2^200 value : %d"
          % n_surplus)
    for name, w in (("max best/mfree over grid", worst),
                    ("max best/mfree over corner points", worst_corner),
                    ("max best/mfree over non-vacuous pts", worst_nonvac),
                    ("max best/conj over grid", worst_conj),
                    ("max M-surplus over grid", worst_surplus)):
        if w[1] is None:
            print("%-36s : none" % name)
            continue
        N, M, sigma, d, q, a = w[1]
        print("%-36s : %.6f   at N=2^%.0f M=2^%.0f sigma=%d delta=%.3g q=%d "
              "(hit=%.4g fit=%.4g plant=%.4g K*=%s)"
              % (name, w[0], math.log2(N), math.log2(M), sigma, d, q,
                 a["hit"], a["fit"], a["plant"], a["argK"]))
    print()
    print("Note: PLANT is entered as the generous stand-in sqrt(sigma' delta), which")
    print("EQUALS the Contract's target at q=0 by construction, so the 'best/conj'")
    print("ratio 1.0 at q=0 is definitional; S3c measures the real constant near 1/3.")
    print()
    print("Monotonicity of Phi in M (so that FIT(M) <= FIT(M=infinity) = M-free):")
    bad, worstrel = 0, 0.0
    for q in (1, 2, 3, 5, 8, 13, 21, 64, 256, 1024, 4096, 65536):
        prev = -1.0
        loc = 0
        for e in range(1, 80):
            v = Phi(q, 2 ** e)
            if prev > 0 and v < prev:
                rel = (prev - v) / prev
                worstrel = max(worstrel, rel)
                if rel > 1e-9:
                    loc += 1
            prev = v
        bad += loc
        print("  q=%6d : Phi(q,2)=%.4f ... Phi(q,2^79)=%.6f   limit q=%d  monotone=%s"
              % (q, Phi(q, 2), Phi(q, 2 ** 79), q, loc == 0))
    print("  monotonicity violations (rel > 1e-9) over the 12 x 79 grid : %d ; "
          "largest relative decrease anywhere = %.2e (float noise in lgamma)"
          % (bad, worstrel))
    print()
    print("Residual M-dependence AT the corner threshold M0 = sigma' q+/(4 delta),")
    print("as 1 - Phi(q,M0)/q  (the fraction of the FIT attack that M costs there);")
    print("sigma=0, delta=1/N:")
    for N in (2 ** 10, 2 ** 20, 2 ** 40):
        for q in (1, 2, 8, 1024):
            d = 1.0 / N
            M0 = sigma_prime(0, N) * (q + 1) / (4 * d)
            print("  N=2^%2d q=%6d : M0=%.4g   1 - Phi(q,M0)/q = %.3e"
                  % (math.log2(N), q, M0, 1.0 - Phi(q, int(M0)) / q))
    print()
    print("VACUITY FRONTIER -- why the exact brute force cannot be run in the corner.")
    print("A corner point says anything only if the bound it replaces is below 1:")
    print("  5 sqrt(sigma' delta) < 1  and  2 delta sqrt M < 1, with delta >= 1/N.")
    print("The second gives M < 1/(4 delta^2) <= N^2/4, so the MEANINGFUL corner is")
    print("  sigma' q+/(4 delta) < M < 1/(4 delta^2),  non-empty iff sigma' q+ delta < 1.")
    print("The first forces delta < 1/(25 sigma') and hence N > 50 log2 N:")
    for sig in (0, 1, 8):
        Nmin = None
        for e in range(1, 40):
            N = 2 ** e
            if 5 * math.sqrt(sigma_prime(sig, N) / N) < 1:
                Nmin = N
                break
        if Nmin:
            print("  sigma=%2d : smallest N with a non-vacuous point at delta=1/N is "
                  "2^%d = %d, i.e. |domain| = N^2 = %.3g cells and |Fun| = M^(N^2)"
                  % (sig, round(math.log2(Nmin)), Nmin, Nmin ** 2))
    print("  -> no non-vacuous instance can be enumerated; S1/S2 therefore probe the")
    print("     FUNCTIONAL FORM of the M-dependence, and S3/S4/S5 carry it to the corner.")
    print()
    print("Where the FIT mechanism's M-dependence lives: for each q, the largest M at")
    print("which FIT still gains 10% over its M -> infinity limit (delta=1/N, N=2^20):")
    N = 2 ** 20
    d = 1.0 / N
    for q in (1, 2, 8, 64, 1024):
        lim = best_known_attack(N, 2 ** 62, 0, d, q)["fit"]
        cut = None
        for e in range(1, 62):
            M = 2 ** e
            v = best_known_attack(N, M, 0, d, q)["fit"]
            if lim > 0 and v < 0.9 * lim:
                cut = M
        print("  q=%6d : FIT(M=inf)=%.6g ; last M with FIT < 0.9*limit : %s ; "
              "corner needs M > %.3g"
              % (q, lim, ("2^%.0f" % math.log2(cut)) if cut else "none",
                 sigma_prime(0, N) * (q + 1) / (4 * d)))


# --------------------------------------------------------------------------- #
# S5: open-ended sampled search at moderate N, with a train/test split         #
# --------------------------------------------------------------------------- #

def stage5():
    print()
    print("=" * 78)
    print("S5  OPEN-ENDED SEARCH AT MODERATE N (sampled oracles, train/test split)")
    print("=" * 78)
    print("Fun is too large to enumerate, so oracles are sampled.  The observer table")
    print("(u : [M] -> cells, beta : [M]x[M] -> {0,1}) is FITTED on train oracles and")
    print("SCORED on fresh ones, with the source recomputed on the fresh oracles by the")
    print("same f-measurable argmax rule.  Overfitting to the sample therefore cannot")
    print("manufacture a counterexample: only the test score is reported.")
    print("Rectangles: all k x k with k in Kset, chosen per oracle by greedy densest-")
    print("submatrix (rows then columns, 3 passes) against the observer's own labels.")
    print()
    grid = [(4, [4, 16, 64, 256, 1024], [2, 3]),
            (6, [4, 16, 64, 256], [2, 3, 4]),
            (8, [16, 64, 256], [2, 4])]
    print("GRID: (N, M list, k list) = %s ; ntrain=ntest=40000 ; 6 alternations" % grid)
    print()
    print("  Pr[accept] in Real and in Real_0 are printed too: an advantage that")
    print("  grows only because Pr[accept | Real] -> 1 while Pr[accept | Real_0]")
    print("  approaches a constant is the PLANT ceiling 1 - p_theta being approached,")
    print("  not growth in M.")
    print("  %3s %6s %3s | %9s | %9s | %7s %7s | %9s | %6s | %s"
          % ("N", "M", "k", "train adv", "TEST adv", "P[acc|R]", "P[acc|R0]",
             "5sqrt(s'd)", "corner", "verdict"))
    series = {}
    for (N, Ms, ks) in grid:
        for k in ks:
            for M in Ms:
                tr, te, d, pr, pi_ = sampled_search(N, M, k, ntrain=40000,
                                                    ntest=40000)
                t = targets(N, M, 1, d, 1)
                verdict = "OK" if te <= t["mfree"] + 1e-9 else "*** EXCEEDS mfree ***"
                print("  %3d %6d %3d | %9.6f | %9.6f | %7.4f %7.4f | %9.6f | %6s | %s"
                      % (N, M, k, tr, te, pr, pi_, t["lead"], t["corner"], verdict))
                series.setdefault((N, 1, 1, 1.0 / k), {})[M] = te
    m_scaling_diagnostic(series)


def sampled_search(N, M, k, ntrain=40000, ntest=40000, rounds=6, seed=21):
    """Alternating fit of a full 1-query observer table against a greedy flat source.

    The source is: with probability 1 (announced by no leakage) x_i uniform on a
    k-subset B_i(f) chosen greedily to maximise the observer's acceptance density on
    B_1 x B_2.  delta = 1/k exactly.  The observer is a full table (u, beta).
    """
    rng = np.random.default_rng(seed)
    n2 = N * N
    Ftr = rng.integers(0, M, size=(ntrain, n2))
    Fte = rng.integers(0, M, size=(ntest, n2))

    def greedy_rect(F, TH):
        """per-oracle greedy k x k rectangle maximising mean theta(f(u)) on it."""
        n = F.shape[0]
        lab = TH[np.arange(n)[:, None], F]            # (n, n2) in {0,1}
        lab = lab.reshape(n, N, N).astype(np.float64)
        rows = np.argsort(-lab.sum(axis=2), axis=1)[:, :k]     # start: best k rows
        for _ in range(3):
            sub = np.take_along_axis(lab, rows[:, :, None], axis=1)      # (n,k,N)
            cols = np.argsort(-sub.sum(axis=1), axis=1)[:, :k]
            sub2 = np.take_along_axis(lab, cols[:, None, :], axis=2)     # (n,N,k)
            rows = np.argsort(-sub2.sum(axis=2), axis=1)[:, :k]
        return rows, cols

    def source_cells(F, rows, cols):
        n = F.shape[0]
        cell = (rows[:, :, None] * N + cols[:, None, :]).reshape(n, k * k)
        return cell

    # init observer: collision test at cell 0
    u = np.zeros(M, dtype=int)
    beta = np.eye(M, dtype=bool)
    TH = beta[:, :].T                                   # placeholder
    def theta_table(F, u, beta):
        n = F.shape[0]
        TH = np.zeros((n, M), dtype=np.uint8)
        for v in range(M):
            TH[:, v] = beta[v][F[:, u[v]]]
        return TH

    for _ in range(rounds):
        TH = theta_table(Ftr, u, beta)
        rows, cols = greedy_rect(Ftr, TH)
        cell = source_cells(Ftr, rows, cols)
        vals = Ftr[np.arange(ntrain)[:, None], cell]     # (ntrain, k*k)
        # W[i, v] = rho_i(v) - 1/M
        W = np.zeros((ntrain, M))
        for j in range(k * k):
            W[np.arange(ntrain), vals[:, j]] += 1.0 / (k * k)
        W -= 1.0 / M
        W /= ntrain
        # exact best observer table given this source (two passes, O(M^2) memory)
        best_gain = np.full(M, -np.inf)
        best_cell = np.zeros(M, dtype=int)
        for c in range(n2):
            oh = (Ftr[:, c][:, None] == np.arange(M)[None, :])
            A = oh.T.astype(np.float64) @ W               # [b][v]
            gain = np.maximum(A, 0.0).sum(axis=0)
            upd = gain > best_gain
            best_gain = np.where(upd, gain, best_gain)
            best_cell = np.where(upd, c, best_cell)
        u = best_cell
        beta = np.zeros((M, M), dtype=bool)
        for c in np.unique(u):
            oh = (Ftr[:, c][:, None] == np.arange(M)[None, :])
            A = oh.T.astype(np.float64) @ W
            vs = np.nonzero(u == c)[0]
            beta[vs] = (A[:, vs] > 0).T
    # train score
    TH = theta_table(Ftr, u, beta)
    rows, cols = greedy_rect(Ftr, TH)
    cell = source_cells(Ftr, rows, cols)
    vals = Ftr[np.arange(ntrain)[:, None], cell]
    tr = float(TH[np.arange(ntrain)[:, None], vals].mean()
               - TH.mean())
    # test score, source recomputed by the same rule on fresh oracles
    THt = theta_table(Fte, u, beta)
    rows, cols = greedy_rect(Fte, THt)
    cell = source_cells(Fte, rows, cols)
    vals = Fte[np.arange(ntest)[:, None], cell]
    te_real = float(THt[np.arange(ntest)[:, None], vals].mean())
    te_ideal = float(THt.mean())
    te = te_real - te_ideal
    return tr, te, 1.0 / k, te_real, te_ideal


# --------------------------------------------------------------------------- #

def stage6():
    print()
    print("=" * 78)
    print("S6  WHAT THE OBSTRUCTION SUGGESTS: A TRANSCRIPT UNION IN PLACE OF THE")
    print("    UNION OVER ALL 2^M TESTS  (a lead for the prover, checked numerically)")
    print("=" * 78)
    print("Where delta sqrt(M) comes from: Lemma B of kappa-2-r3 makes the rectangle")
    print("discrepancy bound hold simultaneously for ALL theta : [M] -> {0,1}, at a")
    print("cost of M ln 2 inside the numerator of t, which surfaces as delta sqrt(M).")
    print("That quantifier grants the observer a test depending on ALL of f.  A")
    print("q-query observer's test on challenge v depends on f only through the q")
    print("cells of THAT challenge's transcript, and (S1/S2/S3, exactly) the whole")
    print("signal is then the mass of the inspected cells:")
    print("      E[ rho(v) | transcript ] - 1/M = (n_v - q/M)/K^2,")
    print("      sum_v | . | = Phi(q,M)/K^2 <= q delta^2   for q <= M.")
    print("So the natural repair is to union over TRANSCRIPTS, not over tests:")
    print("      C_1 = M ln 2 + ln(4N^2/gamma_0)   ~~>   C_1' = q ln(N^2 M) + ln(4N^2/gamma_0),")
    print("giving  delta sqrt(2 C_1')  ~  delta sqrt(2 q ln(N^2 M))  in place of")
    print("delta sqrt(2 M ln 2).  Below: would that suffice for the Contract's target")
    print("      C sqrt(sigma' q+ delta) ?")
    print()
    print("  ratio R := [1.3013 sqrt(sigma' d) + d sqrt(2 q ln(N^2 M) + 2 ln(4N^2/d)) + d]")
    print("             / sqrt(sigma' q+ d)")
    print("  (numerator = Corollary D' with C_1 replaced by C_1'; a ratio bounded by")
    print("   an absolute constant means the repair reaches the Contract's bound.)")
    Ns = [2 ** k for k in (4, 8, 10, 14, 20, 30, 40)]
    sigmas = [0, 1, 8, 64]
    qs = [0, 1, 2, 8, 64, 1024, 65536]
    dmults = [1.0, 2.0, 8.0, 64.0, 1024.0]
    worst = (0.0, None)
    worst_mean = (0.0, None)
    npts = nmean = 0
    for N in Ns:
        for sigma in sigmas:
            sp = sigma_prime(sigma, N)
            for q in qs:
                for mult in dmults:
                    d = min(1.0, mult / N)
                    # the meaningful corner window
                    lo = sp * (q + 1) / (4 * d)
                    hi = 1.0 / (4 * d * d)
                    for M in [2, 4, 2 ** 8, 2 ** 16, 2 ** 32, 2 ** 64,
                              max(2, int(lo) + 1), max(2, int(hi))]:
                        if M < 2:
                            continue
                        num = (1.3013 * math.sqrt(sp * d)
                               + d * math.sqrt(2 * q * math.log(N * N * M)
                                               + 2 * math.log(4 * N * N / d)) + d)
                        R = num / math.sqrt(sp * (q + 1) * d)
                        npts += 1
                        if R > worst[0]:
                            worst = (R, (N, M, sigma, d, q))
                        if lo < M < hi:                 # meaningful corner
                            nmean += 1
                            if R > worst_mean[0]:
                                worst_mean = (R, (N, M, sigma, d, q))
    for name, w, n in (("max R over the whole grid", worst, npts),
                       ("max R inside the meaningful corner", worst_mean, nmean)):
        if w[1] is None:
            print("  %-38s : none (%d points)" % (name, n))
            continue
        N, M, sigma, d, q = w[1]
        print("  %-38s : %.4f   at N=2^%.0f M=2^%.1f sigma=%d delta=%.3g q=%d "
              "(%d points)"
              % (name, w[0], math.log2(N), math.log2(M), sigma, d, q, n))
    print()
    print("  For comparison, the SAME ratio with the current C_1 (i.e. delta sqrt M):")
    worst2 = (0.0, None)
    for N in Ns:
        for sigma in sigmas:
            sp = sigma_prime(sigma, N)
            for q in qs:
                for mult in dmults:
                    d = min(1.0, mult / N)
                    lo = sp * (q + 1) / (4 * d)
                    hi = 1.0 / (4 * d * d)
                    for M in [max(2, int(lo) + 1), max(2, int(hi)), 2 ** 32]:
                        num = (1.3013 * math.sqrt(sp * d) + 2 * d * math.sqrt(M) + d)
                        R = num / math.sqrt(sp * (q + 1) * d)
                        if lo < M < hi and R > worst2[0]:
                            worst2 = (R, (N, M, sigma, d, q))
    if worst2[1]:
        N, M, sigma, d, q = worst2[1]
        print("  max R inside the meaningful corner       : %.4f   at N=2^%.0f "
              "M=2^%.1f sigma=%d delta=%.3g q=%d"
              % (worst2[0], math.log2(N), math.log2(M), sigma, d, q))
    print()
    print("  CAVEAT.  This is an arithmetic feasibility check of a PROOF SKETCH, not")
    print("  a proof.  What it does not supply: the transcript-conditioned rectangle")
    print("  discrepancy bound itself.  The obstruction is that the source's")
    print("  rectangle B_1 x B_2 is chosen AFTER f, hence is not measurable w.r.t.")
    print("  the observer's transcript, so the conditional-mean identity above needs")
    print("  a union over rectangles taken INSIDE the conditioning -- which is where")
    print("  the sqrt(sigma' delta) comes from and where the work remains.")


def main():
    which = sys.argv[1:] or ["1", "1e", "1b", "1s", "1v", "2", "3", "3e", "3f", "4", "5", "6"]
    print("refuter-mcorner : counterexample search for the M-corner, campaign c/0010")
    print("python %s ; numpy %s" % (sys.version.split()[0], np.__version__))
    print("stages requested: %s" % which)
    res = None
    if "1" in which:
        res = stage1()
    if "1e" in which:
        stage1_exhaustive()
    if "1b" in which:
        stage1_bigM()
    if "1s" in which:
        stage1_leakage()
    if "1v" in which and res is not None:
        stage1_verify(res)
    if "2" in which:
        stage2()
    if "3" in which:
        stage3()
    if "3e" in which:
        stage3e()
    if "3f" in which:
        stage3f()
    if "4" in which:
        stage4()
    if "5" in which:
        stage5()
    if "6" in which:
        stage6()


if __name__ == "__main__":
    main()
