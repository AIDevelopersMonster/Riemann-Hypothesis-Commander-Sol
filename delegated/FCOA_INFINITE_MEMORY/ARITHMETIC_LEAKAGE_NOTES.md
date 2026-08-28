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

## B. FO+TC / MSO / computable recovery

Once transitive closure or monadic second-order quantification is admitted, global reachability becomes definable.

In a computable presentation of a single one-way successor ray, order is also algorithmically recoverable by iterating successor.

These are different recoverability frameworks. Do not write them as a single strict general hierarchy.

For this carrier the exact table is:

\[
\boxed{
\begin{array}{c|c}
\text{notion} & \text{full order from successor}\\
\hline
\text{FO} & \text{no}\\
\text{FO+TC} & \text{yes}\\
\text{MSO} & \text{yes}\\
\text{computable reconstruction} & \text{yes}
\end{array}}
\]

## C. Finite local enrichments

Naming finitely many points, adding predecessor, finitely many fixed-distance relations, or local finite output-colorings does not cross the FO full-order boundary when those additions are definable from bounded successor patterns.

The hostile audit proves a stronger statement: even an arbitrary finite family of unary predicates on the ray does not suffice to FO-define the global strict order.

Status:

\[
\boxed{\text{finite unary/local memory still does not yield FO global order}}
\]

## D. Global order compiled into domain

A one-output global-domain layer

\[
x\diamond y=\Omega\iff x<y
\]

makes strict order immediately FO-definable by definedness:

\[
\boxed{x<y\iff\operatorname{Def}(x\diamond y).}
\]

Thus one terminal output suffices if the operation domain itself is allowed to carry the full transitive order.

Status:

\[
\boxed{\text{FO global order leakage through domain memory}}
\]

## E. Complete two-fiber comparison layer

An infinite complete comparison-value layer

\[
x\chi y=\Omega_+\iff x<y,
\qquad
x\chi y=\Omega_-\iff y<x
\]

also makes the full strict order FO-definable.

Because the \(\omega\)-ray has a least point but no greatest point, \(\Omega_+\) and \(\Omega_-\) are not interchangeable by an order reversal. The positive output is internally definable.

Inside the architecture where **every off-diagonal generic pair must remain defined**, one output cannot carry orientation while two outputs suffice.

Therefore:

\[
\boxed{
|O|_{\min}=1\text{ for global order in domain},
\qquad
|O|_{\min}=2\text{ for global orientation in values with complete domain}.}
\]

Status:

\[
\boxed{\text{FO global order leakage through value-fiber memory}}
\]

## F. Hostile-audited arithmetic non-leakage

The canonical order-memory enrichments above add only discrete order information on the generic carrier. They are FO-interpretable in \((\mathbb N,<)\) with finitely many tags/copies.

Ordinary external-index addition is not FO-definable in pure \((\mathbb N,<)\). A fixed-rank FO formula cannot distinguish sufficiently long linear-order intervals whose lengths differ by one; compare, for large \(M\), the pointed triples

\[
(M,2M,3M)
\]

and

\[
(M,2M,3M+1).
\]

They have the same sufficiently shallow FO order type, while only the first satisfies \(x+y=z\).

The same interval-length argument defeats multiplication, e.g. by comparing

\[
(M,M+1,M(M+1))
\]

with

\[
(M,M+1,M(M+1)+1).
\]

Hence, for the exact canonical constructions studied in this branch,

\[
\boxed{
\text{FO global order memory}
\quad\not\Rightarrow\quad
\text{FO ordinary }+\text{ or }\times.
}
\]

This is now a theorem-level non-leakage statement for these constructions, not merely a warning that arithmetic does not automatically follow.

## G. Corrected leakage map

Do not use a one-dimensional unconditional chain. The branch now has two orthogonal coordinates:

\[
\boxed{
\text{local}\leftrightarrow\text{global memory}
\qquad\text{and}\qquad
\text{domain}\leftrightarrow\text{value-fiber memory}.}
\]

Within the exact canonical constructions:

\[
\boxed{
\text{G2 successor memory}
\;<_{\text{FO information}}\;
\text{global order memory}
\;<_{\text{not yet crossed}}\;
\text{ordinary arithmetic reconstruction}.}
\]

The first separation is proved by EF/locality. The second is proved for the order-only enrichments by interpreting them in \((\mathbb N,<)\) and using the FO nondefinability of ordinary addition and multiplication there.
