# H19-LAB-02 Gowin synthesis summary

Target: `GW5A-25A / GW5A-LV25MG121NC1/I0`

| Mode | Synthesis | Logic | Capacity | Logic % | LUT | ALU | Registers | DSP | EX3791 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| direct12 | PASS | 19376 | 23040 | 84,10 | 18882 | 494 | 69 | 28 | 4 |
| prefix19 | PASS | 19376 | 23040 | 84,10 | 18882 | 494 | 69 | 28 | 4 |
| nielsen12 | PASS | 21221 | 23040 | 92,11 | 20729 | 492 | 69 | 28 | 4 |

Measured synthesis-resource quotient: `{{D,P},{N}}`

NIELSEN12 vs DIRECT12/PREFIX19: Logic +1845 (+9,52%), LUT +1847 (+9,78%), ALU -2 (-0,40%).

Claim boundary: this quotient is for the declared Gowin synthesis resource observer only. It is not a netlist-identity claim and not yet a post-P&R physical quotient.

The four EX3791 warnings per mode arise from the frozen H17-08 helper RTL narrowing reduced integer values into 3-bit mod-7 results; the RTL is intentionally unchanged from the cross-tool experiment.
