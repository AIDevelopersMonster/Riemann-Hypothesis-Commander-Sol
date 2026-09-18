# H17-LAB-03 - шаблон отчета студента

## Титульные данные

**ФИО:**  
**Группа:**  
**Дата:**  
**Репозиторий:** https://github.com/AIDevelopersMonster/Riemann-Hypothesis-Commander-Sol  
**Commit SHA:**  
**DOI статьи:** 10.5281/zenodo.22832502

## 1. Цель работы

Сформулировать проверяемый результат.

## 2. Краткая теория

Раскрыть:

- PSL(2,7);
- A, B и simultaneous conjugacy;
- 114 generating orbits;
- robust8 words;
- class codes;
- 24-bit fingerprint;
- known erasure;
- почему distance >= 2 достаточно для одной известной erasure.

## 3. Архитектура LAB-03

Вставить block diagram:

~~~text
A,B -> membership -> 14 DAG ops -> reused classifier -> raw -> mask -> repair -> done
~~~

Объяснить, почему используется один classifier восемь раз.

## 4. Стенд

| Parameter | Value |
|---|---|
| OS | |
| CPU | |
| RAM | |
| Git | |
| Commit SHA | |
| Python | |
| Icarus | |
| VVP | |
| GTKWave | |

## 5. Методика

Привести фактически выполненные команды в порядке запуска.

## 6. Regression results

| Test | Expected | Actual | Result |
|---|---|---|---|
| smoke | PASS; 26 cycles | | |
| quick | 1796/1796; max 26 | | |
| full | 29911/29911; max 26 | | |
| waveform | exact raw/obs/rep | | |

## 7. Fingerprint 8d256a

Заполнить:

| probe | word | bits | code | class |
|---:|---|---|---:|---|
| 0 | AAB | | | |
| 1 | Abb | | | |
| 2 | AAAB | | | |
| 3 | Abbb | | | |
| 4 | AABAb | | | |
| 5 | AAbAb | | | |
| 6 | ABABB | | | |
| 7 | ABaBB | | | |

## 8. Known-erasure experiment

Для \`A=5e3b88\`, \`B=7ecc11\`, \`mode=1\`:

| Signal | Expected | Actual |
|---|---|---|
| raw | 8d256a | |
| observed | ed256a | |
| repaired | 8d256a | |
| status | 2 | |
| wait | 26 cycles | |

Объяснить marker \`111\`.

## 9. Waveform

Вставить собственный GTKWave screenshot.

Отметить:

- start;
- busy;
- op_idx 0..13;
- probe_idx 0..7;
- raw_signature;
- observed_signature;
- repaired_signature;
- fingerprint_valid;
- status;
- done.

## 10. Теория vs практика

| Theory / architecture | Observation | Match? |
|---|---|---|
| 8 probes | | |
| 14 compositions | | |
| one known erasure | | |
| exact repair | | |
| 26-cycle schedule | | |
| full golden equivalence | | |

## 11. Контрольные вопросы

1. Почему это erasure, а не unknown error?
2. Почему 111 не conjugacy class?
3. Почему 26 cycles не являются Fmax?
4. Почему simulator wall-clock не является hardware latency?
5. Что дает resource sharing?
6. Что еще требуется до заявления о реальной FPGA?

## 12. Ограничения

Отдельно перечислить:

- математически доказанное;
- проверенное RTL simulation;
- generic synthesis results из статьи;
- еще не выполненное target FPGA measurement.

## 13. Вывод

5-10 содержательных предложений.

## Приложения

- console logs;
- GTKWave screenshot;
- при наличии - собственные scripts/таблицы;
- \`git status --short\` и \`git rev-parse HEAD\`.
