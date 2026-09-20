#!/usr/bin/env python3
"""H19-02: exact NIELSEN12 source-profile certificate.

The semantic observer family is frozen to the H18 restricted-12 alphabet.
This certificate compares three E0-equivalent source factorizations before
Boolean synthesis:

  DIRECT12  -- independent direct word compositions;
  PREFIX19  -- global shared-prefix composition DAG;
  NIELSEN12 -- ten primitive observers obtained by shortest elementary Nielsen
               programmes, while the two oriented commutators remain direct.

Nielsen programmes are reported as a RESOURCE VECTOR.  Swap, inversion and
shear moves are not silently identified with one hardware primitive.
"""

from __future__ import annotations

import importlib.util
from collections import Counter
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
PRIMITIVE = tuple(w for w in WORDS if w not in ("ABab", "AbaB"))
COMMUTATORS = ("ABab", "AbaB")

assert len(WORDS) == 12
assert len(PRIMITIVE) == 10
assert set(COMMUTATORS) == set(WORDS) - set(PRIMITIVE)

# ---------------------------------------------------------------------------
# P0: independent direct word realization.
# ---------------------------------------------------------------------------

DIRECT_COST = {w: max(0, len(w) - 1) for w in WORDS}
DIRECT_NODES = sum(DIRECT_COST.values())
DIRECT_DEPTH = max(DIRECT_COST.values())

assert DIRECT_NODES == 24
assert DIRECT_DEPTH == 3

# ---------------------------------------------------------------------------
# P1: globally shared prefix DAG.
# ---------------------------------------------------------------------------

PREFIXES = {
    w[:k]
    for w in WORDS
    for k in range(2, len(w) + 1)
}
PREFIX_NODES = len(PREFIXES)
PREFIX_DEPTH = max(len(p) - 1 for p in PREFIXES)

assert PREFIX_NODES == 19
assert PREFIX_DEPTH == 3

# ---------------------------------------------------------------------------
# P2: shortest elementary Nielsen programmes for primitive labels.
# ---------------------------------------------------------------------------

PROGRAMS = r12.PROGRAMS
EXPECTED_LENGTH = r12.EXPECTED_NIELSEN_LENGTH
assert set(PROGRAMS) == set(PRIMITIVE)

MOVE_CLASSES = {
    "S": "swap",
    "I_A": "inverse",
    "I_B": "inverse",
    "N_A+": "shear",
    "N_A-": "shear",
    "N_B+": "shear",
    "N_B-": "shear",
}

per_word = {}
move_totals = Counter()
for word in PRIMITIVE:
    length, coordinate, program, final_pair = PROGRAMS[word]
    assert length == EXPECTED_LENGTH[word]
    classes = tuple(MOVE_CLASSES[m] for m in program)
    counts = Counter(classes)
    move_totals.update(counts)
    per_word[word] = {
        "coordinate": coordinate,
        "program": program,
        "move_classes": classes,
        "counts": counts,
        "elementary_length": length,
        "final_pair": final_pair,
        "direct_compositions": DIRECT_COST[word],
    }

NIELSEN_ELEMENTARY_STEPS = sum(EXPECTED_LENGTH.values())
assert NIELSEN_ELEMENTARY_STEPS == 21

# The two nonprimitive oriented commutators are intentionally left in their
# direct three-composition realization in this first NIELSEN12 presentation.
COMMUTATOR_DIRECT_COMPOSITIONS = sum(DIRECT_COST[w] for w in COMMUTATORS)
assert COMMUTATOR_DIRECT_COMPOSITIONS == 6

MIXED_STEP_COUNT = NIELSEN_ELEMENTARY_STEPS + COMMUTATOR_DIRECT_COMPOSITIONS
assert MIXED_STEP_COUNT == 27

# This 27 is NOT called a hardware gate count: it mixes Nielsen move types with
# direct permutation-composition nodes.  The exact source profile is the vector
# below.
PROFILE = {
    "swap_moves": move_totals["swap"],
    "inverse_moves": move_totals["inverse"],
    "shear_moves": move_totals["shear"],
    "direct_commutator_compositions": COMMUTATOR_DIRECT_COMPOSITIONS,
    "elementary_nielsen_steps": NIELSEN_ELEMENTARY_STEPS,
}

# Exact semantic identity is constructive: the final pair coordinate recorded
# by H18-11 is exactly the requested reduced word.
for word, info in per_word.items():
    assert info["final_pair"][info["coordinate"]] == word

# H18-11 already certifies the elementary-program versus direct-composition
# deltas for the primitive labels: seven ties and three +1.
DELTAS = {
    w: EXPECTED_LENGTH[w] - DIRECT_COST[w]
    for w in PRIMITIVE
}
assert Counter(DELTAS.values()) == Counter({0: 7, 1: 3})

print("H19 NIELSEN12 source-profile certificate")
print("observer alphabet =", WORDS)
print("DIRECT12 composition nodes =", DIRECT_NODES)
print("DIRECT12 max composition depth =", DIRECT_DEPTH)
print("PREFIX19 shared composition nodes =", PREFIX_NODES)
print("PREFIX19 max composition depth =", PREFIX_DEPTH)
print("NIELSEN12 primitive shortest programmes:")
for word in PRIMITIVE:
    info = per_word[word]
    print(
        " ",
        word,
        "program=", info["program"],
        "classes=", info["move_classes"],
        "coordinate=", info["coordinate"],
        "direct=", info["direct_compositions"],
    )
print("NIELSEN12 resource vector =", PROFILE)
print("NIELSEN12 mixed source-step count =", MIXED_STEP_COUNT)
print("primitive Nielsen-minus-direct deltas =", DELTAS)
print("RESULT: all three source presentations are E0-equivalent on observer semantics")
print("CLAIM BOUNDARY: mixed source-step count is not a Boolean/FPGA area metric")
print("PASS")
