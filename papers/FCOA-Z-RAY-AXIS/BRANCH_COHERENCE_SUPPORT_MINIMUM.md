# FCOA-Z — Exact Support Minimum for One-Bit Branch Coherence

Status: theorem package v0.1  
Date: 2026-08-31

This note sharpens `BRANCH_COHERENCE_VALUE_RECOVERY.md`.

The previous construction encoded the one-bit connection on the minimal seven-vertex binary carrier using two anonymous terminal outputs on nine defined cells: eight directed cross-branch leaf cells plus the root anchor `(o,o)`.

The question here is whether nine is merely convenient or actually minimal.

Under the natural constraints below, it is exact.

\[
\boxed{\text{minimum connection-independent domain size}=9.}
\]

Moreover the minimum connection-dependent value fiber has four cells.

---

## 1. Group-theoretic setup

Let

\[
T=\{o,u,v,a_0,a_1,b_0,b_1\}
\]

be the complete rooted binary tree of depth two, and let

\[
G=\operatorname{Aut}(T,o,\rho)\cong D_8.
\]

Fix one of the two branch connections

\[
M=\{\{a_0,b_0\},\{a_1,b_1\}\}.
\]

Its stabilizer is

\[
H=\operatorname{Stab}_G(M)\cong C_2\times C_2,
\]

with

\[
[G:H]=2.
\]

We seek a binary terminal-valued partial operation whose definedness does **not** depend on which of the two connection matchings was chosen, but whose values reduce the active group from `G` exactly to `H`.

The two terminal outputs are anonymous, so operation automorphisms are allowed to exchange them unless the value geometry itself forbids the exchange.

---

## 2. Admissible support model

Let

\[
D\subseteq T^2
\]

be the operation domain.

We impose:

1. **connection-independent definedness:** `D` is fixed before choosing `M`;
2. **no definedness leakage of the bit:** `G <= Aut(D)`; equivalently `D` is a union of `G`-orbits in `T^2`;
3. **value-only target:** a distinguished value fiber `F subset D` must satisfy

\[
\operatorname{Stab}_G(F)=H
\]

once output exchange has been disabled internally;
4. the output alphabet has two anonymous terminal elements.

These conditions isolate the incremental cost of storing the coherence bit in values rather than in the domain.

---

## 3. Orbit classification on ordered pairs

The `G ~= D_8` action on `T^2` has orbit sizes

\[
1,
2,2,2,2,
4,4,4,4,4,4,4,4,
8.
\]

The unique size-eight orbit relevant to connection transport is

\[
\boxed{
O_\times=(A\times B)\cup(B\times A),
}
\]

where

\[
A=\{a_0,a_1\},\qquad B=\{b_0,b_1\}.
\]

Thus `O_x` is exactly the eight directed cross-branch leaf cells.

A complete subset-stabilizer check gives the following.

### Lemma 3.1 — Orbit Support Lemma

No subset of any `G`-orbit of size `1`, `2`, or `4` has setwise stabilizer exactly `H`.

Inside the size-eight cross orbit `O_x`, the minimum subset with stabilizer exactly `H` has size four, namely the directed realization of one connection matching:

\[
\boxed{
F_M=
\{(a_0,b_0),(b_0,a_0),(a_1,b_1),(b_1,a_1)\}.
}
\]

Its complement in `O_x` is the directed realization of the other connection matching.

#### Verification

The statement is a finite exact orbit/stabilizer calculation in the eight-element group `D_8`. It is independently reproduced by `verify_branch_coherence_support.py` in this directory.

A conceptual reason for the four-cell minimum is that preserving `H` requires preserving the *whole perfect matching*, not an individual matched edge. A single unordered matched edge has a smaller stabilizer and hence over-rigidifies the carrier; the pair of matched unordered edges is exactly the object whose stabilizer is `H`. Because the operation is on ordered pairs and the branch exchange belongs to `H`, both orientations of each matched edge must be present, giving four ordered cells. □

---

## 4. Minimum domain before output anonymity is considered

### Theorem 4.1 — Eight-Cell Labeled-Output Minimum

If the two terminal outputs were externally distinguished and therefore could not be exchanged, the minimum connection-independent domain supporting exact value stabilizer `H` would be

\[
\boxed{|D|=8,}
\]

and the minimum special fiber would have

\[
\boxed{|F|=4.}
\]

#### Proof

By Lemma 3.1, any `G`-invariant domain containing a fiber with stabilizer `H` must contain the size-eight orbit `O_x`. Taking `D=O_x` and `F=F_M` attains the bound. □

So `8` is the exact domain cost before anonymous-output exchange is taken into account.

---

## 5. Anonymous-output obstruction

For `D=O_x`, the two natural fibers are

\[
F_M
\]

and

\[
O_x\setminus F_M=F_{M'}.
\]

Both have cardinality four.

An element of `G\setminus H` exchanges the two connection choices and hence exchanges these two four-cell fibers. If the two terminal outputs are anonymous, that carrier action can be extended by swapping the two terminal labels.

Therefore the balanced `4+4` coloring fails to reduce the active automorphism group to `H` in the full typed operation.

### Proposition 5.1

With exactly the eight cross cells and two anonymous outputs,

\[
\pi_T Aut(\chi)=G,
\]

not `H`, because connection exchange can be compensated by terminal-output exchange.

Thus at least one additional asymmetry is necessary.

---

## 6. The unique cheapest asymmetry

The action of `G` on `T^2` has exactly one one-point orbit relevant here:

\[
\boxed{\{(o,o)\}.}
\]

The root is fixed by every radial automorphism, so `(o,o)` is a canonical `G`-fixed cell.

Add it to the domain and place it in the same value fiber as `F_M`.

Then the two fiber sizes become

\[
5\quad\text{and}\quad4.
\]

The terminal outputs can no longer be exchanged by any operation automorphism.

### Theorem 6.1 — Exact Nine-Cell Minimum

Under the admissible support model of Section 2, the minimum number of defined cells required to encode and recover exactly one branch-coherence bit with two anonymous terminal outputs is

\[
\boxed{9.}
\]

A minimum realization is

\[
D=O_\times\cup\{(o,o)\},
\]

with value fibers

\[
F_+=F_M\cup\{(o,o)\},
\]

\[
F_-=O_\times\setminus F_M.
\]

Then

\[
|F_+|=5,\qquad |F_-|=4,
\]

and

\[
\pi_T Aut(\chi)=H.
\]

#### Proof

Eight cells are necessary by Theorem 4.1. On those eight cells anonymous-output exchange preserves the full `G` action by Proposition 5.1, so eight cannot suffice.

Any strict enlargement of a `G`-invariant domain adds at least one complete `G`-orbit. The smallest possible additional orbit has size one, and `(o,o)` provides such an orbit. Therefore any successful anonymous-output construction has at least nine defined cells.

The anchored `5+4` construction attains nine and has active stabilizer exactly `H`, as proved in `BRANCH_COHERENCE_VALUE_RECOVERY.md`. □

---

## 7. Exact resource passport

The minimal seven-vertex branch-coherence compiler therefore has the resource passport

\[
\boxed{
\begin{array}{ll}
\text{active carrier}: & 7,\\
\text{connection states}: & 2,\\
\text{coherence information}: & 1\text{ bit},\\
\text{anonymous terminal outputs}: & 2,\\
\text{connection-dependent special cells}: & 4,\\
\text{canonical anti-swap anchor cells}: & 1,\\
\text{total defined cells}: & 9,\\
\text{domain automorphism group}: & D_8,\\
\text{value-preserving active group}: & V_4,\\
\text{Value-Rigidity Index}: & 2.
\end{array}}
\]

This is an exact finite targeted-value-rigidity result.

---

## 8. Why four special cells are not “four bits”

The support size and semantic information are different resources.

The four connection-dependent cells form one orbit-level object: a perfect matching. There are only two admissible such matching fibers compatible with the fixed domain.

Therefore the semantic choice is one bit even though its symmetric representation uses four ordered operation cells.

This is another example of the distinction

\[
\boxed{
\text{support cost}\neq\text{information cardinality}.
}
\]

The same distinction appears throughout the FCOA rigidity programme.

---

## 9. Relation to identity-digraph sparsity

The published Value-Rigidity work asks how sparsely one can destroy **all** active symmetry.

Here the target is weaker and more structured:

\[
D_8\longrightarrow V_4.
\]

So the relevant extremal object is not an identity digraph but a subset with a prescribed nontrivial stabilizer.

This suggests the general quantity

\[
\boxed{
m_G(H;S)=\min\{|F|:F\subseteq S,\ \operatorname{Stab}_G(F)=H\},}
\]

for a permutation `G`-set `S`.

For the cross-branch ordered-pair orbit in the present example,

\[
\boxed{m_{D_8}(V_4;O_\times)=4.}
\]

The branch-coherence theorem is therefore the first explicit **prescribed-stabilizer support** problem in the FCOA line.

---

## 10. Next strike

The seven-vertex problem is now exact at three levels:

1. lift ambiguity = one `C_2` torsor bit;
2. minimum anonymous output alphabet = two;
3. minimum value-only defined support = nine cells, with four connection-dependent cells.

The next mathematically natural generalization is no longer another ad hoc tree. It is the prescribed-stabilizer problem:

\[
\boxed{
\text{determine }m_G(H;S)\text{ for wreath-product branch groups and natural pair orbits }S.
}
\]

For a rooted carrier with branch automorphism group

\[
G=A\wr S_b,
\]

a connection choice corresponds to a subgroup `H` fixing a matching/identification between isomorphic branch fibers. The new question is whether the one-bit `D_8 -> V_4` calculation extends to an exact asymptotic/support law for larger branch multiplicity and deeper wreath products.