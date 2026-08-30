# FCOA-Z — Symmetric Coordinate Completion

**Branch:** `director/fcoa-z-symmetric-line`  
**Working directory:** `delegated/FCOA_Z_SYMMETRIC_LINE/`  
**Status:** ACTIVE RESEARCH / FOUNDATION PHASE  
**Started:** 2026-08-30  
**Parent programme:** FCOA — Fixed-Carrier Oriented Algebra

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

The resulting carrier will then be proved canonically isomorphic, as an oriented pointed line, to the ordinary integer line.

This keeps the FCOA Arithmetic Firewall intact:

\[
\text{signed coordinates}\neq\text{primitive }+\text{ or }\times.
\]

---

## 2. Why this branch is separate

The existing note `papers/FCOA-ADMISSIBILITY-GEOMETRY/SUCCESSOR_RECURSION_AND_INTEGER_LINE.md` treats the integer line as a given ambient carrier and then studies generated addition on it.

FCOA-Z changes the order of construction:

1. start from the rooted natural-coordinate ray;
2. add a mirrored branch around the fixed origin;
3. define the reflection involution geometrically;
4. define successor/predecessor across the origin;
5. prove that this signed completion is the integer line;
6. only afterwards ask which arithmetic relations are generated or recovered;
7. only afterwards extend the legacy FCOA operations and their output channels.

Thus this branch does **not** invalidate the earlier integer-line note. It supplies a stronger foundational route to its ambient carrier.

---

## 3. Primary object

The unsigned starting ray is

\[
R=\{P_0,P_1,P_2,\ldots\}.
\]

The signed completion will have carrier

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

The branch must preserve the following FCOA principles.

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

remain typed output channels. Their possible mirror extensions are studied separately from the base-line reflection.

### 4.6 Arithmetic remains a leakage/recovery question

The branch asks whether a given signed FCOA structure recovers

\[
<,\quad \operatorname{EqSignedGap},\quad Add,\quad Mul,
\]

rather than assuming these relations.

---

## 5. Initial theorem programme

The first foundation package must contain proofs of the following statements before any theorem is promoted to FIXED.

1. **Signed Completion Theorem.** The two-branch completion with its declared successor/predecessor structure is canonically isomorphic to the pointed oriented integer line.
2. **Reflection Characterization.** The origin-fixing involution satisfying
   \[
   \nu S=P\nu
   \]
   is unique.
3. **Coordinate Rigidity.** Once `P_0` and the oriented successor are retained, the full base carrier has trivial automorphism group.
4. **Erasure Symmetry Table.** Removing the origin and/or orientation produces precisely classified translation/reflection symmetries.
5. **Finite Window Coherence.** Symmetric windows must be restrictions of one infinite signed structure; no wrap-around is permitted.
6. **Arithmetic Firewall.** Signed completion alone does not identify any legacy operation with `+` or `\times`.

---

## 6. Legacy-operation transfer programme

Only after the base signed line is fixed will the branch extend the old operation tables.

Every binary operation will be split into four signed sectors:

\[
(++),\qquad (+-),\qquad (-+),\qquad (--).
\]

The branch will distinguish:

- **mirror-forced cells** — if an explicit equivariance law is adopted and proved compatible;
- **legacy-preserved cells** — inherited from the positive ray;
- **new signed cells** — genuinely new mixed-sign behaviour;
- `UNDEF` — fixed mathematical undefinedness;
- `OPEN` — research locations where no extension law is yet selected.

No rule such as

\[
(-)\star(-)=(+)
\]

is imported by analogy with arithmetic.

---

## 7. Output-channel programme

The current canonical FCOA foundation already treats output families as disjoint typed sorts and terminal by default.

FCOA-Z will test a signed fiber extension of the form

\[
E_n^{\alpha,+},\qquad E_n^{\alpha,-}
\]

with candidate reflection

\[
\nu_\alpha(E_n^{\alpha,+})=E_n^{\alpha,-}.
\]

This does **not** yet assert that every old operation commutes with reflection. Equivariance laws such as

\[
\nu_\alpha(x\star y)=\nu(x)\star\nu(y)
\]

must be separately declared and audited.

This distinction is required if the output fibers are later to become transport channels between multiple coordinate lines.

---

## 8. Long-range geometric route

FCOA-Z is deliberately designed so that a later programme may replace terminal output channels by re-enterable inter-line channels.

The possible progression is

\[
\boxed{
\text{rooted ray}
\to
\text{zero-symmetric line}
\to
\text{line with signed fibers}
\to
\text{interacting lines}
\to
\text{path/operator geometry}.
}
\]

Ordinary lattice geometry should arise only as a special commuting case. If longitudinal and transverse transports fail to commute or are partial, the resulting geometry need not reduce to \(\mathbb Z^d\).

---

## 9. Publication discipline

This is a research branch, not a publication claim.

- No theorem is published without a proof.
- No candidate result is promoted merely because it matches ordinary integer intuition.
- Classical facts about pointed lines, successor structures, torsors, Cayley graphs, Presburger arithmetic, groupoids, quivers, or noncommutative geometry must not be claimed as FCOA discoveries.
- Potential novelty lies in the FCOA-specific combination of fixed coordinates, partial oriented operations, typed output fibers, erasure/recovery diagnostics, resource cost, and later inter-line channel composition.

---

## 10. Current next step

Construct and audit the signed base carrier before touching multiplication or multi-line geometry:

\[
\boxed{
R\rightsquigarrow B^{\pm}
\rightsquigarrow (B^{\pm},P_0,S,P,\nu,<)
\cong
(\mathbb Z,0,S_{\mathbb Z},P_{\mathbb Z},-,<).
}
\]

The isomorphism symbol above refers only to the **pointed oriented-line structure**. It does not import ordinary binary addition or multiplication.