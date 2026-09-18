# HATTER-SOL-17 · Research Seed
## Неабелевы структурные инварианты как возможная основа криптографического примитива

**Статус:** интересный вариант дальнейшего исследования.  
**Важно:** это **не утверждение о создании постквантовой криптосистемы** и не заявление о стойкости H17. Текущий \(PSL(2,7)\) слишком мал и перебирается полностью. Документ фиксирует только исследовательскую гипотезу, естественно возникшую из H17.

---

## 1. Откуда возникает идея

В H17 изучается отображение

\[
(A,B)
\longrightarrow
[(A,B)]
\longrightarrow
F(A,B),
\]

где

\[
(A,B)\sim(hAh^{-1},hBh^{-1}),
\qquad h\in PSL(2,7).
\]

Для generating pairs:

- существует 19152 конкретных пар \((A,B)\);
- они разбиваются на 114 simultaneous-conjugacy orbits;
- каждая orbit содержит 168 представителей;
- robust8 fingerprint одинаков для всех представителей одной orbit;
- при переходе к orbit-level description информация о конкретном conjugator/frame теряется.

То есть H17 уже содержит конечную модель следующего явления:

\[
\boxed{
\text{много конкретных representatives}
\longrightarrow
\text{один легко вычислимый structural invariant}
}
\]

При этом quotient map намеренно забывает, **какой именно представитель** породил invariant.

---

## 2. Почему это ещё не криптография

В H17 группа фиксирована:

\[
PSL(2,7),
\qquad |PSL(2,7)|=168.
\]

Полное generating-пространство содержит всего:

\[
19152
\]

пар.

Такое пространство не имеет криптографического масштаба и перебирается практически мгновенно.

Следовательно, нельзя использовать текущий H17 как:

- шифр;
- key exchange;
- signature scheme;
- password hash;
- post-quantum primitive.

Неабелевость сама по себе также **не является доказательством квантовой стойкости**.

---

## 3. Правильная исследовательская постановка

Вместо вопроса

> «Можно ли использовать H17 как постквантовый шифр?»

ставится более узкий вопрос:

\[
\boxed{
\text{существует ли масштабируемое семейство неабелевых структур,}
\\
\text{где invariant вычисляется легко, а восстановление скрытого}
\\
\text{representative/conjugator остаётся трудным?}
}
\]

Пусть существует семейство групп:

\[
G_n,
\]

где \(n\) — параметр безопасности.

Публично фиксируется пара:

\[
(A,B)\in G_n^2.
\]

Секрет:

\[
h\in G_n.
\]

Строится:

\[
A'=hAh^{-1},
\qquad
B'=hBh^{-1}.
\]

Публичные данные могут включать:

\[
(A,B,A',B')
\]

и/или структурные invariants, удовлетворяющие:

\[
F(A,B)=F(A',B').
\]

Тогда естественная search-задача:

\[
\boxed{
\text{найти }h
\text{ из }
A'=hAh^{-1},
\quad
B'=hBh^{-1}.
}
\]

Это simultaneous conjugacy search problem в конкретном выбранном семействе.

---

## 4. Возможный криптографический смысл

Если для подходящего \(G_n\):

1. применение \(h\) эффективно;
2. вычисление invariant эффективно;
3. проверка relation эффективна;
4. восстановление \(h\) существенно труднее;
5. не существует более простого обхода через leakage invariants;

то естественно исследовать primitive вида:

\[
\boxed{
\text{easy verification}
+
\text{hidden conjugator}
}
\]

Первая потенциальная цель здесь — не шифрование данных, а более простые конструкции:

- identification protocol;
- proof of knowledge;
- authentication;
- signature-like construction;
- commitment-like primitive.

Это только направления для проверки, а не готовые схемы.

---

## 5. Почему H17 интересен как лабораторная модель

H17 уже показывает несколько необходимых ингредиентов в малом конечном случае.

### 5.1. Quotient-инвариантность

\[
F(A,B)
=
F(hAh^{-1},hBh^{-1}).
\]

То есть fingerprint зависит от structural orbit, а не от конкретной нумерации/представителя.

### 5.2. Нетривиальная роль порядка умножения

В неабелевой группе:

\[
AB\neq BA.
\]

Поэтому короткие слова

\[
AAB,\;
Abb,\;
AABAb,\;
AAbAb,\;
ABABB,\;
ABaBB
\]

несут информацию, отсутствующую в полностью коммутативной модели.

### 5.3. Compact structural observations

Большой объект \((A,B)\) может отображаться в компактный набор class observations.

### 5.4. Loss of representative information

Переход к orbit-level representation действительно уничтожает frame/conjugator information.

Но в H17 это уничтожение **информационное**, а не вычислительно трудное: маленький размер позволяет перебор.

---

## 6. Что нельзя утверждать

На данном этапе запрещено делать следующие выводы:

- «неабелевы группы устойчивы к алгоритму Шора»;
- «неабелевость автоматически означает post-quantum security»;
- «невозможно восстановить исходную группу Галуа»;
- «H17 является one-way function»;
- «H17 даёт collision-resistant hash»;
- «H17 пригоден для хранения криптографических ключей»;
- «текущий \(PSL(2,7)\) имеет практическую криптостойкость».

В H17 вообще не требуется восстанавливать «исходную группу Галуа». Группа известна заранее. Теряется информация о конкретном representative/conjugator внутри одной simultaneous-conjugacy orbit.

---

## 7. Главный математический барьер

Нужна не просто большая группа, а семейство, в котором одновременно выполняются противоположные требования:

\[
\boxed{
\begin{array}{l}
\text{legitimate operations — дешёвые},\\
\text{verification — дешёвая},\\
\text{public invariants — компактные},\\
\text{secret recovery — дорогая}.
\end{array}
}
\]

При этом нельзя допустить, чтобы выбранный fingerprint сам раскрывал секрет через:

- centralizers;
- canonical forms;
- character data;
- matrix normal forms;
- linearization;
- representation-theoretic leakage;
- short-word relations;
- hidden abelian quotient;
- efficient reduction к известной лёгкой задаче.

---

## 8. Что означает «постквантовый» в этой ветке

Для серьёзного результата мало показать отсутствие очевидного классического алгоритма.

Нужно исследовать как минимум:

### Classical attacks

- exhaustive search;
- meet-in-the-middle;
- centralizer attacks;
- canonical form reduction;
- linear algebra attacks;
- Gröbner / polynomial reformulation, если применимо;
- decomposition attacks;
- representation attacks.

### Quantum attacks

- reduction to abelian hidden subgroup;
- nonabelian hidden subgroup algorithms;
- quantum walk / collision approaches;
- amplitude-amplified search;
- group-specific quantum algorithms.

Только после такого анализа можно говорить о candidate post-quantum assumption.

---

## 9. Возможный исследовательский маршрут

### Stage PQ-0 — finite toy model

Использовать H17 как fully enumerable лабораторию:

\[
PSL(2,7).
\]

Цель — понять, какие invariants теряют representative information, а какие её случайно раскрывают.

### Stage PQ-1 — scalable families

Рассмотреть несколько семейств \(G_n\), не выбирая победителя заранее.

Критерии:

- efficient representation;
- efficient multiplication/inversion/conjugation;
- rapidly growing state space;
- nontrivial simultaneous-conjugacy search;
- возможность строить H17-like short-word invariants.

### Stage PQ-2 — leakage audit

Для каждого candidate family проверить:

\[
\text{public data}
\Rightarrow
\text{сколько bits/structure о }h\text{ раскрывается}.
\]

### Stage PQ-3 — attack-first prototype

До проектирования протокола попытаться сломать саму hard-problem assumption.

Если hidden conjugator эффективно восстанавливается, family отбрасывается.

### Stage PQ-4 — primitive only after surviving attacks

Только после выживания hard problem рассматривать:

- identification;
- proof of knowledge;
- signatures;
- key establishment.

---

## 10. H17-specific эксперимент, который стоит сделать первым

Даже на \(PSL(2,7)\) полезно измерить, **насколько robust8 fingerprint уменьшает uncertainty внутри полного пространства пар**.

Для каждого набора публичных наблюдений можно вычислить:

\[
N_{\mathrm{compatible}}
=
\#\{(A,B):\text{наблюдения совпадают}\}.
\]

Далее сравнить:

- raw pair;
- orbit ID;
- robust8 fingerprint;
- subsets of probes;
- extra class invariants.

Это даст точную finite-model картину:

\[
\boxed{
\text{какая информация сохраняется}
\quad\text{и}\quad
\text{какая уничтожается quotient map}
}
\]

и позволит не путать «неоднозначность» с «вычислительной трудностью».

---

## 11. Критерий продолжения ветки

Ветка заслуживает отдельного активного research branch только если найдено хотя бы одно масштабируемое семейство \(G_n\), для которого одновременно:

1. H17-like invariant имеет естественное определение;
2. размер пространства растёт экспоненциально с параметром;
3. known classical attacks не дают немедленного polynomial-time recovery;
4. структура не схлопывается к малой абелевой/линейной задаче;
5. существует содержательная attack model для quantum adversary.

До этого документ остаётся **research seed**, а не криптографическим результатом.

---

## 12. Рабочая формулировка идеи

Наиболее аккуратная версия гипотезы:

> H17 даёт конечный пример, в котором большое множество конкретных пар \((A,B)\), связанных simultaneous conjugation, отображается в общий легко вычислимый structural invariant, а информация о конкретном representative уничтожается при факторизации по orbit. Это не создаёт криптографической стойкости в малом \(PSL(2,7)\), но мотивирует исследование масштабируемых неабелевых семейств, где вычисление invariant остаётся дешёвым, а восстановление скрытого conjugator или representative может стать вычислительно трудной задачей для классического и квантового противника.

---

## 13. Текущий статус

\[
\boxed{\text{INTERESTING RESEARCH DIRECTION — NOT A CRYPTOGRAPHIC CLAIM}}
\]

H17 остаётся математической и аппаратной лабораторией.

Криптографическая ветка открывается только как вопрос:

\[
\boxed{
\text{может ли структурная quotient-инвариантность быть масштабирована}
\\
\text{до настоящей computational hardness?}
}
\]
