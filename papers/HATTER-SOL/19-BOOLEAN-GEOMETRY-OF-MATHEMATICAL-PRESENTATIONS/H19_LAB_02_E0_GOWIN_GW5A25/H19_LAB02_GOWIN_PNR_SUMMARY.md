# H19-LAB-02 Gowin post-P&R physical summary

Target: `GW5A-25A / GW5A-LV25MG121NC1/I0`

Clock contract: `clk = 100 MHz` via `create_clock -period 10.000`.

| Mode | P&R | 100 MHz | Logic | Logic % | LUT | ALU | Reg | CLS | DSP | Fmax MHz | Levels | WNS ns | setup TNS ns | setup EP | hold TNS ns |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| direct12 | PASS | FAIL | 19628 | 85,19 | 18882 | 746 | 69 | 10150 | 28 | 16,276 | 49 | -51,440 | -644,501 | 13 | 0,000 |
| prefix19 | PASS | FAIL | 19628 | 85,19 | 18882 | 746 | 69 | 10150 | 28 | 16,276 | 49 | -51,440 | -644,501 | 13 | 0,000 |
| nielsen12 | PASS | FAIL | 21448 | 93,09 | 20729 | 719 | 69 | 10941 | 28 | 16,599 | 49 | -50,243 | -628,206 | 13 | 0,000 |

Measured post-P&R physical quotient: `{{D,P},{N}}`

Claim boundary: equality means equality of the declared measured physical-profile vector, not identity of routed netlists, placements, bitstreams, or all physical state.

All three variants completed placement, routing, timing analysis, and bitstream generation. A P&R PASS does not imply the 100 MHz constraint is met; timing status is reported separately.
