# HATTER-SOL-18
# Адаптивная неабелева томография: Nielsen dynamics, Higman trace, сжатие языка опросов и аппаратные образы математики

**Статус:** рабочий публикационный черновик RU v0.3  
**Ветка:** \`research/hatter-sol-18-adaptive-word-tomography\`  
**Родительская работа:** HATTER-SOL-17  
**Дата состояния:** 19 сентября 2026

## Аннотация

HATTER-SOL-18 продолжает конечную лабораторию \(PSL(2,7)\), построенную в
HATTER-SOL-17, заменяя фиксированный набор word observers адаптивной программой
опроса. Состояния — simultaneous-conjugacy орбиты ordered pairs \((A,B)\).
На generating locus имеется 114 орбит; полный identify-or-REJECT quotient
\(PSL(2,7)^2\) содержит 197 орбит: 114 generating и 83 non-generating.

Для freely reduced words длины не более четырёх 160 сырых слов индуцируют
50 различных class-valued queries. Точный dynamic-programming certificate
даёт минимальную worst-case adaptive depth

\[
\boxed{D^*(W_4)=4},
\]

тогда как fixed observation в том же пуле требует минимум пять запросов:

\[
\boxed{5_{\rm fixed}\rightarrow4_{\rm adaptive}}.
\]

На 114 generating states минимальная суммарная длина путей depth-four дерева
равна \(382\), то есть

\[
\boxed{\bar D_{\min}=\frac{191}{57}\approx3.350877}.
\]

Nielsen moves на этих 114 состояниях дают четыре connected components размеров

\[
\boxed{36,\ 32,\ 32,\ 14}.
\]

Они в точности являются fibers canonical commutator-lift trace

\[
\tau(A,B)=\operatorname{tr}([\widetilde A,\widetilde B])\in\mathbb F_7
\]

со значениями \(6,4,3,5\). Это связывает H18 decomposition с классическим
Higman invariant.

Далее три projective shadow observations

\[
A^2B^2,\qquad ABAB^{-1},\qquad ABA^{-1}B
\]

восстанавливают \(\tau\) на generating locus, причём три является минимальным
числом \(W_4\)-class queries для этой задачи.

Для одного persistent known query erasure четыре успешных class-ответа всё ещё
достаточны:

\[
\boxed{S_1=4,\qquad A_1=5}.
\]

Наконец, Nielsen structure позволяет сократить глобальный язык запросов:
сначала \(50\to26\), затем найден 12-query alphabet, сохраняющий полный
one-erasure contract. Точная нижняя граница даёт

\[
\boxed{9\le M_1(W_4)\le12},
\]

где \(M_1(W_4)\) — минимальное число globally supported query labels,
достаточное для exact four-successful-answer one-erasure strategy.

При детерминированной рематериализации 12-query strategy число query nodes
уменьшается

\[
308\to305,
\]

а explicit microprogram payload

\[
19057\to18425\text{ bits}.
\]

Отдельный exact shortest-program analysis показывает, что Nielsen semantic
compression не означает автоматического уменьшения числа permutation
compositions: для части primitive words direct execution короче.

Две аппаратные реализации restricted-12 strategy показывают противоположные
точки area/time trade-off. Последовательный H18-LAB-03 на Cyclone IV
EP4CE22F17C6 занимает 5,227 LE и имеет \(F_{\max}=41.28\) MHz, но требует до
42 тактов на transaction. Полностью spatialized H18-LAB-04 разворачивает все
12 observers и 305-node decision DAG в one-cycle combinational core. На том же
22K Cyclone IV он требует 26,332 logic elements и не помещается; на Cyclone V
5CEFA7F23C6 успешно реализуется в 10,627 ALM + 48 DSP с
\(F_{\max}=28.52\) MHz и worst data delay 34.827 ns.

Matched one-cycle comparison с H17-LAB-02 на том же Cyclone V даёт
7,941 ALM + 40 DSP и 35.694 ns для H17 против 10,627 ALM + 48 DSP и
34.827 ns для H18. Таким образом, H18 дороже по площади, но немного быстрее и
мельче по logic depth (30 против 34 levels). На Cyclone IV EP4CE115F29C7
обе схемы, несмотря на различную математику, имеют одинаковые 65 logic levels
и близкие data delays 47.249 ns и 46.516 ns.

Эти измерения мотивируют отдельную H18-12 постановку:
\[
\boxed{
\text{математическое представление}
\to
\text{булева реализация}
\to
\text{technology-relative hardware image}.
}
\]
FPGA здесь используется не как доказательство «абсолютной сложности», а как
фиксированный воспроизводимый физический преобразователь для сравнения
различных конечных математических представлений.

## 1. Постановка

H17 использует фиксированный robust fingerprint. H18 спрашивает, может ли
наблюдатель выбирать следующее слово из уже полученных ответов:

\[
w_1\rightarrow c_1\rightarrow w_2(c_1)\rightarrow c_2\rightarrow\cdots.
\]

Так fixed code превращается в branching interrogation program.

Мы различаем три независимые меры сложности:

1. **transaction complexity** — число ответов на одном пути;
2. **query-alphabet complexity** — число различных запросов, которые машина
   должна поддерживать глобально;
3. **hardware realization complexity** — controller memory, arithmetic,
   logic, routing и latency.

## 2. Конечная модель

Пусть

\[
G=PSL(2,7),\qquad |G|=168.
\]

Для ordered pair \((A,B)\in G^2\) вводится simultaneous conjugacy

\[
(A,B)\sim(hAh^{-1},hBh^{-1}).
\]

Generating pairs дают 114 орбит. Полный quotient всех ordered pairs содержит

\[
\boxed{197=114+83}
\]

орбит; 83 non-generating states имеют общий terminal REJECT.

Для freely reduced words длин \(1,\ldots,4\) имеется

\[
4+12+36+108=160
\]

сырых слов. После дедупликации по exact class-response vector остаётся

\[
\boxed{50}
\]

различных \(W_4\)-queries.

## 3. Exact adaptive depth four

Exact dynamic programming доказывает

\[
\boxed{D^*(W_4)=4}.
\]

Depth three невозможна, depth four достижима.

В том же query pool ни один fixed subset размеров \(1,2,3,4\) не разделяет
все 114 generating states. Пять слов

\[
\boxed{A,\ B,\ AB,\ Ab,\ ABab}
\]

разделяют их, поэтому

\[
\boxed{5_{\rm fixed}\rightarrow4_{\rm adaptive}}.
\]

Для depth-four trees минимальный total path length равен

\[
382,
\]

следовательно,

\[
\boxed{\bar D_{\min}=382/114=191/57}.
\]

Один выбранный optimum имеет 48 внутренних узлов, root \(\texttt{AAB}\);
74 states завершаются на depth 3 и 40 на depth 4.

## 4. Nielsen dynamics

Рассматриваются standard Nielsen moves, включая

\[
S(A,B)=(B,A),\qquad
I_A(A,B)=(A^{-1},B),\qquad
N_A(A,B)=(AB,B).
\]

На 114 generating orbit states соответствующий graph имеет connected
components

\[
\boxed{36,\ 32,\ 32,\ 14}
\]

с diameters

\[
\boxed{7,\ 6,\ 8,\ 4}.
\]

По projective commutator class они имеют вид:

- \(36\) states: \(3A\);
- \(32\) states: \(4A\);
- \(32\) states: \(4A\);
- \(14\) states: \(7A/7B\).

Projective commutator class не различает два 32-state sectors.

## 5. Canonical lift trace и Higman invariant

Выберем determinant-one lifts

\[
\widetilde A,\widetilde B\in SL(2,7).
\]

Коммутатор lift не зависит от знаков lifts, поэтому

\[
\boxed{
\tau(A,B)=\operatorname{tr}([\widetilde A,\widetilde B])
}
\]

корректно определён на projective pair.

На 114 states exact fibers:

\[
\boxed{
\tau=6:36,\qquad
\tau=4:32,\qquad
\tau=3:32,\qquad
\tau=5:14.
}
\]

Каждый fiber совпадает ровно с одним Nielsen connected component.

В частности,

\[
\boxed{
4A^{(+)}:\tau=3,\qquad
4A^{(-)}:\tau=4=-3\pmod7.
}
\]

H18 не заявляет открытие Higman invariant; новый результат — его exact
идентификация внутри H17/H18 state model и связь с adaptive query structure.

## 6. Three-shadow reconstruction theorem

Положим

\[
x=\operatorname{tr}\widetilde A,\qquad
y=\operatorname{tr}\widetilde B,\qquad
z=\operatorname{tr}(\widetilde A\widetilde B).
\]

Fricke identity:

\[
\tau=x^2+y^2+z^2-xyz-2.
\]

Определим

\[
R_z=A^2B^2,\qquad
R_x=ABAB^{-1},\qquad
R_y=ABA^{-1}B.
\]

Тогда

\[
\operatorname{tr}(R_z)=z^2-\tau,
\]

\[
\operatorname{tr}(R_x)=x^2-\tau,
\]

\[
\operatorname{tr}(R_y)=y^2-\tau.
\]

Projective conjugacy class определяет trace-square lift-а. Поэтому classes
трёх shadows восстанавливают \(\tau\) на generating locus.

Exact search по 50 \(W_4\)-queries даёт

\[
\boxed{m_\tau(W_4)=3}.
\]

Ни один single query и ни одна pair не определяют \(\tau\); ровно 16 triples
определяют.

## 7. Persistent known query erasure

Fault model:

- не более одного requested query возвращает ERASED;
- identity неудавшегося query известна;
- этот query запрещён до конца transaction;
- повторять его нельзя.

Для полного 197-state identify-or-REJECT task:

\[
\boxed{D_0=4}
\]

без erasure и

\[
\boxed{S_1=4}
\]

успешных answers при одном persistent erasure.

Следовательно,

\[
\boxed{A_1=5}.
\]

Три успешных ответа невозможны уже в no-erasure model, поэтому successful-query
bound является точным.

## 8. Первая RTL-реализация

H18-07 materializes exact strategy как sequential RTL:

\[
308=69+239
\]

nonterminal query states, 24 distinct word labels, max word length 4, one shared
word datapath и one reused class engine.

Проверенная regression:

\[
\boxed{197\times5=985/985\ \mathrm{PASS}}.
\]

Observed maxima:

\[
\boxed{\text{max attempts}=5,\qquad \text{max RTL wait}=32\text{ cycles}}.
\]

В common generic Yosys methodology:

\[
H17\text{-LAB-03}=13547,
\]

\[
H18\text{-LAB-01}=17205
\]

hierarchy-expanded generic cells. Первая hardwired adaptive implementation
примерно на 27% больше H17 reference. Это implementation result, а не общий
theorem о цене adaptivity.

## 9. Canonical microcoded baseline

H18-08 заменяет hardwired decode на canonical microprogram.

Baseline payload:

\[
1540+16632+621+264
=
\boxed{19057\text{ bits}}.
\]

Direct loading первого letter также уменьшает worst five-attempt arithmetic
bound

\[
19\rightarrow14
\]

permutation compositions без изменения query decision strategy.

H18-08 остаётся baseline 24-query architecture и должен закрываться отдельным
dual-RTL CI.

## 10. Nielsen-normal query compression

Из 50 canonical \(W_4\)-queries ровно 24 являются primitive free-group words,
то есть Nielsen transports координатного observer.

На 114 generating states их joint signature имеет 107 values и оставляет
ровно семь doublets:

\[
\boxed{
(12,27),(13,28),(14,29),(84,89),(90,92),(100,103),(106,107).
}
\]

Это в точности H17 commutator-defect pairs.

Все семь разделяются oriented commutator query \(\texttt{ABab}\). Естественный
restricted pool:

\[
\boxed{
24\text{ primitive}+2\text{ commutator orientations}=26.
}
\]

На нём сохраняются

\[
\boxed{D_0=4,\qquad S_1=4,\qquad A_1=5}
\]

и

\[
\boxed{5_{\rm fixed}\rightarrow4_{\rm adaptive}}.
\]

Generating-only optimum total path length меняется лишь

\[
382\rightarrow386,
\]

то есть mean depth

\[
\frac{191}{57}\rightarrow\frac{193}{57}.
\]

## 11. Глобальный query alphabet

Пусть \(M_1(W_4)\) — minimum number of globally supported query labels,
сохраняющее exact four-successful-answer one-erasure strategy.

Для tolerating one persistent erasure любой supported alphabet обязан иметь
distance at least two на каждой required gen/gen и gen/non state pair.

В полном 50-query pool ровно семь critical pairs имеют только два separating
labels:

\[
\boxed{\texttt{ABab},\qquad\texttt{AbaB}}.
\]

Поэтому обе commutator orientations forced.

После их фиксации size-eight alphabet мог бы добавить только шесть labels из
остальных 48. Полный перебор

\[
\binom{48}{6}=12\,271\,512
\]

вариантов показывает: ни один не удовлетворяет necessary distance-two
condition.

Size-nine distance-two witness существует, следовательно minimum robust
alphabet по coding criterion равен 9.

Для полного adaptive contract найден 12-query witness:

\[
\boxed{
A,B,ABab,AbaB,ABB,Abb,AAb,AAAB,AAAb,Baa,aab,abb.
}
\]

На нём exact DP снова даёт

\[
\boxed{D_0=4,\qquad S_1=4,\qquad A_1=5}.
\]

Поэтому

\[
\boxed{9\le M_1(W_4)\le12}.
\]

## 12. Restricted 12-query controller

После rematerialization exact controller под 12-query alphabet содержит

\[
\boxed{305=67+238}
\]

nonterminal query nodes, вместо

\[
308=69+239.
\]

Все 12 labels реально используются выбранной deterministic strategy.

При canonical 9-bit node address и 4-bit query selector explicit payload:

\[
305\times4=1220
\]

query-selector bits,

\[
305\times6\times9=16470
\]

class-transition bits,

\[
67\times9=603
\]

erasure-transition bits,

\[
12\times11=132
\]

word-descriptor bits.

Итого

\[
\boxed{18425\text{ bits}}.
\]

По сравнению с H18-08:

\[
\boxed{
19057\rightarrow18425
}
\]

или

\[
\boxed{-632\text{ bits}=-3.32\%}.
\]

Сильное сокращение query vocabulary \(24\to12\) даёт умеренное сокращение
payload, потому что dominant term — six-way transition table.

## 13. Nielsen semantic compression не равна arithmetic compression

Для десяти primitive labels 12-query witness вычислены shortest elementary
Nielsen programs.

В seven cases shortest Nielsen cost совпадает с direct \(L-1\) composition cost.
В three cases Nielsen realization требует на один move больше.

Следовательно,

\[
\boxed{
\text{Nielsen semantic compression}
\not\Rightarrow
\text{automatic arithmetic compression}.
}
\]

Это отрицательный, но важный engineering result: дальнейшее hardware
сокращение надо искать в control/transition factoring, а не предполагать
ускорение word datapath из одной лишь Nielsen equivalence.

## 14. Главный структурный вывод

Получена последовательность

\[
50\text{ canonical }W_4\text{ queries}
\]

\[
\Downarrow
\]

\[
24\text{ primitive Nielsen transports}
+
2\text{ commutator orientations}
\]

\[
\Downarrow
\]

\[
12\text{-label adaptive witness},
\]

при неизменном exact worst-case information bound

\[
\boxed{
4\text{ successful answers}
+
1\text{ possible erasure}.
}
\]

Nielsen dynamics и adaptive tomography тем самым становятся одной задачей:
динамика объясняет, как организовать и сокращать сам язык interrogation
program. Но аппаратная реализация показывает следующий уровень: сжатие
семантического языка и сжатие физической схемы являются различными задачами.

## 15. Две аппаратные реализации одной H18-математики

Restricted-12 strategy допускает по крайней мере две точные реализации,
сохраняющие один математический certificate, но по-разному распределяющие
вычисление между временем и пространством.

### 15.1 H18-LAB-03: temporal / microcoded realization

LAB-03 использует:

- один переиспользуемый word engine;
- один переиспользуемый class engine;
- microcoded transition logic;
- последовательное выполнение реально запрошенных observers.

Exhaustive ModelSim regression:

\[
\boxed{
197\text{ states}\times5\text{ schedules}=985\text{ runs}
}
\]

даёт

\[
\boxed{
\text{max attempts}=5,\qquad
\text{max cycles}=42.
}
\]

На Cyclone IV EP4CE22F17C6:

\[
\boxed{5227/22320\text{ LE}=23\%},
\]

\[
\boxed{F_{\max}=41.28\text{ MHz}},
\]

worst data delay равен \(24.510\) ns, reported critical depth — 42 logic
levels. Explicit 18,425-bit controller payload при этом не был автоматически
отображён в block RAM; asynchronous transition access остался logic-dominated.

Смысл этой реализации — temporal reuse: H18 спрашивает только то, что
действительно требуется текущей ветви decision strategy.

### 15.2 H18-LAB-04: fully spatialized combinational realization

LAB-04 сохраняет restricted-12 mathematics, но устраняет sequential query
execution. Его архитектура:

\[
\boxed{
\text{registered inputs}
\to
\text{12 parallel observers}
\to
\text{305-node compiled decision DAG}
\to
\text{registered result}.
}
\]

Shared word-prefix DAG содержит 19 permutation compositions с maximum
composition depth 3. Exact H18-11 decision DAG имеет query depth 5 при учёте
одного возможного erasure.

Fault input в LAB-04 — static identity одного persistently unavailable query.
Это circuit-form того же known-query-erasure semantics: identity erasure
используется только тогда, когда pre-erasure strategy действительно дошла до
соответствующего query.

Exhaustive regression проверяет

\[
\boxed{
197\times(1+12)=2561
}
\]

registered transactions: no erasure и каждая из 12 возможных erased query
identities.

### 15.3 Цена spatialization

На EP4CE22F17C6 LAB-04 требует

\[
\boxed{26332>22320}
\]

logic elements и Fitter возвращает NO FIT. На том же кристалле temporal
LAB-03 занимает 5,227 LE.

Следовательно, перевод одной и той же adaptive mathematics

\[
\Pi_{\rm seq}\to\Pi_{\rm spat}
\]

может обменять cycles на area в очень крупном масштабе. При этом NO FIT —
содержательный capacity result, но не даёт права приписывать LAB-04 routed
\(F_{\max}\) на этом target.

Это первый прямой hardware-урок H18:

\[
\boxed{
\text{adaptive temporal simplicity}
\not\Rightarrow
\text{small spatial circuit}.
}
\]


### 15.4 Cyclone V: чистый same-mathematics architecture control

На 5CEFA7F23C6 обе H18-реализации теперь измерены на одном device/tool/corner.

| quantity | LAB-03 temporal | LAB-04 spatial | spatial/temporal |
| --- | ---: | ---: | ---: |
| ALM | 1,455 | 10,627 | 7.304 |
| DSP blocks | 26 | 48 | 1.846 |
| registers | 211 | 69 | 0.327 |
| \(F_{\max}\) | 47.02 MHz | 28.52 MHz | 0.607 |
| worst data delay | 21.075 ns | 34.827 ns | 1.653 |
| logic levels | 18 | 30 | 1.667 |
| cell delay | 10.227 ns | 13.556 ns | 1.326 |
| routing delay | 10.850 ns | 21.270 ns | 1.960 |
| worst transaction cycles | 42 | 1 | 0.0238 |

LAB-03 critical path:

\[
\texttt{class\_perm[23]}
\to
\texttt{next\_node\_q[4]},
\]

с 10.227 ns cell delay и 10.850 ns routing delay.

При работе каждой architecture на её measured \(F_{\max}\):

\[
T_{\rm temporal}
=
\frac{42}{47.02\text{ MHz}}
\approx0.893\,\mu s,
\]

\[
T_{\rm spatial}
=
\frac{1}{28.52\text{ MHz}}
\approx0.0351\,\mu s.
\]

Следовательно, full spatialization одной и той же H18 mathematics:

\[
\boxed{
A_{\rm spatial}/A_{\rm temporal}\approx7.30
}
\]

по ALM и

\[
\boxed{
T_{\rm temporal}/T_{\rm spatial}\approx25.5.
}
\]

Это особенно важный контроль: здесь математическое представление фиксировано,
а меняется только execution discipline. Поэтому разница не может быть
приписана H17/H18 mathematical-presentation effect.

Одновременно результат показывает, почему \(F_{\max}\) нельзя использовать как
синоним transaction speed. Temporal LAB-03 имеет более высокий \(F_{\max}\)
и более короткий single-cycle path, но проигрывает end-to-end latency из-за
42-cycle schedule.


## 16. H17 против H18: сравнение двух математических представлений

### 16.1 Граница эквивалентности

H17 и H18 не следует называть двумя побитово идентичными RTL одного интерфейса.

В fault-free части они идентифицируют один и тот же конечный объект:
simultaneous-conjugacy orbit ordered pair \((A,B)\), с REJECT для
non-generating pairs.

В fault-tolerant части H17 использует fixed robust fingerprint с known erased
coordinate, тогда как H18 использует adaptive word queries с persistent known
query erasure. Поэтому сравнение относится к уровню

\[
\boxed{\mathrm{E1}:\ \text{common abstract correctness contract}},
\]

а не к более сильному E0 pointwise identity одного Boolean input/output map.

Чтобы сравнивать именно mathematical-presentation effect, используются
one-cycle implementations с одной архитектурной дисциплиной:

\[
\boxed{
\text{input register}
\to
\text{combinational mathematical core}
\to
\text{output register}.
}
\]

Для H17 это LAB-02, для H18 — LAB-04.

### 16.2 Cyclone IV EP4CE22F17C6: capacity boundary

H17-LAB-02 успешно размещается:

\[
19540/22320\text{ LE}=88\%.
\]

H18-LAB-04 требует:

\[
26332/22320\text{ LE}=118\%
\]

и не помещается.

На одной и той же technology point отношение mapping demand составляет

\[
\boxed{
\rho_A^{\rm C4,22K}
\approx
\frac{26332}{19540}
\approx1.348.
}
\]

Это area/density result. Timing ratio на этом target для H18-LAB-04
не существует, поскольку routed fit отсутствует.

### 16.3 Cyclone IV EP4CE115F29C7: matched timing

На просторном Cyclone IV C7 обе one-cycle реализации успешно routed.

| quantity | H17-LAB-02 | H18-LAB-04 |
| --- | ---: | ---: |
| worst data delay | 47.249 ns | 46.516 ns |
| logic levels | 65 | 65 |
| cell delay | 17.092 ns | 15.721 ns |
| routing delay | 29.941 ns | 30.579 ns |
| reciprocal data-delay frequency | 21.16 MHz | 21.50 MHz |

Их total physical depth почти совпадает:

\[
\boxed{65\leftrightarrow65}.
\]

Но внутренняя факторизация различна: H18 имеет примерно на 8% меньший cell
delay и примерно на 2.1% больший routing delay.

Таким образом,

\[
\boxed{
\text{similar scalar delay}
\not\Rightarrow
\text{same internal physical factorization}.
}
\]

Для этого 115K run отдельный extractor дал MAP estimate

[
oxed{26460	ext{ logic elements}}
]

и 69 registers. Это число в статье используется именно как **MAP estimate**,
а не как final fitter utilization: текущий сохранённый вывод не содержит
отдельной final-fit строки, которую можно было бы безопасно отождествить с этим
значением.

### 16.4 Cyclone V 5CEFA7F23C6: второй matched technology point

Cyclone V особенно полезен, потому что Quartus II 13.1 автоматически использует
hard DSP blocks. Поэтому это platform-level comparison, а не ALM-only
comparison.

Measured result:

| quantity | H17-LAB-02 | H18-LAB-04 | H18/H17 |
| --- | ---: | ---: | ---: |
| ALM | 7,941 | 10,627 | 1.338 |
| DSP blocks | 40 | 48 | 1.200 |
| registers | 132 | 69 | 0.523 |
| \(F_{\max}\) | 27.85 MHz | 28.52 MHz | 1.024 |
| worst data delay | 35.694 ns | 34.827 ns | 0.976 |
| logic levels | 34 | 30 | 0.882 |
| cell delay | 12.726 ns | 13.556 ns | 1.065 |
| routing delay | 22.969 ns | 21.270 ns | 0.926 |

H18 тем самым использует примерно на 33.8% больше ALM и на 20% больше DSP,
но имеет примерно на 2.4% меньший worst data delay и на 11.8% меньшую
reported logic depth.

H18 critical path проходит через два inferred DSP blocks; DSP являются
реальной частью физического пути, а не только неиспользованным resource count.

На обоих designs 100 MHz constraint не закрыт; эти результаты используются
как matched comparative physical evidence, а не как board-level timing
signoff.

### 16.5 Что устойчиво между технологиями

Получены две независимые matched technology points.

На Cyclone IV large C7 H17 и H18 почти совпадают по delay и полностью совпадают
по reported logic levels.

На Cyclone V H18 становится заметно глубинно короче, но остаётся дороже по
area/hard-block resources.

Особенно интересна близость area ratios:

\[
1.348\quad\text{(Cyclone IV 22K mapping demand)}
\]

и

\[
1.338\quad\text{(Cyclone V fitted ALM ratio)}.
\]

Это пока лишь cross-technology empirical regularity. Её нельзя объявлять
инвариантом по двум точкам.

Полный physical vector показывает, что H17 и H18 занимают разные точки
area/depth/routing Pareto frontier; одного универсального слова «быстрее» или
«компактнее» недостаточно.

## 17. H18-12: hardware image математического представления

FPGA measurements мотивируют более общую постановку.

Пусть конечная задача задана как

\[
\Phi:X\to Y
\]

или, при fault model, relation

\[
\mathcal R\subseteq X\times F\times Y.
\]

Пусть \(M\) — конечное математическое представление этой задачи:
алгебраические carriers, primitive operations и explicit factorization /
decision program.

После injective finite encoding каждого carrier любая primitive operation
имеет exact Boolean realization. Поэтому существует отображение

\[
\boxed{
M
\xrightarrow{\mathcal B_\Pi}
C_M,
}
\]

где \(\Pi\) фиксирует discipline перевода mathematics в circuit:
разрешённые rewrites, sharing, register boundaries, temporal reuse,
spatialization и fault encoding.

Далее фиксируется technology stack

\[
\Theta=
(\text{device, speed grade, tool, settings, constraints, corner}),
\]

и физический profile

\[
P_\Theta(C)=
(A,R,M,DSP,d_{\rm logic},
t_{\rm cell},t_{\rm route},F_{\max},N_{\rm cyc},T_{\rm tx},\ldots).
\]

### 17.1 Presentation hardware image

Идеальный объект:

\[
\boxed{
H_{\Theta,\Pi}(M)
=
\operatorname{ParetoMin}
\{P_\Theta(C):C\in\mathscr C_\Pi(M)\}.
}
\]

Но один Quartus run не доказывает этот optimum. Поэтому реально измеренная
величина обозначается как witness

\[
\boxed{
\widehat H_{\Theta,\Pi,S}(M)=
P_\Theta(S_{\Theta,\Pi}(M)),
}
\]

где \(S\) — конкретный synthesis/place-and-route flow.

### 17.2 Сложность представления и сложность задачи — разные объекты

Если разрешить synthesis completely forget внутреннюю mathematics и
оптимизировать только flattened truth table \(\Phi\), разные presentations
могут стать неразличимыми.

Поэтому отдельно определяется semantic frontier

\[
H_\Theta^*(\Phi),
\]

где исходное математическое представление забыто.

В общем случае

\[
\boxed{
H_{\Theta,\Pi}(M)\ne H_\Theta^*(\Phi).
}
\]

Именно первое понятие необходимо для вопроса «как различаются две математики
после одинакового отображения в Boolean/physical computation».

### 17.3 Три независимых эффекта

Нужно различать:

\[
\boxed{\text{mathematics effect}}
\]

— меняется \(M\), фиксируются \(\Pi,\Theta\);

\[
\boxed{\text{architecture effect}}
\]

— фиксируется \(M,\Theta\), меняется \(\Pi\);

\[
\boxed{\text{technology effect}}
\]

— фиксируются \(M,\Pi\), меняется \(\Theta\).

В HATTER первые experimental controls уже существуют:

- mathematics: H17-LAB-02 vs H18-LAB-04;
- architecture: H18-LAB-03 vs H18-LAB-04;
- technology: Cyclone IV vs Cyclone V и capacity controls внутри Cyclone IV.

Это превращает FPGA из простой target platform в воспроизводимый
**technology-relative measuring transform**:

\[
\boxed{
\text{mathematics}
\to
\text{Boolean geometry}
\to
\text{physical geometry}.
}
\]

Не утверждается, что FPGA непосредственно измеряет абсолютную математическую
сложность.

## 18. Waveform evidence: две ветви одной adaptive strategy

Для визуальной проверки LAB-04 построен отдельный ModelSim waveform scenario.

Используется certified generating state

\[
\boxed{\text{state}=16}
\]

с

\[
\boxed{A=\texttt{0x5e3b88},\qquad B=\texttt{0x7ecc11}},
\]

expected orbit:

\[
\boxed{0}.
\]

Корневой query restricted-12 strategy:

\[
\boxed{\texttt{AAAB}},
\]

его local hardware word ID равен 8, а class response выбранного state равен 2.

Первая transaction выполняется без erasure. Для root используется ordinary
child

\[
\boxed{\text{node }16}.
\]

Вторая transaction получает static persistent erasure identity

\[
\boxed{\texttt{erase\_valid}=1,\qquad\texttt{erased\_word\_id}=8},
\]

и root переключается на erasure child

\[
\boxed{\text{node }233}.
\]

Поскольку LAB-04 является fully spatialized circuit, normal и erasure
subtrees уже вычисляются комбинационно. Root не «выполняет» их последовательно;
он выбирает между одновременно существующими physical branches.

Для выбранного state обе branches дают

\[
\boxed{\texttt{node\_result}=0x100},
\]

то есть 10-bit encoding

\[
\texttt{status}=2=\mathrm{IDENTIFIED},
\qquad
\texttt{orbit\_id}=0.
\]

На registered output видны два distinct done pulses с одинаковым результатом.

Этот waveform является наглядным hardware witness формулы

\[
\boxed{
\text{same input}
\to
\text{different decision branch}
\to
\text{same certified orbit}.
}
\]

Он также иллюстрирует причину spatialization cost: взаимоисключающие
во времени adaptive futures в LAB-04 существуют одновременно как circuit
structure.

**Figure candidate.** ModelSim waveform H18-LAB-04: two transactions for
state 16, normal root branch node 16 and root-erasure branch node 233, both
returning IDENTIFIED/orbit 0.

## 19. Что доказано, что измерено и что пока является гипотезой

### 19.1 Exact mathematical/certificate results

Доказано или exhaustive-certified:

- 197-state finite quotient \(=114+83\);
- 50 distinct \(W_4\)-queries;
- exact adaptive depth \(D^*=4\);
- strict \(5_{\rm fixed}\to4_{\rm adaptive}\) separation;
- exact minimum mean depth \(191/57\);
- Nielsen components \(36,32,32,14\);
- exact identification этих components с Higman trace fibers;
- three-shadow reconstruction и \(m_\tau(W_4)=3\);
- one-persistent-erasure bounds \(S_1=4,A_1=5\);
- 26-query Nielsen-normal reduction;
- robust-alphabet lower bound 9 и 12-query full adaptive witness;
- restricted controller \(305=67+238\);
- explicit payload 18,425 bits;
- exact shortest Nielsen-program comparison.

### 19.2 Verified implementation results

Проверено:

- H18-LAB-03 exhaustive 985-run temporal RTL regression;
- H18-LAB-03 Cyclone-IV physical fit/timing;
- H18-LAB-04 exhaustive 2561-transaction static-erasure regression;
- H18-LAB-04 Cyclone-IV 22K NO-FIT capacity boundary;
- H18-LAB-04 Cyclone-IV 115K routed timing;
- H18-LAB-04 Cyclone-V routed area/DSP/timing;
- matched H17/H18 one-cycle comparisons на Cyclone IV и Cyclone V;
- interactive ModelSim waveform normal/root-erasure pair.

### 19.3 Non-claims

Не заявляется:

- общий theorem для всех \(PSL(2,q)\);
- exact \(M_1(W_4)\) до closure search для 9,10,11;
- cryptographic hardness;
- physical fault tolerance против произвольных transient hardware faults;
- global optimality FPGA area или delay;
- technology-independent superiority одной mathematics над другой;
- абсолютная математическая complexity из одного Quartus flow;
- pure ALM-only interpretation Cyclone-V result, поскольку используются DSP.

## 20. Воспроизводимость

Основные certificates:

- \`h18_adaptive_depth4_certificate.py\`;
- \`h18_nielsen_dynamics_certificate.py\`;
- \`h18_higman_trace_lift_certificate.py\`;
- \`h18_adaptive_with_tau_certificate.py\`;
- \`h18_three_shadow_higman_decoder.py\`;
- \`h18_adaptive_one_erasure_certificate.py\`;
- \`h18_nielsen_query_compression_certificate.py\`;
- \`h18_query_alphabet_compression_certificate.py\`;
- \`h18_restricted12_controller_certificate.py\`.

Hardware layers:

- H18-LAB-01 — first hardwired adaptive RTL;
- H18-LAB-02 — canonical 24-query microcoded dual-RTL baseline;
- H18-LAB-03 — restricted-12 temporal microcoded FPGA realization;
- H18-LAB-04 — restricted-12 fully spatialized combinational realization.

LAB-04 reproducibility commands include:

\`\`\`powershell
.\tools\run_regression.ps1
.\tools\run_quartus13_115k_c7.ps1
.\tools\run_worst_path_115k_c7.ps1
.\tools\run_quartus13_cyclonev_a7.ps1
.\tools\run_worst_path_cyclonev_a7.ps1
.\tools\run_waveform.ps1
\`\`\`

H18-12 framework:

- \`H18_12_ALGEBRA_TO_PHYSICAL_COMPLEXITY.md\`;
- \`H18_12_MATHEMATICS_COMPARISON_PROTOCOL.md\`.

## 21. Литературная граница и смежные complexity frameworks

Classical Nielsen equivalence, Fricke identity и Higman invariant не являются
результатами H18. H18-specific contribution — их exact finite integration с
adaptive query design, fault-aware compression и hardware realization.

Для algebra-to-hardware interpretation используются как смежные основания:

- straight-line program complexity в arbitrary algebras;
- relative complexity of algebraic presentations/implementations;
- circuits over finite algebraic structures;
- Thompson area-time VLSI complexity;
- FPGA LUT technology mapping.

H18 не утверждает, что эти области ранее не были связаны вообще. Более узкая
исследовательская постановка — использовать fixed Boolean/FPGA realization
discipline как воспроизводимое отображение для сравнительного исследования
различных finite mathematical presentations одного abstract task.

## 22. Следующие шаги перед publication freeze

1. Закрыть
   \[
   M_1(W_4)\in\{9,10,11,12\}.
   \]
2. Архивировать 115K H18 MAP estimate 26,460 отдельно от final-fit claims;
   при необходимости позже извлечь отдельную fitter utilization line.
3. H18-LAB-03/LAB-04 Cyclone-V same-mathematics architecture control — CLOSED.
4. Общий H17/H18 abstract erasure contract — CLOSED как H18-13; в финальном
   тексте сохранять разделение E0 fault-free и E1 fault-tolerant.
5. Проверить устойчивость H17/H18 area ratio ещё на одной technology point или
   при запрещённом DSP inference.
6. Найти первый provable lower bound, связывающий adaptive decision structure
   с Boolean circuit size/depth.
7. После финального bibliography/claim/reproducibility audit собрать RU/EN
   publication PDF.

## References

1. D. McCullough, M. Wanderley, *Nielsen Equivalence of Generating Pairs of
   SL(2,q)*, Glasgow Mathematical Journal 55 (2013), 481–509.
   DOI: 10.1017/S0017089512000675.
2. J. Boschheidgen, B. Klopsch, A. Thillaisundaram, *Generating pairs of
   projective special linear groups that fail to lift*, Mathematische
   Nachrichten 293 (2020). DOI: 10.1002/mana.201900354.
3. N. A. Lynch, *Straight-line program length as a parameter for complexity
   analysis*, Journal of Computer and System Sciences 21(3), 1980.
   DOI: 10.1016/0022-0000(80)90024-0.
4. N. A. Lynch, E. K. Blum, *Relative Complexity of Algebras*,
   Mathematical Systems Theory 14 (1981). DOI: 10.1007/BF01752396.
5. H. Ehrig, B. Mahr, *Complexity of algebraic implementations for abstract
   data types*, Journal of Computer and System Sciences 23(2), 1981.
   DOI: 10.1016/0022-0000(81)90014-3.
6. C. D. Thompson, *Area-Time Complexity for VLSI*, STOC 1979.
   DOI: 10.1145/800135.804401.
7. J. Cong, E. Ding, *FlowMap: An Optimal Technology Mapping Algorithm for
   Delay Optimization in Lookup-Table Based FPGA Designs*, IEEE TCAD 13(1),
   1994. DOI: 10.1109/43.273754.
8. P. Kawałek, J. Krzaczkowski, *Complexity Classes Arising from Circuits over
   Finite Algebraic Structures*, LICS 2026.
   DOI: 10.4230/LIPIcs.LICS.2026.61.
9. HATTER-SOL-17 repository and DOI materials.
