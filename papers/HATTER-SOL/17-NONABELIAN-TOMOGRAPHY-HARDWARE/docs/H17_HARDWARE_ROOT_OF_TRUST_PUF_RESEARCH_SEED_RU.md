# HATTER-SOL-17 · Research Seed
## Hardware Root-of-Trust, PUF и структурная H17-диагностика

**Статус:** перспективное практико-теоретическое направление H17.  
**Не является:** готовой security architecture, доказанной post-quantum scheme или утверждением о tamper-proof FPGA.

---

## 1. Идея

Следующий физический шаг H17 можно строить не как попытку искусственно назначить математическим орбитам прикладные команды, а как аппаратную структуру, где **сам кристалл участвует в формировании входных данных**.

Physical Unclonable Function (PUF) использует неизбежные производственные вариации конкретного экземпляра кремния: различия задержек, частот, порогов и других физических параметров.

Концептуальная цепочка:

\[
\text{physical silicon}
\longrightarrow
\text{PUF measurements}
\longrightarrow
\text{stable device features}
\longrightarrow
(A,B)
\longrightarrow
\text{H17 structural state}.
\]

Тогда H17 получает не произвольно назначенные \(A,B\), а данные, связанные с физической индивидуальностью экземпляра устройства.

---

## 2. Почему формулировка «зонд сразу разрушит симметрию» слишком сильна

Нельзя заранее утверждать:

> любое вскрытие, probing, laser injection или side-channel measurement обязательно изменит H17 orbit.

Разные физические атаки ведут себя по-разному.

- Side-channel observation может извлекать информацию, почти не изменяя функциональное состояние.
- Fault injection действительно может менять delay/frequency/logic behavior.
- Laser, voltage, clock, EM или thermal perturbation могут влиять на локальные элементы, но характер изменения зависит от технологии и layout.
- PUF response сам по себе шумный и меняется с температурой, напряжением и старением.

Поэтому правильная H17-гипотеза должна быть экспериментальной:

\[
\boxed{
\text{можно ли подобрать PUF/H17 representation,}
\\
\text{где физическое вмешательство с высокой вероятностью}
\\
\text{вызывает детектируемый structural drift?}
}
\]

Это задача измерения, а не предположение.

---

## 3. PUF не должен напрямую выдавать криптографический ключ без стабилизации

PUF measurement обычно не является идеально воспроизводимым битовым словом.

Поэтому практическая цепочка должна иметь вид:

\[
\text{raw PUF}
\rightarrow
\text{reliability filtering / helper data / fuzzy extraction}
\rightarrow
\text{stable secret or feature vector}.
\]

Затем уже:

\[
\text{stable vector}
\rightarrow
(A,B)
\rightarrow
\text{H17}.
\]

Или параллельно:

\[
\text{stable PUF secret}
\rightarrow
\text{cryptographic KDF}
\rightarrow
\text{device key}.
\]

H17 здесь не обязан заменять fuzzy extractor или cryptographic KDF.

---

## 4. Более реалистичная архитектура Hardware Root-of-Trust

Разделим систему на три слоя.

### Layer A — Physical identity

\[
\text{PUF}
\rightarrow
\text{device-specific stable secret/features}.
\]

### Layer B — Structural health / attestation

\[
\text{device features}
\rightarrow
(A,B)
\rightarrow
\text{H17 orbit/fingerprint}.
\]

H17 может использоваться как структурный признак:

- нормального физического состояния;
- конкретного device class;
- конфигурации fabric;
- drift/tamper condition;
- degraded mode.

### Layer C — Standard cryptography

Для реальной post-quantum защиты ключевого обмена и подписей следует использовать стандартизованные PQ primitives.

Например:

\[
\text{PUF-derived root secret}
\rightarrow
\text{KDF}
\rightarrow
\text{keys for standard PQ protocol}.
\]

H17/PUF в этой архитектуре — **hardware trust anchor и attestation layer**, а не замена проверенной криптографии.

---

## 5. Где появляется связь с H17 conjugacy

Отдельная исследовательская ветка может использовать:

\[
(A,B)
\sim
(hAh^{-1},hBh^{-1})
\]

и hidden conjugator \(h\).

Возможная идея:

- PUF определяет device-specific frame \(h\);
- canonical H17 state задаёт structural class;
- конкретный кристалл получает representative

\[
(A',B')=(hAh^{-1},hBh^{-1}).
\]

Тогда:

\[
\text{orbit}=\text{общая structural identity},
\]

а

\[
h=\text{device-specific physical frame}.
\]

Это красивое соединение ранее выделенных компонентов:

\[
\boxed{
\text{STATE\_ID}
+
\text{FRAME\_ID}
}
\]

с физической идентичностью кристалла.

Но это пока **модель исследования**, а не security proof.

---

## 6. Что может означать «чип забывает ключ»

Корректная реализация может вообще не хранить долговременный device key в обычной nonvolatile memory.

Вместо этого:

1. после reset считывается PUF;
2. из noisy response восстанавливается stable secret;
3. из него через KDF получается working key;
4. ключ живёт только в volatile registers/secure RAM;
5. после reset/tamper policy рабочий ключ стирается;
6. при следующем доверенном запуске он заново выводится из PUF.

Таким образом физически не хранится обычная статическая копия ключа.

Но это **не означает**, что tamper автоматически делает PUF невосстановимым.

Если сам PUF и helper data остаются доступными, ключ потенциально может быть снова выведен. Поэтому secure erase, tamper sensors, access control и защита helper data остаются отдельными задачами.

---

## 7. H17 как tamper-evidence, а не magic tamper-proof

Наиболее проверяемая гипотеза:

\[
\text{enrolled physical state}
\longrightarrow
F_0
\]

и при эксплуатации:

\[
\text{current physical state}
\longrightarrow
F_t.
\]

Если:

\[
F_t\notin\mathcal A(F_0),
\]

где \(\mathcal A(F_0)\) — заранее определённое допустимое множество температурных, напряженческих и aging-вариаций, система фиксирует structural anomaly.

То есть H17 может играть роль:

\[
\boxed{\text{structured tamper/anomaly detector}}
\]

если физические features удаётся достаточно стабильно привязать к H17 states.

---

## 8. Почему это хорошо сочетается с distributed probes

Ранее в H17 была выявлена главная граница текущего one-erasure repair:

> если все восемь probes вычислены одним общим combinational blob, восстановление одной искусственно стёртой координаты имеет узкое физическое значение.

PUF-ветка даёт естественный способ physicalize probes.

Например:

\[
P_0,\ldots,P_7
\]

могут быть восемью physically separated delay/oscillator regions.

Каждый регион выдаёт independent physical feature.

Далее:

\[
(P_0,\ldots,P_7)
\rightarrow
\text{feature encoder}
\rightarrow
(A,B)
\]

или отдельные structural observations.

Тогда:

- local fault;
- local heating;
- routing disturbance;
- partial reconfiguration;
- device aging;

могут изменять не абстрактную симуляционную координату, а реально отдельный physical channel.

---

## 9. Первый честный FPGA-эксперимент

До криптографии нужен физический characterization experiment.

### Enrollment

Для каждого кристалла:

1. выбрать 8 физически разнесённых delay/oscillator structures;
2. измерить их многократно;
3. повторить измерения при разных temperature/voltage regimes;
4. оценить intra-device stability;
5. сравнить несколько экземпляров платы/device;
6. построить stable feature encoder.

### H17 mapping

Затем определить:

\[
\text{physical feature vector}
\rightarrow
(A,B)
\rightarrow
F(A,B).
\]

### Perturbation experiment

И отдельно выполнить controlled perturbations:

- clock disturbance;
- voltage variation;
- local heating/cooling;
- routing/configuration changes;
- fault injection methods, допустимые для лаборатории.

Измеряется:

\[
\Pr[
\text{structural state changes}
\mid
\text{physical perturbation}
].
\]

Параллельно измеряется false-positive rate при нормальных environmental variations.

---

## 10. Что будет считаться интересным результатом

Практически значимый результат появится, если одновременно наблюдается:

1. **device uniqueness** — разные экземпляры дают различимые physical identities;
2. **reliability** — один экземпляр стабилен в допустимом диапазоне среды;
3. **structural compactness** — H17 representation удобно описывает допустимые states;
4. **tamper sensitivity** — выбранные вмешательства вызывают measurable structural drift;
5. **low false alarm rate** — обычные temperature/voltage variations не выглядят как tamper;
6. **fault localization** — distributed probes позволяют локализовать изменившийся region;
7. **recoverable degraded mode** — known erasure одного physical probe может быть компенсирован H17 repair.

---

## 11. Где находится post-quantum часть

Нужно разделять две задачи.

### Hardware Root-of-Trust

PUF/H17 отвечают за:

- device identity;
- hardware binding;
- attestation;
- tamper evidence;
- local secret derivation.

### Post-Quantum Cryptography

Стандартизованные PQ algorithms отвечают за:

- key establishment;
- signatures;
- external cryptographic security.

Нельзя выводить post-quantum стойкость только из PUF или неабелевости H17.

Некоммутативная Conjugacy Search Problem остаётся отдельной экспериментальной research branch и требует собственного classical/quantum attack audit.

---

## 12. Возможная конечная архитектура

\[
\boxed{
\begin{array}{c}
\text{silicon process variations}\\
\downarrow\\
\text{distributed PUF probes}\\
\downarrow\\
\text{stabilization / fuzzy extraction}\\
\downarrow\\
\text{device-specific frame }h\\
\downarrow\\
(A',B')=(hAh^{-1},hBh^{-1})\\
\downarrow\\
\text{H17 structural attestation}\\
\downarrow\\
\text{PUF-derived root key}\\
\downarrow\\
\text{standard PQ cryptographic protocol}
\end{array}
}
\]

Эта схема соединяет:

- физическую индивидуальность кремния;
- H17 quotient/orbit structure;
- аппаратную диагностику;
- distributed one-erasure recovery;
- standard post-quantum cryptography.

---

## 13. Research status

На сегодняшний день H17 предоставляет:

- конечную математическую laboratory model;
- robust8 structural fingerprints;
- one-known-erasure reconstruction;
- closure-aware RTL;
- ROM-free repair;
- естественное разделение STATE_ID / representative information.

PUF/Root-of-Trust направление пока является:

\[
\boxed{
\text{EXPERIMENTAL HARDWARE RESEARCH DIRECTION}
}
\]

и должно начинаться с измерений реального silicon, а не с утверждений о security.

Если physical characterization окажется положительным, эта ветка может стать главным мостом H17:

\[
\boxed{
\text{nonabelian mathematics}
\rightarrow
\text{physical silicon identity}
\rightarrow
\text{hardware trust}
}
\]
