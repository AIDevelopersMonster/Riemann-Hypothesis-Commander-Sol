// H17-06 ROM-free robust fingerprint core.
module psl27_robust8_romfree_core(
    input  logic [23:0] A,
    input  logic [23:0] B,
    input  logic [2:0]  erased_idx,
    output logic        input_valid,
    output logic        fingerprint_valid,
    output logic [23:0] raw_signature,
    output logic [23:0] orbit_fingerprint
);
logic repair_valid;
psl27_robust8_engine u_eng(.A(A),.B(B),.valid(input_valid),.signature(raw_signature));
psl27_robust8_repair u_rep(.signature(raw_signature),.erased_idx(erased_idx),.valid(repair_valid),.repaired_signature(orbit_fingerprint));
assign fingerprint_valid = input_valid & repair_valid;
endmodule
