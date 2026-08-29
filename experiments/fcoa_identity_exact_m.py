#!/usr/bin/env python3
"""Exact calculator for minimum-size identity digraphs.

Given n >= 1, computes

    m(n) = min{|F| : F subset X_n^2 \ Delta, Stab_{S_n}(F) = 1}

using the exact counts a_k of nonisomorphic identity oriented trees.

Mathematical input:
- A102755: a_k = number of asymmetric/identity oriented trees on k nodes.
- A005753: rooted identity-oriented-tree series B(x), with

      B(x) = x * exp(2 * sum_{r>=1} (-1)^(r+1) B(x^r)/r)

  and A102755 generating function A(x)=B(x)-B(x)^2.

The script computes the coefficients internally with exact integer arithmetic;
no network access or precomputed OEIS table is required.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from math import isqrt
from typing import List


OEIS_A102755_PREFIX = [
    1, 1, 1, 4, 10, 37, 135, 522, 2060, 8430, 35115, 149286,
    644456, 2821835, 12503878, 56001856, 253174451, 1154179790,
    5301178673, 24513058220, 114042743290, 533510321377,
    2508491383101, 11849321038092, 56211286929146,
    267707017974770, 1279602152054934,
]


@dataclass(frozen=True)
class ExactResult:
    n: int
    m: int
    delta: int
    threshold_order: int
    types_below: int
    vertices_below: int
    selected_at_threshold: int
    available_at_threshold: int
    remainder: int


def _signed_divisor_sum(m: int, rooted: List[int]) -> int:
    """Return s_m = 2 sum_{d|m} (-1)^(m/d+1) d b_d."""
    total = 0
    q = isqrt(m)
    for d in range(1, q + 1):
        if m % d:
            continue

        d1 = d
        r1 = m // d1
        total += 2 * (1 if r1 % 2 else -1) * d1 * rooted[d1]

        d2 = m // d
        if d2 != d1:
            r2 = m // d2
            total += 2 * (1 if r2 % 2 else -1) * d2 * rooted[d2]
    return total


def next_tree_count(rooted: List[int], svals: List[int]) -> int:
    """Append one rooted count b_{m+1} and return unrooted a_{m+1}.

    If rooted currently contains b_1,...,b_m, use the exponential-series
    recurrence

        m b_{m+1} = sum_{k=1}^m s_k b_{m-k+1},

    where

        s_k = 2 sum_{d|k} (-1)^(k/d+1) d b_d.
    """
    m = len(rooted) - 1
    sm = _signed_divisor_sum(m, rooted)
    if len(svals) <= m:
        svals.append(sm)
    else:
        svals[m] = sm

    numerator = sum(svals[k] * rooted[m - k + 1] for k in range(1, m + 1))
    if numerator % m:
        raise ArithmeticError("rooted recurrence lost integrality")

    b_next = numerator // m
    rooted.append(b_next)
    n = m + 1

    convolution = sum(rooted[i] * rooted[n - i] for i in range(1, n))
    return b_next - convolution


def exact_m(n: int) -> ExactResult:
    if n < 1:
        raise ValueError("n must be a positive integer")

    # b_1=1; a_1=1.
    rooted = [0, 1]
    svals = [0, 0]
    tree_counts = [0, 1]

    A_prev = 0  # sum_{j<k} a_j
    W_prev = 0  # sum_{j<k} j a_j
    k = 1

    while True:
        a_k = tree_counts[k]
        W_k = W_prev + k * a_k

        if n < W_k:
            q = (n - W_prev) // k
            delta = A_prev + q
            remainder = n - (W_prev + q * k)
            return ExactResult(
                n=n,
                m=n - delta,
                delta=delta,
                threshold_order=k,
                types_below=A_prev,
                vertices_below=W_prev,
                selected_at_threshold=q,
                available_at_threshold=a_k,
                remainder=remainder,
            )

        A_prev += a_k
        W_prev = W_k

        a_next = next_tree_count(rooted, svals)
        tree_counts.append(a_next)
        k += 1


def self_test() -> None:
    rooted = [0, 1]
    svals = [0, 0]
    got = [1]
    while len(got) < len(OEIS_A102755_PREFIX):
        got.append(next_tree_count(rooted, svals))
    if got != OEIS_A102755_PREFIX:
        raise AssertionError(f"A102755 prefix mismatch:\nexpected={OEIS_A102755_PREFIX}\ngot={got}")

    expected = {
        1: (0, 1),
        2: (1, 1),
        3: (1, 2),
        6: (3, 3),
        10: (6, 4),
        27: (19, 8),
        1000: (846, 154),
        1_000_000: (911_561, 88_439),
    }
    for n, pair in expected.items():
        r = exact_m(n)
        if (r.m, r.delta) != pair:
            raise AssertionError((n, pair, r))


def print_result(r: ExactResult) -> None:
    print(f"n                         = {r.n}")
    print(f"m(n)                      = {r.m}")
    print(f"delta(n)=n-m(n)           = {r.delta}")
    print(f"threshold order K         = {r.threshold_order}")
    print(f"types of order < K        = {r.types_below}")
    print(f"vertices used below K     = {r.vertices_below}")
    print(f"selected order-K types    = {r.selected_at_threshold}")
    print(f"available order-K types   = {r.available_at_threshold}")
    print(f"exact-order remainder     = {r.remainder}")

    k = r.threshold_order
    q = r.selected_at_threshold
    rem = r.remainder
    print("\nOptimal symbolic component recipe:")
    print(f"  take every identity oriented-tree type of order < {k};")
    if q:
        print(f"  take any {q} distinct identity oriented-tree types of order {k};")
    if rem:
        if q:
            print(
                f"  replace one selected order-{k} component by a directed path "
                f"of order {k + rem}."
            )
        else:
            s = k - 1
            print(
                f"  replace one maximum-order selected component (order {s}) "
                f"by a directed path of order {s + rem}."
            )
    else:
        print("  no stretching is needed.")

    print(f"\nComponent count = delta(n) = {r.delta}")
    print(f"Arc count       = n-delta(n) = {r.m}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Exact minimum-size identity-digraph calculator")
    parser.add_argument("n", nargs="?", type=int, help="positive order n")
    parser.add_argument("--self-test", action="store_true", help="verify recurrence against OEIS prefix")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("SELF-TEST: PASS")

    if args.n is not None:
        print_result(exact_m(args.n))
    elif not args.self_test:
        parser.error("provide n or use --self-test")


if __name__ == "__main__":
    main()
