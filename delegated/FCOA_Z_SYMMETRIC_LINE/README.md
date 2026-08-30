# FCOA-Z — Symmetric Coordinate Completion

**Branch:** `director/fcoa-z-symmetric-line`  
**Working directory:** `delegated/FCOA_Z_SYMMETRIC_LINE/`  
**Status:** PUBLISHED CORE / PUBLISHED SHADOW-RECONSTRUCTION LAYER / ACTIVE 1D RESEARCH  
**Started:** 2026-08-30  
**Parent programme:** FCOA — Fixed-Carrier Oriented Algebra  
**Published papers:**  
- [10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264) — signed-line completion and mixed-sector localization  
- [10.5281/zenodo.22179357](https://doi.org/10.5281/zenodo.22179357) — classical shadows, matrix units, and reconstruction

---

## 0. Published milestones

### 0.1 Signed-line theorem nucleus

The first FCOA-Z theorem nucleus is published as:

**Reflections on How a Ray Becomes an Axis: And Why Old Operations Reveal New Local Laws after a Second Direction Appears**  
Zenodo DOI: **[10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264)**

Published chain:

\[
\boxed{
\text{rooted ray}
\to
\text{minimal reversible completion}
\to
\text{derived reflection}
\to
\text{legacy-operation transfer}
\to
\text{punctured radialization}
\to
\text{mixed-sector localization}.
}
\]

### 0.2 Shadow-reconstruction theorem layer

The second FCOA-Z publication is:

**Classical Algebra as a Resolution-Dependent Shadow of a One-Dimensional Partial Geometry: Collapse, Matrix Units, and Reconstruction in FCOA-Z**  
Zenodo DOI: **[10.5281/zenodo.22179357](https://doi.org/10.5281/zenodo.22179357)**

Published chain:

\[
\boxed{
\begin{array}{c}
\text{direct associativization}
\Rightarrow
\text{coordinate collapse},\\[1mm]
\text{legacy translations}
\Rightarrow
 e_0
\Rightarrow
\{E_{ij}\}
\Rightarrow
M_{\mathrm{fin}}(\mathbb Z,K),\\[1mm]
(I,U,V)
\Rightarrow
\text{rooted signed-line reconstruction},\\[1mm]
(I,U,V)
\not\Rightarrow
\text{primitive provenance / definedness / terminal attachment}.
\end{array}}
\]

The publication establishes that ordinary associative algebra can arise as a resolution-dependent operator shadow without replacing the primitive partial laws. It also separates recoverable carrier geometry from operation-level information that the classical shadow forgets.

Both publications remain strictly one-dimensional at the carrier level. No second independently iterable coordinate is introduced in the shadow-reconstruction paper.

---

## 1. Mission

This branch studies the passage from the canonical rooted natural ray

\[
P_0,P_1,P_2,\ldots
\]

to a **zero-symmetric, coordinate-rigid, bi-infinite line** without importing ordinary integer addition or multiplication into the FCOA signature.

The core design decision is:

\[
\boxed{\text{do not assume }\mathbb Z\text{ as arithmetic; construct the signed line as a symmetry completion of the rooted ray.}}
\]

The resulting carrier is canonically isomorphic, as an oriented pointed line, to the ordinary integer line.

This keeps the FCOA Arithmetic Firewall intact:

\[
\text{signed coordinates}\neq\text{primitive }+\text{ or }\times.
\]

The later Shadow Ladder result changes the role of that firewall: classical algebra is no longer treated as a failure mode. Instead the programme records **which FCOA information is forgotten before a classical law appears**.

---

## 2. Why this branch is separate

The existing note `papers/FCOA-ADMISSIBILITY-GEOMETRY/SUCCESSOR_RECURSION_AND_INTEGER_LINE.md` treats the integer line as a given ambient carrier and then studies generated addition on it.

FCOA-Z changes the order of construction:

1. start from the rooted natural-coordinate ray;
2. construct the second direction by minimal reversible completion;
3. derive the reflection involution from the reversible orbit and fixed root;
4. define successor/predecessor across the origin;
5. prove that this signed completion is the integer line as a pointed oriented-line structure;
6. only afterwards ask which arithmetic relations are generated or recovered;
7. only afterwards extend the legacy FCOA operations and their output channels;
8. then study classical operator shadows and the exact resolution at which source information is lost or reconstructed.

Thus this branch does **not** invalidate the earlier integer-line note. It supplies a stronger foundational route to its ambient carrier.

---

## 3. Primary object

The unsigned starting ray is

\[
R=\{P_0,P_1,P_2,\ldots\}.
\]

The signed completion has carrier

\[
B^{\pm}
=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}.
\]

The intended line is

\[
\cdots<P_3^-<P_2^-<P_1^-<P_0<P_1^+<P_2^+<P_3^+<\cdots.
\]

Reflection about the origin is

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\]

The important point is that `+` and `-` here are initially **branch labels**, not arithmetic operations.

---

## 4. Research invariants

The branch preserves the following FCOA principles.

### 4.1 Fixed coordinate significance

Absolute position relative to `P_0` remains meaningful. Translation of the whole line is not an allowed symmetry once the origin is retained.

### 4.2 Orientation remains structural

Argument order, left/right role, and successor/predecessor direction remain available to generators.

### 4.3 Legacy operations are not replaced

The existing FCOA symbols

\[
\oplus,\qquad\otimes,\qquad\star,\ldots
\]

remain independent partial operations. They are not silently identified with ordinary integer addition or multiplication.

### 4.4 Noncommutativity and nonassociativity remain admissible

No signed-completion axiom imposes commutativity, associativity, distributivity, closure, or arithmetic sign laws on legacy operations.

### 4.5 Output sorts remain genuine sorts

The families

\[
E^+,\quad E^\ast,\quad E^\times,\ldots
\]

remain typed output channels. Their possible mirror extensions and re-entry laws are studied separately from the base-line reflection.

### 4.6 Arithmetic remains a leakage/recovery question

The branch asks whether a given signed FCOA structure recovers

\[
<,\quad \operatorname{EqSignedGap},\quad Add,\quad Mul,
\]

rather than assuming these relations.

### 4.7 Classical algebra is a shadow-resolution question

The branch now also asks whether ordinary groups, rings, matrix algebras, and associative algebras occur as operator shadows and, when they do, exactly which source distinctions survive.

---

## 5. Published theorem nuclei

### 5.1 Signed completion and radialization

The first publication establishes, with proofs:

1. **Minimal Reversible Completion.** The rooted one-sided successor ray has a unique minimal pointed reversible completion up to unique pointed shift isomorphism.
2. **Derived Reflection.** The fixed-root involution conjugating successor and predecessor is uniquely determined.
3. **Symmetry-Induced Radialization.** For every non-root coordinate,
   \[
   \boxed{x_k\oplus x_0=x_{k-\operatorname{sgn}(k)}}.
   \]
4. **Legacy role asymmetry survives.** The old noncommutative root/nonzero behavior remains on both sides.
5. **Mixed-Sector Localization.** Once the full nonnegative legacy substructure and reflection action are fixed, all remaining independent binary base freedom is confined to
   \[
   (X^+\times X^-)
   \cup
   (X^-\times X^+).
   \]

### 5.2 One-dimensional classical shadows and reconstruction

The second publication establishes, with proofs:

1. **Associative Collapse.** Direct semigroup realization preserving the audited radial `oplus` cells collapses all base coordinates.
2. **Root Isolation.** Two existing `otimes` translations isolate the root as a singleton partial identity.
3. **Matrix-Unit Generation.** Conjugating the root projector by the existing shift yields a complete system of matrix units and
   \[
   M_{\mathrm{fin}}(\mathbb Z,K),
   \]
   containing `M_n(K)` for every finite `n` while the carrier remains one-dimensional.
4. **Resolution Reconstruction.** The finitary matrix algebra alone forgets the line, `(I,U)` reconstructs the oriented line up to translation, and `(I,U,V)` reconstructs the rooted signed line.
5. **Provenance No-Go.** The generated base algebra does not determine whether certain operators were primitive `oplus` translations or derived from the existing `otimes`/kinematic shadow.
6. **Definedness and Terminal Loss.** A base-only shadow cannot reconstruct the distinction between true `UNDEF` cells and erased terminal-valued cells, nor the `share/split` terminal attachment geometry.

The canonical mixed-sign value law is **not** part of either published theorem nucleus.

---

## 6. Legacy-operation continuation programme

Every binary operation is split into four signed sectors:

\[
(++),\qquad (+-),\qquad (-+),\qquad (--).
\]

The branch distinguishes:

- **mirror-forced cells** — determined by an adopted and audited equivariance law;
- **legacy-preserved cells** — inherited from the original ray;
- **new signed cells** — genuinely new mixed-sign behaviour;
- `UNDEF` — mathematical undefinedness retained by the current structure;
- `OPEN` — research locations where no canonical extension law has yet been selected.

No rule such as

\[
(-)\star(-)=(+)
\]

is imported by analogy with arithmetic.

The first explicit mixed commutativity test generator is recorded in `MIXED_COMMUTATIVE_BRIDGE_GENERATOR_0_1.md`; it is a candidate model, not a canonical theorem.

---

## 7. Output-channel and line-completion programme

The current FCOA foundation treats output families as disjoint typed sorts and terminal by default.

FCOA-Z now asks whether

\[
E^+,\qquad E^\ast,\qquad E^\times
\]

can be conservatively realized as re-enterable states without destroying the published line structure or silently recovering forbidden arithmetic.

The mandatory gate is recorded in:

`APPLIED_DIRECTIONS/LINE_COMPLETION_GATE.md`.

Before any claim of emergent plane/space geometry, each realization must be classified as:

- `1D-CLOSED`;
- `1D-OBSTRUCTED`;
- `DIMENSION-FORCING`.

Only a proved dimension-forcing result or an explicit audited higher-dimensional construction licenses spatial interpretation of an output channel.

---

## 8. Long-range geometric route

The possible progression is deliberately conditional:

\[
\boxed{
\text{rooted ray}
\to
\text{signed line}
\to
\text{line completion}
\to
\text{independent transport candidate}
\to
\text{Cartesian or non-Cartesian geometry}.
}
\]

Ordinary lattice geometry should arise only as a special commuting case. If longitudinal and transverse transports fail to commute or are partial, the resulting geometry need not reduce to \(\mathbb Z^d\).

The controlled roadmap is recorded in `FUTURE_LADDER_0_1.md`.

---

## 9. Publication discipline

Published FCOA-Z papers:

1. **Signed-line completion / local laws** — [10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264)
2. **Classical shadows / matrix units / reconstruction** — [10.5281/zenodo.22179357](https://doi.org/10.5281/zenodo.22179357)

The branch itself remains active.

- No theorem is published without a proof.
- No candidate result is promoted merely because it matches ordinary integer intuition.
- Classical facts about pointed lines, successor structures, torsors, Cayley graphs, Presburger arithmetic, group completions, groupoids, quivers, graded algebras, Brandt matrix units, Toeplitz/Jacobson extensions, Leavitt path algebras, or noncommutative geometry must not be claimed as FCOA discoveries.
- Potential novelty lies in the FCOA-specific mechanism by which audited partial legacy translations generate classical shadows and in the exact reconstruction-resolution hierarchy separating carrier geometry from primitive provenance, definedness, and terminal attachment.

---

## 10. Current next step

The signed line and its first Shadow Ladder layer are now published fixed bases. The active problem remains strictly one-dimensional:

\[
\boxed{
\text{find the weakest enrichment that reconstructs primitive operation labels, domains, and terminal incidence without introducing a new coordinate.}
}
\]

Mixed-cell and `E`-output realization remain behind the same Line Completion Gate. No proof is to be moved into a plane or higher-dimensional carrier merely because it may become easier there.