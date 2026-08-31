# FCOA-Z — Minimal Branching Symmetry, Lift Obstruction, and the First Coherence Bit

Status: theorem package v0.2 — hostile-audit corrected  
Date: 2026-08-31

This note supersedes v0.1 of the same file. The automorphism-group thresholds remain valid, but the earlier claim that an unlabeled seven-vertex binary tree *canonically* selects a noncommuting upper transport lift was too strong. The correction below isolates the missing datum exactly.

## 1. Rooted radial carrier

Let `(T,o)` be a finite rooted tree with parent map `rho`. We study

\[
\operatorname{Aut}(T,o,\rho).
\]

The classical recursive form of a rooted-tree automorphism group is a product of wreath-type factors coming from multiplicities of isomorphic child-subtrees.

## 2. First non-Abelian ambient symmetry

### Theorem 2.1 — Four-Vertex Minimum

The smallest rooted tree with non-Abelian automorphism group has four vertices: a root with three leaf children.

\[
\boxed{\operatorname{Aut}(T)\cong S_3.}
\]

Every rooted tree on at most three vertices has automorphism group `1` or `C_2`, hence Abelian.

So

\[
\boxed{|T|=4}
\]

is the absolute threshold for non-Abelian **ambient** rooted symmetry.

This does not yet give an ordered noncommuting radial transport history: the tree has depth one.

## 3. Binary threshold

### Theorem 3.1 — Seven-Vertex Binary Minimum

Among rooted trees of outdegree at most two, the smallest non-Abelian example has seven vertices: the complete binary tree of depth two.

Let the root children be `u,v`, each carrying a two-leaf cherry. Then

\[
\boxed{
\operatorname{Aut}(T)
\cong
(C_2\times C_2)\rtimes C_2
\cong C_2\wr C_2
\cong D_8.
}
\]

#### Minimality

For a binary rooted tree of order at most six:

- one root child only recurses to a smaller tree;
- two nonisomorphic root subtrees give a direct product of smaller groups;
- two isomorphic root subtrees satisfy `1+2|A|<=6`, hence `|A|<=2`, so `Aut(A)=1` and the only new factor is `C_2`.

Thus every binary rooted tree of order at most six has Abelian automorphism group. □

## 4. The hostile-audit issue: branch permutation versus lift

Let the seven-vertex tree have leaves `a0,a1` under `u` and `b0,b1` under `v`.

The lower local swaps

\[
s_u=(a0\ a1),\qquad s_v=(b0\ b1)
\]

are uniquely defined as automorphisms supported on the corresponding cherries.

At the root, however, there is a crucial distinction.

The transposition

\[
\bar r:\{T_u,T_v\}\to\{T_u,T_v\}
\]

of the two **branch blocks** is unique.

But a lift of `bar r` to a vertex automorphism of the full tree is not unique, because an isomorphism

\[
T_u\to T_v
\]

may be composed with an automorphism of the target cherry.

Since

\[
\operatorname{Aut}(T_u)\cong C_2,
\]

there are exactly two rooted isomorphisms `T_u -> T_v`, and correspondingly several full-tree lifts of the block transposition.

Therefore the unlabeled tree canonically determines the block swap but **not a unique leaf-level element `r`**.

This invalidates the stronger v0.1 phrase “geometry alone uniquely selects `r`”.

## 5. Lift Torsor Theorem

### Theorem 5.1

Let `A` and `B` be isomorphic rooted subtrees. The set

\[
\operatorname{Iso}(A,B)
\]

of rooted isomorphisms from `A` to `B`, if nonempty, is a torsor under `Aut(A)` on the right and under `Aut(B)` on the left.

#### Proof

Fix one isomorphism `f:A->B`. Every other isomorphism `g:A->B` has

\[
f^{-1}g\in\operatorname{Aut}(A),
\]

so `g=f alpha` for a unique `alpha in Aut(A)`. The left-action statement is analogous. □

### Corollary 5.2 — Minimal binary lift ambiguity

For the seven-vertex binary tree, each upper branch-lift choice is a torsor over

\[
C_2.
\]

Hence selecting a definite upper lift requires exactly

\[
\boxed{1\text{ coherence bit}.}
\]

This bit is not a depth phase. It identifies corresponding internal points across two isomorphic sibling subtrees.

## 6. Canonical-selection obstruction

A second way to see the problem is by symmetry.

### Proposition 6.1

A globally canonical choice of an element of `Aut(T)` from the unlabeled rooted tree alone must be fixed under conjugation by every automorphism of `T`; hence it must lie in

\[
Z(\operatorname{Aut}(T)).
\]

#### Proof

If a selection rule depends only on the isomorphism type of the rooted tree, applying any automorphism `h` to the same object cannot change the selected element. Equivariance therefore gives

\[
hgh^{-1}=g
\]

for all `h`, which is exactly centrality. □

For the minimal binary tree,

\[
\operatorname{Aut}(T)\cong D_8
\]

and its center has order two. Thus the bare unlabeled carrier cannot canonically select a pair of noncommuting automorphisms.

This is a structural obstruction, not merely a notation issue.

## 7. What one coherence bit buys

Choose one rooted isomorphism

\[
\phi:T_u\to T_v.
\]

This is the minimal **connection datum** between the two isomorphic root branches.

It determines a preferred lift `r_phi` of the root block transposition by

- using `phi` from `T_u` to `T_v`;
- using `phi^{-1}` from `T_v` to `T_u`.

Then

\[
r_\phi s_u r_\phi^{-1}=s_v,
\]

so

\[
\boxed{r_\phi s_u\neq s_u r_\phi.}
\]

Therefore the seven-vertex carrier plus one coherence bit supports a definite noncommuting transport word.

## 8. Corrected threshold table

The valid hierarchy is

\[
\boxed{
\begin{array}{lll}
4\text{ vertices} &:& \text{first non-Abelian ambient rooted symmetry }S_3,\\
7\text{ vertices} &:& \text{first binary non-Abelian ambient symmetry }D_8,\\
7\text{ vertices}+1\text{ bit} &:& \text{first definite nested noncommuting transport lift.}
\end{array}}
\]

The earlier claim that the last line required zero extra coherence has been withdrawn.

## 9. General coherence-cost principle

The minimal case suggests the correct general invariant.

Suppose a radial path enters a parent having two isomorphic child-subtrees of type `A`. The branch-block transposition is visible at the quotient level, but lifting it to a pointwise transport requires choosing an element of the torsor

\[
\operatorname{Iso}(A,A').
\]

Once one reference isomorphism is fixed, the ambiguity is exactly `Aut(A)`.

Thus the natural finite coherence cost is

\[
\boxed{
C_{\rm lift}(A)=\log_2 |\operatorname{Aut}(A)|
}
\]

bits when the automorphism group is finite, up to the usual integer coding convention.

For the cherry `A`, `|Aut(A)|=2`, giving one bit.

This is not yet an information-theoretic optimality theorem for arbitrary FCOA encodings; it is the exact cardinality of the lift torsor.

## 10. Connection versus carrier memory

The new bit is categorically different from the scalar phase bit found on the axis.

### Axis phase

The carrier already has a canonical reflection; the hidden memory chooses whether to apply it after `k` cancellation steps:

\[
\nu^{\varepsilon(k)}.
\]

### Branch coherence

The branch block permutation exists canonically, but its lift through internally symmetric subtrees is ambiguous. The memory chooses a **matching/isomorphism between sibling fibers**.

So the two resources are

\[
\boxed{
\text{depth phase memory}\neq\text{branch coherence memory}.
}
\]

## 11. Consequence for FCOA holonomy

A genuine branch-holonomy word

\[
G(z)=g_{k-1}\cdots g_0
\]

cannot be defined from the unlabeled rooted carrier alone whenever some required branch permutation has a nontrivial lift torsor.

It becomes well-defined only relative to a declared connection/coherence structure.

The correct FCOA extension problem is therefore not

> “does branching alone produce a canonical non-Abelian phase?”

but

> “how little connection data is needed before branching supports noncommuting transport, and can that connection later be recovered from the operation table after erasure?”

For the smallest binary carrier, the first answer is exact:

\[
\boxed{1\text{ bit}.}
\]

## 12. Classical boundary

The rooted-tree wreath-product recursion and the fact that isomorphism sets are torsors under automorphism groups are classical group-action facts. Wreath products are standard semidirect products; regular rooted-tree automorphism groups are classically described by iterated wreath constructions.

The FCOA-Z-specific contribution here is the memory interpretation:

1. separating branch-block symmetry from pointwise lift;
2. identifying the false-canonical-lift trap;
3. locating the minimal seven-vertex binary carrier;
4. proving that its first lift ambiguity is exactly a `C_2` torsor;
5. identifying one bit as the first branch-coherence resource beyond the axis phase hierarchy.

## 13. Next strike — recoverability of the coherence bit

The next question is now precise:

\[
\boxed{
\text{can the one-bit branch connection be erased from the carrier presentation and recovered from FCOA operation values?}
}
\]

This is stronger than merely storing the bit externally.

The minimum-value problem should ask:

- one terminal output cannot encode incremental value-rigidity beyond definedness;
- are two anonymous terminal values sufficient to recover the chosen lift `phi` on the seven-vertex carrier?
- can the two possible lifts be distinguished without rigidifying the entire carrier?
- what is the exact stabilizer index of a one-bit connection fiber?

This reconnects branching holonomy directly to the published Value-Rigidity / Identity-Digraph line.