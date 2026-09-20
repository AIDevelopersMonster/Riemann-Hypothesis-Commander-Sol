# H19 · Bibliography and prior-art audit

Status: **PUBLICATION HARDENING / VERIFIED CORE REFERENCES**

Date: 20 September 2026.

## Scope

This audit supports the publication claim of HATTER-SOL-19. It does not attempt to make the abstract observer/partition language novel. The manuscript must distinguish:

1. classical background;
2. tool/method references;
3. the H19-specific controlled cross-stage/cross-vendor experiment.

## Verified background references

### Branching programs, decision diagrams, circuits

**Ingo Wegener.** *Branching Programs and Binary Decision Diagrams: Theory and Applications.* SIAM, 2000. DOI: 10.1137/1.9780898719789.

Use for the classical relation among branching programs, decision trees, formulas and circuits. H19 must not present temporal/spatial or adaptive/circuit comparisons as a new general complexity theory.

**Ingo Wegener.** “Time-space trade-offs for branching programs.” *Journal of Computer and System Sciences* 32(1), 1986, 91–96. DOI: 10.1016/0022-0000(86)90004-8.

Use as classical background for representation-dependent time/space phenomena.

**Randal E. Bryant.** “Graph-Based Algorithms for Boolean Function Manipulation.” *IEEE Transactions on Computers* C-35(8), 1986, 677–691. DOI: 10.1109/TC.1986.1676819.

Use for classical graph-based Boolean representations and the fact that representation structure can matter independently of extensional Boolean semantics.

### Compiler correctness and translation validation

**Amir Pnueli, Michael Siegel, Eli Singerman.** “Translation Validation.” TACAS 1998, LNCS 1384, 151–166. DOI: 10.1007/BFb0054170.

**George C. Necula.** “Translation Validation for an Optimizing Compiler.” PLDI 2000, 83–94. DOI: 10.1145/349299.349314.

**Xavier Leroy.** “Formal Verification of a Realistic Compiler.” *Communications of the ACM* 52(7), 2009, 107–115. DOI: 10.1145/1538788.1538814.

Use these to delimit H19 from semantic-preservation/compiler-correctness work. E0 equivalence and preservation are experimental controls in H19, not claimed contributions to verified compilation.

### Equality saturation and retained equivalence information

**Ross Tate, Michael Stepp, Zachary Tatlock, Sorin Lerner.** “Equality Saturation: A New Approach to Optimization.” POPL 2009, 264–276. DOI: 10.1145/1480881.1480915.

Use to avoid novelty claims of the form “compilers can preserve multiple equivalent representations” or “destructive optimization order can hide alternatives.”

### Logic synthesis tools used by the experiment

**Clifford Wolf, Johann Glaser.** “Yosys - A Free Verilog Synthesis Suite.” *Austrochip Workshop on Microelectronics 2013*, 47–52.

**Robert K. Brayton, Alan Mishchenko.** “ABC: An Academic Industrial-Strength Verification Tool.” CAV 2010, LNCS 6174, 24–40. DOI: 10.1007/978-3-642-14295-6_5.

Use as method/tool references for the generic synthesis stages. Tool behavior in H19 remains version/options relative.

## Novelty boundary after audit

The manuscript may claim as H19-specific:

\[
\boxed{
\text{controlled E0 mathematical presentations}
+
\text{stage-indexed observer partitions}
+
\text{measured nonmonotone visibility}
+
\text{two-vendor replicated physical quotient}
}
\]

on the frozen finite family.

The manuscript must **not** claim novelty for:

- partition lattices;
- observational equivalence in the abstract;
- branching-program/circuit comparisons;
- semantic preservation;
- translation validation;
- equality saturation;
- e-graphs;
- generic phase-ordering effects;
- unrestricted circuit lower bounds.

## Strongest defensible empirical claim

For the frozen E0 family

\[
\mathcal F=\{D,P,N\},
\]

the generic ABC-fast cell observer induces

\[
\{\{D\},\{P\},\{N\}\},
\]

whereas two independent vendor-specific joint measured physical observers induce

\[
\boxed{
\{\{D,P\},\{N\}\}.
}
\]

This is a replicated finite experimental partition result. It is not a universal technology-independent invariant.

## Bibliography status

Core bibliography: **verified sufficiently for manuscript candidate**.

Remaining optional expansion before journal submission:

- add a modern e-graph survey/application reference if equality-saturation context is expanded;
- add vendor tool manuals only if the target venue requires formal tool citations;
- add FPGA synthesis reproducibility literature if the discussion section is enlarged.

No additional reference is required to support the narrow present claim set.
