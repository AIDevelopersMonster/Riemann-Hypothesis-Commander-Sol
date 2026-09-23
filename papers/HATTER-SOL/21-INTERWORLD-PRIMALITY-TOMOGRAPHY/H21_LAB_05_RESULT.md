# HATTER-SOL-21 · H21-LAB-05 RESULT

Status: **CI REPRODUCED / FACTOR-TOMOGRAPHY POSITIVE RESULT**

Run:

\`35597694491\`

Range:

\[
3\le n<2^{19},\qquad n\text{ odd}.
\]

Composite inputs:

\[
\boxed{218754}.
\]

Prime proper-divisor witness failures:

\[
\boxed{0}.
\]

## 1. Six-world factor exposure

Worlds:

\[
-7,\ 5,\ -3,\ -11,\ 13,\ -19.
\]

At least one proper divisor is exposed for

\[
\boxed{
185063/218754
=
84.598682\%.
}
\]

Unresolved by all six worlds:

\[
\boxed{33691}.
\]

At least two distinct proper-divisor values are exposed for

\[
\boxed{115444}
\]

composites.

At least two distinct prime factors occur in the union of world witnesses for

\[
\boxed{103450}
\]

composites.

The complete distinct-prime support is recovered for

\[
\boxed{33432}
\]

composites.

Thus different arithmetic worlds are genuinely complementary as factor
observers in this finite laboratory.

## 2. Individual world yields

| world | proper-divisor hits | fraction |
|---|---:|---:|
| \(D=-7\) | 128051 | 58.536530% |
| \(D=5\) | 132455 | 60.549750% |
| \(D=-3\) | 87380 | 39.944412% |
| \(D=-11\) | 138261 | **63.203873%** |
| \(D=13\) | 133644 | 61.093283% |
| \(D=-19\) | 127125 | 58.113223% |

No single world accounts for the six-world union.

The best individual world is \(D=-11\), but its coverage is only

\[
63.203873\%,
\]

well below the six-world coverage

\[
84.598682\%.
\]

## 3. Arithmetic-class dependence

| factor shape | count | any factor | fraction |
|---|---:|---:|---:|
| prime square | 127 | 127 | **100%** |
| distinct semiprime | 90180 | 58599 | **64.980040%** |
| higher prime power | 44 | 44 | **100%** |
| other composite | 128403 | 126293 | **98.356736%** |

The difficult class is therefore not prime powers but **distinct semiprimes**.

For distinct semiprimes, the six worlds expose at least one factor in only

\[
64.980040\%
\]

of the declared range.

They expose both distinct prime factors somewhere across the world family for

\[
29288
\]

of the \(90180\) semiprimes.

This identifies the next mathematical target sharply.

## 4. Frozen-order marginal gain

For the old order

\[
-7\to5\to-3\to-11\to13\to-19
\]

the new factor hits per step are

\[
128051,\ 37342,\ 5851,\ 4968,\ 4240,\ 4611.
\]

Thus later worlds still reveal factors not exposed by earlier worlds.

This is direct finite evidence of interworld complementarity.

## 5. Exact static order optimization

All

\[
6!=720
\]

static orders were evaluated exactly through the 64 possible world-hit masks.

The optimal order for **first proper-divisor revelation** is

\[
\boxed{
-11\to-19\to-7\to13\to5\to-3.
}
\]

Using unresolved penalty \(7\), the mean cost over all composites is

\[
\boxed{2.262066}
\]

world evaluations.

Conditioned on inputs for which the six-world family exposes some factor, the
mean first-factor handle is

\[
\boxed{1.399518}.
\]

The worst static order is

\[
-3\to13\to-11\to-7\to5\to-19
\]

with mean all-composite cost

\[
\boxed{2.797773}.
\]

Hence ordering alone changes the finite expected factor-revelation cost by

\[
\boxed{
2.797773-2.262066=0.535707
}
\]

world evaluations.

## 6. Observer-dependent optimal trajectory

This is the most important conceptual result of LAB-05.

The earlier primality-certification laboratory strongly favored the sequence
starting with

\[
D=-7.
\]

The factor-revelation objective instead favors

\[
D=-11
\]

as the first world.

Therefore there is no observer-independent "best next world" even inside this
frozen finite family.

The optimal trajectory depends on the target observable:

\[
\boxed{
\text{best world for compositeness certification}
\ne
\text{best world for factor revelation}.
}
\]

This is a concrete H21 instance of observer-dependent revelation time.

## 7. FPGA consequence

H21-HW-01 should therefore not hardwire one world order.

It must support a programmable world schedule.

At minimum the scheduler needs two frozen profiles:

### certification profile

optimized for earliest COMPOSITE certificate;

### factor profile

optimized for earliest proper-divisor witness.

The arithmetic core can be identical in both cases.

Only the world-descriptor schedule changes.

## 8. Claim boundary

This is an exact finite result for:

- the six declared quadratic worlds;
- odd \(n<2^{19}\);
- the declared Frobenius-defect gcd observer.

It is not a general-purpose factorization theorem and no asymptotic efficiency
claim is made.

The strongest open mathematical question is now why the distinct-semiprime
class is the resistant class and which arithmetic relation between its two
prime factors controls exposure by a given world.
