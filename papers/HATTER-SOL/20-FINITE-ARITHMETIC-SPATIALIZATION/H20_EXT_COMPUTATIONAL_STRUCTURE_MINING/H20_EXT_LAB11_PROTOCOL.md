# H20-EXT-LAB-11 · Final practical wheel gate: include divisibility by 13

Status: **PROTOCOL FROZEN BEFORE EXECUTION**

## 1. Purpose

LAB-10 showed C1 survives conditioning modulo

[
2310=2cdot3cdot5cdot7cdot11.
]

LAB-11 adds the next sieve prime:

[
oxed{
30030=2cdot3cdot5cdot7cdot11cdot13.
}
]

This is the final practical wheel enlargement on W<=19.

## 2. Why this is the final wheel gate

At W=17 the complete interval contains only about

[
2^{17}/30030approx4.37
]

numbers per residue class on average.

Further wheel enlargement would make most conditioned cells singleton or empty,
causing the null ensemble to approach the observed function trivially.

Therefore no larger wheel will be interpreted as a stronger structural test at
these widths.

## 3. Exact null ensembles

### Global mod-30030 conditioning

For every W=17,18,19 preserve exact prime counts in each residue class modulo
30030 over the full interval.

Equivalently use one magnitude block of size (2^W).

### Additional local-density checks at W=19

At W=19 additionally preserve the joint tables

[
(nmod30030,lfloor n/262144floor)
]

and

[
(nmod30030,lfloor n/131072floor).
]

These give respectively two and four magnitude blocks while retaining
nontrivial occupancy per residue class.

## 4. Observer

Unchanged:

[
L_W(4)=2^{-2W}sum_{1le|S|le4}widehat f_W(S)^2.
]

The conditional expectation is exact.

## 5. Frozen criterion

C1 survives the final practical wheel gate only if every declared discrepancy
is strictly negative:

1. W=17, global mod30030;
2. W=18, global mod30030;
3. W=19, global mod30030;
4. W=19, block size 262144;
5. W=19, block size 131072.

One nonnegative value fails LAB-11.

## 6. Interpretation boundary

PASS would establish survival after explicitly conditioning all wheel primes

[
2,3,5,7,11,13.
]

FAIL would retain earlier finite results but show that C1 does not survive this
stronger sieve control.

No wheels beyond 30030 will be pursued at W<=19 merely to increase the table.

## 7. Required artifacts

- `lab11_mod30030.csv`;
- `H20_EXT_LAB11_REPORT.md`;
- exact self-test PASS record.
