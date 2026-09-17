# FCOA Hybrid Memory — Synergy Classes

**Status:** internal research checkpoint; shared-output mechanism discovered; not upstreamed.

## 1. Two layers of hybrid symmetry

For independently typed output sorts, carrier actions are enough:

\[
\pi_X\operatorname{Aut}(\oplus,\otimes)
=
\pi_X\operatorname{Aut}(\oplus)
\cap
\pi_X\operatorname{Aut}(\otimes).
\]

This is the **carrier-intersection regime**.

For a common anonymous output sort `O`, this is no longer sufficient. A carrier permutation may lie in both projected groups but require different output permutations in the two reducts. The joint automorphism exists only when the lifts are compatible.

Thus the correct general object is the fiber product of the two automorphism groups over their common actions on `X` and `O`, not merely the intersection of carrier projections.

## 2. DD — domain-domain synergy

Both operations can be constant-valued. Joint rigidity is caused solely by incompatible definedness geometries. Minimal active carrier is `3`, and minimum cell cost is `1+1=2`.

## 3. DV-I — domain-value synergy with independent outputs

One operation contributes domain geometry; the other has a definedness automorphism group strictly larger than its full valued automorphism group.

The value-bearing operation needs at least three cells because no partition of at most two cells can reduce its domain automorphism group. Hence the sharp minimum is

\[
1+3=4.
\]

## 4. VV-I — value-value synergy with independent outputs

Both operations contribute genuinely value-sensitive partitions. Each therefore needs at least three cells. The sharp minimum is

\[
3+3=6.
\]

## 5. JFS — Joint Fiber Synchronization on a shared output sort

This is the new mechanism found by attacking DV/VV minimality without clean-template restrictions.

Let

\[
X=\{a,b,c\},\qquad O=\{u,v\}.
\]

Define

\[
a\oplus a=u,
\]

\[
b\otimes b=u,
\qquad
c\otimes c=v.
\]

The nontrivial carrier transposition

\[
r=(b\ c)
\]

survives in both reducts. In `\oplus`, however, it forces `u` to stay fixed; in `\otimes`, it forces `u\leftrightarrow v`.

Hence

\[
\pi_X\operatorname{Aut}(\oplus)
=
\pi_X\operatorname{Aut}(\otimes)
=\langle r\rangle\cong C_2,
\]

but

\[
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

This is not transverse carrier symmetry. It is **incompatible lifting of the same carrier symmetry to shared anonymous outputs**.

### Erasure signature

The joint definedness reduct retains `r`. Erasing either operation's value layer restores `r`. Thus the rigidity is genuinely caused by cross-operation output equality.

### Minimality

With at most two total tagged cells, the global equality partition of values is automatically invariant under every tagged-cell permutation. Therefore no shared-output value effect exists below three total cells.

The `1+2` construction is sharp.

## 6. Complete three-cell classification

For `|X|=3`, exactly three total cells, nonrigid individual reducts, nonrigid joint definedness, and rigid joint valued structure, every witness is isomorphic to one of eight classes with operation symbols distinguished.

Up to relabeling `X`, the one-cell operation has loop `(a,a)`, residual transposition `(b c)`, and the two-cell operation domain is one of the four two-element orbits:

\[
\{(a,b),(a,c)\},
\quad
\{(b,a),(c,a)\},
\quad
\{(b,b),(c,c)\},
\quad
\{(b,c),(c,b)\}.
\]

The value partition must identify the one-cell operation's output with exactly one member of the two-cell orbit. Exchanging the operation symbols gives four further classes.

Exhaustive search yields `48` labeled witnesses and `8` isomorphism classes.

## 7. Revised mechanism map

The branch now has two qualitatively different symmetry-killing architectures:

### A. Transverse carrier stabilizers

\[
H_\oplus\cap H_\otimes=1.
\]

This contains DD, DV-I and VV-I.

### B. Incompatible lift synchronization

\[
H_\oplus\cap H_\otimes\ne1,
\]

but no common lift of a surviving carrier permutation exists on the shared output sort.

JFS is the minimal example.

## 8. Structural lesson

The earlier slogan

\[
\text{Hybrid memory}\sim
\operatorname{Aut}(\oplus)\cap\operatorname{Aut}(\otimes)
\]

is correct only when output actions are independently typed or otherwise decoupled.

The more general invariant is the **compatibility of automorphism lifts** across all shared sorts.

A useful categorical/group-theoretic formulation is:

\[
\boxed{
\operatorname{Aut}(\oplus,\otimes)
\text{ is a compatibility/fiber-product subgroup of the reduct automorphism groups.}
}
\]

The precise abstract formulation should be hostile-audited before theorem naming or upstream use.
