#!/usr/bin/env python3
"""HATTER-SOL-16: rigorous compact-strip certificate.

This closes 4 <= mu <= 23/5.  Together with the existing exact
large-mu certificate, it proves the A5 scalar Mahler class ordering for
all mu >= 4.

The script deliberately reuses the already audited boundary machinery:
  a5_boundary_mahler_mu4_interval_certificate.py
That module provides the exact Q(sqrt(5)) determinant construction,
14 Mahler-type representatives, exact tensor-gap lower bounds, and
outward-rounded interval arithmetic.
"""

from fractions import Fraction
import time

import a5_boundary_mahler_mu4_interval_certificate as base

iv = base.iv
iv.dps = 30

TYPE_INDICES = base.TYPE_INDICES
GAMMA = base.GAMMA
GRID = base.GRID


def det_coefficient_polynomials(a, b):
    """Return P2,P1,P0 for det(mu I-H)=mu^3+P2 mu^2+P1 mu+P0."""
    t1 = base.trace_power(a, b, 1)
    t2 = base.trace_power(a, b, 2)
    t3 = base.trace_power(a, b, 3)
    p2 = base.pscale(t1, Fraction(-1))
    p1 = base.pscale(
        base.padd(base.pmul(t1, t1), base.pscale(t2, -1)),
        Fraction(1, 2),
    )
    cubic = base.padd(
        base.padd(
            base.pmul(base.pmul(t1, t1), t1),
            base.pscale(base.pmul(t1, t2), -3),
        ),
        base.pscale(t3, 2),
    )
    p0 = base.pscale(cubic, Fraction(-1, 6))
    return p2, p1, p0


def evaluate_laurent_grid(poly, M):
    """Outward-rounded values of an exact Laurent polynomial on the M-grid."""
    _, pows = base.roots_and_pows(M)
    coeff = {(m, n): base.iq(c) for (m, n), c in poly.items()}
    rows = []
    for i in range(M):
        zp = pows[i]
        cn = {
            n: sum(
                (coeff.get((m, n), iv.mpf(0)) * zp[m] for m in range(-3, 4)),
                iv.mpc(0),
            )
            for n in range(-3, 4)
        }
        row = []
        for j in range(M):
            value = sum(
                (cn[n] * pows[j][n] for n in range(-3, 4)),
                iv.mpc(0),
            ).real
            row.append(value)
        rows.append(row)
    return rows


# Precompute the mu-independent cubic coefficient grids once.
COEFF_GRIDS = {}
for idx in TYPE_INDICES:
    a, b = base.reps[idx]
    p2, p1, p0 = det_coefficient_polynomials(a, b)
    M = GRID[idx]
    COEFF_GRIDS[idx] = (
        evaluate_laurent_grid(p2, M),
        evaluate_laurent_grid(p1, M),
        evaluate_laurent_grid(p0, M),
    )


# Exact check of the universal second torus moment S_2=12.
for idx in TYPE_INDICES:
    a, b = base.reps[idx]
    t2 = base.trace_power(a, b, 2)
    assert t2[(0, 0)] == (Fraction(12), Fraction(0))


CLASSES = {
    idx: base.cname(base.comm(*base.reps[idx]))
    for idx in TYPE_INDICES
}


def certified_G(idx, mu):
    """Certified interval for G(mu)=M(mu)-3 log(mu)+6/mu^2.

    For a type with tensor gap gamma, the boundary theorem gives
        ||H||/4 < q_gamma = sqrt(1-gamma/6).
    Hence at general mu>=4 the logarithmic expansion ratio is
        r = 4 q_gamma / mu < 1.
    The same Fourier-support argument as in the boundary certificate gives
        |G-T_M(normalized)| <= 6 r^M / (M(1-r)).
    """
    M = GRID[idx]
    g2, g1, g0 = COEFF_GRIDS[idx]
    muv = iv.mpf(mu.numerator) / mu.denominator
    mu2 = muv * muv
    mu3 = mu2 * muv

    total = iv.mpf(0)
    for i in range(M):
        row2, row1, row0 = g2[i], g1[i], g0[i]
        for j in range(M):
            detv = mu3 + row2[j] * mu2 + row1[j] * muv + row0[j]
            assert detv > 0
            total += iv.log(detv)

    avg = total / (M * M)
    gamma = iv.mpf(GAMMA[idx].numerator) / GAMMA[idx].denominator
    q = iv.sqrt(1 - gamma / 6)
    r = 4 * q / muv
    alias = 6 * (r ** M) / (M * (1 - r))

    return (
        avg
        - 3 * iv.log(muv)
        + 6 / (muv ** 2)
        + alias * iv.mpf([-1, 1])
    )


# Monotonicity input (analytic, not numerical):
#
#   M(mu)=3 log mu - sum_{n>=1} S_n/(n mu^n).
#
# Torus balancing forces every odd S_n to vanish.  S_2=12, as checked
# exactly above, and H(theta,phi) is Hermitian, so every even moment
# S_{2m}=<Tr H^{2m}> is nonnegative. Therefore
#
#   G(mu)=M(mu)-3 log mu+6/mu^2
#        =-sum_{m>=2} S_{2m}/(2m mu^{2m})
#
# satisfies
#
#   G'(mu)=sum_{m>=2} S_{2m}/mu^{2m+1} >= 0.
#
# Thus a finite node chain can rigorously cover each whole mu-slab.

NODES = [Fraction(4, 1) + Fraction(k, 100) for k in range(61)]

previous = None
previous_mu = None
min_gap_5A_3A = None
min_gap_3A_5B = None
min_gap_5A_3A_where = None
min_gap_3A_5B_where = None

started = time.time()
for node_number, mu in enumerate(NODES):
    current = {idx: certified_G(idx, mu) for idx in TYPE_INDICES}

    if previous is not None:
        # If mu lies in [previous_mu,mu], monotonicity gives
        # G_low(mu_variable) <= G_low(mu) and
        # G_high(mu_variable) >= G_high(previous_mu).
        for i in TYPE_INDICES:
            if CLASSES[i] == "5A":
                for j in TYPE_INDICES:
                    if CLASSES[j] != "3A":
                        continue
                    assert current[i] < previous[j]
                    margin = previous[j] - current[i]
                    diagnostic = float(margin.a)
                    if min_gap_5A_3A is None or diagnostic < min_gap_5A_3A:
                        min_gap_5A_3A = diagnostic
                        min_gap_5A_3A_where = (previous_mu, mu, i, j)

            if CLASSES[i] == "3A":
                for j in TYPE_INDICES:
                    if CLASSES[j] != "5B":
                        continue
                    assert current[i] < previous[j]
                    margin = previous[j] - current[i]
                    diagnostic = float(margin.a)
                    if min_gap_3A_5B is None or diagnostic < min_gap_3A_5B:
                        min_gap_3A_5B = diagnostic
                        min_gap_3A_5B_where = (previous_mu, mu, i, j)

    previous = current
    previous_mu = mu

print("HATTER-SOL-16 global A5 compact-strip certificate")
print("nodes =", len(NODES), "step = 1/100")
print("covered interval = [4,23/5]")
print("minimum certified 5A<3A slab margin =", min_gap_5A_3A)
print("  at", min_gap_5A_3A_where)
print("minimum certified 3A<5B slab margin =", min_gap_3A_5B)
print("  at", min_gap_3A_5B_where)
print("elapsed seconds =", time.time() - started)
print("PASS: M(5A)<M(3A)<M(5B) on every slab 4<=mu<=23/5")
print("Together with the existing mu>=23/5 theorem: PASS for every mu>=4")
