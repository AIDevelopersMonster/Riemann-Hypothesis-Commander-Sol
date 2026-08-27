# FCOA Admissibility Geometry

GitHub companion for the published research note:

**Alex Malachevsky, “Размышлизмы о геометрии допустимости с Commander Sol: как частичная операция запоминает ориентированный носитель.”**

English title:

**“Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier.”**

- ORCID: 0009-0008-6009-3196
- Publication date: 2026-08-27
- Zenodo DOI: **10.5281/zenodo.22129787**
- Persistent URL: https://doi.org/10.5281/zenodo.22129787

> **Maintenance boundary:** this publication line owns only `papers/FCOA-ADMISSIBILITY-GEOMETRY/**`, `demos/fcoa-domain-compilation/**`, and `experiments/fcoa-domain-compilation/**`. Other paper/experiment/demo branches in this repository are independent active research and must not be modified from this workspace. See [`WORKSPACE.md`](WORKSPACE.md).

> **Continuity checkpoint:** if this work is resumed in another conversation/session, read [`STATE.md`](STATE.md) before changing the mathematics.

## Scope

The paper studies partial, role-sensitive operations on a fixed finite carrier

\[
X_N=\{P_0,\ldots,P_N\},\qquad N\ge3,
\]

with the indices treated only as external labels. The central question is whether carrier geometry can survive after the external relation that originally described it is erased.

The research path is organized as

\[
\boxed{M0\longrightarrow G1\longrightarrow G2}.
\]

### M0 — sparse operational baseline

For the multiplication reduct, the generic sector

\[
G_N=\{P_2,\ldots,P_N\}
\]

is fully exchangeable:

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1}.
\]

### G1 — external interaction skeleton

A separate relation \(A\subseteq G_N^2\) is added without changing any operation value. For every such relation,

\[
\operatorname{Aut}(\mathfrak M_N^\times,A)
\cong
\operatorname{Aut}(G_N,A).
\]

For an undirected path and then a directed path this gives

\[
S_{N-1}\longrightarrow C_2\longrightarrow1.
\]

Erasing \(A\), however, restores the M0 symmetry. This is **external rigidity**, not yet internal memory.

### G2 — domain compilation

The directed path is compiled into the partial-operation domain using one fresh terminal output \(\Omega\):

\[
P_i\otimes_1P_{i+1}=\Omega,
\qquad 2\le i<N,
\]

with the reverse and non-adjacent generic cells left undefined. Then

\[
\operatorname{Aut}(\otimes_1)=1,
\]

and the directed adjacency is recoverable from the reduct itself:

\[
A_{\rm dir}(x,y)
\iff
x,y\in G_N,\ x\ne y,\ \operatorname{Def}(x\otimes_1y).
\]

Thus the external relation can be erased while the orientation survives in the operation domain.

## Main structural message

\[
\boxed{
\text{relation}
\longrightarrow
\text{partial-operation domain}
\longrightarrow
\text{recoverable structural memory}
}
\]

The new \(\Omega\)-cells all have the same output. Edge identity is therefore not encoded by edge-specific values; the distinguishing information lies in **where the operation is defined and in argument order**.

## Exact G2 invariants

For every \(N\ge3\), on base triples \((X_N)^3\),

\[
\begin{aligned}
EQ &= 5N-6,\\
NEQ &= 0,\\
LEFT &= N^2+3N-4,\\
RIGHT &= N^2+2N-4,\\
NONE &= N^3+N^2-7N+15.
\end{aligned}
\]

The commutation locus remains the M0 locus:

\[
\operatorname{Comm}_{\otimes_1}
=
\{(P_i,P_i):2\le i\le N\}
\cup
\{(P_1,P_i),(P_i,P_1):2\le i\le N\},
\]

so

\[
|\operatorname{Comm}_{\otimes_1}|=3(N-1).
\]

Hence automorphism rigidity can change maximally, from \(S_{N-1}\) to the trivial group, while the commutation locus does not change at all.

## Typed Domain Compilation Theorem

Let \(G\) be an input sort, let \(O=\{\Omega\}\) be a singleton output sort, and let \(A\subseteq G^2\). Define a partial operation

\[
\star_A:G\times G\rightharpoonup O
\]

by

\[
x\star_Ay=\Omega\iff A(x,y).
\]

Then restriction to \(G\) gives a canonical isomorphism

\[
\operatorname{Aut}(G,O;\star_A)
\cong
\operatorname{Aut}(G;A).
\]

The typed statement also handles \(A=\varnothing\): sort preservation keeps the singleton output separate from the input sort. In a one-sorted version an additional hypothesis is needed when the range is empty.

## Repository companion contents

- [`WORKSPACE.md`](WORKSPACE.md) — strict ownership boundary and no-touch rules for neighboring branches.
- [`STATE.md`](STATE.md) — continuity checkpoint: fixed results, hostile-audit corrections, exact formulas, and the next unresolved decision.
- [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md) — theorem/proof checkpoint and claim boundaries.
- [`CITATION.cff`](CITATION.cff) — article citation metadata.
- [`release/`](release/) — publication and repository recovery notes.
- [`../../demos/fcoa-domain-compilation/index.html`](../../demos/fcoa-domain-compilation/index.html) — standalone interactive demonstrator.
- [`../../experiments/fcoa-domain-compilation/verify_formulas.py`](../../experiments/fcoa-domain-compilation/verify_formulas.py) — dependency-free formula checks.

The publication PDF/DOCX/bilingual package is canonical on Zenodo. GitHub stores the theorem-level companion, reproducibility code, continuity state, and demonstrator so the mathematical mechanism remains inspectable without changing the archival publication.

## Claim discipline

The paper does **not** claim that successor automatically yields a uniformly first-order definable full order in an infinite limit. It distinguishes finite contextual recovery, uniform recovery of directed adjacency in the G2 family, and the separate question of uniform full-order recovery.

The work also does not claim that the general ideas of partial algebra, many-sorted algebra, left/right translations, conditional branching, or automorphism invariance are new in isolation. The research contribution is the explicit M0-G1-G2 construction and the separation of operation values, operation-domain geometry, external rigidity, and internal memory.
