# EXP-META-01 — Equivariant Off-Diagonal No-Go

Status: theorem-level research note.
Parent work package: WP-O2 (non-diagonal symmetry breakers).

## 1. Setup

Let

`H = l^2(N_{>0})`

with canonical basis `e_n`, and let the multiplicative shifts be

`L_p e_n = e_{pn}`

for primes `p`.

For a permutation `sigma` of the primes, let `hat(sigma)` be the induced automorphism of the free commutative monoid `N_{>0}` and define

`U_sigma e_n = e_{hat(sigma)(n)}`.

Then

`U_sigma L_p U_sigma^* = L_{sigma(p)}`.

This is the spatial prime-permutation symmetry already isolated in the Prime-Successor Operator note.

## 2. Valuation-local off-diagonal candidate

Consider the natural class

`D_f e_n = sum_{r in P} f(v_r(n)) e_{rn}`.

### Domain obstruction

If `f(0) != 0`, then for every fixed `n`, all but finitely many primes satisfy `v_r(n)=0`, hence

`||D_f e_n||^2 >= sum_{r not dividing n} |f(0)|^2 = infinity`.

Therefore the canonical basis does not lie in the domain. For the finite-support version of this ansatz one must at least require

`f(0)=0`.

With `f(0)=0`, the sum is finite on each basis vector.

## 3. Theorem: valuation-local covariance

### Theorem 1

For every prime permutation `sigma`,

`U_sigma D_f U_sigma^* = D_f`.

### Proof

The exponents transform by

`v_{sigma(r)}(hat(sigma)(n)) = v_r(n)`.

Therefore conjugation merely permutes the summation index while leaving the common rule `f` unchanged. Hence the operator is fixed by every prime permutation. QED.

### Corollary 1

`Stab_P(D_f) = Sym(P)`.

Thus no operator in this valuation-local uniform class satisfies the necessary symmetry-breaking condition of the Prime-Successor Operator Problem.

## 4. Explicit commutator

Let

`C_p = [D_f, L_p]`.

For `r != p`, multiplication by `p` does not change `v_r(n)`. Only the `r=p` term survives, giving

`[D_f,L_p] e_n = ( f(v_p(n)+1) - f(v_p(n)) ) e_{p^2 n}`.

This formula shows that the commutator localizes the `p`-adic coordinate but does not introduce any relation among distinct prime coordinates.

Moreover,

`U_sigma C_p U_sigma^* = C_{sigma(p)}`.

## 5. Theorem: commutator successor no-go

### Theorem 2

Let `Phi(C_p,C_q)` be any binary truth-valued rule invariant under simultaneous unitary conjugation of the operator structure. If `D` is prime-permutation invariant and the commutator family is defined by `C_p=[D,L_p]`, then `Phi` cannot equal the standard prime-successor relation.

### Proof

For every prime permutation `sigma`, covariance gives

`Phi(C_p,C_q) <=> Phi(C_{sigma(p)},C_{sigma(q)})`.

The full symmetric group on the primes is transitive on ordered pairs of distinct primes. Hence any such invariant can distinguish at most orbit types such as `p=q` versus `p!=q`; it cannot distinguish the successor pair `(p,p_next)` from an arbitrary distinct pair. QED.

### Interpretation

Local commutators do not help unless the distinguished datum already breaks prime permutation symmetry.

## 6. Graph-canonical version

Consider the unlabeled multiplicative graph with vertices `N_{>0}` and edges

`n ~ np`

for every prime `p`.

Every prime permutation induces a graph automorphism. Consequently any operator constructed canonically/functorially from this unlabeled graph and invariant under graph isomorphism inherits the same prime-permutation symmetry.

Examples include, when mathematically well-defined under a chosen weighting/closure:

- adjacency-type operators;
- graph Laplacians;
- heat kernels;
- resolvents;
- spectral projections and functional calculus derived from such canonical graph operators.

Therefore the unlabeled multiplicative graph alone cannot canonically orient the primes.

## 7. Infinite-degree warning

The naive adjacency operator

`A e_n = sum_p e_{np}`

is not an `l^2` vector on basis states because every vertex has infinite degree:

`||A e_n||^2 = sum_p 1 = infinity`.

A weighted version

`A_c e_n = sum_p c_p e_{np}`

requires at least square-summable weights `(c_p)` for this simple basis-domain test. But then:

- equal nonzero weights are not square-summable over infinitely many primes;
- unequal weights individualize prime coordinates;
- if the weights are chosen from ordinary magnitude, magnitude has been imported;
- if chosen arbitrarily, the construction supplies arbitrary labels rather than intrinsic orientation.

This is a useful symmetry-breaking audit for future candidates.

## 8. Magnitude-blindness must be stronger than `D != g(log N)`

A non-diagonal operator may fail to be a function of the diagonal magnitude operator while still encoding the entire ordinary order or even `nextPrime` in its matrix elements.

Therefore the weak test

`D is not a function of log N`

is insufficient.

A stronger target is structural/model-theoretic:

- standard prime successor should be recoverable from `(A,H,D)`;
- ordinary order on all naturals should not be trivially recoverable;
- ideally full addition should not be definable/recoverable by the same mechanism.

This is the operator analogue of the arithmetic corridor isolated by the Dilation-Collapse theorem.

## 9. Consequence for WP-O2

The initial off-diagonal candidate class is closed.

The remaining search cannot be restricted to operators that are canonical functions of the unlabeled multiplicative graph or uniform valuation-local rules. Such constructions preserve the exact symmetry that obstructs prime successor.

The next problem is therefore not merely to find a non-diagonal `D`, but to identify the weakest natural additional datum `Omega` satisfying

`Stab_P(Omega) = {id}`

without importing ordinary magnitude or hidden prime order.

That problem is formulated as EXP-META-02.
