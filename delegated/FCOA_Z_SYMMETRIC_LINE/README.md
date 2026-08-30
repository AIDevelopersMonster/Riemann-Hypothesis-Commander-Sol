# FCOA-Z — Symmetric Coordinate Completion

**Branch:** `director/fcoa-z-symmetric-line`  
**Working directory:** `delegated/FCOA_Z_SYMMETRIC_LINE/`  
**Status:** PUBLISHED CORE / ACTIVE RESEARCH CONTINUATION  
**Started:** 2026-08-30  
**Parent programme:** FCOA — Fixed-Carrier Oriented Algebra  
**Published paper:** [10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264)

---

## 0. Published milestone

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

The publication closes the first theorem nucleus, not the research programme. Mixed-sign generators, output re-entry, line-completion/no-go theorems, and dimension-forcing tests remain active research.

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
7. only afterwards extend the legacy FCOA operations and their output channels.

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

---

## 5. Published theorem nucleus

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

The canonical mixed-sign value law is **not** part of the published theorem nucleus.

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

The first FCOA-Z paper is published at:

**[https://doi.org/10.5281/zenodo.22169264](https://doi.org/10.5281/zenodo.22169264)**

The branch itself remains active.

- No theorem is published without a proof.
- No candidate result is promoted merely because it matches ordinary integer intuition.
- Classical facts about pointed lines, successor structures, torsors, Cayley graphs, Presburger arithmetic, group completions, groupoids, quivers, graded algebras, or noncommutative geometry must not be claimed as FCOA discoveries.
- Potential novelty lies in the FCOA-specific combination of fixed coordinates, partial oriented operations, typed output fibers, erasure/recovery diagnostics, sector-local law formation, and later inter-line channel composition.

---

## 10. Current next step

The published line is now the fixed base. The active problem is:

\[
\boxed{
\text{classify conservative realizations of mixed cells and }E\text{-outputs before allowing a second dimension}.
}
\]

This includes exact tests of mixed generators, root-cell completion, output re-entry, automorphism change, commutation/association spectra, and arithmetic leakage.