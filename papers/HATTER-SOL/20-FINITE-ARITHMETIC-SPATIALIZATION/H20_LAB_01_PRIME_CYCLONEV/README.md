# H20-LAB-01 · Prime arithmetic on Cyclone V

Target: Cyclone V `5CEFA7F23C6` with Quartus II 13.1.

Function:

[
S_W(x)=min{p>x:p	ext{ prime}}.
]

Measured widths:

[
W=8,9,10.
]

Presentations:

- direct;
- balanced;
- linear.

All are wrapped in the same one-stage input/output registered shell:

[
x 	o x_q 	o 	ext{nextPrime combinational core} 	o p_q.
]

The clock contract is 100 MHz (`10.000 ns`).

The first calibration command is:

```powershell
.	oolsun_cyclonev_prime.ps1 -Width 8 -Mode direct
```

Claim boundary: this laboratory measures vendor synthesis / placement / routing consequences of source presentations. It does not establish minimum circuit complexity or global optimality.
