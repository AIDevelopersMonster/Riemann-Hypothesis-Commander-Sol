# H19-LAB-02 · E0 cross-technology replication on Gowin GW5A-25A

Status: OPEN / SYNTHESIS CALIBRATION

Purpose: repeat the frozen H19 E0 presentation family on a second FPGA vendor/toolchain without changing the mathematical semantics, decision DAG, external contract, or presentation definitions.

Frozen family:

- DIRECT12
- PREFIX19
- NIELSEN12

Target:

- board: Sipeed Tang Primer 25K
- device: GW5A-25A
- full part number: GW5A-LV25MG121NC1/I0
- tool: Gowin Education IDE 1.9.9Beta-4
- CLI: gw_sh.exe

The first gate is intentionally synthesis-only. No physical P&R/timing claim is made until all three variants pass the same synthesis flow and the Gowin report format is inspected.

Initial command:

~~~powershell
.\tools\run_gowin_syn.ps1 -Mode direct12
~~~

Heavy generated/tool output directories are ignored. Compact summaries and provenance will be committed after the report format is frozen.
