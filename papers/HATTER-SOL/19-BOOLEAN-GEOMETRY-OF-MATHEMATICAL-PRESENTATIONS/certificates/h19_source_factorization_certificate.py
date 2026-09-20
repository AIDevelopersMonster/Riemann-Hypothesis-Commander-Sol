#!/usr/bin/env python3
"""H19-01 source-factorization certificate.

Compare two E0-equivalent straight-line presentations of the exact same
restricted-12 H18 observer family:

DIRECT12:
    each word is composed independently from its letters;

PREFIX19:
    all nontrivial word prefixes are shared globally.

This is a source-level mathematical/SLP comparison before Boolean synthesis.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve()
H19 = HERE.parents[1]
HATTER = H19.parent
H18 = HATTER / "18-ADAPTIVE-WORD-TOMOGRAPHY"
CERT = H18 / "certificates" / "h18_restricted12_controller_certificate.py"

spec = importlib.util.spec_from_file_location("h18_r12", CERT)
assert spec is not None and spec.loader is not None
r12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r12)

WORDS = tuple(sorted(r12.WORDS, key=lambda w: (len(w), w)))
assert len(WORDS) == 12

# With the H18 hardware convention, the first letter is a wire/source operand;
# each subsequent letter contributes one permutation composition.
direct_nodes = sum(max(0, len(w) - 1) for w in WORDS)

# A shared prefix p of length >=2 corresponds to one composition node:
# p[:-1] composed with its final letter.  Every observer word reuses the node
# for its full word and any shared proper prefixes.
prefixes = {
    w[:k]
    for w in WORDS
    for k in range(2, len(w) + 1)
}
prefix_nodes = len(prefixes)

direct_depth = max(len(w) - 1 for w in WORDS)
prefix_depth = max(len(p) - 1 for p in prefixes)

EXPECTED_WORDS = (
    "A", "B", "AAb", "ABB", "Abb", "Baa", "aab", "abb",
    "AAAB", "AAAb", "ABab", "AbaB",
)
assert WORDS == EXPECTED_WORDS
assert direct_nodes == 24
assert prefix_nodes == 19
assert direct_depth == 3
assert prefix_depth == 3

saved = direct_nodes - prefix_nodes
ratio = prefix_nodes / direct_nodes

print("H19 source-factorization certificate")
print("restricted12 words =", WORDS)
print("DIRECT12 composition nodes =", direct_nodes)
print("PREFIX19 shared composition nodes =", prefix_nodes)
print("composition nodes saved =", saved)
print("PREFIX19 / DIRECT12 =", f"{ratio:.6f}")
print("DIRECT12 max composition depth =", direct_depth)
print("PREFIX19 max composition depth =", prefix_depth)
print("RESULT: E0-equivalent source factorization 24 -> 19 at unchanged depth 3")
print("PASS")
