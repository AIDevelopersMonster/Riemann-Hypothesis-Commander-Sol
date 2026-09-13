# HATTER-SOL-09 · Canonical typed interfaces

Status: exploratory theorem layer.

## 1. Canonical typed pair

For a nonzero factor alpha, define a unit- and conjugation-invariant pair

\[
\Pi_R(\alpha)=(P_R,Q_R),\qquad P_R\ge Q_R\ge0.
\]

### Square world
For alpha=a+bi,

\[
\boxed{P_G=\max(|a|,|b|),\quad Q_G=\min(|a|,|b|).}
\]

Then

\[
N_G=P_G^2+Q_G^2,\qquad \rho_G=P_G+Q_G.
\]

### Triangular world
For alpha=a+b omega, sort the three numbers

\[
|a|,\ |b|,\ |a-b|.
\]

The largest equals the sum of the other two. Let the smaller two be Q_E<=P_E. Then

\[
\boxed{\Pi_E=(P_E,Q_E)}
\]

is invariant under units and conjugation, and

\[
\boxed{N_E=P_E^2+P_EQ_E+Q_E^2,\qquad \rho_E=P_E+Q_E.}
\]

Thus the scalar world-capacity rho is the forgetful image

\[
(P,Q)\mapsto P+Q.
\]

## 2. World law

Introduce a parameter tau with

\[
eta_tau^2-tau eta_tau+1=0.
\]

Square: tau=0. Triangular: tau=1.

For the same interface pair (P,Q),

\[
\boxed{N_tau(P,Q)=P^2+tau PQ+Q^2.}
\]

Hence the interface counts and the world law are cleanly separated.

Define

\[
S=P+Q,\qquad A=P-Q.
\]

Then

\[
\boxed{N_tau=\frac{(2+tau)S^2+(2-tau)A^2}{4}.}
\]

S is the old scalar capacity; A is a canonical interface imbalance.

## 3. Test network model

For a typed profile ((P_1,Q_1),...,(P_k,Q_k)), use two simple graph layers on the same factor vertices:

\[
G_P=(V,E_P),\qquad G_Q=(V,E_Q),
\]

with

\[
deg_{G_P}(v_j)\le P_j,\qquad deg_{G_Q}(v_j)\le Q_j.
\]

The same pair of factor vertices may carry one P-edge and one Q-edge because the layers are different virtual interfaces. The union support must be connected.

Define

\[
B_P=\sum_j P_j-2|E_P|,\qquad B_Q=\sum_j Q_j-2|E_Q|.
\]

The typed boundary is the vector

\[
\boxed{\mathbf B^{(2)}=(B_P,B_Q).}
\]

This two-layer rule is a test model, not yet final doctrine.

## 4. Uniform typed closure

For k identical nodes of type (P,Q), with k even, full typed closure (0,0) is attainable whenever

\[
\boxed{k\ge P+1.}
\]

For split-prime profiles this is also necessary, because the P-layer cannot realize degree P on fewer than P+1 vertices.

Therefore, if a rational prime p splits and each irreducible factor has canonical pair (P_R(p),Q_R(p)), then p^m has 2m identical typed nodes and

\[
\boxed{\tau_R^{(2)}(p)=\left\lceil\frac{P_R(p)+1}{2}\right\rceil.}
\]

For an inert odd prime, the pair is (p,0) and

\[
\boxed{\tau_R^{(2)}(p)=p+1.}
\]

## 5. Laboratory values

### 7
Square: inert, so

\[
\Pi_G(7)=(7,0),\qquad \tau_G^{(2)}(7)=8.
\]

Triangle: 7=(3+omega)(3+omega^2), and the canonical typed pair of each split factor is

\[
\boxed{\Pi_E(7)=(2,1).}
\]

Hence

\[
\boxed{\tau_E^{(2)}(7)=2.}
\]

### 53
Square: 53=(7+2i)(7-2i), so

\[
\boxed{\Pi_G(53)=(7,2),\qquad \tau_G^{(2)}(53)=4.}
\]

Triangle: inert, so

\[
\boxed{\tau_E^{(2)}(53)=54.}
\]

This improves the scalar square threshold 5 to typed threshold 4 while preserving the huge 4-versus-54 world asymmetry.

## 6. Decisive scalar-collision witness: 37

The prime 37 splits in both worlds.

Square:

\[
37=6^2+1^2,
\qquad
\boxed{\Pi_G(37)=(6,1),\quad \rho_G=7.}
\]

Triangle:

\[
37=7^2-7\cdot3+3^2.
\]

The corresponding canonical adjacent-direction pair is

\[
\boxed{\Pi_E(37)=(4,3),\quad \rho_E=7.}
\]

Therefore the scalar profiles are identical and the scalar HATTER-SOL response cannot distinguish the two worlds:

\[
\mathcal C_G(37)=\mathcal C_E(37)=(7,7).
\]

But the typed profiles differ:

\[
\boxed{(6,1)_\square\ne(4,3)_\triangle.}
\]

Their typed closure exponents are

\[
\boxed{\tau_G^{(2)}(37)=4,\qquad \tau_E^{(2)}(37)=3.}
\]

Hence

\[
\boxed{\text{same scalar capacity response does not imply same typed-network response}.}
\]

This is the cleanest current reason to retain the second interface.

## 7. Open hostile tests

1. Compare the two-layer edge rule with a stricter rule forbidding simultaneous P- and Q-edges on the same vertex pair.
2. Decide whether local direction frames must be restored by unit-group gains on edges.
3. Any final invariant must be switching/gauge invariant if local frames are restored.
4. A future world Laplacian is postponed until natural inter-world maps exist.
5. Prior-art audit must distinguish this arithmetic generation of typed capacities from existing edge-colored b-matching, gain-graph, connection-Laplacian, and sheaf-Laplacian frameworks.
