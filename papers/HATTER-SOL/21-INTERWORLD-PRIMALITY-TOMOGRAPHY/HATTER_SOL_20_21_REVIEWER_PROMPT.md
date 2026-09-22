# HATTER-SOL 20–21 · INDEPENDENT REVIEWER PROMPT

Audit the manuscript as a skeptical reviewer in mathematical hardware /
computer arithmetic.

Do not attempt to strengthen the paper.  Attempt to falsify or narrow it.

## A. H20 semantic layer

1. Does the evidence actually prove DIRECT/BALANCED/LINEAR semantic equivalence
   for every declared width?
2. Is any synthesis difference being confused with an arithmetic difference?
3. Are memory resources compared fairly with logic resources?
4. Are finite-width observations accidentally stated asymptotically?

## B. H20 physical layer

1. Verify every Cyclone V number against the vendor reports.
2. Verify every Gowin number against the vendor reports.
3. Check whether the claimed crossover depends on the chosen vector metric.
4. Confirm that "backend-dependent crossover" is stated only for the measured
   widths and flows.
5. Confirm that DIRECT hard-memory mapping is presented as a resource-class
   observation rather than a universal compiler theorem.

## C. H21 theorem layer

1. Re-derive independently:
   \[
   x^n=C^{(n-1)/2}x
   \]
   from \(x^2=C\).
2. Verify the Jacobi substitution
   \[
   (D/n)=(C/n)
   \]
   for \(D=4C\), odd \(n\), under the stated coprimality assumptions.
3. Verify that the quadratic defect really has zero constant coordinate.
4. Verify factor-gcd semantic equivalence.
5. Identify any unstated exceptional cases.

## D. H21 RTL layer

1. Confirm that scalar and quadratic RTL use the same base modular multiplier.
2. Confirm that the compared controllers implement the declared semantics.
3. Recompute cycle means from raw vectors.
4. Check that generic cell counts are generated under the same Yosys flow.

## E. H21 Cyclone V layer

1. Confirm both designs FIT.
2. Verify ALM/register/DSP counts.
3. Verify TimeQuest Fmax values and corner.
4. Recompute:
   \[
   T=C/F_{\max}.
   \]
5. Recompute ALM-latency ratio.
6. Check whether incomplete external timing constraints invalidate only
   board-level claims or also the internal core comparison.

## F. Prior art

Specifically test whether the manuscript accidentally claims novelty for:

- Solovay-Strassen;
- Euler-Jacobi;
- Lucas/Frobenius tests;
- Jacobi hardware;
- hardware partial evaluation;
- specialization/constant propagation.

Search for prior work closer to:

> descriptor-driven exact arithmetic specialization of a polynomial/residue
> observer followed by matched FPGA validation.

If a direct analogue is found, report it and narrow the contribution.

## G. Final verdict requested

Return:

1. fatal errors;
2. major revisions;
3. minor revisions;
4. claims that are fully supported;
5. claims that must be weakened;
6. missing references;
7. reproducibility failures;
8. publication recommendation under the narrow architecture/compiler framing.

Do not grant novelty merely because no identical title is found.
