# HATTER-SOL-11 · Mixed principalization-tail valence in discriminant -84

Status: closed theorem layer.

This note proves the `Delta=-84` reconnaissance exactly. Unlike `Delta=-35`, where every nonprincipal ideal has the same binary minimal-companion choice, the world `Q(sqrt(-21))` contains three distinct nonprincipal ideal classes with principalization costs `2`, `3`, and `5`; only the cost-`5` class branches. Thus tail valence depends on ideal class inside one fixed arithmetic world.

## 1. Arithmetic setup

Let

\[
K=\mathbb Q(\sqrt{-21}),
\qquad s=\sqrt{-21},
\qquad \mathcal O_K=\mathbb Z[s],
\qquad \Delta_K=-84.
\]

The norm is

\[
\boxed{N(a+bs)=a^2+21b^2.}
\]

The primes `2` and `3` are ramified. Put

\[
\mathfrak p_2=(2,s-1),
\qquad
\mathfrak p_3=(3,s).
\]

Then

\[
\boxed{(2)=\mathfrak p_2^2,\qquad(3)=\mathfrak p_3^2.}
\]

The prime `5` splits because `x^2+21` has roots `+-2` modulo `5`:

\[
\mathfrak p_5^+=(5,s-2),
\qquad
\mathfrak p_5^-=(5,s+2),
\]

\[
\boxed{(5)=\mathfrak p_5^+\mathfrak p_5^-.}
\]

There are no elements of norms `2`, `3`, `5`, or `6`, since the equation

\[
a^2+21b^2=m
\]

for each of these `m` forces `b=0`, after which `m` is not a square.

The element

\[
3+s
\]

has norm `30` and lies in `p_2`, `p_3`, and `p_5^+`. Equality of ideal norms gives

\[
\boxed{(3+s)=\mathfrak p_2\mathfrak p_3\mathfrak p_5^+.}
\]

Hence

\[
\boxed{[\mathfrak p_5^+]=[\mathfrak p_2][\mathfrak p_3].}
\]

Conjugation gives the same class for `p_5^-`.

---

## 2. Exact class group

### Theorem T11.10 — class group of discriminant -84

\[
\boxed{\mathrm{Cl}(\mathcal O_K)\cong C_2\times C_2.}
\]

More precisely, with

\[
c_2=[\mathfrak p_2],
\qquad
c_3=[\mathfrak p_3],
\qquad
c_5=[\mathfrak p_5^+]=[\mathfrak p_5^-],
\]

we have

\[
\boxed{c_5=c_2c_3,}
\]

and the four classes are

\[
1,c_2,c_3,c_5.
\]

### Proof

The ramification identities give `c_2^2=c_3^2=1`. The absence of elements of norms `2` and `3` shows `c_2,c_3` are nontrivial. If `c_2=c_3`, then `p_2p_3` would be principal of ideal norm `6`, contradicting the absence of an element of norm `6`; hence they are distinct and generate a subgroup of order four.

Minkowski's bound for an imaginary quadratic field gives an integral representative in every class of norm at most

\[
\frac{2}{\pi}\sqrt{84}<6.
\]

Therefore every class has a representative of norm `1,2,3,4`, or `5`. Norm `4` gives `p_2^2=(2)`, hence the principal class. Norm `5` gives exactly the two prime ideals `p_5^+,p_5^-`, whose class is `c_2c_3` by `(3+s)=p_2p_3p_5^+`. Thus there are no further classes. QED.

---

## 3. Cost spectrum and tail valence

For an ideal class `c`, define its minimal-companion set

\[
\mathscr A_{\min}(c^{-1})
=
\{J\subset\mathcal O_K:[J]=c^{-1},\ N(J)=\delta(c)\}.
\]

Define the **tail valence**

\[
\boxed{v(c)=|\mathscr A_{\min}(c^{-1})|.}
\]

By the HATTER-SOL-10 witness/least-norm-ideal bijection, `v(c)` is also the number of minimal witness orbits of every integral ideal in class `c`.

### Theorem T11.11 — mixed tail-valence spectrum

The four ideal classes have the exact spectrum

\[
\boxed{
\begin{array}{c|c|c|c}
\text{class}&\delta&\text{minimal companion ideals}&v\\ \hline
1&1&\{\mathcal O_K\}&1\\
c_2&2&\{\mathfrak p_2\}&1\\
c_3&3&\{\mathfrak p_3\}&1\\
c_5&5&\{\mathfrak p_5^+,\mathfrak p_5^-\}&2
\end{array}}
\]

### Proof

Minkowski plus T11.10 shows that the least possible norms in the four classes are respectively `1,2,3,5`. There is a unique ideal of norm `2` because `2` is ramified, and a unique ideal of norm `3` because `3` is ramified. Since `5` splits, the two ideals `p_5^+,p_5^-` are distinct, lie in the same order-two class `c_5`, and exhaust the norm-`5` ideals. QED.

Thus one fixed world contains both deterministic (`v=1`) and binary (`v=2`) principalization tails.

This is the first class-dependent tail-valence phenomenon in HATTER-SOL-11.

---

## 4. Four odd split primes realizing all classes

The class spectrum can be seen using odd rational split primes only.

### Principal class: p = 37

\[
N(4+s)=16+21=37.
\]

Hence one prime ideal above `37` is principal. Its class is `1`, so

\[
\boxed{\delta=1,\qquad v=1.}
\]

### Cost-2 class: p = 11

Since `-21 congruent 1 mod 11`, the prime splits. Let

\[
\mathfrak q_{11}=(11,s-1).
\]

There is no element of norm `11`, so `q_11` is nonprincipal. The element

\[
1-s
\]

has norm `22` and lies in both `q_11` and `p_2`, hence

\[
\boxed{(1-s)=\mathfrak q_{11}\mathfrak p_2.}
\]

Therefore

\[
\boxed{[\mathfrak q_{11}]=c_2,\qquad\delta(\mathfrak q_{11})=2,\qquad v=1.}
\]

Its unique minimal witness orbit is represented by `1-s`.

### Cost-3 class: p = 19

Since `-21 congruent 17 mod 19` and `6^2 congruent17 mod19`, the prime splits. Let

\[
\mathfrak q_{19}=(19,s-6).
\]

The element

\[
6-s
\]

has norm `57` and lies in `q_19` and `p_3`, so

\[
\boxed{(6-s)=\mathfrak q_{19}\mathfrak p_3.}
\]

Thus

\[
\boxed{[\mathfrak q_{19}]=c_3,\qquad\delta(\mathfrak q_{19})=3,\qquad v=1.}
\]

Its unique minimal witness orbit is represented by `6-s`.

### Cost-5 binary class: p = 17

Since `-21 congruent13 mod17` and `8^2 congruent13 mod17`, the prime splits. Put

\[
\mathfrak q_{17}=(17,s-8).
\]

There is no element of norm `17`, so `q_17` is nonprincipal.

Two elements of norm `85=5\cdot17` lie in `q_17`:

\[
\alpha_-=8-s,
\qquad
\alpha_+=1+2s.
\]

They satisfy

\[
\boxed{(8-s)=\mathfrak q_{17}\mathfrak p_5^-,}
\]

and

\[
\boxed{(1+2s)=\mathfrak q_{17}\mathfrak p_5^+.}
\]

Hence

\[
\boxed{[\mathfrak q_{17}]=c_5,\qquad\delta(\mathfrak q_{17})=5,\qquad v=2.}
\]

The two minimal witness orbits have the generic-even orbital signatures

\[
\boxed{\Omega(8-s)=(8,1),\qquad\Omega(1+2s)=(1,2),}
\]

where the entries are the axial and transverse counts respectively.

So the four odd split primes

\[
\boxed{37,11,19,17}
\]

realize the four ideal classes and the full cost/valence spectrum

\[
\boxed{(1,1),\ (2,1),\ (3,1),\ (5,2).}
\]

---

## 5. A second binary prime: p = 41

For `41`, `-21 congruent20 mod41` and `15^2 congruent20 mod41`, so

\[
\mathfrak q_{41}=(41,s-15)
\]

is a split prime ideal.

The norm equation

\[
a^2+21b^2=205
\]

has, inside `q_41`, two unit-orbits represented by

\[
11+2s,
\qquad
4-3s.
\]

They factor as

\[
(11+2s)=\mathfrak q_{41}\mathfrak p_5^+,
\qquad
(4-3s)=\mathfrak q_{41}\mathfrak p_5^-.
\]

Thus `q_41` is another member of class `c_5`, with

\[
\boxed{\delta=5,\qquad v=2.}
\]

and orbital signatures

\[
\boxed{(11,2),\qquad(4,3).}
\]

This confirms that the binary tail is class-level rather than specific to `p=17`.

---

## 6. Rational odd integers: exact residue structure

Let `n` be an odd rational integer. In the prime-ideal factorization of `(n)`, let

\[
M_2=2a,
\qquad
M_3=2b,
\qquad
M_5=2m
\]

be the numbers, counted with multiplicity, of nonprincipal prime-ideal nodes in classes `c_2,c_3,c_5` respectively.

These counts are even for rational input: split rational primes contribute conjugate pairs in the same order-two class, while ramified rational primes occur to even ideal multiplicity.

Each class-`c_2` node has the unique companion `p_2`; each class-`c_3` node has the unique companion `p_3`; each class-`c_5` node independently chooses `p_5^+` or `p_5^-`.

Therefore every minimal-witness residue sector has the form

\[
\boxed{
R_j
=
\mathfrak p_2^{2a}
\mathfrak p_3^{2b}
(\mathfrak p_5^+)^j
(\mathfrak p_5^-)^{2m-j},
\qquad 0\le j\le2m.
}
\]

Using `p_2^2=(2)` and `p_3^2=(3)`, this becomes

\[
\boxed{
R_j=(2)^a(3)^b(\mathfrak p_5^+)^j(\mathfrak p_5^-)^{2m-j}.
}
\]

### Theorem T11.12 — one branching class controls the rational tail

For every odd rational `n` in the `Delta=-84` world:

1. deterministic class-`c_2` and class-`c_3` tails only rescale every residue sector by the common rational ideal `(2)^a(3)^b`;
2. all witness branching comes from class `c_5`;
3. the residue sectors are indexed by `j=0,...,2m`;
4. their multiplicities are
   \[
   \boxed{\binom{2m}{j};}
   \]
5. all sectors have common ideal norm
   \[
   \boxed{2^{2a}3^{2b}5^{2m};}
   \]
6. conjugation sends `j` to `2m-j`.

Thus the full rational tail is a binary ladder sitting on top of deterministic class-dependent companion factors.

---

## 7. Prime 17: exact three-sector residue tail

For the full rational prime

\[
(17)=\mathfrak q_{17}\bar{\mathfrak q}_{17},
\]

we have `a=b=0,m=1`. Hence the three residue sectors are

\[
(\mathfrak p_5^-)^2,
\qquad
\mathfrak p_5^+\mathfrak p_5^-=(5),
\qquad
(\mathfrak p_5^+)^2,
\]

with multiplicities

\[
\boxed{1:2:1.}
\]

Now

\[
N(2+s)=25,
\qquad
N(2-s)=25,
\]

and direct divisibility gives

\[
\boxed{(2+s)=(\mathfrak p_5^-)^2,\qquad(2-s)=(\mathfrak p_5^+)^2.}
\]

Therefore the three principal residue generators may be chosen as

\[
\boxed{2+s,\qquad5,\qquad2-s.}
\]

All have field norm `25`, but their generic-even orbital signatures are

\[
\boxed{(2,1),\qquad(5,0),\qquad(2,1).}
\]

Thus the conjugate-balanced odd prime `17` develops a fixed-norm witness-residue spectrum with a purely axial center and two conjugate mixed axial/transverse tails.

---

## 8. Odd composite example: 11 * 17 * 19

Consider

\[
n=11\cdot17\cdot19.
\]

The split pair over `11` contributes two class-`c_2` nodes, the pair over `19` contributes two class-`c_3` nodes, and the pair over `17` contributes two class-`c_5` nodes. Hence

\[
a=b=m=1.
\]

The deterministic companions multiply to

\[
\mathfrak p_2^2\mathfrak p_3^2=(2)(3)=(6).
\]

Therefore the three residue sectors are generated by

\[
\boxed{6(2+s),\qquad30,\qquad6(2-s),}
\]

again with multiplicities

\[
\boxed{1:2:1.}
\]

and common field norm

\[
\boxed{900.}
\]

Their orbital signatures are

\[
\boxed{(12,6),\qquad(30,0),\qquad(12,6).}
\]

So deterministic tails from the cost-`2` and cost-`3` classes do not erase the cost-`5` branch structure; they scale it.

---

## 9. The odd-input / foreign-prime phenomenon

The principalization companion need not divide the original rational input.

Examples in this single world are:

\[
\boxed{
11\longmapsto\text{companion prime ideal above }2,
}
\]

\[
\boxed{
19\longmapsto\text{companion prime ideal above }3,
}
\]

\[
\boxed{
17\longmapsto\text{one of two companion prime ideals above }5.
}
\]

These arrows are not factorization identities in `Z`; they record the least ideal needed to principalize the selected split prime ideal in `O_K`.

Thus an odd rational input can expose an auxiliary principalization prime that was absent from the input integer. This is a precise arithmetic realization of the informal `tail` intuition.

The phenomenon is classical at the ideal-class level; the HATTER-SOL-11 question is how this foreign-prime tail interacts with orbital interface geometry and network response.

---

## 10. Consequence for HATTER-SOL-11

The `Delta=-35` and `Delta=-84` laboratories now separate three notions:

1. **principalization cost** `delta(c)`;
2. **tail valence** `v(c)`, the number of least-norm companion ideals;
3. **orbital signature** of the corresponding minimal witnesses/residue generators.

They are not interchangeable.

In `Delta=-35` there is one nontrivial class with `(delta,v)=(3,2)`.

In `Delta=-84` the nontrivial classes have

\[
\boxed{(2,1),\quad(3,1),\quad(5,2).}
\]

Therefore the next natural abstraction is a class-level **principalization-tail profile**

\[
\boxed{
\mathcal T_K(c)
=
\bigl(\delta_K(c),\mathscr A_{\min}(c^{-1})\bigr),
}
\]

together with the orbital signatures of the witness generators it induces.

A genuinely multi-branch tail (`v>2`) has not yet been found. The next patrol should search fields where one ideal class has three or more distinct least-norm representatives, rather than expecting this from `Delta=-84`.