# G3 Research Checkpoint — Value Geometry after Domain Geometry

**Project:** FCOA Admissibility Geometry  
**Status:** post-publication research branch; not part of Zenodo DOI 10.5281/zenodo.22129787  
**Date opened:** 2026-08-27  
**Branch discipline:** no ordinary arithmetic is imported; all new generic rules are explicit partial-operation cells.

## 1. Why G3 is opened

The published G2 branch proves that a directed path can be compiled into the **domain** of a constant-valued partial operation. The next question recorded in `STATE.md` was:

> What is the weakest extension that carries information not already reducible to domain geometry, while still avoiding reconstruction of ordinary arithmetic?

G3 answers this by freezing the generic domain to a **symmetric adjacency path** and asking whether orientation can instead live in the **value fibers**.

The experiment is designed to separate three layers:

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

Define a new partial operation \(\otimes_S\) by extending M0 with both orientations of every generic adjacency edge:

\[
P_i\otimes_S P_{i+1}=\Omega,
\qquad
P_{i+1}\otimes_S P_i=\Omega,
\qquad 2\le i<N.
\]

Thus the off-diagonal generic domain is the symmetric path

\[
P_2-P_3-\cdots-P_N.
\]

The value on every new cell is the same.

### Proposition G3-S.1 — residual reflection

\[
\boxed{
\operatorname{Aut}(\otimes_S)\cong C_2.
}
\]

**Proof.** M0 fixes \(P_0,P_1\) and allows arbitrary permutation of \(G_N\). The new off-diagonal definedness relation reduces the generic permutations to automorphisms of the finite undirected path, namely identity and reversal. Because every new edge has the same value \(\Omega\), reversal preserves the operation. \(\square\)

So symmetric domain geometry destroys \(S_{N-1}\) but leaves exactly the endpoint reflection.

### Association Spectrum

For every \(N\ge3\), on \((X_N)^3\),

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

Relative to M0, every directed adjacency cell — now there are \(2(N-2)\) of them — contributes one new `EQ`, one new `LEFT`, and one new `RIGHT` state, while removing three `NONE` states.

### Commutation locus

Because both orientations of each adjacent generic pair are defined and have the same value, all adjacent generic ordered pairs commute. Hence

\[
|\operatorname{Comm}_{\otimes_S}|
=
3(N-1)+2(N-2)
=
\boxed{5N-7}.
\]

This is the first control branch for value geometry.

## 4. G3-C: anonymous two-value orientation coloring

Keep **exactly the same generic domain** as G3-S, but replace the common terminal output by two distinct anonymous terminal values:

\[
P_i\otimes_C P_{i+1}=\Omega_+,
\]

\[
P_{i+1}\otimes_C P_i=\Omega_-,
\qquad 2\le i<N.
\]

No output is named by a constant symbol and no unary type/color distinguishes \(\Omega_+\) from \(\Omega_-\). They are simply two terminal elements in the same output environment.

### Proposition G3-C.1 — output-swap obstruction

Despite the asymmetric values on each ordered edge,

\[
\boxed{
\operatorname{Aut}(\otimes_C)\cong C_2.
}
\]

**Proof.** Let

\[
r(P_i)=P_{N+2-i}
\qquad(2\le i\le N)
\]

be path reversal. Extend \(r\) by fixing \(P_0,P_1\), transporting the indexed M0 outputs in the forced way, and swapping

\[
\Omega_+\leftrightarrow\Omega_-.
\]

A forward edge is sent to a reverse edge and its output is simultaneously swapped, so every operation cell is preserved. No other generic permutation survives the undirected path domain. Therefore the automorphism group is again \(C_2\). \(\square\)

This is the key obstruction:

\[
\boxed{
\text{two unequal anonymous outputs do not by themselves fix an absolute orientation.}
}
\]

The residual reflection can act simultaneously on the carrier and on the output labels.

### Value change visible to commutation, invisible to the Association Spectrum

The Association Spectrum is **identical** to G3-S:

\[
\boxed{
(EQ,NEQ,LEFT,RIGHT,NONE)
=
(6N-8,0,N^2+4N-6,N^2+3N-6,N^3+N^2-10N+21).
}
\]

However, the generic adjacent pairs are no longer commuting because

\[
P_i\otimes_C P_{i+1}=\Omega_+
\ne
\Omega_-=P_{i+1}\otimes_C P_i.
\]

Therefore

\[
\boxed{
|\operatorname{Comm}_{\otimes_C}|=3(N-1),
}
\]

exactly the M0 value.

Thus G3-S and G3-C have:

- the same partial-operation domain;
- the same Association Spectrum;
- the same automorphism-group size \(C_2\);
- but different commutation loci.

So the commutation locus detects a value-fiber distinction that the Association Spectrum and automorphism-group size do not detect here.

## 5. G3-A: one anchored output fiber

The anonymous-output obstruction suggests the weakest internal repair: do not name or externally type the two outputs; instead anchor one output by **one additional operation cell on an already structurally fixed boundary pair**.

Extend G3-C by exactly

\[
\boxed{
P_1\otimes_A P_0=\Omega_+.
}
\]

This cell was undefined in M0. No other cell is added.

The choice \((P_1,P_0)\) is deliberate: both \(P_0\) and \(P_1\) are already fixed by the M0 reduct, so the anchor does not arbitrarily privilege one generic point.

### Proposition G3-A.1 — one-anchor rigidity

For every \(N\ge3\),

\[
\boxed{
\operatorname{Aut}(\otimes_A)=1.
}
\]

**Proof.** Any automorphism fixes \(P_0\) and \(P_1\), hence fixes the ordered pair \((P_1,P_0)\). Since

\[
P_1\otimes_A P_0=\Omega_+,
\]

it follows that \(\Omega_+\) is fixed. Consequently path reversal cannot be extended by swapping \(\Omega_+\) and \(\Omega_-\). The only remaining path automorphism is the identity, hence every generic point is fixed; the M0 output elements are then fixed by their defining cells. \(\square\)

### Proposition G3-A.2 — domain erasure restores reflection

Let \(D_A\) be the definedness relation of \(\otimes_A\), forgetting all output values. Then

\[
\boxed{
\operatorname{Aut}(X_N,D_A)\cong C_2
}
\]

on the generic sector relative to the fixed M0 boundary roles.

**Reason.** The extra domain cell \((P_1,P_0)\) is fixed under generic path reversal because \(P_0,P_1\) themselves are fixed. The generic off-diagonal domain remains an undirected path. Therefore definedness alone still admits reversal.

Combining G3-A.1 and G3-A.2 gives the first clean value-memory witness in this line:

\[
\boxed{
\operatorname{Aut}(\text{domain reduct})\cong C_2,
\qquad
\operatorname{Aut}(\text{full operation})=1.
}
\]

The missing orientation is therefore not reducible to domain geometry alone; it is carried by the **anchored output fiber**.

### Association Spectrum

The single anchor creates exactly \(N\) new `RIGHT` triples:

\[
(P_1,P_0,P_c),
\qquad 1\le c\le N.
\]

All were `NONE` before the anchor. Therefore

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
|\operatorname{Comm}_{\otimes_A}|=3(N-1),
}
\]

because the anchor pair and its reverse have unequal results/definedness, and adjacent generic pairs have the unequal values \(\Omega_+,\Omega_-\).

## 6. Anonymous Output-Swap Lemma

The G3-C phenomenon is not special to a path.

Let \(B\) be a base structure on an input carrier \(G\), let \(D\subseteq G^2\) be a domain relation, and suppose an involution \(r\in\operatorname{Aut}(B,D)\) reverses a two-coloring

\[
c:D\to\{+,-\}
\]

in the sense that

\[
c(r x,r y)=\tau(c(x,y)),
\]

where \(\tau\) swaps \(+\) and \(-\). Compile the colors using two anonymous terminal outputs \(\Omega_+,\Omega_-\).

Then

\[
(r,\Omega_+\leftrightarrow\Omega_-)
\]

is an automorphism of the compiled operation.

Hence an orientation coloring may fail to rigidify the carrier if the value fibers themselves remain exchangeable.

## 7. One-Anchor Lemma

Under the hypotheses above, assume there is an ordered pair \(q=(u,v)\) fixed by every candidate carrier automorphism, and add one operation cell

\[
u\star v=\Omega_+
\]

without adding the corresponding \(\Omega_-\)-anchor.

Then \(\Omega_+\) is internally fixed by the operation value at \(q\). Any automorphism that would require swapping \(\Omega_+\) and \(\Omega_-\) is eliminated.

For a residual group exactly \(C_2=\{1,r\}\), this single anchor is sufficient to make the full operation rigid.

Within the **anonymous two-terminal-value branch**, zero anchors are insufficient in G3-C and one anchor is sufficient in G3-A. This is the only minimality claim made here. It is not a claim that one anchor is necessary if output values are externally named, sorted, or otherwise distinguished.

## 8. Value-Erasure Test — working formulation

G2 motivated Carrier-Erasure / relation-erasure. G3 suggests a complementary diagnostic.

Given a partial operation \(\star\), form its **definedness reduct** by forgetting output values and retaining only

\[
D_\star(x,y)\iff \operatorname{Def}(x\star y).
\]

Compare

\[
\operatorname{Aut}(D_\star)
\quad\text{with}\quad
\operatorname{Aut}(\star).
\]

If the full operation is strictly more rigid than its definedness reduct, then some structural information is carried by value fibers rather than by domain geometry alone.

G3-A gives exactly

\[
\boxed{
C_2\longrightarrow1
}
\]

under value restoration.

`Value-Erasure Test` is working terminology, not a priority claim.

## 9. What G3 establishes if the audit survives

The M0-G1-G2-G3 line would then separate four mechanisms:

\[
\boxed{
\begin{array}{c}
\text{exchangeability}\\
\downarrow\\
\text{external relation geometry}\\
\downarrow\\
\text{compiled domain geometry}\\
\downarrow\\
\text{anchored value-fiber geometry}
\end{array}}
\]

The key new point is that **domain and value geometry can be varied independently enough to move different invariants in different ways**.

In particular:

1. G3-S \(\to\) G3-C changes the commutation locus but not the domain, Association Spectrum, or automorphism-group size.
2. G3-C \(\to\) G3-A changes automorphism rigidity while leaving generic domain geometry and the commutation locus unchanged.
3. G3-A is rigid even though its definedness reduct retains the path reflection.

## 10. Current status and next step

The formulas above have been independently enumerated by the local verifier for finite \(N\), and the group statements have direct proofs. They have **not yet undergone the two-model hostile audit protocol** used for M0/G1/G2.

Therefore the branch status is:

\[
\boxed{
\text{G3 = theorem candidate / computationally checked / hostile audit pending.}
}
\]

Do not merge these claims into the published G2 checkpoint until that audit is complete.
