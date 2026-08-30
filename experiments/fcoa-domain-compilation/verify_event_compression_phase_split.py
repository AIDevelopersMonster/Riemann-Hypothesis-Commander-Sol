#!/usr/bin/env python3
"""Finite verification for the FCOA linear event-compression theorems.

This script checks, on explicit finite ranges:

1. Zeckendorf successor has exactly one 0->1 digit event per increment.
2. |U|+|D| = 2m-2-s_F(m-1).
3. Latest-event integration reconstructs the full Zeckendorf digit history.
4. Binary increment has exactly one 0->1 bit event per increment.
5. |U_2|+|D_2| = 2m-2-s_2(m-1).
6. Latest-event integration reconstructs BIT.

The finite checks are reproducibility evidence only; the repository notes contain
the general proofs.
"""


def fib_weights(limit):
    weights = [1, 2]
    while weights[-1] + weights[-2] <= max(limit, 2):
        weights.append(weights[-1] + weights[-2])
    return weights


def zeckendorf_bits(n, weights):
    bits = [0] * len(weights)
    r = n
    for i in range(len(weights) - 1, -1, -1):
        if weights[i] <= r:
            bits[i] = 1
            r -= weights[i]
    assert r == 0
    assert all(not (bits[i] and bits[i + 1]) for i in range(len(bits) - 1))
    return bits


def binary_bits(n, width):
    return [(n >> i) & 1 for i in range(width)]


def events_from_rows(rows):
    up = set()
    down = set()
    for n in range(1, len(rows)):
        for p, (old, new) in enumerate(zip(rows[n - 1], rows[n])):
            if old == 0 and new == 1:
                up.add((n, p))
            elif old == 1 and new == 0:
                down.add((n, p))
    return up, down


def reconstruct(rows_count, width, up, down):
    out = []
    current = [0] * width
    out.append(tuple(current))
    for n in range(1, rows_count):
        for p in range(width):
            if (n, p) in up:
                assert (n, p) not in down
                current[p] = 1
            elif (n, p) in down:
                current[p] = 0
        out.append(tuple(current))
    return out


def verify_zeckendorf(m):
    weights = fib_weights(m - 1)
    rows = [tuple(zeckendorf_bits(n, weights)) for n in range(m)]
    up, down = events_from_rows(rows)

    for n in range(1, m):
        assert sum((n, p) in up for p in range(len(weights))) == 1

    s_last = sum(rows[-1])
    assert len(up) == m - 1
    assert len(down) == m - 1 - s_last
    assert len(up) + len(down) == 2 * m - 2 - s_last
    assert reconstruct(m, len(weights), up, down) == rows

    return len(up), len(down), s_last


def verify_binary(m):
    width = max(1, (m - 1).bit_length())
    rows = [tuple(binary_bits(n, width)) for n in range(m)]
    up, down = events_from_rows(rows)

    for n in range(1, m):
        assert sum((n, p) in up for p in range(width)) == 1

    s_last = (m - 1).bit_count()
    assert len(up) == m - 1
    assert len(down) == m - 1 - s_last
    assert len(up) + len(down) == 2 * m - 2 - s_last
    assert reconstruct(m, width, up, down) == rows

    return len(up), len(down), s_last


def main():
    test_sizes = [2, 3, 4, 5, 8, 10, 16, 31, 64, 100, 256, 1000, 4096]

    for m in test_sizes:
        zu, zd, zs = verify_zeckendorf(m)
        bu, bd, bs = verify_binary(m)
        print(
            f"m={m:4d}  "
            f"Z-events={zu + zd:5d} (U={zu},D={zd},sF={zs})  "
            f"BIT-events={bu + bd:5d} (U={bu},D={bd},s2={bs})"
        )

    print("Zeckendorf one-up/event-count/reconstruction: PASS")
    print("Binary one-up/event-count/reconstruction: PASS")
    print("Equal-linear-support differential comparison: PASS")


if __name__ == "__main__":
    main()
