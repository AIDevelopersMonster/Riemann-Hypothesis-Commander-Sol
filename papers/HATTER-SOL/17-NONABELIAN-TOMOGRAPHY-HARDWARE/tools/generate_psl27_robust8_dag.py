#!/usr/bin/env python3
"""Generate H17 robust8 RTL using the H17-07 optimal 14-compose word DAG."""
from __future__ import annotations

import argparse
from pathlib import Path

from generate_psl27_robust8 import (
    PROBES,
    STRUCTURAL_CLASSIFIER_SV,
    emit_core,
    emit_decoder,
    emit_tb,
    verify,
)

DAG = (
    ("AB", "A", "B"),
    ("Ab", "A", "invB"),
    ("BB", "B", "B"),
    ("AAB", "A", "AB"),
    ("ABA", "AB", "A"),
    ("ABa", "AB", "invA"),
    ("Abb", "Ab", "invB"),
    ("AAAB", "A", "AAB"),
    ("AbAb", "Ab", "Ab"),
    ("Abbb", "Abb", "invB"),
    ("AABAb", "AAB", "Ab"),
    ("AAbAb", "A", "AbAb"),
    ("ABABB", "ABA", "BB"),
    ("ABaBB", "ABa", "BB"),
)


def emit_engine(path: Path):
    lines = [
        "// Auto-generated H17-07 robust8 word engine: 14 shared permutation compositions.",
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
    for w, _, _ in DAG:
        lines.append(f"logic [23:0] n_{w};")
    for i in range(8):
        lines.append(f"logic v{i}; logic [2:0] c{i};")
    lines += [
        "always_comb begin",
        "  invA=inverse_perm(A); invB=inverse_perm(B);",
    ]
    for w, l, r in DAG:
        le = l if l in ("A", "B", "invA", "invB") else f"n_{l}"
        re = r if r in ("A", "B", "invA", "invB") else f"n_{r}"
        lines.append(f"  n_{w}=compose_perm({le},{re}); // {w}")
    outs = [f"n_{w}" for w in PROBES]
    lines += [
        "  signature={c0,c1,c2,c3,c4,c5,c6,c7};",
        "  valid=vA&vB&v0&v1&v2&v3&v4&v5&v6&v7;",
        "end",
        "psl27_structural_classify uA(.perm(A),.valid(vA),.class_code(cA_unused));",
        "psl27_structural_classify uB(.perm(B),.valid(vB),.class_code(cB_unused));",
    ]
    for i, out in enumerate(outs):
        lines.append(f"psl27_structural_classify u{i}(.perm({out}),.valid(v{i}),.class_code(c{i}));")
    lines += ["endmodule", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out-dir", default="generated_robust8"); args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    gen, non=verify()
    (out/"psl27_structural_classify.sv").write_text(STRUCTURAL_CLASSIFIER_SV, encoding="utf-8")
    emit_engine(out/"psl27_robust8_engine.sv")
    emit_decoder(out/"psl27_robust8_decoder.sv", gen)
    emit_core(out/"psl27_robust8_core.sv")
    emit_tb(out/"tb_psl27_robust8_core.sv", gen, non)
    print("PASS: emitted H17-07 optimal-DAG robust8 processor")
    print("word compositions =", len(DAG), "(naive independent =", sum(len(w)-1 for w in PROBES), ")")
    print("class/membership LUT entries = 0")

if __name__=="__main__": main()
