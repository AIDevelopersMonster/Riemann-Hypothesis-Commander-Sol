# HATTER-SOL-05 · From the First Cup to the Fifth

## Канонический мост серии / Canonical series bridge

Этот файл фиксирует преемственность HATTER-SOL-05 с исходной задачей HATTER-SOL-01. Он предназначен как основа вводного раздела пятой статьи и как контроль против ухода ветки в изолированную задачу о специальных простых.

---

# 1. От первой чашки к пятой

Первая статья серии начиналась не с графа простых и не с специальных последовательностей. Она начиналась с вопроса о том, **какая структура делает простые индивидуальными**.

В чисто мультипликативном мире

\[
M=(\mathbb N_{>0},\times)
\]

основная теорема арифметики показывает, что положительные целые образуют свободный коммутативный моноид на множестве простых. Поэтому любая перестановка простых продолжается до автоморфизма всего моноида:

\[
\boxed{
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
}
\]

С точки зрения одной операции умножения простые не имеют индивидуальных имён: \(3\), \(5\), \(101\) и любой другой простой являются атомами одного структурного типа.

Полная натуральная арифметика ведёт себя противоположно. В структуре

\[
(\mathbb N,+,\times,0,1)
\]

единица фиксирована, затем фиксируются \(2=1+1\), \(3=2+1\), и по индукции каждое натуральное число. Поэтому

\[
\boxed{
\operatorname{Aut}(\mathbb N,+,\times,0,1)
=
\{\mathrm{id}\}.
}
\]

Так возник исходный вопрос серии:

\[
\boxed{
\text{где между чистым умножением и полной арифметикой простые теряют право менять имена?}
}
\]

HATTER-SOL-05 остаётся внутри именно этой задачи.

---

# 2. Серия как лестница забывания и восстановления структуры

Удобно рассматривать серию как движение между двумя крайностями:

\[
(\mathbb N_{>0},\times)
\qquad\text{и}\qquad
(\mathbb N,+,\times,0,1).
\]

При добавлении структуры группа автоморфизмов может только уменьшаться. Исследовательская программа состоит не в том, чтобы сразу вернуть всю арифметику, а в том, чтобы добавлять ровно столько информации, сколько нужно для разрушения тех или иных симметрий простых.

Схематически:

\[
\boxed{
\operatorname{Sym}(\mathbb P)
\supseteq
G_{\mathrm{weak}}
\supseteq
G_{\mathrm{strong}}
\supseteq
\{\mathrm{id}\}.
}
\]

В этой лестнице каждый выпуск отвечает на следующий вопрос: **какая информация уже убивает часть симметрий, а какая ещё оставляет их живыми?**

---

# 3. HATTER-SOL-01 — все простые взаимозаменяемы

Первая статья установила исходную крайность:

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
\]

Это не новая теорема, а структурный нулевой уровень всей программы.

Именно отсюда возникает конкретная тестовая симметрия

\[
\tau=(3\ 5).
\]

В чистом мультипликативном мире она разрешена совершенно свободно.

---

# 4. HATTER-SOL-02 — можно ли назвать простой коротким набором проб?

Вторая статья перешла от полной взаимозаменяемости к задаче индивидуализации простых с помощью ограниченных проб.

Главная идея была информационной: если набор наблюдаемых признаков слишком мал, разные простые остаются в одной орбите; если probes достаточно хорошо подобраны, конечное множество простых можно различить.

Тем самым HATTER-SOL-02 исследовал первую форму перехода

\[
\operatorname{Sym}(\mathbb P)
\longrightarrow
\text{меньшая группа симметрий}.
\]

Но сами probes ещё не являлись окончательным внутренним арифметическим механизмом.

---

# 5. HATTER-SOL-03 — сильная внутренняя структура уже даёт жёсткость

Третья статья сделала probes арифметически внутренними и нашла сильную структуру, которая полностью восстанавливает индивидуальность простых.

Для отношения

\[
S_{\mathbb P}(n,p)
\iff
p\in\mathbb P
\text{ and }
p=n+1
\]

получена жёсткость

\[
\boxed{
\operatorname{Aut}(\mathbb N_{>0},\times,S_{\mathbb P})
=
\{\mathrm{id}\}.
}
\]

Таким образом, серия впервые прошла весь путь от

\[
\operatorname{Sym}(\mathbb P)
\]

до

\[
\{\mathrm{id}\}.
\]

Но возник более острый вопрос: сколько информации в \(p-1\) действительно нужно для этой жёсткости?

Если удалить кратности простых множителей и помнить только support, останется ли структура жёсткой?

Так появился radical predecessor

\[
R_{\mathbb P}(r,p)
\iff
r=\operatorname{rad}(p-1).
\]

---

# 6. HATTER-SOL-04 — радикал забывает кратности

Отношение radical predecessor эквивалентно ориентированному графу на простых

\[
\Pi=(\mathbb P,D),
\qquad
D(q,p)\iff q\mid p-1.
\]

Здесь от полной аддитивной информации в \(p-1\) остаётся только вопрос:

> какие простые делят \(p-1\)?

но забывается, **с какими кратностями** они это делают.

Центральная проблема становится

\[
\boxed{
\operatorname{Aut}(\Pi)
\stackrel{?}{=}
\{\mathrm{id}\}.
}
\]

HATTER-SOL-04 не решил этот yes/no вопрос, но установил строгие ограничения на любой гипотетический нетривиальный автоморфизм. В частности, такой автоморфизм не может быть локальным или малым: его support обязан распространяться на неограниченные Pratt heights и иметь относительную плотность один среди простых; кроме того, он не может быть асимптотически близок к identity по рангу или величине простых.

Ключевой механизм продолжения оказался закодирован в exact predecessor fibers

\[
X_S
=
\{p\in\mathbb P:\operatorname{Pred}(p)=S\},
\qquad
\mu(S)=|X_S|.
\]

Автоморфизм конечной высоты продолжается на следующий уровень тогда и только тогда, когда сохраняются соответствующие multiplicities \(\mu(S)\).

Тем самым абстрактная проблема автоморфизмов была сведена к конкретной арифметической проблеме exact supports.

---

# 7. Почему первая тестовая симметрия — именно \(3\leftrightarrow5\)

В первой статье перестановка

\[
3\leftrightarrow5
\]

является одним из бесчисленных элементов \(\operatorname{Sym}(\mathbb P)\).

После добавления radical-predecessor структуры она не погибает немедленно, потому что

\[
\operatorname{Pred}(3)
=
\operatorname{Pred}(5)
=
\{2\}.
\]

Иными словами, первый слабый арифметический слой всё ещё не умеет отличить \(3\) от \(5\).

Поэтому вопрос HATTER-SOL-05

\[
\boxed{
\text{может ли }(3\ 5)\text{ продолжиться до глобального автоморфизма?}
}
\]

является не новой посторонней задачей, а **минимальным конкретным тестом исходной проблемы HATTER-SOL-01**.

---

# 8. Почему возникают exact-support fibers

Пусть

\[
S\subset\mathbb P
\]

конечно и содержит \(2\). Тогда

\[
X_S
=
\left\{
1+\prod_{q\in S}q^{e_q}
\text{ prime}:e_q\ge1
\right\}.
\]

Это не случайно выбранные экспоненциальные формы. Они являются арифметическим содержанием графового условия

\[
\operatorname{Pred}(p)=S.
\]

Поэтому сравнение

\[
X_S
\quad\text{и}\quad
X_{\tau S}
\]

точно измеряет, способен ли следующий слой radical-predecessor графа отличить support от его образа при \(3\leftrightarrow5\).

Если существует \(S\), для которого

\[
\mu(S)\ne\mu(\tau S),
\]

то \(\tau\) погибает на конечной высоте.

В лучшем случае можно получить

\[
\mu(S)=0,
\qquad
\mu(\tau S)>0,
\]

или наоборот.

Тогда слабая структура \(D\), не различавшая \(3\) и \(5\) напрямую, различит их **через будущее дерево exact descendants**.

---

# 9. Что уже показала пятая статья

Первые удары HATTER-SOL-05 дали три структурных факта.

### 9.1. Finite-cover escape

Для любого exact support \(S\ni2\) и любого конечного множества простых делителей \(T\) существуют exponent vectors, для которых

\[
1+\prod_{q\in S}q^{e_q}
\]

не делится ни на один простой из \(T\).

Следовательно, пустое exact fiber нельзя доказать обычным конечным fixed-divisor covering argument.

### 9.2. Cyclotomic dimension jump

Если candidate prime, то общий gcd показателей является степенью \(2\). Для singleton support это приводит к Fermat-type collapse и нулевой плотности допустимых exponents. Но для \(|S|\ge2\) cyclotomically admissible exponent vectors имеют положительную плотность

\[
\frac1{\zeta(k)(1-2^{-k})}.
\]

То есть higher exact-support fibers находятся по другую сторону настоящего dimension threshold.

### 9.3. Cardinality wall

Локальные sieve asymmetries между \(3\)- и \(5\)-ветвями существуют и наследуются вниз по descendant tree. Но radical graph видит только

\[
\mu(S)=|X_S|.
\]

Если обе paired fibers бесконечны, обе мощности равны \(\aleph_0\), и количественная sieve asymmetry стирается.

Это объясняет, почему исходная symmetry problem не решается простым накоплением локальных арифметических различий.

---

# 10. Главная преемственность в одной формуле

Вся линия HATTER-SOL теперь может быть записана так:

\[
\boxed{
(\mathbb N_{>0},\times)
\ \longrightarrow\ 
(\mathbb N_{>0},\times,R_{\mathbb P})
\ \longrightarrow\ 
(\mathbb N_{>0},\times,S_{\mathbb P})
}
\]

с соответствующим сжатием групп автоморфизмов

\[
\boxed{
\operatorname{Sym}(\mathbb P)
\ \supseteq\ 
\operatorname{Aut}(\Pi)
\ \supseteq\ 
\{\mathrm{id}\}.
}
\]

HATTER-SOL-05 исследует **среднее звено**.

Поэтому его основной вопрос можно сформулировать без упоминания технических деталей:

\[
\boxed{
\text{достаточно ли помнить только prime support числа }p-1,
\text{ чтобы простые снова получили индивидуальные имена?}
}
\]

Техническая работа с \(X_S\), \(\mu(S)\), local sieves и descendant trees — это уже способ ответить на этот вопрос.

---

# 11. Формулировка для вводного раздела будущей статьи

> В первой чашке все простые могли менять имена: чистый мультипликативный моноид видел в них свободно переставляемые атомы. В третьей чашке точный предшественник \(p-1\) вернул жёсткость полностью. Четвёртая чашка стёрла кратности и оставила только множество простых делителей \(p-1\). Пятая спрашивает, достаточно ли этого более слабого следа, чтобы в конце концов отличить даже \(3\) от \(5\). Поэтому формы \(1+\prod q^{e_q}\), возникающие ниже, не являются отдельной задачей о специальных простых: это exact fibers того самого промежуточного reduct, который стоит между полной взаимозаменяемостью простых и полной арифметической жёсткостью.

---

# 12. English canonical bridge

The first HATTER-SOL paper began with the maximal symmetry of the purely multiplicative world:

\[
\operatorname{Aut}(\mathbb N_{>0},\times)
\cong
\operatorname{Sym}(\mathbb P).
\]

Every prime may be renamed arbitrarily. At the opposite end, full natural arithmetic is rigid:

\[
\operatorname{Aut}(\mathbb N,+,\times,0,1)
=\{\mathrm{id}\}.
\]

The series therefore asks where, between these two structures, primes lose the right to exchange names.

HATTER-SOL-03 showed that retaining the exact predecessor relation \(p=n+1\) is already enough for rigidity. HATTER-SOL-04 then erased multiplicities in \(p-1\), retaining only its prime support through

\[
D(q,p)\iff q\mid p-1.
\]

The resulting graph \(\Pi=(\mathbb P,D)\) lies at the unresolved middle stage

\[
\operatorname{Sym}(\mathbb P)
\supseteq
\operatorname{Aut}(\Pi)
\supseteq
\{\mathrm{id}\}.
\]

The transposition \((3\ 5)\), allowed in the first paper's multiplicative world, survives the first radical-predecessor layer because

\[
\operatorname{Pred}(3)=\operatorname{Pred}(5)=\{2\}.
\]

HATTER-SOL-05 asks whether deeper exact-support multiplicities eventually kill this minimal surviving symmetry. The families

\[
X_S
=
\left\{
1+\prod_{q\in S}q^{e_q}
\text{ prime}:e_q\ge1
\right\}
\]

are therefore not an isolated problem about special prime forms. They are exactly the arithmetic fibers that control whether a symmetry from the first paper survives in the intermediate radical-predecessor reduct.

---

## Editorial rule for HATTER-SOL-05

Every technical section of the future article should remain traceable to the series question:

> **Which forgotten part of arithmetic is actually needed to destroy prime-renaming symmetry?**

If a calculation about exact-support primes does not contribute to the survival or death of an automorphism, it belongs in a side note, not in the main proof line.
