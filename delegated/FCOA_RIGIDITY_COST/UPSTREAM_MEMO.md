# FCOA Rigidity Cost — Upstream Memo

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Audience:** main Commander Sol scientific director  
**Status:** audited local results for upstream review; nothing here modifies M0–G4 automatically.

## Executive verdict

The original U1–U8 package remains valid. A ninth, now hostile-audited theorem package closes the first sparse multicolor target.

## U1–U8

U1–U8 are the previously recorded rigidity-cost, terminal-layer, tournament-separator, reconstruction, betweenness, binary ternary-phase, and complete-domain multicolor arity results. Their detailed statements remain in the dedicated theorem notes and in the prior history of this memo.

The key boundary inherited from U7/U8 is

\[
\boxed{
q=2:\ \text{ternary phase propagation is universally exact on the complete binary layer},
}
\]

while in the bounded local anonymous equality-pattern class

\[
\boxed{
q\ge3:\ k_{exact}=4.
}
\]

## U9. Sparse multicolor ternary transport theorem

**Status:** hostile-audited and approved for upstream insertion.  
**Full handoff:** `QGE3/UPSTREAM_MEMO_QGE3.md`  
**Audit:** `QGE3/HOSTILE_AUDIT_COMMANDER_SOL.md`

For a finite surjective anonymous coloring

\[
c:D\to O,\qquad |O|=q\ge3,
\]

on a sparse off-diagonal domain, let Model T retain `D` and ternary equality only between composable defined cells.

The naive binary generalization

\[
\text{connected comparison component}
\Longrightarrow
\text{one local }S_q\text{ phase}
\]

is false for every `q>=3`.

### Sharp q=3 minimum

There is a connected counterexample already on

\[
\boxed{|G|=3,\qquad |D|=4,}
\]

and no surjective q=3 counterexample can have three cells. Thus `|D|=4` is the exact minimum domain size.

### Universal local state

Contract equal-comparison edges in a component `C` into T-equality atoms. The quotient `H_T(C)` is a graph whose original terminal fibers give a proper coloring `kappa_C`.

Every Model-T automorphism transports this proper coloring. The universally defined local datum is therefore its anonymous proper-coloring state, not an `S_q` element.

A local visible-support phase exists exactly when

\[
\boxed{
c(p)=c(q)\iff c(gp)=c(gq)\quad(p,q\in C).}
\]

### Phase sector

Where local phases exist,

\[
\boxed{
\phi_{gh,C}=\phi_{g,hC}\circ\phi_{h,C}.
}
\]

The intrinsic coefficient object is a groupoid of visible-support bijections. It becomes `S_q`-valued only in the full-support sector.

### Exact global gluing

Let

\[
R_g=\bigcup_C\operatorname{graph}(\phi_{g,C}).
\]

Then

\[
\boxed{
g\in Aut^{an}(D,c)
\iff
R_g\text{ is the graph of a permutation of }O.}
\]

Hence Model-T failure for `q>=3` has two structurally distinct layers:

\[
\boxed{
\text{local proper-coloring ambiguity}
+
\text{inter-component gluing ambiguity}.
}
\]

### Safe full-support cost layer

After local phase existence,

\[
0\le\lambda_q^{ph}(D,c)\le(q-1)(r-1),
\]

and the worst-case abstract point-image synchronization capacity satisfies

\[
\boxed{r-1\le L_q(r)\le(q-1)(r-1).}
\]

Exact `L_q(r)` for `q>=3` remains open. No real-cell multicolor `alpha_q` is presently defined.

## Updated structural hierarchy

\[
\boxed{
\begin{array}{rcl}
q=2 &:& \text{connected sparse comparison geometry carries a phase bit},\\
q\ge3 &:& \text{connectedness need not produce any color phase},\\
q\ge3 &:& \text{universal local state is proper-coloring transport},\\
\text{phase-admissible sector} &:& \text{visible-support groupoid + gluing},\\
\text{arbitrary finite }q &:& \text{four-ary arbitrary-cell equality is exact}.
\end{array}}
\]

The conceptual phase transition is therefore deeper than noncommutativity: for `q>=3`, the obstruction can occur before a group-valued phase exists.

## Publication and insertion rule

Any new manuscript generated from U9/QGE3 must comply with the canonical FCOA Definition 1.0 directive on `main`.

Foundation DOI:

`https://doi.org/10.5281/zenodo.22164246`

It must appear explicitly in the Abstract/Аннотация and as a full Foundation bibliographic entry. The manuscript body must also identify the concrete FCOA carrier/sorts/signature/baseline/erasure/recovery/arithmetic-firewall data.

Already published archival Articles A and B are not rewritten merely to add this citation.

## Recommendation

U9 is approved for insertion into the main Rigidity Theory and for a separate focused QGE3 publication.

Next research target:

\[
\boxed{L_q(r)=?}
\]

followed later by the genuinely harder real operation-cell multicolor repair problem.
