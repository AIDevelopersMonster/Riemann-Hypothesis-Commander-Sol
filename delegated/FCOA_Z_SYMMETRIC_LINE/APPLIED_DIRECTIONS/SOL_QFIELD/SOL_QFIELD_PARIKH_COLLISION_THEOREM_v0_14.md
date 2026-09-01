# SOL-QFIELD — Conceptual Parikh-Collision Theorem and Sharp Universal Depth Bound

**Version:** 0.14  
**Date:** 2026-09-01  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** CONCEPTUAL PROOF COMPLETE / TABLE DEPENDENCE REMOVED / UNIVERSAL DEPTH 5 VERIFIED  
**Depends on:** `SOL_QFIELD_CANONICAL_ROUTE_FRAME_v0_12.md`, `SOL_QFIELD_LITERATURE_POSITIONING_v0_13.md`

---

## 1. Executive verdict

The generator-independent collision theorem of v0.12 admits a short conceptual proof. The orbit-by-orbit witness tables are not needed for the theorem itself.

Let

\[
h:\{L,R\}^*\twoheadrightarrow S_3
\tag{1}
\]

be any history morphism with noncommuting generator images

\[
p=h(L),\qquad q=h(R),\qquad pq\ne qp.
\tag{2}
\]

Define \(g\sim_P g'\) when there exist words \(w,w'\) with the same Parikh vector such that

\[
h(w)=g,\qquad h(w')=g'.
\tag{3}
\]

Then

\[
\boxed{
g\sim_P g'\quad\Longleftrightarrow\quad \operatorname{sgn}(g)=\operatorname{sgn}(g')}
\tag{4}
\]

for distinct \(g,g'\in S_3\).

Equivalently, the simple collision graph is exactly

\[
\boxed{
\Gamma_P=K_3[A_3]\sqcup K_3[S_3\setminus A_3].
}
\tag{5}
\]

The proof has only three ingredients:

1. Parikh-equivalent words have the same image parity;
2. \(LR\) and \(RL\) are a nontrivial collision seed;
3. Parikh-collision is closed under adding the same left and right contexts.

A finite exhaustive verifier additionally shows that all six collision edges are already witnessed by histories of length at most five for **every one of the 18 ordered noncommuting generator pairs in \(S_3\)**, and that five is the sharp universal bound:

\[
\boxed{M_{\rm universal}=5.}
\tag{6}
\]

For 12 generator pairs depth four suffices; for the remaining 6 Coxeter-type ordered pairs depth five is necessary.

---

## 2. Parikh equivalence

For a word \(w\in\{L,R\}^*\), define

\[
\Psi(w)=(|w|_L,|w|_R)\in\mathbb N^2.
\tag{7}
\]

Write

\[
w\equiv_P w'
\tag{8}
\]

iff

\[
\Psi(w)=\Psi(w').
\tag{9}
\]

For the FCOA root-comb action, this is exactly the native reconvergence relation away from the root:

\[
\mathsf F_w(x_k)=\rho^{|w|_R}(x_k).
\tag{10}
\]

Thus the abstract theorem applies directly to the safe root-comb histories.

---

## 3. Lemma A — parity is a Parikh invariant

### Lemma 3.1

If

\[
w\equiv_P w',
\tag{11}
\]

then

\[
\operatorname{sgn}(h(w))
=
\operatorname{sgn}(h(w')).
\tag{12}
\]

### Proof

Let

\[
p=h(L),\qquad q=h(R).
\tag{13}
\]

Since sign is a group homomorphism,

\[
\operatorname{sgn}(h(w))
=
\operatorname{sgn}(p)^{|w|_L}
\operatorname{sgn}(q)^{|w|_R}.
\tag{14}
\]

The right-hand side depends only on \(\Psi(w)\). \(\square\)

Hence collision edges cannot cross the parity bipartition.

---

## 4. Lemma B — contextual closure

### Lemma 4.1 — Context transport

Suppose

\[
g\sim_P g'.
\tag{15}
\]

Then for every \(x,y\in S_3\),

\[
\boxed{xgy\sim_P xg'y.}
\tag{16}
\]

### Proof

Choose Parikh-equivalent words \(w,w'\) with

\[
h(w)=g,\qquad h(w')=g'.
\tag{17}
\]

Because \(h\) is onto, choose words \(u,v\) with

\[
h(u)=x,\qquad h(v)=y.
\tag{18}
\]

Then

\[
uwv\equiv_P uw'v,
\tag{19}
\]

because the same prefix and suffix add the same letter counts to both words. Their images are

\[
h(uwv)=xgy,
\qquad
h(uw'v)=xg'y.
\tag{20}
\]

Therefore (16) holds. \(\square\)

This is the structural step that makes the full collision graph follow from one seed.

---

## 5. Lemma C — the shortest seed is nontrivial

The words

\[
LR,
\qquad
RL
\tag{21}
\]

have the same Parikh vector

\[
(1,1).
\tag{22}
\]

Their images are

\[
pq,
\qquad
qp.
\tag{23}
\]

By the reversible-separator requirement,

\[
pq\ne qp.
\tag{24}
\]

Thus

\[
\boxed{pq\sim_P qp}
\tag{25}
\]

is a nontrivial collision.

Let

\[
d:=(pq)^{-1}(qp).
\tag{26}
\]

By Lemma 3.1, \(pq\) and \(qp\) have the same parity, so

\[
d\in A_3.
\tag{27}
\]

Since they are distinct,

\[
d\ne e.
\tag{28}
\]

Therefore \(d\) is one of the two 3-cycles.

---

## 6. Theorem A — complete collision classification

### Theorem 6.1 — Parikh-Collision Theorem for \(S_3\)

For distinct \(g,g'\in S_3\),

\[
\boxed{
g\sim_P g'\iff \operatorname{sgn}(g)=\operatorname{sgn}(g').}
\tag{29}
\]

### Proof

The forward implication is Lemma 3.1.

For the reverse implication, take distinct \(u,v\in S_3\) with the same parity. Then

\[
d':=u^{-1}v
\tag{30}
\]

is a nonidentity even element, hence a 3-cycle.

The two nonidentity elements of \(A_3\) are conjugate in \(S_3\). Therefore there exists \(y\in S_3\) such that

\[
y^{-1}dy=d'.
\tag{31}
\]

Set

\[
g_0=pq,
\qquad
g_1=qp,
\tag{32}
\]

so that

\[
g_0^{-1}g_1=d.
\tag{33}
\]

Define

\[
x:=u y^{-1}g_0^{-1}.
\tag{34}
\]

Then

\[
xg_0y=u,
\tag{35}
\]

and

\[
\begin{aligned}
xg_1y
&=u y^{-1}g_0^{-1}g_1y\\
&=u y^{-1}dy\\
&=ud'\\
&=v.
\end{aligned}
\tag{36}
\]

By the seed collision (25) and contextual closure,

\[
xg_0y\sim_P xg_1y.
\tag{37}
\]

Hence

\[
u\sim_P v.
\tag{38}
\]

This proves the reverse implication. \(\square\)

### Corollary 6.2

The collision graph is

\[
\boxed{
\Gamma_P=K_3\sqcup K_3.
}
\tag{39}
\]

The two connected components are exactly the two parity classes of \(S_3\).

---

## 7. Why this proof is stronger than the witness tables

The v0.12 tables established the result by classifying generator orbits and listing six explicit collisions in each representative case.

Theorem 6.1 explains **why** those tables had to work:

\[
\boxed{
\text{one noncommuting Parikh seed}
+
\text{context transport}
+
[S_3,S_3]=A_3
\Longrightarrow
\text{all same-parity collisions}.
}
\tag{40}
\]

The result is therefore not an accidental enumeration of six group elements.

---

## 8. General pattern suggested by the proof

The proof exposes a possible abstraction beyond \(S_3\).

For a finite group \(G\) and a surjective binary morphism

\[
h:\{L,R\}^*\to G,
\tag{41}
\]

Parikh-equivalent words always differ by an element of the commutator subgroup

\[
[G,G].
\tag{42}
\]

A single nontrivial collision seed, together with context transport, can populate conjugacy classes inside \([G,G]\).

For \(S_3\), the special simplification is

\[
[S_3,S_3]=A_3\cong C_3
\tag{43}
\]

and all nonidentity commutators lie in one conjugacy orbit. This collapses the collision relation exactly to parity classes.

This observation may support a later generalization, but no general theorem is claimed here.

---

## 9. Sharp finite depth

The conceptual proof does not optimize the lengths of the contextual words used to transport the seed. For publication and reproducibility, a finite exhaustive calculation was therefore performed.

There are exactly

\[
18
\tag{44}
\]

ordered noncommuting generator pairs \((p,q)\) in \(S_3\).

For each pair, all binary words were enumerated by increasing length and grouped by their Parikh vectors. The induced collision edges were compared with the six target same-parity edges.

The result is:

\[
\boxed{
\begin{array}{c|c}
\text{minimal maximum depth needed} & \text{number of ordered generator pairs}\\
\hline
4 & 12\\
5 & 6
\end{array}
}
\tag{45}
\]

Hence

\[
\boxed{M_{\rm universal}=5.}
\tag{46}
\]

Depth four is not a universal bound, while depth five is.

The six pairs requiring depth five are precisely the ordered transposition/transposition generating pairs.

---

## 10. Publication-grade finite certificate

A supplementary verifier accompanies this report:

`verify_parikh_collision_s3.py`

It checks:

1. all 18 ordered noncommuting pairs;
2. absence of cross-parity collision edges;
3. complete same-parity collision coverage by depth five;
4. failure of universal coverage at depth four;
5. the distribution \(12\) pairs at depth four and \(6\) pairs at depth five.

The conceptual proof remains primary. The script is only a finite certificate and regression test.

---

## 11. Consequence for the route-frame theorem

The v0.12 tight-frame theorem now rests on a conceptual collision classification rather than case tables.

The sequence is

\[
\boxed{
\text{FCOA root-comb endpoint}
\Rightarrow
\text{Parikh fibers}
\Rightarrow
K_3\sqcup K_3
\Rightarrow
\text{two orthogonal }A_2\text{ edge frames}
\Rightarrow
M_2(\mathbb R).
}
\tag{47}
\]

The first implication is FCOA-specific. The middle collision theorem is an abstract binary-history theorem. The last step is classical representation/frame geometry applied to the collision graph.

---

## 12. Updated publication assessment

The major proof-level vulnerability identified in v0.13 has been removed:

- no generator-orbit case table is needed for the main collision theorem;
- the theorem has a short structural proof;
- the finite depth statement has a machine-checkable certificate.

The remaining publication work is now editorial/bibliographic rather than foundational:

1. stronger literature search around Parikh collisions under group morphisms;
2. theorem numbering and notation normalization;
3. independent hostile reread of all dependencies from v0.3 onward;
4. article assembly with explicit separation between robust theorem and Coxeter-only Clifford/CAR corollaries.

Status:

\[
\boxed{\texttt{PUBLICATION CANDIDATE — PROOF CORE STABLE}.}
\tag{48}
\]

---

## 13. References

1. `SOL_QFIELD_CANONICAL_ROUTE_FRAME_v0_12.md`.
2. `SOL_QFIELD_LITERATURE_POSITIONING_v0_13.md`.
3. Standard Parikh-map / commutative-closure theory.
4. Standard finite-group theory of \(S_3\) and \([S_3,S_3]=A_3\).
5. FCOA-Z v1.1, DOI: https://doi.org/10.5281/zenodo.22169264
