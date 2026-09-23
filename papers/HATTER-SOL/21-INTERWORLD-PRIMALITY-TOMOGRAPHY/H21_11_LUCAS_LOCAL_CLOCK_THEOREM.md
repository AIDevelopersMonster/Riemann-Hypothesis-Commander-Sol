# HATTER-SOL-21 · LUCAS LOCAL CLOCK AND WORLD-QUALITY COMPILER

Status: **EXACT THEOREM LAYER / QUALITY METRIC EXPLORATORY**

## 1. Classical Lucas reduction

Fix a quadratic world

\[
W=(B,C,\Delta),
\qquad
\Delta=B^2+4C,
\]

with algebra

\[
A_R=R[x]/(x^2-Bx-C).
\]

Define

\[
U_0=0,\qquad U_1=1,
\]

\[
\boxed{
U_{m+1}=B\,U_m+C\,U_{m-1}.
}
\]

Equivalently this is the classical Lucas sequence

\[
U_m(B,-C).
\]

## Theorem H21-LC1 — exact power reduction

For every \(m\ge1\),

\[
\boxed{
x^m=U_m x+C\,U_{m-1}.
}
\]

### Proof

For \(m=1\) the formula is immediate.  If it holds at \(m\), then

\[
x^{m+1}
=
U_mx^2+C\,U_{m-1}x
\]

and using

\[
x^2=Bx+C
\]

gives

\[
x^{m+1}
=
C\,U_m
+
(BU_m+CU_{m-1})x
=
C\,U_m+U_{m+1}x.
\]

QED.

## 2. Cross-prime Lucas residual

Let

\[
n=pq,
\qquad
p\ne q
\]

be distinct odd primes in the nonexceptional regime

\[
\gcd(pq,2C\Delta)=1.
\]

Put

\[
\chi_r=\left(\frac{\Delta}{r}\right)\in\{\pm1\},
\qquad
\varepsilon_r=\frac{1-\chi_r}{2}.
\]

The H21-SD cross residual before the outer \(p\)-conjugation is

\[
r_{p\leftarrow q}
=
x^q-\tau^{\varepsilon_q}(x).
\]

By H21-LC1,

\[
\boxed{
r_{p\leftarrow q}
=
a_q+b_qx
}
\]

with

\[
\boxed{
a_q=C\,U_{q-1}-\varepsilon_q B,
}
\]

\[
\boxed{
b_q=U_q-\chi_q.
}
\]

The global defect modulo \(p\) is

\[
\delta_W(pq)\bmod p
=
\tau^{\varepsilon_p}(r_{p\leftarrow q}).
\]

## 3. Exact coordinate-zero rules

Since

\[
\tau(a+bx)
=
(a+Bb)-bx,
\]

the \(x\)-coordinate of the defect vanishes modulo \(p\) iff

\[
\boxed{
U_q\equiv\chi_q\pmod p.
}
\]

This condition is independent of \(\chi_p\).

For the constant coordinate:

### split local world at p

If

\[
\chi_p=+1,
\]

then

\[
\boxed{
d_{0,p}=0
\iff
C\,U_{q-1}
\equiv
\frac{1-\chi_q}{2}B
\pmod p.
}
\]

### inert local world at p

If

\[
\chi_p=-1,
\]

then

\[
d_{0,p}=a_q+Bb_q.
\]

Using

\[
U_{q+1}=BU_q+CU_{q-1},
\]

we obtain

\[
\boxed{
d_{0,p}=0
\iff
U_{q+1}
\equiv
\frac{1+\chi_q}{2}B
\pmod p.
}
\]

Thus the complete local coordinate zero-mask is determined by three neighboring
Lucas values

\[
U_{q-1},U_q,U_{q+1}
\]

modulo \(p\), together with \(\chi_p,\chi_q\).

## 4. Local arithmetic clock

Assume

\[
p\nmid C\Delta.
\]

Multiplication by \(x\) on the basis \((1,x)\) is

\[
J_W
=
\begin{pmatrix}
0&C\\
1&B
\end{pmatrix}.
\]

Because

\[
\det J_W=-C\not\equiv0\pmod p,
\]

the matrix is invertible.

Define the local world clock

\[
\boxed{
h_W(p)
=
\operatorname{ord}_{GL_2(\mathbf F_p)}(J_W\bmod p).
}
\]

Equivalently, \(h_W(p)\) is the multiplicative order of the distinguished
element \(x\) in the quadratic residue algebra.

Then

\[
x^{m+h_W(p)}=x^m
\]

for all \(m\), so

\[
(U_{m-1},U_m,U_{m+1})\pmod p
\]

is periodic with period dividing \(h_W(p)\).

## Theorem H21-LC2 — local signature clock

Let \(f_W\) be a period of the quadratic character

\[
m\mapsto\left(\frac{\Delta}{m}\right)
\]

on admissible odd integers.

Then the local zero-mask

\[
Z_{p\leftarrow q}(W)
\]

depends only on

\[
\boxed{
q\bmod \lambda_W(p),
\qquad
\lambda_W(p)=\operatorname{lcm}(h_W(p),f_W).
}
\]

Thus each prime factor \(p\) carries a world-dependent finite arithmetic clock,
and the other prime \(q\) is observed through its phase on that clock.

## 5. Clock-mismatch factor theorem

Define the two-bit Lucas local signature

\[
L_W(p\leftarrow q)
=
Z_{p\leftarrow q}(W).
\]

H21-SD1 becomes

\[
\boxed{
W\text{ exposes a proper factor of }pq
\iff
L_W(p\leftarrow q)
\ne
L_W(q\leftarrow p).
}
\]

This is the exact form of **cross-clock asymmetry**.

The factors themselves are identified by which coordinate bits occur in one
local mask and not the other.

## 6. Order bounds

For nonexceptional \(p\):

### split case

If

\[
\chi_p=+1,
\]

then

\[
A_p\cong\mathbf F_p\times\mathbf F_p
\]

and therefore

\[
\boxed{
h_W(p)\mid p-1.
}
\]

### inert case

If

\[
\chi_p=-1,
\]

then

\[
A_p\cong\mathbf F_{p^2}.
\]

The norm of \(x\) is

\[
N(x)=-C.
\]

Hence

\[
x^{p+1}=-C.
\]

If

\[
t_p=\operatorname{ord}_{\mathbf F_p^\times}(-C),
\]

then

\[
\boxed{
h_W(p)\mid t_p(p+1).
}
\]

In particular,

\[
h_W(p)\mid p^2-1.
\]

These bounds make exact clock computation practical without brute-force
iteration through all algebra states.

## 7. Torsion-world interpretation

For the silent \(D=-3\) world,

\[
h_{-3}(p)=6
\]

for every nonexceptional odd prime.

For the silent \(D=-4\) world,

\[
h_{-4}(p)=4.
\]

The clock is therefore uniformly tiny and synchronized with the character
period, which forces the expected response and actual power response to
coincide.

This explains the torsion-world no-go as a degenerate local-clock regime.

## 8. What "world quality" can and cannot mean

A large clock order alone does **not** prove that a world is a good factor
observer.

Factor exposure depends on the mismatch

\[
L_W(p\leftarrow q)
\ne
L_W(q\leftarrow p),
\]

not on either clock length separately.

Therefore H21 rejects a one-number theorem of the form

\[
\text{larger }h_W(p)\Rightarrow\text{better world}.
\]

A legitimate finite world-quality score must measure **cross-clock signature
diversity**.

For a finite prime population \(\mathcal P\), candidate descriptors include:

\[
Q_{\rm ord}(W)
=
\operatorname{mean}_{p\in\mathcal P}\log h_W(p),
\]

and the stronger pairwise score

\[
\boxed{
Q_{\rm asym}(W)
=
\Pr_{p\ne q}
[
L_W(p\leftarrow q)\ne L_W(q\leftarrow p)
].
}
\]

The latter is exactly the semiprime factor-exposure rate in the
nonexceptional population.

## 9. World compiler

The resulting compiler pipeline is

\[
\boxed{
(B,C,\Delta)
\to
\text{torsion elimination}
\to
h_W(p)\text{ clock model}
\to
\text{Lucas signature model}
\to
\text{cross-clock asymmetry score}
\to
\text{hardware schedule}.
}
\]

The expensive quadratic exponentiation core is no longer the only possible
implementation.  A Lucas recurrence/matrix core computes exactly the
coordinates needed by the defect observer.

## 10. Prior-art boundary

Lucas sequences, quadratic finite-field representations, and Frobenius
probable-prime tests are classical.

H21 does not claim those ingredients.

The H21 target is the composed observer statement:

\[
\boxed{
\text{local Lucas clocks}
\to
\text{coordinate zero masks}
\to
\text{cross-clock asymmetry}
\to
\text{factor revelation}
\to
\text{world scheduling / hardware compilation}.
}
\]
