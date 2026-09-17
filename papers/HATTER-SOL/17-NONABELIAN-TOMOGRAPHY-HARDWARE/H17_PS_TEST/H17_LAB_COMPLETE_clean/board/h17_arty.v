// Arty A7-35 Rev D/E: 100MHz, USB UART, BTN0 reset. Power-on hold 65535 clocks.
module h17_arty(input clk100,btn0,uart_rx,output uart_tx,output [3:0] led);
reg [15:0] por=0;(* ASYNC_REG="TRUE" *)reg bmeta=0,bsync=0;
reg [26:0] heartbeat=0;wire rst=(por!=16'hffff)||bsync;
always @(posedge clk100)begin bmeta<=btn0;bsync<=bmeta;if(por!=16'hffff)por<=por+1'b1;heartbeat<=heartbeat+1'b1;end
wire busy,passed;
h17_uart_top top(clk100,rst,uart_rx,uart_tx,busy,passed);
assign led={heartbeat[26],!rst,passed,busy};
endmodule
