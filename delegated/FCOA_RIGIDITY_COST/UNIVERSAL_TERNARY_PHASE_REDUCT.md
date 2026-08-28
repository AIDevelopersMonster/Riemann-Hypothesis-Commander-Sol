# FCOA Rigidity Cost — Universal Ternary Phase Reduct

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** local theorem note for upstream hostile review  
**Scope:** complete off-diagonal generic domain, exactly two distinct anonymous terminal values; no tournament assumption  
**Upstream boundary:** this note does not modify G4 or the published M0–G2 checkpoint.

Let

\[
G=G_N,\qquad |G|=n\ge2.
\]

Assume every ordered pair of distinct generic points is defined and takes one of two distinct anonymous terminal values

\[
\Omega_0,\Omega_1.
\]

No relation is assumed between the values of \((x,y)\) and \((y,x)\). Thus for an unordered pair \(\{x,y\}\), all four local possibilities

\[
(\Omega_0,\Omega_0),\quad
(\Omega_0,\Omega_1),\quad
(\Omega_1,\Omega_0),\quad
(\Omega_1,\Omega_1)
\]

are allowed.

Write

\[
c(x,y)\in\{0,1\}
\]

for a temporary binary coding of the two output fibers. The coding itself is not part of the structure: replacing \(c\) by \(1-c\) is the global anonymous-output swap.

Define the full anonymous carrier group

\[
\boxed{
\operatorname{Aut}^{\pm}(c)
=
\{g\in S_G:\ c(gx,gy)=c(x,y)\ \forall x\ne y\}
\cup
\{g\in S_G:\ c(gx,gy)=1-c(x,y)\ \forall x\ne y\}.
}
\]

---

## 1. The universal ternary relation

For \(x\ne y\) and \(y\ne z\), with \(x=z\) allowed, define

\[
\boxed{
Q_\star(x,y,z)
\iff
x\star y=y\star z.
}
\]

Equivalently,

\[
Q_c(x,y,z)
\iff
c(x,y)=c(y,z).
\]

This relation uses only equality of operation values. Neither \(\Omega_0\) nor \(\Omega_1\) is named.

---

## 2. Universal Exactness Theorem

### Theorem

For every complete two-anonymous-output layer on \(G\),

\[
\boxed{
\operatorname{Aut}(G,Q_\star)
=
\operatorname{Aut}^{\pm}(c).
}
\]

Thus one ternary equality relation is a carrier-exact reduct of the entire anonymous two-fiber layer.

### Proof

The inclusion

\[
\operatorname{Aut}^{\pm}(c)
\le
\operatorname{Aut}(Q_c)
\]

is immediate: preserving all colors clearly preserves equality of adjacent colors, and globally swapping the two colors also preserves equality.

For the converse, let

\[
g\in\operatorname{Aut}(Q_c).
\]

For each ordered cell \((x,y)\), \(x\ne y\), define its phase-change bit

\[
\delta_g(x,y)
=
c(gx,gy)\oplus c(x,y)
\in\{0,1\}.
\]

Take any composable ordered cells

\[
(x,y),\qquad(y,z),
\]

with \(x\ne y\) and \(y\ne z\). Since \(g\) preserves \(Q_c\),

\[
c(x,y)=c(y,z)
\iff
c(gx,gy)=c(gy,gz).
\]

For binary values, equality is preserved between two bits exactly when the same phase-change bit is applied to both. Hence

\[
\boxed{
\delta_g(x,y)=\delta_g(y,z).
}
\]

Now form the auxiliary graph \(L_n\) whose vertices are all ordered pairs

\[
D=\{(x,y)\in G^2:x\ne y\},
\]

and join \((x,y)\) to \((y,z)\) whenever \(y\ne z\). We only need connectivity of the underlying undirected graph.

For \(n=2\), the two vertices \((x,y)\) and \((y,x)\) are adjacent by taking \(z=x\).

For \(n\ge3\), every ordered pair \((a,b)\) is connected to every other ordered pair by chaining through shared endpoints; for example one may move

\[
(a,b)\sim(b,u)\sim(u,v)\sim(v,c)\sim(c,d)
\]

with intermediate choices adjusted when endpoints coincide. Equivalently, \(L_n\) is the directed line graph of the complete loopless digraph and is connected.

Since \(\delta_g\) is equal on adjacent vertices of a connected graph, it is constant on all ordered cells:

\[
\delta_g(x,y)\equiv\varepsilon
\qquad\forall x\ne y
\]

for one global

\[
\varepsilon\in\{0,1\}.
\]

If \(\varepsilon=0\), then

\[
c(gx,gy)=c(x,y)
\]

for all ordered cells, so \(g\) is color-preserving.

If \(\varepsilon=1\), then

\[
c(gx,gy)=1-c(x,y)
\]

for all ordered cells, so \(g\) globally exchanges the two anonymous fibers.

Therefore

\[
g\in\operatorname{Aut}^{\pm}(c).
\]

Hence

\[
\operatorname{Aut}(Q_c)=\operatorname{Aut}^{\pm}(c).
\qquad\square
\]

---

## 3. Balancedness is not required

The proof never uses

\[
|c^{-1}(0)|=|c^{-1}(1)|.
\]

Therefore the theorem holds for every **surjective** two-output complete layer, balanced or unbalanced.

If the two fiber cardinalities are unequal, a global output swap may simply fail to be realizable by any carrier permutation. The theorem automatically reflects this: then the second part of \(\operatorname{Aut}^{\pm}(c)\) is empty, and

\[
\operatorname{Aut}(Q_c)=\operatorname{Aut}(c).
\]

Balancedness matters for whether a swap is cardinality-compatible, not for the existence or exactness of the ternary reduct.

---

## 4. Arity optimality

The universal exact arity cannot be reduced to two in the class of anonymous local-pattern reducts.

On two vertices, the anonymous induced pattern records only whether the opposite ordered cells have the same value or different values.

Tournament-type layers give the sharp obstruction: every unordered pair has the same two-point anonymous pattern — the two directions have different values — yet there exist both:

\[
\operatorname{Aut}^{\pm}\cong C_2
\]

for the transitive G4-C tournament, and

\[
\operatorname{Aut}^{\pm}=1
\]

for the rigid tournament family on \(n\ge5\).

Thus no construction determined only by all induced anonymous patterns of arity at most two can universally recover the carrier group.

Since \(Q\) has arity three,

\[
\boxed{
k_{\rm exact}=3}
\]

is optimal in this local anonymous-pattern sense, even without the tournament assumption.

---

## 5. Relation to the previous betweenness reduct

Inside the tournament-type subclass, the earlier relation

\[
B_\star(x,y,z)
\iff
x\star y=y\star z=x\star z
\]

is also exact.

The new relation

\[
Q_\star(x,y,z)
\iff
x\star y=y\star z
\]

is strictly more general and syntactically weaker: it compares only two adjacent cells and makes no assumption about the reverse pair or the third chord \((x,z)\).

Therefore the tournament betweenness theorem is now best viewed as a geometric specialization of the universal phase-propagation theorem.

For G4-C, \(B\) becomes ordinary finite linear betweenness, while \(Q\) is the more primitive adjacent-cell phase relation from which exact anonymous carrier rigidity already follows.

---

## 6. Why four variables are unnecessary

A completely obvious anonymous reduct would compare arbitrary ordered cells:

\[
E((x,y),(u,v))
\iff
x\star y=u\star v.
\]

On the base carrier this is a 4-ary relation and trivially remembers the full partition of ordered cells into two anonymous fibers.

The theorem above shows that this is overkill.

It is enough to retain equality only along composable pairs of cells:

\[
(x,y)\rightsquigarrow(y,z).
\]

Connectivity propagates the relative phase to every ordered cell. Thus

\[
\boxed{
\text{global equality partition on }G^2\setminus\Delta
\text{ is stabilizer-equivalent to one local ternary adjacency relation.}
}
\]

This is the central compression result.

---

## 7. Phase-cocycle interpretation

The proof may be read as a \(\mathbb Z_2\)-phase argument.

A candidate carrier permutation \(g\) induces a local discrepancy

\[
\delta_g:D\to\mathbb Z_2.
\]

Preservation of \(Q\) says that \(\delta_g\) is constant across every adjacency in the ordered-cell line graph. Since that graph is connected,

\[
\delta_g\in H^0(L_n;\mathbb Z_2)
\]

is globally constant.

Hence the only surviving phase freedoms are exactly

\[
0\quad\text{and}\quad1,
\]

corresponding to preservation and global fiber swap.

This cohomological wording is optional intuition; the theorem itself needs only graph connectivity and binary equality.

The connection is structurally reminiscent of switching/two-graph theory, where parity data on small configurations can control global color phase, but no novelty claim is made from that analogy. Classical switching theory uses ternary parity relations in related two-color contexts. See, for example, P. J. Cameron et al., *Switching with more than two colours*, European Journal of Combinatorics 25 (2004), 169–177, DOI `10.1016/S0195-6698(03)00097-0`.

---

## 8. FCOA passport

- **Carrier/signature:** M0 backbone plus complete off-diagonal generic layer with exactly two anonymous terminal outputs.
- **Tournament assumption:** none.
- **Balanced assumption:** none for the theorem; surjectivity onto two outputs is the natural two-fiber setup.
- **Derived reduct:** one ternary relation \(Q_\star\).
- **Definition:** \(Q_\star(x,y,z)\iff x\star y=y\star z\), with \(x\ne y\), \(y\ne z\), and \(x=z\) allowed.
- **External output names:** none.
- **Full generic carrier group:** \(\operatorname{Aut}^{\pm}(c)\).
- **Ternary reduct group:** exactly the same group.
- **Definedness group:** \(S_n\) for the complete generic domain, relative to M0 boundary roles.
- **Commutation:** arbitrary; same-valued reverse cells are allowed.
- **Association Spectrum:** still the complete-domain terminal-layer formula; \(Q\) is derived, not a new operation layer.
- **Small cases:** theorem includes \(n=2\); the connectivity proof handles the two-cell cycle directly.
- **Ordinary arithmetic imported:** no.

---

## 9. Claim firewall

1. The theorem is a structural reduct statement, not a Shannon/minimum-bit compression theorem.
2. Arity optimality is relative to invariants determined from anonymous induced local patterns.
3. The theorem uses exactly two output fibers. More than two anonymous values require a separate analysis because preserving equality of adjacent cells no longer forces a unique global permutation of the color alphabet from a binary phase bit.
4. The complete off-diagonal domain is essential to the simple connectivity argument as stated. Sparse domains require replacing it by connectivity conditions on the corresponding ordered-cell adjacency graph.
5. No novelty claim is made before dedicated literature comparison against binary-relation reconstruction, switching structures, colored digraph reducts, and permutation-group closure theory.
6. Nothing here changes the status of G4 itself.