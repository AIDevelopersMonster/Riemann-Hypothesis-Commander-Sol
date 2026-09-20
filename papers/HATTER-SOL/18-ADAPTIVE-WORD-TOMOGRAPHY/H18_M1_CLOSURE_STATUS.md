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


## C2a · exact constraint profile — CLOSED

The forced oriented commutator pair already covers some required state pairs
twice.  Exactly

\[
\boxed{3556}
\]

required pairs remain with zero forced hits and therefore need two hits from
the remaining 48 labels.

The number of available distinguishing labels per remaining pair ranges from

\[
\boxed{14\text{ to }48}.
\]

The exact minimum occurs for two constraints.

Coverer-count histogram:

\[
\begin{array}{c|rrrrrrrrr}
\#\text{coverers}&14&16&18&20&22&24&26&28&30\\
\#\text{pairs}&2&24&22&34&42&34&20&116&142
\end{array}
\]

\[
\begin{array}{c|rrrrrrrrr}
\#\text{coverers}&32&34&36&38&40&42&44&46&48\\
\#\text{pairs}&200&424&308&432&528&548&400&228&52.
\end{array}
\]

This explains why simple forced propagation alone is weak: even the most
constrained pair still offers 14 candidate labels.

No new bound on \(M_1(W_4)\) is inferred from this profile alone.


## C3 · query partition quotient — CLOSED STRUCTURAL LAYER

The 50 canonical \(W_4\) queries form exactly 25 equality-partition types on
the full 197-state H18 quotient:

\[
\boxed{50=25\times2}.
\]

Every type has multiplicity exactly two.  The pairs include

\[
(A,a),\quad(B,b),\quad(AB,ab),\quad\ldots,
\]

and the forced oriented commutators are one type:

\[
\boxed{(ABab,AbaB)}.
\]

Members of one type induce exactly the same partition of the 197 states; their
used response labels differ only by a bijective relabelling.

Therefore adaptive feasibility is invariant under replacing one query by its
partner, while the multiplicity \(0/1/2\) of a type must still be retained
because persistent erasure acts on query identity.

GitHub Actions run:

\[
\boxed{\texttt{35488360846}}.
\]

## C4 · exact size-9 quotient search — CLOSED NEGATIVE

The size-9 problem was quotiented exactly by the 25 partition types.

The forced commutator type contributes both of its identities.  The remaining
seven query identities were represented by multiplicities

\[
x_t\in\{0,1,2\}
\]

over the other 24 types.

After quotienting the 3,556 raw remaining pair constraints, only

\[
\boxed{882}
\]

distinct distance constraints remain.

The exact DFS visited

\[
\boxed{332254}
\]

states and found

\[
\boxed{2816}
\]

complete size-9 distance-two multiplicity vectors.

Every one was tested by the exact H18-06 adaptive dynamic programme.

Result:

\[
\boxed{
\#\{A:|A|=9,\ D_0(A)\le4\}=0.
}
\]

Hence no size-9 alphabet can satisfy the full one-erasure H18 contract.

Therefore the certified global bound is now

\[
\boxed{
10\le M_1(W_4)\le12.
}
\]

This is strictly stronger than H18-10.

GitHub Actions run:

\[
\boxed{\texttt{35488545595}}.
\]

The result does not depend on the earlier particular ROBUST9 witness.  It is
an exhaustive quotient search over **all** size-9 alphabets.

## C5 · exact size-10 quotient search — RUNNING

The same exact partition-type quotient is now applied to total alphabet size
10.  If it finds no witness,

\[
M_1(W_4)\ge11.
\]

If it finds a full one-erasure depth-four witness,

\[
M_1(W_4)=10.
\]


## C6 · subsets of the certified adaptive12 witness — CLOSED NEGATIVE

All

\[
\binom{12}{10}=66
\]

size-10 subsets and all

\[
\binom{12}{11}=12
\]

size-11 subsets of the frozen H18-11 adaptive12 alphabet were tested against
the exact H18-06 dynamic programme.

GitHub Actions run:

\[
\boxed{\texttt{35489231268}}.
\]

Results:

\[
\begin{array}{c|cc}
& |A|=10 & |A|=11\\
\hline
\text{tested} & 66 & 12\\
D_0(A)\le4 & 56 & 12\\
S_1(A)\le4 & 0 & 0
\end{array}
\]

Thus many proper subsets preserve ordinary depth-four tomography, but **none**
preserves the full one-persistent-erasure depth-four contract.

This yields a structural observation:

\[
\boxed{
\text{fault-tolerant adaptive sufficiency is strictly more fragile than}
\atop
\text{fault-free depth-four sufficiency inside the certified witness family}.
}
\]

No global lower bound beyond

\[
10\le M_1(W_4)\le12
\]

is inferred from this subset experiment, because other size-10 or size-11
alphabets in the full 50-query pool remain possible.

The global size-10 partition-type quotient search remains the decisive next
gate.


## C7 · exact global size-10 partition-type search — CLOSED NEGATIVE

The exact size-10 quotient search completed successfully.

GitHub Actions run:

\[
\boxed{\texttt{35488658329}}.
\]

The 50 W4 query identities were represented by the already certified 25
partition types, preserving multiplicity \(0/1/2\) because erasure acts on
query identity.

After fixing the forced commutator type at multiplicity two, the search selected
total multiplicity eight from the remaining 24 types.

Exact statistics:

\[
\boxed{1\,493\,502\text{ DFS states}}
\]

with

\[
\boxed{88\,100}
\]

complete distance-two size-10 multiplicity vectors.

Every one of those 88,100 alphabets was passed to the exact H18-06 adaptive
dynamic programme.

Among them,

\[
\boxed{6\,368}
\]

support the fault-free depth-four contract

\[
D_0(A)\le4.
\]

But the number supporting the full one-persistent-erasure depth-four contract is

\[
\boxed{0}.
\]

Therefore no size-10 W4 alphabet can realize the H18-06 robust adaptive
contract, and the certified bracket improves to

\[
\boxed{
11\le M_1(W_4)\le12.
}
\]

This is a global exact result, not a neighborhood or witness-family search.

### Structural consequence

The gap between ordinary and fault-tolerant adaptive tomography is now visible
globally at size 10:

\[
6368
\]

alphabets preserve fault-free depth four, while none preserves one-erasure
successful depth four.

Thus the obstruction at size 10 is specifically the robust adaptive contract,
not merely insufficient ordinary distinguishing power.

The global size-11 exact search is now the decisive closure gate:

- a size-11 witness gives \(M_1(W_4)=11\);
- global size-11 exclusion, by the alphabet-monotonicity lemma and the existing
  size-12 witness, gives \(M_1(W_4)=12\).
