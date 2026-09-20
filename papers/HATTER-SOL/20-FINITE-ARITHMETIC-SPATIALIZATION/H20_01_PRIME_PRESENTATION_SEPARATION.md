# H20-01 · Prime presentation separation under Boolean synthesis

Status: **EMPIRICAL LAYER CLOSED FOR W=4..10**

## Frozen function

For each width \(W\),

\[
S_W(x)=\min\{p>x:p\text{ is prime}\},
\qquad 0\le x<2^W.
\]

Three source presentations implement the same function:

- \(D_W\): complete direct lookup;
- \(L_W\): ordered linear threshold chain;
- \(B_W\): balanced threshold decision tree.

## Formal semantic equivalence

Yosys SAT proved

\[
D_W=L_W=B_W
\]

for every

\[
W=4,5,6,7,8,9,10.
\]

The formal miter used the same generated RTL family and proved output mismatch impossible for all inputs.

Therefore the semantic observer induces

\[
\mathcal P_W^{\rm sem}=\{\{D,L,B\}\}
\]

throughout the measured width range.

## Raw compiler recognition

At the early post-proc stage, the direct table is recognized as a ROM-like object:

\[
D_W\mapsto \$mem\_v2
\]

while the linear and balanced presentations remain decision logic.

This is a source-presentation effect and is not yet a fair Boolean-circuit cost comparison.

## Boolean normalization

For the fair circuit comparison, memory cells are expanded using the Yosys memory_map pass before technology mapping and ABC.

The resulting boolnorm stage puts all three presentations into ordinary Boolean logic.

## ABC-fast cell counts

| W | DIRECT | BALANCED | LINEAR |
|---:|---:|---:|---:|
| 4 | 18 | 26 | 37 |
| 5 | 35 | 56 | 75 |
| 6 | 56 | 112 | 158 |
| 7 | 93 | 175 | 292 |
| 8 | 156 | 315 | 562 |
| 9 | 243 | 588 | 1128 |
| 10 | 407 | 1079 | 2226 |

For every measured width,

\[
\mathrm{cells}(D_W)
<
\mathrm{cells}(B_W)
<
\mathrm{cells}(L_W).
\]

The three structural signatures are also distinct in the measured wire/wire-bit coordinates.

Hence for the observer

\[
O_{\rm ABC}=(\#cells,\#wires,\#wirebits)
\]

the partition is

\[
\mathcal P_W^{\rm ABC}
=
\{\{D\},\{B\},\{L\}\}
\]

for every \(W=4,\ldots,10\).

The same three-way separation is present at the Boolean-normalized and technology-mapped observers in this width range.

## First H20 observation

We therefore have, for the same finite arithmetic function,

\[
\boxed{
\mathcal P_W^{\rm sem}
=
\{\{D,L,B\}\}
\neq
\mathcal P_W^{\rm ABC}
=
\{\{D\},\{B\},\{L\}\}.
}
\]

Semantic equivalence does not force structural equivalence under this synthesis flow.

More strongly, the source presentation effect survives

\[
\text{source}
\to
\text{Boolean normalization}
\to
\text{techmap}
\to
\text{ABC-fast}
\]

through all tested widths.

## Important interpretation boundary

This result does **not** establish:

- a closed formula for primes;
- a lower bound or minimum circuit for next-prime;
- that DIRECT is globally optimal;
- that ABC-fast produces canonical or globally minimal circuits;
- that the observed ordering persists for all widths, synthesis settings, or technologies;
- any implication for the Riemann hypothesis.

The valid statement is narrower:

> In the controlled \(W=4..10\) next-prime family, three formally equivalent arithmetic presentations remain structurally distinguishable after a matched Boolean synthesis flow, with a stable measured cell-count ordering DIRECT < BALANCED < LINEAR.

This is evidence that arithmetic presentation is an experimentally meaningful variable even after semantics is frozen.

## Why this matters for the programme

The result distinguishes two questions:

1. Does a finite Boolean realization exist?
2. Which representation of the same arithmetic truth produces which Boolean geometry?

The first is elementary finite-function realizability.

The second is the H20 research object.

A later search for compact arithmetic or zeta-derived observers should therefore be evaluated not only by semantic correctness but by the downstream circuit geometry they induce.
