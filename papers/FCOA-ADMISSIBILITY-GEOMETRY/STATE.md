# FCOA Admissibility Geometry — current state

**Canonical publication DOI:** 10.5281/zenodo.22129787  
**Publication date:** 2026-08-27  
**GitHub role:** theorem/reproducibility/demo companion  
**Maintenance boundary:** see [`WORKSPACE.md`](WORKSPACE.md)

## 1. Publication checkpoint — fixed

The published and audited chain remains

\[
\boxed{M0\longrightarrow G1\longrightarrow G2.}
\]

Nothing in G3/G4 silently revises the Zenodo publication.

### M0 multiplication

For \(G_N=\{P_2,\ldots,P_N\}\),

\[
\operatorname{Aut}(\mathfrak M_N^\times)\cong S_{N-1}.
\]

M0 multiplication Association Spectrum:

\[
(4(N-1),0,N^2+2N-2,N^2+N-2,N^3+N^2-4N+9).
\]

### G1

For external interaction skeleton \(A\subseteq G_N^2\),

\[
\operatorname{Aut}(\mathfrak M_N^\times,A)
\cong
\operatorname{Aut}(G_N,A).
\]

For undirected then directed path:

\[
S_{N-1}\to C_2\to1.
\]

This is external rigidity; erasing \(A\) restores M0 symmetry.

### G2

Directed adjacency is compiled into the operation domain using one terminal value \(\Omega\):

\[
P_i\otimes_1P_{i+1}=\Omega,
\qquad 2\le i<N.
\]

Then

\[
\operatorname{Aut}(\otimes_1)=1,
\]

and directed adjacency is uniformly recoverable from off-diagonal generic definedness.

G2 spectrum:

\[
(5N-6,0,N^2+3N-4,N^2+2N-4,N^3+N^2-7N+15).
\]

Commutation size remains

\[
3(N-1).
\]

## 2. G3 — hostile-audited with repair

Files:

- [`G3_VALUE_GEOMETRY.md`](G3_VALUE_GEOMETRY.md)
- [`G3_HOSTILE_AUDIT_RECONCILIATION.md`](G3_HOSTILE_AUDIT_RECONCILIATION.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_g3.py`

The hostile audit confirms:

\[
\operatorname{Aut}(\otimes_S)\cong C_2,
\qquad
\operatorname{Aut}(\otimes_C)\cong C_2,
\qquad
\operatorname{Aut}(\otimes_A)=1.
\]

G3-S and G3-C have the same spectrum

\[
(6N-8,0,N^2+4N-6,N^2+3N-6,N^3+N^2-10N+21),
\]

but different commutation sizes:

\[
|\operatorname{Comm}_S|=5N-7,
\qquad
|\operatorname{Comm}_C|=3(N-1).
\]

G3-A has spectrum

\[
(6N-8,0,N^2+4N-6,N^2+4N-6,N^3+N^2-11N+21)
\]

and commutation size \(3(N-1)\).

### Audit repair

The intrinsic base-sort definedness group of G3-A is not merely \(C_2\). After the anchor makes \((P_1,P_0)\) defined, definedness alone also permits the boundary swap \(P_0\leftrightarrow P_1\). Therefore

\[
\boxed{
\operatorname{Aut}(D_A\upharpoonright X_N)
\cong C_2\times C_2.
}
\]

Hence value restoration gives the stronger rigidity jump

\[
\boxed{C_2\times C_2\longrightarrow1.}
\]

## 3. Fiber-Transport Theorem — consolidated

See [`FIBER_TRANSPORT_THEOREM.md`](FIBER_TRANSPORT_THEOREM.md).

For a base/domain structure \((B,D)\) and a surjective anonymous terminal-output map

\[
c:D\to O,
\]

full-operation carrier automorphisms are exactly the automorphisms of \((B,D)\) preserving the equality partition of domain cells induced by \(c\):

\[
\boxed{
\operatorname{Aut}(B,D,O;c)
\cong
\operatorname{Stab}_{\operatorname{Aut}(B,D)}(\equiv_c).
}
\]

This makes the domain/value split exact: domain geometry first restricts automorphisms, then value-fiber geometry restricts them further.

Working finite invariant:

\[
\operatorname{VRI}(\star)
=
\left[
\operatorname{Aut}(D_\star\upharpoonright X):
\pi_X\operatorname{Aut}(\star)
\right].
\]

For G3:

\[
\operatorname{VRI}(S)=1,
\qquad
\operatorname{VRI}(C)=1,
\qquad
\operatorname{VRI}(A)=4.
\]

`Value-Rigidity Index` is working terminology only.

## 4. G4 — bounded-output rigidity amplification candidate

Files:

- [`G4_BOUNDED_OUTPUT_AMPLIFICATION.md`](G4_BOUNDED_OUTPUT_AMPLIFICATION.md)
- verifier: `../../experiments/fcoa-domain-compilation/verify_g4.py`

### G4-C

Define every off-diagonal generic cell, but use only two anonymous terminal values according to external carrier orientation:

\[
P_i\otimes_{4C}P_j=
\begin{cases}
\Omega_+,&i<j,\\
\Omega_-,&i>j,
\end{cases}
\qquad 2\le i,j\le N,\ i\ne j.
\]

The generic definedness domain is complete, so

\[
\operatorname{Aut}(D_{4C}\upharpoonright X_N)\cong S_{N-1}.
\]

The full operation retains only identity and reversal-with-output-swap:

\[
\boxed{
\operatorname{Aut}(\otimes_{4C})\cong C_2.
}
\]

Therefore

\[
\boxed{
\operatorname{VRI}(G4\text{-}C)=\frac{(N-1)!}{2}.
}
\]

A fixed two-element anonymous output alphabet thus gives an unbounded, factorially growing value-rigidity index.

G4-C spectrum:

\[
\boxed{
(N^2+N-2,\ 0,\ 2N^2-N,\ 2N^2-2N,\ N^3-2N^2+5N+3).
}
\]

Commutation size remains

\[
3(N-1).
\]

### G4-A

Add the single boundary anchor

\[
P_1\otimes_{4A}P_0=\Omega_+.
\]

Candidate results:

\[
\operatorname{Aut}(\otimes_{4A})=1,
\]

\[
\operatorname{Aut}(D_{4A}\upharpoonright X_N)
\cong C_2\times S_{N-1},
\]

and hence

\[
\boxed{
\operatorname{VRI}(G4\text{-}A)=2(N-1)!.
}
\]

G4-A spectrum:

\[
\boxed{
(N^2+N-2,\ 0,\ 2N^2-N,\ 2N^2-N,\ N^3-2N^2+4N+3).
}
\]

Commutation size is still \(3(N-1)\).

## 5. Current statuses

\[
\mathbf F:\ M0,G1,G2\text{ published/audited checkpoint}
\]

\[
\mathbf F:\ G3\text{ operation groups, spectra and commutation formulas after hostile audit repair}
\]

\[
\mathbf F:\ \operatorname{Aut}(D_A\upharpoonright X_N)=C_2\times C_2
\]

\[
\mathbf F:\ \text{Fiber-Transport theorem in the stated relative typed setup}
\]

\[
\mathbf W:\ \text{Value-Rigidity Index terminology}
\]

\[
\mathbf W:\ G4\text{ bounded-output amplification theorem candidate}
\]

## 6. Immediate next step

Do not open G5 yet.

The next action is a hostile audit of G4, with special attention to:

1. whether the complete generic definedness domain really has full \(S_{N-1}\) symmetry relative to M0;
2. whether preserving the two anonymous orientation fibers leaves exactly identity and reversal;
3. the \(N=3\) edge case, where \(S_2=C_2\) and \(\operatorname{VRI}(G4\text{-}C)=1\);
4. the exact G4-C and G4-A Association Spectra;
5. whether the single boundary anchor makes the full operation rigid while the definedness group becomes \(C_2\times S_{N-1}\);
6. whether the factorial VRI formulas are stated with the correct active-sort scope;
7. whether any hidden naming/sorting of \(\Omega_+,\Omega_-\) would trivialize the anonymous-output claim.

Only after reconciliation with that audit should G4 be promoted from working theorem candidate to fixed result.
