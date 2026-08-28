# Reflections on Anonymous Value Geometry with Commander Sol

## Low-Arity Rigidity Reducts and an Arity Phase Transition

**Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Date: **29 August 2026**

---

## Abstract

We study finite partial operations whose generic sector has a highly symmetric carrier but whose operation values break that symmetry only through anonymous output fibers. The guiding question is not how much raw information is present in the operation table, but how little relational information is sufficient to recover exactly the same carrier automorphism group.

The first part isolates a complete two-output tournament layer. We show that the residual reversal symmetry of a transitive two-fiber coloring is not forced by output anonymity: there are balanced complete two-output layers with trivial automorphism group and the same coarse definedness, commutation, and association data. The first local separator is the cyclic-triangle defect. In the tournament subclass, a ternary anonymous betweenness relation recovers the tournament up to global reversal and therefore has exactly the same carrier automorphism group as the full value layer.

The main result removes the tournament hypothesis. For every complete off-diagonal layer with exactly two anonymous outputs, the ternary relation

\[
Q(x,y,z)\iff x\star y=y\star z
\]

is carrier-exact: its automorphism group is precisely the group of carrier permutations preserving the two output fibers or globally exchanging them. The proof is a binary phase-propagation argument on the connected graph of composable ordered cells.

This mechanism is sharp in the alphabet size. For three or more anonymous outputs, even the complete labeled equality pattern on all subsets of at most three carrier points need not determine the global anonymous color action. We give an explicit five-vertex three-color counterexample. On the other hand, the four-ary relation

\[
E(x,y,u,v)\iff x\star y=u\star v
\]

always recovers the equality partition of the operation cells and hence the full anonymous carrier group. In the natural class of reducts determined by anonymous equality patterns on bounded-size carrier subsets, this yields the exact arity threshold

\[
\boxed{q=2:\ k_{\rm exact}=3,\qquad q\ge3:\ k_{\rm exact}=4.}
\]

The result identifies a genuine binary phase effect: with two outputs, local inequality has a unique complementary phase and propagates globally; with three or more outputs, local color permutations may be compatible on overlaps without gluing to a single global permutation.

**Keywords:** partial operations, automorphism groups, anonymous values, relational reducts, rigidity, colored digraphs, switching, ternary relations, relational complexity.

---

# 1. Why anonymous values are structurally nontrivial

A finite operation table can break carrier symmetry in at least three logically different ways. The set of defined cells can be asymmetric; the values attached to a fixed domain can be asymmetric; or some outputs can be externally named or anchored. These mechanisms should not be conflated.

The present paper isolates the second mechanism. Let

\[
G=\{1,\dots,n\}
\]

be a finite generic carrier and let

\[
D\subseteq G^2\setminus\Delta
\]

be the off-diagonal domain of a terminal operation layer. The outputs used on D are terminal in the sense that they do not participate as arguments in further generic products. We ask how the partition of D into output fibers changes the carrier automorphism group.

When the outputs are **anonymous**, a carrier permutation is allowed to permute the output fibers globally. Thus, for a coloring

\[
c:D\to O,
\]

with finite output set O, the relevant carrier group is

\[
\operatorname{Aut}^{\rm an}(D,c)
=
\left\{
 g\in S_G:
 \exists\pi\in S_O\text{ such that }c(gx,gy)=\pi(c(x,y))
 \text{ for all }(x,y)\in D
\right\}.
\]

This is the carrier shadow of the usual fiber-transport principle: anonymous outputs are not fixed individually, but the partition of the cell domain into value fibers is preserved up to a single global permutation of the fiber labels.

The basic compression problem is therefore:

\[
\boxed{
\text{How small can a derived relational language be while retaining exactly }
\operatorname{Aut}^{\rm an}(D,c)?
}
\]

The answer is unexpectedly sensitive to the number of output fibers.

---

# 2. Coarse invariants can miss the decisive value geometry

Before constructing exact reducts, it is useful to see how much information familiar coarse invariants lose.

Suppose an M0-type backbone is extended by m off-diagonal generic cells whose outputs are terminal. Then each newly defined cell changes exactly three base association triples: one becomes `EQ`, one becomes `LEFT`, and one becomes `RIGHT`. No other second-stage product can be created because the new outputs are terminal.

Consequently the association spectrum depends only on m, not on the geometry of the new cells or on the way terminal values are distributed among them:

\[
\begin{aligned}
EQ &=4(N-1)+m,\\
NEQ&=0,\\
LEFT&=N^2+2N-2+m,\\
RIGHT&=N^2+N-2+m,\\
NONE&=N^3+N^2-4N+9-3m.
\end{aligned}
\]

Likewise, commutation sees only those reverse pairs that carry the same value. Fine fiber geometry can therefore vary while both association data and commutation remain unchanged.

This is not a merely formal observation. We now give two complete two-output layers with the same domain size, the same balanced output multiplicities, the same generic commutation behavior, and the same association spectrum, but different automorphism groups.

---

# 3. Balanced anonymous fibers do not force reversal symmetry

Assume the generic domain is complete off the diagonal:

\[
D=G^2\setminus\Delta.
\]

Suppose further that for every unordered pair \(\{x,y\}\), the two opposite cells receive different anonymous values \(\Omega_+,\Omega_-\). Choosing temporarily which value is called \(\Omega_+\) identifies the layer with a tournament T:

\[
x\to_T y
\iff
c(x,y)=\Omega_+.
\]

The anonymous carrier group becomes

\[
\operatorname{Aut}^{\pm}(T)
=
\{g\in S_G:gT=T\text{ or }gT=T^{\rm op}\}.
\]

For the transitive tournament, the only nontrivial element of \(\operatorname{Aut}^{\pm}\) is order reversal, so the anonymous residual group is \(C_2\).

This residual symmetry is not forced by balancedness or anonymity.

## Proposition 1

On five vertices there exists a tournament T with

\[
\operatorname{Aut}^{\pm}(T)=1.
\]

One explicit example has arc set

\[
T_5=
\{40,41,42,43,20,21,31,32,03,10\}.
\]

### Proof

The outdegree sequence is

\[
(1,1,2,2,4).
\]

Vertex 4 is the unique source and is fixed. Among the two vertices of outdegree 1, vertex 0 points to a vertex of outdegree 2 while vertex 1 points to a vertex of outdegree 1, so they are distinguished. Among the two vertices of outdegree 2, vertex 2 dominates both outdegree-1 vertices while vertex 3 does not. Thus every vertex is fixed and \(\operatorname{Aut}(T_5)=1\).

The tournament has a source but no sink. Its converse has a sink but no source, so \(T_5\not\cong T_5^{\rm op}\). Hence there is no anti-automorphism and \(\operatorname{Aut}^{\pm}(T_5)=1\). \(\square\)

Coloring the tournament arcs by one anonymous output and the reverse arcs by the other gives a complete balanced two-output layer with trivial carrier group. The transitive and rigid examples have the same complete domain, the same fiber sizes, no same-valued reverse pair, and hence the same generic commutation contribution. Their association spectra also coincide because the spectrum depends only on the total number of terminal cells.

This separation motivates the search for a finer local invariant.

---

# 4. The first local separator: cyclic triangles

For a tournament T, let

\[
\tau_3(T)=
\#\{X\in\tbinom G3:T[X]\cong C_3\}.
\]

There is only one anonymous one-point type and only one anonymous two-point tournament type. Thus no local anonymous-pattern invariant of arity at most two can separate two tournament layers.

At arity three there are exactly two anonymous types: transitive and cyclic.

The transitive tournament has

\[
\tau_3=0.
\]

The rigid witness above has exactly two cyclic triples.

A small but useful rigidity bound follows.

## Proposition 2

If a tournament has exactly one cyclic triangle, then it has a nontrivial automorphism. Consequently an anonymous-rigid tournament satisfies

\[
\tau_3\ne1.
\]

### Proof

Let the unique cyclic triangle be

\[
a\to b\to c\to a.
\]

Every outside vertex x must either dominate all of \(a,b,c\) or be dominated by all three. Otherwise x together with two vertices of the cycle would form a second cyclic triangle. Hence \(\{a,b,c\}\) is a module. The 3-cycle

\[
a\mapsto b\mapsto c\mapsto a
\]

extended by the identity outside the module is an automorphism. \(\square\)

Therefore, for the explicit rigid family obtained by successively adjoining universal sources to \(T_5\), the value

\[
\tau_3=2
\]

is exact-minimal for rigidity. Adding a universal source creates no new cyclic triangle, so this defect remains constant for arbitrarily large carriers.

The cyclic-triangle count is a sharp separator for the transitive-versus-rigid question, but it is not a complete symmetry invariant. The next step is to keep local roles, not just local counts.

---

# 5. Tournament betweenness is a carrier-exact ternary reduct

For pairwise distinct vertices define

\[
B_T(x,y,z)
\]

to mean that y is the middle vertex of a transitive triple. In operation language this is

\[
\boxed{
B_\star(x,y,z)
\iff
x\star y=y\star z=x\star z.
}
\]

No output is named. Global exchange of \(\Omega_+\) and \(\Omega_-\) preserves B.

## Theorem 3 (Betweenness reconstruction)

For tournaments T and T' on the same finite carrier,

\[
B_T=B_{T'}
\iff
T'=T\text{ or }T'=T^{\rm op}.
\]

### Proof

On a fixed labeled three-set, the betweenness pattern determines the tournament up to reversal: either the triple is cyclic, in which case no middle vertex exists, or it is transitive and the unique middle vertex is specified.

Thus for every three-set X there is a sign \(\varepsilon_X\in\{+1,-1\}\) such that

\[
T'[X]=T[X]
\]

or

\[
T'[X]=T[X]^{\rm op}.
\]

If two three-sets share an edge, their signs must be equal because the common edge cannot simultaneously agree and disagree with its orientation in T. The graph of three-subsets joined when they share two vertices is connected for \(|G|\ge4\). Therefore all signs are equal. The cases \(|G|\le3\) are immediate. Hence T' equals T or its converse. \(\square\)

## Corollary 4

\[
\boxed{
\operatorname{Aut}(G,B_T)=\operatorname{Aut}^{\pm}(T).
}
\]

Thus the entire anonymous tournament layer has an exact ternary carrier reduct.

The theorem already shows that the classical seven-local half-reconstruction threshold for tournaments addresses a different data model: there the restriction on each subset is retained only up to abstract isomorphism or anti-isomorphism, whereas B retains the labeled role of the middle vertex inside every triple.

The tournament hypothesis, however, is not necessary.

---

# 6. Universal binary phase propagation

Let the complete off-diagonal domain be

\[
D=G^2\setminus\Delta
\]

and let

\[
c:D\to\{0,1\}
\]

be any surjective binary coloring. No relation is assumed between \(c(x,y)\) and \(c(y,x)\).

Define

\[
\boxed{
Q_c(x,y,z)
\iff
c(x,y)=c(y,z),
}
\]

for \(x\ne y\), \(y\ne z\), with \(x=z\) allowed.

Equivalently,

\[
Q_\star(x,y,z)
\iff
x\star y=y\star z.
\]

The full anonymous binary carrier group is

\[
\operatorname{Aut}^{\pm}(c)
=
\{g:c(gx,gy)=c(x,y)\}\cup
\{g:c(gx,gy)=1-c(x,y)\}.
\]

## Theorem 5 (Universal ternary phase reduct)

For every complete binary anonymous layer,

\[
\boxed{
\operatorname{Aut}(G,Q_c)=\operatorname{Aut}^{\pm}(c).
}
\]

### Proof

Every global color-preserving or global color-swapping carrier permutation preserves equality of adjacent cell colors, so

\[
\operatorname{Aut}^{\pm}(c)
\le
\operatorname{Aut}(Q_c).
\]

Conversely let \(g\in\operatorname{Aut}(Q_c)\). Define the discrepancy bit on each ordered cell

\[
\delta_g(x,y)=c(gx,gy)\oplus c(x,y).
\]

If \((x,y)\) and \((y,z)\) are composable cells, preservation of Q gives

\[
c(x,y)=c(y,z)
\iff
c(gx,gy)=c(gy,gz).
\]

For binary values, equality is preserved if and only if the same discrepancy bit is applied to both cells. Hence

\[
\delta_g(x,y)=\delta_g(y,z).
\]

Now consider the graph whose vertices are all ordered off-diagonal cells and whose edges join composable cells \((x,y)\) and \((y,z)\). Its underlying undirected graph is connected for every \(n\ge2\). For \(n=2\), the two cells \((x,y)\) and \((y,x)\) are directly adjacent because \(z=x\) is allowed. For \(n\ge3\), any ordered cell can be chained to any other through shared endpoints.

Therefore \(\delta_g\) is constant on the whole cell domain. If the constant is 0, g preserves every color; if it is 1, g globally swaps the two colors. Thus

\[
g\in\operatorname{Aut}^{\pm}(c).
\]

This proves equality of the two groups. \(\square\)

The result does not require balanced fiber sizes. If the fibers have unequal cardinalities, a global color swap simply cannot be realized by a carrier permutation, so only the color-preserving part survives.

The proof exposes the key binary phenomenon: local phase is a single bit, and connectivity forces that bit to become global.

---

# 7. Why three colors change the problem

For three or more colors, the previous argument breaks at its decisive step. If two adjacent cells have different colors, their images only need to have different colors; there is no unique complementary color.

One might hope that a richer ternary reduct, retaining the **entire equality pattern** of all operation cells supported on a labeled three-set, would still be sufficient. It is not.

## Proposition 6 (Three-color ternary obstruction)

There exists a complete three-anonymous-output layer on five vertices and a carrier permutation g such that:

1. g preserves the complete anonymous equality pattern on every labeled subset of at most three vertices;
2. g is not induced by any single global permutation of the three output fibers.

### Construction

Use a symmetric layer, so

\[
c(x,y)=c(y,x).
\]

Thus it suffices to color the ten edges of \(K_5\). On vertices \(0,1,2,3,4\), in lexicographic edge order

\[
01,02,03,04,12,13,14,23,24,34,
\]

assign colors

\[
\boxed{0,0,0,1,0,0,2,1,0,0.}
\]

Equivalently,

\[
C_0=\{01,02,03,12,13,24,34\},
\]

\[
C_1=\{04,23\},
\qquad
C_2=\{14\}.
\]

Take

\[
g=(0\ 1).
\]

The edge 04 is sent to 14, so any global color permutation compatible with g would have to send color 1 to color 2. But edge 23 is fixed setwise and has color 1, forcing the same global color permutation to fix color 1. This is impossible. Hence g is not an anonymous color automorphism.

Nevertheless, on every labeled three-set the equality relation among the visible edges is preserved. The only global inconsistency involves the two disjoint color-1 edges 04 and 23, and no three-set contains both. On the triple \(\{0,1,4\}\), the three visible edge colors are all distinct, so exchanging the local roles of colors 1 and 2 leaves the ternary equality pattern unchanged. On triples containing 23, the fixed color-1 edge remains locally consistent. Direct finite verification confirms preservation of the complete ternary equality passport. \(\square\)

This example identifies the missing datum. With at least three colors, local color permutations can agree on every overlap that is visible to three variables yet fail to glue to one global permutation when disjoint cells are compared.

The obstruction extends to any fixed \(q>3\) by adjoining fixed vertices carrying fresh colors.

---

# 8. Four variables always suffice

The natural four-ary relation is simply equality of arbitrary operation cells:

\[
\boxed{
E_c(x,y,u,v)
\iff
c(x,y)=c(u,v).
}
\]

In operation notation,

\[
E_\star(x,y,u,v)
\iff
x\star y=u\star v.
\]

## Theorem 7 (Universal four-ary exact reduct)

Let

\[
c:G^2\setminus\Delta\to O
\]

be any surjective coloring by a finite anonymous output set O. Then

\[
\boxed{
\operatorname{Aut}(G,E_c)=\operatorname{Aut}^{\rm an}(c).
}
\]

### Proof

Every anonymous color automorphism preserves equality of cell values, so one inclusion is immediate.

Conversely suppose g preserves E. If two cells p and q have the same color, then gp and gq have the same color; if they have different colors, their images have different colors. Therefore g permutes the value fibers of c. Since c is surjective, define

\[
\pi(c(p))=c(gp).
\]

Preservation of E makes \(\pi\) well-defined, and applying the same argument to \(g^{-1}\) shows that \(\pi\) is bijective. Hence \(\pi\in S_O\) and

\[
c(gp)=\pi(c(p))
\]

for every cell p. Thus g belongs to \(\operatorname{Aut}^{\rm an}(c)\). \(\square\)

The four-ary relation is therefore the exact carrier reduct of the anonymous fiber partition for any finite alphabet.

---

# 9. The arity phase transition

We now combine the binary theorem with the three-color obstruction and the four-ary upper bound.

We work in the following natural class. A bounded-arity anonymous equality reduct is determined by the equality pattern of operation values on labeled carrier subsets of size at most k. No output name is used.

## Theorem 8 (Arity phase transition)

For complete off-diagonal anonymous terminal layers,

\[
\boxed{
q=2:\quad k_{\rm exact}=3,
}
\]

while for every finite

\[
q\ge3,
\]

\[
\boxed{
k_{\rm exact}=4.}
\]

### Proof

For \(q=2\), Theorem 5 gives a ternary exact reduct. Arity at most two cannot be universally exact: the tournament subclass has a unique anonymous two-point local pattern, yet the transitive tournament has residual group \(C_2\) while asymmetric non-self-converse tournaments may have trivial anonymous group.

For \(q\ge3\), Proposition 6 and its q-color extensions show that the complete ternary anonymous equality passport may have a strictly larger carrier stabilizer than the full anonymous value layer. Thus arity three is insufficient. Theorem 7 gives a universal four-ary exact reduct. \(\square\)

The theorem is best read as a phase transition in local gauge freedom:

\[
\boxed{
\text{binary: one complementary phase}\Rightarrow\text{ternary propagation};
}
\]

\[
\boxed{
q\ge3:\text{several local color permutations}\Rightarrow\text{disjoint-cell comparison is necessary}.
}
\]

---

# 10. Relation to switching and relational complexity

The result belongs near, but is not identical with, two classical themes.

First, Seidel switching and its multicolor extensions study local transformations of edge-colored complete graphs. Cameron and Tarzi showed that the finite multicolor switching theory changes qualitatively once more than two colors are allowed; in particular, the switching group is transitive on finite m-colored complete graphs for \(m>2\) [1]. Our setting is different: we do not quotient by a switching action on colorings. Instead we fix one anonymous value partition and ask for the smallest derived relational language with the same **carrier stabilizer**. The common structural message is nevertheless similar: the binary case supports a special parity/phase mechanism that disappears for larger alphabets.

Second, relational complexity and permutation-group arity ask how much relational arity is needed to represent or homogenize a structure without changing its automorphism group. Our `exact reduct` problem is a concrete instance of that philosophy, but with two additional restrictions: the relations must be naturally derived from equality among anonymous operation values, and the underlying object is an operation-cell partition rather than an arbitrary relational structure. This restriction is what makes the explicit \(3/4\) threshold meaningful.

Tournament reconstruction provides another nearby comparison. Classical half-reconstruction retains each local subtournament only up to isomorphism or anti-isomorphism and has an optimal seven-vertex threshold in the general finite case. Our ternary betweenness relation retains labeled local roles, so it solves a strictly different and cheaper stabilizer problem.

We therefore make no broad claim that ternary or four-ary presentations of the relevant permutation groups are new in unrestricted relational language. The contribution is the exact arity classification inside the anonymous-operation equality model developed here.

---

# 11. What the theorem does and does not say

The arity threshold is a **structural reduct statement**, not an information-theoretic compression theorem. A four-ary equality relation can contain as many truth values as the original cell partition, and the ternary binary reduct is not asserted to be Shannon-optimal.

Nor does the theorem say that every q-colored layer has relational complexity exactly 3 or 4 in an unrestricted language. A particular coloring may admit a much smaller accidental reduct. The theorem is universal and model-relative: it asks for the least arity that works for every layer when only anonymous equality information on bounded-size carrier subsets may be used.

The complete-domain assumption is also essential to the ternary binary proof. Once the operation domain becomes sparse, the graph of composable ordered cells can disconnect and different connected components can support independent local phase discrepancies. That sparse-domain theory is the subject of the companion paper.

---

# 12. Conclusion

Anonymous output fibers carry more geometry than coarse operation statistics reveal. Even when definedness, fiber multiplicities, commutation, and association data agree, the arrangement of value fibers can change the carrier automorphism group from a residual reversal to complete rigidity.

For tournament-type layers, the first local separator appears on triples through cyclic-triangle structure, and labeled ternary betweenness already recovers the entire anonymous carrier group. More importantly, the tournament condition can be dropped: every complete binary anonymous layer admits the exact ternary phase reduct

\[
Q(x,y,z)\iff x\star y=y\star z.
\]

The reason is uniquely binary. Equality along composable cells forces a single discrepancy bit to propagate across a connected cell graph. With three or more outputs, local color permutations acquire genuine gauge freedom and can disagree on disjoint cells while remaining indistinguishable on every three-point equality pattern. A fourth variable is then both necessary and sufficient.

The resulting threshold

\[
\boxed{q=2:\ 3\text{ variables};\qquad q\ge3:\ 4\text{ variables}}
\]

provides a compact rigidity law for complete anonymous value layers. It also identifies the natural next boundary: sparse domains, where phase propagation becomes componentwise and rigidity cost must be measured against the geometry of the defined-cell incidence graph.

---

# References

[1] P. J. Cameron and S. Tarzi, “Switching with more than two colours,” *European Journal of Combinatorics* **25** (2004), 169–177. DOI: `10.1016/S0195-6698(03)00097-0`.

[2] A. Boussaïri, P. Ille, G. Lopez, and S. Thomassé, “The C3-structure of the tournaments,” *Discrete Mathematics* **277** (2004), 29–43. DOI: `10.1016/S0012-365X(03)00244-9`.

[3] Y. Boudabbous and G. Lopez, “La relation différence et l’anti-isomorphie,” *Mathematical Logic Quarterly* **41** (1995), 268–280.

[4] Y. Boudabbous, A. Boussaïri, A. Chaïchaâ, and N. El Amri, “(≤ k)-half-reconstructible tournaments for k ≤ 6,” *Comptes Rendus Mathématique* **346** (2008), 919–924. DOI: `10.1016/j.crma.2008.07.024`.

[5] P. J. Cameron and J. H. van Lint, *Designs, Graphs, Codes and Their Links*, London Mathematical Society Student Texts 22, Cambridge University Press, 1991.

[6] P. J. Cameron, *Permutation Groups*, London Mathematical Society Student Texts 45, Cambridge University Press, 1999.

---

## Publication note

This paper is the complete-domain part of the FCOA rigidity-cost programme. Sparse-domain phase cocycles, synchronization costs, and actual cell-extension costs are intentionally deferred to the companion paper.