# HATTER-SOL-12 · ARTICLE ARCHITECTURE

**Working title:** *Observer Laws, World Rotation, and Structural Memory of an Integer*  
**Status:** architecture freeze v0.1 — theorem spine defined, research extensions remain open.

## 0. Publication thesis

The article will not claim that an integer literally contains arbitrary extra message bits. Its central mathematical claim is narrower and stronger:

> the same rational integer can generate different structural states across arithmetic worlds and carriers, and the number of states visible to an observer obeys exact refinement, collapse, reconstruction and resolution laws.

The basic laboratory object is

\[
\boxed{(n,W,C,O).}
\]

The paper separates:

- **world:** generates admissible arithmetic structure;
- **carrier:** constrains realizability and global compatibility;
- **observer:** identifies/forgets structural distinctions.

## 1. Section I — From numerical equality to structural fibers

Define the structural state set

\[
\mathsf S(n;W,C)
\]

and observer

\[
O:\mathsf S(n;W,C)\to Y_O.
\]

Define the observational fiber

\[
\mathcal F_O(s)=O^{-1}(O(s)).
\]

State the distinction between:

- numerical identity;
- structural multiplicity;
- observational indistinguishability;
- independent information/payload, which is not inferred automatically.

## 2. Section II — General laws of the observer

Use `RESEARCH_KERNEL.md`.

### Theorem O12.1 — observer coarsening

If

\[
O_2=f\circ O_1,
\]

then

\[
\mathcal F_{O_1}(s)\subseteq\mathcal F_{O_2}(s).
\]

### Theorem O12.2 — joint refinement

For

\[
O_1\vee O_2=(O_1,O_2),
\]

the fiber is the intersection of the two fibers.

These results are foundational bookkeeping laws and are not novelty claims by themselves.

## 3. Section III — Exact observer/carrier mirror laboratory

Use `OBSERVER_CARRIER_MIRROR_THEOREM.md`.

Fix the HATTER-SOL-11 interior fiber

\[
(P,Q),\quad(Q,P),\quad(0,P+Q),
\qquad P>Q>0.
\]

Observer refinement gives

\[
\boxed{1\to2\to3}
\]

through:

1. total capacity;
2. total capacity + pure/mixed bit;
3. ordered orbit-total pair.

On an even connected `d`-regular 1-factorizable carrier, exact response distinguishability gives

\[
\boxed{3\to2\to1}
\]

at thresholds

\[
d=P,
\qquad d=P+Q.
\]

Call this a **mirror law of finite distinguishability**, explicitly not a categorical duality.

This is the first central new synthesis of the paper.

## 4. Section IV — Rotation through worlds and polynomial digits

Use the established HATTER-SOL-09 prime-toggle world graph:

\[
T_q^2=I,
\qquad T_pT_q=T_qT_p.
\]

For finite `Q`, define

\[
F_n(A)=Z_{T_AR_0}(n;X,Y).
\]

Use `WORLD_DIGIT_FIELD.md` to define

\[
D_B=\left[\prod_{q\in B}(I-T_q)Z_n\right](R_0).
\]

### Theorem WD12.1 — exact finite-cube reconstruction

\[
Z_{T_AR_0}(n)
=
\sum_{B\subseteq A}(-1)^{|B|}D_B,
\]

and conversely

\[
D_B
=
\sum_{C\subseteq B}(-1)^{|C|}Z_{T_CR_0}(n).
\]

Interpret this as an exactly invertible polynomial-valued coordinate system on a finite world cube. State explicitly that the algebra is Boolean-cube/Mobius inversion and is not itself claimed new.

## 5. Section V — Observation horizons

Define finite horizons on potentially infinite response fields.

Examples:

\[
|B|\le r
\]

for world-interaction order,

\[
a+b\le L
\]

for polynomial support,

finite world radius,

finite orbit set,

finite carrier scale.

If `H_1 subset H_2`, then the richer horizon refines the observer and shrinks fibers.

The factor-depth threshold observer from `MAXIMAL_FACTOR_BIT_OBSERVER.md` appears here as an elementary example, not as the article's main invariant.

## 6. Section VI — Infinite expansion versus finite effective diversity

Define the formal infinite world jet

\[
\mathcal J_\infty(n;R_0)
=
\{D_B:B\subset\mathbb P,\ |B|<\infty\}.
\]

Then make the essential negative statement:

If the chosen quadratic-world response depends only on split/inert states of `s` rational prime divisors of `n`, then

\[
N_Q(n)\le2^s
\]

for every finite cube; with a three-state split/inert/ramified coarse local model,

\[
N_Q(n)\le3^s.
\]

Therefore infinite address length is not automatically unbounded independent structural diversity.

### Open problem

Find a natural richer world family for which fixed-number response diversity is provably unbounded without arbitrary external labels.

This is a research question, not a publication claim unless solved before freeze.

## 7. Section VII — The exact `61^6` observer ladder

Use `PRIME_61_OBSERVER_LADDER.md`.

For the same rational integer:

- numerical observer on nine UFD worlds: `1` class;
- scalar 1D-to-planar gain: `2` classes (split/inert);
- one planar weighted sample `r>1` on four split worlds: `3` classes;
- two planar samples: `4` classes;
- one polynomial-valued typed signal: `4` classes.

Thus one concrete number realizes a strict sequence

\[
\boxed{1\to2\to3\to4}
\]

under increasing observational resolving power (with the four-world stages restricted to the split sector as stated explicitly).

## 8. Section VIII — Carrier-induced observability transition

Keep `61^6`, the same four split worlds and the same weighted scalar observer family.

Planar carrier:

\[
\operatorname{tdim}_{Pl}=2.
\]

Explicit triangular torus carrier:

\[
\operatorname{tdim}_{T^2}=1.
\]

Use `OBSERVATION_DIRECTION_PHASE_DIAGRAM.md` for the stronger exact result:

\[
D_{Pl}(r)=
\begin{cases}
2,&r<1,\\
1,&r=1,\\
3,&r>1,
\end{cases}
\]

whereas

\[
D_T(r)=
\begin{cases}
3,&r<1,\\
2,&r=1,\\
4,&r>1.
\end{cases}
\]

Hence

\[
\boxed{D_T(r)-D_{Pl}(r)=1\quad\forall r>0.}
\]

This is stronger than the tomographic-dimension statement and should be highlighted as a principal finite theorem of HATTER-SOL-12.

## 9. Section IX — Beyond the torus: programme, not theorem

Discuss without overclaiming:

- arbitrary surface carriers;
- combinatorial embeddings/rotation systems;
- homology/fundamental group;
- natural arithmetic gain/holonomy only if an arithmetic label group is independently justified;
- embedding-dependent geometric layers such as curvature sign;
- richer world families beyond quadratic split/inert data.

No general genus-memory law should be presented as a HATTER theorem merely because standard topology supplies `H_1(Sigma_g)`.

## 10. Section X — What HATTER-SOL-13 may test

Only prospects:

- self-diagnostic structural words;
- self-synchronizing world traversals;
- rateless verification/check coordinates;
- tamper-evident structural consistency;
- error-correcting/self-carrying codes;
- cryptographic constructions only if a concrete hardness assumption/problem is identified.

No application performance or security claim belongs in HATTER-SOL-12.

## 11. Theorem dependency spine

Publication-critical dependencies:

1. HATTER-SOL-11 orbital fiber classification.
2. HATTER-SOL-11 regular factorizable host response theorem.
3. HATTER-SOL-09 prime-toggle world operators and response polynomial.
4. HATTER-SOL-11 exact `61^6` planar weighted tomography.
5. HATTER-SOL-11 exact triangular-torus weighted response seed.
6. HATTER-SOL-12 observer laws.
7. HATTER-SOL-12 observer/carrier mirror theorem.
8. HATTER-SOL-12 world-digit reconstruction.
9. HATTER-SOL-12 `61^6` observer ladder.
10. HATTER-SOL-12 observation-direction phase diagram.

Not publication-critical:

- speculative cryptography;
- curvature-typed torus constructions;
- unbounded-diversity conjecture;
- general surface holonomy;
- application engineering.

## 12. Current publication threshold

**Not yet crossed.**

The mathematical spine is now substantial enough for a paper, but before manuscript drafting it requires:

1. hostile prior-art audit of observer refinement/information order terminology;
2. audit of Boolean/Mobius world-digit language;
3. audit of geometry/topology-induced distinguishability claims;
4. consistency check that every `61^6` formula is inherited from a closed HATTER-SOL-11 theorem layer;
5. novelty ledger separating standard machinery from the composed HATTER result.

After those audits, an EN v0.1 theorem-spine manuscript is justified.