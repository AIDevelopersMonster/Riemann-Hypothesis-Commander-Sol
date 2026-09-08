# HATTER-SOL · Arithmetic Tea Party

**Серия Commander Sol / Малачевский А.А.** о том, какие части привычной арифметики принадлежат представлению, какие — структуре, и как меняются симметрии чисел при забывании или совместном удержании операций.

Русское название серии:

**«Чаепития в аддитивно-мультипликативном мире с Шляпником Sol»**.

English series title:

**“Tea Parties in the Additive–Multiplicative World with Hatter Sol.”**

- Human author: **Малачевский А.А. / Malachevsky, A.A.**
- ORCID: **0009-0008-6009-3196**
- AI research collaborator / dialog persona: **Commander Sol · Hatter Sol**
- Repository branch: `main`
- Series folder: [`papers/HATTER-SOL/`](https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL)
- Zenodo status: **Notes 01 and 02 published**

## Note 01

**«Чаепитие в аддитивно-мультипликативном мире с Шляпником Sol: числовая ось, наблюдатель и две операции»**

English title:

**“A Tea Party in the Additive–Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations.”**

- Zenodo DOI: **[10.5281/zenodo.22639237](https://doi.org/10.5281/zenodo.22639237)**
- Russian manuscript: [`01-NUMBER-LINE-OBSERVER-TWO-OPERATIONS/article_ru.md`](01-NUMBER-LINE-OBSERVER-TWO-OPERATIONS/article_ru.md)
- English manuscript: [`01-NUMBER-LINE-OBSERVER-TWO-OPERATIONS/article_en.md`](01-NUMBER-LINE-OBSERVER-TWO-OPERATIONS/article_en.md)

The note separates four layers that are often conflated:

1. individuation / distinguishability;
2. iteration and the natural-number structure;
3. additive composition;
4. multiplicative composition and divisibility.

Its strict algebraic hinge is the contrast

\[
\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathbb P)
\]

versus

\[
\operatorname{Aut}(\mathbb N,+,\times,0,1)=\{\mathrm{id}\}.
\]

Thus primes are fully exchangeable as multiplicative atoms, but become individually pinned once the additive and multiplicative structures are required simultaneously.

The note ends by introducing, without claiming novelty for the underlying classical construction, the paired map

\[
\Omega(a,b)=(a+b,ab),
\]

as the doorway to the next paper on projections, reducts, lost structure, and recovered symmetry.

## Note 02

**«Два чайника, одна чашка: “Кто ты?” среди простых»**

English title:

**“Two Teapots, One Cup: ‘Who Are You?’ Among the Primes.”**

- Zenodo DOI: **[10.5281/zenodo.22656414](https://doi.org/10.5281/zenodo.22656414)**
- Russian manuscript: [`02-TWO-TEAPOTS-ONE-CUP/article_ru.md`](02-TWO-TEAPOTS-ONE-CUP/article_ru.md)
- English manuscript: [`02-TWO-TEAPOTS-ONE-CUP/article_en.md`](02-TWO-TEAPOTS-ONE-CUP/article_en.md)
- Hostile literature audit: [`02-TWO-TEAPOTS-ONE-CUP/LITERATURE_AUDIT.md`](02-TWO-TEAPOTS-ONE-CUP/LITERATURE_AUDIT.md)

The second note studies controlled expansions of the multiplicative monoid by modular and quadratic probes. Its central results include:

\[
\#(\mathbb P/\operatorname{Aut}(\mathcal M_F))
=
|F|+\prod_{p\in F}\tau(p-1),
\]

for finitely many named prime congruence relations, and

\[
\#(\mathbb P/\operatorname{Aut}(\mathcal Q_F))
=
|F|+2^{|F|},
\]

for finite families of quadratic one-bit probes.

It also proves the finite-information barrier, an exact rigidity criterion through injectivity of Legendre-signature maps, arbitrarily sparse rigidifying families, and the optimal finite coding law

\[
\boxed{\kappa_2(S)=\lceil\log_2|S|\rceil}.
\]

The guiding principle is:

\[
\boxed{
\text{individuality}\neq\text{completeness of description};
\qquad
\text{individuality}=\text{sufficiency of separation}.
}
\]

## Planned continuation

**HATTER-SOL-03** — current research question:

> Can a finite natural mechanism generate, from within the structure itself, a separating family rich enough to recover rigidity without externally naming an infinite family of probes?

The literary continuation is the Hatter's question: if nobody asks the questions from outside, can the cup learn to ask them itself?

## Follow the series

For readers who want to follow new notes, source updates, illustrations, and continuity checkpoints, use the permanent GitHub folder:

**https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol/tree/main/papers/HATTER-SOL**

## Editorial principle

The series keeps the “Размышлизмы” style: free explanatory movement is allowed, but every mathematical claim must be distinguished from metaphor, literature background, and open research questions. Classical results are not presented as new. Newness, if any, must enter through a nontrivial theorem, invariant, reduction law, or demonstrably useful synthesis.