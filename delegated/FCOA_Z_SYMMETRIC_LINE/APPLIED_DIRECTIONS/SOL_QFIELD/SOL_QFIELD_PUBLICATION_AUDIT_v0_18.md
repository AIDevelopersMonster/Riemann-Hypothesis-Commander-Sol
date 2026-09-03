# SOL-QFIELD — Publication Audit: Fixed-Depth Scope of the FCOA Parikh Specialization

**Version:** 0.18  
**Date:** 2026-09-03  
**Status:** PUBLICATION CORRECTION / GENERAL THEOREMS UNAFFECTED

## Correction

For a safe non-root FCOA root-comb history word `w`,

\[
F_w(x_k)=\rho^{\#_R(w)}(x_k).
\]

Therefore endpoint equality on the carrier depends on `#R(w)` alone. Across histories of different lengths this is **coarser** than full binary Parikh equivalence. For example, `L` and `LL` have the same carrier endpoint but Parikh vectors `(1,0)` and `(2,0)`.

Hence any earlier wording saying that unrestricted native root-comb reconvergence is *exactly* the binary Parikh relation must be qualified.

The correct publication statement is:

> At each fixed history depth `m`, two safe binary root-comb histories have the same carrier endpoint iff they contain the same number of `R` events; since their lengths are equal, this is equivalent to equality of their full binary Parikh vectors. Thus the fixed-depth reconvergence fibers are exactly the Parikh fibers.

Equivalently, for

\[
W_{m,r}=\{w\in\{L,R\}^m:\#_R(w)=r\},
\]

all words in `W_{m,r}` reconverge, and `W_{m,r}` is precisely the Parikh fiber `(m-r,r)`.

Across different history depths, FCOA has additional `L`-stutter reconvergences. The abstract Parikh--abelianization theorem applies to the canonical fixed-depth/Parikh-preserving collision sector and remains unchanged.

## Consequences

The following results are unaffected:

- Parikh--Abelianization Collision Theorem;
- finite collision graph classification;
- relative augmentation collision ideal;
- canonical tight collision frame;
- constructive finite witness bound;
- sharp `S3` depth-five verifier, which already groups words by equal Parikh vectors;
- conditional Coxeter Clifford/CAR corollary.

The final article must distinguish:

\[
\text{unrestricted carrier reconvergence}
\supsetneq
\text{fixed-depth Parikh reconvergence}
\]

whenever histories of unequal length are admitted.

**Publication verdict:** correction incorporated; article assembly continues.