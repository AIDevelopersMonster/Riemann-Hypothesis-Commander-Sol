# H19-15 · Physical Visibility Atlas Protocol

Status: **PROTOCOL CLOSED / MEASUREMENT PENDING LOCAL QUARTUS RUN**

## 1. Purpose

H19-14 introduced the latent partition gap at generic compiler stages.

The next step is physical mapping.

A physical FPGA result should not be reduced to one scalar comparison such as
"smaller ALM count" or "higher Fmax". Different physical coordinates are
different observers and may induce different partitions of the presentation
family.

The first physical family remains

\[
\mathcal F
=
\{DIRECT12,PREFIX19,NIELSEN12\}.
\]

All members use the same H18 restricted-12 E0 semantic task, one-cycle
registered shell, target, Quartus version and timing protocol.

## 2. Frozen physical target

Target device:

\[
\boxed{\mathrm{5CEFA7F23C6}}
\]

Tool:

\[
\boxed{\text{Quartus II 13.1}}
\]

Timing reference:

\[
100\text{ MHz}
\]

Worst-path protocol:

\[
\boxed{
\text{Slow 1100 mV / 85 C}.
}
\]

## 3. Physical observers

The first atlas uses the coordinates

\[
O_{\rm ALM},
\quad
O_{\rm reg},
\quad
O_{\rm DSP},
\quad
O_{F_{\max}},
\]

\[
O_{\rm delay},
\quad
O_{\rm logicdepth},
\quad
O_{\rm celldelay},
\quad
O_{\rm routedelay}.
\]

Each observer induces a partition

\[
\mathcal P_{\rm phys}(O)
\]

of the three-presentation family.

No scalar total order is imposed on these coordinates.

## 4. Joint measured-profile observer

Let

\[
O_{\rm joint}
\]

be the tuple of every physical coordinate that is successfully extracted for
all three presentations.

Then

\[
O_j\preceq O_{\rm joint}
\]

for every included coordinate observer.

The induced partition

\[
\mathcal P_{\rm joint}
\]

is therefore the finest partition supported by the measured summary
coordinates.

It is not identified with the complete Quartus implementation database.

This distinction is mandatory.

## 5. Profile-relative latent gap

For each physical coordinate observer \(O\), define

\[
L_{\rm profile}(O)
=
Q(\mathcal P_O)
-
Q(\mathcal P_{\rm joint}),
\]

where

\[
Q(\mathcal P)
=
\sum_{B\in\mathcal P}
\binom{|B|}{2}.
\]

Then

\[
\boxed{
L_{\rm profile}(O)\ge0.
}
\]

Interpretation:

- \(L_{\rm profile}(O)=0\): that one coordinate separates presentations just
  as finely as the measured joint physical profile;
- \(L_{\rm profile}(O)>0\): the coordinate hides distinctions that are exposed
  by other measured physical coordinates.

This is deliberately weaker than H19-14's full-state latent gap.

## 6. DIRECT12/PREFIX19 physical visibility vector

For the pair

\[
D= DIRECT12,
\qquad
P= PREFIX19,
\]

define the physical visibility vector

\[
V_{\rm phys}(D,P)
=
(
\nu_{\rm ALM},
\nu_{\rm reg},
\nu_{\rm DSP},
\nu_{F_{\max}},
\nu_{\rm delay},
\nu_{\rm logicdepth},
\nu_{\rm celldelay},
\nu_{\rm routedelay}
),
\]

with only coordinates successfully extracted for all three presentations kept
in the final vector.

A bit is one iff the two printed Quartus values differ at the frozen reporting
precision.

This is a measurement convention, not a mathematical equality claim beyond
that report precision.

## 7. Automated laboratory closure

The matched runner run_all_cyclonev_a7.ps1 now performs:

1. direct12 Quartus compile;
2. prefix19 Quartus compile;
3. nielsen12 Quartus compile;
4. matched summary extraction;
5. physical visibility-atlas analysis.

The generated outputs are:

- H19_LAB01_CYCLONEV_SUMMARY.csv;
- H19_LAB01_PHYSICAL_PARTITIONS.csv;
- H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md.

The analyzer refuses to produce a physical atlas unless all three designs have

\[
\boxed{\mathrm{FIT}}
\]

status.

Thus NOFIT cannot silently enter a routed-timing partition.

## 8. Interpretation rule

The scientifically relevant physical object is

\[
\boxed{
O_{\rm phys}
\longmapsto
\mathcal P_{\rm phys}(O_{\rm phys}).
}
\]

Not:

\[
\text{one design is globally better}.
\]

For example, it is entirely possible that

\[
\mathcal P_{\rm ALM}
\ne
\mathcal P_{F_{\max}}
\]

or that one coordinate merges \(D,P\) while another separates them.

Such disagreement is not noise by definition. It is the physical analogue of
the compiler-stage observer dependence already found in H19-11/H19-14.

## 9. What would count as the first physical H19 result

The first publication-relevant physical result requires the completed matched
atlas and one of the following nontrivial outcomes:

1. distinct physical observers induce different partitions;
2. DIRECT12/PREFIX19 become hidden under one physical coordinate but remain
   separated under another;
3. the joint physical profile preserves all three presentation classes while
   some scalar coordinates merge them;
4. the physical stage reproduces or reverses an earlier compiler visibility
   relation in a reproducible way.

A completely discrete partition under every physical coordinate would still be
valid evidence, but it would be a weaker structural result.

## 10. Cross-technology gate

No stable presentation-survival law is claimed from Cyclone V alone.

After the first atlas is measured, the next serious persistence test is the
same family under a second technology/target with the same observer definitions
as far as the vendor reports permit.

Only then may H19 discuss cross-technology stability of a partition/frontier
trajectory.

## 11. Current state

Protocol:

\[
\boxed{\text{CLOSED}}
\]

Automation:

\[
\boxed{\text{CLOSED}}
\]

Physical measurements:

\[
\boxed{\text{PENDING LOCAL QUARTUS II 13.1 RUN}}
\]

Therefore H19-15 is not yet a physical-result theorem.

It is the frozen experimental contract that will prevent post-hoc metric
selection after the Quartus numbers are known.
