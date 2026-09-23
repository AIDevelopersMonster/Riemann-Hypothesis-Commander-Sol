# HATTER-SOL-19 · DIALOGUE_TZ
## Boolean Geometry of Mathematical Presentations

You are continuing HATTER-SOL-19 as the leading researcher.

Do not restart H17/H18 from scratch.  H18 is a frozen parent result and supplies
the experimental seed.  The new programme begins at H18-12/H18-13.

## Scientific target

Develop a rigorous comparison theory for finite mathematical presentations
that are realized as Boolean circuits and then mapped to physical hardware.

The core distinction is:

\[
\text{task semantics}
\neq
\text{mathematical presentation}
\neq
\text{execution architecture}
\neq
\text{technology realization}.
\]

The programme must keep these four layers separate.

## Claim discipline

1. Never identify FPGA area with absolute mathematical complexity.
2. Never infer a circuit lower bound from one synthesis run.
3. Never call two presentations equivalent without specifying E0/E1/E2.
4. H17↔H18 robust comparison is E1 at the fault layer.
5. H18 direct/prefix/Nielsen/flat experiments should be constructed at E0.
6. A presentation-preserving lower bound is not an unrestricted Boolean lower
   bound unless this is separately proved.
7. NOFIT is capacity evidence only; it has no routed timing.
8. Cyclone-V comparisons must report DSP with ALM.
9. Preserve reproducible tool/device/constraint metadata.

## Immediate theorem programme

### H19-01
Formalize adaptive presentation, residual programme, Booleanization discipline,
temporal realization, and full spatial realization.

### H19-02
Derive exact construction-level size/depth identities or upper bounds for a
compiled adaptive DAG with shared observer circuits.

### H19-03
Define structural quantities that may predict spatialization cost:
residual-program count, observer-support cost, branch overlap, and shared
sub-DAG volume.

### H19-04
Build multiple E0-equivalent H18 restricted-12 presentations and compare them
under one fixed compilation/FPGA protocol.

### H19-05
Introduce a flattened-semantic control to estimate how much of the source
presentation survives synthesis.

### H19-06
Seek a parameterized family with a provable separation between adaptive query
complexity and presentation-preserving spatial circuit complexity.

## Experimental rule

Every hardware experiment must answer a theoretical question.  Do not add a
device merely because it is available.

## Publication threshold

H19 does not cross publication threshold from empirical FPGA data alone.

Publication requires at least one of:

- a nontrivial structural theorem on temporal/spatial realization;
- a provable separation family;
- a rigorously defined invariant with demonstrated predictive value across a
  controlled E0-equivalent presentation family.
