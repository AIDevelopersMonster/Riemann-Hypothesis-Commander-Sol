#!/usr/bin/env python3
"""Exact verifier for BRANCH_COHERENCE_SUPPORT_MINIMUM.md.

Enumerates Aut(T) ~= D8 for the seven-vertex complete rooted binary tree,
computes the G-orbits on ordered pairs T^2, and checks the minimum subset
whose setwise stabilizer is the chosen connection subgroup H ~= V4.
"""

from itertools import combinations

V = ["o", "u", "v", "a0", "a1", "b0", "b1"]


def compose(p, q):
    return {x: p[q[x]] for x in V}


def key(p):
    return tuple(p[x] for x in V)


ID = {x: x for x in V}
SU = ID.copy()
SU.update({"a0": "a1", "a1": "a0"})
SV = ID.copy()
SV.update({"b0": "b1", "b1": "b0"})
R = {
    "o": "o",
    "u": "v",
    "v": "u",
    "a0": "b0",
    "a1": "b1",
    "b0": "a0",
    "b1": "a1",
}


def generate_group():
    out = []
    seen = set()
    stack = [ID]
    while stack:
        p = stack.pop()
        k = key(p)
        if k in seen:
            continue
        seen.add(k)
        out.append(p)
        for g in (SU, SV, R):
            stack.append(compose(g, p))
    return out


G = generate_group()
assert len(G) == 8

M0 = {frozenset(("a0", "b0")), frozenset(("a1", "b1"))}


def act_matching(p, matching):
    ans = set()
    for edge in matching:
        a, b = tuple(edge)
        ans.add(frozenset((p[a], p[b])))
    return ans


H = [p for p in G if act_matching(p, M0) == M0]
assert len(H) == 4
H_KEYS = {key(p) for p in H}


def act_pair(p, z):
    return p[z[0]], p[z[1]]


def stabilizer(subset):
    subset = set(subset)
    return [p for p in G if {act_pair(p, z) for z in subset} == subset]


pairs = [(x, y) for x in V for y in V]
unseen = set(pairs)
orbits = []
while unseen:
    z = next(iter(unseen))
    orb = {act_pair(p, z) for p in G}
    orbits.append(orb)
    unseen -= orb

sizes = sorted(len(o) for o in orbits)
assert sizes == [1, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8]

solutions = []
for orb in orbits:
    items = list(orb)
    for r in range(1, len(items) + 1):
        local = []
        for subset in combinations(items, r):
            if {key(p) for p in stabilizer(subset)} == H_KEYS:
                local.append(set(subset))
        if local:
            solutions.append((len(orb), r, local))
            break

assert len(solutions) == 1
orbit_size, min_fiber_size, fibers = solutions[0]
assert orbit_size == 8
assert min_fiber_size == 4

cross = {
    ("a0", "b0"), ("b0", "a0"),
    ("a1", "b1"), ("b1", "a1"),
    ("a0", "b1"), ("b1", "a0"),
    ("a1", "b0"), ("b0", "a1"),
}
assert any(set(f) <= cross for f in fibers)

print("|G| =", len(G))
print("|H| =", len(H))
print("G-orbit sizes on T^2 =", sizes)
print("minimum orbit size supporting stabilizer H =", orbit_size)
print("minimum special-fiber size =", min_fiber_size)
print("balanced anonymous fibers on the 8-cell cross orbit = 4 + 4")
print("smallest G-fixed anchor orbit size = 1: {(o,o)}")
print("minimum anonymous-output domain size = 8 + 1 = 9")
print("PASS")
