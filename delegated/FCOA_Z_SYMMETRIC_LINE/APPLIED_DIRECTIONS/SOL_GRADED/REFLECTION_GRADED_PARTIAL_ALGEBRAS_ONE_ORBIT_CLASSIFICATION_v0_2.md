# Reflection-Graded Partial Algebras — One-Orbit Completion Classification

**Version:** 0.2  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FIRST CLASSIFICATION THEOREM COMPLETE / `Xi` PROVED INCOMPLETE  
**Depends on:** `REFLECTION_GRADED_PARTIAL_ALGEBRAS_FOUNDATIONS_v0_1.md`

---

## 1. Executive result

The first classification question for reflection-partial magmas was:

\[
\boxed{
\text{Is reflection-orbit data together with the finite exchange profile }\Xi
\text{ complete for minimal one-orbit completions?}
}
\tag{1}
\]

The answer is **no**, and the failure occurs at the smallest possible nontrivial reflected carrier.

There are two non-isomorphic reflection-partial magmas on

\[
A=\{x,\bar x\},
\qquad
\nu(x)=\bar x,
\qquad
\nu(\bar x)=x,
\tag{2}
\]

with the same

- carrier reflection orbit;
- added input reflection orbit;
- output reflection orbit;
- exchange profile
  \[
  \Xi=(2,0,2,0),
  \tag{3}
  \]

but different interaction orientation:

\[
\mu_L(x,\bar x)=x,
\qquad
\mu_L(\bar x,x)=\bar x,
\tag{4}
\]

versus

\[
\mu_R(x,\bar x)=\bar x,
\qquad
\mu_R(\bar x,x)=x.
\tag{5}
\]

The two structures differ by a genuine **exchange chirality bit**:

\[
\chi=L
\quad\text{or}\quad
\chi=R,
\tag{6}
\]

meaning that the mirror output is anchored to the first or second participant.

This bit is invisible to `Xi` and also invisible to ordinary `C_2` orbit type data.

More generally, the exact classifier of one-orbit completions over a fixed base is not the ordinary reflection orbit of the chosen output. It is a **twisted stabilizer orbit** of that output.

That gives the first exact classification theorem of the successor RGPA/RPM theory.

---

## 2. Completion problem and notation

Fix a reflection-partial magma

\[
\mathcal A_0=(A,D_0,\mu_0,\nu)
\tag{7}
\]

and a reflection-invariant protected set

\[
P\subseteq A^2.
\tag{8}
\]

Let

\[
R_2(x,y)=(\nu x,\nu y)
\tag{9}
\]

act on input cells.

An unresolved input orbit is an `R_2`-orbit

\[
O\subseteq A^2
\tag{10}
\]

such that

1. `O` is disjoint from `D_0`;
2. `O` is disjoint from `P`.

A **one-orbit completion on `O`** is a conservative completion whose new domain is exactly

\[
D_0\sqcup O.
\tag{11}
\]

The output values on `O` must satisfy reflection equivariance.

---

## 3. Decorated reflection cells

Let

\[
p=(x,y)\in A^2
\tag{12}
\]

be an unresolved cell and let `z in A` be a proposed output.

Define the reflected triple orbit

\[
\widehat O(p,z)
=
\{(p,z),(R_2p,\nu z)\},
\tag{13}
\]

where `(p,z)` abbreviates the graph triple `(x,y,z)`.

If `R_2p=p`, functionality requires

\[
z=\nu z.
\tag{14}
\]

Thus in the fixed-input case the decorated orbit is the singleton graph cell `(p,z)` with reflection-fixed output.

### Definition 3.1 — admissible decorated cell

A pair `(p,z)` is **admissible** if

1. the input orbit of `p` is unresolved and unprotected;
2. if `R_2p=p`, then `z=nu z`.

Every admissible decorated cell determines a unique one-orbit reflection-equivariant extension of `G_0` by adjoining `widehat O(p,z)`.

---

## 4. Relative automorphism group

Let

\[
\Gamma
=
\operatorname{Aut}(\mathcal A_0;P)
\tag{15}
\]

be the automorphism group of the completion problem: bijections

\[
\gamma:A\to A
\tag{16}
\]

that

- commute with `nu`;
- preserve and reflect `D_0`;
- preserve all old operation values;
- preserve `P` setwise.

The group `Gamma` acts on input cells and on graph triples.

For an unresolved input orbit `O`, let

\[
\Gamma_O
=
\{\gamma\in\Gamma:\gamma O=O\}
\tag{17}
\]

be its setwise stabilizer.

---

## 5. Fixed input orbit classification

Suppose

\[
O=\{p\},
\qquad
R_2p=p.
\tag{18}
\]

Then admissible outputs lie in

\[
A^\nu=\{z:\nu z=z\}.
\tag{19}
\]

### Theorem 5.1 — fixed-orbit classifier

One-orbit completions on the fixed input cell `p`, modulo automorphisms of the completion problem preserving `O`, are classified exactly by the ordinary stabilizer orbits

\[
\boxed{
\Gamma_O\backslash A^\nu.
}
\tag{20}
\]

### Proof

Let `A_z` and `A_w` be the completions obtained by assigning outputs `z,w in A^nu` to `p`.

If `gamma in Gamma_O` extends to an isomorphism `A_z -> A_w`, then `gamma p=p` because `O` is a singleton. Product preservation forces

\[
\gamma z=w.
\]

Conversely, if `gamma z=w`, then `gamma` preserves the old graph and sends the unique new graph cell `(p,z)` to `(p,w)`. Hence it is an isomorphism of completions. QED.

---

## 6. Two-point input orbit and the twisted action

Now suppose

\[
O=\{p,R_2p\},
\qquad
p\ne R_2p.
\tag{21}
\]

Choose a representative `p`.

The action of `Gamma_O` on the two-point set `O` gives a homomorphism

\[
\varepsilon_p:\Gamma_O\to C_2,
\tag{22}
\]

defined by

\[
\varepsilon_p(\gamma)=
\begin{cases}
0,&\gamma p=p,\\
1,&\gamma p=R_2p.
\end{cases}
\tag{23}
\]

Because every automorphism commutes with `nu`, define

\[
\boxed{
\gamma\star_p z
=
\nu^{\varepsilon_p(\gamma)}\gamma z.
}
\tag{24}
\]

### Lemma 6.1 — twisted action lemma

Equation (24) defines a genuine group action of `Gamma_O` on `A`.

### Proof

The permutation action on the two-element set `O` makes `epsilon_p` a homomorphism to `C_2`:

\[
\varepsilon_p(\gamma\delta)
\equiv
\varepsilon_p(\gamma)+\varepsilon_p(\delta)
\pmod2.
\tag{25}
\]

Since every `gamma` commutes with `nu`,

\[
\begin{aligned}
(\gamma\delta)\star_p z
&=\nu^{\varepsilon(\gamma)+\varepsilon(\delta)}\gamma\delta z\\
&=\nu^{\varepsilon(\gamma)}\gamma
\bigl(\nu^{\varepsilon(\delta)}\delta z\bigr)\\
&=\gamma\star_p(\delta\star_p z).
\end{aligned}
\]

The identity acts trivially. QED.

---

## 7. One-Orbit Classification Theorem

For `z in A`, let

\[
\mathcal A(O;z)
\tag{26}
\]

denote the one-orbit completion with

\[
\mu(p)=z,
\qquad
\mu(R_2p)=\nu z.
\tag{27}
\]

### Theorem 7.1 — exact two-point classifier

Two one-orbit completions on the same unresolved two-point input orbit `O`,

\[
\mathcal A(O;z)
\quad\text{and}\quad
\mathcal A(O;w),
\]

are isomorphic by an automorphism of the fixed completion problem if and only if

\[
\boxed{
w\in\Gamma_O\star_p z.}
\tag{28}
\]

Equivalently, isomorphism classes are in canonical bijection with the twisted orbit space

\[
\boxed{
A/\!/_p\Gamma_O
:=
\Gamma_O\backslash_{\star_p}A.
}
\tag{29}
\]

### Proof

Suppose `gamma in Gamma_O` is an isomorphism from `A(O;z)` to `A(O;w)`.

If `gamma p=p`, then product preservation at `p` gives

\[
w=\gamma z,
\]

which is `gamma star_p z` because `epsilon=0`.

If `gamma p=R_2p`, then product preservation gives

\[
\gamma z
=
\mu_w(R_2p)
=
\nu w,
\]

hence

\[
w=\nu\gamma z
=\gamma\star_p z.
\]

Thus isomorphism implies twisted-orbit equivalence.

Conversely, if `w=gamma star_p z`, the same two cases show that `gamma` sends the two new graph triples of `A(O;z)` exactly to those of `A(O;w)`, while it already preserves the base completion problem. Hence `gamma` is an isomorphism. QED.

### Interpretation

The crucial point is

\[
\boxed{
\text{ordinary output reflection orbits are generally too coarse.}
}
\tag{30}
\]

If an automorphism reverses the input orbit, the reflected output must be corrected by one additional `nu`. This produces the twisted action rather than the ordinary action.

---

## 8. The minimal counterexample to `Xi`

Take the smallest nontrivial reflected set

\[
A=\{x,\bar x\},
\qquad
\nu x=\bar x.
\tag{31}
\]

Let the base operation be empty:

\[
D_0=\varnothing.
\tag{32}
\]

There is one mirror input orbit

\[
O=
\{(x,\bar x),(\bar x,x)\}.
\tag{33}
\]

There are two one-orbit completions.

### Left-anchored completion

\[
\boxed{
\mu_L(x,\bar x)=x,
\qquad
\mu_L(\bar x,x)=\bar x.
}
\tag{34}
\]

### Right-anchored completion

\[
\boxed{
\mu_R(x,\bar x)=\bar x,
\qquad
\mu_R(\bar x,x)=x.
}
\tag{35}
\]

Both are reflection-equivariant.

---

## 9. Same orbit data, same `Xi`

For both structures the carrier has exactly one reflection two-cycle:

\[
\{x,\bar x\}.
\tag{36}
\]

The defined input cells form exactly the same reflection orbit `O`.

The output values also lie in exactly the same reflection orbit

\[
\{x,\bar x\}.
\tag{37}
\]

The geometric exchange locus is

\[
E_{\mathrm{geom}}=O.
\tag{38}
\]

Since the outputs are not reflection-fixed,

\[
E_{\mathrm{fix}}=\varnothing,
\tag{39}
\]

\[
E_{\mathrm{split}}=O.
\tag{40}
\]

The algebraic exchange equation is forced exactly on the mirror orbit and nowhere else, so

\[
E_{\mathrm{excess}}=\varnothing.
\tag{41}
\]

Therefore both have

\[
\boxed{
\Xi=(2,0,2,0).
}
\tag{42}
\]

Thus not only the orbit **types**, but even the actual carrier/input/output reflection orbits coincide.

---

## 10. Non-Isomorphism Theorem

### Theorem 10.1

The RPMs

\[
\mathcal L=(A,O,\mu_L,\nu)
\qquad\text{and}\qquad
\mathcal R=(A,O,\mu_R,\nu)
\tag{43}
\]

are not isomorphic.

### Proof 1 — exhaustive automorphism proof

Every bijection of `A` commuting with `nu` is either

\[
\operatorname{id}
\quad\text{or}\quad
\nu.
\tag{44}
\]

The identity does not preserve the operation because

\[
\mu_L(x,\bar x)=x
\ne
\bar x=\mu_R(x,\bar x).
\tag{45}
\]

For `f=nu`,

\[
f\mu_L(x,\bar x)=\bar x,
\tag{46}
\]

whereas

\[
\mu_R(fx,f\bar x)
=
\mu_R(\bar x,x)
=x.
\tag{47}
\]

Thus `nu` also fails the homomorphism equation. No isomorphism exists. QED.

### Proof 2 — twisted classifier

For the empty base,

\[
\Gamma=\{\operatorname{id},\nu\}.
\tag{48}
\]

Both elements stabilize `O`.

Take

\[
p=(x,\bar x).
\tag{49}
\]

For the identity,

\[
\operatorname{id}\star_p z=z.
\tag{50}
\]

Reflection swaps the two input orientations, so

\[
\varepsilon_p(\nu)=1.
\tag{51}
\]

Hence

\[
\nu\star_p z
=
\nu(\nu z)
=z.
\tag{52}
\]

The twisted action is therefore **trivial** on `A`. Its two orbits are

\[
\{x\},
\qquad
\{\bar x\}.
\tag{53}
\]

Theorem 7.1 therefore gives exactly two non-isomorphic completions. QED.

---

## 11. Minimality

### Theorem 11.1 — absolute minimality

Two non-isomorphic reflection-partial magmas with identical reflection-orbit data and identical `Xi` already occur at

\[
\boxed{|A|=2,}
\tag{54}
\]

and no smaller carrier can exhibit the phenomenon.

### Proof

The construction above proves existence for two elements.

If `|A|=1`, the involution is necessarily the identity. Every defined input cell is the unique pair `(a,a)` and every defined output is necessarily `a`. Therefore for each possible domain there is only one operation, so no pair of non-isomorphic one-orbit completions with the same data exists. QED.

Thus the failure of `Xi` is not a high-complexity pathology. It is present at the first nontrivial reflected carrier.

---

## 12. Exchange chirality

The counterexample identifies the missing invariant.

Let

\[
O_x=
\{(x,\nu x),(\nu x,x)\}
\tag{55}
\]

be a non-fixed geometric exchange orbit, so `x != nu x`.

Suppose its output lies in the same participant reflection orbit:

\[
\mu(x,\nu x)\in\{x,\nu x\}.
\tag{56}
\]

### Definition 12.1 — exchange chirality

Define

\[
\chi(O_x)=
\begin{cases}
L,&\mu(x,\nu x)=x,\\
R,&\mu(x,\nu x)=\nu x.
\end{cases}
\tag{57}
\]

`L` means **first-participant anchored** and `R` means **second-participant anchored**.

### Lemma 12.2 — representative independence

Definition (57) is independent of whether `x` or `nu x` is chosen to represent the reflection orbit.

### Proof

If `mu(x,nu x)=x`, reflection equivariance gives

\[
\mu(\nu x,x)=\nu x,
\]

which is again the first argument of the reversed ordered pair.

If `mu(x,nu x)=nu x`, reflection equivariance gives

\[
\mu(\nu x,x)=x,
\]

which is again the second argument. QED.

### Theorem 12.3 — chirality is an isomorphism invariant

If an RPM isomorphism maps one non-fixed mirror input orbit to another and the output remains in the participant reflection orbit, it preserves `L/R` chirality.

### Proof

Let `f` be an isomorphism. If

\[
\mu(x,\nu x)=x,
\]

then

\[
\mu'(fx,\nu fx)
=f\mu(x,\nu x)
=fx,
\]

so first-participant anchoring is preserved. The right-anchored case is identical. QED.

Hence `chi` distinguishes the minimal pair `L,R` although `Xi` does not.

---

## 13. Anchoring spectrum

Chirality is the first case of a more general local invariant.

For a non-fixed mirror orbit `O_x`, let

\[
z=\mu(x,\nu x).
\tag{58}
\]

Classify it as

\[
\operatorname{Anchor}(O_x)=
\begin{cases}
\mathrm{FIXED},&z=\nu z,\\
\mathrm{LEFT},&z=x,\\
\mathrm{RIGHT},&z=\nu x,\\
\mathrm{EXTERNAL},&z\notin\{x,\nu x\},\ z\ne\nu z.
\end{cases}
\tag{59}
\]

Here `EXTERNAL` means that the output lies in another non-fixed reflection orbit.

The old exchange profile `Xi` sees only

\[
\mathrm{FIXED}
\quad\text{versus}\quad
\{\mathrm{LEFT},\mathrm{RIGHT},\mathrm{EXTERNAL}\},
\tag{60}
\]

because all latter cases are `split`.

Thus `Xi` is the quotient of a strictly finer anchoring spectrum.

For finite RPMs define

\[
\mathfrak A(\mathcal A)
=
(N_{\mathrm{fixed}},N_L,N_R,N_{\mathrm{external}}),
\tag{61}
\]

counted over non-fixed geometric exchange orbits rather than ordered cells.

This is an isomorphism invariant and refines the `fix/split` part of `Xi`.

It is still not expected to be complete in general: distinct external output orbits can share the same anchoring type.

---

## 14. Exact completion passport

The exact invariant suggested by Theorem 7.1 is not a finite count but an orbit label.

### Definition 14.1 — one-orbit completion passport

For a two-point unresolved input orbit `O` with representative `p`, define

\[
\boxed{
\Pi_O(z)
=
[z]_{\Gamma_O,\star_p}.
}
\tag{62}
\]

For a fixed input orbit, define

\[
\Pi_O(z)
=[z]_{\Gamma_O}.
\tag{63}
\]

### Theorem 14.2 — passport completeness

For a fixed completion problem and a fixed unresolved input orbit `O`,

\[
\boxed{
\Pi_O(z)=\Pi_O(w)
\iff
\mathcal A(O;z)\cong\mathcal A(O;w)
}
\tag{64}
\]

where isomorphisms are induced by automorphisms of the completion problem.

### Proof

This is Theorem 5.1 in the fixed-orbit case and Theorem 7.1 in the two-point case. QED.

Thus `Pi_O` is the first genuinely **complete** invariant in the new theory, at least for one-orbit completions over a fixed base.

---

## 15. Why ordinary output orbits fail

The minimal example gives the conceptual reason.

Ordinary reflection identifies

\[
x\leftrightarrow\bar x.
\tag{65}
\]

One might therefore expect the two outputs to define equivalent completions.

But the same reflection simultaneously reverses the input orientation:

\[
(x,\bar x)
\mapsto
(\bar x,x).
\tag{66}
\]

To compare completions using the same chosen representative `(x,bar x)`, one must reflect the output **again**. These two reflections cancel:

\[
\nu\circ\nu=\operatorname{id}.
\tag{67}
\]

Hence the twisted action of the reflection itself is trivial:

\[
\nu\star_p z=z.
\tag{68}
\]

This cancellation is exactly why left and right anchoring survive as two distinct isomorphism classes even though `x` and `bar x` lie in one ordinary reflection orbit.

This is the structural phenomenon that `Xi` misses.

---

## 16. Relation to FCOA-Z

In FCOA-Z, mirror cells have the form

\[
(P_n^+,P_n^-)
\quad\text{and}\quad
(P_n^-,P_n^+).
\tag{69}
\]

The earlier SOL-GRADED constructions used

- fixed root output `P_0`, giving the `FIXED` anchoring class;
- external reflected terminal fibers `F_n,bar F_n`, giving `EXTERNAL`.

The present classification shows that two additional structurally canonical mirror possibilities exist whenever output typing permits re-entry into the participant orbit:

\[
P_n^+\star P_n^-=P_n^+,
\qquad
P_n^-\star P_n^+=P_n^-
\tag{70}
\]

or

\[
P_n^+\star P_n^-=P_n^-,
\qquad
P_n^-\star P_n^+=P_n^+.
\tag{71}
\]

These are respectively `LEFT` and `RIGHT` exchange chirality.

Whether such rules are admissible for a particular FCOA operation remains a separate legacy/typing question. The RGPA classification itself does not require them to occur in `oplus`.

---

## 17. Publication significance

The v0.1 foundations established a category, a free-linearization functor, a completion dcpo, and exchange loci.

The present v0.2 adds the first nontrivial classification layer:

1. `Xi` is not complete;
2. incompleteness appears at the absolute minimum `|A|=2`;
3. the missing local bit is exchange chirality;
4. the exact one-orbit classifier is the twisted stabilizer orbit `Pi_O`;
5. ordinary reflection orbit classification fails for a precise structural reason.

This materially strengthens the case that reflection-partial magmas form an independent theory rather than just vocabulary around the FCOA example.

However, a standalone publication should still wait for the bibliography audit and at least one multi-orbit classification result.

---

## 18. Next frontier

The exact next question is no longer whether one-orbit completions can be classified. They can.

The next strike is:

\[
\boxed{
\text{For two unresolved reflection input-orbits, when do the two one-orbit passports combine independently,}
\text{ and when does the first extension change the automorphism stabilizer enough to couple the second?}
}
\tag{72}
\]

Equivalently: classify **two-orbit completions** and identify the first obstruction to factorization

\[
\operatorname{Class}(O_1\cup O_2)
\stackrel{?}{=}
\operatorname{Class}(O_1)\times\operatorname{Class}(O_2).
\tag{73}
\]

The expected mechanism is stabilizer breaking: the first decorated orbit may reduce `Gamma`, thereby splitting output classes available to the second orbit.

A minimal example of such coupling would be the first genuine interaction theorem of the completion theory.
