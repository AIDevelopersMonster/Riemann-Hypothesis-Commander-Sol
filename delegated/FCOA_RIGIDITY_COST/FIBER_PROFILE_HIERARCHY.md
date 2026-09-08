# FCOA Rigidity Cost — Fiber-Profile Hierarchy and the 7-Local Ceiling

**Direction:** FCOA — SOL-RIGIDITY — Rigidity Cost & Skeleton Classification  
**Status:** local theorem/computation/literature reconciliation note  
**Scope:** complete generic domain, two anonymous terminal outputs, tournament-type opposite fibers  
**Upstream boundary:** this note does not modify G4.

Let \(T\) be the tournament defined by the \(\Omega_+\)-fiber on the generic carrier \(G_N\), with \(n=N-1\). The \(\Omega_-\)-fiber is \(T^{\rm op}\).

Define

\[
\operatorname{Aut}^{\pm}(T)
=
\{g\in S_n:gT=T\text{ or }gT=T^{\rm op}\}.
\]

This is exactly the generic residual carrier group when the two terminal outputs are anonymous.

---

## 1. Two different meanings of “local profile”

The next invariant must distinguish two information levels which are easy to conflate.

### 1.1 Anonymous histogram profile

For \(1\le k\le n\), let

\[
\boxed{
H_k^{\pm}(T)
=
\multiset{[T[X]]_{\pm}:X\subseteq V(T),\ |X|=k},
}
\]

where \([U]_{\pm}\) identifies a tournament with its converse.

This records **how many** induced anonymous \(k\)-types occur, but forgets **which carrier subset** realizes which type.

The previous invariant \(\tau_3\) is the unique independent scalar contained in \(H_3^{\pm}\).

### 1.2 Coherent hereditary passport

For two tournaments \(T,T'\) on the same carrier, say they agree through arity \(k\) when for every nonempty

\[
X\subseteq V,\qquad |X|\le k,
\]

the restrictions \(T[X]\) and \(T'[X]\) are hemimorphic (isomorphic or converse-isomorphic).

Unlike \(H_k^{\pm}\), this retains **subset identity and cross-subset coherence**.

Call this subset-indexed object the local hemimorphism passport

\[
\boxed{\mathsf{HP}_{\le k}^{\pm}(T).}
\]

---

## 2. Exact finite histogram audit

An exhaustive enumeration of all unlabeled tournaments through \(n=7\) was performed by `verify_fiber_profile_hierarchy.py`.

For each tournament it computes

\[
\sigma(T)=
\bigl(|\operatorname{Aut}(T)|,\ |\operatorname{Anti}(T)|\bigr),
\]

where

\[
\operatorname{Anti}(T)=\{g:gT=T^{\rm op}\}.
\]

Thus the anonymous residual group has size

\[
|\operatorname{Aut}^{\pm}(T)|
=|\operatorname{Aut}(T)|+|\operatorname{Anti}(T)|.
\]

The smallest single histogram order \(k\ge3\) that determines \(\sigma(T)\) among all tournaments of order \(n\) is:

| generic size \(n\) | unlabeled tournaments | minimal histogram order \(k\) determining \(\sigma\) |
|---:|---:|---:|
| 3 | 2 | 3 |
| 4 | 4 | 3 |
| 5 | 12 | 5 |
| 6 | 56 | 5 |
| 7 | 456 | 7 |

The number of ambiguous histogram buckets at each proper order is:

| \(n\) | \(k=3\) | \(k=4\) | \(k=5\) | \(k=6\) |
|---:|---:|---:|---:|---:|
| 5 | 2 | 2 | 0 | — |
| 6 | 6 | 8 | 0 | — |
| 7 | 14 | 37 | 1 | 1 |

Therefore \(\tau_3\) is a sharp separator for the specific G4-C/transitivity question, but it is not a complete residual-symmetry classifier.

---

## 3. A seven-vertex all-proper-profile counterexample

There are two explicit tournaments on vertices \(0,\dots,6\) which differ by reversing only the arc between \(0\) and \(1\).

Define \(S_7\) by the arc set

\[
\begin{aligned}
A(S_7)=\{&10,20,30,04,50,06,21,13,41,51,16,32,42,25,62,\\
&43,53,63,54,64,65\}.
\end{aligned}
\]

Define \(R_7\) by replacing \(10\) with \(01\):

\[
A(R_7)=A(S_7)\setminus\{10\}\cup\{01\}.
\]

Exact enumeration gives

\[
\operatorname{Aut}(S_7)=1,
\qquad
\operatorname{Anti}(S_7)=\{a\},
\]

with the unique anti-isomorphism

\[
\boxed{
a=(0\ 6)(1\ 4)(3\ 5),\qquad a(2)=2.}
\]

Hence

\[
\boxed{\operatorname{Aut}^{\pm}(S_7)\cong C_2.}
\]

For \(R_7\),

\[
\boxed{
\operatorname{Aut}(R_7)=1,
\qquad
\operatorname{Anti}(R_7)=\varnothing,
\qquad
\operatorname{Aut}^{\pm}(R_7)=1.
}
\]

Nevertheless,

\[
\boxed{
H_k^{\pm}(S_7)=H_k^{\pm}(R_7)
\qquad\text{for every }k=3,4,5,6.
}
\]

In particular both have

\[
\tau_3=12,
\]

so their three-point profile is

\[
(23\text{ transitive},\ 12\text{ cyclic}).
\]

Their four-point anonymous profile is also identical:

\[
(5\text{ with }0\ C_3,\ 12\text{ with }1\ C_3,\ 18\text{ with }2\ C_3).
\]

The verifier checks equality of the complete canonical hemimorphism histograms also at orders five and six.

Therefore:

\[
\boxed{
\text{all proper anonymous histogram levels can agree while }
\operatorname{Aut}^{\pm}\text{ differs.}
}
\]

At \(n=7\), no scalar or histogram built only from the multiset of proper induced hemitypes can recover the last global anti-automorphism in general.

---

## 4. The classical coherent-local threshold is exactly seven

The tournament-reconstruction literature uses the stronger subset-indexed notion above.

Y. Boudabbous and G. Lopez proved that finite tournaments are

\[
\boxed{(\le7)\text{-half-reconstructible}}
\]

and that the value \(7\) is optimal. A later characterization paper restates this theorem and classifies the exceptional \((\le k)\)-half-reconstructible classes for \(3\le k\le6\):

- Y. Boudabbous, G. Lopez, *La relation différence et l’anti-isomorphie*, Math. Logic Quart. 41 (1995), 268–280.
- Y. Boudabbous, A. Boussaïri, A. Chaïchaâ, N. El Amri, *(<= k)-half-reconstructible tournaments for k <= 6*, C. R. Acad. Sci. Paris, Ser. I 346 (2008), 919–924, DOI `10.1016/j.crma.2008.07.024`.

Translated into the FCOA tournament layer:

> if two two-anonymous-output tournament layers on the same generic carrier have hemimorphic restrictions on every carrier subset of size at most seven, then the full value-fiber tournaments are hemimorphic globally.

Therefore their residual groups \(\operatorname{Aut}^{\pm}\) agree up to carrier conjugacy.

So the universal coherent local arity is

\[
\boxed{k_{\rm coherent}=7,}
\]

and this is arity-optimal.

---

## 5. The two-threshold theorem for FCOA

We now have two mathematically different thresholds.

### Separation threshold

To distinguish G4-C from **any rigid tournament layer**, it is enough and locality-minimal to inspect three generic vertices:

\[
\boxed{k_{\rm sep}=3.}
\]

Indeed G4-C is transitive and has \(\tau_3=0\), while a rigid tournament cannot have \(\tau_3=0\). The exact minimum rigid defect in the constructed family is \(\tau_3=2\).

### Universal coherent reconstruction threshold

To determine an **arbitrary** anonymous tournament value-fiber structure up to global output exchange by local restrictions, the optimal general arity is

\[
\boxed{k_{\rm rec}=7.}
\]

These numbers answer different questions and must not be conflated:

\[
\boxed{
3=\text{first local separator},
\qquad
7=\text{universal coherent reconstruction ceiling}.
}
\]

---

## 6. Why the histogram fails: coherence is the missing invariant

The pair \(S_7,R_7\) shows that simply increasing the histogram order does not preserve the information needed for the final symmetry decision.

The lost datum is not “one more count”. It is **which overlapping subsets realize which local types**.

Thus the next invariant after \(\tau_3\) should not be another global scalar such as a raw \(4\)-cycle count. The structurally correct refinement is a coherent incidence object linking local fiber patterns across overlapping subsets.

A minimal conceptual ladder is therefore

\[
\boxed{
\begin{array}{c}
\text{cell count / domain}\\
\downarrow\\
\text{fiber sizes}\\
\downarrow\\
\text{commutation and Association Spectrum}\\
\downarrow\\
\tau_3\text{ or }M_2\quad(3\text{-point separator})\\
\downarrow\\
H_k^{\pm}\quad(\text{anonymous histograms})\\
\downarrow\\
\mathsf{HP}_{\le k}^{\pm}\quad(\text{subset-coherent local passport})\\
\downarrow\\
k=7:\ \text{universal global hemimorphism class.}
\end{array}}
\]

---

## 7. Research consequence

For this branch, the next nontrivial compression problem is now precise:

> How much of the full seven-local coherent passport is actually needed to determine \(\operatorname{Aut}^{\pm}(T)\), without reconstructing the whole tournament?

This is strictly weaker than tournament reconstruction and is the natural FCOA-specific problem.

Candidate compressed objects include:

1. overlap incidence of cyclic triples (the `C3-hypergraph` rather than only its cardinality);
2. vertex-wise cyclic-triple degrees;
3. pair-wise cyclic-triple codegrees;
4. coherent 4- and 5-point extension signatures of the `C3-hypergraph`;
5. the coarsest refinement whose stabilizer equals \(\operatorname{Aut}^{\pm}(T)\).

The objective is no longer to prove that seven-local data suffice — that is classical — but to find the **smallest stabilizer-complete compression** adapted to the FCOA value-fiber setting.

---

## 8. Claim firewall

1. The `(<=7)` half-reconstruction threshold is classical and is cited, not claimed as new.
2. The FCOA translation separates histogram information from subset-coherent information; this distinction is essential.
3. The exact `S7/R7` histogram counterexample is a local computational result of this branch; no novelty claim is made before literature comparison against reduced/half-deck catalogues.
4. Equality of anonymous histograms is weaker than `(<=k)` half-isomorphy in the reconstruction literature.
5. `tau3` remains the minimal separator for G4-C versus rigid tournament layers, but not a complete rigidity classifier.
6. No ordinary arithmetic on external carrier labels is imported.