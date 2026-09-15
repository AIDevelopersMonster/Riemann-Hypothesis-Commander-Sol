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
        candidates = [
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        ]
        return I(min(candidates), max(candidates))

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


def cos_pi(num, den, order=28):
    """Rigorous interval for cos(pi*num/den).

    The angle is reduced exactly to [0, pi]. We evaluate the Taylor
    polynomial at an interval for the angle and add a rigorous Lagrange
    remainder bound |R| <= x^(2N+2)/(2N+2)!.
    """

    q = Fraction(num, den)

    # Reduce q modulo 2 to [0,2), then use cos((2-r)pi)=cos(r pi).
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


P = 23
M = 11

# Generator [2] of F_23^*/{+-1}.
powers = []
x = 1
for _ in range(M):
    powers.append(min(x, P - x))
    x = (2 * x) % P

# Signless residue r_j corresponding to mirror angle j*pi/23:
# 2*r_j == +-j (mod 23).
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

assert powers == [1, 2, 4, 8, 7, 9, 5, 10, 3, 6, 11]
assert angle_reps == [11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert placement == [2, 4, 8, 7, 9, 5, 10, 3, 6, 11, 1]


def real_chi(q, r):
    e = (q * logs[r]) % M
    return cos_pi(2 * e, M)


x_intervals = [cos_pi(r, P) ** 2 for r in range(1, M + 1)]


# ---------------------------------------------------------------------------
# A. Order-only Abel certificates for q=1,3,4.
# ---------------------------------------------------------------------------
# We certify that a fixed real projection of every proper cumulative sum
# D_k=sum_{r<=k} d_r is positive. Since the total coefficient sum is zero,
# Abel summation then gives a nonzero projected Fourier coefficient for every
# strictly increasing profile b_1<...<b_11.

projection_phases = {
    1: Fraction(1, 6),      # +30 degrees
    3: Fraction(-2, 11),    # -2*pi/11
    4: Fraction(-13, 22),   # -13*pi/22
}

order_certificate = {}
for q, phi in projection_phases.items():
    cumulative = I(0)
    lows = []
    for r in range(1, M):
        angle = Fraction(2 * q * pos[r], M) - phi
        cumulative = cumulative + cos_pi(angle.numerator, angle.denominator)
        lows.append(cumulative.lo)
    order_certificate[q] = lows
    assert min(lows) > 0


# ---------------------------------------------------------------------------
# B. q=2 moment certificate.
# ---------------------------------------------------------------------------
# For w_r=Re chi_2(r), let c_r=w_r*x_r and C_k=sum_{r<=k} c_r.
# Every C_k is positive. Therefore for every j>=1,
#   sum w_r*x_r^j = sum c_r*x_r^(j-1) > 0
# by Abel summation because x_r^(j-1) is decreasing.

q2_cumulative = []
cumulative = I(0)
for r in range(1, M + 1):
    cumulative = cumulative + real_chi(2, r) * x_intervals[r - 1]
    q2_cumulative.append(cumulative.lo)
assert min(q2_cumulative) > 0


# ---------------------------------------------------------------------------
# C. q=5 moment certificate.
# ---------------------------------------------------------------------------
# For j>=6 we factor x_r^j=(x_r^6)*x_r^(j-6). The cumulative sums of
# Re chi_5(r)*x_r^6 are all positive, hence Abel summation gives positivity
# for every j>=6. The finitely many j=1,...,5 are checked directly.

q5_power6_cumulative = []
cumulative = I(0)
for r in range(1, M + 1):
    cumulative = cumulative + real_chi(5, r) * (x_intervals[r - 1] ** 6)
    q5_power6_cumulative.append(cumulative.lo)
assert min(q5_power6_cumulative) > 0

q5_small_moments = []
for j in range(1, 6):
    total = I(0)
    for r in range(1, M + 1):
        total = total + real_chi(5, r) * (x_intervals[r - 1] ** j)
    q5_small_moments.append(total)
    assert total.lo > 0


if __name__ == "__main__":
    print("p=23 exact rational interval certificate")
    print("powers:", powers)
    print("angle_reps:", angle_reps)
    print("placement:", placement)
    print()

    for q in (1, 3, 4):
        vals = [float(v) for v in order_certificate[q]]
        print(f"q={q} order-projection lower bounds:")
        print(" ", [round(v, 9) for v in vals])
        print("  min =", min(vals))
        print()

    vals = [float(v) for v in q2_cumulative]
    print("q=2 cumulative lower bounds for Re(chi_2(r))*x_r:")
    print(" ", [round(v, 9) for v in vals])
    print("  min =", min(vals))
    print()

    vals = [float(v) for v in q5_power6_cumulative]
    print("q=5 cumulative lower bounds for Re(chi_5(r))*x_r^6:")
    print(" ", [round(v, 9) for v in vals])
    print("  min =", min(vals))
    print()

    print("q=5 direct moment intervals j=1..5:")
    for j, interval in enumerate(q5_small_moments, start=1):
        print(f"  j={j}: {interval}")
