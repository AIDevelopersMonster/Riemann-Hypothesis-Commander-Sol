# Literature Audit — Prime-Only Carrier Elimination and Saturated WMSO Classification

**Project:** Prime-Successor Algebra / beyond the Support-Cardinality Wall  
**Branch:** `research/finite-subset-carrier-wall`  
**Date:** 2026-08-29  
**Purpose:** claim delimitation before publication assembly

## 1. Result under audit

The branch proves, for a canonical saturated family of prime-only residual structures built from the Ramanujan-Delta bridge, an exact decidability equivalence

\[
\operatorname{Th}(\mathcal I_{\kappa_G})\text{ decidable}
\iff
\operatorname{WMSO}(G)\text{ decidable},
\]

where \(G\) is the definable active skeleton of the profile and every finite active neighborhood occurs with countably infinite external multiplicity.

The branch also proves that arbitrary prime-only profiles have a locally finite normal form determined up to isomorphism by the pair

\[
(G_\kappa,\mu_\kappa),
\]

consisting of the active skeleton and the multiplicity spectrum of external finite active neighborhoods.

## 2. Classical WMSO background

Weak monadic second-order logic quantifies over finite subsets. The decidability of the weak monadic theory of successor/natural order goes back to the automata-theoretic work of J. R. Büchi and C. C. Elgot.

Relevant classical references:

- J. R. Büchi, *Weak Second-Order Arithmetic and Finite Automata*, Zeitschrift für Mathematische Logik und Grundlagen der Mathematik / Mathematical Logic Quarterly 6 (1960), 66-92. DOI 10.1002/malq.19600060105.
- C. C. Elgot, *Decision Problems of Finite Automata Design and Related Arithmetics*, Transactions of the American Mathematical Society 98 (1961), 21-51.

Therefore the use of WMSO as the target logic is not itself novel and must not be presented as such.

## 3. Finite-set interpretations

A directly relevant modern framework is:

Thomas Colcombet and Christof Löding, *Transforming structures by set interpretations*, Logical Methods in Computer Science 3(2:4) (2007), DOI 10.2168/LMCS-3(2:4)2007, arXiv:cs/0703039.

They introduce finite-set interpretations defined by WMSO formulas with finite-set variables and explicitly note the basic transfer principle:

> structures obtained by finite-set interpretations from structures of decidable WMSO theory have decidable first-order theory.

Their framework therefore subsumes the **upper-direction logical mechanism** used in the saturated classification: once the saturated prime-only normal form is represented by active vertices together with finite subsets and a pure copy coordinate, decidability transfer from WMSO to FO is part of a known finite-set interpretation paradigm.

Accordingly, publication must not claim novelty for the abstract fact that finite-set interpretations preserve decidability in this direction.

## 4. What remains specific to the present branch

The targeted search did not locate a result combining all of the following ingredients:

1. a Ramanujan-Delta residual incidence relation
   \[
   r^{\kappa(r)}\mid \tau(p)^2-p^{11};
   \]
2. deletion of the multiplicative source sort and of the explicit finite-set carrier;
3. parameter-free recovery of the positive-depth support inside the prime-only residual reduct;
4. the locally finite normal form of that reduct;
5. arithmetic programming of an arbitrary countable backward DAG as the active skeleton by adelic independence plus Chebotarev and finite divisor avoidance;
6. simultaneous arithmetic saturation of every finite active neighborhood with infinitely many external prime realizers;
7. the resulting exact two-way WMSO decidability equivalence for the saturated arithmetic family;
8. the skeleton-plus-multiplicity isomorphism invariant for the arbitrary prime-only normal form.

This is the appropriate candidate novelty package. The novelty claim should be phrased as a construction/result **within this Ramanujan residual family**, not as a new general theorem about WMSO or finite-set interpretations.

## 5. Number-theoretic input

The residual programming mechanism uses David Loeffler's adelic open-image theorem for non-CM modular forms:

David Loeffler, *Images of adelic Galois representations for modular forms*, Glasgow Mathematical Journal 59 (2017), 11-25, DOI 10.1017/S0017089516000367, arXiv:1411.1789.

Loeffler proves openness of the adelic image in the appropriate algebraic group. The preceding Support-Cardinality work specialized this to the Ramanujan form \(\Delta\), passed to the cyclotomic kernel, and extracted simultaneous control of full \(\operatorname{SL}_2\)-factors outside finitely many primes.

The present branch does not strengthen Loeffler's theorem; it uses the already-established finite residual pattern theorem as an input.

## 6. Nearby contemporary Ramanujan-tau undecidability work

A distinct 2026 line is:

Toghrul Karimov, Joris Nieuwveld, and Joël Ouaknine, *Rich sequences and decidability of logical theories* (submitted, 2026).

Their stated Ramanujan application proves undecidability for a structure involving

\[
n\mapsto |\tau(n)|
\]

using richness/quasi-randomness ideas. This differs from the present language and mechanism:

- their universe/function language is different;
- the present work uses valuation-threshold residual incidences;
- the present arithmetic engine is adelic independence plus Chebotarev;
- the prime-only branch studies what remains after removing source arithmetic and finite-set carrier memory.

The two results are therefore nearby in subject matter but should not be conflated.

## 7. Claims that should NOT be made

The publication should not claim:

- a new proof of Büchi-Elgot decidability;
- novelty of finite-set interpretations or the weak powerset construction;
- that every prime-only infinite-support profile is classified by WMSO of its skeleton;
- that the active skeleton alone determines an arbitrary prime-only structure;
- a full elementary-equivalence classification for arbitrary multiplicity spectra;
- historical priority over all model-theoretic uses of finite-neighborhood structures;
- that the targeted web literature search replaces MathSciNet/zbMATH review for journal priority.

## 8. Safe publication-positioning statement

A publication-safe statement is:

> The logical transfer through finite subsets is classical and closely related to finite-set interpretations in weak monadic second-order logic. The contribution here is the arithmetic realization and elimination phenomenon: after deleting both source multiplication and an explicit finite-set carrier from a Ramanujan-Delta valuation structure, the remaining prime-only reduct parameter-free recovers its positive support, admits a locally finite incidence normal form, and can arithmetically realize saturated active skeletons for which first-order decidability is equivalent to WMSO decidability of the skeleton.

## 9. Audit verdict

The literature search found strong prior art for the **logical technology** but no exact match for the **Ramanujan residual carrier-elimination + skeleton-programming + saturated WMSO classification package**.

This supports publication as a distinct sequel provided the manuscript explicitly credits Büchi/Elgot and Colcombet-Löding and presents the finite-set/WMSO transfer as background rather than novelty.

**Literature-audit verdict: PASS for Zenodo/preprint positioning; journal-level historical-priority claims remain intentionally unmade.**
