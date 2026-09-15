#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from fractions import Fraction

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
for a in range(P):
    for b in range(P):
        for c in range(P):
            for d in range(P):
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


unseen = set(G)
classes = []
while unseen:
    g = next(iter(unseen))
    C = {conjugate(h, g) for h in G}
    classes.append(C)
    unseen -= C
classes.sort(key=lambda C: (order(next(iter(C))), min(C)))

class_of = {}
seven_count = 0
for C in classes:
    o = order(next(iter(C)))
    if o == 1:
        name = "1A"
    elif o == 2:
        name = "2A"
    elif o == 3:
        name = "3A"
    elif o == 4:
        name = "4A"
    elif o == 7:
        seven_count += 1
        name = "7A" if seven_count == 1 else "7B"
    else:
        raise AssertionError(o)
    for g in C:
        class_of[g] = name

assert Counter(class_of.values()) == Counter({
    "1A": 1, "2A": 21, "3A": 56, "4A": 42, "7A": 24, "7B": 24
})

unseen_pairs = {(a, b) for a in G for b in G}
pair_orbit_reps = []
while unseen_pairs:
    a, b = next(iter(unseen_pairs))
    orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
    pair_orbit_reps.append((a, b, len(orbit)))
    unseen_pairs -= orbit

gen_reps = []
for a, b, orbit_size in pair_orbit_reps:
    if len(subgroup(a, b)) == 168:
        assert orbit_size == 168
        gen_reps.append((a, b))

assert len(gen_reps) == 114
assert Counter(class_of[commutator(a, b)] for a, b in gen_reps) == Counter({
    "3A": 36, "4A": 64, "7A": 7, "7B": 7
})
assert 168 * len(gen_reps) == 19152

Q0 = (Fraction(0), Fraction(0))
CHI = {
    "1A": (Fraction(3), Fraction(0)),
    "2A": (Fraction(-1), Fraction(0)),
    "3A": (Fraction(0), Fraction(0)),
    "4A": (Fraction(1), Fraction(0)),
    "7A": (Fraction(-1, 2), Fraction(1, 2)),
    "7B": (Fraction(-1, 2), Fraction(-1, 2)),
}
assert len(set(CHI.values())) == 6


def norm2(v):
    a, b = v
    return a * a + 7 * b * b

sizes = Counter(class_of.values())
assert sum(sizes[c] * norm2(CHI[c]) for c in sizes) == 168
assert sum(sizes[c] * CHI[c][0] for c in sizes) == 0
assert sum(sizes[c] * CHI[c][1] for c in sizes) == 0


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qmul(x, y):
    return (x[0] * y[0] - 7 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qscale(x, s):
    return (x[0] * s, x[1] * s)


def padd(A, B):
    R = dict(A)
    for k, v in B.items():
        R[k] = qadd(R.get(k, Q0), v)
    return {k: v for k, v in R.items() if v != Q0}


def pscale(A, s):
    return {k: qscale(v, s) for k, v in A.items() if qscale(v, s) != Q0}


def pmul(A, B):
    R = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            key = (i + k, j + l)
            R[key] = qadd(R.get(key, Q0), qmul(a, b))
    return {k: v for k, v in R.items() if v != Q0}


def trace_power(a, b, n):
    terms = ((a, (1, 0)), (INV[a], (-1, 0)), (b, (0, 1)), (INV[b], (0, -1)))
    state = {(ID, 0, 0): 1}
    for _ in range(n):
        new = defaultdict(int)
        for (g, e1, e2), count in state.items():
            for h, (d1, d2) in terms:
                new[(compose(g, h), e1 + d1, e2 + d2)] += count
        state = new
    out = {}
    for (g, e1, e2), count in state.items():
        v = qscale(CHI[class_of[g]], Fraction(count))
        out[(e1, e2)] = qadd(out.get((e1, e2), Q0), v)
    return {k: v for k, v in out.items() if v != Q0}


def det_poly(a, b, mu=Fraction(4)):
    t1 = trace_power(a, b, 1)
    t2 = trace_power(a, b, 2)
    t3 = trace_power(a, b, 3)
    D = {(0, 0): (mu ** 3, Fraction(0))}
    D = padd(D, pscale(t1, -mu ** 2))
    D = padd(D, pscale(padd(pmul(t1, t1), pscale(t2, -1)), mu / 2))
    cubic = padd(
        padd(pmul(pmul(t1, t1), t1), pscale(pmul(t1, t2), -3)),
        pscale(t3, 2),
    )
    return padd(D, pscale(cubic, Fraction(-1, 6)))


def poly_key(D, swap, s1, s2):
    out = []
    for (m, n), (a, b) in D.items():
        if swap:
            m, n = n, m
        m *= s1
        n *= s2
        out.append((m, n, a.numerator, a.denominator, b.numerator, b.denominator))
    return tuple(sorted(out))


def canonical_mahler_poly(D):
    return min(
        poly_key(D, swap, s1, s2)
        for swap in (0, 1)
        for s1 in (-1, 1)
        for s2 in (-1, 1)
    )


type_sets = defaultdict(set)
for a, b in gen_reps:
    label = class_of[commutator(a, b)]
    type_sets[label].add(canonical_mahler_poly(det_poly(a, b)))

assert {k: len(v) for k, v in type_sets.items()} == {
    "3A": 6, "4A": 12, "7A": 3, "7B": 3
}
assert type_sets["7A"] == type_sets["7B"]
assert type_sets["3A"].isdisjoint(type_sets["4A"])
assert type_sets["3A"].isdisjoint(type_sets["7A"])
assert type_sets["4A"].isdisjoint(type_sets["7A"])

if __name__ == "__main__":
    print("HATTER-SOL-16 exact PSL(2,7) certificate")
    print("|G| =", len(G))
    print("class sizes =", dict(sorted(sizes.items())))
    print("generating-pair orbits =", len(gen_reps))
    print("ordered generating pairs =", 168 * len(gen_reps))
    print("commutator orbit counts =", dict(sorted(Counter(class_of[commutator(a,b)] for a,b in gen_reps).items())))
    print("Mahler-type counts =", {k: len(v) for k, v in sorted(type_sets.items())})
    print("single 3D character is injective on all six conjugacy classes")
    print("7A and 7B have identical scalar determinant/Mahler type sets")
    print("PASS: exact finite assertions succeeded")
