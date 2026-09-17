# HATTER-SOL-11 · Orbital Port Filtrations

Branch: `research/hatter-sol-orbital-port-filtrations`

Base: merged `main` after HATTER-SOL-07--10 publication chain.

Status: **late-stage research / publication architecture phase**.

## Central question

Does a factor or minimal principalization witness carry canonical port-orbit information strictly finer than the HATTER-SOL folded pair `(P,Q)`, and how much of that information survives network optimization as host scale and geometry vary?

The now-established architecture is

\[
\boxed{
\text{arithmetic witness}
\to
\Omega\text{ (intrinsic orbital datum)}
\to
\Xi\text{ (orbit-total datum)}
\to
(P,Q)
\to
\text{network response}.
}
\]

HATTER-SOL-11 is therefore no longer searching for whether such an orbital layer exists. It now studies the exact **information-loss filtration** along these maps.

---

## 1. Hostile correction to naive strongest-first activation — CLOSED

The original naive claim

> the larger folded capacity `P` is an intrinsically stronger port orbit that must be saturated before `Q` activates

is false as a universal arithmetic law.

The orbit-fusion and geodesic classification establishes:

- generic imaginary-quadratic worlds have two natural direction orbits;
- Gaussian and Eisenstein worlds are orbit-fusion exceptions;
- a canonical orbital refinement exists;
- universal sequential activation does not.

Accordingly:

\[
\boxed{
\text{maximal-first is an optional probe, never a model axiom.}
}
\]

This publication warning remains mandatory.

---

## 2. Static forgetting map — CLOSED

For generic odd discriminants, the canonical orbital datum may be written

\[
\Omega=(|x|;\{|y|,|z|\}),
\]

with one axial orbit and one unordered oblique pair.

The folded pair `(P,Q)` is obtained by sorting the nonzero geodesic magnitudes and forgetting their orbit placement.

For an interior pair

\[
P>Q>0,
\]

the fiber has exactly three canonical orbital members:

\[
\boxed{
(P;\{Q,0\}),
\qquad
(Q;\{P,0\}),
\qquad
(0;\{P,Q\}).
}
\]

Under the canonical orbit-total projection

\[
\Xi=(A,O)=(a,b+c),
\]

these become

\[
\boxed{
(P,Q),
\qquad
(Q,P),
\qquad
(0,P+Q).
}
\]

The exact fiber sizes for boundary/diagonal/interior folded states are proved in `FORGETTING_MAP_FIBER_CLASSIFICATION.md`.

Thus the first major HATTER-SOL-11 requirement — a canonical nontrivial orbital refinement with an exact forgetting theorem — is satisfied.

---

## 3. Network-level separation — CLOSED AT SMALL HOST / FIXED FIBER LEVEL

`ORBITAL_NETWORK_FIBER_SEPARATION.md` proves that different members of one generic-odd forgetting fiber can have different network responses before folding.

Therefore `(P,Q)` is not merely a relabeling of the intrinsic interface structure: the information it forgets can be operationally visible.

This is the first strict separation

\[
\boxed{
\Omega\text{/}\Xi
\quad\text{finer than}\quad
(P,Q)
}
\]

at the network level.

---

## 4. Exact host-scale forgetting on unrestricted complete hosts — CLOSED

For an even complete host `K_{2m}` of degree

\[
c=2m-1,
\]

the three interior `Xi` states obey the exact three-stage law:

\[
\boxed{
\begin{array}{ccl}
c<P&:&3\text{ response classes},\\
P\le c<P+Q&:&2\text{ response classes},\\
c\ge P+Q&:&1\text{ closed class}.
\end{array}}
\]

Thus host scale induces a genuine operational forgetting filtration.

The optional maximal-first probe has a different collision relation and must not be substituted for the full Pareto response.

---

## 5. Strict 1D geometry — CLOSED

`GEOMETRY_ORBITAL_MEMORY_PATH_POLYNOMIAL.md` gives the exact path response polynomial.

For every generic-odd interior fiber and every even path size,

\[
\boxed{
Z_I^{1D},Z_{II}^{1D},Z_{III}^{1D}
\text{ are pairwise distinct.}
}
\]

Hence strict 1D preserves all three orbital states at every host scale:

\[
\boxed{3\to3\to3\to\cdots.}
\]

This is the first exact geometry-dependent memory theorem.

---

## 6. Outerplanar geometry — CLOSED IN THE `Xi` MODEL

The hostile outerplanar programme is complete for every generic-odd interior folded pair `P>Q>0` on even hosts.

The class-count law is

\[
\boxed{
\nu^{\Xi}_{O,n}(P,Q)=
\begin{cases}
2,&(P,Q)=(2,1),\\
3,&\text{otherwise}.
\end{cases}}
\]

The pure-oblique state never collides with either mixed state. The only mixed rank-swap collision is the exceptional fiber `(2,1)`.

Thus outerplanar geometry retains dramatically more orbital memory than unrestricted complete hosts.

---

## 7. Planar geometry — SUBSTANTIAL EXACT LAYER CLOSED; GLOBAL CLASSIFICATION NOT REQUIRED FOR PUBLICATION

The branch contains exact planar theorems at several levels.

### Platonic regular supports

For the even regular planar triangulations

\[
(n,d)=(4,3),(6,4),(12,5),
\]

the exact `Xi` Pareto front is known. The mixed rank swap collides exactly when

\[
\boxed{P\le d.}
\]

The class-count law is

\[
\boxed{
\nu^{\Xi}_{Pl,n}(P,Q)=
\begin{cases}
1,&P+Q=d,\\
2,&P+Q>d\text{ and }P\le d,\\
3,&P+Q>d\text{ and }P>d.
\end{cases}}
\]

This yields explicit host-scale trajectories such as

\[
(4,1):\qquad3\to2\to1
\]

along the planar host sequence `4 -> 6 -> 12`.

### Higher-order Gaussian `(6,5)` programme

The branch also contains a long exact planar balancing programme for the Gaussian state `(6,5)`, with orders through `44` closed and the `46` / `r=17` boundary partially closed.

This is valuable evidence and a separate technical spine, but **universal closure of the order-46 Gaussian case is no longer a publication prerequisite for HATTER-SOL-11**. It should not hold the conceptual paper hostage.

---

## 8. New unifying theorem — CLOSED

`REGULAR_FACTORIZABLE_HOST_ORBITAL_MEMORY_THEOREM.md` unifies complete-host and Platonic calculations.

For every connected even-order `d`-regular 1-factorizable host and every uniform `Xi=(A,O)` with

\[
A+O\ge d,
\]

the exact fixed-host Pareto response depends only on `(n,d)` and is

\[
\boxed{
B_A+B_O=n(A+O-d),
}
\]

with exact endpoint truncations

\[
B_A\ge n(A-d)_+,
\qquad
B_O\ge n(O-d)_+.
\]

For a generic-odd interior fiber this yields the universal degree-memory filtration

\[
\boxed{
\begin{array}{ccl}
d<P&:&3,\\
P\le d<P+Q&:&2,\\
d=P+Q&:&1.
\end{array}}
\]

This is currently the cleanest theorem-level expression of the title **Orbital Port Filtrations**.

Hostile correction: for `A+O<d`, 1-factorizability alone does not imply connected zero-boundary closure; a connected spanning factor condition is needed.

---

## 9. Residue-tail and network-collision side line — RETAIN, DO NOT LET IT DOMINATE THE PAPER

The binary-tail programme produced several exact results:

- local principalization-tail valence at most two;
- affine subset-product structure of global residue sectors;
- explicit `9 -> 5` folding loss in `Delta=-1155`;
- first genuine post-pair-flip network collision for `17^2`;
- exact binary-tail count-sector support theorem.

These results prove that arithmetic information can be lost at multiple stages:

\[
\text{exact residue}
\to
\text{orbital/folded state}
\to
\text{network Pareto response}.
\]

For HATTER-SOL-11 they should appear as a secondary information-loss section or appendix, not as the central narrative.

---

## 10. World/geometry/tomography extension — SECONDARY BUT PUBLISHABLE IF KEPT DISCIPLINED

The `61^6` laboratory establishes:

- nonzero world-geometry mixed response in the full typed/Pareto polynomial;
- simultaneous vanishing of the corresponding scalar mixed observable;
- exact projection-loss theorems;
- tropical Pareto tomography;
- finite-world tomographic dimension;
- a scalar splitting-character law on the nine UFD worlds.

These results are mathematically coherent, but they are one layer beyond the minimal orbital-port-filtration story.

For HATTER-SOL-11 publication they should be framed as **consequences of orbital information loss and coarse observation**, not allowed to obscure the main theorem spine.

The torus seed is explicitly deferred to later work.

---

## 11. Current publication spine

The recommended paper architecture is now:

1. **Motivation from HATTER-SOL-09/10:** `(P,Q)` is useful but potentially coarse.
2. **Intrinsic orbital geometry:** direction orbits and the Gaussian/Eisenstein fusion exceptions.
3. **No-go:** no universal strongest-first activation law.
4. **Exact forgetting-map fibers:** complete classification.
5. **Operational visibility:** same folded pair can give different orbital-network responses.
6. **Geometry-dependent memory:** exact path and outerplanar theorems.
7. **Regular-factorizable host theorem:** universal `3 -> 2 -> 1` degree filtration.
8. **Planar exact examples:** tetrahedron/octahedron/icosahedron and selected larger-order results.
9. **Information-loss extensions:** residue collisions and/or `61` tomography, selectively.
10. **Limits and deferred directions:** richer `Omega` semantics, full planar classification, torus/genus programme.

This is a coherent paper even without closing every Gaussian order-46 overload case.

---

## 12. What remains before publication candidate

The remaining work is primarily **synthesis and hostile audit**, not discovery of another giant theorem.

Mandatory tasks:

1. freeze one notation chain `Omega -> Xi -> (P,Q) -> Z` and remove local notation drift;
2. audit theorem assumptions, especially connectedness, host parity, regularity, factorization, and geometry-class versus fixed-host claims;
3. remove duplicated case theorems now subsumed by the regular-factorizable theorem, while retaining them as examples/proofs of hypotheses;
4. decide which secondary line belongs in the main paper and which moves to appendices;
5. create a theorem dependency map;
6. write the EN publication manuscript first, then RU counterpart;
7. run mandatory bibliography / DOI / numbering / RU-EN consistency audit.

## Publication threshold

**The mathematical threshold has now been crossed.**

HATTER-SOL-11 already contains a canonical nontrivial orbital refinement, a no-go theorem against a stronger naive hierarchy, an exact forgetting-fiber classification, geometry-dependent operational memory theorems, and a unifying host-degree filtration theorem.

The branch should now be treated as **publication-candidate construction**, not open-ended theorem hunting.
