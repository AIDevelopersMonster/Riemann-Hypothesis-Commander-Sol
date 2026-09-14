# HATTER-SOL-14 · Two-Filter Hecke Bridge

**Status:** future-transition seed.

## 1. Trivial filter regime

If two filters are diagonal in the same basis, they commute. This models the ordinary red/green-glass intuition:

\[
F_R F_G=F_G F_R.
\]

If their supports are disjoint, the product may even vanish. This is selector/enable behavior and carries no path-order memory.

## 2. Noncommuting projector regime

Let `rho:G->GL(V)` be a finite-dimensional representation. For involutive port actions `a^2=b^2=1`, define

\[
P_a=\frac{I+\rho(a)}2,
\qquad
P_b=\frac{I+\rho(b)}2.
\]

Then `P_a` and `P_b` are idempotent filters. Their commutator is

\[
\boxed{
[P_a,P_b]
=\frac14\bigl(\rho(ab)-\rho(ba)\bigr).
}
\]

Hence if the two port actions fail to commute in the represented action, the order of filtering is observable: there exists a state `v` with

\[
P_aP_bv\ne P_bP_av.
\]

This is the nontrivial classical version of the two-colour-filter analogy.

## 3. Sector filters from a decomposition subgroup

Let `D<=G` be a decomposition subgroup and let

\[
e_D=\frac1{|D|}\sum_{d\in D}\rho(d).
\]

In a unitary realization this is the projector onto the `D`-invariant subspace. A remote sector represented by `g` carries the conjugated projector

\[
P_{gDg^{-1}}
=\rho(g)e_D\rho(g)^{-1}.
\]

Thus local visibility filters can be tied to globally separated sectors through conjugated stabilizers.

## 4. Hecke operators as canonical port filters

Compress transport through a sector by

\[
T_g=e_D\rho(g)e_D.
\]

These operators depend only on the double coset `DgD` and span the Hecke algebra

\[
\mathcal H(G,D)\cong e_D\,\mathbb C[G]\,e_D.
\]

The pair `(G,D)` is a finite Gelfand pair exactly when this Hecke algebra is commutative. Therefore:

\[
\boxed{
\mathcal H(G,D)\text{ noncommutative}
\iff
\exists\text{ two sector filters }T_A,T_B\text{ with }T_AT_B\ne T_BT_A.
}
\]

This gives a sharper transition criterion than merely asking whether `G` is nonabelian: some nonabelian pairs still have a commutative filtered-sector algebra.

## 5. Programme interpretation

The correct hierarchy suggested by the colour-filter intuition is

\[
\text{commuting selectors}
<
\text{noncommuting port projectors}
<
\text{noncommutative Hecke/sector-filter algebra}.
\]

A promising next question is therefore:

> Can a natural nonabelian Galois family produce decomposition pairs `(G,D)` whose Hecke algebra is noncommutative, so that two local sector filters have genuinely order-dependent outputs?

This would turn the informal red/green-glass picture into a precise classical filter model with path-order memory.