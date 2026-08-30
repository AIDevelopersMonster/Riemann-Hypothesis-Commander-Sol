# SOL-GRADED — Exchange-Factor Selection and Mirror-Coupling Audit

**Version:** 0.2  
**Date:** 2026-08-30  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** SECOND TARGET COMPLETE / MIRROR-EXCHANGE THEOREM + EXCHANGE-FACTOR UNDERDETERMINATION  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_GRADED_REPORT_v0_1.md`, `SIGNED_M0_REFLECTION_TRANSFER_0_1.md`, `HOSTILE_AUDIT_SIGNED_M0_TRANSFER_0_1.md`, `LINE_COMPLETION_GATE.md`

---

## 1. Executive result

The second SOL-GRADED target asked whether a conservative generated mixed-sector law on the one-dimensional signed FCOA-Z line can force the nontrivial super exchange factor

\[
\epsilon(p,q)=(-1)^{pq}
\tag{1}
\]

instead of merely allowing it after an external `Z_2` grading has been chosen.

The answer under the **currently fixed FCOA-Z line axioms** is:

\[
\boxed{\text{the super exchange factor is not selected.}}
\tag{2}
\]

This is not a universal impossibility theorem for every future enriched FCOA. It is an exact underdetermination theorem for the present rooted-line + reversible-completion + derived-reflection + legacy-exactness core.

At the same time a stronger positive fact appears.

Let simultaneous reflection of an ordered pair be

\[
R_2(x,y)=(\nu x,\nu y)
\tag{3}
\]

and let argument exchange be

\[
S(x,y)=(y,x).
\tag{4}
\]

Then on the mixed **mirror locus**

\[
\mathcal M=\{(x,\nu x):x\ne P_0\}
\tag{5}
\]

the two actions coincide:

\[
\boxed{R_2=S\quad\text{on }\mathcal M.}
\tag{6}
\]

Therefore, on exactly this locus, reflection equivariance becomes an exchange law. If a mixed interaction has output `z`, then reversing its arguments gives the reflected output `nu_* z`. Consequently reflection-fixed outputs produce symmetric/commutative mirror interactions, while reflected two-cycle outputs produce noncommutative mirror interactions. After linearization, the reflection-even output component is exchange-symmetric and the reflection-odd output component is exchange-antisymmetric.

Thus the precise conclusion is:

\[
\boxed{
\text{line birth can generate an exchange decomposition locally,}
\quad
\text{but it does not yet select the global super braiding.}
}
\tag{7}
\]

The line-first verdict for exchange-factor selection is

\[
\boxed{\texttt{UNDERDETERMINED}.}
\tag{8}
\]

Two explicit conservative one-dimensional realizations witnessing the underdetermination are constructed below.

---

## 2. Fixed FCOA input

Use the signed carrier

\[
B^{\pm}=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}
\tag{9}
\]

with derived reflection

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\tag{10}
\]

The signed M0 transfer has already proved that the positive legacy ray is preserved exactly, the negative-negative sector is its simultaneous-reflection closure, and all genuinely mixed cells

\[
(P_i^+,P_j^-),\qquad(P_i^-,P_j^+)
\tag{11}
\]

remain `UNDEF` in the minimal baseline while being `OPEN` for later conservative realizations.

For `oplus`, the old signed rules include

\[
P_0\oplus x=x\qquad(x\ne P_0)
\tag{12}
\]

and

\[
x\oplus P_0=\rho(x)\qquad(x\ne P_0),
\tag{13}
\]

where `rho` contracts radial depth by one and commutes with reflection.

A reflection-compatible extension obeys

\[
\omega(\nu x,\nu y)=\nu_*\omega(x,y)
\tag{14}
\]

and its domain is invariant under simultaneous reflection.

The hostile audit explicitly fixed the scope: reflection equivariance is a canonical baseline class, not a universal axiom for every imaginable future signed FCOA operation. All no-go statements below retain that scope.

---

## 3. Pair-Involution Separation Theorem

Work on the non-root pair carrier

\[
B^*=B^{\pm}\setminus\{P_0\}.
\tag{15}
\]

Define two involutions on ordered pairs:

\[
R_2(x,y)=(\nu x,\nu y),
\qquad
S(x,y)=(y,x).
\tag{16}
\]

### Theorem 3.1 — pair-involution separation

The maps `R_2` and `S` satisfy

\[
R_2^2=S^2=\operatorname{id},
\qquad
R_2S=SR_2.
\tag{17}
\]

For a mixed nonzero pair `(x,y)`,

\[
\boxed{R_2(x,y)=S(x,y)\iff y=\nu x.}
\tag{18}
\]

Hence simultaneous reflection and exchange agree precisely on the mirror locus `M`.

### Proof

The involution identities follow from `nu^2=id`. Commutation follows directly:

\[
R_2S(x,y)=R_2(y,x)=(\nu y,\nu x)=SR_2(x,y).
\]

Now

\[
R_2(x,y)=S(x,y)
\]

means

\[
\nu x=y,
\qquad
\nu y=x.
\]

The first equality is `y=nu x`; the second then follows automatically from `nu^2=id`. Conversely, if `y=nu x`, both equalities hold. QED.

### Coordinate form

For `n,m>0`, let

\[
a=(P_n^+,P_m^-).
\]

Then

\[
R_2a=(P_n^-,P_m^+),
\qquad
Sa=(P_m^-,P_n^+).
\tag{19}
\]

They coincide exactly when `n=m`.

If `n != m`, the orbit under the commuting involutions is generically the four-point set

\[
\begin{aligned}
&(P_n^+,P_m^-),
(P_n^-,P_m^+),\\
&(P_m^-,P_n^+),
(P_m^+,P_n^-).
\end{aligned}
\tag{20}
\]

Thus reflection and exchange generate distinct directions in pair space away from the mirror diagonal.

### Corollary 3.2 — off-mirror no-go

Reflection equivariance alone cannot impose a relation between

\[
\omega(x,y)
\quad\text{and}\quad
\omega(y,x)
\tag{21}
\]

for a mixed pair with `y != nu x`, because the reversed pair belongs to a different `R_2` orbit.

Therefore a global exchange factor cannot be derived from simultaneous reflection alone. An exchange-sensitive additional principle is required.

This is the first exact obstruction.

---

## 4. Mirror-Exchange Theorem

The separation theorem has one exceptional locus where geometry really does become exchange.

### Theorem 4.1 — mirror exchange

Let `omega` be a reflection-equivariant partial binary operation, and suppose

\[
(x,\nu x)\in D_\omega,
\qquad x\ne P_0.
\tag{22}
\]

Then the reversed cell is automatically defined and

\[
\boxed{
\omega(\nu x,x)=\nu_*\omega(x,\nu x).
}
\tag{23}
\]

### Proof

Since

\[
R_2(x,\nu x)=(\nu x,x)=S(x,\nu x),
\]

domain reflection invariance forces the reversed cell to be defined. Equation (14) then gives (23). QED.

This is the cleanest one-dimensional instance found so far of

\[
\boxed{\text{geometry of the participants determines the exchange law}.}
\tag{24}
\]

No grading has been assigned to the two sides to obtain (23).

---

## 5. Mirror-Orbit Classification Theorem

Let

\[
z=\omega(x,\nu x).
\tag{25}
\]

Because `nu_*` is an involution, every output belongs either to a fixed-point orbit or to a two-cycle.

### Theorem 5.1 — exact mirror commutation classification

For every reflection-equivariant mirror cell:

1. if
   \[
   \nu_*z=z,
   \tag{26}
   \]
   then
   \[
   \omega(x,\nu x)=\omega(\nu x,x),
   \tag{27}
   \]
   so the mirror interaction is commutative;

2. if
   \[
   \nu_*z\ne z,
   \tag{28}
   \]
   then
   \[
   \omega(x,\nu x)\ne\omega(\nu x,x),
   \tag{29}
   \]
   while both directions are defined.

No one-sided definedness status can occur on a reflection-compatible mirror cell.

### Proof

Immediate from (23). QED.

### Corollary 5.2 — unique commutative base-valued mirror output

Assume the output lies in the base line `B^{+-}`. The only base point fixed by reflection is the root `P_0`. Therefore

\[
\boxed{
\text{base-valued + reflection-equivariant + mirror-commutative}
\Longrightarrow
\omega(x,\nu x)=P_0.
}
\tag{30}
\]

Thus root/cancellation is not merely one convenient symmetric base-valued mirror rule. It is the **unique** one under these hypotheses.

This is an FCOA-internal theorem, not a SUSY analogy.

---

## 6. Linearized Mirror Exchange Decomposition

Let the output sort be freely linearized over a field `K` with `char K != 2`, and let `J_O` be the linear reflection involution. Write

\[
P_{\bar0}^O=\frac{I+J_O}{2},
\qquad
P_{\bar1}^O=\frac{I-J_O}{2}.
\tag{31}
\]

For

\[
z=z_{\bar0}+z_{\bar1},
\qquad
J_Oz_{\bar0}=z_{\bar0},
\qquad
J_Oz_{\bar1}=-z_{\bar1},
\tag{32}
\]

Theorem 4.1 gives

\[
\omega(\nu x,x)
=J_Oz
=z_{\bar0}-z_{\bar1}.
\tag{33}
\]

Hence

\[
P_{\bar0}^O\omega(\nu x,x)
=P_{\bar0}^O\omega(x,\nu x),
\tag{34}
\]

while

\[
P_{\bar1}^O\omega(\nu x,x)
=-P_{\bar1}^O\omega(x,\nu x).
\tag{35}
\]

Therefore the line itself produces, on the mirror locus, an exact decomposition into

\[
\boxed{
\text{reflection-even output channel} \Rightarrow \text{exchange-symmetric},
}
\tag{36}
\]

and

\[
\boxed{
\text{reflection-odd output channel} \Rightarrow \text{exchange-antisymmetric}.
}
\tag{37}
\]

This is the strongest positive SOL-GRADED result so far.

It is important that (36)-(37) are **output-grade laws on a geometrically selected interaction locus**. They are not yet the Lie-super input law

\[
[a,b]=-(-1)^{pq}[b,a].
\tag{38}
\]

The raw branch states are not homogeneous parity states, as proved in v0.1.

---

## 7. Conservative realization A — mirror cancellation

Define a new partial operation `oplus_c` by preserving every old signed-M0 `oplus` cell and opening precisely the generated mirror family

\[
\boxed{
x\oplus_c\nu x=P_0\qquad(x\ne P_0).}
\tag{39}
\]

Since `x` ranges over both branches, both argument orientations are included.

### Theorem 7.1 — conservative realization

The extension (39) is a conservative one-dimensional realization under the Line Completion Gate.

### Proof / gate audit

**Legacy exactness.** Every old defined cell keeps its old value. Mixed nonzero cells were previously `UNDEF`, so there is no overlap.

**Positive-ray exactness.** No pair in (39) lies wholly in the positive legacy ray.

**Reflection coherence.** Since `nu P_0=P_0`,

\[
\nu x\oplus_c x=P_0=\nu(P_0).
\]

**Generated rule.** The domain condition is the structural equation `y=nu x`; it is not a finite exception table and does not use ordinary addition or multiplication.

**Finite-window coherence.** Restricting (39) to radial depth at most `N` gives exactly the restriction of the `N+1` rule, so the finite windows nest coherently.

**Closure.** Every new value returns to the existing base root. No new carrier is needed.

Therefore the realization is `1D-CLOSED`. QED.

### Commutation effect

Every mirror pair is now two-way defined and equal:

\[
x\oplus_c\nu x
=\nu x\oplus_c x
=P_0.
\tag{40}
\]

On a symmetric window with depths `1,...,N`, this adds `2N` ordered commuting cells to the previously audited `2N` diagonal commuting cells, so

\[
|Comm_{\oplus_c}(W_N)|=4N.
\tag{41}
\]

The old root/nonzero noncommutativity survives unchanged.

### Association effect

The realization creates a genuine `NEQ` witness where both bracketings are defined. Let `y=nu x`, `x != P_0`. Then

\[
(x\oplus_c y)\oplus_c x
=P_0\oplus x
=x,
\tag{42}
\]

while

\[
x\oplus_c(y\oplus_c x)
=x\oplus P_0
=\rho(x).
\tag{43}
\]

Since `rho(x) != x`,

\[
\boxed{\mathcal A_{\oplus_c}(x,\nu x,x)=NEQ.}
\tag{44}
\]

Thus a commutative mixed mirror law does not make the operation locally associative.

### Automorphism / memory effect

The minimal signed `oplus` reduct already has exact finite active-output automorphism group `C_2`, generated by global reflection. Adding a relation can only shrink that group, and reflection still preserves (39). Hence

\[
\boxed{Aut(W_N,\oplus_c)\cong C_2.}
\tag{45}
\]

The operation still remembers root and radial depth but not absolute branch orientation.

### Arithmetic leakage

The new rule supplies an inverse-like / cancellation relation on exactly the reflection pair. For nonzero base arguments it makes

\[
y=\nu x
\Longrightarrow
x\oplus_c y=P_0.
\tag{46}
\]

This is an additive-looking local feature and must be recorded as such. However it does not define any off-mirror sum law and no reconstruction of full ordinary `Add` or `Mul` is proved here. Full additive definability remains open because reflection itself is not an obstruction to ordinary addition.

### Mathematical meaning

The rule is a **root-valued mirror cancellation coupling** on one line. No particle-antiparticle, vacuum, annihilation, or SUSY interpretation is claimed.

---

## 8. Conservative realization B — split mirror terminal fiber

The previous realization is not forced. Construct an incompatible conservative realization.

For every radial depth `n>=1`, add two terminal outputs

\[
F_n,
\qquad
\overline F_n,
\qquad
F_n\ne\overline F_n,
\tag{47}
\]

with

\[
\nu_F(F_n)=\overline F_n,
\qquad
\nu_F(\overline F_n)=F_n.
\tag{48}
\]

They do not re-enter any operation.

Preserve every old `oplus` cell and define

\[
P_n^+\oplus_F P_n^-=F_n,
\tag{49}
\]

\[
P_n^-\oplus_F P_n^+=\overline F_n.
\tag{50}
\]

### Theorem 8.1

The split-fiber rule is also a conservative `1D-CLOSED` realization.

### Proof

Old cells and the positive ray are untouched. Equations (49)-(50) are exchanged by simultaneous reflection together with (48). The rule is uniform in radial depth, hence finite-window coherent. Every new value lies in a finite two-state terminal fiber over an already existing radial index and has no independent iteration. No second unbounded coordinate is introduced. QED.

### Commutation effect

For each mirror pair, both directions are defined but unequal:

\[
P_n^+\oplus_F P_n^-
\ne
P_n^-\oplus_F P_n^+.
\tag{51}
\]

Thus the old equality-commutation count remains `2N`, while the mirror sector contributes `2N` ordered `defined-but-unequal` cells.

### Association effect

Because `F_n` and `bar F_n` are terminal, they cannot be outer arguments. For example,

\[
(P_0\oplus x)\oplus_F\nu x
=x\oplus_F\nu x
\tag{52}
\]

is defined, while

\[
P_0\oplus(x\oplus_F\nu x)
\tag{53}
\]

is undefined. Thus the extension creates `LEFT` association statuses rather than the `NEQ` witness of the cancellation realization.

### Automorphism / memory effect

Again the old operation already bounds the finite base automorphism group by `C_2`, and global reflection survives with the output swap (48). Therefore the active-output typed group remains `C_2`.

### Arithmetic leakage

No mixed interaction returns a base value, so this realization introduces no candidate off-mirror arithmetic rule. It records only a finite reflection-paired terminal channel at each matched radial depth.

### Mathematical meaning

The new object is a **finite internal orientation fiber over the one-dimensional line**, not a new spatial dimension and not a physical state identification.

---

## 9. Mixed-Mirror Underdetermination Theorem

### Theorem 9.1

The currently accepted one-dimensional FCOA-Z axioms do not determine even the commutation status of the mirror mixed sector.

### Proof

The mirror-cancellation extension of Section 7 and split-terminal extension of Section 8 both satisfy:

1. exact preservation of all old defined cells;
2. exact preservation of the positive legacy ray;
3. simultaneous reflection equivariance;
4. generated, non-finite-exception rules;
5. finite-window coherence;
6. one-dimensional closure.

Yet on every mirror pair the first extension has status `EQ`, whereas the second has two-way-defined status `NEQ`. Therefore the accepted axioms admit incompatible mirror commutation spectra. QED.

### Corollary 9.2

Since the present core does not even select ordinary equality versus inequality under mirror exchange, it cannot select the more refined super exchange factor `(-1)^(pq)`.

Thus the mandated line-first verdict is

\[
\boxed{\texttt{UNDERDETERMINED}.}
\tag{54}
\]

A new invariant or extension principle is required.

---

## 10. Two Braiding Theorem for the Derived Grading

Recall from v0.1 that free linearization of the derived reflection gives

\[
V=V_{\bar0}\oplus V_{\bar1}.
\tag{55}
\]

For homogeneous vectors `v_p`, `w_q`, define for `eta in {+1,-1}`

\[
c_\eta(v_p\otimes w_q)
=\eta^{pq}\,w_q\otimes v_p.
\tag{56}
\]

Then

\[
c_{+1}(v_p\otimes w_q)=w_q\otimes v_p
\tag{57}
\]

is the ordinary flip, while

\[
c_{-1}(v_p\otimes w_q)=(-1)^{pq}w_q\otimes v_p
\tag{58}
\]

is the super flip.

### Theorem 10.1

Both (57) and (58) define symmetric braidings on the same underlying `Z_2`-graded tensor category. The FCOA-derived grading and reflection data do not distinguish them.

### Proof sketch

The scalar factor `eta^(pq)` is a bicharacter on `Z_2`: it is multiplicative in each degree. Therefore the hexagon equations follow from bilinearity of the exponent. Symmetry follows because

\[
\eta^{pq}\eta^{qp}=\eta^{2pq}=1.
\]

Both braidings preserve the same grading decomposition and the same reflection parity operator. The current FCOA data specify root, shift/reflection geometry, partial operation graphs, domains and output involutions, but no tensor braiding or argument-exchange scalar. Replacing (57) by (58) changes none of those FCOA data. QED.

This agrees with the standard theory of `Z_2`-graded vector spaces: the ordinary and super symmetries are distinct symmetric monoidal structures on the same graded tensor product.

Therefore

\[
\boxed{
\text{FCOA-derived parity object}
\not\Rightarrow
\text{super braiding}.
}
\tag{59}
\]

---

## 11. One-Bit Selection Theorem

The obstruction also identifies exactly how small the missing datum is.

### Theorem 11.1

Let

\[
\epsilon:\mathbb Z_2\times\mathbb Z_2\to K^*
\tag{60}
\]

be a normalized bicharacter over a field of characteristic different from `2`. Then `epsilon` is completely determined by

\[
\theta=\epsilon(1,1),
\tag{61}
\]

and

\[
\theta^2=1.
\tag{62}
\]

Hence

\[
\epsilon(p,q)=\theta^{pq},
\tag{63}
\]

with exactly the two possibilities

\[
\theta=+1
\quad\text{or}\quad
\theta=-1.
\tag{64}
\]

If a future FCOA mixed-sector mechanism forces a **nontrivial** bicharacter, then it uniquely forces

\[
\boxed{\epsilon(p,q)=(-1)^{pq}.}
\tag{65}
\]

### Proof

Normalization gives `epsilon(0,q)=epsilon(p,0)=1`. Bilinearity and `1+1=0` in `Z_2` give

\[
1=\epsilon(0,1)
=\epsilon(1+1,1)
=\epsilon(1,1)^2
=\theta^2.
\]

Since `char K != 2`, `theta=+1` or `-1`. Every value follows from normalization and `theta`. Nontriviality excludes `+1`, leaving (65). QED.

### Interpretation

The remaining SOL-GRADED target is therefore not vague. The line already generated the grading. What is missing is one exact structural bit:

\[
\boxed{\epsilon(1,1)=-1.}
\tag{66}
\]

It must be **derived from a conservative FCOA interaction**, not chosen because supersymmetry uses it.

---

## 12. Why mirror symmetry is not yet a superbracket

For a Lie superalgebra, homogeneous inputs obey

\[
[a,b]=-(-1)^{pq}[b,a].
\tag{67}
\]

Thus for two odd inputs,

\[
[a,b]=[b,a],
\tag{68}
\]

and the supercommutator is an anticommutator.

The cancellation realization (39) is indeed symmetric on a geometrically special opposite-side pair. But this does **not** establish (68), because `P_n^+` and `P_n^-` are not odd homogeneous vectors. In the derived reflection grading each individual branch basis vector is a mixture of even and odd modes.

Therefore the correct statement is only:

\[
\boxed{
\text{mirror geometry can generate symmetric exchange,}
\text{ but raw mirror points are not odd-odd inputs.}
}
\tag{69}
\]

This distinction prevents the forbidden shortcut from re-entering through the mixed-sector construction.

---

## 13. Exact success condition for the next phase

A genuine upgrade from `FORMAL EMBEDDING` toward a superalgebra model would require a conservative FCOA-generated construction that supplies all of the following rather than assuming them:

1. a map from FCOA interactions to a bilinear operation on the reflection-homogeneous modes;
2. degree preservation
   \[
   B(V_{\bar p},V_{\bar q})\subseteq V_{\overline{p+q}};
   \tag{70}
   \]
3. an exchange relation that is sensitive to both input grades;
4. a nontrivial odd-odd exchange datum, thereby forcing (65);
5. compatibility with old `oplus` cells and all old `UNDEF`/typed-output semantics;
6. a graded Jacobi test if a Lie-super interpretation is claimed.

The narrow next strike is therefore

\[
\boxed{
\text{Can any 1D conservative LC3 generator induce a nonzero bilinear}
\ V_{\bar1}\times V_{\bar1}\to V_{\bar0}
\text{ law from the original partial }\oplus
\text{ without defining a new bracket by hand?}
}
\tag{71}
\]

If yes, the next test is whether its exchange bit is forced and whether graded Jacobi survives. If no, that no-go would close the strongest SOL-GRADED emergence claim negatively.

---

## 14. Current programme verdict

### Mathematical classification

- reflection-generated `Z_2` shadow: **proved**;
- branch sign = parity: **rejected**;
- mirror geometry = exchange on `y=nu x`: **proved**;
- exact mirror output-orbit commutation classification: **proved**;
- unique commutative base-valued mirror rule = root cancellation: **proved**;
- conservative mirror cancellation realization: **constructed / 1D-CLOSED**;
- conservative split terminal mirror realization: **constructed / 1D-CLOSED**;
- super exchange factor forced by current line core: **no**;
- reason: **UNDERDETERMINED**;
- physical SUSY model: **not established**.

### Applied-domain verdict

\[
\boxed{\texttt{FORMAL EMBEDDING}}
\]

remains the correct applied verdict, now with a sharper internal theorem: FCOA-Z possesses a genuine geometry-generated **mirror exchange decomposition**, but not a selected super braiding.

### Publication recommendation

Do not publish SOL-GRADED as a standalone article yet. The new pair-involution and mirror-output theorems are worth preserving and are stronger than analogy, but the super-specific selection question remains unresolved. The material is publication-quality as a section/module of a future FCOA-Z applied comparison or line-completion paper after the next bilinear-lift/no-go phase.

---

## 15. External mathematical anchors

Standard comparison facts used only for the target-field side:

- nLab, **symmetric monoidal category** — records both the trivial and super symmetric structures on `Z_2`-graded vector spaces: https://ncatlab.org/nlab/show/symmetric+monoidal+category
- nLab, **super Lie algebra** — Lie algebra object internal to super vector spaces, with skew law defined through the super braiding: https://ncatlab.org/nlab/show/super+Lie+algebra
- nLab / super-vector-space definition — super braiding on homogeneous vectors: https://ncatlab.org/schreiber/files/SuperFluxQuantization-240604.pdf

These sources support only standard super/graded definitions. All FCOA-specific theorems above are derived from the FCOA-Z core.

---

## 16. FCOA anchor

Published mathematical base:

https://doi.org/10.5281/zenodo.22169264
