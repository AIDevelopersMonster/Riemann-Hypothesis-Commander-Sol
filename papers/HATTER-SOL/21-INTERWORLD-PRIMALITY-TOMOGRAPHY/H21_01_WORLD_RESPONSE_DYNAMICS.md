# HATTER-SOL-21 · WORLD-RESPONSE DYNAMICS KERNEL

Status: **FOUNDATIONAL RESEARCH LAYER**

## 1. Fixed object, variable world

Let (n) be a fixed arithmetic object and let (mathcal W) be a declared
family of arithmetic worlds.

The primary H21 object is not a single predicate such as

[
operatorname{Prime}_{mathbb Z}(n),
]

but the world-response field

[
oxed{
mathcal R_n:mathcal W	omathcal S,
qquad
Wmapsto mathcal R_n(W).
}
]

The state space (mathcal S) depends on the observer.

Examples include:

- split / inert / ramified;
- Frobenius pass / fail / degenerate;
- number of prime-ideal factors;
- residue degree;
- decomposition type;
- non-Abelian conjugacy response;
- hardware observer output.

This continues the H09--H15 programme directly.

## 2. World change is not object change

A world transition

[
W_i	o W_j
]

does not replace (n).

It changes the ambient arithmetic in which (n) is interrogated.

Hence

[
mathcal R_n(W_i)
emathcal R_n(W_j)
]

is not a contradiction.

It is the central datum.

Example:

[
7	ext{ is inert in }mathbb Z[i]
]

but

[
7	ext{ splits in }mathbb Z[omega].
]

The number is fixed; the world response changes.

## 3. Observer trajectory

An observer does not normally inspect every world at once.

A finite observation protocol is a trajectory

[
oxed{
gamma=(W_0,O_0)	o(W_1,O_1)	ocdots	o(W_T,O_T),
}
]

where (W_t) is the arithmetic world and (O_t) is the observer used there.

The accumulated information after step (t) is

[
K_t
=
ig(
O_0(mathcal R_n(W_0)),
ldots,
O_t(mathcal R_n(W_t))
ig).
]

The knowledge filtration satisfies

[
K_0preceq K_1preceqcdotspreceq K_T.
]

This order is the mathematical content behind the informal phrase
"revelation time".

## 4. Revelation time

For a target property (P(n)), define the revelation time along a fixed
protocol (gamma) by

[
oxed{
	au_gamma(P,n)
=
min{t:K_t	ext{ certifies }P(n)}.
}
]

This is not physical time.

It is the first observation index at which the declared observer protocol has
enough information to certify the target property.

Different trajectories can have different revelation times for the same fixed
object:

[
	au_{gamma_1}(P,n)
e	au_{gamma_2}(P,n).
]

This is the quantity H21 can optimize.

## 5. Sequential arithmetic revelation on the number line

There is a second, independent ordering: increasing integer magnitude.

For odd integer exploration, each discovered prime (p) creates a future
composite-event axis

[
oxed{
C_p(k)=p^2+2pk,qquad kge0.
}
]

At any finite stage maintain a cursor (q_p) for each discovered prime.

The next composite event is

[
oxed{
c_{m next}=min_p q_p.
}
]

Every axis attaining that minimum advances by

[
q_pleftarrow q_p+2p.
]

If the next odd integer is not reached by any active axis, it is prime and
creates the new future axis

[
q_p=p^2.
]

Thus:

[
oxed{
	ext{composite}=	ext{realization of an already active future channel},
}
]

while

[
oxed{
	ext{prime}=	ext{creation of a new future channel}.
}
]

This is an event-driven reformulation of sieve dynamics, not a new primality
theorem.

## 6. Two independent coordinates

H21 therefore has two distinct coordinates:

### magnitude coordinate

[
n:0	oinfty;
]

### world coordinate

[
W_0	o W_1	o W_2	ocdots.
]

The natural combined research object is

[
oxed{
mathcal F(n,W)
}
]

together with observer paths through the ((n,W))-space.

The purpose is not to claim a new physical spacetime.

The purpose is to ask whether a nontrivial trajectory through world space can
certify an arithmetic property earlier or more cheaply than a fixed-world
observer.

## 7. Prime/composite as a world-response problem

For quadratic Frobenius worlds

[
A_{n;B,C}
=
(mathbb Z/nmathbb Z)[x]/(x^2-Bx-C),
]

prime inputs obey an exact Frobenius response law.

Composite inputs may imitate that law in one world and fail in another.

Hence H21-LAB-01 studies

[
oxed{
	ext{world sequence}
	o
	ext{shrinking composite survivor set}.
}
]

The experimentally measured quantity is therefore not merely pass/fail.

For an ordered world list

[
Gamma=(W_1,ldots,W_m),
]

define

[
S_0={	ext{declared composite inputs}},
]

[
S_j
=
{nin S_{j-1}:n	ext{ survives }W_j}.
]

Then

[
oxed{
|S_0|ge|S_1|gecdotsge|S_m|.
}
]

The sequence

[
(|S_0|,|S_1|,ldots,|S_m|)
]

is a finite tomography-efficiency profile.

## 8. H21-LAB-01 certified profile

For odd composites

[
3le n<2^{22},
]

the reproduced CI result is

[
|S_0|=1,801,205.
]

For the world

[
W_1:(B,C)=(1,-2),quadDelta=-7,
]

[
|S_1|=14.
]

For

[
W_2:(B,C)=(1,1),quadDelta=5,
]

[
oxed{|S_2|=0.}
]

Prime sanity failures:

[
oxed{0.}
]

This is an exact finite computational result in known Frobenius probable-prime
territory.

## 9. Central research question

The useful H21 question is now:

[
oxed{
	ext{Can we optimize an observer trajectory through arithmetic worlds}
atop
	ext{by information gained per mathematical/physical cost?}
}
]

For world (W) at state (S), define a finite information score, for example

[
G(Wmid S)
=
|S|-|Scapoperatorname{Survive}(W)|.
]

A hardware-aware policy can use

[
oxed{
eta(Wmid S)
=
rac{G(Wmid S)}
{operatorname{cost}(W)}.
}
]

The cost can mean CPU operations, FPGA cycles, area-time product, energy, or
another declared observer cost.

## 10. Non-claims

H21 does not claim:

- that arithmetic truth is created by observation;
- that revelation time is physical time;
- that Frobenius probable-prime theory is new;
- that a finite world list is a new deterministic primality theorem;
- any RH consequence.

The new research object is the **architecture of observation across worlds**.
