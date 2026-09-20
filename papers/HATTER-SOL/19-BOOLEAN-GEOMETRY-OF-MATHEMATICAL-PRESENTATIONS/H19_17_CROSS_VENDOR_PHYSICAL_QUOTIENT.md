# H19-17 · Cross-Vendor Replication of the Measured Physical Quotient

Status: **CROSS-TECHNOLOGY PHYSICAL RESULT / CLOSED FOR THE TWO DECLARED LABORATORIES**

Date: 20 September 2026.

## 1. Purpose

H19-16 established a technology-specific physical quotient for the frozen E0 family

[
mathcal F={D,P,N}
=
{DIRECT12,PREFIX19,NIELSEN12}
]

on Cyclone V under Quartus II 13.1.

H19-LAB-02 now repeats the same mathematical presentation family on a second FPGA vendor and toolchain:

- Gowin GW5A-25A / GW5A-LV25MG121NC1/I0;
- Gowin Education IDE 1.9.9Beta-4;
- identical frozen E0 semantics;
- identical generated 305-node decision DAG;
- identical external contract;
- identical 100 MHz reference clock contract;
- unchanged source presentation definitions.

The question is deliberately narrow:

[
oxed{
	ext{Does the observer-induced physical partition of }mathcal F
	ext{ repeat on a second FPGA technology?}
}
]

No claim of universal technology independence is made.

## 2. Cyclone-V physical quotient

For H19-LAB-01 the measured profile was:

| presentation | ALM | registers | DSP | Fmax MHz | data delay ns | logic levels | cell ns | routing ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| PREFIX19 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| NIELSEN12 | 12017 | 69 | 48 | 27.50 | 36.212 | 31 | 14.026 | 22.182 |

Therefore the joint measured physical-profile partition was

[
oxed{
mathcal P_{m CV}^{m joint}
=
{{D,P},{N}}.
}
]

DIRECT12 and PREFIX19 agreed on every declared Cyclone-V physical coordinate.

## 3. Gowin synthesis quotient

Before place-and-route, GowinSynthesis produced:

| presentation | Logic | LUT | ALU | registers | DSP |
| --- | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 19376 | 18882 | 494 | 69 | 28 |
| PREFIX19 | 19376 | 18882 | 494 | 69 | 28 |
| NIELSEN12 | 21221 | 20729 | 492 | 69 | 28 |

Thus already the second synthesis backend reproduced

[
oxed{
mathcal P_{m Gowin,syn}
=
{{D,P},{N}}.
}
]

This synthesis result is not used as a substitute for the physical result below.

## 4. Gowin post-P&R physical measurements

All three variants completed placement, routing, timing analysis and bitstream generation.

The 100 MHz timing target was not met by any variant, so P&R completion and timing closure are recorded separately.

| presentation | P&R | Logic | LUT | ALU | Reg | CLS | DSP | Fmax MHz | Levels | WNS ns | setup TNS ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| PREFIX19 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| NIELSEN12 | PASS | 21448 | 20729 | 719 | 69 | 10941 | 28 | 16.599 | 49 | -50.243 | -628.206 |

Hence

[
oxed{
mathcal P_{m GW}^{m joint}
=
{{D,P},{N}}.
}
]

Again DIRECT12 and PREFIX19 agree on every coordinate of the declared joint measured post-P&R profile.

## 5. Experimental Result H19-17.1 — replicated physical quotient

For the two frozen physical laboratories,

[
oxed{
mathcal P_{m CV}^{m joint}
=
mathcal P_{m GW}^{m joint}
=
{{D,P},{N}}.
}
]

Equivalently, the vendor-indexed measured quotient signature is

[
oxed{
mathfrak Q_{m phys}^{(2)}
=
left(
{{D,P},{N}},
{{D,P},{N}}
ight).
}
]

This is a replicated finite experimental result.

It states equality of the induced partitions, not equality of numerical FPGA resources across vendors.

## 6. DIRECT12/PREFIX19 re-coarsening is reproduced

At the generic Yosys ABC-fast stage,

[
60374
e60383,
]

so DIRECT12 and PREFIX19 are separated by the declared total-cell observer.

At both physical endpoints,

[
Dsim_{m CV}^{m joint}P
]

and

[
Dsim_{m GW}^{m joint}P.
]

Thus the observed trajectory contains a replicated re-coarsening event:

[
oxed{
{{D},{P},{N}}
longrightarrow
{{D,P},{N}}
}
]

when passing from the generic ABC-fast observer to either declared vendor-specific joint physical observer.

This arrow is observer-relative. It does not assert that a complete implementation state merged.

## 7. NIELSEN12 remains a distinct measured class

The replicated quotient is nontrivial because the physical observers do not collapse all three presentations.

On Cyclone V, NIELSEN12 uses 1390 additional ALMs, approximately 13.08% more than DIRECT12/PREFIX19, and has a lower measured Fmax.

On Gowin, NIELSEN12 uses 1820 additional post-P&R Logic units, approximately 9.27% more, while its measured Fmax is slightly higher:

[
16.599	ext{ MHz}>16.276	ext{ MHz}.
]

Therefore the physical distinction is multidimensional and cannot be summarized by a universal scalar ordering of the presentations.

## 8. What replicated and what did not

The following structural fact replicated:

[
oxed{
Dsim_{m phys}^{m measured}P,qquad
N
otsim_{m phys}^{m measured}D.
}
]

The numerical direction of every physical coordinate did not replicate.

For example, relative timing behavior of NIELSEN12 differs between the two technologies.

Therefore H19 may claim **partition replication** for the two declared physical observers, but not numerical resource-ratio invariance and not a technology-independent performance ordering.

## 9. Relation to the compiler partition trajectory

The measured family trajectory can now be written as

[
oxed{
{{D,P},{N}}_{m proc}
	o
{{D,P},{N}}_{m techmap}
	o
{{D},{P},{N}}_{m ABC}
	o
egin{cases}
{{D,P},{N}}_{m CycloneV},\
{{D,P},{N}}_{m Gowin}.
end{cases}
}
]

This is the first cross-vendor physical continuation of the H19 presentation-partition atlas.

## 10. Reproducibility

H19-LAB-01 preserves a SHA-256 provenance manifest for 33 Cyclone-V run artifacts.

H19-LAB-02 preserves a SHA-256 provenance manifest for 33 Gowin run artifacts, including:

- generated RTL;
- explicit SDC/Tcl inputs;
- saved Gowin option snapshots;
- primary transcripts;
- synthesis reports;
- P&R resource reports;
- post-route timing reports.

The manifests certify the local files byte-for-byte. They do not claim deterministic rerouting across installations or future tool versions.

## 11. Claim boundary

H19-17 does **not** claim:

- universal cross-technology invariance;
- identical routed netlists or bitstreams for DIRECT12 and PREFIX19;
- equality of full physical state;
- a technology-independent FPGA cost metric;
- a lower bound on Boolean or circuit complexity;
- that NIELSEN12 is globally worse or better.

The exact claim is:

> For the frozen E0 family and the two declared FPGA laboratories, the respective joint measured post-route physical observers induce the same two-block presentation partition ({{DIRECT12,PREFIX19},{NIELSEN12}}).

## 12. Publication consequence

H19-13 required a result that survives the removal of classical observer theory, partition-lattice language, branching-program comparisons and generic compiler-equivalence concepts.

The two-vendor replication supplies such an experimental layer:

[
oxed{
	ext{controlled mathematical presentations}
+
	ext{compiler partition dynamics}
+
	ext{replicated physical quotient}.
}
]

Accordingly, H19 has crossed the publication-candidate threshold for this finite claim set.

A manuscript should make the replicated quotient, rather than the abstract partition lattice itself, the central empirical result.
