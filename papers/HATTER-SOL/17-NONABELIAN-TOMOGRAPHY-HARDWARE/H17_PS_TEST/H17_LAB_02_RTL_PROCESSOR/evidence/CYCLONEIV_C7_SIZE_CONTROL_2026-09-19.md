# H17-LAB-02 — Cyclone IV E C7 size-control experiment (2026-09-19)

## Purpose

Control the effect of device size independently of speed grade.

Same RTL, same generated closure-aware robust8 engine, same ROM-free repair network, same 100 MHz reference constraint, same Cyclone IV E family, same speed grade C7:

- EP4CE22F17C7 — 22,320 LE
- EP4CE115F29C7 — 114,480 LE

The earlier attempted EP4CE115F29C6 control is invalid because that part number is not supported; the correct equal-speed comparison is therefore 22K C7 versus 115K C7.

## Measured slow-corner critical paths

Delay model: Slow 1200 mV, 85 C.

| Metric | EP4CE22F17C7 | EP4CE115F29C7 |
|---|---:|---:|
| Data delay | 47.404 ns | 47.249 ns |
| Logic levels | 68 | 65 |
| Cell delay | 16.736 ns | 17.092 ns |
| uTco | 0.232 ns | 0.232 ns |
| Routing delay | 30.448 ns | 29.941 ns |
| Routing share | 64% | 63% |
| Setup slack at 100 MHz | -37.040 ns | -36.926 ns |
| Clock skew | 0.346 ns | 0.305 ns |

For the 22K C7 build, TimeQuest reports Fmax = 21.26 MHz.

The two C7 implementations differ in worst-path data delay by only 0.155 ns, about 0.33%. The large device reduces routing delay by only about 0.507 ns (about 1.7%) while the selected critical path has three fewer logic levels. The smaller device's critical path has slightly lower summed cell delay, so the effects nearly cancel.

## 22K placement/routing observations

EP4CE22F17C7 uses 19,534 / 22,320 logic elements (88%) and 132 registers. Despite the high LE utilization, the fitter reports estimated interconnect usage of only 31% average and 40% peak. Therefore 88% LE occupancy must not be interpreted as equivalent to routing congestion.

Quartus reports that Auto Fit was used and fitter optimizations were skipped to reduce compilation time. The comparison is therefore a baseline auto-fit comparison, not an exhaustive seed/effort study.

## Interpretation

The equal-speed-grade experiment does **not** support the simple hypothesis that the 22K timing limit is primarily caused by lack of free placement area.

At C7, increasing device capacity from 22,320 to 114,480 LE changes the measured critical delay by only about 0.33%. Routing remains roughly 30 ns and around two-thirds of the critical delay on both devices.

The earlier C6-versus-C7 difference must therefore not be attributed mainly to device size. Speed grade and fitter-selected path/mapping are important confounders.

The stable architectural observation is instead:

- the design has a very deep single-cycle combinational path (about 65–68 logic levels);
- routing contributes about 63–64% of the slow-corner data-path delay;
- merely moving the same RTL to a much larger Cyclone IV E device does not materially shorten that path under default Auto Fit.

## Next experiment

Before RTL optimization, run a small seed/fit-effort sweep on both C7 devices, or move unchanged RTL to a modern LUT6-class FPGA. This separates fitter randomness / placement effort from architectural differences.

