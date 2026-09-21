# HATTER-SOL-21 · TORSION-WORLD NO-GO THEOREM

Status: **EXACT THEOREM LAYER**

## 1. The D=-3 world is cyclotomic

For

\[
B=1,\qquad C=-1,
\]

the quadratic world is

\[
A_n
=
(\mathbb Z/n\mathbb Z)[x]/(x^2-x+1).
\]

The defining polynomial is the sixth cyclotomic polynomial

\[
\Phi_6(x)=x^2-x+1.
\]

Inside every such quotient,

\[
x^2=x-1,
\]

hence

\[
x^3=-1
\]

and

\[
\boxed{x^6=1.}
\]

Quadratic conjugation is

\[
\tau(x)=1-x.
\]

But

\[
x(1-x)=x-x^2=1,
\]

so

\[
\boxed{\tau(x)=x^{-1}=x^5.}
\]

## 2. Character equals the exponent class

For every odd integer \(n\) with

\[
\gcd(n,3)=1,
\]

the quadratic character of discriminant \(-3\) satisfies

\[
\boxed{
\left(\frac{-3}{n}\right)
=
\begin{cases}
+1,&n\equiv1\pmod6,\\
-1,&n\equiv5\pmod6.
\end{cases}
}
\]

Therefore the expected H21 prime-world response is

\[
E_{-3}(n)
=
\begin{cases}
x,&n\equiv1\pmod6,\\
\tau(x)=x^{-1}=x^5,&n\equiv5\pmod6.
\end{cases}
\]

On the other hand, because \(x^6=1\),

\[
x^n
=
\begin{cases}
x,&n\equiv1\pmod6,\\
x^5,&n\equiv5\pmod6.
\end{cases}
\]

Thus the actual exponentiation response and the expected Frobenius response
coincide identically.

## Theorem H21-T1 — D=-3 defect silence

For every odd integer \(n\) with

\[
\gcd(n,3)=1,
\]

\[
\boxed{
\delta_{-3}(n)=0.
}
\]

Hence the coordinate-gcd defect observer can never expose a proper factor of
such an \(n\).

### Proof

The two cases \(n\equiv1,5\pmod6\) above exhaust odd \(n\) coprime to \(3\).
In both cases \(x^n=E_{-3}(n)\). QED.

## Corollary H21-T2 — exact source of D=-3 factor yield

For an odd composite \(n\), the declared \(D=-3\) world can expose a factor
only through the exceptional/precheck divisor

\[
\gcd(n,6).
\]

Therefore:

- if \(3\nmid n\), the full Frobenius defect is identically zero;
- if \(3\mid n\), the cheap precheck exposes the factor \(3\).

Thus the expensive quadratic exponentiation stage contributes **zero**
additional factor information for this world.

## 3. Gaussian analogue D=-4

Take

\[
A_n^{(4)}
=
(\mathbb Z/n\mathbb Z)[x]/(x^2+1),
\]

so

\[
x^2=-1,
\qquad
x^4=1,
\qquad
\tau(x)=-x=x^{-1}.
\]

For every odd \(n\),

\[
\left(\frac{-4}{n}\right)
=
\left(\frac{-1}{n}\right)
=
\begin{cases}
+1,&n\equiv1\pmod4,\\
-1,&n\equiv3\pmod4.
\end{cases}
\]

Hence

\[
x^n
=
\begin{cases}
x,&n\equiv1\pmod4,\\
-x,&n\equiv3\pmod4,
\end{cases}
\]

which again equals the expected quadratic Frobenius response.

## Theorem H21-T3 — D=-4 defect silence

For every odd integer \(n\),

\[
\boxed{
\delta_{-4}(n)=0.
}
\]

Thus the distinguished Gaussian root-of-unity world is completely silent for
the H21 defect-factor observer on odd inputs.

## 4. General torsion-world no-go criterion

Let a world carry a distinguished unit \(u\) satisfying

\[
u^m=1
\]

identically in every admissible residue algebra.

Suppose the expected prime-world response is a map

\[
E(n)
\]

such that for every admissible integer \(n\),

\[
E(n)=u^{n\bmod m}.
\]

Then

\[
u^n=E(n)
\]

identically, and therefore

\[
\boxed{\delta(n)=0}
\]

for every admissible input.

Such a world is **defect-silent** for this observer.

The statement is elementary, but it gives a concrete design rule:

\[
\boxed{
\text{Do not spend Frobenius hardware on a world whose distinguished probe is
uniform torsion and whose expected response is already determined by the same
finite exponent class.}
}
\]

## 5. Relation to the semiprime theorem

H21-SD1 said that semiprime factor revelation requires different local
coordinate zero masks

\[
Z_p\ne Z_q.
\]

In a defect-silent torsion world,

\[
Z_p=Z_q=\{0,1\}
\]

for every nonexceptional pair.

Therefore semiprime factor exposure is impossible by the defect mechanism.

The silence is not an empirical accident; it is forced by the torsion law.

## 6. FPGA consequence

The \(D=-3\) descriptor should be removed from the expensive world schedule.

Replace it by a tiny divisibility-by-3 precheck:

\[
n\bmod3.
\]

For odd \(n\):

- remainder \(0\): expose factor \(3\);
- remainder nonzero: skip the entire \(D=-3\) Frobenius engine.

The \(D=-4\) root-of-unity descriptor should be omitted entirely from a
defect-factor schedule for odd candidates.

This changes the H21 hardware architecture from a blind list of worlds to a
**world compiler** that simplifies or eliminates provably silent observers.

## 7. Claim boundary

Cyclotomic identities and quadratic characters are classical.

The H21-specific point is the observer-compilation consequence:

\[
\text{world algebra}
\to
\text{torsion test}
\to
\text{defect-silence theorem}
\to
\text{hardware elimination rule}.
\]

No novelty priority is asserted before literature audit.
