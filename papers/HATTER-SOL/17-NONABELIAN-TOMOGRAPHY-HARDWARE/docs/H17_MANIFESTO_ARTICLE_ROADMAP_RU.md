# HATTER-SOL-17 · План манифестной статьи
## От неабелевой томографии к RTL, физическому железу и Hardware Root-of-Trust

H17 к настоящему моменту естественно разделился не на одну узкую задачу, а на три взаимосвязанных слоя:

\[
\boxed{
\text{теория}
\longrightarrow
\text{проверяемая RTL-реализация}
\longrightarrow
\text{физическое исследование}
}
\]

Поэтому основная H17-публикация может быть построена как **манифест + reproducible laboratory**, а не как статья, которая преждевременно объявляет конкретное промышленное применение.

---

## I. Теоретическая часть: что уже получено

Зафиксировать H17-01 — H17-08:

- 114 generating simultaneous-conjugacy orbits;
- robust8 one-erasure code;
- optimality/minimality results;
- depth-5 separator structure;
- structural PSL classifier;
- ROM-free repair;
- optimal 14-composition word DAG;
- closure-aware hardware classification.

Основная идея:

> математическое описание объекта само приобретает redundancy, пригодную для аппаратного восстановления одной известной structural erasure.

---

## II. Теоретическая часть дальнейшего развития

### A. Adaptive Word Tomography

Вместо восьми неизменных probes следующее слово выбирается по предыдущим class observations.

Цель:

\[
\text{меньше class queries}
\]

при сохранении точной идентификации orbit.

### B. Nielsen Dynamics

Исследовать действия преобразований:

\[
(A,B)\mapsto(B,A),
\]

\[
(A,B)\mapsto(A^{-1},B),
\]

\[
(A,B)\mapsto(AB,B)
\]

на 114-orbit state space.

Получаем переход от статической tomography к:

\[
\boxed{\text{nonabelian dynamical tomography}}.
\]

### C. Representative-sensitive layer

Исследовать расширение:

\[
\mathrm{STATE\_ID}
+
\mathrm{FRAME\_ID}
\]

для сохранения информации, которую quotient currently discards.

### D. Cryptographic research seed

Исследовать scalable nonabelian families и hidden conjugator problem только как attack-first research hypothesis, без заявления post-quantum security.

---

## III. Практическая RTL-часть

Статья должна включать воспроизводимую инженерную цепочку:

\[
\text{golden model}
\rightarrow
\text{Verilog/VHDL}
\rightarrow
\text{Icarus tests}
\rightarrow
\text{generic synthesis}
\rightarrow
\text{target FPGA}.
\]

LAB-01 показывает sequential table-driven reference.

LAB-02 показывает pure-RTL closure-aware + ROM-free construction.

Важно явно разделить:

- simulator latency;
- RTL clocks;
- generic synthesis cells;
- target-specific LUT/FF/BRAM/Fmax;
- measured physical performance.

Никаких FPGA performance claims до target implementation.

---

## IV. Физическая модель отказа

Текущий repair работает для:

\[
\boxed{\text{one known fingerprint-coordinate erasure}}.
\]

Он не восстанавливает:

- \(A\);
- \(B\);
- произвольный внешний sensor;
- unknown corrupted coordinate;
- общий fabric failure.

Следующий физический experiment:

\[
(A,B)
\rightarrow
8\ \text{independent probe engines}
\rightarrow
8\ \text{valid/data channels}
\rightarrow
\text{repair}.
\]

Это превращает математическое erasure в physical/logical channel failure.

---

## V. Определение железа через эксперимент

Не выбирать FPGA «по привычке».

Сначала установить требования:

- необходимое число LUT/FF;
- необходимость BRAM;
- routing/floorplanning control;
- возможность physically separated regions;
- clocking;
- partial reconfiguration, если понадобится;
- наличие удобных delay/oscillator primitives для PUF experiments;
- доступность open или reproducible synthesis flow;
- измерительное оборудование.

После этого выбирать реальную board/family.

---

## VI. Hardware Root-of-Trust / PUF

Новая практико-теоретическая ветка:

\[
\text{silicon variability}
\rightarrow
\text{PUF}
\rightarrow
\text{stable device features}
\rightarrow
(A,B)
\rightarrow
\text{H17 structural attestation}.
\]

Задача не в лозунге «вскрытие разрушает orbit», а в экспериментальном вопросе:

\[
\boxed{
\text{может ли controlled physical perturbation}
\\
\text{вызывать надёжно детектируемый H17 structural drift?}
}
\]

Если да, H17 получает физический смысл как:

- structural BIST;
- device attestation;
- tamper evidence;
- degraded-mode repair для distributed probes.

---

## VII. Post-Quantum boundary

Статья должна провести жёсткую границу.

PUF/H17:

- hardware identity;
- root secret derivation;
- structural attestation;
- anomaly detection.

Standard PQ cryptography:

- KEM;
- digital signatures;
- external secure protocol.

Experimental nonabelian cryptography:

- отдельная research branch;
- обязательный classical/quantum attack analysis;
- никаких security claims только из-за noncommutativity.

---

## VIII. Главный тезис статьи

H17 интересен не потому, что уже найдено одно коммерческое устройство.

Его ценность в сквозном эксперименте:

\[
\boxed{
\text{абстрактная конечная неабелева структура}
\rightarrow
\text{доказанная tomography}
\rightarrow
\text{оптимизированная Boolean hardware}
\rightarrow
\text{измеримый физический эксперимент}
}
\]

Это позволяет одной работе честно показать весь путь:

1. доказать математическое свойство;
2. превратить его в RTL;
3. увидеть, какие hardware resources удаляет theorem;
4. определить реальную fault model;
5. выбрать FPGA по требованиям;
6. проверить, остаётся ли structural idea содержательной на физическом silicon.

---

## IX. Рабочее название

### RU

**HATTER-SOL-17: От неабелевой томографии к математическому процессору, FPGA и Hardware Root-of-Trust**

Подзаголовок:

**Манифест проверяемого пути от групповых инвариантов к физическому кремнию**

### EN

**HATTER-SOL-17: From Non-Abelian Tomography to a Mathematical Processor, FPGA, and Hardware Root-of-Trust**

Subtitle:

**A Manifesto for a Verifiable Path from Group Invariants to Physical Silicon**

---

## X. Publication rule

В основной статье нужно строго маркировать уровень каждого утверждения:

- **THEOREM** — доказано математически;
- **EXHAUSTIVE COMPUTATION** — проверено полным конечным перебором;
- **RTL VERIFIED** — проверено симуляцией;
- **GENERIC SYNTHESIS** — получено без target device;
- **TARGET SYNTHESIS** — получено для выбранного FPGA;
- **MEASURED HARDWARE** — измерено на физической плате;
- **RESEARCH HYPOTHESIS** — направление дальнейшего исследования.

Так H17 может быть одновременно смелой манифестной работой и технически строгим документом.
