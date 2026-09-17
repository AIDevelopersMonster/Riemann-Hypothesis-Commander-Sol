# HATTER-SOL-15 · The selected genus-two observer motive is absolutely simple

**Status:** exact theorem layer for the `p=3, lambda=0` laboratory.  
**Input:** `MAHLER_REGULATOR_CHARACTER_FILTER.md`, which proves that the natural Mahler regulator lies in the pure `abc` character sector and descends to the genus-two quotient.

## 1. The selected curve

For

\[
p=3,\qquad \lambda=0,\qquad \mu=4,\qquad \vartheta=-1,
\]

the regulator-selected quotient is

\[
C:\quad Y^2=(u^2-4)(u^2+4u+13)(u^2+4u+9).
\]

After the rational translation

\[
x=u+2,
\]

we obtain

\[
\boxed{
C:\quad y^2=f(x)
=x(x-4)(x^2+5)(x^2+9).
}
\]

The polynomial discriminant is

\[
\operatorname{disc}(f)
=2^{16}3^8 5^7 7^2,
\]

so `31` and `37` are primes of good reduction.

The purpose of this note is to decide a critical possibility left open by the character-filter theorem:

\[
\boxed{
J(C)\stackrel{?}{\sim}_{\overline{\mathbf Q}} E_1\times E_2.
}
\]

It does **not** happen.

---

## 2. Exact finite-field counting formula

Let `p` be an odd prime of good reduction. Since `f` is monic of degree six, the smooth projective model has two rational points at infinity over every field in which the leading coefficient is a square; here the leading coefficient is `1`.

Thus

\[
\#C(\mathbf F_q)
=q+2+
\sum_{x\in\mathbf F_q}\chi_q(f(x)),
\]

where `chi_q` is the quadratic character, extended by `chi_q(0)=0`.

For `q=p^2`, choose a nonsquare `d mod p` and write

\[
\mathbf F_{p^2}=\mathbf F_p[\tau]/(\tau^2-d),
\qquad x=a+b\tau.
\]

Since

\[
\chi_{p^2}(z)=\chi_p\!\left(N_{\mathbf F_{p^2}/\mathbf F_p}(z)\right),
\]

we can count using only Legendre symbols in `F_p`.

For our factorized polynomial,

\[
N(f(a+b\tau))=N_1N_2N_3N_4,
\]

with

\[
N_1=a^2-db^2,
\]

\[
N_2=(a-4)^2-db^2,
\]

\[
N_3=(a^2+db^2+5)^2-4da^2b^2,
\]

\[
N_4=(a^2+db^2+9)^2-4da^2b^2.
\]

Hence every point count below is a finite exact character sum over integers modulo `p`; no floating-point arithmetic is involved.

---

## 3. The prime 31

Take `d=3`, a quadratic nonsquare modulo `31`.

The exact character sums are

\[
\sum_{a\in\mathbf F_{31}}\chi_{31}(f(a))=-3,
\]

and

\[
\sum_{a,b\in\mathbf F_{31}}
\chi_{31}(N(f(a+b\tau)))=55.
\]

For audit, the second double sum can be grouped by `b=0,1,...,30`; the row sums are

```text
29, -1, -9, 7, 7, 3, -1, -5, -1, -8, -1, 2, 7, 3, 3, 7,
7, 3, 3, 7, 2, -1, -8, -1, -5, -1, 3, 7, 7, -9, -1
```

and their total is `55`.

Therefore

\[
\boxed{\#C(\mathbf F_{31})=31+2-3=30,}
\]

\[
\boxed{\#C(\mathbf F_{31^2})=31^2+2+55=1018.}
\]

Write the local numerator as

\[
L_{31}(T)
=1-a_1T+a_2T^2-31a_1T^3+31^2T^4.
\]

From

\[
a_1=31+1-\#C(\mathbf F_{31})
\]

and

\[
\#C(\mathbf F_{31^2})
=31^2+1-(a_1^2-2a_2),
\]

we get

\[
a_1=2,
\qquad
a_2=30.
\]

Thus

\[
\boxed{
L_{31}(T)
=1-2T+30T^2-62T^3+961T^4.
}
\]

Equivalently, the Frobenius polynomial is

\[
P_{31}(X)
=X^4-2X^3+30X^2-62X+961.
\]

In the standard notation

\[
P(X)=X^4+aX^3+bX^2+aqX+q^2,
\]

we have

\[
q=31,\qquad a=-2,\qquad b=30.
\]

It is ordinary because `31` does not divide `b`.

The ordinary splitting discriminant is

\[
\Delta=a^2-4(b-2q)
=4-4(30-62)
=132,
\]

which is not a square. Hence the reduction is simple.

Now apply Howe--Zhu, Theorem 6 (*J. Number Theory* 92 (2002), 139--163, DOI `10.1006/jnth.2001.2697`). A simple ordinary abelian surface with Frobenius polynomial as above fails to be absolutely simple only in one of the four exceptional cases

\[
a=0,
\qquad
a^2=q+b,
\qquad
a^2=2b,
\qquad
a^2=3b-3q.
\]

Here

\[
4\ne61,
\qquad
4\ne60,
\qquad
4\ne-3,
\]

and `a != 0`. Therefore

\[
\boxed{
J(C)_{\mathbf F_{31}}
\text{ is absolutely simple.}
}
\]

### Theorem H15.63 — absolute simplicity over `Qbar`

\[
\boxed{
J(C)_{\overline{\mathbf Q}}
\text{ is absolutely simple.}
}
\]

#### Proof

Suppose that the characteristic-zero Jacobian were geometrically non-simple. Then after a finite number-field extension there would be a nontrivial isogeny decomposition, equivalently a nontrivial idempotent in its rational geometric endomorphism algebra. At a prime above `31` of good reduction, specialization of geometric endomorphisms is injective and the decomposition specializes up to isogeny. The geometric reduction would therefore be non-simple. This contradicts the absolute simplicity of the reduction just proved. QED.

---

## 4. Independent second witness: the prime 37

A second prime is useful both as a hostile check and for the endomorphism discussion below.

Take `d=2`, a quadratic nonsquare modulo `37`. The exact sums are

\[
\sum_{a\in\mathbf F_{37}}\chi_{37}(f(a))=-7,
\]

\[
\sum_{a,b\in\mathbf F_{37}}
\chi_{37}(N(f(a+b\tau)))=-17.
\]

The `b`-row sums of the second character sum are

```text
33, 1, -3, -3, 2, 1, -3, 5, 5, 5, -3, -3, 1, -7, -3, -3, -3,
-3, -11, -11, -3, -3, -3, -3, -7, 1, -3, -3, 5, 5, 5, -3, 1, 2,
-3, -3, 1
```

and total `-17`.

Thus

\[
\#C(\mathbf F_{37})=37+2-7=32,
\]

\[
\#C(\mathbf F_{37^2})=37^2+2-17=1354.
\]

Hence

\[
\boxed{
L_{37}(T)
=1-6T+10T^2-222T^3+1369T^4,
}
\]

and

\[
P_{37}(X)
=X^4-6X^3+10X^2-222X+1369.
\]

Here `q=37`, `a=-6`, `b=10`, so the reduction is ordinary and

\[
\Delta
=36-4(10-74)
=292
=4\cdot73,
\]

again nonsquare. None of the four Howe--Zhu exceptional equalities holds, so the reduction at `37` is also absolutely simple.

This independently confirms that the genus-two factor is not hiding an elliptic product.

---

## 5. A stronger endomorphism consequence

For the two ordinary absolutely simple reductions, the maximal real quadratic subfields of the quartic Frobenius CM fields are detected by the same splitting discriminants:

\[
K_{31}^+=\mathbf Q(\sqrt{33}),
\qquad
K_{37}^+=\mathbf Q(\sqrt{73}).
\]

The quartic Frobenius polynomials have `D_4` normal closures; a direct resolvent certificate is

\[
R_{31}(Y)=(Y-62)(Y^2+32Y-1736),
\]

\[
R_{37}(Y)=(Y-74)(Y^2+64Y+592),
\]

with nonsquare polynomial discriminants. Thus each quartic Frobenius field is non-Galois and has a unique quadratic subfield, namely the real field displayed above.

Specialization embeds the characteristic-zero geometric endomorphism algebra into the geometric endomorphism algebra of each good reduction. Since the latter are commutative quartic CM fields, quaternionic multiplication is impossible. A quadratic or quartic geometric endomorphism field would have to embed into both Frobenius fields; uniqueness of their quadratic subfields would force

\[
\mathbf Q(\sqrt{33})\cong\mathbf Q(\sqrt{73}),
\]

which is false. Consequently the only remaining possibility in the Albert classification is

\[
\boxed{
\operatorname{End}^0(J(C)_{\overline{\mathbf Q}})=\mathbf Q.
}
\]

Equivalently, the selected Jacobian has no hidden RM, CM, or QM enhancement compatible with these two reductions.

**Claim discipline:** the absolute-simplicity theorem does not require this strengthened endomorphism paragraph. If a publication audit finds that an additional hypothesis is needed for the two-prime specialization argument, retain H15.63 and demote only the `End^0=Q` strengthening until that hypothesis is supplied.

---

## 6. Structural consequence for HATTER-SOL-15

The previous theorem layer gave

\[
\text{natural Mahler observer}
\longrightarrow
\chi_{abc}\text{ sector}
\longrightarrow
C_{abc}.
\]

The present theorem now gives

\[
\boxed{
\text{natural Mahler observer}
\longrightarrow
\text{a genuinely absolutely-simple genus-two Jacobian}.
}
\]

Therefore the earlier possibility

\[
J(C_{abc})\sim E_1\times E_2
\]

is ruled out even over `Qbar`.

This is important conceptually. The observer filtration does not merely select a quotient that then collapses back to elliptic data. In the first laboratory it selects a genuinely higher-genus arithmetic object.

The next target is consequently no longer an elliptic-label search. It is:

\[
\boxed{
\text{identify the motivic/automorphic }L\text{-data of this simple genus-two Jacobian}
\quad\text{and compare its regulator with the Jensen--Mahler period.}
}
\]

A separate prior-art audit is still required before attaching novelty language to the full observer-selection-plus-simple-motive synthesis.
