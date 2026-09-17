# HATTER-SOL-14 · GALOIS-EQUIVARIANT CARRIERS

**Working title:** *Galois-Equivariant Carriers: Arithmetic Symmetry and the Topological Cost of Structural Erasure*  
**Branch:** `research/hatter-sol-galois-equivariant-carriers`  
**Parent:** HATTER-SOL-13 v1.1  
**Status:** active research

## 1. Motivation

HATTER-SOL-13 proved that, for the fixed rational prime `2` in the cyclotomic worlds

\[
K_k=\mathbb Q(\zeta_{2^k-1}),
\]

the prime-ideal support grows without bound and that arbitrary connected simple carriers exhibit a quantified topological erasure law. In particular, if

\[
n_k=\frac{\varphi(2^k-1)}{k},
\]

then fixed-fraction port-budget exhaustion has minimum orientable genus

\[
\gamma_k(\eta)=\Theta(n_k k)
\]

for every fixed `0<eta<=1`.

The main remaining weakness is that H13 allowed the carrier graph to be chosen arbitrarily on the set of primes above `2`.

H14 removes that freedom.

## 2. Canonical arithmetic vertex set

Let

\[
G_k:=\operatorname{Gal}(K_k/\mathbb Q)
\cong
(\mathbb Z/(2^k-1)\mathbb Z)^\times.
\]

For a prime ideal above `2`, its decomposition group has order equal to the residue degree, hence

\[
D_k=\langle 2\rangle\le G_k,
\qquad |D_k|=k.
\]

Because `G_k` is abelian, `D_k` is normal. The set of prime ideals above `2` is naturally identified with the quotient

\[
X_k=G_k/D_k.
\]

Thus

\[
|X_k|=n_k.
\]

The quotient group

\[
\Gamma_k:=G_k/D_k
\]

acts regularly on `X_k`.

This gives a canonical symmetry group on the H13 carrier vertices.

## 3. Equivariance requirement

A carrier graph `C_k` on `X_k` is called **Galois-equivariant** if

\[
\{x,y\}\in E(C_k)
\quad\Longleftrightarrow\quad
\{\sigma x,\sigma y\}\in E(C_k)
\]

for every `sigma in Gamma_k`.

Since the action is regular, every simple undirected equivariant carrier is expected to be a Cayley graph

\[
\operatorname{Cay}(\Gamma_k,S),
\]

where

\[
S=S^{-1},
\qquad 1\notin S.
\]

The first theorem obligation is to prove this reduction exactly in the present setting, including the connectedness criterion

\[
\langle S\rangle=\Gamma_k.
\]

## 4. Equivariant boundary law

Under the H13 residue-degree port model, every vertex has capacity `k`.

If

\[
C_k=\operatorname{Cay}(\Gamma_k,S),
\qquad d=|S|,
\]

then the carrier is `d`-regular and therefore

\[
\boxed{
B_f(C_k)=n_k(k-d).
}
\]

Hence the unrestricted H13 spectrum collapses to the degree values that can occur for inverse-closed generating sets of `Gamma_k`.

Define the equivariant spectrum

\[
\mathcal B_k^{\mathrm{Gal}}
=
\{n_k(k-|S|):
S=S^{-1},\ 1\notin S,\ \langle S\rangle=\Gamma_k,\ |S|\le k\}.
\]

A principal H14 goal is to characterize this set or obtain nontrivial bounds on it from the group structure of `Gamma_k`.

## 5. Complete exhaustion problem

In the equivariant class,

\[
B_f=0
\]

is possible only if there exists an inverse-closed generating set

\[
S\subseteq\Gamma_k
\]

with

\[
\boxed{|S|=k.}
\]

Thus complete port-budget exhaustion becomes a finite abelian group problem.

### Primary target H14-A

Determine whether there are infinitely many `k` for which no such generating set exists.

A positive result would imply:

\[
\boxed{
\text{arithmetic symmetry forbids complete exhaustion even when unrestricted H13 carriers allow it.}
}
\]

This would be a genuine new barrier beyond genus alone.

## 6. Equivariant topological cost

Define

\[
\gamma_k^{\mathrm{Gal}}(\eta)
=
\min\left\{
\gamma(\operatorname{Cay}(\Gamma_k,S)):
\frac{B_f}{n_k k}\le1-\eta
\right\},
\]

where the minimum is over connected simple Galois-equivariant carriers and `gamma` is orientable genus.

Compare with the unrestricted H13 law

\[
\gamma_k(\eta)=\Theta(n_k k).
\]

### Primary target H14-B

Prove one of the following, in descending order of strength:

1. `gamma_k^Gal(eta)=infinity` for some fixed `eta` and infinitely many `k`;
2. `gamma_k^Gal(eta) / gamma_k(eta) -> infinity` along a subsequence;
3. a nontrivial multiplicative or additive gap between equivariant and unrestricted topological cost;
4. if none of these holds, classify exactly why symmetry does not add asymptotic cost.

## 7. First group-theoretic invariants to test

For the finite abelian group `Gamma_k`, investigate:

- rank / minimal number of generators `d(Gamma_k)`;
- 2-torsion and involutions;
- parity restrictions on inverse-closed generating sets;
- possible cardinalities of inverse-closed generating sets;
- exponent and invariant-factor decomposition;
- whether exact cardinality `k` can always be achieved once one generating set exists;
- effect of requiring the Cayley graph to be connected and simple simultaneously.

A likely first obstruction is parity: non-involutory elements enter inverse-closed sets in pairs, while involutions contribute singly.

## 8. Homological refinement

If boundary/genus alone does not retain enough arithmetic structure, refine the carrier state by homology.

For a Galois-equivariant carrier `C_k`, study

\[
H_1(C_k,\mathbb Z)
\]

together with the induced action

\[
\Gamma_k\curvearrowright H_1(C_k,\mathbb Z).
\]

The resulting object is a `Z[Gamma_k]`-module, not just an integer Betti number.

### Primary target H14-C

Find two Galois-equivariant carriers with the same scalar data

\[
n_k,\ d,\ B_f,\ \gamma
\]

but non-isomorphic `Gamma_k`-module structures on `H_1`.

If possible, this yields the strict hierarchy

\[
\boxed{
\text{boundary memory}
<
\text{topological memory}
<
\text{equivariant homological memory}.
}
\]

## 9. Claim discipline

H14 must distinguish carefully between:

1. canonical arithmetic data (`G_k`, `D_k`, `Gamma_k`, prime-ideal orbit);
2. the mathematically defined equivariant carrier class;
3. model-dependent port interpretation;
4. topological or homological response.

Do not claim Shannon information, cryptographic hardness, or physical memory without a separate theorem.

Do not claim that every natural carrier must be Cayley until the equivariance-to-Cayley reduction is formally proved.

## 10. Immediate attack order

1. Prove the exact equivariance-to-Cayley classification for the regular `Gamma_k` action.
2. Prove the boundary formula `B_f=n_k(k-|S|)`.
3. Compute `Gamma_k` for small `k` and tabulate feasible inverse-closed generating-set sizes.
4. Search first for an exact-cardinality obstruction to `|S|=k`.
5. If complete-exhaustion obstruction fails, attack `gamma_k^Gal(eta)` versus unrestricted `gamma_k(eta)`.
6. Only after the scalar equivariant theory is understood, move to the `Gamma_k`-module structure of `H_1`.

## 11. Publication threshold

H14 should not be prepared for publication merely for the Cayley reduction or the formula `B_f=n_k(k-d)`, since both are structurally straightforward once the model is fixed.

Publication threshold requires at least one genuinely nontrivial statement such as:

- infinitely many symmetry-forbidden exhaustion worlds;
- a provable asymptotic equivariant/unrestricted genus gap;
- a classification theorem for the equivariant boundary spectrum using arithmetic group structure;
- or a nontrivial equivariant homology theorem.
