# Appendix A · HDL proof-of-concept for the H16 orbit decoder

This appendix records the first hardware-facing validation of the frozen HATTER-SOL-16 engineering interface. It is intentionally a **proof of concept**, not yet the full HATTER-SOL-17 implementation.

The tested block realizes the final H16 data path

\[
\boxed{
\text{five class probes}
\to
\text{15-bit signature}
\to
Q_4\text{ orientation state}
\to
\text{orbit LUT/ROM}.
}
\]

The five class inputs correspond to

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad K=[A,B].
\]

A 3-bit class encoding is used:

| class | code |
|---|---|
| `1A` | `000` |
| `2A` | `001` |
| `3A` | `010` |
| `4A` | `011` |
| `7A` | `100` |
| `7B` | `101` |

The orientation output uses

\[
Q_4=0\mapsto 00,
\qquad
Q_4=+1\mapsto 01,
\qquad
Q_4=-1\mapsto 10.
\]

The first two golden vectors differ only in the commutator class and verify the exact `7A/7B` orientation split:

```text
011_011_010_011_100 -> orbit 42, Q4=+1
011_011_010_011_101 -> orbit 43, Q4=-1
```

The assigned orbit IDs in this proof-of-concept are demonstration LUT entries; the complete 114-entry canonical ROM is deliberately left to HATTER-SOL-17.

## Verilog module

```verilog
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

    wire [1:0] q4_next;
    assign q4_next = (class_K == 3'd4) ? 2'b01 : // 7A -> +1
                     (class_K == 3'd5) ? 2'b10 : // 7B -> -1
                                         2'b00;  // 3A, 4A -> 0

    wire [14:0] signature = {class_A, class_B, class_AB, class_AB_inv, class_K};

    reg [6:0] lut_orbit;

    always @(*) begin
        case (signature)
            15'b011_011_010_011_100: lut_orbit = 7'd42;
            15'b011_011_010_011_101: lut_orbit = 7'd43;
            default:                  lut_orbit = 7'h7F;
        endcase
    end

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
```

## Testbench

```verilog
`timescale 1ns/1ps

module tb_h16_orbit_decoder;

    reg        clk;
    reg        rst_n;
    reg        valid_in;
    reg  [2:0] class_A, class_B, class_AB, class_AB_inv, class_K;

    wire       valid_out;
    wire [1:0] q4_orientation;
    wire [6:0] orbit_id;

    h16_orbit_decoder dut (
        .clk(clk),
        .rst_n(rst_n),
        .valid_in(valid_in),
        .class_A(class_A),
        .class_B(class_B),
        .class_AB(class_AB),
        .class_AB_inv(class_AB_inv),
        .class_K(class_K),
        .valid_out(valid_out),
        .q4_orientation(q4_orientation),
        .orbit_id(orbit_id)
    );

    always #5 clk = ~clk;

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars(0, tb_h16_orbit_decoder);

        clk = 0; rst_n = 0; valid_in = 0;
        class_A = 0; class_B = 0; class_AB = 0; class_AB_inv = 0; class_K = 0;

        #20 rst_n = 1;
        #10;

        class_A = 3'd3; class_B = 3'd3; class_AB = 3'd2; class_AB_inv = 3'd3; class_K = 3'd4;
        valid_in = 1;
        #10;

        class_A = 3'd3; class_B = 3'd3; class_AB = 3'd2; class_AB_inv = 3'd3; class_K = 3'd5;
        #10;

        valid_in = 0;
        #20 $finish;
    end

    always @(posedge clk) begin
        if (valid_out) begin
            $display("[T=%0t ps] Orbit ID = %0d | Q4 State = %b (%s)",
                     $time, orbit_id, q4_orientation,
                     (q4_orientation == 2'b01) ? "+1 (7A)" :
                     (q4_orientation == 2'b10) ? "-1 (7B)" : "0");
        end
    end

endmodule
```

## Interpretation

This experiment validates three implementation facts already proved mathematically in H16:

1. the five-probe signature fits into a compact fixed-width interface;
2. the orientation bit is extracted by a trivial combinational map from the commutator class;
3. orbit recovery can be implemented as a finite lookup stage followed by a synchronous registered output.

The present appendix deliberately does **not** claim a complete 114-orbit hardware decoder, synthesis result, fixed-point robustness, timing closure, or physical-board demonstration. Those belong to HATTER-SOL-17.

For the publication package, the corresponding interactive HTML visualization is distributed as `HATTER_SOL_16_PSL27_HTML_DEMO_v1.0.html`.
