`timescale 1ns/1ps
// H17-LAB-03 sequential vector regression.
//
// Golden row format is identical to LAB-01 / LAB-02:
// A B mode status legacy_orbit_id raw observed repaired
//
// The legacy orbit_id column is intentionally ignored.

module tb_h17_lab03_vectors;

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

integer fd, rc, n;
integer cycles_this, max_cycles;
reg [1023:0] file_name;
reg [23:0] ea, eb, eraw, eobs, erep;
reg [3:0] em, es;
reg [7:0] legacy_orbit_id;

task automatic run_vector;
begin
    // Drive away from the active edge.
    @(negedge clk);
    A_in = ea;
    B_in = eb;
    mode_in = em;
    start = 1'b1;

    @(negedge clk);
    start = 1'b0;

    cycles_this = 0;
    while (!done && cycles_this < 80) begin
        @(negedge clk);
        cycles_this = cycles_this + 1;
    end

    if (!done)
        $fatal(1,"timeout vector %0d after %0d cycles",n,cycles_this);

    if (cycles_this > max_cycles)
        max_cycles = cycles_this;

    if (status !== es[2:0] ||
        raw_signature !== eraw ||
        observed_signature !== eobs ||
        repaired_signature !== erep) begin
        $fatal(1,
          "vector %0d A=%h B=%h mode=%h expected s=%h raw=%h obs=%h rep=%h got s=%h raw=%h obs=%h rep=%h",
          n,ea,eb,em,es,eraw,eobs,erep,
          status,raw_signature,observed_signature,repaired_signature);
    end

    if ((es==4'h2) !== fingerprint_valid)
        $fatal(1,"fingerprint_valid mismatch at vector %0d",n);
end
endtask

initial begin
    clk=0; rst=1; start=0; A_in=0; B_in=0; mode_in=0;
    n=0; max_cycles=0;

    repeat(3) @(negedge clk);
    rst=0;

    if (!$value$plusargs("VECTORS=%s",file_name))
        file_name="../H17_LAB_COMPLETE_clean/vectors/quick.txt";

    fd=$fopen(file_name,"r");
    if(!fd) $fatal(1,"vectors missing: %0s",file_name);

    while(!$feof(fd)) begin
        rc=$fscanf(fd,"%h %h %h %h %h %h %h %h\n",
                   ea,eb,em,es,legacy_orbit_id,eraw,eobs,erep);
        if(rc!=8) $fatal(1,"malformed vector %0d",n);

        run_vector();
        n=n+1;

        if((n % 25)==0)
            $display("PROGRESS H17-LAB-03: %0d vectors; sim_time=%0t; max_wait_cycles=%0d",
                     n,$time,max_cycles);
    end

    $fclose(fd);
    $display("PASS H17-LAB-03 sequential RTL: %0d vectors; max_wait_cycles=%0d",n,max_cycles);
    $finish;
end

endmodule
