#!/usr/bin/env python3
"""Exact finite certificate for the A5 Cayley-diameter input used in the
uniform boundary spectral-gap theorem.

No floating-point arithmetic is used.
"""

from collections import Counter, deque
from itertools import permutations

N = 5
ID = tuple(range(N))


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def inverse(p):
    out = [0] * N
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def parity(p):
    return sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N)) % 2


G = [p for p in permutations(range(N)) if parity(p) == 0]
assert len(G) == 60
INV = {g: inverse(g) for g in G}


def conjugate(h, g):
    return compose(compose(h, g), INV[h])


def subgroup_generated(a, b):
    seen = {ID}
    todo = deque([ID])
    gens = (a, b, INV[a], INV[b])
    while todo:
        x = todo.popleft()
        for g in gens:
            y = compose(x, g)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def cayley_distance_distribution(a, b):
    dist = {ID: 0}
    todo = deque([ID])
    gens = (a, b, INV[a], INV[b])
    while todo:
        x = todo.popleft()
        for g in gens:
            y = compose(x, g)
            if y not in dist:
                dist[y] = dist[x] + 1
                todo.append(y)
    assert len(dist) == 60
    return Counter(dist.values())


# Complete ordered generating-pair list.
generating_pairs = []
for a in G:
    for b in G:
        if len(subgroup_generated(a, b)) == 60:
            generating_pairs.append((a, b))
assert len(generating_pairs) == 2280

# Simultaneous-conjugacy representatives.
unseen = set(generating_pairs)
reps = []
while unseen:
    a, b = next(iter(unseen))
    orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
    assert len(orbit) == 60
    reps.append((a, b))
    unseen -= orbit
assert len(reps) == 38

# Diameter is invariant under simultaneous conjugacy.
diameters = []
distributions = []
for a, b in reps:
    counts = cayley_distance_distribution(a, b)
    distributions.append(counts)
    diameters.append(max(counts))

assert Counter(diameters) == Counter({6: 22, 8: 8, 9: 4, 10: 4})
assert max(diameters) == 10

# Exact rational simplification used in the theorem:
# 1/sqrt(3) < 7/12 because 1/3 < 49/144.
assert 48 < 49
# Hence (1-1/sqrt(3))/50 > (1-7/12)/50 = 1/120.

if __name__ == "__main__":
    print("HATTER-SOL-16 exact A5 Cayley-diameter certificate")
    print("ordered generating pairs =", len(generating_pairs))
    print("simultaneous-conjugacy orbits =", len(reps))
    print("diameter histogram =", dict(sorted(Counter(diameters).items())))
    print("maximum diameter =", max(diameters))
    print("rational spectral-gap corollary: delta > 1/120")
    print("PASS: all exact assertions succeeded")
