# H17-LAB-03 - краткая карта преподавателя

## Учебная цель

Связать четыре языка одного объекта:

~~~text
finite group theory -> coding distance -> RTL microarchitecture -> waveform evidence
~~~

## Рекомендуемый маршрут на 2 занятия

### Занятие 1 - 90 минут

- 15 мин: PSL(2,7), orbit, robust8;
- 20 мин: установка/проверка стенда;
- 15 мин: smoke;
- 15 мин: quick;
- 15 мин: fingerprint 8d256a;
- 10 мин: known erasure.

### Занятие 2 - 120 минут

- 20 мин: 14-operation DAG;
- 20 мин: sequential classifier reuse;
- 20 мин: full regression;
- 30 мин: VCD/GTKWave;
- 20 мин: theory-vs-practice table;
- 10 мин: claim boundaries.

## Reference outcomes

~~~text
quick: 1796/1796 PASS; max_wait_cycles=26
full : 29911/29911 PASS; max_wait_cycles=26
wave : 8d256a -> ed256a -> 8d256a; status=2
~~~

Reference wall-clock times are not grading thresholds.

## Оценивание

| Component | Points |
|---|---:|
| reproducible setup | 15 |
| regression | 20 |
| theory | 20 |
| waveform | 20 |
| theory vs practice | 15 |
| claim discipline | 10 |

## Типовые неверные формулировки

- "Восстановили 12.5% любых данных" - неверно.
- "111 - седьмой класс" - неверно.
- "26 cycles = 26 ns" - неверно без target clock.
- "29,911 PASS доказывает работу FPGA" - неверно.
- "LAB-03 быстрее LAB-01 на FPGA в 1663/26 раз" - не доказано.

## Проверка самостоятельности

Требовать:

- commit SHA;
- версии tools;
- собственное wall-clock measurement;
- собственный GTKWave screenshot;
- ручное декодирование 8d256a;
- объяснение одного несоответствия между simulator metric и physical hardware metric.
