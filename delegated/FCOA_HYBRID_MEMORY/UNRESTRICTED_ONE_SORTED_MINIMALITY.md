# FCOA Hybrid Memory — Unrestricted One-Sorted Minimality

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** new theorem candidate; exhaustive small-case classification completed; hostile audit still required  
**Scope:** one-sorted binary partial operations with no external active/output typing and with operation values allowed to be elements of the same universe.

## 1. Why the previous three-cell bound fails here

The previous three-cell lower bound treated values as a coloring of a tagged set of operation cells into a separate terminal-output sort. In a one-sorted structure, an operation value is itself an element of the carrier. Restoring a value can therefore distinguish a carrier element even when the equality partition of operation cells is trivial.

Thus one-sorted value memory is strictly stronger than pure fiber coloring.

## 2. Absolute two-cell VV witness

Let

\[
U=\{a,u,v,w\}.
\]

Define exactly one cell for each operation:

\[
\boxed{a\oplus a=u,}
\]

\[
\boxed{a\otimes a=v.}
\]

Every other cell of both operations is undefined.

No element is named. No sort distinguishes arguments from values.

## 3. Exact automorphism groups

### The `\oplus` reduct

The unique defined cell forces `a` and `u` to be fixed. The remaining points `v,w` may be swapped. Hence

\[
\boxed{\operatorname{Aut}(U,\oplus)\cong C_2.}
\]

### The `\otimes` reduct

Similarly, `a` and `v` are fixed while `u,w` may be swapped:

\[
\boxed{\operatorname{Aut}(U,\otimes)\cong C_2.}
\]

### Joint valued structure

Together the two equations fix `a`, `u`, and `v`; the final point `w` is then fixed automatically. Thus

\[
\boxed{\operatorname{Aut}(U,\oplus,\otimes)=1.}
\]

Therefore this is a balanced hybrid witness using exactly two total defined cells.

## 4. Why this is genuinely value-value

The two operation domains are identical:

\[
D_\oplus=D_\otimes=\{(a,a)\}.
\]

Hence the joint definedness reduct only distinguishes `a`; it leaves the other three points completely symmetric:

\[
\boxed{
\operatorname{Aut}(U,D_\oplus,D_\otimes)
\cong S_{\{u,v,w\}}
\cong S_3.
}
\]

If the `\oplus` value is restored but the `\otimes` value is erased, then `a,u` are fixed and `v,w` may still be swapped:

\[
\boxed{
\operatorname{Aut}(U,\oplus,D_\otimes)
\cong C_2.
}
\]

If the `\otimes` value is restored but the `\oplus` value is erased, then `a,v` are fixed and `u,w` may still be swapped:

\[
\boxed{
\operatorname{Aut}(U,D_\oplus,\otimes)
\cong C_2.
}
\]

Only when both value layers are present is the structure rigid:

\[
\boxed{
S_3\longrightarrow C_2\longrightarrow1.
}
\]

Moreover, **erasing either value layer destroys rigidity**. Thus the witness is genuinely VV in the strongest erasure sense used in this branch.

## 5. Absolute cell minimality

### Theorem HM-OS2

In the unrestricted one-sorted setting, the minimum total number of defined cells in a balanced hybrid-rigidity witness is exactly two.

### Proof

Zero cells give the full symmetric group.

With exactly one defined cell in total, one operation is empty. The joint structure is then exactly the nonempty reduct together with an empty spectator symbol. If the nonempty reduct is nonrigid, as required by balanced hybrid memory, then the joint structure is also nonrigid. Hence one total cell cannot suffice.

The two-cell construction above is balanced and jointly rigid. Therefore the lower bound is sharp. `□`

Thus

\[
\boxed{
\text{absolute one-sorted hybrid cell minimum}=2.
}
\]

This equals the pure DD cell minimum, but unlike DD the displayed witness is genuinely value-value.

## 6. Minimum universe size for two-cell VV

The displayed construction uses four elements. Exhaustive enumeration of all two-operation, one-cell-per-operation binary partial structures on universes of size `2` and `3` found no witness satisfying all of:

1. each valued reduct is nonrigid;
2. the joint definedness reduct is nonrigid;
3. the fully valued joint structure is rigid;
4. erasing either operation's values restores nontrivial symmetry.

On four elements such witnesses exist.

Hence, for binary one-cell-per-operation VV witnesses,

\[
\boxed{|U|=4}
\]

is the smallest carrier size.

This finite enumeration result should still receive an independent hostile check before promotion as a theorem beyond the explicitly searched binary setting.

## 7. Complete four-point classification

On `|U|=4`, enumerate all ordered pairs of one-cell binary partial operations

\[
x_0\oplus y_0=z_0,
\qquad
x_1\otimes y_1=z_1.
\]

Impose the four VV conditions above.

The exhaustive search returns exactly

\[
\boxed{24\text{ labeled witnesses}.}
\]

Under the natural action of `S_4` on the universe, all 24 lie in a single orbit:

\[
\boxed{1\text{ isomorphism class}.}
\]

A canonical representative is precisely

\[
a\oplus a=u,
\qquad
a\otimes a=v,
\]

with fourth point `w` unused.

Therefore the absolute two-cell VV threshold has a unique four-point geometry up to relabeling, with the operation symbols kept distinguished.

## 8. Structural interpretation

This witness is **not** JFS in the earlier tagged-fiber sense. The two output values are different and there is no cross-operation equality constraint.

The mechanism is instead:

\[
\boxed{
\text{shared carrier role memory}
}
\]

or, more explicitly,

\[
\boxed{
\text{each operation value individually pins one point of the same residual carrier orbit.}
}
\]

Definedness fixes `a` and leaves the residual orbit

\[
\{u,v,w\}.
\]

The `\oplus` value selects `u` from that orbit. The `\otimes` value independently selects `v`. Their intersection leaves only `w`.

Thus the two value layers act as transverse point selectors inside a common definedness orbit.

This suggests separating at least two one-sorted VV mechanisms:

1. **fiber synchronization** — cross-operation equality/lift compatibility;
2. **carrier-value selection** — values are themselves carrier points and independently break a common carrier orbit.

## 9. Relation to the typed theorem

The typed Lift-Compatibility theorem remains correct in its own setup. What fails is only the attempt to interpret it as an absolute lower-bound theorem for unrestricted one-sorted FCOA.

In a separated output sort, values affect automorphisms only through the partition of operation cells into equal-value fibers. In a one-sorted structure, values additionally carry unary positional information because the value element is itself moved by carrier automorphisms.

Hence

\[
\boxed{
\text{one-sorted value memory}
=
\text{fiber information}
+
\text{carrier-role information of outputs}.
}
\]

## 10. Arithmetic Leakage firewall

The absolute minimum witness is far below AL0. It consists of two loops at one point with two distinct values. There is no order, orientation, successor, betweenness, EqGap, addition, multiplication, or external index calculation.

Thus

\[
\boxed{
\text{Arithmetic Leakage: NONE / below AL0.}
}
\]

## 11. Revised minimality hierarchy

The branch must now distinguish semantics explicitly:

\[
\boxed{
\begin{array}{c|c}
\text{regime} & \text{sharp total cell threshold}\\
\hline
\text{pure DD} & 2\\
\text{unrestricted one-sorted genuine VV} & 2\\
\text{typed/common-terminal JFS} & 3\\
\text{typed independent-output DV} & 4\\
\text{typed independent-output VV} & 6
\end{array}
}
\]

These are different resource questions, not competing answers to one identical formal problem.

## 12. Current status

The unrestricted one-sorted attack overturned the previous conjectural absolute three-cell value bound and replaced it with a sharper result:

\[
\boxed{
\text{two cells are already enough for genuine value-value hybrid rigidity.}
}
\]

The four-point realization is unique up to relabeling in the exhaustive binary one-cell-per-operation search.

This is now the preferred minimal one-sorted witness for the branch. JFS-3 remains important as the minimal **shared-terminal-fiber synchronization** witness, not as the absolute value minimum.
