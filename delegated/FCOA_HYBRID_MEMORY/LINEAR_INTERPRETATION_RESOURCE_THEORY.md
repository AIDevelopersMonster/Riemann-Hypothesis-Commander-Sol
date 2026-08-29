# FCOA Hybrid Memory — Linear Interpretation Resource Theory

**Status:** new research strike; definitions and first theorem package  
**Context:** Article A is published (DOI 10.5281/zenodo.22165651). This file belongs to the post-Article-A resource-theory line.

## 1. Why unrestricted FO interpretation is too permissive

The RTP hostile audit showed that a dimension-2 interpretation can represent an `N`-point target by pairs over a `sqrt N`-point digit universe. Consequently, primitive coordinate resolution and defect exponents are not invariant under unrestricted FO interpretation.

The first restriction must therefore block polynomial tuple-power expansion while retaining ordinary definitional recoding and incidence compilation.

## 2. Linear FO interpretations

Let `A=(A_n)` and `B=(B_n)` be growing finite-structure families.

A uniform parameter-free FO interpretation `I:A -> B` is called **linearly size-faithful** if there exist constants

\[
0<c\le C<\infty
\]

such that for all sufficiently large `n`,

\[
c|A_n|\le |B_n|\le C|A_n|.
\tag{1}
\]

This blocks the specific `sqrt N -> N` digit expansion at the level of total structure size.

However, (1) alone is not enough: a dimension-2 interpretation over an `N`-point input may still use `N^2` candidate tuples and then select only `Theta(N)` of them by a formula. To control hidden tuple-space access we need a fiber condition.

## 3. Bounded-fiber dimension-1 interpretations

A **BF1 interpretation** is a uniform parameter-free FO interpretation satisfying:

1. interpretation dimension `1`;
2. the interpreted domain is a definable subset `D(A) subseteq A`;
3. the quotient equivalence relation has fibers of size at most a fixed constant `K`;
4. output size is linearly faithful:
   \[
   |I(A)|=Theta(|A|).
   \]

The quotient clause allows bounded duplication/collapse but forbids tuple-power coordinate generation.

For multi-sorted incidence encodings, one may equivalently allow a fixed finite disjoint union of dimension-1 definable sectors. This changes sizes only by constant factors.

## 4. Composition theorem

### Theorem HM-LIRT-COMP

BF1 interpretations are closed under composition.

### Proof

Let `I:A -> B` and `J:B -> C` be BF1, with fiber bounds `K_I,K_J`.

Both interpretations use individual source elements rather than tuples. Substituting the defining formulas of `I` into those of `J` therefore yields another dimension-1 FO interpretation from `A` to `C`.

An output element of `C` has at most `K_J` representatives in `B`; each such `B` representative has at most `K_I` representatives in `A`. Hence every composite quotient fiber has size at most

\[
K_IK_J.
\]

Linear size faithfulness composes:

\[
|B|=Theta(|A|),\qquad |C|=Theta(|B|)
\]

implies

\[
|C|=Theta(|A|).
\]

Thus the composite is BF1. `□`

This gives a genuine category/preorder in which resource invariants can be sought.

## 5. Immediate invariant: size exponent

For a family `A`, let `M(A_n)` be a chosen primitive record/cell measure. Define

\[
\mu(A)=\limsup_{n\to\infty}\frac{\log M(A_n)}{\log |A_n|}.
\]

Raw `mu` is not invariant under arbitrary definitional expansion because one source relation can be replaced by many derived records. We therefore need to quotient by BF1-equivalent presentations.

Define the **BF1-minimized cell exponent**

\[
\mu_{BF1}(A)
=
\inf\{\mu(B): A\le_{BF1} B\text{ and }B\le_{BF1} A\}.
\tag{2}
\]

By construction this is invariant under BF1 bi-interpretability.

This definition is mathematically correct but may be too coarse: all known AL0–AL2 constructions still have exponent `1`, so it does not yet separate them.

## 6. Semantic phase remains monotone

FO Transport Rank remains monotone because every BF1 interpretation is an FO interpretation:

\[
A\le_{BF1}B\Longrightarrow FTR(A)\le FTR(B).
\]

Hence the pair

\[
\boxed{(FTR,\mu_{BF1})}
\]

is stable under the restricted category, but currently gives

\[
(AL0,1),\quad(AL1,1),\quad(AL2,1).
\]

So merely banning tuple-power expansion does **not yet** recover a cell-exponent hierarchy.

## 7. First no-go inside BF1

The existing linear AL2 digit structure itself can be built with total universe `Theta(N)`:

- `N` target points;
- `Theta(sqrt N)` digit points;
- `Theta(N)` table-entry points for digit addition/multiplication;
- `Theta(N)` incidence records after compilation.

Thus its total carrier size and total record size are both `Theta(N)`.

Consequently, forbidding dimension-2 interpretation does not by itself force AL2 above linear cost: one can materialize the digit tuples/table entries as explicit auxiliary carrier points.

Therefore:

\[
\boxed{\text{BF1 alone does not create a superlinear AL2 wall.}}
\]

This is an important negative result: the missing resource is not only interpretation dimension.

## 8. What resource was hidden?

The digit construction uses `Theta(N)` auxiliary records to materialize a complete local arithmetic table on a `sqrt N` digit sort.

The crucial structural feature is **precomputed local-law entropy**: a small coordinate sort is equipped with a dense `b^2` lookup table, and the table itself already costs exactly `Theta(N)`.

Because the global budget is also `Theta(N)`, this remains legal.

Thus any hierarchy based only on total linear size will continue to collapse as long as arbitrary `Theta(N)` auxiliary lookup memory is allowed.

## 9. Candidate next restriction: sublinear auxiliary law memory

Separate the structure into:

- target sector `X_N`, size `N`;
- coordinate/auxiliary carrier `Y_N`;
- **law-memory records** `L_N` whose sole role is to encode lookup laws on auxiliary coordinates;
- target-to-coordinate incidence records.

Define the law-memory exponent

\[
\lambda
=
\limsup_{N\to\infty}\frac{\log |L_N|}{\log N}.
\]

The current sparse AL0 threshold scaffold uses `Theta(N)` comparison-threshold law/incidence memory if represented explicitly, so naive `lambda<1` would also kill our known AL0 realization. The distinction must therefore be more semantic than simply counting auxiliary records.

A better candidate is to distinguish:

1. **coordinate attachment memory** — records incident with target points;
2. **coordinate-internal law memory** — records entirely inside auxiliary sectors.

The digit AL2 construction has

\[
\Theta(N)
\]

coordinate-internal arithmetic law memory.

The next question is whether exact AL0 or AL1 can be achieved with asymptotically less internal-law memory while retaining total `Theta(N)` target attachments.

## 10. New resource vector

For a presentation with target sector `X_N`, define

\[
R(A_N)=(M_{tot},M_{int},D_{int},q,I),
\]

where

- `M_tot` = total primitive records;
- `M_int` = records with no target-sector endpoint;
- `D_int` = maximum Gaifman degree inside the auxiliary induced structure;
- `q` = quantifier rank of the uniform recovery interpretation;
- `I` = interpretation dimension.

The previous work already shows that `M_tot` alone collapses. The present strike shows that `I=1` alone also collapses after explicit materialization.

The promising coordinate is now

\[
\boxed{M_{int}},
\]

or a normalized version invariant under bounded incidence compilation.

## 11. Current phase diagnosis

The sequence of failed scalar invariants is now:

\[
\text{cell exponent}
\to
\text{max degree}
\to
\text{channel count}
\to
\text{resolution exponent}
\to
\text{interpretation dimension alone}.
\]

Each failure has exposed a new compression mechanism.

The surviving research hypothesis is:

\[
\boxed{
\text{arithmetic strength may be paid for in target-independent internal law memory.}
}
\]

This is sharper than the earlier CRT-channel hypothesis because it survives explicit materialization of tuple coordinates.

## 12. Next strike

Determine the minimum possible internal-law memory for uniform recovery of:

\[
<,\qquad +_{tr},\qquad \times_{tr}
\]

under:

- fixed finite bounded-arity signature;
- total primitive records `Theta(N)`;
- BF1 recovery;
- target sector of size `N`;
- bounded-size incidence compilation treated as cost-equivalent.

The first concrete target is:

\[
\boxed{
\text{Can AL0 be realized with }M_{int}=o(N)\text{ while AL2 requires }M_{int}=\Omega(N)?
}
\]

If yes, this is the first genuine resource separation surviving the previous collapse mechanisms. If no, the counterconstruction will identify the next hidden resource.