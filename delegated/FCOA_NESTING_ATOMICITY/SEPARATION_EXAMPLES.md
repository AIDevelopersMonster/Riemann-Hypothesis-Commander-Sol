# FCOA Nesting & Atomicity — Separation Examples

These are finite sandbox witnesses. No ordinary divisibility is imported unless explicitly stated in the classical comparison file.

## Example A — Same carrier, different sandbox, different atomicity

Let

\[
X=\{u,a,b,c\},\qquad U=\{u\},
\]

all elements active.

Sandbox `S0` has no defined nontrivial-result cells. Then `c` is indecomposable and therefore U-atomic.

Sandbox `S1` has the single cell

\[
a\star b=c.
\]

with `a,b notin U`. Then `c` is composite and not U-atomic.

The carrier and `U` are unchanged; only the admitted composition family changed. This is the smallest basic witness of sandbox-relative atomicity.

## Example B — Indecomposable need not be isolated

Let

\[
X=\{u,a,t\},\qquad U=\{u\},
\]

with active sort `A={u,a}` and terminal sort `T={t}`. Define

\[
a\star a=t.
\]

No cell has result `a`, so `a` is indecomposable. But `a` is not isolated because it occurs as an argument.

Thus

\[
\text{isolated}\not\Leftarrow\text{indecomposable}.
\]

## Example C — Atomic need not be indecomposable

Let

\[
X=\{u,a,x\},\qquad U=\{u\},
\]

and define only

\[
u\star a=x.
\]

Then `x` has a decomposition witness, so it is not indecomposable. But every witness has a trivial left factor, hence no two-sided nontrivial witness exists. Therefore `x` is U-atomic.

Thus

\[
\text{indecomposable}\not\Leftarrow U\text{-atomic}.
\]

## Example D — Left- and right-atomicity can diverge

Let

\[
X=\{u,a,x\},\qquad U=\{u\},
\]

and define only

\[
a\star u=x.
\]

Then `x` has a left-nontrivial witness but no right-nontrivial witness. Hence `x` is right-U-atomic but not left-U-atomic.

Replacing the cell by `u star a=x` reverses the conclusion.

No commutativity assumption may therefore be smuggled into directional atomicity.

## Example E — U-atom need not be U-irreducible

Let

\[
X=\{u,a,x\},\qquad U=\{u\},
\]

and define only

\[
u\star a=x.
\]

Assume there is no trivial-factor transport path from `x` back to `a`, and no path from `a` to `x` except the displayed one. Then `a` and `x` are not U-associated.

The result `x` is U-atomic because it has no two-sided nontrivial decomposition, but its only decomposition is not U-inessential. Hence `x` is not U-irreducible.

This separates a mere declaration of `U` from genuine unit-like behavior.

## Example F — Minimal nesting class without atoms

Let

\[
X=\{u,a,b\},\qquad U=\{u\},
\]

and define

\[
a\star a=b,
\qquad
b\star b=a.
\]

Both cells are two-sided nontrivial. The nontrivial factor graph has the directed cycle

\[
a\to b\to a.
\]

The strongly connected class `{a,b}` is minimal in the condensation poset because there is no incoming edge from outside. Yet neither `a` nor `b` is U-atomic.

This is the minimal cycle obstruction to identifying atoms with globally minimal nesting points.

## Example G — Value recoloring changes rigidity but not active atomicity

Let active carrier be

\[
A=\{u,a,b\},\qquad U=\{u\},
\]

and terminal outputs `T={t_+,t_-}`. Keep the same active-result cells in two sandboxes and add only terminal-result cells

\[
a\star b=t_+,
\qquad
b\star a=t_-.
\]

In a second sandbox recolor both terminal cells to a single anonymous terminal value `t`.

The active-result decomposition sets are identical in both sandboxes. Hence their atom classes inside `A` coincide, even though the value-fiber partition and possibly the automorphism group differ.

This is the atomicity analogue of the FCOA domain/value split: terminal value geometry can carry rigidity information without changing active-result composition boundary.

## Example H — Coarse translation counts do not determine atom classes

Consider two sandboxes on

\[
X=\{a,b,c,d\},\qquad U=\varnothing.
\]

In `S1`, define

\[
a\star b=c,
\qquad
c\star d=a.
\]

In `S2`, define

\[
a\star b=c,
\qquad
c\star d=b.
\]

Both have exactly two defined cells, the same multiset of left-domain sizes, and the same multiset of right-domain sizes. Yet their result-incidence patterns differ, and therefore their atom sets differ after relabeling is fixed.

Hence unlabeled translation-cardinality summaries are insufficient; one needs labeled profiles or the operation graph to recover nesting.

## Example I — Terminal outputs are not factors by default

Let

\[
A=\{a,b\},\qquad T=\{t\},\qquad U=\varnothing,
\]

with only

\[
a\star b=t.
\]

No operation accepts `t` as an argument. Therefore `t` cannot be used as a factor in any deeper nesting expression. Treating it as an active factor would fabricate decompositions absent from the signature.

This is why active/terminal typing is part of every branch passport.

## Example J — Pure carrier erasure preserves atomicity

Take any finite sandbox and add an external linear order on its carrier labels. Erase only that order while keeping every operation cell, value, sort, and `U` unchanged.

All decomposition witness sets are identical before and after erasure. Therefore all U-atomic classes are identical, even if the automorphism group grows sharply.

This separates external distinguishability from composition-boundary structure.