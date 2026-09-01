# SOL-TOPO — Channel/Provenance Separation and the Pentagon–Hexagon Coherence Barrier

**Version:** 0.3  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** HOSTILE CORRECTION + MINIMUM-RESOURCE NO-GO + CONDITIONAL ISING COHERENCE CLASSIFICATION  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_TOPO_REPORT_v0_1.md`, `SOL_TOPO_LC2_REFLECTION_BRAID_v0_2.md`, `SIGNED_M0_REFLECTION_TRANSFER_0_1.md`, `LINE_COMPLETION_GATE.md`

---

## 1. Executive verdict

The third SOL-TOPO strike resolves the pentagon/hexagon gate, but not by proving that raw FCOA-Z generates the Ising category.

Instead it proves a sharper boundary.

### Positive result

Conditional on adding a genuine fusion-tree/tensor layer whose simple-label fusion ring is the Ising ring

\[
\psi^2=1,
\qquad
\psi\sigma=\sigma\psi=\sigma,
\qquad
\sigma^2=1+\psi,
\tag{1}
\]

pentagon coherence leaves exactly two monoidal completions. They are the two `Z_2` Tambara–Yamagami / Ising fusion categories, with

\[
F^{\sigma\sigma\sigma}_{\sigma}
=
\frac{\varepsilon}{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
\varepsilon\in\{+1,-1\}.
\tag{2}
\]

For each monoidal sign there are four braided completions; equivalently the braiding is parameterized by a number `zeta` satisfying

\[
\zeta^8=-1,
\qquad
\zeta^2+\zeta^{-2}=\varepsilon\sqrt2.
\tag{3}
\]

Hence there are eight braided Ising fusion categories up to equivalence.

### Negative result

The old FCOA line/reflection/output data do **not** determine the monoidal sign `varepsilon` or the braiding parameter `zeta`.

More fundamentally, the single-fiber LC2 signature of v0.2 does not contain a tensor bifunctor or fusion-tree address, so the categorical pentagon is not merely false or unproved there: it is not internally expressible.

### Correction to v0.2

The v0.2 matrix algebra on a split mirror orbit is correct, but its Ising interpretation conflated two distinct binary degrees of freedom:

1. **mirror provenance** `E_n^alpha <-> bar E_n^alpha`;
2. **fusion channel type** `E_n^+` versus `E_n^times`, previously used for `1` versus `psi`.

Reflection acts on the first. Ising `F` mixes the second.

Therefore the v0.2 formula

\[
F=(J+S)/\sqrt2
\]

is a Hadamard on the provenance qubit, not a derivation of the Ising fusion-channel associator from the v0.1 channel encoding.

The corrected programme verdict is

\[
\boxed{
\texttt{FORMAL FUSION SHADOW + COHERENCE-BARRIER THEOREM}
}
\tag{4}
\]

for raw FCOA-Z/LC2.

A full Ising braided fusion category is a **conditional categorical completion**, not yet an internally generated FCOA structure.

---

## 2. Two different two-state fibers

The first report used the terminal types at a fixed radial level `n` as a channel alphabet:

\[
1\longleftrightarrow E_n^+,
\qquad
\sigma\longleftrightarrow E_n^*,
\qquad
\psi\longleftrightarrow E_n^\times.
\tag{5}
\]

The split reflection lift, however, acts separately inside each terminal type:

\[
E_n^\alpha
\longleftrightarrow
\bar E_n^\alpha,
\qquad
\alpha\in\{+,*,\times\}.
\tag{6}
\]

Thus for the two `sigma x sigma` output channels the relevant split space is naturally four-dimensional:

\[
H_n
=
H_n^+\oplus H_n^\times,
\tag{7}
\]

where

\[
H_n^+
=\operatorname{span}_{\mathbb C}\{E_n^+,\bar E_n^+\},
\qquad
H_n^\times
=\operatorname{span}_{\mathbb C}\{E_n^\times,\bar E_n^\times\}.
\tag{8}
\]

Equivalently, after choosing ordered bases,

\[
H_n\cong H_{ch}\otimes H_{pr},
\tag{9}
\]

where

\[
H_{ch}=\operatorname{span}\{|1\rangle,|\psi\rangle\}
\tag{10}
\]

is the **fusion-channel factor**, while

\[
H_{pr}=\operatorname{span}\{|+\rangle,|-\rangle\}
\tag{11}
\]

is the **legacy/reflected provenance factor**.

The distinction is structural, not notational.

---

## 3. Theorem A — Channel/provenance separation

Let `X_pr,Z_pr` be the usual swap/sign operators on the provenance factor. The old split output reflection and provenance sign have the form

\[
J_{old}=I_{ch}\otimes X_{pr},
\tag{12}
\]

\[
S_{old}=I_{ch}\otimes Z_{pr}.
\tag{13}
\]

They indeed satisfy

\[
J_{old}S_{old}=-S_{old}J_{old},
\tag{14}
\]

and therefore generate a Hadamard on the provenance factor:

\[
F_{pr}
=I_{ch}\otimes
\frac{X_{pr}+Z_{pr}}{\sqrt2}.
\tag{15}
\]

By contrast, the Ising nontrivial associator acts on the channel factor:

\[
F_{Ising}
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}_{ch}
\otimes I_{pr}
\tag{16}
\]

up to the global monoidal sign discussed below.

### Theorem 3.1 — Separation theorem

The operator generated in v0.2 from split reflection/provenance acts on `H_pr`, whereas the Ising associator required by the v0.1 channel dictionary acts on `H_ch`. Therefore

\[
\boxed{F_{pr}\ne F_{Ising}}
\tag{17}
\]

as operators on the corrected four-state space.

### Proof

Equation (15) preserves each channel-type subspace `H_n^+` and `H_n^times`; it only mixes the two provenance basis states inside a fixed output type.

Equation (16) maps, for fixed provenance,

\[
|1\rangle
\mapsto
\frac{|1\rangle+|\psi\rangle}{\sqrt2},
\tag{18}
\]

and hence mixes the distinct output types `E^+` and `E^times`.

An operator that preserves both channel blocks cannot equal one that has nonzero off-diagonal channel blocks. QED.

### Corollary 3.2 — Interpretation correction

The local matrix theorem of v0.2 remains a correct theorem about a split mirror orbit. Its identification with the Ising fusion-tree `F` matrix is not valid under the v0.1 channel assignment (5).

This correction is semantic/structural, not a failure of the matrix calculation itself.

---

## 4. Theorem B — Typed-sort channel-mixing no-go

Let

\[
\mathcal A_{old}^{out}
\subseteq
\operatorname{End}(H_n)
\tag{19}
\]

be any linear operator algebra generated from:

1. the old output reflection, acting sortwise as in (6);
2. legacy/reflected provenance projectors or signs;
3. scalar maps inside each existing terminal sort;
4. compositions and linear combinations of these maps;
5. no new primitive map between `E^+` and `E^times` sorts.

### Theorem 4.1 — Channel-mixing obstruction

Every element of `A_old^out` is block diagonal with respect to

\[
H_n=H_n^+\oplus H_n^\times.
\tag{20}
\]

Consequently

\[
F_{Ising}\notin\mathcal A_{old}^{out}.
\tag{21}
\]

### Proof

Each generator preserves the terminal type `alpha`; in particular reflection maps `E_n^alpha` only to `bar E_n^alpha` of the same `alpha`. Therefore every generator preserves the direct summands in (20). The set of block-diagonal operators is closed under sums, scalar multiples, and compositions. Hence every generated operator is block diagonal.

The matrix (16) has nonzero maps from the `1/E^+` channel to the `psi/E^times` channel and vice versa. It is therefore not block diagonal and cannot belong to the generated algebra. QED.

### Corollary 4.2 — Minimum channel resource

Any generative route to the Ising associator from the current channel dictionary requires at least one new **cross-type channel-mixing morphism**, for example an involution

\[
X_{ch}|1\rangle=|\psi\rangle,
\qquad
X_{ch}|\psi\rangle=|1\rangle.
\tag{22}
\]

No such morphism is present in the audited FCOA terminal-output structure.

---

## 5. Theorem C — Pentagon expressibility barrier

The categorical associator is a family of isomorphisms

\[
\alpha_{a,b,c}:(a\otimes b)\otimes c
\longrightarrow
a\otimes(b\otimes c).
\tag{23}
\]

The pentagon compares composites between five parenthesizations of a fourfold tensor product. One standard form is

\[
\alpha_{a,b,c\otimes d}
\circ
\alpha_{a\otimes b,c,d}
=
(id_a\otimes\alpha_{b,c,d})
\circ
\alpha_{a,b\otimes c,d}
\circ
(\alpha_{a,b,c}\otimes id_d).
\tag{24}
\]

### Theorem 5.1 — Single-fiber LC2 cannot state the pentagon intrinsically

A structure consisting only of

1. active finite output fibers `H_q`, and
2. unary endomorphisms `H_q -> H_q`

has no internal interpretation of (24) unless an additional tensor/fusion-tree composition law is supplied.

### Proof

Equation (24) requires all of the following operations/data:

- a binary tensor product on object labels;
- parenthesized composites such as `(a tensor b) tensor c`;
- tensoring a morphism with an identity, such as `alpha tensor id_d`;
- canonical identification of the source and target fusion spaces along different parenthesization paths.

A family of unrelated fibers with unary endomorphisms supplies none of these typed constructions. Therefore the terms in (24) are not definable in the single-fiber signature. QED.

### Corollary 5.2 — Minimum coherence address resource

Before pentagon coherence can be derived or tested, FCOA-LC2 must add a **fusion-tree/tensor address layer** recording at least:

\[
\boxed{
\text{labels}
+
\text{binary fusion composition}
+
\text{parenthesization address}
+
\text{functorial action on morphisms}.
}
\tag{25}
\]

This is a compositional memory layer. It is not a second spatial coordinate.

---

## 6. Conditional Ising/Tambara–Yamagami completion

We now deliberately add the minimum formal fusion-layer needed to ask the coherence question.

Assume three simple formal labels

\[
\{1,\psi,\sigma\}
\tag{26}
\]

with fusion rule (1), and use the existing FCOA typed output dictionary only as a label realization.

The invertible sector is

\[
G=\{1,\psi\}\cong\mathbb Z_2.
\tag{27}
\]

The fusion rule is exactly the `Z_2` Tambara–Yamagami fusion rule.

A Tambara–Yamagami category is determined by

1. a symmetric nondegenerate bicharacter
   \[
   \chi:G\times G\to\mathbb C^\times,
   \tag{28}
   \]
2. a scalar `tau` satisfying
   \[
   \tau^2=\frac1{|G|}.
   \tag{29}
   \]

For `G=Z_2`, the bicharacter is forced.

### Lemma 6.1 — Unique nondegenerate bicharacter on `Z_2`

Writing the nontrivial element as `psi`,

\[
\boxed{\chi(\psi,\psi)=-1.}
\tag{30}
\]

### Proof

Bilinearity gives

\[
\chi(\psi,\psi)^2
=
\chi(\psi^2,\psi)
=
\chi(1,\psi)=1,
\]

so `chi(psi,psi)=±1`. If it were `+1`, then `psi` would pair trivially with every element of `G`, violating nondegeneracy. Thus it is `-1`. QED.

Equation (29) now gives

\[
\tau=\frac{\varepsilon}{\sqrt2},
\qquad
\varepsilon\in\{+1,-1\}.
\tag{31}
\]

---

## 7. Theorem D — Pentagon completion has exactly one independent sign

Specializing the Tambara–Yamagami classification to `G=Z_2` gives the nontrivial associators, in a standard skeletal gauge,

\[
\alpha_{\psi,\sigma,\psi}=-1,
\tag{32}
\]

\[
\alpha_{\sigma,\psi,\sigma}
=
\operatorname{diag}(1,-1),
\tag{33}
\]

and

\[
\boxed{
F^{\sigma\sigma\sigma}_{\sigma}
=
\frac{\varepsilon}{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
}
\tag{34}
\]

### Theorem 7.1 — Conditional pentagon classification

Once the Ising fusion ring and a genuine tensor/fusion-tree layer are fixed, there are exactly two pentagon-complete fusion categories up to equivalence, distinguished by

\[
\varepsilon=+1
\qquad\text{or}\qquad
\varepsilon=-1.
\tag{35}
\]

### Proof

The fusion rules are precisely the Tambara–Yamagami rules for `G=Z_2`. By the Tambara–Yamagami classification, monoidal structures are classified by pairs `(chi,tau)` with `chi` symmetric nondegenerate and `tau^2=1/|G|`. Lemma 6.1 makes `chi` unique, while (31) leaves exactly two values of `tau`. These give (34). QED.

### Corollary 7.2 — Correction of the v0.2 sign statement

In a single isolated two-dimensional matrix problem, replacing `F` by `-F` may be projectively invisible. In the full fusion category, however, the sign in (34) distinguishes the two inequivalent Ising/Tambara–Yamagami monoidal structures.

Therefore the statement in v0.2 that the overall sign of `F` is merely gauge is **not valid globally at the fusion-category level**.

The sign is an independent Frobenius–Schur/Tambara–Yamagami coherence datum.

---

## 8. Theorem E — Hexagon leaves four braidings per monoidal sign

For an Ising fusion category, braided completions can be parameterized by a complex number `zeta` satisfying

\[
\zeta^8=-1
\tag{36}
\]

and the compatibility condition

\[
\boxed{
\zeta^2+\zeta^{-2}=\varepsilon\sqrt2.
}
\tag{37}
\]

In a standard gauge,

\[
c_{\psi,\psi}=-1,
\tag{38}
\]

\[
c_{\sigma,\sigma}
=
\operatorname{diag}(\zeta,\zeta^{-3})
\tag{39}
\]

on the `1` and `psi` channels, and

\[
c_{\psi,\sigma}
=c_{\sigma,\psi}
=\zeta^4.
\tag{40}
\]

### Theorem 8.1 — Conditional hexagon classification

For each fixed monoidal sign `varepsilon`, equation (37) admits four braided equivalence classes. Across the two monoidal signs there are eight braided Ising fusion categories.

### Projective ratio

Dividing (39) by the `1`-channel phase gives

\[
R_{proj}
=
\operatorname{diag}(1,t),
\qquad
 t=\zeta^{-4}.
\tag{41}
\]

Since `zeta^8=-1`,

\[
(\zeta^4)^2=-1,
\]

so

\[
\boxed{t=\pm i.}
\tag{42}
\]

### Corollary 8.2 — What v0.2 actually recovered

The v0.2 braid calculation

\[
(t-1)(t^2+1)=0
\tag{43}
\]

correctly recovers the only nontrivial **projective relative channel phases** compatible with the two-dimensional Hadamard braid template:

\[
t=\pm i.
\tag{44}
\]

However it does not recover the complete categorical braiding parameter `zeta`. Different allowed values of `zeta` can have the same projective ratio while defining inequivalent braided categories and different twist/central-charge data.

Thus the missing common phase is not globally disposable as “just gauge” once the full braided category is considered.

---

## 9. The coherence-independence theorem

We can now state the exact negative result promised by the previous publication gate.

### Theorem 9.1 — FCOA coherence independence

The audited one-line FCOA-Z structure, its split terminal-output reflection, and conservative LC2 linear activation do not determine a unique pentagon- or hexagon-complete Ising structure.

More precisely:

1. without a fusion-tree/tensor layer, the pentagon is not internally expressible;
2. with the Ising fusion ring added, pentagon coherence still leaves the independent binary parameter
   \[
   \varepsilon\in\{\pm1\};
   \tag{45}
   \]
3. for each such monoidal structure, hexagon coherence leaves four inequivalent braidings;
4. the old output reflection acts on provenance rather than on the `1/psi` fusion-channel factor and therefore cannot supply the required channel mixing.

### Proof

Items 1 and 4 are Theorems 5.1 and 4.1. Item 2 is Theorem 7.1. Item 3 is Theorem 8.1. QED.

### Main consequence

\[
\boxed{
\text{full anyonic coherence is not derivable from line completion + reflection + typed outputs alone.}
}
\tag{46}
\]

This is a minimum-resource no-go theorem, not a statement that FCOA cannot host a coherent anyon-like categorical extension.

---

## 10. Exact minimum-resource ladder

The three SOL-TOPO strikes now separate the resources cleanly.

### R0 — Signed FCOA line

Gives

- rooted two-sided carrier;
- reflection;
- same-sign inherited operations;
- mixed-sector freedom.

### R1 — Typed terminal channels

Gives a finite alphabet

\[
E^+,E^*,E^\times
\]

capable of encoding one-step fusion labels/support.

### R2 — Split output provenance

Gives

\[
E^\alpha\leftrightarrow\bar E^\alpha
\]

and a two-state provenance fiber. It does **not** mix `E^+` with `E^times`.

### R3 — Linear/additive activation

Needed for non-monomial superposition transforms. Still insufficient to produce channel mixing from old sort-preserving maps.

### R4 — Cross-type channel mixer

At least one morphism must connect the `1/E^+` and `psi/E^times` channel sectors.

### R5 — Fusion-tree/tensor address layer

Needed even to formulate pentagon coherence.

### R6 — Monoidal coherence class

For the Ising completion this reduces, after pentagon, to

\[
\varepsilon\in\{\pm1\}.
\]

### R7 — Braiding/twist class

For the Ising completion this is represented by an allowed `zeta` satisfying (36)-(37), four choices per monoidal sign.

The ladder can be summarized as

\[
\boxed{
\text{line}
<
\text{typed channels}
<
\text{provenance fiber}
<
\text{linear channel mixing}
<
\text{fusion-tree composition}
<
\text{monoidal class}
<
\text{braided class}.
}
\tag{47}
\]

None of the final four resources is forced by the current one-line geometry.

---

## 11. Dimensional verdict

This strike strengthens, rather than weakens, the previous dimensional conclusion.

The missing data are

- sort-to-sort channel mixing;
- fusion-tree addresses;
- coherence signs/phases.

These are **internal compositional degrees of freedom**. None is an unbounded independent spatial coordinate.

Therefore the appropriate line-completion verdict remains

\[
\boxed{\texttt{1D-CLOSED WITH RESPECT TO SPATIAL CARRIER}.}
\tag{48}
\]

The one-dimensional carrier is insufficient for geometric braiding, as proved in v0.1, but categorical braid memory can be hosted in finite internal fibers once an independent monoidal/braided layer is supplied.

No `DIMENSION-FORCING` theorem has appeared.

---

## 12. Publication assessment

The previous gate said that either

1. a full generated coherence construction, or
2. a strong no-go theorem identifying the minimum independent new resource

would be publication-grade.

Outcome (2) has now been achieved.

The publishable claim is **not** that FCOA derives Ising anyons. The publishable mathematical claim is the audited boundary:

\[
\boxed{
\begin{array}{c}
\text{typed FCOA output fibers can reproduce one-step Ising fusion support,}\\[2mm]
\text{but reflection acts on provenance, not fusion channel;}\\[2mm]
\text{full pentagon/hexagon coherence requires an independent}\\
\text{channel-mixing + fusion-tree monoidal layer.}
\end{array}
}
\tag{49}
\]

Together with the strict-line braid-topology no-go of v0.1, this now forms a coherent negative-positive paper nucleus.

### Publication threshold

\[
\boxed{\texttt{PUBLICATION THRESHOLD REACHED FOR A STRUCTURAL/NO-GO NOTE}.}
\tag{50}
\]

Before Zenodo release, one editorial step remains: consolidate v0.1–v0.3 into a single corrected manuscript and explicitly mark v0.2's channel/provenance interpretation as superseded.

No standalone physics claim should be made.

---

## 13. Literature anchors

1. D. Tambara, S. Yamagami, **Tensor Categories with Fusion Rules of Self-Duality for Finite Abelian Groups**, *Journal of Algebra* **209** (1998), 692–707. DOI `10.1006/jabr.1998.7558`.
2. V. Drinfeld, S. Gelaki, D. Nikshych, V. Ostrik, **On braided fusion categories I**, *Selecta Mathematica* **16** (2010), Appendix B on Ising categories.
3. L. Kong et al., **An Invitation to Topological Orders** (2026 lecture notes), section on Ising-type categories: two fusion categories, four braidings per fusion category, and explicit `F`/braiding data.
4. A. Conlon, **Generalised Braiding of Anyonic Excitations and Topological Quantum Computation**, PhD thesis, Maynooth University (2023), sections on Tambara–Yamagami and Ising `F/R` solutions.

The classification facts in Sections 6–8 are standard prior art. The FCOA-specific contribution of this report is the channel/provenance separation, typed-sort mixing obstruction, pentagon expressibility barrier, and resulting minimum-resource ladder.

---

## 14. Final conclusion

The final coherence strike closes the original SOL-TOPO question at the present FCOA-Z level.

The strongest true statement is

\[
\boxed{
\text{FCOA can supply typed one-step fusion-channel shadows and internal provenance fibers,}
}
\tag{51}
\]

but

\[
\boxed{
\text{it does not generate the categorical data that turn those shadows into non-Abelian anyons.}
}
\tag{52}
\]

The missing boundary is now exact:

\[
\boxed{
\text{channel mixer}
+
\text{fusion-tree/tensor composition}
+
\text{coherence class}.
}
\tag{53}
\]

Once those are added and the Ising fusion ring is chosen, standard coherence theory gives precisely two monoidal and eight braided Ising completions.

Thus SOL-TOPO has produced a useful positive correspondence, a strict one-dimensional topological no-go, and now a categorical minimum-resource no-go. That is a complete research arc for this applied direction at the current line-completion stage.