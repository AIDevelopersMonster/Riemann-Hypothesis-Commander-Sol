-- ============================================================================
-- HATTER-SOL-17 / H17-LAB-01
-- Sequential table-driven reference processor.
--
-- Input A,B: packed permutations, p(3*i+2 downto 3*i)=p(i), i=0..7.
-- Identity permutation: x"fac688".
--
-- Mathematical flow:
--   A,B membership in PSL(2,7)
--   -> 8 robust observer words
--   -> 8 conjugacy-class codes = 24-bit raw signature
--   -> optional known one-coordinate erasure
--   -> 114 generating-orbit signature scan
--   -> repaired fingerprint + legacy orbit_id.
--
-- mode: 0=no erasure, 1..8=erase coordinate 0..7, >8=invalid.
-- status: 0=idle/reset or non-PSL input, 1=no orbit match,
--         2=unique match, 3=multiple matches, 4=invalid mode.
-- orbit_id=127 is the invalid sentinel.
--
-- Valid status 1/2 transactions take 1663 clocks in the reference TB.
-- This is LAB-01 reference RTL, not H17-08 closure-aware / ROM-free RTL.
-- ============================================================================
library ieee; use ieee.std_logic_1164.all; use ieee.numeric_std.all;
use work.h17_tables.all;
entity h17_core is port(clk,rst,start:in std_logic;a_in,b_in:in word24;
 mode_in:in std_logic_vector(3 downto 0);busy,done:out std_logic;
 status:out std_logic_vector(2 downto 0);orbit_id:out std_logic_vector(6 downto 0);
 raw_signature,observed_signature,repaired_signature:out word24);end;
architecture rtl of h17_core is
 function compose(p,q:word24) return word24 is variable r:word24;variable ix:natural;
 begin for j in 0 to 7 loop ix:=to_integer(unsigned(q(j*3+2 downto j*3)));r(j*3+2 downto j*3):=p(ix*3+2 downto ix*3);end loop;return r;end;
 function inverse(p:word24) return word24 is variable r:word24:=(others=>'0');variable ix:natural;
 begin for j in 0 to 7 loop ix:=to_integer(unsigned(p(j*3+2 downto j*3)));r(ix*3+2 downto ix*3):=std_logic_vector(to_unsigned(j,3));end loop;return r;end;
 -- One sequential datapath is reused for membership, class and orbit scans.
 type states is(IDLE,MEMBER,CHECK,WORD_STEP,CLASSIFY,MASK_STEP,DECODE,FINISH);
 signal state:states:=IDLE;
 signal a,b,ia,ib,acc,mask,raw,observed:word24:=(others=>'0');
 signal mode:natural range 0 to 15:=0;
 signal idx:natural range 0 to 167:=0;signal w:natural range 0 to 7:=0;
 signal k:natural range 0 to 4:=0;signal hits:natural range 0 to 114:=0;
 signal va,vb:std_logic:='0';
begin
 raw_signature<=raw;observed_signature<=observed;
 process(clk) variable row:std_logic_vector(26 downto 0);variable letter,m:word24;
 begin if rising_edge(clk) then
 if rst='1' then state<=IDLE;busy<='0';done<='0';status<="000";orbit_id<=(others=>'1');
 raw<=(others=>'0');observed<=(others=>'0');repaired_signature<=(others=>'0');
 a<=(others=>'0');b<=(others=>'0');ia<=(others=>'0');ib<=(others=>'0');acc<=(others=>'0');mask<=(others=>'0');mode<=0;idx<=0;w<=0;k<=0;hits<=0;va<='0';vb<='0';
 else done<='0';row:=group_row(idx);
 case state is
 when IDLE=>if start='1' then
 a<=a_in;b<=b_in;mode<=to_integer(unsigned(mode_in));busy<='1';status<="000";orbit_id<=(others=>'1');
 raw<=(others=>'0');observed<=(others=>'0');repaired_signature<=(others=>'0');va<='0';vb<='0';idx<=0;hits<=0;
 if unsigned(mode_in)>8 then status<="100";state<=FINISH;else state<=MEMBER;end if;end if;
 -- Scan all 168 PSL(2,7) rows.
 when MEMBER=>
 if row(23 downto 0)=a then va<='1';end if;if row(23 downto 0)=b then vb<='1';end if;
 if idx=167 then state<=CHECK;else idx<=idx+1;end if;
 when CHECK=>if va='0' or vb='0' then state<=FINISH;else
 ia<=inverse(a);ib<=inverse(b);w<=0;k<=0;acc<=x"fac688";state<=WORD_STEP;end if;
 -- Evaluate one observer word one letter per clock.
 when WORD_STEP=>
 case probe_letter(w,k) is when 0=>letter:=a;when 1=>letter:=b;when 2=>letter:=ia;when others=>letter:=ib;end case;
 acc<=compose(acc,letter);
 if k=probe_len(w)-1 then idx<=0;state<=CLASSIFY;else k<=k+1;end if;
 -- Matching group row supplies the 3-bit class code.
 when CLASSIFY=>
 if row(23 downto 0)=acc then raw(23-3*w downto 21-3*w)<=row(26 downto 24);end if;
 if idx=167 then
 if w=7 then state<=MASK_STEP;else w<=w+1;k<=0;acc<=x"fac688";state<=WORD_STEP;end if;
 else idx<=idx+1;end if;
 -- Known erasure: mark one 3-bit field as 111 and mask it.
 when MASK_STEP=>
 if mode=0 then mask<=x"ffffff";observed<=raw;else
 m:=std_logic_vector(shift_left(to_unsigned(7,24),24-3*mode));mask<=not m;observed<=raw or m;end if;
 idx<=0;state<=DECODE;
 -- Compare surviving coordinates against 114 orbit signatures.
 when DECODE=>
 if (orbit_row(idx) and mask)=(observed and mask) then hits<=hits+1;orbit_id<=std_logic_vector(to_unsigned(idx,7));repaired_signature<=orbit_row(idx);end if;
 if idx=113 then state<=FINISH;else idx<=idx+1;end if;
 when FINISH=>
 if mode<=8 and va='1' and vb='1' then
 if hits=1 then status<="010";else
 if hits=0 then status<="001";else status<="011";end if;
 orbit_id<=(others=>'1');repaired_signature<=(others=>'0');end if;end if;
 busy<='0';done<='1';state<=IDLE;
 end case;
 end if;end if;end process;
end;
