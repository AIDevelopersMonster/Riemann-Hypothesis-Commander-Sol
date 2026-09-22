# HATTER-SOL-21 · H21-LAB-13 RESULT

Status: **CI REPRODUCED / SIMPLE SHARED-ORDER HYPOTHESIS REJECTED**

Run:

\`35717107255\`

## 1. Shared-order strength

On the broad common core

\[
|D|\le255,\qquad pq<2^{18},\qquad p,q>255,
\]

the high shared-order quartile has, on average,

\[
\boxed{
-0.041858
}
\]

lower same-mask probability than the low shared-order quartile.

Only

\[
\boxed{
11.47\%
}
\]

of world/stratum rows show a positive high-minus-low same-mask lift.

Therefore

\[
\boxed{
\text{larger shared clock fraction}
\not\Rightarrow
\text{more reciprocal same-mask synchronization}.
}
\]

The simple shared-clock-gcd hypothesis is rejected.

## 2. Duplicate diagnostic discovered

The events

\[
p\equiv q\pmod g
\]

and

\[
pq\equiv1\pmod g
\]

were observed to be identical.

This led to H21-CL1, proved exactly in the next layer.

## 3. Why raw same-mask lift is insufficient

Conditioning on a clock event changes both:

- the joint mask law;
- the marginal mask distribution.

Therefore a higher or lower raw same-mask rate does not by itself determine
the sign or magnitude of conditional coupling

\[
K=Q-G.
\]

The clock mechanism must be studied through conditional marginals and
conditional coupling together.
