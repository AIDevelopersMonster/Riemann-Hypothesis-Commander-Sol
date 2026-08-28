# FCOA Rigidity Cost — Upstream Memo

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Audience:** main Commander Sol scientific director  
**Status:** local results proposed for upstream review; nothing here modifies M0–G4 automatically.

## Executive verdict

Six results from this direction are strong enough for upstream review.

### U1. Rigidity cost is not successor-memory cost

Let `n=N-1` be the generic carrier size and

\[
r_{\to}(n)=\min\{|A|:\operatorname{Aut}(X,A)=1\}.
\]

Exact values through `n=7` are

\[
(1,1,2,3,3,4).
\]

Elementary bounds give

\[
\left\lceil\frac{n-1}{2}\right\rceil\le r_{\to}(n)\le n-2
\qquad(n\ge3).
\]

G2 uses `n-1` cells because it stores a directed Hamiltonian successor path over all generic points. Thus minimum rigidity cost is not successor-memory cost.

### U2. Terminal Generic Layer Master Lemma

For `m` new off-diagonal generic cells with terminal outputs, irrespective of terminal coloring,

\[
\boxed{
(EQ,NEQ,LEFT,RIGHT,NONE)
=
(4(N-1)+m,0,N^2+2N-2+m,N^2+N-2+m,N^3+N^2-4N+9-3m).
}
\]

The exact commutation correction is

\[
\boxed{
|\operatorname{Comm}|=3(N-1)+
|\{(u,v):(u,v),(v,u)\in A,\ c(u,v)=c(v,u)\}|.
}
\]

Hence Association Spectrum and commutation are coarse with respect to fine terminal-fiber geometry.

### U3. Same G4-C coarse invariants, but rigidity instead of C2

On five generic vertices use

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}.
\]

This tournament is asymmetric and non-self-converse. Coloring its arcs by one anonymous output and reverse arcs by the other gives a complete-domain balanced two-output zero-anchor layer with the same Association Spectrum and commutation as G4-C, but with full generic carrier group `1` rather than `C2`.

Adjoining successive universal sources preserves this for every `n>=5`.

### U4. Minimal separator: cyclic-triangle defect

Let

\[
\tau_3(T)=\#\{\text{cyclic induced generic triples}\}.
\]

No induced anonymous pattern invariant of arity at most two distinguishes tournament-type layers. At arity three, `tau3` is the unique independent scalar in the anonymous three-point histogram.

G4-C has

\[
\tau_3=0,
\]

while anonymous rigidity requires

\[
\tau_3\ge2.
\]

The rigid family from U3 has exactly two cyclic triples for every `n>=5`, so

\[
\boxed{
\min\{\tau_3(T):\operatorname{Aut}^{\pm}(T)=1\}=2.
}
\]

Equivalently,

\[
M_2(T)=\sum_v d_+(v)^2
=\frac{n(n-1)(2n-1)}6-2\tau_3(T).
\]

### U5. Histogram data and abstract half-reconstruction have different thresholds

`tau3` does not classify residual anonymous symmetry. More strongly, the explicit seven-vertex pair `S7/R7` in `FIBER_PROFILE_HIERARCHY.md` satisfies

\[
H_k^{\pm}(S_7)=H_k^{\pm}(R_7)
\quad(k=3,4,5,6),
\]

but

\[
\operatorname{Aut}^{\pm}(S_7)\cong C_2,
\qquad
\operatorname{Aut}^{\pm}(R_7)=1.
\]

Thus all proper anonymous histograms may agree while the final residual group differs.

Classically, finite tournaments are `(<=7)`-half-reconstructible and 7 is optimal when each local restriction is retained only up to abstract isomorphism/converse-isomorphism. This is a stronger coherent data model than histograms but still forgets labeled roles inside each local subset.

### U6. Exact stabilizer-complete compression: ternary anonymous betweenness

The search for a smaller stabilizer-complete object closes much earlier than the classical half-reconstruction ceiling once labeled local roles are allowed.

For pairwise distinct generic points define the derived ternary relation

\[
\boxed{
B_\star(x,y,z)
\iff
x\star y=y\star z=x\star z.
}
\]

No terminal output is named. In tournament language, `B(x,y,z)` means that the triple is transitive and `y` is its middle vertex. A cyclic triple has no middle vertex.

#### Betweenness Reconstruction Theorem

For tournaments `T,T'` on the same finite carrier,

\[
\boxed{
B_T=B_{T'}
\iff
T'=T\text{ or }T'=T^{op}.
}
\]

Proof idea: on every labeled 3-set, the betweenness pattern determines its tournament orientation up to reversal. Assign a sign `+/-` to each 3-set according as `T'` agrees with `T` or its converse. Two 3-sets sharing an edge must have the same sign, because that common edge cannot simultaneously agree and disagree with `T`. The graph of 3-sets joined when they share an edge is connected, so the sign is global.

Therefore

\[
\boxed{
\operatorname{Aut}(G_N,B_T)=\operatorname{Aut}^{\pm}(T).
}
\]

This is exactly the carrier group of the complete two-anonymous-output tournament layer. Hence `B` is a **carrier-exact ternary reduct**.

Arity three is minimal in the induced anonymous local-pattern class: one- and two-point tournament-type layers have only one anonymous local type.

#### Why the C3-hypergraph was insufficient

The cyclic-triple hypergraph

\[
\mathcal C_3(T)=\{X:T[X]\cong C_3\}
\]

forgets which vertex is the middle point of a transitive triple.

For G4-C it is empty, so its automorphism group is `S_n` while the tournament anonymous group is only `C2`.

For the rigid `T5`, the two hyperedges are

\[
\{0,1,3\},\qquad\{0,2,3\},
\]

and

\[
\operatorname{Aut}(\mathcal C_3(T_5))\cong C_2\times C_2,
\qquad
\operatorname{Aut}^{\pm}(T_5)=1.
\]

For the recursive rigid family, all added universal sources remain isolated in the cyclic-triple hypergraph, giving

\[
|\operatorname{Aut}(\mathcal C_3(T_n))|=4(n-4)!,
\]

while the tournament layer remains rigid. Thus the `C3`-hypergraph can have a factorial stabilizer error.

Classically, equality of tournament `C3`-structures is characterized by interval inversions; for indecomposable tournaments this ambiguity collapses to global duality. This explains exactly why `C3` works on prime tournaments but fails in decomposable layers.

Full proof, FCOA formula, small exhaustive checks through `n=5`, and literature reconciliation are in `BETWEENNESS_REDUCT.md`.

## Corrected information hierarchy

The previous `3 versus 7` statement needs a data-model qualifier, not a retraction:

\[
\boxed{
3=\text{minimal separator arity for G4-C vs rigidity},
}
\]

\[
\boxed{
7=\text{optimal arity for abstract subset half-reconstruction data},
}
\]

but

\[
\boxed{
3=\text{optimal arity for labeled anonymous role data, via }B_T.
}
\]

Thus the FCOA-specific stabilizer problem is strictly cheaper than generic half-reconstruction.

## Branch passport for U3–U6

- **Carrier/signature:** M0 backbone; complete off-diagonal generic terminal layer; two anonymous terminal outputs.
- **Defined cells:** all `n(n-1)` ordered distinct generic pairs.
- **Full generic carrier group:** `Aut^±(T)`.
- **Definedness group:** `S_n` on the generic sector relative to M0 boundary roles.
- **Commutation:** exactly M0, size `3n`, for tournament-type opposite fibers.
- **Association Spectrum:** exactly G4-C formula for every complete tournament-type terminal layer.
- **Three-point scalar:** G4-C `tau3=0`; minimum rigid defect `tau3=2`.
- **C3 incidence:** not stabilizer-complete in decomposable cases.
- **Exact reduct:** ternary `B_star(x,y,z) iff x star y = y star z = x star z`.
- **Exact reduct group:** `Aut(B_star)=Aut^±(T)`.
- **External output naming:** none.
- **Ordinary arithmetic imported:** no.

## Recommendation

Recommend upstream acceptance of U2, U3 scope-sharpening, U4, U5 with its data-model qualifier, and especially U6 after independent hostile review. Do not edit G4 from this subordinate branch.

U6 materially closes the stabilizer-compression question for tournament-type complete two-anonymous-output layers: the exact residual carrier group already lives in a natural ternary equality reduct of the operation.