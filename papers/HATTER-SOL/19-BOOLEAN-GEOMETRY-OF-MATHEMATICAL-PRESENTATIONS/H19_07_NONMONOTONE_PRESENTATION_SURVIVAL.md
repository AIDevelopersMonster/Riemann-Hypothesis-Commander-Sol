# H19-07 · Non-Monotone Presentation Survival

Status: **CLOSED FIRST EXPERIMENTAL EXAMPLE**

## 1. Question

Does a mathematical distinction, once invisible at some compiler stage, remain
invisible at every later stage?

H19-04 explicitly refused to assume this monotonicity.  The matched ABC-fast
experiment now gives a counterexample at the chosen compiler observables.

## 2. Frozen E0 family

The three presentations are:

\[
DIRECT12,\qquad PREFIX19,\qquad NIELSEN12.
\]

All implement the same frozen restricted-12 semantic task and pass the common
2561-transaction E0 regression.

The source distinction between the first two is exact:

\[
DIRECT12:24\text{ composition nodes},
\]

\[
PREFIX19:19\text{ composition nodes}.
\]

Thus

\[
DIRECT12\ne PREFIX19
\]

as declared source presentations.

## 3. Open Yosys stages

### post-proc/opt

\[
DIRECT12=4919,\qquad PREFIX19=4919.
\]

Their complete reported cell histograms coincide.

### post-techmap

\[
DIRECT12=63719,\qquad PREFIX19=63719.
\]

Again their complete reported Boolean-cell histograms coincide.

Thus, at those two observables,

\[
DIRECT12\sim PREFIX19.
\]

## 4. ABC-fast stage

A third matched flow continued through

\[
\texttt{abc -fast}
\]

under Yosys 0.33.

GitHub Actions run:

\[
\boxed{\texttt{35489140510}}.
\]

The resulting total cell counts are

\[
\boxed{
DIRECT12=60374,\qquad
PREFIX19=60383,\qquad
NIELSEN12=68406.
}
\]

Hence

\[
\boxed{
DIRECT12\not\sim PREFIX19
}
\]

at the ABC-fast cell-histogram observable.

The difference is small but exact for the frozen run:

\[
\boxed{
60383-60374=9.
}
\]

The direction is also notable:

\[
19<24
\]

at the declared source composition-node count, but

\[
60383>60374
\]

after ABC-fast.

Therefore source-level compression does not preserve even the **ordering
direction** of this later compiler-relative scalar observable.

## 5. Cell-histogram details

ABC-fast reports:

| cell type | DIRECT12 | PREFIX19 | NIELSEN12 |
| --- | ---: | ---: | ---: |
| total | 60,374 | 60,383 | 68,406 |
| \`$_ANDNOT_\` | 4,053 | 4,027 | 6,108 |
| \`$_AND_\` | 726 | 746 | 854 |
| \`$_MUX_\` | 37,407 | 37,407 | 38,538 |
| \`$_NAND_\` | 564 | 574 | 693 |
| \`$_NOR_\` | 1,966 | 1,971 | 2,214 |
| \`$_NOT_\` | 707 | 706 | 755 |
| \`$_ORNOT_\` | 4,062 | 4,061 | 5,287 |
| \`$_OR_\` | 8,200 | 8,202 | 10,893 |
| \`$_XNOR_\` | 1,413 | 1,400 | 1,630 |
| \`$_XOR_\` | 1,207 | 1,220 | 1,365 |
| sequential cells | 69 | 69 | 69 |

The two designs therefore do not merely differ in a hidden wire count; ABC-fast
has produced distinct Boolean gate histograms.

NIELSEN12 remains clearly separated:

\[
68406-60374=8032
\]

cells above DIRECT12 in this flow.

## 6. Non-monotone survival proposition-example

Let

\[
O_{\rm hist}
\]

be the complete reported Boolean-cell histogram and consider the open compiler
tower after RTL process lowering.

The controlled pair exhibits

\[
O_{\rm hist}(C_{\rm proc}(DIRECT12))
=
O_{\rm hist}(C_{\rm proc}(PREFIX19)),
\]

\[
O_{\rm hist}(C_{\rm techmap}(DIRECT12))
=
O_{\rm hist}(C_{\rm techmap}(PREFIX19)),
\]

but

\[
O_{\rm hist}(C_{\rm ABCfast}(DIRECT12))
\ne
O_{\rm hist}(C_{\rm ABCfast}(PREFIX19)).
\]

Therefore equality of a compiler observable at one stage is **not absorbing**
under later optimization stages.

Equivalently, compiler-profile kernel relations need not be nested monotonically
along a compiler tower:

\[
\boxed{
\ker_O(C_{i+1})
\not\supseteq
\ker_O(C_i)
\quad\text{and}\quad
\ker_O(C_{i+1})
\not\subseteq
\ker_O(C_i)
\text{ in general}.
}
\]

The current experiment proves only the failure of the particular absorbing
assumption for the frozen pair/flow; the displayed general statement is a
warning about what cannot be assumed without additional hypotheses.

## 7. Consequence for the H19 formalism

The previously defined first forgetting index

\[
f_O(M_1,M_2)
\]

must not be interpreted as permanent information loss.

The primary object should instead be the complete **survival word**

\[
\boxed{
\Sigma_O(M_1,M_2)
=
(\epsilon_0,\epsilon_1,\ldots,\epsilon_k),
}
\]

with no monotonicity assumption.

For the measured DIRECT12/PREFIX19 sequence, presentation distinction is:

\[
\boxed{
\text{visible at source}
\to
\text{hidden at proc/opt}
\to
\text{hidden at techmap}
\to
\text{visible after ABC-fast}.
}
\]

This is the first non-monotone presentation-survival example in H19.

## 8. Claim boundary

The 9-cell difference is not claimed to be:

- technology-independent;
- stable under other ABC scripts;
- a circuit lower bound;
- a physical FPGA area difference.

It is a reproducible compiler-stage fact for Yosys 0.33 and the exact
\`abc -fast\` flow.

The next question is whether the re-emerged distinction survives FPGA mapping
and place-and-route.
