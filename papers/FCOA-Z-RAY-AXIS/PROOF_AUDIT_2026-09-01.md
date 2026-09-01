# Hostile Proof Audit — Prescribed-Stabilizer Support

Status: PASS WITH ONE CLARIFICATION  
Date: 2026-09-01

This audit rereads the two publication-critical arguments:

1. the arbitrary-partition phase-coherence lower bound;
2. the Partition-Overgroup Dichotomy and the singleton macro-swap reduction.

The first passes unchanged. The second is correct but its final double-coset sentence should be expanded in the publication manuscript as below.

---

## 1. Arbitrary-partition phase-coherence theorem

Let `A<=Sym(Lambda)` be transitive of degree `t>=2`, let `P` be a partition of `b` branch labels with block sizes `n_1,...,n_c`, and let

\[
G=A\wr S_b,
\qquad
H_{\mathcal P}=A^{\mathcal P}\rtimes K_{\mathcal P}.
\]

On the ordered cross-branch cell set

\[
S_\times=\{((r,i),(s,j)):r\ne s\},
\]

the claimed minimum is

\[
\boxed{
m_G(H_{\mathcal P};S_\times)
=t\sum_{j=1}^c n_j(n_j-1).
}
\]

### Audit of the upper bound

Use the within-block equality fiber

\[
F_{\mathcal P}
=\{((r,i),(s,i)):r\ne s,\ r,s\text{ in one }\mathcal P\text{-block}\}.
\]

Its cardinality is exactly

\[
t\sum_j n_j(n_j-1).
\]

Projection to branch pairs recovers the partition relation. Within each non-singleton block, preservation of the equality fiber forces the internal branch permutations to coincide pointwise, hence to be equal elements of `A`. Therefore

\[
\operatorname{Stab}_G(F_{\mathcal P})=H_{\mathcal P}.
\]

No gap found.

### Audit of the lower bound

Let `F` have exact stabilizer `H_P`. Fix a non-singleton block-size class `d`.

`K_P`-invariance makes the same-block internal relation identical on every ordered pair of branches lying in a size-`d` block. Call that diagonal-`A`-invariant relation `R_d subset Lambda^2`.

If `R_d` is empty or all of `Lambda^2`, one may apply a nonidentity element of `A` to a single branch of a size-`d` block while fixing all other branches. This extra base-group element preserves:

- the empty/full same-block fibers of that size class;
- every cross-block fiber, because independent `A x A` acts transitively there, so any `H_P`-invariant cross-block fiber is empty or full;
- all cells not incident with the modified branch trivially.

Hence exact stabilizer would be larger than `H_P`, contradiction.

Thus `R_d` is nonempty and proper. Every nonempty diagonal-`A` orbit in `Lambda^2` has size at least `t`, because its first-coordinate projection is a nonempty `A`-invariant subset and therefore all of `Lambda`, with equal positive fiber size. Therefore

\[
|R_d|\ge t.
\]

There are `m_d d(d-1)` relevant ordered branch pairs, giving the lower bound

\[
|F|\ge t\sum_{d\ge2}m_d d(d-1).
\]

No gap found.

### Verdict

\[
\boxed{\text{PASS unchanged.}}
\]

---

## 2. Partition-Overgroup Dichotomy

Let `P` be a set partition of `Omega`, and let

\[
K_{\mathcal P}=\operatorname{Stab}_{S_\Omega}(\mathcal P).
\]

Let `S` be the union of singleton blocks. Since the singleton blocks are unlabeled parts of equal size one, `K_P` induces the full symmetric group on `S`.

The theorem states: if

\[
K_P<L\le S_\Omega,
\]

then either

1. `L` contains a point transposition not lying in `K_P`; or
2. `|S|` equals the size of a non-singleton partition block and `L` contains a permutation exchanging `S` with such a block at the macro level.

### Audit of the block-image argument

Take `g in L\K_P` and a non-singleton block `B`.

Because `Sym(B)<=K_P`, all transpositions of points of `B` belong to `K_P`, and conjugating by `g` places all transpositions of points of `g(B)` in `L`.

If `g(B)` meets two partition blocks and at least one is non-singleton, one of those conjugate transpositions crosses target blocks and is forbidden.

If `g(B) subset S` properly, a transposition between one point of `g(B)` and one point of `S\g(B)` lies in `K_P`; conjugating it back produces a forbidden transposition crossing `B` and its complement.

Therefore, when no forbidden transposition exists, every non-singleton block maps either

- wholly onto a non-singleton block of the same size, or
- wholly onto `S`, which forces `|B|=|S|`.

Applying the same argument to `g^{-1}` shows that if no block maps to `S`, then `S` is preserved setwise and all non-singleton blocks are permuted within their size classes. Thus `g in K_P`, contradiction.

No gap found.

---

## 3. Strengthened macro-swap double-coset lemma

The publication manuscript should replace the compressed final sentence by the following explicit lemma.

### Lemma — Macro-Mover Double Coset

Assume

\[
s:=|S|\ge2
\]

and that `P` has `m_s>=1` non-singleton blocks of size `s`.

Let

\[
\mathcal M=\{S,B_1,\ldots,B_{m_s}\}
\]

be the macro-set consisting of `S` and all size-`s` non-singleton blocks.

Suppose `g in S_Omega` has the following properties:

1. `g` maps each member of `M` bijectively onto another member of `M`;
2. outside the union of `M`, `g` maps every partition block onto a block of the same size.

Let `K=K_P`. Fix any permutation `tau` that swaps `S` with `B_1` by a bijection, maps `B_1` back to `S` by the inverse bijection, and fixes every other partition block setwise.

If `g(S) != S`, then

\[
\boxed{g\in K\tau K.}
\]

#### Proof

The induced action of `K` on the macro-set `M` is the full stabilizer of the distinguished macro-point `S`:

\[
K^{\mathcal M}\cong S_{m_s}.
\]

Indeed `K` permutes the non-singleton size-`s` blocks arbitrarily and fixes `S` as a set.

The full symmetric group on `M` is

\[
S_{m_s+1}.
\]

Its point stabilizer `S_{m_s}` has two double cosets: the stabilizer itself and the set of permutations moving the distinguished point. Equivalently, for any macro-permutation `\bar g` with `\bar g(S) != S`, there are `\bar k_1,\bar k_2 in S_{m_s}` such that

\[
\bar g=\bar k_1\bar\tau\bar k_2,
\]

where `\bar\tau` is the transposition of `S` and `B_1`.

Choose lifts `k_1,k_2 in K` inducing `\bar k_1,\bar k_2`. Then

\[
h=k_1^{-1}gk_2^{-1}\tau^{-1}
\]

fixes every macro-block setwise and maps every other partition block to itself or another same-size block already permitted by `K`. By composing, if necessary, with block permutations in `K`, we may make `h` fix every partition block setwise.

Inside each partition block, `K` contains the full symmetric group; on `S`, `K` contains `Sym(S)`. Hence the remaining internal bijections of `h` also lie in `K`. Therefore `h in K`, and so

\[
g\in K\tau K.
\]

□

### Why this is safer

The strengthened proof makes explicit:

- the macro-set;
- the induced point-stabilizer action;
- why all internal bijection choices are absorbed by `K`;
- why only one canonical macro-swap must be tested in the exact recognition theorem.

### Verdict

\[
\boxed{\text{PASS after exposition strengthening; no theorem change.}}
\]

---

## 4. Exact recognition theorem

For a `K_P`-invariant loopless directed relation `R`, the statement

\[
\operatorname{Aut}(R)=K_P
\]

is equivalent to:

1. every representative forbidden cross-block point transposition fails to preserve `R`;
2. if `|S|` equals a non-singleton block size, one canonical macro-swap fails to preserve `R`.

The strengthened double-coset lemma completes the only compressed step in the earlier proof.

### Verdict

\[
\boxed{\text{PASS.}}
\]

---

## 5. Publication status after proof audit

No central theorem was withdrawn or weakened.

One proof exposition was strengthened before publication.

The branch is now suitable for manuscript assembly, subject to ordinary editorial checks (notation, equation numbering, bibliography, verifier freeze, and RU/EN consistency).
