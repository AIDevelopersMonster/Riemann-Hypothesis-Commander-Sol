# FCOA-Z — Classification of Inward-Covariant Mixed Generators

Status: theorem package v0.1  
Date: 2026-08-30

This note strengthens `MIXED_RADIAL_CANCELLATION_GENERATOR.md`.

## 1. Problem

The preceding note exhibited one natural mixed-sign generator. The sharper question is whether this generator is merely one convenient choice or whether it is forced by a small intrinsic axiom package.

The answer is exact within the class of extensions invariant under simultaneous inward radial reduction:

> every such extension is completely determined by its trace on the first zero-port boundary; if the inherited FCOA zero-port boundary is preserved, the mixed extension is unique.

Thus radial cancellation is not globally forced by the earlier FCOA-Z paper, but **is canonical inside the inward-covariant boundary-local class**.

## 2. Mixed carrier and reduction

Let

\[
M=(X_+\times X_-)\cup(X_-\times X_+)
\]

be the mixed sector of the signed FCOA-Z axis.

For `(x,y) in M`, while neither coordinate is the root, define

\[
C(x,y)=(\rho x,\rho y),
\]

where `rho` is the already-derived one-step contraction toward the distinguished root.

Let the zero-port boundary be

\[
B=((X\times\{x_0\})\cup(\{x_0\}\times X)).
\]

For mixed inputs, repeated application of `C` reaches exactly one element of `B` after

\[
\min\{d(x),d(y)\}
\]

steps.

Write

\[
N:M\to B
\]

for this first-boundary normal-form map.

Because the reduction is deterministic and decreases total radial depth by two, `N` is well defined.

## 3. Inward covariance

Let `Y` be any output sort equipped, when needed, with reflection `nu_Y`.

A partial mixed map

\[
F:M\rightharpoonup Y
\]

is called **inward-covariant** if for every mixed pair with both coordinates still non-root after one reduction,

\[
F(x,y)\simeq F(C(x,y)),
\]

where `simeq` means equality together with preservation of defined/undefined status.

Equivalently, `F` is constant along each finite inward-reduction chain.

This is the intrinsic content of the radial-cancellation generator; no coordinate addition is mentioned.

## 4. Boundary Trace Classification Theorem

### Theorem 4.1

Restriction to the first zero-port boundary gives a bijection

\[
\boxed{
\{\text{inward-covariant partial mixed maps }F:M\rightharpoonup Y\}
\cong
\{\text{partial boundary assignments }\beta:N(M)\rightharpoonup Y\}.
}
\]

The two directions are:

\[
F\longmapsto \beta_F,
\qquad
\beta_F(b)=F(z)\quad\text{for any }z\in M\text{ with }N(z)=b,
\]

and

\[
\beta\longmapsto F_\beta,
\qquad
F_\beta(z)=\beta(N(z)).
\]

Defined/undefined status is transported in the same way.

#### Proof

Fix an inward-covariant `F`. If `N(z)=b`, repeated inward covariance gives

\[
F(z)\simeq F(Cz)\simeq\cdots\simeq F(b),
\]

where the last expression denotes the boundary trace reached by the chain. Hence all mixed inputs with the same normal form must have the same value/undefined status. Therefore `F` induces a unique partial boundary assignment `beta_F`.

Conversely, given any partial boundary assignment `beta`, define

\[
F_\beta(z)=\beta(N(z)).
\]

Since `N(Cz)=N(z)` whenever one inward step is allowed,

\[
F_\beta(Cz)=\beta(N(Cz))=\beta(N(z))=F_\beta(z),
\]

including definedness. Thus `F_beta` is inward-covariant.

The two constructions are inverse because an inward-covariant map is constant on each normal-form fiber and every boundary assignment is recovered by restricting its induced map to the corresponding normal forms. □

## 5. Orbit/quotient interpretation

### Corollary 5.1

The normal-form map `N` identifies the quotient of the mixed sector by inward-reduction equivalence:

\[
(x,y)\sim_C(x',y')
\quad\Longleftrightarrow\quad
N(x,y)=N(x',y').
\]

Every inward-covariant mixed operation factors uniquely as

\[
M\xrightarrow{N}N(M)\xrightarrow{\beta}Y.
\]

Thus the entire mixed extension problem in this class reduces to a boundary-value problem.

This is a deterministic normal-form construction. The general fact that terminating/confluent rewriting systems support unique normal forms is classical; here the reduction is stronger than merely confluent because there is exactly one possible reduction step at every reducible mixed pair.

## 6. Exact boundary image

### Proposition 6.1

The reachable normal-form boundary is

\[
N(M)=
\{(x_k,x_0):k\neq0\}
\cup
\{(x_0,x_k):k\neq0\}
\cup
\{(x_0,x_0)\}.
\]

Every listed boundary point is reached by a mixed pair.

#### Proof

Unequal input depths leave one non-root survivor and one root; equal depths give root/root. Conversely, for any `k != 0`, choose an opposite-side depth-one partner and place the survivor one level deeper than the desired boundary depth; simultaneous inward reduction reaches the required one-root boundary point. Root/root is reached from every opposite pair of equal depth. □

Hence the quotient is one-dimensional on each oriented surviving side, plus one collision class.

## 7. Reflection classification

Reflection on mixed pairs is

\[
\widehat\nu(x,y)=(\nu x,\nu y).
\]

Since `nu rho = rho nu`,

\[
N(\widehat\nu z)=\widehat\nu N(z).
\]

### Theorem 7.1 — Reflection Reduction Principle

Let `Y` carry an involution `nu_Y`. An inward-covariant mixed map `F_beta` is reflection-equivariant iff its boundary assignment is reflection-equivariant:

\[
\beta(\widehat\nu b)\simeq \nu_Y(\beta(b))
\]

for every reachable boundary point `b`.

#### Proof

For any mixed `z`,

\[
F_\beta(\widehat\nu z)
=\beta(N(\widehat\nu z))
=\beta(\widehat\nu N(z)).
\]

Thus boundary equivariance implies

\[
F_\beta(\widehat\nu z)
\simeq\nu_Y\beta(N(z))
=\nu_YF_\beta(z).
\]

Necessity follows by evaluating equivariance on representatives whose normal forms are the specified boundary points. □

So reflection imposes no hidden interior constraints beyond the boundary trace.

## 8. Legacy-boundary rigidity

Now specialize to the original FCOA output sort and require that the reachable zero-port boundary retain the already fixed legacy laws:

\[
x_0\oplus x=x,
\]

\[
x\oplus x_0=\rho(x),
\]

for `x != x_0`, while

\[
x_0\oplus x_0
\]

remains UNDEF.

These conditions determine the boundary assignment uniquely.

### Theorem 8.1 — Canonical Mixed Extension inside the Inward-Covariant Class

There is exactly one partial mixed extension satisfying:

1. inward covariance under simultaneous radial contraction;
2. preservation of every inherited reachable zero-port boundary cell, including UNDEF at root/root.

It is the Radial Cancellation Extension of `MIXED_RADIAL_CANCELLATION_GENERATOR.md`.

If the inherited boundary is already reflection-equivariant, the unique mixed extension is automatically reflection-equivariant.

#### Proof

By Theorem 4.1 an inward-covariant mixed extension is uniquely determined by its boundary assignment. Legacy preservation fixes that assignment on all of `N(M)` by Proposition 6.1. Therefore exactly one extension exists. Theorem 7.1 supplies reflection equivariance. □

This is the sought canonicality statement.

## 9. Minimal axiom audit

The preceding theorem shows that several previously listed requirements are logically redundant inside this class.

A sufficient package is only:

**A1. Signed FCOA-Z carrier with the already-derived radial contraction `rho`.**  
**A2. Inward covariance:** simultaneous contraction of a mixed pair does not change its operation value or definedness until the boundary is reached.  
**A3. Legacy boundary preservation:** first zero-port boundary cells retain their inherited values/UNDEF status.

Then:

- termination is forced by radial depth;
- boundary locality is not an additional axiom, but a theorem;
- uniqueness is forced;
- reflection equivariance is inherited automatically if the legacy boundary and `rho` are reflection-compatible;
- no new terminal output sort is introduced because the boundary assignment already lands in the inherited output structure.

Thus the original five-item candidate axiom list compresses to three essential ingredients.

## 10. Independence cautions

The theorem does **not** say that A2 itself follows from reversible completion or reflection. It does not.

Without A2, Mixed-Sector Localization from the preceding paper leaves arbitrary reflection-orbits of mixed cells available.

Without A3, Theorem 4.1 shows there are as many inward-covariant extensions as boundary assignments.

Therefore the canonicality result is conditional but sharp:

\[
\boxed{
\text{inward covariance + inherited boundary}
\Longrightarrow
\text{unique mixed law}.
}
\]

## 11. Classical comparison boundary

The normal-form factorization has classical rewriting-system ancestry: terminating/confluent systems yield unique normal forms, and bicyclic-type shift/inverse-shift structures exhibit cancellation normal forms. No novelty is claimed for that abstract mechanism.

The FCOA-Z-specific theorem is the combination of:

- a mixed sector created by reversible completion of a one-sided legacy carrier;
- a radial reduction inherited from a noncommutative partial FCOA zero-port law;
- complete classification of inward-covariant extensions by boundary trace;
- rigidity of that trace under legacy preservation;
- the resulting forced local commutation and association phase laws established in the companion theorem package.

Any publication-level novelty statement must remain limited to this conjunction pending a dedicated literature audit.

## 12. Consequence for the programme

The original next-strike question was:

> find a natural generator of mixed-sign interaction that is not a hand-written case table.

That question is now answered positively.

The stronger follow-up question was:

> characterize the mixed generators forced by a minimal intrinsic axiom package.

Within the inward-covariant class, that question is now also answered:

\[
\boxed{
F=\beta\circ N,
}
\]

and legacy preservation fixes `beta` uniquely.

The active frontier therefore moves again.

## 13. Next strike

There are now two genuinely new directions.

### Direction I — remove or weaken inward covariance

Classify reflection-equivariant mixed generators satisfying weaker locality axioms. Determine the first extra degree of freedom when exact invariance

\[
F(x,y)=F(\rho x,\rho y)
\]

is weakened to a finite-state cocycle, output transport, or bounded-memory law.

This asks where nontrivial mixed dynamics first appears beyond the rigid normal-form class.

### Direction II — branching carrier

Replace the two-ray axis by a rooted tree. Radial contraction still exists, but after equal-depth cancellation two inputs may retain branch information. Determine whether the boundary quotient becomes a branch-pair geometry and whether the five association statuses refine into a branch-sensitive phase diagram.

Of these, Direction I is the sharper continuation of the present theorem chain because it directly identifies the first freedom beyond the now-classified canonical mixed law.