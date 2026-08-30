# FCOA-Z — Operation Provenance and Reconstruction No-Go 0.1

**Date:** 2026-08-30  
**Status:** PROVED CORE / HOSTILE AUDIT REQUIRED  
**Branch:** `director/fcoa-z-symmetric-line`  
**Dimensional gate:** `c_coord=0`

---

## 1. Problem

The previous reconstruction package showed that the enriched classical shadow

\[
(I,U,V),
\qquad I=M_{fin}(\mathbb Z,K),
\]

reconstructs the rooted signed line geometry exactly, while terminal output geometry remains invisible until terminal data is restored.

A sharper question remains:

\[
\boxed{
\text{Does the generated operator algebra remember which primitive FCOA operation generated a given operator?}
}
\]

For the current signed M0 answer is negative in a strong form.

The base-valued part of the legacy operation `oplus` contributes no new linear operator to the algebra once the signed kinematics and the existing `otimes` base translations are present.

Thus the classical base shadow can reconstruct the geometry while still forgetting **primitive-law provenance**.

---

## 2. Setup

Write

\[
X=\{x_k:k\in\mathbb Z\},
\qquad U\mathbf e_k=\mathbf e_{k+1},
\qquad V\mathbf e_k=\mathbf e_{-k}
\]

on

\[
V_K=K^{(\mathbb Z)}.
\]

Let

\[
a_+=R_{x_1}^{\otimes},
\qquad
a_-=R_{x_{-1}}^{\otimes}
\]

be the two existing `otimes` tail partial identities.

Their product isolates the root:

\[
e_0=a_+a_-=\operatorname{id}_{\{x_0\}}.
\tag{2.1}
\]

By conjugating with \(U\),

\[
e_k=U^ke_0U^{-k}
\]

is the singleton projector at \(x_k\), and

\[
E_{ij}=U^ie_0U^{-j}
\tag{2.2}
\]

is the singleton partial map \(x_j\mapsto x_i\).

Let

\[
C=L_{x_0}^{\otimes}
\]

be the linearization of the legacy constant-collapse translation

\[
x_k\mapsto x_0\quad(k\ne0).
\]

Define

\[
\mathcal A_{\otimes}^{base}
:=
K\text{-alg}\langle U,U^{-1},V,\widehat a_+,\widehat a_-,C\rangle.
\tag{2.3}
\]

---

## 3. Base components of `oplus`

The legacy signed `oplus` has the following base-valued translation components.

### 3.1 Left translation by the root

\[
L_{x_0}^{\oplus}(x_k)=x_k
\qquad(k\ne0),
\]

and the root/root cell is undefined. Hence

\[
\widehat L_{x_0}^{\oplus}=I-e_0.
\tag{3.1}
\]

### 3.2 Right translation by the root

\[
R_{x_0}^{\oplus}=\rho,
\]

where

\[
\rho(x_k)=x_{k-\operatorname{sgn}(k)}
\qquad(k\ne0).
\]

From the one-dimensional matrix package,

\[
\widehat\rho
=U^{-1}P_+ + UP_-,
\tag{3.2}
\]

where \(P_+\) and \(P_-\) are the positive and negative half-line projectors generated from the two `otimes` tail translations and \(e_0\).

### 3.3 Nonzero right arguments

For \(k\ne0\), the only base-valued cell of the right translation by \(x_k\) is

\[
x_0\oplus x_k=x_k.
\]

Therefore its base component is

\[
\widehat{R_{x_k}^{\oplus}}\big|_{X\to X}=E_{k0}.
\tag{3.3}
\]

The diagonal cell \(x_k\oplus x_k\) lands in a terminal \(E^+\)-sort and is omitted from the base component.

### 3.4 Nonzero left arguments

For \(k\ne0\), the only base-valued cell of the left translation by \(x_k\) is

\[
x_k\oplus x_0=x_{k-\operatorname{sgn}(k)}.
\]

Hence

\[
\widehat{L_{x_k}^{\oplus}}\big|_{X\to X}
=E_{k-\operatorname{sgn}(k),0}.
\tag{3.4}
\]

---

## 4. `oplus` base-provenance erasure theorem

### Theorem 4.1 — Base Operator Redundancy of `oplus`

Every linearized base-valued translation component of the signed legacy `oplus` belongs to

\[
\mathcal A_{\otimes}^{base}.
\]

Consequently

\[
\boxed{
K\text{-alg}\langle
\mathcal A_{\otimes}^{base},
\text{all base-valued `oplus` translations}
\rangle
=
\mathcal A_{\otimes}^{base}.
}
\tag{4.1}
\]

### Proof

Equation (3.1) lies in the algebra because \(e_0\in\mathcal A_{\otimes}^{base}\).

Equation (3.2) lies in the algebra because the half-line projectors \(P_+,P_-\) are obtained from the existing `otimes` tail translations and conjugation by \(U\).

For every \(k\ne0\), equations (3.3) and (3.4) are matrix units of the form (2.2), hence lie in the finitary matrix ideal already generated inside \(\mathcal A_{\otimes}^{base}\).

These exhaust the base-valued translation components of `oplus`. \(\square\)

### Corollary 4.2 — Primitive provenance is lost

The generated linear base algebra does not determine whether the operators in (3.1)–(3.4) were introduced as primitive `oplus` translations or merely arose as composites/linear combinations of the `otimes`-kinematic shadow.

Thus

\[
\boxed{
\text{operator existence}\ne\text{primitive-operation provenance}.
}
\tag{4.2}
\]

---

## 5. A concrete no-go witness

Let \(F\) be the current signed M0 structure with both `oplus` and `otimes`.

Construct a comparison structure \(F^{-\oplus}\) on the same signed carrier and with the same `otimes`, \(T\), and \(\nu\), but with the `oplus` symbol interpreted as nowhere-defined on base-valued cells. Terminal `oplus` data may also be removed for this comparison.

Then \(F\) and \(F^{-\oplus}\) are not isomorphic as structures in the signature containing the distinguished symbol `oplus`, but Theorem 4.1 gives

\[
\boxed{
\mathcal A_{base}(F)
=
\mathcal A_{base}(F^{-\oplus}).
}
\tag{5.1}
\]

where \(\mathcal A_{base}\) means the generated linear base-translation algebra.

### Theorem 5.1 — Operation-Provenance No-Go

There is no reconstruction rule from the bare generated linear base algebra to the primitive binary operation table that is correct on any source class containing both \(F\) and \(F^{-\oplus}\).

### Proof

The two source structures have the same shadow by (5.1) but different primitive `oplus` tables. A single inverse assignment from that common shadow cannot return both source tables. \(\square\)

### Scope

The comparison structure \(F^{-\oplus}\) is a no-go witness, not a proposed replacement for the audited legacy FCOA-Z model. The theorem concerns reconstruction from the shadow, not admissibility as a legacy-preserving extension.

---

## 6. Definedness is a separate information layer

Base-valued shadows merge two semantically different situations:

1. a primitive cell is undefined;
2. the cell is defined but its value lies in a terminal output sort.

For example, in the current signed M0,

\[
x_k\oplus x_k=E_{|k|}^{+,{\rm branch}}
\]

is a defined terminal-valued cell, whereas many off-diagonal same-sign and all genuinely mixed-sign cells are `UNDEF`.

After deleting terminal outputs, both kinds of cell disappear from the base-valued graph.

### Theorem 6.1 — Definedness Erasure No-Go

No base-only translation shadow can reconstruct the full primitive domain of `oplus` or `otimes` unless it is additionally supplied with information distinguishing terminal-valued cells from genuinely undefined cells.

### Proof

Take two partial operation tables that agree on every base-valued cell. In the first, a chosen non-base cell is defined with terminal value \(e\); in the second, declare the same cell undefined. Their base-valued translation components are identical. Hence any reconstruction from those components alone gives the same answer for both source tables and must fail for at least one. \(\square\)

The minimal missing datum is therefore at least a **definedness mask**

\[
D_\omega\subseteq X\times X
\tag{6.1}
\]

for each primitive operation \(\omega\), or an equivalent typed incidence structure.

---

## 7. Terminal value identity is yet another layer

Even the definedness mask does not determine which terminal element occurs at a defined terminal-producing cell.

The canonical `ZM0-share` and `ZM0-split` variants already witness this.

Both have the same base carrier and the same base definedness pattern, but mirror terminal-producing cells either share one output or use two distinct reflected outputs.

Thus:

\[
\boxed{
\text{base geometry + primitive domain}\not\Rightarrow\text{terminal value attachment}.
}
\tag{7.1}
\]

To recover terminal values one must retain at least:

1. the terminal typed universe;
2. terminal reflection \(\nu_E\);
3. the incidence relation assigning a terminal value to each terminal-producing operation cell.

---

## 8. Finite schema reconstruction of the current signed M0

The negative results identify exactly what must be restored. For the currently audited signed M0 family, no infinite independent table needs to be supplied.

Let the reconstruction datum \(\mathfrak R_{M0}\) consist of:

1. the reconstructed signed line \((X,x_0,T,\nu)\);
2. two distinguished primitive operation symbols `oplus` and `otimes`;
3. three typed terminal channel families
   \[
   E^+,
   \qquad E^*,
   \qquad E^\times;
   \]
4. the involution \(\nu_E\) on each terminal family;
5. the following finite schemata on the positive ray, transported to the negative ray by simultaneous reflection.

### `oplus` schema

For \(n\ge1\):

\[
x_0\oplus x_n=x_n,
\tag{8.1}
\]

\[
x_n\oplus x_0=x_{n-1}
\quad(x_0\text{ when }n=1),
\tag{8.2}
\]

\[
x_n\oplus x_n=E_n^+,
\tag{8.3}
\]

with all other positive-positive cells undefined.

### `otimes` schema

For \(n\ge1\):

\[
x_0\otimes x_n=x_0.
\tag{8.4}
\]

For \(n\ge2\):

\[
x_n\otimes x_0=E_n^*,
\tag{8.5}
\]

\[
x_1\otimes x_n=x_n\otimes x_1=x_n,
\tag{8.6}
\]

\[
x_n\otimes x_n=E_n^\times,
\tag{8.7}
\]

with the known exceptional cells and all other positive-positive cells undefined.

No genuinely mixed-sign cell is opened.

### Theorem 8.1 — Finite-Schema Reconstruction Theorem

The datum \(\mathfrak R_{M0}\) determines a unique signed M0 structure within the current minimal simultaneous-reflection-closure class.

### Proof

The signed line provides the positive ray, negative ray, root, radial depth, and reflection.

Equations (8.1)–(8.7) fix every positive legacy cell and every positive terminal attachment. Simultaneous reflection equivariance forces the corresponding negative cells and applies \(\nu_E\) to terminal values. The minimal-domain rule leaves every genuinely mixed-sign cell undefined. Thus every base-base input pair is either assigned a unique value or uniquely declared undefined, and no further freedom remains. \(\square\)

### Interpretation

The full primitive operations are reconstructible from a **finite law schema plus terminal attachment structure**, but not from their generated classical operator algebra alone.

---

## 9. Revised reconstruction ladder

The one-dimensional reconstruction ladder can now be sharpened.

### `R0`

\[
I=M_{fin}(\mathbb Z,K).
\]

Local addressability only.

### `R1`

\[
(I,U).
\]

Oriented line up to translation.

### `R2`

\[
(I,U,V).
\]

Rooted signed line geometry.

### `R2.5` — Primitive provenance marker

Add the information specifying which generated operators are declared primitive translations of which operation symbol.

Without this layer, Theorem 5.1 applies.

### `R3` — Definedness layer

Add each primitive operation domain \(D_\omega\), distinguishing terminal-valued cells from `UNDEF` cells.

### `R4` — Terminal geometry

Add terminal sorts and terminal involutions.

### `R5` — Terminal incidence

Add the cell-to-terminal-value attachment relation.

At `R5`, the current signed M0 is completely reconstructed; equivalently, one may replace `R2.5`–`R5` by the finite schema datum \(\mathfrak R_{M0}\).

---

## 10. Information types now separated

The current one-dimensional theory distinguishes at least five independent kinds of information:

1. **coordinate addressability** — carried by matrix units;
2. **line geometry** — carried by conjugation with \(U,V\);
3. **primitive provenance** — which operators were primitive laws rather than derived operators;
4. **definedness** — whether an absent base value means terminal output or true `UNDEF`;
5. **terminal attachment** — which typed output is produced by which primitive cell.

The classical linear shadow can preserve (1) and, with distinguished kinematic operators, reconstruct (2), while forgetting (3)–(5).

This is a more precise statement than saying merely that “classical algebra loses information.”

---

## 11. Publication-level theorem nucleus

The following chain is now proved entirely in one dimension:

\[
\boxed{
\begin{array}{c}
\text{legacy signed partial FCOA}\[1mm]
\downarrow\text{ operator generation}\[1mm]
M_{fin}(\mathbb Z,K)\triangleleft\mathcal A^{1D}\to M_2(K[t,t^{-1}])\[1mm]
\downarrow\text{ enrichment by }U,V\[1mm]
\text{exact reconstruction of the rooted signed line}\[1mm]
\not\Downarrow\[1mm]
\text{primitive operation provenance / definedness / terminal attachment}.
\end{array}}
\tag{11.1}
\]

Together with the earlier direct Associative Collapse Theorem, this gives a closed conceptual package:

- directly forcing the legacy value law into associativity collapses the carrier;
- composing translations generates ordinary associative structures without carrier collapse;
- the resulting classical shadow can recover the carrier geometry at sufficient resolution;
- but it still cannot recover which primitive law generated its operators or which terminal/undefined distinctions were erased.

This is the first point at which the Shadow Ladder programme forms a publication-sized theorem package rather than an open-ended collection of examples.

---

## 12. Immediate audit tasks before publication

Before publication, the following must be completed:

1. hostile audit of Theorems 4.1, 5.1, 6.1, and 8.1;
2. exact prior-art comparison with:
   - transformation semigroup representations;
   - Brandt matrix units;
   - algebraic Toeplitz/Jacobson extensions;
   - Leavitt path algebras;
   - reconstruction from operator algebras with distinguished shifts;
3. separate source-specific novelty from classical ingredients;
4. prepare RU/EN article with all theorem proofs and scope limitations;
5. publication metadata and DOI placeholder only until a DOI is actually assigned.

No higher-dimensional construction is needed or permitted for this publication package.