# FCOA Admissibility Geometry — current state

**Canonical publication DOI:** 10.5281/zenodo.22129787  
**Publication date:** 2026-08-27  
**GitHub role:** theorem/reproducibility/demo companion  
**Maintenance boundary:** see [`WORKSPACE.md`](WORKSPACE.md)

## 1. What is fixed

The publication checkpoint is the audited chain

\[
M0\longrightarrow G1\longrightarrow G2.
\]

No G3 rule is part of the published checkpoint.

### M0 multiplication

Generic sector:

\[
G_N=\{P_2,\ldots,P_N\},\qquad N\ge3.
\]

Automorphisms:

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1}.
\]

Association Spectrum on \((X_N)^3\):

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
\bigl(4(N-1),0,N^2+2N-2,N^2+N-2,N^3+N^2-4N+9\bigr).
\]

### G1 external skeleton

For any binary relation \(A\subseteq G_N^2\),

\[
\operatorname{Aut}(\mathfrak M_N^\times,A)
\cong
\operatorname{Aut}(G_N,A).
\]

For the undirected and directed path skeletons:

\[
S_{N-1}\to C_2\to1.
\]

But erasing the external relation restores M0 symmetry. Therefore G1 demonstrates **external rigidity**, not internal order memory.

### G2 domain compilation

A single fresh terminal output \(\Omega\) is used for all directed-adjacency cells:

\[
P_i\otimes_1P_{i+1}=\Omega,
\qquad 2\le i<N.
\]

Reverse and non-adjacent generic cells remain undefined. Further composition with \(\Omega\) is undefined.

Then

\[
\operatorname{Aut}(\otimes_1)=1.
\]

Directed adjacency is uniformly recoverable across the family by the off-diagonal definedness relation on the generic sort:

\[
A_{\rm dir}(x,y)
\iff
x,y\in G_N,\ x\ne y,\ \operatorname{Def}(x\otimes_1y).
\]

G2 Association Spectrum:

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
\bigl(5N-6,0,N^2+3N-4,N^2+2N-4,N^3+N^2-7N+15\bigr).
\]

The commutation locus is unchanged from M0 and has size

\[
3(N-1).
\]

## 2. Important distinctions that must not be collapsed

### Role distinguishability is not structural rigidity

The base-indexed left/right translations of M0 are injective, while

\[
\operatorname{Aut}(\otimes)\cong S_{N-1}.
\]

Different translation profiles can move coherently under automorphisms.

### External rigidity is not internal memory

G1 can be rigid because the relation \(A\) is explicitly named. After erasing \(A\), the symmetry returns. G2 remains rigid after the external relation is removed because the directed skeleton has been compiled into the operation domain.

### Values are not the only structural carrier

All new G2 directed edges have the same value \(\Omega\). Edge identity is not encoded by different outputs. The distinguishing information is in which ordered pairs are defined.

### Uniform successor recovery is not uniform full-order recovery

G2 uniformly recovers the directed adjacency/successor relation. Do not infer from this alone that the transitive full order is uniformly first-order definable on an unbounded or infinite carrier.

## 3. Typed Domain Compilation theorem

Primary formulation:

Let \(G\) be an input sort, \(O=\{\Omega\}\) a singleton output sort, and \(A\subseteq G^2\). Define

\[
\star_A:G\times G\rightharpoonup O
\]

by

\[
x\star_Ay=\Omega\iff A(x,y).
\]

Then restriction to the input sort gives

\[
\operatorname{Aut}(G,O;\star_A)
\cong
\operatorname{Aut}(G;A).
\]

The typed version includes \(A=\varnothing\). A one-sorted formulation requires additional hypotheses when the operation has empty range or when unused carrier elements are present.

## 4. Verified finite checkpoints

For \(N=6\):

- M0 addition spectrum: \((5,1,22,22,293)\);
- M0 multiplication spectrum: \((20,0,46,40,237)\);
- G2 multiplication spectrum: \((24,0,50,44,225)\).

The formulas are also checked by `../../experiments/fcoa-domain-compilation/verify_formulas.py` for \(N=3,\ldots,10\).

## 5. Hostile-audit corrections incorporated

The following corrections are part of the final checkpoint:

1. M0 addition has one genuine NEQ triple, \((P_1,P_0,P_1)\); claims of NEQ=0 were rejected.
2. \(x\oplus P_0=y\) defines immediate predecessor, not the whole strict order.
3. In G2, the new family \((P_i,P_1,P_{i+1})\) contributes \(N-2\) additional EQ triples.
4. Base-indexed translations remain injective; full-carrier translation injectivity fails because terminal outputs all have empty translations.
5. The untyped Domain Compilation statement needs an empty-relation/output-distinguishability caveat; the typed theorem is the primary clean formulation.

## 6. Files that represent this publication line

- `README.md` — publication overview and DOI.
- `WORKSPACE.md` — strict scope boundary; do not touch neighboring branches.
- `STATE.md` — this continuity checkpoint.
- `MATHEMATICAL_CORE.md` — theorem/proof checkpoint.
- `CITATION.cff` — citation metadata.
- `release/RELEASE_MANIFEST.md` — archival/repository consistency note.
- `../../demos/fcoa-domain-compilation/index.html` — interactive visual demonstrator.
- `../../experiments/fcoa-domain-compilation/verify_formulas.py` — exact finite verification.

The publication binaries and bilingual archival package remain canonical on Zenodo under DOI 10.5281/zenodo.22129787.

## 7. Post-publication research branch G3 — opened, not yet audited

The next research question has now been opened explicitly as a new checkpoint, without modifying the published G2 result.

Detailed file:

- [`G3_VALUE_GEOMETRY.md`](G3_VALUE_GEOMETRY.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_g3.py`

### G3-S — symmetric domain, one anonymous value

For every adjacent generic pair, both orientations are defined with the same terminal value:

\[
P_i\otimes_S P_{i+1}=\Omega,
\qquad
P_{i+1}\otimes_S P_i=\Omega.
\]

Candidate results:

\[
\operatorname{Aut}(\otimes_S)\cong C_2,
\]

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
(6N-8,0,N^2+4N-6,N^2+3N-6,N^3+N^2-10N+21),
\]

\[
|\operatorname{Comm}_{\otimes_S}|=5N-7.
\]

### G3-C — same symmetric domain, two anonymous directional values

Use two distinct terminal values:

\[
P_i\otimes_C P_{i+1}=\Omega_+,
\qquad
P_{i+1}\otimes_C P_i=\Omega_-.
\]

If \(\Omega_+,\Omega_-\) are anonymous and exchangeable, path reversal extends by swapping them. Candidate result:

\[
\operatorname{Aut}(\otimes_C)\cong C_2.
\]

The Association Spectrum is unchanged from G3-S, but

\[
|\operatorname{Comm}_{\otimes_C}|=3(N-1).
\]

This is the first candidate demonstration that a value-fiber change can alter the commutation locus while leaving the domain, Association Spectrum, and automorphism-group size unchanged.

### G3-A — one anchored value fiber

Add one boundary anchor on the already fixed M0 pair:

\[
P_1\otimes_A P_0=\Omega_+.
\]

Candidate result:

\[
\operatorname{Aut}(\otimes_A)=1,
\]

while the definedness reduct on the generic sector still has the path reflection:

\[
\operatorname{Aut}(D_{\otimes_A})\cong C_2.
\]

Candidate spectrum:

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
(6N-8,0,N^2+4N-6,N^2+4N-6,N^3+N^2-11N+21).
\]

The working interpretation is that G3-A carries an orientation component in an **anchored value fiber** which is not reducible to the operation domain alone.

### New working diagnostics

- **Anonymous Output-Swap Lemma:** an orientation coloring by two exchangeable terminal values need not remove a carrier reflection if the reflection can be extended by swapping the outputs.
- **One-Anchor Lemma:** within that anonymous two-output branch, one value anchor on a structurally fixed pair kills the residual output-swap reflection.
- **Value-Erasure Test:** compare the automorphism group of the full partial operation with the automorphism group of its definedness reduct. A strict drop under value restoration indicates structural information carried by value fibers rather than domain geometry alone.

These names are working terminology, not priority claims.

### Verification status

`verify_g3.py` checks the G3-S/G3-C/G3-A Association Spectrum and commutation counts for \(N=3,\ldots,10\).

The group statements have direct proofs recorded in `G3_VALUE_GEOMETRY.md`.

**Hostile audit is still pending.** Until two independent audits agree, G3 remains theorem-candidate status and must not be treated as part of the published G2 checkpoint.

## 8. Immediate next step

Do not add any further G4-style cells yet.

The next step is a blind hostile audit of G3 with special attention to:

1. whether anonymous \(\Omega_+,\Omega_-\) are genuinely exchangeable in the exact signature;
2. whether the one anchor \(P_1\otimes P_0=\Omega_+\) is sufficient and minimal within the stated branch;
3. exact small-case behavior at \(N=3\);
4. complete Association Spectrum formulas;
5. distinction between the automorphism group of the full operation and that of its definedness reduct;
6. whether any hidden output naming/sorting assumption accidentally trivializes the value-memory claim.

Only after that audit should G3 be promoted from theorem candidate to fixed branch result.
