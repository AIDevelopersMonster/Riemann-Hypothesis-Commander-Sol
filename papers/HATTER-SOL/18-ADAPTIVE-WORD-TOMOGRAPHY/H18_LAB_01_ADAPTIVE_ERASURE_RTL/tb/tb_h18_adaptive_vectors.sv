\`timescale 1ns/1ps
// Generated-vector regression for H18-07 adaptive erasure RTL.

module tb_h18_adaptive_vectors;

logic clk=0, rst=0, start=0;
logic [23:0] A_in, B_in;
logic [2:0] erase_attempt_idx;
logic busy, done;
logic [2:0] status;
logic [6:0] orbit_id;
logic [2:0] attempts, successes;

h18_adaptive_sequential_core dut(
    .clk(clk), .rst(rst), .start(start),
    .A_in(A_in), .B_in(B_in),
    .erase_attempt_idx(erase_attempt_idx),
    .busy(busy), .done(done),
    .status(status), .orbit_id(orbit_id),
    .attempts(attempts), .successes(successes)
);

always #5 clk=~clk;

integer fd, rc, n, wait_cycles;
reg [1023:0] file_name, line;
reg [23:0] ea, eb;
reg [3:0] ee, es, eattempts, esuccesses;
reg [7:0] eorbit;

initial begin
    A_in=0; B_in=0; erase_attempt_idx=0;
    rst=1; repeat(2) @(posedge clk); rst=0;

    if(!$value$plusargs("VECTORS=%s",file_name))
        file_name="generated/h18_adaptive_vectors.txt";

    fd=$fopen(file_name,"r");
    if(!fd) $fatal(1,"vectors missing: %0s",file_name);

    // Skip header.
    rc=$fgets(line,fd);
    n=0;

    while(!$feof(fd)) begin
        rc=$fscanf(fd,"%h %h %h %h %h %h %h\n",
                   ea,eb,ee,es,eorbit,eattempts,esuccesses);
        if(rc==0) break;
        if(rc!=7) $fatal(1,"malformed vector %0d",n);

        while(busy) @(posedge clk);
        A_in=ea; B_in=eb; erase_attempt_idx=ee[2:0];
        start=1; @(posedge clk); start=0;

        wait_cycles=0;
        while(!done) begin
            @(posedge clk);
            wait_cycles=wait_cycles+1;
            if(wait_cycles>100) $fatal(1,"timeout vector %0d",n);
        end

        if(status!==es[2:0] ||
           orbit_id!==eorbit[6:0] ||
           attempts!==eattempts[2:0] ||
           successes!==esuccesses[2:0]) begin
            $fatal(1,
              "vector %0d A=%h B=%h erase=%0d expected s=%0d oid=%0d a=%0d ok=%0d got s=%0d oid=%0d a=%0d ok=%0d",
              n,ea,eb,ee,es,eorbit,eattempts,esuccesses,
              status,orbit_id,attempts,successes);
        end

        n=n+1;
        if((n%100)==0)
            $display("PROGRESS H18-LAB-01: %0d vectors",n);
        @(posedge clk);
    end

    $fclose(fd);
    $display("PASS H18-LAB-01 adaptive RTL: %0d vectors",n);
    $finish;
end
endmodule
