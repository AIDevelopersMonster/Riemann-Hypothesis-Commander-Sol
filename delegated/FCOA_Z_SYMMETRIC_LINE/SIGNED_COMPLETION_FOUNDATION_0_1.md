# FCOA-Z Signed Completion Foundation 0.1

**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** PROVED FOUNDATION PACKAGE / NOT YET PUBLICATION CLAIM  
**Date:** 2026-08-30

---

## 1. Starting ray and symmetric completion

Let the original rooted coordinate ray be

\[
R=\{P_0,P_1,P_2,\ldots\}.
\]

Define its symmetric completion as the disjoint union

\[
B^{\pm}
=
\{P_0\}
\sqcup
\{P_n^+:n\ge1\}
\sqcup
\{P_n^-:n\ge1\}.
\tag{1}
\]

The symbols `+` and `-` in \(P_n^\pm\) are branch labels only. No binary addition or multiplication is part of the structure.

Define a successor permutation \(S:B^{\pm}\to B^{\pm}\) by

\[
S(P_0)=P_1^+,
\tag{2}
\]

\[
S(P_n^+)=P_{n+1}^+
\qquad(n\ge1),
\tag{3}
\]

\[
S(P_1^-)=P_0,
\tag{4}
\]

\[
S(P_n^-)=P_{n-1}^-
\qquad(n\ge2).
\tag{5}
\]

Define \(P=S^{-1}\). Explicitly,

\[
P(P_0)=P_1^-,
\tag{6}
\]

\[
P(P_n^-)=P_{n+1}^-
\qquad(n\ge1),
\tag{7}
\]

\[
P(P_1^+)=P_0,
\tag{8}
\]

\[
P(P_n^+)=P_{n-1}^+
\qquad(n\ge2).
\tag{9}
\]

Define the strict order by

\[
\cdots<P_3^-<P_2^-<P_1^-<P_0<P_1^+<P_2^+<P_3^+<\cdots.
\tag{10}
\]

Finally define the zero reflection

\[
\nu(P_0)=P_0,
\tag{11}
\]

\[
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+
\qquad(n\ge1).
\tag{12}
\]

---

## 2. Signed Completion Theorem

### Theorem 2.1

The pointed oriented successor structure

\[
\mathcal Z_F=(B^{\pm};P_0,S,P,<,\nu)
\]

is canonically isomorphic to the ordinary pointed oriented integer line

\[
(\mathbb Z;0,s,p,<,-),
\]

where

\[
s(k)=k+1,
\qquad
p(k)=k-1,
\qquad
-(k)=-k.
\]

The isomorphism is

\[
\phi(P_0)=0,
\tag{13}
\]

\[
\phi(P_n^+)=n,
\qquad
\phi(P_n^-)=-n
\qquad(n\ge1).
\tag{14}
\]

This theorem identifies only the pointed oriented-line structure. It does not place binary integer addition or multiplication into the FCOA signature.

### Proof

The sets in (1) are pairwise disjoint, so (13)-(14) define a function. Every integer is either \(0\), a unique positive integer \(n\), or a unique negative integer \(-n\) with \(n\ge1\). Hence \(\phi\) is bijective.

We verify successor preservation.

For the origin,

\[
\phi(S(P_0))=\phi(P_1^+)=1=s(0)=s(\phi(P_0)).
\]

For \(n\ge1\),

\[
\phi(S(P_n^+))
=\phi(P_{n+1}^+)
=n+1
=s(n)
=s(\phi(P_n^+)).
\]

For \(P_1^-\),

\[
\phi(S(P_1^-))
=\phi(P_0)
=0
=s(-1)
=s(\phi(P_1^-)).
\]

For \(n\ge2\),

\[
\phi(S(P_n^-))
=\phi(P_{n-1}^-)
=-(n-1)
=-n+1
=s(-n)
=s(\phi(P_n^-)).
\]

Therefore

\[
\phi\circ S=s\circ\phi.
\tag{15}
\]

Since \(P=S^{-1}\) and \(p=s^{-1}\), (15) implies

\[
\phi\circ P=p\circ\phi.
\tag{16}
\]

The order in (10) is sent exactly to the standard order on \(\mathbb Z\), so \(\phi\) is order preserving and reflecting.

Finally,

\[
\phi(\nu(P_0))=0=-0=-\phi(P_0),
\]

and for \(n\ge1\),

\[
\phi(\nu(P_n^+))=\phi(P_n^-)=-n=-\phi(P_n^+),
\]

\[
\phi(\nu(P_n^-))=\phi(P_n^+)=n=-(-n)=-\phi(P_n^-).
\]

Thus

\[
\phi\circ\nu=(-)\circ\phi.
\tag{17}
\]

Hence \(\phi\) is an isomorphism of the declared pointed oriented-line structures. \(\square\)

---

## 3. Reflection Characterization

### Proposition 3.1

There is exactly one map \(r:B^{\pm}\to B^{\pm}\) satisfying

\[
r(P_0)=P_0
\tag{18}
\]

and

\[
r\circ S=P\circ r.
\tag{19}
\]

It is the reflection \(\nu\) defined in (11)-(12).

### Proof

First, \(\nu\) satisfies (18). Direct inspection of (2)-(9) gives

\[
\nu S=P\nu,
\]

so existence holds.

For uniqueness, let \(r\) satisfy (18)-(19). For every \(n\ge1\),

\[
P_n^+=S^n(P_0).
\]

Repeated use of (19) yields

\[
r(P_n^+)
=r(S^n(P_0))
=P^n(r(P_0))
=P^n(P_0)
=P_n^-.
\]

Likewise

\[
P_n^-=P^n(P_0).
\]

Equation (19) is equivalent, because \(P=S^{-1}\), to

\[
rP=Sr.
\]

Therefore

\[
r(P_n^-)
=r(P^n(P_0))
=S^n(r(P_0))
=S^n(P_0)
=P_n^+.
\]

Together with \(r(P_0)=P_0\), this forces \(r=\nu\). \(\square\)

### Corollary 3.2

\[
\nu^2=\operatorname{id}_{B^{\pm}}.
\]

### Proof

Immediate from (11)-(12), or by applying Proposition 3.1 twice. \(\square\)

---

## 4. Coordinate Rigidity

### Theorem 4.1

The pointed successor structure

\[
(B^{\pm};P_0,S)
\]

has trivial automorphism group:

\[
\boxed{\operatorname{Aut}(B^{\pm};P_0,S)=1.}
\tag{20}
\]

The same is therefore true for any expansion retaining \(P_0\) and \(S\), including

\[
(B^{\pm};P_0,S,P,<,\nu).
\]

### Proof

Let \(f\) be an automorphism preserving \(P_0\) and \(S\). Then

\[
f(P_0)=P_0.
\]

For every \(n\ge1\),

\[
P_n^+=S^n(P_0),
\]

hence

\[
f(P_n^+)
=f(S^n(P_0))
=S^n(f(P_0))
=S^n(P_0)
=P_n^+.
\]

Since \(S\) is bijective, every automorphism preserving \(S\) also preserves its inverse \(P=S^{-1}\). Thus

\[
P_n^-=P^n(P_0)
\]

implies

\[
f(P_n^-)=P_n^-.
\]

Therefore every element is fixed and \(f=\operatorname{id}\). \(\square\)

### Interpretation

The signed completion is coordinate-rigid once the origin and oriented unit step are retained. This is a rigidity statement only. It is **not** an assertion that binary addition or multiplication is first-order definable in every reduct considered later.

---

## 5. Symmetry after coordinate erasure

Transporting through the isomorphism \(\phi\), write

\[
T_c(k)=k+c
\qquad(c\in\mathbb Z)
\tag{21}
\]

for translations and

\[
R_c(k)=c-k
\qquad(c\in\mathbb Z)
\tag{22}
\]

for reflections of the undirected integer line.

### Theorem 5.1 — successor without origin

\[
\boxed{
\operatorname{Aut}(B^{\pm};S)\cong(\mathbb Z,+).
}
\tag{23}
\]

Every automorphism is a unique translation \(T_c\).

### Proof

Let \(f\) commute with successor. Put

\[
c=\phi(f(P_0)).
\]

For every integer \(n\), every carrier point is \(S^n(P_0)\), interpreting negative powers through \(S^{-1}\). Hence

\[
f(S^n(P_0))=S^n(f(P_0)).
\]

Applying \(\phi\),

\[
\phi(f(\phi^{-1}(n)))=n+c.
\]

Thus \(f=T_c\), and every \(T_c\) clearly preserves successor. \(\square\)

### Theorem 5.2 — order without origin

\[
\boxed{
\operatorname{Aut}(B^{\pm};<)\cong(\mathbb Z,+).
}
\tag{24}
\]

Every order automorphism is a unique translation.

### Proof

In the discrete order type \(\mathbb Z\), successor is definable from `<` by

\[
\operatorname{Succ}(x,y)
\iff
x<y\land\neg\exists z\,(x<z<y).
\tag{25}
\]

Therefore every order automorphism preserves successor. Theorem 5.1 applies. Conversely every translation preserves order. \(\square\)

### Theorem 5.3 — undirected adjacency without origin

Let

\[
A(x,y)
\iff
(y=S(x))\lor(x=S(y)).
\tag{26}
\]

Then

\[
\boxed{
\operatorname{Aut}(B^{\pm};A)\cong D_\infty,
}
\tag{27}
\]

the infinite dihedral group. Its elements are exactly the translations \(T_c\) and reflections \(R_c\).

### Proof

The graph \((B^{\pm};A)\) is the bi-infinite path. An automorphism is determined by the image of one vertex and the image of one of its two neighbours. After choosing the image of \(0\), there are exactly two choices for which adjacent direction corresponds to `+1`: preserve orientation, yielding a translation, or reverse it, yielding a reflection. All maps (21)-(22) preserve adjacency. \(\square\)

### Theorem 5.4 — rooted undirected line

\[
\boxed{
\operatorname{Aut}(B^{\pm};P_0,A)\cong C_2.
}
\tag{28}
\]

The two automorphisms are the identity and zero reflection \(\nu\).

### Proof

By Theorem 5.3 an automorphism is a translation or reflection. A translation fixing zero has \(c=0\), hence is the identity. A reflection \(R_c(k)=c-k\) fixes zero iff \(c=0\), giving \(k\mapsto-k\), namely \(\nu\). \(\square\)

### Corollary 5.5 — rooted order

\[
\operatorname{Aut}(B^{\pm};P_0,<)=1.
\tag{29}
\]

### Proof

By Theorem 5.2 every order automorphism is a translation; the only translation fixing the origin is the identity. \(\square\)

### Corollary 5.6 — successor plus reflection

\[
\operatorname{Aut}(B^{\pm};S,\nu)=1.
\tag{30}
\]

### Proof

By Theorem 5.1 every successor automorphism is \(T_c\). Commutation with zero reflection requires

\[
T_c(-n)=-(T_c(n))
\]

for all \(n\), hence

\[
-n+c=-n-c,
\]

so \(c=0\). \(\square\)

---

## 6. Exact erasure table

For the signed base line alone:

| Retained structure | Automorphism group | Lost information |
|---|---:|---|
| \(P_0,S\) | \(1\) | none of absolute signed coordinate |
| \(P_0,<\) | \(1\) | explicit unit-step symbol, but discrete order recovers it |
| \(S,\nu\) | \(1\) | named origin, but it is recovered as the unique fixed point of \(\nu\) |
| \(S\) | \(\mathbb Z\) | absolute origin |
| \(<\) | \(\mathbb Z\) | absolute origin |
| \(P_0,A\) | \(C_2\) | orientation/sign naming |
| \(A\) | \(D_\infty\) | origin and orientation |

This is the first exact symmetry ledger for FCOA-Z.

---

## 7. Symmetric finite windows

For \(N\ge0\), define

\[
W_N
=
\{P_0\}
\cup
\{P_n^+,P_n^-:1\le n\le N\}.
\tag{31}
\]

Thus

\[
|W_N|=2N+1.
\tag{32}
\]

Define the finite successor relation by restriction of the infinite successor graph:

\[
S_N(x,y)
\iff
x,y\in W_N\land y=S(x).
\tag{33}
\]

Equivalently, if successor is represented as a partial function on \(W_N\), then it is undefined only at \(P_N^+\); predecessor is undefined only at \(P_N^-\).

There is no wrap-around.

### Proposition 7.1 — window coherence

For \(M\le N\),

\[
W_M\subseteq W_N
\]

and

\[
S_M=S_N\cap(W_M\times W_M).
\tag{34}
\]

Likewise the restricted order, adjacency, origin and reflection relations/functions agree exactly on old points.

### Proof

All finite structures are literal restrictions of the single infinite structure \(\mathcal Z_F\). Therefore every old tuple keeps the same truth/value whenever all members of the tuple remain in the smaller window. \(\square\)

### Corollary 7.2

The family \((W_N)_{N\ge0}\) is a coherent symmetric finite approximation scheme for the signed line.

---

## 8. Arithmetic Firewall

### Proposition 8.1

The construction of \(\mathcal Z_F\) uses only:

- a rooted ray;
- a mirrored copy of its positive branch;
- one successor permutation and its inverse;
- an origin-fixing reflection;
- optionally the induced discrete order.

No primitive binary operation

\[
Add(x,y)=x+y
\]

or

\[
Mul(x,y)=xy
\]

is introduced by Definition (1)-(12).

### Proof

Inspection of the signature and defining clauses (1)-(12) shows that every primitive symbol has arity at most one except the order relation. There is no binary operation symbol whose graph is declared to be integer addition or multiplication. The isomorphism \(\phi\) of Theorem 2.1 is an external identification of the coordinate line with ordinary integer labels, not an expansion of the FCOA signature. \(\square\)

### Warning 8.2

Proposition 8.1 is a **signature firewall**, not yet a non-definability theorem. Whether `Add` or `Mul` becomes first-order definable in a particular expansion/reduct is a separate logical question and must be proved separately.

This distinction is mandatory in all later FCOA-Z work.

---

## 9. Consequence for the old integer-line note

The earlier file

`papers/FCOA-ADMISSIBILITY-GEOMETRY/SUCCESSOR_RECURSION_AND_INTEGER_LINE.md`

starts Part II by taking the ordinary integer line as a given carrier.

The present construction supplies a stronger predecessor stage:

\[
\boxed{
\text{rooted natural ray}
\longrightarrow
\text{symmetric signed completion}
\xrightarrow[\text{Theorem 2.1}]{\cong}
\text{pointed oriented integer line}.
}
\tag{35}
\]

Therefore the old recursive-addition theorem can later be re-audited over \(\mathcal Z_F\) without importing \(\mathbb Z\) as a primitive arithmetic object.

No result of that older note is promoted by this observation alone.

---

## 10. Next theorem package

The next strike is not multiplication.

It is the **legacy-operation signed transfer problem**:

1. embed the positive M0 ray into \(B^{\pm}\);
2. preserve every old positive-sector cell exactly;
3. decide which negative-sector cells are forced by a declared reflection-equivariance law and which remain `OPEN`;
4. keep mixed sectors \((+-)\) and \((-+)\) independent until compatibility is proved;
5. define signed output fibers without collapsing \(E^+,E^\ast,E^\times\) into arithmetic values;
6. compute automorphism, commutation and association diagnostics after each proposed transfer.

The first nontrivial question is:

\[
\boxed{
\text{Does there exist a reflection-compatible extension of M0 to }B^{\pm}
\text{ that preserves its directional asymmetry without forcing ordinary arithmetic laws?}
}
\tag{36}
\]
