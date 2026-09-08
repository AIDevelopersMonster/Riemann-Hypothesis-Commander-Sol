# FCOA Rigidity Cost — Safe-Minimizer Local Cone Audit

**Status:** post-publication computational theorem support for `alpha=beta`.

## 1. Purpose

`UNSAFE_BETA_WITNESS.md` exhibits a six-carrier layer with `beta=alpha=1` for which one optimal beta-repair is unsafe while other one-cell repairs are exact.

A natural counterexample strategy is therefore:

1. start from that unsafe witness;
2. add old cells so that the known safe one-cell alternatives become unavailable or cease to be exact;
3. retain an unsafe one-cell beta-repair;
4. force `beta=1<alpha`.

This note exhaustively tests the first two nontrivial levels of that strategy on the same carrier.

## 2. Base witness

Carrier:

`G={0,1,2,3,4,5}`.

Base domain:

`D0={(0,3),(2,3),(5,3),(1,3),(1,4)}`

with colors

`0,0,1,0,0`

in the displayed order.

The base layer has `beta=alpha=1`, but the added cell `(5,4)` is an unsafe minimum beta-witness for either binary value.

## 3. Complete nine-cell cone

Every superlayer obtained from `D0` by adding exactly four further old domain cells was enumerated, with all `2^4` binary color assignments on those added cells.

Total colored superlayers:

\[
\boxed{202,400}.
\]

Among them, the number remaining nonexact is

\[
\boxed{3,251}.
\]

Every nonexact layer satisfies

\[
\boxed{\beta=\alpha=1.}
\]

No state with positive overhead occurs.

Thus no nine-cell counterexample can be obtained by locally blocking safe repairs around this unsafe witness.

## 4. Complete ten-cell cone

The audit was extended to every superlayer obtained from `D0` by adding exactly five further old cells, with all `2^5` binary assignments.

Total colored superlayers:

\[
\boxed{1,700,160}.
\]

Nonexact layers:

\[
\boxed{8,334}.
\]

Again every nonexact layer has

\[
\boxed{\beta=\alpha=1.}
\]

and no positive-overhead state occurs.

## 5. Structural conclusion

The most obvious mechanism for producing `eta>0` from the known unsafe minimizer fails robustly:

> adding several old cells to eliminate alternative safe repair positions does not, through ten total defined cells on the same six-point carrier, force the unsafe minimizer to become unavoidable.

Unsafe minimizers therefore appear to coexist with safe minimizers in a structurally stable way, not merely by accident in the smallest example.

This supports an **existential safe-selection principle** rather than any claim that individual minimizers are safe.

## 6. Current finite evidence for the stronger conjecture

The known evidence now includes:

- every layer with `|G|<=5` has `eta=0`;
- every six-carrier layer with `|D|<=8` has `eta=0`;
- all `202,400` nine-cell colored superlayers in the local cone of the first unsafe witness have `eta=0`;
- all `1,700,160` ten-cell colored superlayers in the same local cone have `eta=0`.

The local-cone statements do not replace a complete audit of all six-carrier layers with `|D|=9` or `10`.

## 7. Next theoretical target

A proof of `alpha=beta` should explain why an unsafe minimum repair can be **rerouted** to another repair of the same size.

The finite evidence suggests studying the family

\[
\mathcal M_\beta(D,c)
=
\{(E,b): |E|=\beta,\ E\text{ destroys all old bad automorphisms}\}
\]

as a finite exchange system.

The desired statement is not that every element of `\mathcal M_\beta` is safe, but that the safe subset is nonempty.

A promising next question is whether minimum repair sets satisfy an exchange property relative to their killed-old-automorphism incidence hypergraph, strong enough to move away from every domain-mixing orbit without increasing cardinality.

## Claim firewall

1. The cone audits are exhaustive only for superlayers containing the fixed base witness `D0`.
2. They do not prove the global conjecture `alpha=beta`.
3. They do prove that the simplest local-blocking strategy does not yield a counterexample through ten defined cells on the base six-point carrier.
