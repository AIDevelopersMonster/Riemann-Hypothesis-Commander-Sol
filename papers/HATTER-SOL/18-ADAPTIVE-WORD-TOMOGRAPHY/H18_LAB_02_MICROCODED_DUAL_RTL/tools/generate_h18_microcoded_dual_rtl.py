#!/usr/bin/env python3
"""Generate H18-08 canonical microcoded SystemVerilog and VHDL-2008 RTL.

The exact mathematical decision strategy is imported from H18-LAB-01, which
itself is materialized directly from the H18-06 certificate.  This generator
changes representation, not semantics:

* 69 pre-erasure query nodes are renumbered 0..68;
* 239 post-erasure query nodes are renumbered 69..307;
* orbit terminal k is encoded directly as node 308+k;
* REJECT is node 422 and FAULT is node 423;
* the controller program is split into word-id, class-next, erase-next and
  word-descriptor ROMs;
* the same generated program drives SystemVerilog and VHDL-2008 backends.

The first letter of every query word is loaded directly, so a length-L word
requires L-1 permutation compositions instead of L identity-based compositions.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve()
LAB = HERE.parents[1]
H18 = LAB.parent
LAB01_GEN = (
    H18
    / "H18_LAB_01_ADAPTIVE_RTL"
    / "tools"
    / "generate_h18_adaptive_rtl.py"
)

spec = importlib.util.spec_from_file_location("h18lab01", LAB01_GEN)
assert spec is not None and spec.loader is not None
h18lab01 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h18lab01)

QUERY_COUNT = 308
PRE_QUERY_COUNT = 69
POST_QUERY_COUNT = 239
ORBIT_COUNT = 114
ORBIT_BASE = QUERY_COUNT
REJECT_NODE = ORBIT_BASE + ORBIT_COUNT
FAULT_NODE = REJECT_NODE + 1
TOTAL_NODE_COUNT = FAULT_NODE + 1
NODE_W = 9


def build_program():
    builder = h18lab01.StrategyBuilder()
    old_root = builder.build("ONE", h18lab01.ALL_MASK, 4)

    query_nodes = [n for n in builder.nodes if n["kind"] == "QUERY"]
    pre_nodes = sorted(
        (n for n in query_nodes if n["phase"] == "ONE"),
        key=lambda n: n["id"],
    )
    post_nodes = sorted(
        (n for n in query_nodes if n["phase"] == "NO"),
        key=lambda n: n["id"],
    )
    assert len(pre_nodes) == PRE_QUERY_COUNT
    assert len(post_nodes) == POST_QUERY_COUNT
    ordered_queries = pre_nodes + post_nodes
    assert len(ordered_queries) == QUERY_COUNT

    remap = {}
    for new_id, node in enumerate(ordered_queries):
        remap[node["id"]] = new_id

    orbit_terminals = [n for n in builder.nodes if n["kind"] == "ORBIT"]
    reject_terminals = [n for n in builder.nodes if n["kind"] == "REJECT"]
    fault_terminals = [n for n in builder.nodes if n["kind"] == "FAULT"]
    assert len(orbit_terminals) == ORBIT_COUNT
    assert len(reject_terminals) == 1
    assert len(fault_terminals) == 1

    for node in orbit_terminals:
        remap[node["id"]] = ORBIT_BASE + node["orbit_id"]
    remap[reject_terminals[0]["id"]] = REJECT_NODE
    remap[fault_terminals[0]["id"]] = FAULT_NODE

    assert set(remap) == {n["id"] for n in builder.nodes}

    words = sorted(
        {n["word"] for n in ordered_queries},
        key=lambda w: (len(w), w),
    )
    assert len(words) == 24
    word_index = {word: i for i, word in enumerate(words)}

    word_ids = []
    class_next = []
    erase_next = []

    for new_id, node in enumerate(ordered_queries):
        assert remap[node["id"]] == new_id
        word_ids.append(word_index[node["word"]])
        class_next.extend(remap[target] for target in node["class_next"])
        if new_id < PRE_QUERY_COUNT:
            assert node["phase"] == "ONE"
            erase_next.append(remap[node["erase_next"]])
        else:
            assert node["phase"] == "NO"

    word_desc = []
    for word in words:
        wlen, wcode = h18lab01.encode_word(word)
        word_desc.append((wlen << 8) | wcode)

    root = remap[old_root]
    assert root < PRE_QUERY_COUNT
    assert max(word_ids) < 32
    assert max(class_next) < (1 << NODE_W)
    assert max(erase_next) < (1 << NODE_W)
    assert max(word_desc) < (1 << 11)

    summary = {
        "root_node": root,
        "query_nodes": QUERY_COUNT,
        "pre_erasure_query_nodes": PRE_QUERY_COUNT,
        "post_erasure_query_nodes": POST_QUERY_COUNT,
        "orbit_base": ORBIT_BASE,
        "orbit_terminals": ORBIT_COUNT,
        "reject_node": REJECT_NODE,
        "fault_node": FAULT_NODE,
        "total_node_codes": TOTAL_NODE_COUNT,
        "node_width_bits": NODE_W,
        "distinct_words": words,
        "distinct_word_count": len(words),
        "max_word_length": max(map(len, words)),
        "word_id_bits": QUERY_COUNT * 5,
        "class_next_bits": QUERY_COUNT * 6 * NODE_W,
        "erase_next_bits": PRE_QUERY_COUNT * NODE_W,
        "word_desc_bits": len(words) * 11,
    }
    summary["microprogram_bits"] = (
        summary["word_id_bits"]
        + summary["class_next_bits"]
        + summary["erase_next_bits"]
        + summary["word_desc_bits"]
    )
    assert summary["microprogram_bits"] == 19057

    return {
        "builder": builder,
        "root": root,
        "words": words,
        "word_ids": word_ids,
        "class_next": class_next,
        "erase_next": erase_next,
        "word_desc": word_desc,
        "summary": summary,
    }


def emit_mem(path: Path, values, hex_digits: int):
    path.write_text(
        "\n".join(f"{value:0{hex_digits}x}" for value in values) + "\n",
        encoding="utf-8",
    )


def emit_program_json(path: Path, program):
    payload = {
        "contract": {
            "source": "exact H18-06 one-persistent-erasure strategy",
            "successful_answers": 4,
            "maximum_attempts": 5,
            "word_length_bound": 4,
            "outputs": "114 orbit IDs or REJECT",
        },
        "summary": program["summary"],
        "word_ids": program["word_ids"],
        "class_next": program["class_next"],
        "erase_next": program["erase_next"],
        "word_desc": program["word_desc"],
    }
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def emit_sv_core(path: Path, program):
    s = program["summary"]
    text = f"""// Auto-generated H18-08 canonical microcoded controller.
// Exact H18-06 semantics; representation only is changed.
module h18_microcoded_erasure_core(
    input  logic        clk,
    input  logic        rst,
    input  logic        start,
    input  logic [23:0] A_in,
    input  logic [23:0] B_in,
    input  logic        erase_now,
    output logic        busy,
    output logic        done,
    output logic        query_pending,
    output logic        input_valid,
    output logic        identified,
    output logic        rejected,
    output logic [2:0]  status,
    output logic [6:0]  orbit_id
);

localparam integer QUERY_COUNT = {QUERY_COUNT};
localparam integer PRE_QUERY_COUNT = {PRE_QUERY_COUNT};
localparam integer ORBIT_BASE = {ORBIT_BASE};
localparam integer REJECT_NODE = {REJECT_NODE};
localparam integer FAULT_NODE = {FAULT_NODE};
localparam integer ROOT_NODE = {s["root_node"]};

localparam [3:0]
    ST_IDLE=4'd0, ST_CHECK=4'd1, ST_DISPATCH=4'd2,
    ST_WORDDESC=4'd3, ST_WORDINIT=4'd4, ST_WORD=4'd5,
    ST_CLASSIFY=4'd6, ST_APPLY=4'd7, ST_DONE=4'd8;

logic [3:0] state;
logic [23:0] A_reg, B_reg, invA_reg, invB_reg;
logic valid_A, valid_B;
logic [8:0] node_id, next_node_q;
logic [4:0] word_id_q;
logic [10:0] word_desc_q;
logic [2:0] word_len, word_pos;
logic [7:0] word_code;
logic [23:0] word_acc, class_perm;
logic [23:0] selected_perm, first_perm, compose_result;
logic [1:0] selected_letter;
logic [2:0] class_code;

(* rom_style = "distributed" *) logic [4:0] word_id_rom [0:QUERY_COUNT-1];
(* rom_style = "block" *) logic [8:0] class_next_rom [0:QUERY_COUNT*6-1];
(* rom_style = "distributed" *) logic [8:0] erase_next_rom [0:PRE_QUERY_COUNT-1];
(* rom_style = "distributed" *) logic [10:0] word_desc_rom [0:23];

initial begin
    $readmemh("generated_microcode/h18_word_id.mem", word_id_rom);
    $readmemh("generated_microcode/h18_class_next.mem", class_next_rom);
    $readmemh("generated_microcode/h18_erase_next.mem", erase_next_rom);
    $readmemh("generated_microcode/h18_word_desc.mem", word_desc_rom);
end

function automatic [2:0] getp(
    input logic [23:0] p, input integer idx
);
    getp = p[idx*3 +: 3];
endfunction

function automatic [23:0] compose_perm(
    input logic [23:0] p, input logic [23:0] q
);
    integer i;
    logic [23:0] r;
    logic [2:0] qi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin
        qi=getp(q,i);
        r[i*3 +:3]=getp(p,qi);
      end
      compose_perm=r;
    end
endfunction

function automatic [23:0] inverse_perm(input logic [23:0] p);
    integer i;
    logic [23:0] r;
    logic [2:0] pi;
    begin
      r='0;
      for(i=0;i<8;i=i+1) begin
        pi=getp(p,i);
        r[pi*3 +:3]=i[2:0];
      end
      inverse_perm=r;
    end
endfunction

psl27_membership_only u_mem_A(.perm(A_reg),.valid(valid_A));
psl27_membership_only u_mem_B(.perm(B_reg),.valid(valid_B));
psl27_member_class_only u_class(
    .perm(class_perm),.class_code(class_code)
);

always @* begin
    case (word_pos)
      3'd1: selected_letter = word_code[3:2];
      3'd2: selected_letter = word_code[5:4];
      default: selected_letter = word_code[7:6];
    endcase
    case (selected_letter)
      2'd0: selected_perm = A_reg;
      2'd1: selected_perm = B_reg;
      2'd2: selected_perm = invA_reg;
      default: selected_perm = invB_reg;
    endcase

    case (word_desc_q[1:0])
      2'd0: first_perm = A_reg;
      2'd1: first_perm = B_reg;
      2'd2: first_perm = invA_reg;
      default: first_perm = invB_reg;
    endcase

    compose_result = compose_perm(word_acc, selected_perm);
end

assign query_pending = (state == ST_CLASSIFY);

always_ff @(posedge clk) begin
  if (rst) begin
    state<=ST_IDLE;
    busy<=1'b0;
    done<=1'b0;
    input_valid<=1'b0;
    identified<=1'b0;
    rejected<=1'b0;
    status<=3'd0;
    orbit_id<=7'h7f;
    A_reg<=0;
    B_reg<=0;
    invA_reg<=0;
    invB_reg<=0;
    node_id<=ROOT_NODE[8:0];
    next_node_q<=FAULT_NODE[8:0];
    word_id_q<=0;
    word_desc_q<=0;
    word_len<=0;
    word_pos<=0;
    word_code<=0;
    word_acc<=24'hfac688;
    class_perm<=24'hfac688;
  end else begin
    done <= 1'b0;
    case (state)
      ST_IDLE: begin
        busy<=1'b0;
        if(start) begin
          A_reg<=A_in;
          B_reg<=B_in;
          invA_reg<=inverse_perm(A_in);
          invB_reg<=inverse_perm(B_in);
          input_valid<=1'b0;
          identified<=1'b0;
          rejected<=1'b0;
          status<=3'd0;
          orbit_id<=7'h7f;
          node_id<=ROOT_NODE[8:0];
          busy<=1'b1;
          state<=ST_CHECK;
        end
      end

      ST_CHECK: begin
        input_valid <= valid_A & valid_B;
        if(!(valid_A & valid_B)) begin
          status<=3'd0;
          state<=ST_DONE;
        end else begin
          node_id<=ROOT_NODE[8:0];
          state<=ST_DISPATCH;
        end
      end

      ST_DISPATCH: begin
        if(node_id < QUERY_COUNT) begin
          word_id_q <= word_id_rom[node_id];
          state <= ST_WORDDESC;
        end else if(node_id < REJECT_NODE) begin
          identified<=1'b1;
          rejected<=1'b0;
          status<=3'd2;
          orbit_id<=node_id-ORBIT_BASE;
          state<=ST_DONE;
        end else if(node_id == REJECT_NODE) begin
          identified<=1'b0;
          rejected<=1'b1;
          status<=3'd1;
          orbit_id<=7'h7f;
          state<=ST_DONE;
        end else begin
          identified<=1'b0;
          rejected<=1'b0;
          status<=3'd4;
          orbit_id<=7'h7f;
          state<=ST_DONE;
        end
      end

      ST_WORDDESC: begin
        word_desc_q <= word_desc_rom[word_id_q];
        state <= ST_WORDINIT;
      end

      ST_WORDINIT: begin
        word_len <= word_desc_q[10:8];
        word_code <= word_desc_q[7:0];
        word_pos <= 3'd1;
        word_acc <= first_perm;
        if(word_desc_q[10:8] <= 3'd1) begin
          class_perm <= first_perm;
          state <= ST_CLASSIFY;
        end else begin
          state <= ST_WORD;
        end
      end

      ST_WORD: begin
        word_acc <= compose_result;
        if(word_pos + 3'd1 >= word_len) begin
          class_perm <= compose_result;
          state <= ST_CLASSIFY;
        end else begin
          word_pos <= word_pos + 3'd1;
        end
      end

      ST_CLASSIFY: begin
        if(erase_now) begin
          if(node_id < PRE_QUERY_COUNT) begin
            next_node_q <= erase_next_rom[node_id];
            state <= ST_APPLY;
          end else begin
            status<=3'd4;
            orbit_id<=7'h7f;
            state<=ST_DONE;
          end
        end else begin
          next_node_q <= class_next_rom[node_id*6 + class_code];
          state <= ST_APPLY;
        end
      end

      ST_APPLY: begin
        node_id <= next_node_q;
        state <= ST_DISPATCH;
      end

      ST_DONE: begin
        busy<=1'b0;
        done<=1'b1;
        state<=ST_IDLE;
      end

      default: begin
        status<=3'd4;
        orbit_id<=7'h7f;
        busy<=1'b0;
        state<=ST_IDLE;
      end
    endcase
  end
end
endmodule
"""
    path.write_text(text, encoding="utf-8")


def emit_sv_tb(path: Path):
    path.write_text(r'''module tb_h18_microcoded_erasure;
logic clk,rst,start,erase_now;
logic [23:0] A_in,B_in;
logic busy,done,query_pending,input_valid,identified,rejected;
logic [2:0] status;
logic [6:0] orbit_id;

h18_microcoded_erasure_core dut(
 .clk(clk),.rst(rst),.start(start),.A_in(A_in),.B_in(B_in),
 .erase_now(erase_now),.busy(busy),.done(done),
 .query_pending(query_pending),.input_valid(input_valid),
 .identified(identified),.rejected(rejected),
 .status(status),.orbit_id(orbit_id)
);

always #5 clk=~clk;

integer fd,rc,n,attempts,cycles,max_cycles,max_attempts,total_runs;
reg [1023:0] file_name;
reg [23:0] ea,eb;
reg [3:0] es;
reg [7:0] eoid;

task automatic run_case(input integer target);
integer fired;
begin
  @(negedge clk);
  A_in=ea; B_in=eb; start=1'b1; erase_now=1'b0;
  @(negedge clk);
  start=1'b0;
  attempts=0; cycles=0; fired=0;

  while(!done && cycles<180) begin
    @(negedge clk);
    erase_now=1'b0;
    if(query_pending) begin
      attempts=attempts+1;
      if(target>0 && attempts==target && !fired) begin
        erase_now=1'b1;
        fired=1;
      end
    end
    cycles=cycles+1;
  end
  erase_now=1'b0;

  if(!done)
    $fatal(1,"timeout vector=%0d erase_target=%0d",n,target);

  if(cycles>max_cycles) max_cycles=cycles;
  if(attempts>max_attempts) max_attempts=attempts;

  if(status!==es[2:0] || orbit_id!==eoid[6:0])
    $fatal(1,
      "mismatch vector=%0d erase_target=%0d A=%h B=%h expected status=%h orbit=%h got status=%h orbit=%h attempts=%0d cycles=%0d",
      n,target,ea,eb,es,eoid,status,orbit_id,attempts,cycles);

  if(es==4'h2 && (!identified || rejected))
    $fatal(1,"success flags mismatch vector=%0d",n);

  if(es==4'h1 && (!rejected || identified))
    $fatal(1,"reject flags mismatch vector=%0d",n);

  if(attempts>5)
    $fatal(1,"attempt bound exceeded vector=%0d target=%0d attempts=%0d",
      n,target,attempts);

  total_runs=total_runs+1;
end
endtask

initial begin
  clk=0; rst=1; start=0; erase_now=0; A_in=0; B_in=0;
  n=0; max_cycles=0; max_attempts=0; total_runs=0;

  repeat(3) @(negedge clk);
  rst=0;

  if(!$value$plusargs("VECTORS=%s",file_name))
    file_name="generated_microcode/h18_adaptive_vectors.txt";

  fd=$fopen(file_name,"r");
  if(!fd) $fatal(1,"vectors missing: %0s",file_name);

  rc=$fgets(file_name,fd);

  while(!$feof(fd)) begin
    rc=$fscanf(fd,"%h %h %h %h\n",ea,eb,es,eoid);
    if(rc==4) begin
      run_case(0);
      run_case(1);
      run_case(2);
      run_case(3);
      run_case(4);
      n=n+1;
      if((n%25)==0)
        $display(
          "PROGRESS H18-LAB-02-SV: states=%0d runs=%0d max_attempts=%0d max_cycles=%0d",
          n,total_runs,max_attempts,max_cycles);
    end
  end

  $fclose(fd);
  $display(
    "PASS H18-LAB-02 SystemVerilog: %0d states x 5 schedules = %0d runs; max_attempts=%0d max_cycles=%0d",
    n,total_runs,max_attempts,max_cycles);
  $finish;
end
endmodule
''', encoding="utf-8")


def emit_vhdl_membership(path: Path):
    path.write_text(r'''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity psl27_membership_only is
  port(
    perm  : in  std_logic_vector(23 downto 0);
    valid : out std_logic
  );
end entity;

architecture rtl of psl27_membership_only is
  function getp(p : std_logic_vector(23 downto 0); idx : integer)
    return integer is
  begin
    return to_integer(unsigned(p(idx*3+2 downto idx*3)));
  end function;

  function perm_is_bijection(p : std_logic_vector(23 downto 0))
    return boolean is
  begin
    for i in 0 to 7 loop
      for j in i+1 to 7 loop
        if getp(p,i)=getp(p,j) then
          return false;
        end if;
      end loop;
    end loop;
    return true;
  end function;

  function det_point(x,y : integer) return integer is
    variable t : integer;
  begin
    if x=7 and y=7 then return 0;
    elsif x=7 then return 1;
    elsif y=7 then return 6;
    else
      t := x-y;
      if t<0 then t:=t+7; end if;
      return t;
    end if;
  end function;

  function mul7(a,b : integer) return integer is
  begin
    return (a*b) mod 7;
  end function;

  function orient_pos(a,b,c : integer) return boolean is
    variable v : integer;
  begin
    v := mul7(mul7(det_point(a,b),det_point(b,c)),det_point(c,a));
    return v=1 or v=2 or v=4;
  end function;

  function pgl_ok(p : std_logic_vector(23 downto 0)) return boolean is
    variable y0,y1,yi,px,k,lhs,rhs : integer;
  begin
    if not perm_is_bijection(p) then return false; end if;
    y0:=getp(p,0); y1:=getp(p,1); yi:=getp(p,7);
    for x in 2 to 6 loop
      px:=getp(p,x);
      case x is
        when 2 => k:=6;
        when 3 => k:=5;
        when 4 => k:=4;
        when 5 => k:=3;
        when others => k:=2;
      end case;
      lhs:=mul7(det_point(px,y1),det_point(y0,yi));
      rhs:=mul7(k,mul7(det_point(px,yi),det_point(y0,y1)));
      if lhs/=rhs then return false; end if;
    end loop;
    return true;
  end function;
begin
  process(all)
  begin
    if pgl_ok(perm) and orient_pos(getp(perm,0),getp(perm,1),getp(perm,7)) then
      valid <= '1';
    else
      valid <= '0';
    end if;
  end process;
end architecture;
''', encoding="utf-8")


def emit_vhdl_classifier(path: Path):
    path.write_text(r'''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity psl27_member_class_only is
  port(
    perm       : in  std_logic_vector(23 downto 0);
    class_code : out std_logic_vector(2 downto 0)
  );
end entity;

architecture rtl of psl27_member_class_only is
  function getp(p : std_logic_vector(23 downto 0); idx : integer)
    return integer is
  begin
    return to_integer(unsigned(p(idx*3+2 downto idx*3)));
  end function;

  function compose_perm(
    p,q : std_logic_vector(23 downto 0)
  ) return std_logic_vector is
    variable r : std_logic_vector(23 downto 0) := (others=>'0');
    variable qi : integer;
  begin
    for i in 0 to 7 loop
      qi:=getp(q,i);
      r(i*3+2 downto i*3):=
        std_logic_vector(to_unsigned(getp(p,qi),3));
    end loop;
    return r;
  end function;

  function det_point(x,y : integer) return integer is
    variable t : integer;
  begin
    if x=7 and y=7 then return 0;
    elsif x=7 then return 1;
    elsif y=7 then return 6;
    else
      t:=x-y;
      if t<0 then t:=t+7; end if;
      return t;
    end if;
  end function;

  function mul7(a,b : integer) return integer is
  begin
    return (a*b) mod 7;
  end function;

  function orient_pos(a,b,c : integer) return boolean is
    variable v : integer;
  begin
    v:=mul7(mul7(det_point(a,b),det_point(b,c)),det_point(c,a));
    return v=1 or v=2 or v=4;
  end function;
begin
  process(all)
    variable p2,p3,p4,p7 : std_logic_vector(23 downto 0);
    variable is_id,is_o2,is_o3,is_o4,is_o7 : boolean;
    variable startv,y,z : integer;
  begin
    p2:=compose_perm(perm,perm);
    p3:=compose_perm(p2,perm);
    p4:=compose_perm(p2,p2);
    p7:=compose_perm(compose_perm(p4,p2),perm);
    is_id := perm=x"FAC688";
    is_o2 := (not is_id) and p2=x"FAC688";
    is_o3 := (not is_id) and p3=x"FAC688";
    is_o4 := (not is_id) and (not is_o2) and p4=x"FAC688";
    is_o7 := (not is_id) and p7=x"FAC688";

    startv:=0;
    for i in 0 to 7 loop
      if getp(perm,i)/=i then startv:=i; end if;
    end loop;
    y:=getp(perm,startv);
    z:=getp(perm,y);

    class_code <= "111";
    if is_id then
      class_code <= "000";
    elsif is_o2 then
      class_code <= "001";
    elsif is_o3 then
      class_code <= "010";
    elsif is_o4 then
      class_code <= "011";
    elsif is_o7 then
      if orient_pos(startv,y,z) then
        class_code <= "100";
      else
        class_code <= "101";
      end if;
    end if;
  end process;
end architecture;
''', encoding="utf-8")


def emit_vhdl_package(path: Path, program):
    s = program["summary"]
    lines = [
        "library ieee;",
        "use ieee.std_logic_1164.all;",
        "use ieee.numeric_std.all;",
        "",
        "package h18_microcode_pkg is",
        f"  constant QUERY_COUNT : natural := {QUERY_COUNT};",
        f"  constant PRE_QUERY_COUNT : natural := {PRE_QUERY_COUNT};",
        f"  constant ORBIT_BASE : natural := {ORBIT_BASE};",
        f"  constant REJECT_NODE : natural := {REJECT_NODE};",
        f"  constant FAULT_NODE : natural := {FAULT_NODE};",
        f"  constant ROOT_NODE : natural := {s['root_node']};",
        "  subtype node_t is unsigned(8 downto 0);",
        "  subtype word_id_t is unsigned(4 downto 0);",
        "  subtype word_desc_t is unsigned(10 downto 0);",
        "  type word_id_rom_t is array(0 to QUERY_COUNT-1) of word_id_t;",
        "  type class_next_rom_t is array(0 to QUERY_COUNT*6-1) of node_t;",
        "  type erase_next_rom_t is array(0 to PRE_QUERY_COUNT-1) of node_t;",
        "  type word_desc_rom_t is array(0 to 23) of word_desc_t;",
        "",
        "  constant WORD_ID_ROM : word_id_rom_t := (",
    ]
    for i, value in enumerate(program["word_ids"]):
        comma = "," if i + 1 < len(program["word_ids"]) else ""
        lines.append(f"    {i} => to_unsigned({value},5){comma}")
    lines += [
        "  );",
        "",
        "  constant CLASS_NEXT_ROM : class_next_rom_t := (",
    ]
    for i, value in enumerate(program["class_next"]):
        comma = "," if i + 1 < len(program["class_next"]) else ""
        lines.append(f"    {i} => to_unsigned({value},9){comma}")
    lines += [
        "  );",
        "",
        "  constant ERASE_NEXT_ROM : erase_next_rom_t := (",
    ]
    for i, value in enumerate(program["erase_next"]):
        comma = "," if i + 1 < len(program["erase_next"]) else ""
        lines.append(f"    {i} => to_unsigned({value},9){comma}")
    lines += [
        "  );",
        "",
        "  constant WORD_DESC_ROM : word_desc_rom_t := (",
    ]
    for i, value in enumerate(program["word_desc"]):
        comma = "," if i + 1 < len(program["word_desc"]) else ""
        lines.append(f"    {i} => to_unsigned({value},11){comma}")
    lines += [
        "  );",
        "end package;",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def emit_vhdl_core(path: Path):
    path.write_text(r'''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.h18_microcode_pkg.all;

entity h18_microcoded_erasure_core is
  port(
    clk           : in  std_logic;
    rst           : in  std_logic;
    start         : in  std_logic;
    A_in          : in  std_logic_vector(23 downto 0);
    B_in          : in  std_logic_vector(23 downto 0);
    erase_now     : in  std_logic;
    busy          : out std_logic;
    done          : out std_logic;
    query_pending : out std_logic;
    input_valid   : out std_logic;
    identified    : out std_logic;
    rejected      : out std_logic;
    status        : out std_logic_vector(2 downto 0);
    orbit_id      : out std_logic_vector(6 downto 0)
  );
end entity;

architecture rtl of h18_microcoded_erasure_core is
  type state_t is (
    ST_IDLE, ST_CHECK, ST_DISPATCH, ST_WORDDESC, ST_WORDINIT,
    ST_WORD, ST_CLASSIFY, ST_APPLY, ST_DONE
  );
  signal state : state_t := ST_IDLE;

  signal A_reg,B_reg,invA_reg,invB_reg : std_logic_vector(23 downto 0);
  signal valid_A,valid_B : std_logic;
  signal node_id,next_node_q : node_t;
  signal word_id_q : word_id_t;
  signal word_desc_q : word_desc_t;
  signal word_len,word_pos : unsigned(2 downto 0);
  signal word_code : std_logic_vector(7 downto 0);
  signal word_acc,class_perm : std_logic_vector(23 downto 0);
  signal selected_perm,first_perm,compose_result : std_logic_vector(23 downto 0);
  signal selected_letter : std_logic_vector(1 downto 0);
  signal class_code : std_logic_vector(2 downto 0);

  function getp(p : std_logic_vector(23 downto 0); idx : integer)
    return integer is
  begin
    return to_integer(unsigned(p(idx*3+2 downto idx*3)));
  end function;

  function compose_perm(
    p,q : std_logic_vector(23 downto 0)
  ) return std_logic_vector is
    variable r : std_logic_vector(23 downto 0) := (others=>'0');
    variable qi : integer;
  begin
    for i in 0 to 7 loop
      qi:=getp(q,i);
      r(i*3+2 downto i*3):=
        std_logic_vector(to_unsigned(getp(p,qi),3));
    end loop;
    return r;
  end function;

  function inverse_perm(
    p : std_logic_vector(23 downto 0)
  ) return std_logic_vector is
    variable r : std_logic_vector(23 downto 0) := (others=>'0');
    variable pi : integer;
  begin
    for i in 0 to 7 loop
      pi:=getp(p,i);
      r(pi*3+2 downto pi*3):=std_logic_vector(to_unsigned(i,3));
    end loop;
    return r;
  end function;
begin
  u_mem_A: entity work.psl27_membership_only
    port map(perm=>A_reg, valid=>valid_A);
  u_mem_B: entity work.psl27_membership_only
    port map(perm=>B_reg, valid=>valid_B);
  u_class: entity work.psl27_member_class_only
    port map(perm=>class_perm, class_code=>class_code);

  query_pending <= '1' when state=ST_CLASSIFY else '0';

  process(all)
  begin
    case to_integer(word_pos) is
      when 1 => selected_letter <= word_code(3 downto 2);
      when 2 => selected_letter <= word_code(5 downto 4);
      when others => selected_letter <= word_code(7 downto 6);
    end case;

    case selected_letter is
      when "00" => selected_perm <= A_reg;
      when "01" => selected_perm <= B_reg;
      when "10" => selected_perm <= invA_reg;
      when others => selected_perm <= invB_reg;
    end case;

    case std_logic_vector(word_desc_q(1 downto 0)) is
      when "00" => first_perm <= A_reg;
      when "01" => first_perm <= B_reg;
      when "10" => first_perm <= invA_reg;
      when others => first_perm <= invB_reg;
    end case;

    compose_result <= compose_perm(word_acc,selected_perm);
  end process;

  process(clk)
    variable nid : integer;
    variable class_addr : integer;
    variable wlen_i : integer;
  begin
    if rising_edge(clk) then
      if rst='1' then
        state<=ST_IDLE;
        busy<='0';
        done<='0';
        input_valid<='0';
        identified<='0';
        rejected<='0';
        status<="000";
        orbit_id<=(others=>'1');
        A_reg<=(others=>'0');
        B_reg<=(others=>'0');
        invA_reg<=(others=>'0');
        invB_reg<=(others=>'0');
        node_id<=to_unsigned(ROOT_NODE,9);
        next_node_q<=to_unsigned(FAULT_NODE,9);
        word_id_q<=(others=>'0');
        word_desc_q<=(others=>'0');
        word_len<=(others=>'0');
        word_pos<=(others=>'0');
        word_code<=(others=>'0');
        word_acc<=x"FAC688";
        class_perm<=x"FAC688";
      else
        done<='0';
        case state is
          when ST_IDLE =>
            busy<='0';
            if start='1' then
              A_reg<=A_in;
              B_reg<=B_in;
              invA_reg<=inverse_perm(A_in);
              invB_reg<=inverse_perm(B_in);
              input_valid<='0';
              identified<='0';
              rejected<='0';
              status<="000";
              orbit_id<=(others=>'1');
              node_id<=to_unsigned(ROOT_NODE,9);
              busy<='1';
              state<=ST_CHECK;
            end if;

          when ST_CHECK =>
            input_valid<=valid_A and valid_B;
            if not (valid_A='1' and valid_B='1') then
              status<="000";
              state<=ST_DONE;
            else
              node_id<=to_unsigned(ROOT_NODE,9);
              state<=ST_DISPATCH;
            end if;

          when ST_DISPATCH =>
            nid:=to_integer(node_id);
            if nid<QUERY_COUNT then
              word_id_q<=WORD_ID_ROM(nid);
              state<=ST_WORDDESC;
            elsif nid<REJECT_NODE then
              identified<='1';
              rejected<='0';
              status<="010";
              orbit_id<=std_logic_vector(to_unsigned(nid-ORBIT_BASE,7));
              state<=ST_DONE;
            elsif nid=REJECT_NODE then
              identified<='0';
              rejected<='1';
              status<="001";
              orbit_id<=(others=>'1');
              state<=ST_DONE;
            else
              identified<='0';
              rejected<='0';
              status<="100";
              orbit_id<=(others=>'1');
              state<=ST_DONE;
            end if;

          when ST_WORDDESC =>
            word_desc_q<=WORD_DESC_ROM(to_integer(word_id_q));
            state<=ST_WORDINIT;

          when ST_WORDINIT =>
            wlen_i:=to_integer(word_desc_q(10 downto 8));
            word_len<=word_desc_q(10 downto 8);
            word_code<=std_logic_vector(word_desc_q(7 downto 0));
            word_pos<=to_unsigned(1,3);
            word_acc<=first_perm;
            if wlen_i<=1 then
              class_perm<=first_perm;
              state<=ST_CLASSIFY;
            else
              state<=ST_WORD;
            end if;

          when ST_WORD =>
            word_acc<=compose_result;
            if to_integer(word_pos)+1>=to_integer(word_len) then
              class_perm<=compose_result;
              state<=ST_CLASSIFY;
            else
              word_pos<=word_pos+1;
            end if;

          when ST_CLASSIFY =>
            nid:=to_integer(node_id);
            if erase_now='1' then
              if nid<PRE_QUERY_COUNT then
                next_node_q<=ERASE_NEXT_ROM(nid);
                state<=ST_APPLY;
              else
                status<="100";
                orbit_id<=(others=>'1');
                state<=ST_DONE;
              end if;
            else
              class_addr:=nid*6+to_integer(unsigned(class_code));
              next_node_q<=CLASS_NEXT_ROM(class_addr);
              state<=ST_APPLY;
            end if;

          when ST_APPLY =>
            node_id<=next_node_q;
            state<=ST_DISPATCH;

          when ST_DONE =>
            busy<='0';
            done<='1';
            state<=ST_IDLE;
        end case;
      end if;
    end if;
  end process;
end architecture;
''', encoding="utf-8")


def emit_vhdl_tb(path: Path):
    path.write_text(r'''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_textio.all;
use std.textio.all;
use std.env.all;

entity tb_h18_microcoded_erasure is
end entity;

architecture sim of tb_h18_microcoded_erasure is
  signal clk,rst,start,erase_now : std_logic := '0';
  signal A_in,B_in : std_logic_vector(23 downto 0) := (others=>'0');
  signal busy,done,query_pending,input_valid,identified,rejected : std_logic;
  signal status : std_logic_vector(2 downto 0);
  signal orbit_id : std_logic_vector(6 downto 0);
begin
  dut: entity work.h18_microcoded_erasure_core
    port map(
      clk=>clk,rst=>rst,start=>start,A_in=>A_in,B_in=>B_in,
      erase_now=>erase_now,busy=>busy,done=>done,
      query_pending=>query_pending,input_valid=>input_valid,
      identified=>identified,rejected=>rejected,
      status=>status,orbit_id=>orbit_id
    );

  clk <= not clk after 5 ns;

  stim: process
    file vf : text open read_mode is
      "generated_microcode/h18_adaptive_vectors.txt";
    variable l : line;
    variable ea,eb : std_logic_vector(23 downto 0);
    variable es : std_logic_vector(3 downto 0);
    variable eoid : std_logic_vector(7 downto 0);
    variable n,total_runs,max_cycles,max_attempts : integer := 0;

    procedure run_case(constant target : in integer) is
      variable fired : boolean := false;
      variable attempts,cycles : integer := 0;
    begin
      wait until falling_edge(clk);
      A_in<=ea; B_in<=eb; start<='1'; erase_now<='0';
      wait until falling_edge(clk);
      start<='0';

      while done/='1' and cycles<180 loop
        wait until falling_edge(clk);
        erase_now<='0';
        if query_pending='1' then
          attempts:=attempts+1;
          if target>0 and attempts=target and not fired then
            erase_now<='1';
            fired:=true;
          end if;
        end if;
        cycles:=cycles+1;
      end loop;
      erase_now<='0';

      assert done='1'
        report "timeout vector=" & integer'image(n) &
               " erase_target=" & integer'image(target)
        severity failure;

      if cycles>max_cycles then max_cycles:=cycles; end if;
      if attempts>max_attempts then max_attempts:=attempts; end if;

      assert status=es(2 downto 0) and orbit_id=eoid(6 downto 0)
        report "mismatch vector=" & integer'image(n) &
               " erase_target=" & integer'image(target)
        severity failure;

      if es=x"2" then
        assert identified='1' and rejected='0'
          report "success flags mismatch vector=" & integer'image(n)
          severity failure;
      elsif es=x"1" then
        assert rejected='1' and identified='0'
          report "reject flags mismatch vector=" & integer'image(n)
          severity failure;
      end if;

      assert attempts<=5
        report "attempt bound exceeded vector=" & integer'image(n)
        severity failure;

      total_runs:=total_runs+1;
    end procedure;
  begin
    rst<='1';
    wait until falling_edge(clk);
    wait until falling_edge(clk);
    wait until falling_edge(clk);
    rst<='0';

    readline(vf,l);
    while not endfile(vf) loop
      readline(vf,l);
      hread(l,ea);
      hread(l,eb);
      hread(l,es);
      hread(l,eoid);
      for target in 0 to 4 loop
        run_case(target);
      end loop;
      n:=n+1;
      if (n mod 25)=0 then
        report "PROGRESS H18-LAB-02-VHDL states=" & integer'image(n) &
               " runs=" & integer'image(total_runs)
          severity note;
      end if;
    end loop;

    report "PASS H18-LAB-02 VHDL: states=" & integer'image(n) &
           " runs=" & integer'image(total_runs) &
           " max_attempts=" & integer'image(max_attempts) &
           " max_cycles=" & integer'image(max_cycles)
      severity note;
    finish;
    wait;
  end process;
end architecture;
''', encoding="utf-8")


def emit_summary(path: Path, program):
    s = program["summary"]
    path.write_text(
        "# H18-LAB-02 generated microcode summary\n\n"
        f"- root node: {s['root_node']}\n"
        f"- query nodes: {s['query_nodes']}\n"
        f"- pre-erasure nodes: {s['pre_erasure_query_nodes']}\n"
        f"- post-erasure nodes: {s['post_erasure_query_nodes']}\n"
        f"- orbit terminal encoding: {s['orbit_base']}..{s['orbit_base'] + 113}\n"
        f"- REJECT node: {s['reject_node']}\n"
        f"- FAULT node: {s['fault_node']}\n"
        f"- node width: {s['node_width_bits']} bits\n"
        f"- distinct words: {s['distinct_word_count']}\n"
        f"- maximum word length: {s['max_word_length']}\n\n"
        "## Explicit program payload\n\n"
        f"- query word IDs: {s['word_id_bits']} bits\n"
        f"- class transitions: {s['class_next_bits']} bits\n"
        f"- erasure transitions: {s['erase_next_bits']} bits\n"
        f"- word descriptors: {s['word_desc_bits']} bits\n"
        f"- total: **{s['microprogram_bits']} bits**\n\n"
        "The count is a representation count, not a vendor BRAM claim.\n",
        encoding="utf-8",
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default=str(LAB / "generated_microcode"))
    args = ap.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    assert h18lab01.h18e.one_erasure(h18lab01.ALL_MASK, 3) is False
    assert h18lab01.h18e.one_erasure(h18lab01.ALL_MASK, 4) is True

    program = build_program()

    emit_program_json(out / "h18_microcode.json", program)
    emit_mem(out / "h18_word_id.mem", program["word_ids"], 2)
    emit_mem(out / "h18_class_next.mem", program["class_next"], 3)
    emit_mem(out / "h18_erase_next.mem", program["erase_next"], 3)
    emit_mem(out / "h18_word_desc.mem", program["word_desc"], 3)
    h18lab01.emit_vectors(out / "h18_adaptive_vectors.txt")

    emit_sv_core(out / "h18_microcoded_erasure_core.sv", program)
    emit_sv_tb(out / "tb_h18_microcoded_erasure.sv")

    emit_vhdl_membership(out / "psl27_membership_only.vhd")
    emit_vhdl_classifier(out / "psl27_member_class_only.vhd")
    emit_vhdl_package(out / "h18_microcode_pkg.vhd", program)
    emit_vhdl_core(out / "h18_microcoded_erasure_core.vhd")
    emit_vhdl_tb(out / "tb_h18_microcoded_erasure.vhd")

    emit_summary(out / "H18_MICROCODE_SUMMARY.md", program["summary"])

    print("HATTER-SOL-18 H18-LAB-02 microcoded dual-RTL generator")
    for key, value in program["summary"].items():
        if key != "distinct_words":
            print(key, "=", value)
    print("words =", ", ".join(program["words"]))
    print("PASS: canonical microprogram emitted for SystemVerilog and VHDL-2008")


if __name__ == "__main__":
    main()
