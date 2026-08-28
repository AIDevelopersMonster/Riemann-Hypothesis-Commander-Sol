# FCOA Hybrid Memory — Higher-Order Joint Memory

**Direction:** SOL-HYBRID  
**Status:** theorem candidate; internal proof complete; hostile audit required

## 1. Target

We seek a family of three partial operations such that every pair remains nonrigid on the active carrier, but the full triple is rigid:

\[
\pi_X\operatorname{Aut}(\star_i,\star_j)\ne1
\quad(i\ne j),
\]

while

\[
\boxed{\pi_X\operatorname{Aut}(\star_1,\star_2,\star_3)=1.}
\]

This is genuinely higher-order memory: no single operation and no pair suffices.

## 2. Why three operations are minimal

With only two operation symbols there is no distinction between “every proper subfamily is nonrigid” and “the full family is rigid”: the only nontrivial proper subfamilies are the individual reducts. Therefore the first genuinely higher-order level is `k=3`.

## 3. Pure carrier-transversality witness on four points

Let

\[
X=\{a,b,c,d\}.
\]

Use three constant-valued operations with exactly one defined diagonal cell each:

\[
a\star_1 a=\alpha,
\qquad
b\star_2 b=\beta,
\qquad
c\star_3 c=\gamma.
\]

Then

\[
\pi_X\operatorname{Aut}(\star_1)\cong S_3
\]

fixing `a`, and analogously for the other two operations.

Every pair fixes two distinguished points and may transpose the other two:

\[
\pi_X\operatorname{Aut}(\star_1,\star_2)
=\langle(c\ d)\rangle\cong C_2,
\]

\[
\pi_X\operatorname{Aut}(\star_1,\star_3)
=\langle(b\ d)\rangle\cong C_2,
\]

\[
\pi_X\operatorname{Aut}(\star_2,\star_3)
=\langle(a\ d)\rangle\cong C_2.
\]

All three operations together fix `a,b,c`, hence also `d`:

\[
\boxed{\pi_X\operatorname{Aut}(\star_1,\star_2,\star_3)=1.}
\]

This is the cleanest DD higher-order witness: `3` operations, `4` active points, `3` total defined cells.

## 4. A stronger shared-output witness on only three active points

The carrier threshold drops from four to three if we exploit Lift Compatibility.

Let

\[
X=\{0,1,2\},
\qquad
O=\{u_0,u_1,u_2\}.
\]

Each operation is defined on the full diagonal and is bijective from active points to the common output sort.

Choose three bijections

\[
f_1=\mathrm{id},
\qquad
f_2=(01),
\qquad
f_3=(02)
\]

viewed as permutations of the labels `0,1,2` indexing `O`.

Define

\[
x\star_i x=u_{f_i(x)}
\qquad(x\in X),
\]

and no off-diagonal cells.

Thus the tables are

\[
\begin{array}{c|ccc}
&0&1&2\\\hline
\star_1&u_0&u_1&u_2\\
\star_2&u_1&u_0&u_2\\
\star_3&u_2&u_1&u_0
\end{array}
\]

on diagonal arguments.

Each operation individually has the full active symmetry `S_3`: any carrier permutation can be accompanied by the corresponding permutation of the three anonymous outputs.

## 5. Centralizer formula for a pair

For two bijective diagonal encodings `f_i,f_j`, a carrier permutation `g\in S_3` survives the pair iff one output permutation `h` works for both:

\[
hf_i=f_i g,
\qquad
hf_j=f_j g.
\]

Eliminating `h` gives

\[
f_i g f_i^{-1}=f_j g f_j^{-1}.
\]

Equivalently,

\[
\boxed{
g\in C_{S_3}(f_i^{-1}f_j).}
\]

Hence

\[
\boxed{
\pi_X\operatorname{Aut}(\star_i,\star_j)
=C_{S_3}(f_i^{-1}f_j).
}
\]

## 6. Exact pair groups

For the chosen encodings,

\[
f_1^{-1}f_2=(01),
\]

so

\[
\pi_X\operatorname{Aut}(\star_1,\star_2)
=C_{S_3}((01))
=\langle(01)\rangle\cong C_2.
\]

Similarly,

\[
\pi_X\operatorname{Aut}(\star_1,\star_3)
=\langle(02)\rangle\cong C_2.
\]

Finally

\[
f_2^{-1}f_3=(01)(02),
\]

which is a `3`-cycle, so

\[
\pi_X\operatorname{Aut}(\star_2,\star_3)
\cong C_3.
\]

Therefore **every pair is nonrigid**.

## 7. Triple rigidity

A carrier permutation survives all three operations exactly when it centralizes both relative permutations

\[
(01),\qquad(02).
\]

These two transpositions generate all of `S_3`. Therefore their common centralizer is the center of `S_3`, which is trivial:

\[
C_{S_3}((01))\cap C_{S_3}((02))=1.
\]

Hence

\[
\boxed{
\pi_X\operatorname{Aut}(\star_1,\star_2,\star_3)=1.
}
\]

Because every output is used bijectively by every operation, the output action is forced by the carrier action. Thus the full automorphism group is also trivial:

\[
\boxed{
\operatorname{Aut}(\star_1,\star_2,\star_3)=1.
}
\]

This is a genuine third-order memory witness on three active points:

\[
\boxed{
\text{single reducts: }S_3,
\quad
\text{pair reducts: }C_2,C_2,C_3,
\quad
\text{triple reduct: }1.
}
\]

## 8. General diagonal-permutation theorem

Let `X=O` be finite sets of size `n`, let `f_1,\ldots,f_k:X\to O` be bijections, and define diagonal terminal operations by

\[
x\star_i x=f_i(x).
\]

Then for any nonempty subfamily `I` and any chosen base index `i_0\in I`,

\[
\boxed{
\pi_X\operatorname{Aut}(\{\star_i:i\in I\})
=
C_{S_X}\left(
\left\langle
f_{i_0}^{-1}f_i:i\in I
\right\rangle
\right).
}
\]

### Proof

For each `i\in I`, compatibility with a common output permutation requires

\[
h=f_i g f_i^{-1}.
\]

Thus these conjugates must all coincide. Relative to `i_0`, this is equivalent to

\[
g(f_{i_0}^{-1}f_i)=(f_{i_0}^{-1}f_i)g
\]

for every `i\in I`. Hence `g` lies in the centralizer of the subgroup generated by all relative permutations. Conversely such a `g` gives one common forced output action. `□`

This theorem turns higher-order hybrid memory into a centralizer problem.

## 9. Minimal active carrier theorem

### Theorem HM-HO3

Under the requirement that **every pair has a nontrivial active carrier automorphism**, a rigid triple requires at least three active points. Three suffice.

### Proof for `|X|=2`

Let `r` be the unique nonidentity permutation of the two active points. If every pair has nontrivial active projection, then for every pair of operations there exists an output permutation extending `r` simultaneously over that pair.

For one operation `\star_i`, the requirement that `r` preserve it induces a partial bijection `\varphi_i` on the used output values:

\[
\varphi_i(\star_i(p))=\star_i(rp).
\]

Pairwise extendability means that for every `i,j`, the union

\[
\varphi_i\cup\varphi_j
\]

is a well-defined injective partial map on the common output sort. Any conflict in the total union `\bigcup_i\varphi_i` would involve two constraints and would therefore already occur in some pair. Hence the total union is also a well-defined injective partial map.

On a finite pure output sort, every injective partial bijection extends to a permutation. Therefore one common output permutation extends `r` over all three operations. Thus the triple still has a nontrivial active automorphism.

So `|X|=2` is impossible. The three-point construction above attains the lower bound. `□`

Hence

\[
\boxed{
|X|_{\min}=3,
\qquad
k_{\min}=3
}
\]

for genuine third-order active-carrier memory.

## 10. Erasure profile

For the three-point witness, removing any one operation leaves one of the three pair structures and therefore restores nontrivial symmetry:

\[
\operatorname{Aut}(\star_1,\star_2)\ne1,
\]

\[
\operatorname{Aut}(\star_1,\star_3)\ne1,
\]

\[
\operatorname{Aut}(\star_2,\star_3)\ne1.
\]

Thus the rigidity has exact order `3`: every proper two-operation reduct loses it.

This is stronger than ordinary JFS-3, where two operations already suffice.

## 11. Definedness and value origin

All three operations have exactly the same domain:

\[
D_i=\Delta_X.
\]

Therefore for every nonempty subfamily,

\[
\operatorname{Aut}(D_{i_1},\ldots,D_{i_m})=S_3.
\]

No domain information distinguishes the three points at all. Every reduction

\[
S_3\to C_2,C_3\to1
\]

comes solely from compatibility of the common output-value correspondences.

Hence this is a pure higher-order value-memory witness.

## 12. Arithmetic Leakage firewall

The construction is below AL0:

- there is no external carrier order;
- only three active points are used;
- all domains are the symmetric diagonal;
- the value tables are finite permutations, not rank formulas;
- no successor, betweenness, EqGap, addition, or multiplication relation is imported.

The centralizer theorem is purely finite group/action geometry.

## 13. Structural interpretation

JFS-3 showed that one common carrier symmetry may fail because two operations demand incompatible output lifts.

Higher-order JFS shows something stronger:

\[
\boxed{
\text{every pair of lift systems is compatible enough to retain symmetry,}
}
\]

but

\[
\boxed{
\text{the entire family has no common nontrivial compatible lift.}
}
\]

In the diagonal-bijection family, the obstruction is exactly the collapse of the common centralizer:

\[
C(\sigma_{12})\ne1,
\quad
C(\sigma_{13})\ne1,
\quad
C(\sigma_{23})\ne1,
\]

while

\[
\boxed{C(\langle\sigma_{12},\sigma_{13}\rangle)=1.}
\]

This is the first genuinely higher-order joint-memory layer in SOL-HYBRID.

## 14. Status and next attack

The centralizer formula and the explicit `S_3` witness are proof-level finite results. Before upstream adoption, hostile audit should attack:

1. the `|X|=2` lower-bound argument in the presence of unused outputs;
2. one-sorted output mixing;
3. whether a lower total-cell realization exists on `|X|=3` than the `3+3+3` diagonal-bijection witness;
4. classification of all minimal three-point higher-order witnesses;
5. extension to order `k>3`, where every proper subfamily is nonrigid but the full `k`-family is rigid.
