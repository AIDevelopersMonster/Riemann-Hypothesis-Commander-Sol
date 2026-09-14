# HATTER-SOL-11 · WORLD–GEOMETRY RESPONSE CALCULUS

**Status:** closed programme-level operator layer.  
**Scope:** rigorous calculus for comparing HATTER-SOL responses across arithmetic worlds, geometry classes, and host scales. This note does **not** claim novelty for graph Laplacians, finite differences, hypercube spectra, or algebraic-number-theory splitting laws. The mathematical content is the way these standard operators act on the HATTER-SOL arithmetic/network response field.

---

## 1. Correction of the naive product picture

The natural first slogan is

\[
\text{world}\times\text{geometry}\times\text{scale}.
\]

For a fixed rational integer, this is generally too naive.

If a rational prime `p` is raised to exponent `e`, then a split world produces two irreducible prime-factor species, hence `2e` factor-node occurrences, whereas an inert world produces only `e` factor-node occurrences. Thus the canonical host size itself depends on the arithmetic world.

Accordingly, for a fixed arithmetic probe `n`, the correct domain is an **admissible response complex**

\[
\boxed{
\mathscr D_n\subseteq
\mathscr W\times\mathscr G\times\mathscr K\times\mathscr S,
}
\]

where

- `\mathscr W` is a selected arithmetic-world graph;
- `\mathscr G` is a selected graph of justified geometry comparisons;
- `\mathscr K` is a host-scale set;
- `\mathscr S` denotes optional arithmetic sectors, such as principalization residues;
- only mathematically meaningful cells are included in `\mathscr D_n`.

The response is a map

\[
\boxed{
\mathcal Z_n:\mathscr D_n\longrightarrow \mathcal A,
}
\]

where `\mathcal A` is an additive response group.

For the current polynomial encoding one may take

\[
\mathcal A=\mathbb Z[X,Y]
\]

or an enlarged formal group when orbital or residue labels are retained. Passing from the Pareto semiring to its additive group is necessary because finite differences have signed coefficients.

This distinction will matter below: a same-integer world derivative need not be a fixed-host derivative.

---

## 2. World edges and geometry edges

Let `e=(R,R')` be an oriented arithmetic-world edge for which the two relevant response cells exist. Define the forward world difference

\[
D^W_e\mathcal Z
:=
\mathcal Z(R',\cdot)-\mathcal Z(R,\cdot).
\]

If `R'=T_qR` is a HATTER-SOL-09 prime toggle, then the HATTER-SOL-09 convention

\[
\nabla_q\mathcal Z(R)
=
\mathcal Z(R)-\mathcal Z(T_qR)
\]

satisfies

\[
\boxed{D^W_e=-\nabla_q.}
\]

Now let `f=(\mathcal C,\mathcal D)` be an oriented geometry-comparison edge. It need not be reversible; in the current programme it will usually come from a justified inclusion such as

\[
1D\subseteq O\subseteq Pl\subseteq A.
\]

Define

\[
\boxed{
D^G_f\mathcal Z
=
\mathcal Z(\cdot,\mathcal D)-\mathcal Z(\cdot,\mathcal C).
}
\]

No geometry Laplacian is asserted merely from this inclusion hierarchy.

Likewise, for two host scales `k,k'` for which the corresponding cells exist, define

\[
D^K_{k\to k'}\mathcal Z
=
\mathcal Z(\cdot,k')-\mathcal Z(\cdot,k).
\]

---

## 3. Mixed world–geometry response

On any complete response rectangle

\[
\{R,R'\}\times\{\mathcal C,\mathcal D\},
\]

define

\[
\boxed{
H_{e,f}\mathcal Z
:=D^W_eD^G_f\mathcal Z.
}
\]

Explicitly,

\[
\boxed{
H_{e,f}\mathcal Z
=
\mathcal Z(R',\mathcal D)
-\mathcal Z(R',\mathcal C)
-\mathcal Z(R,\mathcal D)
+\mathcal Z(R,\mathcal C).
}
\]

For a prime-toggle edge `R'=T_qR`, this is the mixed difference proposed in the programme note. In the old `\nabla_q=I-T_q` convention,

\[
H_{e,f}=-\nabla_qD^G_f\mathcal Z.
\]

### Proposition WR11.1 — coordinate differences commute

Whenever the full response rectangle exists,

\[
\boxed{
D^W_eD^G_f\mathcal Z
=
D^G_fD^W_e\mathcal Z.
}
\]

The same statement holds for any pair among world, geometry, and scale differences on a complete corresponding rectangle.

### Proof

Both sides expand to the same alternating sum of the four corner values. QED.

This is an algebraic commutation statement, not a curvature theorem. Any future nonzero curvature must come from a genuinely nontrivial transport rule, not from ordinary coordinate subtraction.

---

## 4. Exact separability criterion

The mixed difference has a stronger interpretation than merely being a diagnostic number.

Let `W` and `G` be connected finite graphs, and suppose every pair `(R,\mathcal C)\in V(W)\times V(G)` is an admissible response cell. Let

\[
Z:V(W)\times V(G)\to\mathcal A
\]

with `\mathcal A` any abelian group.

### Theorem WR11.2 — vanishing mixed response iff additive separability

The following are equivalent.

1. For every world edge `e` and every geometry edge `f`,

   \[
   H_{e,f}Z=0.
   \]

2. There exist maps

   \[
   F:V(W)\to\mathcal A,
   \qquad
   G:V(G)\to\mathcal A
   \]

   such that

   \[
   \boxed{Z(R,\mathcal C)=F(R)+G(\mathcal C)}
   \]

   for all `(R,\mathcal C)`.

### Proof

`(2) => (1)` is immediate: the alternating four-corner sum cancels both the pure world and pure geometry terms.

For `(1) => (2)`, fix base vertices `R_0` and `\mathcal C_0`. Define

\[
F(R):=Z(R,\mathcal C_0)-Z(R_0,\mathcal C_0),
\qquad
G(\mathcal C):=Z(R_0,\mathcal C).
\]

Because every mixed edge difference vanishes, the world-edge increment

\[
Z(R',\mathcal C)-Z(R,\mathcal C)
\]

is unchanged when `\mathcal C` is moved across one geometry edge. Since `G` is connected, that increment is independent of `\mathcal C`.

Now choose any world path from `R_0` to `R` and telescope its edge increments. Their independence of `\mathcal C` gives

\[
Z(R,\mathcal C)-Z(R_0,\mathcal C)
=
Z(R,\mathcal C_0)-Z(R_0,\mathcal C_0)
=F(R).
\]

Therefore

\[
Z(R,\mathcal C)=F(R)+Z(R_0,\mathcal C)=F(R)+G(\mathcal C).
\]

QED.

### Corollary WR11.2a — rigorous coupling certificate

If one complete world–geometry rectangle has

\[
\boxed{H_{e,f}Z\ne0,}
\]

then the response cannot be written as a sum of a world-only term and a geometry-only term.

Thus a nonzero mixed response is a rigorous certificate that arithmetic-world sensitivity and geometric sensitivity are coupled.

Conversely, on a connected complete laboratory, vanishing of **all** mixed differences proves exact additive decoupling.

---

## 5. Partial domains: what survives

For the actual HATTER-SOL response field, `\mathscr D_n` need not contain the whole Cartesian product.

On every admissible four-cell rectangle, Proposition WR11.1 and the local coupling test remain exact.

However, the global converse in Theorem WR11.2 requires enough rectangles to connect the product domain. If cells are missing, one must not infer global separability merely from all mixed differences that happened to be computable.

This is the first reason to retain the admissible-domain structure explicitly rather than silently filling unavailable cells.

---

## 6. Fixed-host versus same-integer world derivatives

Let `\kappa_R(n)` be the canonical factor-node count of the fixed arithmetic probe `n` in world `R` under the selected factor/ideal semantics.

For a world edge `e=(R,R')`, define the **same-integer derivative**

\[
\boxed{
D^{\mathrm{can}}_e\mathcal Z_n
:=
\mathcal Z_n(R',\kappa_{R'}(n))
-
\mathcal Z_n(R,\kappa_R(n)).
}
\]

This is the canonical derivative of the actual integer representation.

By contrast, when both synthetic fixed-host cells exist, define

\[
\boxed{
D^{W,k}_e\mathcal Z_n
:=
\mathcal Z_n(R',k)-\mathcal Z_n(R,k).
}
\]

The latter isolates the effect of changing world while holding the host size fixed. It is a controlled network experiment, but it need not compare canonical factorizations of the same integer.

### Proposition WR11.3 — exact world/scale decomposition

Assume the cells

\[
(R,\kappa_R(n)),
\quad
(R',\kappa_R(n)),
\quad
(R',\kappa_{R'}(n))
\]

all exist. Then

\[
\boxed{
D^{\mathrm{can}}_e\mathcal Z_n
=
D^{W,\kappa_R(n)}_e\mathcal Z_n
+
D^K_{\kappa_R(n)\to\kappa_{R'}(n)}
\mathcal Z_n(R',\cdot).
}
\]

### Proof

Add and subtract `\mathcal Z_n(R',\kappa_R(n))`. QED.

This identity is elementary but conceptually essential: an observed same-integer world jump can contain both a change of arithmetic interface and a change of canonical host scale.

Therefore the programme should report both quantities whenever the synthetic fixed-scale comparison is mathematically meaningful.

---

## 7. Prime 61 shows why the distinction is unavoidable

Take the same integer

\[
N=61^{23}.
\]

Across the nine imaginary quadratic class-number-one UFD worlds, `61` is split in discriminants

\[
-4,-3,-19,-163
\]

and inert in

\[
-8,-7,-11,-43,-67.
\]

Hence

\[
\boxed{
\kappa_R(61^{23})=
\begin{cases}
46,&61\text{ split in }R,\\
23,&61\text{ inert in }R.
\end{cases}}
\]

The split-world folded states are

\[
\begin{array}{c|c}
\Delta & \Pi_\Delta(61)\\
\hline
-4&(6,5)\\
-3&(5,4)\\
-19&(7,1)\\
-163&(4,1).
\end{array}
\]

The inert worlds retain the rational-line state `(61,0)`.

Thus comparing a split world to an inert world at fixed `k=46` is **not** the canonical same-integer derivative of `61^{23}`. The canonical inert representation has only 23 nodes.

This corrects the naive interpretation of a world-indexed planar table at fixed host size.

---

## 8. Sector labels from HATTER-SOL-10

HATTER-SOL-10 shows that a nonprincipal ideal may have several minimal witness states and that a principalization residue can select a global witness-composition sector.

The residue is not a third additive boundary coordinate. Therefore the response domain should be refined as

\[
(R,\mathcal C,k,\mathfrak r)
\]

with `\mathfrak r` a **sector label**.

One may encode sectors formally, for example in a group algebra with labels `e_{\mathfrak r}`, and then take finite differences coefficientwise. But no physical meaning should be assigned to subtracting residue ideals themselves as though they were port capacities.

The response-field viewpoint therefore inherits the exact HATTER-SOL-10 distinction:

\[
\boxed{
\text{network resources are coordinates; arithmetic residues are sector selectors.}
}
\]

---

## 9. Arithmetic operations: the correct multiplication baseline

The first programme note proposed a generic multiplication defect

\[
Z(nm)-\Phi_\times(Z(n),Z(m)).
\]

HATTER-SOL-10 makes this more precise.

For block-disjoint factor systems there is an exact residue/Pareto convolution law. When cross-edges are subsequently allowed, the fully interacting network can improve on that block baseline. Therefore the canonical first multiplication experiment should compare

\[
\boxed{
Z_{\mathrm{full}}(nm)
\quad\text{against}\quad
Z_{\mathrm{blk}}(n,m),
}
\]

where `Z_blk` is built from the proved block-disjoint convolution, not from an invented multiplicative law.

In the additive polynomial group define the formal interaction difference

\[
\boxed{
\mathfrak D_{\mathrm{int}}(n,m)
:=
Z_{\mathrm{full}}(nm)-Z_{\mathrm{blk}}(n,m).
}
\]

Signed polynomial coefficients are expected; this object records how the Pareto support changes after interaction and is not itself a nonnegative scalar.

For a chosen nonnegative weighted utilization objective `h`, one may additionally define the scalar gain

\[
\boxed{
g_{\mathrm{int}}
:=h_{\mathrm{full}}-h_{\mathrm{blk}}\ge0,
}
\]

because the block-disjoint realization is a feasible baseline inside the larger interacting problem.

This is the publication-safe form of the first multiplication-defect programme.

---

## 10. Three-way response and the road to genuine curvature

Whenever an eight-cell box in world, geometry, and scale is admissible, define the third mixed difference

\[
D^W D^G D^K\mathcal Z.
\]

It measures the part of the response that cannot be removed by lower-order additive contributions in the three coordinates.

Ordinary coordinate differences commute, so this object is a higher interaction tensor, **not curvature**.

A genuine curvature concept would require a nontrivial transport rule between response fibers — for example, a canonical rule that transports witness/orbital states across world changes and host-scale changes. Only then can path dependence or holonomy be tested honestly.

The present note therefore draws a strict line:

- finite differences and mixed Hessians: established now;
- response coupling and separability tests: established now;
- a connection/transport law: open;
- curvature/holonomy: open until such transport is defined.

---

## 11. Immediate research consequences

The next computations should no longer be organized as a single monotone march in Gaussian `r`.

For each selected probe, construct an admissible-cell table containing

1. arithmetic world and split/inert/ramified status;
2. canonical factor-node count `\kappa_R(n)`;
3. typed/orbital local state;
4. geometry class;
5. host scale;
6. arithmetic sector if present;
7. exact response polynomial or a clearly marked unresolved cell;
8. proof regime responsible for the cell.

Then compute, wherever complete rectangles exist,

\[
D^W Z,
\qquad
D^G Z,
\qquad
D^K Z,
\qquad
H_{W,G}Z,
\qquad
H_{W,K}Z,
\qquad
H_{G,K}Z.
\]

The first global question is no longer merely whether two worlds give different responses. It is:

\[
\boxed{
\text{which parts of the response are world-only, geometry-only, scale-only,}\
\text{and which parts are irreducibly coupled?}
}
\]

That is the operator-level continuation of HATTER-SOL-07 through HATTER-SOL-11.
