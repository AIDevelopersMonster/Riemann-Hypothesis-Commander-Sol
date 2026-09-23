# HATTER-SOL-21 · PROJECTIVE ORBIT GEOMETRY AND EXACT PHASE PLACEMENT

Status: **EXACT LOCAL GEOMETRY THEOREM LAYER**

## 1. From the multiplicative clock to the projective clock

Fix a nonexceptional prime \(p\) and quadratic world

\[
A_p=\mathbf F_p[x]/(x^2-Bx-C),
\qquad
p\nmid C\Delta.
\]

Let

\[
H_p=\langle x\rangle,
\qquad
h_p=|H_p|,
\]

and

\[
D_p=H_p\cap\mathbf F_p^\times,
\qquad
d_p=|D_p|.
\]

Define

\[
\boxed{
e_p=\frac{h_p}{d_p}.
}
\]

This is the order of the image of \(x\) in the projective quotient

\[
A_p^\times/\mathbf F_p^\times.
\]

Thus \(e_p\) is the number of distinct scalar rays visited by the multiplicative orbit.

## Theorem H21-PG1 — unified projective-order formula

Let

\[
\tau(x)=B-x.
\]

Then

\[
\boxed{
e_p
=
\operatorname{ord}\left(\frac{x}{\tau(x)}\right).
}
\]

Moreover,

\[
\boxed{
e_p\mid p-\chi_p,
\qquad
\chi_p=\left(\frac{\Delta}{p}\right).
}
\]

Hence:

- split case \(\chi_p=+1\):
  \[
  e_p\mid p-1;
  \]

- inert case \(\chi_p=-1\):
  \[
  e_p\mid p+1.
  \]

### Proof

A power \(x^m\) is scalar iff it is fixed by conjugation:

\[
x^m=\tau(x^m)=\tau(x)^m.
\]

Therefore

\[
x^m\in\mathbf F_p^\times
\iff
\left(\frac{x}{\tau(x)}\right)^m=1.
\]

The least positive such \(m\) is exactly the order of the projective class of \(x\), which is \(e_p\).

If the algebra splits, the quotient by diagonal scalars is isomorphic to \(\mathbf F_p^\times\), of order \(p-1\).

If the algebra is inert, \(A_p^\times=\mathbf F_{p^2}^\times\) and the quotient by \(\mathbf F_p^\times\) has order \(p+1\).

QED.

## 2. Projective orbit

Projectivize the two-dimensional vector space:

\[
\mathbf P(A_p)\cong\mathbf P^1(\mathbf F_p).
\]

The scalar quotient of \(H_p\) is the cyclic projective orbit

\[
\boxed{
\bar H_p=H_p/D_p
}
\]

with

\[
|\bar H_p|=e_p.
\]

Thus the local multiplicative orbit is a lift of an \(e_p\)-cycle in the projective line, with exactly \(d_p\) scalar points above every visited projective phase.

## 3. Exact phase-fiber coordinates

Because \(H_p\) is cyclic, its unique subgroup of order \(d_p\) is

\[
D_p=\langle x^{e_p}\rangle.
\]

Put

\[
\lambda_p=x^{e_p}\in\mathbf F_p^\times.
\]

Then every exponent phase has a unique representation

\[
\boxed{
m=r+k e_p,
\qquad
0\le r<e_p,
\quad
0\le k<d_p.
}
\]

And

\[
\boxed{
x^m=\lambda_p^k x^r.
}
\]

Thus \(r\) is the projective phase and \(k\) is the scalar-fiber phase.

## Theorem H21-PG2 — exact affine-level phase placement

Let

\[
\ell:A_p\to\mathbf F_p
\]

be nonzero linear.

For each projective phase \(r\), define

\[
s_r=\ell(x^r).
\]

### Zero level

The solution set

\[
M_{\ell,0}
=
\{m\bmod h_p:\ell(x^m)=0\}
\]

is either empty or one complete scalar fiber:

\[
\boxed{
M_{\ell,0}
=
\varnothing
\quad\text{or}\quad
r_0+e_p\mathbf Z/d_p\mathbf Z.
}
\]

Hence it contains either \(0\) or \(d_p\) phases.

### Nonzero level

For \(c\ne0\), define

\[
R_{\ell,c}
=
\left\{
r\in\mathbf Z/e_p\mathbf Z:
s_r\ne0,\ c/s_r\in D_p
\right\}.
\]

For each \(r\in R_{\ell,c}\), there is a unique

\[
k_c(r)\in\mathbf Z/d_p\mathbf Z
\]

such that

\[
\lambda_p^{k_c(r)}=\frac{c}{s_r}.
\]

Therefore

\[
\boxed{
M_{\ell,c}
=
\left\{
r+e_p k_c(r):
r\in R_{\ell,c}
\right\}.
}
\]

So every nonzero affine-level phase set is a **partial transversal** of the scalar fibers: at most one phase above each projective phase.

## Corollary H21-PG3 — scalar translation law

For any

\[
t=\lambda_p^u\in D_p,
\]

\[
\boxed{
M_{\ell,tc}
=
M_{\ell,c}+u e_p
\pmod{h_p}.
}
\]

Thus levels in the same multiplicative \(D_p\)-coset have identical projective support and differ only by a uniform shift along the scalar-fiber direction.

In particular, if

\[
-1\in D_p,
\]

then

\[
\boxed{
M_{\ell,-c}
=
M_{\ell,c}+\frac{h_p}{2}
}
\]

because \(d_p\) is even and \(\lambda_p^{d_p/2}=-1\).

## 4. Geometric proof of the LAB-16 incidence bound

A zero level \(\ell=0\) is one projective point in

\[
\mathbf P^1(\mathbf F_p).
\]

The projective orbit either misses it or visits it once; lifting that point gives \(d_p\) scalar phases.

A nonzero affine level \(\ell=c\) intersects each scalar ray in exactly one vector.

Since \(\bar H_p\) visits only \(e_p\) scalar rays,

\[
\boxed{
N_\ell(c)\le e_p=\frac{h_p}{d_p}.
}
\]

Thus LAB-16 is exactly a projective-incidence statement.

## 5. Exact observer-code compression

For each observer line, the full phase set of length \(h_p\) can be encoded in projective coordinates:

- zero level: one projective phase \(r_0\), or absent;
- nonzero level: a partial graph
  \[
  r\mapsto k_c(r).
  \]

Therefore the local H21 incidence code is not an arbitrary subset of

\[
\mathbf Z/h_p\mathbf Z.
\]

It has the exact form

\[
\boxed{
\text{full fiber}
\quad\text{or}\quad
\text{partial transversal}.
}
\]

This is a strong structural restriction on all zero-mask phase sets.

## 6. Special observer fibers

Whenever a zero-level observer line contains the positive prime-law target \(x\), its projective phase is

\[
\boxed{r=1\pmod{e_p}}.
\]

Whenever a zero-level observer line contains the negative prime-law target \(\tau(x)\in H_p\), its projective phase is

\[
\boxed{r=-1\pmod{e_p}},
\]

because

\[
\tau(x)=(-C)x^{-1}
\]

differs from \(x^{-1}\) only by a scalar.

Thus the distinguished projective phases

\[
+1,\quad -1
\]

appear intrinsically in the observer geometry.

## 7. Canonical even-discriminant collapse

For canonical worlds with

\[
B=0,
\]

we have

\[
x^2=C\in\mathbf F_p^\times.
\]

Hence the projective class of \(x\) has order at most two:

\[
\boxed{
e_p\le2.
}
\]

So every \(B=0\) world has an extremely short projective orbit even when its full multiplicative clock \(h_p\) is large.

This is a new reason to distinguish the projective clock \(e_p\) from the old clock \(h_p\).

## 8. Remaining coupling problem

The local geometry is now compressed into:

\[
e_p,
\quad
d_p,
\quad
\text{projective supports }R_{\ell,c},
\quad
\text{fiber graph }k_c(r).
\]

Reciprocal prime selection uses

\[
q\bmod h_p
\]

and

\[
p\bmod h_q.
\]

Thus the remaining coupling problem is whether prime residues sample the two partial-transversal graphs independently or with arithmetic synchronization.

The correct next object is therefore not a raw phase set but a **reciprocal pair of projective-support / fiber-graph coordinates**.

## 9. Claim boundary

Projective quotients, cyclic subgroups, and affine-line intersections are classical finite algebra.

The H21-specific content is the exact decomposition of the Lucas zero-mask observer into projective phases and scalar fibers, and its use for compiled world-response geometry.
