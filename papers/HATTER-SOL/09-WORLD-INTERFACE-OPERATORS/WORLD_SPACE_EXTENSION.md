# HATTER-SOL-09 — From two exceptional worlds to a discriminant family

Status: structural extension; no world Laplacian yet.

## 1. Unit-only rigidity

If virtual directions are required to be multiplicative units of an imaginary quadratic integer ring, only two nondegenerate two-dimensional cases exist:

- Gaussian world `Z[i]`, with units `±1,±i`;
- Eisenstein world `Z[omega]`, with six units.

Every other imaginary quadratic field has only units `±1`.

Therefore the unit-step rule produces only two genuinely 2D worlds and is too rigid for a nontrivial world space.

## 2. Minimal canonical extension

Let `Delta<0` be an imaginary quadratic discriminant and put

\[
b_\Delta=
\begin{cases}
0,&\Delta\equiv0\pmod4,\\
1,&\Delta\equiv1\pmod4,
\end{cases}
\]

\[
\boxed{F_\Delta:=\frac{b_\Delta+\sqrt\Delta}{2}}.
\]

Then the quadratic order is generated additively by `1` and `F_Delta`.

Among algebraic integers not lying on the rational line, `F_Delta` is a shortest transverse lattice vector up to sign, conjugation and addition of an integer: any element `m+nF_Delta` independent of `1` has `n!=0`, hence imaginary part of magnitude at least `sqrt(|Delta|)/2`, attained when `|n|=1`; the integer `m` is then chosen to minimize the real part.

Thus `F_Delta` is the canonical second-direction orbit determined by the discriminant.

## 3. General world law

Define

\[
q_\Delta:=\frac{b_\Delta^2+|\Delta|}{4}.
\]

Then

\[
\boxed{F_\Delta^2-b_\Delta F_\Delta+q_\Delta=0.}
\]

For a two-channel state

\[
\alpha=L+WF_\Delta,
\]

the regular block is

\[
\boxed{
M_\Delta(L,W)=
\begin{pmatrix}
L&-q_\Delta W\\
W&L+b_\Delta W
\end{pmatrix}.
}
\]

Its determinant is the quadratic norm

\[
\boxed{
N_\Delta(L,W)=L^2+b_\Delta LW+q_\Delta W^2.
}
\]

The old worlds are exactly the two cases with `q_Delta=1`:

- `Delta=-4`: `b=0,q=1`, so `F=i` and `N=L^2+W^2`;
- `Delta=-3`: `b=1,q=1`, so `F=(1+sqrt(-3))/2` and `N=L^2+LW+W^2`.

Hence Gaussian and Eisenstein are not discarded: they are the maximally symmetric first members of the discriminant family.

## 4. New world parameter

A quadratic world is now encoded by

\[
\boxed{W_\Delta=(b_\Delta,q_\Delta)}
\]

or equivalently by its discriminant

\[
\boxed{\Delta=b_\Delta^2-4q_\Delta<0.}
\]

Changing world changes the quadratic law while retaining the same two-channel module form `L+WF_Delta`.

This gives an infinite candidate world space indexed by negative discriminants.

## 5. Important unresolved point

For `q_Delta>1`, the second direction `F_Delta` is no longer a multiplicative unit. Therefore the old unit-word capacity `rho` and the folded pair `(P,Q)` do not extend automatically.

The next task is to define a canonical nonnegative two-interface capacity for general `Delta` that:

1. reduces to the existing Gaussian/Eisenstein `(P,Q)` in `Delta=-4,-3`;
2. is invariant under sign and conjugation;
3. recovers integer capacity `m` on the rational line;
4. interacts naturally with the norm `N_Delta` and factorization.

No world adjacency or Laplacian should be defined before this extension is solved.