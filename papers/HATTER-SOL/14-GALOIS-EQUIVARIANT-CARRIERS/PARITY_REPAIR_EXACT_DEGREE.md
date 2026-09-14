# HATTER-SOL-14 · Parity Repair for Exact Equivariant Degree

**Status:** corrective theorem note for the supporting scalar layer.

The earlier exact-degree argument used parity adjustment too tersely. The central homology-separation theorem is unaffected, but the scalar negative controls should use the following lemma.

## Lemma PR14.1 — inverse-closed generating seeds of prescribed parity

Let `A` be a finite abelian group with `|A|>2`.

1. `A` has an inverse-closed generating set of even cardinality.
2. If `|A|` is even, `A` also has an inverse-closed generating set of odd cardinality.
3. These seeds may be chosen with size at most `2d(A)+2`, where `d(A)` is the minimum number of generators.

### Proof sketch

Write `A` as a product of cyclic factors. A generator of a cyclic factor of order greater than two is inserted together with its inverse, contributing two elements. Order-two direct factors contribute involutions. If the resulting parity is not the desired one, use one redundant involution: when the 2-torsion rank is at least two there are more nonzero involutions than are needed in a basis; when the 2-torsion rank is one and `|A|>2`, the unique involution lies in a cyclic subgroup of order greater than two (or in a cyclic subgroup obtained by combining the `C_2` factor with a nontrivial odd factor), so it can be omitted from an even seed and adjoined to obtain an odd seed. Thus both required parities are available in the even-order case, with at most two extra elements beyond the symmetrized generator bound. QED.

## Lemma PR14.2 — exact cardinality extension

Let `T` be an inverse-closed subset of `A\{1}` and let `q>=0` have the same parity as the desired increment. If

`|A|-1-|T| >= q`,

then, provided the parity of `q` is chosen to match an available union of inversion orbits, `T` can be enlarged by whole inversion orbits to size `|T|+q`.

For even `q` this is automatic: if the complement has at least `q` elements, use 2-orbits first; if fewer than `q/2` such orbits exist, the remaining required even number of elements is supplied by singleton involution orbits.

For odd `q`, first adjoin one unused involution and then apply the even case. PR14.1 lets us instead choose the seed parity so that only the even-increment case is needed.

## Corollary PR14.3 — repaired complete exhaustion statement

For the cyclotomic groups

`Gamma_k=(Z/(2^k-1)Z)^x/<2>`,

we have `d(Gamma_k)<=omega(2^k-1)=o(k)` and `|Gamma_k|=n_k>k` for all sufficiently large `k` (indeed the H13 bound gives this from an explicit large threshold).

Choose an inverse-closed generating seed whose parity equals `k`; its size is `o(k)`, hence is less than `k` for large `k`. Since `n_k>k`, PR14.2 enlarges it to an inverse-closed generating set of exact cardinality `k`.

Therefore, for all sufficiently large `k`, there exists a connected simple Galois-equivariant `k`-regular carrier and

`B_f=0`.

The publication manuscript should use this repaired argument rather than the earlier one-line parity adjustment.