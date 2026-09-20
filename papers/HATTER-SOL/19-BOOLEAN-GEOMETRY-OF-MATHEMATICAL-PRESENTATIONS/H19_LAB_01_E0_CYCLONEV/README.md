# H19-LAB-01 · E0 presentation family on Cyclone V

Status: **READY FOR LOCAL QUARTUS II 13.1 RUN**

Target:

\[
\boxed{\texttt{5CEFA7F23C6}}
\]

This is the same Cyclone V target used for the frozen H17-LAB-02 and
H18-LAB-03/LAB-04 controls.

## Compared presentations

- \`direct12\`
- \`prefix19\`
- \`nielsen12\`

All three implement the same frozen H18 restricted-12 E0 semantics:

- same 197-state identify-or-REJECT task;
- same static persistent erased-query identity;
- same 305-node decision DAG;
- same registered-input / combinational-core / registered-output shell;
- same 2561-transaction regression contract.

Only the observer factorization changes.

## Technology stack

- Quartus II 13.1;
- Cyclone V 5CEFA7F23C6;
- 100 MHz reference SDC;
- Slow 1100 mV / 85 C worst-path report;
- no board pin assignment;
- Auto Fit defaults unless Quartus reports otherwise.

## One-command run

From this directory:

\`\`\`powershell
.\tools\run_all_cyclonev_a7.ps1
\`\`\`

or one presentation:

\`\`\`powershell
.\tools\run_cyclonev_a7.ps1 -Mode direct12
.\tools\run_cyclonev_a7.ps1 -Mode prefix19
.\tools\run_cyclonev_a7.ps1 -Mode nielsen12
\`\`\`

The script prints utilization and TimeQuest summaries and then produces a
detailed Slow85 setup path for each successful fit.

## Claim boundary

This laboratory measures

\[
\widehat H_{\Theta,\Pi_{\rm open}}(M_i)
\]

under one fixed Quartus flow.

It is not a proof of the globally optimal hardware image of any presentation.
