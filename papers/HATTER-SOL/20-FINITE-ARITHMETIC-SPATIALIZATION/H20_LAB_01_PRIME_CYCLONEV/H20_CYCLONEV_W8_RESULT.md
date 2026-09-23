# H20 Cyclone V physical result · W=8

Status: **W=8 TRIPLE CLOSED**

Target: Cyclone V 5CEFA7F23C6  
Toolchain: Quartus II 13.1  
Clock contract: 100 MHz  
Function: strict next prime on 8-bit input.

All three presentations are formally equivalent at the arithmetic level.

## Measured physical profiles

| Presentation | Physical class | ALMs | Registers | Fmax | Worst data delay | Logic levels |
|---|---|---:|---:|---:|---:|---:|
| DIRECT | ROM / M10K | 3 | 8 | 496.03 MHz | 1.870 ns | 0 |
| BALANCED | logic fabric | 78 | 17 | 210.17 MHz | 4.581 ns | 4 |
| LINEAR | logic fabric | 48 | 17 | 254.13 MHz | 3.765 ns | 4 |

Thus the declared physical observer separates all three:

\[
\mathcal P_{W=8}^{CV}=\{\{D\},\{B\},\{L\}\}.
\]

## Important reversal

At ABC-fast for W=8 the cell counts were

\[
D=156,\qquad B=315,\qquad L=562,
\]

so the measured Boolean cell-count ordering was

\[
D < B < L.
\]

On Cyclone V, among the two logic-fabric realizations:

\[
L < B
\]

in ALM count,

\[
48 < 78,
\]

and LINEAR is also faster:

\[
254.13\text{ MHz} > 210.17\text{ MHz}.
\]

Therefore the Boolean-stage ordering between BALANCED and LINEAR is **not preserved** by the Quartus/Cyclone-V physical realization.

This is an observer-dependent ranking reversal:

\[
B <_{\rm ABC} L,
\qquad
L <_{\rm CycloneV} B.
\]

No scalar, presentation-independent ranking is justified.

## DIRECT caveat

DIRECT is not fairly summarized as merely "3 ALMs". Quartus recognizes the table as a ROM and maps it to an M10K hard-memory resource. Its physical resource class is therefore different from BALANCED and LINEAR.

DIRECT is faster and uses very little ALM logic in this run, but it consumes hard memory; comparison must remain multidimensional.

## Claim boundary

This W=8 result establishes only a measured Cyclone-V/Quartus outcome for the frozen source family and flow. It does not prove that the reversal persists at larger widths, under other synthesis settings, or on other FPGA families.
