# H17-LAB-02 - Model excellent-student report
## Non-Abelian tomography as an FPGA processor

### Aim

The experiment traces a certified finite-group observer from its mathematical quotient to an actual placed-and-routed FPGA circuit and determines which claims survive each engineering stage.

The encoded object is not an arbitrary 48-bit pair A,B. The admissible mathematical states are simultaneous-conjugacy orbits of generating pairs in PSL(2,7), of which there are 114.

### Orbit invariant

If (A,B)~(gAg^-1,gBg^-1), then for every word w,

w(gAg^-1,gBg^-1)=g w(A,B) g^-1.

Therefore the conjugacy class of w(A,B) depends only on the orbit. The processor evaluates:

F(A,B)=(C(AAB),C(Abb),C(AAAB),C(Abbb),C(AABAb),C(AAbAb),C(ABABB),C(ABaBB)).

Each class is encoded in three bits, giving a 24-bit hardware fingerprint.

### Known-erasure repair

The certified coordinate-Hamming distances are d_gen/gen=2 and d_gen/non=2. If one erased coordinate location is known, two admissible fingerprints cannot become identical after deleting that same coordinate. Hence the missing coordinate is uniquely reconstructible on the certified domain.

This is not a guarantee for an arbitrary unknown wrong coordinate.

### Hardware structure

Closure gives A,B in PSL(2,7) => w(A,B) in PSL(2,7). Thus membership is tested for A and B, while the eight derived members need only class determination. The eight words share an exact minimum 14-composition DAG with maximum composition depth three. The repair block is ROM-free and implements the certified decision network rather than a table of all 114 fingerprints.

### Functional witness

A=5e3b88, B=7ecc11, mode=1 gives raw=8d256a, observed=ed256a, repaired=8d256a, status=2.

The RTL waveform verifies the expected functional transaction. I do not infer propagation delay from it because RTL event simulation has no fitted FPGA routing delay.

### Cyclone IV EP4CE22F17C6

The processor uses 19,540 / 22,320 LE (88%) and 132 registers. Slow-corner TimeQuest gives:

T_data=41.082 ns, T_cell=15.017 ns, T_route=25.873 ns, Fmax=24.52 MHz.

The fractions are about 36.6% cell and 63.0% routing. The design is successfully placed and routed but does not satisfy the requested 100 MHz clock.

A 20 MHz post-fit ModelSim run with SDF passes the canonical transaction. This is a timing-aware physical sanity check; exhaustive correctness remains a separate RTL/certificate result.

### Capacity experiment

At equal C7 speed grade:

T_22K=47.404 ns and T_115K=47.249 ns.

The reduction is 0.155/47.404, about 0.33%. Thus the much larger Cyclone IV gives essentially the same critical-path delay for unchanged RTL. This experiment does not support high 22K occupancy as the dominant cause of the long path.

### Cyclone V

On 5CEFA7F23C6, Quartus maps the same RTL to 7,941 / 56,480 ALMs, 132 registers, and 40 / 156 DSP blocks.

TimeQuest gives T_data=35.694 ns, T_cell=12.726 ns, T_route=22.969 ns, 34 logic levels, and Fmax=27.85 MHz.

Relative to EP4CE22F17C7, data delay falls about 24.7% and Fmax rises about 31%; selected critical-path logic depth falls from 68 to 34 levels.

This is a complete target-platform comparison, not an ALM-only comparison, because Quartus inferred 40 DSP blocks. Those DSPs are legitimate resources of the target while the RTL is unchanged.

### Why no Cyclone V SDF waveform

Quartus II 13.1 generates the Cyclone V post-fit Verilog netlist but no SDF timing file for this family. Therefore a Cyclone V waveform without SDF is functional, not a visualization of the measured 35.694 ns path. I use TimeQuest as the physical timing evidence for Cyclone V.

### Conclusion

The demonstrated chain is:

orbit invariant -> robust code -> closure-aware RTL -> FPGA place-and-route -> STA.

Nominal same-generation device capacity alone did not cure the long one-cycle path. Cyclone V improves unchanged RTL substantially, but routing still contributes about 64% of the selected critical path and 100 MHz remains unclosed.

My next timing experiment would introduce registered or multi-cycle boundaries between expensive stages, for example between the word/class engine and repair network. That would be a new architecture experiment because it changes latency and potentially throughput.
