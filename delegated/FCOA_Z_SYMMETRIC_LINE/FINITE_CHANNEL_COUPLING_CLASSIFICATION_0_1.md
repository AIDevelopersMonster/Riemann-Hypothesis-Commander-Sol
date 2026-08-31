# FCOA-Z — Finite Channel Coupling Classification 0.1

**Date:** 2026-08-31  
**Status:** PROVED CORE / HOSTILE AUDIT REQUIRED  
**Depends on:** `TERMINAL_OPACITY_AND_UNIFORMITY_INDEPENDENCE_0_1.md`  
**Dimensional gate:** `c_coord = 0`

---

## 1. Problem

In the channel-uniform terminal-lift class, the remaining ambiguity is exactly

\[
(b_+,b_*,b_\times)\in\{0,1\}^3,
\]

with all eight triples realized by the current terminal-opacity theory.

We now ask for the weakest **finite non-spatial coupling** that reduces this ambiguity.

This note first studies the minimal conservative language in which one is allowed only to assert that two terminal channel families have the same lift type.

This is deliberately weaker than terminal re-entry and introduces no new unbounded coordinate.

---

## 2. Equality-coupling graph

Let

\[
C=\{+,*,\times\}
\]

be the finite channel-label set.

A channel-uniform profile is a map

\[
b:C\to\{0,1\}.
\tag{2.1}
\]

Let

\[
G=(C,E)
\]

be a simple undirected graph.

For every edge

\[
\{\alpha,\beta\}\in E
\]

impose the coupling axiom

\[
b_\alpha=b_\beta.
\tag{2.2}
\]

Call the resulting theory the **equality-coupled terminal theory** \(T_G\).

The graph is an auxiliary finite type graph only. It is not a spatial carrier and has no iterative transport.

---

## 3. Connected-component classification

### Theorem 3.1 — Equality-Coupling Classification

A profile

\[
b:C\to\{0,1\}
\]

satisfies \(T_G\) if and only if \(b\) is constant on every connected component of \(G\).

### Proof

If \(b\) satisfies all edge equalities, then along any path

\[
\alpha=v_0-v_1-\cdots-v_r=\beta
\]

we have

\[
b_{v_0}=b_{v_1}=\cdots=b_{v_r},
\]

so \(b\) is constant on connected components.

Conversely, a profile constant on connected components satisfies every edge equality because the endpoints of an edge lie in the same component. \(\square\)

### Corollary 3.2 — Exact profile count

If \(c(G)\) is the number of connected components of \(G\), then

\[
\boxed{N(G)=2^{c(G)}}.
\tag{3.1}
\]

### Proof

Each connected component independently receives one bit, and Theorem 3.1 forces every vertex in that component to carry the same bit. \(\square\)

---

## 4. Complete three-channel phase table

For \(|C|=3\), the possibilities are exact.

### No coupling edges

\[
|E|=0,
\qquad c(G)=3,
\]

so

\[
\boxed{N=8.}
\tag{4.1}
\]

This is the terminal-opacity baseline.

### One coupling edge

\[
|E|=1,
\qquad c(G)=2,
\]

so

\[
\boxed{N=4.}
\tag{4.2}
\]

Exactly two channels are tied and the third remains independent.

### Two distinct coupling edges

Any two distinct edges on three vertices form a connected path, hence

\[
c(G)=1
\]

and

\[
\boxed{N=2.}
\tag{4.3}
\]

The only surviving profiles are global `share` and global `split`.

### Three coupling edges

The triangle is connected, so again

\[
\boxed{N=2.}
\tag{4.4}
\]

The third equality is redundant for profile classification.

---

## 5. Minimal Global Uniformity Theorem

### Theorem 5.1

Within the equality-coupling language, exactly two independent channel-equality constraints are necessary and sufficient to force

\[
\boxed{b_+=b_*=b_\times.}
\tag{5.1}
\]

### Proof

Sufficiency: any two distinct edges connect all three channel vertices, so Theorem 3.1 forces one common bit.

Necessity: with zero edges there are eight profiles; with one edge there are four profiles and the isolated channel can differ from the coupled pair. Hence one equality cannot force global uniformity. \(\square\)

Thus the equality-coupling cost of global uniformity is

\[
\boxed{2.}
\tag{5.2}
\]

---

## 6. Complement symmetry obstruction

Define the global profile complement

\[
\bar b_\alpha=1-b_\alpha
\qquad(\alpha\in C).
\tag{6.1}
\]

### Lemma 6.1

If \(b\) satisfies any family of pure equality constraints

\[
b_\alpha=b_\beta,
\]

then \(\bar b\) satisfies the same family.

### Proof

\[
b_\alpha=b_\beta
\iff
1-b_\alpha=1-b_\beta.
\]

\(\square\)

### Theorem 6.2 — Equality-Only Selection No-Go

No set of pure channel-equality constraints can uniquely select global `share` over global `split`, or global `split` over global `share`.

### Proof

If a globally uniform profile \(b\) satisfies the constraints, its complement \(\bar b\) also satisfies them by Lemma 6.1. The two global profiles are complements of one another and are distinct. \(\square\)

Hence equality coupling can reduce

\[
8\to4\to2,
\]

but never

\[
2\to1.
\]

---

## 7. Anchored coupling

To select one of the two global profiles, add a unary **anchor** on one channel:

\[
b_\alpha=s,
\qquad s\in\{0,1\}.
\tag{7.1}
\]

Here \(s=0\) means `share` and \(s=1\) means `split`.

### Theorem 7.1 — Connected-Plus-Anchor Reconstruction

If \(G\) is connected and one channel is anchored, then the terminal profile is unique.

### Proof

Connectivity forces all channel bits to be equal. The anchor fixes their common value. \(\square\)

### Corollary 7.2 — Unit-cost optimum in the equality-plus-anchor language

If each equality edge and each unary anchor has unit cost, then the minimum cost for a unique global profile is

\[
\boxed{3}
\tag{7.2}
\]

for three channels: two independent equality edges plus one anchor.

### Proof

Two edges are necessary to connect three vertices. One anchor is then necessary by Theorem 6.2 to break complement symmetry. The construction with two path edges and one anchor attains cost three. \(\square\)

This optimality is only for the explicitly defined equality-plus-anchor language; a richer primitive relation could encode more information in one symbol.

---

## 8. General finite-channel theorem

The same argument does not depend on there being three channels.

Let \(C\) be any finite channel set with \(|C|=r\), and let \(G\) be an equality-coupling graph on \(C\).

### Theorem 8.1

The number of admissible binary channel profiles is

\[
\boxed{2^{c(G)}}.
\tag{8.1}
\]

### Corollary 8.2

The minimum number of equality edges required to force global uniformity on \(r\) channels is

\[
\boxed{r-1.}
\tag{8.2}
\]

### Proof

Global uniformity is equivalent to connectedness. A connected graph on \(r\) vertices requires at least \(r-1\) edges, and a spanning tree attains the bound. \(\square\)

### Corollary 8.3

In the equality-plus-anchor language with unit costs, the minimum cost for a unique globally uniform binary profile is

\[
\boxed{r.}
\tag{8.3}
\]

A spanning tree costs \(r-1\), and one anchor breaks the complement symmetry.

---

## 9. Information interpretation

For the three FCOA-Z terminal channels, equality coupling produces an exact ambiguity ladder

\[
\boxed{
8
\xrightarrow{\;1\text{ equality}\;}
4
\xrightarrow{\;1\text{ more equality}\;}
2
\xrightarrow{\;1\text{ anchor}\;}
1.
}
\tag{9.1}
\]

Equivalently, in binary information terms the terminal profile ambiguity decreases from

\[
3\text{ bits}
\to
2\text{ bits}
\to
1\text{ bit}
\to
0.
\tag{9.2}
\]

This is an exact finite reconstruction-cost law inside the declared coupling language.

---

## 10. Relation to the published reconstruction ladder

The published base shadow reconstructs signed carrier geometry but leaves terminal lift type unresolved.

The post-publication results now split that unresolved layer into two stages:

\[
\boxed{
\text{arbitrary radial profile}
\to
\text{channel-uniform profile}
\to
\text{finite channel coupling}
\to
\text{unique terminal profile}.
}
\tag{10.1}
\]

The first reduction requires a radial regularity assumption or theorem.

Once channel uniformity is granted, the remaining coupling problem is finite and classified exactly by Theorem 3.1.

---

## 11. Dimensional status

The graph \(G\) is a finite relation among three terminal channel **types**. It does not create a new source carrier, coordinate, or independently iterable transport.

Therefore

\[
\boxed{c_{coord}=0.}
\]

for every construction in this note.

Matrix size, channel count, and finite graph size are not spatial dimensions.

---

## 12. Prior-art boundary

The graph-theoretic statement that equality constraints propagate along connected components is elementary and not claimed as new.

The FCOA-specific contribution is the identification of the residual terminal-lift ambiguity with three independent channel bits and the resulting exact reconstruction-cost ladder for the audited signed-M0 terminal channels.

No claim is made that binary constraint graphs, spanning-tree bounds, or complement symmetry are new mathematical objects.

---

## 13. Hostile-audit targets

Before publication promotion, verify:

1. the three channel types are structurally distinguished in the signed-M0 language;
2. channel uniformity is explicitly assumed in this note and not smuggled in from the previous independence theorem;
3. `two equalities suffice` is scoped to three channel types;
4. unique selection no-go is scoped to pure equality constraints;
5. the unit-cost optimum `3` is scoped to equality-plus-anchor constraints;
6. no richer single relation is ruled out by the cost theorem;
7. the finite channel graph is not described as a spatial dimension.

---

## 14. Next strike

The equality-coupling class is now completely solved.

The next one-dimensional question is sharper:

\[
\boxed{
\text{Can a structurally natural finite relation break the global share/split complement symmetry without inserting an arbitrary anchor bit?}
}
\]

A successful positive result would need a property already meaningful in FCOA terms, such as:

- minimal output-cardinality;
- faithfulness of branch memory;
- automorphism rigidity;
- preservation of an existing output-channel invariant.

The next strike should compare these candidate selectors and determine whether any one uniquely chooses `share` or `split` from an intrinsic optimization principle.