# RGPA / RPM — Response to Review 1 and Novelty Audit

**Version:** 0.1  
**Date:** 2026-08-31  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** REVIEW PROCESSED / NOVELTY CLAIMS NARROWED / UNIVERSAL-PROPERTY TARGET CORRECTED

---

## 1. Executive verdict on Review 1

Review 1 is valuable and correctly identifies the central strategic issue: the internal theorem package is now dense enough that the main publication risk is overlap with existing partial-algebra, partial-group, groupoid, orbit, and double-coset theory.

However, several novelty statements in the review are too strong, and its proposed next step (`free RPM over Set built as a word tree`) is not correct for the RPM category currently defined.

The review is therefore accepted as a **major strategic review**, but not adopted verbatim.

The corrected verdict is:

\[
\boxed{
\text{the RPM/RGPA package has genuine internal structure,}
\text{ but no priority claim is frozen yet.}
}
\tag{1}
\]

The strongest currently defensible novelty target is not the classical group-action machinery itself, but the combination

\[
\boxed{
\text{partial binary operation}
+
\text{covariant involutive reflection}
+
\text{protected undefinedness}
+
\text{reflection/exchange equalizer}
+
\text{conservative completion moduli}.
}
\tag{2}
\]

---

## 2. Points from Review 1 that are accepted

### 2.1 Classical status of the diagonal quotient

The reviewer is correct that

\[
G\backslash(Z_1\times Z_2)
\tag{3}
\]

is standard orbit theory once the local decoration spaces have been identified as `G`-sets.

The novelty, if any, must lie in how the `Z_i` and their actions arise from reflection-compatible partial-algebra completion, not in the existence of diagonal orbits.

### 2.2 Classical status of the double-coset fiber

Likewise, after fixing transitive individual `G`-orbits, the fiber

\[
H_1\backslash G/H_2
\tag{4}
\]

is classical. Mackey theory, Hecke theory, biset theory, and ordinary orbit theory all use double cosets extensively.

Our theorem remains mathematically useful because it identifies the exact local stabilizers arising from RPM decoration data, but the double-coset mechanism itself is not a novelty claim.

### 2.3 Classical status of the factorization criterion and Burnside count

The criteria

\[
G=H_1H_2
\tag{5}
\]

and the Burnside enumeration formula are standard group-action consequences. They should be presented as tools applied to the RPM completion moduli problem, not as new group theory.

### 2.4 Bibliographic audit is mandatory

This recommendation is fully accepted. In particular, the comparison class must include not only partial `*`-algebras and locality semigroups, but also modern partial groups and their finite enumeration theory.

---

## 3. Corrections to Review 1

### 3.1 The diagonal quotient is not itself “classified by double cosets” in full generality

For arbitrary `G`-sets `Z_1,Z_2`, the primary object is simply the diagonal orbit space

\[
G\backslash(Z_1\times Z_2).
\tag{6}
\]

Double cosets classify the fiber over a chosen pair of transitive individual orbit classes, equivalently after choosing representatives and stabilizers.

Thus the exact statement is the one already proved in the RPM report:

\[
\Phi^{-1}([z_1],[z_2])
\cong
H_1\backslash G/H_2.
\tag{7}
\]

This distinction should be retained in the paper.

### 3.2 “Twisted stabilizers are new” is not yet justified

Our local action

\[
\gamma\star_p z
=
\nu^{\varepsilon_p(\gamma)}\gamma z
\tag{8}
\]

is a genuine action and is intrinsic to the chosen representative of a reflected input orbit. But actions modified by homomorphisms/cocycles into an involution group are standard constructions in transformation-group language.

Therefore the safe claim is:

\[
\boxed{
\text{the twisted action is the correct RPM classifier;}
\text{its abstract group-action form is not claimed new.}
}
\tag{9}
\]

### 3.3 “Relative reflection phase has no analogues” is unsupported

The SAME/OPPOSITE bit is a useful minimal relational invariant inside RPM. But relative-position, parity, cocycle, and double-coset labels occur throughout group actions, bundle theory, cohomology, and representation theory.

Therefore the phrase “has no analogues” must not be used.

The defensible statement is:

\[
\boxed{
\delta\text{ is the smallest RPM manifestation of the double-coset interaction label.}
}
\tag{10}
\]

### 3.4 The minimal SAME/OPPOSITE example is internally new, not yet externally certified new

The proof that the four-element construction is minimal for the specific stabilizer-breaking mechanism is an internal theorem of our framework.

It is premature to call it “genuinely new in mathematics” until finite involutive partial systems have been searched more deeply.

This caution is especially necessary because Philip Hackney's 2026 work enumerates binary partial groups (BPGs), which are unital partial magmas with involution satisfying strong inverse-property axioms, and develops finite classification algorithms on involutive carriers.

RPM is substantially weaker than BPG and uses a covariant reflection law rather than inverse-property axioms, but the methodological neighborhood is much closer than Review 1 indicates.

---

## 4. Literature audit: confirmed neighboring theories

### 4.1 General partial algebras are a mature subject

Relevant foundational literature includes:

- P. Burmeister, *A Model Theoretic Oriented Approach to Partial Algebras* (1986).
- E. S. Ljapin and A. E. Evseev, *The Theory of Partial Algebraic Operations* (1997), including homomorphisms, semigroup extensions, and factorization of partial groupoids.
- Modern categorical work such as M. Hoefnagel and P.-A. Jacqmin, *Partial Algebras and Implications of (Weak) Matrix Properties*, Applied Categorical Structures 32 (2024), article 34, DOI 10.1007/s10485-024-09790-z.

In particular, categories of partial algebras with weak/strong notions of morphism and left adjoints for certain forgetful functors are already established technology.

### 4.2 Strong morphisms preserving and reflecting definedness are standard

Our strong RPM morphism condition

\[
(x,y)\in D_A
\iff
(fx,fy)\in D_B
\tag{11}
\]

is mathematically natural and important for legacy exactness, but it is not a new general partial-algebra notion. Strong/closed homomorphisms preserving and reflecting definedness occur in the classical partial-algebra literature.

The RPM contribution is the use of this exactness notion together with the reflection and exchange structures.

### 4.3 Locality semigroups are nearby but different

Locality semigroups and their nonsymmetric `R`-semigroup variants already formalize partial products and morphisms. They impose compatibility/associativity conditions absent from RPM.

Therefore RPM should not be advertised as “the first theory of directed partial products.” Its narrower distinction is the simultaneous-reflection equivariance and the derived exchange equalizer.

### 4.4 Partial `*`-algebras remain structurally distinct

A partial `*`-algebra satisfies the order-reversing involution law

\[
(xy)^*=y^*x^*.
\tag{12}
\]

RPM instead uses

\[
\nu\mu(x,y)=\mu(\nu x,\nu y),
\tag{13}
\]

without swapping inputs.

This difference survives the audit and remains one of the cleanest reasons why the RPM mirror exchange locus is nontrivial rather than built into the involution axiom.

### 4.5 Partial groups are a serious neighboring theory

Chermak partial groups are much more structured than RPM: they have an inversion map, a partial product on words, and group-like axioms.

Recent work makes the overlap strategically important:

- Edoardo Salati, *Limits and colimits, generators and relations of partial groups*, Journal of Algebra 622 (2023), 291-327, DOI 10.1016/j.jalgebra.2023.01.014, proves completeness/cocompleteness and develops free partial groups over structured input data.
- Philip Hackney, *On partial groups of small order*, arXiv:2605.26199 (2026), enumerates partial groups up to order 10 and explicitly treats binary partial groups as partial magmas on involutive sets with additional inverse-property identities.

Therefore any publication must explicitly explain why RPM is neither a reduct being used trivially nor a disguised BPG/partial group.

---

## 5. The free-RPM recommendation from Review 1 is incorrectly formulated

Review 1 proposes a free RPM over a set `X` built as a tree of words. For the current weak-morphism category `RPM`, this is not the free object.

### Theorem 5.1 — weak free RPM over `Set` is degenerate

Let

\[
U:\mathbf{RPM}\to\mathbf{Set}
\tag{14}
\]

forget the reflection and partial product.

Then `U` has a left adjoint `F_w`, where

\[
F_w(X)=X\times C_2
\tag{15}
\]

with involution

\[
\nu(x,0)=(x,1),
\qquad
\nu(x,1)=(x,0),
\tag{16}
\]

and **empty multiplication domain**

\[
D_{F_w(X)}=\varnothing.
\tag{17}
\]

The unit is

\[
\eta_X(x)=(x,0).
\tag{18}
\]

For every RPM `A` and every set map `f:X->U(A)`, the unique RPM morphism extending `f` is

\[
\bar f(x,0)=f(x),
\qquad
\bar f(x,1)=\nu_Af(x).
\tag{19}
\]

#### Proof

Reflection compatibility forces (19), hence uniqueness. Since the source multiplication domain is empty, product preservation imposes no further condition. Thus every set map extends uniquely. QED.

### Consequence

The naive free object has no word-tree multiplication at all. Partiality makes the free weak object collapse to the least-defined operation.

Thus proving this adjunction would not supply the publication-level structure envisioned by Review 1.

---

## 6. Strong-morphism obstruction

Let `RPM_str` have the same objects but only strong morphisms.

### Theorem 6.1 — no free strong RPM over `Set`

The forgetful functor

\[
U_s:\mathbf{RPM}_{str}\to\mathbf{Set}
\tag{20}
\]

has no left adjoint.

### Proof

Assume a free object `F({x})` exists on one generator with unit element `u`.

Consider the singleton reflected set

\[
A_0=\{a\},
\qquad
\nu(a)=a,
\tag{21}
\]

with empty multiplication domain.

Also consider

\[
A_1=\{a\},
\qquad
\nu(a)=a,
\tag{22}
\]

with

\[
D_1=\{(a,a)\},
\qquad
\mu(a,a)=a.
\tag{23}
\]

The unique set map `{x}->{a}` must extend to strong morphisms

\[
F(\{x\})\to A_0
\quad\text{and}\quad
F(\{x\})\to A_1.
\]

Strongness of the first map forces `(u,u)` to be undefined in `F({x})`, because `(a,a)` is undefined in `A_0`.

Strongness of the second forces `(u,u)` to be defined, because `(a,a)` is defined in `A_1`.

Contradiction. QED.

### Consequence

The category-theoretic situation is sharper than Review 1 suggested:

\[
\boxed{
\text{weak free RPM over Set exists but is trivial;}
\quad
\text{strong free RPM over Set does not exist.}
}
\tag{24}
\]

This itself is an important structural fact for the theory.

---

## 7. Correct universal-property frontier

A nontrivial free construction requires more input than a bare set.

The correct source category must remember **which products are required/admissible/protected**.

Candidate source data are a reflection-admissibility scheme

\[
\mathfrak S=(X,\nu_X,R,P,\tau,\ldots),
\tag{25}
\]

where, depending on the model:

- `X` is a reflected generating set;
- `R` specifies required defined generator pairs or a grammar of admissible term pairs;
- `P` specifies protected undefined pairs;
- `tau` may specify output sorts or re-entry types.

The next meaningful theorem is therefore not

\[
F:\mathbf{Set}\leftrightarrows\mathbf{RPM}:U,
\]

but a **relative free completion** theorem

\[
\boxed{
F_{rel}:\mathbf{RefAdm}\leftrightarrows\mathbf{RPM}_{rel}:U_{rel},
}
\tag{26}
\]

or an equivalent initial-object theorem in a category of RPM realizations of a fixed admissibility schema.

This direction directly matches the actual FCOA notion of protected `UNDEF` and conservative generated completion.

---

## 8. Revised novelty table

| Component | Post-audit status |
|---|---|
| Partial magma / partial algebra | Classical |
| Strong morphism reflecting definedness | Classical |
| Involutive carrier | Classical |
| Partial `*`-algebra comparison | Classical neighboring theory, but anti-multiplicative law differs |
| Diagonal orbit quotient | Classical |
| Double-coset fiber | Classical |
| Stabilizer chain | Classical |
| Burnside enumeration | Classical |
| Twisted action `gamma star z` | Correct RPM mechanism; abstract novelty not claimed |
| Mirror equalizer `Eq(nu x nu,swap)=graph(nu)` | Elementary theorem; structural role in partial-operation exchange appears distinctive |
| `E_geom subset E_alg` and excess exchange locus | Potentially distinctive; novelty not yet certified |
| Protected-UNDEF conservative completion moduli | Potentially distinctive; requires deeper comparison with completion/extension theory of partial groupoids |
| One-orbit RPM passport | New within RPM; external novelty pending |
| SAME/OPPOSITE minimal stabilizer-breaking example | New within RPM; external novelty pending |
| Relative reflection phase | Useful RPM local name for a double-coset/relative-position label; no claim of no analogues |
| Relative free completion over reflection-admissibility schema | High-value open frontier |

---

## 9. Publication decision after Review 1

The review strengthens confidence in mathematical coherence but **does not justify immediate standalone publication**.

In fact, the literature audit raises the publication bar because two major neighboring bodies of work must now be handled explicitly:

1. general partial algebra theory, including strong homomorphisms and free/essentially algebraic constructions;
2. modern partial-group theory, including free objects, generators/relations, and finite enumeration on involutive carriers.

Therefore:

\[
\boxed{\text{standalone RPM/RGPA publication remains NOT FROZEN.}}
\tag{27}
\]

The correct publication threshold is now:

- a precise comparison theorem or separation theorem against BPG/partial groups;
- a relative-free or presentation theorem using protected/admissible domains;
- a full terminology search for covariant involutive partial magmas;
- retention of the finite moduli results with classical group-action ingredients clearly labeled as such.

---

## 10. Immediate next strike

The next theorem should be the **Weak-Free / Strong-No-Free / Relative-Free trichotomy**.

The first two legs are proved in Sections 5-6.

The remaining research target is:

\[
\boxed{
\text{construct the initial RPM realization of a finite reflection-admissibility schema}
\text{ while preserving protected UNDEF exactly.}
}
\tag{28}
\]

Then determine:

1. existence;
2. uniqueness up to unique isomorphism;
3. a term/graph normal form;
4. functoriality in schema morphisms;
5. whether every finite conservative RPM completion is a quotient/realization of such a relative free object.

This is a genuinely nontrivial universal-property problem aligned with FCOA rather than a generic free-partial-algebra construction.

---

## 11. Literature anchors fixed by this audit

- P. Burmeister, *A Model Theoretic Oriented Approach to Partial Algebras*, de Gruyter, 1986. DOI 10.1515/9783112720875.
- E. S. Ljapin and A. E. Evseev, *The Theory of Partial Algebraic Operations*, Kluwer/Springer, 1997. DOI 10.1007/978-94-017-3483-7.
- J.-P. Antoine and W. Karwowski, *Partial *-Algebras of Closed Linear Operators in Hilbert Space*, Publ. RIMS 21 (1985), 205-236. DOI 10.2977/prims/1195179844.
- M. Hoefnagel and P.-A. Jacqmin, *Partial Algebras and Implications of (Weak) Matrix Properties*, Applied Categorical Structures 32 (2024), 34. DOI 10.1007/s10485-024-09790-z.
- E. Salati, *Limits and colimits, generators and relations of partial groups*, Journal of Algebra 622 (2023), 291-327. DOI 10.1016/j.jalgebra.2023.01.014.
- P. Hackney, *On partial groups of small order*, arXiv:2605.26199, 2026.

---

## 12. Final response to Review 1

Review 1 correctly recognizes that the RPM/RGPA programme has passed the point of being merely an analogy extracted from SOL-GRADED.

But the novelty must be stated more conservatively than the review recommends.

The most important consequence of processing the review is a change of research direction:

\[
\boxed{
\text{do not spend the next step proving a naive free-RPM-over-Set theorem.}
}
\tag{29}
\]

That theorem is either trivial (weak morphisms) or false (strong morphisms).

Instead pursue the relative universal object controlled by **reflection admissibility + protected undefinedness**. That is the universal-property problem genuinely specific to the emerging FCOA/RPM architecture.
