# FCOA Hybrid Memory — Linear Cost of AL2 via Four-Modulus CRT

**Direction:** SOL-HYBRID — Joint Memory of Partial Operations  
**Status:** theorem candidate; constructive upper bound proved; hostile audit still required for implementation details

## 1. Question

Can canonical truncated multiplication on an `N`-point arithmetic sector be recovered with only `Theta(N)` bounded-arity memory, or does multiplication force a superlinear resource wall?

The answer is: **no superlinear wall is forced**. Four residue systems of size `Theta(sqrt N)` suffice.

## 2. Why the two-modulus AL1 trick is insufficient

For addition, two coprime moduli `p,q=Theta(sqrt N)` with `pq>2N` suffice because

\[
|x+y-z|<2N.
\]

For multiplication,

\[
-(N-1)\le xy-z\le (N-1)^2,
\]

so the possible error has magnitude `Theta(N^2)`. A product of only two `Theta(sqrt N)` moduli is only `Theta(N)` and cannot force uniqueness.

## 3. Four-modulus construction

Choose four pairwise coprime moduli

\[
m_1,m_2,m_3,m_4=\Theta(\sqrt N)
\]

such that

\[
M:=m_1m_2m_3m_4>(N-1)^2+N.
\]

For instance, one may choose four distinct primes from four disjoint constant-factor intervals above `sqrt N`; all remain `Theta(sqrt N)` and their product is a constant multiple of `N^2`.

For every target element `x\in X_N={0,\ldots,N-1}`, store its four residues

\[
\rho_i(x)=x\bmod m_i.
\]

This costs `4N` residue incidences.

On each residue sort store the complete multiplication table

\[
T_i(a,b,c)\iff ab\equiv c\pmod{m_i}.
\]

Each table has exactly `m_i^2` graph entries, so

\[
\sum_{i=1}^4 m_i^2=\Theta(N).
\]

## 4. Exact recovery of truncated multiplication

Define `Mul_N(x,y,z)` by requiring the residue of `z` to equal the residue product of `x,y` in all four moduli.

Then

\[
xy-z\equiv0\pmod{m_i}
\]

for every `i`, hence by pairwise coprimality

\[
M\mid(xy-z).
\]

But for `x,y,z<N`,

\[
-(N-1)\le xy-z\le(N-1)^2,
\]

and by construction this interval contains no nonzero multiple of `M`. Therefore

\[
\boxed{xy=z.}
\]

Conversely ordinary multiplication equality obviously satisfies all modular multiplication constraints.

Hence the four-residue scaffold uniformly defines the exact truncated rank-multiplication graph.

## 5. AL2 consequence

Combine this multiplication layer with the already established sparse AL0 order layer and the linear CRT AL1 addition layer.

Then the target sector uniformly carries

\[
<,
\qquad +,
\qquad \times
\]

in the canonical truncated-rank sense.

Therefore the family reaches

\[
\boxed{AL2.}
\]

## 6. Resource count

The multiplication layer costs

\[
4N+\sum_{i=1}^4m_i^2=\Theta(N).
\]

Adding the existing AL0 and AL1 layers preserves the same asymptotic scale:

\[
\boxed{\operatorname{Cost}(AL2)=O(N).}
\]

The generic bounded-arity incidence lower bound already gives

\[
\Omega(N)
\]

for any structure that must distinguish an `N`-point arithmetic sector.

Thus in the same auxiliary-carrier cell model,

\[
\boxed{\operatorname{Cost}(AL2)=\Theta(N).}
\]

## 7. No asymptotic phase transition in cell count

The branch now has

\[
\boxed{
\operatorname{Cost}(AL0)=\Theta(N),
\qquad
\operatorname{Cost}(AL1)=\Theta(N),
\qquad
\operatorname{Cost}(AL2)=\Theta(N).
}
\]

So the logical hierarchy

\[
AL0<AL1<AL2
\]

is **not reflected in the exponent of sparse memory cost** when auxiliary carriers and fixed bounded-arity compilation are permitted.

What changes across the hierarchy is the semantic organization of the linear amount of information:

- AL0: comparison coordinates;
- AL1: additive residue coordinates;
- AL2: multiplicative residue coordinates with enough combined modulus to dominate the quadratic error range.

## 8. Why four moduli are the natural sqrt-scale threshold

Suppose one insists on `k` residue systems all of comparable size `N^alpha`. To distinguish multiplication errors of size `Theta(N^2)`, their product must satisfy

\[
N^{k\alpha}>N^2,
\]

so

\[
\alpha>2/k.
\]

The full multiplication tables cost

\[
kN^{2\alpha}.
\]

For linear table cost one needs

\[
2\alpha\le1.
\]

Combining the inequalities requires

\[
\frac{2}{k}<\frac12,
\]

hence

\[
\boxed{k\ge4.}
\]

At `k=4`, taking moduli of size `Theta(sqrt N)` is exactly the critical linear-cost scale.

Thus within the equal-scale complete-table CRT template, four residue systems are asymptotically minimal.

## 9. Fixed two-operation compilation

As in the AL1 construction, each residue-map or multiplication-table record is a bounded-arity finite relational record. Encode it by a constant-size incidence gadget and then compile the incidence graph into the fixed two-operation one-sorted FCOA language.

Constant-factor gadget expansion preserves

\[
\Theta(N)
\]

total operation-cell cost.

Therefore AL2 is reachable in the same fixed-signature partial-operation framework.

## 10. Main conclusion

Multiplication is not the first superlinear resource wall.

The four-modulus CRT construction gives

\[
\boxed{AL2\text{ with }\Theta(N)\text{ sparse memory}.}
\]

Hence the full AL hierarchy discovered so far is a hierarchy of **logical organization**, not asymptotic information volume.

The next meaningful resource question must therefore refine the cost model: leading constants, number of auxiliary carriers, maximum degree, number of residue sorts/gadgets, quantifier complexity, or restrictions forbidding auxiliary-coordinate compression.
