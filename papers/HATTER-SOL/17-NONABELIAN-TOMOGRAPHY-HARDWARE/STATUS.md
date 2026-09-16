# HATTER-SOL-17 · STATUS

**Branch:** `research/hatter-sol-17-nonabelian-tomography-hardware`  
**State:** active processor implementation research.  
**Date:** 16 September 2026.

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

The still-open hardware gate is target-specific mapping / STA / physical-board verification.

## Exact observer/processor tiers

1. **5-channel baseline** — exact orbit/admissibility decoder, no erasure tolerance.
2. **8-channel robust flat-ID** — globally minimal one-known-erasure observer with explicit orbit ID.
3. **8-channel robust ROM-free fingerprint** — preferred mathematical processor architecture at the current generic-synthesis stage.
4. **9-channel H16-compatible robust** — migration target if the original five H16 channels must remain externally visible.

No final FPGA architecture selection is made until technology mapping and timing data exist.

## Arithmetic two-port frontend seed

For composite `n`,

```text
D2(n)={(a,b): a>=b>=2, ab=n}
MF2(n)=(n/p_min(n), p_min(n)).
```

Examples: `52 -> (26,2)`, `9 -> (3,3)`, `6 -> (3,2)`. This maximal-first rule is an experimental arithmetic search protocol only; it is not a canonical PSL orbit law and there is still no justified realization map from integer factor ports to group elements.

Seed: `docs/INTEGER_TWO_PORT_MAXIMAL_FIRST_FRONTEND_SEED.md`.

## Next strike

H17-08 closes the architecture-level generic synthesis question. The next hardware strike is target-specific:

1. choose a concrete FPGA family/part already available or intended for the experiment;
2. map closure-aware flat and ROM-free cores under identical constraints;
3. record LUT/FF/BRAM/DSP usage and inferred memories;
4. run STA / place-and-route and record critical path and Fmax;
5. select the first board architecture only from those target-specific results;
6. then perform physical-board verification with exact golden vectors.

A later mathematical extension, separate from this hardware gate, is the stronger unknown-location single-error problem (`d_min>=3`) rather than the present known-erasure problem (`d_min>=2`).
