# HATTER-SOL-11 · First genuine post-quotient network collision

Status: closed theorem layer.

This note answers the open question at the end of T11.18. The ordinary HATTER Pareto-response map is **not** injective after quotienting the obvious conjugate pair-flip symmetry.

A counterexample already occurs with one binary-tail type at multiplicity four.

---

## 1. Arithmetic laboratory

Work in

\[
K=\mathbb Q(\sqrt{-1155}),
\qquad
\omega=\frac{1+\sqrt{-1155}}2,
\]

so

\[
\omega^2-\omega+289=0.
\]

Retain the binary-tail prime ideals above `17` from T11.15:

\[
A_+=(17,\omega-1),
\qquad
A_-=(17,\omega),
\]

with

\[
(17)=A_+A_-,
\]

\[
A_+^2=(\omega-1),
\qquad
A_-^2=(\omega).
\]

Take the rational input

\[
\boxed{n=17^2.}
\]

Its prime-ideal factorization contains two copies of `A_+` and two copies of `A_-`:

\[
(n)=A_+^2A_-^2.
\]

Every factor node has the same binary companion set

\[
\{A_+,A_-\}.
\]

Let

\[
j\in\{0,1,2,3,4\}
\]

be the total number of nodes choosing companion `A_+`.

By T11.15 the residue ideals

\[
\boxed{
R_j=A_+^jA_-^{4-j}
}
\]

are pairwise distinct and all principal.

Pair flip acts by

\[
\boxed{j\longmapsto4-j.}
\]

Hence there are three pair-flip quotient classes:

\[
\boxed{\{0,4\},\qquad\{1,3\},\qquad\{2\}.}
\]

---

## 2. Local typed states

For an `A_+` factor node:

\[
A_+\cdot A_+=(\omega-1),
\qquad
A_+\cdot A_-=(17),
\]

while for an `A_-` factor node:

\[
A_-\cdot A_+=(17),
\qquad
A_-\cdot A_-=(\omega).
\]

The odd-discriminant HATTER fold gives

\[
\boxed{
L:=\Pi(\omega-1)=\Pi(\omega)=(1,0),
}
\]

and

\[
\boxed{
H:=\Pi(17)=(17,0).
}
\]

Thus choosing the companion with the same sign as the factor ideal gives state `L`, while choosing the opposite companion gives state `H`.

There are no `Q` ports anywhere in this laboratory. Ordinary typed optimization therefore reduces to the scalar simple-support `P` network while the exact residue label is still retained arithmetically.

---

## 3. Witness-state content of each residue sector

There are two `A_+` factor nodes and two `A_-` factor nodes.

Let `x` be the number of the two `A_+` nodes choosing companion `A_+`, and let `y` be the number of the two `A_-` nodes choosing companion `A_+`. Then

\[
j=x+y.
\]

The number `h` of high states `H` is

\[
\boxed{h=(2-x)+y=2+j-2x.}
\]

Therefore the possible high-state counts by residue sector are

\[
\boxed{
\begin{array}{c|c}
 j & h\\
\hline
0 & 2\\
1 & 1,3\\
2 & 0,2,4\\
3 & 1,3\\
4 & 2
\end{array}}
\]

In particular the central residue sector `j=2` contains, among its six raw witness configurations,

- one pure low configuration `L^4`;
- four mixed configurations `L^2H^2`;
- one pure high configuration `H^4`.

The extreme sectors `j=0` and `j=4` each have exactly the mixed typed multiset

\[
\boxed{L^2H^2.}
\]

This is the structural opening through which a post-quotient collision can occur.

---

## 4. Exact ordinary response for the mixed multiset

Consider

\[
L^2H^2
=
\{(1,0),(1,0),(17,0),(17,0)\}.
\]

The total `P` capacity is

\[
P_{\rm tot}=36.
\]

Each low vertex has degree at most one. Therefore, in any connected graph, each low vertex must use its sole port to attach to the high-vertex component. The two high vertices may also use their mutual edge.

Thus

\[
|E_P|\le3.
\]

The bound is attained by the path/tree consisting of the high-high edge and one pendant low vertex attached to each high vertex. Hence

\[
\boxed{
B_P=36-2\cdot3=30,
\qquad B_Q=0.
}
\]

Therefore

\[
\boxed{
\mathcal F(L^2H^2)=\{(30,0)\}.
}
\]

So the extreme residue sectors satisfy

\[
\boxed{
\mathcal F(R_0)=\mathcal F(R_4)=\{(30,0)\}.
}
\]

The equality of `R_0` and `R_4` responses is the already-known pair-flip blindness.

---

## 5. Pure configurations inside the central sector

### Pure low configuration

For

\[
L^4=\{(1,0)^4\},
\]

the total available degree is only `4`, while a connected graph on four vertices needs degree sum at least

\[
2(4-1)=6.
\]

Hence

\[
\boxed{L^4\text{ has no connected HATTER realization}.}
\]

### Pure high configuration

For

\[
H^4=\{(17,0)^4\},
\]

the complete graph `K_4` is feasible and maximizes the number of edges:

\[
|E_P|=6.
\]

Thus

\[
B_P=4\cdot17-2\cdot6=56,
\]

so

\[
\boxed{
\mathcal F(H^4)=\{(56,0)\}.
}
\]

This is strictly dominated by `(30,0)`.

Therefore the union-then-Pareto semantics of HATTER-SOL-10 gives for the central residue sector

\[
\boxed{
\mathcal F(R_2)
=
\operatorname{ParetoMin}
\bigl(\varnothing\cup\{(30,0)\}\cup\{(56,0)\}\bigr)
=
\{(30,0)\}.
}
\]

---

## 6. The neighboring sectors

For completeness, `j=1` and `j=3` allow high-state counts `h=1` and `h=3`.

For `H L^3`, a star centered at the high vertex has three edges, so

\[
P_{\rm tot}=17+3=20,
\qquad
B_P=20-6=14.
\]

For `H^3L`, the three high vertices form a triangle and the low vertex contributes one pendant edge, so

\[
P_{\rm tot}=3\cdot17+1=52,
\qquad
B_P=52-8=44.
\]

Hence Pareto minimization selects the first configuration and

\[
\boxed{
\mathcal F(R_1)=\mathcal F(R_3)=\{(14,0)\}.
}
\]

The full five-sector response pattern is therefore

\[
\boxed{
30,\ 14,\ 30,\ 14,\ 30.
}
\]

under the ordering `j=0,1,2,3,4`.

---

## 7. The residues in the genuine collision are arithmetically different

The extreme sector `j=0` is

\[
R_0=A_-^4=(\omega^2).
\]

Since

\[
\omega^2=\omega-289,
\]

we may use generator

\[
\beta_0=-289+\omega.
\]

The central sector is

\[
R_2=A_+^2A_-^2=((\omega-1)\omega)=(-289)=(289).
\]

Thus

\[
\boxed{R_0\ne R_2.}
\]

They are also not pair-flip equivalent because

\[
0\notin\{2,4-2\}=\{2\}.
\]

More strongly, their folded residue states are different.

For `R_0`, the absolute triple of the generator `-289+omega` is

\[
289,\ 1,\ 288,
\]

so

\[
\boxed{\Pi(R_0)=(288,1).}
\]

For `R_2=(289)`,

\[
\boxed{\Pi(R_2)=(289,0).}
\]

Hence the collision is not caused by the static HATTER fold:

\[
\boxed{
\Pi(R_0)\ne\Pi(R_2)
\quad\text{but}\quad
\mathcal F(R_0)=\mathcal F(R_2).
}
\]

---

## 8. Theorem T11.19 — first genuine network-induced residue collision

In the imaginary quadratic world

\[
K=\mathbb Q(\sqrt{-1155}),
\]

for the rational input

\[
\boxed{n=17^2,}
\]

the principalization-residue sectors

\[
R_0=A_-^4=(\omega^2)
\]

and

\[
R_2=A_+^2A_-^2=(289)
\]

satisfy

\[
\boxed{
R_0\ne R_2,
\qquad
R_0\not\sim_{pf}R_2,
\qquad
\Pi(R_0)\ne\Pi(R_2),
}
\]

but their ordinary HATTER Pareto responses are exactly equal:

\[
\boxed{
\mathcal F(R_0)=\mathcal F(R_2)=\{(30,0)\}.
}
\]

Therefore the quotient response map

\[
\boxed{
\mathscr R/\!\sim_{pf}
\longrightarrow
\{\text{ordinary HATTER Pareto responses}\}
}
\]

is not injective in general.

This is the first explicit HATTER-SOL-11 example in which network optimization itself identifies arithmetically distinct, non-pair-flip-equivalent residue sectors that remain distinct even after the static residue fold.

QED.

---

## 9. Exact information-loss hierarchy

For this system the five exact residue sectors form three pair-flip classes:

\[
\{R_0,R_4\},
\qquad
\{R_1,R_3\},
\qquad
\{R_2\}.
\]

But only two ordinary response values survive:

\[
\boxed{
\{R_0,R_4,R_2\}\mapsto\{(30,0)\},
}
\]

\[
\boxed{
\{R_1,R_3\}\mapsto\{(14,0)\}.
}
\]

Thus

\[
\boxed{
5\ \text{exact sectors}
\longrightarrow
3\ \text{pair-flip classes}
\longrightarrow
2\ \text{ordinary responses}.
}
\]

The second arrow is the genuinely new network-induced collapse.

---

## 10. Structural mechanism

The collision is not accidental.

At multiplicity four, the central count sector `j=2` contains the same mixed typed multiset `L^2H^2` as the extreme sectors `j=0,4`, in addition to the two pure configurations `L^4` and `H^4`.

Therefore

\[
\boxed{
\mathcal F(R_2)
=
\operatorname{ParetoMin}
\bigl(
\mathcal F(L^2H^2)
\cup
\mathcal F(L^4)
\cup
\mathcal F(H^4)
\bigr).
}
\]

Whenever both pure contributions are infeasible or Pareto-dominated by the mixed response, the central and extreme residue sectors must collide.

The `17^2` laboratory realizes exactly this mechanism:

\[
L^4\text{ infeasible},
\qquad
\mathcal F(H^4)=\{(56,0)\}\succ\{(30,0)\}.
\]

So T11.19 exposes a reusable collision criterion rather than a numerical coincidence.

---

## 11. Next target

The next theorem layer should abstract the multiplicity-four mechanism.

For a binary-tail species with conjugation-invariant typed states `L` and `H`, prove a general identity for the residue sectors of four conjugation-balanced nodes:

\[
\boxed{
\mathcal F_0=\mathcal F_4=\mathcal F(L^2H^2),
}
\]

\[
\boxed{
\mathcal F_2=
\operatorname{ParetoMin}
\bigl(
\mathcal F(L^4)\cup
\mathcal F(L^2H^2)\cup
\mathcal F(H^4)
\bigr).
}
\]

Then characterize exactly when

\[
\mathcal F_2=\mathcal F_0
\]

and when the pure configurations strictly improve the central sector.

After that, extend the count-sector combinatorics to multiplicity `2e` and determine which residue levels can share the same typed-composition support before network optimization.