# H18 · M1(W4) closure

Branch: \`research/hatter-sol-18-m1-closure\`

Status: **ACTIVE POST-FREEZE CLOSURE**

The frozen H18 publication remains unchanged.

## C1 · certified robust9 witness versus adaptive contract — CLOSED NEGATIVE

The H18-10 minimum distance-two alphabet witness

\[
\{a,b,Ba,ab,BBa,aab,aaab,ABab,AbaB\}
\]

was tested against the full H18-06 adaptive programme using exactly the same
terminal semantics and persistent-known-query-erasure recursion.

GitHub Actions run:

\[
\boxed{\texttt{35487038248}}
\]

returned

\[
\begin{aligned}
D_0\le3 &: \mathrm{False},\\
D_0\le4 &: \mathrm{False},\\
S_1\le3 &: \mathrm{False},\\
S_1\le4 &: \mathrm{False}.
\end{aligned}
\]

Therefore this particular minimum distance-two alphabet is **not** an adaptive
depth-four alphabet.

No stronger lower bound follows:

\[
\boxed{9\le M_1(W_4)\le12}
\]

remains the exact certified bracket.

## Structural lesson

Distance-two separation is necessary for one-erasure recovery but is not
sufficient for the depth-constrained adaptive contract.

Thus the closure problem is not a pure error-correcting-code/set-cover problem:

\[
\boxed{
\text{pairwise robust separation}
\not\Rightarrow
\text{adaptive depth-four realizability}.
}
\]

This distinction is relevant to H19 because it is another example of two
different complexity structures living on the same observer family.

## C2 · global size-9 search — NEXT

Both oriented commutator labels \`ABab\` and \`AbaB\` are forced by the seven
critical pairs.

A size-9 candidate therefore has the form

\[
\{ABab,AbaB\}\cup S,\qquad |S|=7,\quad S\subseteq48\text{ remaining labels}.
\]

A raw search would inspect

\[
\binom{48}{7}=73,629,072
\]

subsets and is not the desired implementation.

The exact search will instead combine:

1. branch-and-bound on the remaining pairwise distance-two constraints;
2. incremental bitset coverage for 0/1/2-hit pair state;
3. feasibility bounds from the maximum cover obtainable by remaining slots;
4. symmetry/canonical ordering of labels;
5. adaptive-depth testing only for surviving distance-two alphabets;
6. memoization of adaptive subproblems by
   \((\text{state mask},\text{remaining depth},\text{banned query},\text{alphabet})\).

If no size-9 adaptive alphabet exists, repeat at sizes 10 then 11.

The first successful size \(k\), combined with exhaustive failure below \(k\),
will close \(M_1(W_4)=k\).
