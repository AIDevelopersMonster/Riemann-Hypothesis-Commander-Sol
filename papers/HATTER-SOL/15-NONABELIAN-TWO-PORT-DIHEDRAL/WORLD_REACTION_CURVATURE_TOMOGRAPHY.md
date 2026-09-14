# HATTER-SOL-15 · World-Reaction Curvature Tomography

**Status:** exact theorem layer.  
**Role:** reconnect three H15 ideas that had been developed separately:

1. the square/torus carrier and its non-Abelian plaquette holonomy;
2. different port/spectral observers seeing different amounts of information;
3. the response of one arithmetic object across different worlds carrying information about that object.

The main point is that, in the dihedral class-field family, the projective world signature of a prime class is exactly the pattern of **flat versus curved non-Abelian squares** obtained after inserting its Frobenius rotation into the horizontal port.

---

## 1. Master generalized-dihedral world and quotient worlds

Let `E/Q` be imaginary quadratic, let `p` be an odd prime, and put

\[
A=\operatorname{Cl}(E),
\qquad
V=A/pA\cong\mathbf F_p^r.
\]

Let `M/E` be the elementary abelian unramified `p`-class field corresponding to `pA`. Then

\[
\operatorname{Gal}(M/E)\cong V,
\]

and complex conjugation acts by inversion, so

\[
G_*:=\operatorname{Gal}(M/\mathbf Q)
\cong V\rtimes C_2.
\]

Every hyperplane

\[
H<V
\]

defines a degree-`p` dihedral quotient world

\[
G_H=(V/H)\rtimes C_2\cong D_{2p}.
\]

Choose a calibration of that world: a nonzero linear functional

\[
\ell_H:V\to\mathbf F_p,
\qquad
\ker\ell_H=H,
\]

and a rotation generator `R_H` such that the class of `v in V` acts as

\[
R_H^{\ell_H(v)}.
\]

Let `S_H` be the reflection port, so

\[
S_H R_H S_H^{-1}=R_H^{-1}.
\]

Changing the calibration rescales `ell_H` and changes the chosen generator; the zero/nonzero statements below are calibration-free.

---

## 2. Insert the arithmetic object into the square

Let `q` be a rational prime unramified in `M` and split in `E`:

\[
q\mathcal O_E=\mathfrak q\bar{\mathfrak q}.
\]

Choose one prime `mathfrak q` above `q` and let

\[
a=[\mathfrak q]\bmod pA\in V.
\]

In world `H`, its cyclic Frobenius coordinate is

\[
\boxed{
\alpha_H(a):=\ell_H(a)\in\mathbf F_p.
}
\]

Thus the horizontal arithmetic transport is

\[
A_H(a):=R_H^{\alpha_H(a)}.
\]

Use the reflection port as vertical transport:

\[
B_H:=S_H.
\]

The square plaquette holonomy is

\[
K_H(a):=[A_H(a),S_H].
\]

## Theorem H15.73 — the square curvature is twice the world coordinate

For every world `H`,

\[
\boxed{
K_H(a)
=
[R_H^{\alpha_H(a)},S_H]
=
R_H^{2\alpha_H(a)}.
}
\]

### Proof

Using `S_H R_H^{-m}S_H^{-1}=R_H^m`,

\[
[R_H^m,S_H]
=R_H^m S_H R_H^{-m}S_H^{-1}
=R_H^mR_H^m
=R_H^{2m}.
\]

Set `m=alpha_H(a)`. QED.

Since `p` is odd, multiplication by `2` is invertible in `F_p`. Therefore the group-valued square holonomy contains exactly the same calibrated coordinate as the Frobenius rotation:

\[
\boxed{
\alpha_H(a)
=\tfrac12\log_{R_H}K_H(a).
}
\]

Here `log_{R_H}` means the discrete exponent in the fixed cyclic generator; no analytic logarithm is intended.

---

## Corollary H15.74 — arithmetic splitting equals square flatness

The following are equivalent:

\[
\boxed{
\begin{aligned}
&a\in H,\\
&\alpha_H(a)=0,\\
&A_H(a)=1,\\
&K_H(a)=1,\\
&\text{the object-labelled square is flat for the torus law},\\
&q\text{ has identity Frobenius in the degree-}p\text{ world }K_H,\\
&q\text{ splits completely in }K_H.
\end{aligned}}
\]

If `a notin H`, then `alpha_H(a)!=0`; hence `K_H(a)` is a nontrivial rotation and, because `p` is prime, a single `p`-cycle on the Schreier sectors.

Thus one arithmetic object turns the ensemble of worlds into a binary geometric response field:

\[
\boxed{
H\longmapsto
\begin{cases}
\text{flat square},&a\in H,\\
\text{curved square},&a\notin H.
\end{cases}}
\]

This is the square/torus version of the earlier projective Frobenius tomography theorem.

---

## Theorem H15.75 — curvature tomography across worlds

Define the curvature bit

\[
\kappa_a(H)
:=
\mathbf1_{\{K_H(a)\ne1\}}.
\]

For nonzero `a`,

\[
\boxed{
\kappa_a(H)=0\iff a\in H,
}
\]

so the complete curvature pattern over

\[
\mathcal W=\mathbb P(V^*)
\]

determines the projective class

\[
\boxed{[a]\in\mathbb P(V).}
\]

### Proof

By H15.74, the flat worlds are exactly the hyperplanes containing the one-dimensional subspace `<a>`. The intersection of all such hyperplanes is `<a>`. QED.

For `a!=0`, the number of flat worlds is

\[
\boxed{
N_{\rm flat}=\frac{p^{r-1}-1}{p-1},
}
\]

and the number of curved worlds is

\[
\boxed{
N_{\rm curved}=p^{r-1}.
}
\]

Therefore the old statement

\[
\text{“world changes can carry information about the object through its reaction”}
\]

is not merely heuristic in this laboratory. It is an exact theorem: the object is reconstructible projectively from the set of worlds in which its non-Abelian square becomes flat.

---

## Corollary H15.76 — the curvature patterns form the projective incidence code

For distinct projective classes `[a]!=[b]`,

\[
\boxed{
d_H(\kappa_a,\kappa_b)=2p^{r-2}.}
\]

Thus the geometric flat/curved world pattern is exactly the projective incidence code already found arithmetically.

In particular, the curvature signature uniquely corrects up to

\[
\boxed{p^{r-2}-1}
\]

adversarial world-bit errors by nearest-neighbour decoding.

The new point is interpretive but exact:

\[
\boxed{
\text{projective arithmetic codeword}
=
\text{flat/curved surface-response codeword}.
}
\]

The redundancy may therefore be read either arithmetically (splitting) or geometrically (commutator curvature).

---

## 3. Different observers really do see different information

The group-valued holonomy `K_H(a)` contains the full calibrated coordinate `alpha_H(a)`. Coarser observers forget different amounts of it.

Let

\[
\omega=e^{2\pi i/p}
\]

and use the complex Fourier basis `e_k`, `k in F_p`, with

\[
R_H e_k=\omega^k e_k.
\]

Then H15.73 gives

\[
\boxed{
K_H(a)e_k
=
\omega^{2k\alpha_H(a)}e_k.
}
\]

### Theorem H15.77 — observer-resolution ladder

Fix a nonzero Fourier channel `k`.

#### (i) Total centered trace: only flat versus curved

On

\[
V_{H,0}=\mathbf C[\mathbf F_p]\ominus\mathbf1,
\]

\[
\boxed{
\operatorname{Tr}(K_H(a)\mid V_{H,0})
=
\begin{cases}
p-1,&\alpha_H(a)=0,\\
-1,&\alpha_H(a)\ne0.
\end{cases}}
\]

Thus the full centered trace forgets which nonzero rotation occurred. It sees exactly one incidence bit.

#### (ii) One real mirror channel: the coordinate up to sign

On the real mirror pair `{k,-k}`, the trace is

\[
\boxed{
\tau_{H,k}(a)
=2\cos\frac{4\pi k\alpha_H(a)}p.
}
\]

Because `2k` is invertible modulo the prime `p`,

\[
\boxed{
\tau_{H,k}(a)=\tau_{H,k}(b)
\iff
\alpha_H(b)=\pm\alpha_H(a).
}
\]

Hence one real frequency pair recovers the local Frobenius coordinate up to the reflection ambiguity.

#### (iii) One oriented complex channel: the exact coordinate

The eigenphase

\[
\boxed{
\omega^{2k\alpha_H(a)}
}
\]

determines `alpha_H(a)` uniquely, since multiplication by `2k` is invertible modulo `p`.

Therefore, in one and the same world,

\[
\boxed{
\text{total trace}
\prec
\text{real mirror spectrum}
\prec
\text{oriented complex phase}
}
\]

in information resolution:

\[
\boxed{
\{0,\ne0\}
\longleftarrow
\{\pm\alpha\}
\longleftarrow
\alpha.
}
\]

This is an exact example of the HATTER principle that different observers/ports can see genuinely different information about the same underlying object.

---

## 4. Across worlds: projective, signless, and oriented reconstruction

The local hierarchy becomes a world-tomography hierarchy.

### Theorem H15.78 — multimodal reconstruction of the arithmetic class

Let `a in V` be nonzero.

1. **Coarse curvature / total-trace profile.**  
   The family
   \[
   \{\kappa_a(H):H\in\mathcal W\}
   \]
   determines exactly the projective class `[a]`.

2. **Calibrated real mirror profile.**  
   Suppose every world carries a chosen calibration `ell_H` and a fixed nonzero real mirror channel `k`. Then the complete family
   \[
   \{\tau_{H,k}(a):H\in\mathcal W\}
   \]
   determines the unordered pair
   \[
   \boxed{\{a,-a\}.}
   \]

3. **Calibrated oriented complex profile.**  
   Choose `r` calibrated worlds `H_1,...,H_r` whose functionals
   \[
   \ell_{H_1},...,\ell_{H_r}
   \]
   form a basis of `V^*`. The `r` complex phases
   \[
   \omega^{2k\ell_{H_j}(a)}
   \]
   determine `a` exactly.

### Proof

Part 1 is H15.75.

For Part 2, equality of all real profiles for `a` and `b` implies equality of the zero sets, hence `[b]=[a]` by projective tomography. Therefore `b=t a` for some `t in F_p^*`. Choose a world with `ell_H(a)!=0`. Equality of the real-channel traces implies

\[
t\ell_H(a)=\pm\ell_H(a),
\]

so `t=+/-1`. Thus `b=+/-a`.

For Part 3, each complex phase determines the coordinate `ell_{H_j}(a)` exactly. Since the `ell_{H_j}` form a basis of `V^*`, those coordinates determine `a`. QED.

So the same object admits three exact readout levels:

\[
\boxed{
[a]
\quad\subset\quad
\{a,-a\}
\quad\subset\quad
a,
}
\]

selected respectively by a topological/coarse observer, a real spectral observer, and an oriented complex spectral observer.

---

## 5. Reflection is exactly the sign ambiguity

The conjugate prime `\bar{\mathfrak q}` has class `-a` in `V`. Hence

\[
\alpha_H(-a)=-\alpha_H(a)
\]

and

\[
\boxed{
K_H(-a)=K_H(a)^{-1}.
}
\]

Therefore:

- curvature bits are unchanged;
- centered total traces are unchanged;
- real mirror traces are unchanged;
- oriented complex phases are complex-conjugated.

This is not an accidental loss of sign. It is exactly the dihedral reflection law

\[
S_HR_H^mS_H^{-1}=R_H^{-m}.
\]

Thus the observer hierarchy matches the arithmetic symmetry hierarchy:

\[
\boxed{
\text{rational/conjugacy-invariant observation}
\leftrightarrow
\{a,-a\},
}
\]

while choosing an oriented prime ideal above `q` breaks that reflection ambiguity and permits recovery of `a` itself.

---

## 6. Return to the square/torus picture

The earlier H15 square carrier used fixed ports `(R,S)` and found the plaquette defect

\[
[R,S]=R^2.
\]

The present layer replaces the horizontal generator by the **object-dependent world reaction**

\[
R\longmapsto R^{\alpha_H(a)}.
\]

The stretched fundamental square now has holonomy

\[
\boxed{
R^{2\alpha_H(a)}.
}
\]

Therefore the square is no longer merely a test of whether the world is non-Abelian. It becomes a measuring cell for the response of the object in that world.

Across all worlds:

\[
\boxed{
\text{one arithmetic object}
\longrightarrow
\text{field of square curvatures over world space}
\longrightarrow
\text{reconstruction of the object class}.
}
\]

This is the strongest current exact form of the original HATTER intuition that **the object is not described only by what it is in one world, but also by how it reacts when the world is changed**.

---

## 7. Topological storage cost of the reaction field

When `alpha_H(a)!=0`, the holonomy `K_H(a)=R_H^{2alpha_H(a)}` is a single `p`-cycle. If the torus defect is stored in one branch point, the compact covering genus is therefore

\[
\boxed{
g_H(a)=\frac{p+1}{2}.}
\]

When `alpha_H(a)=0`, the square is flat and the torus requires no branch defect.

Thus the same world signature can be read as a binary topological-cost field:

\[
\boxed{
H\longmapsto
\begin{cases}
1,&a\in H,\\
(p+1)/2,&a\notin H,
\end{cases}}
\]

where the value `1` denotes the unbranched torus genus and `(p+1)/2` the one-defect branched-cover genus.

Consequently the projective arithmetic class is recoverable even from the pattern of which worlds require extra topological storage.

---

## 8. Claim boundary

The following ingredients are classical:

- class-field quotient maps;
- projective point/hyperplane incidence;
- dihedral conjugation `r^m -> r^{-m}`;
- Fourier diagonalization of a cyclic shift;
- Wilson/plaquette holonomy and trace observers;
- projective incidence codes.

The H15-specific candidate is their exact composition in one arithmetic two-port laboratory:

\[
\boxed{
\text{prime ideal class}
\to
\text{world quotient coordinate}
\to
\text{object-dependent dihedral square holonomy}
\to
\text{flat/curved world field}
\to
\text{projective tomography},
}
\]

with the spectral-resolution ladder

\[
\boxed{
[a]
\to
\{a,-a\}
\to
a
}
\]

obtained by passing from total trace to real mirror channels to oriented complex channels.

No novelty priority is asserted before a dedicated hostile literature audit of this full composition. No Shannon-information, cryptographic, or physical-memory claim is made.

---

## 9. Next attack

The immediate serious question is whether the nonlinear spectral determinant / Mahler observer respects this resolution ladder.

At the linear/Fourier level we now know exactly what is lost at each projection:

\[
\alpha
\to
\{\pm\alpha\}
\to
\mathbf1_{\alpha\ne0}.
\]

The next test is whether the genus-five spectral curve and its regulator-selected genus-two motive depend only on the coarse class, on the signless class, or on the fully oriented phase. That will determine whether the heavy spectral/Mahler machinery is merely repackaging the same world-response information or genuinely preserving a finer non-Abelian mode.
