# HATTER-SOL-03 · Query-Ladder Gap Theorem

## 0. Motivation

The previous strike showed a qualitative contrast:

- a fixed finite number of static bits on each predecessor edge does not recover exact depth;
- a reusable binary divisibility query applied to all internally generated prime powers does recover exact depth and hence rigidity.

The present note identifies the exact invariant controlling this transition.

The correct object is not merely the number of questions, nor the density of allowed questions. It is the **gap profile of the query ladder**.

---

# 1. Local depth as a threshold-search problem

Fix a prime \(q\), and for a prime \(p\) with \(q\mid p-1\), define

\[
e_q(p)=v_q(p-1)\in\mathbb N_{\ge1}.
\]

A threshold query at exponent \(k\ge1\) asks

\[
T_k(e)=\mathbf 1[k\le e].
\]

In arithmetic form this is exactly the yes/no question

\[
q^k\mid p-1\ ?
\]

Let

\[
A=\{a_0<a_1<a_2<\cdots\}\subseteq\mathbb N_{\ge1}
\]

be an unbounded set of allowed threshold exponents, with \(a_0=1\).

Define the ladder signature

\[
\sigma_A(e)
=
(T_a(e))_{a\in A}.
\]

---

# 2. Gap cells

For consecutive ladder points \(a_j<a_{j+1}\), define the gap

\[
g_j=a_{j+1}-a_j
\]

and the corresponding ambiguity cell

\[
I_j=[a_j,a_{j+1}-1]\cap\mathbb N.
\]

Then

\[
|I_j|=g_j.
\]

## Theorem 2.1 — exact gap classification

For \(e,f\ge1\),

\[
\boxed{
\sigma_A(e)=\sigma_A(f)
\iff
\text{$e$ and $f$ lie in the same gap cell }I_j.
}
\]

### Proof

The signature records exactly which allowed thresholds have already been crossed.

If \(e,f\in I_j\), then for every \(a\in A\), either \(a\le a_j\le e,f\), or \(a\ge a_{j+1}>e,f\). Hence every threshold answer agrees.

Conversely, if \(e<f\) lie in different cells, then some allowed threshold \(a\in A\) satisfies

\[
e<a\le f,
\]

so \(T_a(e)=0\) and \(T_a(f)=1\). \(\square\)

Thus the residual local uncertainty after observing the entire ladder is exactly the size of the corresponding gap.

---

# 3. Exact recovery criterion

## Corollary 3.1 — threshold completeness

The ladder signature recovers every depth \(e\) exactly if and only if

\[
\boxed{
A=\mathbb N_{\ge1}.
}
\]

Equivalently,

\[
\boxed{
g_j=1\text{ for every }j.}
\]

### Proof

By Theorem 2.1 exact recovery is equivalent to every ambiguity cell having size one. This is equivalent to every consecutive integer appearing as a threshold. \(\square\)

This gives a sharp minimality law:

> Among fixed threshold subfamilies, the full prime-power ladder \(q,q^2,q^3,\ldots\) is not merely sufficient for exact depth recovery. It is necessary.

A proper sparse threshold ladder cannot recover all valuations exactly, even if every one of its answers is known simultaneously.

---

# 4. Adaptivity restricted to the same sparse ladder does not help

One might hope that an adaptive decision tree could compensate for missing thresholds.

It cannot, if all allowed questions still come from the same set \(A\).

## Corollary 4.1

If \(e,f\) lie in one gap cell \(I_j\), then **every adaptive protocol using only threshold queries \(T_a\) with \(a\in A\)** receives exactly the same transcript on \(e\) and \(f\).

Hence no adaptive strategy restricted to \(A\) can recover exact depth unless \(A=\mathbb N_{\ge1}\).

### Proof

Every allowed query has the same answer on \(e\) and \(f\), so every decision tree follows the same branch on both inputs. \(\square\)

The obstacle is therefore not a poor search strategy. It is the absence of the missing thresholds themselves.

---

# 5. Static side information: exact bit lower bound

Suppose the ladder signature is augmented by \(b\) additional static binary bits

\[
\beta(e)\in\{0,1\}^b.
\]

Inside a gap cell \(I_j\), the ladder contributes no further distinction, so the auxiliary bits must separate all \(g_j\) possible depths.

## Theorem 5.1 — static completion bound

If the combined code

\[
(\sigma_A(e),\beta(e))
\]

is injective, then

\[
\boxed{
g_j\le2^b\quad\text{for every }j.}
\]

Equivalently,

\[
\boxed{
b\ge\sup_j\lceil\log_2 g_j\rceil.}
\]

Conversely, as a purely information-theoretic statement, if

\[
\sup_j g_j\le2^b,
\]

then one can assign \(b\)-bit local ranks inside each gap cell and make the combined code injective.

### Proof

Within one cell \(I_j\), all ladder signatures are identical. The \(b\) auxiliary bits provide at most \(2^b\) codewords. Pigeonhole gives the lower bound. The converse is obtained by assigning distinct binary labels to the at most \(2^b\) elements of each cell. \(\square\)

Important scope note: the converse is only an information-theoretic coding statement. It does not assert that the required auxiliary labeling is first-order definable in a given arithmetic structure.

---

# 6. Adaptive completion with unrestricted thresholds

Now suppose the coarse ladder \(A\) is only the first stage. Once the cell \(I_j\) is known, allow arbitrary further threshold queries

\[
T_m(e)=\mathbf 1[m\le e]
\]

with \(m\in\mathbb N\).

## Theorem 6.1 — exact adaptive completion cost

For a gap cell of size

\[
g_j=a_{j+1}-a_j,
\]

the minimum worst-case number of additional binary threshold queries required to recover \(e\) exactly is

\[
\boxed{
\lceil\log_2 g_j\rceil.
}
\]

### Proof

Lower bound: \(g_j\) possibilities require at least \(\lceil\log_2 g_j\rceil\) binary transcripts.

Upper bound: threshold comparisons on a finite ordered interval admit ordinary binary search, which identifies one of \(g_j\) ordered values in \(\lceil\log_2 g_j\rceil\) queries. \(\square\)

Thus the gap profile gives not only a yes/no criterion for exactness, but the exact residual binary query complexity.

---

# 7. Dyadic ladder theorem

Take

\[
A_{\mathrm{dyad}}
=
\{1,2,4,8,16,\ldots\}.
\]

For

\[
2^n\le e<2^{n+1},
\]

the ladder signature determines only the dyadic cell

\[
I_n=[2^n,2^{n+1}-1],
\]

whose size is

\[
|I_n|=2^n.
\]

Therefore:

## Corollary 7.1 — dyadic ambiguity

The dyadic ladder alone cannot recover exact depth.

No adaptive strategy using only dyadic thresholds can recover exact depth.

No fixed number \(b\) of additional static bits can repair the dyadic ladder for all depths.

### Proof

The gaps are

\[
g_n=2^n,
\]

which are unbounded. Apply Theorems 2.1 and 5.1. \(\square\)

## Corollary 7.2 — exact dyadic completion law

After the dyadic ladder has located

\[
e\in[2^n,2^{n+1}-1],
\]

exactly

\[
\boxed{n}
\]

additional unrestricted binary threshold queries are necessary and sufficient in the worst case.

### Proof

The interval has size \(2^n\), so Theorem 6.1 gives

\[
\lceil\log_2 2^n\rceil=n.
\]

\(\square\)

This is the exact minimality theorem sought after the previous strike.

---

# 8. Every depth occurs on actual prime targets

The gap theorem above is abstract in the exponent variable. We now show that its ambiguity is genuinely realized in the prime world.

## Lemma 8.1 — exact valuation realization

Fix a prime \(q\) and an integer \(e\ge1\). Then there are infinitely many primes \(p\) such that

\[
\boxed{v_q(p-1)=e.}
\]

### Proof

Choose the arithmetic progression

\[
p\equiv1+q^e\pmod{q^{e+1}}.
\]

The residue \(1+q^e\) is coprime to \(q^{e+1}\), so Dirichlet's theorem gives infinitely many primes in this progression.

For every such prime,

\[
p-1\equiv q^e\pmod{q^{e+1}},
\]

hence \(q^e\mid p-1\) but \(q^{e+1}\nmid p-1\). Therefore

\[
v_q(p-1)=e.
\]

\(\square\)

## Consequence

Every exponent in every ladder gap occurs for infinitely many prime targets.

Therefore the ambiguity in Theorems 2.1–7.2 is not an artefact of allowing impossible exponent values. It is realized infinitely often within the actual \(p-1\) arithmetic of primes.

For the dyadic ladder, for every \(n\) and every

\[
e\in[2^n,2^{n+1}-1],
\]

there are infinitely many primes \(p\) with that exact \(q\)-adic predecessor depth.

---

# 9. Density is not the correct invariant

The exact invariant is the gap profile

\[
(g_j)_j,
\]

not the natural density of \(A\).

Two consequences are immediate.

## Corollary 9.1

If \(A\) has bounded gaps

\[
\sup_jg_j\le G,
\]

then the residual static ambiguity can be resolved information-theoretically with

\[
\lceil\log_2G\rceil
\]

extra bits.

If \(A\) has unbounded gaps, no fixed finite number of static bits suffices.

## Corollary 9.2

If \(A\subseteq\mathbb N\) has natural density zero, then its gaps are unbounded. Consequently, no zero-density threshold ladder can be completed to exact depth recovery by a fixed finite number of additional static bits.

### Proof

A set with gaps bounded by \(G\) has lower density at least \(1/G\). Therefore density zero forces unbounded gaps. \(\square\)

This creates an instructive contrast with HATTER-SOL-02:

- a globally separating family of prime probes can be arbitrarily sparse and still force rigidity;
- a local threshold ladder with zero density necessarily leaves unbounded unresolved depth intervals unless it is supplemented adaptively.

So sparsity behaves differently in global pair separation and local depth reconstruction.

---

# 10. The full ladder is the unique exact static threshold architecture

Let

\[
J_A(a,p)
\]

mean, informally, that \(a=q^k\) is an allowed query power with \(k\in A\) and \(q^k\mid p-1\).

Then the local response pattern at base \(q\) is exactly \(\sigma_A(v_q(p-1))\).

Hence:

## Theorem 10.1 — minimal threshold architecture

Among all fixed exponent-threshold families \(A\subseteq\mathbb N_{\ge1}\) containing \(1\), exact recovery of \(v_q(p-1)\) for every prime target \(p\) and every support prime \(q\) is possible from the raw threshold signature if and only if

\[
\boxed{A=\mathbb N_{\ge1}.}
\]

By Lemma 8.1, necessity already holds when the target is restricted to actual primes.

Thus the full adaptive relation \(J\) from the previous strike uses a threshold family that is minimal in a very strong sense: **every integer threshold is required somewhere to distinguish two adjacent possible depths.**

---

# 11. New HATTER-SOL law: the gap profile of self-questioning

The third paper can now sharpen its central formula.

HATTER-SOL-02:

\[
\text{individuality}=\text{sufficiency of separation}.
\]

Early HATTER-SOL-03:

\[
\text{self-generated individuality}
=
\text{finite query rule}
+
\text{internal query generation}
+
\text{well-founded termination}.
\]

The present theorem adds the missing quantitative layer:

\[
\boxed{
\text{residual uncertainty of a query ladder}
=
\text{its gap profile}.
}
\]

and

\[
\boxed{
\text{adaptive completion cost of a gap of size }g
=
\lceil\log_2g\rceil.
}
\]

The cup does not merely need to ask more questions. It must be able to place new questions **inside the unresolved gap**.

---

# 12. Literary image

The dyadic ladder gives a clean Alice image.

The Caterpillar asks only:

- are you at least 1?
- at least 2?
- at least 4?
- at least 8?
- at least 16?

Alice can then say which room she is in, but not which chair.

To identify the chair, the next question must be asked **inside the room**.

That is the exact mathematical difference between a sparse fixed questionnaire and a self-generated adaptive interrogation.

This is our modern allegory, not a claim about Carroll's intended mathematics.

---

# 13. Publication status after this strike

HATTER-SOL-03 now has a coherent theorem spine:

1. finite-seed impossibility in pure multiplication;
2. anonymous-probe homogeneity warning;
3. exact-depth well-founded rigidity;
4. directed-support reduction to arithmetic multiplicity fibers;
5. static one-, two-, and three-bit local barriers;
6. adaptive binary relation recovering exact depth;
7. **query-ladder gap theorem**;
8. **dyadic exact completion law**;
9. **prime realization of every local depth by Dirichlet**;
10. threshold-family minimality: the full ladder is necessary and sufficient for raw exact depth recovery.

The mathematical threshold for an HATTER-SOL-03 preprint is now essentially crossed.

The remaining high-value strike should be one of two things:

- a hostile literature audit focused on Pratt trees, prime-chain automorphisms, threshold-query/search theory, and model-theoretic definability of the relation \(J\); or
- a final attempt to weaken \(J\) outside the threshold-family model, e.g. replace all powers \(q^k\) by a richer but proper internally generated subfamily and prove an exact impossibility/possibility theorem.

At this stage additional theorem hunting is optional rather than necessary for publication.