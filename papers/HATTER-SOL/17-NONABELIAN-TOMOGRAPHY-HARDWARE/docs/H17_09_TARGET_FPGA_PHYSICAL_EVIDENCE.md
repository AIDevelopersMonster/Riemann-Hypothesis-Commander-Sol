# H17-09 - Target-FPGA physical evidence

Date: 19 September 2026.

## Scope

H17-08 established a technology-independent Boolean result: closure-aware classification nearly halves generic synthesized logic. H17-09 adds target-specific synthesis, place-and-route, static timing, and the boundary between functional and timing simulation.

Four claims must remain separate: functional correctness, synthesizability, physical place-and-route, and timing closure. The experiments establish the first three for the tested targets. They do not establish 100 MHz timing closure.

## Mathematical object carried into hardware

For G=PSL(2,7), |G|=168. The processor acts on simultaneous-conjugacy orbits of generating ordered pairs. There are 19,152 generating ordered pairs and 114 generating orbits.

For every group word w,

w(gAg^-1,gBg^-1) = g w(A,B) g^-1,

so C(w(A,B)) is an orbit invariant.

The robust observer is

F(A,B) = (C(AAB), C(Abb), C(AAAB), C(Abbb), C(AABAb), C(AAbAb), C(ABABB), C(ABaBB)).

Eight three-bit class codes give the 24-bit hardware fingerprint. Its certified metric is coordinate Hamming distance on eight class coordinates, not binary Hamming distance on 24 serialized bits.

The exact certificate gives d_gen/gen=2 and d_gen/non=2. Therefore one coordinate can be reconstructed when its erased location is known. This is not arbitrary unknown-substitution correction.

## RTL architecture

The registered H17-LAB-02 core contains two raw PSL membership tests, the H17-07 exact 14-composition shared word DAG, eight member-class-only observers, and the 306-node ROM-free known-erasure repair network.

The closure theorem

A,B in PSL(2,7) => w(A,B) in PSL(2,7)

is directly responsible for the closure-aware hardware reduction: derived words require class determination but not eight repeated raw membership proofs.

## Cyclone IV E baseline: EP4CE22F17C6

Quartus II 13.1 successfully synthesized, fitted, assembled, and timed the processor.

- 19,540 / 22,320 logic elements = 88%
- 132 registers
- 134 / 154 package pins
- no inferred memory
- Fmax, slow 85 C: 24.52 MHz
- worst data delay: 41.082 ns
- logic levels: 65
- cell delay: 15.017 ns (36%)
- routing delay: 25.873 ns (62%)
- setup slack at 100 MHz: -30.782 ns
- hold slack: +0.343 ns

The design is physically placeable and routable, but its present one-cycle architecture does not close at 100 MHz.

A matched slow-corner Quartus Verilog/SDF pair was also simulated in ModelSim at 20 MHz. SDF backannotation succeeded and the canonical transaction passed:

raw=8d256a, observed=ed256a, repaired=8d256a, status=2.

This is one physical/timing sanity witness. It is not a replacement for exhaustive RTL/certificate verification.

## Equal-speed-grade capacity control

The same RTL was fitted to two Cyclone IV E C7 devices:

| target | nominal size | data delay | levels | cell | routing | Fmax |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EP4CE22F17C7 | 22K LE | 47.404 ns | 68 | 16.736 ns | 30.448 ns | 21.26 MHz |
| EP4CE115F29C7 | 115K LE | 47.249 ns | 65 | 17.092 ns | 29.941 ns | about 21 MHz |

The total delay changes by only 0.155 ns, about 0.33%. Routing changes by about 0.507 ns. Thus the equal-C7 experiment does not support the simple hypothesis that the 22K target is slow mainly because it is 88% full. Logic occupancy and routing congestion are not the same quantity.

## Cyclone V E: 5CEFA7F23C6

The same RTL was compiled without disabling automatic architectural inference.

- 7,941 / 56,480 ALMs = 14%
- 132 registers
- 40 / 156 DSP blocks = about 26%
- 134 / 240 package pins
- average interconnect use about 5-6%
- Fmax, slow 1.1 V 85 C: 27.85 MHz
- worst data delay: 35.694 ns
- logic levels: 34
- cell delay: 12.726 ns (35%)
- routing delay: 22.969 ns (64%)
- setup slack at 100 MHz: -25.908 ns
- hold slack: +0.374 ns

Relative to the EP4CE22F17C7 control, selected-path Fmax improves by about 31%, data delay falls about 24.7%, cell delay about 24%, routing delay about 24.6%, and logic levels fall from 68 to 34.

This is intentionally a platform-level comparison. Quartus inferred 40 DSP blocks; those resources are part of the normal Cyclone V mapping of unchanged RTL. The result must not be presented as a pure ALM-versus-LE comparison.

## Critical-path interpretation

Routing remains about 62-64% of selected critical-path delay across the tested targets. Cyclone V reduces both logic depth and absolute routing delay, but the qualitative bottleneck remains a long single-cycle combinational transaction.

The measurements point to architecture, rather than nominal same-generation capacity alone, as the main next timing lever. Registering boundaries between word evaluation, classification, and repair, or moving to a multi-cycle/microcoded processor, are natural future experiments. They change latency and are outside this unchanged-RTL benchmark.

## Simulation boundary

Cyclone IV in this tool flow supports a post-fit Verilog/SDF timing waveform. For Cyclone V under Quartus II 13.1, the EDA Netlist Writer generated the post-fit .vo but no .sdo. Therefore the Cyclone V physical-delay evidence is TimeQuest, not an SDF-backed ModelSim waveform.

The 35.694 ns Cyclone V path must not be represented as if it had been observed in the functional waveform.

## Bounded conclusion

H17-LAB-02 is a physically realizable FPGA processor. A five-times-larger same-generation Cyclone IV device at the same C7 speed grade does not materially shorten its critical path. Cyclone V gives a substantial platform-level improvement to unchanged RTL, but 100 MHz remains unclosed.

No claim is made about globally optimal FPGA implementation, minimum achievable latency, power, or timing after retiming/pipelining.
