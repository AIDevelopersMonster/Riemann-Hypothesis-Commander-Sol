#!/usr/bin/env python3
"""Finite certificate for SOL-QFIELD v0.14.

Checks all ordered noncommuting generator pairs (p,q) of S3 and verifies:
  * Parikh-equivalent words produce no cross-parity collision edges;
  * every same-parity unordered pair occurs by word length <= 5;
  * length <= 4 is not a universal bound;
  * exactly 12 ordered pairs close by depth 4 and 6 require depth 5.

No third-party dependencies.
"""

from collections import Counter
from itertools import permutations, product

E = (1, 2, 3)
S3 = tuple(permutations(E))


def compose(p, q):
    """Permutation product p*q = p after q."""
    return tuple(p[q[i] - 1] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, value in enumerate(p, 1):
        out[value - 1] = i
    return tuple(out)


def parity(p):
    inversions = sum(
        p[i] > p[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return inversions % 2


def generated_subgroup(p, q):
    seen = {E}
    changed = True
    gens = (p, q, inverse(p), inverse(q))
    while changed:
        changed = False
        for x in tuple(seen):
            for y in gens:
                z = compose(x, y)
                if z not in seen:
                    seen.add(z)
                    changed = True
    return seen


def word_image(word, p, q):
    g = E
    for letter in word:
        g = compose(g, p if letter == "L" else q)
    return g


def collision_edges_upto(p, q, max_depth):
    edges = set()
    for m in range(max_depth + 1):
        buckets = {}
        for letters in product("LR", repeat=m):
            word = "".join(letters)
            key = (m, word.count("R"))
            buckets.setdefault(key, set()).add(word_image(word, p, q))

        for images in buckets.values():
            images = tuple(images)
            for i, g in enumerate(images):
                for h in images[i + 1 :]:
                    edges.add(frozenset((g, h)))
    return edges


def same_parity_target_edges():
    target = set()
    for i, g in enumerate(S3):
        for h in S3[i + 1 :]:
            if parity(g) == parity(h):
                target.add(frozenset((g, h)))
    return target


def main():
    generator_pairs = [
        (p, q)
        for p in S3
        for q in S3
        if compose(p, q) != compose(q, p)
        and len(generated_subgroup(p, q)) == 6
    ]

    assert len(generator_pairs) == 18

    target = same_parity_target_edges()
    assert len(target) == 6

    closure_depths = []

    for p, q in generator_pairs:
        minimal_depth = None
        for depth in range(2, 6):
            edges = collision_edges_upto(p, q, depth)

            # Parikh collisions may never cross parity.
            assert all(
                len({parity(g) for g in edge}) == 1
                for edge in edges
            )

            if target <= edges:
                minimal_depth = depth
                break

        assert minimal_depth is not None
        closure_depths.append(minimal_depth)

    distribution = Counter(closure_depths)
    assert distribution == Counter({4: 12, 5: 6})
    assert max(closure_depths) == 5
    assert any(depth == 5 for depth in closure_depths)

    print("PASS: all 18 ordered noncommuting S3 generator pairs checked")
    print("PASS: collision graph has no cross-parity edges")
    print("PASS: all six same-parity edges occur by depth <= 5")
    print("PASS: universal depth 4 fails")
    print("PASS: closure-depth distribution = {4: 12, 5: 6}")


if __name__ == "__main__":
    main()
