# G3 Research Checkpoint — Value Geometry after Domain Geometry

**Project:** FCOA Admissibility Geometry  
**Status:** post-publication research branch; hostile-audited with repair; not part of Zenodo DOI 10.5281/zenodo.22129787  
**Date opened:** 2026-08-27  
**Branch discipline:** no ordinary arithmetic is imported; all new generic rules are explicit partial-operation cells.

## 1. Why G3 is opened

The published G2 branch proves that a directed path can be compiled into the **domain** of a constant-valued partial operation. The next question recorded in `STATE.md` was:

> What is the weakest extension that carries information not already reducible to domain geometry, while still avoiding reconstruction of ordinary arithmetic?

G3 answers this by freezing the generic domain to a **symmetric adjacency path** and asking whether orientation can instead live in the **value fibers**.

The experiment separates three layers:

\[
\boxed{
\text{symmetric domain}
\longrightarrow
\text{anonymous value coloring}
\longrightarrow
\text{anchored value coloring}
}
\]

No result below is silently folded back into the published G2 checkpoint.

## 2. Common M0 background

Let

\[
X_N=\{P_0,\ldots,P_N\},\qquad N\ge3,
\]

and

\[
G_N=\{P_2,\ldots,P_N\}.
\]

Keep all M0 multiplication cells:

\[
P_0\otimes P_i=P_0\quad(1\le i\le N),
\]

\[
P_i\otimes P_0=E_i^\ast\quad(2\le i\le N),
\]

\[
P_1\otimes P_i=P_i\otimes P_1=P_i\quad(2\le i\le N),
\]

\[
P_i\otimes P_i=E_i^\times\quad(2\le i\le N),
\]

with all other M0 cells undefined.

All new \(\Omega\)-outputs below are terminal: no product with an \(\Omega\)-output as an argument is defined.

## 3. G3-S: symmetric-domain constant-value probe

Define \(\otimes_S\) by extending M0 with both orientations of every generic adjacency edge:

\[
P_i\otimes_S P_{i+1}=\Omega,
\qquad
P_{i+1}\otimes_S P_i=\Omega,
\qquad 2\le i<N.
\]

Thus the off-diagonal generic domain is the undirected path

\[
P_2-P_3-\cdots-P_N.
\]

### Proposition G3-S.1 — residual reflection

\[
\boxed{
\operatorname{Aut}(\otimes_S)\cong C_2.
}
\]

M0 fixes \(P_0,P_1\) and permits arbitrary generic permutations. The new symmetric adjacency domain reduces this to the automorphism group of the finite path, namely identity and reversal. The unique new terminal output \(\Omega\) is preserved.

For every \(N\ge3\), \(\Omega\) is internally distinguishable from all \(E_i^\ast,E_i^\times\). In particular for \(N=3\), \(\Omega\) has two preimage cells while each E-output has one.

### Association Spectrum

\[
\boxed{
\begin{aligned}
EQ &= 6N-8,\\
NEQ &= 0,\\
LEFT &= N^2+4N-6,\\
RIGHT &= N^2+3N-6,\\
NONE &= N^3+N^2-10N+21.
\end{aligned}}
\]

### Commutation locus

The old M0 commuting pairs remain, and every adjacent generic ordered pair now commutes. Hence

\[
\boxed{
|\operatorname{Comm}_{\otimes_S}|=5N-7.
}
\]

## 4. G3-C: anonymous two-value orientation coloring

Keep exactly the same generic domain as G3-S, but define

\[
P_i\otimes_C P_{i+1}=\Omega_+,
\]

\[
P_{i+1}\otimes_C P_i=\Omega_-,
\qquad 2\le i<N.
\]

The terminal values \(\Omega_+,\Omega_-\) are distinct but anonymous: not named constants, not externally colored, and not in separate singleton sorts.

### Proposition G3-C.1 — output-swap obstruction

\[
\boxed{
\operatorname{Aut}(\otimes_C)\cong C_2.
}
\]

Path reversal extends to the operation precisely by simultaneously swapping

\[
\Omega_+\leftrightarrow\Omega_-.
\]

Thus

\[
\boxed{
\text{two unequal anonymous outputs do not by themselves fix absolute orientation.}
}
\]

For \(N=3\), each \(\Omega\)-fiber has one preimage cell, so preimage cardinality alone no longer separates \(\Omega_\pm\) from E-outputs. Nevertheless the argument geometry does: \(\Omega_\pm\) arise from off-diagonal generic-generic pairs, \(E_i^\ast\) from \((P_i,P_0)\), and \(E_i^\times\) from diagonal cells. Hence the unordered pair \(\{\Omega_+,\Omega_-\}\) remains structurally separate from the E-output families.

### Same spectrum, different commutation

The Association Spectrum is identical to G3-S:

\[
\boxed{
(EQ,NEQ,LEFT,RIGHT,NONE)
=
(6N-8,0,N^2+4N-6,N^2+3N-6,N^3+N^2-10N+21).
}
\]

But adjacent generic pairs no longer commute. Therefore

\[
\boxed{
|\operatorname{Comm}_{\otimes_C}|=3(N-1).
}
\]

Hence G3-S and G3-C have the same domain, the same Association Spectrum, and the same automorphism-group size, but different commutation loci.

## 5. G3-A: one anchored output fiber

Extend G3-C by exactly one cell:

\[
\boxed{
P_1\otimes_A P_0=\Omega_+.
}
\]

No other cell is added.

The pair \((P_1,P_0)\) is fixed in the full M0 operation, so the anchor does not privilege a generic point.

### Proposition G3-A.1 — one-anchor rigidity

For every \(N\ge3\),

\[
\boxed{
\operatorname{Aut}(\otimes_A)=1.
}
\]

The anchor fixes \(\Omega_+\). Therefore the path reversal can no longer extend by swapping \(\Omega_+\) and \(\Omega_-\). The generic path is consequently fixed pointwise, and then all terminal outputs are fixed by their preimage cells.

### Proposition G3-A.2 — intrinsic definedness reduct

Let

\[
D_A(x,y)\iff\operatorname{Def}(x\otimes_A y)
\]

and restrict first to the active/base sort \(X_N\).

The hostile audit exposed an important extra symmetry. Once values are erased, the anchor merely adds the defined pair \((P_1,P_0)\). In the resulting binary relation, \(P_0\) and \(P_1\) become symmetric:

- both are loopless;
- both are bidirectionally adjacent to every generic point;
- they are bidirectionally adjacent to each other.

Hence the boundary transposition

\[
s=(P_0\ P_1)
\]

survives. Independently, generic path reversal

\[
r(P_i)=P_{N+2-i},\qquad2\le i\le N
\]

survives. They commute. Therefore

\[
\boxed{
\operatorname{Aut}(D_A\upharpoonright X_N)
\cong C_2\times C_2.
}
\]

If one conditions on the original M0 boundary roles and fixes \(P_0,P_1\) pointwise, the remaining stabilizer is the generic path reflection:

\[
\boxed{
\operatorname{Stab}(P_0,P_1)\cong C_2.
}
\]

Thus the intrinsic Value-Erasure comparison is stronger than first expected:

\[
\boxed{
C_2\times C_2
\longrightarrow
1
}
\]

when values are restored.

The full operation restores two distinctions erased by definedness:

1. the boundary-role distinction \(P_0\) versus \(P_1\);
2. the orientation of the generic symmetric path.

### Full one-sorted definedness caveat

If terminal outputs are retained in the same universe after values are erased, all of them become isolated points of the binary definedness relation. Hence an independent symmetric factor appears.

With

\[
|T_S|=2N-1,
\qquad
|T_C|=|T_A|=2N,
\]

we have

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

The active/base-sort comparison is primary for the domain/value question, but the one-sorted factor must be stated when that presentation is used.

### Association Spectrum

The anchor creates exactly \(N\) new RIGHT-only triples

\[
(P_1,P_0,P_c),\qquad1\le c\le N.
\]

Therefore

\[
\boxed{
\begin{aligned}
EQ &= 6N-8,\\
NEQ &= 0,\\
LEFT &= N^2+4N-6,\\
RIGHT &= N^2+4N-6,\\
NONE &= N^3+N^2-11N+21.
\end{aligned}}
\]

The commutation locus remains

\[
\boxed{
|\operatorname{Comm}_{\otimes_A}|=3(N-1).
}
\]

## 6. Corrected Anonymous Output-Swap Lemma

The unqualified statement "a color-reversing involution always extends by swapping two anonymous outputs" is false.

A sufficient version is:

Let \(B\) be the full base/domain reduct and let \(D=D_+\sqcup D_-\) be exactly the two terminal-output fibers. Suppose:

1. \(r\in\operatorname{Aut}(B,D)\) is an involution of the entire base/domain structure;
2. \(r(D_+)=D_-\) and \(r(D_-)=D_+\);
3. the values on \(D_+,D_-\) are exactly \(\Omega_+,\Omega_-\);
4. no additional fixed cell anchors one of these outputs;
5. every other output fiber admits the permutation forced by \(r\);
6. \(\Omega_+,\Omega_-\) are anonymous and may be permuted.

Then extending \(r\) by

\[
\Omega_+\leftrightarrow\Omega_-
\]

gives an automorphism of the full partial operation.

G3-A is the countermechanism when hypothesis 4 fails.

## 7. One-Anchor Lemma

Assume the only residual full-operation symmetry is

\[
C_2=\{1,r\},
\]

and every extension of \(r\) requires

\[
\Omega_+\leftrightarrow\Omega_-.
\]

If an ordered pair \((u,v)\) is already fixed pointwise by all candidate carrier automorphisms and one adds

\[
u\star v=\Omega_+,
\]

then \(\Omega_+\) is fixed, so \(r\) cannot extend.

Within the anonymous two-terminal-value branch, zero anchors are insufficient in G3-C and one anchor is sufficient in G3-A. This is the only minimality claim made here. Naming, sorting, typing, or otherwise distinguishing the outputs can kill the swap with no anchor cell at all.

## 8. Value-Erasure Test — working formulation

Given a partial operation \(\star\), form its definedness reduct

\[
D_\star(x,y)\iff\operatorname{Def}(x\star y).
\]

Compare

\[
\operatorname{Aut}(D_\star\upharpoonright X_N)
\quad\text{with}\quad
\operatorname{Aut}(\star).
\]

If the full operation is strictly more rigid, then some structural information is carried by value fibers rather than by domain geometry alone.

The audited G3-A example gives

\[
\boxed{
\operatorname{Aut}(D_A\upharpoonright X_N)\cong C_2\times C_2,
\qquad
\operatorname{Aut}(\otimes_A)=1.
}
\]

`Value-Erasure Test` is working terminology, not a priority claim.

## 9. Exact audited comparison

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

Association spectra:

\[
G3\text{-}S=G3\text{-}C:
\]

\[
\boxed{
(6N-8,0,N^2+4N-6,N^2+3N-6,N^3+N^2-10N+21)
}
\]

and

\[
G3\text{-}A:
\]

\[
\boxed{
(6N-8,0,N^2+4N-6,N^2+4N-6,N^3+N^2-11N+21).
}
\]

For \(N=3\):

\[
G3\text{-}S=G3\text{-}C=(10,0,15,12,27),
\]

\[
G3\text{-}A=(10,0,15,15,24).
\]

## 10. Structural conclusions

The audited G3 branch separates two new mechanisms.

First,

\[
G3\text{-}S\to G3\text{-}C
\]

changes only the equality pattern of opposite edge values. The domain, Association Spectrum, and automorphism-group size stay fixed, while the commutation locus changes:

\[
5N-7\to3(N-1).
\]

Second,

\[
G3\text{-}C\to G3\text{-}A
\]

anchors one value fiber. The commutation locus stays fixed, while the full operation becomes rigid. After value erasure the active/base definedness reduct still has

\[
C_2\times C_2
\]

symmetry.

Hence domain geometry, commutation geometry, Association Spectrum, and value-fiber rigidity are genuinely different coordinates of the partial-operation structure.

## 11. Status

The operation-level formulas have been computationally checked for finite \(N\), and the G3 branch has undergone one independent hostile audit. The audit confirmed all spectrum and commutation formulas and all full-operation automorphism groups, while repairing the intrinsic G3-A definedness automorphism group and sharpening the output-swap hypotheses.

Current classification:

\[
\boxed{
G3 = hostile-audited with repair; proof consolidation complete enough for the next research decision.
}
\]

G3 remains post-publication research and is not part of Zenodo DOI 10.5281/zenodo.22129787.
