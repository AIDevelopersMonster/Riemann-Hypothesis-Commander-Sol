// H17 optimal eight-channel one-erasure tomography processor.
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
