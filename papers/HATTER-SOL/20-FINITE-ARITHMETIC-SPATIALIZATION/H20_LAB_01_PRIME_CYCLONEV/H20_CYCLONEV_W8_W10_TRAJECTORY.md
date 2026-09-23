# H20 · Cyclone V finite-width physical trajectory, W=8..10

Status: **H20-LAB-01 CLOSED**

Target: Cyclone V \`5CEFA7F23C6\`  
Toolchain: Quartus II 13.1  
Clock contract: 100 MHz  
Function: strict next-prime map

\[
S_W(x)=\min\{p>x:p\text{ prime}\}.
\]

The three source presentations are:

- \(D_W\): DIRECT truth-table presentation;
- \(B_W\): BALANCED threshold tree;
- \(L_W\): LINEAR ordered threshold chain.

Formal Yosys SAT equivalence was already proved for all \(W=4,\dots,10\).

## Physical profiles

### W=8

| Presentation | Physical class | ALMs | Regs | Fmax | Worst data delay | Logic levels |
|---|---|---:|---:|---:|---:|---:|
| DIRECT | ROM / M10K | 3 | 8 | 496.03 MHz | 1.870 ns | 0 |
| BALANCED | logic fabric | 78 | 17 | 210.17 MHz | 4.581 ns | 4 |
| LINEAR | logic fabric | 48 | 17 | 254.13 MHz | 3.765 ns | 4 |

Among logic-fabric realizations:

\[
L_8 <_{\rm ALM} B_8,
\qquad
L_8 >_{\rm Fmax} B_8.
\]

### W=9

| Presentation | Physical class | ALMs | Regs | Fmax / restricted | Worst data delay | Logic levels |
|---|---|---:|---:|---:|---:|---:|
| DIRECT | ROM / M10K | 5 | 9 | 527.15 / 315.06 MHz | 1.719 ns | 0 |
| BALANCED | logic fabric | 139 | 19 | 149.08 MHz | 6.516 ns | 6 |
| LINEAR | logic fabric | 140 | 19 | 133.80 MHz | 7.287 ns | 9 |

Thus:

\[
B_9 <_{\rm ALM} L_9,
\qquad
B_9 >_{\rm Fmax} L_9.
\]

### W=10

| Presentation | Physical class | ALMs | Regs | Fmax / restricted | Worst data delay | Logic levels |
|---|---|---:|---:|---:|---:|---:|
| DIRECT | ROM / M10K | 6 | 10 | 338.29 / 315.06 MHz | 2.768 ns | 0 |
| BALANCED | logic fabric | 276 | 21 | 122.44 MHz | 7.967 ns | 7 |
| LINEAR | logic fabric | 293 | 21 | 111.35 MHz | 8.771 ns | 13 |

At W=10:

\[
B_{10} <_{\rm ALM} L_{10},
\qquad
B_{10} >_{\rm Fmax} L_{10}.
\]

The 100 MHz clock contract is still met by both logic realizations:

\[
\text{setup slack}(B_{10})=1.833\text{ ns},
\]

\[
\text{setup slack}(L_{10})=1.019\text{ ns}.
\]

## Finite-width crossover

The physical ordering between BALANCED and LINEAR is not constant:

\[
L_8 <_{\rm CycloneV} B_8,
\]

but

\[
B_9 <_{\rm CycloneV} L_9,
\qquad
B_{10} <_{\rm CycloneV} L_{10}.
\]

Therefore a crossover occurs between W=8 and W=9 in this frozen Quartus/Cyclone-V experiment.

This is not merely an ABC-to-FPGA ranking reversal. It is a width-dependent physical ranking trajectory.

## Depth trajectory

The measured worst-path logic depth provides an additional observer:

\[
B: 4\to6\to7,
\]

\[
L: 4\to9\to13
\]

for \(W=8,9,10\).

Thus after the W=8 anomaly, the LINEAR presentation develops a substantially deeper physical critical path than BALANCED.

This does not prove asymptotic depth bounds; it is an empirical finite-width trajectory.

## DIRECT trajectory

DIRECT remains in a different physical resource class throughout:

\[
256\times9,
\quad
512\times10,
\quad
1024\times11
\]

are inferred as ROM / M10K structures.

Its ALM count remains small:

\[
3\to5\to6,
\]

but this is not comparable to the logic-fabric realizations without accounting for hard-memory usage.

A suitable physical observer must therefore be vector-valued:

\[
O_{\rm phys}
=
(\text{resource class},
\text{ALM},
\text{RAM},
F_{\max}^{restricted},
\text{delay},
\text{logic levels}).
\]

## Observer trajectory

Semantically:

\[
\mathcal P_W^{\rm sem}=\{\{D,B,L\}\}.
\]

At ABC-fast for W=8..10:

\[
\mathcal P_W^{\rm ABC}=\{\{D\},\{B\},\{L\}\}.
\]

At Cyclone-V post-P&R:

\[
\mathcal P_W^{\rm CV}=\{\{D\},\{B\},\{L\}\},
\qquad W=8,9,10.
\]

The partition shape remains fully separated, but the induced scalar ordering of B and L changes with W.

## Constraint caveat

The projects intentionally constrain only the registered core clock. Quartus reports that the design is not fully constrained for all setup/hold requirements because external I/O delays and exact pins are not assigned.

The reported register-to-register core timing remains the declared observer for this laboratory. No board-level I/O timing claim is made.

## Claim boundary

This laboratory establishes only the measured trajectory for:

- the frozen strict-next-prime RTL family;
- W=8,9,10;
- Quartus II 13.1;
- Cyclone V 5CEFA7F23C6;
- the declared registered-shell and 100 MHz clock contract.

It does not establish:

- global optimality of any presentation;
- minimum circuit complexity;
- a universal crossover location;
- asymptotic ordering;
- cross-vendor invariance;
- a number-theoretic theorem or any implication for RH.

## Next falsification gate

Repeat the same W=8..10 D/B/L family on the already validated Gowin GW5A-25 backend.

The next question is whether the Cyclone-V crossover shape

\[
L_8<B_8,\quad B_9<L_9,\quad B_{10}<L_{10}
\]

is reproduced, shifted, or destroyed by a second FPGA architecture.
