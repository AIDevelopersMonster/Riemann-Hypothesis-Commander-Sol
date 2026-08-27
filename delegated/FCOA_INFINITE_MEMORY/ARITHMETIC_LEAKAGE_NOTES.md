# Arithmetic Leakage Notes — Infinite Memory Direction

## Scope

This file records only leakage observations relevant to infinite-order recoverability.

## A. Successor/domain memory

The infinite G2 layer recovers only the successor relation on the generic ray:

\[
S(x,y)\iff \operatorname{Def}(x\star y).
\]

This does **not** by itself FO-define the transitive strict order.

Status:

\[
\boxed{\text{local directed memory; no FO global order leakage}}
\]

## B. FO+TC / MSO

Once transitive closure or monadic second-order quantification is admitted, global reachability becomes definable.

This is a logical-strength increase, not an enrichment of the FCOA operation itself.

Status:

\[
\boxed{\text{global order recoverable, but not by ordinary FO}}
\]

No claim is made that this alone reconstructs ordinary addition or multiplication.

## C. Finite local enrichments

Naming finitely many points, adding predecessor, finitely many fixed-distance relations, or local finite output-colorings does not cross the FO full-order boundary when those additions are definable from bounded successor patterns.

Status:

\[
\boxed{\text{no new FO global-order leakage}}
\]

## D. Complete two-fiber comparison layer

An infinite complete comparison-value layer

\[
x\chi y=\Omega_+\iff x<y,
\qquad
x\chi y=\Omega_-\iff y<x
\]

makes the full strict order FO-definable.

This is a genuine increase in memory strength:

\[
\boxed{\text{FO global order leakage}}
\]

However, it still does not automatically yield ordinary arithmetic operations on external indices. Addition and multiplication must not be inferred merely from the presence of a definable linear order.

## E. Leakage hierarchy for this branch

\[
\boxed{
\text{successor memory}
\;<\;
\text{FO global order memory}
\;<\;
\text{arithmetic reconstruction}
}
\]

The first two levels are now separated rigorously in this branch. The third is not established and must remain a separate question.
