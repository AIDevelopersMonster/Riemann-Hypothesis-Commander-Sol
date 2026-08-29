# FCOA Hybrid Memory — Upstream Memo

**To:** main Commander Sol scientific director  
**From:** SOL-HYBRID scientific supervisor  
**Status:** Article A published; finite hybrid-memory core closed; resource-theory continuation remains active

## 1. Publication closure

The finite joint-memory programme has been publication-hardened and released as:

**Alex Malachevsky, “Reflections on Hybrid Memory with Commander Sol: Minimal Joint Rigidity of Partial Operations.”**

Zenodo DOI:

\[
\boxed{10.5281/zenodo.22165651}
\]

Article A is closed for new mathematical claims. Corrections, if ever necessary, must be explicit versioned errata rather than silent extensions.

## 2. Final finite theorem package

The published package establishes, with output semantics stated explicitly:

1. pure DD joint rigidity has sharp total cost `2` cells;
2. the typed/common-terminal Lift-Compatibility theorem identifies surviving carrier permutations with stabilizers of the global output-equality partition, with the non-surjective case handled by compatible lift sets;
3. typed common-terminal genuine value memory has sharp total cost `3` tagged cells (JFS-3);
4. the common-output active-carrier minimum is `n=2`, with sharp cost `4` cells at that carrier size;
5. independent-output DV has sharp cost `4=1+3`;
6. independent-output separately value-sensitive VV has sharp cost `6=3+3`;
7. unrestricted one-sorted hybrid rigidity has absolute total-cell minimum `2`;
8. the one-cell-per-operation strong one-sorted VV search gives no witnesses for `n=2,3`, and at `n=4` gives `24` labeled witnesses in `1` isomorphism class;
9. the typed three-active-point, three-cell JFS search gives `48` labeled witnesses in `8` operation-preserving isomorphism classes;
10. scalable Carrier-Value Selection gives the exact selector ladder
   \[
   S_{m+1}\to S_m\to\cdots\to S_2\to1.
   \]

The finite classifications are backed by the released exhaustive verifier.

## 3. Corrected mechanism taxonomy

The final finite theory separates:

- **carrier-stabilizer transversality**;
- **Joint Fiber Synchronization (JFS)** — incompatible lifts on a shared pure output sort;
- **Carrier-Value Selection (CVS)** — values are carrier points and select members of a residual carrier orbit.

The old global slogans “minimum active carrier = 3”, “all genuine value memory needs 3 cells”, and “VV minimum = 6” are false without their semantic qualifiers and must not be reused.

## 4. Publication boundary

Article A deliberately stops before arithmetic leakage. It does not claim that finite rigidity yields uniform order, addition, multiplication, or arithmetic interpretation.

The following results are post-Article-A material:

- fixed two-operation incidence compilation;
- rigidity without uniform order;
- bounded-degree order wall;
- sparse exact AL0;
- linear-cost AL1 and AL2 constructions;
- Resolution–Transport Profile (RTP);
- RTP interpretation no-go;
- semantic FO Transport Rank;
- restricted-interpretation resource theory.

These belong to Article B / subsequent work.

## 5. Major post-publication correction to the resource programme

The search for a superlinear cell wall through AL0–AL2 failed:

\[
\operatorname{Cost}(AL0)=\operatorname{Cost}(AL1)=\operatorname{Cost}(AL2)=\Theta(N)
\]

in the permissive auxiliary-carrier model.

A proposed normal-form profile `RTP=(rho,tau)` was then hostile-audited. It is **not** invariant under unrestricted FO interpretations. Two-digit base-`sqrt N` arithmetic realizes canonical multiplication with only linear memory and coordinate-resolution exponent `rho=1`, collapsing the direct-CRT `rho=2` presentation.

Thus presentation statistics and semantic interpretability must be separated.

## 6. Current invariant semantic object

Define benchmark families

\[
\mathsf B_0=([N],<),\qquad
\mathsf B_1=([N],<,+_{tr}),\qquad
\mathsf B_2=([N],<,+_{tr},\times_{tr}).
\]

The semantic **FO Transport Rank** is

\[
FTR(\mathcal C)=\max\{j:\mathsf B_j\le_{FO}\mathcal C\}.
\]

Because FO interpretations compose, FTR is monotone under FO interpretation and invariant under FO bi-interpretability.

However, FTR is a semantic phase label, not yet a quantitative resource lower bound.

## 7. Active next problem

The next genuine research problem is:

\[
\boxed{
\text{What is the weakest natural restriction on FO interpretations under which a nontrivial resource rank becomes invariant?}
}
\]

The leading candidate is a **size-faithful dimension-1 bounded-fiber interpretation** (or equivalent linear interpretation notion):

- forbid tuple-power digitization that turns a `sqrt N` base into `N` interpreted points for free;
- retain bounded-size incidence compilation and harmless definitional recodings;
- seek lower bounds that distinguish semantic transport levels while remaining stable under the allowed recodings.

## 8. Immediate research targets

1. formalize the admissible restricted-interpretation category;
2. prove composition closure;
3. define a quantitative resource preorder invariant under that category;
4. test whether AL0, AL1 and AL2 separate in it;
5. if they do not, construct the explicit collapse and tighten the category;
6. only after a genuine separation theorem, promote Article B to publication assembly.

This is now the active SOL-HYBRID research frontier.