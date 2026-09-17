#!/usr/bin/env python3
"""Regression verifier for LQR_R7_TANGENT_SOCLE.md.

Checks the finite linear-algebra normal form used in the analytic proof:
- rank(m_q)=28 for q=t1t2+t3t4+t5t6;
- dim Ann(q)=36;
- graded kernel dimensions 0,0,1,14,14,6,1;
- Ann(q)^2 is exactly the one-dimensional socle A_6;
- J^perp is exactly the same socle for the group-basis Frobenius pairing.
"""

N = 64
QMONS = [0b000011, 0b001100, 0b110000]
TOP = 0b111111


def mul_poly(a, b):
    out = 0
    aa = [i for i in range(N) if (a >> i) & 1]
    bb = [j for j in range(N) if (b >> j) & 1]
    for i in aa:
        for j in bb:
            if i & j == 0:
                out ^= 1 << (i | j)
    return out


def mul_q(x):
    out = 0
    for i in range(N):
        if not ((x >> i) & 1):
            continue
        for m in QMONS:
            if i & m == 0:
                out ^= 1 << (i | m)
    return out


def rref_kernel(rows, ncols):
    rows = [r for r in rows if r]
    r = 0
    piv = []
    for c in range(ncols):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        piv.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv]
    ker = []
    for f in free:
        x = 1 << f
        for i, c in enumerate(piv):
            if (rows[i] >> f) & 1:
                x |= 1 << c
        ker.append(x)
    return r, ker


def rank_vectors(vs, ncols=64):
    rows = [v for v in vs if v]
    r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> c) & 1), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> c) & 1):
                rows[i] ^= rows[r]
        r += 1
    return r


# Full multiplication matrix columns and equation rows.
cols = [mul_q(1 << i) for i in range(N)]
eq_rows = [0] * N
for c, col in enumerate(cols):
    for rr in range(N):
        if (col >> rr) & 1:
            eq_rows[rr] |= 1 << c

rank_q, ann = rref_kernel(eq_rows, N)
assert rank_q == 28
assert len(ann) == 36

# Graded kernel dimensions.
graded = []
for degree in range(7):
    src = [m for m in range(N) if m.bit_count() == degree]
    tgt = [m for m in range(N) if m.bit_count() == degree + 2]
    rows = []
    for tm in tgt:
        row = 0
        for j, sm in enumerate(src):
            if (mul_q(1 << sm) >> tm) & 1:
                row |= 1 << j
        rows.append(row)
    rk, _ = rref_kernel(rows, len(src))
    graded.append(len(src) - rk)
assert graded == [0, 0, 1, 14, 14, 6, 1]

# Products of annihilator basis elements span exactly top socle.
products = []
for i, x in enumerate(ann):
    for y in ann[i:]:
        z = mul_poly(x, y)
        if z:
            assert z & ~(1 << TOP) == 0
            products.append(z)
assert rank_vectors(products) == 1
assert products

# J^perp under lambda(t_S)=1: solve lambda(w*t_T)=0 for all nonempty T.
perp_rows = []
for T in range(1, N):
    row = 0
    for W in range(N):
        if W & T == 0:
            row |= 1 << W
    perp_rows.append(row)
rank_perp_constraints, perp = rref_kernel(perp_rows, N)
assert rank_perp_constraints == 63
assert len(perp) == 1
assert perp[0] == (1 << TOP)

print("PASS: rank(m_q)=28 and dim Ann(q)=36")
print("PASS: graded Ann(q) dimensions 0,0,1,14,14,6,1")
print("PASS: Ann(q)^2 = J^6")
print("PASS: J^perp = J^6 for the group-basis Frobenius pairing")
print("ALL PASS")
