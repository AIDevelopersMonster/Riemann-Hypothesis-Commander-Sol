# SOL-TOPO — Fusion-Channel Shadows and the Strict-Line Braid Obstruction

**Version:** 0.1  
**Date:** 2026-08-30  
**Branch:** `director/fcoa-z-symmetric-line`  
**Status:** FIRST TARGET COMPLETE / ONE-STEP FUSION-CHANNEL EMBEDDING / BRAID-MEMORY NO-GO PROVED  
**Base:** FCOA-Z v1.1, DOI 10.5281/zenodo.22169264

---

## 1. Executive verdict

The first SOL-TOPO target has a sharp positive-negative answer.

1. **Positive result.** The existing FCOA terminal alphabet

\[
E_n^+,\qquad E_n^*,\qquad E_n^\times
\]

is already large enough to encode, at fixed radial level, the three simple Ising labels and hence the complete **support** of the multiplicity-free Ising fusion rules as finite output fibers. In particular, the two-channel rule

\[
\sigma\times\sigma=1+\psi
\]

has an exact typed-fiber shadow

\[
\Phi_n(\sigma,\sigma)=\{E_n^+,E_n^\times\}.
\]

2. **Conservative FCOA realization.** A uniform mixed-sign rule can open two previously undefined cells, one in `oplus` and one in `otimes`, so that the *bundled operation family* produces the two-channel fiber on equal-radius opposite-branch inputs. This preserves every legacy cell and reflection symmetry.

3. **First obstruction.** A raw FCOA binary operation is still a partial **function**. Therefore a single old operation cell cannot itself realize a fusion direct sum such as `1 + psi`. The two-channel object is a derived fiber over the operation family, not yet one intrinsic fusion operation.

4. **Second obstruction.** Current terminal outputs are sinks. Since `E`-values do not re-enter as legal inputs, the present FCOA cannot realize iterated fusion trees, `F`-moves, or the categorical associativity data of an anyon model.

5. **Braid-memory no-go.** A strict one-dimensional collision-free line has contractible unordered configuration space. Hence its fundamental group is trivial, whereas anyon braiding in two dimensions is controlled by the braid group. The current one-line FCOA therefore cannot derive non-Abelian braid memory from line geometry alone.

6. **Concrete Ising witness.** Even two exchanges of the same pair return the particles to the same endpoint ordering, yet in the Ising model the two fusion channels acquire different monodromy phases. Any endpoint-only FCOA encoding necessarily forgets this relative phase.

The programme verdict is therefore

\[
\boxed{\texttt{FORMAL EMBEDDING}}
\]

with the strict qualifier:

\[
\boxed{\text{one-step fusion-channel incidence only; not a braided fusion-category model}.}
\]

No physical identification is claimed.

---

## 2. FCOA-Z input used

Use the audited signed carrier

\[
B^{\pm}=\{P_0\}\sqcup\{P_n^+:n\ge1\}\sqcup\{P_n^-:n\ge1\}
\tag{1}
\]

with reflection

\[
\nu(P_0)=P_0,
\qquad
\nu(P_n^+)=P_n^-,
\qquad
\nu(P_n^-)=P_n^+.
\tag{2}
\]

On the positive M0 sector the terminal outputs include

\[
P_n^+\oplus P_n^+=E_n^+,
\tag{3}
\]

\[
P_n^+\otimes P_0=E_n^*\qquad(n\ge2),
\tag{4}
\]

and

\[
P_n^+\otimes P_n^+=E_n^\times\qquad(n\ge2).
\tag{5}
\]

The negative-negative copies are forced by simultaneous reflection. The genuinely mixed cells

\[
(P_i^+,P_j^-),\qquad(P_i^-,P_j^+)
\tag{6}
\]

remain the unique binary base sector in which new values can be introduced without altering the inherited same-sign tables.

The current output families are terminal: no general rule lets an `E`-value re-enter `oplus` or `otimes` as a new argument.

---

## 3. Target-field definitions: Ising fusion data

The Ising anyon model has three simple topological-charge labels

\[
\mathcal I=\{1,\psi,\sigma\}.
\tag{7}
\]

Its fusion rules are

\[
1\times a=a\times1=a,
\tag{8}
\]

\[
\psi\times\psi=1,
\tag{9}
\]

\[
\psi\times\sigma=\sigma\times\psi=\sigma,
\tag{10}
\]

and

\[
\boxed{\sigma\times\sigma=1+\psi.}
\tag{11}
\]

Let

\[
N_{ab}^c\in\{0,1\}
\tag{12}
\]

be the Ising fusion multiplicities. Equation (11) means

\[
N_{\sigma\sigma}^{1}=1,
\qquad
N_{\sigma\sigma}^{\psi}=1.
\tag{13}
\]

Thus a fixed input pair need not determine a unique fusion label. Instead one has a fusion space

\[
V_{ab}=\bigoplus_c V_{ab}^c,
\qquad
\dim V_{ab}^c=N_{ab}^c.
\tag{14}
\]

For Ising, all nonzero multiplicities are one, so the distinction between channel support and basis multiplicity is especially clean.

Braiding is additional data. On each channel there are `R`-symbols, and for three or more anyons reassociation between fusion trees is controlled by `F`-matrices. Fusion rules alone do not contain braid/path memory.

---

## 4. Theorem A — Exact typed-fiber encoding of Ising fusion support

Fix any radial level

\[
n\ge2
\tag{15}
\]

and define the FCOA output alphabet

\[
O_n=\{E_n^+,E_n^*,E_n^\times\}.
\tag{16}
\]

Define a bijection

\[
\chi_n:\mathcal I\to O_n
\tag{17}
\]

by

\[
\chi_n(1)=E_n^+,
\qquad
\chi_n(\sigma)=E_n^*,
\qquad
\chi_n(\psi)=E_n^\times.
\tag{18}
\]

For each `a,b in I`, define the typed channel fiber

\[
\Phi_n(a,b)
:=
\{\chi_n(c):N_{ab}^c=1\}
\subseteq O_n.
\tag{19}
\]

### Theorem 4.1 — Fusion-support embedding

The map `(18)-(19)` is faithful at the level of Ising fusion support:

\[
\boxed{
N_{ab}^c=1
\iff
\chi_n(c)\in\Phi_n(a,b).
}
\tag{20}
\]

In particular,

\[
\Phi_n(\sigma,\sigma)
=
\{E_n^+,E_n^\times\},
\tag{21}
\]

so a fixed pair of input labels has a two-element typed output fiber rather than one scalar result.

### Proof

By construction, `Phi_n(a,b)` contains exactly the images under the bijection `chi_n` of those labels `c` for which `N_ab^c=1`. Because `chi_n` is injective, no two Ising simple labels collapse to one FCOA output type. Because it is surjective onto `O_n`, every chosen FCOA terminal type has one Ising label. Hence membership in the fiber is equivalent to the corresponding fusion coefficient being nonzero, proving (20). Equation (21) follows from (13) and (18). QED.

### Corollary 4.2

The FCOA terminal alphabet is not intrinsically “scalar.” Its three existing typed families can serve as a finite channel alphabet.

### Limitation 4.3

The theorem encodes **support**, not arbitrary fusion multiplicity. If some target category has

\[
N_{ab}^c>1,
\tag{22}
\]

then one symbol `chi_n(c)` does not distinguish the multiple basis states in `V_ab^c`. Additional multiplicity labels or a vector-space fiber are required.

---

## 5. Theorem B — Conservative mixed-sector two-channel realization

The previous theorem is an incidence encoding. We now ask whether the two-channel pattern can be realized by conservative opening of current mixed-sign FCOA cells.

Work with the shared-fiber reflection lift, so

\[
\nu_O(E_n^\alpha)=E_n^\alpha
\qquad
(\alpha\in\{+,*,\times\}).
\tag{23}
\]

Define the **equal-radius mixed rule** `MC2` for every `n>=2` by

\[
P_n^+\oplus P_n^-=E_n^+,
\qquad
P_n^-\oplus P_n^+=E_n^+,
\tag{24}
\]

and

\[
P_n^+\otimes P_n^-=E_n^\times,
\qquad
P_n^-\otimes P_n^+=E_n^\times.
\tag{25}
\]

No other previously undefined cell is opened.

For a base pair `(x,y)` define the **bundled terminal channel set**

\[
\mathcal C(x,y)
:=
\{\omega(x,y):
\omega\in\{\oplus,\otimes\},
\ \omega(x,y)\text{ is defined and terminal}\}.
\tag{26}
\]

### Theorem 5.1 — Conservative two-channel mixed realization

The rule `MC2` is a conservative FCOA-Z line realization in the sense of `LINE_COMPLETION_GATE.md`, and for every `n>=2`,

\[
\boxed{
\mathcal C(P_n^+,P_n^-)
=
\mathcal C(P_n^-,P_n^+)
=
\{E_n^+,E_n^\times\}.
}
\tag{27}
\]

### Proof

All cells in (24)-(25) lie in the mixed sectors (6), which were undefined in the minimal reflection closure. Therefore no legacy positive, negative, origin, or same-sign value is modified.

The rule is uniform in radial level and is generated by two intrinsic conditions: equal nonzero radial depth and opposite branch sign. It is not a finite exception table.

Under reflection, `(P_n^+,P_n^-)` is sent to `(P_n^-,P_n^+)`. Equations (24)-(25) assign the same shared-fiber values to the reflected cells, so simultaneous reflection equivariance holds.

The line carrier, root, and reflection are unchanged. No ordinary integer addition or multiplication is inserted.

Finally, on either ordered equal-radius mixed pair, `oplus` contributes `E_n^+` and `otimes` contributes `E_n^times`, so the bundled set (26) is exactly (27). QED.

### Corollary 5.2 — One-dimensional closure of the channel alphabet

The construction is `1D-CLOSED` at the level of one-step channel support: the two channels are finite internal terminal fibers indexed by the existing radial coordinate. No second coordinate is required.

### Interpretation

Equation (27) is the precise version of the useful analogy

\[
\boxed{\text{mixed interaction}\longrightarrow\text{multiple typed output channels}.}
\tag{28}
\]

But it is essential that the two channels in (27) arise from a **bundle of two existing operation symbols**. That is weaker than intrinsic anyon fusion, where one tensor product `sigma x sigma` has two channels without an external choice of operation.

---

## 6. Theorem C — Single-operation channel obstruction

### Theorem 6.1

Let `omega` be any current FCOA binary operation, regarded as a partial function

\[
\omega:D_\omega\to Y.
\tag{29}
\]

Then no single cell `(x,y) in D_omega` can simultaneously have two distinct terminal values

\[
u\ne v,
\qquad
\omega(x,y)=u,
\qquad
\omega(x,y)=v.
\tag{30}
\]

Hence the Ising two-channel rule (11) cannot be represented by one unmodified FCOA operation cell as a genuine direct-sum-valued fusion operation.

### Proof

A partial operation is a function on its domain. Therefore each defined input pair has exactly one value. If both equalities in (30) held, functionality would imply `u=v`, contradicting distinctness. QED.

### Consequence

A genuinely intrinsic fusion operation requires at least one of:

1. a finite-valued relation;
2. a power-set/fiber-valued operation;
3. a direct-sum/vector-space-valued operation;
4. a derived bundle such as (26), with the explicit caveat that operation labels preselect channels.

Thus existing FCOA typed outputs supply the **channel alphabet**, but not yet the full fusion semantics.

---

## 7. Theorem D — Terminal-sink obstruction to `F`-moves

For three anyons, categorical fusion requires comparison of the two parenthesizations

\[
(a\times b)\times c
\qquad\text{and}\qquad
a\times(b\times c).
\tag{31}
\]

At the fusion-space level the change of basis has the form

\[
\bigoplus_e V_{ab}^e\otimes V_{ec}^d
\xrightarrow{\ F\ }
\bigoplus_f V_{bc}^f\otimes V_{af}^d.
\tag{32}
\]

The intermediate labels `e` and `f` must therefore remain active enough to participate in the next fusion step.

### Theorem 7.1 — No current FCOA `F`-move realization

In the present signed M0 structure, where every `E_n^alpha` is terminal and has no general re-entry law, there is no faithful realization of (32) using the current operation signature alone.

### Proof

Suppose a first fusion step is represented by a terminal output

\[
x\ \omega\ y=E_n^\alpha.
\tag{33}
\]

To realize a depth-two fusion tree, the intermediate result must next interact with a third input `z`, requiring at least one legal cell of the form

\[
E_n^\alpha\ \omega'\ z
\quad\text{or}\quad
z\ \omega'\ E_n^\alpha.
\tag{34}
\]

By the current terminal-output semantics, such re-entry is absent. Therefore the second composition in the fusion tree cannot be formed. Since (32) compares two depth-two decompositions, the current signature cannot even instantiate both sides, much less an invertible `F`-matrix between them. QED.

### Corollary 7.2

A full fusion-category model is locked behind `LC2 — Output re-entry`.

This is not evidence for a second spatial dimension. It is a typed-composition obstruction on the existing one-dimensional enriched line.

---

## 8. Theorem E — Strict-line braid obstruction

The key topological distinction is now exact.

Let

\[
\operatorname{Conf}_m(\mathbb R)
=
\{(x_1,\ldots,x_m)\in\mathbb R^m:x_i\ne x_j\text{ for }i\ne j\}
\tag{35}
\]

be the ordered collision-free configuration space, and let

\[
C_m(\mathbb R)
=
\operatorname{Conf}_m(\mathbb R)/S_m
\tag{36}
\]

be the unordered configuration space of `m` indistinguishable points on a line.

### Theorem 8.1 — Contractibility of unordered line configurations

For every `m>=1`,

\[
\boxed{C_m(\mathbb R)\text{ is contractible}.}
\tag{37}
\]

Consequently,

\[
\boxed{\pi_1(C_m(\mathbb R))=0.}
\tag{38}
\]

### Proof

Every unordered set of `m` distinct real points has a unique strictly increasing representative

\[
x_1<x_2<\cdots<x_m.
\tag{39}
\]

Hence `C_m(R)` is homeomorphic to

\[
\Delta_m
:=
\{(x_1,\ldots,x_m)\in\mathbb R^m:x_1<\cdots<x_m\}.
\tag{40}
\]

The region `Delta_m` is convex because the inequalities in (40) are strict linear inequalities and are preserved by convex interpolation. Every convex subset of a real vector space is contractible. Therefore `Delta_m`, and hence `C_m(R)`, is contractible. Its fundamental group is trivial. QED.

### Corollary 8.2 — No braid group from strict line geometry

A strict one-dimensional collision-free carrier cannot generate a nontrivial braid group from homotopy classes of particle worldlines. In contrast, for the plane one has the standard relation

\[
\pi_1(C_m(\mathbb R^2))\cong B_m.
\tag{41}
\]

Therefore non-Abelian anyon braiding cannot be **derived from the topology of the current one-line FCOA carrier**.

### FCOA consequence

The present line may still host an **abstract internal braid-action fiber** if one is added as new transport/history structure. What is ruled out is the stronger claim that the existing one-dimensional carrier geometry itself already contains non-Abelian braid memory.

Thus the required negative test returns

\[
\boxed{
\text{braid/path memory is fundamentally absent from strict one-line geometry unless extra transport/history structure is added.}
}
\tag{42}
\]

---

## 9. Theorem F — Concrete Ising endpoint-memory counterexample

For a standard right-handed Ising convention, exchange of two `sigma` anyons has channel-dependent phases

\[
R_{1}^{\sigma\sigma}=e^{-i\pi/8},
\qquad
R_{\psi}^{\sigma\sigma}=e^{3i\pi/8}.
\tag{43}
\]

Two exchanges return the particles to the original endpoint ordering, but act by

\[
(R_{1}^{\sigma\sigma})^2=e^{-i\pi/4},
\tag{44}
\]

and

\[
(R_{\psi}^{\sigma\sigma})^2=e^{3i\pi/4}=-e^{-i\pi/4}.
\tag{45}
\]

### Theorem 9.1 — Endpoint-only encodings erase Ising monodromy memory

Any encoding whose state after a process is determined only by

1. the final line positions/order of the two participants, and
2. the final fusion-channel label,

but carries no path/transport state, cannot faithfully represent the two-exchange Ising action on a superposition of the `1` and `psi` channels.

### Proof

After two exchanges, the endpoint ordering is the same as before. The channel labels themselves are also unchanged. Hence an endpoint-only encoding assigns the same classical endpoint record before and after the double exchange.

However, by (44)-(45), a state

\[
a|1\rangle+b|\psi\rangle
\tag{46}
\]

is transformed to

\[
e^{-i\pi/4}
\bigl(a|1\rangle-b|\psi\rangle\bigr),
\tag{47}
\]

which differs by a nontrivial relative phase whenever both coefficients are nonzero. Therefore the endpoint record does not determine the transported state. A path/history-sensitive degree of freedom is necessary. QED.

### Interpretation

This is the exact point at which the analogy

\[
\text{mixed interaction}\to\text{output channel}
\]

stops being enough. Fusion outcome and braid history are different information types.

---

## 10. Correspondence dictionary

| Anyon / fusion object | FCOA-Z candidate | Status |
|---|---|---|
| simple charge label `c` | terminal type `E_n^alpha` | exact finite label encoding at fixed `n` |
| fusion multiplicity support `N_ab^c != 0` | membership `E_n^alpha in Phi_n(a,b)` | exact for Ising support |
| `sigma x sigma = 1 + psi` | two-element fiber `{E_n^+,E_n^times}` | exact one-step support shadow |
| one mixed equal-radius pair | `(P_n^+,P_n^-)` | convenient interaction site, not physical anyon/anti-anyon claim |
| two allowed fusion channels | bundled outcomes of `oplus` and `otimes` | conservative but operation-tagged |
| fusion multiplicity `N_ab^c > 1` | repeated basis labels inside an output type | absent |
| intermediate fusion label | terminal `E` output | currently cannot re-enter |
| `F`-move | reassociation map between fusion trees | absent / LC2 required |
| `R`-symbol | channel-dependent exchange action | absent |
| braid word / homotopy class | transport-history state | absent |
| braid-group representation | action on an internal fusion space | absent |
| topological memory | persistent nonlocal/path-sensitive state | absent from current endpoint-only line |

The dictionary deliberately does **not** identify `+/-` branch sign with electric charge, particle/antiparticle, chirality, or topological charge.

---

## 11. Hostile audit of the tempting analogy

### Temptation 1

> `+ -` should automatically fuse to vacuum.

Rejected. Ising `sigma` is self-dual and `sigma x sigma` has both `1` and `psi` channels. More generally, a particle and its dual have a vacuum channel, but not necessarily only that channel.

### Temptation 2

> Multiple FCOA terminal symbols already mean quantum superposition.

Rejected. A set of labels is not a Hilbert-space superposition. Amplitudes, inner product, linear evolution, and coherent phase are extra structure.

### Temptation 3

> The two FCOA operation symbols are the two anyon fusion channels.

Too strong. The operation name externally selects the output in (24)-(25), whereas a fusion rule such as (11) presents both channels within one fusion product. The correct statement is only that the **bundled operation family** has the same two-channel support.

### Temptation 4

> Reflection of the line is braiding.

Rejected. Reflection is an involutive carrier automorphism. Braiding is represented by nontrivial paths in a multiparticle configuration space and, for non-Abelian anyons, by noncommuting operators on fusion spaces.

### Temptation 5

> Output fibers force an emergent second spatial dimension.

Rejected at this stage. The one-step channel support is `1D-CLOSED`; finite typed fibers can sit over the line without being coordinates. Braid topology does require more than strict line geometry, but that extra structure could be an abstract transport/history fiber rather than a literal second spatial coordinate.

---

## 12. Minimal next extension if SOL-TOPO continues

The next mathematically honest object is not a plane. It is an **enriched line with an internal fusion/transport fiber**.

A minimal candidate would add, for selected finite configurations `q`, a vector space

\[
H_q
\tag{48}
\]

whose basis is indexed by admissible fusion trees, together with partial transport generators

\[
\rho_q(b_i):H_q\to H_q
\tag{49}
\]

satisfying the braid relations

\[
\rho_q(b_i)\rho_q(b_{i+1})\rho_q(b_i)
=
\rho_q(b_{i+1})\rho_q(b_i)\rho_q(b_{i+1}),
\tag{50}
\]

\[
\rho_q(b_i)\rho_q(b_j)
=
\rho_q(b_j)\rho_q(b_i)
\qquad(|i-j|\ge2).
\tag{51}
\]

The crucial research question would then be whether `(48)-(51)` can be generated conservatively from LC2 output re-entry and mixed-sector rules, or whether they must be imposed as an independent new algebraic layer.

That question is genuinely stronger than the first-target fusion-channel correspondence.

---

## 13. Relation to the Line Completion Gate

### LC1 — Cell realization

For the specific equal-radius mixed cells used in `MC2`:

\[
\boxed{\texttt{REALIZABLE}}
\]

under the explicitly stated shared-fiber and uniform-rule assumptions.

No uniqueness claim is made: other mixed-sector rules remain possible.

### LC2 — Output re-entry

For full fusion-tree composition:

\[
\boxed{\texttt{OPEN / REQUIRED}}
\]

and Theorem 7.1 proves that the current terminal semantics is insufficient.

### LC3 — Mixed-sign realization

A conservative terminal-fiber realization exists via (24)-(25).

### One-dimensional closure

For one-step fusion-channel support:

\[
\boxed{\texttt{1D-CLOSED}.}
\tag{52}
\]

For genuine braid topology derived from carrier geometry:

\[
\boxed{\texttt{1D-OBSTRUCTED}.}
\tag{53}
\]

Equation (53) does **not** yet imply `DIMENSION-FORCING`, because an internal non-geometric transport representation could in principle be attached over the line.

---

## 14. Literature anchors

1. C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. Das Sarma, **Non-Abelian Anyons and Topological Quantum Computation**, *Reviews of Modern Physics* **80** (2008), 1083. DOI: `10.1103/RevModPhys.80.1083`.
2. J. Preskill, **Lecture Notes for Physics 219: Quantum Computation, Chapter 9 — Topological quantum computation**, sections on fusion spaces, `R`-matrices, `F`-matrices, and braid-group representations.
3. M. Stone, S.-B. Chung, **Fusion rules and vortices in p_x + i p_y superconductors**, arXiv:`cond-mat/0505515`; Ising-like fusion rules `psi x psi = 1`, `sigma x psi = sigma`, `sigma x sigma = 1 + psi`.
4. S. H. Simon, **Topological Quantum: Lecture Notes and Proto-Book** (2020 draft), chapters on Ising fusion and exchange; standard right-handed Ising values `R_1^{sigma sigma}=e^{-i pi/8}` and `R_psi^{sigma sigma}=e^{3i pi/8}`.
5. A. Kitaev, **Anyons in an exactly solved model and beyond**, *Annals of Physics* **321** (2006), 2–111. DOI: `10.1016/j.aop.2005.10.005`.

These sources establish the target-field structures used here. They do not validate any physical interpretation of FCOA-Z.

---

## 15. Publication recommendation

The SOL-TOPO first target is mathematically complete enough to keep as a citable internal research report, but **not yet strong enough for an independent Zenodo physics paper**.

Reason:

- the fusion-support embedding is exact but intentionally modest;
- the strict-line braid obstruction is rigorous but topologically classical;
- the potentially novel question is whether FCOA LC2/LC3 can *generate* a nontrivial internal `F/R` transport layer rather than merely host one after it is externally imposed.

Publication threshold for a standalone SOL-TOPO note should require at least one of:

1. a conservative LC2 re-entry theorem producing nontrivial fusion-tree composition;
2. a no-go theorem showing that any such re-entry forces a new independent memory layer;
3. a generated finite `F/R` toy system satisfying pentagon/hexagon or braid relations without hand-inserting the whole category.

Until then, the correct status is

\[
\boxed{\texttt{RESEARCH REPORT — KEEP IN BRANCH, DO NOT PUBLISH SEPARATELY YET}.}
\tag{54}
\]

---

## 16. Final conclusion

The useful part of the anyon analogy is not

\[
+-\Rightarrow\text{commutativity}.
\]

It is

\[
\boxed{
\text{interaction type}
\longrightarrow
\text{typed output-channel fiber}.
}
\tag{55}
\]

FCOA-Z already has enough terminal types to reproduce the support of the simplest non-Abelian fusion rule, and its mixed-sign freedom admits a conservative two-channel realization.

But fusion-channel memory and braid/path memory are categorically different. The current strict line can host the former as an internal fiber, while its geometry cannot generate the latter:

\[
\boxed{
\text{fusion-channel shadow: YES;}
\qquad
\text{non-Abelian braid memory from the line alone: NO.}
}
\tag{56}
\]

This is the first SOL-TOPO boundary.