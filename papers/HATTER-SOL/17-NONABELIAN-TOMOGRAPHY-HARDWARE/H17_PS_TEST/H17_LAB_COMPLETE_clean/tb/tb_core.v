`timescale 1ns/1ps
module tb_core;
reg clk=0;always #5 clk=~clk;
reg rst=1,start=0;reg [23:0] a=0,b=0;reg [3:0] mode=0;
wire busy,done;wire [2:0] status;wire [6:0] oid;wire [23:0] raw,obs,rep;
h17_core dut(clk,rst,start,a,b,mode,busy,done,status,oid,raw,obs,rep);
integer fd,rc,n=0,cycles;reg [23:0] ea,eb,eraw,eobs,erep;reg [3:0] em,es;reg [7:0] eo;
reg [1023:0] file_name;
initial begin
 if(!$value$plusargs("VECTORS=%s",file_name))file_name="vectors/quick.txt";
 repeat(3)@(negedge clk);rst=0;
 // Abort an in-progress operation with reset. No stale done allowed.
 a=24'hfac688;b=a;start=1;@(negedge clk);start=0;
 repeat(10)@(negedge clk);rst=1;@(negedge clk);rst=0;
 if(busy||done)$fatal(1,"reset failed");
 fd=$fopen(file_name,"r");if(!fd)$fatal(1,"vectors missing");
 while(!$feof(fd))begin
 rc=$fscanf(fd,"%h %h %h %h %h %h %h %h\n",ea,eb,em,es,eo,eraw,eobs,erep);
 if(rc!=8)$fatal(1,"malformed vector");
 @(negedge clk);a=ea;b=eb;mode=em;start=1;
 @(negedge clk);start=0;cycles=0;
 while(!done && cycles<1800)begin
 @(posedge clk);#1;cycles=cycles+1;
 // Inputs are latched; requests during busy must be ignored.
 if(cycles==5 && busy)begin a=0;b=0;mode=15;start=1;end
 if(cycles==6)start=0;
 end
 if(!done || busy || status!==es[2:0] || oid!==eo[6:0] || raw!==eraw || obs!==eobs || rep!==erep)
 $fatal(1,"vector %0d A=%h B=%h m=%h got s=%h id=%h raw=%h obs=%h rep=%h cycles=%0d",n,ea,eb,em,status,oid,raw,obs,rep,cycles);
 if(es==1 || es==2)if(cycles!=1663)$fatal(1,"latency %0d",cycles);
 @(negedge clk);start=0;@(posedge clk);#1;if(done)$fatal(1,"done not pulse");
 n=n+1;
 end
 $fclose(fd);$display("PASS Verilog core: %0d vectors; valid latency 1663 cycles; busy/reset checked",n);$finish;
end
initial begin #1000000000;$fatal(1,"watchdog");end
endmodule
