#!/usr/bin/env python3
"""HATTER-SOL-18 H18-02: exact Nielsen-dynamics certificate on 114 H17 orbits."""

from __future__ import annotations
import importlib.util
from collections import Counter, deque
from pathlib import Path

HERE = Path(__file__).resolve()
H18 = HERE.parents[1]
HATTER = H18.parent
H17_MODEL = HATTER / "17-NONABELIAN-TOMOGRAPHY-HARDWARE" / "tools" / "generate_psl27_golden_model.py"

spec = importlib.util.spec_from_file_location("h17_golden", H17_MODEL)
assert spec is not None and spec.loader is not None
h17 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h17)

G = h17.G
INV = h17.INV
REPS = h17.REPS
REP_ID = {rep: i for i, rep in enumerate(REPS)}

def orbit_id(a, b) -> int:
    rep = min((h17.conjugate(g, a), h17.conjugate(g, b)) for g in G)
    return REP_ID[rep]

def move_permutation(move):
    out = [orbit_id(*move(a, b)) for a, b in REPS]
    assert sorted(out) == list(range(114))
    return tuple(out)

MOVES = {
    "swap": lambda a, b: (b, a),
    "invA": lambda a, b: (INV[a], b),
    "invB": lambda a, b: (a, INV[b]),
    "A_to_AB": lambda a, b: (h17.compose(a, b), b),
    "B_to_BA": lambda a, b: (a, h17.compose(b, a)),
    "A_to_Ab": lambda a, b: (h17.compose(a, INV[b]), b),
}
PERMS = {name: move_permutation(move) for name, move in MOVES.items()}

def cycle_distribution(perm):
    seen = set()
    lengths = Counter()
    for start in range(len(perm)):
        if start in seen:
            continue
        cur = start
        n = 0
        while cur not in seen:
            seen.add(cur)
            n += 1
            cur = perm[cur]
        lengths[n] += 1
    return dict(sorted(lengths.items()))

def build_graph(generator_names):
    adj = [set() for _ in range(114)]
    for name in generator_names:
        perm = PERMS[name]
        for i, j in enumerate(perm):
            adj[i].add(j)
            adj[j].add(i)
    return adj

def connected_components(adj):
    seen = set()
    comps = []
    for start in range(114):
        if start in seen:
            continue
        q = deque([start])
        seen.add(start)
        comp = []
        while q:
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        comps.append(sorted(comp))
    comps.sort(key=lambda c: (-len(c), c[0]))
    return comps

def diameter(adj, comp):
    allowed = set(comp)
    diam = 0
    for start in comp:
        dist = {start: 0}
        q = deque([start])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y in allowed and y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        assert len(dist) == len(comp)
        diam = max(diam, max(dist.values()))
    return diam

def commutator_class(a, b):
    k = h17.compose(h17.compose(h17.compose(a, b), INV[a]), INV[b])
    return h17.CLASS_OF[k]

def main():
    assert len(REPS) == 114
    expected_cycles = {
        "swap": {1: 10, 2: 52},
        "invA": {1: 12, 2: 51},
        "invB": {1: 12, 2: 51},
        "A_to_AB": {2: 5, 3: 10, 4: 8, 7: 6},
        "B_to_BA": {2: 5, 3: 10, 4: 8, 7: 6},
        "A_to_Ab": {2: 5, 3: 10, 4: 8, 7: 6},
    }
    for name, expected in expected_cycles.items():
        got = cycle_distribution(PERMS[name])
        assert got == expected, (name, got, expected)

    generators = ("swap", "invA", "A_to_AB")
    adj = build_graph(generators)
    comps = connected_components(adj)
    sizes = [len(c) for c in comps]
    assert sizes == [36, 32, 32, 14]

    comm = [commutator_class(a, b) for a, b in REPS]
    comp_comm = [dict(Counter(comm[i] for i in c)) for c in comps]
    assert comp_comm[0] == {"3A": 36}
    assert comp_comm[1] == {"4A": 32}
    assert comp_comm[2] == {"4A": 32}
    assert comp_comm[3] == {"7A": 7, "7B": 7}

    diameters = [diameter(adj, c) for c in comps]
    assert diameters == [7, 6, 8, 4]

    print("HATTER-SOL-18 H18-02 Nielsen-dynamics certificate")
    print("canonical orbit states = 114")
    for name in MOVES:
        print(name, "cycle distribution =", cycle_distribution(PERMS[name]))
    print("graph generators =", generators)
    print("connected component sizes =", sizes)
    print("component diameters =", diameters)
    print("component commutator classes =", comp_comm)
    print("PASS: exact Nielsen-move dynamics on the 114 H17 orbits certified")

if __name__ == "__main__":
    main()
