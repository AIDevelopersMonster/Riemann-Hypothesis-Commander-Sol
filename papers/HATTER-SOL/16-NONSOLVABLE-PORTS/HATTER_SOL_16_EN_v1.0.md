# HATTER-SOL-16

## Beyond the Dihedral Lab: Engineering Non-Abelian Port Tomography in A5 and PSL(2,7)

**Version:** 1.0 publication candidate  
**Series:** HATTER-SOL  
**Authors:** Commander Sol; Alexey Ivanov  
**ORCID:** 0009-0008-6009-3196  
**Series DOI:** 10.5281/zenodo.17996774

## Abstract

This paper turns the nonsolvable-port program into an engineering calculation. Two finite simple laboratories are solved exactly: `A5` and `PSL(2,7)`. In `A5`, complete generating-pair enumeration and a real three-dimensional irreducible representation give exact commutator-class tomography and a globally separated scalar Mahler observer for every `mu >= 4`. In `PSL(2,7)`, a complex three-dimensional irreducible representation still separates all conjugacy classes, but an orientation-even scalar Mahler quotient collapses the split order-seven classes. The missing datum is recovered by one signed length-four commutator quadrature. Finally, all 114 simultaneous-conjugacy orbits of generating pairs in `PSL(2,7)` are reconstructed from the five probes

\[
A,\quad B,\quad AB,\quad AB^{-1},\quad[A,B],
\]

with maximum word depth four. No four-probe subfamily from the complete depth-at-most-four candidate family suffices. If the interface is restricted to balanced closed loops, exact reconstruction depth rises to fourteen. The result is a finite engineering specification handed to HATTER-SOL-17 for software, HDL, synthesis and physical implementation.

---

## 1. Two-port observer

Let `G` be a finite group, `(A,B)` an ordered generating pair, and

\[
\rho:G\to U(d)
\]

a unitary representation. Define

\[
H_{A,B}(\theta,\phi)=e^{i\theta}\rho(A)+e^{-i\theta}\rho(A)^{-1}
+e^{i\phi}\rho(B)+e^{-i\phi}\rho(B)^{-1}.
\]

Pairs are identified up to simultaneous conjugacy. The engineering problem is to recover the orbit of `(A,B)` from a bounded set of externally addressable port words.

The first non-Abelian closed-word contribution occurs at

\[
K=[A,B]=ABA^{-1}B^{-1}.
\]

### Theorem 1. Universal fourth torus moment

For every finite-dimensional unitary representation,

\[
\boxed{
S_4=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1}).
}
\]

For the real three-dimensional `A5` representation,

\[
\boxed{S_4=84+8\chi_3(K).}
\]

The identity follows by exact enumeration of balanced words of length four: 28 identity contributions, 4 copies of `K`, and 4 copies of `K^{-1}` under cyclic trace.

---

## 2. A5 laboratory

Complete exact enumeration gives

\[
|A_5|=60,
\qquad 2280\text{ ordered generating pairs},
\qquad 38\text{ simultaneous-conjugacy orbits}.
\]

Generating commutators occur only in

\[
3A,\ 5A,\ 5B,
\]

with orbit counts

\[
18,\ 10,\ 10.
\]

A real 3D irreducible character is

\[
\chi_3=(3,-1,0,\varphi,\varphi'),
\qquad
\varphi=\frac{1+\sqrt5}{2},\quad
\varphi'=\frac{1-\sqrt5}{2}.
\]

Its five values are distinct. Hence one 3D trace, and equivalently

\[
P_g(T)=\det(I-\rho_3(g)T)
=1-\chi_3(g)T+\chi_3(g)T^2-T^3,
\]

separates all `A5` conjugacy classes.

For

\[
M_{A,B}(\mu)=\frac1{(2\pi)^2}\iint\log\det(\mu I-H_{A,B})\,d\theta\,d\phi,
\qquad \mu\ge4,
\]

exact moment computation, tensor spectral gaps, interval quadrature and a monotone normalized observer give the following global theorem.

### Theorem 2. Global A5 Mahler separation

For every generating pair and every `mu >= 4`,

\[
\boxed{
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu).
}
\]

Thus the H15 conclusion survives beyond the dihedral case, although the proof mechanism changes from first-harmonic dominance to

\[
\boxed{
\text{3D irrep}\to\text{length-4 commutator trace}
\to\text{tensor spectral gap}\to\text{global determinant separation}.
}
\]

---

## 3. PSL(2,7) laboratory

Realize

\[
G=PSL(2,7),\qquad |G|=168,
\]

in the projective-line action over `F_7`. Exact enumeration gives

\[
19152\text{ ordered generating pairs}
\]

and

\[
\boxed{114}
\]

simultaneous-conjugacy orbits. Generating commutator orbit counts are

\[
36\times3A,\quad64\times4A,\quad7\times7A,\quad7\times7B.
\]

A complex 3D irreducible character is

\[
\chi_3=
\left(3,-1,0,1,
\frac{-1+i\sqrt7}{2},
\frac{-1-i\sqrt7}{2}
\right),
\]

so one complex trace separates all six classes.

The orientation-even scalar Mahler quotient does not: exact determinant classification gives identical scalar type sets

\[
\boxed{\mathcal T_{7A}=\mathcal T_{7B}.}
\]

The cause is the outer involution from `PGL(2,7)`, which exchanges `7A` and `7B` and sends

\[
\chi_3(g)\mapsto\overline{\chi_3(g)}.
\]

---

## 4. Oriented length-four channel

Define

\[
Q_4(A,B)=
\frac{\operatorname{Tr}\rho_3([A,B])-
\operatorname{Tr}\rho_3([A,B]^{-1})}{i\sqrt7}.
\]

### Theorem 3. Exact orientation bit

For every generating pair in `PSL(2,7)`,

\[
Q_4=
\begin{cases}
0,&[A,B]\in3A\cup4A,\\
+1,&[A,B]\in7A,\\
-1,&[A,B]\in7B.
\end{cases}
\]

No nonempty freely reduced balanced word exists below length four, so the orientation bit appears at the first possible closed-loop depth.

The same information is visible in

\[
P_K(t)=\det(I-t\rho_3(K)).
\]

For `0<t<1`, the `7A` and `7B` determinant phases have equal magnitude and opposite signs. Therefore one signed quadrature is sufficient; a large vector observer is not required.

---

## 5. Complete generating-pair tomography

For all cyclically reduced oriented trace words of maximal lengths 1, 2, 3, 4, the exact numbers of distinguished pair orbits are

\[
\boxed{24,\ 107,\ 107,\ 114}.
\]

### Theorem 4. Exact short-word depth and five-probe signature

Trace depth four is necessary and sufficient to reconstruct every generating-pair orbit. The five probes

\[
\boxed{A,\ B,\ AB,\ AB^{-1},\ [A,B]}
\]

already separate all 114 orbits.

Moreover, exhaustive testing of the complete depth-at-most-four candidate family proves that no subfamily of at most four probes separates all 114 orbits. Thus five probes are minimal inside this natural short-word family.

This is the principal engineering result of H16.

---

## 6. Closed-loop-only cost

If every probe must be balanced,

\[
\exp_A(w)=\exp_B(w)=0,
\]

the cumulative numbers of distinguished orbits at maximal depths

\[
4,6,8,10,12,14
\]

are

\[
\boxed{4,22,98,110,112,114}.
\]

### Theorem 5. Exact balanced depth

Balanced closed-loop tomography has exact reconstruction depth

\[
\boxed{14}.
\]

A certified eight-probe balanced signature with maximum depth fourteen is given in the repository. Its size is sufficient, not claimed minimal.

---

## 7. Engineering specification for H17

H16 freezes the preferred mixed-word processor as

\[
\boxed{
\text{PORT WORD ENGINE}
\to
\text{ORIENTED 3D CHANNEL}
\to
\text{5-PROBE SIGNATURE}
\to
\text{114-ORBIT DECODER}.
}
\]

The required words are

\[
A,\ B,\ AB,\ AB^{-1},\ ABA^{-1}B^{-1}.
\]

Maximum primitive word depth is four. The order-seven split requires one signed orientation component, realizable as a complex-trace quadrature, `I/Q`, or determinant-phase sign.

H16 does not choose the final hardware representation. `PSL(2,7)` may be encoded as projective-line permutations, group-element LUT entries, explicit 3D matrices, or a hybrid. H17 must choose bit widths, fixed-point format, timing, memory layout and redundancy.

---

## 8. Arithmetic bridge

For a finite Galois extension and an unramified place,

\[
L_v(T,\rho)=\det(I-\rho(\operatorname{Frob}_v)T)^{-1}.
\]

In `A5`, one real 3D local factor separates all classes. In `PSL(2,7)`, one complex 3D local factor also separates all classes and retains the `7A/7B` orientation lost by real scalarization.

This is a representation-theoretic Artin statement only. No general automorphy claim is made.

---

## 9. Reproducibility and claim boundary

All principal claims are backed by exact finite certificates in `certificates/`. Group enumerations use exact permutation arithmetic. Algebraic computations use `Q(sqrt(5))` or `Q(i sqrt(7))`; Mahler certification uses exact construction plus outward-rounded interval bounds.

The publication-authoritative correction sheet is `FINAL_CORRECTIONS_v1.0.md`.

The paper proves finite information budgets for two explicit simple groups. It does not claim the same five-word signature for arbitrary groups or unknown networks, and it does not establish hardware noise tolerance, erasure resilience, cryptographic security or physical unclonability.

---

## Conclusion

The nonsolvable extension is now an engineering specification. `A5` shows that global scalar determinant separation survives beyond the dihedral laboratory. `PSL(2,7)` shows exactly where orientation-even scalarization fails and how one signed quadrature repairs it. With orientation preserved, five readouts of maximum word depth four reconstruct all 114 generating-pair orbits:

\[
\boxed{
5\text{ oriented readouts}+\text{depth }4
\Longrightarrow
\text{complete pair-orbit tomography in }PSL(2,7).
}
\]

HATTER-SOL-17 begins from this frozen specification and moves to reference software, golden vectors, fixed-point arithmetic, HDL, synthesis and physical hardware tests.

## References

1. J.-P. Serre, *Linear Representations of Finite Groups*, Springer.
2. J. Neukirch, *Algebraic Number Theory*, Springer.
3. HATTER-SOL series archive, DOI 10.5281/zenodo.17996774.
4. Exact H16 theorem layers and certificates in the project repository.
