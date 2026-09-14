# HATTER-SOL-15 · Generating-Pair Universality and Möbius Tomography Across Dihedral Worlds

**Status:** exact theorem layer.  
**Role in H15:** rotate the chosen two-port coordinates without changing the non-Abelian world, then enlarge from prime `p` to odd composite `n` and ask what survives.  
**Main outcome:** for every odd dihedral world, the centered commutator response is independent of the chosen generating pair; for composite worlds it canonically decomposes into primitive cyclotomic divisor layers, and Möbius inversion reconstructs each primitive layer from the family of smaller dihedral worlds.

---

## 1. Affine coordinates for an arbitrary port pair

Let

\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\]

with `n` odd. On the standard Schreier set

\[
X=\langle s\rangle\backslash D_{2n}\cong\mathbf Z/n\mathbf Z,
\]

every group element acts as an affine map

\[
x\longmapsto \varepsilon x+a,
\qquad
\varepsilon\in\{+1,-1\},
\quad a\in\mathbf Z/n\mathbf Z.
\]

Write such an element as `(a,epsilon)`. Composition is

\[
(a,\varepsilon)(b,\delta)
=
(a+\varepsilon b,\varepsilon\delta),
\]

and

\[
(a,\varepsilon)^{-1}=(-\varepsilon a,\varepsilon).
\]

## Theorem H15.68 — exact commutator coordinate

Let

\[
g=(a,\varepsilon),
\qquad
h=(b,\delta).
\]

With the convention

\[
[g,h]=ghg^{-1}h^{-1},
\]

the commutator is always a rotation,

\[
\boxed{
[g,h]=(q,+1),
\qquad
q=(1-\delta)a+(\varepsilon-1)b.
}
\]

Equivalently,

\[
\boxed{
[g,h]=r^q.
}
\]

### Proof

Using the affine multiplication law,

\[
gh=(a+\varepsilon b,\varepsilon\delta).
\]

Multiplying by `g^{-1}` gives

\[
ghg^{-1}
=
((1-\delta)a+\varepsilon b,\delta).
\]

Finally multiplication by `h^{-1}=(-\delta b,\delta)` yields

\[
[g,h]
=((1-\delta)a+(\varepsilon-1)b,+1).
\]

QED.

The four cases are therefore:

\[
\begin{array}{c|c}
(\varepsilon,\delta)&q\\
\hline
(+1,+1)&0\\
(+1,-1)&2a\\
(-1,+1)&-2b\\
(-1,-1)&2(a-b).
\end{array}
\]

Thus the entire route-order defect of an arbitrary two-port assignment is one residue class `q mod n`.

---

## Theorem H15.69 — generating-pair universality for odd dihedral worlds

Assume that the two ports generate the whole world:

\[
\langle g,h\rangle=D_{2n}.
\]

Then

\[
\boxed{\gcd(q,n)=1.}
\]

Hence the commutator

\[
K=[g,h]=r^q
\]

is a generator of the full rotation subgroup `C_n` and acts on the Schreier set as one `n`-cycle.

### Proof

A generating pair cannot consist of two rotations.

If one element is a rotation `r^a` and the other is a reflection, generation of the full dihedral group requires

\[
\gcd(a,n)=1.
\]

By H15.68 the commutator exponent is `q=+/-2a`. Since `n` is odd, `2` is a unit modulo `n`, so `q` is a unit.

If both are reflections, write them as `r^a s` and `r^b s`. Their product is the rotation `r^{a-b}`. They generate the full group exactly when

\[
\gcd(a-b,n)=1.
\]

Now H15.68 gives `q=2(a-b)`, again a unit because `n` is odd. QED.

### Port-coordinate invariance

The commutator element itself changes when the generating pair changes, but its cycle type does not:

\[
\boxed{
\text{every generating two-port coordinate system has one }n\text{-cycle commutator.}
}
\]

Thus all observers depending only on the powers/cycle type of the commutator descend from a chosen port pair to the underlying odd dihedral world.

---

## 2. Universal centered commutator response

Let

\[
V_n=\mathbf C[X],
\qquad
V_{n,0}=V_n\ominus\mathbf1.
\]

For any generating pair `(g,h)`, set

\[
A_n(m)
:=
\operatorname{Tr}([g,h]^m\mid V_{n,0}).
\]

By H15.69, `[g,h]=r^q` with `q` a unit. Therefore `[g,h]^m` is the identity exactly when `n|m`; otherwise it is a nontrivial translation and has no fixed Schreier sector.

Hence

\[
\boxed{
A_n(m)
=
\begin{cases}
n-1,&n\mid m,\\
-1,&n\nmid m.
\end{cases}
}
\]

or equivalently

\[
\boxed{
A_n(m)=n\mathbf1_{n\mid m}-1.
}
\]

This sequence is independent of the generating pair.

For `Re(s)>1`, its Dirichlet response is

\[
\boxed{
\mathcal Z_n^{\rm comm}(s)
:=\sum_{m\ge1}\frac{A_n(m)}{m^s}
=(n^{1-s}-1)\zeta(s).
}
\]

Thus the prime formula found earlier is not an accident of the canonical ports `(R,S)`: it is a generating-pair invariant of every odd dihedral world.

---

## Corollary H15.70 — prime worlds have exactly two commutator-response phases

Let `n=p` be an odd prime and let `g,h` be any two elements of `D_{2p}`.

Then exactly one of the following occurs.

### Abelian phase

If `gh=hg`, then

\[
[g,h]=1
\]

and

\[
\boxed{
\operatorname{Tr}([g,h]^m\mid V_{p,0})=p-1
}
\]

for every `m`, so

\[
\boxed{
\mathcal Z_p^{\rm flat}(s)=(p-1)\zeta(s).
}
\]

### Non-Abelian phase

If `gh!=hg`, then the pair automatically generates `D_{2p}`: a nontrivial rotation already generates `C_p`, while two distinct reflections multiply to a nontrivial rotation. Therefore H15.69 applies and

\[
\boxed{
\operatorname{Tr}([g,h]^m\mid V_{p,0})
=c_p(m),
}
\]

\[
\boxed{
\mathcal Z_p^{\rm nonab}(s)
=(p^{1-s}-1)\zeta(s).
}
\]

Hence this observer sees a genuine binary transition:

\[
\boxed{
[g,h]=1
\quad\text{versus}\quad
[g,h]\ne1
}
\]

with no intermediate commutator cycle type in the prime laboratory.

This strengthens the canonical `(R,S)` calculation: the response is a property of the non-Abelian prime dihedral world, not of one preferred coordinate choice inside it.

---

## 3. Why the prime laboratory hid a larger structure

For prime `p`, every nontrivial `p`-th root of unity is primitive, so

\[
\frac{z^p-1}{z-1}=\Phi_p(z).
\]

Therefore the full centered Schreier response and the primitive cyclotomic response coincide.

For composite odd `n`, they split:

\[
\frac{z^n-1}{z-1}
=
\prod_{\substack{d\mid n\\d>1}}\Phi_d(z).
\]

Let

\[
c_d(m)
=
\sum_{\substack{1\le a\le d\\(a,d)=1}}
\exp(2\pi i am/d)
\]

be the classical Ramanujan sum. Partitioning the nontrivial `n`-th roots by their exact order gives the exact identity

\[
\boxed{
A_n(m)
=
\sum_{\substack{d\mid n\\d>1}}c_d(m).
}
\]

Thus the non-Abelian centered commutator observer in a composite dihedral world is the **sum of all primitive cyclotomic divisor observers**.

This decomposition is classical at the level of roots of unity. Its role here is to separate what the full Schreier observer sees from what a primitive cyclotomic observer sees.

---

## Theorem H15.71 — Möbius tomography across divisor worlds

For every odd `n>1`, define `A_1(m)=0`. Then

\[
\boxed{
c_n(m)
=
\sum_{d\mid n}
\mu(n/d)A_d(m).
}
\]

### Proof

The previous identity says

\[
A_n(m)+1
=
\sum_{d\mid n}c_d(m).
\]

Möbius inversion gives

\[
c_n(m)
=
\sum_{d\mid n}
\mu(n/d)(A_d(m)+1).
\]

For `n>1`,

\[
\sum_{d\mid n}\mu(n/d)=0,
\]

so the constant terms disappear and the stated formula remains. QED.

Hence a primitive frequency layer of world `n` can be reconstructed by signed inclusion-exclusion of the full centered commutator responses of its divisor worlds:

\[
\boxed{
\text{primitive cyclotomic observer at }n
=
\text{Möbius transform of dihedral commutator observers at }d\mid n.
}
\]

At the Dirichlet-series level,

\[
\boxed{
\mathcal C_n(s)
:=
\sum_{m\ge1}\frac{c_n(m)}{m^s}
=
\sum_{d\mid n}
\mu(n/d)\mathcal Z_d^{\rm comm}(s).
}
\]

Using the universal world response,

\[
\boxed{
\mathcal C_n(s)
=
\zeta(s)
\sum_{d\mid n}\mu(n/d)d^{1-s}.
}
\]

This is the classical Dirichlet series of the Ramanujan sum, now obtained as an **inter-world Möbius reconstruction law**.

### Claim discipline

The divisor decomposition of roots of unity, Ramanujan sums, and Möbius inversion are classical. The potentially H15-specific content is the exact synthesis

\[
\boxed{
\text{odd dihedral generating-pair universality}
\to
\text{full Schreier commutator response}
\to
\text{divisor-world decomposition}
\to
\text{primitive cyclotomic reconstruction}.
}
\]

No novelty priority is asserted before a dedicated literature audit of this full composition.

---

## Corollary H15.72 — one world index controls both branch genus and analytic response

For every odd `n` and every generating port pair, the commutator is one `n`-cycle. If the torus commutator defect is stored in one branch point, the Riemann--Hurwitz contribution is `n-1`, hence

\[
\boxed{
g_{\rm branch}=1+\frac{n-1}{2}=\frac{n+1}{2}.}
\]

Therefore

\[
n=2g_{\rm branch}-1
\]

and the universal commutator Dirichlet response may be written directly in terms of this topological storage cost:

\[
\boxed{
\mathcal Z^{\rm comm}_{g}(s)
=
\left((2g-1)^{1-s}-1\right)\zeta(s).
}
\]

This does not create a new zeta identity. It records an exact H15 bridge:

\[
\boxed{
\text{generating-pair noncommutativity}
\to
\text{commutator cycle length }n
\to
\begin{cases}
\text{branch genus }(n+1)/2,\\
\text{Dirichlet response }(n^{1-s}-1)\zeta(s).
\end{cases}}
\]

The same discrete world parameter controls a topological observer and an analytic observer.

---

## Research consequence

The prime `D_{2p}` laboratory is now seen as the irreducible first layer of a larger odd-dihedral hierarchy. At prime level, full centered and primitive cyclotomic observers coincide. At composite level they separate, and the separation is organized exactly by the divisor lattice.

This suggests a new controlled expansion of H15:

\[
\boxed{
\text{prime world}
\subset
\text{odd composite dihedral worlds}
\subset
\text{divisor-lattice observer tomography}.
}
\]

The next question is whether the same Möbius separation survives after adding the *spectral-curve / Mahler / regulator* observer, where primitive divisor layers need not decouple automatically.
