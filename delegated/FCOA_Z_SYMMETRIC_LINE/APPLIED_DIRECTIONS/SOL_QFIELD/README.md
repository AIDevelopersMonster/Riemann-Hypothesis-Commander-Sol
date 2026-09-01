# SOL-QFIELD

**Scientific direction:** exchange / reaction channels / history memory / operator structure  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FOURTEENTH TARGET COMPLETE / PUBLICATION CANDIDATE / PROOF CORE STABLE  
**Physical verdict:** `ANALOGY ONLY`  
**Robust mathematical core:** FCOA root-comb → Parikh collisions → minimal reversible `S3` history → generator-independent `K3 ⊔ K3` collision graph → canonical six-edge tight frame on `M2(R)`  
**Conditional side branch:** involutive/Coxeter history realization → direct Clifford pair → algebraic `CAR_1`  
**Line status:** `1D-CLOSED`

---

## Permanent physical separation

SOL-QFIELD keeps distinct

\[
\boxed{
\text{exchange antisymmetry}
\ne
\text{field/operator anticommutation}
\ne
\text{scattering/annihilation channel structure}.
}
\]

Accordingly, the identifications

- `Pauli = FCOA noncommutativity`,
- `particle/antiparticle sign = statistics parity`,
- `annihilation into bosons = commutativity`

remain rejected.

Current FCOA still lacks the structures needed for a genuine QFT model: physical Hilbert/Fock space, CAR/CCR fields, S-matrix dynamics, Lorentz/Poincare structure, conservation laws, amplitudes/cross-sections and a measurement postulate.

---

# Robust theorem chain

## 1. Native radial reconvergence

For non-root points,

\[
L:x\mapsto x_0\oplus x=x,
\qquad
R:x\mapsto x\oplus x_0=\rho(x).
\]

For any finite history word `w` whose trajectory remains away from the root,

\[
\boxed{
F_w(x_k)=\rho^{\#_R(w)}(x_k).
}
\]

Hence the endpoint depends only on the number of `R` letters.

Equivalently, the native root-comb reconvergence classes are exactly the binary **Parikh fibers**

\[
\Psi(w)=(\#_L(w),\#_R(w)).
\]

The familiar associator diamond `LR/RL` is merely the first nontrivial member.

---

## 2. Minimal finite and reversible history memory

The shortest route pair

\[
LR\ne RL
\]

can be separated compositionally by a cardinality-minimal 3-element irreversible monoid.

If history memory is required to be reversible, its generator images must not commute. Every group of order below six is Abelian, while `S3` is not. Thus the cardinality-minimal reversible history group has size

\[
\boxed{|G_{\rm hist}|=6}
\]

and may be realized by

\[
\boxed{G_{\rm hist}=S_3.}
\]

This is a finite internal history fiber and remains `1D-CLOSED`.

---

## 3. Conditional complex linearization

The FCOA/history data do **not** choose a coefficient semiring. For any commutative semiring `K`, one may form `K[S3]`.

If one explicitly requires

1. complex coefficients;
2. linear superposition of parallel histories;
3. bilinear extension of sequential composition,

then the universal complex linear envelope is

\[
\boxed{A=\mathbb C[S_3].}
\]

Classically,

\[
\boxed{
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
}
\]

This is a conditional algebraic completion, not a derivation of complex quantum mechanics from FCOA.

---

## 4. Order-sensitive matrix sector

For the Coxeter realization used in the first exploration, the shortest route residue

\[
\Delta=st-ts
\]

satisfies

\[
\Delta^*\Delta=3e_{\rm std},
\]

where `e_std` is the central projector onto the standard `M2(C)` block. Thus

\[
J_\Delta=Ae_{\rm std}\cong M_2(\mathbb C).
\]

The later root-comb theorem makes the robust statement stronger: **every native Parikh-collision residue in every cardinality-minimal noncommuting `S3` realization has equal-parity endpoints, hence vanishes in both scalar irreducible blocks and lies entirely in the standard block.**

Before complexification the corresponding real block is

\[
\boxed{
J_{\mathbb R}\cong M_2(\mathbb R).
}
\]

---

## 5. Global state selector no-go and canonical sector state

On the full complex group algebra, positivity + normalization + history-conjugation invariance leave a nontrivial simplex of states. Therefore there is no unique global state selected by current FCOA data:

\[
\boxed{\texttt{P0-GLOBAL}.}
\]

On the standard matrix block, however, conjugation invariance selects the normalized trace

\[
\boxed{
\tau_{\rm ord}(M)=\frac12\operatorname{Tr}(M).
}
\]

Its tracial GNS geometry is

\[
\langle X,Y\rangle
=
\frac12\operatorname{Tr}(X^*Y).
\]

This is a canonical finite-dimensional state/metric on the selected algebraic sector, not yet a physical quantum-state postulate.

---

# Main robust result: Parikh-collision theorem

Let

\[
h:\{L,R\}^*\twoheadrightarrow S_3
\]

be **any** cardinality-minimal reversible history morphism with

\[
h(L)h(R)\ne h(R)h(L).
\]

For distinct `g,g' ∈ S3`, define `g ~P g'` iff there exist Parikh-equivalent histories `w,w'` with

\[
h(w)=g,
\qquad
h(w')=g'.
\]

Then

\[
\boxed{
g\sim_P g'\iff \operatorname{sgn}(g)=\operatorname{sgn}(g').}
\]

Hence the collision graph is exactly

\[
\boxed{
\Gamma_P
=
K_3[A_3]
\sqcup
K_3[S_3\setminus A_3].
}
\]

### Conceptual proof

- Parikh-equivalent words have the same image parity.
- `LR` and `RL` give one nontrivial same-Parikh collision because their images do not commute.
- Collision is stable under equal left/right contexts:

\[
g\sim_P g'\Longrightarrow xgy\sim_P xg'y.
\]

- The relative element of the seed collision is a nonidentity member of

\[
[S_3,S_3]=A_3.
\]

- The two nonidentity 3-cycles are conjugate, so context transport sends the seed to every pair of distinct same-parity elements.

Thus the result is structural rather than an accidental six-element enumeration.

---

## Sharp finite depth

A supplementary exhaustive verifier checks all

\[
18
\]

ordered noncommuting generator pairs of `S3`.

All six collision edges occur by history depth at most

\[
\boxed{5,}
\]

and this is sharp as a universal bound:

- 12 ordered generator pairs close by depth 4;
- 6 ordered transposition/transposition pairs require depth 5.

Verifier:

[`verify_parikh_collision_s3.py`](./verify_parikh_collision_s3.py)

---

# Canonical route-frame theorem

Under the real standard representation

\[
\rho:S_3\to O(2),
\]

the three even vertices

\[
\rho(e),\rho((123)),\rho((132))
\]

form a centered equilateral triangle, and the three transposition matrices form a second centered equilateral triangle.

Their two real spans are orthogonal in the normalized Hilbert-Schmidt metric

\[
\langle X,Y\rangle_{\mathbb R}
=
\frac12\operatorname{Tr}(X^{\mathsf T}Y).
\]

For every collision edge define

\[
E_{g,g'}
=
\frac{\rho(g)-\rho(g')}{\sqrt3}.
\]

The six unordered normalized route residues form a unit-norm tight frame for the full real standard block:

\[
\boxed{
\sum_{\{g,g'\}}
\langle X,E_{g,g'}\rangle E_{g,g'}
=
\frac32X
\qquad
(X\in M_2(\mathbb R)).
}
\]

Thus

\[
\boxed{S_{\rm route}=\frac32 I.}
\]

and

\[
\boxed{
X=\frac23\sum_{\{g,g'\}}
\langle X,E_{g,g'}\rangle E_{g,g'}.
}
\]

This is generator-independent inside the minimal `S3` history layer.

The robust canonical object is therefore **the six-line route frame / metric**, not a privileged Pauli basis.

---

# Qualified Clifford/CAR side branch

The hostile audit found a real canonicity defect in the original v0.9 wording.

Cardinality minimality selects the group size and allows `S3`, but it does **not** force the primitive generator images to be two transpositions. Noncommuting generating pairs may have order type

\[
(2,2),\quad(2,3),\quad(3,2).
\]

For a mixed `(3,2)` realization, direct depth-two/depth-three normalized route residues can satisfy

\[
X^2=Y^2=e_{\rm std},
\qquad
\{X,Y\}=e_{\rm std},
\]

rather than anticommuting.

Therefore the direct Clifford theorem is **not generator-independent**.

If one adds the explicit involutive/Coxeter condition

\[
h(L)^2=h(R)^2=e,
\]

then the primitive images are two transpositions and the direct native residues give

\[
Q_x^2=Q_y^2=e_{\rm std},
\qquad
\{Q_x,Q_y\}=0.
\]

Consequently

\[
\mathrm{Cl}_2(\mathbb C)\cong M_2(\mathbb C)
\]

and

\[
c=\frac12(Q_x+iQ_y),
\qquad
c^*=\frac12(Q_x-iQ_y)
\]

satisfy the one-mode CAR relations

\[
c^2=(c^*)^2=0,
\qquad
cc^*+c^*c=e_{\rm std}.
\]

This is retained only as the conditional implication

\[
\boxed{
\texttt{INVOLUTIVE MINIMAL HISTORY}
\Rightarrow
\texttt{DIRECT CLIFFORD}
\Rightarrow
\texttt{ALGEBRAIC CAR}_1.
}
\]

It must not be reported as an unconditional FCOA theorem.

---

## Two-mode barrier

Once the history algebra is fixed to

\[
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C),
\]

two independent finite CAR modes are impossible because

\[
\operatorname{CAR}_2\cong M_4(\mathbb C)
\]

cannot embed into this six-dimensional algebra.

Thus the fixed `S3` history algebra has matrix capacity at most one CAR mode.

This size obstruction is robust; existence of the direct first CAR pair is conditional as described above.

---

# Literature positioning

The following components are classical background and are **not** novelty claims:

- Parikh vectors / commutative closure;
- representation theory of `S3`;
- `S3` / `A2` equilateral geometry;
- Mercedes-Benz three-vector tight frame and frame bound `3/2`;
- finite group frames;
- real/complex group-algebra decomposition;
- Clifford and finite CAR matrix identities.

The publication candidate is the combined theorem

\[
\boxed{
\text{FCOA root-comb / binary Parikh fibers}
\to
S_3\text{ collision graph }K_3\sqcup K_3
\to
\text{two orthogonal }A_2\text{ edge frames}
\to
M_2(\mathbb R).
}
\]

A preliminary literature search found the surrounding theories but did not locate this exact combined statement. This is **not** proof of novelty; publication wording must remain conservative.

---

# Current ladder

\[
\boxed{
\begin{aligned}
QF0 &: \text{typed channel support},\\
QF1 &: \text{stochastic terminal weights},\\
QF2 &: \text{terminal complex weights (phase-erased without reconvergence)},\\
QF2.5 &: \text{native reconvergence / root-comb histories},\\
QF3a &: \text{finite history memory and minimal reversible size }6,\\
QF3b &: \mathbb C[S_3]\text{ conditional complex linearization},\\
QF3c &: M_2(\mathbb R)\text{ robust route-residue sector},\\
QF3d &: K_3\sqcup K_3\text{ Parikh-collision geometry},\\
QF3e &: \text{canonical six-edge }3/2\text{-tight route frame},\\
QF3f &: \text{conditional Coxeter Clifford/CAR}_1\text{ specialization},\\
QF4 &: \text{physical Hilbert/state/measurement dynamics — not reached},\\
QF5 &: \text{physical Fock/CAR/QFT structure — not reached}.
\end{aligned}
}
\]

All structures through `QF3f` remain finite internal history/operator fibers over the signed one-dimensional carrier.

---

# Files

- [`SOL_QFIELD_REPORT_v0_1.md`](./SOL_QFIELD_REPORT_v0_1.md) — QFT separation and channel no-go.
- [`SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md`](./SOL_QFIELD_AMPLITUDE_LIFT_v0_2.md) — amplitude underdetermination and reconvergence threshold.
- [`SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md`](./SOL_QFIELD_NATIVE_DIAMONDS_v0_3.md) — native radial diamonds.
- [`SOL_QFIELD_MINIMAL_HISTORY_v0_4.md`](./SOL_QFIELD_MINIMAL_HISTORY_v0_4.md) — minimal finite history monoid.
- [`SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md`](./SOL_QFIELD_REVERSIBLE_HISTORY_v0_5.md) — minimal reversible size and `S3` realization.
- [`SOL_QFIELD_LINEARIZATION_v0_6.md`](./SOL_QFIELD_LINEARIZATION_v0_6.md) — coefficient underdetermination and conditional `C[S3]` linearization.
- [`SOL_QFIELD_ORDER_STATE_GNS_v0_7.md`](./SOL_QFIELD_ORDER_STATE_GNS_v0_7.md) — standard-block state and GNS geometry.
- [`SOL_QFIELD_BINARY_OBSERVABLE_v0_8.md`](./SOL_QFIELD_BINARY_OBSERVABLE_v0_8.md) — first binary observable in the Coxeter realization.
- [`SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md`](./SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md) — root-comb and direct Clifford construction; **qualified by v0.11**.
- [`SOL_QFIELD_CAR_ONE_MODE_BARRIER_v0_10.md`](./SOL_QFIELD_CAR_ONE_MODE_BARRIER_v0_10.md) — one-mode CAR and two-mode size barrier; **CAR existence qualified by v0.11**.
- [`SOL_QFIELD_QUOTIENT_ROBUSTNESS_AUDIT_v0_11.md`](./SOL_QFIELD_QUOTIENT_ROBUSTNESS_AUDIT_v0_11.md) — canonicity defect and correction.
- [`SOL_QFIELD_CANONICAL_ROUTE_FRAME_v0_12.md`](./SOL_QFIELD_CANONICAL_ROUTE_FRAME_v0_12.md) — generator-independent collision graph and route tight frame.
- [`SOL_QFIELD_LITERATURE_POSITIONING_v0_13.md`](./SOL_QFIELD_LITERATURE_POSITIONING_v0_13.md) — standard-vs-candidate contribution audit.
- [`SOL_QFIELD_PARIKH_COLLISION_THEOREM_v0_14.md`](./SOL_QFIELD_PARIKH_COLLISION_THEOREM_v0_14.md) — conceptual collision proof and sharp depth bound.
- [`verify_parikh_collision_s3.py`](./verify_parikh_collision_s3.py) — finite certificate for all 18 ordered noncommuting `S3` generator pairs.

---

# Publication decision

The physical/QFT verdict remains

\[
\boxed{\texttt{ANALOGY ONLY}.}
\]

The robust mathematical core has now reached

\[
\boxed{\texttt{PUBLICATION CANDIDATE — PROOF CORE STABLE}.}
\]

The branch should **not yet be released** as a standalone paper until the final publication audit completes:

1. independent proof reread and notation normalization;
2. stronger bibliographic search around Parikh collisions under finite-group morphisms;
3. explicit separation of robust theorems from Coxeter-only corollaries;
4. article assembly with theorem/proof numbering and machine-verifier supplement.

---

# Next strike

The sharp remaining mathematical direction is the possible generalization from `S3`:

\[
\boxed{
\text{Parikh collisions under }h:\{L,R\}^*\twoheadrightarrow G
\quad\text{versus}\quad
[G,G].
}
\]

The `S3` proof suggests that Parikh-collision classes are controlled by the commutator subgroup and its conjugacy structure.

The next question is whether one can prove a general theorem describing the collision graph as unions of cosets/orbits determined by `[G,G]`, and characterize exactly when the associated representation-theoretic edge residues form tight frames.

That generalization is optional for the present paper; it should be pursued only if it strengthens the theorem without delaying the now-stable `S3` publication core.
