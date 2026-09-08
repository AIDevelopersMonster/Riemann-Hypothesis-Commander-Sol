# FCOA Rigidity Cost — Unsafe Optimal Beta Witness

**Status:** post-publication structural note.

## 1. Purpose

The stronger conjecture `alpha=beta` cannot be proved by the false claim that **every** minimum old-obstruction repair is automatically exact.

There are layers with `beta=alpha=1` for which one one-cell extension destroys all old bad automorphisms but creates a new bad automorphism, while another one-cell extension is exact.

Thus the correct theorem target is existential:

> among the minimum beta-repairs there exists at least one safe repair.

It is not a monotonicity theorem and not a local color-choice theorem.

## 2. Explicit six-carrier example

Let the carrier be

`G={0,1,2,3,4,5}`.

Take the old domain

\[
D=\{(0,3),(2,3),(5,3),(1,3),(1,4)\}.
\]

Use the binary coloring

\[
c(0,3)=0,
\quad c(2,3)=0,
\quad c(5,3)=1,
\quad c(1,3)=0,
\quad c(1,4)=0.
\]

The old ternary reduct has six carrier automorphisms; only two are globally anonymous-color compatible. Hence the old bad set is nonempty.

## 3. An unsafe beta witness

Add the single cell

\[
e=(5,4)
\]

with either binary value.

For **both** choices of the new value, every old bad automorphism is destroyed. Hence this extension witnesses

\[
\beta(D,c)=1.
\]

However the enlarged ternary reduct has four carrier automorphisms, only two of which are anonymous-color compatible. In particular a new bad symmetry appears which exchanges carrier points `1` and `5` (together with the required action on the remaining symmetric points).

Therefore the cell `(5,4)` is a minimum old-obstruction repair but is not an exact repair.

Changing only its binary value does not fix the problem.

## 4. Safe beta witnesses of the same size

Instead add either

\[
(0,2)
\]

or

\[
(0,5).
\]

For either binary value, the enlarged ternary reduct is carrier-rigid in this example. Thus

\[
\alpha(D,c)=1=\beta(D,c).
\]

So the layer has zero overhead, but safety depends on the **position** of the minimum repair cell, not merely on its cost or its color.

## 5. Consequence for the proof strategy

The following statements are false:

1. every beta-minimizing extension is exact;
2. if a beta-minimizing cell is unsafe, changing its binary value always makes it safe;
3. automorphism groups are monotone under extension.

The surviving conjectural statement is:

\[
\boxed{
\exists\text{ a beta-minimizing extension that is exact.}
}
\]

Equivalently,

\[
\boxed{\alpha=\beta.}
\]

Any proof must therefore use **global selection among minimum repairs**.

## 6. Orbit-selection formulation

For a beta-minimizing extension `(E,b)`, write

\[
X=(G;D\cup E,Q_{D\cup E}).
\]

Call the repair **safe** if every automorphism of `X` is anonymous-color compatible on the enlarged coloring.

A sufficient, but not necessary, condition is that every automorphism of `X` preserve the old domain `D` setwise. By the No-old-obstruction theorem, such an extension is exact.

Hence a proof of `alpha=beta` may be sought in the following form:

> among all beta-minimizing extensions, there exists one whose new-cell set is orbit-separated from the old domain under the automorphism group of the enlarged ternary reduct, or more generally one for which every domain-moving automorphism is already globally anonymous.

The explicit example above shows why one must optimize over the **whole family** of beta-minimizers rather than repair an arbitrary minimizer locally.

## 7. Current evidence

- exhaustive `|G|<=5`: `alpha=beta`;
- exhaustive `|G|=6, |D|<=8`: `alpha=beta`;
- targeted symmetry-generated and deletion-generated searches on larger small examples found unsafe beta witnesses but no positive overhead;
- the first unverified complete six-carrier layer remains `|D|=9`.

## Claim firewall

The example proves only that unsafe minimum beta-repairs exist. It does **not** disprove `alpha=beta`; in fact this example satisfies equality because safe one-cell repairs also exist.
