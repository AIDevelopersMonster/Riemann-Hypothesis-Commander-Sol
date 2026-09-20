# H19-10 · Exact Adaptive/Spatialization Separation Family

Status: **THEOREM LAYER / CLOSED**

## 1. Purpose

H19 needs at least one parameterized family in which temporal adaptivity and
presentation-preserving spatial realization can be compared exactly.

The target is deliberately narrower than unrestricted Boolean circuit
complexity.

We prove an exponential separation for the canonical compiled-DAG discipline
(Pi_{m DAG}) of H19-01.

No claim is made that every Boolean circuit computing the same semantic
function requires exponential size in the parameter used below.

---

## 2. Address-selection task

Fix (nge1).

The input consists of

[
a=(a_1,ldots,a_n)in{0,1}^n
]

and a payload vector

[
x=(x_u)_{uin{0,1}^n}in{0,1}^{2^n}.
]

Define

[
oxed{
Phi_n(a,x)=x_a.
}
]

Thus the address chooses one of (2^n) payload bits.

This is the standard finite multiplexer/address-selection semantics. H19 does
not claim the task itself as new.

---

## 3. Observer vocabulary

Use address observers

[
A_i(a,x)=a_i,
qquad 1le ile n,
]

and payload observers

[
P_u(a,x)=x_u,
qquad uin{0,1}^n.
]

All observer outputs are one bit.

---

## 4. Canonical adaptive presentation (M_n)

Construct a complete binary decision tree.

At depth (j-1), after observing prefix

[
a_1cdots a_{j-1},
]

query (A_j).

After all (n) address bits are known, query the single selected payload
observer (P_a) and return its value.

Hence every transaction uses exactly

[
oxed{n+1}
]

observer queries.

The adaptive query depth is therefore

[
oxed{
D_{m query}(M_n)=n+1.
}
]

---

## 5. Residual-program structure

After (j) address bits have been observed, there are exactly

[
2^j
]

reachable address-prefix residual programmes.

Thus

[
oxed{
R_j(M_n)=2^j,
qquad
0le jle n.
}
]

At depth (n), the residual programmes are the (2^n) one-query payload
programmes

[
P_u	o x_u.
]

This gives an exact exponential residual-frontier growth law.

---

## 6. Source DAG counts

The address part of the adaptive decision tree contains

[
1+2+cdots+2^{n-1}
=
2^n-1
]

nonterminal address-query nodes.

The payload layer contains

[
2^n
]

distinct payload-query nodes.

Therefore the complete adaptive source tree has

[
oxed{
2^{n+1}-1
}
]

nonterminal query nodes if every payload query is represented explicitly.

Its temporal execution nevertheless visits only

[
oxed{n+1}
]

of them on any transaction.

This is the finite temporal/spatial tension that H19 seeks to isolate.

---

## 7. Canonical full spatial realization

Apply the H19-01 discipline (Pi_{m DAG}):

1. instantiate every distinct observer used by the presentation once;
2. make all observer values simultaneously available;
3. replace every address decision node by a 2-way selector over its two child
   results;
4. preserve the source DAG/tree sharing exactly;
5. forbid semantic flattening across the declared presentation boundary.

For the address-selection family:

- address observers instantiated:
  [
  n;
  ]
- payload observers instantiated:
  [
  2^n;
  ]
- binary selectors instantiated:
  [
  2^n-1.
  ]

Hence the exact generated structural count is

[
oxed{
N_{m gen}(n)
=
n+2^n+(2^n-1)
=
2^{n+1}+n-1
}
]

declared observer/selector instances, before the common shell.

If address-bit observers are treated as free input wires, the nontrivial
spatial presentation cost is still

[
oxed{
2^n+(2^n-1)=2^{n+1}-1.
}
]

---

## 8. Exact separation theorem

### Theorem H19-10.1

For the family (M_n),

[
D_{m query}(M_n)=n+1,
]

while under (Pi_{m DAG}) the presentation-preserving full spatial
realization contains exactly

[
2^n
]

payload observer instances and

[
2^n-1
]

binary selector instances.

Therefore

[
oxed{
N_{m spatial}(M_n)
=
2^{Theta(D_{m query}(M_n))}
}
]

for this compiler discipline.

More explicitly, since

[
D_{m query}=n+1,
]

[
oxed{
N_{m spatial}
=
2^{D_{m query}-1}
+
2^{D_{m query}-1}-1
=
2^{D_{m query}}-1
}
]

when address inputs themselves are not counted as observer hardware.

### Proof

The temporal depth statement follows directly from the construction: (n)
address queries followed by one selected payload query.

Under (Pi_{m DAG}), every distinct payload observer (P_u) used anywhere
in the source presentation is instantiated once. There are (2^n) such
observers.

The complete binary address decision tree has (2^n-1) internal nodes, and
(Pi_{m DAG}) assigns one binary selector to every such node.

Summing gives

[
2^n+(2^n-1)=2^{n+1}-1.
]

Substituting (n=D_{m query}-1) gives

[
2^{D_{m query}}-1.
]
(square)

---

## 9. Selector depth

If each binary selector has declared depth one and the payload observers have
depth (d_P), the generated combinational selector path has depth

[
oxed{
n+d_P
}
]

up to the fixed shell.

Thus this family separates **temporal query count from spatial size**, not
necessarily from spatial logic depth.

The exponential phenomenon is replication of mutually exclusive futures, not
an exponential critical-path depth.

---

## 10. Spatialization burden decomposition

For this family, H19-01's decomposition becomes exact.

Observer burden:

[
oxed{
S_{m obs}(M_n)
=
n,S(A)
+
2^n S(P).
}
]

Future-materialization burden:

[
oxed{
S_{m future}(M_n)
=
(2^n-1)S_{m sel}(2,1).
}
]

Therefore both the simultaneous observer vocabulary and the materialized future
tree grow exponentially in temporal depth.

This gives a clean calibration family for interpreting H18/H19 finite FPGA
experiments.

---

## 11. Relation to unrestricted Boolean circuits

The semantic function (Phi_n) is the ordinary (2^n)-to-1 multiplexer.

The theorem above is **not** an unrestricted lower bound for arbitrary circuits
computing (Phi_n).

In particular:

- the total semantic input already contains (2^n) payload bits;
- a conventional multiplexer circuit is itself (O(2^n)) in ordinary gate
  size;
- H19 does not prove optimality over all Boolean encodings, all circuit bases,
  or all synthesis transformations.

The exact theorem is instead:

[
oxed{
	ext{within }Pi_{m DAG},
quad
	ext{temporal query depth }n+1
	ext{ coexists with exact spatial presentation size }2^{n+1}-1.
}
]

This is a compiler-discipline theorem.

---

## 12. Why the family matters for H18/H19

The H18 restricted-12 controller is finite and irregular. It shows the effect
experimentally but does not by itself expose an asymptotic law.

The address-selection family isolates the mechanism:

[
oxed{
	ext{temporal branch selection}
quadlongleftrightarrowquad
	ext{spatial coexistence of all possible futures}.
}
]

That mechanism is exactly what H18-LAB-03 versus H18-LAB-04 displayed on a
finite FPGA instance.

H19-10 provides the parameterized construction-level theorem behind that
interpretation.

---

## 13. Presentation-preserving lower-bound wording

Within the explicitly frozen discipline (Pi_{m DAG}), the counts are exact
by construction. Therefore one may state a presentation-preserving lower bound:

[
oxed{
N_{Pi_{m DAG}}(M_n)ge 2^{n+1}-1
}
]

for the declared payload-observer plus selector instance measure, with equality
for the canonical construction.

This lower bound is **not** promoted to unrestricted Boolean circuit size.

---

## 14. Publication consequence

H19's publication threshold required at least one of:

- a nontrivial temporal/spatial structural theorem;
- a provable separation family;
- a rigorously defined predictive invariant.

H19-09 supplies the first rigorous compiler-observability theorem layer.

H19-10 supplies an exact parameterized temporal/spatial separation family under
the declared presentation-preserving discipline.

Therefore the theoretical threshold is now crossed **in substance**, subject to
hostile novelty/prior-art audit and manuscript-level claim tightening.

---

## 15. Next strike

Do not search immediately for a stronger unrestricted lower bound.

The next research step should be to connect the finite H18/H19 measurements to
the exact H19-10 quantities:

[
R_t(M),
qquad
S_{m obs}(M),
qquad
S_{m future}(M),
qquad
partialmathcal V_i.
]

The concrete question is:

[
oxed{
	ext{Which of these source quantities best predicts physical
presentation-survival across controlled E0-equivalent families?}
}
]
