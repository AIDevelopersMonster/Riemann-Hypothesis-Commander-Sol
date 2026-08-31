# SOL-TOPO — LC2 Reflection/Provenance Fiber and a Projective Ising Braid Subsystem

**Version:** 0.2  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** LC2 CONSTRUCTION + CONDITIONAL PROJECTIVE ISING BRAID REPRESENTATION + COHERENCE INDEPENDENCE BOUNDARY  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_TOPO_REPORT_v0_1.md`, `SIGNED_M0_REFLECTION_TRANSFER_0_1.md`, `LINE_COMPLETION_GATE.md`

---

## 1. Executive verdict

The second SOL-TOPO strike substantially sharpens the first report.

The current terminal-output semantics cannot produce a nontrivial Ising `F`-matrix by deterministic set-level re-entry. However, the already available **split reflection fiber** contains exactly the raw two-state geometry needed for a canonical linearized construction.

On a split terminal orbit

\[
Q=\{e,\bar e\},
\qquad
\nu_O(e)=\bar e,
\qquad
\nu_O(\bar e)=e,
\tag{1}
\]

retain the legacy/reflected provenance and freely linearize over `C`. Two canonical involutions appear:

\[
J(e)=\bar e,
\qquad J(\bar e)=e,
\tag{2}
\]

and

\[
S(e)=e,
\qquad S(\bar e)=-\bar e.
\tag{3}
\]

They satisfy

\[
J^2=S^2=I,
\qquad
JS=-SJ.
\tag{4}
\]

Therefore the split FCOA output orbit already generates the two-dimensional real Clifford algebra pattern underlying the Pauli pair `X,Z`.

The normalized symmetric exchange operator

\[
\boxed{
F=\frac{J+S}{\sqrt2}
}
\tag{5}
\]

is then forced by a precise minimal duality requirement and has matrix

\[
F=rac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\tag{6}
\]

This is exactly the standard nontrivial Ising matrix

\[
F^{\sigma\sigma\sigma}_{\sigma}.
\tag{7}
\]

Next let adjacent exchange preserve the two channel labels, so up to overall phase

\[
R_t=
\begin{pmatrix}
1&0\\
0&t
\end{pmatrix},
\qquad |t|=1.
\tag{8}
\]

Set

\[
B_t=F R_t F.
\tag{9}
\]

The braid/Yang-Baxter relation

\[
R_tB_tR_t=B_tR_tB_t
\tag{10}
\]

holds if and only if

\[
\boxed{(t-1)(t^2+1)=0.}
\tag{11}
\]

Thus the only non-scalar solutions are

\[
\boxed{t=\pm i.}
\tag{12}
\]

For `t=i`, this is the Ising exchange matrix up to the standard common phase:

\[
R_{\sigma\sigma}
=e^{-i\pi/8}
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix}.
\tag{13}
\]

Hence a minimal LC2-enriched FCOA split fiber reproduces the **projective** Ising `F/R` braid-qubit subsystem without inserting the Hadamard coefficients or the relative phase `i` by hand.

But the hostile boundary is equally important:

- the identification of the two canonical FCOA bases with the two association bases is a new LC2 semantic axiom;
- the braid relation itself is a new coherence axiom;
- the global Ising phase `e^{-i pi/8}` is not fixed;
- the full pentagon/hexagon system is not yet generated;
- therefore this is not a derivation of anyon physics from the old one-line FCOA.

The correct verdict is

\[
\boxed{
\texttt{MODEL CANDIDATE — PROJECTIVE FOUR-}\sigma\texttt{ BRAID-QUBIT SUBSYSTEM}
}
\tag{14}
\]

for the **LC2-enriched** theory, not for raw FCOA-Z.

---

## 2. Why set-level LC2 is insufficient

The first report proved that old `E`-outputs are sinks. Suppose we now allow re-entry but add no additive or scalar structure.

Let `Q` be a finite set of active output states, and suppose every new reassociation/transport law remains deterministic:

\[
f:Q\to Q.
\tag{15}
\]

After free linearization, `f` acts on basis vectors by

\[
e_q\mapsto e_{f(q)}.
\tag{16}
\]

If `f` is reversible, its matrix is a permutation matrix. If one additionally allows a nonzero scalar weight on each basis state, the matrix is monomial.

### Theorem 2.1 — Monomial re-entry obstruction

No reversible deterministic set-level LC2 re-entry law can induce the Ising matrix

\[
H=rac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\tag{17}
\]

### Proof

A reversible map of a two-element set has a permutation matrix, hence exactly one nonzero entry in each row and column. More generally, a weighted reversible basis map is monomial and still has exactly one nonzero entry in each row and column. Matrix (17) has two nonzero entries in each row and each column. Therefore it is not induced by any deterministic basis-state permutation or weighted permutation. QED.

### Corollary 2.2

A genuine Ising `F`-shadow requires an additive superposition layer. Purely set-valued LC2 re-entry is insufficient.

This is the first exact minimum-resource statement of the second strike.

---

## 3. The split terminal orbit

The audited signed M0 transfer already provides two canonical terminal-output lifts.

For a fixed old terminal output `E_n^alpha`, the split lift introduces

\[
\bar E_n^\alpha\ne E_n^\alpha
\tag{18}
\]

with

\[
\nu_O(E_n^\alpha)=\bar E_n^\alpha,
\qquad
\nu_O(\bar E_n^\alpha)=E_n^\alpha.
\tag{19}
\]

Fix one such orbit and abbreviate

\[
e:=E_n^\alpha,
\qquad
\bar e:=\bar E_n^\alpha.
\tag{20}
\]

The old FCOA value is not replaced. We only promote the two already existing output elements to basis states of a new active fiber.

### Definition 3.1 — Minimal active split fiber

Define

\[
H_Q:=\mathbb C e\oplus\mathbb C\bar e.
\tag{21}
\]

The embedding

\[
Q\hookrightarrow H_Q
\tag{22}
\]

sends each old output element to its corresponding basis vector.

This is conservative in the sense that every old carrier and output element remains distinct and every old base-operation value is unchanged.

---

## 4. Two canonical involutions

Reflection extends linearly to

\[
J:H_Q\to H_Q,
\tag{23}
\]

with (2).

Because the signed construction remembers which output is inherited from the old positive branch and which is its reflected partner, define the provenance involution

\[
S:H_Q\to H_Q
\tag{24}
\]

by (3).

In the ordered basis `(e, bar e)`,

\[
J=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
S=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\tag{25}
\]

### Theorem 4.1 — Reflection/provenance Clifford relation

The operators `J,S` satisfy

\[
J^2=S^2=I,
\qquad
JS=-SJ.
\tag{26}
\]

Consequently,

\[
K:=JS
\tag{27}
\]

satisfies

\[
K^2=-I.
\tag{28}
\]

### Proof

The involution identities follow immediately from (2)-(3). On `e`,

\[
JS(e)=J(e)=\bar e,
\]

while

\[
SJ(e)=S(\bar e)=-\bar e.
\]

On `bar e`,

\[
JS(\bar e)=J(-\bar e)=-e,
\]

whereas

\[
SJ(\bar e)=S(e)=e.
\]

Thus `JS=-SJ`. Then

\[
K^2=JSJS=-J^2S^2=-I.
\]

QED.

### Interpretation

A complex-structure precursor appears before any spatial second coordinate is introduced:

\[
\boxed{
\text{split reflection orbit}
+
\text{retained provenance}
\longrightarrow
K^2=-I.
}
\tag{29}
\]

This is an **internal fiber statement**, not an emergent-space statement.

---

## 5. The canonical Hadamard theorem

There are two canonical observables on `H_Q`:

- `S`: which provenance side the basis state belongs to;
- `J`: reflection parity/exchange structure.

An LC2 reassociation transform should exchange these two descriptions if the two fusion-tree bases are identified respectively with the provenance basis and the reflection basis.

We formalize only this minimal duality.

### Definition 5.1 — Minimal association duality

A real-linear operator

\[
F\in\operatorname{span}_{\mathbb R}\{J,S\}
\tag{30}
\]

is a **minimal association duality** if

\[
F^2=I
\tag{31}
\]

and

\[
FJF=S.
\tag{32}
\]

The overall sign of `F` is regarded as gauge.

### Theorem 5.2 — Unique minimal association duality

Up to overall sign,

\[
\boxed{
F=\frac{J+S}{\sqrt2}.
}
\tag{33}
\]

Moreover,

\[
FSF=J.
\tag{34}
\]

### Proof

Write

\[
F=aJ+bS,
\qquad a,b\in\mathbb R.
\tag{35}
\]

Using (26),

\[
F^2=(a^2+b^2)I.
\tag{36}
\]

Thus (31) implies

\[
a^2+b^2=1.
\tag{37}
\]

A direct expansion gives

\[
FJF=(a^2-b^2)J+2abS.
\tag{38}
\]

Equation (32) therefore requires

\[
a^2-b^2=0,
\qquad
2ab=1.
\tag{39}
\]

Hence

\[
a=b=\frac1{\sqrt2}
\]

or both coefficients are simultaneously negated, which changes only the overall sign of `F`. Equation (34) follows symmetrically. QED.

### Corollary 5.3 — Ising `F` form

In basis `(e,bar e)`,

\[
\boxed{
F=rac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
}
\tag{40}
\]

This equals the conventional matrix for

\[
F^{\sigma\sigma\sigma}_{\sigma}
\tag{41}
\]

in the standard Ising gauge.

### Scope warning

Equation (40) is **not** claimed to be forced by raw FCOA alone. What is forced is:

1. `J` from the split reflection lift;
2. `S` from retained signed provenance;
3. the coefficients of `F` once the LC2 association-duality axiom (30)-(32) is adopted.

The identification of the two canonical FCOA bases with the two fusion-tree association bases is new model semantics.

---

## 6. Channel-preserving exchange

In an Ising fusion basis, exchange of the adjacent pair does not change its total fusion channel, so the exchange matrix is diagonal in that basis.

We impose only the corresponding finite-fiber condition.

### Definition 6.1 — Type-preserving phase exchange

Let

\[
P_+=\frac{I+S}{2},
\qquad
P_-=\frac{I-S}{2}.
\tag{42}
\]

A unitary channel-preserving exchange is

\[
R=aP_++bP_-,
\qquad |a|=|b|=1.
\tag{43}
\]

Up to a common phase, write

\[
R_t=P_++tP_-
=
\begin{pmatrix}
1&0\\
0&t
\end{pmatrix},
\qquad |t|=1.
\tag{44}
\]

The exchange of the neighboring pair in the reassociated basis is

\[
B_t=FR_tF.
\tag{45}
\]

Using (40),

\[
B_t=rac12
\begin{pmatrix}
1+t&1-t\\
1-t&1+t
\end{pmatrix}.
\tag{46}
\]

---

## 7. The braid-selection theorem

### Theorem 7.1 — Relative-phase classification

The braid relation

\[
R_tB_tR_t=B_tR_tB_t
\tag{47}
\]

holds if and only if

\[
\boxed{(t-1)(t^2+1)=0.}
\tag{48}
\]

Hence

\[
t\in\{1,i,-i\}.
\tag{49}
\]

### Proof

Substitute (44) and (46). Direct multiplication gives

\[
R_tB_tR_t-B_tR_tB_t
=
\frac{(t-1)(t^2+1)}4
\begin{pmatrix}
-1&1\\
1&1
\end{pmatrix}.
\tag{50}
\]

The displayed constant matrix is nonzero. Therefore (47) is equivalent to the scalar factor in (50) vanishing, which is exactly (48). QED.

### Corollary 7.2 — Nontrivial braid solutions

The solution `t=1` makes `R_t` scalar and therefore carries no non-Abelian channel distinction.

The two non-scalar solutions are

\[
\boxed{t=\pm i.}
\tag{51}
\]

They are exchanged by complex conjugation, corresponding to opposite braid chirality.

### Corollary 7.3 — Exact projective Ising `R`

For `t=i`,

\[
R_i=
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix}.
\tag{52}
\]

The standard Ising matrix is

\[
R_{\sigma\sigma}
=e^{-i\pi/8}R_i.
\tag{53}
\]

Thus the LC2 construction determines the Ising **relative channel phase** exactly, while leaving the common phase undetermined.

The conjugate solution `t=-i` gives the opposite chirality.

---

## 8. Non-Abelianity theorem

### Theorem 8.1

For `t=i`, the two adjacent braid generators

\[
R:=R_i,
\qquad
B:=FR_iF
\tag{54}
\]

do not commute.

### Proof

From (46),

\[
B=
\frac12
\begin{pmatrix}
1+i&1-i\\
1-i&1+i
\end{pmatrix}.
\tag{55}
\]

Direct multiplication yields

\[
[R,B]
=RB-BR
=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}
\ne0.
\tag{56}
\]

QED.

Thus the resulting braid representation is genuinely non-Abelian on the two-dimensional internal fiber even though the underlying FCOA spatial carrier remains a line.

---

## 9. Four-`sigma` braid-qubit subsystem

For four Ising `sigma` anyons with fixed trivial total charge, the fusion space is two-dimensional. In the conventional basis, the braid generators may be represented projectively by

\[
\rho(b_1)=R,
\qquad
\rho(b_2)=B=FRF,
\qquad
\rho(b_3)=R.
\tag{57}
\]

### Theorem 9.1 — Projective `B_4` representation

For `t=\pm i`, the assignment (57) satisfies

\[
\rho(b_1)\rho(b_2)\rho(b_1)
=
\rho(b_2)\rho(b_1)\rho(b_2),
\tag{58}
\]

\[
\rho(b_2)\rho(b_3)\rho(b_2)
=
\rho(b_3)\rho(b_2)\rho(b_3),
\tag{59}
\]

and

\[
\rho(b_1)\rho(b_3)
=
\rho(b_3)\rho(b_1).
\tag{60}
\]

### Proof

Equations (58)-(59) are both instances of Theorem 7.1 because `rho(b_1)=rho(b_3)=R`. Equation (60) is immediate because the two matrices are equal. QED.

### Target match

This is exactly the standard projective Ising braid-qubit matrix pattern. The common phase omitted from each exchange generator does not affect the braid relations because both sides of every braid relation contain the same number of generators.

---

## 10. Complex-phase necessity

The first positive construction can be made over `R`, but the nontrivial braid phase cannot.

### Theorem 10.1 — No non-scalar real channel-preserving braid solution

If `t` in (44) is required to be real, unitary, and nonzero, then the only solution of the braid relation is

\[
t=1.
\tag{61}
\]

Hence no non-scalar real diagonal channel-preserving exchange exists in this two-state model.

### Proof

By Theorem 7.1, `t` must be one of `1, i, -i`. Only `1` is real. QED.

### Corollary 10.2

A nontrivial braid realization requires either

1. complex amplitudes on the two-state fiber, or
2. an equivalent real enlargement carrying an internal complex structure.

This is an internal **phase-memory cost**, not a second spatial coordinate.

---

## 11. Conservative LC2 realization

The extension can now be stated in the format required by `LINE_COMPLETION_GATE.md`.

### Input sort

A split terminal orbit

\[
Q_n^\alpha
=\{E_n^\alpha,\bar E_n^\alpha\}.
\tag{62}
\]

### Active output/re-entry sort

\[
H_n^\alpha
=\mathbb C[Q_n^\alpha].
\tag{63}
\]

### Old-output embedding

\[
E_n^\alpha\mapsto e,
\qquad
\bar E_n^\alpha\mapsto\bar e.
\tag{64}
\]

### Re-entry/transport operations

\[
J,S,F,R,B:H_n^\alpha\to H_n^\alpha.
\tag{65}
\]

### Reflection action

`J` is precisely the linear extension of the old output reflection.

### Closure

All new transport maps remain inside the finite internal fiber `H_n^alpha`.

### Legacy exactness

No old base-base operation cell changes value or definedness.

### Result

At this stage the construction is

\[
\boxed{\texttt{1D-CLOSED}}
\tag{66}
\]

with respect to spatial carrier dimension.

The new resource is a two-dimensional complex internal fiber, not an independently iterable spatial coordinate.

---

## 12. Coherence-independence theorem

The strongest anti-overclaim result is that FCOA does **not** force the braid phase by itself.

### Theorem 12.1 — Braid coherence is independent of the old FCOA data

For every phase

\[
t\in U(1),
\tag{67}
\]

the map `R_t` in (44) is a unitary, channel-preserving endomorphism of the active output fiber and leaves every old FCOA cell untouched.

Therefore the old signed FCOA structure plus conservative LC2 activation does not distinguish `t=i` from any other phase.

Only the additional braid-coherence equation (47) reduces the continuum of allowed phases to (49).

### Proof

For arbitrary `|t|=1`, matrix (44) is unitary and diagonal in the provenance/channel basis. It acts only on the new active fiber and does not alter any old base operation or output embedding. Thus every `t` gives a conservative LC2 transport endomorphism.

Theorem 7.1 shows that the special values `1, ±i` are selected only after imposing (47). Hence braid coherence is logically independent of the old FCOA data. QED.

### Consequence

The phrase

> FCOA generates Ising braiding

would be false at the current stage.

The correct statement is

\[
\boxed{
\text{FCOA split-output geometry generates the minimal }J,S,F\text{ scaffold;}
}
\tag{68}
\]

and

\[
\boxed{
\text{braid coherence then forces the Ising relative phase }\pm i.
}
\tag{69}
\]

---

## 13. What is generated and what is imported

### Generated from audited FCOA-Z data

1. a two-element split output orbit;
2. reflection `J`;
3. signed provenance `S` if provenance is retained;
4. anticommutation `JS=-SJ`;
5. internal complex-structure precursor `(JS)^2=-I`;
6. after free linearization and the association-duality requirement, the numerical Hadamard coefficients in `F`.

### New but minimal mathematical enrichment

1. free linear/additive structure on the output fiber;
2. identification of provenance and reflection bases with the two association bases;
3. unitary phase transport on the fiber;
4. braid/Yang-Baxter coherence.

### Not yet generated

1. the common Ising exchange phase `e^{-i pi/8}`;
2. topological spin data;
3. all one-dimensional `F` and `R` symbols of the full Ising category;
4. pentagon and hexagon coherence as consequences of FCOA laws;
5. arbitrary-many-anyon tensor/fusion spaces;
6. a topological derivation of braid words from line geometry.

---

## 14. Comparison with standard Ising data

A standard Ising convention has

\[
\sigma\times\sigma=1+\psi,
\tag{70}
\]

\[
F^{\sigma\sigma\sigma}_{\sigma}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\tag{71}
\]

and

\[
R_{\sigma\sigma}
=e^{-i\pi/8}
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix}.
\tag{72}
\]

For four `sigma` anyons, adjacent braid generators in the fusion basis are `R` and `FRF` and satisfy the Yang-Baxter relation.

These standard target facts are recorded, for example, in John Preskill's Physics 219 notes/exercises and in the review by Nayak, Simon, Stern, Freedman, and Das Sarma.

The LC2 construction reproduces (71) exactly and (72) projectively, including its nontrivial relative phase.

---

## 15. Publication assessment

The second strike reaches a materially stronger threshold than v0.1:

\[
\boxed{
\text{a finite }F/R\text{ toy system satisfying braid relations has now been constructed.}
}
\tag{73}
\]

However, a standalone publication should still not claim a new anyon model. The algebra `X,Z,H` and the Ising/Clifford braid representation are classical. The potentially distinctive content is only their **generation route from the audited FCOA split-output/provenance architecture**.

Before independent publication, one further hostile gate is required:

\[
\boxed{
\text{Can pentagon/hexagon coherence, or an obstruction to it, be derived from LC2 re-entry rather than imposed?}
}
\tag{74}
\]

If the answer is positive, the SOL-TOPO line likely crosses the standalone publication threshold. If the answer is a strong no-go theorem showing that full coherence necessarily requires an independent tensor/fusion layer, that no-go is also publication-grade.

Current recommendation:

\[
\boxed{
\texttt{KEEP IN BRANCH / MODEL-CANDIDATE THRESHOLD REACHED / ONE COHERENCE STRIKE REMAINS.}
}
\tag{75}
\]

---

## 16. Next strike

The next problem is now narrow:

\[
\boxed{
\text{Does the reflection/provenance LC2 fiber extend to a coherent Ising fusion system?}
}
\tag{76}
\]

There are two acceptable outcomes.

### Construction route

Build the smallest fusion-tree/tensor extension in which:

1. the nontrivial `F` remains (33);
2. the relative `R` remains (51);
3. pentagon and hexagon identities hold;
4. old FCOA cells remain an exact substructure;
5. no full Ising category table is simply copied in by hand.

### Obstruction route

Prove that the old FCOA plus LC2 fiber lacks enough compositional information to force the missing coherence data, and identify the minimum independent new resource: tensor product, fusion-tree address, quantum dimension, topological twist, or another memory layer.

This is the next publication gate.

---

## 17. Literature anchors

1. J. Preskill, *Physics 219c/CS 219c exercises*, 2018, Ising anyons section: `sigma x sigma = 1 + psi`, `F = H`, `R = exp(-i pi/8) diag(1,i)`, and the adjacent braid generator `B = F R F`.
2. C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. Das Sarma, **Non-Abelian Anyons and Topological Quantum Computation**, *Rev. Mod. Phys.* **80** (2008), 1083. DOI: `10.1103/RevModPhys.80.1083`.
3. L. S. Georgiev, **Topological Quantum Computation with the universal R matrix for Ising anyons**, arXiv:`0812.2333`.

The external literature supplies the target Ising structure. Theorems 2.1, 4.1, 5.2, 7.1, 10.1, and 12.1 are the FCOA-side analysis carried out in this report.

---

## 18. Final conclusion

The second SOL-TOPO strike does **not** overturn the strict-line braid-topology no-go from v0.1. Instead it identifies the precise way around it:

\[
\boxed{
\text{keep the spatial carrier one-dimensional, but activate a finite internal output fiber.}
}
\tag{77}
\]

On that fiber, audited FCOA reflection plus retained provenance generate two anticommuting involutions. Their canonical duality transform is the Ising Hadamard `F`. Braid coherence then selects the Ising relative exchange phase `±i`.

Thus:

\[
\boxed{
\text{strict-line topology does not braid,}
\qquad
\text{but an LC2 internal fiber can carry a non-Abelian braid representation.}
}
\tag{78}
\]

The remaining scientific question is whether full fusion coherence can itself emerge from the FCOA re-entry architecture or must be supplied as an independent new layer.