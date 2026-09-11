# HATTER-SOL-05 · Finite-Fiber Compactness and Killing Certificates

## 0. Status

Canonical v1.0 source after hostile proof audit.

For the radical-predecessor graph

\[
\Pi=(\mathbb P,D),\qquad D(q,p)\iff q\mid p-1,
\]

write

\[
X_S=\{p:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

This note proves a compactness principle: if every exact predecessor fiber is finite, then failure of a seed symmetry is witnessed at finite Pratt height. The resulting certificate is **structural**, not an algorithmic decidability statement.

---

# 1. Height truncations

Let

\[
P_{\le n}=\{p:h(p)\le n\},
\qquad
G_n=\operatorname{Aut}(\Pi\upharpoonright P_{\le n}).
\]

For \(m\le n\), let

\[
\rho_{m,n}:G_n\to G_m
\]

be restriction. Fix a seed \(\tau\in G_m\) and define

\[
T_n(\tau)=\{g\in G_n:\rho_{m,n}(g)=\tau\}.
\]

For HATTER-SOL-05 the principal seed is the transposition

\[
\tau=(3\ 5)\in G_1.
\]

---

# 2. Finite-fiber condition

## Definition 2.1 — FFC

The graph satisfies the finite-fiber condition if

\[
\boxed{\mu(S)<\infty}
\]

for every finite exact predecessor support \(S\ni2\).

FFC is a structural hypothesis, not an asserted theorem about the actual prime graph.

## Lemma 2.2

Under FFC, every Pratt truncation \(P_{\le n}\) is finite.

### Proof

Induct on \(n\). The base is \(P_{\le0}=\{2\}\). If \(P_{\le n}\) is finite, only finitely many exact supports \(S\subseteq P_{\le n}\) can occur at height \(n+1\). FFC makes each corresponding fiber \(X_S\) finite. Hence the union of all new fibers is finite. \(\square\)

Consequently, every group \(G_n\) and every extension set \(T_n(\tau)\) is finite.

---

# 3. Extension tree

Construct a tree \(\mathcal T(\tau)\) whose depth-\((n-m)\) vertices are the elements of \(T_n(\tau)\), with

\[
g_{n+1}\to g_n
\]

whenever \(g_{n+1}\) restricts to \(g_n\).

A global extension of \(\tau\) gives an infinite branch. Conversely, an infinite compatible branch gives a global automorphism by the inverse-limit theorem of HATTER-SOL-04.

Under FFC the tree is finitely branching.

---

# 4. Finite-fiber compactness

## Theorem 4.1

Assume FFC. For every seed \(\tau\in G_m\), the following are equivalent:

1. \(\tau\) extends to a global automorphism of \(\Pi\);
2. \(\tau\) extends to every finite Pratt height;
3. \(T_n(\tau)\ne\varnothing\) for every \(n\ge m\).

Equivalently,

\[
\boxed{
\tau\text{ fails globally}
\Longrightarrow
\tau\text{ dies at a finite height}.
}
\]

### Proof

The implications \((1)\Rightarrow(2)\Rightarrow(3)\) are immediate. If every \(T_n(\tau)\) is nonempty, the extension tree has a node at every depth and is finitely branching. König's infinity lemma yields an infinite compatible branch. The inverse-limit identification then gives a global automorphism extending \(\tau\). \(\square\)

---

# 5. Finite killing certificates

Suppose FFC holds and \(\tau\) has no global extension. Let \(N>m\) be the least height such that

\[
T_N(\tau)=\varnothing.
\]

Then \(T_{N-1}(\tau)\) is finite and nonempty. For each surviving candidate

\[
g\in T_{N-1}(\tau),
\]

the multiplicity-tower extension theorem supplies at least one next-layer support \(S_g\) with

\[
\boxed{\mu(S_g)\ne\mu(gS_g).}
\]

## Theorem 5.1 — finite obstruction family

Under FFC, if \(\tau\) has no global extension, then there exist a finite height \(N\) and a finite family

\[
\mathcal W=\{(g,S_g):g\in T_{N-1}(\tau)\}
\]

such that every candidate branch surviving to height \(N-1\) is blocked by at least one exact-fiber cardinality mismatch at height \(N\).

At the immediate next level a single mismatch

\[
\mu(S)\ne\mu(\tau S)
\]

may kill the seed. At later heights, however, prior extension choices can branch. The generally correct object is therefore a **finite obstruction family/tree**, not an unqualified single witness.

### Structural, not algorithmic

The theorem is existential. It does not assert that one can effectively compute all relevant multiplicities, decide FFC, determine the least death height, or algorithmically enumerate a certificate from the ordinary input data. “Finite certificate” here means a finite mathematical obstruction once the relevant exact-fiber cardinalities are known.

---

# 6. Noncompact failure requires an infinite fiber

## Corollary 6.1

If a seed extends to every finite Pratt height but has no global extension, then FFC fails. Hence some exact fiber is infinite:

\[
\boxed{\exists S\quad\mu(S)=\aleph_0.}
\]

Thus infinite fibers are the only possible source of a failure of the finitely-branching compactness mechanism.

---

# 7. The transposition \(3\leftrightarrow5\)

Under FFC exactly one of the following occurs for

\[
\tau=(3\ 5):
\]

- **finite death:** there is a least finite Pratt height at which every surviving extension is blocked by a finite obstruction family;
- **global survival:** the transposition survives every finite height and therefore extends globally.

There is no third possibility under FFC.

This does not imply that the all-finite regime is arithmetically easy. It says only that **noncompact inverse-limit failure cannot occur there**. Determining which alternative holds may still require difficult exact-fiber arithmetic.

---

# 8. Relation to HFI and the mixed regime

The earlier Higher-Fiber Infinitude hypothesis HFI states, roughly, that every higher exact fiber relevant to the seed is countably infinite. Under HFI, the seed transposition survives globally.

FFC is the opposite endpoint:

\[
\mu(S)<\infty
\]

for every exact support.

The mixed regime — some exact fibers finite, others infinite — is the regime in which noncompact extension-tree phenomena **may** occur. It is not claimed to be the only arithmetically difficult regime.

---

# 9. Continuity with HATTER-SOL-01

The first article begins with

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
\]

HATTER-SOL-05 asks what happens to a particular **transposition/element** of this prime-permutation symmetry,

\[
(3\ 5),
\]

when one restores only the weak additive shadow

\[
q\mid p-1.
\]

The exact-fiber multiplicities are precisely the arithmetic data controlling extension through the Pratt-height tower.

We deliberately avoid calling \((3\ 5)\) a “generator” of \(\operatorname{Sym}(\mathbb P)\): it is one transposition among the prime permutations under study.

---

# 10. Literature boundary

The compactness step is an application of König's infinity lemma to a finitely branching extension tree and is not claimed as a new abstract graph-theoretic theorem.

The contribution here is its exact formulation for the radical-predecessor multiplicity tower and the structural finite-obstruction interpretation of seed death.

The 2012 MathOverflow discussion initiated by David Feldman, with Gjergji Zaimi's answer, already identified exact predecessor classes as central to this graph and explicitly connected large fibers with automorphism survival. HATTER-SOL-05 therefore does not claim priority for the basic exact-support architecture or for the broad finite-versus-infinite fiber dichotomy.

The present theorem package instead develops the finite-height extension tree, the exact compactness statement under FFC, and its interaction with the multiplicity-tower formulation used in HATTER-SOL-04.

---

# 11. Publication status

The hostile proof/literature audit has been completed. This note is frozen for HATTER-SOL-05 v1.0.

Its rigorous conclusion is:

\[
\boxed{
\text{under FFC, global seed death is equivalent to finite-height death,}
}
\]

with a finite structural obstruction family at the first death height.

No claim is made that FFC holds for the actual prime graph or that the central automorphism question is solved.
