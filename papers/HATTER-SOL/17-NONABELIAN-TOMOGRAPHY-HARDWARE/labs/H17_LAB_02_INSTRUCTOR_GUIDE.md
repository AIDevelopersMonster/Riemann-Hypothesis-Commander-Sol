# H17-LAB-02 - Instructor guide
## From a finite-group theorem to placed-and-routed FPGA logic

### Purpose

The student follows one mathematical invariant through four representations:

simultaneous-conjugacy orbit -> class-valued word signature -> 24-bit resilient fingerprint -> placed FPGA circuit.

The main lesson is that functional correctness, synthesis, place-and-route, SDF timing simulation, and static timing analysis are different claims.

### Mathematical prerequisites

For G=PSL(2,7), |G|=168. There are 19,152 generating ordered pairs and 114 simultaneous-conjugacy orbits of generating pairs. For every word w,

w(gAg^-1,gBg^-1)=g w(A,B) g^-1,

so C(w(A,B)) is invariant on a simultaneous-conjugacy orbit.

The robust observer uses:

AAB, Abb, AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB.

Its certified coordinate distances are d_gen/gen=2 and d_gen/non=2. Therefore one known erased coordinate is recoverable. Do not describe this as arbitrary one-error correction.

### Architecture to identify

Students locate and explain the input registers A_q, B_q and mode_q; two raw membership blocks; the 14-composition shared word DAG; eight member-class-only blocks; raw_signature; observed_signature; the ROM-free repair network; repaired_signature; input_valid; fingerprint_valid; and status.

The H17 closure theorem is visible in hardware: once A and B are verified members of PSL(2,7), derived group words require class determination but do not require repeated raw membership tests.

### Part A - RTL waveform

Canonical transaction:

A=5e3b88
B=7ecc11
mode=1
raw=8d256a
observed=ed256a
repaired=8d256a
status=2

Required interpretation: observed is the intentionally erased/encoded signature. repaired==raw demonstrates reconstruction for this witness. The RTL waveform contains no fitted FPGA routing delay and must not be used to infer Fmax.

### Part B - Cyclone IV physical timing

EP4CE22F17C6:

- LE: 19540 / 22320 = 88%
- registers: 132
- Fmax slow 85 C: 24.52 MHz
- worst data delay: 41.082 ns
- logic levels: 65
- cell delay: 15.017 ns
- routing delay: 25.873 ns

Students calculate 15.017/41.082 and 25.873/41.082, then compare 41.082 ns with the requested 10 ns period at 100 MHz.

### Part C - SDF waveform

Cyclone IV has a post-fit ModelSim/SDF witness at 20 MHz. Students must distinguish:

RTL WLF = functional event simulation.
Post-fit WLF + SDF = timing-aware vendor-netlist simulation.
TimeQuest = static worst-case timing analysis.

The canonical SDF pass is one physical sanity witness, not exhaustive verification.

### Part D - capacity control

Equal C7:

| target | delay | levels | cell | routing |
| --- | ---: | ---: | ---: | ---: |
| EP4CE22F17C7 | 47.404 ns | 68 | 16.736 ns | 30.448 ns |
| EP4CE115F29C7 | 47.249 ns | 65 | 17.092 ns | 29.941 ns |

Question: did about five times the nominal LE capacity solve the timing problem?

Expected answer: no. The 0.155 ns change is about 0.33%. This experiment does not support capacity shortage as the dominant explanation. The conclusion is limited to this design, these devices, this fitter setup, and this speed grade.

### Part E - Cyclone V platform experiment

5CEFA7F23C6:

- 7941 / 56480 ALMs = 14%
- 132 registers
- 40 / 156 DSP blocks
- Fmax: 27.85 MHz
- worst data delay: 35.694 ns
- logic levels: 34
- cell delay: 12.726 ns
- routing delay: 22.969 ns

Students calculate the change relative to EP4CE22F17C7. They must explain that this is not a pure LUT/ALM comparison because Quartus inferred 40 DSP blocks. Those DSPs remain legitimate target resources and are retained in the primary unchanged-RTL benchmark.

### Part F - missing Cyclone V SDF

Question: why is a .vo generated but no .sdo?

Expected answer: Quartus II 13.1 does not provide gate-level timing simulation for Cyclone V in this flow. The absence of SDF is a tool/family boundary, not a failed fit. Cyclone V physical delay evidence comes from TimeQuest.

### Required report

An excellent report must connect simultaneous conjugacy to class-valued word invariants; state what the 24-bit fingerprint encodes; distinguish known erasure from unknown substitution; explain the 14-composition DAG and closure-aware classifier; distinguish RTL simulation, generic synthesis, place-and-route, SDF simulation, and STA; compute cell/routing fractions; use the equal-C7 experiment to separate capacity from speed-grade effects; state the Cyclone V DSP inference; avoid claiming 100 MHz timing closure; and propose a timing-oriented next architecture while noting that it changes latency.

### Non-claims

The laboratory does not prove a globally optimal FPGA implementation, universal superiority of one FPGA family, that high utilization can never cause congestion, that the fingerprint is cryptographic, that distance two corrects an arbitrary unknown error, or that the Cyclone V 35.694 ns delay was observed in ModelSim.
