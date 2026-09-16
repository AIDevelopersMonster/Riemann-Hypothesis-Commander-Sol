# H17-08 · Closure-aware classification

## 1. The mathematical observation

Let `G = PSL(2,7)`. If the two raw ports satisfy

```text
A,B in G,
```

then every free-group word in `A^{±1},B^{±1}` also lies in `G`.

This is immediate by induction on the word length from closure of a group under multiplication and inversion.

For the H17 robust eight-probe code this means that membership must be established only for the raw ports `A` and `B`. Once that contract is true, each derived probe value needs only its conjugacy-class decoder. Re-running the full

```text
8-point bijection -> PGL cross-ratio -> PSL orientation -> conjugacy class
```

pipeline on all eight derived words is logically redundant.

The optimized hardware contract is therefore

```text
2 x PSL membership-only(A,B)
+ 8 x member-class-only(w_i(A,B)).
```

The probe set and the H17-07 word DAG are unchanged:

```text
AAB, Abb, AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB
```

with exactly 14 permutation compositions and maximum composition depth 3.

## 2. Semantic safety

For invalid raw ports, the derived class codes have no semantic status and the top-level `valid` signal is false.

For valid raw ports that do not generate the whole group, all derived words are still group members, but the robust signature lies outside the generating-orbit code and the downstream decoder/repair path rejects it.

For generating raw ports, the closure-aware class-only outputs agree with the original full structural classifier on every derived word.

Thus membership elimination does not alter the tomography code, erasure distance, orbit IDs, or fingerprint semantics. It removes only logically repeated membership work.

## 3. Exhaustive verification

The GitHub Actions `closure-aware-compare` job completed successfully on the H17 branch.

The generated closure frontend testbench enumerates all

```text
168 x 168 = 28,224
```

ordered PSL(2,7) input pairs and checks the complete 24-bit eight-probe signature against the exact Python group model. This entails

```text
28,224 x 8 = 225,792
```

derived member-class checks.

The separate flat orbit-ID core and the separate ROM-free fingerprint core also compile and simulate successfully in Icarus Verilog in the same CI workflow.

## 4. Yosys methodology

All figures below are from the same generic Yosys `synth; stat` methodology on `ubuntu-latest`. They are technology-independent Boolean-cell counts, not FPGA LUT/FF counts and not timing results.

The control design is the H17-07 14-compose engine with a full `psl27_structural_classify` instance on every derived probe. The optimized design uses the same 14-compose engine and substitutes two raw membership-only blocks plus eight member-class-only blocks.

| design | full-classifier baseline | closure-aware | reduction | reduction % |
|---|---:|---:|---:|---:|
| robust8 frontend | 38,957 | 20,485 | 18,472 | 47.42% |
| flat orbit-ID core | 43,330 | 24,730 | 18,600 | 42.93% |
| ROM-free fingerprint core | 42,484 | 23,937 | 18,547 | 43.66% |

The top-level hierarchy counts are the authoritative comparison because Yosys can slightly change module-local counts depending on the enclosing synthesis context.

For scale, isolated closure-aware block synthesis produced approximately:

```text
membership-only : 1,941 generic cells
member-class-only: 1,393 generic cells
```

while a full structural classifier in the control synthesis is about 3.35k generic cells. The precise saving at the composed top level is already captured by the table above.

## 5. Flat versus ROM-free after closure optimization

Closure optimization does not reverse the backend ordering:

```text
closure-aware flat    = 24,730 cells
closure-aware ROM-free= 23,937 cells
```

The ROM-free fingerprint architecture is smaller by

```text
793 cells = 3.21% of the closure-aware flat total.
```

This comparison is now meaningful because both backends share exactly the same closure-aware 14-compose frontend.

## 6. H17-08 result

Within the current generic synthesis model, the group-closure theorem removes almost half of the synthesized frontend logic without weakening the exact robust tomography contract:

```text
38,957 -> 20,485 generic cells
```

or

```text
47.42% frontend reduction.
```

This closes H17-08 at the technology-independent synthesis level.

It does **not** yet establish FPGA LUT/FF usage, Fmax, critical-path delay, power, or board behavior. Those claims require target-specific technology mapping, place-and-route / STA, and ultimately hardware execution.

## 7. Next hardware strike

The next comparison should preserve the closure-aware frontend and move from generic cells to a concrete FPGA target:

1. choose the target family/part;
2. map both closure-aware backends with the same constraints;
3. record LUT/FF/BRAM/DSP usage;
4. record post-map/post-route critical path and Fmax;
5. select flat orbit-ID or ROM-free fingerprint backend for the first board image.
