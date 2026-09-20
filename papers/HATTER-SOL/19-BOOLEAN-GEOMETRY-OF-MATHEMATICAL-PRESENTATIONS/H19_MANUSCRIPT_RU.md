# HATTER-SOL-19
# Булева геометрия математических представлений
## Наблюдаемость, скрытие и повторное проявление структуры в компиляции и FPGA-реализации

**Автор:** Alex Malachevsky  
**AI research collaborator:** Commander Sol · Hatter Sol  
**Серия:** HATTER-SOL  
**Статус:** рукопись-кандидат  
**Дата:** 20 сентября 2026 г.

---

## Аннотация

Рассматривается конечное семейство математически мотивированных представлений одной и той же вычислительной задачи и исследуется, какие различия между этими представлениями сохраняются, скрываются и вновь проявляются при переходе от исходной факторизации к Boolean RTL, синтезу, generic technology mapping и физической FPGA-реализации.

В качестве контролируемого семейства используются три E0-эквивалентных представления одного и того же H18 restricted-12 контракта:

[
D=\mathrm{DIRECT12},qquad
P=\mathrm{PREFIX19},qquad
N=\mathrm{NIELSEN12}.
]

Они имеют одинаковую семантику, одинаковый 305-узловой decision DAG, одинаковую внешнюю fault-модель, одинаковую зарегистрированную оболочку и один и тот же 2561-векторный функциональный regression contract, но различаются исходной математической факторизацией.

Для фиксированного compiler stage и наблюдателя (O) вводится индуцированное отношение эквивалентности

[
M_asim_O M_b
iff
O(C(M_a))=O(C(M_b)),
]

а для конечного семейства — соответствующее разбиение презентаций. Это позволяет описывать compiler/physical behavior не одним скаляром площади или частоты, а траекторией разбиений и фронтов наблюдаемости.

На generic Yosys flow DIRECT12 и PREFIX19 сначала различимы на source-level, затем совпадают по cell histogram после `proc/opt` и `techmap`, затем вновь различаются после `abc -fast`. При этом полный compiler state не обязан сливаться: детерминированность даёт no-resurrection theorem для точного состояния, поэтому поздняя повторная различимость свидетельствует о более раннем скрытом различии.

На Cyclone V (Quartus II 13.1, 5CEFA7F23C6) joint measured physical profile даёт

[
{{D,P},{N}},
]

причём DIRECT12 и PREFIX19 совпадают по всем восьми заранее объявленным физическим координатам: ALM, registers, DSP, Fmax, data delay, logic levels, cell delay и routing delay.

Независимая репликация на Gowin GW5A-25A (Gowin Education IDE 1.9.9Beta-4) даёт тот же measured post-P&R quotient

[
oxed{
{{D,P},{N}}.
}
]

Тем самым получен первый в серии HATTER-SOL контролируемый cross-vendor пример, в котором различие математических представлений наблюдатель-зависимо: оно видно в одном compiler image, скрыто в другом и вновь склеивается в двух независимых physical FPGA observers. Работа не утверждает универсальную technology-independence, равенство routed netlists или новые нижние оценки Boolean circuit complexity.

---

## 1. Постановка задачи

Стандартная постановка аппаратного синтеза обычно фиксирует вычисляемую функцию и затем оптимизирует её аппаратное представление.

В HATTER-SOL-19 фиксируется другая ось исследования:

> одна и та же конечная семантика может иметь несколько математически естественных представлений, и компилятор/FPGA-реализация может видеть эти представления по-разному.

Мы рассматриваем цепочку

[
M
longrightarrow
B_Pi(M)
longrightarrow
S_Theta(B_Pi(M))
longrightarrow
P_Theta(M),
]

где

- (M) — математическое представление;
- (B_Pi) — presentation-aware Booleanization discipline;
- (S_Theta) — compiler / synthesis / technology mapping / place-and-route;
- (P_Theta) — измеряемый physical profile.

Центральный вопрос:

[
oxed{
	ext{какие различия математического представления переживают}
atop
	ext{Booleanization, synthesis и physical mapping?}
}
]

Важно, что слово «переживают» здесь всегда относится к **конкретному наблюдателю**.

Равенство по числу LUT не означает равенство netlist.
Равенство по cell histogram не означает равенство compiler state.
Равенство по набору P&R summary coordinates не означает равенство routed database или bitstream.

---

## 2. Конечное адаптивное представление

Пусть

[
M=(X,Y,Q,G,lambda,delta,omega)
]

— конечное адаптивное представление, где

- (X) — конечное множество входных состояний;
- (Y) — конечное множество выходов;
- (Q={q_1,dots,q_m}) — конечное семейство наблюдателей;
- (G) — конечный корневой decision DAG;
- (lambda) назначает observer каждому нетерминальному узлу;
- (delta) задаёт переход по ответу observer;
- (omega) задаёт terminal output.

Индуцированная семантика есть функция

[
Phi_M:X	o Y.
]

Если фиксирована fault model (F), то вход можно расширить до (X	imes F).

В H19 сравниваются только представления с одним и тем же внешним E0-контрактом.

---

## 3. Временная и пространственная реализация

### 3.1. Temporal realization

Каноническая временная реализация хранит текущий node/state ID, вычисляет только observer, требуемый текущим узлом, принимает ответ и переходит к следующему состоянию.

Временной ресурс определяется:

- длиной adaptive path;
- временем observer evaluation;
- controller/state-update latency;
- fault schedule.

### 3.2. Spatial realization

При полной пространственной реализации поддерживаемые observer values вычисляются параллельно, а decision DAG превращается в сеть combinational selectors.

В этом случае взаимоисключающие будущие ветви adaptive computation сосуществуют физически.

Следовательно,

[
oxed{
D_{m query}

eq
D_{m Boolean}

eq
L_{m transaction}.
}
]

Эта граница принципиальна для всей работы.

---

## 4. Presentation-preserving compiled-DAG discipline

Фиксируется дисциплина (Pi_{m DAG}):

1. каждый используемый observer инстанцируется один раз;
2. observer output может fan-out во все DAG nodes с тем же observer label;
3. каждый нетерминальный DAG node реализуется одним selector;
4. одинаковые DAG nodes разделяются ровно так, как в исходном DAG;
5. запрещено считать последующую algebraic flattening частью исходного математического представления;
6. внешние input/output encodings фиксированы.

При такой дисциплине до downstream rewriting generated structural size имеет вид

[
S_{m gen}(M)=
sum_{q_iin Q_{m used}}S(q_i)
+
sum_{vin V_{m nt}}s_{m sel}(r_v,b)
+
S_{m shell}.
]

Это точное construction accounting внутри объявленной compiler discipline.

Это **не** нижняя оценка минимальной Boolean circuit complexity функции (Phi_M).

---

## 5. Контролируемое E0-семейство

Исследуется семейство

[
mathcal F={D,P,N}
]

из трёх представлений одной restricted-12 задачи H18.

### 5.1. DIRECT12

Каждый из 12 observer words вычисляется непосредственно.

Source profile:

[
oxed{24 	ext{permutation-composition nodes}}
]

с maximum composition depth

[
oxed{3}.
]

### 5.2. PREFIX19

Общие префиксы observer words разделяются глобально.

Source profile:

[
oxed{19 	ext{shared composition nodes}}
]

при том же maximum depth

[
oxed{3}.
]

То есть исходное algebraic sharing даёт точное

[
24	o19.
]

### 5.3. NIELSEN12

Примитивные observer words строятся через elementary Nielsen programmes; commutator observers сохраняются прямыми.

Профиль первого mixed presentation:

[
18	ext{ shear}
+
3	ext{ inverse}
+
6	ext{ direct commutator compositions}.
]

Scalar sum 27 не интерпретируется как gate count, поскольку операции гетерогенны.

---

## 6. Функциональная эквивалентность

Все три RTL-варианта генерируются одним H19 generator и используют:

- один и тот же 305-node H18 decision DAG;
- одинаковый static erasure interface;
- одинаковую registered shell;
- одинаковый 2561-transaction regression contract.

Все три проходят один и тот же exhaustive regression.

Следовательно, дальнейшие различия трактуются как различия **presentation image**, а не semantics.

---

## 7. Наблюдатели и индуцированные эквивалентности

Пусть (C_i(M)) — состояние реализации/компиляции presentation (M) на стадии (i).

Наблюдатель есть отображение

[
O:C_i	o Z_O.
]

Определим

[
M_asim_{i,O}M_b
iff
O(C_i(M_a))=O(C_i(M_b)).
]

Для конечного семейства (mathcal F) получаем partition

[
oxed{
mathcal P_{i,O}
=
mathcal F/{sim_{i,O}}.
}
]

В H19 именно эта partition является основным объектом экспериментального сравнения.

---

## 8. Refinement наблюдателей

Пишем

[
O_apreceq O_b,
]

если существует (f), такое что

[
O_a=fcirc O_b.
]

Тогда (O_b) не менее различающий, чем (O_a).

Отсюда немедленно:

[
O_apreceq O_b
Longrightarrow
mathcal P_{i,O_a}
preceq
mathcal P_{i,O_b}.
]

Для фиксированной пары presentations visibility functional

[

u_i(O)=
mathbf 1[
O(C_i(M_1))
eq O(C_i(M_2))
]
]

монотонна по refinement observer.

Это элементарное order-theoretic свойство и само по себе не заявляется как новизна.

---

## 9. Joint observers

Для двух observables

[
O_aee O_b:xmapsto(O_a(x),O_b(x)).
]

Тогда

[

u_i(O_aee O_b)
=

u_i(O_a)lor
u_i(O_b).
]

Для физического эксперимента joint observer есть кортеж всех заранее объявленных summary coordinates, которые успешно извлечены для всего семейства.

Joint observer не отождествляется с full implementation database.

---

## 10. No-resurrection theorem для полного compiler state

Пусть compiler tower детерминирован:

[
C_{i+1}(M)=F_i(C_i(M)).
]

Определим exact-state visibility

[
eta_i=
mathbf 1[
C_i(M_1)
eq C_i(M_2)
].
]

Тогда

[
oxed{
eta_i=0Longrightarroweta_{i+1}=0.
}
]

Доказательство тривиально: одинаковый вход детерминированного (F_i) даёт одинаковый выход.

Следовательно full-state survival word не может содержать переход

[
0	o1.
]

Это означает:

> если поздний stage снова различает две presentations, то ранние complete states уже различались; различие было скрыто coarse observer, а не уничтожено.

---

## 11. Compiler forgetting как observer hiding

Для DIRECT12 и PREFIX19 source-level composition count различается:

[
24
eq19.
]

Но после Yosys 0.33

[
	exttt{proc}	o	exttt{flatten}	o	exttt{opt}
]

получено

[
D=4919,qquad P=4919
]

cells с совпадающим reported cell histogram.

После generic `techmap`:

[
D=63719,qquad P=63719
]

и cell histogram снова совпадает.

Однако wire totals различаются:

[
7732
eq7582
]

после post-proc и

[
17674
eq17531
]

после post-techmap.

Поэтому корректная формулировка:

[
oxed{
	ext{cell-observer hiding}

eq
	ext{exact compiler-state merge}.
}
]

---

## 12. Re-separation после ABC-fast

После matched Yosys `abc -fast`:

[
D=60374,
qquad
P=60383,
qquad
N=68406.
]

Все три total-cell counts различаются.

Для D/P получаем coarse survival word

[
oxed{
W_{m coarse}(D,P)=1001
}
]

по стадиям

[
	ext{source}
	o
	ext{post-proc}
	o
	ext{post-techmap}
	o
	ext{ABC-fast}.
]

Но full-state word на измеренном участке равен

[
oxed{
W_{m full}(D,P)=1111,
}
]

поскольку поздняя ABC-различимость ретроспективно запрещает exact-state equality на более ранних детерминированных стадиях.

---

## 13. Visibility frontier

Для конечного observer poset определим

[
partialmathcal V_i
=
min{O:
u_i(O)=1}.
]

Для пары D/P минимальный видимый observer в измеренном open-flow мигрирует как

[
oxed{
O_{m comp}
	o
O_{m wiretot}
	o
O_{m wiretot}
	o
O_{m celltot}.
}
]

Это даёт более информативное описание compiler behavior, чем один resource scalar.

---

## 14. Presentation-partition trajectory

Для всего семейства (mathcal F={D,P,N}) cell-oriented compiler observers дают:

### post-proc

[
oxed{
mathcal P_{m proc}
=
{{D,P},{N}}.
}
]

### post-techmap

[
oxed{
mathcal P_{m techmap}
=
{{D,P},{N}}.
}
]

### ABC-fast

[
oxed{
mathcal P_{m ABC}
=
{{D},{P},{N}}.
}
]

Таким образом coarse observer partition может refine или coarsen между compiler stages.

Это не противоречит no-resurrection theorem, который относится к complete state.

---

## 15. Latent partition gap

Пусть

[
mathcal P_i^{m full}
]

— partition по complete compiler state, а

[
mathcal P_i^O
]

— partition по observer (O).

Всегда

[
mathcal P_i^{m full}
preceq
mathcal P_i^O.
]

Определим hidden-pair count

[
Q(mathcal P)
=
sum_{Binmathcal P}inom{|B|}{2}
]

и latent gap

[
L_i(O)
=
Q(mathcal P_i^O)
-
Q(mathcal P_i^{m full}).
]

Для cell observer в H19 получено:

[
oxed{
L_{m cellhist}:1	o1	o0.
}
]

Это точная конечная формализация наблюдаемого hiding/re-exposure.

---

## 16. Почему теория H19 не сводится к partition lattice

Partition lattice, observational equivalence, decision trees, branching programs, compiler correctness и equality saturation являются известными областями.

Поэтому H19 не заявляет новизну для:

- существования partition lattice;
- observer refinement;
- pullback equivalence;
- decision-tree/circuit separation;
- semantic preservation;
- phase ordering;
- e-graphs.

H19-specific объект уже:

[
oxed{
(i,Pi,O)
longmapsto
mathcal P_{i,Pi,O}
}
]

для **математически мотивированного, функционально замороженного семейства**, реально проходящего compiler и FPGA flows.

---

# Часть II. Аппаратные лаборатории

## 17. H19-LAB-01: Cyclone V

### 17.1. Цель

Проверить, сохраняется ли compiler-visible presentation distinction после полного FPGA synthesis/place-and-route.

### 17.2. Замороженный target

Device:

[
oxed{	exttt{5CEFA7F23C6}}
]

Tool:

[
oxed{	ext{Quartus II 13.1}}
]

Timing reference:

[
100	ext{ MHz}.
]

### 17.3. Объявленные physical observers

Использованы:

[
O_{m ALM},
O_{m reg},
O_{m DSP},
O_{F_{max}},
O_{m delay},
O_{m logicdepth},
O_{m celldelay},
O_{m routedelay}.
]

Эти coordinates были объявлены до анализа результата.

---

## 18. Cyclone-V результаты

Все три presentations получили FIT.

| Presentation | ALM | Registers | DSP | Fmax MHz | Data delay ns | Levels | Cell ns | Routing ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| PREFIX19 | 10627 | 69 | 48 | 28.52 | 34.827 | 30 | 13.556 | 21.270 |
| NIELSEN12 | 12017 | 69 | 48 | 27.50 | 36.212 | 31 | 14.026 | 22.182 |

Следовательно,

[
oxed{
mathcal P_{m CV}^{m joint}
=
{{D,P},{N}}.
}
]

Для D/P physical visibility vector:

[
oxed{
(0,0,0,0,0,0,0,0).
}
]

То есть generic ABC-fast distinction D/P полностью скрывается declared Cyclone-V physical profile.

---

## 19. Что именно означает Cyclone result

Он **не** означает:

[
	ext{routed state}(D)=	ext{routed state}(P).
]

Он означает лишь:

[
oxed{
O_{m CV}^{m joint}(D)
=
O_{m CV}^{m joint}(P).
}
]

То есть две presentations принадлежат одному equivalence class относительно заранее объявленного measured physical observer.

---

## 20. NIELSEN12 на Cyclone V

Относительно D/P:

[
12017-10627=1390
]

дополнительных ALM, то есть примерно

[
13.08%.
]

Fmax ниже примерно на

[
3.58%.
]

Data delay выше примерно на

[
3.98%.
]

Logic depth:

[
31	ext{ против }30.
]

Следовательно NIELSEN12 остаётся отдельным physical class.

---

## 21. H19-LAB-01 provenance

Для Cyclone-V лаборатории сохранён SHA-256 manifest на 33 ключевых артефакта:

- generated RTL;
- Quartus inputs;
- fitter/map/timing reports;
- worst-path report;
- optional flow reports.

Это позволяет проверять byte-level provenance конкретного измеренного run.

Hashes не являются доказательством deterministic rerouting на другой машине или в другой версии toolchain.

---

## 22. H19-LAB-02: Gowin GW5A-25A

### 22.1. Цель

Провести независимую cross-vendor проверку того же presentation family.

Target:

[
oxed{
	exttt{GW5A-LV25MG121NC1/I0}
}
]

Tool:

[
oxed{
	ext{Gowin Education IDE 1.9.9Beta-4}
}
]

CLI:

[
	exttt{gw_sh.exe}.
]

Clock contract:

[
	exttt{create_clock -period 10.000}
]

то есть 100 MHz.

---

## 23. Gowin synthesis gate

GowinSynthesis дал:

| Presentation | Logic | LUT | ALU | Registers | DSP |
| --- | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | 19376 | 18882 | 494 | 69 | 28 |
| PREFIX19 | 19376 | 18882 | 494 | 69 | 28 |
| NIELSEN12 | 21221 | 20729 | 492 | 69 | 28 |

Следовательно уже synthesis resource observer даёт

[
oxed{
mathcal P_{m GW,syn}
=
{{D,P},{N}}.
}
]

Но основной эксперимент требует post-P&R measurement.

---

## 24. Gowin physical-fit calibration

Исходный полный интерфейс содержит 71 port и превысил число обычных package I/O.

RTL не изменялся.

Вместо этого были включены dual-purpose package pins:

- MSPI as GPIO;
- READY as GPIO.

Это изменяет package configuration, но не semantics, mathematical presentation, decision DAG или timing contract.

После этого все три variants прошли:

- synthesis;
- placement;
- routing;
- timing analysis;
- bitstream generation.

---

## 25. Gowin post-P&R результаты

| Presentation | P&R | Logic | LUT | ALU | Reg | CLS | DSP | Fmax MHz | Levels | WNS ns | Setup TNS ns |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DIRECT12 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| PREFIX19 | PASS | 19628 | 18882 | 746 | 69 | 10150 | 28 | 16.276 | 49 | -51.440 | -644.501 |
| NIELSEN12 | PASS | 21448 | 20729 | 719 | 69 | 10941 | 28 | 16.599 | 49 | -50.243 | -628.206 |

Все три нарушают 100 MHz timing target.

Поэтому:

[
oxed{
	ext{P&R PASS}
eq	ext{timing closure at 100 MHz}.
}
]

Post-route Fmax измеряется отдельно.

---

## 26. Gowin physical quotient

DIRECT12 и PREFIX19 совпадают по всем declared post-P&R coordinates:

[
19628=19628,
]

[
18882=18882,
]

[
746=746,
]

[
69=69,
]

[
10150=10150,
]

[
28=28,
]

[
16.276=16.276,
]

[
49=49,
]

[
-51.440=-51.440,
]

[
-644.501=-644.501.
]

Следовательно

[
oxed{
mathcal P_{m GW}^{m joint}
=
{{D,P},{N}}.
}
]

---

## 27. NIELSEN12 на Gowin

Relative to D/P:

[
21448-19628=1820
]

дополнительных Logic units, примерно

[
9.27%.
]

LUT:

[
20729-18882=1847
]

или примерно

[
9.78%.
]

CLS:

[
10941-10150=791
]

или примерно

[
7.79%.
]

Но Fmax немного **выше**:

[
16.599>16.276	ext{ MHz},
]

примерно на

[
1.98%.
]

Это важный отрицательный результат для попытки ввести один global scalar cost.

Большая physical footprint не обязана означать меньший Fmax на другой технологии.

---

## 28. Cross-vendor replication

Получено:

[
oxed{
mathcal P_{m CV}^{m joint}
=
mathcal P_{m GW}^{m joint}
=
{{D,P},{N}}.
}
]

Это основной новый физический результат H19.

Он утверждает **replication partition shape**, а не numerical resource ratios.

То есть структурно повторилось:

[
Dsim_{m phys}P,
qquad
N
otsim_{m phys}D.
]

Но конкретные performance directions между vendors не обязаны совпадать.

---

## 29. Полная наблюдаемая траектория H19

Соберём измеренные stages:

[
oxed{
{{D,P},{N}}_{m post-proc}
	o
{{D,P},{N}}_{m techmap}
	o
{{D},{P},{N}}_{m ABC-fast}
}
]

и затем два независимых physical endpoints:

[
oxed{
egin{cases}
{{D,P},{N}}_{m CycloneV},\[1mm]
{{D,P},{N}}_{m Gowin}.
end{cases}
}
]

Таким образом на coarse observer level наблюдается:

[
oxed{
	ext{merge}
	o
	ext{merge}
	o
	ext{split}
	o
	ext{merge on two vendors}.
}
]

Это не trajectory complete state.

Это trajectory **observer-induced partitions**.

---

## 30. Главный вывод о «булевой геометрии»

Термин «Boolean geometry» в H19 не означает новую геометрию пространства Boolean functions.

Он обозначает конечную структурную картину:

1. существует family математических presentations;
2. существует family observers;
3. каждый observer индуцирует partition presentations;
4. refinement observer даёт refinement partition;
5. compiler stage меняет пространство states и тем самым может менять observer partition;
6. physical mapping добавляет новые observer coordinates;
7. итоговый объект — atlas

[
(i,Pi,O)mapstomathcal P_{i,Pi,O}.
]

Именно этот atlas показывает, где presentation distinction находится «на поверхности», где становится латентным и где вновь проявляется.

---

## 31. Что в работе действительно новое

После hostile prior-art audit сильнейшая H19-specific часть не состоит в абстрактной теории partitions.

Она состоит в комбинации:

[
oxed{
	ext{математически мотивированное E0-семейство}
+
	ext{compiler-stage observer atlas}
+
	ext{nonmonotone visibility}
+
	ext{двухвендорный physical quotient}
}
]

с reproducible evidence.

Особенно важен controlled D/P witness:

- source structures различны;
- intermediate cell histograms совпадают;
- wires остаются различными;
- ABC-fast снова различает;
- Cyclone-V physical joint observer снова склеивает;
- Gowin physical joint observer независимо снова склеивает.

---

## 32. Что работа не утверждает

H19 не утверждает:

1. что DIRECT12 и PREFIX19 имеют одинаковые full compiler states;
2. что они имеют одинаковые routed netlists;
3. что их bitstreams совпадают;
4. что физический quotient invariant для всех FPGA;
5. что NIELSEN12 «хуже» в универсальном смысле;
6. что найден technology-independent complexity measure;
7. что (Pi_{m DAG}) оптимален;
8. что address-selection calibration даёт новую unrestricted circuit lower bound;
9. что partition lattice или observer equivalence являются новыми математическими объектами;
10. что один vendor result достаточен для universal hardware law.

---

## 33. Reproducibility

Для Cyclone-V и Gowin laboratories сохранены compact summaries и SHA-256 provenance manifests.

Cyclone-V:

[
33
]

fingerprinted artifacts.

Gowin:

[
33
]

fingerprinted artifacts.

Для Gowin manifest включает:

- generated RTL;
- SDC;
- Tcl;
- option snapshot;
- transcript;
- synthesis report;
- P&R report;
- timing report.

Это даёт byte-level привязку опубликованных summary numbers к конкретным локальным артефактам.

---

## 34. Интерпретация результатов

### 34.1. Source compression не предсказывает FPGA cost напрямую

PREFIX19 уменьшает source composition count

[
24	o19,
]

но после ABC-fast имеет на 9 cells больше, чем DIRECT12:

[
60383>60374.
]

Поэтому

[
oxed{
	ext{source sharing}

otRightarrow
	ext{monotone downstream area saving}.
}
]

### 34.2. Compiler-visible distinction может исчезнуть физически

ABC-fast различает D/P.

Оба physical endpoints их склеивают.

Значит generic Boolean representation может содержать отличие, которое vendor technology mapping и выбранный joint physical observer не сохраняют.

### 34.3. Physical cost многомерна

NIELSEN12 физически тяжелее на обоих devices.

Но timing direction differs:

- на Cyclone V Fmax ниже;
- на Gowin Fmax немного выше.

Поэтому нельзя корректно определить «лучшую presentation» одним vendor-independent scalar без дополнительного целевого функционала.

---

## 35. Ограничения

Исследование пока ограничено:

- одной semantic task family;
- тремя presentations;
- двумя FPGA vendors;
- конкретными tool versions;
- конкретными declared observers;
- одной registered one-cycle spatial shell;
- конкретным timing contract.

Следовательно cross-vendor replication пока означает только:

[
2/2
]

совпадение partition shape в проведённых лабораториях.

Это не статистическое утверждение о population of FPGA architectures.

---

## 36. Следующие эксперименты

Наиболее ценные продолжения:

### A. Третий technology backend

Например Xilinx 7-series / Zynq-7010 с тем же frozen RTL family и эквивалентным observer set.

Если снова получится

[
{{D,P},{N}},
]

cross-technology persistence станет существенно сильнее.

### B. Второе E0-семейство

Для publication-strength необходимо показать, что framework работает не только на одном restricted-12 family.

### C. Seed sensitivity

Для P&R tools полезно повторить реализацию с несколькими seeds и различать:

- stable partition;
- seed-sensitive partition;
- coordinate-sensitive partition.

### D. Полный physical-state proxy

Summary coordinates остаются coarse observers.

Можно добавить:

- placed cell-location histogram;
- routing-resource summary;
- critical-cone signature;
- bitstream hash как extreme coarse equality test, но не как semantic metric.

### E. Prediction problem

Главный следующий теоретический вопрос:

> какие source invariants предсказывают, какие presentation distinctions останутся видимыми после конкретного compiler/technology observer?

Это уже путь от описательного atlas к предсказательной теории.

---

## 37. Итог

HATTER-SOL-19 показывает на контролируемом конечном примере, что математическая presentation structure не имеет одного фиксированного «аппаратного образа».

Она существует относительно наблюдателя.

Для DIRECT12 и PREFIX19:

[
	ext{source-visible}
	o
	ext{cell-hidden}
	o
	ext{cell-hidden}
	o
	ext{ABC-visible}
	o
	ext{Cyclone-hidden}
]

и независимо

[
	ext{ABC-visible}
	o
	ext{Gowin-hidden}.
]

Для NIELSEN12 различие сохраняется как отдельный measured class на обоих physical endpoints.

Поэтому главный экспериментальный результат можно записать как

[
oxed{
mathcal P_{m CV}^{m joint}
=
mathcal P_{m GW}^{m joint}
=
{{DIRECT12,PREFIX19},{NIELSEN12}}.
}
]

Вместе с no-resurrection theorem для полного deterministic compiler state это приводит к основной концептуальной формуле H19:

[
oxed{
	ext{наблюдаемое забывание}

eq
	ext{уничтожение структуры}.
}
]

Компилятор и технология могут переносить скрытое различие между координатами представления, а coarse observer может его терять и позднее вновь видеть.

Тем самым hardware image математического представления разумнее описывать не одним числом, а **траекторией observer-induced partitions**.

---

## 38. Publication claim

Консервативная формулировка, пригодная для abstract/conclusion:

> Мы вводим и применяем конечный observer-partition framework для отслеживания различий между функционально эквивалентными, математически мотивированными представлениями через compiler и FPGA flows. На замороженном трёхэлементном семействе наблюдается nonmonotone visibility: DIRECT12 и PREFIX19 совпадают по промежуточным cell observers, разделяются после ABC-fast и снова оказываются неразличимыми по заранее объявленным joint physical profiles на двух независимых FPGA vendor/toolchains, тогда как NIELSEN12 остаётся отдельным physical class. Результат является конечным, tool- и observer-relative cross-vendor replication experiment и не утверждает универсальную technology-independent invariance.

---

## 39. Evidence map

Основные theory layers:

- `H19_01_TEMPORAL_SPATIAL_FORMAL_MODEL.md`
- `H19_04_COMPILER_FORGETTING_RESULT.md`
- `H19_05_PRESENTATION_PRESERVATION.md`
- `H19_06_COMPILER_KERNEL_AND_SURVIVAL.md`
- `H19_07_NONMONOTONE_PRESENTATION_SURVIVAL.md`
- `H19_08_PRESENTATION_SURVIVAL_WORDS.md`
- `H19_09_BOOLEAN_OBSERVABILITY_AND_NO_RESURRECTION.md`
- `H19_10_ADAPTIVE_SPATIALIZATION_SEPARATION.md`
- `H19_11_VISIBILITY_FRONTIER_MIGRATION.md`
- `H19_12_PRESENTATION_PARTITION_LATTICE.md`
- `H19_13_PRIOR_ART_AND_NOVELTY_AUDIT.md`
- `H19_14_LATENT_PARTITION_GAP.md`
- `H19_15_PHYSICAL_VISIBILITY_ATLAS_PROTOCOL.md`
- `H19_16_PHYSICAL_PROFILE_QUOTIENT_CYCLONEV.md`
- `H19_17_CROSS_VENDOR_PHYSICAL_QUOTIENT.md`

Cyclone-V evidence:

- `H19_LAB_01_E0_CYCLONEV/H19_LAB01_CYCLONEV_SUMMARY.csv`
- `H19_LAB_01_E0_CYCLONEV/H19_LAB01_PHYSICAL_PARTITIONS.csv`
- `H19_LAB_01_E0_CYCLONEV/H19_LAB01_PHYSICAL_VISIBILITY_ATLAS.md`
- `H19_LAB_01_E0_CYCLONEV/H19_LAB01_PROVENANCE_SHA256.csv`
- `H19_LAB_01_E0_CYCLONEV/H19_LAB01_PROVENANCE_SHA256.md`

Gowin evidence:

- `H19_LAB_02_E0_GOWIN_GW5A25/H19_LAB02_GOWIN_SYNTHESIS_SUMMARY.csv`
- `H19_LAB_02_E0_GOWIN_GW5A25/H19_LAB02_GOWIN_PNR_SUMMARY.csv`
- `H19_LAB_02_E0_GOWIN_GW5A25/H19_LAB02_GOWIN_PROVENANCE_SHA256.csv`
- `H19_LAB_02_E0_GOWIN_GW5A25/H19_LAB02_GOWIN_PROVENANCE_SHA256.md`

---

## 40. Current publication status

[
oxed{
	ext{PUBLICATION CANDIDATE THRESHOLD CROSSED}
}
]

для конечного claim set, сформулированного в этой рукописи.

Перед внешней публикацией остаются редакционные, а не исследовательские обязательные шаги:

1. финальный bibliography audit;
2. англоязычная версия;
3. manuscript-level notation consistency pass;
4. external reviewer prompt;
5. PDF/Zenodo package;
6. DOI insertion after publication.

