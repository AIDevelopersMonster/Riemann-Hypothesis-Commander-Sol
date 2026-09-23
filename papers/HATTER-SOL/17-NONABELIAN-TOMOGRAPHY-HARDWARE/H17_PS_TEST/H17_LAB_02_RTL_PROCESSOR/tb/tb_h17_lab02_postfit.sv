`timescale 1ps/1ps
module tb_h17_lab02_postfit;

reg clk, rst, start;
reg [23:0] a_in, b_in;
reg [3:0] mode_in;
wire busy, done;
wire [2:0] status;
wire input_valid, fingerprint_valid;
wire [23:0] raw_signature, observed_signature, repaired_signature;

h17_lab02_controller dut(
  .clk(clk), .rst(rst), .start(start),
  .a_in(a_in), .b_in(b_in), .mode_in(mode_in),
  .busy(busy), .done(done), .status(status),
  .input_valid(input_valid), .fingerprint_valid(fingerprint_valid),
  .raw_signature(raw_signature),
  .observed_signature(observed_signature),
  .repaired_signature(repaired_signature)
);

// 50 ns period = 20 MHz. The fitted Cyclone IV slow-corner
// one-cycle Fmax measured by TimeQuest is 24.52 MHz.
always #25000 clk = ~clk;

initial begin
  clk=0; rst=1; start=0; a_in=0; b_in=0; mode_in=0;
  repeat (2) @(negedge clk);
  rst=0;

  @(negedge clk);
  a_in=24'h5e3b88;
  b_in=24'h7ecc11;
  mode_in=4'd1;
  start=1;

  @(negedge clk);
  start=0;

  wait(done===1'b1);
  // Allow clock-to-Q propagation in the post-fit netlist.
  #5000;

  if(status!==3'd2 || input_valid!==1'b1 || fingerprint_valid!==1'b1 ||
     raw_signature!==24'h8d256a || observed_signature!==24'hed256a ||
     repaired_signature!==24'h8d256a) begin
    $display("FAIL POSTFIT status=%0d iv=%b fv=%b raw=%h obs=%h rep=%h",
      status,input_valid,fingerprint_valid,raw_signature,observed_signature,repaired_signature);
    $fatal(1);
  end

  $display("PASS POSTFIT raw=%h observed=%h repaired=%h status=%0d",
    raw_signature,observed_signature,repaired_signature,status);
  repeat(3) @(negedge clk);
  $finish;
end
endmodule
