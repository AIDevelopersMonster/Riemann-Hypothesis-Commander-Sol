# HATTER-SOL-14 · Non-Abelian Two-Port Schreier Seed

**Status:** future-transition seed; do not merge into the current H14 theorem spine without a separate audit.

## 1. Motivation

H14 currently exploits an abelian cyclotomic Galois group. For a prime above `2`, the decomposition subgroup `D_k=<2>` is normal, so the prime set is a quotient group and equivariant carriers reduce to Cayley graphs.

The proposed next move is to pass to a genuinely non-abelian finite Galois extension `L/K` with group `G` and decomposition subgroup `D` for a chosen prime. The primes above the base prime form a transitive `G`-set identified with a coset space `D\G` (or `G/D`, depending on convention). When `D` is not normal, this set is not a quotient group. The natural carrier is therefore Schreier/orbital rather than Cayley.

## 2. Two labelled ports

Choose two group elements `a,b in G` and retain their labels as two local ports:

\[
Dg\xrightarrow{a}Dga,
\qquad
Dg\xrightarrow{b}Dgb.
\]

The two length-two routes are

\[
Dg\xrightarrow{a}Dga\xrightarrow{b}Dgab
\]

and

\[
Dg\xrightarrow{b}Dgb\xrightarrow{a}Dgba.
\]

They meet exactly when

\[
Dgab=Dgba.
\]

For right cosets this is equivalent to

\[
\boxed{
 g(aba^{-1}b^{-1})g^{-1}\in D.
}
\]

Thus the failure of the local two-port square to close detects the commutator relative to the conjugate stabilizer `g^{-1}Dg`.

Define the local square defect

\[
\delta_{a,b}(Dg)=
\begin{cases}
0,&Dgab=Dgba,\\
1,&Dgab\ne Dgba.
\end{cases}
\]

This is a purely classical consistency observable. It does not invoke quantum entanglement.

## 3. Why this is structurally different from H14

In the abelian/normal case, the commutator is trivial in the quotient and every such square closes. In the non-abelian/non-normal case, the defect may vary with the vertex because the relevant stabilizer is conjugated by `g`.

Hence two labelled ports can carry path-order memory:

\[
\boxed{
ab\ne ba\quad\Longrightarrow\quad\text{route order can become observable on the coset carrier}.}
\]

This is the precise mathematical content behind the intuitive phrase "tangling two ports".

## 4. Hidden-check interpretation

A word `w(a,b)` closes at vertex `Dg` exactly when

\[
Dgw=Dg
\iff
\boxed{g w g^{-1}\in D}.
\]

Therefore local route-closure tests provide implicit membership tests in conjugates of the decomposition subgroup. A family of short words can act as a consistency-check system without revealing the full group element explicitly.

Potential hierarchy:

\[
\text{scalar boundary}
<
\text{equivariant homology}
<
\text{non-abelian path-order / Schreier memory}.
\]

## 5. Critical modeling caveat

The two ports must remain labelled or edge-coloured/directed. If the labels are forgotten and only an undirected uncoloured graph is retained, much of the order information can collapse.

For fully `G`-equivariant unlabelled relations on `D\G`, the natural objects are orbital/double-coset graphs associated with subsets of `D\G/D` rather than arbitrary single generators.

## 6. Research questions

1. For natural non-abelian Galois families, can the defect field `delta_{a,b}` distinguish arithmetic worlds that scalar/H1 data cannot?
2. Can one reconstruct nontrivial conjugacy or decomposition-subgroup data from finitely many two-port closure tests?
3. Can equal abstract Schreier graphs carry different labelled commutator-defect fields?
4. Is there a minimal pair of ports for which the route-order defect is nonzero on an arithmetic prime orbit?
5. Can the defect be upgraded from a binary closure test to a holonomy/monodromy class attached to short loops?
6. What survives after passing from labelled Schreier carriers to double-coset/orbital carriers?

## 7. Claim discipline

Use terms such as `non-abelian path-order memory`, `commutator defect`, `Schreier memory`, or `classical holonomy`.

Do **not** call this quantum entanglement without a separate physical theorem. The intended analogy is structural only: two routes become coupled through noncommutativity, while all objects remain classical finite groups/graphs.

## 8. Programme placement

This seed is a natural successor to H14 because H14 identifies arithmetic action on cycle space as information absent from the abstract graph. The non-abelian move replaces the abelian quotient group by a coset action and makes route order itself observable.

Recommended use: keep H14 focused on the current abelian equivariant-homology theorem. Treat the present note as the bridge to the next branch unless a direct lemma from this seed becomes necessary for H14's final interpretation.