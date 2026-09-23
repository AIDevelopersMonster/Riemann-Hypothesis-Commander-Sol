# HATTER-SOL-21 · FIXED-STRATUM CLOCK-LOCK DIAGNOSTICS

Status: **ACTIVE MECHANISM TEST**

## 1. Purpose

H21-LAB-12 showed that quadratic-character mixing explains only a small
fraction of the observed coupling.

The residual object is

\[
K_s
\]

inside a fixed stratum

\[
s\in\{++, +-, --\}.
\]

The next candidate mechanism is shared Lucas-clock arithmetic.

## 2. Local clocks

For every nonexceptional prime \(p\), let

\[
h_p=h_W(p)
\]

be the multiplicative order of the distinguished quadratic-algebra generator.

For a pair \(p,q\), define

\[
\boxed{
g_{pq}=\gcd(h_p,h_q).
}
\]

The shared-order fraction is measured by

\[
\boxed{
r_{pq}
=
\frac{\log_2 g_{pq}}
{\log_2 \min(h_p,h_q)}
}
\]

when the denominator is nonzero.

This is a scale-free measure of how much of the smaller local clock is shared.

## 3. Explicit phase-lock events

Three natural reciprocal congruence events are tested:

\[
\boxed{
E_+(p,q): p\equiv q\pmod{g_{pq}},
}
\]

\[
\boxed{
E_-(p,q): p\equiv -q\pmod{g_{pq}},
}
\]

and the control

\[
\boxed{
E_\times(p,q): pq\equiv1\pmod{g_{pq}}.
}
\]

These are not assumed theorems.

They are candidate arithmetic explanations for excess same-mask synchronization.

## 4. Fixed-stratum evaluation

All statistics are reported separately inside

\[
++,\quad+-,\quad--.
\]

For each world/stratum and for each lock event \(E\), compare:

- event frequency;
- same-mask probability with \(E\);
- same-mask probability without \(E\);
- conditional coupling
  \[
  K_E=Q_E-G_E;
  \]
- conditional coupling outside \(E\).

For shared-order strength, compare the top and bottom quartiles of \(r_{pq}\).

## 5. Decision rule

### Support for a clock-lock mechanism

A candidate is interesting only if strong negative-\(K_s\) worlds show:

- non-negligible event frequency;
- substantially elevated same-mask probability under the event;
- more negative conditional coupling under the event;
- behavior stable across more than one world.

### Rejection

If lock events are too rare, weak, or inconsistent, then shared clock gcd is
not the right explanatory variable.

The next object must then include the full mask phase sets, not just clock
orders.

## 6. Non-claim

Clock gcd and simple congruence locks are exploratory descriptors.

No theorem is claimed unless an exact implication for the zero-mask system is
derived.
