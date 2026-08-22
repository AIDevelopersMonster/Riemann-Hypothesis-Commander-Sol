# RH-SOL Series Map

| ID | Label | Working title | Core question | Status |
|---|---|---|---|---|
| RH-SOL-01 | LATTICE | Integer-Lattice Encoding of Riemann-Zeta Argand Loops | Does the Dirichlet `log n` structure survive binary lattice quantization? | Published |
| RH-SOL-02 | SHIFT | Shifted-Lattice Spectroscopy of Riemann-Zeta Argand Loops | Does the effect survive arbitrary lattice translation? | Next priority |
| RH-SOL-03 | REALZERO | Dirichlet Frequencies without Smooth Time | Does the comb survive direct use of actual zero ordinates `gamma_n`? | Planned |
| RH-SOL-04 | FIREWALL | Falsification Tests for Arithmetic Spectra in Quantized Zeta Geometry | Can geometry-preserving and phase-randomized nulls destroy the effect? | Planned |
| RH-SOL-05 | POISSON | Poisson Summation and the Moving Integer Lattice of Zeta Argand Domains | Can shifted lattices expose Fourier coefficients of loop interiors? | Planned |
| RH-SOL-06 | NYQUIST | Nyquist Aliasing, Dirichlet Modes and the Riemann-Siegel Scale | What is the precise status of the sampling/aliasing analogy? | Planned |
| RH-SOL-07 | SURVIVAL | How Much Arithmetic Information Survives Geometric Quantization? | How much geometric information can be removed before the spectrum fails? | Planned |
| RH-SOL-08 | RATE | Rate-Distortion of Dirichlet Spectra under Binary Geometric Encoding | Can a task-specific rate-distortion law be defined? | Planned |
| RH-SOL-09 | DECODE | Decoding Dirichlet Phase from Binary Zeta Geometry | Can `gamma_n log m mod 2pi` be predicted from the bitmap? | Planned |
| RH-SOL-10 | MINCODE | Minimal Geometric Codes for Arithmetic Spectral Recovery | What is the smallest observable preserving useful spectral information? | Planned |
| RH-SOL-11 | LFUNCTIONS | Persistence of Dirichlet Spectra under Geometric Quantization of L-Functions | Does the phenomenon generalize beyond zeta? | Planned |
| RH-SOL-12 | PRIMESET | Logarithmic Spectral Signatures of Prime-Generated Sets under Nonlinear Encoding | Which prime-generated logarithmic structures survive nonlinear maps? | Planned |
| RH-SOL-13 | ENVELOPE | Spectral Envelopes of Quantized Zeta Geometry | What transfer envelope relates source amplitudes to lattice amplitudes? | Planned |
| RH-SOL-14 | RESIDUAL | Beyond the Dirichlet Comb | What remains after removing the known Dirichlet and mixing-frequency algebra? | Planned |
| RH-SOL-15 | SYNTHESIS | Arithmetic Information through Geometric Loss | What survived, what failed, and what general principles remain? | Planned |

## Dependency spine

```text
RH-SOL-01 LATTICE
   |
   +--> RH-SOL-02 SHIFT
   +--> RH-SOL-03 REALZERO
   +--> RH-SOL-04 FIREWALL
             |
             +--> RH-SOL-05 POISSON
             +--> RH-SOL-06 NYQUIST
                       |
                       +--> RH-SOL-07 SURVIVAL
                               |
                               +--> RH-SOL-08 RATE
                               +--> RH-SOL-09 DECODE
                               +--> RH-SOL-10 MINCODE
                                         |
                                         +--> RH-SOL-11 LFUNCTIONS
                                         +--> RH-SOL-12 PRIMESET

RH-SOL-13 ENVELOPE and RH-SOL-14 RESIDUAL are cross-cutting branches.
RH-SOL-15 SYNTHESIS closes the cycle.
```
