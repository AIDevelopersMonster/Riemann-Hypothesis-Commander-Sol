# HATTER-SOL-16 · HDL Control Exercise

## Hardware demonstration of the five-probe `PSL(2,7)` decoder

**Level:** advanced undergraduate / MSc / PhD.  
**Relation to the paper:** supplement to HATTER-SOL-16 v1.1.  
**Public demonstration:** https://www.edaplayground.com/x/Z4Bx

## Objective

Verify that the H16 signature

`A, B, AB, AB^-1, [A,B]`

maps directly to synchronous RTL as a 15-bit input, a 2-bit `Q4` orientation state and a 7-bit identifier for one of the 114 generating-pair orbits.

## Encoding

| Class | Code | Q4 |
|---|---|---|
| `1A` | `000` | `0 / 00` |
| `2A` | `001` | `0 / 00` |
| `3A` | `010` | `0 / 00` |
| `4A` | `011` | `0 / 00` |
| `7A` | `100` | `+1 / 01` |
| `7B` | `101` | `-1 / 10` |

The five 3-bit codes are packed as

```text
{class_A, class_B, class_AB, class_AB_inv, class_K}
```

forming a 15-bit signature. The demonstration LUT contains two golden vectors:

```text
011_011_010_011_100 -> orbit 42, Q4=+1
011_011_010_011_101 -> orbit 43, Q4=-1
```

`orbit_id=42/43` are teaching/demo LUT entries, not the canonical numbering of the complete 114-orbit set. Automatic generation of the full ROM belongs to H17.

## Local CLI

The minimum required tool is Icarus Verilog (`iverilog` + `vvp`). GTKWave is only needed to view `dump.vcd`.

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install iverilog gtkwave
```

Fedora:

```bash
sudo dnf install iverilog gtkwave
```

macOS + Homebrew:

```bash
brew install icarus-verilog gtkwave
```

Windows 10/11: the recommended reproducible route is WSL2 (`wsl --install`), then use the Ubuntu commands above. Native MSYS2 UCRT64 alternative:

```bash
pacman -S mingw-w64-ucrt-x86_64-iverilog mingw-w64-ucrt-x86_64-gtkwave
```

When invoking from `cmd.exe`, add `C:\msys64\ucrt64\bin` to `PATH`.

Verify:

```bash
iverilog -V
vvp -V
gtkwave --version
```

Compile and run:

```bash
iverilog -g2012 -Wall -s tb_h16_orbit_decoder -o h16_sim h16_orbit_decoder.v tb_h16_orbit_decoder.v
vvp h16_sim
```

Waveform:

```bash
gtkwave dump.vcd
```

The Zenodo package also contains a `Makefile`, `run_h16_cli.sh`, `run_h16_cli.bat`, the interactive HTML demo and the EPWave screenshot.

## Practical significance

The exercise connects the H16 mathematical theorem to an actual digital data path. After class recognition, the interface needs only 15 input bits, two orientation-state bits and a 7-bit orbit ID. A student can follow the complete path `theorem -> encoding -> RTL -> testbench -> waveform`; a graduate researcher can extend it to automatic generation of the complete 114-entry ROM, erasure/fault robustness, synthesis and physical FPGA validation.

## Suggested exercises

1. Add an assertion for illegal class codes `110` and `111`.
2. Verify `valid_in -> valid_out` latency.
3. Add a negative vector and confirm `7'h7F`.
4. Generate the ROM from CSV instead of a handwritten `case`.
5. Compare case/LUT/BRAM implementations by area and delay.
6. Prepare the H17 version with all 114 signatures and exhaustive RTL testing.

H16 does not claim timing closure, fixed-point noise margins, error tolerance or a physical-board implementation; those form the H17 program.