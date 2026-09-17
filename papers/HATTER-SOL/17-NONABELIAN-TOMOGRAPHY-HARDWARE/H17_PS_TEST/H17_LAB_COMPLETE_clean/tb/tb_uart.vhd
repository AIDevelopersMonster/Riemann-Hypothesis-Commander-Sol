library ieee;use ieee.std_logic_1164.all;use ieee.numeric_std.all;use ieee.std_logic_textio.all;use std.textio.all;use std.env.all;
entity tb_uart is generic(DIVISOR:positive:=16);end;
architecture test of tb_uart is
 constant BIT_TIME:time:=DIVISOR*10 ns;
 signal clk:std_logic:='0';signal rst:std_logic:='1';signal rx:std_logic:='1';signal tx,busy,passed:std_logic;
 signal received:natural:=0;
begin clk<=not clk after 5 ns;
 dut:entity work.h17_uart_top generic map(DIVISOR*100000,100000)port map(clk,rst,rx,tx,busy,passed);
 process
 file f:text open read_mode is "vectors/uart.txt";variable l:line;variable req:std_logic_vector(95 downto 0);variable ex:std_logic_vector(127 downto 0);variable n:natural:=0;
 procedure send_byte(d:std_logic_vector(7 downto 0))is begin
 rx<='0';wait for BIT_TIME;for i in 0 to 7 loop rx<=d(i);wait for BIT_TIME;end loop;rx<='1';wait for BIT_TIME;end;
 begin
 for i in 1 to 5 loop wait until falling_edge(clk);end loop;rst<='0';wait for BIT_TIME;
 rx<='0';wait for BIT_TIME*11;rx<='1';wait for BIT_TIME*2;
 send_byte(x"a5");send_byte(x"5a");wait for DIVISOR*100000 ns+BIT_TIME*20;send_byte(x"55");
 while not endfile(f)loop readline(f,l);hread(l,req);hread(l,ex);
 for j in 0 to 11 loop send_byte(req(95-8*j downto 88-8*j));end loop;
 n:=n+1;if received<n then wait until received=n;end if;wait for BIT_TIME*3;
 end loop;
 report "PASS VHDL UART: "&integer'image(n)&" frames DIV="&integer'image(DIVISOR)&"; CRC/version/mode rejection, framing and timeout recovery";stop;wait;
 end process;
 process
 file f:text open read_mode is "vectors/uart.txt";variable l:line;variable req:std_logic_vector(95 downto 0);variable ex,got:std_logic_vector(127 downto 0);variable d:std_logic_vector(7 downto 0);variable n:natural:=0;
 begin while not endfile(f)loop readline(f,l);hread(l,req);hread(l,ex);
 for j in 0 to 15 loop
 wait until falling_edge(tx);wait for BIT_TIME+BIT_TIME/2;
 for i in 0 to 7 loop d(i):=tx;wait for BIT_TIME;end loop;
 assert tx='1' report "stop bit" severity failure;got(127-8*j downto 120-8*j):=d;
 end loop;
 assert got=ex report "UART case "&integer'image(n)&" expected "&to_hstring(ex)&" got "&to_hstring(got) severity failure;
 n:=n+1;received<=n;end loop;wait;end process;
 process begin wait for 1 sec;assert false report "UART watchdog" severity failure;end process;
end;
