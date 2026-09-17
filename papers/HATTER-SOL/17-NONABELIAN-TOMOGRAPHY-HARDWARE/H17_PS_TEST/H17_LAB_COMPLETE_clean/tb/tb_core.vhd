library ieee;use ieee.std_logic_1164.all;use ieee.numeric_std.all;use ieee.std_logic_textio.all;
use std.textio.all;use std.env.all;
entity tb_core is generic(VECTORS:string:="vectors/quick.txt");end;
architecture test of tb_core is
 signal clk:std_logic:='0';signal rst:std_logic:='1';signal start:std_logic:='0';
 signal a,b:std_logic_vector(23 downto 0):=(others=>'0');signal mode:std_logic_vector(3 downto 0):=(others=>'0');
 signal busy,done:std_logic;signal status:std_logic_vector(2 downto 0);signal oid:std_logic_vector(6 downto 0);
 signal raw,obs,rep:std_logic_vector(23 downto 0);
begin clk<=not clk after 5 ns;
 dut:entity work.h17_core port map(clk,rst,start,a,b,mode,busy,done,status,oid,raw,obs,rep);
 process
 file f:text open read_mode is VECTORS;variable l:line;variable n,cycles:natural:=0;
 variable ea,eb,eraw,eobs,erep:std_logic_vector(23 downto 0);variable em,es:std_logic_vector(3 downto 0);variable eo:std_logic_vector(7 downto 0);
 begin
 for i in 1 to 3 loop wait until falling_edge(clk);end loop;rst<='0';a<=x"fac688";b<=x"fac688";start<='1';
 wait until falling_edge(clk);start<='0';for i in 1 to 10 loop wait until falling_edge(clk);end loop;
 rst<='1';wait until falling_edge(clk);rst<='0';assert busy='0' and done='0' report "reset failed" severity failure;
 while not endfile(f) loop
 readline(f,l);hread(l,ea);hread(l,eb);hread(l,em);hread(l,es);hread(l,eo);hread(l,eraw);hread(l,eobs);hread(l,erep);
 wait until falling_edge(clk);a<=ea;b<=eb;mode<=em;start<='1';wait until falling_edge(clk);start<='0';cycles:=0;
 while done/='1' and cycles<1800 loop
 wait until rising_edge(clk);wait for 1 ns;cycles:=cycles+1;
 if cycles=5 and busy='1' then a<=(others=>'0');b<=(others=>'0');mode<=x"f";start<='1';end if;
 if cycles=6 then start<='0';end if;
 end loop;
 assert done='1' and busy='0' and status=es(2 downto 0) and oid=eo(6 downto 0) and raw=eraw and obs=eobs and rep=erep
 report "vector "&integer'image(n)&" got status "&to_hstring(status)&" raw "&to_hstring(raw)&" cycles "&integer'image(cycles) severity failure;
 if es=x"1" or es=x"2" then assert cycles=1663 report "latency" severity failure;end if;
 wait until falling_edge(clk);start<='0';wait until rising_edge(clk);wait for 1 ns;assert done='0' report "done pulse" severity failure;
 n:=n+1;end loop;
 report "PASS VHDL core: "&integer'image(n)&" vectors; valid latency 1663 cycles; busy/reset checked";stop;wait;
 end process;
 process begin wait for 1 sec;assert false report "watchdog" severity failure;end process;
end;
