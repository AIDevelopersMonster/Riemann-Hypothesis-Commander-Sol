# HATTER-SOL-17 · Application Research Map
## От конечной неабелевой томографии к моделям будущих применений

**Статус:** карта исследовательских направлений для основной H17-статьи и возможных последующих работ.  
**Правило:** ни одно направление ниже не объявляется готовым применением H17. Для каждого сначала строится самостоятельная теория отображения предметной области в орбитальную/групповую структуру, затем проверяемый алгоритм, затем RTL/FPGA, и только после этого — физический benchmark.

---

# 1. Что именно переносится из H17

H17 следует рассматривать не как универсальный готовый процессор для всех предметных областей, а как **методологию**:

\[
\boxed{
\text{symmetry/action}
\rightarrow
\text{orbit quotient}
\rightarrow
\text{separating observations}
\rightarrow
\text{compact structural signature}
\rightarrow
\text{hardware implementation}
}
\]

Текущий \(PSL(2,7)\) — конечная лаборатория, в которой эта цепочка уже построена полностью.

Для новой предметной области необязательно сохранять именно \(PSL(2,7)\). Может сохраняться сама архитектурная идея:

1. определить пространство физических/логических объектов \(X\);
2. определить группу или полугруппу преобразований \(G\);
3. определить, какие преобразования считаются эквивалентностью;
4. построить orbit space \(X/G\);
5. найти короткое семейство separating probes;
6. доказать различимость / error model / redundancy;
7. только затем переносить алгоритм в FPGA/ASIC.

---

# 2. Универсальный application bridge

Для реального объекта \(x\in X\) нужен frontend:

\[
\Phi:X\rightarrow \mathcal S,
\]

где \(\mathcal S\) — структурное пространство, например:

\[
\mathcal S=G^2,\qquad \Phi(x)=(A_x,B_x),
\]

или более общий набор/group word state.

Далее:

\[
x
\overset{\Phi}{\longrightarrow}
(A_x,B_x)
\longrightarrow
\text{orbit}
\longrightarrow
F(A_x,B_x)
\longrightarrow
\text{decision}.
\]

Главный вопрос каждой будущей работы — **не FPGA**, а построение содержательного \(\Phi\).

Если \(\Phi\) искусственно назначает номера объектам, H17 становится только необычным кодеком.

Если \(\Phi\) отражает естественную симметрию предметной области, orbit processor получает самостоятельный смысл.

---

# 3. Направление A — Equivariant AI / GNN

## 3.1. Почему связь естественная

Graph Neural Networks и geometric/equivariant models специально строятся так, чтобы учитывать симметрии:

- permutation symmetry вершин;
- rotation / reflection / translation;
- orbit equivalence локальных окружений;
- ограничения выразительности, связанные с Weisfeiler-Leman hierarchy.

H17 уже решает конечную задачу:

\[
\text{объекты modulo symmetry}
\longrightarrow
\text{короткие separating invariants}.
\]

Это делает связь с equivariant representation theory естественной.

## 3.2. Что нельзя утверждать сейчас

Нельзя утверждать:

- что H17 заменяет SE(3)-equivariant GNN;
- что FPGA определяет произвольный molecular graph за один такт;
- что получена экономия 99% энергии;
- что H17 сильнее \(1\)-WL или \(k\)-WL;
- что текущий \(PSL(2,7)\) непосредственно кодирует молекулярную геометрию.

Все такие числа требуют отдельного benchmark.

## 3.3. Первая строгая теоретическая задача

Не пытаться заменить всю GNN.

Начать с bounded local graphlets:

\[
\mathcal G_{d,r}
=
\{\text{локальные графовые окружения ограниченного размера}\}.
\]

Определить action:

\[
\mathrm{Aut}/S_n
\]

на labeling узлов и искать H17-like separating probe family.

Сравнить:

\[
\text{orbit signature}
\quad\text{vs}\quad
1\text{-WL},2\text{-WL},\ldots
\]

на конечных graphlet families.

Вопрос:

\[
\boxed{
\text{может ли короткая orbit signature различать те graphlets,}
\\
\text{которые приходится повторно обрабатывать GNN?}
}
\]

## 3.4. Практический hardware bridge

Самая реалистичная первая архитектура:

\[
\text{local graph neighborhood}
\rightarrow
\text{orbit/canonical signature}
\rightarrow
\text{cache / class ID}
\rightarrow
\text{reuse learned embedding}.
\]

То есть FPGA не заменяет neural network, а может выполнять:

- structural preclassification;
- graphlet canonicalization;
- symmetry-aware cache lookup;
- duplicate/equivalent neighborhood detection.

Для molecular modeling и PCB/netlist analysis это может уменьшать повторную обработку одинаковых по симметрии fragments — но размер выигрыша должен быть измерен.

## 3.5. Возможная будущая статья

**Orbit-Separating Hardware Primitives for Equivariant Graph Learning**

Подзадачи:

1. finite graphlet model;
2. WL comparison theorem;
3. separating family search;
4. RTL classifier;
5. CPU/GPU/FPGA benchmark.

**Статус:** сильная теоретическая ветвь; hardware application только после graphlet theorem.

---

# 4. Направление B — Robotics / Aerospace / discrete Lie-group automata

## 4.1. Что здесь переносится из H17

Для ориентации естественная symmetry group:

\[
SO(3),
\]

для положения и ориентации:

\[
SE(3).
\]

H17 methodology можно перенести через finite discretization / finite subgroup action / Schreier graph.

Но **сам \(PSL(2,7)\) не является конечной rotation subgroup \(SO(3)\)**.

Для \(SO(3)\) естественнее рассматривать:

- cyclic groups;
- dihedral rotation groups;
- tetrahedral \(A_4\);
- octahedral \(S_4\);
- icosahedral \(A_5\);

либо более плотные finite orientation grids, уже не являющиеся одной конечной subgroup.

Поэтому здесь переносится метод H17, а не его конкретная группа.

## 4.2. Что неверно обещать

Фраза «нулевой дрейф» слишком сильна.

Discrete state transition действительно можно реализовать точно в цифровом автомате:

\[
s_{n+1}=T(s_n,u_n)
\]

без накопления floating-point ошибки **внутри конечного state machine**.

Но остаются:

- sensor drift;
- quantization error;
- discretization error;
- model mismatch;
- disturbances;
- error при projection \(SO(3)\rightarrow\) finite grid.

Поэтому корректная цель:

\[
\boxed{
\text{bounded-error discrete attitude tracking}
}
\]

а не абсолютный zero-drift physical control.

## 4.3. Теоретический рубеж

Нужно доказать:

1. covering radius orientation grid;
2. transition consistency;
3. bound на accumulated projection error;
4. conditions of closed-loop stability;
5. relation between graph distance on Schreier graph and geodesic distance on \(SO(3)\).

Только после этого появляется controller theorem.

## 4.4. Практический рубеж

FPGA хранит не quaternion/matrix integration как основной internal state, а:

\[
\text{orientation cell ID}
\]

и выполняет exact graph transitions.

Floating-point / fixed-point layer остаётся только на boundary:

\[
\text{IMU}
\rightarrow
\text{state estimation}
\rightarrow
\text{cell}
\rightarrow
\text{finite controller}.
\]

## 4.5. Возможная будущая статья

**Discrete Lie-Group Orbit Automata for Bounded-Error Attitude Tracking**

**Статус:** интересная самостоятельная математическая ветвь; не непосредственное применение существующего H17 RTL.

---

# 5. Направление C — Quantum Error Decoding

## 5.1. Правильная связь

Для обычного surface code основой являются stabilizer syndromes и equivalence classes ошибок.

Поэтому наиболее естественная H17-связь:

\[
\text{syndrome}
\rightarrow
\text{orbit under code symmetries}
\rightarrow
\text{canonical syndrome class}
\rightarrow
\text{decoder action}.
\]

То есть здесь перспективна не абстрактная фраза «неабелевый шум», а **symmetry/orbit compression of syndrome space**.

## 5.2. Что не следует смешивать

Braid groups естественны для non-Abelian anyons и topological quantum computing, но это отдельная тема.

Для standard surface codes нельзя автоматически заменять stabilizer decoding braid-group model.

Поэтому две возможные будущие ветви должны быть разделены:

### C1. Surface-code symmetry decoder

\[
\text{stabilizer syndrome}
\rightarrow
\text{automorphism orbit}
\rightarrow
\text{compressed decoder}.
\]

### C2. Non-Abelian anyonic / braid models

Отдельная более дальняя теория.

## 5.3. Почему hardware направление реально

Real-time QEC действительно требует очень низкой latency и высокой throughput.

Поэтому FPGA decoder является реальной engineering category.

Но утверждение «5 ns» нельзя фиксировать как результат H17 без target implementation.

Правильная цель:

\[
\boxed{
\text{измерить, уменьшает ли orbit compression}
\\
\text{decoder state space / memory / latency}
}
\]

## 5.4. Теоретический рубеж

Для небольших surface/toric codes:

1. построить syndrome symmetry group;
2. перечислить syndrome orbits;
3. найти canonical representatives;
4. проверить, сохраняется ли decoder decision на orbit;
5. измерить quotient compression factor;
6. сравнить с обычным decoder.

## 5.5. Возможная будущая статья

**Symmetry-Orbit Compression for Real-Time Quantum Syndrome Decoding**

**Статус:** сильный research seed; требует полностью новой code-theoretic модели до RTL.

---

# 6. Направление D — 6G / communication decoding

Связывать 6G непосредственно с braid groups сейчас преждевременно.

Для связи с H17 сначала требуется конкретная channel model:

\[
\text{received sequence}
\rightarrow
\text{structured state/noise word}
\rightarrow
\text{orbit or syndrome}.
\]

Если такой map не даёт доказуемого выигрыша, слово «неабелевый шум» остаётся только метафорой.

Поэтому 6G не следует выделять в основной H17 как самостоятельное practical claim.

Его можно сохранить только как:

\[
\boxed{\text{long-term communication research question}}
\]

после построения строгого sequence/noise model.

---

# 7. Направление E — Line-Rate Network Traffic Signatures

## 7.1. Почему это хороший engineering candidate

Сетевой поток уже является **последовательностью событий**.

Можно определить finite alphabet:

\[
\Sigma=
\{\text{packet-size class, direction, timing class, flag class, protocol event}\}
\]

и отображение:

\[
\Sigma^\ast
\rightarrow
\text{words / finite group or monoid state}.
\]

Тогда FPGA может обновлять structural state streaming-wise:

\[
S_{n+1}=T(S_n,e_n)
\]

без хранения всего packet history.

Это намного естественнее H17 methodology, чем попытка использовать H17 как ECC.

## 7.2. Это не DPI в строгом смысле

Если анализируется только:

- packet size;
- direction;
- inter-arrival timing;
- header class;
- ordering;

то корректнее говорить:

- traffic telemetry;
- flow anomaly signature;
- behavioral classification;

а не Deep Packet Inspection, поскольку payload может вообще не анализироваться.

## 7.3. Теоретический рубеж

Нужно определить:

1. event alphabet;
2. word reduction / relation set;
3. update law;
4. invariances;
5. collision/separation properties;
6. adversarial evasion model;
7. window/reset semantics.

Особенно интересна возможность dynamic words:

\[
w_{n+1}=\Psi(w_n,e_n),
\]

то есть streaming non-Abelian automaton.

## 7.4. Hardware рубеж

Сначала:

\[
10/25/100\ \mathrm{Gb/s}
\]

prototype.

Затем только при успешном pipeline переходить к 400G-class architecture.

На 400G интерфейс физически широкий и параллельный; следовательно, алгоритм должен быть не просто быстрым по clock, а параллелизуемым на несколько packet/data segments за цикл.

## 7.5. Возможная будущая статья

**Non-Abelian Streaming Signatures for Line-Rate Network Telemetry**

Подзадачи:

1. finite traffic alphabet;
2. collision/separation theorem;
3. software trace benchmark;
4. pipelined RTL;
5. line-rate replay;
6. adversarial traffic evaluation.

**Статус:** один из самых естественных engineering branches после H17.

---

# 8. Направление F — Hardware Root-of-Trust / PUF

Это направление уже вынесено отдельно в:

H17_HARDWARE_ROOT_OF_TRUST_PUF_RESEARCH_SEED_RU.md

Его место в общей карте:

\[
\text{physical silicon}
\rightarrow
\text{PUF features}
\rightarrow
\text{H17 structural state}
\rightarrow
\text{attestation / anomaly detection}.
\]

В отличие от GNN/robotics/QEC здесь предметная область уже непосредственно находится **внутри самого FPGA**, поэтому эта ветвь наиболее естественно соединяется с текущей hardware laboratory.

---

# 9. Направление G — Non-Abelian / Post-Quantum Cryptography

Уже вынесено отдельно в:

H17_POSTQUANTUM_NONABELIAN_RESEARCH_SEED_RU.md

Главный принцип:

\[
\text{information loss under quotient}
\neq
\text{computational hardness}.
\]

Криптографическая ветка допускается только как attack-first research.

---

# 10. Comparative readiness map

| Направление | Связь с H17 theory | Новый математический барьер | Hardware bridge | Можно включать в H17 сейчас |
|---|---|---|---|---|
| PUF / Root-of-Trust | высокая | physical-to-orbit map | высокая | да, как research model |
| Equivariant AI / GNN | высокая | orbit signatures vs WL/equivariance | средняя | да, как theoretical branch |
| Network streaming | высокая | sequence-to-group map + collisions | высокая | да, как engineering branch |
| Quantum syndrome decoding | средняя-высокая | syndrome orbit quotient | высокая после theory | да, как future article seed |
| Robotics / \(SO(3)\) | методологическая | discretization + control bounds | средняя | да, как distant theory branch |
| PQ conjugacy crypto | концептуальная | scalable hardness | средняя | только research seed |
| 6G non-Abelian noise | пока слабая | отсутствует строгий model | неопределённая | только примечание, не claim |

---

# 11. Что стоит включить прямо в H17-манифест

Основная H17 статья может иметь раздел:

## Beyond H17: Application Models, Not Claims

В нём фиксируются четыре типа будущего переноса.

### 11.1. Symmetry compression

\[
\text{GNN/WL},\quad
\text{quantum syndrome orbits}.
\]

### 11.2. Dynamic group-state machines

\[
\text{adaptive word tomography},\quad
\text{network streaming},\quad
\text{robotics}.
\]

### 11.3. Physical structural identity

\[
\text{PUF},\quad
\text{BIST},\quad
\text{tamper evidence}.
\]

### 11.4. Computational hardness

\[
\text{hidden conjugator / post-quantum research seed}.
\]

Эти направления показывают не «готовые продукты», а **четыре разных способа, которыми orbit-based computation может получить прикладной смысл**.

---

# 12. Общий pipeline будущих статей

Для любого направления применять одинаковую дисциплину:

\[
\boxed{
\text{DOMAIN MODEL}
\rightarrow
\text{SYMMETRY THEOREM}
\rightarrow
\text{SEPARATING PROBES}
\rightarrow
\text{SOFTWARE EXHAUSTIVE TEST}
\rightarrow
\text{RTL}
\rightarrow
\text{TARGET SYNTHESIS}
\rightarrow
\text{PHYSICAL BENCHMARK}
}
\]

До закрытия первых трёх этапов нельзя заявлять hardware advantage.

До target synthesis нельзя заявлять LUT/Fmax/power.

До physical benchmark нельзя заявлять practical superiority.

---

# 13. Проекты возможных будущих статей

## Article A
**Orbit-Separating Hardware Primitives for Equivariant Graph Learning**

Теория: finite graphlet orbit separation и WL comparison.  
Инженерия: FPGA graphlet canonicalizer/cache.

## Article B
**Discrete Lie-Group Orbit Automata for Bounded-Error Attitude Tracking**

Теория: finite \(SO(3)\) covering / Schreier graph / error bounds.  
Инженерия: fixed-state FPGA attitude automaton.

## Article C
**Symmetry-Orbit Compression for Real-Time Quantum Syndrome Decoding**

Теория: syndrome automorphism orbits.  
Инженерия: quotient decoder / FPGA latency benchmark.

## Article D
**Non-Abelian Streaming Signatures for Line-Rate Network Telemetry**

Теория: sequence-to-group map, collisions, adversarial separation.  
Инженерия: pipelined packet-metadata processor.

## Article E
**Physical Orbit Attestation: PUF-to-H17 Hardware Root-of-Trust**

Теория: stable physical feature quotient.  
Инженерия: multi-device silicon characterization.

## Article F
**Hidden Conjugators and Scalable Non-Abelian Invariants**

Теория: attack-first hardness study.  
Инженерия: только после появления credible hard family.

---

# 14. Главный вывод

H17 не должен искать одно искусственное «применение процессора».

Гораздо сильнее рассматривать его как первую полностью закрытую лабораторию принципа:

\[
\boxed{
\text{orbit structure}
+
\text{short separating observations}
+
\text{hardware realization}
}
\]

и затем переносить **сам принцип** в предметные области, где symmetry/orbit structure существует естественно.

Поэтому H17 может завершаться не списком обещаний, а картой проверяемых исследовательских программ:

\[
\boxed{
\text{математика}
\rightarrow
\text{formal application model}
\rightarrow
\text{engineering}
\rightarrow
\text{measurement}.
}
\]

Именно такой формат делает манифестную часть статьи содержательной и одновременно не смешивает доказанное с предполагаемым.
