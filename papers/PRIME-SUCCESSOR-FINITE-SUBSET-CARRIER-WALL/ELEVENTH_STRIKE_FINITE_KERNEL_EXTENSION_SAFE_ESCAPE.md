# Eleventh Strike — Finite Kernel Extension and Safe-Escape Repair

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Author:** Alex Malachevsky  
**Date:** 2026-08-31  
**Status:** proved reductions and exact local repair; global binary kernel remains open

## 1. Aim

The tenth strike refuted odd-cycle exclusion by the exact directed 5-cycle

\[
123527\to83\to71\to1013\to3851\to123527
\]

inside the corridor

\[
H=\Gamma_\Delta[C\setminus\{2\}],
\qquad
C=\{p:p\equiv2\pmod3\}.
\]

The direct question is now whether `H` has a kernel.

This strike replaces the global problem by an exact finite-extension criterion and proves that the first odd cycle is repairable by a single arithmetic escape vertex.

---

## 2. Kernel CNF

Let `D=(V,A)` be an outwardly finite digraph. For every vertex `v` introduce a Boolean variable `X_v`, intended to mean `v` belongs to a kernel.

The kernel conditions are equivalent to the propositional system

\[
\neg X_u\vee\neg X_v
\qquad (u\to v),
\tag{1}
\]

and

\[
X_u\vee\bigvee_{u\to v}X_v
\qquad(u\in V).
\tag{2}
\]

The disjunction in (2) is finite because `D` is outwardly finite.

---

## 3. Finite Kernel Extension Criterion

### Theorem 3.1

For an outwardly finite digraph `D`, the following are equivalent.

1. `D` has a kernel.
2. For every finite `X subset V(D)` there exists a finite `Y`, `X subset Y subset V(D)`, such that the induced digraph `D[Y]` has a kernel.
3. For every finite `X subset V(D)` there exists a finite independent set `K_X` such that every vertex of `X\K_X` has an arc to `K_X`.
4. In (3), `K_X` may be required to lie in the finite set
   \[
   X\cup N^+(X).
   \tag{3}
   \]

### Proof

`(1) => (2)`. Let `K` be a kernel of `D` and `X` finite. For each `x in X\K`, choose one `k_x in K` with `x -> k_x`. Put

\[
Y=X\cup\{k_x:x\in X\setminus K\}.
\]

Then `K cap Y` is independent and absorbs every vertex of `Y\(K cap Y)`, so it is a kernel of `D[Y]`.

`(2) => (3)`. If `L` is a kernel of `D[Y]`, take `K_X=L`. It is independent in `D` and absorbs `X`.

`(3) => (4)`. Delete from `K_X` every vertex outside `X union N^+(X)`. Such a vertex neither belongs to `X` nor can absorb a vertex of `X`, so the required absorption of `X` is unchanged. Independence is preserved.

`(4) => (1)`. Consider the propositional kernel system (1)-(2). Take any finite subset `Sigma` of its clauses and let `X` contain all vertices whose variables occur in `Sigma` and all vertices whose absorption clauses occur in `Sigma`. By (4), choose a finite independent `K_X` absorbing `X`. Assign `X_v=true` for `v in K_X` and false otherwise. Every independence clause in `Sigma` is satisfied because `K_X` is independent, and every absorption clause in `Sigma` is satisfied because its source lies in `X` and is either selected or points to a selected vertex. Thus every finite subset of the kernel CNF is satisfiable. Propositional compactness gives a global satisfying assignment, whose true set is a kernel of `D`. ∎

### Consequence 3.2

For the arithmetic corridor `H`, global kernel existence is equivalent to a purely finite family of problems:

> every finite set of source primes must admit a finite independent absorber chosen from those sources and their actual residual prime divisors.

This is the exact local-global form of the remaining binary singleton problem.

---

## 4. Safe-Escape Repair Lemma

### Lemma 4.1

Let `D` be a finite induced subdigraph, let `v in V(D)`, and suppose `D-v` has a kernel `K`. Let `y notin V(D)` satisfy

\[
v\to y,
\tag{4}
\]

and suppose `y` is nonadjacent in both directions to every vertex of `K`:

\[
\forall k\in K:
\quad
k\not\to y
\quad\text{and}\quad
y\not\to k.
\tag{5}
\]

Then

\[
\boxed{K\cup\{y\}}
\]

is a kernel of the induced digraph `D[V(D) union {y}]`.

### Proof

By (5), `K union {y}` is independent. Every vertex of `D-v` outside `K` already points to `K`, because `K` is a kernel of `D-v`. The removed vertex `v` points to `y` by (4). The new vertex `y` is itself selected. Hence every unselected vertex in `D union {y}` points to `K union {y}`. ∎

### Remark 4.2

For a critical kernel-imperfect finite core, the lemma reduces a one-vertex repair to the search for one safe external residual divisor.

---

## 5. Exact repair of the first directed odd cycle

Let

\[
D_5=
\{123527,83,71,1013,3851\}
\]

with the exact directed 5-cycle

\[
123527\to83\to71\to1013\to3851\to123527.
\tag{6}
\]

This induced 5-cycle has no kernel.

Remove

\[
v=1013.
\]

The remaining directed path is

\[
3851\to123527\to83\to71,
\]

whose kernel is

\[
K_0=\{123527,71\}.
\tag{7}
\]

Now use the external corridor prime

\[
y=15881.
\]

The factorization of `N_1013` contains `15881`, so

\[
1013\to15881.
\tag{8}
\]

An independent exact computation gives

\[
\tau(15881)=100530331232711075846682.
\tag{9}
\]

The four nonadjacency certificates required by Lemma 4.1 are

\[
N_{123527}\equiv9036\pmod{15881},
\tag{10}
\]

\[
N_{71}\equiv15715\pmod{15881},
\tag{11}
\]

\[
N_{15881}\equiv22040\pmod{123527},
\tag{12}
\]

and

\[
N_{15881}\equiv15\pmod{71}.
\tag{13}
\]

All four residues are nonzero. Therefore `15881` is nonadjacent in both directions to `123527` and `71`.

### Theorem 5.1 — One-vertex repair of the 5-cycle

The induced digraph on

\[
\{123527,83,71,1013,3851,15881\}
\]

has the kernel

\[
\boxed{\{123527,71,15881\}}.
\tag{14}
\]

### Proof

Apply Lemma 4.1 to `v=1013`, `K=K_0`, and `y=15881`. ∎

### Consequence 5.2

The first genuine odd cycle is not even a one-step obstruction to the finite-extension criterion. It is killed by one actual Ramanujan residual divisor.

---

## 6. General odd-cycle repair template

Let

\[
v_0\to v_1\to\cdots\to v_{2m}\to v_0
\tag{15}
\]

be a chordless directed odd cycle. Remove `v_0`. The remaining directed path has kernel

\[
K_{\rm alt}=\{v_2,v_4,\dots,v_{2m}\}.
\tag{16}
\]

Therefore any external successor `y` of `v_0` satisfying

\[
y\not\leftrightarrow K_{\rm alt}
\tag{17}
\]

repairs the cycle in one step:

\[
K_{\rm alt}\cup\{y\}
\]

is a kernel after adjoining `y`.

Thus the arithmetic problem for an odd cycle is not “does it exist?” but rather:

> does at least one cycle vertex have a residual prime divisor that is safe against one of the alternating kernels of the broken cycle?

The 5-cycle answers yes.

---

## 7. Exact finite-horizon experiment

A finite induced-corridor test was carried out with exact integer arithmetic on

\[
X_{20000}
=
\{p\le20000:p\equiv2\pmod3\}
\cup\{123527\}.
\tag{18}
\]

The set has

\[
1137
\]

vertices and the induced residual digraph has

\[
1155
\]

directed edges.

The kernel feasibility problem was solved exactly as a binary linear system corresponding to (1)-(2). The induced graph has a kernel of size

\[
680.
\tag{19}
\]

One returned kernel contains

\[
11,\ 71,\ 443,\ 971,\ 15881,\ 123527
\]

among its selected vertices and selects `123527` and `71` from the 5-cycle.

This is computational evidence only; it is not used in any theorem above and does not prove the infinite corridor has a kernel.

---

## 8. What a genuine counterexample must now do

By Theorem 3.1, failure of the binary corridor kernel cannot be established merely by exhibiting an odd cycle. One must find a finite set `X` for which **no finite independent absorber exists in the full arithmetic digraph**.

Equivalently, one must defeat every possible finite repair by actual residual divisors.

The 5-cycle fails this test immediately because of `15881`.

This suggests the correct obstruction notion:

\[
\boxed{\textbf{repair-resistant finite absorber obstruction}.}
\tag{20}
\]

Such an obstruction is stronger than a kernel-imperfect induced subgraph.

---

## 9. Next arithmetic target

The exact remaining problem is now:

\[
\boxed{
\forall X\subset H\text{ finite},\
\exists K_X\subset X\cup N^+(X)\text{ independent and absorbing }X\ ?
}
\tag{21}
\]

Two attack directions are now concrete.

1. **Positive route — Safe divisor theorem.** Prove that every finite critical obstruction admits a safe residual divisor satisfying a repair condition such as Lemma 4.1, then organize repairs into a finite-extension argument.
2. **Negative route — finite absorber SAT core.** Search directly for a finite `X` whose closed out-neighborhood hypergraph has no independent transversal. Such an `X` would be a finite certificate that the corridor has no kernel.

The old parity route is no longer relevant.

---

## 10. Literature connection

The finite-extension formulation is compatible with the standard compactness approach to kernels in outwardly finite digraphs. Duchet and Meyniel formulate the kernel conditions propositionally and use compactness in their work on kernels and the poison game; later surveys state the corresponding finite-extension criteria for outwardly finite digraphs.

This checkpoint does not claim priority for the abstract graph-theoretic compactness principle. Its contribution to this branch is the exact translation to the Ramanujan corridor and the arithmetic safe-escape repair of the first odd cycle.

---

## 11. Hostile audit

1. **Does Theorem 3.1 accidentally use finite in-degree?** No. Only finite out-degree is needed so that each absorption clause is finite.
2. **Can the finite absorber contain irrelevant external vertices?** They can be deleted, giving (3).
3. **Does a kernel of `D[Y]` remain independent in the full graph?** Independence among its selected vertices depends only on arcs between those vertices, all already present in the induced graph.
4. **Does the safe-escape lemma require controlling arcs between `y` and unselected vertices?** No. Kernel independence only concerns selected vertices; unselected old vertices are already absorbed by `K`.
5. **Is `15881` really an outgoing residual divisor of `1013`?** Yes; `15881` divides `N_1013` exactly.
6. **Are all four nonadjacency directions checked?** Yes, by (10)-(13).
7. **Does the repaired 6-vertex graph prove a global kernel?** No.
8. **Does the 20,000-horizon computation prove the infinite statement?** No; it is explicitly evidence only.
9. **What would disprove the corridor kernel now?** A finite source set with no independent absorber from its closed arithmetic out-neighborhood.

**Audit verdict:** PASS for the local-global reduction and exact one-vertex repair. Global binary kernel existence remains open.
