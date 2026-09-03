# SOL-QFIELD

**Scientific direction:** exchange / reaction channels / history memory / operator structure  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** `RESEARCH CORE CLOSED AT v0.17 / PUBLICATION CONTENT READY / ARTICLE ASSEMBLY NEXT`  
**Physical verdict:** `ANALOGY ONLY`  
**Line status:** `1D-CLOSED`

## Canonical robust core

The mature theorem chain is now

\[
\boxed{
\text{FCOA root-comb reconvergence}
\to
\text{Parikh-equivalent histories}
\to
\text{abelianization fibers}
\to
\text{finite collision graph}
\to
\text{relative augmentation sector}
\to
\text{canonical tight collision frame}
\to
\text{constructive finite witness depth}.
}
\]

The earlier direct Clifford/CAR construction survives only as a conditional Coxeter-coordinate corollary. It is no longer part of the canonical theorem chain.

---

# 1. Permanent physical separation

SOL-QFIELD keeps distinct

\[
\boxed{
\text{exchange antisymmetry}
\ne
\text{field/operator anticommutation}
\ne
\text{scattering/annihilation channel structure}.
}
\]

Current FCOA still lacks the structures required for a genuine QFT model: physical Hilbert/Fock space, CAR/CCR fields, Hamiltonian dynamics, S-matrix, Lorentz/Poincare structure, conservation laws, amplitudes/cross-sections, gauge structure and a measurement postulate.

Therefore

\[
\boxed{\texttt{QFT STATUS: ANALOGY ONLY}.}
\]

---

# 2. Native root-comb reconvergence

For non-root points,

\[
L:x\mapsto x_0\oplus x=x,
\qquad
R:x\mapsto x\oplus x_0=\rho(x).
\]

For every safe finite history word \(w\),

\[
\boxed{
F_w(x_k)=\rho^{\#_R(w)}(x_k).
}
\]

Thus two histories with the same binary Parikh vector

\[
\Psi(w)=(\#_L(w),\#_R(w))
\]

reconverge to the same carrier endpoint.

This is the FCOA-specific input to the abstract group theorem below.

---

# 3. Minimal reversible finite history

The route pair

\[
LR\ne RL
\]

requires noncommuting reversible history images.

Every group of order below six is abelian, while \(S_3\) is not. Hence the cardinality-minimal reversible history group has

\[
\boxed{|G_{\rm hist}|=6,}
\]

with \(S_3\) as the minimal realization.

This remains a finite internal history fiber over the one-dimensional signed carrier.

---

# 4. General Parikh-Abelianization Collision Theorem

Let \(\Sigma\) be a finite alphabet and let

\[
h:\Sigma^*\twoheadrightarrow G
\]

be a monoid-surjective morphism into a group \(G\).

For \(g,g'\in G\), write

\[
g\sim_Pg'
\]

when there exist Parikh-equivalent words \(u,v\) with

\[
h(u)=g,
\qquad
h(v)=g'.
\]

Then

\[
\boxed{
g\sim_Pg'\iff g^{-1}g'\in[G,G].}
\]

Equivalently,

\[
\boxed{G/\!\sim_P\cong G_{\rm ab}=G/[G,G].}
\]

For finite groups, generation by the letter images as a group already implies monoid-surjectivity, because inverses are positive powers.

This theorem subsumes the former special \(S_3\) parity classification.

---

# 5. Finite collision graph

For finite \(G\), let

\[
H=[G,G],
\qquad d=|H|,
\qquad m=|G/H|.
\]

The collision graph is exactly

\[
\boxed{
\Gamma_P=\coprod_{G/H}K_d.
}
\]

That is, every abelianization coset is a complete collision component and there are no cross-coset edges.

For \(S_3\),

\[
H=A_3,
\qquad d=3,
\qquad m=2,
\]

so

\[
\boxed{\Gamma_P=K_3\sqcup K_3.}
\]

---

# 6. Canonical collision ideal

Under the optional complex-linearization layer

\[
A=\mathbb C[G],
\]

define the collision-residue span

\[
J_P
=
\operatorname{span}_{\mathbb C}\{g-g':g\sim_Pg'\}.
\]

Then

\[
\boxed{
J_P
=
\ker\!\left(\mathbb C[G]\to\mathbb C[G_{\rm ab}]\right)
=
I([G,G];G),
}
\]

the classical relative augmentation ideal of the derived subgroup.

For finite \(G\), if

\[
e_H=\frac1{|H|}\sum_{h\in H}h,
\]

then

\[
\boxed{J_P=\mathbb C[G](1-e_H).}
\]

Thus the group algebra splits canonically into

\[
\boxed{
\mathbb C[G]
=
\mathbb C[G]e_H
\oplus
\mathbb C[G](1-e_H),
}
\]

where the first summand is abelianization-visible and the second is the Parikh-order-sensitive collision sector.

For \(S_3\),

\[
1-e_{A_3}=e_{\rm std},
\]

hence

\[
\boxed{
J_P\cong M_2(\mathbb C).
}
\]

This is the canonical explanation of the matrix sector previously found through a selected commutator residue.

---

# 7. Universal canonical tight collision frame

Equip \(\mathbb C[G]\) with the coefficient inner product making the group basis orthonormal.

For every unordered collision edge define

\[
r_{g,g'}=\frac{g-g'}{\sqrt2}.
\]

Then the collection of all such vectors is a unit-norm tight frame for \(J_P\) with

\[
\boxed{
S_P=\frac{|[G,G]|}{2}I_{J_P}.
}
\]

Hence every \(x\in J_P\) admits the canonical reconstruction

\[
\boxed{
 x
 =
 \frac{2}{|[G,G]|}
 \sum_{r\in\mathcal R_P}
 \langle x,r\rangle r.
}
\]

For \(S_3\),

\[
|[S_3,S_3]|=3,
\]

so

\[
\boxed{S_P=\frac32I.}
\]

This recovers the six-vector route frame of v0.12 as the first nontrivial member of the general theorem.

---

# 8. Constructive finite witness-depth theorem

For finite \(G\), let \(\delta_+\) be the positive Cayley diameter of the letter images and let \(\delta_H\) be the Cayley diameter of \(H=[G,G]\) with respect to conjugates of the basic letter commutators.

Every collision \(g\sim_Pg'\) has Parikh-equivalent witnesses of common length at most

\[
\boxed{
B(h)
\le
\delta_+
+
\delta_H(2\delta_++2).
}
\]

Using the elementary finite bounds

\[
\delta_+\le|G|-1,
\qquad
\delta_H\le|[G,G]|-1,
\]

we obtain

\[
\boxed{
B(h)
\le
|G|-1+2|G|(|[G,G]|-1)
<2|G|^2.
}
\]

This is a universal effective bound, not claimed sharp.

---

# 9. Sharp S3 depth certificate

For the minimal noncommuting \(S_3\) history quotient, exhaustive verification over all 18 ordered noncommuting generator pairs gives

\[
\boxed{B_{S_3}^{\rm universal}=5.}
\]

More precisely:

- 12 ordered pairs close by depth 4;
- 6 ordered transposition/transposition pairs require depth 5.

Verifier:

[`verify_parikh_collision_s3.py`](./verify_parikh_collision_s3.py)

The conceptual theorem is primary; the script is a finite certificate and regression test.

---

# 10. Qualified Clifford/CAR side branch

The hostile audit in v0.11 found a genuine canonicity defect in the original v0.9 construction.

Cardinality minimality selects size six, but it does **not** force the two primitive history images to be transpositions. Mixed noncommuting generator-order types exist.

Therefore a direct Clifford pair is not generator-independent.

If one adds the explicit Coxeter/involutive hypothesis

\[
h(L)^2=h(R)^2=e,
\]

then the selected route residues satisfy

\[
Q_x^2=Q_y^2=e_{\rm std},
\qquad
\{Q_x,Q_y\}=0,
\]

and one may define algebraic one-mode CAR generators

\[
c=\frac12(Q_x+iQ_y),
\qquad
c^*=\frac12(Q_x-iQ_y).
\]

Thus only the conditional chain remains:

\[
\boxed{
\texttt{INVOLUTIVE MINIMAL HISTORY}
\Rightarrow
\texttt{DIRECT CLIFFORD}
\Rightarrow
\texttt{ALGEBRAIC CAR}_1.
}
\]

It is a coordinate corollary inside the canonical \(M_2(\mathbb C)\) sector, not the canonical theorem itself.

---

# 11. Two-mode barrier

For the fixed minimal history algebra

\[
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C),
\]

one cannot embed

\[
\operatorname{CAR}_2\cong M_4(\mathbb C).
\]

Hence its matrix capacity is at most one finite CAR mode.

This dimension obstruction remains robust independently of whether a particular first-mode Clifford coordinate system is chosen.

---

# 12. Literature positioning

The following ingredients are standard background and are not novelty claims:

- Parikh maps / monoid abelianization;
- group abelianization and derived subgroups;
- commutative closure of regular/group languages;
- relative augmentation ideals;
- complete-graph Laplacians and edge tight frames;
- representation theory of \(S_3\);
- Clifford/CAR matrix identities.

The candidate contribution is the structural synthesis

\[
\boxed{
\text{history reconvergence}
\to
\text{Parikh collisions}
\to
\text{abelianization cosets}
\to
\text{relative augmentation sector}
\to
\text{canonical tight frame}
\to
\text{effective finite witness depth}.
}
\]

The literature audit did not locate this exact combined formulation in the sources consulted. This is a negative bibliographic result only; no “first” or priority claim is authorized.

---

# 13. Current ladder

\[
\boxed{
\begin{aligned}
QF0 &: \text{typed channel support},\\
QF1 &: \text{stochastic terminal weights},\\
QF2 &: \text{terminal complex weights},\\
QF2.5 &: \text{native root-comb reconvergence / Parikh fibers},\\
QF3a &: \text{minimal reversible finite history},\\
QF3b &: \mathbb C[G]\text{ optional complex linearization},\\
QF3c &: \text{Parikh-Abelianization Collision Theorem},\\
QF3d &: \text{coset-complete collision graph},\\
QF3e &: \text{canonical relative augmentation sector},\\
QF3f &: \text{canonical tight collision frame},\\
QF3g &: \text{effective finite witness depth},\\
QF3h &: \text{conditional Coxeter Clifford/CAR}_1,\\
QF4 &: \text{physical Hilbert/state/measurement dynamics — not reached},\\
QF5 &: \text{physical Fock/CAR/QFT structure — not reached}.
\end{aligned}
}
\]

All structures through QF3h remain finite internal history/operator fibers over the signed one-dimensional carrier.

---

# 14. Reports

- `SOL_QFIELD_REPORT_v0_1.md`
- `SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md`
- `SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md`
- `SOL_QFIELD_MINIMAL_HISTORY_v0_4.md`
- `SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md`
- `SOL_QFIELD_LINEARIZATION_v0_6.md`
- `SOL_QFIELD_ORDER_STATE_GNS_v0_7.md`
- `SOL_QFIELD_BINARY_OBSERVABLE_v0_8.md`
- `SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md` — qualified by v0.11
- `SOL_QFIELD_CAR_ONE_MODE_BARRIER_v0_10.md` — CAR existence qualified by v0.11
- `SOL_QFIELD_QUOTIENT_ROBUSTNESS_AUDIT_v0_11.md`
- `SOL_QFIELD_CANONICAL_ROUTE_FRAME_v0_12.md`
- `SOL_QFIELD_LITERATURE_POSITIONING_v0_13.md`
- `SOL_QFIELD_PARIKH_COLLISION_THEOREM_v0_14.md`
- `SOL_QFIELD_PARIKH_ABELIANIZATION_v0_15.md`
- `SOL_QFIELD_FINITE_WITNESS_BOUND_v0_16.md`
- `SOL_QFIELD_GENERAL_NOVELTY_AUDIT_v0_17.md`
- `verify_parikh_collision_s3.py`

---

# 15. Publication decision

\[
\boxed{
\texttt{SOL-QFIELD RESEARCH CORE CLOSED AT v0.17}.
}
\]

\[
\boxed{
\texttt{PUBLICATION CONTENT READY — BEGIN ARTICLE ASSEMBLY}.
}
\]

No additional exploratory theorem is required before publication.

The next work product should be the article itself, with:

1. independent proof reread;
2. theorem/lemma numbering normalization;
3. primary-source bibliography verification;
4. verifier supplement;
5. English master manuscript;
6. Russian companion version;
7. PDF/DOCX/HTML build as required;
8. final DOI/metadata audit before Zenodo release.

Recommended working title:

**Parikh Collisions, Abelianization, and Canonical Tight Frames from Finite Group Histories**
