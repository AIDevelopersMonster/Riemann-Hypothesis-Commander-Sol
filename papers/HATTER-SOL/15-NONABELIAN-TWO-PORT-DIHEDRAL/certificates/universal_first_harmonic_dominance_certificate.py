from fractions import Fraction
from math import comb

# HATTER-SOL-15
# Exact finite certificate used in the audited universal first-harmonic
# dominance proof. No floating-point arithmetic is used in any assertion.


class I:
    """Closed rational interval."""

    def __init__(self, lo, hi=None):
        self.lo = Fraction(lo)
        self.hi = Fraction(hi if hi is not None else lo)
        if self.lo > self.hi:
            self.lo, self.hi = self.hi, self.lo

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-(other if isinstance(other, I) else I(other)))

    def __rsub__(self, other):
        return I(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        vals = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        if not (other.lo > 0 or other.hi < 0):
            raise ZeroDivisionError("interval contains zero")
        vals = [
            self.lo / other.lo,
            self.lo / other.hi,
            self.hi / other.lo,
            self.hi / other.hi,
        ]
        return I(min(vals), max(vals))


def horner(coeffs, interval):
    """Exact interval Horner evaluation; coeffs ascending in degree."""
    out = I(coeffs[-1])
    for c in reversed(coeffs[:-1]):
        out = out * interval + c
    return out


# For x=mu/sqrt(mu^2-4), y=x-1,
#   Q_m(x)=y H_m(y),
# and E_m=c_m s^(-2m) Q_m(x),
# c_m=binom(2m,m)/m.

H_NUM = {
    2: [8, -5, -5],
    3: [72, 36, -200, -225, -63],
    4: [256, 608, -1120, -4730, -5316, -2503, -429],
    5: [
        3200, 16000, -8000, -186800, -457408,
        -520240, -313840, -97145, -12155,
    ],
    6: [
        9216, 77184, 65408, -1234464, -5537280,
        -11191712, -12945888, -9082386, -3825100,
        -890589, -88179,
    ],
    7: [
        50176, 627200, 1505280, -12418560, -95472384,
        -300811392, -552681600, -650654760, -506404360,
        -259754572, -84542976, -15833755, -1300075,
    ],
}
H_DEN = {2: 2, 3: 8, 4: 16, 5: 128, 6: 256, 7: 1024}


def h_interval(m, y):
    if m == 1:
        return (I(2) - y) / (I(2) + y)
    raw = horner(H_NUM[m], y)
    den = Fraction(H_DEN[m])
    return I(raw.lo / den, raw.hi / den)


# ---------------------------------------------------------------------------
# A. Global sign of the first seven m-layers.
# ---------------------------------------------------------------------------

SUBDIVISIONS = 200

global_h_lower = {}
for m in range(2, 8):
    best = None
    for i in range(SUBDIVISIONS):
        y = I(
            Fraction(i, 6 * SUBDIVISIONS),
            Fraction(i + 1, 6 * SUBDIVISIONS),
        )
        h = h_interval(m, y)
        best = h.lo if best is None or h.lo < best else best
    global_h_lower[m] = best
    assert best > 0


# ---------------------------------------------------------------------------
# B. Near-boundary lower bound, 4 <= mu <= 4.1.
# ---------------------------------------------------------------------------

BETA = {
    1: Fraction(123, 1000),
    2: Fraction(51, 100),
    3: Fraction(129, 100),
    4: Fraction(27, 10),
    5: Fraction(101, 20),
    6: Fraction(79, 10),
    7: Fraction(19, 10),
}

near_q_lower = {}
for m in range(1, 8):
    best = None
    for i in range(SUBDIVISIONS):
        lo = Fraction(1, 7) + (Fraction(1, 6) - Fraction(1, 7)) * Fraction(i, SUBDIVISIONS)
        hi = Fraction(1, 7) + (Fraction(1, 6) - Fraction(1, 7)) * Fraction(i + 1, SUBDIVISIONS)
        y = I(lo, hi)
        q = y * h_interval(m, y)
        best = q.lo if best is None or q.lo < best else best
    near_q_lower[m] = best
    assert best > BETA[m]

near_lower = Fraction(0)
for m in range(1, 8):
    c_m = Fraction(comb(2 * m, m), m)
    near_lower += c_m * Fraction(100, 1281) ** m * BETA[m]

# Compare exactly with 2/(15*sqrt(15)) by squaring.
assert near_lower > 0
assert near_lower * near_lower > Fraction(4, 3375)


# ---------------------------------------------------------------------------
# C. Corrected far-tail endpoint series bound.
# ---------------------------------------------------------------------------
# For d>=21/10, y=4/d^2 <= y0=400/441.
# We need
#   sum_{m>=8} y^m/m^2 < (1/15) y^8.
# Equivalently at the endpoint,
#   sum_{k>=0} y0^k/(k+8)^2 < 1/15.
# We bound k=0,...,14 exactly and the remainder geometrically using
# 1/(k+8)^2 <= 1/23^2 for k>=15.

y0 = Fraction(400, 441)
series_head = Fraction(0)
for k in range(15):
    series_head += y0 ** k * Fraction(1, (k + 8) ** 2)
series_tail = y0 ** 15 * Fraction(1, 23 ** 2) * Fraction(1, 1 - y0)
series_bound = series_head + series_tail
assert series_bound < Fraction(1, 15)


# ---------------------------------------------------------------------------
# D. Far-range endpoint comparison, d>=21/10.
# ---------------------------------------------------------------------------
# The audited proof gives
#   E_1 >= 4*(mu/(mu^2-1))^4
# and
#   tail_{m>=8} > - sqrt(d)/60*sqrt(8/15)*(4/d^2)^8.
# The ratio is increasing in d, so it suffices to check d=21/10.

d0 = Fraction(21, 10)
mu0 = d0 + 2

q1_lower_sq = Fraction(16) * (mu0 / (mu0 * mu0 - 1)) ** 8

tail_upper_sq = (
    Fraction(4 ** 16, 3600)
    * Fraction(8, 15)
    * d0 ** (-31)
)

assert q1_lower_sq > tail_upper_sq


# ---------------------------------------------------------------------------
# E. Auxiliary rational checks used in the far proof.
# ---------------------------------------------------------------------------
# For nu<=1/14, the positive part of
# P(nu)=positive_part - 5 nu - 1
# is <1, hence P(nu)<0.

nu0 = Fraction(1, 14)
positive_part = (
    2 * nu0 ** 8
    + 7 * nu0 ** 7
    + 15 * nu0 ** 6
    + 21 * nu0 ** 5
    + 25 * nu0 ** 4
    + 16 * nu0 ** 3
    + nu0 ** 2
)
assert positive_part < 1


if __name__ == "__main__":
    print("Universal first-harmonic dominance audited exact certificate")
    print()
    print("Global H_m lower bounds on y in [0,1/6], m=2..7:")
    for m in range(2, 8):
        print(f"  m={m}: > {float(global_h_lower[m]):.12g}")
    print()
    print("Near-boundary certified Q_m lower bounds on y in [1/7,1/6]:")
    for m in range(1, 8):
        print(
            f"  m={m}: interval lower > {float(near_q_lower[m]):.12g}; "
            f"used beta={float(BETA[m]):.12g}"
        )
    print()
    print("near_lower =", float(near_lower))
    print("2/(15*sqrt(15)) approximately 0.034426518633")
    print("near squared margin =", float(near_lower * near_lower - Fraction(4, 3375)))
    print()
    print("far endpoint normalized series bound =", float(series_bound))
    print("1/15 =", float(Fraction(1, 15)))
    print("far endpoint squared ratio =", float(q1_lower_sq / tail_upper_sq))
