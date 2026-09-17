# HATTER-SOL-11 · Tail-valence no-go theorem

Status: closed theorem layer.

This note resolves the search for a genuinely multi-branch local principalization tail in maximal imaginary quadratic orders. Such a tail does not exist: every ideal class has at most two least-norm integral representatives.

## 1. Tail valence

Let `K` be an imaginary quadratic field of fundamental discriminant `D<0`, with maximal order `O_K`. For an ideal class `c`, define

\[
\delta_K(c)=\min\{N(J): J\subset O_K,\ [J]=c^{-1}\},
\]

and the least-norm representative set

\[
\mathscr A_{\min}(c^{-1})
=\{J\subset O_K:[J]=c^{-1},\ N(J)=\delta_K(c)\}.
\]

Define the local tail valence

\[
\boxed{v_K(c)=|\mathscr A_{\min}(c^{-1})|.}
\]

By the HATTER-SOL-10 witness/least-norm-ideal bijection, `v_K(c)` is exactly the number of minimal principalization witness orbits for every ideal in class `c`.

---

## 2. Reduced-form dictionary

Let

\[
f_c=[a,b,d]
\]

be the unique reduced primitive positive-definite binary quadratic form of discriminant `D` corresponding to the class `c^{-1}` under the classical ideal/form correspondence.

Reduction theory gives:

1. the leading coefficient `a` is the smallest positive integer primitively represented by the class;
2. therefore
   \[
   \boxed{\delta_K(c)=a;}
   \]
3. an integral ideal of norm `a` in the class corresponds to a primitive representation of `a` by `f_c`, modulo the unit automorphisms of the corresponding ideal lattice.

For a reduced positive-definite form

\[
f(x,y)=ax^2+bxy+dy^2,
\qquad |b|\le a\le d,
\]

the minimum value `a` can occur only along shortest primitive lattice directions.

If `a<d`, the only primitive minimum vectors are

\[
(\pm1,0).
\]

If `a=d` and `0<b<a`, the primitive minimum vectors are

\[
(\pm1,0),\qquad(0,\pm1).
\]

The only additional high-symmetry minimum-vector cases in maximal imaginary quadratic orders are the square and hexagonal forms at `D=-4` and `D=-3`; their extra vectors are identified by the extra unit groups and still produce only the unit ideal of norm one.

---

## 3. Main theorem

### Theorem T11.13 — quadratic tail-valence bound

For every ideal class `c` in every imaginary quadratic field,

\[
\boxed{v_K(c)\le2.}
\]

More precisely, if the reduced form attached to `c^{-1}` is

\[
f_c=[a,b,d],
\]

then

\[
\boxed{
v_K(c)=
\begin{cases}
2,&a=d\text{ and }D\notin\{-3,-4\},\\
1,&\text{otherwise}.
\end{cases}}
\]

### Proof

Since `a=delta_K(c)`, every least-norm ideal in the class corresponds to a primitive representation of `a` by the unique reduced form `f_c`.

If `a<d`, reduction theory shows that `a` is represented only by the primitive vectors `(+-1,0)`. These two vectors differ by the unit `-1` and give the same integral ideal. Hence `v_K(c)=1`.

Now suppose `a=d`. For a fundamental discriminant outside `-3,-4`, the boundary cases `b=0` and `b=a` cannot occur: `b=0` would give `D=-4a^2`, fundamental only when `a=1,D=-4`; `b=a` would give `D=-3a^2`, fundamental only when `a=1,D=-3`. Therefore

\[
0<b<a.
\]

The minimum `a` is then represented by exactly the two undirected primitive directions

\[
[(1,0)],\qquad[(0,1)].
\]

They give the two norm-`a` ideals

\[
J_+=\left(a,\frac{-b+\sqrt D}{2}\right),
\qquad
J_-=\left(a,\frac{b+\sqrt D}{2}\right).
\]

These ideals are distinct. Equality would force `b congruent -b mod 2a`, hence `a` divides `b`, contradicting `0<b<a`.

Thus `v_K(c)=2`.

For `D=-4` and `D=-3`, the unique reduced principal form has extra minimum vectors because of square/hexagonal symmetry, but the corresponding norm-one ideals are all `O_K`; the extra vectors are related by nontrivial units. Hence `v_K(1)=1` there as well. QED.

---

## 4. Binary tails are exactly symmetric reduced forms

### Corollary T11.13a

A nontrivial ideal class has a binary local principalization tail if and only if its reduced form has equal outer coefficients:

\[
\boxed{v_K(c)=2\iff f_c=[a,b,a]\text{ with }0<b<a.}
\]

Thus the branching mechanism is a shortest-vector degeneracy of the reduced ideal lattice.

The examples already found fit this exactly:

\[
\Delta=-35:\quad [3,1,3],
\]

\[
\Delta=-84:\quad [5,4,5].
\]

---

## 5. Relation to 2-torsion

For

\[
f=[a,b,a],
\]

the inverse form is

\[
f^{-1}=[a,-b,a].
\]

The determinant-one quarter-turn transformation exchanges the outer coefficients and sends `f` to `f^{-1}`. Therefore the corresponding class satisfies

\[
\boxed{c=c^{-1},\qquad c^2=1.}
\]

### Corollary T11.13b

\[
\boxed{v_K(c)=2\Longrightarrow c\text{ is a nontrivial }2\text{-torsion class}.}
\]

The converse is false. In `Delta=-84`, the classes represented by

\[
[2,2,11]
\quad\text{and}\quad
[3,0,7]
\]

are also nontrivial order-two classes, but have tail valence `1`; only

\[
[5,4,5]
\]

has valence `2`.

Thus class-group order alone does not determine branching. The reduced-form geometry does.

---

## 6. Multi-branch no-go

### Theorem T11.14 — no local multi-branch tail in imaginary quadratic fields

There is no ideal class in a maximal imaginary quadratic order with

\[
\boxed{v_K(c)\ge3.}
\]

Therefore the local minimal-principalization tail alphabet is always either

\[
\boxed{\text{deterministic }(v=1)}
\]

or

\[
\boxed{\text{binary }(v=2).}
\]

Any apparent `3+` branching in a HATTER-SOL residue/network system must arise from composition of several nodes/classes, residue convolution, host optimization, or a later projection. It cannot originate from one ideal class having three or more least-norm companion ideals.

This closes the `v>2` search lane for imaginary quadratic fields.

---

## 7. Computational audit

A direct reduced-form enumeration over all fundamental discriminants

\[
-30000\le D<0
\]

was used as an audit of the theorem.

The scan covered:

- `9125` fundamental discriminants;
- `486191` reduced ideal classes;
- `1481` binary-tail classes with `a=d`;
- no class with predicted or directly observed tail valence above `2`.

The first binary-tail reduced forms encountered are

\[
[-15]:[2,1,2],
\quad
[-35]:[3,1,3],
\quad
[-55]:[4,3,4],
\quad
[-84]:[5,4,5],
\quad
[-91]:[5,3,5],
\]

followed by infinitely many further candidates of the same symmetric reduced-form type.

The computation is an audit, not the proof; T11.13 gives the exact theorem.

---

## 8. Consequence for the research programme

The failed search for `v>2` produces a sharper architecture than a positive example would have:

\[
\boxed{
\text{ideal class}
\longrightarrow
\text{reduced-form minimum geometry}
\longrightarrow
v\in\{1,2\}
\longrightarrow
\text{residue ladder under composition}.
}
\]

So HATTER-SOL-11 should no longer search for a local ternary tail inside imaginary quadratic fields.

The next structural target is instead:

1. classify how binary-tail classes compose inside the class group;
2. determine how many global residue sectors can arise from several binary nodes;
3. compare that global branching with direction-orbit fusion and with the ordinary HATTER network response;
4. identify whether the resulting global sector count carries information invisible to the folded `(P,Q)` response.