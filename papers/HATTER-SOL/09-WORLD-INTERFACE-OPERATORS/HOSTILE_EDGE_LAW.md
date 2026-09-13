# HATTER-SOL-09 · Hostile edge-law audit

## 1. Two incompatible continuations of HATTER-SOL-07

The canonical typed pair `(P,Q)` is well-defined, but the network edge law is not forced.

There are two natural models.

### Model M: multiplex interfaces

A pair of factor vertices may carry one `P`-edge and one `Q`-edge simultaneously.

This treats the two virtual interfaces as independent channels between the same endpoints.

For `k` identical nodes `(P,Q)`, full typed closure can occur once

\[
k\ge P+1.
\]

Hence for a split prime

\[
\tau_M(p)=\left\lceil\frac{P+1}{2}\right\rceil.
\]

This produced the provisional values

\[
\tau_M^G(53)=4,
\qquad
\tau_M^G(37)=4,
\qquad
\tau_M^E(37)=3.
\]

### Model S: simple-support typed edges

A pair of factor vertices may carry at most one edge total. That edge has type `P` or type `Q`, but not both.

Equivalently,

\[
E_P\cap E_Q=\varnothing.
\]

This model is faithful to the simple-graph host of HATTER-SOL-07 after forgetting edge types.

## 2. Exact closure threshold in the 07-faithful model

Let `k` be even and all nodes have the same typed capacity `(P,Q)`.

To saturate all ports in Model S we need an edge-disjoint `P`-regular graph and `Q`-regular graph on the same `k` vertices.

A necessary condition is

\[
P+Q\le k-1,
\]

because the union is a simple graph.

For even `k`, the complete graph `K_k` admits a 1-factorization into `k-1` perfect matchings. Selecting `P` matchings for the `P` layer and `Q` disjoint matchings for the `Q` layer gives edge-disjoint regular layers whenever

\[
P+Q\le k-1.
\]

For the split-prime profiles considered here, the union degree `P+Q` is at least 2, and the selected matchings can be chosen so that the union is connected.

Therefore the first full-closure condition is

\[
\boxed{k\ge P+Q+1.}
\]

Since a split prime `p^m` gives `k=2m` factor nodes,

\[
\boxed{
\tau_S(p)
=
\left\lceil\frac{P+Q+1}{2}\right\rceil.
}
\]

But `P+Q=rho`, so

\[
\boxed{\tau_S(p)=\tau^{(1)}(p).}
\]

Thus the typed closure exponent collapses exactly to the scalar HATTER-SOL threshold when the forgetful projection is required to remain a simple graph.

## 3. Consequence: the earlier threshold improvement was model-dependent

The apparent improvement

\[
53:\quad 5\to4
\]

and the distinction

\[
37:\quad 4\text{ versus }3
\]

come entirely from allowing two different virtual edges between the same pair of factor nodes.

They are valid results for Model M, but they are **not** consequences of the original HATTER-SOL-07 simple-graph model.

Therefore they must not be advertised as a canonical continuation of 07.

## 4. What survives this hostile test

The canonical typed pair survives unchanged:

\[
\Pi_G(37)=(6,1),
\qquad
\Pi_E(37)=(4,3),
\]

while

\[
\rho_G(37)=\rho_E(37)=7.
\]

Hence `37` still proves that the two-interface representation contains world information that scalarization loses.

What fails is only the claim that the **first zero-boundary exponent** must detect that difference in the 07-faithful edge model.

This redirects the search toward a genuinely typed invariant, for example:

1. the two-component boundary vector `(B_P,B_Q)` rather than only `B_P+B_Q`;
2. the attainable boundary region in `Z_{>=0}^2`;
3. a Pareto frontier of typed deficiencies;
4. orientation/gain data needed to glue local interface frames;
5. an operator built from those transition data.

## 5. First conclusion

There are now two branches of interpretation:

\[
\boxed{
\text{M: independent virtual channels}
}
\]

and

\[
\boxed{
\text{S: typed refinement of the original simple graph}.
}
\]

Model S is the conservative continuation of HATTER-SOL-07.

Model M may still be mathematically interesting, but it is a new multiplex network model and must be labeled as such.

The next target is therefore not another closure threshold. It is to find a typed boundary/spectral invariant that distinguishes `(6,1)` from `(4,3)` **inside Model S**, where the scalar simple-graph response is identical.
