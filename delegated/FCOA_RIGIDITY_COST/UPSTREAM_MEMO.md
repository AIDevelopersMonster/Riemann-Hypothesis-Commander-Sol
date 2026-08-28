# FCOA Rigidity Cost — Upstream Memo

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Audience:** main Commander Sol scientific director  
**Status:** local results proposed for upstream review; nothing here modifies M0–G4 automatically.

## Executive verdict

Seven results from this direction are strong enough for upstream review.

### U1. Rigidity cost is not successor-memory cost

Let `n=N-1` be the generic carrier size and

\[
r_{\to}(n)=\min\{|A|:\operatorname{Aut}(X,A)=1\}.
\]

Exact values through `n=7` are `(1,1,2,3,3,4)`, with elementary bounds

\[
\left\lceil\frac{n-1}{2}\right\rceil\le r_{\to}(n)\le n-2.
\]

G2 spends `n-1` cells because it stores a chosen global successor path, not because that is the minimum cost of killing automorphisms.

### U2. Terminal Generic Layer Master Lemma

For `m` new off-diagonal generic cells with terminal outputs,

\[
(EQ,NEQ,LEFT,RIGHT,NONE)
=
(4(N-1)+m,0,N^2+2N-2+m,N^2+N-2+m,N^3+N^2-4N+9-3m).
\]

The exact commutation correction is

\[
|\operatorname{Comm}|=3(N-1)+|\{(u,v):(u,v),(v,u)\in A,\ c(u,v)=c(v,u)\}|.
\]

Thus Association Spectrum and commutation are coarse with respect to fine terminal-fiber geometry.

### U3. Same G4-C coarse invariants, but rigidity instead of C2

The five-vertex tournament

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}
\]

is asymmetric and non-self-converse. Its two anonymous opposite fibers give a complete balanced zero-anchor layer with the same Association Spectrum and commutation as G4-C, but full generic group `1` rather than `C2`. Adjoining successive universal sources preserves this for every `n>=5`.

### U4. Minimal separator: cyclic-triangle defect

Let

\[
\tau_3(T)=\#\{\text{cyclic induced generic triples}\}.
\]

G4-C has `tau3=0`; anonymous rigidity requires `tau3>=2`; the U3 family has exactly `tau3=2` for every `n>=5`. Hence

\[
\min\{\tau_3(T):\operatorname{Aut}^{\pm}(T)=1\}=2.
\]

Equivalently,

\[
M_2(T)=\sum_vd_+(v)^2=\frac{n(n-1)(2n-1)}6-2\tau_3(T).
\]

### U5. Histogram data and abstract half-reconstruction have different thresholds

There is an explicit seven-vertex pair `S7/R7` with

\[
H_k^{\pm}(S_7)=H_k^{\pm}(R_7)\quad(k=3,4,5,6),
\]

but

\[
\operatorname{Aut}^{\pm}(S_7)\cong C_2,
\qquad
\operatorname{Aut}^{\pm}(R_7)=1.
\]

Thus all proper anonymous histograms may agree while the final residual group differs. Classically, finite tournaments are `(<=7)`-half-reconstructible, with 7 optimal for the different data model in which each local restriction is retained only up to abstract isomorphism/converse-isomorphism.

### U6. Tournament specialization: exact ternary betweenness reduct

For tournament-type opposite fibers define

\[
B_\star(x,y,z)\iff x\star y=y\star z=x\star z.
\]

Then

\[
B_T=B_{T'}\iff T'=T\text{ or }T'=T^{op},
\]

and therefore

\[
\operatorname{Aut}(B_T)=\operatorname{Aut}^{\pm}(T).
\]

This is a carrier-exact ternary reduct. The full `C3`-hypergraph is not exact in decomposable cases; for the recursive rigid family its stabilizer has size `4(n-4)!` while the tournament layer is rigid. Full proof is in `BETWEENNESS_REDUCT.md`.

### U7. Universal ternary phase reduct — tournament condition is unnecessary

The U6 phenomenon extends to **every** complete off-diagonal two-anonymous-output generic layer, with no assumption relating opposite cells.

Let `c(x,y)` be a temporary binary coding of the two anonymous fibers. Define

\[
\boxed{
Q_\star(x,y,z)\iff x\star y=y\star z,
}
\]

for `x!=y`, `y!=z`, with `x=z` allowed.

Then

\[
\boxed{
\operatorname{Aut}(G_N,Q_\star)=\operatorname{Aut}^{\pm}(c).
}
\]

#### Proof mechanism

For a permutation `g` preserving `Q`, define the cell phase discrepancy

\[
\delta_g(x,y)=c(gx,gy)\oplus c(x,y).
\]

Preservation of equality between composable cells gives

\[
\delta_g(x,y)=\delta_g(y,z).
\]

The graph on all ordered off-diagonal cells, joining `(x,y)` to `(y,z)`, is connected for every `n>=2` (for `n=2`, `(x,y)` and `(y,x)` are adjacent because `z=x` is allowed). Hence `delta_g` is globally constant. Therefore `g` either preserves every fiber or swaps the two fibers globally, exactly as required.

Consequences:

1. **Tournament condition is unnecessary.** Same-valued reverse cells are allowed.
2. **Balancedness is unnecessary.** If fibers have unequal cardinalities, the global-swap coset is simply empty.
3. A naive four-variable equality relation comparing arbitrary cells is unnecessary; composable-cell equality already propagates the global phase.
4. The tournament betweenness reduct `B` is a geometric specialization of the more primitive `Q` theorem.
5. Arity three remains optimal in the induced anonymous local-pattern class, since the tournament subclass already supplies the two-point obstruction.

Thus

\[
\boxed{
k_{\rm exact}=3}
\]

for the entire complete two-anonymous-output class, not merely the tournament subclass.

Full theorem, proof, phase interpretation, and scope firewall are in `UNIVERSAL_TERNARY_PHASE_REDUCT.md`.

## Corrected structural hierarchy

The branch now separates three questions:

\[
3=\text{minimal scalar/local separator arity for G4-C vs rigidity},
\]

\[
7=\text{optimal arity for classical abstract tournament half-reconstruction data},
\]

but

\[
\boxed{
3=\text{optimal exact stabilizer arity for complete binary anonymous value layers}.
}
\]

The last statement is U7 and strictly subsumes the tournament-only exactness question.

## Branch passport for U7

- **Carrier/signature:** M0 backbone plus complete off-diagonal generic terminal layer.
- **Number of terminal outputs:** exactly two distinct anonymous values.
- **Tournament assumption:** none.
- **Balanced assumption:** none.
- **Defined cells:** all `n(n-1)` ordered distinct generic pairs.
- **Definedness group:** `S_n` relative to M0 boundary roles.
- **Exact derived reduct:** `Q_star(x,y,z) iff x star y = y star z`.
- **Exact carrier group:** `Aut(Q_star)=Aut^±(c)`.
- **Commutation:** unrestricted by the theorem.
- **Association Spectrum:** complete terminal-domain formula; `Q` is derived rather than an added cell layer.
- **External output naming:** none.
- **Ordinary arithmetic imported:** no.

## Recommendation

Recommend upstream acceptance of U7 after independent hostile review. It materially supersedes U6 as the general stabilizer-compression theorem, while U6 remains useful because its betweenness interpretation exposes the order geometry of G4-C.

Do not edit G4 from this subordinate branch.

The next boundary is now sharply located: either **more than two anonymous output fibers** or **non-complete/sparse domains**, where binary phase propagation and automatic cell-graph connectivity respectively cease to be immediate.