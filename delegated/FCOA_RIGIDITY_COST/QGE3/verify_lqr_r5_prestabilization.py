#!/usr/bin/env python3
"""Independent verifier for the exact r=5 LQR pre-stabilization law.

Checks:
- Bell(5)=52 and cut-space dimensions;
- the 25 defect-two partition planes;
- all 50 compatible four-plane cores and their two S5-orbits (20+30);
- explicit non-diagonal witnesses for representatives of both orbits;
- explicit synchronizing constructions for q=4,...,14 by deterministic
  canonical-color forcing certificates;
- the closed-form r=5 values on the full pre-stabilization sector.

The analytic proof lives in LQR_R5_PRESTABILIZATION.md.
"""

from itertools import combinations, permutations
from math import floor

R = 5


def all_set_partitions(r):
    out = []
    seq = [0]

    def rec(pos, mx):
        if pos == r:
            out.append(tuple(tuple(i for i, x in enumerate(seq) if x == b)
                             for b in range(mx + 1)))
            return
        for b in range(mx + 2):
            seq.append(b)
            rec(pos + 1, max(mx, b))
            seq.pop()

    rec(1, 0)
    return out


def labels(part, r=R):
    out = [None] * r
    for b, block in enumerate(part):
        for x in block:
            out[x] = b
    return tuple(out)


def compatible(p, q, r=R):
    lp, lq = labels(p, r), labels(q, r)
    seen, stack = {0}, [0]
    while stack:
        x = stack.pop()
        for y in range(r):
            if y not in seen and (lp[x] == lp[y] or lq[x] == lq[y]):
                seen.add(y)
                stack.append(y)
    return len(seen) == r


def cut_space(part, r=R):
    out = set()
    for mask in range(1 << (r - 1)):
        bits = (0,) + tuple((mask >> (i - 1)) & 1 for i in range(1, r))
        if all(len({bits[i] for i in block}) == 1 for block in part):
            out.add(mask)
    return frozenset(out)


def canonical_part(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0]))


def parse_part(text):
    return canonical_part(tuple(tuple(int(c) for c in block)
                                for block in text.split('|')))


def fmt_part(part):
    return '|'.join(''.join(map(str, block)) for block in part)


def permute_part(part, sigma):
    return canonical_part(tuple(tuple(sigma[x] for x in block) for block in part))


def quotient_graph(parts, q, r=R):
    labs = [labels(p, r) for p in parts]
    vertices, index = [], {}
    for a in range(q):
        for b in sorted(set(labs[a])):
            index[(a, b)] = len(vertices)
            vertices.append((a, b))
    adj = [set() for _ in vertices]
    trans = []
    for i in range(r):
        vs = [index[(a, labs[a][i])] for a in range(q)]
        trans.append(vs)
        for x, y in combinations(vs, 2):
            adj[x].add(y)
            adj[y].add(x)
    return vertices, adj, trans


def forcing_certificate(parts, q, r=R):
    vertices, adj, trans = quotient_graph(parts, q, r)
    canonical = [a for a, _ in vertices]
    color = [-1] * len(vertices)
    for a, v in enumerate(trans[0]):
        color[v] = a

    certificate = []
    while True:
        progressed = False
        for v in range(len(vertices)):
            if color[v] >= 0:
                continue
            used = {color[u] for u in adj[v] if color[u] >= 0}
            avail = [c for c in range(q) if c not in used]
            if len(avail) == 1:
                color[v] = avail[0]
                certificate.append((vertices[v], avail[0]))
                progressed = True
        if not progressed:
            break

    return color == canonical, certificate


def witness_satisfies(parts, rows):
    q = len(parts)
    assert all(sorted(row) == list(range(q)) for row in rows)
    for a, part in enumerate(parts):
        for block in part:
            vals = {rows[i][a] for i in block}
            if len(vals) != 1:
                return False
    return any(rows[i] != rows[0] for i in range(1, R))


def defect(part):
    return len(part) - 1


def target_defect(q):
    assert q >= 3
    return min(15, q + 3, floor((q + 15) / 2))


PARTS = all_set_partitions(R)
ZERO = next(p for p in PARTS if defect(p) == 0)


def P(text):
    part = parse_part(text)
    assert part in PARTS, text
    return part


CONSTRUCTIONS = {
    4: [P('01|23|4'), P('02|14|3'), P('0|12|34'), P('013|24')],
    5: [P('01|23|4'), P('02|14|3'), P('0|12|34'), P('013|24'), P('024|13')],
    6: [P('01|23|4'), P('02|14|3'), P('0|12|34'), P('013|24'), P('024|13'), P('0134|2')],
    7: [P('01|23|4'), P('02|14|3'), P('0|12|34'), P('013|24'), P('024|13'), P('0134|2'), P('0234|1')],
    8: [P('01|23|4'), P('02|14|3'), P('03|1|24'), P('012|34'), P('024|13'), P('034|12'), P('04|123'), P('0134|2')],
    9: [P('01|23|4'), P('02|14|3'), P('03|1|24'), P('012|34'), P('024|13'), P('034|12'), P('04|123'), P('0134|2'), P('0|1234')],
    10: [P('01|23|4'), P('02|14|3'), P('03|1|24'), P('012|34'), P('024|13'), P('034|12'), P('04|123'), P('0134|2'), P('0|1234'), ZERO],
    11: [P('01|23|4'), P('02|14|3'), P('012|34'), P('013|24'), P('024|13'), P('034|12'), P('03|124'), P('04|123'), P('0134|2'), P('0234|1'), P('0|1234')],
    12: [P('01|23|4'), P('02|14|3'), P('012|34'), P('013|24'), P('024|13'), P('034|12'), P('03|124'), P('04|123'), P('0134|2'), P('0234|1'), P('0|1234'), ZERO],
    13: [P('01|23|4'), P('012|34'), P('013|24'), P('023|14'), P('024|13'), P('02|134'), P('034|12'), P('03|124'), P('04|123'), P('0124|3'), P('0134|2'), P('0234|1'), P('0|1234')],
    14: [P('01|23|4'), P('012|34'), P('013|24'), P('023|14'), P('024|13'), P('02|134'), P('034|12'), P('03|124'), P('04|123'), P('0124|3'), P('0134|2'), P('0234|1'), P('0|1234'), ZERO],
}


def main():
    print('LQR r=5 pre-stabilization verifier')
    print('===================================')

    assert len(PARTS) == 52
    assert all(len(cut_space(p)) == (1 << defect(p)) for p in PARTS)
    print('Bell(5)=52 and cut-space dimensions: PASS')

    planes = [p for p in PARTS if defect(p) == 2]
    assert len(planes) == 25
    four_cliques = []
    for fam in combinations(planes, 4):
        if all(compatible(a, b) for a, b in combinations(fam, 2)):
            four_cliques.append(frozenset(fam))
    assert len(four_cliques) == 50

    s5 = list(permutations(range(R)))
    unseen = set(four_cliques)
    orbits = []
    while unseen:
        fam = next(iter(unseen))
        orb = {
            frozenset(permute_part(p, sigma) for p in fam)
            for sigma in s5
        } & set(four_cliques)
        orbits.append((fam, orb))
        unseen -= orb
    assert sorted(len(orb) for _, orb in orbits) == [20, 30]
    print('25 defect-2 planes; 50 compatible four-cores; S5 orbits 20+30: PASS')

    rep_a = [P('01|23|4'), P('02|14|3'), P('03|1|24'), P('04|13|2')]
    rows_a = [
        (0, 1, 2, 3),
        (0, 2, 3, 1),
        (3, 1, 0, 2),
        (3, 0, 2, 1),
        (1, 2, 0, 3),
    ]
    rep_b = [P('01|24|3'), P('023|1|4'), P('0|12|34'), P('04|13|2')]
    rows_b = [
        (0, 1, 2, 3),
        (0, 1, 3, 2),
        (2, 1, 3, 0),
        (3, 1, 0, 2),
        (2, 1, 0, 3),
    ]
    assert witness_satisfies(rep_a, rows_a)
    assert witness_satisfies(rep_b, rows_b)
    print('Explicit witness for each four-plane orbit: PASS')

    expected = {4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12,
                10: 12, 11: 13, 12: 13, 13: 14, 14: 14}
    print('\nExplicit synchronized upper-bound certificates:')
    for q in range(4, 15):
        fam = CONSTRUCTIONS[q]
        assert len(fam) == q
        D = sum(defect(p) for p in fam)
        assert D == expected[q] == target_defect(q)
        assert all(compatible(a, b) for a, b in combinations(fam, 2))
        forced, certificate = forcing_certificate(fam, q)
        assert forced, (q, [fmt_part(p) for p in fam])
        cost = 4 * q - D
        print(f'q={q:2d}: defect={D:2d}, cost={cost:2d}, '
              f'forced_vertices={len(certificate):2d} PASS')

    print('\nClosed form on finite sector:')
    for q in range(3, 15):
        D = target_defect(q)
        if q <= 9:
            L = 3 * q - 3
        else:
            L = (7 * q - 15 + 1) // 2
        assert L == 4 * q - D
        print(f'q={q:2d}: C5={D:2d}, L_q(5)={L:2d}')

    print('\nALL PASS')


if __name__ == '__main__':
    main()
