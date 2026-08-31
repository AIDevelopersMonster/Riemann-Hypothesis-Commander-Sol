# SOL-QFIELD — Finite Reversible History: the Minimal S3 Separator

**Version:** 0.5  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FIFTH TARGET COMPLETE / R1 PROVED / MINIMAL FINITE GROUP SIZE 6 / SCALAR-PHASE ORDER NO-GO  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264  
**Depends on:** `SOL_QFIELD_MINIMAL_HISTORY_v0_4.md`

---

## 1. Executive verdict

Version 0.4 proved that the native radial associator histories

\[
LR\ne RL
\tag{1}
\]

can be distinguished by a cardinality-minimal 3-state history monoid, but every group or unitary representation of that idempotent monoid collapses the distinction.

The next frontier was therefore:

> Does reversible history separation require unbounded memory, or can a finite group-valued history invariant already distinguish \(LR\) from \(RL\)?

This problem has an exact answer.

### Result A — finite reversible separation exists

Take

\[
S_3=\langle s,t\mid s^2=t^2=(st)^3=1\rangle
\tag{2}
\]

with

\[
s=(12),
\qquad
t=(23).
\tag{3}
\]

Define a word homomorphism

\[
g:\{L,R\}^*\to S_3
\tag{4}
\]

by

\[
g(L)=s,
\qquad
g(R)=t.
\tag{5}
\]

Then

\[
g(LR)=st\ne ts=g(RL).
\tag{6}
\]

Thus a finite group-valued compositional memory distinguishes the native diamond routes.

### Result B — six group states are minimal

Any group image distinguishing \(LR\) and \(RL\) must contain two noncommuting elements. Every group of order less than six is abelian. Hence the group must have at least six elements.

Since \(S_3\) has six elements, the bound is sharp:

\[
\boxed{
\min\{|G|: \exists a,b\in G,\ ab\ne ba\}=6.
}
\tag{7}
\]

Therefore the minimal finite reversible separator has exactly six group states.

### Result C — R1 is proved

The previous trichotomy

- `R0`: every finite reversible quotient collapses the distinction;
- `R1`: a finite reversible separator exists;
- `R2`: only an infinite reversible lift works

is resolved as

\[
\boxed{\texttt{R1}.}
\tag{8}
\]

Moreover, the reversible memory is still a fixed finite fiber over the signed line, so it remains

\[
\boxed{\texttt{1D-CLOSED}.}
\tag{9}
\]

### Result D — scalar phase alone can never encode route order

For **any** group \(G\) and any one-dimensional unitary character

\[
\chi:G\to U(1),
\tag{10}
\]

the target is abelian, so

\[
\chi(ab)=\chi(a)\chi(b)=\chi(b)\chi(a)=\chi(ba).
\tag{11}
\]

Hence no multiplicative scalar phase character can distinguish \(LR\) from \(RL\), even when the history group itself is nonabelian.

This gives a broad no-go theorem:

\[
\boxed{
\text{order-sensitive reversible history}
\not\hookrightarrow
\text{one-dimensional phase memory}.
}
\tag{12}
\]

### Result E — a 2D unitary representation is sufficient

\(S_3\) has its standard faithful two-dimensional real orthogonal representation, hence a two-dimensional unitary representation over \(\mathbb C\). In that representation

\[
U(st)\ne U(ts).
\tag{13}
\]

Thus bounded reversible route memory becomes possible at matrix-valued, not scalar-valued, amplitude level.

This is the most significant structural result of SOL-QFIELD so far: the first nontrivial reversible memory layer is naturally **non-Abelian and at least two-dimensional as a faithful unitary representation**.

No claim is made that this is quantum mechanics or a physical particle degree of freedom.

---

## 2. Source history problem

The radial FCOA rules are

\[
L:\ x_0\oplus x_k=x_k,
\tag{14}
\]

\[
R:\ x_k\oplus x_0=\rho(x_k).
\tag{15}
\]

For \(|k|\ge2\), the native associator diamond gives two histories

\[
LR
\qquad\text{and}\qquad
RL
\tag{16}
\]

that have the same extensional endpoint but distinct intermediate states.

Version 0.4 introduced a finite irreversible memory monoid that separates these words. The present report requires the separating history image itself to be reversible, i.e. group-valued.

---

## 3. Necessary condition: noncommutativity

### Proposition 3.1

Let \(G\) be a group and

\[
\phi:\{L,R\}^*\to G
\tag{17}
\]

a monoid homomorphism. If

\[
\phi(LR)\ne\phi(RL),
\tag{18}
\]

then \(G\) is nonabelian.

### Proof

Write

\[
a=\phi(L),
\qquad
b=\phi(R).
\tag{19}
\]

Then

\[
\phi(LR)=ab,
\qquad
\phi(RL)=ba.
\tag{20}
\]

Condition (18) is exactly

\[
ab\ne ba.
\tag{21}
\]

Therefore \(G\) contains two noncommuting elements and is nonabelian. \(\square\)

### Corollary 3.2

No abelian group-valued invariant can retain the order distinction between the two radial histories.

This applies in particular to additive cyclic phase memories and to every scalar unitary phase group.

---

## 4. Minimal group size

### Lemma 4.1

Every group of order strictly less than six is abelian.

### Proof

Groups of orders \(1,2,3,5\) are cyclic because the nontrivial prime-order cases are cyclic. A group of order \(4\) is isomorphic either to the cyclic group \(C_4\) or to the Klein group \(C_2\times C_2\). Both are abelian. \(\square\)

### Theorem 4.2 — Six-State Lower Bound

If a finite group \(G\) admits a history homomorphism

\[
\phi:\{L,R\}^*\to G
\tag{22}
\]

with

\[
\phi(LR)\ne\phi(RL),
\tag{23}
\]

then

\[
|G|\ge6.
\tag{24}
\]

### Proof

By Proposition 3.1, \(G\) must be nonabelian. Lemma 4.1 excludes all group orders below six. \(\square\)

---

## 5. Theorem A — S3 realizes the lower bound

Let

\[
S_3=\operatorname{Sym}(\{1,2,3\}).
\tag{25}
\]

Choose

\[
s=(12),
\qquad
t=(23).
\tag{26}
\]

### Theorem 5.1 — Minimal Finite Reversible Separator

The unique monoid homomorphism determined by

\[
g(L)=s,
\qquad
g(R)=t
\tag{27}
\]

satisfies

\[
\boxed{g(LR)\ne g(RL).}
\tag{28}
\]

Since \(|S_3|=6\), this is cardinality-minimal among finite group-valued separators.

### Proof

Composition of the two adjacent transpositions in opposite orders gives the two distinct 3-cycles:

\[
st=(123),
\qquad
ts=(132)
\tag{29}
\]

up to the chosen convention for permutation composition. In either convention they are inverse, distinct 3-cycles. Hence

\[
st\ne ts.
\tag{30}
\]

The lower bound is Theorem 4.2, so six is minimal. \(\square\)

### Corollary 5.2 — R1 decision

\[
\boxed{\texttt{R1: finite reversible separator exists}.}
\tag{31}
\]

Neither an infinite group nor an unbounded memory coordinate is required merely to retain the radial route-order distinction reversibly.

---

## 6. Reflection covariance and finite-fiber closure

The labels \(L,R\) refer to the operand slot occupied by the root. Reflection

\[
\nu(x_k)=x_{-k}
\tag{32}
\]

preserves those operand slots. Therefore the same history word is assigned to a reflected evaluation path.

Define the reflected action on the memory group trivially:

\[
\nu_M(g)=g
\qquad(g\in S_3).
\tag{33}
\]

Then

\[
g(\nu\pi)=g(\pi)
\tag{34}
\]

for every radial history \(\pi\).

An enriched endpoint is

\[
(x_k,\sigma),
\qquad
\sigma\in S_3.
\tag{35}
\]

The forgetting map

\[
(x_k,\sigma)\mapsto x_k
\tag{36}
\]

recovers the old FCOA value exactly.

### Proposition 6.1 — Reversible history remains 1D-closed

The minimal finite reversible history separator requires only a fixed six-element fiber over the signed line. Therefore

\[
\boxed{\texttt{R1 is 1D-CLOSED}.}
\tag{37}
\]

No second unbounded coordinate is forced.

---

## 7. Theorem B — universal scalar-phase order obstruction

The earlier 3-state monoid had trivial group images because its distinguishing elements were idempotent. One might hope that after replacing it by the genuine group \(S_3\), scalar unitary phases could distinguish the two route products. They cannot.

### Theorem 7.1 — Scalar Character Order No-Go

Let \(G\) be any group, let \(a,b\in G\), and let

\[
\chi:G\to U(1)
\tag{38}
\]

be any one-dimensional unitary representation. Then

\[
\boxed{\chi(ab)=\chi(ba).}
\tag{39}
\]

Consequently no scalar unitary character of any history group can distinguish the order pair \(LR\) versus \(RL\) through multiplicative history composition.

### Proof

Because \(U(1)\) is abelian,

\[
\begin{aligned}
\chi(ab)
&=\chi(a)\chi(b)\\
&=\chi(b)\chi(a)\\
&=\chi(ba).
\end{aligned}
\tag{40}
\]

This proves the claim. \(\square\)

### Corollary 7.2

The obstruction is not specific to \(S_3\). It is universal for all one-dimensional multiplicative phase representations.

Thus if the route-order distinction itself is the memory one wants to preserve, a scalar phase is structurally too small.

### Interpretation caution

This does **not** say that scalar complex amplitudes never produce interference. Ordinary quantum amplitudes certainly do. The theorem says only that a scalar **group character of an order-sensitive history group** cannot encode the noncommutative distinction \(ab\ne ba\), because every scalar multiplicative target is abelian.

---

## 8. Theorem C — two-dimensional unitary memory is sufficient

The permutation representation of \(S_3\) on \(\mathbb R^3\) leaves invariant the line

\[
\operatorname{span}(1,1,1)
\tag{41}
\]

and its orthogonal complement

\[
V=\{(x_1,x_2,x_3):x_1+x_2+x_3=0\}.
\tag{42}
\]

The subspace \(V\) has real dimension two.

Restrict the permutation action to \(V\) and complexify if desired:

\[
U:S_3\to U(V_\mathbb C).
\tag{43}
\]

### Theorem 8.1 — Minimal Standard Unitary Witness

The standard two-dimensional representation is faithful. Hence

\[
\boxed{
U(st)\ne U(ts).
}
\tag{44}
\]

Therefore a two-dimensional unitary memory space can retain the radial route-order distinction reversibly.

### Proof

If a permutation acts trivially on both the invariant line \(\operatorname{span}(1,1,1)\) and its orthogonal complement \(V\), then it acts trivially on all of \(\mathbb R^3\), so the permutation is the identity. Since every permutation already fixes the invariant line pointwise, the restriction to \(V\) has trivial kernel. Thus the standard representation is faithful.

Because \(st\ne ts\), faithfulness implies

\[
U(st)\ne U(ts).
\]

The matrices are orthogonal on the real plane and hence unitary after complexification. \(\square\)

### Corollary 8.2

For order-sensitive reversible route memory,

\[
\boxed{
\text{one complex dimension is impossible, while two dimensions suffice for the minimal }S_3\text{ witness}.
}
\tag{45}
\]

This is a representation-dimension statement about the history separator, not a derivation of a physical Hilbert space.

---

## 9. What has and has not emerged

The sequence of results now reads:

\[
\text{native base diamond}
\to
\text{3-state finite irreversible memory}
\to
\text{6-state finite reversible memory}
\to
\text{2D faithful unitary representation}.
\tag{46}
\]

Every arrow above is mathematically explicit.

But several essential quantum ingredients are still missing:

1. no rule says physical states are vectors in the representation space;
2. no FCOA-internal principle selects the \(S_3\) representation as dynamics;
3. no coherent sum over parallel histories has been derived;
4. no Born/measurement rule has been derived;
5. no tensor product or many-particle structure has been derived;
6. no CAR/CCR or particle-antiparticle field interpretation follows.

Thus the correct conclusion is not “FCOA has generated quantum mechanics.”

The correct conclusion is:

\[
\boxed{
\text{native FCOA route-order memory admits a bounded non-Abelian reversible encoding.}
}
\tag{47}
\]

---

## 10. Refined QFIELD ladder

The ladder is now:

### QF2.5 — native evaluation diamonds

Present in legacy FCOA.

### QF3a-F — minimal finite irreversible memory

3 states, proved minimal.

### QF3a-R — minimal finite reversible group memory

6 states via \(S_3\), proved minimal among finite groups.

### QF3a-U — faithful unitary history representation

2 complex dimensions suffice via the standard \(S_3\) representation; 1D scalar characters cannot preserve order.

### QF3b — coherent parallel-history summation

Still absent.

### QF4 — state-space dynamics with norm/Born structure

Still absent.

### QF5 — Fock/CAR field-statistics structure

Still absent.

Symbolically,

\[
\boxed{
QF2.5
<
QF3a\text{-}F(3)
<
QF3a\text{-}R(6)
<
QF3a\text{-}U(2D)
<
QF3b
<
QF4
<
QF5.
}
\tag{48}
\]

The numbers in parentheses are proven minimal sizes/dimensions for the specific radial route-order separation problem.

---

## 11. R0/R1/R2 decision

### R0 — finite reversible no-go

**False.** \(S_3\) provides a finite group separator.

### R1 — finite reversible separator

**True.** Minimal group size is six.

### R2 — unbounded reversible memory barrier

**False for route-order separation itself.** No unbounded memory is needed for this task.

Therefore

\[
\boxed{\texttt{R1}.}
\tag{49}
\]

This closes the reversible-history-size question for the native radial pair.

---

## 12. Line-completion consequence

The new result is another negative control on premature dimension claims.

Even after requiring:

- distinct histories;
- compositional memory;
- reversibility;
- a faithful unitary representation of that memory,

one still needs only a fixed finite internal fiber over the one-dimensional signed line.

Therefore

\[
\boxed{
\text{finite non-Abelian reversible history memory is not DIMENSION-FORCING}.
}
\tag{50}
\]

A later emergent-dimension claim must rely on independent unbounded iteration/transport, not merely on noncommuting internal history states.

---

## 13. Hostile audit

### “S3 means a new physical symmetry has been discovered.”

**Rejected.** \(S_3\) is the cardinality-minimal abstract finite group capable of representing two noncommuting history generators. No physical symmetry identification is claimed.

### “The 2D representation is the qubit.”

**Rejected.** A two-dimensional complex representation space is not by itself a qubit theory. State preparation, superposition semantics, allowed dynamics, measurement and Born probabilities are still absent.

### “The two routes now have different scalar phases.”

**Rejected.** Theorem 7.1 proves that no one-dimensional unitary character can distinguish \(LR\) from \(RL\).

### “Non-Abelian history implies non-Abelian particles/anyons.”

**Rejected.** This is rule-order memory in an evaluation-history quotient, not braid statistics or topological charge.

### “Six states create another coordinate dimension.”

**Rejected.** They are a bounded internal fiber.

---

## 14. Publication decision

The publication recommendation is still

`HOLD FOR APPLIED-DIRECTIONS SYNTHESIS`,

but SOL-QFIELD has now crossed an internal mathematical maturity threshold. Versions 0.3-0.5 form a coherent abstract result independent of the original QFT analogy:

\[
\boxed{
\text{native associator diamond}
\to
\text{minimal finite memory}
\to
\text{minimal finite reversible memory}
\to
\text{minimal faithful unitary representation dimension}.
}
\tag{51}
\]

This material may become separately publishable as an FCOA history-memory note if the next missing step—coherent parallel-history composition—either receives a canonical construction or a sharp no-go theorem.

---

## 15. Next strike — parallel-history addition selector

The reversible history problem is closed. The next unresolved boundary is not representation but **addition of parallel histories**.

We now have two distinct route operators

\[
U_LU_R
\qquad\text{and}\qquad
U_RU_L
\tag{52}
\]

in a finite unitary representation. But ordinary group composition supplies multiplication/composition only. It does not tell us to form

\[
U_LU_R+U_RU_L,
\tag{53}
\]

nor how such a sum should be normalized or observed.

The next exact question is therefore:

\[
\boxed{
\text{Can an additive law on parallel FCOA histories be derived from existing structure,}
\text{ rather than imported as vector-space linearity?}
}
\tag{54}
\]

Possible outcomes:

### A0 — no additive selector

Composition and reflection determine no canonical parallel-history sum. Then the quantum analogy stops at non-Abelian reversible memory.

### A1 — finite semiring/enrichment selector

A natural FCOA-internal enrichment determines a unique or finite family of parallel-combination laws, still without a full Hilbert structure.

### A2 — linearization forced

Any nontrivial conservative parallel-history combination satisfying natural coherence axioms factors through a linear/group-algebra completion. This would be the first rigorous bridge from FCOA history to a genuinely linear state/process layer.

The `A0/A1/A2` problem is now the sharp SOL-QFIELD frontier.
