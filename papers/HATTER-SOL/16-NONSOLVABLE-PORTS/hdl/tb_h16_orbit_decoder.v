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

        clk = 0;
        rst_n = 0;
        valid_in = 0;
        class_A = 0;
        class_B = 0;
        class_AB = 0;
        class_AB_inv = 0;
        class_K = 0;

        #20 rst_n = 1;
        #10;

        // Golden Vector 1: commutator class 7A -> Q4=+1.
        class_A = 3'd3;
        class_B = 3'd3;
        class_AB = 3'd2;
        class_AB_inv = 3'd3;
        class_K = 3'd4;
        valid_in = 1;
        #10;

        // Golden Vector 2: same first four probes, commutator class 7B -> Q4=-1.
        class_A = 3'd3;
        class_B = 3'd3;
        class_AB = 3'd2;
        class_AB_inv = 3'd3;
        class_K = 3'd5;
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
