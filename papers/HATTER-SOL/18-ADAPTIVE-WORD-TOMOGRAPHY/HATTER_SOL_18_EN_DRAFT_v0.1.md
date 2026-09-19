# HATTER-SOL-18
# Adaptive Non-Abelian Tomography: When the Next Word Is Chosen by the Previous Observation

**Status:** publication working draft EN v0.1  
**Ветка:** `research/hatter-sol-18-adaptive-word-tomography`  
**Родитель:** HATTER-SOL-17

## Editorial note

This English draft is synchronized structurally with the Russian publication draft. HATTER-SOL-18 continues the finite mathematical/hardware laboratory
(PSL(2,7)), established in HATTER-SOL-17 by replacing a fixed observer family with an adaptive interrogation program.

Состояния — simultaneous-conjugacy орбиты упорядоченных пар ((A,B)). Для
порождающих пар имеется 114 орбит. Для полного identify-or-REJECT контракта
учитываются все 197 орбит пар в (PSL(2,7)^2): 114 generating и 83
non-generating.

Для class-valued observers, задаваемых freely reduced words длины не более
четырёх, 160 сырых слов индуцируют 50 различных запросов. Точный
dynamic-programming certificate показывает, что минимальная worst-case
adaptive depth равна четырём, тогда как fixed observation требует минимум
пять запросов в том же пуле:

[
oxed{5_{m fixed}	o4_{m adaptive}}.
]

Минимальная суммарная длина путей depth-4 дерева на 114 generating states равна
382, поэтому оптимальная средняя глубина равна

[
rac{191}{57}approx3.350877.
]

На пространстве 114 generating-orbits стандартные Nielsen moves порождают
четыре компонента размеров

[
36, 32, 32, 14.
]

Они в точности являются слоями canonical commutator-lift trace

[
	au(A,B)=operatorname{tr}([widetilde A,widetilde B])inmathbb F_7
]

со значениями (6,4,3,5). Тем самым расщепление двух projective (4A)-секторов
на (32+32) связывается с классическим Higman invariant.

Далее доказывается three-shadow theorem: три projective class observations

[
A^2B^2,qquad ABAB^{-1},qquad ABA^{-1}B
]

восстанавливают (	au) на generating locus, и три является минимальным
числом (W_4)-наблюдений для этой задачи.

При одном persistent known query erasure четыре успешных class-ответа всё ещё
достаточны, поэтому worst-case число попыток равно пяти:

[
oxed{S_1=4,qquad A_1=5}.
]

Наконец, Nielsen structure позволяет существенно сократить глобальный словарь
опросов. Сначала полный 50-query пул уменьшается до 26 queries =
24 primitive Nielsen-coordinate observers + две ориентации commutator без
изменения worst-case adaptive bounds. Затем найден 12-query alphabet,
сохраняющий полный one-erasure контракт. Точная exhaustive lower bound даёт

[
oxed{9le M_1(W_4)le12},
]

где (M_1(W_4)) — минимальное число globally supported query labels,
достаточное для exact four-successful-answer one-erasure strategy.

Работа связывает adaptive decision trees, Nielsen dynamics, Fricke trace
geometry и последовательную RTL-архитектуру. Аппаратные результаты
рассматриваются как отдельный engineering layer и не подменяют математические
теоремы.

## 1. From a fixed fingerprint to an interrogation program

H17 показал, что восемь специально выбранных class-valued word observers
образуют robust fingerprint, допускающий восстановление одной известной
стёртой координаты.

H18 меняет постановку. Вместо вычисления всех probes заранее наблюдатель
выбирает следующее слово по уже полученному class result:

[
w_1	o c_1	o w_2(c_1)	o c_2	ocdots.
]

Следовательно, семейство групповых слов становится не только кодом, но и
branching program.

Основные сложности теперь разделяются на три уровня:

1. **transaction complexity** — сколько ответов нужно конкретному состоянию;
2. **query-alphabet complexity** — сколько различных labels должна поддерживать
   машина глобально;
3. **hardware realization complexity** — сколько памяти, логики, циклов и
   маршрутизации стоит такое ветвление.

H18 рассматривает эти уровни раздельно.

## 2. Finite model

Пусть

[
G=PSL(2,7),qquad |G|=168.
]

Элемент реализуется как перестановка восьми точек (mathbb P^1(mathbb F_7)).

Для пары ((A,B)in G^2) рассматривается simultaneous conjugacy:

[
(A,B)sim(hAh^{-1},hBh^{-1}).
]

Порождающие пары дают 114 орбит. Полный quotient всех ordered pairs содержит

[
oxed{197=114+83}
]

орбит, где 83 non-generating states объединяются терминальным ответом REJECT.

Для freely reduced words длины (1,dots,4) имеется

[
4+12+36+108=160
]

сырых слов. После дедупликации по exact class-response vector на конечной
модели остаётся

[
oxed{50}
]

различных class queries.

## 3. Exact adaptive depth-four theorem

Для query pool (mathcal W_4) точный dynamic programming даёт

[
oxed{D^*(mathcal W_4)=4}.
]

Depth three невозможна, depth four достижима.

В том же query pool никакой fixed subset размеров 1–4 не разделяет все 114
generating states. Пять слов

[
A, B, AB, Ab, ABab
]

дают separating fixed family.

Следовательно,

[
oxed{5_{m fixed}	o4_{m adaptive}}.
]

Среди depth-four trees минимальная суммарная state-path length равна

[
382,
]

а mean depth

[
oxed{ar D_{min}=191/57}.
]

Один выбранный optimum имеет 48 внутренних узлов, root (	exttt{AAB}),
74 состояния завершаются на depth 3 и 40 на depth 4.

## 4. Nielsen dynamics

Рассматриваются moves

[
S(A,B)=(B,A),qquad I_A(A,B)=(A^{-1},B),
]

[
N_A(A,B)=(AB,B),
]

и эквивалентные элементарные Nielsen transformations.

На 114 H17 states получаются connected components

[
oxed{36, 32, 32, 14}
]

с diameters

[
7, 6, 8, 4.
]

По projective commutator class они имеют распределение:

- 36 states: (3A);
- 32 states: (4A);
- 32 states: (4A);
- 14 states: (7A/7B).

Обычный PSL commutator class не различает два 32-state worlds.

## 5. Higman trace and the canonical lift

Выберем lifts

[
widetilde A,widetilde Bin SL(2,7).
]

Коммутатор lift не зависит от знаков lifts, поэтому

[
oxed{	au(A,B)=operatorname{tr}([widetilde A,widetilde B])}
]

корректно определён на projective pair.

На 114 states:

[
	au=6:36,qquad
	au=4:32,qquad
	au=3:32,qquad
	au=5:14.
]

Каждый (	au)-fiber совпадает ровно с одним Nielsen component.

Особенно:

[
4A^{(+)}:	au=3,qquad
4A^{(-)}:	au=4=-3pmod7.
]

Это идентифицирует наблюдавшееся H18 расщепление с classical
Higman/commutator-trace invariant, а не объявляет новый общий invariant.

## 6. Three-shadow reconstruction theorem

Пусть

[
x=operatorname{tr}widetilde A,quad
y=operatorname{tr}widetilde B,quad
z=operatorname{tr}(widetilde Awidetilde B).
]

Fricke identity:

[
	au=x^2+y^2+z^2-xyz-2.
]

Определим

[
R_z=A^2B^2,qquad
R_x=ABAB^{-1},qquad
R_y=ABA^{-1}B.
]

Тогда

[
operatorname{tr}(R_z)=z^2-	au,
]

[
operatorname{tr}(R_x)=x^2-	au,
]

[
operatorname{tr}(R_y)=y^2-	au.
]

Projective conjugacy class определяет trace-square lift-а. Поэтому классы трёх
shadow words восстанавливают (	au) на generating locus.

Точный поиск по 50 W4 observers показывает:

[
oxed{m_	au(W_4)=3}.
]

Ни один одинарный или двойной набор class queries не определяет (	au), а 16
различных triples определяют.

Это связывает projective word observations с SL(2,7) lift geometry.

## 7. Persistent known query erasure

Fault model:

- не более одного requested query возвращает ERASED;
- его identity известна;
- тот же query запрещён до конца transaction;
- повторять стёртый запрос нельзя.

Для полного 197-state identify-or-REJECT problem точный результат:

[
oxed{D_0=4}
]

без erasure и

[
oxed{S_1=4}
]

успешных ответов при одном persistent erasure.

Следовательно,

[
oxed{A_1=5}.
]

Это строгий adaptive аналог H17 known-coordinate erasure, но output contracts
различаются: H17 восстанавливает fixed robust fingerprint, H18 идентифицирует
orbit или выдаёт REJECT.

## 8. First RTL realization

H18-07 материализует exact strategy в sequential RTL:

- 308 nonterminal query states;
- 69 pre-erasure;
- 239 post-erasure;
- 24 distinct query labels;
- maximum word length 4;
- one shared word datapath;
- one reused class engine.

Проверенная regression:

[
197	imes5=985/985 {m PASS}.
]

Observed RTL maximum:

[
5	ext{ attempts},qquad32	ext{ cycles}.
]

Common generic Yosys methodology дала:

[
H17	ext{-LAB-03}=13547,
]

[
H18	ext{-LAB-01}=17205
]

hierarchy-expanded generic cells.

То есть первая hardwired adaptive implementation была приблизительно на 27%
больше H17 reference. Это engineering result текущей реализации, не общий
theorem против adaptivity.

## 9. Microcoded representation

H18-08 заменяет hardwired 308-node decode на canonical microprogram.

Program payload до vendor-specific packing:

[
1540+16632+621+264
=
oxed{19057	ext{ bits}}.
]

Кроме того, direct loading первого letter уменьшает worst five-attempt word
composition bound

[
19	o14.
]

Этот слой меняет representation, но не математическую decision strategy.

## 10. Nielsen-normal query compression

Из 50 canonical W4 queries ровно 24 являются primitive free-group words и
конструктивно получаются Nielsen transformations координатного generator.

На 114 generating states эти 24 primitive observers дают 107 signatures и
оставляют ровно семь doublets:

[
(12,27),(13,28),(14,29),(84,89),(90,92),(100,103),(106,107).
]

Это те же H17 commutator-defect pairs.

Они все разделяются oriented commutator query (	exttt{ABab}). Естественная
Nielsen-normal family:

[
24	ext{ primitive}+2	ext{ commutator orientations}=26.
]

На этом сокращённом пуле всё ещё:

[
D_0=4,qquad S_1=4,qquad A_1=5,
]

и сохраняется

[
5_{m fixed}	o4_{m adaptive}.
]

Для generating-only оптимального дерева total path length становится 386
вместо 382:

[
rac{193}{57}approx3.385965
]

против (191/57). Worst-case depth остаётся 4.

## 11. Global query-alphabet theorem

Следующий вопрос: сколько query labels вообще обязана поддерживать машина?

Для одного persistent erasure любой supported alphabet должен иметь
coordinate distance не меньше двух на каждой required gen/gen и gen/non паре.

В полном W4 pool семь critical pairs имеют только два separating labels:

[
	exttt{ABab},qquad	exttt{AbaB}.
]

Значит обе commutator orientations обязательны.

После их фиксации size-eight alphabet мог бы добавить только шесть из остальных
48 labels. Полный перебор

[
inom{48}{6}=12,271,512
]

вариантов показывает: ни один не достигает требуемого distance two.

Однако size-nine distance-two witness существует.

Следовательно, minimum robust alphabet size по distance criterion равен 9.

Для полного four-successful-answer adaptive contract найден 12-query witness:

[
oxed{
A,B,ABab,AbaB,ABB,Abb,AAb,AAAB,AAAb,Baa,aab,abb.
}
]

Для него exact DP снова даёт

[
D_0=4,quad S_1=4,quad A_1=5.
]

Поэтому

[
oxed{9le M_1(W_4)le12}.
]

Определение точного (M_1in{9,10,11,12}) остаётся следующим узким theorem
target.

## 12. Main structural conclusion

H18 начинает с 50 unrelated-looking short-word queries, но постепенно выявляет
меньшую структуру:

[
50	ext{ W4 observers}
]

[
Downarrow
]

[
24	ext{ primitive Nielsen transports}+2	ext{ commutator orientations}
]

[
Downarrow
]

[
12	ext{-label adaptive witness}
]

при сохранении exact worst-case information bound

[
oxed{4	ext{ successful answers}+1	ext{ possible erasure}.}
]

Это показывает, что adaptivity и Nielsen dynamics не являются двумя
параллельными темами. Nielsen geometry объясняет, как сокращать сам язык
опросной программы.

## 13. Claim boundaries

Доказано/сертифицировано:

- exact finite state counts;
- adaptive depth four;
- fixed/adaptive separation;
- Nielsen component decomposition;
- identification components with Higman trace fibers;
- three-shadow reconstruction of (	au);
- one persistent known erasure bound;
- finite RTL regression H18-07;
- generic synthesis comparison H17/H18;
- Nielsen-normal 26-query reduction;
- exact query-alphabet bracket (9le M_1le12).

Не заявляется:

- общий theorem для всех (PSL(2,q));
- cryptographic hardness;
- physical fault tolerance;
- target FPGA superiority H18 over H17;
- exact value (M_1) до закрытия следующего finite search;
- measured power/Fmax/board behavior для H18.

## 14. Reproducibility

Основные certificates:

- `h18_adaptive_depth4_certificate.py`;
- `h18_nielsen_dynamics_certificate.py`;
- `h18_higman_trace_lift_certificate.py`;
- `h18_adaptive_with_tau_certificate.py`;
- `h18_three_shadow_higman_decoder.py`;
- `h18_adaptive_one_erasure_certificate.py`;
- `h18_nielsen_query_compression_certificate.py`;
- `h18_query_alphabet_compression_certificate.py`.

Аппаратные слои:

- H18-LAB-01 adaptive RTL;
- H18-LAB-02 canonical microcoded dual RTL.

## 15. Literature boundary

Классическая Nielsen equivalence и Higman invariant не являются результатами
H18. McCullough и Wanderley систематически исследуют Nielsen equivalence
generating pairs of (SL(2,q)) и (PSL(2,q)), где Higman invariant и trace
commutator играют центральную роль.

H18-specific contribution состоит в exact finite connection:

[
	ext{Nielsen dynamics}
leftrightarrow
	ext{adaptive word tomography}
leftrightarrow
	ext{Fricke/Higman reconstruction}
leftrightarrow
	ext{query-program compression}
leftrightarrow
	ext{RTL}.
]

## 16. Remaining theorem targets before publication freeze

1. Закрыть точное значение
   [
   M_1(W_4)in{9,10,11,12}.
   ]
2. Проверить, существует ли cost-optimal adaptive tree одновременно
   минимизирующий global alphabet и total path length.
3. Сравнить direct-word и Nielsen-microprogram arithmetic cost, не предполагая
   заранее, что Nielsen representation дешевле.
4. Закрыть H18-08 dual-RTL CI.
5. После этого провести final publication audit и собрать RU/EN PDF.

## References

1. D. McCullough, M. Wanderley, *Nielsen Equivalence of Generating Pairs of
   SL(2,q)*, Glasgow Mathematical Journal 55 (2013), 481–509.
   DOI: 10.1017/S0017089512000675.
2. J. Boschheidgen, B. Klopsch, A. Thillaisundaram, *Generating pairs of
   projective special linear groups that fail to lift*, Mathematische
   Nachrichten 293 (2020). DOI: 10.1002/mana.201900354.
3. HATTER-SOL-17 repository and DOI materials.
