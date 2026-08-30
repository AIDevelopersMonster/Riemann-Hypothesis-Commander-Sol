# FCOA-Z — One-Dimensional Reconstruction Resolution 0.1

**Date:** 2026-08-30  
**Status:** PROVED CORE / PRIOR-ART BOUNDARY ADDED / HOSTILE AUDIT REQUIRED  
**Branch:** `director/fcoa-z-symmetric-line`  
**Dimensional gate:** `c_coord = 0`

---

## 1. Reconstruction question

The one-dimensional classicalization programme has produced the finitary matrix ideal

\[
I:=M_{fin}(\mathbb Z,K)
\]

inside the operator shadow of the signed FCOA-Z line, together with the bilateral shift \(U\) induced by \(T\) and reflection \(V\) induced by \(\nu\).

The reconstruction problem is now:

\[
\boxed{
\text{How much of the original signed line and how much of the original FCOA operation structure can be recovered from these classical shadows?}
}
\]

The answer is layered:

1. \(I\) alone does **not** remember line geometry;
2. \((I,U)\) reconstructs the oriented line as a \(\mathbb Z\)-torsor;
3. \((I,U,V)\) reconstructs the rooted reflected signed line;
4. the complete base-translation shadow still does **not** distinguish `ZM0-share` from `ZM0-split`;
5. terminal output data is therefore a genuinely independent reconstruction layer.

This gives an exact first **reconstruction-resolution ladder**.

---

## 2. The finitary matrix ideal alone forgets geometry

Write

\[
I=M_{fin}(\mathbb Z,K)
\]

with standard matrix units \(E_{ij}\).

For every permutation

\[
\sigma:\mathbb Z\to\mathbb Z
\]

define

\[
\Phi_\sigma(E_{ij})=E_{\sigma(i),\sigma(j)}.
\tag{2.1}
\]

### Theorem 2.1 — Pure Matrix Erasure Theorem

Every bijection \(\sigma\in\operatorname{Sym}(\mathbb Z)\) induces a \(K\)-algebra automorphism \(\Phi_\sigma\) of \(I\).

Consequently the abstract algebra \(I\) alone does not canonically determine:

- the successor relation on \(\mathbb Z\);
- the order of the line;
- the root \(0\);
- the reflection \(k\mapsto-k\).

### Proof

Using the matrix-unit law,

\[
E_{ij}E_{kl}=\delta_{jk}E_{il},
\]

we have

\[
\Phi_\sigma(E_{ij})\Phi_\sigma(E_{kl})
=
E_{\sigma(i),\sigma(j)}E_{\sigma(k),\sigma(l)}
=
\delta_{\sigma(j),\sigma(k)}E_{\sigma(i),\sigma(l)}
=
\delta_{jk}\Phi_\sigma(E_{il}).
\]

Thus \(\Phi_\sigma\) preserves multiplication and extends linearly to an automorphism.

Because arbitrary permutations need not preserve adjacency, order, the distinguished index \(0\), or reflection, none of those structures can be recovered canonically from the abstract algebra \(I\) alone. \(\square\)

### Interpretation

The matrix ideal remembers arbitrarily fine **local addressability**, but not how those addresses are arranged into a line.

---

## 3. Shift-relative characterization of coordinate projectors

Let

\[
V_K=K^{(\mathbb Z)}
\]

with basis \(\{\mathbf e_k:k\in\mathbb Z\}\), and let \(U\) be the bilateral shift

\[
U\mathbf e_k=\mathbf e_{k+1}.
\]

The operator \(U\) normalizes \(I\).

Define

\[
\mathscr C_U
:=
\left\{
 p\in I:
\begin{array}{l}
p\text{ is a primitive idempotent},\\
pU^np=0\text{ for every }n\in\mathbb Z\setminus\{0\}
\end{array}
\right\}.
\tag{3.1}
\]

### Theorem 3.1 — Coordinate Projector Characterization

\[
\boxed{
\mathscr C_U=\{E_{kk}:k\in\mathbb Z\}.
}
\tag{3.2}
\]

Thus the individual coordinate projectors of the line are intrinsically recoverable from the pair \((I,U)\).

### Proof

Every primitive idempotent of the finitary matrix algebra has rank one. Hence write

\[
p=v\otimes\varphi,
\]

where \(v\in V_K\) has finite support, \(\varphi\) has finite support, and

\[
\varphi(v)=1.
\tag{3.3}
\]

For every integer \(n\),

\[
pU^np
=
\varphi(U^nv)p.
\tag{3.4}
\]

Therefore condition (3.1) says

\[
\varphi(U^nv)=
\begin{cases}
1,&n=0,\\
0,&n\ne0.
\end{cases}
\tag{3.5}
\]

Write

\[
v(z)=\sum_k v_kz^k,
\qquad
q(z)=\sum_j\varphi_jz^{-j}
\]

as Laurent polynomials. The coefficient of \(z^{-n}\) in

\[
q(z)v(z)
\]

is exactly \(\varphi(U^nv)\). Hence (3.5) is equivalent to

\[
q(z)v(z)=1
\quad\text{in }K[z,z^{-1}].
\tag{3.6}
\]

The units of the Laurent polynomial ring are precisely

\[
cz^m,
\qquad
c\in K^\times,\ m\in\mathbb Z.
\]

Therefore \(v\) is supported at one coordinate only and \(\varphi\) is the corresponding reciprocal coordinate functional. Hence

\[
p=E_{mm}
\]

for some \(m\in\mathbb Z\).

Conversely every \(E_{mm}\) clearly satisfies (3.1). \(\square\)

---

## 4. Reconstruction of the oriented line

Define

\[
\alpha:\mathscr C_U\to\mathscr C_U,
\qquad
\alpha(p)=UpU^{-1}.
\tag{4.1}
\]

By Theorem 3.1,

\[
\alpha(E_{kk})=E_{k+1,k+1}.
\tag{4.2}
\]

### Theorem 4.1 — Oriented-Line Reconstruction Theorem

The dynamical set

\[
(\mathscr C_U,\alpha)
\]

is canonically isomorphic to a two-sided successor line

\[
(\mathbb Z,k\mapsto k+1).
\tag{4.3}
\]

It reconstructs the orientation and adjacency of the line, but not a distinguished root.

### Proof

By Theorem 3.1 the elements of \(\mathscr C_U\) are exactly the coordinate projectors \(E_{kk}\). Equation (4.2) makes them a single free orbit under \(\alpha\). Hence choosing any one projector as temporary index \(0\) identifies the orbit with \(\mathbb Z\), and different choices differ only by an overall translation. \(\square\)

### Corollary 4.2

The passage

\[
I
\longrightarrow
(I,U)
\]

recovers precisely the information lost by arbitrary coordinate permutation down to global translation freedom.

---

## 5. Reflection reconstructs the root

Let \(V\) be the linearized reflection:

\[
V\mathbf e_k=\mathbf e_{-k}.
\]

Then

\[
V^2=1,
\qquad
VUV=U^{-1}.
\tag{5.1}
\]

Define

\[
\beta(p)=VpV^{-1}.
\tag{5.2}
\]

On coordinate projectors,

\[
\beta(E_{kk})=E_{-k,-k}.
\tag{5.3}
\]

### Theorem 5.1 — Rooted Signed-Line Reconstruction Theorem

Inside \(\mathscr C_U\), the reflection action \(\beta\) has exactly one fixed point:

\[
\boxed{E_{00}.}
\tag{5.4}
\]

Therefore the enriched classical shadow

\[
\boxed{(I,U,V)}
\]

reconstructs the pointed oriented reflected line

\[
(\mathbb Z,0,k\mapsto k+1,k\mapsto-k)
\]

up to unique isomorphism preserving the displayed operators.

### Proof

By (5.3),

\[
\beta(E_{kk})=E_{kk}
\iff
-k=k
\iff
k=0.
\]

Thus \(E_{00}\) is the unique reflection-fixed coordinate projector. Using it as the root and iterating \(\alpha\) gives

\[
E_{kk}=\alpha^k(E_{00}).
\]

The relation \(VUV=U^{-1}\) then recovers the reflected orientation exactly. \(\square\)

### Meaning

The classical shadow is not uniformly information-poor. Once the local ideal and the distinguished kinematic operators are retained, the original one-dimensional carrier geometry is fully recoverable.

---

## 6. Reconstruction of order and sign

From Theorem 5.1 define

\[
E_{ii}<E_{jj}
\iff
j-i>0,
\]

equivalently if

\[
E_{jj}=\alpha^n(E_{ii})
\]

for some positive integer \(n\).

Relative to the unique root \(E_{00}\), define

\[
\mathscr C_U^+
=
\{\alpha^n(E_{00}):n\ge1\},
\]

\[
\mathscr C_U^-
=
\{\alpha^{-n}(E_{00}):n\ge1\}.
\]

Hence the positive/negative decomposition of the signed line is also recovered from \((I,U,V)\).

---

## 7. The coarse quotient alone still loses local coordinates

The previous one-dimensional matrix package established

\[
\mathcal A_{sym}/I
\cong
M_2(K[t,t^{-1}]).
\tag{7.1}
\]

The quotient has forgotten every singleton projector because

\[
E_{kk}\in I.
\]

Thus the quotient remembers asymptotic translation/reflection structure but not individual coordinate points.

The exact extension

\[
0\to I\to\mathcal A_{sym}\to M_2(K[t,t^{-1}])\to0
\tag{7.2}
\]

should therefore be viewed as a two-resolution object:

- \(I\): local coordinate resolution;
- quotient: asymptotic two-ended resolution.

Neither layer alone contains all the information carried by the enriched pair \((I,U,V)\).

---

## 8. `share` and `split` remain invisible to every base-only shadow

Let

\[
F_{share}
\]

and

\[
F_{split}
\]

be the established signed M0 variants differing only in terminal-output reflection geometry.

Define the **base translation shadow** \(\mathscr B(F)\) by retaining:

1. the base carrier \(X\);
2. every partial translation component whose input and output both lie in \(X\);
3. the operators \(T\) and \(\nu\);
4. arbitrary algebraic closure/linearization of those base maps;
5. no terminal \(E\)-elements and no maps whose values lie in terminal sorts.

### Theorem 8.1 — Persistent Share/Split Collision

\[
\boxed{
\mathscr B(F_{share})
=
\mathscr B(F_{split})
}
\tag{8.1}

as concrete base translation systems.

Consequently every classical structure functorially derived from \(\mathscr B(F)\) is identical for `share` and `split`.

### Proof

By construction the two signed M0 variants have exactly the same base carrier, exactly the same domains of all legacy operations on base inputs, and exactly the same base-valued outputs.

They differ only when a terminal output \(E_n^\alpha\) is either shared by the two mirror cells or split into two outputs exchanged by reflection.

The definition of \(\mathscr B(F)\) deletes all terminal-valued components. Therefore no retained map differs between the two variants. \(\square\)

### Corollary 8.2 — Full signed-line geometry does not reconstruct terminal geometry

Even though \((I,U,V)\) reconstructs the signed line exactly,

\[
\boxed{
(I,U,V)\not\Rightarrow\text{unique reconstruction of the full FCOA-Z expansion}.
}
\tag{8.2}
\]

This is witnessed by `ZM0-share` and `ZM0-split`.

---

## 9. Minimal terminal separator for `share` versus `split`

Let \(E\) denote the active terminal output set and \(\nu_E\) its output-reflection involution.

In the shared model,

\[
\nu_E(e)=e
\]

for every mirrored terminal output retained in a shared fiber.

In the split model, each positive terminal output is paired with a distinct reflected output:

\[
e\ne\nu_E(e).
\]

### Theorem 9.1 — Terminal-Cycle Separator

The enriched shadow

\[
\boxed{(I,U,V;E,\nu_E)}
\tag{9.1}

separates the canonical `share` and `split` variants.

### Proof

The number and cycle type of fixed points of an involution are invariants of an isomorphism of involutive sets.

The shared terminal fibers contain reflection-fixed active outputs, whereas the canonical split fibers consist of nontrivial two-cycles. Therefore the terminal involutive sets are nonisomorphic. \(\square\)

### Important limitation

The pair \((E,\nu_E)\) tells us that the terminal geometry is shared or split, but by itself does not tell us **which operation cell produced which terminal element**.

For that one must retain a terminal attachment/incidence map.

---

## 10. Reconstruction ladder

The current one-dimensional reconstruction resolution is therefore:

### `R0` — Pure local algebra

\[
I=M_{fin}(\mathbb Z,K).
\]

Recovers:

- arbitrarily large finite matrix corners;
- countable local addressability.

Forgets:

- adjacency;
- order;
- root;
- reflection;
- terminal fibers;
- operation labels.

### `R1` — Oriented local algebra

\[
(I,U).
\]

Recovers:

- the coordinate projectors;
- successor;
- oriented two-sided line up to global translation.

Still forgets:

- root;
- terminal fibers;
- operation attachment.

### `R2` — Rooted signed geometry

\[
(I,U,V).
\]

Recovers:

- the root;
- positive and negative branches;
- reflection;
- full pointed oriented-line geometry.

Still does not distinguish `share` from `split`.

### `R3` — Terminal reflection geometry

\[
(I,U,V;E,\nu_E).
\]

Now distinguishes canonical `share` and `split`.

Still does not reconstruct the operation-cell-to-terminal attachment map.

### `R4` — Terminal incidence

Add the map/relation recording which defined legacy cells land in which terminal outputs.

At this level the currently audited signed-M0 output assignment is recoverable.

---

## 11. Reconstruction resolution theorem

### Theorem 11.1

For the current signed M0 FCOA-Z family, reconstruction information is strictly layered:

\[
\boxed{
R0<R1<R2<R3<R4
}
\tag{11.1}

in resolving power on the canonical source class, with the following explicit witnesses:

1. arbitrary coordinate permutations witness the failure of \(R0\) to recover the line;
2. global translations witness the absence of a root at \(R1\);
3. `ZM0-share` and `ZM0-split` witness the failure of \(R2\) to reconstruct terminal geometry;
4. different terminal attachment maps with the same involutive terminal set witness the remaining gap between \(R3\) and \(R4\).

### Proof

Items 1–3 are Theorems 2.1, 4.1–5.1, and 8.1–9.1.

For item 4, keep the same base line and the same involutive terminal set but permute terminal labels among two terminal-producing operation orbits in a way compatible with the involution. The involutive set remains unchanged while the cell-to-output incidence relation changes. Thus \(R3\) alone cannot determine the attachment relation. \(\square\)

---

## 12. What is actually invertible now

The correct statement is not

\[
\text{FCOA}\to\text{classical shadow is always irreversible}.
\]

The refined statement is:

\[
\boxed{
\text{different shadow resolutions forget different layers, and some forgotten layers become reconstructible after enrichment.}
}
\]

Specifically,

\[
\boxed{
(I,U,V)
\Longleftrightarrow
\text{rooted signed line geometry}
}
\tag{12.1}

up to the natural notion of isomorphism used above.

But

\[
\boxed{
(I,U,V)
\not\Longleftrightarrow
\text{full FCOA-Z operation/output structure}.
}
\tag{12.2}

Thus the source is not simply “more information than classical algebra” in one undifferentiated sense. The information loss can now be localized by structural layer.

---

## 13. Relation to the one-dimensional matrix extension

The short exact sequence

\[
0\to M_{fin}(\mathbb Z,K)
\to\mathcal A_{sym}
\to M_2(K[t,t^{-1}])
\to0
\tag{13.1}

has a strong formal resemblance to classical algebraic Toeplitz/Jacobson and Leavitt-path-algebra extensions, where a finitary-matrix ideal sits below a Laurent-polynomial quotient.

This resemblance is mathematically important for prior-art control.

The novelty candidate is **not** the bare existence of a matrix ideal/Laurent quotient extension. Those structures are classical in algebraic Toeplitz and Leavitt path algebra theory.

The FCOA-specific question is narrower:

\[
\boxed{
\text{the matrix ideal is generated intrinsically from the audited legacy FCOA translations, and its enrichment by }U,V\text{ reconstructs the signed source line.}
}
\]

A separate exact literature audit is required before any priority claim.

---

## 14. Dimensional firewall

All reconstruction occurs on the same source line.

The pair of indices in \(E_{ij}\) refers to the source and target of an operator

\[
x_j\mapsto x_i,
\]

not to a point \((i,j)\) in a plane.

Likewise the matrix factor \(2\) in

\[
M_2(K[t,t^{-1}])
\]

records two reflected asymptotic ends of one line.

Therefore

\[
\boxed{c_{coord}=0}
\]

throughout this reconstruction package.

---

## 15. Next one-dimensional strike

The geometry-reconstruction question is now substantially solved.

The next strictly one-dimensional problem is the **Operation Reconstruction Problem**:

\[
\boxed{
\text{What is the weakest enrichment of }(I,U,V)
\text{ that reconstructs the primitive legacy operations }\oplus,\otimes
\text{ rather than merely their generated algebra?}
}
\]

The correct targets are:

1. characterize the distinguished partial translations \(R_a^\oplus,L_a^\oplus,R_a^\otimes,L_a^\otimes\) intrinsically inside the generated partial-transformation system;
2. determine which translations are definable from \(I,U,V\) and which require explicit operation labels;
3. classify the minimal terminal attachment data needed to recover `share` and `split` completely;
4. prove a reconstruction/no-reconstruction theorem before any E-output re-entry is allowed.

No higher-dimensional construction is licensed by these results.