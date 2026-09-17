# HATTER-SOL-11 · EN v0.3 Audited Patch Set

**Base manuscript:** `HATTER_SOL_11_EN_v0.2_publication_candidate.md`  
**Hostile audit:** `HATTER_SOL_11_V02_HOSTILE_AUDIT.md`  
**Status:** authoritative patch set. Applying every item below to v0.2 yields the intended EN v0.3 audited candidate.

## 1. Theorem 4.1: replace vague Type-III existence sentence

Replace the sentence

> All three occur, for example through suitable elements of the forms `P+QF`, `Q+PF`, and an element using the two oblique directions.

with the following self-contained text:

For the three interior placements take explicitly

\[
\alpha_I=P+QF,
\qquad
\alpha_{II}=Q+PF,
\qquad
\alpha_{III}=Q-(P+Q)F.
\]

The median-geodesic formula gives, respectively,

\[
(P,Q,0),
\qquad
(Q,P,0),
\qquad
(0,-P,-Q),
\]

up to sign and exchange of the two oblique slots. Hence the three orbital signatures

\[
(P;\{Q,0\}),
\qquad
(Q;\{P,0\}),
\qquad
(0;\{P,Q\})
\]

are all realized.

## 2. Outerplanar low-Q proof: make connectedness semantics explicit

In the `Q=1,2` construction, after introducing the perfect matching / Hamiltonian cycle in `H_n`, insert:

> The two channel edge sets partition `E(H_n)`. Therefore their union is the full connected host `H_n`. The HATTER connectedness requirement applies to this union; the individual channel subgraphs are not required to be connected. The remaining check is only the per-channel degree constraint.

Do not claim that the complementary color class is independently connected.

## 3. Novelty citation range

Where v0.2 says that the neighboring classical topics are covered by `[1--7]`, use `[1--8]` if the color-degree `b`-matching reference remains in the bibliography.

## 4. Notation normalization

Use consistently:

- `\bar F` for the conjugate basis element;
- `\Omega`, `\Xi`, `\Pi` in mathematical displays;
- `Z^{\Xi}_{O,n}` for outerplanar geometry-class response;
- `Z^{\Xi}_{Pl,n}` for planar geometry-class response;
- `Z_H^{\Xi}` only for a fixed host.

This prevents a fixed-host theorem from being visually confused with a geometry-class theorem.

## 5. Scope sentence to retain near Theorem 8.2

Keep the following warning immediately after the regular-factorizable theorem:

\[
S=A+O\ge d
\]

is part of the theorem. The underfull regime `S<d` is not covered by `(n,d)` universality because a selected union of `S` 1-factors may be disconnected.

## 6. Planar lifting sentence

In the planar section retain the independent extremality step:

> The tetrahedron, octahedron and icosahedron attain the global planar edge ceiling at their orders. Therefore the fixed-host lower-bound line from the regular-factorizable theorem is also the geometry-class lower-bound line at `n=4,6,12`.

Do not state or imply that every 1-factorizable planar host automatically gives the exact full planar-class response.

## 7. Icosahedral factorization audit

The explicit five perfect matchings printed in Appendix A were mechanically checked against the stated 30-edge icosahedral edge set. The check confirms:

- five matchings;
- six edges per matching;
- every displayed edge is an icosahedral edge;
- pairwise edge-disjointness;
- union size 30;
- union equals the entire icosahedral edge set.

The appendix can therefore retain the explicit factorization.

## 8. Bibliography gate

The following external references are acceptable in the v0.3 bibliography after metadata verification already recorded in the preliminary literature audit:

- Tutte (1947), factorization / perfect matching background;
- Hell & Kirkpatrick (1993), degree-constrained factors of minimum deficiency, DOI `10.1006/jagm.1993.1006`;
- Zhou & Nishizeki (1999), degree-constrained decompositions and edge coloring, DOI `10.1006/jctb.1998.1883`;
- Akiyama & Kano (2011), `[a,b]`-factorizations, DOI `10.1007/978-3-642-21919-1_5`;
- Brewster, McGuinness & Nielsen (2013), multiple degree constraints, DOI `10.1137/110850402`;
- Chetwynd & Hilton (1985), high-degree 1-factorization, DOI `10.1112/plms/s3-50.2.193`;
- Onn (2020), degree-sequence optimization, DOI `10.1016/j.orl.2020.10.010`;
- Anapolska et al. (2021), minimum color-degree perfect b-matchings, DOI `10.1002/net.21974`.

HATTER-SOL-07--10 must remain repository-series references until their final DOI/version metadata are individually verified.

## 9. Publication theorem spine after audit

The intended v0.3 main claims are now frozen as:

1. natural direction-orbit fusion occurs only at `Delta=-4,-3`;
2. no universal strongest-first activation law follows from the orbit filtration;
3. generic-odd shortest geodesics are given by the median formula;
4. `(P,Q)` is the magnitude-sorted forgetting of the direction-labelled geodesic;
5. every interior folded pair has exactly three canonical orbital placements;
6. all three are operationally visible on the two-node host;
7. strict 1D preserves all three at every even order;
8. outerplanar geometry has the unique mixed collision `(2,1)` and no mixed/pure collision;
9. connected even-order `d`-regular 1-factorizable hosts with `P+Q>=d` obey the exact Pareto interval theorem;
10. the interior response-class filtration is

\[
\boxed{
3\xrightarrow{d=P}2\xrightarrow{d=P+Q}1;
}
\]

11. at planar orders `4,6,12`, the Platonic extremal hosts lift this fixed-host theorem to the entire planar class;
12. the `(4,1)` fiber realizes the exact planar trajectory `3->2->1` on `4->6->12` vertices.

## 10. What is explicitly deferred

Not part of the v0.3 dependency graph:

- universal order-46 Gaussian `(6,5)` planar closure;
- prime-61 tomography/spectrum;
- residue-tail collisions;
- torus observability;
- surfaces/genus classification;
- full `Omega=(a;{b,c})` network semantics.

## 11. Gate

**Mathematical gate:** PASS after application of Sections 1--2 above.  
**Graph-literature gate:** PASS for publication-candidate wording; classical ingredients are not claimed as new.  
**Arithmetic-prior-art gate:** still requires one specialized final search before v1.0.  
**Metadata gate:** HATTER-SOL-07--10 DOI/version verification remains.  
**PDF/Zenodo gate:** not yet authorized.
