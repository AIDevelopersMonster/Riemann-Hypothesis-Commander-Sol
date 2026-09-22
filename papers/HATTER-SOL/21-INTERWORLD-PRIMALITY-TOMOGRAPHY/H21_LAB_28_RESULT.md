# HATTER-SOL-21 · H21-LAB-28 RESULT

Status: **DEVICE-SPECIFIC CYCLONE V RESULT / PUBLICATION-GATE TRIGGER SATISFIED**

Date: 2026-09-22

Target:

\[
\boxed{\text{Cyclone V 5CEFA7F23C6}}
\]

Toolchain:

\[
\boxed{\text{Quartus II 13.1.0 Build 162}}
\]

Compared RTL:

- compiled scalar \(B=0\) Euler-Jacobi observer:
  \[
  \texttt{h21\_scalar\_pow};
  \]

- uncompiled quadratic \(B=0\) observer:
  \[
  \texttt{h21\_quad\_pow\_b0}.
  \]

Both are the unchanged matched LAB-27 cores and use the same sequential base
modular multiplier.

## 1. Fit result

Both designs completed Analysis & Synthesis, Fitter, Assembler and TimeQuest.

\[
\boxed{\text{scalar FIT}}
\]

\[
\boxed{\text{quadratic FIT}}
\]

No DSP blocks were used by either design.

## 2. Device utilization

| metric | scalar | quadratic | quadratic/scalar |
|---|---:|---:|---:|
| ALMs | 215 | 328 | 1.5256x |
| registers | 251 | 455 | 1.8127x |
| DSP blocks | 0 | 0 | — |

Therefore the compiled scalar observer uses

\[
\boxed{34.45\%}
\]

fewer ALMs and

\[
\boxed{44.84\%}
\]

fewer registers than the matched quadratic datapath.

## 3. Fmax

Slow 1100 mV, 85 C:

\[
F_{\max,\mathrm{scalar}}
=
\boxed{157.33\ \mathrm{MHz}},
\]

\[
F_{\max,\mathrm{quad}}
=
\boxed{123.20\ \mathrm{MHz}}.
\]

Hence

\[
\boxed{
\frac{F_{\max,\mathrm{scalar}}}
{F_{\max,\mathrm{quad}}}
=
1.2770
}
\]

so the scalar mapping has about

\[
\boxed{27.70\%}
\]

higher Fmax.

At the declared 100 MHz constraint, both designs have positive worst-case
setup slack:

\[
\boxed{3.644\ \mathrm{ns}}
\]

for scalar and

\[
\boxed{1.883\ \mathrm{ns}}
\]

for quadratic at Slow 1100 mV, 85 C.

## 4. Mean latency

Using the authoritative LAB-27 mean cycle counts

\[
\bar C_{\mathrm{scalar}}=175,
\qquad
\bar C_{\mathrm{quad}}=861,
\]

and the device Fmax values:

\[
T_{\mathrm{scalar}}
=
\frac{175}{157.33\ \mathrm{MHz}}
=
\boxed{1.112312\ \mu s},
\]

\[
T_{\mathrm{quad}}
=
\frac{861}{123.20\ \mathrm{MHz}}
=
\boxed{6.988636\ \mu s}.
\]

Thus

\[
\boxed{
\frac{T_{\mathrm{quad}}}
{T_{\mathrm{scalar}}}
=
6.2830
}
\]

and the compiled scalar observer reduces mean latency by

\[
\boxed{84.08\%}.
\]

## 5. Area-latency product

Using fitted ALMs and Fmax-derived mean latency:

\[
A T_{\mathrm{scalar}}
=
215\times1.112312
=
\boxed{239.147016\ \mathrm{ALM}\cdot\mu s},
\]

\[
A T_{\mathrm{quad}}
=
328\times6.988636
=
\boxed{2292.272727\ \mathrm{ALM}\cdot\mu s}.
\]

Therefore

\[
\boxed{
\frac{AT_{\mathrm{quad}}}
{AT_{\mathrm{scalar}}}
=
9.5852
}
\]

or equivalently the compiled scalar path reduces the matched ALM-latency
product by

\[
\boxed{89.57\%}.
\]

## 6. End-to-end evidence chain

H21 now has the complete experimentally measured chain

\[
\boxed{
B=0\text{ descriptor}
\to
\text{exact algebraic collapse}
\to
\text{semantics-preserving compiler lowering}
\to
\text{bit-exact RTL equivalence}
\to
\text{generic synthesis advantage}
\to
\text{Cyclone V device advantage}.
}
\]

The strongest measured device-specific statement is:

\[
\boxed{
\text{for the declared matched 12-bit sequential architecture on Cyclone V,
the compiled scalar }B=0\text{ observer uses fewer ALMs/registers, reaches
higher Fmax, and has }9.5852\times\text{ lower ALM-latency product.}
}
\]

## 7. Important limitations

This experiment is a matched core comparison, not a board-level timing
sign-off.

Quartus reports:

- no exact physical pin assignments;
- the design is not fully constrained for all setup/hold requirements;
- Auto Fit was used and timing optimizations were skipped to reduce compile
  time.

The internal clock-to-clock paths used for the Fmax comparison are constrained
and both designs use the same flow.

Therefore safe claims are:

- device-specific logic utilization;
- internal clock-domain Fmax comparison;
- Fmax-derived matched latency;
- ALM-latency comparison.

Unsafe claims remain:

- board-level maximum frequency;
- power or energy advantage;
- universal FPGA ratios;
- first-ever hardware architecture.

## 8. Publication consequence

The device-specific condition in PUBLICATION_GATE Gate E is satisfied.

\[
\boxed{\text{LAB-28 ENGINEERING TRIGGER: PASS}}
\]

This is sufficient to cross the H21 architecture-paper publication threshold
for the narrow semantics-preserving compiler-lowering claim, subject to final
bibliography and claim-discipline audit.
