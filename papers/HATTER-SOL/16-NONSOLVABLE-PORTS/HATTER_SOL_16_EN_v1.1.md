# HATTER-SOL-16

## Beyond the Dihedral Lab: Engineering Non-Abelian Port Tomography in A5 and PSL(2,7)

**Version:** 1.1 publication candidate, referee-integration release  
**Series:** HATTER-SOL · Arithmetic Tea Party  
**Author:** Malachevsky, A.A.  
**ORCID:** 0009-0008-6009-3196  
**AI research collaborator:** Commander Sol / Hatter Sol  
**Series DOI:** 10.5281/zenodo.17996774  
**Date:** 16 September 2026

---

## Abstract

This paper turns the nonsolvable-port program into a finite engineering calculation. Two simple-group laboratories are solved exactly: `A5` and `PSL(2,7)`. In `A5`, complete generating-pair enumeration and a real three-dimensional irreducible representation give exact commutator-class tomography and a globally separated scalar Mahler observer for every `mu >= 4`. In `PSL(2,7)`, a complex three-dimensional irreducible representation still separates all conjugacy classes, but an orientation-even scalar determinant/Mahler quotient collapses the split order-seven classes. The lost datum is recovered by one signed length-four commutator quadrature. Finally, all 114 simultaneous-conjugacy orbits of generating pairs in `PSL(2,7)` are reconstructed from the five probes

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad[A,B],
\]

with maximum word depth four. No subfamily of at most four probes from the complete depth-at-most-four trace-word family separates all 114 orbits. If the interface is restricted to balanced closed loops, exact reconstruction depth rises to fourteen. Version 1.1 makes the observer definitions, enumeration conventions, determinant-phase proof and certificate identities explicit. The result is an engineering specification; fixed-point, HDL, synthesis and physical implementation are delegated to HATTER-SOL-17.

**Keywords:** finite simple groups; non-Abelian ports; tomography; commutator holonomy; Mahler measure; `A5`; `PSL(2,7)`; representation channels; engineering specification.

---

# 1. Engineering problem and exact observer definitions

Let `G` be a finite group and `(A,B)` an ordered generating pair. We identify pairs under simultaneous conjugation,

\[
(A,B)\sim(hAh^{-1},hBh^{-1}).
\]

For a unitary representation

\[
\rho:G\to U(d),
\]

define the Hermitian two-port operator

\[
H_{A,B}(\theta,\phi)=
 e^{i\theta}\rho(A)+e^{-i\theta}\rho(A)^{-1}
 +e^{i\phi}\rho(B)+e^{-i\phi}\rho(B)^{-1}.
\]

For every integer `n >= 0`, the normalized torus moment is

\[
\boxed{
S_n(A,B)=\frac1{(2\pi)^2}
\int_0^{2\pi}\!\int_0^{2\pi}
\operatorname{Tr}\bigl(H_{A,B}(\theta,\phi)^n\bigr)
\,d\theta\,d\phi.
}
\]

The engineering problem is to recover the simultaneous-conjugacy orbit of `(A,B)` from a bounded family of externally addressable port words and a finite representation readout.

Put

\[
K=[A,B]=ABA^{-1}B^{-1}.
\]

## Theorem 1. Universal fourth torus moment

For every finite-dimensional unitary representation,

\[
\boxed{
S_4(A,B)=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1}).
}
\]

For a real three-dimensional representation,

\[
S_4=84+4\chi(K)+4\chi(K^{-1}),
\]

and when the character is inversion-invariant, as in the real `A5` channel below,

\[
\boxed{S_4=84+8\chi_3(K).}
\]

### Proof

Torus averaging kills every monomial with nonzero total exponent in `A` or `B`. At length four, six balanced pure-`A` words contribute the identity and six balanced pure-`B` words contribute the identity. The mixed balanced sector consists of all `4!=24` orderings of

\[
A,\ A^{-1},\ B,\ B^{-1}.
\]

Under cyclicity of trace, sixteen of them contribute the identity, four contribute `K`, and four contribute `K^{-1}`. Hence the identity coefficient is

\[
6+6+16=28,
\]

which proves the formula. `□`

This is the first closed-word location at which genuinely non-Abelian information can appear.

---

# 2. The A5 laboratory

## 2.1 Exact generating-pair enumeration

Complete exact enumeration gives

\[
|A_5|=60,
\qquad 2280\text{ ordered generating pairs},
\qquad 38\text{ simultaneous-conjugacy orbits}.
\]

For a generating pair `(A,B)`, the common centralizer is

\[
C_{A_5}(A)\cap C_{A_5}(B)=C_{A_5}(\langle A,B\rangle)=Z(A_5)=1.
\]

Therefore every simultaneous-conjugacy orbit has size `60`, and `2280/60=38`.

Generating commutators occur only in

\[
3A,\qquad5A,\qquad5B,
\]

with orbit counts

\[
18,\qquad10,\qquad10.
\]

## 2.2 The real 3D class channel

Choose the standard real three-dimensional irreducible character

\[
\chi_3=(3,-1,0,\varphi,\varphi'),
\qquad
\varphi=\frac{1+\sqrt5}{2},
\quad
\varphi'=\frac{1-\sqrt5}{2}.
\]

| class | `1A` | `2A` | `3A` | `5A` | `5B` |
|---|---:|---:|---:|---:|---:|
| `chi_3` | `3` | `-1` | `0` | `phi` | `phi'` |

The values are pairwise distinct; one real trace therefore determines the conjugacy class.

For the corresponding orientation-preserving 3D representation, the eigenvalue multiset is invariant under inversion and has determinant one. Hence

\[
\boxed{
P_g(T)=\det(I-\rho_3(g)T)
=1-\chi_3(g)T+\chi_3(g)T^2-T^3.
}
\]

The coefficient of `T^2` equals `Tr rho_3(g)^{-1}=chi_3(g)` in this real orthogonal determinant-one representation.

---

# 3. The A5 scalar Mahler observer

For `mu >= 4`, define

\[
\boxed{
M_{A,B}(\mu)=\frac1{(2\pi)^2}
\int_0^{2\pi}\!\int_0^{2\pi}
\log\det\bigl(\mu I-H_{A,B}(\theta,\phi)\bigr)
\,d\theta\,d\phi.
}
\]

The certified spectral gap at `mu=4` keeps the determinant positive and makes the logarithm and moment expansion uniformly well-defined over the full natural range `mu >= 4`.

For a commutator class `C`, define the finite response set

\[
\boxed{
\mathcal M_C(\mu)=
\{M_{A,B}(\mu):\langle A,B\rangle=A_5,\ [A,B]\in C\}.
}
\]

This notation removes an ambiguity of earlier drafts: a commutator class can contain several exact determinant/Mahler types.

## Theorem 2. Global A5 class separation

For every `mu >= 4`,

\[
\boxed{
\sup\mathcal M_{5A}(\mu)<\inf\mathcal M_{3A}(\mu),
\qquad
\sup\mathcal M_{3A}(\mu)<\inf\mathcal M_{5B}(\mu).
}
\]

Equivalently, every `5A` type lies below every `3A` type, and every `3A` type lies below every `5B` type.

### Certified proof architecture

The 38 generating-pair orbits reduce to fourteen exact determinant/Mahler types: four in `5A`, six in `3A`, and four in `5B`.

1. Exact moments through order 40 over `Q(sqrt(5))` and a rational tail bound prove the ordering for
   \[
   \mu\ge\frac{23}{5}.
   \]
2. A typewise tensor-Cayley spectral-gap certificate supplies a positive lower gap for each of the fourteen types; the weakest certified value is `gamma > 1/5`.
3. Outward-rounded interval quadrature proves the strict ordering at the boundary `mu=4`.
4. Define
   \[
   G(\mu)=M(\mu)-3\log\mu+\frac6{\mu^2}.
   \]
   Torus balancing kills all odd moments, exact computation gives `S_2=12`, and Hermiticity gives
   \[
   S_{2m}=\langle\operatorname{Tr}H^{2m}\rangle\ge0.
   \]
   Therefore
   \[
   G(\mu)=-\sum_{m\ge2}\frac{S_{2m}}{2m\mu^{2m}},
   \qquad
   \boxed{
   G'(\mu)=\sum_{m\ge2}\frac{S_{2m}}{\mu^{2m+1}}\ge0.
   }
   \]
5. Sixty rational slabs of width `1/100` cover `[4,23/5]`. Monotonicity reduces every slab to two certified endpoint inequalities. Together with the large-`mu` theorem, this closes every `mu >= 4`.

Thus the H15 scalar-tomography conclusion survives in `A5`, although the proof mechanism changes from first-harmonic dominance to

\[
\boxed{
\text{3D irrep}\to\text{length-4 commutator trace}
\to\text{tensor spectral gap}
\to\text{global determinant separation}.
}
\]

---

# 4. The PSL(2,7) laboratory

Realize

\[
G=PSL(2,7),\qquad |G|=168,
\]

in its faithful action on `P^1(F_7)`.

Complete exact enumeration gives

\[
19152\text{ ordered generating pairs}
\]

and

\[
\boxed{114}
\]

simultaneous-conjugacy orbits. Again a generating pair has common centralizer equal to `Z(G)=1`, so each orbit has size `168` and `19152/168=114`.

The six conjugacy classes have sizes

\[
1,21,56,42,24,24
\]

for

\[
1A,2A,3A,4A,7A,7B.
\]

Generating commutator orbit counts are

\[
\boxed{
36\times3A,\quad64\times4A,\quad7\times7A,\quad7\times7B.
}
\]

Choose one complex three-dimensional irreducible character:

\[
\chi_3=
\left(
3,-1,0,1,
\frac{-1+i\sqrt7}{2},
\frac{-1-i\sqrt7}{2}
\right).
\]

| class | `1A` | `2A` | `3A` | `4A` | `7A` | `7B` |
|---|---:|---:|---:|---:|---:|---:|
| `chi_3` | `3` | `-1` | `0` | `1` | `(-1+i√7)/2` | `(-1-i√7)/2` |

All six values are distinct, so one complex 3D trace separates every class.

---

# 5. Exact scalar type and the 7A/7B collapse

For a generating pair define the Laurent determinant polynomial at the boundary parameter `mu=4` by

\[
D_{A,B}(z,w)=\det\!\left(
4I-z\rho(A)-z^{-1}\rho(A)^{-1}
-w\rho(B)-w^{-1}\rho(B)^{-1}
\right).
\]

Two determinant polynomials are assigned the same **scalar determinant/Mahler type** when they are related by the torus-measure-preserving symmetries used by the exact certificate:

\[
(z,w)\mapsto(z^{\pm1},w^{\pm1}),
\qquad
(z,w)\mapsto(w,z),
\]

followed by exact Laurent-polynomial equality. Let

\[
\boxed{
\mathcal T_C=\{
[D_{A,B}]:\langle A,B\rangle=PSL(2,7),\ [A,B]\in C
\}.
}
\]

Exact finite classification gives

\[
|\mathcal T_{3A}|=6,\qquad
|\mathcal T_{4A}|=12,\qquad
|\mathcal T_{7A}|=|\mathcal T_{7B}|=3,
\]

and, critically,

\[
\boxed{\mathcal T_{7A}=\mathcal T_{7B}.}
\]

This is not a failure of the complex 3D representation. It is a loss caused by orientation-even scalarization.

A projective matrix of nonsquare determinant in `PGL(2,7)` induces an outer automorphism `alpha` satisfying

\[
7A\leftrightarrow7B,
\qquad
\boxed{
\chi_3(\alpha(g))=\overline{\chi_3(g)}.
}
\]

Therefore every real scalar class observer invariant under this outer orientation reversal must merge the split order-seven pair.

---

# 6. Minimal oriented closed-loop channel

Define

\[
\boxed{
Q_4(A,B)=
\frac{\operatorname{Tr}\rho_3([A,B])-
\operatorname{Tr}\rho_3([A,B]^{-1})}{i\sqrt7}.
}
\]

## Theorem 3. Exact orientation bit

For every generating pair in `PSL(2,7)`,

\[
Q_4(A,B)=
\begin{cases}
0,&[A,B]\in3A\cup4A,\\
+1,&[A,B]\in7A,\\
-1,&[A,B]\in7B.
\end{cases}
\]

### Proof

For `7A`,

\[
\chi_3(K)=\frac{-1+i\sqrt7}{2},
\qquad
\chi_3(K^{-1})=\frac{-1-i\sqrt7}{2},
\]

so their difference is `i sqrt(7)`. The sign reverses on `7B`; the `3A` and `4A` values are real. `□`

No nonempty freely reduced balanced word can have length below four: balancing requires at least one occurrence of each of `A,A^{-1},B,B^{-1}`. Thus length four is the first possible closed-loop depth.

## Lemma 3.1. Determinant-phase sign

Let

\[
P_K(t)=\det(I-t\rho_3(K)),\qquad 0<t<1.
\]

For `K in 7A`,

\[
P_{7A}(t)=R(t)-i\frac{\sqrt7}{2}t(1+t),
\]

while for `K in 7B`,

\[
P_{7B}(t)=R(t)+i\frac{\sqrt7}{2}t(1+t),
\]

where

\[
R(t)=(1-t)\left(1+\frac32t+t^2\right)>0.
\]

Hence, for every `0<t<1`,

\[
\boxed{
\operatorname{Im}P_{7A}(t)<0,
\qquad
\operatorname{Im}P_{7B}(t)>0.
}
\]

The orientation bit is therefore measurable by one signed determinant-phase quadrature.

---

# 7. Complete generating-pair tomography

Let the free alphabet be

\[
\{A,a,B,b\},
\qquad a=A^{-1},\quad b=B^{-1}.
\]

For a word `w`, first perform free reduction, then cyclic reduction. For trace tomography we identify a reduced word with every cyclic rotation and with the inverse word, because

\[
\operatorname{Tr}\rho(x_1\cdots x_m)
\]

is cyclically invariant and the chosen class channel treats the inverse convention explicitly. Let `W_{<=L}` denote the canonical representatives of all nonempty cyclically reduced trace words of length at most `L` under these equivalences.

The exact generator used by the certificate produces

\[
\boxed{|W_{\le4}|=25.}
\]

For all 114 generating-pair orbits, the cumulative signature counts are

\[
\boxed{
|\Sigma_{\le1}|=24,
\quad
|\Sigma_{\le2}|=107,
\quad
|\Sigma_{\le3}|=107,
\quad
|\Sigma_{\le4}|=114.
}
\]

## Theorem 4. Exact short-word depth and five-probe signature

Trace depth four is necessary and sufficient for complete generating-pair orbit reconstruction. The five probes

\[
\boxed{
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad[A,B]
}
\]

already separate all 114 simultaneous-conjugacy orbits.

Moreover, the certificate exhausts every subset of `W_{<=4}` of sizes one, two, three and four. None of them separates all 114 orbits. Therefore

\[
\boxed{
5\text{ probes are minimal inside the complete depth-}\le4\text{ trace-word family}.
}
\]

This is a finite-interface minimality statement, not an absolute lower bound over every imaginable nonlinear measurement scheme.

---

# 8. Closed-loop-only cost

A word is **balanced** when

\[
\exp_A(w)=0,
\qquad
\exp_B(w)=0.
\]

The exact numbers of new canonical balanced words at lengths

\[
4,6,8,10,12,14
\]

are

\[
\boxed{1,2,14,76,505,3386},
\]

for a cumulative total of `3984` words through depth 14.

The corresponding cumulative numbers of distinguished generating-pair orbits are

\[
\boxed{4,22,98,110,112,114}.
\]

## Theorem 5. Exact balanced depth

Balanced closed-loop trace tomography has exact reconstruction depth

\[
\boxed{14}.
\]

Depth at most twelve leaves two nontrivial collisions; depth fourteen separates all 114 orbits.

One certified sufficient eight-probe balanced signature is represented by the canonical words

```text
AABBaabb
AAABAbabbaBaaB
AAbABaBBBabbab
AABBAbababaB
AAAABabaBabbaB
AABabaBAAbaBab
ABBAbaBBabbb
ABABABaBabbabb
```

where lowercase letters denote inverse ports. Minimality of the number eight is not claimed.

---

# 9. Frozen engineering specification for H17

H16 freezes the preferred mixed-word processor as

\[
\boxed{
\text{PORT WORD ENGINE}
\longrightarrow
\text{ORIENTED 3D CHANNEL}
\longrightarrow
\text{5-PROBE SIGNATURE}
\longrightarrow
\text{114-ORBIT DECODER}.
}
\]

The word engine evaluates

\[
A,\qquad B,\qquad AB,\qquad AB^{-1},\qquad ABA^{-1}B^{-1}.
\]

Maximum primitive word depth is four. The `7A/7B` split requires one signed orientation component, realizable as `I/Q`, as the antisymmetric trace quadrature `Q_4`, or as the sign of the determinant phase above.

What is proved in H16 is exact arithmetic separation. It does **not** yet prove robustness under quantization, fixed-point rounding, analog noise, dropped measurements or timing faults. The 114-state decoder is exact under error-free probe values. H17 must establish margins, bit widths, redundancy and hardware fault behavior before any physical-performance claim is made.

---

# 10. Arithmetic bridge and claim boundary

For a finite Galois extension and an unramified place `v`, the local Artin factor has the representation-theoretic form

\[
L_v(T,\rho)=\det(I-\rho(\operatorname{Frob}_v)T)^{-1}.
\]

In `A5`, one real 3D local factor separates all classes. In `PSL(2,7)`, one complex 3D local factor also separates all classes and retains the `7A/7B` orientation lost by orientation-even scalarization.

This is a local representation-theoretic Artin bridge. No general automorphy theorem is asserted.

H16 proves finite information budgets for two explicit simple groups. It does not claim that the same five words solve arbitrary finite groups, arbitrary networks or unknown topologies, and it makes no cryptographic-security, PUF or physical-unclonability claim.

---

# 11. Reproducibility and certificate identities

All finite-group enumerations use exact permutation arithmetic. Algebraic character calculations use exact arithmetic over `Q(sqrt(5))` or `Q(i sqrt(7))`. The A5 boundary and compact-strip Mahler certificates combine exact algebraic construction with outward-rounded interval arithmetic.

The authoritative branch is

`research/hatter-sol-16-nonsolvable-ports`.

The principal certificate files and their Git content identities are:

| certificate | principal claim | Git blob SHA |
|---|---|---|
| `a5_generating_pair_commutator_certificate.py` | 2280 pairs, 38 orbits, 18/10/10 commutator split | `0198ca2abecb2a6a8082d69150d7b057a5e5da74` |
| `a5_mahler_separation_mu_23_over_5_certificate.py` | exact `mu >= 23/5` Mahler separation | `987ffe58a79bcd9a6ea63af249efaec701cb1388` |
| `a5_uniform_spectral_gap_diameter_certificate.py` | uniform boundary spectral gap | `5d0bf981afb7d793cd9d8f5e6b804f01dc90edd1` |
| `a5_type_tensor_gap_certificate.py` | exact typewise tensor gaps | `d6a4490086c2c24fc1dee1e1b2e472fe5f82a638` |
| `a5_boundary_mahler_mu4_interval_certificate.py` | strict class ordering at `mu=4` | `c7fa2446ec9132047be0b05a998904535556bd5e` |
| `a5_global_mahler_mu_ge_4_certificate.py` | compact-strip monotone closure | `7887cf1ff164a21f8399d05bcaa688a1092a8098` |
| `psl27_generating_pair_and_scalar_collapse_certificate.py` | 114 orbits and exact scalar `7A/7B` collapse | `6a0c4ae4bb28b84142b7989f156312107880a85f` |
| `psl27_outer_orientation_minimal_observer_certificate.py` | outer involution and oriented 3D separation | `4e615ca2b5a7bb1d81961986c95f27e845e6d10f` |
| `psl27_oriented_loop_spectral_observer_certificate.py` | `Q_4`, depth four, determinant-phase sign | `20882008268ef62293cf3e64af42fc2e7c6fbee2` |
| `psl27_pair_tomography_short_word_certificate.py` | 25-word family, five-probe minimality, balanced depth 14 | `a60113f99bc7a959bcbc6c9231d6b6c4893f8865` |

A release-level SHA-256 manifest accompanies the publication package. Git blob identities above are additionally listed because they bind each claim to the exact repository content. The reproduction command for every standalone script is

```bash
python <certificate-file>.py
```

and every certificate terminates with an explicit `PASS` assertion only after all exact or interval proof obligations succeed.

---

# 12. Annotated HATTER-SOL series bibliography

The complete preceding series is included because H16 is a cumulative engineering layer. DOI fields are given only where an installment DOI is already assigned.

**Series archive:** `10.5281/zenodo.17996774`.

**[01] HATTER-SOL-01. _A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations._** DOI `10.5281/zenodo.22639237`. Foundational note separating arithmetic structure from the observer and coordinate system used to represent it.

**[02] HATTER-SOL-02. _Two Teapots, One Cup: “Who Are You?” Among the Primes._** DOI `10.5281/zenodo.22656414`. Develops finite probe complexity for prime identification, exact congruence/quadratic-probe orbit counts and sparse rigidifying families.

**[03] HATTER-SOL-03. _The Cup That Asks Its Own Questions: Anonymous Probes, the Exact Predecessor of a Prime, and Recursive Rigidity._** DOI `10.5281/zenodo.22679521`. Replaces external labels by intrinsic relations and proves rigidity for the exact prime-predecessor structure.

**[04] HATTER-SOL-04. _The Cup Forgets Multiplicities: Radical Predecessor, the Multiplicity Tower, and the Cost of a Hypothetical Prime Symmetry._** Publication candidate; installment DOI pending deposit. Builds the multiplicity tower and proves strong constraints on any hypothetical symmetry without claiming the automorphism problem solved.

**[05] HATTER-SOL-05. _Who Is Missing from the Table? Empty Fibers, Exact-Support Spectra, and the Survival of the 3↔5 Transposition._** DOI `10.5281/zenodo.22718278`. Refines the symmetry problem through exact-support fibers and their cardinality/compactness constraints.

**[06] HATTER-SOL-06. _Orbitwise Survival Kernel._** Repository research layer; no separate installment DOI assigned. Localizes extension of a seed symmetry to the exact support-orbit data visible inside its causal cone.

**[07] HATTER-SOL-07. _Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting._** DOI `10.5281/zenodo.22724185`. Introduces the factor-as-node network model and its exact free-boundary law.

**[08] HATTER-SOL-08. _From a Line to Space: Dimensional Suppression of Factor-Architecture Sensitivity._** DOI `10.5281/zenodo.22744644`. Studies how path, planar and unrestricted carrier classes change factor-network sensitivity.

**[09] HATTER-SOL-09. _World-Dependent Factor Networks and a Prime-Toggle Response Operator._** DOI `10.5281/zenodo.22732435`. Composes arithmetic worlds with typed factor networks, Pareto responses and a prime-toggle hypercube/Laplacian.

**[10] HATTER-SOL-10. _Ideal Factor Networks Beyond Unique Element Factorization._** DOI `10.5281/zenodo.22734865`. Moves from element factorization to prime ideals and principalization witnesses, adding multistate nodes and exact phase transitions.

**[11] HATTER-SOL-11. _Orbital Port Filtrations: How Network Geometry Forgets Arithmetic Direction Data._** DOI `10.5281/zenodo.22746559`. Separates arithmetic, network and observational forgetting and quantifies a geometry-controlled `3→2→1` collapse.

**[12] HATTER-SOL-12. _Observer Laws, World Rotation, and Structural Memory of an Integer._** DOI `10.5281/zenodo.22747698`. Treats visibility as a joint function of integer, arithmetic world, carrier and observer; compares planar and toroidal resolving power.

**[13] HATTER-SOL-13. _A Fixed Integer Across Growing Arithmetic Worlds: Unbounded Structural Diversity and the Topological Cost of Erasure._** DOI `10.5281/zenodo.22754637`. Proves unbounded branching for a fixed integer in growing cyclotomic worlds and quantifies the genus cost of erasure.

**[14] HATTER-SOL-14. _Galois-Equivariant Carriers: Same Graph, Different Arithmetic Homology._** DOI `10.5281/zenodo.22757307`. Shows that the same abstract graph can carry different arithmetic regular actions with non-isomorphic equivariant homology.

**[15] HATTER-SOL-15. _Non-Abelian Ports: From Dihedral Commutator Holonomy to Universal Mahler Tomography._** Final release candidate v0.5; no installment DOI assigned as of this assembly. Builds the prime-dihedral two-port laboratory and proves universal first-harmonic dominance for the centered primitive Mahler observer; it is the direct mathematical parent of H16.

---

# 13. External references

1. Serre, J.-P. _Linear Representations of Finite Groups_. Springer.
2. Isaacs, I. M. _Character Theory of Finite Groups_. Dover / classical text.
3. Neukirch, J. _Algebraic Number Theory_. Springer.

---

# Conclusion

The passage from the prime-dihedral laboratory to finite simple groups changes the proof machinery but not the port principle. `A5` shows that global scalar determinant separation survives in a nonsolvable simple group. `PSL(2,7)` identifies the exact orientation information destroyed by a real scalar quotient and recovers it at the first possible balanced depth. Once the oriented 3D channel is retained, five trace probes of maximum word depth four reconstruct every one of the 114 generating-pair orbits.

\[
\boxed{
5\text{ oriented readouts}+\text{depth }4
\Longrightarrow
\text{complete pair-orbit tomography in }PSL(2,7).
}
\]

This is the frozen mathematical specification handed to HATTER-SOL-17 for reference software, golden vectors, fixed-point arithmetic, HDL, synthesis and physical-board validation.
