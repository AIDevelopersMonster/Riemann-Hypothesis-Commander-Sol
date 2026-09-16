# Appendix A · HDL proof-of-concept for the H16 orbit decoder

This appendix records the first hardware-facing validation of the frozen HATTER-SOL-16 engineering interface. It is intentionally a **control / demonstration exercise**, not yet the full HATTER-SOL-17 implementation.

**Public EDA Playground demonstration:** https://www.edaplayground.com/x/Z4Bx  
**RTL source:** `hdl/h16_orbit_decoder.v`  
**Testbench:** `hdl/tb_h16_orbit_decoder.v`  
**Detailed reports:** `HDL_DEMONSTRATION_RU_v1.0.md`, `HDL_DEMONSTRATION_EN_v1.0.md`

The tested block realizes the final H16 data path

\[
\boxed{
\text{five class probes}
\to
\text{15-bit signature}
\to
Q_4\text{ orientation state}
\to
\text{orbit LUT/ROM}.
}
\]

The five class inputs correspond to

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad K=[A,B].
\]

A 3-bit class encoding is used:

| class | code |
|---|---|
| `1A` | `000` |
| `2A` | `001` |
| `3A` | `010` |
| `4A` | `011` |
| `7A` | `100` |
| `7B` | `101` |

The orientation output uses

\[
Q_4=0\mapsto 00,
\qquad
Q_4=+1\mapsto 01,
\qquad
Q_4=-1\mapsto 10.
\]

The first two golden vectors differ only in the commutator class and verify the exact `7A/7B` orientation split:

```text
011_011_010_011_100 -> orbit 42, Q4=+1
011_011_010_011_101 -> orbit 43, Q4=-1
```

The assigned orbit IDs in this proof-of-concept are demonstration LUT entries; the complete 114-entry canonical ROM is deliberately left to HATTER-SOL-17.

## Verilog module

The publication source is stored separately in `hdl/h16_orbit_decoder.v`. Its principal logic is:

```verilog
assign q4_next = (class_K == 3'd4) ? 2'b01 : // 7A -> +1
                 (class_K == 3'd5) ? 2'b10 : // 7B -> -1
                                     2'b00;

wire [14:0] signature = {class_A, class_B, class_AB, class_AB_inv, class_K};

always @(*) begin
    case (signature)
        15'b011_011_010_011_100: lut_orbit = 7'd42;
        15'b011_011_010_011_101: lut_orbit = 7'd43;
        default:                  lut_orbit = 7'h7F;
    endcase
end
```

The result is registered synchronously on the next positive clock edge.

## Testbench

The full testbench is stored as `hdl/tb_h16_orbit_decoder.v`. It performs reset, applies the `7A` golden vector, changes only the commutator class to `7B`, and writes `dump.vcd` for waveform inspection.

## Observed result

The supplied EDA Playground waveform shows the expected state transition:

```text
class_K        : 4 -> 5
q4_orientation : 1 -> 2     // binary 01 -> 10
orbit_id       : 2a -> 2b   // hexadecimal 42 -> 43
```

Thus the experiment demonstrates the implementation-level distinction between the split order-seven classes using the exact orientation channel established mathematically in H16.

## Reproduction

The shared EDA Playground page provides the browser demonstration. EDA Playground documentation states that simulator execution requires sign-in, although a shared page can be used as a public code/demo reference.

The HDL is not tied to the web service. With Icarus Verilog it can be run from a normal terminal:

```bash
iverilog -g2012 -o h16_sim \
  hdl/h16_orbit_decoder.v hdl/tb_h16_orbit_decoder.v
vvp h16_sim
```

and the generated waveform can be opened with

```bash
gtkwave dump.vcd
```

## Interpretation and practical significance

This experiment validates three implementation facts already proved mathematically in H16:

1. the five-probe class signature fits into a compact 15-bit fixed-width interface;
2. the orientation bit is extracted by a trivial combinational map from the commutator class;
3. orbit recovery can be implemented as a finite lookup stage followed by a synchronous registered output.

Consequently the frozen H16 information interface already has the form of an ordinary FPGA datapath:

\[
\boxed{
5\times3\text{ input bits}
\to 15\text{-bit signature}
\to 2\text{-bit orientation}
\to 7\text{-bit orbit ID}.
}
\]

This is the practical conclusion required by H16: there is no architectural gap between the exact five-probe tomography theorem and a conventional LUT/ROM-based synchronous digital implementation.

The present appendix deliberately does **not** claim a complete 114-orbit hardware decoder, synthesis result, fixed-point robustness, timing closure, or physical-board demonstration. Those belong to HATTER-SOL-17.

For the publication package, the corresponding interactive HTML visualization is distributed as `HATTER_SOL_16_PSL27_HTML_DEMO_v1.0.html`.
