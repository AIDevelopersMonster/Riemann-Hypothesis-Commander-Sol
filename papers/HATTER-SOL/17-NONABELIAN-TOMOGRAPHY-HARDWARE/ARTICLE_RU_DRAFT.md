# HATTER-SOL-17
# От неабелевой томографии к математическому процессору, FPGA и физическому кремнию

**Авторы:** Commander Sol, Алексей Иванов  
**Статус:** рабочий препринт / manifesto + reproducible laboratory  
**Версия:** draft 0.1, 18 September 2026

---

## Аннотация

Эта работа исследует путь от конечной неабелевой томографии к аппаратной реализации.

В лаборатории

\[
G=PSL(2,7)
\]

рассматриваются generating ordered pairs \((A,B)\), факторизованные по simultaneous conjugation. Полное пространство содержит

\[
19152
\]

generating pairs и распадается на

\[
114
\]

simultaneous-conjugacy orbits.

Мы строим короткие семейства group-word observations, которые разделяют эти орбиты, доказываем минимальные глубины и минимальное число наблюдений для one-known-erasure reconstruction, строим exact structural classifier, ROM-free repair network и оптимальный shared word DAG, а затем переносим конструкцию в RTL.

Главная инженерная идея работы состоит не в том, чтобы объявить H17 готовым универсальным ECC или готовым промышленным контроллером, а в том, чтобы показать воспроизводимый путь:

\[
\boxed{
\text{symmetry theorem}
\rightarrow
\text{orbit tomography}
\rightarrow
\text{Boolean architecture}
\rightarrow
\text{RTL}
\rightarrow
\text{target hardware experiment}
}
\]

Работа также формулирует границы текущей fault model и выделяет направления следующего поколения: adaptive word tomography, Nielsen dynamics, hardware root-of-trust/PUF, symmetry compression for GNN and quantum decoding, streaming non-Abelian automata and attack-first non-Abelian cryptography.

---

## 1. Почему H17

Обычный аппаратный алгоритм часто начинается с логической функции и заканчивается измерением LUT, FF и Fmax.

H17 идёт в обратную сторону.

Сначала строится математическая задача:

> какие короткие наблюдения конечного неабелева объекта достаточно различают его состояния modulo symmetry?

Затем исследуется, какую аппаратную цену имеет найденная theorem layer.

Так появляется возможность измерить не только стоимость схемы, но и **стоимость математического утверждения**.

В H17 это особенно видно на closure-aware architecture: групповая замкнутость позволяет удалить повторяющиеся membership tests для derived words и почти вдвое сократить generic synthesized frontend logic.

---

## 2. Конечная лаборатория

Используется группа

\[
G=PSL(2,7),
\qquad |G|=168.
\]

Рассматриваются ordered pairs:

\[
(A,B)\in G^2
\]

такие, что

\[
\langle A,B\rangle=G.
\]

Всего таких generating pairs:

\[
\boxed{19152}.
\]

На них действует simultaneous conjugation:

\[
(A,B)\mapsto
(hAh^{-1},hBh^{-1}),
\qquad h\in G.
\]

Получается:

\[
\boxed{114}
\]

generating simultaneous-conjugacy orbits.

Каждая такая орбита имеет размер:

\[
\boxed{168}.
\]

Следовательно:

\[
114\cdot168=19152.
\]

Идентификаторы орбит фиксируются как:

\[
0,1,\ldots,113.
\]

---

## 3. Наблюдения как group words

Пусть:

\[
a=A^{-1},
\qquad
b=B^{-1}.
\]

Для group word \(w\) рассматривается conjugacy class:

\[
c_w(A,B)=\operatorname{class}(w(A,B)).
\]

Для \(PSL(2,7)\) используются oriented classes:

\[
1A,\ 2A,\ 3A,\ 4A,\ 7A,\ 7B.
\]

Именно порядок букв важен:

\[
AB\neq BA.
\]

Поэтому group word является не просто строкой, а программой наблюдения неабелевой структуры.

---

## 4. От пяти probes к robust8

Родительская H16-конструкция показала, что пять probes:

\[
A,\ B,\ AB,\ Ab,\ ABab
\]

разделяют все 114 generating orbits.

Но injectivity ещё не означает erasure robustness.

H17 ставит более сильную задачу:

> найти минимальное семейство probes, которое различает generating orbits и сохраняет однозначность после потери одной известной coordinate.

Для полного primitive cyclic trace family глубины до 5 решается конечная covering problem.

Получено:

\[
\boxed{
\text{minimum joint one-known-erasure probe count}=8.
}
\]

Одна оптимальная семья:

\[
\boxed{
AAB,\;
Abb,\;
AAAB,\;
Abbb,\;
AABAb,\;
AAbAb,\;
ABABB,\;
ABaBB
}
\]

с:

\[
d_{\mathrm{gen/gen}}=2,
\qquad
d_{\mathrm{gen/non}}=2.
\]

Это означает, что удаление любой одной известной coordinate не разрушает идентификацию generating orbit и separation from non-generating states.

---

## 5. Минимальная глубина

Полная primitive family глубины до 4 имеет 25 coordinates, но:

\[
d_{\min}=1.
\]

Существуют ровно семь пар generating orbits, различимых только одним probe в depth-\(\le4\) family.

Для всех семи дефектов необходимым separator оказывается commutator:

\[
ABab=[A,B].
\]

Exact-depth-5 probe:

\[
AABAb
\]

разделяет все семь defect pairs.

Следовательно:

\[
\boxed{
\text{minimum possible maximum primitive depth}=5.
}
\]

Это первый важный пример того, что аппаратная глубина наблюдения ограничивается не эвристикой, а theorem layer.

---

## 6. Structural classifier без orbit ROM

Входной group element представлен 24-битной перестановкой восьми точек.

Structural classifier проверяет:

1. bijectivity;
2. projective cross-ratio consistency;
3. PSL orientation;
4. conjugacy class.

Exhaustive enumeration всех

\[
8!=40320
\]

перестановок даёт:

\[
PGL(2,7)=336,
\qquad
PSL(2,7)=168.
\]

Для valid PSL members классы orders \(1,2,3,4\) соответствуют:

\[
1A,2A,3A,4A,
\]

а order-7 elements разделяются на:

\[
7A,\ 7B
\]

по orientation test.

---

## 7. ROM-free repair

24-битный robust8 fingerprint:

\[
F(A,B)=(c_0,\ldots,c_7)
\]

сам является canonical generating-orbit fingerprint.

Для каждого известного erased coordinate exact dynamic programming строит minimum worst-case repair decision tree depth:

\[
\boxed{4}.
\]

Количество internal nodes по восьми erasure modes:

\[
41,\ 41,\ 43,\ 43,\ 30,\ 39,\ 39,\ 30.
\]

Итого:

\[
306
\]

nodes до synthesis/factoring.

Это позволяет восстанавливать erased class coordinate без 114-entry orbit decoder ROM.

---

## 8. Shared word DAG

Если восемь robust words вычислять независимо, требуется:

\[
26
\]

permutation compositions.

Exact DAG optimization снижает это до:

\[
\boxed{14}
\]

при максимальной composition depth:

\[
\boxed{3}.
\]

Один optimum:

\[
\text{level 1: } AB,\ Ab,\ BB;
\]

\[
\text{level 2: } AAB,\ ABA,\ ABa,\ Abb,\ AbAb;
\]

\[
\text{level 3: } AAAB,\ Abbb,\ AABAb,\ AAbAb,\ ABABB,\ ABaBB.
\]

Это проверено на всех:

\[
168^2=28224
\]

ordered PSL pairs.

---

## 9. Closure-aware theorem как аппаратная оптимизация

Ключевой групповой факт:

\[
A,B\in PSL(2,7)
\Rightarrow
w(A,B)\in PSL(2,7)
\]

для любого free-group word \(w\).

Следовательно, derived words не требуют повторной полной membership проверки.

Архитектура:

\[
2\times\text{membership-only}(A,B)
+
8\times\text{member-class-only}.
\]

При одинаковой generic Yosys methodology получено:

| Design | Full classifier | Closure-aware | Reduction |
|---|---:|---:|---:|
| robust8 frontend | 38957 | 20485 | 47.42% |
| flat orbit-ID core | 43330 | 24730 | 42.93% |
| ROM-free fingerprint core | 42484 | 23937 | 43.66% |

Это **generic Boolean-cell counts**, а не LUT/FF/Fmax конкретного FPGA.

Главный смысл таблицы:

\[
\boxed{
\text{теорема о замкнутости удаляет аппаратную логику.}
}
\]

---

## 10. Что именно восстанавливает H17

Это принципиальная граница.

Текущий robust8 repair восстанавливает:

\[
\boxed{
\text{one known fingerprint-coordinate erasure}
}
\]

то есть:

\[
(c_0,\ldots,c_{j-1},?,c_{j+1},\ldots,c_7)
\Rightarrow
(c_0,\ldots,c_7).
\]

Он **не восстанавливает**:

- потерянный \(A\);
- потерянный \(B\);
- произвольный внешний sensor;
- неизвестно где повреждённую coordinate;
- общий FPGA fabric failure.

В LAB-02 erasure пока вводится после вычисления полного fingerprint.

Поэтому это строгая RTL-демонстрация mathematics, но ещё не physical channel failure.

---

## 11. Путь к физическому эксперименту

Следующий hardware step должен заменить искусственный mask на восемь independent valid/data paths:

\[
(A,B)
\rightarrow
\begin{cases}
P_0\\
P_1\\
\vdots\\
P_7
\end{cases}
\rightarrow
\text{repair}.
\]

Каждый \(P_i\) должен быть отдельным logical/physical probe channel.

Тогда известная потеря:

\[
P_j=\mathrm{ERASED}
\]

становится реальным fault model.

Это создаёт естественный мост к:

- distributed probe fabric;
- structural BIST;
- fault localization;
- degraded mode;
- region-separated FPGA experiment.

---

## 12. Почему FPGA выбирается после логики

H17 сознательно не привязывает architecture к конкретной плате до получения требований.

Сначала измеряются:

- LUT/FF class;
- need for BRAM;
- routing complexity;
- timing;
- clocking;
- floorplanning requirements;
- physical separation requirements;
- possible PUF primitives;
- instrumentation needs.

Только после этого выбирается FPGA family/board.

Это делает выбор железа следствием архитектуры, а не наоборот.

---

## 13. От статической к адаптивной томографии

Фиксированная observer family — не единственный вариант.

Можно выбирать следующее group word в зависимости от уже полученных classes:

\[
c_1
\rightarrow
w_2(c_1)
\rightarrow
c_2
\rightarrow
w_3(c_1,c_2)
\rightarrow\cdots
\]

Так возникает:

\[
\boxed{\text{adaptive non-Abelian tomography}}.
\]

Это направление вынесено в HATTER-SOL-18.

Главная идея:

> group words становятся не фиксированным списком probes, а branching program, который адаптируется к наблюдаемому объекту.

---

## 14. Nielsen dynamics

Другой путь — менять сами generators:

\[
(A,B)\mapsto(B,A),
\]

\[
(A,B)\mapsto(A^{-1},B),
\]

\[
(A,B)\mapsto(AB,B).
\]

Тогда 114 orbit states становятся вершинами dynamic state graph.

Это превращает H17 из статической tomography в:

\[
\boxed{\text{non-Abelian dynamical tomography}}.
\]

В H18 этот слой будет исследоваться совместно с adaptive word selection.

---

## 15. Application models, not claims

H17 не объявляет готовыми следующие приложения. Он формулирует проверяемые research programs.

### 15.1. Equivariant AI / GNN

Идея:

\[
\text{local graphlet}
\rightarrow
\text{orbit signature}
\rightarrow
\text{reuse/canonicalization}.
\]

Перед hardware требуется сравнить expressive power с WL hierarchy на конечных graphlet families.

### 15.2. Robotics / aerospace

Идея:

\[
SO(3),SE(3)
\rightarrow
\text{finite orbit/grid automaton}.
\]

Цель — bounded-error discrete attitude tracking, а не обещание zero physical drift.

### 15.3. Quantum syndrome decoding

Идея:

\[
\text{syndrome}
\rightarrow
\text{symmetry orbit}
\rightarrow
\text{compressed decoder state}.
\]

Surface-code symmetry и braid-group models должны исследоваться отдельно.

### 15.4. Streaming network telemetry

Идея:

\[
\text{packet-event stream}
\rightarrow
\text{non-Abelian state update}
\rightarrow
\text{structural anomaly signature}.
\]

Это потенциально line-rate friendly, но реальные throughput claims требуют target pipeline.

### 15.5. Hardware Root-of-Trust / PUF

Идея:

\[
\text{physical silicon}
\rightarrow
\text{stable PUF features}
\rightarrow
(A,B)
\rightarrow
\text{H17 structural attestation}.
\]

H17 здесь рассматривается как tamper/anomaly structure, а не как замена стандартной cryptography.

### 15.6. Non-Abelian / post-quantum research seed

Идея hidden conjugator:

\[
A'=hAh^{-1},
\qquad
B'=hBh^{-1}.
\]

Информационная потеря quotient map:

\[
\neq
\]

computational hardness.

Поэтому это только attack-first research direction.

---

## 16. Универсальный pipeline будущих применений

Для каждого нового domain:

\[
\boxed{
\text{DOMAIN MODEL}
\rightarrow
\text{SYMMETRY THEOREM}
\rightarrow
\text{SEPARATING PROBES}
\rightarrow
\text{EXHAUSTIVE/SOFTWARE TEST}
\rightarrow
\text{RTL}
\rightarrow
\text{TARGET SYNTHESIS}
\rightarrow
\text{PHYSICAL BENCHMARK}
}
\]

Если отсутствует meaningful map:

\[
\Phi:X\rightarrow \mathcal S,
\]

то H17 превращается лишь в необычный encoder.

Если \(\Phi\) отражает естественную symmetry предметной области, orbit processor приобретает самостоятельный смысл.

---

## 17. Уровни доказательности

В H17 вводится явная маркировка:

- **THEOREM** — доказано математически;
- **EXHAUSTIVE COMPUTATION** — проверено полным finite enumeration;
- **RTL VERIFIED** — проверено simulation;
- **GENERIC SYNTHESIS** — technology-independent synthesis;
- **TARGET SYNTHESIS** — mapped to a concrete FPGA;
- **MEASURED HARDWARE** — измерено на physical board;
- **RESEARCH HYPOTHESIS** — ещё не доказанное направление.

Это позволяет не смешивать математические результаты, RTL и future applications.

---

## 18. Итог

H17 показывает конечный пример того, как symmetry quotient можно превратить в exact hardware object.

Получена цепочка:

\[
\boxed{
PSL(2,7)
\rightarrow
114\ \text{orbits}
\rightarrow
8\ \text{robust probes}
\rightarrow
14\ \text{shared compositions}
\rightarrow
\text{closure-aware classifier}
\rightarrow
\text{ROM-free repair}
}
\]

Смысл результата не в утверждении, что найден универсальный fault-tolerant processor.

Смысл в другом:

> математическая структура может определять не только правильность алгоритма, но и архитектуру аппаратуры, её redundancy, её минимальную глубину и даже то, какую логику можно удалить.

Следующий шаг H17 — physical target experiment.

Следующий математический шаг серии — HATTER-SOL-18:

\[
\boxed{
\text{Adaptive Word Tomography and Nielsen Dynamics}
}
\]

где фиксированное множество probes заменяется программой наблюдений, которая сама зависит от уже полученной structural information.
