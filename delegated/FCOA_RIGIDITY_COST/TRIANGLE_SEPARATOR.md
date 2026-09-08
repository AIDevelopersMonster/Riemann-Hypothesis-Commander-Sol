# FCOA Rigidity Cost — Minimal Triangle Separator

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** local theorem note for upstream review  
**Scope:** complete generic domain, exactly two distinct anonymous terminal values, tournament-type opposite fibers  
**Upstream boundary:** this note does not modify G4; it classifies what the first missing invariant must detect.

Let

\[
n=|G_N|=N-1.
\]

For every unordered generic pair \(\{x,y\}\), assume the two ordered cells are defined and receive opposite anonymous values. Write

\[
x\to y
\iff
x\star y=\Omega_+,
\]

so the \(\Omega_+\)-fiber is a tournament \(T\), and the \(\Omega_-\)-fiber is its converse \(T^{\rm op}\).

Because the two outputs are anonymous, the relevant carrier group is

\[
\boxed{
\operatorname{Aut}^{\pm}(T)
=
\{g\in S_n:gT=T\text{ or }gT=T^{\rm op}\}.
}
\]

The full terminal layer is rigid on the generic carrier exactly when

\[
\operatorname{Aut}^{\pm}(T)=1.
\]

---

## 1. Why all current coarse invariants miss the distinction

For any tournament-type complete two-fiber layer:

- generic definedness is complete;
- each anonymous fiber has \(\binom n2\) cells;
- every unordered generic pair has one \(\Omega_+\) direction and one \(\Omega_-\) direction;
- therefore the generic commutation correction is zero;
- by the Terminal Generic Layer Master Lemma, the Association Spectrum depends only on the total number \(n(n-1)\) of new cells.

Thus domain size, output alphabet size, fiber balance, Association Spectrum and commutation cannot distinguish the transitive G4-C coloring from an asymmetric non-self-converse tournament coloring.

The missing information must see how value fibers close around more than one unordered pair at once.

---

## 2. Locality-minimality theorem

Consider invariants built from counts of anonymous isomorphism types of induced \(k\)-vertex value patterns.

### Order 1

There is no internal generic pair, so every one-point induced pattern is identical.

### Order 2

Every two-point tournament layer consists of exactly one \(\Omega_+\) ordered cell and one \(\Omega_-\) ordered cell. Up to swapping the two vertices and globally swapping the two anonymous outputs, there is exactly one two-point type.

Therefore no induced-pattern invariant of order at most two can distinguish any two tournament-type layers.

### Order 3

There are exactly two anonymous three-point tournament types:

1. a transitive triangle;
2. a cyclic triangle \(C_3\).

Define

\[
\boxed{
\tau_3(T)
=
\#\{\{x,y,z\}:T[\{x,y,z\}]\cong C_3\}.
}
\]

The complete three-point profile is

\[
\boxed{
\left(\binom n3-\tau_3(T),\ \tau_3(T)\right).
}
\]

Since the total number of triples is fixed, \(\tau_3\) is the unique independent scalar in the three-point induced-profile count.

Hence:

\[
\boxed{
\text{the first nontrivial anonymous local separator occurs exactly at }k=3.
}
\]

This is the precise sense in which the invariant is minimal. Without specifying an invariant class, arbitrary information can always be encoded into one artificial scalar, so no meaningful absolute minimality statement is made.

---

## 3. G4-C value

The G4-C \(\Omega_+\)-fiber is the transitive tournament induced by the external carrier order.

A tournament is transitive exactly when it contains no cyclic triangle. Therefore

\[
\boxed{\tau_3(G4\text{-}C)=0.}
\]

The residual anonymous-output symmetry is the unique order reversal together with

\[
\Omega_+\leftrightarrow\Omega_-.
\]

Thus

\[
\operatorname{Aut}^{\pm}(T_{\rm tr})\cong C_2.
\]

---

## 4. One cyclic triangle is still not enough

### Theorem — Unique-C3 obstruction

If a tournament \(T\) has exactly one cyclic triangle, then

\[
\operatorname{Aut}(T)\supseteq C_3.
\]

In particular it is not rigid, even before allowing anonymous-output exchange.

### Proof

Let the unique cyclic triangle be

\[
a\to b\to c\to a.
\]

Take any vertex \(x\notin\{a,b,c\}\). If the orientation between \(x\) and the three triangle vertices is mixed, then \(x\) together with two of \(a,b,c\) forms another cyclic triangle:

- if \(x\) dominates exactly one triangle vertex, use that vertex and its outgoing successor on the cycle;
- if \(x\) dominates exactly two triangle vertices, use one of those vertices and the triangle vertex dominating \(x\).

Therefore every outside vertex either dominates all three of \(a,b,c\), or is dominated by all three.

Hence \(\{a,b,c\}\) is a module: every outside vertex sees all three cycle vertices identically. The rotation

\[
a\mapsto b\mapsto c\mapsto a
\]

extended by the identity outside the triangle is an automorphism of \(T\). \(\square\)

So

\[
\tau_3=1
\]

cannot support rigidity.

---

## 5. Exact minimum cyclic-triangle defect for anonymous rigidity

### Theorem — Minimum Triangle Defect

For every \(n\ge5\), among tournament-type complete-domain two-anonymous-output layers satisfying

\[
\operatorname{Aut}^{\pm}(T)=1,
\]

the exact minimum is

\[
\boxed{
\min \tau_3(T)=2.
}
\]

### Lower bound

- If \(\tau_3=0\), then \(T\) is transitive. Its order reversal is an isomorphism \(T\cong T^{\rm op}\), so \(\operatorname{Aut}^{\pm}(T)\) contains a nontrivial element.
- If \(\tau_3=1\), the Unique-C3 obstruction gives a nontrivial \(C_3\le\operatorname{Aut}(T)\).

Thus anonymous rigidity implies

\[
\tau_3\ge2.
\]

### Sharpness at n=5

Use

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}.
\]

Its only cyclic triangles are

\[
\{0,1,3\},
\qquad
\{0,2,3\}.
\]

Hence

\[
\boxed{\tau_3(T_5)=2.}
\]

As proved in the previous rigidity-cost checkpoint, \(T_5\) is asymmetric and non-self-converse, so

\[
\operatorname{Aut}^{\pm}(T_5)=1.
\]

### Sharpness for every n>5

Inductively adjoin a new vertex dominating every old vertex.

The new vertex is the unique source, so every automorphism fixes it and restricts to an automorphism of the old tournament. The construction keeps a source and no sink, so it remains non-self-converse.

Every triple containing the new source is transitive. Therefore no new cyclic triangle is created:

\[
\boxed{
\tau_3(T_n)=2
\qquad\forall n\ge5.
}
\]

Thus the lower bound is attained for every \(n\ge5\). \(\square\)

Exact finite enumeration confirms that no anonymous-rigid tournament layer exists for \(n\le4\); the first case is \(n=5\), corresponding to FCOA \(N=6\).

---

## 6. Equivalent degree-moment invariant

Let

\[
d_+(v)=|\{w\ne v:v\to w\}|.
\]

The first moment is fixed for every tournament:

\[
\sum_v d_+(v)=\binom n2,
\]

so it cannot distinguish G4-C from another tournament layer.

Every transitive triple has a unique source. Hence

\[
\binom n3-\tau_3(T)
=
\sum_v\binom{d_+(v)}2.
\]

Writing

\[
M_2(T)=\sum_v d_+(v)^2,
\]

we obtain

\[
\boxed{
M_2(T)
=
\frac{n(n-1)(2n-1)}6-2\tau_3(T).
}
\]

Equivalently,

\[
\boxed{
\tau_3(T)
=
\frac12\left[
\frac{n(n-1)(2n-1)}6-M_2(T)
\right].
}
\]

The output swap sends

\[
d_+(v)\mapsto n-1-d_+(v),
\]

but because the first moment is fixed, \(M_2\) is unchanged. Therefore \(M_2\) is an anonymous-output invariant.

This gives a second minimality statement:

\[
\boxed{
\text{first degree moment: constant; second degree moment: sufficient.}
}
\]

For G4-C,

\[
M_2=\frac{n(n-1)(2n-1)}6,
\qquad \tau_3=0.
\]

For the rigid family,

\[
M_2=\frac{n(n-1)(2n-1)}6-4,
\qquad \tau_3=2.
\]

The sorted score sequence of the recursive rigid family is

\[
\boxed{
(1,1,2,2,4,5,\dots,n-1).
}
\]

So a constant four-unit second-moment defect, equivalently exactly two cyclic triangles, persists while \(n\) grows.

---

## 7. Constant microscopic defect, factorial rigidity amplification

G4-C and the rigid tournament family have the same:

- complete generic domain;
- two anonymous outputs;
- equal output-fiber sizes;
- generic commutation behavior;
- Association Spectrum.

Yet

\[
\tau_3:\quad 0\longrightarrow2
\]

changes

\[
\operatorname{Aut}^{\pm}:\quad C_2\longrightarrow1.
\]

Relative to complete definedness \(S_n\), the full-operation VRI therefore changes from

\[
\frac{n!}{2}
\]

to

\[
n!.
\]

The striking point is that the extra local defect does **not grow with n**:

\[
\boxed{
\text{two cyclic generic triples are enough for the entire infinite rigid family.}
}
\]

Thus a bounded microscopic value-fiber defect can remove the last global reversal symmetry while the ambient generic carrier grows without bound.

---

## 8. Why Association Spectrum misses what the triangle defect sees

Both invariants involve triples, but they inspect different structure.

The Association Spectrum asks whether

\[
(x\star y)\star z
\quad\text{and}\quad
x\star(y\star z)
\]

exist and agree. Terminal outputs stop the second composition, so the spectrum collapses to a cell-count statistic in this layer.

The triangle defect instead inspects the simultaneous value-fiber pattern on

\[
(x,y),\ (y,z),\ (z,x).
\]

It therefore survives terminality and sees the orientation geometry that associativity cannot.

This suggests the invariant ladder

\[
\boxed{
\text{domain}
\to
\text{fiber sizes}
\to
\text{commutation}
\to
\text{Association Spectrum}
\to
\tau_3\text{ / }M_2
\to
\text{higher fiber-pattern data}.
}
\]

For separating G4-C from the rigid tournament family, the ladder stops at \(\tau_3\).

---

## 9. Small-case passport

| FCOA N | generic n | tournament anonymous rigidity? | minimum tau3 if rigid |
|---:|---:|---|---:|
| 3 | 2 | no | — |
| 4 | 3 | no | — |
| 5 | 4 | no | — |
| 6 | 5 | yes | 2 |
| >=7 | >=6 | yes | 2 |

For \(n=5\), exhaustive labeled enumeration gives an especially sharp finite classification: every anonymous-rigid tournament has exactly two cyclic triangles.

---

## 10. Claim firewall

1. `tau3` / cyclic-triangle structure is standard tournament-theoretic material; no priority claim is made for the invariant itself.
2. The minimum-locality statement is relative to **induced anonymous value-pattern counts**.
3. The exact defect minimum `2` is proved here for tournament-type complete-domain two-anonymous-output FCOA layers; it is not a statement about arbitrary two-fiber colorings with same-valued reverse pairs.
4. `tau3>0` distinguishes G4-C from every rigid tournament layer but does not by itself characterize rigidity; many nontransitive tournaments still have automorphisms or are self-converse.
5. No arithmetic on the external carrier labels is imported.
6. G4 remains an upstream theorem candidate until its own hostile audit.