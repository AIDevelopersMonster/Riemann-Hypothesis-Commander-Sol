# Finite-to-Infinite Map

**Direction:** FCOA — SOL-INFINITY — Infinite Carrier & FO Memory Boundary

## Transfer table

### M0 generic exchangeability

Finite:

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1}.
\]

Canonical infinite analogue:

\[
\operatorname{Aut}(\mathfrak M_\omega^\times)\cong \operatorname{Sym}(G_\omega)
\]

before any successor geometry is compiled, provided the E-output families are carried along equivariantly.

**Transfers:** yes, at the structural level.

---

### G1 external directed ray

Finite directed path:

\[
P_2\to\cdots\to P_N
\]

is rigid.

Infinite directed ray:

\[
P_2\to P_3\to\cdots
\]

is also rigid because the unique root is fixed and every later point is its unique finite successor iterate.

**Transfers:** rigidity yes.

**Does not transfer into:** FO full-order memory. Rigidity alone is insufficient.

---

### G2 domain compilation

Finite:

\[
S(x,y)\iff \operatorname{Def}(x\otimes_1 y)
\]

uniformly defines directed adjacency.

Infinite:

exactly the same local formula defines successor adjacency.

**Transfers:** local directed memory yes, uniformly.

**Does not transfer:** full transitive order is not FO-definable in the infinite structure.

---

### Per-finite full order

For fixed \(N\),

\[
x<_Ny\iff \bigvee_{1\le k\le N-2}S^k(x,y).
\]

**Transfers:** only as a different formula for each finite \(N\).

**Does not transfer:** no single uniform FO formula works for all \(N\), and no infinite FO formula defines reachability on the ray.

---

### G3 local value-fiber memory

Finite G3 shows value geometry can remove residual automorphisms left by definedness.

The corresponding infinite local enrichments can likewise distinguish local edge orientation or boundary roles.

**Transfers:** value/domain separation as a mechanism.

**Does not transfer:** local finite-valued edge enrichment does not automatically give global FO order. Any enrichment first-order definable from bounded successor patterns remains below the FO reachability boundary.

---

### G4 complete comparison-value geometry

Finite G4-C has complete off-diagonal generic domain and two anonymous orientation outputs. Finite reversal survives by swapping the outputs.

Infinite \(\omega\)-ray analogue:

\[
x\chi y=\Omega_+\iff x<y,
\qquad
x\chi y=\Omega_-\iff y<x.
\]

Here reversal does not exist: the carrier has a least point but no greatest point. The positive output becomes internally FO-definable from the unique point whose every off-diagonal outgoing comparison has that value.

**Transfer:** the two-fiber comparison mechanism survives.

**Finite-to-infinite change:** anonymous output symmetry collapses in the infinite ray, and full order becomes FO-definable.

---

## Main non-transfer theorem

The implication

\[
\text{finite rigidity + uniform successor recovery}
\Longrightarrow
\text{infinite FO full-order recovery}
\]

is false.

The exact obstruction is not automorphism-theoretic. It is logical: first-order formulas over successor have bounded syntactic depth and cannot express unbounded transitive reachability.

## Current status

- finite M0-G2: inherited fixed publication checkpoint;
- finite G3: inherited hostile-audited result;
- finite G4: inherited theorem candidate only;
- infinite FO-1/FO-2 boundary: working theorem checkpoint in this branch;
- infinite complete-comparison result: working theorem checkpoint in this branch, not a promotion of finite G4.
