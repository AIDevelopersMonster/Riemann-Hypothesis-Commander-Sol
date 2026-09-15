#!/usr/bin/env python3
"""Exact HATTER-SOL-16 A5 generating-pair / commutator certificate.

No floating-point arithmetic is used in any assertion.

Conventions:
- permutations are tuples p with p[i] = image of i;
- composition compose(p,q) means p after q;
- [A,B] = A B A^{-1} B^{-1};
- 5A is the A5-conjugacy class of (1 2 3 4 5);
- 5B is the A5-conjugacy class of its square.
"""

from collections import Counter, defaultdict, deque
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
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            count += p[i] > p[j]
    return count % 2


G = [p for p in permutations(range(N)) if parity(p) == 0]
assert len(G) == 60
GSET = set(G)
INV = {g: inverse(g) for g in G}


def conjugate(h, g):
    return compose(compose(h, g), INV[h])


def commutator(a, b):
    return compose(compose(compose(a, b), INV[a]), INV[b])


def subgroup_generated(a, b):
    seen = {ID}
    todo = deque([ID])
    generators = (a, b, INV[a], INV[b])
    while todo:
        x = todo.popleft()
        for g in generators:
            y = compose(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def cycle_lengths(p):
    seen = [False] * N
    lengths = []
    for i in range(N):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


# Fix the split 5-cycle classes canonically.
g5 = (1, 2, 3, 4, 0)  # (1 2 3 4 5)
g5_sq = compose(g5, g5)
C5A = {conjugate(h, g5) for h in G}
C5B = {conjugate(h, g5_sq) for h in G}
assert len(C5A) == len(C5B) == 12
assert C5A.isdisjoint(C5B)


def class_name(g):
    ct = cycle_lengths(g)
    if ct == (1, 1, 1, 1, 1):
        return "1A"
    if ct == (2, 2, 1):
        return "2A"
    if ct == (3, 1, 1):
        return "3A"
    if ct == (5,):
        return "5A" if g in C5A else "5B"
    raise AssertionError(ct)


# Conjugacy-class sizes.
class_sizes = Counter(class_name(g) for g in G)
assert class_sizes == Counter({"1A": 1, "2A": 15, "3A": 20, "5A": 12, "5B": 12})

# Exhaust all ordered pairs and record subgroup order by commutator class.
subgroup_by_comm = defaultdict(Counter)
generating_pairs = []
for a in G:
    for b in G:
        k = commutator(a, b)
        h_size = len(subgroup_generated(a, b))
        subgroup_by_comm[class_name(k)][h_size] += 1
        if h_size == 60:
            generating_pairs.append((a, b))

assert len(generating_pairs) == 2280

assert subgroup_by_comm["1A"] == Counter({1: 1, 2: 45, 3: 80, 4: 30, 5: 144})
assert subgroup_by_comm["2A"] == Counter({12: 480})
assert subgroup_by_comm["3A"] == Counter({6: 180, 60: 1080})
assert subgroup_by_comm["5A"] == Counter({10: 180, 60: 600})
assert subgroup_by_comm["5B"] == Counter({10: 180, 60: 600})

# Thus a generating pair has commutator only in 3A, 5A or 5B.
gen_comm_counts = Counter(class_name(commutator(a, b)) for a, b in generating_pairs)
assert gen_comm_counts == Counter({"3A": 1080, "5A": 600, "5B": 600})

# Simultaneous-conjugacy orbits of generating pairs.
unseen = set(generating_pairs)
orbits = []
while unseen:
    a, b = next(iter(unseen))
    orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
    # A generating pair has common centralizer equal to Z(A5)=1.
    assert len(orbit) == 60
    orbits.append(orbit)
    unseen -= orbit

assert len(orbits) == 38
assert Counter(len(o) for o in orbits) == Counter({60: 38})
orbit_comm_counts = Counter(
    class_name(commutator(*next(iter(orbit)))) for orbit in orbits
)
assert orbit_comm_counts == Counter({"3A": 18, "5A": 10, "5B": 10})

# Character values of one real 3-dimensional irreducible representation:
# chi_3 = (3,-1,0,phi,phi'), phi=(1+sqrt(5))/2, phi'=(1-sqrt(5))/2.
# Encode a+b*sqrt(5) over denominator 2 where convenient.
chi3 = {
    "1A": (6, 0, 2),   # 3
    "2A": (-2, 0, 2),  # -1
    "3A": (0, 0, 2),   # 0
    "5A": (1, 1, 2),   # (1+sqrt5)/2
    "5B": (1, -1, 2),  # (1-sqrt5)/2
}
assert len(set(chi3.values())) == 5

# The smallest trace gap among generating commutator classes is
# delta=(sqrt(5)-1)/2.  The universal fourth-order remainder estimate
# proves pairwise Mahler separation whenever
#   (sqrt(5)-1)(mu^2-16) > 4096.
# Certify that the integer threshold mu=58 satisfies this exactly.
# At mu=58 the inequality is sqrt(5) > 1861/837.
assert 5 * 837 * 837 > 1861 * 1861


if __name__ == "__main__":
    print("HATTER-SOL-16 exact A5 generating-pair certificate")
    print("|A5| =", len(G))
    print("class sizes =", dict(sorted(class_sizes.items())))
    print("ordered generating pairs =", len(generating_pairs))
    print("simultaneous-conjugacy orbits =", len(orbits))
    print("generating commutator pair counts =", dict(sorted(gen_comm_counts.items())))
    print("generating commutator orbit counts =", dict(sorted(orbit_comm_counts.items())))
    print("subgroup orders by commutator class:")
    for name in ("1A", "2A", "3A", "5A", "5B"):
        print(" ", name, dict(sorted(subgroup_by_comm[name].items())))
    print("chi_3 is injective on all five A5 conjugacy classes")
    print("uniform large-mu separation certificate: mu >= 58")
    print("PASS: all exact assertions succeeded")
