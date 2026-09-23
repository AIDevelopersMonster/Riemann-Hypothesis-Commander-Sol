#!/usr/bin/env python3
from pathlib import Path
import argparse
import importlib.util

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gen", HERE / "generate_prime_spatial_lab.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

def rename(src: str, name: str) -> str:
    return src.replace("module nextprime_top(", f"module {name}(", 1)

def emit_miter(w: int) -> str:
    ow = w + 1
    d = rename(gen.emit_direct(w), "nextprime_direct")
    l = rename(gen.emit_linear(w), "nextprime_linear")
    b = rename(gen.emit_balanced(w), "nextprime_balanced")
    top = f"""
module equiv_top(
  input  logic [{w-1}:0] x,
  output logic bad
);
  logic [{ow-1}:0] pd, pl, pb;

  nextprime_direct   u_d(.x(x), .p(pd));
  nextprime_linear   u_l(.x(x), .p(pl));
  nextprime_balanced u_b(.x(x), .p(pb));

  always_comb begin
    bad = (pd != pl) || (pd != pb);
  end
endmodule
"""
    return d + "\n" + l + "\n" + b + "\n" + top

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="generated")
    ap.add_argument("--widths", nargs="+", type=int, default=[4,5,6])
    a = ap.parse_args()

    root = Path(a.out_dir)
    root.mkdir(parents=True, exist_ok=True)
    for w in a.widths:
        d = root / f"w{w}"
        d.mkdir(exist_ok=True)
        p = d / "nextprime_equiv_miter.sv"
        p.write_text(emit_miter(w))
        print(p)

if __name__ == "__main__":
    main()
