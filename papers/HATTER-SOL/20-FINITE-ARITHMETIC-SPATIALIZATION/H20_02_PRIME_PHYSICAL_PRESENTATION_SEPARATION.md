# H20-02 · Prime physical presentation separation

Status: **TWO-VENDOR PHYSICAL LAYER CLOSED**

Arithmetic function:

\[
S_W(x)=\min\{p>x:p\text{ prime}\}.
\]

Frozen presentations:

- \(D_W\): DIRECT truth-table presentation;
- \(B_W\): BALANCED threshold tree;
- \(L_W\): LINEAR ordered threshold chain.

Formal Yosys SAT equivalence had already established

\[
D_W \equiv B_W \equiv L_W
\]

for all \(W=4,\dots,10\).

This layer compares post-P&R physical images for \(W=8,9,10\) on two FPGA architectures.

---

## 1. Cyclone V · Quartus II 13.1 · 5CEFA7F23C6

| W | Presentation | Physical class | Area | Fmax | Worst delay | Levels |
|---:|---|---|---:|---:|---:|---:|
| 8 | DIRECT | M10K ROM | 3 ALM | 496.03 MHz | 1.870 ns | 0 |
| 8 | BALANCED | logic fabric | 78 ALM | 210.17 MHz | 4.581 ns | 4 |
| 8 | LINEAR | logic fabric | 48 ALM | 254.13 MHz | 3.765 ns | 4 |
| 9 | DIRECT | M10K ROM | 5 ALM | 527.15 / 315.06 MHz restricted | 1.719 ns | 0 |
| 9 | BALANCED | logic fabric | 139 ALM | 149.08 MHz | 6.516 ns | 6 |
| 9 | LINEAR | logic fabric | 140 ALM | 133.80 MHz | 7.287 ns | 9 |
| 10 | DIRECT | M10K ROM | 6 ALM | 338.29 / 315.06 MHz restricted | 2.768 ns | 0 |
| 10 | BALANCED | logic fabric | 276 ALM | 122.44 MHz | 7.967 ns | 7 |
| 10 | LINEAR | logic fabric | 293 ALM | 111.35 MHz | 8.771 ns | 13 |

Cyclone-V logic-fabric ordering:

\[
L_8 < B_8,
\]

but

\[
B_9 < L_9,\qquad B_{10}<L_{10}.
\]

Hence the Cyclone-V crossover occurs between \(W=8\) and \(W=9\).

---

## 2. Gowin GW5A-25 · Gowin Education 1.9.9Beta-4

| W | Presentation | Physical class | LUT | CLS | BSRAM | Fmax | Worst delay | Levels |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 8 | DIRECT | BSRAM | 0 | 0 | 2 | 455.463 MHz | 2.122 ns | 1 |
| 8 | BALANCED | logic fabric | 108 | 58 | 0 | 150.775 MHz | 6.614 ns | 6 |
| 8 | LINEAR | logic fabric | 92 | 48 | 0 | 165.180 MHz | 5.993 ns | 6 |
| 9 | DIRECT | BSRAM | 0 | 0 | 2 | 565.494 MHz | 1.730 ns | 1 |
| 9 | BALANCED | logic fabric | 190 | 99 | 0 | 129.124 MHz | 7.723 ns | 6 |
| 9 | LINEAR | logic fabric | 185 | 101 | 0 | 133.955 MHz | 7.393 ns | 7 |
| 10 | DIRECT | BSRAM | 0 | 0 | 2 | 493.494 MHz | 1.955 ns | 1 |
| 10 | BALANCED | logic fabric | 309 | 166 | 0 | 105.619 MHz | 9.394 ns | 6 |
| 10 | LINEAR | logic fabric | 313 | 165 | 0 | 103.719 MHz | 9.589 ns | 7 |

At W=8:

\[
L_8 <_{\rm LUT} B_8,
\qquad
L_8 >_{\rm Fmax} B_8.
\]

At W=9:

\[
L_9 <_{\rm LUT} B_9,
\qquad
L_9 >_{\rm Fmax} B_9,
\]

while BALANCED has smaller depth and slightly smaller CLS count:

\[
B_9 <_{\rm depth} L_9,
\qquad
99<101.
\]

At W=10:

\[
B_{10} <_{\rm LUT} L_{10},
\qquad
B_{10} >_{\rm Fmax} L_{10},
\qquad
B_{10} <_{\rm depth} L_{10},
\]

but LINEAR retains a one-CLS advantage:

\[
165<166.
\]

Therefore the Gowin crossover in the primary LUT/timing observer occurs between \(W=9\) and \(W=10\).

---

## 3. Backend-dependent crossover location

The two backends do not place the crossover at the same finite width.

Cyclone V:

\[
L_8<B_8,\qquad
B_9<L_9,\qquad
B_{10}<L_{10}.
\]

Gowin:

\[
L_8<B_8,\qquad
L_9<B_9,\qquad
B_{10}<L_{10}
\]

for the primary LUT/ALM plus timing comparison.

Thus the physical ordering trajectory depends on both finite width and realization backend:

\[
\boxed{
\text{presentation ordering}
=
f(\text{backend},W,\text{observer})
}
\]

and the crossover location itself is backend-dependent.

This is stronger than a single backend ranking reversal.

---

## 4. Stable cross-vendor result: DIRECT selects hard memory

Across both FPGA architectures and all measured widths \(W=8,9,10\),

\[
D_W
\]

is mapped into a hard-memory resource class rather than ordinary logic fabric:

- Cyclone V: M10K ROM;
- Gowin GW5A-25: 2 BSRAM.

Meanwhile BALANCED and LINEAR remain logic-fabric realizations.

This gives a two-vendor reproduction of the qualitative resource-class shape:

\[
D_W\to\text{hard memory},
\qquad
B_W,L_W\to\text{logic fabric}.
\]

The statement is qualitative and flow-specific; it is not a universal synthesis theorem.

---

## 5. Physical observer must be vector-valued

No single scalar cost is sufficient.

A suitable observer must include at least

\[
O_{\rm phys}
=
(
\text{resource class},
\text{logic area},
\text{hard memory},
F_{\max},
\text{worst delay},
\text{logic depth},
\text{register topology}
).
\]

The Gowin W=9 and W=10 results show why: LUT, CLS, depth, and timing do not always induce the same ordering.

---

## 6. Contrast with ABC-fast

For Yosys ABC-fast, the measured ordering was stable over W=8,9,10:

\[
D_W < B_W < L_W.
\]

The FPGA backends do not preserve that scalar ordering.

At W=8 both vendors reverse the BALANCED/LINEAR pair.

Cyclone V crosses back by W=9.

Gowin crosses back only by W=10.

Therefore the scalar ordering is not preserved by representation transport from ABC-fast into vendor-specific place-and-route.

---

## 7. Timing interpretation

Both logic realizations still satisfy the 100 MHz declared clock contract at W=10 on Gowin:

\[
F_{\max}(B_{10})=105.619\text{ MHz},
\]

\[
F_{\max}(L_{10})=103.719\text{ MHz}.
\]

However margins are already small.

The W=10 Gowin worst paths are dominated substantially by routing, not only Boolean logic depth.

Hence physical degradation cannot be inferred from source expression depth alone.

---

## 8. Claim boundary

This layer establishes only the measured post-P&R behavior for the frozen strict-next-prime experiment:

- W=8,9,10;
- Cyclone V 5CEFA7F23C6 under Quartus II 13.1;
- Gowin GW5A-LV25MG121NC1/I0 under Gowin Education 1.9.9Beta-4;
- the declared registered shell and 100 MHz clock contract.

It does **not** establish:

- global circuit optimality;
- universal crossover widths;
- asymptotic complexity;
- a vendor-independent scalar ranking;
- a new theorem on primes;
- any implication for the Riemann Hypothesis.

The result is a finite empirical theorem-layer about representation transport into two concrete FPGA realization systems.

---

## 9. Next programme step

The physical benchmarking gate is now closed.

The next H20 question should move from comparing equivalent presentations at fixed W to studying the structural increment

\[
\Delta_W = C_{W+1}\ominus C_W
\]

or, more generally, the exact transformation law between adjacent finite prime circuits.

The next substantive target is to test whether these increments admit recurrent finite structural types or a recursively compact description.
