from collections import Counter


def plus_M0(N, a, b):
    if a[0] != 'P' or b[0] != 'P':
        return None
    i, j = a[1], b[1]
    if i == 0 and 1 <= j <= N:
        return ('P', j)
    if 1 <= i <= N and j == 0:
        return ('P', i - 1)
    if 1 <= i <= N and i == j:
        return ('Ep', i)
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


def times_G2(N, a, b):
    r = times_M0(N, a, b)
    if r is not None:
        return r
    if a[0] == 'P' and b[0] == 'P':
        i, j = a[1], b[1]
        if 2 <= i < N and j == i + 1:
            return ('Om', 0)
    return None


def assoc_spectrum(N, op):
    pts = [('P', i) for i in range(N + 1)]
    c = Counter()
    for x in pts:
        for y in pts:
            for z in pts:
                xy = op(N, x, y)
                yz = op(N, y, z)
                L = op(N, xy, z) if xy is not None else None
                R = op(N, x, yz) if yz is not None else None
                if L is not None and R is not None:
                    c['EQ' if L == R else 'NEQ'] += 1
                elif L is not None:
                    c['LEFT'] += 1
                elif R is not None:
                    c['RIGHT'] += 1
                else:
                    c['NONE'] += 1
    return c


KEYS = ('EQ', 'NEQ', 'LEFT', 'RIGHT', 'NONE')

for N in range(3, 11):
    cp = assoc_spectrum(N, plus_M0)
    cm = assoc_spectrum(N, times_M0)
    cg = assoc_spectrum(N, times_G2)

    fp = {
        'EQ': N - 1,
        'NEQ': 1,
        'LEFT': 4 * N - 2,
        'RIGHT': 4 * N - 2,
        'NONE': (N + 1) ** 3 - 9 * N + 4,
    }
    fm = {
        'EQ': 4 * (N - 1),
        'NEQ': 0,
        'LEFT': N * N + 2 * N - 2,
        'RIGHT': N * N + N - 2,
        'NONE': N ** 3 + N ** 2 - 4 * N + 9,
    }
    fg = {
        'EQ': 5 * N - 6,
        'NEQ': 0,
        'LEFT': N * N + 3 * N - 4,
        'RIGHT': N * N + 2 * N - 4,
        'NONE': N ** 3 + N ** 2 - 7 * N + 15,
    }

    assert {k: cp[k] for k in KEYS} == fp, (N, cp, fp)
    assert {k: cm[k] for k in KEYS} == fm, (N, cm, fm)
    assert {k: cg[k] for k in KEYS} == fg, (N, cg, fg)
    print(N, 'OK', cp, cm, cg)
