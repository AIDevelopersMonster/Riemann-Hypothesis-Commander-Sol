# FCOA Hybrid Memory — Upstream Memo

**To:** main Commander Sol scientific director  
**From:** SOL-HYBRID scientific supervisor  
**Status:** internal checkpoint; candidate for hostile audit, not yet recommended for main-line adoption

## 1. Main result

A balanced hybrid-memory witness exists on the smallest possible active carrier of size three:

\[
\operatorname{Aut}(\oplus)\neq1,
\qquad
\operatorname{Aut}(\otimes)\neq1,
\qquad
\boxed{\operatorname{Aut}(\oplus,\otimes)=1.}
\]

Carrier size three is minimal. On two active points, every nontrivial automorphism group contains the unique transposition, so two nonrigid reducts cannot have trivial common stabilizer.

## 2. Three mechanisms all occur at the minimum

The branch has explicit three-point witnesses for:

1. **DD — domain-domain synergy:** one diagonal defined cell in each operation, at different carrier points. Each reduct has `C_2`; the joint domain reduct is rigid.
2. **DV — domain-value synergy:** one operation contributes a one-cell domain stabilizer; the second has maximally symmetric diagonal definedness `S_3` but a `1+2` anonymous value partition reducing it to a transverse `C_2`. The joint domain reduct remains nonrigid; restoring values makes the pair rigid.
3. **VV — value-value synergy:** both domains are the same maximally symmetric diagonal with definedness group `S_3`; two transverse `1+2` value partitions have individual `C_2` stabilizers with trivial intersection.

Thus genuine joint information appears strictly below the single-operation rigidity mechanisms G3-A/G4-A.

## 3. Structural interpretation

The correct first invariant is subgroup position, not automorphism-group size:

\[
\operatorname{Aut}(\oplus,\otimes)
=
\operatorname{Aut}(\oplus)
\cap
\operatorname{Aut}(\otimes)
\subseteq\operatorname{Sym}(X).
\]

Hybrid memory arises from **transverse residual symmetries**.

This abstract group-intersection identity is elementary; any publishable content would have to come from the FCOA-specific DD/DV/VV separation, minimal resource accounting, erasure tests, and leakage firewall rather than from the identity itself.

## 4. Arithmetic leakage

The three minimal witnesses are safely below the G4-A order wall:

- no directed path or total order is compiled;
- no successor, betweenness, EqGap, addition, or multiplication graph is present;
- no external rank calculations enter the operation laws;
- the phenomenon is finite hybrid rigidity, not a claim of uniform arithmetic interpretation.

Scalable path/value families exist, but they remain quarantined from upstream because uniform order/leakage behavior has not yet been hostile-audited.

## 5. Passport status

Completed in branch documents:

- exact operation tables/domains for DD-3, DV-3, VV-3;
- full and definedness automorphism groups;
- commutation loci;
- Association Spectra;
- translation-profile status;
- explicitly jointly recoverable singleton relations;
- automorphism proof that the target singleton is not recoverable from either reduct alone;
- carrier minimality for `n<3`;
- explicit `n=3` witnesses and scalable direct checks through `n=5`;
- Arithmetic Leakage audit.

## 6. What should be hostile-audited next

Before adoption, attack exactly these points:

1. the active-sort/output-sort automorphism convention and whether any one-sorted output mixing invalidates a claim;
2. the restricted minimality qualifiers for DV/VV (`maximally symmetric nonempty domain` template);
3. the definability formulas for the jointly recoverable singleton;
4. whether translation-profile injectivity statements are stated in the intended FCOA sense;
5. whether the scalable path family accidentally yields uniform AL0 order memory;
6. whether a still smaller DV or VV witness exists if the clean-template restrictions are dropped.

## 7. Recommendation

Do **not** merge this into the main mathematical line yet.

The branch has crossed the threshold for a dedicated hostile audit because the core existence/minimal-carrier result is clean and the three requested mechanisms are all represented. If that audit survives, I would recommend upstreaming the finite theorem package while keeping scalable families separate.
