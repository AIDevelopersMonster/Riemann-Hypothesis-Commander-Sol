# H19-16 · Physical Profile Quotient on Cyclone V

Status: **PHYSICAL RESULT / CLOSED FOR THE FROZEN H19-LAB-01 PROFILE**

Date: 20 September 2026.

## 1. Frozen experiment

Presentation family:

\[
\mathcal F=\{D,P,N\}
=
\{DIRECT12,PREFIX19,NIELSEN12\}.
\]

Target:

\[
\mathrm{5CEFA7F23C6}
\]

Tool:

\[
\text{Quartus II 13.1}.
\]

All three presentations reached

\[
\boxed{\mathrm{FIT}}.
\]

The physical atlas uses the predeclared observers

\[
O_{\rm ALM},
O_{\rm reg},
O_{\rm DSP},
O_{F_{\max}},
O_{\rm delay},
O_{\rm logicdepth},
O_{\rm celldelay},
O_{\rm routedelay}.
\]

Equality means equality at the frozen Quartus report precision.

---

## 2. Matched physical measurements

The measured profile is

| presentation | ALM | registers | DSP | Fmax MHz | data delay ns | logic levels | cell ns | routing ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 10,627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| PREFIX19 | 10,627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| NIELSEN12 | 12,017 | 69 | 48 | 27.50 | 36.212 | 31 | 14.026 | 22.182 |

Thus DIRECT12 and PREFIX19 agree on every declared physical coordinate.

---

## 3. Physical observer partitions

The induced partitions are

\[
\mathcal P_{\rm ALM}
=
\{\{D,P\},\{N\}\},
\]

\[
\mathcal P_{\rm reg}
=
\{\{D,P,N\}\},
\]

\[
\mathcal P_{\rm DSP}
=
\{\{D,P,N\}\},
\]

and

\[
\mathcal P_{F_{\max}}
=
\mathcal P_{\rm delay}
=
\mathcal P_{\rm logicdepth}
=
\mathcal P_{\rm celldelay}
=
\mathcal P_{\rm routedelay}
=
\{\{D,P\},\{N\}\}.
\]

Hence the joint measured physical-profile partition is

\[
\boxed{
\mathcal P_{\rm joint}^{\rm phys}
=
\{\{D,P\},\{N\}\}.
}
\]

The DIRECT12/PREFIX19 physical visibility vector is

\[
\boxed{
V_{\rm phys}(D,P)
=
(0,0,0,0,0,0,0,0).
}
\]

---

## 4. Theorem H19-16.1 — measured physical quotient

For the frozen H19-LAB-01 Cyclone-V experiment, the declared joint physical
observer induces exactly two presentation classes:

\[
\boxed{
[D]_{\rm phys}
=
[P]_{\rm phys}
\ne
[N]_{\rm phys}.
}
\]

Equivalently,

\[
\boxed{
\mathcal F/{\sim_{\rm joint}^{\rm phys}}
=
\{\{DIRECT12,PREFIX19\},\{NIELSEN12\}\}.
}
\]

This is an experimental theorem relative to the declared target, tool,
constraints and report precision.

It is not a claim that the complete Quartus implementation databases of
DIRECT12 and PREFIX19 are bit-for-bit identical.

---

## 5. Theorem H19-16.2 — complete hiding of the D/P distinction under the declared physical atlas

The pair DIRECT12/PREFIX19 is distinguished earlier in the open Yosys flow
after ABC-fast by total generic cell count:

\[
60374\ne60383.
\]

Nevertheless every declared H19-LAB-01 physical coordinate agrees:

\[
10627=10627,
\]

\[
69=69,
\]

\[
48=48,
\]

\[
28.52=28.52,
\]

\[
34.827=34.827,
\]

\[
30=30,
\]

\[
13.556=13.556,
\]

\[
21.270=21.270.
\]

Therefore the earlier observable distinction is completely hidden by the
declared physical profile:

\[
\boxed{
\nu_{\rm ABC,celltot}(D,P)=1,
\qquad
\nu_{\rm phys,joint}(D,P)=0.
}
\]

This is an observer-relative re-coarsening event.

No statement is made that a full compiler or physical state first merged and
then split or vice versa.

---

## 6. First compiler-to-physical partition trajectory

For the cell-oriented open-flow observer, H19-12 had

\[
\{\{D,P\},\{N\}\}
\to
\{\{D,P\},\{N\}\}
\to
\{\{D\},\{P\},\{N\}\}
\]

from post-proc through post-techmap to ABC-fast.

The physical joint measured profile now adds

\[
\boxed{
\{\{D,P\},\{N\}\}
}
\]

at the Cyclone-V endpoint.

Thus one measured presentation-partition trajectory is

\[
\boxed{
\{\{D,P\},\{N\}\}
\to
\{\{D,P\},\{N\}\}
\to
\{\{D\},\{P\},\{N\}\}
\to
\{\{D,P\},\{N\}\}.
}
\]

The final arrow is not a refinement-order law. It crosses from a generic
Yosys cell observer to a different joint physical observer under Quartus
technology mapping.

Its meaning is empirical:

> the D/P distinction visible after generic Boolean optimization is not visible
> in any of the eight predeclared Cyclone-V summary coordinates.

---

## 7. NIELSEN12 remains physically separated

Relative to DIRECT12/PREFIX19, NIELSEN12 requires

\[
12017-10627=1390
\]

additional ALMs, approximately

\[
13.1\%
\]

more.

Its measured Fmax is lower:

\[
27.50\text{ MHz}
\quad\text{versus}\quad
28.52\text{ MHz},
\]

approximately

\[
3.6\%
\]

lower.

Its worst-path data delay is

\[
36.212\text{ ns}
\]

versus

\[
34.827\text{ ns},
\]

approximately

\[
4.0\%
\]

higher.

Its worst path also contains one additional logic level:

\[
31\text{ versus }30.
\]

The delay decomposition is likewise separated:

\[
14.026>13.556
\]

for cell delay, and

\[
22.182>21.270
\]

for routing delay.

Thus the physical quotient does not collapse the entire E0 family. It
selectively merges DIRECT12 and PREFIX19 while preserving NIELSEN12 as a
separate measured class.

---

## 8. Physical latent-gap profile

Using the finest measured joint physical profile as the reference partition,

\[
\mathcal P_{\rm joint}^{\rm phys}
=
\{\{D,P\},\{N\}\},
\]

the indistinguishable-pair count is

\[
Q(\mathcal P_{\rm joint}^{\rm phys})=1.
\]

Therefore

\[
L_{\rm profile}(O_{\rm ALM})=0,
\]

\[
L_{\rm profile}(O_{\rm reg})=2,
\]

\[
L_{\rm profile}(O_{\rm DSP})=2,
\]

and

\[
L_{\rm profile}(O)=0
\]

for each of

\[
O_{F_{\max}},
O_{\rm delay},
O_{\rm logicdepth},
O_{\rm celldelay},
O_{\rm routedelay}.
\]

Hence register count and DSP count are strictly too coarse to recover the
two-class physical quotient, while ALM and each timing/depth coordinate recover
it individually.

---

## 9. Interpretation

The strongest finite conclusion is not that DIRECT12 is "better" or PREFIX19
is "better".

The conclusion is

\[
\boxed{
DIRECT12
\sim_{\rm phys}^{\rm measured}
PREFIX19
}
\]

under the complete declared Cyclone-V summary profile, whereas

\[
\boxed{
NIELSEN12
\not\sim_{\rm phys}^{\rm measured}
DIRECT12.
}
\]

This is a concrete example in which different mathematical presentations of
the same E0 task survive compiler layers differently, yet two of them become
indistinguishable again under the final measured technology-specific profile.

---

## 10. Claim boundary

This result is conditional on:

- the H18 restricted-12 E0 contract;
- the frozen H19 generators;
- Quartus II 13.1;
- Cyclone V 5CEFA7F23C6;
- the frozen timing protocol;
- the eight declared report coordinates;
- the finite report precision.

H19 does not claim:

- complete routed-state identity of D and P;
- cross-tool invariance;
- cross-technology invariance;
- a Boolean circuit lower bound;
- a universal compiler quotient theorem.

---

## 11. Publication significance

H19-16 closes the first genuinely H19-specific physical gate requested by the
hostile prior-art audit:

\[
\boxed{
\text{controlled E0 family}
+
\text{compiler partition trajectory}
+
\text{technology-specific physical quotient}.
}
\]

The novelty threshold is now materially stronger than after H19-14, because
the result is no longer only elementary observer/order formalism: it includes a
predeclared, reproducible FPGA measurement in which the presentation partition
changes again at physical realization.

A publication candidate is now justified **after**:

1. preservation of the raw summary/atlas artifacts in the repository;
2. one reproducibility rerun or report-hash capture;
3. preferably a second-tool or second-technology replication before making
   any persistence claim.

---

## 12. Next target

The immediate next step is artifact preservation:

- commit H19_LAB01_CYCLONEV_SUMMARY.csv;
- commit H19_LAB01_PHYSICAL_PARTITIONS.csv;
- commit H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md;
- preserve a compact provenance/hash manifest for the three Quartus report
  directories.

After that, the strongest next scientific target is a second technology chart
using the identical presentation family.
