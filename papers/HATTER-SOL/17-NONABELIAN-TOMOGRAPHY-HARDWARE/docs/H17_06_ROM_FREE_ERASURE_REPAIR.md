# HATTER-SOL-17 · H17-06 · ROM-free erasure repair and canonical orbit fingerprint

## 1. Goal

H17-05 removed the 168-entry element/class lookup table. The remaining large finite table in the robust8 pipeline was the projected-signature-to-`orbit_id` decoder.

H17-06 separates two questions that had previously been conflated:

1. **recover the mathematical orbit invariant** after one known probe erasure;
2. **attach an arbitrary external integer name** `0..113` to that orbit.

The second operation is not mathematically necessary for the processor core.

## 2. Robust8 signature

The optimal one-erasure observer is

```text
AAB
Abb
AAAB
Abbb
AABAb
AAbAb
ABABB
ABaBB
```

Each coordinate is one of the six oriented conjugacy classes

```text
1A, 2A, 3A, 4A, 7A, 7B,
```

encoded in three bits. Hence the full observer signature is a 24-bit word.

On the 114 generating simultaneous-conjugacy orbits these full signatures are pairwise distinct. Therefore the full 24-bit signature itself is a canonical finite fingerprint of the generating orbit relative to the fixed ordered observer family.

No `orbit_id` ROM is needed to preserve the mathematical classification.

## 3. Known one-erasure repair problem

Suppose coordinate `e` is known to be missing. The remaining seven class coordinates must determine simultaneously:

- whether the state belongs to the generating domain;
- if generating, the missing class value;
- hence the complete 24-bit canonical fingerprint.

The exact finite domain contains:

```text
114 generating signatures
 66 distinct non-generating signatures
```

and H17-04 already proves `d_gen/gen >= 2` and `d_gen/non >= 2`. Thus each one-coordinate deletion preserves exact generating-orbit separation and generating/non-generating separation.

## 4. Exact decision-tree optimization

For each erased coordinate independently, H17-06 considers decision trees whose internal nodes ask for the class value of one surviving coordinate. Leaves output either

```text
G + missing-class
```

or

```text
NON.
```

An exact dynamic programme enumerates every reachable state subset and remaining-coordinate set. The optimization objective is lexicographic:

1. minimum worst-case query depth;
2. among those trees, minimum number of internal decision nodes.

The exact results are:

| erased probe | realizable projected states | optimal depth | internal nodes |
|---|---:|---:|---:|
| `AAB`   | 178 | 4 | 41 |
| `Abb`   | 178 | 4 | 41 |
| `AAAB`  | 180 | 4 | 43 |
| `Abbb`  | 180 | 4 | 43 |
| `AABAb` | 178 | 4 | 30 |
| `AAbAb` | 180 | 4 | 39 |
| `ABABB` | 180 | 4 | 39 |
| `ABaBB` | 178 | 4 | 30 |

Therefore

```text
four surviving class queries are necessary and sufficient
```

for every erasure position within this decision-tree model.

The eight depth-optimal trees contain `306` internal decision nodes in total before logic synthesis/factoring across erasure modes.

Certificate:

`certificates/psl27_erasure_repair_tree_certificate.py`

## 5. ROM-free processor interface

The preferred H17 core can now expose

```text
orbit_fingerprint[23:0]
fingerprint_valid
```

instead of requiring an internal 114-entry integer-ID ROM.

The pipeline becomes

```text
raw A,B permutations
 -> structural PSL(2,7) membership
 -> exact permutation word arithmetic
 -> structural six-class computation
 -> eight-class robust signature
 -> depth-4 erasure repair / admissibility tree
 -> repaired 24-bit canonical orbit fingerprint
```

Every stage above is generated as combinational logic. There is no element ROM and no orbit ROM in this mathematical core.

A legacy adapter may still map the 24-bit fingerprint to the historical `orbit_id=0..113` numbering when an external software/API interface requires it. Such a numbering table is metadata, not part of the mathematical computation.

## 6. HDL generator and adversarial test

Generator:

`tools/generate_psl27_romfree_repair.py`

It emits:

```text
psl27_robust8_repair.sv
psl27_robust8_romfree_core.sv
tb_psl27_robust8_repair.sv
```

The generated testbench deliberately overwrites the erased 3-bit coordinate with invalid value `3'b111`. The repair network must reconstruct the original class using only surviving coordinates. Thus a passing simulation cannot be explained by accidentally reading the supposedly erased value.

The test set contains

```text
114 * 8 = 912 generating erasure states
 66 * 8 = 528 non-generating erasure states
```

for a total of 1,440 exact erasure cases.

## 7. Status boundary

The exact finite/tree certificate is closed.

The previous H17-05 structural classifier and flat robust8 decoder have already passed Icarus Verilog in GitHub Actions. The new ROM-free repair RTL has been added to the same CI pipeline; its independent HDL simulation result must be recorded separately once the corresponding workflow run completes.

No synthesis resource or timing claim is made at this layer.
