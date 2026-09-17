// Board-independent synchronous top; rst is active high and synchronous.
module h17_uart_top #(parameter CLK_HZ=100000000,BAUD=115200)(input clk,rst,uart_rx,output uart_tx,
 output busy_led,output reg pass_led);
localparam DIV=(CLK_HZ+BAUD/2)/BAUD;
wire [7:0] rxd;wire rv,tbusy;reg [7:0] txd;reg ts;
h17_uart #(.DIV(DIV)) uart(clk,rst,uart_rx,uart_tx,rxd,rv,txd,ts,tbusy);
reg cs;reg [23:0] a,b;reg [3:0] mode;wire cb,cd;wire [2:0] status;wire [6:0] oid;wire [23:0] raw,obs,rep;
h17_core core(clk,rst,cs,a,b,mode,cb,cd,status,oid,raw,obs,rep);
reg [7:0] req[0:11];reg [127:0] response;integer pos,timer,txpos,state,j;reg [7:0] crc;reg [127:0] frame;
assign busy_led=(state!=0);
function [7:0] crc8;input [7:0] c,d;reg [7:0] x;integer i;begin x=c^d;for(i=0;i<8;i=i+1)x=x[7]?(x<<1)^8'h07:x<<1;crc8=x;end endfunction
function [127:0] reply;input [7:0] seq,st,id;input [23:0] r,o,p;reg [127:0] f;reg [7:0] c;integer i;
begin f={8'h00,p,o,r,id,st,seq,8'h01,8'ha5,8'h5a};c=0;for(i=0;i<15;i=i+1)c=crc8(c,f[8*i+:8]);f[127:120]=c;reply=f;end endfunction
always @(posedge clk)begin
 if(rst)begin pos<=0;timer<=0;txpos<=0;state<=0;ts<=0;txd<=0;cs<=0;a<=0;b<=0;mode<=0;response<=0;pass_led<=0;for(j=0;j<12;j=j+1)req[j]<=0;end
 else begin ts<=0;cs<=0;
 case(state)
 0:begin
 if(pos!=0)begin if(timer>=CLK_HZ/10)begin pos<=0;timer<=0;end else timer<=timer+1;end
 if(rv)begin timer<=0;
 if(pos==0)begin if(rxd==8'ha5)begin req[0]<=rxd;pos<=1;end end
 else if(pos==1)begin if(rxd==8'h5a)begin req[1]<=rxd;pos<=2;end else if(rxd!=8'ha5)pos<=0;end
 else if(pos==11)begin
 crc=0;for(j=0;j<11;j=j+1)crc=crc8(crc,req[j]);pos<=0;
 if(crc!=rxd || req[2]!=1 || req[4]>15)begin response<=reply(req[3],5,127,0,0,0);txpos<=0;state<=2;pass_led<=0;end
 else begin a<={req[7],req[6],req[5]};b<={req[10],req[9],req[8]};mode<=req[4][3:0];cs<=1;state<=1;end
 end else begin req[pos]<=rxd;pos<=pos+1;end
 end end
 1:if(cd)begin response<=reply(req[3],{5'b0,status},{1'b0,oid},raw,obs,rep);pass_led<=(status==2);txpos<=0;state<=2;end
 2:if(!tbusy)begin txd<=response[8*txpos+:8];ts<=1;state<=3;end
 3:if(tbusy)state<=4;
 4:if(!tbusy)begin if(txpos==15)state<=0;else begin txpos<=txpos+1;state<=2;end end
 default:state<=0;
 endcase end
end
endmodule
