# FCOA Rigidity Cost — Exact Anonymous Betweenness Reduct

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** local theorem note for upstream hostile review  
**Scope:** complete generic domain, two distinct anonymous terminal outputs, tournament-type opposite fibers  
**Upstream boundary:** this note does not modify G4 or the published M0–G2 checkpoint.

Let

\[
G=G_N,
\qquad |G|=n=N-1.
\]

Assume every ordered pair of distinct generic points is defined and, for each unordered pair \(\{x,y\}\), the two opposite cells receive the two different anonymous terminal outputs.

Choose one output temporarily and write

\[
x\to_T y
\iff
x\star y=\Omega_+.
\]

Then \(T\) is a tournament and the other output fiber is \(T^{\rm op}\). Since the two terminal outputs are anonymous, the carrier group of the generic value layer is

\[
\boxed{
\operatorname{Aut}^{\pm}(T)
=
\{g\in S_G:gT=T\text{ or }gT=T^{\rm op}\}.
}
\]

The temporary choice of which output is called \(\Omega_+\) has no mathematical content.

---

## 1. Definition: anonymous fiber betweenness

For pairwise distinct \(x,y,z\in G\), define

\[
\boxed{
B_\star(x,y,z)
\iff
x\star y=y\star z=x\star z.
}
\]

Only equality of operation values is used; neither terminal output is named.

Equivalently, in tournament language,

\[
B_T(x,y,z)
\]

holds exactly when \(T[\{x,y,z\}]\) is transitive and \(y\) is the middle vertex:

\[
x\to y\to z,\ x\to z,
\]

or after global reversal,

\[
z\to y\to x,\ z\to x.
\]

Therefore

\[
B_T(x,y,z)\iff B_T(z,y,x).
\]

For a cyclic triangle no vertex satisfies the betweenness relation.

---

## 2. The labeled three-point pattern is complete up to global duality

For every 3-set \(X=\{a,b,c\}\), the restriction of \(B_T\) to \(X\) has exactly one of four labeled anonymous forms:

1. no middle vertex — the triple is cyclic;
2. \(a\) is the unique middle vertex;
3. \(b\) is the unique middle vertex;
4. \(c\) is the unique middle vertex.

In each case, the tournament on that fixed labeled triple is determined up to reversal of all three arcs.

Thus \(B_T\) retains more information than the cyclic-triangle hypergraph. The latter is definable from \(B_T\) by

\[
\boxed{
C_3(\{x,y,z\})
\iff
\neg B_T(x,y,z)
\wedge
\neg B_T(y,z,x)
\wedge
\neg B_T(z,x,y).
}
\]

---

## 3. Betweenness Reconstruction Theorem

### Theorem

Let \(T,T'\) be tournaments on the same finite carrier \(G\), with \(|G|\ge2\). Then

\[
\boxed{
B_T=B_{T'}
\iff
T'=T\text{ or }T'=T^{\rm op}.
}
\]

### Proof

The reverse implication is immediate because global reversal preserves the middle vertex of every transitive triple and preserves cyclicity.

Assume

\[
B_T=B_{T'}.
\]

For every 3-subset \(X\subseteq G\), the two tournaments \(T[X]\) and \(T'[X]\) have the same labeled betweenness pattern. Hence there exists a sign

\[
\varepsilon_X\in\{+1,-1\}
\]

such that

\[
T'[X]=T[X]
\]

when \(\varepsilon_X=+1\), and

\[
T'[X]=T[X]^{\rm op}
\]

when \(\varepsilon_X=-1\).

Now suppose two 3-subsets \(X,Y\) share an unordered pair \(\{u,v\}\). Their signs must agree. Indeed, if \(\varepsilon_X\ne\varepsilon_Y\), then the single edge between \(u\) and \(v\) would have to agree with its orientation in \(T\) from one triple and disagree with it from the other, impossible.

For \(|G|\ge4\), the graph whose vertices are the 3-subsets of \(G\), with adjacency when two triples share two vertices, is connected. Therefore all \(\varepsilon_X\) are equal to one global sign \(\varepsilon\).

Hence

\[
T'=T
\]

or

\[
T'=T^{\rm op}.
\]

For \(|G|=3\) there is only one 3-subset, so the conclusion is immediate. For \(|G|=2\), the two possible tournaments are already dual to one another. \(\square\)

---

## 4. Exact stabilizer theorem

### Corollary — stabilizer completeness

For every finite tournament \(T\),

\[
\boxed{
\operatorname{Aut}(G,B_T)
=
\operatorname{Aut}^{\pm}(T).
}
\]

### Proof

Every automorphism or anti-automorphism of \(T\) preserves \(B_T\), so

\[
\operatorname{Aut}^{\pm}(T)
\le
\operatorname{Aut}(B_T).
\]

Conversely, if \(g\in\operatorname{Aut}(B_T)\), then

\[
B_{gT}=g(B_T)=B_T.
\]

By the Betweenness Reconstruction Theorem,

\[
gT=T
\]

or

\[
gT=T^{\rm op}.
\]

Thus \(g\in\operatorname{Aut}^{\pm}(T)\). \(\square\)

In the FCOA complete two-anonymous-output tournament layer, the ternary reduct \((G,B_\star)\) therefore has exactly the same generic carrier automorphism group as the full value layer.

This is stronger than a separator: it is a **carrier-exact reduct**.

---

## 5. Arity minimality in the local anonymous-pattern class

On one generic point there is no orientation information.

On two distinct generic points, the induced tournament-type operation layer always consists of two opposite defined cells carrying two unequal anonymous outputs. Up to the allowed global exchange of the outputs, there is only one local two-point type.

Therefore no invariant determined solely from the induced anonymous operation pattern on at most two generic points can reconstruct an arbitrary tournament layer up to global output swap.

The betweenness reduct is ternary. Hence, in this local labeled-role class,

\[
\boxed{k_{\rm exact}=3}
\]

is optimal.

This does **not** contradict the classical optimal bound \(7\) for tournament half-reconstruction: that literature compares each induced subset only up to abstract isomorphism or converse-isomorphism, whereas \(B_T\) remembers the identities of the vertices and, on a transitive triple, which one is the middle point.

---

## 6. Why the C3-hypergraph is not stabilizer-complete

Let

\[
\mathcal C_3(T)
=\{X\in\tbinom G3:T[X]\cong C_3\}.
\]

Then

\[
\operatorname{Aut}^{\pm}(T)
\le
\operatorname{Aut}(\mathcal C_3(T)),
\]

but equality may fail badly.

### G4-C

For the transitive G4-C tournament,

\[
\mathcal C_3(T)=\varnothing.
\]

Hence

\[
\boxed{
\operatorname{Aut}(\mathcal C_3(T))\cong S_n,
\qquad
\operatorname{Aut}^{\pm}(T)\cong C_2.
}
\]

The full cyclic-triple incidence therefore loses essentially all order information in the transitive case.

### The rigid T5 witness

For

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\},
\]

the cyclic triples are exactly

\[
\{0,1,3\},
\qquad
\{0,2,3\}.
\]

Their 3-uniform hypergraph admits independent swaps

\[
0\leftrightarrow3,
\qquad
1\leftrightarrow2,
\]

so

\[
\boxed{
\operatorname{Aut}(\mathcal C_3(T_5))
\cong C_2\times C_2,
}
\]

whereas

\[
\operatorname{Aut}^{\pm}(T_5)=1.
\]

### Recursive rigid family

Adjoin successive universal sources to \(T_5\), producing the previously constructed rigid family \(T_n\), \(n\ge5\). No new cyclic triangle is created. Thus

\[
\mathcal C_3(T_n)
\]

still has the two hyperedges above, while vertices \(4,5,\dots,n-1\) are isolated in the hypergraph.

Therefore

\[
\boxed{
\operatorname{Aut}(\mathcal C_3(T_n))
\cong
C_2\times C_2\times S_{n-4},
}
\]

and

\[
\boxed{
|\operatorname{Aut}(\mathcal C_3(T_n))|
=4(n-4)!.
}
\]

But the tournament layer remains rigid:

\[
\operatorname{Aut}^{\pm}(T_n)=1.
\]

So the gap between the cyclic-triple hypergraph and the exact anonymous value-layer stabilizer can itself grow factorially.

By contrast,

\[
\operatorname{Aut}(B_{T_n})=1
\]

for every \(n\ge5\).

---

## 7. Exact obstruction identified by the classical C3-structure theorem

The failure of \(\mathcal C_3(T)\) is not mysterious.

Boussaïri, Ille, Lopez and Thomassé proved that two tournaments on the same vertex set have the same \(C_3\)-structure **if and only if** one can be obtained from the other by a sequence of interval inversions. An interval inversion reverses all arcs internal to a tournament interval while leaving the rest unchanged.

Thus

\[
\boxed{
\mathcal C_3\text{ forgets precisely interval-inversion phase information.}
}
\]

For an indecomposable/prime tournament this ambiguity collapses: the same authors prove that equality of \(C_3\)-structures then forces

\[
T'=T
\quad\text{or}\quad
T'=T^{\rm op}.
\]

Consequently, for prime tournaments,

\[
\boxed{
\operatorname{Aut}(\mathcal C_3(T))
=
\operatorname{Aut}^{\pm}(T).
}
\]

The later modular-decomposition treatment of realizable 3-uniform hypergraphs shows that a realizable \(C_3\)-hypergraph and each of its tournament realizations share the same strong modules. This locates the obstruction exactly in the decomposable layers.

Literature:

- A. Boussaïri, P. Ille, G. Lopez, S. Thomassé, *The C3-structure of the tournaments*, Discrete Mathematics 277 (2004), 29–43, DOI `10.1016/S0012-365X(03)00244-9`.
- A. Boussaïri, B. Chergui, P. Ille, M. Zaidi, *3-uniform hypergraphs: modular decomposition and realization by tournaments*, Contributions to Discrete Mathematics 15(1), 121–153, DOI `10.55016/ojs/cdm.v15i1.67935`.

No novelty claim is made for the classical \(C_3\)-structure or interval-inversion results.

---

## 8. Reconciliation with the previous 3-versus-7 hierarchy

The previous branch result distinguished three information regimes:

1. scalar/histogram statistics such as \(\tau_3\);
2. subset-indexed hemimorphism data;
3. the full anonymous value layer.

The betweenness theorem inserts a fourth, stronger local regime:

\[
\boxed{
\text{labeled local role data}.
}
\]

The correct hierarchy is now

\[
\boxed{
\begin{array}{c}
\tau_3\text{ / }M_2
\\[2mm]\downarrow\\[-1mm]
\mathcal C_3(T)\text{ incidence hypergraph}
\\[2mm]\downarrow\\[-1mm]
H_k^{\pm}\text{ histograms}
\\[2mm]\downarrow\\[-1mm]
\text{subset hemimorphism passport }(\le7)
\\[2mm]\downarrow\\[-1mm]
B_T\text{ labeled ternary role reduct}
\\[2mm]\downarrow\\[-1mm]
\{T,T^{\rm op}\}.
\end{array}}
}
\]

The arrows here mean increasing retained structural information, not literal definability in every direction.

The two arity statements are both correct because they concern different data models:

\[
\boxed{
7=\text{optimal arity for abstract half-reconstruction data},
}
\]

where local vertex roles are forgotten up to isomorphism, whereas

\[
\boxed{
3=\text{optimal arity for labeled anonymous role data}.
}
\]

---

## 9. FCOA passport

- **Carrier/signature:** M0 backbone plus complete generic tournament-type terminal layer with two anonymous outputs.
- **New reduct:** one ternary relation \(B_\star\) on the generic carrier.
- **Definition:** \(B_\star(x,y,z)\iff x\star y=y\star z=x\star z\) for distinct generic points.
- **External output names:** none.
- **Full generic carrier group:** \(\operatorname{Aut}^{\pm}(T)\).
- **Betweenness reduct group:** exactly the same group.
- **Definedness group:** \(S_n\) on the complete generic domain, relative to M0 boundary roles.
- **G4-C:** \(B\) is ordinary finite linear betweenness; its group is \(C_2\).
- **Rigid family:** \(\operatorname{Aut}(B)=1\).
- **Small cases:** exhaustive labeled verification completed through \(n=5\).
- **Commutation:** unchanged from the tournament layer.
- **Association Spectrum:** unchanged; \(B\) is a derived invariant, not a new operation cell layer.
- **Ordinary arithmetic imported:** no.

---

## 10. Claim firewall

1. The theorem is stated for the tournament-type complete two-anonymous-output layer.
2. `B` is a derived ternary reduct; it does not reduce raw bit-storage complexity below the original tournament table. `stabilizer-complete compression` here means structural/reduct compression, not Shannon-optimal encoding.
3. Arity-minimality is relative to invariants determined from induced anonymous local patterns.
4. The classical `C3` and interval-inversion theorems are prior art and are cited explicitly.
5. The elementary betweenness reconstruction argument is proved here, but no broad novelty or priority claim is made before a dedicated literature audit for tournament reducts/betweenness relations.
6. Nothing here changes the status of G4 itself.