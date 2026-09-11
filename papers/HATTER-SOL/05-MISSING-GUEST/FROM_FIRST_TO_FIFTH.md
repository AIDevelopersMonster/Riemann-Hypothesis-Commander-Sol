# HATTER-SOL-05 · From the First Cup to the Fifth

## Канонический мост серии / Canonical series bridge

Этот файл фиксирует математическую преемственность HATTER-SOL-05 с исходной задачей серии.

---

# 1. Исходная крайность

В чисто мультипликативном мире

\[
(\mathbb N_{>0},\times)
\]

простые являются свободными атомами, поэтому

\[
\boxed{
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
}
\]

В полной натуральной арифметике

\[
(\mathbb N,+,\times,0,1)
\]

все натуральные числа фиксируются, и

\[
\boxed{
\operatorname{Aut}(\mathbb N,+,\times,0,1)=\{\mathrm{id}\}.
}
\]

Отсюда вопрос всей серии:

\[
\boxed{
\text{какой минимальный фрагмент арифметики уже лишает простые права менять имена?}
}
\]

---

# 2. От сильного predecessor к radical predecessor

HATTER-SOL-03 использует достаточно сильную predecessor-информацию, чтобы получить жёсткость.

HATTER-SOL-04 ослабляет эту информацию до directed prime graph

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

Здесь сохраняется только support простых делителей \(p-1\), но забываются их кратности.

Центральный вопрос:

\[
\boxed{
\operatorname{Aut}(\Pi)\stackrel?=\{\mathrm{id}\}.
}
\]

HATTER-SOL-04 свёл задачу к exact predecessor fibers

\[
X_S=\{p:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|,
\]

и к multiplicity tower по Pratt heights.

---

# 3. Почему тестируем \(3\leftrightarrow5\)

В чистом мультипликативном мире transposition

\[
\tau=(3\ 5)
\]

разрешён свободно.

В radical-predecessor graph он не погибает на первом слое, потому что

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

Поэтому вопрос

\[
\boxed{
\text{продолжается ли }(3\ 5)\text{ до глобального автоморфизма }\Pi?
}
\]

является минимальным конкретным тестом исходной темы серии.

---

# 4. Exact-support arithmetic

Для конечного \(S\ni2\),

\[
X_S
=
\left\{
1+\prod_{q\in S}q^{e_q}
\text{ prime}:e_q\ge1
\right\}.
\]

Эти экспоненциальные семейства возникают не как внешняя теория специальных простых, а как точное арифметическое содержание condition

\[
\operatorname{Pred}(p)=S.
\]

На одном конкретном шаге tower, когда действие \(g\) на support уже задано, mismatch

\[
\mu(S)\ne\mu(gS)
\]

блокирует это продолжение.

Для самого seed \(\tau\) на непосредственном следующем уровне это может иметь вид

\[
\mu(S)\ne\mu(\tau S).
\]

Но на более поздних высотах нельзя безусловно говорить об одном support witness: предыдущие уровни могут иметь несколько допустимых продолжений. Тогда корректный объект — **finite obstruction family/tree**, блокирующий каждую surviving branch.

---

# 5. Что доказал HATTER-SOL-05

Пятый цикл дал следующий theorem package.

## 5.1. Finite-cover escape

Для любого fixed exact support и любого конечного множества fixed prime divisors существуют candidate exponent vectors, избегающие всех этих делителей. Поэтому обычный finite fixed-divisor covering не может доказать emptiness exact fiber.

## 5.2. Cyclotomic dimension jump

Если

\[
1+\prod q_i^{e_i}
\]

prime, то

\[
\gcd(e_1,\ldots,e_k)
\]

есть степень \(2\).

Для singleton support это Fermat-type collapse; для \(k\ge2\) остаётся положительная плотность

\[
\frac1{\zeta(k)(1-2^{-k})}.
\]

## 5.3. Local \(3\)-versus-\(5\) asymmetry

Для first competing supports получены exact first-sieve densities

\[
\{2,3\}:\frac6{\pi^2},
\qquad
\{2,5\}:\frac4{\pi^2},
\]

с ratio \(3/2\). В weighted numerical ordering:

\[
A_{23}(X)
\sim
\frac{3}{\pi^2\log2\log3}(\log X)^2,
\]

\[
A_{25}(X)
\sim
\frac{2}{\pi^2\log2\log5}(\log X)^2.
\]

## 5.4. Descendant persistence and cardinality wall

The local \(3/2\) gap persists along 3-pure exact-descendant chains. Но multiplicity tower видит только cardinality. Если paired fibers infinite, то

\[
\mu(S)=\mu(gS)=\aleph_0,
\]

и количественная асимметрия исчезает из graph-visible data.

## 5.5. Finite-fiber compactness

Under FFC — all exact fibers finite — survival to every finite Pratt height implies global survival by König compactness. Если seed dies globally, то он dies на конечной высоте, и существует finite obstruction family/tree.

## 5.6. Density-one forward cone

Для каждого odd prime \(a\),

\[
\boxed{d_{\mathbb P}(C^+(a))=1.}
\]

Более того, уже directed future на расстоянии не более двух имеет relative prime density one.

Для seed transposition causal cone

\[
C_\tau=C^+(\{3,5\})
\]

также имеет density one.

## 5.7. Causal survival criterion

Cone-Fiber Infinitude CFI\((\tau)\) требует infinitude только для exact supports, пересекающих causal cone seed symmetry. Это строго локальнее прежнего HFI.

Under CFI\((\tau)\), transposition \((3\ 5)\) extends globally, причём extension можно выбрать фиксирующим все primes outside \(C_\tau\).

---

# 6. Что пятая статья не доказывает

Не доказано ни

\[
\operatorname{Aut}(\Pi)=\{\mathrm{id}\},
\]

ни существование nontrivial automorphism unconditionally.

Не доказана infinitude

\[
X_{\{2,3\}}
\]

и тем более general higher-fiber infinitude.

Local sieve asymmetry не является killing certificate сама по себе.

Finite obstruction theorem under FFC не является algorithmic decidability theorem.

---

# 7. Literature boundary

David Feldman's 2012 MathOverflow question and Gjergji Zaimi's answer already identified the graph

\[
p\to q\iff p\mid q-1
\]

and the importance of classes with the same exact incoming predecessor set. Therefore HATTER-SOL-05 не заявляет priority за сам exact-support architecture и broad finite/infinite-fiber dichotomy.

Classical ingredients include cyclotomic factorization, PNT in arithmetic progressions, divergence of reciprocal primes in a reduced progression, CRT, Möbius inversion, König's lemma, and standard lattice counting.

Publication claim is the rigorously assembled structural package inside the HATTER-SOL multiplicity-tower programme, with theorem/heuristic boundaries stated explicitly.

---

# 8. Итоговая линия серии

Содержательно путь теперь выглядит так:

\[
\boxed{
\operatorname{Sym}(\mathbb P)
\longrightarrow
\operatorname{Aut}(\Pi)
\stackrel?\longrightarrow
\{\mathrm{id}\}.
}
\]

HATTER-SOL-05 не закрывает последний знак вопроса, но точно показывает, где он живёт: не в дешёвом local sieve difference, а в exact-support cardinalities и их orbitwise compatibility through the multiplicity tower.

Следующий естественный шаг — orbitwise minimal survival criterion, weaker than cone-wide CFI. Это уже задача HATTER-SOL-06 и не должна задерживать freeze пятой статьи.
