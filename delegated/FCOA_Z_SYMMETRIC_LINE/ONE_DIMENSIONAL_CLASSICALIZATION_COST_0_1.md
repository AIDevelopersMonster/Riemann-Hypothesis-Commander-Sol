# FCOA-Z — One-Dimensional Classicalization Cost 0.1

**Date:** 2026-08-30  
**Status:** PROVED CORE / ONE-DIMENSIONAL GATE ACTIVE  
**Branch:** `director/fcoa-z-symmetric-line`

---

## 1. Dimensional restriction

This note deliberately remains inside the already audited FCOA-Z signed line.

No theorem below introduces a second independently iterable coordinate operator.

No construction below uses an orbit of the form

\[
\{T^mQ^n(x_0):m,n\in\mathbb Z\}
\]

with independent unbounded parameters \(m,n\).

The working rule is:

\[
\boxed{
\text{finite internal fibers and finite-dimensional linear representations are not new spatial coordinates.}
}
\]

A target is marked `DIMENSION-GATED` rather than pursued if its proof would require a genuinely independent unbounded coordinate direction.

---

## 2. One-dimensional realization tiers

Let \(F_Z\) denote the audited signed-line FCOA-Z source with

\[
X=\{x_k:k\in\mathbb Z\},
\qquad
T(x_k)=x_{k+1},
\qquad
\nu(x_k)=x_{-k}.
\]

We use three tiers.

### Tier `1D-0` — bare shadow

No new source carrier, sort, cell, or primitive translation is added.

Allowed operations are standard post-processing of already generated source shadows:

- subgroups/monoids of existing translations;
- homomorphic quotients;
- endomorphism rings;
- group/category algebras;
- finite-dimensional representations and their image algebras.

### Tier `1D-F` — finite-fiber enrichment

One may conservatively add only finite internal sorts/fibers and finitely many local transition types, with no new independently iterable unbounded coordinate.

### Tier `DIMENSION-GATED`

Any construction requiring an independently iterable unbounded generator beyond the signed line is suspended.

Nothing in this note enters this tier.

---

## 3. Bare kinematic groups

The established operator groups are

\[
G_T:=\langle T\rangle\cong\mathbb Z,
\tag{3.1}
\]

and

\[
G_D:=\langle T,\nu\rangle
\cong
D_\infty
=
\langle T,\nu\mid \nu^2=1,\ \nu T\nu=T^{-1}\rangle.
\tag{3.2}
\]

These belong to Tier `1D-0`.

---

## 4. Complete finite quotient classification for the translation shadow

### Theorem 4.1 — Finite quotients of \(G_T\)

Every finite quotient of \(G_T\cong\mathbb Z\) is cyclic.

More precisely, for every \(n\ge1\),

\[
\boxed{
G_T/\langle T^n\rangle\cong C_n,
}
\tag{4.1}
\]

and these exhaust the finite quotients of \(G_T\).

### Proof

Every subgroup of \(\mathbb Z\) is \(n\mathbb Z\) for a unique \(n\ge0\). A finite quotient requires \(n\ge1\), and

\[
\mathbb Z/n\mathbb Z\cong C_n.
\]

Under the isomorphism \(1\mapsto T\), the subgroup \(n\mathbb Z\) corresponds to \(\langle T^n\rangle\). \(\square\)

### Cost consequence

The source modification cost of every \(C_n\) is zero:

\[
\Delta c_{sort}
=
\Delta c_{cell}
=
\Delta c_{gen}
=
\Delta c_{coord}
=0.
\tag{4.2}
\]

Only the external quotient relation

\[
T^n=1
\]

is imposed at the shadow level.

---

## 5. Complete finite quotient classification for the dihedral shadow

For \(n\ge2\), write

\[
D_{2n}
=
\langle r,s\mid r^n=1,\ s^2=1,\ srs=r^{-1}\rangle,
\]

so \(|D_{2n}|=2n\).

### Theorem 5.1 — Finite quotients of \(G_D\)

Every finite quotient of \(D_\infty\) is either

\[
1,
\qquad
C_2,
\qquad
D_{2n}\ (n\ge2).
\tag{5.1}
\]

For every \(n\ge2\),

\[
\boxed{
D_\infty/\langle\!\langle T^n\rangle\!\rangle
\cong D_{2n}.
}
\tag{5.2}
\]

### Proof

Let

\[
q:D_\infty\twoheadrightarrow H
\]

be a finite quotient and put

\[
r=q(T),
\qquad
s=q(\nu).
\]

Then

\[
s^2=1,
\qquad
srs=r^{-1},
\tag{5.3}
\]

and \(H=\langle r,s\rangle\).

Because \(H\) is finite, \(r\) has finite order \(n\).

If \(s\notin\langle r\rangle\), then \(\langle r\rangle\) has exactly two cosets in \(H\):

\[
\langle r\rangle,
\qquad
\langle r\rangle s.
\]

Every element therefore has the form \(r^k\) or \(r^ks\), the two cosets are disjoint, and relation (5.3) gives the standard dihedral group of order \(2n\).

If \(s\in\langle r\rangle\), then \(H=\langle r\rangle\) is cyclic. Conjugation by \(s\) is therefore trivial, while (5.3) says it sends \(r\) to \(r^{-1}\). Hence

\[
r=r^{-1},
\]

so \(r^2=1\). Thus \(H\) is trivial or \(C_2\).

Finally imposing \(T^n=1\) in (3.2) gives exactly the presentation of \(D_{2n}\). \(\square\)

### Consequence

The finite group shadows already accessible from the bare line kinematics are completely classified. No second coordinate is needed.

---

## 6. Finite rings from the same line

The established ring shadow is

\[
\operatorname{End}(G_T)\cong\mathbb Z.
\tag{6.1}
\]

### Theorem 6.1 — Residue-ring shadows

For every \(n\ge1\),

\[
\boxed{
\operatorname{End}(G_T)/n\operatorname{End}(G_T)
\cong
\mathbb Z/n\mathbb Z.
}
\tag{6.2}
\]

### Proof

Transport the ideal \(n\mathbb Z\) through the ring isomorphism (6.1). \(\square\)

Thus all residue rings of the integers occur at Tier `1D-0`.

---

## 7. Laurent shadow and all of its algebra quotients

Let \(K\) be a field. The translation group algebra is

\[
A_T:=K[G_T]
\cong
K[t,t^{-1}].
\tag{7.1}
\]

### Theorem 7.1 — Principal one-dimensional algebra-quotient theorem

Every two-sided ideal of \(A_T\) is principal. Therefore every algebra quotient of the bare translation group algebra has the form

\[
\boxed{
K[t,t^{-1}]/(f(t))
}
\tag{7.2}
\]

for some Laurent polynomial \(f\).

If \(f\ne0\), the generator may be multiplied by a unit \(ct^m\) so that it is an ordinary polynomial with nonzero constant term.

### Proof

The polynomial ring \(K[t]\) is a Euclidean domain and hence a PID. The Laurent ring is the localization

\[
K[t,t^{-1}]
=S^{-1}K[t],
\qquad
S=\{1,t,t^2,\ldots\}.
\]

Localization of a principal ideal domain is again a principal ideal domain. Hence every ideal in \(K[t,t^{-1}]\) is principal.

For nonzero \(f\), multiply by a suitable power of \(t\), which is a unit in the Laurent ring, to remove negative exponents and then divide out any remaining factor \(t^m\). The resulting polynomial has nonzero constant term and generates the same ideal. \(\square\)

### Corollary 7.2 — Cyclic group algebras

For every \(n\ge1\),

\[
\boxed{
K[C_n]
\cong
K[t,t^{-1}]/(t^n-1).
}
\tag{7.3}
\]

### Proof

The quotient relation \(t^n=1\) makes the distinguished invertible generator have order \(n\). The basis classes

\[
1,t,\ldots,t^{n-1}
\]

then reproduce the group basis of \(K[C_n]\). \(\square\)

### Corollary 7.3 — Truncated local algebras from one line

For every \(m\ge1\),

\[
\boxed{
K[t,t^{-1}]/((t-1)^m)
\cong
K[\varepsilon]/(\varepsilon^m).
}
\tag{7.4}
\]

### Proof

Put \(\varepsilon=t-1\), so \(t=1+\varepsilon\). In \(K[\varepsilon]/(\varepsilon^m)\), the element \(1+\varepsilon\) is invertible with finite inverse

\[
1-\varepsilon+\varepsilon^2-\cdots+(-1)^{m-1}\varepsilon^{m-1}.
\]

Hence the Laurent inversion of \(t\) adds nothing beyond the truncated polynomial algebra. \(\square\)

### Interpretation

Even nilpotent classical algebra can appear as an algebraic quotient shadow of one reversible coordinate generator. No geometric second direction is involved.

---

## 8. A non-group semigroup already hidden in the legacy radial law

The signed legacy operation has right-zero translation

\[
\rho:=R_{x_0}^{\oplus},
\]

with domain

\[
\operatorname{dom}(\rho)=X\setminus\{x_0\}
\]

and

\[
\rho(x_k)=x_{k-\operatorname{sgn}(k)}.
\tag{8.1}
\]

For \(m\ge1\), its \(m\)-fold partial composition satisfies

\[
\operatorname{dom}(\rho^m)
=
\{x_k:|k|\ge m\}
\tag{8.2}
\]

and

\[
\rho^m(x_k)
=
 x_{k-m\operatorname{sgn}(k)}.
\tag{8.3}
\]

### Theorem 8.1 — Radial monoid theorem

The partial transformation monoid

\[
R_\rho:=\{\operatorname{id}_X,\rho,\rho^2,\ldots\}
\]

is isomorphic to the additive monoid \((\mathbb N_0,+)\):

\[
\boxed{R_\rho\cong\mathbb N_0.}
\tag{8.4}
\]

### Proof

By associativity of partial-map composition,

\[
\rho^m\circ\rho^n=\rho^{m+n}.
\]

The powers are distinct because their domains in (8.2) are distinct. Hence

\[
m\mapsto\rho^m
\]

is an injective monoid homomorphism with image exactly \(R_\rho\). \(\square\)

Define a congruence on \(\mathbb N_0\) by keeping \(0\) separate and identifying all positive integers.

### Corollary 8.2 — Two-element semilattice shadow

The quotient of \(R_\rho\) by the corresponding congruence is

\[
\boxed{
E_2=\{1,e\},
\qquad
e^2=e,
\qquad
1e=e1=e.
}
\tag{8.5}
\]

Thus the two-element semilattice monoid is already a Tier `1D-0` quotient shadow of the existing FCOA-Z radial contraction.

### Significance

This shows that bare one-dimensional FCOA-Z does not generate only group-like classical shadows. A genuinely noninvertible idempotent classical law can emerge after quotienting the iterated radial partial translations.

---

## 9. A full matrix algebra from the one-dimensional dihedral shadow

The next result is deliberately about **representation dimension**, not coordinate-space dimension.

Let \(K\) be a field containing an element

\[
\lambda\in K^\times
\]

with

\[
\lambda^2\ne1.
\tag{9.1}
\]

Define

\[
R=
\begin{pmatrix}
\lambda&0\\
0&\lambda^{-1}
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\tag{9.2}
\]

Then

\[
S^2=I,
\qquad
SRS=R^{-1}.
\tag{9.3}
\]

Hence there is a representation

\[
\rho_\lambda:D_\infty\to GL_2(K)
\]

with

\[
T\mapsto R,
\qquad
\nu\mapsto S.
\]

### Theorem 9.1 — Matrix-two shadow theorem

Under condition (9.1), the induced algebra homomorphism

\[
K[D_\infty]\to M_2(K)
\]

is surjective. Therefore

\[
\boxed{M_2(K)}
\]

is a quotient algebra of the bare one-dimensional dihedral shadow.

### Proof

Because \(\lambda\ne\lambda^{-1}\), the two diagonal matrices \(I\) and \(R\) are linearly independent and span the full diagonal subalgebra of \(M_2(K)\). Thus the standard diagonal matrix units \(E_{11},E_{22}\) lie in the algebra generated by \(R\).

Now

\[
E_{11}SE_{22}=E_{12},
\qquad
E_{22}SE_{11}=E_{21}.
\]

Therefore the algebra generated by \(R,S\) contains all four matrix units

\[
E_{11},E_{12},E_{21},E_{22}.
\]

Hence it equals \(M_2(K)\). \(\square\)

### Dimensional firewall

The two basis coordinates of the representation space \(K^2\) are not two FCOA coordinate directions. The source still has only the single signed line generated by \(T\).

---

## 10. Kinematic matrix ceiling

The preceding theorem is nearly maximal for the **bare dihedral group algebra**.

### Theorem 10.1 — Rank-two simple-quotient ceiling

Let \(K\) be algebraically closed. If there is a surjective \(K\)-algebra homomorphism

\[
K[D_\infty]\twoheadrightarrow M_n(K),
\tag{10.1}
\]

then

\[
\boxed{n\le2.}
\tag{10.2}
\]

### Proof

Compose the group embedding

\[
D_\infty\subset K[D_\infty]^\times
\]

with the quotient map (10.1). The natural simple \(M_n(K)\)-module \(K^n\) becomes an irreducible finite-dimensional representation \(V\) of \(D_\infty\).

Let \(R\) be the linear operator representing \(T\), and \(S\) the operator representing \(\nu\). Since \(K\) is algebraically closed, \(R\) has an eigenvector \(v\ne0\):

\[
Rv=\lambda v
\]

for some \(\lambda\ne0\).

From

\[
SRS=R^{-1}
\]

we obtain

\[
R(Sv)=\lambda^{-1}Sv.
\]

Therefore

\[
W:=\operatorname{span}\{v,Sv\}
\]

is invariant under both \(R\) and \(S\), hence under all of \(D_\infty\).

Because \(V\) is irreducible and \(W\ne0\),

\[
V=W.
\]

Thus

\[
\dim_KV\le2.
\]

But \(\dim_KV=n\), so \(n\le2\). \(\square\)

### Interpretation

This is a true one-dimensional shadow wall:

\[
\boxed{
K[D_\infty]\text{ alone can produce }M_2(K)\text{, but no }M_n(K)\text{ with }n\ge3
}
\]

as a simple matrix quotient over an algebraically closed field.

This statement concerns the **bare kinematic shadow only**. It does not imply that larger matrix algebras require a second FCOA spatial dimension.

---

## 11. Finite-fiber escape without a new coordinate

The matrix ceiling can be crossed while remaining one-dimensional by finite internal enrichment.

For \(n\ge1\), let \(\mathcal P_n\) be the finite category with objects

\[
1,\ldots,n
\]

and exactly one arrow

\[
e_{ij}:j\to i
\]

for every ordered pair \((i,j)\), with

\[
e_{ij}\circ e_{jk}=e_{ik}.
\]

Its category algebra satisfies

\[
K[\mathcal P_n]\cong M_n(K)
\tag{11.1}
\]

via

\[
e_{ij}\mapsto E_{ij}.
\]

### Theorem 11.1 — Finite-fiber matrix realization

For every \(n\ge1\), \(M_n(K)\) admits a Tier `1D-F` FCOA realization obtained by conservatively attaching a finite translation-category fiber model of \(\mathcal P_n\) to the existing signed line.

No second independently iterable coordinate is introduced.

### Proof

Use the already proved Universal Category Shadow Realization to realize \(\mathcal P_n\) by finitely many typed state and marker sorts. Attach those sorts disjointly to the existing FCOA-Z source, or regard them as finite internal fibers over the distinguished root, while adding no unbounded successor/translation on the new fiber index.

The reduct to the original FCOA-Z signature is unchanged, so the extension is conservative.

The translation-category algebra of the finite fiber is

\[
K[\mathcal P_n]\cong M_n(K).
\]

Because all newly added indexing sets are finite and possess no independently iterable unbounded translation, the construction introduces no new coordinate dimension under the Line Completion Gate criterion. \(\square\)

### Consequence

Matrix size and spatial dimension separate sharply:

\[
\boxed{
\text{large }n\text{ in }M_n(K)
\not\Rightarrow
\text{new FCOA coordinate dimension}.
}
\tag{11.2}
\]

The price may be finite fiber complexity rather than geometric dimension.

---

## 12. First one-dimensional cost table

The following entries are established upper bounds, not all proven minima.

| Target classical object | Lowest established tier | New FCOA coordinate | Source modification | Shadow operation |
|---|---|---:|---:|---|
| \(C_n\) | `1D-0` | 0 | none | quotient \(T^n=1\) |
| \(D_{2n}\) | `1D-0` | 0 | none | quotient \(T^n=1\) in \(D_\infty\) |
| \(\mathbb Z/n\mathbb Z\) | `1D-0` | 0 | none | ring quotient |
| \(K[C_n]\) | `1D-0` | 0 | none | \((t^n-1)\) quotient |
| \(K[\varepsilon]/(\varepsilon^m)\) | `1D-0` | 0 | none | \(((t-1)^m)\) quotient |
| two-element semilattice monoid | `1D-0` | 0 | none | quotient of \(\langle\rho\rangle\) |
| \(M_2(K)\) under (9.1) | `1D-0` | 0 | none | representation image of \(K[D_\infty]\) |
| \(M_n(K),n\ge3\) | `1D-F` upper bound | 0 | finite fiber only | category algebra |

For algebraically closed \(K\), \(M_n(K),n\ge3\) cannot occur as a simple quotient of the bare dihedral group algebra, by Theorem 10.1.

The exact minimum finite-fiber cost for \(M_n(K)\) remains open.

---

## 13. Revised Classicalization Cost

The previous candidate vector

\[
\operatorname{CCost}(A;F_Z)
=
(c_{sort},c_{cell},c_{gen},c_{depth},c_{coord},c_{memory})
\]

needs one additional coordinate because source cost and shadow-quotient cost are different resources.

We therefore refine it to

\[
\boxed{
\operatorname{CCost}_{1D}(A;F_Z)
=
(c_{sort},c_{cell},c_{gen},c_{depth},c_{coord},c_{memory};c_{rel}),
}
\tag{13.1}
\]

where \(c_{rel}\) records the number/complexity of external shadow relations, quotient congruences, or representation kernels.

This prevents a zero-source-cost quotient such as

\[
\mathbb Z\to C_n
\]

from being confused with a relation-free emergence theorem.

For the current programme we impose

\[
\boxed{c_{coord}=0}
\tag{13.2}
\]

as a hard research constraint.

---

## 14. What the one-dimensional results now say

The signed FCOA line already supports three distinct kinds of classicalization without any second coordinate:

### 14.1 Reversible kinematic classicalization

\[
T,\nu
\leadsto
\mathbb Z,D_\infty,C_n,D_{2n}.
\]

### 14.2 Algebraic quotient classicalization

\[
K[t,t^{-1}]
\leadsto
K[C_n],
K[\varepsilon]/(\varepsilon^m),
\text{and other one-generator Laurent quotients}.
\]

### 14.3 Irreversible radial classicalization

\[
\rho
\leadsto
\mathbb N_0
\leadsto
E_2.
\]

Thus both reversible and irreversible classical laws already coexist as shadows of one-dimensional FCOA-Z mechanisms.

---

## 15. Dimensional non-claim

Nothing proved here implies

\[
\text{matrix rank}
=
\text{spatial dimension},
\]

or

\[
\text{number of algebra generators}
=
\text{number of FCOA coordinate axes}.
\]

In particular, Theorem 11.1 proves the opposite warning: arbitrarily large matrix algebras can be represented with finite fibers while the FCOA coordinate carrier remains one-dimensional.

Therefore all future dimension claims remain locked behind the existing Line Completion Gate.

---

## 16. Immediate one-dimensional next strike

The next research problem is now entirely internal to the line:

\[
\boxed{
\textbf{Minimal 1D Classicalization Problem}
}
\]

For each target classical structure \(A\), minimize

\[
\operatorname{CCost}_{1D}(A;F_Z)
\]

subject to

\[
c_{coord}=0.
\]

The first unresolved targets are:

1. exact minimal finite-fiber cost of \(M_n(K)\) for \(n\ge3\);
2. whether the already existing legacy translations \(\oplus,\otimes\), without any new fibers, can exceed the rank-two kinematic matrix ceiling;
3. classification of all finite semigroup quotients of the radial translation monoid and of the combined \(T,\nu,\rho\) partial-transformation system;
4. classification of which finite-dimensional associative algebras occur as quotients of the **existing** one-line translation-category algebra before any finite-fiber enrichment;
5. determination of the first algebraic target that is impossible at Tier `1D-0` but possible at Tier `1D-F`.

No plane or higher-dimensional construction is needed to attack any of these questions.