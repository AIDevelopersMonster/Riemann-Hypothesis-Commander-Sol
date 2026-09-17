# HATTER-SOL-15 · Schreier Commutator Character, Ramanujan Response, and Zeta

**Status:** exact theorem layer for the non-Abelian core of H15.  
**Purpose:** reconnect the previously separate commutator-holonomy and cyclotomic-contour lines. The Riemann-zeta factor appears here as the Dirichlet transform of the **centered character of powers of the non-Abelian port commutator**.

## 1. Dihedral Schreier laboratory

Let

\[
G=D_{2p}=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle,
\]

with `p` an odd prime, and let

\[
D=\langle s\rangle\cong C_2.
\]

On the Schreier sector set

\[
X=D\backslash G\cong\mathbf F_p
\]

the two H15 ports act as

\[
R:i\mapsto i+1,
\qquad
S:i\mapsto-i.
\]

We use the commutator convention

\[
[A,B]=ABA^{-1}B^{-1}.
\]

Then

\[
\boxed{K:=[R,S]=R^2.}
\]

Indeed `SRS^{-1}=R^{-1}`, hence

\[
RSR^{-1}S^{-1}
=R(SR^{-1}S)
=R^2.
\]

Thus the local route-order defect is itself a generator of the rotation subgroup because `p` is odd.

---

## 2. Centered Schreier representation

Let

\[
V=\mathbf C[X]
\cong \operatorname{Ind}_D^G\mathbf1
\]

be the permutation representation on the `p` Schreier sectors, and split off the invariant line:

\[
V=\mathbf1\oplus V_0.
\]

Therefore

\[
\dim V_0=p-1.
\]

The standard irreducible decomposition of the dihedral permutation representation is

\[
\boxed{
V_0\cong
\bigoplus_{k=1}^{(p-1)/2}\rho_k,
}
\]

where the `rho_k` are the two-dimensional irreducible representations with

\[
\chi_{\rho_k}(r^m)
=2\cos\frac{2\pi km}{p}.
\]

This is the non-Abelian version of the H15 mirror-frequency pairing `k <-> -k`.

---

## Theorem H15.64 — the commutator character is a Ramanujan sum

For every integer `m>=1`,

\[
\boxed{
\operatorname{Tr}(K^m\mid V_0)
=c_p(m),
}
\]

where

\[
c_p(m)
=\begin{cases}
p-1,&p\mid m,\\-1,&p\nmid m.
\end{cases}
\]

### Proof I: fixed points on the Schreier sectors

Since `K=R^2`,

\[
K^m=R^{2m}.
\]

On `X=F_p`, a nontrivial translation has no fixed point, while the identity fixes all `p` sectors. Because `p` is odd,

\[
p\mid 2m\iff p\mid m.
\]

Hence

\[
\operatorname{Tr}(K^m\mid V)
=\begin{cases}p,&p\mid m,\\0,&p\nmid m.
\end{cases}
\]

Subtracting the invariant line gives

\[
\operatorname{Tr}(K^m\mid V_0)
=\begin{cases}p-1,&p\mid m,\\-1,&p\nmid m,
\end{cases}
\]

which is `c_p(m)`. QED.

### Proof II: genuinely dihedral character decomposition

Using the irreducible decomposition above,

\[
\operatorname{Tr}(K^m\mid V_0)
=
2\sum_{k=1}^{(p-1)/2}
\cos\frac{4\pi km}{p}.
\]

Multiplication by `2` permutes the nonzero residue classes modulo the odd prime `p`, so

\[
2\sum_{k=1}^{(p-1)/2}
\cos\frac{4\pi km}{p}
=c_p(2m)=c_p(m).
\]

QED.

### Interpretation

The Ramanujan sequence is therefore not only the character of a cyclic rotation port. In H15 it is also

\[
\boxed{
\text{the centered character of repeated non-Abelian square holonomy }[R,S]^m.
}
\]

This identifies the arithmetic response directly with the route-order defect.

---

## Corollary H15.65 — repeated plaquette loops recover the same sequence

In the periodic square-lattice connection model, an `m`-fold positively oriented traversal of one elementary plaquette has fibre transport `K^m`. Therefore its centered fibre trace is

\[
\boxed{
\operatorname{Tr}(K^m\mid V_0)=c_p(m).
}
\]

The reverse traversal contributes the same value because `c_p(-m)=c_p(m)`.

Thus the closed-walk spectral observer and the arithmetic Ramanujan observer coincide on repeated elementary-square holonomy.

Combined with `FOURTH_SPECTRAL_MOMENT_HOLONOMY.md`, this gives

\[
\boxed{
\text{closed square walks}
\to
[R,S]^m
\to
c_p(m).
}
\]

---

## Theorem H15.66 — commutator Dirichlet response

For `Re(s)>1`, define

\[
\mathcal Z^{\rm comm}_p(s)
:=
\sum_{m=1}^{\infty}
\frac{\operatorname{Tr}(K^m\mid V_0)}{m^s}.
\]

Then

\[
\boxed{
\mathcal Z^{\rm comm}_p(s)
=(p^{1-s}-1)\zeta(s).
}
\]

### Proof

By Theorem H15.64 the coefficients are `c_p(m)`, and

\[
c_p(m)=p\mathbf1_{p\mid m}-1.
\]

Therefore

\[
\mathcal Z^{\rm comm}_p(s)
=p\sum_{p\mid m}m^{-s}-\sum_{m\ge1}m^{-s}
=(p^{1-s}-1)\zeta(s).
\]

QED.

The apparent pole at `s=1` cancels and

\[
\boxed{
\mathcal Z^{\rm comm}_p(1)=-\log p.
}
\]

So the H15 zeta factor can be obtained directly from the non-Abelian commutator response, without first introducing the cyclotomic contour.

---

## Theorem H15.67 — exact contour/commutator identity

Let

\[
I_{p,m}(\rho)
=\frac1{2\pi i}
\oint_{|z|=\rho}
 z^m\frac{\Phi_p'(z)}{\Phi_p(z)}\,dz
\]

be the H15 cyclotomic contour observer. For `rho>1`,

\[
I_{p,m}(\rho)=c_p(m).
\]

Hence

\[
\boxed{
I_{p,m}(\rho>1)
=
\operatorname{Tr}([R,S]^m\mid V_0).
}
\]

This closes the exact triangle

\[
\boxed{
\text{non-Abelian commutator holonomy}
=
\text{centered Schreier character}
=
\text{cyclotomic contour jump}
}
\]

at the level of the coefficient sequence, and therefore also at the Dirichlet-series level:

\[
\boxed{
\sum_{m\ge1}
\frac{I_{p,m}}{m^s}
=
\sum_{m\ge1}
\frac{\operatorname{Tr}([R,S]^m\mid V_0)}{m^s}
=(p^{1-s}-1)\zeta(s).
}
\]

---

## 3. Flat control: what is genuinely caused by noncommutativity?

Replace the dihedral pair by any commuting pair on the same `p`-dimensional fibre. Then

\[
K=[A,B]=I.
\]

On the centered space,

\[
\operatorname{Tr}(K^m\mid V_0)=p-1
\]

for every `m`, so

\[
\boxed{
\mathcal Z^{\rm flat}_p(s)
=(p-1)\zeta(s).
}
\]

For the dihedral pair,

\[
\mathcal Z^{\rm dih}_p(s)
=(p^{1-s}-1)\zeta(s).
\]

Therefore the exact response defect relative to the flat control is

\[
\boxed{
\mathcal Z^{\rm dih}_p(s)
-
\mathcal Z^{\rm flat}_p(s)
=
(p^{1-s}-p)\zeta(s).
}
\]

This does **not** solve or constrain RH by itself. It isolates, however, which Dirichlet response is created when the square law changes from `K=1` to the dihedral route-order defect `K=R^2`.

---

## 4. Why the prime hypothesis matters

For the odd dihedral group `D_{2n}` with composite `n`, the centered full Schreier representation gives

\[
\operatorname{Tr}(R^{2m}\mid V_0)
=n\mathbf1_{n\mid m}-1,
\]

which is generally **not** the classical Ramanujan sum `c_n(m)`.

The prime case is special because every nontrivial `p`-th root is primitive:

\[
V_0
=
\text{primitive cyclotomic sector}
\qquad (p\text{ prime}).
\]

For general odd `n`, let `V_n^{\rm prim}` be the sum of frequency lines indexed by units modulo `n`. Then

\[
\boxed{
\operatorname{Tr}(R^{2m}\mid V_n^{\rm prim})
=c_n(2m)=c_n(m),
}
\]

because `2` is invertible modulo odd `n`.

Consequently

\[
\sum_{m\ge1}
\frac{\operatorname{Tr}(R^{2m}\mid V_n^{\rm prim})}{m^s}
=
\zeta(s)
\sum_{d\mid n}\mu(n/d)d^{1-s}.
\]

This extension is retained as a secondary line; H15 keeps prime `p` as the minimal non-Abelian laboratory.

---

## 5. Prior-art boundary

The following ingredients are classical or already represented in the literature:

- Ramanujan sums as sums/characters of primitive roots of unity;
- cyclic and induced-representation appearances of Ramanujan sums;
- the Dirichlet-series identity for `c_p(m)`;
- character spectra of dihedral groups;
- traces of holonomy around closed walks;
- recent work also studies generalized Ramanujan sums for arbitrary finite groups.

A targeted literature search therefore does **not** support claiming that `Ramanujan sum = character trace` is new.

The H15-specific candidate is narrower:

\[
\boxed{
\text{non-normal dihedral Schreier world}
\to
\text{two ordered ports}
\to
\text{commutator }[R,S]
\to
\text{closed-square spectral holonomy}
\to
\text{centered Ramanujan character}
\to
\text{cyclotomic contour response}
\to
\zeta(s).
}
\]

No novelty priority is asserted until a hostile audit searches specifically for this full composition.

## 6. Consequence for the H15 research programme

The earlier contour-to-zeta layer was in danger of becoming a beautiful but detachable side result. The present theorem puts it back into the **non-Abelian spine** of H15:

\[
\boxed{
RS\ne SR
\Longrightarrow
K=[R,S]\ne1
\Longrightarrow
\chi_{V_0}(K^m)=c_p(m)
\Longrightarrow
\mathcal Z^{\rm comm}_p(s)
=(p^{1-s}-1)\zeta(s).
}
\]

The next serious question is no longer whether zeta can be made to appear. It already appears exactly. The question is whether the *geometric/spectral constraints imposed by the same non-Abelian port system* yield any new positivity, self-adjointness, transfer, or regulator statement for this response that is not automatic from the classical identity.
