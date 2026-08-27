# G3 Hostile Audit Reconciliation — R2

**Project:** FCOA Admissibility Geometry  
**Audit target:** `G3_VALUE_GEOMETRY.md`  
**Date:** 2026-08-27  
**Status after reconciliation:** one substantive repair incorporated; remaining G3 formulas and full-operation automorphism claims confirmed.

## 1. Audit verdict

The hostile audit independently confirms the three full-operation groups

\[
\operatorname{Aut}(\otimes_S)\cong C_2,
\qquad
\operatorname{Aut}(\otimes_C)\cong C_2,
\qquad
\operatorname{Aut}(\otimes_A)=1,
\]

for every \(N\ge3\), including the small case \(N=3\).

It also confirms the exact commutation counts

\[
|\operatorname{Comm}_{\otimes_S}|=5N-7,
\]

\[
|\operatorname{Comm}_{\otimes_C}|
=|\operatorname{Comm}_{\otimes_A}|
=3(N-1),
\]

and the Association Spectra

\[
(EQ,NEQ,LEFT,RIGHT,NONE)_S
=(EQ,NEQ,LEFT,RIGHT,NONE)_C
\]

\[
=
(6N-8,0,N^2+4N-6,N^2+3N-6,N^3+N^2-10N+21),
\]

and

\[
(EQ,NEQ,LEFT,RIGHT,NONE)_A
=
(6N-8,0,N^2+4N-6,N^2+4N-6,N^3+N^2-11N+21).
\]

For \(N=3\) the confirmed spectra are

\[
G3\text{-}S=G3\text{-}C=(10,0,15,12,27),
\]

\[
G3\text{-}A=(10,0,15,15,24).
\]

## 2. Substantive repair: the G3-A definedness reduct

The original G3 checkpoint stated only the residual generic path reflection after value erasure and summarized the definedness automorphism group as \(C_2\). That was too small for the intrinsic base-sort definedness reduct.

After adding the anchor cell

\[
P_1\otimes_A P_0=\Omega_+,
\]

the definedness relation contains both

\[
(P_0,P_1),\qquad(P_1,P_0),
\]

and for every generic \(P_i\), both \(P_0\) and \(P_1\) are bidirectionally connected to \(P_i\). Both are loopless. Therefore definedness alone no longer distinguishes the two boundary points.

Hence the transposition

\[
s=(P_0\ P_1)
\]

is an automorphism of the base-sort definedness reduct. Independently, the generic path reversal

\[
r(P_i)=P_{N+2-i},\qquad 2\le i\le N,
\]

also survives. The two involutions commute.

Therefore the correct intrinsic statement is

\[
\boxed{
\operatorname{Aut}(D_A\upharpoonright X_N)
\cong C_2\times C_2.
}
\]

The previously recorded \(C_2\) is recovered only as the stabilizer of the two boundary roles pointwise:

\[
\boxed{
\operatorname{Stab}_{\operatorname{Aut}(D_A)}(P_0,P_1)
\cong C_2.
}
\]

Thus the audit does not weaken the value-memory conclusion; it strengthens it:

\[
\boxed{
C_2\times C_2
\longrightarrow
1
}
\]

when values are restored, rather than merely \(C_2\to1\).

The two erased distinctions are:

1. boundary-role distinction \(P_0\) versus \(P_1\);
2. orientation of the symmetric generic path.

The full operation restores both through its value fibers.

## 3. One-sorted definedness caveat

If terminal outputs are retained as elements after values are erased, they become isolated points of the definedness relation. Therefore the full one-sorted definedness automorphism groups contain an independent symmetric factor on terminal outputs.

With

\[
|T_S|=2N-1,
\qquad
|T_C|=|T_A|=2N,
\]

we obtain

\[
\operatorname{Aut}_{\rm full}(D_S)
\cong C_2\times\operatorname{Sym}(T_S),
\]

\[
\operatorname{Aut}_{\rm full}(D_C)
\cong C_2\times\operatorname{Sym}(T_C),
\]

\[
\operatorname{Aut}_{\rm full}(D_A)
\cong (C_2\times C_2)\times\operatorname{Sym}(T_A).
\]

For the domain/value comparison in this research line, the primary comparison is on the active/base sort \(X_N\); the isolated-terminal factor must nevertheless be stated whenever a one-sorted full carrier is used.

## 4. Small-case repair check: N=3

The audit specifically checked the potentially dangerous case \(N=3\).

In G3-S, \(\Omega\) has two preimage cells while every \(E_i^\ast,E_i^\times\) has one, so \(\Omega\) remains internally distinguishable.

In G3-C, \(\Omega_+\) and \(\Omega_-\) each have only one preimage cell, so cardinality alone cannot separate them from the E-outputs. Nevertheless their preimages are off-diagonal generic-generic pairs, whereas \(E_i^\ast\) arises from \((P_i,P_0)\) and \(E_i^\times\) from the diagonal \((P_i,P_i)\). Thus the unordered pair \(\{\Omega_+,\Omega_-\}\) remains structurally separate from the E-output families.

No exceptional failure occurs at \(N=3\).

## 5. Repair of the general Anonymous Output-Swap statement

The original informal lemma was too broad. A color-reversing involution on one chosen domain subset does not automatically extend to the whole operation.

A sufficient version requires at least:

1. \(r\) is an automorphism of the entire base/domain reduct, not just of the colored subgraph;
2. the \(\Omega_+\)- and \(\Omega_-\)-fibers are exchanged exactly by \(r\);
3. no additional cell fixed by \(r\) anchors only one of the two outputs;
4. every other output fiber also admits the permutation forced by \(r\);
5. \(\Omega_+,\Omega_-\) are genuinely anonymous and not separately named, sorted, typed, or otherwise distinguished.

Under these hypotheses, extending \(r\) by

\[
\Omega_+\leftrightarrow\Omega_-
\]

gives an automorphism.

Without them the statement is false. G3-A itself supplies the relevant countermechanism: the fixed anchor pair forces \(\Omega_+\) to remain fixed and therefore prevents the swap.

## 6. One-anchor minimality

The audit confirms the restricted minimality claim:

- zero anonymous operation-cell anchors leave the G3-C reflection/output-swap automorphism;
- one anchor on a pair already fixed by all candidate carrier automorphisms kills it.

Thus one anchor is minimal **within the anonymous two-output operation-cell branch**.

No global minimality is claimed if naming, sorting, typing, or other external distinctions of the outputs are allowed.

## 7. Structural conclusion after repair

The strongest audited G3 comparison is now

\[
\boxed{
\begin{array}{c|c|c|c}
& G3\text{-}S & G3\text{-}C & G3\text{-}A\\
\hline
\operatorname{Aut}(\star)&C_2&C_2&1\\
\operatorname{Aut}(D_\star\upharpoonright X_N)&C_2&C_2&C_2\times C_2\\
|\operatorname{Comm}|&5N-7&3(N-1)&3(N-1)
\end{array}
}
\]

with the exact Association Spectra stated above.

This yields two independent separations:

\[
G3\text{-}S\to G3\text{-}C:
\quad
\text{same domain, same Association Spectrum, same }|\operatorname{Aut}|,
\]

but a different commutation locus;

and

\[
G3\text{-}C\to G3\text{-}A:
\quad
\text{value anchoring destroys the residual full-operation symmetry,}
\]

while the definedness reduct retains even more symmetry than previously noticed.

## 8. Status

The R2 hostile audit confirms the G3 operation-level construction and exact finite formulas, while repairing the intrinsic definedness-group statement and the general output-swap lemma.

Current classification:

\[
\boxed{
G3 = hostile-audited with repair; proof consolidation pending.
}
\]

It is still post-publication research and is not part of the Zenodo G2 publication DOI 10.5281/zenodo.22129787.
