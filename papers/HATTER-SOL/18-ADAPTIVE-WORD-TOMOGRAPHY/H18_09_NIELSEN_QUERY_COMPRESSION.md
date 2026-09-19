# HATTER-SOL-18 · H18-09
# Nielsen-compressed interrogation: primitive observers plus one commutator type

**Status:** CLOSED exact finite theorem layer.

## 1. Motivation

H18-01 and H18-06 were solved over the full set of 50 distinct class-valued
queries induced by freely reduced words of length at most four.

That pool is mathematically convenient, but it hides a strong structural
redundancy.

A primitive word of the free group (F_2=langle A,Bangle) is an image of
one free generator under an automorphism of (F_2). Equivalently, its class
observer can be realized by first applying Nielsen moves to the generating
pair and then reading a coordinate-class observer.

Thus primitive-word queries are not 24 unrelated measuring devices. They are
one Nielsen-transported observer family.

The H18-09 question is:

[
oxed{
	ext{how much of the 50-query }W_4	ext{ pool is actually needed?}
}
]

## 2. Constructive primitive subset

Using elementary Nielsen moves

[
S:(A,B)mapsto(B,A),
]

[
I_A:(A,B)mapsto(A^{-1},B),
qquad
I_B:(A,B)mapsto(A,B^{-1}),
]

[
N_A^{pm}:(A,B)mapsto(AB^{pm1},B),
]

[
N_B^{pm}:(A,B)mapsto(A,BA^{pm1}),
]

the certificate constructs every canonical primitive query representative of
length at most four.

Exactly 24 of the 50 canonical W4 observers are primitive:

[
egin{aligned}
&A, B, a, b,\
&AB, Ab, Ba, ab,\
&AAB, AAb, ABB, Abb, BBa, Baa, aab, abb,\
&AAAB, AAAb, ABBB, Abbb, BBBa, Baaa, aaab, abbb.
end{aligned}
]

Hence these 24 observers form a single structural Nielsen family: each is a
coordinate observer after a suitable free-group automorphism.

## 3. Primitive observers alone almost identify the 114 generating states

Evaluate all 24 primitive observers on the 114 canonical H17 generating
orbits.

The resulting joint signature has

[
oxed{107}
]

distinct values.

Therefore only seven ambiguities remain, each a doublet.

Translated back to the canonical H17 orbit IDs, the unresolved pairs are

[
oxed{
(12,27), (13,28), (14,29), (84,89), (90,92), (100,103), (106,107).
}
]

These are exactly the seven H17 depth-(le4) defect pairs.

So the old H17 obstruction has a new structural interpretation:

[
oxed{
	ext{primitive/Nielsen observations fail on exactly seven commutator-sign pairs.}
}
]

## 4. The missing observer is the oriented commutator

Let

[
K=[A,B]=ABA^{-1}B^{-1}.
]

The projective class query for

[
	exttt{ABab}
]

takes values (7A) and (7B) on opposite members of every one of the seven
primitive collisions.

Thus the commutator class separates all seven unresolved pairs.

Its inverse orientation is represented by

[
	exttt{AbaB},
]

and the two class-response vectors differ only by inversion:

[
7Aleftrightarrow7B,
]

while (1A,2A,3A,4A) remain unchanged.

Therefore the natural H18 short-query architecture has two observer types:

[
oxed{
	ext{primitive Nielsen observer}
quad+quad
	ext{oriented commutator observer}.
}
]

At the canonical-query level this is the 26-query pool

[
oxed{
24	ext{ primitive}+2	ext{ commutator orientations}.
}
]

## 5. Exact adaptive complexity is unchanged

Restrict H18-06 from all 50 W4 queries to this 26-query Nielsen-normal pool.

Exact dynamic programming gives:

[
oxed{D_0=4}
]

for no-erasure identify-or-REJECT tomography.

Depth three remains impossible.

Under one persistent known query erasure:

[
oxed{S_1=4}
]

successful class answers still suffice, and therefore

[
oxed{A_1=5}
]

total attempts still suffice.

Thus the central H18 robust-adaptive theorem survives a nearly factor-two
reduction of the canonical query pool:

[
oxed{
50longrightarrow26
}
]

with no loss in worst-case adaptive depth.

## 6. Fixed/adaptive separation is also preserved

Inside the restricted 26-query pool, no fixed set of at most four queries
solves the full identify-or-REJECT problem.

The five-query witness

[
oxed{
A, B, AB, Ab, ABab
}
]

still works.

Hence the exact separation remains

[
oxed{
5_{m fixed}longrightarrow4_{m adaptive}.
}
]

So the fixed/adaptive theorem did not depend on the 24 discarded
non-Nielsen/noncommutator query types.

## 7. Price of the structural restriction

The restriction is not completely free.

On the 114 generating-state no-erasure problem, the unrestricted W4 optimum
has total path length

[
382
]

and mean depth

[
rac{191}{57}approx3.350877.
]

The Nielsen-normal 26-query pool has optimum total path length

[
oxed{386}
]

and therefore mean depth

[
oxed{
rac{386}{114}
=
rac{193}{57}
approx3.385965.
}
]

The worst-case depth stays exactly four, and the selected optimum still has
48 internal decision nodes rooted at

[
oxed{	exttt{AAB}}.
]

So the structural compression costs only four aggregate query steps over all
114 generating states.

This gives a clean Pareto trade:

[
oxed{
50	ext{ query labels}, 382	ext{ total path}
}
]

versus

[
oxed{
26	ext{ query labels}, 386	ext{ total path}.
}
]

## 8. Why this is a Nielsen theorem for H18 rather than only a finite pruning

The key identity is

[
q_w(alphacdot x)=q_{alpha(w)}(x)
]

up to the fixed action convention.

Therefore a primitive query (q_{alpha(A)}) can be realized in two dual ways:

1. keep ((A,B)) fixed and evaluate the word (alpha(A));
2. apply the Nielsen transformation (alpha) to the pair and read the class
   of the first coordinate.

So the 24 primitive query labels are not 24 independent algebraic mechanisms.
They are transport of one base observable along the Nielsen action.

The seven surviving doublets show exactly where this reduction stops:
primitive coordinate transport cannot recover the oriented commutator sign.

The commutator provides the missing second observer type.

Hence H18-09 identifies a structural normal form for the short-word
interrogation algebra:

[
oxed{
	ext{Nielsen coordinate transport}
+
	ext{commutator orientation}.
}
]

## 9. Hardware consequence

H18-07/H18-08 currently store a word selector and word descriptors for many
query labels.

H18-09 suggests a different controller encoding:

[
	ext{node}
longrightarrow
(	ext{Nielsen move program}, 	ext{observer type})
]

with only two semantic observer types:

- coordinate class;
- commutator class.

This does **not** yet prove a smaller FPGA implementation.

The new engineering target is exact:

[
oxed{
	ext{replace word-ROM diversity by Nielsen micro-operations and measure the cost.}
}
]

The comparison must include:

- microcode bits;
- permutation-composition count;
- controller states;
- ALM/LUT cost;
- BRAM/distributed-memory use;
- Fmax and transaction latency.

## 10. Relation to H18-03--H18-05

H18-03 identified the four Nielsen components through the Higman lift trace.

H18-05 showed that three special projective shadows reconstruct that invariant.

H18-09 adds a complementary statement:

> for exact orbit tomography, almost all short-word information can be
> generated by transporting a coordinate observer through Nielsen dynamics;
> the residual obstruction is precisely the oriented commutator sector already
> visible in H17.

Thus the adaptive and Nielsen sides of H18 are no longer merely adjacent.
They share one reduced observation architecture.

## 11. Certificate

Run:

```text
python certificates/h18_nielsen_query_compression_certificate.py
```

Expected terminal statement:

```text
PASS: Nielsen primitive + commutator normal form preserves H18 worst-case query bounds
```

## 12. Theorem statement

### Nielsen-normal interrogation theorem for the H18 PSL(2,7) laboratory

For the simultaneous-conjugacy quotient of ordered pairs in (PSL(2,7)^2),
consider class-valued word observers induced by freely reduced words of length
at most four.

There is a 26-query subfamily consisting of all 24 primitive canonical
observers together with the two oriented commutator observers such that:

1. its no-erasure identify-or-REJECT adaptive depth is exactly four;
2. under one persistent known query erasure, exactly four successful answers
   suffice and at most five attempts suffice;
3. its minimum fixed identify-or-REJECT size is five;
4. on generating states, the 24 primitive observers alone leave exactly the
   seven H17 commutator-defect doublets, all of which are separated by the
   oriented commutator class.

Consequently,

[
oxed{
50	ext{ canonical W4 queries}
longrightarrow
24	ext{ Nielsen-coordinate observers}
+
2	ext{ commutator orientations}
}
]

without changing the exact H18 worst-case adaptive observation complexity.
