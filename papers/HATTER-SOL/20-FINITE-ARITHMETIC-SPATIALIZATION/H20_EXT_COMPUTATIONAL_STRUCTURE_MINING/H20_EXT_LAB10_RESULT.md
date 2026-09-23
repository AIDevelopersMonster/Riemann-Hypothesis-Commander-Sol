# H20-EXT-LAB-10 · Extended-wheel result: mod 2310

Status: **PASS / C1 SURVIVES EXPLICIT DIVISIBILITY-BY-11 CONDITIONING**

Run: GitHub Actions `35582639425`.

## Frozen condition

Prime labels were randomized only inside cells preserving

[
(nmod2310,lfloor n/Bfloor)
]

with

[
Bin{65536,32768,16384},
qquad
Win{17,18,19}.
]

All nine exact conditioned deltas had to remain negative.

## Exact result

| W | B | delta |
|---:|---:|---:|
| 17 | 65536 | -0.000508585309 |
| 17 | 32768 | -0.000746030370 |
| 17 | 16384 | -0.000822283818 |
| 18 | 65536 | -0.000521769292 |
| 18 | 32768 | -0.000608836108 |
| 18 | 16384 | -0.000609940463 |
| 19 | 65536 | -0.000295536413 |
| 19 | 32768 | -0.000327627546 |
| 19 | 16384 | -0.000342767528 |

Hence

[
oxed{Delta_{W,B}^{(2310)}<0}
]

for every predeclared case.

## Interpretation

Adding the next wheel prime 11 reduces the size of the deficit but does not
remove it.

Therefore C1 is not explained merely by the omission of divisibility by 11 from
the earlier mod-210 conditioned null models.

## Non-claim

This does not show survival under arbitrarily large wheels.

At fixed W, sufficiently fine residue conditioning eventually makes blocks so
small that the null ensemble approaches the observed function itself.
