# HATTER-SOL 20–21 · REPRODUCIBILITY MANIFEST

Status: **PRE-RELEASE CHECKLIST**

## H20 semantic equivalence

Required artifacts:

- strict-next-prime RTL generator;
- DIRECT/BALANCED/LINEAR RTL;
- Python reference model;
- Yosys SAT miter;
- W=4..10 equivalence logs.

Acceptance:

\[
D_W\equiv B_W\equiv L_W
\]

for every declared width.

## H20 Boolean synthesis

Required:

- memory-mapped normalized flow;
- techmap/ABC commands;
- W=4..10 cell-count table.

Acceptance:

\[
D_W<B_W<L_W
\]

for the declared ABC-fast cell-count observer.

## H20 Cyclone V

Target:

\[
5CEFA7F23C6
\]

Tool:

\[
\text{Quartus II 13.1}
\]

Required:

- W=8,9,10 projects/reports;
- resource-class evidence;
- ALM/Fmax/delay/depth extraction.

## H20 Gowin

Target:

\[
\text{GW5A-LV25MG121NC1/I0}
\]

Tool:

\[
\text{Gowin Education 1.9.9Beta-4}
\]

Required:

- W=8,9,10 projects/reports;
- LUT/CLS/BSRAM/Fmax/depth extraction.

## H21 theorem

Required source:

\[
\texttt{H21\_36\_B0\_EULER\_JACOBI\_COLLAPSE.md}
\]

Must contain:

- assumptions;
- exact identity;
- defect equivalence;
- factor-gcd equivalence;
- non-claim boundary.

## H21 matched RTL

Required:

\[
\texttt{H21\_LAB\_27\_B0\_RTL}
\]

Acceptance:

- scalar/quadratic result equality;
- \(q_0=0\);
- \(q_1=\) scalar output;
- zero mismatches on frozen vectors.

Authoritative CI run:

\[
\boxed{35741867585}
\]

## H21 Cyclone V

Required:

\[
\texttt{H21\_LAB\_28\_B0\_CYCLONEV}
\]

Target:

\[
5CEFA7F23C6
\]

Toolchain:

\[
\text{Quartus II 13.1.0 Build 162}
\]

Freeze:

- scalar fit report;
- quadratic fit report;
- scalar TimeQuest report;
- quadratic TimeQuest report;
- generated summary CSV;
- generated device-result Markdown.

Expected headline metrics:

| metric | scalar | quadratic |
|---|---:|---:|
| ALM | 215 | 328 |
| registers | 251 | 455 |
| DSP | 0 | 0 |
| Fmax | 157.33 MHz | 123.20 MHz |
| mean cycles | 175 | 861 |
| mean latency | 1.112312 us | 6.988636 us |

Expected:

\[
\boxed{
AT_{\rm quad}/AT_{\rm scalar}=9.5852.
}
\]

## Archive freeze

Final paper must record:

- Git commit:
  \[
  \texttt{<FINAL\_COMMIT>}
  \]
- release/tag:
  \[
  \texttt{<FINAL\_TAG>}
  \]
- archival DOI:
  \[
  \texttt{<ZENODO\_DOI>}
  \]

These placeholders are intentionally unresolved until final release.

## One-command local LAB-28 reproduction

From the LAB-28 directory:

\[
\texttt{powershell -ExecutionPolicy Bypass -File .\textbackslash tools\textbackslash run\_all\_cyclonev\_a7.ps1}
\]

The generated summary must be archived unchanged.

## Integrity rule

Do not manually transcribe final FPGA numbers into the archival bundle when an
authoritative generated CSV/report exists.

The final manuscript table must be traceable to frozen machine-generated
artifacts.
