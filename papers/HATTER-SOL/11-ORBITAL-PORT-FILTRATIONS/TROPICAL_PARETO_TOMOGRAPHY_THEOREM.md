# HATTER-SOL-11 · TROPICAL PARETO TOMOGRAPHY THEOREM

**Status:** closed theorem layer.  
**Purpose:** determine exactly what is retained by all positive weighted scalarizations of a finite Pareto response, and prove what information is still lost relative to the full discrete response polynomial.

---

## 1. Weighted scalarization

Let

\[
S\subset\mathbb Z_{\ge0}^d
\]

be a finite response support. In the current two-channel setting `d=2` and a point is `(B_A,B_O)`.

For a positive weight vector

\[
w\in\mathbb R_{>0}^d
\]

define the tropical minimum

\[
\boxed{m_S(w):=\min_{x\in S}\langle w,x\rangle.}
\]

For a response polynomial

\[
Z=\sum_{x\in S}c_xX^x
\]

with positive support coefficients, write `m_Z=m_S`; multiplicities are ignored by this scalarization.

The ordinary scalar free-boundary minimum is the single sample

\[
m_S(1,1).
\]

---

## 2. Convexification is unavoidable

### Lemma TP11.1

For every finite `S` and every positive `w`,

\[
\boxed{m_S(w)=m_{\operatorname{conv}S}(w).}
\]

### Proof

A linear functional attains its minimum over a compact polytope at a vertex, and every vertex of `conv S` lies in `S` after redundant points are removed. Thus convexification does not change the minimum. QED.

Therefore weighted scalarization can never detect whether additional lattice points were inserted inside an already existing convex hull.

---

## 3. The positive lower hull

Let

\[
P=\operatorname{conv}S.
\]

Define the **positive lower hull** `LH_+(P)` to be the union of faces of `P` exposed by some normal vector in `R_{>0}^d`.

Equivalently, a face `F` belongs to `LH_+(P)` iff there exists `w>0` such that

\[
F=\operatorname*{argmin}_{x\in P}\langle w,x\rangle.
\]

The function `m_S` is the negative of the usual support function of `-P` restricted to the positive cone.

---

## 4. Exact tomography theorem

### Theorem TP11.2 — all positive weights determine exactly the positive lower convex envelope

Let `S,T` be finite subsets of `R_{>=0}^d`, with convex hulls `P=conv S` and `Q=conv T`. Then the following are equivalent:

1. `m_S(w)=m_T(w)` for every `w in R_{>0}^d`;
2. the closed upper completions coincide:

   \[
   \boxed{P+\mathbb R_{\ge0}^d=Q+\mathbb R_{\ge0}^d;}
   \]

3. `P` and `Q` have the same positive lower convex envelope, equivalently the same exposed lower faces for all positive normals with the same supporting values.

### Proof

By TP11.1 we may replace `S,T` by `P,Q`.

For any compact convex `P`, define the upper completion

\[
U_P=P+\mathbb R_{\ge0}^d.
\]

For `w>0`, adding a nonnegative vector can only increase `w·x`, hence

\[
\inf_{x\in U_P}w\cdot x=\min_{x\in P}w\cdot x=m_P(w).
\]

Thus `(2) => (1)`.

Conversely assume `(1)`. A closed convex upper set `U` is the intersection of its supporting halfspaces whose inward normals lie in the nonnegative cone:

\[
U=\bigcap_{w\in\mathbb R_{>0}^d}\{x:\langle w,x\rangle\ge \inf_{u\in U}\langle w,u\rangle\},
\]

with boundary directions obtained by limits from strictly positive normals. Equal minimum functions therefore give identical intersections, so `U_P=U_Q`. Hence `(1)=>(2)`.

The equivalence with `(3)` is exactly the statement that the minimal boundary of an upper completion is its positive lower convex envelope. QED.

---

## 5. What all weighted minima still cannot recover

### Theorem TP11.3 — discrete-support non-reconstruction

Knowledge of `m_S(w)` for **all** positive weights does not determine the discrete support `S`, even when `S` is Pareto-minimal.

### Proof by explicit counterexample

Take

\[
S_1=\{(0,4),(4,0)\},
\]

and

\[
S_2=\{(0,4),(2,2),(4,0)\}.
\]

Every point of each set is Pareto-minimal: no distinct point is coordinatewise smaller.

But

\[
\operatorname{conv}S_1=\operatorname{conv}S_2,
\]

so by TP11.1

\[
\boxed{m_{S_1}(w)=m_{S_2}(w)\quad\forall w>0.}
\]

Nevertheless

\[
S_1\ne S_2.
\]

Thus all positive weighted minima recover the lower convex geometry but not the lattice occupancy of that geometry. QED.

### Corollary TP11.3a

The response polynomials

\[
Z_1=Y^4+X^4,
\qquad
Z_2=Y^4+X^2Y^2+X^4
\]

have identical tropical minimum functions for all positive weights but are distinct polynomials.

Hence tropical tomography is strictly weaker than full polynomial response.

---

## 6. Information hierarchy

The current HATTER-SOL response layers therefore admit the strict hierarchy

\[
\boxed{
\text{one scalar weight}
\;<\;
\text{all positive weighted minima}
\;<\;
\text{full discrete Pareto support}
\;\le\;
\text{full typed/orbital response}.
}
\]

The first strict inequality occurs whenever two responses agree at the chosen weight but have different lower convex envelopes.

The second strict inequality is TP11.3.

The final inequality may also be strict because the same Pareto support can arise from different richer orbital states.

---

## 7. Piecewise-linear structure

### Proposition TP11.4

For finite `S`, the function

\[
w\mapsto m_S(w)
\]

is positively homogeneous, concave, and piecewise linear on the positive cone.

Its cones of linearity are the positive-normal cones of the exposed faces of the lower convex envelope.

### Proof

It is the pointwise minimum of finitely many linear forms `w -> w·x`. Positive homogeneity and concavity are immediate, and the active minimizer set is constant on the relative interior of each normal cone. QED.

Thus breakpoints of the weighted scalarization are genuine geometric observables of the Pareto front.

---

## 8. Reconstruction with extra discrete hypotheses

Full discrete reconstruction becomes possible only after adding information beyond the support function.

### Proposition TP11.5

Suppose it is known a priori that the support `S` consists of **all** lattice points in a specified lattice/coset `L` lying on its positive lower convex envelope. Then the pair

\[
(m_S,L)
\]

determines `S` exactly.

### Proof

TP11.2 reconstructs the lower convex envelope. Intersecting that envelope with the known lattice/coset `L` gives exactly `S` by hypothesis. QED.

This applies directly to theorem families in HATTER-SOL where parity and complete step-two occupancy of an exact segment have already been proved. In such families, tropical data plus the parity lattice can recover the full Xi Pareto support. Outside such a theorem, this inference is invalid.

---

## 9. Consequence for world spectra

For each arithmetic world `R`, one may form the tropical signature

\[
\boxed{\tau_R(w):=m_{Z_R}(w).}
\]

For fixed `w`, `R -> tau_R(w)` is an ordinary scalar world signal and can be analyzed by the world Laplacian.

Varying `w` produces a family of scalar world spectra.

However, TP11.3 warns that even the complete family

\[
\{\tau_R(w):w>0\}
\]

need not recover the full discrete response polynomial unless a discrete occupancy theorem is separately available.

Thus a world-spectrum tomography programme must explicitly state its reconstruction level:

1. one-weight scalar signal;
2. lower-convex-envelope signal from all weights;
3. discrete Pareto signal;
4. typed/orbital signal.

---

## 10. Immediate target for prime 61

For `N=61^6`, all four split-world 1D and planar Xi fronts are already exact. Therefore their weighted minima can be computed explicitly as piecewise-linear functions of `(w_A,w_O)`.

The next theorem target is to determine whether the family of weighted geometry gains

\[
\boxed{g_R(w):=m_{Z_{1D,R}}(w)-m_{Z_{Pl,R}}(w)}
\]

separates the four split worlds

\[
-4,-3,-19,-163
\]

that the single total-boundary weight `(1,1)` collapses.

This will measure exactly how much of the hidden typed world information can be recovered by tropical tomography before returning to the full polynomial response.
