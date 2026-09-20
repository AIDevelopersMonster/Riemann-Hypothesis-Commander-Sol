#!/usr/bin/env python3
"""Generate H19 E0-equivalent restricted-12 one-cycle RTL variants.

The frozen H18-11 305-node decision DAG, fault interface, output encoding and
registered shell remain identical. Only the mathematical factorization of the
12 observer words changes:

  direct12  -- independent direct word chains;
  prefix19  -- shared prefix DAG;
  nielsen12 -- shortest elementary Nielsen programs for ten primitive words,
               direct realization for the two oriented commutators.

The variants are intended for exact E0 regression and matched synthesis.
"""

from __future__ import annotations

import argparse
import importlib.util
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
HATTER = HERE.parents[2]
H18 = HATTER / "18-ADAPTIVE-WORD-TOMOGRAPHY"
CERT = H18 / "certificates" / "h18_restricted12_controller_certificate.py"

spec = importlib.util.spec_from_file_location("h18_r12_cert", CERT)
assert spec is not None and spec.loader is not None
r12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r12)

QUERY_COUNT = 305
assert len(r12.nodes) == QUERY_COUNT
assert r12.PRE == 67
assert r12.POST == 238

WORDS = tuple(sorted(r12.WORDS, key=lambda w: (len(w), w)))
WORD_ID = {w: i for i, w in enumerate(WORDS)}
assert len(WORDS) == 12

STATUS_INVALID = 0
STATUS_REJECT = 1
STATUS_IDENTIFIED = 2
STATUS_FAULT = 4
INVALID_ORBIT = 127


def target_expr(target) -> str:
    kind, payload = target
    if kind == r12.NODE_KIND:
        return f"node_result_{payload}"
    if kind == r12.ORBIT_KIND:
        return f"{{3'd{STATUS_IDENTIFIED},7'd{payload}}}"
    if kind == r12.REJECT_KIND:
        return f"{{3'd{STATUS_REJECT},7'd{INVALID_ORBIT}}}"
    return f"{{3'd{STATUS_FAULT},7'd{INVALID_ORBIT}}}"


def child_nodes(node):
    out = []
    for t in node["targets"]:
        if t[0] == r12.NODE_KIND:
            out.append(t[1])
    if node["mode"] == "pre-erasure":
        t = node["erasure_target"]
        if t[0] == r12.NODE_KIND:
            out.append(t[1])
    return out


def graph_depth() -> int:
    visiting = set()

    @lru_cache(maxsize=None)
    def depth(nid: int) -> int:
        if nid in visiting:
            raise AssertionError(f"decision graph cycle at node {nid}")
        visiting.add(nid)
        kids = child_nodes(r12.nodes[nid])
        d = 1 if not kids else 1 + max(depth(k) for k in kids)
        visiting.remove(nid)
        return d

    return depth(0)


MAX_DAG_QUERY_DEPTH = graph_depth()
assert MAX_DAG_QUERY_DEPTH == 5


def prefix_dag():
    prefixes = set()
    for word in WORDS:
        for k in range(2, len(word) + 1):
            prefixes.add(word[:k])
    ordered = sorted(prefixes, key=lambda w: (len(w), w))
    return ordered


PREFIXES = prefix_dag()
assert len(PREFIXES) == 19
assert max(len(p) - 1 for p in PREFIXES) == 3


def perm_expr(word: str) -> str:
    if word == "A":
        return "A"
    if word == "B":
        return "B"
    if word == "a":
        return "invA"
    if word == "b":
        return "invB"
    return f"p_{word}"



def emit_word_realization(lines, mode: str, keep_intermediates: bool = False, module_primitives: bool = False):
    """Emit one of three E0-equivalent observer factorizations.

    Returns a dict word -> SystemVerilog expression carrying exactly that word
    permutation.
    """
    a = lines.append
    out = {}
    wire_kw = "(* keep *) wire" if keep_intermediates else "wire"

    def letter_expr(ch: str) -> str:
        return {"A": "A", "B": "B", "a": "invA", "b": "invB"}[ch]

    def emit_comp(name: str, p: str, q: str) -> str:
        if module_primitives:
            a(f"wire [23:0] {name};")
            a(f"(* keep_hierarchy *) h19_compose_perm u_{name}(.p({p}),.q({q}),.r({name}));")
        else:
            a(f"{wire_kw} [23:0] {name} = compose_perm({p}, {q});")
        return name

    def emit_inv(name: str, p: str) -> str:
        if module_primitives:
            a(f"wire [23:0] {name};")
            a(f"(* keep_hierarchy *) h19_inverse_perm u_{name}(.p({p}),.r({name}));")
        else:
            a(f"{wire_kw} [23:0] {name} = inverse_perm({p});")
        return name

    def emit_direct(word: str, tag: str) -> str:
        if len(word) == 1:
            return letter_expr(word)
        cur = letter_expr(word[0])
        for k, ch in enumerate(word[1:], start=1):
            name = f"{tag}_{k}"
            cur = emit_comp(name, cur, letter_expr(ch))
        return cur

    if mode == "prefix19":
        for pref in PREFIXES:
            parent = pref[:-1]
            last = pref[-1]
            emit_comp(f"p_{pref}", perm_expr(parent), perm_expr(last))
        for word in WORDS:
            out[word] = perm_expr(word)
        return out

    if mode == "direct12":
        for wid, word in enumerate(WORDS):
            out[word] = emit_direct(word, f"d{wid}")
        return out

    if mode == "nielsen12":
        # Primitive observers use the exact shortest elementary Nielsen
        # programmes certified in H18-11.  The two oriented commutators remain
        # direct in this first mixed presentation.
        for wid, word in enumerate(WORDS):
            if word in ("ABab", "AbaB"):
                out[word] = emit_direct(word, f"c{wid}")
                continue

            length, coordinate, program, final_pair = r12.PROGRAMS[word]
            u = "A"
            v = "B"
            for step, op in enumerate(program):
                if op == "S":
                    u, v = v, u
                elif op == "I_A":
                    nu = f"n{wid}_{step}_u"
                    emit_inv(nu, u)
                    u = nu
                elif op == "I_B":
                    nv = f"n{wid}_{step}_v"
                    emit_inv(nv, v)
                    v = nv
                elif op == "N_A+":
                    nu = f"n{wid}_{step}_u"
                    emit_comp(nu, u, v)
                    u = nu
                elif op == "N_A-":
                    iv = f"n{wid}_{step}_iv"
                    nu = f"n{wid}_{step}_u"
                    emit_inv(iv, v)
                    emit_comp(nu, u, iv)
                    u = nu
                elif op == "N_B+":
                    nv = f"n{wid}_{step}_v"
                    emit_comp(nv, v, u)
                    v = nv
                elif op == "N_B-":
                    iu = f"n{wid}_{step}_iu"
                    nv = f"n{wid}_{step}_v"
                    emit_inv(iu, u)
                    emit_comp(nv, v, iu)
                    v = nv
                else:
                    raise AssertionError(op)

            expr = u if coordinate == 0 else v
            assert final_pair[coordinate] == word
            assert length == len(program)
            out[word] = expr
        return out

    raise ValueError(f"unknown realization mode: {mode}")


def emit_core(path: Path, mode: str, keep_intermediates: bool = False, module_primitives: bool = False) -> None:
    lines = []
    a = lines.append

    a("// Auto-generated H19 restricted-12 E0 comparison core.")
    a("// Exact H18-11 decision DAG; observer factorization selected by generator mode.")
    if module_primitives:
        a("(* keep_hierarchy *) module h19_compose_perm(input logic [23:0] p, input logic [23:0] q, output logic [23:0] r);")
        a("  function automatic [2:0] gp(input logic [23:0] x, input integer idx); gp=x[idx*3 +: 3]; endfunction")
        a("  integer i; logic [2:0] qi;")
        a("  always @* begin r='0; for(i=0;i<8;i=i+1) begin qi=gp(q,i); r[i*3 +:3]=gp(p,qi); end end")
        a("endmodule")
        a("")
        a("(* keep_hierarchy *) module h19_inverse_perm(input logic [23:0] p, output logic [23:0] r);")
        a("  function automatic [2:0] gp(input logic [23:0] x, input integer idx); gp=x[idx*3 +: 3]; endfunction")
        a("  integer i; logic [2:0] pi;")
        a("  always @* begin r='0; for(i=0;i<8;i=i+1) begin pi=gp(p,i); r[pi*3 +:3]=i[2:0]; end end")
        a("endmodule")
        a("")
    a("module h18_r12_comb_core(")
    a("    input  logic [23:0] A,")
    a("    input  logic [23:0] B,")
    a("    input  logic        erase_valid,")
    a("    input  logic [3:0]  erased_word_id,")
    a("    output logic        input_valid,")
    a("    output logic        identified,")
    a("    output logic        rejected,")
    a("    output logic [2:0]  status,")
    a("    output logic [6:0]  orbit_id")
    a(");")
    a("")
    a("function automatic [2:0] getp(input logic [23:0] p, input integer idx);")
    a("  getp = p[idx*3 +: 3];")
    a("endfunction")
    a("")
    a("function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);")
    a("  integer i; logic [23:0] rr; logic [2:0] qi;")
    a("  begin")
    a("    rr='0;")
    a("    for(i=0;i<8;i=i+1) begin")
    a("      qi=getp(q,i);")
    a("      rr[i*3 +:3]=getp(p,qi);")
    a("    end")
    a("    compose_perm=rr;")
    a("  end")
    a("endfunction")
    a("")
    a("function automatic [23:0] inverse_perm(input logic [23:0] p);")
    a("  integer i; logic [23:0] rr; logic [2:0] pi;")
    a("  begin")
    a("    rr='0;")
    a("    for(i=0;i<8;i=i+1) begin")
    a("      pi=getp(p,i);")
    a("      rr[pi*3 +:3]=i[2:0];")
    a("    end")
    a("    inverse_perm=rr;")
    a("  end")
    a("endfunction")
    a("")
    a("wire valid_A, valid_B;")
    if module_primitives:
        a("wire [23:0] invA, invB;")
        a("(* keep_hierarchy *) h19_inverse_perm u_invA(.p(A),.r(invA));")
        a("(* keep_hierarchy *) h19_inverse_perm u_invB(.p(B),.r(invB));")
    else:
        a("wire [23:0] invA = inverse_perm(A);")
        a("wire [23:0] invB = inverse_perm(B);")
    a("psl27_membership_only u_mem_A(.perm(A),.valid(valid_A));")
    a("psl27_membership_only u_mem_B(.perm(B),.valid(valid_B));")
    a("")

    word_expr = emit_word_realization(lines, mode, keep_intermediates, module_primitives)
    a("")

    for wid, word in enumerate(WORDS):
        a(f"wire [2:0] class_{wid}; // {word}")
        a(f"psl27_member_class_only u_class_{wid}(.perm({word_expr[word]}),.class_code(class_{wid}));")
    a("")

    for nid in range(QUERY_COUNT):
        a(f"wire [9:0] node_result_{nid};")
    a("")

    for nid, node in enumerate(r12.nodes):
        wid = WORD_ID[node["word"]]
        cls = f"class_{wid}"
        targets = [target_expr(t) for t in node["targets"]]
        class_expr = (
            f"({cls}==3'd0) ? {targets[0]} : "
            f"({cls}==3'd1) ? {targets[1]} : "
            f"({cls}==3'd2) ? {targets[2]} : "
            f"({cls}==3'd3) ? {targets[3]} : "
            f"({cls}==3'd4) ? {targets[4]} : "
            f"({cls}==3'd5) ? {targets[5]} : "
            f"{{3'd{STATUS_FAULT},7'd{INVALID_ORBIT}}}"
        )
        if node["mode"] == "pre-erasure":
            erase_expr = target_expr(node["erasure_target"])
            expr = (
                f"(erase_valid && erased_word_id==4'd{wid}) ? "
                f"{erase_expr} : ({class_expr})"
            )
        else:
            expr = class_expr
        a(f"assign node_result_{nid} = {expr};")
    a("")

    a("always @* begin")
    a("  input_valid = valid_A & valid_B;")
    a(f"  status = 3'd{STATUS_INVALID};")
    a(f"  orbit_id = 7'd{INVALID_ORBIT};")
    a("  if (input_valid) begin")
    a("    status = node_result_0[9:7];")
    a("    orbit_id = node_result_0[6:0];")
    a("  end")
    a("  identified = (status == 3'd2);")
    a("  rejected = (status == 3'd1);")
    a("end")
    a("endmodule")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_wrapper(path: Path) -> None:
    path.write_text(r'''// H18-LAB-04 registered wrapper: one full combinational result cycle.
module h18_r12_comb_controller(
    input  logic        clk,
    input  logic        rst,
    input  logic        start,
    input  logic [23:0] A_in,
    input  logic [23:0] B_in,
    input  logic        erase_valid,
    input  logic [3:0]  erased_word_id,
    output logic        busy,
    output logic        done,
    output logic        input_valid,
    output logic        identified,
    output logic        rejected,
    output logic [2:0]  status,
    output logic [6:0]  orbit_id
);

logic [23:0] A_q, B_q;
logic erase_valid_q;
logic [3:0] erased_word_id_q;
logic pending;

wire core_input_valid, core_identified, core_rejected;
wire [2:0] core_status;
wire [6:0] core_orbit_id;

h18_r12_comb_core u_core(
    .A(A_q),.B(B_q),
    .erase_valid(erase_valid_q),
    .erased_word_id(erased_word_id_q),
    .input_valid(core_input_valid),
    .identified(core_identified),
    .rejected(core_rejected),
    .status(core_status),
    .orbit_id(core_orbit_id)
);

always_ff @(posedge clk) begin
  if (rst) begin
    A_q <= 0;
    B_q <= 0;
    erase_valid_q <= 0;
    erased_word_id_q <= 0;
    pending <= 0;
    busy <= 0;
    done <= 0;
    input_valid <= 0;
    identified <= 0;
    rejected <= 0;
    status <= 0;
    orbit_id <= 7'h7f;
  end else begin
    done <= 0;

    if (!busy && start) begin
      A_q <= A_in;
      B_q <= B_in;
      erase_valid_q <= erase_valid;
      erased_word_id_q <= erased_word_id;
      pending <= 1;
      busy <= 1;

      input_valid <= 0;
      identified <= 0;
      rejected <= 0;
      status <= 0;
      orbit_id <= 7'h7f;
    end else if (pending) begin
      input_valid <= core_input_valid;
      identified <= core_identified;
      rejected <= core_rejected;
      status <= core_status;
      orbit_id <= core_orbit_id;
      pending <= 0;
      busy <= 0;
      done <= 1;
    end
  end
end
endmodule
''', encoding="utf-8")


def pack_perm(p) -> int:
    value = 0
    for i, x in enumerate(p):
        value |= x << (3 * i)
    return value


def emit_vectors(path: Path) -> None:
    h17_id = {rep: i for i, rep in enumerate(r12.c.h17.REPS)}
    lines = ["# A B expected_status expected_orbit"]
    for state, (aa, bb) in enumerate(r12.c.REPS):
        if r12.c.IS_GENERATING[state]:
            st = STATUS_IDENTIFIED
            oid = h17_id[(aa, bb)]
        else:
            st = STATUS_REJECT
            oid = INVALID_ORBIT
        lines.append(f"{pack_perm(aa):06x} {pack_perm(bb):06x} {st:x} {oid:02x}")
    assert len(lines) == 198
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_tb(path: Path) -> None:
    path.write_text(r'''module tb_h18_r12_comb_controller;
logic clk=0,rst=1,start=0,erase_valid=0;
logic [23:0] A_in=0,B_in=0;
logic [3:0] erased_word_id=0;
logic busy,done,input_valid,identified,rejected;
logic [2:0] status;
logic [6:0] orbit_id;

h18_r12_comb_controller dut(
 .clk(clk),.rst(rst),.start(start),.A_in(A_in),.B_in(B_in),
 .erase_valid(erase_valid),.erased_word_id(erased_word_id),
 .busy(busy),.done(done),.input_valid(input_valid),
 .identified(identified),.rejected(rejected),
 .status(status),.orbit_id(orbit_id)
);

always #5 clk=~clk;

integer fd,rc,n,total_runs,eid;
reg [1023:0] file_name;
reg [23:0] ea,eb;
reg [3:0] es;
reg [7:0] eoid;

task automatic launch_and_check(input integer ev, input integer wid);
begin
  @(negedge clk);
  A_in=ea; B_in=eb;
  erase_valid=ev[0];
  erased_word_id=wid[3:0];
  start=1;

  @(negedge clk);
  start=0;

  // Inputs are already latched; corrupt external pins while the core settles.
  A_in=24'h000000;
  B_in=24'hffffff;
  erase_valid=0;
  erased_word_id=4'hf;

  @(negedge clk);

  if(!done) $fatal(1,"done missing vector=%0d ev=%0d wid=%0d",n,ev,wid);
  if(busy) $fatal(1,"busy stuck vector=%0d ev=%0d wid=%0d",n,ev,wid);
  if(status!==es[2:0] || orbit_id!==eoid[6:0])
    $fatal(1,
      "mismatch vector=%0d ev=%0d wid=%0d expected status=%h orbit=%h got status=%h orbit=%h",
      n,ev,wid,es,eoid,status,orbit_id);

  if(es==4'h2 && (!identified || rejected))
    $fatal(1,"identified flags mismatch vector=%0d",n);
  if(es==4'h1 && (!rejected || identified))
    $fatal(1,"reject flags mismatch vector=%0d",n);

  @(negedge clk);
  if(done) $fatal(1,"done is not a one-cycle pulse vector=%0d",n);

  total_runs=total_runs+1;
end
endtask

initial begin
  repeat(3) @(negedge clk);
  rst=0;

  if(!$value$plusargs("VECTORS=%s",file_name))
    file_name="h18_r12_comb_vectors.txt";

  fd=$fopen(file_name,"r");
  if(!fd) $fatal(1,"vectors missing: %0s",file_name);
  rc=$fgets(file_name,fd);

  n=0; total_runs=0;
  while(!$feof(fd)) begin
    rc=$fscanf(fd,"%h %h %h %h\n",ea,eb,es,eoid);
    if(rc==4) begin
      launch_and_check(0,0);
      for(eid=0;eid<12;eid=eid+1)
        launch_and_check(1,eid);
      n=n+1;
    end
  end
  $fclose(fd);

  if(n!=197) $fatal(1,"expected 197 states, got %0d",n);
  if(total_runs!=2561) $fatal(1,"expected 2561 runs, got %0d",total_runs);

  $display("PASS H18-LAB-04 comb: %0d states x 13 erasure identities = %0d runs; one registered result cycle",
    n,total_runs);
  $finish;
end

initial begin
  #1000000000;
  $fatal(1,"watchdog");
end
endmodule
''', encoding="utf-8")


def emit_summary(path: Path, mode: str) -> None:
    path.write_text(
        "# H19 generated E0-equivalent combinational architecture\n\n"
        f"- observer realization mode: {mode}\n"
        f"- exact H18-11 decision nodes: {QUERY_COUNT}\n"
        f"- pre/post nodes: {r12.PRE}/{r12.POST}\n"
        f"- supported query labels: {len(WORDS)}\n"
        f"- words: {', '.join(WORDS)}\n"
        f"- shared prefix-DAG permutation compositions: {len(PREFIXES)}\n"
        f"- maximum prefix-DAG composition depth: {max(len(p)-1 for p in PREFIXES)}\n"
        f"- maximum compiled decision-DAG query depth including one erasure: {MAX_DAG_QUERY_DEPTH}\n"
        "- target wrapper latency: one registered result cycle\n"
        "- exhaustive static erasure schedules: 197 x (no erasure + 12 erased identities) = 2561\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path("generated_comb"))
    parser.add_argument("--mode", choices=("direct12","prefix19","nielsen12"), default="prefix19")
    parser.add_argument("--keep-intermediates", action="store_true",
                        help="mark declared word-factorization intermediates with Yosys keep")
    parser.add_argument("--module-primitives", action="store_true",
                        help="realize compose/inverse as retained primitive module instances")
    args = parser.parse_args()
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)

    emit_core(out / "h18_r12_comb_core.sv", args.mode, args.keep_intermediates, args.module_primitives)
    emit_wrapper(out / "h18_r12_comb_controller.sv")
    emit_vectors(out / "h18_r12_comb_vectors.txt")
    emit_tb(out / "tb_h18_r12_comb_controller.sv")
    emit_summary(out / "H18_R12_COMB_SUMMARY.md", args.mode)

    print("H19 restricted-12 E0 comparison generator")
    print("mode =", args.mode)
    print("keep_intermediates =", args.keep_intermediates)
    print("module_primitives =", args.module_primitives)
    print("words =", list(WORDS))
    print("shared prefix-DAG compositions =", len(PREFIXES))
    print("maximum word-DAG composition depth =", max(len(p)-1 for p in PREFIXES))
    print("compiled decision-DAG depth =", MAX_DAG_QUERY_DEPTH)
    print("PASS: combinational decision DAG and registered wrapper emitted")


if __name__ == "__main__":
    main()
