# FCOA Definition 1.0

**Full name:** Fixed-Carrier Oriented Algebra  
**Russian:** Ориентированная алгебра фиксированного носителя  
**Status:** normative working definition 1.0  
**Role:** backend mathematical definition for the FCOA programme  
**Depends on:** `FCOA_FOUNDATIONAL_SPECIFICATION.md`  
**Does not replace:** the published `M0 -> G1 -> G2` theorem chain or later research branches

---

## 1. Purpose

This document answers a narrow question:

> What mathematical object is meant by an FCOA before any particular research extension such as G1, G2, G3, G4, arithmetic leakage, CRT, BIT history or nesting is added?

FCOA is not defined as a group, ring, semiring, field or ordinary total algebra. The natural standard setting is a typed partial algebra equipped with an oriented carrier presentation and a distinguished erasure/reduct operation.

---

## 2. Signature

An FCOA signature is a tuple

\[
\Sigma=(\mathsf B,\mathsf O_1,\ldots,\mathsf O_t;\Omega),
\]

where:

- `B` is the active/base sort;
- `O_1,...,O_t` are optional output sorts;
- `Omega` is a finite family of partial operation symbols of fixed arity.

In the canonical FCOA line the principal operation symbols are binary:

\[
\oplus,\qquad\otimes.
\]

The symbols are names only. They carry no inherited laws from ordinary addition or multiplication.

---

## 3. Oriented carrier

An oriented carrier is a pair

\[
(B,\preceq),
\]

where `B` is a set and `preceq` is a fixed orientation relation used by the construction.

In the canonical natural-carrier realization,

\[
B=\mathbb N_0=\{0,1,2,\ldots\},
\]

with

\[
0<1<2<\cdots.
\]

The notation

\[
P_n
\]

is a structural renaming of the base point `n`. It is used when one must distinguish the FCOA element from ordinary arithmetic on the index.

### Arithmetic firewall

The carrier being `N_0` does not put ordinary

\[
+_{\mathbb N},\qquad \times_{\mathbb N}
\]

into the FCOA signature.

Any use of numerical indices is metamathematical unless the corresponding relation is explicitly present or proved internally definable.

---

## 4. Partial operations

A binary FCOA operation has type

\[
\omega:B\times B\rightharpoonup B\sqcup O_1\sqcup\cdots\sqcup O_t.
\]

The domain

\[
D_\omega\subseteq B^2
\]

is part of the mathematical structure.

If `(x,y)` is not in `D_omega`, then

\[
\omega(x,y)=\mathrm{UNDEF}.
\]

`UNDEF` is not an element and is not an operation value.

Argument positions are structural roles. Therefore

\[
\omega(x,y)
\]

and

\[
\omega(y,x)
\]

are independent cells unless a theorem or explicit rule relates them.

---

## 5. Output sorts and terminality

Outputs may leave the active carrier.

The canonical M0 realization uses three orthogonal output families:

\[
E^+=\{E_n^+:n\ge1\},
\]

\[
E^\ast=\{E_n^\ast:n\ge2\},
\]

\[
E^\times=\{E_n^\times:n\ge2\}.
\]

These are disjoint from `B` and from one another.

### Terminal-output convention

In Definition 1.0, outputs in these sorts are terminal by default: they are not legal inputs to the base operations unless an extension explicitly declares a larger typing rule.

Thus expressions such as

\[
E_i^+\oplus x
\]

or

\[
x\otimes E_j^\times
\]

are typed-undefined in the baseline.

A future system in which output objects can re-enter operations is an extension/subclass, not a silent completion of Definition 1.0.

---

## 6. Oriented presentation and erased reduct

An oriented FCOA presentation is

\[
\mathfrak F^{\mathrm{or}}
=(B,\preceq;O_1,\ldots,O_t;\Omega).
\]

Its carrier-erased operational reduct is

\[
\mathfrak F^\circ
=(B;O_1,\ldots,O_t;\Omega),
\]

obtained by removing the explicit orientation symbol from the signature.

The central memory question is always posed in the reduct:

> Which relations used to generate the table remain recoverable or first-order definable after the explicit orientation is erased?

This distinction is part of the FCOA definition, not merely a later diagnostic.

---

## 7. Canonical natural baseline M0

Definition 1.0 designates one reference structure for the main programme:

\[
\mathfrak F_{M0}^{\omega}.
\]

Its active carrier is

\[
B=\mathbb N_0.
\]

Its two principal partial operations are `oplus` and `otimes`.

### 7.1 Baseline `oplus`

For every `n>=1`:

\[
0\oplus n=n,
\tag{A1}
\]

\[
n\oplus0=n-1,
\tag{A2}
\]

\[
n\oplus n=E_n^+.
\tag{A3}
\]

All other base-base cells are undefined.

Therefore

\[
0\oplus0=\mathrm{UNDEF},
\]

and for `m,n>0`, `m!=n`:

\[
m\oplus n=\mathrm{UNDEF}.
\]

### 7.2 Baseline `otimes`

For every `n>=1`:

\[
0\otimes n=0.
\tag{M1}
\]

For every `n>=2`:

\[
n\otimes0=E_n^\ast,
\tag{M2}
\]

\[
1\otimes n=n\otimes1=n,
\tag{M3}
\]

\[
n\otimes n=E_n^\times.
\tag{M4}
\]

All other base-base cells are undefined.

In particular:

\[
0\otimes0=\mathrm{UNDEF},
\]

\[
1\otimes0=\mathrm{UNDEF},
\qquad
1\otimes1=\mathrm{UNDEF},
\]

and for distinct `m,n>=2`:

\[
m\otimes n=\mathrm{UNDEF}.
\]

---

## 8. Why M0 has two different principal operations

`oplus` and `otimes` are not intended as partial reconstructions of ordinary arithmetic.

They have different laboratory roles.

### `oplus`

`oplus` is a boundary/predecessor operation. It contains strong directional asymmetry already at M0:

\[
0\oplus n=n,
\qquad
n\oplus0=n-1.
\]

It is therefore useful for studying boundary-mediated order memory.

### `otimes`

`otimes` is a symmetry-rich reference operation. On the generic sector

\[
G=\{2,3,4,\ldots\},
\]

the generic off-diagonal table is deliberately empty at M0.

This preserves a large symmetry baseline on finite truncations and makes `otimes` the principal laboratory for measuring how domain geometry and value geometry destroy exchangeability.

---

## 9. Finite truncations

For `N>=3`, define the finite active carrier

\[
B_N=\{0,1,\ldots,N\}
\]

or equivalently

\[
X_N=\{P_0,\ldots,P_N\}.
\]

The finite baseline

\[
\mathfrak F_{M0}^{N}
\]

is obtained by restricting the stable M0 rules to the finite active carrier and the corresponding output elements.

Finite truncations are the primary objects for the exact automorphism, association-spectrum, support-cost and finite uniform-definability experiments.

The infinite master object is the coherent union of the stable baseline rules, but no finite theorem is automatically promoted to the infinite structure.

---

## 10. Three statuses for unspecified behaviour

FCOA distinguishes three notions.

### `UNDEF`

A mathematical property of the current structure:

\[
(x,y)\notin D_\omega.
\]

### `OUT`

A finite-truncation bookkeeping status: a globally generated result exists but lies beyond the present finite carrier.

### `OPEN`

A research-programme status: no canonical future rule has yet been selected for a sector.

Therefore a cell may be

\[
\boxed{\text{fixed UNDEF in M0}}
\]

and simultaneously

\[
\boxed{\text{open as a location for a future extension}}.
\]

Opening such a cell creates a new FCOA structure. It does not repair a missing value in M0.

---

## 11. Extensions

### Definition 11.1 — FCOA extension

An extension of an FCOA structure may:

1. open previously undefined operation cells;
2. add new terminal/output sorts;
3. split value fibers by assigning different outputs;
4. add a new partial operation symbol;
5. add an external relation used as a generator scaffold;
6. add an auxiliary carrier/sort;
7. change the typing discipline, if explicitly declared.

An extension must identify which baseline rules remain unchanged.

### Named examples

- `G1`: adds an external relation but does not alter M0 operation cells;
- `G2`: compiles directed adjacency into new definedness cells of a partial operation;
- `G3/G4`: change value/domain geometry in post-publication structures;
- Arithmetic-Leakage constructions add further generated memories or representations.

These are extensions of the programme, not hidden clauses of M0.

---

## 12. Subclasses

Definition 1.0 recognizes the following useful subclasses.

### Line-FCOA

The active carrier orientation is a linear order.

### Finite FCOA

The active carrier is finite.

### Typed-output FCOA

Active and output sorts are explicitly distinguished.

### Terminal FCOA

Output-sort elements cannot re-enter the principal operations.

### Nested-output FCOA

A future/generalized subclass in which some output-sort elements are legal inputs to further operations. No canonical Definition-1.0 nesting law is assumed.

### Generated FCOA family

A coherent family of finite structures produced by one declared uniform generator rule.

---

## 13. Morphisms

A full categorical theory is not yet frozen. Definition 1.0 therefore fixes only the minimal safe notion.

### Definition 13.1 — strict FCOA homomorphism

A strict typed homomorphism

\[
h:\mathfrak F\to\mathfrak G
\]

is a sort-preserving map such that whenever

\[
\omega^{\mathfrak F}(x_1,\ldots,x_k)=y
\]

is defined, then

\[
\omega^{\mathfrak G}(h(x_1),\ldots,h(x_k))=h(y)
\]

is defined and equal.

No converse definedness condition is required for a homomorphism.

### Definition 13.2 — strong embedding

A strong embedding additionally reflects definedness and operation values on its image.

### Definition 13.3 — automorphism

An automorphism is a bijective strong self-embedding preserving the declared sorts and all primitive symbols of the reduct under study.

The precise treatment of orientation-preserving versus orientation-erased morphisms remains context-dependent and must be stated with the structure.

---

## 14. Relationalization

Every partial operation can be relationalized by its graph:

\[
T_\omega(x_1,\ldots,x_k,y)
\iff
\omega(x_1,\ldots,x_k)=y.
\]

Definedness becomes

\[
\operatorname{Def}_\omega(x_1,\ldots,x_k)
\iff
\exists y\,T_\omega(x_1,\ldots,x_k,y).
\]

This relationalized presentation is the standard interface for first-order definability and interpretation questions.

No expressive power is gained merely by switching between a partial-function presentation and its exact graph relation.

---

## 15. Canonical derived diagnostics

The following are derived from an FCOA structure and are not primitive unless explicitly named.

### Domain geometry

\[
D_\omega.
\]

### Left and right translations

\[
L_a^\omega(x)=\omega(a,x),
\qquad
R_a^\omega(x)=\omega(x,a).
\]

### Commutation locus

\[
\operatorname{Comm}_\omega
=\{(x,y):\omega(x,y),\omega(y,x)\text{ are defined and equal}\}.
\]

### Association status

For a triple `(x,y,z)`, compare

\[
\omega(\omega(x,y),z)
\]

and

\[
\omega(x,\omega(y,z))
\]

when the typing permits the intermediate outputs to re-enter the operation. In a terminal FCOA many bracketings are undefined by type.

The finite programme records the five statuses

`EQ`, `NEQ`, `LEFT`, `RIGHT`, `NONE`.

### Automorphism group

\[
\operatorname{Aut}(\mathfrak F^\circ)
\]

measures symmetry after the selected external structure is erased.

---

## 16. Memory levels are properties, not axioms

Terms such as

- rigidity;
- order memory;
- EqGap/additive memory;
- multiplication/full-arithmetic memory

are not part of the definition of FCOA.

They are properties of particular FCOA families after a stated erasure and in a stated logical language.

Thus one may have an FCOA that is:

- highly symmetric;
- rigid but without uniform FO order;
- order-recovering but non-additive;
- additive but not multiplicative;
- fully arithmetic.

Definition 1.0 deliberately permits all of these.

---

## 17. Laws not assumed

No FCOA axiom states any of the following:

\[
x\oplus y=y\oplus x,
\]

\[
(x\oplus y)\oplus z=x\oplus(y\oplus z),
\]

\[
x\otimes y=y\otimes x,
\]

\[
(x\otimes y)\otimes z=x\otimes(y\otimes z),
\]

or any distributive law.

Global neutral elements, inverses and closure of all outputs in the active sort are also not assumed.

Any such law, local or global, is a theorem of a concrete operation table if true.

---

## 18. Equality of FCOA presentations versus equality of represented information

Two presentations may encode the same recoverable structure at different resource cost.

Definition 1.0 distinguishes:

1. literal isomorphism of partial algebras;
2. definitional equivalence / mutual FO interpretability;
3. equality of a selected recovered relation;
4. equality of semantic leakage level.

These are not interchangeable.

The programme does not yet freeze one universal equivalence notion for all resource comparisons. Any optimization theorem must declare which notion of representation equivalence is being used.

---

## 19. Fixed / Working / Open ledger

### F — fixed in Definition 1.0

- active natural carrier for the canonical line;
- partial operations with structural domains;
- positional argument roles;
- typed output sorts;
- terminal baseline convention;
- explicit oriented presentation and carrier-erased reduct;
- M0 rules A1-A3 and M1-M4;
- unspecified M0 base cells are mathematically UNDEF;
- ordinary natural addition and multiplication are not primitives;
- new rules create explicit extensions;
- relationalization is the FO interface;
- no ordinary algebraic laws are inherited by notation.

### W — working conventions

- `Fixed-Carrier Oriented Algebra` / `FCOA` as programme terminology;
- the precise category-theoretic package of morphisms;
- the choice of strict homomorphism above as the default safe morphism;
- whether the infinite master object or coherent finite family should be primary in the final abstract theory.

### O — foundational open problems

- canonical generic off-diagonal law for `oplus`, if any;
- canonical generic off-diagonal law for `otimes`, if any;
- formal nested-output subclass axioms;
- representation-equivalence notion for intrinsic resource complexity;
- whether orientation should belong to the mathematical object itself or only to generator provenance in the most abstract definition;
- minimal axiom package broad enough to contain all useful FCOA families but narrow enough to exclude arbitrary unrelated partial algebras.

---

## 20. Definition 1.0 in one line

A **Fixed-Carrier Oriented Algebra** is, in the current programme, a typed partial algebra built on a declared oriented active carrier, with argument-role-sensitive operation domains and optional output sorts, studied together with the reduct obtained after erasing the explicit carrier orientation in order to measure which structural information has been compiled into the operations themselves.

The canonical natural reference object is

\[
\boxed{
\mathfrak F_{M0}^{\omega}
=(\mathbb N_0;E^+,E^\ast,E^\times;\oplus,\otimes)
}
\]

with the M0 tables fixed in Section 7 and all other base cells undefined.

---

## 21. Backend/frontier separation rule

This document belongs to the **backend** of the programme.

It may change only through an explicit foundational revision such as `Definition 1.1` or `Definition 2.0`.

Frontier research may add new branches, generators, auxiliary carriers, arithmetic memories and interpretation mechanisms without silently changing this definition.

Conversely, a frontier result that reveals a genuine inconsistency or insufficiency in Definition 1.0 must be promoted as an explicit foundational revision rather than patched locally inside one branch.
