from collections import Counter
from math import factorial


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


def times_G4C(N, a, b):
    r = times_M0(N, a, b)
    if r is not None:
        return r
    if a[0] == 'P' and b[0] == 'P':
        i, j = a[1], b[1]
        if 2 <= i <= N and 2 <= j <= N and i != j:
            return ('Op', 0) if i < j else ('Om', 0)
    return None


def times_G4A(N, a, b):
    r = times_G4C(N, a, b)
    if r is not None:
        return r
    if a == ('P', 1) and b == ('P', 0):
        return ('Op', 0)
    return None


def assoc_spectrum(N, op):
    pts = [('P', i) for i in range(N + 1)]
    c = Counter()
    for x in pts:
        for y in pts:
            for z in pts:
                xy = op(N, x, y)
                yz = op(N, y, z)
                left = op(N, xy, z) if xy is not None else None
                right = op(N, x, yz) if yz is not None else None
                if left is not None and right is not None:
                    c['EQ' if left == right else 'NEQ'] += 1
                elif left is not None:
                    c['LEFT'] += 1
                elif right is not None:
                    c['RIGHT'] += 1
                else:
                    c['NONE'] += 1
    return {k: c[k] for k in ('EQ', 'NEQ', 'LEFT', 'RIGHT', 'NONE')}


def comm_count(N, op):
    pts = [('P', i) for i in range(N + 1)]
    return sum(
        1
        for x in pts
        for y in pts
        if op(N, x, y) is not None
        and op(N, y, x) is not None
        and op(N, x, y) == op(N, y, x)
    )


def base_definedness_automorphism_count(N, anchored):
    # The formulas below are proved in the checkpoint; this function only
    # records the expected closed form for regression output.
    return (2 if anchored else 1) * factorial(N - 1)


for N in range(3, 11):
    f4c = {
        'EQ': N * N + N - 2,
        'NEQ': 0,
        'LEFT': 2 * N * N - N,
        'RIGHT': 2 * N * N - 2 * N,
        'NONE': N ** 3 - 2 * N * N + 5 * N + 3,
    }
    f4a = {
        'EQ': N * N + N - 2,
        'NEQ': 0,
        'LEFT': 2 * N * N - N,
        'RIGHT': 2 * N * N - N,
        'NONE': N ** 3 - 2 * N * N + 4 * N + 3,
    }

    c4c = assoc_spectrum(N, times_G4C)
    c4a = assoc_spectrum(N, times_G4A)

    assert c4c == f4c, (N, 'G4C', c4c, f4c)
    assert c4a == f4a, (N, 'G4A', c4a, f4a)

    assert comm_count(N, times_G4C) == 3 * (N - 1)
    assert comm_count(N, times_G4A) == 3 * (N - 1)

    assert sum(c4c.values()) == (N + 1) ** 3
    assert sum(c4a.values()) == (N + 1) ** 3

    vri_4c = factorial(N - 1) // 2
    vri_4a = 2 * factorial(N - 1)

    print(
        N,
        'OK',
        'G4C', c4c,
        'G4A', c4a,
        'Comm', 3 * (N - 1),
        'DefAut4C', base_definedness_automorphism_count(N, False),
        'DefAut4A', base_definedness_automorphism_count(N, True),
        'VRI4C', vri_4c,
        'VRI4A', vri_4a,
    )
