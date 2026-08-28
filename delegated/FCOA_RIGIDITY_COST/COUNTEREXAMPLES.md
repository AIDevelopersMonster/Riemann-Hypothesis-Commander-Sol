# FCOA Rigidity Cost — Counterexamples and Failed Conjectures

**Rule:** failed conjectures are retained here so the direction does not repeatedly reopen them.

## C1. “The directed Hamiltonian path is rigidity-minimal.” — FALSE

With three generic points, one directed edge plus one isolated point is already rigid: tail, head and isolate have distinct structural roles. Thus the G2 Hamiltonian path is not generally minimal for the weaker target `Aut = 1`. G2 spends extra cells to remember a global successor skeleton.

## C2. “Equal-size anonymous output fibers must be swappable.” — FALSE

On four generic points let

\[
A=\{01,02,03,10,12,21\}
\]

and use its six-cell complement as the other anonymous fiber. Exact enumeration gives

\[
\operatorname{Aut}(\{A,A^c\})=1.
\]

Equal cardinality is necessary for a fiber swap but not sufficient.

## C3. “A complete two-output tournament coloring always leaves reversal.” — FALSE

The transitive tournament used by G4-C has a reversal anti-automorphism. The five-vertex tournament

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}
\]

is asymmetric and non-self-converse. Hence the anonymous partition

\[
\{T_5,T_5^{\rm op}\}
\]

is rigid.

## C4. “One anchor is globally necessary for G4-style complete domains.” — FALSE

One anchor is sufficient and minimal **inside the transitive-order G4-C branch**. It is not globally necessary among all complete-domain two-anonymous-output colorings. Unbalanced rigid fibers and balanced asymmetric non-self-converse tournament fibers both give zero-anchor rigidity.

## C5. “Association Spectrum detects skeleton geometry.” — FALSE in the terminal generic layer

If `m` off-diagonal generic cells with terminal outputs are added to M0, then

\[
\Delta(EQ,NEQ,LEFT,RIGHT,NONE)=(m,0,m,m,-3m)
\]

regardless of skeleton shape or terminal value partition.

## C6. “Domain + alphabet size + fiber balance + Association Spectrum + commutation determine rigidity.” — FALSE

For every generic size `n >= 5`, compare G4-C with the asymmetric non-self-converse tournament family from `RESULTS.md`. Both have:

- complete generic domain;
- two anonymous outputs;
- equal fiber sizes;
- the same Association Spectrum;
- the same commutation count.

Yet G4-C has full-operation group `C2`, whereas the tournament layer is rigid.

## C7. “An undirected skeleton can rigidify every small generic sector.” — FALSE

No asymmetric simple graph exists on fewer than six vertices. Therefore full rigidity by an undirected simple skeleton is impossible for generic sizes `n=2,3,4,5`.

## C8. “A pure carrier admits a canonical symmetry-breaking skeleton.” — FALSE

If a construction is natural under every bijection of a pure `n`-element carrier, every element of `S_n` preserves the resulting skeleton. A symmetry-breaking rule must use additional transported structure.

## C9. “Anonymous outputs need external names to become distinguishable.” — FALSE

Unequal value-fiber cardinalities already prevent a fiber swap. The outputs remain unnamed but become structurally distinguishable through their preimages.

## C10. “The small exact tables already show the asymptotic law.” — NOT ACCEPTED

The exact values through generic size seven are calibration data. No asymptotic formula is accepted without proof or a dedicated literature audit.

## C11. “The cyclic-triangle count tau3 determines residual anonymous symmetry.” — FALSE

Already on five generic vertices, tournaments with the same `tau3` may have different pairs

\[
(|\operatorname{Aut}(T)|,|\operatorname{Anti}(T)|).
\]

Thus `tau3` is the locality-minimal separator for G4-C versus a rigid tournament, but it is not a complete classifier of `Aut^±`.

## C12. “Taking all anonymous local histograms through n-1 vertices recovers the residual group.” — FALSE

The explicit seven-vertex pair `S7/R7` from `FIBER_PROFILE_HIERARCHY.md` has

\[
H_k^{\pm}(S_7)=H_k^{\pm}(R_7)
\quad\text{for every }k=3,4,5,6,
\]

but

\[
\operatorname{Aut}^{\pm}(S_7)\cong C_2,
\qquad
\operatorname{Aut}^{\pm}(R_7)=1.
\]

So the missing information is not merely another histogram count. It is cross-subset coherence.

## C13. “The classical seven-local reconstruction theorem is just a stronger histogram theorem.” — FALSE

The classical `(<=7)` half-reconstruction result is subset-indexed: corresponding restrictions on each carrier subset are compared up to converse. This retains overlap coherence. A histogram only records multiplicities of local types and can fail even when every proper order is included.

## Firewall

None of these counterexamples modifies the published M0–G2 checkpoint. They also do not refute the G4-C construction; they restrict the scope of any minimality or inevitability interpretation attached to it.