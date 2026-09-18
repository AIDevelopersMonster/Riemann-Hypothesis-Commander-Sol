/*
 * HATTER-SOL-17 / H17-LAB-01
 * Board-independent byte UART for the laboratory transport layer.
 *
 * 8N1, LSB first, integer divider DIV (DIV >= 8).
 * RX uses a two-flop synchronizer and samples near the bit centre.
 * rx_valid pulses for one clock after a valid stop bit.
 * A bad stop bit enters framing recovery until RX returns high.
 * TX accepts tx_start only while tx_busy=0.
 *
 * Packet framing, CRC and H17 semantics are handled in h17_uart_top.v.
 */
module h17_uart #(parameter DIV=868)(input clk,rst,input rx,output reg tx,
 output reg [7:0] rx_data,output reg rx_valid,
 input [7:0] tx_data,input tx_start,output reg tx_busy);
// CDC front end for asynchronous RX.
(* ASYNC_REG="TRUE" *) reg rx_meta,rx_sync;
reg [2:0] rs;integer rc,rb,tc,tb;reg [7:0] rx_shift;reg [9:0] tx_shift;
always @(posedge clk)begin
 if(rst)begin rx_meta<=1;rx_sync<=1;end else begin rx_meta<=rx;rx_sync<=rx_meta;end
end
// RX FSM: start detect -> data bits -> stop validation.
always @(posedge clk)begin
 if(rst)begin rs<=0;rc<=0;rb<=0;rx_shift<=0;rx_data<=0;rx_valid<=0;end
 else begin rx_valid<=0;
 case(rs)
 0:if(!rx_sync)begin rc<=DIV/2-1;rs<=1;end
 1:if(rc!=0)rc<=rc-1;else if(!rx_sync)begin rc<=DIV-1;rb<=0;rs<=2;end else rs<=0;
 2:if(rc!=0)rc<=rc-1;else begin rx_shift[rb]<=rx_sync;rc<=DIV-1;if(rb==7)rs<=3;else rb<=rb+1;end
 3:if(rc!=0)rc<=rc-1;else begin if(rx_sync)begin rx_data<=rx_shift;rx_valid<=1;rs<=0;end else rs<=4;end
 4:if(rx_sync)rs<=0;
 default:rs<=0;
 endcase end
end
// TX FSM: start + 8 data + stop, one bit every DIV clocks.
always @(posedge clk)begin
 if(rst)begin tx<=1;tx_busy<=0;tc<=0;tb<=0;tx_shift<=10'h3ff;end
 else if(!tx_busy)begin
 if(tx_start)begin tx_shift<={1'b1,tx_data,1'b0};tx<=0;tc<=DIV-1;tb<=0;tx_busy<=1;end
 end else if(tc!=0)tc<=tc-1;
 else if(tb==9)begin tx<=1;tx_busy<=0;end
 else begin tx_shift<={1'b1,tx_shift[9:1]};tx<=tx_shift[1];tb<=tb+1;tc<=DIV-1;end
end
endmodule
