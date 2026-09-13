# HATTER-SOL-09 · World-Dependent Factor Networks and a Prime-Toggle Response Operator

**Malachevsky, A.A.**  
ORCID: `0009-0008-6009-3196`  
Date: 2026-09-13  
Series: HATTER-SOL · Arithmetic Tea Party  
Status: preprint candidate v0.9

## Abstract

A positive integer may have different irreducible factorizations after it is embedded into different quadratic arithmetic worlds. Classical algebraic number theory describes this split/inert/ramified behavior, but it does not ask how the resulting factorization changes a degree-constrained network built from the factors. This paper composes these two structures.

For the Gaussian and Eisenstein worlds, each irreducible factor is assigned a canonical two-interface capacity pair `(P,Q)` obtained from a symmetry-reduced shortest-step description of the lattice. A typed factor network is then a simple graph whose edges consume either `P`-capacity or `Q`-capacity, with at most one edge per unordered vertex pair. Its response is the Pareto frontier of the remaining two-component boundary. The ordinary scalar HATTER-SOL free boundary is recovered by forgetting the edge type.

The typed response is strictly finer. The prime `37` has the same scalar boundary in the Gaussian and Eisenstein worlds but different typed Pareto frontiers. The composite integer `15` gives a heterogeneous scalar collision of the same kind, while `65` changes even the lattice shape of the Pareto frontier. For uniform split-prime powers an exact Pareto-front formula is obtained, together with two thresholds: an interface-forgetting threshold and a later full-closure threshold.

To compare arithmetic worlds canonically, quadratic fields are organized by prime toggles of squareclasses. Multiplication of a negative squareclass by a rational prime is an involution, and finitely many prime toggles generate a hypercube. The typed Pareto frontier is encoded by a polynomial-valued signal

\[
Z_R(n;X,Y)=\sum_{(b_P,b_Q)\in\partial_P\mathfrak B_R^{(2)}(n)}X^{b_P}Y^{b_Q}.
\]

The standard graph Laplacian on the prime-toggle cube then acts coefficientwise on this arithmetic-network response. The novelty claim is deliberately narrow: the paper does not claim new Gaussian/Eisenstein splitting laws, new `(g,f)`-factor theory, new hypercube spectra, or a new graph Laplacian. The proposed contribution is the composition

\[
\text{world-dependent arithmetic factorization}
\to
\text{typed factor network}
\to
\text{Pareto response}
\to
\text{canonical world derivative/Laplacian}.
\]

---

## 1. Motivation and relation to HATTER-SOL-07

HATTER-SOL-07 represents a factorization

\[
n=a_1\cdots a_k
\]

by a simple graph with degree capacities `a_i`. If `G` is connected and

\[
\deg_G(v_i)\le a_i,
\]

the free boundary is

\[
B(G;a)=\sum_i a_i-2|E(G)|,
\]

and the optimized scalar response is

\[
\lambda(a)=\min_G B(G;a).
\]

That construction keeps the arithmetic factorization fixed. The present work changes the arithmetic world first. The same rational integer `n` may be inert in one quadratic ring and split in another; therefore the factor nodes themselves change before the network optimization begins.

The central question is:

> Can world-dependent arithmetic factorization be converted into a canonical network response that is comparable across worlds without erasing the geometric information carried by the factorization?

The answer developed below is yes, but a scalar capacity is not sufficient. Two interface types are required.

---

## 2. Two arithmetic worlds and their canonical typed factors

### 2.1 Gaussian world

For

\[
\alpha=a+bi\in\mathbb Z[i],
\]

define the folded typed pair

\[
\boxed{
\Pi_G(\alpha)
=(P_G,Q_G)
=(\max(|a|,|b|),\min(|a|,|b|)).
}
\]

This is invariant under multiplication by the Gaussian units and under conjugation. The scalar shortest-step capacity is

\[
\boxed{\rho_G(\alpha)=P_G+Q_G=|a|+|b|.}
\]

The norm is

\[
N_G(\alpha)=P_G^2+Q_G^2.
\]

### 2.2 Eisenstein world

Use the adjacent-unit generator

\[
\eta=1+\omega=e^{i\pi/3},
\qquad \eta^2-\eta+1=0.
\]

Every factor orbit under units and conjugation has a representative

\[
P_E+Q_E\eta,
\qquad P_E\ge Q_E\ge0.
\]

Define

\[
\boxed{\Pi_E(\alpha)=(P_E,Q_E).}
\]

Then

\[
\boxed{\rho_E(\alpha)=P_E+Q_E}
\]

and

\[
N_E(\alpha)=P_E^2+P_EQ_E+Q_E^2.
\]

Equivalently, if `alpha=a+b omega`, sort

\[
|a|,\ |b|,\ |a-b|
\]

as `Q<=P<=P+Q`; the two smaller values give `(P_E,Q_E)` after ordering decreasingly.

### Proposition 2.1 — recovery of the rational line

For every positive rational integer `m`,

\[
\boxed{\rho_G(m)=\rho_E(m)=m.}
\]

Hence the old HATTER-SOL scalar degree-capacity is recovered exactly on the embedded rational line.

### Remark 2.2 — classical arithmetic boundary

The Gaussian and Eisenstein norm forms, unit actions, and split/inert/ramified laws are classical. They are inputs to the present construction, not novelty claims.

---

## 3. Typed simple-support factor networks

Let the world factorization of `n` produce irreducible factor nodes with canonical typed capacities

\[
\Pi=((P_1,Q_1),\ldots,(P_k,Q_k)).
\]

A **typed simple-support network** consists of a connected simple support graph on these factor nodes, with every edge labelled `P` or `Q`, such that

\[
d_P(v_i)\le P_i,
\qquad
d_Q(v_i)\le Q_i,
\]

and at most one edge total is allowed on each unordered vertex pair.

Define

\[
B_P=\sum_iP_i-2|E_P|,
\qquad
B_Q=\sum_iQ_i-2|E_Q|.
\]

The attainable boundary region is

\[
\mathfrak B^{(2)}(\Pi)
=\{(B_P,B_Q):\text{admissible connected typed networks}\}.
\]

Its Pareto-minimal subset is

\[
\boxed{\partial_P\mathfrak B^{(2)}(\Pi).}
\]

The scalar HATTER-SOL projection is

\[
(B_P,B_Q)\mapsto B_P+B_Q.
\]

Thus the typed model refines rather than replaces the old scalar free boundary.

---

## 4. Exact two-node response and the first scalar collision

Consider two identical factor nodes with capacity `(P,Q)`, `P>=Q>0`. Connectivity forces one support edge, which may have either type.

### Theorem 4.1 — two-node Pareto frontier

\[
\boxed{
\partial_P\mathfrak B^{(2)}(P,Q)
=\{(2P-2,2Q),(2P,2Q-2)\}.
}
\]

Both points have scalar sum

\[
2(P+Q)-2.
\]

The midpoint of their imbalance coordinates `B_P-B_Q` recovers `P-Q`; together with `P+Q`, the frontier therefore determines `(P,Q)` exactly.

### Example 4.2 — the prime 37

The prime `37` splits in both worlds.

Gaussian:

\[
37=6^2+1^2,
\qquad
\Pi_G(37)=(6,1),
\]

so

\[
\boxed{
\partial_P\mathfrak B_G^{(2)}(37)
=\{(10,2),(12,0)\}.
}
\]

Eisenstein:

\[
37=7^2-7\cdot3+3^2,
\qquad
\Pi_E(37)=(4,3),
\]

so

\[
\boxed{
\partial_P\mathfrak B_E^{(2)}(37)
=\{(6,6),(8,4)\}.
}
\]

In both worlds the scalar minimum is `12`, but the typed frontiers differ. Hence

\[
\boxed{
\text{same scalar network response}
\not\Rightarrow
\text{same typed world response}.
}
\]

---

## 5. Uniform powers and interface-memory dynamics

Let `k=2m` identical nodes have typed capacity `(P,Q)`, `P>=Q>=0`, and put

\[
S=P+Q,
\qquad c=k-1.
\]

### Theorem 5.1 — exact uniform Pareto frontier

If

\[
S\le c,
\]

then

\[
\boxed{\partial_P\mathfrak B_k^{(2)}(P,Q)=\{(0,0)\}.}
\]

If

\[
S>c,
\]

define

\[
D_k=k(S-c),
\]

\[
L_P=k(P-c)_+,
\qquad
L_Q=k(Q-c)_+.
\]

Then

\[
\boxed{
\partial_P\mathfrak B_k^{(2)}(P,Q)
=
\{(B_P,B_Q):
B_P+B_Q=D_k,
\ L_P\le B_P\le D_k-L_Q,
\ B_P\equiv0\pmod2\}.
}
\]

The proof uses almost-regular realizations and complements in the complete support graph.

### Definition 5.2 — interface-forgetting threshold

\[
\boxed{
\sigma(P,Q)=\left\lceil\frac{P+1}{2}\right\rceil.
}
\]

For `m>=sigma`, the Pareto frontier is centered at zero imbalance and no longer retains the intrinsic split `P-Q` in its center.

### Definition 5.3 — full-closure threshold

\[
\boxed{
\tau(P,Q)=\left\lceil\frac{P+Q+1}{2}\right\rceil.
}
\]

For `m>=tau`, the frontier is `{(0,0)}`.

Hence

\[
\boxed{\sigma(P,Q)\le\tau(P,Q),}
\]

and an intermediate regime may occur in which the network remains open while its directional interface memory has already vanished.

### Example 5.4 — 53 in the square world

For the split Gaussian factor of `53`,

\[
(P,Q)=(7,2).
\]

Thus

\[
\boxed{\sigma_G(53)=4,\qquad\tau_G(53)=5.}
\]

The network is still open at the fourth power but its Pareto center has already forgotten the original interface imbalance; closure occurs at the fifth power.

---

## 6. Heterogeneous arithmetic blocks

For an arbitrary typed profile, exact zero boundary requires two edge-disjoint realizations of prescribed degree sequences. This contains the classical degree-sequence packing problem, which is NP-complete in general. Therefore the arithmetic structure of the profile must be exploited rather than replaced by a universal closed scalar formula.

### 6.1 One axial block plus one split block

Consider

\[
\Pi=(a,0)^r\cup(P,Q)^n,
\qquad n=2m,
\qquad N=r+n.
\]

### Theorem 6.1 — complete-support criterion

Complete typed support `K_N` exists if and only if

\[
\boxed{a\ge N-1}
\]

and

\[
\boxed{P+\min(Q,n-1)\ge N-1.}
\]

In this regime the global Pareto frontier is an exact parity segment. Put

\[
D=ra+n(P+Q)-N(N-1),
\]

\[
L_P=r(a-N+1)+n(P-N+1)_+,
\]

\[
L_Q=n(Q-n+1)_+.
\]

Then

\[
\boxed{
\partial_P\mathfrak B^{(2)}(\Pi)
=\{(B_P,B_Q):
B_P+B_Q=D,
\ L_P\le B_P\le D-L_Q,
\ B_P\equiv ra\pmod2\}.
}
\]

### Example 6.2 — 6

Gaussian:

\[
\Pi_G(6)=(3,0)\cup(1,1)^2,
\qquad
\partial_P\mathfrak B_G^{(2)}(6)=\{(1,0)\}.
\]

Eisenstein:

\[
\Pi_E(6)=(2,0)\cup(1,1)^2,
\qquad
\partial_P\mathfrak B_E^{(2)}(6)=\{(0,0)\}.
\]

Thus `6` is a heterogeneous closure separator.

### Example 6.3 — 15

Gaussian:

\[
\partial_P\mathfrak B_G^{(2)}(15)=\{(1,2),(3,0)\}.
\]

Eisenstein:

\[
\partial_P\mathfrak B_E^{(2)}(15)=\{(3,0)\}.
\]

Both scalar minima equal `3`, so `15` is a heterogeneous scalar collision.

---

## 7. Complete support as a `(g,f)`-factor problem

For a general typed profile on `N` nodes, complete support means coloring every edge of `K_N` either `P` or `Q`. Choose the `P`-edge subgraph `H`; the complement is then the `Q`-graph.

For node `i`, put

\[
g_i=\max(0,N-1-Q_i),
\qquad
f_i=\min(P_i,N-1).
\]

### Theorem 7.1 — exact reduction

Complete typed support exists if and only if `K_N` has a `(g,f)`-factor satisfying

\[
g_i\le d_H(v_i)\le f_i.
\]

This permits the use of Lovasz's classical `(g,f)`-factor theorem.

For two block-constant arithmetic classes, the general disjoint-set test collapses to four block counts. This gives a finite low-dimensional obstruction landscape, but the present paper uses the exact reduction only as structural support; the principal world response is the Pareto frontier itself.

### Example 7.2 — 65

Gaussian:

\[
\Pi_G(65)=(2,1)^2\cup(3,2)^2,
\]

with exact frontier

\[
\boxed{
\partial_P\mathfrak B_G^{(2)}(65)
=\{(4,0),(2,2),(0,4)\}.
}
\]

Eisenstein:

\[
\Pi_E(65)=(5,0)\cup(3,1)^2,
\]

with

\[
\boxed{
\partial_P\mathfrak B_E^{(2)}(65)
=\{(7,0),(5,2)\}.
}
\]

Changing the arithmetic world therefore changes not only a scalar value but the lattice shape of the typed Pareto response.

---

## 8. Prime-labelled world states

Let

\[
n=\prod_{p\mid n}p^{e_p}.
\]

For each original rational prime `p`, a quadratic UFD world `R` determines a prime-labelled state

\[
\boxed{
X_R(p;n)=(m_R(p),P_R(p),Q_R(p)),
}
\]

where `m_R(p)` is the number of irreducible factor nodes produced by `p^{e_p}` and `(P_R,Q_R)` is their canonical typed pair.

For inert primes, `m_R(p)=e_p` and the pair is `(p,0)`. For split primes, `m_R(p)=2e_p` and the pair is that of either conjugate prime factor. Ramified primes are treated analogously.

This aligns worlds by the original rational primes rather than by an arbitrary matching of irreducible factors.

---

## 9. Prime-toggle graph of arithmetic worlds

Represent an imaginary quadratic field by a negative squareclass

\[
[d]\in\mathbb Q^*/\mathbb Q^{*2}.
\]

For each rational prime `q`, define

\[
\boxed{T_q[d]=[qd].}
\]

Then

\[
T_q^2=I,
\qquad
T_pT_q=T_qT_p.
\]

Thus a finite set

\[
Q=\{q_1,\ldots,q_r\}
\]

generates an `r`-dimensional cube of worlds from a base squareclass.

The original square and triangular worlds are adjacent:

\[
\boxed{[-1]\xleftrightarrow{\ 3\ }[-3].}
\]

For an odd unramified rational prime `p`, quadratic characters obey

\[
\left(\frac{qd}{p}\right)
=\left(\frac qp\right)
\left(\frac dp\right).
\]

Hence a `q`-toggle changes split/inert behavior exactly at the unramified primes for which `(q/p)=-1`.

This world graph is classical squareclass/Cayley structure. Its role here is to provide canonical directions along which the arithmetic-network response may be differentiated.

---

## 10. Polynomial encoding of the Pareto response

Define

\[
\boxed{
Z_R(n;X,Y)
=\sum_{(b_P,b_Q)\in\partial_P\mathfrak B_R^{(2)}(n)}
X^{b_P}Y^{b_Q}.
}
\]

The scalar HATTER-SOL response is recovered by

\[
\boxed{
\Lambda_R(n)
=\min\{a+b:[X^aY^b]Z_R(n;X,Y)\ne0\}.
}
\]

Introduce total-boundary/imbalance coordinates

\[
\boxed{
\widetilde Z_R(n;u,v)
=Z_R(n;uv,u/v)
=\sum u^{b_P+b_Q}v^{b_P-b_Q}.
}
\]

The exponent of `u` records total free boundary; the exponent of `v` records typed imbalance.

### Example 10.1 — 37

\[
Z_G(37)=X^{12}+X^{10}Y^2,
\]

\[
Z_E(37)=X^8Y^4+X^6Y^6.
\]

The scalar minima coincide, while the polynomials do not.

---

## 11. Prime-toggle derivative and world Laplacian

For a prime-toggle edge define

\[
\boxed{
\nabla_qZ_n(R)
=Z_R(n)-Z_{T_qR}(n).
}
\]

For a finite prime set `Q` with positive weights `w_q`, define

\[
\boxed{
(\mathcal L_QZ_n)(R)
=\sum_{q\in Q}w_q\bigl(Z_R(n)-Z_{T_qR}(n)\bigr).
}
\]

Equivalently,

\[
\mathcal L_Q=\sum_{q\in Q}w_q(I-T_q).
\]

The operator acts coefficientwise on the polynomial-valued world signal.

### Theorem 11.1 — exact world-cube spectrum

For the cube generated by `Q`, the Walsh characters

\[
\psi_B(A)=(-1)^{|A\cap B|},
\qquad B\subseteq Q,
\]

are eigenfunctions with

\[
\boxed{
\lambda_B=2\sum_{q\in B}w_q.
}
\]

This spectrum is the standard weighted hypercube/Cayley spectrum; it is included to make the operator explicit, not as a novelty claim.

### Definition 11.2 — response Dirichlet energy

For a finite cube define

\[
\boxed{
\mathcal E_Q(n)
=\frac12\sum_R\sum_{q\in Q}w_q
\|Z_R(n)-Z_{T_qR}(n)\|_2^2,
}
\]

where the norm is the Euclidean norm of the finite coefficient vector. Then

\[
\mathcal E_Q(n)\ge0,
\]

with equality exactly when the Pareto response is constant on the connected cube.

---

## 12. Exact square/triangle derivatives

The square/triangle comparison is the single `q=3` world edge.

### 12.1 `n=7`

\[
Z_G(7)=X^7,
\qquad
Z_E(7)=X^4+X^2Y^2,
\]

so

\[
\boxed{
\nabla_3Z_7=X^7-X^4-X^2Y^2.
}
\]

### 12.2 `n=53`

\[
Z_G(53)=X^{14}Y^2+X^{12}Y^4,
\qquad
Z_E(53)=X^{53}.
\]

### 12.3 `n=37`

\[
\boxed{
\nabla_3Z_{37}
=X^{12}+X^{10}Y^2-X^8Y^4-X^6Y^6\ne0.
}
\]

Yet

\[
\Lambda_G(37)=\Lambda_E(37)=12.
\]

Hence the world derivative detects a change invisible to the scalar theory.

### 12.4 `n=15`

\[
Z_G(15)=X^3+XY^2,
\qquad
Z_E(15)=X^3,
\]

so

\[
\boxed{\nabla_3Z_{15}=XY^2.}
\]

Again the scalar responses coincide.

---

## 13. Conservative finite UFD laboratory

The element-factor model is unambiguous in imaginary quadratic rings of class number one. By the Baker-Heegner-Stark theorem, the nine imaginary quadratic class-number-one fields correspond to squarefree radicands

\[
\boxed{
-1,-2,-3,-7,-11,-19,-43,-67,-163.
}
\]

Restricting prime-toggle edges to this set produces an induced star centered at `[-1]`, with leaves obtained by toggles

\[
2,3,7,11,19,43,67,163.
\]

This gives a finite global laboratory for polynomial-valued world responses without invoking nonunique element factorization. Beyond class number one, the natural extension should be formulated using prime ideals rather than arbitrary irreducible elements.

---

## 14. Novelty boundary and prior-art audit

The following ingredients are classical and are not claimed as new:

1. Gaussian and Eisenstein integers, their norms, units, and rational-prime splitting laws;
2. quadratic characters and squareclasses;
3. degree-constrained graph factors and Lovasz `(g,f)`-factor theory;
4. packing/edge-disjoint realization of degree sequences and its known hard general case;
5. Cayley graphs, hypercubes, Walsh characters, and graph Laplacians;
6. class-number-one imaginary quadratic fields;
7. CM/isogeny graphs and other graph structures built from imaginary quadratic orders.

A literature audit located substantial prior work in all of these neighboring areas, including graph representations of quadratic-character data, CM/isogeny graphs, prime walks in imaginary quadratic UFDs, graph-factor theory, and hypercube Laplacian spectra. No source found in this audit constructs the specific chain

\[
\boxed{
\text{quadratic arithmetic world}
\to
\text{world-dependent irreducible factor profile}
\to
\text{typed HATTER-SOL factor network}
\to
\text{Pareto response polynomial}
\to
\text{prime-toggle world derivative/Laplacian}.
}
\]

Accordingly, the novelty claim is restricted to this composition and to the exact response theorems proved for it.

---

## 15. Limitations

1. The present factor-node construction is publication-safe only in UFD worlds when phrased in terms of irreducible elements. General quadratic fields require an ideal-theoretic version.
2. The two-interface model is tied to the canonical folded lattice description used here; alternative typed network laws may exist.
3. The world Laplacian itself is standard once the prime-toggle graph is fixed. The new content lies in the arithmetic-network signal on which it acts.
4. The paper establishes exact finite examples and structural theorems; it does not claim a universal classification of all integers by their world-response spectra.

---

## 16. Outlook

The immediate next mathematical problems are:

- replace element factorization by prime-ideal factorization in non-UFD quadratic worlds;
- determine which information about splitting vectors can be reconstructed from the world-response signal;
- study the spectral decomposition of `Z_n` on finite prime-toggle cubes;
- identify integers whose scalar world response is constant but whose typed spectral content is nontrivial;
- investigate whether conductor directions inside a fixed quadratic field and prime-toggle directions between fields combine into a two-level world geometry.

The central conceptual point is that a number is not assigned a single network. It generates a family of typed factor networks indexed by arithmetic world, and the variation of those networks can itself be treated as a signal on a canonical graph of worlds.

---

## References

[1] Malachevsky, A.A. *Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting.* HATTER-SOL-07, 2026. DOI: `10.5281/zenodo.22724185`.

[2] Lovasz, L. “Subgraphs with prescribed valencies.” *Journal of Combinatorial Theory* 8(4), 391–416 (1970). DOI: `10.1016/S0021-9800(70)80033-3`.

[3] Erdős, P.L., Ferrara, M.J., Hartke, S.G. “Navigating between packings of graphic sequences.” *Discrete Applied Mathematics* 266, 252–258 (2019). DOI: `10.1016/j.dam.2018.06.034`.

[4] Bérczi, K., Király, T., Liu, C.-C., Miklós, I. “Packing Tree Degree Sequences.” *Graphs and Combinatorics* 36, 779–801 (2020). DOI: `10.1007/s00373-020-02153-0`.

[5] Stark, H.M. “On the ‘gap’ in a theorem of Heegner.” *Journal of Number Theory* 1(1), 16–27 (1969). DOI: `10.1016/0022-314X(69)90023-7`.

[6] Cox, D.A. *Primes of the Form x^2 + ny^2: Fermat, Class Field Theory, and Complex Multiplication.* Wiley, 1989.

[7] Ireland, K., Rosen, M. *A Classical Introduction to Modern Number Theory.* 2nd ed., Springer, 1990.

[8] Chung, F.R.K. *Spectral Graph Theory.* CBMS Regional Conference Series in Mathematics 92, AMS, 1997.

[9] Prasad, S. “Walks on Primes in Imaginary Quadratic Fields.” arXiv:1412.2310 (2014).

[10] Arpin, S., Chen, M., Lauter, K., Scheidler, R., Stange, K.E., Tran, H.T.N. “Orienting supersingular isogeny graphs.” *Journal of Mathematical Cryptology* 14 (2020). DOI: `10.1515/jmc-2019-0034`.
