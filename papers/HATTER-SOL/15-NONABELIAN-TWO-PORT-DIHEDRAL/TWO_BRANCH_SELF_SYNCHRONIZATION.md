# HATTER-SOL-15 · Two-Branch Self-Synchronization from One Fixed Prime

**Status:** exact theorem layer

Let `L/Q` be a Galois extension with

\[
G=\operatorname{Gal}(L/\mathbb Q)
\cong D_{2p}
=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle,
\]

where `p` is an odd prime. Let `q` be an unramified rational prime whose decomposition group is a reflection subgroup of order `2`. The fixed-prime family developed in H15 gives such worlds with `q=2` for every odd prime `p`.

Choose one prime `P_0` of `L` above `q` with

\[
D_{P_0}=\langle s\rangle.
\]

Since `e=1` and `f=2`, the number of primes above `q` is

\[
g=\frac{|G|}{2}=p.
\]

Write

\[
P_i=r^iP_0,
\qquad i\in\mathbb F_p.
\]

## Theorem H15.8 — the fixed prime carries all reflection branches

The decomposition subgroup at `P_i` is

\[
D_{P_i}=r^iD_{P_0}r^{-i}
=\langle \tau_i\rangle,
\]

where

\[
\boxed{\tau_i=r^{2i}s.}
\]

Thus the `p` branches of the single rational prime `q` in the Galois closure carry exactly the `p` reflection subgroups of `D_{2p}`.

### Proof

Stabilizers conjugate under the Galois action:

\[
D_{r^iP_0}=r^iD_{P_0}r^{-i}.
\]

Using `s r^{-i}=r^i s`,

\[
r^isr^{-i}=r^{2i}s.
\]

The `p` reflections `r^{2i}s` are distinct because `2` is invertible modulo the odd prime `p`. QED.

## Theorem H15.9 — two branches generate the rotation port

For distinct branches `P_i` and `P_j`,

\[
\boxed{\tau_i\tau_j=r^{2(i-j)}.}
\]

Since `i!=j` and `p` is prime, the exponent `2(i-j)` is nonzero modulo `p`. Therefore

\[
\boxed{\langle\tau_i\tau_j\rangle=\langle r\rangle\cong C_p.}
\]

Hence any ordered pair of distinct branches of the **same rational prime** determines a generator of the full rotation subgroup.

Reversing the order reverses the generator:

\[
\tau_j\tau_i=(\tau_i\tau_j)^{-1}.
\]

Thus an unordered pair determines the cyclic frame up to orientation, while an ordered pair determines an oriented cyclic frame.

## Theorem H15.10 — exact branch synchronization

Fix an ordered pair `(P_i,P_j)` with `i!=j` and put

\[
R_{ij}:=\tau_i\tau_j.
\]

Then `R_{ij}` acts transitively and freely on the `p` primes above `q`. Consequently every branch `P_k` has a unique coordinate

\[
\boxed{m\in\mathbb F_p}
\]

such that

\[
P_k=R_{ij}^{\,m}P_i.
\]

Therefore two distinguished branches of a single fixed prime give a complete internal coordinate system on all of its Galois branches.

### Proof

`R_{ij}` is a generator of the normal subgroup `C_p`, which acts regularly on the `p` primes above `q`. Regularity gives existence and uniqueness of `m`. QED.

## Corollary H15.11 — base size two

The action of `D_{2p}` on the `p` primes above `q` has permutation-group base size

\[
\boxed{2}.
\]

Indeed, one branch has stabilizer of order `2`, while two distinct branches have trivial common stabilizer because distinct reflection subgroups intersect trivially.

In classical permutation-group terminology, any two distinct prime branches form a base.

## 4. Self-synchronization hierarchy

For the same fixed rational prime `q`:

1. **no distinguished branch:** the `p` branches are a transitive Galois orbit;
2. **one distinguished branch:** an anchor is selected, but a reflection ambiguity remains;
3. **two distinguished branches, unordered:** the network obtains a cyclic coordinate frame up to reversal;
4. **two distinguished branches, ordered:** the network obtains a full oriented coordinate frame.

Thus

\[
\boxed{
\text{one fixed prime}
\to
p\text{ reflection branches}
\to
\text{two branches}
\to
\text{rotation generator}
\to
\text{full sector coordinates}.
}
\]

No second rational prime is required.

## 5. Relation to observer/surface structure

This theorem explains the earlier observer ladder structurally.

- An unordered branch pair supplies the orientation-free cyclic carrier needed by metric observers.
- Ordering the pair selects a direction and supplies the oriented displacement structure.

Hence the transition

\[
\mathsf C_{metric}=2
\quad\to\quad
\mathsf C_{oriented}=1
\]

corresponds exactly to whether the two synchronizing branches are unordered or ordered.

## 6. Claim boundary

The set of all primes above `q` is canonical, but a particular ordered pair is additional marked data. Therefore H15 does not claim that the arithmetic world spontaneously chooses a global coordinate frame. It claims something more precise:

\[
\boxed{\text{the factorization of one fixed prime contains enough internal structure that any two distinct marked branches rigidify the whole dihedral branch network.}}
\]

This is a classical finite-group statement applied to arithmetic decomposition data, not a physical synchronization mechanism.