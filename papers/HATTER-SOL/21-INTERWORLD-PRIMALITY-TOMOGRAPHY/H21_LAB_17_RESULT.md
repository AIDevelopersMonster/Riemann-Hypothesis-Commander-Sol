# HATTER-SOL-21 · H21-LAB-17 RESULT

Status: **CI REPRODUCED / PROJECTIVE PHASE-PLACEMENT THEOREM VALIDATED**

Run:

\`35726609291\`

Largest validation grid:

\[
p\le257,
\qquad
|D|\le63.
\]

## 1. Validation totals

World/prime rows:

\[
\boxed{1987}.
\]

Projective-order checks:

\[
\boxed{1987}.
\]

Zero-fiber placement checks:

\[
\boxed{5961}.
\]

Nonzero partial-transversal checks:

\[
\boxed{11922}.
\]

Minus-level translation checks:

\[
\boxed{3870}.
\]

Special \(+1/-1\) projective-fiber checks:

\[
\boxed{1987}.
\]

Canonical \(B=0\) projective-collapse checks:

\[
\boxed{743}.
\]

Failures:

\[
\boxed{0}.
\]

## 2. Exact projective clock

Define

\[
e_p=\frac{h_p}{d_p},
\qquad
d_p=|H_p\cap\mathbf F_p^\times|.
\]

Then

\[
\boxed{
e_p
=
\operatorname{ord}\left(\frac{x}{\tau(x)}\right)
}
\]

and

\[
\boxed{
e_p\mid p-\chi_p.
}
\]

Thus:

\[
\chi_p=+1
\Longrightarrow
e_p\mid p-1,
\]

\[
\chi_p=-1
\Longrightarrow
e_p\mid p+1.
\]

This identifies \(e_p\), not \(h_p\), as the number of geometrically distinct
scalar rays visited by the orbit.

## 3. Exact phase coordinates

Because

\[
D_p=\langle x^{e_p}\rangle,
\]

every phase has a unique decomposition

\[
\boxed{
m=r+k e_p,
}
\]

with

\[
0\le r<e_p,
\qquad
0\le k<d_p.
\]

Writing

\[
\lambda_p=x^{e_p}\in\mathbf F_p^\times,
\]

we have

\[
\boxed{
x^m=\lambda_p^k x^r.
}
\]

Hence every local phase has two intrinsic coordinates:

\[
\boxed{
(\text{projective phase }r,\ \text{scalar-fiber phase }k).
}
\]

## 4. Zero levels are complete fibers

For every tested nonzero linear observer functional \(\ell\),

\[
\ell(x^m)=0
\]

was either unsatisfied for the entire orbit or held exactly on one complete
fiber

\[
\boxed{
r_0+e_p\mathbf Z/d_p\mathbf Z.
}
\]

This validates the exact geometric statement:

\[
\boxed{
\text{zero-level phase set}
=
\text{one projective point lifted through all scalar phases}.
}
\]

## 5. Nonzero levels are partial transversals

For

\[
c\ne0,
\]

the phase set

\[
M_{\ell,c}
=
\{m:\ell(x^m)=c\}
\]

contains at most one phase above each projective point \(r\).

Thus it is exactly a partial graph

\[
\boxed{
r\mapsto k_c(r)
}
\]

over a subset of the projective clock.

All

\[
\boxed{11922}
\]

tested nonzero observer-level cases satisfied this partial-transversal law.

## 6. Scalar translation law

If

\[
t=\lambda_p^u\in D_p,
\]

then the phase sets for levels \(c\) and \(tc\) are related by

\[
\boxed{
M_{\ell,tc}
=
M_{\ell,c}+u e_p
\pmod{h_p}.
}
\]

In particular, whenever

\[
-1\in D_p,
\]

\[
\boxed{
M_{\ell,-c}
=
M_{\ell,c}+\frac{h_p}{2}.
}
\]

All tested \(c=\pm1\) translations passed.

## 7. Distinguished projective phases

The positive prime-law target \(x\) lies at projective phase

\[
\boxed{r=+1}.
\]

The negative target

\[
\tau(x)=(-C)x^{-1}
\]

differs from \(x^{-1}\) only by a scalar, hence lies at

\[
\boxed{r=-1}.
\]

Thus the two distinguished observer directions appear intrinsically as the two
projective phases

\[
+1,\ -1.
\]

## 8. Canonical even-discriminant collapse

For canonical worlds with

\[
B=0,
\]

\[
x^2=C\in\mathbf F_p^\times.
\]

Therefore

\[
\boxed{
e_p\le2.
}
\]

All

\[
\boxed{743}
\]

tested canonical \(B=0\) cases satisfied this collapse.

This reveals an important distinction:

a world may have a large full multiplicative order \(h_p\) but still have an
extremely small projective observer orbit.

## 9. Finite geometry statistics

On the largest grid:

\[
\operatorname{mean}d_p
=
\boxed{55.009059},
\]

median

\[
\boxed{23},
\]

maximum

\[
\boxed{256}.
\]

The projective clock had

\[
\operatorname{mean}e_p
=
\boxed{45.728234},
\]

and maximum

\[
\boxed{258}.
\]

These are finite experimental descriptors, not universal bounds.

## 10. New exact observer geometry

The local H21 observer is no longer represented by a flat clock

\[
m\in\mathbf Z/h_p\mathbf Z.
\]

It has the exact fibered geometry

\[
\boxed{
\mathbf Z/h_p\mathbf Z
\longleftrightarrow
\mathbf Z/e_p\mathbf Z
\times
\mathbf Z/d_p\mathbf Z
}
\]

at the set level, with the multiplicative orbit written as

\[
x^{r+k e_p}
=
\lambda_p^k x^r.
\]

Observer lines become:

- complete fibers for zero levels;
- partial transversals for nonzero levels.

This is the first exact phase-placement structure in H21.

## 11. Remaining reciprocal problem

For a semiprime \(pq\), the two selected phases are

\[
q\bmod h_p,
\qquad
p\bmod h_q.
\]

They now decompose into

\[
(r_{p\leftarrow q},k_{p\leftarrow q})
\]

and

\[
(r_{q\leftarrow p},k_{q\leftarrow p}).
\]

The unexplained coupling term \(K_W\) is therefore no longer an arbitrary
correlation on long phase tables.

It is a correlation between two **projective-support / scalar-fiber
coordinates**.

The next strike is to determine whether coupling lives mainly in:

1. projective-phase synchronization \(r\);
2. scalar-fiber synchronization \(k\);
3. or the dependence \(k(r)\) of the partial-transversal graph.

That is now a sharply finite and algebraically natural decomposition problem.
