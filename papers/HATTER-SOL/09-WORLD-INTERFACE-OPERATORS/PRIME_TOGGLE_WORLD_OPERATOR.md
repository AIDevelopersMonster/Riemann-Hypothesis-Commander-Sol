# HATTER-SOL-09 — Prime-toggle world graph and response operator

Status: closed structural layer; publication candidate component.

## 1. World graph

Represent an imaginary quadratic field by a negative squareclass

\[
[d]\in\mathbb Q^*/\mathbb Q^{*2},\qquad d<0.
\]

For every rational prime `q`, define

\[
T_q[d]=[qd].
\]

Then

\[
T_q^2=1,\qquad T_pT_q=T_qT_p.
\]

Thus negative squareclasses form an infinite prime-labelled hypercube torsor. In particular

\[
[-1]\xleftrightarrow{\ 3\ }[-3],
\]

so the Gaussian and Eisenstein worlds are adjacent by a single `3`-toggle.

For an odd rational prime `p` away from ramification, splitting obeys

\[
\left(\frac{qd}{p}\right)
=\left(\frac q p\right)\left(\frac d p\right).
\]

Hence a `q`-toggle flips split/inert type at exactly the unramified primes `p` with `(q/p)=-1`.

## 2. Finite world cubes

Fix a base world `d_0` and a finite prime set

\[
Q=\{q_1,\ldots,q_r\}.
\]

The generated world cube is

\[
\mathcal C_Q(d_0)
=\left\{\left[d_0\prod_{q\in A}q\right]:A\subseteq Q\right\}.
\]

For positive weights `w_q`, define on any vector-valued world signal `F`

\[
\boxed{
(\mathcal L_QF)(A)
=\sum_{q\in Q}w_q\bigl(F(A)-F(A\triangle\{q\})\bigr).
}
\]

Equivalently

\[
\mathcal L_Q=\sum_{q\in Q}w_q(I-T_q).
\]

### Theorem 2.1 — exact cube spectrum

For each `B subset Q`, the Walsh character

\[
\psi_B(A)=(-1)^{|A\cap B|}
\]

is an eigenfunction with eigenvalue

\[
\boxed{\lambda_B=2\sum_{q\in B}w_q.}
\]

Proof: `T_q psi_B=(-1)^{1_{q in B}} psi_B`; substitute into the operator. QED.

Thus the world Laplacian is forced by the commuting prime involutions; its spectrum is not introduced ad hoc.

## 3. Conservative UFD domain for element factorization

The current HATTER-SOL factor nodes use irreducible elements. To retain unique factorization, a finite global experiment may be restricted to the nine imaginary quadratic class-number-one fields

\[
\mathcal H=\{-1,-2,-3,-7,-11,-19,-43,-67,-163\}.
\]

Their rings of integers are PIDs/UFDs. The induced prime-toggle graph is the star `K_{1,8}` centered at `[-1]`; every other vertex is `[-q]` for one of

\[
q=2,3,7,11,19,43,67,163.
\]

The unweighted graph-Laplacian spectrum of this star is

\[
\boxed{0,\quad 1\text{ (multiplicity 7)},\quad 9.}
\]

This spectrum is classical graph theory. The HATTER-SOL signal placed on the graph is the new research layer. Extension beyond class number one should use ideals rather than nonunique element factorizations.

## 4. Pareto response polynomial

For a UFD world `R` and positive integer `n`, define

\[
\boxed{
Z_R(n;X,Y)
=\sum_{(b_P,b_Q)\in\partial_P\mathfrak B_R^{(2)}(n)}X^{b_P}Y^{b_Q}.
}
\]

The old scalar HATTER-SOL boundary is recovered by

\[
\boxed{
\Lambda_R(n)
=\min\{a+b:[X^aY^b]Z_R(n;X,Y)\ne0\}.
}
\]

Thus `Z` refines `Lambda`.

The sum/imbalance coordinates are exposed by

\[
\widetilde Z_R(n;u,v):=Z_R(n;uv,u/v)
=\sum u^{b_P+b_Q}v^{b_P-b_Q}.
\]

The `u` exponent is total free boundary and the `v` exponent is typed anisotropy.

## 5. Edge derivative and world Laplacian on the response

For a prime-toggle edge define

\[
\boxed{
\nabla_qZ_n(R)=Z_R(n)-Z_{T_qR}(n).
}
\]

Whenever the relevant worlds belong to the chosen UFD domain, `Z_n` is a polynomial-valued signal and `L_Q Z_n` is defined coefficientwise.

For finite-support coefficient vectors, the Dirichlet energy is

\[
\boxed{
\mathcal E_Q(n)
=\frac12\sum_A\sum_{q\in Q}w_q
\|Z_A(n)-Z_{A\triangle\{q\}}(n)\|_2^2.
}
\]

It is nonnegative and vanishes exactly when the response is constant on the connected world cube.

## 6. Exact square/triangle tests on the 3-edge

Write `G` for Gaussian and `E` for Eisenstein.

### n=7

\[
Z_G(7)=X^7,
\qquad
Z_E(7)=X^4+X^2Y^2.
\]

Hence

\[
\nabla_3Z_7=X^7-X^4-X^2Y^2.
\]

### n=53

\[
Z_G(53)=X^{14}Y^2+X^{12}Y^4,
\qquad
Z_E(53)=X^{53}.
\]

### n=37 — scalar collision

\[
Z_G(37)=X^{12}+X^{10}Y^2,
\]

\[
Z_E(37)=X^8Y^4+X^6Y^6.
\]

Both scalar boundaries equal `12`, but

\[
\boxed{\nabla_3Z_{37}\ne0.}
\]

In sum/imbalance coordinates,

\[
\widetilde Z_G(37)=u^{12}(v^{12}+v^8),
\]

\[
\widetilde Z_E(37)=u^{12}(v^4+1).
\]

Thus the scalar response is blind while the typed world derivative detects the change.

### n=15 — heterogeneous scalar collision

\[
Z_G(15)=X^3+XY^2,
\qquad
Z_E(15)=X^3.
\]

Again `Lambda_G(15)=Lambda_E(15)=3`, while

\[
\boxed{\nabla_3Z_{15}=XY^2\ne0.}
\]

## 7. Interpretation

The resulting chain is

\[
\boxed{
\text{quadratic world}
\to
\text{world-dependent factorization}
\to
\text{typed factor network}
\to
Z_R(n;X,Y)
\to
\mathcal L_QZ_n.
}
\]

No novelty is claimed for squareclasses, quadratic characters, hypercube/Cayley graphs, graph Laplacians, or the class-number-one list separately. The candidate contribution is their composition with the HATTER-SOL typed free-boundary response.
