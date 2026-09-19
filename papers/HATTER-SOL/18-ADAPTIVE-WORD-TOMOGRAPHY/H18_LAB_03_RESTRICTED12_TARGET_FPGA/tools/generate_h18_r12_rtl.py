#!/usr/bin/env python3
"""Generate H18-LAB-03 restricted-12 microcoded SystemVerilog RTL.

Source of truth:
  H18-11 exact restricted 12-query controller certificate.

This generator remaps the exact 305 query nodes into a canonical layout:
  * 67 pre-erasure query nodes first;
  * 238 post-erasure query nodes next;
  * orbit terminal k -> 305+k;
  * REJECT -> 419;
  * FAULT / invalid -> 420.

It emits:
  * four ROM images;
  * one SystemVerilog microcoded core;
  * one exhaustive 197-state testbench;
  * one common vector file;
  * JSON and Markdown program summaries.

The mathematical contract is unchanged:
  D0 = 4, S1 = 4, A1 = 5.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve()
LAB = HERE.parents[1]
H18 = LAB.parent
CERT = H18 / "certificates" / "h18_restricted12_controller_certificate.py"

spec = importlib.util.spec_from_file_location("h18_r12_cert", CERT)
assert spec is not None and spec.loader is not None
r12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r12)

QUERY_COUNT = 305
PRE_QUERY_COUNT = 67
POST_QUERY_COUNT = 238
ORBIT_COUNT = 114
ORBIT_BASE = QUERY_COUNT
REJECT_NODE = ORBIT_BASE + ORBIT_COUNT
FAULT_NODE = REJECT_NODE + 1
TOTAL_NODE_COUNT = FAULT_NODE + 1
NODE_W = 9
WORD_ID_W = 4
WORD_COUNT = 12

assert len(r12.nodes) == QUERY_COUNT
assert r12.PRE == PRE_QUERY_COUNT
assert r12.POST == POST_QUERY_COUNT
assert TOTAL_NODE_COUNT == 421


def encode_word(word: str) -> tuple[int, int]:
    symbol = {"A": 0, "B": 1, "a": 2, "b": 3}
    value = 0
    for pos, ch in enumerate(word):
        value |= symbol[ch] << (2 * pos)
    assert 1 <= len(word) <= 4
    return len(word), value


def remap_target(target, remap):
    kind, payload = target
    if kind == r12.NODE_KIND:
        return remap[payload]
    if kind == r12.ORBIT_KIND:
        return ORBIT_BASE + payload
    if kind == r12.REJECT_KIND:
        return REJECT_NODE
    return FAULT_NODE


def build_program():
    pre = sorted(
        ((old_id, node) for old_id, node in enumerate(r12.nodes)
         if node["mode"] == "pre-erasure"),
        key=lambda item: item[0],
    )
    post = sorted(
        ((old_id, node) for old_id, node in enumerate(r12.nodes)
         if node["mode"] == "post-erasure"),
        key=lambda item: item[0],
    )
    assert len(pre) == PRE_QUERY_COUNT
    assert len(post) == POST_QUERY_COUNT

    ordered = pre + post
    remap = {old_id: new_id for new_id, (old_id, _) in enumerate(ordered)}
    assert len(remap) == QUERY_COUNT

    words = sorted(
        {node["word"] for _, node in ordered},
        key=lambda w: (len(w), w),
    )
    assert len(words) == WORD_COUNT
    assert set(words) == set(r12.WORDS)
    word_id = {word: i for i, word in enumerate(words)}

    word_ids = []
    class_next = []
    erase_next = []

    for new_id, (_, node) in enumerate(ordered):
        word_ids.append(word_id[node["word"]])
        class_next.extend(remap_target(t, remap) for t in node["targets"])
        if new_id < PRE_QUERY_COUNT:
            assert node["mode"] == "pre-erasure"
            erase_next.append(remap_target(node["erasure_target"], remap))
        else:
            assert node["mode"] == "post-erasure"

    word_desc = []
    for word in words:
        wlen, wcode = encode_word(word)
        word_desc.append((wlen << 8) | wcode)

    root = remap[0]
    assert root < PRE_QUERY_COUNT
    assert max(word_ids) < (1 << WORD_ID_W)
    assert max(class_next) < (1 << NODE_W)
    assert max(erase_next) < (1 << NODE_W)
    assert max(word_desc) < (1 << 11)

    summary = {
        "root_node": root,
        "query_nodes": QUERY_COUNT,
        "pre_erasure_query_nodes": PRE_QUERY_COUNT,
        "post_erasure_query_nodes": POST_QUERY_COUNT,
        "orbit_base": ORBIT_BASE,
        "orbit_terminals": ORBIT_COUNT,
        "reject_node": REJECT_NODE,
        "fault_node": FAULT_NODE,
        "total_node_codes": TOTAL_NODE_COUNT,
        "node_width_bits": NODE_W,
        "distinct_words": words,
        "distinct_word_count": len(words),
        "max_word_length": max(map(len, words)),
        "word_id_width_bits": WORD_ID_W,
        "word_id_bits": QUERY_COUNT * WORD_ID_W,
        "class_next_bits": QUERY_COUNT * 6 * NODE_W,
        "erase_next_bits": PRE_QUERY_COUNT * NODE_W,
        "word_desc_bits": len(words) * 11,
    }
    summary["microprogram_bits"] = (
        summary["word_id_bits"]
        + summary["class_next_bits"]
        + summary["erase_next_bits"]
        + summary["word_desc_bits"]
    )
    assert summary["microprogram_bits"] == 18425

    return {
        "root": root,
        "words": words,
        "word_ids": word_ids,
        "class_next": class_next,
        "erase_next": erase_next,
        "word_desc": word_desc,
        "summary": summary,
    }


def emit_mem(path: Path, values, hex_digits: int) -> None:
    path.write_text(
        "\n".join(f"{value:0{hex_digits}x}" for value in values) + "\n",
        encoding="utf-8",
    )


def emit_json(path: Path, program) -> None:
    payload = {
        "contract": {
            "source": "H18-11 exact restricted-12 one-erasure strategy",
            "D0": 4,
            "S1": 4,
            "A1": 5,
            "outputs": "114 orbit IDs or REJECT",
        },
        "summary": program["summary"],
        "word_ids": program["word_ids"],
        "class_next": program["class_next"],
        "erase_next": program["erase_next"],
        "word_desc": program["word_desc"],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def emit_summary(path: Path, program) -> None:
    s = program["summary"]
    text = f"""# H18-LAB-03 restricted-12 generated program

- exact query contract: D0=4, S1=4, A1=5
- query nodes: {s['query_nodes']}
- pre-erasure query nodes: {s['pre_erasure_query_nodes']}
- post-erasure query nodes: {s['post_erasure_query_nodes']}
- distinct words: {s['distinct_word_count']}
- words: {', '.join(s['distinct_words'])}
- word ID width: {s['word_id_width_bits']} bits
- node width: {s['node_width_bits']} bits
- query selector: {s['word_id_bits']} bits
- six-way class transitions: {s['class_next_bits']} bits
- erasure transitions: {s['erase_next_bits']} bits
- word descriptors: {s['word_desc_bits']} bits
- total explicit microprogram payload: **{s['microprogram_bits']} bits**
"""
    path.write_text(text, encoding="utf-8")


def emit_sv_core(path: Path, program) -> None:
    root = program["root"]
    text = f"""// Auto-generated H18-LAB-03 restricted-12 microcoded controller.
// Exact H18-11 semantics: D0=4, S1=4, A1=5.
module h18_r12_microcoded_core(
    input  logic        clk,
    input  logic        rst,
    input  logic        start,
    input  logic [23:0] A_in,
    input  logic [23:0] B_in,
    input  logic        erase_now,
    output logic        busy,
    output logic        done,
    output logic        query_pending,
    output logic        input_valid,
    output logic        identified,
    output logic        rejected,
    output logic [2:0]  status,
    output logic [6:0]  orbit_id
);

localparam integer QUERY_COUNT = {QUERY_COUNT};
localparam integer PRE_QUERY_COUNT = {PRE_QUERY_COUNT};
localparam integer ORBIT_BASE = {ORBIT_BASE};
localparam integer REJECT_NODE = {REJECT_NODE};
localparam integer FAULT_NODE = {FAULT_NODE};
localparam integer ROOT_NODE = {root};

localparam [3:0]
    ST_IDLE=4'd0, ST_CHECK=4'd1, ST_DISPATCH=4'd2,
    ST_WORDDESC=4'd3, ST_WORDINIT=4'd4, ST_WORD=4'd5,
    ST_CLASSIFY=4'd6, ST_APPLY=4'd7, ST_DONE=4'd8;

logic [3:0] state;
logic [23:0] A_reg, B_reg, invA_reg, invB_reg;
logic valid_A, valid_B;
logic [8:0] node_id, next_node_q;
logic [3:0] word_id_q;
logic [10:0] word_desc_q;
logic [2:0] word_len, word_pos;
logic [7:0] word_code;
logic [23:0] word_acc, class_perm;
logic [23:0] selected_perm, first_perm, compose_result;
logic [1:0] selected_letter;
logic [2:0] class_code;

(* rom_style = "distributed" *) logic [3:0] word_id_rom [0:QUERY_COUNT-1];
(* rom_style = "block" *) logic [8:0] class_next_rom [0:QUERY_COUNT*6-1];
(* rom_style = "distributed" *) logic [8:0] erase_next_rom [0:PRE_QUERY_COUNT-1];
(* rom_style = "distributed" *) logic [10:0] word_desc_rom [0:11];

initial begin
    $readmemh("h18_r12_word_id.mem", word_id_rom);
    $readmemh("h18_r12_class_next.mem", class_next_rom);
    $readmemh("h18_r12_erase_next.mem", erase_next_rom);
    $readmemh("h18_r12_word_desc.mem", word_desc_rom);
end

function automatic [2:0] getp(
    input logic [23:0] p, input integer idx
);
    getp = p[idx*3 +: 3];
endfunction

function automatic [23:0] compose_perm(
    input logic [23:0] p, input logic [23:0] q
);
    integer i;
    logic [23:0] r;
    logic [2:0] qi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin
        qi=getp(q,i);
        r[i*3 +:3]=getp(p,qi);
      end
      compose_perm=r;
    end
endfunction

function automatic [23:0] inverse_perm(input logic [23:0] p);
    integer i;
    logic [23:0] r;
    logic [2:0] pi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin
        pi=getp(p,i);
        r[pi*3 +:3]=i[2:0];
      end
      inverse_perm=r;
    end
endfunction

psl27_membership_only u_mem_A(.perm(A_reg),.valid(valid_A));
psl27_membership_only u_mem_B(.perm(B_reg),.valid(valid_B));
psl27_member_class_only u_class(.perm(class_perm),.class_code(class_code));

always @* begin
    case (word_pos)
      3'd1: selected_letter = word_code[3:2];
      3'd2: selected_letter = word_code[5:4];
      default: selected_letter = word_code[7:6];
    endcase

    case (selected_letter)
      2'd0: selected_perm = A_reg;
      2'd1: selected_perm = B_reg;
      2'd2: selected_perm = invA_reg;
      default: selected_perm = invB_reg;
    endcase

    case (word_desc_q[1:0])
      2'd0: first_perm = A_reg;
      2'd1: first_perm = B_reg;
      2'd2: first_perm = invA_reg;
      default: first_perm = invB_reg;
    endcase

    compose_result = compose_perm(word_acc, selected_perm);
end

assign query_pending = (state == ST_CLASSIFY);

always_ff @(posedge clk) begin
  if (rst) begin
    state<=ST_IDLE;
    busy<=1'b0;
    done<=1'b0;
    input_valid<=1'b0;
    identified<=1'b0;
    rejected<=1'b0;
    status<=3'd0;
    orbit_id<=7'h7f;
    A_reg<=0;
    B_reg<=0;
    invA_reg<=0;
    invB_reg<=0;
    node_id<=ROOT_NODE[8:0];
    next_node_q<=FAULT_NODE[8:0];
    word_id_q<=0;
    word_desc_q<=0;
    word_len<=0;
    word_pos<=0;
    word_code<=0;
    word_acc<=24'hfac688;
    class_perm<=24'hfac688;
  end else begin
    done<=1'b0;
    case (state)
      ST_IDLE: begin
        busy<=1'b0;
        if(start) begin
          A_reg<=A_in;
          B_reg<=B_in;
          invA_reg<=inverse_perm(A_in);
          invB_reg<=inverse_perm(B_in);
          input_valid<=1'b0;
          identified<=1'b0;
          rejected<=1'b0;
          status<=3'd0;
          orbit_id<=7'h7f;
          node_id<=ROOT_NODE[8:0];
          busy<=1'b1;
          state<=ST_CHECK;
        end
      end

      ST_CHECK: begin
        input_valid<=valid_A & valid_B;
        if(!(valid_A & valid_B)) begin
          status<=3'd0;
          state<=ST_DONE;
        end else begin
          node_id<=ROOT_NODE[8:0];
          state<=ST_DISPATCH;
        end
      end

      ST_DISPATCH: begin
        if(node_id < QUERY_COUNT) begin
          word_id_q<=word_id_rom[node_id];
          state<=ST_WORDDESC;
        end else if(node_id < REJECT_NODE) begin
          identified<=1'b1;
          rejected<=1'b0;
          status<=3'd2;
          orbit_id<=node_id-ORBIT_BASE;
          state<=ST_DONE;
        end else if(node_id == REJECT_NODE) begin
          identified<=1'b0;
          rejected<=1'b1;
          status<=3'd1;
          orbit_id<=7'h7f;
          state<=ST_DONE;
        end else begin
          identified<=1'b0;
          rejected<=1'b0;
          status<=3'd4;
          orbit_id<=7'h7f;
          state<=ST_DONE;
        end
      end

      ST_WORDDESC: begin
        word_desc_q<=word_desc_rom[word_id_q];
        state<=ST_WORDINIT;
      end

      ST_WORDINIT: begin
        word_len<=word_desc_q[10:8];
        word_code<=word_desc_q[7:0];
        word_pos<=3'd1;
        word_acc<=first_perm;
        if(word_desc_q[10:8] <= 3'd1) begin
          class_perm<=first_perm;
          state<=ST_CLASSIFY;
        end else begin
          state<=ST_WORD;
        end
      end

      ST_WORD: begin
        word_acc<=compose_result;
        if(word_pos + 3'd1 >= word_len) begin
          class_perm<=compose_result;
          state<=ST_CLASSIFY;
        end else begin
          word_pos<=word_pos + 3'd1;
        end
      end

      ST_CLASSIFY: begin
        if(erase_now) begin
          if(node_id < PRE_QUERY_COUNT) begin
            next_node_q<=erase_next_rom[node_id];
            state<=ST_APPLY;
          end else begin
            status<=3'd4;
            orbit_id<=7'h7f;
            state<=ST_DONE;
          end
        end else begin
          next_node_q<=class_next_rom[node_id*6 + class_code];
          state<=ST_APPLY;
        end
      end

      ST_APPLY: begin
        node_id<=next_node_q;
        state<=ST_DISPATCH;
      end

      ST_DONE: begin
        busy<=1'b0;
        done<=1'b1;
        state<=ST_IDLE;
      end

      default: begin
        status<=3'd4;
        orbit_id<=7'h7f;
        busy<=1'b0;
        state<=ST_IDLE;
      end
    endcase
  end
end
endmodule
"""
    path.write_text(text, encoding="utf-8")


def pack_perm(p) -> int:
    value = 0
    for i, x in enumerate(p):
        value |= x << (3 * i)
    return value


def emit_vectors(path: Path) -> None:
    h17_id = {rep: i for i, rep in enumerate(r12.c.h17.REPS)}
    lines = ["# A B expected_status expected_orbit"]
    for state, (a, b) in enumerate(r12.c.REPS):
        if r12.c.IS_GENERATING[state]:
            status = 2
            orbit = h17_id[(a, b)]
        else:
            status = 1
            orbit = 127
        lines.append(f"{pack_perm(a):06x} {pack_perm(b):06x} {status:x} {orbit:02x}")
    assert len(lines) == 198
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def emit_sv_tb(path: Path) -> None:
    path.write_text(r'''module tb_h18_r12_microcoded;
logic clk,rst,start,erase_now;
logic [23:0] A_in,B_in;
logic busy,done,query_pending,input_valid,identified,rejected;
logic [2:0] status;
logic [6:0] orbit_id;

h18_r12_microcoded_core dut(
 .clk(clk),.rst(rst),.start(start),.A_in(A_in),.B_in(B_in),
 .erase_now(erase_now),.busy(busy),.done(done),
 .query_pending(query_pending),.input_valid(input_valid),
 .identified(identified),.rejected(rejected),
 .status(status),.orbit_id(orbit_id)
);

always #5 clk=~clk;

integer fd,rc,n,attempts,cycles,max_cycles,max_attempts,total_runs;
reg [1023:0] file_name;
reg [23:0] ea,eb;
reg [3:0] es;
reg [7:0] eoid;

task automatic run_case(input integer target);
integer fired;
begin
  @(negedge clk);
  A_in=ea; B_in=eb; start=1'b1; erase_now=1'b0;
  @(negedge clk);
  start=1'b0;
  attempts=0; cycles=0; fired=0;

  while(!done && cycles<180) begin
    @(negedge clk);
    erase_now=1'b0;
    if(query_pending) begin
      attempts=attempts+1;
      if(target>0 && attempts==target && !fired) begin
        erase_now=1'b1;
        fired=1;
      end
    end
    cycles=cycles+1;
  end
  erase_now=1'b0;

  if(!done)
    $fatal(1,"timeout vector=%0d erase_target=%0d",n,target);

  if(cycles>max_cycles) max_cycles=cycles;
  if(attempts>max_attempts) max_attempts=attempts;

  if(status!==es[2:0] || orbit_id!==eoid[6:0])
    $fatal(1,
      "mismatch vector=%0d erase_target=%0d A=%h B=%h expected status=%h orbit=%h got status=%h orbit=%h attempts=%0d cycles=%0d",
      n,target,ea,eb,es,eoid,status,orbit_id,attempts,cycles);

  if(es==4'h2 && (!identified || rejected))
    $fatal(1,"success flags mismatch vector=%0d",n);

  if(es==4'h1 && (!rejected || identified))
    $fatal(1,"reject flags mismatch vector=%0d",n);

  if(attempts>5)
    $fatal(1,"attempt bound exceeded vector=%0d target=%0d attempts=%0d",
      n,target,attempts);

  total_runs=total_runs+1;
end
endtask

initial begin
  clk=0; rst=1; start=0; erase_now=0; A_in=0; B_in=0;
  n=0; max_cycles=0; max_attempts=0; total_runs=0;

  repeat(3) @(negedge clk);
  rst=0;

  if(!$value$plusargs("VECTORS=%s",file_name))
    file_name="h18_r12_vectors.txt";

  fd=$fopen(file_name,"r");
  if(!fd) $fatal(1,"vectors missing: %0s",file_name);
  rc=$fgets(file_name,fd);

  while(!$feof(fd)) begin
    rc=$fscanf(fd,"%h %h %h %h\n",ea,eb,es,eoid);
    if(rc==4) begin
      run_case(0);
      run_case(1);
      run_case(2);
      run_case(3);
      run_case(4);
      n=n+1;
    end
  end

  $fclose(fd);
  if(n!=197) $fatal(1,"expected 197 states, got %0d",n);
  if(total_runs!=985) $fatal(1,"expected 985 runs, got %0d",total_runs);

  $display(
    "PASS H18-LAB-03 restricted12: %0d states x 5 schedules = %0d runs; max_attempts=%0d max_cycles=%0d",
    n,total_runs,max_attempts,max_cycles);
  $finish;
end
endmodule
''', encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=Path("generated_r12"))
    args = parser.parse_args()
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)

    program = build_program()

    emit_mem(out / "h18_r12_word_id.mem", program["word_ids"], 1)
    emit_mem(out / "h18_r12_class_next.mem", program["class_next"], 3)
    emit_mem(out / "h18_r12_erase_next.mem", program["erase_next"], 3)
    emit_mem(out / "h18_r12_word_desc.mem", program["word_desc"], 3)
    emit_json(out / "h18_r12_program.json", program)
    emit_summary(out / "H18_R12_PROGRAM_SUMMARY.md", program)
    emit_sv_core(out / "h18_r12_microcoded_core.sv", program)
    emit_vectors(out / "h18_r12_vectors.txt")
    emit_sv_tb(out / "tb_h18_r12_microcoded.sv")

    s = program["summary"]
    print("H18-LAB-03 restricted-12 RTL generator")
    print("query nodes =", s["query_nodes"])
    print("pre/post =", s["pre_erasure_query_nodes"], s["post_erasure_query_nodes"])
    print("distinct words =", s["distinct_words"])
    print("microprogram bits =", s["microprogram_bits"])
    print("PASS: deterministic restricted-12 RTL/microcode emitted")


if __name__ == "__main__":
    main()
