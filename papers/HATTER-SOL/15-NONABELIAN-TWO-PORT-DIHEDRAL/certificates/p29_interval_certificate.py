from fractions import Fraction
from math import factorial

# Exact rational bounds:
#   103993/33102 < pi < 104348/33215.
PI_LO = Fraction(103993, 33102)
PI_HI = Fraction(104348, 33215)


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

    def __pow__(self, n):
        if n == 0:
            return I(1)
        if self.lo >= 0:
            return I(self.lo**n, self.hi**n)
        out = I(1)
        for _ in range(n):
            out = out * self
        return out

    def widen(self, eps):
        eps = Fraction(eps)
        return I(self.lo - eps, self.hi + eps)

    def __repr__(self):
        return f"[{float(self.lo):.12g}, {float(self.hi):.12g}]"


def cos_pi(num, den, order=32):
    """Rigorous rational interval for cos(pi*num/den)."""

    q = Fraction(num, den)

    # Reduce q modulo 2 and then use cos((2-r)pi)=cos(r*pi).
    k = q.numerator // (2 * q.denominator)
    r = q - 2 * k
    while r < 0:
        r += 2
    while r >= 2:
        r -= 2
    if r > 1:
        r = 2 - r

    x = I(r * PI_LO, r * PI_HI)
    s = I(0)
    for n in range(order + 1):
        term = (x ** (2 * n)) * Fraction(1, factorial(2 * n))
        s = s + term if n % 2 == 0 else s - term

    rem = x.hi ** (2 * order + 2) * Fraction(1, factorial(2 * order + 2))
    return s.widen(rem)


P = 29
M = 14

# Generator [2] of F_29^*/{+-1}.
powers = []
x = 1
for _ in range(M):
    powers.append(min(x, P - x))
    x = (2 * x) % P

# Signless residue r_j corresponding to mirror angle j*pi/29:
# 2*r_j == +-j (mod 29).
angle_reps = []
for j in range(1, M + 1):
    for r in range(1, M + 1):
        if min((2 * r) % P, P - ((2 * r) % P)) == j:
            angle_reps.append(r)
            break

rep_to_b = {r: j + 1 for j, r in enumerate(angle_reps)}
placement = [rep_to_b[r] for r in powers]
pos = {b_index: j for j, b_index in enumerate(placement)}
logs = {r: j for j, r in enumerate(powers)}

assert powers == [1, 2, 4, 8, 13, 3, 6, 12, 5, 10, 9, 11, 7, 14]
assert angle_reps == [14, 1, 13, 2, 12, 3, 11, 4, 10, 5, 9, 6, 8, 7]
assert placement == [2, 4, 8, 13, 3, 6, 12, 5, 10, 9, 11, 7, 14, 1]


def projected_character(q, r, phi):
    """Re(exp(-i*pi*phi) * chi_q(r)), with chi_q([2])=exp(2*pi*i*q/M)."""
    e = (q * logs[r]) % M
    angle = Fraction(2 * e, M) - phi
    return cos_pi(angle.numerator, angle.denominator)


x_intervals = [cos_pi(r, P) ** 2 for r in range(1, M + 1)]


# ---------------------------------------------------------------------------
# A. Order-only Abel certificates for q=2,3,5,6.
# ---------------------------------------------------------------------------
# If every proper cumulative coefficient sum has positive projection, then
# Abel summation excludes a zero Fourier coefficient for every strictly
# increasing response profile.

order_phases = {
    2: Fraction(0, 1),       # 0 degrees
    3: Fraction(0, 1),       # 0 degrees
    5: Fraction(4, 3),       # 240 degrees
    6: Fraction(-1, 2),      # -90 degrees
}

order_certificate = {}
for q, phi in order_phases.items():
    cumulative = I(0)
    lows = []
    for r in range(1, M):
        angle = Fraction(2 * q * pos[r], M) - phi
        cumulative = cumulative + cos_pi(angle.numerator, angle.denominator)
        lows.append(cumulative.lo)
    order_certificate[q] = lows
    assert min(lows) > 0


# ---------------------------------------------------------------------------
# B. Shifted positive-moment certificates.
# ---------------------------------------------------------------------------
# Let x_r=cos^2(pi*r/29). If the cumulative sums of
#   Re(exp(-i*pi*phi) chi_q(r)) * x_r^h
# are all positive, then Abel summation gives the same positive projection
# for every moment exponent j>=h.

moment_specs = {
    1: (1, Fraction(0, 1)),   # all j>=1
    4: (1, Fraction(2, 5)),   # projection phase 72 degrees; all j>=1
    7: (12, Fraction(0, 1)),  # all j>=12
}

moment_cumulative = {}
for q, (h, phi) in moment_specs.items():
    cumulative = I(0)
    lows = []
    for r in range(1, M + 1):
        term = projected_character(q, r, phi) * (x_intervals[r - 1] ** h)
        cumulative = cumulative + term
        lows.append(cumulative.lo)
    moment_cumulative[q] = lows
    assert min(lows) > 0


# ---------------------------------------------------------------------------
# C. Finite moments for the quadratic q=7 channel.
# ---------------------------------------------------------------------------
# The shifted certificate above handles j>=12. We certify j=1,...,11
# directly in the real q=7 character direction.

q7_small_moments = []
for j in range(1, 12):
    total = I(0)
    for r in range(1, M + 1):
        total = total + projected_character(7, r, Fraction(0, 1)) * (x_intervals[r - 1] ** j)
    q7_small_moments.append(total)
    assert total.lo > 0


if __name__ == "__main__":
    print("p=29 exact rational interval certificate")
    print("powers:", powers)
    print("angle_reps:", angle_reps)
    print("placement:", placement)
    print()

    for q in (2, 3, 5, 6):
        vals = [float(v) for v in order_certificate[q]]
        print(f"q={q} order-projection lower bounds:")
        print(" ", [round(v, 9) for v in vals])
        print("  min =", min(vals))
        print()

    for q in (1, 4, 7):
        h, phi = moment_specs[q]
        vals = [float(v) for v in moment_cumulative[q]]
        print(f"q={q} shifted moment cumulative lower bounds (h={h}, phi={phi}*pi):")
        print(" ", [round(v, 9) for v in vals])
        print("  min =", min(vals))
        print()

    print("q=7 direct moment intervals j=1..11:")
    for j, interval in enumerate(q7_small_moments, start=1):
        print(f"  j={j}: {interval}")
