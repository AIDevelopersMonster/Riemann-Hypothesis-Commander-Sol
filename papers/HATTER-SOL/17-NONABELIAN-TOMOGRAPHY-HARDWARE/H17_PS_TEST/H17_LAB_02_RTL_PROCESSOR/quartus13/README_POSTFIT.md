# H17-LAB-02 post-fit timing simulation

This experiment deliberately leaves all top-level pin locations unconstrained.
Quartus therefore chooses legal package pins automatically during fitting.
This is suitable for a board-free place-and-route experiment, but the resulting
pinout must NOT be programmed into an arbitrary physical board.

The flow reuses the fitted Cyclone IV E EP4CE22F17C6 database, writes a
gate-level Verilog netlist plus SDF timing data, and simulates the canonical
H17-LAB-02 vector in ModelSim-Altera at 20 MHz.

Run from H17_LAB_02_RTL_PROCESSOR:

    .\tools\run_quartus13_postfit.ps1

Expected logical result:

    raw      = 8d256a
    observed = ed256a
    repaired = 8d256a
    status   = 2

Artifacts are written to build_postfit, including the automatic pin report
and h17_lab02_postfit.wlf.
