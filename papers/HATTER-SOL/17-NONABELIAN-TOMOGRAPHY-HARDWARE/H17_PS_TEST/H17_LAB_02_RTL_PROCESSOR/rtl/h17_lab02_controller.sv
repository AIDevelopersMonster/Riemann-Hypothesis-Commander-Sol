// H17-LAB-02 registered controller wrapper.
//
// This wrapper turns the pure combinational mathematical core into a normal
// start/busy/done transaction interface without changing the mathematics.
//
// Accepted transaction:
//   start=1 while busy=0
//     -> latch A,B,mode
//     -> compute through h17_lab02_core
//     -> capture outputs on the next clock
//     -> pulse done for one clock
//
// Latency is intentionally one registered result cycle, not LAB-01's 1663
// cycle sequential-table latency.

module h17_lab02_controller(
    input  logic        clk,
    input  logic        rst,
    input  logic        start,
    input  logic [23:0] a_in,
    input  logic [23:0] b_in,
    input  logic [3:0]  mode_in,

    output logic        busy,
    output logic        done,
    output logic [2:0]  status,
    output logic        input_valid,
    output logic        fingerprint_valid,
    output logic [23:0] raw_signature,
    output logic [23:0] observed_signature,
    output logic [23:0] repaired_signature
);

logic [23:0] a_q, b_q;
logic [3:0]  mode_q;
logic        pending;

logic        core_input_valid;
logic        core_fingerprint_valid;
logic [2:0]  core_status;
logic [23:0] core_raw;
logic [23:0] core_observed;
logic [23:0] core_repaired;

h17_lab02_core u_core(
    .A(a_q),
    .B(b_q),
    .mode(mode_q),
    .input_valid(core_input_valid),
    .fingerprint_valid(core_fingerprint_valid),
    .status(core_status),
    .raw_signature(core_raw),
    .observed_signature(core_observed),
    .repaired_signature(core_repaired)
);

always_ff @(posedge clk) begin
    if (rst) begin
        a_q <= 24'h0;
        b_q <= 24'h0;
        mode_q <= 4'h0;
        pending <= 1'b0;
        busy <= 1'b0;
        done <= 1'b0;
        status <= 3'd0;
        input_valid <= 1'b0;
        fingerprint_valid <= 1'b0;
        raw_signature <= 24'h0;
        observed_signature <= 24'h0;
        repaired_signature <= 24'h0;
    end else begin
        done <= 1'b0;

        if (!busy && start) begin
            // Transaction acceptance point. External inputs may change after
            // this edge; computation uses only these latched copies.
            a_q <= a_in;
            b_q <= b_in;
            mode_q <= mode_in;
            pending <= 1'b1;
            busy <= 1'b1;

            status <= 3'd0;
            input_valid <= 1'b0;
            fingerprint_valid <= 1'b0;
            raw_signature <= 24'h0;
            observed_signature <= 24'h0;
            repaired_signature <= 24'h0;
        end else if (pending) begin
            // One full cycle has elapsed since the input latch. Capture the
            // pure-RTL result and complete the transaction.
            status <= core_status;
            input_valid <= core_input_valid;
            fingerprint_valid <= core_fingerprint_valid;
            raw_signature <= core_raw;
            observed_signature <= core_observed;
            repaired_signature <= core_repaired;

            pending <= 1'b0;
            busy <= 1'b0;
            done <= 1'b1;
        end
    end
end

endmodule
