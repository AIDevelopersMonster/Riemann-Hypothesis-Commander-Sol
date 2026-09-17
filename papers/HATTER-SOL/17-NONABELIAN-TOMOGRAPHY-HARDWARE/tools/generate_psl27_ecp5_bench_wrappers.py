#!/usr/bin/env python3
"""Emit registered wrappers for target-specific ECP5 area/timing comparison.

The underlying H17-08 cores are combinational.  These wrappers put exactly one
input register bank and one output register bank around each core so nextpnr can
measure the same register-to-register combinational processor path for the flat
orbit-ID and ROM-free fingerprint backends.
"""
from pathlib import Path
import argparse

FLAT = r'''module psl27_closure_flat_bench(
    input  logic        clk,
    input  logic [23:0] A,
    input  logic [23:0] B,
    input  logic [2:0]  erased_idx,
    output logic        input_valid,
    output logic        orbit_valid,
    output logic [6:0]  orbit_id,
    output logic [23:0] signature
);
logic [23:0] A_r, B_r;
logic [2:0] erased_idx_r;
logic core_input_valid, core_orbit_valid;
logic [6:0] core_orbit_id;
logic [23:0] core_signature;

always_ff @(posedge clk) begin
    A_r <= A;
    B_r <= B;
    erased_idx_r <= erased_idx;
    input_valid <= core_input_valid;
    orbit_valid <= core_orbit_valid;
    orbit_id <= core_orbit_id;
    signature <= core_signature;
end

psl27_closure_flat_core u_core(
    .A(A_r), .B(B_r), .erased_idx(erased_idx_r),
    .input_valid(core_input_valid), .orbit_valid(core_orbit_valid),
    .orbit_id(core_orbit_id), .signature(core_signature)
);
endmodule
'''

ROMFREE = r'''module psl27_closure_romfree_bench(
    input  logic        clk,
    input  logic [23:0] A,
    input  logic [23:0] B,
    input  logic [2:0]  erased_idx,
    output logic        input_valid,
    output logic        fingerprint_valid,
    output logic [23:0] raw_signature,
    output logic [23:0] orbit_fingerprint
);
logic [23:0] A_r, B_r;
logic [2:0] erased_idx_r;
logic core_input_valid, core_fingerprint_valid;
logic [23:0] core_raw_signature, core_orbit_fingerprint;

always_ff @(posedge clk) begin
    A_r <= A;
    B_r <= B;
    erased_idx_r <= erased_idx;
    input_valid <= core_input_valid;
    fingerprint_valid <= core_fingerprint_valid;
    raw_signature <= core_raw_signature;
    orbit_fingerprint <= core_orbit_fingerprint;
end

psl27_closure_romfree_core u_core(
    .A(A_r), .B(B_r), .erased_idx(erased_idx_r),
    .input_valid(core_input_valid), .fingerprint_valid(core_fingerprint_valid),
    .raw_signature(core_raw_signature), .orbit_fingerprint(core_orbit_fingerprint)
);
endmodule
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out-dir', default='generated_h17_09')
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'psl27_closure_flat_bench.sv').write_text(FLAT, encoding='utf-8')
    (out / 'psl27_closure_romfree_bench.sv').write_text(ROMFREE, encoding='utf-8')
    print('PASS: emitted registered H17 ECP5 benchmark wrappers')

if __name__ == '__main__':
    main()
