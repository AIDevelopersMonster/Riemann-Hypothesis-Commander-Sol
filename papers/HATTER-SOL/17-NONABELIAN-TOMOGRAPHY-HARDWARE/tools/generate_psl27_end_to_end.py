#!/usr/bin/env python3
"""H17-02: build the complete exact PSL(2,7) tomography RTL bundle.

This orchestrates the H17-01 golden-model generator and H17-02 port-engine
generator, then emits the end-to-end wrapper and a testbench covering every
five-probe signature realized by PSL(2,7)^2: 114 generating signatures accept
with canonical orbit IDs and 66 non-generating signatures reject.
"""
from pathlib import Path
import argparse
from generate_psl27_golden_model import G, REPS, class_signature, signature_code, subgroup, build_rows, write_csv, write_sv_rom
from generate_psl27_port_engine import pack, emit_classifier, emit_engine


def q4(sig):
    return "2'b01" if sig[4] == '7A' else "2'b10" if sig[4] == '7B' else "2'b00"


CORE = """// HATTER-SOL-17 end-to-end zero-oracle finite tomography core.
// Exact finite certificate proves for valid PSL(2,7) inputs:
//   orbit_valid == 1 iff <A,B> = PSL(2,7).
module psl27_tomography_core(
    input logic [23:0] A, input logic [23:0] B,
    output logic group_input_valid, output logic signature_hit,
    output logic orbit_valid, output logic [6:0] orbit_id,
    output logic [1:0] q4_orientation, output logic [14:0] signature,
    output logic [23:0] AB, output logic [23:0] AB_inv, output logic [23:0] K
);
logic engine_valid, rom_valid;
logic [6:0] rom_orbit_id;
logic [1:0] rom_q4;
psl27_five_probe_engine u_engine(
    .A(A), .B(B), .valid(engine_valid),
    .signature(signature), .AB(AB), .AB_inv(AB_inv), .K(K)
);
psl27_orbit_rom u_rom(
    .signature(signature), .valid(rom_valid),
    .orbit_id(rom_orbit_id), .q4_orientation(rom_q4)
);
assign group_input_valid = engine_valid;
assign signature_hit = rom_valid;
assign orbit_valid = engine_valid & rom_valid;
assign orbit_id = orbit_valid ? rom_orbit_id : 7'h7f;
assign q4_orientation = orbit_valid ? rom_q4 : 2'b00;
endmodule
"""


def emit_tb(path: Path):
    gen = {class_signature(a, b): i for i, (a, b) in enumerate(REPS)}
    non = {}
    for a in G:
        for b in G:
            s = class_signature(a, b)
            if len(subgroup(a, b)) != 168:
                non.setdefault(s, (a, b))
    assert len(gen) == 114
    assert len(non) == 66
    assert set(gen).isdisjoint(non)

    lines = [
        '`timescale 1ns/1ps',
        '// Exhaustive over all 180 five-probe signatures realized by PSL(2,7)^2.',
        'module tb_psl27_tomography_core;',
        'logic [23:0] A,B;',
        'logic group_input_valid,signature_hit,orbit_valid;',
        'logic [6:0] orbit_id;',
        'logic [1:0] q4_orientation;',
        'logic [14:0] signature;',
        'logic [23:0] AB,AB_inv,K;',
        'psl27_tomography_core dut(.A(A),.B(B),.group_input_valid(group_input_valid),.signature_hit(signature_hit),.orbit_valid(orbit_valid),.orbit_id(orbit_id),.q4_orientation(q4_orientation),.signature(signature),.AB(AB),.AB_inv(AB_inv),.K(K));',
        'task automatic check_gen(input logic [23:0] a,input logic [23:0] b,input logic [14:0] sig,input logic [6:0] oid,input logic [1:0] qq); begin A=a;B=b;#1; if(!group_input_valid||!signature_hit||!orbit_valid||signature!==sig||orbit_id!==oid||q4_orientation!==qq)$fatal(1); end endtask',
        'task automatic check_nongen(input logic [23:0] a,input logic [23:0] b,input logic [14:0] sig); begin A=a;B=b;#1; if(!group_input_valid||signature_hit||orbit_valid||signature!==sig||orbit_id!==7\'h7f)$fatal(1); end endtask',
        'initial begin',
    ]
    for oid, (a, b) in enumerate(REPS):
        s = class_signature(a, b)
        lines.append(
            f"check_gen(24'h{pack(a):06x},24'h{pack(b):06x},15'b{signature_code(s):015b},7'd{oid},{q4(s)});"
        )
    for s, (a, b) in sorted(non.items()):
        lines.append(
            f"check_nongen(24'h{pack(a):06x},24'h{pack(b):06x},15'b{signature_code(s):015b});"
        )
    lines += [
        '$display("PASS: all 180 realized PSL(2,7)^2 signature states checked");',
        '$finish;',
        'end',
        'endmodule',
        '',
    ]
    path.write_text('\n'.join(lines), encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='generated')
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    rows = build_rows()
    write_csv(rows, out / 'psl27_114_orbit_signatures.csv')
    write_sv_rom(rows, out / 'psl27_orbit_rom.sv')
    emit_classifier(out / 'psl27_classify_perm.sv')
    emit_engine(out / 'psl27_five_probe_engine.sv')
    (out / 'psl27_tomography_core.sv').write_text(CORE, encoding='utf-8')
    emit_tb(out / 'tb_psl27_tomography_core.sv')

    print('PASS: complete H17 exact RTL bundle emitted')
    print('TB coverage: 114 generating signatures + 66 non-generating signatures')


if __name__ == '__main__':
    main()
