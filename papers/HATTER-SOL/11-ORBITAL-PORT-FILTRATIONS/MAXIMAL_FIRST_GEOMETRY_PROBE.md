# HATTER-SOL-11 · Maximal-First Geometry Probe

**Branch:** `research/hatter-sol-orbital-port-filtrations`  
**Status:** methodological layer; not a model axiom and not a canonical orbital law.

## 1. Why this note exists

An earlier HATTER-SOL working convention was easy to misremember as a theorem:

> when several construction choices are available, inspect first the trajectory that uses / saturates the largest factor-capacities before smaller ones.

The purpose was practical: avoid duplicating every local choice while changing the ambient geometry and obtain one controlled comparison path.

It was **not** intended to assert that arithmetic, the port-orbit structure, or the physical world obeys a universal strongest-first activation law.

This distinction is now mandatory in HATTER-SOL-11.

---

## 2. Three different objects that must not be conflated

### 2.1 Full model

For arithmetic data `A` and an admissible geometry / host class `G`, let

\[
\mathfrak F(A;G)
\]

denote the full feasible family of HATTER-SOL networks (including every allowed witness, orbit, placement, and edge choice relevant to the current model).

The full response is obtained by optimizing over all of `\mathfrak F(A;G)`.

This is the primary mathematical object.

### 2.2 Canonical orbital structure

The orbital programme asks whether the arithmetic data itself determines intrinsic direction or port orbits, filtrations, stabilizers, norm shells, or related invariants.

These must be proved symmetry-invariant. They cannot be manufactured by a search heuristic.

### 2.3 Maximal-first probe

Choose an explicit priority convention `pi` that ranks the construction choices. The historical example is to rank factor-capacities from largest to smallest and, where the construction permits it, consume / saturate the currently highest-ranked available capacity before moving to the next rank.

Let

\[
\mathfrak F_{\mathrm{MF}}(A;G,\pi)
\subseteq
\mathfrak F(A;G)
\]

be the family reached by that restricted search rule (a singleton when the convention plus tie-breaking is deterministic, and a small family when ties are retained).

The corresponding response is the **maximal-first probe response**.

It is an auxiliary controlled experiment, not the definition of the HATTER-SOL response.

---

## 3. Explicit non-assumptions

The maximal-first probe does **not** imply any of the following:

1. `P>=Q` means that the `P` orbit is intrinsically stronger;
2. an inner norm shell must saturate before an outer shell activates;
3. larger arithmetic factors are physically or canonically prior to smaller ones;
4. the greedy trajectory is globally optimal;
5. the greedy trajectory is invariant under change of basis, unit action, conjugation, or an automorphism of the underlying arithmetic object.

Any such statement requires an independent theorem.

In particular, Theorem T11.6 in `ORBIT_FUSION_CLASSIFICATION.md` already rules out a universal sequential activation law for the canonical norm-shell filtration: outer-shell directions can occur with zero inner-shell usage.

---

## 4. What the probe is allowed to do

The probe is useful when the question is:

> keep one construction policy fixed and change only the geometry; what part of the response changes?

Examples of geometry changes include the HATTER-SOL-08 architecture ladder

\[
P\subset O\subset Pl\subset A,
\]

or a change of quadratic arithmetic world that alters the intrinsic direction geometry while the comparison protocol is held fixed.

The rule therefore acts as a **control gauge for an experiment**: it suppresses branching due purely to search order so that geometric effects can be inspected first.

If the probe and the full optimization later agree, that agreement is a result to be proved. It is not built into the construction.

---

## 5. Exact comparison with the full response

Let `B(N)` be the boundary vector of a feasible network `N`, and let `w` be any nonnegative scalarization vector appropriate to the response under study.

Define

\[
\Phi_w^{\mathrm{full}}(A;G)
:=
\min_{N\in\mathfrak F(A;G)} w\cdot B(N),
\]

and

\[
\Phi_w^{\mathrm{MF}}(A;G,\pi)
:=
\min_{N\in\mathfrak F_{\mathrm{MF}}(A;G,\pi)} w\cdot B(N),
\]

whenever the restricted family is nonempty.

Because

\[
\mathfrak F_{\mathrm{MF}}(A;G,\pi)
\subseteq
\mathfrak F(A;G),
\]

we have the elementary but useful inequality

\[
\boxed{
D_w(A;G,\pi)
:=
\Phi_w^{\mathrm{MF}}(A;G,\pi)
-
\Phi_w^{\mathrm{full}}(A;G)
\ge0.
}
\]

Call `D_w` the **selection penalty** of the maximal-first probe.

Thus the probe never certifies a better optimum than the full model. Equality means that, for that scalarization and instance, at least one full optimum is reachable under the chosen priority rule.

---

## 6. Geometry-change identity

For two geometries `G_0,G_1`, define

\[
\Delta_w^{\mathrm{full}}
=
\Phi_w^{\mathrm{full}}(A;G_1)
-
\Phi_w^{\mathrm{full}}(A;G_0),
\]

and

\[
\Delta_w^{\mathrm{MF}}
=
\Phi_w^{\mathrm{MF}}(A;G_1,\pi)
-
\Phi_w^{\mathrm{MF}}(A;G_0,\pi).
\]

Then identically

\[
\boxed{
\Delta_w^{\mathrm{MF}}
-
\Delta_w^{\mathrm{full}}
=
D_w(A;G_1,\pi)-D_w(A;G_0,\pi).
}
\]

### Interpretation

The maximal-first probe reproduces the **exact geometry response** for the scalarization `w` iff its selection penalty is unchanged between the two geometries.

In particular, if

\[
D_w(A;G_0,\pi)=D_w(A;G_1,\pi)=0,
\]

then the cheap probe and the full optimization give exactly the same geometry-change signal.

Conversely, disagreement between the two geometry signals measures a change in the cost of restricting the search order, not automatically a new arithmetic invariant.

This identity is bookkeeping, not a novelty claim, but it gives the precise semantics needed for future experiments.

---

## 7. Relation to orbital-port filtrations

The orbital programme and the maximal-first probe should now be kept in the order

\[
\boxed{
\text{intrinsic arithmetic/orbit data}
\longrightarrow
\text{full feasible response}
\longrightarrow
\text{optional maximal-first probe}.
}
\]

Not

\[
\text{maximal-first rule}
\longrightarrow
\text{invented orbital hierarchy}.
\]

If a maximal-first rule is applied to orbital data, the ranking `pi` must be stated explicitly. It may use, for example, factor capacity, norm shell, or another score, but that score remains part of the **experimental protocol** until an invariance theorem promotes it to intrinsic structure.

---

## 8. Immediate HATTER-SOL-11 use

The next orbital experiments should report both layers whenever computationally reasonable:

\[
\mathcal R_{\mathrm{full}}(A;G)
\quad\text{and}\quad
\mathcal R_{\mathrm{MF}}(A;G,\pi).
\]

Start with laboratories already present in this branch, especially the `Q(sqrt(-15))` witnesses and the generic odd-world direction-orbit model.

For each geometry change, record:

- the explicit priority rule `pi`;
- whether ties were kept or broken;
- whether the probe reaches a full optimum;
- the selection penalty `D_w` for the scalarizations used;
- whether the geometry-change signal survives removal of the maximal-first restriction.

This restores the original role of the convention: **a cheap controlled geometry probe, not a universal law of port activation**.
