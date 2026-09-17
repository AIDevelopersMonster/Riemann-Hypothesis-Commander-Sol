library ieee;use ieee.std_logic_1164.all;use ieee.numeric_std.all;
entity h17_arty is port(clk100,btn0,uart_rx:in std_logic;uart_tx:out std_logic;led:out std_logic_vector(3 downto 0));end;
architecture rtl of h17_arty is
 signal por:unsigned(15 downto 0):=(others=>'0');signal hb:unsigned(26 downto 0):=(others=>'0');
 signal bmeta,bsync:std_logic:='0';signal rst,busy,passed:std_logic;
 attribute ASYNC_REG:string;attribute ASYNC_REG of bmeta,bsync:signal is "TRUE";
begin
 process(clk100)begin if rising_edge(clk100)then bmeta<=btn0;bsync<=bmeta;if por/=65535 then por<=por+1;end if;hb<=hb+1;end if;end process;
 rst<='1' when por/=65535 or bsync='1' else '0';
 top:entity work.h17_uart_top port map(clk100,rst,uart_rx,uart_tx,busy,passed);
 led<=hb(26)&(not rst)&passed&busy;
end;
