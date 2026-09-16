# HATTER-SOL-17 · Two-port maximal-first arithmetic frontend seed

## Status

Interface seed only. This is **not** part of the proved `PSL(2,7)` tomography theorem and is not promoted to a canonical orbital law.

It records a possible arithmetic frontend linking the H07 free-port factorization model and the H11 maximal-first experimental protocol to a future H17 two-port processor.

## 1. Source model

H07 uses multiplicative factorizations

\[
(a_1,\ldots,a_k),\qquad a_i\ge2,\qquad \prod_i a_i=n.
\]

For a strict two-port/factor-node frontend define

\[
\mathcal D_2(n)
:=
\{(a,b): a\ge b\ge2,\ ab=n\}.
\]

If `n` is prime, `D_2(n)` is empty and the frontend simply has no nontrivial two-factor state. Prime inputs are not the motivating case here.

## 2. Maximal-first protocol

H11 preserved the historical **maximal-first** convention only as an experimental search rule: rank factor capacities from larger to smaller and inspect the largest available capacity first. It is not assumed to be an intrinsic orbit law.

For the two-factor frontend this gives the deterministic probe

\[
\operatorname{MF}_2(n)
:=
\max_{\rm lex}\mathcal D_2(n),
\]

when `D_2(n)` is nonempty.

Thus the first coordinate is made as large as possible, with the second coordinate forced by the product constraint.

## 3. Elementary closed form

Let `n` be composite and let `p_min(n)` be its smallest prime divisor. Then

\[
\boxed{
\operatorname{MF}_2(n)
=
\left(\frac{n}{p_{\min}(n)},\ p_{\min}(n)\right).
}
\]

### Proof

For `(a,b) in D_2(n)`, `a=n/b`. Maximizing `a` is therefore equivalent to minimizing the nontrivial divisor `b>=2`. The least nontrivial divisor of a composite integer is prime and equals `p_min(n)`. Hence the displayed pair is the unique lexicographically maximal two-factor decomposition. QED.

This proposition proves only the behavior of the stated maximal-first **protocol**. It does not prove that arithmetic intrinsically privileges that factor pair.

## 4. Examples

### `n=52`

The unordered two-factor states are

\[
\mathcal D_2(52)=\{(26,2),(13,4)\}.
\]

Since

\[
26>13,
\]

the maximal-first probe begins with

\[
\boxed{52\mapsto(26,2)}.
\]

The `(13,4)` state remains in the full feasible two-factor family and must not be erased from the mathematical model merely because the probe inspects `(26,2)` first.

### `n=9`

\[
\mathcal D_2(9)=\{(3,3)\},
\]

so

\[
\boxed{9\mapsto(3,3)}.
\]

### `n=6`

\[
\mathcal D_2(6)=\{(3,2)\},
\]

so

\[
\boxed{6\mapsto(3,2)}.
\]

## 5. Why this may matter for H17

A future arithmetic frontend could turn an integer into a controlled pair of port capacities before the non-Abelian observer layer:

```text
integer n
 -> full two-factor family D2(n)
 -> optional maximal-first selector MF2(n)
 -> two port capacities
 -> chosen port-world realization
 -> non-Abelian tomography core
```

The important separation is:

```text
factor pair != group elements A,B
```

A further realization map is required before capacities such as `(26,2)` become actual noncommuting port actions. That realization map is a new research problem and must not be silently invented.

## 6. Research question retained

Determine whether there exists a natural, symmetry-respecting realization functor from H07 factor-capacity pairs into one of the H14/H15/H17 port worlds such that:

1. different two-factor states can sometimes land in different observer orbits;
2. the maximal-first probe has a measurable selection penalty relative to the full factor family;
3. the construction preserves enough arithmetic information to be more than an arbitrary encoding.

Until such a result exists, this file is an interface seed, not a theorem connecting integer factorization to `PSL(2,7)` orbits.
