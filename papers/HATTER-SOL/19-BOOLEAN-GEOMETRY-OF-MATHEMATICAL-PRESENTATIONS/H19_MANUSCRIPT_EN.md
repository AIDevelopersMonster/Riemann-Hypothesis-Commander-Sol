# HATTER-SOL-19

# Boolean Geometry of Mathematical Presentations

## Observability, hiding, and re-exposure of structure across compilation and FPGA realization

Author: Alex Malachevsky  
ORCID: 0009-0008-6009-3196  
AI research collaborator: Commander Sol · Hatter Sol  
Status: publication candidate  
Date: 20 September 2026

## Abstract

We study a finite family of mathematically motivated presentations of the same finite computational task and ask which structural distinctions remain observable after Booleanization, synthesis, technology mapping, and physical FPGA implementation.

The frozen E0-equivalent family is

\[
D=\mathrm{DIRECT12},\qquad
P=\mathrm{PREFIX19},\qquad
N=\mathrm{NIELSEN12}.
\]

All three realizations have identical semantics, the same 305-node decision DAG, the same fault model, the same registered shell, and the same 2561-vector regression contract, while differing in source mathematical factorization.

For compiler stage \(i\) and observer \(O\), define

\[
M_a\sim_{i,O}M_b
\iff
O(C_i(M_a))=O(C_i(M_b)).
\]

This induces a partition of the finite presentation family. In the generic Yosys flow, DIRECT12 and PREFIX19 are distinct at source level, indistinguishable by the reported cell histogram after proc/opt and techmap, and distinct again after abc-fast. Determinism yields a no-resurrection statement for complete compiler state: once two complete states are equal, a later deterministic stage cannot separate them again.

On Cyclone V, Quartus II 13.1, 5CEFA7F23C6, the declared joint measured physical profile yields

\[
\mathcal P_{\rm CV}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

An independent replication on Gowin GW5A-25A, Gowin Education IDE 1.9.9Beta-4, yields the same post-P&R quotient:

\[
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

The main result is therefore a finite two-vendor replication of partition shape, not a universal FPGA-cost law.

## 1. Formal model

Let

\[
M=(X,Y,Q,G,\lambda,\delta,\omega)
\]

be a finite adaptive presentation inducing

\[
\Phi_M:X\to Y.
\]

All compared presentations share the same external E0 contract.

A canonical temporal realization evaluates only the observer selected by the current decision node. A full spatial realization computes supported observers in parallel and replaces decision nodes by combinational selectors. Therefore

\[
D_{\rm query}\ne D_{\rm Boolean}\ne L_{\rm transaction}.
\]

Under the presentation-preserving discipline \(\Pi_{\rm DAG}\),

\[
S_{\rm gen}(M)
=
\sum_{q_i\in Q_{\rm used}}S(q_i)
+
\sum_{v\in V_{\rm nt}}s_{\rm sel}(r_v,b)
+
S_{\rm shell}.
\]

This is construction accounting, not a lower bound on minimum Boolean circuit complexity.

## 2. Controlled family

DIRECT12 uses 24 permutation-composition nodes with maximum composition depth 3.

PREFIX19 uses 19 shared composition nodes at the same depth:

\[
24\to19.
\]

NIELSEN12 uses the mixed source profile

\[
18\ \text{shear}
+
3\ \text{inverse}
+
6\ \text{direct commutator compositions}.
\]

All three RTL variants use the same 305-node decision DAG and pass the common 2561-transaction regression.

## 3. Observer-induced partitions

At compiler stage \(i\), let \(C_i(M)\) be the complete stage state and

\[
O:C_i\to Z_O
\]

an observer. Define

\[
M_a\sim_{i,O}M_b
\iff
O(C_i(M_a))=O(C_i(M_b)).
\]

For a finite family,

\[
\mathcal P_{i,O}=\mathcal F/{\sim_{i,O}}.
\]

If \(O_a=f\circ O_b\), then

\[
O_a\preceq O_b
\Longrightarrow
\mathcal P_{i,O_a}\preceq\mathcal P_{i,O_b}.
\]

These order-theoretic facts are used as language, not claimed as standalone novelty.

## 4. No resurrection of complete state

For a deterministic compiler tower

\[
C_{i+1}(M)=F_i(C_i(M)),
\]

equality at stage \(i\) implies equality at stage \(i+1\). Thus exact-state visibility cannot contain a \(0\to1\) transition.

Later coarse re-separation therefore witnesses an earlier hidden distinction rather than reconstruction of destroyed information.

## 5. Generic compiler trajectory

For DIRECT12/PREFIX19,

\[
24\ne19
\]

at source level.

After Yosys proc/flatten/opt:

\[
D=4919,\qquad P=4919
\]

reported cells with equal reported cell histograms.

After generic techmap:

\[
D=63719,\qquad P=63719.
\]

Wire totals remain distinct:

\[
7732\ne7582,
\qquad
17674\ne17531.
\]

After abc-fast:

\[
D=60374,\qquad
P=60383,\qquad
N=68406.
\]

Hence the family partitions are

\[
\mathcal P_{\rm proc}
=
\{\{D,P\},\{N\}\},
\]

\[
\mathcal P_{\rm techmap}
=
\{\{D,P\},\{N\}\},
\]

\[
\mathcal P_{\rm ABC}
=
\{\{D\},\{P\},\{N\}\}.
\]

## 6. Latent partition gap

Let \(\mathcal P_i^{\rm full}\) be the complete-state partition and \(\mathcal P_i^O\) the observer partition. Then

\[
\mathcal P_i^{\rm full}\preceq\mathcal P_i^O.
\]

With

\[
Q(\mathcal P)=\sum_{B\in\mathcal P}\binom{|B|}{2},
\]

define

\[
L_i(O)=Q(\mathcal P_i^O)-Q(\mathcal P_i^{\rm full}).
\]

For the cell-histogram observer,

\[
\boxed{
L_{\rm cellhist}:1\to1\to0.
}
\]

## 7. Cyclone-V laboratory

Target: 5CEFA7F23C6. Tool: Quartus II 13.1. Reference clock: 100 MHz.

| Presentation | ALM | Reg | DSP | Fmax MHz | Data delay ns | Levels | Cell ns | Routing ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| PREFIX19 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| NIELSEN12 | 12017 | 69 | 48 | 27.50 | 36.212 | 31 | 14.026 | 22.182 |

Thus

\[
\boxed{
\mathcal P_{\rm CV}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

DIRECT12 and PREFIX19 agree on every predeclared Cyclone-V physical coordinate. This is measured-profile equality, not routed-state identity.

## 8. Gowin laboratory

Target: GW5A-LV25MG121NC1/I0. Tool: Gowin Education IDE 1.9.9Beta-4. Clock contract: 100 MHz, period 10 ns.

### Synthesis

| Presentation | Logic | LUT | ALU | Reg | DSP |
| --- | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 19376 | 18882 | 494 | 69 | 28 |
| PREFIX19 | 19376 | 18882 | 494 | 69 | 28 |
| NIELSEN12 | 21221 | 20729 | 492 | 69 | 28 |

### Post-P&R

| Presentation | P&R | Logic | LUT | ALU | Reg | CLS | DSP | Fmax MHz | Levels | WNS ns | Setup TNS ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| PREFIX19 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| NIELSEN12 | PASS | 21448 | 20729 | 719 | 69 | 10941 | 28 | 16.599 | 49 | -50.243 | -628.206 |

All variants completed placement, routing, timing analysis, and bitstream generation. None closes the 100 MHz target.

Thus

\[
\boxed{
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

## 9. Cross-vendor replication

The central physical result is

\[
\boxed{
\mathcal P_{\rm CV}^{\rm joint}
=
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

The measured trajectory is

\[
\{\{D,P\},\{N\}\}_{\rm proc}
\to
\{\{D,P\},\{N\}\}_{\rm techmap}
\to
\{\{D\},\{P\},\{N\}\}_{\rm ABC}
\to
\begin{cases}
\{\{D,P\},\{N\}\}_{\rm CycloneV},\\
\{\{D,P\},\{N\}\}_{\rm Gowin}.
\end{cases}
\]

This is observer-relative physical re-coarsening.

## 10. Multidimensional physical cost

NIELSEN12 is physically larger on both targets, but its timing direction differs: its Fmax is lower than D/P on Cyclone V and slightly higher on Gowin.

Therefore these experiments do not support a universal scalar ordering of the presentations.

## 11. Reproducibility

Each physical laboratory preserves a SHA-256 provenance manifest over 33 key run artifacts.

The hashes bind reported summaries to specific local RTL, constraints, tool snapshots, transcripts, synthesis/P&R reports, and timing reports. They do not prove deterministic rerouting across machines, seeds, installations, or future tool versions.

## 12. Prior-art boundary

Branching programs, BDDs, and decision-tree/circuit comparisons are classical [Wegener 2000; Wegener 1986; Bryant 1986]. Translation validation and verified compilation are established [Pnueli et al. 1998; Necula 2000; Leroy 2009]. Equality saturation is established [Tate et al. 2009].

Accordingly, H19 does not claim novelty for partition lattices, observational equivalence, semantic preservation, branching-program/circuit comparisons, equality saturation, generic phase-ordering effects, or unrestricted circuit lower bounds.

The H19-specific contribution is

\[
\boxed{
\text{controlled E0 presentations}
+
\text{compiler observer atlas}
+
\text{nonmonotone visibility}
+
\text{two-vendor replicated physical quotient}.
}
\]

## 13. Limitations and non-claims

The result is limited to one semantic task family, three presentations, two FPGA vendors, specific tool versions/options, and declared observers.

We do not claim complete compiler-state equality for D/P, routed-netlist identity, bitstream identity, universal cross-technology invariance, a globally optimal presentation, a technology-independent scalar cost, or unrestricted circuit lower bounds.

## 14. Conclusion

For the frozen E0 family,

\[
\boxed{
\mathcal P_{\rm CycloneV}^{\rm joint}
=
\mathcal P_{\rm Gowin}^{\rm joint}
=
\{\{DIRECT12,PREFIX19\},\{NIELSEN12\}\}.
}
\]

Together with deterministic no-resurrection for complete compiler state, the experiments support

\[
\boxed{
\text{observed forgetting}
\ne
\text{destruction of structure}.
}
\]

A hardware image of a mathematical presentation is therefore more faithfully described by a trajectory of observer-induced partitions than by a single scalar resource value.

## References

1. Ingo Wegener. Branching Programs and Binary Decision Diagrams: Theory and Applications. SIAM, 2000. DOI 10.1137/1.9780898719789.
2. Ingo Wegener. Time-space trade-offs for branching programs. Journal of Computer and System Sciences 32(1), 1986, 91-96. DOI 10.1016/0022-0000(86)90004-8.
3. Randal E. Bryant. Graph-Based Algorithms for Boolean Function Manipulation. IEEE Transactions on Computers C-35(8), 1986, 677-691. DOI 10.1109/TC.1986.1676819.
4. Amir Pnueli, Michael Siegel, Eli Singerman. Translation Validation. TACAS 1998, 151-166. DOI 10.1007/BFb0054170.
5. George C. Necula. Translation Validation for an Optimizing Compiler. PLDI 2000, 83-94. DOI 10.1145/349299.349314.
6. Xavier Leroy. Formal Verification of a Realistic Compiler. Communications of the ACM 52(7), 2009, 107-115. DOI 10.1145/1538788.1538814.
7. Ross Tate, Michael Stepp, Zachary Tatlock, Sorin Lerner. Equality Saturation: A New Approach to Optimization. POPL 2009, 264-276. DOI 10.1145/1480881.1480915.
8. Clifford Wolf, Johann Glaser. Yosys - A Free Verilog Synthesis Suite. Austrochip 2013, 47-52.
9. Robert K. Brayton, Alan Mishchenko. ABC: An Academic Industrial-Strength Verification Tool. CAV 2010, 24-40. DOI 10.1007/978-3-642-14295-6_5.


## Appendix A. Position of H19 in the HATTER-SOL programme

HATTER-SOL is the research series “Tea Parties in the Additive-Multiplicative World with Hatter Sol.”

Programme author: Malachevsky, A.A. / Alex Malachevsky.  
ORCID: 0009-0008-6009-3196.  
Programme repository: https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL

Main research folders:

1. HATTER-SOL-01 - NUMBER-LINE-OBSERVER-TWO-OPERATIONS.
2. HATTER-SOL-02 - TWO-TEAPOTS-ONE-CUP.
3. HATTER-SOL-03 - CUP-ASKS-ITSELF.
4. HATTER-SOL-04 - RADICAL-PREDECESSOR.
5. HATTER-SOL-05 - MISSING-GUEST.
6. HATTER-SOL-06 - ORBITWISE-SURVIVAL.
7. HATTER-SOL-07 - FREE-PORT-FACTORIZATION.
8. HATTER-SOL-08 - DIMENSIONAL-FACTOR-ARCHITECTURES.
9. HATTER-SOL-09 - WORLD-INTERFACE-OPERATORS.
10. HATTER-SOL-10 - IDEAL-FACTOR-NETWORKS.
11. HATTER-SOL-11 - ORBITAL-PORT-FILTRATIONS.
12. HATTER-SOL-12 - OBSERVER-WORLD-STRUCTURAL-MEMORY.
13. HATTER-SOL-13 - UNBOUNDED-WORLD-DIVERSITY.
14. HATTER-SOL-14 - GALOIS-EQUIVARIANT-CARRIERS.
15. HATTER-SOL-15 - NONABELIAN-TWO-PORT-DIHEDRAL.
16. HATTER-SOL-16 - NONSOLVABLE-PORTS.
17. HATTER-SOL-17 - NONABELIAN-TOMOGRAPHY-HARDWARE.
18. HATTER-SOL-18 - ADAPTIVE-WORD-TOMOGRAPHY.
19. HATTER-SOL-19 - BOOLEAN-GEOMETRY-OF-MATHEMATICAL-PRESENTATIONS.

The repository also contains the parallel HATTER-SOL-18-HOLONOMY-AUTHENTICATION folder and an HATTER-SOL-08--10 research map.

The direct experimental lineage of the present paper is HATTER-SOL-16 -> HATTER-SOL-17 -> HATTER-SOL-18 -> HATTER-SOL-19: nonsolvable observer family -> hardware tomography -> adaptive word tomography -> observer-dependent compiler/FPGA presentation geometry.
