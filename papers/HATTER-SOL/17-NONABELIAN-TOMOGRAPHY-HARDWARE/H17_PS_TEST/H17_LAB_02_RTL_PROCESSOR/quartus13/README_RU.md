# H17-LAB-02 - Quartus II 13.1 board-free benchmark

Target: Cyclone IV E EP4CE22F17C6, used only as a representative technology target.
No physical board or programmer is required.

From H17_LAB_02_RTL_PROCESSOR run:

    .\tools\run_quartus13.ps1

The script regenerates the exact H17 RTL, runs full Quartus compile, and prints utilization and TimeQuest lines.

Important reports:

    quartus13\h17_lab02_q13.map.rpt
    quartus13\h17_lab02_q13.fit.rpt
    quartus13\h17_lab02_q13.sta.rpt

The 10 ns clock is only a reference. Negative slack is useful: it measures how far the one-cycle combinational architecture is from 100 MHz.
