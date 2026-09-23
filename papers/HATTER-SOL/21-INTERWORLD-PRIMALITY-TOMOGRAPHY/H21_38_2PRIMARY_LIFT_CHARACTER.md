# HATTER-SOL-21 · 2-PRIMARY LIFT CHARACTER THEOREM

Status: **EXACT LOCAL THEOREM / BINARY-LIFT COMPLETION**

## 1. Setup

Fix a nonexceptional local quadratic world at an odd prime \(p\).

Let

\[
D_p=\langle \lambda_p\rangle\subset \mathbf F_p^\times
\]

be the scalar subgroup of order

\[
d_p.
\]

Assume \(d_p\) is even and write

\[
\boxed{
d_p=2^{a_p}u_p,
\qquad
a_p\ge1,
\qquad
u_p\ \text{odd}.
}
\]

The norm-square map on the scalar fiber is

\[
z\mapsto z^2.
\]

Its kernel is

\[
\{+1,-1\}.
\]

Thus every admissible norm value has the two lifts

\[
z,\ -z.
\]

## Theorem H21-2P1 — canonical 2-primary projection

Define

\[
\boxed{
\eta_p:D_p\to \mathbf F_p^\times,
\qquad
\eta_p(z)=z^{u_p}.
}
\]

Then:

1. the image of \(\eta_p\) is exactly the Sylow-\(2\) subgroup of \(D_p\);
2. its order is
   \[
   \boxed{2^{a_p}};
   \]
3. its kernel has odd order
   \[
   \boxed{u_p};
   \]
4. for every \(z\in D_p\),
   \[
   \boxed{
   \eta_p(-z)=-\eta_p(z).
   }
   \]

### Proof

Because \(D_p\) is cyclic of order \(2^{a_p}u_p\), raising to the odd-part
exponent \(u_p\) kills exactly the odd-order subgroup and maps onto the unique
subgroup of order \(2^{a_p}\).

Since \(u_p\) is odd,

\[
(-z)^{u_p}
=
- z^{u_p}.
\]

QED.

## Corollary H21-2P2 — every binary norm lift is visible in the 2-primary projection

If

\[
z^2=t^2
\]

inside \(D_p\), then

\[
z=\pm t.
\]

Applying \(\eta_p\),

\[
\boxed{
\eta_p(z)=\pm\eta_p(t),
}
\]

with the same sign.

Therefore the two norm lifts are always separated by the antipodal map in the
2-primary subgroup.

This remains true even in the regime where the quadratic character

\[
D_p\to\{\pm1\}
\]

cannot distinguish the lifts.

## 2. Exponent form

Write

\[
z=\lambda_p^k.
\]

Let

\[
\omega_p=\lambda_p^{u_p}.
\]

Then

\[
\operatorname{ord}(\omega_p)=2^{a_p}
\]

and

\[
\boxed{
\eta_p(z)=\omega_p^k.
}
\]

Thus the 2-primary observer sees only

\[
\boxed{
k\bmod 2^{a_p}.
}
\]

The norm-square datum sees

\[
\eta_p(z)^2=\omega_p^{2k},
\]

which determines

\[
\boxed{
k\bmod 2^{a_p-1}.
}
\]

Exactly one bit remains:

\[
\boxed{
\beta_p^{(2)}
=
\left\lfloor
\frac{k\bmod 2^{a_p}}
{2^{a_p-1}}
\right\rfloor
\in\{0,1\}.
}
\]

Hence the H21 binary norm-lift bit is the highest bit of the 2-primary exponent
coordinate.

## Corollary H21-2P3 — the two norm lifts toggle exactly the top 2-primary bit

The two scalar lifts differ by

\[
-z=z\lambda_p^{d_p/2}.
\]

Since

\[
\frac{d_p}{2}
=
2^{a_p-1}u_p
\equiv
2^{a_p-1}
\pmod{2^{a_p}}
\]

because \(u_p\) is odd, the two exponent classes differ by

\[
\boxed{
2^{a_p-1}
\pmod{2^{a_p}}.
}
\]

Therefore they have identical lower \(a_p-1\) bits and opposite highest bit.

## 3. Relation to H21-LC1

When

\[
a_p=1,
\]

the 2-primary subgroup has order two and

\[
\eta_p
\]

is exactly a \(\{\pm1\}\)-valued character.

This recovers the lift-character-visible regime of H21-LC1.

When

\[
a_p\ge2,
\]

a binary-valued group character may fail to distinguish \(z\) and \(-z\), but
the higher-order 2-primary projection \(\eta_p\) always does.

Thus H21-LC1 is the first layer of a complete 2-adic hierarchy.

## 4. Observer consequence

After projective phase and norm compatibility are fixed, every optional H21
zero-bit comparison in an even scalar fiber can be decided by comparing the
2-primary projections:

\[
\boxed{
z=t
\iff
z^2=t^2
\ \text{and}\
\eta_p(z)=\eta_p(t).
}
\]

Because norm compatibility already supplies the first condition, the remaining
binary observer decision is exactly the antipodal choice in the 2-primary
subgroup.

## 5. Reciprocal consequence

The unresolved semiprime pair problem is therefore sharpened from an abstract
binary lift to a concrete 2-primary exponent bit:

\[
\boxed{
\beta_{p\leftarrow q}^{(2)}
\quad\text{and}\quad
\beta_{q\leftarrow p}^{(2)}.
}
\]

The next arithmetic target is a reciprocal law, bias, or bound for these
highest 2-primary exponent bits after conditioning on:

- world;
- character stratum;
- projective phase;
- norm compatibility;
- observer target sheet.

## 6. Claim boundary

The Sylow decomposition of a cyclic group is classical.

The H21-specific content is the identification of the final residual
zero-mask observer bit with the highest 2-primary exponent bit after the exact
projective and norm reductions.

This theorem does not by itself establish publication novelty.
