# HATTER-SOL-21 · H21-LAB-10 RESULT

Status: **CI REPRODUCED / BROAD COMPILER HEURISTIC VALIDATED**

Run:

\`35694477935\`

## 1. Broad world families

Two canonical fundamental-discriminant families were scanned:

\[
|D|\le127
\]

with

\[
\boxed{78}
\]

fundamental worlds, of which

\[
\boxed{76}
\]

are non-torsion ranking worlds, and

\[
|D|\le255
\]

with

\[
\boxed{156}
\]

fundamental worlds, of which

\[
\boxed{154}
\]

are non-torsion ranking worlds.

The torsion controls

\[
D=-3,\qquad D=-4
\]

remained exactly silent:

\[
\boxed{Q=G=K=0}.
\]

## 2. Common-core control

To remove world-specific admissibility bias, the principal ranking uses only
semiprimes

\[
n=pq
\]

with

\[
p>D_{\max},\qquad q>D_{\max}.
\]

Thus every scanned world sees the same prime-pair population.

### |D| <= 127, bits=18

Common-core pairs:

\[
\boxed{6436}.
\]

Cheap Gini diversity versus exact factor exposure:

\[
\boxed{
\rho_S(G,Q)=0.983133
}
\]

and

\[
\boxed{
\rho_P(G,Q)=0.987664.
}
\]

Pairwise ranking inversions:

\[
\boxed{
137/2826
=
4.847841\%.
}
\]

Top-10 overlap:

\[
\boxed{7/10}.
\]

Mean relative coupling correction:

\[
\boxed{
\operatorname{mean}|K|/G
=
12.108046\%.
}
\]

Maximum observed:

\[
\boxed{
27.825687\%.
}
\]

### |D| <= 255, bits=18

Common-core pairs:

\[
\boxed{2162}.
\]

The broadest completed scan gives

\[
\boxed{
\rho_S(G,Q)=0.968066
}
\]

and

\[
\boxed{
\rho_P(G,Q)=0.965605.
}
\]

Pairwise ranking inversions:

\[
\boxed{
727/11462
=
6.342698\%.
}
\]

Top-10 overlap:

\[
\boxed{7/10}.
\]

Mean relative coupling:

\[
\boxed{
14.265519\%.
}
\]

Maximum observed:

\[
\boxed{
52.422520\%.
}
\]

Thus the cheap diversity score remains strongly predictive after expanding from
six hand-selected worlds to more than 150 canonical worlds, but it is not an
exact ranking law.

## 3. The six-world perfection does not survive

H21-LAB-09 found

\[
\rho_S=1
\]

on the original six worlds.

H21-LAB-10 finds explicit rank inversions in the broad families.

Therefore the statement

\[
\boxed{
G_{W_1}>G_{W_2}
\Longrightarrow
Q_{W_1}>Q_{W_2}
}
\]

is false in general on the tested finite families.

The correct exact relation remains

\[
\boxed{
Q_W=G_W+K_W.
}
\]

## 4. Compiler interpretation

The broad scan supports a genuine two-stage compiler.

### Stage 1 — cheap world pre-screen

Compute or estimate

\[
G_W.
\]

This removes clearly poor worlds and identifies a high-quality candidate set.

### Stage 2 — exact coupling refinement

Within the surviving candidate set, evaluate

\[
K_W
\]

or the equivalent pairwise zero-mask law.

Then rank by

\[
\boxed{
Q_W=G_W+K_W.
}
\]

This is now justified empirically across a much broader world family.

## 5. Top worlds are population-dependent

The exact top common-core world changes with the declared family/range.

For

\[
|D|\le127,\quad pq<2^{18},
\]

the leading world is

\[
\boxed{D=5}
\]

with

\[
Q\approx3.899938\%.
\]

For

\[
|D|\le255,\quad pq<2^{18},
\]

the leading world is

\[
\boxed{D=229}
\]

with

\[
Q\approx3.746531\%.
\]

Therefore H21 does not define a universal "best discriminant" independent of
the prime-pair population.

The world schedule is population- and objective-dependent.

## 6. Coupling is not a perturbative detail for every world

Although mean

\[
|K|/G
\]

is only around 12--14 percent in the principal scans, individual worlds reach

\[
\boxed{
|K|/G>50\%.
}
\]

Therefore there exist strongly coupling-dominated worlds for which one-direction
diversity alone is misleading.

This rules out compiling every world from a marginal descriptor only.

## 7. Hardware consequence

The FPGA scheduler should not hardwire a single static order derived from
discriminant magnitude or clock length.

The compiler should produce:

1. a rejected set: torsion/silent worlds;
2. a cheap candidate ranking from \(G_W\);
3. a refined shortlist ordered by \(Q_W\);
4. optional alternative schedules for different objectives:
   - compositeness certificate;
   - first factor;
   - two-factor exposure;
   - coverage of a declared input population.

## 8. Current strongest H21 architecture

The mathematical/hardware chain is now

\[
\boxed{
(B,C,\Delta)
\to
\text{torsion no-go}
\to
\text{Lucas local masks}
\to
G_W
\to
K_W
\to
Q_W
\to
\text{world schedule}
\to
\text{FPGA observer}.
}
\]

This is stronger than the original "try several quadratic worlds" concept
because every stage now has a defined mathematical role.

## 9. Publication status

\[
\boxed{\text{STILL NOT YET}}
\]

The broad scan validates the compiler heuristic, but a publication-quality
result still requires one of:

- an analytic bound on \(K_W\);
- a theorem relating marginal phase structure to \(Q_W\);
- an adaptive scheduling theorem;
- or a hardware theorem showing a nontrivial area/latency advantage from the
  compiled world schedule.

## 10. Next strike

The next theoretical target is the coupling term itself:

\[
\boxed{
K_W
=
Q_W-G_W.
}
\]

Specifically:

- classify when \(K_W=0\);
- derive sign criteria for \(K_W\);
- seek bounds on \(|K_W|\);
- identify arithmetic descriptors that predict coupling-dominated worlds.

That is now the narrowest path from the broad finite compiler result to a real
theorem.
