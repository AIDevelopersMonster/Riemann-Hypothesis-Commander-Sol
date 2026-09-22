# HATTER-SOL-21 · SHARED-CLOCK LOCK EQUIVALENCE

Status: **EXACT CLOCK-ARITHMETIC LAYER**

## 1. Shared clock divisor

For a fixed nonexceptional quadratic world W, let

\[
h_p=h_W(p),
\qquad
h_q=h_W(q),
\]

and

\[
g=\gcd(h_p,h_q).
\]

From the local-order bounds,

\[
h_p\mid p^2-1,
\qquad
h_q\mid q^2-1.
\]

Therefore

\[
\boxed{
g\mid p^2-1
\quad\text{and}\quad
g\mid q^2-1.
}
\]

Hence

\[
p^2\equiv q^2\equiv1\pmod g.
\]

## Theorem H21-CL1 — reciprocal lock equivalence

For every such pair,

\[
\boxed{
p\equiv q\pmod g
\iff
pq\equiv1\pmod g.
}
\]

Likewise,

\[
\boxed{
p\equiv -q\pmod g
\iff
pq\equiv-1\pmod g.
}
\]

### Proof

If p is congruent to q modulo g, then pq is congruent to q squared, hence to 1 modulo g.

Conversely, if pq is congruent to 1 modulo g, multiply by q. Since q squared is congruent to 1 modulo g, one gets p congruent to q modulo g.

The negative case is identical. QED.

## 2. Consequence for LAB-13

The two previously tested events

\[
p\equiv q\pmod g
\]

and

\[
pq\equiv1\pmod g
\]

are not independent diagnostics.

They are the same event on the shared Lucas clock.

Thus the exact arithmetic lock variable is naturally

\[
\boxed{
\sigma_g(p,q)=pq\bmod g\in\{+1,-1,\text{other}\}.
}
\]

## 3. Trivial-lock contamination

For odd primes:

- if g=1, both congruences are vacuous;
- if g=2, plus one and minus one coincide modulo 2, and every odd pair is trivially locked.

Therefore a meaningful clock-lock test must separate

\[
\boxed{g\le2}
\]

from

\[
\boxed{g>2}.
\]

The raw LAB-13 equality frequency is not interpretable as a nontrivial synchronization rate until this contamination is removed.

## 4. Refined lock classes

For g>2, define:

\[
L_+=\{pq\equiv1\pmod g\},
\]

\[
L_-=\{pq\equiv-1\pmod g\},
\]

\[
L_0=\{pq\not\equiv\pm1\pmod g\}.
\]

These three classes are disjoint.

The next laboratory tests whether same-mask attraction and negative conditional coupling concentrate in L-plus, L-minus, or neither.

## 5. Claim boundary

H21-CL1 is elementary modular arithmetic once the local-order divisibility is known.

Its role is to remove a duplicated diagnostic and expose the correct nontrivial shared-clock lock variable.
