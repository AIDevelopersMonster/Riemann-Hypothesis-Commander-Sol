`timescale 1ns/1ps
module tb_uart;
parameter DIVISOR=16;
localparam BIT_NS=DIVISOR*10;
reg clk=0;always #5 clk=~clk;reg rst=1,rx=1;wire tx,busy,passed;
h17_uart_top #(.CLK_HZ(DIVISOR*100000),.BAUD(100000))dut(clk,rst,rx,tx,busy,passed);
integer fd,rc,n=0,j,k;reg [95:0] req;reg [127:0] expct,got;reg [7:0] byte_got;
task send_byte;input [7:0] d;integer i;begin
 rx=0;#(BIT_NS);for(i=0;i<8;i=i+1)begin rx=d[i];#(BIT_NS);end rx=1;#(BIT_NS);end endtask
task read_byte;output [7:0] d;integer i;begin
 @(negedge tx);#(BIT_NS+BIT_NS/2);for(i=0;i<8;i=i+1)begin d[i]=tx;#(BIT_NS);end
 if(tx!==1)$fatal(1,"bad stop bit");end endtask
initial begin
 repeat(5)@(negedge clk);rst=0;#(BIT_NS);
 // Framing error (low stop), then truncated frame timeout, then noise.
 rx=0;#(BIT_NS*11);rx=1;#(BIT_NS*2);
 send_byte(8'ha5);send_byte(8'h5a);#(DIVISOR*100000+BIT_NS*20);
 send_byte(8'h55);
 fd=$fopen("vectors/uart.txt","r");if(!fd)$fatal(1,"missing uart vectors");
 while(!$feof(fd))begin
 rc=$fscanf(fd,"%h %h\n",req,expct);if(rc!=2)$fatal(1,"format");got=0;
 fork
 begin for(j=0;j<12;j=j+1)send_byte(req[95-8*j-:8]);end
 begin for(k=0;k<16;k=k+1)begin read_byte(byte_got);got[127-8*k-:8]=byte_got;end end
 join
 if(got!==expct)$fatal(1,"UART case %0d expected %h got %h",n,expct,got);
 #(BIT_NS*3);n=n+1;
 end
 $display("PASS Verilog UART: %0d frames DIV=%0d; CRC/version/mode rejection, framing and timeout recovery",n,DIVISOR);$finish;
end
initial begin #1000000000;$fatal(1,"UART watchdog");end
endmodule
