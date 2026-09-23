#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv
from pathlib import Path

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def next_prime_strict(x: int) -> int:
    n = x + 1
    while not is_prime(n):
        n += 1
    return n

def primes_for_width(w: int):
    max_x = (1 << w) - 1
    last = next_prime_strict(max_x)
    return [n for n in range(2, last + 1) if is_prime(n)]

def emit_membership(w: int) -> str:
    vals = [n for n in range(1 << w) if is_prime(n)]
    cases = ", ".join(f"{w}'d{n}" for n in vals)
    return f"""module prime_member_top(
  input  logic [{w-1}:0] x,
  output logic is_prime_o
);
  always_comb begin
    unique case (x)
      {cases}: is_prime_o = 1'b1;
      default: is_prime_o = 1'b0;
    endcase
  end
endmodule
"""

def emit_direct(w: int) -> str:
    ow = w + 1
    lines = [f"      {w}'d{x}: p = {ow}'d{next_prime_strict(x)};" for x in range(1 << w)]
    return f"""module nextprime_top(
  input  logic [{w-1}:0] x,
  output logic [{ow-1}:0] p
);
  always_comb begin
    unique case (x)
{chr(10).join(lines)}
      default: p = '0;
    endcase
  end
endmodule
"""

def emit_linear(w: int) -> str:
    ow = w + 1
    ps = primes_for_width(w)
    lines = []
    for i, p in enumerate(ps):
        kw = "if" if i == 0 else "else if"
        lines.append(f"    {kw} (x < {ow}'d{p}) p = {ow}'d{p};")
    lines.append("    else p = '0;")
    return f"""module nextprime_top(
  input  logic [{w-1}:0] x,
  output logic [{ow-1}:0] p
);
  always_comb begin
{chr(10).join(lines)}
  end
endmodule
"""

def balanced_lines(ps, lo, hi, ow, indent="    "):
    if lo == hi:
        return [f"{indent}p = {ow}'d{ps[lo]};"]
    mid = (lo + hi) // 2
    threshold = ps[mid]
    out = [f"{indent}if (x < {ow}'d{threshold}) begin"]
    out += balanced_lines(ps, lo, mid, ow, indent + "  ")
    out += [f"{indent}end else begin"]
    out += balanced_lines(ps, mid + 1, hi, ow, indent + "  ")
    out += [f"{indent}end"]
    return out

def emit_balanced(w: int) -> str:
    ow = w + 1
    ps = primes_for_width(w)
    lines = balanced_lines(ps, 0, len(ps) - 1, ow)
    return f"""module nextprime_top(
  input  logic [{w-1}:0] x,
  output logic [{ow-1}:0] p
);
  always_comb begin
{chr(10).join(lines)}
  end
endmodule
"""

def emit_tb_nextprime(w: int) -> str:
    ow = w + 1
    return f"""module tb;
  logic [{w-1}:0] x;
  logic [{ow-1}:0] p;
  integer i;
  integer e;
  integer c;
  nextprime_top dut(.x(x), .p(p));

  function automatic integer prime(input integer n);
    integer d;
    begin
      if (n < 2) prime = 0;
      else begin
        prime = 1;
        for (d = 2; d*d <= n; d = d + 1)
          if ((n % d) == 0) prime = 0;
      end
    end
  endfunction

  function automatic integer nextp(input integer n);
    integer q;
    begin
      q = n + 1;
      while (!prime(q)) q = q + 1;
      nextp = q;
    end
  endfunction

  initial begin
    e = 0;
    for (i = 0; i < {1<<w}; i = i + 1) begin
      x = i[{w-1}:0];
      #1;
      c = nextp(i);
      if (p !== c) begin
        $display("FAIL x=%0d got=%0d expected=%0d", i, p, c);
        e = e + 1;
      end
    end
    if (e == 0) $display("PASS nextPrime W={w}: {1<<w} exhaustive inputs");
    else $display("FAIL nextPrime W={w}: errors=%0d", e);
    $finish;
  end
endmodule
"""

def emit_tb_member(w: int) -> str:
    return f"""module tb;
  logic [{w-1}:0] x;
  logic is_prime_o;
  integer i;
  integer d;
  integer expected;
  integer e;
  prime_member_top dut(.x(x), .is_prime_o(is_prime_o));

  initial begin
    e = 0;
    for (i = 0; i < {1<<w}; i = i + 1) begin
      x = i[{w-1}:0];
      #1;
      if (i < 2) expected = 0;
      else begin
        expected = 1;
        for (d = 2; d*d <= i; d = d + 1)
          if ((i % d) == 0) expected = 0;
      end
      if (is_prime_o !== expected[0]) begin
        $display("FAIL member x=%0d got=%0d expected=%0d", i, is_prime_o, expected);
        e = e + 1;
      end
    end
    if (e == 0) $display("PASS prime-member W={w}: {1<<w} exhaustive inputs");
    else $display("FAIL prime-member W={w}: errors=%0d", e);
    $finish;
  end
endmodule
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="generated")
    ap.add_argument("--widths", nargs="+", type=int, default=[4, 5, 6])
    a = ap.parse_args()
    root = Path(a.out_dir)
    root.mkdir(parents=True, exist_ok=True)

    for w in a.widths:
        d = root / f"w{w}"
        d.mkdir(exist_ok=True)
        (d / "prime_member_direct.sv").write_text(emit_membership(w))
        (d / "nextprime_direct.sv").write_text(emit_direct(w))
        (d / "nextprime_linear.sv").write_text(emit_linear(w))
        (d / "nextprime_balanced.sv").write_text(emit_balanced(w))
        (d / "tb_nextprime.sv").write_text(emit_tb_nextprime(w))
        (d / "tb_prime_member.sv").write_text(emit_tb_member(w))

        with (d / "truth_nextprime.csv").open("w", newline="") as f:
            cw = csv.writer(f)
            cw.writerow(["x", "next_prime"])
            for x in range(1 << w):
                cw.writerow([x, next_prime_strict(x)])

        print(f"W={w}: inputs={1<<w}, last={next_prime_strict((1<<w)-1)}, primes={len(primes_for_width(w))}")

if __name__ == "__main__":
    main()
