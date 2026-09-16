# H17-05 · LUT-free structural PSL(2,7) processor layer

## Purpose

H16 demonstrated that a proved finite tomography signature can be decoded in ordinary HDL, but its proof-of-concept accepted already classified probes and used a small demonstration LUT.  H17-05 removes the remaining element-level lookup stage from the real processor path.

The target data path is now

```text
raw 24-bit permutations A,B
 -> structural PSL(2,7) membership
 -> permutation word arithmetic
 -> structural conjugacy-class engine
 -> robust trace-word signature
 -> finite orbit decoder
```

Only the final `signature -> canonical orbit_id` map remains a ROM/case table.  Membership in the group and conjugacy-class recognition are computed from the input itself.

## 1. Structural membership in PSL(2,7)

The eight symbols are the points of `P^1(F_7) = {0,1,...,6,infinity}`.  A 24-bit value stores the images of these eight points as eight 3-bit fields.

First require the eight images to be pairwise distinct.  This is the `S_8` permutation check.

A projective transformation is determined by the images of `0,1,infinity`.  To test that an arbitrary permutation is induced by an element of `PGL(2,7)`, H17-05 checks preservation of the five cross-ratios associated with `x=2,...,6`:

```text
CR(x,0;1,infinity) = 1-x mod 7.
```

Written without division, each test is a product equality of homogeneous determinants in `F_7`.  Exhaustive enumeration of all `8! = 40320` permutations gives exactly

```text
PGL(2,7) accepted = 336.
```

To distinguish `PSL(2,7)` from the other projective coset, define the projective triple orientation

```text
chi(det(v_a,v_b) det(v_b,v_c) det(v_c,v_a)),
```

where `chi` is the quadratic character of `F_7^*`.  Applied to the image of the base triple `(0,1,infinity)`, the positive sign selects exactly

```text
PSL(2,7) accepted = 168.
```

The accepted 168 permutations agree exactly with the independent determinant-one matrix construction of `PSL(2,7)`.

Therefore raw input membership no longer requires a 168-entry LUT.

## 2. Structural six-class channel

For a valid group element `g`, permutation powers determine four classes immediately:

```text
ord(g)=1 -> 1A
ord(g)=2 -> 2A
ord(g)=3 -> 3A
ord(g)=4 -> 4A.
```

For `ord(g)=7`, the permutation has one fixed point and one seven-cycle.  Choose any point `x` in that cycle and compute

```text
s(g,x) = chi(det(v_x,v_gx) det(v_gx,v_g^2x) det(v_g^2x,v_x)).
```

Exhaustive verification proves that the sign is independent of the chosen cycle point and gives exactly

```text
7A -> +1   (24 elements)
7B -> -1   (24 elements).
```

Thus all six conjugacy classes are determined by finite computation rather than element lookup.

## 3. Exhaustive certificate

`certificates/psl27_structural_class_engine_certificate.py` checks all 40320 permutations and all 168 group elements.

It certifies:

```text
S8 permutations checked = 40320
PGL(2,7) accepted        =   336
PSL(2,7) accepted        =   168
class counts             = 1,21,56,42,24,24
```

and exact agreement of the structural class engine with the independently constructed conjugacy classes.

## 4. RTL handoff

`tools/generate_psl27_structural_processor.py` emits

```text
psl27_structural_classify.sv
```

with no 168-entry class ROM.

`tools/generate_psl27_robust8.py` has been switched to instantiate this structural classifier for both raw inputs and all eight computed observer words.

The preferred H17 processor path is therefore

```text
A,B
 -> cross-ratio + orientation membership
 -> inverse/compose word engine
 -> order + order-seven orientation classifier
 -> 8 x 3-bit signature
 -> one-erasure projection
 -> canonical 114-orbit decoder.
```

## 5. What remains a ROM and why

The final orbit decoder remains finite memory.  This is not a substitute for the mathematical computation of the probes: it is the canonical naming map from a proved finite sufficient statistic to one of 114 simultaneous-conjugacy orbits.

A later H17 layer may investigate logic minimization of that decoder, but eliminating it is not required to call the preceding pipeline computational: every group operation and every class measurement before it is now derived from the raw ports.

## Verification boundary

The structural formulas have been exhaustively verified in Python.  The emitted SystemVerilog has not yet crossed an external simulator/synthesis gate in the present environment.  No timing, area, or board claim is made at H17-05.
