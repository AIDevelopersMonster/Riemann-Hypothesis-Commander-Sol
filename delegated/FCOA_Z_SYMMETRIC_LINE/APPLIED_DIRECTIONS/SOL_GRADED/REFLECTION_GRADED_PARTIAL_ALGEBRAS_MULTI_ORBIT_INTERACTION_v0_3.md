# Reflection-Graded Partial Algebras — Multi-Orbit Interaction and Classification

**Version:** 0.3  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** TWO-ORBIT INTERACTION THEOREM COMPLETE / GENERAL FINITE LABELLED CLASSIFICATION OBTAINED  
**Depends on:** `REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`, `REFLECTION_GRADED_PARTIAL_ALGEBRAS_ONE_ORBIT_CLASSIFICATION_v0_2.md`

---

## 1. Executive result

The next RPM/RGPA question was whether two unresolved reflection input-orbits classify independently:

\[
\operatorname{Class}(O_1\cup O_2)
\stackrel{?}{=}
\operatorname{Class}(O_1)\times\operatorname{Class}(O_2).
\tag{1}
\]

The answer is **no in general**.

The obstruction has an exact group-theoretic form.

Let `G` be the common automorphism stabilizer of the two unresolved input-orbits, and let `Z_i` be the admissible output-decoration space of `O_i`, carrying the twisted action from the one-orbit theory. Then two-orbit completions are classified by the **diagonal orbit space**

\[
\boxed{
G\backslash(Z_1\times Z_2),
}
\tag{2}
\]

not by the product

\[
(G\backslash Z_1)\times(G\backslash Z_2).
\tag{3}
\]

If `z_i in Z_i` and

\[
H_i=\operatorname{Stab}_G(z_i),
\tag{4}
\]

then the number of joint isomorphism classes lying over the same pair of individual passport classes is exactly

\[
\boxed{
|H_1\backslash G/H_2|.
}
\tag{5}
\]

Thus independence holds over that pair exactly when

\[
\boxed{
G=H_1H_2.
}
\tag{6}
\]

The first decoration changes the effective symmetry group from `G` to `H_1`; the second passport must then be computed under `H_1`, not under the original `G`. This is the precise **stabilizer-breaking interaction mechanism** anticipated in v0.2.

A minimal nontrivial-reflection example occurs on four carrier elements. Two output choices that are individually equivalent become jointly inequivalent according to a new **relative reflection-phase bit**: SAME versus OPPOSITE. The two completions have the same local one-orbit passports, the same exchange profile `Xi`, and the same anchoring data, yet are non-isomorphic.

The same argument extends immediately to any finite labelled family of unresolved reflection orbits:

\[
\boxed{
\operatorname{Class}(O_1,\ldots,O_k)
\cong
G\backslash\prod_{i=1}^k Z_i.
}
\tag{7}
\]

For finite `G`, Burnside's lemma gives an exact enumeration formula.

---

## 2. Fixed completion problem

Fix a reflection-partial magma completion problem

\[
\mathcal P=(A,D_0,\mu_0,\nu,P),
\tag{8}
\]

where `P subseteq A^2` is the protected reflection-invariant set of cells that must remain undefined.

Let

\[
\Gamma=\operatorname{Aut}(\mathcal P)
\tag{9}
\]

be the automorphism group preserving the reflection, the old partial operation, and the protected set.

Let

\[
O_1,O_2\subseteq A^2
\tag{10}
\]

be distinct unresolved `R_2`-orbits, where

\[
R_2(x,y)=(\nu x,\nu y).
\tag{11}
\]

We first treat **labelled orbit completion**, meaning an isomorphism must preserve each input orbit `O_i` setwise. This separates genuine decoration interaction from the additional phenomenon in which automorphisms permute the unresolved input orbits themselves.

Define the common input stabilizer

\[
\boxed{
G=\Gamma_{O_1,O_2}
=\{\gamma\in\Gamma:\gamma O_1=O_1,\ \gamma O_2=O_2\}.
}
\tag{12}
\]

---

## 3. Decoration spaces and local actions

For each `O_i`, choose a representative `p_i` when the orbit has two points.

Define the admissible decoration space

\[
Z_i=
\begin{cases}
A,&|O_i|=2,\\
A^\nu,&|O_i|=1.
\end{cases}
\tag{13}
\]

For a two-point orbit, the permutation action of `G` on `O_i` defines

\[
\varepsilon_i:G\to C_2,
\tag{14}
\]

where `epsilon_i(gamma)=1` exactly when `gamma p_i=R_2p_i`.

The twisted action is

\[
\boxed{
\gamma\star_i z
=\nu^{\varepsilon_i(\gamma)}\gamma z.
}
\tag{15}
\]

For a fixed input orbit, use the ordinary action on `A^nu`:

\[
\gamma\star_i z=\gamma z.
\tag{16}
\]

The one-orbit theorem already proves that these are exactly the actions controlling isomorphism of individual decorated orbits.

---

## 4. Two-Orbit Diagonal Classification Theorem

For `z_i in Z_i`, let

\[
\mathcal A(z_1,z_2)
\tag{17}
\]

be the conservative completion obtained by adjoining exactly the two decorated reflection graph-orbits determined by `(O_1,z_1)` and `(O_2,z_2)`.

### Theorem 4.1 — diagonal classifier

Two labelled two-orbit completions

\[
\mathcal A(z_1,z_2)
\quad\text{and}\quad
\mathcal A(w_1,w_2)
\]

are isomorphic over the fixed completion problem if and only if there exists one **single** element `gamma in G` such that

\[
\boxed{
w_1=\gamma\star_1 z_1,
\qquad
w_2=\gamma\star_2 z_2.
}
\tag{18}
\]

Consequently

\[
\boxed{
\operatorname{Class}(O_1,O_2)
\cong
G\backslash(Z_1\times Z_2),
}
\tag{19}
\]

where `G` acts diagonally by

\[
\gamma\cdot(z_1,z_2)
=(\gamma\star_1z_1,\gamma\star_2z_2).
\tag{20}
\]

### Proof

Any isomorphism of the two completions that preserves the fixed base and each labelled input orbit belongs to `G` by definition.

On each decorated orbit separately, the one-orbit classification theorem says that preservation of the new graph orbit is equivalent to

\[
w_i=\gamma\star_i z_i.
\]

The same carrier map `gamma` must preserve both new decorated graph-orbits simultaneously, giving (18).

Conversely, if one `gamma in G` satisfies both equations, it preserves the old graph and protected set and maps each of the two new graph-orbits to the corresponding target graph-orbit. Hence it is an isomorphism. QED.

### Structural point

The product of one-orbit classifications would allow one automorphism `gamma_1` for the first output and an unrelated automorphism `gamma_2` for the second. A real isomorphism of the joint completion has only **one carrier map**. Equation (18) is the source of interaction.

---

## 5. Static versus dynamic coupling

There are two distinct reasons why naive factorization can fail.

### Static input coupling

The individual orbit stabilizers

\[
\Gamma_{O_1},
\qquad
\Gamma_{O_2}
\tag{21}
\]

may be larger than their common intersection `G`. Then some symmetries available in the separate one-orbit problems are already unavailable before any outputs are chosen.

### Dynamic decoration coupling

Even after restricting from the start to the common group `G`, choosing `z_1` reduces the residual symmetry to

\[
H_1=\operatorname{Stab}_G^{\star_1}(z_1).
\tag{22}
\]

The second decoration must then be classified under `H_1`, not under `G`.

The minimal example in Section 9 is constructed so that

\[
\Gamma_{O_1}=\Gamma_{O_2}=G,
\tag{23}
\]

thereby eliminating static coupling and isolating the dynamic stabilizer-breaking mechanism.

---

## 6. Sequential Stabilizer Theorem

### Theorem 6.1

Fix a first decoration `z_1 in Z_1` and let

\[
H_1=\operatorname{Stab}_G^{\star_1}(z_1).
\tag{24}
\]

Then joint isomorphism classes whose first coordinate lies in the `G`-orbit of `z_1` are classified exactly by

\[
\boxed{
H_1\backslash Z_2
}
\tag{25}
\]

for the restricted `star_2` action.

### Proof

Every pair whose first coordinate lies in `G star_1 z_1` can be moved by a diagonal element of `G` to a pair of the form

\[
(z_1,z_2').
\]

Once the first coordinate has been fixed to `z_1`, the only remaining diagonal automorphisms are precisely those in `H_1`. They identify two second coordinates exactly when those coordinates lie in the same `H_1` orbit. QED.

### Interpretation

This proves the interaction law in the intended causal form:

\[
\boxed{
\text{first decoration}
\longrightarrow
\text{stabilizer reduction }G\to H_1
\longrightarrow
\text{refinement of second passport space}.
}
\tag{26}
\]

---

## 7. Double-Coset Fiber Theorem

There is a natural map that forgets relative alignment:

\[
\Phi:
G\backslash(Z_1\times Z_2)
\longrightarrow
(G\backslash Z_1)\times(G\backslash Z_2).
\tag{27}
\]

It sends a joint class to its two individual `G`-passport classes.

The map is always surjective: choose arbitrary representatives from the two individual classes and pair them.

### Theorem 7.1 — double-coset fiber theorem

Fix `z_i in Z_i` and put

\[
H_i=\operatorname{Stab}_G^{\star_i}(z_i).
\tag{28}
\]

Then the fiber of `Phi` over

\[
([z_1]_G,[z_2]_G)
\tag{29}
\]

is canonically in bijection with the double-coset space

\[
\boxed{
H_1\backslash G/H_2.
}
\tag{30}
\]

### Proof

Every pair in the specified fiber has the form

\[
(g_1\star_1z_1,\ g_2\star_2z_2)
\tag{31}
\]

for some `g_1,g_2 in G`.

Apply the diagonal action of `g_1^{-1}`. The pair becomes

\[
(z_1,\ g\star_2z_2),
\qquad
g=g_1^{-1}g_2.
\tag{32}
\]

Changing the initial representation by an element of `H_2` changes `g` on the right and does not change the second coordinate. After fixing the first coordinate to `z_1`, the remaining diagonal symmetries are exactly `H_1`, which act on `g` from the left.

Thus two elements `g,g'` give the same joint orbit exactly when

\[
g'\in H_1gH_2.
\]

Hence the fiber is `H_1 backslash G/H_2`. QED.

---

## 8. Exact Factorization Criterion

### Theorem 8.1 — independence criterion

For a fixed pair of individual passport classes `([z_1]_G,[z_2]_G)`, there is exactly one joint completion class above them if and only if

\[
\boxed{
G=H_1H_2.
}
\tag{33}
\]

The two orbit decorations classify independently for **all** output classes if and only if

\[
G=\operatorname{Stab}_G(z_1)\operatorname{Stab}_G(z_2)
\tag{34}
\]

for every admissible pair of representatives, with stabilizers taken in the corresponding twisted actions.

### Proof

By Theorem 7.1 the fiber is a singleton exactly when `H_1 backslash G/H_2` has one double coset. This is equivalent to every element of `G` lying in `H_1H_2`, i.e. `G=H_1H_2`. QED.

### Immediate sufficient conditions

Factorization over a pair certainly holds if either

\[
H_1=G
\quad\text{or}\quad
H_2=G.
\tag{35}
\]

Thus a decoration that breaks no common symmetry cannot create dynamic coupling with the other orbit.

---

## 9. Minimal stabilizer-breaking example

Let

\[
A=\{a,\bar a,b,\bar b\}
\tag{36}
\]

with fixed-point-free reflection

\[
\nu(a)=\bar a,
\qquad
\nu(b)=\bar b.
\tag{37}
\]

Take the empty base operation and no protected cells.

Define two unresolved input reflection orbits using only the first carrier reflection pair:

\[
O_1=
\{(a,a),(\bar a,\bar a)\},
\tag{38}
\]

and

\[
O_2=
\{(a,\bar a),(\bar a,a)\}.
\tag{39}
\]

The first is the reflected diagonal orbit; the second is the geometric mirror orbit.

Let `r` swap `a <-> bar a` and fix `b,bar b`, and let `s` swap `b <-> bar b` and fix `a,bar a`. Then

\[
\nu=rs.
\tag{40}
\]

The setwise stabilizer of either `O_1` or `O_2` in the empty-base automorphism group is exactly

\[
\boxed{
G=\langle r,s\rangle\cong C_2\times C_2.
}
\tag{41}
\]

Thus

\[
\Gamma_{O_1}=\Gamma_{O_2}=G,
\tag{42}
\]

so there is no static input coupling.

Choose representatives

\[
p_1=(a,a),
\qquad
p_2=(a,\bar a).
\tag{43}
\]

For both orbits,

\[
\varepsilon_i(r)=1,
\qquad
\varepsilon_i(s)=0,
\qquad
\varepsilon_i(rs)=1.
\tag{44}
\]

Using `nu=rs`, the twisted actions satisfy

\[
r\star_i z=sz,
\qquad
s\star_i z=sz,
\qquad
rs\star_i z=z.
\tag{45}
\]

Hence for both one-orbit problems

\[
[b]_G=\{b,\bar b\}.
\tag{46}
\]

So `b` and `bar b` define the **same individual passport** for each orbit.

---

## 10. SAME and OPPOSITE joint completions

Define two joint completions.

### SAME

On `O_1`:

\[
\mu_S(a,a)=b,
\qquad
\mu_S(\bar a,\bar a)=\bar b.
\tag{47}
\]

On `O_2`:

\[
\mu_S(a,\bar a)=b,
\qquad
\mu_S(\bar a,a)=\bar b.
\tag{48}
\]

### OPPOSITE

Keep `O_1` unchanged:

\[
\mu_O(a,a)=b,
\qquad
\mu_O(\bar a,\bar a)=\bar b,
\tag{49}
\]

but reverse the output phase on `O_2`:

\[
\mu_O(a,\bar a)=\bar b,
\qquad
\mu_O(\bar a,a)=b.
\tag{50}
\]

Both are reflection-equivariant conservative two-orbit completions.

Each orbit separately carries the same one-orbit passport in `SAME` and `OPPOSITE` because `b` and `bar b` lie in the same twisted `G` orbit.

---

## 11. Interaction theorem in the minimal example

For the first decoration `z_1=b`, the twisted stabilizer is

\[
H_1
=
\{1,rs\}
=
\{1,\nu\}.
\tag{51}
\]

The same is true for `z_2=b`:

\[
H_2=\{1,\nu\}.
\tag{52}
\]

Since `G` is abelian,

\[
|H_1\backslash G/H_2|
=|G/H_1|
=2.
\tag{53}
\]

Therefore the pair of identical individual passport classes has exactly two joint completion classes.

They are represented by

\[
(b,b)
\quad\text{and}\quad
(b,\bar b),
\tag{54}
\]

namely `SAME` and `OPPOSITE`.

### Theorem 11.1 — non-factorization

\[
\boxed{
\mathcal A_S\not\cong\mathcal A_O
}
\tag{55}
\]

although the two structures have the same individual one-orbit passports on both `O_1` and `O_2`.

### Proof

The double-coset computation already proves the result.

Concretely, every allowed element of `G` either leaves both chosen `b/bar b` decorations unchanged or flips them simultaneously. It can never change the relative relation

\[
z_2=z_1
\tag{56}
\]

to

\[
z_2=\nu z_1.
\tag{57}
\]

Hence SAME and OPPOSITE belong to distinct diagonal `G` orbits. QED.

---

## 12. Relative reflection phase

The minimal counterexample exposes a new relational invariant not visible in the local passports.

Suppose two decorated input orbits have outputs in the same non-fixed reflection orbit

\[
\{z,\nu z\}.
\tag{58}
\]

After choosing compatible representatives, define the **relative reflection phase**

\[
\delta(O_1,O_2)=
\begin{cases}
0,&z_2=z_1,\\
1,&z_2=\nu z_1.
\end{cases}
\tag{59}
\]

when this binary comparison is well-defined modulo the common diagonal automorphism action.

In the minimal example, `delta` is exactly the double-coset label:

\[
\boxed{
\delta=0\ \text{for SAME},
\qquad
\delta=1\ \text{for OPPOSITE}.
}
\tag{60}
\]

This is not an additional primitive invariant in the general theory: the complete object is the double-coset class. `delta` is its smallest binary manifestation.

---

## 13. Why previous invariants miss the interaction

The two minimal completions have the same exchange profile.

Only `O_2` lies on the geometric mirror locus. It is split in both structures, so

\[
\Xi(\mathcal A_S)=\Xi(\mathcal A_O)=(2,0,2,0).
\tag{61}
\]

The reflected diagonal orbit `O_1` is not geometric exchange, and because its output is non-fixed it does not enter `E_alg` through its trivial swap.

The anchoring spectrum on the geometric orbit is also the same: the output lies in the external reflection pair `{b,bar b}` in both cases.

Thus the distinction survives after fixing

- carrier reflection orbit data;
- input orbit data;
- output reflection orbit data;
- `Xi`;
- local anchoring type;
- each one-orbit completion passport.

The missing information is purely **relational between decorated orbits**.

---

## 14. Minimality for nontrivial reflection coupling

### Theorem 14.1

The four-element construction is minimal among carriers with nonidentity reflection for the dynamic mechanism in which

1. the two input-orbit problems have the same common nontrivial stabilizer before decoration;
2. an output pair is equivalent in each individual one-orbit problem;
3. choosing the first decoration breaks the symmetry that made the second pair equivalent.

### Proof

For `|A|=1`, reflection is trivial.

For `|A|=2` with nonidentity reflection, the carrier is one reflection two-cycle and the automorphism group commuting with reflection is `C_2={1,nu}`. Every input reflection orbit has two points. For its chosen representative, the nonidentity element sends the representative to its `R_2` mate, so the twisted action is

\[
\nu\star z=\nu(\nu z)=z.
\tag{62}
\]

Thus the twisted action is trivial; there is no nontrivial individual output equivalence available to split.

For `|A|=3` with nonidentity reflection, the carrier consists of one two-cycle and one fixed point. The commuting automorphism group is again at most `C_2`. On every two-point input orbit the same cancellation (62) makes the twisted action trivial. A fixed input orbit must use only reflection-fixed coordinates, hence is `(r,r)` for the unique fixed point `r`, and reflection equivariance permits only the fixed output `r`. Again there is no nontrivial individual output equivalence to split dynamically.

The four-element construction supplies the required mechanism. QED.

---

## 15. General labelled multi-orbit theorem

Let

\[
O_1,\ldots,O_k
\tag{63}
\]

be distinct unresolved reflection input-orbits and restrict to isomorphisms preserving each `O_i` setwise.

Let

\[
G=igcap_{i=1}^k\Gamma_{O_i}
\tag{64}
\]

and let `Z_i` carry its local twisted/ordinary action `star_i`.

For

\[
z=(z_1,\ldots,z_k)\in\prod_i Z_i,
\tag{65}
\]

let `A(z)` be the completion by all `k` decorated graph-orbits.

### Theorem 15.1 — finite labelled completion classification

\[
\boxed{
\mathcal A(z)\cong\mathcal A(w)
\iff
\exists\gamma\in G\ \forall i:\
w_i=\gamma\star_i z_i.
}
\tag{66}
\]

Therefore

\[
\boxed{
\operatorname{Class}(O_1,\ldots,O_k)
\cong
G\backslash\prod_{i=1}^k Z_i.
}
\tag{67}
\]

### Proof

Exactly as in Theorem 4.1: a single carrier automorphism must preserve every decorated graph-orbit simultaneously. The one-orbit condition on each coordinate is necessary and jointly sufficient. QED.

### Sequential stabilizer chain

Fix an ordering of the selected input orbits. Define

\[
G_0=G,
\tag{68}
\]

and recursively after choosing `z_i`,

\[
G_i
=
\operatorname{Stab}_{G_{i-1}}^{\star_i}(z_i).
\tag{69}
\]

At stage `i+1`, genuinely distinct continuations are the `G_i`-orbits in `Z_{i+1}`.

Thus finite completion classification admits an exact recursive algorithm by stabilizer refinement.

---

## 16. Burnside Enumeration Theorem

Assume `G` and all `Z_i` are finite.

For `gamma in G`, let

\[
\operatorname{Fix}_{Z_i}(\gamma)
=
\{z\in Z_i:\gamma\star_i z=z\}.
\tag{70}
\]

### Theorem 16.1

The number of labelled `k`-orbit completion classes is

\[
\boxed{
N(O_1,\ldots,O_k)
=
\frac1{|G|}
\sum_{\gamma\in G}
\prod_{i=1}^k
|\operatorname{Fix}_{Z_i}(\gamma)|.
}
\tag{71}
\]

### Proof

Theorem 15.1 identifies completion classes with orbits of the finite diagonal `G` action on `prod_i Z_i`. Burnside's lemma counts those orbits. A tuple is fixed by `gamma` exactly when every coordinate is fixed by its corresponding local action, so the fixed-tuple count factors as the product in (71). QED.

This is the first exact enumeration formula for finite RPM conservative completions modulo base automorphism.

---

## 17. Unlabelled orbit families

If the base automorphism group permutes the selected unresolved input-orbits among themselves and the classification problem does **not** label them, then the diagonal theorem must be enlarged by the induced permutation action on the orbit index set.

The natural object is an assignment

\[
\zeta:O_i\mapsto z_i
\tag{72}
\]

of an admissible decorated graph-orbit to each selected input orbit. `Gamma` acts simultaneously by

1. permuting the input-orbit indices;
2. transporting the chosen representative orientation;
3. applying the corresponding reflected output correction.

The unlabelled classification is the orbit space of this assignment set under that full action.

This is a genuine extension of the labelled theorem, but it introduces no new local algebraic axiom; it is an additional permutation-group layer. The present report keeps the labelled theorem as the clean interaction nucleus.

---

## 18. Consequence for the completion dcpo

The foundations report showed that conservative completions form a dcpo under graph inclusion. The present result describes finite rank slices of that dcpo modulo automorphism.

For a fixed finite set of unresolved input reflection-orbits, the raw completion choices form a product of local flat domains. Isomorphism then quotients this product by the common diagonal symmetry group.

Thus the conceptual structure is

\[
\boxed{
\text{raw completion space}
=
\text{product of local reflection choices},
}
\tag{73}
\]

but

\[
\boxed{
\text{moduli space of completions}
=
\text{global diagonal quotient},
}
\tag{74}
\]

and it is the quotient that creates inter-orbit coupling.

This cleanly separates **construction independence** from **classification dependence**.

---

## 19. Publication significance

The RPM/RGPA successor theory now has:

1. category and strong embeddings;
2. free linearization to reflection-graded partial algebras;
3. completion dcpo and orbitwise raw completion theorem;
4. geometric/algebraic/excess exchange loci;
5. exact one-orbit twisted passport classification;
6. minimal chirality counterexample to `Xi` completeness;
7. exact two-orbit diagonal classification;
8. double-coset interaction obstruction;
9. minimal stabilizer-breaking example;
10. exact labelled finite multi-orbit classification;
11. Burnside enumeration formula.

This crosses the mathematical threshold from a collection of definitions to a genuine **finite completion/moduli theory**.

The remaining barrier to a standalone new-theory publication is now primarily bibliographic and positioning-related, not lack of internal theorem structure. A novelty/terminology audit against neighboring partial-algebra frameworks is therefore becoming mandatory before naming/priority claims are frozen.

---

## 20. Next frontier

There are two natural continuations.

### A. Unlabelled completion moduli

Develop the full action when automorphisms permute unresolved input-orbits, and derive a cycle-index / Burnside formula for unlabelled finite completion classes.

### B. Universality / representation

Characterize free RPMs generated by a reflected set with a prescribed protected domain, and determine whether free linearization `K[-]` satisfies a useful universal property relative to set maps into RGPAs.

The second direction is the more important publication threshold: a clean universal-property theorem would establish RPM/RGPA as an algebraic construction rather than merely an orbit-classification language.
