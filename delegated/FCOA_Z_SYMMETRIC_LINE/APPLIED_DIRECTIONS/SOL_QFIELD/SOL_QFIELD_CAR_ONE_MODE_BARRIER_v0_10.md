# SOL-QFIELD — One-Mode CAR Closure and the Two-Mode Matrix Barrier

**Version:** 0.10  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** TENTH TARGET COMPLETE / EXACT ONE-MODE CAR COPY / TWO-MODE NO-GO IN CURRENT HISTORY ALGEBRA  
**Depends on:** `SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md`

---

## 1. Executive verdict

Version 0.9 proved that two independently generated native root-comb route contrasts give self-adjoint elements

\[
Q_x,Q_y\in J_\Delta\cong M_2(\mathbb C)
\tag{1}
\]

satisfying

\[
Q_x^2=Q_y^2=e_{\rm std},
\qquad
Q_xQ_y+Q_yQ_x=0.
\tag{2}
\]

Define

\[
\boxed{
c:=\frac12(Q_x+iQ_y),
\qquad
c^*:=\frac12(Q_x-iQ_y).
}
\tag{3}
\]

Then the native Clifford relations imply exactly

\[
\boxed{
c^2=0,
\qquad
(c^*)^2=0,
\qquad
cc^*+c^*c=e_{\rm std}.
}
\tag{4}
\]

Thus the order-sensitive history sector contains an exact algebraic copy of the **one-mode complex CAR algebra**.

More strongly,

\[
\boxed{
C^*(c,c^*)=J_\Delta\cong M_2(\mathbb C).
}
\tag{5}
\]

The associated number projection

\[
N:=c^*c
\tag{6}
\]

is rank one and satisfies

\[
N^2=N,
\qquad
cc^*=e_{\rm std}-N.
\tag{7}
\]

However, the same theorem chain also gives a strict obstruction:

\[
\boxed{
\text{the current }\mathbb C[S_3]\text{ history algebra cannot contain two independent CAR modes.}
}
\tag{8}
\]

Two complex fermionic modes generate the universal finite CAR algebra

\[
\operatorname{CAR}_2\cong M_4(\mathbb C),
\tag{9}
\]

whereas

\[
\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C)
\tag{10}
\]

has no \(M_4(\mathbb C)\) simple block and dimension only six.

Hence the present FCOA history construction reaches exactly one algebraic mode and then hits a matrix-size wall.

This is an algebraic CAR result only. It does **not** derive physical fermions, fermionic statistics, Fock-space locality, a Hamiltonian, or QFT.

---

## 2. Input theorem: the native Clifford pair

From v0.9,

\[
Q_x^*=Q_x,
\qquad
Q_y^*=Q_y,
\tag{11}
\]

and

\[
Q_x^2=Q_y^2=e_{\rm std},
\qquad
\{Q_x,Q_y\}=0.
\tag{12}
\]

Here \(e_{\rm std}\) is the identity of the native order-sensitive ideal

\[
J_\Delta=Ae_{\rm std}\cong M_2(\mathbb C),
\qquad
A=\mathbb C[S_3].
\tag{13}
\]

The operators \(Q_x,Q_y\) were not inserted as Pauli matrices by hand. They arose from two distinct native reconvergence contrasts at root-history depths two and three.

---

## 3. Theorem A — exact one-mode CAR relations

### Theorem 3.1 — Native CAR closure

Let \(c,c^*\) be defined by (3). Then

\[
\boxed{
c^2=(c^*)^2=0}
\tag{14}
\]

and

\[
\boxed{cc^*+c^*c=e_{\rm std}.}
\tag{15}
\]

### Proof

Using (12),

\[
\begin{aligned}
c^2
&=\frac14(Q_x+iQ_y)^2\\
&=\frac14\left(Q_x^2-Q_y^2+i(Q_xQ_y+Q_yQ_x)\right)\\
&=0.
\end{aligned}
\tag{16}
\]

Taking adjoints gives

\[
(c^*)^2=0.
\tag{17}
\]

Also

\[
\begin{aligned}
cc^*+c^*c
&=\frac14\Big((Q_x+iQ_y)(Q_x-iQ_y)\\
&\qquad +(Q_x-iQ_y)(Q_x+iQ_y)\Big)\\
&=\frac12(Q_x^2+Q_y^2)\\
&=e_{\rm std}.
\end{aligned}
\tag{18}
\]

Thus the one-mode CAR relations hold exactly. \(\square\)

### Corollary 3.2 — The CAR generators recover the Clifford pair

\[
\boxed{
Q_x=c+c^*,
\qquad
Q_y=-i(c-c^*).
}
\tag{19}
\]

Therefore

\[
\boxed{
C^*(c,c^*)=C^*(Q_x,Q_y)=J_\Delta\cong M_2(\mathbb C).
}
\tag{20}
\]

So the CAR algebra is not a proper subalgebra accidentally sitting inside the order block; it is the entire block.

---

## 4. The number projection

Define

\[
N:=c^*c.
\tag{21}
\]

### Proposition 4.1

\[
\boxed{
N^*=N,
\qquad
N^2=N.
}
\tag{22}
\]

### Proof

Self-adjointness is immediate. Using the CAR relation,

\[
\begin{aligned}
N^2
&=c^*cc^*c\\
&=c^*(e_{\rm std}-c^*c)c\\
&=c^*c-c^*(c^*)c c\\
&=c^*c=N,
\end{aligned}
\tag{23}
\]

because \((c^*)^2=c^2=0\). \(\square\)

Likewise

\[
cc^*=e_{\rm std}-N.
\tag{24}
\]

Thus the one-mode sector contains the complementary rank-one pair

\[
\boxed{
N,
\qquad
e_{\rm std}-N.
}
\tag{25}
\]

---

## 5. Relation to the generated third Clifford axis

Version 0.9 defined

\[
Q_z:=-iQ_xQ_y.
\tag{26}
\]

A direct expansion gives

\[
\begin{aligned}
N=c^*c
&=\frac14(Q_x-iQ_y)(Q_x+iQ_y)\\
&=\frac12(e_{\rm std}-Q_z),
\end{aligned}
\tag{27}
\]

while

\[
cc^*=\frac12(e_{\rm std}+Q_z).
\tag{28}
\]

Therefore the number decomposition is exactly the spectral decomposition of the third generated Clifford direction.

Depending on the sign convention chosen for \(Q_z\), the labels “occupied” and “empty” exchange. The unordered rank-one pair is algebraically intrinsic once the oriented Clifford pair is fixed; a physical interpretation of one member as vacuum and the other as occupied is additional semantics.

---

## 6. Matrix form

In the standard representation basis used in v0.9,

\[
Q_x=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix},
\qquad
Q_y=
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix},
\qquad
Q_z=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\tag{29}
\]

Then, up to an irrelevant overall sign convention,

\[
c=
\begin{pmatrix}
0&0\\
-1&0
\end{pmatrix},
\qquad
c^*=
\begin{pmatrix}
0&-1\\
0&0
\end{pmatrix},
\tag{30}
\]

and

\[
N=c^*c=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
\quad\text{or its complementary projector, depending on the sign convention.}
\tag{31}
\]

Thus the nilpotent creation/annihilation pattern is exact as matrix algebra.

---

## 7. Canonical tracial state

Under the unique history-conjugation-invariant order-sector state

\[
\tau_{\rm ord}(X)=\frac12\operatorname{Tr}(X),
\tag{32}
\]

we have

\[
\boxed{
\tau_{\rm ord}(N)=\frac12,
\qquad
\tau_{\rm ord}(e_{\rm std}-N)=\frac12.
}
\tag{33}
\]

Also

\[
\tau_{\rm ord}(c)=\tau_{\rm ord}(c^*)=0.
\tag{34}
\]

Again, (33) is a state-theoretic statement inside the conditional finite-dimensional \(C^*\)-algebraic layer. It is not a derivation of thermal occupation, vacuum probability, or a physical Born experiment.

---

## 8. Theorem B — one-mode CAR algebra is exactly \(M_2(\mathbb C)\)

The universal unital complex \(*\)-algebra generated by one element \(a\) satisfying

\[
a^2=0,
\qquad
(a^*)^2=0,
\qquad
\{a,a^*\}=1
\tag{35}
\]

is isomorphic to

\[
\boxed{\operatorname{CAR}_1\cong M_2(\mathbb C).}
\tag{36}
\]

The representation (3) is nonzero and generates all of \(J_\Delta\), so it realizes this universal algebra faithfully.

Therefore the strongest legitimate algebraic statement at the present stage is

\[
\boxed{
J_\Delta\text{ is canonically generated by a native one-mode CAR pair after the v0.6 complex-linearization assumption.}
}
\tag{37}
\]

The word “canonically” here refers to generation from the established ordered native Clifford pair. It does not mean that a physical fermionic interpretation is canonical.

---

## 9. Theorem C — two independent CAR modes cannot fit

Suppose there were two independent mode pairs

\[
c_1,c_1^*,c_2,c_2^*
\tag{38}
\]

inside the current history algebra satisfying

\[
\{c_i,c_j\}=0,
\qquad
\{c_i,c_j^*\}=\delta_{ij}e
\qquad(i,j\in\{1,2\}).
\tag{39}
\]

The universal complex two-mode CAR algebra is

\[
\boxed{
\operatorname{CAR}_2\cong M_4(\mathbb C).
}
\tag{40}
\]

### Theorem 9.1 — Order-sector two-mode no-go

There is no unital faithful realization of (39) in

\[
J_\Delta\cong M_2(\mathbb C).
\tag{41}
\]

### Proof

Relations (39) induce a unital \(*\)-homomorphism

\[
\Phi:M_4(\mathbb C)\to M_2(\mathbb C).
\tag{42}
\]

Because \(M_4(\mathbb C)\) is simple, a nonzero unital homomorphism is injective. But an injective complex-linear map from a 16-dimensional algebra into a 4-dimensional algebra is impossible. \(\square\)

Thus

\[
\boxed{\texttt{CAR2-IN-ORDER-SECTOR: IMPOSSIBLE}.}
\tag{43}
\]

---

## 10. Stronger theorem — even the full \(\mathbb C[S_3]\) cannot host two modes

One might try to use the two scalar blocks in addition to \(M_2(\mathbb C)\). This does not help.

### Theorem 10.1 — Full-history-algebra two-mode no-go

There is no unital \(*\)-representation of the two-mode CAR relations (39) inside

\[
A=\mathbb C[S_3]
\cong
\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C).
\tag{44}
\]

### Proof 1 — simplicity and dimension

A unital realization would induce a nonzero unital \(*\)-homomorphism

\[
M_4(\mathbb C)\to A.
\tag{45}
\]

Simplicity of \(M_4(\mathbb C)\) makes it injective. But

\[
\dim_\mathbb C M_4(\mathbb C)=16
>6=\dim_\mathbb C A.
\tag{46}
\]

Impossible. \(\square\)

### Proof 2 — simple-block structure

Any irreducible representation of \(M_4(\mathbb C)\) has dimension four. The largest simple block of \(A\) has matrix size two. Hence no nonzero \(*\)-representation can embed the two-mode CAR algebra into \(A\). \(\square\)

Therefore

\[
\boxed{\texttt{CAR2-IN-} \mathbb C[S_3]\texttt{: IMPOSSIBLE}.}
\tag{47}
\]

---

## 11. Equivalent Majorana/Clifford barrier

For two complex CAR modes define four Majorana generators

\[
\gamma_{2j-1}=c_j+c_j^*,
\qquad
\gamma_{2j}=-i(c_j-c_j^*)
\qquad(j=1,2).
\tag{48}
\]

Then

\[
\gamma_r^*=\gamma_r,
\qquad
\{\gamma_r,\gamma_s\}=2\delta_{rs}e.
\tag{49}
\]

Thus two CAR modes require a representation of

\[
\mathrm{Cl}_4(\mathbb C)\cong M_4(\mathbb C).
\tag{50}
\]

The present order sector realizes exactly

\[
\mathrm{Cl}_2(\mathbb C)\cong M_2(\mathbb C),
\tag{51}
\]

and therefore has precisely the algebraic capacity of one complex mode.

This identifies the obstruction structurally rather than by mere element counting.

---

## 12. Sharp capacity theorem

For \(n\) independent finite CAR modes, the complex CAR algebra is

\[
\boxed{
\operatorname{CAR}_n\cong M_{2^n}(\mathbb C),
}
\tag{52}
\]

with complex dimension

\[
4^n.
\tag{53}
\]

Therefore a finite history algebra can support \(n\) faithful independent CAR modes only if it contains a simple matrix block of size at least

\[
2^n.
\tag{54}
\]

For the present history algebra, the maximal block size is two, so

\[
\boxed{n_{\max}=1.}
\tag{55}
\]

This is the exact **matrix-size capacity bound** for the current \(S_3\) history quotient.

---

## 13. What has actually been reached

The theorem chain has now crossed an algebraic boundary that must be named carefully.

### Reached

Inside the conditional complex history layer:

1. two native reconvergence contrasts generate \(\mathrm{Cl}_2(\mathbb C)\);
2. their complex combinations generate an exact one-mode CAR algebra;
3. the associated number operator is a rank-one projection;
4. the current history algebra has capacity exactly one CAR mode.

### Not reached

None of the following follows:

- physical fermionic exchange statistics;
- a many-particle antisymmetric Fock space;
- spacelike locality or microcausal CAR;
- spin-statistics;
- particle/antiparticle creation and annihilation;
- a Hamiltonian or time evolution;
- measurable occupation probabilities;
- quantum field theory.

Hence the physical verdict remains

\[
\boxed{\texttt{ANALOGY ONLY}.}
\tag{56}
\]

The new result is better described as

\[
\boxed{\texttt{NATIVE ALGEBRAIC CAR}_1\texttt{ SKELETON}.}
\tag{57}
\]

---

## 14. Dimensional gate

The one-mode CAR algebra is still the same finite internal matrix fiber

\[
M_2(\mathbb C)
\tag{58}
\]

over the original signed line. It does not force a second spatial carrier coordinate.

Thus

\[
\boxed{\texttt{LINE STATUS: 1D-CLOSED}.}
\tag{59}
\]

---

## 15. Hostile audit

### Claim: “FCOA has derived fermions.”

**Rejected.** It has generated a finite algebra satisfying one-mode CAR after conditional complex linearization. Physical fermionic interpretation requires substantially more structure.

### Claim: “The operators \(c,c^*\) are physical particle creation and annihilation operators.”

**Rejected.** They are algebraic nilpotent ladder operators in \(M_2(\mathbb C)\). No particle species, energy spectrum, vacuum dynamics, spacetime field, or scattering interpretation has been supplied.

### Claim: “The one-mode CAR result was inserted by choosing Pauli matrices.”

**Rejected.** The Pauli/Clifford pair was derived from distinct native root-comb reconvergence residues in v0.9; (3) is the standard algebraic conversion of a Clifford pair into CAR generators.

### Claim: “Longer root histories may generate arbitrarily many fermionic modes inside the same \(S_3\) quotient.”

**Rejected.** All such history images remain in \(\mathbb C[S_3]\), whose largest simple matrix block is \(M_2(\mathbb C)\). The exact capacity is one CAR mode.

### Claim: “The state \(\tau_{\rm ord}\) is the fermionic vacuum.”

**Rejected.** It is the maximally mixed tracial state on the order sector, with \(\tau_{\rm ord}(N)=1/2\), not a selected vacuum pure state.

---

## 16. Publication assessment

Versions 0.3–0.10 now form a surprisingly rigid finite theorem chain:

\[
\boxed{
\text{native reconvergence}
\to
S_3
\to
\mathbb C[S_3]
\to
M_2(\mathbb C)
\to
\mathrm{Cl}_2(\mathbb C)
\to
\operatorname{CAR}_1
}
\tag{60}
\]

with an exact obstruction to \(\operatorname{CAR}_2\) inside the same history quotient.

This is now strong enough to justify a **publication-candidate mathematical note**, provided it passes a dedicated hostile audit of:

1. the legitimacy/canonicity of the history quotient \(S_3\);
2. the root-comb history semantics and stutter objection;
3. the conditional nature of complex linearization;
4. literature/novelty positioning so that standard Clifford/CAR facts are not presented as novel in themselves.

Status:

\[
\boxed{\texttt{PUBLICATION CANDIDATE — HOSTILE AUDIT REQUIRED BEFORE RELEASE}.}
\tag{61}
\]

---

## 17. Next strike

The most important remaining mathematical vulnerability is now **quotient robustness**:

> Is the Clifford/CAR result an artifact of choosing the cardinality-minimal reversible separator \(S_3\), or does every reversible history representation that distinguishes the relevant native root-comb routes necessarily carry a quotient/subrepresentation with the same \(\mathrm{Cl}_2\) structure?

The next trichotomy is:

- `ARTIFACT` — another equally legitimate reversible history quotient preserves route distinctions but destroys anticommutation;
- `MINIMAL-ONLY` — Clifford/CAR is forced only after imposing cardinality minimality;
- `ROBUST-FACTOR` — every admissible reversible separator factors onto a structure carrying the same native Clifford pair.

This is the correct hostile-audit frontier before publication.

---

## 18. References

1. `SOL_QFIELD_ROOT_COMB_CLIFFORD_v0_9.md`.
2. Standard finite CAR algebra identity \(\operatorname{CAR}_n\cong M_{2^n}(\mathbb C)\).
3. Standard complex Clifford identities \(\mathrm{Cl}_{2n}(\mathbb C)\cong M_{2^n}(\mathbb C)\).
4. FCOA-Z v1.1, DOI: https://doi.org/10.5281/zenodo.22169264
