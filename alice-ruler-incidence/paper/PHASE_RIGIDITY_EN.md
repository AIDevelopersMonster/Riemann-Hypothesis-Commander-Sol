# Phase Rigidity in Steiner Triple Systems
## Quantitative Hall–Projective Stability from Anti-Mitre Defects

**Alice Throws Away the Ruler II**

**Malachevsky, A.A.**  
ORCID: **0009-0008-6009-3196**  
Preprint manuscript v1.0 — 12 September 2026

---

## Abstract

We introduce a phase graph on the noncollinear triples of a Steiner triple system and use it to obtain a quantitative form of the classical projective/Hall dichotomy. A noncollinear triple is assigned projective phase `P` when it generates the Fano subsystem `S_7`, Hall phase `H` when it generates the affine plane `S_9`, and defect phase `D` otherwise. The graph `G_ind` joins two noncollinear triples when they share two points. It is a regular induced subgraph of the Johnson graph `J(v,3)`. Cauchy interlacing gives a Laplacian spectral gap at least `v-3`, and hence a uniform phase-isoperimetric inequality.

The classical anti-mitre configuration `C_A` of Král'–Máčajová–Pór–Sereni is then used as a local defect certificate. A constructive re-reading of their local `S_7/S_9` lemma shows that every `D`-triple is contained in an anti-mitre; consequently `|D| <= 56 c_A`. A localization of the finite phase-purity argument from their 2007 technical report shows that every direct `P/H` interface forces a nearby `D`-triple, with reverse multiplicity `O(v)`. Combining these facts with spectral expansion yields an absolute constant `C` such that

```math
\min\{\rho_P,\rho_H\}
\le C\,\frac{c_A}{N},
```

where `N=v(v-1)(v-3)/6` is the number of noncollinear triples and `rho_P,rho_H` are the corresponding phase densities. Thus a small normalized anti-mitre count forces almost all noncollinear triples into one of the two pure closure regimes. The zero-defect case recovers the exact projective/Hall dichotomy. The result is a phase-profile stability theorem; no edit-distance conclusion for the entire block set is claimed.

---

## 1. Introduction

A Steiner triple system `S=(X,B)` of order `v` is a set of `v` points together with three-point blocks such that every pair of distinct points belongs to exactly one block. The local rule is therefore extremely small and rigid: every pair has a unique completion. Nevertheless, different global closure laws can emerge from the same local block size.

Two extremal examples are projective and Hall triple systems. In a projective Steiner triple system, every three noncollinear points generate the Fano plane `S_7`. In a Hall triple system, every three noncollinear points generate the affine plane `S_9`. Král', Máčajová, Pór and Sereni proved a finite forbidden-configuration characterization of these regimes. In particular, their anti-mitre configuration `C_A` separates the mixed case: a nonprojective Steiner triple system with no `C_A` is Hall. Their published proof passes through the local statement that in a `C_A`-free system every noncollinear triple generates either `S_7` or `S_9`, followed by a theorem of Teirlinck forcing one global type.

The exact theorem leaves a natural quantitative question.

> If anti-mitres are rare rather than absent, can both local closure phases occupy a macroscopic fraction of the system?

The answer developed here is no. The key is to stop treating local `S_7/S_9` behavior only as a forbidden-configuration problem and instead place the local phases on an expanding graph.

For a noncollinear triple `tau`, define

```math
\sigma(\tau)=
\begin{cases}
P,&\langle\tau\rangle\cong S_7,\\
H,&\langle\tau\rangle\cong S_9,\\
D,&\text{otherwise}.
\end{cases}
```

The vertices of the resulting phase graph are all noncollinear triples; two vertices are adjacent when they share two points. The underlying uncoloured graph is nearly the Johnson graph `J(v,3)`, and its spectral expansion creates a surface-tension principle: a macroscopic mixture of `P` and `H` must pay either in direct `P/H` interfaces or in `D`-bulk.

The second ingredient is local charging. The classical anti-mitre proof can be read constructively: a defective triple contains an anti-mitre witness. A second, finite argument from the authors' earlier 2007 technical report can be localized around a Fano subsystem and an external point. It implies that a direct `P/H` interface must create a nearby `D`-triple. The reverse fibers of this construction are only `O(v)`, exactly the scale required to combine it with the degree `Theta(v)` of the phase graph.

The result is a quantitative Hall/projective stability theorem in phase space.

### 1.1 What is new and what is classical

The following ingredients are classical or directly source-derived:

- the Fano/projective and affine/Hall closure interpretations;
- the anti-mitre configuration and the local `S_7/S_9` lemma;
- the exact projective/Hall dichotomy;
- the finite 2007 phase-purity case analysis;
- the five-line configuration formulas;
- the standard spectrum of the Johnson graph.

The new layer is the combination:

1. the independent-triple phase graph as a quantitative carrier;
2. its spectral phase-isoperimetry;
3. root-preserving anti-mitre charging;
4. localization and finite-fiber counting for direct phase interfaces;
5. the resulting linear phase-profile stability theorem.

A dedicated literature search found no equivalent quantitative `P/H/D` phase-stability statement as of 12 September 2026. This is a novelty assessment, not a formal priority guarantee.

---

## 2. Preliminaries and notation

For distinct points `x,y` of an STS, write

```math
x\oplus y
```

for the unique third point on their block. For three distinct points `x,y,z`, we call `{x,y,z}` **independent** or **noncollinear** when it is not a block. For a three-point set `tau`, write `\langle tau\rangle` for the Steiner subsystem generated by it.

Let `S_7` denote the Fano plane and `S_9` the affine plane `AG(2,3)`.

### Definition 2.1 (local phase)

For every independent triple `tau`, define

```math
\sigma(\tau)=P
```

if `\langle tau\rangle\cong S_7`, define `\sigma(\tau)=H` if `\langle tau\rangle\cong S_9`, and define `\sigma(\tau)=D` otherwise.

Let `P,H,D` also denote the corresponding sets of vertices.

The number of independent triples is

```math
N=\binom v3-\frac{v(v-1)}6
 =\frac{v(v-1)(v-3)}6.
\tag{2.1}
```

Define phase densities

```math
\rho_P=\frac{|P|}{N},\qquad
\rho_H=\frac{|H|}{N},\qquad
\rho_D=\frac{|D|}{N}.
\tag{2.2}
```

### Definition 2.2 (independent-triple graph)

`G_ind(S)` is the graph whose vertices are the independent triples of `S`; two vertices are adjacent when they have exactly two common points.

For every independent triple there are three choices of a retained pair. For each retained pair there are `v-4` admissible new third points: the old third point is excluded and the unique block-completion point would create a block rather than an independent triple. Hence

```math
G_{\rm ind}(S)\text{ is }3(v-4)\text{-regular}.
\tag{2.3}
```

Let

```math
s=e_{G_{\rm ind}}(P,H),
\qquad
q=\min\{|P|,|H|\}.
\tag{2.4}
```

---

## 3. Spectral phase isoperimetry

The graph `G_ind(S)` is obtained from the Johnson graph `J(v,3)` by deleting the vertices that are blocks of the Steiner triple system. Thus its adjacency matrix is a principal submatrix of the adjacency matrix of `J(v,3)`.

The Johnson eigenvalues for `J(v,3)` are

```math
3(v-3),\qquad 2v-9,\qquad v-7,\qquad -3.
\tag{3.1}
```

### Lemma 3.1 (spectral gap)

For every nontrivial `STS(v)`,

```math
\mu_2(G_{\rm ind})\ge v-3,
\tag{3.2}
```

where `mu_2` is the second Laplacian eigenvalue.

#### Proof

By Cauchy interlacing, the second adjacency eigenvalue of the principal subgraph satisfies

```math
\lambda_2(G_{\rm ind})\le 2v-9.
```

Since `G_ind` is `3(v-4)`-regular,

```math
\mu_2
=3(v-4)-\lambda_2(G_{\rm ind})
\ge 3(v-4)-(2v-9)
=v-3.
```

`\square`

### Corollary 3.2 (cut expansion)

For every `A subseteq V(G_ind)`,

```math
e(A,A^c)
\ge
(v-3)|A|\left(1-\frac{|A|}{N}\right).
\tag{3.3}
```

In particular, if `|A|<=N/2`, then

```math
e(A,A^c)\ge \frac{v-3}{2}|A|.
\tag{3.4}
```

This is the standard Laplacian cut estimate applied with (3.2).

### Theorem 3.3 (phase isoperimetry)

For every nontrivial Steiner triple system,

```math
(v-3)q\left(1-\frac qN\right)
\le
s+3(v-4)|D|.
\tag{3.5}
```

Consequently,

```math
\frac{v-3}{2}\,q
\le
s+3(v-4)|D|.
\tag{3.6}
```

#### Proof

Apply (3.3) to the smaller of the pure phase sets `P,H`. Its edge boundary consists of direct edges to the other pure phase and edges into `D`. The direct contribution is `s`. Since the graph has degree `3(v-4)`, the second contribution is at most `3(v-4)|D|`. This gives (3.5), and (3.6) follows from `q<=N/2`. `\square`

Equation (3.5) is the basic surface-tension inequality. A macroscopic two-phase mixture cannot have simultaneously small interface and small defective bulk.

---

## 4. The correct five-line defect coordinate

The anti-mitre `C_A` used in the projective/Hall characterization is the eight-point five-block configuration

```text
012, 034, 135, 236, 457.
```

In the standard list of 56 five-line configurations of Danziger–Mendelsohn–Grannell–Griggs, it is configuration no. 4. Let its occurrence count be `c_A`.

A different five-line configuration occurs naturally in the mirror-completion experiment of the preceding research seed:

```text
012, 034, 135, 246, 567.
```

This is configuration no. 7; write its count as `r_7`. The two configurations are not isomorphic.

Let `p` be the Pasch count, `m` the mitre count, and

```math
n(v)=v(v-1)(v-3).
```

The classical five-line formulas give

```math
c_A=\frac{n(v)}2-12p-6m,
\tag{4.1}
```

and

```math
r_7=\frac{n(v)}4-6p-3m.
\tag{4.2}
```

Therefore

```math
\boxed{c_A=2r_7.}
\tag{4.3}
```

This identity repairs an identification error in research seed v0.6: the residual mirror configuration and the anti-mitre are different pictures, but their counts differ by the exact factor two.

If

```math
P(v)=\frac{v(v-1)(v-3)}{24},
\qquad
\alpha=\frac{r_7}{6P(v)},
\tag{4.4}
```

then `N=4P(v)` and hence

```math
c_A=12P(v)\alpha=3N\alpha.
\tag{4.5}
```

In particular,

```math
\alpha=0\iff c_A=0.
\tag{4.6}
```

Thus all zero-defect conclusions previously attached to the residual coordinate remain valid after the configuration itself is correctly identified.

---

## 5. Bulk defects are charged to anti-mitres

We now use the constructive local argument behind the classical `C_A`-free `S_7/S_9` lemma.

### Lemma 5.1 (root-preserving anti-mitre witness)

Every `D`-phase independent triple is contained in a copy of `C_A`.

#### Proof

Let the root be `tau={A,B,C}` and put

```math
a=B\oplus C,\qquad
b=A\oplus C,\qquad
c=A\oplus B.
\tag{5.1}
```

The classical proof splits according to whether `a,b,c` form a block.

**Case 1: `a,b,c` form a block.** Put `m=A\oplus a`. If the Fano closure identity fails, then with `x=m\oplus c` the five blocks

```text
BCa, ACb, ABc, Aam, mcx
```

form an anti-mitre. They contain the original points `A,B,C`.

If the identity does not fail, the symmetric identities close the root to `S_7`.

**Case 2: `a,b,c` are independent.** Put

```math
A'=b\oplus c,\qquad
B'=a\oplus c,\qquad
C'=a\oplus b.
\tag{5.2}
```

At the first closure level, a failed required identity produces an anti-mitre containing `A,B,C`; for example, if `A'\ne A\oplus a`, setting `y=A\oplus a` gives

```text
BCa, ACb, ABc, bcA', Aay.
```

If the first closure level succeeds, the classical proof imposes a second level of identities. Again, a failure gives an anti-mitre containing the root. For example, if `B'\ne A\oplus C'`, with `x=A\oplus C'` one may use

```text
BCa, ACb, abC', BbB', AC'x.
```

If no failure occurs at either level, the nine displayed points close to `S_9`.

Since the root has phase `D`, one of the failure alternatives must occur. `\square`

### Corollary 5.2 (bulk bound)

```math
\boxed{|D|\le56c_A.}
\tag{5.3}
```

#### Proof

Charge each `D` root to one anti-mitre that contains it, using Lemma 5.1. An anti-mitre has eight points and therefore has at most

```math
\binom83=56
```

three-point subsets that could serve as roots. `\square`

In density form,

```math
\rho_D\le56\frac{c_A}{N}=168\alpha.
\tag{5.4}
```

---

## 6. Direct phase interfaces force defective roots

The bulk estimate alone does not control the direct interface term `s`. We now localize the finite phase-purity argument from the 2007 technical report of Král'–Máčajová–Pór–Sereni.

Let `F\cong S_7` be a Fano subsystem and let `d` be a point outside `F`. For `x in F`, write

```math
d_x=d\oplus x.
\tag{6.1}
```

Assume first that every phase query made below is pure (`P` or `H`). Each line `L={u,v,w}` of `F` can then be colored red if `\langle d,u,v\rangle\cong S_7` and blue if `\langle d,u,v\rangle\cong S_9`. This is well-defined because any two points of a Fano line generate the third.

A direct `P/H` edge supplies exactly this situation: the `P` endpoint generates a Fano subsystem `F`, the third point of the `H` endpoint lies outside `F`, and the common pair lies on a blue line of `F`.

### Lemma 6.1 (localized phase-interface witness)

Let `F\cong S_7` and `d\notin F`. If at least one line of `F` is blue, then some independent triple in a finite Steiner-term closure of `(F,d)` has phase `D`.

Moreover, after Fano relabelling, every phase query needed by the finite argument has one of the four forms

```math
\{d,u,v\},
\qquad
\{d_x,u,v\},
\qquad
\{u,d_x,d_y\},
\qquad
\{d_x,d_y,d_z\},
\tag{6.2}
```

with the base points in `F`; in the last two forms the base points used in the actual query templates are noncollinear and hence generate `F`.

#### Proof

The 2007 proof colors the seven Fano lines exactly as above and uses the elementary fact that a two-coloring of the Fano lines has a point whose three incident lines receive one color. Its subsequent contradiction is a finite case analysis.

There is one point in the original presentation where four-point independence is invoked: in the red-star case, the auxiliary points `d_A,d_B,d_C` are asserted not to form a block. For the present localized statement, if they *do* form a block, then the closure of `{A,B,d}` already contains the entire Fano subsystem `F` as well as `d`. It therefore cannot be `S_7`; it also cannot be `S_9`, because an affine plane `AG(2,3)` has no Fano subsystem. Hence `{A,B,d}` itself has phase `D` and we are done.

If `d_A,d_B,d_C` do not form a block, the original red-star case proceeds unchanged. The blue-star case never needs the four-point independence assumption. Under the hypothesis that all queried roots remain `P` or `H`, both cases reach the same finite contradictions as in the 2007 proof. Consequently at least one queried root must have phase `D`.

Inspecting the queried roots in that case analysis gives only the forms in (6.2). Concretely, besides the line queries `{d,u,v}`, the proof uses roots of the types

```text
{d_m,a,b}, {m,d_a,d_b}, {m,d_A,d_B},
{d_m,d_a,d_c}, {m,d_A,d_b}, {d_m,a,B},
```

and their Fano-symmetric counterparts. These are precisely the remaining three forms in (6.2). For the third and fourth forms, the corresponding base triples (for example `m,a,b`, `m,A,B`, `m,A,b`, and `m,a,c`) are noncollinear in the Fano plane. `\square`

The point of the lemma is not the exact radius of the finite closure, but the finite list of reconstruction types.

---

## 7. Reverse multiplicity of the interface witness

Call a pair `(F,d)` **mixed** when `F\cong S_7`, `d\notin F`, and at least one Fano line is blue relative to `d`.

A `P/H` edge determines a unique mixed pair: `F` is the subsystem generated by the `P` endpoint, and `d` is the point of the `H` endpoint outside `F`.

For a fixed mixed pair, at most `84` direct `P/H` edges determine it: `F` has `28` independent triples, and one may choose at most three shared pairs from each such `P` root.

We now bound how many mixed pairs can charge to one fixed `D` root.

### Lemma 7.1 (Fano subsystems through a block)

A fixed block of an `STS(v)` belongs to at most

```math
\frac{v-3}{4}
\tag{7.1}
```

Fano subsystems.

#### Proof

A Fano subsystem containing a fixed block has four further points. Conversely, after choosing any point outside the block, there is at most one generated Fano subsystem containing the block and that point. Count pairs `(F,x)` with `x` outside the fixed block and inside `F`. `\square`

### Lemma 7.2 (interface fiber bound)

There is an absolute constant `K` such that a fixed `D`-phase triple can be selected as the witness in Lemma 6.1 for at most `Kv` mixed pairs `(F,d)`.

#### Proof

There are only finitely many query templates and finitely many Fano roles, so it is enough to bound each of the four forms in (6.2).

**Type I: `{d,u,v}`.** Once the root and the role of `d` are fixed, the pair `u,v` is fixed. Any admissible `F` contains the block determined by that pair. Lemma 7.1 gives `O(v)` choices for `F`.

**Type II: `{d_x,u,v}`.** Fix the role of `d_x`. The two remaining root points fix `u,v`, hence again a block contained in `F`; there are `O(v)` possible Fano subsystems. Once `F` and the finite role of `x` are fixed,

```math
d=x\oplus d_x
```

is uniquely recovered.

**Type III: `{u,d_x,d_y}`.** Choose `d` first; there are at most `v` choices. Then

```math
x=d\oplus d_x,\qquad y=d\oplus d_y.
```

In every template that occurs in Lemma 6.1, the three base points `u,x,y` are noncollinear in `F`; hence they generate `F` uniquely. Thus there is at most one `F` for each choice of `d` and each finite role assignment.

**Type IV: `{d_x,d_y,d_z}`.** Again choose `d` first and recover `x,y,z`. In the occurring templates these three points are noncollinear and determine `F` uniquely.

Absorbing the finite number of templates and role assignments into one universal constant gives the claim. `\square`

### Corollary 7.3 (interface bound)

There is an absolute constant `C_I` such that

```math
\boxed{s\le C_I v|D|.}
\tag{7.2}
```

#### Proof

Choose one `D` witness for every mixed pair using Lemma 6.1. By Lemma 7.2, the number of mixed pairs is at most `Kv|D|`. Each mixed pair supports at most `84` direct `P/H` edges, so one may take `C_I=84K`. `\square`

No attempt is made to optimize `K` or `C_I`; only their independence of `v` matters.

---

## 8. Quantitative Hall–projective phase stability

We can now combine expansion, bulk charging, and interface charging.

### Theorem 8.1 (phase-profile stability)

There is an absolute constant `C>0` such that every nontrivial `STS(v)` satisfies

```math
\boxed{
\min\{\rho_P,\rho_H\}
\le
C\,\frac{c_A}{N}.
}
\tag{8.1}
```

Equivalently, using `c_A/N=3alpha`,

```math
\min\{\rho_P,\rho_H\}\le 3C\alpha
\tag{8.2}
```

after a harmless renaming of the absolute constant.

#### Proof

From the coarse phase-isoperimetric inequality (3.6) and the interface bound (7.2),

```math
\frac{v-3}{2}q
\le
\bigl(C_Iv+3(v-4)\bigr)|D|.
\tag{8.3}
```

Divide by `N`. For `v>=7`,

```math
\frac{v}{v-3}\le\frac74,
\qquad
\frac{v-4}{v-3}<1.
```

Therefore

```math
\min\{\rho_P,\rho_H\}
\le
\left(\frac72C_I+6\right)\rho_D.
\tag{8.4}
```

By (5.3),

```math
\rho_D\le56\frac{c_A}{N}.
```

Thus (8.1) holds, for example with

```math
C=56\left(\frac72C_I+6\right).
```

`\square`

### Corollary 8.2 (zero-defect dichotomy)

If `c_A=0`, then all independent triples have one pure phase:

```math
(\rho_P,\rho_H,\rho_D)=(1,0,0)
```

or

```math
(\rho_P,\rho_H,\rho_D)=(0,1,0).
```

Hence the Steiner triple system is projective or Hall.

This recovers the classical exact dichotomy as the zero-temperature limit of the quantitative estimate.

### Corollary 8.3 (completion-simplex form)

With the corrected residual coordinate `alpha` from (4.4), there exists an absolute constant `C_alpha` such that

```math
\min\{\rho_P,\rho_H\}\le C_\alpha\alpha.
\tag{8.5}
```

Thus moving close to the Hall/projective zero-residual face forces phase purity, even though convex configuration-count relaxations alone contain the entire formal Hall/projective segment.

---

## 9. Interpretation: the phantom edge acquires surface tension

At the level of low-order configuration counts, the Hall and projective endpoints can lie on a common convex edge. A convex relaxation cannot remove the interior of such an edge once both endpoints are present. This is the origin of the **phantom-edge** phenomenon: local linear statistics permit formal mixtures that exact Steiner closure forbids.

The phase graph explains what the convex picture misses.

The two pure local regimes are

```math
P\quad | \quad H.
```

There are two ways to pay for mixing:

- **bulk defects**, the vertices `D` whose closure is neither `S_7` nor `S_9`;
- **interfaces**, the direct graph edges joining a `P` root to an `H` root.

The spectral inequality says that a macroscopic mixture must have a macroscopic boundary. The local charging lemmas say that both boundary and bulk are controlled by anti-mitre defects. The combination produces a discrete analogue of surface tension.

It is therefore useful to define the phase energy

```math
\mathcal E(S)=s+3(v-4)|D|.
\tag{9.1}
```

Then (3.5) becomes

```math
\mathcal E(S)
\ge
(v-3)q\left(1-\frac qN\right).
\tag{9.2}
```

The anti-mitre count controls both terms of this energy at the correct asymptotic scale.

---

## 10. Scope and limitations

Theorem 8.1 is deliberately a **phase-profile stability theorem**.

It proves that a small normalized anti-mitre count makes the minority local closure phase small. It does **not** prove that the block set of the entire Steiner triple system can be changed in `o(v^2)` or any other small number of edits to obtain an actual projective or Hall system.

Several separate difficulties remain before an edit-distance statement could be claimed:

1. a dominant local phase need not immediately identify a canonical global model;
2. projective orders `2^m-1` and Hall orders `3^m` are arithmetically sparse and incompatible, so order stability itself becomes relevant;
3. an edit theorem would require a reconstruction or removal mechanism stronger than the finite witness counting used here.

No such stronger conclusion is used in this paper.

---

## 11. Further problems

The present theorem suggests four natural continuations.

### 11.1 Constant optimization

The constants from the finite-template proof are intentionally crude. An exact enumeration of the query templates and their Fano symmetries should substantially reduce `C_I` and the final stability constant.

### 11.2 Edit-distance rigidity

Does there exist a function `f(epsilon)->0` such that a system with anti-mitre density at most `epsilon` and dominant projective phase can be edited in at most `f(epsilon)v^2` blocks to a projective STS, whenever the order permits one? Is there an analogous Hall statement?

### 11.3 Order stability

Can a small defect density force the order `v` to lie quantitatively close, in an appropriate arithmetic sense, to one of the sparse spectra

```math
2^m-1
\qquad\text{or}\qquad
3^m?
```

### 11.4 Higher phase systems

The method is not inherently binary. Whenever a bounded local closure theorem has finitely many pure closure types and a bounded obstruction set, one can ask for a phase graph, its expansion, and defect/interface charging. This suggests a general program for converting exact finite forbidden-configuration classifications into quantitative rigidity theorems.

---

## 12. Literature and priority boundary

The exact forbidden-configuration theory used here belongs to the classical STS literature. Danziger, Mendelsohn, Grannell and Griggs computed the five-line occurrence formulas. Král', Máčajová, Pór and Sereni established the relevant projective/Hall characterizations; the final 2010 paper uses Teirlinck's theorem to pass from local `S_7/S_9` behavior to a single global phase, while their 2007 technical report contains the longer finite phase-purity argument localized in Sections 6–7 above.

The quantitative statement (8.1), the independent-triple phase graph, the spectral phase-isoperimetric inequality, and the two charging estimates were not found in the sources located during the dedicated priority search. Searches included combinations of *Hall triple system stability*, *projective/Hall Steiner stability*, *anti-mitre supersaturation*, *Steiner quasigroup stability/removal*, and *phase graph*. The search was performed through 12 September 2026.

This section records the search boundary; it does not assert that an equivalent theorem cannot exist under different terminology.

---

## References

[1] P. Danziger, E. Mendelsohn, M. J. Grannell, T. S. Griggs, **Five-line configurations in Steiner triple systems**, *Utilitas Mathematica* **49** (1996), 153–159.

[2] D. Král', E. Máčajová, A. Pór, J.-S. Sereni, **Characterisation Results for Steiner Triple Systems and Their Application to Edge-Colourings of Cubic Graphs**, *Canadian Journal of Mathematics* **62**(2) (2010), 355–381. DOI: `10.4153/CJM-2010-021-9`.

[3] D. Král', E. Máčajová, A. Pór, J.-S. Sereni, **Characterization Results for Steiner Triple Systems and Their Application to Edge-Colorings of Cubic Graphs**, Institute for Theoretical Computer Science, Charles University, technical report IUUK-CE-ITI 2007-352 (2007).

[4] D. Král', E. Máčajová, A. Pór, J.-S. Sereni, **Characterization of affine Steiner triple systems and Hall triple systems**, *Electronic Notes in Discrete Mathematics* **29** (2007), 17–21. DOI: `10.1016/j.endm.2007.07.004`.

[5] L. Teirlinck, **On linear spaces in which every plane is either projective or affine**, *Geometriae Dedicata* **4** (1975), 39–44. DOI: `10.1007/BF00147400`.

[6] M. J. Grannell, T. S. Griggs, E. Mendelsohn, **A small basis for four-line configurations in Steiner triple systems**, *Journal of Combinatorial Designs* **3**(1) (1995), 51–59. DOI: `10.1002/jcd.3180030107`.

[7] D. R. Stinson, Y. J. Wei, **Some results on quadrilaterals in Steiner triple systems**, *Discrete Mathematics* **105** (1992), 207–219. DOI: `10.1016/0012-365X(92)90143-4`.

[8] C. J. Colbourn, A. Rosa, **Triple Systems**, Oxford University Press, New York, 1999.

---

## Author note

This manuscript grew from the research sequence *Alice Throws Away the Ruler: Through the Looking-Glass of Incidence — Arithmetic Without Metric*. The present paper isolates the first quantitative rigidity theorem from that exploratory sequence. The mathematical claims above are intentionally narrower than the surrounding heuristic program: only the statements proved in the numbered lemmas and theorems are asserted.