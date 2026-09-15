# HATTER-SOL-16 · A5 Mahler separation down to mu = 23/5

## Status

**Closed theorem layer.**  This sharpens the first rigorous A5 scalar Mahler threshold from `mu >= 21/4` to

\[
\boxed{\mu\ge\frac{23}{5}=4.6}.
\]

The proof is finite, exact, and certificate-backed.

---

## Setup

Let \(\rho_3:A_5\to SO(3)\) be the real three-dimensional irreducible representation with

\[
\chi_3(3A)=0,\qquad
\chi_3(5A)=\frac{1+\sqrt5}{2},\qquad
\chi_3(5B)=\frac{1-\sqrt5}{2}.
\]

For a generating pair \((A,B)\) write

\[
H_{A,B}(\theta,\phi)=
 e^{i\theta}\rho_3(A)+e^{-i\theta}\rho_3(A)^{-1}
 +e^{i\phi}\rho_3(B)+e^{-i\phi}\rho_3(B)^{-1}
\]

and, for \(\mu>4\),

\[
M_{A,B}(\mu)=\frac1{(2\pi)^2}
\int_0^{2\pi}\int_0^{2\pi}
\log\det(\mu I-H_{A,B}(\theta,\phi))\,d\theta\,d\phi.
\]

The complete generating-pair enumeration gives 2280 ordered generating pairs, 38 simultaneous-conjugacy orbits, and commutator classes only in \(3A,5A,5B\).

---

## Exact moment expansion

Define the balanced torus moments

\[
S_{2m}(A,B)=\frac1{(2\pi)^2}\iint \operatorname{Tr} H_{A,B}(\theta,\phi)^{2m}\,d\theta\,d\phi.
\]

Odd balanced moments vanish.  With

\[
t=\mu^{-2},
\]

we have

\[
M_{A,B}(\mu)
=3\log\mu-
\sum_{m\ge1}\frac{S_{2m}(A,B)}{2m}t^m.
\]

Every exact moment lies in \(\mathbf Q(\sqrt5)\).  The certificate computes all moments through order 40 for all 38 simultaneous-conjugacy orbits and proves that the resulting moment sequences collapse to

\[
\boxed{6\text{ types for }3A,\qquad4\text{ for }5A,\qquad4\text{ for }5B.}
\]

The universal fourth-moment identity remains

\[
S_4=84+8\chi_3([A,B]).
\]

---

## Theorem 16.E · uniform scalar Mahler class separation

For every generating pair \((A,B)\) in \(A_5\), the scalar determinant observer separates the three possible commutator classes throughout the half-line

\[
\mu\ge\frac{23}{5}.
\]

More precisely,

\[
\boxed{
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu)
\qquad
\forall\mu\ge\frac{23}{5}.
}
\]

Here the notation means that the inequality holds uniformly between **every** moment type whose commutator lies in the indicated class.

### Proof architecture

For two moment types \(i,j\), divide the Mahler difference by \(t^2\).  The exact terms through \(m=20\) give a polynomial

\[
Q_{ij}(t)=t^{-2}\sum_{m=2}^{20} c_m t^m,
\qquad
c_m=-\frac{S_{2m}^{(i)}-S_{2m}^{(j)}}{2m}.
\]

The only irrationality is \(\sqrt5\), enclosed exactly by

\[
\frac{22360679}{10^7}<\sqrt5<\frac{22360680}{10^7}.
\]

Since \(\|H_{A,B}\|\le4\),

\[
|S_{2m}^{(i)}-S_{2m}^{(j)}|\le6\,16^m.
\]

Therefore, after division by \(t^2\), the omitted tail \(m\ge21\) satisfies

\[
|R_{ij}(t)|
\le
\frac{3}{21}\,
\frac{16^{21}t^{19}}{1-16t}.
\]

On the theorem range

\[
0\le t\le \frac{25}{529},
\]

we have \(16t<1\).  Exact rational interval Horner evaluation on 128 equal rational subintervals proves positive lower margins for all cross-class type pairs.  The smallest normalized margins are approximately

\[
3.2360679
\]

for \(3A-5A\), and

\[
0.8033839842
\]

for \(5B-3A\).

Hence the ordering is strict on the entire half-line. ∎

---

## Certificate

`certificates/a5_mahler_separation_mu_23_over_5_certificate.py`

The certificate:

1. constructs \(A_5\) exactly as even permutations of five letters;
2. enumerates all 2280 ordered generating pairs;
3. reduces them to 38 simultaneous-conjugacy orbits;
4. computes exact balanced moments through order 40 in \(\mathbf Q(\sqrt5)\);
5. verifies the `6/4/4` moment-type collapse;
6. performs only rational interval assertions for the final separation theorem.

No floating-point quantity is used in a proof assertion.

---

## Boundary evidence versus theorem status

Independent numerical quadrature at \(\mu=4\) still shows the same class ordering with visible gaps across all 38 orbit representatives.  This is **evidence only**, not part of Theorem 16.E.

The present analytic tail bound uses \(\|H\|\le4\), and therefore degenerates exactly at \(t=1/16\).  The remaining barrier is no longer the finite moment computation; it is to prove a strict uniform spectral gap

\[
\sup_{\theta,\phi}\|H_{A,B}(\theta,\phi)\|<4
\]

for every generating pair, with a quantitative lower bound uniform over the 38 orbit types.  Such a gap would restore geometric convergence at \(\mu=4\) and should permit the same exact moment method to close the natural boundary.

This is the next H16 strike.