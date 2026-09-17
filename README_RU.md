# Commander Sol / Гипотеза Римана — замороженный исследовательский архив

> **ПРОГРАММА ЗАМОРОЖЕНА — 17.09.2026.** Научное развитие этого репозитория остановлено. `main` является каноническим архивным деревом. Слова `active`, `next`, `planned`, `in progress`, «следующий шаг», «рабочий рубеж», «будущая работа» в старых локальных файлах отражают состояние на момент их написания и не являются действующими указаниями после заморозки.

Актуальный статус программы: **[`PROGRAMME_STATUS_2026-09-17.md`](PROGRAMME_STATUS_2026-09-17.md)**. Механика консолидации веток и сохранения истории: **[`PROJECT_FREEZE_2026-09-17.md`](PROJECT_FREEZE_2026-09-17.md)**.

English navigation: [`README.md`](README.md).

## Что сохранено

Это консолидированный архив математической программы Commander Sol: RH-SOL, Prime-Successor Algebra и связанные исследования простых, FCOA, HATTER-SOL и линия Alice/Ruler. При заморозке в `main` сохранены theorem layers, исследовательские checkpoints, рукописи, публикационные метаданные, воспроизводимые эксперименты и необходимая история Git.

Сам факт наличия материала в архиве не означает, что каждая гипотеза, theorem candidate, эксперимент, roadmap или future-work note доказаны либо опубликованы. Публикационный статус определяется явной DOI/release-информацией; математический статус — соответствующим проверенным theorem/manuscript layer.

## Основные направления

| Направление | Статус | Каноническое расположение |
|---|---|---|
| RH-SOL | **FROZEN** | `programme/`, `papers/RH-SOL-*` |
| PRIME-SUCCESSOR | **FROZEN** | `papers/PRIME-*` и связанные release-материалы |
| FCOA | **FROZEN** | `papers/FCOA-*`, delegated/release-материалы |
| HATTER-SOL | **FROZEN** | `papers/HATTER-SOL/` |
| ALICE-RULER | **FROZEN** | `alice-ruler-incidence/`, `alice-ruler-edit-rigidity/` |

Подробный статус отдельных линий: [`PROGRAMME_STATUS_2026-09-17.md`](PROGRAMME_STATUS_2026-09-17.md).

## Публикации, явно зафиксированные в каноническом дереве

Эта таблица служит навигацией и не заменяет release metadata. Здесь перечислены только записи, для которых название и DOI явно присутствуют в консолидированном дереве.

| Линия | Публикация | DOI |
|---|---|---|
| RH-SOL-01 · LATTICE | *Integer-Lattice Encoding of Riemann-Zeta Argand Loops: Persistence of Dirichlet Frequencies under Binary Geometric Quantization* | `10.5281/zenodo.22060296` |
| Alice Ruler II | *Phase Rigidity in Steiner Triple Systems: Quantitative Hall–Projective Stability from Anti-Mitre Defects* | `10.5281/zenodo.22722951` |
| Alice Ruler III | *From Local Fano Phase to Partial Projective Geometry: Sharp Obstructions and Rank-2 Boolean Fiberization* | `10.5281/zenodo.22737943` |
| FCOA · Admissibility Geometry | *Reflections on Admissibility Geometry with Commander Sol: How a Partial Operation Remembers an Oriented Carrier* | `10.5281/zenodo.22129787` |
| FCOA · Value-Rigidity / Identity Digraphs | *Reflections on Value-Rigidity with Commander Sol: Two Anonymous Outputs, Identity Digraphs, and Sparse Rigid Fibers* | `10.5281/zenodo.22160014` |
| FCOA-Z · Ray to Axis | *Reflections on How a Ray Becomes an Axis: And why old operations reveal new local laws after a second direction appears* | `10.5281/zenodo.22171473` |
| HATTER-SOL-01 | *A Tea Party in the Additive-Multiplicative World with Hatter Sol: The Number Line, the Observer, and Two Operations* | `10.5281/zenodo.22639237` |
| HATTER-SOL-02 | *Two Teapots, One Cup: “Who Are You?” Among the Primes* | `10.5281/zenodo.22656414` |
| HATTER-SOL-07 | *Alice in the Land of Free Threads: Factors as Nodes and the Exact Cost of Multiplicative Splitting* | `10.5281/zenodo.22724185` |
| HATTER-SOL-10 | *Ideal Factor Networks Beyond Unique Element Factorization* | `10.5281/zenodo.22734865` |

DOI в историческом candidate-файле сам по себе не повышает статус работы, если это не подтверждается канонической release/publication-информацией.

## RH-SOL на момент заморозки

Старая карта серии сохранена как история программы, но её прежние метки `Active` и `Planned` больше не являются оперативными. На 17.09.2026: RH-SOL-01 опубликована; исследования RH-SOL-02/03/04 завершены без финальной публикационной сборки; RH-SOL-05/06 остались незавершёнными; RH-SOL-07..15 — зафиксированные направления/замыслы. См. [`programme/SERIES_MAP.md`](programme/SERIES_MAP.md).

## HATTER-SOL на момент заморозки

Нумерованные каталоги HATTER-SOL — архивные единицы программы, а не действующие ветки. Материал HATTER-SOL 01–18 сохранён в `main`. HATTER-SOL-17 заморожен в незавершённом исследовательско-аппаратном состоянии; HATTER-SOL-18 — future-work seed. Номер каталога сам по себе не означает наличие опубликованной статьи.

## Исторические статусные файлы

Локальные `STATUS.md`, `RESEARCH_TZ.md`, `DIALOGUE_TZ.md`, `PUBLICATION_CANDIDATE.md`, roadmap и старые README намеренно сохранены: это история развития программы. При противоречии используется следующий приоритет:

1. явная каноническая DOI/publication record;
2. канонические release metadata и manifests;
3. [`PROGRAMME_STATUS_2026-09-17.md`](PROGRAMME_STATUS_2026-09-17.md);
4. локальные исторические статусы — только для восстановления хронологии.

## Структура архива

```text
programme/                 история RH-SOL и замороженная карта серии
papers/                    математические и публикационные материалы
alice-ruler-incidence/     архив Alice/Ruler II
alice-ruler-edit-rigidity/ архив Alice/Ruler III и продолжения
experiments/               сохранённые вычислительные эксперименты
demos/                     демонстрации
reviews/                   рецензии и аудиты
releases/                  release/Zenodo metadata
scripts/                   воспроизводимость и служебные скрипты
```

## Правило возобновления

Если программа когда-либо будет возобновлена, исходной точкой являются `main`, `PROGRAMME_STATUS_2026-09-17.md` и `PROJECT_FREEZE_2026-09-17.md`. Нельзя автоматически продолжать старую ветку или воспринимать старую запись «следующий шаг» как текущую задачу без новой сверки.

## Авторство

Автор / владелец программы: **Alex Malachevsky**, ORCID **0009-0008-6009-3196**. Commander Sol использовался как ИИ-соавтор исследовательского процесса: генерация гипотез, вычислительный дизайн, планирование фальсификаций, помощь с кодом, литературный поиск, аудит и подготовка рукописей. Статус математических утверждений определяется их явным доказательным/вычислительным статусом.