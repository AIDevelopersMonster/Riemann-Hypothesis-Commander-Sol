# HATTER-SOL-21 · SEMIPRIME EXPOSURE MECHANISM

Status: **NEXT MATHEMATICAL STRIKE**

## 1. Why semiprimes are now central

H21-LAB-05 gives six-world factor coverage:

\[
100\%\quad\text{for prime squares},
\]

\[
100\%\quad\text{for higher prime powers},
\]

\[
98.356736\%\quad\text{for other composites},
\]

but only

\[
\boxed{64.980040\%}
\]

for distinct semiprimes.

Therefore the dominant unresolved set is not generic compositeness.  It is the
two-prime product

\[
n=pq,\qquad p\ne q.
\]

## 2. Local CRT decomposition

For \(n=pq\), the quadratic algebra decomposes by CRT:

\[
A_n
\cong
A_p\times A_q.
\]

The defect

\[
\delta_W(n)
\]

therefore has independent reductions modulo \(p\) and modulo \(q\).

A gcd witness appears exactly when one defect component vanishes modulo one
prime factor but not the other.

Schematically,

\[
d_W(n)\equiv0\pmod p,
\qquad
d_W(n)\not\equiv0\pmod q
\]

gives

\[
\gcd(n,d_W(n))=p.
\]

Thus factor exposure is controlled by **asymmetry of the two local world
responses**.

This is the mechanism to characterize exactly.

## 3. Target classification

For every world \(W\) and semiprime \(pq\), record the local response type of
each prime factor:

- split/inert/ramified character;
- local Frobenius exponent class;
- whether the global \(n\)-exponent response agrees with the prime-law response
  modulo \(p\);
- same modulo \(q\).

Then classify the pair

\[
(\rho_W(p;q),\rho_W(q;p)).
\]

The central theorem target is an exact iff criterion

\[
\boxed{
W\text{ exposes }p
\iff
\text{specified mismatch between the }p\text{- and }q\text{-local responses}.
}
\]

A symmetric criterion should characterize exposure of \(q\).

## 4. World-pair complementarity

For two worlds \(W_i,W_j\), define the semiprime coverage gain

\[
G_{ij}
=
|E_i\cup E_j|-|E_i|,
\]

where \(E_i\) is the set of semiprimes for which world \(i\) exposes a proper
factor.

The next finite lab should compute the full \(6\times6\) complementarity
matrix and compare it with arithmetic descriptors of the discriminant pair.

The objective is to explain why the optimized factor order begins

\[
\boxed{-11\to-19\to-7}
\]

rather than merely observe it.

## 5. Hardware significance

If the exposure criterion depends only on a compact local descriptor, a
scheduler may choose the next world adaptively from information already
obtained from previous handles.

That would turn H21 from static world ordering into genuine adaptive
factor tomography.
