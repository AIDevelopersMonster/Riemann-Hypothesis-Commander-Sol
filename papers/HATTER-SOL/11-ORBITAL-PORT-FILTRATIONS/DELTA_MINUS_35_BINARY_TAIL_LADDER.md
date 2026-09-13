# HATTER-SOL-11 · Binary odd-tail ladder in discriminant -35

Status: closed theorem layer.

This note turns the `Delta=-35` reconnaissance from `ODD_INTEGER_TAIL_PATROL.md` into an exact theorem. The key point is that the nontrivial ideal class has principalization cost `3`, and its two least-norm representatives are the two conjugate prime ideals above `3`. Consequently every nonprincipal ideal carries an exact binary companion-tail choice.

## 1. Arithmetic of the world

Let

\[
K=\mathbb Q(\sqrt{-35}),
\qquad
\omega=\frac{1+\sqrt{-35}}2,
\qquad
\mathcal O_K=\mathbb Z[\omega].
\]

Then

\[
\omega^2-\omega+9=0,
\qquad
N(a+b\omega)=a^2+ab+9b^2.
\]

Equivalently,

\[
\boxed{
4N(a+b\omega)=(2a+b)^2+35b^2.
}
\]

The prime `3` splits because `x^2-x+9` has roots `0,1` modulo `3`:

\[
\mathfrak p=(3,\omega),
\qquad
\bar{\mathfrak p}=(3,\omega-1),
\qquad
(3)=\mathfrak p\bar{\mathfrak p}.
\]

Since `N(omega)=9` and `omega in p` but `omega notin pbar`, ideal norms force

\[
\boxed{
\mathfrak p^2=(\omega).
}
\]

Conjugating gives

\[
\boxed{
\bar{\mathfrak p}^{\,2}=(\bar\omega),
\qquad \bar\omega=1-\omega.
}
\]

There is no element of norm `3`: from

\[
12=(2a+b)^2+35b^2
\]

we get `b=0`, which would require a square equal to `12`. Hence `p` and `pbar` are nonprincipal.

---

## 2. Class group and universal cost 3

### Theorem T11.8 — class group C2 and least nontrivial norm

\[
\boxed{
\mathrm{Cl}(\mathcal O_K)\cong C_2.
}
\]

Its unique nontrivial class is represented by both `p` and `pbar`, and the least norm of an integral ideal in that class is `3`.

### Proof

The Minkowski bound for an imaginary quadratic field says that every ideal class has an integral representative of norm at most

\[
\frac{2}{\pi}\sqrt{|\Delta_K|}
=
\frac{2}{\pi}\sqrt{35}
<4.
\]

Thus every class has a representative of norm `1`, `2`, or `3`.

Because `Delta=-35 congruent 5 mod 8`, the rational prime `2` is inert, so there is no prime ideal of norm `2`. The norm-`3` ideals are exactly `p,pbar`. They are nonprincipal, while `p^2=(omega)` is principal; hence `[p]` has order `2` and `[pbar]=[p]^{-1}=[p]`.

Therefore the only possible classes are the principal class and `[p]`. QED.

### Corollary T11.8a — universal principalization cost

For every nonprincipal integral ideal `I` in `O_K`,

\[
\boxed{
\delta(I)=3.
}
\]

Indeed T10.2 identifies `delta(I)` with the least norm in the inverse ideal class, which is the same unique nontrivial class.

### Corollary T11.8b — exactly two minimal witness orbits

For every nonprincipal integral ideal `I`, the minimal witness-orbit set is in canonical bijection with

\[
\boxed{
\{\mathfrak p,\bar{\mathfrak p}\}.
}
\]

Equivalently, every nonprincipal node has exactly two minimal companion ideals:

\[
\boxed{
J_+=\mathfrak p,
\qquad
J_-=\bar{\mathfrak p}.
}
\]

This follows from the HATTER-SOL-10 witness/least-norm-ideal bijection.

Thus the `3` observed in the reconnaissance is not a prime-specific accident. It is a class-level law of the entire `Delta=-35` world.

---

## 3. Binary tail law for rational integers

Let `n` be a positive rational integer and factor the principal ideal `(n)` into prime ideals with multiplicity. Call a prime-ideal factor node **active** if it is nonprincipal.

Let

\[
M(n)=\text{number of active prime-ideal factor nodes, counted with multiplicity}.
\]

Because every active node has the same nontrivial class of order `2`, while `(n)` is principal,

\[
\boxed{
M(n)=2m
}
\]

is even.

Principal factor nodes have principalization cost `1` and contribute no nontrivial companion. Every active node independently contributes either `p` or `pbar` by T11.8b.

For a witness configuration let `j` be the number of active nodes choosing `p`. Then `2m-j` choose `pbar`, and the total companion residue ideal is

\[
\boxed{
R_j=\mathfrak p^{\,j}\bar{\mathfrak p}^{\,2m-j},
\qquad
0\le j\le2m.
}
\]

### Theorem T11.9 — binary odd-tail ladder

For every rational integer `n` with `M(n)=2m` active nodes:

1. the residue ideals `R_0,...,R_{2m}` are pairwise distinct;
2. every `R_j` is principal;
3. every `R_j` has ideal norm
   \[
   \boxed{N(R_j)=3^{2m};}
   \]
4. the number of minimal witness configurations producing `R_j` is
   \[
   \boxed{\binom{2m}{j};}
   \]
5. conjugation reverses the ladder:
   \[
   \boxed{\overline{R_j}=R_{2m-j}.}
   \]

### Proof

Distinctness follows from unique prime-ideal factorization because the exponents of `p` and `pbar` differ with `j`.

Every companion has the nontrivial class `c=[p]=[pbar]`, so `R_j` has class `c^{2m}=1`; hence it is principal.

Its norm is the product of `2m` ideals of norm `3`, so `N(R_j)=3^{2m}`.

The multiplicity is simply the number of ways to choose which `j` of the `2m` active nodes use `p` rather than `pbar`.

Conjugation swaps `p` and `pbar`. QED.

### Explicit generators

Using

\[
\mathfrak p\bar{\mathfrak p}=(3),
\qquad
\mathfrak p^2=(\omega),
\qquad
\bar{\mathfrak p}^{\,2}=(\bar\omega),
\]

we obtain

\[
\boxed{
R_j=
\begin{cases}
(3^j\bar\omega^{\,m-j}),&0\le j\le m,\\[1mm]
(3^{2m-j}\omega^{\,j-m}),&m\le j\le2m.
\end{cases}}
\]

All these generators have the same absolute field norm `3^{2m}`.

The ladder therefore carries nontrivial arithmetic geometry on a fixed norm shell.

---

## 4. First exact prime laboratory: rational prime 13

The polynomial

\[
x^2-x+9
\]

has roots `6,8` modulo `13`, so

\[
(13)=\mathfrak q\bar{\mathfrak q},
\]

where

\[
\mathfrak q=(13,\omega-6),
\qquad
\bar{\mathfrak q}=(13,\omega-8).
\]

There is no element of norm `13` or `26`.

For norm `13`,

\[
52=(2a+b)^2+35b^2,
\]

so `|b|<=1`; `b=0` would require square `52`, while `|b|=1` would require square `17`.

For norm `26`,

\[
104=(2a+b)^2+35b^2,
\]

again `|b|<=1`; the remaining squares would be `104` or `69`.

Thus the split prime ideals above `13` are nonprincipal, and T11.8 gives principalization cost `3`.

Two clean minimal witnesses for `q` are

\[
\alpha_+=6-\omega,
\qquad
\alpha_-=1+2\omega,
\]

with

\[
N(\alpha_+)=N(\alpha_-)=39=3\cdot13.
\]

They satisfy

\[
\boxed{
(6-\omega)=\mathfrak q\mathfrak p,
}
\]

because `6-omega` lies in both `q` and `p`, and both sides have norm `39`; similarly

\[
\boxed{
(1+2\omega)=\mathfrak q\bar{\mathfrak p}.
}
\]

Hence these are the two minimal witness orbits of `q`.

Their HATTER-SOL-11 orbital geodesic signatures are

\[
\boxed{
\Omega(6-\omega)=(5;\{1,0\}),
\qquad
\Pi(6-\omega)=(5,1),
}
\]

and

\[
\boxed{
\Omega(1+2\omega)=(1;\{2,0\}),
\qquad
\Pi(1+2\omega)=(2,1).
}
\]

So even a single nonprincipal prime ideal already has two genuinely different axial/oblique allocations.

The conjugate ideal `qbar` has the conjugate witness choices and the same two companion options `p,pbar`.

Therefore the full rational prime `(13)=q qbar` has `M(13)=2`, so T11.9 gives exactly three residue sectors:

\[
\boxed{
R_0=\bar{\mathfrak p}^{\,2}=(\bar\omega),
\qquad
R_1=\mathfrak p\bar{\mathfrak p}=(3),
\qquad
R_2=\mathfrak p^2=(\omega).
}
\]

Their witness multiplicities are

\[
\boxed{1:2:1.}
\]

All three have residue norm `9`.

But their orbit geometry is not the same:

\[
\Omega(\omega)=\Omega(\bar\omega)=(0;\{1,0\}),
\qquad
\Pi(\omega)=\Pi(\bar\omega)=(1,0),
\]

whereas

\[
\Omega(3)=(3;\{0,0\}),
\qquad
\Pi(3)=(3,0).
\]

Thus a raw conjugation-balanced rational prime produces, after minimal-witness resolution, a fixed-norm residue spectrum with a balanced axial center and two conjugate oblique tails.

This is the first exact realization of the patrol's anticipated `tail` mechanism.

---

## 5. First composite ladder: 13 times 17

The prime `17` also splits because `x^2-x+9` has roots `7,11` modulo `17`:

\[
(17)=\mathfrak q_{17}\bar{\mathfrak q}_{17}.
\]

There is no element of norm `17`, since

\[
68=(2a+b)^2+35b^2
\]

has no integral solution. Hence both prime ideals above `17` are nonprincipal.

For example, one of them has minimal witnesses

\[
7-\omega,
\qquad
3+2\omega,
\]

with norm `51`, and orbital signatures

\[
\Omega(7-\omega)=(6;\{1,0\}),
\qquad
\Pi(7-\omega)=(6,1),
\]

\[
\Omega(3+2\omega)=(3;\{2,0\}),
\qquad
\Pi(3+2\omega)=(3,2).
\]

Therefore

\[
n=13\cdot17=221
\]

has four active prime-ideal nodes:

\[
M(221)=4.
\]

The residue ladder has five sectors

\[
R_j=\mathfrak p^j\bar{\mathfrak p}^{\,4-j},
\qquad j=0,1,2,3,4,
\]

with multiplicities

\[
\boxed{1:4:6:4:1.}
\]

All have norm

\[
\boxed{81.}
\]

A convenient generator table is

| `j` | generator `beta_j` | orbital signature | folded pair |
|---:|---|---|---|
| 0 | `bar omega^2 = -8-omega` | `(8;{1,0})` | `(8,1)` |
| 1 | `3 bar omega = 3-3omega` | `(0;{3,0})` | `(3,0)` |
| 2 | `9` | `(9;{0,0})` | `(9,0)` |
| 3 | `3 omega` | `(0;{3,0})` | `(3,0)` |
| 4 | `omega^2 = -9+omega` | `(8;{1,0})` | `(8,1)` |

Conjugation reflects the table about its central sector `j=2`.

So composite multiplication does not merely repeat the prime-level three-sector tail. It produces an exact binomial ladder of residue sectors whose orbit geometry changes non-monotonically across a fixed norm shell.

---

## 6. Hostile correction: no scalar tail coordinate is enough

The diagnostic scalar from `ODD_INTEGER_TAIL_PATROL.md`,

\[
\tau=A-O,
\]

where `A` and `O` are total axial and oblique geodesic usage, does not parameterize the residue ladder monotonically.

For the five sectors of `221` its values are

\[
\boxed{7,-3,9,-3,7.}
\]

Thus the tail cannot safely be reduced to one ordered scalar. The full residue ideal together with its orbital geodesic signature is the correct current object.

---

## 7. Interpretation and boundary of the claim

What is proved:

\[
\boxed{
\text{raw ideal balance}
\to
\text{binary minimal companion choices}
\to
\text{principal residue tail ladder}.
}
\]

The odd prime `3` appears because it is the least norm in the unique nontrivial ideal class of `Q(sqrt(-35))`. It is therefore an arithmetic principalization tail, not an imposed network parameter.

The construction is still conjugation-symmetric globally: sector `j` is paired with sector `2m-j`. The "tail" is not a violation of the raw ideal balance theorem T11.7. It is extra witness/residue structure that becomes visible only after resolving minimal principalizations.

Class groups, Minkowski bounds, split-prime ideals, and principalization by multiplying ideal classes are classical. The HATTER-SOL-11 contribution under investigation is the residue-ladder/network interpretation and its interaction with the orbit-fusion framework.

---

## 8. Next targets

1. Prove the analogous `Delta=-84` cost-`5` world and determine whether it yields a binary tail over the split prime `5` or a more complicated least-norm companion set.
2. Abstract T11.9 to any quadratic world whose relevant ideal class has order `2` and exactly two conjugate least-norm prime-ideal representatives.
3. Feed the `R_j` sectors into the HATTER network optimization and test whether distinct tail sectors can have identical ordinary `(P,Q)` network response while differing in orbital response.
4. Compare with Gaussian/Eisenstein controls carefully: those worlds fuse direction orbits but also have trivial class group, so disappearance of this principalization tail there has two simultaneous causes and must not be attributed to orbit fusion alone.