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

The carrier and `U` are unchanged; only the admitted composition family changed.

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

## Example C — Atomic need not be indecomposable

Let

\[
X=\{u,a,x\},\qquad U=\{u\},
\]

and define only

\[
u\star a=x.
\]

Then `x` has a decomposition witness but no two-sided nontrivial witness. Hence `x` is U-atomic but not indecomposable.

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

## Example E — U-atom need not satisfy transport irreducibility without U-coherence

Let

\[
X=\{u,a,x\},\qquad U=\{u\},
\]

and define only

\[
u\star a=x.
\]

Assume there is no trivial-factor transport path from `x` back to `a`. Then `a` and `x` are not U-associated.

The result `x` is U-atomic because it has no two-sided nontrivial decomposition, but its only decomposition is not U-transport-inessential. Hence `x` is not U-transport-irreducible.

This is why unqualified `U`-irreducibility requires the U-coherence contract.

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

The factor graph has the directed cycle

\[
a\to b\to a.
\]

The SCC `{a,b}` is minimal, yet neither element is atomic.

## Example F2 — Cycles above the boundary are harmless

Let

\[
X=\{u,a,b,c\},\qquad U=\{u\},
\]

and define

\[
a\star a=b,
\qquad
b\star b=c,
\qquad
c\star c=b.
\]

The factor graph contains

\[
a\to b,
\qquad
b\leftrightarrows c.
\]

The graph is cyclic, but its unique minimal SCC is the edge-free singleton `{a}`. Therefore

\[
\operatorname{Atom}=\operatorname{MinNest}=\{a\}.
\]

This disproves any claim that global acyclicity is necessary for atom/minimal equality.

## Example G — Value recoloring changes rigidity but not active atomicity

Let active carrier be

\[
A=\{u,a,b\},\qquad U=\{u\},
\]

and terminal outputs `T={t_+,t_-}`. Add only

\[
a\star b=t_+,
\qquad
b\star a=t_-.
\]

In a second sandbox recolor both terminal cells to a single anonymous terminal value `t`.

The active-result decomposition sets are identical. Hence the active atom classes coincide even though value-fiber geometry can differ.

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

Both have two defined cells and the same multisets of left- and right-domain sizes, but their result-incidence patterns differ. Coarse translation counts therefore do not determine atom classes.

## Example I — Terminal outputs are not factors by default

Let

\[
A=\{a,b\},\qquad T=\{t\},\qquad U=\varnothing,
\]

with only

\[
a\star b=t.
\]

No operation accepts `t` as an argument. Therefore `t` cannot be used as a factor in any deeper nesting expression.

## Example I2 — A terminal-labelled element must enter the factor graph once legally activated

Let

\[
X=\{a,t,x\},\qquad U=\varnothing,
\]

where `t` was historically a terminal output, but the current signature explicitly contains

\[
t\star a=x.
\]

Then `t` is a legal nontrivial factor of `x`. Omitting `t` from the factor-graph universe would incorrectly classify `x` as atomic.

Hence the repaired graph uses `X\U`, while target-sort declarations only determine where atomhood is reported.

## Example J — Pure carrier erasure preserves atomicity

Take any finite sandbox and add an external linear order on its carrier labels. Erase only that order while keeping every operation cell, value, sort, and `U` unchanged.

All operation incidences and decomposition witnesses are identical. Therefore isolation and every atomicity notion are preserved, even if the automorphism group grows sharply.

## Example K — Quotient destroys an atom by result-fiber contamination

Let

\[
X=\{u,a,b,x,y\},\qquad U=\{u\},
\]

with the single nontrivial cell

\[
a\star b=y.
\]

Then `x` is atomic and `y` is composite. Form a quotient identifying

\[
x\sim y
\]

and leaving all other points separate.

The quotient is triviality-reflecting because the `U`-fiber is unchanged. Nevertheless

\[
[x]=[y]
\]

is composite because the witness for `y` descends.

Thus an atomic representative can be destroyed solely by merging its result fiber with a composite representative.

## Example L — Quotient creates an atom by triviality collapse

Let

\[
X=\{u,a,b,x\},\qquad U=\{u\},
\]

with

\[
a\star b=x,
\qquad
u\star b=x.
\]

Then `x` is non-atomic because `a,b notin U` and `a star b=x`.

Identify

\[
a\sim u.
\]

The quotient cell becomes

\[
[u]\star[b]=[x].
\]

Since `[u]` is trivial, the quotient result `[x]` has no two-sided nontrivial witness and is atomic.

This quotient fails triviality reflection:

\[
q^{-1}(\bar U)\supsetneq U.
\]

Hence quotienting can manufacture atoms when nontrivial factors collapse into the trivial class.

## Example M — Ordinary quotient destroys well-foundedness

Let `U=emptyset` and define

\[
a\star b=c,
\qquad
c\star b=d.
\]

The original factor graph is acyclic. Identify

\[
c\sim d.
\]

Then in the ordinary existential quotient

\[
[c]\star[b]=[c],
\]

so the quotient factor graph has a self-loop.

Thus ordinary congruence quotienting need not preserve acyclicity, well-foundedness, or ordinal factor rank.

## Example N — Self-loop is the one-point minimal-SCC obstruction

Let `U=emptyset` and define only

\[
a\star a=a.
\]

The unique SCC `{a}` is minimal, but it carries an internal self-loop. Hence `a` is nesting-minimal and non-atomic.

This shows why the exact criterion is not merely "minimal SCCs are singletons" but "minimal SCCs are edge-free singletons".