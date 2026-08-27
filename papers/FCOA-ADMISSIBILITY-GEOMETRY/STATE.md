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

## 7. Next research decision, not yet executed

Do **not** invent additional generic operation values by default.

The next legitimate research question, if this line is resumed, is whether to open a new branch beyond G2 and, if so, what minimal extension adds information that is not already reducible to domain geometry while avoiding reconstruction of ordinary arithmetic.

That decision belongs to a future explicit research step and must not be silently folded into the published G2 checkpoint.
