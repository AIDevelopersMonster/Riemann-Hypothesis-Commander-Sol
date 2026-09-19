#!/usr/bin/env python3
"""Generate a compact ModelSim waveform experiment for H18-LAB-04.

The experiment uses one certified generating pair twice:
  1. no erasure;
  2. persistent erasure of the exact root query of the H18-11 decision DAG.

Both transactions must identify the same orbit. The waveform exposes the
registered shell, the 12 parallel query classes, the root result, and the
normal/erasure child selected by the mathematical decision DAG.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve()
LAB = HERE.parents[1]
H18 = LAB.parent
CERT = H18 / "certificates" / "h18_restricted12_controller_certificate.py"

spec = importlib.util.spec_from_file_location("h18_r12_cert", CERT)
assert spec is not None and spec.loader is not None
r12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r12)

WORDS = tuple(sorted(r12.WORDS, key=lambda w: (len(w), w)))
WORD_ID = {w: i for i, w in enumerate(WORDS)}

root = r12.nodes[0]
root_word = root["word"]
root_wid = WORD_ID[root_word]
root_qi = root["query_index"]


def pack_perm(p) -> int:
    value = 0
    for i, x in enumerate(p):
        value |= x << (3 * i)
    return value


def class_of(state: int, qi: int) -> int:
    bit = 1 << state
    hits = [cls for cls, mask in enumerate(r12.c.QUERY_MASKS[qi]) if mask & bit]
    assert len(hits) == 1
    return hits[0]


chosen = None
for state, rep in enumerate(r12.c.REPS):
    if not r12.c.IS_GENERATING[state]:
        continue
    cls = class_of(state, root_qi)
    normal = root["targets"][cls]
    erased = root["erasure_target"]
    if normal[0] == r12.NODE_KIND and erased[0] == r12.NODE_KIND:
        chosen = (state, rep, cls, normal[1], erased[1])
        break

assert chosen is not None
state, (aa, bb), root_cls, normal_node, erased_node = chosen
orbit_id = r12.GEN_ORBIT_ID[(aa, bb)]
a_hex = pack_perm(aa)
b_hex = pack_perm(bb)

tb = f"""module tb_h18_r12_comb_wave;
logic clk=0,rst=1,start=0,erase_valid=0;
logic [23:0] A_in=24'h{a_hex:06x},B_in=24'h{b_hex:06x};
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

task automatic transact(input logic ev, input logic [3:0] wid);
begin
  @(negedge clk);
  erase_valid=ev;
  erased_word_id=wid;
  start=1;

  @(negedge clk);
  start=0;

  @(negedge clk);
  if(!done) $fatal(1,"wave demo: done missing");
  if(status!==3'd2 || orbit_id!==7'd{orbit_id})
    $fatal(1,"wave demo: wrong result status=%0d orbit=%0d",status,orbit_id);

  @(negedge clk);
  if(done) $fatal(1,"wave demo: done is not a one-cycle pulse");
end
endtask

initial begin
  $display("H18-LAB-04 WAVE DEMO");
  $display("state={state} A={a_hex:06x} B={b_hex:06x} expected_orbit={orbit_id}");
  $display("root word={root_word} root_word_id={root_wid} root_class={root_cls}");
  $display("normal child node={normal_node} erasure child node={erased_node}");

  repeat(3) @(negedge clk);
  rst=0;

  transact(1'b0,4'd0);
  repeat(2) @(negedge clk);
  transact(1'b1,4'd{root_wid});

  repeat(2) @(negedge clk);
  $display("PASS H18-LAB-04 waveform: same orbit with and without root-query erasure");
  $finish;
end

initial begin
  #1000;
  $fatal(1,"wave demo watchdog");
end
endmodule
"""

out = LAB / "generated_comb"
out.mkdir(parents=True, exist_ok=True)
(out / "tb_h18_r12_comb_wave.sv").write_text(tb, encoding="utf-8")


def add(label: str, signal: str, radix: str | None = None) -> str:
    r = f" -radix {radix}" if radix else ""
    return f"add wave{r} -label {{{label}}} {signal}"


do = ["view wave", "delete wave *", "add wave -divider {CLOCK / CONTROL}"]
for label, signal in [
    ("clk","sim:/tb_h18_r12_comb_wave/clk"),
    ("rst","sim:/tb_h18_r12_comb_wave/rst"),
    ("start","sim:/tb_h18_r12_comb_wave/start"),
    ("busy","sim:/tb_h18_r12_comb_wave/busy"),
    ("pending","sim:/tb_h18_r12_comb_wave/dut/pending"),
    ("done","sim:/tb_h18_r12_comb_wave/done"),
]:
    do.append(add(label, signal))

do.append("add wave -divider {INPUT / LATCH}")
for label, signal, radix in [
    ("A_in","sim:/tb_h18_r12_comb_wave/A_in","hexadecimal"),
    ("B_in","sim:/tb_h18_r12_comb_wave/B_in","hexadecimal"),
    ("A_q","sim:/tb_h18_r12_comb_wave/dut/A_q","hexadecimal"),
    ("B_q","sim:/tb_h18_r12_comb_wave/dut/B_q","hexadecimal"),
    ("erase_valid","sim:/tb_h18_r12_comb_wave/erase_valid",None),
    ("erased_word_id","sim:/tb_h18_r12_comb_wave/erased_word_id","unsigned"),
    ("erase_valid_q","sim:/tb_h18_r12_comb_wave/dut/erase_valid_q",None),
    ("erased_word_id_q","sim:/tb_h18_r12_comb_wave/dut/erased_word_id_q","unsigned"),
]:
    do.append(add(label, signal, radix))

do.append("add wave -divider {PSL MEMBERSHIP}")
do.append(add("valid_A","sim:/tb_h18_r12_comb_wave/dut/u_core/valid_A"))
do.append(add("valid_B","sim:/tb_h18_r12_comb_wave/dut/u_core/valid_B"))

do.append("add wave -divider {12 PARALLEL OBSERVERS}")
for wid, word in enumerate(WORDS):
    do.append(add(f"class[{wid}] {word}",
                  f"sim:/tb_h18_r12_comb_wave/dut/u_core/class_{wid}",
                  "unsigned"))

do.append("add wave -divider {COMPILED DECISION DAG}")
do.append(add(f"ROOT node0 query={root_word}",
              "sim:/tb_h18_r12_comb_wave/dut/u_core/node_result_0",
              "hexadecimal"))
do.append(add(f"normal child node{normal_node}",
              f"sim:/tb_h18_r12_comb_wave/dut/u_core/node_result_{normal_node}",
              "hexadecimal"))
do.append(add(f"erasure child node{erased_node}",
              f"sim:/tb_h18_r12_comb_wave/dut/u_core/node_result_{erased_node}",
              "hexadecimal"))
do.append(add("core_status","sim:/tb_h18_r12_comb_wave/dut/core_status","unsigned"))
do.append(add("core_orbit_id","sim:/tb_h18_r12_comb_wave/dut/core_orbit_id","unsigned"))

do.append("add wave -divider {REGISTERED RESULT}")
for label, signal, radix in [
    ("input_valid","sim:/tb_h18_r12_comb_wave/input_valid",None),
    ("identified","sim:/tb_h18_r12_comb_wave/identified",None),
    ("rejected","sim:/tb_h18_r12_comb_wave/rejected",None),
    ("status","sim:/tb_h18_r12_comb_wave/status","unsigned"),
    ("orbit_id","sim:/tb_h18_r12_comb_wave/orbit_id","unsigned"),
]:
    do.append(add(label, signal, radix))

do += [
    "configure wave -namecolwidth 240",
    "configure wave -valuecolwidth 100",
    "configure wave -timelineunits ns",
    "run -all",
    "wave zoom full",
]
(out / "wave_h18_r12_comb.do").write_text("\n".join(do) + "\n", encoding="utf-8")

info = f"""# H18-LAB-04 waveform scenario

- certified state: {state}
- A: 0x{a_hex:06x}
- B: 0x{b_hex:06x}
- expected orbit: {orbit_id}
- root query: {root_word}
- root query ID: {root_wid}
- root class for selected state: {root_cls}
- ordinary child node: {normal_node}
- root-erasure child node: {erased_node}

The waveform executes the same pair twice: first without erasure, then with
the root query persistently unavailable. Both must return the same orbit.
"""
(out / "H18_R12_WAVE_SCENARIO.md").write_text(info, encoding="utf-8")

print("H18-LAB-04 waveform assets generated")
print(f"state={state} A={a_hex:06x} B={b_hex:06x} orbit={orbit_id}")
print(f"root={root_word} wid={root_wid} class={root_cls}")
print(f"normal_node={normal_node} erasure_node={erased_node}")
print("PASS: waveform TB and ModelSim .do emitted")
