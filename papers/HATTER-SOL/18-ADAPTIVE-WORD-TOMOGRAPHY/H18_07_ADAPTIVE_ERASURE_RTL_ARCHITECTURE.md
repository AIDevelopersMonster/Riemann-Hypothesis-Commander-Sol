# HATTER-SOL-18 · H18-07
# Adaptive erasure controller: hardware handoff and structural cost

**Status:** architecture/generator layer CLOSED; independent RTL regression and generic synthesis remain validation gates.

## 1. Exact decision program materialized

The H18-06 recurrence has now been materialized into a deterministic finite controller.

The selected strategy contains

\[
\boxed{308}
\]

nonterminal controller states:

\[
\boxed{69\text{ pre-erasure}+239\text{ post-erasure}.}
\]

It uses only

\[
\boxed{24}
\]

distinct word labels from the 50-query \(W_4\) pool.

Maximum word length remains

\[
\boxed{4}.
\]

The machine-readable generator emits:

- controller ROM RTL;
- compact word microcode ROM;
- JSON representation;
- 1182 frozen representative/fault vectors.

## 2. Exact path-cost metrics

For the selected deterministic strategy:

\[
\boxed{\text{worst attempts}=5},
\]

\[
\boxed{\text{worst successful class answers}=4},
\]

\[
\boxed{\text{worst naive letter-compositions}=19}.
\]

Without erasure:

\[
\boxed{\text{worst attempts}=4},
\]

\[
\boxed{\text{worst naive letter-compositions}=15}.
\]

These are exact properties of the generated strategy.

## 3. Comparison with H17 LAB-03

H17 LAB-03 has:

\[
14
\]

shared DAG composition operations and

\[
8
\]

class captures, followed by its ROM-free repair network.

H18's simple reference engine deliberately does not yet share prefixes across different adaptive queries. In the worst one-erasure path it may execute

\[
19
\]

letter-compositions but only

\[
5
\]

class captures.

So adaptivity trades

\[
\boxed{\text{fewer expensive observations}}
\]

for

\[
\boxed{\text{more control and potentially more repeated word arithmetic}}.
\]

This is exactly the engineering trade-off H18 was meant to expose.

## 4. The 308-versus-306 coincidence

The selected H18 controller has 308 nonterminal states.

The H17 ROM-free known-erasure repair layer has 306 internal decision nodes.

Thus, at the level of raw decision-structure counts:

\[
\boxed{308\approx306}.
\]

This is intriguing but not a hardware-area theorem. The nodes have different fan-in, fan-out, data widths and synthesis structure.

Only a common Yosys/FPGA synthesis can decide whether the apparent combinatorial similarity survives technology mapping.

## 5. First sequential RTL architecture

The reference architecture is:

\[
(A,B)
\to
\text{membership}
\to
\text{controller}
\to
\text{word microcode}
\to
\text{one composition datapath}
\to
\text{one class engine}
\to
\text{branch}.
\]

The same class engine is reused for every adaptive query.

One injected erasure is selected by attempted-query number. This is a laboratory fault-injection port, not a claim about a physical sensor.

## 6. Latency observation before RTL measurement

The simple non-caching engine has at most

\[
19+5
\]

word-composition plus classification stages on a one-erasure path.

With raw membership/check and terminal control, this naturally lands near a 26-cycle reference schedule.

H17 LAB-03 also measured 26 cycles in its frozen RTL.

This equality is currently only an **architectural count**, not an H18 simulator measurement. It should be treated as a testable prediction.

If independent RTL regression confirms it, the comparison becomes especially clean:

\[
\text{same order of sequential latency},
\]

but with radically different internal work:

\[
\begin{array}{c|c|c}
 & H17\text{ LAB-03} & H18\text{ adaptive}\\
\hline
\text{composition work} & 14\text{ DAG ops} & \le19\text{ naive letter ops}\\
\text{class observations} & 8 & \le5\\
\text{repair/controller} & 306\text{-node repair} & 308\text{-state controller}
\end{array}
\]

## 7. Next optimization target

The adaptive path repeatedly asks words with shared prefixes such as

\[
A,\ AB,\ AAB,\ AAAB,\ldots
\]

The obvious H18-08 problem is therefore:

\[
\boxed{
\text{adaptive prefix cache / online word DAG}
}
\]

to reduce the worst 19 composition operations without destroying the exact one-erasure strategy.

That is the hardware analogue of H17-07's 26-to-14 shared-DAG reduction.

## 8. Validation gate

Run:

\`\`\`powershell
.\tools\test_h18_adaptive.ps1
\`\`\`

and, with Yosys:

\`\`\`powershell
.\tools\synth_h18_adaptive.ps1
\`\`\`

Publication claims about RTL equivalence or cell count must wait for those logs.
