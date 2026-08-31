# FCOA-Z — Minimal Branching Carrier for Non-Abelian Geometric Transport

Status: theorem package v0.1  
Date: 2026-08-31

This note continues `OTIMES_TERMINAL_SYMMETRY_COLLAPSE.md`.

That note showed that a non-Abelian terminal transport group is latent in the symmetry-rich `otimes` reduct but is collapsed by the one-dimensional `oplus` radial memory of the full FCOA-Z axis. It also showed a second obstruction: on a one-dimensional inward chain, one fixed homogeneous transport generator produces only a cyclic history.

The present note asks for the smallest carrier on which **branch geometry itself**, without an external finite-state controller, can supply multiple transport generators and make their order observable.

The answer separates two thresholds:

\[
\boxed{
\begin{array}{ll}
4\text{ vertices} &: \text{smallest rooted carrier with non-Abelian automorphism group},\\
7\text{ vertices} &: \text{smallest rooted carrier with intrinsic noncommuting radial transport history}.
\end{array}}
\]

The second threshold is also the minimum under binary branching.

---

## 1. Rooted radial carriers

A finite rooted tree is a pair

\[
(T,o)
\]

with root `o`. Every non-root vertex `v` has a unique parent

\[
\rho(v),
\]

and radial depth

\[
d(v)=\min\{k:\rho^k(v)=o\}.
\]

We study the rooted radial automorphism group

\[
\operatorname{Aut}(T,o,\rho),
\]

the group of bijections fixing the root and commuting with the parent map.

This is the natural branching replacement for the two-ray radial group used in FCOA-Z.

---

## 2. Classical recursive structure

Let the rooted child-subtrees of the root fall into rooted-isomorphism classes

\[
A_1,\ldots,A_s
\]

with multiplicities

\[
m_1,\ldots,m_s.
\]

Then the rooted automorphism group has the standard recursive form

\[
\operatorname{Aut}(T)
\cong
\prod_{i=1}^s
\left(
\operatorname{Aut}(A_i)^{m_i}\rtimes S_{m_i}
\right).
\]

Thus symmetric groups and wreath products arise exactly from repeated isomorphic branches. This recursive mechanism is classical; the FCOA-Z question is the minimal carrier on which it can drive radial transport.

---

## 3. Absolute automorphism threshold

### Theorem 3.1 — Four-Vertex Non-Abelian Minimum

Among finite rooted trees, the smallest order admitting a non-Abelian rooted automorphism group is

\[
\boxed{|T|=4.}
\]

The unique minimal shape is the rooted three-star: a root with three leaf children. Its automorphism group is

\[
\boxed{S_3}.
\]

#### Proof

For one vertex, the automorphism group is trivial.

For two vertices, the rooted edge has trivial automorphism group.

For three vertices there are only two rooted shapes up to isomorphism relevant to symmetry: a rooted chain, with trivial group, and a root with two leaf children, with group `S_2 ~= C_2`. Both are Abelian.

With four vertices, take a root with three identical leaf children. Any permutation of the three leaves is a rooted automorphism, and every rooted automorphism is such a permutation. Hence

\[
\operatorname{Aut}(T)\cong S_3,
\]

which is non-Abelian. □

### Important limitation

The rooted three-star has depth one. A radial trajectory traverses only one nontrivial parent edge before reaching the root. Therefore the carrier has a non-Abelian ambient symmetry group but cannot yet generate an **ordered product of two geometrically selected transport steps** along one inward path.

Ambient non-Abelianity and noncommuting transport history are different thresholds.

---

## 4. Binary branching threshold

Call a rooted tree binary if every vertex has at most two children.

### Theorem 4.1 — Seven-Vertex Binary Minimum

The smallest binary rooted tree with non-Abelian rooted automorphism group has

\[
\boxed{7\text{ vertices}.}
\]

It is the complete rooted binary tree of depth two:

- the root has two children `u,v`;
- each of `u,v` has two leaf children.

Its rooted automorphism group is

\[
\boxed{
(C_2\times C_2)\rtimes C_2
\cong C_2\wr C_2
\cong D_8,
}
\]

of order `8`.

#### Proof — existence

Each lower cherry has one nontrivial swap, giving `C_2 x C_2`. The root may exchange the two isomorphic cherries, giving another `C_2` which interchanges the two lower factors. Hence the semidirect product above.

#### Proof — minimality

Proceed recursively for binary rooted trees of order at most six.

If the root has one child, the whole automorphism group is the child-subtree automorphism group, so no smaller non-Abelian example is created.

If the root has two nonisomorphic child-subtrees `A,B`, then

\[
\operatorname{Aut}(T)=\operatorname{Aut}(A)\times\operatorname{Aut}(B).
\]

For total order at most six, the child-subtrees have smaller order, and the only nontrivial automorphism group available at order at most three is `C_2`; products arising under the size bound are therefore Abelian.

If the root has two isomorphic child-subtrees `A`, then

\[
|T|=1+2|A|\le6
\]

forces

\[
|A|\le2.
\]

Every rooted tree of order at most two has trivial automorphism group, so

\[
\operatorname{Aut}(T)\cong S_2\cong C_2.
\]

Thus every binary rooted tree on at most six vertices has Abelian automorphism group. The seven-vertex example is minimal. □

---

## 5. Local branch swaps

The seven-vertex tree supplies more than a non-Abelian ambient group.

Let the root children be `u,v`. Let the two leaves under `u` be `a_0,a_1`, and the two leaves under `v` be `b_0,b_1`.

Define three intrinsic local swaps:

- `s_u`: exchange `a_0,a_1` and fix the rest of the tree;
- `s_v`: exchange `b_0,b_1` and fix the rest;
- `r`: exchange the two isomorphic depth-one subtrees, so `u <-> v` and the two cherries are exchanged.

The names `a_0,a_1` are only expository. Intrinsically, `s_u` is the unique nonidentity automorphism supported on the two isomorphic children of `u`, and similarly for `s_v`; `r` is the unique nonidentity automorphism induced by the transposition of the two isomorphic root branches once the two lower subtrees are identified as whole rooted components.

They satisfy

\[
r s_u r^{-1}=s_v.
\]

Because `s_u != s_v`,

\[
\boxed{r s_u\neq s_u r.}
\]

Thus nested local branch swaps are genuinely noncommuting.

---

## 6. Geometry-selected transport along a radial path

The crucial point is that no external state machine is needed to select these generators.

Consider a radial path beginning at a leaf `a` under `u`:

\[
a\longrightarrow u\longrightarrow o.
\]

At each contraction step, inspect the parent just entered.

### Definition 6.1 — intrinsic binary edge transport

If the parent has exactly two isomorphic child-subtrees, associate to the incoming edge the unique local involution that exchanges those two child-subtrees at that parent.

For the path above:

1. the step `a -> u` selects `s_u`;
2. the step `u -> o` selects `r`.

Therefore the ordered radial transport word is

\[
\boxed{r s_u}
\]

if transports act after each inward step in chronological composition convention.

Reversing the order would give

\[
s_u r,
\]

and these are different.

### Theorem 6.2 — Intrinsic Noncommuting Radial History

The complete binary rooted tree of depth two supports a radial path whose successive transport generators are selected entirely by nested branch geometry and do not commute.

#### Proof

The leaf-to-root path traverses two branching parents. The lower parent selects its local child swap `s_u`; the root selects the upper branch swap `r`. Section 5 proves these elements do not commute. No external controller state or branch label is required: each generator is the unique local transposition of the two isomorphic child-subtrees at the parent currently crossed. □

This removes the one-dimensional obstruction found in the axis case. The transport generator is no longer globally fixed; it changes because the path crosses different branching stabilizers.

---

## 7. Seven vertices are also minimal for intrinsic noncommuting path transport

### Theorem 7.1 — Path-Transport Minimum

A finite rooted tree supporting two successive, intrinsically selected, noncommuting local branch transports along one radial path must have at least seven vertices.

The seven-vertex complete binary depth-two tree attains the bound.

#### Proof

To obtain two successive nontrivial local branch transports along one path, the path must cross two distinct branching vertices, say a lower vertex `u` and a higher ancestor `v`.

At `u`, a nontrivial local permutation requires at least two isomorphic child-subtrees. The smallest possibility is two leaf children, so the rooted subtree at `u` has at least three vertices.

For the transport at the higher vertex `v` to fail to commute merely as a consequence of nested branch geometry, `v` must be able to move the entire subtree containing `u` to an isomorphic sibling subtree. Therefore `v` must have at least two isomorphic child-subtrees, each of size at least three.

Hence the subtree rooted at `v` has at least

\[
1+2\cdot3=7
\]

vertices.

The complete binary depth-two tree realizes equality, and Section 6 gives a noncommuting path word. □

### Corollary 7.2

The same number `7` is simultaneously:

- the binary threshold for a non-Abelian rooted automorphism group;
- the absolute threshold for two-level geometry-selected noncommuting radial transport under the local-isomorphic-branch swap principle.

The smaller four-vertex `S_3` star crosses only the first threshold.

---

## 8. FCOA-Z branching transport extension

The preceding statements concern carrier geometry. To connect them back to FCOA, let a boundary output object `y` carry the rooted-tree automorphism action.

For a mixed reduction trajectory

\[
z=z_0\to z_1\to\cdots\to z_k=N(z),
\]

let `g_j` be the intrinsic local branch transport selected by the `j`-th radial step on the surviving output path.

Define the transport word

\[
G(z)=g_{k-1}\cdots g_1g_0.
\]

Then a branch-sensitive boundary extension has the form

\[
\boxed{
F(z)=G(z)\,\beta(N(z)).
}
\]

rather than the scalar-axis form

\[
\nu^{\varepsilon(k)}\beta(N(z)).
\]

The ordered word `G(z)` can now be genuinely non-Abelian.

### Theorem 8.1 — Branching Removes Unary Abelianization

On the seven-vertex minimal branching carrier, there exist radial trajectories for which `G(z)` contains two noncommuting geometry-selected factors. Hence the transport history cannot in general be compressed to a scalar cancellation-depth phase or to powers of one fixed group element.

#### Proof

Use the leaf-to-root path of Section 6. Its transport word contains `s_u` and `r`, with `r s_u != s_u r`. Therefore the path history depends on ordered branch events, not only on path length. □

---

## 9. A new memory invariant: transport word versus depth clock

On the axis, the hidden memory was a scalar phase clock

\[
\varepsilon(k).
\]

On a branching carrier, cancellation depth `k` no longer determines transport.

Two trajectories of the same length may cross different nested branch stabilizers and yield different words in `Aut(T)`.

### Definition 9.1 — branch holonomy word

For a reduction trajectory `z`, define

\[
\mathcal H(z)=G(z)
\]

up to the declared action kernel on the output sort.

This is the natural next invariant after the scalar value-phase `Pi_F`.

### Corollary 9.2

Depth-memory and branch-memory are strictly different resources:

\[
\boxed{
k(z)=k(z')\not\Rightarrow \mathcal H(z)=\mathcal H(z').}
\]

Thus branching creates a genuinely path-sensitive mixed memory rather than a richer encoding of the same unary clock.

---

## 10. Cross-operation coherence question

The `otimes` terminal-symmetry note showed that `oplus` can collapse exchangeability on the axis by recovering radial depth.

On a branching carrier, preserving only the parent map `rho` does **not** kill local swaps of isomorphic child-subtrees: those swaps commute with `rho`.

Therefore the symmetry-collapse theorem changes qualitatively.

### Proposition 10.1

If the only inherited cross-operation memory added to a rooted tree is radial contraction `rho`, then every rooted-tree automorphism remains compatible with that radial memory by definition.

Hence branch automorphisms survive unless another operation distinguishes sibling branches.

This is the first structural reason branching is different from the two-ray axis: radial memory determines depth but does not determine branch identity.

---

## 11. Classical boundary

The recursive appearance of symmetric groups and wreath products in automorphism groups of rooted trees is classical. Wreath products are standard semidirect products, and automorphism groups of regular rooted trees are described through iterated wreath-product structures.

No novelty is claimed for:

- `Aut` of a rooted star being a symmetric group;
- `Aut` of the depth-two binary tree being `C_2 wr C_2`;
- the general rooted-tree wreath recursion.

The FCOA-Z-specific content is the threshold interpretation and transport consequence:

1. distinguish ambient non-Abelian symmetry from observable noncommuting radial history;
2. prove the thresholds `4` and `7` for those two phenomena;
3. identify the seven-vertex binary carrier as the first geometry where successive radial steps select different noncommuting local transports without an external controller;
4. replace the axis phase clock by an ordered branch-holonomy word;
5. observe that radial cross-operation memory no longer collapses branch symmetry because sibling swaps preserve the parent map.

---

## 12. Current conclusion

The preceding frontier was:

\[
\text{find the minimal branching carrier whose geometry can produce genuine noncommuting transport.}
\]

It is now resolved:

\[
\boxed{
\begin{array}{ll}
|T|=4 &: \text{first non-Abelian ambient rooted symmetry }S_3,\\
|T|=7 &: \text{first intrinsic noncommuting radial transport history}.
\end{array}}
\]

For the seven-vertex carrier,

\[
\operatorname{Aut}(T)\cong D_8,
\]

and the radial path itself supplies a noncommuting ordered word.

---

## 13. Next strike

The next question is now sharper than simply enlarging the tree:

\[
\boxed{
\text{what is the smallest FCOA operation signature that can *observe* the branch-holonomy word after carrier erasure?}
}
\]

The carrier geometry can generate `D_8`-valued transport, but publication-level significance requires proving that this ordered word survives in the operational reduct rather than disappearing when the tree relation is erased.

The next theorem package should therefore study **holonomy recoverability**:

- can one recover the branch partition from operation values alone?
- can one distinguish `r s_u` from `s_u r` in the erased reduct?
- what is the minimum number of terminal value fibers required?
- does one-output collapse reappear, forcing at least two or three output colors?

This reconnects the new branching line directly to the earlier FCOA value-rigidity programme.