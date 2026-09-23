# H20 Cyclone V · W=8..9 presentation crossover

Status: **CROSSOVER OBSERVED**

Target: Cyclone V 5CEFA7F23C6  
Toolchain: Quartus II 13.1  
Clock contract: 100 MHz

The arithmetic function is the strict next-prime map and the three source presentations are formally equivalent.

## W=8

Measured post-P&R profiles:

| Presentation | ALMs | Registers | Fmax | Worst data delay | Logic levels |
|---|---:|---:|---:|---:|---:|
| DIRECT | 3 | 8 | 496.03 MHz | 1.870 ns | 0 |
| BALANCED | 78 | 17 | 210.17 MHz | 4.581 ns | 4 |
| LINEAR | 48 | 17 | 254.13 MHz | 3.765 ns | 4 |

Among the two logic-fabric realizations:

\[
L_8 <_{\rm ALM} B_8,\qquad
L_8 >_{\rm Fmax} B_8.
\]

Thus W=8 reverses the ABC-fast ordering between BALANCED and LINEAR.

## W=9

Measured post-P&R profiles:

| Presentation | ALMs | Registers | Fmax / restricted Fmax | Worst data delay | Logic levels |
|---|---:|---:|---:|---:|---:|
| DIRECT | 5 | 9 | 527.15 / 315.06 MHz | 1.719 ns | 0 |
| BALANCED | 139 | 19 | 149.08 MHz | 6.516 ns | 6 |
| LINEAR | 140 | 19 | 133.80 MHz | 7.287 ns | 9 |

At W=9:

\[
B_9 <_{\rm ALM} L_9,
\qquad
B_9 >_{\rm Fmax} L_9.
\]

Therefore the W=8 physical reversal does **not** persist at W=9.

Instead, a width-dependent crossover is observed:

\[
L_8 <_{\rm CycloneV} B_8,
\qquad
B_9 <_{\rm CycloneV} L_9.
\]

## Interpretation

The physical ordering of equivalent arithmetic presentations is not a fixed invariant of the source family.

It depends on at least:

1. the observer / backend stage;
2. the target FPGA architecture;
3. the finite input width W.

This strengthens the H20 programme thesis that representation transport must be treated as a trajectory of observer-dependent physical profiles, not as a single scalar ranking.

## DIRECT remains a separate physical class

DIRECT is inferred as ROM / M10K rather than ordinary logic fabric. It therefore remains inappropriate to compare it against BALANCED and LINEAR using ALM count alone.

A physical observer should be vector-valued, e.g.

\[
O_{\rm phys}
=
(\text{resource class},\text{ALM},\text{RAM},F_{\max}^{restricted},
\text{delay},\text{logic levels}).
\]

## Claim boundary

The observed crossover is empirical for the frozen W=8 and W=9 experiments under Quartus II 13.1 on Cyclone V 5CEFA7F23C6.

It does not prove a universal crossover law, asymptotic ordering, minimum circuit complexity, or any number-theoretic consequence.
