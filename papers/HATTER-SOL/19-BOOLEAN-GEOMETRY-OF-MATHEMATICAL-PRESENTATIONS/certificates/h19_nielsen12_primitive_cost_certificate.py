#!/usr/bin/env python3
"""H19-01: decompose the frozen H18-11 shortest Nielsen programmes by primitive.

This certificate deliberately DOES NOT collapse unlike primitives into one
scalar hardware cost.

For the ten primitive restricted-12 observers, H18-11 already certified
shortest elementary-Nielsen programme length.  Here each certified shortest
programme is decomposed into

    (composition moves, inversion moves, swaps, total moves).

The two non-primitive commutator observers remain direct word observers and are
reported separately.

This is a source-structure certificate, not an FPGA cost theorem.
"""

from __future__ import annotations

import importlib.util
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve()
H19 = HERE.parents[1]
HATTER = H19.parent
H18 = HATTER / "18-ADAPTIVE-WORD-TOMOGRAPHY"
SRC = H18 / "certificates" / "h18_restricted12_controller_certificate.py"

spec = importlib.util.spec_from_file_location("h18_r12", SRC)
assert spec is not None and spec.loader is not None
r12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r12)

PRIMITIVE = r12.PRIMITIVE
PROGRAMS = r12.PROGRAMS
WORDS = r12.WORDS

COMPOSE_OPS = {"N_A+", "N_A-", "N_B+", "N_B-"}
INVERSE_OPS = {"I_A", "I_B"}
SWAP_OPS = {"S"}


def vector(program):
    ops = tuple(program)
    return {
        "compose": sum(op in COMPOSE_OPS for op in ops),
        "inverse": sum(op in INVERSE_OPS for op in ops),
        "swap": sum(op in SWAP_OPS for op in ops),
        "moves": len(ops),
    }


rows = {}
for word in PRIMITIVE:
    length, coordinate, program, final_pair = PROGRAMS[word]
    v = vector(program)
    assert v["moves"] == length
    rows[word] = {
        **v,
        "coordinate": coordinate,
        "program": tuple(program),
        "final_pair": final_pair,
        "direct_compositions": len(word) - 1,
    }

totals = {
    k: sum(row[k] for row in rows.values())
    for k in ("compose", "inverse", "swap", "moves", "direct_compositions")
}

# Frozen H18-11 shortest-move lengths.
assert {w: rows[w]["moves"] for w in PRIMITIVE} == r12.EXPECTED_NIELSEN_LENGTH
assert Counter(
    rows[w]["moves"] - rows[w]["direct_compositions"] for w in PRIMITIVE
) == Counter({0: 7, 1: 3})

# The two commutator labels are not primitive basis coordinates.
COMMUTATORS = ("ABab", "AbaB")
assert set(WORDS) - set(PRIMITIVE) == set(COMMUTATORS)
commutator_direct_compositions = sum(len(w) - 1 for w in COMMUTATORS)
assert commutator_direct_compositions == 6


def main() -> None:
    print("H19 Nielsen12 primitive-cost certificate")
    for word in PRIMITIVE:
        row = rows[word]
        print(
            word,
            "direct_comp=", row["direct_compositions"],
            "nielsen_vector=",
            (row["compose"], row["inverse"], row["swap"], row["moves"]),
            "program=", row["program"],
            "coord=", row["coordinate"],
        )

    print("primitive totals =", totals)
    print("commutator direct compositions =", commutator_direct_compositions)
    print(
        "IMPORTANT: shortest Nielsen move count and direct composition count "
        "are not one physical cost metric."
    )
    print("PASS")


if __name__ == "__main__":
    main()
