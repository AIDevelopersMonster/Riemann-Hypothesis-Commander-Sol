# HATTER-SOL-21 · B=0 RUNTIME COST COLLAPSE

Status: **EXACT OPERATION-MODEL CONSEQUENCE**

## 1. Shared base multiplier model

Assume both runtime engines use the same sequential modular multiplication
primitive

\[
\operatorname{MM}(a,b;n)=ab\bmod n.
\]

Measure arithmetic cost in calls to this primitive.

This isolates the representation cost from a particular FPGA technology.

## 2. Generic quadratic multiplication for canonical B=1 worlds

For

\[
(a+bx)(c+dx)
\]

with

\[
x^2=x+C,
\]

compute

\[
m_0=ac,
\qquad
m_1=bd,
\qquad
m_2=(a+b)(c+d).
\]

Then

\[
ad+bc=m_2-m_0-m_1,
\]

and because \(B=1\),

\[
(a+bx)(c+dx)
=
\left(m_0+C m_1\right)
+
\left(m_2-m_0\right)x.
\]

Thus a generic runtime descriptor \(C\) requires:

\[
m_0,\ m_1,\ m_2,\ C m_1.
\]

Therefore:

\[
\boxed{
1\text{ quadratic algebra multiply}
\le
4\text{ base modular multiplications}.
}
\]

If multiplication by \(C\) is implemented by a cheaper constant unit, the
count may fall below four; LAB-26 treats four as the shared-general-multiplier
architecture.

## 3. B=0 compiled world

By H21-EJ1,

\[
x^n=C^{(n-1)/2}x.
\]

The full quadratic exponentiation disappears.

The runtime engine computes one ordinary scalar exponentiation

\[
C^{(n-1)/2}\bmod n.
\]

Every scalar square/multiply requires exactly one base modular multiplication.

## 4. Binary exponentiation count

For the standard left-to-right binary algorithm on a positive exponent \(e\),
starting from accumulator \(1\), the number of modular multiplications is

\[
\boxed{
M(e)
=
\lfloor\log_2 e\rfloor
+
\operatorname{popcount}(e)
}
\]

when the leading one initializes the accumulator rather than multiplying by
one.

Equivalent implementation conventions may shift both counts by at most a
constant; LAB-26 records the declared convention explicitly.

Hence the compiled \(B=0\) world costs

\[
\boxed{
M_{\rm scalar}(n)
=
M\left(\frac{n-1}{2}\right).
}
\]

A generic quadratic computation of \(x^n\) costs

\[
\boxed{
M_{\rm quad}(n)
=
4M(n)
}
\]

base modular multiplications in the shared-multiplier model.

## 5. Asymptotic ratio

For odd \(n\),

\[
M(n)=\Theta(\log n),
\]

and

\[
M((n-1)/2)=\Theta(\log n).
\]

Therefore

\[
\boxed{
\frac{M_{\rm quad}(n)}
{M_{\rm scalar}(n)}
\to 4
}
\]

up to the one-bit exponent shortening and popcount fluctuations.

This is a representation-level runtime saving, not a new primality theorem.

## 6. Hardware claim boundary

This model predicts cycle savings for a serial shared modular multiplier.

Actual FPGA claims require synthesis/timing and cycle-accurate RTL.

The next hardware laboratory should instantiate:

1. one shared sequential base modular multiplier;
2. a scalar Euler-Jacobi controller;
3. a quadratic algebra controller;

and compare:

- ALM/LUT;
- register count;
- Fmax;
- cycles per world;
- area×cycle cost.
