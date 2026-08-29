# Zeckendorf Selective Additive Memory

**Project:** FCOA Admissibility Geometry  
**Status:** central theorem candidate; proof architecture complete, hostile audit required  
**Scope:** Presburger Compression Corridor after binary-history overshoot

## 1. Central question

The binary-history construction proved that subquadratic materialization is possible:

\[
\Theta(m\log m)\text{ stored BIT history}\Longrightarrow \operatorname{Add}/\operatorname{EqGap}.
\]

But BIT overshoots to finite full arithmetic.

The next target is therefore selective compression:

\[
\boxed{
\text{Find }o(m^2)\text{ generated memory from which Add is uniformly FO-definable,}
}
\]

while

\[
\boxed{
\text{Mul is not uniformly FO-definable.}
}
\]

This note gives a concrete candidate using canonical Zeckendorf/Fibonacci representations.

The essential new phenomenon is that the synchronous addition automaton for Fibonacci numeration is **aperiodic**. Hence addition is first-order readable from the digit incidence itself, while the entire finite-prefix family remains automata-decidable strongly enough to rule out uniform multiplication.

## 2. Carrier and Fibonacci digit incidence

Let

\[
G_m=\{g_0<g_1<\cdots<g_{m-1}\}
\]

be the recovered generic chain. Subscripts are external ranks only.

Use shifted Fibonacci weights

\[
F_0=1,\qquad F_1=2,\qquad F_{j+2}=F_{j+1}+F_j.
\]

Every nonnegative integer has a unique Zeckendorf representation

\[
n=\sum_j \varepsilon_jF_j,
\qquad
\varepsilon_j\in\{0,1\},
\qquad
\varepsilon_j\varepsilon_{j+1}=0.
\]

Define the binary incidence relation

\[
Z(x,p)
\]

on the active carrier by

\[
Z(g_n,g_{F_j})
\iff
\varepsilon_j(n)=1.
\]

The second coordinate is the **actual Fibonacci weight as a carrier point**, not its numerical digit index.

Define

\[
\operatorname{FibPos}(p):=Z(p,p).
\]

Then \(\operatorname{FibPos}(p)\) holds exactly on carrier points whose external rank is a Fibonacci weight. Indeed a number contains itself as a Zeckendorf summand iff it is itself one basis weight.

This makes the ordered digit-position set internally visible without adding a separate numerical index sort.

## 3. Generated rather than imported history

The relation \(Z\) need not be supplied as an external rank table.

Fibonacci numeration is a Pisot numeration system. Standard normalization results give a fixed finite automaton/transducer for normalization, hence for adding the constant one to a canonical representation and producing the next canonical representation.

Thus rows may be generated prefix-consistently:

\[
\operatorname{rep}_F(n)
\longmapsto
\operatorname{rep}_F(n+1)
\]

by one fixed finite-control normalization mechanism independent of the final carrier size \(m\).

Operationally:

1. start with the zero row;
2. apply the same finite-state successor/normalization transducer;
3. materialize the `1`-digit incidences of the new row;
4. never revise an earlier row.

No final-size predicate, rank oracle, addition table, multiplication table, or arbitrary size bit is queried.

Accordingly this is a generated-history candidate under the Uniformity Firewall. It is stronger than unary U1 because it uses a growing digit-position dimension.

## 4. Support is subquadratic

Let \(s_F(n)\) be the number of summands in the Zeckendorf representation of \(n\). Then

\[
|Z_m|
=
\sum_{0\le n<m}s_F(n).
\]

The trivial upper bound is

\[
s_F(n)=O(\log n),
\]

because the active Fibonacci weights grow exponentially. Therefore

\[
|Z_m|=O(m\log m)=o(m^2).
\]

More precisely, Lekkerkerker's theorem gives average summand count

\[
\frac{k}{\varphi^2+1}+O(1)
\]

on a Fibonacci block \([F_k,F_{k+1})\). Since \(F_k=\Theta(\varphi^k)\), block summation yields

\[
\boxed{|Z_m|=\Theta(m\log m).}
\]

A modern reference is M. Kologlu, G. Kopp, S. J. Miller, Y. Wang, *On the Number of Summands in Zeckendorf Decompositions*, Fibonacci Quarterly 49(2), 2011, 116-130, DOI 10.1080/00150517.2011.12428056.

Thus the memory has the same asymptotic support class as binary BIT history, but potentially different logical leakage.

## 5. A concrete Fibonacci addition automaton

Walnut contains the canonical most-significant-digit Fibonacci addition automaton

`Custom Bases/msd_fib_addition.txt`

in repository `firetto/Walnut`.

The file has seven listed states over alphabet

\[
\{0,1\}^3,
\]

one track for each of \(x,y,z\). Completing missing transitions with one rejecting sink gives an eight-state DFA.

Repository source blob SHA used in this audit:

`cf7be811768be7aa981b3a7a38a9688783ee98e5`.

This is the automaton Walnut uses for the relation

\[
x+y=z
\]

on canonical Fibonacci representations.

## 6. Aperiodicity certificate

A deterministic word language is star-free, equivalently FO[<]-definable on word positions, whenever its syntactic monoid is aperiodic. It is sufficient that the transition monoid of a recognizing DFA be aperiodic.

We independently enumerated the transition monoid of the completed Walnut Fibonacci-addition DFA.

Result:

\[
\boxed{|M|=83.}
\]

For every transition-monoid element \(t\), powers stabilize:

\[
\exists e\le4:\qquad t^e=t^{e+1}.
\]

Hence no element has a nontrivial group cycle and

\[
\boxed{M\text{ is aperiodic}.}
\]

Therefore the Fibonacci addition language recognized by this automaton is star-free and hence definable by one fixed first-order formula over the ordered digit positions with the three digit predicates.

Reproducibility script:

`experiments/fcoa-domain-compilation/verify_zeckendorf_adder_aperiodic.py`.

The script also performs finite semantic sanity checks against ordinary addition on canonical Zeckendorf representations.

The aperiodicity computation is exact for the supplied automaton; the semantic identity of that automaton with Fibonacci addition is the standard Walnut/numeration-system component and should still be attacked independently in hostile audit.

## 7. FO translation into the FCOA carrier

Let

\[
\psi_{\rm FibAdd}(X,Y,Z)
\]

be an FO[<] sentence over word positions defining the star-free synchronous addition language.

Translate its position variable \(q\) into a carrier variable satisfying

\[
\operatorname{FibPos}(q).
\]

Translate its three letter predicates by

\[
X_1(q)\rightsquigarrow Z(x,q),
\]

\[
Y_1(q)\rightsquigarrow Z(y,q),
\]

\[
Z_1(q)\rightsquigarrow Z(z,q).
\]

Use the reverse of the ambient order if the automaton is read most-significant digit first. Reversing a finite linear order is FO-trivial.

Leading zero padding is harmless: the Walnut automaton's initial state has a `000` self-loop.

Thus there is one fixed FCOA-side formula

\[
\operatorname{Add}_Z(x,y,z)
\]

obtained from \(\psi_{\rm FibAdd}\).

### Theorem candidate 7.1 — Zeckendorf Addition Recovery

For every finite carrier prefix,

\[
\boxed{
\operatorname{Add}_Z(g_a,g_b,g_c)
\iff
a+b=c<m.
}
\]

Hence EqGap is uniformly FO-definable as well, by the previously fixed Add/EqGap interdefinition.

The key difference from binary BIT is that the arithmetic relation is not obtained by exposing positional powers of two. It is obtained from an aperiodic normalization geometry on a non-positional recurrence basis.

## 8. The whole finite-prefix family is automata-decidable

The relation \(Z(x,p)\) is Fibonacci-recognizable.

Indeed, in synchronized canonical Fibonacci representations, `p is a basis weight used by x` is checked by a finite automaton:

- the representation of \(p\) has exactly one `1` and zeros elsewhere;
- at that same digit position the representation of \(x\) has `1`.

Order is also Fibonacci-recognizable, and Fibonacci/Pisot numeration admits automata for addition and normalization.

Consequently, for every fixed FO formula over

\[
(<,Z),
\]

the set of tuples satisfying it is effectively Fibonacci-recognizable.

The finite-prefix parameter can also be exposed. Given a sentence \(\theta\), relativize every quantified carrier variable by

\[
x<m.
\]

Then the set

\[
S_\theta=\{m:\mathfrak Z_m\models\theta\}
\]

is effectively recognizable by a finite automaton. In particular it is decidable whether

\[
S_\theta=\varnothing.
\]

This is the exact family-level decidability property needed below; it is stronger than merely saying that one infinite structure has decidable theory.

## 9. Uniform multiplication would decide Hilbert's tenth problem

We now obtain the selective-separation theorem.

Assume for contradiction that there is one fixed FO formula

\[
\mu(x,y,z)
\]

over \((<,Z)\) such that in every prefix

\[
\mathfrak Z_m
\]

it defines canonical truncated multiplication:

\[
\mu(g_a,g_b,g_c)
\iff
ab=c<m.
\]

Section 7 already supplies one fixed formula for truncated addition.

Take an arbitrary Diophantine equation over the natural numbers. Rewrite it as equality of two polynomials with nonnegative coefficients and introduce helper variables so that the computation uses only:

- zero;
- one;
- addition;
- multiplication;
- equality.

Zero and one are definable from the finite order as the least point and its successor.

Replace every addition gate by \(\operatorname{Add}_Z\) and every multiplication gate by \(\mu\). This yields an FO sentence

\[
\Theta_P
\]

over \((<,Z)\).

The original Diophantine equation has a solution in \(\mathbb N\) iff

\[
\exists m\;\mathfrak Z_m\models\Theta_P.
\]

Forward direction: choose \(m\) larger than all values appearing in one finite computation witness.

Reverse direction: every witness inside a prefix is, by the assumed exactness of the truncated operation formulas, a genuine natural-number solution.

But Section 8 gives an effective decision procedure for whether the prefix spectrum of \(\Theta_P\) is empty.

This would decide Hilbert's tenth problem over \(\mathbb N\), contradiction.

### Theorem candidate 9.1 — Selective Additive-Memory Separation

For the finite-prefix Zeckendorf incidence family,

\[
\boxed{
\operatorname{Add}/\operatorname{EqGap}\text{ is uniformly FO-definable}
}
\]

while

\[
\boxed{
\operatorname{Mul}\text{ is not uniformly FO-definable}.
}
\]

This is a **finite-family** separation, not merely an argument from the decidability of an infinite limit structure.

## 10. Presburger Compression Corridor is nonempty

Combining Sections 4, 7, and 9 gives exactly the sought witness:

\[
\boxed{
|Z_m|=\Theta(m\log m)=o(m^2),
}
\]

\[
\boxed{
Add,EqGap\in FO(<,Z),
}
\]

but

\[
\boxed{
Mul\notin FO(<,Z)
}
\]

uniformly across finite prefixes.

Therefore, subject to hostile audit of the automaton-to-FO bridge and the family decidability reduction,

\[
\boxed{
\textbf{the Presburger Compression Corridor is nonempty.}
}
\]

This is the first central candidate in the programme that simultaneously achieves:

1. generated rather than size-oracular memory;
2. subquadratic support;
3. full additive leakage;
4. no uniform multiplicative leakage.

## 11. Why Fibonacci succeeds where binary BIT fails

Both histories use \(\Theta(m\log m)\) incidences, so support alone does not distinguish them.

Binary BIT exposes a positional basis whose digit relation classically yields full finite arithmetic:

\[
FO(BIT)=FO(+,\times).
\]

The Zeckendorf incidence instead exposes a recurrence basis with a regular normalization system. The crucial observed property is that its specific three-track addition automaton is aperiodic, so addition can be read by FO from the digit history without requiring arbitrary automaton reachability.

At the same time the complete finite-prefix FO family remains automata-decidable, which blocks a uniform multiplication definition.

Thus the selective resource is not merely `digits`.

It is

\[
\boxed{
\text{an addable recurrence representation whose addition relation is FO/aperiodic,}
}
\]

while the representation family remains within an effective automata theory.

## 12. New resource axis: normalization complexity

The binary-vs-Fibonacci comparison reveals another axis missing from raw support cost:

\[
\boxed{
\text{normalization/transition-monoid complexity}.
}
\]

Two \(\Theta(m\log m)\)-support memories can sit at different arithmetic leakage levels because the algebra of their normalization mechanisms differs.

Candidate refined cost vector:

\[
C=(\text{support},\text{alphabet},\text{anchors},\text{generator class},\text{normalization monoid},\text{leakage}).
\]

The relevant finite-state distinction is not only number of states; aperiodicity versus group content matters.

## 13. FCOA interpretation

A typed FCOA compilation may materialize every positive digit incidence with one anonymous terminal output:

\[
x\star_Z p=\Omega_Z
\iff
Z(x,p).
\]

All other \(\star_Z\)-cells are UNDEF.

Then

\[
Z(x,p)\iff\operatorname{Def}(x\star_Z p),
\]

so the entire theorem transfers to a single constant-valued partial operation with domain support

\[
\Theta(m\log m).
\]

Thus, if the candidate survives audit, the corridor has a particularly clean FCOA realization:

\[
\boxed{
\text{one anonymous terminal value + }\Theta(m\log m)\text{ domain cells}
}
\]

already suffices for selective additive memory.

The arithmetic information is again in domain geometry rather than differentiated output values.

## 14. Hostile-audit targets

Before promotion to \(\mathbf F\), attack all of the following.

1. **Automaton semantics.** Independently verify that the exact Walnut file used here recognizes canonical Fibonacci addition for all inputs, not merely in finite tests.
2. **Aperiodicity implementation.** Recompute the completed transition monoid independently; verify sink completion and accepting states.
3. **Star-free bridge.** Check that transition-monoid aperiodicity is being used in the correct direction to obtain an FO[<] definition.
4. **Position realization.** Verify \(\operatorname{FibPos}(p)=Z(p,p)\) and the translation from word positions to carrier Fibonacci-weight points.
5. **Finite-prefix boundary.** Ensure missing Fibonacci positions above \(m\) cannot cause false truncated-addition witnesses.
6. **Recognizability of Z.** Build or exhibit the finite automaton recognizing the synchronous pair relation \(Z(x,p)\).
7. **Prefix-spectrum decidability.** Formalize the relativization by \(x<m\) and automata construction for the size parameter.
8. **Hilbert-10 reduction.** Verify helper variables and truncation never lose a genuine Diophantine witness when \(m\) is chosen sufficiently large.
9. **Generator firewall.** Exhibit a fixed successor/normalization transducer so the history is demonstrably generated rather than silently imported.
10. **Support asymptotics.** Check the passage from blockwise Lekkerkerker averages to arbitrary prefixes.

## 15. Status

The following points are already strongly supported:

\[
\boxed{
\mathbf F:\ |Z_m|=O(m\log m)=o(m^2).
}
\]

\[
\boxed{
\mathbf F:\ \text{the audited Walnut DFA has an 83-element aperiodic transition monoid.}
}
\]

\[
\boxed{
\mathbf F:\ \text{if the DFA is the exact Fibonacci adder, its accepted language is FO[<]-definable.}
}
\]

Central combined claim awaiting hostile audit:

\[
\boxed{
\mathbf W:\ \Theta(m\log m)\text{ Zeckendorf domain memory gives Add/EqGap but not Mul.}
}
\]

If the ten hostile-audit targets survive, promote to

\[
\boxed{
\mathbf F:\ \text{Presburger Compression Corridor is nonempty.}
}
\]

No numbered G5 family is opened yet.