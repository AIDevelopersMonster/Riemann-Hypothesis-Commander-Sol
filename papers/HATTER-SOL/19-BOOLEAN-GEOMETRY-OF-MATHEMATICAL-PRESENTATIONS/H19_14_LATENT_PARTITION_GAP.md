# H19-14 · Latent Partition Gap

Status: **CLOSED FOUNDATIONAL H19-SPECIFIC LAYER**

## 1. Purpose

A coarse compiler observer can merge presentations that remain distinct in the
complete compiler state.

H19-09 proved this pairwise through the no-resurrection principle.

H19-12 lifted pairwise visibility to finite presentation partitions.

This note combines the two levels and defines the **latent partition gap**:
the structural distinction still present in the compiler state but hidden from
a declared observer.

The first exact laboratory is

\[
\mathcal F=\{D,P,N\}
=
\{DIRECT12,PREFIX19,NIELSEN12\}.
\]

---

## 2. Full-state partition

At compiler stage \(i\), define

\[
M_a\equiv_i^{\rm full}M_b
\]

iff

\[
C_i(M_a)=C_i(M_b)
\]

as complete compiler states.

This induces the full-state partition

\[
\boxed{
\mathcal P_i^{\rm full}
=
\mathcal F/{\equiv_i^{\rm full}}.
}
\]

For a declared observer \(O_i\), define

\[
M_a\equiv_i^O M_b
\]

iff

\[
O_i(C_i(M_a))
=
O_i(C_i(M_b)),
\]

with observed partition

\[
\boxed{
\mathcal P_i^O
=
\mathcal F/{\equiv_i^O}.
}
\]

Because \(O_i\) is a function of complete state,

\[
\boxed{
\mathcal P_i^{\rm full}
\preceq
\mathcal P_i^O.
}
\]

Thus the observed partition can only be as fine as, or coarser than, the
full-state partition.

---

## 3. Theorem H19-14.1 — deterministic full-state partitions can only coarsen

Let

\[
C_{i+1}=F_i\circ C_i
\]

for a deterministic compiler stage \(F_i\).

Then

\[
\boxed{
\mathcal P_i^{\rm full}
\preceq
\mathcal P_{i+1}^{\rm full}.
}
\]

### Proof

If two presentations are equal as complete states at stage \(i\), then applying
the same deterministic map \(F_i\) gives equal complete states at stage
\(i+1\).

Therefore a full-state equivalence class may merge with another class later,
but an existing full-state class cannot split.

Hence the next partition is equal or coarser. \(\square\)

This is the finite-family version of H19-09's no-resurrection theorem.

---

## 4. Hidden pair count

For a partition

\[
\mathcal P=\{B_1,\ldots,B_k\}
\]

define its indistinguishable-pair count

\[
Q(\mathcal P)
=
\sum_{j=1}^{k}
\binom{|B_j|}{2}.
\]

This counts unordered presentation pairs identified by the corresponding
equivalence relation.

Because

\[
\mathcal P_i^{\rm full}
\preceq
\mathcal P_i^O,
\]

we have

\[
Q(\mathcal P_i^{\rm full})
\le
Q(\mathcal P_i^O).
\]

Define the **latent pair gap**

\[
\boxed{
L_i(O)
=
Q(\mathcal P_i^O)
-
Q(\mathcal P_i^{\rm full}).
}
\]

Thus \(L_i(O)\) counts presentation pairs that are still different in complete
compiler state but are merged by observer \(O\).

Clearly

\[
\boxed{
L_i(O)\ge0.
}
\]

---

## 5. Theorem H19-14.2 — zero latent gap criterion

For finite \(\mathcal F\),

\[
\boxed{
L_i(O)=0
}
\]

iff the observer-induced and full-state equivalence relations identify exactly
the same presentation pairs on \(\mathcal F\).

Equivalently,

\[
\boxed{
\mathcal P_i^O
=
\mathcal P_i^{\rm full}.
}
\]

### Proof

The full-state partition refines the observed partition. Therefore every pair
identified by full state is also identified by the observer.

The difference of pair counts is zero exactly when the observer creates no
additional identified pair. Since both are equivalence relations on the same
finite set and one refines the other, this is equivalent to equality of the
partitions. \(\square\)

---

## 6. Full-state partition for the frozen H19 family

### Post-proc/opt

DIRECT12 and PREFIX19 have different wire counts:

\[
7732\ne7582.
\]

NIELSEN12 has

\[
8269
\]

wires and also a different cell profile.

Hence all three complete compiler states are distinct:

\[
\boxed{
\mathcal P_1^{\rm full}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

### Post-techmap

DIRECT12 and PREFIX19 again have different wire counts:

\[
17674\ne17531.
\]

NIELSEN12 has a different Boolean-cell total:

\[
72867\ne63719.
\]

Therefore all three full states are again distinct:

\[
\boxed{
\mathcal P_2^{\rm full}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

### ABC-fast

All three total cell counts are distinct:

\[
60374,\quad60383,\quad68406.
\]

Hence

\[
\boxed{
\mathcal P_3^{\rm full}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

Thus over the measured open-flow stages the full-state partition remains
discrete.

---

## 7. Cell-observer latent gap

Use the complete reported cell-histogram observer.

### Post-proc/opt

Observed partition:

\[
\mathcal P_1^{\rm cell}
=
\{\{D,P\},\{N\}\}.
\]

Hence

\[
Q(\mathcal P_1^{\rm cell})=1.
\]

But the full-state partition is discrete, so

\[
Q(\mathcal P_1^{\rm full})=0.
\]

Therefore

\[
\boxed{
L_1(O_{\rm cellhist})=1.
}
\]

Exactly one presentation pair is hidden by the cell observer:

\[
\boxed{\{D,P\}.}
\]

### Post-techmap

Again

\[
\mathcal P_2^{\rm cell}
=
\{\{D,P\},\{N\}\},
\]

while the full state remains discrete.

Therefore

\[
\boxed{
L_2(O_{\rm cellhist})=1.
}
\]

### ABC-fast

The cell observer becomes discrete:

\[
\mathcal P_3^{\rm cell}
=
\{\{D\},\{P\},\{N\}\}.
\]

Hence

\[
\boxed{
L_3(O_{\rm cellhist})=0.
}
\]

---

## 8. First latent-gap trajectory

The frozen H19 family therefore gives

\[
\boxed{
L_{\rm cellhist}:
1\to1\to0.
}
\]

This is the exact family-level form of the earlier pairwise phenomenon

\[
\text{hidden}
\to
\text{hidden}
\to
\text{visible}.
\]

Crucially, the full-state partition did not split:

\[
\boxed{
\mathcal P_1^{\rm full}
=
\mathcal P_2^{\rm full}
=
\mathcal P_3^{\rm full}
=
\{\{D\},\{P\},\{N\}\}.
}
\]

The change

\[
1\to0
\]

in latent gap is therefore caused by the later observed image exposing a
distinction that had remained latent in the compiler state.

---

## 9. Theorem H19-14.3 — observed re-separation consumes latent gap

Suppose two presentations \(M_a,M_b\) satisfy

\[
M_a\equiv_i^O M_b
\]

at stage \(i\), but are distinguished by some later observer at stage \(j>i\).

Then

\[
M_a\not\equiv_i^{\rm full}M_b.
\]

Hence the pair contributes to the latent gap at stage \(i\).

### Proof

If the pair were equal in full state at stage \(i\), deterministic transport
would keep the full states equal at every later stage. No later observer could
distinguish them.

Therefore later re-separation implies that the pair was already distinct in
full state at the earlier stage while merged only by the coarse observer.
\(\square\)

For DIRECT12/PREFIX19, the ABC-fast re-separation is therefore an explicit
witness that their earlier cell equality represented latent, not destroyed,
structure.

---

## 10. Latent block multiplicity

Pair count is one useful scalarization, but the full object is the refinement
map

\[
\boxed{
\mathcal P_i^{\rm full}
\preceq
\mathcal P_i^O.
}
\]

For each observed block \(B\in\mathcal P_i^O\), define its latent multiplicity

\[
\lambda_i^O(B)
=
\#\{
A\in\mathcal P_i^{\rm full}:A\subseteq B
\}.
\]

Thus \(\lambda_i^O(B)\) counts how many distinct full-state classes have been
collapsed into one observed class.

For the cell observer at post-proc and post-techmap:

\[
\lambda(\{D,P\})=2,
\]

\[
\lambda(\{N\})=1.
\]

After ABC-fast every observed block has latent multiplicity one.

---

## 11. Latent partition profile

Define the multiset

\[
\boxed{
\Lambda_i(O)
=
\{
\lambda_i^O(B):
B\in\mathcal P_i^O
\}.
}
\]

For the H19 cell observer:

\[
\boxed{
\Lambda_1=\{2,1\},
}
\]

\[
\boxed{
\Lambda_2=\{2,1\},
}
\]

\[
\boxed{
\Lambda_3=\{1,1,1\}.
}
\]

This retains more structure than the scalar latent pair gap.

---

## 12. Relation to observer refinement

If

\[
O_a\preceq O_b,
\]

then

\[
\mathcal P_i^{O_a}
\preceq
\mathcal P_i^{O_b}.
\]

Thus a finer observer can only reduce or preserve latent ambiguity relative to
the same full-state partition.

In particular,

\[
\boxed{
L_i(O_b)\le L_i(O_a)
}
\]

for the hidden-pair scalar whenever \(O_b\) refines \(O_a\).

This gives a monotone quantitative observer-resolution law at a fixed compiler
stage.

---

## 13. Distinguishing compiler forgetting from observer hiding

H19 can now separate two phenomena rigorously.

### True compiler merge

If

\[
\mathcal P_{i+1}^{\rm full}
\]

is strictly coarser than

\[
\mathcal P_i^{\rm full},
\]

then distinct complete compiler states have actually merged.

By Theorem H19-14.1, such a merge is irreversible in later deterministic
stages.

### Observer hiding

If

\[
\mathcal P_i^{\rm full}
\prec
\mathcal P_i^O,
\]

then complete states remain distinct but the chosen observer hides some of the
distinction.

This hiding can disappear at a later stage because later transformations may
move latent structural differences into coordinates visible to the observer.

For the current DIRECT12/PREFIX19 data, the measured phenomenon is the second
case.

---

## 14. Claim boundary

The partition definitions and monotonicity statements are elementary finite
set theory once the compiler maps are fixed.

The H19-specific result is the measured latent-gap trajectory on the controlled
E0 family:

\[
\boxed{
1\to1\to0
}
\]

for the cell-histogram observer while the full-state partition remains
discrete.

This result is compiler/version/observer relative.

It is not a technology-independent invariant and not a lower bound on Boolean
circuit complexity.

---

## 15. Next research target

The latent-gap framework creates a sharper physical question for H19-LAB-01.

For each physical observer \(O_{\rm phys}\), compute

\[
L_{\rm phys}(O_{\rm phys})
\]

relative to the physical full-state realization.

Then ask whether physical mapping:

1. exposes the remaining latent distinctions;
2. hides new distinctions;
3. or actually merges complete implementation states under a suitably defined
   physical-state representation.

The immediate experimental target is therefore not "which design is smaller"
but

\[
\boxed{
\text{what happens to the latent partition profile under physical mapping?}
}
\]
