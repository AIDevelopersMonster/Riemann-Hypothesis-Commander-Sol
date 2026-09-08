# A Tea Party in the Additive-Multiplicative World with Hatter Sol

## The Number Line, the Observer, and Two Operations

**HATTER-SOL-01 · Reflections · 2026**

**Malachevsky, A.A.**  
ORCID: **0009-0008-6009-3196**  
A joint research line with Commander Sol / Hatter Sol

> *The number line may be an interface. The structure is deeper than the interface.*

## Abstract

We begin with an almost naive question: why do prime numbers look so irregular on the familiar number line? A closer look shows that the question already mixes two different structures: translation and linear geometry are natural for addition, whereas primality is defined through multiplication. We therefore separate, step by step, distinguishability, iteration, the natural-number sequence, addition, multiplication, divisibility, and primality.

The strict mathematical hinge of the essay is the contrast between the enormous automorphism group of the purely multiplicative structure of the positive integers and the rigidity of full natural-number arithmetic. Primes are completely interchangeable as atoms of the multiplicative monoid, but become individually fixed once addition and multiplication must be preserved simultaneously:

\[
\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathbb P),
\]

whereas

\[
\operatorname{Aut}(\mathbb N,+,\times,0,1)=\{\mathrm{id}\}.
\]

At the end we introduce the paired map

\[
\Omega(a,b)=(a+b,ab),
\]

not as a new operation, but as a doorway to the next question: can the loss and recovery of arithmetic symmetries be studied systematically through reducts of a joint additive-multiplicative structure?

**Keywords:** natural numbers; number line; addition; multiplication; prime numbers; automorphisms; structuralism; natural numbers object; symmetry; structural reducts.

### Status of the claims

The two automorphism lemmas are elementary consequences of unique factorization and the rigidity of the natural-number successor structure; they are not claimed as new results. The contribution of this note lies in the framing, synthesis, and the transition to a programme of reducts of the joint structure. The formula \(\Omega(a,b)=(a+b,ab)\) is classical as the pair of elementary symmetric characteristics of two quantities.

Throughout, \(\mathbb N=\{0,1,2,\ldots\}\), \(\mathbb N_{>0}=\{1,2,3,\ldots\}\), and \(\mathbb P\) denotes the set of prime numbers.

---

## 1. Where the tea party began

Some mathematical constructions are so familiar that we stop noticing that they are constructions at all. The number line is one of them.

We write

\[
0,1,2,3,4,5,\ldots
\]

place the numbers from left to right, introduce addition, then multiplication, divisibility, and prime numbers - and very quickly begin to experience the whole arrangement almost as if it were the immediate architecture of reality.

But how many choices have already been made before the first mathematical question is asked? Why is there a distinguished zero? Why does translation feel like the natural symmetry? Why do we treat primes as points on this line? And to what extent does their apparent strangeness belong to the primes themselves, rather than to the mathematical environment in which we look at them?

That is where our tea party began.

## 2. Primes as a reason to doubt the line

Take a finite segment of the natural numbers and mark the primes. We may move the origin, glue the ends into a ring, rotate the resulting prime mask, and count overlaps. Very quickly we enter classical mathematics: prime pairs, correlations, differences between primes, cyclic patterns, and additive combinatorics. The Hardy-Littlewood programme already treats joint primality under shifts as a central object [1].

But then another question appears. Why do we expect primes to be symmetric under a translation

\[
n\mapsto n+a?
\]

Translation is natural for the additive structure. Primality is multiplicative: \(p\) is prime because it has no nontrivial factorization \(p=ab\).

So the first change of viewpoint is this:

\[
\boxed{\text{a multiplicative object is being examined through additive geometry}.}
\]

At that moment the ordinary number line ceases to look neutral.

## 3. What happens if we keep only multiplication?

Consider the positive integers only as the multiplicative system

\[
(\mathbb N_{>0},\times).
\]

The fundamental theorem of arithmetic gives each \(n\) a unique prime factorization. In this geometry, the primes are the atoms of a free commutative monoid.

Now the primes may be permuted and the permutation extended to all composite numbers through factorization. For example, if we send \(2\) to \(101\), \(3\) to \(17\), and \(5\) to \(1009\), and continue this bijectively on all primes, then

\[
12=2^2\cdot3
\]

is sent to

\[
101^2\cdot17,
\]

while multiplication is preserved.

### Lemma 1. Multiplicative symmetry of the primes

\[
\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathbb P).
\]

**Proof.** Every automorphism of the multiplicative monoid must send atoms to atoms, and therefore induces a permutation of the set of primes. Conversely, every permutation

\[
\sigma:\mathbb P\to\mathbb P
\]

extends uniquely to \(\mathbb N_{>0}\) by replacing each prime factor \(p\) in the factorization of an integer by \(\sigma(p)\). Unique factorization guarantees that the extension is well defined and multiplicative. \(\square\)

Thus, from the point of view of multiplication alone, there is no structural individuality separating \(2\), \(3\), \(5\), and \(7919\): they all lie in a single orbit of the automorphism group.

\[
\boxed{\text{all primes are atoms of one and the same structural type}.}
\]

## 4. Addition removes that symmetry

Now restore the full structure

\[
(\mathbb N,+,\times,0,1).
\]

Here \(1\) fixes \(2=1+1\), then \(3=2+1\), and by induction every natural number. We can no longer interchange \(2\) and \(101\) without destroying addition.

### Lemma 2. Rigidity of full natural-number arithmetic

\[
\operatorname{Aut}(\mathbb N,+,\times,0,1)=\{\mathrm{id}\}.
\]

**Proof.** An automorphism preserves the constant \(1\). Hence it preserves \(2=1+1\), then \(3=2+1\), and inductively every \(n\in\mathbb N\). Therefore the automorphism is the identity. \(\square\)

This is the mathematical hinge of the whole essay:

\[
\boxed{\text{primes are interchangeable as atoms of multiplication,}}
\]

but

\[
\boxed{\text{they are individually fixed as elements of the joint world }(+ ,\times).}
\]

A richer structure has fewer symmetries:

\[
\operatorname{Sym}(\mathbb P)\longrightarrow\{\mathrm{id}\}.
\]

## 5. Alice looks at the number line

Imagine Alice standing before an infinitely long tea table. Along the edge are cups labelled

\[
0,1,2,3,4,5,\ldots
\]

Small stars glow on the cups corresponding to prime numbers. Alice moves the entire table by one place: the stars do not match. By two places: some match. By six: a different pattern appears.

One could study those coincidences for a very long time. But the Hatter asks another question:

> Why are you moving the table at all?

Translation is a law of additive geometry. The stars were placed according to factorization.

Perhaps Alice is not only studying the irregularity of the stars. Perhaps she is also seeing the tension between two different ways of looking at the same table. The image proves nothing; it merely keeps the central plot visible while the formal argument proceeds through automorphisms and forgotten structure.

## 6. Why does the natural-number sequence feel obvious?

Human beings are good at distinguishing separate objects, so "one, one more, one more" can feel almost like a direct feature of the world. Yet the cognitive science of number gives a more complicated picture. In infants, adults, and animals, researchers distinguish at least two pre-symbolic systems: an approximate representation of larger numerosities and an exact system for tracking a small number of individual objects [2].

Studies of the Munduruku make the distinction between approximate numerosity and exact symbolic arithmetic especially vivid: large quantities can be compared and approximately combined without an elaborate numeral system, while exact arithmetic beyond small numbers depends strongly on culturally learned counting resources [3].

So the exact sequence

\[
1,2,3,4,\ldots
\]

is not simply read off from the visible world. It is conceptually and culturally completed - through language, training, symbols, and, crucially, the recursive idea of "one more" [4].

## 7. What counts as an object in the first place?

To write

\[
1+1=2,
\]

we have already decided that there are two instances of something before us. But the same fragment of reality can be individuated in different ways. A glass of water may be treated as one object, as an enormous collection of molecules, or as a density field \(\rho(x,t)\).

In quantum theory the question becomes sharper. Identical particles need not possess the classical individuality of little labelled balls with permanent names. The philosophy of quantum physics therefore treats identity, individuality, and indistinguishability as separate problems [8].

A more careful conceptual chain therefore begins not with a ready-made "object", but with a distinguishable state or event that can recur.

## 8. Natural number as iteration

Suppose there is a state \(x_0\) and a repeatable transformation \(f\). Then we obtain

\[
x_0,\quad f(x_0),\quad f^2(x_0),\quad f^3(x_0),\ldots
\]

The number \(3\) may be understood as the position corresponding to three repetitions, rather than as three pictured apples.

Category theory formalizes precisely this structural role through a natural numbers object: zero and successor provide a universal mechanism of recursion. In Lawvere's classical formulation, the natural numbers are characterized not by the substance of their representatives but by a universal property [5].

This matters for our imagined "other intelligence". It may never draw a horizontal number line and still arrive at a structure isomorphic to the natural numbers by iterating states.

## 9. The observer and the structure

The observer influences how a structure is first detected; body, culture, and language influence which representations feel natural. Mathematics then asks a different question: what remains invariant when one realization is replaced by another?

Benacerraf showed how problematic it is to identify a number with one particular set-theoretic realization [6]. The structuralist line takes the next step: arithmetic concerns positions in a network of relations rather than a special "substance of numbers"; Shapiro summarizes this attitude with the idea that mathematics is the science of structures [7].

This separates the way we encounter mathematics from what survives independently of the chosen representation.

## 10. The three-dimensional world: source or interface?

Our spatial experience almost certainly shapes mathematical intuition. Points, lines, distances, directions, and motions feel natural to us. Yet the successor operation

\[
n\mapsto n+1
\]

does not require three spatial dimensions. It can arise from a temporal sequence of beats or from repeated state transitions.

Three-dimensionality therefore seems more likely to explain part of the naturalness of our representations than the natural-number structure itself. The number line may be a magnificent interface to arithmetic - but an interface is not the object it displays.

## 11. Where does addition come from?

If a number records the count of repetitions, addition appears as composition of those repetitions. Performing an action \(m\) times and then another \(n\) times is performing it \(m+n\) times.

On this reading, \(+\) is not fundamentally a move to the right on a school ruler. The line represents addition, but need not generate it. Addition expresses composition of iteration counts.

## 12. Multiplication as the next level of composition

Now we may repeat not one action but whole equal blocks of actions. Five blocks of three repetitions give

\[
3+3+3+3+3=5\times3.
\]

Multiplication may thus be viewed as iteration of addition.

But once \(\times\) appears, a qualitatively new network of relations appears with it: divisibility, factors, composite numbers, and multiplicative atoms. The distributive law

\[
a(b+c)=ab+ac
\]

couples the two operations so that they are no longer independent layers.

Primality therefore lies surprisingly far downstream from the first act of counting:

\[
\boxed{\text{distinguishability}\to\text{iteration}\to\mathbb N\to+\to\times\to\text{divisibility}\to\text{primes}.}
\]

## 13. The small asymmetry of even and odd numbers

Consider

\[
2\mathbb Z
\]

and

\[
1+2\mathbb Z.
\]

Additively these are two neighbouring cosets; translation by one interchanges them. From an affine point of view they are on equal footing.

Multiplicatively, however, a sharp asymmetry appears: every element of \(2\mathbb Z\) has the common nontrivial factor \(2\), while the coset \(1+2\mathbb Z\) has no such common factor. The distinction between even and odd emerges precisely when the multiplicative structure is laid on top of the additive one.

This is a small model of the same phenomenon that makes primes individually distinguishable in full arithmetic.

## 14. The problem is not the horizontal line

If another intelligence draws the natural numbers as a spiral, a tree, or machine states, the primes do not change provided that \(+\) and \(\times\) are preserved. An isomorphism of the full arithmetic structure carries primality with the entire network of relations.

So prime numbers are not an artifact of the horizontal number line. Their individuality, however, does depend on how much structure is being retained. Forget addition, and the primes become interchangeable atoms again.

## 15. Before choosing an operation

Usually we ask either for \(a+b\) or for \(ab\), as if pressing one of two buttons. But the structure \((\mathbb N,+,\times)\) already contains both results at once.

Take \(a=3\) and \(b=5\). Addition gives \(8\); multiplication gives \(15\). If we keep the pair \((8,15)\), then the original unordered pair is recovered as the roots of

\[
x^2-8x+15=0.
\]

This is simply Viete's relation: sum and product are the elementary symmetric characteristics of a pair.

\[
a=3,\ b=5\Rightarrow(a+b,ab)=(8,15)\Rightarrow x^2-8x+15=0\Rightarrow\{3,5\}.
\]

The interesting point is not that the formula is new. It is the change of viewpoint. Instead of treating \(+\) and \(\times\) as two unrelated buttons, we may temporarily keep them as two coordinates of one joint characteristic of the pair.

## 16. One object instead of two buttons

The most immediate notation for this viewpoint is the paired map

\[
\boxed{\Omega(a,b)=(a+b,ab).}
\]

It is not a binary operation \(S\times S\to S\): its value lives in \(S^2\). Ordinary addition and multiplication are recovered by projection to the first or second coordinate.

Forget the second coordinate and the additive view remains. Forget the first and the multiplicative view remains. Forget neither and the joint information remains. Formally this is elementary. The research problem begins only when we ask whether such forgetting can support a useful theory of structural reducts.

## 17. What exactly is lost under projection?

Passing from a richer structure to a reduct usually enlarges the automorphism group: the fewer relations a transformation must preserve, the more transformations qualify as symmetries.

In our simplest example, the passage

\[
(\mathbb N,+,\times,0,1)\longrightarrow(\mathbb N_{>0},\times)
\]

changes the symmetry group radically:

\[
\{\mathrm{id}\}\longrightarrow\operatorname{Sym}(\mathbb P).
\]

The symmetry of the primes does not arise from nowhere. It becomes visible after we forget the structure that distinguished primes additively.

The next question is therefore no longer merely philosophical: can one build natural intermediate reducts between full arithmetic and pure multiplication, and quantify how much arithmetic individuality is lost at each stage?

## 18. The number line after the tea party

We began with the simple picture

\[
0-1-2-3-4-5-\cdots
\]

and the question of why the primes sit on it so strangely. The picture now looks different.

A number need not be a point. Counting need not begin with a classical physical object. The natural-number sequence can arise from repetition. Addition can be the law of composing repetitions. Multiplication adds a second level of composition. Divisibility appears only once these structures interact. Primes arrive later still.

The number line is therefore not arithmetic itself. It is one extraordinarily successful projection of a richer structure.

Perhaps the productive change of viewpoint is not to search for another line, but to suspend, for a moment, the demand that we choose one operation at all.

## Boundaries of the claim

This note does not claim that sum and product are physically fundamental "coordinates of the world", nor does it propose \(\Omega(a,b)=(a+b,ab)\) as a new algebraic operation. The pair \((a+b,ab)\) is classical, and the automorphism lemmas are elementary. The narrower programme developed here is to study arithmetic individuality and symmetry through successive retention and forgetting of structure, keeping known constructions clearly separated from any genuinely new theorem that may emerge later.

The Alice-and-Hatter literary frame is used as a device for making familiar arithmetic strange again; it carries no evidential or deductive weight.

## References

1. Hardy, G. H.; Littlewood, J. E. *Some problems of "Partitio numerorum"; III: On the expression of a number as a sum of primes.* Acta Mathematica 44(1), 1-70 (1923). DOI: 10.1007/BF02403921.
2. Feigenson, L.; Dehaene, S.; Spelke, E. *Core systems of number.* Trends in Cognitive Sciences 8(7), 307-314 (2004). DOI: 10.1016/j.tics.2004.05.002.
3. Pica, P.; Lemer, C.; Izard, V.; Dehaene, S. *Exact and approximate arithmetic in an Amazonian indigene group.* Science 306(5695), 499-503 (2004). DOI: 10.1126/science.1102085.
4. Carey, S. *The Origin of Concepts.* Oxford University Press (2009). DOI: 10.1093/acprof:oso/9780195367638.001.0001.
5. Lawvere, F. W. *An elementary theory of the category of sets.* Proceedings of the National Academy of Sciences 52(6), 1506-1511 (1964). DOI: 10.1073/pnas.52.6.1506.
6. Benacerraf, P. *What Numbers Could Not Be.* The Philosophical Review 74(1), 47-73 (1965). DOI: 10.2307/2183530.
7. Shapiro, S. *Philosophy of Mathematics: Structure and Ontology.* Oxford University Press (1997).
8. French, S.; Krause, D. *Identity in Physics: A Historical, Philosophical, and Formal Analysis.* Oxford University Press (2006). DOI: 10.1093/0199278245.001.0001.
9. Wigner, E. P. *The unreasonable effectiveness of mathematics in the natural sciences.* Communications on Pure and Applied Mathematics 13(1), 1-14 (1960). DOI: 10.1002/cpa.3160130102.

---

## To be continued

### HATTER-SOL-02 · working title

**"Two Cups of the Same Tea: \(\Omega=(+,\times)\), Structural Reducts, and the Return of Prime Symmetry."**

The next note will separate the mere packaging of two familiar operations from a substantive theory of reducts: which intermediate structures are natural, how their automorphism groups change, and whether the loss of arithmetic individuality can be measured.

> At the next tea party, the Hatter will no longer ask Alice why she is moving the table. He will ask what happened to the world when she removed one of the two cups.

\[
\boxed{\text{To be continued.}}
\]
