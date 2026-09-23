# H21-LAB-28 · Cyclone V device-specific B=0 specialization

Target:

\[
\boxed{\text{5CEFA7F23C6}}
\]

Tool:

\[
\boxed{\text{Quartus II 13.1}}
\]

Expected installation:

\`C:\altera\13.1\quartus\bin64\quartus_sh.exe\`

## Purpose

Compare the exact same RTL pair already validated in H21-LAB-27:

- \`h21_scalar_pow\` — compiled \(B=0\) Euler-Jacobi path;
- \`h21_quad_pow_b0\` — uncompiled quadratic \(x^n\) path.

Both retain the same 12-bit sequential base modular multiplier architecture.

This laboratory adds device mapping:

- ALMs;
- registers;
- DSP blocks;
- Fmax.

## Run

From PowerShell in this directory:

\`powershell -ExecutionPolicy Bypass -File .\tools\run_all_cyclonev_a7.ps1\`

Or individually:

\`powershell -ExecutionPolicy Bypass -File .\tools\run_cyclonev_a7.ps1 -Mode scalar\`

\`powershell -ExecutionPolicy Bypass -File .\tools\run_cyclonev_a7.ps1 -Mode quadratic\`

Then:

\`powershell -ExecutionPolicy Bypass -File .\tools\summarize_cyclonev_a7.ps1\`

## Acceptance

Both designs must FIT.

Record:

- scalar ALMs / registers / DSP / Fmax;
- quadratic ALMs / registers / DSP / Fmax;
- ratio quadratic/scalar for ALMs;
- combine with LAB-27 cycle counts for area×cycle comparison.

Do not change RTL between LAB-27 and LAB-28 before the matched comparison is recorded.
