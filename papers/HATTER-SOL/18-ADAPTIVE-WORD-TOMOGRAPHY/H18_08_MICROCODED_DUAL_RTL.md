# HATTER-SOL-18 · H18-08
# Canonical microcoded controller and dual-RTL target

**Status:** architecture frozen; implementation/certification in progress.

## 1. Objective

H18-07 proved that the exact H18-06 adaptive strategy is hardware-realizable, but the first hardwired controller pays for 308 query states as a large combinational decode network.

The H18-08 objective is to preserve the exact mathematical strategy while changing only its representation:

\[
\boxed{\text{hardwired decision decode}\;\longrightarrow\;\text{canonical microprogram}}
\]

The reference implementation remains sequential. A fully combinational all-at-once realization is not a release requirement because H17-LAB-02 demonstrated that such a topology can become impractical even at smoke-test simulation scale.

## 2. Canonical node numbering

The H18-07 strategy contains

\[
308=69+239
\]

query nodes:

- 69 nodes while the one-erasure budget is still available;
- 239 nodes after the erasure has already occurred.

H18-08 renumbers them as

\[
0,\ldots,68 \quad\text{pre-erasure},
\]

\[
69,\ldots,307 \quad\text{post-erasure}.
\]

Terminal states are encoded without ROM records:

\[
308+k,\qquad 0\le k<114
\]

means generating orbit \(k\),

\[
422=\mathrm{REJECT},
\qquad
423=\mathrm{FAULT}.
\]

Hence a node address remains only 9 bits.

This renumbering is semantics-preserving: every H18-06 class transition and every allowed erasure transition is remapped bijectively.

## 3. Microprogram decomposition

The exact controller program is stored as four small tables.

### Query-word selector

There are 308 query nodes and only 24 distinct word labels.

\[
308\times5=1540\text{ bits}.
\]

### Class-transition table

Every query has six possible successful class outcomes and every target is a 9-bit node address.

\[
308\times6\times9=16632\text{ bits}.
\]

This table is naturally addressable by

\[
6\,\mathrm{node\_id}+\mathrm{class\_code}.
\]

### Erasure-transition table

Only the 69 pre-erasure nodes need a legal erasure edge.

\[
69\times9=621\text{ bits}.
\]

For post-erasure nodes, a second erasure goes directly to FAULT.

### Word-descriptor table

Each of 24 distinct words has an 8-bit letter code plus a 3-bit length.

\[
24\times11=264\text{ bits}.
\]

Therefore the complete explicit controller-program payload is

\[
\boxed{
1540+16632+621+264=19057\text{ bits}
}
\]

before vendor-specific memory packing.

This is a representation count, not a claim about a particular FPGA BRAM count.

## 4. Sequential execution model

The H18-08 reference machine uses:

1. two raw PSL(2,7) membership checks;
2. one shared word engine;
3. one shared member-class engine;
4. synchronous microprogram lookups;
5. one 9-bit program counter / node ID.

The first word letter is loaded directly rather than multiplied by the identity. Thus a word of length \(L\) needs \(L-1\) actual permutation compositions.

The H18-07 worst path used at most 19 identity-based letter compositions. Without changing any query choice, H18-08 reduces that arithmetic count to at most

\[
\boxed{19-5=14}
\]

on a five-attempt worst path, because every attempted query saves its first identity composition.

This optimization is independent of the microcode compression and does not change the exact H18-06 observation bound.

## 5. Dual RTL contract

One Python generator must emit from the same exact H18-06 certificate:

- SystemVerilog RTL;
- VHDL-2008 RTL;
- identical microprogram contents;
- identical 197-state regression vectors;
- a machine-readable microcode JSON summary.

The SystemVerilog path must pass the complete

\[
197\times5=985
\]

fault-schedule regression.

The VHDL path must compile, elaborate and run the same vector contract in GHDL before H18-08 is closed.

## 6. Synthesis boundary

Three different measurements must not be conflated:

1. hierarchy-expanded generic gate count after memory mapping;
2. memory-preserving Yosys structure;
3. FPGA-family mapping with inferred block/distributed memories.

H18-08 will report each separately when available.

No LUT, FF, BRAM, Fmax, power or board claim is made until the corresponding target-specific synthesis/place-and-route evidence exists.

## 7. Release criterion

H18-08 closes only when:

- canonical remapping is generated deterministically from the H18-06 exact strategy;
- SystemVerilog passes all 985 cases;
- VHDL passes the same behavioral contract;
- both RTL variants synthesize successfully;
- microprogram bit counts are generated, not handwritten;
- CI artifacts preserve the emitted RTL, ROM images/packages and logs.

After that, H18 can move to publication assembly while later hardware layers attack word-prefix caching and target-FPGA implementation.
