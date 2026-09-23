# H19-LAB-01 · Physical Visibility Atlas

Status: AUTO-GENERATED FROM MATCHED CYCLONE-V REPORTS

Target: 5CEFA7F23C6
Tool: Quartus II 13.1
Reference constraint: 100 MHz
Timing protocol: Slow 1100 mV / 85 C

Presentations: D = DIRECT12; P = PREFIX19; N = NIELSEN12.

All equality and partition statements below are at the finite precision printed by the frozen Quartus reporting flow.

## 1. Matched physical profile

| mode | ALM | registers | DSP | Fmax MHz | data delay ns | logic levels | cell ns | routing ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| D | 10,627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| P | 10,627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| N | 12,017 | 69 | 48 | 27.5 | 36.212 | 31 | 14.026 | 22.182 |

## 2. Physical observer partitions

| observer | partition | classes | indistinguishable pairs | profile-relative latent gap | D/P visible |
| --- | --- | ---: | ---: | ---: | ---: |
| ALM | {{D,P},{N}} | 2 | 1 | 0 | 0 |
| Registers | {{D,P,N}} | 1 | 3 | 2 | 0 |
| DSP | {{D,P,N}} | 1 | 3 | 2 | 0 |
| Fmax_MHz | {{D,P},{N}} | 2 | 1 | 0 | 0 |
| DataDelay_ns | {{D,P},{N}} | 2 | 1 | 0 | 0 |
| LogicLevels | {{D,P},{N}} | 2 | 1 | 0 | 0 |
| Cell_ns | {{D,P},{N}} | 2 | 1 | 0 | 0 |
| Routing_ns | {{D,P},{N}} | 2 | 1 | 0 | 0 |

## 3. Finest measured joint physical profile

Available coordinates: ALM, Registers, DSP, Fmax_MHz, DataDelay_ns, LogicLevels, Cell_ns, Routing_ns.

Joint-profile partition: {{D,P},{N}}.

Joint-profile indistinguishable-pair count: 1.

This joint profile is the finest measured observer in this laboratory. It is not identified with the complete routed FPGA implementation state.

ProfileRelativeLatentGap means Q(single-coordinate partition) minus Q(joint measured-profile partition), not a claim about hidden distinctions in the full Quartus database.

## 4. DIRECT12 / PREFIX19 physical visibility vector

Coordinate order: ALM, Registers, DSP, Fmax_MHz, DataDelay_ns, LogicLevels, Cell_ns, Routing_ns.

Visibility vector: (0,0,0,0,0,0,0,0).

A 1 means the printed Quartus values differ; a 0 means they coincide at the frozen report precision.

## 5. Interpretation rule

Do not collapse this atlas to one scalar winner. ALM, DSP, register count, Fmax, logic depth, cell delay and routing delay are different physical observers and may induce different presentation partitions.

The scientifically relevant object is the family O_phys -> P_phys(O_phys), together with the joint measured-profile partition.

## 6. Publication boundary

This report is a technology/tool/constraint-relative realization witness. It is not a Boolean circuit lower bound, not a technology-independent mathematical invariant, and not evidence that a coordinate ordering persists on another FPGA family.

The next cross-technology test should repeat the identical presentation family and observer definitions on a second target before any persistence claim is made.
