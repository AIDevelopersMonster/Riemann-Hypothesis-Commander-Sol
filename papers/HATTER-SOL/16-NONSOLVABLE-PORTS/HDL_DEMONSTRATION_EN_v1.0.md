# HATTER-SOL-16 · Verilog Control / Demonstration Exercise

## Hardware Realization of the Five-Probe PSL(2,7) Orbit Decoder

**Status:** control / demonstration exercise accompanying HATTER-SOL-16  
**Date:** 16 September 2026  
**Simulation platform:** EDA Playground  
**Public playground:** https://www.edaplayground.com/x/Z4Bx  
**Purpose:** hardware-facing validation that the mathematically proved H16 five-probe signature maps naturally to a compact synchronous digital data path.

---

## 1. Objective

HATTER-SOL-16 proves that all 114 simultaneous-conjugacy orbits of generating pairs in `PSL(2,7)` are separated by the five oriented trace probes

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad K=[A,B],
\]

with maximum word depth four. The purpose of this exercise is not to reimplement the full finite-group mathematics in HDL, but to validate the hardware form of the already proved interface:

\[
\boxed{
\text{5 class inputs}
\rightarrow
\text{15-bit signature}
\rightarrow
Q_4\text{ orientation}
\rightarrow
\text{LUT/ROM}
\rightarrow
\text{orbit ID}.
}
\]

This is deliberately an H16 control demonstration. The complete canonical 114-entry ROM, automatic generation of all golden vectors, fixed-point representation channel, synthesis, resource/timing measurements and physical FPGA implementation belong to HATTER-SOL-17.

---

## 2. Inputs and class encoding

Each of the five observed group elements is assumed to have already been classified into one of the six conjugacy classes of `PSL(2,7)`:

| class | 3-bit code |
|---|---|
| `1A` | `000` |
| `2A` | `001` |
| `3A` | `010` |
| `4A` | `011` |
| `7A` | `100` |
| `7B` | `101` |

The five 3-bit values are packed into the 15-bit vector

\[
\boxed{
\texttt{signature}=
\{\texttt{class\_A},\texttt{class\_B},\texttt{class\_AB},
\texttt{class\_AB\_inv},\texttt{class\_K}\}.
}
\]

At this proof-of-concept level, the HDL block begins at the class interface. It does not yet derive the classes from representation matrices; it validates the next architectural stages: signature packing, orientation extraction and orbit decoding.

---

## 3. Q4 orientation extraction

For

\[
K=[A,B],
\]

H16 proves the exact orientation observable

\[
Q_4(A,B)=
\frac{\operatorname{Tr}\rho_3(K)-\operatorname{Tr}\rho_3(K^{-1})}{i\sqrt7}.
\]

At the class level,

\[
Q_4=0\quad\text{on }3A,4A,
\]

\[
Q_4=+1\quad\text{on }7A,
\qquad
Q_4=-1\quad\text{on }7B.
\]

The RTL implementation therefore reduces to a trivial combinational decoder:

```verilog
assign q4_next = (class_K == 3'd4) ? 2'b01 : // 7A -> +1
                 (class_K == 3'd5) ? 2'b10 : // 7B -> -1
                                     2'b00;  // other classes -> 0
```

The state coding is

\[
0\mapsto00,
\qquad
+1\mapsto01,
\qquad
-1\mapsto10.
\]

Thus, once the commutator class has been identified, the mathematically nontrivial orientation information becomes a very small amount of digital logic.

---

## 4. Orbit decoding

Because H16 proves that the five-probe signature is injective on the 114 generating-pair orbits, the hardware decoder can be a finite LUT/ROM:

```verilog
always @(*) begin
    case (signature)
        15'b011_011_010_011_100: lut_orbit = 7'd42;
        15'b011_011_010_011_101: lut_orbit = 7'd43;
        default:                  lut_orbit = 7'h7F;
    endcase
end
```

Only two demonstration entries are included in the H16 control exercise. Orbit IDs `42` and `43` are test identifiers, not yet the frozen canonical numbering of the complete 114-orbit table.

The value

```text
7'h7F = 127
```

acts as `UNKNOWN` for signatures that are absent from the demonstration LUT.

---

## 5. Synchronous pipeline

Outputs are registered on the positive edge of `clk`:

```verilog
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        valid_out      <= 1'b0;
        q4_orientation <= 2'b00;
        orbit_id       <= 7'd0;
    end else begin
        valid_out      <= valid_in;
        q4_orientation <= q4_next;
        orbit_id       <= lut_orbit;
    end
end
```

This gives a simple one-stage architecture:

\[
\text{inputs}
\rightarrow
\text{combinational signature/Q4/LUT}
\rightarrow
\text{registered output}.
\]

At this level, the block already has the form of a normal FPGA datapath and needs no complicated control logic.

---

## 6. Testbench and golden vectors

The testbench checks two vectors that differ only in the commutator class.

### Golden Vector 1

```text
class_A      = 011 = 4A
class_B      = 011 = 4A
class_AB     = 010 = 3A
class_AB_inv = 011 = 4A
class_K      = 100 = 7A
```

Expected output:

```text
signature = 011_011_010_011_100
Q4        = +1 = 01
orbit_id  = 42
```

### Golden Vector 2

```text
class_A      = 011 = 4A
class_B      = 011 = 4A
class_AB     = 010 = 3A
class_AB_inv = 011 = 4A
class_K      = 101 = 7B
```

Expected output:

```text
signature = 011_011_010_011_101
Q4        = -1 = 10
orbit_id  = 43
```

The first four probes are identical. Changing only the commutator class from `7A` to `7B` changes both the orientation state and the LUT result. This directly visualizes why H16 needs an orientation-sensitive channel rather than a purely real orientation-even scalar observer.

---

## 7. Simulation result

The EDA Playground waveform shows the expected behavior:

1. reset drives the registered outputs to zero;
2. the first valid vector is captured and produces `Q4=01`, `orbit_id=42`;
3. the second vector produces `Q4=10`, `orbit_id=43`;
4. `valid_out` follows `valid_in` through the registered stage;
5. signatures not present in the small demonstration LUT map to `7'h7F`.

Public playground:

https://www.edaplayground.com/x/Z4Bx

In the waveform supplied with the experiment, the transitions `class_K=4 -> 5`, `q4_orientation=1 -> 2`, and `orbit_id=2a -> 2b` agree with the RTL description.

---

## 8. Reproduction

### EDA Playground

Open the shared playground, select an available Verilog/SystemVerilog simulator, run the testbench, and open `EPWave` for the generated `dump.vcd`.

Shared EDA Playground pages are useful as public code/demo links. EDA Playground itself states that running simulators requires sign-in; that is a service restriction rather than an HDL dependency.

### Local command-line reproduction with Icarus Verilog

The same test is independent of EDA Playground and can be run from a terminal:

```bash
iverilog -g2012 -o h16_sim \
  h16_orbit_decoder.v tb_h16_orbit_decoder.v
vvp h16_sim
```

The generated `dump.vcd` can then be opened in GTKWave:

```bash
gtkwave dump.vcd
```

So the HDL demonstration has a straightforward command-line reproduction path without any web service.

---

## 9. Practical significance

This control exercise translates the principal H16 mathematical result into a standard digital architecture. It shows that, after class recognition:

- the five mathematical probes require only `15` input bits;
- the `Q4` orientation channel is implemented by trivial combinational logic;
- one of 114 orbit IDs fits into `7` bits;
- orbit recovery maps naturally to a LUT/ROM;
- the complete block can be registered as a one-stage synchronous pipeline.

The practical point is not the two demonstration ROM entries. It is that there is **no architectural gap** between the proved finite tomography and a conventional FPGA structure.

H16 supplies the exact information interface; the RTL demonstrates that this interface is directly implementable.

---

## 10. Conclusions

The control exercise validates the hardware feasibility of the frozen H16 specification at RTL proof-of-concept level.

The resulting interface is

\[
\boxed{
5\times3\text{ bit class inputs}
\rightarrow15\text{ bit signature}
\rightarrow2\text{ bit }Q_4
\rightarrow7\text{ bit orbit ID}.
}
\]

The two golden vectors demonstrate the critical `7A/7B` case: identical first four probes plus opposite commutator orientation produce distinct hardware states.

This is sufficient for HATTER-SOL-16 as a demonstration of engineering realizability. HATTER-SOL-17 should generate the complete 114-entry ROM automatically from the exact mathematical certificate, verify all golden vectors, measure synthesis resource/timing costs, and deploy the processor on a physical FPGA.
