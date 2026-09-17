# ROBUST_BOOLEAN_RECOVERY_FROM_GROUP_DISTANCE

**Branch:** `research/alice-ruler-edit-rigidity`  
**Status:** closed algebraic compatibility step, 2026-09-12  
**Depends on:** `PROJECTIVE_ASSOCIATOR_BRIDGE.md`  
**Purpose:** remove commutativity / exponent-2 / identity / order / STS-distance issues once any same-set group approximation is available at `o(n^2)` table distance.

---

## 1. Setup

Let `(L,\circ)` be the Steiner loop of an `STS(v)`, with

```math
n=|L|=v+1
```

and Steiner identity `0`. Thus

```math
x\circ0=x,
\qquad
x\circ x=0,
\qquad
x\circ(x\circ y)=y,
\qquad
x\circ y=y\circ x.
```

Suppose `*` is an arbitrary group operation on the **same set** `L`. Write

```math
t=d_H(\circ,*)
=|\{(x,y)\in L^2:x\circ y\ne x*y\}|.
```

No compatibility of the two identities is assumed.

The aim is to show that sufficiently small *normalized* group-table distance already forces the approximating group itself to be Boolean; the very strong absolute condition `t<n/2` used in `PROJECTIVE_DRAPAL_EDIT_RIGIDITY.md` is unnecessary for this algebraic step.

---

## 2. Bad rows control non-involutions

For `a\in L`, let

```math
Q_a(y)=a\circ y,
\qquad
P_a(y)=a*y,
```

and put

```math
r_a=d_H(P_a,Q_a).
```

Then

```math
\sum_{a\in L}r_a=t.
\tag{2.1}
```

The Steiner identity gives

```math
Q_a^2=\operatorname{id}_L
\tag{2.2}
```

for every `a`.

### Lemma 2.1

If `a*a` is not the group identity `e`, then

```math
r_a\ge \frac n2.
\tag{2.3}
```

### Proof

Hamming distance on permutations is invariant under left or right composition by a permutation. Therefore

```math
d_H(P_a^2,Q_a^2)
\le
d_H(P_a^2,P_aQ_a)+d_H(P_aQ_a,Q_a^2)
=2r_a.
\tag{2.4}
```

In the group,

```math
P_a^2(y)=(a*a)*y.
```

If `a*a\ne e`, left multiplication by `a*a` has no fixed points. Hence

```math
d_H(P_a^2,\operatorname{id}_L)=n.
```

Using (2.2) in (2.4) gives `n\le2r_a`, proving (2.3). `\square`

Let

```math
I=\{a\in L:a*a=e\}
```

be the set of group involutions, with the identity included. Lemma 2.1 and (2.1) imply

```math
|L\setminus I|\frac n2\le t,
```

hence

```math
\boxed{|I|\ge n-\frac{2t}{n}.}
\tag{2.5}
```

---

## 3. More than three quarters involutions forces a Boolean group

### Lemma 3.1

If a finite group `G` of order `n` has more than `3n/4` elements satisfying `x^2=e`, then `G` is an elementary abelian `2`-group.

### Proof

Let `I={x:x^2=e}` and assume `|I|>3n/4`.

Fix `x\in I`. Since left multiplication preserves cardinality,

```math
|I\cap xI|
\ge 2|I|-n
>\frac n2.
\tag{3.1}
```

For every `z\in I\cap xI`, write `z=xy` with `y\in I`. Since also `z\in I`,

```math
xy=z=z^{-1}=(xy)^{-1}=yx.
```

Thus `x` commutes with more than `n/2` elements. Its centralizer is a subgroup of order strictly larger than `n/2`, so it is the whole group. Hence every element of `I` is central.

Therefore the center contains more than `n/2` elements and, being a subgroup, must equal the whole group. So `G` is abelian. In an abelian group, `I` is a subgroup; since `|I|>n/2`, it follows that `I=G`. Thus every element has order dividing `2`, and `G` is elementary abelian. `\square`

Combining (2.5) with Lemma 3.1 gives the robust threshold.

### Theorem 3.2 (robust Boolean recovery)

If

```math
\boxed{t<\frac{n^2}{8},}
\tag{3.2}
```

then `(L,*)` is an elementary abelian `2`-group. In particular,

```math
\boxed{n=2^m}
\tag{3.3}
```

for some integer `m`.

### Proof

From (2.5) and (3.2),

```math
|I|>n-\frac n4=\frac{3n}{4}.
```

Apply Lemma 3.1. `\square`

This already settles **order rigidity** once a same-set group approximation has normalized Hamming error below `1/8`.

---

## 4. Aligning the group identity with the Steiner identity

The Boolean group identity `e` need not equal the Steiner identity `0`. This costs only `O(n)` table cells.

If `e=0`, do nothing. Otherwise let `\pi` be the transposition of `e` and `0`, fixing every other point, and transport the group law by

```math
x\star y
:=
\pi\bigl(\pi^{-1}(x)*\pi^{-1}(y)\bigr).
\tag{4.1}
```

Then `(L,\star)` is isomorphic to `(L,*)`, hence is still elementary abelian `2`, and its identity is exactly `0`.

### Lemma 4.1

```math
d_H(*,\star)\le6n.
\tag{4.2}
```

### Proof

A cell `(x,y)` is certainly unchanged whenever

```math
x,y\notin\{0,e\}
```

and

```math
x*y\notin\{0,e\}.
```

Thus possible changed cells lie in the union of:

- two rows: at most `2n` cells;
- two columns: at most `2n` cells;
- cells whose `*`-output is `0` or `e`: exactly `2n` cells because each group-table symbol occurs once per row.

The union has size at most `6n`. `\square`

Consequently

```math
d_H(\circ,\star)\le t+6n.
\tag{4.3}
```

---

## 5. Exact conversion to Steiner block distance

Let `X=L\setminus\{0\}`. Since `\star` is Boolean with identity `0`, its nonzero elements define the projective STS `T` with blocks

```math
\{x,y,x\star y\}
```

for distinct nonzero `x,y`.

Both `\circ` and `\star` have identity `0`, exponent `2`, and are commutative. Hence they agree on all cells involving `0` and all diagonal cells. If

```math
t_0=d_H(\circ,\star),
```

then all mismatches occur on ordered pairs of distinct points of `X` and come in symmetric pairs.

Let

```math
m=|\mathcal B(S)\setminus\mathcal B(T)|.
```

Each missing STS block contributes exactly its three unordered pairs, hence six ordered table cells, and distinct STS blocks have disjoint pair sets. Therefore

```math
t_0=6m.
\tag{5.1}
```

Since

```math
b(v)=\frac{v(v-1)}6
```

and the branch normalization is

```math
d_{blk}(S,T)
=\frac{|\mathcal B(S)\triangle\mathcal B(T)|}{2b(v)}
=\frac{m}{b(v)},
```

we obtain the exact identity

```math
\boxed{
d_{blk}(S,T)=\frac{t_0}{v(v-1)}
=\frac{t_0}{(n-1)(n-2)}.
}
\tag{5.2}
```

Together with (4.3):

```math
\boxed{
d_{blk}(S,T)
\le
\frac{t+6n}{(n-1)(n-2)}.
}
\tag{5.3}
```

---

## 6. Uniform transfer theorem

### Theorem 6.1

Let `S` be an `STS(v)`, let `L` be its Steiner loop of order `n=v+1`, and suppose there exists **some group law on the same set** at Hamming distance `t` from the Steiner-loop table. If

```math
t<n^2/8,
```

then:

1. `n` is a power of `2`;
2. after changing the group labeling in at most `6n` table cells, the group identity is `0` and the group is Boolean;
3. there is a projective `STS(v)` on the same point set with

```math
\boxed{
d_{blk}(S,T)
\le
\frac{t+6n}{(n-1)(n-2)}.
}
```

In normalized notation `\eta=t/n^2`,

```math
d_{blk}(S,T)
\le
\eta\frac{n^2}{(n-1)(n-2)}
+
\frac{6n}{(n-1)(n-2)}.
\tag{6.1}
```

Thus any same-set group stability statement

```math
\eta\le f(\delta),
\qquad f(\delta)\to0,
```

for associativity-failure density `\delta=s/n^3` automatically yields projective STS edit rigidity, with no further algebraic obstruction:

```math
d_{blk}(S,\mathcal P_v)
\le f(\delta)+o_{n\to\infty}(1).
```

Moreover, once `f(\delta)<1/8`, the order is forced **exactly**:

```math
v+1=2^m.
```

---

## 7. What this closes

The projective reconstruction problem no longer needs separate future arguments for:

- recovering commutativity;
- recovering exponent `2`;
- forcing the projective order spectrum;
- aligning the group identity with the added Steiner-loop point;
- converting multiplication-table distance to STS block edit distance.

All five issues are discharged by Theorem 6.1.

The **only remaining uniform projective bottleneck** is now the analytic/combinatorial stability implication

```math
\frac{s}{n^3}\to0
\quad\Longrightarrow\quad
\frac{t}{n^2}\to0
```

for a Steiner loop (or, more generally, for a quasigroup), where `t` is distance to a group law on the same underlying set.

The published Gowers–Long paper reports such a qualitative '99% case' due to Elad Levi, but its cited source is a master's thesis/private communication. Until an accessible proof is verified or an in-house proof is completed, that implication remains open **for publication purposes** in this branch.
