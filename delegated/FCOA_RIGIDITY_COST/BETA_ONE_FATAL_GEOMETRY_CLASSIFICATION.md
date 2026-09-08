# FCOA Rigidity Cost — Classification of Fatal Anchored Beta-One Geometries

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication theorem note.

## 1. Setup

Assume

\[
\beta(D,c)=1.
\]

Let `e` be an **anchored beta-killing cell**: adding the singleton cell `e` destroys every old bad automorphism, and `e` lies in a component of

\[
\Lambda(D\cup\{e\})
\]

containing an old cell.

Put

\[
S=D\cup\{e\}.
\]

For each binary value `b in F_2`, write

\[
A_b=\operatorname{Aut}(G;S,Q_S^{b})
\]

for the ternary-reduct automorphism group of the extension in which `e` receives color `b`.

Let

\[
\Gamma_e=\operatorname{Aut}(G;S)
\]

be the uncolored domain automorphism group.

Let `A^+(D,c)` denote the old globally color-preserving automorphisms.

Define

\[
\boxed{
H_e=\{g\in A^+(D,c):g(e)=e\}.
}
\]

Since every old automorphism preserves `D`, the expression `g(e)=e` is understood using the carrier action on the missing cell `e`.

## 2. Common D-preserving core

### Theorem 2.1

For both colors `b=0,1`, the subgroup of `A_b` that preserves the old domain `D` setwise is exactly

\[
\boxed{H_e.}
\]

In particular it is independent of the color assigned to `e`.

### Proof

Let `g in A_b` preserve `D`. Since `S=D union {e}` and `gD=D`, the unique new cell must be fixed:

\[
ge=e.
\]

The restriction of `g` to the old layer belongs to `A_Q(D,c)`. Because `e` is beta-killing, no old bad automorphism survives. Thus the old restriction is globally anonymous, with phase either 0 or 1.

Phase 1 is impossible because `e` is fixed, hence has discrepancy 0, while anchoring places `e` in an incidence component containing an old cell of discrepancy 1. Componentwise phase constancy would fail.

Therefore the old phase is 0, so `g in A^+(D,c)` and `ge=e`; hence `g in H_e`.

Conversely, if `g in H_e`, then `g` preserves all old colors and fixes `e`. Every equality comparison between `e` and an adjacent old cell is therefore preserved for either choice of `b`, while old-old comparisons are already preserved. Thus `g in A_b` for both colors. `square`

## 3. Badness is constant on H_e-cosets

For fixed color `b`, let

\[
B_b=A_b\setminus\operatorname{Aut}^{\pm}(S,c\cup b)
\]

be the bad automorphisms of the extended reduct.

### Lemma 3.1

If `h in B_b` and `a in H_e`, then

\[
ah\in B_b
\qquad\text{and}\qquad
ha\in B_b.
\]

### Proof

Every `a in H_e` is a globally color-preserving automorphism of the colored extension. Composition with such an automorphism preserves the property of being a reduct automorphism and cannot turn a non-global discrepancy pattern into a global one. `square`

Thus `B_b` is a union of left and right `H_e`-cosets inside `Gamma_e`.

Every bad element lies outside `H_e` and therefore moves the old domain.

## 4. Two-color fatality classification

Call the anchored geometry `e` **fatal** if both color choices are nonexact:

\[
B_0\ne\varnothing,
\qquad
B_1\ne\varnothing.
\]

### Theorem 4.1 — Persistent-or-split dichotomy

An anchored beta-killing cell is fatal if and only if at least one of the following occurs.

### Type P — persistent replacement obstruction

There exists a carrier permutation

\[
h\in\Gamma_e\setminus H_e
\]

which is bad for **both** colors:

\[
\boxed{h\in B_0\cap B_1.}
\]

Equivalently, the fixed-geometry bad-color set of `h` is the full one-dimensional color cube:

\[
\mathcal B_h(\{e\})=\mathbf F_2.
\]

### Type S — split-color replacement obstruction

There exist bad automorphisms

\[
h_0\in B_0,
\qquad
h_1\in B_1
\]

whose `H_e`-cosets are distinct:

\[
\boxed{H_eh_0\ne H_eh_1.}
\]

### Proof

If Type P or Type S occurs, both colors are plainly unsafe.

Conversely suppose both colors are unsafe. Choose `h_0 in B_0` and `h_1 in B_1`. If some carrier permutation is bad for both colors, Type P holds.

Otherwise `B_0 cap B_1` is empty. We claim the two chosen `H_e`-cosets must be distinct. If

\[
H_eh_0=H_eh_1,
\]

then `h_1=ah_0` for some `a in H_e`. Since `a` is a color-preserving automorphism for **both** color choices, `h_1 in B_1` implies

\[
h_0=a^{-1}h_1\in B_1,
\]

contradicting `h_0 in B_0` and the assumption that no permutation is bad for both colors. Hence the cosets are distinct and Type S holds. `square`

## 5. Index consequence

### Corollary 5.1

If a fatal anchored beta-killing cell has no persistent bad replacement symmetry, then

\[
\boxed{[\Gamma_e:H_e]\ge3.}
\]

### Proof

The uncolored extension group contains the core coset `H_e`, a bad coset for color 0, and a distinct bad coset for color 1. `square`

Therefore:

\[
\boxed{
[\Gamma_e:H_e]\le2
\quad\Longrightarrow\quad
\text{fatality requires a single bad symmetry surviving both colors.}
}
\]

This eliminates split-color coverage in all index-one and index-two singleton extensions.

## 6. Replacement-defect interpretation

Every element of

\[
\Gamma_e\setminus H_e
\]

moves the old domain. Since only one new cell is present, the Replacement Boundary Theorem gives

\[
d_D(h)=1,
\qquad
P_D(h)=\{e\}.
\]

Hence both Type P and Type S are entirely supported on defect-one replacement symmetries.

The difference is:

- Type P: one replacement symmetry defeats both color choices;
- Type S: different replacement cosets defeat the two colors separately.

Thus the one-cell color problem has no further hidden mechanism.

## 7. Consequences for a beta-one counterexample

If

\[
\beta=1<\alpha,
\]

then every anchored beta-killing cell `e` must satisfy all of the following:

1. `e in R_1(D)`;
2. the singleton geometry is fatal;
3. fatality is either Type P, or Type S with
   \[
   [\Gamma_e:H_e]\ge3.
   \]

If, in addition, every anchored beta-killing extension satisfies

\[
[\Gamma_e:H_e]\le2,
\]

then a counterexample can exist only if **every** such extension has a persistent bad replacement symmetry surviving both colors.

This converts the remaining beta-one problem into a sharply defined defect-one replacement classification.

## 8. Relation to affine bad sets

For `|E|=1`, every affine subset of the color cube `F_2` is one of

\[
\varnothing,
\quad\{0\},
\quad\{1\},
\quad\mathbf F_2.
\]

The theorem above is the group-theoretic refinement of this trivial affine classification:

- `F_2` corresponds to Type P for some bad replacement symmetry;
- the cover `{0} union {1}` with no common bad symmetry corresponds to Type S and requires distinct `H_e`-cosets.

Thus the full affine-cover problem at beta one has now been reduced to two replacement-group mechanisms.

## 9. Next theorem target

The remaining strongest route to

\[
\boxed{\beta=1\Longrightarrow\alpha=1}
\]

is now to exclude the two fatal mechanisms globally:

1. **Persistent exclusion:** show that not every anchored beta-killing cell can support a defect-one bad symmetry which survives both colors;
2. **Split exclusion:** show that some anchored beta-killing cell has replacement index at most two, or otherwise prove that its distinct bad cosets cannot cover opposite colors.

A weaker result excluding either mechanism on a broad structural class would already close beta one on that class.

## Claim firewall

1. The persistent-or-split dichotomy is theorem-level for anchored beta-killing singleton extensions.
2. The index bound is necessary for Type S, not sufficient.
3. `Gamma_e` is the uncolored domain automorphism group; `H_e` is the common D-preserving reduct core.
4. The global beta-one theorem remains open.
