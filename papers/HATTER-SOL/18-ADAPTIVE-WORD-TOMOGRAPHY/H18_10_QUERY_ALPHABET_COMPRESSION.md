# HATTER-SOL-18 · H18-10
# Query-alphabet compression under one persistent erasure

**Status:** CLOSED exact finite theorem layer.

## 1. From transaction depth to global query vocabulary

H18-06 solved the per-transaction information problem:

[
oxed{S_1=4,qquad A_1=5.}
]

Four successful class answers suffice under one persistent known query erasure,
hence at most five total attempts suffice.

That result does not determine how many *different* query labels the machine
must support globally. H18-07/H18-08 materialize many different short words
because different branches use different observers.

H18-10 therefore introduces a second complexity parameter.

Let

[
M_1(mathcal W_4)
]

be the minimum cardinality of a fixed global query alphabet
(Qsubseteqmathcal W_4) such that an exact H18 identify-or-REJECT strategy
still exists with:

- at most one persistent known query erasure;
- exactly four successful class answers in the worst case;
- at most five total attempts.

The per-transaction optimum (S_1=4) and the global alphabet size (M_1) are
different notions.

## 2. A necessary distance-two condition

Suppose the machine supports a finite alphabet (Q).

If one supported query can disappear permanently, then after erasing any
single label the remaining supported responses must still separate:

1. every pair of distinct generating orbit states;
2. every generating state from every non-generating state.

Therefore every required state pair must be distinguished by at least two
query labels in (Q).

So any one-erasure-capable global alphabet must satisfy the exact necessary
condition

[
oxed{d_Qge2}
]

on the H18-06 identify-or-REJECT state relation.

This is only a necessary condition for the four-successful-answer adaptive
strategy, but it gives a powerful lower bound.

## 3. Seven critical pairs force both commutator orientations

Over the full set of 50 canonical (W_4) class-valued queries, there are
exactly seven required state pairs that are distinguished by only two query
labels.

Translated to the canonical H17 generating orbit IDs, these pairs are

[
oxed{
(12,27), (13,28), (14,29), (84,89), (90,92), (100,103), (106,107).
}
]

For every one of them, the only two separating canonical queries are

[
oxed{	exttt{ABab},qquad	exttt{AbaB}.}
]

These are the two oriented commutator observers.

Hence every distance-two global alphabet must contain both of them.

This strengthens the H18-09 interpretation: the commutator pair is not merely
a convenient augmentation of the primitive Nielsen family. Under the present
fault model it is **forced** by the seven critical pairs.

## 4. Exact lower bound: eight labels are impossible

Once (	exttt{ABab}) and (	exttt{AbaB}) are forced, a hypothetical
eight-label alphabet could contain only six further labels chosen from the
remaining 48 canonical queries.

The certificate exhausts all

[
inom{48}{6}
=
oxed{12,271,512}
]

possible completions.

For every completion, at least one required state pair has fewer than two
separating supported queries.

Therefore

[
oxed{	ext{no distance-two alphabet of size }8	ext{ exists}.}
]

Since a one-erasure adaptive alphabet must satisfy the distance-two condition,

[
oxed{M_1(mathcal W_4)ge9.}
]

This is an exact exhaustive lower bound.

## 5. Exact distance-two minimum is nine

A nine-query distance-two witness exists:

[
oxed{
a, b, Ba, ab, BBa, aab, aaab, ABab, AbaB.
}
]

It has distance at least two on every:

- generating/generating pair;
- generating/non-generating pair.

Together with the exhaustive size-eight impossibility this proves:

[
oxed{
	ext{minimum distance-two }W_4	ext{ alphabet size}=9.
}
]

This is a coding/admissibility statement. It does **not** yet prove that some
nine-query alphabet attains the H18-06 adaptive four-successful-answer bound.

## 6. A twelve-query adaptive witness

The certificate also identifies the following 12-label alphabet:

[
oxed{
A, B, ABab, AbaB, ABB, Abb, AAb, AAAB, AAAb, Baa, aab, abb.
}
]

Ten of these twelve words are primitive free-group words, hence
Nielsen-coordinate observers. The remaining two are the oriented commutator
pair.

On this restricted alphabet exact dynamic programming gives:

[
oxed{D_0=4}
]

for no-erasure identify-or-REJECT tomography, and

[
oxed{S_1=4}
]

under one persistent known query erasure.

Therefore

[
oxed{A_1=5}.
]

So the full H18-06 theorem survives after shrinking the globally supported
query vocabulary from

[
50
]

canonical (W_4) queries to only

[
oxed{12}.
]

## 7. Current exact bracket

Combining the lower and upper bounds:

[
oxed{
9le M_1(mathcal W_4)le12.
}
]

The lower bound is exact exhaustive distance-two impossibility below nine.

The upper bound is constructive and preserves the complete H18-06 adaptive
contract.

The remaining theorem problem is narrow:

[
oxed{
M_1(mathcal W_4)in{9,10,11,12}.
}
]

Determining the exact value is now a finite optimization problem over query
alphabets, not an open-ended search over decision trees.

## 8. Relation to H18-09

H18-09 proved that all worst-case H18 bounds survive in a 26-query
Nielsen-normal pool:

[
24	ext{ primitive}+2	ext{ commutator}.
]

H18-10 goes further.

It shows that the adaptive machine does not need all 24 primitive labels
globally. A 12-label alphabet suffices, with only ten primitive observers plus
the forced commutator pair.

Thus the compression sequence is now

[
oxed{
50
longrightarrow
26
longrightarrow
12
}
]

while preserving

[
oxed{
D_0=4,quad S_1=4,quad A_1=5.
}
]

## 9. Hardware implication

H18-08 stores a 24-word descriptor table because the selected hardwired
strategy uses 24 distinct word labels.

H18-10 proves that 24 labels are not information-theoretically necessary for
the same H18-06 contract.

A future controller may target the 12-query alphabet directly.

The most conservative immediate hardware saving is in query-description
storage. But a more important possibility is structural:

- ten supported labels are Nielsen-coordinate observers;
- two labels are commutator orientations.

This suggests a controller split into:

[
oxed{
	ext{Nielsen primitive path}
+
	ext{commutator path}.
}
]

Whether that reduces ALM/LUT/BRAM/Fmax cost is an engineering measurement, not
a theorem.

## 10. What is not yet proved

H18-10 does **not** claim:

- (M_1=9);
- that the nine-query distance-two witness supports the exact
  four-successful-answer adaptive strategy;
- that no 10- or 11-query adaptive alphabet exists;
- that a Nielsen-microcoded implementation is smaller or faster on FPGA;
- that the 12-query witness is unique.

The exact publication-safe claim is

[
oxed{9le M_1(mathcal W_4)le12.}
]

## 11. Certificate

Run:

```text
python certificates/h18_query_alphabet_compression_certificate.py
```

Expected conclusion:

```text
minimum distance-2 W4 alphabet size = 9
certified global alphabet bracket: 9 <= M1(W4) <= 12
PASS: exact H18 query-alphabet compression bounds certified
```

## 12. Theorem statement

### Query-alphabet compression theorem

For the H18 identify-or-REJECT problem on the simultaneous-conjugacy quotient
of (PSL(2,7)^2), with class-valued queries induced by freely reduced words of
length at most four and one persistent known query erasure, let
(M_1(mathcal W_4)) denote the minimum number of globally supported query
labels required while retaining the exact four-successful-answer adaptive
bound.

Then:

[
oxed{
9le M_1(mathcal W_4)le12.
}
]

The lower bound follows from an exhaustive distance-two argument: both
oriented commutator queries are forced by seven critical H17 pairs, and all
(inom{48}{6}=12,271,512) possible size-eight completions fail.

The upper bound is witnessed by the 12-query alphabet

[
A,B,ABab,AbaB,ABB,Abb,AAb,AAAB,AAAb,Baa,aab,abb,
]

for which exact dynamic programming certifies

[
D_0=4,qquad S_1=4,qquad A_1=5.
]
