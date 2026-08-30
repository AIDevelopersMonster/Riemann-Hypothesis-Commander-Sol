# FCOA-Z Mixed-Sector Localization Principle 0.1

**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** PROVED / LOCAL STRUCTURAL THEOREM  
**Date:** 2026-08-30

---

## 1. Setup

Let

\[
B^{\pm}=\{P_0\}\sqcup B^+\sqcup B^-
\]

with zero reflection

\[
\nu(P_0)=P_0,
\qquad
\nu(B^+)=B^-,
\qquad
\nu(B^-)=B^+.
\]

Let \(\omega\) be a partial binary FCOA operation whose restriction to

\[
(\{P_0\}\cup B^+)^2
\]

is fixed in advance by the legacy positive-ray algebra.

Assume that the signed extension is simultaneously reflection-equivariant:

\[
\omega(\nu x,\nu y)=\nu_*(\omega(x,y))
\tag{1}
\]

for all defined cells, with a declared involution \(\nu_*\) on base and output values.

Partition the nonzero base-base table into four sectors:

\[
B^+\times B^+,
\qquad
B^+\times B^-,
\qquad
B^-\times B^+,
\qquad
B^-\times B^-.
\]

---

## 2. Mixed-Sector Localization Theorem

### Theorem 2.1

Once the positive sector and the output reflection involution are fixed, reflection equivariance uniquely determines the whole negative-negative sector.

Hence every remaining free base-base value/domain choice lies in the mixed sectors

\[
\boxed{
(B^+\times B^-)
\cup
(B^-\times B^+).
}
\tag{2}
\]

### Proof

Take any \(x,y\in B^-\). Since \(\nu\) exchanges the two branches, there exist unique \(x',y'\in B^+\) with

\[
x=\nu x',
\qquad
y=\nu y'.
\]

The positive-sector status of \((x',y')\) is already fixed. If it is undefined, reflection invariance of the domain forces \((x,y)\) to be undefined. If it is defined with value \(v\), then (1) forces

\[
\omega(x,y)
=\omega(\nu x',\nu y')
=\nu_*(v).
\]

Thus no negative-negative cell remains free.

By contrast, simultaneous reflection sends

\[
B^+\times B^-
\longleftrightarrow
B^-\times B^+.
\]

Neither mixed sector is the image of the fixed positive-positive sector. Therefore the positive legacy table plus reflection law imposes no value on a new mixed reflection orbit until one representative of that orbit is separately chosen. Hence all residual base-base freedom is localized in (2). \(\square\)

---

## 3. Corollary — novelty localization

### Corollary 3.1

For reflection-compatible signed extensions preserving the legacy positive ray exactly, the negative branch by itself contributes no new independent base-operation law: it is a forced mirror copy.

Any genuinely new signed interaction law must first appear in a mixed-sign orbit.

Symbolically,

\[
\boxed{
\text{legacy }(++ )
+\text{reflection}
\Longrightarrow
(-- )\text{ forced},
\qquad
(+ -),(- +)\text{ free}.
}
\tag{3}
\]

---

## 4. What can still be new outside the mixed sector

The theorem concerns **base-base operation cells** only.

Independent novelty can still occur through:

1. the choice of output-fiber reflection lift (`shared`, `split`, or another declared lift);
2. added unary structure on either branch;
3. deliberately broken reflection symmetry;
4. re-entry rules for output sorts;
5. additional carriers/lines.

Thus the localization theorem should not be misread as saying that every possible future FCOA-Z innovation must literally be a mixed base-base cell.

It says that under the current one-line, reflection-equivariant, legacy-preserving architecture, **all new binary base interaction freedom is mixed-sign freedom**.

---

## 5. Interpretation

This explains why the signed completion itself is conservative on each same-sign branch.

The sectors

\[
(++),\qquad(--)
\]

are inheritance sectors.

The sectors

\[
(+-),\qquad(-+)
\]

are interaction sectors.

Hence the first genuinely signed phenomena are naturally expected to be cross-branch phenomena:

- sign selection;
- branch coupling;
- cross-zero displacement;
- possible cancellation-like effects;
- possible transverse output events;
- later arithmetic or transport leakage.

No claim is made that any of these must reproduce ordinary integer arithmetic.

---

## 6. Research consequence

The future mixed-sector problem should therefore be treated as an **interaction theory**, not as a routine completion of the old table.

The immediate open question is:

\[
\boxed{
\text{which directed-displacement generator is the weakest nontrivial mixed interaction law?}
}
\]

The current branch intentionally leaves that law unfrozen.