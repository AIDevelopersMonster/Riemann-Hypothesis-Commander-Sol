# FCOA Rigidity Cost — Split Transporter Obstruction

**Published foundations:** Article A DOI `10.5281/zenodo.22157403`; Article B DOI `10.5281/zenodo.22159246`.

**Status:** post-publication structural note. This note records a failed proof route and the exact replacement object.

## 1. Split Exclusion is false

Persistent Exclusion is valid for anchored beta-killing singleton cells, but the stronger statement

\[
\text{“an anchored beta-killing cell cannot be fatal for both colors”}
\]

is false.

There exist anchored beta-killing cells `e` for which color `0` is defeated by one defect-one replacement symmetry and color `1` by a different defect-one replacement symmetry, with no carrier permutation bad for both colors.

Thus Type S split fatality is a real phenomenon.

## 2. Explicit six-carrier split witness

Take

\[
G=\{0,1,2,3,4,5\}
\]

and

\[
D=\{(1,5),(2,0),(3,4),(5,1)\}
\]

with colors

\[
c(1,5)=1,\quad c(2,0)=0,\quad c(3,4)=1,\quad c(5,1)=1.
\]

Let

\[
e=(0,2).
\]

The cell `e` is anchored and kills every old bad automorphism, so it is a one-cell beta witness.

Nevertheless both singleton colorings are nonexact.

For color `0`, bad replacement automorphisms include carrier permutations

\[
(0\ 1)(2\ 5)
\]

and related symmetries, sending `e` to `(1,5)` or `(5,1)`.

For color `1`, bad replacement automorphisms include

\[
(0\ 2),
\]

sending `e` to `(2,0)`.

No single bad automorphism survives both colors. Hence this is genuine Type S split fatality.

The old layer still has many other one-cell beta witnesses which are exact, so

\[
\boxed{\beta=\alpha=1}
\]

for the layer. The example disproves only universal Split Exclusion, not the Safe-Minimizer conjecture.

## 3. Same-target split also occurs

Even the attempted strengthening

\[
\text{“split fatality requires different replacement targets”}
\]

is false.

Take

\[
D=\{(0,1),(0,5),(2,1),(2,5),(3,1),(3,4),(3,5),(4,1),(4,5)\}
\]

with colors, in the displayed order,

\[
1,0,1,1,0,1,0,1,0.
\]

Let

\[
e=(0,4).
\]

For color `0`, one bad replacement symmetry is

\[
h_0=(0\ 3)(1\ 5),
\]

while for color `1`, one bad replacement symmetry is

\[
h_1=(0\ 3).
\]

Both send the new cell to the same old target:

\[
\boxed{h_0(e)=h_1(e)=(3,4).}
\]

Again the cell is anchored and beta-killing, and the two colors are defeated by different replacement symmetries.

## 4. Replacement-target lemma

Let

\[
S=D\cup\{e\}
\]

and let `h,k in Aut(G;S)` both move `D`.

Define their replacement targets

\[
p_h=h(e)\in D,
\qquad
p_k=k(e)\in D.
\]

### Lemma 4.1

\[
\boxed{
k^{-1}h(D)=D\iff p_h=p_k.}
\]

### Proof

Since

\[
h(D)=S\setminus\{h(e)\}=S\setminus\{p_h\},
\]

we have

\[
k^{-1}h(D)=S\setminus\{k^{-1}(p_h)\}.
\]

This equals

\[
D=S\setminus\{e\}
\]

if and only if

\[
k^{-1}(p_h)=e,
\]

that is, iff

\[
p_h=k(e)=p_k.
\]
`\square`

Dually, if

\[
q_h=h^{-1}(e),\qquad q_k=k^{-1}(e),
\]

then

\[
\boxed{hk^{-1}(D)=D\iff q_h=q_k.}
\]

## 5. Why the composition argument fails

Suppose `h_0` is a bad automorphism for color `0` and `h_1` is a bad automorphism for color `1`, and suppose they have the same replacement target. Then

\[
k=h_1^{-1}h_0
\]

preserves the old definedness domain `D` by Lemma 4.1.

However it need not lie in

\[
A_Q(D,c).
\]

The two factors preserve **different ternary reducts**, corresponding to the two different values assigned to `e`. Therefore their quotient need not preserve the original old ternary equality structure.

In the same-target witness above,

\[
k=h_1^{-1}h_0=(1\ 5),
\]

which preserves the old domain but fails the old ternary reduct.

Thus the hoped-for direct contradiction with beta-killing does not follow.

## 6. Split transporter

Call such a domain-preserving quotient

\[
\boxed{T(h_1,h_0)=h_1^{-1}h_0}
\]

a **split transporter** whenever `h_0,h_1` are bad replacement automorphisms for opposite singleton colors and have the same replacement target.

It is an automorphism of the old definedness domain, but generally a transporter between two different one-cell ternary structures rather than an automorphism of the old ternary reduct.

This is a genuinely new obstruction layer between replacement symmetry and old bad symmetry.

## 7. Same-color target fibers

Fix one singleton color `b` and one old target cell `p`.

If two bad replacement automorphisms `h,k` for the same color satisfy

\[
h(e)=k(e)=p,
\]

then `k^{-1}h` preserves `D` and is an automorphism of the **same** enlarged ternary reduct. Because `e` is anchored and beta-killing, every D-preserving enlarged-reduct automorphism is globally anonymous. Hence

\[
k^{-1}h\in H_e.
\]

Therefore all same-color bad replacement automorphisms with a fixed target form a single left `H_e`-coset.

Thus split fatality can be compressed by target cells rather than by individual carrier permutations.

## 8. Replacement-target sets

For an anchored beta-killing cell define

\[
P_b(e)=\{h(e):h\in B_b\}\subseteq D,
\qquad b\in\mathbf F_2.
\]

Persistent Exclusion gives no common **automorphism** between `B_0` and `B_1`, but the examples above show that both cases are possible:

\[
P_0(e)\cap P_1(e)=\varnothing
\]

and

\[
P_0(e)\cap P_1(e)\ne\varnothing.
\]

If a target lies in the intersection, opposite-color bad cosets over that target differ by a split transporter in `Aut(G;D)`.

## 9. Consequence for the beta-one programme

The remaining proof cannot proceed by excluding split fatality cell-by-cell.

The correct global target is now:

> prove that whenever one beta-killing cell is split-fatal, another beta-killing cell exists whose replacement-target system does not cover both colors.

Equivalently, the Safe-Minimizer theorem at beta one is a **global escape-cell theorem across the whole missing-cell complement**, not a local theorem about every beta witness.

This matches all exhaustive and stress evidence: unsafe and split-fatal beta minimizers exist, but safe minimizers coexist with them.

## 10. Next structural target

Define the beta-killing set

\[
W_{kill}(D,c)
\]

and for each `e in W_kill` its target-color incidence data

\[
\mathcal T(e)=\{(p,b):p\in P_b(e)\}.
\]

A beta-one counterexample would require **every** `e in W_kill` to have both colors covered by replacement-target data (or by the isolated phase trap).

The next problem is therefore a global covering problem on

\[
W_{kill}\times\mathbf F_2
\]

induced by defect-one replacements of the old domain.

A proof that this global replacement cover cannot be complete would establish

\[
\boxed{\beta=1\Longrightarrow\alpha=1.}
\]

## Claim firewall

1. Universal Split Exclusion is false.
2. Same-target Split Exclusion is also false.
3. The examples above are not counterexamples to `alpha=beta`; each admits safe one-cell alternatives.
4. The replacement-target lemma is theorem-level and purely domain-theoretic.
5. The split transporter need not preserve the old ternary reduct.
6. The global beta-one theorem remains open.
