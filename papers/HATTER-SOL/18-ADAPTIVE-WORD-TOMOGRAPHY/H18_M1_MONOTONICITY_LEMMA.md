# H18 M1 closure · Alphabet monotonicity lemma

Status: **EXACT ELEMENTARY LEMMA**

## Setting

Fix the H18-06 finite state space, terminal semantics, successful-answer budget
\(s\), and the fault model of at most one persistent known query erasure.

For a supported query alphabet \(A\subseteq W_4\), write

\[
\operatorname{Feas}(A,s)
\]

when there exists an adaptive strategy using only labels from \(A\) that solves
the identify-or-REJECT task with at most \(s\) successful answers under the
declared one-erasure model.

## Lemma

If

\[
A\subseteq B\subseteq W_4
\]

and

\[
\operatorname{Feas}(A,s),
\]

then

\[
\boxed{\operatorname{Feas}(B,s)}.
\]

### Proof

Take a correct strategy for \(A\).  Regard it as a strategy over \(B\) that
never chooses any label in \(B\setminus A\).

If the erased query identity lies in \(A\), behavior is exactly the already
certified \(A\)-strategy under its allowed persistent known erasure.

If the erased identity lies in \(B\setminus A\), the strategy never attempts
that query, so the erasure has no effect on any branch.

Thus every input/fault case admitted for alphabet \(B\) is solved with the same
successful-answer bound \(s\). \(\square\)

## Corollary — upward closure by cardinality

If any alphabet of size \(k<50\) is feasible, then a feasible alphabet exists
at every size

\[
k,k+1,\ldots,50,
\]

by adjoining arbitrary unused query labels.

Equivalently, if **no** alphabet of size \(m\) is feasible, then no alphabet of
any smaller size can be feasible.

## H18 closure consequence

H18-11 supplies a feasible alphabet of size 12.

Therefore an exhaustive proof that no size-11 alphabet is feasible immediately
gives

\[
\boxed{M_1(W_4)=12}.
\]

No independent size-10 exclusion is logically required once size 11 is
globally excluded, although a size-10 search remains useful as an independent
cross-check.
