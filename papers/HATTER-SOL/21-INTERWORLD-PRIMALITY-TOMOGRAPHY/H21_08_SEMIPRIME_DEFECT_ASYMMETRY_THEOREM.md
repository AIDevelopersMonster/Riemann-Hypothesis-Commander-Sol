# HATTER-SOL-21 · SEMIPRIME DEFECT-ASYMMETRY THEOREM

Status: **EXACT THEOREM LAYER / FINITE VALIDATION REQUIRED**

## 1. Setup

Let

\[
n=pq,
\qquad
p\ne q
\]

be distinct odd primes.

Fix a quadratic world

\[
W=(B,C,\Delta),
\qquad
\Delta=B^2+4C,
\]

and assume the nonexceptional squarefree case

\[
pq\nmid 2C\Delta,
\qquad
\gcd(pq,2C\Delta)=1.
\]

Let

\[
A_r
=
\mathbf F_r[x]/(x^2-Bx-C)
\]

for \(r=p,q\).

Write the global Frobenius defect in the basis \(1,x\) as

\[
\delta_W(n)
=
(d_0,d_1)
\in
(\mathbb Z/n\mathbb Z)^2.
\]

Under CRT,

\[
\delta_W(n)
\longleftrightarrow
\big(
\delta_{p\leftarrow q},
\delta_{q\leftarrow p}
\big)
\in
A_p\times A_q.
\]

## 2. Cross-Frobenius residual

For a prime \(r\), put

\[
\chi_r
=
\left(\frac{\Delta}{r}\right)\in\{\pm1\},
\]

and

\[
e_r=\frac{1-\chi_r}{2}\in\{0,1\}.
\]

Let \(\tau\) be quadratic conjugation,

\[
\tau(x)=B-x.
\]

The prime Frobenius law in \(A_r\) is

\[
x^r=\tau^{e_r}(x).
\]

For \(n=pq\), reduction of the global defect modulo \(p\) satisfies

\[
\boxed{
\delta_W(pq)\bmod p
=
\tau^{e_p}
\left(
x^q-\tau^{e_q}(x)
\right)
\in A_p.
}
\]

Symmetrically,

\[
\boxed{
\delta_W(pq)\bmod q
=
\tau^{e_q}
\left(
x^p-\tau^{e_p}(x)
\right)
\in A_q.
}
\]

### Proof

Modulo \(p\),

\[
x^{pq}
=
(x^p)^q
=
\left(\tau^{e_p}(x)\right)^q
=
\tau^{e_p}(x^q),
\]

because \(\tau\) is an algebra automorphism.

The expected response for \(n=pq\) is determined by

\[
\left(\frac{\Delta}{pq}\right)
=
\chi_p\chi_q,
\]

hence equals

\[
\tau^{e_p+e_q}(x).
\]

Subtracting gives

\[
\tau^{e_p}(x^q)
-
\tau^{e_p+e_q}(x)
=
\tau^{e_p}
\left(
x^q-\tau^{e_q}(x)
\right).
\]

The \(q\)-formula is symmetric. QED.

## 3. Full local pass criterion

The global defect vanishes modulo \(p\) iff

\[
\boxed{
x^q
=
\tau^{e_q}(x)
\quad\text{in }A_p.
}
\]

Thus the local fate modulo \(p\) is governed by the **other prime \(q\)**.

Likewise,

\[
\boxed{
\delta_W(pq)\equiv0\pmod q
\iff
x^p
=
\tau^{e_p}(x)
\quad\text{in }A_q.
}
\]

This is the exact cross-prime response law.

## 4. Coordinate zero masks

Write

\[
\delta_W(pq)\bmod p
=
(d_{0,p},d_{1,p}),
\]

\[
\delta_W(pq)\bmod q
=
(d_{0,q},d_{1,q}).
\]

Define the coordinate zero masks

\[
Z_p
=
\{j\in\{0,1\}:d_{j,p}=0\},
\]

\[
Z_q
=
\{j\in\{0,1\}:d_{j,q}=0\}.
\]

The implemented factor observer computes

\[
g_j=\gcd(n,d_j),
\qquad j=0,1.
\]

## Theorem H21-SD1 — exact semiprime factor-exposure criterion

In the nonexceptional squarefree case,

\[
\boxed{
W\text{ exposes a proper divisor of }pq
\iff
Z_p\ne Z_q.
}
\]

More precisely,

\[
\boxed{
g_j=p
\iff
j\in Z_p\setminus Z_q,
}
\]

and

\[
\boxed{
g_j=q
\iff
j\in Z_q\setminus Z_p.
}
\]

### Proof

For \(n=pq\),

\[
\gcd(pq,d_j)=p
\]

iff

\[
p\mid d_j
\quad\text{and}\quad
q\nmid d_j.
\]

This is exactly

\[
j\in Z_p\setminus Z_q.
\]

The statement for \(q\) is symmetric. Therefore some proper divisor is exposed
iff the two coordinate-zero masks differ. QED.

## Corollary H21-SD2 — two factors from one world

One world exposes both prime factors \(p\) and \(q\) iff the two coordinates
split the factors in opposite directions:

\[
\boxed{
Z_p\setminus Z_q\ne\varnothing
\quad\text{and}\quad
Z_q\setminus Z_p\ne\varnothing.
}
\]

With two coordinates this means, up to exchange,

\[
Z_p=\{0\},
\qquad
Z_q=\{1\}.
\]

Then

\[
\gcd(n,d_0)=p,
\qquad
\gcd(n,d_1)=q.
\]

## Corollary H21-SD3 — full-local-pass asymmetry is sufficient, not necessary

If

\[
\delta_W(n)\equiv0\pmod p
\]

but

\[
\delta_W(n)\not\equiv0\pmod q,
\]

then \(Z_p=\{0,1\}\) and \(Z_q\ne\{0,1\}\), so a proper divisor is exposed.

However the converse is false in general: factor exposure may occur with

\[
Z_p,Z_q
\]

both proper nonempty subsets.

Therefore the correct mechanism is **coordinate defect asymmetry**, not merely
whole-vector pass/fail asymmetry.

## 5. Observer dependence

The theorem depends on the chosen basis coordinates because the hardware
observer takes gcds of \(d_0,d_1\) separately.

An invertible change of basis over \(\mathbb Z/n\mathbb Z\) can alter which
individual coordinates vanish modulo \(p\) or \(q\).

Therefore H21 distinguishes:

- the basis-invariant full local defect;
- the basis-dependent coordinate-gcd factor observer.

This is not a flaw. It is another exact instance of observer dependence.

## 6. Immediate consequences

For a fixed semiprime \(pq\), each world supplies a pair

\[
(Z_p(W),Z_q(W)).
\]

The six-world factor fingerprint is therefore a finite code over the four
possible masks

\[
\varnothing,\{0\},\{1\},\{0,1\}.
\]

A world is useful exactly when its two masks differ.

World complementarity means that different discriminants produce mask
asymmetry on different semiprime populations.

## 7. Next finite validation

H21-LAB-06 must verify, for every distinct semiprime \(pq<2^{19}\) and every
declared world:

1. the cross-Frobenius residual formulas;
2. the exact equivalence
   \[
   \text{proper divisor exposed}\iff Z_p\ne Z_q;
   \]
3. the exact identification of whether \(p\), \(q\), or both are exposed;
4. the frequency of all \(4\times4\) mask pairs;
5. the \(6\times6\) semiprime complementarity matrix.

Any mismatch closes the theorem claim until repaired.
