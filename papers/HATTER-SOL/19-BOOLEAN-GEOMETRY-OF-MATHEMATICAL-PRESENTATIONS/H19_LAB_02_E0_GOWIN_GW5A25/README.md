# H19-LAB-02 · E0 cross-technology replication on Gowin GW5A-25A

Status: OPEN / SYNTHESIS CALIBRATION

Purpose: repeat the frozen H19 E0 presentation family on a second FPGA vendor/toolchain without changing the mathematical semantics, decision DAG, external contract, or presentation definitions.

Frozen family:

- DIRECT12
- PREFIX19
- NIELSEN12

Target:

- board: Sipeed Tang Primer 25K
- device: GW5A-25A
- full part number: GW5A-LV25MG121NC1/I0
- tool: Gowin Education IDE 1.9.9Beta-4
- CLI: gw_sh.exe

The first gate is intentionally synthesis-only. No physical P&R/timing claim is made until all three variants pass the same synthesis flow and the Gowin report format is inspected.

Initial command:

~~~powershell
.\tools\run_gowin_syn.ps1 -Mode direct12
~~~

Heavy generated/tool output directories are ignored. Compact summaries and provenance will be committed after the report format is frozen.


## Synthesis gate — CLOSED / MEASURED

GowinSynthesis 1.9.9Beta-4 on `GW5A-LV25MG121NC1/I0` completed successfully for all three frozen H19 E0 presentations.

| Mode | Logic | Capacity | Logic % | LUT | ALU | Registers | DSP | EX3791 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DIRECT12 | 19376 | 23040 | 84.10 | 18882 | 494 | 69 | 28 | 4 |
| PREFIX19 | 19376 | 23040 | 84.10 | 18882 | 494 | 69 | 28 | 4 |
| NIELSEN12 | 21221 | 23040 | 92.11 | 20729 | 492 | 69 | 28 | 4 |

Measured synthesis-resource quotient:

```
{{DIRECT12,PREFIX19},{NIELSEN12}}
```

NIELSEN12 relative to DIRECT12/PREFIX19:

- Logic: +1845 (+9.52%)
- LUT: +1847 (+9.78%)
- ALU: -2 (-0.40%)
- Registers: equal (69)
- DSP: equal (28)

Claim boundary: this is a **Gowin synthesis-resource observer** result. It is not a synthesized-netlist identity claim and it is not yet a post-place-and-route physical quotient.

The four EX3791 warnings per mode arise from the frozen H17-08 helper RTL narrowing already reduced mod-7 integer values into 3-bit results. The RTL is intentionally unchanged so the cross-tool experiment remains matched to the earlier H19/Cyclone-V evidence.

Next gate: Gowin place-and-route calibration, beginning with DIRECT12 only.


## Post-P&R physical gate — CLOSED / MEASURED

All three frozen H19 E0 presentations completed placement, routing, timing analysis, and bitstream generation on `GW5A-LV25MG121NC1/I0` under the same explicit SDC clock contract:

```tcl
create_clock -name clk -period 10.000 [get_ports {clk}]
```

The physical I/O fit required exposing the MSPI and READY dual-purpose pins as GPIO. The RTL, mathematical presentation, decision DAG, external contract, and 100 MHz timing target were not changed.

| Mode | P&R | 100 MHz | Logic | LUT | ALU | Reg | CLS | MULT12X12 | Actual Fmax | Levels | setup TNS | setup EP | hold TNS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DIRECT12 | PASS | FAIL | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 MHz | 49 | -644.501 ns | 13 | 0.000 ns |
| PREFIX19 | PASS | FAIL | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 MHz | 49 | -644.501 ns | 13 | 0.000 ns |
| NIELSEN12 | PASS | FAIL | 21448 | 20729 | 719 | 69 | 10941 | 28 | 16.599 MHz | 49 | -628.206 ns | 13 | 0.000 ns |

Measured Gowin post-P&R physical quotient:

```
{{DIRECT12,PREFIX19},{NIELSEN12}}
```

Thus the declared physical-profile observer again merges DIRECT12 with PREFIX19 while separating NIELSEN12. This reproduces the same partition previously observed on Cyclone V.

Important claim boundary: this is equality of the declared measured post-P&R profile vector, not a claim that DIRECT12 and PREFIX19 have identical routed netlists, placements, bitstreams, or full physical state.

The 100 MHz timing constraint is not met by any mode. P&R PASS means that placement, routing, timing analysis, and bitstream generation completed successfully; timing closure is reported separately.

NIELSEN12 is physically larger than DIRECT12/PREFIX19 but has a slightly higher measured post-route Fmax in this Gowin run. Therefore the physical observer is genuinely multidimensional and should not be reduced to a single scalar notion of "better" or "worse".

Generate the compact family evidence with:

~~~powershell
.\tools\summarize_all_gowin_pnr.ps1
~~~
