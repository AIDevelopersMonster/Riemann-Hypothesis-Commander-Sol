# HATTER-SOL-21 · SCALAR-COSET ORBIT / AFFINE-LINE INCIDENCE THEOREM

Status: **EXACT LOCAL INCIDENCE THEOREM LAYER**

## 1. Setup

Fix an odd prime \(p\) and a nonexceptional quadratic world

\[
A_p=\mathbf F_p[x]/(x^2-Bx-C),
\qquad
p\nmid C\Delta,
\]

with

\[
\Delta=B^2+4C\ne0\pmod p.
\]

Let

\[
H_p=\langle x\rangle\subset A_p^\times
\]

and

\[
h_p=|H_p|.
\]

The base-field scalars embed as

\[
\mathbf F_p^\times\subset A_p^\times.
\]

Define the scalar part of the orbit group

\[
\boxed{
D_p=H_p\cap\mathbf F_p^\times
}
\]

and

\[
\boxed{
d_p=|D_p|.
}
\]

Let

\[
\ell:A_p\to\mathbf F_p
\]

be any nonzero \(\mathbf F_p\)-linear functional and define the affine-level
incidence number

\[
N_\ell(c)
=
|\{y\in H_p:\ell(y)=c\}|.
\]

## Theorem H21-OI1 — scalar-coset incidence law

For every nonzero linear functional \(\ell\):

### Zero level

\[
\boxed{
N_\ell(0)\in\{0,d_p\}.
}
\]

### Nonzero levels

For every

\[
c\in\mathbf F_p^\times,
\]

\[
\boxed{
N_\ell(c)\le\frac{h_p}{d_p}.
}
\]

Since an affine level in the two-dimensional algebra contains exactly \(p\)
points,

\[
\boxed{
N_\ell(c)\le
\min\left(p,\frac{h_p}{d_p}\right).
}
\]

### Scalar-orbit symmetry of levels

For every

\[
t\in D_p,
\]

\[
\boxed{
N_\ell(tc)=N_\ell(c).
}
\]

Thus the nonzero incidence counts are constant on multiplicative
\(D_p\)-cosets in \(\mathbf F_p^\times\).

### Proof

The nonzero part of the kernel of \(\ell\) is a one-dimensional
\(\mathbf F_p\)-line,

\[
\ker(\ell)\setminus\{0\}=u\mathbf F_p^\times
\]

for some nonzero \(u\in A_p\).

If \(H_p\) meets this scalar line at one point \(y\), then every other point of
the intersection is exactly

\[
yD_p.
\]

Hence the zero-level intersection is either empty or one \(D_p\)-coset, giving
cardinality \(0\) or \(d_p\).

Now partition

\[
H_p
\]

into its scalar cosets

\[
H_p/D_p.
\]

Fix one coset \(yD_p\).  For \(t\in D_p\),

\[
\ell(ty)=t\ell(y)
\]

because \(t\in\mathbf F_p^\times\).

If \(c\ne0\), the equation

\[
t\ell(y)=c
\]

has at most one solution \(t\in D_p\).  Therefore each of the

\[
h_p/d_p
\]

scalar cosets contributes at most one point to the nonzero affine level.

Finally multiplication by \(t\in D_p\) is a bijection of \(H_p\) sending the
level \(\ell=c\) to \(\ell=tc\), proving level symmetry. QED.

## 2. Exact scalar-subgroup size

### Inert local algebra

If

\[
\left(\frac{\Delta}{p}\right)=-1,
\]

then

\[
A_p\cong\mathbf F_{p^2}.
\]

Both \(H_p\) and \(\mathbf F_p^\times\) are subgroups of the cyclic group
\(\mathbf F_{p^2}^\times\), hence

\[
\boxed{
d_p=\gcd(h_p,p-1).
}
\]

### Split local algebra

If

\[
\left(\frac{\Delta}{p}\right)=+1,
\]

write the two roots as

\[
r,s\in\mathbf F_p^\times.
\]

Under

\[
A_p\cong\mathbf F_p\times\mathbf F_p,
\qquad
x\mapsto(r,s),
\]

the orbit is

\[
H_p=\langle(r,s)\rangle.
\]

A power \(x^m\) is scalar exactly when

\[
r^m=s^m,
\]

or equivalently

\[
(r/s)^m=1.
\]

Therefore

\[
\boxed{
d_p
=
\frac{h_p}{\operatorname{ord}(r/s)}.
}
\]

## 3. Observer lines are trace levels

Put

\[
\delta=2x-B.
\]

Then

\[
\delta^2=\Delta,
\qquad
\tau(\delta)=-\delta.
\]

For

\[
y=a+bx,
\]

the coefficient functional \(b\) has the intrinsic form

\[
\boxed{
b(y)
=
\operatorname{Tr}_{A_p/\mathbf F_p}
\left(
\delta^{-1}y
\right).
}
\]

Indeed,

\[
\operatorname{Tr}(\delta^{-1}y)
=
\frac{y-\tau(y)}{\delta}
=
b.
\]

The other mask-defining coordinate functionals are also trace pairings with
fixed elements because the trace pairing on the etale quadratic algebra is
nondegenerate.

Hence every H21 zero-bit condition is exactly an affine trace level

\[
\boxed{
\operatorname{Tr}(\eta y)=c
}
\]

intersected with the cyclic multiplicative orbit \(H_p\).

## 4. Exact mask-count theorem

Fix the incoming character sign

\[
\sigma\in\{+1,-1\}.
\]

Let

\[
L_0^{(\chi_p,\sigma)}
\]

and

\[
L_1^{(\sigma)}
\]

be the two affine observer lines defining the constant-coordinate and
\(x\)-coordinate zero bits.

Write

\[
N_0
=
|H_p\cap L_0^{(\chi_p,\sigma)}|,
\]

\[
N_1
=
|H_p\cap L_1^{(\sigma)}|.
\]

The two lines meet in exactly the expected prime-law target

\[
t_\sigma
=
\begin{cases}
x,&\sigma=+1,\\
\tau(x),&\sigma=-1.
\end{cases}
\]

Define

\[
f_\sigma
=
\mathbf 1_{\{t_\sigma\in H_p\}}.
\]

Then the four local phase-set sizes are exactly

\[
\boxed{
|A_{\{0,1\}}|=f_\sigma,
}
\]

\[
\boxed{
|A_{\{0\}}|=N_0-f_\sigma,
}
\]

\[
\boxed{
|A_{\{1\}}|=N_1-f_\sigma,
}
\]

\[
\boxed{
|A_{\varnothing}|
=
h_p-N_0-N_1+f_\sigma.
}
\]

Thus the complete local mask histogram is determined by only:

- two orbit-line incidence counts;
- one target-membership bit.

No full phase-table enumeration is mathematically necessary.

## 5. Full-mask target membership

For

\[
\sigma=+1,
\]

\[
t_{+}=x\in H_p,
\]

so

\[
\boxed{
f_+=1.
}
\]

For

\[
\sigma=-1,
\]

use

\[
x\tau(x)=-C.
\]

Hence

\[
\tau(x)=(-C)x^{-1}.
\]

Therefore

\[
\boxed{
f_-=1
\iff
-C\in D_p.
}
\]

In the inert case,

\[
x^{p+1}=-C,
\]

so automatically

\[
\boxed{
f_-=1.
}
\]

In the split case the negative-sign full-mask phase may be absent.

## 6. Immediate observer bounds

Whenever a mask-defining line has nonzero affine level,

\[
\boxed{
N_i\le\min\left(p,\frac{h_p}{d_p}\right).
}
\]

Whenever it is a zero level,

\[
\boxed{
N_i\in\{0,d_p\}.
}
\]

Therefore partial-mask populations inherit exact deterministic bounds.

For example,

\[
|A_{\{1\}}|
\le
\min\left(p,\frac{h_p}{d_p}\right)-f_\sigma
\]

because the \(b=\sigma\) line always has nonzero level.

## 7. Compression consequence

The previous incidence code

\[
\mathcal I_{W,p}(m),
\qquad
m\in\mathbf Z/h_p\mathbf Z,
\]

contains \(h_p\) mask symbols.

For mask-count purposes it compresses exactly to

\[
\boxed{
(h_p,d_p,N_0,N_1,f_\sigma).
}
\]

For nonzero line levels, the full set of incidence counts across all target
values further compresses to at most

\[
\boxed{
\frac{p-1}{d_p}
}
\]

distinct scalar-level classes.

This is the first exact H21 compression theorem for the local observer
geometry.

## 8. What this theorem does not solve

H21-OI1 determines local incidence sizes and symmetries.

It does not determine the reciprocal placement of prime phases

\[
q\bmod h_p,
\qquad
p\bmod h_q
\]

inside those incidence sets.

Therefore it explains local mask geometry but not yet the full coupling term
\(K_W\).

The remaining problem is now sharply separated:

\[
\boxed{
\text{local incidence size}
\quad\text{vs}\quad
\text{reciprocal phase placement}.
}
\]

## 9. Claim boundary

The scalar-coset argument is elementary finite-group geometry, and trace
pairings in quadratic etale algebras are classical.

The H21 contribution under study is the use of this exact incidence law to
compress the Lucas zero-mask observer and feed the world compiler / hardware
scheduler.
