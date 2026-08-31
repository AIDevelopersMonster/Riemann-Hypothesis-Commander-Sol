# Literature Positioning and Novelty Boundary

**Branch:** `research/prime-status-corridor`  
**Date:** 2026-08-29  
**Status:** preliminary-to-publication literature audit PASS

## 1. Classical components that must NOT be claimed as new

### 1.1 Prime support / radical coding

The use of the support

\[
\sigma(n)=\{p:p\mid n\}
\]

and radical/squarefree representatives is classical. Modern model-theoretic work on Skolem arithmetic explicitly treats radical elements as coding prime supports.

Relevant source:

A. Stonestrom, *Some model theory of Th(N,·)*, Mathematical Logic Quarterly 68 (2022), 288-303, DOI `10.1002/malq.202100049`.

The paper defines support, radical elements, squarefree representatives, and discusses their model-theoretic role.

### 1.2 Prime permutations in pure multiplication

The large symmetry obtained by permuting prime coordinates is standard background for pure multiplicative arithmetic. The present work should use this as motivation/background, not as a novelty claim.

### 1.3 WS1S / automata decidability

Decidability of weak monadic second-order logic of one successor is classical Buechi-Elgot-Trakhtenbrot theory.

### 1.4 Semenov criterion

The characterization of decidable MSO theories of recursive omega-words by a recursive indicator of recurrence is classical.

Modern accessible source:

D. Kuske, J. Liu, A. Moskvina, *Infinite and Bi-infinite Words with Decidable Monadic Theories*, Logical Methods in Computer Science 14(3:9), 2018.

### 1.5 Robinson definability

Julia Robinson proved in 1949 that addition and multiplication are first-order definable from successor and divisibility on the natural/positive integers.

Source:

J. Robinson, *Definability and decision problems in arithmetic*, Journal of Symbolic Logic 14 (1949), 98-114, DOI `10.2307/2266510`.

## 2. Candidate new combined construction

The specific quotient

\[
\Xi(n)=(\operatorname{supp}(n),Q(n)),
\qquad
Q(n)=1\iff \exists p\ p^2\mid n,
\]

with product

\[
(A,e)\star(B,d)
=
(A\cup B,e\vee d\vee[A\cap B\ne\varnothing])
\]

was not located as a standard named quotient in the initial literature search.

However the individual ingredients (support, squarefree/radical status) are classical. Therefore novelty should not be phrased as invention of support coding or squarefree detection.

The mathematically distinctive use is the quotient's combination of:

- exact preservation of prime/composite status;
- complete prime-coordinate symmetry;
- an internal finite-subset carrier;
- a controlled corridor of symmetry-breaking expansions.

## 3. Candidate novel theorem package

The current publication-worthy contribution is the **combined Prime-Status Corridor theorem package**, especially:

1. exact primehood in a quotient with full prime permutation symmetry;
2. finite periodic phase expansions that reduce symmetry but provably do not recover prime order/successor;
3. explicit nonperiodic block relations that further reduce symmetry without recovering order;
4. finite-injury examples showing that successor edge density tending to one does not imply successor definability;
5. effective mutual interpretation of the successor-enriched Prime-Status quotient with a weak monadic labelled word;
6. reduction of arithmetic residue alignment to the monadic theory of the consecutive-prime residue word;
7. the **Finite-Carrier Arithmetic Jump**: coordinate addition plus the internal finite-set carrier defines divisibility, then multiplication by Robinson, hence full arithmetic;
8. the **Maximal Recurrence Separation**: a computable binary word can contain every finite binary pattern infinitely often and still fail to define coordinate addition because its MSO theory remains decidable by Semenov's criterion;
9. the necessary condition for the actual mod-4 prime word: if it defines coordinate addition, its Semenov recurrence indicator cannot be recursive.

No exact prior theorem matching this full chain was found in the present search.

## 4. Novelty wording recommended for the manuscript

Do NOT claim:

- support/radical coding is new;
- squarefree elements as finite sets are new;
- prime permutations in `(N,×)` are new;
- WS1S, Semenov, or Robinson technology is new.

Do claim, subject to final bibliographic verification:

> We introduce and analyse a prime-status quotient that retains exact primality while erasing prime coordinates, and use it as a controlled definability corridor. The main new result is a finite-carrier arithmetic-jump mechanism: once coordinate addition on the prime-successor chain becomes definable, the quotient's internal finite-set carrier makes coordinate divisibility definable, after which classical Robinson definability yields full arithmetic. We further separate local pattern richness from arithmetic recovery by constructing a maximally recurrent computable binary phase word with decidable monadic theory and hence no definable coordinate addition.

This wording isolates the new combined mechanism from classical ingredients.

## 5. Priority-search verdict

**PASS for Zenodo/preprint scope, with conservative novelty wording.**

The search located close classical background but no direct prior work using the exact one-bit prime-status quotient as a definability corridor culminating in the finite-carrier arithmetic-jump and maximal-recurrence separation package.

Absence from search is not a proof of priority. The manuscript should say `to our knowledge` rather than make an absolute first-discovery claim.
