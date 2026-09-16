# HATTER-SOL-17 · H17-04 Optimal Joint One-Erasure Code

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**Status:** exact finite theorem/certificate layer; HDL realization still open.  
**Date:** 16 September 2026.

## 1. Problem

The H16 five-probe observer

\[
(A,B,AB,AB^{-1},[A,B])
\]

separates the 114 simultaneous-conjugacy orbits of generating pairs in
`PSL(2,7)`, and its 114 signatures are disjoint from all 66 five-probe
signatures realized by non-generating pairs.

However, its minimum generating-orbit Hamming distance is only one, so loss of
one probe can destroy canonical orbit reconstruction.

H17-04 asks for the smallest cyclic trace-word observer, with primitive word
length at most five, satisfying simultaneously

\[
d_{\rm gen/gen}\ge2,
\qquad
d_{\rm gen/non}\ge2.
\]

The first condition preserves orbit reconstruction after deletion of any one
known coordinate.  The second preserves generating/non-generating admissibility
after the same deletion.

## 2. Exact candidate family

Cyclically reduced words in `A,a,B,b`, modulo cyclic rotation and inversion,
of length at most five give exactly

\[
51
\]

candidate trace coordinates.

The finite state model has

- 114 generating simultaneous-conjugacy orbits;
- 83 non-generating simultaneous-conjugacy orbits;
- 66 distinct non-generating signatures in the full 51-coordinate observer.

The joint distance conditions reduce to 13,965 binary covering inequalities.

## 3. Optimal channel count

A binary MILP solved to zero MIP gap gives

\[
\boxed{m_{\min}=8}.
\]

Thus no seven-probe subfamily of the 51 depth-`<=5` trace coordinates can
simultaneously provide one-erasure orbit recovery and one-erasure admissibility.

One exact optimal family is

\[
\boxed{
AAB,
Abb,
AAAB,
Abbb,
AABAb,
AAbAb,
ABABB,
ABaBB
}.
\]

Direct finite verification gives

\[
\boxed{d_{\rm gen/gen}=2},
\qquad
\boxed{d_{\rm gen/non}=2}.
\]

Hence deletion of any one known probe coordinate leaves both tasks exact.

## 4. Depth profile is also optimal

Among all eight-probe joint codes, a second exact MILP minimizes the number of
length-five words.  The optimum is

\[
\boxed{4}.
\]

With cardinality eight and exactly four depth-five coordinates fixed, minimizing
total primitive word length gives

\[
\boxed{34}.
\]

Therefore an optimal depth profile is

\[
\boxed{(3,3,4,4,5,5,5,5)}.
\]

The displayed eight-probe family realizes this profile and total length.

This is the current hardware-optimal trace-word architecture under the frozen
candidate class: eight observer channels, maximum primitive depth five, four
channels at depth five, total primitive word length 34.

## 5. H16 backward-compatible optimum

If the original H16 channels

\[
A,B,AB,Ab,ABab
\]

must remain physically exposed, then eight total channels are impossible.

There are 46 remaining candidate coordinates.  Exhaustive enumeration of all

\[
\binom{46}{3}=15180
\]

three-coordinate extensions shows that every such eight-channel extension
violates at least one joint distance constraint.

A nine-channel extension exists:

\[
\boxed{
A,
B,
AA,
AB,
Ab,
ABB,
Abb,
ABab,
ABaBB
}.
\]

It satisfies

\[
d_{\rm gen/gen}=d_{\rm gen/non}=2.
\]

Only one of its four added coordinates has depth five.  Thus the conservative
hardware migration path is substantially cheaper in word depth than simply
adding four arbitrary depth-five channels.

Consequently

\[
\boxed{m_{\min}^{\rm H16-frozen}=9}.
\]

## 6. Architecture consequence

H17 now has three exact observer tiers:

1. **5-channel minimal decoder** — exact orbit/admissibility with no erasure tolerance;
2. **8-channel robust redesign** — globally minimal one-erasure trace observer;
3. **9-channel compatible extension** — minimal one-erasure observer if the H16 five-channel pin/interface contract is frozen.

The preferred research architecture is the eight-channel core.  The nine-channel
variant is the preferred migration architecture for hardware that already
implements the H16 interface.

## 7. Certificate

Executable source:

`certificates/psl27_joint_one_erasure_code_certificate.py`

The certificate reconstructs `PSL(2,7)`, its generating/non-generating orbit
states, the complete 51-coordinate depth-`<=5` cyclic trace family, the MILP
constraints, and direct Hamming-distance checks.  It also exhaustively excludes
all three-probe extensions of the frozen H16 core.

## 8. Verification boundary

The mathematical/computational finite layer is closed for this candidate class.
The following remain implementation gates:

- generate the eight-channel word engine and erasure-aware decoder;
- generate the nine-channel H16-compatible variant;
- HDL simulation against all 114 generating states and all 66 non-generating signature states for every single erased coordinate;
- synthesis and timing/resource measurement on a real FPGA flow.

No HDL-simulation or synthesis claim is made here.
