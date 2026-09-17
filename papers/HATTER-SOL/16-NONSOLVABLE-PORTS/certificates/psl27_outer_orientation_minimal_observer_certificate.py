#!/usr/bin/env python3
"""Exact finite certificate for the PSL(2,7) orientation obstruction.

The certificate verifies:
- the PGL outer involution on conjugacy classes;
- the 3D character transforms by complex conjugation;
- the 3D Artin local polynomial separates all six classes;
- a single calibrated real oriented scalar separates all six classes;
- among irreducible character rows, only the two conjugate 3D rows are
  individually class-separating.

All arithmetic is exact over Q(i*sqrt(7)); no floating point is used.
"""

from collections import Counter
from fractions import Fraction
from itertools import product

P = 7
N = 8
INF = 7
ID = tuple(range(N))


def invmod(a):
    return pow(a, P - 2, P)


def mobius_perm(a, b, c, d):
    out = []
    for x in range(P):
        den = (c * x + d) % P
        num = (a * x + b) % P
        out.append(INF if den == 0 else (num * invmod(den)) % P)
    out.append(INF if c % P == 0 else (a * invmod(c)) % P)
    return tuple(out)


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def inverse(p):
    out = [0] * N
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


G = set()
for a, b, c, d in product(range(P), repeat=4):
    if (a * d - b * c) % P == 1:
        G.add(mobius_perm(a, b, c, d))
G = list(G)
GSET = set(G)
assert len(G) == 168
INV = {g: inverse(g) for g in G}


def conjugate(h, g):
    return compose(compose(h, g), inverse(h))


def order(g):
    x = ID
    for n in range(1, 169):
        x = compose(x, g)
        if x == ID:
            return n
    raise AssertionError


# Exact conjugacy classes of PSL(2,7).
unseen = set(G)
classes = []
while unseen:
    g = next(iter(unseen))
    C = {compose(compose(h, g), INV[h]) for h in G}
    classes.append(C)
    unseen -= C
classes.sort(key=lambda C: (order(next(iter(C))), min(C)))
assert [(order(next(iter(C))), len(C)) for C in classes] == [
    (1, 1), (2, 21), (3, 56), (4, 42), (7, 24), (7, 24)
]

names = ["1A", "2A", "3A", "4A", "7A", "7B"]
class_of = {}
for name, C in zip(names, classes):
    for g in C:
        class_of[g] = name

# Nontrivial PGL element represented by diag(3,1); det=3 is a nonsquare mod 7.
# Its projective action normalizes PSL(2,7) but is not itself in PSL(2,7).
h = mobius_perm(3, 0, 0, 1)
hinv = inverse(h)
assert h not in GSET


def alpha(g):
    return compose(compose(h, g), hinv)


assert all(alpha(g) in GSET for g in G)
assert all(alpha(compose(g, k)) == compose(alpha(g), alpha(k)) for g in G for k in G)

class_map = {}
for name, C in zip(names, classes):
    image_names = {class_of[alpha(g)] for g in C}
    assert len(image_names) == 1
    class_map[name] = next(iter(image_names))

assert class_map == {
    "1A": "1A",
    "2A": "2A",
    "3A": "3A",
    "4A": "4A",
    "7A": "7B",
    "7B": "7A",
}
# Since an inner automorphism cannot swap conjugacy classes, alpha is outer.

# Elements of Q(i sqrt(7)) are stored as (a,b)=a+b*i*sqrt(7).
Q0 = (Fraction(0), Fraction(0))


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qmul(x, y):
    return (x[0] * y[0] - 7 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qconj(x):
    return (x[0], -x[1])


chi3 = {
    "1A": (Fraction(3), Fraction(0)),
    "2A": (Fraction(-1), Fraction(0)),
    "3A": (Fraction(0), Fraction(0)),
    "4A": (Fraction(1), Fraction(0)),
    "7A": (Fraction(-1, 2), Fraction(1, 2)),
    "7B": (Fraction(-1, 2), Fraction(-1, 2)),
}
assert len(set(chi3.values())) == 6
assert all(chi3[class_map[c]] == qconj(chi3[c]) for c in names)

# Full irreducible character rows.
chi3b = {c: qconj(chi3[c]) for c in names}
rows = {
    "1": [(Fraction(1), Fraction(0))] * 6,
    "3": [chi3[c] for c in names],
    "3bar": [chi3b[c] for c in names],
    "6": [(Fraction(x), Fraction(0)) for x in (6, 2, 0, 0, -1, -1)],
    "7": [(Fraction(x), Fraction(0)) for x in (7, -1, 1, -1, 0, 0)],
    "8": [(Fraction(x), Fraction(0)) for x in (8, 0, -1, 0, 1, 1)],
}
assert [len(set(rows[k])) for k in ("1", "3", "3bar", "6", "7", "8")] == [1, 6, 6, 4, 4, 4]

# Character-table orthogonality.
sizes = [1, 21, 56, 42, 24, 24]
keys = ["1", "3", "3bar", "6", "7", "8"]
for i, ki in enumerate(keys):
    for j, kj in enumerate(keys):
        s = Q0
        for n, x, y in zip(sizes, rows[ki], rows[kj]):
            s = qadd(s, (Fraction(n), Fraction(0)) if False else qmul((Fraction(n), Fraction(0)), qmul(x, qconj(y))))
        target = (Fraction(168 if i == j else 0), Fraction(0))
        assert s == target, (ki, kj, s)

# The 3D local Artin denominator is
# P_c(T)=1-chi(c)T+conj(chi(c))T^2-T^3.
local_polys = {
    c: ((Fraction(1), Fraction(0)),
        (-chi3[c][0], -chi3[c][1]),
        qconj(chi3[c]),
        (Fraction(-1), Fraction(0)))
    for c in names
}
assert len(set(local_polys.values())) == 6

# Canonical I/Q coordinates and one calibrated real oriented scalar.
# I=Re chi, Q=(2/sqrt(7)) Im chi = 2*b for chi=a+b*i*sqrt(7).
IQ = {c: (chi3[c][0], 2 * chi3[c][1]) for c in names}
F = {c: IQ[c][0] + IQ[c][1] for c in names}
assert F == {
    "1A": Fraction(3),
    "2A": Fraction(-1),
    "3A": Fraction(0),
    "4A": Fraction(1),
    "7A": Fraction(1, 2),
    "7B": Fraction(-3, 2),
}
assert len(set(F.values())) == 6

if __name__ == "__main__":
    print("HATTER-SOL-16 exact PSL(2,7) orientation certificate")
    print("outer class map =", class_map)
    print("class-separating irreducible rows = 3, 3bar")
    print("I/Q coordinates =", IQ)
    print("single real oriented scalar F=I+Q =", F)
    print("3D local Artin polynomials are pairwise distinct")
    print("PASS: all exact assertions succeeded")
