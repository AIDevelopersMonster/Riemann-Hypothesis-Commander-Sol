# H19-12 · Presentation Partition Lattice

Status: **CLOSED FOUNDATIONAL FINITE-FAMILY LAYER**

## 1. Motivation

H19-08 assigns a bit to one presentation pair.

H19-11 upgrades that bit to a visibility frontier over an observer poset.

For a finite family of more than two E0-equivalent presentations, the natural
object is not a collection of unrelated pairwise bits. It is the partition of
the presentation family induced by an observer.

The first frozen family is

\[
\mathcal F
=
\{D,P,N\}
=
\{DIRECT12,PREFIX19,NIELSEN12\}.
\]

All three implement the same restricted-12 E0 semantic contract.

## 2. Observer-induced equivalence

Fix a compiler stage \(i\), realization discipline \(\Pi\), and observer \(O\).

Define

\[
M_a\sim_{i,\Pi,O}M_b
\]

iff

\[
O(C_{i,\Pi}(M_a))
=
O(C_{i,\Pi}(M_b)).
\]

This is an equivalence relation.

Hence every observer induces a partition

\[
\boxed{
\mathcal P_{i,\Pi,O}
=
\mathcal F/{\sim_{i,\Pi,O}}.
}
\]

For three presentations the possible class-count values are

\[
1,\ 2,\ 3.
\]

But class count alone does not determine the partition: for example

\[
\{\{D,P\},\{N\}\}
\]

differs from

\[
\{\{D,N\},\{P\}\}.
\]

Therefore H19 retains the actual partition, not only its cardinality.

## 3. Partition refinement order

For partitions \(\mathcal P,\mathcal Q\) of the same finite set, write

\[
\mathcal P\preceq\mathcal Q
\]

when \(\mathcal Q\) refines \(\mathcal P\): every block of \(\mathcal Q\) is
contained in a block of \(\mathcal P\).

Thus the one-block partition is coarsest and the singleton partition is finest.

## 4. Theorem H19-12.1 — observer refinement induces partition refinement

If

\[
O_a\preceq O_b
\]

in the observer order, then

\[
\boxed{
\mathcal P_{i,\Pi,O_a}
\preceq
\mathcal P_{i,\Pi,O_b}.
}
\]

### Proof

If two presentations are equal under the finer observer \(O_b\), then because

\[
O_a=f\circ O_b,
\]

they are equal under \(O_a\). Therefore every \(O_b\)-equivalence class lies
inside an \(O_a\)-equivalence class. \(\square\)

This is the finite-family version of H19-09's pairwise monotonicity theorem.

## 5. H19 three-presentation data at post-proc/opt

Under the open Yosys post-proc/opt flow:

\[
D:4919\text{ cells},
\]

\[
P:4919\text{ cells},
\]

\[
N:5230\text{ cells}.
\]

The complete reported cell histograms of \(D\) and \(P\) coincide, while
\(N\) differs.

Therefore

\[
\boxed{
\mathcal P_{1,O_{\rm cellhist}}
=
\{\{D,P\},\{N\}\}.
}
\]

The class count is

\[
\boxed{2}.
\]

Now use the scalar wire-count observer:

\[
D:7732,
\qquad
P:7582,
\qquad
N:8269.
\]

All three are distinct.

Hence

\[
\boxed{
\mathcal P_{1,O_{\rm wiretot}}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

Thus on this finite family the wire-count observer separates all three
presentations even though the cell-histogram observer merges two of them.

## 6. Exact finite refinement witness

The two measured partitions satisfy

\[
\boxed{
\{\{D,P\},\{N\}\}
\prec
\{\{D\},\{P\},\{N\}\}.
}
\]

This is a strict empirical partition refinement on the frozen E0 family.

It should not be confused with a universal functional relation

\[
O_{\rm cellhist}\preceq O_{\rm wiretot}
\]

on all netlists. H19-11 explicitly treats cell and wire observers as
incomparable globally.

The strict refinement is a **family-relative fact**:

\[
\boxed{
\mathcal P_{\mathcal F}(O_{\rm cellhist})
\prec
\mathcal P_{\mathcal F}(O_{\rm wiretot}).
}
\]

## 7. Post-techmap partition

After generic techmap:

\[
D=63719,
\qquad
P=63719,
\qquad
N=72867
\]

reported Boolean cells, with the complete reported Boolean-cell histograms of
\(D\) and \(P\) equal.

Therefore

\[
\boxed{
\mathcal P_{2,O_{\rm cellhist}}
=
\{\{D,P\},\{N\}\}.
}
\]

The two-class cell partition survives one compiler stage unchanged.

For the pair \(D,P\), wire counts remain different:

\[
17674\ne17531.
\]

The complete three-way wire-count partition is not asserted here because the
post-techmap NIELSEN12 wire count has not been frozen in the theorem record.

Claim discipline requires leaving that coordinate incomplete rather than
guessing it.

## 8. ABC-fast partition

After matched Yosys 0.33 abc-fast:

\[
D=60374,
\qquad
P=60383,
\qquad
N=68406.
\]

All three total cell counts are distinct.

Therefore already the scalar total-cell observer induces the discrete
partition

\[
\boxed{
\mathcal P_{3,O_{\rm celltot}}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

Since total cell count is coarser than the complete cell histogram,

\[
O_{\rm celltot}\preceq O_{\rm cellhist},
\]

the histogram partition is also discrete:

\[
\boxed{
\mathcal P_{3,O_{\rm cellhist}}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

## 9. Compiler-induced partition dynamics

For the fixed cell-histogram observer, the measured open-flow sequence is

\[
\boxed{
\{\{D,P\},\{N\}\}
\to
\{\{D,P\},\{N\}\}
\to
\{\{D\},\{P\},\{N\}\}
}
\]

from post-proc through post-techmap to ABC-fast.

Thus the compiler tower itself changes the observer-induced partition.

In particular, the pair \(D,P\) moves from one common block to two singleton
blocks under the same declared observer family at a later stage.

This is the finite-family counterpart of H19-07's pairwise re-separation.

## 10. Theorem H19-12.2 — partition dynamics need not be monotone across compiler stages

There is no general requirement that

\[
\mathcal P_{i,O}
\preceq
\mathcal P_{i+1,O}
\]

or that

\[
\mathcal P_{i+1,O}
\preceq
\mathcal P_{i,O}
\]

for a coarse observer \(O\).

The H19 family supplies a concrete non-absorbing example for the cell observer:

\[
\boxed{
\{\{D,P\},\{N\}\}
\to
\{\{D\},\{P\},\{N\}\}.
}
\]

This does not contradict H19-09's no-resurrection theorem, because the theorem
there applies to **complete compiler state**, not to a coarse observer-induced
partition.

## 11. Information count versus partition shape

Define the observed class count

\[
N_{i,\Pi,O}
=
|\mathcal P_{i,\Pi,O}|.
\]

For the current family:

### post-proc/opt

\[
N_{1,O_{\rm cellhist}}=2,
\]

\[
N_{1,O_{\rm wiretot}}=3.
\]

### post-techmap

\[
N_{2,O_{\rm cellhist}}=2.
\]

### ABC-fast

\[
N_{3,O_{\rm celltot}}=3.
\]

The scalar count is useful but secondary.

The primary object remains the partition itself because different two-class
partitions encode different identifications among presentations.

## 12. Pairwise visibility is the edge shadow of a partition

For a finite family \(\mathcal F\), define the visibility graph of observer
\(O\):

- vertices are presentations;
- connect \(M_a,M_b\) iff the observer distinguishes them.

Because indistinguishability is an equivalence relation, the complement of
this graph is a disjoint union of cliques corresponding exactly to partition
blocks.

Hence pairwise visibility bits contain no extra information beyond the full
observer-induced partition if all pairs are measured consistently.

For the post-proc cell observer:

\[
D\sim P,\qquad
D\not\sim N,\qquad
P\not\sim N.
\]

For ABC total cells:

\[
D\not\sim P,\qquad
D\not\sim N,\qquad
P\not\sim N.
\]

## 13. Partition signature

For a fixed observer sequence \(O_0,\ldots,O_k\), define the
**presentation-partition signature**

\[
\boxed{
\mathfrak P(\mathcal F)
=
(
\mathcal P_{0,O_0},
\ldots,
\mathcal P_{k,O_k}
).
}
\]

This generalizes the pairwise survival word.

For \(|\mathcal F|=2\), every partition is either

\[
\{\{M_1,M_2\}\}
\]

or

\[
\{\{M_1\},\{M_2\}\},
\]

so the partition signature reduces exactly to a binary survival word.

Thus

\[
\boxed{
\text{survival words are the two-presentation special case of partition
signatures}.
}
\]

## 14. Partition lattice as Boolean-geometry object

The set of all partitions of \(\mathcal F\), ordered by refinement, is the
classical partition lattice.

H19 does not claim the partition lattice itself as new.

The H19 object is the map

\[
\boxed{
(i,\Pi,O)
\longmapsto
\mathcal P_{i,\Pi,O}
}
\]

generated by a controlled family of E0-equivalent mathematical presentations
under real compiler flows.

This separates three sources of structure:

1. presentation family \(\mathcal F\);
2. realization/compiler coordinate \((i,\Pi)\);
3. observer resolution \(O\).

## 15. Current exact atlas for the first family

The verified entries are:

| stage | observer | induced partition |
| --- | --- | --- |
| proc/opt | cell histogram | \(\{\{D,P\},\{N\}\}\) |
| proc/opt | wire count | \(\{\{D\},\{P\},\{N\}\}\) |
| techmap | cell histogram | \(\{\{D,P\},\{N\}\}\) |
| ABC-fast | total cell count | \(\{\{D\},\{P\},\{N\}\}\) |
| ABC-fast | cell histogram | \(\{\{D\},\{P\},\{N\}\}\) |

This is the first complete finite partition-atlas slice in H19.

## 16. Claim boundary

All partition statements are relative to:

- the finite family \(\mathcal F\);
- exact source generator version;
- compiler/version/options;
- realization discipline;
- observer definition.

No partition is asserted to be an invariant of the semantic function alone.

No unrestricted Boolean complexity conclusion follows from a partition
refinement.

## 17. Next target

The physical H19-LAB-01 result should be recorded not as three unrelated FPGA
rows but as a family of physical partitions:

\[
\mathcal P_{\rm ALM},
\quad
\mathcal P_{\rm DSP},
\quad
\mathcal P_{\rm reg},
\quad
\mathcal P_{F_{\max}},
\quad
\mathcal P_{\rm delay},
\ldots
\]

The next question is whether these physical observer partitions agree,
conflict, or form a nontrivial refinement pattern.

That is the correct family-level meaning of a **physical visibility atlas**.
