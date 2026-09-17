# HATTER-SOL-17 · H17-01 · Canonical PSL(2,7) Golden Model

**Status:** first implementation layer closed at the software/generator level.  
**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`.

## 1. Purpose

HATTER-SOL-16 proved that the five oriented trace probes

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad[A,B]
\]

separate all 114 simultaneous-conjugacy orbits of generating pairs in `PSL(2,7)`, and that no subfamily of at most four probes from the full depth-at-most-four family does so.

H17-01 turns that theorem into a deterministic digital address book.

## 2. Canonical orbit IDs

The H16 certificate used arbitrary representatives produced from Python sets; that is sufficient for theorem verification but is not a stable hardware ABI.

H17 therefore defines canonical orbit IDs as follows.

1. Construct `PSL(2,7)` exactly in its faithful action on `P^1(F_7)`.
2. For every generating pair `(A,B)`, form its simultaneous-conjugacy orbit.
3. Choose the lexicographically smallest pair of permutations in that orbit.
4. Sort the resulting 114 representatives lexicographically.
5. Number them `orbit_id = 0,...,113`.

This makes the decoder table reproducible across runs and independent of hash/set iteration order.

## 3. Five-probe signature

For every canonical representative evaluate

```text
A
B
AB
Ab      # b = B^{-1}
ABab    # [A,B] = A B A^{-1} B^{-1}
```

and map each result to its conjugacy class using

```text
1A -> 000
2A -> 001
3A -> 010
4A -> 011
7A -> 100
7B -> 101
```

The five class codes form a 15-bit signature.

Exact generation gives

```text
group order = 168
generating-pair orbits = 114
unique five-probe signatures = 114
PASS
```

Thus the generated table is collision-free by exact finite computation.

## 4. Orientation output

The commutator class also supplies the hardware orientation state

```text
7A -> Q4 = +1 -> 01
7B -> Q4 = -1 -> 10
other classes -> Q4 = 0 -> 00
```

This preserves the orientation information whose loss was identified exactly in H16.

## 5. Source of truth

The generator is

`tools/generate_psl27_golden_model.py`.

It emits three artifacts:

```text
psl27_114_orbit_signatures.csv
psl27_orbit_rom.sv
tb_psl27_orbit_rom.sv
```

The generated ROM contains all 114 legal signatures and returns `valid=0` for every other 15-bit word.

The generated testbench contains one exact check for every canonical orbit plus an invalid-signature check.

## 6. Local generation audit

The generator was executed successfully on 16 September 2026. SHA-256 hashes of the locally generated artifacts were:

```text
2276ad772ca10d1dda45601e1aad9d37ac0ec458e4ca3787fafcee8d7d1ffb37  psl27_114_orbit_signatures.csv
0959b15847c0d5016ca930bc70e0b8211c464b51b9e5fa0f43b28699daf49694  psl27_orbit_rom.sv
ff4310ec905cde7881b1fde276ca3cc30c93b0d8b0072a5c4730cfe255f8cb80  tb_psl27_orbit_rom.sv
9accb7e6f92547495ac1af28ed07c3669a61638e2805e73975998049b0df303e  generate_psl27_golden_model.py
```

The current execution environment did not contain `iverilog` or `verilator`, so the generated SystemVerilog testbench has not yet been executed here. This is an implementation dependency, not a mathematical gap; HDL simulation remains an explicit H17 gate.

## 7. Next strike

H17-02 removes the remaining H16 shortcut.

The decoder must no longer receive five class labels from outside. It must receive exact hidden ports `(A,B)` and compute

\[
A,\quad B,\quad AB,\quad AB^{-1},\quad[A,B]
\]

internally, followed by class/orientation detection and the 114-orbit lookup.

The first architecture will use the eight-point permutation realization of `PSL(2,7)`. This avoids premature finite-field optimization and gives the shortest path to an exact end-to-end demonstrator.
