# H18-LAB-04 — EP4CE115F29C7 matched timing evidence

Date: 19 September 2026.

Target:

- Quartus II 13.1 Web Edition
- Cyclone IV E EP4CE115F29C7
- 100 MHz SDC reference clock
- Slow 1200 mV / 85 C TimeQuest model
- one-result-cycle registered combinational architecture

## H18-LAB-04 routed critical path

The matched 115K C7 design successfully produced a routed TimeQuest timing
netlist and a full setup-path report.

Worst of the three reported setup paths:

- from \`B_q[5]\`
- to \`orbit_id[6]~reg0\`
- data delay: **46.516 ns**
- setup slack at 100 MHz: **-36.189 ns**
- logic levels: **65**
- data-path cell delay: **15.721 ns**
- data-path routing delay: **30.579 ns**

The next two reported paths are 46.513 ns and 46.485 ns.

The 100 MHz constraint is an analysis reference and is not met.

The reciprocal of the 46.516 ns selected data-path delay is approximately
21.50 MHz.  This is a derived comparison number, not a replacement for a
Quartus Fmax Summary report.

## Matched H17-LAB-02 comparison

Previously measured H17-LAB-02 on the same EP4CE115F29C7 C7 target:

- data delay: 47.249 ns
- logic levels: 65
- data-path cell delay: 17.092 ns
- data-path routing delay: 29.941 ns
- Fmax: about 21 MHz

Therefore, on the matched large device:

- H18 data delay is 0.733 ns lower, about **1.55%**;
- both selected critical paths have **65 logic levels**;
- H18 cell delay is about **8.02% lower**;
- H18 routing delay is about **2.13% higher**;
- reciprocal-delay frequency is about **1.58% higher** for H18.

This is a striking near-equality in end-to-end physical depth despite very
different mathematical presentations.

## Interpretation for H18-12

The matched experiment gives the first concrete presentation-effect timing
comparison under a common technology stack and a common one-result-cycle
discipline.

The result does **not** show that the two mathematics are hardware-equivalent.
Instead it shows that one physical coordinate -- routed one-cycle delay --
can be nearly equal while lower-level decomposition differs.

The present H18 path spends less delay in cells but more in routing.  Thus a
scalar timing result hides distinct Boolean/physical geometries.

Exact 115K H18 area/utilization must be taken from the corresponding
map/fit report before the full area-delay comparison is closed.  No 115K area
number is inferred from the earlier 22K no-fit estimate.
