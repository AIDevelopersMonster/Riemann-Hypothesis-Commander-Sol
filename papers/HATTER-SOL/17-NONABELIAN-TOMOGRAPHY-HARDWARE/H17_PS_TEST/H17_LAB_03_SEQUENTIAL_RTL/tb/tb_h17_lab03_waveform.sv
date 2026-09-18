`timescale 1ns/1ps
// H17-LAB-03 publication waveform test.
//
// One canonical generating vector with mode=1:
//   A=5e3b88, B=7ecc11
//   raw      = 8d256a
//   observed = ed256a  (probe 0 erased)
//   repaired = 8d256a
//
// The dump intentionally includes controller state and the shared datapath so
// the 26-cycle transaction can be inspected in GTKWave.

module tb_h17_lab03_waveform;

logic clk, rst, start;
logic [23:0] A_in, B_in;
logic [3:0] mode_in;
logic busy, done, input_valid, fingerprint_valid;
logic [2:0] status;
logic [23:0] raw_signature, observed_signature, repaired_signature;

h17_lab03_sequential_core dut(
    .clk(clk), .rst(rst), .start(start),
    .A_in(A_in), .B_in(B_in), .mode_in(mode_in),
    .busy(busy), .done(done),
    .input_valid(input_valid),
    .fingerprint_valid(fingerprint_valid),
    .status(status),
    .raw_signature(raw_signature),
    .observed_signature(observed_signature),
    .repaired_signature(repaired_signature)
);

always #5 clk = ~clk;

integer wait_cycles;

initial begin
    $dumpfile("build/h17_lab03_waveform.vcd");
    $dumpvars(0, tb_h17_lab03_waveform);

    clk=0;
    rst=1;
    start=0;
    A_in=24'h000000;
    B_in=24'h000000;
    mode_in=4'd0;
    wait_cycles=0;

    repeat(3) @(negedge clk);
    rst=0;

    @(negedge clk);
    A_in=24'h5e3b88;
    B_in=24'h7ecc11;
    mode_in=4'd1;
    start=1'b1;

    @(negedge clk);
    start=1'b0;

    while(!done && wait_cycles < 80) begin
        @(negedge clk);
        wait_cycles=wait_cycles+1;
    end

    if(!done)
        $fatal(1,"waveform transaction timeout");

    if(status!==3'd2 ||
       raw_signature!==24'h8d256a ||
       observed_signature!==24'hed256a ||
       repaired_signature!==24'h8d256a ||
       !fingerprint_valid)
        $fatal(1,
          "waveform mismatch wait=%0d status=%0d raw=%h obs=%h rep=%h valid=%b",
          wait_cycles,status,raw_signature,observed_signature,
          repaired_signature,fingerprint_valid);

    $display("PASS H17-LAB-03 waveform: wait_cycles=%0d raw=%h observed=%h repaired=%h",
             wait_cycles,raw_signature,observed_signature,repaired_signature);

    // Keep the terminal values visible for two extra clock periods in the VCD.
    repeat(2) @(negedge clk);
    $finish;
end

endmodule
