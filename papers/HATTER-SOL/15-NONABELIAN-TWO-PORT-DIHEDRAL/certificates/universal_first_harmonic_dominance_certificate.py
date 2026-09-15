from fractions import Fraction
from math import comb

# HATTER-SOL-15
# Exact finite certificate used in the universal first-harmonic dominance proof.
# No floating-point arithmetic is used in any assertion.


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
    """Exact interval Horner evaluation; coeffs are ascending in degree."""
    out = I(coeffs[-1])
    for c in reversed(coeffs[:-1]):
        out = out * interval + c
    return out


# For x=mu/sqrt(mu^2-4), y=x-1, the low-m contribution factor is
#
#   Q_m(x) = y * H_m(y),
#
# with q_m = c_m * s^(-2m) * Q_m(x),
# c_m = binom(2m,m)/m.
#
# For m=1, H_1(y)=(2-y)/(2+y).
# For m=2,...,7 the following integer polynomials are the numerators
# of H_m; denominators are listed separately.

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
# For mu>=4, x=mu/sqrt(mu^2-4) lies in (1, 2/sqrt(3)] and therefore
# y=x-1 lies in [0,1/6].  We certify H_m(y)>0 on the larger rational
# interval [0,1/6].  Hence Q_m(x)>=0 for m=1,...,7.

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
# Put d=mu-2.  On 2<=d<=21/10 one has
#   8/7 <= x <= 7/6,
# hence 1/7 <= y <= 1/6.
# We certify simple rational lower bounds beta_m <= Q_m(x).

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

# Also s^2=d(d+4)<= (21/10)(61/10)=1281/100.
# Therefore q_m >= c_m*(100/1281)^m*beta_m.
near_lower = Fraction(0)
for m in range(1, 8):
    c_m = Fraction(comb(2 * m, m), m)
    near_lower += c_m * Fraction(100, 1281) ** m * BETA[m]

# The analytic tail estimate in the proof is
#   tail_{m>=8} < 2/(15*sqrt(15)).
# We compare exactly by squaring.
assert near_lower > 0
assert near_lower * near_lower > Fraction(4, 3375)


# ---------------------------------------------------------------------------
# C. Far-range endpoint check, d>=21/10.
# ---------------------------------------------------------------------------
# The proof gives
#   q_1 >= 4*(mu/(mu^2-1))^4,
# while the negative m>=8 tail is bounded by
#   T_*(d) = sqrt(d)/30 * sqrt(8/15) * (4/d^2)^8.
# The ratio q_1/T_* is proved analytically to be increasing in d.
# It therefore suffices to certify the endpoint d=21/10 exactly.

d0 = Fraction(21, 10)
mu0 = d0 + 2

q1_lower_sq = Fraction(16) * (mu0 / (mu0 * mu0 - 1)) ** 8

tail_upper_sq = (
    Fraction(4 ** 16, 900)
    * Fraction(8, 15)
    * d0 ** (-31)
)

assert q1_lower_sq > tail_upper_sq


if __name__ == "__main__":
    print("Universal first-harmonic dominance exact finite certificate")
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
    print("far endpoint squared ratio =", float(q1_lower_sq / tail_upper_sq))
