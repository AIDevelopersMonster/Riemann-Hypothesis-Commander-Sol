# HATTER-SOL-09 — Canonical capacity for general discriminant worlds

Status: closed extension of the scalar/two-interface capacity to every imaginary quadratic discriminant.

Let

\[
F_\Delta=(b+\sqrt\Delta)/2,
\qquad b\in\{0,1\},
\]

with

\[
F_\Delta^2-bF_\Delta+q=0,
\qquad q=(b^2+|\Delta|)/4.
\]

Write

\[
\alpha=L+WF_\Delta.
\]

## 1. Symmetric additive step set

Define

\[
\boxed{
S_\Delta=\{\pm1,\pm F_\Delta,\pm\bar F_\Delta\}.
}
\]

Because

\[
\bar F_\Delta=b-F_\Delta,
\]

the set is invariant under sign and conjugation. It generates the additive lattice.

Define the world word-capacity

\[
\boxed{
\rho_\Delta(\alpha)
=\text{word distance from }0\text{ to }\alpha\text{ using }S_\Delta.
}
\]

Then

\[
\rho_\Delta(-\alpha)=\rho_\Delta(\alpha),
\qquad
\rho_\Delta(\bar\alpha)=\rho_\Delta(\alpha),
\]

and for every rational integer `m`,

\[
\boxed{\rho_\Delta(m)=|m|.}
\]

Thus the HATTER-SOL-07 scalar capacity is recovered exactly on the rational line for every discriminant world.

## 2. Even discriminant class: b=0

Here

\[
\bar F=-F.
\]

The distinct step directions are `±1,±F`, so

\[
\boxed{\rho_\Delta(L+WF)=|L|+|W|.}
\]

A canonical sign/conjugation-invariant typed capacity is

\[
\boxed{\Pi_\Delta(\alpha)=(|L|,|W|).}
\]

The two entries are labelled axial/transverse capacities; for generic `q>1` they should not be sorted because the two geometric directions have different lengths.

At the exceptional Gaussian world `Delta=-4`, `q=1` and multiplication by `i` exchanges the directions. Quotienting by this extra unit symmetry gives the earlier folded pair

\[
(\max(|L|,|W|),\min(|L|,|W|)).
\]

## 3. Odd discriminant class: b=1

Now

\[
\bar F=1-F.
\]

In coefficient coordinates the three positive step directions are

\[
(1,0),\quad(0,1),\quad(1,-1).
\]

Therefore

\[
\boxed{
\rho_\Delta(L+WF)
=
\max\{|L|,|W|,|L+W|\}.
}
\]

The largest of the three absolute values equals the sum of the other two. Let the three values be sorted as

\[
0\le Q\le P\le R.
\]

Then `R=P+Q`, so define

\[
\boxed{\Pi_\Delta(\alpha)=(P,Q)}
\]

and

\[
\boxed{\rho_\Delta=P+Q.}
\]

This pair is invariant under sign and conjugation because these operations permute the absolute-value triple.

At `Delta=-3`, the extra Eisenstein units enlarge the symmetry, and this construction reduces exactly to the earlier triangular folded pair.

## 4. Norm remains world-dependent

The additive capacity law depends only on the parity class `b`, but the multiplicative norm retains the discriminant parameter:

\[
\boxed{
N_\Delta(L,W)=L^2+bLW+qW^2.
}
\]

Thus two worlds can assign the same additive interface capacity to a coordinate state while giving it different multiplicative norm and therefore different arithmetic factorization behavior.

This separation is desirable:

- `Pi_Delta` describes additive/network interface resources;
- `N_Delta` and the factorization law describe the arithmetic world.

## 5. Recovery of the old worlds

For `Delta=-4`,

\[
q=1,
\qquad
N=L^2+W^2,
\qquad
\rho=|L|+|W|,
\]

which is the Gaussian model.

For `Delta=-3`,

\[
q=1,
\qquad
N=L^2+LW+W^2,
\]

and the three-direction word metric gives the Eisenstein model.

Hence the discriminant extension preserves both previous worlds exactly.

## 6. Consequence for the future world operator

We now have an infinite indexed family

\[
\Delta<0
\longmapsto
\bigl(N_\Delta,\Pi_\Delta,\rho_\Delta\bigr).
\]

The next missing structure is not a capacity law but **adjacency between discriminant worlds**. It must be arithmetic/canonical, not imposed by numerical closeness of discriminants. Candidate routes to audit next are inclusion/conductor maps between quadratic orders and prime-labelled splitting transitions.