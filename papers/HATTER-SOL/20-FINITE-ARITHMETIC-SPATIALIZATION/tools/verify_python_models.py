#!/usr/bin/env python3
import argparse
import math

def prime(n):
    if n < 2:
        return False
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def nextp(x):
    q = x + 1
    while not prime(q):
        q += 1
    return q

def plist(w):
    last = nextp((1 << w) - 1)
    return [n for n in range(2, last + 1) if prime(n)]

def linear(x, ps):
    for p in ps:
        if x < p:
            return p
    raise AssertionError

def balanced(x, ps):
    lo, hi = 0, len(ps) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if x < ps[mid]:
            hi = mid
        else:
            lo = mid + 1
    return ps[lo]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--widths", nargs="+", type=int, default=[4,5,6,7,8,9,10])
    a = ap.parse_args()

    for w in a.widths:
        ps = plist(w)
        for x in range(1 << w):
            e = nextp(x)
            assert linear(x, ps) == e, (w, x, "linear")
            assert balanced(x, ps) == e, (w, x, "balanced")
        print(f"PASS W={w}: {1<<w} inputs; primes={len(ps)}; next after max={ps[-1]}")

if __name__ == "__main__":
    main()
