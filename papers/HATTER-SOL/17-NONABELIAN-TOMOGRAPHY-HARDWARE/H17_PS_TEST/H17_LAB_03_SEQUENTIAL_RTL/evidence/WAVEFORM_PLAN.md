# H17-LAB-03 · publication waveform plan

The publication waveform uses one canonical generating transaction:

```text
A        = 5e3b88
B        = 7ecc11
mode     = 1
raw      = 8d256a
observed = ed256a
repaired = 8d256a
status   = 2
```

Mode 1 erases robust8 coordinate 0 by replacing bits 23:21 with `111`.

## Signals to display

Primary interface:

- clk
- rst
- start
- busy
- done
- A_in
- B_in
- mode_in
- input_valid
- fingerprint_valid
- status
- raw_signature
- observed_signature
- repaired_signature

Controller/datapath:

- dut.state
- dut.op_idx
- dut.probe_idx
- dut.class_perm
- dut.class_code

Optional detailed word registers:

- dut.n_AB
- dut.n_Ab
- dut.n_BB
- dut.n_AAB
- dut.n_Abb
- dut.n_AAAB
- dut.n_Abbb
- dut.n_AABAb
- dut.n_AAbAb
- dut.n_ABABB
- dut.n_ABaBB

## Expected visible story

1. start latches A/B/mode;
2. busy rises;
3. op_idx advances through the 14 shared compositions;
4. eight class results are captured one at a time;
5. raw_signature becomes `8d256a`;
6. mode 1 masks coordinate 0, giving `ed256a`;
7. ROM-free repair restores `8d256a`;
8. fingerprint_valid/status=2 assert;
9. done pulses after a measured 26-cycle wait.

The waveform is simulation evidence, not a target-FPGA timing claim.
