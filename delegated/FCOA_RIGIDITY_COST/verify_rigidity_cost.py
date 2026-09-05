from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb


def degree_classes_directed(n, edges):
    indeg = [0] * n
    outdeg = [0] * n
    for u, v in edges:
        outdeg[u] += 1
        indeg[v] += 1
    classes = defaultdict(list)
    for v in range(n):
        classes[(outdeg[v], indeg[v])].append(v)
    return list(classes.values())


def degree_classes_undirected(n, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    classes = defaultdict(list)
    for v in range(n):
        classes[deg[v]].append(v)
    return list(classes.values())


def candidate_permutations(n, classes):
    ident = tuple(range(n))
    for choices in product(*(list(permutations(c)) for c in classes)):
        p = list(range(n))
        for c, pc in zip(classes, choices):
            for old, new in zip(c, pc):
                p[old] = new
        p = tuple(p)
        if p != ident:
            yield p


def aut_size_directed(n, edges):
    E = frozenset(edges)
    size = 1
    for p in candidate_permutations(n, degree_classes_directed(n, E)):
        if frozenset((p[u], p[v]) for u, v in E) == E:
            size += 1
    return size


def aut_size_undirected(n, edges):
    E = frozenset(tuple(sorted(e)) for e in edges)
    size = 1
    for p in candidate_permutations(n, degree_classes_undirected(n, E)):
        image = frozenset(tuple(sorted((p[u], p[v]))) for u, v in E)
        if image == E:
            size += 1
    return size


def min_directed_with_aut_size(n, target):
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for m in range(n):
        for E in combinations(arcs, m):
            if target == 1:
                incident = {x for e in E for x in e}
                if n - len(incident) > 1:
                    continue
            if aut_size_directed(n, E) == target:
                return m, E
    return None


def min_undirected_with_aut_size(n, target):
    edges = list(combinations(range(n), 2))
    for m in range(n + 1):
        for E in combinations(edges, m):
            if target == 1:
                incident = {x for e in E for x in e}
                if n - len(incident) > 1:
                    continue
            if aut_size_undirected(n, E) == target:
                return m, E
    return None


def anonymous_two_fiber_group(n, A):
    A = frozenset(A)
    universe = frozenset((u, v) for u in range(n) for v in range(n) if u != v)
    B = universe - A
    good = []
    for p in permutations(range(n)):
        image = frozenset((p[u], p[v]) for u, v in A)
        if image == A or image == B:
            good.append(p)
    return good


def first_balanced_rigid_partition(n):
    universe = tuple((u, v) for u in range(n) for v in range(n) if u != v)
    half = len(universe) // 2
    fixed = universe[0]
    for subset in combinations(universe[1:], half - 1):
        A = frozenset((fixed,) + subset)
        if len(anonymous_two_fiber_group(n, A)) == 1:
            return A
    return None


def tournament_from_bits(n, bits):
    A = set()
    for k, (u, v) in enumerate(combinations(range(n), 2)):
        A.add((u, v) if (bits >> k) & 1 else (v, u))
    return frozenset(A)


def first_balanced_rigid_tournament(n):
    for bits in range(1 << comb(n, 2)):
        A = tournament_from_bits(n, bits)
        if len(anonymous_two_fiber_group(n, A)) == 1:
            return A
    return None


def times_M0(N, a, b):
    if a[0] != 'P' or b[0] != 'P':
        return None
    i, j = a[1], b[1]
    if i == 0 and 1 <= j <= N:
        return ('P', 0)
    if 2 <= i <= N and j == 0:
        return ('Es', i)
    if i == 1 and 2 <= j <= N:
        return ('P', j)
    if 2 <= i <= N and j == 1:
        return ('P', i)
    if 2 <= i <= N and i == j:
        return ('Ex', i)
    return None


def times_layer(N, A, colors, a, b):
    r = times_M0(N, a, b)
    if r is not None:
        return r
    if a[0] == 'P' and b[0] == 'P' and (a[1], b[1]) in A:
        return ('Om', colors[(a[1], b[1])])
    return None


def assoc_spectrum(N, A, colors):
    pts = [('P', i) for i in range(N + 1)]
    c = Counter()
    for x in pts:
        for y in pts:
            for z in pts:
                xy = times_layer(N, A, colors, x, y)
                yz = times_layer(N, A, colors, y, z)
                L = times_layer(N, A, colors, xy, z) if xy is not None else None
                R = times_layer(N, A, colors, x, yz) if yz is not None else None
                if L is not None and R is not None:
                    c['EQ' if L == R else 'NEQ'] += 1
                elif L is not None:
                    c['LEFT'] += 1
                elif R is not None:
                    c['RIGHT'] += 1
                else:
                    c['NONE'] += 1
    return {k: c[k] for k in ('EQ', 'NEQ', 'LEFT', 'RIGHT', 'NONE')}


def verify_master_formula(max_N=5):
    for N in range(3, max_N + 1):
        generics = range(2, N + 1)
        arcs = [(u, v) for u in generics for v in generics if u != v]
        for mask in range(1 << len(arcs)):
            A = {arc for i, arc in enumerate(arcs) if (mask >> i) & 1}
            colors = {arc: i % 3 for i, arc in enumerate(sorted(A))}
            m = len(A)
            expected = {
                'EQ': 4 * (N - 1) + m,
                'NEQ': 0,
                'LEFT': N * N + 2 * N - 2 + m,
                'RIGHT': N * N + N - 2 + m,
                'NONE': N ** 3 + N ** 2 - 4 * N + 9 - 3 * m,
            }
            assert assoc_spectrum(N, A, colors) == expected


def main():
    rigid_dir = {2: 1, 3: 1, 4: 2, 5: 3, 6: 3, 7: 4}
    rigid_undir = {2: None, 3: None, 4: None, 5: None, 6: 6, 7: 6}
    c2_dir = {2: 0, 3: 2, 4: 1, 5: 2, 6: 3, 7: 3}
    c2_undir = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5}

    print('FULL RIGIDITY MINIMA')
    for n, expected in rigid_dir.items():
        got = min_directed_with_aut_size(n, 1)
        assert got and got[0] == expected
        print('directed', n, got)
    for n, expected in rigid_undir.items():
        got = min_undirected_with_aut_size(n, 1)
        assert (got is None) if expected is None else (got and got[0] == expected)
        print('undirected', n, got)

    print('\nC2 MINIMA')
    for n, expected in c2_dir.items():
        got = min_directed_with_aut_size(n, 2)
        assert got and got[0] == expected
        print('directed C2', n, got)
    for n, expected in c2_undir.items():
        got = min_undirected_with_aut_size(n, 2)
        assert got and got[0] == expected
        print('undirected C2', n, got)

    print('\nBALANCED COMPLETE TWO-FIBER PARTITIONS')
    for n in range(2, 5):
        got = first_balanced_rigid_partition(n)
        assert (got is None) if n < 4 else (got is not None)
        print('balanced arbitrary', n, got)

    print('\nBALANCED TOURNAMENT PARTITIONS')
    for n in range(2, 6):
        got = first_balanced_rigid_tournament(n)
        assert (got is None) if n < 5 else (got is not None)
        print('balanced tournament', n, got)

    T5 = frozenset({
        (4, 0), (4, 1), (4, 2), (4, 3),
        (2, 0), (2, 1), (3, 1), (3, 2), (0, 3), (1, 0),
    })
    assert aut_size_directed(5, T5) == 1
    assert len(anonymous_two_fiber_group(5, T5)) == 1

    print('\nTERMINAL LAYER MASTER FORMULA')
    verify_master_formula(5)
    print('verified exhaustively for every directed generic domain through N=5')
    print('\nALL CHECKS PASSED')


if __name__ == '__main__':
    main()
