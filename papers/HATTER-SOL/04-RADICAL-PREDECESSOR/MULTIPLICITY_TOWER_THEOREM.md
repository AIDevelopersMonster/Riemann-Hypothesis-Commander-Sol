# HATTER-SOL-04 · Multiplicity Tower Theorem

## 0. Objective

We study the directed graph on the primes

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1,
\]

which is first-order equivalent, over the multiplicative monoid, to retaining only

\[
\operatorname{rad}(p-1).
\]

The goal is to describe exactly how automorphisms of finite Pratt-height truncations are created, constrained, and either propagated or killed by the next level.

The resulting structure is a **multiplicity tower**.

---

# 1. Pratt height

Define

\[
h(2)=0
\]

and for odd prime \(p\)

\[
h(p)=1+\max_{q\mid p-1}h(q).
\]

Every prime has finite height because every predecessor \(q\mid p-1\) satisfies \(q<p\).

Set

\[
L_n=\{p\in\mathbb P:h(p)=n\},
\qquad
P_{\le n}=\bigcup_{j=0}^{n}L_j.
\]

Every edge strictly increases height:

\[
D(q,p)\Longrightarrow h(q)<h(p).
\]

Hence there are no edges between two vertices of the same level.

Let

\[
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n}).
\]

Since height is graph-theoretically definable by well-founded rank, every automorphism preserves each \(P_{\le n}\).

---

# 2. Exact predecessor fibers at one level

For a finite set

\[
S\subseteq P_{\le n}
\]

with

\[
\max_{q\in S}h(q)=n,
\]

define

\[
X_S
=
\{p\in L_{n+1}:\operatorname{Pred}(p)=S\},
\]

where

\[
\operatorname{Pred}(p)=\{q\in\mathbb P:q\mid p-1\}.
\]

Let

\[
\mu_n(S)=|X_S|\in\{0,1,2,\ldots,\aleph_0\}.
\]

For impossible support sets we simply have \(\mu_n(S)=0\).

Every vertex of \(L_{n+1}\) belongs to exactly one such fiber, so

\[
L_{n+1}=\bigsqcup_S X_S.
\]

---

# 3. One-step extendable subgroup

The group \(G_n\) acts naturally on finite subsets of \(P_{\le n}\):

\[
gS=\{g(q):q\in S\}.
\]

Define

\[
E_n
=
\left\{
 g\in G_n:
 \mu_n(S)=\mu_n(gS)
 \text{ for every admissible finite }S
\right\}.
\]

This is the subgroup of level-\(n\) automorphisms that preserve the complete multiplicity coloring of predecessor sets for the next level.

---

# 4. Multiplicity Tower Theorem

## Theorem 4.1

Let

\[
\rho_n:G_{n+1}\to G_n
\]

be restriction to \(P_{\le n}\). Then:

### (i) Image

\[
\boxed{
\operatorname{im}(\rho_n)=E_n.
}
\]

### (ii) Kernel

\[
\boxed{
\ker(\rho_n)
\cong
\prod_S\operatorname{Sym}(X_S).
}
\]

### (iii) Split exact sequence

There is a noncanonical split exact sequence

\[
\boxed{
1\longrightarrow
\prod_S\operatorname{Sym}(X_S)
\longrightarrow
G_{n+1}
\overset{\rho_n}{\longrightarrow}
E_n
\longrightarrow1.
}
\]

Equivalently, after choosing identifications inside equally sized fibers,

\[
\boxed{
G_{n+1}
\cong
\left(\prod_S\operatorname{Sym}(X_S)\right)
\rtimes E_n.
}
\]

---

# 5. Proof of Theorem 4.1

## 5.1 Necessity of multiplicity preservation

Let \(\widetilde g\in G_{n+1}\), and write

\[
g=\rho_n(\widetilde g).
\]

Take \(p\in X_S\). Since all predecessors of \(p\) lie in \(P_{\le n}\), preservation of edges gives

\[
\operatorname{Pred}(\widetilde g(p))
=
 g(S).
\]

Therefore

\[
\widetilde g(X_S)=X_{gS}.
\]

Hence \(X_S\) and \(X_{gS}\) have equal cardinality:

\[
\mu_n(S)=\mu_n(gS).
\]

Thus

\[
\operatorname{im}(\rho_n)\subseteq E_n.
\]

## 5.2 Sufficiency

Now let \(g\in E_n\).

For every predecessor set \(S\), choose a bijection

\[
\beta_S:X_S\to X_{gS}.
\]

Such a bijection exists because

\[
\mu_n(S)=\mu_n(gS).
\]

Define \(\widetilde g\) on \(P_{\le n+1}\) by

\[
\widetilde g\upharpoonright P_{\le n}=g,
\qquad
\widetilde g\upharpoonright X_S=\beta_S.
\]

This is a bijection because the fibers partition \(L_{n+1}\).

Relations inside \(P_{\le n}\) are preserved because \(g\in G_n\).

There are no edges inside \(L_{n+1}\).

Finally, for \(q\in P_{\le n}\) and \(p\in X_S\),

\[
D(q,p)
\iff
q\in S
\iff
g(q)\in gS
\iff
D(g(q),\beta_S(p)).
\]

Therefore \(\widetilde g\in G_{n+1}\), proving

\[
E_n\subseteq\operatorname{im}(\rho_n).
\]

Thus

\[
\operatorname{im}(\rho_n)=E_n.
\]

## 5.3 Kernel

If \(\widetilde g\in\ker\rho_n\), every vertex of \(P_{\le n}\) is fixed.

Hence a vertex \(p\in X_S\) must stay inside the same fiber \(X_S\), because its complete predecessor set is fixed pointwise.

Conversely, any independent permutation of each \(X_S\) preserves all edges: vertices in one fiber have exactly the same lower neighbors, and there are no edges within \(L_{n+1}\).

Therefore

\[
\ker\rho_n
\cong
\prod_S\operatorname{Sym}(X_S).
\]

## 5.4 Splitting

For each cardinal \(\kappa\) occurring among the fibers, choose a model set \(I_\kappa\). For every \(S\), fix a bijection

\[
\phi_S:X_S\to I_{\mu_n(S)}.
\]

For \(g\in E_n\), define on \(X_S\)

\[
s(g)
=
\phi_{gS}^{-1}\circ\phi_S.
\]

Together with \(g\) on \(P_{\le n}\), this gives an extension in \(G_{n+1}\).

Moreover,

\[
s(gh)|_{X_S}
=
\phi_{ghS}^{-1}\phi_S
=
\left(\phi_{ghS}^{-1}\phi_{hS}\right)
\left(\phi_{hS}^{-1}\phi_S\right),
\]

so

\[
s(gh)=s(g)s(h).
\]

Thus \(s:E_n\to G_{n+1}\) is a section of \(\rho_n\). \(\square\)

---

# 6. Global automorphism group as an inverse limit

Every prime has finite Pratt height, so

\[
\mathbb P=\bigcup_{n\ge0}P_{\le n}.
\]

Restriction therefore gives a canonical map

\[
\operatorname{Aut}(\Pi)
\longrightarrow
\varprojlim_n G_n.
\]

## Theorem 6.1

\[
\boxed{
\operatorname{Aut}(\Pi)
\cong
\varprojlim_n G_n.
}
\]

### Proof

A global automorphism gives a compatible family of finite-height restrictions.

Conversely, a compatible family

\[
(g_0,g_1,g_2,\ldots),
\qquad
\rho_n(g_{n+1})=g_n,
\]

defines a unique permutation of all primes because every prime lies in some \(P_{\le n}\). Compatibility makes this definition independent of the chosen level, and every edge lies in some finite truncation, so the resulting permutation preserves \(D\). \(\square\)

Hence the radical-predecessor structure is rigid exactly when this inverse limit is trivial.

---

# 7. Symmetry birth-and-death law

The tower gives a clean dynamic picture.

Whenever

\[
\mu_n(S)\ge2,
\]

a new local symmetric factor

\[
\operatorname{Sym}(X_S)
\]

is born in \(G_{n+1}\).

That symmetry is invisible to all previous levels, because the vertices in \(X_S\) have identical predecessor sets.

It can only be killed by still higher descendants, through failure to preserve the next multiplicity coloring.

Thus:

\[
\boxed{
\text{symmetry is born inside equal-predecessor fibers}
}
\]

and

\[
\boxed{
\text{symmetry can die only through the arithmetic of future fibers}.}
\]

This is the central structural law of the radical-predecessor problem.

---

# 8. The first nontrivial floor: Fermat-prime symmetry

The height-zero truncation is

\[
P_{\le0}=\{2\},
\]

so

\[
G_0=1.
\]

A prime has height one exactly when

\[
p-1=2^m,
\]

that is, exactly when \(p\) is a Fermat prime.

Let

\[
\mathcal F=X_{\{2\}}
\]

be the set of Fermat primes.

Then

\[
\boxed{
G_1\cong\operatorname{Sym}(\mathcal F).
}
\]

Since at least the five primes

\[
3,5,17,257,65537
\]

belong to \(\mathcal F\), the first nontrivial truncation has substantial symmetry.

The full structure can be rigid only if every nontrivial permutation of these vertices eventually fails to extend coherently through the tower.

---

# 9. Level two as a multiplicity-colored hypergraph on Fermat primes

Every level-two predecessor set has the form

\[
S=\{2\}\cup T,
\]

where \(T\) is a finite nonempty subset of \(\mathcal F\).

Define the color

\[
c(T)
=
\mu_1(\{2\}\cup T).
\]

Then the one-step survivors of the Fermat-prime symmetry are exactly

\[
\boxed{
E_1
=
\operatorname{Aut}(\mathcal F,c),
}
\]

where the right-hand side means permutations \(\sigma\in\operatorname{Sym}(\mathcal F)\) satisfying

\[
c(T)=c(\sigma T)
\]

for every finite nonempty \(T\subseteq\mathcal F\).

Thus the first survival problem is already a colored-hypergraph automorphism problem whose colors are shifted-smooth prime multiplicities.

---

# 10. Small explicit symmetry births

The first few levels already contain equal-predecessor fibers:

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\},
\]

\[
\operatorname{Pred}(7)=\operatorname{Pred}(13)=\{2,3\},
\]

\[
\operatorname{Pred}(29)=\operatorname{Pred}(113)=\{2,7\},
\]

\[
\operatorname{Pred}(59)=\operatorname{Pred}(233)=\{2,29\}.
\]

Their heights are respectively

\[
1,2,3,4.
\]

Therefore \(G_1,G_2,G_3,G_4\) are all nontrivial.

These examples do **not** imply a nontrivial global automorphism. They only show explicitly that local symmetry keeps being born at successive finite heights.

The unresolved question is whether any such symmetry survives all higher multiplicity constraints.

---

# 11. What the theorem reduces the research problem to

The original question

\[
\operatorname{Aut}(\Pi)=1\ ?
\]

is now equivalent to the following survival problem:

> Does there exist a nontrivial compatible sequence
> \[
> g_n\in G_n,
> \qquad
> \rho_n(g_{n+1})=g_n
> \]
> through all Pratt heights?

At each stage two competing processes occur:

1. **birth:** every fiber of multiplicity at least two creates a new symmetric factor;
2. **selection:** only automorphisms preserving the entire next multiplicity coloring can propagate upward.

The hard arithmetic object is therefore not merely the family of numbers \(\mu(S)\) individually, but the full recursively nested coloring

\[
S\mapsto\mu(S)
\]

across all heights.

---

# 12. A sharp caution

It is tempting to argue:

- every finite truncation has nontrivial symmetry;
- therefore the full graph is nonrigid.

This implication is false in general.

A compatible infinite branch through the automorphism tower is required. Nontrivial elements can appear at every finite stage while every particular symmetry dies after finitely many further levels.

Likewise, proving that a fixed automorphism extends to arbitrarily large finite heights is not automatically enough unless the extensions are chosen coherently.

The correct object is the inverse limit, not the collection of finite groups separately.

---

# 13. Next strike

The multiplicity tower exposes the next precise target.

We should now search for a **finite killing witness** for one of the first Fermat-prime transpositions, beginning with

\[
(3\ 5).
\]

Such a witness would be a finite predecessor set \(S\) for which

\[
\boxed{
\mu(S)\ne\mu((3\ 5)S).
}
\]

The easiest possible form would be

\[
\mu(S)=0,
\qquad
\mu((3\ 5)S)>0,
\]

or the reverse.

If no such low-complexity witness appears, the next step is to compute and classify bounded multiplicity profiles for small supports while keeping a strict distinction between:

- certified exact multiplicities;
- lower bounds from found primes;
- unknown/infinite status.

That search can tell us whether the radical structure begins to rigidify immediately or whether the first Fermat symmetry survives surprisingly deep.
