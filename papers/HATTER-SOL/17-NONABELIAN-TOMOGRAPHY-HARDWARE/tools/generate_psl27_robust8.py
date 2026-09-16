#!/usr/bin/env python3
"""Generate the HATTER-SOL-17 optimal 8-channel one-erasure RTL bundle.

The observer coordinates are the H17-04 optimum

    AAB, Abb, AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB.

For valid PSL(2,7) ports their class code has d(gen,gen)>=2 and d(gen,non)>=2.
The decoder therefore accepts a known erased coordinate index 0..7, ignores that
coordinate, reconstructs the canonical generating orbit ID, and rejects all
non-generating full-signature states after any one erasure.

H17-05 removes the 168-entry permutation/class ROM.  The emitted bundle uses a
structural classifier based on permutation validity, projective cross-ratios,
PSL orientation, permutation order, and the order-seven orientation invariant.
Only the final signature-to-orbit decoder remains a finite ROM/case table.
"""
from __future__ import annotations

import argparse
from itertools import combinations
from pathlib import Path

from generate_psl27_golden_model import G, REPS, CLASS_CODE, CLASS_OF, eval_word, subgroup
from generate_psl27_port_engine import pack
from generate_psl27_structural_processor import SV as STRUCTURAL_CLASSIFIER_SV

PROBES = ("AAB", "Abb", "AAAB", "Abbb", "AABAb", "AAbAb", "ABABB", "ABaBB")


def full_signature(a, b):
    return tuple(CLASS_OF[eval_word(w, a, b)] for w in PROBES)


def erase_key(sig, erased):
    return tuple(sig[i] for i in range(8) if i != erased)


def verify():
    gen = [full_signature(a, b) for a, b in REPS]
    non = []
    for a in G:
        for b in G:
            if len(subgroup(a, b)) != 168:
                non.append(full_signature(a, b))
    non = list(dict.fromkeys(non))
    assert len(gen) == 114 and len(set(gen)) == 114
    assert len(non) == 66
    dgg = min(sum(x != y for x, y in zip(a, b)) for a, b in combinations(gen, 2))
    dgn = min(sum(x != y for x, y in zip(a, b)) for a in gen for b in non)
    assert dgg == 2 and dgn == 2
    for e in range(8):
        gm = {erase_key(s, e) for s in gen}
        nm = {erase_key(s, e) for s in non}
        assert len(gm) == 114
        assert gm.isdisjoint(nm)
    return gen, non


def compose_expr(word):
    table = {"A": "A", "a": "invA", "B": "B", "b": "invB"}
    e = table[word[0]]
    for c in word[1:]:
        e = f"compose_perm({e},{table[c]})"
    return e


def emit_engine(path: Path):
    lines = [
        "// Auto-generated H17 optimal eight-probe structural word engine.",
        "module psl27_robust8_engine(",
        "    input logic [23:0] A, input logic [23:0] B,",
        "    output logic valid, output logic [23:0] signature",
        ");",
        "function automatic [2:0] getp(input logic [23:0] p, input integer idx);",
        "    getp = p[idx*3 +: 3];",
        "endfunction",
        "function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);",
        "    integer i; logic [23:0] r; logic [2:0] qi;",
        "    begin r='0; for(i=0;i<8;i=i+1) begin qi=getp(q,i); r[i*3 +: 3]=getp(p,qi); end compose_perm=r; end",
        "endfunction",
        "function automatic [23:0] inverse_perm(input logic [23:0] p);",
        "    integer i; logic [23:0] r; logic [2:0] pi;",
        "    begin r='0; for(i=0;i<8;i=i+1) begin pi=getp(p,i); r[pi*3 +: 3]=i[2:0]; end inverse_perm=r; end",
        "endfunction",
        "logic [23:0] invA,invB;",
        "logic vA,vB; logic [2:0] cA_unused,cB_unused;",
    ]
    for i in range(8):
        lines.append(f"logic [23:0] w{i}; logic v{i}; logic [2:0] c{i};")
    lines += ["always_comb begin", "  invA=inverse_perm(A); invB=inverse_perm(B);"]
    for i, w in enumerate(PROBES):
        lines.append(f"  w{i}={compose_expr(w)}; // {w}")
    lines.append("  signature={c0,c1,c2,c3,c4,c5,c6,c7};")
    lines.append("  valid=vA&vB&v0&v1&v2&v3&v4&v5&v6&v7;")
    lines.append("end")
    lines.append("psl27_structural_classify uA(.perm(A),.valid(vA),.class_code(cA_unused));")
    lines.append("psl27_structural_classify uB(.perm(B),.valid(vB),.class_code(cB_unused));")
    for i in range(8):
        lines.append(f"psl27_structural_classify u{i}(.perm(w{i}),.valid(v{i}),.class_code(c{i}));")
    lines += ["endmodule", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def projected_bits(sig, erased):
    return "".join(f"{CLASS_CODE[s]:03b}" for i, s in enumerate(sig) if i != erased)


def emit_decoder(path: Path, gen):
    lines = [
        "// Auto-generated H17 robust decoder. erased_idx is the known missing coordinate 0..7.",
        "module psl27_robust8_decoder(",
        "    input logic [23:0] signature, input logic [2:0] erased_idx,",
        "    output logic valid, output logic [6:0] orbit_id",
        ");",
        "logic [20:0] projected;",
        "always_comb begin",
        "  case(erased_idx)",
        "    3'd0: projected=signature[20:0];",
        "    3'd1: projected={signature[23:21],signature[17:0]};",
        "    3'd2: projected={signature[23:18],signature[14:0]};",
        "    3'd3: projected={signature[23:15],signature[11:0]};",
        "    3'd4: projected={signature[23:12],signature[8:0]};",
        "    3'd5: projected={signature[23:9],signature[5:0]};",
        "    3'd6: projected={signature[23:6],signature[2:0]};",
        "    default: projected=signature[23:3];",
        "  endcase",
        "end",
        "always_comb begin",
        "  valid=1'b1; orbit_id=7'h7f;",
        "  unique case ({erased_idx,projected})",
    ]
    for e in range(8):
        seen = set()
        for oid, sig in enumerate(gen):
            bits = projected_bits(sig, e)
            assert bits not in seen
            seen.add(bits)
            lines.append(f"    {{3'd{e},21'b{bits}}}: orbit_id=7'd{oid};")
        assert len(seen) == 114
    lines += [
        "    default: begin valid=1'b0; orbit_id=7'h7f; end",
        "  endcase",
        "end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def emit_core(path: Path):
    path.write_text("""// H17 optimal eight-channel one-erasure tomography processor.
module psl27_robust8_core(
    input logic [23:0] A, input logic [23:0] B, input logic [2:0] erased_idx,
    output logic input_valid, output logic orbit_valid,
    output logic [6:0] orbit_id, output logic [23:0] signature
);
logic dec_valid;
logic [6:0] decoded_id;
psl27_robust8_engine u_eng(.A(A),.B(B),.valid(input_valid),.signature(signature));
psl27_robust8_decoder u_dec(.signature(signature),.erased_idx(erased_idx),.valid(dec_valid),.orbit_id(decoded_id));
assign orbit_valid=input_valid & dec_valid;
assign orbit_id=orbit_valid ? decoded_id : 7'h7f;
endmodule
""", encoding="utf-8")


def emit_tb(path: Path, gen, non):
    non_rep = {}
    for a in G:
        for b in G:
            if len(subgroup(a, b)) != 168:
                s = full_signature(a, b)
                non_rep.setdefault(s, (a, b))
    assert len(non_rep) == 66
    lines = [
        "`timescale 1ns/1ps",
        "module tb_psl27_robust8_core;",
        "logic [23:0] A,B; logic [2:0] erased_idx;",
        "logic input_valid,orbit_valid; logic [6:0] orbit_id; logic [23:0] signature;",
        "psl27_robust8_core dut(.A(A),.B(B),.erased_idx(erased_idx),.input_valid(input_valid),.orbit_valid(orbit_valid),.orbit_id(orbit_id),.signature(signature));",
        "task automatic check_gen(input logic [23:0] a,input logic [23:0] b,input logic [2:0] e,input logic [6:0] oid); begin A=a;B=b;erased_idx=e;#1;if(!input_valid||!orbit_valid||orbit_id!==oid)$fatal(1);end endtask",
        "task automatic check_non(input logic [23:0] a,input logic [23:0] b,input logic [2:0] e); begin A=a;B=b;erased_idx=e;#1;if(!input_valid||orbit_valid||orbit_id!==7'h7f)$fatal(1);end endtask",
        "initial begin",
    ]
    for oid, (a, b) in enumerate(REPS):
        for e in range(8):
            lines.append(f"check_gen(24'h{pack(a):06x},24'h{pack(b):06x},3'd{e},7'd{oid});")
    for _, (a, b) in sorted(non_rep.items()):
        for e in range(8):
            lines.append(f"check_non(24'h{pack(a):06x},24'h{pack(b):06x},3'd{e});")
    lines += [
        '$display("PASS: robust8 checked 114*8 generating and 66*8 non-generating erasure states");',
        "$finish; end endmodule", "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out-dir", default="generated_robust8"); args = ap.parse_args()
    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    gen, non = verify()
    (out / "psl27_structural_classify.sv").write_text(STRUCTURAL_CLASSIFIER_SV, encoding="utf-8")
    emit_engine(out / "psl27_robust8_engine.sv")
    emit_decoder(out / "psl27_robust8_decoder.sv", gen)
    emit_core(out / "psl27_robust8_core.sv")
    emit_tb(out / "tb_psl27_robust8_core.sv", gen, non)
    print("PASS: H17 robust8 structural processor bundle emitted")
    print("probes =", PROBES)
    print("test states =", 114*8, "generating +", 66*8, "non-generating")
    print("class/membership LUT entries = 0")


if __name__ == "__main__":
    main()
