# H19-08 · Presentation-Survival Words

Status: **FOUNDATIONAL RESULT / FIRST FINITE EXAMPLE CLOSED**

## 1. Motivation

For two E0-equivalent mathematical presentations, visibility of their
difference need not change monotonically along a compiler flow.

The controlled H19 pair

\[
D= DIRECT12,
\qquad
P= PREFIX19
\]

already gives:

\[
24\neq19
\]

at the source composition-node observable,

\[
4919=4919
\]

after Yosys \`proc/flatten/opt\` at the reported cell-histogram observable,

\[
63719=63719
\]

after \`techmap/opt\` at the generic Boolean-cell histogram,

and

\[
60374\neq60383
\]

after matched \`abc -fast\` generic logic synthesis.

Thus the source distinction is visible, becomes hidden, remains hidden, and
then reappears.

---

## 2. Visibility bit

Fix:

- two E0-equivalent presentations \(M_1,M_2\);
- a compiler-stage sequence
  \[
  S_0,S_1,\ldots,S_k;
  \]
- one declared observable \(O_i\) at each stage.

Define

\[
\nu_i(M_1,M_2)
=
\begin{cases}
1,&O_i(S_i(M_1))\neq O_i(S_i(M_2)),\\
0,&O_i(S_i(M_1))=O_i(S_i(M_2)).
\end{cases}
\]

No monotonicity is assumed.

## 3. Presentation-survival word

Define

\[
\boxed{
W(M_1,M_2)
=
\nu_0\nu_1\cdots\nu_k
}
\]

and call it the **presentation-survival word** relative to the declared
compiler tower and observable sequence.

The word is not an invariant of the mathematics alone.  It is indexed by the
entire experiment:

\[
W_{S,O,\Pi}(M_1,M_2).
\]

## 4. First H19 survival word

For DIRECT12 versus PREFIX19, use the stage/observable pairs:

\[
\begin{array}{c|l}
0 & \text{source composition-node count}\\
1 & \text{post-proc/opt complete reported cell histogram}\\
2 & \text{post-techmap complete reported Boolean-cell histogram}\\
3 & \text{post-ABC-fast total generic-cell count}
\end{array}
\]

Current exact/measured evidence gives

\[
\boxed{
W(DIRECT12,PREFIX19)=1001.
}
\]

Interpretation:

\[
\boxed{
\text{visible}
\to
\text{hidden}
\to
\text{hidden}
\to
\text{visible}.
}
\]

This is the first H19 non-monotone survival example.

## 5. Re-separation index

Define the first forgetting index

\[
f=\min\{i:\nu_i=0\},
\]

when such an index exists.

If there is a later stage with visibility restored, define the first
re-separation index

\[
\boxed{
r=\min\{j>f:\nu_j=1\}.
}
\]

For the current H19 pair,

\[
\boxed{
f=1,\qquad r=3.
}
\]

These indices are compiler/observable-relative.

## 6. Survival transition count

Define

\[
T(W)
=
\sum_{i=1}^{k}|\nu_i-\nu_{i-1}|.
\]

For

\[
W=1001,
\]

\[
\boxed{T(W)=2}.
\]

A word with \(T=0\) has constant visibility over the measured tower.
A word with \(T\ge2\) exhibits at least one disappearance and reappearance, or
vice versa.

The H19 pair is therefore a certified/measured example with nonzero
presentation-visibility oscillation.

## 7. Why monotonicity cannot be assumed

A compiler stage is not generally an information-monotone projection with
respect to a chosen coarse observable.

Even if two intermediate netlists have equal cell histograms, they may have
different wiring, logic cones, don't-care structure, or local Boolean forms.
A later optimization can map those hidden structural differences into
different cell counts again.

Thus

\[
O_i(C_i(M_1))=O_i(C_i(M_2))
\]

does not imply

\[
O_{i+1}(C_{i+1}(M_1))
=
O_{i+1}(C_{i+1}(M_2)).
\]

This is a logical statement about incomplete observables, not a claim that the
compiler reconstructs information that was literally destroyed from its full
internal state.

## 8. Full-state versus observed forgetting

This distinction is essential.

At the post-techmap stage DIRECT12 and PREFIX19 had equal reported cell
histograms but different wire profiles.

Therefore H19-04 did **not** prove equality of full netlists.

The re-separation at ABC is consistent with the survival of source-sensitive
information in a finer internal representation that the chosen histogram
observable did not expose.

Hence the correct phrase is

\[
\boxed{
\text{observable forgetting}
}
\]

rather than irreversible compiler information destruction.

## 9. Observable lattice

Let \(O_a\preceq O_b\) mean that \(O_b\) is at least as discriminating as
\(O_a\):

\[
O_b(C_1)=O_b(C_2)
\Longrightarrow
O_a(C_1)=O_a(C_2).
\]

Then each compiler stage has a family of possible survival bits, depending on
observable resolution.

For example at post-techmap:

- total cell count: hidden;
- complete cell histogram: hidden;
- wire-count vector: visible.

Thus presentation survival should be studied over an **observable lattice**,
not by one scalar metric.

This leads to the next theoretical object:

\[
\boxed{
\mathcal V_i(M_1,M_2)
=
\{O:\ O(C_i(M_1))\neq O(C_i(M_2))\},
}
\]

the family of observables that still distinguish the pair at stage \(i\).

## 10. Physical extension

H19-LAB-01 adds the next stage

\[
S_4=\text{Cyclone-V Quartus P\&R}.
\]

The current survival word is therefore a prefix:

\[
\boxed{1001?}
\]

The Quartus experiment will determine whether the physical-profile observable
extends it as

\[
10010
\]

or

\[
10011,
\]

depending on whether the chosen physical profile distinguishes DIRECT12 and
PREFIX19.

If different physical coordinates disagree, no single final bit should be
forced; the physical stage must instead be reported as a vector of visibility
bits by coordinate.

## 11. Claim boundary

The survival word is relative to:

- presentation pair;
- semantics and encoding;
- realization discipline;
- compiler and version;
- stage definition;
- observable choice.

It is not a technology-independent invariant of the abstract task.

Its purpose is to formalize **where and at what resolution mathematical
presentation differences remain experimentally visible**.
