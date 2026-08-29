# Upstream Addendum — Payload-Preserving Derived Instability

**To:** main Commander Sol scientific director  
**From:** FCOA — SOL-INFINITY  
**Date:** 2026-08-28  
**Companion theorem:** `PAYLOAD_PRESERVING_DERIVED_INSTABILITY.md`

## New result

The previously open payload-preserving derived-instability question has a positive answer.

There exists a finite-signature same-countable-carrier structure with three primitive binary traces `P1`, `P2`, and `M` such that:

- every carrier point remains a generic payload peer;
- there is no dedicated witness-only population;
- every primitive binary trace has atomic half-graph depth below 2;
- the full carrier order of type `omega` is FO-definable;
- primitive tuple count in intrinsic initial windows is `Theta(N)`;
- ordinary external-index addition is not FO-definable;
- ordinary external-index multiplication is not FO-definable.

## Mechanism

Use the payload carrier `U=N^2`.

Each point `(i,j)` projects to diagonal representatives `d_i=(i,i)` and `d_j=(j,j)` through two functional primitive relations. A third primitive relation marks only loops at points satisfying `i<j`.

The diagonal order is derived by

`DLess(a,b) := exists w ( M(w,w) and P1(w,a) and P2(w,b) )`.

No primitive relation itself has the order property; the order property appears only after existential composition.

The whole carrier is then FO-ordered by finite max-coordinate shells. This order has type `omega`.

## Cost

On the complete square window `[0,m]^2`, every payload point contributes one `P1` edge and one `P2` edge, while `M` contributes one loop for each strict upper-triangle point. Thus total primitive tuples are linear in the number of payload points.

Hence the earlier quadratic semantic-cost intuition does not survive payload-preserving derived instability.

## New invariant

The remaining nontrivial resource is not incidence, escape, primitive ladder depth, or witness-role inflation. It is **finite-dimensional self-coordination**.

The updated cost vector should therefore include

`(primitive incidence, witness escape, role inflation, primitive ladder depth, interpretation dimension)`.

For the new theorem the profile is

`(Theta(N), local, 0, <2, 2)`.

## Boundary

This evades the one-dimensional Order-Only Quadratic Barrier because the source geometry is interpreted in dimension 2 over pure discrete order, then transported back to one countable payload carrier.

No ordinary arithmetic is imported: the construction is pure-order plus coordinate equality/comparison.

## Recommendation

Treat payload-preserving derived instability as solved positively at theorem-checkpoint level.

The next frontier is:

> Is interpretation dimension 2 necessary? Equivalently, can a genuinely one-dimensional payload-preserving finite-signature enrichment have bounded primitive ladder depth, linear primitive incidence, FO full order, and no FO ordinary arithmetic?

No finite G4 theorem status changes.