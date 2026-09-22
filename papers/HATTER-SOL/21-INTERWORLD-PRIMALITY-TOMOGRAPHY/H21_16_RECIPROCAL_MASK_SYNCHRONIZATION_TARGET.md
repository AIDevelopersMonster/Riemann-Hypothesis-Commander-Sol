# HATTER-SOL-21 · RECIPROCAL MASK SYNCHRONIZATION TARGET

Status: **NEXT THEOREM STRIKE**

## 1. Problem

For a fixed world \(W=(B,C,\Delta)\), define

\[
X=L_W(p\leftarrow q),
\qquad
Y=L_W(q\leftarrow p).
\]

H21-LAB-11 shows that the coupling correction is exactly

\[
K
=
-\sum_a
\left(
\Pr[X=a,Y=a]-\Pr[X=a]^2
\right).
\]

Therefore every nonzero coupling comes from an excess or deficit of reciprocal
same-mask events.

## 2. Explicit Lucas conditions

For the \(p\leftarrow q\) direction, write

\[
\chi_p=\left(\frac{\Delta}{p}\right),
\qquad
\chi_q=\left(\frac{\Delta}{q}\right).
\]

The \(x\)-coordinate zero condition is

\[
\boxed{
U_q\equiv\chi_q\pmod p.
}
\]

The constant-coordinate zero condition is

\[
\boxed{
C U_{q-1}
\equiv
\frac{1-\chi_q}{2}B
\pmod p
}
\]

when \(\chi_p=1\), and

\[
\boxed{
U_{q+1}
\equiv
\frac{1+\chi_q}{2}B
\pmod p
}
\]

when \(\chi_p=-1\).

The reciprocal \(q\leftarrow p\) conditions are obtained by exchanging
\(p,q\).

Thus each same-mask event is an explicit **simultaneous reciprocal Lucas
congruence system**.

## 3. Four synchronization channels

The diagonal events are:

### Empty-empty

Neither defect coordinate vanishes in either direction.

### {0}-{0}

Exactly the constant coordinate vanishes in both directions.

### {1}-{1}

Exactly the \(x\)-coordinate vanishes in both directions.

### Full-full

Both coordinates vanish in both directions.

The observed negative \(K\) means the union of these four reciprocal
synchronization channels is more common than an independence model predicts.

## 4. Theorem targets

Seek, in increasing strength:

### Target A — exact residue-class formulation

Show that for fixed \(p\), each mask is a union of residue classes

\[
q\bmod\lambda_W(p).
\]

This follows from the local-clock theorem but must be written explicitly for
all four masks.

### Target B — reciprocal compatibility graph

Construct a directed finite graph whose vertices are local clock phases and
whose edges represent

\[
p\leftarrow q
\]

mask states.

The reciprocal pair \((p,q)\) samples two linked graph constraints.

Coupling becomes excess diagonal mass in the induced mask-pair graph.

### Target C — arithmetic synchronization criterion

Find conditions on

\[
p\bmod\lambda_W(q),
\qquad
q\bmod\lambda_W(p),
\]

or on the corresponding Frobenius/Lucas orders, which force

\[
X=Y.
\]

### Target D — covariance bound from arithmetic data

Bound

\[
|c_a|
\]

without enumerating all semiprime pairs.

That would turn H21 from an empirical compiler into a theorem-driven compiler.

## 5. Negative control

Do not assume quadratic reciprocity alone explains the effect.

The zero-mask conditions involve Lucas powers in residue algebras, not only
the signs

\[
\left(\frac{\Delta}{p}\right),
\qquad
\left(\frac{\Delta}{q}\right).
\]

Any proposed explanation must distinguish worlds having similar character
statistics but different measured coupling.

## 6. Hardware relevance

If reciprocal synchronization can be predicted from compact clock metadata,
the scheduler can flag coupling-dominated worlds before pairwise training.

This would remove the last expensive offline step in the current compiler.
