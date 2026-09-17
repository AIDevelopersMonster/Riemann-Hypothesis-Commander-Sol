# HATTER-SOL-15 · Frobenius Marking and Observer Boundary

**Status:** exact claim-boundary / structural theorem note

Let `L/Q` be a finite Galois extension with

\[
G\cong D_{2p},
\qquad p\text{ odd},
\]

and let

\[
D=\langle s\rangle,
\qquad
K=L^D.
\]

Consider an unramified rational prime `q` whose Frobenius conjugacy class is the reflection class.

## 1. What the rational prime canonically determines

The rational prime `q` determines only the conjugacy class

\[
\operatorname{Frob}_q\subset G,
\]

not a distinguished element of that class.

For odd `p`, all `p` reflections

\[
r^j s,\qquad j\in\mathbb F_p,
\]

form one conjugacy class. Therefore the unmarked arithmetic world attached to `q` canonically determines the reflection cycle type on `D\backslash G`, namely

\[
\boxed{1\,2^{(p-1)/2}},
\]

and hence the factorization type in the degree-`p` field `K`:

\[
q\mathcal O_K
=
\mathfrak q_0\mathfrak q_1\cdots\mathfrak q_{(p-1)/2},
\]

with one residue-degree-one prime and `(p-1)/2` residue-degree-two primes.

This splitting type is conjugacy-invariant.

## 2. What requires a marking

Choose a prime `P` of `L` above `q`. Then a definite Frobenius element

\[
\operatorname{Frob}_{P/q}\in G
\]

is specified. Replacing `P` by `gP` conjugates the Frobenius element by `g`.

Thus identifying a particular reflection

\[
r^j s
\]

requires the choice of a prime above `q` (equivalently, a compatible Galois marking).

The two-port sector address associated with the reflection index `j` is therefore a **marked** invariant, not an invariant of the rational prime alone.

## 3. World/observer separation

This gives a sharp hierarchy:

\[
\boxed{
\text{unmarked rational-prime world}
\to
\text{reflection conjugacy class / splitting type}
}
\]

while

\[
\boxed{
\text{marked Galois world }(q,P)
\to
\text{specific reflection }r^j s
\to
\text{specific fixed sector}.
}
\]

The unmarked world remembers **that there is exactly one degree-one branch**. The marked observer can remember **which Schreier sector realizes it**.

## 4. Theorem H15.8 — marking is exactly the missing sector data

For a reflection prime `q`, all choices of `P|q` give conjugate reflection Frobenius elements and hence isomorphic unmarked splitting data in `K`. However, after fixing the Schreier marking of `D\backslash G`, different reflection representatives select different unique fixed sectors.

Therefore the sector identity is not intrinsic to the rational prime; it is data of the pair

\[
\boxed{(\text{arithmetic world},\text{Galois marking}).}
\]

## 5. Programme consequence

This is the non-abelian analogue of the H14 fixed-action qualification. H14 showed that the abstract graph forgets which arithmetic regular action is marked. H15 shows that a rational prime forgets which representative of a non-abelian Frobenius conjugacy class is marked.

Thus the HATTER forgetful ladder now contains two distinct losses:

\[
\text{marked Frobenius element}
\longrightarrow
\text{Frobenius conjugacy class}
\longrightarrow
\text{splitting type / Euler factor}.
\]

Future observer claims must specify at which level they operate.