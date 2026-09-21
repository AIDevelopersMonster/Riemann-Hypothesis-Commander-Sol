# H20 · W=8 cross-vendor replication

Status: **TWO-VENDOR W=8 RESULT CLOSED**

Arithmetic function: strict next-prime map on 8-bit input.

Presentations:

- \(D_8\): DIRECT truth-table;
- \(B_8\): BALANCED threshold tree;
- \(L_8\): LINEAR threshold chain.

All three are formally equivalent.

## Cyclone V

Target: 5CEFA7F23C6, Quartus II 13.1.

| Presentation | Physical class | Logic resource | Fmax | Critical depth |
|---|---|---:|---:|---:|
| DIRECT | M10K ROM | 3 ALM | 496.03 MHz | 0 |
| BALANCED | logic fabric | 78 ALM | 210.17 MHz | 4 |
| LINEAR | logic fabric | 48 ALM | 254.13 MHz | 4 |

Thus among logic-fabric realizations:

\[
L_8 <_{\rm area} B_8,
\qquad
L_8 >_{\rm Fmax} B_8.
\]

## Gowin GW5A-25

Target: GW5A-LV25MG121NC1/I0, Gowin Education 1.9.9Beta-4.

| Presentation | Physical class | Logic resource | CLS | BSRAM | Fmax | Critical levels |
|---|---|---:|---:|---:|---:|---:|
| DIRECT | BSRAM | 0 LUT | 0 | 2 | 455.463 MHz | 1 |
| BALANCED | logic fabric | 108 LUT | 58 | 0 | 150.775 MHz | 6 |
| LINEAR | logic fabric | 92 LUT | 48 | 0 | 165.180 MHz | 6 |

Again, among logic-fabric realizations:

\[
L_8 <_{\rm area} B_8,
\qquad
L_8 >_{\rm Fmax} B_8.
\]

## Replicated shape

The two vendors reproduce the same qualitative W=8 shape:

\[
D_8 \to \text{hard-memory class},
\]

\[
B_8,L_8 \to \text{logic-fabric class},
\]

and, within the logic-fabric pair,

\[
L_8 < B_8
\]

by declared area metric, while LINEAR also has the higher measured Fmax.

This is a **two-vendor reproduction of qualitative partition/ranking shape**, not an invariant numerical identity.

The physical quotients remain fully separated:

\[
\mathcal P_{8}^{CV}
=
\mathcal P_{8}^{GW}
=
\{\{D\},\{B\},\{L\}\}.
\]

## Contrast with ABC-fast

At ABC-fast for W=8:

\[
D=156,\quad B=315,\quad L=562,
\]

so

\[
D < B < L.
\]

Both FPGA backends reverse the ordering of the logic-fabric pair:

\[
B <_{\rm ABC} L,
\]

but

\[
L <_{\rm CycloneV} B,
\qquad
L <_{\rm Gowin} B.
\]

Hence the W=8 ranking reversal is reproduced across two FPGA architectures.

## Claim boundary

This is not evidence for a universal ordering or a cross-vendor invariant.

The valid statement is:

> For the frozen W=8 strict-next-prime experiment, two independent FPGA backends reproduce the same qualitative physical partition and the same BALANCED/LINEAR ranking reversal relative to ABC-fast.

The next falsification gate is W=9, where Cyclone V had already crossed back to:

\[
B_9 < L_9.
\]

The key question is whether Gowin reproduces the same crossover location.
