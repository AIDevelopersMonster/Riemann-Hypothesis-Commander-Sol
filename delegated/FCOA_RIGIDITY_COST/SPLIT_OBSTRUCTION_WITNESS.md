# FCOA Rigidity Cost — Genuine Split-Color Obstruction Witness

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication counterexample to the local Split Exclusion strategy.

## 1. Purpose

`PERSISTENT_EXCLUSION_THEOREM.md` proves that an anchored beta-killing singleton cell cannot have one and the same bad replacement symmetry for both binary colors.

It was natural to ask whether the remaining Type-S mechanism could also be excluded locally.

The answer is **no**.

There exist anchored beta-killing cells for which color 0 is spoiled by one defect-one replacement symmetry and color 1 by a different replacement symmetry, while no bad symmetry is common to both colors.

Thus the statement

\[
\text{“every anchored beta-killing cell has a safe color”}
\]

is false.

The global conjecture `beta=1 => alpha=1` survives because the same old layer has many other beta-killing cells that are exact.

## 2. Explicit six-carrier witness

Let

\[
G=\{0,1,2,3,4,5\}.
\]

Take

\[
D=\{(0,4),(1,3),(2,5),(3,1)\}
\]

with coloring

\[
c(0,4)=0,\qquad
c(1,3)=0,\qquad
c(2,5)=1,\qquad
c(3,1)=0.
\]

The old ternary reduct is nonexact. It has four reduct automorphisms, two of which are old bad automorphisms.

Now add

\[
\boxed{e=(5,2)}.
\]

The new cell is anchored because it is composable with the old cell `(2,5)`.

Moreover, the singleton extension by `e` destroys every old bad automorphism, so `e` is a genuine beta-killing cell.

## 3. Color 0 obstruction

Give the new cell color

\[
b=0.
\]

Then the enlarged reduct has bad domain-moving automorphisms including

\[
h_0=(0,1,5,3,4,2)
\]

in one-line notation.

It satisfies

\[
h_0(e)=(2,5),
\]

and

\[
h_0(D)=D-\{(2,5)\}+\{e\}.
\]

Thus `h_0` is a defect-one replacement symmetry.

For color 0 it is a bad ternary-reduct automorphism.

## 4. Color 1 obstruction

Give the same new cell color

\[
b=1.
\]

Then a different bad replacement symmetry exists, for example

\[
h_1=(0,2,1,5,4,3).
\]

It satisfies

\[
h_1(e)=(3,1),
\]

and

\[
h_1(D)=D-\{(3,1)\}+\{e\}.
\]

Thus `h_1` is another defect-one replacement symmetry, supported on a different deletion of the old domain.

For color 1 it is bad.

## 5. Genuine split character

Direct enumeration gives

\[
B_0\ne\varnothing,
\qquad
B_1\ne\varnothing,
\]

but

\[
\boxed{B_0\cap B_1=\varnothing.}
\]

Hence the obstruction is exactly Type S from `BETA_ONE_FATAL_GEOMETRY_CLASSIFICATION.md`:

\[
\boxed{
\mathcal B_{h_0}(\{e\})=\{0\},
\qquad
\mathcal B_{h_1}(\{e\})=\{1\}
}
\]

for suitable replacement representatives.

This is consistent with Persistent Exclusion and proves that Split Exclusion is false as a local theorem.

## 6. The old layer still has alpha=beta=1

The failure is local to the chosen geometry `e=(5,2)`.

The same old layer has many other beta-killing cells which are exact for both colors. Examples include

\[
(0,1),\ (0,2),\ (0,3),\ (1,0),\ (1,2),\ (2,0),\ (3,0),\ (4,1),\ (5,3),
\]

among many others.

For example, adding

\[
(0,1)
\]

with either binary value yields an exact singleton extension.

Therefore

\[
\boxed{\beta(D,c)=\alpha(D,c)=1.}
\]

The witness does not challenge the global Safe-Minimizer conjecture.

## 7. Consequence for the proof architecture

The following increasingly strong local statements are now known to be false:

1. every beta-minimal repair is safe;
2. changing only the color of an unsafe beta-minimal cell always makes it safe;
3. every anchored beta-killing cell has a safe color.

What survives is genuinely global:

\[
\boxed{
\beta=1
\Longrightarrow ?
\exists\text{ some beta-killing cell and some color giving exactness.}
}
\]

Thus the proof must optimize over the **set of beta-killing cells**, not only over the two colors of a fixed geometry.

## 8. New escape-selection target

Let

\[
W_{kill}(D,c)
\]

be all beta-killing singleton cells and define

\[
W_{fatal}(D,c)
\subseteq
W_{kill}(D,c)
\]

as those cells for which both binary colors are nonexact.

The witness shows

\[
W_{fatal}\ne\varnothing
\]

is possible.

The global beta-one theorem is equivalent to

\[
\boxed{
\beta=1
\Longrightarrow
W_{kill}\setminus W_{fatal}\ne\varnothing.
}
\]

A counterexample must therefore satisfy the much stronger **total fatal saturation** condition

\[
\boxed{
W_{kill}=W_{fatal}.
}
\]

This replaces the now-false local Split Exclusion target.

## 9. Structural clue from the witness

In the explicit split cell `e=(5,2)`, the two colors are defeated by replacement symmetries corresponding to two **different old deletions**:

\[
(2,5)
\quad\text{and}\quad
(3,1).
\]

At the same time, the old domain leaves a large complement of cells whose singleton addition destroys the same old bad symmetries without completing either dangerous deletion orbit.

This suggests that the true global theorem should compare:

- the set of all beta-killing cells;
- the union of color-specific defect-one replacement completion sets.

A total-fatal counterexample would require those replacement completions to cover **every** beta-killing cell.

## 10. Next theorem target

The next target is no longer Split Exclusion.

It is the **Total Fatal Saturation Exclusion Problem**:

> Can a sparse binary layer with `beta=1` satisfy
> \[
> W_{kill}(D,c)=W_{fatal}(D,c)?
> \]

Equivalently: can every one-cell geometry that kills all old bad automorphisms be trapped by either split replacement symmetries or the isolated phase mechanism?

A proof that total fatal saturation is impossible would establish

\[
\boxed{\beta=1\Longrightarrow\alpha=1.}
\]

## Claim firewall

1. The witness disproves only the local Split Exclusion strategy.
2. It is not a counterexample to `alpha=beta`; this layer has `alpha=beta=1`.
3. No minimality in carrier size is claimed yet for the split witness.
4. The explicit automorphisms above were independently checked by direct exhaustive carrier-permutation enumeration.
