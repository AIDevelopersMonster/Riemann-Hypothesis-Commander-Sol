#!/usr/bin/env python3
"""Generate H17-08 closure-aware robust8 RTL on the H17-07 14-compose DAG."""
from __future__ import annotations

import argparse
from pathlib import Path

from generate_psl27_robust8 import PROBES, emit_core, emit_decoder, emit_tb, verify
from generate_psl27_robust8_dag import DAG
from generate_psl27_closure_classifiers import MEMBERSHIP_SV, MEMBER_CLASS_SV


def emit_engine(path: Path):
    lines = [
        "// H17-08 closure-aware robust8 engine: 2 raw membership checks + 8 member-class decoders.",
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
        "logic vA,vB;",
    ]
    for w, _, _ in DAG:
        lines.append(f"logic [23:0] n_{w};")
    for i in range(8):
        lines.append(f"logic [2:0] c{i};")
    lines += [
        "always_comb begin",
        "  invA=inverse_perm(A); invB=inverse_perm(B);",
    ]
    for w, l, r in DAG:
        le = l if l in ("A", "B", "invA", "invB") else f"n_{l}"
        re = r if r in ("A", "B", "invA", "invB") else f"n_{r}"
        lines.append(f"  n_{w}=compose_perm({le},{re}); // {w}")
    lines += [
        "  signature={c0,c1,c2,c3,c4,c5,c6,c7};",
        "  valid=vA&vB;",
        "end",
        "psl27_membership_only uA(.perm(A),.valid(vA));",
        "psl27_membership_only uB(.perm(B),.valid(vB));",
    ]
    for i, w in enumerate(PROBES):
        lines.append(f"psl27_member_class_only u{i}(.perm(n_{w}),.class_code(c{i}));")
    lines += ["endmodule", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',default='generated_closure8'); args=ap.parse_args()
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    gen, non=verify()
    (out/'psl27_membership_only.sv').write_text(MEMBERSHIP_SV,encoding='utf-8')
    (out/'psl27_member_class_only.sv').write_text(MEMBER_CLASS_SV,encoding='utf-8')
    emit_engine(out/'psl27_robust8_engine.sv')
    emit_decoder(out/'psl27_robust8_decoder.sv',gen)
    emit_core(out/'psl27_robust8_core.sv')
    emit_tb(out/'tb_psl27_robust8_core.sv',gen,non)
    print('PASS: emitted H17-08 closure-aware robust8 processor')
    print('word compositions =',len(DAG))
    print('raw membership engines = 2; derived member-class engines = 8')

if __name__=='__main__': main()
