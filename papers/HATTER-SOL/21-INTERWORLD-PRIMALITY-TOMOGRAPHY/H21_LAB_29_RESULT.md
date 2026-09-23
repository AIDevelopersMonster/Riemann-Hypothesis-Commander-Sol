# HATTER-SOL-21 · H21-LAB-29 RESULT

Status: **CI REPRODUCED / 2-PRIMARY LIFT REDUCTION VALIDATED**

Run:

\`35750213834\`

Largest validation grid:

\[
p\le509,\qquad |D|\le127.
\]

## 1. Validation totals

Even-fiber local rows:

\[
\boxed{4541}.
\]

2-primary subgroup checks:

\[
\boxed{4541}.
\]

Scalar exponent checks:

\[
\boxed{680006}.
\]

Norm-lift antipode checks:

\[
\boxed{680006}.
\]

Failures:

\[
\boxed{0}.
\]

## 2. Exact 2-primary reduction

For

\[
d_p=2^{a_p}u_p,\qquad u_p\text{ odd},
\]

the map

\[
\eta_p(z)=z^{u_p}
\]

projects the scalar subgroup \(D_p\) onto its Sylow-\(2\) subgroup of order

\[
2^{a_p}.
\]

The two norm-compatible lifts \(z,-z\) satisfy

\[
\boxed{
\eta_p(-z)=-\eta_p(z).
}
\]

Thus the norm-lift ambiguity is always visible in the 2-primary projection,
even when the ordinary quadratic character cannot distinguish the two lifts.

## 3. Exponent interpretation

If

\[
z=\lambda_p^k,
\]

then the 2-primary projection depends only on

\[
k\bmod 2^{a_p}.
\]

The norm-square datum determines

\[
k\bmod 2^{a_p-1},
\]

leaving exactly the highest 2-primary bit unresolved.

The two norm lifts differ by

\[
\boxed{
2^{a_p-1}\pmod{2^{a_p}}.
}
\]

Therefore they have the same lower \(a_p-1\) bits and opposite top bit.

## 4. Observed 2-adic depth

On the largest grid, the histogram of

\[
a_p=v_2(d_p)
\]

is:

- \(a=1\): 2587;
- \(a=2\): 1091;
- \(a=3\): 417;
- \(a=4\): 233;
- \(a=5\): 102;
- \(a=6\): 72;
- \(a=7\): 10;
- \(a=8\): 29.

Hence the scalar double-cover problem genuinely occurs at multiple 2-adic
depths; it is not confined to a quadratic-character layer.

## 5. Relation to H21-LC1

H21-LC1 corresponds only to the first Sylow-\(2\) layer

\[
a_p=1.
\]

LAB-29 validates the full hierarchy

\[
\boxed{
D_p
\to
D_p^{(2)}
\cong C_{2^{a_p}}
\to
\text{highest 2-primary exponent bit}.
}
\]

## 6. Publication consequence

This is an exact and useful completion of the local binary-lift description,
but the underlying cyclic Sylow decomposition is classical.

Therefore:

\[
\boxed{\text{PUBLICATION THRESHOLD NOT CROSSED BY LAB-29 ALONE}.}
\]

The remaining publication-level mathematical question is now extremely narrow:

\[
\boxed{
\text{Does reciprocal prime sampling impose a nontrivial law on the highest
2-primary exponent bits?}
}
\]

A targeted prior-art audit is required before claiming novelty for any such
law.
