# Future seed · Orbital port filtrations

Status: deferred idea only. Do not merge into the current HATTER-SOL-10 theorem line.

## Question

Can a factor or minimal principalization witness be modeled not only by a typed pair `(P,Q)`, but by an intrinsic **orbit of ports with an activation filtration**?

The motivating heuristic is:

> strongest port orbit is used first; weaker orbit(s) activate only when the stronger layer is saturated or insufficient.

This is not assumed in HATTER-SOL-10. It is only a possible future development.

## Current two-type decomposition

For a folded typed state

\[
(P,Q),\qquad P\ge Q,
\]

one may formally write

\[
(P,Q)=(P-Q,0)+(Q,Q).
\]

This suggests, but does not prove, an interpretation as

- a dominant layer of size `P-Q`, and
- a secondary paired layer of size `Q`.

Examples from the current nonprincipal witness-switching work:

\[
(6,1)=(5,0)+(1,1),
\]

\[
(3,2)=(1,0)+(2,2).
\]

The observed host-size switch `(3,2) -> (6,1)` could then be reinterpreted as an activation transition between different internal orbital port architectures.

## Candidate general object

Instead of a pair, consider

\[
\mathcal O(\alpha)=
(O_1,c_1;O_2,c_2;\ldots),
\]

where `O_j` is an orbit of equivalent interface directions under a canonical symmetry/stabilizer action, and `c_j` is its multiplicity/capacity.

A stronger future model could carry a filtration

\[
F_0\subset F_1\subset F_2\subset\cdots
\]

of activated port orbits, with a rule such as

\[
O_{j+1}\text{ becomes available only after }O_j\text{ reaches a canonical saturation condition}.
\]

## Required proof obligations before this becomes mathematics

1. Identify the acting symmetry group canonically.
2. Prove that the proposed port orbits are basis-independent.
3. Derive an intrinsic ordering/ranking of the orbits; `P>=Q` alone is not enough.
4. Show that any strongest-first activation law follows from the arithmetic/geometric structure rather than being imposed ad hoc.
5. Recover the current HATTER-SOL `(P,Q)` model by a well-defined forgetting/projection map.
6. Re-test all current witness-switching examples under the refined object.

## Possible hierarchy

For a nonprincipal ideal one may ultimately have two levels:

\[
I
\longrightarrow
\mathscr W(I)
\longrightarrow
\mathcal O(\alpha),
\]

that is:

\[
\text{ideal}
\to
\text{minimal witness orbit}
\to
\text{port orbits / activation filtration}.
\]

This could become a separate post-HATTER-SOL-10 branch. Until then, current work continues with witness states `(P,Q)` and the host-size phase-transition problem.