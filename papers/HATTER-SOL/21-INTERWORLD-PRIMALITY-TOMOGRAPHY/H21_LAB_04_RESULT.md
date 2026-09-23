# HATTER-SOL-21 · H21-LAB-04 SIGN-ONLY NEGATIVE CONTROL

Status: **CLOSED NEGATIVE CONTROL**

Wide CI run:

\`35595482167\`

## 1. Frozen world signs

Discriminants:

\[
-7,\ 5,\ -3,\ -11,\ 13,\ -19.
\]

The sign-only observer retains only

\[
\left(\frac{D_i}{n}\right)\in\{-1,0,+1\}.
\]

Its combined character modulus is

\[
\boxed{M=285285}.
\]

Because the scanned sequence contains odd integers only, the comparison period is

\[
\boxed{2M=570570}.
\]

## 2. Direct periodicity verification

On the \(2^{21}\) scan, the CI checked

\[
\boxed{277400}
\]

eligible pairs

\[
n,\ n+570570
\]

and found

\[
\boxed{0\text{ mismatches}.}
\]

Thus the selected sign-only surface is exactly periodic under the tested odd
translation, as predicted by the finite quadratic-character structure.

## 3. Curvature-proxy control

Mean sign-only curvature proxy:

| class | mean |
|---|---:|
| prime | 24.267774 |
| prime square | 22.157895 |
| distinct semiprime | 25.229807 |
| higher prime power | 25.419355 |
| other composite | 27.109160 |

The prime class is **not** extremal.

In particular the apparent prime-high curvature found in the richer LAB-03
categorical observer disappears after Frobenius pass/fail information is
removed.

## 4. Conclusion

The quadratic split/inert surface by itself does not provide a new geometric
signature of primality in this laboratory.

Its geometry is a finite periodic residue-character geometry.

Therefore H21 should not continue by adding more static quadratic-character
surfaces or by interpreting their plotted curvature as a prime law.

## 5. Surviving target

The richer Frobenius observer remains useful because it measures more than the
quadratic character:

\[
\boxed{
\text{expected Frobenius action}
\quad\text{versus}\quad
\text{actual action modulo }n.
}
\]

For composites this produces a defect

\[
\delta_W(n)
=
x^n-\operatorname{Frob}^{\rm expected}_W(x)
\]

inside the quadratic algebra.

That defect is generally nonperiodic in \(n\) over a fixed finite character
modulus and may expose a nontrivial factor through gcd projections.

H21 therefore moves from **surface curvature of signs** to **surface defect
tomography**.

## 6. Next theorem/lab target

For every world handle retain the full defect pair

\[
\delta_W(n)=(d_{0,W}(n),d_{1,W}(n))\pmod n.
\]

Measure:

1. zero/nonzero defect;
2. gcd\((n,d_0)\);
3. gcd\((n,d_1)\);
4. gcd\((n,d_0,d_1)\);
5. first world that certifies compositeness;
6. first world that yields an actual nontrivial factor;
7. whether different worlds expose different factors of the same composite.

The new question is

\[
\boxed{
\text{Does a multiworld defect surface carry a reproducible factorization
tomography beyond single-world probable-prime rejection?}
}
\]

This is now the active H21 strike.
