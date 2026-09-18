-- ============================================================================
-- HATTER-SOL-17 / H17-LAB-01
-- Board-independent byte UART.
--
-- 8N1, LSB first, integer DIVISOR.
-- RX uses a two-flop synchronizer; rx_valid pulses after a valid stop bit.
-- A bad stop bit waits for RX to return high.
-- TX accepts tx_start only while tx_busy='0'.
-- Packet framing and H17 semantics live in h17_uart_top.vhd.
-- ============================================================================
library ieee;use ieee.std_logic_1164.all;use ieee.numeric_std.all;
entity h17_uart is generic(DIVISOR:positive:=868);port(clk,rst,rx:in std_logic;tx:out std_logic;
 rx_data:out std_logic_vector(7 downto 0);rx_valid:out std_logic;
 tx_data:in std_logic_vector(7 downto 0);tx_start:in std_logic;tx_busy:out std_logic);end;
architecture rtl of h17_uart is
 -- Two-flop synchronizer for asynchronous RX.
 signal rx_meta,rx_sync:std_logic:='1';attribute ASYNC_REG:string;attribute ASYNC_REG of rx_meta,rx_sync:signal is "TRUE";
 signal rs:natural range 0 to 4:=0;signal rc,tc:natural range 0 to DIVISOR:=0;
 signal rb:natural range 0 to 7:=0;signal tb:natural range 0 to 9:=0;
 signal rx_shift:std_logic_vector(7 downto 0):=(others=>'0');signal tx_shift:std_logic_vector(9 downto 0):=(others=>'1');signal busy:std_logic:='0';
begin tx_busy<=busy;
 process(clk)begin if rising_edge(clk)then if rst='1' then rx_meta<='1';rx_sync<='1';else rx_meta<=rx;rx_sync<=rx_meta;end if;end if;end process;
 process(clk)begin if rising_edge(clk)then
 if rst='1' then rs<=0;rc<=0;rb<=0;rx_shift<=(others=>'0');rx_data<=(others=>'0');rx_valid<='0';
 else rx_valid<='0';case rs is
 when 0=>if rx_sync='0' then rc<=DIVISOR/2-1;rs<=1;end if;
 when 1=>if rc/=0 then rc<=rc-1;elsif rx_sync='0' then rc<=DIVISOR-1;rb<=0;rs<=2;else rs<=0;end if;
 when 2=>if rc/=0 then rc<=rc-1;else rx_shift(rb)<=rx_sync;rc<=DIVISOR-1;if rb=7 then rs<=3;else rb<=rb+1;end if;end if;
 when 3=>if rc/=0 then rc<=rc-1;else if rx_sync='1' then rx_data<=rx_shift;rx_valid<='1';rs<=0;else rs<=4;end if;end if;
 when 4=>if rx_sync='1' then rs<=0;end if;
 end case;end if;end if;end process;
 process(clk)begin if rising_edge(clk)then
 if rst='1' then tx<='1';busy<='0';tc<=0;tb<=0;tx_shift<=(others=>'1');
 elsif busy='0' then if tx_start='1' then tx_shift<='1'&tx_data&'0';tx<='0';tc<=DIVISOR-1;tb<=0;busy<='1';end if;
 elsif tc/=0 then tc<=tc-1;
 elsif tb=9 then tx<='1';busy<='0';
 else tx_shift<='1'&tx_shift(9 downto 1);tx<=tx_shift(1);tb<=tb+1;tc<=DIVISOR-1;end if;
 end if;end process;
end;
