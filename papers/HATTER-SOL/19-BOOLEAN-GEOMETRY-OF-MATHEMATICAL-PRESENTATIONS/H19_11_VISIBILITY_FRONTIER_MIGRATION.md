# H19-11 · Visibility-Frontier Migration

Status: **CLOSED FINITE THEOREM/EXPERIMENT LAYER**

## 1. Purpose

H19-08 compresses a presentation pair into one survival word.

H19-09 shows that a single bit per stage is too coarse: visibility depends on
the chosen observer, and the visible-observer family is an upset in an observer
poset.

The next finite object is therefore the **visibility matrix** and its minimal
visible frontier.

This note closes that construction for the frozen pair

\[
D=DIRECT12,
\qquad
P=PREFIX19.
\]

All numerical entries below come from the already closed H19-04, H19-05 and
H19-07 experiments.

---

## 2. Frozen compiler path

The open-flow path is

\[
S_0=\text{source},
\]

\[
S_1=\text{Yosys proc/flatten/opt},
\]

\[
S_2=\text{Yosys techmap/opt},
\]

\[
S_3=\text{Yosys abc -fast}.
\]

A separate presentation-preserving control

\[
S_{\rm mod}
\]

uses retained mathematical primitive modules and is not inserted into the open
flow as though it were another serial compiler stage.

---

## 3. Declared observer families

### 3.1 Source observer

At source level use

\[
O_{\rm comp}
=
\text{number of declared permutation-composition nodes}.
\]

For the frozen pair,

\[
O_{\rm comp}(D)=24,
\qquad
O_{\rm comp}(P)=19.
\]

Hence

\[
\nu_0(O_{\rm comp})=1.
\]

### 3.2 Cell observers

At a netlist stage define

\[
O_{\rm celltot}
=
\text{total reported cell count},
\]

and

\[
O_{\rm cellhist}
=
\text{complete reported cell-type histogram}.
\]

Because total cell count is the sum of histogram coordinates,

\[
\boxed{
O_{\rm celltot}\preceq O_{\rm cellhist}.
}
\]

### 3.3 Wire observers

Define

\[
O_{\rm wiretot}
=
\text{reported wire count},
\]

and, when available,

\[
O_{\rm wirevec}
=
(\text{wires},\text{wire bits},
\text{public wires},\text{public wire bits}).
\]

Then

\[
\boxed{
O_{\rm wiretot}\preceq O_{\rm wirevec}.
}
\]

The cell and wire observer chains are not assumed comparable.

### 3.4 Full-state observer

Let

\[
I_i
\]

be the full compiler-state identity observer from H19-09.

Every declared coarse observer is below \(I_i\).

---

## 4. Exact visibility matrix

Use symbols

- \(1\): measured/proved visible;
- \(0\): measured hidden;
- \(*\): observer not used or not available at that stage.

For DIRECT12 versus PREFIX19:

| observer | source \(S_0\) | proc/opt \(S_1\) | techmap \(S_2\) | ABC-fast \(S_3\) |
| --- | ---: | ---: | ---: | ---: |
| composition-node count \(O_{\rm comp}\) | **1** | * | * | * |
| total cell count \(O_{\rm celltot}\) | * | **0** | **0** | **1** |
| complete cell histogram \(O_{\rm cellhist}\) | * | **0** | **0** | **1** |
| total wire count \(O_{\rm wiretot}\) | * | **1** | **1** | * |
| wire profile \(O_{\rm wirevec}\) | * | **1** | **1** | * |
| full compiler state \(I_i\) | **1** | **1** | **1** | **1** |

The full-state row at \(S_1,S_2\) follows both from the measured wire
difference and independently from H19-09's retrospective no-resurrection
argument using the later ABC distinction.

---

## 5. Numerical certificate

### Source

\[
\boxed{
24\ne19.
}
\]

### Post-proc/opt

Cell count:

\[
4919=4919.
\]

Wire count:

\[
7732\ne7582.
\]

Wire bits:

\[
136842\ne132987.
\]

Public wires:

\[
3804\ne3654.
\]

Public wire bits:

\[
81978\ne78123.
\]

Thus the cell observers are hidden while even the coarse wire-count observer is
visible.

### Post-techmap

Cell count:

\[
63719=63719.
\]

Complete reported Boolean-cell histograms also coincide.

Wire count:

\[
17674\ne17531.
\]

Wire bits:

\[
600635\ne597020.
\]

Again the cell observer chain is hidden while the wire observer chain is
visible.

### ABC-fast

Total cell count:

\[
60374\ne60383.
\]

Hence already the coarsest declared cell observer distinguishes.

By observer refinement,

\[
\nu_3(O_{\rm celltot})=1
\Longrightarrow
\nu_3(O_{\rm cellhist})=1.
\]

The published ABC histogram confirms this directly.

---

## 6. Minimal visible frontier

For each stage, restrict attention to the finite declared observer poset
available at that stage.

Define

\[
\partial\mathcal V_i
=
\min\{O:\nu_i(O)=1\}.
\]

### Source

The declared source observer family has

\[
\boxed{
\partial\mathcal V_0
=
\{O_{\rm comp}\}.
}
\]

### Post-proc/opt

The entire cell chain is hidden:

\[
\nu_1(O_{\rm celltot})
=
\nu_1(O_{\rm cellhist})
=
0.
\]

But

\[
\nu_1(O_{\rm wiretot})=1.
\]

Since

\[
O_{\rm wiretot}\preceq O_{\rm wirevec},
\]

the minimal visible frontier is

\[
\boxed{
\partial\mathcal V_1
=
\{O_{\rm wiretot}\}.
}
\]

### Post-techmap

Exactly the same declared frontier occurs:

\[
\boxed{
\partial\mathcal V_2
=
\{O_{\rm wiretot}\}.
}
\]

### ABC-fast

Now

\[
\nu_3(O_{\rm celltot})=1.
\]

Since \(O_{\rm celltot}\) is the coarsest declared cell observer,

\[
\boxed{
\partial\mathcal V_3
=
\{O_{\rm celltot}\}
}
\]

within the measured ABC observer family.

---

## 7. Frontier-migration law for the frozen pair

The observed minimal distinguishing coordinate therefore migrates as

\[
\boxed{
O_{\rm comp}
\longrightarrow
O_{\rm wiretot}
\longrightarrow
O_{\rm wiretot}
\longrightarrow
O_{\rm celltot}.
}
\]

In words:

\[
\boxed{
\text{source factorization}
\to
\text{wiring}
\to
\text{wiring}
\to
\text{Boolean gate count}.
}
\]

This is a strictly stronger description than the coarse word

\[
1001.
\]

The word says only whether one chosen observer distinguishes.

The frontier trajectory says **which least discriminating declared observer is
already sufficient** at each stage.

---

## 8. Theorem H19-11.1 — frontier determines the finite visibility field

Let \(\mathcal O_i\) be a finite observer poset at stage \(i\).

Then the visibility function

\[
\nu_i:\mathcal O_i\to\{0,1\}
\]

is monotone and is uniquely determined by the antichain

\[
\partial\mathcal V_i.
\]

Specifically,

\[
\boxed{
\nu_i(O)=1
\iff
\exists F\in\partial\mathcal V_i
\text{ with }
F\preceq O.
}
\]

### Proof

By H19-09, the visible set

\[
\mathcal V_i=\{O:\nu_i(O)=1\}
\]

is an upset. Every element of a finite upset lies above at least one minimal
element of that upset. Conversely, every observer above a visible observer is
visible by monotonicity. Therefore \(\mathcal V_i\), and hence \(\nu_i\), is
determined exactly by its minimal antichain. \(\square\)

---

## 9. Theorem H19-11.2 — equal coarse cells do not imply equal structural image

For the frozen DIRECT12/PREFIX19 pair at both \(S_1\) and \(S_2\),

\[
O_{\rm cellhist}(C_i(D))
=
O_{\rm cellhist}(C_i(P)),
\]

but

\[
O_{\rm wiretot}(C_i(D))
\ne
O_{\rm wiretot}(C_i(P)).
\]

Therefore

\[
\boxed{
\ker O_{\rm wiretot}
\not\supseteq
\ker O_{\rm cellhist}
}
\]

on this pair.

Equivalently, the cell-histogram and wire-count observers are genuinely
incomparable as information channels in the empirical compiler image: equality
under the apparently richer **cell-type** description does not force equality
of even the scalar wire count.

This is not a paradox because neither observer is a deterministic function of
the other on the full netlist state.

---

## 10. Presentation-preserving control

The module-preserving experiment is a second realization discipline, not a
serial stage of the open tower.

Under \(\Pi_{\rm module}\),

\[
D:
24\ {\rm compose}+2\ {\rm inverse},
\]

\[
P:
19\ {\rm compose}+2\ {\rm inverse}.
\]

The retained core-cell counts are

\[
1591\ne1586.
\]

Thus even the scalar hierarchical core-cell observer distinguishes:

\[
\boxed{
\nu_{\rm module}(O_{\rm corecell})=1.
}
\]

This gives a second visibility frontier controlled by compiler discipline:

\[
\boxed{
\Pi_{\rm open}
\ne
\Pi_{\rm module}
}
\]

not merely by compiler stage.

---

## 11. Two-dimensional visibility atlas

H19 should therefore index visibility by two independent coordinates:

\[
\boxed{
(\text{compiler stage},\text{realization discipline}).
}
\]

The finite observable state becomes

\[
\Gamma_{\Pi,i,\alpha}
=
\mathbf 1[
O_\alpha(C_{\Pi,i}(D))
\ne
O_\alpha(C_{\Pi,i}(P))
].
\]

The earlier matrix \(\Gamma_{i,\alpha}\) is one slice at fixed
\(\Pi=\Pi_{\rm open}\).

This is the first genuine **atlas** interpretation of H19 Boolean geometry:
different realization disciplines give different visibility charts over the
same E0-equivalent presentation family.

---

## 12. Claim boundary

The frontier depends on

- the presentation pair;
- compiler/version/options;
- realization discipline;
- declared observer family;
- stage definition.

It is not an invariant of the semantic Boolean function alone.

The theorem about finite upsets and minimal antichains is elementary order
theory. H19 does not claim that abstract fact as new.

The research result is the controlled compiler instance in which the minimal
visible observer migrates

\[
O_{\rm comp}
\to
O_{\rm wiretot}
\to
O_{\rm wiretot}
\to
O_{\rm celltot},
\]

while the semantic task remains fixed.

---

## 13. Physical extension

H19-LAB-01 should add a physical chart whose observer coordinates include

\[
O_{\rm ALM},
\quad
O_{\rm DSP},
\quad
O_{\rm reg},
\quad
O_{F_{\max}},
\quad
O_{\rm logicdepth},
\quad
O_{\rm celldelay},
\quad
O_{\rm routedelay}.
\]

Because these coordinates are generally incomparable, the physical visibility
frontier may contain more than one minimal observer.

No scalar “winner” should be forced.

---

## 14. Next theorem target

The next natural object is no longer one pair.

For a finite E0-equivalent family

\[
\mathcal F=\{M_1,\ldots,M_r\},
\]

each observer induces a partition of \(\mathcal F\).

The next H19 target is therefore the **partition lattice of presentation
visibility**:

\[
\boxed{
O
\longmapsto
\mathcal F/{\sim_O}.
}
\]

This will generalize the binary DIRECT12/PREFIX19 visibility bit to the full
three-presentation family

\[
\{DIRECT12,PREFIX19,NIELSEN12\}
\]

and quantify exactly how compiler stages merge and split presentation classes.
