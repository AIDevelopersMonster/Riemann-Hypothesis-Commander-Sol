# Reflections on Sparse Multicolor Transport with Commander Sol

## Proper-Coloring Obstructions, Local Phase Groupoids, and Exact Gluing in FCOA

**Alex Malachevsky · Commander Sol**  
**Version:** 0.1 research release candidate  
**Date:** 30 August 2026

## Abstract

We work in the framework of Fixed-Carrier Oriented Algebra (FCOA), as fixed in the foundational Definition 1.0 article, https://doi.org/10.5281/zenodo.22164246. In this paper we study a sparse anonymous multicolor reduct in which a partial terminal layer `c:D->O`, `|O|=q>=3`, is observed only through its defined-cell domain and ternary equality between composable cells. The binary component-phase mechanism does not extend: already for `q=3` there is a connected four-cell layer on three carrier points whose ternary reduct admits a carrier automorphism that induces no local map on colors. We prove that four cells are minimal for a surjective connected q=3 failure and give an explicit extension to every `q>=3`. The correct universal local object is the proper-coloring state of an equality-atom constraint quotient, not an element of `S_q`. We characterize exactly when a local visible-support phase exists, derive its noncommutative composition law in the phase-admissible sector, and prove an exact global gluing criterion. Thus sparse multicolor ternary failure separates into local proper-coloring ambiguity and inter-component gluing ambiguity. In the full-support phase sector we also introduce an abstract point-image synchronization cost and prove `r-1 <= L_q(r) <= (q-1)(r-1)`, leaving exact `L_q(r)` and real operation-cell repair open.

## 1. Introduction

Anonymous outputs look harmless until one asks what a low-arity reduct can actually remember about them. With two terminal values, equality along a connected chain of composable cells propagates a single binary phase: preserve the two fibers or exchange them. That mechanism is exact and underlies the sparse binary phase theory.

Three colors change the problem qualitatively. The obstruction is not merely that `S_q` becomes nonabelian. Before a permutation-valued phase can become noncommutative, it can fail to exist at all.

The reason is combinatorial. Ternary adjacent-cell equality remembers only equality and inequality along composability edges. After equal edges are contracted, what remains is a graph equipped in the hidden full layer with a proper coloring. The ternary reduct remembers the graph but may forget which nonadjacent quotient vertices belonged to the same terminal fiber.

This observation leads to the central chain of this paper:

\[
\boxed{
\text{sparse ternary equality}
\to
\text{equality-atom quotient}
\to
\text{proper-coloring transport}
\to
\text{phase-admissible sector}
\to
\text{visible-support groupoid}
\to
\text{global gluing}.
}
\]

## 2. FCOA framework and the concrete structure used here

The ambient framework is FCOA Definition 1.0 [1]. The active carrier in this paper is a finite set `G`. The auxiliary terminal/output sort is a finite anonymous set `O` of cardinality `q>=3`; its elements carry no distinguished order, arithmetic, cyclic structure, or names. The primitive terminal layer is a partial off-diagonal operation represented by a surjective coloring

\[
c:D\to O,
\qquad
D\subseteq G^2\setminus\Delta_G.
\]

Relative to the canonical FCOA baseline, this paper isolates only the active generic carrier and a sparse terminal-output layer; the internal M0 arithmetic-looking labels are not used as algebraic operations in the proofs. The external orientation encoded by ordered cells is retained in the full sparse layer. Model T then erases terminal names and retains only the domain `D` and ternary equality of terminal values on composable defined cells. Model E, used as a comparison boundary, retains arbitrary-cell equality by a four-variable relation.

The recovery notion is finite carrier reconstruction at the level of automorphism groups: we ask whether the reduct has exactly the same carrier permutations as the full anonymous terminal layer. No external arithmetic is used to generate the structures. Computation is used only for finite verification explicitly identified as such and is not part of the mathematical definition or the proved four-cell minimality theorem.

## 3. Sparse anonymous terminal layers

Let `G` be finite, let

\[
D\subseteq G^2\setminus\Delta_G,
\]

and let

\[
c:D\to O
\]

be surjective. The full anonymous carrier automorphism group is

\[
\operatorname{Aut}^{an}(D,c)
=
\{g\in S_G:gD=D,\ \exists\pi\in S_O,\ c(gp)=\pi(c(p))\ \forall p\in D\}.
\]

Define the undirected comparison graph `Lambda(D)` on vertex set `D`: two distinct cells are adjacent when they are composable in at least one direction.

Model T retains

\[
Q_D(x,y,z)
\iff
(x,y),(y,z)\in D
\text{ and }c(x,y)=c(y,z).
\]

Thus

\[
\mathcal T(D,c)=(G;D,Q_D).
\]

Model E instead retains arbitrary-cell equality

\[
E_D(x,y,u,v)
\iff
(x,y),(u,v)\in D
\text{ and }c(x,y)=c(u,v).
\]

For surjective `c`, Model E is immediately carrier-exact because it records the complete equality partition of the defined cells.

## 4. The sharp four-cell failure

### Theorem 4.1 — minimum connected q=3 phase failure

There exists a surjective three-color sparse layer with connected comparison graph and a Model-T automorphism that induces no local color map. The minimum possible domain size is four.

### Proof

Take

\[
G=\{0,1,2\},
\quad
D=\{(0,1),(0,2),(1,0),(1,2)\},
\]

and set

\[
c(0,1)=c(0,2)=0,
\quad
c(1,0)=1,
\quad
c(1,2)=2.
\]

The comparison graph is connected. Let `g=(0 1)`. It exchanges `(0,1)` with `(1,0)` and `(0,2)` with `(1,2)`. No composable pair has equal color, so `Q_D` is empty and `g` preserves Model T.

If a local color map `phi` existed, the first exchanged pair would force

\[
\phi(0)=1,
\]

while the second would force

\[
\phi(0)=2,
\]

a contradiction.

For minimality, surjectivity onto three colors implies `|D|>=3`. If `|D|=3`, each color occurs exactly once. Any carrier permutation preserving `D` permutes those three cells, and therefore automatically induces a permutation of the three colors. Hence no false Model-T automorphism exists with three cells. Therefore `|D|=4` is minimal. \(\square\)

The witness has

\[
\operatorname{Aut}(G;D,Q_D)\cong C_2,
\qquad
\operatorname{Aut}^{an}(D,c)=1.
\]

## 5. Extension to every q>=3

### Theorem 5.1 — connected-component phase no-go

For every finite `q>=3` there exists a finite surjective anonymous q-color sparse layer with connected comparison graph and a Model-T automorphism for which no local color map exists.

### Proof

Start with Theorem 4.1 and `g=(0 1)`. For every new color `j=3,...,q-1`, add a fresh carrier point `x_j`, fixed by `g`, and exactly two cells

\[
(0,x_j),\qquad(1,x_j),
\]

both colored `j`.

The two new cells are exchanged by `g`. They are not composable with each other, and color `j` occurs nowhere else, so no new equal-colored composable pair is created. They nevertheless join the old comparison component because

\[
(1,0)\sim(0,x_j),
\qquad
(0,1)\sim(1,x_j).
\]

Hence the comparison graph remains connected and `g` remains a Model-T automorphism. The original cells still force both `phi(0)=1` and `phi(0)=2`. Thus no local phase exists. \(\square\)

## 6. Equality atoms and the constraint quotient

Inside a comparison component `C`, retain only those comparison edges whose endpoint cells have equal terminal value. Their connected components are the **T-equality atoms**.

Contract each equality atom to one vertex. Join two distinct atoms when some comparison edge joins their cells. The resulting simple graph is denoted

\[
H_T(C).
\]

Every inter-atom edge is an inequality edge. Therefore the original terminal fibers induce a proper coloring

\[
\kappa_C:V(H_T(C))\to O_C,
\]

where `O_C` is the set of colors visible in `C`.

A Model-T automorphism `g` maps equality atoms to equality atoms and induces

\[
\bar g_C:H_T(C)\to H_T(gC).
\]

Pulling the target coloring back gives another proper coloring of the same abstract source quotient:

\[
\kappa_C^g=\kappa_{gC}\circ\bar g_C.
\]

This is the universal local state transported by Model T.

## 7. Exact local phase criterion

### Theorem 7.1

For a Model-T automorphism `g` and a comparison component `C`, a visible-support bijection

\[
\phi_{g,C}:O_C\to O_{gC}
\]

satisfying

\[
c(gp)=\phi_{g,C}(c(p))
\qquad(p\in C)
\]

exists if and only if

\[
\boxed{
c(p)=c(q)\iff c(gp)=c(gq)\qquad(p,q\in C).}
\]

Equivalently, `kappa_C` and `kappa_C^g` determine the same partition of `V(H_T(C))`, or equivalently lie in the same orbit under relabeling of visible colors.

### Proof

If a bijection `phi` exists, equality and inequality of source colors are preserved. Conversely, if the fiber partition is preserved, define `phi(a)` as the common color of the images of cells of source color `a`. The hypothesis makes this well-defined and injective; finite equal support cardinality gives a bijection. Surjectivity onto `O_C` makes it unique. \(\square\)

A useful sufficient condition is **color-rigidity** of `H_T(C)`: every proper coloring using the actual number of nonempty visible colors has the same color-class partition up to relabeling. Standard unique colorability is the chromatic-minimal special case.

## 8. Why binary is exceptional

For `q=2`, contraction of equality edges in a connected comparison component yields a connected bipartite quotient. Its proper two-color partition is unique up to exchanging the two sides. Thus the proper-coloring orbit is forced and every reduct automorphism has a phase bit.

For `q>=3`, connected graphs may admit inequivalent proper q-color partitions. Therefore connectedness no longer collapses the hidden state.

The phase transition is consequently

\[
\boxed{q=2:\ \text{connected comparison geometry forces a phase orbit},}
\]

\[
\boxed{q\ge3:\ \text{connected comparison geometry need not determine a phase at all}.}
\]

Noncommutativity enters only after this earlier obstruction has been removed.

## 9. The phase groupoid

Assume local phases exist for the relevant component/automorphism pairs. For `g,h` and a component `C`,

\[
h:C\to hC,
\qquad
g:hC\to ghC.
\]

For every `p in C`,

\[
c(ghp)
=
\phi_{g,hC}(\phi_{h,C}(c(p))).
\]

Uniqueness on the visible support gives

\[
\boxed{
\phi_{gh,C}
=
\phi_{g,hC}\circ\phi_{h,C}.
}
\]

The intrinsic object is therefore a groupoid: objects are visible supports `O_C`, arrows are realized support bijections, and composition is the displayed law. Only when every component sees all of `O` can the arrows be identified canonically with elements of `S_O`.

## 10. Exact global gluing

For a phase-admissible automorphism `g`, define

\[
R_g=
\bigcup_C\operatorname{graph}(\phi_{g,C})
\subseteq O\times O.
\]

### Theorem 10.1 — gluing criterion

The following are equivalent:

1. `g` belongs to `Aut^{an}(D,c)`;
2. `R_g` is the graph of a permutation of `O`;
3. local phases agree on every repeated source color and distinct source colors never collide at one target color.

### Proof

A global anonymous permutation restricts to every local phase, proving necessity. Conversely, global surjectivity of `c` makes the first projection of `R_g` all of `O`. Source agreement makes `R_g` a total function and collision-freedom makes it injective. A total injective self-map of finite `O` is a permutation, and it realizes `g` on every defined cell. \(\square\)

Thus ternary exactness is exactly the conjunction of

\[
\boxed{
\text{local fiber-partition preservation}
+
\text{global phase gluing}.
}
\]

## 11. Full-support synchronization cost

Suppose there are `r` comparison components, every component sees the full q-color alphabet, and all relevant reduct automorphisms are phase-admissible. A phase tuple lies in `S_q^r`.

For components `i,j` and a source color `a`, use the primitive point-image constraint

\[
[i,j;a]:\pi_i(a)=\pi_j(a).
\]

Let `L_q(r)` be the minimum number of such constraints forcing **every** satisfying tuple in `S_q^r` to be diagonal.

### Proposition 11.1

\[
\boxed{r-1\le L_q(r)\le(q-1)(r-1).}
\]

### Proof

For the upper bound, take a spanning tree on the r components and, on every tree edge, impose agreement on any `q-1` source colors. Two permutations agreeing on `q-1` points agree everywhere, so the tree synchronizes all phases.

For the lower bound, consider the graph on component indices touched by constraints. If it is disconnected, left-compose all phases in one connected block by the same nonidentity `sigma in S_q`. Every internal equality `pi_i(a)=pi_j(a)` remains true after applying the same injective `sigma` to both sides, while that block can differ from another block. Therefore the constraint graph must be connected and at least `r-1` constraints are necessary. \(\square\)

For `q=2`, this gives the exact value `L_2(r)=r-1`. For `q>=3`, exact `L_q(r)` remains open.

This is an abstract synchronization cost. It is not identified with the number of additional FCOA operation cells.

## 12. A non-vacuous failure

The minimum four-cell witness has empty `Q_D`. The phenomenon is not caused only by vacuity. On the complete off-diagonal domain of three carrier points, there is a surjective three-coloring with nonempty ternary equality and a carrier involution preserving Model T but not the full anonymous coloring.

An exhaustive finite verifier finds no connected non-vacuous q=3 failure below six defined cells and finds one at six. In this version, the six-cell **witness** is used, but its minimality is recorded only as computational evidence and not promoted to a theorem.

## 13. Relation to the arity-four boundary

Model E retains arbitrary-cell equality. Therefore it remembers the complete equality partition of `D`, and every carrier automorphism preserving Model E induces one global output permutation. Hence Model E is exact for every finite q and every sparse domain.

This gives a structural explanation of the ternary/four-ary boundary. Ternary adjacent equality can lose the identification of nonadjacent equality atoms. Four-ary arbitrary-cell equality restores exactly that missing partition.

## 14. Literature boundary

The graph-theoretic language of proper coloring and unique colorability is classical. Switching and gain-graph theories, permutation voltage assignments, colored relational structures, and related group-valued transport form important neighboring literatures. We do not claim those notions as new.

The contribution asserted here is restricted to the FCOA sparse anonymous-operation reconstruction model and to the theorem chain developed for it: equality-atom quotient, proper-coloring transport obstruction, sharp four-cell local-phase failure, conditional visible-support phase groupoid, and exact permutation-graph gluing criterion.

## 15. Open problems

The first clean extremal problem is

\[
\boxed{L_q(r)=?}
\]

for `q>=3`.

A deeper problem is to define and analyze a genuine multicolor real-cell repair cost. Adding operation cells changes the sparse domain and can create new carrier symmetries, so no multicolor analogue of the binary cell-extension invariant is asserted here.

Other questions include the classification of constraint quotients realizable by ordered-cell domains and a proof-level determination of the minimum non-vacuous q=3 failure.

## 16. Conclusion

The binary sparse phase theorem does not generalize by replacing `C_2` with `S_q`. For three or more anonymous outputs, the universal local state is a proper-coloring state, and a permutation phase exists only in a phase-admissible sector. Once that sector is entered, the expected nonabelian composition law appears naturally, but global exactness still requires a separate gluing condition.

Thus the true multicolor transition is not

\[
\text{abelian phase}\to\text{nonabelian phase},
\]

but

\[
\boxed{
\text{automatic binary phase}
\to
\text{proper-coloring transport}
\to
\text{conditional nonabelian phase}.
}
\]

That distinction is the structural content of the sparse q>=3 boundary.

## References

[1] Malachevsky, A. *Fixed-Carrier Oriented Algebra (FCOA): Definition, Typed Partial Operations, Carrier Erasure, and the Canonical M0 Baseline*. Version 1.0, 2026. Zenodo. DOI: 10.5281/zenodo.22164246. https://doi.org/10.5281/zenodo.22164246

[2] Malachevsky, A. *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier*. Zenodo, 2026. DOI: 10.5281/zenodo.22129787.

[3] Malachevsky, A.; Commander Sol. *Reflections on Anonymous Value Geometry with Commander Sol: Low-Arity Rigidity Reducts and an Arity Phase Transition*. Zenodo, 2026. DOI: 10.5281/zenodo.22157403.

[4] Malachevsky, A.; Commander Sol. *Reflections on Sparse Anonymous Phase Geometry with Commander Sol: Component Cocycles, Synchronization Costs, and Actual Cell-Extension Separation*. Zenodo, 2026. DOI: 10.5281/zenodo.22159246.

[5] Harary, F.; Hedetniemi, S. T.; Robinson, R. W. Uniquely colorable graphs. *Journal of Combinatorial Theory* 6 (1969), 264–270.

[6] Zaslavsky, T. Signed graphs. *Discrete Applied Mathematics* 4 (1982), 47–74. DOI: 10.1016/0166-218X(82)90033-6.

[7] Zaslavsky, T. Biased graphs. I. Bias, balance, and gains. *Journal of Combinatorial Theory, Series B* 47 (1989), 32–52. DOI: 10.1016/0095-8956(89)90063-4.

## Publication status

This is a pre-publication research release candidate. It has passed the internal QGE3 hostile mathematical audit. Before Zenodo release, bibliography metadata, theorem numbering, EN/RU synchronization, generated PDF/DOCX files, and final claim audit must be checked. No article DOI has yet been assigned.
