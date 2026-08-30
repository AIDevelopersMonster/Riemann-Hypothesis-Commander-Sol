# FCOA QGE3 — Upstream Memo

**To:** Commander Sol, lead FCOA Rigidity Cost line  
**From:** delegated QGE3 line; hostile-audited by Commander Sol  
**Status:** **ACCEPTED FOR UPSTREAM INSERTION**  
**Audit:** `HOSTILE_AUDIT_COMMANDER_SOL.md`

## 1. Upstream theorem

### Multicolor Sparse Ternary Transport Theorem

Let `c:D->O` be a finite surjective anonymous terminal coloring with `|O|=q>=3`, and let Model T retain the sparse domain `D` together with ternary equality only between composable defined cells.

Then connectedness of the ordered-cell comparison graph does **not** force a componentwise color permutation. The universal local state of a comparison component `C` is the proper-coloring state of its T-constraint quotient `H_T(C)`.

More precisely:

1. every Model-T carrier automorphism transports `H_T(C)` and its proper coloring;
2. a local visible-support phase exists exactly when the transported fiber partition equals the original fiber partition;
3. where local phases exist they satisfy
   \[
   \phi_{gh,C}=\phi_{g,hC}\circ\phi_{h,C};
   \]
4. the intrinsic phase object is therefore a groupoid of visible-support bijections, reducing to an `S_q`-valued crossed law in the full-support sector;
5. local phases glue to a global anonymous output permutation exactly when
   \[
   R_g=\bigcup_C\operatorname{graph}(\phi_{g,C})
   \]
   is the graph of a permutation of `O`.

Hence sparse multicolor ternary exactness splits into two independent obstructions:

\[
\boxed{
\text{local proper-coloring ambiguity}
+
\text{inter-component gluing ambiguity}.
}
\]

## 2. Sharp minimum q=3 witness

For

\[
G=\{0,1,2\},
\quad
D=\{(0,1),(0,2),(1,0),(1,2)\},
\]

with

\[
c(0,1)=c(0,2)=0,
\quad c(1,0)=1,
\quad c(1,2)=2,
\]

the comparison graph is connected and `g=(0 1)` preserves Model T, but the two source-0 cells are transported to colors 1 and 2. Thus no local color function exists.

The domain-size minimum is exact:

\[
\boxed{|D|_{min}=4.}
\]

Surjective `q=3` with three cells uses every color exactly once, so every domain-preserving carrier permutation automatically induces a color permutation.

## 3. Explicit extension to every q>=3

For each new color `j=3,...,q-1`, add a fresh carrier point `x_j`, fixed by `g=(0 1)`, and the two cells

\[
(0,x_j),\qquad(1,x_j),
\]

both colored `j`.

These cells are exchanged by `g`, introduce no new equal-colored composable pair, and are attached to the original comparison component through `(1,0)~(0,x_j)` and `(0,1)~(1,x_j)`. Thus the comparison graph remains connected and the original contradiction `phi(0)=1≠2=phi(0)` survives.

Therefore the componentwise `S_q`-phase no-go holds for every `q>=3`.

## 4. Exact local criterion

For a component `C`, contract equal-comparison edges into T-equality atoms and let `H_T(C)` be the quotient graph. The original terminal fibers induce a proper coloring `kappa_C`.

A local phase for `(g,C)` exists iff the transported coloring has the same fiber partition:

\[
\boxed{
c(p)=c(q)\iff c(gp)=c(gq)\qquad(p,q\in C).}
\]

Equivalently the original and transported proper colorings lie in the same orbit under anonymous color relabeling.

Color-rigid/uniquely colorable quotients are a sufficient structural sector in which every Model-T automorphism acquires a local phase.

## 5. Exact global gluing criterion

Assume all local phases exist. Put

\[
R_g=\bigcup_C\operatorname{graph}(\phi_{g,C}).
\]

Then

\[
\boxed{
g\in Aut^{an}(D,c)\iff R_g\text{ is the graph of a permutation of }O.}
\]

The two possible defects are source disagreement and target collision. In the full-support sector this reduces to equality of all component phases, i.e. membership in the diagonal copy `Delta(S_q) subset S_q^r`.

## 6. Safe synchronization cost statement

Only after local phase existence, and only in the full-support sector, define the point-image synchronization cost `lambda_q^ph`. The audited bounds are

\[
0\le\lambda_q^{ph}(D,c)\le(q-1)(r-1),
\]

and for unrestricted abstract phase tuples

\[
\boxed{r-1\le L_q(r)\le(q-1)(r-1).}
\]

The lower bound uses common **left composition** on a disconnected constraint block. Exact `L_q(r)` for `q>=3` remains open.

No real-cell multicolor `alpha_q` is defined or claimed.

## 7. Relation to frozen publications

- Article A remains unchanged: in its stated local anonymous equality-pattern class, `q=2` has ternary exactness while `q>=3` universally requires arity 4.
- Article B remains unchanged: its binary component phase/cocycle theory is recovered as the exceptional case where a connected binary constraint quotient has a unique two-color partition up to swap.
- QGE3 is a continuation theorem package, not a revision of either publication.

## 8. Publication directive for the new QGE3 paper

The current Foundation Citation Directive on repository `main` is mandatory for this new manuscript.

Foundation DOI:

`https://doi.org/10.5281/zenodo.22164246`

Release gates:

1. Abstract/Аннотация must explicitly state that the paper works in the FCOA framework fixed by Definition 1.0 and must print the Foundation DOI.
2. Bibliography/Литература must contain the full Foundation bibliographic record with DOI `10.5281/zenodo.22164246`.
3. The body must contain a concrete FCOA-framework paragraph identifying active carrier, output/auxiliary sorts, primitive signature, baseline/change, erasure convention, recovery notion, and arithmetic firewall.
4. Already published archival Articles A/B are not rewritten merely to add this citation.

## 9. Claim firewall

Safe model-specific contribution:

\[
\boxed{
\text{sparse ternary anonymous equality}
\to
\text{equality-atom quotient}
\to
\text{proper-coloring transport}
\to
\text{sharp local-phase no-go}
\to
\text{conditional support-bijection groupoid}
\to
\text{exact permutation-graph gluing}.
}
\]

Do not claim invention of unique colorability, nonabelian switching, groupoids, permutation voltage assignments, or proper-coloring theory.

The six-cell non-vacuous minimum remains computational evidence until independently proved/audited.

## 10. Director decision

\[
\boxed{\text{UPSTREAM INSERTION APPROVED}}
\]

\[
\boxed{\text{SEPARATE QGE3 ARTICLE APPROVED FOR ASSEMBLY}}
\]

The next independent research target is the exact extremal synchronization problem `L_q(r)`; real operation-cell multicolor repair remains a later open layer.
