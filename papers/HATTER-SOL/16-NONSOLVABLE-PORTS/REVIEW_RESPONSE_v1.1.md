# HATTER-SOL-16 · Response to external review · v1.1 correction gate

**Decision:** the review is accepted as a publication-blocking editorial audit. The current v1.0 package is not to be deposited as the final Zenodo version until the v1.1 patch below is integrated and re-rendered.

The review correctly distinguishes the hand-checkable algebraic core from the computer-assisted finite classification. Several criticisms concern exposition rather than a missing mathematical result: the underlying certificates already contain more detail than the short v1.0 manuscript exposes. The v1.1 goal is therefore to make the proof/evidence boundary explicit inside the publication.

## 1. Points accepted without qualification

The v1.1 manuscript shall:

1. define the normalized torus moments explicitly;
2. formalize the classwise Mahler ordering instead of using shorthand notation;
3. define the scalar determinant/Mahler type set used for the `7A/7B` collapse;
4. define precisely the depth-`<=4` trace-word candidate family and its quotient by trace symmetries;
5. expose the complete finite-search counts used for the five-probe minimality theorem;
6. expose the complete balanced-word counts used for the depth-14 theorem;
7. include a direct analytic sign lemma for the order-seven determinant phase;
8. add a reproducibility manifest tying every principal certificate to the release commit/blob/hash and expected terminal output;
9. make the exact-arithmetic / interval-arithmetic / floating-diagnostic distinction explicit;
10. recheck all DOI strings in the rendered EN/RU publication files.

## 2. Clarification: the Mahler observer is already defined, but the class notation is too compressed

The v1.0 manuscript already defines

\[
M_{A,B}(\mu)=\frac1{(2\pi)^2}\int_0^{2\pi}\!\int_0^{2\pi}
\log\det(\mu I-H_{A,B}(\theta,\phi))\,d\theta\,d\phi,
\qquad \mu\ge4.
\]

The review is nevertheless correct that notation such as

\[
M_{5A}(\mu)<M_{3A}(\mu)<M_{5B}(\mu)
\]

must be formalized because a commutator class can contain several determinant/Mahler types.

For v1.1 define

\[
\mathcal M_C(\mu)=
\{M_{A,B}(\mu):\langle A,B\rangle=A_5,\ [A,B]\in C\}.
\]

For two finite subsets of reals write \(X<Y\) when every element of \(X\) is strictly smaller than every element of \(Y\). The global theorem then becomes

\[
\boxed{
\mathcal M_{5A}(\mu)<\mathcal M_{3A}(\mu)<\mathcal M_{5B}(\mu)
\qquad(\mu\ge4).
}
\]

Equivalently,

\[
\sup\mathcal M_{5A}(\mu)<\inf\mathcal M_{3A}(\mu),
\qquad
\sup\mathcal M_{3A}(\mu)<\inf\mathcal M_{5B}(\mu).
\]

## 3. Explicit torus-moment definition

For every integer \(n\ge0\), define

\[
S_n(A,B)=\frac1{(2\pi)^2}
\int_0^{2\pi}\!\int_0^{2\pi}
\operatorname{Tr}\bigl(H_{A,B}(\theta,\phi)^n\bigr)
\,d\theta\,d\phi.
\]

Then the universal fourth-moment theorem is exactly

\[
\boxed{
S_4(A,B)=28d+4\operatorname{Tr}\rho(K)+4\operatorname{Tr}\rho(K^{-1}),
\qquad K=[A,B].
}
\]

The proof is the exact `28+4+4` balanced-word count already used in the theorem layer.

## 4. Local determinant coefficient in the 3D channels

For a three-dimensional determinant-one unitary representation,

\[
\det(I-t\rho(g))
=1-\chi(g)t+\chi(g^{-1})t^2-t^3.
\]

For the real icosahedral 3D representation of \(A_5\),
\(\chi(g^{-1})=\chi(g)\), hence

\[
P_g(t)=1-\chi_3(g)t+\chi_3(g)t^2-t^3.
\]

For the complex 3D representation of \(PSL(2,7)\), the coefficient of \(t^2\) must instead be written as \(\chi_3(g^{-1})=\overline{\chi_3(g)}\).

## 5. Scalar determinant/Mahler type in `PSL(2,7)`

For a generating pair \((A,B)\), let

\[
D_{A,B}(z,w;\mu)=\det(\mu I-H_{A,B}(z,w))
\]

be its exact Laurent determinant polynomial. At fixed \(\mu=4\), two such Laurent polynomials are declared scalar-Mahler equivalent if they are related by any composition of

\[
(z,w)\mapsto(z^{-1},w),\qquad
(z,w)\mapsto(z,w^{-1}),\qquad
(z,w)\mapsto(w,z),
\]

all of which preserve Haar measure on the torus and therefore preserve the scalar Mahler integral.

Let \(\mathcal T_C\) be the set of canonical equivalence types obtained from generating-pair orbits with commutator class \(C\). The exact certificate proves

\[
|\mathcal T_{3A}|=6,\qquad
|\mathcal T_{4A}|=12,\qquad
|\mathcal T_{7A}|=|\mathcal T_{7B}|=3,
\]

and

\[
\boxed{\mathcal T_{7A}=\mathcal T_{7B}}.
\]

This is the precise meaning of the orientation-even scalar collapse.

## 6. Direct sign lemma for the order-seven determinant phase

Put

\[
\alpha=\frac{-1+i\sqrt7}{2}.
\]

For \(K\in7A\),

\[
\chi_3(K)=\alpha,
\qquad
\chi_3(K^{-1})=\bar\alpha,
\]

so

\[
P_K(t)=\det(I-t\rho_3(K))
=1-\alpha t+\bar\alpha t^2-t^3.
\]

Therefore

\[
\operatorname{Im}P_K(t)
=-\frac{\sqrt7}{2}(t+t^2)<0
\qquad(0<t<1).
\]

For \(K\in7B\), the polynomial is the complex conjugate and

\[
\operatorname{Im}P_K(t)
=+\frac{\sqrt7}{2}(t+t^2)>0.
\]

Hence the determinant-phase sign separates `7A` and `7B` for every fixed real \(0<t<1\), with no numerical assumption. This should replace the former proof-sketch wording.

## 7. Exact depth-4 candidate family and five-probe minimality

The authoritative certificate is

`certificates/psl27_pair_tomography_short_word_certificate.py`.

Its convention is:

- alphabet `A,a,B,b`, with lowercase letters inverse to uppercase;
- freely reduced words;
- cyclic reduction;
- canonicalization modulo cyclic rotation and inversion of the whole word, exactly the symmetries of trace;
- all canonical nonempty words of exact length \(L\), accumulated through depth \(L\).

The complete unrestricted depth-`<=4` candidate family contains exactly

\[
\boxed{25}
\]

canonical trace words. The cumulative numbers of distinct signatures on the 114 generating-pair orbits are

\[
\boxed{24,107,107,114}
\]

at depths \(1,2,3,4\).

The five probes are encoded as

`A, B, AB, Ab, ABab`,

that is

\[
A,\quad B,\quad AB,\quad AB^{-1},\quad ABA^{-1}B^{-1}.
\]

They separate all 114 orbits. Exhaustive testing of every subfamily of sizes \(1,2,3,4\) of the complete 25-word family proves that no such subfamily separates all 114 orbits. Thus five probes are minimal **inside this explicitly defined depth-4 trace-word interface**; no absolute minimum over arbitrary observables is claimed.

## 8. Exact balanced-word family and depth 14

The same certificate enumerates canonical torus-balanced words, meaning

\[
\exp_A(w)=\exp_B(w)=0.
\]

At exact lengths

\[
4,6,8,10,12,14
\]

the newly appearing canonical word counts are

\[
\boxed{1,2,14,76,505,3386},
\]

for a cumulative total of

\[
\boxed{3984}
\]

through depth 14. The cumulative numbers of distinguished pair orbits are

\[
\boxed{4,22,98,110,112,114}.
\]

Hence depth 14 is necessary and sufficient in this balanced trace interface. The certificate also gives one explicit eight-probe balanced signature; sufficiency is certified, but cardinality eight is not claimed minimal.

## 9. Global `A5` Mahler proof should be exposed, not merely referenced

The authoritative compact-strip certificate is

`certificates/a5_global_mahler_mu_ge_4_certificate.py`.

It defines

\[
G(\mu)=M(\mu)-3\log\mu+\frac6{\mu^2}.
\]

Torus balancing kills odd moments, the exact second moment is \(S_2=12\), and Hermiticity gives \(S_{2m}\ge0\). Therefore

\[
G(\mu)
=-\sum_{m\ge2}\frac{S_{2m}}{2m\mu^{2m}},
\]

and

\[
\boxed{
G'(\mu)=\sum_{m\ge2}\frac{S_{2m}}{\mu^{2m+1}}\ge0.
}
\]

The certificate combines this analytic monotonicity with outward-rounded interval evaluation on 61 rational nodes of step \(1/100\), covering

\[
4\le\mu\le23/5,
\]

and joins it to the exact large-\(\mu\) theorem for \(\mu\ge23/5\). The v1.1 manuscript shall state this finite cover explicitly and point to the exact certificate.

## 10. Current Git evidence to be exposed in the release manifest

The following principal files are already present on the publication branch and have stable Git blob identifiers:

- `psl27_pair_tomography_short_word_certificate.py` — blob `a60113f99bc7a959bcbc6c9231d6b6c4893f8865`;
- `psl27_outer_orientation_minimal_observer_certificate.py` — blob `4e615ca2b5a7bb1d81961986c95f27e845e6d10f`;
- `psl27_generating_pair_and_scalar_collapse_certificate.py` — blob `6a0c4ae4bb28b84142b7989f156312107880a85f`;
- `a5_global_mahler_mu_ge_4_certificate.py` — blob `7887cf1ff164a21f8399d05bcaa688a1092a8098`.

The final publication ZIP shall additionally contain a SHA-256 manifest over the exact archived certificate bytes and a reproduction transcript. Git blob identifiers are not a substitute for that SHA-256 release manifest.

## 11. DOI review

The review reports truncated H08/H09 DOI strings in extracted text. The source bibliography used in the H16 assembly carries full DOI strings, so this may be a PDF text-extraction/line-breaking artefact rather than missing metadata. Nevertheless, the final v1.1 release must verify DOI strings both in source and in rendered/extracted PDF text before deposition.

## 12. Publication gate after review

The mathematical core does **not** require a new theorem strike before H16 can be published. The review exposes a presentation/reproducibility gap: several exact computer-assisted claims live primarily in certificates rather than in the article body.

The publication gate is therefore reset from `READY FOR ZENODO` to:

\[
\boxed{\text{READY AFTER v1.1 INTEGRATION + REPRODUCIBILITY AUDIT}}.
\]

Required final outputs:

- revised EN manuscript v1.1;
- revised RU manuscript v1.1;
- certificate/reproduction appendix;
- SHA-256 release manifest;
- rebuilt EN/RU PDF and DOCX;
- visual QA + PDF preflight;
- final DOI-text extraction audit.
