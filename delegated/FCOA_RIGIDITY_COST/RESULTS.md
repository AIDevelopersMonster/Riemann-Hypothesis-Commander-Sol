# FCOA Rigidity Cost — Local Results

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Branch:** `director/fcoa-rigidity-cost`  
**Status:** local theorem/proof ledger; nothing here modifies the main FCOA line automatically  
**Upstream boundary:** M0–G2 are fixed by DOI `10.5281/zenodo.22129787`; G3 is hostile-audited with repair; G4 is still a candidate pending hostile audit.

Throughout, put

\[
n:=|G_N|=N-1,
\qquad
G_N=\{P_2,\dots,P_N\}.
\]

Unless stated otherwise, a directed skeleton is loopless, \(A\subseteq G_N^2\setminus\Delta\), and an undirected skeleton is a simple graph on \(G_N\).

---

## R1. Prescribed-group orbital reduction

Let \(X\) be a finite carrier, \(|X|=n\), and let \(K\le S_X\) be a **fixed permutation embedding** of a target group.

For directed loopless skeletons, every relation \(A\subseteq X^2\setminus\Delta\) with

\[
\operatorname{Aut}(X,A)=K
\]

is necessarily a union of \(K\)-orbits on ordered pairs. Conversely, every union \(U\) of such orbitals satisfies \(K\le\operatorname{Aut}(X,U)\), with equality exactly when the setwise stabilizer of \(U\) in \(S_X\) is \(K\).

Hence, for the fixed embedding,

\[
\boxed{
\operatorname{RC}^{\to}_X(K)
=
\min_{\mathcal S}
\left\{
\sum_{O\in\mathcal S}|O|:
\operatorname{Stab}_{S_X}\!\left(\bigcup_{O\in\mathcal S}O\right)=K
\right\}.
}
\]

The undirected version is identical with orbitals on \(\binom X2\). For an **abstract** target group \(H\), minimize further over faithful permutation embeddings \(K\cong H\) on the chosen carrier.

This converts prescribed-group rigidity cost from a search over all relations to subset selection over the 2-orbits of the chosen target action.

---

## R2. Rigid-component decomposition

Let \(A\) be a finite directed skeleton and take weakly connected components; in the undirected case take ordinary connected components.

### Theorem

\[
\boxed{
A\text{ is rigid}
\iff
\begin{cases}
\text{every connected component is rigid},\\
\text{no two connected components are isomorphic}.
\end{cases}}
\]

A nontrivial automorphism of one component extends by the identity. Two isomorphic components may be exchanged. Conversely, if every component is rigid and component types are pairwise nonisomorphic, every automorphism fixes each component and is trivial on it.

More generally, if connected isomorphism type \(C_i\) occurs with multiplicity \(m_i\), then

\[
\operatorname{Aut}\!\left(\bigsqcup_i C_i^{\sqcup m_i}\right)
\cong
\prod_i \operatorname{Aut}(C_i)\wr S_{m_i}.
\]

Thus global rigidity-cost constructions can be built as a packing problem over pairwise nonisomorphic connected rigid components, with at most one isolated singleton.

---

## R3. Pure-carrier naturality barrier

Suppose a rule assigns to every \(n\)-element pure set \(X\) a skeleton \(A_X\), and is natural under every bijection: every bijection \(f:X\to Y\) sends \(A_X\) to \(A_Y\).

Taking \(Y=X\) and \(f\in S_X\) gives

\[
f(A_X)=A_X
\qquad\forall f\in S_X.
\]

Therefore

\[
\boxed{
\operatorname{Aut}(X,A_X)=S_X.
}
\]

So no fully equivariant rule on a **pure carrier** can break the original \(S_n\) symmetry.

`carrier-uniform` must therefore be separated into two meanings:

1. **pure-carrier natural under all bijections:** symmetry breaking is impossible;
2. **uniform relative to transported extra structure** — order, anchor, chosen skeleton, tournament, etc.: symmetry breaking is possible, but the extra structure is an input.

No arithmetic statement is involved.

---

## R4. Exact small rigidity costs

Define

\[
r_{\to}(n)=\min\{|A|:\operatorname{Aut}(X,A)=1\}
\]

for loopless directed skeletons, and similarly \(r_-(n)\) for simple undirected skeletons. Write \(\infty\) if no rigid skeleton exists.

Exhaustive enumeration gives:

| \(n=N-1\) | \(N\) | \(r_{\to}(n)\) | one directed witness | \(r_-(n)\) |
|---:|---:|---:|---|---:|
| 2 | 3 | 1 | one directed edge | \(\infty\) |
| 3 | 4 | 1 | one directed edge + isolate | \(\infty\) |
| 4 | 5 | 2 | directed 2-path + isolate | \(\infty\) |
| 5 | 6 | 3 | rigid 3-arc oriented tree + isolate | \(\infty\) |
| 6 | 7 | 3 | directed 2-path + directed edge + isolate | 6 |
| 7 | 8 | 4 | rigid 3-arc oriented tree + directed edge + isolate | 6 |

A six-vertex minimum undirected witness is

\[
\{01,02,03,12,14,35\}.
\]

The seven-vertex minimum witness is the same rigid six-vertex graph plus one isolated point.

### Lower bounds in the first directed cases

- \(n=3\): zero arcs leave \(S_3\); one arc makes tail, head and isolate distinct.
- \(n=4\): one arc leaves two isolates, so at least two arcs are needed; a directed 2-path plus an isolate is rigid.
- \(n=5\): with at most two arcs, either at least two vertices are isolated or the two arcs form two isomorphic edge components; hence three arcs are necessary.
- \(n=6\): incidence gives \(2m\ge n-1\), hence \(m\ge3\), and the stated three-arc construction is rigid.
- \(n=7\): three arcs can cover six nonisolated vertices only as three disjoint directed edges, which are permutable; hence four arcs are necessary.

For every \(n\ge2\),

\[
\boxed{
r_{\to}(n)\ge \left\lceil\frac{n-1}{2}\right\rceil}
\]

because a rigid skeleton has at most one isolated vertex and each arc touches at most two vertices.

For every \(n\ge3\),

\[
\boxed{r_{\to}(n)\le n-2}
\]

by a directed path on \(n-1\) vertices plus one isolate.

The undirected small values are classical asymmetric-graph territory and are recorded here only to calibrate the FCOA cost function.

---

## R5. Rigidity–Memory Gap

The G2 directed successor path across \(n\) generic vertices uses

\[
M_{\rm succ}(n)=n-1
\]

new operation cells. Define

\[
\Delta(n)=M_{\rm succ}(n)-r_{\to}(n).
\]

For \(n=2,3,4,5,6,7\),

\[
\boxed{\Delta(n)=0,1,1,1,2,2.}
\]

Thus

\[
\boxed{
\text{cost of killing automorphisms}
<
\text{cost of storing a chosen global successor skeleton}
}
\]

in general.

This does **not** weaken G2. G2 stores uniformly recoverable directed adjacency over the whole generic sector; a cheaper rigid skeleton need not recover a full successor relation.

---

## R6. Terminal Generic Layer Master Lemma

Start from M0 multiplication and add

\[
A\subseteq G_N^2\setminus\Delta,
\qquad |A|=m,
\]

new generic cells. Every new value is terminal: no product having a new output as an argument is defined. The values on \(A\) may be constant or partitioned among several terminal outputs.

### Association Spectrum theorem

On base triples \((X_N)^3\), **only the number of newly defined generic cells matters**:

\[
\boxed{
\begin{aligned}
EQ &= 4(N-1)+m,\\
NEQ &= 0,\\
LEFT &= N^2+2N-2+m,\\
RIGHT &= N^2+N-2+m,\\
NONE &= N^3+N^2-4N+9-3m.
\end{aligned}}
\]

This is independent of the geometry of \(A\) and independent of the equality partition of its terminal values.

### Proof

Each new ordered cell

\[
u\star v=\Omega_{uv}
\]

changes exactly three base triples:

\[
(u,P_1,v):\quad EQ,
\]

\[
(P_1,u,v):\quad LEFT,
\]

\[
(u,v,P_1):\quad RIGHT.
\]

In the first triple both bracketings evaluate to the same new cell value. In the other two, the opposite bracketing hits a terminal output and stays undefined. Terminality prevents any other second-stage value. Distinct new cells give distinct affected triples. Every cell therefore contributes exactly

\[
(+1,0,+1,+1,-3).
\]

This single formula recovers the G2, G3-S/G3-C and G4-C spectra by substituting their numbers of generic cells.

### Exact commutation formula

If \(c:A\to O\) is the terminal value map, then

\[
\boxed{
|\operatorname{Comm}|
=
3(N-1)
+
\left|
\{(u,v)\in A:(v,u)\in A,\ c(u,v)=c(v,u)\}
\right|.
}
\]

The correction set is counted as ordered pairs.

Hence Association Spectrum is blind to skeleton shape and terminal value-fiber geometry beyond \(|A|\), while commutation sees only same-valued reverse pairs.

### Domain-only cost transfer

If all new cells have one terminal output \(\Omega\), typed Domain Compilation gives

\[
\operatorname{Aut}(\text{M0 + layer }A)
\cong
\operatorname{Aut}(G_N,A).
\]

Therefore, under the same signature and embedding conventions,

\[
\boxed{
\operatorname{RC}^{\rm domain}_N(H)
=
\operatorname{RC}^{\to}_{n}(H).
}
\]

---

## R7. Low-cost compiled rigid operations for N=3,4,5

Compile the rigidity-minimal directed skeletons from R4 with one terminal output. No reverse pair is present, so commutation stays at M0 size \(3(N-1)\).

| \(N\) | generic \(n\) | new cells | full \(\operatorname{Aut}\) | \(\operatorname{Aut}(D\upharpoonright X_N)\) | commutation | Association Spectrum |
|---:|---:|---:|---|---|---:|---|
| 3 | 2 | 1 | 1 | 1 | 6 | \((9,0,14,11,30)\) |
| 4 | 3 | 1 | 1 | 1 | 9 | \((13,0,23,19,70)\) |
| 5 | 4 | 2 | 1 | 1 | 12 | \((18,0,35,30,133)\) |

Relative to G2:

- \(N=3\): same one-cell cost;
- \(N=4\): rigidity needs 1 cell, G2 successor memory needs 2;
- \(N=5\): rigidity needs 2 cells, G2 successor memory needs 3.

These use domain geometry only, no anchors, one terminal value, and no arithmetic on external indices.

---

## R8. Two anonymous values: unbalanced complete-domain transfer

Fix the complete off-diagonal generic domain

\[
D=G_N^2\setminus\Delta,
\qquad |D|=n(n-1).
\]

Choose a directed relation \(A\subset D\), and assign

\[
c(x,y)=
\begin{cases}
\Omega_+,&(x,y)\in A,\\
\Omega_-,&(x,y)\in D\setminus A,
\end{cases}
\]

with \(\Omega_+,\Omega_-\) distinct anonymous terminal outputs.

In the relative terminal-output setup of the Fiber-Transport Theorem, the carrier automorphism group is

\[
\{g\in S_n:gA=A\text{ or }gA=D\setminus A\}.
\]

If

\[
|A|\ne|D\setminus A|,
\]

fiber exchange is impossible by cardinality. Hence

\[
\boxed{
\operatorname{Aut}(D,\{A,D\setminus A\})=
\operatorname{Aut}(A).
}
\]

Every rigid directed skeleton of non-half size therefore produces a complete-domain, two-anonymous-output, zero-anchor rigid terminal layer. For \(n\ge3\), \(r_{\to}(n)\le n-2<n(n-1)/2\), so the minimum minority-fiber size in this relative unbalanced model is exactly \(r_{\to}(n)\).

Anonymous outputs need not be externally named to become individually fixed: unequal fiber cardinalities may distinguish them internally.

One-sorted presentations must still verify the standard output-family/preimage-geometry separation; this result is stated primarily in the relative Fiber-Transport setup.

---

## R9. Balanced two-output rigidity without anchors

The residual reversal in G4-C is **not** forced by complete definedness, two anonymous outputs, or equal fiber size.

### R9a. Four generic vertices: a balanced rigid partition

For \(n=4\), on vertices \(0,1,2,3\), let

\[
A_4=\{01,02,03,10,12,21\},
\]

and let the other six ordered pairs form the second anonymous fiber.

Then

\[
|A_4|=|A_4^c|=6
\]

and exhaustive verification gives

\[
\boxed{
\operatorname{Aut}(\{A_4,A_4^c\})=1.
}
\]

So at \(N=5\), a balanced complete generic domain can already be rigid with two anonymous values and no anchor. This witness has same-valued reverse pairs, so its commutation locus differs from G4-C.

### R9b. Five generic vertices: same coarse invariants as G4-C, but rigid

On vertices \(0,1,2,3,4\), define the tournament

\[
T_5=
\{40,41,42,43,20,21,31,32,03,10\}.
\]

Its outdegrees are

\[
(1,1,2,2,4).
\]

It is asymmetric:

- vertex 4 is the unique vertex of outdegree 4;
- among the outdegree-1 vertices, 0 points to an outdegree-2 vertex while 1 points to an outdegree-1 vertex;
- among the outdegree-2 vertices, 2 dominates both outdegree-1 vertices while 3 does not.

Thus every vertex is fixed.

It is also not self-converse: it has a source and no sink, whereas its converse has a sink and no source.

Color tournament arcs by \(\Omega_+\) and their reverses by \(\Omega_-\). Then

\[
|D_+|=|D_-|=10.
\]

A carrier permutation preserving the anonymous partition would be either an automorphism of \(T_5\) or an isomorphism \(T_5\cong T_5^{\rm op}\). Neither exists. Therefore

\[
\boxed{\operatorname{Aut}=1.}
\]

Because exactly one direction of each unordered pair has each value, no new generic commuting pair appears. Thus for \(N=6\) this construction has:

- the same complete generic definedness domain as G4-C;
- the same two anonymous terminal outputs;
- the same balanced fiber sizes;
- the same Association Spectrum \((40,0,66,60,177)\);
- the same commutation size \(15\);
- but \(\operatorname{Aut}=1\) instead of \(C_2\).

### R9c. Infinite family for every n >= 5

Starting from \(T_5\), form \(T_{n+1}\) from \(T_n\) by adjoining one new vertex that dominates every old vertex.

Inductively:

1. the new vertex is the unique source and is fixed by every automorphism;
2. restriction to the old vertices is an automorphism of \(T_n\), hence trivial;
3. no sink is created, so \(T_n\) has a source and no sink and cannot be self-converse.

Therefore for every \(n\ge5\),

\[
\boxed{T_n\text{ is asymmetric and non-self-converse}.}
\]

Its two anonymous tournament-orientation fibers give a complete-domain FCOA terminal layer with

\[
\boxed{
\operatorname{Aut}=1,
\qquad
\operatorname{Aut}(D\upharpoonright X_N)\cong S_n,
\qquad
\operatorname{VRI}=n!.
}
\]

At the same time,

\[
|\operatorname{Comm}|=3n
\]

and the Association Spectrum is exactly the G4-C complete-domain formula.

Thus

\[
\boxed{
\text{G4-C's residual }C_2
\text{ comes from its transitive-order fiber geometry,}
\text{ not from two-valued anonymity itself.}
}
\]

This does **not** refute G4-C. The G4 one-anchor mechanism remains correct inside its chosen transitive-order branch; it is not a global minimum over all two-anonymous-output complete-domain colorings.

---

## R10. Natural cyclic and dihedral skeleton costs

These are **fixed-action** results, not global abstract-group minima.

### Directed regular cyclic action

For the regular action of \(C_n\), \(n\ge3\), every nonempty orbital on ordered pairs has size \(n\). A one-step directed cycle is one orbital and has full automorphism group \(C_n\). Hence

\[
\boxed{\operatorname{RC}^{\to}_{\rm reg}(C_n)=n.}
\]

### Undirected regular cyclic obstruction

For \(n>2\), every undirected circulant admits inversion in addition to the regular translations. Hence the full automorphism group cannot be exactly the regular \(C_n\) in this undirected regular-action class. This is classical GRR territory, not a novelty claim.

### Natural dihedral polygon action

The undirected cycle \(C_n\) has automorphism group \(D_n\) and uses \(n\) edges. For odd \(n\ge5\), every nonempty orbit of the natural dihedral action on unordered pairs has size \(n\), so the cost is exactly \(n\). For even \(n\ge6\), the only smaller orbit is the opposite-pair matching of size \(n/2\), whose automorphism group is strictly larger than \(D_n\); hence the exact natural-action cost is again \(n\).

Small cases: \(D_3\cong S_3\) is realized by the empty graph at cost 0; for \(D_4\), the two opposite edges already have automorphism group \(D_4\).

---

## R11. Small exact C2 table

Exact enumeration for target automorphism group of order 2 gives:

| generic \(n\) | directed minimum | undirected minimum |
|---:|---:|---:|
| 2 | 0 | 0 |
| 3 | 2 | 1 |
| 4 | 1 | 2 |
| 5 | 2 | 3 |
| 6 | 3 | 4 |
| 7 | 3 | 5 |

No asymptotic law is asserted from this short table.

---

## Research firewall

1. No ordinary arithmetic on external indices is imported by any theorem above.
2. `UNDEF` is not treated as a value.
3. `R1` is a fixed-embedding reduction; abstract-group minima require minimization over embeddings.
4. `R8–R9` use anonymous value fibers; no externally named color constants are used in the automorphism comparison.
5. A chosen tournament/skeleton is transported combinatorial input, not a canonical structure generated from a pure carrier; R3 forbids the latter.
6. The graph-theoretic existence/minimality of asymmetric graphs, prescribed automorphism groups, GRRs, asymmetric tournaments, etc. is classical territory. See `LITERATURE_NOTES.md`; no broad novelty claim is made.
7. G4 remains an upstream theorem candidate until its own hostile audit. The present results sharpen the scope of its residual symmetry but do not edit or supersede it.