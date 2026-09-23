# H20 · W=9 cross-vendor divergence

Status: **BACKEND-DEPENDENT CROSSOVER LOCATION OBSERVED**

Arithmetic function: strict next-prime map on 9-bit input.

Presentations:

- \(B_9\): BALANCED threshold tree;
- \(L_9\): LINEAR threshold chain.

Both are formally equivalent to the same arithmetic map.

## Cyclone V result

Under Quartus II 13.1 on Cyclone V 5CEFA7F23C6:

\[
B_9 = 139\ \text{ALM},\quad 149.08\ \text{MHz},\quad 6\ \text{levels},
\]

\[
L_9 = 140\ \text{ALM},\quad 133.80\ \text{MHz},\quad 9\ \text{levels}.
\]

Thus:

\[
B_9 <_{\rm area} L_9,
\qquad
B_9 >_{\rm Fmax} L_9.
\]

Cyclone V therefore crossed from the W=8 ordering \(L_8<B_8\) to \(B_9<L_9\).

## Gowin GW5A-25 result

Under Gowin Education 1.9.9Beta-4 on GW5A-LV25MG121NC1/I0:

\[
B_9 = 190\ \text{LUT},\quad 99\ \text{CLS},\quad 129.124\ \text{MHz},\quad 6\ \text{levels},
\]

\[
L_9 = 185\ \text{LUT},\quad 101\ \text{CLS},\quad 133.955\ \text{MHz},\quad 7\ \text{levels}.
\]

Therefore Gowin still gives:

\[
L_9 <_{\rm LUT} B_9,
\qquad
L_9 >_{\rm Fmax} B_9.
\]

However, the CLS metric reverses:

\[
B_9 <_{\rm CLS} L_9.
\]

So even within one backend, scalar resource rankings depend on the chosen resource coordinate.

## Consequence

The W=8 qualitative ranking was reproduced by both FPGA families:

\[
L_8 < B_8.
\]

At W=9 the two backends diverge:

\[
B_9 <_{\rm CycloneV} L_9,
\]

while by Gowin LUT/Fmax observers:

\[
L_9 <_{\rm Gowin} B_9.
\]

Hence the finite-width crossover location is **not cross-vendor invariant**.

The observed presentation ranking must be treated as a function of at least

\[
(\text{backend},\text{device},W,\text{resource observer}).
\]

## Depth signal

Although Gowin W=9 still favors LINEAR by LUT count and Fmax, its critical depth has already grown beyond BALANCED:

\[
\operatorname{depth}(B_9)=6,
\qquad
\operatorname{depth}(L_9)=7.
\]

This suggests the depth crossover precedes the area/timing crossover on this backend.

This is an empirical finite-width observation, not an asymptotic theorem.

## Claim boundary

This result establishes only that the Cyclone-V and Gowin W=9 physical rankings differ for the frozen H20 experiment.

It does not establish:

- a universal ordering;
- a universal crossover width;
- asymptotic complexity;
- vendor-independent optimality;
- any number-theoretic consequence.

## Next falsification gate

Run W=10 DIRECT/BALANCED/LINEAR on Gowin.

The key question becomes:

> Does Gowin cross by W=10, remain LINEAR-favored, or produce a multi-coordinate tradeoff with no single winner?
