# HATTER-SOL-21 · H21-LAB-16 RESULT

Status: **CI REPRODUCED / LOCAL INCIDENCE THEOREM VALIDATED**

Run:

\`35721440607\`

Largest validation grid:

\[
p\le257,
\qquad
|D|\le63.
\]

## 1. Validation totals

World/prime/sign rows:

\[
\boxed{3974}.
\]

Scalar-subgroup formula checks:

\[
\boxed{1987}.
\]

Zero-level incidence checks:

\[
\boxed{2730}.
\]

Nonzero affine-line bound checks:

\[
\boxed{5218}.
\]

Full-mask one-point checks:

\[
\boxed{3974}.
\]

Exact mask-count reconstruction checks:

\[
\boxed{3974}.
\]

Failures:

\[
\boxed{0}.
\]

## 2. Corrected implementation note

The first LAB-16 run failed because the auxiliary integer factorizer omitted the
prime \(2\) when reducing candidate orders dividing \(p^2-1\).

Consequently some reported values called \(h_p\) were multiples of the true
multiplicative order, causing the orbit to be traversed repeatedly.

After restoring the factor \(2\), all four CI grids passed.

Thus the initial failure was an order-computation bug, not a counterexample to
the scalar-coset theorem.

## 3. Exact local geometry

For

\[
H_p=\langle x\rangle
\]

and

\[
D_p=H_p\cap\mathbf F_p^\times,
\qquad
d_p=|D_p|,
\]

every nonzero linear functional

\[
\ell:A_p\to\mathbf F_p
\]

obeys:

\[
\boxed{
|\{y\in H_p:\ell(y)=0\}|
\in\{0,d_p\}
}
\]

and, for \(c\ne0\),

\[
\boxed{
|\{y\in H_p:\ell(y)=c\}|
\le
\frac{h_p}{d_p}.
}
\]

The tested observer lines satisfy these bounds exactly.

## 4. Scalar subgroup formulas

For inert local worlds,

\[
\boxed{
d_p=\gcd(h_p,p-1).
}
\]

For split local worlds with roots \(r,s\),

\[
\boxed{
d_p=
\frac{h_p}{\operatorname{ord}(r/s)}.
}
\]

Both formulas passed exhaustive validation on the declared grid.

## 5. Exact mask histogram compression

For fixed incoming sign \(\sigma\), define the two observer-line incidence
counts

\[
N_0,
\qquad
N_1,
\]

and the target-membership bit

\[
f_\sigma.
\]

Then:

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

All tested histograms were reconstructed exactly.

Therefore the local phase-table histogram compresses from \(h_p\) mask symbols
to

\[
\boxed{
(h_p,d_p,N_0,N_1,f_\sigma).
}
\]

## 6. Full-mask geometry

The two observer lines intersect in exactly the expected prime-law target.

Hence the full mask has at most one phase:

\[
\boxed{
|A_{\{0,1\}}|\in\{0,1\}.
}
\]

For positive incoming sign,

\[
f_+=1.
\]

For negative incoming sign,

\[
f_-=1
\iff
-C\in D_p.
\]

In inert local worlds this always holds because

\[
x^{p+1}=-C\in H_p.
\]

## 7. Empirical incidence scale

On the largest validation grid,

\[
\max\frac{N_1}{h_p}
=
\boxed{0.5},
\]

and

\[
\max\frac{N_0}{h_p}
=
\boxed{0.5}.
\]

This is an observed finite maximum, not a universal theorem.

The proven universal control is through

\[
h_p/d_p.
\]

## 8. What has now been separated

H21 coupling is no longer a single opaque phenomenon.

The local observer geometry is now understood exactly at the level of
incidence counts:

\[
\boxed{
\text{cyclic orbit}
\cap
\text{affine trace levels}.
}
\]

What remains unexplained is not how many phases each mask has, but where the
prime-selected reciprocal phases land inside those sets:

\[
q\bmod h_p,
\qquad
p\bmod h_q.
\]

Thus the surviving coupling problem is now purely a reciprocal-placement
problem.

## 9. Next target

For each prime \(p\), replace the full phase table by the exact incidence sets

\[
A_{p,z}
\subset
\mathbf Z/h_p\mathbf Z.
\]

Study whether these sets are:

- unions of cosets of a smaller subgroup;
- translates of sparse algebraic subsets;
- or pseudorandomly distributed with respect to prime residues.

The next theorem target is a structural description of the **positions** of
the incidence phases, not merely their cardinalities.

That is the remaining object controlling reciprocal coupling.
