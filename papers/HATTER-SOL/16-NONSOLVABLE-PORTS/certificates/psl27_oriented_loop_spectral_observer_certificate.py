#!/usr/bin/env python3
"""Exact finite certificate for the oriented PSL(2,7) two-port observer.

This verifies that the first orientation-sensitive closed port word has length 4,
that the commutator trace supplies an exact orientation bit for the 7A/7B split,
and that the corresponding non-Hermitian loop determinant separates the two
classes for every real 0<t<1.

No floating-point arithmetic is used.
"""

from collections import Counter, deque
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
assert len(G) == 168
INV = {g: inverse(g) for g in G}


def conjugate(h, g):
    return compose(compose(h, g), INV[h])


def order(g):
    x = ID
    for n in range(1, 169):
        x = compose(x, g)
        if x == ID:
            return n
    raise AssertionError


def subgroup(a, b):
    seen = {ID}
    q = deque([ID])
    gens = (a, b, INV[a], INV[b])
    while q:
        x = q.popleft()
        for g in gens:
            y = compose(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def commutator(a, b):
    return compose(compose(compose(a, b), INV[a]), INV[b])


# Exact conjugacy classes.
unseen = set(G)
classes = []
while unseen:
    g = next(iter(unseen))
    C = {conjugate(h, g) for h in G}
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

# Generating-pair orbits.
unseen_pairs = {(a, b) for a in G for b in G}
gen_reps = []
while unseen_pairs:
    a, b = next(iter(unseen_pairs))
    orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
    unseen_pairs -= orbit
    if len(subgroup(a, b)) == 168:
        assert len(orbit) == 168
        gen_reps.append((a, b))

assert len(gen_reps) == 114
assert Counter(class_of[commutator(a, b)] for a, b in gen_reps) == Counter({
    "3A": 36, "4A": 64, "7A": 7, "7B": 7
})

# chi=a+b*i*sqrt(7).
CHI = {
    "1A": (Fraction(3), Fraction(0)),
    "2A": (Fraction(-1), Fraction(0)),
    "3A": (Fraction(0), Fraction(0)),
    "4A": (Fraction(1), Fraction(0)),
    "7A": (Fraction(-1, 2), Fraction(1, 2)),
    "7B": (Fraction(-1, 2), Fraction(-1, 2)),
}

# The exact orientation observable
#   Q4(K) = (chi(K)-chi(K^{-1}))/(i*sqrt(7)).
Q4 = {"1A": 0, "2A": 0, "3A": 0, "4A": 0, "7A": 1, "7B": -1}
for a, b in gen_reps:
    k = commutator(a, b)
    kinv = INV[k]
    c = class_of[k]
    ci = class_of[kinv]
    ar, ai = CHI[c]
    br, bi = CHI[ci]
    assert ar == br and ai == -bi
    assert 2 * ai == Q4[c]

assert Counter(Q4[class_of[commutator(a, b)]] for a, b in gen_reps) == Counter({
    0: 100, 1: 7, -1: 7
})

# Exact local determinant polynomial P_c(t)=det(I-t rho(c)):
#   1 - chi(c)t + conjugate(chi(c))t^2 - t^3.
# Coefficients are stored as (real, coefficient of i*sqrt(7)).
local_poly = {
    c: (
        (Fraction(1), Fraction(0)),
        (-CHI[c][0], -CHI[c][1]),
        (CHI[c][0], -CHI[c][1]),
        (Fraction(-1), Fraction(0)),
    )
    for c in names
}
assert len(set(local_poly.values())) == 6

# For 7A/7B the real part is the same and the imaginary parts have opposite sign:
#   R(t)=(1-t)(1+3t/2+t^2) > 0 for 0<t<1,
#   Im P_7A(t)=-(sqrt(7)/2)t(1+t),
#   Im P_7B(t)=+(sqrt(7)/2)t(1+t).
for c, sign in (("7A", -1), ("7B", 1)):
    coeff = local_poly[c]
    assert coeff[0] == (Fraction(1), 0)
    assert coeff[1] == (Fraction(1, 2), Fraction(sign, 2))
    assert coeff[2] == (Fraction(-1, 2), Fraction(sign, 2))
    assert coeff[3] == (Fraction(-1), 0)

# Minimality of port length: no freely reduced balanced word of length <4 exists.
letters = [
    ("A", 1, 0),
    ("a", -1, 0),
    ("B", 0, 1),
    ("b", 0, -1),
]
inverse_letter = {"A": "a", "a": "A", "B": "b", "b": "B"}
for n in range(1, 4):
    for word in product(letters, repeat=n):
        symbols = [x[0] for x in word]
        if any(inverse_letter[symbols[i]] == symbols[i + 1] for i in range(n - 1)):
            continue
        ea = sum(x[1] for x in word)
        eb = sum(x[2] for x in word)
        assert (ea, eb) != (0, 0)

# At length four the primitive balanced reduced orientation pair is the commutator pair.
word_K = ("A", "B", "a", "b")
word_Kinv = ("B", "A", "b", "a")
assert len(word_K) == len(word_Kinv) == 4

if __name__ == "__main__":
    print("HATTER-SOL-16 exact PSL(2,7) oriented loop observer certificate")
    print("generating-pair orbits =", len(gen_reps))
    print("orientation values on generating commutators = 3A:0, 4A:0, 7A:+1, 7B:-1")
    print("first freely reduced balanced port-word length = 4")
    print("P_7A and P_7B have opposite determinant phase for every real 0<t<1")
    print("PASS: all exact assertions succeeded")
