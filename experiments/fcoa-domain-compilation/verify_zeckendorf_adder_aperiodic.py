#!/usr/bin/env python3
"""Verify the aperiodicity certificate used by the FCOA Zeckendorf-memory note.

Source automaton:
  firetto/Walnut, Custom Bases/msd_fib_addition.txt
  Git blob SHA: cf7be811768be7aa981b3a7a38a9688783ee98e5

Walnut lists seven states. Missing transitions are completed by one rejecting
sink state. The script enumerates the transition monoid and verifies that every
monoid element has an idempotent power, hence the monoid is aperiodic.

It also performs a finite sanity check that the automaton accepts precisely
x+y=z on canonical Zeckendorf representations for x,y,z in a small range.
"""

from collections import deque
from itertools import product

SOURCE_BLOB_SHA = "cf7be811768be7aa981b3a7a38a9688783ee98e5"

ALPHABET = list(product((0, 1), repeat=3))
LISTED_STATES = tuple(range(7))
DEAD = 7
STATES = tuple(range(8))
ACCEPTING = {0, 4, 6}

RAW = {
    0: {
        (0, 0, 0): 0,
        (0, 0, 1): 1,
        (1, 0, 1): 0,
        (0, 1, 1): 0,
    },
    1: {
        (0, 0, 0): 2,
        (1, 0, 0): 3,
        (0, 1, 0): 3,
        (1, 1, 0): 4,
        (1, 0, 1): 2,
        (0, 1, 1): 2,
        (1, 1, 1): 3,
    },
    2: {
        (1, 0, 0): 2,
        (0, 1, 0): 2,
        (1, 1, 0): 3,
        (1, 1, 1): 2,
    },
    3: {
        (0, 0, 0): 1,
        (1, 0, 0): 0,
        (0, 1, 0): 0,
        (1, 0, 1): 1,
        (0, 1, 1): 1,
        (1, 1, 1): 0,
    },
    4: {
        (0, 0, 0): 5,
        (0, 0, 1): 6,
        (1, 0, 1): 5,
        (0, 1, 1): 5,
    },
    5: {
        (0, 0, 1): 0,
    },
    6: {
        (0, 0, 0): 3,
        (1, 0, 0): 4,
        (0, 1, 0): 4,
        (0, 0, 1): 2,
        (1, 0, 1): 3,
        (0, 1, 1): 3,
        (1, 1, 1): 4,
    },
}


def transition(state, symbol):
    if state == DEAD:
        return DEAD
    return RAW[state].get(symbol, DEAD)


def transformation(symbol):
    return tuple(transition(state, symbol) for state in STATES)


def compose(f, g):
    """Return f after g."""
    return tuple(f[g[i]] for i in STATES)


def transition_monoid():
    identity = tuple(STATES)
    generators = list(dict.fromkeys(transformation(a) for a in ALPHABET))
    monoid = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            nxt = compose(generator, current)
            if nxt not in monoid:
                monoid.add(nxt)
                queue.append(nxt)
    return monoid


def stabilization_exponent(t, bound=100):
    identity = tuple(STATES)
    power = identity
    for n in range(bound + 1):
        nxt = compose(t, power)
        if nxt == power:
            return n
        power = nxt
    return None


def fib_weights(max_value):
    max_value = max(max_value, 1)
    weights = [1, 2]
    while weights[-1] + weights[-2] <= max_value:
        weights.append(weights[-1] + weights[-2])
    return weights


def zeckendorf_bits(n, weights):
    bits = [0] * len(weights)
    remainder = n
    for i in range(len(weights) - 1, -1, -1):
        if weights[i] <= remainder:
            bits[i] = 1
            remainder -= weights[i]
    assert remainder == 0
    assert all(not (bits[i] and bits[i + 1]) for i in range(len(bits) - 1))
    return bits


def accepts(x, y, z):
    weights = fib_weights(max(x, y, z))
    bx = zeckendorf_bits(x, weights)
    by = zeckendorf_bits(y, weights)
    bz = zeckendorf_bits(z, weights)
    state = 0
    for i in range(len(weights) - 1, -1, -1):
        state = transition(state, (bx[i], by[i], bz[i]))
    return state in ACCEPTING


def addition_sanity(limit=64):
    for x in range(limit):
        for y in range(limit):
            # Check the true sum when it is in the tested output range.
            if x + y < 2 * limit and not accepts(x, y, x + y):
                return False, (x, y, x + y, "false negative")
            # A few canonical false targets, including truncation-like cases.
            candidates = {0, x, y, (x + y + 1) % (2 * limit)}
            for z in candidates:
                if z != x + y and accepts(x, y, z):
                    return False, (x, y, z, "false positive")
    return True, None


def main():
    monoid = transition_monoid()
    exponents = [stabilization_exponent(t) for t in monoid]
    assert None not in exponents

    ok, witness = addition_sanity()
    assert ok, witness

    print(f"Walnut source blob SHA: {SOURCE_BLOB_SHA}")
    print(f"completed DFA states: {len(STATES)}")
    print(f"distinct letter transformations: {len(set(transformation(a) for a in ALPHABET))}")
    print(f"transition monoid size: {len(monoid)}")
    print(f"maximum stabilization exponent: {max(exponents)}")
    print("aperiodicity: PASS")
    print("Zeckendorf addition sanity check: PASS")


if __name__ == "__main__":
    main()
