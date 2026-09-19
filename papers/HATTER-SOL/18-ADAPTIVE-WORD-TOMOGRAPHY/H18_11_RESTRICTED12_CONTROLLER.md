# HATTER-SOL-18 · H18-11
# Restricted 12-query adaptive controller: exact structural and microprogram cost

**Status:** CLOSED exact finite theorem/engineering layer.

## 1. Why H18-11 is needed

H18-10 proved that the full H18-06 one-erasure theorem does not require the
entire 50-query (W_4) pool.

A 12-query alphabet already preserves

[
D_0=4,qquad S_1=4,qquad A_1=5.
]

However, an information-theoretic alphabet reduction is not yet an
architectural reduction until the exact adaptive strategy is materialized
again under that restriction.

H18-11 therefore freezes the 12-query alphabet

[
oxed{
A, B, ABab, AbaB, ABB, Abb, AAb, AAAB, AAAb, Baa, aab, abb
}
]

and reconstructs the complete deterministic one-erasure controller from
scratch using only these labels.

## 2. Exact restricted strategy

Exact dynamic programming reconfirms:

[
oxed{D_0=4}
]

for the no-erasure identify-or-REJECT problem,

[
oxed{S_1=4}
]

under one persistent known query erasure, and therefore

[
oxed{A_1=5}.
]

The selected deterministic materialization contains

[
oxed{305}
]

nonterminal query nodes.

They split as

[
oxed{
67	ext{ pre-erasure}
+
238	ext{ post-erasure}.
}
]

For comparison, the earlier H18-07/H18-08 strategy had

[
308=69+239
]

query nodes.

Thus the query-alphabet restriction changes not only the descriptor table,
but also the decision program itself:

[
oxed{
308	o305.
}
]

This is a small but exact structural reduction.

## 3. All twelve labels are genuinely used

The selected 305-node strategy uses every label in the frozen alphabet.

Node-use counts are:

| Query | Nodes |
|---|---:|
| (A) | 76 |
| (B) | 64 |
| (ABab) | 37 |
| (AAb) | 33 |
| (ABB) | 32 |
| (Abb) | 26 |
| (aab) | 13 |
| (AbaB) | 11 |
| (AAAb) | 7 |
| (Baa) | 3 |
| (abb) | 2 |
| (AAAB) | 1 |

Therefore the 12-label alphabet is not merely a superset around a smaller
strategy produced by the deterministic tie-break. All twelve labels occur in
the selected exact program.

This does not prove that the alphabet is globally minimal; H18-10 still gives

[
9le M_1(W_4)le12.
]

## 4. Canonical node encoding

The restricted program has 305 query nodes.

Use the canonical encoding

[
0,ldots,304
]

for query nodes,

[
305+k,qquad0le k<114
]

for generating orbit terminals,

[
419=mathrm{REJECT},
qquad
420=mathrm{FAULT}.
]

There are only 421 used node codes, so a 9-bit program counter remains
sufficient.

Thus H18-11 does not change the basic 9-bit control-address width.

## 5. Explicit microprogram payload

With 12 supported query labels, the query selector needs only

[
lceillog_2 12ceil=4
]

bits per query node.

Therefore:

### Query selector

[
305	imes4
=
oxed{1220	ext{ bits}}.
]

### Six class transitions

Each of 305 query nodes stores six 9-bit successful-response targets:

[
305	imes6	imes9
=
oxed{16470	ext{ bits}}.
]

### Erasure transitions

Only the 67 pre-erasure nodes require legal erasure transitions:

[
67	imes9
=
oxed{603	ext{ bits}}.
]

### Word descriptors

Each of 12 words uses the same 11-bit descriptor convention as H18-08:

[
12	imes11
=
oxed{132	ext{ bits}}.
]

Hence the complete explicit representation is

[
1220+16470+603+132
=
oxed{18425	ext{ bits}}.
]

The H18-08 24-word program used

[
19057	ext{ bits}.
]

Therefore the exact representation reduction is

[
oxed{
19057-18425=632	ext{ bits}
}
]

or approximately

[
oxed{3.32%}.
]

This is a raw representation count before any FPGA-specific ROM/BRAM packing.

## 6. Why the percentage is modest

The query alphabet shrinks strongly:

[
24	o12,
]

but the dominant term is not the word descriptor table.

The dominant payload is the six-way transition table:

[
305	imes6	imes9=16470	ext{ bits}.
]

Therefore halving the query-label vocabulary cannot halve the complete
microprogram.

This identifies the next hardware bottleneck precisely:

[
oxed{
	ext{controller transition structure, not word descriptors}.
}
]

The major future gain must come from factoring or symmetry-compressing the
transition table, not merely shortening the word ROM.

## 7. Nielsen execution does not automatically reduce arithmetic

Ten of the twelve supported labels are primitive free-group words.

Each can be realized either:

1. directly as a word in (A,B); or
2. by an elementary Nielsen program that transforms the pair and then reads a
   coordinate class.

The certificate computes shortest elementary-Nielsen programs for these ten
labels.

Shortest Nielsen-move counts:

[
egin{array}{c|c}
	ext{word} & 	ext{shortest Nielsen moves}\
hline
A & 0\
B & 0\
ABB & 2\
Abb & 2\
AAb & 2\
Baa & 2\
aab & 3\
abb & 3\
AAAb & 3\
AAAB & 4
end{array}
]

Compare with direct execution after loading the first letter, where a word of
length (L) costs (L-1) permutation compositions.

For the ten primitive labels:

- six are tied;
- four require one more Nielsen move than direct word execution.

Thus:

[
oxed{
	ext{Nielsen semantic compression}

otRightarrow
	ext{automatic arithmetic compression}.
}
]

This is an important negative result.

Nielsen structure reduces and organizes the query language, but an FPGA
implementation must still compare concrete arithmetic schedules.

## 8. Architectural consequence

The first H18 hardware bottleneck was hardwired controller decode.

H18-08 replaced it by explicit microcode.

H18-11 shows that query-alphabet compression alone yields:

[
oxed{
308	o305	ext{ query nodes}
}
]

and

[
oxed{
19057	o18425	ext{ program bits}.
}
]

That is real but modest.

The next engineering target is therefore not simply

[
	ext{24 words}	o12	ext{ words},
]

but:

[
oxed{
	ext{factor the 6-way transition relation using Nielsen/Higman symmetry}.
}
]

Possible approaches include:

- component-relative node numbering by (	au)-sector;
- shared transition templates under Nielsen-equivalent candidate sets;
- canonical state-set representatives with a small transformation tag;
- mixed direct-word/Nielsen execution chosen by arithmetic cost.

## 9. Publication-safe interpretation

H18-11 proves a representation saving, not a target-FPGA area saving.

It is valid to claim:

- fewer globally supported query labels;
- fewer deterministic query nodes in the selected strategy;
- fewer explicit program bits;
- exact shortest Nielsen programs for the primitive labels.

It is not yet valid to claim:

- fewer LUTs/ALMs;
- fewer BRAM blocks;
- higher Fmax;
- lower physical latency;
- lower power.

Those require target-specific synthesis/place-and-route.

## 10. Certificate

Run:

```text
python certificates/h18_restricted12_controller_certificate.py
```

Expected terminal values include:

```text
query nodes = 305
pre-erasure nodes = 67
post-erasure nodes = 238
total explicit microprogram payload bits = 18425
PASS: restricted 12-query controller and representation certified
```

## 11. Theorem statement

### Restricted-alphabet controller theorem

For the H18 identify-or-REJECT problem on the 197 simultaneous-conjugacy
pair-orbits of (PSL(2,7)^2), the 12-query alphabet

[
A,B,ABab,AbaB,ABB,Abb,AAb,AAAB,AAAb,Baa,aab,abb
]

admits an exact adaptive strategy with

[
D_0=4,qquad S_1=4,qquad A_1=5.
]

Under the deterministic H18 strategy materialization used in this project,
the controller has exactly

[
305=67+238
]

nonterminal query states and admits an explicit 9-bit-address microprogram
representation of

[
oxed{18425	ext{ bits}}.
]

Moreover, shortest elementary Nielsen programs for the ten primitive labels
show that semantic Nielsen compression does not by itself reduce direct
per-query permutation-composition cost.
