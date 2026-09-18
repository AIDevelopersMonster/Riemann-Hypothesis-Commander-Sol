`timescale 1ns/1ps

// Registered-controller test using the same LAB-01 vector files.
//
// In addition to result equivalence this test checks:
//   * start acceptance only when idle
//   * external input changes after start do not corrupt a transaction
//   * done is a one-cycle pulse
//   * reset clears pending work

module tb_h17_lab02_controller;

logic clk=0;
always #5 clk=~clk;

logic rst=1, start=0;
logic [23:0] a_in=0, b_in=0;
logic [3:0] mode_in=0;

logic busy,done;
logic [2:0] status;
logic input_valid,fingerprint_valid;
logic [23:0] raw_signature,observed_signature,repaired_signature;

h17_lab02_controller dut(
    .clk(clk),.rst(rst),.start(start),
    .a_in(a_in),.b_in(b_in),.mode_in(mode_in),
    .busy(busy),.done(done),.status(status),
    .input_valid(input_valid),
    .fingerprint_valid(fingerprint_valid),
    .raw_signature(raw_signature),
    .observed_signature(observed_signature),
    .repaired_signature(repaired_signature)
);

integer fd,rc,n;
reg [1023:0] file_name;
reg [23:0] ea,eb,eraw,eobs,erep;
reg [3:0] em,es;
reg [7:0] legacy_orbit_id;

task automatic launch_and_check;
begin
    @(negedge clk);
    a_in=ea; b_in=eb; mode_in=em; start=1'b1;

    @(negedge clk);
    start=1'b0;

    // Deliberately corrupt external inputs while busy. The controller must use
    // the copies latched on the accepted start edge.
    a_in=24'h000000;
    b_in=24'hffffff;
    mode_in=4'hf;
    start=1'b1;

    @(negedge clk);
    start=1'b0;

    if(!done) $fatal(1,"vector %0d: done missing",n);
    if(busy)  $fatal(1,"vector %0d: busy did not clear",n);

    if(status!==es[2:0] ||
       raw_signature!==eraw ||
       observed_signature!==eobs ||
       repaired_signature!==erep)
        $fatal(1,
          "vector %0d expected s=%h raw=%h obs=%h rep=%h got s=%h raw=%h obs=%h rep=%h",
          n,es,eraw,eobs,erep,
          status,raw_signature,observed_signature,repaired_signature);

    if((es==4'h2) !== fingerprint_valid)
        $fatal(1,"vector %0d: fingerprint_valid mismatch",n);

    @(negedge clk);
    if(done) $fatal(1,"vector %0d: done not one-cycle pulse",n);
end
endtask

initial begin
    if(!$value$plusargs("VECTORS=%s",file_name))
        file_name="vectors/quick.txt";

    repeat(3) @(negedge clk);
    rst=0;

    // Abort a pending operation with reset.
    a_in=24'h5e3b88; b_in=24'h7ecc11; mode_in=4'd1; start=1;
    @(negedge clk); start=0;
    rst=1;
    @(negedge clk); rst=0;
    if(busy || done) $fatal(1,"reset failed to clear transaction");

    fd=$fopen(file_name,"r");
    if(!fd) $fatal(1,"vectors missing: %0s",file_name);

    n=0;
    while(!$feof(fd)) begin
        rc=$fscanf(fd,"%h %h %h %h %h %h %h %h\n",
                   ea,eb,em,es,legacy_orbit_id,eraw,eobs,erep);
        if(rc!=8) $fatal(1,"malformed vector %0d",n);
        launch_and_check();
        n=n+1;
    end

    $fclose(fd);
    $display("PASS H17-LAB-02 controller: %0d vectors; input latch, busy/done and reset checked",n);
    $finish;
end

initial begin
    #1000000000;
    $fatal(1,"controller watchdog");
end

endmodule
