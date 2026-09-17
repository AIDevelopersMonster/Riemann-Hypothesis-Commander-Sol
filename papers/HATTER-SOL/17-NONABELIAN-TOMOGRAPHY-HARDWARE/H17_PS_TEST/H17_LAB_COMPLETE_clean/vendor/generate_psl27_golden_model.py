#!/usr/bin/env python3
"""HATTER-SOL-17 H17-01: canonical PSL(2,7) golden model + ROM generator.

This generator is the implementation handoff from the closed HATTER-SOL-16
short-word tomography theorem.

It constructs PSL(2,7) exactly in its action on P^1(F_7), finds the 114
simultaneous-conjugacy orbits of generating pairs, assigns deterministic
canonical orbit IDs, evaluates the five proved probes

    A, B, AB, AB^{-1}, [A,B],

and emits:
  * a machine-readable CSV golden table,
  * a complete 114-entry SystemVerilog orbit ROM,
  * an exhaustive 114-vector SystemVerilog ROM testbench.

No floating point, Mahler quadrature, or heuristic classification is used.
"""

from __future__ import annotations

import argparse
import csv
from collections import deque
from itertools import product
from pathlib import Path

P = 7
N = 8
INF = 7
ID = tuple(range(N))

PROBES = ("A", "B", "AB", "Ab", "ABab")
CLASS_NAMES = ("1A", "2A", "3A", "4A", "7A", "7B")
CLASS_CODE = {name: i for i, name in enumerate(CLASS_NAMES)}


def invmod(a: int) -> int:
    return pow(a, P - 2, P)


def mobius_perm(a: int, b: int, c: int, d: int) -> tuple[int, ...]:
    out = []
    for x in range(P):
        den = (c * x + d) % P
        num = (a * x + b) % P
        out.append(INF if den == 0 else (num * invmod(den)) % P)
    out.append(INF if c % P == 0 else (a * invmod(c)) % P)
    return tuple(out)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p o q."""
    return tuple(p[q[i]] for i in range(N))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * N
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def build_group() -> list[tuple[int, ...]]:
    gset = set()
    for a, b, c, d in product(range(P), repeat=4):
        if (a * d - b * c) % P == 1:
            gset.add(mobius_perm(a, b, c, d))
    group = sorted(gset)
    assert len(group) == 168
    return group


G = build_group()
INV = {g: inverse(g) for g in G}


def conjugate(h, g):
    return compose(compose(h, g), INV[h])


def subgroup(a, b):
    seen = {ID}
    q = deque([ID])
    gens = (a, b, INV[a], INV[b])
    while q:
        x = q.popleft()
        for g in gens:
            y = compose(x, g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen


def element_order(g):
    x = ID
    for n in range(1, 169):
        x = compose(x, g)
        if x == ID:
            return n
    raise AssertionError("order overflow")


def canonical_generating_pair_reps():
    """Return deterministic representatives of the 114 generating-pair orbits."""
    unseen = {(a, b) for a in G for b in G}
    reps = []
    while unseen:
        a, b = min(unseen)
        orbit = {(conjugate(h, a), conjugate(h, b)) for h in G}
        unseen -= orbit
        if len(subgroup(a, b)) == 168:
            assert len(orbit) == 168
            reps.append(min(orbit))
    reps.sort()
    assert len(reps) == 114
    return reps


def build_conjugacy_classes():
    unseen = set(G)
    classes = []
    while unseen:
        g = min(unseen)
        cls = {conjugate(h, g) for h in G}
        classes.append(cls)
        unseen -= cls
    classes.sort(key=lambda cls: (element_order(next(iter(cls))), min(cls)))
    assert [len(c) for c in classes] == [1, 21, 56, 42, 24, 24]
    class_of = {
        g: name
        for name, cls in zip(CLASS_NAMES, classes)
        for g in cls
    }
    return classes, class_of


CLASSES, CLASS_OF = build_conjugacy_classes()
REPS = canonical_generating_pair_reps()


def eval_word(word, a, b):
    table = {"A": a, "a": INV[a], "B": b, "b": INV[b]}
    g = ID
    for c in word:
        g = compose(g, table[c])
    return g


def class_signature(a, b):
    return tuple(CLASS_OF[eval_word(w, a, b)] for w in PROBES)


def signature_code(sig):
    value = 0
    for name in sig:
        value = (value << 3) | CLASS_CODE[name]
    return value


def build_rows():
    rows = []
    signatures = set()
    for orbit_id, (a, b) in enumerate(REPS):
        sig = class_signature(a, b)
        code = signature_code(sig)
        assert sig not in signatures
        signatures.add(sig)
        rows.append(
            {
                "orbit_id": orbit_id,
                "signature_hex": f"{code:04x}",
                "signature_bin": f"{code:015b}",
                "class_A": sig[0],
                "class_B": sig[1],
                "class_AB": sig[2],
                "class_AB_inv": sig[3],
                "class_K": sig[4],
                "q4_orientation": (
                    "+1" if sig[4] == "7A"
                    else "-1" if sig[4] == "7B"
                    else "0"
                ),
                "rep_A": " ".join(map(str, a)),
                "rep_B": " ".join(map(str, b)),
            }
        )
    assert len(rows) == 114
    assert len(signatures) == 114
    return rows


def write_csv(rows, path: Path):
    fields = [
        "orbit_id",
        "signature_hex",
        "signature_bin",
        "class_A",
        "class_B",
        "class_AB",
        "class_AB_inv",
        "class_K",
        "q4_orientation",
        "rep_A",
        "rep_B",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_sv_rom(rows, path: Path):
    lines = [
        "// Auto-generated by generate_psl27_golden_model.py. Do not edit by hand.",
        "// Complete H17-01 114-orbit decoder for the H16 five-probe signature.",
        "module psl27_orbit_rom(",
        "    input  logic [14:0] signature,",
        "    output logic        valid,",
        "    output logic [6:0]  orbit_id,",
        "    output logic [1:0]  q4_orientation",
        ");",
        "",
        "always_comb begin",
        "    valid = 1'b1;",
        "    orbit_id = 7'h7f;",
        "    q4_orientation = 2'b00;",
        "    unique case (signature)",
    ]
    for r in rows:
        q4 = (
            "2'b01" if r["class_K"] == "7A"
            else "2'b10" if r["class_K"] == "7B"
            else "2'b00"
        )
        lines.append(
            f"        15'b{r['signature_bin']}: begin orbit_id = 7'd{r['orbit_id']}; "
            f"q4_orientation = {q4}; end"
        )
    lines += [
        "        default: begin",
        "            valid = 1'b0;",
        "            orbit_id = 7'h7f;",
        "            q4_orientation = 2'b00;",
        "        end",
        "    endcase",
        "end",
        "",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def write_sv_tb(rows, path: Path):
    lines = [
        "`timescale 1ns/1ps",
        "// Auto-generated exhaustive ROM testbench: all 114 canonical signatures.",
        "module tb_psl27_orbit_rom;",
        "    logic [14:0] signature;",
        "    logic valid;",
        "    logic [6:0] orbit_id;",
        "    logic [1:0] q4_orientation;",
        "",
        "    psl27_orbit_rom dut(",
        "        .signature(signature),",
        "        .valid(valid),",
        "        .orbit_id(orbit_id),",
        "        .q4_orientation(q4_orientation)",
        "    );",
        "",
        "    task automatic check(",
        "        input logic [14:0] sig,",
        "        input logic [6:0] expected_id,",
        "        input logic [1:0] expected_q4",
        "    );",
        "    begin",
        "        signature = sig;",
        "        #1;",
        "        if (!valid || orbit_id !== expected_id || q4_orientation !== expected_q4) begin",
        "            $display(\"FAIL sig=%015b got valid=%b orbit=%0d q4=%b expected orbit=%0d q4=%b\",",
        "                     sig, valid, orbit_id, q4_orientation, expected_id, expected_q4);",
        "            $fatal(1);",
        "        end",
        "    end",
        "    endtask",
        "",
        "    initial begin",
    ]
    for r in rows:
        q4 = (
            "2'b01" if r["class_K"] == "7A"
            else "2'b10" if r["class_K"] == "7B"
            else "2'b00"
        )
        lines.append(
            f"        check(15'b{r['signature_bin']}, 7'd{r['orbit_id']}, {q4});"
        )
    lines += [
        "        signature = 15'b111_111_111_111_111;",
        "        #1;",
        "        if (valid) begin",
        "            $display(\"FAIL invalid signature accepted\");",
        "            $fatal(1);",
        "        end",
        "        $display(\"PASS: all 114 canonical H17-01 ROM vectors matched\");",
        "        $finish;",
        "    end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        default="generated",
        help="Output directory for CSV and SystemVerilog files.",
    )
    args = parser.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    write_csv(rows, out / "psl27_114_orbit_signatures.csv")
    write_sv_rom(rows, out / "psl27_orbit_rom.sv")
    write_sv_tb(rows, out / "tb_psl27_orbit_rom.sv")

    print("HATTER-SOL-17 H17-01 canonical golden model")
    print("group order =", len(G))
    print("generating-pair orbits =", len(REPS))
    print("five probes =", PROBES)
    print("unique five-probe signatures =", len({class_signature(a, b) for a, b in REPS}))
    print("PASS: deterministic 114-orbit golden model and ROM emitted")


if __name__ == "__main__":
    main()
