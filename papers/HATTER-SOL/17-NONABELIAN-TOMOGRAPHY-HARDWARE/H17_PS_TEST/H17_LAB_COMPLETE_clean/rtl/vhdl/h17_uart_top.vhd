library ieee;use ieee.std_logic_1164.all;use ieee.numeric_std.all;
entity h17_uart_top is generic(CLK_HZ:positive:=100000000;BAUD:positive:=115200);
 port(clk,rst,uart_rx:in std_logic;uart_tx,busy_led,pass_led:out std_logic);end;
architecture rtl of h17_uart_top is
 subtype byte is std_logic_vector(7 downto 0);subtype word24 is std_logic_vector(23 downto 0);
 subtype frame128 is std_logic_vector(127 downto 0);type bytes is array(0 to 11)of byte;
 signal req:bytes:=(others=>(others=>'0'));signal response:frame128:=(others=>'0');
 signal rxd,txd:byte:=(others=>'0');signal rv,tbusy,ts,cs,cb,cd:std_logic:='0';
 signal a,b,raw,obs,rep:word24:=(others=>'0');signal mode:std_logic_vector(3 downto 0):=(others=>'0');
 signal status:std_logic_vector(2 downto 0);signal oid:std_logic_vector(6 downto 0);
 signal pos:natural range 0 to 11:=0;signal timer:natural range 0 to CLK_HZ/10:=0;
 signal txpos:natural range 0 to 15:=0;signal state:natural range 0 to 4:=0;
 function crc8(c,d:byte)return byte is variable x:unsigned(7 downto 0);begin x:=unsigned(c xor d);
 for i in 0 to 7 loop if x(7)='1' then x:=shift_left(x,1) xor x"07";else x:=shift_left(x,1);end if;end loop;return std_logic_vector(x);end;
 function reply(seq,st,id:byte;r,o,p:word24)return frame128 is variable f:frame128;variable c:byte:=x"00";
 begin f:=x"00"&p&o&r&id&st&seq&x"01"&x"a5"&x"5a";
 for i in 0 to 14 loop c:=crc8(c,f(i*8+7 downto i*8));end loop;f(127 downto 120):=c;return f;end;
begin
 busy_led<='0' when state=0 else '1';
 uart:entity work.h17_uart generic map((CLK_HZ+BAUD/2)/BAUD)port map(clk,rst,uart_rx,uart_tx,rxd,rv,txd,ts,tbusy);
 core:entity work.h17_core port map(clk,rst,cs,a,b,mode,cb,cd,status,oid,raw,obs,rep);
 process(clk)variable crc:byte;
 begin if rising_edge(clk)then
 if rst='1' then pos<=0;timer<=0;txpos<=0;state<=0;ts<='0';txd<=x"00";cs<='0';a<=(others=>'0');b<=(others=>'0');mode<=(others=>'0');response<=(others=>'0');pass_led<='0';req<=(others=>(others=>'0'));
 else ts<='0';cs<='0';case state is
 when 0=>
 if pos/=0 then if timer=CLK_HZ/10 then pos<=0;timer<=0;else timer<=timer+1;end if;end if;
 if rv='1' then timer<=0;
 if pos=0 then if rxd=x"a5" then req(0)<=rxd;pos<=1;end if;
 elsif pos=1 then if rxd=x"5a" then req(1)<=rxd;pos<=2;elsif rxd/=x"a5" then pos<=0;end if;
 elsif pos=11 then
 crc:=x"00";for j in 0 to 10 loop crc:=crc8(crc,req(j));end loop;pos<=0;
 if crc/=rxd or req(2)/=x"01" or unsigned(req(4))>15 then response<=reply(req(3),x"05",x"7f",x"000000",x"000000",x"000000");txpos<=0;state<=2;pass_led<='0';
 else a<=req(7)&req(6)&req(5);b<=req(10)&req(9)&req(8);mode<=req(4)(3 downto 0);cs<='1';state<=1;end if;
 else req(pos)<=rxd;pos<=pos+1;end if;end if;
 when 1=>if cd='1' then response<=reply(req(3),"00000"&status,'0'&oid,raw,obs,rep);
 if status="010" then pass_led<='1';else pass_led<='0';end if;txpos<=0;state<=2;end if;
 when 2=>if tbusy='0' then txd<=response(8*txpos+7 downto 8*txpos);ts<='1';state<=3;end if;
 when 3=>if tbusy='1' then state<=4;end if;
 when 4=>if tbusy='0' then if txpos=15 then state<=0;else txpos<=txpos+1;state<=2;end if;end if;
 end case;end if;end if;end process;
end;
