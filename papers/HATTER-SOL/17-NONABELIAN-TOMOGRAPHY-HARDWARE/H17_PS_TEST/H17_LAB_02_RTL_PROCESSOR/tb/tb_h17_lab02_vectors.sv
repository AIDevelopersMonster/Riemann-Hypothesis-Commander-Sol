`timescale 1ns/1ps
// H17-LAB-02 pure-RTL vector test.
//
// Uses the SAME golden vector format as LAB-01, but tests the closure-aware
// + ROM-free architecture directly.
//
// Columns:
// A B mode status legacy_orbit_id raw observed repaired
//
// legacy_orbit_id is read and ignored deliberately. The mathematical output
// of LAB-02 is the repaired 24-bit fingerprint.

module tb_h17_lab02_vectors;

logic [23:0] A, B;
logic [3:0]  mode;
logic        input_valid;
logic        fingerprint_valid;
logic [2:0]  status;
logic [23:0] raw_signature;
logic [23:0] observed_signature;
logic [23:0] repaired_signature;

h17_lab02_core dut(
    .A(A), .B(B), .mode(mode),
    .input_valid(input_valid),
    .fingerprint_valid(fingerprint_valid),
    .status(status),
    .raw_signature(raw_signature),
    .observed_signature(observed_signature),
    .repaired_signature(repaired_signature)
);

integer fd, rc, n;
reg [1023:0] file_name;
reg [23:0] ea, eb, eraw, eobs, erep;
reg [3:0]  em, es;
reg [7:0]  legacy_orbit_id;

initial begin
    A=0; B=0; mode=0; n=0;

    if (!$value$plusargs("VECTORS=%s",file_name))
        file_name="vectors/quick.txt";

    fd=$fopen(file_name,"r");
    if(!fd) $fatal(1,"vectors missing: %0s",file_name);

    while(!$feof(fd)) begin
        rc=$fscanf(fd,"%h %h %h %h %h %h %h %h\n",
                   ea,eb,em,es,legacy_orbit_id,eraw,eobs,erep);
        if(rc!=8) $fatal(1,"malformed vector %0d",n);

        A=ea; B=eb; mode=em;
        #1;

        if(status!==es[2:0] ||
           raw_signature!==eraw ||
           observed_signature!==eobs ||
           repaired_signature!==erep) begin
            $fatal(1,
              "vector %0d A=%h B=%h mode=%h expected s=%h raw=%h obs=%h rep=%h got s=%h raw=%h obs=%h rep=%h",
              n,ea,eb,em,es,eraw,eobs,erep,
              status,raw_signature,observed_signature,repaired_signature);
        end

        if((es==4'h2) !== fingerprint_valid)
            $fatal(1,"fingerprint_valid mismatch at vector %0d",n);

        n=n+1;
    end

    $fclose(fd);
    $display("PASS H17-LAB-02 pure RTL: %0d vectors; closure-aware frontend + ROM-free fingerprint",n);
    $finish;
end

endmodule
