# UNIFORM_99_PERCENT_ATTACK

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** active proof attack; translation-code reduction closed, completion step open  
**Date:** 2026-09-12

## 1. Translation code

Let `(L,\circ)` be a Steiner loop of order `n`. For `x\in L` define

```math
T_x(z)=x\circ z.
```

Each `T_x` is an involution.

### Lemma 1.1 (maximal separation)
For `x\ne y`,

```math
d_H(T_x,T_y)=n.
```

### Proof
If `T_x(z)=T_y(z)` for some `z`, then `x\circ z=y\circ z`, hence `x=y` by quasigroup cancellation. Thus the two permutations disagree at every point. `\square`

So

```math
C:=\{T_x:x\in L\}\subset Sym(L)
```

is an `n`-word permutation code of minimum Hamming distance exactly `n`.

---

## 2. Associativity is nearest-codeword multiplication

For every `x,y,z`:

```math
(x\circ y)\circ z=T_{x\circ y}(z),
```

while

```math
x\circ(y\circ z)=T_xT_y(z).
```

Hence the associativity-defect count satisfies exactly

```math
\boxed{
s
=\sum_{x,y\in L} d_H(T_{x\circ y},T_xT_y).
}
\tag{2.1}
```

If

```math
e(x,y):=d_H(T_{x\circ y},T_xT_y)/n,
```

then

```math
\mathbb E_{x,y} e(x,y)=s/n^3=:\delta.
```

For a threshold `tau<1/2`, call `(x,y)` `tau`-good if

```math
d_H(T_{x\circ y},T_xT_y)<tau n.
```

Markov gives

```math
|B_tau|\le (\delta/\tau)n^2.
\tag{2.2}
```

Because codewords in `C` are pairwise distance `n`, whenever `tau<1/2`, `T_{x\circ y}` is the unique codeword within `tau n` of `T_xT_y`.

Thus on almost all pairs the original product is recovered uniquely by nearest-codeword decoding inside `Sym(n)`.

---

## 3. Four-good-pairs rigidity

### Lemma 3.1
Let `tau<1/4`. Suppose the four pairs

```math
(x,y),
(y,z),
(x\circ y,z),
(x,y\circ z)
```

are all `tau`-good. Then

```math
(x\circ y)\circ z=x\circ(y\circ z).
```

### Proof
Put

```math
u=(x\circ y)\circ z,
\qquad
w=x\circ(y\circ z).
```

Using left/right invariance of Hamming distance under permutation composition,

```math
d_H(T_u,T_xT_yT_z)
\le
d_H(T_u,T_{x\circ y}T_z)
 +d_H(T_{x\circ y}T_z,T_xT_yT_z)
<2tau n.
```

Similarly,

```math
d_H(T_w,T_xT_yT_z)<2tau n.
```

Therefore

```math
d_H(T_u,T_w)<4tau n<n.
```

By Lemma 1.1 distinct codewords have distance exactly `n`, hence `T_u=T_w` and therefore `u=w`. `\square`

This is a deterministic local rigidity statement: once the four relevant multiplication pairs are sufficiently well decoded in the translation code, associativity is forced exactly.

---

## 4. Consequence: dense partial exact group law

Delete the bad pair set `B_tau` from the multiplication table and retain the product `x\circ y` on the remaining pairs.

For `tau<1/4`, the retained partial Latin operation satisfies the associative law on every triple for which all four pairs required to form both sides are retained.

The deleted density is at most

```math
\delta/tau.
```

Thus the uniform 99% problem has been reduced to the following completion statement.

> **Dense associative partial-Latin completion problem.**  
> If a partial Latin operation on an `n`-set is defined on `(1-o(1))n^2` pairs and is associative whenever both sides are defined through retained pairs, must it agree on `(1-o(1))n^2` cells with a group table (preferably on the same set, or after an `o(n)` adjustment)?

A positive answer, combined with `ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE.md`, completes the projective branch.

---

## 5. Literature boundary

Gowers–Long (2020) prove strong structure from positive-density partial associativity, and explicitly report that Elad Levi proved the 99% case. However the cited Levi source is an M.A. thesis/private communication and an accessible proof has not been located.

The general Latin-square removal / repair statements that would trivially solve the completion step are still presented in the Latin-square limits literature as conjectural in their full generality. Therefore this branch must not silently invoke a generic Latin-square repair lemma.

The special partial law here is much more rigid than an arbitrary dense partial Latin square: it comes from a maximally separated involution code in `Sym(n)` and inherits Steiner commutativity and inverse identities. The next proof attack should exploit these additional constraints rather than appeal to an unresolved general repair conjecture.
