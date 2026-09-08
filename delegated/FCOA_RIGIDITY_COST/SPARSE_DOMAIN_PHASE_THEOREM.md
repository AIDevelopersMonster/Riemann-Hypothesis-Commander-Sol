# FCOA Rigidity Cost — Sparse-Domain Phase Theorem

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** local theorem note for upstream hostile review  
**Scope:** partial/off-diagonal generic domain with exactly two anonymous terminal values  
**Upstream boundary:** this note does not modify G4 or the published M0–G2 checkpoint.

Let

\[
G=G_N,
\qquad
D\subseteq G^2\setminus\Delta
\]

be the defined generic cell domain. Let

\[
c:D\to\{0,1\}
\]

be a temporary coding of the two anonymous terminal value fibers.

The full anonymous carrier group is

\[
\boxed{
\operatorname{Aut}^{\pm}(D,c)
=
\{g\in S_G:gD=D,\ c(gp)=c(p)\ \forall p\in D\}
\cup
\{g\in S_G:gD=D,\ c(gp)=1-c(p)\ \forall p\in D\}.
}
\]

---

## 1. Ordered-cell incidence graph

Define the undirected graph

\[
\Lambda(D)
\]

whose vertex set is D. Two defined cells

\[
p=(x,y),\qquad q=(y,z)
\]

are adjacent whenever both belong to D; we take the underlying undirected adjacency, so composability in either direction suffices.

Let

\[
\pi_0(\Lambda(D))=\{C_1,\dots,C_r\},
\qquad r=\kappa(\Lambda(D)).
\]

Define the derived ternary relation

\[
\boxed{
Q_D(x,y,z)
\iff
(x,y),(y,z)\in D
\text{ and }
c(x,y)=c(y,z).
}
\]

The correct reduct for the sparse problem is the pair

\[
(G;D,Q_D),
\]

because Q alone need not recover the sparse definedness relation.

---

## 2. Componentwise Phase Theorem

### Theorem

Let

\[
A_Q=\operatorname{Aut}(G;D,Q_D).
\]

For every

\[
g\in A_Q
\]

define on each cell p in D

\[
\delta_g(p)=c(gp)\oplus c(p).
\]

Then \(\delta_g\) is constant on every connected component \(C_i\) of \(\Lambda(D)\).

### Proof

If p and q are adjacent in \(\Lambda(D)\), after orienting the adjacency we may write

\[
p=(x,y),\qquad q=(y,z).
\]

Since g preserves both D and Q_D,

\[
c(p)=c(q)
\iff
c(gp)=c(gq).
\]

For binary values this is equivalent to

\[
\delta_g(p)=\delta_g(q).
\]

Constancy propagates along every path in \(\Lambda(D)\). \(\square\)

Thus every reduct automorphism has a well-defined component phase signature

\[
\boxed{
\varepsilon_g=(\varepsilon_g(C_1),\dots,\varepsilon_g(C_r))\in\mathbf F_2^r,
}
\]

where \(\varepsilon_g(C_i)\) is the common discrepancy on component \(C_i\).

---

## 3. Exactness criterion

### Theorem

The sparse ternary reduct is carrier-exact if and only if every realized component phase signature is diagonal:

\[
\boxed{
\operatorname{Aut}(G;D,Q_D)=\operatorname{Aut}^{\pm}(D,c)
}
\]

if and only if

\[
\boxed{
\varepsilon_g\in\{0^r,1^r\}
\qquad\forall g\in A_Q.
}
\]

### Proof

By the Componentwise Phase Theorem, every g in A_Q changes colors by one constant bit on each component. It belongs to the full anonymous layer exactly when that bit is the same on all components, i.e. all zero or all one. \(\square\)

This is the exact replacement for the false naive criterion based only on the number of components.

---

## 4. Connectivity is sufficient, not necessary

If

\[
\Lambda(D)\text{ is connected},
\]

then r=1, so every component phase signature is automatically global. Therefore

\[
\boxed{
\Lambda(D)\text{ connected}
\Longrightarrow
\operatorname{Aut}(D,Q_D)=\operatorname{Aut}^{\pm}(D,c).
}
\]

However the converse is false.

For example, choose any sparse domain D whose carrier automorphism group is already trivial:

\[
\operatorname{Aut}(G,D)=1.
\]

Then

\[
A_Q=1
\]

for every binary coloring c of D, so the reduct is exact regardless of how many components \(\Lambda(D)\) has.

Hence

\[
\boxed{
\kappa(\Lambda(D))-1
}
\]

is **not** the actual carrier repair cost in general.

---

## 5. The phase signature is a cocycle

The component signatures have a natural group-action law.

Every g in A_Q permutes the components of \(\Lambda(D)\). For g,h in A_Q,

\[
\delta_{gh}(p)
=
\delta_h(p)+\delta_g(hp)
\quad\text{in }\mathbf F_2.
\]

Therefore, on components,

\[
\boxed{
\varepsilon_{gh}(C)
=
\varepsilon_h(C)+\varepsilon_g(hC).
}
\]

Thus

\[
\varepsilon:A_Q\to\mathbf F_2^{\pi_0(\Lambda(D))}
\]

is a 1-cocycle for the permutation action of A_Q on the component set.

The full anonymous layer consists exactly of those reduct automorphisms whose cocycle value lies in the diagonal subspace

\[
\boxed{
\Delta=\{0^r,1^r\}\subseteq\mathbf F_2^r.
}
\]

This gives the intrinsic obstruction:

\[
\boxed{
\text{sparse phase defect}
=
\text{non-diagonal realized values of the component phase cocycle}.
}
\]

---

## 6. Realized phase set versus abstract phase capacity

Define the realized phase set

\[
\boxed{
\Sigma(D,c)
=
\{\varepsilon_g:g\in A_Q\}
\subseteq\mathbf F_2^r.
}
\]

Because component permutations may occur, Sigma need not itself be a linear subspace under ordinary coordinatewise addition. The cocycle formulation is the invariant statement.

Nevertheless:

- the **abstract phase capacity** of r disconnected components is \(\mathbf F_2^r\);
- the **globally admissible anonymous phase** is only the diagonal \(\Delta\);
- the **actually realized phase freedom** is Sigma.

Exactness is equivalent to

\[
\boxed{
\Sigma(D,c)\subseteq\Delta.
}
\]

Thus there are three distinct quantities which must not be conflated:

\[
\boxed{
\text{component count}
\neq
\text{abstract phase capacity}
\neq
\text{realized carrier phase freedom}.
}
\]

---

## 7. Why kappa-1 is still a sharp universal synchronization bound

Although

\[
\kappa(\Lambda(D))-1
\]

is not the actual carrier repair cost, it remains the exact worst-case number of independent component links needed to force a single binary phase if one is allowed to add **abstract phase-comparison links** between components.

A spanning tree on r components uses r-1 links and forces all component phase bits equal.

The bound is sharp in the worst case. Consider r disjoint two-cell components supported on disjoint carrier pairs

\[
\{a_i,b_i\},
\]

with

\[
D_i=\{(a_i,b_i),(b_i,a_i)\}
\]

and opposite colors on the two cells. Swapping a_i and b_i realizes an independent phase flip on component i. Hence a subgroup

\[
(C_2)^r
\]

of independent component flips occurs in the ternary reduct. The full anonymous layer permits only the diagonal simultaneous flip. Therefore the phase quotient has r-1 independent binary degrees of freedom, and fewer than r-1 independent equality links cannot universally collapse them.

So:

\[
\boxed{
M_{\rm sync}^{\rm worst}(r)=r-1,
}
\]

but this is a worst-case abstract synchronization theorem, not a formula for every concrete carrier/domain pair.

---

## 8. A refined repair invariant

For a fixed sparse layer, define the **phase-link number**

\[
\lambda(D,c)
\]

as the minimum number of independent component-equality constraints needed to force every realized phase signature in Sigma into the diagonal Delta.

Equivalently, choose pairs of components

\[
(i_1,j_1),\dots,(i_m,j_m)
\]

such that every realized non-diagonal signature violates at least one equality

\[
\varepsilon_{i_s}=\varepsilon_{j_s}.
\]

Then lambda is the minimum such m.

It satisfies

\[
\boxed{
0\le\lambda(D,c)\le r-1.
}
\]

The extremes are both realized:

- lambda=0 when the reduct is already exact, for example if the domain is carrier-rigid;
- lambda=r-1 in the independent-component-flip family above.

This is a finite hitting/synchronization problem on the **realized** phase signatures, not merely on the component graph.

### Important scope caveat

Lambda measures the minimum number of abstract phase links. Turning such links into actual new operation cells is a further FCOA admissibility problem: a new cell changes D, may change the carrier automorphism group, and may merge components in ways not captured by a fixed-domain phase model.

Therefore

\[
\boxed{
\lambda(D,c)
}
\]

is the correct fixed-domain synchronization invariant, while actual operation-cell repair cost requires a second optimization over admissible domain extensions.

---

## 9. Corrected Rigidity-Cost hierarchy

The sparse binary branch now has the following exact hierarchy:

\[
\boxed{
\begin{array}{c}
D\text{ and its carrier automorphisms}\\
\downarrow\\
\Lambda(D)\text{ cell-incidence components}\\
\downarrow\\
Q_D\text{ propagates one phase per component}\\
\downarrow\\
\varepsilon\text{ = realized component phase cocycle}\\
\downarrow\\
\Sigma(D,c)\subseteq\mathbf F_2^r\\
\downarrow\\
\lambda(D,c)\text{ = fixed-domain phase synchronization cost}.
\end{array}}
\]

Connectivity is the simple sufficient case. The cocycle is the general exact invariant.

---

## 10. FCOA passport

- **Carrier/signature:** M0-relative generic sector with sparse off-diagonal domain D.
- **Output alphabet:** exactly two anonymous terminal values.
- **Definedness:** arbitrary sparse D.
- **Derived data:** D plus ternary Q_D.
- **Cell-incidence graph:** Lambda(D).
- **Connected case:** Q_D is carrier-exact.
- **Disconnected case:** exactness iff every realized phase signature is diagonal.
- **General obstruction:** component phase 1-cocycle epsilon.
- **Naive formula kappa-1:** false as concrete carrier cost.
- **Worst-case abstract synchronization cost:** exactly kappa-1.
- **Refined fixed-domain cost:** lambda(D,c), with 0 <= lambda <= kappa-1.
- **Actual operation-cell repair cost:** not identified with lambda without an admissibility/extension analysis.
- **Ordinary arithmetic imported:** no.

---

## 11. Claim firewall

1. The theorem is for two anonymous output fibers. Multicolor sparse domains require an S_q-valued rather than binary phase analysis.
2. Q_D must be considered together with the sparse domain relation D.
3. The component phase cocycle is an exact structural description of the ternary reduct gap.
4. Lambda is a fixed-domain abstract comparison cost, not yet the minimum number of new operation cells.
5. The worst-case r-1 statement is a synchronization bound, not a per-instance formula.
6. No novelty claim is made before literature comparison with gain graphs, switching theory, graph cocycles, and permutation-group extensions.
7. Nothing here changes the status of G4 itself.