# HATTER-SOL-18
# Адаптивная неабелева томография: Nielsen dynamics, Higman trace и сжатие языка опросов

**Статус:** рабочий публикационный черновик RU v0.2  
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
program.

## 15. Границы claims

Доказано/сертифицировано:

- exact finite state counts;
- exact adaptive depth four;
- strict fixed/adaptive separation;
- exact Nielsen component decomposition;
- identification with Higman trace fibers;
- three-shadow reconstruction and \(m_\tau(W_4)=3\);
- exact persistent-one-erasure bound;
- H18-07 RTL regression;
- generic H17/H18 synthesis comparison;
- 26-query Nielsen-normal reduction;
- \(9\le M_1(W_4)\le12\);
- 305-node restricted controller;
- explicit 18,425-bit restricted program count;
- exact shortest Nielsen programs for the ten primitive labels.

Не заявляется:

- общий theorem для всех \(PSL(2,q)\);
- exact \(M_1\) до отдельного exhaustive closure;
- cryptographic hardness;
- physical fault tolerance;
- target-FPGA superiority H18 over H17;
- lower LUT/ALM/BRAM/Fmax/power для 12-query architecture до target synthesis.

## 16. Воспроизводимость

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

- H18-LAB-01 adaptive hardwired RTL;
- H18-LAB-02 canonical 24-query microcoded dual RTL;
- restricted 12-query successor architecture from H18-11.

## 17. Литературная граница

Classical Nielsen equivalence и Higman invariant не являются результатами H18.
McCullough и Wanderley исследуют Nielsen equivalence generating pairs of
\(SL(2,q)\) и \(PSL(2,q)\); commutator trace является классическим invariant.

H18-specific contribution — exact finite chain

\[
\boxed{
\text{Nielsen dynamics}
\leftrightarrow
\text{adaptive word tomography}
\leftrightarrow
\text{Fricke/Higman reconstruction}
\leftrightarrow
\text{query-language compression}
\leftrightarrow
\text{RTL}.
}
\]

## 18. Следующие шаги перед publication freeze

1. Закрыть точное
   \[
   M_1(W_4)\in\{9,10,11,12\}.
   \]
2. Закрыть baseline H18-08 dual-RTL CI.
3. Реализовать restricted 12-query microcoded RTL как отдельный successor
   experiment.
4. Исследовать factoring six-way transition table под Nielsen/Higman symmetry.
5. Провести финальный theorem/claim/reproducibility audit.
6. Собрать RU/EN publication PDF только после этих gates.

## References

1. D. McCullough, M. Wanderley, *Nielsen Equivalence of Generating Pairs of
   SL(2,q)*, Glasgow Mathematical Journal 55 (2013), 481–509.
   DOI: 10.1017/S0017089512000675.
2. J. Boschheidgen, B. Klopsch, A. Thillaisundaram, *Generating pairs of
   projective special linear groups that fail to lift*, Mathematische
   Nachrichten 293 (2020). DOI: 10.1002/mana.201900354.
3. HATTER-SOL-17 repository and DOI materials.
