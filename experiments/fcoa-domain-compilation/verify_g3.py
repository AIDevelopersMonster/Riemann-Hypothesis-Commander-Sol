from collections import Counter


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


def times_G3S(N, a, b):
    r = times_M0(N, a, b)
    if r is not None:
        return r
    if a[0] == 'P' and b[0] == 'P':
        i, j = a[1], b[1]
        if 2 <= i <= N and 2 <= j <= N and abs(i - j) == 1:
            return ('Om', 0)
    return None


def times_G3C(N, a, b):
    r = times_M0(N, a, b)
    if r is not None:
        return r
    if a[0] == 'P' and b[0] == 'P':
        i, j = a[1], b[1]
        if 2 <= i < N and j == i + 1:
            return ('Op', 0)
        if 2 <= j < N and i == j + 1:
            return ('Om', 0)
    return None


def times_G3A(N, a, b):
    r = times_G3C(N, a, b)
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
    return {k: c[k] for k in ('EQ', 'NEQ', 'LEFT', 'RIGHT', 'NONE')}


def comm_count(N, op):
    pts = [('P', i) for i in range(N + 1)]
    total = 0
    for x in pts:
        for y in pts:
            xy = op(N, x, y)
            yx = op(N, y, x)
            if xy is not None and yx is not None and xy == yx:
                total += 1
    return total


for N in range(3, 11):
    fs = {
        'EQ': 6 * N - 8,
        'NEQ': 0,
        'LEFT': N * N + 4 * N - 6,
        'RIGHT': N * N + 3 * N - 6,
        'NONE': N ** 3 + N ** 2 - 10 * N + 21,
    }
    fa = {
        'EQ': 6 * N - 8,
        'NEQ': 0,
        'LEFT': N * N + 4 * N - 6,
        'RIGHT': N * N + 4 * N - 6,
        'NONE': N ** 3 + N ** 2 - 11 * N + 21,
    }

    ss = assoc_spectrum(N, times_G3S)
    sc = assoc_spectrum(N, times_G3C)
    sa = assoc_spectrum(N, times_G3A)

    assert ss == fs, (N, 'G3S', ss, fs)
    assert sc == fs, (N, 'G3C', sc, fs)
    assert sa == fa, (N, 'G3A', sa, fa)

    assert comm_count(N, times_G3S) == 5 * N - 7
    assert comm_count(N, times_G3C) == 3 * (N - 1)
    assert comm_count(N, times_G3A) == 3 * (N - 1)

    print(N, 'OK', 'G3S', ss, 'G3C', sc, 'G3A', sa)
