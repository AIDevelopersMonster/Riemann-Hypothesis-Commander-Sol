# H17-LAB-02 — pure-RTL mathematical processor

## What this laboratory is

H17-LAB-01 implements H17 as a deliberately slow, sequential, table-driven
reference machine. Its value is transparency and a stable golden I/O contract.

H17-LAB-02 implements the stronger architecture already proved in H17-06,
H17-07 and H17-08:

    LAB-01:
    finite mathematical classification
        -> sequential table searches

    LAB-02:
    group theorem + observer code
        -> structural logic
        -> canonical 24-bit fingerprint

The experiment is pure RTL first. No FPGA vendor, part, development board,
synthesis suite or pin map is selected here.

## Mathematical map

The fixed robust observer family is:

    AAB
    Abb
    AAAB
    Abbb
    AABAb
    AAbAb
    ABABB
    ABaBB

Each word is mapped to one of the six oriented conjugacy classes
1A, 2A, 3A, 4A, 7A, 7B, encoded by three bits.

The ordered eight-tuple is a 24-bit fingerprint F(A,B). On the 114 generating
simultaneous-conjugacy orbits these fingerprints are pairwise distinct.

## Why closure changes the RTL

A naive design can run complete PSL membership plus class logic on every
derived word. H17-08 proves this is redundant.

Once A and B are members of PSL(2,7), group closure implies that every word in
A, B and their inverses is also a member. Therefore the hardware contract is:

    2 x membership-only for raw A,B
    8 x class-only for derived words

The shared word datapath is the H17-07 optimum: 14 permutation compositions,
maximum composition depth 3.

## Why the backend is ROM-free

LAB-01 searches a 114-entry table and attaches a historical integer orbit ID
0..113. That integer is only an external label.

The robust 24-bit signature already uniquely identifies the generating orbit.
For one known erased coordinate, H17-06 gives an exact decision tree using
surviving coordinates only. Every erasure position has worst-case query depth
4.

Thus the mathematical result is:

    repaired_signature[23:0]
    fingerprint_valid

No 114-entry orbit-ID ROM is required in the mathematical core.

## rtl/h17_lab02_core.sv

The first block is psl27_robust8_engine. It is generated from the audited
H17-08 source and contains:

    structural membership for A and B
    inverse A and B
    shared 14-compose word DAG
    eight class-only decoders
    24-bit raw signature

The second block is psl27_robust8_repair. It is generated from H17-06 and is an
exact ROM-free decision network.

For mode 1..8, LAB-02 physically overwrites the erased field by 3'b111 before
repair. For example mode 1 overwrites bits 23:21. The corresponding repair
tree never queries those bits.

## Why mode 0 still invokes a repair tree

With no visible erasure, observed_signature equals raw_signature. LAB-02 still
uses the erasure-0 tree internally as a generating-domain validator.

That tree ignores coordinate 0, reconstructs it from the other seven
coordinates and accepts only a valid generating projection. Therefore an
accepted mode-0 result must reproduce the original full fingerprint without a
114-entry generating-orbit table.

## Status compatibility with LAB-01

    0 = A or B is not a PSL(2,7) member
    1 = PSL members but non-generating / rejected projected signature
    2 = unique valid generating fingerprint
    4 = illegal mode

LAB-01 also had a theoretical status 3 for multiple flat-table matches.
The H17 robust code excludes this case, so the ROM-free tree has no status-3
branch.

## Testbench

tb/tb_h17_lab02_vectors.sv reads the same vector rows as LAB-01:

    A B mode status orbit_id raw observed repaired

It verifies status, raw signature, erased observation and repaired signature.

The legacy orbit_id column is deliberately ignored. Removing this arbitrary
integer lookup is part of the experiment.

## Windows PowerShell

From the H17_LAB_02_RTL_PROCESSOR directory run:

    .\tools\test_lab02.ps1 -Set quick

The script performs:

    generate H17-08 closure-aware SystemVerilog
    generate H17-06 ROM-free repair SystemVerilog
    compile with Icarus SystemVerilog
    compare against 1,796 LAB-01 golden vectors

After quick passes:

    .\tools\test_lab02.ps1 -Set full

This uses all 29,911 vectors.

## What a full PASS will establish

For the complete published finite golden-vector domain, LAB-02 will have the
same externally observable mathematical results as LAB-01 for:

    status
    raw fingerprint
    erased observation
    repaired fingerprint

while replacing the sequential table implementation by the structural
closure-aware, ROM-free architecture.

That still makes no claim about a physical FPGA. Hardware selection begins only
after the pure-RTL equivalence gate is closed.
