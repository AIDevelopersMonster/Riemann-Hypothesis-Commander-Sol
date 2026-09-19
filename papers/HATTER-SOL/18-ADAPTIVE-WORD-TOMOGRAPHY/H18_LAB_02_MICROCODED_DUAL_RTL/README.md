# H18-LAB-02 · Canonical microcoded dual RTL

This laboratory is the H18-08 hardware representation layer.

It keeps the exact H18-06 adaptive one-persistent-erasure strategy but replaces
the H18-LAB-01 hardwired 308-node decode network with a canonical microprogram.

## Contract

Input:

- packed 24-bit permutations \(A,B\);
- one transaction start;
- at most one known persistent query erasure.

Output:

- exact generating orbit ID \(0,\ldots,113\); or
- REJECT for all non-generating pair orbits.

Exact observation bound inherited from H18-06:

\[
4\text{ successful class answers}
+
1\text{ possible ERASED attempt}.
\]

The erased query is not retried.

## Canonical encoding

Query nodes:

- 0..68: erasure still available;
- 69..307: erasure already consumed.

Terminals:

- 308..421: orbit IDs 0..113;
- 422: REJECT;
- 423: FAULT.

The node address is therefore 9 bits.

Only the 308 query nodes require program storage.

## Generate

From this directory:

\`\`\`powershell
py -3 .\tools\generate_h18_microcoded_dual_rtl.py --out-dir generated_microcode
\`\`\`

Generated outputs include:

- exact microprogram JSON;
- four memory images;
- common 197-state vectors;
- SystemVerilog core and testbench;
- VHDL-2008 membership/classifier/core/testbench;
- generated VHDL microcode package;
- generated program-size summary.

## Expected explicit program payload

Before vendor-specific memory packing:

\[
\boxed{19057\text{ bits}}
\]

split as:

- 1,540 bits query-word IDs;
- 16,632 bits six-way class transitions;
- 621 bits legal erasure transitions;
- 264 bits word descriptors.

This is a representation count, not an FPGA BRAM claim.

## Important datapath change

H18-LAB-01 formed every query word by starting from the identity and composing
all letters.

H18-LAB-02 loads the first letter directly.

Therefore a word of length \(L\) uses only

\[
L-1
\]

permutation compositions.

On the frozen H18-07 worst five-attempt path this changes the naive arithmetic
count from at most

\[
19
\]

identity-based letter compositions to at most

\[
\boxed{14}
\]

actual compositions, without changing the decision strategy.

## CI

Workflow:

\`\`\`text
.github/workflows/h18-microcoded-dual-rtl.yml
\`\`\`

It performs:

1. deterministic generation from the exact H18-06 certificate;
2. full 985-run SystemVerilog regression with Icarus;
3. full 985-run VHDL-2008 regression with GHDL;
4. memory-preserving SystemVerilog Yosys synthesis;
5. ordinary generic SystemVerilog Yosys synthesis;
6. VHDL synthesis smoke with GHDL;
7. evidence artifact upload.

## Release boundary

H18-LAB-02 is not closed merely because sources exist.

Closure requires CI evidence that:

- both language implementations pass the same behavioral contract;
- both synthesis paths succeed;
- generated microprogram sizes agree with the architecture note.

Target FPGA LUT/FF/BRAM/Fmax/power comes later and must be reported separately.
