# H18-LAB-01 — adaptive one-erasure RTL handoff

This laboratory turns H18-06 into a board-independent sequential RTL reference.

## Architecture

\`\`\`text
A,B
 -> two raw PSL membership checks
 -> exact adaptive controller (308 nonterminal states)
 -> compact 24-word microcode
 -> one sequential word accumulator, max word length 4
 -> one reused conjugacy-class engine
 -> branch on class or one injected ERASED result
 -> canonical H17 orbit_id or REJECT
\`\`\`

The controller is generated from the exact H18-06 recurrence, not handwritten.

## Frozen structural metrics

The deterministic materialization currently gives:

- **308** nonterminal controller states;
- **69** pre-erasure states;
- **239** post-erasure states;
- **24** distinct word labels used by the selected strategy;
- maximum word length **4**;
- worst case **5** query attempts;
- worst case **4** successful class answers;
- worst case **19** sequential letter-compositions;
- no-erasure worst case **4** attempts and **15** letter-compositions.

For comparison, H17-LAB-03 uses:

- one class engine;
- a fixed 14-composition shared DAG;
- 8 fixed class captures;
- H17 ROM-free repair with 306 internal decision nodes;
- measured RTL transaction wait 26 cycles in its frozen implementation.

The striking \(308\) versus \(306\) node counts are only a **structural proxy**. They are not LUT counts and must not be interpreted as equal hardware area.

## Cycle-level implication of the simple reference engine

The H18 reference engine evaluates each selected word from the identity, one letter per composition cycle, without cross-query caching.

Hence a worst-case one-erasure path has:

\[
19\text{ composition cycles}
+
5\text{ classify/branch cycles}.
\]

Adding one raw-membership/check stage and one terminal stage gives a natural reference bound of roughly **26 sequential stages/cycles from accepted request to completion**, depending on the exact testbench edge-count convention.

This numerical coincidence with H17-LAB-03's measured 26-cycle transaction is architecturally interesting but is **not yet a measured H18 RTL result**.

The important difference is:

- H17 spends 14 shared-DAG compositions and 8 class captures;
- H18 may spend up to 19 naive word-letter compositions and 5 class captures.

Therefore the next optimization target is obvious: cache common word prefixes across the adaptive path.

## Run on Windows PowerShell

From this directory:

\`\`\`powershell
.\tools\test_h18_adaptive.ps1
\`\`\`

The script:

1. regenerates the controller ROM and word ROM;
2. regenerates the H17 closure-aware membership/classifier RTL;
3. compiles the H18 sequential core with Icarus;
4. runs **197 x 6 = 1182** frozen representative/fault vectors.

The six fault modes are:

\`\`\`text
0 = no erasure
1..5 = erase that attempted query if reached
\`\`\`

## Generic synthesis

If Yosys is installed:

\`\`\`powershell
.\tools\synth_h18_adaptive.ps1
\`\`\`

The result must be compared with H17-LAB-03 using the same Yosys version and the same generic synthesis methodology.

## Output contract

\`\`\`text
status=0  raw A/B invalid (not PSL)
status=1  valid PSL pair but non-generating -> REJECT
status=2  generating pair identified exactly
status=4  invalid/unreachable controller transition
\`\`\`

\`orbit_id\` is the canonical H17 ID \(0..113\) on status 2 and 127 otherwise.

## Non-claim

This layer is a reproducible RTL handoff. Until regression and synthesis logs are produced on an actual toolchain, no FPGA LUT/FF/Fmax/power claim is made.
