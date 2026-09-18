`timescale 1ns/1ps

// H17 educational waveform testbench.
// One known generating pair, mode=1, with VCD output.

module tb_wave_one;
reg clk=0;
always #5 clk=~clk;

reg rst=1;
reg start=0;
reg [23:0] a=0,b=0;
reg [3:0] mode=0;

wire busy,done;
wire [2:0] status;
wire [6:0] oid;
wire [23:0] raw,obs,rep;

h17_core dut(
    .clk(clk), .rst(rst), .start(start),
    .a_in(a), .b_in(b), .mode_in(mode),
    .busy(busy), .done(done),
    .status(status), .orbit_id(oid),
    .raw_signature(raw),
    .observed_signature(obs),
    .repaired_signature(rep)
);

integer cycles=0;

initial begin
    $dumpfile("build/h17_lab04.vcd");
    $dumpvars(0,tb_wave_one);

    repeat(3) @(negedge clk);
    rst=0;

    @(negedge clk);
    a=24'h5e3b88;
    b=24'h7ecc11;
    mode=4'h1;
    start=1;

    @(negedge clk);
    start=0;

    while(!done && cycles<1800) begin
        @(posedge clk);
        #1;
        cycles=cycles+1;
    end

    if(!done) $fatal(1,"timeout");
    if(cycles!=1663) $fatal(1,"unexpected latency %0d",cycles);
    if(status!==3'd2 ||
       oid!==7'd0 ||
       raw!==24'h8d256a ||
       obs!==24'hed256a ||
       rep!==24'h8d256a)
        $fatal(1,
          "unexpected result s=%h id=%h raw=%h obs=%h rep=%h",
          status,oid,raw,obs,rep);

    $display("PASS LAB-04 waveform: cycles=%0d status=%0d orbit=%0d raw=%h observed=%h repaired=%h",
             cycles,status,oid,raw,obs,rep);

    repeat(2) @(posedge clk);
    $finish;
end

initial begin
    #1000000000;
    $fatal(1,"watchdog");
end
endmodule
