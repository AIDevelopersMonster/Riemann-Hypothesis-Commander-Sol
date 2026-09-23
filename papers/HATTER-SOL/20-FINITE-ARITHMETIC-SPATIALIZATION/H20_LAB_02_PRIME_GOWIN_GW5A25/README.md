# H20-LAB-02 · Prime arithmetic on Gowin GW5A-25

Second-vendor falsification gate for the H20 finite arithmetic spatialization experiment.

Target:

\[
\text{GW5A-LV25MG121NC1/I0}
\]

Toolchain: Gowin Education 1.9.9Beta-4.

The arithmetic function, source presentations, registered shell, and 100 MHz clock contract match H20-LAB-01 as closely as the vendor toolchains permit.

Measured widths:

\[
W=8,9,10.
\]

Presentations:

- direct;
- balanced;
- linear.

First calibration command:

\`\`\`powershell
.\tools\run_gowin_prime.ps1 -Width 8 -Mode direct
\`\`\`

Primary question:

Does the Cyclone-V finite-width ordering

\[
L_8 < B_8,\qquad
B_9 < L_9,\qquad
B_{10} < L_{10}
\]

reproduce, shift, or disappear on the GW5A-25 backend?

Claim boundary: cross-vendor comparison concerns measured observer profiles and partition/ranking shapes only. It does not imply routed-netlist identity or a universal hardware invariant.
