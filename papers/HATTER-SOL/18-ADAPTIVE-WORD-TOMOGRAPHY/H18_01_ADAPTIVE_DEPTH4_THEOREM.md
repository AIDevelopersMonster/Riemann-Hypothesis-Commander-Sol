# HATTER-SOL-18 · H18-01
# Exact adaptive depth-four tomography in the H17 PSL(2,7) laboratory

**Status:** CLOSED by exact finite certificate.

## 1. Query model

Let \(X\) be the 114 canonical simultaneous-conjugacy orbits of generating ordered pairs \((A,B)\) in \(PSL(2,7)\).

For every freely reduced word \(w\in F_2=\langle A,B\rangle\), define

\[
q_w:X\to\{1A,2A,3A,4A,7A,7B\},
\qquad
q_w([(A,B)])=\operatorname{class}(w(A,B)).
\]

Freeze

\[
\mathcal W_4=\{w:\ 1\le |w|\le4,\ w\text{ freely reduced}\}.
\]

There are exactly

\[
4+12+36+108=160
\]

raw reduced words.  Two words are identified only when they induce exactly the same 114-entry class-response vector.  This leaves

\[
\boxed{50}
\]

distinct class-valued queries.

## 2. Exact adaptive theorem

Let \(D^\*(\mathcal W_4)\) be the smallest worst-case depth of an adaptive decision tree whose internal nodes are queries from the 50-query pool and whose leaves identify all 114 orbit states.

The exhaustive dynamic-programming certificate proves

\[
\boxed{D^\*(\mathcal W_4)=4}.
\]

Specifically:

- every depth-\(\le3\) tree is impossible;
- a depth-4 tree exists.

This is an exact finite result, not a heuristic tree search.

## 3. Adaptive vs fixed observation

The same 50-query pool has no separating fixed subset of sizes 1, 2, 3 or 4.

A five-query witness is the H16 family

\[
\boxed{A,\ B,\ AB,\ Ab,\ ABab}.
\]

Hence the minimum fixed probe count inside the same query pool is

\[
\boxed{5},
\]

whereas adaptive worst-case complexity is

\[
\boxed{4}.
\]

Therefore branching gives a strict one-query worst-case improvement in this finite laboratory:

\[
\boxed{5_{\rm fixed}\longrightarrow4_{\rm adaptive}}.
\]

## 4. Minimum mean depth among depth-4 trees

Among all admissible depth-4 trees, the certificate also minimizes total state-path length.

The optimum is

\[
\boxed{382}
\]

queries summed over all 114 states.  Thus

\[
\boxed{
\bar D_{\min}
=
\frac{382}{114}
=
\frac{191}{57}
\approx3.350877.
}
\]

One selected optimum has:

- root query \(AAB\);
- root nonempty branch sizes \(32,30,21,21,10\);
- 48 internal decision nodes;
- 74 states terminating at depth 3;
- 40 states terminating at depth 4;
- 13 distinct query-word labels across the whole tree.

A selected optimum uses the words

\[
A,\ B,\ AB,\ Ab,\ AAB,\ ABB,\ Abb,\ AAAB,\ AAAb,\ AABB,\ ABaB,\ ABab,\ Abbb.
\]

The certificate minimizes mean depth first, then internal node count, then cumulative internal-node word length under a deterministic tie-break.  The number 13 is therefore the distinct-word count of this selected optimum; a separate global minimum-distinct-label problem is not claimed solved.

## 5. Why simple word rotation is often invisible

If a word has the form \(uv\), then \(uv\) and \(vu\) are conjugate:

\[
u^{-1}(uv)u=vu.
\]

Therefore any cyclic rotation of a word has the same conjugacy-class observation.

So merely rotating letters in a word does not create a new class query.  H18 must use transformations that change the induced observer, not cosmetic cyclic shifts.

## 6. Hardware interpretation

H17 robust8 evaluates eight fixed probes because it solves a one-known-erasure coding problem.

H18-01 solves a different problem: exact orbit identification with no erasure.

The exact result says that a controller may ask one query, inspect its class result, and choose a different next word for different states.  Some states terminate after three queries; the hard states require four.

This creates a sequential architecture of the form

\[
(A,B)
\to
\text{word selector}
\to
\text{shared word engine}
\to
\text{class engine}
\to
\text{branch controller}.
\]

No hardware superiority is claimed until this adaptive controller is synthesized and compared against fixed-probe architectures under the same cost model.

## 7. Certificate

Run:

\`\`\`text
python certificates/h18_adaptive_depth4_certificate.py
\`\`\`

Optional machine-readable tree:

\`\`\`text
python certificates/h18_adaptive_depth4_certificate.py --emit-json generated/h18_adaptive_tree_W4.json
\`\`\`

The certificate reuses the canonical H17 golden model directly, so the 114 orbit IDs and conjugacy classes are not independently redefined.
