# H19-17 · Cross-Vendor Replication of the Measured Physical Quotient

Status: CLOSED CROSS-TECHNOLOGY PHYSICAL RESULT

For the frozen E0 family

\[
\mathcal F=\{D,P,N\}
=
\{DIRECT12,PREFIX19,NIELSEN12\},
\]

the Cyclone-V joint measured physical observer gives

\[
\mathcal P_{\rm CV}^{\rm joint}
=
\{\{D,P\},\{N\}\},
\]

and the independent Gowin GW5A-25A post-P&R joint measured observer gives

\[
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
\]

Therefore

\[
\boxed{
\mathcal P_{\rm CV}^{\rm joint}
=
\mathcal P_{\rm GW}^{\rm joint}
=
\{\{D,P\},\{N\}\}.
}
\]

At generic Yosys ABC-fast, total cells separate all three presentations:

\[
60374,\quad60383,\quad68406,
\]

hence

\[
\mathcal P_{\rm ABC}
=
\{\{D\},\{P\},\{N\}\}.
\]

The physical endpoints show observer-relative re-coarsening:

\[
\{\{D\},\{P\},\{N\}\}_{\rm ABC}
\to
\begin{cases}
\{\{D,P\},\{N\}\}_{\rm CycloneV},\\
\{\{D,P\},\{N\}\}_{\rm Gowin}.
\end{cases}
\]

This is a replicated finite experimental partition result. It does not assert routed-netlist identity, bitstream identity, complete physical-state equality, universal cross-technology invariance, or a technology-independent performance ordering.

Each physical laboratory includes a SHA-256 provenance manifest covering 33 key local run artifacts.
