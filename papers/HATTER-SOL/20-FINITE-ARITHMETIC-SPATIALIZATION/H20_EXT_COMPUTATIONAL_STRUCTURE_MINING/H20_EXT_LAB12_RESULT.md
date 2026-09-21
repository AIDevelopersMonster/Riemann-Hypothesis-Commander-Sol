# H20-EXT-LAB-12 · Conditioning-resolution crossover hold-out result

Status: **FAIL / CROSS-WIDTH CROSSOVER LAW NOT VALIDATED**

Run: GitHub Actions `35582985892`.

## Frozen candidate

The W=19 pattern to be tested on fresh widths W=20,21 was

[
(+,-,-)
]

for discrepancies under respectively 1, 2 and 4 equal magnitude blocks,
all with mod-30030 residue conditioning.

That is:

[
Delta_{W,1}ge0,qquad
Delta_{W,2}<0,qquad
Delta_{W,4}<0.
]

## Fresh result

### W=20

[
Delta_{20,1}=+0.000175016706,
]

[
Delta_{20,2}=+0.0000183088724,
]

[
Delta_{20,4}=-0.0000733202526.
]

Pattern:

[
(+,+,-),
]

not the frozen candidate.

### W=21

[
Delta_{21,1}=+0.000197790761,
]

[
Delta_{21,2}=+0.0000684026533,
]

[
Delta_{21,4}=-0.0000125225603.
]

Again:

[
(+,+,-).
]

Therefore

[
oxed{	ext{CRITERION PASS = FALSE}.}
]

## Interpretation

The conditioning-resolution sign crossover is real as a finite phenomenon, but
the W=19 threshold does not transport unchanged to W=20,21.

The minimum tested power-of-two block count producing negative discrepancy is:

- W=19: 2;
- W=20: 4;
- W=21: 4.

This sequence is recorded only descriptively.

No recurrence is fitted and no new threshold law is proposed.

## Decision

The conditioning-crossover candidate is closed as a validated cross-width law.

Further block-count mining would be post-hoc model fitting and is not justified
without an independent theoretical reason.
