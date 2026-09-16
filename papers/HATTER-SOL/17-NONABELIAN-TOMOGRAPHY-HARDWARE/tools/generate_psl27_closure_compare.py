#!/usr/bin/env python3
"""Generate H17-08 closure-aware hardware as two physically separate SV designs.

The mathematical optimization is

    A,B in PSL(2,7)  =>  w(A,B) in PSL(2,7)

for every probe word w.  Therefore membership is checked exactly twice, on the
raw ports A and B.  The eight internal probe words use a class-only decoder
(order 1/2/3/4/7 plus the existing orientation split for 7A/7B).

The two final architectures are emitted as independent, self-contained files:

  * psl27_closure_flat_core.sv
  * psl27_closure_romfree_core.sv

They deliberately duplicate their frontend module definitions so that a Yosys
run on one file cannot share logic with the other architecture.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from generate_psl27_golden_model import (
    G,
    REPS,
    CLASS_CODE,
    CLASS_OF,
    compose,
    eval_word,
    subgroup,
)
from generate_psl27_port_engine import pack
from generate_psl27_robust8 import PROBES, emit_decoder, full_signature, verify
from generate_psl27_robust8_dag import DAG
from generate_psl27_romfree_repair import emit_repair


MEMBERSHIP_SV = r'''// H17-08: raw-port PSL(2,7) membership only.
module psl27_membership(
    input  logic [23:0] perm,
    output logic        valid
);
function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction
function automatic logic perm_is_bijection(input logic [23:0] p);
    integer i,j; logic ok;
    begin
      ok=1'b1;
      for(i=0;i<8;i=i+1)
        for(j=i+1;j<8;j=j+1) if(getp(p,i)==getp(p,j)) ok=1'b0;
      perm_is_bijection=ok;
    end
endfunction
function automatic [2:0] det_point(input logic [2:0] x,input logic [2:0] y);
    integer t;
    begin
      if(x==3'd7 && y==3'd7) det_point=3'd0;
      else if(x==3'd7) det_point=3'd1;
      else if(y==3'd7) det_point=3'd6;
      else begin
        t=x-y;
        if(t<0) t=t+7;
        det_point=t;
      end
    end
endfunction
function automatic [2:0] mul7(input logic [2:0] a,input logic [2:0] b);
    integer t;
    begin
      t=a*b;
      if(t>=35) t=t-35;
      else if(t>=28) t=t-28;
      else if(t>=21) t=t-21;
      else if(t>=14) t=t-14;
      else if(t>=7) t=t-7;
      mul7=t;
    end
endfunction
function automatic logic orient_pos(input logic [2:0] a,input logic [2:0] b,input logic [2:0] c);
    logic [2:0] v;
    begin
      v=mul7(mul7(det_point(a,b),det_point(b,c)),det_point(c,a));
      orient_pos=(v==3'd1 || v==3'd2 || v==3'd4);
    end
endfunction
function automatic logic pgl_ok(input logic [23:0] p);
    integer x; logic ok; logic [2:0] y0,y1,yi,px,k,lhs,rhs;
    begin
      ok=perm_is_bijection(p); y0=getp(p,0); y1=getp(p,1); yi=getp(p,7);
      for(x=2;x<=6;x=x+1) begin
        px=getp(p,x);
        case(x) 2:k=3'd6; 3:k=3'd5; 4:k=3'd4; 5:k=3'd3; default:k=3'd2; endcase
        lhs=mul7(det_point(px,y1),det_point(y0,yi));
        rhs=mul7(k,mul7(det_point(px,yi),det_point(y0,y1)));
        if(lhs!=rhs) ok=1'b0;
      end
      pgl_ok=ok;
    end
endfunction
always_comb begin
    valid=pgl_ok(perm) & orient_pos(getp(perm,0),getp(perm,1),getp(perm,7));
end
endmodule
'''


MEMBER_CLASSIFIER_SV = r'''// H17-08: class decoder for an already-known PSL(2,7) member.
// No bijection test, no PGL cross-ratio test, no repeated PSL membership test.
module psl27_member_classify(
    input  logic [23:0] perm,
    output logic [2:0]  class_code
);
function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction
function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);
    integer i; logic [23:0] r; logic [2:0] qi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin qi=getp(q,i); r[i*3 +: 3]=getp(p,qi); end
      compose_perm=r;
    end
endfunction
function automatic [2:0] det_point(input logic [2:0] x,input logic [2:0] y);
    integer t;
    begin
      if(x==3'd7 && y==3'd7) det_point=3'd0;
      else if(x==3'd7) det_point=3'd1;
      else if(y==3'd7) det_point=3'd6;
      else begin
        t=x-y;
        if(t<0) t=t+7;
        det_point=t;
      end
    end
endfunction
function automatic [2:0] mul7(input logic [2:0] a,input logic [2:0] b);
    integer t;
    begin
      t=a*b;
      if(t>=35) t=t-35;
      else if(t>=28) t=t-28;
      else if(t>=21) t=t-21;
      else if(t>=14) t=t-14;
      else if(t>=7) t=t-7;
      mul7=t;
    end
endfunction
function automatic logic orient_pos(input logic [2:0] a,input logic [2:0] b,input logic [2:0] c);
    logic [2:0] v;
    begin
      v=mul7(mul7(det_point(a,b),det_point(b,c)),det_point(c,a));
      orient_pos=(v==3'd1 || v==3'd2 || v==3'd4);
    end
endfunction
logic [23:0] p2,p3,p4,p7;
logic is_id,is_o2,is_o3,is_o4,is_o7;
logic [2:0] start,y,z;
integer i;
always_comb begin
    p2=compose_perm(perm,perm);
    p3=compose_perm(p2,perm);
    p4=compose_perm(p2,p2);
    p7=compose_perm(compose_perm(p4,p2),perm);
    is_id =(perm==24'hfac688);
    is_o2 =(!is_id && p2==24'hfac688);
    is_o3 =(!is_id && p3==24'hfac688);
    is_o4 =(!is_id && !is_o2 && p4==24'hfac688);
    is_o7 =(!is_id && p7==24'hfac688);
    start=3'd0;
    for(i=0;i<8;i=i+1) if(getp(perm,i)!=i[2:0]) start=i[2:0];
    y=getp(perm,start); z=getp(perm,y);
    class_code=3'b111;
    if(is_id) class_code=3'd0;
    else if(is_o2) class_code=3'd1;
    else if(is_o3) class_code=3'd2;
    else if(is_o4) class_code=3'd3;
    else if(is_o7) class_code=orient_pos(start,y,z) ? 3'd4 : 3'd5;
end
endmodule
'''


def emit_engine_sv() -> str:
    lines = [
        "// H17-08 closure-aware 14-compose, depth-3 frontend.",
        "module psl27_closure_engine(",
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
        "psl27_membership uA(.perm(A),.valid(vA));",
        "psl27_membership uB(.perm(B),.valid(vB));",
    ]
    for i, w in enumerate(PROBES):
        lines.append(f"psl27_member_classify u{i}(.perm(n_{w}),.class_code(c{i}));")
    lines += ["endmodule", ""]
    return "\n".join(lines)


FLAT_TOP_SV = r'''// H17-08 architecture A: closure-aware frontend + flat orbit-ID decoder.
module psl27_closure_flat_core(
    input logic [23:0] A, input logic [23:0] B, input logic [2:0] erased_idx,
    output logic input_valid, output logic orbit_valid,
    output logic [6:0] orbit_id, output logic [23:0] signature
);
logic dec_valid;
logic [6:0] decoded_id;
psl27_closure_engine u_eng(.A(A),.B(B),.valid(input_valid),.signature(signature));
psl27_robust8_decoder u_dec(.signature(signature),.erased_idx(erased_idx),.valid(dec_valid),.orbit_id(decoded_id));
assign orbit_valid=input_valid & dec_valid;
assign orbit_id=orbit_valid ? decoded_id : 7'h7f;
endmodule
'''


ROMFREE_TOP_SV = r'''// H17-08 architecture B: closure-aware frontend + ROM-free fingerprint repair.
module psl27_closure_romfree_core(
    input  logic [23:0] A,
    input  logic [23:0] B,
    input  logic [2:0]  erased_idx,
    output logic        input_valid,
    output logic        fingerprint_valid,
    output logic [23:0] raw_signature,
    output logic [23:0] orbit_fingerprint
);
logic repair_valid;
psl27_closure_engine u_eng(.A(A),.B(B),.valid(input_valid),.signature(raw_signature));
psl27_robust8_repair u_rep(.signature(raw_signature),.erased_idx(erased_idx),.valid(repair_valid),.repaired_signature(orbit_fingerprint));
assign fingerprint_valid = input_valid & repair_valid;
endmodule
'''


def det_point_py(x: int, y: int) -> int:
    if x == 7 and y == 7:
        return 0
    if x == 7:
        return 1
    if y == 7:
        return 6
    return (x - y) % 7


def orient_pos_py(a: int, b: int, c: int) -> bool:
    v = det_point_py(a, b) * det_point_py(b, c) * det_point_py(c, a) % 7
    return v in (1, 2, 4)


def member_class_code_py(g) -> int:
    identity = tuple(range(8))
    p2 = compose(g, g)
    p3 = compose(p2, g)
    p4 = compose(p2, p2)
    p7 = compose(compose(p4, p2), g)
    if g == identity:
        return 0
    if p2 == identity:
        return 1
    if p3 == identity:
        return 2
    if p4 == identity and p2 != identity:
        return 3
    if p7 == identity:
        start = 0
        for i in range(8):
            if g[i] != i:
                start = i
        y = g[start]
        z = g[y]
        return 4 if orient_pos_py(start, y, z) else 5
    return 7


def pack_signature(sig) -> int:
    value = 0
    for name in sig:
        value = (value << 3) | CLASS_CODE[name]
    return value


def verify_closure_math() -> int:
    for g in G:
        got = member_class_code_py(g)
        expected = CLASS_CODE[CLASS_OF[g]]
        assert got == expected, (g, got, expected, CLASS_OF[g])
    gset = set(G)
    checks = 0
    for a in G:
        for b in G:
            for w in PROBES:
                x = eval_word(w, a, b)
                assert x in gset
                assert member_class_code_py(x) == CLASS_CODE[CLASS_OF[x]]
                checks += 1
    assert checks == 168 * 168 * 8
    return checks


def emit_engine_tb(path: Path):
    lines = [
        "`timescale 1ns/1ps",
        "module tb_psl27_closure_engine;",
        "logic [23:0] A,B; logic valid; logic [23:0] signature;",
        "psl27_closure_engine dut(.A(A),.B(B),.valid(valid),.signature(signature));",
        "task automatic check_pair(input logic [23:0] a,input logic [23:0] b,input logic [23:0] expected); begin",
        "  A=a; B=b; #1; if(!valid || signature!==expected) begin $display(\"FAIL A=%h B=%h got v=%b sig=%h expected=%h\",a,b,valid,signature,expected); $fatal(1); end",
        "end endtask",
        "initial begin",
    ]
    for a in G:
        for b in G:
            lines.append(
                f"  check_pair(24'h{pack(a):06x},24'h{pack(b):06x},24'h{pack_signature(full_signature(a,b)):06x});"
            )
    lines += [
        "  A=24'h000000; B=24'hfac688; #1; if(valid) $fatal(1);",
        '$display("PASS: H17-08 closure engine checked all 168^2 pairs = 28224, i.e. 225792 internal word classifications");',
        "$finish; end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def non_generating_representatives():
    out = {}
    for a in G:
        for b in G:
            if len(subgroup(a, b)) != 168:
                sig = full_signature(a, b)
                out.setdefault(sig, (a, b))
    assert len(out) == 66
    return out


def emit_flat_tb(path: Path):
    non_rep = non_generating_representatives()
    lines = [
        "`timescale 1ns/1ps",
        "module tb_psl27_closure_flat_core;",
        "logic [23:0] A,B; logic [2:0] erased_idx;",
        "logic input_valid,orbit_valid; logic [6:0] orbit_id; logic [23:0] signature;",
        "psl27_closure_flat_core dut(.A(A),.B(B),.erased_idx(erased_idx),.input_valid(input_valid),.orbit_valid(orbit_valid),.orbit_id(orbit_id),.signature(signature));",
        "task automatic check_g(input logic [23:0] a,input logic [23:0] b,input logic [2:0] e,input logic [6:0] oid,input logic [23:0] sig); begin",
        "  A=a;B=b;erased_idx=e;#1;if(!input_valid||!orbit_valid||orbit_id!==oid||signature!==sig)$fatal(1);",
        "end endtask",
        "task automatic check_n(input logic [23:0] a,input logic [23:0] b,input logic [2:0] e,input logic [23:0] sig); begin",
        "  A=a;B=b;erased_idx=e;#1;if(!input_valid||orbit_valid||orbit_id!==7'h7f||signature!==sig)$fatal(1);",
        "end endtask",
        "initial begin",
    ]
    for oid, (a, b) in enumerate(REPS):
        sig = pack_signature(full_signature(a, b))
        for e in range(8):
            lines.append(f"  check_g(24'h{pack(a):06x},24'h{pack(b):06x},3'd{e},7'd{oid},24'h{sig:06x});")
    for sig_names, (a, b) in sorted(non_rep.items()):
        sig = pack_signature(sig_names)
        for e in range(8):
            lines.append(f"  check_n(24'h{pack(a):06x},24'h{pack(b):06x},3'd{e},24'h{sig:06x});")
    lines += [
        '$display("PASS: H17-08 separate flat core checked 912 generating + 528 non-generating erasure states");',
        "$finish; end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def emit_romfree_tb(path: Path):
    non_rep = non_generating_representatives()
    lines = [
        "`timescale 1ns/1ps",
        "module tb_psl27_closure_romfree_core;",
        "logic [23:0] A,B; logic [2:0] erased_idx;",
        "logic input_valid,fingerprint_valid; logic [23:0] raw_signature,orbit_fingerprint;",
        "psl27_closure_romfree_core dut(.A(A),.B(B),.erased_idx(erased_idx),.input_valid(input_valid),.fingerprint_valid(fingerprint_valid),.raw_signature(raw_signature),.orbit_fingerprint(orbit_fingerprint));",
        "task automatic check_g(input logic [23:0] a,input logic [23:0] b,input logic [2:0] e,input logic [23:0] sig); begin",
        "  A=a;B=b;erased_idx=e;#1;if(!input_valid||!fingerprint_valid||raw_signature!==sig||orbit_fingerprint!==sig)$fatal(1);",
        "end endtask",
        "task automatic check_n(input logic [23:0] a,input logic [23:0] b,input logic [2:0] e,input logic [23:0] sig); begin",
        "  A=a;B=b;erased_idx=e;#1;if(!input_valid||fingerprint_valid||raw_signature!==sig)$fatal(1);",
        "end endtask",
        "initial begin",
    ]
    for a, b in REPS:
        sig = pack_signature(full_signature(a, b))
        for e in range(8):
            lines.append(f"  check_g(24'h{pack(a):06x},24'h{pack(b):06x},3'd{e},24'h{sig:06x});")
    for sig_names, (a, b) in sorted(non_rep.items()):
        sig = pack_signature(sig_names)
        for e in range(8):
            lines.append(f"  check_n(24'h{pack(a):06x},24'h{pack(b):06x},3'd{e},24'h{sig:06x});")
    lines += [
        '$display("PASS: H17-08 separate ROM-free core checked 912 generating + 528 non-generating erasure states");',
        "$finish; end",
        "endmodule",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="generated_h17_08")
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    checks = verify_closure_math()
    gen, _ = verify()

    tmp_decoder = out / ".flat_decoder.tmp.sv"
    emit_decoder(tmp_decoder, gen)
    decoder_sv = tmp_decoder.read_text(encoding="utf-8")
    tmp_decoder.unlink()

    tmp_repair = out / ".romfree_repair.tmp.sv"
    solved = emit_repair(tmp_repair)
    repair_sv = tmp_repair.read_text(encoding="utf-8")
    tmp_repair.unlink()

    frontend = MEMBERSHIP_SV + "\n" + MEMBER_CLASSIFIER_SV + "\n" + emit_engine_sv() + "\n"
    (out / "psl27_closure_flat_core.sv").write_text(
        frontend + decoder_sv + "\n" + FLAT_TOP_SV, encoding="utf-8"
    )
    (out / "psl27_closure_romfree_core.sv").write_text(
        frontend + repair_sv + "\n" + ROMFREE_TOP_SV, encoding="utf-8"
    )

    emit_engine_tb(out / "tb_psl27_closure_engine.sv")
    emit_flat_tb(out / "tb_psl27_closure_flat_core.sv")
    emit_romfree_tb(out / "tb_psl27_closure_romfree_core.sv")

    assert len(DAG) == 14
    print("PASS: emitted two physically separate H17-08 synthesis files")
    print("closure proof checks =", checks, "= 168^2 * 8")
    print("raw membership blocks per design = 2")
    print("internal member-class blocks per design = 8")
    print("word compositions =", len(DAG), "; maximum DAG depth = 3")
    print("ROM-free repair worst-case query depth =", max(x[1] for x in solved))
    print("files = psl27_closure_flat_core.sv, psl27_closure_romfree_core.sv")


if __name__ == "__main__":
    main()
