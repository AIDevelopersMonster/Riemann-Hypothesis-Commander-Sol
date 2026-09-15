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


def cos_pi(num, den, order=32):
    """Rigorous rational interval for cos(pi*num/den)."""

    q = Fraction(num, den)
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


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p):
    phi = p - 1
    fac = prime_factors(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in fac):
            return g
    raise ValueError("primitive root not found")


def signrep(a, p):
    a %= p
    return min(a, p - a)


def build_world(p):
    m = (p - 1) // 2
    g = primitive_root(p)

    powers = []
    x = 1
    for _ in range(m):
        powers.append(signrep(x, p))
        x = (g * x) % p

    logs = {r: j for j, r in enumerate(powers)}

    angle_reps = []
    for j in range(1, m + 1):
        for r in range(1, m + 1):
            if signrep(2 * r, p) == j:
                angle_reps.append(r)
                break

    rep_to_b = {r: j + 1 for j, r in enumerate(angle_reps)}
    placement = [rep_to_b[r] for r in powers]
    pos = {b: j for j, b in enumerate(placement)}
    x_intervals = [cos_pi(r, p) ** 2 for r in range(1, m + 1)]

    return {
        "p": p,
        "m": m,
        "g": g,
        "powers": powers,
        "logs": logs,
        "angle_reps": angle_reps,
        "placement": placement,
        "pos": pos,
        "x": x_intervals,
    }


def projected_character(world, q, r, phase):
    m = world["m"]
    e = (q * world["logs"][r]) % m
    angle = Fraction(2 * e, m) - phase
    return cos_pi(angle.numerator, angle.denominator)


def certify_order(world, q, phase):
    m = world["m"]
    pos = world["pos"]
    cumulative = I(0)
    lows = []
    for b in range(1, m):
        angle = Fraction(2 * q * pos[b], m) - phase
        cumulative = cumulative + cos_pi(angle.numerator, angle.denominator)
        lows.append(cumulative.lo)
    assert min(lows) > 0
    return min(lows)


def certify_moment(world, q, h, phase):
    m = world["m"]
    xs = world["x"]

    small = []
    for j in range(1, h):
        total = I(0)
        for r in range(1, m + 1):
            total = total + projected_character(world, q, r, phase) * (xs[r - 1] ** j)
        small.append(total.lo)

    cumulative = I(0)
    cumulative_lows = []
    for r in range(1, m + 1):
        cumulative = cumulative + projected_character(world, q, r, phase) * (xs[r - 1] ** h)
        cumulative_lows.append(cumulative.lo)

    assert min(cumulative_lows) > 0
    if small:
        assert min(small) > 0

    return (
        min(small) if small else None,
        min(cumulative_lows),
    )


# Each phase is an exact rational multiple of pi.
# O = order-Abel certificate.
# M = shifted moment-Abel certificate: (M, h, phase).
CERTIFICATES = {
    31: {
        1: ("O", Fraction(2694, 3600)),
        2: ("O", Fraction(7123, 3600)),
        3: ("O", Fraction(720, 3600)),
        4: ("O", Fraction(5922, 3600)),
        5: ("M", 1, Fraction(0, 1)),
        6: ("M", 8, Fraction(6840, 3600)),
        7: ("M", 1, Fraction(1132, 3600)),
    },
    37: {
        1: ("M", 1, Fraction(147, 3600)),
        2: ("O", Fraction(262, 3600)),
        3: ("M", 1, Fraction(941, 3600)),
        4: ("O", Fraction(6443, 3600)),
        5: ("O", Fraction(6958, 3600)),
        6: ("M", 1, Fraction(6600, 3600)),
        7: ("O", Fraction(5600, 3600)),
        8: ("M", 14, Fraction(1000, 3600)),
        9: ("M", 1, Fraction(0, 1)),
    },
    41: {
        1: ("O", Fraction(4746, 3600)),
        2: ("M", 14, Fraction(6839, 3600)),
        3: ("O", Fraction(6828, 3600)),
        4: ("O", Fraction(0, 1)),
        5: ("M", 1, Fraction(6120, 3600)),
        6: ("M", 1, Fraction(5752, 3600)),
        7: ("M", 1, Fraction(457, 3600)),
        8: ("O", Fraction(4320, 3600)),
        9: ("M", 1, Fraction(5897, 3600)),
        10: ("M", 1, Fraction(0, 1)),
    },
    43: {
        1: ("O", Fraction(6469, 3600)),
        2: ("M", 1, Fraction(228, 3600)),
        3: ("O", Fraction(57, 3600)),
        4: ("O", Fraction(558, 3600)),
        5: ("O", Fraction(5127, 3600)),
        6: ("M", 1, Fraction(761, 3600)),
        7: ("M", 1, Fraction(0, 1)),
        # q=8 intentionally absent: first unresolved channel for these two templates.
        9: ("M", 18, Fraction(6428, 3600)),
        10: ("M", 1, Fraction(6531, 3600)),
    },
}


if __name__ == "__main__":
    print("HATTER-SOL-15 exact automatic certificate range p=31..43")
    print()

    for p in (31, 37, 41, 43):
        world = build_world(p)
        m = world["m"]
        independent = list(range(1, m // 2 + 1))
        unresolved = []

        print(f"p={p}, m={m}, primitive root={world['g']}")

        for q in independent:
            spec = CERTIFICATES[p].get(q)
            if spec is None:
                unresolved.append(q)
                print(f"  q={q}: UNRESOLVED by O/M certificate table")
                continue

            if spec[0] == "O":
                margin = certify_order(world, q, spec[1])
                print(f"  q={q}: O margin > {float(margin):.12g}")
            else:
                small, cumulative = certify_moment(world, q, spec[1], spec[2])
                if small is None:
                    print(
                        f"  q={q}: M h={spec[1]} cumulative margin > "
                        f"{float(cumulative):.12g}"
                    )
                else:
                    print(
                        f"  q={q}: M h={spec[1]} small margin > {float(small):.12g}; "
                        f"cumulative margin > {float(cumulative):.12g}"
                    )

        if p in (31, 37, 41):
            assert not unresolved
        if p == 43:
            assert unresolved == [8]

        print("  unresolved:", unresolved)
        print()
