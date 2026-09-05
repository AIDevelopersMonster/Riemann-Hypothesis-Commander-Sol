# FCOA Rigidity Cost — Counterexamples and Failed Conjectures

**Rule:** failed conjectures are retained here so the direction does not repeatedly reopen them.

## C1. “The directed Hamiltonian path is rigidity-minimal.” — FALSE

With three generic points, one directed edge plus one isolated point is already rigid: tail, head and isolate have distinct structural roles. Thus the G2 Hamiltonian path is not generally minimal for the weaker target `Aut = 1`. G2 spends extra cells to remember a global successor skeleton.

## C2. “Equal-size anonymous output fibers must be swappable.” — FALSE

On four generic points let

\[
A=\{01,02,03,10,12,21\}
\]

and use its six-cell complement as the other anonymous fiber. Exact enumeration gives `Aut({A,A^c})=1`.

## C3. “A complete two-output tournament coloring always leaves reversal.” — FALSE

The transitive tournament used by G4-C has a reversal anti-automorphism. The five-vertex tournament

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}
\]

is asymmetric and non-self-converse. Hence the anonymous partition `{T5,T5^op}` is rigid.

## C4. “One anchor is globally necessary for G4-style complete domains.” — FALSE

One anchor is sufficient and minimal inside the transitive-order G4-C branch. It is not globally necessary among all complete-domain two-anonymous-output colorings.

## C5. “Association Spectrum detects skeleton geometry.” — FALSE in the terminal generic layer

If `m` off-diagonal generic cells with terminal outputs are added to M0, then

\[
\Delta(EQ,NEQ,LEFT,RIGHT,NONE)=(m,0,m,m,-3m)
\]

regardless of skeleton shape or terminal value partition.

## C6. “Domain + alphabet size + fiber balance + Association Spectrum + commutation determine rigidity.” — FALSE

For every generic size `n>=5`, G4-C and the asymmetric non-self-converse tournament family have the same complete generic domain, two anonymous outputs, equal fiber sizes, Association Spectrum and commutation count, but groups `C2` and `1` respectively.

## C7. “An undirected skeleton can rigidify every small generic sector.” — FALSE

No asymmetric simple graph exists on fewer than six vertices.

## C8. “A pure carrier admits a canonical symmetry-breaking skeleton.” — FALSE

A construction natural under every bijection of a pure finite carrier is preserved by all of `S_n`.

## C9. “Anonymous outputs need external names to become distinguishable.” — FALSE

Unequal value-fiber cardinalities already prevent a fiber swap.

## C10. “The small exact tables already show the asymptotic law.” — NOT ACCEPTED

Exact small values are calibration data only.

## C11. “The cyclic-triangle count tau3 determines residual anonymous symmetry.” — FALSE

Already on five generic vertices, tournaments with the same `tau3` may have different `(Aut,Anti)` data. `tau3` is a minimal separator for G4-C versus rigidity, not a complete classifier.

## C12. “Taking all anonymous local histograms through n-1 vertices recovers the residual group.” — FALSE

The explicit seven-vertex pair `S7/R7` from `FIBER_PROFILE_HIERARCHY.md` has

\[
H_k^{\pm}(S_7)=H_k^{\pm}(R_7)
\quad(k=3,4,5,6),
\]

but

\[
\operatorname{Aut}^{\pm}(S_7)\cong C_2,
\qquad
\operatorname{Aut}^{\pm}(R_7)=1.
\]

The missing information is cross-subset coherence.

## C13. “The classical seven-local reconstruction theorem is just a stronger histogram theorem.” — FALSE

The classical `(<=7)` half-reconstruction result is subset-indexed and compares corresponding restrictions up to isomorphism/converse-isomorphism. Histograms retain less information.

## C14. “The full C3-hypergraph is stabilizer-complete.” — FALSE

The cyclic-triple incidence hypergraph

\[
\mathcal C_3(T)=\{X:T[X]\cong C_3\}
\]

forgets the middle vertex of every transitive triple.

For G4-C, `C3(T)` is empty, hence

\[
\operatorname{Aut}(\mathcal C_3(T))=S_n
\]

while

\[
\operatorname{Aut}^{\pm}(T)=C_2.
\]

For the rigid witness `T5`, the hyperedges are exactly

\[
\{0,1,3\},\qquad\{0,2,3\},
\]

so

\[
\operatorname{Aut}(\mathcal C_3(T_5))\cong C_2\times C_2,
\]

while `Aut^±(T5)=1`.

For the recursive rigid family, successive universal sources are isolated in the C3-hypergraph, so

\[
|\operatorname{Aut}(\mathcal C_3(T_n))|=4(n-4)!
\]

although the tournament layer remains rigid. Thus the stabilizer error can grow factorially.

The exact ternary repair is the betweenness relation in `BETWEENNESS_REDUCT.md`.

## C15. “The 7-local half-reconstruction ceiling prevents an exact ternary reduct.” — FALSE

The number 7 is optimal for a specific weaker data model: each local subset is retained only up to abstract isomorphism/converse-isomorphism. If labeled local roles are retained, the ternary relation

\[
B_\star(x,y,z)\iff x\star y=y\star z=x\star z
\]

already satisfies

\[
\operatorname{Aut}(B_\star)=\operatorname{Aut}^{\pm}(T).
\]

There is no contradiction because the information models differ.

## Firewall

None of these counterexamples modifies the published M0–G2 checkpoint. They do not refute G4-C; they restrict the scope of minimality or inevitability interpretations attached to it.