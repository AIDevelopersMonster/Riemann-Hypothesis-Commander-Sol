# HATTER-SOL-17 · STATUS

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**State:** active implementation research.  
**Date:** 16 September 2026.

## Closed implementation layer: H17-01

A deterministic canonical golden model for the final H16 `PSL(2,7)` handoff now exists.

Exact verified counts:

```text
|PSL(2,7)| = 168
generating-pair simultaneous-conjugacy orbits = 114
unique five-probe signatures = 114
```

Canonical orbit IDs are independent of Python set/hash iteration: each simultaneous-conjugacy orbit is represented by its lexicographically minimal permutation pair, the 114 representatives are sorted, and IDs `0..113` are assigned in that order.

Source:

`tools/generate_psl27_golden_model.py`

The generator emits a CSV golden table, a complete 114-entry SystemVerilog decoder, and an exhaustive 114-vector decoder testbench.

## Active implementation layer: H17-02

A second generator has been added:

`tools/generate_psl27_port_engine.py`

It removes the H16 demonstration shortcut of supplying five conjugacy-class labels externally.

The generated architecture accepts `A,B` as exact 8-point permutations and computes internally

\[
A,\quad B,\quad AB,\quad AB^{-1},\quad[A,B].
\]

It also emits an exact 168-entry permutation-to-conjugacy-class classifier preserving the split `7A/7B` orientation.

The Python algebraic model was exhaustively checked over all

\[
168^2=28224
\]

ordered port pairs. For every pair, inverse, composition, mixed probe, and commutator values remain in the exact `PSL(2,7)` model and are classifiable.

Local generator result:

```text
PASS: exhaustive Python port-engine algebra over 168^2 ordered port pairs
PASS: classifier and five-probe engine RTL emitted
```

## Current verification gap

The current execution environment has neither `iverilog` nor `verilator`. Therefore the generated SystemVerilog has not yet crossed the HDL-simulation gate in this environment.

This is not marked closed until an HDL simulator reproduces every golden vector.

## Next strike

Build the end-to-end RTL composition

\[
(A,B)
\to
\text{five-probe engine}
\to
\text{class/orientation signature}
\to
\text{114-orbit ROM}
\to
orbit\_id
\]

and generate an exhaustive testbench from all 114 canonical representatives.

After this passes simulation, compare the depth-4 five-probe interface against the depth-14 balanced closed-loop interface as a hardware cost experiment.

## Integer-to-port note

The observation `6=2\cdot3` naturally exposes two ordinary multiplicative ports in `Z`, while primes such as `17` or `53` do not split into two ordinary multiplicative integer ports. They may split into prime-ideal/decomposition branches only after an arithmetic world/extension is specified. This is a legitimate future frontend connecting H07/H10/H14 to the H17 processor, but it is intentionally kept outside the current `PSL(2,7)` core so that the first hardware theorem remains exact and minimal.
