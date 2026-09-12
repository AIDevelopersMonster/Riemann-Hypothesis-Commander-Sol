# HATTER-SOL-07 · Free-Port Factorization

**Russian title:** «Алиса в Стране Свободных Нитей: множители как узлы и точная цена мультипликативного расщепления»  
**English title:** “Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting”

- Series: **HATTER-SOL · Arithmetic Tea Party**
- Human author: **Малачевский А.А. / Malachevsky, A.A.**
- ORCID: **0009-0008-6009-3196**
- AI research collaborator / persona: **Commander Sol · Hatter Sol**
- Branch: `research/hatter-sol-free-ports`
- Zenodo DOI: **https://doi.org/10.5281/zenodo.22724185**
- YouTube video: **https://youtu.be/80rIpjZ3iuM**
- Interactive demo: `HATTER-SOL-07_INTERACTIVE.html`
- Publication status: **RU + EN release published on Zenodo; interactive HTML companion assembled; YouTube presentation published**

## Publication result

HATTER-SOL-07 develops the factor-capacity network viewpoint and proves the sharp one-step multiplicative-refinement bound

\[
\boxed{
\lambda(\ldots,a,b,\ldots)-\lambda(\ldots,ab,\ldots)
\le ab-a-b.
}
\]

The bound is attained for every pair `a,b>=2` in a suitable ambient capacity vector:

\[
\boxed{
\sup_{\text{ambient}}
\left[
\lambda(\ldots,a,b,\ldots)-\lambda(\ldots,ab,\ldots)
\right]
=ab-a-b.
}
\]

A fixed capacity vector remains classical maximum simple `b`-matching / `f`-bounded-subgraph territory. The contribution claimed here is the exact interaction between that deficiency and the arithmetic split `ab -> (a,b)`.

## Publication and media

- **Zenodo:** https://doi.org/10.5281/zenodo.22724185
- **YouTube presentation:** https://youtu.be/80rIpjZ3iuM
- **Interactive HTML companion:** `HATTER-SOL-07_INTERACTIVE.html`

## Interactive HTML companion

A standalone interactive demonstration is available in this directory as `HATTER-SOL-07_INTERACTIVE.html`.

Its core scenes are:

1. **One number — several factor architectures:** `12`, `3×4`, `2×2×3`.
2. **Tree vs cycle:** for fixed capacities, every added independent cycle changes the free boundary by exactly `-2`.
3. **Refinement inversion:** a more detailed multiplicative description can have a larger optimal free boundary.
4. **Sharp theorem explorer:** sliders for `a,b` display

   \[
   \delta(a,b)=ab-a-b
   \]

   together with the coarse saturated construction and the refined sharpness construction.
5. **Forward research bridge:** reserved controls for the next dimensional programme `1D | circle/outerplanar | 2D | 3D | square | triangle`, without treating those future models as already-proved results of HATTER-SOL-07.

The HTML is intended both as a reader-facing explanation and as an experimental front end for the later HATTER-SOL dimensional and geometry-transfer programme.

## Seed idea

Do not collapse a factorization immediately to its numerical product. Interpret each factor `m` as a node with `m` available connection ports. In a through-chain, one port is used by the incoming connection and one by the outgoing connection, leaving

\[
f(m)=m-2
\]

free external ports.

Thus a factorization

\[
n=a_1a_2\cdots a_k
\]

is represented as an ordered chain of factor-nodes with free-port count

\[
F(a_1,\ldots,a_k)=\sum_{i=1}^k(a_i-2).
\]

Examples:

\[
12:\quad F(12)=10,
\]

\[
12=3\cdot4:\quad F(3,4)=1+2=3,
\]

\[
12=2\cdot6:\quad F(2,6)=0+4=4,
\]

\[
12=2\cdot2\cdot3:\quad F(2,2,3)=1.
\]

The same integer therefore supports distinct connection architectures depending on how much multiplicative structure is exposed.

## General network model

For a connected simple graph `G=(V,E)` with vertex capacities `c_v>=2`, define

\[
B(G;\mathbf c)=\sum_v(c_v-\deg_Gv)=\sum_v c_v-2|E|.
\]

For connected `G`, with cycle rank

\[
\beta_1(G)=|E|-|V|+1,
\]

we have

\[
\boxed{
B(G;\mathbf c)=2+\sum_v(c_v-2)-2\beta_1(G).
}
\]

Thus, for fixed capacities, each additional independent cycle consumes exactly two free ports.

Define

\[
\lambda(\mathbf c)=\min_G B(G;\mathbf c),
\]

where the minimum is over connected simple graphs satisfying `deg(v_i)<=c_i`.

## Claim discipline

1. `m` as a node with `m` ports is a chosen model, not a canonical interpretation of multiplication.
2. The chain expression `f(m)=m-2` depends on the designated through-input / through-output convention.
3. Fixed-vector optimization is classical `b`-matching / `f`-bounded-subgraph theory.
4. Matula/Göbel-type number-to-tree encodings are classical and are not claimed as new.
5. The publication claim is the sharp multiplicative-split sensitivity law and its consequences, not the broad idea “number as graph.”
6. The dimensional `1D/2D/3D` and square/triangle/circle morphism programme belongs to subsequent HATTER-SOL research and is not retroactively claimed as part of the proved HATTER-SOL-07 theorem set.

## Research continuation

The next programme is intentionally split into distinct seeds:

- **Dimensional factor architectures:** compare admissible network classes in 1D, outerplanar/circular, planar 2D, and unrestricted/3D settings.
- **Integer as factorization state space:** represent `n=∏p_j^{e_j}` by its exponent vector and factorizations as vector partitions `e=α_1+...+α_k`, enriched by network fibres.
- **Geometry-transfer morphisms:** determine which invariants survive transfers among square, triangular, circular and other geometric realizations.

These continuations are tracked separately so that the published HATTER-SOL-07 theorem remains clean.

See `ARTICLE_RU_v0.9.md`, `STATUS.md`, `SHARP_REFINEMENT_BOUND.md`, `LITERATURE_AUDIT.md`, and the Zenodo record **10.5281/zenodo.22724185**.
