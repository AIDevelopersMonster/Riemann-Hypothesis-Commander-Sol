# HATTER-SOL-16 · STATUS

**Research status:** CLOSED at v1.0 publication candidate.  
**Implementation status:** handed off to HATTER-SOL-17.  
**Branch:** `research/hatter-sol-16-nonsolvable-ports`.

## Final publication files

- `HATTER_SOL_16_EN_v1.0.md`
- `HATTER_SOL_16_RU_v1.0.md`
- `FINAL_CORRECTIONS_v1.0.md`
- `FINAL_PUBLICATION_AUDIT_v1.0.md`

## Frozen principal engineering result

For generating pairs in `PSL(2,7)`, the five oriented trace probes

\[
A,\quad B,\quad AB,\quad AB^{-1},\quad[A,B]
\]

separate all 114 simultaneous-conjugacy orbits, with maximum primitive word depth four. No subfamily of at most four probes from the complete depth-at-most-four candidate family suffices.

The implementation block handed to H17 is

\[
\boxed{
\text{PORT WORD ENGINE}
\to
\text{ORIENTED 3D CHANNEL}
\to
\text{5-PROBE SIGNATURE}
\to
\text{114-ORBIT DECODER}.
}
\]

## Publication threshold

Crossed. No further theorem strike is required for H16 before publication. Remaining tasks are editorial/typesetting only: final PDF rendering, visual audit, bibliographic normalization, Zenodo deposition, DOI insertion, and branch merge/archive according to the series publication workflow.
