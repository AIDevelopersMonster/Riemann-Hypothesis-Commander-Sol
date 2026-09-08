# FCOA Rigidity Cost — Safe Escape-Cell Theorem (Corrected)

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** corrected post-publication theorem note.

## 1. Correction notice

An earlier version stated that intrinsic recognizability of the new-cell set alone was sufficient for a beta-optimal extension to be exact. That was too strong: a surviving old-good anonymous automorphism can, in principle, acquire an independent phase on an enlarged incidence component containing only new cells.

The correct theorem requires **anchoring** in addition to recognizability.

## 2. Definitions

Let

\[
S=D\cup E.
\]

The new-cell set `E` is **recognizable relative to D** if every carrier automorphism of the uncolored extended domain preserves `D` setwise (equivalently, preserves `E` setwise).

The extension is **D-anchored** if every connected component of

\[
\Lambda(S)
\]

contains at least one old cell from `D`.

The extension is **beta-valid** if every old bad automorphism of `(G;D,Q_D)` is destroyed in the enlarged ternary reduct.

## 3. Correct Safe Escape Theorem

### Theorem

If `(E,b)` is beta-valid, recognizable relative to `D`, and D-anchored, then

\[
\boxed{
\operatorname{Aut}(G;S,Q_S)
=
\operatorname{Aut}^{\pm}(S,c\cup b).
}
\]

In particular, if `|E|=beta(D,c)`, then

\[
\boxed{\alpha(D,c)=\beta(D,c).}
\]

### Proof

Let `h` preserve the enlarged ternary reduct. Recognizability gives `hD=D`, so the restriction of `h` lies in the old reduct automorphism group. Beta-validity excludes all old bad automorphisms; therefore one global old phase `epsilon in F_2` works on every old cell.

By the Componentwise Phase Theorem, the discrepancy of `h` is constant on each connected component of `Lambda(S)`. Since every such component contains an old cell, its phase must equal the old global phase `epsilon`. Hence the same phase works on all cells of `S`, so `h` is globally anonymous-color compatible. The reverse inclusion is automatic. `square`

## 4. Single-cell corollary

If `beta(D,c)=1` and there exists a beta-killing cell `e` such that:

1. `e` is adjacent in `Lambda(D union {e})` to at least one old cell; and
2. every automorphism of the uncolored domain `D union {e}` fixes `e` as the unique new cell,

then

\[
\boxed{\alpha(D,c)=1.}
\]

For a one-cell extension, condition 1 is exactly D-anchoring and condition 2 is recognizability.

## 5. Signature certificates

Any domain-invariant cell signature may certify recognizability. Useful sufficient coordinates include:

- reverse-definedness;
- in/out-degree data of the cell endpoints;
- incidence-component size;
- further isomorphism-invariant local domain data.

If every new cell has a signature absent from the old domain and the extension is D-anchored, the theorem applies.

The disjoint-bidirected-pair construction satisfies this by reverse-definedness: old cells occur in bidirected pairs while the chosen bridges are one-way and attached to old components.

## 6. Exact one-cell kill criterion for old bad automorphisms

Let `g` be an old bad automorphism and `e` an undefined cell. Since `gD=D`, adding the singleton `e` kills `g` precisely if either:

1. `g(e) != e`, so the enlarged domain is not `g`-invariant; or
2. `g(e)=e` and the fixed new cell is attached to an old phase-1 incidence component, forcing discrepancy `0=1` in the enlarged component.

This criterion is independent of the binary value assigned to `e`. The color matters only for possible newly created automorphisms of the enlarged domain.

## 7. Current evidence

The Anchored-Recognizable theorem has been verified exhaustively as a sufficient mechanism on the complete five-carrier nonexact space: all 89,880 nonexact layers admit a one-cell repair of this type.

A separate random six-carrier stress search over 1,000,000 sparse binary layers found 19,408 nonexact layers with `beta=1`; every such sampled layer admitting an exact one-cell repair also had an anchored-recognizable beta-killing one-cell repair. This is exploratory evidence, not an exhaustive six-carrier theorem.

## Claim firewall

1. Recognizability alone is not sufficient; anchoring is required.
2. The theorem is sufficient, not a proof that anchored-recognizable beta-minimizers always exist.
3. The random six-carrier stress test is evidence only.
4. Articles A and B remain frozen publications.
