# Reflections on Anonymous Value Geometry with Commander Sol

## Low-Arity Rigidity Reducts and an Arity Phase Transition

**Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Version: **1.0**  
Date: **29 August 2026**  
Zenodo DOI: **10.5281/zenodo.22157403**  
Published version: https://doi.org/10.5281/zenodo.22157403

---

## Abstract

We study finite partial operations whose generic sector has a highly symmetric carrier while symmetry is broken only by anonymous terminal output fibers. The central question is not how much raw information is stored in the operation table, but how little derived relational information is sufficient to recover exactly the same carrier automorphism group.

For complete two-output tournament layers, balanced anonymous fibers need not leave the residual reversal symmetry of the transitive coloring: an explicit five-vertex balanced layer is rigid while retaining the same complete definedness, fiber sizes, commutation contribution, and terminal association spectrum as the transitive model. The first local separator is the cyclic-triangle defect. In the tournament subclass, a ternary anonymous betweenness relation reconstructs the tournament up to global reversal and is therefore carrier-exact.

The main theorem removes the tournament condition. For every complete off-diagonal layer with exactly two anonymous outputs, the ternary relation

\[
Q(x,y,z)\Longleftrightarrow x\star y=y\star z \tag{1}
\]

is carrier-exact: its automorphism group is precisely the group of carrier permutations preserving the two output fibers or globally exchanging them. The proof is a binary phase-propagation argument on the connected graph of composable ordered cells.

The binary mechanism is sharp in alphabet size. For three or more anonymous outputs, even the complete labeled equality pattern on all carrier subsets of size at most three need not determine a single global permutation of the output fibers. We give an explicit five-vertex three-color counterexample. Conversely, the four-ary relation

\[
E(x,y,u,v)\Longleftrightarrow x\star y=u\star v \tag{2}
\]

always recovers the equality partition of all operation cells. In the natural class of reducts determined by anonymous equality patterns on bounded-size labeled carrier subsets, the universal exact arity is therefore

\[
\boxed{q=2:\ k_{\mathrm{exact}}=3,\qquad q\ge3:\ k_{\mathrm{exact}}=4.} \tag{3}
\]

The result isolates a binary phase phenomenon: with two outputs, local inequality has a unique complementary phase and propagates globally; with three or more outputs, locally compatible color permutations may fail to glue to one global permutation.

**Keywords:** partial operations; automorphism groups; anonymous values; relational reducts; rigidity; colored digraphs; switching; tournament betweenness; relational complexity.

---

# 1. Anonymous value geometry

Let \(G\) be a finite carrier and \(D\subseteq G^2\setminus\Delta\) the off-diagonal domain of a terminal operation layer. Let \(c:D\to O\) be the value map to a finite output set. Outputs are **anonymous**: a carrier permutation may permute output fibers globally. The relevant carrier group is

\[
\operatorname{Aut}^{\mathrm{an}}(D,c)=\{g\in S_G:\exists\pi\in S_O\ \forall(x,y)\in D,\ c(gx,gy)=\pi(c(x,y))\}. \tag{4}
\]

Thus the structural datum is the partition of \(D\) into value fibers, not their names. We ask how small a naturally derived relational language can be while retaining exactly (4).

# 2. Coarse invariants can miss fiber geometry

For an M0-type backbone extended by \(m\) off-diagonal generic cells with terminal outputs, terminality implies that each new cell changes exactly three base association triples. Hence

\[
\begin{aligned}
EQ &=4(N-1)+m,\\
NEQ&=0,\\
LEFT&=N^2+2N-2+m,\\
RIGHT&=N^2+N-2+m,\\
NONE&=N^3+N^2-4N+9-3m.
\end{aligned} \tag{5}
\]

The spectrum depends on \(m\), not on the geometry of the new cells or their terminal values. Commutation likewise sees only reverse pairs carrying equal values. Fine fiber geometry may therefore vary while both coarse invariants remain unchanged.

# 3. Balanced anonymous fibers need not leave reversal symmetry

Assume \(D=G^2\setminus\Delta\), and opposite cells always receive different anonymous values. Temporarily naming one value identifies the layer with a tournament \(T\). Its anonymous carrier group is

\[
\operatorname{Aut}^{\pm}(T)=\{g\in S_G:gT=T\text{ or }gT=T^{\mathrm{op}}\}. \tag{6}
\]

For the transitive tournament this group is \(C_2\). It need not be so.

## Proposition 1

On five vertices there exists a tournament \(T_5\) with \(\operatorname{Aut}^{\pm}(T_5)=1\). One explicit arc set is

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}. \tag{7}
\]

### Proof

Its outdegree sequence is \((1,1,2,2,4)\). Vertex 4 is the unique source. The two outdegree-1 vertices are distinguished because vertex 0 points to an outdegree-2 vertex while vertex 1 points to an outdegree-1 vertex. The two outdegree-2 vertices are distinguished because vertex 2 dominates both outdegree-1 vertices while vertex 3 does not. Thus every vertex is fixed and \(\operatorname{Aut}(T_5)=1\).

The tournament has a source and no sink; its converse has a sink and no source. Hence \(T_5\not\cong T_5^{\mathrm{op}}\), so no anti-automorphism exists. \(\square\)

The transitive and rigid examples have the same complete domain, equal fiber sizes, no same-valued reverse pair, and the same spectrum (5), but different carrier groups.

# 4. The first local separator: cyclic triangles

For a tournament define

\[
\tau_3(T)=\#\{X\subseteq G:|X|=3,\ T[X]\cong C_3\}. \tag{8}
\]

There is one anonymous tournament type on at most two vertices; arity three is the first place where transitive and cyclic types separate. The transitive tournament has \(\tau_3=0\); the witness (7) has exactly the cyclic triples \(\{0,1,3\}\) and \(\{0,2,3\}\).

## Proposition 2

If a tournament has exactly one cyclic triangle, then it has a nontrivial automorphism.

### Proof

Let the unique cycle be \(a\to b\to c\to a\). Every outside vertex must either dominate all three vertices or be dominated by all three; otherwise a second cyclic triangle appears. Hence \(\{a,b,c\}\) is a module, and its 3-cycle rotation extends by the identity to an automorphism. \(\square\)

Thus an anonymous-rigid tournament cannot have \(\tau_3=0\) or 1. The witness (7) attains 2, and adjoining universal sources preserves this value.

# 5. Tournament betweenness is an exact ternary reduct

For pairwise distinct vertices define

\[
B_\star(x,y,z)\Longleftrightarrow x\star y=y\star z=x\star z. \tag{9}
\]

## Theorem 3 (Betweenness reconstruction)

For tournaments \(T,T'\) on the same finite carrier,

\[
B_T=B_{T'}\Longleftrightarrow T'=T\text{ or }T'=T^{\mathrm{op}}. \tag{10}
\]

### Proof

On a labeled three-set, the betweenness pattern determines the tournament up to reversal. Hence each three-set chooses agreement or reversal. Two three-sets sharing an edge must make the same choice, because their common edge cannot simultaneously agree and disagree with its orientation in \(T\). The graph of three-subsets joined when they share two vertices is connected for \(|G|\ge4\); smaller cases are immediate. Thus one global choice holds. \(\square\)

Therefore

\[
\operatorname{Aut}(G,B_T)=\operatorname{Aut}^{\pm}(T). \tag{11}
\]

This differs from classical half-reconstruction, where each local subtournament is retained only up to abstract isomorphism or anti-isomorphism; here the labeled middle role is retained.

# 6. Universal binary phase propagation

Let \(D=G^2\setminus\Delta\) and \(c:D\to\{0,1\}\) be any surjective binary coloring. Define

\[
Q_c(x,y,z)\Longleftrightarrow c(x,y)=c(y,z),
\]

for \(x\ne y\), \(y\ne z\), with \(x=z\) allowed.

## Theorem 5 (Universal ternary phase reduct)

\[
\operatorname{Aut}(G,Q_c)=\operatorname{Aut}^{\pm}(c). \tag{12}
\]

### Proof

Global preservation or exchange of the two colors preserves \(Q_c\). Conversely, for \(g\in\operatorname{Aut}(Q_c)\), define

\[
\delta_g(x,y)=c(gx,gy)\oplus c(x,y).
\]

For composable cells \((x,y),(y,z)\), preservation of \(Q_c\) is equivalent, in the binary alphabet, to

\[
\delta_g(x,y)=\delta_g(y,z).
\]

The undirected graph on ordered off-diagonal cells joining \((x,y)\) to \((y,z)\) is connected for every \(n\ge2\) when \(x=z\) is allowed. Therefore \(\delta_g\) is globally constant. Constant 0 gives color preservation and constant 1 gives global color exchange. \(\square\)

Balanced fiber sizes are not required. The theorem exposes the binary mechanism: a local discrepancy is one bit, and connectivity makes that phase global.

# 7. The three-color obstruction

For \(q\ge3\), inequality no longer determines a unique complementary phase. Even retaining the complete equality pattern among all operation cells supported on each labeled carrier subset of size at most three is insufficient.

## Proposition 6

There exists a complete three-output layer on five vertices and a carrier permutation \(g\) that preserves every labeled anonymous equality pattern on carrier subsets of size at most three but is not induced by a single global permutation of the three output fibers.

### Construction and proof

Use a symmetric coloring of \(K_5\). In edge order

\[
01,02,03,04,12,13,14,23,24,34,
\]

assign colors

\[
0,0,0,1,0,0,2,1,0,0. \tag{13}
\]

Thus \(C_0=\{01,02,03,12,13,24,34\}\), \(C_1=\{04,23\}\), and \(C_2=\{14\}\). Let \(g=(0\ 1)\).

Edge 04 maps to 14, so any global output permutation compatible with \(g\) must send color 1 to color 2. But edge 23 is fixed and has color 1, forcing the same permutation to fix color 1. Hence no global output permutation realizes \(g\).

Nevertheless, every labeled three-set retains the same equality pattern. The global inconsistency is between disjoint edges 04 and 23, which no three-set can see simultaneously. On \(\{0,1,4\}\), all three edge colors are distinct, so the local exchange of colors 1 and 2 is equality-invisible. Exhaustive finite verification confirms all triples. \(\square\)

For any fixed \(q>3\), adjoin vertices fixed by \(g\), realize each fresh color on a selected edge entirely among those fixed vertices, and color all remaining new incident edges by color 0. The original 1/2 inconsistency persists while every ternary equality pattern remains preserved. Thus ternary anonymous equality data are not universally exact for any \(q\ge3\).

# 8. Four variables always suffice

Define

\[
E_c(x,y,u,v)\Longleftrightarrow c(x,y)=c(u,v).
\]

## Theorem 7 (Universal four-ary exact reduct)

For every finite surjective coloring \(c:G^2\setminus\Delta\to O\),

\[
\operatorname{Aut}(G,E_c)=\operatorname{Aut}^{\mathrm{an}}(c). \tag{14}
\]

### Proof

Anonymous color automorphisms preserve equality of cell values. Conversely, if \(g\) preserves \(E_c\), define \(\pi(c(p))=c(gp)\). Equality preservation makes \(\pi\) well-defined, and the same argument for \(g^{-1}\) makes it bijective. Thus \(g\) induces one global permutation of the output fibers. \(\square\)

# 9. The arity phase transition

A **bounded-arity anonymous equality reduct of order \(k\)** is a relational reduct determined by equality patterns of operation values on labeled carrier subsets of size at most \(k\), without naming output fibers.

## Theorem 8 (Arity phase transition)

For complete off-diagonal anonymous terminal layers,

\[
\boxed{q=2:\ k_{\mathrm{exact}}=3,\qquad q\ge3:\ k_{\mathrm{exact}}=4.}
\]

### Proof

For \(q=2\), Theorem 5 gives a ternary exact reduct. Arity at most two is not universally exact: the tournament subclass has one anonymous two-point pattern, while transitive and asymmetric non-self-converse tournaments can have anonymous groups \(C_2\) and 1 respectively.

For \(q\ge3\), Proposition 6 and its extensions show that even the full labeled ternary equality passport may have a strictly larger carrier stabilizer than the full anonymous value layer. Thus arity three is insufficient. Theorem 7 gives the universal four-ary upper bound. \(\square\)

# 10. Relation to switching, reconstruction, and relational complexity

Seidel switching and multicolor extensions study equivalence under local transformations of colored complete graphs. Cameron and Tarzi showed a qualitative change beyond two colors. Our question is different: one anonymous value partition is fixed, and we seek a derived low-arity language with the same carrier stabilizer. The shared structural feature is the exceptional binary case.

Tournament \(C_3\)-structure and half-reconstruction study recovery from local subtournaments, often only up to isomorphism or anti-isomorphism. Relation (9) retains labeled local roles and therefore solves a different stabilizer problem.

Cherlin's relational complexity asks for the least arity in a relational representation with a prescribed automorphism group. Our problem has an additional source restriction: relations must be derived from equality among anonymous operation values on bounded-size labeled carrier subsets. Theorem 8 is therefore **not** a claim about unrestricted relational complexity. Its contribution is the exact threshold inside this anonymous-operation equality model.

# 11. Scope

The threshold is structural, not an information-theoretic compression bound. Particular colorings may admit accidental lower-arity reducts. The complete-domain assumption is essential to the binary proof because it guarantees connectivity of the composable-cell graph. Sparse domains may support independent component phases and belong to the companion work.

# 12. Computational verification

The two finite sharpness witnesses were independently re-enumerated. For (7), exhaustive permutation checking gives

\[
|\operatorname{Aut}(T_5)|=1,\qquad |\operatorname{AntiAut}(T_5)|=0,\qquad \tau_3(T_5)=2.
\]

For (13), exhaustive checking of all \(3!\) output permutations confirms that \(g=(0\ 1)\) is not globally color-induced, while direct comparison of all equality relations among ordered cells supported on every carrier subset of size at most three confirms preservation of the full ternary equality passport. These computations verify finite witnesses; the general theorems are proved independently of computation.

# 13. Conclusion

Every complete binary anonymous layer admits an exact ternary equality reduct because a local \(\mathbb Z_2\)-discrepancy propagates across a connected composable-cell graph. With three or more outputs, local color permutations can remain compatible on every three-point overlap without gluing to one global permutation; direct comparison of disjoint cells requires four carrier variables.

Hence, within the anonymous equality-reduct model,

\[
\boxed{q=2:\ 3\text{ variables};\qquad q\ge3:\ 4\text{ variables}.}
\]

The natural next boundary is the sparse-domain regime, where phase propagation becomes componentwise.

# References

1. P. J. Cameron and S. Tarzi, “Switching with more than two colours,” *European Journal of Combinatorics* 25 (2004), 169-177. DOI: 10.1016/S0195-6698(03)00097-0.
2. A. Boussaïri, P. Ille, G. Lopez, and S. Thomassé, “The C3-structure of the tournaments,” *Discrete Mathematics* 277 (2004), 29-43. DOI: 10.1016/S0012-365X(03)00244-9.
3. Y. Boudabbous and G. Lopez, “La relation différence et l'anti-isomorphie,” *Mathematical Logic Quarterly* 41 (1995), 268-280. DOI: 10.1002/malq.19950410213.
4. Y. Boudabbous, A. Boussaïri, A. Chaïchaâ, and N. El Amri, “(≤ k)-half-reconstructible tournaments for k ≤ 6,” *Comptes Rendus Mathématique* 346 (2008), 919-924. DOI: 10.1016/j.crma.2008.07.024.
5. G. Cherlin, “On the relational complexity of a finite permutation group,” *Journal of Algebraic Combinatorics* 43 (2016), 339-374. DOI: 10.1007/s10801-015-0636-8.
6. P. J. Cameron, *Permutation Groups*, London Mathematical Society Student Texts 45, Cambridge University Press, 1999.