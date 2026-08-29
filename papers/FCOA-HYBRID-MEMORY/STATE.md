# State checkpoint — FCOA Hybrid Memory Article A

**Status:** REVIEWED_CLEAN — Zenodo DOI reservation and final rebuild pending.

## Fixed mathematical results

1. Pure DD: two total cells are necessary and sufficient for balanced domain-only joint rigidity.
2. Typed/common-terminal Lift-Compatibility:
   \[
   Aut(X,O;\star_1,\ldots,\star_k)\cong Stab_{\Gamma_D}(\equiv_c)
   \]
   under global output surjectivity; the active projection in the non-surjective case is governed by the intersection of lift sets.
3. Typed common-terminal value effect: at least three tagged cells; JFS-3 is sharp.
4. Common-output active carrier minimum: n=2; at n=2 the sharp cell cost is four.
5. Independent outputs: sharp DV cost 4 and separately value-sensitive VV cost 6, under the stated semantics.
6. Unrestricted one-sorted binary partial operations: absolute hybrid cell minimum 2, attained by
   \[
   a\star a=u,\qquad a\diamond a=v
   \]
   on four points.
7. Strong one-sorted one-cell-per-operation VV search:
   - n=2: 0;
   - n=3: 0;
   - n=4: 24 labeled, 1 isomorphism class.
8. Typed three-active-point, three-tagged-cell JFS search: 48 labeled, 8 operation-preserving isomorphism classes.
9. CVS selector ladder: after restoring r of m values, the exact residual group is
   \[
   S_{m+1-r}.
   \]

## Repaired historical claims

- “Minimum active carrier is 3” is false in the common-output typed regime; n=2 is possible with four cells.
- “Every genuine value-induced hybrid effect needs at least 3 cells” is false without the separated terminal-output assumption; unrestricted one-sorted CVS needs only 2.
- “VV minimum = 6” is only an independent-output / separately value-sensitive statement, not an absolute one-sorted statement.
- JFS and CVS are different mechanisms and must not be conflated.

## Publication boundary

Article A ends with the finite hybrid-memory theory and scalable CVS ladder. Arithmetic leakage/resource-cost research is not part of the release.

## Next action

Reserve Zenodo DOI, insert it into both language sources and metadata, rebuild, rerender, checksum, then mark `PUBLICATION_READY`.