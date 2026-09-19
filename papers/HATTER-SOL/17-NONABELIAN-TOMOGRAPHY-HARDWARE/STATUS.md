# HATTER-SOL-17 · STATUS

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**State:** target-FPGA physical evidence obtained; H17-09 supplement prepared.  
**Date:** 19 September 2026.

## H17-01 · canonical golden model — CLOSED

The deterministic `PSL(2,7)` golden model is fixed:

```text
|G|                                      = 168
generating ordered pairs                 = 19,152
non-generating ordered pairs             =  9,072
generating simultaneous-conjugacy orbits =    114
```

Canonical orbit IDs `0..113` are stable. Source: `tools/generate_psl27_golden_model.py`.

## H17-02 · generation admissibility — CLOSED

For the original H16 five-probe signature,

```text
generating signature image      = 114
non-generating signature image  =  66
intersection                    =   0
```

Hence for valid `PSL(2,7)` raw ports,

```text
signature_hit <=> <A,B> = PSL(2,7).
```

Certificate: `certificates/psl27_signature_admissibility_certificate.py`.  
Note: `docs/H17_02_SIGNATURE_ADMISSIBILITY_AND_ERASURE.md`.

## H17-03 · minimum depth for one-known-erasure recovery — CLOSED

The complete primitive cyclic trace family through depth four has 25 coordinates but `d_min=1`. Exactly seven generating-orbit pairs are at distance one, and in every case the only depth-`<=4` separator is `ABab=[A,B]`.

The exact-depth-five probe `AABAb` separates all seven defects. Therefore, within this observer family,

```text
minimum possible maximum primitive depth = 5.
```

The full 51-coordinate depth-`<=5` family has generating `d_min=5`.

Certificate: `certificates/psl27_depth5_erasure_certificate.py`.  
Note: `docs/H17_03_DEPTH5_ONE_ERASURE.md`.

## H17-04 · optimal joint one-erasure tomography — CLOSED

The robust objective is simultaneously

```text
d_gen/gen >= 2
d_gen/non >= 2.
```

Across all 51 depth-`<=5` cyclic trace coordinates, the exact finite model yields 13,965 binary covering constraints. A zero-gap binary MILP gives

```text
minimum joint one-known-erasure probe count = 8.
```

One optimal family is

```text
AAB, Abb, AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB
```

with direct verification

```text
d_gen/gen = 2
d_gen/non = 2.
```

Among cardinality-eight optima, at least four probes have exact depth five; with exactly four depth-five probes the minimum total primitive length is 34, realized by profile `(3,3,4,4,5,5,5,5)`.

Certificate: `certificates/psl27_joint_one_erasure_code_certificate.py`.  
Note: `docs/H17_04_OPTIMAL_JOINT_ONE_ERASURE_CODE.md`.

### H16-frozen migration variant

If the original H16 five probes must remain exposed, exhaustive enumeration of all `C(46,3)=15,180` three-coordinate extensions proves that eight total probes are impossible. A minimum nine-probe robust family is

```text
A, B, AA, AB, Ab, ABB, Abb, ABab, ABaBB
```

with both joint distances equal to two.

## H17-05 · LUT-free structural PSL/class processor — CLOSED

The structural classifier works directly from a 24-bit permutation. It checks 8-point bijectivity, projective cross-ratio consistency, PSL orientation, then conjugacy class.

Exhaustive enumeration over all `8! = 40,320` permutations gives exactly

```text
PGL(2,7) accepted = 336
PSL(2,7) accepted = 168.
```

For valid members, orders `1,2,3,4` identify `1A,2A,3A,4A`; quadratic orientation on the unique 7-cycle separates `7A` and `7B` into `24+24` elements.

Certificate: `certificates/psl27_structural_class_engine_certificate.py`.  
Generator: `tools/generate_psl27_structural_processor.py`.  
Note: `docs/H17_05_LUT_FREE_STRUCTURAL_PROCESSOR.md`.

## H17-06 · ROM-free erasure repair — CLOSED

The 24-bit robust8 signature is itself a canonical generating-orbit fingerprint. For every known erased coordinate, exact dynamic programming gives minimum worst-case repair/admissibility decision depth

```text
4 class queries.
```

Depth-optimal internal-node counts are

```text
41, 41, 43, 43, 30, 39, 39, 30
```

for 306 nodes before synthesis/factoring across erasure modes.

The adversarial HDL test overwrites the erased class field by `3'b111`; the repair path therefore cannot accidentally read the missing value.

Certificate: `certificates/psl27_erasure_repair_tree_certificate.py`.  
Generator: `tools/generate_psl27_romfree_repair.py`.  
Note: `docs/H17_06_ROM_FREE_ERASURE_REPAIR.md`.

## H17-07 · optimal shared word DAG — CLOSED

Naively evaluating the eight robust words independently costs 26 permutation compositions. Exact DAG optimization proves the minimum is

```text
14 permutation compositions
maximum composition depth = 3.
```

One optimum is

```text
level 1: AB, Ab, BB
level 2: AAB, ABA, ABa, Abb, AbAb
level 3: AAAB, Abbb, AABAb, AAbAb, ABABB, ABaBB.
```

It has been checked over all `168^2=28,224` PSL input pairs.

Certificate: `certificates/psl27_word_dag_certificate.py`.  
Generator: `tools/generate_psl27_robust8_dag.py`.  
Note: `docs/H17_07_OPTIMAL_WORD_DAG.md`.

## H17-08 · closure-aware classification — CLOSED at generic-synthesis level

The key group fact is

```text
A,B in PSL(2,7) => w(A,B) in PSL(2,7)
```

for every free-group probe word `w`. Therefore the eight derived words do not need eight repeated membership tests. The optimized architecture is

```text
2 x raw membership-only(A,B)
+ 8 x member-class-only(derived word)
```

on the same H17-07 14-compose/depth-3 DAG.

The GitHub Actions closure-aware job passes exhaustive Icarus verification. The frontend test enumerates all 28,224 ordered PSL input pairs, hence checks 225,792 derived word classes against the exact model. Separate flat orbit-ID and ROM-free fingerprint cores also compile and simulate successfully.

Using identical generic Yosys `synth; stat` methodology:

| design | full-classifier baseline | closure-aware | reduction | reduction % |
|---|---:|---:|---:|---:|
| robust8 frontend | 38,957 | 20,485 | 18,472 | 47.42% |
| flat orbit-ID core | 43,330 | 24,730 | 18,600 | 42.93% |
| ROM-free fingerprint core | 42,484 | 23,937 | 18,547 | 43.66% |

Thus the group-closure theorem removes nearly half of the generic synthesized frontend logic without changing the tomography code or erasure guarantees.

After closure optimization the ROM-free complete core remains smaller than the flat-ID core:

```text
24,730 - 23,937 = 793 cells
```

or 3.21% of the closure-aware flat total.

These are technology-independent Boolean-cell counts. They are **not** FPGA LUT/FF counts and do not establish Fmax, critical path, power, or board behavior.

Generators/workflows:

- `tools/generate_psl27_closure_compare.py`
- `tools/generate_psl27_closure_classifiers.py`
- `tools/generate_psl27_robust8_closure.py`
- `.github/workflows/hatter-sol-17-hdl.yml`
- `.github/workflows/h17-baseline-metrics.yml`

Detailed note: `docs/H17_08_CLOSURE_AWARE_CLASSIFICATION.md`.

## External HDL / synthesis gates

GitHub-hosted Icarus/Yosys gates now cover:

```text
structural classifier           PASS
robust8 full-classifier core    PASS
ROM-free repair                 PASS
closure-aware frontend          PASS
closure-aware flat core         PASS
closure-aware ROM-free core     PASS
generic Yosys synthesis         PASS
```

Target-specific mapping and STA are now completed for Cyclone IV E and Cyclone V E. Cyclone IV also has a matched post-fit SDF ModelSim witness. Physical-board verification remains open.

## Exact observer/processor tiers

1. **5-channel baseline** — exact orbit/admissibility decoder, no erasure tolerance.
2. **8-channel robust flat-ID** — globally minimal one-known-erasure observer with explicit orbit ID.
3. **8-channel robust ROM-free fingerprint** — preferred mathematical processor architecture at the current generic-synthesis stage.
4. **9-channel H16-compatible robust** — migration target if the original five H16 channels must remain externally visible.

No final FPGA architecture selection is made until technology mapping and timing data exist.

## H17-09 · target-FPGA physical evidence — CLOSED for board-free benchmark

The closure-aware H17-LAB-02 processor has now been compiled through vendor place-and-route and TimeQuest.

Cyclone IV E EP4CE22F17C6:

```text
LE                     19,540 / 22,320 = 88%
registers              132
Fmax slow 85 C         24.52 MHz
worst data delay       41.082 ns
logic levels           65
cell / routing         15.017 / 25.873 ns
```

A matched slow-corner Verilog/SDF ModelSim run passes the canonical 20 MHz transaction.

The equal-C7 capacity control gives 47.404 ns on EP4CE22F17C7 and 47.249 ns on EP4CE115F29C7: only about 0.33% difference despite the much larger nominal device. Thus the experiment does not support the simple hypothesis that high 22K occupancy is the dominant timing limit.

Cyclone V E 5CEFA7F23C6, with unchanged RTL and normal automatic mapping:

```text
ALMs                   7,941 / 56,480 = 14%
registers              132
DSP blocks             40 / 156
Fmax slow 85 C         27.85 MHz
worst data delay       35.694 ns
logic levels           34
cell / routing         12.726 / 22.969 ns
```

Relative to the equal-grade Cyclone IV 22K C7 control, selected-path Fmax improves about 31% and data delay falls about 24.7%. This is a platform-level result, not a pure LUT/ALM comparison, because Quartus infers 40 DSP blocks.

Routing remains about 62–64% of the selected critical path. The unchanged one-cycle architecture does not close at 100 MHz on the tested targets.

Quartus II 13.1 generates a Cyclone V post-fit `.vo` but no timing `.sdo` for this family; Cyclone V physical-delay evidence is therefore TimeQuest, not an SDF-backed waveform.

Detailed supplement: `docs/H17_09_TARGET_FPGA_PHYSICAL_EVIDENCE.md`.  
Instructor laboratory: `labs/H17_LAB_02_INSTRUCTOR_GUIDE.md`.  
Model student report: `labs/H17_LAB_02_MODEL_STUDENT_REPORT.md`.

## Arithmetic two-port frontend seed

For composite `n`,

```text
D2(n)={(a,b): a>=b>=2, ab=n}
MF2(n)=(n/p_min(n), p_min(n)).
```

Examples: `52 -> (26,2)`, `9 -> (3,3)`, `6 -> (3,2)`. This maximal-first rule is an experimental arithmetic search protocol only; it is not a canonical PSL orbit law and there is still no justified realization map from integer factor ports to group elements.

Seed: `docs/INTEGER_TWO_PORT_MAXIMAL_FIRST_FRONTEND_SEED.md`.

## Next strike

The board-free target-specific gate is now closed. The next hardware question is architectural rather than capacity-only: test registered/multi-cycle boundaries through the word/class/repair path under a separately versioned architecture, while preserving the current unchanged-RTL measurements as the baseline. Physical-board verification remains a later independent gate.

A later mathematical extension, separate from the hardware gate, is the stronger unknown-location single-error problem (d_min>=3) rather than the present known-erasure problem (d_min>=2).
