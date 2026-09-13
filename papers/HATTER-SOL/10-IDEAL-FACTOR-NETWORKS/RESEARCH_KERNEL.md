# HATTER-SOL-10 · Ideal Factor Networks

## Research kernel

**Branch:** `research/hatter-sol-ideal-factor-networks`  
**Parent:** HATTER-SOL-09, `research/hatter-sol-world-interface-operators`  
**Primary target:** `IDEAL_TYPED_CAPACITY`

## 1. Motivation

HATTER-SOL-09 attaches typed network nodes to irreducible **elements**. This is canonical only in a UFD/PID setting. In a general imaginary quadratic ring, element factorization is not unique, while nonzero ideals still factor uniquely into prime ideals.

The target of HATTER-SOL-10 is therefore

\[
\text{element factor network}
\longrightarrow
\text{ideal factor network},
\]

without losing the typed response of HATTER-SOL-09 in the principal/UFD case.

## 2. Non-negotiable compatibility requirement

A valid ideal capacity must satisfy:

1. **Ideal canonicity:** it is attached to the integral ideal itself, not to a chosen basis.
2. **Unit invariance:** changing a principal generator by a unit changes nothing.
3. **Conjugation compatibility:** conjugate prime ideals have conjugate/folded-compatible data.
4. **HATTER-SOL-09 recovery:** if `I=(alpha)` is principal, the ideal construction must recover the old typed element capacity `Pi(alpha)`.
5. **Nonprincipal existence:** the construction remains nonempty for nonprincipal ideals.

## 3. First rejected candidate: normalized ideal-lattice shape alone

For an integral ideal `I`, the classical normalized norm form is

\[
Q_I(x)=\frac{|N(x)|}{N(I)},\qquad x\in I.
\]

If `I=(alpha)` is principal, multiplication by `alpha` identifies the normalized form with that of `O_K`:

\[
Q_{(\alpha)}(\alpha y)=|N(y)|.
\]

Hence any capacity depending only on the normalized ideal-lattice shape / ideal class is constant on all principal ideals. It cannot recover the varying HATTER-SOL-09 pairs of different principal factors.

**No-go principle:** an ideal-class invariant by itself is too coarse for HATTER-SOL-09 compatibility.

## 4. Current candidate: minimal principal subideal

For a nonzero integral ideal `I` define

\[
\boxed{
\delta(I)
:=
\min_{0\ne\alpha\in I}
\frac{|N(\alpha)|}{N(I)}.
}
\]

Because `(alpha) subset I`, every ratio is the finite index

\[
\frac{|N(\alpha)|}{N(I)}=[I:(\alpha)]\in\mathbb Z_{\ge1}.
\]

Define the minimal-witness set

\[
\boxed{
\mathcal M(I)
:=
\{\alpha\in I\setminus\{0\}:|N(\alpha)|=\delta(I)N(I)\}.
}
\]

For the world-dependent element capacity `Pi_K(alpha)` already built in HATTER-SOL-09, define the **ideal interface frontier**

\[
\boxed{
\mathcal P_K(I)
:=
\operatorname{ParetoMin}
\{\Pi_K(\alpha):\alpha\in\mathcal M(I)\}.
}
\]

The candidate ideal node state is

\[
\boxed{
\mathfrak C_K(I)
:=
(\delta(I),\mathcal P_K(I)).
}
\]

Interpretation:

- `delta(I)` is a class/principalization cost;
- `P_K(I)` is the embedded typed geometry of the cheapest principal subideal witnesses.

## 5. Immediate theorem targets

### T10.1 — integrality and principality

Prove

\[
\delta(I)\in\mathbb Z_{\ge1},
\qquad
\delta(I)=1\iff I\text{ is principal}.
\]

### T10.2 — class interpretation

For invertible `I`, prove

\[
\boxed{
\delta(I)
=
\min\{N(J):J\subset O_K,\ [J]=[I]^{-1}\}.
}
\]

Indeed `(alpha)=IJ` with `J=(alpha)I^{-1}`.

### T10.3 — exact recovery of HATTER-SOL-09

If `I=(alpha)`, prove

\[
\mathcal M(I)=O_K^\times\alpha,
\]

and therefore, because `Pi_K` is unit-invariant,

\[
\boxed{
\mathcal P_K((\alpha))=\{\Pi_K(\alpha)\}.
}
\]

This is the required compatibility theorem.

### T10.4 — conjugation

Prove

\[
\delta(\bar I)=\delta(I)
\]

and, for the folded/conjugation-invariant interface law,

\[
\mathcal P_K(\bar I)=\mathcal P_K(I).
\]

## 6. First non-UFD laboratory

Use

\[
K=\mathbb Q(\sqrt{-5}),
\qquad
O_K=\mathbb Z[\sqrt{-5}],
\qquad
\Delta_K=-20.
\]

This is the classical first test because element factorization is nonunique and the class group is nontrivial.

Primary prime-ideal tests:

\[
\mathfrak p_2=(2,1+\sqrt{-5}),\qquad N(\mathfrak p_2)=2,
\]

\[
\mathfrak p_3=(3,1+\sqrt{-5}),\qquad N(\mathfrak p_3)=3.
\]

Expected minimal witnesses:

\[
\delta(\mathfrak p_2)=2,
\qquad
\mathcal M(\mathfrak p_2)=\{\pm2\},
\]

and

\[
\delta(\mathfrak p_3)=2,
\qquad
1+\sqrt{-5}\in\mathcal M(\mathfrak p_3).
\]

Under the discriminant-world capacity from HATTER-SOL-09 (`Delta=-20`, even class),

\[
\Pi(2)=(2,0),
\qquad
\Pi(1+\sqrt{-5})=(1,1).
\]

This should produce the first genuinely nonprincipal typed ideal nodes.

## 7. Prior-art boundary

The following are classical inputs and are **not** novelty claims:

- unique factorization of ideals in Dedekind domains;
- ideal lattices and Minkowski embeddings;
- the normalized norm form `N(x)/N(I)`;
- correspondence between imaginary quadratic ideal classes and positive definite binary quadratic forms;
- reduced ideals / least-norm representatives of ideal classes;
- shortest-vector and Euclidean-minimum questions for ideal lattices.

The candidate new layer is the composition

\[
\boxed{
\text{prime-ideal factorization}
\to
\text{minimal principalization witnesses}
\to
\text{typed ideal interface frontier}
\to
\text{HATTER-SOL network response}.
}
\]

## 8. Stop conditions before publication

Do not call HATTER-SOL-10 publication-ready until:

1. T10.1--T10.4 are proved cleanly;
2. `Q(sqrt(-5))` examples are fully audited;
3. at least one ideal-factor network exhibits information unavailable from norm alone;
4. the relation to reduced binary quadratic forms is stated without claiming that classical reduction is new;
5. hostile literature search finds no pre-existing identical arithmetic-network construction;
6. the network law for a set-valued ideal interface frontier is fixed and tested.
