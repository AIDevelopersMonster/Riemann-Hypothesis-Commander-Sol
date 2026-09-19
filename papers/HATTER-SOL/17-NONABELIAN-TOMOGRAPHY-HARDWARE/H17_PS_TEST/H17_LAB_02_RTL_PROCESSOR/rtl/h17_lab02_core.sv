// H17-LAB-02 pure-RTL mathematical processor.
//
// No board, vendor, clock, UART or FPGA-family dependency is present here.
// The module expresses the H17 mathematical map as combinational RTL:
//
//   (A,B) -> robust8 class fingerprint -> known one-erasure repair
//
// Frontend: H17-08 closure-aware engine.
// Backend:  H17-06 ROM-free decision network.
//
// mode:
//   0    no externally visible erasure; the e=0 repair tree is still used as
//        a generating-domain validator and must reconstruct the same signature.
//   1..8 known erased robust8 coordinate; that field is overwritten by 3'b111.
//   >8   illegal mode.
//
// status compatible with H17-LAB-01 where applicable:
//   0 raw A/B fail PSL(2,7) membership
//   1 valid PSL inputs, but non-generating / not repairable
//   2 unique valid generating fingerprint
//   4 illegal mode
//
// status=3 (multiple flat-ROM hits) cannot occur in this exact ROM-free tree.

module h17_lab02_core(
    input  logic [23:0] A,
    input  logic [23:0] B,
    input  logic [3:0]  mode,

    output logic        input_valid,
    output logic        fingerprint_valid,
    output logic [2:0]  status,

    output logic [23:0] raw_signature,
    output logic [23:0] observed_signature,
    output logic [23:0] repaired_signature
);

logic        raw_membership_valid;
logic [23:0] engine_signature;
logic [2:0]  erased_idx;
logic        repair_valid;
logic [23:0] repair_signature;
logic        mode_valid;

// H17-08: only raw A and B need membership logic.
// Every derived free-group word stays in PSL(2,7) by group closure.
psl27_robust8_engine u_engine(
    .A(A),
    .B(B),
    .valid(raw_membership_valid),
    .signature(engine_signature)
);

// H17-06: exact depth-4 one-erasure decision network.
// Generated trees never query the coordinate named by erased_idx.
psl27_robust8_repair u_repair(
    .signature(observed_signature),
    .erased_idx(erased_idx),
    .valid(repair_valid),
    .repaired_signature(repair_signature)
);

always_comb begin
    mode_valid = (mode <= 4'd8);
    input_valid = raw_membership_valid;

    // LAB-01 stops before word evaluation when A/B are invalid and stops
    // immediately on an illegal mode. Gate public signatures identically.
    raw_signature = (mode_valid && raw_membership_valid)
                  ? engine_signature : 24'h000000;

    observed_signature = raw_signature;
    erased_idx = 3'd0;

    // Preserve the LAB-01 public-output contract: invalid raw membership
    // produces all-zero public signatures regardless of a syntactically valid
    // erasure mode.  The erasure marker is meaningful only after A/B have
    // passed PSL(2,7) membership.
    if (!mode_valid || !raw_membership_valid) begin
        observed_signature = 24'h000000;
        erased_idx = 3'd0;
    end else begin
        case (mode)
          4'd0: begin
            // No visible erasure. The e=0 tree ignores coordinate 0, validates
            // the generating domain from the other seven coordinates, and
            // reconstructs coordinate 0. For a valid generating state the
            // result must equal raw.
            erased_idx = 3'd0;
          end
          4'd1: begin erased_idx=3'd0; observed_signature[23:21]=3'b111; end
          4'd2: begin erased_idx=3'd1; observed_signature[20:18]=3'b111; end
          4'd3: begin erased_idx=3'd2; observed_signature[17:15]=3'b111; end
          4'd4: begin erased_idx=3'd3; observed_signature[14:12]=3'b111; end
          4'd5: begin erased_idx=3'd4; observed_signature[11: 9]=3'b111; end
          4'd6: begin erased_idx=3'd5; observed_signature[ 8: 6]=3'b111; end
          4'd7: begin erased_idx=3'd6; observed_signature[ 5: 3]=3'b111; end
          4'd8: begin erased_idx=3'd7; observed_signature[ 2: 0]=3'b111; end
          default: begin
            erased_idx = 3'd0;
            observed_signature = 24'h000000;
          end
        endcase
    end

    fingerprint_valid = mode_valid && raw_membership_valid && repair_valid;
    repaired_signature = fingerprint_valid
                       ? repair_signature : 24'h000000;

    if (!mode_valid)
        status = 3'd4;
    else if (!raw_membership_valid)
        status = 3'd0;
    else if (repair_valid)
        status = 3'd2;
    else
        status = 3'd1;
end

endmodule
