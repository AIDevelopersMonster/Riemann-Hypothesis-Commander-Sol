#!/usr/bin/env python3
"""Exhaustive small verifier for the QGE3 sparse ternary no-go witness.

Checks:
1. No surjective q=3 counterexample exists with |G|=3 and |D|<=3.
2. A connected counterexample exists at |G|=3, |D|=4.
3. Reports the first connected non-vacuous-Q counterexample on |G|=3.

No external packages are required.
"""

from itertools import combinations, permutations, product


def cells(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def act(g, p):
    return (g[p[0]], g[p[1]])


def preserves_domain(g, D):
    return {act(g, p) for p in D} == set(D)


def comp_adj(p, q):
    return p[1] == q[0] or q[1] == p[0]


def components(D):
    D = list(D)
    seen = set()
    out = []
    for p in D:
        if p in seen:
            continue
        stack = [p]
        seen.add(p)
        C = []
        while stack:
            x = stack.pop()
            C.append(x)
            for y in D:
                if y not in seen and comp_adj(x, y):
                    seen.add(y)
                    stack.append(y)
        out.append(C)
    return out


def q_relation(n, D, c):
    D = set(D)
    Q = set()
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if (x, y) in D and (y, z) in D and c[(x, y)] == c[(y, z)]:
                    Q.add((x, y, z))
    return Q


def preserves_T(n, g, D, c):
    if not preserves_domain(g, D):
        return False
    Q = q_relation(n, D, c)
    for t in product(range(n), repeat=3):
        gt = tuple(g[v] for v in t)
        if (t in Q) != (gt in Q):
            return False
    return True


def anonymous_phase_exists(g, D, c):
    fwd = {}
    rev = {}
    for p in D:
        a = c[p]
        b = c[act(g, p)]
        if a in fwd and fwd[a] != b:
            return False
        if b in rev and rev[b] != a:
            return False
        fwd[a] = b
        rev[b] = a
    return True


def first_counterexample(n, m, require_connected=True, require_nonempty_Q=False):
    for D in combinations(cells(n), m):
        if require_connected and len(components(D)) != 1:
            continue
        Dset = set(D)
        for g in permutations(range(n)):
            if g == tuple(range(n)):
                continue
            if {act(g, p) for p in D} != Dset:
                continue
            for values in product(range(3), repeat=m):
                if set(values) != {0, 1, 2}:
                    continue
                c = dict(zip(D, values))
                if require_nonempty_Q and not q_relation(n, D, c):
                    continue
                if preserves_T(n, g, D, c) and not anonymous_phase_exists(g, D, c):
                    return D, c, g, q_relation(n, D, c)
    return None


def main():
    n = 3
    print("QGE3 exhaustive verifier: n=3, q=3")

    for m in (3,):
        hit = first_counterexample(n, m)
        print(f"connected counterexample at |D|={m}: {hit is not None}")
        assert hit is None

    hit4 = first_counterexample(n, 4)
    assert hit4 is not None
    D, c, g, Q = hit4
    print("first connected |D|=4 counterexample:")
    print("D =", D)
    print("c =", c)
    print("g =", g)
    print("Q =", Q)

    nonvacuous = None
    for m in range(3, 7):
        nonvacuous = first_counterexample(n, m, require_nonempty_Q=True)
        if nonvacuous is not None:
            print(f"first connected non-vacuous-Q counterexample occurs at |D|={m}")
            D, c, g, Q = nonvacuous
            print("D =", D)
            print("c =", c)
            print("g =", g)
            print("Q =", Q)
            break
    assert nonvacuous is not None


if __name__ == "__main__":
    main()
