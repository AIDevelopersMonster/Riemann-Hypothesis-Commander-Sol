// H17-LAB-03 sequential/time-multiplexed structural processor.
//
// Purpose:
//   Keep the H17-06/H17-07/H17-08 mathematics, but remove the enormous
//   all-at-once combinational event graph that makes Icarus impractically slow.
//
// Architecture:
//   latch A,B
//   -> 2 x raw membership check
//   -> H17-07 14-node word DAG, ONE composition per cycle
//   -> ONE reusable member-class-only engine
//   -> eight 3-bit fingerprint registers
//   -> known erasure mask
//   -> H17-06 ROM-free repair
//
// This is board-independent RTL.  No FPGA family, vendor primitive, UART,
// pin map or physical clock claim is made here.
//
// Valid PSL inputs (generating or non-generating) take a fixed sequential
// path.  Illegal mode / invalid raw membership are rejected early.

module h17_lab03_sequential_core(
    input  logic        clk,
    input  logic        rst,
    input  logic        start,
    input  logic [23:0] A_in,
    input  logic [23:0] B_in,
    input  logic [3:0]  mode_in,

    output logic        busy,
    output logic        done,
    output logic        input_valid,
    output logic        fingerprint_valid,
    output logic [2:0]  status,
    output logic [23:0] raw_signature,
    output logic [23:0] observed_signature,
    output logic [23:0] repaired_signature
);

localparam [3:0]
    ST_IDLE     = 4'd0,
    ST_CHECK    = 4'd1,
    ST_COMPOSE  = 4'd2,
    ST_CLASSIFY = 4'd3,
    ST_MASK     = 4'd4,
    ST_REPAIR   = 4'd5,
    ST_DONE     = 4'd6;

logic [3:0] state;
logic [3:0] op_idx;
logic [2:0] probe_idx;

logic [23:0] A_reg, B_reg, invA_reg, invB_reg;
logic [3:0]  mode_reg;

// H17-07 DAG registers, in frozen operation order.
logic [23:0] n_AB, n_Ab, n_BB;
logic [23:0] n_AAB, n_ABA, n_ABa, n_Abb;
logic [23:0] n_AAAB, n_AbAb, n_Abbb;
logic [23:0] n_AABAb, n_AAbAb, n_ABABB, n_ABaBB;

logic [23:0] compose_left, compose_right, compose_result;
logic [23:0] class_perm;
logic [2:0]  class_code;
logic        valid_A, valid_B;

logic [2:0]  erased_idx_reg;
logic        repair_valid;
logic [23:0] repair_signature;

function automatic [2:0] getp(input logic [23:0] p, input integer idx);
    getp = p[idx*3 +: 3];
endfunction

function automatic [23:0] compose_perm(input logic [23:0] p, input logic [23:0] q);
    integer i;
    logic [23:0] r;
    logic [2:0] qi;
    begin
      r = '0;
      for (i=0; i<8; i=i+1) begin
        qi = getp(q,i);
        r[i*3 +: 3] = getp(p,qi);
      end
      compose_perm = r;
    end
endfunction

function automatic [23:0] inverse_perm(input logic [23:0] p);
    integer i;
    logic [23:0] r;
    logic [2:0] pi;
    begin
      r = '0;
      for (i=0; i<8; i=i+1) begin
        pi = getp(p,i);
        r[pi*3 +: 3] = i[2:0];
      end
      inverse_perm = r;
    end
endfunction

function automatic [23:0] erase_signature(
    input logic [23:0] sig,
    input logic [3:0] mode
);
    logic [23:0] r;
    begin
      r = sig;
      case (mode)
        4'd0: ;
        4'd1: r[23:21] = 3'b111;
        4'd2: r[20:18] = 3'b111;
        4'd3: r[17:15] = 3'b111;
        4'd4: r[14:12] = 3'b111;
        4'd5: r[11: 9] = 3'b111;
        4'd6: r[ 8: 6] = 3'b111;
        4'd7: r[ 5: 3] = 3'b111;
        4'd8: r[ 2: 0] = 3'b111;
        default: r = 24'h000000;
      endcase
      erase_signature = r;
    end
endfunction

// Two raw membership engines remain parallel.  They are only used once per
// transaction, in ST_CHECK.
psl27_membership_only u_mem_A(.perm(A_reg), .valid(valid_A));
psl27_membership_only u_mem_B(.perm(B_reg), .valid(valid_B));

// One class engine is reused for all eight derived robust probes.
psl27_member_class_only u_class(
    .perm(class_perm),
    .class_code(class_code)
);

// One ROM-free repair tree is evaluated only after all eight classes have
// been registered.
psl27_robust8_repair u_repair(
    .signature(observed_signature),
    .erased_idx(erased_idx_reg),
    .valid(repair_valid),
    .repaired_signature(repair_signature)
);

// Exactly one H17-07 DAG composition is presented to compose_perm at a time.
always @* begin
    compose_left  = 24'hfac688; // identity; overwritten for valid op_idx
    compose_right = 24'hfac688;

    case (op_idx)
      4'd0:  begin compose_left=A_reg;  compose_right=B_reg;     end // AB
      4'd1:  begin compose_left=A_reg;  compose_right=invB_reg;  end // Ab
      4'd2:  begin compose_left=B_reg;  compose_right=B_reg;     end // BB
      4'd3:  begin compose_left=A_reg;  compose_right=n_AB;      end // AAB
      4'd4:  begin compose_left=n_AB;   compose_right=A_reg;     end // ABA
      4'd5:  begin compose_left=n_AB;   compose_right=invA_reg;  end // ABa
      4'd6:  begin compose_left=n_Ab;   compose_right=invB_reg;  end // Abb
      4'd7:  begin compose_left=A_reg;  compose_right=n_AAB;     end // AAAB
      4'd8:  begin compose_left=n_Ab;   compose_right=n_Ab;      end // AbAb
      4'd9:  begin compose_left=n_Abb;  compose_right=invB_reg;  end // Abbb
      4'd10: begin compose_left=n_AAB;  compose_right=n_Ab;      end // AABAb
      4'd11: begin compose_left=A_reg;  compose_right=n_AbAb;    end // AAbAb
      4'd12: begin compose_left=n_ABA;  compose_right=n_BB;      end // ABABB
      4'd13: begin compose_left=n_ABa;  compose_right=n_BB;      end // ABaBB
      default: ;
    endcase
end

always @* begin
    compose_result = compose_perm(compose_left, compose_right);
end

always_ff @(posedge clk) begin
    if (rst) begin
        state <= ST_IDLE;
        busy <= 1'b0;
        done <= 1'b0;
        input_valid <= 1'b0;
        fingerprint_valid <= 1'b0;
        status <= 3'd0;
        raw_signature <= 24'h000000;
        observed_signature <= 24'h000000;
        repaired_signature <= 24'h000000;
        A_reg <= 24'h000000;
        B_reg <= 24'h000000;
        invA_reg <= 24'h000000;
        invB_reg <= 24'h000000;
        mode_reg <= 4'd0;
        op_idx <= 4'd0;
        probe_idx <= 3'd0;
        class_perm <= 24'hfac688;
        erased_idx_reg <= 3'd0;
        n_AB <= 0; n_Ab <= 0; n_BB <= 0; n_AAB <= 0; n_ABA <= 0; n_ABa <= 0; n_Abb <= 0;
        n_AAAB <= 0; n_AbAb <= 0; n_Abbb <= 0; n_AABAb <= 0; n_AAbAb <= 0; n_ABABB <= 0; n_ABaBB <= 0;
    end else begin
        done <= 1'b0;

        case (state)
          ST_IDLE: begin
            busy <= 1'b0;
            if (start) begin
                A_reg <= A_in;
                B_reg <= B_in;
                invA_reg <= inverse_perm(A_in);
                invB_reg <= inverse_perm(B_in);
                mode_reg <= mode_in;

                input_valid <= 1'b0;
                fingerprint_valid <= 1'b0;
                status <= 3'd0;
                raw_signature <= 24'h000000;
                observed_signature <= 24'h000000;
                repaired_signature <= 24'h000000;
                erased_idx_reg <= 3'd0;
                op_idx <= 4'd0;
                probe_idx <= 3'd0;
                busy <= 1'b1;
                state <= ST_CHECK;
            end
          end

          ST_CHECK: begin
            input_valid <= valid_A & valid_B;

            if (mode_reg > 4'd8) begin
                status <= 3'd4;
                raw_signature <= 24'h000000;
                observed_signature <= 24'h000000;
                repaired_signature <= 24'h000000;
                fingerprint_valid <= 1'b0;
                state <= ST_DONE;
            end else if (!(valid_A & valid_B)) begin
                status <= 3'd0;
                raw_signature <= 24'h000000;
                observed_signature <= 24'h000000;
                repaired_signature <= 24'h000000;
                fingerprint_valid <= 1'b0;
                state <= ST_DONE;
            end else begin
                op_idx <= 4'd0;
                state <= ST_COMPOSE;
            end
          end

          ST_COMPOSE: begin
            case (op_idx)
              4'd0:  n_AB     <= compose_result;
              4'd1:  n_Ab     <= compose_result;
              4'd2:  n_BB     <= compose_result;
              4'd3:  begin n_AAB   <= compose_result; class_perm <= compose_result; probe_idx <= 3'd0; end
              4'd4:  n_ABA    <= compose_result;
              4'd5:  n_ABa    <= compose_result;
              4'd6:  begin n_Abb   <= compose_result; class_perm <= compose_result; probe_idx <= 3'd1; end
              4'd7:  begin n_AAAB  <= compose_result; class_perm <= compose_result; probe_idx <= 3'd2; end
              4'd8:  n_AbAb   <= compose_result;
              4'd9:  begin n_Abbb  <= compose_result; class_perm <= compose_result; probe_idx <= 3'd3; end
              4'd10: begin n_AABAb <= compose_result; class_perm <= compose_result; probe_idx <= 3'd4; end
              4'd11: begin n_AAbAb <= compose_result; class_perm <= compose_result; probe_idx <= 3'd5; end
              4'd12: begin n_ABABB <= compose_result; class_perm <= compose_result; probe_idx <= 3'd6; end
              4'd13: begin n_ABaBB <= compose_result; class_perm <= compose_result; probe_idx <= 3'd7; end
              default: ;
            endcase

            case (op_idx)
              4'd3,4'd6,4'd7,4'd9,4'd10,4'd11,4'd12,4'd13:
                state <= ST_CLASSIFY;
              default: begin
                op_idx <= op_idx + 1'b1;
                state <= ST_COMPOSE;
              end
            endcase
          end

          ST_CLASSIFY: begin
            case (probe_idx)
              3'd0: raw_signature[23:21] <= class_code;
              3'd1: raw_signature[20:18] <= class_code;
              3'd2: raw_signature[17:15] <= class_code;
              3'd3: raw_signature[14:12] <= class_code;
              3'd4: raw_signature[11: 9] <= class_code;
              3'd5: raw_signature[ 8: 6] <= class_code;
              3'd6: raw_signature[ 5: 3] <= class_code;
              3'd7: raw_signature[ 2: 0] <= class_code;
            endcase

            if (op_idx == 4'd13) begin
                state <= ST_MASK;
            end else begin
                op_idx <= op_idx + 1'b1;
                state <= ST_COMPOSE;
            end
          end

          ST_MASK: begin
            observed_signature <= erase_signature(raw_signature, mode_reg);
            if (mode_reg == 4'd0)
                erased_idx_reg <= 3'd0;
            else
                erased_idx_reg <= mode_reg[2:0] - 3'd1;
            state <= ST_REPAIR;
          end

          ST_REPAIR: begin
            fingerprint_valid <= repair_valid;
            repaired_signature <= repair_valid ? repair_signature : 24'h000000;
            status <= repair_valid ? 3'd2 : 3'd1;
            state <= ST_DONE;
          end

          ST_DONE: begin
            busy <= 1'b0;
            done <= 1'b1;
            state <= ST_IDLE;
          end

          default: begin
            state <= ST_IDLE;
            busy <= 1'b0;
          end
        endcase
    end
end

endmodule
