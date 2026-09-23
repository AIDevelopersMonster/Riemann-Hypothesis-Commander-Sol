# HATTER-SOL-21 · DEFECT-SURFACE FACTORIZATION TARGET

Status: **NEXT ACTIVE STRIKE**

## 1. Why the target changed

LAB-04 closed the static split/inert geometry as a finite periodic character
system.

Therefore the next surface coordinates must retain the actual Frobenius
defect, not only its quadratic sign.

For world \(W=(B,C,\Delta)\), let

\[
x^n=(u_W(n),v_W(n))
\]

in the basis \(1,x\).

Let the expected prime response be

\[
E_W(n)=
\begin{cases}
(0,1),&(\Delta/n)=+1,\\
(B,-1),&(\Delta/n)=-1.
\end{cases}
\]

Define

\[
\boxed{
\delta_W(n)=x^n-E_W(n)
=(d_{0,W}(n),d_{1,W}(n))
\pmod n.
}
\]

For nonexceptional primes,

\[
\delta_W(p)=(0,0).
\]

For composites the defect may be zero (pseudoprime response) or nonzero.

## 2. Factor projections

Every nonzero component gives a natural gcd projection

\[
g_{0,W}(n)=\gcd(n,d_{0,W}(n)),
\]

\[
g_{1,W}(n)=\gcd(n,d_{1,W}(n)).
\]

Also retain

\[
g_{01,W}(n)=\gcd(n,d_{0,W}(n),d_{1,W}(n)).
\]

A value strictly between \(1\) and \(n\) is an explicit factor witness.

## 3. Multiworld factor fingerprint

For \(m\) handles define

\[
\boxed{
\Phi_m(n)
=
\big(
g_{0,1},g_{1,1},g_{01,1};
\ldots;
g_{0,m},g_{1,m},g_{01,m}
\big).
}
\]

This is not a geometric drawing.

It is a factor-exposure field over arithmetic worlds.

Questions:

- how many composites yield at least one factor;
- how many yield two different factors in different worlds;
- whether semiprimes tend to expose one of the two prime factors consistently;
- whether prime powers and products behave differently;
- whether adaptive world ordering reduces expected factor-revelation time.

## 4. FPGA relevance

This target is hardware-friendly.

The sequential quadratic core already computes the defect pair before the final
PASS/FAIL comparison.

The only new blocks are gcd engines and a factor-witness accumulator.

Therefore H21-HW-01 can expose both:

\[
\boxed{\text{classification}}
\]

and

\[
\boxed{\text{factor revelation}}
\]

without changing the main modular-exponentiation datapath.

## 5. Publication discipline

A high empirical factor-exposure rate is not enough for publication.

The serious threshold is one of:

- an exact theorem about factor exposure under a declared world family;
- a minimal/adaptive world-selection theorem;
- a provable distinction between factor classes;
- a hardware/observer theorem not reducible to standard Frobenius testing.
