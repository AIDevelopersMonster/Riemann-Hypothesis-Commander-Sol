# HATTER-SOL-11 · Orbital Port Filtrations

Branch: `research/hatter-sol-orbital-port-filtrations`

Base: merged `main` after HATTER-SOL-07--10 publication chain.

Status: open research branch.

## Central question

Does a factor or minimal principalization witness carry a **canonical filtration of port orbits** that refines the HATTER-SOL typed capacity pair?

The target architecture is

\[
I
\longrightarrow
\mathscr W(I)
\longrightarrow
\mathcal O(\alpha)
\longrightarrow
F_1\subset F_2\subset\cdots
\longrightarrow
(P,Q)
\longrightarrow
\text{network response}.
\]

The words `orbit`, `stronger`, `weaker`, and `activation` are not assumptions. They must be derived from an intrinsic symmetry action or rejected.

## First hostile target

Before constructing any activation law, try to falsify the naive claim:

> The folded pair `(P,Q)` canonically comes from an ordered pair of port orbits in which the `P`-orbit is intrinsically stronger and must be saturated before the `Q`-orbit activates.

Search first for counterexamples showing that:

1. different symmetry-compatible coordinate choices exchange the proposed orbit ranking;
2. the stabilizer acts transitively on directions that the `(P,Q)` projection separates;
3. two witnesses with the same folded `(P,Q)` have non-isomorphic internal port-orbit structure;
4. an apparent strongest-first law depends on a chosen basis, embedding, metric, or weight rather than arithmetic structure.

If any of these occur, the naive filtration is not canonical and must be replaced by a weaker invariant.

## Closed correction to the naive strongest-first idea

`ORBIT_FUSION_CLASSIFICATION.md` now closes the first hostile layer:

- generic imaginary-quadratic worlds have two natural direction orbits;
- the Gaussian and Eisenstein worlds are exactly the two orbit-fusion exceptions;
- a canonical norm-shell filtration exists in generic worlds;
- **universal sequential activation does not**.

In particular, T11.6 gives elements whose geodesic usage lies entirely in the outer shell while the inner shell has zero usage. Therefore no universal arithmetic law of the form

\[
\text{inner / stronger orbit must saturate before outer / weaker orbit activates}
\]

is permitted.

This no-go result does **not** prohibit using a strongest- or maximal-first convention as an explicitly chosen experimental search rule.

## Maximal-first geometry probe — methodological, not canonical

An earlier HATTER-SOL working convention was to inspect, as one controlled trajectory, constructions that use or saturate the largest available factor-capacities before smaller ones. Its purpose was to avoid duplicating every search branch while asking what changes when the ambient geometry changes.

That convention is restored here with strict semantics:

\[
\boxed{
\text{maximal-first is an optional probe, not a model axiom.}
}
\]

It must not be inferred from `P>=Q`, from norm-shell order, or from the existence of an orbital filtration.

The full formal statement is in `MAXIMAL_FIRST_GEOMETRY_PROBE.md`.

For arithmetic data `A`, geometry `G`, and an explicit priority rule `pi`, the restricted family

\[
\mathfrak F_{\mathrm{MF}}(A;G,\pi)
\subseteq
\mathfrak F(A;G)
\]

is compared with the full feasible family. For any nonnegative scalarization `w`, define

\[
D_w(A;G,\pi)
=
\Phi_w^{\mathrm{MF}}(A;G,\pi)
-
\Phi_w^{\mathrm{full}}(A;G)
\ge0.
\]

For a geometry change `G_0 -> G_1`, the exact bookkeeping identity is

\[
\boxed{
\Delta_w^{\mathrm{MF}}-\Delta_w^{\mathrm{full}}
=
D_w(A;G_1,\pi)-D_w(A;G_0,\pi).
}
\]

Thus a maximal-first probe reproduces the exact geometry signal precisely when its selection penalty is unchanged across the compared geometries. This is a control protocol, not a novelty claim.

## Candidate canonical data

For a witness `alpha`, possible intrinsic objects to test include:

- the unit/conjugation stabilizer of the witness orbit;
- the action of that stabilizer on primitive interface directions;
- orbit sizes and stabilizer indices;
- norm shells and shortest-step classes;
- incidence relations among direction orbits;
- principalization companion ideals and their automorphism action.

No ranking is accepted merely from numerical inequalities such as `P>=Q`.

## Mandatory recovery condition

Any successful orbital-port object `O(alpha)` must admit a well-defined forgetting map

\[
\boxed{
\mathcal O(\alpha)\longrightarrow\Pi(\alpha)=(P,Q)
}
\]

that exactly recovers the HATTER-SOL-09/10 typed model.

Thus HATTER-SOL-11 must refine, not replace, the published theory.

## First laboratory

Start with the nonprincipal prime ideal in

\[
K=\mathbb Q(\sqrt{-15}),
\qquad
\omega=\frac{1+\sqrt{-15}}2,
\]

from HATTER-SOL-10:

\[
\mathfrak q=(23,\omega-7),
\]

with minimal witness states

\[
S=(3,2),
\qquad
T=(6,1).
\]

Determine whether their different host-size behavior can be explained by distinct canonical port-orbit structures, or whether `(P,Q)` already exhausts the invariant information visible to the natural symmetry group.

The HATTER-SOL-10 observation

\[
(6,1)=(5,0)+(1,1),
\qquad
(3,2)=(1,0)+(2,2)
\]

is only a heuristic decomposition and is **not** to be treated as a theorem.

## Side line retained but no longer the main road

The binary-tail / residue-sector work later produced genuine information-loss results at the network projection stage, including the post-pair-flip collision mechanism and the exact count-support theorem.

Those results are retained as evidence that ordinary network response can forget arithmetic information, but further scalar-network classification is **paused** here. It is auxiliary to the central orbital question rather than a replacement for it.

The main direction is again

\[
\boxed{
\text{intrinsic directions}
\to
\text{symmetry orbits / norm shells}
\to
\text{full response}
\to
(P,Q)\text{ forgetting}
}
\]

with the maximal-first trajectory available only as an optional geometry probe.

## Publication discipline

Do not claim:

- a canonical port hierarchy without proving basis/symmetry invariance;
- strongest-first activation from the inequality `P>=Q` alone;
- maximal-first search order as a universal arithmetic law;
- equality of maximal-first and full responses without proof;
- new group-action facts that are standard orbit/stabilizer theory;
- a physical interpretation where only a combinatorial filtration has been proved.

A publishable HATTER-SOL-11 result requires at least one of:

1. a canonical nontrivial orbit filtration with an exact forgetting theorem;
2. a no-go theorem proving that no stronger ordered filtration can be recovered from the natural symmetry data under stated axioms;
3. a classification theorem identifying precisely when an ordered port-orbit hierarchy exists;
4. a theorem showing that an explicitly stated restricted probe is sufficient for a specified family of geometry changes.

## Immediate next step

Do **not** continue the scalar-network collision line first.

Return to the existing orbital classification and attack the forgetting map itself:

1. define the direction-labelled geodesic object before magnitude sorting;
2. identify exactly which information is lost in the map to `(P,Q)`;
3. classify when two non-isomorphic labelled/orbital states have the same folded pair;
4. only then compare full geometry response with the optional maximal-first probe on those collision classes.

The next theorem target is therefore a **classification of the fibers of the forgetting map**

\[
\mathcal O(\alpha)\longrightarrow(P,Q),
\]

not another residue-response collision theorem.