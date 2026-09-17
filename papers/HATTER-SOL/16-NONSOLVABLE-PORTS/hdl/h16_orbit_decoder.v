`timescale 1ns/1ps

module h16_orbit_decoder (
    input  wire       clk,
    input  wire       rst_n,
    input  wire       valid_in,
    input  wire [2:0] class_A,
    input  wire [2:0] class_B,
    input  wire [2:0] class_AB,
    input  wire [2:0] class_AB_inv,
    input  wire [2:0] class_K,

    output reg        valid_out,
    output reg  [1:0] q4_orientation,
    output reg  [6:0] orbit_id
);

    // Combinational Q4 orientation state from the commutator class.
    wire [1:0] q4_next;
    assign q4_next = (class_K == 3'd4) ? 2'b01 : // 7A -> +1
                     (class_K == 3'd5) ? 2'b10 : // 7B -> -1
                                         2'b00;  // 1A,2A,3A,4A -> 0

    // Five 3-bit class probes packed into one 15-bit signature.
    wire [14:0] signature = {class_A, class_B, class_AB, class_AB_inv, class_K};

    // Demonstration LUT. H17 will replace this with the complete canonical
    // 114-orbit table generated from the exact H16 certificate.
    reg [6:0] lut_orbit;

    always @(*) begin
        case (signature)
            15'b011_011_010_011_100: lut_orbit = 7'd42; // Golden 7A vector
            15'b011_011_010_011_101: lut_orbit = 7'd43; // Golden 7B vector
            default:                  lut_orbit = 7'h7F; // Unknown signature
        endcase
    end

    // One-stage synchronous registered output.
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            valid_out      <= 1'b0;
            q4_orientation <= 2'b00;
            orbit_id       <= 7'd0;
        end else begin
            valid_out      <= valid_in;
            q4_orientation <= q4_next;
            orbit_id       <= lut_orbit;
        end
    end

endmodule
