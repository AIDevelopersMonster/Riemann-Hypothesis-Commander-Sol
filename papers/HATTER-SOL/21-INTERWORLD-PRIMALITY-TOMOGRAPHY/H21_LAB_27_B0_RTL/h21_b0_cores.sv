module h21_modmul_seq #(parameter W=12) (
    input  wire             clk,
    input  wire             rst,
    input  wire             start,
    input  wire [W-1:0]     a,
    input  wire [W-1:0]     b,
    input  wire [W-1:0]     modn,
    output reg              busy,
    output reg              done,
    output reg  [W-1:0]     result
);
    reg [W:0] acc, acur;
    reg [W-1:0] bcur, nreg;
    integer count;
    reg [W:0] sumv, dblv, next_acc, next_a;

    always @* begin
        sumv = acc + (bcur[0] ? acur : {W+1{1'b0}});
        if (sumv >= {1'b0,nreg}) next_acc = sumv - {1'b0,nreg};
        else next_acc = sumv;
        dblv = acur << 1;
        if (dblv >= {1'b0,nreg}) next_a = dblv - {1'b0,nreg};
        else next_a = dblv;
    end

    always @(posedge clk) begin
        if (rst) begin
            busy <= 0; done <= 0; result <= 0; acc <= 0; acur <= 0;
            bcur <= 0; nreg <= 0; count <= 0;
        end else begin
            done <= 0;
            if (start && !busy) begin
                busy <= 1;
                acc <= 0;
                acur <= {1'b0,a};
                bcur <= b;
                nreg <= modn;
                count <= 0;
            end else if (busy) begin
                acc <= next_acc;
                acur <= next_a;
                bcur <= bcur >> 1;
                if (count == W-1) begin
                    result <= next_acc[W-1:0];
                    busy <= 0;
                    done <= 1;
                end else begin
                    count <= count + 1;
                end
            end
        end
    end
endmodule


module h21_scalar_pow #(parameter W=12) (
    input  wire             clk,
    input  wire             rst,
    input  wire             start,
    input  wire [W-1:0]     n,
    input  wire [W-1:0]     cmod,
    output reg              busy,
    output reg              done,
    output reg  [W-1:0]     result,
    output reg  [31:0]      cycles
);
    localparam IDLE=0, SQ_L=1, SQ_W=2, MU_L=3, MU_W=4;
    reg [2:0] state;
    reg [W-1:0] expreg, basereg, acc, nreg;
    integer idx;
    reg mm_start;
    reg [W-1:0] mm_a, mm_b;
    wire mm_busy, mm_done;
    wire [W-1:0] mm_result;

    h21_modmul_seq #(W) mm(
        .clk(clk),.rst(rst),.start(mm_start),.a(mm_a),.b(mm_b),.modn(nreg),
        .busy(mm_busy),.done(mm_done),.result(mm_result)
    );

    function integer msb_index;
        input [W-1:0] v;
        integer i;
        begin
            msb_index = 0;
            for (i=0;i<W;i=i+1)
                if (v[i]) msb_index = i;
        end
    endfunction

    always @(posedge clk) begin
        if (rst) begin
            state<=IDLE; busy<=0; done<=0; result<=0; cycles<=0;
            mm_start<=0; mm_a<=0; mm_b<=0; expreg<=0; basereg<=0; acc<=0; nreg<=0; idx<=0;
        end else begin
            done<=0; mm_start<=0;
            if (busy) cycles<=cycles+1;
            case(state)
              IDLE: if (start) begin
                  nreg<=n;
                  expreg<=(n-1'b1)>>1;
                  basereg<=cmod;
                  acc<=cmod;
                  cycles<=0; busy<=1;
                  if (((n-1'b1)>>1) <= 1) begin
                      result<=cmod; done<=1; busy<=0; state<=IDLE;
                  end else begin
                      idx<=msb_index((n-1'b1)>>1)-1;
                      state<=SQ_L;
                  end
              end
              SQ_L: begin mm_a<=acc; mm_b<=acc; mm_start<=1; state<=SQ_W; end
              SQ_W: if (mm_done) begin
                  acc<=mm_result;
                  if (expreg[idx]) state<=MU_L;
                  else if (idx==0) begin result<=mm_result; done<=1; busy<=0; state<=IDLE; end
                  else begin idx<=idx-1; state<=SQ_L; end
              end
              MU_L: begin mm_a<=acc; mm_b<=basereg; mm_start<=1; state<=MU_W; end
              MU_W: if (mm_done) begin
                  acc<=mm_result;
                  if (idx==0) begin result<=mm_result; done<=1; busy<=0; state<=IDLE; end
                  else begin idx<=idx-1; state<=SQ_L; end
              end
            endcase
        end
    end
endmodule


module h21_quadmul_b0_seq #(parameter W=12) (
    input wire clk, rst, start,
    input wire [W-1:0] a0,a1,b0,b1,cmod,modn,
    output reg busy, done,
    output reg [W-1:0] y0,y1
);
    localparam IDLE=0,M0L=1,M0W=2,M1L=3,M1W=4,M2L=5,M2W=6,MCL=7,MCW=8;
    reg [3:0] state;
    reg [W-1:0] A0,A1,B0,B1,C,N,m0,m1,m2;
    reg mm_start; reg [W-1:0] mm_a,mm_b;
    wire mm_busy,mm_done; wire [W-1:0] mm_result;

    h21_modmul_seq #(W) mm(
        .clk(clk),.rst(rst),.start(mm_start),.a(mm_a),.b(mm_b),.modn(N),
        .busy(mm_busy),.done(mm_done),.result(mm_result)
    );

    function [W-1:0] addm;
        input [W-1:0] x,y,nv;
        reg [W:0] t;
        begin t={1'b0,x}+{1'b0,y}; if(t>=nv)t=t-nv; addm=t[W-1:0]; end
    endfunction
    function [W-1:0] subm;
        input [W-1:0] x,y,nv;
        begin if(x>=y)subm=x-y; else subm=x+nv-y; end
    endfunction

    always @(posedge clk) begin
      if(rst) begin state<=IDLE;busy<=0;done<=0;y0<=0;y1<=0;mm_start<=0; end
      else begin
        done<=0;mm_start<=0;
        case(state)
          IDLE: if(start) begin A0<=a0;A1<=a1;B0<=b0;B1<=b1;C<=cmod;N<=modn;busy<=1;state<=M0L; end
          M0L: begin mm_a<=A0;mm_b<=B0;mm_start<=1;state<=M0W;end
          M0W: if(mm_done) begin m0<=mm_result;state<=M1L;end
          M1L: begin mm_a<=A1;mm_b<=B1;mm_start<=1;state<=M1W;end
          M1W: if(mm_done) begin m1<=mm_result;state<=M2L;end
          M2L: begin mm_a<=addm(A0,A1,N);mm_b<=addm(B0,B1,N);mm_start<=1;state<=M2W;end
          M2W: if(mm_done) begin m2<=mm_result;state<=MCL;end
          MCL: begin mm_a<=m1;mm_b<=C;mm_start<=1;state<=MCW;end
          MCW: if(mm_done) begin
             y0<=addm(m0,mm_result,N);
             y1<=subm(subm(m2,m0,N),m1,N);
             busy<=0;done<=1;state<=IDLE;
          end
        endcase
      end
    end
endmodule


module h21_quad_pow_b0 #(parameter W=12) (
    input wire clk,rst,start,
    input wire [W-1:0] n,cmod,
    output reg busy,done,
    output reg [W-1:0] y0,y1,
    output reg [31:0] cycles
);
    localparam IDLE=0,SQL=1,SQW=2,MUL=3,MUW=4;
    reg [2:0] state;
    reg [W-1:0] expreg,nreg,creg,a0,a1,base0,base1;
    integer idx;
    reg q_start;
    reg [W-1:0] qa0,qa1,qb0,qb1;
    wire q_busy,q_done; wire [W-1:0] qy0,qy1;

    h21_quadmul_b0_seq #(W) qm(
      .clk(clk),.rst(rst),.start(q_start),
      .a0(qa0),.a1(qa1),.b0(qb0),.b1(qb1),.cmod(creg),.modn(nreg),
      .busy(q_busy),.done(q_done),.y0(qy0),.y1(qy1)
    );

    function integer msb_index;
      input [W-1:0] v; integer i;
      begin msb_index=0; for(i=0;i<W;i=i+1)if(v[i])msb_index=i; end
    endfunction

    always @(posedge clk) begin
      if(rst) begin state<=IDLE;busy<=0;done<=0;y0<=0;y1<=0;cycles<=0;q_start<=0; end
      else begin
        done<=0;q_start<=0;if(busy)cycles<=cycles+1;
        case(state)
          IDLE: if(start) begin
            nreg<=n;creg<=cmod;expreg<=n;base0<=0;base1<=1;a0<=0;a1<=1;
            idx<=msb_index(n)-1;cycles<=0;busy<=1;state<=SQL;
          end
          SQL: begin qa0<=a0;qa1<=a1;qb0<=a0;qb1<=a1;q_start<=1;state<=SQW;end
          SQW: if(q_done) begin
            a0<=qy0;a1<=qy1;
            if(expreg[idx])state<=MUL;
            else if(idx==0)begin y0<=qy0;y1<=qy1;busy<=0;done<=1;state<=IDLE;end
            else begin idx<=idx-1;state<=SQL;end
          end
          MUL: begin qa0<=a0;qa1<=a1;qb0<=base0;qb1<=base1;q_start<=1;state<=MUW;end
          MUW: if(q_done) begin
            a0<=qy0;a1<=qy1;
            if(idx==0)begin y0<=qy0;y1<=qy1;busy<=0;done<=1;state<=IDLE;end
            else begin idx<=idx-1;state<=SQL;end
          end
        endcase
      end
    end
endmodule
