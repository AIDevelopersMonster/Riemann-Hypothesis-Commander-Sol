`timescale 1ns/1ps
module tb_h17_lab02_waveform;

logic clk, rst, start;
logic [23:0] a_in, b_in;
logic [3:0] mode_in;
logic busy, done;
logic [2:0] status;
logic input_valid, fingerprint_valid;
logic [23:0] raw_signature, observed_signature, repaired_signature;

h17_lab02_controller dut(
  .clk(clk), .rst(rst), .start(start),
  .a_in(a_in), .b_in(b_in), .mode_in(mode_in),
  .busy(busy), .done(done), .status(status),
  .input_valid(input_valid), .fingerprint_valid(fingerprint_valid),
  .raw_signature(raw_signature),
  .observed_signature(observed_signature),
  .repaired_signature(repaired_signature)
);

// 20 MHz: slower than measured slow-corner Fmax = 24.52 MHz.
always #25 clk = ~clk;

initial begin
  clk=0; rst=1; start=0;
  a_in=0; b_in=0; mode_in=0;
  repeat(2) @(negedge clk);
  rst=0;

  @(negedge clk);
  a_in=24'h5e3b88;
  b_in=24'h7ecc11;
  mode_in=4'd1;
  start=1;

  @(negedge clk);
  start=0;

  wait(done===1'b1);
  #1;

  if(status!==3'd2 ||
     input_valid!==1'b1 ||
     fingerprint_valid!==1'b1 ||
     raw_signature!==24'h8d256a ||
     observed_signature!==24'hed256a ||
     repaired_signature!==24'h8d256a) begin
    $display("FAIL H17-LAB-02 waveform");
    $display("status=%0d raw=%h obs=%h rep=%h",
             status,raw_signature,observed_signature,repaired_signature);
    $fatal(1);
  end

  $display("PASS H17-LAB-02 waveform raw=%h observed=%h repaired=%h",
           raw_signature,observed_signature,repaired_signature);
  repeat(3) @(negedge clk);
  $finish;
end
endmodule
