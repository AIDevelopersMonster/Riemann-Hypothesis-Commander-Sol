# HATTER-SOL-04 · Fermat Swap Strike and Literature Collision

## 0. Why this note exists

After the multiplicity-tower theorem, the first natural killing test is the transposition

\[
\tau=(3\ 5)
\]

inside the height-one Fermat-prime fiber.

The question is whether \(\tau\) survives to the next level, and more generally whether it can survive through the whole inverse tower.

During this strike we found an important prior-literature collision: **the exact directed-prime automorphism problem was already asked explicitly on MathOverflow in 2012 by David Feldman**, with an answer by Gjergji Zaimi explaining that he expected many automorphisms but could not prove this unconditionally.

The purpose of this note is therefore twofold:

1. make the \((3\ 5)\)-survival criterion exact;
2. separate what is classical/previously asked from what our multiplicity-tower formalism adds.

---

# 1. Exact level-two criterion for \((3\ 5)\)

Let \(\mathcal F\) denote the full height-one fiber

\[
\mathcal F=X_{\{2\}},
\]

i.e. the set of Fermat primes.

At level two, every exact predecessor set has the form

\[
S=\{2\}\cup T,
\qquad
\varnothing\ne T\subseteq_{\mathrm{fin}}\mathcal F.
\]

For such \(T\), define

\[
c(T)=\mu(\{2\}\cup T).
\]

Then, by the multiplicity-tower theorem, the transposition \(\tau=(3\ 5)\) extends from height one to height two **if and only if**

\[
\boxed{
 c(T)=c(\tau T)
 \quad
 \text{for every finite nonempty }T\subseteq\mathcal F.
}
\]

Equivalently,

\[
\boxed{
\mu(S)=\mu(\tau S)
}
\]

for every exact predecessor support \(S\subseteq P_{\le1}\).

Thus a finite killing witness for \((3\ 5)\) is any finite support \(S\) for which

\[
\boxed{
\mu(S)\ne\mu(\tau S).
}
\]

The strongest possible form would be

\[
\mu(S)=0,
\qquad
\mu(\tau S)>0,
\]

or the reverse.

---

# 2. Why a naive finite adjacency witness cannot work

There is an important distinction between:

- prescribing adjacency/nonadjacency to finitely many already chosen primes;
- prescribing the **entire exact predecessor set**.

The first task is flexible.

## Lemma 2.1 — finite one-point extension

Let \(B\) be a finite set of primes, and let \(U,V\subseteq B\) be disjoint. Assume that if \(2\in B\), then \(2\in U\). Then there are infinitely many primes \(p>\max B\) such that

\[
q\mid p-1
\quad(q\in U),
\]

and

\[
q\nmid p-1
\quad(q\in V).
\]

### Proof

Impose

\[
p\equiv1\pmod q
\quad(q\in U),
\]

and

\[
p\equiv-1\pmod q
\quad(q\in V).
\]

Because the moduli are distinct primes, the Chinese remainder theorem combines these conditions into one residue class modulo

\[
M=\prod_{q\in U\cup V}q.
\]

The resulting residue is coprime to \(M\). Dirichlet's theorem therefore gives infinitely many primes in this class. Choosing one larger than \(\max B\) also guarantees that the new prime cannot divide \(b-1\) for any \(b\in B\). \(\square\)

This means that every finite local future pattern compatible with the orientation can be cloned.

In particular, a finite graph picture around \(3\) can be mirrored around \(5\) as long as one only asks for finitely many incidences.

Therefore:

\[
\boxed{
\text{a killing witness must use exact/global predecessor information,}
}
\]

not merely a finite collection of edge and nonedge conditions.

This is the precise reason the problem immediately encounters shifted-smooth prime arithmetic.

---

# 3. Exact predecessor fibers are the hard arithmetic object

For finite \(S\ni2\),

\[
X_S
=
\left\{
1+\prod_{q\in S}q^{e_q}
\text{ prime}:
 e_q\ge1
\right\}.
\]

Hence

\[
\mu(S)=|X_S|
\]

is the number of prime values in a shifted finite-prime semigroup.

Even the first fiber

\[
S=\{2\}
\]

is the Fermat-prime problem.

So the level-two survival criterion for \((3\ 5)\) is already governed by arithmetic at least as hard as understanding the cardinalities of families such as

\[
1+2^a3^b,
\qquad
1+2^a5^b,
\]

and their analogues with additional Fermat-prime bases.

No unconditional exact cardinality comparison is currently available from the methods used here.

---

# 4. Prior literature: the exact automorphism problem was already asked

In 2012 David Feldman asked on MathOverflow for the automorphism group of the digraph on the primes with

\[
p\to q
\iff
p\mid q-1.
\]

This is exactly the graph \(\Pi\) studied in HATTER-SOL-04, up to notation/orientation convention.

Gjergji Zaimi's answer stated that he expected the graph to have many automorphisms but could not prove this unconditionally. He singled out the same first layer: \(2\) is the unique source, and the primes with incoming edges only from \(2\) are the Fermat primes.

He proposed, as a heuristic/conjectural mechanism, that for every finite set of predecessor primes there should be infinitely many primes whose predecessor support is exactly that set. Under such a hypothesis, the graph would have many automorphisms.

Therefore HATTER-SOL-04 must **not** present the underlying automorphism question, the Fermat-fiber observation, or the heuristic "all exact fibers infinite implies many automorphisms" as new.

What remains potentially new in our branch is the explicit multiplicity-tower theorem, its split exact sequences, inverse-limit formulation, and the exact symmetry birth/death language built around them.

---

# 5. Conditional full-symmetry theorem

We now formalize the heuristic in the language of the multiplicity tower.

## Hypothesis FSI — Full Support Infinitude

For every finite set of primes \(S\) containing \(2\),

\[
\boxed{
\mu(S)=\aleph_0.
}
\]

That is, every formally possible finite exact predecessor support occurs for infinitely many primes.

This hypothesis is very strong and is **not known**; for \(S=\{2\}\) it already implies infinitely many Fermat primes.

## Theorem 5.1 — conditional surjectivity of the tower

Assume FSI. Then every restriction map

\[
\rho_n:G_{n+1}\to G_n
\]

is surjective.

### Proof

Under FSI, every exact predecessor fiber at level \(n+1\) has cardinality \(\aleph_0\). Hence for every \(g\in G_n\) and every predecessor set \(S\),

\[
\mu_n(S)=\aleph_0=\mu_n(gS).
\]

Therefore \(E_n=G_n\). The multiplicity-tower theorem gives

\[
\operatorname{im}\rho_n=E_n=G_n.
\]

\(\square\)

## Corollary 5.2 — every finite-height symmetry survives globally

Assume FSI. Then every \(g_n\in G_n\) extends to a global automorphism of \(\Pi\).

### Proof

By Theorem 5.1, recursively choose

\[
g_{n+1},g_{n+2},\ldots
\]

with

\[
\rho_k(g_{k+1})=g_k.
\]

The compatible sequence defines a global element of

\[
\varprojlim G_k
\cong
\operatorname{Aut}(\Pi).
\]

\(\square\)

In particular, under FSI,

\[
\boxed{
(3\ 5)
\text{ extends to a global automorphism.}
}
\]

## Corollary 5.3 — continuum many automorphisms

Assume FSI. Then

\[
\boxed{
|\operatorname{Aut}(\Pi)|=2^{\aleph_0}.
}
\]

### Proof

FSI makes the Fermat fiber \(\mathcal F\) countably infinite. Hence

\[
|\operatorname{Sym}(\mathcal F)|=2^{\aleph_0}.
\]

Every permutation of \(\mathcal F\) extends globally by Corollary 5.2, so the automorphism group has cardinality at least continuum. Since \(\Pi\) is countable, its full permutation group has cardinality at most continuum. \(\square\)

This turns Zaimi's heuristic into an exact tower statement.

---

# 6. The opposite direction: finite killing certificates

The tower also gives a completely rigorous way to prove rigidity **if** enough arithmetic asymmetry can be certified.

For \(g\in G_n\), define a killing certificate at level \(n+1\) to be a predecessor set \(S\) such that

\[
\mu_n(S)\ne\mu_n(gS).
\]

Then \(g\notin E_n\), hence \(g\) does not extend one level further.

Thus global rigidity follows if every nontrivial finite-height automorphism eventually receives a finite killing certificate.

This is weaker and more flexible than demanding all multiplicities \(\mu(S)\) be globally distinct.

The radical-predecessor problem is therefore a contest between two extreme scenarios:

\[
\boxed{
\text{uniform/infinite multiplicities}
\Longrightarrow
\text{large automorphism group}
}
\]

versus

\[
\boxed{
\text{enough multiplicity asymmetry}
\Longrightarrow
\text{eventual killing of every symmetry}.}
\]

---

# 7. Status of the \((3\ 5)\) strike

We did **not** find an unconditional exact support-cardinality witness killing \((3\ 5)\).

That failure is mathematically informative rather than merely computational:

- finite adjacency patterns cannot do the job because CRT + Dirichlet clone them;
- exact support cardinalities immediately enter hard shifted-smooth prime questions;
- the exact global automorphism problem was already explicitly recognized as hard in 2012.

Accordingly, the next productive direction is not a blind search for one more small prime example. It is to study **weaker arithmetic invariants of the multiplicity coloring** that can be proved to differ without knowing the full cardinalities \(\mu(S)\).

Candidate targets include:

1. parity or congruence restrictions on exponents in fibers;
2. existence of canonical finite subfamilies defined by additional graph-theoretic conditions;
3. relative multiplicity comparisons that can be injected between fibers;
4. eventual-support invariants obtained from higher descendants rather than exact cardinality at one level.

The next strike should ask whether any such invariant already separates \(3\) and \(5\) unconditionally.

---

# References / prior pointers

- David Feldman, **“Automorphisms of a certain digraph defined on the set of primes?”**, MathOverflow, 2012.
- Gjergji Zaimi, answer to the above question, 2012: conjectural large-automorphism scenario via infinitely many exact-support primes.
- G. A. Jones, **“Regular embeddings of complete bipartite graphs: classification and enumeration”**, Proc. London Math. Soc. 101 (2010), 427–453. The paper uses the directed relation \(q\mid p-1\), proves universality of finite acyclic labelled subgraphs, and identifies a Rado-graph shadow after forgetting orientation and the vertex 2.
