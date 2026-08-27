# Hostile Audit Prompt — FCOA G4 Bounded-Output Rigidity Amplification

Use this prompt with the independent reviewer model. Do not provide our expected formulas or expected automorphism groups separately from the structure below.

---

You are performing an independent hostile audit of FCOA Branch G4.

Work strictly from the stated partial-operation cells. Do not import ordinary arithmetic meanings into the indices. External indices are construction labels only. UNDEF means absence of a cell, not a special value. Do not assume any expected automorphism group, spectrum formula, or minimality claim.

Let

\[
X_N=\{P_0,\dots,P_N\},\qquad N\ge3,
\]

with generic sector

\[
G_N=\{P_2,\dots,P_N\}.
\]

Retain the M0 multiplication cells:

\[
P_0\otimes P_i=P_0\qquad(1\le i\le N),
\]

\[
P_i\otimes P_0=E_i^\ast\qquad(2\le i\le N),
\]

\[
P_1\otimes P_i=P_i\otimes P_1=P_i\qquad(2\le i\le N),
\]

\[
P_i\otimes P_i=E_i^\times\qquad(2\le i\le N).
\]

All unspecified M0 cells are UNDEF. Every \(E_i^\ast,E_i^\times\) is terminal. Their subscripts are bookkeeping labels, not named constants.

## G4-C

Add exactly two distinct anonymous terminal outputs

\[
\Omega_+,\Omega_-.
\]

They are not named constants, not separately colored, and not placed in separate singleton sorts. They are anonymous terminal elements in the same structural environment. No product with either \(\Omega_+\) or \(\Omega_-\) as an argument is defined.

For every two distinct generic points, define exactly one cell by external carrier orientation:

\[
P_i\otimes_{4C}P_j=
\begin{cases}
\Omega_+,&i<j,\\
\Omega_-,&i>j,
\end{cases}
\qquad 2\le i,j\le N,\ i\ne j.
\]

Thus every off-diagonal ordered pair in \(G_N^2\) is defined.

Independently determine:

1. the automorphism group of the base-sort definedness reduct;
2. the automorphism group of the full partial operation;
3. whether the only possible nontrivial generic carrier automorphism is total reversal together with \(\Omega_+\leftrightarrow\Omega_-\);
4. whether any non-monotone permutation can preserve the unordered pair of value fibers;
5. the exact commutation locus and its size;
6. the complete Association Spectrum on \((X_N)^3\);
7. all exceptional small cases, especially \(N=3\) and \(N=4\);
8. whether \(\Omega_+,\Omega_-\) can be mixed with any \(E_i^\ast,E_i^\times\), especially at small \(N\);
9. whether a fixed two-element anonymous output alphabet can yield an unbounded index

\[
[\operatorname{Aut}(D):\pi_X\operatorname{Aut}(\star)]
\]

as \(N\to\infty\).

Do not assume that preserving the two fibers means preserving each individually; anonymous outputs may be swapped if the full operation permits it.

## G4-A

Start from G4-C and add exactly one further cell:

\[
P_1\otimes_{4A}P_0=\Omega_+.
\]

Do not add any other cell.

Independently determine:

1. whether this anchor internally fixes \(\Omega_+\);
2. whether total generic reversal can still extend to a full-operation automorphism;
3. the full-operation automorphism group;
4. the base-sort definedness automorphism group after erasing all output values;
5. whether definedness alone now permits the boundary swap \(P_0\leftrightarrow P_1\);
6. whether generic permutations remain arbitrary after value erasure;
7. the exact commutation locus;
8. the complete Association Spectrum;
9. the exact active-sort index

\[
[\operatorname{Aut}(D_{4A}|X_N):\pi_X\operatorname{Aut}(\otimes_{4A})].
\]

## Fiber-partition issue

Let

\[
D_+=\{(P_i,P_j):2\le i<j\le N\},
\]

\[
D_-=\{(P_i,P_j):2\le j<i\le N\}.
\]

Do not assume a priori that the setwise stabilizer of the partition \(\{D_+,D_-\}\) inside \(S_{N-1}\) is \(C_2\). Prove it or give a counterexample.

In particular, determine all permutations \(g\in S_{N-1}\) satisfying either

\[
i<j\iff g(i)<g(j)
\]

for all distinct generic labels, or

\[
i<j\iff g(i)>g(j)
\]

for all distinct generic labels.

Then test whether there are any other permutations preserving the equivalence relation

\[
(i,j)\equiv(k,l)
\iff
\bigl[(i<j\land k<l)\lor(i>j\land k>l)\bigr]
\]

without globally preserving or globally swapping the two classes.

## Association Spectrum discipline

For both G4-C and G4-A:

- enumerate the families of triples rather than extrapolating from G3;
- count `EQ`, `NEQ`, `LEFT`, `RIGHT`, `NONE` independently;
- check the total equals \((N+1)^3\);
- check \(N=3\) explicitly;
- report every family responsible for any `NEQ` if one exists;
- remember that terminal outputs cannot be used as further arguments.

## Definedness / one-sorted caveat

Report both:

1. the structurally relevant automorphism group on the active/base sort \(X_N\);
2. the full one-sorted definedness group if terminal outputs are retained as isolated points after value erasure.

Do not silently identify the two.

## Arithmetic leakage discipline

The G4 construction imports only the external orientation relation of the finite carrier into value fibers. It does not explicitly add internal addition or multiplication on indices.

Audit whether the stated G4 results themselves imply more than this. In particular:

- do not call the structure arithmetic merely because a finite total order is recoverable from the value coloring;
- do identify any stronger definability consequence that follows in the exact finite family;
- distinguish fixed-finite definability from uniform first-order definability across unbounded \(N\).

## Required final verdict

End with a table for G4-C and G4-A listing:

\[
\operatorname{Aut}(\star),
\qquad
\operatorname{Aut}(D_\star|X_N),
\qquad
|\operatorname{Comm}_\star|,
\]

\[
(EQ,NEQ,LEFT,RIGHT,NONE),
\]

and the active-sort rigidity index

\[
[\operatorname{Aut}(D_\star|X_N):\pi_X\operatorname{Aut}(\star)].
\]

Classify each main claim as CONFIRMED, REPAIRED, or REFUTED, and state every exceptional small case.
