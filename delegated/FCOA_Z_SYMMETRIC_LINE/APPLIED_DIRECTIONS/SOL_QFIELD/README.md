# SOL-QFIELD

**Scientific direction:** Pauli / particle-antiparticle / reaction channels / history memory / amplitude structure  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** SIXTH TARGET COMPLETE / PREPUBLICATION NUCLEUS  
**Physical verdict:** `ANALOGY ONLY`  
**Mathematical status:** native history-memory chain established through conditional complex linearization  
**Line status:** all structures obtained through the current target remain `1D-CLOSED`

## Permanent separation

SOL-QFIELD separates three target-field structures that must not be conflated:

\[
\boxed{
\text{exchange antisymmetry}
\ne
\text{field/operator anticommutation}
\ne
\text{scattering/annihilation channel structure}.
}
\]

Accordingly, the direct identifications

- `Pauli = FCOA noncommutativity`,
- `particle/antiparticle sign = boson/fermion parity`,
- `annihilation into bosons = operation became commutative`

are rejected.

The surviving first-level match is only

\[
\boxed{
\text{input geometry}
\longrightarrow
\text{typed output-channel class}.
}
\]

## Target 1 — channel taxonomy

A single deterministic FCOA operation cannot faithfully encode a genuinely multichannel reaction support for one fixed incoming pair. Current FCOA also lacks the Hilbert/Fock, CAR/CCR, S-matrix, amplitude, conservation and relativistic structures required for genuine QFT modeling.

Verdict: `ANALOGY ONLY`.

## Target 2 — terminal amplitude lift

Normalized complex amplitudes on terminal channels are wildly underdetermined. More strongly, independent terminal-channel phases are observationally invisible under the current one-step readout, so

\[
\boxed{
QF1\;\text{stochastic weights}
\equiv_{\rm terminal}
QF2\;\text{terminal complex amplitudes}.
}
\]

Operational relative phase requires at least branching, reconvergence, and a coherent path-sum rule. Re-entry alone is not interference.

## Target 3 — native evaluation diamonds

The legacy `oplus` already contains an infinite reflected family of base-only reconvergence diamonds. For every \(n\ge2\),

\[
\boxed{
(P_0\oplus P_n)\oplus P_0
=
P_0\oplus(P_n\oplus P_0)
=
P_{n-1},
}
\]

with distinct intermediate values \(P_n\ne P_{n-1}\).

Current terminal \(E^+,E^*,E^\times\) values cannot participate in such a legacy two-step diamond because no general re-entry rule exists.

An associator diamond is an evaluation/rewrite diamond, not automatically coherent superposition. Relative route phase requires the histories themselves to be retained as mathematical objects.

## Target 4 — minimal finite history memory

Write the intrinsic radial rule types as

\[
L:\ x_0\oplus x_k=x_k,
\qquad
R:\ x_k\oplus x_0=\rho(x_k).
\]

The native diamond histories are \(LR\) and \(RL\).

A cardinality-minimal compositional separator is the 3-element first-role monoid

\[
M_{\rm first}=\{1,\ell,r\},
\qquad
ab=a\quad(a,b\in\{\ell,r\}).
\]

It distinguishes

\[
h(LR)=\ell\ne r=h(RL).
\]

No monoid of fewer than three elements can distinguish them. Thus `H1` is proved: finite/local compositional history memory exists and is `1D-CLOSED`.

However, every group or unitary representation of this idempotent minimal monoid collapses \(\ell,r\) to the identity. The minimal classical memory is not itself a reversible phase carrier.

## Target 5 — minimal reversible history memory

For a group-valued separator, \(LR\ne RL\) requires two noncommuting group elements. Every group of order below six is abelian, while

\[
S_3=\langle s,t\rangle,
\qquad
s=(12),\ t=(23)
\]

gives

\[
st\ne ts.
\]

Therefore the minimal finite reversible history group has exactly six states:

\[
\boxed{G_{\rm hist}=S_3.}
\]

This resolves the reversible-memory trichotomy as `R1`: bounded reversible history memory exists and remains `1D-CLOSED`.

No one-dimensional scalar unitary character can distinguish \(ab\) from \(ba\), because \(U(1)\) is abelian. The standard faithful 2D representation of \(S_3\) does distinguish \(st\) from \(ts\). Thus order-sensitive reversible memory is first visible at a matrix-valued, not scalar-character, level.

## Target 6 — parallel-history linearization

FCOA and the history group do **not** select a coefficient semiring. For every commutative semiring \(K\), formal parallel histories admit the canonical enrichment

\[
K[S_3].
\]

Thus the coefficient choice remains underdetermined.

But once one explicitly requires

1. complex coefficients;
2. linear superposition of parallel histories;
3. bilinear extension of sequential composition,

the universal completion is forced:

\[
\boxed{\mathbb C[S_3].}
\]

Its semisimple decomposition is

\[
\boxed{
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
}
\]

For the route-order residue

\[
\Delta=[st]-[ts],
\]

both scalar irreducible blocks give zero, while the standard matrix block is nonzero:

\[
\boxed{
\Delta\longmapsto(0,0,D),
\qquad D\in M_2(\mathbb C),\ D\ne0.
}
\]

Hence the entire native \(LR/RL\) order information survives only in the genuinely non-Abelian matrix component of the universal complex history algebra.

This is a **conditional linearization theorem**, not a derivation of quantum mechanics or of the complex field from FCOA.

## Current ladder

\[
\boxed{
QF0\;\text{typed support}
<
QF1\;\text{stochastic weights}
\equiv_{\rm terminal}
QF2\;\text{terminal complex weights}
<
QF2.5\;\text{native diamonds}
<
QF3a\text{-}F(3)\;\text{finite irreversible memory}
<
QF3a\text{-}R(6)\;\text{finite reversible }S_3\text{ memory}
<
QF3a\text{-}U(2D)\;\text{faithful unitary memory}
<
QF3b\text{-}C\;\mathbb C[S_3]\text{ conditional linearization}
<
QF4\;\text{physical Hilbert/state/measurement structure}
<
QF5\;\text{Fock/CAR structure}.
}
\]

Everything through `QF3b-C` remains a bounded internal fiber/history algebra over the one-dimensional signed carrier and therefore does not establish emergent spatial dimension.

## Files

- [`SOL_QFIELD_REPORT_v0_1.md`](./SOL_QFIELD_REPORT_v0_1.md) — QFT three-layer separation, channel taxonomy and deterministic-channel no-go.
- [`SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md`](./SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md) — amplitude underdetermination, Terminal Phase Erasure and reconvergence threshold.
- [`SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md`](./SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md) — native radial diamonds, typed-diamond no-go and history-layer obstruction.
- [`SOL_QFIELD_MINIMAL_HISTORY_v0_4.md`](./SOL_QFIELD_MINIMAL_HISTORY_v0_4.md) — minimal 3-state compositional history monoid and unitary-collapse theorem.
- [`SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md`](./SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md) — minimal 6-state reversible separator \(S_3\), scalar-character order no-go and faithful 2D unitary witness.
- [`SOL_QFIELD_LINEARIZATION_v0_6.md`](./SOL_QFIELD_LINEARIZATION_v0_6.md) — coefficient underdetermination, universal complex group-algebra completion and non-Abelian matrix residue.

## Publication decision

The physical/QFT claim remains `ANALOGY ONLY` and must not be upgraded.

The abstract FCOA history-memory material has reached

\[
\boxed{\texttt{PREPUBLICATION NUCLEUS — DO NOT RELEASE YET}.}
\]

Versions 0.3–0.6 now form a coherent theorem chain that may support a separate mathematical note after one more boundary is settled.

## Next strike

Test **positive-functional/state selection** on \(\mathbb C[S_3]\).

The next trichotomy is:

- `P0` — reflection/history invariance leaves a nontrivial convex family of positive normalized functionals; no state is canonically selected;
- `P1` — natural invariance selects only the normalized regular trace/class state, without a pure-state/Born structure;
- `P2` — stronger FCOA constraints select a smaller positive-state family or canonical GNS representation that still detects the matrix order residue.

This `P0/P1/P2` problem is now the sharp SOL-QFIELD frontier.
