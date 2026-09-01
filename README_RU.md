# Размышления о гипотезе Римана с Commander Sol

**Серия:** *Размышления о гипотезе Римана и живучести логарифмических арифметических структур с Commander Sol*.

Репозиторий предназначен для воспроизводимой серии вычислительных исследований: Argand-петли дзета-функции Римана, бинарное кодирование целочисленной решёткой, сохранение частот Дирихле, sampling/aliasing, нулевые модели и оценка того, сколько арифметической информации переживает нелинейную геометрическую квантизацию.

## Первая публикация

**RH-SOL-01 · LATTICE**  
*Integer-Lattice Encoding of Riemann-Zeta Argand Loops: Persistence of Dirichlet Frequencies under Binary Geometric Quantization*  
Автор: **Alex Malachevsky**  
ORCID: **0009-0008-6009-3196**  
Zenodo DOI: **10.5281/zenodo.22060296**

## Дополнительные опубликованные математические ветви

### FCOA · Геометрия допустимости

**«Размышлизмы о геометрии допустимости с Commander Sol: как частичная операция запоминает ориентированный носитель»**  
Zenodo DOI: **10.5281/zenodo.22129787**  
GitHub-компаньон: [`papers/FCOA-ADMISSIBILITY-GEOMETRY/`](papers/FCOA-ADMISSIBILITY-GEOMETRY/)  
Интерактивная демонстрация: [`demos/fcoa-domain-compilation/`](demos/fcoa-domain-compilation/)

Основная цепочка:

`M0 -> G1 -> G2`

и центральный механизм:

`отношение -> область частичной операции -> восстанавливаемая структурная память`.

### FCOA · Ценностная жёсткость / Identity-орграфы

**«Размышлизмы о ценностной жёсткости с Commander Sol: два анонимных выхода, identity-орграфы и разреженные жёсткие волокна»**  
Zenodo DOI: **[10.5281/zenodo.22160014](https://doi.org/10.5281/zenodo.22160014)**  
GitHub-компаньон: [`papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/`](papers/FCOA-VALUE-RIGIDITY-IDENTITY-DIGRAPHS/)

Ключевые результаты:

`|O|=1 -> VRI=1`, а при `|O|=2` достижим абсолютный максимум `VRI=n!`; задача о минимальном числе специальных клеток сводится к классическому экстремальному `m(n)` для identity digraph, для которого получены точная конечная формула, второй асимптотический член и фазовый закон последнего слоя.

## FCOA-пакеты на финальной стадии Zenodo

### FCOA-Z · Луч в ось / локальная дифференциация закона

**«Размышлизмы о том, как луч становится осью: И почему старые операции после появления второго направления обнаруживают новые локальные законы»**  
Zenodo DOI: **[10.5281/zenodo.22171473](https://doi.org/10.5281/zenodo.22171473)**  
GitHub-компаньон: [`papers/FCOA-Z-RAY-AXIS/`](papers/FCOA-Z-RAY-AXIS/)

Пакет v1.1 теоремно завершён, прошёл hostile audit и PDF preflight; DOI внесён в публикационные материалы.

### FCOA-Z · Предписанная стабилизаторная опора

**«Предписанная стабилизаторная опора в фиксированно-носительной ориентированной алгебре: Wreath-когерентность, сжатие разбиений и точное орбитальное разделение»**  
Английская версия: **Prescribed-Stabilizer Support in Fixed-Carrier Oriented Algebra: Wreath Coherence, Partition Compression, and Exact Orbital Separation**  
GitHub-компаньон: [`papers/FCOA-Z-PRESCRIBED-STABILIZER-SUPPORT/`](papers/FCOA-Z-PRESCRIBED-STABILIZER-SUPPORT/)  
Zenodo DOI: **ожидается после депозита**

Ключевые результаты:

- точная цена global coherence: `b(b-1)t`;
- точная цена произвольной partition+phase coherence: `t sum_j n_j(n_j-1)`;
- точная partition-only редукция `t^2 d(P)`;
- Partition-Overgroup Dichotomy;
- Macro-Mover Double-Coset Lemma;
- точная Orbital XOR-Separation Program для произвольного конечного типа разбиения;
- явная ресурсная немонотонность между partition-only и phase-coherent памятью.

Proof audit, literature audit, reproducible build и визуальная проверка PDF завершены. Exact verifier проверен прямым перебором для всех integer partitions при `2 <= b <= 7`: 43 типа разбиений, 1468 invariant orbital unions, итог **ALL PASS**. Публикационный пакет готов к Zenodo; после выдачи DOI его нужно внести в этот README и release metadata ветки.

## Принцип серии

Каждая ветка должна иметь точное определение объекта, гипотезу, полный upstream-конвейер, нулевые/суррогатные контроли, воспроизводимые рисунки и таблицы, а также фиксацию отрицательных результатов.

Карта серии: [`programme/SERIES_MAP.md`](programme/SERIES_MAP.md).

## Статус FCOA-публикаций

- 27.08.2026 — **FCOA · Геометрия допустимости**, Zenodo DOI **10.5281/zenodo.22129787**.
- 29.08.2026 — **FCOA · Ценностная жёсткость / Identity-орграфы**, Zenodo DOI **10.5281/zenodo.22160014**.
- 30.08.2026 — **FCOA-Z · Луч в ось / локальная дифференциация закона**, DOI **10.5281/zenodo.22171473**, финальный пакет подготовлен.
- 01.09.2026 — **FCOA-Z · Предписанная стабилизаторная опора**, research/PDF/source thresholds пройдены, exact verifier **ALL PASS**, готово к Zenodo, DOI ожидается.
