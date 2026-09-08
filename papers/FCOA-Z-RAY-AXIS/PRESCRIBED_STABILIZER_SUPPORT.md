# FCOA-Z — Prescribed-Stabilizer Support on Wreath Branch Groups

Status: theorem package v0.1  
Date: 2026-08-31

This note generalizes the exact seven-vertex branch-coherence calculation from

\[
D_8\longrightarrow V_4
\]

to a family of imprimitive branch groups.

The central resource is

\[
\boxed{
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\},}
\]

with value `infinity` if no such subset exists.

Unlike the classical base-size problem, this is a **setwise** support problem. Unlike ordinary distinguishing-number theory, the target stabilizer need not be trivial. Unlike the subgroup-relative distinguishing number `D_{Gamma,H}`, the present quantity asks for the stabilizer to be **exactly** `H` and minimizes the size of one support fiber rather than the number of labels.

The FCOA framework citation is:

A. Malachevsky, *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*, Zenodo, 2026, DOI `10.5281/zenodo.22164246`.

---

## 1. Orbit-union reduction

Let a finite group `G` act on a finite set `S`, and let `H<=G`.

### Theorem 1.1 — Orbit-Union Reduction

Every subset `F subset S` satisfying

\[
H\le \operatorname{Stab}_G(F)
\]

is a union of `H`-orbits on `S`.

Therefore

\[
\boxed{
m_G(H;S)
=
\min\left\{
\sum_{O\in\mathcal A}|O|:
\mathcal A\subseteq \operatorname{Orb}_H(S),\
\operatorname{Stab}_G\!\left(\bigcup_{O\in\mathcal A}O\right)=H
\right\}.}
\]

#### Proof

If `F` is stabilized setwise by `H`, then for every `x in F` the entire `H`-orbit `Hx` is contained in `F`. Hence `F` is a union of `H`-orbits. Conversely every union of `H`-orbits is stabilized by `H`; one then tests whether its full `G`-stabilizer is exactly `H`. Taking the minimum size gives the formula. □

This finite reduction is the prescribed-stabilizer analogue of passing from arbitrary subsets to orbit data.

---

## 2. Normal-subgroup quotient reduction

Assume now that

\[
H\unlhd G.
\]

Let

\[
Q=G/H.
\]

Because `H` is normal, `Q` acts on the set of `H`-orbits

\[
\Omega=H\backslash S.
\]

Give each orbit `O in Omega` weight

\[
w(O)=|O|.
\]

### Theorem 2.1 — Weighted Quotient Regular-Set Theorem

There is a weight-preserving correspondence between

- `H`-invariant subsets `F subset S`, and
- subsets `A subset Omega`.

Under this correspondence,

\[
\boxed{
\operatorname{Stab}_G(F)/H
\cong
\operatorname{Stab}_Q(A).
}
\]

Hence

\[
\boxed{
m_G(H;S)
=
\min\left\{
\sum_{O\in A}w(O):
A\subseteq\Omega,\
\operatorname{Stab}_Q(A)=1
\right\}.}
\]

#### Proof

An `H`-invariant subset is exactly a union of `H`-orbits, giving the correspondence. Since `H` is normal, any `g in G` permutes the `H`-orbits, and two elements of the same coset in `G/H` induce the same permutation on `Omega`. Thus `g` stabilizes the union `F` iff the coset `gH` stabilizes the corresponding subset `A`. The stabilizer quotient formula follows, and exact stabilizer `H` is equivalent to trivial setwise stabilizer in `Q`. □

This connects prescribed-stabilizer support to the classical theory of regular sets in power-set actions, but with nonuniform orbit weights.

---

## 3. Exact index-two formula

Suppose

\[
[G:H]=2.
\]

Then `H` is normal and `Q~=C_2`.

### Corollary 3.1 — Index-Two Support Formula

Let `q` be the nontrivial element of `Q`. Then

\[
\boxed{
m_G(H;S)
=
\min\{|O|:
O\in H\backslash S,\ qO\neq O\}.}
\]

#### Proof

A subset of `Omega` has trivial `C_2` stabilizer iff it is not fixed by `q`. Any such subset contains at least one orbit-point `O` moved by `q`, whose weight is at least the stated minimum. Conversely the singleton subset `{O}` has trivial `C_2` stabilizer whenever `qO != O`. □

For the seven-vertex coherence problem, the two four-cell directed matching fibers are the two `H`-orbits exchanged by the quotient involution, so

\[
m_{D_8}(V_4;O_\times)=4.
\]

The earlier brute-force result is therefore an instance of a general index-two theorem.

---

## 4. Wreath branch setup

Let `Lambda` be a set of size

\[
t\ge2,
\]

and let

\[
A\le \operatorname{Sym}(\Lambda)
\]

be 2-transitive.

Take `b>=2` isomorphic branches. The active imprimitive carrier is

\[
X=[b]\times\Lambda.
\]

Let

\[
G=A\wr S_b=A^b\rtimes S_b
\]

act in the natural imprimitive action. An element is written

\[
g=(\sigma_1,\ldots,\sigma_b;\pi),
\]

with `sigma_r in A` and `pi in S_b`.

Define the ordered cross-branch cell orbit

\[
S_\times=
\left\{
((r,i),(s,j)):
 r\neq s
\right\}.
\]

Its size is

\[
\boxed{|S_\times|=b(b-1)t^2.}
\]

Fix a coherence identification of the internal coordinates of all branches. Its equality fiber is

\[
F_=\ =
\left\{
((r,i),(s,i)):
 r\neq s
\right\}.
\]

Thus

\[
\boxed{|F_=|=b(b-1)t.}
\]

The complement inside `S_x` is

\[
F_\neq=S_\times\setminus F_=
\]

with

\[
|F_\neq|=b(b-1)t(t-1).
\]

---

## 5. Coherence stabilizer

Define the diagonal subgroup

\[
\Delta A=\{(\sigma,\ldots,\sigma):\sigma\in A\}\le A^b.
\]

Let

\[
H=\Delta A\times S_b
\]

inside the wreath product. The diagonal internal action commutes with permutation of branches, so this is naturally a direct product.

### Theorem 5.1 — Coherence Stabilizer Theorem

\[
\boxed{\operatorname{Stab}_G(F_=)=H.}
\]

#### Proof

Every element of `H` preserves equality of internal coordinates, so `H` stabilizes `F_=`.

Conversely let

\[
g=(\sigma_1,\ldots,\sigma_b;\pi)
\]

stabilize `F_=`. For every pair of distinct branches `r,s` and every `i in Lambda`, the cell

\[
((r,i),(s,i))
\]

must be sent to another equality cell. Therefore

\[
\sigma_r(i)=\sigma_s(i)
\]

for every `i`. Hence

\[
\sigma_r=\sigma_s.
\]

As `b>=2`, all internal permutations are equal. The branch permutation `pi` is arbitrary. Thus `g in Delta A x S_b`. □

### Corollary 5.2 — Number of coherence states

The `G`-orbit of the coherence relation has

\[
\boxed{[G:H]=|A|^{b-1}}
\]

distinct states.

Indeed

\[
|G|=|A|^b b!,
\qquad
|H|=|A| b!.
\]

So the semantic coherence information is

\[
\boxed{I_{\rm coh}=(b-1)\log_2|A|\ \text{bits}.}
\]

---

## 6. Exact prescribed support

Because `A` is 2-transitive and `S_b` is 2-transitive on ordered distinct branch pairs, `H` has exactly two orbits on `S_x`:

1. `F_=` — equal internal coordinates;
2. `F_neq` — unequal internal coordinates.

### Theorem 6.1 — Wreath Coherence Support Theorem

For every 2-transitive `A` of degree `t>=2` and every `b>=2`,

\[
\boxed{
m_G(H;S_\times)=b(b-1)t.}
\]

#### Proof

Any subset stabilized by `H` must be a union of `H`-orbits. Since there are only the two orbits `F_=` and `F_neq`, the only `H`-invariant subsets are

\[
\varnothing,
\quad F_=,
\quad F_\neq,
\quad S_\times.
\]

The empty set and full set have stabilizer `G`. By Theorem 5.1,

\[
\operatorname{Stab}_G(F_=)=H.
\]

The complement has the same setwise stabilizer:

\[
\operatorname{Stab}_G(F_\neq)=H.
\]

Therefore

\[
m_G(H;S_\times)=\min\{|F_=|,|F_\neq|\}.
\]

Since `t>=2`,

\[
t\le t(t-1),
\]

so the minimum is

\[
b(b-1)t.
\]

□

### Specialization to the seven-vertex carrier

Take

\[
A=S_2,
\qquad
b=2,
\qquad
t=2.
\]

Then

\[
G=S_2\wr S_2\cong D_8,
\]

\[
H=\Delta S_2\times S_2\cong V_4,
\]

and

\[
\boxed{m_G(H;S_\times)=2\cdot1\cdot2=4.}
\]

This recovers the exact four-cell matching support without enumerating subsets.

---

## 7. Domain cost

The full wreath group `G` is transitive on `S_x`: independent internal branch permutations can send any ordered cross-branch cell to any other, and `S_b` moves any ordered pair of distinct branches to any other.

### Proposition 7.1

If the operation domain is required to

1. lie inside `S_x`,
2. be nonempty, and
3. be connection-independent, equivalently `G`-invariant,

then the only possible domain is

\[
D=S_\times.
\]

Hence the exact natural-domain cost is

\[
\boxed{|D|=b(b-1)t^2.}
\]

For fixed `b`, the coherence fiber uses only a fraction

\[
\boxed{\frac{|F_=|}{|D|}=\frac1t}
\]

of the defined cross cells.

---

## 8. Two-output threshold

In a value-only compiler, one terminal output cannot reduce active symmetry beyond the fixed domain: with one output, all defined cells have the same value. This is the One-Output Collapse already established in the FCOA Value-Rigidity line.

Therefore two outputs are necessary whenever `H<G`.

With two distinguished outputs, color

\[
F_=
\]

by one value and

\[
F_\neq
\]

by the other. The active color-preserving group is exactly `H`.

Thus for named outputs the output-cardinality threshold is exactly

\[
\boxed{2.}
\]

---

## 9. Anonymous-output swap theorem

Now suppose the two terminal values are anonymous, so an operation automorphism may exchange them.

The active group becomes larger than `H` exactly when some

\[
g\in G
\]

sends

\[
F_=
\]

to

\[
F_\neq.
\]

### Theorem 9.1 — Unique Anonymous-Swap Exception

For the wreath coherence family above,

\[
\boxed{
\exists g\in G:\ gF_=F_\neq
\quad\Longleftrightarrow\quad
(b,t)=(2,2).
}
\]

#### Proof

Fix an ordered pair of distinct source branches. Its equality fiber contains exactly `t` cells. Under any wreath element, those `t` cells are sent into one ordered target branch pair.

But the unequal fiber inside one ordered branch pair contains

\[
t(t-1)
\]

cells. Therefore equality can map onto inequality only if

\[
t=t(t-1),
\]

which for `t>=2` forces

\[
t=2.
\]

Now `A` has degree two, hence `A=S_2`. Write each internal permutation as a bit: identity or transposition. Mapping equality to inequality requires the internal permutations attached to every two distinct branches to be opposite. With only two possible bits, this can hold for every pair of distinct branches iff

\[
b=2.
\]

Conversely, for `b=t=2`, choose identity on one branch and the transposition on the other; this sends equal-coordinate cross cells to unequal-coordinate cross cells. □

### Corollary 9.2

Except for

\[
\boxed{(b,t)=(2,2),}
\]

two anonymous terminal outputs already recover the exact coherence stabilizer `H` on the natural cross domain with no extra anchor.

The seven-vertex binary carrier is therefore an exceptional balanced case, not the generic behavior.

---

## 10. The exceptional anchor

For `(b,t)=(2,2)`, the two fibers have equal size `4+4`, and an outer wreath element exchanges them. An anti-swap anchor is necessary.

If the ambient operation-cell universe contains a `G`-fixed cell outside `S_x`, such as the rooted cell

\[
(o,o),
\]

adding that one cell to one color fiber makes the fiber sizes `5+4` and forbids output exchange.

Thus the previous exact branch-coherence compiler has

\[
\boxed{|D|=8+1=9.}
\]

The earlier exhaustive orbit calculation proves this is minimal for the seven-vertex FCOA support model.

---

## 11. Symmetric-branch specialization

For the maximally exchangeable branch fiber

\[
A=S_t,
\]

we obtain

\[
G=S_t\wr S_b,
\qquad
H=\Delta S_t\times S_b.
\]

The exact formulas become

\[
\boxed{m_G(H;S_\times)=b(b-1)t,}
\]

\[
\boxed{|D|=b(b-1)t^2,}
\]

\[
\boxed{[G:H]=(t!)^{b-1}.}
\]

Therefore the coherence information is

\[
I_{\rm coh}=(b-1)\log_2(t!).
\]

By Stirling,

\[
\log_2(t!)
=
 t\log_2 t-(\log_2 e)t+O(\log t).
\]

Hence for fixed `b`,

\[
\boxed{
\frac{m_G(H;S_\times)}{I_{\rm coh}}
\sim
\frac{b}{\log_2 t}.
}
\]

So the number of special cells per semantic coherence bit tends to zero as branch width grows.

This does **not** violate an information lower bound: one operation cell is not an independent bit. The entire support is interpreted modulo a rapidly growing ambient symmetry group.

---

## 12. Relative VRI statement

Suppose the erased background FCOA reduct has active automorphism group exactly

\[
G=A\wr S_b.
\]

Then the two-value coherence compiler reduces the active group to `H`, so its relative value-rigidity index is

\[
\boxed{\operatorname{VRI}_{G}= [G:H]=|A|^{b-1}.}
\]

For `A=S_t`, if the only background relation is the cross-domain block relation, its full automorphism group is indeed `S_t wr S_b`.

For a proper 2-transitive subgroup `A<S_t`, additional inherited structure is required to make the baseline active group exactly `A wr S_b`; the support theorem itself is a theorem of the declared permutation action and remains valid.

---

## 13. Literature boundary

Three classical/nearby lines must be kept distinct.

1. **Regular sets / power-set orbits.** A subset with trivial setwise stabilizer is classically called a regular set. Ordinary 2-color distinguishing is equivalent to existence of such a set.
2. **Wreath-product distinguishing number.** Melody Chan studied the distinguishing number of wreath-product actions and characterized the minimum number of colors needed to destroy all symmetry.
3. **Subgroup-relative distinguishing.** Alikhani and Soltani introduced `D_{Gamma,H}(X)`, the minimum number of labels for which every label-preserving element of `Gamma` lies in `H`.
4. **Set-stabilizers with structural properties.** Recent work of Sabatini studies subsets whose setwise stabilizers have controlled orbit/derived structure.

The present resource is different:

\[
\boxed{m_G(H;S)}
\]

requires the setwise stabilizer to be **exactly** `H` and minimizes support cardinality on a declared `G`-set `S`.

No worldwide novelty claim is made without a dedicated literature review for this exact extremal quantity. The wreath coherence formula above is proved self-containedly.

Relevant references for the audit:

- M. Chan, *The distinguishing number of the direct product and wreath product action*, Journal of Algebraic Combinatorics 24 (2006), DOI `10.1007/s10801-006-0006-7`.
- S. Alikhani, S. Soltani, *The distinguishing number of groups based on the distinguishing number of subgroups*, arXiv:1701.00141.
- L. Sabatini, *On stabilizers in finite permutation groups*, Bulletin of the London Mathematical Society (2026), DOI `10.1112/blms.70201`.

---

## 14. Current conclusion

The seven-vertex result has now become the first point of an exact family:

\[
\boxed{
D_8\to V_4
\quad\leadsto\quad
A\wr S_b\to \Delta A\times S_b.
}
\]

For every 2-transitive branch action of degree `t`,

\[
\boxed{
\begin{aligned}
\text{special support} &= b(b-1)t,\\
\text{natural domain} &= b(b-1)t^2,\\
\text{coherence states} &= |A|^{b-1},\\
\text{semantic bits} &= (b-1)\log_2|A|,\\
\text{terminal outputs} &=2.
\end{aligned}}
\]

The only anonymous-output anti-swap exception is the minimal binary case `(b,t)=(2,2)`.

---

## 15. Next strike

The 2-transitive family is now exact because `H` has only two orbits on the natural cross-cell action.

The next true difficulty begins when the internal branch group `A` is **not 2-transitive**. Then its orbital decomposition on

\[
\Lambda\times\Lambda
\]

has more than two classes, and the prescribed-support problem becomes a weighted orbit-selection problem.

The next target is therefore:

\[
\boxed{
\text{express }m_{A\wr S_b}(\Delta A\times S_b;S_\times)
\text{ in terms of the orbital structure of }A.
}
\]

This is the point where prescribed-stabilizer support stops being a two-orbit exercise and becomes a genuine new extremal theory.