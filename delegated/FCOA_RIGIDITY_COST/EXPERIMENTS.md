# FCOA Rigidity Cost — Exact Finite Experiments

**Branch:** `director/fcoa-rigidity-cost`  
**Purpose:** exact small-carrier checks only; computation is evidence/support for proofs, not a substitute for general proof.

## E1. Search conventions

Write \(n=N-1\) for the generic carrier size.

The exhaustive search uses:

- directed skeletons: loopless relations \(A\subseteq X^2\setminus\Delta\);
- undirected skeletons: simple graphs \(E\subseteq\binom X2\);
- automorphisms: all carrier permutations preserving the relation;
- cost: number of directed arcs or undirected edges;
- no external vertex colors, names, anchors, arithmetic, or distinguished constants.

The search prunes candidate automorphisms by in/out-degree classes (directed) or degree classes (undirected), but still checks exact relation preservation.

Reproducibility script: `verify_rigidity_cost.py` in this directory.

---

## E2. Exact full-rigidity minima

### Directed

| generic \(n\) | FCOA \(N\) | minimum arcs | first witness found |
|---:|---:|---:|---|
| 2 | 3 | 1 | \(0\to1\) |
| 3 | 4 | 1 | \(0\to1\), vertex 2 isolated |
| 4 | 5 | 2 | \(0\to1\to2\), vertex 3 isolated |
| 5 | 6 | 3 | 3-arc rigid oriented tree + isolate |
| 6 | 7 | 3 | \(0\to1\to2\), \(3\to4\), vertex 5 isolated |
| 7 | 8 | 4 | 3-arc rigid oriented tree + directed edge + isolate |

### Undirected

| generic \(n\) | FCOA \(N\) | minimum edges |
|---:|---:|---:|
| 2 | 3 | none |
| 3 | 4 | none |
| 4 | 5 | none |
| 5 | 6 | none |
| 6 | 7 | 6 |
| 7 | 8 | 6 |

A six-vertex minimum witness returned by enumeration is

\[
\{01,02,03,12,14,35\}.
\]

The seven-vertex minimum witness is the same graph plus one isolated vertex.

---

## E3. Exact small C2 minima

Because a group of order two is necessarily cyclic, searching for automorphism-group size two gives the exact \(C_2\) cost.

| \(n\) | directed arcs | undirected edges |
|---:|---:|---:|
| 2 | 0 | 0 |
| 3 | 2 | 1 |
| 4 | 1 | 2 |
| 5 | 2 | 3 |
| 6 | 3 | 4 |
| 7 | 3 | 5 |

No asymptotic extrapolation is made from this table.

---

## E4. Terminal Generic Layer Master Formula

For every directed generic domain \(A\subseteq G_N^2\setminus\Delta\), compile every cell with terminal outputs and compare the measured Association Spectrum against

\[
\begin{aligned}
EQ &= 4(N-1)+|A|,\\
NEQ &= 0,\\
LEFT &= N^2+2N-2+|A|,\\
RIGHT &= N^2+N-2+|A|,\\
NONE &= N^3+N^2-4N+9-3|A|.
\end{aligned}
\]

The script exhausts **every** directed skeleton for \(N=3,4,5\):

- \(N=3\): \(2^2=4\) domains;
- \(N=4\): \(2^6=64\) domains;
- \(N=5\): \(2^{12}=4096\) domains.

Terminal colors are deliberately varied during the test. All cases pass.

This is only a finite regression check; the proof in `RESULTS.md` is cell-local and holds for all \(N\).

---

## E5. Complete-domain two-anonymous-output search

For a complete generic domain let one fiber be \(A\) and the other its complement \(A^c\). Since output names are anonymous, the carrier group is

\[
\Gamma(A)=\{g\in S_n:gA=A\text{ or }gA=A^c\}.
\]

### Balanced fibers

Exhaustive search among balanced partitions gives:

| \(n\) | balanced rigid two-fiber partition? |
|---:|---|
| 2 | no |
| 3 | no |
| 4 | yes |

A four-vertex witness is

\[
A_4=\{01,02,03,10,12,21\}.
\]

It has six cells in each anonymous fiber and \(\Gamma(A_4)=1\).

### Tournament subclass

If exactly one orientation of each unordered pair lies in \(A\), then \(A\) is a tournament and \(A^c=A^{\rm op}\). Exhaustive tournament search gives:

| \(n\) | asymmetric non-self-converse tournament? |
|---:|---|
| 2 | no |
| 3 | no |
| 4 | no |
| 5 | yes |

A five-vertex witness is

\[
T_5=\{40,41,42,43,20,21,31,32,03,10\}.
\]

The script verifies

\[
\operatorname{Aut}(T_5)=1
\]

and that no carrier permutation maps \(T_5\) to its converse.

Because tournament fibers assign opposite values to reverse ordered pairs, this witness has no new generic commuting pair. It is the finite control for the `same spectrum + same commutation + different automorphism group` comparison with G4-C.

---

## E6. FCOA N=3,4,5 compiled rigidity controls

Using rigidity-minimal directed domains and one terminal value:

| \(N\) | new generic cells | \(\operatorname{Aut}\) | commutation | Association Spectrum |
|---:|---:|---|---:|---|
| 3 | 1 | 1 | 6 | \((9,0,14,11,30)\) |
| 4 | 1 | 1 | 9 | \((13,0,23,19,70)\) |
| 5 | 2 | 1 | 12 | \((18,0,35,30,133)\) |

For comparison, G2 uses \(N-2\) directed-path cells, i.e. 1, 2, 3 cells respectively.

The finite controls expose the first Rigidity–Memory gaps at \(N=4\) and \(N=5\).

---

## E7. Reproduction command

From the repository root:

```bash
python delegated/FCOA_RIGIDITY_COST/verify_rigidity_cost.py
```

Expected terminal summary ends with:

```text
TERMINAL LAYER MASTER FORMULA
verified exhaustively for every directed generic domain through N=5

ALL CHECKS PASSED
```

Exact witness labels may differ if search order is changed; costs and group tests are invariant.