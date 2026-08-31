# SOL-TOPO

**Scientific direction:** non-Abelian anyons, fusion channels, braid/path memory  
**Parent:** `delegated/FCOA_Z_SYMMETRIC_LINE/APPLIED_DIRECTIONS/`  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Status:** MODEL-CANDIDATE THRESHOLD REACHED / FULL COHERENCE OPEN

## Main progression

The useful correspondence is

\[
\boxed{\text{mixed/typed interaction}\to\text{output-channel fiber},}
\]

not `+ - -> commutativity`.

The first strike established an exact one-step Ising fusion-support shadow and proved that strict line geometry cannot itself generate braid topology.

The second strike activates a split terminal orbit as a two-state internal LC2 fiber. The old split reflection gives an involution `J`; retained legacy/reflected provenance gives an involution `S`. They obey

\[
J^2=S^2=I,
\qquad
JS=-SJ,
\qquad
(JS)^2=-I.
\]

After free linearization, the unique minimal duality in `span_R{J,S}` that exchanges the two canonical observables is

\[
\boxed{
F=\frac{J+S}{\sqrt2}
=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
}
\]

which is exactly the standard nontrivial Ising `F` matrix.

For a channel-preserving phase exchange

\[
R_t=\operatorname{diag}(1,t),
\qquad |t|=1,
\]

and

\[
B_t=FR_tF,
\]

the braid relation holds iff

\[
\boxed{(t-1)(t^2+1)=0.}
\]

Thus the nontrivial relative phases are

\[
\boxed{t=\pm i,}
\]

giving the standard Ising `R` matrix projectively, with the common phase left undetermined.

This produces a genuine non-Abelian projective braid representation on the internal two-state fiber while the spatial carrier remains one-dimensional.

## Sharp boundaries

1. Pure deterministic set-level LC2 re-entry can only induce permutation/monomial matrices and therefore cannot produce the Ising Hadamard `F`; additive linearization is a minimum extra resource.
2. The FCOA split-output geometry generates the `J,S` scaffold, and the association-duality requirement fixes `F`; however, identifying these bases with fusion-tree bases is new LC2 semantics.
3. Conservative LC2 activation allows every phase `t in U(1)`. The old FCOA data therefore do not select `t=±i`; braid/Yang-Baxter coherence is an independent new axiom that selects it.
4. The global Ising phase `e^{-i pi/8}`, topological twist, arbitrary fusion trees, and full pentagon/hexagon coherence are not yet generated.
5. Strict one-dimensional collision-free carrier topology remains braid-trivial. The non-Abelian memory lives in an internal output fiber, not in line geometry.

## Current verdict

\[
\boxed{\texttt{MODEL CANDIDATE — PROJECTIVE FOUR-}\sigma\texttt{ BRAID-QUBIT SUBSYSTEM}}
\]

for the **LC2-enriched** FCOA theory.

Spatial carrier status remains

\[
\boxed{\texttt{1D-CLOSED}}
\]

for this finite internal braid representation. No emergent second spatial coordinate has been proved or required.

## Files

- `SOL_TOPO_REPORT_v0_1.md` — fusion-support embedding, conservative mixed-sector construction, terminal-sink obstruction, strict-line braid no-go.
- `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md` — split-fiber activation, reflection/provenance Clifford structure, canonical Hadamard theorem, braid-phase classification, projective Ising braid subsystem, coherence-independence theorem.

## Publication status

The line has reached a model-candidate threshold but should still remain in the research branch before standalone publication.

One coherence strike remains:

\[
\boxed{
\text{Can pentagon/hexagon coherence be generated from LC2 re-entry, or must an independent tensor/fusion layer be added?}
}
\]

A positive construction or a strong minimum-resource no-go theorem at that gate should be considered publication-grade.