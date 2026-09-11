# HATTER-SOL-05 · Hostile Proof and Literature Audit

**Audit date:** 2026-09-11  
**Scope:** current research package in `papers/HATTER-SOL/05-MISSING-GUEST/`  
**Target:** determine whether the branch is mathematically coherent, which claims survive hostile checking, where the literature boundary lies, and whether the fifth HATTER-SOL note has crossed the publication threshold.

---

# 0. Executive verdict

The central open problem remains unresolved:

\[
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\},
\qquad
\Pi=(\mathbb P,D),\quad D(q,p)\iff q\mid p-1.
\]

The current HATTER-SOL-05 package does **not** prove that \((3\ 5)\) dies, and does **not** prove that it survives unconditionally.

However, hostile checking finds a coherent structural theorem package around the survival problem. No fatal defect was found in the following core results:

1. finite fixed-divisor coverings cannot cover an exact-support candidate family;
2. the common-odd-divisor/cyclotomic obstruction has a genuine dimension jump at \(|S|=1\to2\);
3. the first local sieve distinguishes the \(\{2,3\}\) and \(\{2,5\}\) parameter spaces by a rigorous \(3/2\) factor;
4. the one-prime local divisor density is controlled by the subgroup \(H_\ell(S)\);
5. the \(3\)-versus-\(5\) local sieve gap persists down 3-pure descendant chains;
6. the multiplicity tower is cardinality-blind to quantitative asymptotic differences once both exact fibers are infinite;
7. Higher-Fiber Infinitude (HFI), which does **not** require infinitely many Fermat primes, forces every permutation of the actually existing Fermat primes to extend globally;
8. under the all-finite exact-fiber condition (FFC), survival at every finite Pratt height implies global survival by König compactness, hence global death has a finite-height obstruction family.

There are nevertheless mandatory publication patches. Two statements are currently too broad, and several editorial claims must be narrowed.

The correct verdict is therefore

\[
\boxed{
\text{PUBLICATION THRESHOLD REACHED FOR A STRUCTURAL HATTER-SOL NOTE,}
}
\]

\[
\boxed{
\text{BUT ONLY AFTER THE MANDATORY PATCHES BELOW.}
}
\]

This is a threshold for **HATTER-SOL-05 as a structural continuation**, not a claim that the radical-predecessor automorphism problem has been solved.

---

# 1. Continuity audit: is this really the fifth paper?

Yes.

HATTER-SOL-01 starts from

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P),
\]

while full natural arithmetic is rigid. The series asks where prime-renaming symmetry disappears as arithmetic structure is restored.

HATTER-SOL-03 reaches rigidity using a strong exact-predecessor relation. HATTER-SOL-04 removes multiplicities from \(p-1\) and retains only

\[
D(q,p)\iff q\mid p-1.
\]

HATTER-SOL-05 then tests the smallest explicit surviving transposition

\[
\tau=(3\ 5),
\qquad
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

Thus the forms

\[
1+\prod_{q\in S}q^{e_q}
\]

are not an unrelated excursion into special primes. They are precisely the exact predecessor fibers that control whether a prime permutation from the pure multiplicative world survives in the radical-predecessor reduct.

**Verdict:** continuity with HATTER-SOL-01 is genuine and should be made explicit in the published introduction.

---

# 2. Audit of the finite fixed-divisor escape theorem

For finite \(S\ni2\) and finite prime set \(T\), the note chooses

\[
m_q
=
\operatorname{lcm}_{\ell\in T\setminus S}
\operatorname{ord}_\ell(q)
\]

and studies

\[
N_t=1+\prod_{q\in S}q^{tm_q}.
\]

For \(\ell\in S\),

\[
N_t\equiv1\pmod\ell.
\]

For \(\ell\notin S\),

\[
q^{tm_q}\equiv1\pmod\ell
\]

for all \(q\in S\), so

\[
N_t\equiv2\pmod\ell.
\]

The only possible problem would be \(\ell=2\), but \(2\in S\), so the second case never contains \(\ell=2\).

Therefore

\[
\gcd\left(N_t,\prod_{\ell\in T}\ell\right)=1
\]

for all \(t\ge1\).

**Verdict:** proof correct.

### Scope correction

The corollary should say:

> no finite set of **fixed prime divisors** covers the whole exact-support family.

It should **not** be inflated into a claim that every conceivable finite congruence argument is impossible. A cross-level or exponent-dependent congruence mechanism is not excluded by this theorem.

### Strengthening available from the generalized Fermat spine

Fix any positive exponent vector \(\mathbf m\) and put

\[
A=\prod_{q\in S}q^{m_q}.
\]

The subsequence

\[
A^{2^k}+1
\]

is pairwise coprime because for \(j<k\),

\[
A^{2^k}+1\equiv2\pmod{A^{2^j}+1},
\]

and all terms are odd. Hence every fixed prime divides at most one term of this spine. Therefore, for **any** finite prime set \(T\), all but finitely many terms of one fixed spine avoid every prime in \(T\).

This is cleaner than choosing the exponent vector after \(T\) is given. The identity itself is classical; the useful point here is its consequence for the exact-support programme.

---

# 3. Audit of the cyclotomic common-divisor theorem

Suppose

\[
N_S(\mathbf e)=1+\prod_{i=1}^k q_i^{e_i}
\]

is prime. If an odd integer \(d>1\) divides every \(e_i\), then

\[
N_S(\mathbf e)=A^d+1
\]

with \(A>1\), and because \(d\) is odd,

\[
A^d+1=(A+1)(A^{d-1}-A^{d-2}+\cdots-A+1).
\]

Thus primality forces

\[
\gcd(e_1,\ldots,e_k)=2^r.
\]

**Verdict:** correct; classical algebraic factorization, not a priority claim.

For \(k=1\), this recovers the Fermat exponent restriction. For \(k\ge2\), Möbius inversion over odd common divisors gives density

\[
\sum_{d\text{ odd}}\frac{\mu(d)}{d^k}
=
\prod_{\ell\text{ odd}}(1-\ell^{-k})
=
\frac1{\zeta(k)(1-2^{-k})}.
\]

For \(k=2\), this is \(8/\pi^2\).

**Verdict:** correct.

The phrase “dimension jump” is acceptable as the paper's structural terminology, provided the underlying density calculation is not presented as a new classical number-theory theorem.

---

# 4. Audit of the \(\{2,3\}\) versus \(\{2,5\}\) local sieve

For

\[
1+2^a5^b,
\]

modulo \(3\),

\[
2^a5^b\equiv(-1)^{a+b},
\]

so odd \(a+b\) gives divisibility by \(3\). Thus the local survival fraction is \(1/2\).

For

\[
1+2^a3^b,
\]

modulo \(5\), since \(3\equiv2^3\), divisibility by \(5\) is equivalent to

\[
a+3b\equiv2\pmod4.
\]

Exactly one quarter of residue pairs mod \(4\) are forbidden, so the local survival fraction is \(3/4\).

Because common multiplication of \((a,b)\) by an odd integer preserves the relevant bad class, Möbius inversion over odd common divisors combines with these local conditions. Hence the combined densities are

\[
\frac6{\pi^2}
\quad\text{and}\quad
\frac4{\pi^2},
\]

with ratio

\[
\boxed{\frac32}.
\]

**Verdict:** correct.

### Weighted-by-size asymptotics

The manuscript also states

\[
A_{23}(X)
\sim
\frac{3}{\pi^2\log2\log3}(\log X)^2,
\]

\[
A_{25}(X)
\sim
\frac{2}{\pi^2\log2\log5}(\log X)^2.
\]

The constants are consistent with:

1. the area of the triangle
   \[
   a\log2+b\log q\le\log X;
   \]
2. Möbius inversion over odd common divisors;
3. periodic residue-class densities \(3/4\) and \(1/2\).

No counterexample to the constants was found. However the current source gives only a proof sketch.

**Mandatory publication action:** either expand this to a full lattice-point/Möbius proof with an explicit \(o((\log X)^2)\) remainder, or label it as a proposition with proof supplied in an appendix. Do not leave a theorem with only a sketch in the publication candidate.

---

# 5. Audit of the one-prime local divisor density

For \(\ell\notin S\), let

\[
H_\ell(S)=\langle q\bmod\ell:q\in S\rangle.
\]

Over the finite exponent-period torus, the map

\[
\mathbf e\mapsto\prod_{q\in S}q^{e_q}\pmod\ell
\]

is a surjective homomorphism onto \(H_\ell(S)\). Every fiber therefore has the same size. Hence

\[
\delta_\ell(S)
=
\begin{cases}
|H_\ell(S)|^{-1},&-1\in H_\ell(S),\\
0,&-1\notin H_\ell(S).
\end{cases}
\]

**Verdict:** correct.

For \(3\) and \(5\), because \(2\) generates the full unit groups,

\[
3\notin S\Rightarrow\delta_3(S)=\frac12,
\qquad
5\notin S\Rightarrow\delta_5(S)=\frac14.
\]

**Verdict:** correct.

---

# 6. Audit of hereditary descendant sieve pressure

If \(S\) contains \(2,3\) but not \(5\), and

\[
p\in X_S,
\]

then every predecessor of \(p\) is smaller than \(p\), so \(p>\max S\), and \(p\ne5\). Adjoining \(p\) therefore preserves the property “contains 3, omits 5”. Under an extension of \((3\ 5)\), the image support contains \(5\) and omits \(3\).

The local survival factors remain

\[
\frac34
\quad\text{versus}\quad
\frac12
\]

at every such stage.

The manuscript defines

\[
\mathfrak P_5(\mathcal S)
=
\prod_j(1-\delta_5(S_j)),
\qquad
\mathfrak P_3(g\mathcal S)
=
\prod_j(1-\delta_3(gS_j)),
\]

so the ratio is tautologically

\[
\left(\frac32\right)^{m+1}.
\]

**Verdict:** algebra correct.

### Mandatory interpretation patch

\(\mathfrak P\) is an **external bookkeeping functional**. It is not a joint probability or joint density of a single common sample space across descendant levels. The publication must state this immediately where \(\mathfrak P\) is defined.

---

# 7. Cardinality wall

Every exact fiber is a subset of the countable set \(\mathbb P\). Therefore every infinite exact fiber has cardinality \(\aleph_0\).

Thus if both \(X_S\) and \(X_T\) are infinite,

\[
\mu(S)=\mu(T)=\aleph_0
\]

no matter how different their parameter-space densities, counting constants, or prime-size distributions are.

This is exactly the information loss relevant to the multiplicity tower, because one-step extension depends on equality of the fiber cardinalities.

**Verdict:** correct, elementary, strategically important; do not oversell it as a deep new set-theoretic theorem.

---

# 8. Mandatory correction to the descendant “no-go theorem”

The current descendant note states too broadly that no argument based solely on finitely many fixed congruence divisors at finitely many exact-descendant levels can produce a killing certificate.

What has actually been proved is narrower:

- each individual exact-support candidate family escapes every finite set of fixed prime divisors;
- finitely many local divisor tests can leave quantitative asymmetries without giving cardinality asymmetry;
- if two paired fibers are both infinite, those quantitative differences are invisible to the multiplicity tower.

This does **not** formally exclude every possible finite system of congruence constraints involving correlations between several levels, or divisors depending on earlier chosen vertices.

### Required replacement

Replace the broad theorem by a precise statement such as:

> **Levelwise fixed-divisor-cover barrier.** A killing certificate cannot be obtained merely by exhibiting, at finitely many individual supports, finite fixed sets of prime divisors whose union is asserted to divide every candidate in those support families; no such finite fixed-divisor cover exists for any one of the families.

The more ambitious cross-level statement should remain an open strategy question unless separately proved.

This is the most important proof-scope correction found by the audit.

---

# 9. Audit of HFI

HFI states

\[
\mu(S)=\aleph_0
\qquad
\text{for every finite }S\ni2,\ S\ne\{2\}.
\]

For every level \(n\ge1\), a support generating a vertex of level \(n+1\) contains an odd predecessor, hence is not \(\{2\}\). Therefore HFI makes every relevant paired fiber countably infinite, so

\[
E_n=G_n
\]

and the restriction map

\[
G_{n+1}\to G_n
\]

is surjective for every \(n\ge1\).

Starting with any permutation of the actually existing Fermat-prime fiber at level one, recursive lifting and the inverse-limit theorem produce a global automorphism.

In particular,

\[
\boxed{
\text{HFI}\Longrightarrow(3\ 5)\text{ extends globally}.
}
\]

This does **not** assume infinitely many Fermat primes.

**Verdict:** proof correct and a genuine sharpening of the earlier FSI formulation.

Under HFI, \(X_{\{2,3\}}\) is countably infinite, so its full symmetric group has cardinality \(2^{\aleph_0}\); surjectivity above level two then gives

\[
|\operatorname{Aut}(\Pi)|=2^{\aleph_0}.
\]

**Verdict:** correct, conditional on HFI.

---

# 10. Audit of the finite-fiber compactness theorem

FFC states that every exact fiber has finite cardinality.

Under FFC, \(P_{\le0}=\{2\}\) is finite. If \(P_{\le n}\) is finite, there are only finitely many candidate predecessor supports inside it, and each corresponding fiber is finite. Hence \(L_{n+1}\) and \(P_{\le n+1}\) are finite.

Therefore every finite-height automorphism group \(G_n\) is finite.

For a seed \(\tau\in G_m\), let

\[
T_n(\tau)=\{g\in G_n:g|_{P_{\le m}}=\tau\}.
\]

If every \(T_n(\tau)\) is nonempty, the extension tree is infinite and finitely branching. König's infinity lemma gives an infinite compatible branch, and the inverse-limit theorem gives a global automorphism extending \(\tau\).

Hence under FFC,

\[
\boxed{
\tau\text{ fails globally}
\Longrightarrow
\tau\text{ dies at some finite height}.
}
\]

**Verdict:** correct.

At the least death height, every surviving extension from the previous height violates at least one next-level multiplicity equality. Because the previous extension set is finite, finitely many such support mismatches suffice to block all branches.

**Verdict:** correct.

### Mandatory terminology patch

Call this a **finite obstruction family** or a **structural finite certificate**. Do not imply algorithmic decidability: the exact values \(\mu(S)\) may themselves be arithmetically inaccessible.

### Wording patch

The mixed finite/infinite regime is the regime where noncompact extension-tree failure can occur. It is not justified to call it the only “genuinely difficult” regime; deciding survival in the all-finite regime may also be arithmetically difficult.

---

# 11. Stale single-witness formulation

The initial research state and the continuity bridge contain a formulation of the form

\[
\mu(S)\ne\mu(\tau S)
\Longrightarrow
\tau\text{ dies at finite height}.
\]

This is safe at the immediate next level, or when the action on every member of \(S\) is already forced by the chosen extension.

At later heights, however, the seed \(\tau\) may have several extensions that move the newly created vertices differently. A mismatch against one particular image support need not block every extension branch.

The correct general target is therefore not necessarily one support pair but a finite obstruction tree/family that intersects every surviving branch.

**Mandatory patch:** revise `RESEARCH_STATE.md` and `FROM_FIRST_TO_FIFTH.md` to distinguish the immediate-level witness from the general finite obstruction family.

---

# 12. Literature collision audit

## 12.1 Exact graph question predates the series

The exact digraph

\[
p\to q\iff p\mid q-1
\]

was asked about on MathOverflow by David Feldman in 2012.

Gjergji Zaimi's answer already made several observations extremely close to the broad architecture:

- \(2\) is the unique source;
- primes whose incoming set is exactly \(\{2\}\) are the Fermat primes;
- one may stratify primes by exact sets of incoming predecessors;
- under a strong infinitude conjecture for primes
  \[
  1+\prod p_i^{a_i},
  \]
  many automorphisms should exist;
- if instead all exact-support fibers were finite and their sizes sufficiently distinguishing, rigidity could result.

Therefore HATTER-SOL-05 must **not** claim priority for the idea of exact predecessor fibers, nor for the broad “infinitely many fibers give symmetry / finite distinct fibers may give rigidity” dichotomy.

What the current branch adds is a more explicit multiplicity-tower formalism inherited from HATTER-SOL-04 and then the new structural consequences developed here: HFI without Fermat infinitude, finite fixed-divisor escape, the cyclotomic dimension comparison, local 3-versus-5 sieve pressure, cardinality loss, and the FFC/König finite-obstruction formulation.

Source: MathOverflow, “Automorphisms of a certain digraph defined on the set of primes?” (2012), https://mathoverflow.net/questions/102907/automorphisms-of-a-certain-digraph-defined-on-the-set-of-primes-edited

## 12.2 Two-prime S-unit distribution

Languasco, Luca, Moree and Togbé study consecutive two-prime S-units \(p^a q^b\), their gaps and distribution. Their lattice-point count naturally contains the same triangular main scale

\[
\frac{(\log x)^2}{2\log p\log q}.
\]

This is relevant background for the weighted counting section, but their paper studies S-units themselves, not infinitude of prime values

\[
p^a q^b+1.
\]

Reference: A. Languasco, F. Luca, P. Moree, A. Togbé, *Sequences of integers generated by two fixed primes*, Abh. Math. Semin. Univ. Hambg. 95 (2025), 123–148, DOI 10.1007/s12188-025-00293-9.

## 12.3 Pierpont frontier remains outside the proved package

The fiber

\[
X_{\{2,3\}}
\]

is the Pierpont-prime family with positive exponents. The literature continues to treat infinitude of Pierpont primes as conjectural/unproved. Therefore the fifth paper must not infer infinitude of even this first higher fiber from the sieve-density calculations.

Useful references:

- OEIS A005109, https://oeis.org/A005109
- MathWorld, “Pierpont Prime”, https://mathworld.wolfram.com/PierpontPrime.html
- MathOverflow discussions on Pierpont primes.

## 12.4 Recent S-unit irreducibility work is adjacent, not a solution

Stoll and Siksek, *Hilbert's Irreducibility for \(\mathbb G_m\)*, arXiv:2609.04551 (2026), give an explicit description of reducible specializations over S-units for a broad Hilbert-irreducibility problem. This is close enough that it should be checked/cited in a modern literature section, but it does not supply a theorem asserting infinitely many prime values of

\[
1+\prod q_i^{e_i}.
\]

It therefore does not close the HATTER-SOL-05 frontier.

---

# 13. Priority audit

The following should be treated as **classical or standard ingredients**:

- free commutative monoid automorphisms from prime permutations;
- factorization of \(A^d+1\) for odd \(d\);
- Möbius density for coprimality-type conditions;
- multiplicative orders modulo primes;
- pairwise-coprime generalized Fermat-type sequences;
- lattice-point counting in a logarithmic triangle;
- König's infinity lemma;
- countability implying every infinite exact fiber has cardinality \(\aleph_0\).

The publication-worthy contribution is therefore not any one of those classical facts. It is the **assembled structural analysis of how they interact with the radical-predecessor multiplicity tower and the seed prime-renaming symmetry \((3\ 5)\)**.

No literature-wide priority claim is justified from the present search. The targeted audit did not locate an existing source packaging the exact theorem sequence in this form, but absence from the search is not proof of novelty.

---

# 14. Mandatory patch list before article assembly

1. **Narrow the descendant no-go theorem.** Replace the broad claim excluding all finite congruence strategies by a theorem only about levelwise finite fixed-divisor covers, unless a stronger cross-level theorem is separately proved.
2. **Correct the single-witness language.** At later heights use a finite obstruction family/tree, not an unqualified \(\mu(S)\ne\mu(\tau S)\) criterion.
3. **Clarify the pressure functional.** \(\mathfrak P\) is an external product/bookkeeping functional, not a joint density across levels.
4. **Clarify finite certificate.** It is a structural finite obstruction family, not an effective decision algorithm.
5. **Finish the weighted asymptotic proof.** Replace the proof sketch by a complete Möbius + periodic lattice-point argument, or demote/relegate it.
6. **Acknowledge Zaimi 2012 explicitly.** Exact-support stratification and the broad conditional symmetry/rigidity alternatives were already anticipated there.
7. **Use “transposition/element”, not “generator”, for \((3\ 5)\).** One transposition is not by itself a generator of the full infinite symmetric group.
8. **Strengthen finite-cover escape with one fixed generalized-Fermat spine.** This is optional but gives a cleaner theorem statement.

---

# 15. What the paper may safely claim after patching

The paper may safely claim a structural chain of implications and barriers:

\[
\boxed{
\text{finite fixed-divisor covers fail for every exact support},
}
\]

\[
\boxed{
|S|=1\text{ and }|S|\ge2
\text{ have different cyclotomic-admissibility dimensions},
}
\]

\[
\boxed{
\{2,3\}\text{ and }\{2,5\}
\text{ already have unequal local sieve profiles},
}
\]

\[
\boxed{
\text{that local asymmetry persists along 3-pure descendants},
}
\]

\[
\boxed{
\text{infinite fibers erase quantitative asymmetry at the cardinality level},
}
\]

\[
\boxed{
\text{HFI}\Longrightarrow(3\ 5)\text{ survives globally},
}
\]

and

\[
\boxed{
\text{FFC}\Longrightarrow
\bigl[\text{global death has a finite-height structural obstruction}\bigr].
}
\]

These statements sharpen the boundary left by HATTER-SOL-04 without pretending to decide the central automorphism problem.

---

# 16. What the paper must not claim

Do **not** claim:

- \(\operatorname{Aut}(\Pi)=\{\mathrm{id}\}\);
- \(\operatorname{Aut}(\Pi)\ne\{\mathrm{id}\}\) unconditionally;
- an unconditional global extension of \((3\ 5)\);
- an unconditional finite-height death of \((3\ 5)\);
- that \(X_{\{2,3\}}\) or every higher exact fiber is infinite;
- that different sieve densities imply different fiber cardinalities;
- that the pressure functional is a graph invariant;
- that finite-height obstruction certificates are effectively computable;
- that every finite congruence strategy is impossible;
- priority for the 2012 exact-support viewpoint;
- literature-wide novelty merely because no collision was found in this targeted search.

---

# 17. Publication decision

The branch has moved beyond a collection of experiments. It now has a single narrative:

> a prime transposition that is completely legal in the pure multiplicative world survives the first radical-predecessor layer; local arithmetic then distinguishes the two branches quantitatively, but the graph forgets that quantitative information whenever both exact fibers are infinite; in the opposite all-finite regime, König compactness forces every genuine global failure to appear through a finite-height obstruction family.

That narrative is mathematically coherent, directly continues HATTER-SOL-01 through HATTER-SOL-04, and has enough theorem-level structure for a fifth note once the scope patches are applied.

Final audit verdict:

\[
\boxed{
\textbf{PUBLICATION THRESHOLD REACHED AFTER MANDATORY SCOPE PATCHES.}
}
\]

The correct publication status is **structural result / boundary theorem package**, not **solution of the radical-predecessor automorphism problem**.
