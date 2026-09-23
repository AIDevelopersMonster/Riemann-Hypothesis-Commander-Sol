module tb_h21_b0_rtl;
  localparam W=12;
  reg clk=0,rst=1,start=0;
  reg [W-1:0] n,c;
  wire sbusy,sdone,qbusy,qdone;
  wire [W-1:0] sres,q0,q1;
  wire [31:0] scyc,qcyc;
  integer failures=0;
  integer total=0;

  h21_scalar_pow #(W) S(.clk(clk),.rst(rst),.start(start),.n(n),.cmod(c),.busy(sbusy),.done(sdone),.result(sres),.cycles(scyc));
  h21_quad_pow_b0 #(W) Q(.clk(clk),.rst(rst),.start(start),.n(n),.cmod(c),.busy(qbusy),.done(qdone),.y0(q0),.y1(q1),.cycles(qcyc));

  always #5 clk=~clk;

  task runvec(input integer nn,input integer cc);
    integer gotS,gotQ;
    reg [31:0] cs,cq;
    begin
      @(negedge clk); n=nn; c=cc; start=1;
      @(negedge clk); start=0;
      wait(sdone); cs=scyc; gotS=sres;
      wait(qdone); cq=qcyc; gotQ=q1;
      total=total+1;
      if(q0!==0 || gotS!==gotQ) begin
        $display("FAIL n=%0d C=%0d scalar=%0d quad=(%0d,%0d)",nn,cc,gotS,q0,gotQ);
        failures=failures+1;
      end else begin
        $display("PASSV n=%0d C=%0d scalar_cycles=%0d quad_cycles=%0d scalar=%0d",nn,cc,cs,cq,gotS);
      end
    end
  endtask

  initial begin
    repeat(4) @(negedge clk); rst=0;
    runvec(101,3);
    runvec(91,5);
    runvec(221,7);
    runvec(341,3);
    runvec(899,5);
    runvec(1009,11);
    runvec(1729,7);
    runvec(2047,3);
    runvec(3001,17);
    $display("SUMMARY vectors=%0d failures=%0d",total,failures);
    if(failures) $fatal(1,"RTL mismatch");
    $finish;
  end
endmodule
