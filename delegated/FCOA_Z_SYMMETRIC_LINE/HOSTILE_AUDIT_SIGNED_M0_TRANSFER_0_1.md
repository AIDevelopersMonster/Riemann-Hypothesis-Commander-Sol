# Hostile Audit — FCOA-Z Signed M0 Reflection Transfer 0.1

**Branch:** `director/fcoa-z-symmetric-line`  
**Audited file:** `SIGNED_M0_REFLECTION_TRANSFER_0_1.md`  
**Date:** 2026-08-30  
**Verdict:** PASS WITH TWO SCOPE CLARIFICATIONS / theorem nucleus accepted

---

## 1. Audit target

The package claims that canonical positive-ray M0 admits a minimal simultaneous-reflection extension to the signed completion, with no mixed-sign arithmetic imported, and derives finite automorphism and definability consequences.

The audit attacks the following possible failure modes:

1. hidden use of ordinary integer sign laws;
2. hidden use of addition or multiplication in the generator;
3. inconsistency at cells involving the fixed origin;
4. ambiguity of the reflected base-domain table;
5. incorrect treatment of terminal output sorts;
6. accidental branchwise automorphisms omitted from the group calculation;
7. small-window exceptions;
8. confusion between full typed automorphisms and projected base automorphisms;
9. invalid FO non-definability inference from automorphisms;
10. silent promotion of reflection equivariance from one admissible extension to a universal FCOA-Z axiom.

---

## 2. Hidden-arithmetic attack

### Objection

Writing the signed carrier as positive and negative branches and reflecting one branch onto the other may merely disguise the usual arithmetic sign rule.

### Audit

The extension rule is

\[
\omega(\nu x,\nu y)=\nu_*(\omega(x,y)).
\]

This is a structural equivariance requirement. It mentions neither a binary addition graph nor a multiplication graph. The reflected `oplus` rule gives

\[
P_n^-\oplus P_0=P_{n-1}^-,
\]

which, under the external integer labels, moves from \(-n\) to \(-(n-1))=-n+1\). Hence it is **not** the global predecessor rule and is not ordinary signed addition in disguise.

Likewise no mixed-sign product cell is opened. Ordinary sign multiplication would necessarily impose information in such sectors.

### Verdict

PASS. Reflection is structural branch exchange, not an imported arithmetic law.

---

## 3. Fixed-origin consistency attack

### Objection

Because \(P_0\) is fixed by reflection, a positive cell involving \(P_0\) might be mapped onto a conflicting old positive cell.

### Audit

The positive old ray contains nonzero points only on the `+` branch. Simultaneous reflection sends

\[
(P_0,P_n^+)\mapsto(P_0,P_n^-),
\]

\[
(P_n^+,P_0)\mapsto(P_n^-,P_0),
\]

and

\[
(P_n^+,P_n^+)\mapsto(P_n^-,P_n^-).
\]

These reflected cells are not old positive cells. The only fully origin-fixed pair is \((P_0,P_0)\), which is undefined in both M0 operations and remains outside the minimal domain. Therefore no contradictory double assignment occurs.

### Verdict

PASS.

---

## 4. Uniqueness attack

### Objection

Could two different reflected tables have the same positive restriction and domain while both satisfy equivariance?

### Audit

Once the output involution \(\nu_O\) is fixed, every reflected value is forced by

\[
\omega(\nu x,\nu y)=\nu_*(\omega(x,y)).
\]

The domain is exactly the positive domain union its reflected image. Hence there is no residual freedom on that domain.

However, uniqueness does **not** extend to the choice of \(\nu_O\) itself, nor to later opening of mixed-sign cells.

### Verdict

PASS with scope retained exactly as stated: unique **relative to a chosen output reflection lift and minimal domain**.

---

## 5. Terminal-output attack

### Objection

Full typed automorphism groups may contain arbitrary permutations of unused output elements, invalidating the finite group formulas.

### Audit

The theorem explicitly restricts finite windows to output elements actually used by that finite restriction. Under that convention there is no unused-output symmetric kernel.

If instead one carries an ambient infinite output sort into every finite window, then unused terminal outputs would indeed contribute additional symmetric factors. This is the same typed-output caveat already known from earlier FCOA Fiber-Transport work.

### Scope clarification A

All finite automorphism formulas in the transfer package mean:

\[
\boxed{\text{exact finite typed restriction with only active output elements present}.}
\]

For ambient-output presentations, append the corresponding unused-output permutation kernels.

### Verdict

PASS after explicit scope clarification.

---

## 6. `oplus` automorphism attack

### Claimed group

\[
\operatorname{Aut}(W_N,\oplus)\cong C_2.
\]

### Audit

The base point \(P_0\) is uniquely characterized among base-sort points by the left-action property

\[
\forall x\ne P_0:\ P_0\oplus x=x.
\]

Right multiplication by \(P_0\) yields the parent map on two equal finite rooted chains. Hence an automorphism must preserve radial depth. At each positive depth there are exactly two candidates, one on each arm. Preservation of the parent relation forces the choice of branch swap to be globally consistent across all depths. Thus the base projection is exactly identity or full reflection.

For `ZM0-share`, diagonal values are fixed by depth and are compatible with both maps. For `ZM0-split`, the full reflection exchanges each paired output value and again extends uniquely. No independent per-depth swaps survive the parent-chain incidence.

For \(N=1\), the same conclusion holds: the two one-edge arms may be exchanged, so the group is \(C_2\).

### Verdict

PASS.

---

## 7. `otimes` split-fiber automorphism attack

### Claimed group

\[
(S_{N-1}\times S_{N-1})\rtimes C_2.
\]

### Audit

For \(N\ge2\), each branch has one local unit \(P_1^\sigma\) and a generic set of size \(N-1\). Distinct generic indices have identical domain pattern inside one branch, while split terminal outputs can be permuted coherently with any generic permutation. Thus each branch contributes an independent \(S_{N-1}\).

The two entire branch structures can be exchanged by reflection; that involution swaps the two symmetric-group factors, giving the wreath-product semidirect structure.

At \(N=2\), \(S_1\) is trivial, so the formula reduces to \(C_2\), as expected.

### Verdict

PASS.

---

## 8. `otimes` shared-fiber automorphism attack

### Claimed group

\[
S_{N-1}\times C_2.
\]

### Audit

Because the positive and negative radial-index-\(n\) generic points feed the **same** terminal outputs in both the `*` and diagonal `times` families, any positive generic permutation \(\pi_+\) and negative generic permutation \(\pi_-\) must induce the same permutation of the shared output fibers. Therefore

\[
\pi_+=\pi_-.
\]

This leaves one diagonal copy of \(S_{N-1}\). Global branch reflection survives and commutes with that simultaneous radial permutation, so the product is direct.

No larger branch-mixing permutation is possible because the two local units and branch incidence partition the generic points into two complete stars of the same type; any map sending one branch into the other forces the entire branch swap.

### Verdict

PASS.

---

## 9. Both-operation intersection attack

### Claimed group

\[
\operatorname{Aut}(W_N,\oplus,\otimes)\cong C_2.
\]

### Audit

The `oplus` group is already exactly \(C_2\). Both identity and reflection preserve `otimes` by construction. Hence the intersection is exactly \(C_2\).

### Verdict

PASS.

---

## 10. Commutation-count attack

For `oplus`, the only equal reversed defined pairs are the \(2N\) nonzero diagonal cells. Origin/nonzero pairs are both defined but unequal, and all other off-diagonal pairs lack two-sided definedness.

Thus

\[
|Comm_{\oplus}|=2N.
\]

For `otimes`, on each branch there are \(2(N-1)\) ordered unit/generic commuting pairs plus \(N-1\) generic diagonal pairs. Hence

\[
3(N-1)
\]

per branch and

\[
6(N-1)
\]

total.

### Verdict

PASS.

---

## 11. Partial-association attack

### Objection

Calling the operation nonassociative might be inappropriate because one bracketing is undefined by partiality.

### Audit

The canonical FCOA association diagnostic explicitly distinguishes `EQ`, `NEQ`, `LEFT`, `RIGHT`, and `NONE`. Therefore a triple for which one bracketing is defined and the other is not witnesses failure of partial associativity in the programme's declared sense.

The example

\[
(P_0\oplus P_0)\oplus x
\]

undefined versus

\[
P_0\oplus(P_0\oplus x)=x
\]

is valid.

### Scope clarification B

The claim is **failure of FCOA partial associativity / asymmetric bracketing definedness**, not a claim that two simultaneously defined bracketings evaluate to unequal base values.

### Verdict

PASS with terminology clarified.

---

## 12. FO automorphism-barrier attack

### Order

Reflection sends every strict comparison \(x<y\) to \(-x>-y\). Thus standard signed order is not invariant and cannot be parameter-free definable in a reduct admitting reflection as an automorphism.

### Multiplication

The graph

\[
Mul(x,y,z):xy=z
\]

contains \((1,1,1)\), while simultaneous reflection gives \((-1,-1,-1)\), which is not in the graph. Hence it is not invariant and cannot be parameter-free definable.

### Addition

The graph

\[
Add(x,y,z):x+y=z
\]

is invariant under simultaneous reflection because

\[
(-x)+(-y)=-(x+y).
\]

Therefore reflection supplies no analogous obstruction to addition.

### Audit issue checked

The argument concerns **parameter-free definability on the base sort** in the exact reflection-symmetric operational reduct. Naming a branch point or adding an asymmetric predicate can destroy the automorphism and invalidate this particular obstruction.

### Verdict

PASS.

---

## 13. Universality attack

### Objection

The package might silently make reflection equivariance a mandatory axiom of all FCOA-Z operations.

### Audit

The branch charter and transfer file both distinguish reflection-compatible extensions from genuinely asymmetric signed operations. The construction is therefore one canonical baseline class, not the definition of all future signed FCOA.

### Verdict

PASS. This distinction must remain explicit in every later theorem.

---

## 14. Final audit verdict

No mathematical defect was found in the theorem nucleus after the two scope clarifications above.

Promote the following branch results from PROVED-CANDIDATE to FIXED:

- minimal-domain reflection closure relative to a chosen output involution;
- radial interpretation of signed `oplus` right-zero action;
- survival of noncommutativity and partial-association asymmetry;
- shared/split terminal-fiber baselines;
- exact finite automorphism groups under active-output restriction;
- exact commutation counts;
- rooted radial memory with residual zero reflection;
- parameter-free zero-reflection barriers for order and multiplication;
- absence of a corresponding symmetry obstruction for addition.

The next research frontier is genuinely new rather than a repair:

\[
\boxed{
(+,-)\text{ and }(-,+)\text{ mixed-sector coupling.}
}

The correct next target is to classify the weakest couplings by their effect on:

1. reflection symmetry;
2. branch independence;
3. coordinate/radial memory;
4. additive leakage;
5. output-fiber transport potential.
