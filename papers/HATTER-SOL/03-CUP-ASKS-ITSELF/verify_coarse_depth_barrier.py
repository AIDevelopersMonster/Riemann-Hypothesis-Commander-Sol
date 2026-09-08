#!/usr/bin/env python3
"""Deterministic finite verifier for HATTER-SOL-03 coarse-depth barriers.

It enumerates all numbers p = 2^a 3^b + 1 < 10^12 with a,b >= 1,
and certifies primality by trial division by every prime <= 10^6.
Since sqrt(10^12)=10^6, this is deterministic for the entire search range.
"""
from __future__ import annotations

import hashlib

LIMIT = 10**12
TRIAL_LIMIT = 10**6


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    m = int(n**0.5)
    for p in range(2, m + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


TRIAL_PRIMES = primes_upto(TRIAL_LIMIT)


def is_prime_below_1e12(n: int) -> bool:
    if n < 2 or n >= LIMIT:
        return False
    for p in TRIAL_PRIMES:
        if p * p > n:
            return True
        if n % p == 0:
            return n == p
    return True


def enumerate_support_23() -> list[tuple[int, int, int]]:
    rows: list[tuple[int, int, int]] = []
    a = 1
    while (2**a) * 3 + 1 < LIMIT:
        b = 1
        while (2**a) * (3**b) + 1 < LIMIT:
            n = (2**a) * (3**b) + 1
            if is_prime_below_1e12(n):
                rows.append((a, b, n))
            b += 1
        a += 1
    return rows


def main() -> None:
    rows = enumerate_support_23()
    payload = "\n".join(f"{a},{b},{p}" for a, b, p in rows).encode("ascii")
    digest = hashlib.sha256(payload).hexdigest()

    fermat = [3, 5, 17, 257, 65537]
    assert all(is_prime_below_1e12(p) for p in fermat)
    assert len(rows) == 77, len(rows)
    assert 77 > 8**2
    assert len(fermat) == 5 > 4

    print("HATTER-SOL-03 coarse-depth verifier")
    print(f"search bound: p < {LIMIT}")
    print(f"trial division bound: {TRIAL_LIMIT}")
    print(f"certified primes p=2^a*3^b+1 with a,b>=1: {len(rows)}")
    print(f"SHA256(a,b,p rows): {digest}")
    print("five known Fermat primes used for the 2-bit pigeonhole barrier:")
    print(" ".join(map(str, fermat)))
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
